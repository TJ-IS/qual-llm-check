---
otero_id: 17760
otero_key: "2RAU2RPE"
title: "An ontological and semantical approach to source-receiver interoperability"
authors: "Jacob L. Lee; Michael D. Siegel"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00012-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An ontological and semantical approach to source-receiver interoperability

Jacob L. Lee $^{*}$ , Michael D. Siegel

Sloan School of Management, Massachusetts Institute of Technology, 50 Memorial Drive, Cambridge, MA 02139, USA

## Abstract

Given the current explosion of information resources available to decision makers, achieving semantic interoperability between a data source (e.g., a database) and a data receiver (e.g., a decision maker) is more critical than ever. As decision makers interact with unfamiliar sources that have been independently created and maintained, they need to expend non-trivial cognitive effort to understand the meaning of the information contained within these sources. To address this problem, an architecture called the Context Interchange Architecture is proposed. The central component in this architecture is the context mediator, an intelligent agent which facilitates source-receiver interoperability by enabling the receiver to issue queries and to be presented with answers in a manner that is consistent with the receiver's preferences, goals and knowledge. As a result, a convenient and consistent interface is presented to the receiver, reducing the cognitive effort required for the interaction. In this paper, the theoretical foundation for this architecture, based on the philosophical disciplines of Ontology and Semantics, is presented. A key result of this paper is the formal definition of the external behavior of the context mediator. Such a formal characterization provides a basis for the subsequent design of the knowledge representation and reasoning processes internal to the mediator.

Keywords: Context; Ontology; Semantics; Interoperability

## 1. Introduction

The increased access to and the proliferation of information resources are both a boon and a bane to decision makers. The former because of the easy availability of information required for decision making. The latter because decision makers are required to expend non-trivial cognitive effort in order to filter off irrelevant information and to make sense of the relevant information that remains. This problem arises because a data source (e.g., a database) and a data receiver (e.g., a decision maker) can have different contexts. Sources have been independently created and maintained with some underlying assumptions and goals in mind. Receivers, too, have preferences, goals and underlying assumptions, and which may not be consistent with those of the sources. This problem has led us to propose an architecture called the Context Interchange Architecture. The central goal of this architecture is to facilitate semantic interoperability between a source and a receiver while preserving not only the autonomy of the source, but also that of the receiver. Preserving receiver autonomy requires that the receiver be allowed to issue queries and be presented with answers in a manner consistent with its own preferences, goals and knowledge. It is the key to reducing the cognitive effort required of the decision maker to interact with multiple, unfamiliar and dynamically changing sources.

There are several distinguishing features of the Context Interchange Architecture. This architecture requires sources and receivers to explicate their contexts. The central actor in this architecture is the context mediator. The context mediator is an intelligent agent which draws upon explicated context knowledge as well as available conversion knowledge to automatically identify relationships between a source context and a receiver context. It then performs the task of mediating the interaction between source and receiver, preserving the autonomy of both. Conversion knowledge needs to be specified once and can be re-used by the context mediator. As sources and receivers enter and leave the federation, or change their contexts, identifying the relationships between sources and receivers can be automatically carried out by the context mediator. We claim that, as a result, this architecture is both scalable and flexible.

In this paper, we present the philosophical foundations underlying this architecture. Our primary concern is to formally explicate the notion of context, conversion and the external behavior of the context mediator. A definition of what a context mediator should do is a critical and necessary precursor to determining how a context mediator should do it. We are therefore not presenting an implementation. An implementable, albeit limited, model based on the Context Interchange approach has been proposed [16]. In addition, a limited prototype, based on this model, has been implemented and is described elsewhere [10]. Furthermore, although we will use the relational data model [8] to illustrate our ideas, the theory developed in this paper is not driven nor limited by any data model in particular. Rather, we present a theoretical foundation, based on the philosophical disciplines of Semantics and Ontology, that should lead to theoretically grounded implementations.

## 1.1. Background and motivation

Drawing upon the discipline of Semantics due to Bunge [4], we distinguish among the notions of a symbol, a construct, and a context. A symbol is a label (e.g., a character string) that is used to designate meaning. A construct on the other hand is the meaning assigned to a symbol and has no physical existence apart from mental processes ([4]: pp. 21–23). The most basic difficulty in achieving semantic interoperability is due to the uncoordinated use of symbols among different autonomous agents to designate meaning. For example, different symbols might be used to designate the same meaning, or the same symbol might be used to designate different meanings. These are examples of symbolic heterogeneity referred to as synonyms and homonyms [3]. Symbolic heterogeneity has been extensively discussed in the database integration literature.

However, even if the problem of symbolic heterogeneity was resolved, decision makers still have to contend with the problem of context heterogeneity which, by comparison, has received relatively less attention. Informally, a context defines a set of constructs. Specifically, a source context defines the set of constructs that can be expressed by the source, while a receiver context defines the set of constructs that are acceptable to a receiver. One important type of construct defined in a context is the proposition. A proposition is a statement or fact to which we can attach a truth value. Propositions are designated by symbolic items called sentences. We will enter into a more formal and detailed discussion of context in Section 2.

Difficulties can arise when a source and receiver attempt to communicate in the presence of context heterogeneity. This can lead, for example, to retrieval of answers that are irrelevant, ambiguous, incorrect and/or meaningless to the receiver. Given this situation, two potential approaches might be considered. In the first approach, the receiver is required to understand the context of the source. In the second approach, the source needs to present information in a manner consistent with the receiver's context. Either approach, however, will violate the autonomy of the receiver and the source respectively. As a third alternative, potentially meaningful information from a source can be converted to information consistent with the receiver's context without violating the autonomy of either. This is the approach adopted by the Context Interchange Architecture. To give a more concrete description of what we mean, we shall consider an example. As we are primarily concerned with resolving context heterogeneity, we shall assume that there is no symbolic heterogeneity involved.

