---
otero_id: 21385
otero_key: "H6ZMNYC5"
title: "A connectionist approach for similarity assessment in case-based reasoning systems"
authors: "Kalyan Moy Gupta; Ali Reza Montazemi"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00063-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A connectionist approach for similarity assessment in case-based reasoning systems

Kalyan Moy Gupta ${}^{a,b,*}$ , Ali Reza Montazemi ${}^{b}$

$^{a}$ Atlantis Aerospace Corporation, 1 Kenview Boulevard, Brampton, Ontario, Canada, L6T 5E6 $^{b}$ Michael G. DeGroote School of Business, McMaster University Hamilton, Ontario, Canada, L8S 4M4

Accepted 9 September 1996

## Abstract

Case-Based Reasoning (CBR) systems support ill-structured decision making. In ill-structured decision environments, decision makers (DMs) differ in their problem solving approaches. As a result, CBR systems would be more useful if they were able to adapt to the idiosyncrasies of individual decision makers. Existing implementations of CBR systems have been mainly symbolic, and symbolic CBR systems are unable to adapt to the preferences of decision makers (i.e., they are static). Retrieval of appropriate previous cases is critical to the success of a CBR system. Widely used symbolic retrieval functions, such as nearest-neighbor matching, assume independence of attributes and require specification of their importance for matching. To ameliorate these deficiencies connectionist systems have been proposed. However, these systems are limited in their ability to adapt and grow. To overcome this limitation, we propose a distributed connectionist-symbolic architecture that adapts to the preferences of a decision maker and that, additionally, ameliorates the limitations of symbolic matching. The proposed architecture uses a supervised learning technique to acquire the matching knowledge. The architecture allows the growth of a case base without the involvement of a knowledge engineer. Empirical investigation of the proposed architecture in an ill-structured diagnostic decision environment demonstrated a superior retrieval performance when compared to the nearest-neighbor matching function. © 1997 Elsevier Science B.V.

Keywords: Case-based reasoning; Adaptive decision support systems; Connectionist networks; Information retrieval

## 1. Introduction

The paradigm of Case-Based Reasoning (CBR) has been used effectively in domains where decision problems are open ended and where no clear cut methods are available to solve them $[19,31,42,49,65]$ . A CBR system reasons by remembering previous decision problems: it uses their outcome to evaluate new decision problems $[34]$ . The processes followed by a CBR system is as follows [53,62]: to assist a decision maker (DM), previous case(s) that closely resemble the new decision problem (new case) is(are) retrieved. The solution of the previous case is then mapped as a solution for the new case. The mapped solution is adapted to account for the differences between a new case and a previous case. For future decision making, feedback of the success or failure of the solution is obtained from the DM.

CBR systems support individual DMs faced with ill-structured decision problems. Ill-structured decision problems are characterized by a large number of variables, incomplete information, and uncertainty of relationships among these variables. As a result, cut-and dried solution techniques for these problems do not exist, and solutions cannot be characterized as right or wrong [44,60]. In such decision environments, DMs differ in their approaches to problem solving [37,41,43]. Therefore, DSSs that adapt to the idiosyncrasies of individual DMs are most desirable [39].

Existing implementations of CBR are mainly symbolic. However, symbolic CBR systems are static: they are unable to adapt to the preferences of DMs. The measure of the success of a CBR system depends on its ability to retrieve the most relevant previous cases in support of the solution of a new case $[47]$ . One of the methodologies widely used in existing symbolic CBR systems to retrieve previous cases is that of the nearest-neighbor (NN) matching function $[30]$ . The NN matching function is based on assumptions of the independence of attributes in previous cases and the availability of rules and procedures for matching. However, little has been done to verify these assumptions in domains in which CBR has been applied $[28]$ .

Connectionist systems have been proposed to ameliorate deficiencies inherent in symbolic matching systems $[5,67]$ . However, existing connectionist implementations of CBR systems are limited in their ability to grow and adapt. In this paper, we present a combination of connectionist and symbolic architecture that adapts to the preferences of DMs and that additionally ameliorates the assumptions of symbolic matching. An empirical investigation of our proposed connectionist architecture was performed by developing a CBR application for diagnosis and repair of A.C. motors.

The remaining paper is structured as follows. In Section 2, we provide a brief overview of the methodologies for retrieving previous cases and the assumptions that underlie the existing retrieval methodologies. Section 3 provides an overview of connectionist retrieval methodologies. Section 4 presents the proposed connectionist architecture for matching in a CBR system. Section 5 describes the empirical evaluation of the connectionist architecture. Findings of the empirical evaluation are presented in Section 6 and are discussed in Section 7. Section 8 concludes the paper.

## 2. Retrieval in CBR systems

The aim of case-based retrieval is to retrieve previous cases of most use towards solution of a new decision problem and to ignore irrelevant previous cases $[32,36]$ . Retrieval in CBR consists of the following steps (see Fig. 1): Based on a description of the new decision problem (i.e., the new case) the case-base is searched for candidate previous cases that have a potential to provide decision support. Searching increases the efficiency of the retrieval because only a subset of the case-base is examined. However, the effectiveness of the selection process toward choice of the most appropriate previous cases (i.e., the most appropriate cases may not be retrieved) is not guaranteed. Effectiveness of retrieval is based on the matching process.

## 2.1. Matching

Matching assesses the degree of similarity of a candidate previous case with a new case as follows: case can be considered as a schema that consists of a set of attribute value pairs (i.e., descriptors) [18,30]. For example, in a credit assessment decision scenario, a Loan Manager assesses several descriptor pairs (e.g., descriptor ‘Character of the applicant’ has a value of ‘average’). Matching involves establishing the similarity of the schema of the new case with the schema of the previous case (e.g., See SIZZLE [45]). Matching proceeds as follows (see Fig. 1).

![](/api/attachments/H6ZMNYC5/fulltext/images/dabaeeec4af51e2f1208bcc9e8f5ab9ddf0dd51a4928a12edaf33a7376285376.jpg)  
Fig. 1. Component processes in CBR retrieval.

First, the pair-wise similarity along the descriptors of the schemata of the new case and the previous case is assessed. Similarity of schemata of two cases along descriptors can be assessed using domain knowledge in the form of heuristics and domain specific matching rules (e.g., JULIA [33], and PRO-TOS [50,63]). For example, a matching rule determines that the descriptor 'color of the object' with value orange is very similar to the descriptor with value red.

Second, a matching function is used to assess the overall similarity of the schemata of a new case with a previous case. Here, we focus on methodologies for assessing overall similarity. The overall similarity of a new case with the previous case is assessed by aggregation of pair-wise similarity along descriptors. Overall similarity can be determined by the following two functions: (1) Tversky's matching function [69], and (2) Nearest-Neighbor (NN) matching function [15]. Tversky's matching function has been applied successfully in a CBR system for model management [48]. However, it has not been used in other domains because the pair-wise similarity is considered as binary and does not incorporate domain knowledge. In complex ill-structured decision problems, the use of domain knowledge is necessary for good retrieval performance of the CBR system [7], [20]. Therefore, in this paper, we do not consider the Tversky's matching function.

