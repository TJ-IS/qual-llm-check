---
otero_id: 17259
otero_key: "VDRF6HD2"
title: "A framework for supporting distributed group decision-making"
authors: "Varghese S. Jacob; Hasan Pirkul"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90034-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for supporting distributed group decision-making

Varghese S. Jacob and Hasan Pirkul

College of Business, The Ohio State University, Columbus, OH 43210, USA

Group decision support systems (GDSS) have been proposed as tools for aiding the group decision making process. Research in GDSS has focused primarily on facilitating group meetings. However, meetings form only one aspect of the group decision problem solving process. In fact it is desirable to reduce the number of meetings, especially if the group members are in geographically distant locations. The need for meetings can be reduced if the group is provided with a system which will allow the group members to exchange information and expertise on a continuous basis rather than only during meetings. In this paper we propose a framework for such a system which we designate a distributed group decision support system (DGDSS). The DGDSS works in conjunction with an organizational information system composed of a network of knowledge based systems. This network is utilized to support information and expertise exchange between group members on a continuous basis.

Keywords: Expertise sharing, Group decision support systems, Knowledge, Networked knowledge-based systems.

![](/api/attachments/VDRF6HD2/fulltext/images/f3107fcba74b06225591974173765673517e845489a39e94a39346bafb7c4841.jpg)

Varghese S. Jacob is an Assistant Professor of Management Information Systems at The Ohio State University. He received his Ph.D. in Management, majoring in Management Information Systems, from Purdue University in 1986. His research interests are in artificial intelligence, distributed processing, decision support systems, decision theory and economics. His publications include articles which have either appeared or will appear in Interfaces, Information and Manage-

ment, Computer Science in Economics and Management, IEEE Transactions on Systems, Man and Cybernetics, and Journal of Economic Dynamics and Control. He is a member of The Institute of Management Science, IEEE Computer Society, Association of Computing Machinery, American Association of Artificial Intelligence and Decision Sciences Institute.

## 1. Introduction

A decision-making group has been defined $[6]$ as two or more people jointly responsible for detecting a problem, elaborating on the nature of the problem, generating possible solutions, evaluating potential solutions, or formulating strategies for implementing solutions. In other words, the group is engaged in the decision process together, as opposed to an individual engaged in the process. Since decision support systems (DSSs) were proposed to aid an individual in decision-making, a natural extension of the concept is to develop DSSs to support groups. A DSS designed to aid group decision making has been defined as a group decision support system (GDSS).

A key factor in group decision making which is absent in individual decision making is the need for interaction between the group members during the decision making process. This has led researchers to focus on communication or informa-

![](/api/attachments/VDRF6HD2/fulltext/images/097ea069693d321e25a9b6af2ccc068374ecf69269c016fcec397fd6eb075b91.jpg)

Hasan Pirkul is Professor of Management Information Systems at The Ohio State University where he is the Director of the Management Information Systems program. He received the M.S. degree in Management Science and the Ph.D. degree in Computers and Information Systems from the Graduate School of Management, University of Rochester. His research interests are in the areas of distributed computer systems, telecommunication networks, knowledge based systems, decision support systems and mathematical programming. He has published in various journals including Management Science, Computers & Operations Research, Decision Sciences, Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Computers, IEEE Transactions on Communications, IEEE Transactions on Systems, Man, and Cybernetics, IIE Transactions, Information Systems, Mathematical Programming, and Naval Research Logistics. He is an Associate Editor of Operations Research. He is also a member of the Editorial Boards of Accounting Review, Computers & Operations Research, Information Resources Management Journal, and Journal of Microcomputer Systems Management. Dr. Pirkul is a member of ACM, IEEE, IEEE Computer Society, TIMS, ORSA, Information Resources Management Association and Regional Science Association.

tion exchange issues during group meetings in the design of GDSSs. The degree to which a GDSS facilitates the communication or information exchange has been used by DeSanctis and Gallupe [6] to classify GDSSs. As a result of the focus on facilitating the information exchange during group meetings, another key factor in group problem solving, information exchange and expertise sharing between group members outside of meetings, has not received much attention.

The need for expertise sharing between members could arise due to several factors. For example, a group member might need the expertise of another group member to interpret or solve a component of the decision problem before he/she can make a meaningful attempt at understanding or solving the overall problem. Another situation in which interaction is necessary is when a complex problem is decomposed into sub-problems, each of which is solved by an individual within the group. In such a situation there could be interaction between the sub-problems which requires group members to interact before finally integrating the results.

The computer support system available to the group members should facilitate exchange of information and expertise both within meetings as well as outside of meetings. This system should have several fundamental features which are based on the nature of groups within an organization. First, individuals within an organization can belong simultaneously to multiple groups dealing with different issues. Therefore, the GDSS would have to provide continuous support for the individual tailored for each group and the problem it is solving. Second, groups are constantly being created and disbanded. Largely due to this, researchers in the past have argued that a problem specific GDSS is not practical since it loses its usefulness once the problem is solved $[12]$ . However, knowledge about the problem domain is a key factor in the decision process. Therefore, the GDSS framework should be flexible enough to support the group members with domain knowledge in different problem domains.