<table><tr><td>COMPANY</td><td>CITY</td></tr><tr><td>C1</td><td>New York</td></tr><tr><td>C2</td><td>Tokyo</td></tr><tr><td>C3</td><td>London</td></tr><tr><td>C4</td><td>Chicago</td></tr></table>

Fig. 1. Source relation.

Fig. 1 shows a relation called HEAD\_OFFICE which contains the set of propositions on companies and the cities in which their head offices are located. Furthermore, the receiver's view has the schema COUNTRY\_OF\_INCORPORATION (COMPANY, COUNTRY). This means that the receiver "sees" a virtual table against which it can issue queries. In its context, the receiver understands the notions of COMPANY, COUNTRY and COUNTRY\_OF\_INCORPORATION. It does not, however, understand the notion of HEAD\_OFFICE or CITY. Furthermore, there is a domain associated with each column in both the source and receiver schemas. For example, the domain of COMPANY in the relation HEAD\_OFFICE is C1, C2, C3, and C4, while the domain of COMPANY in the receiver schema is C2, C3, C4 and C5. Note that the domain of COMPANY in the receiver's schema can and does differ from that of the source.

Besides domain constraints, there can be other integrity constraints (e.g., functional dependencies) associated not only with the source relation, but with the receiver's view as well. For the purpose of this example, however, we shall consider only domain constraints. A cursory examination of both the source and the receiver schemas might lead us to conclude that the source information is irrelevant to the receiver's interests. As it stands, each proposition in the source context is not relevant or acceptable to the receiver.

Now suppose that for all the companies x that the source and receiver are concerned with (i.e., C1 to C5), it is generally known or agreed upon that if the head office of x is located in a city y, and if city y is in country z, then the country of incorporation of company x is country z. Knowledge of which cities are in which countries is also available. This knowledge, shown in Fig. 2, may be used to convert propositions in the source to propositions acceptable to the receiver. For instance, the statement “The head office of C4 is in Chicago” in the source can be converted to “The country of incorporation of C4 is USA” which can then be processed meaningfully by the receiver. For this reason, the propositions described in Fig. 2 are collectively referred to as conversion knowledge. Thus, ideally, the receiver’s view can be populated as shown in Fig. 3. Essentially, the propositions in this table can be “proven” from the facts in the source and the conversion knowledge. The company C1 has been correctly excluded from the receiver’s view because it is not within the receiver’s domain. Furthermore, as the source knows nothing about C5, the corresponding value for COUNTRY of C5 is null.

The receiver may then issue the following SQL query:

select COMPANY

from COUNTRY\_OF\_INCORPORATION

where COUNTRY = “USA”

The answer returned should be C4, which is consistent with the receiver context. Thus, meaningful interaction between source and receiver can still take place! This simple example illustrates the preservation of receiver autonomy. That is, the receiver should be allowed to issue queries and be presented with answers in terms of constructs it understands. Furthermore, the receiver was not required to explicitly state its assumptions that are normally “taken for granted” in its local environment within a query. Observe that the company C1 was excluded from the answer without requiring the receiver to make the domain restriction explicit in the query. In this particular example, domain assumptions are taken for granted by the receiver. This is common practice because domain assumptions, like most context assumptions, tend to be stable over time, and explicating them within a query may require non-trivial effort. For example, the receiver should not be required to issue a query in which domain assumptions are explicated i.e.:

![](/api/attachments/2RAU2RPE/fulltext/images/17bbaec504d4e3360676e9fc0a9a599cdc0e81c33e2e1983fe4c78e4e9ec9d6a.jpg)  
Fig. 2. Available conversion knowledge.

COUNTRY\_OF\_INCORPORATION

<table><tr><td>COMPANY</td><td>COUNTRY</td></tr><tr><td>C2</td><td>Japan</td></tr><tr><td>C3</td><td>England</td></tr><tr><td>C4</td><td>USA</td></tr><tr><td>C5</td><td></td></tr></table>

Fig. 3. Receiver's view.

select COMPANY

```python
from COUNTRY_OF_INCORPORATION
where COUNTRY = "USA"
and
(
COMPANY = "C2"
or
COMPANY = "C3"
or
COMPANY = "C4"
or
COMPANY = "C5"
)
```

This does not mean, however, that the receiver need not state its context at all. Rather, we are advocating that the context of a receiver be stated outside the confines of a query. As the context tends to be stable over time, it can be reused to appropriately process queries during the period in which the context applies. The receiver need not restate its context each time it issues a query. Consequently, a consistent and convenient user interface is presented to the receiver regardless of the source. Supporting receiver autonomy is the key to minimizing the cognitive effort required by decision makers to interact with sources of data that are independently created and maintained.

To appreciate the difficulty of achieving such a level of semantic interoperability while preserving the autonomy of both sources and receivers, the reader is invited to consider how the same results can be accomplished using an approach based on schema integration as described in [2]. One will quickly realize that such techniques will not be very useful in such a situation. Observe that in this case, it is difficult to define the receiver's view in terms of the source schema because knowledge outside the source, namely the countries in which the various cities are located, is required. Thus, in order to interoperate, the receiver is forced to change its "view of the world". Specifically, the receiver must first find out which cities are located in the USA. Then, it must issue a query against the HEAD\_OFFICE relation to find out which companies have head offices in these cities, and finally conclude that these companies are incorporated in the USA. This simple problem illustrates the potential demands on decision makers if their autonomy is not preserved. The Context Interchange Architecture, which we describe in the following, is aimed at preserving both source and receiver autonomy while maintaining a high level of semantic interoperability.

## 1.2. Organization of paper

