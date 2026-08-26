---
otero_id: 314
otero_key: "BZWTNAQA"
title: "A hierarchical Naïve Bayes model for approximate identity matching"
authors: "G. Alan Wang; Homa Atabakhsh; Hsinchun Chen"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hierarchical Naïve Bayes model for approximate identity matching

G. Alan Wang <sup>a,</sup>⁎, Homa Atabakhsh <sup>b,1</sup>, Hsinchun Chen <sup>b,1</sup>

<sup>a</sup> Department of Business Information Technology, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061, United States <sup>b</sup> Department of Management Information Systems, The University of Arizona, Tucson, AZ 85721, United States

## a r t i c l e i n f o

Article history: Received 6 November 2008 Received in revised form 10 January 2011 Accepted 20 January 2011 Available online 31 January 2011

Keywords: EM algorithm Entity matching Identity management Hierarchical Naïve Bayes model Semi-supervised learning

## a b s t r a c t

Organizations often manage identity information for their customers, vendors, and employees. Identity management is critical to various organizational practices ranging from customer relationship management to crime investigation. The task of searching for a speci<sup>fi</sup>c identity is dif<sup>fi</sup>cult because disparate identity information may exist due to the issues related to unintentional errors and intentional deception. In this paper we propose a hierarchical Naïve Bayes model that improves existing identity matching techniques in terms of searching effectiveness. Experiments show that our proposed model performs signi<sup>fi</sup>cantly better than the exact-match based matching technique. With 50% training instances labeled, the proposed semi-supervised learning achieves a performance comparable to the fully supervised record comparison algorithm. The semisupervised learning greatly reduces the efforts of manually labeling training instances without signi<sup>fi</sup>cant performance degradation.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Most organizations manage identity information for their customers, vendors, and employees, etc. Identity management is critical for various organizational practices. In Customer Relationship Management (CRM), a poorly maintained customer database may lead to a poor relationship with customers (e.g., a customer may be contacted many times if duplicate customer records exist). When two companies merge, their customer databases should be combined and information about the same customer needs to be consolidated. It is even more critical to effectively manage identity information, particularly criminal identities, in law enforcement and intelligence agencies. The ability to locate a suspect's records in databases and collect relevant information is central to <sup>fi</sup>ghting against crimes and terrorism [7,8].

A person may change his/her identity information throughout his/ her lifespan due to life changes [9]. For example, a female may change her last name when she gets married. As a form of data, identity information is also subject to data quality issues in data management systems. As a result of these problems, multiple identity representations may exist for an individual person.

Current identity matching techniques either rely on exact value matching [29] or require human intervention [6,30,40]. Exact value matching is also called all-or-none matching [17]. Even if an existing identity record is very similar to the information of a suspect, if it is not actually the same, an exact-match query is unlikely to bring up that record. On the other hand, automated matching techniques often need to be trained using a manually generated dataset. This manual process, however, can be very time-consuming and labor-intensive.

In this research we examine what causes problems in identity matching and propose an advanced identity matching technique that requires less or no human intervention. In Section 2 we discuss possible identity problems and review existing identity matching techniques. In Section 3 we state the objectives of this research. In Section 4 we propose a Naïve Bayes model for approximate identity matching. We also report a case study using real law enforcement data in order to determine the features effective for identity matching. We describe our experimental design and report the results and discussions in Section 5. We summarize our <sup>fi</sup>ndings, discuss research contributions, and provide future directions in the last section.

## 2. Literature review

In this section, we review issues related to identity problems and matching techniques proposed in a previous research.

## 2.1. Identity problems

An identity is a set of characteristic features that distinguish a person from others [15,22]. For identi<sup>fi</sup>cation purposes, Clarke [9] proposed an identity model that categorized identity features into <sup>fi</sup>ve categories (Table 1). An identity can be represented by a vector of features selected from the <sup>fi</sup>ve categories.

Table 1  
Identity features included in Clarke's identity model.

<table><tr><td>Feature category</td><td>Description</td><td>Example</td></tr><tr><td>Names</td><td>What the person is called by other people</td><td>First name, surname</td></tr><tr><td>Codes</td><td>What the person is called by an organization</td><td>Social Security number</td></tr><tr><td>Knowledge</td><td>Information that the person is expected to know</td><td>Address</td></tr><tr><td>Tokens</td><td>What the person has</td><td>Driver&#x27;s license</td></tr><tr><td>Biometric features</td><td>Physical and difficult-to-change characteristics</td><td>Fingerprint</td></tr></table>

Identity information is unreliable due to various reasons. First, unintentional errors often occur in data management processes such as data entry, storage and transformation. A study showed that the data error rate in typical enterprises could be as high as 30% [34]. Secondly, identity information sometimes is subject to intentional deception, especially the identities of criminals or terrorists who are known to use false identities to mislead police investigations [40]. Identity deception also exists in online auction. A customer may use false identities to register multiple user accounts in order to drive up the bidding prices [39]. In addition, the lack of a reliable unique identi<sup>fi</sup>er causes problems when integrating identity information from different sources. For example, one information system may use a social security number (SSN) to uniquely identify a person whereas another system uses employee ID to uniquely represent each identity. There are no easy means to match identities in two systems where unique identi<sup>fi</sup>ers do not agree.

These problems may result in multiple identity representations for an individual in an information system or across different systems. To ef<sup>fi</sup>ciently manage identities, we need a mechanism to associate identities that belong to an individual. It will also be useful in searching for information about a particular person, which is a critical task for law enforcement and intelligence investigations.

## 2.2. Identity matching

According to a psychological theory, the perceptive matching process is closely related to pair-wise similarity judgment [3]. Assuming each stimulus (e.g., an identity) is represented by a vector of perceived attributes in a multidimensional space, the psychological similarity of two stimuli can be represented by the perceived similarities on individual attributes. Two types of matching models, deterministic and probabilistic models, are often considered to convert the perceived similarities into an overall matching decision [2]. Deterministic models always produce the same decision (matching or non-matching) on different trials if the perceived similarities are the same. Probabilistic models can capture the uncertainty of matching by associating each matching decision with a probability rating.

## 2.2.1. Existing identity matching techniques

To the best of our knowledge, there are few solutions designed speci<sup>fi</sup>cally for the problem of identity matching. Marshall et al. [29] provided an exact matching technique for law enforcement applications. Two identities are considered matching only when their <sup>fi</sup>rst names, last names, and date-of-birth (DOB) values are identical. However, as identity information is unreliable, it is possible that identities referring to the same person have disagreeing values. Wang et al. [40] proposed a record comparison algorithm to detect deceptive identities. Given two identities, the algorithm <sup>fi</sup>rst computes a similarity rating for the value-pair of each individual identity feature. Assuming features are equally important in making a matching decision, all the similarity ratings are combined into an overall similarity rating using a Euclidean distance function. The two identities being compared are considered matching when the overall similarity rating is greater than a threshold value. A supervised learning process is required to determine the threshold value. This technique has the following disadvantages. First, supervised learning needs experts to manually generate a training dataset, which can be time-consuming and inef<sup>fi</sup>cient. Second, the assumption of features' equal importance is ad-hoc. Moreover, this technique is speci<sup>fi</sup>cally designed to match deceptive identities. It is unknown whether this algorithm could match identities having other problems such as unintentional errors.

Table 2  
Common similarity measures for different feature types.

