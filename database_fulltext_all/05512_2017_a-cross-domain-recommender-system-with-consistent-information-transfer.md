---
otero_id: 5512
otero_key: "PJT4P2KQ"
title: "A cross-domain recommender system with consistent information transfer"
authors: "Qian Zhang; Dianshuang Wu; Jie Lu; Feng Liu; Guangquan Zhang"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.10.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(17)30180-X</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2017.10.002</td></tr><tr><td>Reference:</td><td>DECSUP 12883</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>30 March 2017</td></tr><tr><td>Revised date:</td><td>20 July 2017</td></tr><tr><td>Accepted date:</td><td>4 October 2017</td></tr></table>

## Accepted Manuscript

A cross-domain recommender system with consistent information transfer

Qian Zhang, Dianshuang Wu, Jie Lu, Feng Liu, Guangquan Zhang

![](/api/attachments/PJT4P2KQ/fulltext/images/a6b304eb72f9cee622cfaf708bc07a289f5ee96b017505343ae9c6af6a765252.jpg)

Please cite this article as: Qian Zhang, Dianshuang Wu, Jie Lu, Feng Liu, Guangquan Zhang , A cross-domain recommender system with consistent information transfer. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2017.10.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A cross-domain recommender system with consistent information transfer

Qian Zhang, Dianshuang Wu, Jie Lu, Feng Liu, Guangquan Zhang

Decision Systems and e-Service Intelligence Laboratory, Centre for Artificial Intelligence, Faculty of Engineering

and Information Technology, University of Technology Sydney, Australia

E-mail: qian.zhang-11@student.uts.edu.au, dianshuang.wu@uts.edu.au, jie.lu@uts.edu.au, feng.liu-2@student.uts.edu.au, guangquan.zhang@uts.edu.au

## Abstract

Recommender systems provide users with personalized online product and service recommendations and are a ubiquitous part of today’s online entertainment smorgasbord. However, many suffer from cold-start problems due to a lack of sufficient preference data, and this is hindering their development. Cross-domain recommender systems have been proposed as one possible solution. These systems transfer knowledge from one domain that has adequate preference information to another domain that does not. The outlook for crossdomain recommendation is promising, but existing methods cannot ensure the knowledge extracted from the source domain is consistent with the target domain, which may impact the accuracy of the recommendations. To address this challenging issue, we propose a cross-domain recommender system with consistent information transfer (CIT). Knowledge consistency is based on user and item latent groups, and domain adaptation techniques are used to map and adjust these groups in both domains to maintain consistency during the transfer learning process. Experiments were conducted on five real-world datasets in three categories: movies, books, and music. The results for nine cross-domain recommendation tasks show that CIT outperforms five benchmarks and increases the accuracy of recommendations in the target domain, especially with sparse data. Practically, our proposed method is applied into a telecom product recommender system and a business partner recommender system (Smart BizSeeker) to enhance personalized decision making for both businesses and individual customers.

Keywords: Recommender systems, cross-domain recommender system, knowledge transfer, collaborative filtering

# ACCEPTED MANUSCRIPT

## 1. Introduction

Recommender systems, which aim to provide users with personalized services and overcome the information overload problems, have been developed for more than twenty years [1]. The mainly used recommendation techniques are roughly divided into content-based and collaborative filtering-based. Without content restriction, collaborative filtering is more widely used in areas where users express their preferences by rating items, such as movies, books, and music. Over the last two decades, collaborative filtering has been comprehensively explored from basic memory-based methods [2] to various model-based methods such as matrix factorization [3], probabilistic models [4] and deep learning models [5]. However, sparsity, or the cold-start problem, remains the most challenging outstanding issue in collaborative filtering [6]. If a system fails to provide practical support, new users will quickly lose interest and stop using it [7]. To solve the cold-start problem, traditional methods aim to find additional information, such as social network [8], trust [9] or reviews [10] from within the same domain to infer user-item relationships. Unfortunately, additional information is not often available.

However, where there is insufficient data in one domain, such as movies, but relatively rich data in another domain, such as books. Transfer learning can be used to overcome cold-start problems if the two domains are either explicitly or implicitly related [11]. Moreover, transfer learning and collaborative filtering can be combined to extract knowledge from a source domain with sufficient data to increase recommendation accuracy in a target domain. In this way, a newly launched recommender system in one domain is able to benefit from a mature recommender system in another domain. Such systems are known as a cross-domain recommender system (CDRS) [12]. Because of advantages of collaborative filtering, such as its high efficiency and its lack of content restrictions, CDRSs provide relatively high-quality recommendation together with the ability to deal with cold start problems.

CDRSs aim to use information from an alternative source domain in the target domain where sufficient preference data is unavailable. CDRSs are developed into two directions. One collectively uses preference data from both domains, while the other tries to connect the domains through other information, such as the

## ACCEPTED MANUSCRIPT

users’ social relations [13] or the items’ attributes [14]. Our research focuses solely on preference data since it is not restricted by other information and universally applicable. CDRSs based on preference data can be generally divided into two classes. The first class deals with situations where users and items in the source domain are either totally or partially mapped to those in the target domain [15-17]. However, these methods cannot use data without corresponding users or items in the target domain. The second class deals with situations where there are no intersections between the two domains [18, 19]. This scenario is more widely seen in real-world applications. Sharing user ID from different data source is almost impossible due to confidential user information. Our research falls into the scope of CDRS handling preference data without intersections between two domains.

Existing CDRS methods for preference data without intersections between two domains use shared information of users and items despite a lack of direct corresponding between domains. For example, a group of well-clustered users implies similar preference information, and a group of well-clustered items implies similar content information. From such groups, a user group to item group rating pattern, defined as grouplevel knowledge, can be extracted and shared as a compressed form of the original user-item rating matrix. These methods partly alleviate the sparsity problem and increase the prediction accuracy of recommender systems in target domain. However, none positively transfer knowledge to the target domain in a stable manner, which reduces the accuracy of the recommendations when there is shift between domains. Some methods are prone to failure because they use the group-level knowledge matrix directly without ensuring the consistency of the user/item group information is maintained during transfer. Without collectively clustering or adjusting the group-level knowledge, it usually diverges between domains. Obviously, integrating inconsistent knowledge into the target domain causes harm, rather than helping the recommender system. By ensuring the consistency of the knowledge transferred between the domains, we aim to increase the prediction accuracy of CDRSs and overcome some general problems associated with domain shift in real world decision-making applications.

In this paper, we investigate how to effectively transfer knowledge from the source rating matrix to help

## ACCEPTED MANUSCRIPT

increase the prediction accuracy of the recommender system on the target rating matrix. To avoid divergence caused by domains, group level knowledge is extracted on the basis of consistent user/item group information. That is, user/item information should be consistent in each corresponding group from source and target domain. A domain adaptation technique regulates user/item group information in both domains. Then grouplevel knowledge is learned to maximize the overall level of fitting in both domains. Thus, a cross-domain recommender system with consistent information transfer (CIT) is proposed as a knowledge transfer method. The main contributions of this paper are:

(1).A definition for “Consistent knowledge” to answer the essential question of “what to transfer” in CDRSs. We argue that information should be consistent for each user and item group so that group-level knowledge can be shared. In this way, the requirement for when group-level knowledge can be transferred is addressed, which has not been considered by previous CDRSs.

(2).A domain adaptation method that matches and adjusts user and item latent groups to maintain the consistency of group information. The group-level knowledge learned on this basis represents the domains.

(3).An adaptive knowledge transfer method for CDRSs, called CIT. This method lessens the caused by insufficient data in the target domain. It improves the performance of immature recommender systems by transferring knowledge from another related but different domain.

The remainder of the paper is organized as follows. Section 2 contains a review of work related to CDRSs. Section 3 formally defines the problem solved. In Section 4, we present our CIT method in three parts: an overview, the steps, and the conceptual framework of the cross-domain recommender system. Section 5 presents the empirical experiments on five real-world datasets spanning three categories of data. The results for nine tasks in terms of three data sparsity ratios show that our method is better than five existing nontransfer and cross-domain methods. Finally, the discussion, conclusion and directions for future study are provided in Section 6. Guidelines for recommender system developers along with a discussion on the potential industry applications of the proposed method are included.

## 2. Related Work

In this Section, related works about CDRSs are reviewed.

As mentioned in Introduction, two different types of CDRSs have been developed. Some methods that connect two domains through other information rather than preference data are as follows: FUSE [13] integrates social information with preference data by sharing implicit cluster-level tensers from multiple domains. Collective matrix factorization (CMF) [14] factorizes the source rating matrix and the target rating matrix concurrently by sharing parameters when the user or item is found in both domains. This method is especially suitable with item attribute information or information contributed by users.

On the other hand, CDRSs based on preference data can be designed in various ways according to the overlap of users and item, the form the data takes, or the tasks the system needs to handle. Methods dealing with data where user/item partially or fully corresponds in both domains usually collectively factorize two matrixes in each domain by sharing part of the factorization parameters. Cross-domain triadic factorization (CDTF) [17] models the relation of a user-item-domain to extract the interactions of items in different domains. Clustering-based matrix factorization (CBMF) [15] subsequently tried to improve CDTF by utilizing information from unobserved ratings at a cluster level. These two methods work well in situations where users have ratings in multiple domains with different sparsity, i.e., where the user information fully overlaps. A large e-commerce website housing various products or services is a good example. Rating over site-time (ROST) [20] is similar to the two methods above, but it also considers the user-interest drift in different time-windows. In this situation, users/items are partly or fully overlapped. Transfer by collective factorization (TCF) [16] explores how to use implicit binary preference data in the source domain to assist recommendations in the target domain with explicit rating data. Since the data in both domains are heterogeneous, it requires that users and items in the source and target rating matrixes have one-to-one mappings. All these methods above have their own application scenarios, but they cannot be used when data

# ACCEPTED MANUSCRIPT

from two domains have non-overlapped users/items.

Methods that handle two domains with no intersections of users/items usually transfer knowledge between the domains on a group level. Codebook transfer (CBT) [18] extracts knowledge from the source rating matrix as a ‘codebook’. In this method, the source rating matrix must be full; hence, it is filled with the mean ratings of each user. The rating matrix generative model (RMGM) [19] was extended from CBT. It avoids the full matrix limitation by relaxing the hard membership constraint on user/item groups. Our research falls within the scope of methods without any user/item overlap. However, a specific definition of “consistent knowledge” is not given in the existing literature. By default, two rating matrixes take from source and target domains and factorized to acquire the shared knowledge. But in our proposed CIT, we defined how two rating matrixes are consistently tri-factorized and how consistent knowledge can be extracted, which helps to improve the recommendation performance in the target domain. This makes our method different from previous works. The related works in this Section are summarized in Table 1.

Table 1 Summary of related works

<table><tr><td rowspan="3"></td><td colspan="3">user/item overlap</td><td colspan="3">data</td><td colspan="2">tasks</td></tr><tr><td rowspan="2">full overlap</td><td rowspan="2">partly overlap</td><td rowspan="2">non-overlap</td><td colspan="2">preference data only</td><td rowspan="2">Other data needed</td><td rowspan="2">Two domains</td><td rowspan="2">Multi-domain</td></tr><tr><td>heterogeneous</td><td>homogeneous</td></tr><tr><td>FUSE [13]</td><td></td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>CMF [14]</td><td></td><td>×</td><td></td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>CBMF [15]</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td><td></td></tr><tr><td>CDTF [17]</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>TCF [16]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>×</td><td></td></tr><tr><td>CBT [18]</td><td></td><td></td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td></tr><tr><td>RMGM [19]</td><td></td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>ROST [20]</td><td>×</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>our CIT</td><td></td><td></td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td></tr></table>

## 3. Problem Formulation and Motivation

In this section, a factorization view of the recommender system in one domain is given to clearly describe the problem setting. The problem under study in this paper is then formally described. Finally, the motivation of this research is given as an example.

## 3.1 Recommendation Task based on Tri-factorization in One Domain

In a single domain, suppose there are ?? users and ?? items. The relationship between the users and the items is represented by the user-item rating matrix $\pmb { X } \in \mathbb { R } ^ { M \times N }$ (bold letters represent a matrix). Any rating $r _ { i j }$ in ?? is subject to $r _ { i j } \in \{ 1 , 2 , 3 , 4 , 5 , ? \}$ $( ^ { 6 6 } ? ^ { 5 }$ denotes a missing value). To construct the group-level knowledge matrix, users and items are clustered. The rating matrix ?? can be factorized into three matrixes [21]: $\pmb { X } = \pmb { U } \pmb { S } \pmb { V } ^ { T }$ , where $\pmb { U } \in \mathbb { R } ^ { M \times K }$ is the user-group membership matrix, $V \in \mathbb { R } ^ { N \times L }$ is the item-group membership matrix, and $\pmb { S } \in \mathbb { R } ^ { K \times L }$ is the group-level knowledge matrix. Each row of ?? and ?? contains the memberships of the user/item entity for all groups. ?? is the rating pattern of each user group to each item group.

The recommendation task requires the prediction of user ratings for items where the rating values are not known. To calculate the missing values, the user-item rating matrix is reconstructed through $\widehat { \pmb { X } } = \pmb { U } \pmb { S } \pmb { V } ^ { T }$ . Trifactorization of ?? minimizes the loss function $L ( X , U S V ^ { T } )$ , which measures the error of prediction. Since ?? is usually sparse, the loss function is in a weighted form as follows:

$$
L (\boldsymbol {X}, \boldsymbol {U} \boldsymbol {S} \boldsymbol {V} ^ {T}) = \| \boldsymbol {W} \odot (\boldsymbol {X} - \boldsymbol {U} \boldsymbol {S} \boldsymbol {V} ^ {T}) \| ^ {F}\tag{1}
$$

where ⊙ denotes the element-wise product of matrixes, and ?? is the indicator matrix representing whether e-domain recommendation, $\pmb \theta = \{ \pmb U , S , \pmb V \}$ are the parameters the recommender system uses to predict the ratings and provide a recommendation. The tri-factorization is

$$
\min L (\boldsymbol {X}, \boldsymbol {U S V} ^ {T})
$$

