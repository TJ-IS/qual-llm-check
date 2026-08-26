---
otero_id: 22605
otero_key: "VS2JV8CU"
title: "Fuzzy cognitive map for the design of EDI controls"
authors: "Sangjae Lee; Ingoo Han"
year: "2000"
journal: "Information & Management"
doi: "10.1016/s0378-7206(99)00033-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Fuzzy cognitive map for the design of EDI controls

Sangjae Lee $^{a}$ , Ingoo Han $^{b,*}$

$^{a}$ Techno-Management Research Institute, Korea Advanced Institute of Science and Technology, Seoul 130-012, South Korea $^{b}$ Graduate School of Management, Korea Advanced Institute of Science and Technology 207-43, Cheongryangri-Dong Dongdaemun-Gu, Seoul 130-012, South Korea

Received 4 October 1998; received in revised form 22 March 1999; accepted 10 July 1999

## Abstract

EDI control design is ill-structured and demands consideration of the complex causal relationships among various components of the controls, which may be broadly classified into formal, informal, and automated types. Each of these can, in turn, be categorized as internal or external. However, it is difficult even for EDI experts to predict the causal effects of one control on another. In order to aid the design of EDI controls, the application of a fuzzy cognitive map, EDIFCM (EDI-Control Design using a Fuzzy Cognitive Map), was developed. Structural equation modeling was used to identify relevant relationships among the components and indicate their direction and strength. A standardized causal coefficient from structural equation modeling was then used to create a fuzzy cognitive map, through which the state or movement of one control component was shown to have an influence on the state or movement of others. Thus, EDI auditors were able to enhance their understanding of the causal relationship of controls and effectively design them. © 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic data interchange; Fuzzy cognitive map; Controls; Performance; Security

## 1. Introduction

EDI (Electronic Data Interchange) is the electronic, computer-to-computer exchange of information in a standard format between business trading partners or various units within an organization. A document must be initially converted into an agreed-upon format (grammar), then transmitted in such a manner that it is error free. Despite the benefits claimed for EDI, the EDI literature indicates that EDI adopters seem to have mixed success. One of the major problems relates to the security of EDI. While a substantial reduction in operating costs may be achieved, these savings can be wiped out by deliberate or accidental loss of data during communication. The system does not accomplish its intended outcome if the security and integrity of the system control are insufficient. A general absence of hard copy or signature/authorization for transactions and audit trails demands changes and enhancement to the traditional control systems.

EDI controls can be broadly defined as the process through which an organization achieves its goals when implementing EDI. The controls can safeguard IS resources, thereby, accomplishing the system objectives of timeliness and accuracy. Designing EDI controls is seldom simple, as it demands consideration of the complex interrelationships among various components.

The tasks of evaluating and designing EDI controls, as performed by managers and internal auditors, are difficult and unstructured. IS auditors have relied upon their experience and know-how to make decisions on the degree to which a system maintains integrity and security. A traditional technique for evaluating control systems is a checklist. However, it is difficult to assess the interactions among components using only a checklist method. As the relevant environment is likely to be complex and EDI auditors do not fully understand how the rigorous analytical techniques can assist them in determining the interrelationships among various components.

It is difficult for EDI auditors or managers to quantify the strength and direction of the interrelationships among EDI controls and performance. This is likely to be particularly true for decision environments which are not well understood. Further, the expertise of a larger number of experts needs to be combined in order to produce a more reliable EDI control structure. A rigorous method is needed to integrate information from various experts and sources.

This article proposes the use of an FCM (Fuzzy Cognitive Map) approach in designing EDI controls.

## 2. Components of EDI controls

EDI controls ensure that an error or failure in the EDI process does not propagate into other applications of organizations. The EDI system may not reduce cycle time or administrative cost unless it is well designed. If its performance level is unsatisfactory, formal, informal, and automated controls need to be checked and adjusted. These three types of controls can be combined to achieve the organizational goals $[23]$ .

While internal controls deal with such components as the application system and communication interface, external controls are concerned with systems such as proprietary networks connected with trading partners and VANs. Internal controls are established to monitor such systems as accounting or sales connected to the network. Agreements must be reached between trading partners on transmission and message standards, and communication protocols. The parties must continuously manage such needs as mutual training, contingency planning, and transmission security with the electronic trading partners.

Controls can be classified into two important dimensions: formality and automation; thus, there are six potential control types. Internal formal controls are established by management and based on written procedures to:

\- protect applications from errors and unauthorized access, and

\- ensure that communication is accurate and secure.

The parallel external controls involve procedures to be used by:

\- VAN service providers to ensure security of EDI messages and communication processes, and

\- trading partners to ensure security and integrity of communication.

The items for informal controls are adapted from Jaworski et al. [17]. Internal informal controls include those of IS members and users in recognizing the extent of risk, sense of responsibility, experience, and interaction among colleagues. In a similar way, the external informal controls include components for VANs and trading partners with cross-vulnerabilities.

Internal automated controls indicate the degree to which such procedures and methods are used to detect and correct errors during input, process, and output of data and ensure security and authentication software to protect the systems from unauthorized access and computer abuse. External automated controls involve the VANs and trading partners in protecting system integrity.

## 3. The causal relations among EDI controls

Controls need to be evaluated together with others that pertain to the same environment [28]. For instance, the breach of an accounting inventory system by an external intruder may result in the an erroneous order to a supplier or incorrect inventory totals. Each component should be independently tested to see whether it accomplishes its purported goals. But because they are closely interrelated, the violation of one part might immediately demand its isolation and removal [1,14]. Frank et al. [10] suggest that the correlation between formal policies and norms for security-related behaviors are stronger when the user level of knowledge is low; this correlation with knowledge turns out to be higher when formal policies do not exist and when standards are not implemented.

EDI auditors must enforce controls to achieve organizational goals. An access control system using a password is one example illustrating the interaction of the three controls. Procedures for maintaining user passwords and changing procedures are formal; users' recognition of responsibility and faith in the procedures comprise informal controls. Access control software and embedded audit routines are automated controls. As appropriately designed EDI controls can improve performance, successful design requires a detailed understanding of the control structure and its implication on performance.

A clearly defined set of policies regarding the education of system users can be the basis for enhancing user awareness of the effect of violation of rules on the integrity and security of the system. An education program on the ethical aspects of system usage can similarly increase the responsibility of employees. Communication and discussion among employees can be encouraged through formalized team training.

After the installation of automated controls, EDI adopters may recognize the importance of formal procedures for managing the system $[7,16]$ ; e.g., transaction logs must be protected from alteration in order to retain a valid audit trail.

It may be inefficient for EDI managers to implement full controls that require significant resources. The appropriate levels of various controls should be determined according to their interdependency and impact on performance.

## 4. Need for FCM in the design of EDI controls

Audit support systems help auditors with evidence collection and evaluation. Tools, such as generalized audit software packages, have been developed to provide data retrieval, manipulation, and reporting capabilities that are specifically oriented to the needs of auditors. This software allows them to use a high-level problem-oriented language to invoke functions to be performed on data. Auditors can increase their understanding of the system and can be supported while making semistructured and unstructured decisions with such specialized audit software. Expert systems using artificial-intelligence techniques encapssulate the knowledge of good auditors about a specific problem domain and can reproduce their expertise when faced with a similar domain.