<table><tr><td>Feature Type</td><td colspan="4">Similarity Measure</td></tr><tr><td>Numeric</td><td colspan="4">Similarity $(s1, s2) = 1 - \frac{|s_1 - s_2|}{max(s) - min(s)}$  [21]</td></tr><tr><td>Binary</td><td colspan="4">Similarity $(s1, s2) = \begin{cases} 1, & \text{when } s_1 \text{ and } s_2 \text{ agree} \\ 0, & \text{otherwise} \end{cases}$  [1]</td></tr><tr><td>Nominal</td><td colspan="4">Look up a similarity table that is elicited from users [1]</td></tr><tr><td rowspan="3">Textual strings</td><td>Phonetic</td><td>Character-based</td><td>Token-based</td><td>Hybrid</td></tr><tr><td>Soundex</td><td>Edit distance</td><td>Jaccard similarity</td><td rowspan="2">Token-based plus character-based [4]</td></tr><tr><td>[35]</td><td>[26]</td><td>[4]</td></tr></table>

## 2.2.2. Entity matching techniques

The problem of identity matching can be considered as a special case of entity matching, where it is determined whether an entity in one database is the same as the entity in another one [14]. Mostly studied in the area of databases, entity matching techniques consist of two components: similarity measures and a matching decision model. Like an identity, an entity is also represented by a feature vector. A similarity measure is de<sup>fi</sup>ned for each entity feature and calculates a score for the perceived similarities between two feature values. Table 2 shows common similarity measures de<sup>fi</sup>ned for different feature types.

A matching decision model maps a set of feature similarity scores onto a binary decision variable. We classify existing entity matching models into two categories: deterministic and probabilistic models.

A deterministic decision model associates matching decisions with the probability of one. Given a pair of entities, a deterministic model combines similarity scores of individual features into an overall similarity rating and considers the two entities as a match if the overall similarity rating is greater than a threshold. Weights may be used to represent relative importance of individual features when combining individual similarity scores. Brown and Hagen [6] proposed a deterministic technique for associating suspects or incidents having similar modus operandi. It <sup>fi</sup>rst compares corresponding feature values of two records and calculates a weighted total similarity measure (TSM). It relies on experts to estimate weights by minimizing the difference between the algorithm's similarity ratings and those given by experts. For each suspect or incident, this technique orders candidate matching records by their TSM values. Assuming a one-to-one mapping between two databases, Dey et al. modeled entity matching as an integer programming problem [14]. In this model, individual feature similarities are <sup>fi</sup>rst combined into a total similarity measure as a weighted-sum. Weights are elicited from users. Entities in two databases are mapped in a way that the total cost of type-I and type-II errors is minimized. The major problem of both approaches is their reliance on human inputs to determine feature weights. They become inef<sup>fi</sup>cient since human interventions are time-consuming. Some deterministic models developed unsupervised clustering algorithms to <sup>fi</sup>nd approximate matches without human interventions [27,28]. However, the clustering-based algorithms tend to achieve low recall ratings (i.e., a high number of false negatives) or high recall with very low precision (i.e., a high number of false positives).

A probabilistic decision model applies statistical theories to capture the uncertainty in entity matching. Unlike a deterministic model, a probabilistic model associates a matching decision with a probability between zero and one. A matching decision is made directly based on individual similarity ratings instead of an overall similarity score. Originated in the area of statistics, record linkage (RL) is a probabilistic model that identi<sup>fi</sup>es records corresponding to the same entity in one or more data sources. A formal RL de<sup>fi</sup>nition was given by Fellegi and Sunter [16]. Given a comparison vector γ that consists of feature similarity ratings for a record pair, RL calculates an odds ratio $R = m ( \gamma ) / u ( \gamma )$ , where $m ( \gamma )$ is the probability that γ belongs to the matching set (M) and u(γ) is the probability that γ belongs to the non-matching set (U). The higher the ratio R, the more likely it is for the two records to match. Two cut-off threshold values are determined according to the expected type-I and type-II error rates. When R is greater than the upper threshold, a match will be found. When R is smaller than the lower threshold, a non-matching decision will be made. When R falls between the two thresholds, the comparison needs to hold for clerical review. A supervised learning is often required to estimate the parameters such as $m ( \gamma ) , u ( \gamma )$ and threshold values. It needs a training dataset generated by domain experts. This process could be time-consuming and labor-intensive. Dey presented a logistic regression based approach to solve the entity heterogeneity problem in the absence of training data [13]. However, that approach cannot be automated because it must rely on input from users knowledgeable about the application context when estimating the probability of a match between two records. Winkler [43] and Jaro [20] improved the classic RL by providing an unsupervised learning mechanism. Their approaches assume that all comparison vectors are distributed according to a <sup>fi</sup>nite mixture with unknown parameters such as $m ( \gamma )$ and u(γ). The EM (Expectation– Maximization) algorithm was used to estimate those parameters. The unsupervised learning avoids the time-consuming process of manually generating a training dataset. However, it only performs well in a few situations that are extremely favorable [44].

Ravikumar and Cohen proposed a three-layer hierarchical graphical model for record linkage problems [33]. In this model a layer of latent variables were added between the binary matching decision variable and feature similarity ratings. This latent layer captures the intuition that a match decision made for a record pair is often dependent on matching decisions based on features rather than the similarity ratings of features. To estimate the parameters of the graphical model shown in Fig. 1, the EM algorithm is also used for unsupervised learning. Experiments showed that this approach achieved performance comparable to that of the fully supervised RL methods. Although effective, this approach has the following problems. First, similar to the classic RL, unsupervised learning is not always preferable because unlabeled data alone often are not suf<sup>fi</sup>cient for training [31] and the model is subject to over<sup>fi</sup>tting the noisy data [33]. Second, the computational complexity of this approach is polynomial because it allows dependencies between latent variables. These dependencies can increase computation in the orders between 100 and 10,000 [44]. Moreover, the three-layer architecture may limit the ability to capture more complex matching heuristics. For example, a matching decision made for a pair of names can depend on the separate matching decisions of <sup>fi</sup>rst name and surname. Therefore, an extra layer of latent variable is necessary to capture the separate matching decisions of name components.

![](/api/attachments/BZWTNAQA/fulltext/images/ae1959527207d59567efbf0b91021e9aa81d016895d2742fd47c1e5d05989a99.jpg)  
Fig. 1. A three-layer hierarchical graphical model (the arrows signify dependencies, $\mathrm { e . g . }$ variable M depends on $X _ { 1 } , X _ { 2 } , X _ { 3 } ,$ and $X _ { 4 } , X _ { 1 }$ depends on $F _ { 1 }$ and $X _ { 3 } )$

## 3. Research objectives

In this research our <sup>fi</sup>rst objective is to develop a probabilistic decision model for identity matching. We hope the proposed approach could rely less on human intervention and still improve the performance of identity matching. Our second objective is to investigate carefully the identity problems that hinder effectively matching identities. We hope such a study could provide a good basis for proposing a more advanced identity matching technique. A systematic evaluation will be conducted to evaluate our proposed identity matching technique.

## 4. Research design

## 4.1. A Hierarchical Naïve Bayes model for approximate identity matching

To overcome the high computational complexity of the three-layer hierarchical graphical model, we propose a Hierarchical Naïve Bayes (HNB) model for approximate identity matching as shown in Fig. 3. A Naïve Bayes (NB) classi<sup>fi</sup>er is a simple probabilistic classi<sup>fi</sup>er that can be trained very ef<sup>fi</sup>ciently. It may surprisingly achieve higher classi<sup>fi</sup>cation performance than other complex graphical models despite its oversimpli<sup>fi</sup>ed independence assumptions [47]. An HNB model was <sup>fi</sup>rst proposed by Zhang et al. [48,49] to further improve the performance of NB models by relaxing NB's strong independence assumptions. HNB models are tree-structured Bayesian networks with latent variables between the class node and independent attributes. The latent variables enable conditional dependence among the attributes. The computational complexity of learning an HNB model is $O ( n )$ , a linear function of the number of nodes in the network [24]. An HNB model also allows a multi-layer structure in order to encode a complex model structure while maintaining the model learning ef<sup>fi</sup>ciency. Most existing studies on HNB models use either supervised-learning [24,48,49] or unsupervised learning [18]. In this study we propose a semi-supervised learning method that is expected to achieve a balance between training effectiveness and ef<sup>fi</sup>ciency. In the rest of the section we formally describe the HNB model for approximate identity matching.

