---
otero_id: 4256
otero_key: "NTKSMBYD"
title: "Recommender system based on workflow"
authors: "Lu Zhen; George Q. Huang; Zuhua Jiang"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.08.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Recommender system based on work<sup>fl</sup>ow

Lu Zhen <sup>a,</sup>⁎, George Q. Huang <sup>b</sup>, Zuhua Jiang <sup>c</sup>

<sup>a</sup> Department of Industrial and Systems Engineering, National University of Singapore, Singapore

<sup>b</sup> Department of Industrial and Manufacturing Systems Engineering, The University of Hong Kong, PR China

<sup>c</sup> Department of Industrial Engineering and Management, Shanghai Jiao Tong University, Shanghai, PR China

## a r t i c l e i n f o

Article history: Received 14 December 2008 Received in revised form 29 July 2009 Accepted 23 August 2009 Available online 29 August 2009

Keywords: Recommender system Work<sup>fl</sup>ow Collaborative <sup>fi</sup>ltering Knowledge management

## a b s t r a c t

This paper proposes a work<sup>fl</sup>ow-based recommender system model on supplying proper knowledge to proper members in collaborative team contexts rather than daily life scenarios, e.g., recommending commodities, <sup>fi</sup>lms, news, etc. Within collaborative team contexts, more information could be utilized by recommender systems than ordinary daily life contexts. The work<sup>fl</sup>ow in collaborative team contains information about relationships among members, roles and tasks, which could be combined with collaborative <sup>fi</sup>ltering to obtain members' demands for knowledge. In addition, the work schedule information contained in the work<sup>fl</sup>ow could also be employed to determine the proper volume of knowledge that should be recommended to each member. In this paper, we investigate the mechanism of the work<sup>fl</sup>ow-based recommender system, and conduct a series of experiments referring to several realworld collaborative teams to validate the effectiveness and ef<sup>fi</sup>ciency of the proposed methods.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

This study concerns knowledge recommender systems for collaborative team contexts, rather than general situations in daily life, e.g., recommending commodities, news, <sup>fi</sup>lms to customers. Among a collaborative team, members usually come from diverse disciplines, each with particular expertise and contribution from their relevant areas. Thus, their demands for knowledge are also different from each other. Recommender system provides a platform to deliver right knowledge in the right context to the right person in the right volume [27,34,36].

This paper proposes a work<sup>fl</sup>ow-based recommender system model, which is oriented to the collaborative team environment. Within this context, more information could be utilized by recommender systems, comparing to ordinary daily life situations. Work-<sup>fl</sup>ow is one type of collaborative processes and it virtually exists behind every collaborative team [37,38]. The work<sup>fl</sup>ow in the collaborative team environment contains members-roles-tasks reference information that describes which member plays which roles or ful<sup>fi</sup>lls which tasks. This reference information could be combined with collaborative <sup>fi</sup>ltering to obtain members' demands for knowledge. It ensures that knowledge resources in proper domains will be recommended to proper members in collaborative team. Moreover, the volume of those recommended knowledge resources should also be proper for each member. Otherwise, too much knowledge is recommended to some busy members, which will cause information overload and interruption to them. In our study, the work schedule information contained in the work<sup>fl</sup>ow is utilized to determine the proper volume of recommended knowledge for each member.

This paper investigates the mechanism of the work<sup>fl</sup>ow-based recommender system, and conducts a series of experiments referring to several real-world collaborative teams so as to validate the effectiveness and ef<sup>fi</sup>ciency of the proposed methods. The rest of this paper is organized as follows. Some related works done by other scholars are brie<sup>fl</sup>y introduced in the next section. In Section 3, we introduce the application background: collaborative environment, which is the basis for our proposed method. Then, Section 4 addresses the general framework of the work<sup>fl</sup>ow-based recommender system, and analyzes two key technical issues. Sections 5 and 6 investigate those issues in detail respectively: work<sup>fl</sup>ow-based collaborative <sup>fi</sup>ltering, and recommendation volume control by using the schedule information in work<sup>fl</sup>ow. For performances evaluation, several experiments are conducted to validate the proposed model and methods in Section 7. Closing remark and summary are then outlined in the last section.

## 2. Related works

The recommendation technology has become a promising and hot area in both academia and industries; numerous recommender systems (RS) have been developed [2]. Tapestry [7] is one of the earliest RSs. Based on this work, several automated RSs were designed and implemented. A RS for news and movie recommendations was developed by Konstan et al. [13]. For book recommendation, Mooney and Roy proposed a content-based RS [23]. McNee et al. designed a RS to help recommend research papers' citation [19]. Citeseer [3], Webpersonalizer [22], GroupLens [13], SiteSeer [25] <sup>fi</sup>lter and recommend web information according to the similarities between web resources and users' interests. For improving sales on ecommerce websites, a taxonomy RS was developed by Schafer et al. [26]. Ontology technologies were also brought into RS researches. Middleton et al. explored a novel ontological approach for user pro<sup>fi</sup>ling within RS, which could recommend on-line academic research papers [20,21]. Li and Zhong presented an abstract Web mining model for extracting approximate concepts hidden in user pro<sup>fi</sup>les, which could make recommendation much more ef<sup>fi</sup>cient [14,15]. Godoy and Amandi designed a document clustering algorithm that carried out incremental, unsupervised concept learning over Web documents for acquiring user pro<sup>fi</sup>les to support recommendation of web information [6]. Yu et al. suggested a hybrid collaborative <sup>fi</sup>ltering method for multiple-interests and multiple-content recommendation in e-commerce [31]. By analyzing customer behaviors (navigational patterns), Yong et al. designed a collaborative <sup>fi</sup>ltering based RS for e-commerce sites [30]. Yeong et al. proposed a new methodology in which customer purchase sequences were used to improve the quality of collaborative <sup>fi</sup>ltering based recommendation [29]. Liang et al. developed a knowledge recommender that allows customized content to be suggested based on the user's browsing pro<sup>fi</sup>le. The method adopts a semantic-expansion approach to build the user pro<sup>fi</sup>le by analyzing documents previously read by the person [16]. Malinowski et al. developed a relational recommendation approach for providing an automated pre-selection of candidates that <sup>fi</sup>t best with future team members [18]. Gar<sup>fi</sup>nkel et al. designed a recommender system which extends the one-product-at-a-time search approach used in current ‘Shopbot’ implementations to consider purchasing plans for a bundle of items [4]. They also developed ‘Shopbot 2.0’ to integrate recommendations and promotions with comparison shopping [5]. Jiang et al. studied how to maximize customer satisfaction through an online recommende system, and proposed a novel associative classi<sup>fi</sup>cation model. Products could be recommended to the potential buyer if the model predicts his/her satisfaction level will be high [9]. Kagie et al. designed a graphical shopping interface based on product attributes. It represents the mutual similarities of the recommended products in a two dimensional map, where similar products are located close to each other and dissimilar products far apart [11]. Wang et al. developed a navigation graph-based recommender system, in which the navigation patterns of previous website visitors are utilized to provide recommendations for newcomers [28].

