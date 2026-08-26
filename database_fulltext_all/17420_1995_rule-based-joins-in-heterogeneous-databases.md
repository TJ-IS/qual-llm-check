---
otero_id: 17420
otero_key: "NAC5GFTW"
title: "Rule based joins in heterogeneous databases"
authors: "Abhirup Chatterjee; Arie Segev"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0048-i"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Rule based joins in heterogeneous databases

Abhirup Chatterjee $^{*}$ , Arie Segev $^{1}$

Walter A. Haas School of Business, University of California at Berkeley, Berkeley, CA, USA
Information and Computing Sciences Division, Lawrence Berkeley Laboratory, Berkeley, CA 94720, USA

## Abstract

In this paper, the problem of computing joins in heterogeneous databases is analyzed. Rules are combined with a probabilistic framework to resolve the data heterogeneity problem. The Entity join operator is defined to identify and join records across databases. Certain amount of uncertainty is associated with this Entity join model due to the possibility of wrong matches. While the rule based approach captures the data semantics, the probabilistic framework models the uncertainty and provides a formal measure of accuracy of the Entity join. Representing the values of mismatched attributes presents a difficult problem because the true value of the attribute cannot be identified from the various conflicting values. Probabilistic partial values are used to represent these attribute values so that user preferences and reliability of the data can be taken into account.

Keywords: Federated database; Database management system; Structural heterogeneity; Semantic heterogeneity; Rules; Approximation; Join; Tuple probability; Probabilistic partial value

## 1. Introduction

During the past decade, organizations have increased their scope and operations beyond their traditional geographic boundaries. In order to survive the stiff market competition, the number of mergers, acquisitions and joint ventures among businesses have increased at a tremendous rate.

This has significantly changed the information processing needs of the organizations. Furthermore, advancements in computer technology have dramatically increased the number, type, size and complexity of the commercially available Database Management Systems (DBMSs). Organizations have adopted these diverse and frequently incompatible DBMSs without a consideration that one day they may need to integrate their information resources. Consequently, data sharing across independent DBMSs has become one of the most challenging issues for the decade. This is referred to as the heterogeneity problem in this paper.

The key factors which impede information sharing in heterogeneous databases are as follows:

\- the databases are designed and maintained in an uncoordinated way by independent organizations

\- they are implemented on different hardware and/or software, and are distributed among the nodes of computer networks

\- there are no common conventions for naming, describing, formatting, representing and structuring data. As a result, data conveying the same information contained in these data sources have different logical and physical representation and even different values [3].

Researchers in the area of heterogeneous databases have emphasized the importance of resolving the heterogeneity problem $[13,2,29]$ . Cases where straightforward mapping or data type conversions suffice have been studied in $[4,11]$ . Other papers have assumed the availability of additional data or constructs such as pointers $[23]$ or all possible spellings for names $[25]$ . The use of rules to resolve this problem was suggested in $[35]$ which used an informal expert systems approach to solve the heterogeneity problem. A subsequent paper $[30]$ used a similar approach to determine if a database can supply meaningful information to an application. However, modelling of uncertainty and resolution of conflicts are some of the areas not addressed in these papers.

The objective of our research is to develop a data model that will allow the users to query data stored in heterogeneous databases. In particular, we focus on the join query in this paper. The conventional joins (e.g., theta, natural, etc.) supported by the currently available systems are too syntactic to be useful in a heterogeneous environment. In this paper, we propose a probabilistic rule-based model which allows the users to specify arbitrarily complex rules to join and retrieve data from different databases. We use the Entity Join model that was presented in [8] for this purpose. From a historical perspective, the (deterministic) Entity join model was first introduced by Kent in [18]. This was extended to a probabilistic framework in [7]. In this paper, we extend it further to a semantically richer rule-based model.

Rules are used in this model to establish equivalence between attribute values, when the relationships between them are arbitrarily complex. Using the concept of semantic domain as defined in [30], we identify the “first order” condition two attributes need to satisfy to be meaningfully compared. We propose join rules to transform the attributes (when such transformations exist), in order to make them comparable. In addition to the first order condition, the attributes sometimes satisfy the stronger “second order” condition for compatibility. In such cases, simple inference rules can be used to convert heterogeneous attributes to mutually compatible ones which can be materialized and compared at a later time.

Rules help in reducing the heterogeneity among the data items to a large extent, but they depend on the availability of certain semantic information. In a heterogeneous environment, such information may not always be available. In such cases, the users often settle for approximations rather than not having any results at all. We use a probabilistic framework in this paper to model the uncertainty associated with such approximations.

We also address the problem of representing the values of mismatched attributes. We mentioned that data heterogeneity may cause different values to be assigned to the same data item. In such situations it is not easy to identify the true value of the attribute. We use probabilistic partial values to express the conflicting attribute values. We also demonstrate the effectiveness of this representation, both in capturing the uncertainty and in answering queries.

The advantages of our model over a conventional join are as follows:

\- it provides a unified treatment to the heterogeneity problem by combining the rule based approach with the probabilistic data model. While the rule based approach captures the data semantics, the probabilistic framework models the uncertainty and provides a formal measure of accuracy for the entity join.

\- currently, most identification conflicts are clerically resolved. In comparison, the proposed model reduces explicit user involvement in query evaluation and consequently reduces the response time.

\- it allows accounting for user preferences or data reliability, when representing mismatched attributes values using partial values.

\- there are a number of statistical and scientific applications (outlined in Section 3), where the user requires the probabilistic results of our model.

This paper is organized as follows. In Section 2, the data heterogeneity problem is discussed in detail. Some of the potential applications of the model are presented in Section 3. In Section 4, the conceptual framework for our model is introduced. The rule based probabilistic join model is developed in Section 5. The properties of join and inference rules are discussed in Section 6. In Section 7, the framework is further extended using probabilistic partial values to represent the values of mismatched attributes. The paper is concluded in Section 8 with a summary and directions for future research.

## 2. Data heterogeneity

In this section, we discuss various sources of data heterogeneity in databases. Some of the material presented in this section appeared in $[7]$ . We briefly repeat it here for the sake of completeness and to motivate the reader towards the subsequent treatment of this issue.

Applications often need information from various parts of a single database or from several databases. If the databases are independently managed, the same data is likely to be represented differently in these databases. Not only the values, but the semantics, underlying assumptions and the integrity rules may differ as well. We denote these problems associated with the incompatible representation of the data as the data heterogeneity problems. These problems have also been referred to in the literature as instance identification problems $[35]$ and hence, the terms instance identification and data heterogeneity are used interchangeably in this paper. We distinguish between two types of heterogeneity: structural and semantic.

## Structural heterogeneity

Structural heterogeneity occurs when the attributes are defined differently in different databases. Some of the sources of structural heterogeneity are:

Type mismatch: The same attribute may have incompatible type definitions in different databases. For example, social security number could be of type “character” in one database and “numeric” in another. Similarly, an attribute may be set-valued in one database and single-valued in another.

Formats: Different databases often use different formats for the same data element, e.g., date in day/month/year versus month/day/year.

Scale differences: Different databases use different scales to record the same information. For instance, inventory level may be expressed in terms of the number of items, or their weight (in tons) or their dollar value. Sometimes, these differences can lead to ambiguity and imprecision, e.g., if temperature is represented in a scale of four values {cold, cool, warm, hot} in one database and in degree Fahrenheit in another.

Granularity: Data elements representing measurements differ in granularity levels, e.g., sales per month or annual sales. This could also happen when two attributes get combined in an irreversible way.

## Semantic heterogeneity

Semantic heterogeneity occurs when similarly structured attributes take on different semantics and values in different databases. Some of the sources of semantic heterogeneity are as follows:

Synonyms: Different symbols or values used in different databases to represent the same data item. For example, the same person may be referred to by name, social security number or employee number in different databases.

Homonyms: Different data items sharing the same symbol or value in different databases. For example, a popular name like “John Smith” may identify many persons.

Codes: Codes are used for various reasons, such as saving storage space. Codes are often local to the databases, and therefore non-uniform even when referring to the same domain.

Incomplete Information: Missing and incomplete information is represented by null values in relational databases. While some databases allow nulls, others do not. Moreover, the meaning of nulls (e.g., unknown, not applicable, unavailable) varies among databases.

Recording Errors: These could be due to typographical mistakes or variations in measurement. Typing errors happen frequently with similar sounding names, e.g., “Smith”, “Schmidt” and “Smythe”.

Domain Evolution: This problem occurs when the semantics of values in a particular domain change over time in ways that are not amenable to applying simple mappings between the “old” and the “new” values. The difficulty arises because the values may remain the same but their interpretation may change over time.

Asynchronous Updates: These happen when data items, replicated in different databases, get updated at different points in time and become inconsistent. These are more likely if the data items are inherently time varying, such as a person's salary.

The sources of heterogeneity listed above are not meant to be exhaustive. Other cases of heterogeneity are discussed in $[13,2]$ . It is also possible to have combinations of different cases, like synonyms and recording errors, occurring at the same time which adds to the complexity of the problem. In some situations, heterogeneity is introduced deliberately to gain competitive advantage; sometimes it is due to a lack of information, e.g., a hospital may be unaware of the identifier assigned to a patient at another facility; or it could be due to a data entry error, e.g., a name being misspelled.

These complicate the heterogeneity resolution process, since no matter what the cause, the end effect appears to be the same.