A cognitive map (CM), introduced by Axelrod [2], is a representation of the causal relationships among the elements of a given environment. It describes the perceptions of experts about the subjective world rather than objective reality. CMs were originally used to represent knowledge in the political and social sciences. Their concern is to see whether the state of one element seems to influence the state of another.

CMs can be generalized into FCMs by fuzzifying edge values or causality values. FCMs give different strengths to each link and appear more reasonable to represent most cases. In many cases, knowledge about a specific domain is uncertain as well as fuzzy, because most knowledge is expressed as different causal relationships between concepts or variables. The FCM approach is an inference mechanism that allows the fuzzy causal relations among factors to be identified and their impact to be constructed. An FCM is composed of nodes that represent the factors most relevant to the decision environment and arrows that indicate different causal relationships among factors. One factor has a direct positive or negative effect on another. Arrows may have different numerical strengths. Experts describe their understanding of the relationships among the defined key factors in order to build a cognitive map.

FCMs are commonly considered best for problems where experts have diverse opinions about a correct answer. An FCM sets up a series of nodes, each of which represents one of the key elements of the problem. It is often difficult to quantify the impact of one factor on another. The causal relationships can, however, be indicated by weighted directed connections.

If specific nodes are stimulated, the resulting activities can resonate through other nodes on the map until equilibrium is reached. The nodes transmit activities to others in the network along positively or negatively weighted connections. In turn, the activities of each recipient node increase or decrease, and are then transmitted throughout the network. FCMs can yield insights into indirect effects among nodes. Such indirect effects can be understood only after the entire map is displayed.

FCMs are especially useful for knowledge acquisition/processing in soft but highly complicated domains where both system concepts and relationships are fundamentally fuzzy (e.g. [20,21,27]). Montazemi and Conrath [26] used FCMs for information requirement analysis, suggesting a pattern of effective factors for evaluating the performance of subordinates by insurance claim managers. Looney and Alfize [24] suggested binary matrices to describe rule-based knowledge. An M-labeled digraph has been used to represent causation in static and dynamic processes [4]. Binary matrices and matrix multiplications have also been introduced for reasoning in semantic networks [5]. Kim and Pearl [19] used the causal network formalism suggested by Pearl [29] to develop an inference engine for causal and diagnostic reasoning. Further, FCMs have been used to analyze electrical circuits [30], to analyze and extend graph-theoretic behavior [35], and model plant control [12].

The usefulness of FCMs can be highlighted in dynamic feedback systems for which conventional rule-based expert systems are inadequate $[31]$ . Auditors rely on past experience rather than explicit rules when evaluating and designing controls. They use past cases to make recommendations for controls and use few inferential rules. As an AI approach, the fuzzy cognitive map technique can compensate for the lack of rule-based mechanisms in traditional expert systems by providing the higher level of abstraction needed for EDI control design.

Subjective, nondeterministic, and context-sensitive judgments have been used to evaluate and determine the interrelationships among controls. Past experience and professional knowledge of EDI auditors may be used in their design. However, the cognitive and situational limitations of auditors may hinder the effectiveness of their reasoning process. People tend to search for information that supports their own ideas and is consistent with their established beliefs. They have difficulty in simultaneously integrating large quantities of information. Since EDI auditors only deal with a small number of cases, their ability to infer relationships among controls may be limited. The increasing complexity of computerized systems necessitates improved aid for evidence collection and evaluation. The interaction among related controls might even complicate the design and audit process.

## 5. FCM development

The purpose of FCM is to aid in the recommendation of EDI controls that ensure high EDI performance. It is necessary to devise a systematic way to estimate the causal relationships among factors based on a historical case base, as there exist no normative model of EDI controls. Methods of determining causal relationships among factors include using the statements of decision makers $[9]$ , questionnaires prepared specifically for this purpose or neural network-based learning $[6]$ . The first and second approaches are based on the assumption that experts in the domain can accurately provide the weights in causal relationships. Traditional design procedures for IS controls, such as interview and observation, may be insufficient to deal with the control complexities inherent in EDI. However, integration of the individual FCMs created by experts is needed when there exist multiple maps devised by experts from the same domain with varying degrees of credibility. It is difficult to determine the precise strength of the interrelationships among factors at the outset. The edge weights define the degree to which concepts interact. Experts can assign numbers to the entries of adjacency matrices but it is difficult to gauge their strength. In addition, in cases where each map has less accuracy and reliability, the resulting combined map cannot precisely describe, through algorithms, the actual state of the domain environment.

Algorithmic ways of combining various FCMs are incomplete. Existing studies have focused on the combination of knowledge after they are built. A combined FCM is potentially stronger than an individual one, because information comes from multiple sources. However, maps can differ in content and relative strength, making accurate combination difficult. It is even difficult to determine the credibility weight given to each expert accurately when a global FCM is computed from the weighted sum of individual FCMs:

$$
F _ {w} = \sum_ {i = 1} ^ {N E} F _ {i} \cdot W _ {i}
$$

where $F_{w}$ is the combined FCM; $F_{i}$ is the FCM suggested by individual experts; and $W_{i}$ is the credibility weight. Experts have varying experience and credentials, making the determination of credibility weight subjective. There are methods of combining knowledge [22] or estimation of weights, but these demand a comparison of opinions from experts. As the number of experts increases, the comparison of their opinions becomes very complex. Hence it is necessary that the knowledge of experts be accurately represented when the FCM is first constructed.

Using neural network-based learning is inappropriate unless the number of data points to be analyzed or the range of values for each data point is large (much larger than statistical techniques) in order to produce reliable weights of each link. In addition, as knowledge is distributed over the entire network, reading and understanding it is difficult. It has been suggested that neural network systems are limited in their inability to provide explanations of how input attributes are used to produce output predictions $[8,34]$ . This has resulted in the idea that neural networks are black boxes that cannot show what the network has learned $[13]$ . There are some heuristic methods to identify the strength of the relationships between inputs and each output variables $[11,32,33]$ . Further, the learning of weights is highly dependent on various parameters such as network architecture (e.g. backpropagation networks, recurrent networks), degree of training, learning rate, and activation function.

In this study, modeling with Linear Structural Relationships (LISREL) was used to determine the complex causal relationships among factors based on a large number of cases. This approach can validate the significance of causal links. Simultaneous causation among observed variables can also be investigated using LISREL $[3,18]$ .

An FCM was first built to aid the design of EDI controls by representing how the state of one mode of controls affects that of others. The interrelationships among seven components are modeled using structural equations. The latent variables in the paths represent factors; the relationships among them can be determined after LISREL estimates the standardized causal relation. These estimates are then mapped into values ranging from -1 to 1. The overall fit of the model can be assessed by generating fitness indices among them the chi-square statistics.