To adapt recommendation technologies to large scale peer-to-peer (P2P) environment, Han et al. suggested a distributed collaborative <sup>fi</sup>ltering algorithm to construct a scalable distributed RS [8]. Kim et al. implemented an image content recommender in P2P architecture [12]. Olsson developed a headline recommender system in P2P environment without centralized control [24]. As to multi-dimensional RS [1], a work<sup>fl</sup>ow space based collaborative <sup>fi</sup>ltering method was proposed in [35]. However, those systems mainly concern personalized recommendations in ordinary daily life situations, e.g., recommending commodities, news, <sup>fi</sup>lms to customers. They have not considered speci<sup>fi</sup>c applications of knowledge recommendation in collaborative team context, or about some speci<sup>fi</sup>c business processes. Jung proposed blog context overlay network architecture for context matching between blogs, so as to realize knowledge recommendation and distribution among members in community [10]. Liu and Wu developed a novel task-based knowledge recommender. A modi<sup>fi</sup>ed relevance feedback technique, which is integrated with the taskrelevance assessment method, could be enabled to provide knowledge workers with task-relevant information based on task pro<sup>fi</sup>les [17]. Based on knowledge grid environment, some conceptual models of proactive knowledge recommender system and reactive knowledge query platform were proposed in [32,33].

## 3. Work<sup>fl</sup>ow-centric collaborative environment

The recommender system model proposed in this paper is mainly oriented to the work<sup>fl</sup>ow-centric collaborative environment, and one example is illustrated in Fig. 1. This collaborative environment consists of three key concepts: members, roles and tasks. Members are the core factor in collaborative environment. All the knowledge is produced and also used by members while performing their tasks. Each member in a collaborative organization may have one or more roles, e.g., product engineer, design engineer, test engineer, mechanic designer, etc. Moreover, there are up-low relationships between those various roles, all of which constitute a role hierarchy, denoted by ‘role tree’. The role tree re<sup>fl</sup>ects the organization architecture of a collaborative team. Besides the mapping with the member list, the role tree also has the mapping with the task model. As shown in Fig. 1, Mapping\_1 deploys the roles onto tasks in work<sup>fl</sup>ow; Mapping\_2 deploys the roles onto members in member list.

The work<sup>fl</sup>ow-centric collaborative environment is the application context for our proposed recommender model, while traditional recommender systems are oriented to general situations in daily life. The collaborative environment contains some potentially useful relationships among the collaborative members, which could be utilized to support collaborative <sup>fi</sup>ltering in recommender systems.

## 4. The framework of recommender system based on work<sup>fl</sup>ow

As for the implementation of recommender systems in collaborative environment, there exist two core issues. Firstly, as to the recommended knowledge, which domains are suitable for each member? Secondly, what is the suitable volume of recommended knowledge for each member? Once the above two questions are answered, the proper knowledge could be delivered to the proper persons in the proper volume. Fig. 2 illustrates the general framework of the recommender system based on work<sup>fl</sup>ow. There are two core modules in the model, which are marked in the <sup>fi</sup>gure.

For the <sup>fi</sup>rst issue, a novel collaborative <sup>fi</sup>ltering based on task (or role) relationships from work<sup>fl</sup>ow is proposed to obtain the ‘members-to-knowledge domains' relation table, which re<sup>fl</sup>ects the members' demands for suitable domain knowledge.

For the second issue, a statistic analysis method is proposed to obtain the occupancy scale from the schedule in work<sup>fl</sup>ow, so as to determine the suitable volume of the recommended knowledge.

The following two sections will give details to the above two key issues respectively.

## 5. Collaborative <sup>fi</sup>ltering based on work<sup>fl</sup>ow

This section investigates the <sup>fi</sup>rst key issue: as to the recommended knowledge for each member, how to determine suitable domain that may be potentially useful for him (or her). We proposed a novel collaborative <sup>fi</sup>ltering method based on work<sup>fl</sup>ow to reach the above target.

Work<sup>fl</sup>ow realizes work cooperation between team members through a de<sup>fi</sup>nite logical process, and it is used to integrate distributed and heterogeneous tasks (activities) into a uni<sup>fi</sup>ed process. Abundant information is contained in work<sup>fl</sup>ow, e.g., the logical dependence order relationships between team members' tasks (activities), and member-roles–tasks reference information that describes which member plays which roles or ful<sup>fi</sup>lls which tasks. The above information could be combined with collaborative <sup>fi</sup>ltering so as to obtain members' demands for knowledge from their correlative colleagues. It guarantees that knowledge resources in proper domains could be recommended to proper members in the collaborative team.

![](/api/attachments/NTKSMBYD/fulltext/images/210f5595794414405c217383daeb735dace1d39a3cbb4e7728456c692f192699.jpg)  
Fig. 1. An example of the work<sup>fl</sup>ow-centric collaborative environment.

## 5.1. Collaborative filtering based on the same task or role

Collaborative methods try to predict a member's preferences based on the preferences of other similar members. More formally, the weight of a knowledge category c for member m is estimated according to the weights assigned to category c by those members who are ‘similar’ to member m.

Various approaches have been used to quantify the similarities between members, such as Pearson correlation coef<sup>fi</sup>cient, Cosinebased approach, etc. In this paper, we make use of the information of task and role. There is an assumption here: members in the same task or role could be regarded as ‘similar’ members. In this way, we could avoid calculation for members' similarities. The process of determining ‘similar’ members based on the information of task or role could be much faster and more rational. As shown in Fig. 3, ‘Member-1’ has three colleagues in the same task (T\_3). The knowledge demands of ‘Member-1’ will be in<sup>fl</sup>uence by the other three members (‘Member-2’, ‘Member-3’, ‘Member-4’). In addition, those three colleagues (e.g., Member-2, 3, and 4) may be different in working experiences; veteran colleagues will have more in<sup>fl</sup>uence on the knowledge demands of ‘Member-1’ than novice colleagues.

![](/api/attachments/NTKSMBYD/fulltext/images/c2e17ed17696d221127964e29c5c86675fd3b1a888236e49f14e25d293ac8a6f.jpg)  
Fig. 2. The framework of the recommender system based on work<sup>fl</sup>ow

As to the member's knowledge demands, the weight of category c<sub>i</sub> for member m (denoted by $w _ { m , i } )$ is calculated as follows:

$$
w _ {m, i} = \overline {{w _ {m}}} + k \sum_ {m ^ {\prime} \in \widehat {M}} w (m ^ {\prime}) \times (w _ {m ^ {\prime}, i} - \overline {{w _ {m ^ {\prime}}}})\tag{1}
$$

