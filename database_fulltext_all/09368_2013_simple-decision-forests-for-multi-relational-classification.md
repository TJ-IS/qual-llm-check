---
otero_id: 9368
otero_key: "RB9KGWQP"
title: "Simple decision forests for multi-relational classification"
authors: "Bahareh Bina; Oliver Schulte; Branden Crawford; Zhensong Qian; Yi Xiong"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Simple decision forests for multi-relational classi<sup>fi</sup>cation

Bahareh Bina, Oliver Schulte ⁎, Branden Crawford, Zhensong Qian, Yi Xiong

School of Computing Science, Simon Fraser University, Burnaby, B.C., Canada V5A 1S6

## a r t i c l e i n f o

Article history: Received 30 November 2011 Received in revised form 20 September 2012 Accepted 25 November 2012 Available online 3 December 2012

Keywords: Link-based classification Multi-relational Naive Bayes classi<sup>fi</sup>ers Multi-relational decision trees Logistic regression

## a b s t r a c t

An important task in multi-relational data mining is link-based classi<sup>fi</sup>cation which takes advantage of attributes of links and linked entities, to predict the class label. The relational Naive Bayes classi<sup>fi</sup>er exploits independence assumptions to achieve scalability. We introduce a weaker independence assumption to the effect that information from different data tables is independent given the class label. The independence assumption entails a closed-form formula for combining probabilistic predictions based on decision trees learned on different database tables. Logistic regression learns different weights for information from different tables and prunes irrelevant tables. In experiments, learning was very fast with competitive accuracy.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Most real-world structured data are stored in the relational format, with different types of entities and information about their attributes and links between the entities. Relational data classi<sup>fi</sup>cation is the problem of predicting a class label of a target entity given information about features (attributes) of the entity, of the related entities, and of the links. One of the issues that makes link-based classi<sup>fi</sup>cation dif<sup>fi</sup>cult compared to single-table learning is the large number of different types of dependencies that a model may have to consider [19,42]. A principled way to approach the complexity of correlation types is to consider model classes with explicitly stated independence assumptions. The aim is to make a good trade-off between the expressive power of the model on the one hand, and the scalability of learning on the other. Multi-relational Naive Bayes net classi<sup>fi</sup>ers (NBCs) are a prominent example of this approach [8,29,31]. Naive Bayes Classi<sup>fi</sup>ers incorporate two different kinds of independence assumptions: (1) cross-table independence, roughly that information from different tables is independent given the target class label, and (2) within-table independence, that descriptive attributes from the same table are independent given the target class label. The approach of this paper is to maintain the <sup>fi</sup>rst assumption, but to drop the second one. This allows us to capture and exploit complex dependencies among the attributes and the class label within each table.

## 1.1. The classification model

The target table is the table that contains the class attribute. Consider the set of tables that can be joined to the target table via a chain of foreign key links; we refer to the corresponding table joins as join tables. We de<sup>fi</sup>ne a cross-table Naive Bayes assumption, according to which different join tables are independent given the class label, and mathematically derive from it a novel log-linear classi<sup>fi</sup>cation formula. We extend the log-linear classi<sup>fi</sup>cation model to allow different join tables to contribute more or less strongly to the classi<sup>fi</sup>cation decision, with weights for the relative contributions learned by a logistic regression algorithm. Zero weights can be used to prune irrelevant tables.

## 1.2. Simple decision forests

We use a decision tree classi<sup>fi</sup>er as a base learner for dependencies within a single table, for the following reasons. (1) Decision tree learners are very fast. (2) There are well-researched methods for learning trees that provide class probability estimates in their leaves [12,23,34,44]. Such trees are sometimes called probability estimation trees; in this paper, we use the simpler term decision tree. (3) Other multi-relational decision tree classi<sup>fi</sup>ers are available for comparison. (4) Decision trees easily handle continuous and categorical variables. (5) Decision trees support rule learning, and conversion to logic-based relational models, such as Markov Logic Networks [9]. (6) Decision trees are one of the most popular classi<sup>fi</sup>ers. Brydon and Gemino describe applications of decision trees in decision support and business intelligence [6]. An empirical comparison shows a large run-time advantage and a strong predictive performance, that is better than that of previous relational decision tree learners, and of a relational Naive Bayes classi<sup>fi</sup>er.

## 1.3. Contributions

The main novel contributions of our work are as follows.

1. Use of Naive Bayes assumption across tables but not within tables.

2. Use of logistic regression to assign weights for the contributions from different linked tables, including zero weights for pruning.

3. A new method, based on independence assumptions, for upgrading a single-table decision tree classi<sup>fi</sup>er for multi-relational classi<sup>fi</sup>cation.

4. An experimental evaluation on <sup>fi</sup>ve real life databases, demonstrating that our method is very fast with good predictive accuracy.

## 1.4. Paper organization

We <sup>fi</sup>rst describe related work, review background material and de-<sup>fi</sup>ne our notation. Then we formalize the independence assumptions for multi-relational learning and derive the classi<sup>fi</sup>cation formula. We describe the simple forest induction, use of logistic regression, and classi<sup>fi</sup>cation algorithms. The <sup>fi</sup>nal section evaluates the classi<sup>fi</sup>cation performance of the different models on <sup>fi</sup>ve benchmark datasets.

## 2. Related work

We selectively describe relevant multi-relational classi<sup>fi</sup>cation approaches.

## 2.1. Feature generation

Most of the work on relational upgrades of single-table classi<sup>fi</sup>ers uses a mechanism for relational feature generation. Feature generation is done by using aggregate functions to summarize the information in links [1,24,26,32,41]. Inductive Logic Programming (ILP) approaches use existentially quanti<sup>fi</sup>ed logical rules [27,43]. Several recent systems combine both aggregation and logical conditions (e.g., [1,41]). Treeliker is a recent propositionalization system that uses monotonicity properties to generate non-redundant conjunctive features, with state-of-the-art ef<sup>fi</sup>ciency performance [26]. The generated features can be used by any propositional learner. The predictors in our model are not derived features, but the descriptive attributes as de<sup>fi</sup>ned in the relational database schema.

Relational feature generation is by far the most computationally demanding part of such approaches. (For an example, generating 100,000 features on the CiteSeer dataset, which is smaller than the databases we consider in this paper, can take several CPU days ([1], Ch. 16.1.2)). Models that use independence assumptions rather than generated features to combine the information from different tables are orders of magnitude faster to learn, as our experiments con<sup>fi</sup>rm. At the end of the paper we discuss how our approach can be extended to support aggregate feature generation.

## 2.2. Relational decision trees

To our knowledge, all previous work on relational decision trees has followed the propositionalization/aggregation paradigm (e.g., [4,32,41]).

We do not utilize aggregate functions or existential quanti<sup>fi</sup>cation (which may be viewed as an aggregation mechanism). Instead, we consider each link independently and utilize all the information from them. Using aggregation/quanti<sup>fi</sup>cation implies loss of information [8].

FORF (First Order Random Forest) learns an ensemble of different decision trees, each of which is constructed using a random subset of the schema features [41]. Nodes of the trees are <sup>fi</sup>rst-order logic queries.

First order random forests can be categorized according to different levels of aggregation. FORF-NA is the simplest one with no aggregation function. FORF-SA uses simple aggregation, and FORF-RA employs re-<sup>fi</sup>nements of aggregate queries. The <sup>fi</sup>nal decision is made by averaging the results of trees. In contrast, in our model we learn different trees using all attributes of each table. Attributes within a table are typically more correlated than attributes from different tables, so it is advantageous to learn trees from each table's attributes jointly than on random subsets of features. We combine the results using the weights learned by logistic regression rather than plain averaging.

TILDE (top-down induction of <sup>fi</sup>rst-order logical decision tree) is a prominent relational decision tree within the Inductive Logic

Programming framework [4]. The nodes in TILDE trees test <sup>fi</sup>rst-order conditions. The trees are learned with a divide and conquer algorithm similar to C4.5 [35]. The main difference with our model is that Tilde uses the existential quanti<sup>fi</sup>er to build rules. Runtime ef<sup>fi</sup>ciency is a challenge in Tilde, because it potentially generates many rules to <sup>fi</sup>nd the best ones.

MRDT (Multi Relational Decision Tree) constructs the decision tree by using selection graphs as the nodes of the tree [2]. A selection graph is a directed graph which imposes a set of constraints on incorporating information from several tables. MRDT use the existential quanti<sup>fi</sup>er to aggregate information from different links. Guo et al. in [16] speed up the MRDT algorithm by using id propagation to implement a virtual join operation that avoids the cost of physical joins.

## 2.3. Independence assumptions

