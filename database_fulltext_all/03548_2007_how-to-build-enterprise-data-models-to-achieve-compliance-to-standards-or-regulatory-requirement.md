---
otero_id: 3548
otero_key: "DR9T6Z6T"
title: "How To Build Enterprise Data Models To Achieve Compliance To Standards Or Regulatory Requirements (and share data)."
authors: "Henry Kim; Mark Fox; Arijit Sengupta"
year: "2007"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00115"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 8 | Issue 2

Article 5

2-3-2007

# How To Build Enterprise Data Models To Achieve Compliance To Standards Or Regulatory Requirements (and share data).

Henry Kim

Mark S. Fox

Arijit Sengupta

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

How To Build Enterprise Data Models To Achieve Compliance To Standards Or Regulatory Requirements (and share data).

Henry M. Kim
Schulich School of Business
York University
hmkim@schulich.yorku.ca

Mark S. Fox
Department of Mechanical and Industrial Engineering
University of Toronto
mark.fox@utoronto.ca

Arijit Sengupta
Information Systems
Kelley School of Business, Indiana University

## Abstract:

Sharing data between organizations is challenging because it is difficult to ensure that those consuming the data accurately interpret it. The promise of the next generation WWW, the semantic Web, is that semantics about shared data will be represented in ontologies and available for automatic and accurate machine processing of data. Thus, there is inter-organizational business value in developing applications that have ontology-based enterprise models at their core. In an ontology-based enterprise model, business rules and definitions are represented as formal axioms, which are applied to enterprise facts to automatically infer facts not explicitly represented. If the proposition to be inferred is a requirement from, say, ISO 9000 or Sarbanes-Oxley, inference constitutes a model-based proof of compliance. In this paper, we detail the development and application of the TOVE ISO 9000 Micro-Theory, a model of ISO 9000 developed using ontologies for quality management (measurement, traceability, and quality management system ontologies). In so doing, we demonstrate that when enterprise models are developed using ontologies, they can be leveraged to support business analytics problems - in particular, compliance evaluation - and are sharable.

Key Words: enterprise modeling, ontologies, quality management, ISO 9000, regulatory requirements

# How To Build Enterprise Data Models To Achieve Compliance To Standards Or Regulatory Requirements (and share data).

## Introduction

A (computational) enterprise (data) model $^{1}$ is “a computational representation of the structure, activities, processes, information, resources, people, behavior, goals, and constraints of a business, government, or other enterprise” [Fox and Gruninger, 1998]. The model can be a conceptual artifact resulting from an analysis phase. It can also be logical, resulting from design; and physical, resulting from implementation. It is a broad term that encompasses the models of the following: General Enterprise Reference Architecture and Model (GERAM) applicable to all industries [Kosanke et al., 1997; Tølle and Bernus, 2003; Vernadat, 1996]; Partial Enterprise Reference Architecture and Model (PERAM) applicable to a few industries; or instantiated models applicable to all or parts of one enterprise.

Enterprise data models underlie, for example, all Enterprise Resource Planning (ERP) and supply chain management applications. However, effective use of data models used by different applications within the same organization, let alone between organizations, is an issue of concern. The Internet provides a ubiquitous infrastructure, though how best to use this infrastructure for data model use is still an open question.

In this paper, we postulate and demonstrate the following about enterprise data models: When they are developed using computational ontologies, they: 1) can be leveraged to support business analytics problems, in particular, compliance evaluation (to e.g. ISO 9000 [ISO, 2000] or Sarbanes-Oxley [Sarbanes-Oxley, 2002]) and 2) are easier to share, increasingly and especially over the Web.

A (computational) ontology $^{2}$ is a data model that “consists of a representational vocabulary with precise definitions of the meanings of the terms of this vocabulary plus a set of formal axioms that constrain interpretation and well-formed use of these terms” [Campbell and Shapiro, 1995]. Because precise definitions and axioms exist, proper interpretation of data results from automated theorem proving (inference). Hence, correct interpretation by a computer—i.e. computational inference, not a referential theory of semantics—or a decision maker who did not develop the definitions and axioms is possible. Therefore, ontologies are the base for presenting the second postulate of this paper. Furthermore, ontologies are a fundamental base for the nascent semantic Web [Berners-Lee et al., 2001], an enhanced Web wherein software agents conduct commerce automatically over the Web by applying business rules and using business vocabulary, both represented in Web-sharable ontologies. Moreover, an ontology-based enterprise model’s inference capability is particularly suitable for business analytics requiring evaluation of compliance: A requirement can be modeled as a theorem, and if the theorem is inferred to be true, the model shows that the enterprise complies with that requirement. Hence, ontologies are the base for presenting and demonstrating the first postulate of this paper.

Ontologies constitute re-useable, sharable building blocks with which to build enterprise models [Grosof and Morgenstern, 1992]. The presentation of a methodology entailing development of building block ontologies herein provides both a partial blueprint and a set of re-useable pieces for those interested in developing enterprise models for compliance evaluation ( $1^{st}$ postulate) or sharing ( $2^{nd}$ postulate).

In this paper, we detail an ontology-based enterprise data model for compliance evaluation. We use the model, called the TOVE ISO 9000 Micro-Theory, to evaluate how the quality management business processes and practices of enterprises comply with against the ISO 9000 standards. In Section II, we survey and analyze the quality management, enterprise modeling, and ontology fields. In Section III, we detail the modeling methodology and quality management ontologies that serve as building blocks for the model. Section IV details the TOVE ISO 9000 Micro-Theory, and Sections V and VI present the competency and generality of the ontology respectively. Finally in Section VII we offer concluding remarks as well as discussions of how this work can be extended to provide compliance evaluation over the semantic Web.

## Literature Review

The business value of compliance to business practices and processes requirements is well-acknowledged: In many industries, compliance to ISO 9000 is a pre-requisite for commerce, and U.S. corporations must, by law, comply with the

![](/api/attachments/DR9T6Z6T/fulltext/images/07a72c980662888a1de5b5432b55f7e238e1f887a8e22291d460e96a1781d455.jpg)

Sarbanes-Oxley Act. However achieving compliance is expensive; ISO 9000 compliance serves as a good example. A study of small- to medium-sized firms showed average cost for achieving compliance to be around \$110,000, and completion time around 16 months [Walters et al., 2000]. In addition, ISO 9000 requirements are subjectively and vaguely stated, and hence there is great reliance on auditor interpretation, which varies widely [Seddon, 1997]. To some extent, this is an unavoidable side effect of the fact that the ISO 9000 aims to be applicable to all industries, from manufacturing to services. In order to do this practicably, the standard's developers chose to state the requirements generally, to be applied specifically by auditors with industry and domain expertise [ISO, 2000]. However, not all requirements require subjectivity in interpretation; some can be transformed into those that can be objectively verified if reasonable assumptions are made. We consider whether objective verification can be inferred from data already stored in the enterprise's computers. That is, can an existing enterprise data model be leveraged for automated compliance evaluation to requirements such as those of the ISO 9000? If so, what are the desirable characteristics of this model?

After all, though it would be quite inexact to estimate the percentage of requirements that are objectively verifiable, it has been stated that compliance auditing is equal parts describing the business process, referencing the procedure manual, and exhibiting evidence in documented, objectively verifiable records [Seddon, 2001]. A computer program can verify whether some artifact of the enterprise is described (i.e. modeled) or not in the data model, but it cannot determine whether a manual is referenced properly or whether evidence is sufficient. Put another way, the program can verify that a receiving inspection manual exists; but a human is better at validating whether the manual is written properly or whether there is sufficient evidence that it is followed properly.

Enterprise data models are most prevalently used in software such as ERP applications that support day-to-day operations. These models represent the enterprise, and hence describe the enterprise. However, a data model of ISO 9000 would not so much be a description of the enterprise as it would be an evaluation of the enterprise. So, it would evaluate descriptive models. The first desirable characteristic of a compliance data model, then, is that it be evaluative, and can be applied to a descriptive enterprise data model. A descriptive model then can be leveraged by different types of evaluative models. Or conversely, one evaluative model may be applicable to different descriptive models.

Evaluative data models for organizational analysis and design such as an ISO 9000 evaluator or workbench or “flight simulator” for Business Process Re-engineering (BPR) [Hammer, 1990] are generally implemented as relational databases or expert systems, and represent evaluations as queries whose answers reveal insights about the modeled enterprise. According to Fox and Gruninger [1998], there are three types of queries: factual, expert, and common-sense.

SQL queries are factual because they retrieve information explicitly represented in an instantiated data model; expert systems queries are “expert” because they entail applying complicated, idiosyncratic rules to the instantiated model to automatically deduce facts like an expert. Common-sense systems represent fundamental, general concepts (common-sense) of a domain such that the system is able to answer less general queries about an instantiated model as deductions using common-sense rules.

The latter two query types have a rule-base that is separate from the data-base, where the rule-base in and of itself is conceptually meaningful, not just convenient for implementation. That is, an SQL query implements a procedure; expert and common-sense rules represent knowledge. This is a key reason why a rule-based approach is superior as the basis for an evaluative model. However, a data-based approach is computationally more efficient and understood by a wider audience. For the purpose of explicating desirable characteristics of a data model, not necessarily an implementation of it, it is fair to assume that the capability to represent a compliance standard as rules is more important than these drawbacks.