where M denotes the set of N members that belong to the same task or role. w(m′)is the weight of the member m′ in the task or role. In this paper, it is measured by the difference between the current year and the year the member took up the task or role. Veteran members (with longer working experiences) will have more in<sup>fl</sup>uence on others' knowledge demands than novice members. It is assumed that a member with hl years experience will have a half in<sup>fl</sup>uence of expert who may have the highest in<sup>fl</sup>uence value. Here, the hl, abbreviated from ‘half-life span’, is a parameter to determine the impact degree from experts to novices. For example, if the highest in<sup>fl</sup>uence value is set as 1.0 and hl as 5, it means that a member with 5years working experience, his (or her) weight w(m) equals to 0.5. Members' weights will approach 1.0 with their working experiences increase larger and larger. In formula (1), the weight of members and some coef<sup>fi</sup>cients are de<sup>fi</sup>ned as:

$$
w (m ^ {\prime}) = \frac {2}{\pi} \arctan (\text { Year } (m ^ {\prime}) / h l)\tag{2}
$$

$$
k = 1 \Big / \sum_ {m ^ {\prime} \in \widehat {M}} w (m ^ {\prime})\tag{3}
$$

$$
\overline {{w _ {m}}} = (1 / | S _ {c} |) \times \sum_ {c \in S _ {c}} w _ {m, c}\tag{4}
$$

$$
S _ {c} = \{c \in C | w _ {c, m} \neq \phi \}.\tag{5}
$$

## 5.2. Multi-layer workflow and relationship types

Considering the complex architectures of collaborative teams' work<sup>fl</sup>ow, the members who belong to two different tasks should also be regarded as having some relationships and in<sup>fl</sup>uences on each other. For example, members belong to two different tasks: ‘diesel design’ and ‘engine design’. The former one is actually a subtype of the latter one. The two different tasks are virtually correlative. Therefore, the members, who belong to the two tasks, should also have in<sup>fl</sup>uences on each other. Besides the above mentioned ‘subtype’ relationship between tasks. There exist other relationship types as shown in Fig. 4.

![](/api/attachments/NTKSMBYD/fulltext/images/d984ff8bc52b1d08453854127f4b699e7e7c67cea140b45567cd62230106f748.jpg)  
Fig. 3. The collaborative <sup>fi</sup>ltering based on the same task.

The relationships among tasks could be de<sup>fi</sup>ned as: $T _ { 1 } { \mathrm { - } } \alpha { \mathrm { - } } > \mathrm { T } _ { 2 } ,$ where α is a type of semantic relationship between two tasks $\mathrm { T } _ { 1 }$ and $\mathrm { T } _ { 2 } .$ Some types of semantics are de<sup>fi</sup>ned as follows:

Part of: denoted as $\mathrm { T } _ { 1 } { \cdot } p a r { - } > \mathrm { T } _ { 2 } ,$ where $\mathrm { T } _ { 1 }$ is a part of $\mathrm { T } _ { 2 } .$ As shown in Fig. $4 , \ : \mathrm { T } _ { - } 1 ^ { \prime } , \ : \mathrm { T } _ { - } 2 ^ { \prime } , \ : \mathrm { T } _ { - } 3 ^ { \prime } , \ : \mathrm { T } _ { - } 4 ^ { \prime }$ are part of $\mathrm { ~  ~ \because ~ } | \mathrm { ~  ~ \cdot ~ } | \mathrm { ~  ~ \cdot ~ }$ respectively.

Sequential: denoted as $\mathrm { T } _ { 1 } { \cdot } \mathrm { s e q } { \cdot } > \mathrm { T } _ { 2 } ,$ which de<sup>fi</sup>nes that $\mathrm { T } _ { 1 }$ should be ful<sup>fi</sup>lled before $\mathrm { T } _ { 2 } .$ For example, the task ‘building mathematic model for compressor’ -seq-N‘the simulation of compressor’.

Subtype: denoted as $\mathrm { T } _ { 1 } { \cdot } s u b { \cdot } s \mathrm { T } _ { 2 } ,$ which describes the relationship between a general task $\mathrm { T _ { 1 } }$ and a speci<sup>fi</sup>c task $\mathrm { T } _ { 2 } .$ For example, the task ‘engine design’ -sub-N‘diesel design’.

Supplement: denoted as $\mathrm { T } _ { 1 } { \cdot } s u p { \cdot } > \mathrm { T } _ { 2 }$ , which means that $\mathrm { T } _ { 2 }$ servers as the supplementary or additional task to $\mathrm { T } _ { 1 } .$

Corequisite: denoted as ${ \mathrm { T } } _ { 1 } { \mathrm { - } } C O r { \mathrm { - } } > { \mathrm { T } } _ { 2 } ,$ which denotes that $\mathrm { T _ { 1 } }$ and $\mathrm { T } _ { 2 }$ should be ful<sup>fi</sup>lled in parallel. The corequisite relationship is symmetric. As shown in Fig. 4, ‘T\_2’, and $\ " \mathrm { T } _ { - 3 } \cdot$ are corequisite with each other.

Besides the <sup>fi</sup>ve types of relationships as described above, there may be other types that are also involved in the work<sup>fl</sup>ow model. For each type of relationship, a Relationship Similarity Coef<sup>fi</sup>cient (RSC), which is between 0 and 1, is assigned by experts or knowledge engineers. The purpose of RSC is to calculate the in<sup>fl</sup>uence between two members, which is de<sup>fi</sup>ned by In<sup>fl</sup>uence Coef<sup>fi</sup>cient (InfC).

Rule 1: if two members $M _ { 1 }$ and $M _ { 2 } ,$ two tasks $T _ { 1 }$ and $T _ { 2 } , M _ { 1 } \in T _ { 1 }$ and $M _ { 2 } \in T _ { 2 }$ , ∃α: $T _ { 1 } \mathbf { - } \mathbf { \alpha } \mathbf { - } > T _ { 2 }$ , (α is a type of relationship among tasks); then $\mathrm { I n f C } ( M _ { 1 } , M _ { 2 } ) = \mathrm { R S C } ( \alpha )$