There are various proposals to apply Naive Bayes (NB) Assumptions and logistic regression (LR) to relational data. Logistic regression can be viewed as a discriminative version of the generative Naive Bayes Classi-<sup>fi</sup>er model [33]. For single-table classi<sup>fi</sup>cation, the advantages of logistic regression over simple Naive Bayes Classi<sup>fi</sup>er have been studied in detail [33], and similar results have been reported for single-relation classi<sup>fi</sup>- cation [28]. Popescul and Unger combine logistic regression with an expressive feature generation language based on SQL queries [1].

Much of the work on relational Naive Bayes Classi<sup>fi</sup>ers combines <sup>fi</sup>rst-order features de<sup>fi</sup>ned by logical rules [7,13,27]. The nFOIL system utilizes the Naive Bayes assumption to learn existentially quanti<sup>fi</sup>ed <sup>fi</sup>rst-order features. Neville et al. [31] investigate different functions for aggregating the in<sup>fl</sup>uence of linked objects. Chen et al. discuss the pros and cons of using aggregation vs. independence assumptions, and argue that for a relational Naive Bayes Classi<sup>fi</sup>er, the use of aggregate function loses statistical information and is not necessary [8]. The multi-relational Naive Bayes Classi<sup>fi</sup>er assumes that all attributes in a database are independent, including attributes from the same table [8]. We use a weaker assumption by learning decision trees for attributes within the tables.

CrossMine [43] is an ef<sup>fi</sup>cient ILP-style rule learner algorithm. It uses tuple ID propagation to virtually join tables, and randomly selects instances to overcome the skewness of datasets.

Structured logistic regression treats the in<sup>fl</sup>uence on the class label of the target table and that of linked tables as independent [28]. Two independent logistic regressions are carried out, one on the target table and the other on the set of linked tables. Information from links is summarized using aggregate functions. The product of the results determines the class label. In our method we use a stronger assumption that links are independent of each other, and learn a model for each link separately. The predictors in our model are probabilities predicted based on local information rather than aggregates as in structured logistic regression.

The Heterogeneous Naive Bayes classi<sup>fi</sup>er [29] considers join tables conditionally independent, and combines the posterior results from the table classi<sup>fi</sup>ers applied separately to linked and target tables by a naive Bayes assumption. A key difference is the classi<sup>fi</sup>cation model: We formally derive our classi<sup>fi</sup>cation formula, which normalizes the posterior probability from each linked table by the class prior. Also, we use decision trees, and we employ logistic regression to combine the contributions of different linked tables.

## 2.4. Ensemble classifiers

Our model has some resemblance to ensemble/committee classi<sup>fi</sup>ers in that we combine the probabilistic outputs of different classi<sup>fi</sup>ers. The main differences are as follows.

1. Most ensemble methods grow the set of classi<sup>fi</sup>ers, e.g., a decision forest, dynamically in the course of learning. In a simple decision forest, the set of decision trees is fixed by the database schema, since each tree represents a classi<sup>fi</sup>er for a given relational pathway (chain of foreign key links).

2. In many ensemble models, gating functions are learned that assign different classi<sup>fi</sup>ers to different parts of the input feature space. In our simple decision forest, the partition of the input feature space is predetermined by the database schema.

3. There are potentially many methods for combining the predictions of a classi<sup>fi</sup>er ensemble [3,25]. Our cross-table Naive Bayes independence assumption entails a log-linear combining method.

## 2.5. Graphical models

Ideas from directed graphical models are used by Probabilistic Relational Models [15], which learn a Bayesian network model of the data distribution, and use aggregate functions to specify conditional probability tables.

Unlike directed graphical models which impose an acyclicity constraint, undirected ones do not have a cyclicity problem and are widely used for LBC [9,18,39]. Two major formalisms are relational conditional Markov random <sup>fi</sup>elds [39] and Markov Logic Networks (MLNs) [9]. Relational Markov random <sup>fi</sup>elds are a general log-linear model that does not use aggregate functions nor independence assumptions [9]. The classi<sup>fi</sup>cation formula we derive from the cross-table Naive Bayes assumption is also a log-linear model, which shows that our model is a subclass of relational conditional random <sup>fi</sup>elds. This observation provides a probabilistic interpretation of our classi<sup>fi</sup>cation formulas in terms of a general graphical model. While compared to general Markov models, the expressive power of our log-linear model is restricted by independence assumptions, the trade-off for the expressive power of more general log-linear models is higher complexity in learning; various studies have shown that scaleable learning is a major challenge for Markov model learning in the multi-relational setting [18,22,37].

In practice one often needs to perform collective classi<sup>fi</sup>cation: predict the class label of several interrelated entities simultaneously. While collective classi<sup>fi</sup>cation has received much attention [20,39], our theoretical framework for multi-relational classi<sup>fi</sup>cation formulas is already quite rich, so our empirical evaluation focuses only on individual classi-<sup>fi</sup>cation and leaves applications to collective classi<sup>fi</sup>cation for future work. A principled approach to collective classi<sup>fi</sup>cation is to convert decision forests to Markov Logic Networks, as described in Section 2, and then apply MLN techniques for collective classi<sup>fi</sup>cation [9].

## 3. Preliminaries and notation

A standard relational schema contains a set of tables. A database instance speci<sup>fi</sup>es the tuples contained in the tables of a given database schema. If the schema is derived from an entity-relationship model ([40], Ch. 2.2), the tables in the relational schema can be divided into entity tables and relationship tables. Relationship tables link Entity tables to each other by foreign key pointers.

The natural join of two tables is the set of tuples from their cross product that agree on the values of <sup>fi</sup>elds common to both tables.

## 3.1. Pathways and join tables

One of the key challenges in multi-relational classi<sup>fi</sup>cation is the multiplicity of pathways or table joins through which the target entity may be linked to other entities. Han et al. [8] proposed a graphical way to structure the space of possible pathways.

A Semantic Relationship Graph (SRG) for a database is a directed acyclic graph (DAG) whose nodes are database tables in and whose only source (starting point) is the target table T. For simplicity we assume that the target table is an entity table. If an edge links two tables in the Semantic Relationship Graph, then the two tables share at least one primary key.

For each path $T , T _ { 1 } , \ldots , T _ { k }$ in a Semantic Relationship Graph, there is a corresponding valid join T⋈ $T _ { 1 } . . . \ J { \bowtie } T _ { \mathrm { k } }$

Because the number of attributes in a valid join may become quite large, Han et al. use only the attributes of the last table in the path, and the class attribute from the target table, which is called propagating the class attribute along the join path [8]. An extended database is a database that contains all valid join tables with selecting (projecting) the class attribute and attributes from the last table in each join. We refer to the tables in the extended database as extended join tables, or simply join tables. A decision tree for an extended join table contains nodes labeled with attributes from the join table. The leaves contain a probability distribution over the class labels. A simple decision forest contains a decision tree for each join table in the extended database.

## 3.1.1. Example

A university schema is our running example. The Semantic Relationship Graph is shown in Fig. 1. The schema has three entity tables: Student, Course and Professor, and two relationships: Registration records Courses taken by each Student and RA records research assistantship of students for professors. An instance for this schema is given in Fig. 2. The class attribute is Intelligence of a Student. Therefore, in the Semantic Relationship Graph we have Student table as the source node. Fig. 3 shows an extended university database instance that results from propagating the class attribute Intelligence. The paths in the Semantic Relationship Graph of Fig. 1 correspond to join tables in Fig. 3.

In the extended university database valid joins include the following:

• Student⋈Registration with (a projection of) the attributes from Registration, and the class label from Student (e.g., Intelligence of Student).

• Student⋈Registration⋈Course, with (a projection of) the attributes from Course, and the class label from Student.

• Student⋈RA, with (a projection of) the attributes from RA, and the class label from Student.

• Student⋈RA⋈Professor, with a selection of the attributes from Professor, and the class label from Student.

Fig. 4 shows a simple decision tree for the extended join table Student⋈RA⋈Prof table that may be learned from data like that shown in Fig. 3.

## 3.2. Model conversions

We discuss how decision forests can be converted to other model types. If knowledge discovery is the goal of data analysis, the rule format provides an accessible presentation of statistical regularities for users. Simple decision forests support rule extraction because each join table corresponds to a Semantic Relationship Graph path. For each table decision tree, each branch converts to a rule in the usual way (conjunction of conditions along the branch). The relational context in which the rule holds is speci<sup>fi</sup>ed by the join conditions of the table. Fig. 4 (right) provides an example.

Markov Logic Networks (MLNs) are a prominent statistical–relational model class that combines <sup>fi</sup>rst-order logic with Markov random <sup>fi</sup>elds (undirected graphical models) [9]. An MLN comprises a set of weighted <sup>fi</sup>rst-order clauses. In terms of graphical models, an MLN is a template for a Markov random <sup>fi</sup>eld, with a log-linear likelihood function that is the weighted sum of counts of features de<sup>fi</sup>ned by the <sup>fi</sup>rst-order formulas. A state-of-the-art approach to learning the clauses in an MLN is to <sup>fi</sup>rst learn a set of decision trees and then convert each branch of each decision tree to an MLN clause [21,22]. The weights of the clauses are obtained from probability estimation trees by using the log-conditional probabilities associated with a leaf [21], and from regression trees by using the regression weights [22]. The example rule from Fig. 4 (right) would induce the MLN clause