$$
s. t. \boldsymbol {U} > 0, \boldsymbol {S} > 0, \boldsymbol {V} > 0
$$

## 3.2 Cross-domain Transfer Learning Recommender System

As mentioned in the Introduction, users and items are usually denoted by de-identified user and item IDs, it is often difficult to find an explicit correlation between the two domains. In this problem setting, the users/items have no correspondence across the domains and are treated as completely different users/items. We assume that explicit rating data are available for both the source and target domains. Formally, the problem is defined as:

Definition 1 (Cross-domain Transfer Learning Recommender System). Given a source rating matrix $X _ { s } \in$ ℝ ${ M _ { s } } { \times } { N _ { s } }$ and a target rating matrix $\pmb { X } _ { t } \in \mathbb { R } ^ { M _ { t } \times N _ { t } }$ , a cross-domain transfer learning recommender system aims to help recommendation tasks in the target domain predict the rating $\widehat { X } _ { t } = U _ { t } S _ { t } V _ { t } ^ { T }$ using knowledge in the source rating matrix $X _ { s }$ and $\pmb { \theta } _ { s } = \{ \pmb { U } _ { s } , \pmb { S } _ { s } , \pmb { V } _ { s } \}$ , where $P _ { s } \cap P _ { t } = \emptyset$ and $Q _ { s } \cap Q _ { t } = \emptyset . \ : P _ { s }$ and $Q _ { s }$ represent the user set and item set in the source domain, while $P _ { t }$ and $Q _ { t }$ represent the user set and item set in the target domain.

## 3.3 Motivation for developing CIT

A CDRS for movies serves as a good example for describing this problem. Consider three movie rating websites. Two sites focus on classic movies (the source domain and target domain 1); the other only contains second-rate movies (target domain 2). Fig. 1 illustrates three scenarios.

Scenario 1: Users 1-4 in Fig. 1 (a) and users 7-10 in Fig. 1 (b). Although the chosen movies have different origins, all the movie subsets from the source domain and target domain 1 are quite similar. Users 1-4 in the source domain and users 7-10 in the target domain 1 also have similar movie preferences; hence, the user and item groups contain similar information in the source and target domains. In this first scenario, using the group-level knowledge directly in the target domain is effective even though there is no group-matching module.

Scenario 2: Users 5, 6 in Fig. 1 (a) and users 11, 12 in Fig. 1 (b). UG6 in target domain 1 has completely different information to UG3 in the source domain. Because the group-level knowledge is inconsistent (here, due to the user preference information), directly transferring that knowledge from source domain to target domain will impair the performance of the CDRS.

Scenario 3: Users 1-6 in Fig. 1 (a) and users 13-18 in Fig. 1 (c). As in scenario 2, UGs 7-9 have completely different group information from UGs 1-3 in the source domain, as is the case with IG 1-3 and IG 7-9. Here, both the user preference information and the item content information are inconsistent. As a result, using knowledge extracted from the source domain in target domain 2 may produce even poorer recommendations than from a recommender system that was built solely from target domain 2.

These scenarios reflect the knowledge inconsistency problem that existing CDRSs are unable to deal with. Using knowledge from another domain without mapping and adjustment only helps to produce a more

## ACCEPTED MANUSCRIPT

accurate prediction if there is no significant divergence between the source domain and target domain. The CIT method, described in the following section, helps to solve the problem.

![](/api/attachments/PJT4P2KQ/fulltext/images/9d5377bbaf75fcb751d1eb25cb2b1a610b0e93f1fa88ca50dc7b9acc6b71061a.jpg)  
(c) Recommender system in target domain 2  
Fig. 1. An example for CDRS.

(a)-(c) Recommender systems for a source domain, target domain 1 and target domain 2. The left side shows the schematic rating matrixes; the right side shows the group-level knowledge matrixes. These represent possible groups of users and items from the left-side rating matrixes. The possible user/item group semantic meanings are annotated as UG - user group and IG - item group.

## 4. A Cross-domain Recommender System with Consistent Information Transfer

This section introduces our CIT method beginning with an overview of the entire procedure. Each of the five steps of the method are then presented in detail followed by the system architecture to support decisionmaking for individuals and businesses.

## 4.1 CIT Method Overview

The proposed CIT method uses a domain adaptation technique to ensure that knowledge extracted from the source domain is consistent with the target domain and that knowledge transfer is positive. The procedure consists of five steps, as shown in Fig. 2. 1). Users/items from the source and target domains are clustered separately into groups. 2). Domain adaptation techniques are used to generate consistent user/item latent groups in the source and target domains. 3). Consistent knowledge is extracted from the latent groups. 4). Group representations in the target domain are adjusted to retain their domain-specific characteristics. 5). A recommender system for the target domain is built. We use a specific algorithm for each step, but other clustering or domain adaptation algorithms could be substituted.

![](/api/attachments/PJT4P2KQ/fulltext/images/60d40ad8d283bf7db83d7382f0a3847c6244c6bec83b78d948036ba839197168.jpg)  
Fig. 2. The CIT method procedure  
Note: The notations in the figure correspond to the equations that follow in this section.

## 4.2 CIT Method

Our proposed CIT method consists of five steps.

# ACCEPTED MANUSCRIPT

## 4.2.1 Step 1: Clustering of users and items in both domains

This step clusters users and items into groups. Clustering users and items appropriately is a crucial issue. Intuitively, users may have various preferences and items may have diverse content. Therefore, it is usually more appropriate to allow both users and items to fall into multiple groups with different memberships. Thus, in this paper, a flexible mixture model (FMM) [22] is used to cluster the users and items separately. The same clustering procedure is used for both the source domain and the target domain; however, for simplicity, we have only provided the description for one domain.

Suppose users are clustered into ?? user groups $\left\{ Z _ { u } ^ { ( 1 ) } , \ldots , Z _ { u } ^ { ( K ) } \right\}$ while items are clustered into ?? item groups $\Big \{ Z _ { v } ^ { ( 1 ) } , \ldots , Z _ { v } ^ { ( L ) } \Big \} . Z _ { u }$ and $Z _ { v }$ are two latent variables that denote the user and item groups respectively. $P ( Z _ { u } | u )$ is the conditional probability of a user belonging to a user group, denoting the group membership of the user; $P ( Z _ { v } | v )$ is the conditional probability of an item belonging to an item group, denoting its group membership. Each user group has a rating preference for each item group. ?? is the variable representing the preference of user groups to item groups. $P ( r | Z _ { u } , Z _ { v } )$ is the conditional probability of ?? given user group $Z _ { u }$ and item group $Z _ { v }$ . The rating for a coupled user-item pair is:

$$
R (u, v) = \sum_ {r} r \sum_ {Z _ {u}, Z _ {v}} P (r | Z _ {u}, Z _ {v}) P (Z _ {u} | u) P (Z _ {v} | v)\tag{2}
$$

Equation (2) can be rewritten into matrix form:

$$
\boldsymbol {X} = \boldsymbol {U} \boldsymbol {S} \boldsymbol {V} ^ {T}\tag{3}
$$

where $\pmb { U } \in \mathbb { R } ^ { M \times K }$ $V \in \mathbb { R } ^ { N \times L }$ are the user and item group membership matrix. $\pmb { U } _ { i j }$ represents the $u _ { i }$ $Z _ { u } ^ { ( j ) } . \pmb { U } _ { i * }$ is the ??th row of matrix ?? representing membership of user $u _ { i }$ to each group. $\pmb { U } _ { * j }$ is the ??th column of matrix ?? representing the membership of each user to user group $Z _ { u } ^ { ( j ) }$ . The same goes for items. $\pmb { S } \in \mathbb { R } ^ { K \times L }$ is the group-level knowledge matrix. $\pmb { S } _ { i j }$ represents the preference of user group $Z _ { u } ^ { ( i ) }$ for item group $Z _ { v } ^ { ( j ) }$

After clustering, the user group and item group membership matrixes ${ \pmb U } _ { s } ^ { ( 0 ) } , { \pmb V } _ { s } ^ { ( 0 ) }$ are acquired for the source domain and ${ \pmb U } _ { t } ^ { ( 0 ) } , { \pmb V } _ { t } ^ { ( 0 ) }$ for the target domain.

$$
\pmb {U} _ {\pmb {s}} ^ {(\mathbf {0})} = P \big (Z _ {u _ {s}} | u _ {s} \big), \pmb {V} _ {\pmb {s}} ^ {(\mathbf {0})} = P \big (Z _ {v _ {s}} | v _ {s} \big)\tag{4}
$$

$$
\pmb {U} _ {\pmb {t}} ^ {(\mathbf {0})} = P \big (Z _ {u _ {t}} | u _ {t} \big), \pmb {V} _ {\pmb {t}} ^ {(\mathbf {0})} = P \big (Z _ {v _ {t}} | v _ {t} \big)\tag{5}
$$

where

$$
P (Z _ {u} | u) = \frac {P (u | Z _ {u}) P (Z _ {u})}{\sum_ {Z _ {u}} P (u | Z _ {u}) P (Z _ {u})} \quad \mathrm{and} \quad P (Z _ {v} | v) = \frac {P (v | Z _ {v}) P (Z _ {v})}{\sum_ {Z _ {v}} P (v | Z _ {v}) P (Z _ {v})}\tag{parameters}
$$

$P ( u | Z _ { u } ) , P ( v | Z _ { v } ) , P ( r | Z _ { u } , Z _ { v } ) , P ( Z _ { u } )$ and $P ( Z _ { v } )$ are learnt from the FMM (for details, see [22]).

## 4.2.2 Step 2: Domain adaptation of the user and item groups

This step ensures information consistency between the user/item group membership matrixes of two domains. The original user group membership matrixes ${ \pmb U } _ { s } ^ { ( 0 ) } , { \pmb U } _ { t } ^ { ( 0 ) }$ $V _ { s } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) }$ from the source and target domains are used as the starting point.

In one domain (say, the source domain), each column $\pmb { U } _ { s * j } ^ { ( 0 ) }$ represents the memberships of all users in a user group ??. Thus, it is reasonable to use the marginal probability distribution of column $U _ { s * j } ^ { ( 0 ) }$ to represent the characteristics of the user group information from user group ??. This is also applied to the other three matrixes $V _ { s } ^ { ( 0 ) } , U _ { t } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) }$ . The disparity of the marginal probability distributions of user/item group membership matrixes in both domains is used to measure the divergence of the user/item group information. If the marginal probability distributions of the memberships of the two user/item groups are the same, these two user/item groups are regarded as having the same characteristics and the same physical meanings – information in the two user/item groups is consistent. This provides a method to measure the similarity between latent user/item groups in both domains. According to the basic assumption of recommender systems, i.e., “similar users like similar items”, the preferences of similar user groups to similar item groups can be shared. Therefore, if the user/item group information of two domains is consistent, this group-level knowledge can be shared by both domains. The following formal definition of consistent user/item information and consistent knowledge determines which knowledge is transferrable.

Definition 2 (Information-consistent Tri-factorization). Given a source rating matrix $\pmb { X _ { s } } \in \mathbb { R } ^ { M _ { s } \times N _ { s } }$ and a target rating matrix, $\boldsymbol { X } _ { t } \in \mathbb { R } ^ { M _ { t } \times N _ { t } } , \boldsymbol { X } _ { s }$ and $X _ { t }$ can be factorized based on nonnegative tri-factorization:

$$
\boldsymbol {X} _ {s} = \boldsymbol {U} _ {s} ^ {(\mathbf {0})} \boldsymbol {S} _ {s} ^ {(\mathbf {0})} \left(\boldsymbol {V} _ {s} ^ {(\mathbf {0})}\right) ^ {T}\tag{6}
$$

$$
\boldsymbol {X} _ {t} = \boldsymbol {U} _ {t} ^ {(\mathbf {0})} \boldsymbol {S} _ {t} ^ {(\mathbf {0})} \left(\boldsymbol {V} _ {t} ^ {(\mathbf {0})}\right) ^ {T}\tag{7}
$$

If both tri-factorizations satisfy the following equations, then they are information-consistent trifactorizations.

$$
P \Big (\boldsymbol {U} _ {s} ^ {(\mathbf {0})} \Big) = P \Big (\boldsymbol {U} _ {t} ^ {(\mathbf {0})} \Big)\tag{8}
$$

$$
P \Big (\boldsymbol {V} _ {s} ^ {(\mathbf {0})} \Big) = P \Big (\boldsymbol {V} _ {t} ^ {(\mathbf {0})} \Big)\tag{9}
$$

where $P \Big ( U _ { s } ^ { ( 0 ) } \Big )$ and $P \left( V _ { s } ^ { \left( 0 \right) } \right)$ represent the marginal probability distributions of ${ \pmb U } _ { s } ^ { ( 0 ) }$ and $V _ { s } ^ { ( 0 ) }$ , respectively. We say that the user group information from ${ \pmb U } _ { s } ^ { ( 0 ) }$ and ${ \pmb U } _ { { \pmb t } } ^ { ( { \pmb 0 } ) }$ is consistent, and the item group information from $V _ { s } ^ { ( 0 ) }$ and $V _ { t } ^ { ( 0 ) }$ is consistent. That is, the user/item groups from source and target domains are consistent. ${ \pmb S } _ { s } ^ { ( 0 ) }$ is the “consistent knowledge” of the two matrixes $X _ { s }$ <sub>??</sub> and $X _ { t }$

According to this definition, if the marginal probability distributions of user/item groups from source and target domains are the same, the group-level knowledge matrix can be shared, so that the consistent knowledge ${ \pmb S } _ { s } ^ { ( 0 ) }$ can be directly used for the target rating matrix (let ${ \pmb S } _ { t } ^ { ( 0 ) } = { \pmb S } _ { s } ^ { ( 0 ) } )$ ). If the marginal probability distributions of the user/item group membership matrixes in both domains are not the same, we need to find other tri-factorization results that satisfy the conditions in Definition 2. Looking for a solution by trying different kinds of existing matrix factorization techniques is unattainable and time-consuming. Instead, we seek the solution by aligning consistent latent user groups and item groups through domain adaptation techniques. By adjusting the marginal probability distributions of user and item groups from the source and target domains comparatively, the similarities between the latent user and item groups are maximized. Consistent knowledge can then be extracted from the source rating matrix which can be directly used to help predict ratings in the target rating matrix.

