---
otero_id: 17408
otero_key: "3QPKTAK6"
title: "Inductive consistency in knowledge-based decision support systems"
authors: "Heidi D. Owens; Andrew S. Philippakis"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0039-g"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Inductive consistency in knowledge-based decision support systems

Heidi D. Owens $^{a,*}$ and Andrew S. Philippakis $^{b}$

$^{a}$ School of Business Administration, Portland State University, Portland, Oregon 97207-0751, USA $^{b}$ Decision and Information Systems, College of Business, Arizona State University, Tempe, Arizona 85287-4206, USA

## Abstract

Efforts to integrate knowledge into Decision Support Systems have lead to approaches that incorporate induction techniques to derive rules from data. Such integration efforts create a new integrity control challenge for Knowledge-Based Decision Support Systems. The challenge is recognizing and coping with change. In this paper, we analyze the inductive consistency relationship that exists between data and inductively derived rules and present a strategy for recognizing violations of the inductive consistency relationship. The recognition of integrity problems provides a first defense toward refining knowledge in a Knowledge-Based Decision Support System.

Keywords: Knowledge-based decision support systems; Integrity control; Induction support

## 1. Introduction

Incorporating knowledge, in the form of rules, into Decision Support Systems (DSS) has been recognized for some time as a means of gaining competitive advantage, formulating better problem solving processes, improving decision quality, and refining business operations $[5,20,21,25,27,48]$ . The phrase Knowledge-Based DSS (KBDSS) is often used to describe the efforts to integrate DSS architectures with Artificial Intelligence or Expert System technologies. Specific approaches to incorporate rule derivation, using induction, into DSS have developed over the past few years $[8,42,45]$ . Such approaches provide both new modelling and analysis capabilities to the decision maker.

However, as decision makers become dependent on KBDSS that integrate data and inductively derived rules, significant risks may occur if the system is unable to cope or adapt to new information. Specifically, the use of decision rules that are not adapted to new information may result in poor decisions. Over time, KBDSS must adapt to changes from the continuous environment. The lack of change processes may result in brittle systems.

Within knowledge-based systems, brittleness has been defined as the inability to cope with unexpected problems [31]. Although the need for DSS to be flexible and adapt to changing conditions represents an important research topic [5], the issue of coping with brittleness and adaptation has been minimally addressed in the DSS and KBDSS contexts. Yet, it is the continual refinement of knowledge that will make the use of KBDSS advantageous to managerial decision makers [43].

In this paper, we explore the issue of brittleness within the context of KBDSS that incorporate induction to derive rules from environmental data. This issue represents an integrity control challenge for KBDSS. Specifically, we are interested in recognizing when a brittle situation exists and is in need of refinement. The problem of monitoring the integrity between environmental data and rules inductively derived from that data requires focusing on the relationship between the data and those rules. We refer to that relationship as inductive consistency. We will examine the inductive consistency relationship and present a strategy for recognizing disruptions to that relationship.

The next section reviews background literature related to data-derived rules. In the third section and it's several subsections, we identify knowledge integrity control needs within KBDSS. The fourth section details the development of our model of inductive consistency. In the fifth section, we operationalize inductive consistency in a relational framework and present SQL queries for recognizing disruptions to inductive consistency. We conclude the paper with a section that summarizes the research and outlines developmental issues to operationalize this control mechanism in a KBDSS environment.

## 2. The generation of rules in a KBDSS context

Much of the difficulty in expert system development has been attributed to the transfer of expertise $[2]$ , more popularly known as the “knowledge acquisition bottleneck” $[24]$ . The bottleneck has been defined as the problem of eliciting and representing knowledge. Problems with methods based on direct representation of knowledge have led to efforts that automate the knowledge acquisition process by deriving rules from environmental data. The fundamental technique for deriving rules from data is induction, which began with work by Hunt, Marin, and

Stone [26] and has continued [32,33,34,40]. Evidence that induction techniques perform well suggests that computer-based induction techniques are viable knowledge acquisition methods [33].

Conceptual frameworks, suggesting the synergy to be gained from integrating knowledge and decision support systems $[25,48]$ , have led to applications that incorporate categorical knowledge into decision support applications. Braun and Chandler $[6]$ used machine learning strategies to obtain categorical type knowledge about stock market movements and incorporated this knowledge into a knowledge base that was used in a decision support context. Shaw's $[45]$ MARBLE system uses induction to determine classifications in loan evaluation decisions and automates the knowledge acquisition process. Sandman's $[42]$ induction support system provides assistance for the decision maker to guide the rule generation process resulting in shorter rule sets with fewer classification errors. In all instances, the environmental knowledge takes the form of data, from case histories, and the categorical knowledge takes the form of decision rules, an antecedent implies a consequence. As decisions are made from the application of categorical decision rules new data are generated.

## 3. The integrity control issue for KBDSS

The generation of rules via induction presents an integrity control issue for KBDSS. Of central concern is a fundamental aspect of induction that logicians have known for sometime: it is always possible to generate hypotheses (i.e., rules) that are well substantiated by the available evidence (i.e., data) but no procedure exists to find the “best” one [7]. This aspect is a particular problem when the rules and data are affected by the changing environment. Furthermore, in a KBDSS, the completeness and accuracy of rules will limit the success of their use.

## 3.1. Rule refinement

It is possible to improve the accuracy of rules through refinements based on additional information. The consistency between the rules used in the decision processes and the new data is an important and relevant issue that guides knowledge refinement [3]. Monitoring consistency is a necessary control process to help recognize the need for refinements to support the changing environment and refinements to correct knowledge acquisition errors. The ability to refine knowledge is the essential adaptation requirement that systems must exhibit to control brittleness.

The knowledge refinement process has been defined as the generation, testing, and possible alteration of rules in an existing knowledge base, in an attempt to improve the system's performance [18,19]. Empirical methods that use case examples with known conclusions to generate rules for a knowledge base [e.g., 40] can also be used to generate possible suggestions for rule refinement. Ginsberg [18] defined a metalinguistic framework for accomplishing refinement tasks. In this framework, a refinement system compares the conclusions of rules in the knowledge based system with known conclusions to discover areas in need of refinement. The SEEK system [38] uses information on rule performance to analyze and revise rules by generalization, i.e., weakening the condition of the rule by removing components, or specialization, i.e., strengthening the condition of the rule by adding components. Others have addressed rule revision by systematically adjusting the weights of rules in the knowledge base [e.g., 41].

