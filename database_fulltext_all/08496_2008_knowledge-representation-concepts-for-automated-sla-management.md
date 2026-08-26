---
otero_id: 8496
otero_key: "86KCW6KT"
title: "Knowledge representation concepts for automated SLA management"
authors: "Adrian Paschke; Martin Bichler"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.06.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge representation concepts for automated SLA management

Adrian Paschke ⁎, Martin Bichler

Internet-based Information Systems, Department of Informatics, TU München, Boltzmannstr. 3, D-85748 Garching, Germany

a r t i c l e i n f o

Article history: Received 11 September 2006 Received in revised form 6 June 2008 Accepted 20 June 2008 Available online 1 July 2008

Keywords: Service Level Agreements (SLA) Service Level Management (SLM) Logic Programming (LP) Rule-based Knowledge Representation (KR) Business rules Policy management

## a b s t r a c t

Outsourcing of complex IT infrastructure to IT service providers has increased substantially during the past years. IT service providers must be able to ful<sup>fi</sup>l their service-quality commitments based upon prede<sup>fi</sup>ned Service Level Agreements (SLAs) with the service customer. They need to manage, execute and maintain thousands of SLAs for different customers and different types of services, which needs new levels of <sup>fl</sup>exibility and automation not available with the current technology. The complexity of contractual logic in SLAs requires new forms of knowledge representation to automatically draw inferences and execute contractual agreemen ts. A logic-based approach provides several advantages including automated rule chaining allowing for compact knowledge representation as well as <sup>fl</sup>exibility to adapt to rapidly changing business requirements. We suggest logical formalisms for the representation and enforcement of SLA rules and describe a proof-of-concept implementation. The article describes selected formalisms of the ContractLog KR and their adequacy for automated SLA management and presents results of experiments and examples from common industry use cases to demonstrate the expressiveness of the language and the scalability of the approach.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Outsourcing of complex IT infrastructure to IT service providers has become increasingly popular and led to much recent development. To ensure Quality of Service (QoS) between the service customer and the provider, they jointly de<sup>fi</sup>ne a Service Level Agreement (SLA) as a part of a service contract that can be monitored by either party or a third party. An SLA provides metrics for measuring the performance of the agreed upon Service Level Objectives (SLOs). SLA rules are used to monitor service execution and detect violations of SLOs. SLAs are fundamental not only for outsourcing relationships, but for any kind of service supply chain and assume a central position in popular IT service management standards such as ITIL (www.itil.co.uk). As a consequence, IT service providers need to manage, execute and maintain thousands of SLAs for different customers and different types of services in the upcoming service-oriented computing landscape. Commercial service level management tools such as IBM Tivoli™, HP OpenView™, and Microsoft Application Center™ store selected QoS parameters such as availability or response time as parameters in the application code or database tiers. This approach is restricted to simple, static rules with only a limited set of parame ters. We have analyzed a large number of text-only real-world SLAs [46] and found various types of complex rules which need to be enforced by IT service providers such as graduate rules, dependent rules, normative rules, default rules, and exception rules. In most cases these SLA rules are part of a hierarchical set of contracts, consisting of a basic agreement with general terms and conditions, a group-level service agreement, one or more SLAs and internal operation level agreements (OLAs) or underpinning contracts (see Section 2.1 and e.g. [46]). These types of interlinked, unitized rule sets with multiple conditions which are possibly scattered among business partners, organizations or departments demand for advanced knowledge representation (KR), which allows an IT service provider to analyze, interchange, manage and enforce large amounts of (decentralized) rules and adapt them during run time. Moreover, traceability and veri<sup>fi</sup>ability of drawn conclusions (e.g. derived penalties) and triggered reactions during contract monitoring and enforcement is a requirement in order to ful<sup>fi</sup>l legal regulations and compliance rules.

In this article we propose a declarative rule-based approach to SLA representa tion and management. Whereas existing approaches to standardize SLAs are based on imperative procedural or simple propositional logic (see Section 6), we draw on logic programming (LP) and related knowledge representation concepts. LP allows for a compact knowledge representation of SLA rules and for automated rule chaining by resolution and variable uni<sup>fi</sup>cation, which alleviates the burden of having to implement extensive control <sup>fl</sup>ows as in imperative programming languages and allows for easy extensibility. However, further logical formalisms are needed for automated SLA management. We propose an expressive framework of adequate KR concepts, called ContractLog, which combines a labelled, typed and prioritized logic, reactive rules and complex event processing, temporal event logics (event calculus), defeasible logic, deontic logic, description logic and veri<sup>fi</sup>cation and validation techniques for the domain of SLA management. In particular, the integration of reactive and derivation rules with complex event/action processing, KR based event logics, deontic norms and procedural attachments enables an adequate representation of contractual rules as they can be found in SLAs nowadays. ContractLog enables the speci<sup>fi</sup>cation of contractual logic in a formal, declarative machine-readable and executable fashion and supports calls to object-oriented code (Java) or existing system monitoring tools.

The main contribution of this paper is an evaluation of the expressiveness of the ContractLog language and its adequacy for the SLA domain, plus an empirical analysis of the computational complexity of rule chaining in large numbers of SLA rules. We demonstrate its adequacy with several examples derived from common industrial use cases. Performance considerations are essential, since SLA Management typically deals with hundreds or thousands of contracts, and a logic programming approach needs to satisfy tight response time requirements, also for large-scale SLA Management applications.

Contrary to numerous empirically oriented studies in IS research of the last years and pure theoretical works in logics, the presented approach follows a constructivist, software engineering-oriented methodology and presents an implementation. It adopts the Design Science Research approach as described in Hevner et al. [14] and proposes ContractLog as a new design artifact, which tackles the prescriptive design problem which is in engineering an assemblage of adequate components for improving SLA representation, monitoring and enforcement. This rule-based artifact helps to overcome real-world problems which are of high relevance and importance for IT service provider such as insuf<sup>fi</sup>cient automation of IT service level management based on SLAs or slow change cycles of contractual agreements in rapidly changing, highly-distributed and loosely coupled service-oriented environments.

The article is organised as follows: We <sup>fi</sup>rst provide an overview of SLAs in Section 2, de<sup>fi</sup>ne relevant terms, introduce a use case based on real-world industrial SLAs and discuss requirements. In Section 3 we describe the ContractLog KR and the selected logical formalisms for the adequate representation of SLAs. In Section 4 we introduce superimposed rule-based service level management tools (RBSLM) which serves as a proof-of-concept implementation. Section 5 presents experimental evaluations and illustrates the rulebased formalization of SLA rules in the ContractLog KR based on the use case example de<sup>fi</sup>ned in Section 3. Section 6 discusses related work. Finally, Section 7 concludes with a short summary of key <sup>fi</sup>ndings.

## 2. Problem statemen

An SLA is a document that describes the performance criteria a provider promises to meet while delivering a service. It typically sets out the remedial actions and penalties that will take effect if performance falls below the agreed service levels. It is an essential component of the legal contract between a service consumer and the provider. [20] In the following, we will describe relevant terms, before we introduce a use case that we will use later for the evaluation.

## 2.1. Terminology

SLA rules represent guarantees with respect to graduated high/low ranges of metrics (e.g., average availability range [low: 95% , high: 99%, median: 97%]) so that it can be seen whether the measured metrics exceed, meet or fall below the de<sup>fi</sup>ned service levels during a certain time interval. They can be informally represented as rules which might be chained in order to form graduations, complex policies and conditional guarantees, e.g., “if the average service availability during one mon th is below 95% then the service provider is obliged to pay a penalty of 20% of the monthly service fee”. According to their intended purpose, their scope of application or their versatility, SLAs can be grouped into different categories. In this paper, we use the terms described in Table 1.

Service Level Agreements come in several varieties and comprise different technical, organizational or legal components. Table 2 lists some typical contents.

Although the characteristics and clauses may differ considerably among different contracts, they all include more or less static parts such as the involved parties, the contract validity period or the service de<sup>fi</sup>nitions. But the main part of a service contract is dynamic and more likely to change. It contains QoS de<sup>fi</sup>nitions stated as SLA rules specifying, e.g., service level guarantees and appropriated actions to be taken if a contract violation has been detected according to measured performance values. The representation of the static part of an SLA is straightforward. From the point of view of rule-based decision/contract logic they can be simply represented as facts managed in the knowledge base (KB) or in an external datasource such as a relational database or in Semantic Web documents, e.g. in RDF format. In this article we focus on the dynamic part of an SLA — the SLA rules.

Table 1 SLA categorization

<table><tr><td colspan="2">Purpose of the contract</td></tr><tr><td>Basic agreement</td><td>Defines the general framework for the contractual relationship and is the basis for all subsequent SLAs.</td></tr><tr><td>Group-level service agreement</td><td>Subsumes all components which apply to several subordinated SLAs.</td></tr><tr><td>Service level agreement</td><td>Main contract between service provider and service customer.</td></tr><tr><td>Operation level agreement (OLA)</td><td>A contract with internal operational partners, needed to fulfil an SLA.</td></tr><tr><td>Underpinning contract (UC)</td><td>A contract with an external operational partner.</td></tr></table>

Table 2  
Categorization of SLA contents

<table><tr><td>Technical components</td><td>Organizational components</td><td>Legal components</td></tr><tr><td>- Service description</td><td>- Liability/liability limitations</td><td>- Obligations to co-operate</td></tr><tr><td>- QoS metrics</td><td>- Level of escalation</td><td>- Legal responsibilities</td></tr><tr><td>-Actions</td><td>- Maintenance periods</td><td>- Proprietary rights</td></tr><tr><td>- ...</td><td>- Monitoring and reporting</td><td>- Modes of invoicing and payment</td></tr><tr><td></td><td>- Change management</td><td>- ...</td></tr><tr><td></td><td>- ...</td><td></td></tr></table>

## 2.2. SLA use case

In order to better illustrate the requirements of SLA management we will describe a use case derived from realworld SLA examples from an industry partner. The SLA de<sup>fi</sup>nes three monitoring schedules, “Prime”, “Standard” and “Maintenance” (Table 3).

During prime time the average availability is de<sup>fi</sup>ned by a low value of 98%, a median of 99% and a high value of 100% and a response time which must be below 4 s. The service metrics are calculated via a ping every 10 s. During standard time, the average availability is {high: 99%; low: 95%; median: 97%} and the response time is {high: 10 s; low: 16 s; median: 14 s} monitored via a ping every minute. Maintenance is permitted to take place between midnight and 4 a.m. During this period the average availability is {high: 80%; low: 20%; median: 50%} monitored every 10 min. Response time will not be monitored in this case. Further the SLA de<sup>fi</sup>nes a “bonusmalus” policy (Table 4).

According to the monitoring schedules a differentiated base price (p<sub>prime</sub>, p<sub>standard</sub>, p<sub>maintenance</sub>) is de<sup>fi</sup>ned if the service levels are met. If the service levels are exceeded (median to high) a bonus is added and if they fall below the agreed upon service levels (median to low) a discount is deducted. The bonus and malus are de<sup>fi</sup>ned as a percentage value $( x _ { \mathrm { b o n u s } } , \ x _ { \mathrm { m a l u s } } )$ of the base price. If a service level is missed, i.e. the actual value falls below the low service level (blow) an additional penalty $( p _ { \mathrm { i n c i d e n t } } )$ has to be paid which increases exponentially with the number (n) of incidents during the accounting period. In case of outages/incidents the SLA de<sup>fi</sup>nes two escalation levels (Table 5).

Table 3 Monitoring schedule

<table><tr><td>Schedule</td><td>Time</td><td>Availability</td><td>Response time</td></tr><tr><td>Prime</td><td>8 a.m.-18 p.m.</td><td>98% [99%] 100%; pinged every 10 s</td><td>4 s.; pinged every 10 s</td></tr><tr><td>Standard</td><td>18 p.m.-8 a.m.</td><td>95% [97%] 99%; pinged every min.</td><td>10 [14] 16 s.; pinged every min.</td></tr><tr><td>Maintenance</td><td>0 a.m.-4 a.m.*</td><td>20% [50%] 80%; pinged every 10 min</td><td>No monitoring</td></tr></table>

Table 4  
“Bonus Malus” price policy