The NN matching function incorporates domain knowledge and has been widely used in the existing CBR systems (e.g., [10,14,25,30]). The overall similarity (OS) determined by NN matching function is mathematically represented as follows:

$$
\mathrm{OS} ^ {\mathrm{NN}} \left(\mathrm{n}, \mathrm{p} _ {k}\right) \frac {\sum_ {i = 1} ^ {m} w _ {i} \operatorname{sim} \left(a _ {i} ^ {\mathrm{n}} , a _ {i} ^ {\mathrm{p} _ {k}}\right)}{\sum_ {i = 1} ^ {m} w _ {i}},\tag{1}
$$

where, $a_{i}^{n}$ is the ith descriptor of the new case; $a_{i}^{P_{k}}$ is the ith descriptor of the kth candidate previous case; the superscripts n and p refer to the new case and the previous case respectively; $\text{sim}(\cdot)$ is a function, rule, or heuristic that determines the pair-wise similarity along a descriptor; and $w_{i}$ is the weight representing degree of importance of the ith descriptor towards the decision problem.

The NN matching function is based on four assumptions. The first assumption is in regard to the mutual independence of descriptors of a case, and the next three assumptions are related to the use and acquisition of weights in NN matching function. These four assumptions are as follows:

1. The linear combination assumes mutual independence of the descriptors of a case, and that the overall similarity is an additive combination of pair-wise similarity. However, the goal of CBR is to support ill-structured decision making in domains where descriptors have complex interrelationships. Under these circumstances, the number of descriptors and their possible values are potentially large, and the matching along descriptors is fuzzy and partial. Often, the dependence among descriptors is conditional on their values. Therefore, in order to reduce their effect on the assessment of overall similarity, statistical techniques cannot be used for determining these dependencies. For example, let us consider a complex decision domain such as the problem of diagnosing an A.C. motor fault. In a domain of this complexity the troubleshooter has to consider multiple faults scenarios. In these types of environments, non-linearity can arise when matching a previous case with multiple faults, such as 'Damaged Shaft' and 'Overload'. Since 'Overload' is (sometimes) caused by 'Damaged Shaft', they are related. Hence for this previous case, the feature 'Overload' is of greater importance when 'Damaged Shaft' is investigated. Errors can be introduced when using a linear combination of pair-wise similarity because relationships among descriptors can be ignored [22]. Therefore, a matching technique that can deal with non-linear relationships among the descriptors would be most useful.

2. The importance of descriptors is acquired by a knowledge engineer from experts or by a machine learning technique such as explanation-based learning [7,12]. A heuristic is used to transform the subjective notion of importance into numbers, and trial and error is used to refine these numbers to give a satisfactory performance. The underlying assumption is that the DM can provide an explanation of the degree of importance of a descriptor. However, the goal of CBR is to support ill-structured decision making where domain knowledge is noisy and weak. Therefore, it is difficult for a DM to provide an accurate assessment of the degree of importance of pertinent descriptors. The question arises whether it is possible to determine the importance of weights without explicit input from the DM.

3. In the existing CBR systems, the weights used are always positive. This is because of the singular emphasis on similarity. However, it would be much more useful if the presence of a descriptor in the new case that had an adverse effect on the usefulness of a candidate previous case be weighted negatively. This is similar to the notion of confirmatory and disconfirmatory evidence in evidential reasoning systems [57]. Evidential reasoning has been incorporated into CBR systems, in part, by including deep knowledge in form of validity constraints [17,58,68] censors [50], exclusion criteria [30] and causal models [35]. However, such systems assume that the constraints, censors, and exclusion criteria are known with certainty. Furthermore, the application of more than one constraint is not considered and the assumption is that constraints are independent of each other. For instance, in the A.C. motors decision domain, a previous case of overheating and tripping is considered appropriate towards the diagnosis of a motor of 'size' medium when the value of descriptor 'voltage drop' is greater than 15% of rated voltage and the value of descriptor 'current drawn' is greater than 10% of the rated current. However, these constraints take on different degrees of importance when the appropriateness of the same previous case toward a new case with a motor of 'size' large is assessed. This is because of the interrelationship of constraints on descriptors 'voltage drop' and 'current drawn' with the descriptor 'motor size'. Accurate assessment of these constraints is difficult due to their interrelationships with other descriptors. The question is how might we take into account the interaction effect among constraints.

4. It is not only the similarity between the new case and the previous case that determines usefulness of a previous case towards a new case, but also the similarities and differences among the candidate previous cases [1]. Therefore, the usefulness of a previous case towards solution of the new case is dependent on the presence of other candidate previous cases (i.e., matching is competitive). For instance, in the domain of A.C. motors, a previous case explaining 'failure of thermal protection mechanism' with a higher degree of overall similarity is considered secondary to a previous case with lower degree of overall similarity that explains 'winding failure'. The underlying reason is that 'winding failure' is considered as a catastrophic failure, and 'failure of thermal protection mechanism' a failure of less severity. In addition, these failures can have common causes. Matching techniques in most existing CBR systems assume that each candidate previous case is independent of the other. The interrelationship of previous cases is considered in HYPO by comparing them with each other based on each of the descriptors necessary to partially order the candidate previous cases [2]. However, this methodology has not been used in other application domains because of the difficulties inherent in determining the basis of ordering. Likewise, in PRO-TOS, explicit difference links are traversed to explain the new case [3]. Nonetheless, these differences are not used to determine the importance of descriptors in the context of a new case. The question arises as to what methodologies can be used to determine importance weights that take into consideration the presence of other candidate previous cases.

Artificial intelligence (AI) methodologies for problem solving can be broadly categorized into two categories: (1) symbolic, and (2) connectionist. Symbolic AI comprises a symbolic representation of knowledge coupled with a formal inferencing technique. These techniques have been successful in narrow, well-defined domains. However, symbolic AI has met with limited success in solving complex, ill-structured decision environments because of the brittleness problem [64]. Connectionist networks have been used to overcome some of the limitations of symbolic reasoning [26,64]. Integration of symbolic and connectionist systems has been suggested as a means to capitalize on strengths and overcome weaknesses $[25,70]$ . In the following section, we provide a brief overview of connectionist networks.

## 3. Connectionist networks

Connectionist networks are composed of relatively simple, neuron-like processing elements that store their knowledge in the strengths of connections between processors $[26]$ . The connectionist networks are based on an analogy with the biological structure of the brain which functions as a highly complex, non-linear, parallel information processing system $[54]$ . The capabilities of connectionist networks include: (1) the ability to determine non-linear relationships among objects (descriptors) in a domain; (2) to map a set of inputs to a set of outputs; (3) to learn or adapt to the changes in environment by alteration of connection strengths and by processing information that is incomplete and noisy; and (4) to incorporate the effect of contextual information $[23]$ . These capabilities of connectionist networks can overcome the limitations of retrieval in symbolic CBR systems.