Research addressing knowledge refinement has examined the process using known inconsistencies. Therefore, it is necessary to recognize sources of information (i.e., evidence) that suggest the need to refine in order to support refinement methods in KBDSS. In the KBDSS context, the ability to support knowledge refinement will demand the ability to recognize sources of potential brittleness.

## 3.2. Reasoning about brittleness

In general, the view of integrity control in knowledge bases centres on the notion of knowledge consistency within the knowledge system.

Brittleness, itself, does not imply inconsistency. Yet, inconsistencies within the system may lead to brittleness because of an inability to cope with the change that lead to the inconsistency. Methods that seek to restore knowledge consistency focus on maintaining a contradiction-free environment.

Gardenfors and Makinson [17], addressed the issue of revising a source of knowledge when presented with new, but inconsistent information. The problem, in this situation, involves both what knowledge is to be revised and what knowledge is to be removed. They define integrity constraint sets that express the types of consistencies that the knowledge set must sustain. The integrity constraint sets examine how consistency can be maintained using three kinds of updates: (a) expansions, a new knowledge hypothesis is added to the knowledge source K regardless of its consequences; (b) revision, a new knowledge hypothesis that is inconsistent with a knowledge source K is added to K, but in order for K to remain consistent, some existing knowledge in K is removed; and (c) contraction, some knowledge hypothesis in knowledge source K is removed to satisfy some integrity constraint $I_{j}$ without adding any new knowledge.

Closely linked to the issue of knowledge consistency is the issue of nonmonotonic reasoning. Nonmonotonic reasoning employs defeasible reasoning $[39]$ strategies that enable one to retract a previous conclusion when presented with new information that refute that conclusion. It has been explored under an umbrella of research topics, and has been shown to be important in common sense reasoning $[23]$ and Decision Support $[29,35,36]$ because nonmonotonic reasoning strategies allow one to revise conclusions given new information. A Truth Maintenance System (TMS) can support nonmonotonic reasoning by maintaining consistency among beliefs in the system. A TMS finds a current set of beliefs from a current set of reasons $[15]$ . When inconsistencies are found among beliefs, dependency directed backtracking is used to retract beliefs that are not supported by current reasons.

Because brittleness does not result directly from inconsistencies, approaches to maintain a contradiction-free environment will fail to adequately address the brittleness issue. In TMS and similar methods, there is no notion of a “global state” [11]. There is a need for systems to contain adequate representations, to fall back on, when it is necessary to cope with change [31].

In a KBDSS environment that integrates data and rules, an interaction exists between the data and the inductively derived rules. Knowledge about the interaction of forces is viewed as a source of “profound” knowledge that provides an adequate representation for improving quality $[12]$ . Reasoning defeasibly about that “interaction” knowledge provides a strategy for recognizing knowledge inconsistencies and potential sources of brittleness in a KBDSS. In particular, the relationship between data and inductively derived rules represents an integrity norm of the system that can be evaluated as information in the system is changed. These integrity norms provide a global state for directing change. Control strategies, within the system, must seek to maintain the integrity norms, not to reject them. In the next section, we define the inductive consistency relationship that exists between data and inductively derived rules and present our strategy for recognizing disruptions to that relationship. Section 5 will demonstrate our approach.

## 4. The inductive consistency relationship

A commonly used form of induction that is relevant to KBDSS because it aids in the construction of rules from data is conceptual inductive learning. Two frequently studied types of conceptual inductive learning are: learning from examples and learning from observation [32]. Although inductive consistency could apply to both types, the inductive consistency relationship is focused on learning from observations, which entails generalizing a description or classification from a collection of observations. These observations are represented by historical data, i.e., environmental knowledge, stored in the KBDSS. The decision rules for formulating classifications are an output of the induction process and represent a second source of knowledge within the KBDSS.

Inductive consistency defines a two way relationship between data and the set of rules derived from that data. It is based on the notion that no matter how efficient an induction algorithm, as new information becomes available, a “better” set of rules might exist. The objective of focusing on a rule/data inductive consistency relationship is not to find the “best” set of rules but to evaluate when to pursue finding a “better” set. Updates that involve changes to either the data or the rules provide the circumstances to make that evaluation. Inductive consistency is a two way relationship because changes to either the data or the rules will affect the balance of the inductive relationship. The inductive generation of rules from the data establishes a one way relationship; however, once the rules are applied, new case histories result and become part of the data. Expressing this inductive consistency relationship as integrity norms of the system provides a tool for monitoring updates to the KBDSS and recognizing potential sources of brittleness. Reasoning defeasibly about the inductive consistency relationship provides a disruption recognition tool that serves as the first step toward resolution strategies that can refine and improve the categorical knowledge.

## 4.1. The intension dependency

It has been suggested that the interdependencies between knowledge provide a resource to support adaptation because the basic structure of a relationship remains intact even as knowledge changes $[1,12,13,16]$ . Structural relationships have been studied in cognitive development as constraints that guide knowledge development $[28]$ . In database systems, structural relationships are used to capture domain integrity that guide attribute values $[9]$ . In this research, two structural dependencies are used to model inductive consistency. These dependencies are the intension dependency, which captures an existential relationship between two knowledge sources, and the domain dependency, which generalizes the notion of domain integrity to knowledge sources.

The intension dependency was recently defined to represent a general class of knowledge interdependencies for use in controlling integrated information systems [37]. The intension dependency defines a structural relationship between two knowledge sources that is based on existence, one knowledge source is bound by the existence of another. For example, policy rules that establish guidelines for credit approval will determine the set of “possible” individuals who could receive credit; therefore, the existence of a policy rule knowledge source bounds what could exist within a knowledge source that records credit approval data. The specific form of the intension dependency is as follows:

$$
\operatorname{EXT} (\mathrm{KSi}) \rightarrow \operatorname{INT} (\mathrm{KSd})\tag{1}
$$