In this paper we present a framework for a system which contains both of the features outlined above. We call this system a distributed group decision support system (DGDSS). The DGDSS works in conjunction with an organizational information system composed of a network of knowledge based systems. The networked knowledge based system provides the links necessary to support interaction between the group members on a continuous basis. The use of such a network to support group decision making was first proposed in Jacob and Pirkul [14]. Here we further develop and formalize this idea by specifying the conditions under which a DGDSS can interact and utilize the networked knowledge based systems to provide group members with problem specific support. It should be noted that the concepts discussed in this paper are not intended to replace nor are they proposed as alternatives to the features proposed in the literature [6] for GDSS. As such the paper does not deal in detail with traditional GDSS issues.

The paper is structured as follows; In Section 2 we discuss some features of group decision making which are not adequately captured in conventional GDSS. The DGDSS framework to support these features is outlined in Section 3. Section 4 discusses the knowledge necessary for the networked knowledge based system and the DGDSS to support the problem solving activity. The interaction between the DGDSS and the networked knowledge based system is demonstrated through an example in Section 5. Section 6 summarizes the paper.

## 2. Group decision making

Within an organization a group is formed to work on a decision problem and it is disbanded when the problem is solved. As a result of which, the type of decision problem dealt with by a group, the group composition, the location of group members, and the characteristics of the members would vary from group to group. The need and cost of having group meetings is determined to a large extent by the above factors. One way to make the meetings productive is to have group decision support systems with features such as those proposed by DeSanctis and Gallupe [6]. However, these features are specified within the context of meetings. Although it may not be feasible or advisable to eliminate meetings, one would like to minimize them [12], a primary reason for this being cost.

A meeting generally accomplishes several things which could possibly be accomplished without the meeting if a good computer support system was in place. For example, a face to face meeting may be necessary when group members engage in negotiations or brainstorming. On the other hand in the absence of a computer system which provides continuous support to the members, a meeting may have to be called purely for the purposes of sharing information derived from the expertise of the individuals within the group. Therefore, one of the features we visualize for a GDSS is the ability to permit group members to access requisite data and expertise from each other without calling for a meeting.

An alternative to a meeting is the direct communication between two group members. This communication can take place in one of several ways. Let us suppose for the moment that group member x requires the expertise of group member y. Group member x can use the telephone and call group member y, however there is no guarantee that y will indeed talk to x at that instant either because he/she is not in, or is busy. This can lead to a cycle of x and y calling each other back and forth until one of them finally gets in touch with the other on the phone. Alternatively, x can send y written or electronic messages the response to which would be delayed until y found time to respond. It is also possible that y may not want x to have the information which he/she seeks, causing y to procrastinate or ignore x's messages. A problem with using messages as a communication framework is its non-interactive nature which can cause delays in the solution of the decision problem. The problem becomes much more acute when y's expertise forms the core on which a number of the other group members are dependent. The issue of y providing consistent answers to the queries of each of the group members is also a factor affecting the overall solution process.

One of the keys, therefore, for effective and efficient group problem solving is to provide group members access to each others expertise by creating a GDSS with an expert system base containing expertise corresponding to those of the members. This will allow the group member who needs the expertise to access the expert system interactively. Additionally it relieves the group members from performing tasks which they might ordinarily have to perform for others in the group. Although there are advantages to designing a GDSS with expertise, it may be impractical to implement due to groups having short lives. Additionally an individual in an organization could be in several groups with different facets of his expertise needed in the different groups. Thus, the creation of a group decision support system to solve a problem on a one time basis might not be viable.

![](/api/attachments/VDRF6HD2/fulltext/images/6490a4ba3cda8be9c41cb10b709e247af47e4b121c4360449101971382b4742e.jpg)  
Fig. 1. Computer support for group decision problem solving.

We overcome the above problem by considering group decision making within the larger framework in which the group exists namely, the organization. The organization members are assumed to be supported in their decision process by knowledge based systems which are networked together $[13]$ . The distributed GDSS is effectively a GDSS which has the capability to interact with the networked knowledge based system (Fig. 1). The DGDSS has knowledge about the nodes within the networked knowledge base system. It is this knowledge which provides the interface between the networked knowledge based system and the DGDSS and allows the DGDSS to be flexible enough to support several groups simultaneously. In the next section we discuss the features of the distributed group decision support system and the networked knowledge based system.

## 3. Distributed group decision support system

In order to support the group members decision making on an ongoing basis rather than only at meetings, one needs a computer support infrastructure which can be appropriately utilized for the needs of the various groups. We propose a network of knowledge based systems as such an infrastructure. In this section we discuss the structure of the nodes within the network and the structure of the DGDSS.

We view an organization as being composed of a networked collection of human-computer information processors $[10,13]$ . The nodes in the network are either directly or indirectly linked to each other. The computer component of each node has the necessary information on how to communicate with the other nodes in the network. This information alone, however, is not sufficient for problem solving in the networked framework. As will be discussed later, the key to effective utilization of this information is the knowledge about which node can provide the necessary expertise when needed.

The computer component of each node is viewed as having the capabilities that encompass those proposed for decision support systems (DSS) namely, easy utilization of models and data; as well as those proposed for expert systems, that is, heuristic knowledge which can be utilized along with other domain knowledge to make expert level decisions. Thus, the knowledge based system (KBS) as we view it is an integrated DSS-expert system. The integration allows the expert system to access models and data through the DSS and then interpret the results or utilize the results of the models to perform other heuristic computations for solving a decision problem.