A path diagram for a structural model is shown in Fig. 1. It communicates the basic ideas of the research model, and represents corresponding algebraic equations of the model. The causal relationships of the three controls are related to performance through theories of organizational controls and innovation. It is suggested that formal controls be established first to affect other controls. Informal and automated controls affect each other. Further, there are collective effects of multiple controls that implies that their combination increases performance.

![](/api/attachments/VS2JV8CU/fulltext/images/de8a4d53cce0cc21eef21be7ade55f0093648b37dd8bdf63d1f9867227a51abd.jpg)  
Fig. 1. Causal relationships between concepts.

Latent variables are enclosed in circles or ellipses, following the notation suggested by Jöreskog and Sorbom. A one-way arrow between two variables indicates a hypothesized direct effect.

Structured interviews were used as the primary method of data collection. One or two EDI managers participated simultaneously; they were assumed to know enough about EDI implementation. Any unanswered questions were passed to colleagues having sufficient knowledge. The data were gathered as part of a larger investigation concerning EDI controls. The survey instrument was first verified by interviewing EDI practitioners from each firm. The wording and interpretation of items, and the extent to which practitioners felt they possessed the necessary knowledge to provide appropriate responses were analyzed until a final draft of the questionnaire required only minor revisions. Altogether 10 interviews with practitioners were conducted, and a final review of the questionnaire was made by four IS professors.

After validation, the questionnaire was distributed to EDI staff members and a manger. A total of 110 usable responses were returned. A multiple 7-point Likert-type scale was used for each variable of the EDI controls and EDI performance. EDI control measures were newly developed through a synthesis of various sources (e.g. [15,25]) etc. The informal control measures were based on several previous studies including Jaworski et al. EDI performance represents the extent of service improvement and competitiveness achieved through EDI. The measures for these variables are shown in the Appendix A. The unit of analysis were individual EDI-adopting companies.

There are two ways in which an organization can alter the design process of EDI controls: adjustment of internal or external formal controls. Formal controls are policy variables, and performance is measured as value variables; other EDI controls nodes are cognitive variables.

Seven fit indices suggest a good fit for the proposed model. $\chi^2$ is 15.7 with 5 degrees of freedom for the unconstrained model. $P$ value is 0.0079. The model's goodness-of-fit index is 0.96; this measures the relative amount of variables and covariances jointly accounted for by the model. The adjusted-goodness-of-fit is 0.80. The root mean square residual is 0.08; this is a measure of the average of the residuals. These measures of overall fit indicate the explanatory power of the model.

Some paths have only indirect effects and thus no direct link exists. Most of the 30 causal paths among the variables are significant, except those easily identified in Table 1 of the appendix; e.g., from internal informal to external informal controls and to internal automated controls, etc.

Table 2 shows the adjacency matrix, E. The size of each causal effect is normalized there to show unit variances. The adjacency matrix can be derived from the standardized causal effect.

All standardized effects range from -1 to 1. The highest and lowest causal effects are found in the path from external formal controls to external automated controls (0.71), and from external automated controls back to itself (-0.73). Only six of the 20 nonzero effects among different modes of controls are negative, moderately supporting the positive influence of one mode of controls on another, and the effectiveness of the balanced use of three control modes. The negative numbers indicate negative effects between EDI controls.

EDI systems in Korea are rapidly expanding; and the size and direction of causal effects may reflect unique country characteristics. The significance of some EDI controls may change as the diffusion of EDI progresses. For instance, as the strategic impact of EDI increases and its future role as an integral part of IS expands, the influence of formal and automated controls becomes greater in improving system performance than informal controls. Reliance on VANs is common in Korea and this may influence the relationship between EDI controls and EDI implementation. The development of EDI in Korea relies heavily on policies initiated by these companies and the degree to which they can agree on such fundamental issues as message standards, communication protocols, and operation procedures. The development of a standardized EDI system has government support. Heavy reliance on a VAN or on influential trading partners may lead to a reactive attitude in EDI adopters; this might explain the relatively insignificant influence of informal controls on EDI implementation.

Table 1
Causal effects among controls and performance

