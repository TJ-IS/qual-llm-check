---
otero_id: 15498
otero_key: "B4YSPHWX"
title: "Two-level trust-based decision model for information assurance in a virtual organization"
authors: "Yanjun Zuo; Brajendra Panda"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Two-level trust-based decision model for information assurance in a virtual organization

Yanjun Zuo <sup>a,⁎</sup>, Brajendra Panda

<sup>a</sup> Department of Information Systems and Business Education, University of North Dakota, Grand Forks, ND, USA 58203 <sup>b</sup> Department of Computer Science and Computer Engineering, University of Arkansas, Fayetteville, AR, USA 72701

Received 31 March 2006; received in revised form 19 December 2007; accepted 20 December 2007 Available online 3 January 2008

## Abstract

Like other unstructured decision problems, selection of external trustworthy objects are challenging particularly in a virtual organization (VO). Novel methods are desired to filter out invalid information as well as insecure programs. This paper presents a new, conceptual approach to support selection of objects. It is a two-level decision model, which helps a VO participant determine whether an external object can be accepted based on the object's quality and security features. This hierarchical decision-making process complies with both practical evidence and theoretical decision models. Its underlying concepts are logically sound and comprehensible. We illustrate the approaches using software selection. © 2007 Elsevier B.V. All rights reserved.

Keywords: Decision model; Hierarchical decision-making process; Information assurance; Trust; Virtual organization; Policy rule; Policy specification

## 1. Introduction

A virtual organization represents a loosely coupled community with a set of participants sharing resources based on mutually agreed upon rules. In our discussion, each participant represents an independent computing system associated with a single administrative domain. Each system contains a set of internal applications (see Fig. 1). An internal application performs dedicated functions or provides certain services. Some common features of a VO are: (1) they are self-organized by participants based on mutual interests; (2) they have a large scope spanning over multiple administrative domains; (3) they have dynamic members, i.e., participants join and leave at any time; and (4) they allow resources shared in a controlled and accountable manner. An open source software community is an example of a virtual organization, where thousands of programmers and software engineers voluntarily contribute to developing large-scale software and offer programs they have developed to share with other participants. Such a virtual organization is decentralized and self-organized. In GNUe [8], for example, no company or corporate executive has administrative authority or resource control to determine what work will be done, what the schedule will be, and who will be assigned to perform any of the specified tasks [26]. The participants decide to offer and consume information based on their own needs and criteria. Many other types of VOs exist including peer-to-peer systems, Grid systems, and electronic virtual markets.

A Virtual Organization (VO)  
![](/api/attachments/B4YSPHWX/fulltext/images/8f942d0b43ec799401ff9f4b3ddc23c5ebe9d36941c2314d08c6a249031b81d0.jpg)  
Fig. 1. Architecture of a virtual organization (VO).

Information assurance has become a major concern for many VOs. Low barriers to publishing information in a VO require novel mechanisms to verify the quality and security features of available information before they can be used by a participant. In an open source software community, there are thousands of software freely available for download. The quality of each software varies widely due to the expertise of the software's developers, the software engineering practices those developers use, and the information process culture those developers have. In this paper, we focus on two aspects of information assurance: information quality and security. Information quality refers to the quality of an object, e.g., correctly describes a “thing” or provides a function. For instance, the quality of a software program can be described by its functionality, usability, reliability, etc. If a program has been developed with race condition or deadlock, for example, then that program is considered to have poor quality. If a program produces correct results in a consistent and predictable manner given a full set of well-prepared testing inputs, then it has high quality in term of functionality. Security features of a program refer to its safety and reliability when being executed by users. A program is safe to use if it does not contain malicious code, is free of vulnerabilities, and has no functions beyond its designed specifications.

Our framework addresses the issue of information assurance from the object trust perspective. A user evaluates the quality and security of a program based on how much the program can be trusted from two aspects: (1) whether the program functions correctly, and (2) whether the program is secure and safe for use. The core part of our framework is a two-level decision model developed to assist users in selecting external objects that satisfy the users' requirements for information assurance. As the name implies, a final decision is made based on evaluations at two levels – the system level and the internal application level. As mentioned earlier, a participant of a VO represents an independent system, which contains a set of internal applications providing different functions and services. The two-level decision model separates the specifications of selection criteria between a system and its internal applications. With different focuses and scopes at the two levels, the requirements for information assurance are specified with different degrees of details. The decision at the system level is based on a set of general trust-related attributes for a given type of objects and their respective testing conditions. For instance, for software selection and reuse, a system may define general policy rules based on general attributes related to the software's licenses (not all the open source software is created with the same licenses) and virus detection. These rules, for example, may define that “any software without appropriate licenses can't be selected” and “the software must pass virus detection test.” The goal is to quickly filter or select an object, if possible. The decision rules defined at this level are applied within the entire scope of the system. The decision at the application level, on the other hand, is based on additional or refined trust-related attributes for the given type of objects and their respective testing conditions to further filter and rearrange the objects that have been selected at the system level. For instance, the decision rules at the internal application level may specify, “the software selected to run on a server machine must not have hidden routines to open network connections without system administrator's acknowledgement” and “the software selected to be used as components to build mission-critical projects cannot accept arbitrary-length files as inputs for security reasons.” Any external object must satisfy the requirements defined at both the system and internal application levels in order to be used internally. A flow chart for a high-level view of the proposed decision process is illustrated in Fig. 2.

![](/api/attachments/B4YSPHWX/fulltext/images/2b48c21d1930895021146f2906f4a684ebf5982feae2d17c13c73ba3850b0755.jpg)  
Fig. 2. Flow chart of the two-level decision process.

Throughout this paper, we use open source software selection and reuse as an illustrative example. Although our model focuses on the security and quality features of a given object, it is open to other dimensions. Our major contributions include (1) proposal of a trust-based hierarchical decision model, which focuses on object intrinsic and extrinsic features; (2) design of key decision-making components, e.g., attribute-driven policy rules, threshold selection criteria and operators, and balance between positive and negative features of an object; (3) development of an utility fusion theory based on the decreasing margin utility theory; and (4) applications of the proposed framework to software selection and reuse.

## 2. Related work

Two major streams of literature are related to our work: general decision-making methods and trust-based decision models. We discuss each of them next.

## 2.1. General decision-making methods

In terms of general decision-making methods, our framework can be classified into the “Decisions whether” [13] category, which is the “yes/no”, “either/ or” decision that must be made before one proceeds with other alternatives. Available choices for one subject of matter are evaluated one by one. One can be accepted as long as it satisfies the evaluator's requirements. There are several decision-making strategies such as optimizing [13], satisfying, maximax (maximize the maximums), and maxmin (maximize the minimums) [21]. Our decision model falls into the satisfying category, where the first satisfactory alternative is chosen rather than the best alternative. It is essentially different from those decision methods [5,19] that aim at selecting the “best” option among alternatives.

The presented framework also has solid theoretical foundations on the filter theory [14] and the multiattribute choice principle of decision-making [4,22]. According to the filter theory, users make some choices through a series of selection filters, where different criteria can be used in the successive stages. In the two-level decision model as presented in this paper, decisions are made at both system and internal application levels in this order. A software program that is obviously out of the boundaries is ruled out first. Other software that satisfies the system-level decision criteria can be selected. Then the refined decision criteria are applied to the selected software to organize them for different usages (e.g., used as software components for mission-critical, routine, or experimentation projects). The software in each reorganized group may also be granted appropriate privileges to access local resources. According to the multi-attribute choice principle of decision-making, various strategies are used for different types of choices. The decision at the system level in our model uses conjunctive rules and quantitative numerical variables to eliminate choices that lie outside boundaries. The decision at the application level uses qualitative analysis to address less formalized decision problems, for example, organizing objects into different groups based on their features.

Decision support systems (DSS) focus on supporting and improving managerial decision-making. There are various sub-fields in the general DSS discipline including personal decision support systems, group support systems, negotiation support systems, etc. [2]. Artificial intelligence techniques have been employed predominantly to solve various problems in decision-making under uncertainty [30]. Rough set theory, fuzzy logic, neural networks, genetic algorithms, and intelligent agents systems have been widely used in DSS [1,27,34, 37,18,10,33]. Those soft computing models have strong theoretical foundations but sometimes are complex and hard to be applied to such an unstructured decision problem as selecting objects with desires features. Our model is simple and effective. While being applied to software evaluation and selection, it assists users in eliminating the chances that selected software programs are embedded with malicious code or hidden vulnerabilities, or developed with incorrect functions. The model appeals to management since it is intuitive and relatively transparent, allowing users to see the logic of the results. Two-level decision-making also mitigates the risk of using wrong, incomplete, or insecure information.

## 2.2. Trust-based decision models

Many researchers have investigated trust as a critical factor in decision-making in various field [11,20,17, 24,29]. Our decision model is trust-based. But it focuses on studying the intrinsic and extrinsic trust features of an object. An object is evaluated based on a set of trustrelated attributes and their corresponding testing conditions. The evaluator then decides whether the object is trustworthy and, hence, can be used. Focusing on the study of information quality and security at object level gives a user higher confidence in using an object since the object has been directly assessed instead of letting the evaluator entirely rely on others' opinions about the object. Existing trust-based decision models, on the other hand, are based on subject trust management. For instance, they rely on the principle of transitive trust. A user trusts another object because a trusted third party says so. Any process that needs to access local resources should present a set of certificates signed by some trusted parties to confirm to the local system administrators that the request submitter is trustworthy. The PolicyMaker framework [3,25], for example, defines which resources the user having a particular public key can access. Certificates and policies play a crucial role in describing who are to be trusted and what level of rights those trusted entities should have. The REFEREE framework [6] is another trust management system for making access decisions relating to Web documents. Its core component is a recommendation-based query engine, which interprets the policy and list of arguments and returns an answer to the calling application. IBM Trust Establishment Framework [9] is a role-based access control model. Its trust Establishment module validates the client's certificate and then maps the certificate owner to a user role based on a set of pre-defined rules. Although those trust models are effective, they don't fully address the intrinsic features of individual objects under evaluation. On the other hand, our model systematically defines the intrinsic and extrinsic trust features for object evaluation and selection.