The resolution of the heterogeneity depends on the identification of a mapping function between the different incompatible representations; and the probabilistic rule based model can be used in a couple of ways in this regard. Firstly, the rules provide a powerful, general purpose tool to model the mapping function, when such a function is identifiable. Secondly, for situations where the data values are randomly generated and no mapping can be identified, e.g., data entry errors, the probabilistic aspect of the model is utilized to account for the randomness. The model details are discussed in Section 4. In the next section, we present some of its potential applications.

## 3. Applications of the model

It is our observation that data heterogeneity problems occur in many settings and the proposed model can have numerous applications in business, social, biological and physical sciences. In this section, we list a number of examples which could benefit from this approach. These can be classified into exact and approximate depending on the application and the amount of semantic information available. In general, an exact join results in higher precision at higher cost compared to an approximate join.

## 3.1. Exact join

The model presented in this paper can be used in applications where the precision is crucial. Examples of such applications may be found in financial institutions like banks and accounting firms, in manufacturing and in various government agencies like Census Bureau and IRS. Typical usage may be in creating consolidated statements and balance sheets, preventing mortgage frauds, detecting tax evasions, and in identifying similarities between products of different vendors. Other applications include frame creation in U.S. census [10], coverage estimation in surveys [19], long term medical follow up studies in epidemiology [5], immigration control [9] and forensics [32]. These applications mostly prefer an exact response to their queries.

## 3.2. Approximate join

There are applications, e.g., in scientific and statistical computing, which require only an approximate response to their queries. In many other situations, the computational resources and the necessary semantic information for an exact response are not available. In such cases, an approximation presents a compromise between an expensive, exact response and not having any response at all. The following presents a way to classify approximate queries depending on the underlying problem one is trying to solve. These classes are as follows:

## Finding similar objects

In this class of application, the objective is to find other distinct objects from the same or different databases which have similar but not necessarily identical characteristics as the reference object. This is an identification problem as the names or the identification numbers of the objects being retrieved are not known in advance. So the retrieval is based on the similarity of other attributes between the reference and the retrieved objects. Applications in this category are: document matching [28], comparison of chemical properties [16], cluster analysis [22] and matched pair sampling [27].

## Classification by nearest neighbour

The construction of taxonomy is a fundamental undertaking in science. This class of application is an extension to the one discussed above. The objective is not only to find objects (or groups of objects) similar to the reference object but also to assign the reference object to a group based on these similarities. Examples belonging to this category can be found in biology $[31]$ and political science $[24]$ .

The model presented in this paper can be used by organizations to achieve competitive advantage through superior database management techniques. Higher precision in information retrieval involves higher cost. Our model provides sufficient flexibility to the users to strike a balance between cost and accuracy. Consequently, the techniques derived in this research can be built into a management decision support environment.

While the problem of data heterogeneity is likely to be more pronounced in a heterogeneous environment, it could also occur within a single database. For example, the data pertaining to the same object can be entered differently by different users in a single database. Our model can be effectively used in such a situation. The current commercial systems do not provide much safeguard against this situation. They mostly leave it up to the user and/or the database administrator to ensure that the data representation is consistent and standard across the database.

## 4. The framework

The concept of the instance-identification operator, the Entity join, was developed in [8]. We informally present the general characteristics of the model in this section. We also demonstrate how the instance identification capability of the model is enhanced by integrating it with rules. Formal definitions and modelling details are analyzed in the later sections.

Entity join represents a semantic approach to heterogeneity resolution in a federated environment. Conventional joins are always symbolic as opposed to semantic, where two tuples are joined if specified fields contain the same symbol $[18]$ . In a heterogeneous environment, when the relations being joined are from different databases, the symbolic comparison of the join attributes can inadvertently lead to wrong conclusions. For example, joining on codes, where a “1” signifies excellent in one database and poor in the other. The underlying issue here is that independent databases have many “standard practices” and hidden assumptions which are not captured by a symbolic join. These reasons led us to look for alternate ways to process queries for heterogeneous databases.

Rule based Entity join takes into account the attribute semantics while processing the query. It checks for compatibility between the relevant attributes and transforms the heterogeneous ones to a mutually compatible format so that they can be meaningfully compared. The effectiveness of the transformation however, is dependent on the semantic information provided by the individual databases.

Entity join can be exact or approximate depending on the application and the availability of semantic information. If sufficient information to resolve the heterogeneity is available, an exact join can be computed. On the other hand, if the necessary information is unavailable, posing an approximate query is often the only option. Thus, query processing in a heterogeneous environment involves: (i) resolution of heterogeneity, through the use of rules, and, (ii) accounting for any residual uncertainty using approximations. Both these issues are addressed below.

## 4.1. Rule based mapping

Rules can perform the dual function of resolving heterogeneity and providing the users the flexibility of formulating arbitrarily complex queries. In order to meaningfully compare two attributes, they have to be expressed in a mutually compatible format. This implies that either one or both the attributes will have to be converted before they can be compared. Rules can be used to perform this conversion and derive attributes that are compatible with each other.

The data conversion rules depend on the availability of the necessary semantic information (in the metadata) and the identification of appropriate mapping functions. The theory of mapping attributes values across databases (often referred to as establishing attribute equivalence) was originally presented in [21]. We extend this work further in this paper through the use of rules to model the mapping functions in a databases environment. Depending on the order of compatibility between the attributes being compared, different types of conversion rules are required. Inference rules are used if the data conversion has to be done without accessing the individual tuples of the relations being joined. For higher precision and more complicated queries, it might become necessary to access both relations simultaneously and the corresponding conversion rules are referred to as the join rules. While the Inference rules are easier to implement, the Join rules provide more power and flexibility to the user. We analyze these issues further in Section jrule, in the context of the formal model presented in the next section.

## 4.2. Modelling uncertainty

Rules help in reducing the heterogeneity among the data items to a large extent, but they depend on the availability of certain semantic information. In a heterogeneous environment, such information may not always be available. In such cases, the users often settle for approximations rather than not having any results at all. We use a probabilistic framework to model the uncertainty associated with such approximations.

The uncertainty occurs when an attribute of the same real world instance is assigned different values in different databases and there are no identifiable, deterministic mapping between these values. There are couple of reasons which can cause this to happen:

\- Random data entry errors can cause the same value to be different in different databases, and usually no mapping exists between a correct value and its erroneous version.

\- General lack of information or standardization between the participating databases can result in asynchronous updates, domain evolution or assignment of different identifiers to the same data instance in different databases. This creates overall data inconsistencies, even though the data may be correct with respect to each individual database. Since the data is being managed independently, there may not be a suitable mapping between the values in different databases.

In the absence of conversion rules, the values have to be compared symbolically as strings. If heterogeneity is present, this may result in some erroneous conclusions. We propose to improve accuracy and reduce the uncertainty by incorporating additional information in the join query. During the Entity join (in short, E-join), we consider not only the join attributes as in a regular join, but other attributes of the data items (being joined) that are common to the two relations.

The additional attributes are incorporated to the query in the form of added constraints to improve the chances of accurate instance identification. These constraints are similar to the user supplied join conditions, except that they are supplied by the DBMS. The idea behind this approach is that even if the keys are unavailable or incompatible, most of the other common attributes would match if two records describe the same real world instance. On the other hand, if the two records sharing the same key refer to two different real world instances, the other common attributes are less likely to match. Thus, by considering all common attributes, the probability of accurate identification is significantly improved.

Given the additional attributes and constraints, our focus in this paper is to determine if a result tuple satisfies the join conditions. This process may not be deterministic if the necessary semantic information is unavailable. Based on the available data, a tuple probability is assigned to each (concatenated) tuple, which measures the degree to which the tuple satisfies the join condition. This allows us to consider not only those tuples which satisfy all the conditions but also those which satisfy only a subset of them. The fewer the number of conditions satisfied by a tuple, the lower will be its tuple probability. In other words, tuple probability can be used to rank the tuples. This feature could be particularly useful for scientific and statistical applications, where the records being matched are often similar but not necessarily identical.

## 5. The entity join

This section presents the formal development of the rule based probabilistic join framework, which was outlined in the previous section. The basic concepts of the model are discussed here, the rule related issues are discussed further in Section 6. The comparison vector is the central construct of the E-join model. We define this vector later in this section and using it, derive of the tuple probability estimation formula.

## 5.1. Basic concepts

Let $r(R)$ and $r(S)$ be the two relations to be joined, where, R and S denote the schemas for the two relations respectively. Assume the join attribute to be $a_{J}$ , where $a_{J} \in R$ , S. Let the tuples of $r(R)$ be $r_{i}, i = 1, \ldots, K$ . Similarly, let the tuples of $r(S)$ be denoted by $s_{i}, i = 1, \ldots, L$ . Then M, a set containing the accurate result of joining $r(R)$ and $r(S)$ on $a_{J}$ , can be expressed as:

$$
\begin{array}{r l} \mathcal {M} & = r (R) \bowtie r (S) \\ & = r (R) \times r (S) \end{array}
$$

such that $r_i[a_J] \equiv s_j[a_J]$

The symbol “≡” is being used to indicate equivalence. It symbolizes the relationship the join attributes need to satisfy for two tuples to join. It can be replaced by any simple operator like equality, as in a symbolic join, or by a complex set of rules. This is necessary, because in a heterogeneous environment, the join attributes may not have the same symbols or values although they may be equivalent, i.e., may represent the same object in real life. The cross product:

$$
r (R) \times r (S) = \left\{\left(r _ {i}, s _ {j}\right): r _ {i} \in r (R), s _ {j} \in r (S), \forall i, j \right\}
$$

can now be expressed as the union of two disjoint sets:

$$
\mathcal {M} = \left\{\left(r _ {i}, s _ {j}\right): r _ {i} \left[ a _ {J} \right] \equiv s _ {j} \left[ a _ {J} \right]; r _ {i} \in r (R), s _ {j} \in r (S) \right\}
$$

$$
\mathcal {U}; = \left\{\left(r _ {i}, s _ {j}\right): r _ {i} \left[ a _ {J} \right] \neq s _ {j} \left[ a _ {J} \right]; r _ {i} \in r (R), s _ {j} \in r (S) \right\}
$$

Our ultimate objective is to estimate M and hence the result of the join. In the absence of semantic information, the symbolic matching of heterogeneous attributes can cause two types of errors:

1. for a given $i, j, r_{i}[a_{J}] \neq s_{j}[a_{J}]$ , but $(r_{i}, s_{j}) \in \mathcal{M}$ .

2. $r_i[a_J] = s_j[a_J]$ but $(r_i, s_j) \in \mathcal{U}$ ; for a particular $i, j$ pair.

By using mapping rules (if available) and comparing other common attributes, the probability of such errors can be reduced.

It may be noted that when there are no conversion rules (unavailable or unnecessary) such that the join attributes are compared symbolically and there are no additional information in the form of attributes other than the join attribute, the E-join defaults to the conventional join. A conventional join is thus a trivial case of the E-join. Unless specifically mentioned, all future reference to the E-join will refer to the non-trivial case.

Example 1. The Census Bureau wants to eliminate duplicates from two lists, UNV and DMV that it has received from a local university and the Department of Motor Vehicles respectively. The entries in the duplicate free list will be included in the census data. This query requires a join between the Tables, UNV and DMV. Tables 1 and 2 are the schemas of the two tables containing a sample record each. Note that the identifiers (in bold type) used in the two tables are different.

Table 1

<table><tr><td>License Number</td><td>Last name</td><td>First name</td><td>Address</td><td>Zip</td><td>Birth date</td><td>Sex</td><td>Height</td><td>Weight</td><td>Date of expiration</td></tr><tr><td>1234</td><td>Smith</td><td>John</td><td>New York</td><td>10006</td><td>5/11/62</td><td>M</td><td>5.9</td><td>160</td><td>7/12/92</td></tr></table>

Suppose that the displayed records belong to the same individual so ideally these should join. But an equi-join on the last name – first name combination will not be able to match these as the first name is misspelled as “Jorn” in UNV. A join on last name alone will not be very useful either as the DMV tuple will get joined to all UNV tuples which have “Smith” as the last name. So, we need to perform an approximate E-join in this case. (The example is continued in Section 6.)

## 5.2. The comparison vector

In order to E-join $r(R)$ and $r(S)$ , a pair of tuples is selected, one from each relation, and all the join conditions are evaluated. The result of this evaluation is stored in a Comparison Vector which we define below. This process is repeated for all $K \times L$ pairs of tuples.

Let n be the total number of join conditions to be evaluated, including those that are supplied by the system. Let t be a concatenated tuple, such that $t = (r_i, s_j)$ : $r_i \in r(R)$ , $s_j \in r(S)$ . Then, the comparison vector is defined as $\gamma(t) = \{\gamma_1(t), \gamma_2(t), \ldots, \gamma n(t)\}$ , where the number of components of $\gamma(t)$ is equal to the number of join conditions [15,33]. (We denote vectors in bold type.) The result of the comparison of the two tuples $r_i$ and $s_j$ is stored in this vector.

$$
\begin{array}{l l} \gamma_ {1} (r _ {i}, s _ {k}) = 1 & \text {if r_{i} [a_{1} ]\equiv s_{k} [a_{1} ]} \\ = 0 & \text {otherwise} \\ \gamma_ {2} (r _ {i}, s _ {k}) = 1 & \text {if r_{i} [a_{2} ]\equiv s_{k} [a_{2} ]} \\ = 0 & \text {otherwise} \\ \vdots \\ \gamma_ {n} (r _ {i}, s _ {k}) = 1 & \text {if r_{i} [a_{n} ]\equiv s_{k} [a_{n} ]} \\ = 0 & \text {otherwise} \end{array}
$$

The interesting feature of the vector is that it can be used in conjunction with rules. Each component of the vector is associated with a join condition and an equivalence operator can be used in all of them. This provides considerable flexibility in query formulation, particularly if the join condition requires a complex set of rules to be represented. The vector also keeps track of the conditions that a tuple has satisfied. This becomes particularly important, if the user wants to retrieve tuples which partially satisfied the join conditions. We define below the tuple probability in terms of the comparison vector.

## 5.3. Tuple probability

Tuple probability measures the appropriateness of joining two tuples given the information available in the comparison vector; higher the probability, the more appropriate is the join. Being a numeric measure, it can also be used to rank the joined tuples. Each of the $K \times L$ concatenated tuples is assigned a tuple probability.

Table 2
The UNV table

<table><tr><td>Registration Number</td><td>Last name</td><td>First name</td><td>Address</td><td>Zip</td><td>Birth date</td><td>Sex</td><td>Nationality</td><td>Major field</td></tr><tr><td>1064</td><td>Smith</td><td>Jorn</td><td>New York</td><td>10006</td><td>5/11/62</td><td>M</td><td>US</td><td>Comp Sc.</td></tr></table>

Definition 1. Tuple Probability. Given the comparison vector, the conditional probability that the corresponding tuple belongs to M. Formally,

$$
p _ {t u p l e} (t) = \operatorname * {P r} \left\{t \in \mathcal {M} \mid \gamma (t) \right\}.
$$

We say that $t \in M$ with certainty, when we have a “perfect match”, i.e., the comparison vector is a unit vector. Mathematically,

$$
\operatorname * {P r} \{t \in \mathcal {M} \mid \gamma (t) = 1 \} = 1.
$$

Similarly, we say that $t \notin M$ with certainty, when we have a “perfect mismatch”, i.e., the comparison vector is zero. Formally,

$$
\operatorname * {P r} \{t \in \mathcal {M} \mid \gamma (t) = 0 \} = 0.
$$

In order to estimate $p_{tuple}(t)$ , we use the Bayes' Theorem.

$$
\begin{array}{r l} p _ {t u p l e} (t) & = \operatorname * {P r} \{t \in \mathcal {M} \mid \gamma (t) \} \\ & = \frac {\operatorname * {P r} [ t \in \mathcal {M} , \gamma (t) ]}{\operatorname * {P r} [ \gamma (t) ]} \\ & = \frac {\operatorname * {P r} [ \gamma (t) \mid t \in \mathcal {M} ] \cdot \operatorname * {P r} [ t \in \mathcal {M} ]}{\operatorname * {P r} [ \gamma (t) ]} \end{array}
$$

Thus, to evaluate the tuple probability, we need to estimate the two unconditional probabilities $\Pr\{\gamma(t)\}$ and $\Pr\{t\in\mathcal{M}\}$ and a conditional one, $\Pr\{\gamma(t)\mid t\in\mathcal{M}\}$ . A scheme to estimate these probabilities is given in Appendix A.

## 6. Rule based comparisons

The “≡” was introduced in the previous section to represent conditions the attributes need to satisfy for their corresponding tuples to join. We now illustrate how the rules can be used to model these conditions.

A rule is an If-Then statement that applies constraints to some existing data and derives new data or triggers an action, when the If-side is satisfied. The If-side is called the antecedent, and the Then-side is called consequent. The constraints are specified in the antecedent and the actions are stated in the consequent. We will occasionally refer to the antecedent as condition and the consequent as the result. In general, we distinguish between data rules and action rules. The former directly affect existing data or derive new data and the latter activate DBMS commands or procedures such as abort a transaction or print a report.

An attribute is considered user defined if its value is explicitly supplied by the user. The term user is used in a broad sense to include the database administrator, system analysts and the end users. An attribute is considered derived if its value is not explicitly user supplied but obtained by the action of certain rules.

In a heterogeneous environment, the same attribute is often represented differently in different databases. Meaningful comparison of such attributes has to be done in two steps:

(1) conversion of the attributes(s) to a mutually compatible representation, and,

(2) comparison of the values according to the user specifications.

Conversion rules are used to transform the heterogeneous attribute(s) into a mutually compatible form. These rely on the availability of two types of information:

(1) the knowledge of the semantic domain of the heterogeneous attributes (defined below), and,

(2) a mapping function that can convert an attribute from one semantic format into another.

There could be more than one mapping function, as a typical data item may be represented in several different formats. Depending on the attribute semantics and the available mapping options, the rules for the attribute conversion transform the attributes into a mutually compatible format for the subsequent comparison step. It should be noted that an inverse of every mapping may not exist. For instance, monthly sales can be easily mapped to annual sales, but the reverse may not be possible. The process of formulating conversion rules is described in detail in the rest of the section, following the definition of semantic domain.

The semantic domain of an attribute A is the set of attributes used to define the semantics of A. It is denoted as:

$$
\operatorname{sem} (A) = \left\{D _ {1}, D _ {2}, \dots , D _ {m} \right\}
$$

where each $D_{i}$ is an attribute. These attributes represent the facts about data representation that are assumed and implicitly enforced in each database in order to provide context to each data item. For each $a \in A$ , the semantics of that value can be defined in terms of the semantic domain as:

$$
\operatorname{sem} (a) = \left\{d _ {1}, d _ {2}, \dots , d _ {m} \right\}
$$

where $d_{i} \in domain(D_{i})$ . As an example, we may think of the semantic domain of an attribute, inventory, in terms of units, i.e., $sem(inventory) = \{units\}$ , where, units = {dollar, tons, number}.