<table><tr><td>Causal path</td><td></td><td>MLEa of causal coefficient</td><td>Standardized coefficient</td><td>t-value</td></tr><tr><td>Internal informal controls → internal informal controls</td><td>Indirect effect</td><td>-0.71</td><td>-0.71</td><td>-8.47***</td></tr><tr><td>External informal controls → external informal controls</td><td>Indirect effect</td><td>-0.63</td><td>-0.63</td><td>-9.39***</td></tr><tr><td>Internal automated controls → internal automated controls</td><td>Indirect effect</td><td>-0.62</td><td>-0.62</td><td>-9.19***</td></tr><tr><td>External automated controls → external automated controls</td><td>Indirect effect</td><td>-0.73</td><td>-0.73</td><td>-12.71***</td></tr><tr><td>Internal informal controls → external informal controls</td><td>Indirect effect</td><td>-0.07</td><td>-0.07</td><td>-1.23</td></tr><tr><td>External informal controls → internal informal controls</td><td>Indirect effect</td><td>0.14</td><td>0.14</td><td>2.18**</td></tr><tr><td>Internal automated controls → external automated controls</td><td>Indirect effect</td><td>0.07</td><td>0.07</td><td>1.44*</td></tr><tr><td>External automated controls → internal automated controls</td><td>Indirect effect</td><td>-0.16</td><td>-0.16</td><td>-2.14**</td></tr><tr><td rowspan="3">Internal formal controls → internal informal controls</td><td>Direct effect ( $\gamma_{11}$ )</td><td>1.61</td><td>1.63</td><td>3.92***</td></tr><tr><td>Indirect effect</td><td>-1.12</td><td>-1.14</td><td>-2.85***</td></tr><tr><td>Total effect</td><td>0.48</td><td>0.49</td><td>8.02***</td></tr><tr><td rowspan="3">Internal formal controls → external informal controls</td><td>Direct effect ( $\gamma_{21}$ )</td><td>0.79</td><td>0.80</td><td>1.65**</td></tr><tr><td>Indirect effect</td><td>-0.31</td><td>-0.32</td><td>-0.67</td></tr><tr><td>Total effect</td><td>0.48</td><td>0.49</td><td>7.79***</td></tr><tr><td rowspan="3">Internal formal controls → internal automated controls</td><td>Direct effect ( $\gamma_{31}$ )</td><td>-0.44</td><td>-0.45</td><td>-2.46***</td></tr><tr><td>Indirect effect</td><td>0.93</td><td>0.95</td><td>5.23***</td></tr><tr><td>Total effect</td><td>0.49</td><td>0.50</td><td>6.80***</td></tr><tr><td rowspan="3">Internal formal controls → external automated controls</td><td>Direct effect ( $\gamma_{41}$ )</td><td>0.39</td><td>0.39</td><td>1.03</td></tr><tr><td>Indirect effect</td><td>0.13</td><td>0.13</td><td>0.34</td></tr><tr><td>Total effect</td><td>0.52</td><td>0.53</td><td>8.54***</td></tr><tr><td rowspan="3">External formal controls → internal informal controls</td><td>Direct effect ( $\gamma_{12}$ )</td><td>2.06</td><td>2.09</td><td>4.38***</td></tr><tr><td>Indirect effect</td><td>-1.47</td><td>-1.49</td><td>-3.20***</td></tr><tr><td>Total effect</td><td>0.59</td><td>0.60</td><td>8.97***</td></tr><tr><td rowspan="3">External formal controls → external informal controls</td><td>Direct effect ( $\gamma_{22}$ )</td><td>0.84</td><td>0.85</td><td>1.36*</td></tr><tr><td>Indirect effect</td><td>-0.26</td><td>-0.26</td><td>-0.42</td></tr><tr><td>Total effect</td><td>0.58</td><td>0.59</td><td>8.86***</td></tr><tr><td rowspan="3">External formal controls → internal automated controls</td><td>Direct effect ( $\gamma_{32}$ )</td><td>-0.62</td><td>-0.63</td><td>-3.02***</td></tr><tr><td>Indirect effect</td><td>1.14</td><td>1.16</td><td>5.50***</td></tr><tr><td>Total effect</td><td>0.52</td><td>0.53</td><td>6.97***</td></tr><tr><td rowspan="3">External formal controls → external automated controls</td><td>Direct effect ( $\gamma_{42}$ )</td><td>0.54</td><td>0.55</td><td>1.13</td></tr><tr><td>Indirect effect</td><td>0.16</td><td>0.16</td><td>0.33</td></tr><tr><td>Total effect</td><td>0.69</td><td>0.71</td><td>11.35***</td></tr><tr><td rowspan="3">Internal informal controls → internal automated controls</td><td>Direct effect ( $\beta_{31}$ )</td><td>0.95</td><td>0.96</td><td>2.07**</td></tr><tr><td>Indirect effect</td><td>-0.75</td><td>-0.75</td><td>-2.54***</td></tr><tr><td>Total effect</td><td>0.20</td><td>0.21</td><td>0.92</td></tr><tr><td rowspan="3">Internal informal controls → external automated controls</td><td>Direct effect ( $\beta_{41}$ )</td><td>1.02</td><td>1.02</td><td>2.80***</td></tr><tr><td>Indirect effect</td><td>-0.67</td><td>-0.68</td><td>-2.03**</td></tr><tr><td>Total effect</td><td>0.34</td><td>0.35</td><td>4.94***</td></tr><tr><td rowspan="3">External informal controls → internal automated controls</td><td>Direct effect ( $\beta_{32}$ )</td><td>0.98</td><td>0.98</td><td>2.94***</td></tr><tr><td>Indirect effect</td><td>-0.49</td><td>-0.49</td><td>-1.87**</td></tr><tr><td>Total effect</td><td>0.50</td><td>0.50</td><td>4.97***</td></tr><tr><td rowspan="3">External informal controls → external automated controls</td><td>Direct effect ( $\beta_{42}$ )</td><td>-0.76</td><td>-0.76</td><td>-1.64*</td></tr><tr><td>Indirect effect</td><td>0.62</td><td>0.63</td><td>1.93**</td></tr><tr><td>Total effect</td><td>-0.14</td><td>-0.14</td><td>-0.81</td></tr><tr><td rowspan="3">Internal automated controls → internal informal controls</td><td>Direct effect ( $\beta_{13}$ )</td><td>-0.25</td><td>-0.25</td><td>-0.40</td></tr><tr><td>Indirect effect</td><td>0.02</td><td>0.02</td><td>0.03</td></tr><tr><td>Total effect</td><td>-0.23</td><td>-0.23</td><td>-1.32*</td></tr><tr><td rowspan="3">Internal automated controls → external informal controls</td><td>Direct effect ( $\beta_{23}$ )</td><td>-1.14</td><td>-1.14</td><td>-6.05***</td></tr><tr><td>Indirect effect</td><td>0.74</td><td>0.74</td><td>4.67***</td></tr><tr><td>Total effect</td><td>-0.40</td><td>-0.40</td><td>-3.25***</td></tr><tr><td rowspan="3">External automated controls → internal informal controls</td><td>Direct effect ( $\beta_{14}$ )</td><td>-1.94</td><td>-1.93</td><td>-3.10***</td></tr><tr><td>Indirect effect</td><td>1.45</td><td>1.44</td><td>2.74***</td></tr><tr><td>Total effect</td><td>-0.49</td><td>-0.48</td><td>-3.40***</td></tr><tr><td rowspan="3">External automated controls → external informal controls</td><td>Direct effect ( $\beta_{24}$ )</td><td>0.48</td><td>0.48</td><td>0.60</td></tr><tr><td>Indirect effect</td><td>-0.17</td><td>-0.17</td><td>-0.27</td></tr><tr><td>Total effect</td><td>0.31</td><td>0.31</td><td>1.63*</td></tr><tr><td rowspan="3">Internal formal controls → performance</td><td>Direct effect ( $\gamma_{51}$ )</td><td>0.31</td><td>0.27</td><td>0.64</td></tr><tr><td>Indirect effect</td><td>0.08</td><td>0.07</td><td>0.20</td></tr><tr><td>Total effect</td><td>0.40</td><td>0.34</td><td>4.08***</td></tr><tr><td rowspan="3">External formal controls → performance</td><td>Direct effect ( $\gamma_{52}$ )</td><td>0.29</td><td>0.25</td><td>0.50</td></tr><tr><td>Indirect effect</td><td>0.11</td><td>0.10</td><td>0.21</td></tr><tr><td>Total effect</td><td>0.41</td><td>0.35</td><td>4.17***</td></tr><tr><td rowspan="3">Internal informal controls → performance</td><td>Direct effect ( $\beta_{51}$ )</td><td>0.11</td><td>0.09</td><td>0.43</td></tr><tr><td>Indirect effect</td><td>-0.04</td><td>-0.03</td><td>0.26</td></tr><tr><td>Total effect</td><td>0.07</td><td>0.06</td><td>0.33</td></tr><tr><td rowspan="3">External informal controls → performance</td><td>Direct effect ( $\beta_{52}$ )</td><td>-0.03</td><td>-0.02</td><td>-0.13</td></tr><tr><td>Indirect effect</td><td>-0.01</td><td>0.00</td><td>-0.03</td></tr><tr><td>Total effect</td><td>-0.03</td><td>-0.03</td><td>-0.26</td></tr><tr><td rowspan="3">Internal automated controls → performance</td><td>Direct effect ( $\beta_{53}$ )</td><td>-0.04</td><td>-0.04</td><td>-0.23</td></tr><tr><td>Indirect effect</td><td>0.02</td><td>0.02</td><td>0.12</td></tr><tr><td>Total effect</td><td>-0.02</td><td>-0.02</td><td>-0.17</td></tr><tr><td rowspan="3">External automated controls → performance</td><td>Direct effect( $\beta_{54}$ )</td><td>0.13</td><td>0.11</td><td>0.31</td></tr><tr><td>Indirect effect</td><td>-0.15</td><td>-0.13</td><td>0.41</td></tr><tr><td>Total effect</td><td>-0.02</td><td>-0.02</td><td>-0.16</td></tr></table>