Connectionist network representations can be categorized as [26] (see Fig. 2): (1) Localist, and (2) distributed. Localist representations are those in which each processing element corresponds to a meaningful concept (i.e., descriptor), and each connection corresponds to a defined relationship. The localist representation is suitable for representing structured knowledge (e.g., semantic networks [56]). In a distributed representation, each processing unit may correspond to many descriptors, and vice-versa. Consequently, the structure of a distributed network does not correspond to the structure of relationships among the descriptors. However, distributed networks are capable of implicitly learning the relationships that best perform its intended function. Distributed networks adapt their reasoning process to the decision environment by changing the strength of their connections. A number of learning procedures have been developed for distributed representations. In contrast, structured localist networks lack suitable learning methodologies [26].

A few implementations of connectionist based CBR systems are reported in the literature. However, these implementations use localist representation techniques, and thereby they do not learn or adapt to decision environments. An overview of the connectionist implementations of CBR systems is presented next.

## 3.1. Connectionist implementation of CBR systems

The existing connectionist implementations of CBR systems have attempted to accomplish three objectives. The first objective was to improve the speed of retrieval and search. An example is PARADYME, which is a parallel implementation of its symbolic counterpart JULIA [33]. In

## a) Localist representation

b) Distributed representation  
![](/api/attachments/H6ZMNYC5/fulltext/images/48f40cb4f9d1babf0aefdfb4447a85146d7439b752c3835811b43a88a02e1ea1.jpg)  
Fig. 2. Categories of connectionist representation: (a) Localist representation; (b) Distributed representation.

PARADYME, previous cases are represented using scripts and memory organization packets (MOPs). The retrieval mechanism uses a localist representation of descriptors to retrieve previous cases by spreading activation [13]. Consequently, the relationships among the descriptors of a case are predefined by the knowledge engineer and no connectionist learning takes place. PARADYME assumes that the structure of relationships, although non-linear, is known. Likewise, CAPER, a CBR system used in the planning domain is one in which cases are represented as frames and propositions [27]. Matching is done by parallel implementation of the NN matching function. CAPER works in a way similar to Carbonell's derivational analogy [8] where the solution to a new decision problem is created by the repeated retrieval of very small snippets or propositions and propagating constraints. The structure of the relationship among the descriptors is replicated by the structure of the network in a localist representation. Since localist representations lack learning methodologies, connectionist learning is not implemented in this application.

The second goal of a connectionist CBR system was to overcome the rigidity of existing rule-based systems. For instance, CONPOSIT is a connectionist implementation of CBR that is a result of the extensions made to a connectionist implementation of a rule-based system [4]. CONPOSIT uses a configuration matrix memory to match and retrieve previous cases. It can represent different levels of abstraction and includes variable bindings. Likewise, ARCS is a CBR system in the domain of story understanding where previous cases are represented in form of propositions [66]. Retrieval is carried out by simultaneous satisfaction of semantic, structural and pragmatic constraints. CONPOSIT makes use of production rules and ARCs makes use of propositional calculus to represent the previous case, and this imposes a relationship structure. However, such a structure is restrictive in a complex ill-structured decision environment.

Finally, connectionist implementation of CBR systems have been made to ameliorate matching difficulties. For example, CAPS and CLIPS use self-organized feature maps to cluster similar design cases in the cluster memory, and previous cases are retrieved by accessing the required cluster and modifying the selected design by use of rules [9]. The connectionist network in CAPS and CLIPS is used to organize previous cases but not during the matching process itself. Becker and Jazayeri [5] and Thrift [67] have proposed a connectionist representation of previous cases in the form of a set of descriptors. However, these models assume that the strength of relationships can be specified by the knowledge engineer and that no learning is required. Matching consisted of a linear combination of descriptors. Therefore, independence of descriptors is assumed.

The issues pertaining to dependencies among the descriptors (e.g., connectionist hierarchy of descriptors) have been addressed by localist implementation of connectionist CBR systems. However, as noted earlier, a localist connectionist system is limited in its ability to adapt. In these systems, addition of cases to the case base requires a knowledge engineer to specify the relationship among the descriptors of the case and to position a new case in the retrieval hierarchy. Distributed connectionist implementation of CBR systems such as CAPS and CLIPs, although adaptive, have not addressed the issue of case base growth.

## 4. Proposed architecture

We propose a connectionist CBR architecture with a distributed representation to determine overall similarity (see Fig. 3). The proposed connectionist architecture is based on the following three capabilities of distributed connectionist networks:

1. Assessment of overall similarity is equivalent to a function that maps a set of inputs (i.e., pair-wise similarity along the descriptors of the new case) to the output (i.e., overall similarity of the new case with a previous case), where non-linearity may exist due to the existence of complex relationships among the descriptors of the decision problem domain. No assumption about the nature of the relationship among the descriptors is needed in a distributed connectionist network.

2. The importance of descriptors of a previous case can be inductively learned without explicitly asking the DM. The DM can indicate the degree to which a candidate previous case should be retrieved or rejected. The rejection of a candidate case will enable the system to acquire constraints on the descriptors.

![](/api/attachments/H6ZMNYC5/fulltext/images/c1ae554701e012abe488d3dd40935c18597dd778cddf22e81ef6b36c2f762fc2.jpg)  
Fig. 3. Modular connectionist architecture for overall similarity integrated with a symbolic architecture of a CBR system.

3. The inductive learning capabilities of connectionist networks can be used for adapting the importance of descriptors of a previous case to incorporate the presence of other candidate previous cases.

Let us assume that each previous case in the CBR system is represented by a set of descriptors. Each previous case can be considered as a prototype with relevant information useful toward the solution of a new decision problem. The applicability of a previous case to a new case is determined by matching. The architecture is based on the notion of modular networks [23]. Modular networks comprise of many sub-networks that work together as a whole. In the proposed architecture, each sub-network is an expert in retrieving the previous case that it represents. These sub-networks are called Expert Previous case Sub-Network (EPSN).

## 4.1. Expert previous case sub-network (EPSN)

An EPSN represents a previous case in the form of a network with a distributed representation. The function of the network is to determine overall similarity. An EPSN is a fully connected feed-forward network with one hidden layer (see Fig. 4). The input layer of an EPSN comprises of a node for each descriptor of the previous case, called a descriptor node. The pair-wise similarity along a descriptor determines the level of activation of the corresponding descriptor node. For example, in the decision domain of the diagnosis of A.C. motors, if the pair-wise similarity of the new case and the previous case along a descriptor 'low voltage' is assessed as 0.7, then the level of activation for the voltage descriptor neuron is 0.7. The output layer consists of a single node whose level of activation represents the extent of overall similarity of the previous case with the new case. The hidden layer includes the non-linearity needed to determine the overall similarity. The processing units (i.e., neurons) use a hyperbolic activation function. The activation level of an output node of a candidate EPSN determines its usefulness towards the new case. For example, an activation level of 0.8 of the output node of a candidate EPSN implies that the corresponding previous case is very useful towards the solution of the new case. Likewise, an activation level of -0.8 implies that the previous case is not useful and should not be presented to the DM.

![](/api/attachments/H6ZMNYC5/fulltext/images/f2f158dfd1fd47a393971cf97a8d17ff40a7d0db6bf942f22a05e6590a77fece.jpg)  
Fig. 4. Distributed representation of an EPSN.