The knowledge based system, therefore, serves two functions; it functions as a DSS for the human at the node and as an expert for all other nodes which consult it for specialized advice. As a DSS it assists the human decision-maker at the node by providing access to the various models, data and information (including expertise) from other nodes required by the decision-maker. As an expert system it provides expert level solutions comparable to that of the human at the node for other members (nodes) of the organization. The expert system also has access to the DSS capabilities at the node and can access the same information the human expert could using the DSS.

The knowledge based system as described is an extension to the DSS framework proposed by Sprague and Carlson [16] and is consistent with the approach taken by Turban and Watkins [17] (also see Turban [18] and Goul, Shane and Tonge [7]). An alternative approach has been proposed by Holsapple and Whinston [11]. They argue that both the DSS view as advocated by Sprague and Carlson and an expert system can be viewed as special cases of the generic DSS proposed by Bonczek, Holsapple and Whinston [1]. Although the KBS as visualized by us can be viewed as a special case of the DSS framework proposed by Bonczek et al., a key difference between the earlier approaches [2,7,10,11,17] and ours is the form of the expertise present at each node. The earlier approaches viewed the expertise at a node as that necessary to aid the human at the node in problem solving, while we view it as necessary for the problem solving efforts of others.

The networked KBS can be used to provide the group members with continuous decision support. In the networked KBS each node typically has knowledge about other nodes with which it interacts under normal organizational conditions. This knowledge, as we will show in Section 4, may not be sufficient to handle the specific requirements of the group. Therefore, at the time a specific group is formed the knowledge that is available in the networked KBS is augmented to suit the needs of the group. The knowledge then is stored in the knowledge system of the DGDSS as a particular group's knowledge base. It is this knowledge which provides the DGDSS with problem and group specific features. One aspect of the knowledge in the DGDSS relates to the information about the domain knowledge of the group members, this knowledge facilitates the interaction of the DGDSS with the nodes in the network. A group member can then sign on to the DGDSS by specifying the group he/she is in. The DGDSS would use its knowledge about the nodes in the network to aid him/her on the specific group problem. One advantage of this framework is that once a group is disbanded the knowledge associated with that group can be discarded without affecting the networked KBS or the DGDSS.

A DGDSS can be visualized within the DSS structure proposed by Bonczek, Holsapple and Whinston [1]. A DGDSS contains a language system, a problem processing system which we will call the group problem processing system and a knowledge system which we will call the group knowledge system (Fig. 2). The group problem processing and group knowledge system are designed with a generic group's needs in mind and can then be tailored to meet the needs of specific groups.

The language system has been defined as containing the total of all linguistic facilities made available to a decision maker by the DSS [1]. Thus, it is characterized by the syntax it makes available to the decision maker to interact with the DSS. The language system in the DGDSS performs a similar activity and allows a user to interact with the DGDSS.

<table><tr><td>USER</td><td>Language System</td><td>Group Problem Processing System</td><td>Group Knowledge System Group Domain and Interaction Knowledge</td></tr></table>

Fig. 2. A distributed group decision support system.

The group knowledge system contains the knowledge necessary for the group to function. We will consider the knowledge system in detail in Section 4.2. It should be noted here that the knowledge system of a DGDSS needs to contain knowledge to support the groups activities. The generic knowledge would include features generally associated with a GDSS. Procedures such as the parliamentary procedure, the Delphi technique, nominal technique, preference weighing schemes etc. are examples of such features. A specific group could abstract from this generic list those specific features needed for its operation. In addition to these generic group based features, one needs domain knowledge pertaining to the problem dealt with by the group. This domain knowledge is the collective domain knowledge of the group and is available in the networked KBS. The DGDSS, therefore, maintains knowledge about the domain knowledge of the group members and how to access it from the network. As a result of this, the domain knowledge of the group members is not duplicated in the DGDSS.

The group problem processing system provides the interface between the language system and the group knowledge system. It is responsible for activities such as inference, maintaining the knowledge, interpreting the group members requests coming from the language system, and using the knowledge system to respond to the requests. It is also responsible for aiding the group in the creation of problem and group specific knowledge.

Knowledge forms the central core on which both the networked knowledge base system and the DGDSS operate. In the next section we discuss the form of the knowledge in the nodes of the network and the DGDSS.

## 4. Knowledge in a distributed group decision support system

Since both the distributed group decision support system and the networked knowledge based system are required to support the group's problem solving efforts, in this section we discuss the knowledge necessary in each component to facilitate problem solving and interaction between the components.

## 4.1. Knowledge in the networked KBS

Knowledge in the expert system literature has meant domain knowledge. The definitions of knowledge also tend to reflect this bias. For example, Hayes-Roth [8] has defined knowledge along three dimensions, (1) scope of knowledge, ranging from general to specific; (2) purpose of knowledge, ranging from descriptive to prescriptive; (3) validity of knowledge, ranging from certain to uncertain. It is evident from the discussion of the dimensions in Hayes-Roth [8] that the knowledge which is considered is problem domain specific and pertains purely to solving problems within the domain with no external requirements. Within an organizational setting the knowledge described by Hayes-Roth can essentially be viewed as the three dimensions of one component of knowledge, the problem domain specific knowledge. While constructing knowledge based systems, this knowledge may be organized in several levels. The lowest level would be the domain knowledge which refers to objects, events and actions. Meta-knowledge, which is on a higher level, is knowledge about the domain knowledge, i.e., it is involved in deciding the appropriate domain knowledge to apply in a given situation [3]. Meta-meta-knowledge is the control knowledge about the meta-knowledge [19].