Read: The extension of KSi bounds the inten-
sion of KSd,
where:

EXT - defines the extension of a knowledge source (i.e., its current contents) and represents what the knowledge is.

INT - defines the intension of a knowledge source (i.e., its domain of interpretation) and represents everything a knowledge source can be. The extension of a knowledge source can be viewed as an “assignment” from the knowledge source’s intension.

KSi - the independent knowledge source.

KSd - the dependent knowledge source.

The domain dependency expresses a structural relationship within a knowledge source. It states that the values for a knowledge source must be drawn from its domain of interpretation (i.e., possible values). The domain dependency can be represented in its general form as follows:

$$
\operatorname{INT} (\mathrm{KSx}) \rightarrow \operatorname{EXT} (\mathrm{KSx})\tag{2}
$$

Read: The intension of KSx bounds its own extension.

Using the intension dependency and domain dependency, one can derive an extension constraint that represents an integrity norm of the system, and it can be used for integrity control recognition problems. The extension constraint defines a structural existence relationship between knowledge sources in terms of extension only. For integrity control purposes the extension constraint represents a defeasible belief, i.e., it is believed to be true until evidence is presented that defeats it. Using the intension dependency (equation 1) and the following domain dependency, for a dependent knowledge source:

$$
\mathrm{INT} (\mathrm{KSd}) \rightarrow \mathrm{EXT} (\mathrm{KSd})
$$

the following extension constraint can be derived using modus ponens:

$$
\mathrm{EXT} (\mathrm{KSi}) \rightarrow \mathrm{EXT} (\mathrm{KSd})
$$

Read: The extension of KSi bounds the extension of KSd.

Two sources of evidence have been shown logically to defeat the extension constraint $[37]$ : (a) insertions to a dependent knowledge source that result in a final state change; (b) deletions from an independent knowledge that result in a restricting transfer change. A final state change is an update that would violate the current intention of the updated knowledge source. A final state change to a dependent knowledge source can be recognized by determining if the extension of the independent knowledge source continues to bound the extension of the updated dependent knowledge source. A restricting transfer change is an update that would cause a “narrowing” of the current extension of a knowledge source on which another knowledge source depends. It is recognized by determining if the new extension of the independent knowledge source continues to bound the extension of the current dependent knowledge source.

In the next subsection, we present the intension dependencies to model the relationship between data and inductively derived rules as integrity norms of the system. From the intension dependencies, we will derive extension constraints that can be operationalized for controlling inductive consistency.

## 4.2. Intension dependencies for inductive consistency

The two way relationship that can be expressed between rules and data can be captured with a set of intension dependencies, one defining the rules as dependent on the data and a second dependency defining the data as dependent on the rules. The following definitions will apply to these dependencies.

DEFINITION: A rule consists of an antecedent and a consequence, the antecedent implies the consequence. For example, $A \rightarrow B$ expresses a rule that A implies B. A is the antecedent, is B is the consequence.

DEFINITION: A set of data, T, will serve as the training set from which a set of rules, $I_{T}$ are inductively generated.

DEFINITION: A classification is the attribute or set of attributes in the data training set that classify the observations in that data set. A classification will correspond to the consequence of a rule.

DEFINITION: A set of classifying attributes, consisting of one or more attributes, exists in the data training set that provides a disruption of the classes defined by the classification attribute. The classifying attributes that uniquely describe a class will correspond to the antecedent of a rule.

Given a set of rules, $I_{T}$ , derived from a set of data, T, the existence of those rules can be expressed in terms of that data. Using intension dependencies, the inductive consistency relationship can be abstractly expressed as follows:

$$
\operatorname{EXT} (\mathrm{T}) \rightarrow \operatorname{INT} \left(\mathrm{I} _ {\mathrm{T}}\right)\tag{3}
$$

Read: The extension of the training set, T, bounds the intension of the inductively generated rule set, $I_{T}$ .

Equation 3 is a specific instance of equation 1 for the instance of induction. It merely states that the classifying attributes for a particular classification in the data set will constrain the rule antecedent and corresponding consequence in the rule set. Given a valid rule set, a parallel relationship is defined in the reverse direction that implies that the rules now constrain the data, as follows:

$$
\operatorname{EXT} \left(\mathrm{I} _ {\mathrm{T}}\right)\rightarrow \operatorname{INT} (\mathrm{T})\tag{4}
$$

Read: The extension of the inductively generated rule set bounds the intension of the training set.

Equation 4 also represents an instance of equation 1. It is considered valid if the rule set, $I_{T}$ , is applied in the decision processes that will generate new data observations. In essence, because the categorical decision rules have been defined as a knowledge source for directing future decisions, new data observations are guided by those rules. Hence, from an integrity standpoint, equation 4 must be accepted as true. If this relationship is not accepted, then no confidence can be placed in those categorical decision rules because they do not guide future decisions.

Formally, inductive consistency can be defined for two knowledge sources, T, a set of data, and $I_{T}$ , a set of inductively generated rules, if: the classifying attributes in T that classify a particular observation are equally compatible with the same attributes and classifications in $I_{T}$ and vice versa. Therefore, the general relationship forms given in equations 3 and 4 form the inductive consistency relationship. The precise definition of the data to rule existence relationship, that considers the classifying attributes, is denoted as follows:

$$
\begin{array}{r l}&{\mathrm{EXT} \big (\mathrm{A} _ {1}, \mathrm{A} _ {2}, \dots , \mathrm{A} _ {\mathrm{n-1}}; \mathrm{T} | \mathrm{A} _ {\mathrm{n}} = \mathrm{V} _ {c} \big)}\\&{\rightarrow \mathrm{INT} \big (A n t e; \mathrm{I} _ {\mathrm{T}} | \mathrm{A} _ {\mathrm{n}} = \mathrm{V} _ {c} \big)}\end{array}\tag{3a}
$$

Read: The Extension of attributes $A_{1}$ to $A_{n-1}$ in a training set given that a classifying attribute, $A_{n}$ , has value, $V_{c}$ , constrains the intention of the antecedent, Ante, in an inductively generated rule set given that the classifying attribute, $A_{n}$ , has the same value, $V_{c}$ . The condition that $A_{n} = V_{c}$ represents the selection criterion of the dependency.