These rules can conveniently be used to answer queries if they are represented formally; i.e. they are represented in a language like mathematics or first-order logic, which has restrictive syntax and semantics and, hence, supports automated theorem proving or inference. Quite naturally, then, as long as the models are represented formally, the evaluative model can take the form of a rule-base; the descriptive model, a data-base. Therefore, the second desirable characteristic of a compliance data model is that it be represented in a formal language.

One rule-based type, the expert system, is very good at solving a bounded set of problems, challenging as these may be, but not useful beyond its narrow scope - often one specific problem for one specific enterprise [Fox, 1990]. However, it is advantageous for a data model to not preclude a widened scope [Fox, 1992]. For example, parts of the model may be re-used to build another model for a different set of problems, or the model may be shared with those performing compliance evaluations even if they did not develop it.

So the third desirable characteristic of a compliance evaluation model is that it be re-useable and sharable.

Therefore, developing enterprise models for compliance evaluation entails 1) evaluative modeling coupled with descriptive modeling; 2) formal representation; and 3) re-useability and shareability. It is constructive here to commit to an exemplar standard and compare existing data models of that standard as per the three characteristics. From here on, ISO 9000 [ISO, 1994] $^{3}$ is so committed.

Let's explore candidate works that may potentially satisfy the three above-mentioned characteristics. One type is ERPs, which have systematically developed enterprise data models. These models cannot generally be considered formal models. That is, the models are classically designed using ER or object-oriented models and data dictionaries, but the terms in the data dictionary are not generally defined in a language that can be considered a true formal language. Let's consider SAP R/3 $^{TM}$ . There is, for instance, no SAP R/3 $^{TM}$ module that evaluates the ISO 9000 compliance of the organization for which an enterprise data model exists. It can be argued that such a module also does not exist for other ERP data models. The SCOPE [Hausen, 1998; McCall et al., 1977] project describes and evaluates quality of the "products" of software engineering such as programs, specifications, requirements, and documentation, and the software engineering processes that produce them. SCOPE's models are formal, and it is possible to evaluate them versus a few ISO 9001 requirements that have been customized to describe software development only [Welzel, 1993]. However the focus of SCOPE is not on representing ISO 9000 requirements, but rather on formally representing a common sense of software production and testing.

There are many applications like statistical quality control tools that help organizations satisfy some portion of ISO 9000 requirements [QualityDigest, 2000]. Many tools that assist more directly in ISO 9000 compliance evaluation only provide checklists, wherein questions posed to users are nearly verbatim, sentence-by-sentence dissections of ISO 9000 requirements. One tool that did push some slight, objective audit decision-making onto a computer was The Strategic Analyst™ [ODS, 1998], an expert system for internal, informal ISO 9000 compliance auditing. It offered some 500 questions, where questions asked of the user depended on answers given to previous questions. It still employed a checklist approach, since its key input source was the user, not a descriptive model of the enterprise to be analyzed.

There are also GERAMs, which contain general data models of ISO 9000 enterprise facets such as quality policy and procedures [Bernus, 2003; Zelm and Kosanke, 1997]. A descriptive model of an ISO-9000 compliant organization can be developed using these models, but these GERAMs do not offer a concomitant evaluative model for ISO 9000 compliance.

Most of these models apparently do not exhibit all three desirable characteristics. And even though SCOPE's model does, it is not meant for wider scope: general compliance evaluation. So then, what model is, and also exhibits the desirable characteristics?

Recall that expert and common-sense systems support the combination of evaluative and descriptive models, and they are formal. Though expert systems are not re-useable and sharable, common-sense models are. So common-sense models have the potential to exhibit all desirable characteristics. Common-sense models of the natural world include those of time [Allen, 1983], space [Kautz, 1985], materials [Hayes, 1985], causality [Reiger and Grinberg, 1977], activity [Sathi et al., 1985], and qualitative physics [Kuipers, 1986]. These are general concepts, so parts of these models can be re-used to develop more specific models about the world. When common-sense models are implemented, they are generally implemented as computational ontologies (e.g. Lenat, 1995, Storey et al., 1997). Not all ontologies are common sense models, however.

For the specific ISO 9000 compliance data model, the most general common-sense model required is that of the enterprise i.e. models about organizational structures, people, and their roles, and about activities and resources. A model more specific than a common-sense model of the enterprise, but still more general than ISO 9000 rules, is a common-sense model about quality within the enterprise. That is, there need to be general enterprise ontologies that form the building blocks for quality management ontologies (which are less general or fundamental to the function of an enterprise than, say, roles, activities, and resources), which in turn form building blocks for the desired ISO 9000 compliance data model.

The Enterprise [Uschold et al., 1998] and TOVE (Toronto Virtual Enterprise) [Fox, 1992] projects provide enterprise ontologies. In TOVE, ontologies considered fundamental to describe any enterprise are called the TOVE Core Ontologies. These are ontologies of activity, state, causality, and time, collectively called the activity-state ontology [Grüninger and Fox, 1994]; a resource ontology [Fadel et al., 1994]; and an organizational structure ontology [Fox et al., 1994]. Using these core ontologies, ontologies for measurement [Kim and Fox, 2002], traceability [Kim et al., 1999], and quality management systems, collectively called the TOVE Ontologies for Quality Modeling (aka quality ontologies), are developed [Kim et al., 1999].

Representations of the ISO 9000 compliance data model could very naturally be organized into the "ISO 9000 ontology." However, in the spirit of the largest ontology development project ever, the Cyc project [Lenat and Guha, 1990], subtly, this would not be quite right. That project differentiates between an ontology and a micro-theory. Operationally the difference is mostly in name only: A micro-theory is developed using ontologies similar to the way more specific ontologies (e.g. quality) are developed from more general ontologies (e.g. activity-state). However conceptually there is an important distinction. According to the principle of minimal ontological commitment [Newell, 1982], an ontology of a domain should contain only those representations required to minimally describe that domain. A micro-theory, on the other hand, is a formal model of knowledge required to solve a problem in a domain or to describe a subset of the domain in detail. It is very important to state this distinction and label the compliance data model as the ISO 9000 Micro-Theory. Figures 3 and 4 should demonstrate this distinction. By explicating this distinction, it is clearly indicated to the research and industry communities that the quality ontologies are descriptive models that do not violate the principle of minimal ontological commitment. It also indicates that the ISO 9000 Micro-theory does violate the principle. Thus it is a clear signal to those who want to use and extend this work when the quality ontologies should be referred and when the ISO 9000 Micro-Theory should be used.

The TOVE ISO 9000 Micro-Theory then can be stated as an evaluative data model for ISO 9000 compliance. This model can be applied to a descriptive model of a specific enterprise, which is developed using TOVE Core and quality ontologies. Both the evaluative and descriptive models are formal, re-useable, and sharable because they are built using ontologies. So the ISO 9000 compliance data model exhibits all three desired characteristics and serves as a blueprint for other ontology-based enterprise models for compliance evaluation. In the next section, we describe the methodology used to develop the micro-theory and required ontologies, as well as the quality ontologies.

## Methodology and Quality Ontologies

## Methodology

In TOVE modeling, model builders develop general ontologies, and users populate models of their specific enterprises by instantiating terms from these ontologies. TOVE Core Ontologies are comprised terms like organization(O) and activity(A), where $<O>^{4}$ and $<A>$ are variables; and users instantiate (populate) these terms with instances such as organization(abc) and activity(painting). Such terms are used in TOVE quality ontologies to, for example, formally define measure as a primitive measure activity or an activity for which all its sub activities are primitive measure activities. This definition is expressed as a first-order logic expression as follows:

$$
\begin{array}{l} \forall A \forall s [ h o l d s (\text {primitive\_measure} (A), s) \lor \forall A o (h o l d s (\text {has\_subactivity} (A, A o), s) \to \\ h o l d s (\text {measure} (A o), s)) \to h o l d s (\text {measure} (A), s) ]. \end{array}\tag{1}
$$

Quality ontologies' definitions like these are then applied to deduce quality-related facts about the enterprise that answer important queries. These definitions can be composed to define TOVE ISO 9000 Micro-Theory expressions. For example, the definition for ISO 9001 4.10.1 compliant is expressed in terms of activity(A) and measure(A). Definitions like these are then composed to deduce the answer to the key question: "Is the enterprise compliant to ISO 9000?" we illustrate the layering of these models below.

![](/api/attachments/DR9T6Z6T/fulltext/images/13fc2fcc5f6f2935b71c4f1bb4b47f4f536e071252a43766a93de22efc320a01.jpg)

![](/api/attachments/DR9T6Z6T/fulltext/images/579f0781005c4252456a030b58fe030b9cbb028041eee0c9837d88943e93d365.jpg)  
Figure 1: Model Architecture for TOVE Modeling  
Additionally, we provide an overview of the methodology [Gruninger and Fox, 1995] used to engineer TOVE ontologies and micro-theories.

![](/api/attachments/DR9T6Z6T/fulltext/images/7ac3c6d4a74a30d26006c6bdf791dc21814d1aea1a26e5d12b6525d6770c5199.jpg)

A Motivating Scenario is a detailed narrative about a specific enterprise, where emphasis is placed on problems it faces or tasks it needs to perform. Ultimately, an application uses an ontology-based model of the specific enterprise to solve the problems or perform the tasks. When the Motivating Scenario is analyzed, general concepts independent of reference to a specific enterprise are abstracted. These concepts can be characterized as questions stated using informal, non-ontology terminology. These Informal Competency Questions denote capability or competency: The more interesting or difficult the questions are to answer, the more competent the ontology or micro-theory used to answer them needs to be. If a general enterprise model (a GERAM) is constructed using this ontology, and populated with facts about a specific enterprise, querying the populated model will result in answers to these questions.