Holsapple and Whinston [10] propose several components for knowledge:

1. Descriptive knowledge - relates to data and information about the problem solving environment;

2. Procedural knowledge - specifies the steps necessary to achieve certain tasks;

3. Reasoning knowledge - specifies what conclusions can be drawn given the existence of certain situations;

4. Derived knowledge - knowledge which may be derived by using other components of knowledge and may itself actually belong to other components if it is kept;

5. Linguistic knowledge - concerned with the syntax and semantics of the languages used in the organization or problem domains;

6. Presentation knowledge - pertains to how knowledge should be disclosed; and

7. Assimilative knowledge - knowledge about what new knowledge to accept from external sources.

The various categories of knowledge could be broadly classified as domain knowledge (descriptive, procedural, reasoning, derived) and interaction knowledge (linguistic, presentation and assimilative).

In addition to the above components of knowledge we propose two other components which can also be considered to belong to the category of interaction knowledge. Clearly, in addition to domain knowledge and the interaction knowledge considered above, human information processors typically have the following knowledge:

(a) What information lies outside their area of expertise but has an impact on the problems being solved by them.

(b) From whom to obtain the knowledge or information needed for problem solving if it is not known to them.

The reason why expert systems appear narrow, brittle, or do not gracefully degrade $[15]$ , can be attributed to the absence of the knowledge specified in (a) and (b) above. Jacob and Pirkul $[13]$ have circumvented the problem by specifying a networked KBS with each node having necessary knowledge about the other nodes.

Although knowledge about the domain of expertise is the key ingredient for problem solving within an organizational setting, two other components of knowledge which come into play are: (a) peripheral knowledge and (b) access knowledge. Often a node requires expertise in another domain to generate information or interpret data: Each node, therefore, needs to have knowledge about the other nodes and their expertise, this knowledge is referred to as peripheral knowledge. Access knowledge on the other hand can be viewed as a control feature in that this knowledge specifies which of the other nodes can access one's expertise.

We view knowledge as a four tuple,

$$
K = \langle d, P, A, O I \rangle ,
$$

where d is the domain knowledge, P is the peripheral knowledge, A the access knowledge, and OI is the other interaction knowledge such as linguistic etc. The various components of the domain knowledge can be considered along the three dimensions proposed by Hayes-Roth [8], namely the scope, purpose and validity of knowledge. Thus d is defined by $d(s,p,v)$ . In this paper we will focus on the domain, peripheral and access knowledge. The other interaction knowledge are addressed in Holsapple and Whinston [10].

Definition 1. An organization is viewed as a collection of nodes. The organization is represented as $O = \{w_{1}, \ldots, w_{n}\}$ .

Definition 2. For each node $w_{i} \in \mathbf{O}$ , the domain knowledge is defined as $d_{i}$ .

The domain knowledge $d_{i}$ of $w_{i}, i=1,\ldots,n$ , includes facts or data, models, knowledge about the utilization and interpretation of the results of the models, heuristic knowledge, etc. The domain knowledge of the organization is represented by $D_{O}=\{d_{i},\ldots,d_{n}\}$ .

Definition 3. The expertise of node $w_{i}$ resulting from domain knowledge, $d_{i}$ , is

$$
E _ {i} = \left\{e _ {i 1}, e _ {i 2}, \dots , e _ {i z} \right\},
$$

where $e_{il}, l=1,\ldots,z$ , represents the various categories of information or conclusions $w_{i}$ can generate as a result of being in possession of $d_{i}$ .

In addition to domain knowledge, the individuals within an organization have to know who they can ask for information when they are unable to generate it themselves. This is where peripheral knowledge is utilized. Peripheral knowledge consists of information about the external knowledge which has an impact on the domain of expertise and the node from which the knowledge can be obtained. In considering peripheral knowledge one has to keep in mind three factors. First, more than one node may have the capability to generate the information you seek. Second, which one of the nodes is most likely to generate the information quickly and at a low cost to you. Finally, although one may know that there is an individual who would generate the information being sought, one may not know for sure who it is. Thus the definition of peripheral knowledge includes the probability of obtaining the information from a node.

Definition 4. The peripheral knowledge $P_{b}$ of node $w_{b}$ is defined as

$$
P _ {b} = \left\{\rho_ {e} | \forall e \notin E _ {b} \text {   and   } e \in N _ {b} \text {   and   } \rho_ {e} \notin P _ {b} \right\},
$$

where $N_{b}$ is the set of outside knowledge required by $w_{b}$ for the problem it has to solve, and

$$
\rho_ {e} = \left\{\left(e, w _ {j}, \zeta_ {j}\right) | \forall w _ {j} \in O, j \neq b \right\},
$$

where $\zeta_{j}$ is the likelihood of obtaining the information $e$ from node $w_{j}$ .