We use open source software selection as an illustrative example for our framework. Software selection is a challenging issue. The Business Readiness Rating (BRR) proposal [31] offers a standard model for rating open source software and is comparable to our work. But our model focuses more on decision-making theory and process. In addition to object selection, our model goes one step further and specifies refined rules to re-filter and group the selected objects based on their quality and security features. There is another trust-based decisionmaking research work related to open source trustworthiness. A trust management solution is presented in [35], which can manage trust adaptively in a component based software system. A trust model was developed to specify, evaluate, and set up trust relationships that exist among system entities. But the focus of the paper is on trustworthy middleware architecture. The paper in [28] discusses how the EU-funded EDOS project can be used to improve the evaluation and monitoring of Free/Libre and Open Source Software (F/LOSS) security. The paper addresses various important security issues under different assumptions regarding the underlying technical infrastructure of F/LOSS. A security risk in software component technology is discussed in [16] – an application owner may incriminate a component designer falsely for any damage in his application which in reality was caused by somebody else. A solution was provided where trust values of the component users are stored and each user's ratings are discounted based on his/her trust value. Our model is different from [28,16] since they attempt to solve different set of problems in open source software evaluation and selection.

## 3. Terminology

This section first defines object, trust-related attributes of a type of objects, and the values of those attributes given an object. Then the coined term utility is introduced. A UML class diagram is developed to illustrate the relationships among the terms defined in this paper (see Fig. 3).

Definition 1. An object is a passive entity that represents a piece of information or knowledge in various forms such as a software program, a data item, a statement, or a file.

Object is a generic term. In our discussion, it refers to an intelligent resource shared in a virtual organization. A set of objects, which addresses the same issue, belongs to one type. In terms of open source software, there are often similar software programs which all claim to provide similar functions. That software is considered as one type. For example, Ethereal, TCPdump, or SNMP software all perform network monitoring and packet sniffing. Hence, they can be classified as a type of network monitoring software. We assume a user only needs to select one object from the set of available ones for that type.

Selecting a trustworthy object relies on evaluating the trust-related features of the object. These features are quantitatively expressed by the values of a set of trustrelated attributes defined for the type of objects to which the candidate object belongs.

Definition 2. A trust-related attribute of a type of objects describes a property or characteristic of the objects of this type. The value of such an attribute, given an object, reflects the object's quality and/or security features that provide insights for an evaluator to assess the trustworthiness of the object.

Trust-related attributes of a type of objects include both intrinsic and extrinsic attributes of the objects as long as (1) the values of the attributes expresses the trust features of the objects and (2) those values help an evaluator assess the trustworthiness of the objects. For instance, the robustness (or fault-tolerance) of a software program describes one functional feature about the program. This feature helps an evaluator in making a decision regarding the quality of the software. Hence, this attribute is considered a trust-related attribute for the type of software. Other examples of trust-related attributes include the total books published about a software package under evaluation, the difficulty level to enter the core development team of the software, and the recommendations from adaptive users about the software.

Defining trust-related attributes of a type of objects is domain specific; therefore, our framework is general enough to allow the designers to define those attributes in their applications. For open source software selection, trust attributes should be specific and address the quality and/or security features of software available. Examples of software related trust attributes are provided in Table 1 and Fig. 5.

![](/api/attachments/B4YSPHWX/fulltext/images/80c658a2cd7489ac0aa56b6b86302d9d7e4c4fc1eda156b7481a37e349281676.jpg)  
Fig. 3. UML class diagram of terminology.

The value of a trust-related attribute (or attribute for short) given an object describes either a favorable or unfavorable feature of the object. A generic term utility [32] is coined that measures such a feature. Utility is used as a scale to express and measure an evaluator's expectation (or satisfaction) for the quality and security features of a given object. It is unit-less and can be applied to compare and represent features evaluated from different aspects. Common utility shapes include concave, convex, and combination [36]. We discuss how to determine the utilities assigned to attribute values in Section 4.3.

## 4. Decision model at the system level

Since the decision model at the system level defines general rules to select objects, the decision process at this level is desired to be quick, standard, but less specific. Based on a relatively small set of most representative and important attributes, the decision rules at this level filters out some objects quickly, which are obviously out of boundaries, or select an object, which clearly meets the system's expectations.

The steps in developing policy rules can be summarized as: (1) identifying critical attributes, non-critical (regular) attributes, desired positive values (or ranges) and/or dominating negative values (or ranges) of those critical attributes; (2) defining primary negative rules based on the identified dominating negative attribute values (or ranges), defining primary positive rules based on the identified desired positive attribute values (or ranges), and defining accumulating rules based on other regular attribute values (or range); (3) defining positive and negative threshold selection functions (for implied rules); and (4) defining residual policy rules. Next we explain these terms and discuss the policy making process.

## 4.1. Dominating negative values, desired positive values, and critical attributes

Most objects have both positive and negative features as measured based on their values for the attributes defined for the type of objects. If an object has a negative feature that an evaluator cannot accept, then the object should be rejected immediately. Such a feature is expressed by a dominating negative value.

Table 1 Representatives of refined trust-related attributes for software programs

<table><tr><td>Category</td><td>Representatives attributes</td></tr><tr><td>Security-oriented negative attributes</td><td>Creating hidden network connections and listening at privilege portsForking new process (or threads) automaticallyWriting to local disks without user&#x27;s acknowledgementsReading system configuration and/or log filesCreating a large number of temporary filesPermitting default or weak passwordsManipulating hidden-fieldsDropping a backdoor and creating hidden user accountsAllowing exchanges of sensitive information in plain textLeaving executable code in memory after executionPermitting relative and default file and/or directory pathsEmbedding code segments out of the designed specifications of the programAccepting files with arbitrary-lengths as inputs</td></tr><tr><td>Security-oriented positive attributes</td><td>Certified by CERT (Center of Internet Security hosted at the Carnegie Mellon University)Carrying valid security-proof code supplied by the software developersRequiring strong data typeConducting rigorous checks for memory-overflowExecuting only in a sand-box limited scope</td></tr><tr><td>Quality-oriented positive attributes</td><td>Using a set of well-proved and widely-used algorithmsIntegrating only highly trustworthy software componentsBeing analyzed by leading consulting firms with positive resultsBeing developed using rigorous software development practicesHaving a large number of user downloads since its releaseHaving complete and informative documentationsContaining user friendly interfaces</td></tr><tr><td>Quality-oriented negative attributes</td><td>Having a large number of functional bugs reported by users since its releaseHaving race conditions and deadlocksUsing self-references or having infinite loopsHaving poor software scalability and portabilityProviding no exception handling routinesUsing software components without appropriate licenses</td></tr></table>

Definition 3. A dominating negative value of an object refers to such a value for an attribute that the feature represented by this value is so “negative” that a system must make a denial decision towards that object regardless of its values for other attributes. Such a value is attribute-specific.

Examples of dominating negative values for a set of software programs include (1) the value “ten” (or more) for the attribute “outstanding critical security vulnerabilities” about a software program of that type; (2) the value “yes” for the attribute “backdoor software installed in the program under evaluation,” and (3) the value “yes” for the attribute “serious errors in the algorithms used by the program.”

In the other end, an attribute of a type of objects is so attractive that if a given object has a value for such a favorable attribute and that value is good enough, then the object can be selected by the system.

Definition 4. A desired positive value of an object refers to its value for an attribute so that the feature represented by the value is so “favorable” and the object can be accepted by a system if it does not possess any dominating negative values.

Examples of desired positive attribute values include (1) the value “yes” for the attribute “security- and qualitycarrying code provided by the software developers;” (2) the value “yes” for the attribute “thorough analysis and positive reports about the software's functions from a leading consulting firm;” and (3) the value “yes” for the attribute “rigid software engineering practices in developing the software program and the excellent reputation of the software development team.” After a dominating negative value or a desired positive value is specified, a critical attribute can be easily defined.

Definition 5. A critical attribute refers to an attribute of a type of objects that a given object can have either a dominating negative value or a desired positive value. The former is called dominating negative attribute and the latter is called desired positive attribute.

A critical attribute has at least one value (given an object), which could lead to a decision (either acceptance or rejection of the object). Such a value can be assigned with an infinitely large utility (negative or positive) since it may lead to a decision. All other attributes of a given type of objects are considered as regular (non-critical) because their values alone can't allow an evaluator to make an acceptance or rejection decision no matter what values a candidate object has for those attributes. Examples of regular attributes include (1) the number of books published about a software; (2) the average volume of general mailing list about the software in the last six months; (3) documentations about the software; and (4) the average number of downloads of the software per month.

## 4.2. Decision-making logic at the system level

Decision-making at the system level first specifies a set of dominating negative attributes and the respective testing conditions for a given type of objects under consideration. Each testing condition identifies a set (or a range) of thresholds corresponding to a dominating negative attribute. If a given object has a value for that attribute, which is evaluated in the defined range, then the feature represented by this value is not acceptable by the system. Hence, the object must be rejected. If the object has no dominating negative value and it has at least one desired positive value, then the object can be selected.

As an object can have complex features, it is difficult to decide that it is an absolutely “good” or “bad” object. On one hand, the object may have some positive features; but those merits are not strong enough for a system to make an acceptance decision. On the other hand, the object may have some negative aspects; but those unfavorable features are not severe enough for the system to make a rejection decision. Hence the decision model at the system level applies a scoring mechanism to accumulate the positive and negative features measured based on their utilities respectively. When the balance of those accumulated utilities is beyond a certain level, a decision can be made. Since such a scoring mechanism is only applied after any dominating negative and/or desired positive values are considered, it is used for regular attribute values, non-dominating negative values, and no-desired positive values.

