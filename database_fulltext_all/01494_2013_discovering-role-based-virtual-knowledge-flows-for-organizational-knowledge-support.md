---
otero_id: 1494
otero_key: "J5Y6DZAF"
title: "Discovering role-based virtual knowledge flows for organizational knowledge support"
authors: "Duen-Ren Liu; Chih-Wei Lin; Hui-Fang Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.018"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support

Duen-Ren Liu ⁎, Chih-Wei Lin, Hui-Fang Chen

Institute of Information Management, National Chiao Tung University, No. 1001 Ta Hsueh Rd., Hsinchu 300, Taiwan

a r t i c l e i n f o

Article history: Received 20 May 2011 Received in revised form 24 October 2012 Accepted 4 November 2012 Available online xxxx

Keywords: Knowledge <sup>fl</sup>ow Knowledge <sup>fl</sup>ow view Knowledge support Knowledge management Role Ontology

## a b s t r a c t

In knowledge-intensive work environments, workers need task-relevant knowledge and documents to support the execution of tasks. A knowledge <sup>fl</sup>ow (KF) represents an individual's or group's knowledge-needs and referencing behavior of codi<sup>fi</sup>ed knowledge during the performance of organizational tasks. Through knowledge <sup>fl</sup>ows, organizations can provide workers with task-relevant knowledge to satisfy their knowledge-needs. In teamwork environments, knowledge workers with different roles and task functions usually have diverse knowledge-needs, but conventional KF models cannot satisfy such needs. In a previous work, we proposed a novel concept and theoretical model called Knowledge Flow View (KFV). Based on workers' diverse knowledge-needs, the KFV model abstracts knowledge nodes of partial KFs and generates virtual knowledge nodes through a knowledge concept generalization procedure. However, the KFV model did not consider the diverse knowledge-needs of workers who play different roles in a team. Therefore, in this work, we propose a role-based KFV model that discovers role-based virtual knowledge <sup>fl</sup>ows to satisfy the knowledge-needs of different roles. First, we analyze the level of knowledge required by workers to ful<sup>fi</sup>ll various roles. Then, we develop role-based knowledge <sup>fl</sup>ow abstraction methods that generate appropriate virtual knowledge nodes to provide suf<sup>fi</sup>cient knowledge for each role. The proposed role-based KFV model enhances the ef<sup>fi</sup>ciency of KF usage, as well as the effectiveness of knowledge sharing and knowledge support in organizations.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In knowledge-intensive work environments, workers need taskrelevant knowledge and documents to support their execution of tasks. Thus, how to effectively ful<sup>fi</sup>ll workers' knowledge-needs by preserving, sharing and reusing task-relevant knowledge is an important issue in realizing knowledge management and promoting business intelligence. Organizations can provide task-relevant knowledge through knowledge <sup>fl</sup>ows (KF), which represent the <sup>fl</sup>ow of an individual's or group's knowledge-needs and referencing behavior of codi<sup>fi</sup>ed knowledge during the performance of organizational tasks [16].

In recent years, a considerable number of studies have focused on KF models and applications in business and scienti<sup>fi</sup>c research contexts. One major area of research focuses on knowledge sharing among knowledge workers. For example, researchers cite prior research and propose new ideas through publishing papers, thereby creating KFs in the realm of science [46]; and in the business domain, KFs facilitate knowledge sharing during the execution of tasks [45]. KFs can be discovered by analyzing workers' knowledge-needs, after which appropriate codi<sup>fi</sup>ed knowledge can be recommended to workers based on the KFs [16,20]. When a task involves teamwork, knowledge workers have different roles and task functions, so they usually have diverse knowledge-needs. However, conventional KF models do not provide different perspectives of a KF to ful<sup>fi</sup>ll team members' diverse needs. Although several KF models have been proposed, they do not consider the concept of virtual knowledge <sup>fl</sup>ows, which provide abstracted knowledge. In a previous work [21], we proposed an approach called the knowledge <sup>fl</sup>ow view (KFV) model, which constructs virtual knowledge <sup>fl</sup>ows to serve workers' knowledge-needs. A virtual knowledge <sup>fl</sup>ow (VKF) is derived from a KF and provides abstracted knowledge. Given the knowledge-needs of different workers, the model abstracts some knowledge nodes of a KF to generate several virtual knowledge nodes by an order-preserving approach and a knowledge concept generalization procedure.

In the KFV model, we investigated VKFs and developed algorithms to generate such <sup>fl</sup>ows, but we did not consider workers' knowledge-needs in terms of the different roles they play in an organization. If a task involves teamwork, workers' knowledge-needs will vary, depending on the roles they play. To ensure effective cooperation, each worker not only needs a speci<sup>fi</sup>c level of knowledge to perform his/her individual task, but will also need a general level of knowledge about the other workers' tasks. For example, in a computer manufacturing company, engineers are responsible for product development and marketing people design strategies to launch and promote new products. In this scenario, engineers need a speci<sup>fi</sup>c level of technical knowledge, but marketing people need only a general level of such technical knowledge to assist them in communicating with the engineers. Thus, the KFV model is required to include the aspect of roles in order to apply knowledge management applications in teams [15]. Since workers' knowledge requirements may vary, it is essential that organizations provide rolebased VKFs to ensure effective cooperation and knowledge sharing. The concept of role-based VKFs has not been addressed in previous studies on KFV models. Therefore, in an attempt to <sup>fi</sup>ll this research gap, we propose a role-based KFV model to ful<sup>fi</sup>ll workers' knowledge-needs. The model analyzes the levels of knowledge required by workers based on their roles, and develops role-based knowledge <sup>fl</sup>ow abstraction methods that generate virtual knowledge nodes to provide the appropriate level of knowledge for each role.

This work is targeted as a theoretical paper to establish the rolebased KFV model and extend knowledge <sup>fl</sup>ow research to cooperative teams for organizational knowledge support. To the best of our knowledge, the proposed role-based KFV model is one of the pioneering theoretical studies to illustrate a comprehensive formal representation of VKFs from the perspectives of roles and operations. This work introduces three innovative concepts: (1) identifying VKFs in role and operation perspectives, (2) integrating an approach for evaluating roleknowledge node relevance and an order-preserving algorithm to derive VKFs, and (3) applying role-operation knowledge requirements to facilitate knowledge concept abstraction. From the perspective of cooperation and knowledge sharing, our research facilitates collaboration in an organization. The proposed role-based KFV model can enhance the theoretical scope of KF research. In addition, our work improves the ef<sup>fi</sup>ciency of KFs, as well as the effectiveness of knowledge sharing and knowledge support in organizations.

The remainder of this paper is organized as follows. The next section contains a review of related work. Then, we illustrate the foundation of the KFV model in Section 3 and discuss the important concepts of the role-based KFV model in Section 4. Methods of generating role-based VKFs are introduced in Section 5. Next, we conduct a basic system design and present a case study in Sections 6 and 7, respectively. Finally, we summarize our conclusions and indicate possible directions for future research in Section 8.

## 2. Related work

In this section. we discuss the research background and related work on knowledge management, knowledge <sup>fl</sup>ow, ontology and process-view abstraction.

## 2.1. Knowledge management and knowledge support

Knowledge is one of the key assets that organizations use to maintain a competitive advantage [31]; and knowledge management provides the principles of creation, organization, transfer and application of knowledge within enterprises [40]. Generally, knowledge is classi-<sup>fi</sup>ed as tacit or explicit knowledge, and information technology (IT) is regarded as a natural medium for managing knowledge [4]. Organizations usually use community-based electronic discussion platforms to transfer tacit knowledge from individuals to a knowledge repository [8]. In task-based business environments, knowledge management systems (KMS) facilitate the preservation, reuse and sharing of knowledge, and also support collaboration among workers. For example, based on the speci<sup>fi</sup>cations and process-context of a task, the KnowMore system [1] provides context-aware knowledge retrieval and delivery to support workers' procedural activities. Holz et al. [13] proposed a similarity-based approach that organizes desktop documents and proactively delivers task-speci<sup>fi</sup>c information to users. The task-based K-support system [24,25,39] provides knowledge to adaptively meet a worker's dynamic information needs by analyzing his/her access behavior or relevance feedback on documents. Furthermore, because of the nature of teamwork, a collaborative mechanism is essential for establishing KMS [2,43].

## 2.2. Knowledge flow

Knowledge <sup>fl</sup>ow (KF) research focuses on how KFs transmit, share and accumulate knowledge in a team. In a work<sup>fl</sup>ow situation, work knowledge may <sup>fl</sup>ow among workers, while process knowledge may <sup>fl</sup>ow among various tasks [45,47,48]. Thus, the KF re<sup>fl</sup>ects the level of knowledge cooperation between workers or processes, and in<sup>fl</sup>uences the effectiveness of teamwork or work<sup>fl</sup>ow. The KF in a software development team can gather knowledge from one team member and carry it to another member, and thereby facilitate knowledge sharing [45]. To improve the ef<sup>fi</sup>ciency of teamwork, Zhuge [47] proposed a pattern-based approach which combines codi<sup>fi</sup>cation and personalization strategies to design an effective knowledge <sup>fl</sup>ow network. To enable the automation of KFs, Sarnikar and Zhao [32,33] developed a framework of knowledge work<sup>fl</sup>ow to automate KFs by integrating work<sup>fl</sup>ow and knowledge discovery techniques. Rodriguez et al. [30] posited that KFs in communities of practice help members to share their knowledge and experience about a speci<sup>fi</sup>c domain, in order to complete their tasks. KFs can also facilitate knowledge sharing and reuse in research environments. Speci<sup>fi</sup>cally, a citation network can be seen as a KF that disseminates knowledge among researchers. Citing a scienti<sup>fi</sup>c article implies the occurrence of a KF between the authors of the article and the person citing it.

In recent years, several KF models have been proposed. Luo et al. [26] designed a Textual Knowledge Flow (TKF) model for a semantic link network. TKF can recommend appropriate browsing paths to users after evaluating their interests and inputs. KFs can also represent the sequence of knowledge-needs and/or knowledge reference patterns when workers perform tasks. Lai and Liu [16] constructed a time-ordered KF model to determine the sequence of workers' knowledge referencing behavior. Workers can obtain knowledge to satisfy their needs through the KFs discovered from document access logs. Moreover, the referencing sequence in weblogs can be regarded as a KF, and described as a sender-message-receiver model, since a blogger's weblog post may include a hyperlink to a weblog post of another blogger [3]. Kim et al. [14] proposed a KF model that utilizes a process-oriented approach to capture, store and transfer knowledge. Zhang et al. [41] used Petri-net to model a KF. Speci<sup>fi</sup>cally, a knowledge node can generate, learn, operate, understand, synthesize and deliver knowledge based on four types of <sup>fl</sup>ow relations: creation, merging, replication and broadcasting. Zhao et al. [42] introduced a method that integrates business processes and KFs by dividing KFs into sequence, distribution, combination and self-re<sup>fl</sup>ection, based on a Role-Activity-Diagram model.

## 2.3. Ontology

Ontology illustrates how people view the world. It represents the objects and their inter-relationships in a speci<sup>fi</sup>c domain. More precisely, it is a conceptualization mechanism that de<sup>fi</sup>nes the concepts of objects explicitly and constructs a hierarchical structure of the objects' inter-relationships [11,28]. The mechanism has been applied in many domains. For example, the common terminologies and knowledge concepts in an ontology can improve the problem-solving capability and ef<sup>fi</sup>ciency of a supply chain [5]. Wikipedia articles and categories can also be used as an ontology to predict the concepts of documents [35]. In an organization, an ontology de<sup>fi</sup>nes the knowledge concepts that are understood throughout the organization, and provides a hierarchical structure to demonstrate the relationships among the concepts [29]. Building ontology is an evolving process and involves many techniques and tools to facilitate the whole process. Obviously, the construction process would include an evaluation and feedback mechanism to gradually improve ontology quality and obtain common understanding in organizations [18,28,36]. For example, Uschold and King [37] proposed a skeletal methodology to build an enterprise ontology; it comprises four phases: scoping, building, evaluating and documenting. Du, Li and King [9] designed a sixphase process that includes the preparation, transformation, clustering, recognition, re<sup>fi</sup>nement and revision for extracting ontology from unstructured HTML pages. Therefore, involving users in the evaluation or re<sup>fi</sup>nement phase is essential for gradually adjusting the quality. Many ontology-building tools, such as Protégé, OntoEdit and SNet-Builder, can effectively support the ontology construction process to serve prede<sup>fi</sup>ned purposes and meet users' requirements [6,27].