## 4.2. Retrieval using ESPNs

## Retrieval with EPSNs proceeds as follows:

1. The candidate previous cases (i.e., candidate EP-SNs) are determined by a search module implemented in a symbolic architecture external to the connectionist architecture (see Fig. 3). For example, in our architecture, the previous cases with at least one matching descriptor are selected as candidates toward the solution of the new case.

2. The descriptor nodes of each candidate EPSN are activated based on its pair-wise similarity with the descriptors of the new case.

3. The EPSNs, whose output nodes are positively activated, are selected and rank-ordered based on their level of activation (e.g., +0.8 is ranked highest and 0 is ranked lowest). The EPSNs with negatively activated output nodes are not presented to the DM.

## 4.3. EPSN development

EPSNs are adaptive agents that retrieve previous cases. Adaptive agents can learn from two different sources [38]: (1) An agent learns from hypothetical examples – the hypothetical examples are created and the agent is explicitly told what to do in those cases, and (2) an agent can learn by continuously 'looking over the shoulder', that is, monitoring the actions of a DM. Similarly, EPSNs are first trained with hypothetical examples (i.e., instances of retrieval) to develop a general relationship among the descriptors. Next, the relationships among descriptors are adapted for each individual DM. The processes involved in executing these two phases are described next.

## 4.3.1. Phase I - EPSN training

An EPSN is trained as follows (see Appendix A for an example). For an EPSN to be added to the case base, several hypothetical training cases are randomly created by the system (see Fig. 5). For each hypothetical training case, the desired level of activation for the output node of an EPSN (i.e., overall similarity) is determined by the NN matching function by means of equally weighted descriptors, that is, an EPSN learns to assess overall similarity by a linear combination of similarity along descriptors. Since NN matching function is used, input from a knowledge engineer or a DM is not required at this stage. The training pattern consists of the activation of descriptor nodes based on pair-wise similarity of the previous case and the hypothetical training case together with the desired level of activation for the output node. The number of hypothetical training patterns needed for an EPSN depends on the size of the EPSN. The number of hidden nodes $(M)$ is approximately set at $\sqrt{N}$ for an EPSN with N descriptor nodes. On the basis of the heuristic that the size of training set should be approximately twice the number of connections in the network [40], $2 \cdot M \cdot (N + 1)$ hypothetical patterns are needed for training an EPSN. For instance, in an EPSN with eight descriptor nodes and two hidden nodes, 36 hypothetical training cases are needed. A new EPSN is trained on the hypothetical training set using the backpropagation algorithm [23] and added to the case base.

![](/api/attachments/H6ZMNYC5/fulltext/images/a38cc534c86a99a14f25e117e3dc7c9cdaf4da7facf69dc04398db43e6450cb5.jpg)  
Fig. 5. Phase I: Training and addition of an EPSN to the case base.

## 4.3.2. Phase II - EPSN adaptation

Once an EPSN is added to the case base it adapts to the preferences of a DM as follows (see Appendix A for an example). When a new case is presented to the CBR system, a set of candidate EPSNs is retrieved by means of the procedure described in Section 4.2. The DM is presented with the set of rank ordered previous cases. If the DM disagrees with the rank ordering, he/she specifies the desired rank ordering by means of a seven-point Likert-type scale to indicate the level of usefulness of the candidate previous cases toward solution of a new case. The response of the DM is transformed into the activation level for the output node in the interval [0.1,0.8]. The maximum usefulness is represented by a value of 0.8 instead of 1, thereby preventing the weights in the EPSN from becoming too large. The DM can also specify the degree of irrelevance of the EPSN using a seven-point Likert-type scale. In this scenario, the response of the DM is transformed into a negative activation level in the interval [-0.8, -0.1]. The degree of irrelevance can be interpreted as the DM's confidence in the irrelevance of the previous case towards the new case. For example, if the DM is very confident that the previous case is irrelevant, then the level of activation for the EPSN output node is set at -0.8. On the basis of DM's response, adaptation patterns are created for each candidate EPSN (see Fig. 6). Adaptation patterns are collected for an EPSN over many interactions with the DM. By means of backpropagation on these patterns the EPSNs are adapted. By adaptation, EPSNs learn how to retrieve candidate previous cases by taking into consideration the presence of other candidate previous cases in the context of a new case and include the dependencies among the descriptors. Next, we describe the empirical evaluation of the proposed architecture.

![](/api/attachments/H6ZMNYC5/fulltext/images/12d98887208468c08d46a6a426b0c55c3c64caf48cb8a4f6b79ded1c80f88cc8.jpg)  
Fig. 6. Phase II: Adaptation of EPSNs.

## 5. Empirical evaluation

## 5.1. Objective

The objective of our empirical evaluation was to compare the retrieval performance of proposed connectionist architecture for matching with the NN matching function.

## 5.2. Methodology

## 5.2.1. Environment

Using Case-Based Reasoning (CBR), we developed a DSS to assist the service personnel of a manufacturing and service organization diagnose and repair alternating current (A.C.) motors. These motors are used in diverse applications that range from driving exhaust fans in mine shafts to driving pumps in sewage stations. Given this diversity, a large number of combinations of symptoms and faults are possible. Decision problems associated with diagnosis and repair are by their nature ill-structured because there is no cut-and-dried method of handling them. Diagnosis and repairs are judged as good, bad, or reasonable, but never as correct or incorrect [39].

## 5.2.2. Subjects

The organization under study has several regional service divisions across Canada and a central engineering services division in Ontario. Each division has a team of service engineers who troubleshoot a variety of electrical machinery. Problems not solved at the regional level are referred to Central Engineering Services. Ten troubleshooters from Central Engineering Services and Regional Field Services participated in this investigation. All subjects had a college or university degree. Troubleshooting experience of subjects ranged from 4 to 30 years. Average experience was 10 years. All subjects were male.

## 5.2.3. Instruments

A single-item questionnaire was used to measure the usefulness of a retrieved previous case towards the new decision problem (test case) with a 7-point Likert-type scale [16]. This is based on the reported findings that usefulness and relevance of retrieved information are equivalent [52].

## 5.2.4. Tools

We used two tools in our investigation:

1. A Case-Based Reasoning Shell (CBRS) with a symbolic processing system was developed to incorporate the NN matching function. CBRS uses retrieval methodologies similar to those used in existing CBR systems. CBRS accepts description of a new case, retrieves most appropriate previous cases, and compares and analyzes the new case in light of retrieved previous cases. CBRS can also justify its retrieval and matching process. This shell was used to develop the Troubleshooting and Repair Assistant for A.C. motors (TRAAC). On the basis of a general diagnostic model [51], TRAAC assists a troubleshooter hypothesize faults and gather evidence, and retrieves previous cases to confirm or reject the proffered hypotheses. TRAAC was developed by priming CBRS with A.C. motor knowledge. Thirty-five representative previous cases from the service reports were selected in consultation with the DMs for priming the knowledge-base of TRAAC. The 35 previous cases were represented using a predefined descriptor vocabulary. The descriptor vocabulary comprised of 154 descriptors. The importance of descriptors for each previous case was provided by an expert troubleshooter by means of a seven-point Likert-type scale.