![](/api/attachments/RB9KGWQP/fulltext/images/7677c89823eccd444945ca35e1c9fe12f5bf5ece5fb5671b75733917b45b928f.jpg)  
Fig. 1. Semantic relationship graph for the university schema. Each path in the Semantic Relationship Graph corresponds to a join table in the extended database.

<table><tr><td colspan="3">Course</td><td colspan="3">Student</td><td colspan="3">Professor</td></tr><tr><td rowspan="2">c-id</td><td rowspan="2">Rating</td><td rowspan="2">Difficulty</td><td>s-id</td><td>Intelligence</td><td>Ranking</td><td rowspan="2">p-id</td><td rowspan="2">Popularity</td><td rowspan="2">Teaching-a</td></tr><tr><td>Jack</td><td>?</td><td>1</td></tr><tr><td>101</td><td>3</td><td>1</td><td>Kim</td><td>2</td><td>1</td><td>Oliver</td><td>3</td><td>1</td></tr><tr><td>102</td><td>2</td><td>2</td><td>Paul</td><td>1</td><td>2</td><td>Jim</td><td>2</td><td>1</td></tr></table>

![](/api/attachments/RB9KGWQP/fulltext/images/c0f5f2514293c27c5625b6964a808f998c1e62863e559b49a46eb58de8131c9e.jpg)

<table><tr><td colspan="4">Registration</td></tr><tr><td>s-id</td><td>c.id</td><td>Grade</td><td>Satisfaction</td></tr><tr><td>Jack</td><td>101</td><td>A</td><td>1</td></tr><tr><td>Jack</td><td>102</td><td>B</td><td>2</td></tr><tr><td>Kim</td><td>102</td><td>A</td><td>1</td></tr><tr><td>Paul</td><td>101</td><td>B</td><td>1</td></tr></table>

<table><tr><td colspan="4">RA</td></tr><tr><td>s-id</td><td>p-id</td><td>Salary</td><td>Capability</td></tr><tr><td>Jack</td><td>Oliver</td><td>High</td><td>3</td></tr><tr><td>Kim</td><td>Oliver</td><td>Low</td><td>1</td></tr><tr><td>Paul</td><td>Jim</td><td>Med</td><td>2</td></tr></table>

Fig. 2. A small instance of a university database.

RA S; P ; TeachingA P; 1 ; Intelligence S; 2 : w ln 100% :

For general discussion and details on MLNs and the conversion from decision forests to MLNs please see [21,22]. The conversion to Markov Logic Networks provides a probabilistic foundation for our classi<sup>fi</sup>cation approach in terms of log-linear models, and offers a principled approach to collective classi<sup>fi</sup>cation with the cross-table Naive Bayes assumption (see Section 2).

## 4. The cross-table Naive Bayes assumption

In this section we de<sup>fi</sup>ne our independence assumption formally and derive a classi<sup>fi</sup>cation formula. The formula entails a logistic regression model for multi-relational classi<sup>fi</sup>cation. Applying the regression to decision trees de<sup>fi</sup>nes the simple decision forest classi<sup>fi</sup>cation model.

## 4.1. Independence assumptions

In the de<sup>fi</sup>nitions below, we view a table $M _ { i }$ as a conjunction of the information pieces in it, that is, as a conjunction of value assignments. We write $M _ { i , r }$ for the tuple of values in row r of table M without the primary key(s). For example, suppose that M<sub>i</sub> is the Student⋈Registration⋈ Course table from Fig. 3. Then $M _ { i , 1 } = < 3 , 1 , ? >$ and $M _ { i , 3 } = < 2 , 2 , 2 >$

De<sup>fi</sup>nition 1. Consider an extended database with target table T, containing class attribute c and non-class attributes a, and join tables $J _ { 1 } , \dots J _ { m } .$ . The Inter-Table Independence Principle states that

$$
P (T, J _ {1}, \dots , J _ {m} | c) = P (\mathbf {a} | c) \prod_ {i = 1} ^ {m} \prod_ {r = 1} ^ {\text { rows } _ {i}} P \left(J _ {i, r} | c\right).\tag{1}
$$

For instance, we may have t=jack, c=Intelligence and a={Ranking}, so a(jack)=b1>.

4.1.1. Discussion

<table><tr><td colspan="3">Student</td></tr><tr><td>s-id</td><td>Intelligence</td><td>Ranking</td></tr><tr><td>Jack</td><td>?</td><td>1</td></tr><tr><td>Kim</td><td>2</td><td>1</td></tr><tr><td>Paul</td><td>1</td><td>2</td></tr></table>

Eq. (1) says that, conditional on the class label, the probability of the extended database instance is the product of the probability of the target attributes with the probabilities of each row of each join table. This assumption combines two principles, which we separate for discussion.

First, that the information in different tables is independent given the class label:

$$
P (T, J _ {1}, \dots , J _ {m} | c) = P (\mathsf {a} | c) \prod_ {i = 1} ^ {m} P (J _ {i} | c)\tag{2}
$$

and second, that the information in different rows is independent given the class label, for each table i with rows rows:

$$
P (J _ {i} | c) = \prod_ {r = 1} ^ {\text { rows } _ {i}} P \left(J _ {i, r} | c\right).\tag{3}
$$

<table><tr><td colspan="5">Student→Registration→Course</td></tr><tr><td>s-id</td><td>c.id</td><td>Rating</td><td>Diff</td><td>Intelligence</td></tr><tr><td>Jack</td><td>101</td><td>3</td><td>1</td><td>?</td></tr><tr><td>Jack</td><td>102</td><td>2</td><td>2</td><td>?</td></tr><tr><td>Kim</td><td>102</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Paul</td><td>101</td><td>3</td><td>1</td><td>1</td></tr></table>

<table><tr><td colspan="5">Student=RA=Prof</td></tr><tr><td>s-id</td><td>p-id</td><td>Popularity</td><td>Teaching-a</td><td>Intelligence</td></tr><tr><td>Jack</td><td>Oliver</td><td>3</td><td>1</td><td>?</td></tr><tr><td>Kim</td><td>Oliver</td><td>3</td><td>1</td><td>1</td></tr><tr><td>Paul</td><td>Jim</td><td>2</td><td>1</td><td>2</td></tr></table>

<table><tr><td colspan="5">RA</td></tr><tr><td>s-id</td><td>p-id</td><td>Salary</td><td>Capability</td><td>Intelligence</td></tr><tr><td>Jack</td><td>Oliver</td><td>High</td><td>3</td><td>?</td></tr><tr><td>Kim</td><td>Oliver</td><td>Low</td><td>1</td><td>2</td></tr><tr><td>Paul</td><td>Jim</td><td>Med</td><td>2</td><td>1</td></tr></table>

<table><tr><td colspan="5">Registration</td></tr><tr><td>s-id</td><td>c.id</td><td>Grade</td><td>Satisfaction</td><td>Intelligence</td></tr><tr><td>Jack</td><td>101</td><td>A</td><td>1</td><td>?</td></tr><tr><td>Jack</td><td>102</td><td>B</td><td>2</td><td>?</td></tr><tr><td>Kim</td><td>102</td><td>A</td><td>1</td><td>2</td></tr><tr><td>Paul</td><td>101</td><td>B</td><td>1</td><td>1</td></tr></table>

Fig. 3. An instance of the extended university database. The target entity is Jack, the target table is Student, and the class label is Intelligence.

![](/api/attachments/RB9KGWQP/fulltext/images/14c63dcdc537cab5e3a772f2e51c6db4ed0e78f6137d89d9b8b4323de4a9d90e.jpg)  
Fig. 4. Left: A simple single decision tree that may be learned for data in the format of the extend join table Student RA Prof table. Right: a logical rule extracted from the tree, corresponding to the leftmost branch.

It is easy to see that Assumptions (2) and (3) entail the Inter-Table Independence Principle (1). Fig. 5 illustrates Assumption (2) for the university schema using a Bayesian network.

Since the class attribute is propagated to all join tables, table independence requires conditioning on this common information. This is an instance of the general principle that structured objects may become independent if we condition on their shared components. For instance, in Fig. 3 the join tables Student–Registration–Course and Student–RA–Prof both share the information about the intelligence of students.

Assumption (3) says that, given the common class label, rows of the link table join are independent of each other. This assumption is required to apply a single table classi<sup>fi</sup>er to each extended table. For instance, in Fig. 3 two rows in the Registration table with the same student-id both share the information about the intelligence of the student.