$^{a}$ (MLE: Maximum Likelihood Estimate) $*p<0.1$ , $**p<0.05$ , $***p<0.01$ .

Table 2  
The adjacency matrix representing fuzzy cognitive map

<table><tr><td>Effect cause</td><td>Internal formal controls</td><td>External formal controls</td><td>Internal informal controls</td><td>External informal controls</td><td>Internal automated controls</td><td>External automated controls</td><td>Performance</td></tr><tr><td>Internal formal controls</td><td>0</td><td>0</td><td>0.49</td><td>0.49</td><td>0.50</td><td>0.53</td><td>0.34</td></tr><tr><td>External formal controls</td><td>0</td><td>0</td><td>0.60</td><td>0.59</td><td>0.53</td><td>0.71</td><td>0.35</td></tr><tr><td>Internal informal controls</td><td>0</td><td>0</td><td>-0.71</td><td>-0.07</td><td>0.21</td><td>0.35</td><td>0.06</td></tr><tr><td>External informal controls</td><td>0</td><td>0</td><td>0.14</td><td>-0.63</td><td>0.50</td><td>-0.14</td><td>-0.03</td></tr><tr><td>Internal automated controls</td><td>0</td><td>0</td><td>-0.23</td><td>-0.40</td><td>-0.62</td><td>0.07</td><td>-0.02</td></tr><tr><td>External automated controls</td><td>0</td><td>0</td><td>-0.48</td><td>0.31</td><td>-0.16</td><td>-0.73</td><td>-0.02</td></tr><tr><td>Performance</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## 6. Example of FCM application

The direction and strength of cause and effect linkages were identified using a number of cases representing the state of controls. However, this result does not show that the FCM is of value. It is necessary to assess the impact of positive and negative causalities when stimuli are exerted on one or more elements. The objective of the application is to illustrate the recommendation of EDI controls that result in the highest EDI performance. The adjacency matrix shows that the enhancement of some control modes causes an effect on other controls and performance.

‘What-if’ questions are answered by entering an input vector that, multiplied by the adjacency matrix produces an ordered list of consequences and diagnoses. The value of each element of the input vector can be 1 or 0. A number of hypothetical situations can be provided regarding the state of formal, informal, and automated controls. There are seven combinations of input, depending on whether each state of three controls is activated Table 3.

The state of input and output values for FCM the case that has the highest performance in the stage n1: internal formal controls, n2: external formal controls, n3: internal informal controls, n4: external informal controls, n5: internal automated controls, n6: external automated controls, n7: performance