2. A system called CTRAAC (Connectionist TRAAC) was created by replacing the NN matching function of TRAAC by the 35 EPSN that represented the 35 previous cases. The symbolic search mechanism of TRAAC was used to generate the candidate EPSNs. Each EPSN had the same descriptors as did its counterpart in TRAAC. The number of descriptor nodes in an EPSN ranged from six to seventeen. On average, an EPSN consisted of eight input nodes, two hidden nodes, and one output node. Each EPSN was individually trained by randomly creating hypothetical training examples (i.e., Phase I). On average, a training set of size 30 was used, and a root mean squared error of less than 0.05 was obtained after 30,000 epochs.

Next, each of the thirty five previous cases were presented as new cases to the CTRAAC to adapt the EPSNs. The DM's desired ranking of candidate previous cases for each presentation was collected (i.e., Phase II). On average 10 adaptation patterns were collected for adapting each EPSN. Each EPSN was adapted using these patterns for 10,000 iterations. On average, a root mean squared error of less than 0.05 was obtained.

## 5.2.5. Test

Eleven test cases (i.e., new cases) representative of the problems that had occurred in the field were selected for our investigation. The diagnosis and the repair solution used in the test cases were known. To begin with, the functionality and the use of TRAAC for troubleshooting A.C. motors was demonstrated to the subject by use of a troubleshooting event that had occurred in the field. Then subject was provided with a warm-up test case to familiarize himself with the functionality of the system. This test case was removed from subsequent analysis. After the subject was comfortable with the system, he was given one test case at a time. Learning during the evaluation process can affect the response provided by the subjects [52]. Hence, test cases were given to each subject in a random order.

The subject was given the general specification of the A.C. motor application, and the initial report of symptoms for each test case. Based on the recommendations of TRAAC, the subject selected descriptors that described the test scenario. To simulate the conditions in the field, the subject was allowed to ask for any information regarding tests performed and the observations made. The response these questions when they arose was based on available information contained in the service reports.

Based on the test case description provided by the subject, TRAAC retrieved a subset of the 35 previous cases with any combination of symptoms, hypothesized faults, and presented them in a random order to the subject. After reading the content of each retrieved previous case, the subject rated it by means of the usefulness questionnaire. When the response indicated ties with the usefulness rating, the subject was given the option of expressing a preferred order among the tied, retrieved previous cases. On completion of the rating process, the subject wrote an analysis of the new case and suggested a repair technique. The experimental session comprising of the description of the new case, matching process, and retrieved previous cases was recorded by TRAAC for later analysis. On average, it took 45 min to complete the analysis of a test case. Due to the lack of time, the number of test cases assessed by the subjects varied between four and ten. A total of 80 test cases were analyzed by the 10 subjects.

## 5.2.6. Measure of CBR retrieval performance

Although a number of CBR systems have been reported in the literature, only a few have attempted to evaluate their performance [11]. Some CBR Systems have used classification accuracy as a measure of retrieval performance [50,61], while other CBR systems have used recall and precision to measure retrieval performance [36,59]. Recall and precision have been adopted from the information retrieval literature (e.g., see [28,29,46,55]). However, these measures are not suitable when multiple previous cases are retrieved and rank-ordered based on their degree of usefulness. This is because recall and precision ignore the rank-ordering of retrieved previous cases. Furthermore, use of these two measures (i.e., recall and precision) make comparison of alternative retrieval methodologies ambiguous.

A measure of retrieval performance of CBR system should incorporate the following four components:

1. retrieved previous cases that are useful to the new case;

2. retrieved previous cases that are not useful to the new case;

3. useful previous cases that are not retrieved; and

4. agreement of ranking produced by the CBR system and ranking expected by the DM.

We used the Kendal's Tau with ties [24] to measure a retrieval performance which incorporates the above four components [21]. Kendal's Tau with ties $(\tau)$ measures the agreement of judgments from two sources that produce ordinal ranking of a set of items. The two sources in the CBR retrieval evaluation are the rank ordering of previous cases determined by the usefulness rating of the retrieved previous cases provided by the DM and the rank ordering of the previous cases retrieved by the CBR system. $\tau$ determines the number of agreements and disagreements between the rank order by the DM and the rank order by the system and measures the statistical correlation between the two rank orderings.

## 5.2.7. Experimental design

To compare their relative performance, retrieval was carried out for each test case using TRAAC and CTRAAC. The retrieval performance of each retrieval methodology was determined for each test case by computing $\tau$ . The performance of TRAAC and CTRAAC was compared by conducting a nonparametric pair-wise signed test [24].

## 6. Analysis

The solution provided by the subjects for each test case was scored in accordance with the actual solution implemented in the field. The average score was 87.38%. The question arises as to whether there were any significant differences among the solutions provided by the subjects. To answer this question we adopted analysis of variance (ANOVA) of the scores. The results indicated that there was no significant difference among the subjects (p = 0.139, F = 1.58). Therefore, the subjects were uniformly competent in assessing the test cases (i.e., the new cases).

Retrieval was carried out by TRAAC, and CTRAAC using the description of the test cases provided by the subjects. $\tau$ was computed for the two systems, and comparisons were made using the pair-wise signed test. The analysis shows that CTRAAC performed significantly better than TRAAC (p = 0.0031) (see Table 1). This implies that the connectionist architecture we propose has a superior retrieval performance compared to that of the NN matching function. This is due to CTRAAC's ability to include the non-linearity arising from the complex interrelationships among descriptors and its ability to consider the effect of other candidate previous cases on matching. The retrieval performance of EPSN's over the set of test cases indicates that EPSN's of CTRAAC were able to generalize (i.e., provide a reasonably accurate response when presented with cases that were not used during training). Although, the retrieval performance of CTRAAC was significantly superior to TRAAC, it is important to analyze the instances in which CTRAAC lost to TRAAC. Our analysis indicated that among the ten test cases, in three CTRAAC did not perform as well as did TRAAC. This was due to inadequate training of EPSNs for retrieval towards these test cases. In a real decision environment, the response of the DM can be used by CTRAAC for the ongoing adaptation process. In fact, this ability provides a major advantage of CTRAAC over TRAAC.

## 7. Discussion

The effectiveness of a CBR system depends on its ability to retrieve appropriate previous cases in support of the solution of a new case. This, in turn, is based on its ability to match. Many existing symbolic CBR systems provide descriptor-based matching with a linear matching function such as the NN. These symbolic systems are unable to adapt to the preferences of DMs. We addressed this issue by proposing a connectionist architecture that adapts to a decision environment. Empirical testing of the proposed architecture in an ill-structured diagnostic domain demonstrated that it was capable of adapting to a decision environment and of incrementally acquiring matching knowledge (i.e., importance of descriptors in previous cases, rules, and procedures). This is in contrast to these symbolic CBR systems in which matching knowledge is predefined and static. However, in practice, a number of changes to matching knowledge are necessary as cases are added to the case base of symbolic systems $[36,59]$ .