Rule 2: if two members M<sub>1</sub> and $M _ { 2 }$ , two tasks $T _ { 1 }$ and $T _ { 2 } , M _ { 1 } \in T _ { 1 }$ and $M _ { 2 } \in T _ { 2 } , \exists \mathsf { p a t h } _ { 1 } = \alpha _ { 1 } ^ { 1 } \alpha _ { 2 } ^ { 1 } . . . \alpha _ { N _ { 1 } } ^ { 1 } , \mathsf { p a t h } _ { 2 } = \alpha _ { 1 } ^ { 2 } \alpha _ { 2 } ^ { 2 } . . . a _ { N _ { 2 } } ^ { 2 } , . . . , \mathsf { p a t h } _ { m } =$ $\alpha _ { 1 } ^ { m } \alpha _ { 2 } ^ { m } . . . \alpha _ { N _ { m } } ^ { m } , T _ { 1 ^ { - } } \mathrm { p a t h } _ { 1 ^ { - } } > T _ { 2 } , T _ { 1 ^ { - } } \mathrm { p a t h } _ { 2 ^ { - } } > T _ { 2 } , . . . , T _ { 1 ^ { - } } \mathrm { p a t h } _ { m ^ { - } } > T _ { 2 } , ( \alpha _ { 1 }  \alpha _ { 2 }  T _ { 1 ^ { - } } \mathrm { p a t h } _ { m ^ { - } } ) > T _ { 1 ^ { - } } \mathrm { p a t h } _ { m ^ { - } } .$ is a type of relationship among tasks, $N _ { m }$ is the length of the mth path); then $\mathrm { I n f C } ( M _ { 1 } , ~ M _ { 2 } ) = \mathrm { M a x } ( \prod _ { i } ~ \mathrm { R S C } ( \alpha _ { i } ^ { 1 } ) , \prod _ { i } ~ R S C ( \alpha _ { i } ^ { 2 } ) , . . . , \prod _ { i }$ $\mathsf { R S C } ( \alpha _ { i } ^ { m } ) )$ .

In the situation of ‘members belong to the same task or role’, as mentioned in the previous subsection, the RSC and the Inf $\Upsilon ( \mathbf { M } _ { 1 } , \mathbf { M } _ { 2 } )$ are both 1.

![](/api/attachments/NTKSMBYD/fulltext/images/b578120ca8f09f5ba64e1d0394d64085bc095a5eec84568d214ec26ba4ae7f6e.jpg)  
Fig. 4. The architecture of multi-layer work<sup>fl</sup>ow.

Here, there may be more than one paths or relationship chains between two tasks among the above multi-layer work<sup>fl</sup>ow. As shown in Fig. 3, two tasks $\begin{array} { r } { T _ { - } 1 , T _ { - } 2 , T _ { 1 } \mathrm { - s e q - > } T _ { 2 } , } \end{array}$ and two members $M _ { 1 } \in T _ { 1 }$ and $M _ { 2 } \in T _ { 2 } ,$ we can have InfC $( M _ { 1 } , M _ { 2 } ) = { \tt R S C } ( { \tt s e q } )$ ). However, T\_1 and T\_2 also belong to the same task (T\_b) in the upper layer. That is: T\_1 b-par-T b-par- NT\_2. According to the above rules, InfC $( M _ { 1 } , M _ { 2 } )$ could also be de<sup>fi</sup>ned as $\mathsf { R S C } ( p a r ) \times \mathsf { R S C } ( p a r )$ ). Based on the above two paths between tasks T\_1 and T\_2, the max value of ‘RSC (seq)’ and ‘RSC(par) × RSC(par)’ will be assigned to InfC $\mathbf { \Omega } ( \mathbf { M } _ { 1 } , \mathbf { M } _ { 2 } )$

It should be mentioned that those prede<sup>fi</sup>ned values to the above relationships (e.g., RSC(par), RSC(seq), etc.) are very important, which will affect the in<sup>fl</sup>uence value between members $( \operatorname { I n f C } ( M _ { 1 } , M _ { 2 } ) )$ . For determining rational values to those relationships coef<sup>fi</sup>cients, we conduct some experiments in Section 7.

## 5.3. Collaborative filtering based on the correlative tasks or roles

In the previous section, we analyze the relationships among tasks from a view of multi-layer work<sup>fl</sup>ow architecture, and de<sup>fi</sup>ne in<sup>fl</sup>uence coef<sup>fi</sup>cients (InfC) between members. The goal of above analysis is to calculate members' knowledge demands more precisely.

Based on the in<sup>fl</sup>uence coef<sup>fi</sup>cient between two members, we could calculate the members' knowledge demands through collaborative <sup>fi</sup>ltering. We could make some revision on the previous formula (1) in Section 5.1 by adding the in<sup>fl</sup>uence coef<sup>fi</sup>cient (InfC). The new formula is revised as follows:

$$
w _ {m, i} = \overline {{w _ {m}}} + k \sum_ {m ^ {\prime} \in \widehat {M}} w (m ^ {\prime}) \times \operatorname{InfC} (m, m ^ {\prime}) \times (w _ {m ^ {\prime}, i} - \overline {{w _ {m ^ {\prime}}}})\tag{6}
$$

where:

$$
w (m ^ {\prime}) = \frac {2}{\pi} \arctan (\text { Year } (m ^ {\prime}) / \text { hl })\tag{7}
$$

$$
k = 1 \Big / \sum_ {m ^ {\prime} \in \widehat {M}} w (m ^ {\prime})\tag{8}
$$

$$
\overline {{w _ {m}}} = (1 / | S _ {c} |) \times \sum_ {c \in S _ {c}} w _ {m, c}\tag{9}
$$

$$
S _ {c} = \{c \in C | w _ {c, m} \neq \phi \}.\tag{10}
$$

The new formulas consider the in<sup>fl</sup>uence between members in more aspects and take into account the relationships among tasks. All members are involved in collaborative team's work<sup>fl</sup>ow, which is a complex architecture of tasks, roles and members. Those tasks or roles relationships would have impacts on the correlations between collaborative team members, hence in<sup>fl</sup>uence their demands for knowledge.

## 6. Recommendation volume control based on work<sup>fl</sup>ow

Besides providing knowledge in suitable domains, the volume of the recommended knowledge should also be appropriate. This section will give details to the second issue mentioned in Section 4. We propose a statistic analysis method to obtain the occupancy from the schedule in work<sup>fl</sup>ow, so as to determine the suitable volume for knowledge recommendation.

## 6.1. Control the volume by threshold

For busy members, only those knowledge resources that have higher correlations with them will be recommended. On the contrary, more knowledge resources would be delivered to free members. We use some threshold values to control the suitable volume of recommended knowledge. As to busy members (with a high occupancy scale), only the knowledge resources whose correlation degree exceed a high threshold value will be recommended. While more knowledge resources are recommended to free members with lower occupancy scale. Here, the correlation degree is the similarity between member's demands and knowledge resources' descriptions. For example, for busy members who have high occupancy scale, we could set a higher threshold value, e.g., 0.9. It means only the knowledge resources with the correlation degree higher than 0.9 will be recommended to him (or her). On the contrary, for members with low occupancy scale, the threshold value could be set lower, e.g., 0.6.

There are two main problems: (1) how to identify busy members and free members, in other words, how to quantify the busy degree for each member; and (2) how to connect the busy degree to the threshold values setting.

As to the <sup>fi</sup>rst problem, we use the occupancy scale to measure the busy degree of members. As to the second problem, we build a mapping table between the occupancy scale and a certain threshold value, in which the difference in members' experience (novices– experts) is taken into account. Those two problems are introduced in following subsections respectively.