<table><tr><td></td><td>Case</td><td>Squared difference from previous stages</td><td>n1</td><td>n2</td><td>n3</td><td>n4</td><td>n5</td><td>n6</td><td>n7</td></tr><tr><td rowspan="7">Stage 0 (Input case)</td><td>Case 1</td><td>-</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Case 2</td><td>-</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Case 3</td><td>-</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Case 4</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Case $5</td><td>-</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Case 6</td><td>-</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Case 7</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td rowspan="7">Stage1</td><td>Case 1</td><td>7.41</td><td>0</td><td>0</td><td>1.09</td><td>1.08</td><td>1.02</td><td>1.23</td><td>0.70</td></tr><tr><td>Case 2</td><td>5.91</td><td>0</td><td>0</td><td>-0.57</td><td>-0.70</td><td>0.70</td><td>0.21</td><td>0.03</td></tr><tr><td>Case 3</td><td>6.42</td><td>0</td><td>0</td><td>-0.71</td><td>-0.09</td><td>-0.77</td><td>-0.66</td><td>-0.03</td></tr><tr><td>Case 4*</td><td>8.21</td><td>0</td><td>0</td><td>0.52</td><td>0.38</td><td>1.73</td><td>1.44</td><td>0.73</td></tr><tr><td>Case $5</td><td>11.71</td><td>0</td><td>0</td><td>-1.29</td><td>-0.80</td><td>-0.07</td><td>-0.45</td><td>0.00</td></tr><tr><td>Case 6</td><td>4.30</td><td>0</td><td>0</td><td>0.38</td><td>0.98</td><td>0.25</td><td>0.57</td><td>0.67</td></tr><tr><td>Case 7</td><td>4.48</td><td>0</td><td>0</td><td>-0.20</td><td>0.28</td><td>0.95</td><td>0.78</td><td>0.69</td></tr><tr><td rowspan="7">Stage 2</td><td>Case 1*</td><td>15.01</td><td>0</td><td>0</td><td>-1.46</td><td>-0.79</td><td>-0.07</td><td>-0.60</td><td>0.00</td></tr><tr><td>Case 2</td><td>4.17</td><td>0</td><td>0</td><td>0.05</td><td>0.27</td><td>-0.93</td><td>-0.20</td><td>-0.03</td></tr><tr><td>Case 3</td><td>5.08</td><td>0</td><td>0</td><td>0.99</td><td>0.22</td><td>0.39</td><td>0.19</td><td>-0.02</td></tr><tr><td>Case 4</td><td>17.56</td><td>0</td><td>0</td><td>-1.41</td><td>-0.52</td><td>-1.00</td><td>-0.80</td><td>-0.03</td></tr><tr><td>Case $5</td><td>7.47</td><td>0</td><td>0</td><td>1.04</td><td>0.48</td><td>-0.54</td><td>-0.01</td><td>-0.04</td></tr><tr><td>Case 6</td><td>4.57</td><td>0</td><td>0</td><td>-0.47</td><td>-0.57</td><td>0.32</td><td>-0.41</td><td>-0.02</td></tr><tr><td>Case 7</td><td>5.33</td><td>0</td><td>0</td><td>-0.42</td><td>-0.31</td><td>-0.61</td><td>-0.61</td><td>-0.05</td></tr><tr><td rowspan="7">Stage 3</td><td>Case 1</td><td>9.41</td><td>0</td><td>0</td><td>1.24</td><td>0.44</td><td>-0.55</td><td>0.04</td><td>-0.05</td></tr><tr><td>Case 2</td><td>2.99</td><td>0</td><td>0</td><td>0.32</td><td>0.14</td><td>0.75</td><td>0.06</td><td>0.01</td></tr><tr><td>Case 3</td><td>3.83</td><td>0</td><td>0</td><td>-0.86</td><td>-0.30</td><td>0.04</td><td>0.20</td><td>0.04</td></tr><tr><td>Case 4</td><td>12.23</td><td>0</td><td>0</td><td>1.55</td><td>0.58</td><td>0.20</td><td>0.10</td><td>-0.04</td></tr><tr><td>Case $5*</td><td>4.80</td><td>0</td><td>0</td><td>-0.55</td><td>-0.16</td><td>0.79</td><td>0.26</td><td>0.06</td></tr><tr><td>Case 6</td><td>2.32</td><td>0</td><td>0</td><td>0.37</td><td>0.14</td><td>-0.51</td><td>0.24</td><td>-0.01</td></tr><tr><td>Case 7</td><td>3.12</td><td>0</td><td>0</td><td>0.69</td><td>0.28</td><td>0.24</td><td>0.30</td><td>0.00</td></tr><tr><td rowspan="7">Stage 4</td><td>Case 1</td><td>6.06</td><td>0</td><td>0</td><td>-0.71</td><td>-0.13</td><td>0.81</td><td>0.30</td><td>0.07</td></tr><tr><td>Case 2</td><td>2.00</td><td>0</td><td>0</td><td>-0.41</td><td>-0.39</td><td>-0.34</td><td>0.10</td><td>0.00</td></tr><tr><td>Case 3</td><td>2.67</td><td>0</td><td>0</td><td>0.47</td><td>0.30</td><td>-0.38</td><td>-0.40</td><td>-0.05</td></tr><tr><td>Case 4*</td><td>8.53</td><td>0</td><td>0</td><td>-1.12</td><td>-0.52</td><td>0.47</td><td>0.40</td><td>0.07</td></tr><tr><td>Case $5</td><td>2.99</td><td>0</td><td>0</td><td>0.06</td><td>-0.10</td><td>-0.72</td><td>-0.30</td><td>-0.04</td></tr><tr><td>Case 6</td><td>1.38</td><td>0</td><td>0</td><td>-0.24</td><td>0.17</td><td>0.43</td><td>-0.10</td><td>0.02</td></tr><tr><td>Case 7</td><td>2.17</td><td>0</td><td>0</td><td>-0.65</td><td>-0.23</td><td>0.09</td><td>0.00</td><td>0.02</td></tr><tr><td rowspan="7">Stage5</td><td>Case 1</td><td>3.70</td><td>0</td><td>0</td><td>0.16</td><td>-0.10</td><td>-0.76</td><td>-0.39</td><td>-0.06</td></tr><tr><td>Case 2</td><td>1.30</td><td>0</td><td>0</td><td>0.27</td><td>0.44</td><td>-0.09</td><td>-0.18</td><td>-0.01</td></tr><tr><td>Case 3*</td><td>1.94</td><td>0</td><td>0</td><td>-0.01</td><td>-0.19</td><td>0.54</td><td>0.38</td><td>0.03</td></tr><tr><td>Case 4</td><td>5.82</td><td>0</td><td>0</td><td>0.43</td><td>0.34</td><td>-0.84</td><td>-0.57</td><td>-0.06</td></tr><tr><td>Case $5</td><td>1.82</td><td>0</td><td>0</td><td>0.26</td><td>0.25</td><td>0.46</td><td>0.20</td><td>0.02</td></tr><tr><td>Case 6</td><td>0.78</td><td>0</td><td>0</td><td>0.15</td><td>-0.29</td><td>-0.21</td><td>0.00</td><td>-0.02</td></tr><tr><td>Case 7</td><td>1.47</td><td>0</td><td>0</td><td>0.42</td><td>0.15</td><td>-0.30</td><td>-0.19</td><td>-0.03</td></tr><tr><td rowspan="7">Stage 6</td><td>Case 1</td><td>2.21</td><td>0</td><td>0</td><td>0.23</td><td>0.24</td><td>0.51</td><td>0.30</td><td>0.03</td></tr><tr><td>Case 2</td><td>0.98</td><td>0</td><td>0</td><td>-0.02</td><td>-0.32</td><td>0.36</td><td>0.16</td><td>0.01</td></tr><tr><td>Case 3</td><td>1.58</td><td>0</td><td>0</td><td>-0.33</td><td>0.02</td><td>-0.49</td><td>-0.22</td><td>-0.01</td></tr><tr><td>Case 4*</td><td>4.22</td><td>0</td><td>0</td><td>0.21</td><td>-0.08</td><td>0.87</td><td>0.46</td><td>0.04</td></tr><tr><td>Case $5</td><td>1.10</td><td>0</td><td>0</td><td>-0.35</td><td>-0.30</td><td>-0.14</td><td>-0.06</td><td>0.00</td></tr><tr><td>Case 6</td><td>0.42</td><td>0</td><td>0</td><td>-0.09</td><td>0.26</td><td>0.02</td><td>0.08</td><td>0.02</td></tr><tr><td>Case 7</td><td>0.97</td><td>0</td><td>0</td><td>-0.12</td><td>-0.06</td><td>0.38</td><td>0.24</td><td>0.03</td></tr><tr><td rowspan="7">Stage7</td><td>Case 1</td><td>1.35</td><td>0</td><td>0</td><td>-0.40</td><td>-0.28</td><td>-0.20</td><td>-0.13</td><td>-0.01</td></tr><tr><td>Case 2*</td><td>0.84</td><td>0</td><td>0</td><td>-0.19</td><td>0.11</td><td>-0.41</td><td>-0.06</td><td>0.00</td></tr><tr><td>Case 3</td><td>1.28</td><td>0</td><td>0</td><td>0.46</td><td>0.14</td><td>0.28</td><td>0.01</td><td>-0.01</td></tr><tr><td>Case 4</td><td>3.23</td><td>0</td><td>0</td><td>-0.58</td><td>-0.17</td><td>-0.61</td><td>-0.19</td><td>-0.01</td></tr><tr><td>Case $5</td><td>0.69</td><td>0</td><td>0</td><td>0.27</td><td>0.25</td><td>-0.13</td><td>-0.05</td><td>-0.01</td></tr><tr><td>Case 6</td><td>0.23</td><td>0</td><td>0</td><td>0.06</td><td>-0.14</td><td>0.08</td><td>-0.12</td><td>-0.01</td></tr><tr><td>Case 7</td><td>0.67</td><td>0</td><td>0</td><td>-0.13</td><td>-0.03</td><td>-0.32</td><td>-0.18</td><td>-0.01</td></tr></table>

As an example, the effect of enhancing the strength of formal controls on all the other controls can be tested by setting the first and second concept node (node for internal and external formal controls) in an input vector to 1:

$C_1$ (1 1 0 0 0 0 0)

This results in the output:

$C_{1} \times E$ (0 0 1.09 1.08 1.02 1.23 0.70) $C_{2}$ where the level of performance is 0.7, showing that enhancing some EDI controls improves EDI performance. However, it is necessary to find the input vector that leads to highest performance by iteration.

The states of controls suggested are not stable. The set of output vectors may indicate a repeating pattern, whose cycle may vary. However, the size of the difference between one stage and the previous one becomes smaller as the number of multiplication increases. The square difference between the two stages is defined as:

$$
D _ {i} = \sum_ {i = 1} ^ {7} \left(C _ {i, j} - C _ {i - 1, j}\right) ^ {2}
$$

where $C_{ij}$ is the state of jth controls in stage i. The squared differences for each state of seven controls are shown in Table 3. They become smaller after stage 2 for all the controls, which shows the convergence of the absolute relative state of controls.

The evolution of the state of controls can be seen as a natural sequence of time, and indicates the possibility of future performance change. EDI auditors can search for the most desirable state of controls leading to the highest performance. For example, cases resulting in the highest performance are: 4, 1, 5, 4, 3, 4, and 2. Cases 1, 5, 3 and 3 must be focused in stages 2, 3, 5, and 7. Input Case 4 is superior to the other cases, as it leads to the highest performance in three of seven stages while the other cases result in the highest performance only once. This suggests that Korean EDI auditors should strengthen formal and informal controls in order to make the system more successful.