For a candidate object O, the accumulated positive and negative utilities can be represented as a point, say P, in a two-dimension coordinate system (see Fig. 4). There are three regions in this system. If P falls into region (1), the accumulated utility based on O's negative features is high while the accumulated utility based on its positive features is low. In this case, O should be rejected. Region (1) is called the rejection region. If P falls into region (2), O can be selected since the accumulated utility for its positive features overweight the accumulated utility for its negative features. Region (2) is called the acceptance region. For any object with P falling in region (3), a further analysis (see Section 4.3) is required to determine whether the object can be selected. Region (3) is called the indecisive region.

![](/api/attachments/B4YSPHWX/fulltext/images/df217f3590bdbecec3081aa0a745c17c0a94e0165ff5f994d262ef62ac1153f1.jpg)  
Fig. 4. Non-linear threshold selection/rejection curves.

Along with the two coordinate axes, the two curves as shown in Fig. 4 can uniquely determine the three regions. The curve that determines region (1) (with the vertical axis) is called the rejection threshold curve. Similarly, the curve that determines region (2) (with the horizontal axis) is called the selection threshold curve. Each curve is determined by a general function like nu=f(pu), where nu represents the accumulated utility for the negative features, or negative utility for short, of an object under evaluation; pu represents the accumulated utility for the positive features of the object; and f represents the relationship function between nu and pu. f is called a selection curve function for the selection threshold curve and a rejection curve function for the rejection threshold curve. See Fig. 4 for an example of the three regions, two threshold curves, rejection threshold, and selection threshold.

Making a balance between the positive and negative features of a candidate object is subjective by nature. It depends on such factors as how strict one is in selecting objects, to which degree to accept objects with negative features, and how to view the net results of positive and negative features. We address this issue by defining acceptance and rejection functions with flexibility. Policy makers and system administrators can then determine how strictly they want to set the policies. Two functions are discussed below, which can be used by an evaluator to make a balance between the positive and negative features of a given object: constant-difference linear function and logarithmic non-linear function.

## 4.2.1. Constant-difference linear function

This function assumes that the difference between the values of nu and pu is constant for any point on the two selection threshold curves. For a given object, its negative features are compared with its positive ones. Their difference determines the strength (or weakness)

of the candidate object. Visually, both curves have a linear line shape with angles of $4 5 ^ { \mathrm { { o } } }$ with both axes. The functions are defined below (where constant value a represents the selection threshold and constant value d represents the rejection threshold):

Selection curve function : $p u - n u = a \mathrm { o r } n u$

$$
= p u - a\tag{1.a}
$$

Rejection curve function : $n u - p u = d \mathrm { o r } n u$

$$
= p u + d\tag{1.b}
$$

## 4.2.2. Logarithmic non-linear functions

This function assumes non-linear relations between values of nu and pu for the selection or rejection threshold curves. The rational of this function is that more positive features need to “cover” or “compensate for” any negative features that a candidate object may have. Compared with the linear functions, which are more tolerable, the nonlinear selection/rejection functions are more conservative. Some objects, which may be selected under the linear functions, could be rejected if the non-linear functions are applied. The two functions are defined below (where b represents a base such as 2 (binary), e (natural log function), etc.). An example of the non-linear function curves is given in Fig. 4. The larger the b value is, the more conservative the selection threshold curve (towards rejection) would be. Hence a decision maker can adjust this value for flexibility.

$$
\text { Selection   curve   function }: n u = \log_ {b} (p u + 1 - a)\tag{2.a}
$$

$$
\text { Rejection   curve   function }: n u = \log_ {b} (p u + b ^ {d})\tag{2.b}
$$

## 4.3. Policy specification

Based on the decision-making logic at the system level, an attribute-driven policy specification can be defined to select only qualified objects from external sources.

Definition 6. A policy specification is a set of trustbased policy rules, specifying high-level descriptions of what features of an object can't be tolerated and thus the object must be denied as well as what features are favorable and thus the object could be accepted.

As discussed earlier, critical attributes and their dominating negative values and/or desired positive values are specified first in a decision-making process. The testing conditions can then be defined based on those threshold values. Finally, the policy rules can be developed based on the testing conditions. There are four types of policy rules in a policy specification: (1) the first type specifies a dominating negative attribute for a type of objects and the related testing condition. If a candidate object has a value for such a negative attribute and that value is tested as not acceptable, then the object must be denied; (2) the second type specifies a desired positive attribute for the type of objects and the respective testing condition. If a candidate object has a value for such a positive attribute and the value is tested as good enough, then the object can be accepted (unless it also possesses a dominating negative value for some critical attributes); (3) the third type of policy rule specifies non-critical attributes of the type of objects, for which a candidate object has a value that is not significant enough (for an evaluator to make an acceptance or rejection decision). But, the utility based on that attribute value can be accumulated towards the positive or negative features of the object; and (4) the fourth type of policy rule verifies whether the accumulated positive and negative features (measured as their respective utilities) for the candidate object enable the system to make a decision after balancing their opposite effects. A policy rule of types (1), (2) or (3) is called a primary rule. More specifically, a rule of type (1) is called a primary negative rule and a rule of type (2) is called a primary positive rule. A rule of type (3) is called a primary accumulating rule. A rule of type (4) is called an implied rule. An implied rule considers a pair of accumulated positive and negative utilities and produces a value from the set {acceptance, rejection, indecisive}.

All the primary policy rules are evaluated and enforced in a pre-defined order. A primary negative rule, if any exists, cannot appear after any other types of primary rules. In other words, a policy specification must start with a set of primary negative rules, if any. Those primary negative rules specify the dominating negative attributes of a type of objects and their testing conditions. If a given object has one of those values as tested true by such a condition $( \mathrm { i . e . , }$ it has a negative feature that cannot be accepted by the system), that object must be denied. If the object does not possess any negative feature as specified by a primary negative rule, it is tested based on the following primary positive rules, accumulating rules, and implied rules. Finally, if all available similar objects have been evaluated and no object has been selected for that subject matter, residual policy rules are applied (see Section 4.4).

Every critical attribute identified for a type of objects must be addressed in a policy specification. The number of non-critical (or regular) attributes to consider depends on the nature of a particular decision case. In terms of open source software selection and reuse, the Business Readiness Rating proposal (BRR) [31] suggests that 12 categories of attributes are ranked and fewer than 7 top categories are considered. The number of metrics (similar to attributes in our paper) in each category is typically no more than 7. After specifying a set of attributes, say, $a _ { 1 } ,$ $a _ { 2 } , a _ { 3 } , . . . , a _ { n } ,$ the utilities (positive or negative) assigned to the domain values of those attributes can be determined by following the three steps below:

(1) Normalize and transform, if necessary, the domain values of each attribute in a range (called attribute value range) with discrete elements. The number of normalized domain values in each range can be flexible according to different scaling policies. To make our following discussions clear, we assume that the value ranges for attributes $a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . , a _ { n }$ are represented as $[ \nu _ { 1 1 } , \ \nu _ { 1 2 } , . . . , \ \nu _ { 1 i } ] , \ [ \nu _ { 2 1 } , \ \nu _ { 2 2 } , . . . ,$ $\nu _ { 2 j } ] , [ \nu _ { 3 1 } , \nu _ { 3 2 } , . . . , \nu _ { 3 m } ] , . . . ,$ and $[ \nu _ { n 1 } , \nu _ { n 2 } , . . . , \nu _ { n k } ] ,$ respectively, where the first subscript letter of each element identifies the attribute and the second subscript letter represents a domain value number for that attribute. We require that in an attribute value range, the left most value $( \mathrm { e } . \mathrm { g } . , \nu _ { 1 1 }$ in $[ \nu _ { 1 1 } , \nu _ { 1 2 } , . . . , \nu _ { 1 i } ] )$ must be the least favorable value and the right most value must be the most favorable value. Therefore, $\nu _ { \mathrm { 1 i } } , ~ \nu _ { 2 j } , ~ \nu _ { 3 m } . . . , ~ \nu _ { n k }$ represent the most favorable values for attributes $a _ { 1 } , \ : a _ { 2 } , \ : a _ { 3 } , . . . , \ : a _ { n }$ respectively and $\nu _ { 1 1 } , \nu _ { 2 1 } , \nu _ { 3 1 } . . . ,$ $\nu _ { n 1 }$ represent the least favorable values for those attributes respectively.

(2) Rank or weight the n most favorable values $\nu _ { 1 i } , \nu _ { 2 j } ,$ $\nu _ { 3 m } , . . . , \nu _ { n k }$ based on their significance/importance related to intended usage of those objects. Assign a maximum positive utility (e.g., 10) to the most significant value, say $\nu _ { 2 j } .$ . Then the other $n - 1$ most significant values, i.e., $\nu _ { 1 i } , ~ \nu _ { 3 m } . . . , ~ \nu _ { n k }$ can be assigned their corresponding utilities according to their relative importance/significance to $\nu _ { 2 j } .$ . For instance, $\mathrm { i f } \nu _ { 2 j }$ is evaluated as twice as significant as $\nu _ { 3 m }$ in terms of the features they represent towards the intended usage of the objects under consideration, then the utility assigned to $\nu _ { 2 j }$ is roughly the twice of that assigned to $\nu _ { 3 m } . \mathrm { A p p l y }$ the similar procedure to the n least significant values $\nu _ { 1 1 } , \nu _ { 2 1 } , \nu _ { 3 1 } . . . , \nu _ { n 1 }$ . After this step, the utilities of each attribute's domain values must be in a certain range.