To align consistent latent user and item groups, we need to find a projection to adjust the user/item group information of both rating matrixes so that the following equations are achieved:

$$
P \left(\boldsymbol {\Psi} _ {s} \left(\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)}\right)\right) = P \left(\boldsymbol {\Psi} _ {t} \left(\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)}\right)\right)\tag{10}
$$

$$
P \left(\boldsymbol {\Phi} _ {s} \left(V _ {s} ^ {(0)}, V _ {t} ^ {(0)}\right)\right) = P \left(\boldsymbol {\Phi} _ {t} \left(V _ {s} ^ {(0)}, V _ {t} ^ {(0)}\right)\right)\tag{11}
$$

It is apparent that $\boldsymbol { \psi } _ { s } , \boldsymbol { \psi } _ { t } , \boldsymbol { \Phi } _ { s }$ and $\Phi _ { t }$ are the keys to ensuring that the latent groups remain consistent in both domains. We need to find maps that can force different distributions to become the same after mapping. A geodesic flow kernel (GFK) [23] is a domain adaptation strategy for learning robust features that is flexible against mismatch across domains and can be used to find a space for data in two domains to project into, so that the data distributions of the two domains in the projected space are similar. After projecting a GFK, a new representation is learned that satisfies the condition in Definition 2. Thus, we use a GFK to map $U _ { s } ^ { ( 0 ) } , U _ { t } ^ { ( 0 ) } , V _ { s } ^ { ( 0 ) }$ and $V _ { t } ^ { ( 0 ) }$ to $U _ { s } ^ { ( 1 ) } , U _ { t } ^ { ( 1 ) } , V _ { s } ^ { ( 1 ) }$ and $\pmb { V } _ { t } ^ { ( 1 ) }$ . Based on the details of GFK, $\boldsymbol { \psi } _ { s } , \boldsymbol { \psi } _ { t } , \boldsymbol { \Phi } _ { s } ,$ and $\pmb { \phi } _ { t }$ can be written as follows:

$$
\boldsymbol {\Psi} _ {s} \Big (\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)} \Big) = \boldsymbol {\Psi} _ {G} \Big (\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)} \Big) \times \boldsymbol {f} _ {z s} \Big (\boldsymbol {U} _ {s} ^ {(0)} \Big)\tag{12}
$$

$$
\pmb {\Psi} _ {t} \Big (\pmb {U} _ {s} ^ {(0)}, \pmb {U} _ {t} ^ {(0)} \Big) = \pmb {\Psi} _ {G} \Big (\pmb {U} _ {s} ^ {(0)}, \pmb {U} _ {t} ^ {(0)} \Big) \times \pmb {f} _ {z s} \Big (\pmb {U} _ {t} ^ {(0)} \Big)\tag{13}
$$

$$
\Phi_ {s} \Big (V _ {s} ^ {(0)}, V _ {t} ^ {(0)} \Big) = \Phi_ {G} \Big (V _ {s} ^ {(0)}, V _ {t} ^ {(0)} \Big) \times f _ {z s} \Big (V _ {s} ^ {(0)} \Big)\tag{14}
$$

$$
\boldsymbol {\Phi} _ {t} \left(V _ {s} ^ {(0)}, V _ {t} ^ {(0)}\right) = \boldsymbol {\Phi} _ {G} \left(V _ {s} ^ {(0)}, V _ {t} ^ {(0)}\right) \times \boldsymbol {f} _ {z s} \left(V _ {t} ^ {(0)}\right)\tag{15}
$$

where $\pmb { \psi } _ { G } \Big ( U _ { s } ^ { ( 0 ) } , U _ { t } ^ { ( 0 ) } \Big )$ and $\phi _ { G } \Big ( V _ { s } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) } \Big )$ are the operators of the GFK method and $\pmb { f } _ { z s } ( \cdot )$ is the function of Z-score. More details on $\pmb { \psi } _ { G } \Big ( \pmb { U } _ { s } ^ { ( 0 ) } , \pmb { U } _ { t } ^ { ( 0 ) } \Big )$ and $\Phi _ { G } \Big ( V _ { s } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) } \Big )$ can be found in Appendix A.

Then, the adapted latent user groups of the two rating matrixes can be obtained, which are expressed as

$$
\boldsymbol {U} _ {s} ^ {(1)} = \boldsymbol {\Psi} _ {s} \left(\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)}\right)\tag{16}
$$

$$
\boldsymbol {U} _ {t} ^ {(1)} = \boldsymbol {\Psi} _ {t} \left(\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)}\right)\tag{17}
$$

The same goes for the item groups: $V _ { s } ^ { ( 1 ) } = \Phi _ { s } \Big ( V _ { s } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) } \Big ) , V _ { t } ^ { ( 1 ) } = \Phi _ { t } \Big ( V _ { s } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) } \Big ) . U _ { s } ^ { ( 1 ) } , U _ { t } ^ { ( 1 ) }$ are user group membership matrixes unified to the same domain-invariant feature space for the source and target domains, while $\pmb { V } _ { s } ^ { ( 1 ) }$ and $\pmb { V } _ { t } ^ { ( 1 ) }$ are unified item group membership matrixes.

## ACCEPTED MANUSCRIPT

Here, an example best illustrates the domain adaptation process of the user and item group information. Consider a source domain and a target domain that both have 1000 non-overlapped users. In each domain, the users are clustered into six user groups, with inconsistent user group information between the source and target domains. The probability distributions of the first user group (the first column of ${ \pmb U } _ { s } ^ { ( 0 ) }$ and ${ \pmb U } _ { t } ^ { ( 0 ) } )$ is shown in Fig. 3 (a); each is quite different. To force consistency, the information for every user group in each domain is adjusted, after which the user group information of the adapted matrixes $\pmb { U } _ { s } ^ { ( 1 ) }$ and ${ \pmb U } _ { t } ^ { ( 1 ) }$ is almost the same, as shown in Fig. 3 (b).

![](/api/attachments/PJT4P2KQ/fulltext/images/222c0061355cfacab4baed5c14ca07508ffcd56635e1e3feed7cfc1c73142208.jpg)  
(a) Distribution before adjustment

![](/api/attachments/PJT4P2KQ/fulltext/images/bd096ae730c1952b617956e71ec497238e3700cf32c2d8f8732ac9fac70fc24f.jpg)  
(b) Distribution after adjustment  
Fig. 3. An example of user group information adjustment in two domains

Note: (a) Marginal probability distribution of the first column in ${ \pmb U } _ { s } ^ { ( 0 ) }$ and ${ \pmb U } _ { { \pmb t } } ^ { ( 0 ) }$ , (b) Marginal probability distribution of the first column in $\pmb { U } _ { s } ^ { ( 1 ) }$ and ${ \pmb U } _ { t } ^ { ( 1 ) }$ .

## 4.2.3 Step 3: Consistent knowledge extraction

After the domain adaptation, ${ \pmb U } _ { s } ^ { ( 1 ) } , { \pmb U } _ { t } ^ { ( 1 ) }$ are consistent, and $V _ { s } ^ { ( 1 ) } , V _ { t } ^ { ( 1 ) }$ are consistent. Once we have obtained consistent group representations that are meaningful across both rating matrixes, the model trained on the source rating matrix and the target rating matrix can be brought together. On this basis, the recommender systems learned from the source and target domains will share the same group-level knowledge matrix ??.

Consistent knowledge ?? is obtained by maximizing the approximation of the available data in both the source rating matrix and the target rating matrix by approximating $\pmb { X _ { s } } \approx \pmb { U _ { s } ^ { ( 1 ) } } \pmb { S } \Big ( \pmb { V _ { s } ^ { ( 1 ) } } \Big ) ^ { T }$ together with $X _ { t } \approx$ $U _ { t } ^ { ( 1 ) } S \Big ( V _ { t } ^ { ( 1 ) } \Big ) ^ { T }$ . To qualify the approximation, one useful and simple measure is to use a Frobenius norm between the original rating matrix and the approximation. We have the following cost function:

$$
J _ {s} (\pmb {S}) = \frac {1}{M _ {s} N _ {s}} \left\| \pmb {W} _ {s} \odot \left(\pmb {X} _ {s} - \pmb {U} _ {s} ^ {(\mathbf {1})} \pmb {S} \left(\pmb {V} _ {s} ^ {(\mathbf {1})}\right) ^ {T}\right) \right\| _ {F} + \frac {1}{M _ {t} N _ {t}} \left\| \pmb {W} _ {t} \odot \left(\pmb {X} _ {t} - \pmb {U} _ {t} ^ {(\mathbf {1})} \pmb {S} \left(\pmb {V} _ {t} ^ {(\mathbf {1})}\right) ^ {T}\right) \right\| _ {F} + \frac {1}{2 K L} \lambda \| \pmb {S} \| _ {F}\tag{18}
$$

where ${ \pmb W } _ { s }$ is a binary weighting matrix for $X _ { s } , [ W _ { s } ] _ { i j } = 1 , { \mathrm { i f } } [ X _ { s } ] _ { i j } \neq 0$ and $[ { \pmb W } _ { s } ] _ { i j } = 0$ , otherwise. The same applies to ${ \pmb W } _ { t }$ for $\pmb { X } _ { t } . \odot$ is an entry-wise product, λ is the parameter for regularization.

Since the physical meaning of ?? is the preference that the user groups give to the item groups, it should be in range of (0,5]. Regularization to constrain the range of ?? is added to the cost function. Finally, consistent knowledge is learned through the following optimization problem:

$$
\begin{array}{l} \min J _ {s} (\boldsymbol {S}) \\ s. t. \boldsymbol {S} > 0 \end{array}
$$

Gradient descent is a general algorithm for optimization, which leads to the update rule: $s _ { a b } \gets s _ { a b } +$ $\eta _ { a b } \frac { \partial J _ { s } } { \partial S _ { a b } }$ . For this problem, we need to constrain the non-negativity of S. The partial derivative of the cost function has a special form, so we can use tricks to set the learning rate $\eta _ { a b } = { ^ { ( S ) } } _ { a b } \Big / \Big ( A + B + { \textstyle \frac { \lambda S } { 2 K L } } \Big ) _ { a b }$ to guarantee that ?? is nonnegative, where $\begin{array} { r } { A = \frac { 1 } { M _ { s } N _ { s } } \Big ( U _ { s } ^ { ( 1 ) } \Big ) ^ { T } \Bigg ( W _ { s } \odot \Big ( U _ { s } ^ { ( 1 ) } S \Big ( V _ { s } ^ { ( 1 ) } \Big ) ^ { T } \Big ) \Bigg ) V _ { s } ^ { ( 1 ) } } \end{array}$ $B =$ Y $\begin{array} { r } { \frac { 1 } { M _ { t } N _ { t } } \Big ( U _ { t } ^ { ( 1 ) } \Big ) ^ { T } \Bigg ( W _ { t } \odot \Big ( U _ { t } ^ { ( 1 ) } S \Big ( V _ { t } ^ { ( 1 ) } \Big ) ^ { T } \Big ) \Bigg ) V _ { t } ^ { ( 1 ) } } \end{array}$ . The objective function is non-increasing under the following update rule:

$$
S _ {a b} \leftarrow S _ {a b} \frac {\left(\frac {1}{M _ {s} N _ {s}} \Big (U _ {s} ^ {(1)} \Big) ^ {T} X _ {s} V _ {s} ^ {(1)} + \frac {1}{M _ {t} N _ {t}} \Big (U _ {t} ^ {(1)} \Big) ^ {T} X _ {t} V _ {t} ^ {(1)}\right) _ {a b}}{\Big (A + B + \frac {\lambda S}{2 K L} \Big) _ {a b}}\tag{19}
$$

The learning process is summarized in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Consistent Knowledge Extraction
Input: $X_s$, the source rating matrix
$X_t$, the target rating matrix
$U_s^{(1)}, V_s^{(1)}$, user and item membership matrix of source domain
$U_t^{(1)}, V_t^{(1)}$, user and item membership matrix of target domain
$(U_s^{(1)}, V_s^{(1)}, U_t^{(1)}, V_t^{(1)}$ are obtained from GFK algorithm)
Output: $S$, the consistent knowledge
1 INITILIZE $S \in \mathbb{R}^{K \times L}$, $J_s^{(\min)} \leftarrow 0$, $J_s \leftarrow 0$
2 WHILE $J_s = 0$ OR $J_s - J_s^{(\min)} &gt; \varepsilon$ DO
3 FOR each element $s_{ab}$ in $S$ DO
4 UPDATE $s_{ab}$ as in equation (19)
5 ENDFOR
</div>

## ACCEPTED MANUSCRIPT

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
6 UPDATE  $J_{s}$  as in equation (18)
7 IF  $J_{s}^{(min)} &gt; J_{s}$ 
8  $J_{s}^{(min)} = J_{s}$ 
9 ENDIF
10 ENDWHILE
11 RETURN S
</div>

## 4.2.4 Step 4: Group representation regulation

The domain adaptation technique GFK is designed for unsupervised transfer learning where no label is available in the target domain. In this problem setting, some domain-specific characteristics are embedded in the small amount of available data in the target rating matrix. To reveal these idiosyncrasies of the target domain, we amend the group representations of the target rating matrix to make the model fit better to the task in target rating matrix. It is imperative that we find maps $f _ { u } \colon U _ { t } ^ { ( 1 ) } \longmapsto \mathbb { R } ^ { M _ { t } \times K }$ and $f _ { v } \colon V _ { t } ^ { ( 1 ) } \longmapsto \mathbb { R } ^ { N _ { t } \times L }$ to make ${ \pmb U } _ { t } ^ { ( 1 ) }$ and $\pmb { V } _ { t } ^ { ( 1 ) }$ more suitable for the target rating matrix. At the same time, the adjustment should not impair the consistency of user groups and item groups between two domains. According to Definition 2, $f _ { u }$ and $f _ { v }$ should satisfy the following equation:

$$
P \left(\boldsymbol {S} \left| f _ {u} \left(\boldsymbol {U} _ {\boldsymbol {t}} ^ {(1)}\right), f _ {v} \left(\boldsymbol {V} _ {\boldsymbol {t}} ^ {(1)}\right)\right) = P \left(\boldsymbol {S} \mid \boldsymbol {U} _ {\boldsymbol {t}} ^ {(1)}, \boldsymbol {V} _ {\boldsymbol {t}} ^ {(1)}\right) \right.\tag{20}
$$

Equation (20) ensures that the probability of each element in ?? will not change after mapping ${ \pmb U } _ { t } ^ { ( 1 ) }$ and $\pmb { V } _ { t } ^ { ( 1 ) }$ using $f _ { u }$ and $f _ { v }$ . Here, we choose $f _ { u } \Big ( U _ { t } ^ { ( 1 ) } \Big ) = U _ { t } ^ { ( 1 ) }$ ?? and $f _ { v } \Big ( V _ { t } ^ { ( 1 ) } \Big ) = V _ { t } ^ { ( 1 ) } v ,$ , where ${ \pmb u } \ge { \pmb 0 }$ and ${ \pmb v } \ge { \bf 0 }$ . These two maps satisfy equation (20). For further details of why $f _ { u }$ and $f _ { v }$ are chosen like this, see Appendix B. Learning $f _ { u }$ and $f _ { v }$ is an optimization problem. The cost function is:

$$
J _ {r} (\boldsymbol {u}, \boldsymbol {v}) = \left\| \boldsymbol {W} _ {t} \odot \Big (\boldsymbol {X} _ {t} - \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {u} \boldsymbol {S} \Big (\boldsymbol {V} _ {t} ^ {(1)} \boldsymbol {v} \Big) ^ {T} \Big) \right\| _ {F}\tag{21}
$$

The tuning factors can be learned through optimizing

$$
\begin{array}{c} \min J _ {r} (\boldsymbol {u}, \boldsymbol {v}) \\ s. t. \boldsymbol {u} \geq 0, \boldsymbol {v} \geq 0 \end{array}
$$

Similarly, the cost function is non-increasing under the following update rules:

$$
u _ {a b} \leftarrow u _ {a b} \frac {\left(\left(U _ {t} ^ {(1)}\right) ^ {T} X _ {t} V _ {t} ^ {(1)} v S ^ {T}\right) _ {a b}}{\left(\left(U _ {t} ^ {(1)}\right) ^ {T} \left(W _ {t} \odot \left(U _ {t} ^ {(1)} u S \left(V _ {t} ^ {(1)} v\right) ^ {T}\right)\right) V _ {t} ^ {(1)} v S ^ {T}\right) _ {a b}}\tag{22}
$$

$$
v _ {c d} \leftarrow v _ {c d} \frac {\left(\left(V _ {t} ^ {(1)}\right) ^ {T} X _ {t} ^ {T} U _ {t} ^ {(1)} v S\right) _ {c d}}{\left(\left(V _ {t} ^ {(1)}\right) ^ {T} \Big (W _ {t} ^ {T} \odot \Big (V _ {t} ^ {(1)} v S ^ {T} u ^ {T} \Big (U _ {t} ^ {(1)} \Big) ^ {T} \Big)\right) U _ {t} ^ {(1)} v S\left. \right) _ {c d}}\tag{23}
$$

Finally, the optimization problem is solved by alternatively estimating ??, ?? . How ${ \pmb u } , { \pmb v }$ is learned is summarized in Algorithm 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: Group Representation Regulation
Input: $X_{t}$, the target rating matrix
    S, the consistent knowledge
    $U_{t}^{(1)}, V_{t}^{(1)}$, user and item membership matrix of target domain
    $(U_{t}^{(1)}, V_{t}^{(1)}$ are obtained from GFK algorithm)
Output: u, user tuning factor
    v, item tuning factor
1 INITIALIZE $u \in \mathbb{R}^{K \times K}$, $v \in \mathbb{R}^{L \times L}$, $J_{r}^{(min)} \leftarrow 0$, $J_{r} \leftarrow 0$
2 WHILE $J_{r} = 0$ OR $J_{r} - J_{r}^{(min)} &gt; \varepsilon$ DO
3 FOR each element $u_{ab}$ in u DO
4 UPDATE $u_{ab}$ as in equation (22)
5 ENDFOR
6 FOR each element $v_{cd}$ in v DO
7 UPDATE $v_{cd}$ as in equation (23)
8 ENDFOR
9 UPDATE $J_{r}^{(i)}$ as in equation (21)
10 IF $J_{r}^{(min)} &gt; J_{r}$
11 $J_{r}^{(min)} = J_{r}$
12 ENDIF
13 ENDWHILE
14 RETURN u, v
</div>

## 4.2.5 Step 5: Recommendation in target domain

The recommendation in target domain is given by equation (24).

$$
\left\{ \begin{array}{l} \widehat {\boldsymbol {X}} _ {t} = \Big (\boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {u} \Big) \boldsymbol {S} \Big (\boldsymbol {V} _ {t} ^ {(1)} \boldsymbol {v} \Big) ^ {T} \\ \boldsymbol {U} _ {t} ^ {(1)} = \boldsymbol {\Psi} _ {G} \Big (\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)} \Big) \times \boldsymbol {f} _ {z s} \Big (\boldsymbol {U} _ {t} ^ {(0)} \Big) \\ \boldsymbol {V} _ {t} ^ {(1)} = \boldsymbol {\Phi} _ {G} \Big (\boldsymbol {V} _ {s} ^ {(0)}, \boldsymbol {V} _ {t} ^ {(0)} \Big) \times \boldsymbol {f} _ {z s} \Big (\boldsymbol {V} _ {t} ^ {(0)} \Big) \end{array} \right.\tag{24}
$$

where $\widehat { \pmb X } _ { t }$ is the reconstructed user-item rating matrix for prediction, ??, ?? are user and item tuning factors for target domain, ?? is the consistent knowledge, ${ \pmb U } _ { s } ^ { ( 0 ) } , { \pmb U } _ { t } ^ { ( 0 ) }$ are user group membership matrixes, and $V _ { s } ^ { ( 0 ) } , V _ { t } ^ { ( 0 ) }$ are item group membership matrixes for the source domain and the target domain before domain adaptation. $\pmb { U } _ { t } ^ { ( 1 ) } , \pmb { V } _ { t } ^ { ( 1 ) }$ are user and item group membership matrixes for the target domain after domain adaptation. $\Psi _ { G } ( \cdot )$ and $\pmb { \phi } _ { G } ( \cdot )$ are GFK operators to map group membership matrixes to a domain-invariant feature space, and $\pmb { f } _ { z s } ( \cdot )$ is the Z-score function.

## 4.3 Architecture of a Cross-domain Recommender System

In the proposed CIT method, group-level knowledge from a source domain and a target domain can be combined and augmented compared with what can be acquired independently from only the target domain. In this section, we introduce how to use the proposed CIT method when developing a recommender system to support decision making for businesses and individual customers.

A conceptual framework for a cross-domain recommender system that applies the proposed method is shown in Fig. 4. When businesses launch a new product or service, a sufficient amount of data has not always been collected to populate the target domain. It is often easier to acquire data from another mature service – the source domain. Accordingly, a cross-domain recommendation engine can be built, based on our method, to provide better predictions of a user’s preferences for items. This assists decision making for both businesses and individual customers.

For businesses, the CDRS could be used to support product development and marketing decisions. For example, businesses could predict user preferences for more accurate cross-selling or identify potential user groups to market specific products to. They could also develop product bundles based on user preference prediction. For individual customers, our proposed CDRS could be used to facilitate targeted product searches. By ranking products according to predicted preference, customers may be able to locate the most desirable products more quickly and effectively.

![](/api/attachments/PJT4P2KQ/fulltext/images/c900578d7a057346195e3de11f69f8f71db1b1528bdb6f2b6fcf5099b10fb733.jpg)  
Fig. 4. Conceptual framework of a cross-domain recommender system

## 5. Experiments and Analysis

Our empirical experiments are presented in this section. First, the datasets and evaluation metrics are

## ACCEPTED MANUSCRIPT

introduced, followed by the experimental settings and the baseline methods. The results of the experiments are presented along with an analysis of the parameters.

## 5.1 Dataset and Evaluation Metrics

In testing the CIT method, it was important to choose data from different but similar domains. Previous research has considered movies, books, and music as appropriate categories for CDRS experiment tests. For a fair comparison, we have chosen the same categories and many of the same datasets for our experiments. Our tests comprise nine cross-domain recommendation tasks, including movie-to-movie and book-to-movie recommendations, common in prior research, as well as some new tasks extending to the music category that are less commonly tested. The baseline methods include three non-transfer methods and two cross-domain methods. Five real-world datasets were used: Movielens 20M<sup>1</sup>, Netflix<sup>2</sup>, LibraryThing<sup>3</sup>, Amazon Book<sup>4</sup> and YahooMusic<sup>5</sup>. Each is publicly available and has been used to test recommender systems in a variety of scenarios for recommender systems in single domain. But tests on these dataset in this novel cross-domain setting are lacking. The statistical information for these datasets is provided in Table II.

Table II Statistical information on the original datasets

<table><tr><td></td><td>Movielens 20M</td><td>Netflix</td><td>Library Thing</td><td>Amazon Book</td><td>Yahoo Music_1</td><td>Yahoo Music_2</td></tr><tr><td>#user</td><td>138493</td><td>480189</td><td>7279</td><td>8026324</td><td>200000</td><td>200000</td></tr><tr><td>#item</td><td>26744</td><td>17770</td><td>37232</td><td>2330066</td><td>136736</td><td>136736</td></tr><tr><td>#rating</td><td>20000263</td><td>100480507</td><td>749401</td><td>22507155</td><td>78344627</td><td>78742463</td></tr><tr><td>sparsity</td><td>0.54%</td><td>1.18%</td><td>0.28%</td><td>0.0001%</td><td>0.29%</td><td>0.29%</td></tr><tr><td>range</td><td>0.5-5</td><td>1-5</td><td>0.5-5</td><td>1-5</td><td>1-5</td><td>1-5</td></tr><tr><td>average</td><td>3.5255</td><td>3.6043</td><td>3.8709</td><td>4.2958</td><td>3.1613</td><td>3.1634</td></tr><tr><td>STD</td><td>1.0520</td><td>1.0852</td><td>0.9387</td><td>1.1115</td><td>1.5991</td><td>1.6046</td></tr></table>

In the Amazon Book dataset, we found that more than 6 million among 8 million users gave all their reviewed items the same rating. This phenomenon is very uncommon and rarely happens in real-world. As such, it was determined that these users could provide no effective contribution to the construction of a recommender system and were removed. For the Movielens20M and LibraryThing datasets, we normalized the ratings to a range of {1,2,3,4,5}. Movielens20M, LibraryThing, and YahooMusic\_1 were used as the source domain, while Netflix, AmazonBook, YahooMusic\_2 were used as the target domain. Across all the datasets, 2000 items that had been rated more than 10 times were randomly chosen. We then filtered out the users who had given less than a total of 20 ratings. The next section describes how the users were chosen.

For the source domain data, we randomly selected 4000 users to be regular customers of the site. The sparsity ratio of source domain data was controlled at 2%. Two source domain datasets with different statistical properties were chosen to test the performance of different algorithms. For the target domain data, we randomly selected 2000 users to be regular customers of the site, and another 2000 users to be new customers. In terms of regular customers, three sparsity ratios were used to compare different algorithms in different circumstances. For new users, five observed ratings were given, and the rest of the ratings were used for evaluation. In the end, the rating matrixes for both the source and target domains were all 4000 × 2000 matrixes. The details of the final datasets are summarized in Table III.

Mean absolute error (MAE) and root mean square error (RMSE) were used as the evaluation metrics:

$$
\begin{array}{c} M A E = \sum_ {(u, v, r _ {u, v}) \in Y} \frac {\left| \hat {r} _ {u , v} - r _ {u , v} \right|}{| Y |} \\ R M S E = \sqrt {\sum_ {(u , v , r _ {u , v}) \in Y} \frac {\left(\hat {r} _ {u , v} - r _ {u , v}\right) ^ {2}}{| Y |}} \end{array}
$$

where ?? is the test set, and |??| is the number of test ratings.

Table III Description of data subsets in three categories

<table><tr><td>Data_type</td><td>Data_name</td><td>Data_source</td><td>Domain</td><td>Sparsity</td><td>Average</td></tr><tr><td rowspan="5">Movie</td><td>movie_s1</td><td>Movielens20M</td><td>source</td><td>2.00%</td><td>3.66</td></tr><tr><td>movie_s2</td><td>Movielens20M</td><td>source</td><td>2.00%</td><td>2.63</td></tr><tr><td>movie_t1</td><td>Netflix</td><td>target</td><td>0.50%</td><td>2.68</td></tr><tr><td>movie_t2</td><td>Netflix</td><td>target</td><td>1.00%</td><td>2.67</td></tr><tr><td>movie_t3</td><td>Netflix</td><td>target</td><td>1.50%</td><td>2.67</td></tr><tr><td rowspan="5">Book</td><td>book_s1</td><td>LibraryThing</td><td>source</td><td>2.00%</td><td>4.02</td></tr><tr><td>book_s2</td><td>LibraryThing</td><td>source</td><td>2.00%</td><td>3.72</td></tr><tr><td>book_t1</td><td>Amazon</td><td>target</td><td>0.50%</td><td>3.52</td></tr><tr><td>book_t2</td><td>Amazon</td><td>target</td><td>0.75%</td><td>3.53</td></tr><tr><td>book_t3</td><td>Amazon</td><td>target</td><td>0.94%</td><td>3.53</td></tr><tr><td rowspan="5">Music</td><td>music_s1</td><td>YahooMusic_1</td><td>source</td><td>2.00%</td><td>4.13</td></tr><tr><td>music_s2</td><td>YahooMusic_1</td><td>source</td><td>2.00%</td><td>2.73</td></tr><tr><td>music_t1</td><td>YahooMusic_2</td><td>target</td><td>0.50%</td><td>2.26</td></tr><tr><td>music_t2</td><td>YahooMusic_2</td><td>target</td><td>1.00%</td><td>2.26</td></tr><tr><td>music_t3</td><td>YahooMusic_2</td><td>target</td><td>1.50%</td><td>2.25</td></tr></table>