## 6.2. Occupancy scale to measure members' busy degree

The <sup>fl</sup>owchart of determining the occupancy scale is illustrated in Fig. 5. The occupancy scale is obtained by analyzing the total busy time $( T _ { \mathrm { b u s y } } )$ and variance of the free time $\left( \delta _ { \mathrm { i d l e } } \right)$ of each member. The busy members, whose $T _ { \mathrm { b u s y } }$ is high, will have less time to browse the knowledge provided by recommender systems. In addition, if the free time is allocated at different periods, the member has less <sup>fl</sup>exibility to take advantage of the recommended knowledge. A mapping table $( T _ { \mathrm { b u s y } } \times \delta _ { \mathrm { i d l e } } )$ is established to obtain the occupancy scale of the speci<sup>fi</sup>ed member. Then, the suitable volume for knowledge recommendation could be determined for each member.

Firstly, two indices $( T _ { \mathrm { b u s y } }$ and $\delta _ { \mathrm { i d l e } } )$ are calculated as follows:

$$
T _ {\mathrm{busy}} = \sum_ {i = 1} ^ {N} B _ {i} = \sum_ {i = 1} ^ {N} (B E _ {i} - B S _ {i})\tag{11}
$$

$$
\delta_ {\text {idle}} = \frac {\sum_ {j = 1} ^ {N - 1} (F I _ {j} - \operatorname{Avg} (F I)) ^ {2}}{(N - 1) - 1} = \frac {\sum_ {j = 1} ^ {N - 1} (F I _ {j} - \operatorname{Avg} (F I)) ^ {2}}{N - 2}\tag{12}
$$

$$
\operatorname{Avg} (F I) = \frac {\sum_ {j = 1} ^ {N - 1} F I _ {j}}{N - 1}\tag{13}
$$

where $B _ { i }$ denotes the ith busy time, $B S _ { i }$ and BE denote the starting and ending time of the ith busy period. $F I _ { j }$ denotes free time interval between the jth and j+1th busy period. If there are N busy time periods, there are $N - 1$ free time periods. So i is from 1 to N, while j is from 1 to $N - 1$

Assume that the total busy time and variance of free time of all members follow the normal distribution, that is $T _ { \mathrm { b u s y } } { \sim } N ( \mu _ { 1 } , \delta _ { 1 } ^ { 2 } )$ and $\delta _ { \mathrm { i d l e } } { \sim } N ( \mu _ { 2 } , \delta _ { 2 } ^ { 2 } )$ . In order to classify the members into categories based on their workload, the lower and upper bounds of each category should be derived. Based on total busy time, members could be categorized into k categories with equal probabilities and the boundary BounT can be determined by:

$$
P \left(\frac {B o u n T _ {i} - \mu_ {1}}{\sigma_ {1}} \leq Z\right) = \frac {i}{k} \times 100\%, i = 1,2,...,k - 1.\tag{14}
$$

The target member could be assigned with a corresponding category based on the total busy time $T _ { \mathrm { b u s y } }$ and the category boundary BoundT .

![](/api/attachments/NTKSMBYD/fulltext/images/392aa698d7a3c2b32da1a5811efe68a6b55cc1b4cf53e2e956a1df57dc48520d.jpg)  
Fig. 5. Statistical analysis of occupancy scale from schedules in work<sup>fl</sup>ow.

Similarly, based on the variance of free time, the members can be categorized into h categories with equal probabilities and the boundary Bounδ can be determined by:

$$
P \left(\frac {B o u n \delta_ {j} - \mu_ {2}}{\sigma_ {2}} \leq Z\right) = \frac {j}{h} \times 100\%, j = 1, 2,..., h - 1.\tag{15}
$$

The target member could be assigned with a corresponding category based on the variance of free time $\delta _ { \mathrm { i d l e } }$ and the category boundary Bounδ<sub>j</sub>.

After determining the above boundaries, a mapping table for member category (or occupancy scale) can be established (as shown in Fig. 5). Members with category $\mathrm { C _ { 1 , k } }$ are regarded as busiest ones, so only the knowledge resources that have the highest correlation with them will be recommended. On the contrary, the members with category $\mathrm { C } _ { \mathrm { h , 1 } }$ have more free time to browse the recommended knowledge. In all, based on statistic analysis on members' busy time and free time variance, their occupancy scales could be determined. According to the member's occupancy scale, recommender systems can intelligently provide appropriate volume of knowledge to him (or her) so as to avoid information overload.

## 6.3. Mapping occupancy scale to threshold

We de<sup>fi</sup>ne a mapping table between occupancy scales and threshold values. For example, the busiest occupancy scale $\left( { \mathsf { C } } _ { 1 , \mathrm { k } } \right)$ maps threshold value 0.95; the freest occupancy scale $\left( { \mathsf { C } } _ { \mathrm { h } , 1 } \right)$ maps threshold value 0.15. In this mapping table, the speci<sup>fi</sup>c threshold values could be determined by knowledge engineers or experts in advance.

As to the issue of determining suitable volume of recommended knowledge, it should also take different experience levels of members (e.g., expert or novice) into account. For some experts, although they are not busy, they don't really need a lot of knowledge documents recommended from the knowledge repository. As to some novices, they may be busy, but they still need more related knowledge documents for browsing and learning. Therefore, it is not rational to use uniform mapping table for both experts and novices. We should take account of the different experience levels of team members (expert or novice) in building the mapping table. More speci<sup>fi</sup>cally, the threshold values in the mapping table should be adjusted according to members' experience levels, which could be measured by their working years. For experts, a higher factor (α) could be multiplied with previous threshold; while for novices, a lower factor would be used. For example, two members $( \mathbf { m } _ { 1 } , \mathbf { m } _ { 2 } )$ , 1 is with 10years working experiences $( \mathrm { y e a r } ( m _ { 1 } ) = 1 0 )$ , the other is just 1year $( \mathrm { y e a r } ( m _ { 2 } ) = 1 )$ . Their occupancy scales are both $\mathsf { C } _ { 3 , 2 } ,$ which is corresponding to a threshold value 0.8. The <sup>fi</sup>nal threshold values for the above two members are different, the expert may be 0.72 $( 0 . 8 \times \alpha ( m _ { 1 } ) , \alpha ( m _ { 1 } ) = 0 . 9 )$ , while the novice may be 0.56 $( 0 . 8 \times \mathbf { \alpha } \alpha ( m _ { 2 } )$ $\alpha ( m _ { 2 } ) = 0 . 7 )$ . Different years of working experience, year(m), have different factors α(m).

We could employ many possible functions to map year(m) to α(m). In this paper, it is de<sup>fi</sup>ned as follows:

$$
\alpha (m) = \frac {2}{\pi} \arctan (\text { year } (m) / \text { hl }).\tag{16}
$$

Here, year(m) is the year difference between the current year and the year the member took up the task or role. It is assumed that a member with hl years experience will have a middle factor (0.5). If the length of working period is long enough, the factor will approach 1.0 gradually.