Let I be an identity record represented as a vector of m feature values, $I = \{ f _ { 1 } , f _ { 2 } , . . . , f _ { m } \}$ . Given a pair of identity records, similarity ratings $s _ { i } \ ( 1 \leq i \leq m )$ can be computed for the m feature value-pairs. The value of the match-class variable M, however, is not directly dependent on the feature similarity ratings. Instead, it is conditionally dependent on the values of some latent variables, $x _ { j } \ ( 1 \leq j \leq k )$ . The value of each latent variable is binary, representing a match decision on a particular feature $( \mathsf { e } . \mathsf { g } . , x _ { 2 }$ in Fig. 3) or a set of related features (e.g., x and $x _ { 3 }$ in Fig. 3). The value of the latent variable that represents a match decision on one particular feature is conditionally dependent on the corresponding feature similarity rating. The value of the latent variable that represents a match decision on a set of related features is conditionally dependent on latent variables at the next level that represent lower level decisions(e.g., x , x , x , x , and $x _ { 3 2 }$ in Fig. 3). The purpose of having multiple levels of latent variables is to encode complex decision heuristics in identity matching. However, dependencies among latent variables at the same level are not allowed in order to maintain the linear computational complexity of the model training process. Variable dependencies described above are formulated as the following.

![](/api/attachments/BZWTNAQA/fulltext/images/d6c78d1443e07ddb765e3678b96167620827050da7e5416b5651045378027f9c.jpg)  
Fig. 2. Taxonomy of identity problems.

$$
P \left(M \mid x _ {j} \in X _ {M}\right) = \prod_ {x _ {j} \in X _ {M}} P \left(M \mid x _ {j}\right),\tag{1}
$$

where $1 \le j \le k , X _ { M }$ is the set of latent variables that the match variable M is conditionally dependent on.

$$
P \left(x _ {j} \mid s _ {l}, x _ {j h}\right) = \prod_ {x _ {j h} \in X _ {j}} P \left(x _ {j} \mid S _ {l}\right) P \left(x _ {j} \mid x _ {j h}\right),\tag{2}
$$

where $1 \leq j \leq k , \ 1 \leq l \leq k ,$ , and $h { \geq } 1 , X _ { j }$ is the set of lower-level latent variables that $x _ { j }$ is conditionally dependent on.

The proposed HNB model for identity matching can be applied to all types of identity features. However, not all of them are effective and reliable in determining identities. It is important to select a feature set that is both effective in making matching decisions and readily available in identity record management systems. In addition, a reduced number of features can improve the ef<sup>fi</sup>ciency of identity matching. In the following section we describe a case study on a real identity record management system and discuss the features that contribute to effective identity matching.

## 4.2. Identity feature analysis

Law enforcement agencies have accumulated a great amount of personal identities from investigational activities. Local police departments can provide a rich data source for studying identity features. We conducted a case study at the Tucson Police Department (TPD). TPD serves a relatively large population of 487,000 that ranks 30th among U.S. cities with populations of over 100,000. We hope that the results of this case study can be generalized to other agencies.

![](/api/attachments/BZWTNAQA/fulltext/images/69ebab6566692dbdd4044637c8ffbf7cd320b6897a0332f6d92401f620619c59.jpg)  
Fig. 3. A hierarchical Naïve Bayes model.

TPD's COPLINK database maintains 2.4 million identity records. Each identity record consists of many features such as name, DOB, ID numbers, gender, race, weight, height, address, phone number, eye color, and hair color. Name is a mandatory feature and always has a value. Other features are allowed to be empty (i.e., missing) or are assigned a default value when not available (e.g., the default value for height is one inch in the TPD).

We randomly drew 200 unique identity records out of the 2.4 million records stored in the TPD database. We considered them to be “suspects” for whom we were trying to <sup>fi</sup>nd matching identities in the TPD database. Given the huge amount of identity records in the TPD, it is nearly impossible to manually <sup>fi</sup>nd matching identity records. We used the identity matching approach that we had previously developed to compute a similarity score when comparing each “suspect” against every identity record in the database [40]. For each suspect, we chose the top ten identity records having the highest similarity scores. With the help of a veteran TPD detective who has served law enforcement for 30 years, we manually veri<sup>fi</sup>ed the 10 possible matches for each of the 200 suspects. Each possible match was classi<sup>fi</sup>ed into four categories. The <sup>fi</sup>rst two categories, deception (D) and error (E), imply a true match. A possible match was considered an unintentional error when identical values were found in key attributes such as name and ID numbers. A possible match was considered intentional deception when values of key attributes were not identical but showed similar patterns that can be visually identi<sup>fi</sup>ed by the police expert. If a possible match had missing values in many attributes and we were unable to judge, we classi<sup>fi</sup>ed it as U (uncertain). All other cases were classi<sup>fi</sup>ed as N (non-matching). We found that more than half (55.5%) of the 200 “suspects” had at least one true match, caused by deception (29.5%) and/or by errors (42%) in the database (Table 3). The counts in different categories were not exclusive. When possible matches of a suspect fell into four different categories, the suspect was counted by all the categories.

After carefully studying the patterns of the features in matching identities, we created a taxonomy of identity problems (Fig. 2) based on our <sup>fi</sup>ndings. Among other features, matching values in name, DOB, ID numbers, and address indicate deception or errors in most cases. Errors were found to occur in only one feature of the records with errors. There were 50% of identities with errors in name, 11.9% in DOB, and 3.6% in ID numbers. It was interesting that 34.5% identities were duplicate, which is probably caused by a bad database design. Deceptive identities usually involve false values in more than one feature. The name feature was found to be the most deceptive feature (91.5%). Less than half of the deceptive identities (44.1%) had altered DOB values, 22% of them had altered ID numbers, and 6.8% of the deceptive identities had altered residential addresses.