<table><tr><td>Price</td><td>Base</td><td>Bonus</td><td>Malus</td></tr><tr><td>Prime</td><td> $p_{prime}$ </td><td> $p_{prime} + p_{prime} * x_{bonus}$ %</td><td> $p_{prime} - p_{prime} * x_{malus} \%$ </td></tr><tr><td>Standard</td><td> $p_{standard}$ </td><td> $p_{standard} + p_{standard} * x_{bonus} \%$ </td><td> $p_{standard} - p_{standard} * x_{malus} \%$ </td></tr><tr><td>Maintenance</td><td> $p_{maintenance}$ </td><td> $p_{maintenance} + p_{maintenance} * x_{bonus} \%$ </td><td> $p_{maintenance} - p_{maintenance} * x_{malus} \%$ </td></tr><tr><td>Incident penalty</td><td> $-p^{n}_{incident}$ </td><td></td><td></td></tr></table>

Each escalation level de<sup>fi</sup>nes clear responsibilities in terms of associated roles which have certain rights and are obliged to do certain remedial actions in case of incidents which initiate the respective escalation level. In the SLAs' escalation level 1 the process manager is obliged to restart an unavail able service within 10 min. Accordingly, the process manager has the right (permission) to start and stop the service. If he fails to do so, escalation level 2 is triggered and the quality manager is informed. The quality manager has more rights, e.g. the righ t (permission) to adapt/change the SLA management systems respectively the service levels within the maximum agreed values. For instance, the quality manager might discuss the time needed to repair with the process manager and extend it up to the agreed maximum time to repair level (change request). In case of very critical incidents the system might directly proceed to escalation level 2 and skip level 1.

## 2.3. Requirements of a rule-based SLA language

From our analysis of the SLA domain and the example in the last subsection, the following top-level requirements for a declarative, logic-based rule language for representing SLAs can be derived:

1. Different kinds of rules and facts: A logic-based SLA language should allow to coherently represent derivation rules, reaction rules, integrity rules and deontic rules in a homogeneous syntax and homogenous knowledge base. Derivation rules are sentences of knowledge that are derived from other knowledge by an inference or mathematical calculation. Reaction rules are behavioural rules which react on occurred events or changed conditions by executing actions. Integrity rules (or constraints) are assertions which express conditions that must be always satis<sup>fi</sup>ed. Deontic rules describe rights and obligations of roles in the context of evolving states and state transitions.

Table 5  
Escalation levels with role models and associated rights and obligations

<table><tr><td>Level</td><td>Role</td><td>Time-to-Repair (TTR)</td><td>Rights/obligations</td></tr><tr><td>1</td><td>Process manager</td><td>10 min</td><td>Start/stop service</td></tr><tr><td>2</td><td>Quality manager</td><td>Max. Time-to-Repair (MTTR)</td><td>Change service levels</td></tr></table>

2. Interoperation with (webized) descriptive domain speci-<sup>fi</sup>cations: An SLA language for contracts in open distributed domains such as the Semantic Web should be able to refer to external (Semantic Web) ontologies by means of URIs in order to use the vocabularies as type systems for terms in rules. Domain-independent SLA rules can be given a domain-dependent meaning (with a precise semantics) and accordingly rules can be much more easily interchanged and managed/maintained in a distributed environment. The core SLA rule language stays compact and can be <sup>fl</sup>exibly extended with different domain-speci<sup>fi</sup>c vocabularies on an “as-needed-basis”.

3. Practical procedural language constructs such as constructive queries on external data sources, expressive procedural attachments and ex ternal type systems which allow calling external functionalities and using ex ternal objects and data during rule execution. Many SLA rules refer to or describe measurement functions over data stored in some kind of external database which can be anything from log <sup>fi</sup>les to web sources or relational databases and data warehouses. The rule language must allow the direct integration of these secondary data storages as facts into the rules in order to reduce redundancy and high memory consumption. It should also support outsourcing of expensive (pre-)processing of data to an external system, e.g., by using SQL aggregation queries.

4. Ef<sup>fi</sup>cient operational semantics and declarative semantics: A declarative reading of the SLA logic language with declarative semantics for extended LPs is needed, with default and explicit negation, dynamic knowledge selfupdates and support for open and close reasoning by scoped reasoning on explicitly close parts of open, distributed and Web-based KBs. The operational semantics of a SLA rule language should support automated rule chaining based on backward-reasoning in order to cope with masses of frequently changing data. External functionalities such as procedural code, description logic ontology reasoning or data queries on external data sources (relational databases, XML web sources/services etc.) should be in tegrated in a hybrid way in order to exploit ef<sup>fi</sup>cient external reasoners, procedural functionalities and highly optimized query languages.

6. Modularization and quanti<sup>fi</sup>cations with metadata labels and priorities: IT service contracts include rules on different contractual levels such as general conditions, agreements on service properties, agreements on service usage, operational/measurement rules on IT infrastructure level, and (business) policies. Moreover, the agreements, policies and rule sets are typically managed in a distributed way and are scattered over domain boundaries. To support such distributed KBs in open environments such as the Semantic Web, rule sets should be bundled to modules. Modules might be written and managed as stand alone scripts provided on the Web. They have their own unique identi<sup>fi</sup>ers, e.g. their URIs, from which they are imported into the running SLA system. Rules and modules should be possibly labelled by additional metadata such as rule names/identi<sup>fi</sup>ers, authoring information such as Dublin Core metadata or quali<sup>fi</sup>cations such as validity times or priority values.

8. Transactional dynamic updates: The dynamic character of the SLA domain where contracts and in particular SLA rules need to be adapted to changing requirements and environments requires declarative mechanisms to maintain and evolve the SLA speci<sup>fi</sup>cations. That is, the intensional (rules) and extensional (facts) KB needs to be updated frequently, rules and complete modules need to be added and removed and the knowledge sta tes need to be transited to evolved knowledge states, leading to a sequence of state transitions which might possibly be rolled back in a transactional style if (integrity) constraints are violated.

9. Veri<sup>fi</sup>cation, validation, integrity testing and con<sup>fl</sup>ict resolution: Measurement of the quality, anomaly freeness and well-formedness of the rule sets used to formalize SLAs is an important need for the acceptance by the contract partners, in particular when rules are subject to change and have different information sources. Basically this means using verification, validation and integrity preserving techniques and providing means to solve rule conflicts which occur in different situations, in particular if modular revisioning/updating is allowed, i.e., new behaviour can be speci<sup>fi</sup>ed by simply adding rules without the need to modify or delete previous rules. Expressive integrity constraints (integrity rules) are an appropriate way to represent all sorts of domain-speci<sup>fi</sup>c and logical con<sup>fl</sup>icts. (User-de<sup>fi</sup>ned) preferences written as priority relations between rules or rule sets (modules) can be used to address consistency and coherence w.r.t. to the violated integrity constraints, i.e. the semantics should decide whether and how it is possible to (defeasibly) derive the expected conclusions w.r.t. to the de<sup>fi</sup>ned integrity constraints and priority de<sup>fi</sup>nitions. Veri<sup>fi</sup>cation and validation is also vital for collaborative engineering of larger rule sets (contracts) and interchanging rule bases in different execution environments on the Semantic Web.

10. Support for normative reasoning on deontic rules: The main aim for concluding a contract is to arrange the normative relationships relating to permissions, obligations, prohibitions and other normative modalities between contract partners. These contract norms must be personalized based on role models de<sup>fi</sup>ned in relational database schemas or Semantic Web taxonomies and must be quali<sup>fi</sup>ed in an extensible way.

This list of requirements describes only the top level of critical success factors and many other requirements can be derived from them. All these requirements have to be satis<sup>fi</sup>ed and integrated into a single framework. It is crucial to <sup>fi</sup>nd the right trade-off between generality, expressiveness, strictly (classical) logical semantics and the practical integration of non-classical inference features and practical concepts such as procedural attachments. In the next section we will further expand on these requirements and introduce the ContractLog KR as a solution to tackle these issues in an adequate and coherent framework. We have also addressed engineering and rendering issues with our RBSLA (Rule-Based Service Level Agreement) mark-up language and the RBSLM (Rule-Based Service Level Management) tool which will be described in Section 4. But, the focus in this article is on the logical core, the ContractLog KR and its evaluation in terms of expressiveness and scalability in Section 5.

## 3. ContractLog KR

ContractLog [41,42,26] is an expressive and computationally tractable KR framework consisting of adequate KR concepts used to describe contracts and SLAs resp. It combines selected logical formalisms which are all implemented on the basis of logic programming (mainly a meta programming approach based on derivation rules). It provides a typed, labelled, unitized and prioritized logic with extended Javabased procedural attachments which enable reuse of external (procedural) functionalities, tools and data directly into declarative LPs.

## 3.1. Notation and semantics of ContractLog

In this article we use the standard LP notation and extended logic programs with default negation and explicit negation for the knowledge base. We assume that the reader is familiar with basic Horn theory and logic programming, see e.g. [11] and [6].

## 3.1.1. Core syntax and semantics of ContractLog

A ContractLog LP is an extended LP (ELP). An ELP is a set of clauses (rules) of the from $H \gets B ,$ , where H is a literal over the language L called the head of the derivation rule, and B is a set of literals over L called the body of the rule. A literal is either an atom or the negation “\~” or “¬” of an atom, where “\~” is denoted as default negation and “¬” as explicit negation. Roughly, default negation means, everything that can not be proven as true is assumed to be false. A rule is called a fact if it only consists of the rule head H←. An atom is a n-ary formula containing terms $p ( a , X , f ( \ldots ) )$ , where p is the predicate name. A term is either a constant a, a (possibly free) variable X or a n-ary complex term/function $\mathbb { f } ( \ldots ) .$ . A goal/query G? is a headless clause de<sup>fi</sup>ning a conjunction of literals (positive or negative atoms) ← $. L _ { 1 } \land \dotsc \land L _ { i }$ where each L is called a subgoal.