## 7. Conclusions

FCMs are fuzzy-graph structures for representing causal reasoning. Their fuzziness can allow the representation of hazy degrees of causality between various control components. Their graph structure enables systematic causal propagation, in particular forward and backward chaining. FCM was developed to support EDI auditors in discovering the most effective controls. The causal reasoning process of EDI practitioners is inevitably subject to human cognitive limitations and bias. Furthermore, their memories are variable and finite. They cannot be completely consistent in searching for relevant experiences, interpreting them, and applying them to problem solving. high priority controls can be determined through fuzzy cognitive mapping. EDI auditors can obtain an idea of the desirable state of controls by reviewing controls that lead to high performance.

The causal relations among variables and the relative explanatory power of such relationships are derived from a statistical approach rather than by integrating different FCMs. The structural equation modeling approach is used to derive causal relationships among controls. It is difficult for EDI staff members to predict causal relations among a number of control components. However, it is much easier for them to estimate the state of each part of a control. This approach will enhance the quality of decision making in the investment of IS resources and establishing controls.

In this paper, we have provided an example that illustrates the causal reasoning process of control design. The set of controls having high values across the entire network may be suggested as the most desirable control set. The performance resulting from implementation of controls can also be suggested. EDI auditors can thus recognize the value of one control component as it relates to the values of others, allowing control designers to identify each pertinent control component, as well as to develop a more accurate model of EDI controls. EDI auditors can support their decision as to the initial state of controls for the highest future state of performance.

## Appendix A. Questionnaire

## A.1. EDI Controls

Respondents answer the extent to which they agree or disagree with each statement about controls. The seven-point Likert type scales are used. Select the representative Value Added Network (VAN) Service your company uses the most. If your company does not use VAN, skip the questions about VAN.

## A.1.1. Internal formal controls

1. Systems are changed only through authorization from the responsible managers.

2. Integrity check of messages is strictly performed before the messages are processed in the application.

3. Audit trails of transactions are always maintained for correction of errors and contingency planning.

4. System login is appropriately controlled by access control procedures such as passwords.

5. EDI messages are checked for duplication, omission or inaccuracy after they are generated and before transmitting the messages.

6. The sender, receiver, and contents of EDI messages are appropriately authenticated after the messages are generated or received.

## A.1.2. External formal controls

1. VAN service providers have an appropriate contingency plan for network failures.

2. The representative trading partner has an appropriate contingency plan for network failures.

3. VAN service providers retransmit messages if the messages are omitted, duplicated, or inaccurate.

4. The representative trading partner retransmits messages if they are omitted, duplicated, or inaccurate.

5. VAN service provider maintains audit trails for recovery of inaccurate messages.

6. The representative trading partner maintains audit trails for the recovery of inaccurate messages.

7. VAN service provider controls unauthorized access and dial login to network.

8. The representative trading partner controls unauthorized access and dial login to network.

9. VAN service provider controls unauthorized access to mailbox by internal staff.

## A.1.3. Internal informal controls

1. EDI staff clearly recognizes the risks of the possible propagation of errors from one system to another.

2. Users who process EDI messages clearly recognize the risks of possible propagation of errors from one system to another.

3. EDI staff clearly recognizes the importance of their responsibility for the performance of EDI system.

4. Users who process EDI messages clearly recognize the importance of their responsibility for the performance of EDI system.

5. EDI staff can evaluate tasks of colleagues to see whether they are incorrect.

6. Users who process EDI messages can evaluate tasks of colleagues to see whether they are incorrect.

7. EDI staff can cope with errors in EDI messages using their own experience.

8. Users who process EDI messages can cope with errors in EDI messages using their own experience.

9. EDI staff frequently cooperates with colleagues to assist in correcting errors.

10. Users who process EDI messages frequently cooperate with their colleagues to assist in correcting errors.

## A.1.4. External informal controls

1. EDI staff clearly recognizes that errors of the VAN can seriously affect our system.

2. EDI staff clearly recognizes that errors of the system of the representative trading partner can seriously affect our system.

3. EDI staff clearly recognizes that the active participation of the VAN service provider is necessary for successful EDI implementation.

4. EDI staff clearly recognizes that the active participation of the representative trading partner is necessary for successful EDI implementation.

5. EDI staff has extensive experience in successfully processing errors with the cooperation of the VAN service provider.

6. EDI staff has extensive experience in processing errors successfully with the cooperation of the representative trading partner.

7. EDI staff knows which items among contracts with the VAN service provider should be applied in communicating messages strictly.

8. EDI staff knows through experience which items among contracts with the representative trading partner should be strictly applied in communicating messages.

9. EDI staff processes their tasks by actively communicating information to their counterparts in the VAN service provider.

10. EDI staff processes their tasks by actively communicating information to their counterparts in the representative trading partner.

## A.1.5. Internal automated controls

1. Automated integrity check of data fields is performed using embedded software before received messages are processed in internal applications.

2. Access to sensitive files and programs is effectively controlled using access controls software.

3. Embedded software is effectively used to automatically check accuracy of messages received.

4. Automated authentication procedures effectively ascertain the identity of sources or destination before sending and after receiving messages.

## A.1.6. External automated controls

1. The VAN service provider automatically records messages for the correction of errors and retransmission of corrected messages.

2. The representative trading partner automatically records messages for the correction of errors and retransmission of corrected messages.

3. The VAN service provider automatically tracks and reports the status of message communication.

4. The representative trading partner automatically tracks and reports the status of message communication.

5. The VAN service provider attaches message identification codes or digital signatures to effectively authenticate the messages.

6. The representative trading partner attaches message identification codes or digital signatures to effectively authenticate the messages.

7. The VAN service provider supports connections with diverse environment through various protocol conversion services.

8. The VAN service provider supports connections with diverse environments through providing various message standards.

## A.2. EDI performance

Respondents answer the extent to which they agree or disagree with each statement about controls. The seven-point Likert type scales are used. Select the representative trading partner with which your company has the largest volume of transactions.

1. Relations with the representative trading partner are greatly improved through reduced response time after adopting EDI.

2. Our company maintains improved relations with the representative trading partner by reducing delay from errors.

3. Our company improved trust in relations with the representative trading partner by enhancing confidentiality of documents

4. Relations with the representative trading partner are greatly improved by reducing omission and inaccurate transmission.

5. Our company maintains high trust with the representative trading partner by protecting messages from disclosure to unauthorized third party.

6. The efficiency of interdepartmental transaction processing is greatly increased.

7. Accuracy is greatly improved by reduced paperwork.

8. Transaction processing costs are greatly reduce after adopting EDI.

## References

[1] R. Anthony, The Management Control Function, Harvard Business School Press, Boston, MA, 1988.

[2] R. Axelrod, Structure of Decision: the Cognitive Maps of Political Elites, Princeton University, Press, Princeton, NJ, 1976.

[3] H.M. Blalock, Theory Construction: from Verbal to Mathematical Formulations. Prentice-Hall, Englewood Cliffs, NJ, 1969.