Examples. Consider the extended university database from Fig. 3 with the four join tables as shown. Then by Assumption (2), the joint probability of the database instance conditional on the class label factors as

$$
\begin{array}{c} P (T, J _ {1}, J _ {2}, J _ {3}, J _ {4} | \text {Intelligence} (j a c k) = 2) = \\ P (\text {Ranking} (j a c k) = 1 | \text {Intelligence} (j a c k) = 2) \cdot \\ P (\text {Student - Registration} | \text {Intelligence} (j a c k) = 2) \cdot \\ P (\text {Student - Registration - Course} | \text {Intelligence} (j a c k) = 2) \cdot \\ P (\text {Student - RA} | \text {Intelligence} (j a c k) = 2) \cdot \\ P (\text {Student - RA - Prof} | \text {Intelligence} (j a c k) = 2) \end{array}
$$

where the expression attribute(jack)=2 denotes that the attribute value for target entity jack is 2.

Applying the Assumption (3) to the join table J = Student − Registration − Course we have

P Student−Registration−Course Intelligence jack 2 P Rating 101 3; Dif f 101 1 Intelligence jack 2 ⋅ P Rating 102 2; Dif f 102 2 Intelligence jack 2

where the expression attribute(course) = x denotes that the attribute value for course course is x. Rows that do not contain the target entity jack are not included in the equation.

Multi-relational Naive Bayes (NB) classi<sup>fi</sup>ers [8] add yet another assumption: the Column Independence Principle that within each row of each join table, the attributes are independent given the class label, which amounts to applying the single-table NB classi<sup>fi</sup>er in each join table.

Using only Inter-Table Independence adds a degree of freedom that allows us to apply a classi<sup>fi</sup>er other than single-table NB to the join tables. Data from the same table is more likely to be correlated than data from different tables, because the database designer groups related attributes within a table. Thus by not assuming Column Independence, we exploit the domain knowledge implicit in the database design.

## 4.1.2. Impact of assumption

We emphasize that we do not claim that the Inter-Table Independence Assumption is exactly true in a given database. For example, if we know that Jack is an intelligent student, the row independence principle (3) implies that his grades in course 101, and his grades in course 102, are independent of each other. There will in general be dependencies among different links/link attributes of the same entity. Therefore in a given dataset, these assumptions may not be entirely but only approximately true. The use of relational independence principles is best viewed as a simplifying approximation to the actual dependencies in the dataset. Like the non-relational Naive Bayes assumption, the assumption permits accurate predictions of an entity's attributes even when false [10]. Another view is that it represents which correlations are modeled: Namely correlations between attributes and the class label given the link structure, but not correlations among the links or among the attributes of non-target entities.

Analogously, the Naive Bayes assumption allows a model to present correlations between features and the class label in a single table, but not correlations among the features. As our experiments illustrate, the assumption leads to highly scalable learning, while it allows a model to capture the most relevant correlations from the data. To develop a learning algorithm and to investigate the impact of the assumption empirically, we derive a classi<sup>fi</sup>cation formula from it.

## 5. The multi-relational classi<sup>fi</sup>cation model

Let t denote the target entity from table T, such that c(t) is the target class label and a(t) its non-class features.

For simplicity we assume a binary class label, so c(t) ∈{0,1}; our derivation can be extended to multi-class problems. Given a testing example (all the information in the extended tables) the posterior class odds are given by:

$$
\frac {P (c (t) = 0 | T , J _ {1} , \dots , J _ {m})}{P (c (t) = 1 | T , J _ {1} , \dots , J _ {m})} = \frac {P (T , J _ {1} , \dots , J _ {m} | c (t) = 0) P (c (t) = 0)}{P (T , J _ {1} , \dots , J _ {m} | c (t) = 1) P (c (t) = 1)}.
$$

![](/api/attachments/RB9KGWQP/fulltext/images/2413bcb1deb2be48c639d9fc9c566f3a75d67eed678a6916b567ac2f071568a0.jpg)  
Fig. 5. An example of the Table Independence Principle in the university domain. Attributes of different tables extended by the class label are independent of each other given the class label.

The class label is 0 if the posterior odds is larger than 1 and 1 otherwise. Applying the Inter-Table Independence Assumption (1), we have:

$$
= \frac {P (c (t) = 0) P (\mathsf {a} (t) | c (t) = 0) \prod_ {i = 1} ^ {m} \prod_ {r = 1} ^ {\text { rows } _ {i}} P \left(J _ {i , r} | c (t) = 0\right)}{P (c (t) = 1) P (\mathsf {a} (t) | c (t) = 1) \prod_ {i = 1} ^ {m} \prod_ {r = 1} ^ {\text { rows } _ {i}} P \left(J _ {i , r} | c (t) = 1\right)}
$$

where rows is the number of rows in join table $J _ { i \cdot }$ Substituting posterior probabilities using Bayes' theorem leads to the <sup>fi</sup>nal classification formula:

$$
= \frac {P (c (t) = 0 | a (t))}{P (c (t) = 1 | a (t))} \prod_ {i = 1} ^ {m} \prod_ {r = 1} ^ {\text { rows } _ {i}} \frac {P (c (t) = 1)}{P (c (t) = 0)} \cdot \frac {P \left(c (t) = 0 | J _ {i , r}\right)}{P \left(c (t) = 1 | J _ {i , r}\right)}.\tag{4}
$$

## 5.1. The weighted log-linear classification model

We convert the classi<sup>fi</sup>cation formula (4) to a parametrized log-linear model that assigns different weights to information from different database tables.

Adding weight parameters and scale factors to formula (4) leads to our <sup>fi</sup>nal log-linear classification model:

$$
\begin{array}{l} \log \left(\frac {P (c = 0 | T , J _ {1} , \dots , J _ {m})}{P (c = 1 | T , J _ {1} , \dots , J _ {m})}\right) = w _ {0} + w _ {T} \log \left(\frac {P (c (t) = 0 | a (t))}{P (c (t) = 1 | a (t))}\right) \\ \quad + \sum_ {i = 1} ^ {m} \frac {w _ {i}}{\text { rows } _ {i}} \sum_ {r = 1} ^ {\text { rows } _ {i}} \log \left(\frac {P (c (t) = 1)}{P (c (t) = 0)}\right) + \log \left(\frac {P (c (t) = 0 | J _ {i , r})}{P (c (t) = 1 | J _ {i , r})}\right). \end{array}\tag{5}
$$

First, the weighted log of the posterior odds given the information in the target table is computed. Second, for each of the join tables and for each row in it, we compute the log of: the posterior odds, given the attributes of the join table, protect divided by the prior class odds. This quantity measures how much the information from the join table changes the prior probability of a class label. Thirdly, the log-contribution from each extended table is weighted and scaled by the number of its rows. Finally, the weighted log-contributions are added together to predict the class label. Algorithm 12 shows the classi<sup>fi</sup>cation algorithm that corresponds to formula (5).

## 5.1.1. Motivation

A direct application of inter-table independence assigns the same weight for the information obtained from different sources. The weights $w _ { 0 } , w _ { 1 } , . . . , w _ { m }$ adaptively control the impact of information from different links for class prediction.<sup>1</sup>

If an object has a large number of links, the information from links contributes many more terms in Eq. (5) than the target entity's attributes. For example if Jack has taken 6 courses, the information from attributes of Jack, like ranking, is overwhelmed by information about courses. Normalizing the total log-contribution from each table by its size puts the contribution from tables with different sizes on the same scale: This uses the average log-contribution from the rows in a table, rather than the sum total of the log-contributions over all rows in the table. Scaling factors have been previously used with log-linear models [9,36].

## Algorithm 1. Multi-Relational Data Classi<sup>fi</sup>cation

Input

(1) A new target instance t.

(2) Extended data base tables $J _ { 1 } , \ldots , J _ { k } .$

(3) Regression weights $\vec { w } .$

(4) Probabilistic Classi<sup>fi</sup>er $\mathcal { C } _ { T }$ for the target table, $\mathcal { C } _ { i }$ for each extended table.

Output: A predicted class label

1: TP : w<sub>0</sub> w<sub>1</sub>⋅ log <sub>T</sub> c 0 a t − log c 1 a t {Posteriors of the target table}

2: for all (extended tables J<sub>i</sub>) do

$$
3 \colon L P := 0
$$

4: for each (row $J _ { i , r }$ containing the target entity t) do

$$
\begin{array}{l} 5 \text {:} L P + = \log \left(\frac {\mathcal {C} _ {i} \big (c (t = 0) | J _ {i , r} \big) \cdot \mathcal {C} _ {i} (c (t) = 1)}{\mathcal {C} _ {i} \big (c (t = 1) | J _ {i , r} \big) \cdot \mathcal {C} _ {i} (c (t) = 0)}\right) \\ 6 \text {:} e n d   f o r \end{array}
$$