## 5.2 Experimental Settings and Baselines

Three non-transfer learning methods and two cross-domain methods were chosen as comparisons for the

## ACCEPTED MANUSCRIPT

proposed method. The non-transfer learning methods were: Pearson’s correlation coefficient (PCC) [2], FMM [22] and SVD [3]. The cross-domain methods were: CBT [18] and RMGM [19]. PCC uses user-based CF, and the number of neighborhoods was set at 50. For SVD, the latent feature number was fixed at 40, the regularization factor was set to 0.015, and the learning rate was set to 0.003. For FMM, CBT, and RMGM, the user group number and item group number were both set to 40. For the proposed method, CIT, the user group number and the item group number were both set to 40, and the regularization factor was set to 0.5. Further analysis of the parameters is provided in Sub-section 5.4.

For each target domain, three configurations of sparsity were settled; thus, nine cross-domain recommendation tasks each under three sparsity ratios were conducted for comparison between the baselines and the proposed method. Since the algorithms (except for PCC) need to initialize the factorized matrix randomly, we ran 20 random initializations and report the averaged results and standard deviations.

## 5.3 Results

Comparison results are given in Table IV, V and VI. The proposed method, CIT, had the lowest MAE and RMSE among all the six methods in most of the cross-domain recommendation tasks. Compared with the non-transfer learning methods, we find that our method is more effective at extracting knowledge from the source domain to apply in the target domain. This is especially significant when the statistical properties of the source rating matrix are different from those in the target rating matrix. This indicates that our method gains its benefits by keeping the user and item group information in both domains consistent. The CIT method is able to extract knowledge even when the statistical properties of the source rating matrix diverge from the target rating matrix, while CBT and RMGM may need some restricted conditions of source data.

Comparing the six methods and given the results of all nine tasks with different sparsity ratios, we can make the following observations:

(1) For non-transfer learning methods, the FMM method shows superior performance compared to the memory-based method PCC and the famous matrix factorization method SVD from the Netflix competition. PCC and SVD are not very good at handling the cold-start problem. When the number

## ACCEPTED MANUSCRIPT

of available ratings for users in target domain is limited, they fail to give good recommendations. (2) CBT is not stable and positive transfer is not guaranteed. When the statistical properties of the source rating matrix is similar to that of the target rating matrix (say movie\_s2 to movie\_t1/2/3), CBT is better than the non-transfer baselines. Since CBT fills the source rating matrix with the users

Table IV Prediction performance on a movie target domain

<table><tr><td rowspan="3">method</td><td rowspan="3">source data</td><td colspan="3">MAE</td><td colspan="3">RMSE</td></tr><tr><td colspan="3">Sparsity</td><td colspan="3">Sparsity</td></tr><tr><td>0.50%</td><td>1.00%</td><td>1.50%</td><td>0.50%</td><td>1.00%</td><td>1.50%</td></tr><tr><td>PCC</td><td>-</td><td>1.2609</td><td>1.2710</td><td>1.1981</td><td>1.5671</td><td>1.5789</td><td>1.4839</td></tr><tr><td>FMM</td><td>-</td><td>1.0164±0.0027</td><td>1.0069±0.0033</td><td>1.0029±0.0028</td><td>1.2283±0.0036</td><td>1.2143±0.0045</td><td>1.2064±0.0037</td></tr><tr><td>SVD</td><td>-</td><td>1.0230±0.0013</td><td>1.0227±0.0012</td><td>1.0391±0.0077</td><td>1.2372±0.0015</td><td>1.2382±0.0012</td><td>1.2544±0.0096</td></tr><tr><td rowspan="6">CBT</td><td>movie_s1</td><td>1.2868±0.0034</td><td>1.2845±0.0072</td><td>1.2836±0.0038</td><td>1.5318±0.0043</td><td>1.5290±0.0092</td><td>1.5277±0.0048</td></tr><tr><td>movie_s2</td><td>1.0205±0.0007</td><td>1.0194±0.0016</td><td>1.0192±0.0010</td><td>1.1964*±0.0003</td><td>1.1962±0.0008</td><td>1.1958±0.0004</td></tr><tr><td>book_s1</td><td>1.4493±0.0075</td><td>1.4477±0.0071</td><td>1.4441±0.0066</td><td>1.7627±0.0114</td><td>1.7604±0.0107</td><td>1.7551±0.0100</td></tr><tr><td>book_s2</td><td>1.3272±0.0118</td><td>1.3248±0.0071</td><td>1.3253±0.0104</td><td>1.5871±0.0159</td><td>1.5839±0.0093</td><td>1.5849±0.0134</td></tr><tr><td>music_s1</td><td>1.4917±0.0189</td><td>1.4935±0.0164</td><td>1.4923±0.0146</td><td>1.8115±0.0187</td><td>1.8131±0.0155</td><td>1.8112±0.0141</td></tr><tr><td>music_s2</td><td>1.0144±0.0023</td><td>1.0134±0.0019</td><td>1.0141±0.0020</td><td>1.2027±0.0027</td><td>1.2032±0.0020</td><td>1.2018±0.0030</td></tr><tr><td rowspan="6">RMGM</td><td>movie_s1</td><td>1.0347±0.0065</td><td>1.0252±0.0050</td><td>1.0214±0.0034</td><td>1.2515±0.0079</td><td>1.2402±0.0067</td><td>1.2345±0.0047</td></tr><tr><td>movie_s2</td><td>1.0038±0.0022</td><td>0.9994±0.0025</td><td>0.9977±0.0028</td><td>1.2104±0.0031</td><td>1.2025±0.0033</td><td>1.1992±0.0038</td></tr><tr><td>book_s1</td><td>1.0464±0.0048</td><td>1.0369±0.0046</td><td>1.0309±0.0052</td><td>1.2711±0.0060</td><td>1.2583±0.0064</td><td>1.2501±0.0069</td></tr><tr><td>book_s2</td><td>1.0396±0.0033</td><td>1.0326±0.0038</td><td>1.0261±0.0043</td><td>1.2616±0.0043</td><td>1.2523±0.0048</td><td>1.2433±0.0057</td></tr><tr><td>music_s1</td><td>1.0498±0.0055</td><td>1.0387±0.0056</td><td>1.0299±0.0058</td><td>1.2734±0.0078</td><td>1.2595±0.0079</td><td>1.2463±0.0076</td></tr><tr><td>music_s2</td><td>1.0591±0.0061</td><td>1.0512±0.0039</td><td>1.0489±0.0046</td><td>1.2813±0.0076</td><td>1.2711±0.0052</td><td>1.2655±0.0058</td></tr><tr><td rowspan="6">CIT</td><td>movie_s1</td><td>1.0002*±0.0025</td><td>0.9906*±0.0027</td><td>0.9888*±0.0025</td><td>1.1846*±0.0027</td><td>1.1881*±0.0034</td><td>1.1846*±0.0027</td></tr><tr><td>movie_s2</td><td>0.9995*±0.0028</td><td>0.9911*±0.0023</td><td>0.9873*±0.0022</td><td>1.1987±0.0040</td><td>1.1887*±0.0029</td><td>1.1828*±0.0034</td></tr><tr><td>book_s1</td><td>0.9992*±0.0022</td><td>0.9908*±0.0019</td><td>0.9886*±0.0023</td><td>1.1978*±0.0034</td><td>1.1882*±0.0026</td><td>1.1843*±0.0028</td></tr><tr><td>book_s2</td><td>0.9993*±0.0032</td><td>0.9907*±0.0022</td><td>0.9889*±0.0022</td><td>1.1985*±0.0041</td><td>1.1886*±0.0026</td><td>1.1853*±0.0032</td></tr><tr><td>music_s1</td><td>0.9996*±0.0033</td><td>0.9914*±0.0022</td><td>0.9883*±0.0018</td><td>1.1985*±0.0045</td><td>1.1885*±0.0029</td><td>1.1839*±0.0025</td></tr><tr><td>music_s2</td><td>1.0004*±0.0025</td><td>0.9931*±0.0021</td><td>0.9892*±0.0023</td><td>1.1997*±0.0031</td><td>1.1886*±0.0028</td><td>1.1848*±0.0033</td></tr></table>

Table V Prediction performance on a book target domain

<table><tr><td rowspan="3">method</td><td rowspan="3">source data</td><td colspan="3">MAE</td><td colspan="3">RMSE</td></tr><tr><td colspan="3">Sparsity</td><td colspan="3">Sparsity</td></tr><tr><td>0.50%</td><td>0.75%</td><td>0.94%</td><td>0.50%</td><td>0.75%</td><td>0.94%</td></tr><tr><td>PCC</td><td>-</td><td>1.2625</td><td>1.2654</td><td>1.2340</td><td>1.5737</td><td>1.5739</td><td>1.5305</td></tr><tr><td>FMM</td><td>-</td><td>1.0645±0.0028</td><td>1.0256±0.0022</td><td>1.0211*±0.0029</td><td>1.3152±0.0035</td><td>1.2645±0.0033</td><td>1.2582±0.0045</td></tr><tr><td>SVD</td><td>-</td><td>1.0591±0.0025</td><td>1.0288±0.0021</td><td>1.1702±0.0034</td><td>1.3220±0.0028</td><td>1.2826±0.0026</td><td>1.5032±0.0047</td></tr><tr><td rowspan="6">CBT</td><td>movie_s1</td><td>1.0859±0.0009</td><td>1.0856±0.0005</td><td>1.0851±0.0006</td><td>1.3233±0.0037</td><td>1.3219±0.0023</td><td>1.3220±0.0024</td></tr><tr><td>movie_s2</td><td>1.2345±0.0118</td><td>1.2334±0.0072</td><td>1.2287±0.0078</td><td>1.4271±0.0105</td><td>1.4260±0.0064</td><td>1.4215±0.0070</td></tr><tr><td>book_s1</td><td>1.0896±0.0012</td><td>1.0893±0.0009</td><td>1.0895±0.0012</td><td>1.4330±0.0030</td><td>1.4310±0.0038</td><td>1.4312±0.0038</td></tr><tr><td>book_s2</td><td>1.0813±0.0010</td><td>1.0814±0.0009</td><td>1.0809±0.0008</td><td>1.3569±0.0059</td><td>1.3547±0.0046</td><td>1.3525±0.0041</td></tr><tr><td>music_s1</td><td>1.1128±0.0082</td><td>1.1127±0.0098</td><td>1.1105±0.0080</td><td>1.4616±0.0096</td><td>1.4618±0.0091</td><td>1.4598±0.0073</td></tr><tr><td>music_s2</td><td>1.1881±0.0129</td><td>1.1906±0.0147</td><td>1.1935±0.0119</td><td>1.3895±0.0099</td><td>1.3910±0.0116</td><td>1.3930±0.0095</td></tr><tr><td rowspan="4">RMGM</td><td>movie_s1</td><td>1.0673±0.0046</td><td>1.0460±0.0051</td><td>1.0425±0.0047</td><td>1.3057±0.0066</td><td>1.2786±0.0065</td><td>1.2750±0.0070</td></tr><tr><td>movie_s2</td><td>1.0594±0.0037</td><td>1.0329±0.0036</td><td>1.0277±0.0037</td><td>1.2933±0.0039</td><td>1.2614±0.0043</td><td>1.2558±0.0036</td></tr><tr><td>book_s1</td><td>1.0726±0.0041</td><td>1.0440±0.0039</td><td>1.0409±0.0046</td><td>1.3339±0.0052</td><td>1.2962±0.0050</td><td>1.2914±0.0057</td></tr><tr><td>book_s2</td><td>1.0649±0.0037</td><td>1.0424±0.0037</td><td>1.0376±0.0029</td><td>1.3172±0.0049</td><td>1.2883±0.0050</td><td>1.2807±0.0036</td></tr></table>

ACCEPTED MANUSCRIPT

<table><tr><td rowspan="2"></td><td>music_s1</td><td> $1.0817 \pm 0.0055$ </td><td> $1.0588 \pm 0.0063$ </td><td> $1.0539 \pm 0.0053$ </td><td> $1.3432 \pm 0.0074$ </td><td> $1.3143 \pm 0.0103$ </td><td> $1.3082 \pm 0.0081$ </td></tr><tr><td>music_s2</td><td> $1.1028 \pm 0.0076$ </td><td> $1.0832 \pm 0.0072$ </td><td> $1.0713 \pm 0.0068$ </td><td> $1.3430 \pm 0.0094$ </td><td> $1.3196 \pm 0.0086$ </td><td> $1.3092 \pm 0.0084$ </td></tr><tr><td rowspan="6">CIT</td><td>movie_s1</td><td> $\mathbf{1.0464}^{*} \pm 0.0045$ </td><td> $\mathbf{1.0246} \pm 0.0031$ </td><td> $1.0243 \pm 0.0028$ </td><td> $\mathbf{1.2685}^{*} \pm 0.0041$ </td><td> $\mathbf{1.2464}^{*} \pm 0.0041$ </td><td> $\mathbf{1.2458}^{*} \pm 0.0046$ </td></tr><tr><td>movie_s2</td><td> $\mathbf{1.0456}^{*} \pm 0.0036$ </td><td> $\mathbf{1.0249} \pm 0.0032$ </td><td> $1.0245 \pm 0.0024$ </td><td> $\mathbf{1.2688}^{*} \pm 0.0040$ </td><td> $\mathbf{1.2474}^{*} \pm 0.0035$ </td><td> $\mathbf{1.2458}^{*} \pm 0.0022$ </td></tr><tr><td>book_s1</td><td> $\mathbf{1.0465}^{*} \pm 0.0031$ </td><td> $1.0257 \pm 0.0028$ </td><td> $1.0247 \pm 0.0030$ </td><td> $\mathbf{1.2705}^{*} \pm 0.0041$ </td><td> $\mathbf{1.2468}^{*} \pm 0.0040$ </td><td> $\mathbf{1.2458}^{*} \pm 0.0039$ </td></tr><tr><td>book_s2</td><td> $\mathbf{1.0474}^{*} \pm 0.0045$ </td><td> $\mathbf{1.0254} \pm 0.0026$ </td><td> $1.0236 \pm 0.0031$ </td><td> $\mathbf{1.2707}^{*} \pm 0.0050$ </td><td> $\mathbf{1.2476}^{*} \pm 0.0034$ </td><td> $\mathbf{1.2448}^{*} \pm 0.0043$ </td></tr><tr><td>music_s1</td><td> $\mathbf{1.0467}^{*} \pm 0.0040$ </td><td> $\mathbf{1.0249}^{*} \pm 0.0024$ </td><td> $1.0238 \pm 0.0030$ </td><td> $\mathbf{1.2711}^{*} \pm 0.0047$ </td><td> $\mathbf{1.2465}^{*} \pm 0.0039$ </td><td> $\mathbf{1.2442}^{*} \pm 0.0033$ </td></tr><tr><td>music_s2</td><td> $\mathbf{1.0457}^{*} \pm 0.0030$ </td><td> $1.0265 \pm 0.0030$ </td><td> $1.0238 \pm 0.0032$ </td><td> $\mathbf{1.2690}^{*} \pm 0.0030$ </td><td> $\mathbf{1.2482}^{*} \pm 0.0036$ </td><td> $\mathbf{1.2456}^{*} \pm 0.0028$ </td></tr></table>