## 2.4. Process-view abstraction

Work<sup>fl</sup>ow Management Systems (WfMS) are effective process management tools that allow businesses to analyze, simulate, design, implement, control and monitor their overall business processes [10,17]. Processes describe the operation <sup>fl</sup>ows involved in performing business activities. In practice, participants involved in a work<sup>fl</sup>ow need a <sup>fl</sup>exible work<sup>fl</sup>ow model that is capable of providing appropriate process information [22]. Because of the increasing complexity of business processes and the variety of participants, it is bene<sup>fi</sup>cial to de<sup>fi</sup>ne virtual processes from different perspectives. Liu and Shen [22] presented a novel concept of process abstraction called process-view. It is a virtual process derived from a base process to provide abstracted process information. The process-view is generated by an order-preserving approach, which ensures that the original order of the activities in a base process is preserved. Under the process-view concept, a WfMS can provide various views of a process for different participants within an organization or cross organizations [23]. Shen and Liu [34] proposed a role-based approach to discover role-relevant process views for different work<sup>fl</sup>ow participants. They developed algorithms to generate such views automatically, based on the relevance degrees between roles and tasks.

## 3. Foundation of knowledge <sup>fl</sup>ow view model

A virtual knowledge <sup>fl</sup>ow (VKF) is an abstract form of a base knowledge <sup>fl</sup>ow (BKF). It reveals abstract knowledge by providing customized views of a KF to team members. In our previous work [21], a novel knowledge <sup>fl</sup>ow view (KFV) model was proposed to construct VKFs to serve workers' knowledge-needs. The following summarizes the concepts and de<sup>fi</sup>nitions of the KFV model. Please refer to [21] for detailed de<sup>fi</sup>nitions, semantics and examples.

## 3.1. Virtual knowledge flow: an abstract form of a base knowledge flow

A KF that may have multiple VKFs is referred to herein as a base knowledge <sup>fl</sup>ow (BKF). A VKF is generated from a BKF and is considered to be a view of the BKF. We take an example from a mobile phone company to explain how to identify a BKF.

Fig. 1 shows a business process of mobile phone development. To derive BKFs of the business process, KF designers may either consult domain experts or investigate workers' document access logs to identify participants' knowledge-needs. A collection of the knowledge-needs and the order of referencing sequences would be used to construct BKFs, which represent participants' knowledge-needs by knowledge concepts. These knowledge concepts are stored in base knowledge nodes (BKNs), respectively. Fig. 2 illustrates an example of the BKFs to explain the concepts of base knowledge <sup>fl</sup>ows. In this example, KF designers derive the BKF's knowledge dependencies from the process level dependencies because it is a more intuitive and easier way for team members to understand. Nevertheless, KF designers can apply different ways to set the knowledge dependencies from other perspectives. Generally speaking, the knowledge dependencies in a BKF indicate the referencing sequence of knowledge (information) in task performance which may occur in a distributed software development team [44], an academic research project [16] or a web exploration [3]. So, knowledge dependencies do not always relate to process level dependencies. In practice, KF designers are responsible for setting knowledge dependencies based on the characteristics of applications.

In the KFV model, we adopt an order-preserving approach and a knowledge concept generalization mechanism to generate VKFs based on task functions and organizational security rules. Hence, team members have their own VKFs to ful<sup>fi</sup>ll their knowledge-needs and assist them to obey security policy.

Suppose that the BKF in Fig. 3 is the corresponding BKF of a manufacturing process. Product managers need not know all of the knowledge concepts in detail, but they must have general manufacturing knowledge to understand yield trends and increase communication effectiveness with factory members. So, KF designers may design an appropriate VKF for the product managers as follows: base knowledge nodes $k _ { 1 }$ and $k _ { 2 }$ are abstracted to a virtual knowledge node $\nu k _ { 1 } ; k _ { 3 } , k _ { 4 } ,$ $k _ { 5 }$ and $k _ { 6 }$ are abstracted to vk . In addition, manufacturers have their own VKF to serve for their knowledge-needs. Consequently, team members have respective VKFs to represent their knowledge-needs in collaborative environments.

## 3.2. Basic definitions of the knowledge flow view model

BKFs and VKFs are formally de<sup>fi</sup>ned in the KFV model. A BKF consists of base knowledge nodes and dependencies. A BKN contains knowledge concepts to represent knowledge-needs, and a dependency is the order between two BKNs. Likewise, a VKF, an abstract form of a BKF, consists of virtual knowledge nodes (VKNs) and virtual dependencies. A VKN is formed by abstracting a set of BKNs. Besides, a VKN contains knowledge concepts derived from its member knowledge nodes' knowledge concepts. Those knowledge concepts can be identi-<sup>fi</sup>ed in organizational domain ontology. Fig. 4 shows the components of the KFV model. in which the basic definitions of BKF and VKF are presented accordingly.

## 3.2.1. Definition 1 (domain ontology, O)

Domain ontology is constructed to de<sup>fi</sup>ne the knowledge concepts and their hierarchical relationships in an organization. It is divided into different knowledge categories. We de<sup>fi</sup>ne the ontology as O= ${ < } C , H R { > }$ , where C is a set of knowledge concepts derived from a domain; and HR is a set of hierarchical relations that de<sup>fi</sup>ne the parent–child relationships between the knowledge concepts in C. HR is formally expressed as $H R = \{ h r \mid h r { } \in { \cal C } \times { \cal C } \}$ . Given two knowledge concepts: x and y, if x has a downward link to y (or y has an upward link to x) in the concept hierarchy, then x is a parent concept of y and y is a child concept of x. Two semantic relations, Generalization and Specialization, are used to describe the parent–child relations. The

![](/api/attachments/J5Y6DZAF/fulltext/images/8805bc2568344b479b4047496b57c14f2cd3bcee3595b811bb0aa3b23d77076a.jpg)  
Fig. 1. Business process of mobile phone development.

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/J5Y6DZAF/fulltext/images/ba587c59f714914444f737f3b0fef72eb33f6b527a79ef9b7f6f31836d5bd5bb.jpg)  
Fig. 2. A sample BKF of the mobile phone development process.

relation between a parent concept x and a child concept y is formally expressed as: Specialization(x)={y | y is a child concept of x} and Generalizatio $\iota ( y ) = \{ x \mid$ x is a parent concept of y}.

## 3.2.2. Definition 2 (concept level, CL)

A knowledge concept is mapped to the corresponding CL in the domain ontology. CL is de<sup>fi</sup>ned by letting the root of the domain ontology be level one. If a knowledge concept is at level l, then its child concepts are at level l+1. The CLs indicate the levels of knowledge concepts and represent their granularity; that is, the knowledge concepts with larger CLs (i.e., in the lower levels of domain ontology) are more speci<sup>fi</sup>c than those with smaller CLs (i.e., in the upper levels of domain ontology).

## 3.2.3. Definition 3 (knowledge concepts, KC)

Knowledge concepts represent the different types of knowledge in domain ontology. Some KCs are general and some are speci<sup>fi</sup>c. A knowledge concept's generality (or speci<sup>fi</sup>city) is determined by its CL.

## 3.2.4. Definition 4 (base knowledge node, BKN)

A BKN x is a 2-tuple bbid, BKC>, where bid is the label of x and BKC is a set of knowledge concepts. BKC of x are denoted by $B K C _ { x } = \{ c _ { 1 } , c _ { 2 } ,$ $c _ { 3 } , . . . , c _ { m } \}$ , where the knowledge concept $c _ { i }$ can be identi<sup>fi</sup>ed in domain ontology and is associated with a corresponding CL.

## 3.2.5. Definition 5 (base knowledge flow, BKF)

A BKF is a 2-tuple bBKNS, BD>, where BKNS is a non-empty set of BKNs. BD is a non-empty set of dependencies. The preceding node and succeeding node of a dependency are in BKNS.

## 3.2.6. Definition 6 (virtual knowledge node, VKN)

A VKN vx is a 4-tuple bvid, KNS, D, VKC>, where vid is the label of vx, KNS is a non-empty set of BKNs or previously de<sup>fi</sup>ned VKNs. D is a non-empty set of dependencies whose preceding and succeeding nodes are in KNS. The VKC, abstracted knowledge concept set, is a non-empty set of knowledge concepts de<sup>fi</sup>ned in domain ontology. The knowledge concepts of vx are denoted as $V K C _ { v x } = \{ v c _ { 1 }$ , vc<sub>2</sub>, vc<sub>3</sub>, …, $v c _ { q } \} .$ , where vc is abstracted from some knowledge concepts of vx's member knowledge nodes.

## 3.2.7. Definition 7 (virtual dependency, VD)

Given a based knowledge <sup>fl</sup>ow BKF=bBKNS, BD> and two virtual knowledge nodes vx and vy, a virtual dependency vdep(vx, vy) from vx to vy exists if dep (x, y) is in BD, where x is a member of vx and y is a member of vy. A virtual dependency is used to connect two virtual knowledge nodes vx and vy.

## 3.2.8. Definition 8 (virtual knowledge flow, VKF)

A virtual knowledge <sup>fl</sup>ow is a 2-tuple bVKNS, VDS>, where VKNS is a non-empty set of virtual knowledge nodes; and VDS is a non-empty set of virtual dependencies.

Based on the KFV model, KF designers can obtain VKFs from a given BKF by an order-preserving approach and a knowledge concept generalization method. The detailed algorithms and examples of the approach and the method are listed in our previous work [21]. Consequently, different VKFs can be derived to ful<sup>fi</sup>ll team members knowledge-needs in teamwork environments.

## 4. Introducing roles into the knowledge <sup>fl</sup>ow view model

In this section, we extend the knowledge <sup>fl</sup>ow view (KFV) model to a role-based KFV model by adding the role aspect. The purpose of the role-based KFV model is to derive role-based virtual knowledge <sup>fl</sup>ows (VKFs) from a base knowledge <sup>fl</sup>ow (BKF). In the role-based KFV model, virtual knowledge nodes (VKNs) are generated from base knowledge nodes (BKNs) based on the relevance degrees between roles and BKNs. In addition, a concept abstraction method is developed to abstract knowledge concepts of BKNs for a VKN.

![](/api/attachments/J5Y6DZAF/fulltext/images/83910b1302594352b5d7b591efb1afb5170946861e46bb181e9d1902eb2e1755.jpg)  
Fig. 3. A BKF derives multiple VKFs.

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/J5Y6DZAF/fulltext/images/c286d54f80f77e2e1e71a884b1ba9fe98e5e327ba639db4bfed4ac18403fe572.jpg)  
Fig. 4. KFV model.

## 4.1. Concepts of role-based virtual knowledge flows

