---
otero_id: 26350
otero_key: "4VW9PKAD"
title: "Modifications of Uncertain Data: A Bayesian Framework for Belief Revision"
authors: "Debabrata Dey; Sumit Sarkar"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.1.1.11785"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [155.198.30.43] On: 15 September 2016, At: 09:55 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## 6SR

![](/api/attachments/4VW9PKAD/fulltext/images/2b65508614b6fba664693e63ef5cc2fc6219fcf261b183cf5bdcd7ceda8e1c62.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Modifications of Uncertain Data: A Bayesian Framework for Belief Revision

Debabrata Dey, Sumit Sarkar,

To cite this article:

Debabrata Dey, Sumit Sarkar, (2000) Modifications of Uncertain Data: A Bayesian Framework for Belief Revision. Information Systems Research 11(1):1-16. http://dx.doi.org/10.1287/isre.11.1.1.11785

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/4VW9PKAD/fulltext/images/e60b34e1e1118d85c11ffd1f78b28506b3eee8f27e150e66987c075010877215.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Modifications of Uncertain Data: A Bayesian Framework for Belief Revision

Debabrata Dey • Sumit Sarkar

University of Washington, School of Business Administration, Department of Management Science,

Seattle, Washington 98195-3200

ddey@u.washington.edu

University of Texas at Dallas, School of Management, P.O. Box 830688, JO44, Richardson, Texas 75803-0688 sumit@utdallas.edu

he inherent uncertainty pervasive over the real world often forces business decisions to be made using uncertain data. The conventional relational model does not have the ability to handle uncertain data. In recent years, several approaches have been proposed in the literature for representing uncertain data by extending the relational model, primarily using probability theory. The aspect of database modification, however, has not been addressed in prior research. It is clear that any modification of existing probabilistic data, based on new information, amounts to the revision of one’s belief about real-world objects. In this paper, we examine the aspect of belief revision and develop a generalized algorithm that can be used for the modification of existing data in a probabilistic relational database. The belief revision scheme is shown to be closed, consistent, and complete.

(Data Uncertainty; Probabilistic Relational Model; Data Updating)

## 1. Introduction

Decision making in most modern businesses requires extensive use of large volumes of data; the quality of these decisions depends critically on the quality of the available data. The database approach to business information systems provides the decision maker with an easy-to-use interface, and yet maintains a high level of quality and integrity on large volumes of data. In recent years, database systems based on the relational model have become very popular for handling business data. Unfortunately, relational databases do not handle incomplete and uncertain data in a comprehensive manner. In many real-world business applications, however, the available data are often uncertain because of several reasons:

• The actual value of a data item may be unknown. For example, the actual release date of a competitor’s product may not be known with certainty. However, based on announcements and industry analysis, one could form an opinion about likely release dates. A company could then use these data to time the launching of its own product.

• The data item may not be realized yet. For example, one could store the uncertainty associated with future stock prices in a securities database (Barbara´ et al. 1992). This information would be useful in developing a portfolio of investments with specified characteristics.

• Uncertainty may also arise from consolidation or summarization of data (Bischoff and Alexander 1997). For example, the results of a market survey are often expressed in a consolidated manner in which the details of individual consumer preferences are summarized. Such information could be used in enhancing the design of the product.

• Another source of data uncertainty is data heterogeneity (Motro 1990). When two heterogeneous databases show different values for the same real-world data item, its actual value is not known with certainty. This is an important concern in developing corporate data warehouses where multiple heterogeneous data sources are often consolidated into a larger data repository.

Having no means to model them, the relational model ignores all uncertain data and focuses primarily on data values that are known with certainty; uncertain data values are represented using “null” (or unknown) values (Codd 1979, Date, 1986). Consequently, relational databases do not provide sufficient decision support in many business situations. The decision making process requires a data model that (i) can organize uncertain information from the real world in a readily usable form, and (ii) can consistently update this information based on changes in the real world.

Several extensions of the relational model (e.g., Barbara´ et al. 1992, Cavallo and Pittarelli 1987, Dey and Sarkar 1996) have been proposed, primarily based on probability theory, that attempt to overcome the above problem.<sup>1</sup> However, prior research has not addressed one of the most important aspects of a data model, namely modifications of existing data. Most databases go through the normal process of addition, deletion, and update of data items. In a probabilistic database, these modifications could result from two sources. First, the belief about the joint distribution of attributes may undergo modifications as the user obtains more reliable information. Second, some of the objects in the database may change their states in the real world. For example, a new employee may be hired, or an old one may be transferred to a new department. Clearly, the database must accommodate both by changing the existing belief about one or more objects. The purpose of this research is to examine the revision of belief in a probabilistic database. A belief revision scheme should ideally be: (i) consistent with the axioms of probability theory, (ii) complete so that all possible cases can be handled, and (iii) closed, meaning that the results of revisions are all valid relations. We use a Bayesian framework for developing a revision scheme that abides by the above properties.

The issue of belief revision has been widely studied in the literature. A simple, yet elegant, approach has been the use of Bayesian networks for knowledge representation in expert systems (Pearl 1988, Neapolitan 1990). There are several reasons why the relational representation and an associated belief revision scheme is better than Bayesian networks in capturing and revising data uncertainty. First, the representation of uncertainty in real-world data would require a separate Bayesian network for each individual entity instance; in other words, if we want to store information about 3,000 employees, we will need to construct 3,000 separate networks. Although the underlying structure of these networks may be the same, each network will have different numeric figures representing the interdependencies of the attributes. Such a representation can logically be viewed as an extension of the Network data model (Ullman 1988). Given that older database systems based on the Network model are rapidly being replaced by the newer relational database products, the market acceptability of a probabilistic database system based on the Network model is potentially a limiting factor. Second, there is a more serious conceptual problem. The Bayes’ net framework requires every possible realization of each variable to be explicitly encoded a priori, which implies that the entire domain of each attribute must be enlisted. Even if we ignore the issue of wasted storage space, it is very difficult— and often impossible—to develop a network with all possible realizations in the database context. For example, a new “rank” may be created and assigned to some employees. Since this could not have been enlisted a priori, such a situation would require a revision of the underlying network structure itself, as well as the revision of some of the probability values. The update performance in these situations would be a serious concern. Finally, using Bayesian networks, it is difficult to represent incomplete probability distributions, i.e., to represent facts where a portion of the probability mass is left unspecified. For example, we may not be able to say that there is a probability of 0.7 of EMP # 4432 being in the “accounting” department, but the assignment of the remaining probability mass of 0.3 is currently unknown. This has been identified as a common situation in the database context and the unspecified probability mass has been termed the miss ing probability by Barbara´ et al. (1992).

The rest of this paper is organized as follows. Section 2 provides further motivation for a probabilistic relational model and an associated belief revision scheme. The probabilistic relational model is outlined in § 3. Section 4 discusses the Bayesian framework for belief revision and its applicability to probabilistic databases. The belief revision scheme is described and illustrated in § 5. The complete algorithm is provided and its properties are discussed in § 6. Section 7 concludes the paper and offers future research directions.

## 2. Motivation and Problem Description

In the previous section, we discussed a few possible sources of data uncertainty. To illustrate the usefulness of capturing the uncertainty in a database environment, let us consider a situation where the dean of a particular college has asked that a database be developed for tracking all the alumni from that college. This database would rely on several sources for its input, such as the records and registration system, the central alumni database, and departmental records within the college. There are two important observations about this type of heterogeneous data sources (Bischoff and Alexander 1997). First, there is some overlap in the contents of these sources, i.e., the data on an alumnus may appear in more than one of these sources. Second, when there is an overlap, often the data stored are not identical across sources. For example, the address information of an alumnus may be different in two different data sources. Given that the correctness of these conflicting attribute values cannot be easily verified, the user is often faced with one of the following two difficult choices: (i) to retain only one of the values and discard the rest, or (ii) to represent these multiple values in an ad-hoc fashion (using multiple records or multiple fields). If the first option is chosen, it is possible that some valuable information (perhaps the correct address) is permanently lost in the process. On the other hand, if the user chooses to represent multiple values of address in multiple records, for example, the user may subsequently not recognize that several addresses are listed for that alumnus of which only one is accurate. Therefore, while generating a mailing list to, say, solicit contribution, one may end up with duplicate mailings thereby wasting time and money.

It is clear that the difficulty in consolidating such data from heterogeneous sources arises from the uncertainty in identifying the correct value of an attribute (Motro 1990). It would be easier to consolidate such data if we could assign a probability distribution to the multiple values of an attribute to capture the uncertainty associated with that attribute. To illustrate, assume that the address information from the records and registration system is the same as that in the departmental records for a certain individual, but is different from the address stored in the central alumni database. If all three sources are assumed to be equally credible, one could assign a probability of $\frac { 2 } { 3 }$ to the address obtained from the records and registration system and a probability of $; \frac { 1 } { 3 }$ to the address in the alumni database (Tseng et al. 1993). It is even possible that the user has more confidence in one of these sources since it is usually more accurate than others; in that case, one could adjust the probability assignments appropriately to reflect that belief. Several methods for obtaining the probability assignments have been presented in the literature. Pearl (1986) discusses how the probability values could be assigned based on the user’s confidence. It is also possible to assign probability values based on sampling, where a portion of the population is sampled to estimate the distribution (Barbara´ et al. 1992). Yet a third method, based on maximizing the entropy subject to a set of known constraints, is described in the classical work by Jaynes (1968).

Representing the uncertainty about attribute values in terms of a probability distribution is obviously beneficial at the time when such data are used for making a decision. Suppose, as before, that the alumni data are being used for generating a mailing list. If the user decides to send at most one mail to each individual, disregarding the cost of not reaching a few, the user could simply generate a list with the address having the highest probability for each individual. Such a list would be appropriate where the mailing costs are much higher than the cost of not reaching an alumnus. On the other hand, if the potential cost of not reaching a contributor is high, then one may decide to send mailings to all the available addresses. The nice feature of the probability-based data model is that the user has the flexibility of choosing not only between these two options, but from the entire range that these two extremes cover. By appropriately choosing a probability threshold and by including an address that has a probability greater than that threshold, the user can effectively determine the trade-off between these two costs for a real-world decision.<sup>2</sup> A data model that does not support data uncertainty clearly lacks this flexibility.

Another nice feature of a probabilistic representation is that the user has the option of revising his or her belief about a particular data item. After the initial consolidation of the heterogeneous sources has been done, new information may become available that, for example, could change the user’s opinion about the probability assignments to the address information. Therefore, when storing uncertain data, it is necessary for us to have a mechanism for modifying that data. We adopt the probabilistic relational model outlined in (Dey and Sarkar 1996) and develop a Bayesian framework for belief revision for that model. There are several reasons for our choice of the above model over other existing alternatives. First, the above model is in 1NF and is easy to implement. Second, their model and algebra are formally outlined in terms of the valid objects and associated operations. Finally, in this model, uncertainty in data has been modeled using probability theory, which, because of its wide acceptance, is easy to interpret. Probability measures have a rich theoretical basis for representing uncertainty; they lend themselves to empirical testability and provide an easy-to-use semantics (Pearl 1986, 1988).

## 3. The Probabilistic Relational Model

The belief revision scheme discussed in this paper is based on the probabilistic relational model of Dey and Sarkar (1996). In this section, we summarize the key features of that model.

In the deterministic relational model, real-world data are organized (logically) in the form of relations (or tables). A tuple (or a row) in a relation may be viewed as a representation of a real-world fact. It is assumed that this represented fact is “true” and is implicitly assigned a value of 1. Any fact that is not listed explicitly in the relation is assumed to be “false” and is (implicitly) assigned a value of 0; this is the usual closed world assumption. However, when there is uncertainty associated with real-world facts, it is not always possible to assign a value of 0 or 1 to these tuples.

This limitation can be addressed by using probability calculus. Instead of a value of 0 or 1, a tuple can be assigned a probability. This can be represented in the usual tabular format of a relation by appending a special column called the probability stamp or pS and explicitly storing only those tuples that have a non-zero probability. Table 1 shows this tabular representation of a probabilistic relation. It is clear that such a relation captures, for each distinct object, the joint distribution over all of the attributes; the probability associated with a particular attribute value of an object can be obtained by an appropriate marginalization of this joint distribution. For example, the first three rows in the EMPLOYEE relation in Table 1 represent the joint probability distribution associated with EMP# 3025. The marginal probability for EMP# 3025 is one, which implies that this employee is known to exist with certainty, although some of the attribute values are not known precisely. The probability that the rank of this employee is cashier is 0.8 (from the first and the third rows). It is also possible that the user may have a more complete probabilistic information about some attributes over others. In that case, null values (\*) are used as values for stochastic attributes that are not completely specified. This is illustrated with the second and third tuples corresponding to EMP# 6879.

Table 1 EMPLOYEE: A Probabilistic Relation

<table><tr><td> $EMP\#$ </td><td>LName</td><td>FName</td><td>Rank</td><td>Salary</td><td>Dept</td><td>pS</td></tr><tr><td>3025</td><td>Lyons</td><td>James</td><td>cashier</td><td>20K</td><td>shoe</td><td>0.6</td></tr><tr><td>3025</td><td>Lyons</td><td>James</td><td>clerk</td><td>15K</td><td>toy</td><td>0.2</td></tr><tr><td>3025</td><td>Lyons</td><td>James</td><td>cashier</td><td>15K</td><td>auto</td><td>0.2</td></tr><tr><td>6723</td><td>Kivari</td><td>Jack</td><td>clerk</td><td>18K</td><td>toy</td><td>0.4</td></tr><tr><td>6723</td><td>Kivari</td><td>Jack</td><td>cashier</td><td>20K</td><td>auto</td><td>0.4</td></tr><tr><td>6723</td><td>Kivari</td><td>Jack</td><td>*</td><td>*</td><td>*</td><td>0.1</td></tr><tr><td>6879</td><td>Peters</td><td>Julia</td><td>clerk</td><td>25K</td><td>toy</td><td>0.3</td></tr><tr><td>6879</td><td>Peters</td><td>Julia</td><td>clerk</td><td>*</td><td>toy</td><td>0.1</td></tr><tr><td>6879</td><td>Peters</td><td>Julia</td><td>cashier</td><td>*</td><td>*</td><td>0.6</td></tr></table>

We formalize this structure in the following manner.<sup>3</sup> A relation scheme R is a set of attribute names $\{ A _ { 1 } ,$ $A _ { 2 } , \ldots , A _ { N } \}$ , one of which may be $p S ,$ the implicit probability attribute. The domain of $A _ { i }$ is a set ${ \mathcal { D } } _ { i } ; { \mathrm { i f } } A _ { i } = p S ,$ then $\mathcal { D } _ { i } = ( 0 , 1 ]$ . Let $\mathcal { D } = \mathcal { D } _ { 1 } \cup \mathcal { D } _ { 2 } \cup . . . \cup \mathcal { D } _ { N } . \mathsf { A }$ tuple over R is a function from R to  ( : $R  \mathcal { D } )$ , such that $\alpha ( A _ { i } ) \in \mathcal { D } _ { i } , i \in \{ 1 , 2 , . . . , N \}$ . Thus, is a set of attribute name-value pairs: $\alpha = \{ \langle A _ { i } , v _ { i } \rangle | ( A _ { i } \in R \land v _ { i }$ $\in \mathcal { D } _ { i } ) \}$ . Restriction of over $S \subset R$ is defined as: (S) $= \{ \langle A , v \rangle \in \alpha \mid A \in S \}$ . Two tuples  and $\beta$ on relation scheme R are value-equivalent (written $\alpha \simeq \beta )$ if and only if, for all $A \in ( R \mathrm { ~ - ~ } \{ p S \} ) , \alpha ( A ) = \beta ( A )$ . A relation r on the scheme R is a finite collection of tuples  on R such that no two tuples in r are value-equivalent. Analogous to the elimination of duplicates in a deterministic relation, value-equivalent tuples are not allowed in a relation; they must be coalesced. The coalescence operation (denoted by $\textcircled{+} )$ on two valueequivalent tuples and $\beta$ is defined as:

$$
\begin{array}{l} \gamma = \alpha \oplus \beta \Leftrightarrow (\gamma \simeq \alpha) \wedge (\gamma \simeq \beta) \wedge \\ (\gamma (p S) = \min \{1, \alpha (p S) + \beta (p S) \}). \end{array}
$$

Of course, the idea of value-equivalent tuples and the coalescence operation can be extended to more than two tuples by treating them in a pairwise fashion.

In the relational model, every tuple in a relation represents a unique object (i.e., an entity or a relationship) from the real world; a superkey is a set of attributes that uniquely identifies a tuple and, hence, an object. A superkey, in that sense, is an object surrogate, one that uniquely identifies every object. A candidate key is a minimal superkey, minimal in the sense that no attribute can be dropped without sacrificing the property of uniqueness. For each relation, only one candidate key is chosen as the primary key of that relation. In the probabilistic extension, where every tuple has a probability stamp that represents the joint probability of occurrence of the attribute values in that tuple, each tuple cannot stand for a unique object. Associated with every object there may be several tuples representing the complete joint distribution of its attributes. This suggests that we must retain the object surrogate interpretation of a candidate key (i.e., minimal unique identifier of real-world objects) and discard the notion of a candidate key as a unique identifier of tuples. The primary key is chosen from the set of candidate keys, and two constraints are imposed on it: (i) A primary key value cannot be null, and (ii) the marginal probability associated with a primary key value must be no more than one. In other words, if r is a relation on scheme R with primary key K, then, for all $\alpha \in r ,$

$$
\alpha (K)\neq \text{null, and}\sum_{\substack{\beta \in r\\ \beta (K) = \alpha (K)}}\beta (pS)\leq 1.
$$

In the following, we redefine the three most common relational operations, namely projection, selection, and join, and define a new operation called conditionalization.

1. Projection. Let r be a relation on scheme $R ,$ and let $S \subset R$ . The projection of r onto S is defined as:

$$
\Pi_{S}(r) = \bigg\{\alpha (S)\mid \alpha = \bigoplus_{\substack{\beta \in r\\ \beta (S)\simeq \alpha}}\beta (S)\bigg\} .
$$

2. Selection. Let r be a relation on scheme R. Let H be a set of comparators over domains of attribute names in R. Let $P$ be a predicate (called the selection predicate) formed by attributes in $R ,$ comparators in $\Theta ,$ constants in the domain of A for all $A \in R$ , and logical connectives. The selection on r for $P ,$ written $\sigma _ { P } ( r )$ , is the set { $\in r \mathnormal { | } P ( \alpha ) \}$

3. Natural Join. Let r and s be any two relations on schemes R and $S ,$ respectively, and let $R ^ { \prime } = R - \{ p S \}$ and $S ^ { \prime } = S - \{ p S \}$ }. The natural join of r and s is defined as:

$$
\begin{array}{r l} r \bowtie s = & \{\alpha (R \cup S) \mid \exists \beta \in r   \exists \gamma \in s ((\alpha (R ^ {\prime}) \\ & = \beta (R ^ {\prime})) \wedge (\alpha (S ^ {\prime}) = \gamma (S ^ {\prime})) \wedge \\ & (\alpha (p S) = \beta (p S) \gamma (p S)) \}. \end{array}
$$

4. Conditionalization. Let r be a relation on scheme $R ,$ and let $S \subset R \mathrm { ~ - ~ } \{ p S \}$ . The conditionalization of r on S is given by:

$$
Y _ {S} (r) = \left\{\alpha (R) \mid \exists \beta \in r \left((\alpha \simeq \beta) \wedge \left(\alpha (p S) = \frac {\beta (p S)}{\eta_ {S , r} (y)}\right)\right) \right\},
$$

where $\eta _ { S , r } ( \alpha )$ is a function defined on a tuple $\alpha \in r$ if $p S \in R ,$ and is given by:<sup>4</sup>

$$
\eta_{S,r}(\alpha) = \min \left\{1,\sum_{\substack{\beta \in r\\ \beta (S) = \alpha (S)}}\beta (pS)\right\} .
$$

## 4. The Bayesian Framework

We consider the Bayesian framework for belief revision. Let $B _ { i } , i = 1 , 2 , \ldots , n ,$ be a set of exhaustive and mutually exclusive propositions. The degree of belief in another proposition $C ,$ which is dependent on the propositions $B _ { i } ,$ can be written using Bayes’ conditionalization formula as:

$$
\operatorname{prob} [ C ] = \sum_ {i = 1} ^ {n} \operatorname{prob} [ C \mid B _ {i} ] \operatorname{prob} [ B _ {i} ].
$$

It then amounts to finding a way of updating the probability of C based on updated probabilities of $B _ { i } , i =$ $1 , 2 , \ldots , n .$

## 4.1. Jeffrey’s Kinematics

Jeffrey (1983) addresses the problem of updating the degree of belief in C when some new evidence (or some passage of an experience) e is obtained. It is assumed that e does not affect the probability of C directly, neither does it change the conditional degree of belief in C given $B _ { i } .$ In other words, if this new degree of belief is denoted by “PROB,” then PROB[C $\begin{array} { r l } { B _ { i } ] } & { { } = } \end{array}$ prob[C| $B _ { i } ] .$ However, if e changes the degree of belief in $B _ { i } ,$ it is clear that it should (indirectly) affect the degree of belief in C. The revised degree of belief in C is then written as (Jeffrey’s rule of probability kinematics):

$$
\operatorname{PROB} [ C ] = \sum_ {i = 1} ^ {n} \operatorname{prob} [ C \mid B _ {i} ] \operatorname{PROB} [ B _ {i} ].
$$

Pearl (1988) illustrates this using the following example. Assume that an agent is uncertain about the color of a cloth and is considering the propositions that the cloth is green, blue or violet. These three propositions are denoted as $G , B$ and V respectively. Let the agent’s current degrees of belief in these propositions be given by: prob[G]  0.3, prob[B]  0.3, and prob[V] $= \ 0 . 4 .$ . Consider a proposition C that the cloth will be sold the next day. If we make the additional assumption that the chances of selling the cloth depend on its color in the following manner: prob[C|G]  0.4, prob[ $C \mid B \mid ~ = ~ 0 . 4 ,$ , and prob[C $~ | ~ V ] ~ = ~ 0 . 8 ,$ then the agent’s belief of the cloth selling the next day should be given by:

$$
\operatorname{prob} [ C ] = (0. 4) (0. 3) + (0. 4) (0. 3) + (0. 8) (0. 4) = 0. 5 6.
$$

Now, let us consider the situation where that the agent gets to inspect the cloth by candlelight and subsequently revises the belief about the color of the cloth as: PROB[G]  0.70, PROB[B]  0.25, and PROB[V] $= 0 . 0 5$ . Since the dependence of salability of the cloth on its color ought not to have changed, the agent’s revised belief of the cloth selling the next day is given by:

$$
\begin{array}{r l} \text { PROB } [ C ] & = (0. 4) (0. 7) + (0. 4) (0. 2 5) \\ & + (0. 8) (0. 0 5) = 0. 4 2. \end{array}
$$

Pearl (1988) argues that, based on the new evidence $e ,$ the update should be based on the conditionalization formula:

$$
\operatorname{prob} [ C \mid e ] = \sum_ {i = 1} ^ {n} \operatorname{prob} [ C \mid B _ {i}, e ] \operatorname{prob} [ B _ {i} \mid e ],
$$

and, in the case where prob[C| $B _ { i } , e ] = { \sf p r o b } [ C \mid B _ { i } ] ,$ simply as:

$$
\operatorname{prob} [ C \mid e ] = \sum_ {i = 1} ^ {n} \operatorname{prob} [ C \mid B _ {i} ] \operatorname{prob} [ B _ {i} \mid e ],
$$

It is possible to argue that the evidence e may not always be expressible as a proposition and Jeffrey’s rule is, in that sense, more general than the above conditionalization formula. Furthermore, in the database context, the passage of an experience changes certain data values which are explicitly captured in the database. Naturally, in modifying a database, one is primarily concerned with the new belief about the captured data; in particular, users may not really care about the underlying passage of experience (or its expressibility as a proposition), if it is not being captured explicitly in the database. Therefore, as long as one interprets PROB[•] as prob[•|e], either notation provides a satisfactory working formula.

## 4.2. Database Modification

Let us now examine how the above can be used in updating the belief about objects in a database. Consider the following simple relation with K as the primary key:

<table><tr><td> $\underline{K}$ </td><td>X</td><td>Y</td><td>pS</td></tr><tr><td> $k_{1}$ </td><td> $x_{1}$ </td><td> $y_{1}$ </td><td>0.5</td></tr><tr><td> $k_{1}$ </td><td> $x_{1}$ </td><td> $y_{2}$ </td><td>0.5</td></tr><tr><td> $k_{2}$ </td><td> $x_{2}$ </td><td> $y_{1}$ </td><td>0.3</td></tr></table>

It implies that:

$$
\mathsf {p r o b} [ K = k _ {1}, X = x _ {1}, Y = y _ {1} ] = 0. 5
$$

$$
\mathsf {p r o b} [ K = k _ {1}, X = x _ {1}, Y = y _ {2} ] = 0. 5
$$

$$
\operatorname{prob} [ K = k _ {2}, X = x _ {2}, Y = y _ {1} ] = 0. 3
$$

Now assume that some new information (passage of a new experience) makes us change our belief about the marginal probability of $[ K = k _ { 1 } , X = x _ { 1 } ]$ to 0.8. In other words, we have:

$$
\mathsf {P R O B} [ K = k _ {1}, X = x _ {1} ] = 0. 8.
$$

How should this new information affect the first two tuples in the previous relation? If we assume that the conditional distribution of Y given K and X has not changed, i.e., if

$$
\begin{array}{l} \text {PROB} [ Y = y _ {1} | K = k _ {1}, X = x _ {1} ] \\ \quad = \text {prob} [ Y = y _ {1} | K = k _ {1}, X = x _ {1} ], \end{array}
$$

then, using Jeffrey’s rule of probability kinematics, we have:

$$
\mathsf {P R O B} [ K = k _ {1}, X = x _ {1}, Y = y _ {1} ] =
$$

$$
\operatorname{prob} \left[ Y = y _ {1} \mid K = k _ {1}, X = x _ {1} \right] \times
$$

$$
\mathsf {P R O B} [ K = k _ {1}, X = x _ {1} ] = 0. 5 \times 0. 8 = 0. 4.
$$

Similarly,

$$
\mathsf {P R O B} [ K = k _ {1}, X = x _ {1}, Y = y _ {2} ] = 0. 4,
$$

and the resulting new relation would reflect the $\mathrm { r e - }$ vised belief as:

<table><tr><td> $\underline{K}$ </td><td>X</td><td>Y</td><td>pS</td></tr><tr><td> $k_{1}$ </td><td> $x_{1}$ </td><td> $y_{1}$ </td><td>0.4</td></tr><tr><td> $k_{1}$ </td><td> $x_{1}$ </td><td> $y_{2}$ </td><td>0.4</td></tr><tr><td> $k_{2}$ </td><td> $x_{2}$ </td><td> $y_{1}$ </td><td>0.3</td></tr></table>

The question is: how justified are we in assuming that the conditional distribution of the unspecified attribute $\boldsymbol { Y } ,$ with respect to the attributes K and $X ,$ has not changed? We conclude that it is the only practical assumption to make in absence of further information. If the user were to know how the conditional distribution has changed, then the information would not be provided only in terms of K and $X ;$ it should be specified as a joint distribution involving K, X, and Y. So we must assume that the user does not know about the nature of the changed conditional distribution. In that case, using any other value for the dependence of Y on K and X clearly has no basis, and one should persist with the old information about the dependence in updating the relation. Thus, the use of stale information in the absence of fresh information is the only practical course of action.

It must be emphasized that we use the notation e in a more general sense than the conventional Bayesian framework (see Figure 1). There, the belief about the dependent proposition C at a specific point in time is computed based on new information about the propositions $B _ { i } .$ In the above example—observation by candlelight, as it has come to be called—we were only considering the dependence of the salability of the cloth on its color at a specific time; it is understood that this dependence itself might change over time, and the temporal behavior was not considered relevant.

In database systems, however, the temporal nature of objects and their properties is important. A database stores probabilistic information about real-world objects, the probabilities indicating the current best estimates of our belief in the properties of these objects. There are two ways in which these estimates may change. First, an event may have recently taken place in the real world that forces some objects to change their states. This implies that the database must reflect a change in our beliefs about those objects. For example, if the government imposes heavier taxes on tobacco products, we must revise our belief about the

Figure 1 Sources of Belief Revision for a Database  
![](/api/attachments/4VW9PKAD/fulltext/images/cf4a6f7145db507dc7dec7c4b5f04dcd363c582af8279c9df83647e8e9558562.jpg)  
Table 2 A Probabilistic EMPLOYEE Relation  
profitability of R. J. Reynolds Tobacco Company or the risk associated with investing in that company. On the other hand, even though an object may persist in its original state, some new information may have become available which may change our belief about it. For example, a better financial analysis may reveal that the riskiness of a particular investment is actually lower than it was perceived earlier. We use e as a joint notation for either a real-world event or as evidence. While an evidence typically does not change the conditional dependence of Y on $X ,$ an event might. However, if fresh information to the contrary is not explicitly provided, we will assume that the conditional distribution has not changed. We formalize this idea in the next section by extending it to the case where X and Y are not just attributes, rather they are sets of attributes.

## 5. The Belief Revision Scheme

Let R be a probabilistic relation scheme. We can, in general, express R as $R = K X Y \cup \{ p S \}$ , where K denotes the primary key of the relation scheme, pS is the probability stamp, $X \subset ( R - K )$ , and $Y = R - ( K X \cup \{ p S \} )$ In other words, X and Y are mutually exclusive sets of nonkey attributes; the possibility that one of them is empty is not excluded. Let r be a relation on R. We consider arrival of new information about object k in r in the form:

$$
\mathsf {P R O B} [ K = k, X = x _ {i} ] = p _ {i}, i = 1, 2, \dots , m.
$$

For example, consider the probabilistic employee relation shown in Table 2. This table is obtained by projecting the relevant attributes from the relation in Table 1 and will be used to illustrate the belief revision scheme throughout this section. Now, if the new information is PROB[ $\mathrm { E M P \# } = 6 7 2 3 ] = 0 . 4 5 ,$ then $K =$ {EMP#}, $X = \emptyset .$ , and Y  {rank, salary, dept}. Also, m  1 and $p _ { 1 } = 0 . 4 5$

<table><tr><td> $EMP\#$ </td><td>rank</td><td>salary</td><td>dept</td><td>pS</td></tr><tr><td>3025</td><td>cashier</td><td>20K</td><td>shoe</td><td>0.6</td></tr><tr><td>3025</td><td>clerk</td><td>15K</td><td>toy</td><td>0.2</td></tr><tr><td>3025</td><td>cashier</td><td>15K</td><td>auto</td><td>0.2</td></tr><tr><td>6723</td><td>clerk</td><td>18K</td><td>toy</td><td>0.4</td></tr><tr><td>6723</td><td>cashier</td><td>20K</td><td>auto</td><td>0.4</td></tr><tr><td>6723</td><td>*</td><td>*</td><td>*</td><td>0.1</td></tr><tr><td>6879</td><td>clerk</td><td>25K</td><td>toy</td><td>0.3</td></tr><tr><td>6879</td><td>clerk</td><td>*</td><td>toy</td><td>0.1</td></tr><tr><td>6879</td><td>cashier</td><td>*</td><td>*</td><td>0.6</td></tr></table>

Note that, for the new information to be meaningful, the p s must add up to no more than one and the x s must be distinct. Often, users may not be able to provide the new information as a complete distribution for attributes K and X. Therefore, we allow the new information to be an incomplete specification of the distribution. Irrespective of whether this new information is complete or otherwise, the database must be revised in a manner that: (i) is consistent with the new information and, (ii) results in assigning probabilities to unspecified realizations of the stochastic variables in a manner consistent with the existing data. As in the previous section, we will use the following notation. All new information, as well as revised beliefs, will be denoted as “PROB,” whereas old beliefs will be represented as “prob.”

To revise beliefs about attributes of an object, we need to consider the following three possibilities:

Case 1. There exists tuple $\langle k , x , y , q \rangle \in r ,$ for some q $\in ( 0 , 1 ]$ , such that $x \ = \ x _ { i } ,$ for some $i \in \{ 1 , 2 , \dots , m \}$ This is case where an existing tuple matches a tuple in the new information on the attributes K and X.

Case 2. There exists tuple $\langle k , x , y , q \rangle \in r ,$ for some q $\in ( 0 , 1 ] ,$ such that $x \neq x _ { i } ,$ for all $i \in \{ 1 , 2 , \dots , m \}$ . In this case, a tuple in the existing relation has no matching tuple in the new information.

Case 3. There exists some $i \in \left\{ 1 , 2 , \dots , m \right\} .$ , such that the tuple $\left. k , x _ { i } \right. \notin \Pi _ { K X } \left( r \right)$ . This would be the case when a tuple in the new information does not match with any tuple in the existing relation.

## 5.1. Case 1

Consider a tuple $\langle k , x , y , q \rangle \in r$ for some $q \in ( 0 ,$ 1], and assume that $x = x _ { i }$ for some $i \in \{ 1 , 2 , \ldots ,$ m}. It is now straightforward to calculate the new probability Q associated with the above tuple:

$$
\begin{array}{r l} Q & = \text { PROB } [ K = k, X = x _ {i}, Y = y ] \\ & = \text { prob } [ Y = y | K = k, X = x _ {i} ] \\ & \quad \times \text { PROB } [ K = k, X = x _ {i} ] \\ & = \frac {\text { prob } [ K = k , X = x _ {i} , Y = y ]}{\text { prob } [ K = k , X = x _ {i} ]} \\ & \quad \times \text { PROB } [ K = k, X = x _ {i} ] \\ & = \frac {q}{\prod_ {p S} (\sigma_ {K = k , X = x _ {i}} (r))} \times p _ {i}. \end{array}\tag{1}
$$

Clearly, a new tuple $\langle k , \ x _ { i } , \ y , \ Q \rangle$ should replace the corresponding old tuple in r.

The assumption made here is that the conditional probability of $Y = y ,$ given $K = k$ and $X = x _ { i } ,$ is unchanged given the new information (as discussed in the previous section). If we consider the new information to be the result of taking some experience (or event) e into evidence, then it is assumed that

$$
\begin{array}{c} \mathsf {p r o b} [ Y = y | X = x _ {i}, K = k, e ] \\ = \mathsf {p r o b} [ Y = y | X = x _ {i}, K = k ], \end{array}
$$

that is, Y and e are conditionally independent of each other given K and X. However, since prob $[ K = k ,$ X $\mathbf { \theta } = \mathbf { \theta } _ { x _ { i } } | \mathbf { \theta } _ { e } ]$ is different from prob $[ K = k , X = x _ { i } ] ,$ , the revised value of prob $[ K = k , X = x _ { i } , Y = y$ |e] is also different from prob $[ K = k , X = x _ { i } , Y = y ] .$ . The net outcome is that probability masses in the original relation that are assigned to different values of Y for given K and X are prorated such that the marginal probability of $K = k$ and $X = x _ { i }$ in the revised database matches the new probability prob $[ K = k , X = x _ { i } | e ]$

Example 1. Consider the relation in Table 2, and let the new information be:

$$
\mathrm{PROB} [ \mathrm{EMP} \# = 6 7 2 3 ] = 0. 4 5.
$$

This information implies that the probability of existence of an employee with EMP#  6723 is 0.45. The revision is straightforward: all tuples in the existing relation with EMP#  6723 fall under Case 1. The total probability of 0.45 should now be proportionately distributed across the existing tuples. The resulting relation is shown in Table 3.

## 5.2. Case 2

Consider a tuple $\langle k , x , y , q \rangle \in r ,$ for some $q \in ( 0 , 1 ]$ ; there is no new information available on tuples with $X = x .$ The total probability currently assigned to object k is given by:

$$
\mathsf {p r o b} [ K = k ] = \Pi_ {p S} (\sigma_ {K = k} (r)) = P _ {k} (\text { say }).
$$

The new information, on the other hand, assigns a probability of $\Sigma _ { i = 1 } ^ { m } \ p _ { i }$ to the existence of object k. We assume that the revised distribution assigns a value of max $\{ P _ { k } , \ \Sigma _ { i = 1 } ^ { m } \ p _ { i } \}$ to object k. If $\Sigma _ { i = 1 } ^ { m } \ p _ { i } \geq P _ { k } ,$ then the entire probability mass assigned to object k is specified in the new distribution. Therefore, $\mathsf { P R O B } [ K = k , X =$ x] becomes zero, and the corresponding tuples should be eliminated from r. However if $\Sigma _ { i = 1 } ^ { m } \ p _ { i } < P _ { k } ,$ then PROB[K  k] retains the value $P _ { k } .$ In that case, PROB[K  k, X  x] cannot be computed directly, since part of the probability mass is unspecified. It is, however, clear that $\mathsf { P R O B } [ K = k , X = x ]$ will be a fraction of the unspecified probability mass, i.e., $\left( P _ { k } \ - \ \Sigma _ { i = 1 } ^ { m } \ p _ { i } \right)$

Table 3 Revised EMPLOYEE Relation for EMP# 	 6723

<table><tr><td> $EMP\#$ </td><td>rank</td><td>salary</td><td>dept</td><td>pS</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>6723</td><td>clerk</td><td>18K</td><td>toy</td><td>0.2</td></tr><tr><td>6723</td><td>cashier</td><td>20K</td><td>auto</td><td>0.2</td></tr><tr><td>6723</td><td>*</td><td>*</td><td>*</td><td>0.05</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr></table>

We recommend that this unspecified mass be distributed in a way such that the new assignment is proportional to the older assignment of probabilities. We see that the missing probability mass of $( P _ { k } \mathrm { ~ - ~ }$ $\Sigma _ { i = 1 } ^ { m } \ \ l { p _ { i } } )$ has to be assigned to values other than $x _ { i } , i =$ $1 , 2 , \ldots , m$ . The corresponding probability mass that was previously assigned to these values is:

$$
P _ {k} - \sum_ {i = 1} ^ {m} \Pi_ {p S} (\sigma_ {K = k, X = x _ {i}} (r)).
$$

Out of this, the probability mass that was assigned to $K = k$ and $X = x$ is:

$$
\mathsf {p r o b} [ K = k, X = x ] = \Pi_ {p S} (\sigma_ {K = k, X = x} (r)).
$$

The new probability can now be calculated by appropriate normalization as:

$$
\begin{array}{l} \text {PROB} [ K = k, X = x ] = \Pi_ {p S} (\sigma_ {K = k, X = x} (r)) \\ \times \frac {P _ {k} - \sum_ {i = 1} ^ {m} p _ {i}}{P _ {k} - \sum_ {i = 1} ^ {m} \Pi_ {p S} (\sigma_ {K = k , X = x _ {i}} (r))}. \end{array}
$$

The calculation of the new probability Q associated with $\langle k , x , y \rangle$ is now easy:

$$
\begin{array}{r l} Q & = \text {PROB} [ K = k, X = x, Y = y ] \\ & = \text {prob} [ Y = y | K = k, X = x ] \\ & \quad \times \text {PROB} [ K = k, X = x ] \\ & = \frac {\text {prob} [ K = k , X = x , Y = y ]}{\text {prob} [ K = k , X = x ]} \\ & \quad \times \text {PROB} [ K = k, X = x ] \\ & = \frac {q}{\prod_ {p S} (\sigma_ {K = k , X = x} (r))} \times \Pi_ {p S} (\sigma_ {K = k, X = x} (r)) \end{array}
$$

$$
\begin{array}{c} \times \frac {P _ {k} - \sum_ {i = 1} ^ {m} p _ {i}}{P _ {k} - \sum_ {i = 1} ^ {m} \Pi_ {p S} (\sigma_ {K = k , X = x _ {i}} (r))} \\ = q \times \frac {\Pi_ {p S} (\sigma_ {K = k} (r)) - \sum_ {i = 1} ^ {m} p _ {i}}{\Pi_ {p S} (\sigma_ {K = k} (r)) - \sum_ {i = 1} ^ {m} \Pi_ {p S} (\sigma_ {K = k , X = x _ {i}} (r))}. \end{array}\tag{2}
$$

The old tuple $\langle k , x , y , q \rangle$ should then be deleted from the relation, and a new tuple $\langle k , x , y , Q \rangle$ should be included in r.

The above scheme can also be explained in terms of an assumption of conditional independence. Let $\tilde { X }$ be the set of values of attributes of X that appear in the original relation for $K = k ,$ but are not specified as part of the new information. Then the assumption made here is that

$$
\mathsf {p r o b} [ K = k, X = x _ {i} | \tilde {X}, e ] = \mathsf {p r o b} [ K = k, X = x _ {i} | \tilde {X} ],
$$

where $x _ { i } \in { \tilde { X } } .$ . Thus, for lack of any other information, we assume that the probability of any of the outcomes $x _ { i } \mathrm { g i v e n } \tilde { X }$ is unchanged in the new distribution. Once the revised beliefs are obtained for $x _ { i } \in { \tilde { X } } ,$ the beliefs for $[ K = k , Y = y , X = x _ { i } ]$ are updated in a fashion similar to Case 1.

Example 2. Consider the relation in Table 2, and let the new information be:

$$
\operatorname{PROB} [ \text { EMP } \# = 3 0 2 5, \text { rank } = \text { clerk } ] = 0. 6.
$$

This information will affect the tuples in the old relation in two ways. There are three tuples in this relation satisfying EMP#  3025; the second tuple falls under Case 1, whereas the first and the third tuples fall under Case 2. It is clear that the second tuple should have a pS-value of 0.6. For the other two tuples, note that the probability of rank  “cashier” for this employee is no longer 0.8. In absence of better information, we assume that the residual probability of 0.4 is assigned to it. Then, this probability mass 0.4 is proportionately distributed (based on the previous distribution) over the other two tuples. The resulting relation is shown in Table 4; the tuples revised according to Case 2 are italicized in this table.

## 5.3. Case 3

The new information, in the form $\mathsf { P R O B } [ K = k , X =$ $x _ { i } ] = p _ { i } ,$ where $\langle k , x _ { i } \rangle \not \in \varPi _ { \mathrm { K X } } ( r )$ for some $i \in \{ 1 , 2 , \ldots ,$ m}, is incorporated by inserting a new tube $\langle k , x _ { i } , \rangle , p _ { i } \rangle$ into r.

Example 3. Consider the following new information:

$$
\text { PROB } [ \text { EMP\# } = 6 7 2 3, \text { rank } = \text { packer } ] = 0. 4 5,
$$

$$
\mathsf {P R O B} [ \mathsf {E M P} \# = 6 7 2 3, \text { rank } = \text { clerk } ] = 0. 2.
$$

This information will affect the tuples in the old relation (Table 2) in three different ways. The first among the existing tuples for $\mathrm { E M P } \# = 6 7 2 3$ falls under Case 1, while the second and the third fall under Case 2. Also, based on the new information, a new tuple has to be created according to Case 3. The revised relation is shown in Table 5, with the tuple resulting from Case 3 italicized.

## 5.4. Information Scattered Across Multiple Relations

So far, we have implicitly assumed that the attributes in a probabilistic relation are all mutually dependent. When that is not the case, a significant amount of data redundancy can be eliminated by normalizing them in a way such that each relation scheme represents only those attributes that are conditionally dependent given the primary key attributes. In developing the revision scheme, we have assumed that the relation is normalized; i.e., it does not contain any attribute that is independent of all the other nonkey attributes given the primary key. This assumption is reasonable since it eliminates data inconsistencies during the revision process. This is analogous to the issue of update anomalies in deterministic nonnormalized relations. However, the above assumption also means that the information about an entity may be distributed across several relations. For example, the hire-dates of employees may be stored in a separate relation as shown in Table 6.

Table 4 Revised EMPLOYEE Relation for EMP# 	 3025

<table><tr><td> $EMP\#$ </td><td>rank</td><td>salary</td><td>dept</td><td>pS</td></tr><tr><td>3025</td><td>cashier</td><td>20K</td><td>shoe</td><td>0.3</td></tr><tr><td>3025</td><td>clerk</td><td>15K</td><td>toy</td><td>0.6</td></tr><tr><td>3025</td><td>cashier</td><td>15K</td><td>auto</td><td>0.1</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr></table>

Table 5 Revised EMPLOYEE Relation for EMP# 	 6723

<table><tr><td> $EMP\#$ </td><td>rank</td><td>salary</td><td>dept</td><td>pS</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>6723</td><td>clerk</td><td>18K</td><td>toy</td><td>0.2</td></tr><tr><td>6723</td><td>cashier</td><td>20K</td><td>auto</td><td>0.2</td></tr><tr><td>6723</td><td>*</td><td>*</td><td>*</td><td>0.05</td></tr><tr><td>6723</td><td>packer</td><td>*</td><td>*</td><td>0.45</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr></table>

Information Systems Research Vol. 11, No. 1, March 2000

In that case, the new information about an entity need not be confined to just one relation; it may span more than one relation. In other words, the relation scheme may be $R = K X Y \cup \{ p S \}$ , and the new information could be of the form

$$
\begin{array}{c} \text {PROB} [ K = k, X = x _ {i}, Z = z _ {j} ] = q _ {i j}, \\ i = 1, 2, \ldots , m, j = 1, 2, \ldots , l, \end{array}
$$

where the attributes in $Z$ are stored in another relation; $\mathrm { i . e . , } Z \cap ( X Y ) = \emptyset$ . To use this new information to consistently revise the relation, we calculate the appropriate marginal probabilities for the relevant attributes. Thus, to revise a relation r over scheme R, we would only consider the following marginal distribution:

$$
\operatorname{PROB} [ K = k, X = x _ {i} ] = p _ {i} = \sum_ {j = 1} ^ {l} q _ {i j}, i = 1, 2, \dots , m.
$$

Table 6 EMP-Hire-Date Relation

<table><tr><td>EMP#</td><td>hire-date</td><td>pS</td></tr><tr><td>3025</td><td>10/1/93</td><td>0.5</td></tr><tr><td>3025</td><td>11/1/93</td><td>0.5</td></tr><tr><td>6723</td><td>12/7/94</td><td>0.4</td></tr><tr><td>6723</td><td>12/8/94</td><td>0.5</td></tr><tr><td>6879</td><td>11/3/95</td><td>0.3</td></tr><tr><td>6879</td><td>12/3/95</td><td>0.7</td></tr></table>

This distribution can then be used to revise relation r in the previously discussed manner.

Example 4. Assume that the new information is:

$$
\text { PROB } [ \text { EMP } \# = 3 0 2 5, \text { rank } = \text { clerk },
$$

$$
\mathrm{hire-date} = 1 0 / 1 / 9 3 ] = 0. 3,
$$

$$
\text { PROB } [ \text { EMP } \# = 3 0 2 5, \text { rank } = \text { clerk },
$$

$$
\mathrm{hire-date} = 1 0 / 2 / 9 3 ] = 0. 3.
$$

This is used to get the marginal distribution for EMP# and rank as:

$$
\mathsf {P R O B} [ \mathsf {E M P \# = 3 0 2 5 , r a n k = c l e r k} ] = 0. 6.
$$

Since this is the same as the new information in Example 2, the revised EMPLOYEE relation would be as shown in Table 4. We also get a marginal distribution for EMP# and hire-date as:

$$
\mathsf {P R O B} [ \mathsf {E M P \# = 3 0 2 5 , h i r e - d a t e = 1 0 / 1 / 9 3 ] = 0. 3},
$$

$$
\text { PROB } [ \text { EMP\# } = 3 0 2 5, \text { hire - date } = 1 0 / 2 / 9 3 ] = 0. 3.
$$

This information can be applied to revise the relation shown in Table 6. The relation resulting from the proposed revision scheme is shown in Table 7, with the changed tuples italicized.

## 6. Belief Revision Algorithm and its Properties

This section summarizes the revision scheme as an algorithm in Figure 2 and discusses it properties. The algorithm shows how the revision scheme can be embedded in a simple procedure that modifies an existing database given new information. We note that, when the input information spans multiple relations, it should be appropriately marginalized (as discussed in § 5.4) before the algorithm is used.

Table 7 EMP-Hire-Date Relation

<table><tr><td>EMP#</td><td>hire-date</td><td>pS</td></tr><tr><td>3025</td><td>10/1/93</td><td>0.3</td></tr><tr><td>3025</td><td>10/2/93</td><td>0.3</td></tr><tr><td>3025</td><td>11/1/93</td><td>0.4</td></tr><tr><td>6723</td><td>12/7/94</td><td>0.4</td></tr><tr><td>6723</td><td>12/8/94</td><td>0.5</td></tr><tr><td>6879</td><td>11/3/95</td><td>0.3</td></tr><tr><td>6879</td><td>12/3/95</td><td>0.7</td></tr></table>

## 6.1. Complexity Analysis

In this section, we examine the performance characteristics of the algorithm and compare it with the simpler deterministic updating of conventional relations. We consider two cases: (i) all indices necessary for the update operation exist for the relation, and (ii) there is no index for the relation.

Relation Is Indexed. For updating an object in a deterministic relation r, one has to search for its location. The complexity of the search, in the presence of an appropriate index, is O (log |r|) where |r| denotes the number of tuples in r. On the other hand, when updating an object in a probabilistic relation $r , L O O P$ 1 is executed $\mid r _ { k } \mid$ times, where $r _ { k } = \sigma _ { K } = \rho _ { k } \left( r \right)$ is only that portion of the relation that contains information on object k. Within LOOP 1, LOOP 2 is executed m times, where m is the number of incoming tuples. So, the total time requirement is $O ( m \mid r _ { k } \mid )$ . Of course, prior to the execution of these loops, one has to find the locations of the records in $r _ { k } \subset r .$ In the presence of an index, that can be done in O (log |r|) time. Therefore, the overall complexity of the update operation is O(log $\mid r \mid ~ + ~ m \mid r _ { k } \mid )$ . For small values of m or $r _ { k } , $ the performance is, therefore, comparable to the deterministic case. Of course, the additional overhead of disk access and index updating are not considered in this analysis because they will be comparable for both the deterministic and probabilistic relations.<sup>5</sup>

Relation Is Not Indexed. The overall complexity in the deterministic case is clearly O(|r|). For the revision of probabilistic relations, the complexity is O $( \mid r \mid ~ + ~ m \mid r _ { k } \mid )$ . Since, for all practical purposes, |r|  m $\mid r _ { k } \mid$ , we can see that the complexity is the same as a deterministic update.

<sup>5</sup>We assume that probabilistic tuples for the same object (i.e., with the same primary key value) are clustered together. This way, two disk accesses (one for reading and one for writing) would usually be sufficient for updating an object, even though there may be several tuples representing that object.

## Figure 2 Complete Algorithm for Belief Revision in a Probabilistic Relation

```txt
Algorithm: Belief Revision

input: relation r on scheme R; PROB[K = k, X = xi] = pi, i = 1, 2, ..., m.
output: revised relation r.

BEGIN
    for i := 1 to m do
    μi := true;
    for all α ∈ σK=k(r) do { LOOP 1 }
    begin
    found := false;
    r := r - α;
    for i := 1 to m do { LOOP 2 }
    if α(X) = xi then
    begin
    calculate Q from Case 1 [Equation 1];
    μi := false;
    found := true;
    end;
    if not(found) then
    calculate Q from Case 2 [Equation 2];
    if Q > 0 then
    r := r ∪ ⟨k, α(X), α(Y), Q⟩;
    end;
    for i := 1 to m do
    if μi then
    r := r ∪ ⟨k, xi, *, pi⟩;
END.
```

## 6.2. Completeness, Consistency, and Closure

We will now show that the proposed belief revision algorithm is: (i) complete (meaning that it covers all possible modification situations), (ii) consistent with the axioms of probability theory, and (iii) closed (meaning that the use of this algorithm always results in a valid relation). To prove these properties, we will denote the set of new information tuples as I. Also, since only the tuples with K  k are affected, we consider only those tuples in $r _ { k } = \sigma _ { K = k } ( r )$

6.2.1. Completeness. As shown in Figure 3, the set of tuples in $r _ { k }$ can be partitioned into two subsets. In the first subset $r _ { \mathrm { k 1 } }$ , the X-value of a tuple matches with the X-value of a tuple in I. Recall that for each tuple in $r _ { k 1 } ,$ there could be only one such tuple in I, since x’s are distinct. The second subset, $r _ { k 2 } = r _ { k } - r _ { k 1 } ,$ is the set of tuples whose X-values do not match with the X-value of any tuple in I. Similarly, the set I is partitioned into $I _ { 1 }$ and $I _ { 2 } .$ In $I _ { 1 } ,$ the X-value of a tuple matches with the X-value of one or more tuples in $r _ { k } ,$ and $I _ { 2 } = I - I _ { 1 }$ . The algorithm combines $r _ { k 1 }$ and $I _ { 1 }$ into a new set of tuples under Case 1. Case 2 revises the tuples in $r _ { k 2 } .$ . Finally, the tuples in $I _ { 2 }$ are inserted into the revised relation under Case 3. Therefore, all the tuples in $r _ { k }$ and I are covered by the three cases. Further, since X could be an empty set, the algorithm covers the entire range of possibilities from I containing the full joint distribution of all attributes to I containing just the marginal distribution of the primary key. This shows that the algorithm is complete.

6.2.2. Consistency. To prove consistency with the axioms of probability theory, we need to show (i) the probabilities generated by the algorithm are all nonnegative, (ii) the total probability mass assigned to an object is no more than one, and (iii) the total probability assigned to two disjoint sets of tuples for an object is the sum of the probability masses in those two sets for that object. Since the probability numbers generated by Equations (1) and (2) are all nonnegative, the first axiom trivially holds.

To prove the second axiom, consider an object k in the revised relation; we will show that the total probability mass assigned to k is no more than one. To show this, we index the tuples in the partitions of I as $I _ { 1 } =$ $\{ 1 , . . . . , m ^ { \prime } \}$ and $I _ { 2 } = \{ m ^ { \prime } + 1 , . . . , m \}$ . Since, for each tuple $i \in I _ { 1 }$ there could be several tuples in $r _ { k 1 } ,$ we index them as $r _ { k 1 } = \{ i j | i \in I _ { 1 } , j \in T _ { i } \}$ , where $T _ { i } = \{ 1 , . . . , t _ { i } \}$ and $t _ { i } \geq 1$ is the number of tuples in $r _ { k 1 }$ that correspond with $i \in I _ { 1 }$ . Finally, we index $r _ { k 2 }$ as $r _ { k 2 } = \{ 1 , . . . , t \}$ . This indexing scheme is clearly shown in Figure 3.

Set $\pi _ { 1 } ~ = ~ \Sigma _ { i = 1 } ^ { m ^ { \prime } } ~ p _ { i }$ and $\pi _ { 3 } ~ = ~ \Sigma _ { i = m ^ { \prime } + 1 } ^ { m } ~ p _ { i } .$ . Since, for the input data to be consistent, we must have $\Sigma _ { i = 1 } ^ { m } \ p _ { i } \leq$ $1 , \pi _ { 1 } + \pi _ { 3 } \leq 1$ . Further, recall that $P _ { k } = \Pi _ { p S } \left( \sigma _ { K = k } ( r ) \right)$ is the total probability assigned to object k in the original relation; so, $P _ { k } \leq 1$ . Therefore, if we set $\pi _ { 2 } = m a x \{ 0 ,$ $P _ { k } - ( \pi _ { 1 } + \pi _ { 3 } ) \}$ , then $\pi _ { 1 } + \pi _ { 2 } + \pi _ { 3 } \leq 1$ . We can now complete the proof by showing that $\pi _ { j }$ is the total probability assigned to object k after belief revision under Case $j , j = 1 , 2 , 3$

Case 1. Consider a tuple $i j \in r _ { k 1 }$ . The new probability assigned to it can be calculated from Equation (1) as:

$$
Q _ {i j} = \left. p _ {i} q _ {i j} \right/ \sum_ {j = 1} ^ {t _ {i}} q _ {i j}.
$$

The total probability mass assigned under Case 1 is then calculated by summing this over all i and j:

$$
\begin{array}{r l} \sum_ {i = 1} ^ {m ^ {\prime}} \sum_ {j = 1} ^ {t _ {i}} Q _ {i j} & = \sum_ {i = 1} ^ {m ^ {\prime}} \sum_ {j = 1} ^ {t _ {i}} \left(p _ {i} q _ {i j} \Big / \sum_ {j = 1} ^ {t _ {i}} q _ {i j}\right) \\ & = \sum_ {i = 1} ^ {m ^ {\prime}} p _ {i} \left(\sum_ {j = 1} ^ {t _ {i}} q _ {i j} \Big / \sum_ {j = 1} ^ {t _ {i}} q _ {i j}\right) \\ & = \sum_ {i = 1} ^ {m ^ {\prime}} p _ {i} = \pi_ {1}. \end{array}
$$

Case 2. If $P _ { k } \le \pi _ { 1 } + \pi _ { 3 } ,$ then $\pi _ { 2 } = 0$ . In that case, no probability mass is assigned to the tuples under Case $2 ; \mathbf { s o } , \pi _ { 2 }$ is trivially the probability assigned to tuples under Case 2. On the other hand, if $P _ { k } > \pi _ { 1 } + \pi _ { 3 } ,$ then $\pi _ { 2 } = P _ { k } - ( \pi _ { 1 } + \pi _ { 3 } ) $ . The revised probability assigned to a tuple $i \in \boldsymbol { r } _ { k 2 }$ is calculated from Equation (2):

$$
Q _ {i} = q _ {i} \pi_ {2} / \left(P _ {k} - \sum_ {i = 1} ^ {m ^ {\prime}} \sum_ {j = 1} ^ {t _ {i}} q _ {i j}\right).
$$

Since $P _ { k }$ is the total probability mass assigned to object k in the original relation $r _ { k } ,$ we must have:

$$
P _ {k} = \sum_ {i = 1} ^ {m ^ {\prime}} \sum_ {j = 1} ^ {t _ {i}} q _ {i j} + \sum_ {i = 1} ^ {t} q _ {i},
$$

which can be substituted in the previous expression to give:

$$
Q _ {i} = \left. q _ {i} \pi_ {2} \right/ \sum_ {i = 1} ^ {t} q _ {i}.
$$

The total probability assigned to tuples under Case 2 is then found by summing over all tuples i:

$$
\sum_ {i = 1} ^ {t} Q _ {i} = \sum_ {i = 1} ^ {t} \left(q _ {i} \pi_ {2} \bigg / \sum_ {i = 1} ^ {t} q _ {i}\right) = \pi_ {2}.
$$

Case 3. Since the tuples under Case 3 are simply inserted into the revised relation with the same probabilities given in $I _ { 2 } ,$ the total probability mass assigned to object k under Case 3 is $\Sigma _ { i = m ^ { \prime } + 1 } ^ { m } p _ { i } = \pi _ { 3 }$

Finally, to prove the third axiom, denote the revised relation as s. Consider $s _ { 1 } , s _ { 2 } \subset s$ such that $s _ { 1 } \cap s _ { 2 } =$ /.0 We consider the probability distribution of the attributes of object k in $s _ { 1 } \cup s _ { 2 }$ . The total probability assigned to k in $s _ { 1 } \cup s _ { 2 }$ is P $\ L _ { p S } ( \sigma _ { K = k } ( s _ { 1 } \cup s _ { 2 } ) )$ . However, since $s _ { 1 }$ and $s _ { 2 }$ are disjoint, we could write:

$$
\begin{array}{l} \Pi_ {p S} (\sigma_ {K = k} (s _ {1} \cup s _ {2})) = \Pi_ {p S} (\sigma_ {K = k} (s _ {1}) \cup \sigma_ {K = k} (s _ {2})) \\ \qquad = \min \{1, (\Pi_ {p S} (\sigma_ {K = k} (s _ {1})) + \Pi_ {p S} (\sigma_ {K = k} (s _ {2}))) \} \\ \qquad = \Pi_ {p S} (\sigma_ {K = k} (s _ {1})) + \Pi_ {p S} (\sigma_ {K = k} (s _ {2})) \leq 1, \end{array}
$$

the last claim following from the definition of the projection operations and the observation that the sum of the probabilities from $s _ { 1 }$ and $s _ { 2 }$ assigned to k must be no more than one (from the second axiom). This completes the proof.

6.2.3. Closure. To show that the algorithm is closed, we need to prove that, as long as $r _ { k }$ and I are valid relations, the resulting set of tuples is also a valid relation. The algorithm explicitly ensures that only tuples with positive pS-values are inserted. From the proof of consistency, we know that the total probability mass assigned to an object is never more than one. Further, the primary key value cannot become null by applying this algorithm. So, to complete the proof that only valid relations can result from the algorithm, all we need to show is that the revised relation cannot have any value-equivalent tuples. Since, $I _ { 1 } \cap$ $I _ { 2 } \ = \ \varnothing$ and $r _ { k 1 } \cap r _ { k 2 } = \emptyset$ , it is clear that a tuple resulting from Case i cannot be value-equivalent with a tuple resulting from Case j $, i \neq j , i , j = 1 , 2 , 3 .$ . So, if there are two tuples (in the revised relation) that are value-equivalent, both must fall under the same case. Now suppose that two value-equivalent tuples are generated under Case $i , i = 1 , 2 , 3$ . Recall that the belief revision algorithm only changes the $p S \cdot$ -values; other attribute values are not changed. These two tuples, therefore, must have been value-equivalent before the revision. This implies one of the following:

Figure 3 Proof of Completeness and Consistency of the Belief Revision Algorithm  
![](/api/attachments/4VW9PKAD/fulltext/images/8ed4a09084e96cefb7584953ea7bf7876b8bdd34cc0af92b2a8268ed700d27f7.jpg)

• $r _ { k 1 }$ have value-equivalent tuples if the revised tuples are from Case 1,

• $r _ { k 2 }$ has value-equivalent tuples if the revised tuples are from Case 2, or

• $I _ { 2 }$ has value-equivalent tuples if the revised tuples are from Case 3.

This implies that either $r _ { k }$ or I must have valueequivalent tuples and, hence, cannot be a valid relation to begin with.

## 7. Conclusions

Although relational databases enjoy a very widespread popularity in modern business information systems, they lack the ability to model uncertainty in data items. Several extensions of the relational model have been proposed in the literature to this end. However, these extensions overlook a very important aspect of a data model, namely the modification of data items. In a probabilistic database where uncertain data items are stored along with the users’ degree of belief in them, modification of data is equivalent to revision of belief about the data. In this paper, we present a simple scheme for revision of belief in a probabilistic database based on the Bayesian framework.

We discuss the basic assumptions in applying the Bayesian framework and formally describe an algorithm that updates an existing relation based on the user’s input. Modification of data in a probabilistic database could arise from two sources: (i) change of state of one or more data items due to some real-world event and (ii) change of degree of belief about one or more data items due to new (better) information. Our revision scheme is general enough to accommodate both types of modifications. The proposed algorithm has been shown to be closed, consistent, and complete.

The modification of a database must address the issue of data redundancy and normalization. In developing the revision algorithm, we have assumed that the attributes in a relation are all mutually dependent. When that is not the case, a significant amount of data redundancy can be eliminated by normalizing them such that each relation scheme represents only dependent attributes. Dependency and normalization theories are well understood for conventional deterministic databases; we are exploring how they can be generalized for probabilistic databases.

The storage requirement for probabilistic data could be substantially higher than the conventional data. However, their storage provide the user with better information for decision support. Thus, this issue is inherently one of a trade-off between the cost of storing probabilistic data and the value of these data to the user. This issue will become increasingly important in situations such as development of data warehouses that consolidate data from heterogeneous sources; statistical analyses have yet to find a way into such consolidation processes. Future research will examine how the above-mentioned trade-off can be modeled to best support the user’s goals.

Acknowledgments. A preliminary version of this work was presented at the International Conference on Information Systems (ICIS), Cleveland, December 1996. We wish to thank Amit Basu at Vanderbilt University and Veda Storey at Georgia State University for their helpful comments on an earlier draft. We also wish to acknowledge the helpful comments and suggestions from Arie Segev, the associate editor, and the anonymous reviewers of Information Systems Research.

## References

Barbara´, D., H. Garcia-Molina, D. Porter. 1992. The management of probabilistic data. IEEE Trans. Knowledge and Data Engrg. 4(5) 487–502.

Bischoff, J., T. Alexander. 1997. Data Warehouse: Practical Advice from the Experts. Prentice-Hall, Upper Saddle River, NJ.

Cavallo, R., M. Pittarelli. 1987. The theory of probabilistic databases. Proc. 13th VLDB Conf. Brighton, 71–81.

Codd, E. F. 1979. Extending the database relational model to capture more meaning. ACM Trans. Database Systems 4(4) 397–434.

Date, C. J. 1986. Relational Database: Selected Writings. Addison-Wesley, Reading, MA.

Dey, D., S. Sarkar. 1996. A probabilistic relational model and algebra. ACM Trans. Database Systems 21(3) 339–369.

Jaynes, E. T. 1968. Prior probabilities. IEEE Trans. Systems Sci. Cybernetics, SSC-4(3) 227–241.

Jeffrey, R. 1983. The Logic of Decision. University of Chicago Press, Chicago, IL.

Motro, A. 1990. Accommodating imprecision in database systems: Issues and solutions. Database Engrg. 9 213–218.

Neapolitan, R. E. 1990. Probabilistic Reasoning in Expert Systems: Theory and Algorithms. John Wiley and Sons, New York.

Pearl, J. 1986. Fusion, propagation, and structuring in belief networks. Artificial Intelligence, 29 241–288.

——. 1988. Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference. Morgan Kaufmann, San Mateo, CA.

Raju, K. V. S. V. N., A. K. Majumdar. 1988. Fuzzy functional dependencies and lossless join decomposition of fuzzy relational database systems. ACM Trans. Database Systems 13(2) 129–166.

Tseng, F. S. C, A. L. P. Chen, W. -P. Yang. 1993. Answering heterogeneous database queries with degrees of uncertainty. Distributed and Parallel Databases: Internat. J. 1(3) 281–302

Ullman J. D. 1988. Principles of Database and Knowledge-base Systems (Volume I: Classical Database Systems). Computer Science Press, Rockville, MD.