Table VI Prediction performance on a music target domain

<table><tr><td rowspan="3">method</td><td rowspan="3">source data</td><td colspan="3">MAE</td><td colspan="3">RMSE</td></tr><tr><td colspan="3">Sparsity</td><td colspan="3">Sparsity</td></tr><tr><td>0.50%</td><td>1.00%</td><td>1.50%</td><td>0.50%</td><td>1.00%</td><td>1.500025</td></tr><tr><td>PCC</td><td>-</td><td>1.4403</td><td>1.3617</td><td>1.3262</td><td>1.8421</td><td>1.7080</td><td>1.6489</td></tr><tr><td>FMM</td><td>-</td><td> $1.2619 \pm 0.0023$ </td><td> $1.2460 \pm 0.0027$ </td><td> $1.2448 \pm 0.0028$ </td><td> $1.5009 \pm 0.0035$ </td><td> $1.4754 \pm 0.0057$ </td><td> $1.4685 \pm 0.0045$ </td></tr><tr><td>SVD</td><td>-</td><td> $1.2675 \pm 0.0009$ </td><td> $1.2603 \pm 0.0009$ </td><td> $1.2566 \pm 0.0014$ </td><td> $1.4972 \pm 0.0011$ </td><td> $1.4916 \pm 0.0015$ </td><td> $1.4876 \pm 0.0015$ </td></tr><tr><td rowspan="6">CBT</td><td>movie_s1</td><td> $1.3776 \pm 0.0030$ </td><td> $1.3759 \pm 0.0044$ </td><td> $1.3764 \pm 0.0029$ </td><td> $1.6168 \pm 0.0046$ </td><td> $1.6136 \pm 0.0069$ </td><td> $1.6149 \pm 0.0048$ </td></tr><tr><td>movie_s2</td><td> $1.2726 \pm 0.0021$ </td><td> $1.2734 \pm 0.0025$ </td><td> $1.2728 \pm 0.0024$ </td><td> $1.4663 \pm 0.0017$ </td><td> $1.4644 \pm 0.0021$ </td><td> $1.4634 \pm 0.0021$ </td></tr><tr><td>book_s1</td><td> $1.4666 \pm 0.0038$ </td><td> $1.4665 \pm 0.0038$ </td><td> $1.4656 \pm 0.0064$ </td><td> $1.7929 \pm 0.0076$ </td><td> $1.7926 \pm 0.0076$ </td><td> $1.7908 \pm 0.0127$ </td></tr><tr><td>book_s2</td><td> $1.3986 \pm 0.0045$ </td><td> $1.3973 \pm 0.0050$ </td><td> $1.4005 \pm 0.0035$ </td><td> $1.6598 \pm 0.0071$ </td><td> $1.6581 \pm 0.0085$ </td><td> $1.6634 \pm 0.0068$ </td></tr><tr><td>music_s1</td><td> $1.4971 \pm 0.0131$ </td><td> $1.4934 \pm 0.0102$ </td><td> $1.5012 \pm 0.0049$ </td><td> $1.8343 \pm 0.0139$ </td><td> $1.8310 \pm 0.0102$ </td><td> $1.8387 \pm 0.0050$ </td></tr><tr><td>music_s2</td><td> $1.2597 \pm 0.0059$ </td><td> $1.2598 \pm 0.0054$ </td><td> $1.2568 \pm 0.0051$ </td><td> $1.4604 \pm 0.0036$ </td><td> $1.4604 \pm 0.0035$ </td><td> $1.4603 \pm 0.0041$ </td></tr><tr><td rowspan="6">RMGM</td><td>movie_s1</td><td> $1.2699 \pm 0.0038$ </td><td> $1.2576 \pm 0.0048$ </td><td> $1.2539 \pm 0.0036$ </td><td> $1.5099 \pm 0.0062$ </td><td> $1.4952 \pm 0.0075$ </td><td> $1.4897 \pm 0.0056$ </td></tr><tr><td>movie_s2</td><td> $1.2482 \pm 0.0023$ </td><td> $1.2401 \pm 0.0027$ </td><td> $1.2406 \pm 0.0029$ </td><td> $1.4819 \pm 0.0051$ </td><td> $1.4698 \pm 0.0048$ </td><td> $1.4707 \pm 0.0051$ </td></tr><tr><td>book_s1</td><td> $1.2832 \pm 0.0049$ </td><td> $1.2690 \pm 0.0030$ </td><td> $1.2623 \pm 0.0054$ </td><td> $1.5374 \pm 0.0069$ </td><td> $1.5180 \pm 0.0058$ </td><td> $1.5094 \pm 0.0088$ </td></tr><tr><td>book_s2</td><td> $1.2757 \pm 0.0037$ </td><td> $1.2620 \pm 0.0047$ </td><td> $1.2575 \pm 0.0042$ </td><td> $1.5285 \pm 0.0065$ </td><td> $1.5096 \pm 0.0076$ </td><td> $1.5026 \pm 0.0070$ </td></tr><tr><td>music_s1</td><td> $1.2901 \pm 0.0051$ </td><td> $1.2767 \pm 0.0063$ </td><td> $1.2683 \pm 0.0083$ </td><td> $1.5497 \pm 0.0097$ </td><td> $1.5317 \pm 0.0095$ </td><td> $1.5199 \pm 0.0117$ </td></tr><tr><td>music_s2</td><td> $1.2881 \pm 0.0037$ </td><td> $1.2842 \pm 0.0035$ </td><td> $1.2799 \pm 0.0057$ </td><td> $1.5385 \pm 0.0066$ </td><td> $1.5328 \pm 0.0079$ </td><td> $1.5264 \pm 0.0069$ </td></tr><tr><td rowspan="6">CIT</td><td>movie_s1</td><td> $1.2450^{*} \pm 0.0021$ </td><td> $1.2375^{*} \pm 0.0019$ </td><td> $1.2344^{*} \pm 0.0015$ </td><td> $1.4516^{*} \pm 0.0030$ </td><td> $1.4451^{*} \pm 0.0029$ </td><td> $1.4400^{*} \pm 0.0026$ </td></tr><tr><td>movie_s2</td><td> $1.2452^{*} \pm 0.0019$ </td><td> $1.2375^{*} \pm 0.0018$ </td><td> $1.2345^{*} \pm 0.0020$ </td><td> $1.4513^{*} \pm 0.0026$ </td><td> $1.4439^{*} \pm 0.0030$ </td><td> $1.4409^{*} \pm 0.0038$ </td></tr><tr><td>book_s1</td><td> $1.2449^{*} \pm 0.0019$ </td><td> $1.2385^{*} \pm 0.0017$ </td><td> $1.2350^{*} \pm 0.0021$ </td><td> $1.4511^{*} \pm 0.0020$ </td><td> $1.4448^{*} \pm 0.0022$ </td><td> $1.4411^{*} \pm 0.0040$ </td></tr><tr><td>book_s2</td><td> $1.2455^{*} \pm 0.0015$ </td><td> $1.2377^{*} \pm 0.0016$ </td><td> $1.2344^{*} \pm 0.0017$ </td><td> $1.4523^{*} \pm 0.0026$ </td><td> $1.4444^{*} \pm 0.0029$ </td><td> $1.4403^{*} \pm 0.0023$ </td></tr><tr><td>music_s1</td><td> $1.2449^{*} \pm 0.0021$ </td><td> $1.2379^{*} \pm 0.0021$ </td><td> $1.2349^{*} \pm 0.0026$ </td><td> $1.4511^{*} \pm 0.0027$ </td><td> $1.4445^{*} \pm 0.0027$ </td><td> $1.4404^{*} \pm 0.0039$ </td></tr><tr><td>music_s2</td><td> $1.2453^{*} \pm 0.0023$ </td><td> $1.2375^{*} \pm 0.0018$ </td><td> $1.2344^{*} \pm 0.0021$ </td><td> $1.4513^{*} \pm 0.0025$ </td><td> $1.4438^{*} \pm 0.0021$ </td><td> $1.4402^{*} \pm 0.0031$ </td></tr></table>

average ratings, the average is crucial to this method and gains more advantages on two datasets when their average ratings are close. However, many results, like movie\_s1 to movie\_t1/2/3, suggest that CBT grapples with negative transfer issues. Referring to the statistical properties in Table III, the performance of CBT is directly related to the average of ratings. When the average rating of the source rating matrix deviates from that of the target domain, the performance of CBT is greatly impaired.

(3) RMGM shows similar performance to CBT but is more stable. The rating matrixes from the source and target domains are diagonally joined in RMGM. It is necessary for the two matrixes to have similar statistical properties to extract common knowledge, but RMGM fails to note whether or not the two matrixes are similar. RMGM’s results suggest that discrepancies in the average will disturb

## ACCEPTED MANUSCRIPT

the extraction of common knowledge, thus weakening transfer learning. We can see that positive transfer cannot be assured without a similarity guarantee of the rating matrixes for the source and target domains.

(4) The proposed CIT performs better than all the other baseline methods in almost all tasks, whether or not the datasets are in the same category. CIT ensures a steady improvement compared to non-transfer learning methods. Unlike the other two cross-domain methods, CIT is also suitable for datasets with different statistical properties. The adaptation knowledge transfer in CIT ensures that the knowledge extracted from the source rating matrix is suitable for assisting recommendation in the target domain.

(5) Negative transfer was always observed for CBT and RMGM when the average rating in the source domain was different from that of the target domain. This leads to a fundamental question in transfer learning: ‘When to transfer?’ This is an area seldom studied in CDRS. Instead of determining when to transfer, our proposed method reduces the difference between the source and target domains by preserving consistent user and item group information. In the scope of this paper, we did not see any negative transfer learning in our proposed method.

To confirm that the improvement of our CIT method over other methods was significant, we conducted a significance analysis on all pairs of experiments for each of the nine tasks in all three sparsity ratios using Friedman’s test. Most of the resulting P-values were much smaller than the significance level α (α = 0.05). Statistically significant results are marked with an asterisk (\*) in Tables IV, V and VI. Only one result was not a statistically significant improvement – the book target domain with a sparsity of 1.50% compared to the FMM non-transfer method in terms of MAE. However, CIT’s performance improvement in the same scenario was significant at a data sparsity of 0.50%, suggesting that cross-domain transfer may not be required as data richness in target domain increases.

To better understand the effectiveness of transfer learning on each individual task, we calculated the average MAEs and RMSEs for each cross-domain recommendation task. The results are presented in Tables

VII and VIII. The results for the nine tasks show that the proposed CIT method achieves the best performance in terms of both MAE and RMSE of the six methods.

Fig. 5 compares the results for all the methods. Since the rating average is different between the source and target domains, the overall performance of cross-domain methods CBT and RMGM was not as good as the non-transfer learning method FMM. RMGM is relatively stable and is mostly better than SVD, while CBT fluctuates and is worse than most of the other methods. We can see that the overall performance in the music category is worse than that in the movie and book categories, indicating that the rating matrix in the music category has different characteristics; however, our proposed method was still able to extract useful knowledge to help increase the prediction accuracy.

Table VII Prediction result of average MAE

<table><tr><td rowspan="2">Task</td><td colspan="3">non-transfer</td><td colspan="3">cross-domain</td></tr><tr><td>PCC</td><td>FMM</td><td>SVD</td><td>CBT</td><td>RMGM</td><td>CIT</td></tr><tr><td>m2m</td><td></td><td></td><td></td><td>1.1523</td><td>1.0137</td><td>0.9929</td></tr><tr><td>b2m</td><td>1.2433</td><td>1.0087</td><td>1.0283</td><td>1.3864</td><td>1.0354</td><td>0.9929</td></tr><tr><td>mu2m</td><td></td><td></td><td></td><td>1.2532</td><td>1.0463</td><td>0.9937</td></tr><tr><td>m2b</td><td></td><td></td><td></td><td>1.1589</td><td>1.0460</td><td>1.0317</td></tr><tr><td>b2b</td><td>1.2540</td><td>1.0371</td><td>1.0860</td><td>1.0853</td><td>1.0504</td><td>1.0322</td></tr><tr><td>mu2b</td><td></td><td></td><td></td><td>1.1514</td><td>1.0753</td><td>1.0319</td></tr><tr><td>m2mu</td><td></td><td></td><td></td><td>1.3248</td><td>1.2517</td><td>1.2390</td></tr><tr><td>b2mu</td><td>1.3761</td><td>1.2509</td><td>1.2615</td><td>1.4325</td><td>1.2683</td><td>1.2393</td></tr><tr><td>mu2mu</td><td></td><td></td><td></td><td>1.3784</td><td>1.2812</td><td>1.2392</td></tr></table>