$$
7: T P + = w _ {i} \cdot \frac {1}{r O W S _ {i}} \cdot L P
$$

8: end for

9: if (TP > 0) return 0

10: else return 1.

## 6. Learning decision forests with regression

The log-linear classi<sup>fi</sup>er of Algorithm 12 requires as input three components.

We discuss the construction of each of these components in turn.

(1) For constructing the extended database, in our experimental datasets it suf<sup>fi</sup>ces simply to enumerate the possible valid joins based on Semantic Relationship Graphs and add the corresponding join tables as views to the database. The foreign key constraints keep the space of valid table joins manageable.

(2) For the classi<sup>fi</sup>er C for the join table J , we used probability estimation trees with the Laplace correction and no post-pruning, as recommended by Provost and Domingos [34].

(3) To learn the regression weights for combining the contributions from different table classi<sup>fi</sup>ers, we apply logistic regression as follows. De<sup>fi</sup>ne $b _ { i }$ by

$$
\begin{array}{l} b _ {T} = \log \left(\frac {P (c (t) = 0 | \boldsymbol {a} (t))}{P (c (t) = 1 | \boldsymbol {a} (t))}\right), \\ b _ {i} = \frac {1}{r o w s _ {i}} \sum_ {r = 1} ^ {r o w s _ {i}} \log \left(\frac {P \Big (c (t) = 0 | J _ {i , r} \Big) \cdot P (c (t) = 1)}{P \Big (c (t) = 1 | J _ {i , r} \Big) \cdot P (c (t) = 0)}\right). \end{array}
$$

Then formula (5) can be rewritten as a logistic regression formula (Logit of posterior odds)