Access knowledge has two components, namely, information on who can utilize the expertise possessed by the node and what information is allowed to be accessed.

Definition 5. For $e_{bl} \in E_b$ we define $a_{e_{bl}}^j = 1$ if $w_j$ can access the knowledge $e_{bl}$ . Then the set of all nodes that can access $e_{bl} \in E_b$ is defined as $A_{e_{bl}} = \{w_j | a_{e_{bl}}^j = 1, \forall w_j \in \mathbf{O}, j \neq b\}$ . The access knowledge for node $w_b$ is therefore defined as $A_b = \{A_{e_{bl}} | \forall e_{bl} \in E_b\}$ .

Conversely the access knowledge can also be defined as all the nodes who cannot access information at a particular node. The decision to choose one or the other is based on whether the number of nodes which can access a particular category of information is greater than or less than the number of nodes which cannot. Obviously, it is preferable to implement the framework in which fewer nodes have to be specified. It is therefore possible that a combination of the two approaches could be used in an implementation.

A request for information can be viewed as a mapping from the peripheral knowledge of one node to the access knowledge of another node. Thus if node $w_{j}$ requests information $e_{bl}$ from node $w_{b}$ , the request will be honored only if $w_{j} \in A_{e_{bl}}$ , where $A_{e_{bl}} \in A_{b}$ , the access knowledge of node $w_{b}$ . To fulfill the request however node $w_{b}$ may have to use its domain knowledge i.e. expertise. This information is then communicated back to the requester. If node $w_{j}$ is not allowed to access the information then the request is denied. If the information requested does not belong to the domain knowledge of the node then the message would correspond to that effect. A formal characterization of the above discussion can be specified as follows:

![](/api/attachments/VDRF6HD2/fulltext/images/de511c3f155f030f6e65c609689febd00550c0119e31b30b1c234db8200e935b.jpg)  
Fig. 3. A KBS as an extension of the Sprague and Carlson DSS framework.

Definition 6. A communication action is either (a) A request for information, $e_{bl}$ , from node $w_{j}$ to node $w_{b}$ represented as:

$$
r _ {j} ^ {b}: \left(e _ {b l}, w _ {b}, \zeta_ {j}\right)\rightarrow A _ {e _ {b l}},
$$

where $A_{e_{b}l}\in A_b$ , and $(e,w_b,\zeta_j)\in P_j$ , or (b) A response to request $r_j^b$ represented as