The precise definition of the rule to data existence relationship, that considers the classifying attribute, is denoted as follows:

$$
\begin{array}{r l}&\mathrm{EXT} \big (A n t e; \mathrm{I} _ {\mathrm{T}} | \mathrm{A} _ {\mathrm{n}} = \mathrm{V} _ {c} \big)\\&\rightarrow \mathrm{INT} \big (\mathrm{A} _ {1}, \mathrm{A} _ {2}, \dots , \mathrm{A} _ {\mathrm{n-1}}; \mathrm{T} | \mathrm{A} _ {\mathrm{n}} = \mathrm{V} _ {c} \big)\end{array}\tag{4a}
$$

Read: The Extension of the antecedent, Ante, in an inductively generated rule set, given that a classifying attribute, $A_{n}$ , has value,

$V_{c}$ , constrains the intention of attributes $A_{1}$ to $A_{n-1}$ in a training set given that the classifying attribute, $A_{n}$ , has the same value, $V_{c}$ . The condition that $A_{n} = V_{c}$ represents the selection criterion of the dependency.

Equations 3a and 4a specify the general form to represent specific instances of the intension dependency for the inductive consistency relationship. Together the intension dependencies and instances of the domain dependency, one for the data training set and one for the inductively generated rules, can be used to derive extension constraints for inductive consistency. Recall from Section 4.1 that extension constraints, derived from inclusion dependencies, are defeasible beliefs that capture an existence relationship between two knowledge sources. KBDSS architectures that can treat extension constraints as beliefs and seek to maintain those beliefs can recognize and resolve inductive consistency disruptions. Hence, extension constraints provide the mechanism for operationalizing inductive consistency controls. The derivation of extension constraints from intension and domain dependencies is shown below:

$$
\operatorname{EXT} (\mathrm{T}) \rightarrow \operatorname{INT} \left(\mathrm{I} _ {\mathrm{T}}\right)\tag{3}
$$

$$
\operatorname{EXT} \left(\mathrm{I} _ {\mathrm{T}}\right)\rightarrow \operatorname{INT} (\mathrm{T})\tag{4}
$$

$$
\operatorname{INT} \left(\mathrm{I} _ {\mathrm{T}}\right)\rightarrow \operatorname{EXT} \left(\mathrm{I} _ {\mathrm{T}}\right)\tag{5}
$$

$$
\operatorname{INT} (\mathrm{T}) \rightarrow \operatorname{EXT} (\mathrm{T})\tag{6}
$$

$$
\operatorname{EXT} (\mathrm{T}) \rightarrow \operatorname{EXT} \left(\mathrm{I} _ {\mathrm{T}}\right)\tag{7; from 3, 5}
$$

$$
\mathrm{EXT} \left(\mathrm{I} _ {\mathrm{T}}\right)\rightarrow \mathrm{EXT} (\mathrm{T})\tag{8; from 4, 6}
$$

Equations 3 and 4 are repeated here for clarity. Equations 5 and 6 represent the abstraction of the domain dependency (equation 2) for the inductively generated rules and the training set. In both instances, the equation states that the current contents of the rule or data set is bound by the domain of interpretation (i.e., set of all possible values).

<table><tr><td>INSERT</td><td>Training Set:If classifying attributes from update EVALUATES-TO antecedent in  $I_T$ ANDclassification from update EVALUATES-TOconsequence from  $I_T$ ThenA FINAL STATE CHANGE has not occurred</td><td>Rule Set:If antecedent from update EVALUATES-TOclassifying attributes in T ANDconsequence from update EVALUATES-TOclassification from TThenA FINAL STATE CHANGE has not occurred</td></tr><tr><td>DELETE</td><td>Training Set:If classifying attributes from update EVALUATES-TO antecedent in  $I_T$ ANDclassification from update EVALUATES-TOconsequence from  $I_T$ ThenA RESTRICTING TRANSFER CHANGE has occurred</td><td>Rule Set:If antecedent from update EVALUATES-TOclassifying attributes in T ANDconsequence from update EVALUATES-TOclassification from TThenA RESTRICTING TRANSFER CHANGE has occurred</td></tr></table>

Fig. 1. General queries for recognizing disruptions to inductive consistency.

Equations 7 and 8 will serve as the extension constraints for inductive consistency. They are derived by applying modus ponens from the instances of the intension dependency (equations 3 and 4) and the domain dependency (equations 5 and 6). As a first line of defense, a KBDSS must recognize when an extension constraint has been violated. We present our approach for operationalizing a disruption recognition strategy within the relational model in Section 5.

For the purpose of recognizing an integrity control problem of inductive consistency, the specific induction algorithm or process to derive rules from environmental data, i.e., training set, is not a concern. Because the extension constraints define the inductive consistency relationship in terms of extension, a disruption recognition strategy need only focus on the current contents of the related knowledge sources. In the next subsection, we examine the conditions under which disruptions will exist for an inductive consistency relationship.

## 4.3. Inductive consistency disruption recognition

The purpose of recognizing disruptions to inductive consistency is to maintain that relationship. It is possible that an update to the training set or inductively generated rules may not violate the inductive consistency relationship, but how would one know? Formally, controlling the integrity of the inductive consistency relationship requires two actions: (a) evaluate the updates to determine whether the relationship is disrupted (i.e., violated), and (b) take action to permit nondisrupting updates and to prohibit or resolve disrupting updates. Our present concern is the first action: recognizing disruptions. The availability of a general disruption recognition strategy for inductive consistency will enable future research to explore a number of “resolution” strategies. At the very minimum, disrupting updates can be prohibited by the system and resolved by a human system administrator.