The mapping functions and semantic domain attributes (henceforth, referred to as semantic attributes) like $D_{i}$ need to be identified during the schema integration. We assume that the information is stored as rules in the metadata and is available to all the participating databases. The rationale behind this assumption is that the autonomous databases are far less likely to change their data (during integration) than to include additional information in their metadata. Moreover, the cardinalities of the semantic attributes are often much smaller than the user defined ones, i.e., $|D_{i}| \ll |A|$ , and the same value of the semantic attribute applies to a large number of tuples. This information can be succinctly stored as a rule, rather than repeating the same value for a large number of tuples.

The concept of semantic domain and idea of capturing attribute semantics in the metadata to supply meaningful information to applications was initially suggested in $[30]$ . In the next section, we demonstrate how semantic domain information can be used in our model for data conversion and subsequent processing of the join.

## 6.1. Join rules

Suppose that attribute A is being compared to attribute B and they are mutually incompatible, i.e., $\text{sem}(A) \neq \text{sem}(B)$ . In order to compare the two attributes, A needs to be mapped to $A'$ , where $sem(A') = sem(B)$ . We denote this as the first order condition for compatibility. Two attributes cannot be compared if they do not satisfy the first order condition for compatibility.

When an attribute is mapped from one format to another, its values as well as the values of its semantic attributes change. The join rule performs the dual function of data conversion and semantic attribute assignment. If a function mapping A to an attribute like $A'$ exists, then Join rules can be used to derive such an attribute, so that it can be compared to B.

The first order condition guarantees that the two attributes will have the same semantic domain. For example, the semantic domain of “inventory” will be “units” in both the databases. However, the first order condition does not guarantee that the values of the semantic attributes would be equal. Thus, different inventory items in the same relation can have different units, like dollar or ton.

This creates a conversion problem as the same item in A can be converted to several different formats, e.g., an inventory item expressed in numbers in A could be converted to either dollars or tons, and it may not be obvious as to which one of these would be applicable. In other words, the mapping function cannot effectively derive $A'$ solely within the context of one database. If B expresses a certain inventory item in dollars, then the same item should be expressed in dollars in $A'$ for the two values to be compared. This means the tuples in two relations have to be accessed simultaneously. Once the values are converted to a mutually compatible format, they are checked against the user supplied join condition. The Join rules presented below do not actually derive any attribute such as $A'$ , they perform the data conversion and the constraint satisfaction in a single step in an effort to cut down the I/O cost.

We have mentioned that the information about the values of semantic attributes can be stored in the metadata. Let us assume that A is an attribute of relation $r(R)$ to be converted to $A'$ , and a is one of its values. Also, let

$$
\operatorname{sem} (A) = \left\{D _ {1}, D _ {2}, \dots , D _ {m} \right\}
$$

Using rules, the semantic information about a can expressed as:

$$
\text {   If   } C _ {r} (r [ X _ {1} ]) \wedge \dots \wedge C _ {r} (r [ X _ {q} ])
$$

Then $(D_{1} = d_{1})\wedge \ldots \wedge (D_{m} = d_{m})$

where tuple $r \in r(R)$ , $X_{1}, \ldots, X_{q}$ are other attributes of R and $C_{r}(r[X_{i}])$ denotes a constraint defined on attribute $X_{i}$ . A similar condition for a value b of B would be:

If $C_s(s[Y_1]) \wedge \ldots \wedge C_s(s[Y_t])$

$$
\text { Then } \left(E _ {1} = e _ {1}\right) \wedge \dots \wedge \left(E _ {n} = e _ {n}\right)
$$

where $\text{sem}(B)=\{E_{1}, E_{2}, \ldots, E_{n}\}$ , tuple $s \in r(S)$ , $Y_{1}, \ldots, Y_{t} \in S$ and $C_{s}(s[Y_{i}])$ denotes a constraint on attribute $Y_{i}$ .

For $A'$ to be compared to B, the following first order condition must hold:

$$
\operatorname{sem} (A ^ {\prime}) = \operatorname{sem} (B)
$$

where $\text{sem}(A') = \{F_1, F_2, \ldots, F_n\}$ .

In addition to the domain semantics, we require the knowledge about the mapping function. This may be provided by the user, but is more likely to be generated during schema integration and maintained in the metadata by the database administrator. Let f denote one such (conditional) mapping function, expressed as a rule:

$$
\text { If } \quad \mathcal {M} (r [ X _ {1} ]) \wedge \dots \wedge \mathcal {M} (r [ X _ {m} ])
$$

$$
\wedge \left(D _ {1} = d _ {1}\right) \wedge \dots \left(D _ {m} = d _ {m}\right)
$$

$$
\begin{array}{r l} \text { Then } & r [ A ^ {\prime} ] = f (r [ A ]) \\ & \wedge (F _ {1} = f _ {1}) \wedge (F _ {n} = f _ {n}) \end{array}
$$

Here, $\mathcal{M}(r[X_{i}])$ denotes any additional mapping constraint that may be defined on the attributes. (If there are no constraints of the type $\mathcal{M}(\cdot)$ , then we get an unconditional mapping function. These are of particular interest when used with Inference rules, as demonstrated later in the section.) Then, the Join rule can be defined as follows:

$$
\text { If } \quad J (r [ X _ {1} ]) \wedge \dots \wedge J (r [ X _ {m} ])
$$

$$
\wedge (D _ {1} = d _ {1}) \wedge \dots (D _ {m} = d _ {m})
$$

$$
\wedge J (s [ Y _ {1} ]) \wedge \dots \wedge J (s [ Y _ {t} ])
$$

$$
\wedge \left(E _ {1} = f _ {1}\right) \wedge \dots \wedge \left(E _ {n} = f _ {n}\right)
$$

$$
\wedge s [ B ] \theta f (r [ A ])
$$

Then $r[A] \equiv s[B]$

Here, $\theta$ represents any user specified operator, such as $= ,\neq , < , >$ or their legal combinations. $J(\cdot)$ denotes a join constraint on the attribute on which it is defined. If the constraints on attribute $X_{i}$ in one database imply the constraints on $Y_{i}$ in the other database, then the Join rule imposes the stronger constraint on $Y_{i}$ . In other words, if $C_r(r[X_i]) \to C_s(s[Y_i])$ then, $J(s[Y_i]) = C_r(s[Y_i])$ and $J(r[X_i]) = C_r(r[X_i])$ . Join constraints can be derived in similar manner if the implication holds in the opposite direction (from $Y_{i}$ to $X_{i}$ ). These constraints ensure that the tuples of both relations satisfy the all the conditions of the join, including the hidden ones. We illustrate the use of the Join rule in the following example.

Example 2. We want to match the ratings of Chinese restaurants obtained from different sources (New York Times – NYT and Restaurant Guide – RG). $r(NYT)$ is solely for Chinese restaurants, whereas $r(RG)$ contains data about all types of restaurants and hence has an attribute, type, specifying the type of cuisine. Moreover, the relations use different systems to rank the restaurants.

Let the semantic domain of rating in $r(R)$ be $\{source_{1}, rest_{type}\}$ . So for all tuples $r \in r(R)$ , $source_{1} = "NYT"$ and $rest_{type} = "Chinese"$ . Since $r(S)$ contains an user-defined attribute, type, the semantic domain of rating in $r(S)$ is simply $\{source_{2}\}$ , which takes on a value, "RG", for all tuples $s \in r(S)$ . In order to compare rating in the two databases, their semantic domain must be identical. So we need to map r[rating] to r[rating'], where $sem(r[rating']) = sem(s[rating])$ , using the following mapping rule:

If source $_{1}$ = NYT ∧ rest type = Chinese

$$
\begin{array}{r l} \wedge \text { Then } & r [ r a t i n g ^ {\prime} ] = 1. 3 3 ^ {*} r [ r a t i n g ] \\ & \wedge s o u r c e _ {2} = R G \end{array}
$$

There is only one implication that needs to be accounted for in this example. This can be done using a single constraint which will ensure that the tuples of $r(R)$ are only compared to the tuples of type “Chinese” in $r(S)$ . The complete Join rule is given below:

$$
\text { If } \quad s o u r c e _ {1} = N Y T \wedge r e s t _ {t y p e} = C h i n e s e
$$

$\wedge$ source $_{2}$ = RG $\wedge$ s[ type] = Chinese

$$
\wedge s [ r a t i n g ] = 1. 3 3 ^ {*} r [ r a t i n g ]
$$

Then $r$ [rating] $\equiv s$ [rating]

## 6.2. Inference rule

Join rules introduce considerable semantics into joins. However, the numerous conditions in the antecedent and simultaneous access to the tuples being joined could make the join processing slow and expensive. In such situations, the users could opt for an approximation, where the conversion can be achieved primarily within one database, using only a limited amount of semantic information from the other database. The conversion rule corresponding to this type of data conversion is denoted as the inference rule. (Under certain strict semantic conditions, inference rules can also yield precise results.)

Using the same notation as before, let us assume that attribute A needs to be compared to B, where $sem(A) \neq sem(B)$ . In order to satisfy the first order condition, let us further assume that A can be mapped to $A'$ , where $sem(A') = sem(B)$ . A semantically precise comparison would have required the use of Join rules, but due to resource constraints, the user wishes to approximate it using Inference rules.

The Inference rule converts A to $A'$ simply using the semantic domain information about B and the mapping function. As there might be a delay between the derivation of $A'$ and its comparison with B, $A'$ values may be materialized. Note that unlike Join rules, data conversion and comparison steps are performed separately and the semantic constraints used by Inference rules in data derivation are not carried forward to the subsequent comparison step. $A'$ and B are compared symbolically and the resulting imprecision, if any, is reflected in the tuple probability.