The paper is organized as follows. In Section 2, we give an overview of the Context Interchange Architecture. In Section 3, we introduce some basic concepts and ideas from Mario Bunge's Semantics [4] and Ontology [6,7] which will serve as a conceptual foundation for the research presented here. In Section 4 we show how these concepts form the underlying foundation for the Context Interchange Architecture. The main result in this section is a definition of the external behavior of the context mediator. A discussion on conversion knowledge and context knowledge is presented in Section 5. We conclude in Section 6.

## 2. The context interchange architecture: An overview

The Context Interchange Architecture is shown in Fig. 4. A key component in this architecture is the context mediator, an intelligent agent which mediates the interaction between a source and a receiver, both of which can exist in different contexts. In this architecture, both the source and receiver are required to explicitly represent their contexts. The explication of the receiver's context, however, takes place outside the confines of a query. The ontology base contains conversion knowledge which specifies relationships between constructs in the source and receiver context. The context mediator, drawing upon both context knowledge and conversion knowledge, appropriately processes queries and retrieves answers without violating the autonomy of the source and receiver.

A data source represents some collection of statements or facts about the world which may be retrieved by a receiver. However, as noted earlier, a statement in a source context will not always be acceptable to a receiver. Often, in order for the receiver to “understand” the source statement, it has to be converted to an “equivalent” statement that exists in the receiver’s context. For instance, we saw that the statement “The head office of C4 is in Chicago” should be converted to “The country of incorporation of C4 is USA”. The Context Interchange Architecture can therefore be analyzed as follows. The source is a set of sentences (symbols) which designate some propositions (constructs) about a domain of interest. The source context defines the set of allowable propositions that can be asserted by the source. The receiver context defines the set of propositions that are acceptable to the receiver. We shall assume that all contexts and the ontology base is specified using a common symbol system, i.e., a universal language. In all probability, this universal language will differ from the languages used by the source and the receiver. The set of sentences in the source, therefore, corresponds to some subset of sentences in the source context (Arrow 1). This correspondence involves only a symbolic transformation of sentences in the source language to sentences of the universal language. A query issued by the receiver defines a set of propositions within its context that has to be “proven”, based on propositions asserted by the source and conversion knowledge within the ontology base (Arrow 2).

![](/api/attachments/2RAU2RPE/fulltext/images/a5235657ee30c0cdb9f332523c167749b1d74d84407965870ee6f49cda38c131.jpg)  
Fig. 4. Source receiver model.

In our preceding example, the propositions to be deduced are “The country of incorporation of Ci is USA” where i = 2, 3, 4 and 5. In this case, the only proposition that can be deduced is “The country of incorporation of C4 is USA”. Arrow 3 indicates a symbolic transformation of the deduced answers as sentences of the universal language to the language of the receiver. Note that the preceding discussion is intended as an analytic description, not a computational one.

In this paper, we are particularly interested in Arrow 2, which represents a fundamental and essential aspect of source-receiver interoperability. We are concerned with the convertibility of propositions in the source context to “equivalent” statements in the receiver context. For this reason, and for simplicity of exposition, we shall not deal with issues of symbolic heterogeneity, i.e., we will not be concerned with Arrow 1 and Arrow 3. The main result of this paper is a formal characterization of the context mediator grounded in theories from Ontology and Semantics. More specifically, we define the input-output behavior of the context mediator based on precisely explicated notions of a context, conversion and an ontology base. A definition of the context mediator, based on these formally defined concepts, provides a basis for the subsequent design of the knowledge representation and reasoning processes internal to the mediator. The ideas and concepts discussed in this paper, although described in terms of a single-source/single-receiver model, is intended to be generalizable to systems with multiple, autonomous and heterogeneous sources and receivers.

## 3. Ontology and semantics

## 3.1. Ontology

Bunge's Ontology [6,7] has been introduced and applied in the context information systems research. We will, therefore, not go into a detailed discussion, but limit ourselves to ideas that are particularly relevant for the current topic of discussion. A more detailed discussion on Bunge's Ontology and its application to information systems is found in these references [18–22].

According to Bunge “...an ontology is not a set of things but a philosophical theory concerning the basic traits of the world” ([4]: p. 38). In Bunge’s Ontology, the world is made up of things. Things possess properties. We perceive the properties of things via attributes. That is, we only know properties as attributes. A property is a feature that a thing possesses even if we are ignorant of this fact. On the other hand, an attribute is a feature we assign to a thing ([6]: p. 58). Therefore there is a distinction between an attribute and a property of a thing. An attribute, (e.g., weight) represents a property in general while an attribute value (e.g., 36 kilograms) represents a property in particular. A collection of objects possessing the same property in particular is referred to as a class.

There are simple and complex things. A complex thing, or system, is made up of simpler things that interact. There is a part-whole relationship between a system and its components. An example of a system is the computer which is made up of simpler, interacting things such as the central processing unit (CPU), memory and keyboard etc. This is called an aggregation hierarchy. Complex things have inherited and emergent properties, and hence, inherited and emergent attributes. An inherited attribute is an attribute common to a system and one of its components. For example, the clock speed of computer is an inherited attribute because it is also the clock speed of the computer's CPU. An emergent attribute is an attribute of a complex thing as a whole but not of any of its components (e.g., the computational power of the computer is an attribute of the computer, but not of any one component).

The state of a thing is represented by a combination of its attribute values. For example, the title of an employee in an organization refers to a state of an employee. The state of a thing can vary over time and space. One useful property of time and space not discussed by Bunge, but which will prove useful, is the concept of granularity. Consider for example the day 4 July 1987. This date refers to a 24-hour period within the month of July 1987 which is within the year 1987. This is an example of a granularity hierarchy of time (Fig. 5a). The smallest granularity of time is an instant. No time periods can therefore appear below an instant in a granularity hierarchy of time. Similarly, Chicago is in the USA is an example of a granularity hierarchy of space (Fig. 5b). The smallest granularity of space is a point. No space values can appear below a point in a granularity hierarchy of space.