The ContractLog KR uses an extended ISO Prolog related scripting syn tax (ISO Prolog ISO/IEC 13211-1:1995) called Prova (http://www.prova.ws/, [17]) to write ContractLog LPs as scripts, where a variable starts with an upper-case letter, e.g. X,Y,Z, a constant/individual with a lower-case letter, e.g. a, b,c and a query is written as a function :-sovle(…) or :-eval $( \ldots ) ,  \mathrm { i } s$ denoted by $" \cdot "$ and by “,”. Default negation is written as not(…), e.g., not(p()), and explicit negation as neg $( \ldots ) , \mathrm { e . g . , n e g } ( p ( ) )$

ContractLog is intended to be a general KR framework which is applicable to various rule languages and declarative LP semantics such as well-founded semantics (WFS) or stable model semantics (STABLE) respectively answer set semantics (ASS). Due to the use of general meta programs, the ContractLog KR to a large extent avoids a strong commitment to one particular LP semantics used to interpret the formalisms of the KR and allows for direct implementations respectively transformations on top of many existing rule languages [26].

## 3.1.2. Representation of contract rules/business rules

Before we elaborate on further (non-monotonic) logical formalisms and rule types which are needed for adequately formalising SLAs, we brie<sup>fl</sup>y demonstrate the general applicability of derivation rules (as described above) for the representation of contract rules and in particular for the representation of SLA rules and higher-level policy rules. SLA rules typically have the form “if … then… (else)”. Such informal rules can be formalized as a set of prerequisites (conditions) which form the body of a derivation rule and a conclusion (consequent) which forms the head of the rule. The rules are relatively easy to write since the user only needs to express what (decision logic) they want. The responsibility to interpret this and to decide on how to do it is delegated to an inference engine. Table 6 provides an example of the translation of an informal business rule set, which might occur in a SLA.

Negation can be formalized with either default or explicit negation, depending on the intention. For example, rules with epistemic character such as “if X is not believed to be a valuable customer, then X is assigned standard level” might be formalized with default negation as follows: standard (Customer) :- not(spending(Customer, N1000\$, last year), i.e. the rule expresses a default rule which holds in case that there is no information about the spending at all or the spending of the customer was less than 1000\$ in the last year. It should be noted that our reference implementation of the ContractLog inference engine preserves the linearity property of SLD(NF)- style resolution and combines it with linear goal memoization and a four-valued logic to support extended well-founded semantics, so that strictly sequential operators such as cuts and serial rules with update primitives and procedural calls are still possible (in contrast e.g. to the typical SLG resolution as implemented e.g., in XSB). [26,27] In the following we will introduce several logical extensions to the core concept of extended ContractLog LPs and derivation rules, which are needed to adequately formalize SLA rules.

## 3.2. Typed logic and procedural attachments

SLA rules are typically de<sup>fi</sup>ned over external business objects and business/contract vocabularies, which map to internal logical object representations in order to give SLA rules a domain-speci<sup>fi</sup>c meaning. Moreover, service level management tools do not operate on a static internal fact base but access a great variety of external systems such as system and network management tools. From a software engineering (SE) point of view the lack of types, as in standard LP languages (e.g. Prolog), can been seen as a serious restriction for implementing larger rule-based systems and SLA decision logics which are engineered and maintained by different people. Typical SE principles such as data abstraction and modularization are not directly suppor ted. Therefore, rulebased SLA engineering can bene<sup>fi</sup>t from a type concept which enables static and dynamic type checking. Types capture the developer's intended meaning of a logic program, increase the expressiveness and the readability of the formalized SLAs,

## Table 6

Example of a business rule set

(r1) “If customer has spent more than 1000\$ in the last year then customer is a bronze customer.

(r2) “If the customer is a bronze customer he will get a discount of 5%.” (r1) discount(Customer, 5%) :- bronze(Customer).

(r2) bronze(Customer) :- spending(Customer, Value, last year), Value N1000 Fact: spending(Peter Miller, 1200, last year).

detect type errors and increase robustness and reduce the search space of goals and accordingly optimize the ef<sup>fi</sup>ciency.

Types in ContractLog are de<sup>fi</sup>ned by a type relation t:r, denoting that term t has a type r . ContractLog supports two different external type systems: Object-oriented Java class hierarchies and Description Logic Semantic Web ontologies. The typed uni<sup>fi</sup>cation in ContractLog follows a hybrid approach and uses an external reasoner integrated via logical entailment for dynamic type checking and type conversion during uni<sup>fi</sup>cation of typed or untyped terms; hence leading to a hybrid, typed logic language. [28,29].

## 3.2.1. Java types

The object-oriented type system of Java is essentially a static type system in the sense that is does not allow parametric polymorphic type parameteriza tion (except for generics available since Java 1.5). It supports inheritance (subclassing) and ad-hoc polymorphism with overloading and coercion (casting) as a kind of automatic type conversion between classes. In the ContractLog language the fully quali<sup>fi</sup>ed name of the class to which a typed term/variable should belong to must be used. During uni<sup>fi</sup>cation of terms ContractLog then uses the declared types, assuming the root Java type “Object” if no information is given (= untyped variable) and tries to unify the terms using the Java instanceof operator to compute subclass relations, i.e. it uses Java for dynamic type checking. For example, a typed variable java. lang.Integer X uni<sup>fi</sup>es with a variable java.lang.Number Y since the class Number is a super class of Integer.

## 3.2.2. Semantic web DL types

In ContractLog external RDFS or OWL ontologies describing types (concept classes) and constant objects (individuals) can be dynamically imported to the knowledge base. Different external DL reasoners like Racer (www.sts.tu-harburg.de/\~r.f. moeller/racer/), Pellet (www.mindswap.org/2003/pellet/) or Jena (jena.sourceforge.net/) for e.g. RDFS, OWL Lite, OWL DL reasoning can be con<sup>fi</sup>gured and hybridly used in ContractLog. [28,29].

Example 1. discount(X:businessVoc1\_Customer, math\_ Percentage:10) :- gold(X: businessVoc1\_Customer).

## 3.2.3. Java-based procedural attachments

Another extension of ContractLog to logic programming is the concept of procedural attachments which are used to dynamically instantiate and bind Java objects at runtime and call their external Java-based procedural functions/methods during resolution (see [17,18]). They enable the reuse of pro cedural code and facilitate the dynamic integration of facts from external data sources such as relational databases (via JDBC/SQL). Java object instantiations of particular types (classes) can be bound to variables having appropriate types. During resolution the methods and attributes of the bound Java object can be used as procedural attachments within rule bodies. Class and instance methods can be dynamically invoked (via Java re<sup>fl</sup>ection) taking arguments and returning a result which can possibly alter the state of the knowledge base. Basically, (1) Boolean-valued attachments which can be used on the level of atoms in the rule body and (2) object valued attachments which are treated as functions that take arguments and are executed in the contex t of a particular object or class in case of static method calls (see Example 2), can be used.

Example 2. add(java.lang.Integer.In1, java.lang.Integer.In2, Result):- … Result=In1+In2

add(In1, In2, Result):- I1=java.lang.Integer(In1), I2=java. lang.Integer(In2), X =I1 + I2, Result= X.toString().

3.3. Reactive rules: Event-Condition-Action rules (ECA rules) and messaging reaction rules

In SLA execution event-driven reactive functionalities are an obvious necessity. Typical SLA rules describe reactive decision logics following the Event-Condition-Action (ECA) paradigm, e.g. “if service is unavailable (event) and it is not maintenance time (condition) then send noti<sup>fi</sup>cation (action)”. These ECA rules are de<sup>fi</sup>ned globally and are best suited to represent reaction rules that actively detect or query internal and external events and trigger reactions in a global context. For instance, to actively monitor an external system, data source, or service and to trigger a reaction whenever the system/service becomes unavailable. In a distributed serviceoriented environment with independent system nodes that communicate with each other relative to a certain context (e.g. a work<sup>fl</sup>ow, conversation protocol state or complex event situation), event processing requires event noti<sup>fi</sup>cation and communication mechanisms, and often needs to be done in a local context, e.g. a conversation state or (business) process work<sup>fl</sup>ow. Systems either communicate events according to a prede<sup>fi</sup>ned or negotiated communication/coordination protocol or they subscribe to speci<sup>fi</sup>c event types on a server (publish-subscribe). In the latter case, the server monitors its environment and upon detecting an atomic or complex event (situation), noti<sup>fi</sup>es the concerned clients.

## 3.3.1. Syntax of reaction rules in ContractLog

The Event-Condition-Action logic programming language (ECA-LP) [26,30,45,31] represents an extended ECA rule as a 6-ary function ECA(T,E,C,A,P,EL), where T (time), E (event), C (condition), A (action), P (post-condition), EL(se) are complex terms which are interpreted as queries/goals on derivation rules. The derivation rules are used to implement the respective functionality of each of the ECA rules' parts. A complex term is a logical function of the form c(C1,…, Cn) with a bound number of arguments (terms) which might be constant, variable or again complex. Boolean-valued procedural attachments, as de<sup>fi</sup>ned in Section 3.2, are supported in ECA rules and can be directly used instead of a complex term. While the E, C, A parts of an ECA rule comply with the typical de<sup>fi</sup>nitions of standard ECA rules (omitted here), the T, P and EL part are special extensions to ECA rules:

• The time part (T) of an ECA rule de<sup>fi</sup>nes a pre-condition (an explicitly stated temporal event) which speci<sup>fi</sup>es a speci<sup>fi</sup> point in time at which the ECA rule should be processed by the ECA processor, either absolutely (e.g., “at 1 p.m. on the 1st of May 2007”), relatively (e.g., “1 min after event X was detected”) or periodically (e.g., “every 10 s”).

• The post-condition (P) is evaluated after the action. It might be used to prevent backtracking from different variable bindings carrying the context information from the event or condition part via setting a cut. Or, it might be used to apply veri<sup>fi</sup>cation and validation tests on performed update actions using integrity constraints or test cases. If the update violates the integrity test of the post-condition, it is automatically rolled back.

• The else part (EL) de<sup>fi</sup>nes an alternative action which is execute alternatively in case the ECA rule can not be applied, e.g. to specify a default action or trigger some failure handling (re-)action.

In order to integrate the (re)active behaviour of ECA rules into goal-driven backward-reasoning the goals de<sup>fi</sup>ned by the complex terms in the ECA rules need to be actively used to query the knowledgebase and evaluate the derivation rules which implemented the functionality of the ECA rules' parts. Hence, an ECA rule is interpreted as a conjunction of goals (the complex terms) which must be processed in a left-to-right sequence starting with the goal denoting the time par t, in order to capture the forwarddirected operational semantics of ECA rules: ECA? = T ٨ E ٨ ((C ٨ A ٨ P) ٧ EL), where ECA? is the top goal and T,E,C,A,P, EL are the subgoals. An ECA rule succeeds, if all subgoals succeed.

The task of interpreting ECA rules and executing the de<sup>fi</sup>ned goals is solved by an active ECA processor with a daemon process which is build on top of the rule engine. The ECA processor implements a general wrapper interface in order to be applicable to arbitrary backward-reasoning rule engines. The daemon frequently queries the KB for new or updated ECA rules via the query eca(T,E,C,A,P,EL)? and adds the found ECA rules to its active KB, which is a kind of volatile storage for reactive rules. It then evaluates the ECA rules one after another via using the complex terms de<sup>fi</sup>ned in the ECA rule as queries on the KB.

In contrast to standard Event-Condition-Action (ECA) reaction rules which typically only have a global state, messaging reaction rules [45] maintain a local conversation state which re<sup>fl</sup>ects the process execution state and support performing of different activities within process instances managed in simultaneous conversation branches. Messaging reaction rules do not require separate threads for handling multiple conversation situations simultaneously. They describe (abstract) processes in terms of message-driven conversations between parties and represent their associated interactions via constructs for asynchronously sending and receiving event messages:

sendMsg(XID,Protocol,Agent,Performative,Payload|Context) rcvMsg(XID,Protocol,From,Performative,Paylod|Context) rcvMult(XID,Protocol,From,Performative,Paylod|Context)

where XID is the conversation identi<sup>fi</sup>er (conversation-id) of the conversation to which the message will belong. Protocol de<sup>fi</sup>nes the communication protocol (more than 30 protocols such as JMS, HTTP, SOAP, Jade are supported by the underlying enterprise service bus as ef<sup>fi</sup>cient and scalable object-broker and communication middleware [27]). Agent denotes the target (an agent or service wrapping an instance of a rule engine) of the message. Performative describes the pragmatic context in which the message is send. A standard nomenclature of performatives is e.g. the FIPA Agents Communication Language ACL. Payload represents the message content sent in the message envelope. It can be a speci<sup>fi</sup>c query or answer or a complex interchanged rule base (set of rules and facts).

Example 3. % Upload a rule base read from File to the host at address Remote via JMS

upload\_mobile\_code(Remote,File) :-

% Opening a <sup>fi</sup>le returns an instance of java.io. BufferedReader in Reader

fopen(File,Reader), Writer = java.io.StringWriter(),

copy(Reader,Writer), Text = Writer.toString()

% SB will encapsulate the whole content of File

SB=StringBuffer(Text), sendMsg(XID,jms,Remote,eval, consult(SB)).

The example shows a messaging reaction rule that sends a rule base from an external <sup>fi</sup>le to the agent service Remote using JMS as transport protocol. The inline sendMsg reaction rule is locally used within a derivation rule, i.e. only applies in the context of the derivation rule.

## 3.3.2. Representation of reactive rules

To illustrate the usage and formalization of ECA rules in ContractLog, consider an ECA rule which states that:

Example 4. Every 10 s it is checked (time) whether there is a service request by a customer (event). If there is a service request a list of all currently unloaded servers is created (condition) and the service is loaded to the <sup>fi</sup>rst server (action). In case this action fails, the system will backtrack and try to load the service to the next server in the list. Otherwise it succeeds and further backtracking is prevented (postcondition cut).

eca( every10 Sec(), detect(request(Customer, Service),T), <sup>fi</sup>nd(Server, Service), load(Server, Service), ! ).

% time derivation rule

every10 Sec() :- sysTime(T), interval( timespan(0,0,0,10),T). % event derivation rule

detect(request(Customer, Service),T):- occurs(request (Customer,Service),T), consume(request(Customer,Service)).

% condition derivation rule

<sup>fi</sup>nd(Server,Service) :- sysTime(T), holdsAt(status(Service, unloaded),T).

% action derivation rule

load(Server, Service) :- sysTime(T),

rbsla.utils.WebService.load(Server,Service), % procedural attachment

add(key(Server), “happens(loading(\_0),\_1).”, [Server, T]). % update KB with “loading” event

The state of each server might be managed via a KR event logics formalism such as the Event Calculus:

terminates(loading(Server),status(Server,unloaded),T). initiates(unloading(Server),status(Server,unloaded),T).

The conversation and event context based semantics of messaging reaction rules allows implementing typical semantics of state machines or work<sup>fl</sup>ow-style systems such as Petri nets or pi-calculus, which can be used for complex event processing and work<sup>fl</sup>ow process executions (e.g. in style of BPEL). [44] The declarative rule-based approach provides a highly expressive declarative programming language to represent complex conditional event processing logic, conditional reactions (activities) and complex eventbased work<sup>fl</sup>ow patterns.

3.4. Event/action logics: event calculus and interval-based event/action algebra

Pure reactive rule processing, as described in the last subsection, is concerned with detecting real-time event occurrences (volatile situations) and triggering immediate reactions. But, in SLA representation there is also a need for an event/action algebra and an temporal event/action logic which is used to de<sup>fi</sup>ne complex events / actions and reason over the effects of events/actions on the knowledge state. Typical examples found in SLAs are, for example, “After four outages then… ”, “If the service is unavailable it must be repaired within 10 min. If it is still unavailable afterwards then… ” or “If average availability is below 99% and maximum response time is more than 4 s then… ”.

## 3.4.1. Event calculus

Kowalski and Sergot's Event Calculus (EC) [19] is a formalism for temporal reasoning about events/actions and their effects on LP system as a computation of earlier events (longterm “historical” perspective). It de<sup>fi</sup>nes a model of change in which events happen at timepoints and initiate and/or terminate time-intervals over which some properties (time-varying fluents) of the world hold. The basic idea is to state that fluents are true at particular timepoints if they have been initiated by an event at some earlier timepoint and not terminated by another event in the meantime. The EC embodies a notion of default persistence according to which <sup>fl</sup>uents are assumed to persist until an event occurs which terminates them. In ContractLog we have implemented an optimized meta program formalization of the classical EC and extended it with an interval-based EC variant [37] and several other expressive features e.g. for planning, delayed effects, counters or deadlines [41,39]. The core EC axioms describe when events/actions occur (transient view)/happen (non-transient view)/are planned (planning view) and which properties (<sup>fl</sup>uents) are initiated and/or terminated by these events/ actions:

<table><tr><td>occurs(E,T)</td><td>Event/action E occurs at time interval T:= [T1,T2]</td></tr><tr><td>happens(E,T)</td><td>Event/action E happens at time T</td></tr><tr><td>planned(E,T)</td><td>Event/action E is planned at time T</td></tr><tr><td>initiates(E,F,T)</td><td>Event/action E initiates fluent F for all time &gt;T</td></tr><tr><td>terminates(E,F,T)</td><td>Event/action E terminates fluent F for all time &gt;T</td></tr><tr><td>holdsAt(F,T)</td><td>Fluent F holds at timepoint T</td></tr><tr><td>holdsInterval([E1,E2], [T1,T2])</td><td>Event/action with initiator E1 and terminator E2 holds between time T1 and T2</td></tr><tr><td>holdsInterval([E1,E2], [T1,T2],[&lt;Terminators&gt;])</td><td>With list of terminator events which terminate the event interval [E1,E2]</td></tr></table>

Example 5.  
![](/api/attachments/86KCW6KT/fulltext/images/03857089297587715789db9125f6cd99fb48090a2eaa416e20c671a7f38be840.jpg)

The example states that an event e1 initiates a <sup>fl</sup>uent f while an event e2 terminates it. An event e1 happens at timepoint t1 and e2 happens at timepoint t5. Accordingly a query on the <sup>fl</sup>uent f at timepoint t3 will succeed while it fails at timepoint t7. Note, that in ContractLog there is no restriction on the terms used within the EC axioms, i.e. a term can be a constant or DL individual, a (Java) object, a variable or even a complex term in a rei<sup>fi</sup>ed functional style which is uni<sup>fi</sup>ed with other rules. Moreover, it can be assigned a certain type dynamically at runtime.

3.4.2. Complex event/action algebra based on the interval-based event calculus

Based on an interval-based EC formalization we implement a logic-based event/action algebra which provides typical operators for de<sup>fi</sup>ning and computing complex events and actions, e.g. sequence, conjunction, disjunction, negation. As we have pointed out in [37] typical event algebras in the active database domain, such as Snoop [5], which considered events to be instantaneous, have unintended semantics and anomalies for several of their operators and the intervalbased treatment of complex events/actions in ContractLog helps to overcome these inconsistencies and irregularities. Moreover, the formal logical basis of the used KR event logics (event calculus) in ContractLog facilita tes reliable and traceable results. Using the holdsInterval axiom typical event algebra operators can be formalized in terms of an intervalbased EC variant. For example, the sequence operator “;” of Snoop, which de<sup>fi</sup>nes that the speci<sup>fi</sup>ed events/actions have to occur in the speci<sup>fi</sup>ed order, can be formalized as follows:

Sequence operator (;), e.g. (a;b;c)≡ detect(e,[T1,T3]) :- holdsInterval([a,b],[T1,T2],[a,b,c]), holdsInterval([b,c], [T2,T3],[a,b,c]), [T1,T2]b=[T2,T3].

The example de<sup>fi</sup>nes the detection conditions (detection rules) of a complex event e which is de<sup>fi</sup>ned by the two subevent intervals [a,b] and [b,c], where the <sup>fi</sup>rst interval must occur before the second [T1,T2]b=[T2,T3]. For both sub-event intervals a list of terminator events [a,b,c] is provided which might terminate the event intervals. In order to make de<sup>fi</sup>nitions of complex events more comfortable and remove the burden of de<sup>fi</sup>ning all interval conditions for a particular complex event type in terms of interval-based EC axioms as described above, we have implemented a meta program which implements an interval-based EC event algebra with the following axioms:

<table><tr><td>Sequence:</td><td>sequence(E1,E2,..., En)</td></tr><tr><td>Disjunction:</td><td>or(E1,E2,..., En)</td></tr><tr><td>Mutual exclusive:</td><td>xor(E1,E2,..., En)</td></tr><tr><td>Conjunction:</td><td>and(E1,E2,..., En)</td></tr><tr><td>Simultaneous:</td><td>concurrent(E1,E2,..., En)</td></tr><tr><td>Negation:</td><td>neg([ET1,..., ETn],[E1,E2])</td></tr><tr><td>Quantification:</td><td>any(n,E)</td></tr><tr><td>Aperiodic:</td><td>aperiodic(E,[E1,E2])</td></tr></table>

The Event Calculus and the EC based event algebra can be easily integrated into reaction rules via querying the EC axioms. For example, a SLA rule might de<sup>fi</sup>ne that (the state) escalation level 1 is triggered (action) in case a service $" s "$ is detected to be unavailable via a minutely (time) ping on the service (event), except we are currently in a maintenance state (condition). This can be formalized as an ECA rule: eca (everyMinute(), detect(unavailable(s),T), not(holdsAt( maintenance(s),T)), add(“”,happens( unavailable(s),T)))., i.e., in the condition part it is evaluated whether the state maintenance for the service s holds at the time of detection of the unavailable event or not. In short, the EC can be effectively used to model the effects of events on the knowledge sta tes and describe sophisticated state transitions akin to state machines. In contrast to the original use of ECA rules in active database management systems to trigger timely response when situations of interest occur which are detected by volatile vanishing events, the integration of event logics KR formalisms adds temporal reasoning on the effects of nontransient, happened (or planned) events on the knowledge system, i.e. enable traceable “state tracking”. They allow building complex decision logics based on a logical semantics as opposed to the database implementations which only have an operational semantics. As a result, the derived conclusions and triggered actions become veri<sup>fi</sup>able and traceable.

## 3.5. Deontic logic with norm violations and exceptions

One of the main objectives of a SLA is to de<sup>fi</sup>ne and reason with the normative relationships relating to permissions, obligations and prohibitions between con tract partners, i.e. to de<sup>fi</sup>ne the rights and obligations that each role has in particular state of the contract. Deontic Logic (DL) studies the logic of normative concepts such as obligation (O), permission (P) and prohibition (F). Adding deontic logic is therefore a useful concept for SLM tools, in particular with respect to traceability and veri<sup>fi</sup>ability of derived contract norms (rights and obligations).

In ContractLog we extended the general concepts of standard deontic logic (SDL) and integrated it into the event calculus implementation in order to model the effects of events/actions on personalized deontic norms in terms of changeable <sup>fl</sup>uents. [41,42] A deontic norm in ContractLog consists of the normative concept (norm), the subject (S) to which the norm pertains, the object (O) on which the action is performed and the action (A) itself. We represent a deontic norm as an EC <sup>fl</sup>uent of the form: norm(S, O, A).

Example 6. initiates(unavailable(Server), escl(1),T). terminates(available(Server), escl(1),T).

initiates(maintaining(Server),status(Server,maintenance), T). terminates(maintaining(Server),escl(1),T).

derived(oblige(processManager, Service, restart(Service))). holdsAt(oblige(processManager, Service, restart(Service)), T):- holdsAt(escl(1),T).

In the example above, the escalation level 1 is initiated resp. terminated, when a service becomes unavailable or available, e.g. happens(unavailable(s1), t1). The deontic obligation for the process manager to restart the service is de<sup>fi</sup>ned as a derived <sup>fl</sup>uent, i.e. it holds whenever the state escl(1) holds. If the process manager is permitted to start maintenance (e.g. between 0 a.m. and 4 a.m. — not shown here) the second and third rule state that the event maintaining(Server) will initiate maintenance and terminate the escalation level 1.

The integration of deontic logic concepts into the EC enables the de<sup>fi</sup>nition of sophisticated dependencies between events and contract norms. A norm represented as a <sup>fl</sup>uent can be initiated or terminated by an event and the EC allows inferring all actual contract state, i.e. the rights and obligations (deontic norms stated as <sup>fl</sup>uents) which hold at a speci<sup>fi</sup>c point in time according to the happened events (contract norm/state tracking).

3.6. Metadata labeled logic, scoped modules and ID-based updates

As discussed in Section 2.1 typical electronic contracts consist of a hierarchy of possibly distributed, interlinked and collaboratively engineered and maintained subcontracts. To capture this distributed (Web-based) open structure, enable scoped queries on explicitly closed parts of the formalized open and distributed contract knowledge and support principles of information hiding and modularization, we have extended the ContractLog KR to a general metadata annotated labelled logic with scoped reasoning. Metadata such as rule labels, module labels or Dublin Core annotations (e.g. author, date etc.) can be attached to rules and facts. To explicitly annotate clauses in a labelled LP with an additional set of metadata labels we introduce a general n-ary metadata () function in the ContractLog language: metadata $( l _ { 1 } , . . . , l _ { n } )$ :: H ← B, where l are a <sup>fi</sup>nite set of unary positive literals (positive metadata literals) which denote an arbitrary metadata “property(value)” pair, e.g. label(rule1). The explicit metadata() annotation is optional. Clauses (i.e. rules, facts and queries) are treated as objects having an unique object id (oid) which might be user-de<sup>fi</sup>ned, i.e. explicitly de<sup>fi</sup>ned by a label in the metadata annotations, e.g., metadata(label(boidN),…):: H←B or system-de<sup>fi</sup>ned i.e. automatically “labelled” with an auto-incremented object id (a increasing natural number) provided by the system at compile time. Rules and facts might be bundled to clause sets, so called modules, which also have an object id, the module oid. By default, the module oid is the webized or <sup>fi</sup>lesystem based URI of the imported ContactLog script which de<sup>fi</sup>nes the module. But it might also be userde<sup>fi</sup>ned.

The meta annotations of rules and rule sets (modules) enable meta reasoning with the semantic annotations and forms the basis for many expressive functionalities of the ContractLog KR, e.g., to de<sup>fi</sup>ne priorities between modules (see Section 3.7), add and remove rules or rule modules by their oid or de<sup>fi</sup>ne an explicit scope for constructive scoped queries on the open knowledge base consisting of dynamically imported web-based modules/rule scripts. Scopes are in particular useful to constrain and close-off queries to the open and distributed knowledge base, in particular in the context of default negated queries which need a closed world assumption on scoped parts of the knowledge base.

To support scoped reasoning, scoped literals are introduced into the ContractLog language:

metadata(bliteralN,bVariableN,bmetadata propertyN) query metadata value

metadata(bliteralN,bmetadata valueN,bmetadata propertyN) constrain scoped goal literal

scope(bliteralN,bmetadata valueN) scoped literal

Example 7. metadata(label(rule1), src(“http://rbsla.de module1”)):: p1(X):-scope(q(X),http://rbsla.de/module1).

metadata(label(rule2), src(http://rbsla.de/module2)):: p2(X):-scope(q(X),http://rbsla.de/module2).

metadata(label(fact1), src(http://rbsla.de/module1)):: q(1). metadata(label(fact2), src(http://rbsla.de/module2)):: q(2).

:-solve(scope(p1(X),http://rbsla.de/module1).

:-solve(scope(p2(X),http://rbsla.de/module2)).

:-solve(metadata(p1(X),RuleOID,label).

:-solve(metadata(p2(X),RuleOID,label).

The example shows scoped reasoning on explicitly closed parts of the knowledge base. The <sup>fi</sup>rst query has the userde<sup>fi</sup>ned scope http://rbsla.de/module1, i.e. a query on the module with the URI being the object id (oid) which is used as module label. Accordingly, the answer here is X=1. The second query has the scope http://rbsla.de/module2 and the answer is X=2. The third and fourth queries return the rule oid of both rules which is bound to the variable RuleOID, i.e. RuleOID=rule1 and RuleOID=rule2, i.e. they de<sup>fi</sup>ne queries on the set of metadata annotations.

In ContractLog we have implemented support for expressive (transactional) ID-based updates [26,30,31,37,38] which facilitate bundling of rule sets to modules including imports of external rule modules/scripts. Each module (rule set) has a unique ID with which it can be added or removed from the KB.

## Example 8.

```matlab
add("./examples/test/test.prova")
add(id1,"r(1):-f(1).f(1).")
add(id2,"r(X):-f(X).")
p(X,Y):- add(id3, "r(_0):-f(_0), g(_0). f(_0). g(_1).", [X,Y]).
remove(id1)
remove("./examples/test/test.prova")
% add an external script
% add rule "r(1):-f(1)." and fact "f(1)." with ID "id1"
% add rule "r(X):-f(X)." with ID "id2"
%Object place holders _N: _0=X; _1=Y.
% remove update/module with ID "id1"
% remove external update
```

Transactional updates transaction(add(…)) make an additional test on all integrity constraints de<sup>fi</sup>ned in the KB or an explicitly stated integrity constraint. If the tests fail the update is rolled back. The semantics of transactional updates in rules is adopted from serial (Horn) rules of transaction logics [4]. In short positive (add) or negative (remove) ID-based update to a program P as a <sup>fi</sup>nite set $U _ { o i d } ^ { \mathrm { p o s / n e g } } : = \{ r u l e ^ { N } : H \gets$ $B , f a c t ^ { M } \colon A \gets \}$ , where $N = 0 , . . . , n , M = 0 , . . . ,$ , m and oid denotes the label of the update, i.e. the unique object id with which it is managed in the unitized KB. Applying U<sub>oid</sub><sup>pos</sup> or U<sub>oid</sub><sup>pos</sup> to P leads to the extended knowledge state $P ^ { + } { = } P \cup U _ { o i d } ^ { \mathrm { p o s } }$ or reduced state $\textstyle P = P \backslash U _ { o i d } ^ { \mathrm { n e g } } .$ . Applying arbitrary sequences of positive and negative updates leads to a sequence of state transitions $< P , U > \longrightarrow < P ^ { \prime } , U ^ { \prime } > \longrightarrow < P ^ { \prime \prime } , U ^ { \prime \prime } > \longrightarrow \ldots  < P ^ { n } ,$ U<sup>n</sup>, AN of program states $P _ { } . . . , P ^ { n }$ which is remembered as sequence of update oids with which the added clause sets are managed as modules in the KB. In case a derivation (execution path) for a particular query/goal, which also includes updates in the instantiated rules during resolution, fails, the updates in this execution path are rolled back till the original state of the last backtracking point via inverting the processed update primitives with the remembered update oids.

## 3.7. Integrity constraints and defeasible reasoning

Rules in SLAs might overlap and contradict each other, in particular if contracts grow larger and more complex and are authored, maintained and updated by different people.

Example 9. (r1) discount(Customer,10) :- spending(Customer, Value, last year), ValueN1000.

(r2) discount(Customer, 5) :- spending(Customer, Value, last year), ValueN500.

In the example a customer might apply for a discount of “10%” as well as a discount of “5%”. From an applications point of view only the higher discount should be drawn.

Nute's defeasible logic (DefL) [22] is a non-monotonic reasoning approach which allows defeasible reasoning, where the conclusion of a rule might be overturned by the effect of another rule with higher priority, i.e. it seeks to resolve con<sup>fl</sup>icts by “defeating” and explicitly expressed superiority relations between rules. Different variants have been proposed, reaching from simple defeasible implementations which deal with con<sup>fl</sup>icts between positive and negative conclusions [3] to Generalized Courteous Logic Programs (GCLP) [12] which use an additional “Mutex” (mutual exclusive) to de<sup>fi</sup>ne and handle arbitrary mutual exclusive literals. Several meta programming approaches have been proposed [2] to execute a defeasible theory in a logic program. In ContractLog we have generalized the basic concept of defeasible reasoning and combined it with the concept of integrity constraints and labelled modules (rules sets with IDs) using a meta program approach. [42,26] An integrity constraint expresses a condition which must always hold. In ContractLog we support four basic types of integrity constraints: [38,32]

1. Not-constraints: express that none of the stated conclusions should be drawn: integrity( not( $p _ { 1 } ( . . . ) , . . . , p _ { n } ( . . . ) ) .$

2. Xor-constraints: express that the stated conclusions are mutual exclusive, i.e. should not be drawn at the same time: integri $\mathbb { y } ( \mathrm { x o r } ( p _ { 1 } ( \dots ) , \dots , p _ { n } ( \dots ) ) )$

3. Or-constraints: express that at least one of the stated conclusions should be drawn: integrity( ${ \mathfrak { o r } } ( p _ { 1 } ( \ldots ) , \ldots ,$ $p _ { n } ( \ldots ) ) )$

4. And-constraints: express that all of the stated conclusion should be drawn: integrity $( \mathrm { a n d } ( p _ { 1 } ( \dots ) , . . . , p _ { n } ( \dots ) ) )$ .

Integrity constraints might be conditional, i.e. stated as integrity rules of the form: integri $\mathtt { y ( \dots ) } \dots \mathtt { b } _ { 1 } ( \dots ) \dots \mathtt { b } _ { m } ( \dots )$

We have implemented a meta programming approach in ContractLog [42,26] which is used to test the integrity constraints speci<sup>fi</sup>ed within an ContractLog LP. The core axioms are:

1. testIntegrity(): enumerates all integrity constrain ts and tests them based on the actual facts and rules in the knowledge base.

2. testIntegrity(Literal): tests the integrity of the LP extended with the literal, i.e. it makes a test of the hypothetically added/removed literal, which might be a fact or the head of a rule.

Example 10. integrity(xor(discount(C,5), discount(C,10)). testIntegrity(discount(“Adrian”,X))? %query test integrity.

The example de<sup>fi</sup>nes an integrity constraint, which states that a discount of 5% and a discount of 10% for the customer are mutually exclusive, i.e. are not allowed to occur at the same time. Integrity constraints might be used for example to hypothetically test knowledge updates before they are applied/committed.

Based on integrity constraints we have generalized the concept of defeasible reasoning, i.e. a con<sup>fl</sup>ict might not be just between positive and negative conclusions as in standard defeasible theories but also between arbitrary opposing conclusions, which are formalized as integrity constraints. Priorities might be de<sup>fi</sup>ned between single rules but also between complete rule sets (modules) enabling rule set alternatives and hierarchical module structures (contract modules). The defeasible meta program implemented in ContractLog tests whether the defeasible rule r with the head p is defeated by testing if the rule defeasibly violates the integrity of the logic program according to the de<sup>fi</sup>ned integrity constraints. If a con<sup>fl</sup>icting defeasible rule, i.e. a rule which is de<sup>fi</sup>ned in an integrity constraint to be con<sup>fl</sup>icting, is not blocked and is of higher priority than the defeasible rule p, p is defeated and will be not concluded. Superiority relations between defeasible rules can be either de<sup>fi</sup>ned based on the rule names (rule oids) such as overrides(r1,r2), the module oids (typically the URLs of rule scripts) such as overrides(m1, m2) or based on head literals such as overrides(p1(X),p2(X)), i.e. a rule (or fact) with head p1(X) overrides a rule with head p2(X). This is very useful to de<sup>fi</sup>ne general superiority rules such as “prefer positive knowledge over negative knowledge”: overrides([P|Args], neg([P|Args])) :- bound(P).

## 3.8. Summary

Contractual logic in SLAs requires several logic formalisms in order to adequately represent respective rules. Such a KR needs to be expressive, but at the same time computationally ef<sup>fi</sup>cient due to the large number of contracts and contract rules that need to be managed. Table 7 provides a short summary of the ContractLog KR framework [42,26,43].

## 4. Implementation

Based on the ContractLog concepts described above, we have implemented the rule-based service level management tool (RBSLM) as a proof of concept. Fig. 1 shows the general archi tecture of the RBSLM tool.

The open-source Prova scripting language (http://prova.ws ) [17], which we extended in the ContractLog rule engine [26,27] with linear goal memoization, ef<sup>fi</sup>cient data structures and different resolution algorithms and semantics (see Section 3.1) serves as inference engine for the logical contract rules. The rules are represented on the basis of the ContractLog framework (2) and are imported using the Prova scripting language [18] into the internal knowledgebase of the rule engine. A high-level declarative mark-up language called the rule-based SLA (RBSLA) language [34,35] is provided to facilitate rule interchange, serialisation, tool based editing and veri<sup>fi</sup>cation of rules. A XSLT based mapping is de<sup>fi</sup>ned which transforms RBSLA into executable ContractLog rules. The graphical user interface – the Contract Manager (4) – is used to write, edit and maintain the SLAs which are persistently stored in the contract base (3). The repository (5) contains typical rule templates and prede<sup>fi</sup>ned SLA domain-speci<sup>fi</sup>c objects, built-in metrics and contract vocabularies (ontologies) which can be reused in the SLA speci<sup>fi</sup>cations. During the enforcement and monitoring of the SLAs, external system management tools and business objects can be integrated (6) (via procedural attachments or event messages transported by an enterprise service bus [45]). Finally, the Service Dash Board (7) visualizes the monitoring results and supports further SLM processes, e.g. reports on violated services, metering and accounting functions, noti<sup>fi</sup>cation services. An enterprise service bus (ESB) is used to deploy several RBSLM services on the Web and communicate between these services and other external services or tools using the RBSLA language as common interchange format — see [26,45] for further details.

Main logic concepts integrated in ContractLog

<table><tr><td>Logic</td><td>Formalism</td><td>Usage</td></tr><tr><td>Extended logic programs</td><td>Derivation rules and extended LPs with negations</td><td>Deductive reasoning on SLA rules extended with default and explicit negation.</td></tr><tr><td>Typed logic (Section 3.2)</td><td>Object-oriented typed logic and procedural attachments + Description logic type systems</td><td>Typed terms restrict the search space and enable object-oriented software engineering principles. Procedural attachments integrate object-oriented programming into declarative rules.→ integration of external systems</td></tr><tr><td>Metadata annotated labelled logic (Section 3.6)</td><td>Metadata labels such as object IDs or Dublin core annotations</td><td>Labelled rule sets (modules) can be used for scoped reasoning on explicitly closed parts of the knowledge in open environments such as the Semantic Web.→ meta annotation and scoped reasoning</td></tr><tr><td>Description logic (Section 3.2)</td><td>Hybrid description logic types and semantic web ontology languages</td><td>Semantic domain descriptions (e.g., contract ontologies) in order to describe rules domain-independent.→ Semantic Web contract/domain vocabularies</td></tr><tr><td>(Re)active logic (Section 3.3)</td><td>Extended ECA rules with ID-based updates, rollbacks, complex events/actions, active rules</td><td>Active event detection/event processing and event-triggered actions.→ reactive rules and complex event / actions</td></tr><tr><td>Temporal event/action logic (Section 3.4)</td><td>Event calculus</td><td>Temporal reasoning about dynamic systems, e.g. interval-based complex event/ action definitions (event algebra) or effects of events on the contrac t state.→ contract state tracking; reasoning about events/actions and their effects</td></tr><tr><td>Deontic logic (Section 3.5)</td><td>Deontic logic with norm violations and exceptions</td><td>Rights and obligations formalized as deontic contract norms with norm violations (contrary-to-duty obligations) and exceptions (conditional. defeasible obligations)→ normative deontic rules.</td></tr><tr><td>Integrity preserving, preferred, defeasible logic (Section 3.8)</td><td>Defeasible logic and integrity constraints</td><td>Default rules and priority relations of rules. Facilitates conflict de tection and resolution as well as revision/updating and modularity of rules with preferences or rules and modules.→ default rules and rule/module priorities</td></tr><tr><td>Test Logic (see [38,33,40])</td><td>Test-driven verification and validation for rule bases</td><td>Validation and verification of SLA specifications against predefined SLA requirements→ safeguards the engineering, dynamic adaptation and interchange process of SLAs</td></tr></table>

![](/api/attachments/86KCW6KT/fulltext/images/620dc49f824050490e5e49d907184f412353994f1b9b740ffd7e37f6aa16eb9e.jpg)  
Fig. 1. Architecture of rule-based service level management tool.

## 5. Validation

ContractLog provides compact, declarative knowledge representation for contractual agreements based on logic programming. On the one hand, this enables high levels of <sup>fl</sup>exibility and easy maintenance as compared to traditional SLA approaches. On the other hand, generic rule engines allow for an ef<sup>fi</sup>cient execution of SLAs. In the following, we evaluate our KR approach by means of experiments and on an example derived from common industry use cases. For a formal analysis of the average and worst case complexity of LPs see [36].

## 5.1. Experimental performance evaluation

To experimentally analyze the performance of the ContractLogs' formalisms w.r.t. query answering in different logic classes (e.g. propositional, Datalog, normal) we adapt a benchmark test suite for defeasible theories [2] to the ContractLog KR and extend it to evalua te different inference properties, rule types and logic program classes. The experiments are designed to test different performance scalability aspects of the inference engine and the logical formalisms. We run the performance tests on an Intel Pentium 1.2 GHz PC with 512 MB RAM using Windows XP. We use different benchmark tests to measure the time required for proofs, i.e. we test performance (time in CPU seconds to answer a query) and scalability (size of test in number of literals). Various metrics such as number of facts, number of rules, overall size of literal indicating the size of complexity of a particular benchmark test might be used to estimate the time for query answering and memory consumption.

The <sup>fi</sup>rst group of benchmarks evaluates different inference aspec ts of the ContractLog KR such as rule chaining, recursion, and uni<sup>fi</sup>cation. In the chains test a chain of n rules and one fact at its end is queried. In the dag test a directedacyclic tree of depth n is spanned by the rules in which every literal occurs recursively k times. In the tree test a fact is at the root of a k-branching tree of depth n in which every literal occurs once. Each test class is performed for propositional LPs without variables and Datalog LPs with one variable. The tests further distinguish strict LPs, i.e. normal LPs with only strict (normal) derivation rules and defeasible LPs with defeasible derivation rules and compare inference for both classes with goal memoization and without goal memoization. We use the total number of literals as a measure of problem size, which is much larger for the defeasible theories due to the meta program inference (see Section 3.7). The second and third group of experiments test the ECA processor for (re)active rule processing and complex event processing based on Event Calculus formulations. Table 8 shows a summary of selected performance results in CPU seconds [36].

Table 8 Performance evaluation

<table><tr><td rowspan="2">Test</td><td colspan="2">Size</td><td colspan="2">No memoization</td><td colspan="2">Memoization</td></tr><tr><td>Strict</td><td>Defeasible</td><td>Strict (Propos./datalog)</td><td>Defeasible (Propositional/datalog)</td><td>Strict (Propositional/datalog)</td><td>Defeasible (Propos./datalog)</td></tr><tr><td rowspan="4">chains (n)</td><td>2001</td><td>11,001</td><td>0.01/0.07</td><td>4/7.6</td><td>0.05/0.17</td><td>5.7/7.8</td></tr><tr><td>5001</td><td>27,501</td><td>0.03/0.17</td><td>12.8/25</td><td>0.15/0.47</td><td>18/24.3</td></tr><tr><td>10,001</td><td>55,001</td><td>0.07/0.3</td><td>40/70</td><td>0.4/1.05</td><td>59/75</td></tr><tr><td>20,001</td><td>110,001</td><td>0.15/0.62</td><td>127/250</td><td>1.25/2.62</td><td>170/200</td></tr><tr><td>dag(n,k)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>n=3 k=3</td><td>39</td><td>156</td><td>0.01/0.06</td><td>0.54/0.89</td><td>0.005/0.01</td><td>0.05/0.05</td></tr><tr><td>n=4 k=4</td><td>84</td><td>324</td><td>2.2/7.7</td><td>81/120</td><td>0.01/0.03</td><td>0.06/0.07</td></tr><tr><td>n=10 k=10</td><td>1110</td><td>3810</td><td>-/-</td><td>-/-</td><td>0.05/0.16</td><td>0.2/0.32</td></tr><tr><td>Tree (n,k)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>n=3 k=3</td><td>79</td><td>248</td><td>0.01/0.02</td><td>0.04/0.04</td><td>0.001/0.001</td><td>0.04/0.05</td></tr><tr><td>n=4 k=3</td><td>281</td><td>761</td><td>0.015/0.03</td><td>0.09/0.1</td><td>0.005/0.006</td><td>0.08/0.11</td></tr><tr><td>n=8 k=3</td><td>19,681</td><td>62,321</td><td>0.17/0.5</td><td>-/-</td><td>0.02/0.04</td><td>0.09/0.14</td></tr><tr><td></td><td></td><td></td><td colspan="2">Update time</td><td colspan="2">Execution time</td></tr><tr><td rowspan="4">ecaplain(n)</td><td>1000</td><td></td><td>0.4</td><td></td><td>0.005</td><td></td></tr><tr><td>2500</td><td></td><td>1.1</td><td></td><td>0.01</td><td></td></tr><tr><td>5000</td><td></td><td>2.5</td><td></td><td>0.015</td><td></td></tr><tr><td>10,000</td><td></td><td>4.3</td><td></td><td>0.02</td><td></td></tr><tr><td rowspan="4">echoldsAt(n)</td><td>1002</td><td></td><td>3.3</td><td></td><td></td><td></td></tr><tr><td>2502</td><td></td><td>6.8</td><td></td><td></td><td></td></tr><tr><td>5002</td><td></td><td>14.6</td><td></td><td></td><td></td></tr><tr><td>10,002</td><td></td><td>28.7</td><td></td><td></td><td></td></tr></table>

Each experiment was performed several times (10 experiments per benchmark test) and Table 8 shows the average results with a range of ±10% for the measured values in the series of tests. The table shows the computation time to <sup>fi</sup>nd an answer for a query. Due to the needed variable uni<sup>fi</sup>cations and variable substitutions in the derivation trees, the datalog tests are in general more expensive than the propositional tests and goal memoization adds small extra costs to rule derivations. In the chains test, where subgoals are never reused, the experiments with memoization are slower than without memoization due to the caching overhead. However, the advantages of goal memoization can be seen in the tree and dag tests which (recursively) reuse subgoals. Here goal memoization leads to much higher performance and scalability (large problem sizes can be solved).

As expected, the defeasible experiments are slower, due to the much larger problem sizes and the meta program interpretations which need several KB subgoal queries. Goal memoization reduces duplication of work, e.g. to test strict in tegrity of defeasible rules. The ECA rule experiments distinguish between update time for querying the KB for ECA rules and processing time for executing the ECA rules. The experiments reveal an increase in time linear in the problem size. The event calculus tests also show linear time increase in the problem size, which here is the number of occurred events stated as happens facts which initiate or terminate a <sup>fl</sup>uent.

In summary, the experiments reveal high performance of the ContractLog formalisms even for larger problem sizes with thousands of rules and more than 10,000 literals, which suggests the approach also for industrial-size applications. We have formalized typical real-world SLAs from different industries in ContractLog within several dozens up to hundreds of rules and much smaller literal sizes (see for example the RIF / RuleML use cases<sup>1</sup>) which can be ef<sup>fi</sup>ciently executed and monitored within milliseconds. Moreover, the hybrid approach in ContractLog allows outsourcing lowerlevel computations and operational functionalities to procedural code and specialized external systems (e.g. DL reasoner [28]).

## 5.2. Use case revisited — adequacy/expressiveness

In this section, we illustrate the adequacy of the rulebased SLA representation approach, in particular with respect to expressiveness of the ContractLog KR, by means of a use case example derived from common industry SLAs. We revive the example SLA described in Section 2.2 and present a formalization of a selected subset in ContractLog, namely the monitoring schedules, the escalation levels and the associated roles, as well as the following SLA rules:

## Example 11. ContractLog formalization of SLA

The service availability will be measured every t<sub>schedule</sub> according to the actual schedule by a ping on the service. If the service is unavailable and it is not maintenance then escalation level 1 is triggered and the process manager is informed. Between 0 and 4 a.m. the process manager is permitted to start servicing which terminates any escalation level. The process manager is obliged to restart the service within time-to-repair, if the service is unavailable. If the process manager fails to restore the service in time-to-repair (violation of obligation), escalation level 2 is triggered and the chief quality manager is informed. The chief quality manager is permitted to extend the time-to-repair interval up to a de<sup>fi</sup>ned maximum value in order to enable the process manager to restart the service within this new timeto-repair. If the process manager fails to restart the service within a maximum time-to-repair escalation level 3 is triggered and the control committee is informed. In escalation level 3 the service consumer is permitted to cancel the contract.

The formalization in ContractLog is as follows:

% service de<sup>fi</sup>nition % service definition

service(http://ibis.in.tum.de/staff/paschke/rbsla/index.htm). % role model and escalation levels initially(escl\_lvl(0)). % initially escalation level 0 role(process\_manager) :- holdsAt(escl\_lvl(1),T). % if escalation level 1 then process\_manager role(chief\_quality\_manager) :- holdsAt(escl\_lvl(2),T). % if escalation level 2 then chief quality manager role(control\_committee) :- holdsAt(escl\_lvl(3),T). % if escalation level 3 then control committee % time schedules standard, prime, maintenance and monitoring intervals % before 8 and after 18 every minute schedule(standard, Service):- systime(datetime(Y,M,D,H,Min,S)), less(datetime(Y,M,D,H,Min,S), datetime(Y,M,D,8,0,0)) not(maintenance(Service)). % not maintenance schedule(standard, Service):- interval(timespan(0,0,1,0), datetime(Y,M,D,H,Min,S)), service(Service), not(maintenance(Service)). % not maintenance % between 8 and 18 every 10 seconds schedule(prime, Service):- sysTime(datetime(Y,M,D,H,Min,S)), lessequ(datetime(Y,M,D,H,Min,S),datetime(Y,M,D,18,0,0)), moreequ(datetime(Y,M,D,H,Min, S),datetime(Y,M,D,8,0,0)), interval(timespan(0,0,0,10), datetime(Y,M,D,H,Min,S)) , service(Service) % between 0 and 4 if maintenance every 10 minutes schedule(maintenance, Service) :- sysTime(datetime(Y,M,D,H,Min,S)), lessequ(datetime(Y,M,D,H,Min,S),datetime(Y,M,D,4,0,0)), interval(timespan(0,0,10,0), date time(Y,M,D,H,Min,S)) , service(Service), maintenance(Service). % servicing initiates(startServicing(S),maintenance(S),T). % initiate maintenance if permitted terminates(stopServicing(S), maintenance(S),T). % terminate maintenance happens(startServicing(Service),T):- happens(requestServicing(Role,Service),T), holdsAt(permit(Role,Service, startServicing(Service)),T). % ECA rule: “If the ping on the service fails and not maintenance then trigger escalation level 1 and notify process manager, else if ping succeeds and service is down then update with restart information and inform responsible role about restart". eca(schedule(T,S), not(available(S)), not(maintenance(S)), escalate(S),\_, restart(S)). % ECA rule available(S) :- WebService.ping(S). % ping service maintenance(S) :- sysTime(T), holdsAt(maintenance(S),T). escalate(S) :- sysTime(T), not(holdsAt(unavailable(S),T)), % escalate only once add(“outages”,”happens(outage(\_0),\_1).”,[S,T]),% add event role(R), notify (R, unavailable(S)). % notify restart(S) :- sysTime(T), holdsAt(unavailable(S),T), add(“outages”,”happens(restart(\_0),\_1).”,[S,T]),% add event role(R), notify(R,restart(S)). % update + notify % initiate unavailable state if outage event happens initiates(outage(S),unavailable(S),T). terminates(restart(S),unavailable(S),T). % initiate escalation level 1 if outage event happens terminates(outage(S),escl\_lvl(0),T). initiates(outage(S),escl\_lvl(1),T) % terminate escalation level 1/2/3 if restart event happens initiates(restart(S),escl\_lvl(0),T). terminates(restart(S),escl\_lvl(1),T). terminates(restart(S),escl\_lvl(2),T). terminates(restart(S) escl\_lvl(3), T). % terminate escalation level 1/2/3 if servicing is started

initiates(startServicing(S),escl\_lvl(0),T). terminates(startServicing(S), escl\_lvl(1),T). terminates(startServicing(S), escl\_lvl(2),T). terminates(startServicing(S),escl\_lvl(3),T). % permit process manager to start servicing between 0 and 4 a.m. holdsAt(permit(process\_manager,Service, startServicing(Service)), datetime(Y,M,D,H,Min,S)):- lessequ(datetime(Y,M,D,H,Min,S),datetime(Y,M,D,4,0,0)) % else forbid process manager to start servicing. holdsAt(forbid(process\_manager,Service, startServicing(Service)), datetime(Y,M,D,H,Min,S)):- more(datetime(Y,M,D,H,Min,S),datetime(Y,M,D,4,0,0)).. % derive obligation to start the service if service unavailable derived(oblige(process\_manager, Service , restart(Service))). % oblige process manager holdsAt(oblige(process\_manager, Service , restart(Service)), T) :- holdsAt(unavailable(Service),T) % de<sup>fi</sup>ne time-to-repair deadline and trigger escalation level 2 if deadline is elapsed time\_to\_repair(t ). % relative time to repair value trajectory(escl\_lvl(1),T1,deadline,T2,(T2–T1)) . % deadline function derivedEvent(elapsed). happens(elapsed,T) :- time\_to\_repair(TTR), valueAt(deadline,T, TTR). terminates(elapsed, escl\_lvl(1),T).% terminate escalation level 1 initiates(elapsed, escl\_lvl(2),T). % initiate escalation level 2 % trigger escalation level 3 if (updated) time-to-repair isNmax time-to-repair happens(exceeded,T) :- happens(elapsed,T1), T = T1 +ttr<sub>max</sub>. terminates(exceeded,escl\_lvl(2),T). initiates(exceeded, escl\_lvl(3),T). % service consumer is permitted to cancel the contract in escl\_lvl3 derived(permit(service\_consumer, contract , cancel)). holdsAt(permit(service\_consumer, contract , cancel), T) :- holdsAt(escl\_lvl(3),T).

Via simple queries, the actual escalation level and the rights and obligations each role has in a particular state can be derived from the rule base. And, the maximum validity interval (MVI) for each contract state, e.g. the maximum outage time, can be computed. These MVIs can be used to compute the service levels such as average availability. The ECA processor of the ContractLog framework actively monitors the ECA rules. Every t according to the actual schedule it pings the service via a procedural attachment, triggers the next escalation level if the service is unavailable and informs the corresponding role.

To illustrate this process, we assume that the service becomes unavailable at time t1. Accordingly, escalation level 1 is triggered and the process manager has time-to-repair t2. After t2 escalation level 2 is triggered and the chief quality manager adapts the time-to-repair to t3 and then to t4 until the maximum threshold max. time-to-repair is reached at timepoint t4. After t4 the SLA is violated and escalation level 3 is initiated which permits the service consumer to terminate the contract. Via querying the rule engine these status information can be dynamically derived at each point in time and used to feed periodical reports e.g. for IT service level management (IT-SLM) and business activity monitoring (BAM), enforce rights and obligations or visualize monitoring results on quality aspects in the Service Dashboard (see Fig. 2).

Finally, we demonstrate the interplay between the various approaches to complex event processing and reaction rules in ContactLog by means of a typical high-level service failover policy speci<sup>fi</sup>cations found in industry:

## Example 12. Automated failover policy

A Manager node is responsible for holding housekeeping information about various servers playing different roles.

When a server fails to send a heartbeat for a speci<sup>fi</sup>ed amount of time, the Manager assumes that the server failed and cooperates with the Agent component running on an unloaded node to resurrect it.A typical rule for receiving and updating the latest heartbeat in event noti<sup>fi</sup>cation style would look like this:

rcvMsg(XID,Protocol,FromIP,inform,heartbeat(Role,

RemoteTime)) :-

time(LocalTime), add(key(FromIP,Role),

”heartbeats(\_0, \_1, \_2, \_3).”, [ FromIP, Role, RemoteTime, LocalTime] ).

The rule responds to a message pattern matching the one speci<sup>fi</sup>ed in the rcvMsg arguments. XID is the correlation-id of the incoming message; inform is called a performative representing the semantic type of the message, in this case, a one-way information passed between parties; heartbeat(…) is the payload of the message. The body of the rule enquires about the current local time and updates the record containing the latest heartbeat from the controller. This rule follows a push pattern where the event is pushed towards the rule systems and the latter reacts. A pull-based global ECA rule that is activated every second by the rule engine and for each server that fails to have sent heartbeats within the last second will detect server failures and respond to it by initiating failover to the <sup>fi</sup>rst available unloaded server. The accompanying derivation rules detect and respond are used for speci<sup>fi</sup>c purpose of detecting the failure and organising the response.

<table><tr><td>escalation level 0</td><td>escalation level 1</td><td>escalation level 2</td><td>escalation level 3</td></tr></table>

![](/api/attachments/86KCW6KT/fulltext/images/b631cc58b82a213a5c4ab39cc1aa23fffdb77af71adfc6d8069d18c62a348547.jpg)  
Fig. 2. Contract tracking

eca( every(‘1S’) , detect(controller\_failure(IP,Role,‘1S’)) ,respond(controller\_failure(IP,Role,‘1S’)) ) .

every(‘1S’):- sysTime(T), interval(timespan(0,0,0,1),T).

detect(controller\_failure(IP,Role,Timeout)) :-

sysTime(LocalTimeNow), heartbeats(IP,Role,RemoteTime, LocalTime), LocalTimeNow-LocalTimeNTimeout.

respond(controller\_failure(IP,Role,Timeout)) :- sysTime (LocalTime), <sup>fi</sup>rst(holdsAt(status(Server,unloaded), LocalTime)),

add(key(Server),”happens(loading(\_0),\_1).”,[ Server, LocalTime]),

sendMsg(XID,loopback,self,initiate,failover(Role,IP, Server)).

The ECA logic involves possible backtracking so that all failed components will be resurrected. The state of each server is managed via an event calculus formulation:

initiates(loading(Server),status(Server,loaded),T). terminates(unloading(Server),status(Server,loaded),T).

initiates(unloading(Server),status(Server,unloaded),T). terminates(loading(Server),status(Server, loaded),T).

The actual state of each server is derived from the happened loading and unloading events and used in the ECA rule to detect the <sup>fi</sup>rst server which is in state unloaded. This EC based formalization can be easily extended, e.g. with new states such as a maintenance state which terminates an unloaded state, but is not allowed in case a server is already loaded:

initiates(maintaining(Server),status(Server,maintenance),T):- not(holdsAt(status(Server,loaded),T)).

terminates(maintaining(Server),status(Server,unloaded),T).

As can be seen from these use case examples, the declarative rule-based approach allows a very compact representation of globally de<sup>fi</sup>ned SLA rules, which would not be possible in standard imperative programming languages. To encapsulate this QoS monitoring and decision making logic in Java, a large object-oriented program with several Java classes and multiple methods to model all subtle nuances would be needed. The entire control <sup>fl</sup>ow must be speci<sup>fi</sup>ed, i.e. the exact order and number of steps and decisions needs to be translated in the procedural code. Obviously, this does not always scale and maintenance and management of the knowledge structures becomes increasingly dif<sup>fi</sup>cult, especially when the SLA logic is likely to change frequently. The ability to dynamically and quickly alter the SLA logic at runtime without any extensions to the generic inference engine is a key advantage of the declarative rule-based approach, which would require reimplementation of the procedural application code or database schemas and perhaps larger service execution outages for redeployment.

Hence, by representing the SLA monitoring and enforcement logic on a more abstract rule-based level and separating it form the low-level procedural aspects of service runtime environment, much more powerful SLA speci<sup>fi</sup>cations can be writ ten and maintenance and management of large numbers of complex individualized SLAs becomes easier. The logical formalisation ensures correctness and traceability of derived results, which is crucial in the SLA domain in order to provide reliable and provable reactions and results, e.g. computed penalties used in accounting. Furthermore, it enables easier validation and veri<sup>fi</sup>cation of the SLA speci<sup>fi</sup>cations and therefore ensures consistency (due to sound and complete logical semantics of the formalisms) and integrity (integrity constraints/test cases) as well automated con<sup>fl</sup>ict resolution (via defeasible refutation).

## 6. Related work

The tendency in common commercial SLA/SLM tools such as IBM Tivoli SLA, HP OpenView, CA Unicenter, BMC Remedy Service Management is to allow speci<sup>fi</sup>cation of QoS parameters (e.g., availability, response time) with high/low bounds. Typically, these parameters are directly encoded in the application code or database tier, which makes it complicated to dynamically extend the SLA logic and describe more complex speci<sup>fi</sup>cations than simple bounds. Hence, this approach is restricted to simple, static rules with only a limited set of parameters. More complex conditionals where one parameter depends upon some other parameters / conditions or states are not expressible. Due to the implicit procedural encoding of the SLA logic into the application code the SLAs are hard to manage, maintain and in particular adapt to new requirements, which would require heavy time and cost intensive refactoring of the application code and database schemas.

There are several XML based mark-up languages for SLAs such as the IBM Web Service Level Agreements (WSLA) [8], the HP Web Service Management Language (WSML) [49], the Web Service Offering Language (WSOL) [50], and WS-Agreement [1] as currently being discussed by the Grid Resource

Allocation Agreement Protocol-Working Group of the Open Grid Forum. These languages include de<sup>fi</sup>nitions of the involved parties (signatory and supporting parties), references to the operational service descriptions (e.g., WSDL) of the service(s) covered by the SLA, the SLA parameters to be monitored and the metrics and algorithms used to compute SLA parameters from raw metrics collected by measurement directives from external sources. They allow the speci<sup>fi</sup>cation of QoS guarantees, constraints imposed on SLA parameters and compensating activities in case these constraints are violated, in terms of material implicational clauses wi th simple Boolean evaluation functions and explicit Boolean connectives. Accordingly, these rules only have a very limited expressiveness restricted to material truth/false implications without variables, quanti<sup>fi</sup>cations, rule chaining and (nonmonotonic) reasoning inferences. Hence these synactical languages can not express more than simple conditional clauses and the interpreter must be adapted each time new functionalities are introduced into the serialization language. In contrast, ContractLog is an expressive logic-based SLA rule programming language with a precise semantics based on logic programming which can be dynamically extended with different domain-speci<sup>fi</sup>c vocabularies from Semantic Web ontologies such as WSMO [51], WS-Policy Ontology [25], OWL-S [23] or other ontologies such as OWL time [24].

Recently, in the area of policy speci<sup>fi</sup>cations there are several proposals which address the de<sup>fi</sup>nition of policies such as WS-Policy [15] or policy languages such as KAos [16], Rei [47] or Ponder [7]. However, WS-Policy is only a general framework, where the details of special policy aspects still need to be de<sup>fi</sup>ned in specialized sublanguages, and the latter mainly focus on typical operational policies such as access control or security issues and only require/consider a very limited set of logical formalisms. In particular they are missing expressive rules (reactive rules, defeasible rules, normative rules).

Defeasible Deontic Logic has been investigated for the modelling of regulations in commercial law and other social institutions. [48] There are also proposals on using Petri-nets [21] or Finite State Machines as in the works of Daskalopulu et al. [9] to describe legal contracts as process <sup>fl</sup>ows. However, those approaches are best suited for contracts which follow a prede<sup>fi</sup>ned protocol sequence. The work of Grosof et al. [13] The Semantic Web Enabling Technology (SWEET) toolkit comprises the CommonRules syntax and also enables business rules to be represented in RuleML. Whilst their approach deals with contracts in a broader range namely e-commerce contracts and mainly supports rule priorities via Generalized Courteous Logic Programs (GCLP) [12] and supports direct procedural attachments, our approach is focused on the speci<sup>fi</sup>cs of Service Level Management. In contrast to SWEET, ContractLog incorporates additional logical concepts which are needed for adequate SLA representation such as contract states, explicit rights and obligations (deontic norms) supplemented with violations and exceptions of norms, integrity constraints, event processing facilities with active sensing, monitoring and triggering of actions, full support for different type systems (e.g. Java, Semantic Web) and sophisticated procedural attachments enabling dynamic Java object instantiations and functional calls, in order to integrate exis ting business object implementations, and SLA-speci<sup>fi</sup>c contract vocabularies.

## 7. Conclusions

Logic programming has been a popular paradigm in the late 1980s and one of the most successful representatives of declarative programming in general. Although, logic programming is based on solid and well-understood theoretical concepts and has been proven to be very useful for rapid prototyping and describing problems on a high abstraction level, its application to commercial software has been limited throughout the past years. Service level management and more generally contract management appear to be particularly suitable to logic programming. IT service providers need to manage large amounts of SLAs with complex contractual rules describing various decision and business logic, ranging from deeply nested conditional clauses, reactive or even proactive behaviour to normative statements and integrity de<sup>fi</sup>nitions. These rules are typically not of static nature and need to be continuously adapted to changing needs. Furthermore, the derived conclusions and results need to be highly reliable and traceable to count even in the legal sense of a contract.

This demands for a declarative knowledge representation language which is computationally ef<sup>fi</sup>cient even for larger SLA speci<sup>fi</sup>cations, traceable in case of incomplete or contradicting knowledge, and <sup>fl</sup>exible in a way that allows to quickly alter the behaviour of the SLA management system. Extended logic programs and derivation rules have several advantages over imperative languages such as Java, or database solutions. However, general logic programs need to be extended by multiple knowledge representation concepts and integrated with commercial sys tem management tools to allow formalising the complex rules in nowadays SLAs and to provide the basis for professional service level management.

In this article we have described ContractLog, an integrated framework of knowledge representation concepts to de<sup>fi</sup>ne and automatically enforce large amounts of SLAs based on generic derivation rule engines. In contrast to a conven tional procedural implementations or pure formal speci<sup>fi</sup>cation approaches the declarative, rule-based approach in ContractLog provides high levels of extensibility and allows for a greater degree of <sup>fl</sup>exibility in de<sup>fi</sup>ning contractual agreements. In this article we have provided an evaluation of the approach with respect to ef<sup>fi</sup>ciency and expressiveness by means of experimentation and examples from industry use cases. The RBSLM tool<sup>2</sup> serves as a proof-of-concept implementation and illustrates that this particular combination of knowledge representation concepts allows for an ef<sup>fi</sup>cient and scalable implementation of service level management tools.

Other properties of the formalized policy and contract speci<sup>fi</sup>cations such as maintenance of the quality of the rule base and the reliability of the produced results could not be addressed in this article. Some of them are addressed in related literature [26,38,32,40,10]. In particular, we have provided suggestions for self-validating rule bases and test driven development, to provide for correctness, reliability and adequacy of rule-based policy and contract speci<sup>fi</sup>cations.

## References

[1] A. Andrieux, et al., WebServices Agreement Speci<sup>fi</sup>cation (WS-Agree ment), 2005.

[2] G. Antoniou, et al., Ef<sup>fi</sup>cient defeasible reasoning systems, Australian Workshop on Computational Logic, 2000, Australia.

[3] G. Antoniou, et al., Representation results for defeasible logic, ACM Transactions on Computational Logic, vol. 2, 2001, pp. 255–287.

[4] A.J. Bonner, M. Kifer, Transaction Logic Programming (or a Logic of Declarative and Procedural Knowledge), 1995 University of Toronto.

[5] S. Chakravarthy, et al., Composite events for active databases: semantics contexts and detection, VLDB, vol. 94, 1994.

[6] W.F. Clocksin, C.S. Mellish, Programming in Prolog, Springer, Berlin, 2003.

[7] N. Damianou, et al., The ponder policy speci<sup>fi</sup>cation language, Work. on Policies for Distributed Systems and Networks (Policy'01), 2001, Bristol, UK.

[8] A. Dan, et al., Web services on demand: WSLA-driven automated management, IBM Systems Journal, Special Issue on Utility Computing 43 (1) (2004) 136–158.

[9] A. Daskalopulu, Modelling legal contracts as processes, 11th Int. Conf. and Work. on Databases and Expert Systems Applications, 2000.

[10] J. Dietrich, A. Paschke, On the test-driven development and validation of business rules, ISTA05, Massey, New Zealand, 2005.

[11] M.H. Emden, R.A. Kowalski, The semantics of predicate logic as a programming language, Journal of the ACM 23 (4) (1976) 733–742.

[12] B.N. Grosof, A Courteous Compiler from Generalized Courteous Logic Programs to Ordinary Logic Progams, IBM T.J. Watson Research Center, 1999.

[13] B.N. Grosof, Y. Labrou, H.Y. Chan, A declarative approach to business rules in contracts: courteous logic programms in XML, EC-99, ACM Press, Denver UK, 1999.

[14] A. Hevner, et al., Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–101.

[15] M. Hondo, C. Kaler, Web Services Policy Framework (WSPolicy), , 2003 ftp://www6.software.ibm.com/software/developer/library/ws-policy. pdf.

[16] M. Jonson, et al., KAoS semantic policy and domain services: an application of DAML to web services-based grid architectures, AAMAS'03, 2003, Melbourne, Australia.

[17] A. Kozlenkov, A. Paschke, M. Schroeder, Prova, , 2006 http://prova.ws.

[18] A. Kozlenkov, M. Schroeder, PROVA: rule-based Java-scripting for a bioinformatics semantic web, International Workshop on Data Integration in the Life Sciences. 2004.

[19] R.A. Kowalski, M.J. Sergot, A logic-based calculus of events, New Generation Computing 4 (1986) 67–95.

[20] LooselyCoupled. SLA, 2003 http://looselycoupled.com/glossary/SLA.

[21] C. Molina-Jimenez, et al., Contract representation for run-time monitoring and enforcement, IEEE Int. Conf. on E-Commerce (CEC), 2003, Newport Beach, USA.

[22] D. Nute, Defeasible reasoning and decision support systems, Decision Support Systems 4 (1) (1988) 97–110.

[23] OWL-S, 2003 http://www.daml.org/services/owl-s.

[24] F. Pan, J. Hobbs, OWL Time, , 2004 http://www.isi.edu/\~pan/OWL-Time. html.

[25] B. Parsia, V. Kolovski, J. Hendler, Expressing WS-policies in OWL, Policy Management for the Web Workshop, 2005.

[26] A. Paschke, ContractLog — a logic framework for SLA representation, management and enforcement, IBIS, TUM, Technical Report, 2004, Munich.

[27] A. Paschke, RBSLA: a rule based service level agreements language, IBIS, TUM, Technical Report, 2004, Munich.

[28] A. Paschke, ContractLog — a logic framework for SLA representation, management and enforcement, IBIS, TUM, Technical Report, 07/2004, 2004, Munich.

[29] A. Paschke, The ContractLog inference engine: a con<sup>fi</sup>gurable inference service for extended logic programming implementing linear SLE Resolution with goal memoization, loop prevention and a hybrid description logic typed uni<sup>fi</sup>cation for the extended well-founded semantics, IBIS, TUM, Technical Report, 2005, Munich.

[30] A. Paschke, ECA-LP: a homogeneous event-condition-action logic programming language 2005 IBIS Technische Universität München Technical Report. 11/2005. Munich

[31] A. Paschke, Typed hybrid description logic programs with order-sorted semantic web type systems based on OWL and RDFS, Internet Based Information Systems, Technical University Munich, Technical Report,12/ 2005 Munich.

[32] A. Paschke, RBSLA — a declarative rule-based service level agreement language based on RuleML, International Conference on Intelligent

Agents, Web Technology and Internet Commerce (IAWTIC 2005), 2005 Vienna, Austria.

[33] A. Paschke, ECA-RuleML: an approach combining ECA Rules with intervalbased event logics, 2005, IBIS, TUM, Technical Report, 2005, Munich.

[34] A. Paschke, The ContractLog approach towards test-driven veri<sup>fi</sup>cation and validation of rule bases — a homogeneous integration of test cases and integrity constraints into evolving logic programs and rule markup languages (RuleML), 2005, IBIS, TUM, Technical Report, 2005, Munich.

[35] A. Paschke, OWL2Prova: a typed hybrid description logic programming language with polymorphic order-sorted DL-typed uni<sup>fi</sup>cation, Int. Workshop on OWL: Experiences and Directions (RuleML/OWLED'06), Springer LNCS, Athens, Georgia, USA, 2006.

[36] A. Paschke, ECA-RuleML/ECA-LP: a homogeneous event-conditionaction logic programming language, http://2006.ruleml.org., Int. Conf. on Rule Markup Languages (RuleML'06), 2006, Athens, Georgia, USA.

[37] A. Paschke, Veri<sup>fi</sup>cation, validation and integrity of distributed and interchanged rule based policies and contracts in the semantic web, Int. Semantic Web Policy Workshop (SWPW'06), Springer, LNCS, Athens, GA, USA, 2006.

[38] A. Paschke, Evaluation of the ContractLog KR: worst case complexity and experimental results, IBIS, TUM, Technical Report, 2006, Munich.

[39] A. Paschke, Rule-Based Service Level Agreements — Knowledge Representation for Automated e-Contract, SLA and Policy Management, Idea Verlag GmbH, Munich978-3-88793-221-3, 2007.

[40] A. Paschke, M. Bichler, SLA representation, management and enforcement — combining event calculus, deontic logic, horn logic and event condition action rules, IEEE EEE'05, 2005, Hong Kong, China.

[41] A. Paschke, A. Kozlenkov, A rule-based middleware for business process execution, Multi-Conference Information Systems (MKWI08), 2008, Munich.

[42] A. Paschke, E. Schnappinger-Gerull, A categorization scheme for SLA metrics, Multi-Conference Information Systems (MKWI06), Passau, Germany, 2006.

[43] A. Paschke, M. Bichler, J. Dietrich, ContractLog: an approach to rule based monitoring and execution of service level agreements, RuleML 2005, 2005, Galway, Ireland.

[44] A. Paschke, J. Dietrich, K. Kuhla, A logic based SLA management framework, Semantic Web and Policy Workshop (SWPW) at 4th Semantic Web Conference, 2005, (ISWC 2005). (Galway, Ireland.

[45] A. Paschke, et al., On self-validating rule bases, Int. Workshop on Semantic Web Enabled Software Engineering (SWESE 2006), Springer, LNCS, Athens, GA, USA, 2006.

[46] A. Paschke, A. Kozlenkov, H. Boley, A homogenous reaction rules language for complex event processing, International Workshop on Event Drive Architecture for Complex Event Process (EDA-PS 2007), 2007, Vienna, Austria.

[47] Rei, 2002 Rei, http://rei.umbc.edu/.

[48] Y.U. Ryu, R.M. Lee, Defeasible deontic reasoning and its applications to normative systems, Decision Support Systems 14 (1) (1995) 59–73.

[49] A.D., A. Sahai, V. Machiraju, Towards Automated SLA Management for Web Services, HP Labs, Palo Alto, 2001

[50] V. Tosic, et al., Management applications of the web service offerings language (WSOL), 15th Int. Conf. on Advanced Information Systems Engineering (CaiSE03), 2003, Velden, Austria.

[51] Web Services Modelling Ontology, 2005 http://www.wsmo.org/.

![](/api/attachments/86KCW6KT/fulltext/images/38092e40f79fd4a3b4eccc618ed6c7ee487af810485d60d80387238b35577178.jpg)

Adrian Paschke is a director of RuleML Inc., steering-committee chair of the RuleML Initiative, co-chair of the Reaction RuleML technical group, founding member of the Event Processing Technical Society (EPTS), and member of W3C (W3C RIF and W3C HCLS) and voting member of OMG He received his PhD in Information Systems from the Technical University Munich on the topic of rule-based service level agreements. His research career led him to the Ludwig Maximilian University (Munich, Germany), Friedrich Alexander University (Nuernberg, Germany), Technical Uni-

versity Munich (Munich, Germany), National Research Council (New Brunswick, Canada), and the Biotec Center, Technical University Dresden (Dresden, Germany). He has led several national and international research and open-source projects and organized several international workshops and conferences. He was involved in multiple industrial software development, business engineering, and language standardization projects and published about 40 papers in international conference, edited books and journals, on topics including IT Service Management, Business Process Management, Complex Event Processing, Pragmatic Web and Semantic Web. Multi-Agent Systems and Rule-based Systems.

![](/api/attachments/86KCW6KT/fulltext/images/c65fe4abec70502b638e834210ce27b8a08f816ec3a1f1167a932a7583c49a81.jpg)

Martin Bichler is a full professor at the Department of Informatics at TU München. He received his MSc in Information Systems from the Technical University of Vienna, and his Ph. D. as well as his Habilitation from the Vienna University of Economics and Business Administration. Martin was working as a research fellow at UC Berkeley and as a research staff member at the IBM T. J. Watson Research Center, Yorktown Heights, New York. Since 2003 he is a full professor at the TU München. Martin has been involved in research and development in the areas of electronic market design, analytical CRM, data mining, and service operations management.