Table VIII Prediction result of average RMSE

<table><tr><td rowspan="2">Task</td><td colspan="3">non-transfer</td><td colspan="3">cross-domain</td></tr><tr><td>PCC</td><td>FMM</td><td>SVD</td><td>CBT</td><td>RMGM</td><td>CIT</td></tr><tr><td>m2m</td><td></td><td></td><td></td><td>1.3628</td><td>1.2231</td><td>1.1879</td></tr><tr><td>b2m</td><td>1.5433</td><td>1.2163</td><td>1.2433</td><td>1.6724</td><td>1.2561</td><td>1.1905</td></tr><tr><td>mu2m</td><td></td><td></td><td></td><td>1.5073</td><td>1.2662</td><td>1.1907</td></tr><tr><td>m2b</td><td></td><td></td><td></td><td>1.3736</td><td>1.2783</td><td>1.2538</td></tr><tr><td>b2b</td><td>1.5594</td><td>1.2793</td><td>1.3693</td><td>1.3932</td><td>1.3013</td><td>1.2544</td></tr><tr><td>mu2b</td><td></td><td></td><td></td><td>1.4261</td><td>1.3229</td><td>1.2541</td></tr><tr><td>m2mu</td><td></td><td></td><td></td><td>1.5399</td><td>1.4862</td><td>1.4455</td></tr><tr><td>b2mu</td><td>1.7330</td><td>1.4816</td><td>1.4921</td><td>1.7263</td><td>1.5176</td><td>1.4457</td></tr><tr><td>mu2mu</td><td></td><td></td><td></td><td>1.6475</td><td>1.5332</td><td>1.4452</td></tr></table>

## 5.4 Parameter Analysis

In this section, we test how the parameters affect the performance of CIT. There are three parameters in the proposed CIT: ??, ?? and λ. ?? is the number of user groups and ?? is the number of item groups. ?? is the regularization factor for consistent knowledge extraction. For simplicity, only the result for the movie to movie task has been included. Datasets with three sparsity ratios were used to test all three parameters. Both MAE and RMSE were used as evaluation metrics. As the results for MAE were similar to RMSE, only the results for RMSE have been included.

To analyze the parameter ??, ?? and ?? were fixed at 40. In Fig. 6, we can see that RMSEs were not influenced significantly when ?? was varied from 0.1 to 1.0. As for ?? and ??, the number of user groups and the number of item groups did affect the RMSE, with a similar influence as described in previous papers: the higher the

![](/api/attachments/PJT4P2KQ/fulltext/images/0b70d46787b536fd7d8e452ee1bb63c3afbf04ca7e55a65c99da22b596da0b9e.jpg)

![](/api/attachments/PJT4P2KQ/fulltext/images/2a6b23aa1f5b3778d5fabf6fc009debca63436e232e00f49a4800e1f1f5f5217.jpg)

![](/api/attachments/PJT4P2KQ/fulltext/images/7815dc425cab8a161dcca0a305f02278855e0c16ff7b42a7dabc5026877ed412.jpg)  
(c) MAE of music target domain

![](/api/attachments/PJT4P2KQ/fulltext/images/f6c4c356cf5a0bbb63de5422513c230c476e5c26d9758b37e438ca00db397724.jpg)  
(d) RMSE of movie target domain

![](/api/attachments/PJT4P2KQ/fulltext/images/0afe6651c6edfc4169c46e719d4ec93e917785283d0b7a8715eda9164147575a.jpg)  
(e) RMSE of book target domair

![](/api/attachments/PJT4P2KQ/fulltext/images/626904c956a6e71cdb9c8d062c1bc5b1db569ae9669e48d4dfbb8f07de319fbe.jpg)  
(f) RMSE of music target domain  
Fig. 5. Prediction result for all methods

number, the higher the accuracy. In the range of 10 to 100, the influence of ?? and ?? is not significant. However, it took more time to run the algorithm when higher ?? and ?? values were chosen. This phenomenon was especially remarkable when ?? and ?? were larger than 100. To trade-off between an acceptable running speed for the algorithm and relative accuracy on RMSE, ?? = 40 and ?? = 40 were chosen for all experiments.

## 6. Discussion and Conclusion

Making decisions from an overwhelming volume of information is a crucial problem for both businesses and individual customers. And when a business begins operating in a new area, most existing recommender systems are not able to provide much guidance. The cross-domain recommendation method presented in this paper is intended to help businesses and individual customers with decision-making in unchartered waters.

![](/api/attachments/PJT4P2KQ/fulltext/images/82ace1779676904c1cca7c6ddbda5433bddf60974ff6e7587c82db78822f52c1.jpg)

(a) RMSE of parameter λ  
![](/api/attachments/PJT4P2KQ/fulltext/images/4baaf982970df0eadee1c3d43e2781374eeac51dceda99972a5162f85e2c49b2.jpg)

(b) RMSE of parameter K  
![](/api/attachments/PJT4P2KQ/fulltext/images/f548d00628f04a9ffdf9313ad38e67781a8f65076370dd12b683f1717b021524.jpg)  
(c) RMSE of parameter L  
Fig. 6. Results of RMSE with different parameter settings

## 6.1 Guidelines for Recommender System Developers

Recommender system developers will find the following guidelines useful:

Guideline #1: The CIT method should be used when two domains have different sparsity ratios. One domain should have a relatively sufficient amount of data; the other should be relatively sparse. There is no need to ensure user/item correspondence between the two domains.

Guideline #2: The CIT has been specially developed for two domains with divergent statistical properties (average and variance) and is appropriate for any divergence condition.

Guideline #3: If the users in target domain have no ratings at all, the CIT method is not suitable. If the sparsity ratio is more than 2.5%, developers should carefully consider whether or not to use the CIT method. Guideline #4: The range of ratings should be normalized before using the CIT method.

## 6.2 Practical Applications

The proposed cross-domain recommendation method can be used to solve cold-start problems – a

## ACCEPTED MANUSCRIPT

significant issue in the development and application of recommender systems. Developers can use this method to effectively transfer knowledge from a source domain with sufficient data to enhance recommendation models in a target domain. Our proposed method can be used when developing a recommender system to help businesses determine marketing strategies and to attract customers. The method can also provide end users with more effective decision-making support at the initial stage of a recommender system when very little data is available in the target domain. The improved recommendations the system provides will in turn help attract users, making the system grow more feasible and useful over time. Some examples of practical applications are provided below.

Our proposed method is used in the telecom product/service recommender system [24]. Telecommunications companies often introduce new product/service categories, such as new kinds of mobile plans. To attract customers to their new revenue lines, it is important to generate accurate recommendations, and that requires new and specific recommendation models. However, creating an effective recommendation model with very little user and sales data can be challenging when a new product category is first introduced. Through the proposed method, sales data from a similar product category can be used as the source domain to enhance the recommendation model.

Our proposed method is also used in Smart BizSeeker, a B2B recommender system [25]. Smart BizSeeker aims to recommend appropriate business partners to businesses in Australia. It also suffers from the coldstart problem, as initially there is very little rating data between businesses. However, similar B2B websites, such as Alibaba<sup>6</sup>, contain a great deal of business rating data, which provides an opportunity to enhance Smart BizSeeker’s recommendation model. The proposed cross-domain recommendation method effectively transfers knowledge from the rating data of other B2B websites to Smart BizSeeker to alleviate the cold-start problem.

Our method can also solve cold-start problems in G2B and G2C recommender systems [26] with a relevant source domain that contains sufficient rating data.

## ACCEPTED MANUSCRIPT

## 6.3 Conclusion and Further Study

Developing CDRS is an efficient way to deal with the cold-start problem in recommender systems. However, using cross-domain recommendation without considering domain shift is little better than gambling [27]. If the knowledge extracted from the source domain just happens to fit the target domain, the quality of recommendations may not suffer. However, if the knowledge does not, the likely result is inaccurate, poor quality recommendations. In this paper, we proposed the CIT method to transfer consistent knowledge learned from a source domain to assist recommendations in a target domain with insufficient rating data. Unlike previous research on knowledge transfer recommender systems, our work investigates what knowledge to transfer and how to effectively transfer that knowledge from the source domain to the target domain. We put forward a tri-factorization method for a cross-domain knowledge transfer recommender system to acquire consistent knowledge. One advantage of the CIT method is that user and item groups are aligned using domain adaptation techniques to ensure consistent user/item group information in both domains. Another advantage is that the method does not require corresponding users and items across domains. Experiments were conducted on five real-world datasets spanning three categories of data and nine results show that the proposed CIT method achieves better performance than five other methods in both single and cross-domain settings. The CIT performs particularly well, comparatively, when there is wide deviation in the rating averages between domains.

Cold-start problems are frequent in real-world applications, giving CDRSs great practical significance. However, there are many research gaps to be filled including: the types of situations that benefit from transfer learning; the sparsity levels of the data required for the target and source domains; and how to choose the most optimal source domain to assist transfer learning. If these questions are solved, CDRS can be better applied to markets and industry. Our future work will focus on developing a combined framework that containing more scenarios. To date, our work has only taken explicit rating data into consideration; more information, such as user feedback, item attributes, and implicit data needs to be considered. In addition, new customers in our experimental scenarios each have five ratings, and future work will explore ‘pure’ cold-start

problems where new users have no ratings at all.

## Appendix A. GFK operators $\psi _ { G }$ and $\Phi _ { G }$

$U _ { s } ^ { ( 1 ) } , V _ { s } ^ { ( 1 ) } , U _ { t } ^ { ( 1 ) } , V _ { t } ^ { ( 1 ) }$ are obtained through maps $\boldsymbol { \psi } _ { s } , \boldsymbol { \psi } _ { t } , \boldsymbol { \Phi } _ { s }$ and $\Phi _ { t } .$ . According to equations (12)-(15), the cores of these maps are GFK operators $\psi _ { G }$ and $\Phi _ { G }$ . We refer readers to [23] for the details. Here we briefly introduce how the user membership matrixes are unified to the same domain-invariant feature space. The matrixes of items are the same as the users.

Let $\pmb { P } _ { s } , \pmb { P } _ { t } \in \mathbb { R } ^ { K \times d }$ denote the two sets of bases for the subspaces of the source user membership matrix ${ \pmb U } _ { s } ^ { ( 0 ) }$ and the target user membership matrix ${ \pmb U } _ { { \pmb t } } ^ { ( { \pmb 0 } ) }$ , where ?? is the dimensionality of the matrixes, i.e., the number of user groups, and ?? is the dimension of the subspace. The subspaces can be obtained by principle component analysis (PCA) or other methods. ${ \pmb R } _ { s }$ is the orthogonal component to $P _ { s }$ . By performing generalized SVD,

$$
\boldsymbol {P} _ {t} ^ {T} \boldsymbol {P} _ {t} = \boldsymbol {U} _ {1} \boldsymbol {\Gamma} \boldsymbol {V} ^ {T}, \boldsymbol {R} _ {s} ^ {T} \boldsymbol {P} _ {t} = - \boldsymbol {U} _ {2} \boldsymbol {\Sigma} \boldsymbol {V} ^ {T}\tag{A.1}
$$

where ?? and $\pmb { \Sigma } \in \mathbb { R } ^ { d \times d }$ are diagonal matrixes. The diagonal elements of ?? and ?? are ?????? $\theta _ { i }$ and ?????? $\theta _ { i } ,$ , where $i = 1 , 2 , \ldots , d . \theta _ { i }$ are the angles between subspaces $P _ { s }$ and $P _ { t }$ .

To ensure the consistency of the user groups between both domains, the GFK operator is used to map the original user group membership matrixes to a domain-invariant space:

$$
\boldsymbol {\Psi} _ {G} \left(\boldsymbol {U} _ {s} ^ {(0)}, \boldsymbol {U} _ {t} ^ {(0)}\right) = \boldsymbol {U} _ {s} ^ {(0)} \boldsymbol {L}\tag{A.2}
$$

where ?? is ${ \pmb G } ^ { \prime } \mathrm { \bf s }$ square root, $L ^ { T } L = G ,$

$$
\boldsymbol {G} = \left[ \begin{array}{c c} \boldsymbol {P} _ {s} \boldsymbol {U} _ {1} & \boldsymbol {R} _ {s} \boldsymbol {U} _ {2} \end{array} \right] \left[ \begin{array}{c c} \boldsymbol {\Lambda} _ {1} & \boldsymbol {\Lambda} _ {2} \\ \boldsymbol {\Lambda} _ {2} & \boldsymbol {\Lambda} _ {3} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {U} _ {1} ^ {T} \boldsymbol {P} _ {s} ^ {T} \\ \boldsymbol {U} _ {2} ^ {T} \boldsymbol {R} _ {s} ^ {T} \end{array} \right]\tag{A.3}
$$

where $\pmb { { \cal A } } _ { 1 }$ to $\pmb { { \cal A } } _ { 3 }$ are diagonal matrixes whose diagonal elements are $\begin{array} { r } { \lambda _ { 1 } = 1 + \frac { s i n ( 2 \theta _ { i } ) } { 2 \theta _ { i } } , \lambda _ { 2 } = \frac { c o s ( 2 \theta _ { i } ) - 1 } { 2 \theta _ { i } } , \lambda _ { 3 } = } \end{array}$ $1 - \frac { s i n ( 2 \theta _ { i } ) } { 2 \theta _ { i } } .$

According to equations (16) and (17), $U _ { s } ^ { ( 1 ) } , V _ { s } ^ { ( 1 ) } , U _ { t } ^ { ( 1 ) }$ and $\pmb { V } _ { t } ^ { ( 1 ) }$ are obtained.

Appendix B. Proof of $f _ { u }$ and $f _ { v }$ ensuring consistency A definition for maps like $f _ { u }$ and $f _ { v }$ is given as follows.

Definition 3 (Distribution Consistency Maps). Given a source rating matrix $\pmb { X _ { s } } \in \mathbb { R } ^ { M _ { s } \times N _ { s } }$ and a target rating matrix $\pmb { X } _ { t } \in \mathbb { R } ^ { M _ { t } \times N _ { t } }$ , the tri-factorizations of $X _ { s }$ and $X _ { t }$ are group-consistent and they share consistent knowledge ?? such that