Our proposed architecture also reduces some of the limitations of the existing connectionist architecture of CBR systems. These limitations include the following: (1) the inability to learn due to lack of learning methodologies for a localist representation, and (2) the difficulty associated with training large monolithic networks with distributed representation that can arise from the requirement of a large number of training cases. Additionally, cases cannot be added to monolithic connectionist networks. The proposed connectionist architecture is modular; hence, addition of a case (i.e., EPSN) does not affect the structure of other networks. Training an EPSN is feasible because of its small size compared to an equivalent monolithic network that represents all the previous cases. In the proposed architecture, a case is added to the case-base by adding a new EPSN. The new EPSN learns the matching knowledge required for its retrieval and adapts itself to the idiosyncrasies of the individual DMs.

Table 1  
Comparison of the nearest-neighbor with connectionist matching

<table><tr><td>Comparisons A vs. B</td><td>Wins  $\tau_{A} > \tau_{B}$ </td><td>Losses  $\tau_{A} < \tau_{B}$ </td><td>Draws  $\tau_{A} = \tau_{B}$ </td><td>z-value (Level of significance p)</td></tr><tr><td>CTRAAC vs. TRAAC</td><td>47</td><td>23</td><td>10</td><td>2.7490(0.0031)</td></tr></table>

Additionally, we raised the issue of non-linearity in overall similarity due to the interrelationships of descriptors in a complex decision domain. The proposed connectionist architecture acquires the non-linearity needed for assessing the overall similarity. Our empirical investigation shows that the proposed connectionist architecture has a superior retrieval performance compared to the NN matching function.

## 8. Concluding remarks

The proposed methodology is useful for ill-structured decision problems that require retrieval adaptable to a DM's decision style. The decision environment used to test our methodology was complex and ill-structured [41], and the subjects were domain experts. As a result, subjects favoured a DSS that could adapt to their individual decision style. In fact, a large expert system previously developed to provide them support was never used because of its rigidity and its inability to adapt to the individual decision behavior of the users. A major attractiveness of the CTRAAC for the subjects was its ability to adapt to their view of the nature of retrieved previous case(s).

While the results of our empirical tests are encouraging, we acknowledge that its context is limited. Ten DMs and 80 observations provided us with a reasonable sample size, but all concerned a given type of decision within the context of a given organization. It is our hope that this work will generate fruitful discussion and provoke further research. We suggest several directions. First, the issue of expanding the sample by application of the proposed methodology in a variety of different decision environments needs addressing. One could answer this question: how common are decision environments wherein the relationships among the values of the descriptors, rather than the mere values of individual descriptors, are important? Results taken from actual decisions might also address the problem of 'adaptiveness'. This latter issue poses yet another question: is adaptiveness desirable? Our proposed retrieval method relies on a DM's judgment to assess the usefulness of the retrieved previous cases in support of a new case. Bolger and Wright [6] contend that good judgmental performance can be expected from the DMs operating in environments with high 'learnability'. Learnability is defined by Bolger and Wright [6] as "the extent to which it is possible to master decision making and judgment in the task domain under investigation, specifically by making use of feedback to refine reliable domain models as a basis for subsequent judgment" (p. 20). The decision environment adopted for the test of proposed methodology can be categorized as having 'high learnability'. Therefore, in such an environment, an adaptive retrieval method for a CBR system is desirable.

However, for some decision tasks such as security analysis, adaptiveness of retrieval for each individual security analyst (i.e., DM) may be inappropriate. The reason is that in such a decision environment the 'learnability' of decision task is low. As a result, the DM's judgment for assessing the usefulness of the retrieved previous cases may follow a random behavior [43]. The question arises as to how might we provide adaptiveness for the environments categorized as having 'low learnability'.

Finally, a variety of preference heuristics have been proposed for assessing the usefulness of a previous case toward a new case $[32]$ . These include heuristics that favour a more recent previous case, and/or that favor a previous case more easily adapted. We need to assess the effectiveness of these heuristics within operational environments with high ecological validity.

## Acknowledgements

The authors would like to extend their appreciation to the employees of Westinghouse Canada Inc. for their help and cooperation in this research, and three anonymous reviewers for their helpful comments on the original version of this paper. This paper has been supported by Grant #39126 from Natural Sciences and Engineering Research Council of Canada.

## Appendix A

## A.1. Phase I - EPSN training

Consider three previous cases (EPSNs): $P_{1}$ , $P_{2}$ , and $P_{3}$ that are to be added to the case base. Let us assume that the descriptors of these three cases are as shown in the Table 2. For simplicity, assume that the assessment of similarity along the descriptors is binary (i.e., 0 and 1).

Consider the addition of the case $P_{1}$ to the case base. First, an untrained $EPSN_{1}$ with small random weights was created (see Fig. 7). Next, hypothetical training examples were created. These training examples consist of the activation level of the descriptors of $EPSN_{1}$ based on the extent of similarity along them and the activation level of the output node indicating the level of overall similarity. Four of the possible eight training examples are shown in Table 3. Finally, $EPSN_{1}$ was trained by means of backpropagation with the training examples and included in the case base. A similar process was followed to add the previous cases $P_{2}$ and $P_{3}$ to the case base.

## A.2. Phase II - EPSN adaptation

Consider the presentation of a new case $P_{4}$ (see Table 4) to the case base. Since the new case $P_{4}$ partially matches the previous cases, the connectionist CBR system retrieves the three previous cases $P_{1}$ , $P_{2}$ , and $P_{3}$ and presents them in the order shown in Table 5. However, the DM does not agree with the ranking and provides his own ranking of the retrieved previous cases by means of a seven-point Likert-type scale (see Table 5). The DM's ranking is used by the connectionist CBR system to create adaptation patterns for the previous cases $P_{1}$ , and $P_{3}$ as shown in Table 6. No pattern is created for $P_{2}$ since its ranking was not affected.

Table 2  
Descriptors representing the previous cases

<table><tr><td>Case</td><td colspan="3">Descriptors in cases</td></tr><tr><td> $P_1$ </td><td>A</td><td>B</td><td>C</td></tr><tr><td> $P_2$ </td><td>A</td><td>C</td><td>D</td></tr><tr><td> $P_3$ </td><td>B</td><td>C</td><td>E</td></tr></table>

![](/api/attachments/H6ZMNYC5/fulltext/images/9c78a01d69794fac4bafed72ffb302ac6559ea9d3bb9e142d740b7e2fb0ebc7a.jpg)  
Fig. 7. Untrained EPSN $_{1}$ .

Table 3  
Hypothetical training examples for EPSN $_{1}$

<table><tr><td rowspan="2">Training examples</td><td colspan="3">Descriptor nodes activation (similarity along descriptors)</td><td rowspan="2">Output node activation (overall similarity) $O(NN \cdot 0.8)$ </td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td> $T_1$ </td><td>1</td><td>1</td><td>1</td><td>0.80</td></tr><tr><td> $T_2$ </td><td>1</td><td>1</td><td>0</td><td>0.53</td></tr><tr><td> $T_3$ </td><td>1</td><td>0</td><td>0</td><td>0.26</td></tr><tr><td> $T_n$ </td><td>0</td><td>0</td><td>0</td><td>0.00</td></tr></table>