$$
r _ {j} ^ {\prime b} = \left\{ \begin{array}{l l} e _ {b l} & \text { if } w _ {j} \in A _ {e _ {b l}}, \text { where } A _ {e _ {b l}} \in A _ {b} \\ \phi & \text { if } w _ {j} \notin A _ {e b l}, \text { where } A _ {e _ {b l}} \in A _ {b} \\ B & \text { if } w _ {b} \text { is   busy } \\ u & \text { if } e _ {b l} \notin E _ {b}, \end{array} \right.
$$

where $\phi$ corresponds to a denial of the request, B is the busy response and u is response signalling that the information is unknown.

If the response to a request for information is denied then the system should automatically inform the user at the node about the access request which was denied. This provides a control feature in that the human information processor knows that there has been an attempt to utilize information for which there was no prior clearance. Each node within our framework can be visualized as in

![](/api/attachments/VDRF6HD2/fulltext/images/57e3287c3faf3dd4cf0baf58a8089e5c1aff72fe1269179bafaaab44e80061f8.jpg)  
Fig. 4. A KBS within the Bonczek, Holsapple and Whinston DSS framework.

Fig. 3. Within the generic Bonczek et al. [1] view, each node can be visualized as shown in Fig. 4. Once the groups are established the interaction between nodes will be redefined to take into account the groups needs.

As a result of defining peripheral and access knowledge, it is not necessary for more than one processor to analyze the request for information as in the case of the contract net framework [4]. By incorporating peripheral knowledge into each of the nodes, a node which is working on a problem can directly communicate with another node which has the expertise to aid in the solution of the problem at hand. The minimization of human intervention in the process should speed the solution process as well as enhance the reliability of the solution in many situations. The peripheral knowledge is analogous to the concept of acquaintances in the actor model of Hewitt [9]. The actor model approach to distributed decision making systems has been used by Burns et al. [2]. However, here we assume that the actor, i.e., the node knows the likelihood of obtaining the required information from another node.

## 4.2. Knowledge in a DGDSS

Groups are typically formed to solve a decision problem and as such are put together based on the domain knowledge which they can bring together to solve the problem. We can now formally define a group based on the domain knowledge required to solve a decision problem.

Definition 7. Let $D_g$ be the domain knowledge required to solve a decision problem, where $D_g \subseteq D_O$ then node $w_i \in O$ , is a member of group $g$ set up to solve the decision problem, i.e., $w_i \in g$ , iff $d_i \in D_g$ . Thus $g \subseteq O$ .

In general there could be several groups within an organization and some nodes could belong to several of these groups. Let $G = \{g_{1}, \ldots, g_{m}\}$ be the various groups within the organization, where each $g_{i}, i = 1, \ldots, m$ , is such that $g_{i} \subseteq O$ .

The group knowledge system in a DGDSS contains as before two broad categories of knowledge, the group domain knowledge and the group interaction knowledge. The group domain knowledge consists of several different components One of the main components is information about the collective domain knowledge of the group members. As mentioned earlier, the domain knowledge of each group member is available in the networked KBS and is not duplicated by the DGDSS. The information stored in the DGDSS is utilized to access domain knowledge of the group members. This is illustrated by the example presented in Section 5. The group domain knowledge also includes group descriptive knowledge, group procedural knowledge and group derived knowledge. The group descriptive knowledge is the data and information about the problem solving environment. Group procedural knowledge contains procedures necessary to achieve certain group tasks, for example, the voting procedure. Group reasoning knowledge corresponds to what conclusions to draw given certain situations, for example, a tie in voting. Group derived knowledge corresponds to any knowledge the group might have derived using a combination of their domain knowledge.

The group interaction knowledge such as the linguistic, presentation and assimilative knowledge is similar to that proposed for a DSS supporting an individual, however, this knowledge would be tailored to accommodate group interaction. For example, presentation knowledge in the DGDSS would include a framework for tabulation of voting results.

In addition to the above knowledge, as in the networked KBS case, the access rights of group members would have to be established. Corresponding to each group member $w_{j} \in g_{i}$ , the DGDSS maintains access rights along with information about each component of the group member's domain knowledge. These access rights are in addition to the access rights already existing within the organization and are valid only as long as the group exists.

One of the initial steps the group has to deal with is to determine who would be allowed access to one's knowledge. This could be done by the group leader or the person who creates the group. Alternatively, in a democratic group framework, establishing access rights could lead to the need for voting and negotiation. However, once the access rights of the various nodes are decided on, this information is stored along with the information on the domain knowledge of each group member. This access knowledge can be viewed as an extension of the access knowledge already specified in the networked KBS. The access knowledge in the DGDSS is specified as follows:

Definition 8. For any group member $w_{b} \in g_{i}$ and for any $e_{bl}$ required by $w_{j} \in g_{i}$ and $w_{j} \notin A_{e_{bl}}$ , where $A_{e_{bl}}$ is the original access knowledge of $w_{b}$ , we define the access knowledge required for the group problem as: For $e_{bl} \in E_{b}$ let $a_{e_{bl}}^{j} = 1$ if $w_{j}$ can access the knowledge $e_{bl}$ with $w_{j} \in g_{i}$ and $w_{j} \notin A_{e_{bl}}$ . Then the set of all nodes belonging to $g_{i}$ that can access $e_{bl} \in E_{b}$ is defined as

$$
A _ {c _ {b l}} ^ {g _ {i}} = \left\{w _ {j} \mid a _ {e _ {b l}} ^ {j} = 1, \forall w _ {j} \in g _ {i} \right\}.
$$

The access knowledge for node $w_{b}$ is therefore defined as

$$
A _ {b} ^ {g _ {i}} = \left\{A _ {e _ {b l}} ^ {g _ {i}} | \forall e _ {b l} \in E _ {b} \right\}.
$$

The access knowledge for node $w_{b}$ can therefore be viewed as $A_{b} \cup A_{b}^{g_{i}}$ . Communication now can occur directly based on a node's peripheral knowledge or based on the group domain knowledge possessed by the DGDSS. Since the DGDSS has complete domain knowledge about the group members, the peripheral knowledge associated with the DGDSS can be viewed as $P^{g_{i}} = \cup_{\forall w_{j} \in g_{i}} (E_{j}, w_{j})$ .

Definition 9. A communication action is now defined as either (a) A request for information, $e_{bl}$ , from node $w_j$ to node $w_b$ represented as

$$
r _ {j} ^ {b}: \left(e _ {b l}, w _ {b}, \zeta_ {j}\right) \cup P ^ {g _ {i}} \rightarrow A _ {e _ {b l}} \cup A _ {e _ {b l}} ^ {g _ {i}},
$$

where $A_{e_{bl}} \in A_b$ and $A_{e_{bl}}^{g_i} \in A_b^{g_i}$ and $(e, w_b, \zeta_j) \in P_j$ , or (b) A response to request $r_j^b$ represented as

$$
r _ {j} ^ {\prime b} = \left\{ \begin{array}{l l} e _ {b l} & \text { if } w _ {j} \in A _ {e _ {b l}} \cup A _ {e _ {b l}} ^ {g _ {i}}, \\ & \text { where } A _ {e _ {b l}} \cup A _ {e _ {b l}} ^ {g _ {i}} \in A _ {b} \cup A _ {b} ^ {g _ {i}} \\ \phi & \text { if } w _ {j} \notin A _ {e _ {b l}} \cup A _ {e _ {b l}} ^ {g _ {i}}, \\ & \text { where } A _ {e _ {b l}} \cup A _ {e _ {b l}} ^ {g _ {i}} \in A _ {b} \cup A _ {b} ^ {g _ {i}} \\ B & \text { if } w _ {b} \text { is   busy } \\ u & \text { if } e _ {b l} \notin E _ {b}, \end{array} \right.
$$

where, as in Definition 6, $\phi$ corresponds to a denial of the request, B is the busy response and u is the response signalling that the information is unknown.

In defining such a structure several factors become apparent. A group is supported in its meeting and other generic group related activities by the group and interaction knowledge. On the other hand, the problem domain specific activities of the group are supported by the group domain knowledge component which has information about the network. This allows the group members to interact through the networked KBS. The DGDSS maintains group domain and interaction knowledge for each group that is in existence. When a group is disbanded, knowledge corresponding to that group is eliminated.

## 5. An example

In this section an example is used to illustrate the concepts presented in the paper. The example deals with a group studying the feasibility of introducing a new product. For this group a component of the group domain knowledge that is necessary for the DGDSS to interact with the network is presented. The domain, peripheral and access knowledge of one of the group members within the network is also demonstrated.

The knowledge representation scheme used to represent knowledge in both the DGDSS and the KBS is frames [5]. A frame is typically utilized to represent an object or a class of objects. A frame is composed of slots in which the attributes of the object can be specified. One can also specify facets which describe the properties of the attributes within the frame. Another key feature of frames is that one can attach procedures to the frames. For example, KEE [5] uses two forms of procedural attachments called methods and active values. Methods are procedures that respond to messages and are stored as the values of slots that have been identified as message responders. This feature can be utilized both for modifying group membership as well as for responding to messages from the other nodes. Active values are procedures that are invoked when the slot's values are accessed or stored. They are also called demons since they monitor changes and uses of the value. One of the functions served by the demons is to serve as sensors or alarms when necessary.

For each group member, the KBS supporting him/her is considered to be a collection of related frames. At each node the root frame is called the Master frame and contains four categories of information. The first category is the domain knowledge. Under this category the slots are essentially pointers to the subtree of frames making up the domain knowledge. Thus there is a slot for each area of expertise of the node. The second category of information is the access and peripheral knowledge which is incorporated into the frames as facets of the domain knowledge slot. Finally there is the group membership slot which contains information on all the groups the node is a member of.

<table><tr><td colspan="2">Frame: Masterframe in Knowledge Base of Node MM</td></tr><tr><td colspan="2">Expertise Slot: Advertising Budget Analysis</td></tr><tr><td colspan="2">AK: {SM1, SM2, MVP}</td></tr><tr><td colspan="2">PK: {SM1, MAa, MAb, MVP}</td></tr><tr><td colspan="2">Active Values: Update Access Table</td></tr><tr><td colspan="2">Expertise Slot: Target Sales</td></tr><tr><td colspan="2">AK: {SM1, SM2, MVP}</td></tr><tr><td colspan="2">PK: {SM1, MAa, MVP}</td></tr><tr><td colspan="2">Active Values: Update Access Table</td></tr><tr><td colspan="2">Expertise Slot: Production Levels</td></tr><tr><td colspan="2">AK: {SM1, SM2, MVP}</td></tr><tr><td colspan="2">PK: {PM, MVP}</td></tr><tr><td colspan="2">Active Values: Update Access Table</td></tr><tr><td colspan="2">Group Membership Slot: {New Product, Market Analysis}</td></tr><tr><td colspan="2">Update Procedure: Update group forming and disbanding table</td></tr><tr><td colspan="2">SM1 Sales Manager Product 1</td></tr><tr><td colspan="2">SM2 Sales Manager Product 2</td></tr><tr><td colspan="2">MAa Market Analyst a</td></tr><tr><td colspan="2">MAb Market Analyst b</td></tr></table>

Fig. 5. Marketing managers frame.

We use a marketing manager as an example. Fig. 5 illustrates the frame corresponding to him/her. The marketing manager is assumed to perform three functions: setting advertising budgets, setting target sales quotas and advising on production levels based on the sales quotas which have been set. The expertise slots are pointers to frames which contain the domain knowledge. The facets associated with the slot are the following: (a) The access knowledge which represents the nodes which can access the particular domain knowledge is denoted by AK. (b) The peripheral knowledge which specifies the components of the knowledge required from other nodes and the node which it can be obtained from is denoted by PK. (c) Active values, which are a mechanism for updating a table with information on the access requests received. This information is primarily for the human at the node and serves as a control mechanism for monitoring the usage of information under one's control. The names of the group to which one belongs is specified in the group membership slot. The update procedure associated with it performs the update of the membership of the node.

The access and peripheral knowledge associated with the expertise slots are the typical knowledge which is used by the marketing manager in his day to day work. The group membership slot essentially takes a number of values depending on the groups to which the marketing manager belongs. Use of a specific name within the list to communicate with the DGDSS indicates to the DGDSS the appropriate frame to consider within its knowledge base to aid the node.

To illustrate the concept of the group domain knowledge consider the “New Product Group”, which is made up of the marketing vice president (MVP), production vice president (PVP), the marketing manager (MM) for a region, and the plant manager (PM) of the region. The group has been formed to determine the possibility of introducing a new product into the market. In analyzing this decision problem one needs expertise in different areas. For example, the marketing manager’s expertise is needed to analyze the market and predict the demand. The MVP’s expertise is needed to analyze the impact the new product will have on other products manufactured by the company. The PP’s expertise is needed to analyze whether the plant is capable of producing the projected demand. The PVP might be concerned with the implications of demand not meeting the projections and the implications of a cut back on production and whether the product should be manufactured at the plant under consideration or a different one.

Each group within the organization has a collection of frames specifying its unique characteristics. Thus, the New Product Group would have a frame corresponding to its members and the information pertaining to it is illustrated in fig. 6. The information pertaining to each group member is stored within the frame along with the associated access knowledge. This knowledge can be used by the DGDSS to satisfy any requests from the group members pertaining to expertise outside a node's domain. For example, if the PVP needs to know about the projected sales of the new product, he/she would query the DGDSS, which uses its domain knowledge to direct the request to MM.

Frame: Masterframe New Product
Group Member Slot: MVP
ES1: Product Share in Markets
AK1: {PVP}
Group Member Slot: PVP
ES1: New Plant Capabilities
AK1: {MVP, MM, PM}
Group Member Slot: MM
ES1: Advertising Budget Analysis
AK1: {PVP, PM}
ES2: Target Sales
AK2: {PVP, PM}
ES3: Production Levels
AK1: {PVP}

Fig. 6. New product group master frame in DGDSS knowledge system.

Although in the figure we have shown information pertaining purely to group members and their expertise, one could specify other frames under the master frame with information on the name of the group leader, preferred meeting modes, notes on past meetings, future meeting information, etc.

Given the above knowledge representation scheme, one of the activities of the group problem processing system is to access the appropriate frame and route the request from the requester to the appropriate group member who will perform the task.

## 6. Summary

The paper proposes a framework for, distributed group decision support. Such a system would facilitate the exchange of information and expertise between the group members without the need for a meeting or direct communication. This feature could lead to a reduction in the number of meetings and also make the meetings more productive.

The dynamic nature of the distributed group decision support is achieved by viewing an organization as being composed of a network of human-computer information processors. The computer is considered as a knowledge based system which has the capabilities traditionally associated with a DSS as well as those associated with an expert system. Both these capabilities are utilized differently. The DSS capability is primarily for the human at the node. The expert system on the other hand is used by other nodes. This networked KBS is utilized by the DGDSS to support the groups activities. The interaction between the networked KBS and the DGDSS provides a framework for the group members to access relevant problem solving information on a continuous basis rather than only at meetings.

Although several factors need to be considered within an implementation context, in this paper, we have focused on knowledge. We believe this is the most critical factor in designing and implementing a distributed group decision support system.

## References

[1] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, (1981).

[2] A. Burns, M.A. Rathwell and R.C. Thomas, A Distributed Decision-Making System, Decision Support Systems, 3, (1987) 121–131.

[3] R. Davis and B.C. Buchanan, Meta-Level Knowledge: Overview and Applications, Proceedings Fifth International Conference on AI, Cambridge, MA, (1977) 920–927.

[4] R. Davis and R.G. Smith, Negotiation as a Metaphor for Distributed Problem Solving, Artificial Intelligence, 20, (1983) 63–109.

[5] R. Fikes and T. Kehler, The Role of Frame-Based Representation in Reasoning, Communications of the ACM, 28, Nr. 9 (1985) 906–920.

[6] G. DeSanctis and R.B. Gallupe, A Foundation for the Study of Group Decision Support Systems, Management Science, 23, Nr. 5 (1987) 589–609.

[7] M. Goul, B. Shane, and F. Tonge, Use of an Expert Subsystem in Decision Recognition Channeling, paper presented at the 17th Hawaii International Conference on Systems Sciences, Honolulu, (1984) 558–567.

[8] F. Hayes-Roth, The Knowledge-Based Expert System: A Tutorial, IEEE Computer, 17, Nr. 9 (1984) 11–28.

[9] C. Hewitt, Viewing Control Structures as Patterns of Passing Messages, Artificial Intelligence, 8, (1977) 323–364.

[10] C.W. Holsapple and A.B. Whinston, Knowledge-Based Organizations, The Information Society, 5, (1987) 77–90.

[11] C.W. Holsapple and A.B. Whinston, Model Management Issues and Directions, Working Paper No. 7, Kentucky Institute of Knowledge Management, College of Business and Economics, University of Kentucky, Lexington, (1988).

[12] G.P. Huber, Issues in the Design of Group Decision Support Systems MIS Quarterly, September, (1984) 195–204.

[13] V.S. Jacob and H. Pirkul, A Framework for Networked Knowledge Based Systems, IEEE Transactions on Systems Man and Cybernetics, 20, Nr. 1 (1990) 119–127.

[14] V.S. Jacob and H. Pirkul, "A Dynamically Configurable Networked Knowledge-Based System For Group Deci-

sion-Making, Proceedings of the 22nd Hawaii International Conference on System Sciences, (1989) 709–715.

[15] G. Silverman, Should a Manager “Hire” an Expert System?, in Expert Systems for Business, edited by B.C. Silverman, Addison-Wesley, Reading, MA, (1987).

[16] R.H. Sprague and E.D. Carslon, Building Effective Decision Support Systems, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, (1982).

[17] E. Turban and P.R. Watkins, Integrating Expert-Systems

and Decision Support Systems, in Decision Support Systems – Putting Theory into Practice, edited by R.H. Sprague and H.J. Watson, Prentice Hall, Englewood Cliffs, New Jersey, (1988).

[18] E. Turban, Decision Support Systems and Expert Systems Managerial Perspectives, Macmillan Publishing Company, New York, (1988).

[19] B.W. Wah, New Computers for Artificial Intelligence Processing, IEEE Computer, 20, Nr. 1 (1987) 10–15.