The combination of attribute values is restricted by state laws which define the legal states that a thing can take. An event is a change in the state of a thing and is represented as an ordered pair of states. For example, a promotion is an event where the title of an employee changes.

![](/api/attachments/2RAU2RPE/fulltext/images/74a8cade72e5e628e461ac410f51226c4786fc9880c2ccdf51ab1de1521f7bba.jpg)  
Fig. 5. Granularity hierarchy of: (a) time, and (b) space.

## 3.2. Semantics

## 3.2.1. Predicates, arguments and propositions

Bunge's work also encompasses the discipline of Semantics [4,5] which he describes as “...concerned not only with linguistic items but also, and primarily, with the constructs such items stand for and their eventual relation to the real world” ([4]: p. 2). Predicates, propositions and predicate arguments are constructs. A predicate, as Bunge defined it, is a template for instantiating propositions. In fact, a predicate is sometimes referred to by Bunge as a statement schema. Propositions are obtained by instantiating the predicate arguments. Note that Bunge's notion of a predicate differs from that in traditional first order logic in that there is no extension associated with a predicate ([4]: p. 16). In other words, Bunge's notion of a predicate does not include a commitment as to the truth or falsity of a proposition. The union of all possible argument values that a predicate can take is referred to as its reference class.

Bunge also proposed that “Scientific concepts are often partitioned into constants and variables” ([4]: p. 40), namely

1. Object variables and constants;

2. Property variables and constants;

3. Spatio-temporal variables and constants;

4. Units variables and constants; and

5. Proportionality (i.e., scale) variables and constants.

In other words, arguments of predicates corresponding to attributes can be classified according to the following types: (i) object, (ii) property, (iii) space, (iv) time, (v) unit, and (vi) scale ([4]: p. 40). The object variable ranges over a class of things. The object constant refers to an individual thing. The property variable ranges over a set of attribute values while a property constant corresponds to an attribute value. An attribute value may be associated with a unit (e.g., currency unit such as Yen). Time and space values indicate the temporal and spatial location of a thing. A proportionality variable is nothing more than a scale factor.

## 3.2.2. Context

Bunge defines a context as $\mathbf{C} = (S, P, D)$ ([4]: p. 57). $D$ , the domain of the context, is the union of all the reference classes of the all the predicates in the set P. Each individual in D is associated with a type as discussed above. There are no other individuals in C other than those in D. The predicates in P are the only ones that are allowed in C and each has a well-defined arity. Examples of predicates are classes, relationships, attributes, events etc. S is a restricted set of propositions that are allowed within the context. The most basic restriction on S is that propositions must be formed from predicates in P and arguments from D. Type restrictions can also be imposed by restricting each argument of a predicate to a subset of values in D. State laws can also impose restrictions on the combinations of values a predicate can take.

Bunge's notion of a context, therefore, highlights three important components. $D$ is an important component because it defines the set of all the individuals that a source knows about, and all the individuals that a receiver is interested in. $D$ defines the scope of universal quantification (i.e., “for all x”) which may vary from context to context. $P$ is an important component of a context because it represents the kinds of knowledge that a source may have about the individuals in $D$ or the kind of knowledge that a receiver is interested in. In our example, the source contains knowledge of cities in which the head offices of certain companies are located, while the receiver is interested in the countries in which certain companies are incorporated. In the source context, $S$ is the set of propositions that can be expressed. In the receiver context, $S$ is the set of propositions that are acceptable.

## 3.2.3. Meaning relations

Table 1 shows some basic ideas drawn from Semantics as described in ([1]: pp. 203–212). We have already noted the distinction between a construct and a symbol. Two classes of symbols are words (e.g., loves) and sentences (e.g., Jack loves Jill). Words designate a class of constructs called concepts and sentences stand for a class of constructs called statements or propositions. There are some important meaning relations in the word-concept class and in the sentence-statement class. In the former, there are meaning relations called homonyms, synonyms and meaning inclusion. We have already discussed homonyms and synonyms. They are instances of symbolic heterogeneity. Meaning inclusion is a type of relationship among concepts. For example, the meaning of Parent includes the meaning of Father. The meaning relation in the sentence-statement class is entailment. That is, the truth of a proposition necessitates the truth of another.

Table 1  
Meaning relations

<table><tr><td>Symbol</td><td>Word</td><td>Sentence</td></tr><tr><td>Construct</td><td>Concept</td><td>Statement</td></tr><tr><td>Important meaning relations</td><td>Homonyms, synonyms, meaning inclusion</td><td>Entailment</td></tr><tr><td>Example</td><td>“Loves”</td><td>“Jack loves Jill”</td></tr></table>

These meaning relations are important because they may be used to achieve semantic interoperability. Homonyms and synonyms are the most basic and well known meaning relations. In database circles, meaning inclusion is referred to as generalization and has been identified as an important mechanism for database integration [12] because of concepts that exist at differing levels of abstraction. Class hierarchies are typical operationalizations of meaning inclusion. Homonyms, synonyms and meaning inclusion have been heavily exploited by the database integration community. However, entailment or logical implication has received very little attention by comparison. Logical deduction is a very general and powerful means of performing conversions and achieving greater semantic interoperability. Meaning inclusion can be considered a special case of logical deduction, e.g., $\forall x$ Father(x) $\Rightarrow$ Parent(x). Logical deduction enables semantic interoperability in situations where meaning inclusion cannot (as in our example described in Section 1). In the next section, we discuss how the notion of logical deduction can be used in the Context Interchange Architecture to achieve a higher degree of semantic interoperability between a source and receiver with different contexts.

## 4. Applying ontology and semantics to context interchange