(3) Determine the utilities of all the other intermediate domain values for each attribute except the most and the least favorable ones. The utilities assigned to those intermediate values are based on their relative “distances” to the most and the least favorable values.

To further explain how the scoring mechanism scales different attribute values in the decision process of selecting an open source software program, we give a short example with only three attributes to consider: (a) $A _ { 1 } { \mathrm { : } }$ the number of security and quality patches about the software released in the past 12 months; (b) $A _ { 2 } \mathrm { : }$ total books published about the software; and (c) $A _ { 3 } { \mathrm { : } }$ difficulty level to enter the core development team. Three steps are specified below: Step 1: Normalize the domain values of each attribute. For instance, the domain values of attribute A : “total books published about a software package” can be normalized in a range [few; some; many] according to the following guidelines: $0 { - } 5 { \longrightarrow } ^ { \mathrm { * * } } \mathrm { f e w } ^ { \mathrm { * * } } , 6 { - } 1 5 { \longrightarrow } ^ { \mathrm { * * } } \mathrm { s o m e } ^ { \mathrm { * * } }$ , 16 or more→ “many.” The similar method can be applied to the other two attributes. Suppose the three normalized attribute value ranges for $A _ { 1 } , A _ { 2 } ,$ , and $A _ { 3 }$ are represented as $[ \nu _ { 1 1 } ; > 6 ;$ v : 0–2 or 5–6; v : 3–4], [v : few; $\nu _ { 2 2 } .$ some; v<sub>23</sub>:

many], and $[ \nu _ { 3 1 } ;$ easy; v<sub>32</sub>: normal; $\nu _ { 3 3 } \colon$ difficult; $\nu _ { 3 4 } \mathrm { : }$ very difficult], respectively. Step 2: Rank $\nu _ { 1 3 } , \nu _ { 2 3 } ,$ , and $\nu _ { 3 4 }$ in terms of their significance related to the intended usage of the software. Assume that $\nu _ { 1 3 }$ is ranked highest and a utility 10 (utility is a relative measuring scale) is assigned. Relative to $\nu _ { 1 3 } , \nu _ { 2 3 }$ and $\nu _ { 3 4 }$ can be assigned utilities 4 and 6 based on their relative significance compared with $\nu _ { 1 3 } .$ Relative ranking or weighting factors among those values can be determined using either the Analytic Hierarchy Process or the “zig–zap” method as proposed in BRR [31] (Due to page limitation, we won't discuss this issue further). Similarly, utilities can be assigned to the least favorable attribute value of each attribute. In our example, $\nu _ { 1 1 } , \nu _ { 2 1 } ,$ , and $\nu _ { 3 1 }$ are assigned utilities as − 8, 0, − 2, respectively. Step 3: Determine the utilities for the intermediate domain values of each attribute. According to step 2, for the attribute $A _ { 2 }$ the utility assigned to its most favorable value, i.e., “many”, is 4 and the utility assigned to its least favorable value, i.e., “few”, is 0. The utility assigned to the intermediate value “some” can be calculated as the average of the two values, i.e., (0+ 4)/ 2 = 2, if we figure out (via Analytic Hierarchy Process or the “zig– zap” method) the value “some” is equally close to “few” and “many.” Apply this procedure to the intermediate values in other two attribute value ranges.

A complete example of the primary rules of a policy specification is given in Fig. 5. Here, a system evaluates software S in order to determine if S satisfies the system's requirements for information quality and security. The policy specification starts with a primary negative rule, which indicates S should be rejected if either S or its software components don't have appropriate licenses (not all open licenses are created equal; some licenses are much more restrictive than others). The dominating negative attribute specified in this rule is “appropriate software licenses of software and its components, if any.” For a candidate software program, if its value for this attribute is evaluated as “no”, then this software program should be rejected. If the value is “yes”, then the evaluation moves to the next rule. Rules 2–5 are also primary negative rules. If S doesn't have any dominating negative values as tested by those rules but has a desired positive value, which satisfies any of primary positive rules 6–8, then S can be accepted. Otherwise, S is evaluated based on rule 9, which is a primary accumulating rule based on the attribute “the number of security and quality patches released on the software in the past 12 months.” If S's value for this attribute is greater than 6, then a negative utility (or disutility) $\mathrm { o f } - 8$ is assigned to this value. Consequently, the software's accumulated negative utility is subtracted by 8. If S's value for this attribute is between 0–2 and 5–6, then its accumulated positive utility is incremented by 1. If the value is 3 or 4, $S ^ { \prime } { \mathrm { s } }$ accumulated positive utility is incremented by 9. The positive and negative accumulated utilities are counted separately for a given object under evaluation. After rule 9, the following primary accumulating rules are evaluated for S one by one. Finally, the implied rules are applied, which take the accumulated utilities for both positive and negative features of S as inputs to determine if S should be selected, or rejected, or no definitive decision is reached.

```csv
1. Reject S ← S or its software components don't have appropriate licenses
2. Reject S ← S is tested with mal-ware (e.g., back door or logic bomb)
3. Reject S ← S has serious quality or security vulnerabilities outstanding (e.g., not patched)
4. Reject S ← S was developed using questionable or wrong algorithms (as indicated in its developing documents)
5. Reject S ← S doesn't comply with industry standards
6. Select S ← S has been tested by a leading consulting firm with positive recommendations in terms of its quality and security features
7. Select S ← S has passed in-house rigorous functional tests with positive results
8. Select S ← S was developed by a prestigious software team with a very good reputation of following rigid software engineering practices
9. [-8; 1; 9] ← the number of security and quality patches about S released in past 12 months: [>6; 0-2 or 5-6; 3-4]
10. [0; 7] ← availability of research reports on S from the leading market research firms: [no; yes]
11. [-8; -4; 0; 4; 8] ← implementation language desirability: [strongly not desired; not desired; desired; neutral; strongly desired]
12. [-2; 2] ← availability of a security site/wiki: [no; yes]
13. [0; 2; 4] ← total books published about S: [few; some; many]
14. [-2; 0; 4; 6] ← difficulty level to enter the core development team: [easy; normal; difficulty; very difficult]
15. [-5, 5] ← S is accompanied with detailed troubleshooting tips: [no, yes]
16. [-1; 1] ← the publisher of S maintains an informative web site for user support: [no; yes]
17. [-10, 10] ← the source code of S comes with solid documentations: [no; yes]
18. [-3; -1; 1; 3] ← the number of downloads of S per month: [<100; <500; <1000; >1000]
19. [-2; -1; 0; 1; 2] ← time to setup prerequisites for installing S: [>4 hours; 1-4 hours; 30 minutes – 1 hour; 10 – 30 minutes; < 10 minutes]
```  
Fig. 5. Primary rules of a policy specification to evaluate a software program S.

## 4.4. Residual policy rules

After applying all the primary and implied policy rules to a candidate object, three results are possible: (1) the object has been accepted and the decision process for the matter of subject is completed; (2) the object has been denied and the next object about the same subject of topic should be evaluated; or (3) no decision can be made regarding the object but the object can be added to a set Candidate, which contains the residual objects after all the primary policy rules and implied rules have been applied. Since all the residual objects are about the same subject of interest, selecting one, if any, is enough.

The residual policy rules help select an object from the Candidate set. There are several ways to design residual policy rules: (1) filter out any object with negative utility beyond a threshold; (2) rank the candidate objects based on the difference between their positive and negative utilities, then select the one with the largest net positive difference; or (3) select the object based on certain customized criteria. In terms of option (3), one criterion is to select the object with the highest trust value.

The trust value of an object can be calculated based on the aggregation of a group of recommenders' options towards the quality and/or security features of the object. Each recommended trust value of the object is then discounted using the trustworthiness of the recommender. This is simply because the recommender may not be fully trusted in making a reliable recommendation. Consider the case where a recommender doesn't provide his/her authentic opinions about the object or the recommender has imperfect knowledge about the object under evaluation. Formula (3) represents a method to calculate the trust value of an object, $O ,$ for an evaluator E in terms of its quality and security features. The trust value is denoted as $T ( E , O )$

$$
T (E, O) = \sum_ {i = 1} ^ {i = n} [ T (E, R _ {i}) ^ {*} T (R _ {i}, O) ] / n\tag{3}
$$

where $T ( E , R _ { i } )$ represents the trust that evaluator $E$ places on recommender $R _ { i } ,$ where $1 \leq i \leq n$ (we assume n recommenders are available) and $T ( R _ { i } , O )$ represents the recommended trust value of object O by $R _ { i } .$

We next discuss the calculation of the trust value of a recommender $T ( E , R _ { i } )$ using a web of trust network. A web of trust describes direct trust relationship between two neighbor subjects. One subject is a neighbor to another if the latter has built and maintained personal trust relationship with the former. Those direct trusts form a trust network. A web of trust is represented by a weighted directed graph with each vertex representing a subject and each directed edge with weight t from vertices V to $V ^ { \ast }$ representing that V directly trusts $V ^ { \ast }$ with trust value of t. Indirect trust between two subjects that are not neighbors can be calculated based on the principle of subject trust transitivity. Under the maximum principle, a user believes anything that is believed by at least one of the users she trusts. The trustworthiness of a subject can be obtained by applying the algorithm in Fig. 6. The algorithm identifies a path with minimum sum of distrust for every pair of remote subjects. Then appropriate aggregation of trust along that path can be applied to calculate the indirect trust values between any pair of subjects based on a trust network. Given a trust network $G ,$ for every edge $e \in E$ (G) with edge weight $t ,$ where t is a real number in the range [0, 1], re-label e with $t ^ { \prime } { = } 1 - t .$ So a new graph $G ^ { \prime }$ is generated with $V ( G ) = V ( G ^ { \prime } )$ and $E ( G ) = E ( G )$ but each edge of $G ^ { \prime }$ has different value from the corresponding edge of $G .$ . Intuitively, $t ^ { \prime }$ specifies the degree of direct distrust between two subjects. $G ^ { \prime }$ is called a distrust network. The goal of this algorithm is to find a path between any pair of nodes of $G ^ { \prime }$ with minimum sum of $\mathit { \Pi } _ { t { ' } } ^ { \phantom { \dagger } }$ values along that path.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm: All-pair shortest path discovery for indirect subject trust computation
1. For every $e \in \mathrm{E}(\mathrm{G})$, change the weight of $e$ from $t$ to $t'$ where $t' = 1 - t$
    /* This generates a new trust network, $G'$, such that $V(G) = V(G')$ and
    $E(G) = E(G')$ but each $e \in E(G')$ has a new weight as $t'$    */
2. Perform a “all-pair shortest path discovery” algorithm to identify the shortest path between every pair of vertices in $G'$, and generate a path $P = \{S_i, S_{i+1}, ..., S_j\}$ for every given pair of nodes $S_i$ and $S_j$.
3. For every pair of nodes $(S_i, S_j)$, the amount of trust that $S_i$ has on $S_j$ is calculated as
    $T(S_i, S_j) = T(S_i, S_{i+1}) * T(S_{i+1}, S_{i+2}), ..., *T(S_{j-1}, S_j)$
    where edge $(S_k, S_{k+1}) \in E(G)$ and $(S_k, S_{k+1}) \in P$ for $i \leq k \leq j-1$; $T(S_k, S_{k+1})$ represents the amount of trust $S_k$ has on $S_{k+1}$ as indicated in $G$, i.e., edge value of $(S_k, S_{k+1})$.
</div>

Fig. 6. Subject trust calculation.

## 5. Decision model at the application level

The decision model at the system level focuses on the system-wide general requirements for information quality and security without addressing any particular concerns of internal applications within that system. The decision model at the application level allows individual internal applications to specify and apply their additional and refined policies to filter or reorganize those objects selected at the system level.

## 5.1. Additional and/or refined attributes

The decision model at the application level defines additional and/or refined trust-related attributes for a type of object. Certain attributes would be best specified by individual internal applications. For instance, for the selection of open source software, additional attributes can be defined to describe the refined technical features of available software and restrict their usages based on different criteria. Developing mission-critical, routine, experimental, or testing projects each has different requirements towards the quality and security features of their software components. Any mission-critical project requires that its software components have high level of reliability. Our study draws its motivation from research on service quality [7,23,15]. But it is different in terms of the measurements in focus.

Trust-related attributes of a type of objects can be refined from two aspects: (1) domain-dependent technical perspective; and (2) semantic meaning perspective. The first aspect focuses on the intrinsic features of the type of objects. Technical attributes can be classified into two major categories: security-oriented and qualityoriented. The second aspect focuses on favorable or unfavorable semantic meanings of an attribute. An attribute, which describes a desired and welcome $( \mathrm { i . e . , }$ favorable) property of the type of objects, is called a positive attribute. A positive attribute expresses a user's expectation towards a particular feature of the type of objects. Hence, users wish to see a higher value for a positive attribute given an object. Examples of positive attributes of software programs include rigorous software engineering practices in producing the software, the expertise of the software development team, and complete and informative documentations of the software. On the other hand, an attribute with negative semantic meaning, called a negative attribute, represents an unfavorable property of the type of objects. A negative attribute expresses an evaluator's concerns and wishes to minimize such property of a given object. Users would like to see a lower value for a negative attribute. One example of a negative attribute is the possibility of virus infection given a software program. Based on a positive feature of an object, the semantic meaning of a utility is considered positive. Such a utility is called a positive utility. In contrast, a utility based on a negative feature of an object is called a negative utility, or disutility.

A positive or negative attribute only represents an evaluator's preferences or concerns towards a favorable or unfavorable property of a type of objects, respectively. An object under evaluation may have a “poor” value for a positive attribute. For instance, the attribute “correctness of algorithm” describes a desired property of a software program (hence, from the user's perspective, it is considered as a positive attribute). But a particular software program may be assessed with a negative value for this attribute if that program was developed using incorrect or questionable algorithms. On the other hand, an object may have a positive value for a negative attribute. For instance, “memory leak” is considered as a negative description of any software, which expresses a user's concern about the negative feature of the program's memory management. But, for a particular program, the user may assess a very positive value for this attribute if the program was tested or analyzed with no memory leak at all.

Combining both the technical and semantic aspects, four categories of refined and additional attributes are identified for software programs. Representatives for each category are listed in Table 1.

## 5.2. Attribute dimension

Although some attributes describe the quality and security features of a type of objects, their semantic meanings are close to each other's. Those attributes can be considered together from the same point of view. Object trustworthiness is a multi-faced concept. Trustrelated attributes of a type of objects can be organized into different sets, called attribute dimensions.

Definition 7. An attribute dimension of a type of objects consists of a set of attributes, which have similar logical meanings and all describe one feature aspect of the type of objects.

All the attributes in a dimension describe the feature(s) of a type of objects from the same aspect. For instance, one attribute dimension is about the producer information of the objects. Attributes in this dimension may include (1) the trustworthiness of the producer in faithfully completing its work as assessed based on the evaluator's past personal experiences with the producer; (2) the reputation of the producer in producing quality products as recognized based on public opinions; and (3) the aggregated trust value of the producer based on recommendations from some third parties. All the three attributes describe the trustworthiness of the producer of a given object and hence can be grouped in one dimension.

A dimension consisting of only positive attributes is called a positive dimension. Otherwise, if it consists of only negative attributes, it is called a negative dimension. A positive dimension represents an evaluator's overall expectations towards some positive characteristics of the type of objects from a certain perspective. Any selected object must have the required minimum positive features as evaluated based on the criteria from the perspective of that positive dimension. In the mean time, an evaluator also specifies negative dimensions to describe potential negative features of objects under consideration. A candidate object's negative features, if any, can't go beyond a certain level as defined based on those negative dimensions in order for that object to be selected.

## 5.3. Specifying requirements for an object from the perspective of an attribute dimension

This section discusses the evaluation of a candidate object from the viewpoint of one dimension. A theory is first derived and then a set of threshold selection operators is defined.

## 5.3.1. Utility fusion theory

For a given dimension $d _ { i }$ which contains n attributes, $a _ { 1 } , ~ a _ { 2 } , ~ . . . , ~ a _ { n } ,$ an internal application quantitatively measures the “goodness” or “badness” of a candidate object, say, O. O is evaluated with a value, say, $\nu _ { i } ,$ where $1 \leq i \leq n ,$ for every corresponding attribute $a _ { i }$ of dimension $d _ { i } .$ The attributes of a dimension in a particular order form an attribute permutation. In the following discussion, we consider an attribute permutation unless specified otherwise. Based on $a _ { i }$ the evaluator measures an utility, say, $U ( V ( a _ { i } ) )$ , called a component utility. According to the declining marginal utility theory [12], the marginal utility due to one more component utility is accordingly decreasing (see Fig. 7). Given a candidate object, the total utility that an evaluator measures based on the object's values for all attributes of dimension $d _ { i } ,$ called dimension utility and denoted as $U ( d _ { i } )$ , is thus less than the sum of all the individual component utilities. This is partially due to the overlaps among the features represented by different attribute values. The process of dimension utility accumulation presents a “fast start but slow growth” pattern.

Utility fusion theory. Given a candidate object, the fused (or accumulated) utility for an attribute dimension with a set of component utilities is not greater than the mathematical addition of all the corresponding component utilities, i.e., $\begin{array} { r } { U ( d _ { i } ) \leq \sum _ { i = 1 } ^ { i = n } U ( V ( a _ { i } ) ) } \end{array}$ , where $a _ { 1 } , . . . , a _ { n }$ represent the candidate's values for the attributes in the attribute dimension.

![](/api/attachments/B4YSPHWX/fulltext/images/caa787850fb46d458b3f4a5f6ed896088858e2ee3b1393c4d4f7266f9caffbb9.jpg)  
Fig. 7. Relationship between accumulated utility and component utilities.

Consider a dimension D, which describes software scalability. D consists of four attributes: (1) reference deployment, which measures whether the software is scalable and tested through a real-world deployment; (2) design for scalability, which measures whether the components of the software were designed with scalability in mind. Does the program thread-safe? Does it run in a cluster environment? (3) incorporation of third-party plugins, which measures the design for extensibility through third-party plug-ins; and (4) public API/External Service, which measures the extensions via a public API and the design for customization. The corresponding testing conditions for the four attributes can be defined as $C _ { 1 } \mathrm { { : } }$ the scalability of a given software program is tested in rea use with positive reports; $C _ { 2 } \mathrm { : }$ the program was designed with scalability in consideration and this has been verified by reviewing the detailed software engineering practice; $C _ { 3 } \mathrm { : }$ the software program allows third-party plug-ins; and $C _ { 4 } \mathrm { : }$ the software program allows for extensions via a public API and shows design for customization. If a software program satisfies $C _ { 1 }$ , then the fact that the program satisfies $C _ { 2 }$ only adds a marginal utility in the eye of the evaluator, which is less than the value evaluated in a situation if $C _ { 1 }$ was not conducted. For the third condition $C _ { 3 }$ , additional utility resulted from the allowance of thirdparty plug-ins may not add too much new “findings” regarding the software's scalability. The marginal utility of considering $C _ { 3 }$ would then be further decreased. Thus, the accumulated utility based on the four conditions is less than the mathematical sum of the four individual utilities based on their corresponding testing conditions.

## 5.3.2. Low-bound threshold selection operators

Given a positive attribute dimension defined for a type of objects, an evaluator may only need to assess a candidate object's values for a subset of attributes of that dimension. Evaluating other attribute values in the same dimension may not add too much utility (according to the utility fusion theory). As long as the accumulated utility based on this subset of attributes is good enough, the evaluator considers that the features of the object are acceptable from the viewpoint of that dimension.

## 5.3.2.1. Basic low-bound threshold selection operator.

For a positive dimension, the basic low-bound threshold selection operator, denoted as $\varTheta _ { i } ( C _ { 1 } , C _ { 2 } , . . . , C _ { n } )$ , specifies an evaluator's requirements for a candidate object from the viewpoint of that dimension. An object meets an evaluator's expectation if the object satisfies at least i out of n testing conditions, $C _ { 1 } , \ C _ { 2 } , . . . , \ C _ { k } , . . . , \ C _ { n } ,$ where

$1 \leq i \leq n ,$ and each testing condition $C _ { k } \ ( 1 \leq k \leq n )$ is defined based on a attribute, say $a _ { k }$ , in that dimension. Each $C _ { k }$ verifies whether a candidate object's value for $a _ { k }$ satisfies the evaluator's expectation for the feature expressed by $a _ { k } .$ Mathematically, the threshold value i represents the smallest number of attributes in the dimension so that $\begin{array} { r } { \sum _ { k = 1 } ^ { k = i } U ( V ( a k ) ) { \ge } \mathrm { U e } } \end{array}$ , where Ue represents <sup>¼</sup>the expected utility, i.e., the minimum utility with which the evaluator is satisfied toward that dimension (the i value is illustrated in Fig. 7). If every two component utilities are roughly equal, i.e., $U ( V ( a _ { i } ) ) \approx U ( V ( a _ { t } ) )$ , where $0 \leq j , t \leq n ,$ , then i can be calculated as $\begin{array} { r } { \dot { \iota } = \left\lfloor \frac { \mathrm { U e } } { U ( V ( a j ) ) } \right\rfloor . } \end{array}$ <sup>¼ ð Þð Þ</sup>Component utilities can be reformatted to be roughly even. For example, if $U ( V ( a _ { j } ) ) { = } 2 \ U ( V ( a _ { t } ) )$ , then $U ( V$ $\left( a _ { j } \right) )$ can be divided into $U ( \mathrm { { V a } _ { i } ^ { \prime } ) }$ and $U ( V ( a _ { \mathrm { i } } ^ { \prime \prime } ) )$ such that U $( \bar { \mathrm { V } } \mathrm { a } _ { \mathrm { j } } ^ { \prime } ) + U ( \mathrm { V } \mathrm { a } _ { \mathrm { j } } ^ { \prime \prime } ) { = } U ( \mathrm { V } \mathrm { a } _ { \mathrm { j } } )$ and $\bar { U } ( \mathrm { V a _ { j } ^ { \prime } } ) { = } U ( \mathrm { V a _ { j } ^ { \prime \prime } } )$

Consider the dimension D as discussed above. An evaluator may require that at least three of $C _ { 1 } , C _ { 2 } , C _ { 3 }$ and $C _ { 4 }$ be satisfied in order for a candidate object to be selected. In this case the basic low-bound threshold selection operator is specified as $\theta _ { 3 } ( C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } )$ in term of dimension $D .$

## 5.3.2.2. Conditional low-bound threshold selection

operator. The basic low-bound threshold selection operator does not specify particular testing conditions that a candidate object must satisfy. A more specific and restricted low-bound threshold selection operator, called conditional low-bound threshold selection operator and denoted as $\varTheta _ { i , [ C j . . . , C k ] } \left( C _ { 1 } , C _ { 2 } . . . , C _ { n } \right)$ , where $1 \leq j \leq k \leq n ,$ is defined to indicate that an object meets the evaluator's requirements for that dimension if it satisfies at least i out of n testing conditions and at the same time conditions $C _ { j , \cdots } C _ { k }$ must be satisfied as well. Consider the dimension D again. If the evaluator specifies an additional requirement that any software program selected must be scalable and tested using real-world deployment, the conditional low-bound threshold selection operator can be defined as $\Theta _ { 3 , \mathrm { [ } C 1 ] } \left( C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } \right)$

## 5.3.3. Upper-bound threshold selection operators

It is rare to have perfect objects. Hence, flexibility is desired to allow for a limited number of non-critical negative features of an object to be accepted given the condition that the object possesses other significant and critical positive features. As discussed earlier, a negative dimension expresses an evaluator's concerns about certain possible negative features of an object. An evaluator does not expect any selected object to be discovered with negative features worse than a tolerable level.

Consider a negative dimension $D '$ about I/O features of a set of software programs with six attributes:

(1) allowance of arbitrary-length file input; (2) forceful browsing; (3) cross-site references; (4) hidden-field manipulation; (5) cookie posing; and (6) manipulation of local file systems. The corresponding testing conditions based on these attributes are defined as below:

$C _ { 1 } { } ^ { \prime } \colon$ a candidate program accepts files with arbitrarylengths as inputs

$C _ { 2 } ^ { \prime } { : }$ the program forcefully browses

$C _ { 3 } { } ^ { \prime } \colon$ the program uses cross-site references

$C _ { 4 } ^ { \prime } { : }$ the program manipulates hidden-fields

$C _ { 5 } { } ^ { \prime } \colon$ the program has the feature of cookie poising

$C _ { 6 } { } ^ { \prime } \colon$ the program writes to local file systems

5.3.3.1. Basic upper-bound threshold selection operator. For a negative dimension with m attributes, the basic upper-bound threshold selection operator, denoted as $\Omega _ { j } ( C _ { 1 } ^ { \prime } , C _ { 2 } ^ { \prime } , . . . , C _ { m } ^ { \prime } )$ , indicates that no more than j out of m testing conditions, i.e., $C _ { 1 } ^ { \prime } , \ C _ { 2 } , . . . \ C _ { k } , . . . , \ C _ { m } ,$ where $1 \leq j \leq m$ , should be satisfied in order to consider that a candidate object doesn’t go beyond an evaluator's concerns regarding negative features of the object from the perspective of that dimension. A basic upper-bound threshold selection operator defines this “upper” bound for negative features of an object under evaluation, indicating the “worst” acceptable criteria in order to select an object from the point of view of that dimension. Consider the negative dimension $D ^ { \prime } .$ . If no more than two testing conditions can be satisfied in order for a software program to be accepted, the basic upper-bound threshold selection operator is defined as $\Omega _ { 2 } ( C _ { 1 } ^ { \prime } , C _ { 2 } ^ { \prime } , C _ { 3 } ^ { \prime } , C _ { 4 } ^ { \prime } , C _ { 5 } ^ { \prime } , C _ { 6 } ^ { \prime } )$

5.3.3.2. Conditional upper-bound threshold selection operator. If some testing conditions, e.g., $C _ { \mathrm { i } } ^ { \prime } { , } { . . . , } C _ { k } ^ { \prime }$ where $1 \leq i , k \leq n ,$ , must not be satisfied, then the basic upper-bound threshold operator can be refined as $\Omega _ { j , [ C _ { i } ^ { \prime } , C _ { i + 1 } ^ { \prime } , \dots , ~ C _ { k } ^ { \prime } ] } ( C _ { 1 } ^ { \prime } , C _ { 2 } ^ { \prime } , \dots , C _ { m } ^ { \prime } )$ . Since more strict condi-<sup>þ½ ð Þ</sup>tions are specified for the selection criteria, such an operator is called a conditional upper-bound threshold selection operator. According to its semantic meaning, an object can't satisfy more than j out of m testing conditions and $C _ { i } ^ { \prime } , C _ { i } ^ { \prime } + { } _ { 1 } , . . . , C _ { k } ^ { \prime }$ must be among the j conditions.

Consider the dimension $D '$ again. If the selected software will be used to develop a mission-critical project, the evaluator may not select any software that has the feature of cookie posing. Then condition $C _ { 5 } { ^ \prime }$ must not be satisfied. In this case, the conditional upperbound threshold selection operator is defined as $\Omega _ { 2 [ C _ { 5 } ^ { \prime } ] }$ $( { C _ { 1 } } ^ { \prime } , { C _ { 2 } } ^ { \prime } , { C _ { 3 } } ^ { \prime } , { C _ { 4 } } ^ { \prime } , { C _ { 5 } } ^ { \prime } , { C _ { 6 } } ^ { \prime } )$ , which indicates that at least two of $C _ { 1 } ^ { \prime } , C _ { 2 } ^ { \prime } , C _ { 3 } ^ { \prime } , C _ { 4 } ^ { \prime } , C _ { 5 } ^ { \prime }$ and $C _ { 6 } { ' }$ must not be satisfied and $C _ { 2 } { ' }$ must be one of them.

## 5.4. Inter-dimension evaluation

The low-bound and upper-bound threshold selection operators support decision-making from a single attribute perspective. To assess a given object from the multi-dimension point of view, an internal application must specify policies to make a balance among different dimensions.

Recall that an attribute dimension describes one aspect of the quality or security features of a type of objects. An evaluator needs to weigh the importance of different dimensions and maintain a balance between the minimum required positive features and the most tolerable negative features. More specifically, an internal application may accept an object if it has at least certain “strong” values for the attributes of some crucial positive dimensions but at the same time the evaluated utilities based on its values for the attributes of other non-crucial negative dimensions are not worse than a tolerable threshold. A simple example can further illustrate this idea. The decision policies specified by an internal application may indicate that a software program can be selected if it satisfies: (1) the scalability criteria defined based on attributes of dimension $D ; ( 2 )$ at least two testing conditions defined based on the attributes of dimension $D ^ { \prime \prime }$ about the functional correctness of the software program; and (3) no more than two of the six testing conditions defined based on the attributes of dimension $D '$ . Dimension D and $D ^ { \prime }$ were defined in Sections 5.3.2 and 5.3.3 respectively. Dimension $D ^ { \prime \prime }$ consists of three attributes: (a) static analysis of algorithms used in the software program; (b) dynamic testing of software program with a set of well-prepared inputs; and (c) user feedbacks about the functions of the software program; the first two dimensions represent an evaluator's expectations towards the necessary positive features that any selected software must have. At the same time, the evaluator requires that the software possesses no negative security features worse than those indicated by the third dimension. Any software can be selected only if it has positive features at least as good as those specified in the first two dimensions and at the same time it has no negative features worse than those specified in the third dimension. The balance between the positive and negative features for an object is achieved using logical operators such as AND and OR as shown in a trust zone mapping policy below.

## 5.5. Trust zone and trust zone mapping

Objects are first selected at the system level, which all satisfy the system-wide requirements for information assurance. Before they can be safely used by internal applications, those objects are further clustered into different groups. This is the second level of decisionmaking process (see Fig. 2).

Organizing and clustering external objects appropriately serves two purposes: minimizing security risks of executing external software and limiting their usage by internal applications. The first objective is to make sure that any accepted external programs will not compromise local systems or introduce security vulnerabilities. In light of this, external software should be assigned with different privileges to access local resources. Privileges can be defined on a group basis. Any object mapped to one group automatically inherits the access rights assigned to this group. Internet Explorer, for instance, isolates the downloaded websites from native documents in local systems. It defines five zones: Internet, Local Intranet, Trusted Sites, Restricted Sites, and My Computer. Web sites in each zone have different levels of security restrictions to access local resources. The second purpose of clustering selected objects is to make sure that they will be used appropriately to build larger-scale projects with different usages.

Definition 8. A trust zone represents a logical group of objects, all of which satisfy the requirements of an internal application for information quality and/or security and hence can be assigned appropriate privileges to access local resources and used for intended purposes.

One important aspect of information assurance is to disseminate data to different groups based on their features. Objects are mapped to different trust zones based on a set of policy rules as discussed next.

## 5.5.1. Trust zone mapping policy and trust zone mapping graph

A trust zone mapping policy consists of a set of logical rules using the upper-bound and low-bound threshold selection operators and logical operators such as AND, and OR. Such a policy determines the trust zone (s) to which an object can be mapped. An object can be mapped to one or more trust zones according to its values of attributes in the dimensions under consideration. A formal specification of a trust zone mapping policy with a set of logical rules is shown in Fig. 8.

An AND–OR graph-like data structure, called a trust zone mapping graph, represents a mapping policy defined for a trust zone. In such a graph, the root is labeled with the identifier of the trust zone. Each of the leaf nodes represents a testing condition defined based on an attribute in a dimension. An internal node represents an AND, OR, $\varTheta _ { j , \phantom { } }$ or $\Omega _ { i }$ operator. $\mathrm { ~ A ~ } \Theta _ { j , }$ or $\Omega _ { i }$ node relates the testing conditions defined based on the attributes of the same dimension.

```txt
trustZonePolicy ::= statement | statementSet
statementSet ::= statement statementSet | ε
statement ::= conditions → zoneName
zoneName ::= STRING
conditions ::= condition op1 conditions | condition | ε
condition ::= op2(testingList)
op1 ::= AND | OR
op2 ::= θj | Ωi | θj,[testingList] | Ωi,[testingList]
testingList ::= testing COMMA testingList | testing | ε
testing ::= testing condition identifier
```  
Fig. 8. Specification of a trust zone mapping policy.

## 5.5.2. A case study

This case study illustrates how an internal application defines a trust zone mapping policy to organize a software program into the appropriate trust zone(s). The following testing conditions are defined based on the attributes identified for the type of software of interest:

$C _ { 1 } \colon$ algorithms used in a candidate software program are analyzed to be correct

$C _ { 2 } \mathrm { : }$ the software program is tested and produces correct outputs given a set of well-prepared inputs

$C _ { 3 } \mathrm { : }$ users provide positive feedbacks about the functions of the software program

$C _ { 4 } \mathrm { : }$ the software program is scalable and tested in real use through a real-world deployment with positive reports

$C _ { 5 } { \mathrm { : } }$ the software program was designed with scalability in mind and has been verified by the evaluator by reviewing the detailed software engineering practices

$C _ { 6 } \mathrm { : }$ the software program was developed to allow third-party plug-ins

$C _ { 7 } { \mathrm { : } }$ the software program allows for extensions via a public API and shows design for scalability

$$
C _ {8}:
$$

$$
C _ {9}:
$$

$C _ { 1 } { } ^ { \prime } \colon$ the software program carries valid security-proof code supplied by the software producer

$C _ { 2 } ^ { \prime } { : }$ : the software program has been monitored by CERT and no open security vulnerabilities are outstanding

$C _ { 3 } { } ^ { \prime }$ : the software program has very few security bugs reported by users since its release

$C _ { 4 } { } ^ { \prime } \mathrm { : }$ : the software program leaves executable code segments in memory after execution

$C _ { 5 } { } ^ { \prime } \colon$ the software program accesses memory out of its allocated address space

$C _ { 6 } ^ { \prime } \mathrm { : }$ the software program has the problem of memory leak

$C _ { 7 } ^ { \prime } \mathrm { : }$ the software program creates hidden network connections and listens at privilege ports

$C _ { 8 } ^ { \prime } \colon$ the software program automatically turns on parsimonious mode and intercepts network traffic

$C _ { 9 } ^ { \prime } \mathrm { : }$ the software program uses weekly seeded cryptographic keys for network communications

$C _ { 1 0 } ^ { \prime } \colon$ the software program permits default passwords $C _ { 1 1 } ^ { \prime }$ : the software program permits relative and/or default directory paths

$C _ { 1 2 } ^ { \prime }$ : the software program exchanges sensitive information in default plain text across networks

$C _ { 1 3 } ^ { \prime }$ : the software program accepts arbitrary-length files as input

$C _ { 1 4 } ^ { \prime }$ : the software program forcefully browses

$C _ { 1 5 } ^ { \prime }$ : the software program uses cross-site references

$C _ { 1 6 } ^ { \prime } \colon$ the software program manipulates hidden-fields of files

$C _ { 1 7 } ^ { \prime }$ : the software program has the feature of cookie poising

$C _ { 1 8 } ^ { \prime }$ : the software program writes to local file systems

Testing conditions $C _ { 1 } , C _ { 2 }$ , and $C _ { 3 }$ are defined based on quality-oriented positive attributes of a dimension focusing on functional correctness of a type of software programs. $C _ { 4 } , \ C _ { 5 } , \ C _ { 6 } ,$ and $C _ { 7 }$ are defined based on quality-oriented positive attributes of a dimension regarding scalability of the software programs. $C _ { 8 }$ and $C _ { 9 }$ are defined based on quality-oriented negative attributes of a dimension describing inter-process communications of the programs. $C _ { 1 } ^ { \prime } , \ C _ { 2 } ^ { \prime }$ , and $C _ { 3 } { ' }$ are related to the security-oriented positive attributes of a dimension about third-party testable security features of the programs. $C _ { 4 } ^ { \prime } , C _ { 5 } ^ { \prime }$ and $C _ { 6 } { } ^ { \prime }$ are defined based on the security-oriented negative attributes of a dimension about memory management. $C _ { 7 } ^ { \prime } , \ C _ { 8 } ^ { \prime } .$ , and $C _ { 9 } ^ { \prime }$ are associated with the security-oriented negative attributes of a dimension about networking and data communications. $C _ { 1 0 } ^ { \prime } , \ C _ { 1 1 } ^ { \prime }$ and $C _ { 1 2 } ^ { \prime \prime }$ correspond to the securityoriented negative attributes of a dimension about risks of using default values. $C _ { 1 3 } ^ { \prime } , C _ { 1 4 } ^ { \prime } , C _ { 1 5 } ^ { \prime } , C _ { 1 6 } ^ { \prime } , C _ { 1 7 } ^ { \prime }$ and $C ^ { \prime } { } _ { 1 8 }$ are defined according to the security-oriented negative attributes of a dimension about I/O operations and program interfaces. An example of mapping policy for Trust Zone 1 is defined below and the corresponding trust zone mapping graph is shown in Fig. 9. $\{ \theta _ { 2 } ( C _ { 1 } , C _ { 2 } , C _ { 3 } ) \mathrm { A N D } \theta _ { 3 } ( C _ { 4 } , C _ { 5 } , C _ { 6 } , C _ { 7 } )$ AND $\Omega _ { 0 } ( C _ { 8 } , C _ { 9 } ) \}$ <sup>f ð</sup>AND $\{ \theta _ { 1 } ( \ C _ { 1 } ^ { \prime } , \ C _ { 2 } ^ { \prime } , \ C _ { 3 } ^ { \prime } )$ OR $[ \Omega _ { 0 } ( \ C _ { 4 } ^ { \prime } , \ C _ { 5 } ^ { \prime } , \ C _ { 6 } ^ { \prime } )$ AND $\Omega _ { 0 } ( { \cal C } _ { 7 } ^ { \prime } ,$ <sup>ð</sup>C V; C V AND $\Omega _ { 2 [ C _ { 1 } \acute { 2 } } ( \ C _ { 1 0 } \ \ : C _ { 1 \acute { 1 } } , \ C _ { 1 2 } )$ AND $\Omega _ { 4 [ C _ { 1 3 } ; C _ { 1 7 } ] } ( C _ { 1 3 } ^ { \prime } C _ { 1 4 } ^ { \prime } C _ { 1 5 } ^ { \prime } C _ { 1 6 } ^ { \prime }$ C V; C V YTrust Zone 1

Each trust zone is assigned a set of privileges for those objects mapped to this trust zone to access local resources. Access control is expressed by a mapping between $Z { \longrightarrow } R \times O _ { \mathrm { { \scriptsize { i } } } }$ , where Z represents a set of trust zones, R represents a set of access rights, e.g., read, write, and execute, and O represents a set of protected local resources. An object mapped to a trust zone inherits all the rights assigned to that trust zone and can only access resources as defined. If an object has been mapped to multiple trust zones, then its access rights are the accumulation of those defined for all the mapped trust zones.

Consider the following situation. According to the principle of least privilege, system administrators only allow external programs that have been mapped to Trust Zone 1 to access files on public drive $D _ { 1 }$ with full set of rights (i.e., read, write, and execute), read and execute files on drive $D _ { 3 }$ , which hosts the system’s web pages, and read files on a drive $D _ { 2 } ,$ which the objects need to access in order to complete their tasks. The mapping between Trust Zone 1 and the assigned access rights is illustrated below (where symbols R, W and E represent read, write, and execution respectively): Trust Zone 1Y $\{ [ D _ { 1 } : R , W , E ] , [ D _ { 2 } : R ] , [ D _ { 3 } : R , E ] \}$

![](/api/attachments/B4YSPHWX/fulltext/images/2db1992fc51aca87fe69d6255a1e5c00d0246c5b8b062857d538fea159d4b8f0.jpg)  
Fig. 9. Mapping graph for trust zone 1.

Access rights can be abbreviated as “All” if there is no restriction for external objects to access local resources. This should be only applied to those highly trustworthy objects. In contrast, a default trust zone is assigned “no access right”, which essentially prohibits those external objects that are mapped to this zone from accessing any local resources. By default, all the objects are mapped to this trust zone.

Consider another situation. An internal application reuses selected software components as sub-routines to develop large-scale software projects with different target usage settings: experimentation, internal development, routine use, and mission-critical use. Consequently, different categories of projects have the corresponding requirements for their software components. In this case, the internal application maps externally selected software with a high level of quality and security to a trust zone whose member software can be used as components to develop mission-critical projects (see below).

Trust Zone 1YDeveloping Mission−critical projects

## 6. Conclusions

This paper addresses the issue of information assurance in a virtual organization (VO) environment. We present a two-level decision model to aid VO participants in selecting external information with required level of quality and security. Evaluating the trustworthiness of an object is challenging since it requires the evaluator to have solid domain knowledge about that object and have reliable resources to refer to. The proposed model guides users to go through two major steps to make the final decision. First, it allows users to explicitly express what features of an external object are desired and what features are not acceptable. The selection criteria are expressed as a set of policy rules, which are pre-defined based on a set of trustrelated attributes of the objects of interest. Secondly, the initially selected objects with different characteristics are reorganized into different groups (called trust zones) in such a way that those objects can be used in appropriate ways and/or access system resources in a controlled manner. Our framework guarantees that any selected objects have the required levels of security and quality features. The framework also offers flexibility for users to specify their decision criteria.

## Acknowledgement

The authors are thankful to Dr. Robert L. Herklotz for his support and the editors and anonymous reviewers for their valuable comments. The research effort of Dr.

Brajendra Panda has been supported by the US AFOSR under grant F49620-01-10346.

## References

[1] K.J. Adams, D.A. Bell, L.P. Maguire, J. McGregor, Knowledge discovery from decision tables by the use of multiple-valued logic, Artificial Intelligence Review 19 (2) (2003) 153–176.

[2] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (2008) 657–672.

[3] M. Blaze, J. Feigenbaum, J. Lacy, Decentralized trust management, Proceeding of the 17th IEEE Symposium on Security and Privacy, Oakland, California, USA, 1996, pp. 164–173.

[4] J. Busemeyer, A. Diederich, Survey of decision field theory, Mathematical Social Sciences 43 (3) (2002) 345–370.

[5] A. Caplin, J. Leahy, Psychological expected utility theory and anticipatory feelings, Quarterly Journal of Economics 116 (1) (2006) 55–79.

[6] Y. Chu, J. Feigenbaum, B. LaMacchia, P. Resnick, M. Strauss, REFEREE: trust management for web applications, World Wide Web Journal 2 (1997) 127–139.

[7] T.P.V. Dyke, L.A. Kappelman, V.R. Prybutok, Measuring information systems service quality: concerns on the use of the SERVQUAL questionnaire, MIS Quarterly 21 (2) (1997) 195–208.

[8] M. Elliott, W. Scacchi, Free software development: cooperation and conflict in a virtual organizational culture, Free/Open Source Software Development, IDEA Group Publishing, 2004.

[9] J. Feigenbaum, Overview of the AT&T Labs Trust Management Project: position paper, Proceeding of the 1998 Cambridge University Workshop on Trust and Delegation, Cambridge, UK, 1998.

[10] S. Gao, H. Wang, D. Xu, Y. Wang, An intelligent agent-assisted decision support system for family financial planning, Decision Support Systems 44 (2007) 60–78.

[11] D. Gefen, E. Karahanna, D. Strub, Trust and TAM in online shopping: an integrated model, MIS Quarterly 27 (1) (2003) 51–90.

[12] J. Greene, J. Baron, Intuitions about declining marginal utility, Journal of Behavioral Decision Making 14 (3) (2001) 243–255.

[13] R. Harris, Introduction to Decision Making, http://www.virtualsalt. com/crebook5.htm (access date: December 1, 2007).

[14] A.C. Kerchhoff, K.E. Davis, Value consensus and need complementarily in mate selection, American Sociological Review 27 (1962) 295–303.

[15] W.J. Kettinger, C.C. Lee, Pragmatic perspectives on the measurement of information system service quality, MIS Quarterly 21 (2) (1997) 223–240.

[16] P. Herrmann, Trust-based protection of software component users and designers, Proceeding of 1st International Conference on Trust Management, Heraklion, Greece, 2003.

[17] D.J. Kim, D.L. Ferrin, H.R. Rao, A trust-based consumer decision-making model in electronic commerce: the role of trust, perceived risk, and their antecedents, Decision Support Systems 44 (2008) 544–564

[18] K.J. Kim, I. Han, The extraction of trading rules from stock market data using rough sets, Expert Systems 18 (4) (2001) 194–202.

[19] W. Lee, Decision Theory and Human Behavior, John Wiley & Sons, Inc., New York, 1971.

[20] J. Leimeister, W. Ebner, H. Krcmar, Design, implementation, and evaluation of trust-supporting components in virtual communities for patients, Journal of Management Information Systems 21 (4) (2005) 101–136.

[21] I. Linkov, A. Varghese, S. Jamil, T. Seager, G. Kiker, T. Bridges, Multi-criteria decision analysis: a framework for structuring remedial decisions at the contaminated sites, Comparative Risk Assessment and Environmental Decision Making, Springer, New York, 2004.

[22] R. Meyer, A. Sathi, A multi-attribute model of consumer choice during product learning, Marketing Science, 4 (1) (1985) 41–46.

[23] A. Parasuraman, V.A. Zeithaml, L.L. Berry, A conceptual model of service quality and its implications for future research, Journal of Marketing 49 (4) (1985) 41–50.

[24] P.A. Pavlou, D. Gefen, Building effective online marketplace with institution-based trust, Information Systems Research 15 (1) (2004) 37–59.

[25] A. Pilz, Policy-maker: a toolkit for policy-based security management, Network Operation and Management Symposium Vol. 1 (2004) 263–276.

[26] W. Scacchi, J. Feller, B. Fitzgerald, S. Hissam, K. Lakhani, Understanding free/open source software development processes, Software Process – Improvement and Practice 11 (2) (2006) 95–105.

[27] S. Schocken, G. Ariav, Neural networks for decision support: problems and opportunities, Decision Support Systems 11 (5) (1994) 393–414.

[28] J. Seigneur, Security evaluation of free/open source software powered by a peer-to-peer ecosystem, Proceeding of EFOSS OpenBRR Workshop, Como, Italy, 2006.

[29] J. Song, F. Zahedi, Trust in health infomediaries, Decision Support Systems 43 (2007) 390–407.

[30] T. Sueyoshi, G.R. Tadiparthi, An agent-based decision support system for wholesale electricity market, Decision Support Systems 44 (2008) 425–446.

[31] A. Wasserman, M. Pal, C. Chan, The business readiness rating model: an evaluation framework for open source, Proceeding of EFOSS OpenBRR Workshop, Como, Italy, 2006.

[32] R. Watt, Defending expected utility theory, Journal of Economic Perspectives 16 (2) (2002) 227–229.

[33] A. Whinston, Intelligent agents as a basis for decision support systems, Decision Support Systems 20 (1) (1997) 1.

[34] R.L. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11 (5) (1994) 545–557.

[35] Z. Yan, R. Maclaverty, Automatic trust management in a component based software system, Proceeding of the 3rd International Conference on Autonomic and Trust Computing, Wuhan, China, 2006.

[36] I. Yang, Utility-based decision support system for schedule optimization, Decision Support Systems 44 (2008) 595–605.

[37] J. Zeleznikow, J.R. Nolan, Using soft computing to build real world intelligent decision systems in uncertain domains, Decision Support Systems 31 (2) (2001) 263–285.

Yanjun Zuo is an assistant professor at the University of North Dakota, Grand Forks, USA. He earned his Ph.D. in Computer Science from the University of Arkansas, Fayetteville, USA in 2005. He also holds two master’s degrees in Computer Science and Business Administration from the University of Arkansas and the University of North Dakota, Grand Forks, USA, respectively. His research interests include information and computer security, trustworthy computing, survivable and self-healing systems, and information privacy protection. He has published numerous articles in referred journals and conference proceedings in these fields.

Brajendra Panda is a professor at the University of Arkansas, Fayetteville, USA. He received his Ph.D. in Computer Science from North Dakota State University, Fargo, USA in 1994 and a master’s degree in mathematics from Utkal University, India in 1985. His research interests include database systems, trusted database systems, computer security, computer forensics, and information assurance. He has published extensively in these fields.