In this sub-section, we present the concepts of role-based VKFs. A role-based VKF comprises a set of VKNs that are aggregated from BKNs according to their relevance to a role. Some BKNs may be more relevant to the role than others. A VKN in a role-based VKF denotes a meaningful (aware-needed) knowledge unit of interest to the role; thus, it should be relevant to the role. The process of identifying a role-relevant VKN involves aggregating BKNs based on their relevance to the role. Once the relevance of the aggregated BKNs to the role reaches a certain threshold, a VKN is identi<sup>fi</sup>ed for the role. The relevance of a BKN to a particular role can be speci<sup>fi</sup>ed by KF designers or derived from the relevance degrees between the role and the operations which are associated with the BKNs. The relevance degree of a BKN indicates how important it is to the role. Based on the relevance degrees of all BKNs, procedures can be clearly de<sup>fi</sup>ned to generate appropriate role-based VKFs for different organizational roles.

After a VKN has been identi<sup>fi</sup>ed, KF designers can derive its knowledge concepts. The objective is to obtain abstractions of the knowledge concepts in the VKN's member knowledge nodes that do not conform to the knowledge required by the role. The knowledge requirements are represented by knowledge concepts which can be identi<sup>fi</sup>ed in domain ontology. Domain ontology is a hierarchical structure comprising knowledge concepts. The lower levels of the hierarchy contain speci<sup>fi</sup>c knowledge, while the upper levels contain knowledge that is more general. The various roles in an organization have different knowledge requirements. Workers need speci<sup>fi</sup>c knowledge about their own roles and tasks, but need general knowledge about other roles' tasks. For example, R&D workers design and develop products, so they must have speci<sup>fi</sup>c technical skills and knowledge. The marketing and sales personnel, who launch and promote products, may not have speci<sup>fi</sup>c technical knowledge about the products, but they must have general knowledge about the technical aspects.

## 4.2. Role-knowledge node relevance and knowledge requirement

The crucial part of deriving role-based VKFs is to <sup>fi</sup>nd the relevance degree between each BKN and each role in a given BKF. Based on the derived relevance degrees, a proposed approach can then generate appropriate VKFs for different organizational roles. The process of generating a role-based VKF incorporates the concept of operations, which is essential in organizational environments. In this sub-section, base knowledge node profile and role-operation relevance profile are introduced for evaluating role-knowledge node relevance to generate VKNs. In addition, operation required knowledge concept set (KCS) profile and role-operation knowledge requirement degree (krdeg) profile are proposed for deriving roles' knowledge requirements to abstract knowledge concepts for VKNs.

## 4.2.1. Base knowledge node profile

A BKN is associated with different operations. The base knowledge node pro<sup>fi</sup>le is a set of 2-tuple bbase knowledge node bkn, operation op>, which expresses that operation op is associated with base knowledge node bkn.

## 4.2.2. Role-operation relevance profile

The pro<sup>fi</sup>le is used to determine how important an operation is to a role, since some operations are more relevant to a role than others. The pro<sup>fi</sup>le, which records the relevance degree between a role and an operation, is a set of 3-tuple brole r, operation op, operation relevance degree ordeg>. Each 3-tuple records that the operation relevance degree between role r and operation op is ordeg. Roles have different ordeg to their operations. The more the relevance between a role and an operation, the higher the ordeg will be. The ordeg is used as a quanti<sup>fi</sup>ed value to abstract BKNs into VKNs.

For example, suppose a software engineer r is assigned to perform an operation op called developing a sales database system. Because the engineer's job function is system development, the op is highly relevant to r. Therefore, the operation relevance degree of op to r is high. The ordeg is limited to the range [0, 1]. In this case, the value is between 0.7 and 1.0. The role-operation relevance pro<sup>fi</sup>le is described as br, op, 0.9>.

## 4.2.3. Operation required knowledge concept set (KCS) profile

The pro<sup>fi</sup>le comprises a set of 3-tuple boperation op, knowledge category ca, knowledge concept set kcs>, which represents the set of required knowledge concepts kcs in knowledge category ca for performing operation op. The domain ontology is divided into knowledge categories, and an operation may be related to more than one knowledge category. A knowledge concept set (kcs) indicates which knowledge concepts in a given knowledge category are required to perform an operation.

For example, according to its operation characteristics, performing a selling iPad operation requires speci<sup>fi</sup>c marketing-related knowledge concepts including Apple, target user, benefit and discount and general IT-related knowledge concepts including requirement, design and programming. These knowledge concepts can be mapped to IT or Marketing knowledge categories, as shown in Fig. 5 where IT occupies c2 and Marketing occupies c3. Thus, the operation required KCS pro<sup>fi</sup>les for the operation selling iPad are bselling iPad, IT, {c21, c22, c23}> and bselling iPad, Marketing, {c3111, c332, c3311, c3422}>.

![](/api/attachments/J5Y6DZAF/fulltext/images/f3a4df7c3ef0776bea8f14159acb15f13445234c87587a022b3a4b120ba65270.jpg)  
Fig. 5. Partial IT and Marketing knowledge categories in domain ontology.

## 4.2.4. Role-operation knowledge requirement degree (krdeg) profile

For a given operation, different roles may require different degrees of knowledge in different knowledge categories. The pro<sup>fi</sup>le is a set of 4-tuple brole r, operation op, knowledge category ca, knowledge requirement degree krdeg>. Each tuple indicates that the degree of knowledge required by role r with respect to operation op in knowledge category ca is krdeg. The value of krdeg is between 0 and 1 and it is used to de<sup>fi</sup>ne how speci<sup>fi</sup>c or general the required knowledge in a certain knowledge category should be for role r while executing operation op.

Overall speaking, two phases are required to generate VKFs. Phase I generates VKNs and Phase II abstracts knowledge concepts for these VKNs. In Phase I, role-operation relevance pro<sup>fi</sup>le, base knowledge node pro<sup>fi</sup>le and a granular threshold TH (a parameter de<sup>fi</sup>ned in Section 5.1.2) are used to generate VKNs. In Phase II, role-operation krdeg pro<sup>fi</sup>le and operation required KCS pro<sup>fi</sup>le are used to abstract knowledge concepts to required concept levels for VKNs. Table 1 shows the pro<sup>fi</sup>les and parameters exploited in the role-based KFV model. Items 1, 2 and 3 are related to Phase I and items 4 and 5 belong to Phase II. The pro<sup>fi</sup>les are derived by operation log analysis or opinions of domain experts in terms of the involved operations and participating roles in the BKF. Moreover, the parameters can be adjusted by roles and KF designers in terms of roles' requirements.

As mentioned earlier, the operation required KCS pro<sup>fi</sup>les record the required knowledge concepts for performing an operation and the role-operation krdeg pro<sup>fi</sup>les represent roles' knowledge require ment degrees. Thus, KF designers can use krdeg, which is estimated by role r and KF designers, as a basis to abstract the required knowledge concepts into appropriate concept levels. Role r should continue evaluating the <sup>fi</sup>tness level of the abstracted knowledge concepts until they are satis<sup>fi</sup>ed with the derived VKFs.

Fig. 6 shows an example to express the two phases for generating role-based VKFs. In Phase I (generate VKN), the relevance degree ordeg of role r to operation op and $o p _ { 2 }$ is 0.2 and 0.05 respectively (shown in role-operation relevance pro<sup>fi</sup>le); $o p _ { 1 }$ and $o p _ { 2 }$ are associated with bkn (shown in base knowledge node pro<sup>fi</sup>le) and the threshold is set to 0.4. In Phase II (abstract knowledge concept), the knowledge concepts required to perform op are {c131, c132} in marketing category and {c621} in hardware category (shown in operation required KCS pro<sup>fi</sup>le); the knowledge requirement degree krdeg of role r to perform op is 0.8 for marketing category and 1.0 for hardware category (shown in role-operation krdeg pro<sup>fi</sup>le). The above information is used to generate role-relevant VKNs as well as derive the corresponding knowledge concepts for the VKNs.

Next, the following section discusses how to construct role-operation relevance pro<sup>fi</sup>le and evaluate the relevance degrees between a given role and a BKN

## 4.2.5. Construction of role-operation relevance profile

Initially, KF designers can obtain role-operation relevance pro<sup>fi</sup>les by consulting domain experts or by analyzing roles' operating logs through adopting process mining technique [38] or knowledge <sup>fl</sup>ow mining methodology [16].

Table 1 List of pro<sup>fi</sup>les and parameters.

<table><tr><td>Phase</td><td>Item</td><td>Name and definition</td><td>Meaning</td><td>Building methods</td></tr><tr><td rowspan="3">I. Generate VKN</td><td>1</td><td>Role-operation relevance profile</td><td>Relevance degree (ordeg) between r and op</td><td>Analyzing operation logs or KF designers consult domain experts</td></tr><tr><td>2</td><td>Base knowledge node profile</td><td>Associate bkn and op</td><td>KF designers consult domain experts</td></tr><tr><td>3</td><td>Granular threshold TH</td><td>Parameter to determine the granularity of the generated VKNs</td><td>Decided by roles and KF designers</td></tr><tr><td rowspan="2">II. Abstract knowledge concepts</td><td>4</td><td>Role-operation krdeg profile</td><td>Degree of knowledge required (krdeg) by role r with respect to operation op in category ca</td><td>Roles and KF designers input krdeg in the profile</td></tr><tr><td>5</td><td>includes a parameter krdeg Operation required KCS profile</td><td>Required knowledge concept set (kcs) in category ca for performing op</td><td>KF designers consult domain experts</td></tr></table>

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

![](/api/attachments/J5Y6DZAF/fulltext/images/1987af1a3671a36005c7aa048f76d60234fcdb9175061f381e1b193793338369.jpg)  
Fig. 6. Two-phase approach to generate role-relevant VKNs.

Let T denote the number of times that role r performs all of the assigned operations, and let N denote the number of times that role r performs an operation op. The default operation relevance degree of r with respect to op is N/T. For example, three operations, selling iPAD (op ), devising business model (op ), and designing advertisement (op ), are assigned to a role r, marketing manager. The role r performs op<sub>1</sub> twice, op seven times, and op once; then T equals 10. The operation relevance degree ordeg of r is 0.2 for op , 0.7 for op , and 0.1 for op . Intuitively, a higher ordeg indicates greater relevance between a role and an operation. Moreover, the higher the cost associated with an operation performed by a role, the higher the relevance degree of the operation to the role will be. Let Q denote the total cost of the operations assigned to role r, and let C denote the cost of a speci<sup>fi</sup>c operation op. The ordeg of role r when performing operation op is C/Q. Based on activity-based costing (ABC) models, the cost can be measured in terms of the time and resources expended by roles when they perform assigned operations. In summary, different statistics can be extracted from the historical log data. Some decision-making methods can be employed to derive the ordeg by combining the statistics.

It is noteworthy, while implementing a role-based KFV system, that the proposed methods for constructing the role-operation relevance pro<sup>fi</sup>les need to be <sup>fi</sup>ne-tuned in terms of the culture of organizations, the accommodation of peripheral systems and the context of operations. Workers' future operation logs can also be used to adjust ordeg to satisfy their real time knowledge-needs. These adjustments are essential to obtain appropriate VKNs.

## 4.2.6. Evaluation of role-knowledge node relevance