Let $\mathbf{C}_s = \langle S_s, P_s, D_s \rangle$ and $\mathbf{C}_r = \langle S_r, P_r, D_r \rangle$ be the source and receiver contexts respectively. Fur ther, let $C_{g} = \langle S_{g}, P_{g}, D_{g} \rangle$ be a context where $S_{s}, S_{r} \subseteq S_{g}; P_{s}, P_{r} \subseteq P_{g}; D_{s}, D_{r} \subseteq D_{g}$ . $C_{g}$ is called the global context. We shall assume that the source asserts only ground propositions (i.e., facts in which there are no variable arguments) $S_{t} \subseteq S_{s}$ . The set of ground propositions defined by a query to be proven is $S_{q} \subseteq S_{r}$ . Conversion knowledge is expressed as a set of conversion axioms $S_{c}$ , which define the entailment relationships among the propositions in $S_{g}$ . Conversion axioms can contain quantifiers and variables. Quantification of conversion axioms takes place over the domain $D_{g}$ of the global context $C_{g}$ . We now formally state the desired behavior of the context mediator:

Given $S_{c}$ , $S_{q}$ and $S_{t}$ , the context mediator outputs $S_{a} \subseteq S_{q}$ which is the set of logical consequences of $S_{c}$ and $S_{t}$ over the domain $D_{g}$ .

A number of comments are now in order. First, in first order logic [13], a set of propositions, say $S_{1}$ , are logical consequences of other propositions, say $S_{2}$ , if $S_{1}$ is true in all the interpretations in which $S_{2}$ is true. In general, interpretations can have different domains, which is the set of values being quantified over. In our definition of the context mediator however, we are concerned only with interpretations whose domain is $D_{g}$ . This is because conversion axioms, which can contain quantifiers, represent general knowledge about a particular global domain of interest. A quantification in the receiver context, say in a query, iterates over the domain $D_{r}$ . Similarly, quantification in the source context iterates over the domain $D_{s}$ .

Second, although the description of the context mediator is in logical terms, we do not necessarily mean to suggest that the context mediator be implemented as a general theorem prover as general theorem proving is known to be undecidable [13]. If the knowledge in the source and ontology base is restricted to certain types of propositions, more efficient retrieval mechanisms can be devised. If the complexity of the knowledge involved in inferencing cannot be avoided, then the completeness of answers may have to be sacrificed for efficiency. The point is this. We have given an abstract, high level description of the context mediator. Issues of efficiency, soundness, completeness, etc., are issues to be considered at the implementation level. Various implementations are possible depending on the choice of the trade-off that is being made. The effectiveness of any implementation should be measured against current approaches for retrieving information which may be labor intensive and time consuming. Taking 4 weeks to automatically generate a report suitable to the context of the decision maker, by the context mediator, might not seem too bad if the alternative is a manual process that would take 12 weeks and 10 persons!

Third, Bunge's Ontology represents some very fundamental knowledge about the world. Building on Bunge's Ontology, more specific knowledge is added for a more specific ontology. For our purposes, an ontology defines the global context $C_{g}$ and appropriate conversion knowledge $S_{c}$ for a particular domain. A particular ontology can be encoded in various ways. A particular encoding of an ontology is called the ontology base, just as a knowledge base is an encoding of some knowledge. Since all the constructs in the source and receiver context are also in the global context, conversion axioms can relate propositions in a source context, to propositions in the receiver context by means of entailment. In the Context Interchange Architecture, conversion is based on the notion of entailment.

Fourth, currently there is a great deal of interest in the development of ontologies to facilitate knowledge sharing in general [15] and database integration in particular [9,16]. To date however, there does not seem to be a consensus on what an ontology (formally) is, or what it should contain. In our opinion, an ontology is simply some basic knowledge about the world. It is a set of commitments that constrains our view in such a way as to provide guidance [11] for the execution of a specific task. We believe that there is no one “correct” ontology, only more or less useful ones depending upon the application in mind. For our purposes, the goal in ontology construction is, therefore, the definition of a global context, and the identification conversion knowledge (i.e., the deductive relationships among propositions in the global context). This knowledge is encoded in a universal language, say $L_{g}$ . Defining the global context requires sources and receivers, within a federation, to commit to a set of suitable predicates, their arities and the type of arguments these predicates should take. Interaction among these sources and receivers will then be mediated by means of these constructs represented by Lg. The global context will also be used to guide context explication at the local level. We will explain this further in Section 5.

Fifth, identifying conversion rules is not unlike the task of a knowledge engineer who elicits knowledge about a particular domain from an expert in order to populate an expert system with rules. Much of the time, this knowledge resides in the heads of humans who manually perform the task of integrating information from disparate sources to provide an integrated view to the decision maker. If this knowledge can be elicited and used to populate the ontology base, the process of converting information from disparate sources into the context of the decision maker can be automated. In Section 5.1, we give examples of the range of example rules that might be used for the purposes of conversion.

Finally, we claim that agreement on the ontology base is critical because it provides the basis for semantic interoperability. To the extent that such an agreement can be achieved, semantic interoperability is facilitated. When no such agreement is possible, semantic interoperability may also not be possible, or might not even be needed because there is nothing to be shared in the first place! We cannot escape this basic requirement whenever we deal with semantic interoperability across different contexts in general. The alternative is to sacrifice autonomy. The important question, therefore, is not whether or not it is reasonable to expect that such an agreement can be achieved. Rather, the issue is how can such an agreement be facilitated. Of course, agreeing on the ontology base does not require agreement on everything. In our example, the source and receiver need not use the same language, although their local languages need to be translatable to the universal language. Furthermore, the source and receiver need not have the same contexts.

## 5. Discussion

In Section 5, we discuss a number of key issues pertaining to conversion and context knowledge. In Section 5.3, we present a brief outline of how both types of knowledge may used in a possible query processing strategy. Our goal, however, is not a rigorous account of an implementation. Rather, our intent is to provide the reader with some hints as to what a possible implementation might involve. In doing so, we hope to further illustrate and clarify some key issues.