Table 4  
Descriptors representing the new case $P_{4}$

<table><tr><td>Case</td><td colspan="4">Descriptors in cases</td></tr><tr><td> $P_{4}$ </td><td>B</td><td>C</td><td>D</td><td>F</td></tr></table>

Table 5  
Ranking of previous cases by the system and the DM

<table><tr><td>Retrieved previous case</td><td>System ranking</td><td>DM&#x27;s ranking</td></tr><tr><td> $P_{3}$ </td><td>1</td><td>2</td></tr><tr><td> $P_{1}$ </td><td>2</td><td>1</td></tr><tr><td> $P_{2}$ </td><td>3</td><td>3</td></tr></table>

Table 6  
Adaptation patterns for $\mathbf{P}_1$ and $\mathbf{P}_2$

<table><tr><td>Previous case</td><td>A</td><td>B</td><td>C</td><td>E</td><td>Output activation</td></tr><tr><td> $P_{1}$ </td><td>0</td><td>1</td><td>1</td><td></td><td>0.64</td></tr><tr><td> $P_{3}$ </td><td></td><td>1</td><td>1</td><td>0</td><td>0.48</td></tr></table>

## References

[1] K.D. Ashley, Assessing similarity among cases: A position paper, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 72–75.

[2] K.D. Ashley and E.L. Rissland, A case-based approach to modeling legal expertise, IEEE Expert 3(3) (1988) 70–77.

[3] E.R. Bareiss, B.W. Porter and C.C. Wier, Protos: An exemplar-based learning apprentice, in: Machine Learning: An Artificial Intelligence Approach 3 (Morgan Kaufman, San Mateo, CA, 1990) 112–139.

[4] J. Barnden and K. Srinivas, Overcoming rule-based rigidity and connectionist limitations through massively parallel case-based reasoning, International Journal of Man-Machine Studies 36(2) (1992) 221–246.

[5] L. Becker and K. Jazayeri, A connectionist approach to case-based reasoning, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 213–227.

[6] F. Bolger and G. Wright, Assessing the quality of expert judgement: Issues and analysis, Decision Support Systems 11(1) (1994) 1–24.

[7] T. Cain, M. Pazzani and G. Silverstein, Using domain knowledge to influence similarity judgments, in: Proc. Case-Based Reasoning Workshop (Washington, DC, 1991) 191–198.

[8] J.G. Carbonell, Learning by analogy: Formulating and generalizing plans from past experience, in: R.S. Michalski, G.J. Carbonell and T.M. Mitchell, eds., Machine Learning, An Artificial Intelligence Approach (Palo Alto, CA, 1983).

[9] C.L. Chen and Y. Pao, An integration of neural network and rule-based systems for design and planning of mechanical assemblies, IEEE Transactions on Systems, Man, and Cybernetics 23(5) (1993) 1359–1377.

[10] Cognitive Systems, REMIND Developers Reference Manual (Boston, MA, 1992).

[11] P.R.Cohen, Evaluation and case-based reasoning, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 168–172.

[12] G. DeJong and R. Mooney, Explanation-based learning: An alternative view, Machine Learning 1(2) (1986) 145–176.

[13] E. Domeshek, Parallelism for index generation and reminding, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 244–247.

[14] D. Donahue, OGRE: Generic reasoning from experience, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 248–252.

[15] R. Duda and P. Hart, Pattern Classification and Scene Analysis (Wiley, New York, NY, 1973).

[16] M.B. Eisenberg, Measuring relevance judgements, Information Processing and Management 24(4) (1988) 373–389.

[17] T.C. Eskeridge, Continuous analogical reasoning: A summary of current research, in: Proc. of DARPA Workshop on

Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 253–257.

[18] D. Gentner, Structure mapping: A theoretical framework for analogy, Cognitive Science 7(2) (1983) 155–170.

[19] A.R. Golding and P.S. Rosenbloom, Improving rule-based systems through case-based reasoning, in: Proc. of ninth National conference on AI, AAAI 1 (1991) 22–27.

[20] K.M. Gupta and A.R. Montazemi, Retrieval in case-based reasoning with modified cosine matching function, Research and Working Paper Series, #401, School of Business, McMaster University, 1995.

[21] K.M. Gupta and A.R. Montazemi, A methodology for evaluating the retrieval performance of case-based reasoning systems, Research and Working Paper Series, #398, School of Business, McMaster University, 1994.

[22] S.J. Hanson, Conceptual clustering and categorization: Bridging the gap between induction and causal models, in: Machine Learning: An Artificial Intelligence Approach 3 (Morgan Kaufman, San Mateo, CA, 1990) 235–268.

[23] S. Haykin, Neural Networks: A Comprehensive Foundation (Maxwell Macmillan, Toronto, Canada, 1994).

[24] W.L. Hays, Statistics (Holt Rinehart and Wilson, New York, NY, 1963).

[25] S. Hedberg, New knowledge tools, Byte 18(8) (1993) 106-111.

[26] G.E. Hinton, Preface to special issue on connectionist symbol processing, Artificial Intelligence 46(1-2) (1990) 1-4.

[27] B.P., Kettler, J.A. Hendler, W.A. Anderson and M.P. Evett, Massively parallel support for case-based planning, IEEE Expert 9(1) (1994) 8–14.

[28] J. King and R. Bareiss, Similarity assessment in case-based reasoning, Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 67–77.

[29] D.W. King and E.C. Bryant, The Evaluation of Information Services and Products (Information Resources Press, Washington, DC, 1971).

[30] J.L. Kolodner, Case-Based Reasoning (Morgan Kaufman, San Mateo, CA, 1993).

[31] J.L. Kolodner, Improving human decision making through case-based decision aiding, Al Magazine 12(2) (1991) 52–68.

[32] J.L. Kolodner, Judging which is the best case for a case-based reasoner, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, CA, 1989) 77–81.

[33] J.L. Koldner, Retrieving events from a case memory: A parallel implementation, Proceedings, in: Proc. of a Workshop on Case-Based Reasoning (Morgan Kaufman, San Mateo, CA, 1988) 233–249.

[34] J.L. Kolodner and W. Mark, Case-based reasoning, IEEE Expert 7(5) (1992) 5–6.

[35] P. Koton, Reasoning about evidence in causal explanations, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1988) 260–270.

[36] M. Kriegsman and R. Barletta, Building a case-based help desk application, IEEE Expert 8(6) (1993) 18–26.

[37] R.G. Lord and R.J. Foti, Schema theories, information pro-

cessing, and organizational behavior, in: H.P. Sims, Jr. and D.A. Gioia, The Thinking Organization (Josey-Bass Publishers, London, England, 1986).

[38] P. Maes, Agents that reduce work and information overload, Communications of the ACM 37(7) (1994) 30–40.

[39] R.O. Mason and I.I. Mitroff, A program for research on management information systems, Management Science 19(5) (1973) 475–487.