The disruption recognition strategy for inductive consistency depends on recognizing evidence that characterizes a disruption. The two sources of evidence that were mentioned in section 4.1 can defeat the inductive consistency relationship: (a) deletions causing a restricting transfer change, and (b) insertions causing a final state change. Fig.1 details the test conditions under which disrupting changes can occur. Because inductive consistency is a two-way relationship, the test conditions are uniform. In each case, the update to one knowledge source is compared with the contents (i.e., extension) of the related knowledge source. The EVALUATES-TO keyword functions as comparison operator that can determine if two values are equivalent (e.g., $1 + 1$ EVALUATES-TO 2; 99 EVALUATES-TO “Less than 100”). In addition, the test conditions do not depend on whether a knowledge source is the dependent or independent knowledge source. Instead, one must interpret the truth value of the test condition in the context of the type of update. For instance, an insertion to a training set is disrupting when the test condition is false, but a deletion to a training set is disrupting when the test condition is true. It is through the interpretation that disruptions are recognized.

The disruption recognition strategy presented in this subsection can be operationalized in KBDSS architectures that trigger the evaluation rules shown in Fig.1 as updates are made to the system. The relational model $[9]$ has a number of strengths for supporting a KBDSS architecture that can support our disruption recognition strategy. In the next section, we discuss these strengths and present examples for operationalizing our inductive consistency disruption recognition strategy in the relational model.

## 5. A relational implementation for inductive consistency

Any KBDSS architecture must be able to assess the disrupting effects of updates that add or delete rules/data in an inductive consistency relationship. To do so, the KBDSS must allow the general queries from Fig. 1 to be activated as updates are made to the system. The relational model provides a number of capabilities to support this activation including: (a) a system catalog to store the inductive consistency relationships;

(b) the ability to query the system catalog at the time of update to find “relevant” integrity control relationships; and (c) the ability to activate control queries that can query various relations without user interference. We have chosen the relational model as a KBDSS architecture because of these strengths and for several other reasons. First, the relational model has influenced many aspects of information technology $[10]$ . It has been used as the basis for model representation $[14,30]$ , as the underlying structure of knowledge-based expert systems $[22]$ , as a supporting architecture for KBDSS environments $[42]$ , and for integrated systems structures $[4]$ . Second, many DSS generators provide a relational model for storing data in a DSS. Third, relational model extensions will support knowledge processing integrations $[e.g., 46]$ . Finally, recent trends toward integrating deductive data modelling with DSS $[44]$ have made use of the relational model and the structured query language (SQL).

In this section, we examine a relational model implementation of a KBDSS that supports inductive consistency. Our example assumes that the inductively generated rules are output from the induction algorithm into the KBDSS, whose knowledge system is stored in a relational database. Therefore, the representation of rules, in the relational database, is a fundamental issue for supporting inductive consistency. Before presenting how we have operationalized the disruption recognition strategy in this KBDSS architecture, we discuss the issue of representing rules in the relational model in the next subsection.

## 5.1. Relational database knowledge sources for rules

Within the context of the relational model, it is possible to combine attributes and treat them as units of information, rather than as individual attributes. The result of combined attributes is a composite attribute. As an example, consider a postal address consisting of a street address, city name, state, and zip code. The composite attribute, ADDRESS, is more useful in its entire form, than individually. Information concerning what domains constitute a composite attributes can be stored in the system catalog. The benefit of composite attributes is that they can be treated as units of information. In this research, composite attributes are used to represent knowledge in the form of categorical decision rules. Composite attributes allow one to construct the compound domains for representing rule antecedents and still sustain the simplicity and generality of the relational model. If a rule antecedent was represented as a simple attribute using a text field, then it would be difficult to decompose that antecedent into parts because information on the structure of the rule is not available in the catalog. Using composite attributes, attribute domains from the classifying attributes in the data set can be combined to form a composite attribute. That composite attribute represents the antecedent of the rule when stored in the relational database. Similarly, the consequence of the rule also can be a composite attribute. For example, consider the following rule:

R1: IF RAINING = YES and MILK = 0
THEN ACTION = DRIVE TO STORE

Representing this rule as a simple attribute would make it difficult to decompose. However, it could be represented as the composite attribute, ANTECEDENT and the simple attribute CONSEQUENCE. ANTECEDENT consists of the domains for both RAINING and MILK. For simplicity, assume that the domain for RAINING is YES or NO and the domain for MILK is 0, 1, or 2, where the number corresponds to “quarts left in the refrigerator.” CONSEQUENCE consists of the domain for ACTION, and might consist of values such as DRIVE TO STORE, WALK TO STORE, RIDE BIKE TO STORE, etc. Using these concepts, R1, above, can be represented as:

## RULE# ANTECEDENT CONSEQUENCE R1 YES 0 DRIVETOSTORE

If an element for the simple domain does not have a value for that rule, then a null value is used. This will be represented as a dash. For example, consider Rule R2:

R2: IF RAINING = NO THEN ACTION = WALK TO STORE

R2 would be represented using the composite

PERFORM-DATA

<table><tr><td>PROFIT</td><td>AGE</td><td>COMPETITION</td><td>TYPE</td></tr><tr><td>Down</td><td>Old</td><td>No</td><td>Software</td></tr><tr><td>Down</td><td>Midlife</td><td>Yes</td><td>Software</td></tr><tr><td>Up</td><td>Midlife</td><td>No</td><td>Hardware</td></tr><tr><td>Down</td><td>Old</td><td>No</td><td>Hardware</td></tr><tr><td>Up</td><td>New</td><td>No</td><td>Hardware</td></tr><tr><td>Up</td><td>New</td><td>No</td><td>Software</td></tr><tr><td>Up</td><td>Midlife</td><td>No</td><td>Software</td></tr><tr><td>Up</td><td>New</td><td>Yes</td><td>Software</td></tr><tr><td>Down</td><td>Midlife</td><td>Yes</td><td>Hardware</td></tr><tr><td>Down</td><td>Old</td><td>Yes</td><td>Software</td></tr></table>

Fig. 2. The data for PERFORM-DATA.

attribute ANTECEDENT and simple attribute CONSEQUENCE as follows:

<table><tr><td>RULE#</td><td>ANTECEDENT</td><td>CONSEQUENCE</td></tr><tr><td>R1</td><td>YES 0</td><td>DRIVETOSTORE</td></tr><tr><td>R2</td><td>NO -</td><td>WALKTOSTORE</td></tr></table>

As shown in this section, rules can be represented as composite attributes. Although not presented, the CONSEQUENCE attribute also could be represented as a composite attribute. The use of composite attributes allows the representation of rules in forms that can be stored and later retrieved for inferencing operations.