Value changes resulting from errors were minor in most cases. For example, all false DOB values and false ID numbers resulting from errors were found to have only a one-digit difference with their corresponding true values. Deception was found in values for name, DOB, ID numbers and address. Value changes that resulted from deception are more drastic than those that resulted from errors. We found that people preferred telling a half-truth lie rather than completely making up things. In most of the cases, deceptive values looked very similar to their corresponding true values. Although in some cases a deceptive value could be very different from its true value in one feature (for example, using someone else's name), other feature values such as DOB and ID numbers might still remain similar and help to identify the connections between the two identity records.

Table 3  
Statistics of matched identities.

<table><tr><td>Category</td><td>Number of suspects</td><td>Percentage</td></tr><tr><td>Matching</td><td>111</td><td>55.5%</td></tr><tr><td>Intentional deception (D)</td><td>(59)</td><td>(29.5%)</td></tr><tr><td>Unintentional errors (E)</td><td>(84)</td><td>(42.0%)</td></tr><tr><td>Nonmatching (N)</td><td>56</td><td>28.0%</td></tr><tr><td>Uncertain (U)</td><td>64</td><td>32.0%</td></tr></table>

According to the case study, matching values in name, DOB, ID numbers, and address indicate matching decisions in most cases. We propose to use the four features in our proposed HNB model for identity matching. The model also re<sup>fl</sup>ects our observation that <sup>fi</sup>eld experts would <sup>fi</sup>rst make matching decisions on individual identity features and then combine them into an overall matching decision for two identity records (Fig. 4).

## 4.3. The system framework

The overall framework we propose consists of a training process and a testing process. Given a training dataset, the training process estimates the parameters of the proposed model. Given a pair of identities with an unknown matching decision, the testing process infers the probability that the identity pair is matched using the trained model. Fig. 5 illustrates both training and testing processes. In the rest of this section we discuss each component of the framework.

## 4.3.1. Similarity measures

All four identity features used in our proposed model, namely name, date-of-birth, ID number, and address, are textual features. Different similarity measures exist for computing a similarity score between two strings (shown in Table 2). Bilenko et al. [4] experimented with these string comparators and found that Levenshtein edit distance [26] performed the best with name matching. Because identity records are quite similar to Census records, we choose Levenshtein edit distance. Edit distance computes the minimum number of character insertions, deletions, and substitutions required to transform one string into the other. A normalized string similarity measure using edit distance is computed as the following:

$$
\operatorname{Sim} \left(S _ {1}, S _ {2}\right) = 1 - \frac {\operatorname{ED} \left(S _ {1} , S _ {2}\right)}{\operatorname{MAX} \left(\left| S _ {1} \right| , \left| S _ {2} \right|\right)}\tag{3}
$$

where $S _ { 1 }$ and $S _ { 2 }$ are two strings, $E D ( S _ { 1 } , S _ { 2 } )$ calculates the Levenshtein edit distance of $S _ { 1 }$ and $S _ { 2 } ,$ and |S| calculates the length of a string. The similarity rating is a continuous number between 0 and 1 because the Levenshtein edit distance is always less than or equal to the length of the longer string.

We represent identity feature values using alphanumeric strings by removing those non-alphanumeric characters in the original feature values. All letter characters are converted into capital letters. Table 4 provides feature representation examples.

## 4.3.2. Discretization

HNB is a multinomial probability model. Continuous similarity scores cannot be directly used by HNB learning and inference algorithms. There are two common approaches, including Gaussian mixture models and discretization, to deal with continuous variables in multinomial probability models. Gaussian mixture models assume values are Gaussian distributed and estimate a probability density function using the training data. Parameters of the multinomial probability model are generated using the estimated probability density function. However, this technique may affect the learning accuracy if the density function is not a proper estimate of the true density [46]. Discretization is a process that separates a continuous value domain into a number of intervals [33,42]. Feature values falling into the same interval have the same nominal value. The number of intervals determines the approximation of the continuous distribution. If the number is too small, it leads to a poor approximation as well as a poor learning performance. If the number is too large, it signi<sup>fi</sup>cantly increases the computational complexity of Bayesian network learning and inference algorithms [11].

![](/api/attachments/BZWTNAQA/fulltext/images/20f4926ec2818e6d6f1c114e3a2f022a4405bf6850d1f433b385ec18a3080485.jpg)  
Fig. 4. A hierarchical Naïve Bayes model for approximate identity matching.

Yang and Webb suggested a Weighted Proportional k-Interval Discretization method (WPKID) that performed better than other alternatives at reducing learning errors [45]. This method maintains a good balance between bias reduction and variance reduction. It also keeps the interval size above a minimum number so that each interval can have enough instances to draw statistical inferences. Let t be the number of intervals and s the interval size. WPKID uses the following formula to calculate s and t:

$$
\begin{array}{l} {s \times t = n} \\ {s - 3 0 = t} \end{array}\tag{4}
$$

where n is the number of instances in the training dataset. Yang and Webb suggest that each interval contains at least 30 instances because a sample size of 30 is commonly held as the minimum that one can draw statistical inferences [45].

## 4.3.3. HNB learning

The proposed HNB model is a classi<sup>fi</sup>er that classi<sup>fi</sup>es the comparison of two identity records into a match or non-match decision. The parameters of the HNB model, including P(M|x ) and

P(x |s ,x ), need to be trained in order to achieve the optimal classi<sup>fi</sup>cation performance. As we discussed in Section 2, we choose to use a semi-supervised learning method over supervised and unsupervised learning techniques. We believe semi-supervised learning is more preferable than fully supervised learning or unsupervised learning for the identity matching problem. Supervised learning requires manually generating a training dataset of identity matches, which could be time-consuming and labor-intensive. Unsupervised learning is subject to over<sup>fi</sup>tting towards noisy data and may reduce learning accuracy. With a tree-like structure in the HNB model, our independence assumption greatly reduces the computational complexity.

The Expectation–Maximization (EM) algorithm [12] is commonly used for semi-supervised learning [31]. We denote the set of parameters that we intend to learn for the HNB model as θ. The training data set D is comprised of identity record comparisons, each of which consists of a vector of feature similarity ratings, the hidden latent variables, and a match class label. The data set D is supposedly drawn from a probabilistic density function p(D|θ) where θ governs the density function. Let Y be the set of observed data set (i.e., identity comparisons with observed feature similarity ratings and match class labels), and Z=D−Y be the missing data that also include the unknown latent variable values. Assuming that m data instances are independently and identically distributed (i.i.d.), the log likelihood function is described as:

![](/api/attachments/BZWTNAQA/fulltext/images/a55242286e264bd306fa10b40fb99451f0aac537edcffe56aadace2b9615a7d9.jpg)  
Fig. 5. The system framework for identity matching

Table 4 Identity feature representation.

<table><tr><td>Feature</td><td>Original value</td><td>String for similarity computation</td></tr><tr><td>First Name</td><td>John</td><td>JOHN</td></tr><tr><td>Middle Name</td><td>M.</td><td>M</td></tr><tr><td>Last Name</td><td>Doe, Jr.</td><td>DOEJR</td></tr><tr><td>Date-of-Birth</td><td>07/10/1968</td><td>680710</td></tr><tr><td>ID Number</td><td>000-12-3456</td><td>000123456</td></tr><tr><td>Address</td><td>100 N. Main St.</td><td>100NMAINST</td></tr></table>

$$
\begin{array}{c} L (\theta | D) \propto P _ {B s} (D | \theta) = \prod_ {i = 1} ^ {m} P _ {B s} (d _ {i} | \theta) \\ = \prod_ {i = 1} ^ {n} \prod_ {j = 1} ^ {q _ {i}} \prod_ {k = 1} ^ {r _ {i}} \theta_ {i j k} ^ {N _ {i j k}}, \end{array}\tag{5}
$$

where $B _ { s }$ is the Bayesian network structure, n is the number of attributes, $q _ { i }$ is the number of possible instantiations of the parents $( x _ { p a i } )$ of attribute $i , r _ { i }$ is the number of discrete values of attribute i, $N _ { i j k }$ is the number of cases where attribute i is instantiated to its kth value while its parents is instantiated to its jth value, and $\theta _ { i j k } = P ( \boldsymbol { x } _ { i } = k ^ { t h }$ instantiation| $x _ { p a i } = j ^ { t h }$ instantiation). The classic EM algorithm <sup>fi</sup>nds the $\boldsymbol { \theta } ^ { * }$ that maximizes the probability of the data set $D , \theta ^ { * } = a r g \smash { m a x } L ( \theta | D )$ by alternating the expectation step and the maximization step. The expectation step <sup>fi</sup>nds the expected suf<sup>fi</sup>cient statistics with respect to the previous conditional distribution parameters θ and the observed data D. The maximization step <sup>fi</sup>nds a new set of parameters θ′ that maximizesP (D|θ), i.e., Q(θ′| θ)=argmax $P _ { B s } ( D | \theta )$ . However, when the data set is incomplete, parameter learning can be more complex and become intractable. Lauritzen [25], Heckerman [19], and Singh [38] discussed a generalized EM algorithm (GEM) for learning a graphical model with a known structure and missing data. Instead of maximizing the likelihood function in the maximization step, the GEM only <sup>fi</sup>nds a new parameter set θ′ that makes Q(θ′| θ) strictly increase over Q(θ| θ). Therefore, each GEM iteration only takes one step towards the direction of the correct parameter space, rather than <sup>fi</sup>nding the optimal at each step. It is known that the GEM converges reliably but slowly. We brie<sup>fl</sup>y summarized the steps of the GEM below.

(1) Initialization: the algorithm begins with an initial set of parameters, $\theta ^ { [ 0 ] }$ , that is randomly generated. A parameter is a conditional probability p(x |x ) relating the values of $x _ { i }$ to the values of its parent node $x _ { p a i }$

(2) Expectation (E step): Given the current estimate of the parameters $\theta ^ { [ a ] } ( a { = } 0 , 1 , 2 . . . )$ and the observed component of the data Y, the algorithm <sup>fi</sup>nds the expected marginal counts

$$
\begin{array}{l} E \left(N _ {i j k} | D, \theta^ {[ a ]}\right) = \sum_ {l = 1} ^ {m} E _ {\theta} \left(\chi_ {i j k} ^ {l} | d _ {l}\right), \\ E _ {\theta} \left(\chi_ {i j k} ^ {l} | d _ {l}\right) = \left\{ \begin{array}{l} 1, \text {   if   } x _ {i} \text {   and   } x _ {p a i} \text {   are   observed   and   } x _ {i} = k ^ {t h} \text {   inst.   or   } x _ {p a i} = j ^ {t h} \text {   inst.   } \\ 0, \text {   if   } x _ {i} \text {   and   } x _ {p a i} \text {   are   observed   and   } x _ {i} \neq k ^ {t h} \text {   inst.   or   } x _ {p a i} \neq j ^ {t h} \text {   inst.   } \\ P _ {B s} \left(x _ {i} = k ^ {t h} \text {   inst.,   } x _ {p a i} = j ^ {t h} \text {   inst.   } | d _ {l}, \theta^ {[ a ]}\right), \text {   otherwise. } \end{array} \right. \end{array}\tag{6}
$$

where $d _ { l }$ is the lth instance in the data set D. When either x or $x _ { p a i }$ is missing from the $d _ { \mathrm { l } } ,$ the Bayesian network is instantiated with the observed evidence in $d _ { \mathrm { l } }$ and inference is carried out to determine $\begin{array} { r } { P _ { B s } ( x _ { i } = k ^ { t h } \mathrm { i n s t . } , x _ { p a i } = j ^ { t h } \mathrm { i n s t . } | d _ { l } , \theta ^ { [ a ] } ) } \end{array}$ .

(3) Maximization (M step): This step use the expected marginal counts acquired in the previous E step as if they were actually observations from a complete data set.

$$
\theta_ {i j k} ^ {[ a + 1 ]} = \frac {E \left(N _ {i j k} | D , \theta^ {[ a ]}\right)}{E \left(N _ {i j} | D , \theta^ {[ a ]}\right)},\tag{7}
$$

$$
\text { where } E (N _ {i j} | D, \theta^ {[ a ]}) = \sum_ {k = 1} ^ {r _ {i}} E (N _ {i j k} | D, \theta^ {[ a ]}).
$$

(4) Convergence: Steps (2) and (3) iterate until the likelihood function (Eq. (5)) converges.

## 4.3.4. HNB inference

Given a parameterized BN model and a new comparison vector, an inference algorithm infers the probability that the two identities being compared match. Most Bayesian network inference algorithms can apply. However, most of them have exponential computational complexity. We choose Pearl's evidence propagation algorithm because it can achieve a linear computational complexity for an HNB network. We summarize Pearl's algorithm below. For the complete description of the algorithm please refer to Ref. [32].

Pearl's algorithm considers a belief network (e.g., an HNB network) as factual knowledge storage as well as a computational architecture for reasoning about that knowledge. The belief encoded in a belief network refers to the conditional probability distribution that relates a node's values to its immediate parent node's values. When a new piece of evidence is introduced to the network, the evidence node will update its probability distribution where the node's instantiated value has a probability of one. That change will have a chain reaction effect that also updates the probability distributions of other nodes connected to the evidence node by causal links. This process is called belief propagation.

We use x to denote a node in the HNB network. $x _ { p a i }$ is x 's single parent node while $x _ { i } ^ { j }$ is the jth child node of $x _ { i \cdot }$ When node $x _ { i }$ is activated by a new evidence, Pearl's algorithm update the probability distribution of $\dot { x } _ { i }$ if three types of parameters are available: the causal support $\pi _ { x _ { p a } }$ contributed by the parent of $x _ { i } ,$ the diagnostic support $\lambda _ { x _ { i } ^ { j } } ($ contributed by the $j ^ { \mathrm { t h } }$ child of $x _ { i } ,$ and a prior conditional probability matrix $p ( x _ { i } | x _ { p a i } )$ . Node x also sends a λ message to its parent node and a π message to its child nodes. That will trigger probability distribution update at x 's parent and child nodes. The belief propagation process has the following three steps:

(1) Belief updating: When a node $x _ { i }$ receives new evidence or messages from its parent and child nodes, it is activated to update its parameters. It simultaneously inspects the π message communicated from its parent node and λ messages from its child nodes. The node x 's parameters are updated as follows:

$$
\begin{array}{l} p (x _ {i}) = \alpha \lambda (x _ {i}) \pi (x _ {i}), \\ \lambda_ {x _ {i}} = \prod_ {j} \lambda_ {x _ {i} ^ {i}} \\ \pi_ {x _ {i}} = \sum_ {x _ {p a i}} p \big (x _ {i} | x _ {p a i} \big) \pi_ {x _ {p a i}} \end{array}\tag{8}
$$

where α is a normalizing constant rendering $\sum _ { \boldsymbol { x } _ { i } p ( \boldsymbol { x } _ { i } ) } = 1 ,$ $\pi _ { x _ { p a i } }$ the π message sent from its parent node, and $\lambda _ { X j }$ the λ message from its jth child node.

(2) Bottom-up propagation: If a node x receives λ messages from its child nodes, it also computes a new message: $\lambda _ { x _ { i } } \left( x _ { p a i } \right) =$ $\sum _ { x _ { i } } \lambda ( x _ { i } ) p { \big ( } x _ { i } | x _ { p a i } { \big ) }$ , which is sent to x 's parent node. An evidence node produces a λ message such as $\lambda = ( 0 , . . . , 0 , 1 , 0 , . . . , 0 )$ where the probability of the observed value is one. x 's parent node is then activated for belief updating.

(3) Top-down propagation: If a node x<sub>i</sub> receives π and/or λ messages from its parent and child nodes, it computes a π message to be sent to each of its child nodes: $\pi _ { x _ { i } ^ { j } } = \alpha \pi _ { x _ { i } } \prod _ { k \neq i } \lambda _ { x _ { i } ^ { k } }$ , where α is still a normalizing constant. This process propagates new information coming from x 's parent and child nodes (except the jth node) to $x _ { i } ^ { \prime } s$ jth child node. $x _ { i } ^ { \prime } s$ child nodes that receive the π message are then activated for belief updating.

The belief propagation process begins when a new piece of evidence is introduced to a node sending a 0−1 λ message to the evidence node's parent node and π messages to its child nodes. The λ and π messages are propagated around the network until all the nodes within the network have received belief updates. When the Pearl's algorithm is used during the expectation step of the EM algorithm, the observed values of a data instance (i.e., the comparison of two identity records) are considered as new evidence. Those values will update the probability distributions of the corresponding nodes in the HNB model and change other nodes' probability distributions via λ and π messages. When the propagation is completed, the estimated value for an unknown node (e.g., a missing value node or a latent variable node) is determined as the value that has the highest probability. When the Pearl's algorithm is used to infer an identity matching decision with a trained model, a match decision can be made when the estimated probability of match is greater than that of non-match in the root node (i.e., the Identity Match node in Fig. 5).

## 5. Experiments

In this section we report a systematic evaluation of our proposed BN model for identity matching using real law enforcement data.

## 5.1. A law enforcement dataset

We used the identity records that we collected for our case study as the test bed of our experiments. The collection contained 200 unique identity records that we considered as “suspects”. For each suspect we identi<sup>fi</sup>ed 10 possible matching records in the TPD database as we described in Section 4.2. Each record was represented by a vector of four features: name, DOB, address, and SSN. The training dataset was generated by comparing each suspect's primary identity against each of its possible matches. The dataset contained 2000 comparisons, each of which was represented by a comparison vector and a matching decision label. A matching decision label was set to one if the corresponding comparison was considered to be a true match by the police expert, and zero otherwise.

## 5.2. Performance metrics

We consider identity matching as a classi<sup>fi</sup>cation problem. When we compared a matching decision label predicted by a matching algorithm to the actual label, the result fell into one of the four categories de<sup>fi</sup>ned in Table 5.

We measured the performance of our proposed model using the following three measures: recall, precision, and F-measure. Those measures are widely used in information retrieval and text mining [36]. Precision, in this scenario, is de<sup>fi</sup>ned as the percentage of correctly detected matching identities in all matching identities suggested by the algorithm. Recall is the percentage of matching identities that are correctly identi<sup>fi</sup>ed. F-measure is a well-accepted single measure that combines both recall and precision.

Categories of Classi<sup>fi</sup>cation Results.

<table><tr><td></td><td>Actual label = 1</td><td>Actual label = 0</td></tr><tr><td>Predicted label = 1</td><td>True positive (TP)</td><td>False positive (FP)</td></tr><tr><td>Predicted label = 0</td><td>False negative (FN)</td><td>True negative (TN)</td></tr></table>

$$
\text { Recall } = \frac {T P}{T P + F N}\tag{9}
$$

$$
\text { Precision } = \frac {T P}{T P + F P}\tag{10}
$$

$$
\mathrm{F-measure} = \frac {2 * \text {precision} * \text {recall}}{\text {precision} + \text {recall}}\tag{11}
$$

## 5.3. Experimental design

## 5.3.1. Hypotheses

In our experiments we compared the performance of our proposed model to that of the two existing identity matching techniques, namely the exact-match based technique [29] and the record comparison algorithm [40]. We also evaluated the performance differences of our model in three different learning modes: supervised, semi-supervised, or unsupervised learning. The following hypotheses were tested in our experiments.

Hypothesis 1. The HNB model with semi-supervised learning can achieve an F-measure comparable to that with supervised learning. □

Hypothesis 2. The HNB model with semi-supervised learning can achieve a higher F-measure than that with unsupervised learning. □

Hypothesis 3. The HNB model can achieve a higher F-measure than the exact-match based technique. □

Hypothesis 4. The HNB model can achieve a higher F-measure than the record comparison algorithm. □

## 5.3.2. Testing procedure

5.3.2.1. The exact-match based technique. A 10-fold validation procedure was adopted. We randomly divided the training dataset into 10 subsets. For each subset, we compared each identity to every other identity in the same subset using the exact-based matching heuristic. The predicted class label of a comparison was assigned the value one (i.e., a match) only when the <sup>fi</sup>rst name, last name, and DOB values of one identity were identical to those of the other identity being compared. Precision, recall, and F-measure were calculated for each subset.

5.3.2.2. The record comparison algorithm. We also used a 10-fold validation method here. After randomly dividing the dataset into 10 subsets, each time we used 9 subsets for training in which a threshold value was determined. With the other subset for testing, we computed a similarity score for every pair of identities in that subset. Only when the similarity score is greater than the threshold value determined in the training, we consider the two identities as matching.

5.3.2.3. The HNB model. During the training process, the EM algorithm estimated the parameters of the HNB model using 9 subsets. During the testing, we compared every pair of identity in the other subset and used Pearl's inference algorithm [32] to calculate the probability that the two identities match. The predicted class label was assigned the value one when the probability was greater than 0.5 (i.e., the probability of matching is greater than that of not-matching), or zero otherwise. To implement semi-supervised learning, we controlled the ratio of unlabeled instances by randomly removing class labels from a percentage of training instances. When the percentage was set to zero (i.e., no class labels were removed), the learning became supervised. We increased the percentage by 10% each time until all class labels of training instances were removed, and it became unsupervised learning. In unsupervised learning the prime M step of the EM algorithm cannot apply due to the absence of labeled instances. Instead, we started with a prime E step that randomly assigned class labels to all training instances. The M step therefore can follow the prime E step and is followed by the iteration of the EM algorithm.

Table 6 Experimental results.

<table><tr><td colspan="3"></td><td>Precision</td><td>Recall</td><td>F-Measure</td></tr><tr><td colspan="3">Exact-match based technique</td><td>0.9667</td><td>0.0291</td><td>0.0560</td></tr><tr><td colspan="3">Record comparison algorithm</td><td>0.6401</td><td>0.9073</td><td>0.7307</td></tr><tr><td rowspan="11">Hierarchical Naïve Bayes model</td><td colspan="2">Supervised learning</td><td>0.9498</td><td>0.7327</td><td>0.8220</td></tr><tr><td rowspan="9">Semi-supervised learning</td><td>R=0.1</td><td>0.9539</td><td>0.7254</td><td>0.8188</td></tr><tr><td>R=0.2</td><td>0.9495</td><td>0.7303</td><td>0.8229</td></tr><tr><td>R=0.3</td><td>0.9561</td><td>0.7198</td><td>0.8189</td></tr><tr><td>R=0.4</td><td>0.9624</td><td>0.7275</td><td>0.8275</td></tr><tr><td>R=0.5</td><td>0.9551</td><td>0.7261</td><td>0.8206</td></tr><tr><td>R=0.6</td><td>0.9603</td><td>0.7115</td><td>0.8117</td></tr><tr><td>R=0.7</td><td>0.9298</td><td>0.7284</td><td>0.8135</td></tr><tr><td>R=0.8</td><td>0.9648</td><td>0.6746</td><td>0.7859</td></tr><tr><td>R=0.9</td><td>0.9654</td><td>0.6532</td><td>0.7769</td></tr><tr><td colspan="2">Unsupervised learning</td><td>0.1635</td><td>0.5567</td><td>0.2396</td></tr></table>

R is the ratio of unlabeled instances to all instances in a training dataset.  
Values are the average over 10 subsets.

## 5.4. Experimental results

In this section we discuss the experimental results summarized in Table 6 and report <sup>fi</sup>ndings related to each of the four research hypotheses.

## 5.4.1. Hypothesis 1: Semi-supervised learning vs. supervised learning

With varied percentages of unlabeled training instances, the HNB model with semi-supervised learning achieved F-measures ranging from 0.7769 to 0.8188 (Fig. 6). When the percentage was less than or equal to 50%, the F-measure performance of the semi-supervised learning was not statistically different from that of the supervised learning (p-value N0.1). Therefore, we <sup>fi</sup>xed the percentage of unlabeled training instances at 50% in subsequent hypotheses testing. At this level the semi-supervised learning can perform comparably to the supervised learning, but with the least human inputs.

![](/api/attachments/BZWTNAQA/fulltext/images/d84c9cdad98fc6741943f2b1db8bc1b42cae5b979274ede5c06fd36b13b2e46b.jpg)  
Fig. 7. Semi-supervised vs. unsupervised learning.

As the percentage of unlabeled training instances increased, one may notice that the precision of the semi-supervised learning improved slightly while its recall slightly degraded. This may be caused by the uneven class distribution. In our dataset the proportion of minority class instances (i.e., matching instances with class labels equal to one) was less than 11%. The learning favored the majority class more than the minority class (i.e., it was more likely to classify an instance as nonmatching when the feature values of the instance could not suggest a clear winner). In general we found that adding unlabeled instances reduced false positive rates while increasing false negative rates (due to the uneven class distribution).

## 5.4.2. Hypothesis 2: semi-supervised learning vs. unsupervised learning

The HNB model with unsupervised learning achieved low F-measures (with an average of 0.2396) for identity matching (Fig. 7). Statistical t-tests showed that semi-supervised learning signi<sup>fi</sup>cantly outperformed unsupervised learning at all levels (p-values b0.001). Hypothesis 2 was supported. Due to the lack of prior knowledge (i.e., a set of labeled instances), unsupervised learning favored the majority class even more. This led to less true positive and more false negative predictions.

## 5.4.3. Hypothesis 3: HNB model vs. exact-match

Although the exact-match based technique achieved high precision (0.9667), it received a very low average recall (0.0291) as well as a low average F-measure (0.0560) (Fig. 8). The low recall suffered greatly from those matching identities with disagreed name and/or DOB values. As our case study on identity problems indicates, matching identities appear to have similar feature values that are not identical. The proposed BN model with semi-supervised learning performed signi<sup>fi</sup>cantly better than the exact-match technique (p-valuesb0.001). Hypothesis 3 was supported.

![](/api/attachments/BZWTNAQA/fulltext/images/f1b9f92f870e422c8df7e98f79a1c3e3ee8dabc799fd129f3ff9b6ad3f17b45b.jpg)  
Fig. 6. Semi-supervised vs. supervised learning.

![](/api/attachments/BZWTNAQA/fulltext/images/fce41dbf4ff3d459c09a77608f2c5a8f7bcf0bf0dd9368b6845a339cb581ab16.jpg)  
Fig. 8. Semi-supervised vs. exact-match technique learning.

## 5.4.4. Hypothesis 4: HNB model vs. record comparison

The record comparison algorithm achieved an average F-measure of 0.7307 (Fig. 9). The low precision rating (0.6401) indicates that the algorithm produced a relatively large number of false positive matching decisions. Non-matching identities were considered as matching ones when their similarity ratings were greater than the decision threshold. The semi-supervised BN model achieved statistically higher precision and lower recall than the record comparison algorithm. The overall F-measure of the semi-supervised BN model statistically outperformed the record comparison algorithm $( p \mathrm { - v a l u e } = 0 . 0 0 3 2 5 )$ ). Hypothesis 4 was also supported. The semisupervised HNB model is favorable also because it achieved better performance with only 50% training instances labeled. A low recall may be caused by the fact that the BN model is more sensitive to skewed class distribution than the record comparison algorithm. Daskalaki et al. showed that a Bayesian network classi<sup>fi</sup>er provided a lower true negative rating (i.e., a higher false negative rating) than a linear regression classi<sup>fi</sup>er using a dataset with skewed class distribution [10]. Undersampling (i.e., a strati<sup>fi</sup>ed random sampling from the majority class) and oversampling (i.e., replicating instances in the minority class) techniques have been proposed to solve the class distribution problem [5,23]. However, both techniques have drawbacks. Undersampling throws away potentially useful data, while oversampling may lead to data over<sup>fi</sup>tting [41]. We leave the solution to the class distribution problem as a future direction that could further improve the performance of the HNB model.

## 6. Conclusions

Identity information is critical to various organizational practices ranging from customer relationship management to crime investigation. The task of searching for a speci<sup>fi</sup>c identity is dif<sup>fi</sup>cult because multiple identity representations may exist due to issues such as errors and deception. In this paper we proposed a probabilistic HNB model that improved existing identity matching techniques. Experiments showed that the proposed model achieved F-measure ratings signi<sup>fi</sup>cantly better than those of the exact-search based technique. With 50% training instances, the semi-supervised BN model outperformed the fully supervised record comparison algorithm. This training method outperformed both fully supervised and unsupervised learning. Although unsupervised learning required no human intervention, it did not train the model well and performed poorly in the task of identity matching. With only 10% training instances labeled, our proposed technique still achieved a high F-measure of 0.7769.

![](/api/attachments/BZWTNAQA/fulltext/images/d9b8a82f94423f00fde5030b859f2042a94f6f2d07553a0ff45403d70d07ae43.jpg)  
Fig. 9. Semi-supervised HNB model vs. record comparison algorithm

We also have several caveats for this research. First, the identity problems that we studied were drawn from a law enforcement agency dataset. Problems in other domains such as customer relationship management might display characteristics different from those of criminal identities. Second, we assumed that for a pair of matching identities, the value-pairs of individual features would also be matches. This assumption made the learning easier but contradicted the fact that a pair of matching identities may have non-matching feature value-pairs. Lastly, our proposed technique did not consider the privacy and con<sup>fi</sup>dentiality issues that may occur when data are shared across organizations [37].

In the future we will continue to improve our HNB model by expanding our model and the associated identity features. We also plan to develop an identity consolidation and searching tool for our law enforcement research partner including Tucson Police Department and Pima County Sheriff Department. We believe such a system can be useful for law enforcement and intelligence agencies in their <sup>fi</sup>ghting against crime and terrorism.

## Acknowledgment

We would like to thank the Tucson Police Department and the Arti<sup>fi</sup>cial Intelligence Lab at the University of Arizona.

## References

[1] M.R. Anderberg, Cluster Analysis for Applications, Academic Press, New York, 1973.

[2] F.G. Ashby, L.A. Alfonso-Reese, Categorization as probability density estimation Journal of Mathematical Psychology 39 (1995)

[3] F.G. Ashby, N.A. Perrin, Toward a uni<sup>fi</sup>ed theory of similarity and recognition Psychological Review 95 (1) (1988).

[4] M. Bilenko, R. Mooney, W.W. Cohen, P. Ravikumar, S. Fienberg, Adaptive name matching in information integration, IEEE Intelligent Systems 18 (5) (2003).

[5] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classi<sup>fi</sup>cation and Regression Trees, Wadsworth International Group, Belmont, CA, 1984.

[6] D.E. Brown, S.C. Hagen, Data association methods with applications to law enforcement, Decision Support Systems 34 (4) (2003).

[7] H. Chen, J. Schroeder, R. Hauck, L. Ridgeway, H. Atabakhsh, H. Gupta, C. Boarman, K. Rasmussen, A. Clements, Coplink Connect: information and knowledge management for law enforcement, Decision Support Systems 34 (3) (2003).

[8] W. Chung, H. Chen, W. Chang, S. Chou, Fighting cybercrime: a review and the Taiwan experience, Decision Support Systems 41 (3) (2006).

[9] R. Clarke, Human identi<sup>fi</sup>cation in information systems: management challenges and public policy issues, Information Technology & People 7 (4) (1994).

[10] S. Daskalaki, I. Kopanas, N. Avouris, Evaluations of Classi<sup>fi</sup>ers for an Uneven Class Distribution Problem, Applied Arti<sup>fi</sup>cial Intelligence, Taylor and Francis Ltd., 2006.

[11] R. Dechter, Bucket Elimination: A Unifying Framework for Probabilistic Inference, Proceedings of the 12th Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, Portland, Oregon, 1996.

[12] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data via EM algorithm, Journal of the Royal Statistical Society Series b-Methodological 39 (1) (1977).

[13] D. Dey, Entity matching in heterogeneous databases: a logistic regression approach, Decision Support Systems 44 (3) (2008).

[14] D. Dey, S. Sarkar, P. De, A distance-based approach to entity reconciliation in heterogeneous databases, IEEE Transactions on Knowledge and Data Engineering 14 (3) (2002).

[15] J.S. Donath, Identity and deception in the virtual community, in: M. Smith, P. Kollock (Eds.), Communities in Cyberspace, Routledge, London, 1998.

[16] I.P. Fellegi, A.B. Sunter, A theory for record linkage, Journal of the American Statistical Association 64 (328) (1969).

[17] L. Gill, Methods for Automatic Record Matching and Linkage and Their Use in National Statistics, Oxford University, London, Technical Report National Statistics Methodological Series No. 25, National Statistics, 2001.

[18] H. Han, W. Xu, H. Zha, C. Giles, A hierarchical Naïve Bayes mixture model for name disambiguation in author citations, 2005.

[19] D. Heckerman, A Tutorial on Learning with Bayesian Networks, Microsoft Research, Advanced Technology Division, Redwood, WA, MSR-TR-95-06, 1995.

[21] R.A. Johnson, D.W. Wichern, Applied Multivariate Statistical Analysis, Prentice Hall, Englewood Cliffs: N.J, 1989.

[22] G. Jones, E-Commerce and Identity Fraud, Experian Co., UK, 2001.

[23] M. Kubat, S. Matwin, Addressing the Curse of Imbalanced Training Sets: One-Sided Selection, Proceedings of the Fourteenth International Conference on Machine Learning, Nashville, TN, 1997.

[24] H. Langseth, T.D. Nielsen, Classi<sup>fi</sup>cation using hierarchical Naïve Bayes models, Machine Learning journal 63 (2) (2006).

[25] S.L. Lauritzen, The EM algorithm for graphical association models with missing data, Computational Statistics & Data Analysis 19 (1995) (1995).

[26] V.I. Levenshtein, Binary codes capable of correcting deletions, insertions, and reversals, Soviet Physics Doklady 10 (1966).

[27] C. Li, C. Biswas, Unsupervised learning with mixed numeric and nominal data, IEEE Transactions on Knowledge and Data Engineering 14 (4) (2002).

[28] C. Li, E. Chang, H. Garcia-Molina, G. Wiederhold, Clustering for approximate similarity search in high-dimensional spaces, IEEE Transactions on Knowledge and Data Engineering 14 (4) (2002).

[29] B. Marshall, S. Kaza, J. Xu, H. Atabakhsh, T. Petersen, C. Violette, H. Chen, Cross-Jurisdictional Criminal Activity Networks to Support Border and Transportation Security, Proceedings of the 7th Annual IEEE Conference on Intelligent Transportation Systems (ITSC), Washington, D.C., 2004.

[30] A.E. Monge, Matching algorithms within a duplicate detection system, IEEE Data Engineering Bulletin 23 (4) (2000).

[31] K. Nigam, A.K. McCallum, S. Thrun, T. Mitchell, Text classi<sup>fi</sup>cation from labeled and unlabeled documents using EM, Machine Learning 39 (2000).

[32] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Morgan Kaufmann Publishers, San Mateo, CA, 1988.

[33] P. Ravikumar, W.W. Cohen, A Hierarchical Graphical Model for Record Linkage, Proceedings of the 20th Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence (UAI), Banff Park Lodge, Banff, Canada, 2004.

[34] T.C. Redman, The impact of poor data quality on the typical enterprises, Communications of the ACM 41 (3) (1998).

[35] R.C. Russell, Improvements in Indexes, US Patent 1,261,167, 1918.

[36] G. Salton, Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer, Addison-Wesley Pub. 1988

[37] R. Sarathy, K. Muralidhar, Secure and useful data sharing, Decision Support Systems 42 (1) (2006).

[38] M. Singh. Learning Bavesian Networks from Incomplete Data, Proceedings of the 14th National Conference on Artificial Intelligence, 1997.

[39] J.M. Snyder, Online auction fraud: are the auction houses doing all they should or could to stop online fraud? Federal Communications Law Journal 52 (2) (2000).

[40] G. Wang, H. Chen, H. Atabakhsh, Automatically detecting deceptive criminal identities, Communications of the ACM 47 (3) (2004).

[41] G.M. Weiss, F. Provost, The Effect of Class Distribution on Classi<sup>fi</sup>er Learning: An Empirical Study, Department of Computer Science, Rutgers University, 2001.

[42] W.E. Winkler, String Comparator Metrics and Enhanced Decision Rules in the Fellegi-Sunter Model of Record Linkage, Survey Research Methods Section, American Statistical Association, 1990.

[43] W.E. Winkler, Using the EM Algorithm for Weight Computation in the Fellegi– Sunter Model of Record Linkage, Proceedings of the Section on Survey Research Methods, American Statistical Association, 1998.

[44] W.E. Winkler, Methods for Record Linkage and Bayesian Networks, Proceedings of the Section on Survey Research Methods, American Statistical Association, Alexandria, Virginia, 2002.

[45] Y. Yang, G.I. Webb, A Comparative Study of Discretization Methods for Naïve-Bayes Classi<sup>fi</sup>ers, Proceedings of 2002 Paci<sup>fi</sup>c Rim Knowledge Acquisition Workshop, Tokyo, Japan, 2002.

[46] Y. Yang, G.I. Webb, On Why Discretization Works for Naïve-Bayes Classi<sup>fi</sup>ers, Proceedings of the 16th Australian Joint Conference on Arti<sup>fi</sup>cial Intelligence, Perth, Australia, 2003.

[47] H. Zhang, Exploring conditions for the optimality of Naïve Bayes, International Journal of Pattern Recognition and Arti<sup>fi</sup>cial Intelligence 19 (2) (2005).

[48] N. Zhang, Hierarchical latent class models for cluster analysis, The Journal of Machine Learning Research 5 (2004).

[49] N. Zhang, T. Nielsen, F. Jensen, Latent variable discovery in classi<sup>fi</sup>cation models, Arti<sup>fi</sup>cial Intelligence in Medicine 30 (3) (2004).

G. Alan Wang received his M.S. degree in industrial engineering from the Louisiana State University in 2001 and the Ph.D. degree in management information systems at the University of Arizona in 2006. He is currently an Assistant Professor in Business Information Technology at Virginia Tech. He has published papers in the Communications of the ACM, the Journal of the American Society for Information Science and Technology, IEEE Computer, and Journal of Association for Information Systems. His research interests include data heterogeneity and uncertainty, data mining, and knowledge management.

Homa Atabakhsh received her B.S., M.S. (1984), and Ph.D. (1987) in Computer Science from the University of Toulouse in France. She is currently a researcher at Raythoen Co. She was the Associate Director of the COPLINK Center for Excellence and a Principal Research Specialist at the University of Arizona. She was Assistant Professor in Toulouse from Jan. 1988–Jan. 1989. She was employed by the National Research Council of Canada, as Research Scientist, from Jan. 1989 to 1996 and worked in areas such as knowledge based systems, object-oriented design and programming, GUI, applications in Manufacturing and Business. She has also been adjunct lecturer at the University of Ottawa.

Hsinchun Chen received the Ph.D. degree in information systems from New York University, New York, NY, in 1989. He is currently McClelland Endowed Professor of management information systems at the University of Arizona, Tucson. He is a Fellow of IEEE and AAAS. He has authored or co-authored over 260 papers concerning semantic retrieval, search algorithms, knowledge discovery, and collaborative computing. He is an expert in digital library and knowledge management research, and his research has been featured in scientific and information technology publications.