[40] T. Masters, Practical Neural Network Recipes in $C++$ (Academic Publishers, Toronto, Canada, 1993).

[41] A.R. Montazemi and K.M. Gupta, An adaptive agent for case description in diagnostic CBR system, Journal of Computers in Industry, 29(3) (1996) 209–224.

[42] A.R. Montazemi and K.M.Gupta, Case-based reasoning: A methodology for decision support systems, Proc. of the Eleventh Annual Conference of the Association of Management (Atlanta, Georgia, Collective Supplement 11(1), 1993) p. 63.

[43] A.R. Montazemi and L. Chan, An analysis of the structure of expert knowledge, European Journal of Operational Research 45 (1990) 275–292.

[44] A.R. Montazemi, D.W Conrath and C.A Higgins, An exception reporting information system for ill-structured decision problems, IEEE Transactions on Systems Man, and Cybernetics 17(5) (1987) 771–779.

[45] D. Offutt, SIZZLE: A knowledge acquisition tool specialized for the sizing task, in: Sandra Marcus, ed., Automating Knowledge Acquisition for Expert Systems (Kluwer Academic Publishers, Norwell, MA, 1988) 175–200.

[46] E. Ozakarahan, Database Machines and Database Management (Printice Hall, Englewood Cliffs, NJ, 1986).

[47] Panel of CBR Workshop, Case-based reasoning from DARPA machine learning program, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 1–14.

[48] T.P. Liang and B. Konsynski, Modeling by analogy: Use of analogical reasoning in model management systems, Decision Support Systems 9(1) (1993) 113–126.

[49] D. Poetschke, Analogical reasoning for second generation expert systems, in: Proc. of International Workshop on Analogical and Inductive Inference (All '89, Reinhardsbun Castle, Germany, 1989) 264–276.

[50] B.W. Porter, R. Bariess and R.C. Holte, Concept learning in weak theory domains, Artificial Intelligence 45(12) (1990) 229–264.

[51] O. Raoult, A survey of diagnosis expert systems, in: G. Saucier, A. Ambler and M.A. Breuer eds., Knowledge Based Systems for Test and Diagnosis (Elsevier Science, New York, NY, 1989) 153–167.

[52] J.J. Regazzi, Performance measures for information retrieval systems – An experimental approach, Journal of American Society for Information Science 39(4) (1988) 235–251.

[53] C.K. Riesbeck and R.C. Schank, Inside Case-Based Reasoning (Lawrence Erlbaum, Hillside, NJ, 1989).

[54] D.E. Rumelhardt and J.L. McClelland, Parallel Distributed Processing: Explorations in Microstructure of Cognition 1 and 2 (Cambridge, MIT Press, 1986).

[55] G. Salton, The state of retrieval system evaluation, Information Processing and Management 28(4) (1992) 441–449.

[56] L. Shastri, Why semantic networks, in J.F. Sowa, ed., Principles of Semantic Networks (Morgan Kaufaman, San Mateo, CA, 1991) 109–136.

[57] E.H. Shortliffe and B.G. Buchannan, A model of inexact reasoning in medicine, in: B.G. Buchannan and E.H. Shortliffe, eds., Rule-Based Expert Systems (Addison Wesley, Melno Park, CA, 1984) 233–262.

[58] E. Simoudis and J. Miller, Validated retrieval in case-based reasoning, Eighth National Conference on AI (AAAI 1, 1990) 310–315.

[59] E. Simoudis, Using case-based retrieval for customer technical support, IEEE Expert 7(5) (1992) 7–11.

[60] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Printice-Hall, Englewood Cliffs, NJ, 1982).

[61] C. Stanfill and D.L. Waltz, Memory-based reasoning paradigm, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman, San Mateo, CA, 1988) 414–424.

[62] R.J. Sternberg, Component processes in analogical reasoning, Psychological Review 84(4) (1977) 353–378.

[63] R.H. Stottler, CBR for cost and sales prediction, AI Expert 9(8) (1994) 25–33.

[64] R. Sun, A connectionist model for commonsense reasoning incorporating rules and similarities, Knowledge Acquisition 4(3) (1992) 293–32.

[65] K.P. Sycara, Machine learning for intelligent support of conflict resolution, Decision Support System 10(4) (1993) 121–136.

[66] P. Thagard, K.J. Holyoak, G. Nelson and D. Gochfeld, Analog retrieval by constraint satisfaction, Artificial Intelligence 46(3) (1990) 259–310.

[67] P. Thrift, A neural network model for case-based reasoning, in: Proc. of DARPA Workshop on Case Based Reasoning (Morgan Kaufman Publishers, San Mateo, CA, 1989) 334–337.

[68] C. Tsatsoulis and R.L. Kashyap, Case-based reasoning in manufacturing with TOLTEC planner, IEEE Transactions on Systems, Man, and Cybernetics 23(4) (1994) 1010–1023.

[69] A. Tversky, Features of similarity, Psychological Review 84(4) (1977) 327–352.

[70] D. Waltz and J.A. Feldman, Connectionist models and their implications, in: D.Waltz and J.A. Feldman, eds., Connectionist Models and Their Implications: Reading From Cognitive Science (Ablex Publishing, NJ, 1988).

![](/api/attachments/H6ZMNYC5/fulltext/images/e985c44c0145552a074b8076ef7129384598593bb96af061c9d851baaf400d5a.jpg)

Kalyan Moy Gupta is a research engineer at Atlantis Aerospace Corporation. He received his Ph.D. degree from McMaster University in 1996. He has a B.E. degree from Ravishanker University in India and a M. Tech. degree from the Indian Institute of Technology at Kharagpur in India. At Atlantis, he designs and develops performance support systems. Prior to joining his Ph.D., he spent several years developing business information systems. He is a member of

ACM, INFORMS, and ToRCHI. His publications appear in IEEE Transactions on Systems, Man, and Cybernetics, Journal of Computers in Industry and Journal of Management Information Systems. He has presented and published in the conferences of the North East Decision Sciences Institute, the Canadian Operations Research Society, and the American Association of Management. His current research interests include use of artificial intelligence techniques in performance support systems, message extraction, and requirements analysis.

![](/api/attachments/H6ZMNYC5/fulltext/images/927fe5f3e8f24dd72a515fd001065d6ba2bff9f2f845fc1b8d773108fd06335a.jpg)

Ali R. Montazemi is Associate Professor of Management Information Systems at the Michael G. DeGroote School of Business, and Associate Member of the Department of Electrical and Computer Engineering, McMaster University. He received his Ph.D. in Management Sciences from the University of Waterloo in 1984. His publications have appeared in Decision Support Systems, European Journal of Operational Research, IEEE Transaction on Systems,

Man and Cybernetics, INFOR, International Journal of Man-Machine Studies, Journal of Artificial Intelligence in Education, Journal of Computers in Industry, Journal of Educational Computing Research, Journal of Management Information Systems, Journal of Operational Research Society, MIS Quarterly, amongst others. His area of current research interests include human-computer interaction, application of case-based reasoning systems in business, design and development of DSS, and intelligent tutoring systems.