Assuming that the semantic information about the attributes and the mapping functions are represented in the same way as before, the Inference rule takes the following form:

$$
\begin{array}{l} \text {If} \quad J (r [ X _ {1} ]) \wedge \dots \wedge J (r [ X _ {m} ]) \\ \qquad \wedge (D _ {1} = d _ {1}) \wedge \dots (D _ {m} = d _ {m}) \\ \qquad \wedge (E _ {1} = f _ {1}) \wedge \dots \wedge (E _ {n} = f _ {n}) \end{array}
$$

$$
\text { Then } \quad r [ A ^ {\prime} ] = f (r [ A ])
$$

Since the tuples of $r(S)$ are not available during the data conversion, we can no longer impose constraints on the attributes of relation S. The possible error resulting from this can be best demonstrated using the example of Chinese restaurants.

Example 2. (Continued) Using an Inference rule, rating values of $r(R)$ can easily be converted to a format semantically compatible to the rating in $r(S)$ . However, once the conversion is completed, the fact that $r(R)$ only contains data about the Chinese restaurants will be lost. During the subsequent symbolic comparison, rating values of Chinese restaurants might match the rating values of non-Chinese restaurants, which could lead to wrong conclusions unless such anomalies are detected and eliminated by the probabilistic model. (The tuple probability would be low if no attribute other than the rating match. However, the accuracy of the probabilistic approach can be guaranteed only in a statistical sense.)☐

Before concluding the section, we would like to discuss the special case when the Inference rules guarantee precise results. We have already stated that in order to compare two attributes, A and B, they must satisfy the first order condition of compatibility. To guarantee precision when using Inference rules, the following two conditions need to hold:

(1) the antecedent of the rules assigning values to the semantic attributes of $A$ and $B$ are empty, and,

(2) the relevant mapping functions should be unconditional.

We denote these as the second order conditions for compatibility. In other words, if there are no implicit assumptions regarding the individual values of an attribute A, it can be converted to an equivalent format $A'$ (which is compatible to B) without simultaneously accessing the tuples of both relations. No loss of information occurs in this case.

Due to the second order conditions, the semantic information about A and B can be stated as:

$$
\begin{array}{l l} \text {sem} (a _ {i}) = \text {sem} (a _ {j}) & a _ {i}, a _ {j} \in A, i \neq j \\ \text {sem} (b _ {i}) = \text {sem} (b _ {j}) & b _ {i}, b _ {j} \in B, i \neq j \end{array}
$$

that is, all attribute values of A and B will have the same values for their respective semantic attributes. The Inference rule simplifies to:

$$
\text { If } \quad (E _ {1} = f _ {1}) \wedge \dots \wedge (E _ {n} = f _ {n})
$$

$$
\text { Then } \quad r [ A ^ {\prime} ] = f (r [ A ])
$$

If both the first and the second order conditions hold and the necessary conversion function is available, then A can be mapped to $A'$ with no loss of information without accessing the tuples of relation $r(S)$ .

## 7. Representation of mismatched attributes

The tuples produced by E-join can be categorized into two classes: (a) tuples in which all common attributes match, and (b) those in which some of the common attributes did not match. These two classes are easy to distinguish. The former will have a unity comparison vector, while the latter will have some the vector components zero.

The tuples in which all the attributes match do not pose any problems. Each attribute has only one possible value and so, the result of the E-join query can be presented in any format desired by the user. Typically, this would be the format used in the database from which the query was issued. Joined tuples in which one or more common attributes do not match pose a difficult representation problem. The problem arises because it is not easy to identify between the two conflicting values, the “true” value of the attribute. For instance, when a person’s salary is stated as 40k in one database and 50k in another, it is not obvious as to which one of these should be accepted as correct.

One way to address this problem is to accept the most recent value as the true value of the attribute. The difficulty with this approach is that the most recent value may not necessarily be correct. Also, the approach requires that individual attributes in each tuple be time stamped. Simply recording the last update time for the tuple is not adequate to obtain the update times of individual attributes. Secondly, the time stamping procedure will affect the local query processing which may be considered as a violation of the autonomy.

We propose the use of partial values for representing the values of mismatched attributes. This approach has several advantages over the time stamping procedure. First of all, it does not make the assumption that a value recorded on a later date is necessarily more accurate. Secondly, it allows us to retain both the mismatched values (as partial values) instead of discarding one prematurely. This could be crucial, as often the users are interested to know how close the two mismatched values were. Finally, this approach takes into account the preference of the users or the reliability of the data, particularly when such information can be quantified. For example, the user could specify that “Age” in relation 1 is five times more reliable than that in relation 2. Next we introduce some of the basic concepts and our definition of partial value.

## 7.1. Partial values

When an attribute cannot be mapped to a single definite value, we need to use a set of partial values. Partial values constitute a finite set of possible values such that the “true” or “real” value of the attribute is exactly one of the values in the set.

Partial values were introduced for the resolution of domain mismatch problems in $[14]$ where a one-to-many mapping between two attributes resulted in partial values. This approach was further extended in $[34]$ by combining the ideas of partial values with the probabilistic data model proposed by $[1]$ .

We would like to point out that partial value and its probabilistic extension is used in a different context in this paper and consequently, our interpretations and definitions are different from those suggested in the earlier papers.

Definition 2. Partial Value. Let A be an attribute and the set, $A(\eta) = \{\eta_{1}, \eta_{2}, \ldots, \eta_{n}\}$ be such that $\eta_{j} \in Dom(A)\forall j = 1, \ldots, n$ . Then each $\eta_{j}$ represents a partial value of attribute A.

We use $Dom(A)$ to indicate the domain of attribute A. All possible candidates for the true value of A must belong to the domain of A.

The cardinality of a partial value set is defined as $|A(\eta)|$ . When the cardinality of a partial value set is one, that is, when there exists only one possible value, say d, then the partial value $\{d\}$ is called a definite value. A partial value set with cardinality greater than one is referred to as proper partial value.

Partial values are used in our framework to represent mismatched attribute values for joined tuples. Every mismatched attribute has its corresponding comparison vector component zero. Consider any pair of tuples concatenated as the result of E-join. Any attribute which has its corresponding comparison vector component zero will need to have partial values assigned to it. The cardinality of the partial value set would be two; the two elements being the two mismatched attribute values obtained from the two tuples being joined. The common attributes which match and all other attributes would have definite values.

Example 1. (Continued) The matching of the two tuples, r and s, resulted in a zero in the first name component in the comparison vector. As a result, the value of the first name in the joined tuple will be the partial value set, {John, Jorn}. Table 3 shows only the attributes relevant to the join. □

Table 3 implicitly assumes both the partial values to be equally “true”. In other words, it is equally likely that the value of attribute A is $\eta_{1}$ or $\eta_{2}$ . However, there could be situations where the data in one relation is more reliable than the data in the other, thereby making the corresponding partial value more likely to be the “true” value of the attribute. In the next section, we demonstrate how probabilistic partial values can be used to model this situation.

Table 3  
Table containing partial valued attributes

<table><tr><td>Rec. number</td><td>Last name</td><td>First name</td><td>Address</td><td>Zip</td><td>Birth date</td><td>Sex</td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $r \times s$ </td><td>Smith</td><td>[John, Jorn]</td><td>New York</td><td>10006</td><td>5/11/62</td><td>M</td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 7.2. Probabilistic partial values

Definition 3. Probabilistic Partial Value. Let A be an attribute and $A(\xi)=\{\eta_{1}^{p_{1}},\eta_{2}^{p_{2}},\ldots,\eta_{n}^{p_{n}}\}$ be such that $\eta_{j}$ is a partial value of attribute A, $p_{j}\neq0\forall j=1,\ldots,n$ and $\sum_{j=1}^{n}p_{j}=1$ . If we denote $\eta_{j}^{p_{j}}=\xi_{j}$ , then each $\xi_{j}$ represents a probabilistic partial value of attribute A.

A definite value d can be regarded as a probabilistic partial value $[d^{1}]$ and vice versa.

When partial values are equally likely to be true, the probabilities are uniformly distributed on them. Thus, there will be a probability 1/n associated with n partial values. For example, the mismatched first names can be written as $[John^{1/2}, Jorn^{1/2}]$ .

The main strength of probabilistic partial values is their capability to model user preferences and/or reliability of the data. Weights indicating the reliability of the data, are assigned by the user to the common attributes in each table. Larger the weight, greater is the reliability. For example, let $w_{i}^{R}$ be the weight assigned to attribute $A_{i}$ in relation $r(R)$ and $w_{i}^{S}$ be the weight assigned to the same attribute in $r(S)$ . If $w_{i}^{R} > w_{i}^{S}$ then the attribute $A_{i}$ values in $r(R)$ are more reliable than those in $r(S)$ . Users can assign a weight to the entire relation instead of assigning it to individual attributes. Similarly, weights may be assigned to some attributes while others may be left unspecified, in which case, the unspecified attributes will acquire the weight assigned to the relation. In case there is insufficient information to assign weights to the table and/or to individual attributes, the attributes are considered equally reliable.

The weights are combined with the partial values in a straightforward way. Consider an attribute $A_{i}$ common to two tables $r(R)$ and $r(S)$ . Let $w_{i}^{R}$ and $w_{i}^{S}$ be the weights assigned to the attribute in the two tables. If $r[A]=\eta_{1}$ and $s[A]=\eta_{2}$ and $p_{j}$ is the probability associated with $\eta_{j}$ for j=1, 2, then