$$
\log \left(P \left(\frac {c = 0 | T , J _ {1} , \dots , J _ {m}}{P (c = 1 | T , J _ {1} , \dots , J _ {m})}\right) = w _ {0} + w _ {T} b _ {T} + w _ {1} b _ {1} + \dots + w _ {m} b _ {m}. \right.\tag{6}
$$

The regression model serves to combine the predictions of the different table classi<sup>fi</sup>ers. Whereas there are in general many options for combining classi<sup>fi</sup>er predictions [25], ([3], Ch. 14), the features of the log-linear model (the $b _ { i }$ values) follow from the Inter-Table Independence Assumption of Definition 1.

Algorithm 2. Multi-Relational Simple Decision Forest Induction and meta regression weight learning (implements formula (5))

Input: Extended join tables $J _ { 1 } , \dots , J _ { m } .$

Output:

(1) A forest of decision tree: probabilistic Classi<sup>fi</sup>er $\mathcal { C } _ { T }$ for target table, $\mathcal { C } _ { i }$ for each extended table.

(2) Regression weights w<sup>→</sup>.

Call: decision tree learner DT, and logistic regression weight learner LR

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Fix a training set for DT learning, and a validation set for LR.
2: {Start Decision Trees induction}  $C_{T} :=$  Call DT (target table T).
3: for each table  $J_{i}$  in D do
4:  $C_{i} :=$  Call DT ( $J_{i}$ ).
5: end for
6: {Start Logistic Regression}. Create matrix M with  $m + 1$  columns.
7: for each target object  $t_{k}$  in the validation set with the class label  $c(t_{k})$  do
8:  $M_{k,0} := c(t_{k})$ 
9:  $M_{k,1} := \log(\mathcal{C}_{T}(c(t_{k}) = 0 | a(t_{k})) - \log(\mathcal{C}(c(t_{k}) = 1 | a(t_{k}))$ 
10: for all join tables  $J_{i}$  do
11: LP := 0
12: for each row  $J_{i,r}$  containing the target entity  $t_{k}$  do
13:  $LP + \log\left(\frac{\mathcal{C}_{i}(c(t_{k}) = 0) | J_{i,r}) \cdot \mathcal{C}_{i}(c(t_{k}) = 1)}{\mathcal{C}_{i}(c(t_{k}) = 1) | J_{i,r}) \cdot \mathcal{C}_{i}(c(t_{k}) = 0)}\right)$ 
14: end for
15:  $M_{k,i} := \frac{1}{ROWS_{i}} \cdot LP$ 
16: end for
17: end for
18:  $\vec{w} = \text{Call LR}(M)$ .
</div>

Algorithm 7 describes the model learning phase. First, we divide the learning input data into training and validation set using a division of the original target table. We learn the classi<sup>fi</sup>ers on the training set and the weights on the validation set, to avoid over<sup>fi</sup>tting. In lines 1 to 5 different trees on each table in the extended database are learned. To learn the regression weights, for each instance $t _ { k }$ in the set, feature vectors or independent variables $b _ { 1 } ( t _ { k } ) , . . . , b _ { m } ( t _ { k } )$ are computed. A matrix with one row for each training instance $t _ { k } ,$ one column for the class label c(t ), and one column for each predictor $b _ { i } ( t _ { k } )$ is formed. This matrix is the input for a logistic regression package.

Fig. 6 represents the whole process of classifying relational data using the decision forest.

The run-time complexity of the method is dominated by the cost of applying a decision tree learner to different join tables, which in turn depends essentially on the size of the table joins. Experience with join-based methods [8,29,42] indicates that the table join sizes are manageable, for the following reasons: (i) informative correlations seldom require more than a foreign key path of length 3, which correspond to joins of 3 tables or less. (ii)

The tuple ID propagation technique is an ef<sup>fi</sup>cient virtual join method that <sup>fi</sup>nds the suf<sup>fi</sup>cient statistics for learning without materializing the actual table join [42].

## 7. Evaluation

In this section, we compare different con<sup>fi</sup>gurations of our proposed model with various relational classi<sup>fi</sup>cation models. We describe the datasets, basic setting of our experiments, and results in different evaluation metrics. Our code and datasets are available for anonymous ftp download from ftp://ftp.fas.sfu.ca/pub/cs/oschulte/sdf. The hypotheses we investigate are as follows.

1. That assuming (conditional) independence between only join tables leads to better use of the database information than assuming independence between attributes (as in the multi-relational Naive Bayes classi<sup>fi</sup>er) or randomly selecting attributes.

2. That the induction or learning time of methods making independence assumptions should be much faster than more general methods that do not.

3. That logistic regression applied to the log-contributions of linked tables is an effective way of pruning uninformative tables.

## 7.1. Datasets

We use <sup>fi</sup>ve benchmark real-world datasets. The datasets feature both many-to-many and self-join relationships, as indicated, as well as 2-class and 3-class problems. The semantic relationship graphs for the datasets are depicted in Fig. 7.

## 7.1.1. Financial dataset

This dataset was used in the PKDD CUP 1999. Loan is the target table with 682 instances (606 of loans are successful).

Since 86% of the examples are positive, the data distribution is quite skewed. We followed the modi<sup>fi</sup>cations of Yin and Han [8,43] and randomly selected 324 positive instances, and all the negative loans to make the numbers of positive tuples and negative tuples more balanced.

The number of join tables in the extended database was 8.

## 7.1.2. Hepatitis database

This data is a modi<sup>fi</sup>ed version of the PKDD'02 Discovery Challenge database. We followed the modi<sup>fi</sup>cation of Frank et al. [14]. Biopsy is the target table with 206 instances of Hepatitis B, and 484 cases of Hepatitis C. The number of join tables in the extended database was 4.

## 7.1.3. Mondial database

This dataset contains data from multiple geographical web data sources [30]. We predict the religion of a country as Christian (positive) with 114 instances vs. all other religions with 71 instances. We followed the modi<sup>fi</sup>cation of She et al. [38].

![](/api/attachments/RB9KGWQP/fulltext/images/a045fc4fb762a0b885c819ad03edc98171c3858d153e77227036b489c3b50840.jpg)  
Fig. 6. The process of classifying relational data using the Decision Forest

![](/api/attachments/RB9KGWQP/fulltext/images/aa9d958e2ca8daa4e73f9ae03ab6ac9c1ec56ff4c2c32552b45f547fdab98351.jpg)  
Fig. 7. Semantic relationship graphs: (a) Financial, (b) Hepatitis, and (c) Mondial dataset.

We use a subset of the tables and features. Borders is a many-many relationship between Country and Country. To create an acyclic semantic relationship graph for this database, we duplicated the Country table (cf. [8,43]). The number of join tables in the extended database was 5.

## 7.1.4. MovieLens

This dataset is drawn from the UC Irvine machine learning repository. It contains two entity tables: User with 941 tuples and Item, with 1682 tuples, and one relationship table Rated with 80,000 ratings. The table Item has 17 Boolean attributes that indicate the genres of a given movie. The class label is the user attribute age that we discretized into three bins with equal frequency.

## 7.1.5. JMDB

This is our most complex dataset, containing information from the Internet Movie Database (IMDB), about movies, such as titles, ratings, actors, studios. We obtained it from the IMDB data interface (http:// www.imdb.com/interfaces). The target table is ratings, and the target attribute rank records users, on average, rank a movie on a scale from 1 to 10.

We discretized the ratings into 3 equal-width intervals, and removed movies that had not been ranked by any user, for a total of 281,449 target instances. We omitted textual information, so our original database contained 7 tables, with an additional 6 join tables in the extended database.

## 7.2. Experimental setting, systems, and performance metrics

All experiments were done on a Pentium 4 CPU 2.8 Ghz and 3 GB of RAM system (except for some on the JMDB dataset, see below). The implementation used many of the procedures of the data mining software Weka [17]. We compared the following relational classi<sup>fi</sup>ers. The <sup>fi</sup>rst three are variations of our own framework and the last <sup>fi</sup>ve classi-<sup>fi</sup>ers were developed by other researchers.

• Normalized decision forest: Weighted log linear decision forest with scaling factors (formula (5)).

• Unnormalized decision forest: Weighted log linear decision forest with no scaled weights (formula (5) with rows =1).

• Naive decision forest: Decision forest with no weights for the trees (formula (4)).

• TILDE: First-order decision tree [4].

• FORF-NA: First-order random forest with no aggregates [41].

• Graph-NB: Multi-relational naive Bayes classi<sup>fi</sup>er [8].

• TreeLiker-Relf: A propositionalization algorithm that constructs treelike nonredundant conjunctive features [26]. We apply a decision tree learner to the constructed features.

• TreeLiker-Poly: An extension of TreeLiker that supports the use of aggregate functions for numeric attributes [26].

The datasets MovieLens and JMDB feature class labels with 3 possible values. We used a multinomial logistic regression model, which learns 2 log-odds weight vectors with class 3 as the pivot (log-odds of 1 vs. 3 and log-odds of 2 vs. 3). We converted the log-odds to probabilities using the standard formula for the multinomial logistic regression model, and classi<sup>fi</sup>ed instances according to the resulting probability ranking of classes.

We made use of the following implementations.

• Decision Tree Learning: Weka's J48 as a decision tree learner on each join table. For simple decision forests, we used the probability estimation tree setting that turns off pruning and applies the Laplace correction [34]. We applied the classi<sup>fi</sup>cation tree setting with the features generated by TreeLiker.

• Logistic Regression: The simple logistic regression procedure of Weka.

• Graph-NB: We implemented Graph-NB using the single-table Naive Bayes Classi<sup>fi</sup>er procedure of Weka as the code is not available.

• TreeLiker: We use the code provided by the system creators, available at http://ida.felk.cvut.cz/treeliker/. The minimum frequency parameter is set at the default value 1%.

This design evaluates two different ways of upgrading the same propositional decision tree learner to relational data: using the cross-table Naive Bayes assumption, as in simple decision forests, vs. using propositionalized features, as in Treeliker.

and FORF-NA are included in the ACE data mining system [5]. We ran TILDE with the default setting. For FORF-NA we used bagging, chose 25% of features to consider for testing in each node, and <sup>fi</sup>xed the number of trees in the forest to 33. Vens et al. report that this setting leads to the most ef<sup>fi</sup>cient results in terms of accuracy and running time [41]. As in previous studies [4,8,41], we use a leave-one-out test, where the prediction for each target entity is based on knowledge of all other entities, and we average the predictions over all target entities in the test fold.

For decision forests and Graph-NB, we performed ten-fold crossvalidation to evaluate predictive accuracy. In each run we learn the decision tree on a random 8-fold of data, learn the weights of logistic regression on a 1 fold (validation set), and test the model on the remaining fold.

## Table 1

Average induction time of different algorithms in seconds. Normalized and Unnormalized Decision Forests use logistic regression to learn weights for join tables. NT denotes nontermination after 4 days of running. The TreeLiker results on JMDB were obtained on a high-performance cluster, as described in the text. Numbers in bold indicate the top score.

<table><tr><td>Learning time</td><td colspan="3">Simple decision forest</td><td colspan="5">Reference methods</td></tr><tr><td>Dataset</td><td>Normalized</td><td>Unnormalized</td><td>Naive</td><td>TILDE</td><td>FORF-NA</td><td>Graph-NB</td><td>TreeLiker-Relf</td><td>TreeLiker-Poly</td></tr><tr><td>Financial</td><td>2.3</td><td>2.3</td><td>1.4</td><td>2429</td><td>54,006</td><td>0.8</td><td>61.5</td><td>41.3</td></tr><tr><td>Hepatitis</td><td>1.1</td><td>1.1</td><td>0.54</td><td>853</td><td>10,515</td><td>0.21</td><td>7.24</td><td>6.43</td></tr><tr><td>Mondial</td><td>0.26</td><td>0.26</td><td>0.25</td><td>0.3</td><td>7.07</td><td>0.18</td><td>11.97</td><td>9.51</td></tr><tr><td>MovieLens</td><td>2.2</td><td>2.2</td><td>2</td><td>3</td><td>20</td><td>1.3</td><td>17.51</td><td>16.5</td></tr><tr><td>JMDB</td><td>13</td><td>13</td><td>11</td><td>NT</td><td>NT</td><td>9</td><td>3173.1</td><td>506.67</td></tr></table>

Table 2  
Number of attributes constructed by the TreeLiker propositionalization methods.

<table><tr><td>No. of attributes</td><td>TreeLiker-Relf</td><td>Treeliker-Poly</td></tr><tr><td>MovieLens</td><td>53</td><td>26</td></tr><tr><td>Financial</td><td>337</td><td>353</td></tr><tr><td>Hepatitis</td><td>305</td><td>185</td></tr><tr><td>Mondial</td><td>418</td><td>40</td></tr><tr><td>JMDB</td><td>44</td><td>33</td></tr></table>

For the other systems, we used the evaluation procedures supplied with the systems as recommended by their creators. (Cross-validation for TILDE, out-of-bag for FORF-NA.)

To evaluate classi<sup>fi</sup>cation performance, we used the following metrics:

• Run time: Induction time of the model.

• Accuracy: Percentage of correctly classi<sup>fi</sup>ed instances.

• AUC: The area under the ROC curve.

• Weighted F-measure: Sum of the F-measures for each class label, each weighted according to the number of instances with a particular class label (class prior). F-measure is the weighted harmonic mean of precision and recall.

## 7.3. Results

We discuss run times for learning, then predictive performance.

## 7.3.1. Learning times

Table 1 reports the induction times of different relational classi-<sup>fi</sup>ers on the three datasets. The fastest system is Graph-NB, the multi-relational Naive Bayes classi<sup>fi</sup>er, which makes the strongest independence assumptions. For Normalized and Unnormalized Decision Forests, the induction time is basically the sum of the runtimes of the Naive Decision Forest learner and the logistic regression. Normalized and Unnormalized Decision Forest differ only in using scaling factors so they have the same induction time. The Decision Forest learners are very fast as well, but because the Simple Decision Forest learner considers dependencies within tables, they have a slightly longer induction time compared to the Multi-relational Naive Bayes classifier. The fast learning times of the independence-based methods on the large JMDB dataset illustrate that these methods scale well in the dataset size.

The systems based on independence assumptions are 1000 times or more faster than the older propositionalization-based systems TILDE and FORF-NA, which is a dramatic improvement. The state-of-the-art

TreeLiker method is quite fast on the smaller datasets, still about an order of magnitude slower than decision forest learning. Table 2 shows the number of relevant features constructed by the Treeliker methods. Because TreeLiker constructs a large set of features, which correspond to subsets (conjunctions) of attributes, it does not scale well with the size of the dataset, which is illustrated by its learning time on the JMDB database. TreeLiker did not terminate on JMDB using our standard system, so to obtain the classi<sup>fi</sup>cation results shown, we ran it on a high-performance cluster with 554 nodes.

In sum, our simulations provide evidence that the cross-table independence assumption of De<sup>fi</sup>nition 1 allows learning to proceed ef<sup>fi</sup>ciently by analyzing separate join tables independently and combining the results in a principled manner. In contrast, propositionalization methods search a large feature space, and even a state-of-the-art ef<sup>fi</sup>cient method like TreeLiker does not scale well with dataset size.

## 7.3.2. Predictive performance

Table 3 shows the Accuracy, AUC, and F-measure of the different classi<sup>fi</sup>ers on the three datasets. For the multi-class problems, we report only accuracy, since there is no standard way to extend f-measure and AUC to multi-class problems [11], and since the three measures are highly correlated on the binary class problems.

We make the following observations.

1. Overall, the Normalized Decision Forest achieves always good classi<sup>fi</sup>cation performance and typically the best.

2. Comparing Naive Decision Forest with Naive Bayes net classi<sup>fi</sup>er (Graph-NB), taking into account within-table dependencies between attributes of each join table is clearly bene<sup>fi</sup>cial. Even the worst Decision Forest method makes better predictions.

3. Comparing Decision Forests with Random Forests, we found that grouping together the features of each join table for a classi<sup>fi</sup>er, instead of learning on a randomly selected subset of features, improved the performance substantially on two of the three datasets (Hepatitis and Mondial). On Financial, the Normalized and Naive Decision Forest methods achieved better performance.

7.3.2.1. Regression weights. To show how linear regression assigns weights to the information from different tables, the weights learned by Normalized and Unnormalized decision forests for the target table and each extended table of each dataset with binary class labels are listed in Table 4.

There are two extended join tables involving the Client relation, since in the Semantic Relationship Graph of Financial there are two pathways to the Client table (see Fig. 7). Because both join tables receive regression weights 0, we show only one as “Client”. The fact that the nonzero weights are far from uniform shows that regression learns an importance ranking of the information from different tables. The 0 weights demonstrate how regression prunes uninformative join tables. For instance, on the Mondial database, the weights indicate that the most important factor in predicting the majority religion of a country is the majority religion of its neighbors (1.43), the second most important factor is the continent on which the country is located (1.23), and the third are the attributes of the country contained in the country target table (0.94). If knowledge discovery is the goal of data analysis, the regression weights enhance the information conveyed by the decision trees, or extracted rules (see Section 2).

Performance of different classi<sup>fi</sup>ers by dataset. For multi-class problems we report accuracy only. Numbers in bold indicate the top score.

<table><tr><td rowspan="2">Method</td><td colspan="3">Simple decision forest</td><td colspan="5">Reference methods</td></tr><tr><td>Normalized</td><td>Unnormalized</td><td>Naive</td><td>TILDE</td><td>FORF-NA</td><td>Graph-NB</td><td>TreeLiker-Relf</td><td>TreeLiker-Poly</td></tr><tr><td colspan="9">Financial</td></tr><tr><td>Accuracy</td><td>92%</td><td>87%</td><td>91%</td><td>89%</td><td>89%</td><td>81%</td><td>87%</td><td>88%</td></tr><tr><td>AUC</td><td>0.88</td><td>0.85</td><td>0.85</td><td>0.69</td><td>0.75</td><td>0.82</td><td>0.67</td><td>0.58</td></tr><tr><td>F-measure</td><td>0.89</td><td>0.84</td><td>0.89</td><td>0.88</td><td>0.87</td><td>0.79</td><td>0.85</td><td>0.86</td></tr><tr><td colspan="9">Hepatitis</td></tr><tr><td>Accuracy</td><td>84%</td><td>84%</td><td>80%</td><td>61%</td><td>63%</td><td>75%</td><td>69%</td><td>67%</td></tr><tr><td>AUC</td><td>0.88</td><td>0.86</td><td>0.80</td><td>0.61</td><td>0.64</td><td>0.79</td><td>0.74</td><td>0.69</td></tr><tr><td>F-measure</td><td>0.79</td><td>0.75</td><td>0.75</td><td>0.59</td><td>0.61</td><td>0.68</td><td>0.69</td><td>0.67</td></tr><tr><td colspan="9">Mondial</td></tr><tr><td>Accuracy</td><td>84%</td><td>84%</td><td>83%</td><td>71%</td><td>71%</td><td>73%</td><td>80%</td><td>77%</td></tr><tr><td>AUC</td><td>0.85</td><td>0.86</td><td>0.86</td><td>0.75</td><td>0.79</td><td>0.74</td><td>0.833</td><td>0.702</td></tr><tr><td>F-measure</td><td>0.83</td><td>0.82</td><td>0.81</td><td>0.78</td><td>0.77</td><td>0.75</td><td>0.79</td><td>0.74</td></tr><tr><td colspan="9">Multi-class</td></tr><tr><td>MovieLens-Acc</td><td>61.5%</td><td>60%</td><td>62%</td><td>47%</td><td>47%</td><td>51%</td><td>61%</td><td>63%</td></tr><tr><td>JMDB-Acc</td><td>57%</td><td>56%</td><td>53%</td><td>NT</td><td>NT</td><td>51.7%</td><td>51%</td><td>51%</td></tr></table>

Table 4  
The regression weights indicating the importance of linked tables for datasets with binary class labels. Normalized DF divides a weight by the size of the associated join table

<table><tr><td>Financial</td><td> $w_0$ </td><td>Loan</td><td>Account</td><td>Order</td><td>Trans</td><td>Disp</td><td>District</td><td>Card</td><td>Client</td></tr><tr><td>Normalized DF</td><td>-0.19</td><td>0.52</td><td>0</td><td>0</td><td>0.2</td><td>0.02</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Unnormalized DF</td><td>-0.34</td><td>0.38</td><td>0</td><td>0.34</td><td>0.2</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Hepatitis</td><td> $w_0$ </td><td></td><td>Biopsy</td><td>Patient</td><td></td><td>In-Hosp</td><td>Out-Hosp</td><td></td><td>Interferon</td></tr><tr><td>Normalized DF</td><td>0.29</td><td></td><td>0.3</td><td>0.2</td><td></td><td>0.9</td><td>0</td><td></td><td>0.3</td></tr><tr><td>Unnormalized DF</td><td>0.97</td><td></td><td>0.76</td><td>0.4</td><td></td><td>0.22</td><td>0.03</td><td></td><td>0.9</td></tr><tr><td>Mondial</td><td> $w_0$ </td><td>Country</td><td>Borders</td><td colspan="2">Country2</td><td>Continent</td><td>Economy</td><td></td><td>Government</td></tr><tr><td>Normalized DF</td><td>0</td><td>0.94</td><td>0</td><td colspan="2">1.43</td><td>1.23</td><td>0.86</td><td></td><td>0.7</td></tr><tr><td>Unnormalized DF</td><td>0</td><td>0.8</td><td>0.3</td><td colspan="2">1.09</td><td>1.1</td><td>0.79</td><td></td><td>0</td></tr></table>

## 8. Conclusion

A goal of relational classi<sup>fi</sup>cation is to make predictions that utilize information not only about the target table but also about related objects. Decisions trees are a well-established predictive method for propositional single table data. We proposed a new way of upgrading them for relational data classi<sup>fi</sup>cation. The basic idea is to independently learn different decision trees for different related tables, and then combine their contributions in a new log-linear model to predict class probabilities. The log-linear model is derived from an explicitly de<sup>fi</sup>ned crosstable Naive Bayes independence assumption. Features that distinguish this method from other relational decision tree learners include the following. (1) Aggregation functions are not used, which avoids some information loss and allows for ef<sup>fi</sup>cient learning. (2) Information from all links is considered in classi<sup>fi</sup>cation. (3) Logistic regression is used to weight information from different tables.

Empirical evaluation on three datasets showed very fast runtimes, with improved predictive performance.

A natural variant of our approach, especially for continuous attributes, is to use logistic regression as the base probabilistic classi<sup>fi</sup>er, instead of decision trees. This would provide regression weights on attributes/features within each table in addition to the weights for each table we learned in our experiment.

A promising direction for future work is to combine our loglinear model with propositionalization techniques. While a search for informative aggregate features is computationally expensive, when it succeeds, the new aggregate features can increase the predictive accuracy (e.g., [14,41]). There are several possibilities for a combined hybrid approach. (i) Once good aggregate features are found, they can be treated like other features and used in a decision tree. (ii) A simple decision forest is fast to learn and can establish a strong baseline for evaluating the information gain due to a candidate aggregate feature. (iii) The regression weights can be used to quickly prune uninformative join tables with 0 or small weights, which allows the search for aggregate features to focus on the most relevant link paths.

## Acknowledgments

This research was supported by a Discovery grant to the senior author by the Natural Sciences and Engineering Research Council of Canada. Zhensong Qian was supported by a grant from the China Scholarship Council. Anonymous reviewers for Decision Support Systems provided helpful comments. We are grateful to Ondvrej Kuvzelka for help with running Treeliker.

## References

[1] X. Yin, J. Han, Exploring the power of heuristics and links in multi-relational data mining, in: ISMIS, LNAI, Springer, 2008, pp. 17–27.

[2] J. Neville, D. Jensen, Relational dependency networks, in: Introduction to Statistical Relational Learning [45], Ch. 8, pp. 239–268.

[3] J. Neville, D. Jensen, B. Gallagher, R. Fairgrieve, Simple estimators for relational bayesian classi<sup>fi</sup>ers, in: ICDM, IEEE Computer Society, 2003, pp. 609–612

[4] H. Chen, H. Liu, J. Han, X. Yin, Exploring optimization of semantic relationship graph for multi-relational Bayesian classi<sup>fi</sup>cation, Decision Support Systems 48 (1) (2009) 112–121.

[5] G. Manjunath, M.N. Murty, D. Sitaram, A practical heterogeneous classi<sup>fi</sup>er for relational databases, in: ICPR, IEEE Computer Society, 2010, pp. 3316–3319.

[6] F.J. Provost, P. Domingos, Tree induction for probability-based ranking, Machine Learning 52 (3) (2003) 199–215

[7] D. Fierens, J. Ramon, H. Blockeel, M. Bruynooghe, A comparison of pruning criteria for probability trees, Machine Learning 78 (1–2) (2010) 251–285.

[8] H. Zhang, J. Su, Conditional independence trees, in: ECML, LNAI, Springer, 2004, pp. 513–524.

[9] R. Kohavi, Scaling up the accuracy of naive-bayes classi<sup>fi</sup>ers: A decision-tree hybrid, in: KDD, AAAI Press, 1996, pp. 202–207.

[10] P. Domingos, D. Lowd, Markov Logic: An Interface Layer for Arti<sup>fi</sup>cial Intelligence Morgan and Claypool Publishers, 2009.

[11] M. Brydon, A. Gemino, You've data mined. now what?, The Communications of the Association for, Information Systems 22 (33) (2008) 603–616.

[12] A. Van Assche, C. Vens, H. Blockeel, S. Dvzeroski, First order random forests: Learning relational classi<sup>fi</sup>ers with complex aggregates, Machine Learning 64 (1) (2006) 149–182.

[13] S. Kramer, N. Lavrac, P. Flach, Propositionalization approaches to relational data mining, in: Relational Data Mining, Springer, 2000, pp. 262–286.

[14] J. Neville, D. Jensen, L. Friedland, M. Hay, Learning relational probability trees, in: KDD, ACM Press, 2003, pp. 625–630.

[15] A. Popescul, L. Ungar, Feature generation and selection in multi-relational learning, in: Introduction to Statistical Relational Learning [45], Ch. 16, pp. 453–476.

[16] O. Kuzelka, F. Zelezný, Block-wise construction of tree-like relational features with monotone reducibility and redundancy, Machine Learning 83 (2) (2011) 163–192.

[17] N. Landwehr, K. Kersting, L.D. Raedt, nfoil: Integrating na¨ıve bayes and foil, in: AAAI, AAAI Press, 2005, pp. 795–800.

[18] X. Yin, J. Han, J. Yang, P.S. Yu, Crossmine: Ef<sup>fi</sup>cient classi<sup>fi</sup>cation across multiple database relations, in: ICDE, IEEE Computer Society, 2004, pp. 399–410.

[19] H. Blockeel, L.D. Raedt, Top-down induction of <sup>fi</sup>rst-order logical decision trees, Arti<sup>fi</sup>cial Intelligence 101 (1–2) (1998) 285–297.

[20] J.R. Quinlan, C4.5: programs for machine learning, Morgan Kaufmann Publishers Inc., 1993.

[21] A. Atramentov, H. Leiva, V. Honavar, A multi-relational decision tree learning algorithm - implementation and experiments, in: ILP, Vol. 2835 of LNAISpringer, 2003, pp. 38–56.

[22] J.-F. Guo, J. Li, W.-F. Bian, An ef<sup>fi</sup>cient relational decision tree classi<sup>fi</sup>cation algorithm, in: ICNC, 3, IEEE Computer Society, 2007, pp. 530–534.

[23] A.Y. Ng, M.I. Jordan, On discriminative vs. generative classi<sup>fi</sup>ers: A comparison of logistic regression and naive bayes, in: NIPS, 14, MIT Press, 2001, pp. 841–848.

[24] Q. Lu, L. Getoor, Link-based classi<sup>fi</sup>cation, in: ICML, AAAI Press, 2003, pp. 496–503.

[25] M. Ceci, A. Appice, D. Malerba, Mr-SBC: A multi-relational naïve Bayes classi<sup>fi</sup>er in: PKDD, Vol. 2838 of LNAISpringer, 2003, pp. 95–106.

[26] P.A. Flach, N. Lachiche, Naive Bayesian classi<sup>fi</sup>cation of structured data, Machine Learning 57 (3) (2004) 233–269.

[27] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006.

[28] L.I. Kuncheva, Combining Pattern Classi<sup>fi</sup>ers: Methods and Algorithms, Wiley 2004.

[29] L. Getoor, N. Friedman, D. Koller, A. Pfeffer, B. Taskar, Probabilistic relational models, in: Introduction to Statistical Relational Learning [45], Ch. 5, pp. 129–173.

[30] B. Taskar, P. Abbeel, D. Koller, Discriminative probabilistic models for relational data, in: UAI, Morgan Kaufmann Publishers Inc., 2002, pp. 485–492.

[31] T.N. Huynh, R.J. Mooney, Discriminative structure and parameter learning for markov logic networks, in: ICML, 307, ACM, 2008, pp. 416–423.

[32] O. Schulte, H. Khosravi, Learning graphical models for relational data via lattice search, Machine Learning 88 (3) (2012) 331–368.

[33] T. Khot, S. Natarajan, K. Kersting, J.W. Shavlik, Learning markov logic networks via functional gradient boosting, in: ICDM, IEEE Computer Society, 2011, pp. 320–329.

[34] D. Jensen, J. Neville, B. Gallagher, Why collective inference improves relational classi<sup>fi</sup>cation, in: SIGKDD, ACM Press, 2004, pp. 593–598.

[35] J.D. Ullman, Principles of database systems, 2nd Edition W. H. Freeman & Co., 1982.

[36] H. Khosravi, O. Schulte, J. Hu, T. Gao, Learning compact markov logic networks with decision trees, Machine Learning 89 (3) (2012) 257–277.

[37] P. Domingos, M. Pazzani, Beyond independence: Conditions for the optimality of the simple Bayesian classi<sup>fi</sup>er, in: ICML, Morgan Kaufmann, 1996, pp. 105–112.

[38] R. Raina, Y. Shen, A.Y. Ng, A. Mccallum, Classi<sup>fi</sup>cation with hybrid generative/ discriminative models, in: NIPS, MIT Press, 2003, pp. 545–552.

[39] R. Frank, F. Moser, M. Ester, A method for multi-relational classi<sup>fi</sup>cation using single and multi-feature aggregation functions, in: PKDD, Vol. 4702 of LNAISpringer, 2007, pp. 430–437.

[40] W. May, Information extraction and integration: The mondial case study, Tech. rep, Universit¨at Freiburg, Institut f¨ur Informatik, 1999.

[41] R. She, K. Wang, Y. Xu, P.S. Yu, Pushing feature selection ahead of join, in: SIAM SDM, 2005, pp. 536–540.

[42] M. Hall, E. Frank, G. Holmes, B. Pfahringer, P. Reutemann, I.H. Witten, The weka data mining software: an update, SIGKDD Explorations 11 (1) (2009) 10–18.

[43] H. Blockeel, L. Dehaspe, J. Ramon, et al., The ACE Data Mining System: User's Manual, http://dtai.cs.kuleuven.be/ACE/doc/ACEuser-1.2.16.pdf2009.

[44] R. Espíndola, N. Ebecken, On extending f-measure and g-mean metrics to multi-class problems, Data mining VI: Data mining, text mining and their business applications 35 (2005) 25–34.

[45] L. Getoor, B. Taskar, Introduction to statistical relational learning, MIT Press, 2007.

![](/api/attachments/RB9KGWQP/fulltext/images/0efdc87869bc58478a3516a687f1b360dd23d6a3c9922a8d2eff3309e10b77f7.jpg)  
Bahareh Bina received an M.Sc. from Simon Fraser University in 2011. She is now with Microsoft, Seattle.

![](/api/attachments/RB9KGWQP/fulltext/images/444770086d9618e341077844c0d727dda07ebe156daaf802996eaed69c24cf73.jpg)

Oliver Schulte received a Ph.D. from Carnegie Mellon University in 1997. He joined the University of Alberta as Assistant Professor in 1997, and has been at Simon Fraser University since 2000, where he is now Associate Professor. He has published extensively in different areas, such as machine learning, computational learning theory, computation theory, game theory and statistical–relational learning.

Zhensong Qian received an M.E. degree from Shandong University, China, in 2010. He is a Ph.D. candidate at Simon Fraser University.

![](/api/attachments/RB9KGWQP/fulltext/images/98b4232ae4c555033eb29f8fdd9d6d1a46a4b4400b9a6d2dcfd302fe9ede240a.jpg)

Yi Xiong is an M.Sc. candidate at Simon Fraser University.

![](/api/attachments/RB9KGWQP/fulltext/images/f013d2a33fd1ce0bf12f19b2f1ae15695fe9beaceba15890afea8fbb457b4792.jpg)