The relevance degree between a given role and a BKN can be derived from role-operation relevance profile and base knowledge node profile. For example, given a role-operation relevance pro<sup>fi</sup>le {br, $o p _ { 1 } , \ 0 . 2 > , \ < r , \ o p _ { 2 } , \ 0 . 0 5 > $ and a knowledge node pro<sup>fi</sup>le {bbkn , $o p _ { 1 } > , < b k n _ { 1 } , ~ o p _ { 2 } > \}$ , the relevance degree between r and bkn is max $( 0 . 2 , 0 . 0 5 ) { = } 0 . 2 $ . That is, the relevance degree between r and bkn is the largest ordeg among all operations related to bkn .

## 5. Discovering role-based virtual knowledge <sup>fl</sup>ows

In this section, we propose a role-based approach for discovering virtual knowledge <sup>fl</sup>ows (VKF) suitable for participating roles. Generating VKFs involves two phases: Phase I identi<sup>fi</sup>es role-relevant virtual knowledge nodes (VKNs); and Phase II derives the knowledge concepts of the identi<sup>fi</sup>ed VKNs.

Phase I is to aggregate the BKNs based on their relevance to a given role. The relevance degree between a BKN and a role, which is derived as discussed in Section 4.2, describes how important the BKN is to the role. Based on the relevance degrees, procedures can be de<sup>fi</sup>ned to generate appropriate role-based VKFs for different roles. The knowledge concept abstraction process in Phase II obtains the knowledge concepts of VKNs based on operation required KCS profile and role-operation krdeg profile. An operation required KCS profile indicates the speci<sup>fi</sup>c knowledge concepts required to perform an operation. For a given operation, different roles may require different degrees of knowledge. The role-operation krdeg profile indicates how speci<sup>fi</sup>c the knowledge required for the role will be. The smaller the krdeg, the more general the required knowledge will be. The krdeg is used to adjust operation required knowledge concepts to a more general concept level in the domain ontology. The abstraction method analyzes the concept levels of required knowledge concepts and abstracts them to a suitable concept level.

In Section 5.1, we propose an approach for identifying role-relevant VKNs. In addition, the corresponding ideas and algorithms for generating role-based VKFs are introduced. We explain how to derive the knowledge concepts of VKNs in Section 5.2.

## 5.1. Phase I: generate virtual knowledge node

We propose algorithms that generate role-relevant VKNs automatically based on the role-knowledge node relevance degrees described in Section 4.2, which can be derived from role-operation relevance profile and base knowledge node profile. To obtain VKNs, KF designers take the highest order BKN x in the BKF as a seed node to identify a role-relevant VKN by combining adjacent BKNs based on their relevance to the given role. The detail steps are described in the following subsections.

## 5.1.1. Identifying role-relevant virtual knowledge nodes

A VKN in a role-based VKF denotes a meaningful knowledge unit of interest to the role; thus, it should be relevant to the role. Algorithm VKNSGenerator identi<sup>fi</sup>es VKNs based on a BKF bBKNS, BD>. The objective is to discover the VKNs whose relevance degrees approximate a granular threshold, TH, which is decided by roles and KF designers.

The algorithm VKNSGenerator in Fig. 7 selects the highest order BKN x in the BKF as the seed node to identify a role-relevant VKN. It uses the algorithm GenerateRVKN to aggregate the adjacent BKNs based on their relevance to the role. When the total relevance degree of the set of aggregated BKNs approximates TH, a VKN is identi<sup>fi</sup>ed for the role and deemed relevant to the role. The above steps are repeated on the remaining BKNs until all of the derived VKNs cover all BKNs of the BKF. The process yields a set of VKNs to build the target VKF. For any pair of VKNs, vx and vy, a virtual dependency vdep (vx, vy) exists if dep(x, y) exists in BD, where x is a member of vx and y is a member of vy.

Next we explain three important components of the algorithm VKNSGenerator: (1) determining the relevance between roles and BKNs, (2) generating a role-relevant VKN by algorithm GenerateRVKN and (3) verifying the order-preserving property.

## 5.1.2. Determining the relevance between roles and base knowledge nodes

From the base knowledge node profile, KF designers can determine whether a BKN is associated with certain operations. In addition, the role-operation relevance profile indicates the degree of relevance of an operation to a role. The relevance of a BKN to a role can be derived from the base knowledge node profile and the role-operation relevance profile by applying maximum function over the ordeg of the operations associated with the BKN, as described in Section 4.2.

Granular Threshold TH determines the granularity of a generated VKN. After calculating the degree of relevance of each BKN to the role, the algorithm GenerateRVKN combines adjacent BKNs to generate a role-relevant VKN. When the sum of the relevance degrees of the set of adjacent BKNs approximates TH, the set of adjacent BKNs can form a VKN, which is deemed relevant to the role. A larger TH corresponds to the generation of fewer VKNs, which means that more BKNs are included in one VKN.

Total relevance degree $F _ { T R D } \mathrm { : }$ Let function f (role r, base knowledge node bkn) return the relevance degree of bkn to role r; and let function $F _ { T R D }$ (role r, base knowledge node set V) return the total degree of relevance of a virtual knowledge node vkn comprising the base knowledge node set $V . F _ { T R D } \left( r , V \right) = \Sigma f _ { K R D }$ (r, bkn ) for all $b k n _ { i } \in V .$

The threshold TH in Phase I (Generate VKN) is determined by the roles and KF designers to obtain VKNs with their expected granularity. Abstracting BKNs based on the degrees of relevance of role-knowledge nodes could help to accumulate several less role-relevant BKNs until their total degree of relevance, $F _ { T R D } ,$ is close to a threshold TH. In order to sustain productivity and conduct KM effectively, a role requires greater attention paid to the operations and associated knowledge concepts of BKNs with high degrees of relevance to the role. Roles can omit the speci<sup>fi</sup>c (detailed) information of BKNs with low degrees of relevance. Accordingly, BKNs with low degrees of relevance to a role are aggregated until they form a role-relevant VKN that is suf<sup>fi</sup>ciently relevant to the role. Here, a granular threshold TH is set as the criterion to determine suf<sup>fi</sup>cient relevance. According to a role-relevant VKN, a role can have a general idea about the BKNs included in the VKN and omit the speci<sup>fi</sup>c (detailed) information of those BKNs.

For example, given three BKNs: $k _ { 1 } , k _ { 2 }$ and $k _ { 3 }$ with relevance degrees 0.1, 0.2 and 0.05 to role $r ,$ respectively, role r sets TH as 0.4. In other words, role r requests the detail information and knowledge concepts of these less role-relevant BKNs to be ignored until their total degree of relevance, $F _ { T R D } ,$ is close to 0.4 after abstraction. Hence, KF designers aggregate $k _ { 1 } ,$ k and $k _ { 3 }$ to a virtual knowledge node, vkn , following the proposed role-based knowledge <sup>fl</sup>ow abstraction methods. The degree of relevance between role r and vkn<sub>1</sub> would be 0.35, which is close to 0.4. After the abstraction, the virtual knowledge node, vkn , deserves role r's awareness.

## 5.1.3. Virtual knowledge node generation algorithm

The algorithm GenerateRVKN generates a VKN, which contains a given seed node, by repeatedly aggregating the adjacent BKNs according to the order of their relevance degrees sorted from high to low. Note that the aggregation of BKNs needs to satisfy the order-preserving property; this will be illustrated in Section 5.1.4. The process is repeated until the total relevance degree of the aggregated BKNs approximates TH. The steps of the algorithm are detailed in Fig. 8.

For a virtual knowledge node vkn=bvid, V, D, VKC>, the members of V must be identi<sup>fi</sup>ed <sup>fi</sup>rst. Initially, V only contains the given seed knowledge node bkn. The algorithm then determines whether the BKNs which are adjacent to members of V can be added to maximize its total relevance degree $F _ { T R D } \left( r , V \right)$ so that it approximates TH. V is updated during the while loop by adding the adjacent BKNs that satisfy three conditions: (1) V conforms to the order-preserving property; (2) the total relevance degree of V does not exceed the threshold (F<sub>TRD</sub> $( r , K N S _ { t m p } ) \mathop { \leq } T H ) ;$ ; and (3) V does not overlap with previously derived VKNs $( K N S _ { t m p } ~ R K N S )$ . The repeat-until loop continues until no other adjacent BKNs can be added to $V ,$ i.e., no more adjacent BKNs can be added to V, which still satisfy the threshold limit and maintain order-preserving property.

## 5.1.4. Verification of the order-preserving property

Liu and Shen [22] developed an order-preserving approach that generates virtual processes from a base process in work<sup>fl</sup>ow environments.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm VKNSGenerator: generate a set of VKNs
input: a base knowledge flow $BKF = &lt;BKNS, BD&gt;$
output: the virtual knowledge node set (VKNS) of a virtual knowledge flow $VKF = &lt;VKNS, VDS&gt;$
begin
i=1
repeat
Create a new virtual knowledge node $vkn_i = &lt;vid_i, KNS_i, D_i, VKC_i&gt; \leftarrow &lt;i, \emptyset, \emptyset, \emptyset&gt;$
Residual Knowledge Node Set $RKNS \leftarrow BKNS - \{x | x \text{ belongs to one of } KNS_i, \text{ for any } i\}$
Select the highest order base knowledge node $x$ from $RKNS$ $vkn_i \leftarrow \text{GenerateRVKN}(i, x, RKNS, BKF)$ $VKNS = VKNS \cup \{vkn_i\}$ $i = i+1$
until $\forall x \in BKNS, x$ belongs to one of $KNS_i$, for any $i$
return VKNS
end
</div>

Fig. 7. Algorithm for generating a set of VKNs

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx-xxx

Algorithm GenerateRVKN: generate a VKN whose total relevance degree approximates TH
input: label i, seed knowledge node bkn, residual knowledge node set RKNS, BKF = &lt;BKNS, BD&gt;
output: a virtual knowledge node vkn

begin

vkn = ⟨vid, V, D, VKC⟩ ← ⟨i, {bkn}, ∅, ∅⟩

repeat

Temp Knowledge Node Set TKNS ← V

Adjacent Knowledge Node Set AKNS ← {x | x, y ∈ RKNS, x∉ V, y ∈ V, and dep(x, y) ∈ BD}

while AKNS is not empty do

select a BKN x from AKNS

remove x from AKNS

 $KNS_{tmp} \leftarrow OderPrsv(V \cup \{x\}, BKF) /* check order-preserving property */$ 

if ( $F_{TRD}$  (role r,  $KNS_{tmp}$ ) ≤ TH) and ( $KNS_{tmp} \subseteq RKNS$ ) then /* check threshold */

 $V \leftarrow KNS_{tmp}$ $AKNS \leftarrow AKNS - \{y \mid y \in AKNS \cap V\}$ 

end if

end while

until V = TKNS

A dependency set D ← {dep(x, y) | x, y ∈ V, and dep(x, y) ∈ BD}

VKC = KCGEN-OKR (role r, virtual knowledge node vkn)

return vkn = ⟨vid, V, D, VKC⟩

end

Fig. 8. Algorithm for generating a role-relevant VKN.
</div>

The approach ensures that the generated virtual process satis<sup>fi</sup>es the following order-preserving property: the implied ordering relations of activities in a virtual process must comply with the ordering relations of activities in the base process. The generation algorithm GenerateRVKN adopts the order-preserving approach to ensure that a VKF maintains the knowledge referencing order in its corresponding BKF. A legal virtual knowledge node vkn=〈vid, V, D, VKC〉 must satisfy the following order-preserving property: the implied ordering relations of VKNs in a VKF must comply with the ordering relations of the BKNs in its corresponding BKF. The order-preserving property is satis<sup>fi</sup>ed when the ordering relations between any BKN x∉V and all member knowledge nodes in V are identical as their ordering relations in the corresponding BKF. Regarding the function OderPrsv in algorithm GenerateRVKN for adopting the order-preserving approach, please refer to our previous work [19,21,22] for the detailed steps and examples.

## 5.1.5. Illustrating examples

Given a base knowledge node $b k n _ { 1 }$ and its adjacent base knowledge nodes, $b k n _ { 2 }$ and $b k n _ { 3 } ,$ we explain how the algorithm generates a virtual knowledge node vkn .

Example 1. The role-knowledge node relevance degree is derived from the following pro<sup>fi</sup>les. (A) Base knowledge node profile: $\{ < b k n _ { 1 } , o p _ { 1 } >$ $< b k n _ { 1 } , o p _ { 2 } > , < b k n _ { 1 } , o p _ { 5 } > , < b k n _ { 1 } , o p _ { 7 } > \}$ , which indicates that operations $o p _ { 1 } , o p _ { 2 } , o p _ { 5 }$ and $o p _ { 7 }$ are associated with bkn . (B) Role-operation relevance profile: $\{ < r _ { 1 } , \ o p _ { 1 } , \ 0 . 6 > , \ < r _ { 1 } , \ o p _ { 2 } , \ 0 . 3 > , \ < r _ { 1 } , \ o p _ { 5 } , \ 0 . 4 > , \ < r _ { 1 } , $ op<sub>7</sub>, $0 . 1 > \}$ , which indicates the relevance degrees between $r _ { 1 }$ and the operations. Based on the above information, the maximum function is used to obtain the relevance degree between bkn and $r _ { 1 } .$ Max (0.6, 0.3, 0.4, $0 . 1 ) { = } 0 . 6$

Example 2. A VKN is generated from the following pro<sup>fi</sup>les. (A) Base knowledge node profile: $\{ < b k n _ { 2 } , o p _ { 3 } > , < b k n _ { 2 } , o p _ { 5 } > , < b k n _ { 3 } , o p _ { 4 } > , $ bbkn , $o p _ { 6 } { > } \}$ , which indicates $b k n _ { 2 }$ is associated with $o p _ { 3 } , o p _ { 5 }$ , and $b k n _ { 3 }$ is associated with op<sub>4</sub>, op<sub>6</sub>. (B) Role-operation relevance profile: {br<sub>1</sub>, op<sub>3</sub>, $\theta . 2 > , < r _ { 1 } , o p _ { 5 } , 0 . 3 > , < r _ { 1 } , o p _ { 4 } , 0 . 1 > , < r _ { 1 } , o p _ { 6 } , 0 . 2 > \}$ . The pro<sup>fi</sup>le indicates the relevance degrees between $r _ { 1 }$ and the operations associated with $b k n _ { 2 }$ and $b k n _ { 3 } .$ Based on the above information, the maximum function is used to obtain the relevance degrees of $b k n _ { 2 }$ and $b k n _ { 3 }$ for $r _ { 1 } .$ Max $( 0 . 2 , 0 . 3 ) = 0 . 3$ for $b k n _ { 2 } ;$ Max $( 0 . 1 , 0 . 2 ) = 0 . 2 $ for $b k n _ { 3 } .$ . The relevance order of the adjacent knowledge nodes of $b k n _ { 1 }$ is bkn followed by bkn<sub>3</sub>.

Taking the order structure into consideration, $b k n _ { 2 }$ and $b k n _ { 3 }$ are candidate nodes to be combined with $b k n _ { 1 }$ . Assuming that the threshold TH is 1, the relevance degrees for bkn and $b k n _ { 3 }$ are 0.3 and 0.2, respectively. According to the function $F _ { T R D } ,$ the two nodes cannot be combined with $b k n _ { 1 }$ together to form a VKN because $f _ { K R D } ( b k n _ { 1 } ) + f _ { K R D } ( b k n _ { 2 } ) + f _ { K R D } ( b k n _ { 3 } ) > 1$ . However, the total relevance degree $f _ { K R D } ( b k n _ { 1 } ) + f _ { K R D } ( b k n _ { 2 } ) \leq 1$ , which is not greater than TH. Thus, $b k n _ { 1 }$ is combined with $b k n _ { 2 }$ to form a virtual knowledge node vkn .

## 5.2. Phase II: abstract knowledge concept

After a virtual knowledge node vkn has been generated, its knowledge concepts can be derived. Fig. 9 shows the algorithm KCGEN-OKR that derives the knowledge concepts of vkn based on the operation required knowledge concept set (KCS) profiles and the role-operation knowledge requirement degree (krdeg) profiles.

We explain how to derive the required KCS and corresponding krdeg for operations that the role performs on a VKN. The operation required knowledge concepts indicate the most speci<sup>fi</sup>c level of knowledge in the domain ontology that are required to perform operations. Different roles may require different degrees of knowledge to perform operations. In this work, we use the knowledge requirement degree krdeg as the basis to abstract the operation required knowledge concepts into the appropriate concept levels CLs) in order to satisfy a role's operation knowledge requirement. The virtual knowledge node vkn may include more than one BKN, so the knowledge concepts of all BKNs should be abstracted to derive the knowledge concepts of vkn. The knowledge concept abstraction process involves two steps. The <sup>fi</sup>rst step derives the required knowledge concept set (KCS) and corresponding knowledge requirement degrees (krdeg). The second step adjusts (generalizes) the knowledge concepts in KCS to the appropriate concept level according to the corresponding krdeg of the role.