$$
p _ {1} = \frac {w _ {i} ^ {R}}{w _ {i} ^ {R} + w _ {i} ^ {S}} \quad \text { and } \quad p _ {2} = \frac {w _ {i} ^ {S}}{w _ {i} ^ {R} + w _ {i} ^ {S}}
$$

Example 1. (Continued) Suppose that the user specifies that the data in the DMV table is four times as reliable than that in UNV except for the address attribute which is only twice as reliable. This results in the two sets of weights, shown in Table 4.

Table 4
Attribute weights

<table><tr><td>Table name</td><td>Last name</td><td>First name</td><td>Address</td><td>Zip</td><td>Birth date</td><td>Sex</td></tr><tr><td>DMV</td><td>4</td><td>4</td><td>2</td><td>4</td><td>4</td><td>4</td></tr><tr><td>UNV</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

The joining of tuples r and s will result in the creation of partial values for the attribute First Name. The probability associated with each partial value is shown in Table 5.

## 7.3. The extended operators

It was mentioned earlier that our definition of partial value is different from those proposed in literature $[14,34]$ . Despite the difference, the extended relational operators defined in $[34]$ can be applied to the partial values developed in this paper. This can be done by modifying the probability calculations to incorporate the contribution of the tuple probability. These extended relational operators can be used for manipulating relations containing probabilistic partial values. We present a brief discussion of the extended operators below. We then demonstrate how the probability calculations can be adjusted in context of extended selection and projection. Other operators can be adjusted in like manner.

The extended operators for manipulating relations were studied in [34]. These operators are similar to the conventional operators, e.g. [12], except that the attributes on which they are defined may contain probabilistic partial values as opposed to definite ones.

Table 5  
Probabilistic partial valued attributes

<table><tr><td>Rec. number</td><td>Last name</td><td>First name</td><td>Address</td><td>Zip</td><td>Birth date</td><td>Sex</td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $r \times s$ </td><td>Smith</td><td>[John $^{4/5}$ , Jorn $^{1/5}$ ]</td><td>New York</td><td>10006</td><td>5/11/62</td><td>M</td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The partial values affect the query processing in two ways. Firstly, the operators need to be defined on a set rather than a single value. This is accomplished in a simple way. Consider a selection condition defined on a probabilistic partial valued attribute A. The condition is considered to be satisfied if there is at least one value $\eta \in A(\eta)$ that satisfies it. Of course, for the tuple to be selected, other conditions specified by the user have to be satisfied as well.

Secondly, the conventional and the extended query processing differ because of the probabilities. Satisfying a query condition using probabilistic partial values introduces a degree of disbelief in the result. If there are multiple conditions, then the uncertainty resulting from each individual condition have to be considered. A systematic way to combine these probabilities are presented in [34]. This computation scheme is given below for selection and projection queries.

Selection

Let $p_{att}(t)$ be the probability contributed by the partial valued attributes when selection conditions are applied to tuple t. In other words, it is the probability that tuple t satisfies the selection conditions. Let P be any selection predicate and $r[A]$ , $r[A_1]$ and $r[A_2]$ be partial valued attributes of a relation $r(R)$ . The selection predicate can be of various forms, e.g., conjunction or disjunction of two other predicates, or comparison of an attribute with a constant or another attribute. Given below is the scheme to calculate $p_{att}(t)$ for each of these cases:

$$
\begin{array}{l l} P: - & P \vee P \left\{p _ {a t t} (t) = \max (1, 3); \right\} \\ | & P \wedge P \left\{p _ {a t t} (t) = 1 \times 3; \right\} \\ | & \neg P \left\{p _ {a t t} (t) = 1 - 3; \right\} \\ | & r [ A ] \theta C o n s t a n t \left\{p _ {a t t} (t) \right. \\ = & \sum_ {(\forall a \in 1) (a \theta 3)} p r o b (a); \Bigg \} \end{array}
$$