## 5.2. An instance of inductive consistency

For the purpose of examining our disruption recognition strategy in the relational model, consider an inductive consistency relationship between profit performance data, from Fig.2, and rules that were inductively derived from the data using Quinlan's [40] classification method. This example is adapted from [47].

The data will be viewed as knowledge source PERFORM-DATA. The rules, derived from PERFORM-DATA, will be viewed as knowledge source PERFORM-RULES. PERFORM-RULES contains one composite attribute, AN-

PERFORM-RULES

<table><tr><td>RULE #</td><td colspan="2">ANTECEDENT</td><td>CONSEQUENCE</td></tr><tr><td>R1</td><td>OLD</td><td>--</td><td>Down</td></tr><tr><td>R2</td><td>NEW</td><td>--</td><td>Up</td></tr><tr><td>R3</td><td>MIDLIFE</td><td>NO</td><td>Up</td></tr><tr><td>R4</td><td>MIDLIFE</td><td>YES</td><td>Down</td></tr></table>

Fig. 3. The PERFORM-RULES rule set.

TECEDENT that consists of simple domains AGE and COMPETITION, from PERFORM-DATA. Attribute CONSEQUENCE corresponds to the profit classification for the rule. The rules for PERFORM-RULES are shown in Fig.3.

Consider the following extension constraints that capture the inductive consistency relationship between PERFORM-DATA and PERFORM-RULES:

EC1: EXT(AGE, COMPETITION; PERFORM-DATA | PROFIT = value) →

EXT(ANTECEDENT; PERFORM-RULES | CONSEQUENCE = value)

EC2: EXT(ANTECEDENT; PERFORM-RULES | CONSEQUENCE = value) → EXT(AGE, COMPETITION; PERFORM-DATA | PROFIT = value)

The selection criterion used in the above extension constraints is necessary to establish the classification for this inductive consistency relationship. In this specific instance, the classification attribute from PERFORM-DATA is PROFIT. PROFIT represents the CONSEQUENCE of the rules shown in PERFORM-RULES. The classifying attributes from PERFORM-DATA are AGE and COMPETITION. Together these attributes are combined to form the composite attribute ANTECEDENT in PERFORM-RULES.

## 5.3. Inductive consistency disrupters

In this subsection, we operationalize the general disruption recognition queries, from Fig.1, in the relational model KBDSS architecture. Using the above extension constraints for the inductive consistency relationship between PERFORM-RULES and PERFORM-DATA, four types of disruptions can occur. These disruptions occur due to the insertion or deletion of data or rules from the related knowledge sources. Using SQL, queries can be formulated to determine if a disruption occurs from an update. Fig.4 details the SQL queries that operationalize the disruption test conditions given in Fig.1. The SQL queries must be nested to support the comparison of the update to the related knowledge source. As mentioned in Section 4.3, the uniformity of the queries is due to the two way relationship of inductive consistency.

<table><tr><td>INSERT</td><td>FINAL STATE CHANGE:SELECT key attributeFROM  $KS_{data}$ WHERE classifying attributesEVAL(SELECT antecedentFROM update)AND classificationEVAL(SELECT consequenceFROM update)</td><td>FINAL STATE CHANGESLECT key attributeFROM  $KS_{rules}$ WHERE antecedentEVAL(SELECT classifying attributesFROM update)AND consequenceEVAL(SELECT classificationFROM update)</td></tr><tr><td>DELETE</td><td>RESTRICTING TRANSFERCHANGE:SELECT key attributeFROM  $KS_{data}$ WHERE classifying attributesEVAL(SELECT antecedentFROM update)AND classificationEVAL(SELECT consequenceFROM update)</td><td>RESTRICTING TRANSFERCHANGESLECT key attributeFROM  $KS_{rules}$ WHERE antecedentEVAL(SELECT classifying attributesFROM update)AND consequenceEVAL(SELECT classificationFROM update)</td></tr></table>

Fig. 4. SQL queries for recognizing disruptions to inductive consistency.

The queries are standard SQL queries except for the EVAL connective, which is used to implement the EVALUATES-TO function shown in Fig.1. EVAL determines if a query is equivalent to a subquery based on value of the two expressions. For example, the data value 10 EVAL to the rule antecedent <20.

Each query, in Fig.4, has a second condition in the WHERE clause that utilizes a selection criterion to limit the evaluation to a specific classification. The queries make use of this condition to determine: (a) if a data tuple exists that corresponds to an inserted/deleted rule, for rule updates, and (b) if a rules exist that would classify the inserted/deleted tuple, for data updates. In the following subsections, we will demonstrate two disruption examples.

## 5.4. Example disrupter: an insertion to the data set

As an example of an inductive consistency disruption, consider the following primitive update, PU, which inserts a tuple in PERFORM-DATA:

insert into PERFORM-DATA

(PROFIT, AGE, COMPETITION, TYPE)

values (“DOWN”, “MIDLIFE”, “NO”,

"SOFTWARE")

This update could be disrupting by nature of PERFORM-DATA being a dependent knowledge source, or it could be disrupting by nature of PERFORM-DATA being an independent knowledge source. However, the queries are the same in either case, and it is not necessary to be concerned with the direction of the relationship.

Following the general forms from Figure 4, the query to determine if the above update is disrupting is as follows:

select R#

from PERFORM-RULES

where ANTECEDENT eval

(select AGE, COMPETITION from PU)

and CONSEQUENCE eval

(select PROFIT from PU)

Query Result: NULL

Because the result of this query is null, there is no rule to classify this tuple; therefore, the update would cause a disruption. The update would result in a final state change to PERFORM-DATA.

In the case of insertions to the data set, a disruption is found when the above query does not find a rule that describes the data tuple. Although this could be a result of the rule set not being complete, i.e., handle every possible classification, it is also possible that the addition of the data tuple contradicts an existing rule. Finding that rule would be useful for resolving the disruption; resolution strategies are a future research topic.