Terms with which such queries can be composed, and those with which the query terms may be defined comprise the Terminology (object or data model) of the ontology or micro-theory. The queries, re-stated using the terminology, are called Formal Competency Questions. Answers to these questions can be automatically deduced if axioms (logical or semantic model) that define and constrain the terminology are developed in a formal language such as first-order logic. These deductions constitute a Demonstration of Competency, and can be implemented in a programming language like Prolog. Recall that one of the key design criteria for developing this model is the shareability and re-useability of ontology representations. Fox et al. list the key measurement criteria for evaluating the goodness of an ontology. Of these the most appropriate measure of shareability and re-useability is generality: "To what degree is the representation shared between diverse activities such as design and troubleshooting, or even design and marketing" [Fox et al., 1993]? A step in the methodology entails applying a technique called representational reduction to measure or provide a demonstration of generality.

![](/api/attachments/DR9T6Z6T/fulltext/images/66c52bbd6dbb161cd9a8b9df85e4e1d5f1394e297ca120d479586a15ec59de9c.jpg)

The demonstrations of competency and generality are operational verifications of the goodness of an ontology, and the conventional wisdom of the ontology community has generally accepted these and other verification techniques [Gómez-Pérez et al.; 2004, Uschold and Gruninger, 1996]. However, of late, some works have also started to validate ontology representations—i.e. whether the terms and definitions are reasonable, complete, and accurate—via empirical means [Burton-Jones et al., 2002, Storey et al., 2005]. Admittedly, this paper is like conventional ontology, insofar as we only perform very limited validation via ad hoc interviews (as opposed to a more systematic discussion with panel of experts a la Purao and Storey [2005] with ISO 9000 auditors and ISO 9000 experts at the companies that provided the setting for the motivating scenarios. We recognize this limitation, but we emphasize that such verification is enough to fulfill this paper's purpose of demonstrating the viability of ontology-based compliance evaluation.

## TOVE Core Ontologies

The core ontologies are the first used to define ISO 9000 Micro-Theory representations. The situation calculus [McCarthy and Hayes, 1969] is a first-order language for representing dynamically changing worlds in which each perturbation to the modeled world changes the model from one situation to another. This language is the foundation for the core ontologies. A term, whose truth value changes over situations, is called a fluent <f>, which is said to hold (is true) in a given situation <s>. This is expressed as holds(f,s). All ontology terms are fluents unless otherwise stated.

The following are some of the key modeled concepts: resource(R) like 'arm assembly', tru(Rt) (Traceable or Track-able Resource Units) like 'batch 11 of arm assemblies', activity(A) like 'assemble arm assembly batch 11', organization\_agent(O) like 'Gary the assembler' or 'G11, the intelligent robot.' An activity may consume a tru (consume\_res\_tru(A,Rt)) of one resource to produce trus of another resource (produce\_res\_tru(A,Rt)), and may use trus of yet another resource (use\_res\_tru(A,Rt)), which are not consumed and are available for use after an activity's execution. An activity may have sub-activities <Ao> (has\_subactivity(A,Ao)), but a primitive activity (primitive\_activity(A)) does not.

## TOVE Ontologies for Quality Modeling

Measurement. Measurement concepts belong in the quality ontologies because before quality can be evaluated, controlled, and managed, it must first be measured. The gist of this ontology is the following: An attribute that bears on quality, measured attribute <At> of a tru <Rt>, is deemed to be a conformance or nonconformance point <X> at time <Tp> (conformance\_pt(X,Rt,At,Tp), nonconformance\_pt(X,Rt,At,Tp)) as a result of a measure activity.

Traceability. Traceability belongs in the quality ontologies because when measurement identifies a problem, traceability is the primitive analysis capability required to solve it. The gist of the ontology is the following: A path $<\mathrm{L}>$ from any pair of trus, $<\mathrm{Rt}_{1}>$ and $<\mathrm{Rt}_{2}>$ , in the production chain from output resource unit (finished product) to intermediate resource unit (work-in-process) to input resource unit (raw material) can be found via a tru trace $(\mathrm{tru\_trace}(L,Rt_{1},Rt_{2}))$ . An activity trace $(\text{activity\_trace}(L,A_{1},A_{2}))$ traces the chain between activities.

Quality Management System. Quality Management System (QMS) concepts belong in the quality ontologies, since there must be a QMS in place to consistently ensure that quality problems are properly measured, traced, and analyzed. The gist of the ontology is the following: Quality-related roles are assigned via quality procedures that are documented by quality plans, and quality evidence documented by quality records expresses whether and how these procedures were followed.

## Application to the Micro-Theory: Agent Constraints

An agent constraint is a special fluent that constrains an organization agent to achieve some goal. In the micro-theory, ISO 9000 compliance is represented as a goal achieved if a set of quality-related agent constraints upon an enterprise is satisfied. This goal is defined in terms of compliance to the necessary 20 requirements like this:

$$
\forall O \forall s [ h o l d s (a g e n t \_ c o n s t r a i n t (O, i s o \_ 9 0 0 1 \_ c o m p l i a n t), s) \leftrightarrow\tag{2}
$$

holds(agent\_constraint(O,iso\_9001\_4.1\_compliant),s) ∧

holds(agent\_constraint(O,iso\_9001\_4.2\_compliant),s) ∧...

holds(agent\_constraint(O,iso\_9001\_4.20\_compliant),s)].

An agent constraint is a special fluent that constrains an organization agent to achieve some goal.

## ISO 9000 Micro-Theory

## Motivating Scenario

BHP Steel is an international manufacturer of quality steel products. Its Flat Products Division (FPD) produces a wide range of finished and semi-finished flat steel products from two integrated steelworks. Consistent identification of non-prime products (of inferior quality) indicates that there is something faulty in the production unit, a factory within the division. A cause for this is suspected to be an inadequate inspection system. One way to check this is to compare BHP Steel's quality inspection system with established guidelines for conducting inspection, such as the ISO 9001 requirement on inspection and testing. This check can be part of BHP Steel's initiative to eventually achieve ISO 9000 compliance.

## ISO 9000 Micro-Theory: Inspection and Testing Requirements

Inspection and testing are the most common means by which nonconformities are prevented from being delivered to customers, so requirements for ensuring adequate inspection and testing (requirement 4.10) and indicating inspection and testing status (4.12) are stated in ISO 9001. Key for representing these requirements in the micro-theory $^{5}$ is the measurement ontology, since inspection and testing are special measurement activities. The micro-theory does not represent all of the ISO 9000 requirements.

Informal Competency Questions. The questions are of the following form: Does the company comply with requirements on general inspection and testing (4.10.1), receiving (4.10.2), in-process (4.10.3), final (4.10.4) inspection and testing, and inspection and testing records (4.10.5)? These together comprise the inspection and testing requirement (4.10). Also, does the company comply with the requirement on inspection and test status (4.12)?

![](/api/attachments/DR9T6Z6T/fulltext/images/c56f2bea340fe734a77ddd14c8a247d27fd3e646647cbb2c8cc6a1ffa77caddb.jpg)

Figure 3: Data Model for ISO 9000 Micro-Theory Inspection and Testing Requirements

Formal Comptency Questions. Using terms in the data model, ISO 9001 4.10.1 compliance for an organization $<\mathsf{O}>\equiv\varepsilon^{6}$ in a situation $<s>=\sigma$ is expressed as:

holds(agent\_constraint(ε,iso\_9001\_4.10.1\_compliant),σ).

(3)

Other formal competency questions are expressed in the same form.

Axioms. Requirement 4.10.1 ([ISO, 2000] pp. 128) states:

(i) The supplier shall establish and maintain documented procedures for inspection and testing activities in order to verify that the specified requirements for the product are met.

(ii) The required inspection and testing, and the records to be established, shall be detailed in the quality plan or documented procedures.

(i) is interpreted as follows: An enterprise <O> controls its inspection and testing in accordance with ISO 9001 if for every inspection and test process <A>, <A> is controlled by some quality procedure <Ra> and some documentation for the procedure, the quality plan <Rb>.

∀O∀A∀s [holds(agent\_constraint(O,inspection\_and\_testing\_controlled),s)

(4)

$\leftrightarrow$ holds(descendent-process-organization(A,O),s)

$\wedge$ holds(inspect\_and\_test(A),s) $\rightarrow$

∃Ra∃Rb ( holds(process-control(A,Ra),s) ∧ holds(process-control(A,Rb),s) ∧

![](/api/attachments/DR9T6Z6T/fulltext/images/dd3fbb9a8d9db9a8280d68748640cad0e89c51c140f01c9249608752be9d02ed.jpg)

holds(quality\_procedure(Ra),s) ∧ holds(quality\_plan(Rb),s)) ].

descendant-process-organization(A,O): <A> is a process within organization <O>

(ii) is interpreted as follows: An enterprise <O> records its inspection and testing in accordance with ISO 9001 if for every inspection and test process <A>, <A> outputs some quality evidence <Rb> and some quality record <Ra>, the documentation of this evidence.

∀O∀A∀s[holds(agent\_constraint(O, inspection\_and\_testing\_recorded),§) ↔

(5)

holds(descendent-process-organization(A,O),s) ∧ holds(inspect\_and\_test(A),s) →

∃Ra∃Rb ( holds(process-output(A,Ra),s) ∧ holds(process-output(A,Rb),s) ∧

$holds(quality_record(Ra),s) \land holds(quality_evidence(Rb),s))$ .

An enterprise is compliant to 4.10.1 if (i) and (ii) are satisfied:

∀O∀s [holds(agent\_constraint(O,iso\_9001\_4.10.1\_compliant),s) ↔

(6)

holds(agent\_constraint(O,inspection\_and\_testing\_controlled),s) ∧

holds(agent\_constraint(O,inspection\_and\_testing\_recorded),s)].

Requirement 4.12 ([ISO, 2000], pp. 129) states:

(iii) The inspection and test status of a product shall be identified by suitable means, which indicate the conformance or nonconformance of product with regard to inspection and tests performed.

(iv) The identification of inspection and test status shall be maintained, as defined in the quality plan and/or documented procedures, throughout production, installation, and servicing of the product to ensure that only product that has passed the required inspections and tests [or released under an authorized concession] is dispatched, used, or installed.

(iii) is interpreted as follows: All trus must be identified as either a conformity or nonconformity at the end of an inspection and testing activity:

∀O∀s [ holds(agent\_constraint(O,iso\_9001\_4.12\_compliant),s) ↔

(7)

∀A∀Rt∀At∀T∀Tp ( holds(descendent-process-organization(A,O),s) ∧

holds(inspect\_and\_test(A),s) ∧ holds(process-output(A,Rt),s) ∧

holds(tru(Rt),s) ∧ holds(has\_attribute(Rt,At),s) ∧ holds(measured\_attribute(At),s) ∧

$occurs_{T}(activity\_duration(A,T)) \land end\_point(T,Tp) \rightarrow$

∃X ( holds(conformance\_pt(X,Rt,At,Tp),s) ∨

holds(nonconformance\_pt(X,Rt,At,Tp),s)) ].

<O>: an enterprise that satisfies ISO 9001 requirement 4.12

<A>: an inspect and test activity of O

<Rt>: a tru

<X>: the ID for a conformance or nonconformance point

<At>: a measured attribute of Rt

<Tp>: the time point of measurement

<s>: an extant or hypothetical situation

As for (iv), it is assumed that the maintenance of the identification of inspection and test status throughout production, installation, and servicing is implied by the previous requirement's satisfaction.

Kim [1999] expresses additional micro-theory representations for inspection and testing.

ISO 9000 Micro-Theory: Traceability Requirements

Compliance to the ISO 9000 requirement on product identification and traceability (4.8) gives confidence to an organization's customers that it has an adequate system to identify and locate products in various stages of production

Volume 8 ■ Issue 2 ■ Article 2

throughout the enterprise and trace back to causes of the nonconformities that occur. Key for representing these requirements in the micro-theory is the traceability ontology.

Informal Competency Questions. Does the company comply to ISO 9001 requirements on product identification and traceability (4.8), and sub-requirements on satisfactory identification and traceability of all products?

Terminology.

![](/api/attachments/DR9T6Z6T/fulltext/images/169d42b8b1dfc52a9c21d18e7506604541316f660d703657692359528fe79a31.jpg)  
Figure 4: Data Model for ISO 9000 Micro-Theory Traceability Requirements

Formal Competency Questions. For an organization $<\mathrm{O}>= \varepsilon$ in a situation $<\mathrm{s}>=\sigma$ , the questions are expressed as the following assertions, which must be proved true:

holds(agent\_constraint(ε,iso\_9001\_4.8\_compliant),σ). (8)

holds(agent\_constraint(ε,product\_identification),σ). (9)

holds(agent\_constraint(ε,traceability\_satisfied), σ).

(10)

Axioms. In the micro-theory, an enterprise satisfactorily identifies its products in accordance with ISO 9001 if all trus of primitive activities are identified as input, output, or intermediate resource units. Then, an enterprise complies to requirement 4.8 if it complies to the previous requirement and the following one. Any tru <Rt> must be traceable back to an input resource unit <Rta> for a process <Aa>, via a trace path <L₁>; and <Rt> must also be traceable forward to an output resource unit <Rtb> for a process <Ab>, via a trace path <L₂>. Violation of this requirement means that there is a tru that should, but cannot, be traced.

∀O∀A∀Rt∀s∃Aa∃Ab∃Rta∃Rtb∃s₀∃s'

(1 1)

[ holds(agent\_constraint(O,traceability\_satisfied),s) ↔

holds(descendent-process-organization(A,O),s) ∧ holds(process-ICOM(A,Rt),s) ∧

$holds(tru(Rt),s) \land holds(descendent-process-organization(Aa,O),s') \land$

$holds(process-output(Aa,Rta),s') \land holds(output_ru(Rta),s') \land$

holds(descendent-process-organization(Ab, O), s $_{o}$ ) ∧

$holds(process-input(Ab,Rtb),s_{o}) \land holds(input\_ru(Rtb),s_{o}) \rightarrow$

$(Rt \neq Rta \rightarrow \exists L_1 holds(tru\_trace(Rta, Rt, L_1), s')) \land$

( Rt≠Rtb → ∃L₂ holds(tru\_trace(Rt,Rtb,L₂),s₀)) ].

ISO 9000 Micro-Theory: Quality Management System Requirements

The central tenets of a quality management system (QMS) are the following:

\- Roles of workers of the QMS are planned. This is addressed by ISO 9001 requirements on management responsibility (4.1) and quality system (4.2).

\- Expectations of the roles are documented and disseminated. This is addressed by requirements on document and data control (4.5) and control of quality records (4.16).

\- All workers of the quality management system execute their roles.

![](/api/attachments/DR9T6Z6T/fulltext/images/ade691eef9f6ad73d3b67c412cc637db75758ac370dc2c8be214dde33748168d.jpg)

Key for representing these requirements in the micro-theory is the QMS ontology.

Informal Competency Questions. The following are examples of micro-theory competency questions related to the QMS:

• Is the enterprise compliant to ISO 9001 requirement 4.1?

\- Does the enterprise define and document the quality objectives in accordance with ISO 9001?

\- Does the enterprise implement the quality policy in accordance with ISO 9001?

• Is the enterprise compliant to ISO 9001 requirement 4.2.1?

\- Does there exist a quality manual in accordance with ISO 9001?

• Is the enterprise compliant to ISO 9001 requirement 4.5?

\- Does the master list identify current revisions of documents in accordance with ISO 9001?

\- Does the enterprise retain documents for an adequate amount of time in accordance with ISO 9001?

## Terminology.

![](/api/attachments/DR9T6Z6T/fulltext/images/1c5fe25c66f087dbe1f627004bfd030df8e28dd596382ffb34979176a07d5df7.jpg)  
Figure 5: Data Model of ISO 9000 Micro-Theory QMS Planning Requirements $^{7}$

Figure 6: Data Model of ISO 9000 Micro-Theory QMS Documentation Requirements $^{8}$  
![](/api/attachments/DR9T6Z6T/fulltext/images/c60af32d149a7e961e3195e88bc62649a358f5c9fadaa5014478a98f5a851831.jpg)

![](/api/attachments/DR9T6Z6T/fulltext/images/3267ac81cd294d30623105999933781f34d3b1a3f385c8e29393913935414586.jpg)  
Terms from the Ontologies used to define these micro-theory terms

Formal Competency Questions. These correspond to some of the informal questions.

Does an enterprise $\varepsilon$ comply to the ISO 9001 requirement 4.1 in a situation $\sigma$ ?:

holds(agent\_constraint(ε,iso\_9001\_4.1\_compliant),σ)].

Does an enterprise comply to the ISO 9001 requirement upon defining and documenting quality objectives in a situation $\sigma$ ?:

∃A∃G∃E [holds(agent\_constraint(ε,

(13)

quality\_objective\_define\_and\_document(A,G,E),σ) ].

<A> define and document activity

<G> quality objective

<E> executive manager

Does an enterprise $\varepsilon$ comply to the ISO 9001 requirement upon implementing the quality policy in a situation $\sigma\vdots$ : holds(agent\_constraint( $\varepsilon$ ,quality\_policy\_ implemented), $\sigma$ ). (14)

```txt
Axioms. For brevity, definitions are not shown.
```

## Demonstration of Competency

A demonstration of competency is useful both for analysis (for the enterprise analyst), and evaluations of general ontologies and prescriptive micro-theories (for the ontology builder). An advisor is a user interface and access routines front-end software that supports both uses.

<table><tr><td colspan="3">Table 1: Steps for Using an Advisor for Demonstrating Competency</td></tr><tr><td>Step #</td><td>Enterprise Analyst View: Using the Advisor to Analyze Specific Enterprise</td><td>Ontology Builder View: Using the Advisor to Evaluate Competency of Ontology</td></tr><tr><td>1</td><td>Stating facts about an enterprise</td><td>Representing populated enterprise model</td></tr><tr><td>2</td><td>Stating queries for analyzing enterprise</td><td>Representing formal competency questions</td></tr><tr><td>3</td><td>Stating data dictionary of enterprise&#x27;s terms</td><td>Representing ontology terminology and axioms</td></tr><tr><td>4</td><td>Answering queries</td><td>Deducing answers to formal competency questions</td></tr><tr><td>5</td><td>Explaining the derivation of answers</td><td>Displaying Prolog trace list</td></tr></table>

$\Leftrightarrow$ denotes translation between knowledge about an enterprise and how that knowledge is represented using an ontology

The following is an example use of the ISO 9000 Quality Advisor.

Step #1: Stating facts about the enterprise $\Leftrightarrow$ Representing populated enterprise model. One benefit of the micro-theory design is that ISO 9000 evaluation can be performed on a sufficiently well populated enterprise model that was designed for another purpose. Shown in Error! Reference source not found. are data instances used for the demonstration of competency for the measurement ontology [Kim and Fox, 2002]. These instances are also used to evaluate ISO 9000 compliance.

![](/api/attachments/DR9T6Z6T/fulltext/images/6c2975adfb3c23bb3f067d2c821ec4530dffa4c5a69934304e12780e9e2642fa.jpg)  
Figure 7. Displaying Facts and Representing Them using an Advisor  
Step #2: Stating queries for analyzing enterprise $\Leftrightarrow$ Representing formal competency questions. Error! Reference source not found. shows that BHP Steel's query is translated into a micro-theory competency question, expressed both in English and first-order logic. The question then is expressed formally in first-order logic.

Figure 8: Displaying Queries and Representing Them as Formal Competency Questions  
![](/api/attachments/DR9T6Z6T/fulltext/images/acb805937c54308fe5aaa4bac350ef0cdc83f4d72503c3951d34f1a4f847f686.jpg)

![](/api/attachments/DR9T6Z6T/fulltext/images/8b9668e2515c40e5abe7ecb09de17264bf425359272fb9ec196e55aefb006880.jpg)  
Step #3: Stating data dictionary of enterprise's terms $\Leftrightarrow$ Representing micro-theory terminology and axioms. The terms BHP Steel uses to describe ISO 9000 should obviously be no different from the standard itself. The company's ISO 9000 data dictionary is conceptually the same as the micro-theory's terminology. The former is expressed as English words (e.g. "Results of inspection must be carefully recorded."); the latter, as first-order predicates (e.g. holds(agent\_constraint(O, iso\_9001\_inpection\_and\_testing\_recorded,s)).

Step #4: Answering queries $\Leftrightarrow$ Deducing answers to formal competency questions. A BHP Steel query answer screen is shown in Figure 9. Figure 10 shows an actual Prolog screen of the query evaluating BHP Steel's compliance to ISO 9001 requirement 4.10.1. Answering this query takes 175 deductions.  
![](/api/attachments/DR9T6Z6T/fulltext/images/accb93e2b3e42f4a886ac1f21ab6355598f786510b70033e523f0055a390dcb3.jpg)

![](/api/attachments/DR9T6Z6T/fulltext/images/7e4a19a3b49ac13f191bcbdd463b507b8ad98c3bf96517a3b9342e4d5fe97b99.jpg)  
Step #5: Explaining the derivation of answers $\Leftrightarrow$ Displaying Prolog trace list. The trace list is not shown here.

We implemented the micro-theory, ontologies, and the advisor for a prototype case study for BHP Steel and another industrial partner, de Havilland Manufacturing. The purpose of the study was to prototypically demonstrate how the ontologies and micro-theories could be used to analyze quality within an enterprise, including use for evaluating ISO 9000 compliance. Ontology and micro-theory terminology were implemented and instantiated in ROCK $^{™}$ , an object-oriented database, and axioms were represented and applied to instances to answer competency questions in Prolog, a logic programming language. The ISO 9000 Quality Advisor was designed using HTML. Specialized programmatic interfaces written in C++ were used to integrate the different software. We achieved the following from prototyping:

<table><tr><td colspan="3">Table 2: Case Study Milestones</td></tr><tr><td></td><td>BHP Steel</td><td>de Havilland Manufacturing</td></tr><tr><td>Constructed model of partner enterprise using Ontologies for Quality Modeling</td><td>x</td><td>x</td></tr><tr><td>Reasoned about quality within partner enterprise model</td><td>x</td><td>x</td></tr><tr><td>Demonstrated proof-of-concept of engineering ontology-based enterprise models</td><td>x</td><td></td></tr><tr><td>Tested ISO 9000 Micro-Theory by using partner enterprise model as testbed</td><td>x</td><td>x</td></tr><tr><td>Incorporated user requirements for prototyping ISO 9000 Quality Advisor</td><td>x</td><td></td></tr></table>

Next, we present a demonstration of micro-theory generality—another reason for ontology use, aside from competency.

## Demonstration of Generality

## What Is Generality?

Whereas competency evaluates an ontology's problem-solving capability, reducibility [Gruninger, 1996] can be used to evaluate generality. If a set of competency questions from a foreign or "target" ontology can be reasonably translated (reduced) to a set answerable using a "native" ontology's representations, then the competency of the "native" ontology is a superset of the competency of the "target" ontology vis-à-vis the questions. Reducibility demonstrates that an ontology is general enough to answer competency questions for a variety of applications that support solving different problems. General representations in turn can be re-used to construct different applications that solve different problems.

The reduction of competency questions can be expressed as the following meta-theoretic problem:

$$
\bullet \quad T _ {\text { ontology }} ^ {\prime} \cup T _ {\text { ground }} ^ {\prime} | = Q \Rightarrow T _ {\text { ontology }} \cup T _ {\text { ground }} \cup T _ {\text { def }} | = Q\tag{15}
$$

$T_{ontology}$ and $T'_{ontology}$ denote native and target ontology representations, respectively.

\- $T_{ground}$ and $T'_{ground}$ denote ground terms (facts), represented using the primitive terms of the TOVE ontology and target ontology representations, respectively.

\- $T_{\text{def}}$ is the set of axioms that translate $T'_{\text{ontology}} \cup T'_{\text{ground}}$ into the same language as $T_{\text{ontology}} \cup T_{\text{ground}}$

Q denotes a first-order sentence, which is entailed by $T'_{ontology} \cup T'_{ground}$ . Q is also entailed by $T_{ontology} \cup T_{ground} \cup T_{def}$ .

The procedure for reduction to TOVE competency questions is as follows.

1. Determine the target ontology.

$$
T _ {\text { ontology }} ^ {\prime}.
$$

2. State the target ontology's competency question in the language of the target ontology.

$$
Q \in L (T _ {\text { ontology }} ^ {\prime}).
$$

3. Ensure that the competency question is answerable using target ontology representations.

$$
T _ {\text { ontology }} ^ {\prime} \cup T _ {\text { ground }} ^ {\prime} \mid = Q.
$$

4. Specify a set of reduction axioms such that the target ontology's competency question can be posed in the formal language of the native (TOVE) ontology.

$$
Q \cup T _ {d e f} \in L (T _ {\text { ontology }}).
$$

5. Answer the competency question in the language of the native (TOVE) ontology.

$$
T _ {\text { ontology }} \cup T _ {\text { ground }} \cup T _ {\text { def }} \mid = Q.
$$

## Reducing The Strategic Analyst™

1. Determine the target ontology. As mentioned in the literature review, the Strategic Analyst $^{™}$ is a software similar to the ISO 9000 Quality Advisor: Its primary use is for diagnostic internal quality audits, and it provides an easy-to-use interface for the analyst that presents standard terminology and example help on applying ISO 9000. The computer-encoded ontology for The Strategic Analyst $^{™}$ can be considered as the 500 or so hierarchically organized questions, the relationships between them, and the keywords defined in English with which they are expressed. There is no explicit The Strategic Analyst $^{™}$ ontology. The predicates [equations (17)-(28) below] and axioms [(29)-(32)] are very reasonable representations that we manually inferred after examining The Strategic Analyst $^{™}$ software. Reduction entails mapping relationships between two ontologies reasonably, practicably, and manually when two ontologies differ in representation format, syntax, and semantics, as is the case for this demonstration. Therefore, the reduction is valid even if the The Strategic Analyst $^{™}$ cannot be validated.

2. State the target ontology's competency question in the language of the target ontology. This is one question that an analyst must answer in using The Strategic Analyst™: "Does the enterprise document its strategic intent especially as it relates to quality?" Stating this ontology in first-order logic, an expression for the question follows:

∃G enterprise\_documents\_quality\_strategic\_intent(ε,G).

(16)

<G>: a document that details strategic intent related to quality

3. Ensure that the competency question is answerable using target ontology representations. The software notes that "strategic intent" is a concept, "sometimes called a mission statement or a corporate vision, it is an organizational framework into whose context short and long term goals comfortably fit." What follows is a partial list of the predicates of The Strategic Analyst™. It must be noted that these predicates are mainly nouns excerpted from the English text above.

$$
\text { enterprise } (\bigcirc).\tag{17}
$$

$$
\operatorname{document} (D).\tag{18}
$$

$$
\text { strategic\_intent } (S).\tag{19}
$$

$$
\text { mission\_statement(S) }.\tag{20}
$$

$$
\text { corporate\_vision } (S).\tag{21}
$$

$$
\operatorname{concept} (S).\tag{22}
$$

$$
\text { short\_term\_goal } (G).\tag{23}
$$

$$
\text { long\_term\_goal } (G).\tag{24}
$$

$$
\text { quality\_related\_goal } (G).\tag{25}
$$

$$
\text { goal\_fits\_context\_of } (G, S).\tag{26}
$$

$$
\text { enterprise\_documents } (O, D).\tag{27}
$$

$$
\text { concept\_is\_documented\_by(S,D) }.\tag{28}
$$

If a mission statement or corporate vision has a short- or long-term goal in its context, then the statement or vision expresses strategic intent.

$$
\forall \mathsf {S} \exists \mathsf {G} [ (\text { mission\_statement } (\mathsf {S}) \vee \text { corporate\_vision } (\mathsf {S})) \wedge
$$

$$
\text { goal\_fits\_context\_of } (G, S) \land\tag{29}
$$

$$
(\text { short\_term\_goal } (G) \vee \text { long\_term\_goal } (G)) \to \text { strategic\_intent } (S) ].
$$

A quality related goal is a short or long term goal.

$$
\forall G [ \text { quality\_related\_goal } (G) \to \text { short\_term\_goal } (G) \lor \text { long\_term\_goal } (G) ].\tag{30}
$$

Strategic intent is a concept.

$$
\forall S [ \text { strategic\_intent } (S) \to \text { concept } (S) ].\tag{31}
$$

If a document of an enterprise documents a concept then the enterprise documents the concept.

$$
\forall \mathbf {O} \forall \mathbf {S} \forall \mathbf {D} [ \text { enterprise } (\mathbf {O}) \land \text { document } (\mathbf {D}) \land \text { concept } (\mathbf {S}) \land\tag{32}
$$

$$
\text { enterprise\_documents } (O, D) \land \text { concept\_is\_documented\_by } (S, D) \rightarrow
$$

$$
\text { enterprise\_documents\_concept } (O, S) ].
$$

The predicate representing the competency question then can be expressed as follows:

$$
\forall \mathbf {O} \forall \mathbf {G} \forall S [ \text { strategic\_intent(S) } \land \text { goal\_fits\_context\_of(G,S) } \land\tag{33}
$$

$$
\text { quality\_related\_goal } (G) \land \text { enterprise\_documents\_concept } (O, S) \to
$$

$$
\text { enterprise\_documents\_quality\_strategic\_intent } (O, G).
$$

(42)

Here is a minimal set of ground terms. Note that ground terms are populated predicates and hence do not have operators:

quality\_related\_goal(γ). (34)

mission\_statement(ζ). (35)

goal\_fits\_context\_of(γ,ζ). (36)

document(δ). (37)

concept\_is\_documented\_by(ζ,δ). (38)

enterprise( $\varepsilon$ ). (39)

enterprise\_documents(ε, δ). (40)

Given the ontology [(17)-(34)] and these ground terms, the competency question (16) is answered as follows:

enterprise\_documents\_quality\_strategic\_intent(ε,γ).

4. Specify a set of reduction axioms such that the target ontology's competency question can be posed in the formal language of the native (TOVE) ontology. Say the following axiom is asserted as a reduction axiom. If an enterprise documents its strategic intent that has a goal in its context, then the enterprise documents that goal.

∀O∀G∀S [ strategic\_intent(S) ∧ goal\_fits\_context\_of(G,S) ∧

enterprise\_documents\_concept(O,S) →

enterprise\_documents\_strategic\_goal(O,G)].

Also, assume that the operator in (34) is equivalence ( $\leftrightarrow$ ), rather than implication. Then the competency question can be re-expressed as follows: Is there a quality-related, strategic goal documented by the enterprise?

$\exists G$ [ quality\_related\_goal(G) ∧ enterprise\_documents\_strategic\_goal(ε,G)]. (43)

These axioms defined in the The Strategic Analyst™ ontology will be mapped to the TOVE ontology term, agent\_constraint(O,quality\_objective\_define\_document(A,G,E)) in the next step.

5. Answer the competency question in the language of the native (TOVE) ontology. Assuming that a quality-related goal (from The Strategic Analyst™ ontology) is a quality objective (from ISO 9000 Micro-Theory) and that the question is posed in order to achieve ISO 9000 compliance, the competency question can be entirely expressed using the micro-theory, as: "Does an organization define and document its quality objective in accordance with the ISO 9001?"

∀s∀O∃G∃A∃E holds(agent\_constraint(O,quality\_objective\_define\_document(A,G,E)),s) (44)

↔ quality\_related\_goal(G) ∧ enterprise\_documents\_strategic\_goal(O,G).

The term, quality objective define and document, denotes an ISO 9000 Micro-Theory constraint that there be a define and document activity <A> for which the executive manager <E> defines and documents a quality objective <G>.

Such reductions as shown here provide evidence that representations of the micro-theory are general enough to be re-used to evaluate ISO 9000 compliance of organizations, not only for BHP Steel, but also for organizations that use The Strategic Analyst™ software. The scope of The Strategic Analyst™ 's competency is narrower than the micro-theory's, since many more than 500 competency questions can be answered using the micro-theory. Just as a second party standard is more specific and narrower in scope than a third party's, so is The Strategic Analyst™ 's competency, relative to the micro-theory's. The demonstration presented here is then akin to showing that the micro-theory's representations are general enough to be re-used to express second party quality standards. Hence, one goal of micro-theory development is satisfied.

![](/api/attachments/DR9T6Z6T/fulltext/images/5aa2f94e1f9f68f9f857f18d42517439adc8ab86eca8365e1e794bb2271110bc.jpg)

## Concluding Remarks

In this paper, the TOVE ISO 9000 Micro-Theory is presented as a formal and sharable evaluative model that presents an exemplar application for evaluating compliance using enterprise models built from descriptive quality ontologies.

The micro-theory represents ISO 9000 requirements for the following: Inspection and testing, represented using the measurement ontology; product identification and traceability, represented using the traceability ontology; and management of the quality system, represented using the QMS (Quality Management System) ontology. We develop the micro-theory by posing competency questions, analyzing the ISO 9000 domain, stating assumptions, and developing terminology and axioms. Then, we prototypically demonstrate competency of the micro-theory by automatically evaluating ISO 9000 compliance of a research partner, BHP Steel, to a subset of requirements. The demonstration of generality shows that the micro-theory representations are general enough to be re-used to express competency questions for another ISO 9000 software, The Strategic Analyst $^{™}$ , or for a model of a second party quality standard.

The contributions of the work detailed in the paper can be classified according to the two postulates about ontology-based enterprise models stated in Section I:

\- They can be leveraged to support business analytics problems, in particular, compliance evaluation (for example, to ISO 9000 or Sarbanes-Oxley). It has been thoroughly demonstrated that a micro-theory built from ontologies can indeed be used to infer compliance to standards or requirements. It is further demonstrated that a micro-theory removes some of the subjectivity of compliance evaluation by the objective, formal representation of requirements and is generally applicable to a wide set of modeled enterprises.

\- They are easier to share. This model constitutes a more formal and systematic representation of a standard or requirement. Compliance is deduced as satisfaction to hierarchically organized constraints, subject to explicitly stated assumptions. Formal models must be precisely stated to support deduction without error; this precision enables sharing.

Ontologies serve as one of the cornerstones for the nascent data sharing infrastructure over the Web, the semantic Web. For use on the semantic Web, the ontologies and micro-theory stated in this paper need only be implemented using one of the de facto languages for the semantic Web, RuleML [Boley et al., 2001], a language which is also based on first-order logic.

Along with these benefits, there are limitations to ontology use. The same limitations apply to micro-theory use. Substantial effort is required to take a concept informally, though sufficiently, represented in a data model and add sufficient formal semantics to make interpretation more precise for an ontology. An ontology is also less comprehensible to the user or analyst than natural language requirements or ER models because formal representational languages are more esoteric. Experiences from ontology use for natural language processing show that sharing axioms between ontologies is labor intensive even if language translators exist [Uschold, 1998]. So, developing and maintaining a library of ontologies, as opposed to traditional data models, is expensive and time consuming [Menzies, 1999]; we cannot recommend ontology use for one-off applications that do not re-use these libraries.

Another limitation is that our work pre-supposes that both the data-base and the rule-base are represented using ontologies. However, traditional ER or XML-based databases dominate in numbers in comparison to ontology-based knowledge-bases. Providing a means of inter-operating between ER or XML based models and ontology-based models would have definitely strengthened this paper. As it is though, this type of ontology inter-operability or integration is a separately challenging problem; there is much research that concentrates on this issue alone without heed to the competency of ontologies [Alani et al., 2003; Maedche et al., 2002; Philippi and Kohler, 2004], which is our focus. We, therefore, made a choice to concentrate on ontology competency, and leave inter-operability beyond the scope of this paper. However, there are works that facilitate inter-operation between XML databases and ontologies developed using the TOVE engineering methodology [Kim and Sengupta, 2007].

There are also open questions about how this work would be used practically by quality-minded managers. First, quite evidently, we did not perform an economic analysis of the value of achieving compliance using this work. We believe that such quantification is beyond the information systems and prototyping aim of our paper. Yet we recognize that such quantification would be critical to “sell” a final system based upon this prototype to managers. Second there is also the issue that such a final system would perform badly if the model of the specific enterprise upon which the system is applied is incomplete or inaccurate. Ensuring a model is properly populated is a resources management issue that we believe is beyond the scope of this paper. Third, we do not address the subtle but important issue of ensuring that the evaluation

Volume 8 ■ Issue 2 ■ Article 2

using ISO 9000 Micro-Theory is compliant with the ISO 9000. We recognize that to not encompass the three issues within our scope limits widespread adoption of our work, but our scope is consistent with our aim of showing that ontology-based compliance evaluation is technically very possible.

To realize widespread use of the technical possibility of ontology use, the semantic Web has been put forth as the enabling technology that will lead to greater adoption of ontologies [Berners-Lee et al., 2001; Kim, 2002] for applications such as compliance evaluation. Tim Berners-Lee, the oft-acknowledged inventor of the WWW, has a vision of the next generation of the Web, the semantic Web:

Computers will find the meaning of semantic data by following hyperlinks to definitions of key terms and rules for reasoning about them logically. The resulting infrastructure will spur the development of automated Web services such as highly functional agents [Berners-Lee et al., 2001].

In this vision, meanings that computers can find and reason about are represented using ontologies. Companies such as IBM and HP [McBride, 2002] have initiated large projects to develop the infrastructure for semantic Web based services. Web services are “self-contained, modular business process applications, which are based on open, Internet standards...Web services can be mixed and matched to create innovative applications, processes, and value chains” [IBM, 2002]. There are numerous other efforts: e.g. ontology languages for the semantic Web [Bechhofer et al., 2001; McGuinness and van Harmelen, 2003], languages that describe the type of Web services [McIlraith et al., 2001], and ontology development environments [Noy et al., 2001].

There are even a few projects revolving around for quality: for example, evaluations of quality (and trustworthiness) of data [Thuraisingham, 2002] and quality of service [FIPA, 2002]; and dissemination of data about quality (of tourist sites) [Mädche and Staab, 2003]. The TOVE quality ontologies can be used for either; that is, they can be used 1) to measure, trace, and manage Web services, or 2) to represent and interpret data about measurement, tracing, and management of products and business processes for automated sharing over the semantic Web. These ontologies then can arguably form the building blocks to develop specialized ontologies and micro-theories for any type of quality management application over the semantic Web. In Kim and Fox [2003], the measurement ontology is indeed used for a semantic Web application.

However, ontologies for the semantic Web are still in their infancy. Yahoo!™ [Labrou and Finin, 1999] and VerticalNet™ [Das and Wu, 2001] are popular examples of companies using ontologies for e-commerce. As it is, semantics interpretable by external software agents responsible for Web services are not provided for these ontologies. Recently, however, tools for semantic Web ontology development such as those that provide graphical, more intuitive ontology development, configuration controls for managing maintenance, and semi-automatic support for integrating ontologies from different sources have been developed [Noy et al., 2001; Staab et al., 2001]. Moreover OWL [McGuinness and van Harmelen, 2003] and RuleML [Boley et al., 2001] have emerged as de facto languages for modeling semantic Web ontology axioms and classes, respectively.

These works will be used in addressing one obvious future work from this paper: The implementation of the TOVE ontologies and micro-theory in the semantic Web. In the nascent MOQ Project, TOVE ontologies are translated and augmented to develop ontologies for evaluating quality-of-service of general Web services, and building from that, for delivering a suite of third-party quality management Web services to general Web services [Kim et al., 2005]. Another direction for future research lies in additional compliance evaluations using ontology-based enterprise models.

One project just initiated because it is currently so topical and important is compliance evaluation against the corporate governance requirements set forth in the Sarbanes-Oxley Act. The Sarbanes Oxley Act (SOx) of 2002 is a set of strict requirements for financial accounting of public companies. The primary conceptual difference between SOx and ISO 9000 lies in the fact that SOx is a law and not a standard, leading to differing consequences of non-conformance. However, they are similar in the level of internal control requirements. An existing ISO 9000 framework can make it relatively straightforward to provide auditing facilities and methods for SOx [Stimson, 2005]. Consequently, we believe that much of the methodology, ontology representations, and proof-of-concept application modules can be used to develop a SOx Micro-Theory.

## References

EDITOR'S NOTE: The following reference list contains hyperlinks to World Wide Web pages. Readers who have the ability to access the Web directly from their word processor or are reading the paper on the Web, can gain direct access to these linked references. Readers are warned, however, that

1. these links existed as of the date of publication but are not guaranteed to be working thereafter.

2. the contents of Web pages may change over time. Where version information is provided in the References, different versions may not contain the information or the conclusions referenced.

3. the author(s) of the Web pages, not AIS, is (are) responsible for the accuracy of their content.

4. the author(s) of this article, not AIS, is (are) responsible for the accuracy of the URL and version information.

Alani, H., S. Kim, D. E. Millard, M. J. Weal et al. (2003) "Automatic Ontology-Based Knowledge Extraction from Web Documents," IEEE Intelligent Systems (18) 1, pp. 14-21.

Allen, J. F. (1983) "Maintaining Knowledge about Temporal Intervals," Communications of the ACM (26) 11, pp. 832-43.

Bechhofer, S., C. Goble, and I. Horrocks. (2001) DAML+OIL Is not Enough. First Semantic Web Working Symposium (SWWS-01), Stanford, CA, 2001.

Berners-Lee, T., J. Hendler, and O. Lassila (2001) "The Semantic Web," Scientific American (284) 5, pp. 34-43.

Bernus, P. (2003) "Enterprise Models for Enterprise Architecture and ISO9000:2000," Annual Reviews in Control, To Appear.

Boley, H., S. Tabet, and G. Wagner. (2001) Design Rationale of RuleML: A Markup Language for Semantic Web Rules. Proceedings of the First Semantic Web Working Symposium (SWWS'01), Stanford, CA, 2001.

Burton-Jones, A., S. Purao, and V. C. Storey, "in, L. Applegate, R. Galliers and J. I. DeGross (eds.), Dec. 16-19, 2002, pp. 195-208. (2002) Context-Aware Query Processing on the Semantic Web. Proceedings of the Twenty-third International Conference on Information Systems (ICIS), Barcelona, Spain, 2002.

Campbell, A. E. and S. C. Shapiro. (1995) Ontological Mediation: An Overview. IJCAI Workshop on Basic Ontological Issues in Knowledge Sharing, 1995.

Das, A. and W. Wu. (2001) Industrial Strength Ontology Management. International Semantic Web Working Symposium, Stanford, CA, 2001.

Fadel, F. G., M. S. Fox, and M. Grüninger. (1994) A Generic Enterprise Resource Ontology. Workshop on Enabling Technologies: Infrastructure for Collaborative Enterprises, Morgantown, WV, 1994.

FIPA (2002) "FIPA Quality of Service Specification," Foundation for Intelligent Physical Agents,

Fox, M., J. F. Chionglo, and F. G. Fadel. (1993) A Common Sense Model of the Enterprise. Proceedings of the 2nd Industrial Engineering Research Conference, Norcross GA, 1993, pp. 425-429.

Fox, M. S. (1990) "Artificial Intelligence and Expert Systems: Myths, Legends, and Facts," IEEE Expert (5) 1, pp. 8-22.

Fox, M. S. (1992) The TOVE Project, Towards a Common Sense Model of the Enterprise, in C. Petrie (Ed.) Enterprise Integration, Cambridge, MA: MIT Press.

Fox, M. S., M. Barbuceanu, and M. Grüninger (1994) "An Organization Ontology for Enterprise Modelling: Preliminary Concepts for Linking Structure and Behaviour," Computers in Industry (29pp. 123-34.

Fox, M. S. and M. Gruninger (1998) "Enterprise Modelling," AI Magazine (19) 3, pp. 109-121.

Gómez-Pérez, A., M. Fernández-López, and O. Corcho (2004) Ontological Engineering with examples from the areas of Knowledge Management, e-Commerce and the Semantic Web: Springer.

Grosof, B. N. and L. Morgenstern. (1992) Applications of Logicist Knowledge Representation to Enterprise Modeling. AAAI-92 Workshop on Enterprise Integration, San Jose, CA, 1992.

Gruninger, M. (1996) Designing and Evaluating Generic Ontologies. Proceedings of the Workshop on Ontological Engineering, European Conference on Artificial Intelligence, Budapest, 1996, pp. 53-65.

Gruninger, M. and M. S. Fox. (1995) Methodology for the Design and Evaluation of Ontologies. Workshop on Basic Ontological Issues in Knowledge Sharing, IJCAI-95, Montreal, Canada, 1995.

Grüninger, M. and M. S. Fox. (1994) An Activity Ontology for Enterprise Modelling. Workshop on Enabling Technologies - Infrastructures for Collaborative Enterprises, West Virginia University, WV, 1994.

Hammer, M. (1990) "Reengineering Work: Don't Automate, Obliterate," Harvard Business Review pp. 104-112.

Hausen, H.-L. (1998) "A rule-based process model for cooperative software projects," Knowledge-Based Systems (11pp. 105-113.

Hayes, P. J. (1985) Naive Physics I: Ontology for Liquids, in J. Hobbs and B. Moore (Eds.) Theories of the Commonsense World: Ablex Publishing Corp., pp. 71-89.

IBM (2002) "Web services by IBM," IBM, HTTP://WWW-3.IBM.COM/SOFTWARE/SOLUTIONS/WEBSERVICES/OVERVIEW.HTML (May 20, 2002).

ISO (1994) ISO 9000 Standards for Quality Management. Geneva, Switzerland: International Organization for Standards Central Secretariat.

ISO (2000) ISO 9000 Standards for Quality Management: 2000. Geneva, Switzerland: International Organization for Standards Central Secretariat.

Kautz, H. (1985) Formalizing Spatial Concepts and Spatial Language. Center for the Study of Language and Information, Stanford University CSLI-85-35.

Kim, H. M. (1999) Representing and Reasoning about Quality using Enterprise Models. Ph.D., Department of Industrial Engineering, University of Toronto.

Kim, H. M. (2002) "Predicting how the semantic Web will evolve," Communications of the ACM (45) 2, pp. 48-54.

Kim, H. M. and M. S. Fox (2002) "Towards Quality Management Web Services: An Ontology of Measurement for Enterprise Modeling," Lecture Notes in Computer Science (2348pp. 230-44.

Kim, H. M., M. S. Fox, and M. Grüninger (1999) "An Ontology for Quality Management: Enabling Quality Problem Identification and Tracing," BT Technology Journal (17) 4, pp. 131-9.

Kim, H. M. and M. S. Fox, in revision for: (2003) "An Ontology of Measurement for Enterprise Modeling: A Fundamental Data Model for Quality Management Web Services," ACM Transactions on Information Systems (In Revision).

Kim, H. M. and A. Sengupta (2007) "Extracting Knowledge from XML Document Repository: A Semantic Web-Based Approach," Information Technology and Management (Accepted for Publication).

Kim, H. M., A. Sengupta, and J. Evermann. (2005) MOQ: Web services ontologies for QoS and general quality evaluations. European Conference on Information Systems, Regensburg, Germany, 2005.

Kosanke, K., F. B. Vernadat, and T. J. Williams. (1997) Manufacturing Enterprise Modelling with PERA and CIMOSA. IFAC Workshop-MIM'97, 1997.

Kuipers, B. J. (1986) "Qualitative Simulation," Artificial Intelligence (29) 3, pp. 289-338.

Labrou, Y. and T. Finin. (1999) Yahoo! as an Ontology - Using Yahoo! Categories to Describe Documents. Proceedings of the 8th International Conference on Information and Knowledge Management (CIKM 99), Kansas City, MO, 1999, pp. 180-187.

Lenat, D. B. (1995) "CYC: A large-scale investment in knowledge infrastructure," Communications of the ACM (38) 11, pp. 33-8.

Lenat, D. B. and R. V. Guha (1990) Building Large Knowledge-based Systems: Addison-Wesley.

Mädchen, A. and S. Staab. (2003) Services on the Move - Towards P2P-Enabled Semantic Web Services. 10th International Conference on Information Technology and Travel & Tourism, ENTER 2003, Helsinki, Finland, 2003.

Maedche, A., S. Staab, R. Studer, Y. Sure et al. (2002) "SEAL - Tying Up Information Integration and Web Site Management by Ontologies," IEEE Computer Society Data Engineering Bulletin (25) 1, pp. 10-17.

McBride, B. (2002) "Four Steps Towards the Widespread Adoption of a Semantic Web," Lecture Notes in Computer Science (2342pp. 419.

McCall, J. A., P. K. Richards, and G. F. Walters (1977) Concepts and definitions of software quality, in, vol. 1, November Factors in software quality, Springfield, VA: NTIS.

McCarthy, J. and P. J. Hayes (1969) Some Philosophical Problems from the Standpoint of AI, in, vol. 4 B. Meltzer and D. Michie (Eds.) Machine Intelligence, Edinburgh, UK: Edinburgh University Press, pp. 463-501.

McGuinness, D. L. and F. van Harmelen. (2003) OWL Web Ontology Language Overview. W3C CR-owl-features-20030818.

McIlraith, S. A., T. C. Son, and H. Zeng (2001) "Semantic Web Services," IEEE Intelligent Systems (16) 2, pp. 46-53.

Menzies, T. (1999) "Cost Benefits of Ontologies," IEEE Intelligence (10) 3, pp. 26-32.

Newell, A. (1982) "The Knowledge Level," Artificial Intelligence (18) 1, pp. 87-127.

Noy, N. F., M. S. Decker, M. Crubezy, R. W. Fergerson et al. (2001) "Creating Semantic Web Contents with Protégé-2000," IEEE Intelligent Systems (16) 2, pp. 60-71.

ODS. (1998) The Strategic Analyst. Omni Data Sciences.

Philippi, S. and J. Kohler (2004) "Using XML technology for the ontology-based semantic integration of life science databases," IEEE Transactions on Information Technology in Biomedicine (8) 2, pp. 154-160.

Purao, S. and V. Storey (2005) "A multi-layered ontology for comparing relationship semantics in conceptual models of database," Applied Ontology (1) 2, pp. 117-139.

QualityDigest (2000) "2000 ISO 9000 Software Buyer Guide," Quality Digest.

Reiger, C. and M. Grinberg. (1977) The Declarative Representation and Procedural Simulations of Causality in Physical Mechanisms. Joint Conference on Artificial Intelligence, 1977, pp. 250-5.

Sarbanes-Oxley. (2002) Sarbane-Oxley Act: Public Law 107-204. 107th US Congress.

Sathi, A., M. S. Fox, and M. Greenberg (1985) "Representation of Activity Knowledge for Project Management," IEEE Transactions on Pattern Analysis and Machine Intelligence (7) 5, pp. 531-52.

![](/api/attachments/DR9T6Z6T/fulltext/images/51d6b0155fa6d296abe138484980d1dd9f751323aaeaf085e9b5a739dcd7584e.jpg)

Seddon, J. (1997) "Ten Arguments Against ISO 9000," Managing Service Quality (7) 4, pp. 162-8.

Seddon, J. (2001) The Case Against ISO 9000. Dublin, Ireland: Oak Tree Press.

Staab, S., H.-P. Schnurr, R. Studer, and Y. Sure (2001) "Knowledge Processes and Ontologies," IEEE Intelligent Systems (16) Stimson, W. (2005) "Sarbanes Oxley and ISO 9000," Quality Progress (March) pp. 24-29.

Storey, V. C., R. H. L. Chiang, D. Dey, R. C. Goldstein et al. (1997) "Database design with common sense business reasoning and learning," ACM Trans. Database Syst. (22) 4, pp. 471-512.

Storey, V. C., V. Sugumaran, and Y. Ding. (2005) A Semi-automatic Approach to Extracting Common Sense Knowledge from Knowledge Sources. International Conference on Applications of Natural Language to Information Systems, Versaille, France, 2005, pp. 322-332.

Thuraisingham, B. M. (2002) Building Secure Survivable Semantic Webs. International Conference on Tools with Artificial Intelligence, 2002, pp. 395-8.

Tølle, M. and P. Bernus (2003) "Reference models supporting enterprise networks and virtual enterprises," International Journal of Networking and Virtual Organisations (2) 1, pp. 2-15.

Uschold, M. (1998) Where Are the Killer Apps? Proceedings of ECAI-98 Workshop on Applications of Ontologies and Problem-Solving Methods, 1998.

Uschold, M. and M. Gruninger (1996) "Ontologies: Principles, Methods and Applications," Knowledge Engineering Review (11) 2, pp. 93-136.

Uschold, M., M. King, S. Moralee, and Y. Zorgios (1998) "The Enterprise Ontology," Knowledge Engineering Review (13) 1, pp. 31-89.

Vernadat, F. B. (1996) Enterprise Modelling and Integration - Principles and Applications: Chapman & Hall.

Walters, J., D. Kuratko, and L. Dusseau. (2000) An Attitudinal Survey of Indiana ISO/QS 9000 Registered Companies Regarding Process and Participant Roles. Midwest Quality Conference, St. Louis, MO, 2000.

Welzel, D. (1993) Tailoring and Conformance Testing of Software Processes - The ProcePT Approach, in ERCIM News.

Zelm, M. and K. Kosanke. (1997) CIMOSA and its Application in an ISO 9000 Process Model. IFAC Workshop-MIM'97, Vienna, Austria, 1997.

ISSN: 1536-9323

Editor

Kalle Lyytinen
Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Elena Karahanna</td><td>University of Georgia, USA</td></tr><tr><td>Robert Kauffman</td><td>University of Minnesota, USA</td><td>Frank Land</td><td>London School of Economics, UK</td></tr><tr><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td><td>Yair Wand</td><td>University of British Columbia, Canada</td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Ritu Agarwal</td><td>University of Maryland, USA</td><td>Steve Alter</td><td>University of San Francisco, USA</td></tr><tr><td>Michael Barrett</td><td>University of Cambridge, UK</td><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td></tr><tr><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td><td>Francois Bodart</td><td>University of Namur, Belgium</td></tr><tr><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Yolande E. Chan</td><td>Queen&#x27;s University, Canada</td><td>Dave Chatterjee</td><td>University of Georgia, USA</td></tr><tr><td>Roger H. L. Chiang</td><td>University of Cincinnati, USA</td><td>Wynne Chin</td><td>University of Houston, USA</td></tr><tr><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td></tr><tr><td>Dennis Galletta</td><td>University of Pittsburg, USA</td><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td></tr><tr><td>Matthew R. Jones</td><td>University of Cambridge, UK</td><td>Bill Kettinger</td><td>University of South Carolina, USA</td></tr><tr><td>Rajiv Kohli</td><td>Colleage of William and Mary, USA</td><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td></tr><tr><td>Ho Geun Lee</td><td>Yonsei University, Korea</td><td>Jae-Nam Lee</td><td>Korea University</td></tr><tr><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td></tr><tr><td>Ann Majchrzak</td><td>University of Southern California, USA</td><td>Ji-Ye Mao</td><td>Remnin University, China</td></tr><tr><td>Anne Massey</td><td>Indiana University, USA</td><td>Emmanuel Monod</td><td>Dauphine University, France</td></tr><tr><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>B. Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td><td>Paul Palou</td><td>University of California, Riverside, USA</td></tr><tr><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td><td>Nava Pliskin</td><td>Ben-Gurion University of the Negev, Israel</td></tr><tr><td>Jan Pries-Heje</td><td>Copenhagen Business School, Denmark</td><td>Dewan Rajiv</td><td>University of Rochester, USA</td></tr><tr><td>Sudha Ram</td><td>University of Arizona, USA</td><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td><td>Katherine Stewart</td><td>University of Maryland, USA</td></tr><tr><td>Kar Yan Tam</td><td>University of Science and Technology, Hong Kong</td><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td></tr><tr><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td><td>Richard T. Watson</td><td>University of Georgia, USA</td></tr><tr><td>Bruce Weber</td><td>London Business School, UK</td><td>Richard Welke</td><td>Georgia State University, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University, USA</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