## 7. Experimental evaluations

## 7.1. Experiment design

The experiments are set in the environment of a manufacturing enterprise. Three types of collaborative teams are involved in experiments:

(1) R&D collaborative team: 30 engineers from the research and design department form a collaborative team, which mainly do some research for new product development.

(2) Manufacturing control team: 30 engineers from the manufacturing department form a collaborative team, which mainly manage and control the manufacturing process.

(3) Routine of<sup>fi</sup>ce team: 30 clerks from the administration department form a collaborative team, which mainly do some routine documents handling work.

Our experiments used the data records from the above departments. The data sets record 90 participants' knowledge querying and browsing tracks from the knowledge repository in 80 days. Every participant queried and browsed a lot of knowledge documents each day, and those knowledge documents belong to various domains or categories. For each day, a frequency statistic about each domain could be obtained. Thus, for every participant, we could have 80 such domain frequency statistic tables, which are aggregated with weights. The nearer is the date, the higher is the weight. Then, we could obtain one <sup>fi</sup>nal ‘Member-Domain’ rating table from the above process. That would form the basis for further collaborative <sup>fi</sup>ltering (CF).

Based on the above source dataset, we could generate new ‘Member-Domain’ rating table by using the CF based on work<sup>fl</sup>ow. As to a certain member, some knowledge documents with higher rating domains could be recommended to him (or her) from the knowledge repository in the company. As to the suitable volume of the recommendation, it is determined by the member's time occupancy scale, which is obtained according to the member's schedule information in work<sup>fl</sup>ow.

For the benchmark (or ground truth) ranking data, we asked each engineer in the team to rank and sort the items of knowledge categories in a prede<sup>fi</sup>ned list, which is based on the company's industrial domains. This benchmark data re<sup>fl</sup>ects the members' interests and requirements for the categories of knowledge. With comparison between recommendation results and the benchmark data, the precision values could be obtained for all participants. The average of results is calculated as the <sup>fi</sup>nal evaluation metrics to the recommender system.

In this paper, our experiments mainly address following six issues:

(1) We analyze the recommendation precisions with T changing. The parameter T denotes the length of interval involved in calculation.

(2) We make the comparison between the work<sup>fl</sup>ow-based CF and ordinary CF (without consideration of work<sup>fl</sup>ow).

(3) We study the precisions under different RSC coef<sup>fi</sup>cient parameter settings. The RSC coef<sup>fi</sup>cients denote the weights for different relationships among tasks in work<sup>fl</sup>ow.

(4) We compare the recommender system's performances among three different collaborative teams: R&D, manufacturing control, and routine of<sup>fi</sup>ce teams.

(5) We take into account the differences in members' experience (expert or novice) when using occupancy scale to determine suitable recommendation volume. We test the method's effects on <sup>fi</sup>nal performance.

(6) We study the precisions with hl changing. Parameter hl is key to determining impact degree from experts to novices.

## 7.2. Results and analysis

7.2.1. Experiment 1: Different CF modes, with T changing (as to the above issues (1) and (2))

In the <sup>fi</sup>rst experiment, we compare the performances of different CF modes: (1) CF based on work<sup>fl</sup>ow with considering relationships among tasks (Section 5.2, 5.3), (2) CF based on the same task in work<sup>fl</sup>ow (Sections 5.1), and (3) Ordinary CF.

Fig. 6 shows the precisions of above three CF modes with T changing. Parameter T denotes the length of interval used in calculation. Because the length of the source data sets is 80, T could be an integer from 1 to 80. If T is too small, the results vary in wide extent, and lack meanings for supporting the proposed methods. So T is assigned from 20 to 80 in this experiment. From Fig. 6, we could see that the precisions increase with T grows and hold at a steady value with T over 60.

The results of different collaborative filtering modes as T varies (R&D Team)  
![](/api/attachments/NTKSMBYD/fulltext/images/2368e1f547861c76066957754c13de56d990c1dde738900d3a10dea01df6ed3d.jpg)  
Fig. 6. The performances of different CF modes

The CF based on work<sup>fl</sup>ow, proposed in this paper, contains two ways: one is only based on the same task (introduced in Section 5.1), while the other takes into account the relationships among tasks (introduced in Section 5.2, 5.3). Fig. 6 shows three curves: one is about the situation only considering the same tasks (denoted by ‘in Same Task’ in Fig. 6); one is considering relationships among tasks (denoted by ‘with RSC’ in Fig. 6); and one is using the ordinary CF. From this experiment, we could see the proposed CF based on work<sup>fl</sup>ow outperforms the ordinary CF, especially the one considering relationships among tasks. Those results re<sup>fl</sup>ect that the collaborative environment could supply more information about the implicative relationships among members so as to improve the CF ef<sup>fi</sup>ciency.

7.2.2. Experiment 2: Different RSCs settings, with T changing (as to the above issue (3))

Considering the relationships among tasks will improve the CF's performances for collaborative environments. The assignment of RSC's values is essential in the above steps. The parameters RSCs (Relationship Similarity Coef<sup>fi</sup>cient) denote the weights for different relationships among tasks in work<sup>fl</sup>ow. We perform the experiments to <sup>fi</sup>nd out which sets of RSCs are proper. Fig. 7 shows three groups of experiments. The assignments of RSC's values are listed as follows.

$$
\text { RSC   1:   } \mathrm{RSC} (\text { seq }) = 0. 9, \mathrm{RSC} (\text { par }) = 0. 5, \mathrm{RSC} (\text { sub }) = 0. 7;
$$

$$
\text { RSC   2: } \mathrm{RSC} (\text { seq }) = 0. 7, \mathrm{RSC} (\text { par }) = 0. 5, \mathrm{RSC} (\text { sub }) = 0. 9;
$$

$$
\text { RSC   3: } \mathrm{RSC} (\text { seq }) = 0. 7, \mathrm{RSC} (\text { par }) = 0. 9, \mathrm{RSC} (\text { sub }) = 0. 5;
$$

From the results shown in Fig. 7, we could see that the three curves are close to each other, which means the changes of the assignment of RSC do not have signi<sup>fi</sup>cant in<sup>fl</sup>uence on the <sup>fi</sup>nal results. However, the curve of RSC1 is better than RSC2 and RSC3. The results re<sup>fl</sup>ect that the RSC(seq) should be set higher, while RSC(par) should be set lower. It means the ‘sequential’ relationship has higher in<sup>fl</sup>uence on corresponding members than ‘subtype’ and ‘part of’ relationships.

The results of different collaborative filtering modes as T varies (R&D Team)  
![](/api/attachments/NTKSMBYD/fulltext/images/7549d09561dbdb9d676915d2a93d7b5841869b2cdf3760639ac6385363fe7358.jpg)  
Fig. 7. The performances of work<sup>fl</sup>ow-based CF under different RSCs' settings.