$$
\begin{array}{l} \mid r [ A _ {1} ] \theta r [ A _ {2} ] \left\{p _ {a t t} (t) \right. \\ = \sum_ {(\forall a \in 1) (\forall b \in 3) (a \theta b)} [ p r o b (a) \times p r o b (b) ]; \end{array}
$$

Note that \$i is used to represent the values associated with the ith right hand side symbol. For instance, in the first line of this grammar, P:-P ∨ P, \$1 is P, \$2 is ∨ and ∨ \$3 is p. θ is any operator of the form >, < or = or their valid combinations.

## Projection

The projection for a probabilistic partial relation is the same as the conventional projection.

## 7.4. Probability adjustments

Every tuple in E-join result has a tuple probability assigned to it. This can be interpreted as the probability that an E-joined tuple, t, rightly belongs to the result of an E-join query. A selection operation (followed by E-join) involving partial valued attributes introduces additional uncertainty. This is because the true value of such attributes cannot be uniquely determined.

Under some situations, selection and E-join may be considered independent. However, this assumption does not hold in this model because of the way E-join is evaluated. E-join involves the comparison of common attributes. The tuple probability is likely to be less than one, if some of the common attributes do not match. Partial values are used to represent the values of mismatched attributes. Since the partial values are proper, the probabilities associated with them will be less than one. Thus, a non trivial dependency exists between the selection of common attributes and the join. As a result, the combined probability of selection and E-join cannot be obtained without statistical analysis on the real data. We provide below the upper and lower bounds to this probability. This analysis is not necessary if selection involves definite valued attributes.

Let $p_{att}(t)$ be the probability contributed by the partial valued attributes when selection conditions are applied to tuple t. Let $p_{tuple}(t)$ be the probability associated with E-join. Then the overall probability $p(t)$ , associated with select-E-join operation can be nontrivially bounded as shown below.

Lemma 1

$$
\begin{array}{r l} & \max \left\{0, p _ {a t t} (t) + p _ {t u p l e} (t) - 1 \right\} \\ & \leqslant p (t) \leqslant \min \left\{p _ {a t t} (t), p _ {t u p l e} (t) \right\} \end{array}
$$

Proof. See Appendix B.

This result has been derived in the context of selection and E- join. It is trivial to extend it to the case of projection because $p_{att}(t)=1$ for pure projection operation [34]. This gives us the following corollary.

Corollary 1. The bounds derived in Lemma 1 applies to the overall probability associated with select-project-E-join queries.

We conclude the section with a short example on probability calculation.

Example 1. (Continued) Assume that the tuple probability for tuple $t = (r \times s)$ is given as, $p_{tuple}(t) = 1/2$ . Further, the tuple has been retrieved by the following query:

$$
\sigma_ {(f i r s t n a m e = J o h n) \wedge (l a s t n a m e = S m i t h)} (D M V E - j o i n U M V)
$$

Using the data in Table 5 and the formula in Section 7.3, $p_{att}(t) = 4/5$ . Using Lemma 1, the overall probability to be assigned to this tuple is bounded by the interval: $\max\{0, \frac{4}{5} + \frac{1}{2} - 1\} = \frac{3}{10}$ , and $\min\{\frac{4}{5}, \frac{1}{2}\} = \frac{1}{2}$ .

## 8. Conclusions and future research

Due to advances in networking and the increased value of information, organizations need the capability to share and manipulate data across heterogeneous databases. Data management becomes a complicated problem in a heterogeneous environment because the databases are independently managed. The same attribute can have conflicting semantics and values, and it may be updated at different points in time in different databases.

In this paper, we combined rules with a probabilistic framework to resolve the data heterogeneity problem. We introduced the Entity join model to identify and join records across databases. Rules were used to establish complex equivalence relationships between attribute values. We identified the first order condition two attributes need to satisfy to be meaningfully compared and proposed join rules to transform the attributes (when such transformations exist), in order to make them comparable. If the attributes satisfy the stronger second order compatibility condition, simple inference rules can be used to convert heterogeneous attributes into mutually compatible ones which can be materialized and compared at a later time.

Certain amount of uncertainty is associated with this E-join model due to the possibility of wrong matches. The probabilistic framework provides a formal measure of this uncertainty by assigning tuple probability to each pair of tuples. The tuple probability can be interpreted as the appropriateness of joining a pair of tuple and can be used to eliminate poorly matched tuples.

Representing the values of mismatched attributes presents a difficult problem. This is because the true value of the attribute cannot be identified from the various conflicting values. We used probabilistic partial values to represent these attributes. The advantages of this representation are: (i) all the conflicting values are retained, (ii) the DBMS is not required to make any assumption regarding the accuracy of the data, and, (iii) user preferences and reliability of the data can be taken into account. In order to answer queries involving partial valued attributes, various relational operators have been suggested in literature. We extended these in our model and presented a scheme for computing selections and projections.

As a part of our future research, we are looking at the possibility of using a comparison vector whose individual components would be continuous. In this paper, we assumed each component to be binary. It is possible to extend it to the case where $\gamma_{j}(t)$ can take on any value in the range [0, 1]. The continuous version can be used if functions can be defined to map the degree to which a join condition is satisfied to a value in this range.

One example of such a function is the edit distance d, which is used to measure distances between strings [20]. A name, John, mismatches with Jorn and Mike, but it is much closer to Jorn (d = 1) than it is to Mike (d = 4). This information, which might have been overlooked otherwise, can be captured with a continuous vector. Another potential application is when the rules associated with individual components of the vector are fuzzy [26], have a non-unity measure of belief or, define a set or a range of values (as opposed to a unique one) [36]. So even if the rule is satisfied, the contribution towards the vector would be less than one.

We are also considering various strategies to compute the join. In this paper, we assumed a simple strategy to compute E-join using the Cartesian product of the two relations. However, if the relations are large, and do not fit in the main memory then the writing of $K \times L$ tuples will have a significant impact on the total cost and the query response time to render E-join impractical.

A practical solution to this problem is to first subdivide the relations into a number of disjoint and smaller subsets, called buckets. Similar buckets are then identified between the two relations and their tuples are compared. Tuples not compared are automatically classified as unmatched. Since individual bucket sizes are much smaller than the original relation, computing cross products among buckets becomes considerably cheaper than computing the complete cross product. The only disadvantage of using buckets however, is that the probability of errors may increase with the decrease in bucket size. Thus, the bucketing strategy could be the practical way to execute approximate E-join, if the errors are within acceptable limits. The cost savings due to bucketing and the resultant errors are analyzed in [6]. We are currently developing a parallel architecture for bucket processing that would minimize the response time for the join queries.

We also plan to implement the E-join in the prototype DBMS, Postgres [17]. Postgres is an object oriented database management system being developed at the University of California at Berkeley. Although formally a relational DBMS, the system contains substantial new facilities to support procedural objects, rules, versions, inheritance and user defined operators. A simple form of E-join obtained by replacing the equivalence in the comparison vector by an equality, can be easily implemented. The problem of extending it to handle rule based joins is slightly involved and is currently under investigation. We are also looking at the following areas for further research:

\- extending the model to include matching of set valued attributes.

\- considering the relative informativeness of attributes and trade off issues between cost of data derivation and accuracy of join.

\- devising query computation algorithms using graph theoretic results like bipartite graph matching and its variants.

\- performing cost analysis for the proposed algorithms and implementing selective ones.

## Acknowledgements

Some of the ideas in this paper were developed as a result of Michael R. Stonebraker's suggestion to integrate rules with the probabilistic framework.

## A. Computing E-join results

Computing the result of an E-join involves: (i) calculating the tuple probabilities for all tuples, and (ii) using the threshold or the cutoff value to discard the poorly matched ones. We briefly outline these two steps in this section.

## A.1. Tuple probability estimations

As mentioned in Section 5.3, the computation of the tuple probability involves the evaluation of the following three terms: $\operatorname{Pr}\{\gamma(t)\}$ , $\operatorname{Pr}\{t \in \mathcal{M}\}$ and $\operatorname{Pr}\{\gamma(t) | t \in \mathcal{M}\}$ . We introduce the following notation to help estimate these terms:

m = number of tuples (out of $K \times L$ ) that satisfy the join query, $|M|$

$$
N (g) = \text { number   of   tuples } t, \text { such   that } \gamma (t) = \mathbf {g}
$$

$M(g) =$ number of matched tuples, $t\in \mathcal{M}$ , such that $\gamma (t) = \mathbf{g}$ , and,

$\mathrm{U}(\mathbf{g}) = \text{number of unmatched tuples, } t \in \mathcal{U};,$ such that $\gamma(t) = \mathbf{g}$

We can now express (and evaluate) the three terms as follows:

$$
\operatorname * {P r} \{t \in \mathcal {M} \} = \frac {m}{K \times L},
$$

$$
\operatorname * {P r} \{\gamma (t) = g \} = \frac {N (g)}{K \times L} \text { and }
$$

$$
\operatorname * {P r} \{\gamma (t) = g \mid t \in \mathcal {M} \} = \frac {M (g)}{m}.
$$

Notice that this representation results in a probability distribution as:

$$
\begin{array}{r l} & {\operatorname * {P r} \bigl \{t \in \mathcal {M} \mid \gamma (t) = \mathbf {g} \bigr \}} \\ & {\qquad = \frac {\operatorname * {P r} \bigl [ \gamma (t) = \mathbf {g} \mid t \in \mathcal {M} \bigr ] \cdot \operatorname * {P r} \bigl [ t \in \mathcal {M} \bigr ]}{\operatorname * {P r} \bigl [ \gamma (t) = \mathbf {g} \bigr ]}} \\ & {\qquad = \frac {M (\mathbf {g})}{m} \times \frac {m}{K \times L} \times \frac {1}{\frac {N (\mathbf {g})}{K \times L}}} \\ & {\qquad = \frac {M (\mathbf {g})}{N (\mathbf {g})}} \\ & {\qquad \leqslant 1.} \end{array}
$$

We can similarly show that

$$
\operatorname * {P r} \{t \in \mathcal {U}; | \gamma (t) = \mathbf {g} \} = \frac {U (\mathbf {g})}{N (\mathbf {g})}
$$

Since, $M(\mathbf{g}) + U(\mathbf{g}) = N(\mathbf{g})$ , the sum of the probabilities add up to one, and we have a valid probability distribution.

Thus, the calculation of tuple probabilities require only the knowledge of the distributions of the comparison vectors. For the binary vector, the statistical information can be stored in histograms and may be updated periodically, with the computation of the join.

The distributions can be obtained in several ways. For instance, it can be supplied by the user or the database administrator. Alternately, it can be estimated either by sampling or from previous results of the join. In many applications such as immigration control [9] and the CEDR project of U. S. Department of Energy (in progress at

Lawrence Berkeley Laboratory), records are matched clerically. These results, being fairly accurate, can be utilized in estimating the distributions. It should be noted though that since the data is frequently changing, storing join results for future references may not be of much use. Instead, by extracting the necessary statistical information from these results and using an appropriate knowledge base, the process of record matching can be made more efficient by reducing and eventually eliminating human intervention.

The problems of acquisition and storage of statistical information are of great practical importance but is outside the scope of the current paper. We defer a more detailed analysis to a follow-up study.

## A.2. The threshold value

A high value of tuple probability indicates a good match whereas a low value indicates otherwise. It is desirable that the tuples having a high value of tuple probability be in the output of the join and the rest be excluded. This requires setting a cutoff value, $p_{th}$ , such that all tuples having tuple probabilities greater than this value are considered good enough to be included in the output.

The decision regarding these tuples are subject to two types of errors. A type-I error (or an omission) occurs when $t \in M$ but $t \notin output$ . That is, a tuple that should have been a part of the output has been accidentally left out. A type-II error (or false alarm) occurs when $t \notin M$ but $t \in output$ . This means, an irrelevant tuple has been included in the output. With each type-II error, we associate a relative cost of $\alpha$ ; with each type-I error, we associate a relative cost of $(1-\alpha)$ . Then it can be shown [8] that the probability that minimizes these costs,

$$
p _ {t h} = \alpha
$$

A decision rule $\mathrm{d}(\gamma)$ can be now defined as a mapping from $\Gamma$ , the comparison space, to an action space $\{A_{m}, A_{u}\}$ where,

$A_{m} =$ include the tuple in the output set

$A_{u} =$ do not include the tuple in the output set and the set of all possible realizations of $\gamma$ constitutes the comparison space, $\Gamma$ . Using the threshold probability obtained above, the optimal decision rule is defined as:

$$
\begin{array}{r l} d [ \gamma (t) ] & = A _ {u} \quad \text { if } 0 \leqslant p _ {t u p l e} (t) <   p _ {t h} \\ & = A _ {m} \text { or } A _ {u} \quad \text { if } p _ {t u p l e} (t) = p _ {t h} \\ & = A _ {m} \quad \text { if } p _ {t h} <   p _ {t u p l e} (t) <   1. \end{array}
$$

The minimum expected cost of the error in computing the join is then given by:

$$
C (E) = \sum_ {t = 1} ^ {K \times L} \left[ \min \left\{p _ {\text { tuple }} (t), \alpha \right\} - \alpha p _ {\text { tuple }} (t) \right]
$$

The cost figures can be set by the database administrator, but it will be more appropriate if it is supplied by the user depending on the likely use of the result. In either case, estimating the threshold is fairly easy as only a relative value needs to be specified: the cost of a particular type of error with respect to the total error cost. The absolute cost of error on the other hand, is much harder to estimate.

## B. Proof of lemma 1

We prove this lemma using a set theoretic approach. Consider an event $A$ such that

$$
\begin{array}{l} A = \left\{t \in \mathcal {M} \mid \gamma (t) = g \right\}. \\ \text { and } \\ p _ {t u p l e} (t) = \operatorname * {P r} (A). \end{array}
$$

Let an event B be any generic selection condition involving partial valued attributes, as given in Section 7.3, such that

$$
p _ {a t t} (t) = \operatorname * {P r} (B).
$$

We want the overall probability of (i) an accurate join, and (ii) the satisfaction of the selection conditions by the partial valued valued attributes. (It should be kept in mind that all definite valued attributes are just special cases of probabilistic partial values.) In other words, we want to determine the probability that both events A and B occur at the same time, that is, $\Pr(A \wedge B)$ .

We know that

$$
\operatorname * {P r} (A \vee B) = \operatorname * {P r} (A) + \operatorname * {P r} (B) + \operatorname * {P r} (A \vee B)\tag{1}
$$

$$
\operatorname * {P r} (A)\tag{2}
$$

Similarly, we can write,

$$
\operatorname * {P r} (A \vee B) \geq \operatorname * {P r} (B)\tag{3}
$$

From Equatoins (2) and (3) we have,

$$
\operatorname * {P r} (A \vee B) \geq \max \left\{\operatorname * {P r} (A), \operatorname * {P r} (B) \right\}\tag{4}
$$

The above holds true because by definition, all probabilities are non negative. We can also write,

$$
\operatorname * {P r} (A \wedge B) = \operatorname * {P r} (A) + \operatorname * {P r} (B) - \operatorname * {P r} (A \vee B)\tag{5}
$$

$$
\leqslant \operatorname * {P r} (A) + \operatorname * {P r} (B) - \max \left\{\operatorname * {P r} (A), \right.
$$

$$
\operatorname * {P r} (B) \}\tag{6}
$$

$$
\leqslant \min \left\{\operatorname * {P r} (A), \operatorname * {P r} (B) \right\}\tag{7}
$$

From the definition of probability, we also know that any probability is bounded by one, that is,

$$
\operatorname * {P r} (A \vee B) \leq 1 \vee
$$

So we can write,

$$
\operatorname * {P r} (A \wedge B) = \operatorname * {P r} (A) + \operatorname * {P r} (B) - \operatorname * {P r} (A \vee B)\tag{8}
$$

$$
\geqslant \operatorname * {P r} (A) + \operatorname * {P r} (B) - 1\tag{9}
$$

From Equations (7) and (9) and the nonnegativity of probability, we can deduce,

$$
\begin{array}{r l} \max \{0, \operatorname * {P r} (A) + \operatorname * {P r} (B) - 1 \} & \leqslant \operatorname * {P r} (A \wedge B) \\ & \leqslant \min \{\operatorname * {P r} (A), \operatorname * {P r} (B) \} \end{array}
$$

and we have the proof.

## References

[1] Daniel Barbara, Hector Garcia-Molina, and Daryl Porter, A probabilistic relational data model, In Proceedings of International Conference on Extending Database Technology (EDBT'90), pages 60–74, Springer-Verlag, March 1990.

[2] M. Batini, C. Lenzirini, and S. Navathe, A comparative analysis of methodologies for database schema integration, ACM Computer Surveys, 18(4): 323–363, December 1986.

[3] Yuri Breitbart, Multidatabase interoperability, ACM SIGMOD Record, 19(3): 53–60, September 1990.

[4] Yuri Breitbart, Peter L. Olson, and Glenn R. Thompson, Database integration in a distributed heterogeneous database system, In Proceedings of the Second Interna-

tional Conference on Data Engineering, Los Angeles, California, pages 301–310, February 1986.

[5] M. Carpenter and M. Fair, editors, Canadian Epidemiology Research Conference - 1989 Proceedings of the Record Linkage Sessions and Workshop, Ottawa, Ontario, 1990.

[6] Rakesh Chandra, Abhirup Chatterjee, and Arie Segev, Accuracy and performance tradeoffs in multidatabase matching join processing, Technical Report 33338, Information and Computing Sciences Division, Lawrence Berkeley Laboratory, University of California at Berkeley, Berkeley, CA 94720, 1992.

[7] Abhirup Chatterjee and Arie Segev, Data manipulation in heterogeneous databases, ACM SIGMOD Record, 20(4): 64–68, December 1991.

[8] Abhirup Chatterjee and Arie Segev, A probabilistic approach to information retrieval in heterogeneous databases, In Proceedings of the First Workshop on Information Technologies and Systems (WITS), pages 107–124, Sponsored by the Centre for Information Systems Research, MIT, December 1991.

[9] J.B. Copas and F.J. Hilton, Record linkage: Statistical models for matching computer records, Journal of the Royal Statistical Society, Series A, 153(3): 287–312, 1990.

[10] Lawrence T. Cox and Robert F. Boruch, Record linkage, privacy and statistical policy, Journal of Official Statistics, 4(1): 3–16, 1988.

[11] Bogdan Czejdo, Marek Rusinkiewicz, and David W. Embley, An approach to schema integration and query formulation in federated database systems, In Proceedings of the Third International Conference on Data Engineering, Los Angeles, California, pages 477–484, February 1987.

[12] C. J. Date, Introduction to Database Systems, volume 1, Addison-Wesley Publishing Company, 5 th edition, 1990.

[13] Umeshwar Dayal and Hai-Yann Hwang, View definition and generalization for database integration in a multidatabase system, IEEE Transactions on Software Engineering, SE-10(6): 628–645, November 1984.

[14] Linda G. DeMichiel, Resolving database incompatibility: An approach to performing relational operations over mismatched domains, IEEE Transactions on Knowledge and Data Engineering, 1(4): 485–493, December 1989.

[15] I. P. Fellegi and A. B. Sunter, A theory of record linkage, Journal of the American Statistical Association, 64: 1183–1210, December 1969.

[16] Mark A. Johnson and Gerald M. Maggiora, editors, Concepts and Applications of Molecular Similarity, John Wiley and Sons, Inc., 1990.

[17] Greg Kemnitz, The PostgKss Reference Manual, Version 2.1. Report M91/10, Electronics Research Laboratory, University of California, Berkeley, CA, February 1991.

[18] William Kent, The entity join, In Proceedings of the Fifth International Conference on Very Large Databases (VLDB), pages 232–238, October 1979.

[19] N. Keyfitz, Information and allocation: Two uses of the 1980 census, The American Statistician, 33: 45–50, 1979.

[20] Donald E. Knuth, James H. Morris Jr., and Vaughan R. Pratt, Fast pattern matching in strings, Siam Journal on Computing, 6(2): 323–350, June 1977.

[21] James A. Larson, Shamkant B. Navathe, and Ramez Elmasri, A theory of attribute equivalence in databases with application to schema integration, IEEE Transactions on Software Engineering, 15(4): 449–463, April 1989.

[22] Maurice Lorr, Cluster Analysis for Social Scientists, Jossey-Bass Publishers, 1983.

[23] Victor M. Markowitz, An architecture for identifying objects in multidatabases, In Proceedings of the First International Workshop on Interoperability in Multidatabase Systems, Kyoto, Japan, pages 294–301, Sponsored by IEEE Computer Society and The Information Processing Society of Japan, April 1991.

[24] Frederick Mosteller and David L. Wallace, Inference and Disputed Authorship: The Federalist, Addison-Wesley Publishing; Company, Inc, 1964.

[25] Calton Pu, Key equivalence in heterogeneous databases, In Proceedings of the First International Workshop on Interoperability in Multidatabase Systems, Kyoto, Japan, pages 314–316, Sponsored by IEEE Computer Society and The Information Processing Society of Japan, April 1991.

[26] K.V.S.V.N. Raju and Arun K. Majumdar, Fuzzy functional dependencies and lossless join decomposition of fuzzy relational database systems, ACM Transactions on Database Systems, 13(2): 129–166, June 1988.

[27] Paul R. Rosenbaum, Optimal matching for observational studies, Journal of the American Statistical Association, 84(408): 1024–1032, December 1989.

[28] Gerard Salton and Michael J. McGill, Introduction to Modern Information Retrieval McGrawHill Book Company, 1983.

[29] Amit P. Sheth and James A. Larson, Federated database systems for managing distributed, heterogeneous, and autonomous databases, ACM Computer Surveys, 22(3):183–235, September 1990.

[30] Michael Siegel and Stuart E. Madnick, A metadata approach to resolving semantic conflicts, In Proceedings of the Seventeenth International Conference on Very Large Databases (VLDB), pages 133–145, September 1991.

[31] Richard J. Smith, Rebecca Z. German, and William L. Jungers, Variability of biological similarity criteria, Journal of Theoretical Biology, 118(3): 287–293, February 1986.

[32] R.L. Taft, Name search techniques, Technical report, New York State Identification and Intelligence System, New York, 1970.

[33] B. J. Tepping, A model for optimal linkage of records, Journal of the American Statistical Association, 63:1321–1332, December 1968.

[34] Erank Shou-Cheng Tseng, Arbee L. P. Chen, and Wei-Pang Yang, Answering heterogeneous database queries with degree of uncertainty, Technical Report CS-DB-92-007, National Tsing Hua University, Taiwan, 1992.

[35] Y. Richard Wang and Stuart E. Madnick, The interdatabase instance identification problem in integrating autonomous systems, In Proceedings of the Fifth International Conference on Data Engineering, Los Angeles, California, pages 46–55, February 1989.

[36] Eugene Wong, A statistical approach to incomplete information in database systems, ACM Transactions on Database Systems, 7(3): 470–488, September 1982.

![](/api/attachments/NAC5GFTW/fulltext/images/6c976a0ee11025413352439ad687aacaf6b2376dced7d606998c2a4b13b63cad.jpg)

Abhirup Chatterjee received his Bachelor's degree in Chemical Engineering from Jadavpur University, India, and Master's degree in Industrial Engineering from Stanford University. Currently, he is a Ph.D. candidate at the Walter A. Haas School of Business, University of California, Berkeley, and is also working in the Information and Computing Sciences Division, Lawrence Berkeley Laboratory. His research interests include

heterogeneous databases, rule based systems and query optimization. Mr. Chatterjee is a student member of the Association for Computing Machinery and the Institute of Management Science.

![](/api/attachments/NAC5GFTW/fulltext/images/20f8889d2095d17cae9b444000b4144726e1068b285f7c15b42375b1c9f61180.jpg)

Arie Segev received his Ph.D. degree in Computers and Information Systems from the University of Rochester in 1984. Since then he has been with the University of California at Berkeley, where he is now an Associate Professor and Director of the Information Technology Management Program at the Haas School of Business, with an affiliate position at the Information & Computing Sciences Division of Lawrence Berkeley Labora

tory. His research interests include logical and physical design of temporal databases, the integration of AI and Database technologies, the development and applications of advanced technologies to financial and manufacturing information systems, and the management of enterprise-wide Computing. He has published over 50 papers on these topics in leading journals and conferences. Professor Segev is currently the Editor-in-Chief of ACM SIGMOD RECORD, and is a member of the Association for Computing Machinery, IEEE Computer Society, and the Institute of Management Sciences.