[4] J.R. Burns, W.H. Winstead, M-labeled digraphs: an aid to the use of structural and simulation models, Management Science 21(3) (1985), pp. 343–358.

[5] J.R. Burns, W.H. Winstead, D.A. Haworth, Semantic nets as paradigms for both causal and judgmental knowledge representation, IEEE Transactions on Systems, Man, and Cybernetics 19(1) (1989), pp. 58–67.

[6] M. Caudill, Using neural nets: fuzzy cognitive maps, AI Expert, 1990, 49-53.

[7] S. Chan, M. Govindan, J.Y. Picard, E. Leschiutta, EDI for Managers and Auditors, Electronic Data Interchange Council of Canada, Toronto, Ontario, 1991.

[8] P. Deng, Automatic knowledge acquisition and refinement for decision support: A connectionist inductive inference model, Decision Sciences 24(2) (1993), pp. 371–393.

[9] C. Eden, S. Jones, D. Sims, Thinking in Organizations, Macmillian Press, London, England, 1979.

[10] J. Frank, B. Shamir, W. Briggs, Security-related behavior of PC users in organizations, Information Management 21 (1991), pp. 127–135.

[11] L.W. Glorfeld, A methodology for simplification and interpretation of backpropagation-based neural network models, Expert Systems with Applications 10(1) (1996), pp. 37–54.

[12] K. Gotoh, J. Murakami, T. Yamaguchi, Y. Yamanaka, Application of fuzzy cognitive maps to supporting for plant control, SICE Joint Symposium of 15th Systems Symposium and 10th knowledge Engineering Symposium, 1989, pp. 99–104.

[13] J.V. Hansen, J.B. McDonald, J.D. Stice, Artificial intelligence and generalized qualitative-response models: An empirical test on two audit decision-making domains, Decision Sciences 23(3) (1992), pp. 704–723.

[14] A. Hopwood, An empirical study of the role accounting data in performance evaluation. Empirical Research in Accounting: Selected Studies, supplement to Journal of Accounting Research 10 (1972) 156-182.

[15] ISACA. EDI Control Guide, EDI Council of Australia, Information Systems Audit and Control Association, Sydney Chapter, 1990.

[16] R. Jamieson, EDI: An Audit Approach, The EDP Auditors Foundation, Rolling Meadows, IL, 1994.

[17] J.B. Jaworski, V. Stathakopoulos, H.S. Krishnan, Control combinations in marketing: Conceptual framework and empirical evidence, Journal of Marketing 57 (1993), pp. 57–69.

[18] K.G. Joreskog, D. Sorbom, LISREL 7: A Guide to the Program and Applications, 2nd ed., SPSS, 1989.

[19] J.H. Kim, J. Pearl, CONVINCE: A conversational inference consolidation engine, IEEE Transactions on Systems Man and Cybernetics SMC-17(2) (1987) 120-133.

[20] J.H. Klein, D.F. Cooper, Cognitive maps of decision-makers in a complex game, Journal of the Operational Research Society 33 (1982), pp. 63–71.

[21] B. Kosko, Fuzzy cognitive maps, International Journal of Man-Machine Studies 24 (1986), pp. 65–75.

[22] K. Lee, H. Kim, A fuzzy cognitive map-based bi-directional inference mechanism: an application to stock investment analysis, International Journal of Intelligent Systems in Accounting, Finance and Management 6 (1997), pp. 41–57.

[23] S. Lee, I. Han, H. Kym, The impact of EDI controls on EDI implementation, International Journal of Electronic Commerce 2(4) (1998), pp. 71–98.

[24] C.G. Looney, A.A. Alfize, Logical controls via boolean rule matrix transformations, IEEE Transactions on Systems, Man, and Cybernetics SMC 17(6) (1987), pp. 1077–1082.

[25] J.A. Marcella, S. Chan, EDI Security, Control, and Audit, Artech House, Norwood, MA, 1993.

[26] A.R. Montazemi, D.W. Conrath, The use of cognitive mapping for information requirement analysis, MIS Quarterly 10(1) (1986), pp. 45–56.

[27] K.S. Park, S.H. Kim, Fuzzy cognitive maps considering time relationships, International Journal of Human-Computer Studies 42 (1995), pp. 157–168.

[28] D.B. Parker, A guide to selecting and implementing security controls, Information Systems Management, 1994, pp. 75–86.

[29] J. Pearl, propagation and structuring in belief networks, Artificial Intelligence 29 (1986), pp. 241–288.

[30] M.A. Styblinski, B.D. Meyer, Fuzzy cognitive maps, signal flow graphs, and qualitative circuit analysis, Proceedings of the 2nd IEEE International Conference on Neural Networks (ICNN-87), 2, 1988, pp. 549–556.

[31] W.R. Taber, Knowledge processing with fuzzy cognitive maps, Expert Systems with Applications 2(1) (1991), pp. 83–87.

[32] Y. Yoon, R. Brobst, P. Bergstresser, L. Peterson, A desktop neural network for dermatology diagnosis, Journal of Neural Network Computing 1(1) (1989), pp. 43–54.

[33] Y. Yoon, T. Guimaraes, G. Swales, Integrating artificial neural networks with rule-based expert systems, Decision Support Systems 11 (1994), pp. 497–507.

[34] Y. Yoon, L. Peterson, Artificial neural networks: An emerging new technique, Data Base 23(1) (1992), pp. 55–57.

[35] W. Zhang, S. Chen, A logical architecture for cognitive maps, Proceedings of the 2nd IEEE Conference on Neural Networks (ICNN-88), 1, 1988, pp. 231–238.

![](/api/attachments/VS2JV8CU/fulltext/images/feb23e0520877a49577aa68f8303f717450bcb396ef9c8fde7fe6f0d42086c71.jpg)

Sangjae Lee is a researcher at Techno-Management Research Institute in Korea Advanced Institute of Science and Technology. He received Ph.D. in Management Information Systems from the Graduate School of Management, Korea Advanced Institute of Science and Technology. He is a certified information systems auditor (CISA). His research papers are forthcoming or published in Telecommunication Systems, Information

Resources Management Journal, International Journal of Electronic Commerce, International Journal of Intelligent Systems in Accounting, Finance and Management, etc. His research interests include electronic data interchange, information systems control and audit.

![](/api/attachments/VS2JV8CU/fulltext/images/ba6af3fcdddbb8404371cbc250e01133b9c924ec727050b1f01fedd7e66496ab.jpg)

Ingoo Han is an associate professor at the Graduate School of Management, Korea Advanced Institute of Science and Technology. He received Ph.D. from the University of Illinois at Urbana-Champaign. His research interests are information systems audit and security, information system evaluation, and AI applications in accounting and finance. The recent research issues include the audit and control under EC, prediction

of stock price using neural network, and integration of AI techniques. Dr. Han has published in Decision Support Systems, International Journal of Electronic Commerce, Contemporary Accounting Research, International Journal of Intelligent Systems in Accounting Finance & Management, Expert Systems with Applications, Engineering Economists, etc.