7.2.3. Experiment 3: Different collaborative teams, with T changing (as to the above issue (4))

In order to examine the proposed methods' performances under different collaborative environments, we conduct experiments for three types of collaborative teams: (1) R&D collaborative team: 30 engineers from the research and design department form a collaborative team, which mainly do some research for new product development; (2) Manufacturing control team: 30 engineers from the manufacturing department form a collaborative team, which mainly manage and control the manufacturing process; and (3) Routine office team: 30 clerks from the administration department form a collaborative team, which mainly do some routine documents handling work.

Fig. 8 shows the results under the above three different collaborative environments. We could see that the work<sup>fl</sup>ow-based CF has evident effects on R&D team, Manufacturing control team; while on the routine of<sup>fi</sup>ce team, the work<sup>fl</sup>ow-based method seems not effective. The reasons may lie in that the collaborative characteristics of routine of<sup>fi</sup>ce team are not as distinct as two other teams. The R&D team deals with high level knowledge intensive work, so it contains much stronger collaborative relationships among members. Therefore, the effect of work<sup>fl</sup>ow-based CF is much more evident than two other teams. This experiment shows that the proposed work<sup>fl</sup>owbased CF may be much more suitable to those teams or organizations with more potential and implicative collaborations among members.

7.2.4. Experiment 4: Considering difference between expert and novice (as to the above issues (5) and (6))

The last experiment takes into account the differences in members' experience (expert or novice). We perform the experiment by using occupancy scale to determine suitable recommendation volume, and study hl's impact on precision. Here, the hl, abbreviated from ‘half-life span’, is a parameter to determine impact degree from experts to novices, and it means that a member with hl years experience will have a half in<sup>fl</sup>uence of expert who may have the highest in<sup>fl</sup>uence value.

Fig. 9 shows recommendation precisions under two cases: (a) one is to consider expert–novice differences in calculating occupancy scale so as to determine suitable recommendation volume; (b) the other is to ignore the expert–novice differences. From Fig. 9, we could <sup>fi</sup>nd that the former one performs better than the latter one except some peak points. When determining the suitable volume of recommendation, different strategies are adoptive for improving the recommender's performance under different environments.

As to the trends of precision with hl changing, we could see that the precision increases when hl is below <sup>fi</sup>ve, and decreases when hl exceeds <sup>fi</sup>ve. Thus the ‘half-life span’ hl should be set as <sup>fi</sup>ve for that collaborative team. Here, ‘hl=5’ means that a member $( { \mathrm { e } } . { \mathrm { g } } . , M _ { E } )$ with 5years working experience will have a middle factor (0.5) according to formula (16) in previous Section 6.3, and a member $( \mathbf { e } . \mathbf { g } . , M _ { N } )$ with only 2years working experience has a factor (0.24). If the two members (M and $M _ { N } )$ have the same busy level (occupancy scale value) that maps to a threshold value (e.g., 0.8) in recommendation volume control, the <sup>fi</sup>nal threshold value for the $M _ { E }$ is actually 0.4 (0.5×0.8) and $M _ { N }$ is 0.2 $( 0 . 2 4 \times 0 . 8 )$ . That is the working experiences' impact on the recommendation volume control for different members.

The results of different collaborative teams as T varies  
![](/api/attachments/NTKSMBYD/fulltext/images/c97297dc75a3fdd848c42b49a1fd8bdec754d584b9b3bfefd60b38e55c83d077.jpg)  
Fig. 8. The performances of the work<sup>fl</sup>ow-based CF in different collaborative teams.

![](/api/attachments/NTKSMBYD/fulltext/images/fdf96b68177674e5ff28790cb1f1ace408637b8d0d55bf76cc86fbfe0d7d16d2.jpg)  
Fig. 9. The performances with considering members' differences (expert–novice).

## 8. Summary

This paper introduces a work<sup>fl</sup>ow-based recommender system model for collaborative team environment. Two work<sup>fl</sup>ow-centric approaches for mining team members' knowledge demands and determining proper recommendation volume are proposed. This study paves the way for implementing a platform which would ensure that a proper volume of proper knowledge resources could be recommended to the proper members among the collaborative team.

However, there exist some limitations for the current model and methods, which need further studies in future:

(1) The proposed methods consider expert–novice in<sup>fl</sup>uence on members' demands for knowledge. However, the current study has not mentioned how ‘expert’ a new member is viewed. In Section 4.3, the manner in which hl is used has not taken into account how much expertise an individual brings into the collaborative team. This is actually a new user cold starting problem. In future studies, the agency theory could be applied to how knowledge workers address their knowledge needs. In this way, it may improve on or replace the current methods of using hl.

(2) In experiments, we are not able to use all possible combinations of parameters. Currently, those settings are determined according to experience. As to different collaborative teams, the ‘optimal’ settings are actually different from each other. There is no universal setting that could adapt to all contexts with the best performance. The sensitivity analysis of those parameter settings for different application environments should be conducted in future studies.

## References

[1] G. Adomavicius, R. Sankaranarayanan, S. Sen, A. Tuzhilin, Incorporating contextual information in recommender systems using a multidimensional approach, ACM Transactions on Information Systems 23 (2005) 103–145

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state of the art and possible extensions, IEEE Transactions on Knowledge & Data Engineering 17 (2005) 734–749

[3] K.D. Bollacker, S. Lawrence, C.L. Giles, Discovering relevant scienti<sup>fi</sup>c literature on the Web IEEE Intelligent Systems 15 (2) (2000) 42–47

[4] R. Gar<sup>fi</sup>nkel, R. Gopal, A. Tripathi, F. Yin, Design of a shopbot and recommender system for bundle purchases, Decision Support Systems 42 (3) (2006) 1974–1986

[5] R. Gar<sup>fi</sup>nkel, R. Gopal, B. Pathak, F. Yin, Shopbot 2.0: integrating recommendations and promotions with comparison shopping, Decision Support Systems 46 (1) (2008) 61–69.

[6] D. Godoy, A. Amandi, Modeling user interests by conceptual clustering, Information Systems 31 (4-5)(2006) 247–265

[7] D. Goldberg, D. Nichols, B.M. Oki, D. Terry, Using collaborative <sup>fi</sup>ltering to weave an information tapestry, Communications of the ACM 35 (1992) 12–13.

[8] P. Han, B. Xie, F. Yang, R. Shen, A scalable P2P recommender system based on distributed collaborative <sup>fi</sup>ltering, Expert Systems with Applications 27 (2004) 203–210.

[9] Y.C. Jiang, J. Shang, and Y.Z. Liu, Maximizing customer satisfaction through an online recommendation system: A novel associative classi<sup>fi</sup>cation model, Decision Support Systems, (2009) In Press, doi:10.1016/j.dss.2009.06.006.