The selection criterions of EC1 and EC2 are used in the above query to determine if the consequence of a rule evaluates to the inserted tuples classification. We can reverse the selection criterion evaluation to determine if the new data tuple contradicts any existing rules in the rule set. Formally, a contradiction would occur if the inserted tuple would evaluate to a different classification in the rule set. If a rule is found that results in a different classification, then the inserted tuple is in direct contradiction with that rule. The $\neg EVAL$ connective is used in the selection criterion evaluation to find the contradicting rule. The $\neg EVAL$ connective finds consequences that do not match the classification in the tuples. The use of $\neg EVAL$ reverses the interpretation of the query results. If the result of the query is null, then there is no contradiction, and a disruption does not exist. If the result of the query is non-null, then a contradicting rule exists, and a disruption has occurred. For the above update, the query to make this evaluation is as follows:

select R#

from PERFORM-RULES

where ANTECEDENT eval

(select AGE, COMPETITION from PU)

and CONSEQUENCE $\neg$ eval (select PROFIT from PU)

Query Result: R3

The result of the above query is Rule R3. The inserted tuple is in direct contradiction with R3 because R3 states that companies with AGE = "Midlife" and COMPETITION = "No" have an upwards profit potential, whereas, the updated tuple specified an instance of a company with AGE = "Midlife", COMPETITION = "No", and PROFIT = "Down".

## 5.5. Example disrupter: deletion from the rule set

As another example of inductive consistency disrupters, consider an update that deletes a rule from PERFORM-RULES. It is expected that because the rules were initially derived inductively from the data, the removal of a rule from PERFORM-RULES would result in a disruption. Consider the following update that deletes a rule from PERFORM-RULES:

delete PERFORM-RULES

where R# = "R2"

Because this update deletes the entire tuple, and R# is the primary key of PERFORM-RULES, it has changed the extension of PERFORM-RULES. It is therefore necessary to query the data set to determine if this update causes a restricting transfer change that narrows the extension in a way that affects the inductive consistency relationship. The following query will determine if the update causes a restricting transfer change:

select PROFIT, AGE, COMPETITION, TYPE

from PERFORM-DATA

where AGE, COMPETITION eval

(select ANTECEDENT

from PU)

and PROFIT eval (select CONSEQUENCE from PU)

Query Result: Up New No Hardware

Up New No Software

Up New Yes Software

Because the result of the above query is non-null, the update results in a restricting transfer change. The deleted rule was able to classify the data tuples. The update will cause a disruption.

## 5.6. Summary

In this section, we demonstrated how we have operationalized our disruption recognition strategy in the relational model using an instance of inductive consistency and example disruptions. The two disrupting instances were an insertion to the data set that results in a final state change and a deletion from the rule set that results in a restricting transfer change. Although not shown, deletions from the data set that result in a restricting transfer change and insertions to the rule set that result in a final state change will also be disrupting.

Our approach makes use of SQL to recognize evidence of disruptions. The EVAL connective was introduced as the means of evaluating equivalence between subqueries. The selection criterion is used, from the extension constraint, to tailor the specific SQL queries that isolate disruptions. Specifically, the selection criterion helps to identify specific rule/data contradictions. The $\neg$ EVAL connective is used to detect classifications that do not evaluate to the specified selection criterion. Using the $\neg$ EVAL connective in final state change queries reverses the interpretation of the query results, i.e., a non-null query result points to a contradiction. In queries on rule sets, the $\neg$ EVAL connective will detect the rules that contradict an inserted data tuple. In queries on data sets, the $\neg$ EVAL connective will detect the data tuples that contradict an inserted rule.

## 6. Conclusions and future directions

In this article, we have presented a disruption recognition strategy for inductive consistency. Inductive consistency represents an integrity control challenge for KBDSS that integrate environmental data with inductively derived rules. The inductive consistency relationship was modeled using instances of the intension dependency, which captures an existence relationship between two sources of knowledge – i.e., one knowledge source exists from the other. Recognizing inductive consistency violations provides the first defense to averting brittleness in a KBDSS environment. Brittleness can occur when the knowledge within a KBDSS cannot adapt to the changing environment. Serious consequences will result, over time, if KBDSS cannot recognize and refine knowledge to support the changing business environment.

Our next direction for research focuses on refining our prototype that was developed earlier to investigate the problem of inductive consistency. The initial prototype showed the importance of the inductive consistency problem, but did not provide a uniform control strategy. Our strategy to recognize evidence that defeats the extension constraints, that model inductive consistency, does provide a uniform control strategy. We are presently redesigning our prototype to correspond to the disruption recognition strategy presented in this article.

Additional research is focused on addressing the problem of refining knowledge once a disruption is recognized. The prototype system mentioned above will provide the technological tool for exploring different refinement strategies as we make our way toward controlling brittleness in KBDSS.

## References

[1] L.M. Applegate, J.I. Cash, Jr., and D.Q. Mills (1988), November-December), Information technology and tomorrow's manager, Harvard Business Review, 128–136.

[2] A. Barr, and E. Feigenbaum (1982), Applications-oriented AI research: Science. In A. Barr and E.A. Feigenbaum (Eds.), The handbook of artificial intelligence Vol. 2 (pp. 78–174), Reading, MA: Addison-Wesley Publishing.

[3] A. Basden (1983), On the application of expert systems, International Journal Man-Machine Studies, 19, 461–477.

[4] R. Blanning (1986), A relational framework for information management, In E.R. McLean, H.G. Sol (Eds.), Decision support systems: A decade in perspective (pp. 25–40), North-Holland: Elsevier Science Publishers B.V.

[5] R. Bonczek, C. Holsapple, and A. Whinston (1980), The evolving roles of models in decision support systems, Decision Sciences, 11, 337–356.

[6] H. Braun, and J.S. Chandler (1987), Predicting stock

market behavior through rule induction: An application of the learning from-example approach, Decision Sciences, 13, 415–429.

[7] R. Carnap (1962), Logical foundations of probability (2nd Ed.), New York: Wiley.

[8] C. Carter and J. Catlett (1987, Fall), Assessing credit card applications using machine learning, IEEE Expert, 71–79.

[9] E.F. Codd (1990), The relational model for database management: Version 2, Reading, MA: Addison-Wesley Publishing Company.

[10] C.J. Date (1986), An introduction to database systems, Reading, MA: Addison-Wesley Publishing Company.