```txt
Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge flows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx-xxx

Algorithm KCGEN-OKR: generalize knowledge concepts based on operation required KCS profile and role-operation krdeg profile
input: role r, a virtual knowledge node vkn = &lt;vid, KNS, D, VKC&gt;
output: VKC of vkn

begin
    $CRD_{r}^{vkn} = \{\}$  /* is a set of 3-tuple &lt;concept c, category ca, knowledge requirement degree krdeg&gt; */
    $OP_{r}^{vkn}$  is a set of operations associated with vkn and performed by role r
    /* Step 1: derive required KCS and corresponding krdeg for each concept in KCS*/
    for each operation op in  $OP_{r}^{vkn}$  do
    $KCS_{op}^{ca}$  is a set of knowledge concepts in category ca required to perform op
    for each knowledge category ca related to operation op do
    for each concept c in  $KCS_{op}^{ca}$  and its associated role-operation knowledge req. degree  $krdeg_{r,op}^{ca}$  do
    if concept c already exists in  $CRD_{r}^{vkn}$  then
    $krdeg_{r,c}^{ca} = \text{the knowledge requirement degree of concept c in } CRD_{r}^{vkn}$ $CRD_{r}^{vkn} = \max(krdeg_{r,c}^{ca}, krdeg_{r,op}^{ca})$ 
    else
    $krdeg_{r,c}^{ca} = krdeg_{r,op}^{ca}$ 
    end if
    $CRD_{r}^{vkn} = CRD_{r}^{vkn} \cup \{&lt;concept c, category ca, krdeg_{r,c}^{ca}&gt; \}$ 
    end for
    end for
end for
/* Step 2: adjusts (generalizes) knowledge concepts to appropriate concept levels */
for each tuple &lt;concept c, category ca, knowledge requirement degree  $krdeg_{r,c}^{ca} &gt; \text{in } CRD_{r}^{vkn}$  do
    $gc = GenConcept(c, ca, krdeg_{r,c}^{ca})$ $GKCS = GKCS \cup \{gc\} /* GKCS: generalized knowledge concept set */$ 
end for
for each knowledge concept  $c_i$  in GKCS do
    if every path from  $c_i$  to leaf nodes in the domain ontology  $\exists c_j(c_i \text{ is not included}) \in GKCS$  then
    remove  $c_i$  from GKCS
    end if
end for
VKC of vkn = GKCS
end
</div>

Fig. 9. Algorithm for generalizing knowledge concepts of a VKN.

An operation required KCS pro<sup>fi</sup>le speci<sup>fi</sup>es the knowledge concepts required in different knowledge categories to perform an operation. The domain ontology is divided into different knowledge categories; an operation may be associated with more than one knowledge category. From the operation required KCS pro<sup>fi</sup>le, the speci<sup>fi</sup>c knowledge concepts required for each operation in each knowledge category are obtained. For a given operation, different roles may have different degrees of knowledge requirements in different knowledge categories. The role-operation krdeg pro<sup>fi</sup>le is used to de<sup>fi</sup>ne how speci<sup>fi</sup>c or general the required knowledge in a certain knowledge category should be for role r when it performs an operation. From the operation required KCS pro<sup>fi</sup>le and role-operation krdeg pro<sup>fi</sup>le, KF designers can generate the set of required knowledge concepts and their corresponding knowledge requirement degrees for the role to perform the operations associated with vkn. A role may have different knowledge requirement degrees to perform different operations that need the same knowledge concepts. Therefore, a knowledge concept required by a role may be associated with more than one krdeg. The maximum function is used to derive the <sup>fi</sup>nal krdeg of a concept for the role.

The <sup>fi</sup>rst step in algorithm KCGEN-OKR is to derive required KCS and corresponding krdeg, which uses several working sets and variables for computation, including: (1) $O P _ { r } ^ { v k n }$ is a working set of operations. The operations are associated with vkn and performed by r. Thereby; vkn comprises a set of merged BKNs. (2) KCS<sup>ca</sup> is a working set of knowledge concepts. The knowledge concepts belong to knowledge category ca and they are required to perform operation op. (3) $k r d e g _ { r , o p } ^ { c a }$ is a working variable of r's knowledge requirement degree. The krdeg is related to knowledge category ca and operation op. $( 4 ) C R D _ { r } ^ { \nu k n }$ is a working set associated with r and vkn. It is a 3-tuple bconcept $c ,$ category ca, knowledge requirement degree krdeg>, which indicates the required krdeg of c in ca $C R D _ { r } ^ { v k n }$ is derived from $O P _ { r } ^ { v k n }$ , KCS<sub>op</sub><sup>ca</sup> and $k r d e g _ { r , o p } ^ { c a }$ as detailed in algorithm KCGEN-OKR.

In algorithm KCGEN-OKR, the second step is to adjust (generalize) the knowledge concepts to the appropriate concept level according to krdeg. For each knowledge concept in $C R D _ { r } ^ { v k n }$ bconcept c, category ca, knowledge requirement degree krdeg>, krdeg determines how many levels of the original concept c should be abstracted. The value of krdeg is between 0 and 1; the larger the value, the more speci<sup>fi</sup>c the knowledge concepts that are required; conversely, the smaller the value, the more general the knowledge concepts that are required. If krdeg is 1.0, the most speci<sup>fi</sup>c level of knowledge concept is required, so there is no need to perform abstraction. A function GenConcept(c, ca, krdeg<sub>r,c</sub><sup>ca</sup>) is used to adjust the concept c in category ca to an appropriate concept level according to krdeg<sup>ca</sup>. For example, $\mathrm { i f ~ } k r d e g _ { r , A p p l e } ^ { M a r k e t i n g } = 0 . 8 ,$ GenConcept (Apple, marketing, 0.8) returns the parent knowledge concept brand of knowledge concept Apple in category marketing. According to Fig. 5, the concept level (CL) of brand is 4 and the CL of Apple is 5. That is, GenConcept (Apple, marketing, 0.8) executes one-level up abstraction of Apple to get generated concept (gc) through the domain ontology as shown in algorithm KCGEN-OKR. If $k r d e g _ { r , c } ^ { c a } = 0 . 6 ,$ , GenConcept(c, ca, 0.6) returns the grandparent knowledge concept of concept c in category ca by executing two-level up abstraction through the domain ontology. If there are insuf<sup>fi</sup>cient levels in the domain ontology can be obtained when executing the function GenConcept, the concept c is abstracted to the most general concept level. If $k r d e g _ { r , c } ^ { c a } = 1 . 0$ , no abstraction is needed; GenConcept(c, ca, 1.0) returns the concept c. It is notable that the mapping between the value of krdeg $( 0 . 8 , 0 . 6 , \ldots )$ and the levels of abstraction (one-level up abstraction, two-level up abstraction,…) can be adjusted by KF designers depending on applications.

```txt
Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge flows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018
```

The function GenConcept(c, cl, acl) is used to adjust concept c to an appropriate concept gc. Let GKCS (generalized knowledge concept set) denote the set of knowledge concepts for vkn. For each knowledge concept c of the member knowledge nods in vkn, GKCS is added with the generalized knowledge concept gc, which is derived from concept c, to meet r's knowledge requirement. The <sup>fi</sup>nal step of the procedure removes the implied (redundant) concepts from GKCS and yields the knowledge concepts VKC of vkn.

Example 3. The knowledge concepts of vkn, which combines bkn and $b k n _ { 2 } ,$ are derived as follows. (A) Base knowledge node profile: $\{ < b k n _ { 1 } , o p _ { 1 } > , < b k n _ { 1 } , o p _ { 2 } > , < b k n _ { 2 } , o p _ { 3 } > \}$ . (B) Operation required KCS profiles: bop , Marketing, {Apple (c3111), benefit (c3311), discount $( c 3 4 2 2 ) \} > , < o p _ { 1 } , I T ,$ {Java (c2321), user need $( c 2 1 2 ) \} > , < o p _ { 2 } ,$ , Marketing, {need (c312), Apple (c3111), discount(c3422)}>, bop , IT, {Java (c2321), system $( c 2 2 1 ) \} >$ . These knowledge concepts are in different knowledge categories as shown in Fig. 5. (C) Role-operation krdeg profiles: br, op , Marketing, 0.8>, br, op , IT, 0.6>, br, $o p _ { 2 } ,$ Marketing, $0 . 6 > , < r _ { 1 } , o p _ { 3 } , I T , 0 . 4 >$

Investigating the operation required KCS profiles in Example 3, op and $o p _ { 2 }$ require the same knowledge concepts Apple and discount in Marketing knowledge category. Moreover, op and $o p _ { 3 }$ require the same knowledge concept Java in IT knowledge category. Thus, the krdeg of knowledge concept Apple, discount and Java should be preprocessed by a maximum function before abstraction. In Marketing knowledge category, the krdeg of Apple and discount for $o p _ { 1 }$ is 0.8, for $o p _ { 2 }$ is 0.6. After applying the maximum function Max (0.8, 0.6), the <sup>fi</sup>nal krdeg of Apple and discount is 0.8, which means that the two knowledge concepts should be abstracted by one-level up to their parent knowledge concepts brand and promotion respectively, according to the domain ontology in Fig. 5. In IT knowledge category, the krdeg of Java for $o p _ { 1 }$ is 0.6, for $o p _ { 3 }$ is 0.4. Thus, the <sup>fi</sup>nal krdeg of Java is Max $( 0 . 6 , 0 . 4 ) = 0 . 6 .$ Thus, the knowledge concept Java should be abstracted by two-level up to knowledge concept programming as well.

## 6. Designing a role-based KFV system

We analyze the proposed model and concepts to conduct the basic system design of a role-based KFV system. The basic system design constructs an overall architecture by identifying important functional modules and decomposing them into layers. An activity diagram models the procedural <sup>fl</sup>ow of actions from the perspectives of KF designers, roles and experts. Moreover, Protégé 4.0 software is used to build an ontology prototype to represent knowledge concepts and their hierarchical relationships in the mobile phone development domain. The system architecture, activity diagram and ontology prototype are the fundamental elements for putting the theoretical model into practice.

Fig. 10 depicts the system architecture to implement the role-based KFV system, which comprises four layers: data link layer, con<sup>fi</sup>guration layer, modeling layer and application layer.

## 6.1. Data link layer

This layer enables data links to other legacy systems to collect information from external data sources during the design time and run time. The operation logs preserve the history of roles' operations in work<sup>fl</sup>ow management systems. The knowledge databases store codi<sup>fi</sup>ed knowledge which is labeled by the knowledge concepts of domain ontology. Enterprise knowledge-based management systems can be utilized to manage these knowledge databases and provide interfaces for the role-based KFV system to access required codi<sup>fi</sup>ed knowledge. Domain ontology stores the pre-de<sup>fi</sup>ned knowledge concepts and their hierarchical relationships for the purpose of representing knowledge-needs and facilitating knowledge concept abstraction.

## 6.2. Configuration layer

This layer comprises three parts: pro<sup>fi</sup>le management module, BKF and role-based VKF repository as well as relevance degree calculating engine. KF designers and experts utilize the pro<sup>fi</sup>le management module to collect essential information, such as role-operation relevance pro<sup>fi</sup>les, operation required KCS pro<sup>fi</sup>les and base knowledge node pro<sup>fi</sup>les. The BKF and role-based VKF repository preserves model de<sup>fi</sup>nitions and enactment instances. The role-knowledge node relevance degree calculating engine is responsible for obtaining the relevance degrees between roles and BKNs.

## 6.3. Modeling layer

This layer includes three de<sup>fi</sup>nition tools to de<sup>fi</sup>ne BKFs, role-based VKFs and roles' knowledge requirement degrees. Roles use the knowledge degree de<sup>fi</sup>nition tool to set role-operation krdeg pro<sup>fi</sup>les to re<sup>fl</sup>ect roles' krdeg based on their knowledge-needs. Meanwhile, KF designers work with experts to specify BKFs and corresponding role-based VKFs by BKF and role-based VKF de<sup>fi</sup>nition tools, respectively. Moreover, the algorithms shown in Figs. 7, 8 and 9 for generating role-based VKFs will be realized in the de<sup>fi</sup>nition tools.

## 6.4. Application layer

An integrated platform is built in this layer for the operations of KF designers, experts and roles. This layer mainly provides an interface for them to get visualization support and maintain pro<sup>fi</sup>les.

We produced the activity diagram of the role-based KFV system, as shown in Fig. 11. The actors in the activity diagram are KF designers, roles and experts. They perform these procedural activities and produce relevant material for generating role-based VKFs. The activity diagram is organized into three partitions to indicate the major responsible person of the activities of each partition. The rounded rectangles represent the activities which are performed by actors manually or executed by the tools of the role-based KFV system. And the rectangles show the material such as pro<sup>fi</sup>les, parameters or intermediate output that passed between activities. We omitted the detailed explanation of the activity diagram here because it is somewhat self-explanatory. The activity diagram is useful for system modeling to describe the control <sup>fl</sup>ow of the role-based KFV system, such as exploring the knowledge concept abstraction and knowledge node generation approaches, as well as parameter evaluation and adjustment methods.

![](/api/attachments/J5Y6DZAF/fulltext/images/a325dc4109a9f944d41b000d2693fc7228af33dd5ffd866f70e558818221f713.jpg)  
Fig. 10. System architecture of the role-based KFV system

An approach of iterative evaluation and adjustment is adopted in the design to <sup>fi</sup>ne-tune pro<sup>fi</sup>les and parameters to improve the <sup>fi</sup>tness level of VKFs. At the bottom of the left partition in the activity diagram, role r should evaluate the <sup>fi</sup>tness level of the generated VKF. If role r is satis<sup>fi</sup>ed with the VKF, the procedure stops. Otherwise, role

![](/api/attachments/J5Y6DZAF/fulltext/images/3cf9474b34fffa0cb6d907cdd74195a3e8a3793c64313009a7fbd814efedbb58.jpg)  
Fig. 11. Activity diagram.

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

r would re<sup>fl</sup>ect the discrepancies of current VKF to KF designers and/or experts. Then, they may adjust BKF, ontology, krdeg, or TH and estimation methodologies, and regenerate VKFs again until role r satis<sup>fi</sup>es the result. For example, the iteration of krdeg's adjustment is shown by the merging of a start point (●) and the label © in the top of the left partition in Fig. 11.

The role-based concept has been adopted in many work<sup>fl</sup>ow related studies to reduce the impact of people turnover. Hence, the role-based VKFs are generated from a role perspective instead of an individual user perspective. The knowledge concepts in a VKN are the required knowledge concepts for roles to perform corresponding operations and communicate with other teammates. In case, some certain users playing the roles may already have the knowledge contained in the VKN or they cannot be satis<sup>fi</sup>ed with the knowledge concepts of the VKN. The certain users can <sup>fi</sup>ne-tune krdeg to adjust the knowledge concepts in the VKN to meet their requirements afterwards.

We used Protégé 4.0 software to build an ontology prototype, as shown in Fig. 12, to represent a part of knowledge concepts and their hierarchical relationships in mobile phone development domain. The process of ontology construction would include an evaluation and feedback mechanism to gradually improve ontology quality and result in a common understanding in organizations. The ontology prototype is appropriate for system designers to understand the concepts of ontologies in system design phase. Since new knowledge is continually generated with changes in technology and business environments, KF designers should periodically maintain domain ontologies and BKFs to check if any knowledge concepts should be added to or removed from BKNs. After the adjustment of BKFs, KF designers can regenerate new VKFs per roles' demands.

## 7. Case illustration and discussion

This section uses a base knowledge <sup>fl</sup>ow (BKF) of a mobile phone company, named Smart-Tech Company, to illustrate the application of the role-based KFV model. The BKF represents the knowledge which a project team requires while conducting a mobile phone development process. KF designers build the BKF based on the mobile phone development process, as shown in Fig. 1. They consult domain experts to identify important knowledge-needs and seek proper knowledge concepts in domain ontology for the purpose of building the BKF to represent these knowledge-needs. The participants of the mobile phone development team work for different departments and play different roles in the team. For example, a sourcing planner role performs the logistics of parts outsourcing and a sourcing department manager role evaluates project performance and the sourcing planner role's productivity. The sourcing department manager role is responsible for communicating with the project manager about the project status and outsourcing strategy, as well as appraising the performance of the sourcing planner role. Therefore, KF designers can generate a role-based VKF from the BKF to represent the sourcing department manager role's knowledge-needs to support task execution. The following discussion illustrates the process used to generate the role-based VKF. First, the BKF and the relevance degrees between the sourcing department manager role and the BKNs are obtained by the approach described in Section 4.2. The BKF in Fig. 13 includes eight BKNs, $k _ { 0 }$ to $k _ { 7 } .$ . Each BKN contains multiple knowledge concepts and has distinct operation relevance degrees to r, herein; r stands for the sourcing department manager role.

Next, KF designers generate virtual knowledge nodes (VKN) based on a threshold (TH) 0.4. They select a BKN with the highest order, $k _ { 0 } ,$ as a seed node to generate the <sup>fi</sup>rst virtual knowledge node vkn . The adjacent base knowledge node set AKNS of $k _ { 0 } \mathrm { i } s \{ k _ { 1 } \} .$ So, vkn is considered a legal VKN having two member knowledge nodes $k _ { 0 } , k _ { 1 } .$ . After checking $F _ { T R D } \left( r , \{ k _ { 0 } , k _ { 1 } \} \right)$ , KF designers can <sup>fi</sup>nd $F _ { T R D } \left( r , \left\{ k _ { 0 } , k _ { 1 } \right\} \right) = f _ { K R D }$ $\begin{array} { r } { \left( r , k _ { 0 } \right) + f _ { K R D } \left( r , k _ { 1 } \right) = 0 . 1 \le T H , } \end{array}$ which meet the threshold requirement. And vkn also complies with the order-preserving property. So, vkn is a legal VKN when it has two member KNs $k _ { 0 } , k _ { 1 }$ . Because $F _ { T R D } \left( r , \{ k _ { 0 } , k _ { 1 } \} \right)$ is not approximately close to TH, KF designers continue to evaluate AKNS of $\{ k _ { 0 } , k _ { 1 } \}$ , which is $\{ k _ { 2 } , k _ { 5 } \}$ . According to the order-preserving property, we should add BKNs $k _ { 2 } , k _ { 3 } , k _ { 4 } , k _ { 5 }$ and $k _ { 6 }$ into vkn . However, $\begin{array} { r } { F _ { T R D } \left( r , \left\{ k _ { 0 } \dots k _ { 6 } \right\} \right) = \sum f _ { K R D } \left( r , k _ { j } \right) \left\{ j = 0 \dots 6 \right\} = } \end{array}$ 0.55 exceeds TH. Therefore, the <sup>fi</sup>rst virtual knowledge node vkn and its member knowledge nodes, $k _ { 0 }$ and $k _ { 1 } ,$ are determined. Repeating the iteration, the BKNs are merged into four virtual knowledge nodes $\nu k n _ { 1 } , \nu k n _ { 2 } , \nu k n _ { 3 }$ and $\nu k n _ { 4 }$ to form a role-based VKF, as shown in Fig. 14.

![](/api/attachments/J5Y6DZAF/fulltext/images/b37428c40449579e8f324dfaef64fe0240f3ca32bfa5b813bd120a05e056759c.jpg)  
Fig. 12. An ontology prototype

D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/J5Y6DZAF/fulltext/images/a3db50985791b36d83e163302254cb7bf5b1a41adb1a6812e2ae2eceddc8aded.jpg)  
Fig. 13. Operation relevance degrees between role r and BKNs.

The following discussion takes virtual knowledge node vkn as an example to illustrate the concept abstraction method. First, KF designers and role r set r's knowledge-needs in terms of krdeg by different knowledge categories. A partial domain ontology which includes <sup>fi</sup>ve knowledge categories, such as: Marketing, Industrial design, Hardware design, Software design and Sales, is illustrated in Fig. 15. It is to be noted that the partial domain ontology is only used for concept explanation and case illustration here, instead of implementing a role-based KFV system in an organization. Ontology construction for organization use is a complex task and needs to further consider users' requirements, IT environments and the context of applications. This type of ontology is much more complete and complex than the partial domain ontology in Fig. 15.

Based on the two-phase approach for generating role-based VKFs shown in Fig. 6, KF designers, experts and role r determine the relevant pro<sup>fi</sup>les and parameters as shown in Fig. 16. According to the algorithm in Fig. 9, the knowledge requirement degree krdeg<sup>ca</sup>, which represents the knowledge requirement degree of role r in regard to the knowledge concept c in the knowledge category ca, can be obtained as below through computing the operation required KCS pro<sup>fi</sup>les and the role-operation krdeg pro<sup>fi</sup>les.

![](/api/attachments/J5Y6DZAF/fulltext/images/d856e35e08d2590fb8f687d8f9ed653b8039846f3d78a8c17b2c4d910199ea41.jpg)

Finally, the knowledge concepts are generalized to required concept levels. Consequently, the knowledge concepts of virtual knowledge node vkn are marketing, outsourcing, hardware design and display options. The same method can apply to other VKNs. Fig. 17 shows the <sup>fi</sup>nal result of the role-based VKF for sourcing department manager role.

## 7.1. Simulation by examples

As shown in Table 1, two phases are required to generate VKFs. Phase I generates VKNs and Phase II derives knowledge concepts for these VKNs. The pro<sup>fi</sup>les, including role-operation relevance pro<sup>fi</sup>le and base knowledge node pro<sup>fi</sup>le in Phase I, role-operation krdeg pro-<sup>fi</sup>le and operation required KCS pro<sup>fi</sup>le in Phase II, are predetermined by KF designers according to the involved operations and the participating roles in the BKF. The parameters, including threshold TH in

![](/api/attachments/J5Y6DZAF/fulltext/images/579f9e5196726789b7704d6a826876f9caeeeec5e5294655b5269e919248b7a7.jpg)  
Fig. 14. VKNs and their relevance degrees when TH=0.4.

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

![](/api/attachments/J5Y6DZAF/fulltext/images/25ce359aa822245157fc34a9cd08cb7756eef1b95932bfc7fbf9ea83dd0a9022.jpg)  
Fig. 15. Partial knowledge categories of Marketing and Hardware Design.

Phase I and knowledge requirement degree krdeg in Phase II, can be adjusted by roles and KF designers to re<sup>fl</sup>ect roles' requirements. The simulation by examples is performed to evaluate these two parameters, which is based on the BKF shown in Fig. 13.

In Phase I, the granular threshold TH is a parameter to determine the granularity of the generated VKNs. Fig. 18 shows the simulation result when the threshold TH increases from 0.1 to 0.7, which illustrate different level of aggregate abstraction of the BKF. The different level of aggregate abstraction can provide appropriate VKFs for concealing the detail structure of the corresponding BKFs to reduce the complexity and improve comprehension for roles. As shown in Fig. 18, larger TH deriving fewer VKNs can conceal the more detailed structure of BKFs. On the other hand, the smaller TH deriving more VKNs can illustrate the details of BKFs.

In Phase II, the krdeg is a parameter for roles to set the expected concept levels (CLs) of knowledge concepts in VKNs. Fig. 19(a) takes the vkn in Fig. 18(c) as an example. The TH of the corresponding VKF is 0.4 and the knowledge concepts in the VKF can be found in

![](/api/attachments/J5Y6DZAF/fulltext/images/a99118b4003a4488fa80380e7cbb66d90050e0910787d849d8f482a03b8d80db.jpg)  
Fig. 16. Information of sourcing department manager role.

<table><tr><td>Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge flows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018</td></tr></table>

D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/J5Y6DZAF/fulltext/images/019b86ce5b151d1751deacb8c6bc7f9f0e9c787400945ce8146f2ec899f5f3e0.jpg)  
Fig. 17. Role-based VKF for sourcing department manager role

Fig. 14. Following the algorithm in Fig. 9 to perform knowledge concept abstraction, the Fig. 19(b), (c) and (d) demonstrate the result of knowledge concepts abstraction for vkn when krdeg is set to 1.0, 0.8 and 0.6 for all knowledge categories respectively, which means no abstraction, one-level up abstraction and two-level up abstraction. Because the concept level re<sup>fl</sup>ects the granularity of knowledge concepts, the concept levels of knowledge concepts increases while krdeg increases, which means that the knowledge concepts are more speci<sup>fi</sup>c. Thus, roles can select the smaller krdeg to obtain more general knowledge concepts to communicate with other teammates or they can select the larger krdeg to get more speci<sup>fi</sup>c knowledge concepts to perform their operations. Based on the investigation of the simulations, the parameters TH in Phase I and krdeg in Phase II serve different purposes and they are set by KF designers and roles according to their requirements.

## 7.2. Feasibility evaluation and implications

To investigate the feasibility of the role-based KFV model, a preliminary analysis was conducted. We illustrated the case of mobile phone development and provided system design-related documents to several professionals to ask for their opinions about the feasibility of the proposed model from a practical perspective. Overall, there was general agreement that it is justi<sup>fi</sup>ed and feasible to realize the role-based KFV model in organizations. According to their opinions on system implementation, the provided system architecture and activity diagram can be the base to conduct detailed system design for building functional speci<sup>fi</sup>cations as well as for implementation.

Moreover, these interviewees highlighted that a role-based KFV system tends to evolve in a longitudinal process. The proposed approaches heavily rely on the knowledge of domain experts, KF designers and roles while building KFs and virtual KFs. People put their knowledge in pro-<sup>fi</sup>les and estimate related parameters while realizing the model, but their experience and knowledge is implicit and hard to obtain systematically. Hence, the back-and-forth between system evaluation and parameter adjustment is necessary for obtaining a well-run system; it will not be trivial work and needs lots of time and effort. From the industrial professionals' perspective, pro<sup>fi</sup>le setting and parameter estimation according to people' opinions is a common practice for implementing IT systems, especially in design and pilot run phases.

![](/api/attachments/J5Y6DZAF/fulltext/images/8f083ef9de168573e06ae0365b85f8d858e46f1c4659c7a56a26639d82ed681d.jpg)  
Fig. 18. Simulation result of different TH (the larger TH obtains fewer VKNs).

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

D.-R. Liu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/J5Y6DZAF/fulltext/images/0466967b0d22916577339747f9b8f4521355c9a18035340e19c5c366eacb8e51.jpg)  
(b) vkn2 with knowledge concepts abstraction under krdeg = 1.0  
Fig. 19. Abstract knowledge concepts under different krdeg.

Practical implications are obtained from the preliminary analysis. These experts recognized the business value of the role-based KFV model because it enhances the ef<sup>fi</sup>ciency of knowledge <sup>fl</sup>ow usage and the effectiveness of knowledge sharing and support in organizations. We summarize practical bene<sup>fi</sup>ts as follows: (1) the role-based VKFs show roles with a full picture of knowledge-needs by presenting corresponding knowledge concepts with proper concept levels; (2) workers can describe their knowledge-needs precisely by krdeg and TH and gain a consensus quickly in teams by common domain ontology; (3) KF designers can avoid complex and time-consuming tasks of estimating parameters for each different role; (4) the iterative evaluation and adjustment approach can <sup>fi</sup>ne-tune the <sup>fi</sup>tness level of VKFs to increase roles' satisfaction; and (5) the proposed model facilitates organizational knowledge support platforms to help teams improve their communication quality and increase members' productivity.

For a new discipline or a new research topic, theoretical papers are required to explore the basic theory by illustrating term de<sup>fi</sup>nitions and establishing relationships between concepts [7,12]. In order to explore the new topic, knowledge <sup>fl</sup>ow view, this work is targeted as a theoretical paper to establish the role-based KFV model and extend knowledge <sup>fl</sup>ow research to cooperative teams for organizational knowledge support. It is an originative study addressing an important extension of knowledge <sup>fl</sup>ow research, which considers a phenomenon that workers in teams usually have different knowledge-needs to support task execution according to their individual roles and task functions. We summarize the theoretical contributions in the knowledge <sup>fl</sup>ow research <sup>fi</sup>eld as follows: (1) de<sup>fi</sup>ne a formal role-based KFV model to illustrate virtual knowledge <sup>fl</sup>ows; (2) design a kernel approach to derive role-based VKFs from a BKF in role and operation perspectives to extend the application of knowledge <sup>fl</sup>ow to teamwork environments; (3) adopt the role-operation krdeg pro<sup>fi</sup>le to accurately illustrate workers' knowledge-needs and effectively facilitate knowledge concept abstraction; (4) employ role-operation relevance to systematically generate VKNs and (5) establish a role-based KFV system architecture as the base of system implementation.

## 8. Conclusions and future work

Through knowledge <sup>fl</sup>ows (KF), organizations can provide workers with task-relevant knowledge to meet their knowledge-needs. In teamwork environments, knowledge workers with different roles and task functions usually have different knowledge-needs; however conventional KF models do not adapt KFs to satisfy the different knowledge-needs of individuals or team workers. In our previous work, we proposed a novel concept and theoretical model called the knowledge <sup>fl</sup>ow view (KFV) model. Based on a worker's speci<sup>fi</sup>c knowledge-needs, the KFV model abstracts the knowledge nodes of a partial knowledge <sup>fl</sup>ow to generate virtual knowledge nodes through knowledge concept generalization.

In this work, we extended the KFV model to discover role-based virtual knowledge <sup>fl</sup>ows (VKF). The knowledge-needs of workers in a team may vary because they have different roles when they execute tasks. The role-based KFV model examines the worker's knowledge-needs in terms of his/her role. Discovering role-based VKFs involves two phases: identifying role-relevant virtual knowledge nodes (VKNs) is Phase I and deriving the knowledge concepts of VKNs is Phase II. A role-based VKF comprises a set of VKNs, which are generated from the base knowledge nodes (BKNs) in Phase I according to the relevance degrees between these BKNs and the role. The relevance degrees can be obtained through base knowledge node pro<sup>fi</sup>les and role-operation relevance pro<sup>fi</sup>les. Based on the relevance degrees, we proposed procedures for generating appropriate role-based VKFs for different organizational roles. Once the accumulated relevance degree of the aggregated BKNs reaches a certain threshold TH, a VKN is identi<sup>fi</sup>ed for the role. Then, KF designers can derive the knowledge concepts of the VKN in Phase II based on the role's knowledge requirement level. The approach adjusts (generalizes) the knowledge concepts of VKNs to the appropriate concept levels based on the operation required KCS pro<sup>fi</sup>les and the role-operation krdeg pro<sup>fi</sup>les.

The role-based VKFs are essential for teamwork because they provide effective knowledge support for team members who are engaged in knowledge-intensive tasks within organizations. This paper is valuable in regard to enhancing knowledge <sup>fl</sup>ow's ef<sup>fi</sup>ciency and increasing the effectiveness of knowledge support through: (1) building the rolebased KFV model and illustrating its innovative concepts, (2) undertaking a case analysis and conducting simulation by examples to validate the model's feasibility in a preliminary manner, and (3) conducting elementary system design to further support system implementation.

One limitation of this work is the lack of a rigorous validation for the proposed model by system implementation. Developing a role-based KFV system is an interesting and valuable research direction. However, constructing a system is very complex and dif<sup>fi</sup>cult to control due to an organization's culture, peripheral system accommodation and operational context [7]. A well-running role-based KFV system also tends to take place in longitudinal processes and needs to adjust parameters and <sup>fi</sup>ne-tune methodologies. Consequently, we completed the basic system design in this work and we are going to conduct a detailed system design and implementation, which can rigorously validate the role-based KFV model and the proposed approaches. Furthermore, we have not addressed the issue of generating VKFs in the context of work<sup>fl</sup>ow or process environments. A BKF may be modeled in accordance with a process to provide needed knowledge to perform a task. It would be interesting to investigate the interactions between a BKF and a process. Our future work will consider the discovery of rolebased VKFs in a process context and explore the synergy between role-based VKFs and process views.

## Acknowledgements

This research was supported by the National Science Council of Taiwan under grant no. NSC 99-2410-H-009-034-MY3.

## References

[1] A. Abecker, A. Bernardi, K. Hinkelmann, O. Kuhn, M. Sintek, Context-aware, proactive delivery of task-speci<sup>fi</sup>c information: the knowmore project, Information Systems Frontiers 2 (3) (2000) 253–276.

[2] H.J. Ahn, H.J. Lee, K. Cho, S.J. Park, Utilizing knowledge context in virtual collaborative work, Decision Support Systems 39 (4) (2005) 563–582.

[3] A. Anjewierden, R. de Hoog, R. Brussee, L. E<sup>fi</sup>mova, Detecting knowledge <sup>fl</sup>ows in weblogs, Proceedings of the Thirteenth International Conference on Conceptual Structures, Atlanta, 2005, pp. 1–12.

[4] U.M. Borghoff, R. Pareschi, Information technology for knowledge management, Journal of Universal Computer Science 3 (8) (1997) 835–842.

[5] C. Chandra, A. Tumanyan, Organization and problem ontology for supply chain information support system, Data & Knowledge Engineering 61 (2) (2007) 263–280.

[6] Y.-J. Chen, Development of a method for ontology-based empirical knowledge representation and reasoning, Decision Support Systems 50 (1) (2010) 1–20.

[7] D.T. Croasdell, M. Jennex, Z. Yu, T. Christianson, M. Chakradeo, W. Makdum, A meta-analysis of methodologies for research in knowledge management, organizational learning and organizational memory: <sup>fi</sup>ve years at HICSS, Proceedings of the 36th Annual Hawaji International Conference on System Sciences 2003

[8] T.H. Davenport, D.W.D. Long, M.C. Beers, Successful knowledge management projects, Sloan Management Review 39 (2) (1998) 43–57.

[9] T.C. Du, F. Li, I. King, Managing knowledge on the Web — extracting ontology from HTML Web, Decision Support Systems 47 (4) (2009) 319–331.

[10] D. Georgakopoulos, M. Hornick, A. Sheth, An overview of work<sup>fl</sup>ow management: from process modeling to workflow automation infrastructure, Distributed and Parallel Databases 3 (2) (1995) 119–153.

[11] T.R. Gruber, A translation approach to portable ontology speci<sup>fi</sup>cations, Knowledge Acquisition 5 (2) (1993) 199–220.

[12] Z. Guo, J. Shef<sup>fi</sup>eld, A paradigmatic and methodological examination of knowledge management research: 2000 to 2004, Decision Support Systems 44 (3) (2008) 673–688.

[13] H. Holz, H. Maus, A. Bernardi, O. Rostanin, A lightweight approach for proactive, task-speci<sup>fi</sup>c information delivery, Proceedings of the 5th International Conference on Knowledge Management (I-Know), Graz, Austria, 2005, pp. 413–420.

[14] S. Kim, H. Hwang, E. Suh, A process-based approach to knowledge-<sup>fl</sup>ow analysis: a case study of a manufacturing <sup>fi</sup>rm, Knowledge and Process Management 10 (4) (2003) 260–276

[15] M.M. Kwan, P. Balasubramanian, KnowledgeScope: managing knowledge in context, Decision Support Systems 35 (4) (2003) 467–486.

[16] C.-H. Lai, D.-R. Liu, Integrating knowledge <sup>fl</sup>ow mining and collaborative <sup>fi</sup>ltering to support document recommendation, Journal of Systems and Software 82 (12) (2009) 2023–2037.

[17] F. Leymann, W. Altenhuber, Managing business processes as an information resource, IBM Systems Journal 33 (2) (1994) 326–348

[18] S.-T. Li, H.-C. Hsieh, Managing operation knowledge for the metal industry, Journal of Universal Computer Science 9 (6) (2003) 472–480.

[19] C.-W. Lin, D.-R. Liu, H.-F. Chen, Modeling knowledge-<sup>fl</sup>ow view for knowledge support in teamwork, Proceedings of the 21st IASTED International Conference on Modelling and Simulation, Banff, Alberta, Canada, 2010.

[20] D.-R. Liu, C.-H. Lai, Mining group-based knowledge <sup>fl</sup>ows for sharing task knowledge, Decision Support Systems 50 (2) (2011) 370–386.

[21] D.-R. Liu, C.-W. Lin, Modeling the knowledge-<sup>fl</sup>ow view for collaborative knowledge support, Knowledge-Based Systems 31 (2012) 41–54.

[22] D.-R. Liu, M. Shen, Work<sup>fl</sup>ow modeling for virtual processes: an order-preserving process-view approach, Information Systems 28 (6) (2003) 505–532.

[24] D.-R. Liu, I.-C. Wu, Collaborative relevance assessment for task-based knowledge support, Decision Support Systems 44 (2) (2008) 524–543.

[25] D.-R. Liu, I.-C. Wu, K.-S. Yang, Task-based k-support system: disseminating and sharing task-relevant knowledge, Expert Systems with Applications 29 (2) (2005) 408–423.

[26] X. Luo, Q. Hu, W. Xu, Z. Yu, Discovery of textual knowledge <sup>fl</sup>ow based on the management of knowledge maps, Concurrency and Computation: Practice and Experience 20 (15) (2008) 1791–1806.

[27] A. Öhgren, K. Sandkuhl, Towards a methodology for ontology development in small and medium-sized enterprises, IADIS Conference on Applied Computing, Algarve, Portugal, 2005.

[28] Á.E. Prieto, A. Lozano-Tello, Use of ontologies as representation support of work<sup>fl</sup>ows oriented to administrative management, Journal of Network and Systems Management 17 (3) (2009) 309–325.

[29] T.S. Raghu, A. Vinze, A business process context for knowledge management Decision Support Systems 43 (3) (2007) 1062–1079.

[30] O.M. Rodríguez, A.I. Martínez, J. Favela, A. Vizcaíno, M. Piattini, Understanding and supporting knowledge <sup>fl</sup>ows in a community of software developers, 10th Collaboration Researchers International Working Group (CRIWG) Conference, San Carlos, Costa Rica, 2004, pp. 52–66.

[31] V. Sambamurthy, M. Subramani, Special issue on information technologies and knowledge management, MIS Ouarterly 29 (1) (2005) 1–7

[32] S. Sarnikar, J.L. Zhao, Automating knowledge <sup>fl</sup>ows by integrating work<sup>fl</sup>ow and knowledge discovery techniques, Proceedings of the 2007 Winter Conference on Business Intelligence, Salt Lake City, UT, 2007.

[33] S. Sarnikar, J. Zhao, Pattern-based knowledge work<sup>fl</sup>ow automation: concepts and issues, Information Systems and E-Business Management 6 (4) (2008) 385–402.

[34] M. Shen, D.-R. Liu, Discovering role-relevant process-views for disseminating process knowledge, Expert Systems with Applications 26 (3) (2004) 301–310.

[35] Z.S. Syed, T. Finin, A. Joshi, Wikipedia as an ontology for describing documents, Proceedings of the Second International Conference on Weblogs and Social Media, Seattle, Washington, 2008.

[36] M. Uschold, M. Gruninger, Ontologies: principles, methods and applications, Knowledge Engineering Review 11 (2) (1996) 93-136

[37] M. Uschold, M. King, Towards a methodology for building ontologies, Proceedings of the International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI), 1995.

[38] A.J.M.M. Weijters, W.M.P. van der Aalst, Process mining: discovering work<sup>fl</sup>ow models from event-based data, Proceedings of the 13th Belgium–Netherlands Conference on Arti<sup>fi</sup>cial Intelligence (BNAIC 2001), 2001.

[39] I.-C. Wu, D.-R. Liu, W.-H. Chen, Task-stage knowledge support: coupling user information needs with stage identi<sup>fi</sup>cation, IEEE International Conference on Information Reuse and Integration (IRI), 2005, pp. 19–24.

[40] M.H. Zack, Managing codi<sup>fi</sup>ed knowledge, Sloan Management Review 40 (4) (1999) 45–58.

[41] Z. Zhang, Z. Yang, Q. Liu, Modeling knowledge <sup>fl</sup>ow using Petri Net, IEEE International Symposium on Knowledge Acquisition and Modeling Workshop, China, 2008, pp. 142–146.

[42] W. Zhao, W. Dai, Integrated modeling of business processes and knowledge <sup>fl</sup>ow based on RAD, IEEE International Symposium on Knowledge Acquisition and Modeling Workshop, China, 2008, pp. 49–53.

[43] J.L. Zhao, H.H. Bi, H. Chen, D.D. Zeng, C. Lin, M. Chau, Process-driven collaboration support for intra-agency crime analysis, Decision Support Systems 41 (3) (2006) 616-633.

[44] H. Zhuge, Knowledge <sup>fl</sup>ow management for distributed team software development, Knowledge-Based Systems 15 (8) (2002) 465–471.

[45] H. Zhuge, A knowledge <sup>fl</sup>ow model for peer-to-peer team knowledge sharing and management, Expert Systems with Applications 23 (1) (2002) 23–30.

Please cite this article as: D.-R. Liu, et al., Discovering role-based virtual knowledge <sup>fl</sup>ows for organizational knowledge support, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2012.11.018

[46] H. Zhuge, Discovery of knowledge <sup>fl</sup>ow in science, Communications of the ACM 49 (5) (2006) 101–107.

[47] H. Zhuge, Knowledge <sup>fl</sup>ow network planning and simulation, Decision Support Systems 42 (2) (2006) 571–592.

[48] H. Zhuge, W. Guo, Virtual knowledge service market — for effective knowledge <sup>fl</sup>ow within knowledge grid, Journal of Systems and Software 80 (11) (2007) 1833–1842.

Dr. Duen-Ren Liu is a professor of the Institute of Information Management at the National Chiao Tung University of Taiwan. He received the BS and MS degrees in Computer Science from the National Taiwan University and his PhD in Computer Science from the University of Minnesota. His research interests include information systems, knowledge engineering and management, work<sup>fl</sup>ow systems, electronic commerce and recommende systems.

Dr. Chih-Wei Lin received his PhD degree in Information Management from National Chiao Tung University in 2012. His research interests include knowledge management, work<sup>fl</sup>ow management systems, and electronic commerce.

Hui-Fang Chen is a PhD student of the Institute of Information Management at the National Chiao Tung University of Taiwan. She received the MS degree in Information Management from the National Chiao Tung University. Her research interests include information systems, knowledge management, and recommender systems.