[10] J.J. Jung, Knowledge distribution via shared context between blog-based knowledge management systems: a case study of collaborative tagging, Expert Systems with Applications 36 (7) (2009) 10627–10633

[11] M. Kagie, M. van Wezel, P.J.F. Groenen, A graphical shopping interface based on product attributes, Decision Support Systems 46 (1) (2008) 265–276.

[12] J.K. Kim, H.K. Kim, Y.H. Cho, A user-oriented contents recommendation system un peer-to-peer architecture, Expert Systems with Applications 34 (1) (2008) 300–312.

[13] J. Konstan, B. Miller, D. Maltz, J. Herlocker, L. Gordon, J. Riedl, GroupLens: applying collaborative <sup>fi</sup>ltering to usenet news, Communications of the ACM 40 (3) (1997) 77–87.

[14] Y. Li, N. Zhong, Web mining model and its applications for information gathering Knowledge-Based Systems 17 (2004) 207–217.

[15] Y. Li, N. Zhong, Mining ontology for automatically acquiring web user information needs, IEEE Transactions on Knowledge and Data Engineering 18 (2006) 554–568.

[16] T.P. Liang, Y.F. Yang, D.N. Chen, Y.C. Ku, A semantic-expansion approach to personalized knowledge recommendation, Decision Support Systems 45 (3) (2008) 401–412.

[17] D.R. Liu, I.C. Wu, Collaborative relevance assessment for task-based knowledge support, Decision Support Systems 44 (2) (2008) 524–543.

[18] J. Malinowski, T. Weitzel, T. Keim, Decision support for team staf<sup>fi</sup>ng: an automated relational recommendation approach, Decision Support Systems 45 (3) (2008) 429–447.

[19] S.M. McNee, I. Albert, D. Cosley, P. Gopalkrishnan, S.K. Lam, A.M. Rashid, On the recommending of citations for research papers, Proceedings of CSCW 2002 New Orleans, USA, 2002, pp. 116–125.

[20] S. E. Middleton, Capturing Knowledge of User Preferences with Recommender Systems, Doctoral thesis, Univ. Southampton, (2003).

[21] S.E. Middleton, N.R. Shadbolt, D.C. De Roure, Ontological user pro<sup>fi</sup>ling in recommender systems, ACM Transactions on Information Systems 22 (1) (2004) 54–88.

[22] B. Mobasher, R. Cooley, J. Srivastava, Automatic personalization based on web usage mining, Communications of the ACM 43 (8) (2000) 142–151.

[23] R.J. Mooney, L. Roy, Content-based book recommending using learning for text categorization, In Proceedings of the ACM international conference on digital libraries, San Antonia, Texas, USA, 2000 195–204.

[24] T. Olsson, Bootstrapping and decentralizing recommender system. Ph.D. Thesis Dept, of Information Technology Uppsala Uniy. 2003.

[25] J. Rucker, M.J. Polanco, Siteseer: personalized navigation for the web, Communications of the ACM 40 (3) (1997) 73–75.

[26] J.B. Schafer, J. Konstan, J. Riedl, Recommender systems in e-commerce, Proceedings of 1st ACM conference on electronic commerce, Denver, Colorado, USA, 1999, pp. 158–166.

[27] A. Smirnov, M. Pashkin, N. Chilov, T. Levashova, Knowledge logistics in information grid environment Future Generation Computer Systems 20 (2004) 61–79.

[28] Y.W. Wang, W.H. Dai, Y.F. Yuan, Website browsing aid: a navigation graph-based recommendation system. Decision Support Systems 45 (3)(2008) 387-400.

[29] B.C. Yeong, H.C. Yoon, H.K. Soung, Mining changes in customer buying behavior for collaborative recommendations, Expert Systems with Applications 28 (2005) 359–369.

[30] S.K. Yong, B.J. Yum, J. Song, M.K. Su, Development of a recommender system based on navigational and behavioral patterns of customers in e-commerce sites, Expert Systems with Applications 28 (2005) 381–393.

[31] L. Yu, L. Liu, X. Li, A hybrid collaborative <sup>fi</sup>ltering method for multiple-interests and multiple-content recommendation in e-commerce, Expert Systems with Applications 28 (2005) 67–77.

[32] L. Zhen, Z. Jiang, Knowledge grid based knowledge supply model, IEICE Transactions on Information and Systems E91-D(4 (2008) 1082–1090.

[33] L. Zhen, Z. Jiang, Innovation-oriented knowledge query in knowledge grid, Journal of Information Science and Engineering 24 (2) (2008) 601–613.

[34] L. Zhen, Z. Jiang, H. Song, C. Liu, J. Liang, Information supply: an approach based on demand modeling and information <sup>fi</sup>ltering, Proc.IMechE Part B: Journal of Engineering Manufacture 222 (4) (2008) 541–557.

[35] L. Zhen, G.Q. Huang, Z. Jiang, Collaborative <sup>fi</sup>ltering based on work<sup>fl</sup>ow space, Expert Systems with Applications 36 (4) (2009) 7873–7881.

[36] L. Zhen, G.Q. Huang, and Z. Jiang, An inner-enterprise knowledge recommender system, Expert Systems with Applications, (2009) In Press, doi:10.1016/j.eswa. 2009.06.057.

[37] H. Zhuge, Knowledge <sup>fl</sup>ow management for distributed team software development, Knowledge Based Systems 15 (8) (2002) 465–471.

[38] H. Zhuge, A knowledge <sup>fl</sup>ow model for peer-to-peer team knowledge sharing and management, Expert systems with applications 23 (1) (2002) 23–30.

Lu Zhen received the B.E. and Ph.D. degrees in industrial engineering from Shanghai Jiao Tong University (P.R. China). He is currently a postdoctoral research fellow at the department of industrial and system engineering, National University of Singapore. His current research interests include: knowledge management, information systems, and operation researches. He has published 8 papers (the <sup>fi</sup>rst author) in referred international journals; another 8 papers (the <sup>fi</sup>rst author) have been published in some international conference proceedings and domestic journals.

George Q. Huang is a Professor at the department of industrial and manufacturing system engineering, the University of Hong Kong. He received the Ph.D. degree in mechanical engineering from Cardiff University, Cardiff, U.K., His main research interests include: collaborative product development, mass customization, supply chain management. He has published extensively in these topics, including over 200 technical papers, half of which have appeared in refereed journals, two monographs and an edited reference book. Prof. Huang received Outstanding Young Researcher Award from The University of Hong Kong (2001) and Overseas Outstanding Young Scholar from Natural Science Foundation of China (2007).

Zuhua Jiang is a Professor at the department of industrial engineering and management, Shanghai Jiao Tong University, P.R. China. He received the Ph.D. degree in mechanical engineering from Shanghai Jiao Tong University, P.R. China. His current research interests include: knowledge management, cooperative design, concurrent engineering. He has published 40 papers in referred international conferences and journals.