## 5.1. Conversion knowledge

After defining the global context, the next step in ontology construction is to identify deductive laws or rules that will serve as conversion knowledge. We now give a range of example conversion rules to illustrate the types of conversions that are possible and should be considered in achieving semantic interoperability. For clarity, the predicate names and arguments which are being converted in statements are highlighted in bold. Furthermore, the type of the argument is indicated by “/” followed by the type name in italics.

1. Conversions based on Generalization:

E.g., If the meaning of TradePrice is a more general LatestTradePrice, then LatestTradePrice (IBM/object, 80/property, 1/scale, USdollars/unit) $\Rightarrow$ TradePrice (IBM/object, 80/property, 1/scale, USdollars/unit).

2. Conversion of Units:

E.g., If 1 US dollar is 110 Yen, then TradePrice (IBM/object, 80/property, 1/scale, USdollars/unit) $\Rightarrow$ TradePrice (IBM/object, 8800/property, 1/scale, Yen/unit).

3. Conversion of Scale:

E.g., TradePrice (IBM/object, 8800/property, 1/scale, Yen/unit) $\Rightarrow$ TradePrice (IBM/object, 88/property, 100/scale, Yen/unit).

4. Conversion based on Inherited Attributes:
E.g., Since the attribute ClockSpeed is inherited by the Computer from the CPU, then ClockSpeed (Computer/object, 33/property, $10^{6}$ /scale, Hz/unit) $\Leftrightarrow$ ClockSpeed (CPU/object, 33/property, $10^{6}$ /scale, Hz/unit). Explanation: The CPU is a part of the Computer. In this example, the clock speed of a computer is 33 MHz and clock speed is an inherited attribute from the CPU. Note that we can perform conversions both ways for inherited attributes.

5. Conversion of Time based on granularity:

E.g., Title (John/object, Sales Manager/property, 1987/time)⇒ Title (John/object, Sales Manager/property, Jun 1987/time) Explanation: “John was Sales Manager for all of 1987” means that “John was Sales Manager for all of Jun 1987”.

E.g., Birth (John/object, 4 Jul 1958/time, Chicago/space) $\Rightarrow$ Birth (John/object, Jul 1958/time, Chicago/space).

Explanation: Since John was born at some instant within the day 4 Jul 1958, it is also true that John was born at some instant within the month Jul 1958. Note that these two conversions go in opposite directions in a granularity hierarchy for time.

6. Conversion of Space based on granularity:

6. Conversion of Space based on granularity.
E.g., Birth (John/object, 4 Jul 1958/time, Chicago/space) $\Rightarrow$ Birth (John/object, 4 Jul 1958/time, USA/space).
Explanation: Since John was born at some point within Chicago, John was therefore born at some point in the USA.

7. Other conversions:

E.g., ParentOf(a/object, b/object,) AND ParentOf(a/object, c/object,) AND ≠(b/object, c/object,) ⇒ SiblingOf(b/object, c/object,.

The two most prevalent forms of conversion knowledge used (particularly approaches advocating the use of global schemas) are generalization and aggregation [12,17]. Conversion rules such as (ii) and (iii) have also been noted in the existing literature [3,12,14]. The remaining types of conversions are less commonly used or practically ignored. Exclusive focus on limited types of conversion rules will only allow us to resolve limited forms of context heterogeneity. Unfortunately, it seems that global schemas can express only limited kinds of conversion knowledge. In our example at the beginning of the paper, instance based knowledge such as “Chicago is in the USA” is needed for conversions but cannot be captured at the level of the global schema. As another example, conversion rule (vii) cannot be expressed by means of a global schema. It is also probably obvious by now that any deductive law can be potentially used for the purposes of conversion. Correspondingly, we should acknowledge and take advantage of this fact by expanding the repertoire of conversion rules. Once the conversion knowledge is encoded, translation across different contexts can be automated. Furthermore, this conversion knowledge can be modified and expanded over time as appropriate.

Converting a proposition from the source context to the receiver context may involve several conversion axioms. This represents a multi-step conversion process. Thus, by specifying a minimal set of conversion axioms, more complex conversions can be performed using a combination of these axioms. Multi-step conversion is a powerful mechanism for achieving a higher level of semantic interoperability.

## 5.2. Context knowledge

Assuming that these sources and receivers are committed to the ontology base, their contexts can then be defined with respect to the ontology base. The goal of context definition is to define the set of propositions that can be expressed by a source, or acceptable to a receiver. Context definitions are also encoded in the global language $L_{g}$ . In our example, part of the receiver context definition ought to define the domain of companies in which the receiver is interested.

As another example of the importance of domains in context definitions, consider an example involving two databases containing hotel information: AAA tour book database and the Mass database. For now, it is not immediately clear what the domain of individual databases are. Presumably, the hotels described in the Mass database are Massachusetts hotels and those in the AAA database are North American hotels (including Canada and Mexico). If so, what happens if a receiver implicitly assumes the context of the Mass database, and asks the AAA database for the average rate of all hotels. If the receiver does not specify its domain of hotels, the default domain might be the domain of hotels in the AAA database. Consequently, the answer returned might instead be the average rate for all hotels in North America, not just Massachusetts. Such domain mismatches, if not accounted for, can result in incorrect answers to queries. To put it simply, if the receiver does not specify a domain, some domain or other will be assigned to the receiver by default, like it or not. Domain restrictions are but one aspect of a context. As indicated our example in Section 1, there can be other forms of constraints on both source and receiver contexts.

Problems can also arise due to implicit arguments. For example, the schema of a relation in a source might be closing\_price (stock, amount, date). As only one currency is allowed in the source context, the currency argument was dropped to economize on the costs of storage of information and communication with receivers that have the same context. Such receivers may issue queries against these sources, asking for the closing prices of stocks on 12/12/94 that are “greater than 40.00”, and still obtain meaningful answers even though the currency was not explicit within the query. Obviously, problems may arise when attempting to communicate across different contexts, for example when multiple currencies are possible in the receiving context.

How is the problem of implicit arguments be addressed in the Context Interchange approach? Ideally, the ontology base can serve as a global guide to explicating implicit arguments at the local level. Recall that aside from containing conversion knowledge, an ontology base also defines the global context. In the global context, the various predicates should have been appropriately defined with various arities and argument types. At the local level, the database administrator will use these definitions as a guide to what arguments need to be specified. For example, suppose that the predicate closing\_price is defined in the ontology base with 4 arguments: stock, amount, date, currency. Based on this definition as a guide, the database administrator will now know that the explication of the currency argument for closing prices is necessary for meaningful information exchange across different contexts. However, the explication of otherwise implicit arguments should be non-intrusive. A source, for example, should not be required to re-organize the presentation of its information. And neither should the receiver be required to make these arguments explicit within a query. The reader may refer to [16] for an example of how this may be done.

## 5.3. A query processing sketch

We will outline a brief sketch of a possible query processing strategy based on the Context Interchange

Architecture, highlighting only key intermediate steps. Our goal is to give the reader some intuitions about the role of contexts and the ontology in query processing. We assume a Prolog-like language for the universal language. The query in our example can therefore be translated to

$$
\text { COUNTRY\_OF\_INCORPORATION } (x _ {1}, x _ {2})
$$

$$
\Lambda = \left(x _ {2}, \text { USA }\right).
$$

Since the receiver context defines the set of propositions acceptable to the source, the context mediator can use this knowledge to further restrict the variables within this query, which is $x_{1}$ in this case, resulting in the following query:

$$
\begin{array}{r l} & \text { COUNTRY\_OF\_INCORPORATION } (x _ {1}, x _ {2}) \\ & \wedge \left(= (x _ {1}, C 2) \vee \dots \vee = (x _ {1}, C 5)\right) \\ & \wedge = (x _ {2}, U S A). \end{array}
$$

However, an examination of the source context by the context mediator will indicate that the source knows nothing about countries in which the companies are incorporated. Therefore, the query has to be converted, by means of the conversion knowledge within the ontology, to one that is suitable to the source context. Furthermore, the source context indicates that it knows only about companies C1–C4. Therefore, this query can be further converted to two appropriate sub-queries which are then issued to the source:

$$
\begin{array}{r l} & \text { HEAD\_OFFICE } (x _ {1}, x _ {2}) (= (x _ {1}, C 2) \vee \dots \vee \\ & = (x _ {1}, C 4)) \wedge \dots \wedge = (x _ {2}, \text { New   York }), \end{array}
$$

and

$$
\begin{array}{r l} & \text { HEAD\_OFFICE } (x _ {1}, x _ {2}) (= (x _ {1}, C 2) \vee \dots \vee \\ & = (x _ {1}, C 4)) \wedge \dots \wedge = (x _ {2}, \text { Chicago }). \end{array}
$$

The answer returned by the source, therefore, is $\langle C4\rangle$ . This is used to instantiate the proposition HEAD\_OFFICE(C4, Chicago), which can then be converted to COUNTRY\_OF\_INCORPORATION-(C4, USA). Finally, the answer presented to the receiver is $\langle C4\rangle$ . Note that the absence of C2 and C3 in the answer is taken to mean that these companies are not incorporated in the USA. However, the absence of C5 is due to the fact that the source has no knowledge of C5. Thus, the domain definition helps to disambiguate and clarify the meaning of the absence of a tuple as an answer. The context mediator may therefore consider searching other sources within the federation to determine whether or not C5 is incorporated in the USA.

## 6. Conclusion

The increasing availability of information to decision makers has been accompanied by the need for these decision makers to expend non-trivial cognitive effort in interpreting this information. This problem arises because a source can have a context that is unfamiliar to the decision maker. Also, this problem is exacerbated because of the multiplicity and variety of sources that have been independently created and maintained, and with which a decision maker might potentially interact. This has led us to propose an architecture called the Context Interchange Architecture. The central goal of this architecture is to facilitate semantic interoperability between a source and a receiver while preserving not only the autonomy of the source but that of the receiver as well. Preserving receiver autonomy is the key to reducing the cognitive effort required of the decision maker to make sense of source information.

This architecture requires both sources and receivers to explicate their contexts. The central actor in this architecture is the context mediator, an intelligent agent that automatically identifies relationships between a source context and a receiver context. It then performs the task of mediating the interaction between source and receiver, preserving the autonomy of both. We claim that this architecture is both scalable and flexible. This is because conversion knowledge needs to be specified once and can be re-used by the context mediator. As sources and receivers enter and leave the federation, or change their contexts, identifying the relationships between sources and receivers is automatically carried out by the context mediator.

We presented the philosophical foundations underlying this architecture. Our primary concern was to formally explicate the notion of context, conversion and the external behavior of the context mediator. A key result of this paper is a definition of what a context mediator should do. Such a definition is a critical and necessary precursor to determining reasoning processes internal to the mediator. The theoretical foundation we developed is based on the philosophical disciplines of Semantics and Ontology. Such a foundation provides a basis for theoretically grounded implementations that are not necessarily limited to any particular data model.

Our analysis also reveals some fundamental limitations that are present in current day thinking about semantic interoperability. Current day approaches pay much attention to issues to symbolic heterogeneity, and issues of context heterogeneity among sources and receivers have received relatively little attention by comparison. Furthermore, the sorts of conversion knowledge that are being used are also limited, perhaps in part due to our current view of what a conversion is, and in part due to the limitations of our present techniques in expressing more complex forms of conversion knowledge. We have given examples of the sorts of conversions that should be considered, and certainly, the current repertoire of conversion knowledge needs to be expanded if we are to achieve higher levels of interoperability.

The theoretical foundation for the Context Interchange Architecture presented here strongly indicates major research challenges to be undertaken in the future. This research involves developing (i) a representation schemes for the ontology base and contexts, (ii) methodologies for eliciting and encoding context and conversion knowledge within these schemes, and (iii) an inferencing scheme for the context mediator to process context knowledge, conversion knowledge and queries. The criteria of correctness of this query processing strategy will be determined by our formal definition of the context mediator.

## Acknowledgements

This work is supported in part by ARPA and USAF/Rome Laboratory under contract F30602-93-C-0160, the International Financial Services Research Center (IFSRC), and the PROductivity From Information Technology (PROFIT) project at MIT. Funding from The National University of Singapore is also gratefully acknowledged.

## References

[1] A. Akmajian, R.A. Demers, A.K. Farmer and R.M. Harnish, Linguistics: An Introduction to Language and Communication, 3rd ed. (MIT Press, Cambridge, MA, 1993).

[2] C. Batini, M. Lenzirini and S. Navathe, A Comparative Analysis of Methodologies for Database Schema Integration, ACM Computing Surveys 18, No. 4 (1986) 323–364.

[3] M.W. Bright, A.R. Hurson and S.H. Pakzad. A Taxonomy and Current Issues in Multidatabase Systems, IEEE Computer (1992) 50–60.

[4] M. Bunge, Semantics I: Sense and Reference (D. Reidel Publishing Company, Boston, 1974).

[5] M. Bunge, Semantics II: Interpretation and Truth (D. Reidel Publishing Company, Boston, 1974).

[6] M. Bunge, Ontology I: The Furniture of the World (D. Reidel Publishing Company, Boston, 1977).

[7] M. Bunge, Ontology II: A World of Systems (D. Reidel Publishing Company, Boston, 1979).

[8] E.F. Codd, A Relational Model of Data for Large Shared Data Banks, Communications of the ACM 13, No. 6 (1970) 377–387.

[9] C. Collett, M.N. Huhns and W. Shen, Resource Integration Using a Large Knowledge Base in Carnot, IEEE Computer 24, No. 12 (1991) 55–63.

[10] A. Daruwala, C.H. Goh, S. Hofmeister, K. Hussein, S. Madnick and M. Siegel, The Context Interchange Network, in: IFIP WG2.6 Sixth Working Conference on Database Semantics (DS-6) (Atlanta, Georgia, 1995).

[11] R. Davis, H. Shrobe and P. Szolovits. What is a Knowledge Representation? Al Magazine (1993) 17–33.

[12] U. Dayal and K. Hwang, View Definition and Generalization for Database Integration in Multidatabase System, IEEE Transactions on Software Engineering SE-10 (1984) 628-644.

[13] H.B. Enderton, A Mathematical Introduction to Logic (Academic Press, San Diego, CA, 1972).

[14] W. Kim and J. Seo. Classifying Schematic and Data Heterogeneity in Multidatabase Systems, IEEE Computer 24, No. 12 (1991) 12–18.

[15] R. Neches, R. Fikes, T. Finin, T. Gruber, R. Patil, T. Senator and W.R. Swartout, Enabling Technology For Knowledge Sharing, AI Magazine 12, No. 3 (1991) 16–36.

[16] E. Sciore, M. Siegel and A. Rosenthal, Using Semantic Values to Facilitate Interoperability Among Heterogenous Information Systems, Transactions on Database Systems 19, No. 2 (1994) 254–290.

[17] J.M. Smith and D.C.P. Smith, Database Abstractions: Aggregation and Generalization, Transactions on Database Systems 2, No. 2 (1977).

[18] Y. Wand, A Proposal for a Formal Model of Objects, in: W. Kim and F. Lochovsky, Eds., Object-Oriented Concepts, Databases, and Applications (ACM Press, New York, 1989) 602.

[19] Y. Wand and R. Weber, An Ontological Analysis of Some Fundamental Information Systems Concepts, in: Proceedings

of the Ninth International Conference on Information Systems (Minneapolis, Minnesota, USA, 1988).

[20] Y. Wand and R. Weber. Mario Bunge's Ontology as a Formal Foundation for Information Systems Concepts, in: P. Weingartner and G.J.W. Dorn, Eds., Studies on Mario Bunge's Treatise (Rodopi, Amsterdam, 1990).

[21] Y. Wand and R. Weber, An Ontological Model of an Information System, IEEE Transactions of Software Engineering 16, No. 11 (1990) 1282–1292.

[22] Y. Wand and R. Weber, Toward a Theory of the Deep Structure of Information Systems, in: Proceedings of the Twelfth International Conference on Information Systems (1991).

![](/api/attachments/2RAU2RPE/fulltext/images/d8e4dbc22ada2640242ce56c7a8c5d2d56cddf1ab46cd727183ec270c8016620.jpg)

Jacob Lee is a doctoral student in the Information Technologies Program at the MIT Sloan School of Management. He received his Bachelor's Degree in Engineering with Honors from the National University of Singapore in 1987. His research interests include information integration for decision making, intelligent database systems and the management of data quality. He enjoys soccer, skiing, photography, traveling and camping.

Michael Siegel is a Principal Research Scientist at the MIT Sloan School of Management. He is currently the Co-Director for the Research Center (FRC) and Associate Director of the Productivity from Information Technology (PROFIT) project. He received his Ph.D. degree in Computer Science from Boston University in 1989. His research interests include heterogeneous database systems, managing data semantics, query optimization, intelligent database systems, learning in database systems, integration sciences and the use of information technology in financial risk management and global financial systems. He has taught courses in Management Information Technology and has been active in the development of both research prototype and state-of-the-art information systems. His research has been published in numerous journals and conference proceedings.
gourmet cook.