[11] J. de Kleer (1986), An assumption-based TMS, Artificial Intelligence, 28, 231–272.

[12] W.E. Deming (1990, August), A System of Profound Knowledge, Action Line, 20–26.

[13] V. Dhar (1987), On the plausibility and scope of expert systems in management, Journal of Management Information Systems, 4(1), 25–41.

[14] D.R. Dolk (1988), Model management and structured modelling: The role of an information resource dictionary system, Communications of the ACM, 31, 704–718.

[15] J. Doyle (1979), A truth maintenance system, Artificial Intelligence, 12, 231–272.

[16] O. El Sawy and B. Nanus (1989), Toward the design of robust information systems, Journal of Management Information Systems, 5(4), pp. 33–54.

[17] P. Gardenfors and D. Makinson (1988), Revisions of knowledge systems using epistemic entrenchment, In M. Yardi (Ed.), Proc. of the Second Conference on Theoretical Aspects of Reasoning About Knowledge (pp. 83–96), Los Altos, CA: Morgan Kaufmann Publishers, Inc.

[18] A. Ginsberg (1986), A metalinguistic approach to the construction of knowledge base refinement systems, Proceedings of the 5th National Conference on Artificial Intelligence (pp. 436–441).

[19] A. Ginsberg and P. Politakis (1985), SEEK2: A generalized approach to automatic knowledge base refinement, Proceedings of the Ninth International Joint Conference on Artificial Intelligence (pp. 367–374).

[20] G.A. Gorry and R.B. Krumland (1983), Artificial intelligence research and decision support systems, In J.L. Bennett (Ed.), Building decision support systems (pp. 205–219). Reading, MA: Addison Wesley Publishing.

[21] M. Goul, B. Shane, and F. Tonge (1986), Knowledge based decision support systems in strategic planning decisions: An empirical study, Jrnl of Management Information Systems, 2(4), 70–84.

[22] M. Goul and F. Tonge (1987), Project IPMA: Applying decision support system design principles to building expert-based systems, Decision Sciences, 18, 448–467.

[23] V. Guha and D.B. Lenat (1990), Cyc: A midterm report, AI Magazine, 11, 32–5.

[24] F. Hayes-Roth, D. Waterman, and D. Lenat (1983), Building expert systems, Reading MA: Addison-Wesley Publishing.

[25] J.C. Henderson (1987), Finding synergy between decision support systems and expert systems research, Decision Sciences, 18, 333–349.

[26] E.B. Hunt, J. Marin, and P. Stone (1966), Experiments in induction, New York: Academic Press.

[27] V.S. Jacobs, L.D. Gaultney, and G. Savendy (1986), Strategies and biases in human decision-making and their implications for expert systems, Behaviour and Information Technology, 5(2), 119–149.

[28] F.C. Keil (1981), Constraints on knowledge and cognitive development, Psychological Review, 88(3), 197–227.

[29] S.O. Kimbrough and F. Adams (1988), Why nonmonotonic logic? Decision Support Systems, 4, 111–127.

[30] M. Lenard (1986), Representing models as data, Journal of Management Information Systems, 2(4), 39–48.

[31] D.B. Lenat (1989), Ontological versus knowledge engineering, IEEE Transactions on Knowledge and Data Engineering, 1(1), 84–88.

[32] R.S. Michalski (1983), A theory and methodology of inductive learning, In R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (Eds.), Machine Learning An Artificial Intelligence Approach (pp. 83–134). Los Altos, CA: Morgan Kaufmann.

[33] R.S. Michalski, and R.I. Chilausky (1980), Learning by being told and learning from examples: An experimental comparison of the two methods of knowledge acquisition in the context of developing an expert system for soybean disease diagnosis, Policy Analysis and Information Systems, 4(2), 125–160.

[34] R.S. Michalski, and R. Stepp (1982), Revealing conceptual structure in data by inductive inference, In J.E. Hayes, D. Michie, and Y-H Pao, Machine intelligence 10 (pp. 173–196), Chichester: Ellis Horwood Limited.

[35] D. Nute (1988), Defeasible reasoning and decision support systems, Decision Support Systems, 4, 97–110.

[36] D. Nute, R.I. Mann, and F. Brewer (1990), Controlling expert system recommendations with defeasible logic, Decision Support Systems, 6, 153–164.

[37] H.D. Owens (1992), Formal Models for Integrity Control in Interdependent Knowledge-source Environments: A Relational Model Approach (Doctoral Dissertation, Arizona State University, 1992).

[38] P. Politakis, and S.M. Weiss (1984), Using empirical analysis to refine expert system knowledge bases, Artificial Intelligence, 22, 23–48.

[39] J.L. Pollock (1987), Defeasible reasoning, Cognitive Science, 11, 481–518.

[40] J.R. Quinlan (1983), Learning efficient classification procedures and their application to chess end games, In R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (Eds.), Machine learning: An artificial intelligence approach (pp. 463–482). Los Altos, CA: Morgan Kaufmann.

[41] R. Rada (1985), Gradualness facilitates knowledge refinement, IEEE Transactions on Pattern Analysis and Machine Intelligence, 7, 523–530.

[42] T. Sandman (1990), Induction support systems: Transferring machine learning technology to the business environment (Doctoral dissertation, Arizona State University, 1990).

[43] A. Sen and G. Biswas (1985), Decision support systems: An expert systems approach, Decision Support Systems, 1, 197–204.

[44] A. Sen and J. Choobineh (1990), Deductive data modelling: A new trend in database management for decision support systems, Decision Support Systems, 6, 45–57.

[45] M.J. Shaw (1987), Inductive learning and knowledge-based expert systems, Decision Support Systems, 3, 319-332.

[46] M. Stonebraker, E. Hanson, and S. Potamianos (1988), The POSTGRES rule manager, IEEE Trans, on Software Engineering, 14, 897–907.

[47] B. Thompson, and W. Thompson (1986, November), Finding rules in data, BYTE, 149–158.

[48] E. Turbin, and P. Watkins (1986), Integrating expert systems and decision support systems, MIS Quarterly, 10(2), 1986, 121–136.