$$
\boldsymbol {X} _ {s} = \boldsymbol {U} _ {s} ^ {(1)} \boldsymbol {S} \left(\boldsymbol {V} _ {s} ^ {(1)}\right) ^ {T}\tag{B.1}
$$

$$
\boldsymbol {X} _ {t} = \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {S} \left(\boldsymbol {V} _ {t} ^ {(1)}\right) ^ {T}\tag{B.2}
$$

where $\pmb { U } _ { s } ^ { ( 1 ) } , \pmb { U } _ { t } ^ { ( 1 ) }$ are user group membership matrixes unified to the same domain-invariant feature space for the source and target domains, while $V _ { s } ^ { ( 1 ) }$ and $\pmb { V } _ { t } ^ { ( 1 ) }$ are unified item group membership matrixes. If maps $f _ { u }$ and $f _ { v }$ satisfy equation (20), we call $f _ { u }$ and $f _ { v }$ distribution consistency maps (DCM) for the two rating matrixes.

For a demonstration of a DCM map, we refer readers to some theoretical results in [28] for reliable unsupervised knowledge transfer including a linear monotonic map (LMM) and its related theorem. LMM is a map: $f ( { \boldsymbol { \mathscr { x } } } ) = { \boldsymbol { \mathscr { x } } } { \boldsymbol { \mathscr { u } } } .$ $\pmb { x } \in \mathbb { R } ^ { m \times n }$ $\pmb { u } \in \mathbb { R } ^ { n \times 1 }$ . A theorem for reliable unsupervised knowledge transfer is then given in [28], proving that LMM can ensure the process of unsupervised knowledge transfer is reliable. As in our situation, we give the theorem and proof as follows:

Theorem 1. Given a source rating matrix $\pmb { X _ { s } } \in \mathbb { R } ^ { M _ { s } \times N _ { s } }$ and a target rating matrix $\pmb { X } _ { t } \in \mathbb { R } ^ { M _ { t } \times N _ { t } }$ , the trifactorizations of $X _ { s }$ and ?? $\pmb { X _ { t } }$ are group-consistent and they share a consistent knowledge ?? as in equations (B.1) and (B.2). When ${ \pmb u } \ge { \pmb 0 }$ and $\pmb { v } \ge \mathbf { 0 } , f _ { u } \Big ( \pmb { U } _ { t } ^ { ( 1 ) } \Big ) = \pmb { U } _ { t } ^ { ( 1 ) } ,$ ?? and $f _ { v } \Big ( V _ { t } ^ { ( 1 ) } \Big ) = V _ { t } ^ { ( 1 ) } v$ , they are DCMs for two rating matrixes.

Proof. When ${ \pmb u } \ge { \pmb 0 }$ and $v \geq 0 , f _ { u } \Big ( U _ { t } ^ { ( 1 ) } \Big ) = U _ { t } ^ { ( 1 ) } u$ and $f _ { v } \Big ( V _ { t } ^ { ( 1 ) } \Big ) = V _ { t } ^ { ( 1 ) } v$ can satisfy the following equation:

$$
P \left(\boldsymbol {S} \mid \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {u}, \boldsymbol {V} _ {t} ^ {(1)}\right) = P \left(\boldsymbol {S} \mid \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {I}, \boldsymbol {V} _ {t} ^ {(1)}\right)
$$

Then, to fix $f _ { u } \Big ( U _ { t } ^ { ( 1 ) } \Big )$ , we use the following equation:

$$
P \left(\boldsymbol {S} \mid \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {u}, \boldsymbol {V} _ {t} ^ {(1)} \boldsymbol {v}\right) = P \left(\boldsymbol {S} \mid \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {u}, \boldsymbol {V} _ {t} ^ {(1)} \boldsymbol {I}\right)
$$

So, we then have

$$
P \left(\boldsymbol {S} \left| f _ {u} \left(\boldsymbol {U} _ {\boldsymbol {t}} ^ {(1)}\right), f _ {v} \left(\boldsymbol {V} _ {\boldsymbol {t}} ^ {(1)}\right)\right) = P \left(\boldsymbol {S} \mid \boldsymbol {U} _ {\boldsymbol {t}} ^ {(1)}, \boldsymbol {V} _ {\boldsymbol {t}} ^ {(1)}\right) \right.
$$

Based on Definition 3, $f _ { u } \Big ( U _ { t } ^ { ( 1 ) } \Big ) = U _ { t } ^ { ( 1 ) } \ i$ ?? and $f _ { v } \Big ( V _ { t } ^ { ( 1 ) } \Big ) = V _ { t } ^ { ( 1 ) } { \ i }$ ?? are DCMs.

Hence, the LMM is proven to be a DCM, which means we can let $f _ { u }$ and $f _ { v }$ have the following expressions:

$$
f _ {u} \Big (\boldsymbol {U} _ {t} ^ {(1)} \Big) = \boldsymbol {U} _ {t} ^ {(1)} \boldsymbol {u}, \boldsymbol {u} \geq \boldsymbol {0}\tag{B.3}
$$

$$
f _ {v} \left(\boldsymbol {V} _ {t} ^ {(1)}\right) = \boldsymbol {V} _ {t} ^ {(1)} \boldsymbol {v}, \boldsymbol {v} \geq \mathbf {0}\tag{B.4}
$$

where $\pmb { u } \in \mathbb { R } ^ { K \times K }$ is user tuning factor and $\pmb { v } \in \mathbb { R } ^ { L \times L }$ is item tuning factor.

## Acknowledgement

This work was supported by the Australian Research Council (ARC) under Discovery Grant [DP150101645].

## References

[1] J. Lu, D. Wu, M. Mao, W. Wang, and G. Zhang, "Recommender system application developments: a survey," Decision Support Systems, vol. 74, pp. 12-32, 2015.

[2] M. Deshpande and G. Karypis, "Item-based top-n recommendation algorithms," ACM Transactions on Information Systems, vol. 22, no. 1, pp. 143-177, 2004.

[3] Y. Koren, R. Bell, and C. Volinsky, "Matrix factorization techniques for recommender systems," Computer, vol. 22, no. 8, pp. 30-37, 2009.

[4] J. Liu, C. Wu, and W. Liu, "Bayesian probabilistic matrix factorization with social relations and item contents for recommendation," Decision Support Systems, vol. 55, no. 3, pp. 838-850, 2013.

[5] H. Wang, N. Wang, and D.-Y. Yeung, "Collaborative deep learning for recommender systems," in Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2015, pp. 1235-1244: ACM.

[6] H.-N. Kim, A. El-Saddik, and G.-S. Jo, "Collaborative error-reflected models for cold-start recommender systems," Decision Support Systems, vol. 51, no. 3, pp. 519-531, 2011.

[7] V. Y. Yoon, R. E. Hostler, Z. Guo, and T. Guimaraes, "Assessing the moderating effect of consumer product knowledge and online shopping experience on using recommendation agents for customer loyalty," Decision Support Systems, vol. 55, no. 4, pp. 883-893, 2013.

[8] X. Li, M. Wang, and T.-P. Liang, "A multi-theoretical kernel-based approach to social network-based recommendation," Decision Support Systems, vol. 65, pp. 95-104, 2014.

[9] Y.-M. Li, C.-T. Wu, and C.-Y. Lai, "A social recommender mechanism for e-commerce: Combining similarity, trust, and relationship," Decision Support Systems, vol. 55, no. 3, pp. 740-752, 2013.

[10] J. McAuley and A. Yang, "Addressing complex and subjective product-related queries with customer reviews," in Proceedings of the 25th International Conference on World Wide Web, 2016, pp. 625- 635: International World Wide Web Conferences Steering Committee.

[11] J. Lu, V. Behbood, P. Hao, H. Zuo, S. Xue, and G. Zhang, "Transfer learning using computational intelligence: a survey," Knowledge-Based Systems, vol. 80, pp. 14-23, 2015.

[12] W. Pan, "A survey of transfer learning for collaborative recommendation with auxiliary data," Neurocomputing, vol. 177, pp. 447-453, 2016.

[13] W. Chen, W. Hsu, and M. L. Lee, "Making recommendations from multiple domains," in Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2013, pp. 892-900: ACM.

[14] A. P. Singh and G. J. Gordon, "Relational learning via collective matrix factorization," in Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2008, pp. 650-658: ACM.

[15] N. Mirbakhsh and C. X. Ling, "Improving top-n recommendation for cold-start users via crossdomain information," ACM Transactions on Knowledge Discovery from Data, vol. 9, no. 4, p. 33, 2015.

[16] W. Pan and Q. Yang, "Transfer learning in heterogeneous collaborative filtering domains," Artificial Intelligence, vol. 197, pp. 39-55, 2013.

[17] L. Hu, J. Cao, G. Xu, L. Cao, Z. Gu, and C. Zhu, "Personalized recommendation via cross-domain triadic factorization," in Proceedings of the 22nd International Conference on World Wide Web, 2013, pp. 595-606: ACM.

[18] B. Li, Q. Yang, and X. Xue, "Can movies and books collaborate? Cross-domain collaborative filtering for sparsity reduction," in Proceedings of the 21th International Joint Conference on Artificia Intelligence, 2009, vol. 9, pp. 2052-2057.

[19] B. Li, Q. Yang, and X. Xue, "Transfer learning for collaborative filtering via a rating-matrix generative model," in Proceedings of the 26th Annual International Conference on Machine Learning, 2009, pp. 617-624: ACM.

[20] B. Li, X. Zhu, R. Li, and C. Zhang, "Rating knowledge sharing in cross-domain collaborative filtering," IEEE Transactions on Cybernetics, vol. 45, no. 5, pp. 1068-1082, 2015.

[21] C. Ding, T. Li, W. Peng, and H. Park, "Orthogonal nonnegative matrix tri-factorizations for clustering," in Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2006, pp. 126-135: ACM.

[22] L. Si and R. Jin, "Flexible mixture model for collaborative filtering," in Proceedings of the 20th International Conference on Machine Learning, 2003, vol. 3, pp. 704-711.

[23] B. Gong, K. Grauman, and F. Sha, "Learning kernels for unsupervised domain adaptation with applications to visual object recognition," International Journal of Computer Vision, vol. 109, no. 1- 2, pp. 3-27, 2014.

[24] Z. Zhang, H. Lin, K. Liu, D. Wu, G. Zhang, and J. Lu, "A hybrid fuzzy-based personalized recommender system for telecom products/services," Information Sciences, vol. 235, pp. 117-129, 2013.

[25] D. Wu, G. Zhang, and J. Lu, "A fuzzy preference tree-based recommender system for personalized business-to-business e-services," IEEE Transactions on Fuzzy Systems, vol. 23, no. 1, pp. 29-43, 2015.

[26] M. Al-Hassan, H. Lu, and J. Lu, "A semantic enhanced hybrid recommendation approach: a case study of e-Government tourism service recommendation system," Decision Support Systems, vol. 72, pp. 97-109, 2015.

[27] P. Cremonesi and M. Quadrana, "Cross-domain recommendations without overlapping data: myth or reality?," in Proceedings of the 8th ACM Conference on Recommender systems, 2014, pp. 297-300: ACM.

[28] F. Liu, G. Zhang, H. Lu, and J. Lu, "Heterogeneous Unsupervised Cross-domain Transfer Learning," arXiv:1701.02511 [cs.LG], pp. 1–47, 2017. https://arxiv.org/abs/1701.02511.

# ACCEPTED MANUSCRIPT

## Biographical Note

Qian Zhang studies at the University of Technology Sydney, Australia since 2014. She is a PhD student and she is a member of the Decision Systems and e-Service Intelligence Research Lab in the Centre for Artificial Intelligence. Her research interests include recommender systems and personalized techniques. Besides, she specializes in cross-domain recommender systems.

Dr. Dianshuang Wu is a Postdoctoral Research Fellow in the School of Software, Faculty of Engineering and Information Technology, at the University of Technology Sydney, Australia. He is a member of the Decision Systems and e-Service Intelligence Research Lab in the Centre for Artificial Intelligence. His research interests include tree similarity measure, recommender systems, and business intelligence.

Professor Jie Lu is the Associate Dean Research (acting) in the Faculty of Engineering and Information Technology (FEIT) at the University of Technology, Sydney (UTS). She was Head of School of Software in the FEIT. She is also the Director of Decision Systems & e-Service Intelligence lab in the Centre for Artificial Intelligence. Her research interests lie in the area of recommender systems, decision support systems and eservices intelligence. She has published five research books and 350 papers, won seven Australian Research Council discovery grants and 10 other grants. She received a University Research Excellent Medal in 2010. She serves as Editor-In-Chief for Knowledge-Based Systems (Elsevier), editor for book series on Intelligen Information Systems (World Scientific) and guest editor of six special issues for international journals, as well as delivered six keynote speeches at international conferences.

Feng Liu is working toward the Ph.D. degree with the Faculty of Engineering and Information Technology, University of Technology Sydney, Australia since 2016. He is a Member of the Decision Systems and e-Service Intelligence (DeSI) Research Laboratory, Center for Artificial Intelligence. His research interests include transfer learning and domain adaptation.

Dr. Guangquan Zhang is an Associate Professor and Co-Director of the Decision Systems an e-Service Intelligence Lab, Centre for Artificial Intelligence, Faculty of Engineering and Information Technology, University of Technology Sydney, Australia. He has authored and coauthored 324 publications including four monographs, five text books, 17 book chapters, and 154 refereed international journal papers. His research interests lie in the area of decision support systems, uncertain information processing and fuzzy measure. Dr. Zhang has been awarded six Australian research council discovery grants, served as an Advisory Board Member or a Member of the editorial boards of several international journals and co-chaired several international conferences/workshops in the area of decision-making and knowledge engineering.

## Highlights:

 Consistent knowledge is defined for cross-domain recommender on what to transfer.

 A new domain adaptation method handling domain shift in cross-domain recommender.

 A new adaptive knowledge transfer method relies on user and item group-consistency in two domains.

 The proposed method alleviates the reduction of accuracy for cold-start users.
