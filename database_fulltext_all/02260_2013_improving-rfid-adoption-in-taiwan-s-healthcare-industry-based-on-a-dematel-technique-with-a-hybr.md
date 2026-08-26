---
otero_id: 2260
otero_key: "K88HMUKQ"
title: "Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model"
authors: "Ming-Tsang Lu; Shi-Woei Lin; Gwo-Hshiung Tzeng"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.06.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model

Ming-Tsang Lu <sup>a</sup>, Shi-Woei Lin <sup>b</sup>, Gwo-Hshiung Tzeng <sup>c,d,</sup>⁎

<sup>a</sup> Graduate Institute of Management Science, National Chiao-Tung University, 1001, Ta-Hsueh Road, Hsin-Chu 300, Taiwan

<sup>b</sup> Department of Industrial Management, National Taiwan University of Science and Technology, 43, Keelung Road, Section 4, Taipei 106, Taiwan

<sup>c</sup> Graduate Institute of Urban Planning, National Taipei University, 151, University Road, San Shia 237, Taiwan

<sup>d</sup> Institute of Project Management, Department of Business and Entrepreneurial Management, Kainan University, Taoyuan 338, Taiwan

## a r t i c l e i n f o

Article history: Received 16 June 2011 Received in revised form 11 June 2013 Accepted 11 June 2013 Available online xxxx

Keywords: Healthcare industry Radio frequency identi<sup>fi</sup>cation (RFID) Decision making trial and evaluation laboratory (DEMATEL) DANP (DEMATEL-based ANP) Multiple criteria decision making (MCDM) VIKOR

## a b s t r a c t

The use of radio frequency identi<sup>fi</sup>cation (RFID) technology has progressed tremendously in recent years. In the healthcare industry, the decision to adopt RFID technology is a problem requiring a multi-criteria decision analysis that involves both qualitative and quantitative factors. The evaluation of this decision may be based on imprecise information or uncertain data. Furthermore, there can be signi<sup>fi</sup>cant dependence and feedbacks between the different criteria and alternatives. However, most conventional decision models cannot capture these complex interrelationships. As a result, in this study we develop a general evaluation framework for industry evaluation, improvement and adoption of RFID. We use a hybrid Multiple Criteria Decision Making (MCDM) method known as DDANPV that combines DEMATEL (decision making trial and evaluation laboratory), DANP (DEMATEL-based ANP), and VIKOR to evaluate the factors that in<sup>fl</sup>uence the adoption of RFID. Speci<sup>fi</sup>cally, we study the adoption of RFID in Taiwan's healthcare industry. We <sup>fi</sup>nd that technology integration is the most in<sup>fl</sup>uential criterion and the strongest driver in the adoption of RFID of Taiwan's healthcare industry.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Radio frequency identi<sup>fi</sup>cation (RFID) is a communication technology that uses radio waves to exchange data. RFID has three components: (1) an antenna for transmitting and receiving signals; (2) a transponder programmed with the identi<sup>fi</sup>cation information; and (3) an RF module (reader) with a decoder or transceiver. RFID has many applications and is an increasingly valuable tool for enabling automatic identi<sup>fi</sup>cation and management. For many industries, RFID is not only a new alternative to existing tracking methods but is also a solution for a range of previously cost-prohibitive innovations in internal control and supply chain coordination [34,46].

RFID has existed for decades. This technology was originally used to identify and track <sup>fl</sup>ying aircrafts during the Second World War. Until recently, RFID was deemed to be too expensive and limited in functionality for many commercial applications. As the prices of RFID equipment and RFID tags have dropped in recent years, RFID applications have become increasingly prevalent. Cost is no longer a barrier. However, RFID has not been extensively adopted by the healthcare industry. The relatively conservative attitudes of healthcare providers have prevented hospitals from using the latest information technologies. Furthermore, technology adoption often depends on a critical mass being reached; a manager's decision to adopt a new technology often depends on the technology's diffusion rate, which, in turn, depends on the decisions made by other managers. Furthermore, even if a hospital decides to evaluate the relative costs and bene<sup>fi</sup>ts of implementing RFID technology, no comprehensive evaluation and adoption model exists that can be used as a reference for the adoption of RFID in the healthcare industry. Thus, it is inappropriate to focus only on the cost of a new IT technology as the primary factor in its adoption [4,7,9,50].

Most of the conventional multi-criteria decision analysis (MCDA) models cannot handle the analysis of complex relationships among different hierarchical levels of criteria. However, the decision to adopt RFID requires a decision model that performs just that analysis. In this paper, we develop a hybrid MCDM model called DDANPV that combines DEMATEL, DANP, and VIKOR. DDANPV overcomes the limitations of existing decision models and can be used to help us analyze the factors that in<sup>fl</sup>uence industry adoption of RFID technology. In particular, we use Taiwan's healthcare industry as an example to study the interdependence of the factors that in<sup>fl</sup>uence the adoption of RFID in the healthcare industry, as well as to evaluate alternative RFID adoption processes to achieve the desired levels of performance from RFID technology.

This paper is organized into <sup>fi</sup>ve sections. Section 2 reviews the literature on the implementation of RFID in the healthcare industry.

We will discuss the advances in evaluating the RFID adoption process, the selection criteria for adopting RFID technology, the decision models currently being used to determine whether RFID technology should be adopted, and the speci<sup>fi</sup>c problems related to evaluating the RFID adoption process. Section 3 introduces the hybrid MCDM method called DDANPV. In Section 4, we use Taiwan's healthcare industry as an empirical example to illustrate how DDANPV could help select the best RFID adoption method and discuss the results. In Section 5, we draw conclusions.

## 2. The effects of evaluating the RFID adoption model in the healthcare industry

The purpose of this section is to survey the relevant studies in the RFID adoption process, to investigate and compare various evaluation frameworks, and to identify possible factors that in<sup>fl</sup>uence the RFID adoption process in the healthcare industry. Due to the lack of previous research on the criteria used in evaluating RFID for adoption, this study expands upon a general evaluation framework used in other industries and compiles four primary factors—technology, organization, environment and cost—with the goal of identifying the criteria that are most crucial for the adoption of RFID.

2.1. Related literature on the factors influencing RFID adoption in the healthcare industry

RFID is one of the most promising technologies with the potential to increase supply chain visibility and improve process ef<sup>fi</sup>ciency [45]. Once goods have RFID tags attached, their whereabouts can be tracked automatically by radio readers. With applications in transportation payments, asset management, retail sales, and item tracking, RFID technology provides greater inventory visibility, improves business and control processes, and enhances supply management ef<sup>fi</sup>ciency [26,47]. Hence, many industries are in various stages of applying RFID to experimental projects to improve operational ef<sup>fi</sup>ciency and gain competitive advantages [5]. RFID has also been receiving considerable attention in the healthcare industry because it addresses the vexing problem of locating people and things in healthcare operations, as demonstrated in the case study examined in this project. RFID applications can be classi<sup>fi</sup>ed into two or more major categories based on different objectives in the healthcare industry. However, we only use two alternatives (“patient tracking management performance $\left( \mathsf { A } _ { 1 } \right) ^ { \mathfrak { n } }$ and “asset tracking management performance $\left( { { \sf A } _ { 2 } } \right) ^ { " } )$ from our project as examples to clearly illustrate two relatively good uses for RFID applications. The <sup>fi</sup>rst set of applications is mainly designed for managing the patient-tracking system. For example, RFID is used in patient-tracking to automate the check-in process and other outbound logistical processes (i.e., activities that outsource the service to the customer in a service environment). In a healthcare setting, outbound logistics involve getting the right patient to the right place at the right time [21]. The second set of applications is also used for tracking purposes, but these applications are used to control assets. RFID offers active tags for tracking various healthcare assets, such as wheelchairs, infusion pumps and crash carts. In the healthcare environment, assets (e.g., equipment and staff) are essential to providing healthcare services to patients [21].

Schmitt et al. [38] reviewed related work and derived 25 adoption factors from the technological, organizational, and environmental dimensions of the RFID process. These researchers extracted the <sup>fi</sup>ve most important factors affecting the process of RFID adoption and diffusion in the automotive industry. These factors included compatibility, costs, complexity, performance, and top management support, as well as most of the more technological characteristics. Schmitt et al. [38] concluded that the RFID adoption and diffusion processes were still in the early stages and that the basic technological issues had to be solved <sup>fi</sup>rst. However, the organizational and environmental factors were found to be less important. Similarly, the inter-organizational factors did not play essential roles because most of the RFID deployments in the automotive industry were intraorganizational applications.

Brown and Russell [6] conducted an exploratory investigation to identify the factors that may in<sup>fl</sup>uence RFID adoption in South African retail organizations. A combination of quantitative and qualitative data based on six retailers were collected and analyzed using the Technology, Organization, and Environment (TOE) framework. Brown and Russell [6] expounded upon the intention to adopt RFID technology using technological factors $( \mathrm { i . e . } ,$ , relative advantage, compatibility, complexity, and cost), organizational factors (i.e., top management attitude, information technology expertise, organization size, and organizational readiness), and external factors (i.e., competitive pressure, external support, and the existence of change agents).

In addition to the TOE framework mentioned above, the key barriers to RFID adoption also stem from the high technology expenditures, such as the software and hardware costs, required by RFID [20]. When an organization plans to adopt RFID, both the implementation costs and the maintenance costs need to be evaluated carefully. Lean information technology budgets suggest that new technologies need to demonstrate compelling business reasons for adoption while promising bene<sup>fi</sup>ts and short payback periods. As a result, most companies are still waiting for RFID technology to drop in price to make it a more affordable investment [12,20,36]. In addition to the cost-bene<sup>fi</sup>t analysis mentioned above, many factors contributing to the adoption of RFID are similar to the factors contributing to the recent adoption of e-commerce technology [12].

Previous studies on RFID adoption have not focused on all three TOE dimensions. Many authors have restricted their discussion to only a few key factors. For example, Hoske [13] highlighted the cost factor, while Jones et al. [18] examined private and public policies on RFID. Thus, in this paper, we take the TOE framework $\mathtt { a s \_ a }$ basis and add cost, resulting in technology, organization, environment, and cost (TOEC) as the four dimensions of our research framework. The factors relevant to the adoption of RFID within each dimension will be discussed below.

## 2.2. Criteria for evaluating the RFID adoption process

The criteria for evaluating the RFID adoption process are described below.

Technology dimension $( D _ { 1 } ) \colon$ : Technological factors, also referred to as “innovation characteristics” in several studies on organizational adoption processes [36]. Technology integration, technology competence, and security concerns have all been suggested as important to the adoption of RFID technology and are used in our evaluation framework [37,39].

Organization dimension $( D _ { 2 } ) $ : Characteristics of the organization that is implementing the new technology are shown by Orlikowski [32] to be highly relevant to the adoption process. Several studies have supported this <sup>fi</sup>nding with respect to RFID adoption, with factors such as top management support, <sup>fi</sup>rm size, and organizational readiness considered to be potential in<sup>fl</sup>uences [36,37,39].

Environment dimension $( D _ { 3 } ) \mathrm { : }$ : Orlikowski [32] highlights the role and in<sup>fl</sup>uence of the external environment in an organization's decision to adopt new technology. Competitive pressure, partner support, and regulatory support are regarded as among the most important external factors [36,37,39].

Cost dimension $\left( D _ { 4 } \right)$ : The bene<sup>fi</sup>ts of any new innovation should exceed the costs of adopting it [36]. Therefore, the costs associated with a new technology have a major bearing on the decision of its adoption. In this respect, RFID technology is no exception [39]. Most companies still have doubts about whether the costs associated with RFID can be offset by its promised bene<sup>fi</sup>ts. The cost of RFID tags have been widely mentioned [1,17] in this discussion, as these costs determine the feasible level of tagging: item-level, case-level, or palette-level [13]. In this study, we investigate the related costs of RFID such as hardware, software, implementation, and maintenance.

Our evaluation framework focuses on TOEC as the four dimensions that signi<sup>fi</sup>cantly impact RFID adoption in the healthcare industry. Within each dimension, there are also lower-level criteria based on related factors that were considered in previous studies. Our entire evaluation framework, including both the dimensions and the criteria, is presented in Table 1.

## 3. DDANPV — A hybrid MCDM model for evaluating and improving RFID adoption

DDANPV is comprised of three stages. First, we use the DEMATEL method to uncover the relationship between the criteria and their network structure in the presence of interdependence and feedback among criteria. DEMATEL is more suitable in real-world applications than traditional methods, which assume independence among criteria [8,14,15,23,24,33,43]. Second, we combine DEMATEL with the ANP method to form DANP (DEMATEL-based ANP) to obtain in<sup>fl</sup>uential weights for each dimension and criterion in our evaluation structure. Third, we incorporate these weights into the VIKOR method to rank the performance of the alternatives presented to the decision-maker and identify the gaps that each alternative has to an as yet nonexistent aspired alternative; this approach provides us with a roadmap to how we can improve upon each alternative by reducing the performance gaps of each criterion and dimension relative to their aspired levels through innovation and research in the future. In short, the evaluation framework contains three main stages: (1) use DEMATEL to construct the in<sup>fl</sup>uential network relation map (INRM) among the dimensions and criteria; (2) use DANP to calculate the in<sup>fl</sup>uence weights of each dimension and criterion; and (3) use VIKOR to rank the alternatives and improve the performances of the alternatives.

Table 1 Explanation of criteria.

<table><tr><td>Dimensions/criteria</td><td>Descriptions</td><td>Proposed in ref.</td></tr><tr><td>Technology ( $D_1$ )</td><td></td><td></td></tr><tr><td>Technology integration ( $C_1$ )</td><td>Technology integration reduces incompatibility between legacy systems and enhances the responsiveness of information systems.</td><td>[11,51]</td></tr><tr><td>Technology competence ( $C_2$ )</td><td>Network technologies and enterprise systems that provide a platform on which the RFID applications can be built, installed in the organization.</td><td>[6,45]</td></tr><tr><td>Security concern ( $C_3$ )</td><td>The degree to which the Internet platform is deemed secure for exchanging data and conducting online transactions.Examples include personal data protection and security in using the RFID technology.</td><td>[2,51]</td></tr><tr><td>Organization ( $D_2$ )</td><td></td><td></td></tr><tr><td>Top management support ( $C_4$ )</td><td>Top management can provide vision, support, and a commitment to create a positive effect on the RFID adoption process.</td><td>[25]</td></tr><tr><td>Firm size ( $C_5$ )</td><td>Large firms typically have the resources necessary to experiment, pilot, and decide what technology and standards they require.</td><td>[6,45]</td></tr><tr><td>Organizational readiness ( $C_6$ )</td><td>Organizations must be prepared to make business process changes, and potential sites need to make adjustments for RFID if benefits are to accrue.</td><td>[6]</td></tr><tr><td>Environment ( $D_3$ )</td><td></td><td></td></tr><tr><td>Competitive pressure ( $C_7$ )</td><td>By adopting RFID, firms may benefit from better inventory visibility, greater operation efficiency,and more accurate data collection.</td><td>[6]</td></tr><tr><td>Partner readiness ( $C_8$ )</td><td>Partner readiness refers to the degree to which a firm&#x27;s customers and suppliers are willing and ready to conduct business activities using RFID.</td><td>[3,49]</td></tr><tr><td>Regulatory support ( $C_9$ )</td><td>This concept is similar to government policies that affect IT diffusion.</td><td>[50]</td></tr><tr><td>Cost ( $D_4$ )</td><td></td><td></td></tr><tr><td>Hardware costs ( $C_{10}$ )</td><td>The hardware costs of RFID adoption.</td><td>[16]</td></tr><tr><td>Software costs ( $C_{11}$ )</td><td>The software costs of RFID adoption.</td><td>[16]</td></tr><tr><td>Implement costs ( $C_{12}$ )</td><td>The implementation cost of RFID adoption, including work disruption, initial installation, management of associated change, etc.</td><td>[16]</td></tr><tr><td>Maintenance costs ( $C_{13}$ )</td><td>The cost of maintaining the operation of the RFID system.</td><td>[16]</td></tr></table>

## 3.1. The DEMATEL technique for constructing INRM

The DEMATEL technique has been successfully used to identify critical success factors in the adoption and assessment processes for emergency [48] and knowledge management [14]. This method can con<sup>fi</sup>rm the interdependence of variables/criteria and restrict the relations that re<sup>fl</sup>ect the characteristics within an essential systemic and developmental trend. The method can be summarized in the following steps [14,23,48]:

Step 1: Find the initial average matrix A by assigning scores to each factor. Suppose we have n factors. Respondents (experts or stakeholders) are asked to rate the direct effects that factor i has on factor j using an integer scale ranging from 0 to 4 to represent the range from “absolutely no in<sup>fl</sup>uence (0)” to “very high in<sup>fl</sup>uence (4)”. We then calculate the mean score among the respondents to arrive at element $a _ { i j }$ and form the initial average matrix $\pmb { A } = [ a _ { i j } ] _ { n \times n } .$

Step 2: Normalize the direct influence matrix D. Using matrix A, the normalized direct-relation matrix $\pmb { { \cal D } } = [ d _ { i j } ] _ { n \times n }$ is calculated using Eqs. (1) and (2).

$$
\boldsymbol {D} = \boldsymbol {z} \times \boldsymbol {A}\tag{1}
$$

$$
z = \min \left\{1 / \max _ {i} \sum_ {j = 1} ^ {n} a _ {i j}, 1 / \max _ {j} \sum_ {i = 1} ^ {n} a _ {i j} \right\}, \quad i, j \in \{1, 2,..., n \}\tag{2}
$$

Step 3: Calculate the total influence matrix T. The total in<sup>fl</sup>uence matrix T can be obtained by summing the direct effects and all of the indirect effects using Eq. (3),

$$
\begin{array}{l} \boldsymbol {T} = \boldsymbol {D} + \boldsymbol {D} ^ {2} + \boldsymbol {D} ^ {3} + \dots + \boldsymbol {D} ^ {h} = \boldsymbol {D} \Big (\boldsymbol {I} + \boldsymbol {D} + \boldsymbol {D} ^ {2} + \dots + \boldsymbol {D} ^ {h - 1} \Big) \Big [ (\boldsymbol {I} - \boldsymbol {D}) (\boldsymbol {I} - \boldsymbol {D}) ^ {- 1} \Big ] \\ = \boldsymbol {D} \Big (\boldsymbol {I} - \boldsymbol {D} ^ {h} \Big) (\boldsymbol {I} - \boldsymbol {D}) ^ {- 1}, \end{array}
$$

where I is denoted as the identity matrix and $( \pmb { I } - \pmb { D } ) ( \pmb { I } - \pmb { D } ) ^ { - 1 } = \pmb { I } .$ Then,

$$
\boldsymbol {T} = \boldsymbol {D} (\boldsymbol {I} - \boldsymbol {D}) ^ {- 1}, \text { when } h \rightarrow \infty , \boldsymbol {D} ^ {h} = [ 0 ] _ {n \times n}\tag{3}
$$

$$
\boldsymbol {D} = \left[ d _ {i j} \right] _ {n \times n}, 0 \leq d _ {i j} <   1, 0 \leq \sum_ {i} d _ {i j} \leq 1,
$$

where D = [d<sub>ij</sub>]<sub>n × n</sub>, 0 ≤ d<sub>ij</sub> b 1, 0 ≤ ∑ <sub>i</sub>d<sub>ij</sub> ≤ 1, $0 \leq \textstyle \sum _ { j } d _ { i j } \leq 1$ , and at least one (but not all) of the columns or rows of the summation is equal to 1 in $\sum ^ { n } d _ { i j }$ and $\sum _ { i = 1 } ^ { n } d _ { i j } ,$ , and thus we can guarantee that lim $_ { h  \infty } { \cal D } ^ { h } = [ 0 ] _ { n \times n } .$ <sup>-</sup>We can denote the row and column sums of the total-in<sup>fl</sup>uence matrix T as column vectors r and s respectively:

$$
\pmb {T} = \left[ t _ {i j} \right] _ {n \times n}, i, j = 1, 2, \dots , n,\tag{4}
$$

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

M.-T. Lu et al. / Decision Support Systems xxx (2013) xxx–xxx

$$
\boldsymbol {r} = \left[ r _ {i} \right] _ {n \times 1} = \left[ \sum_ {j = 1} ^ {n} t _ {i j} \right] _ {n \times 1}, \quad \boldsymbol {s} = \left[ s _ {j} \right] _ {n \times 1} = \left[ \sum_ {i = 1} ^ {n} t _ {i j} \right] _ {1 \times n} ^ {\prime}\tag{5}
$$

where the superscript ′ denotes transpose.

If $r _ { i }$ denotes the row sum $\sum _ { j } ^ { n } { } _ { j } ^ { n } = { } _ { 1 } t _ { i j }$ of the ith row of matrix $T ,$ then $r _ { i }$ denotes the sum of the direct and indirect effects that factor i has on all of the other factors. If $s _ { i }$ denotes the column sum from matrix $T ,$ then $s _ { i }$ denotes the sum of the direct and indirect effects that factor i has received from all of the other factors. Furthermore, $( r _ { i } + s _ { i } )$ provides an index of the strength of the in<sup>fl</sup>uences that are given and received; that is, $( r _ { i } + s _ { i } )$ shows the degree of the total in<sup>fl</sup>uences factor i has in this system. Therefore, $\mathrm { i f } \left( r _ { i } - s _ { i } \right)$ is positive, then factor i has a net in<sup>fl</sup>uence on the other factors, and if $( r _ { i } - s _ { i } )$ is negative, then factor i is, on the whole, being in<sup>fl</sup>uenced by the other factors [43].

## 3.2. Combine the ANP method for finding the influence weights of the criteria

We de<sup>fi</sup>ne the total in<sup>fl</sup>uence matrix $\pmb { T } _ { c } = [ t _ { i j } ] _ { n \times n }$ by the criteria and $\pmb { T } _ { D } = [ t _ { i j } ^ { D } ] _ { m \times m }$ by the dimensions; $\mathbf { T } _ { D }$ can be obtain from $\mathbf { T } _ { c } .$ Next, we normalize the total in<sup>fl</sup>uence matrix $\pmb { T } _ { c }$ by each dimension and normalize the in<sup>fl</sup>uence matrix $\pmb { T } _ { D }$ by the total row sums shown as $\pmb { T } _ { c } ^ { \alpha }$ and $\pmb { T } _ { D } ^ { \alpha }$ respectively to <sup>fi</sup>nd the DANP in<sup>fl</sup>uential weights by dimension. Then, the unweighted supermatrix W can be obtained by transposing the normalized total in<sup>fl</sup>uence matrix $\pmb { T } _ { c } ^ { \alpha }$ to bring it into congruence with the de<sup>fi</sup>nition of an ANP supermatrix, i.e., $\pmb { W } = ( \pmb { T } _ { c } ^ { \alpha } ) ^ { \prime }$ . We can subsequently obtain the weighted supermatrix ${ \pmb W } ^ { \alpha } = { \pmb T } _ { D } ^ { \alpha } { \pmb W }$ (i.e., the normalized supermatrix W). Finally, the DANP in<sup>fl</sup>uence weights can be obtained by taking the $\scriptstyle \operatorname* { l i m } _ { g \to \infty } ( \mathbf W ^ { \alpha } ) ^ { g }$ , where g represents any number as a power. The procedures can be described in <sup>fi</sup>ve steps:

Step 1: The total influence matrix for criteria $\pmb { T } _ { c } = [ t _ { i j } ] _ { n } \times \ d _ { n } .$ The total in<sup>fl</sup>uence matrix $\pmb { T } _ { c }$ for the criteria is shown below:(6)

$$
\boldsymbol {T} _ {c} = \begin{array}{c} \boldsymbol {D} _ {1} \\ \vdots \\ \boldsymbol {T} _ {c} ^ {c _ {1 1}} \\ \vdots \\ \boldsymbol {D} _ {c} ^ {c _ {2 1}} \\ \vdots \\ \boldsymbol {D} _ {c} ^ {c _ {3 1}} \end{array} \left[ \begin{array}{c c c c c} \boldsymbol {T} _ {c} ^ {1 1} & \dots & \boldsymbol {T} _ {c} ^ {1 j} & \dots & \boldsymbol {T} _ {c} ^ {1 n} \\ \vdots & \vdots & \vdots & & \vdots \\ \boldsymbol {T} _ {c} ^ {i 1} & \dots & \boldsymbol {T} _ {c} ^ {i j} & \dots & \boldsymbol {T} _ {c} ^ {i n} \\ \vdots & \vdots & \vdots & & \vdots \\ \boldsymbol {T} _ {c} ^ {n 1} & \dots & \boldsymbol {T} _ {c} ^ {n j} & \dots & \boldsymbol {T} _ {c} ^ {n n} \end{array} \right]\tag{6}
$$

Step 2: The normalized total influence matrix for criteria $\pmb { T } _ { c } ^ { \alpha } .$ . The normalized total in<sup>fl</sup>uence matrix $\pmb { T } _ { c } ^ { \alpha }$ for the criteria is shown below.(7)

$$
\boldsymbol {D} _ {\boldsymbol {c} _ {1 2}} ^ {c _ {1 1}} \left[ \begin{array}{c c c c} \boldsymbol {T} _ {c} ^ {\alpha 1 1} & \dots & \boldsymbol {T} _ {c} ^ {\alpha 1 j} & \dots & \boldsymbol {T} _ {c} ^ {\alpha 1 n} \\ \vdots & & \vdots & & \vdots \\ \vdots & & \vdots & & \vdots \\ \boldsymbol {T} _ {c} ^ {\alpha i 1} & \dots & \boldsymbol {T} _ {c} ^ {\alpha i j} & \dots & \boldsymbol {T} _ {c} ^ {\alpha i n} \\ \vdots & & \vdots & & \vdots \\ \boldsymbol {T} _ {c} ^ {\alpha n 1} & \dots & \boldsymbol {T} _ {c} ^ {\alpha n j} & \dots & \boldsymbol {T} _ {c} ^ {\alpha n n} \\ \boldsymbol {D} _ {\boldsymbol {c} _ {n m}} ^ {c _ {2 2}} & \dots & \boldsymbol {T} _ {c} ^ {\alpha n 1} & \dots & \boldsymbol {T} _ {c} ^ {\alpha n n} \end{array} \right]\tag{7}
$$

For example, an explanation for the normalization of $\pmb { T } _ { c } ^ { \alpha 1 1 }$ on dimension 1 based on dimension 1 (α11) is shown by Eqs. (8) and (9).

$$
d _ {c i} ^ {1 1} = \sum_ {j = 1} ^ {m _ {1}} t _ {i j} ^ {1 1}, i = 1, 2, \dots , m _ {1}\tag{8}
$$

$$
\begin{array}{c} \boldsymbol {T} _ {c} ^ {\alpha 1 1} = \left[ \begin{array}{c c c c c} t _ {c 1 1} ^ {1 1} / d _ {c 1} ^ {1 1} & \dots & t _ {c 1 j} ^ {1 1} / d _ {c 1} ^ {1 1} & \dots & t _ {c 1 m _ {1}} ^ {1 1} / d _ {c 1} ^ {1 1} \\ \vdots & & \vdots & & \vdots \\ t _ {c i 1} ^ {1 1} / d _ {c i} ^ {1 1} & \dots & t _ {c i j} ^ {1 1} / d _ {c i} ^ {1 1} & \dots & t _ {c i m _ {1}} ^ {1 1} / d _ {c i} ^ {1 1} \\ \vdots & & \vdots & & \vdots \\ t _ {c m _ {1} 1} ^ {1 1} / d _ {c m _ {1}} ^ {1 1} & \dots & t _ {c m _ {1} j} ^ {1 1} / d _ {c m _ {1}} ^ {1 1} & \dots & t _ {c m _ {1} m _ {1}} ^ {1 1} / d _ {c m _ {1}} ^ {1 1} \end{array} \right] \\ = \left[ \begin{array}{c c c c c} t _ {c 1 1} ^ {\alpha 1 1} & \dots & t _ {c 1 j} ^ {\alpha 1 1} & \dots & t _ {c 1 m _ {1}} ^ {\alpha 1 1} \\ \vdots & & \vdots & & \vdots \\ t _ {c i 1} ^ {\alpha 1 1} & \dots & t _ {c i j} ^ {\alpha 1 1} & \dots & t _ {c i m _ {1}} ^ {\alpha 1 1} \\ \vdots & & \vdots & & \vdots \\ t _ {c m _ {1} 1} ^ {\alpha 1 1} & \dots & t _ {c m _ {1} j} ^ {\alpha 1 1} & \dots & t _ {c m _ {1} m _ {1}} ^ {\alpha 1 1} \end{array} \right] \end{array}\tag{9}
$$

where $t _ { c i j } ^ { \alpha 1 1 } = t _ { c i j } ^ { 1 1 } / d _ { c i } ^ { 1 1 }$ denotes the element of normalized in<sup>fl</sup>uence for the element $t _ { c i j } ^ { 1 1 }$ (shows that the element of i in<sup>fl</sup>uences other j $( j = 1 , 2 , . . . , m _ { 1 } )$ in which dimension 1 in<sup>fl</sup>uences dimension 1 of total in<sup>fl</sup>uence matrix) divided by the sum $d _ { c i } ^ { 1 1 } \left( d _ { c i } ^ { 1 1 } = \sum _ { j = 1 } ^ { m _ { 1 } } t _ { i j } ^ { 1 1 } , i = 1 , 2 , . . . , m _ { 1 } \right)$ of each row (criterion i in<sup>fl</sup>uences all other criteria in dimension 1).

Step 3: Find the unweighted supermatrix W by transposing the normalized total matrix $\pmb { T } _ { c } ^ { \alpha } .$ Because the total in<sup>fl</sup>uence matrix $\pmb { T } _ { c }$ matches and <sup>fi</sup>lls the interdependence among dimensions and criteria, we can transpose the normalized total in<sup>fl</sup>uence matrix T<sup>α</sup> by the dimensions based on the basic concept of ANP resulting in the unweighted supermatrix $\pmb { W } = ( \pmb { T } _ { c } ^ { \alpha } ) ^ { \prime }$ as shown by Eq. (10).(10)

$$
\boldsymbol {W} = (\boldsymbol {T} _ {c} ^ {a}) ^ {\prime} = \begin{array}{c} D _ {1} \frac {c _ {1 1}}{\vdots} \\ D _ {2} \frac {c _ {1 2}}{\vdots} \\ D _ {3} \frac {c _ {1 3}}{\vdots} \\ D _ {4} \frac {c _ {1 4}}{\vdots} \\ D _ {5} \frac {c _ {1 5}}{\vdots} \\ D _ {6} \frac {c _ {1 6}}{\vdots} \\ D _ {7} \frac {c _ {1 7}}{\vdots} \\ D _ {8} \frac {c _ {1 8}}{\vdots} \\ D _ {9} \frac {c _ {1 9}}{\vdots} \\ D _ {1 0} \frac {c _ {1 1}}{\vdots} \\ D _ {1 1} \frac {c _ {1 2}}{\vdots} \\ D _ {1 2} \frac {c _ {1 3}}{\vdots} \\ D _ {1 3} \frac {c _ {1 4}}{\vdots} \\ D _ {1 4} \frac {c _ {1 5}}{\vdots} \\ D _ {1 5} \frac {c _ {1 6}}{\vdots} \\ D _ {1 6} \frac {c _ {1 7}}{\vdots} \\ D _ {1 7} \frac {c _ {1 8}}{\vdots} \\ D _ {1 8} \frac {c _ {1 9}}{\vdots} \\ D _ {1 9} \frac {c _ {2 0}}{\vdots} \\ D _ {2 0} \frac {c _ {2 1}}{\vdots} \\ D _ {2 1} \frac {c _ {2 2}}{\vdots} \\ D _ {2 2} \frac {c _ {2 3}}{\vdots} \\ D _ {2 3} \frac {c _ {2 4}}{\vdots} \\ D _ {2 4} \frac {c _ {2 5}}{\vdots} \\ D _ {2 5} \frac {c _ {2 6}}{\vdots} \\ D _ {2 6} \frac {c _ {2 7}}{\vdots} \\ D _ {2 7} \frac {c _ {2 8}}{\vdots} \\ D _ {2 8} \frac {c _ {2 9}}{\vdots} \\ D _ {2 9} \frac {c _ {3 0}}{\vdots} \\ D _ {3 0} \frac {c _ {3 1}}{\vdots} \\ D _ {3 1} \frac {c _ {3 2}}{\vdots} \\ D _ {3 2} \frac {c _ {3 3}}{\vdots} \\ D _ {3 3} \frac {c _ {3 4}}{\vdots} \\ D _ {3 4} \frac {c _ {3 5}}{\vdots} \\ D _ {3 5} \frac {c _ {3 6}}{\vdots} \\ D _ {3 6} \frac {c _ {3 7}}{\vdots} \\ D _ {3 7} \frac {c _ {3 8}}{\vdots} \\ D _ {3 8} \frac {c _ {3 9}}{\vdots} \\ D _ {3 9} \frac {c _ {4 0}}{\vdots} \\ D _ {4 0} \frac {c _ {4 1}}{\vdots} \\ D _ {4 1} \frac {c _ {4 2}}{\vdots} \\ D _ {4 2} \frac {c _ {4 3}}{\vdots} \\ D _ {4 3} \frac {c _ {4 4}}{\vdots} \\ D _ {4 4} \frac {c _ {4 5}}{\vdots} \\ D _ {4 5} \frac {c _ {4 6}}{\vdots} \\ D _ {4 6} \frac {c _ {4 7}}{\vdots} \\ D _ {4 7} \frac {c _ {4 8}}{\vdots} \\ D _ {4 8} \frac {c _ {4 9}}{\vdots} \\ D _ {4 9} \frac {c _ {5 0}}{\vdots} \\ D _ {5 0} \frac {c _ {\texttt {\scriptsize a n t e}}}{{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt{\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize bd e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t i o n}}} {{\texttt {\scriptsize c d e c t i o n}}} {{\texttt {\scriptsize b d e c t t i o n}}} {{\texttt {\scriptsize c d e c t t i o n}}} {{\texttt {\scriptsize b d e c t t i o n}}} {{\texttt {\scriptsize c d e c t t i o n}}} {{\texttt {\scriptsize b d e c t t i o n}}} {{\texttt {\scriptsize c d e c t t i o n}}} {{\texttt {\scriptsize b d e c t t i o n}}} {{\texttt {\scriptsize c d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize c d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize c d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize c d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize c d u a l}}} {{\texttt {\scriptsize a d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize a d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize a d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize a d u a l}}} {{\texttt {\scriptsize b d u a l}}} {{\texttt {\scriptsize a d u a l}}} {{\textnormal {\scriptsize a d u a l}}} {{\textnormal {\scriptsize b d u a l}}} {{\textnormal {\scriptsize a d u a l}}} {{\textnormal {\scriptsize b d u a l}}} {{\textnormal {\scriptsize a d u a l}}} {{\textnormal {\scriptsize b d u a l}}} {{\textnormal {\scriptsize a d u a l}}} {{\textnormal {\scriptsize b d u a l}}} {{\textnormal {\scriptsize a d u a l}}} {\textsf {.~l~o~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~i~n~j}} {\textnormal {\scriptsize p~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r~r}} {\textnormal {\scriptsize q~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t~t ~i}} {{\textnormal {\scriptsize r~-}-}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - } {{\textnormal {\scriptsize p~-}-}--}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}-{-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}- {-}< |content_end|>\tag{10}
$$

Step 4: Find the weighted normalized supermatrix $W ^ { \alpha } .$ . To obtain the weighted supermatrix $\boldsymbol { W } ^ { \alpha }$ from the unweighted supermatrix W, we can multiply the normalized total in<sup>fl</sup>uence matrix $\pmb { T } _ { D } ^ { \alpha }$ by the unweighted supermatrix W. The normalized total in<sup>fl</sup>uence matrix $\pmb { T } _ { D } ^ { \alpha }$ can be obtained by using to normalize total in-<sup>fl</sup>uence matrix $\mathbf { T } _ { D }$ in process as shown from Eq. (11) to Eq. (12).

$$
\boldsymbol {T} _ {D} = \left[ \begin{array}{c c c c c} t _ {D} ^ {1 1} & t _ {D} ^ {1 j} & \dots & t _ {D} ^ {1 n} \\ \vdots & \dots & \vdots & & \vdots \\ t _ {D} ^ {i 1} & \dots & t _ {D} ^ {i j} & \dots & t _ {D} ^ {i n} \\ \vdots & \dots & \vdots & & \vdots \\ t _ {D} ^ {n 1} & t _ {D} ^ {n j} & \dots & t _ {D} ^ {n n} \end{array} \right]\tag{11}
$$

We normalized the total in<sup>fl</sup>uence matrix $\pmb { T } _ { D }$ of the dimensions (Eq. (11)) and obtained a new normalized total in<sup>fl</sup>uence matrix T<sup>α</sup> of dimensions as shown by Eq. (12) (where $t _ { D } ^ { o i j } = t _ { D } ^ { i j } / d _ { i }$ and $d _ { i } = \sum _ { j = 1 } ^ { n } t _ { D } ^ { i j } ) .$

$$
\begin{array}{c} \boldsymbol {T} _ {D} ^ {\alpha} = \left[ \begin{array}{c c c c c} t _ {D} ^ {1 1} / d _ {1} & \dots & t _ {D} ^ {1 j} / d _ {1} & \dots & t _ {D} ^ {1 n} / d _ {1} \\ \vdots & & \vdots & & \vdots \\ t _ {D} ^ {i 1} / d _ {i} & \dots & t _ {D} ^ {i j} / d _ {i} & \dots & t _ {D} ^ {i n} / d _ {i} \\ \vdots & & \vdots & & \vdots \\ t _ {D} ^ {n 1} / d _ {n} & \dots & t _ {D} ^ {n j} / d _ {n} & \dots & t _ {D} ^ {n n} / d _ {n} \end{array} \right] \\ = \left[ \begin{array}{c c c c c} t _ {D} ^ {\alpha 1 1} & \dots & t _ {D} ^ {\alpha 1 j} & \dots & t _ {D} ^ {\alpha 1 n} \\ \vdots & & \vdots & & \vdots \\ t _ {D} ^ {\alpha i 1} & \dots & t _ {D} ^ {\alpha i j} & \dots & t _ {D} ^ {\alpha i n} \\ \vdots & & \vdots & & \vdots \\ t _ {D} ^ {\alpha n 1} & \dots & t _ {D} ^ {\alpha n j} & \dots & t _ {D} ^ {\alpha n n} \end{array} \right] \end{array}\tag{12}
$$

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

M.-T. Lu et al. / Decision Support Systems xxx (2013) xxx–xxx

Table 2  
The initial in<sup>fl</sup>uence matrix A for the criteria.

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td> $C_7$ </td><td> $C_8$ </td><td> $C_9$ </td><td> $C_{10}$ </td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td></tr><tr><td> $C_1$ </td><td>0.000</td><td>2.400</td><td>2.400</td><td>2.400</td><td>1.800</td><td>2.800</td><td>2.000</td><td>3.000</td><td>1.600</td><td>2.600</td><td>3.000</td><td>2.800</td><td>3.000</td></tr><tr><td> $C_2$ </td><td>2.200</td><td>0.000</td><td>3.200</td><td>2.400</td><td>1.200</td><td>2.200</td><td>2.400</td><td>2.000</td><td>2.800</td><td>1.800</td><td>2.200</td><td>2.200</td><td>1.800</td></tr><tr><td> $C_3$ </td><td>2.400</td><td>2.400</td><td>0.000</td><td>3.000</td><td>1.200</td><td>1.800</td><td>2.200</td><td>2.200</td><td>3.400</td><td>2.200</td><td>2.200</td><td>1.800</td><td>1.800</td></tr><tr><td> $C_4$ </td><td>3.400</td><td>2.200</td><td>2.800</td><td>0.000</td><td>2.600</td><td>3.200</td><td>2.200</td><td>2.200</td><td>2.600</td><td>2.400</td><td>2.800</td><td>2.800</td><td>3.000</td></tr><tr><td> $C_5$ </td><td>2.200</td><td>2.000</td><td>2.200</td><td>2.200</td><td>0.000</td><td>2.800</td><td>2.000</td><td>1.600</td><td>2.000</td><td>2.800</td><td>2.400</td><td>2.200</td><td>2.600</td></tr><tr><td> $C_6$ </td><td>2.200</td><td>1.800</td><td>2.400</td><td>2.400</td><td>2.400</td><td>0.000</td><td>2.000</td><td>2.600</td><td>2.400</td><td>1.600</td><td>1.600</td><td>2.800</td><td>2.400</td></tr><tr><td> $C_7$ </td><td>2.000</td><td>1.800</td><td>2.000</td><td>2.400</td><td>2.000</td><td>2.400</td><td>0.000</td><td>1.800</td><td>1.400</td><td>1.600</td><td>1.800</td><td>2.400</td><td>2.200</td></tr><tr><td> $C_8$ </td><td>2.400</td><td>2.400</td><td>2.400</td><td>2.200</td><td>1.600</td><td>2.400</td><td>2.800</td><td>0.000</td><td>1.400</td><td>2.200</td><td>2.400</td><td>2.600</td><td>2.200</td></tr><tr><td> $C_9$ </td><td>3.000</td><td>1.600</td><td>2.800</td><td>2.800</td><td>2.200</td><td>2.400</td><td>2.400</td><td>2.400</td><td>0.000</td><td>2.200</td><td>1.600</td><td>2.200</td><td>2.800</td></tr><tr><td> $C_{10}$ </td><td>2.600</td><td>2.000</td><td>1.400</td><td>2.200</td><td>2.200</td><td>2.000</td><td>1.800</td><td>1.800</td><td>1.800</td><td>0.000</td><td>2.400</td><td>2.600</td><td>3.000</td></tr><tr><td> $C_{11}$ </td><td>3.200</td><td>1.600</td><td>2.600</td><td>2.400</td><td>2.200</td><td>2.200</td><td>1.800</td><td>1.600</td><td>1.400</td><td>2.400</td><td>0.000</td><td>2.800</td><td>2.200</td></tr><tr><td> $C_{12}$ </td><td>2.800</td><td>2.200</td><td>2.000</td><td>2.600</td><td>2.400</td><td>2.400</td><td>2.000</td><td>1.800</td><td>2.200</td><td>2.400</td><td>2.600</td><td>0.000</td><td>3.200</td></tr><tr><td> $C_{13}$ </td><td>2.800</td><td>2.000</td><td>1.800</td><td>2.400</td><td>2.800</td><td>2.400</td><td>2.600</td><td>2.600</td><td>1.600</td><td>2.400</td><td>2.200</td><td>2.200</td><td>0.000</td></tr></table>

Next, we multiplied the normalized total in<sup>fl</sup>uence matrix of the dimensions $\pmb { T } _ { D } ^ { \alpha } ,$ with the unweighted supermatrix W to obtain the new weighted supermatrix $\boldsymbol { W } ^ { \alpha } \left( \mathrm { i . e . } \right.$ , by the normalized matrix) as shown Eq. (13).

$$
\begin{array}{c} \boldsymbol {W} ^ {\alpha} = \boldsymbol {T} _ {D} ^ {\alpha} \boldsymbol {W} \\ = \left[ \begin{array}{c c c c c} t _ {D} ^ {\alpha 1 1} \times \boldsymbol {W} ^ {1 1} & \dots & t _ {D} ^ {\alpha i 1} \times \boldsymbol {W} ^ {i 1} & \dots & t _ {D} ^ {\alpha n 1} \times \boldsymbol {W} ^ {n 1} \\ \vdots & & \vdots & & \vdots \\ t _ {D} ^ {\alpha 1 j} \times \boldsymbol {W} ^ {1 j} & \dots & t _ {D} ^ {\alpha i j} \times \boldsymbol {W} ^ {i j} & \dots & t _ {D} ^ {\alpha n j} \times \boldsymbol {W} ^ {n j} \\ \vdots & & \vdots & & \vdots \\ t _ {D} ^ {\alpha 1 n} \times \boldsymbol {W} ^ {1 n} & \dots & t _ {D} ^ {\alpha i n} \times \boldsymbol {W} ^ {i n} & \dots & t _ {D} ^ {\alpha n n} \times \boldsymbol {W} ^ {n n} \end{array} \right] \end{array}\tag{13}
$$

Step 5: Find the limit of the weighted supermatrix $\boldsymbol { W } ^ { \alpha }$ by raising it to a sufficiently large power g $( { \mathrm { i } } . { \mathrm { e } } . g \to \infty )$ . If we raise the weighted supermatrix $\boldsymbol { W } ^ { \alpha }$ to a suf<sup>fi</sup>ciently large power $^ { g , }$ then the weighted normalized supermatrix $\boldsymbol { W } ^ { \alpha }$ converges and becomes a long-term stable supermatrix, i.e., $\scriptstyle \operatorname* { l i m } _ { g \to \infty } ( W ^ { \alpha } ) ^ { g }$ , where g represents any number as a power. Consequently, we can obtain what DANP calls the in<sup>fl</sup>uential weights (i.e., global in<sup>fl</sup>uential weights).

## 3.3. The VIKOR method for ranking and improving the alternatives

Opricovic [27] proposed the compromise ranking method (VIKOR) as a technique that could be implemented within the MCDM model $\left[ 2 8 - 3 1 , 4 0 - 4 2 \right]$ . If the feasible alternatives are represented by $A _ { 1 } , A _ { 2 } ,$ $\ldots , A _ { k } , . . . , A _ { m } ,$ the performance scores of alternative $A _ { k }$ in each criterion j can be denoted by ${ f _ { k j } } \left( { k = 1 , 2 , . . . , m ; j = 1 , 2 , . . . , n } \right) ; w$ is the in<sup>fl</sup>uential weight (by DANP) of the jth criterion, where $j = 1 , 2 , . . . , n .$ , and n is the number of criteria. We de<sup>fi</sup>ne the best ${ \bf { \bar { f } } } _ { j } ^ { * }$ values (aspired level) and the worst $f _ { j } ^ { - }$ values (tolerable level) of all of the criterion functions, $j = 1 , 2 , . . . ,$ n. Next, we began the development of the VIKOR method using the following form of the $L _ { p } - \mathrm { { m e t r i c } } .$

$$
L _ {k} ^ {p} = \left\{\sum_ {j = 1} ^ {n} \left[ w _ {j} \left(\left| f _ {j} ^ {*} - f _ {k j} \right|\right) / \left(\left| f _ {j} ^ {*} - f _ {j} ^ {-} \right|\right) \right] ^ {p} \right\} ^ {1 / p}\tag{14}
$$

where $1 \leq p \leq \infty ; k = 1 , 2 , . . . ,$ , m; the weight w is derived from the DANP (the so-called DDANPV method combines the DEMATEL, ANP, and VIKOR methods). To formulate the ranking and gap measures, $L _ { k } ^ { p = 1 } \ { \mathrm { ~ ( a s ~ } } S _ { k } { \mathrm { ) } }$ and $L _ { k } ^ { p = \infty } \ ( { \mathsf { a s } } \ Q _ { k } )$ are used in the VIKOR method $[ \ddot { 2 } 7 , 2 8 , 3 0 , 3 1 , 4 1 , 4 2 ]$

$$
S _ {k} = L _ {k} ^ {p = 1} = \sum_ {j = 1} ^ {n} \left[ w _ {j} \left(\left| f _ {j} ^ {*} - f _ {k j} \right|\right) / \left(\left| f _ {j} ^ {*} - f _ {j} ^ {-} \right|\right) \right]\tag{15}
$$

$$
Q _ {k} = L _ {k} ^ {p = \infty} = \max _ {j} \left\{\left(\left| f _ {j} ^ {*} - f _ {k j} \right|\right) / \left(\left| f _ {j} ^ {*} - f _ {j} ^ {-} \right|\right) | j = 1, 2, \dots , n \right\}\tag{16}
$$

The compromise solution minL<sup>p</sup> shows that the synthesized/integrated gap is the minimum and, as a result, will be selected, as its value is the closest to the aspired level. In addition, the group utility (average gap) is emphasized when $p$ is small (such as $p = 1 ) ;$ however, if p is in<sup>fi</sup>nite, then the individual maximum regrets/gaps gain more importance in prior improvement (basic concept from Yu [44] and Freimer and Yu [10]) of each dimension/criterion. Consequently, $\mathrm { m i n } _ { k } S _ { k }$ stresses the maximum group utility for the majority (in other words, shown for minimizing average gap); however, $\mathrm { m i n } _ { k } Q _ { k }$ stresses selecting the minimum from the maximum individual regrets/gaps (in other words, shown which maximum gap for prior improvement). Following the above aforementioned ideas, we <sup>fi</sup>nd that the compromise ranking and improvement algorithm VIKOR has four steps as described below.

Step 1: Obtain an aspired or tolerable level. We calculate the best $f _ { j } ^ { * }$ values (aspired level) and the worst $f _ { j } ^ { - }$ values (tolerable level) of all of the criterion functions, ${ \bf { \bar { \Phi } } } _ { j } = 1 , 2 , . . . , n .$ For example, the performance value of each criterion can be obtained by using questionnaires with a scale ranging from 0 point (complete dissatisfaction) to 10 points (the best satisfaction). Therefore, we can set the aspired level as $f _ { j } ^ { * } = 1 0$ and the worst value as $f _ { j } ^ { - } = 0 .$ . As a result, in this research, we are setting $f _ { j } ^ { * } = 1 0$ as the aspired level and setting $f _ { j } ^ { - } = 0$ as the worst value for normalization, in contrast to the traditional approach, which sets $f _ { j } ^ { * } = \operatorname* { m a x } _ { k } f _ { k j }$ and $f _ { j } ^ { - } = \operatorname* { m i n } _ { k } f _ { k j } .$ <sup>¼</sup>. We propose this new idea for improvement <sup>¼</sup>to avoid the traditional approach of “choosing the best among the inferior choices/options/alternatives (i.e., pick the best apple in a barrel of rotten apples)”. The original performance rating matrix can be converted into a normalized gaps-rating matrix $[ r _ { k j } ] _ { m \times n }$ (where the rating $r _ { k j }$ shows the gap of alternative k in $j$ criterion; how can we reduce the gaps of each criterion and dimension based on the in<sup>fl</sup>uential network relation map for achieving the aspired level?) using the following equation:

$$
r _ {k j} = \left(\left| f _ {j} ^ {*} - f _ {k j} \right|\right) / \left(\left| f _ {j} ^ {*} - f _ {j} ^ {-} \right|\right)\tag{17}
$$

Step 2: Calculate the means of group utility and maximal regret. These gap-values can be computed using the rating-weighted $S _ { k } =$ $\sum { \overset { n } { j } } = 1 W j r _ { k j } ( \mathrm { i . e . }$ ., the synthesized/integrated gap for all criteria) and $\begin{array} { r l } { Q _ { k } = \operatorname* { m a x } \quad } & { { } \quad j \left\{ r _ { k j } | j = 1 , 2 , . . . , n \right\} } \end{array}$ (shown which the maximal gap of alternative k for prior improvement in each dimension and overall criteria respectively).

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

M.-T. Lu et al. / Decision Support Systems xxx (2013) xxx–xxx

Table 4  
Table 3  
The normalized direct-in<sup>fl</sup>uence matrix D for the criteria.

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td> $C_7$ </td><td> $C_8$ </td><td> $C_9$ </td><td> $C_{10}$ </td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td></tr><tr><td> $C_1$ </td><td>0.000</td><td>0.075</td><td>0.075</td><td>0.075</td><td>0.056</td><td>0.087</td><td>0.062</td><td>0.093</td><td>0.050</td><td>0.081</td><td>0.093</td><td>0.087</td><td>0.093</td></tr><tr><td> $C_2$ </td><td>0.068</td><td>0.000</td><td>0.099</td><td>0.075</td><td>0.037</td><td>0.068</td><td>0.075</td><td>0.062</td><td>0.087</td><td>0.056</td><td>0.068</td><td>0.068</td><td>0.056</td></tr><tr><td> $C_3$ </td><td>0.075</td><td>0.075</td><td>0.000</td><td>0.093</td><td>0.037</td><td>0.056</td><td>0.068</td><td>0.068</td><td>0.106</td><td>0.068</td><td>0.068</td><td>0.056</td><td>0.056</td></tr><tr><td> $C_4$ </td><td>0.106</td><td>0.068</td><td>0.087</td><td>0.000</td><td>0.081</td><td>0.099</td><td>0.068</td><td>0.068</td><td>0.081</td><td>0.075</td><td>0.087</td><td>0.087</td><td>0.093</td></tr><tr><td> $C_5$ </td><td>0.068</td><td>0.062</td><td>0.068</td><td>0.068</td><td>0.000</td><td>0.087</td><td>0.062</td><td>0.050</td><td>0.062</td><td>0.087</td><td>0.075</td><td>0.068</td><td>0.081</td></tr><tr><td> $C_6$ </td><td>0.068</td><td>0.056</td><td>0.075</td><td>0.075</td><td>0.075</td><td>0.000</td><td>0.062</td><td>0.081</td><td>0.075</td><td>0.050</td><td>0.050</td><td>0.087</td><td>0.075</td></tr><tr><td> $C_7$ </td><td>0.062</td><td>0.056</td><td>0.062</td><td>0.075</td><td>0.062</td><td>0.075</td><td>0.000</td><td>0.056</td><td>0.043</td><td>0.050</td><td>0.056</td><td>0.075</td><td>0.068</td></tr><tr><td> $C_8$ </td><td>0.075</td><td>0.075</td><td>0.075</td><td>0.068</td><td>0.050</td><td>0.075</td><td>0.087</td><td>0.000</td><td>0.043</td><td>0.068</td><td>0.075</td><td>0.081</td><td>0.068</td></tr><tr><td> $C_9$ </td><td>0.093</td><td>0.050</td><td>0.087</td><td>0.087</td><td>0.068</td><td>0.075</td><td>0.075</td><td>0.075</td><td>0.000</td><td>0.068</td><td>0.050</td><td>0.068</td><td>0.087</td></tr><tr><td> $C_{10}$ </td><td>0.081</td><td>0.062</td><td>0.043</td><td>0.068</td><td>0.068</td><td>0.062</td><td>0.056</td><td>0.056</td><td>0.056</td><td>0.000</td><td>0.075</td><td>0.081</td><td>0.093</td></tr><tr><td> $C_{11}$ </td><td>0.099</td><td>0.050</td><td>0.081</td><td>0.075</td><td>0.068</td><td>0.068</td><td>0.056</td><td>0.050</td><td>0.043</td><td>0.075</td><td>0.000</td><td>0.087</td><td>0.068</td></tr><tr><td> $C_{12}$ </td><td>0.087</td><td>0.068</td><td>0.062</td><td>0.081</td><td>0.075</td><td>0.075</td><td>0.062</td><td>0.056</td><td>0.068</td><td>0.075</td><td>0.081</td><td>0.000</td><td>0.099</td></tr><tr><td> $C_{13}$ </td><td>0.087</td><td>0.062</td><td>0.056</td><td>0.075</td><td>0.087</td><td>0.075</td><td>0.081</td><td>0.081</td><td>0.050</td><td>0.075</td><td>0.068</td><td>0.068</td><td>0.000</td></tr></table>

Step 3: Calculate the index value. This value can be measured by the following equation:

$$
\begin{array}{l} R _ {k} = v (S _ {k} - S ^ {*}) / (S ^ {-} - S ^ {*}) \\ \qquad + (1 - v) (Q _ {k} - Q ^ {*}) / (Q ^ {-} - Q ^ {*}), v \in [ 0, 1 ] \end{array}\tag{18}
$$

where $S ^ { * } = \operatorname* { m i n } _ { i } S _ { i }$ (traditional approach); or let $S ^ { * } = 0$ (no gap, the aspiration level is achieved in our approach); $S ^ { - } =$ $\boldsymbol { \mathrm { m a x } } _ { i } S _ { i }$ (traditional approach), or let $S ^ { - } = 1$ <sup>¼</sup>(the worst situation in our approach); ${ Q } ^ { * } = \operatorname* { m i n } _ { i } { Q } _ { i }$ (traditional approach), or let $Q ^ { * } = 0$ (no gap, the aspiration level is achieved in our approach); and $Q ^ { - } = \operatorname* { m a x } _ { i } Q _ { i }$ (traditional approach), or let $Q ^ { - } = 1$ <sup>¼</sup>(the worst situation in our approach). Eq. (18) can be rewritten as ${ \cal R } _ { k } = \nu S _ { k } + ( 1 - \nu ) Q _ { k }$ when $S ^ { * } = 0$ and $Q ^ { * } =$ 0 (i.e., all criteria have achieved their corresponding aspiration levels), and $S ^ { - } = 1$ and $Q ^ { - } = 1$ (i.e., the worst situation). How do decision makers determine the v value? When v = 1, only the average gap (the average regret) is considered in each dimension or overall; when $\nu = 0 ,$ , only the maximum gap in the improvement is considered a priority for the criterion in each dimension or overall. The value obtained from $\operatorname* { m i n } _ { i } S _ { i }$ represents the maximum group utility (the minimum average gap indicator), and the value obtained from max $Q _ { i }$ represents the maximum regret (the largest gap shown as priority improvement). Thus, v represents the weight of the strategy. Generally $\nu = 0 . 5 ,$ , which can be adjusted depending on the case under consideration from the view-points of dimensions and overall for improvement priority; v = 1 indicates that only the average gap is considered, and $\nu = 0$ indicates that only the maximum gap is prioritized for improvement individually.

The compromise ranking method (VIKOR) is applied to determine the compromise solution by measured gaps. This solution is useful for decision-makers because it offers the maximum group utility for the majority (shown by min S, i.e., shown for minimizing average gap) and the maximum regret (basic concept from Yu [44]) of the minimum number of individuals of the opponent (shown by min $Q _ { ☉ }$ i.e., shown which maximum gap for priority improvement) to reduce the gaps for improving the performance values in each criterion and dimension forward to achieving the aspired levels in each dimensions and criterion.

## 4. An empirical case study on RFID adoption in Taiwan's healthcare industry

In this section, we present an empirical study using the proposed DDANPV model to evaluate, select, and improve upon the best alternative for RFID adoption in Taiwan's healthcare industry.

## 4.1. Background and problem descriptions

In the environment of a hospital, where service demand might be unpredictable, and the infrastructure is often complex, the speed with which critical medical assets can be located might determine the outcome of a hospital's mission to save lives [19,22,35]. RFID has received considerable attention because it promises to meet the challenge of tracking people and locating items within a large building complex. However, the adoption of new technology involves an analysis of its costs and bene<sup>fi</sup>ts, and managers in the healthcare industry need an evaluation framework to help them decide whether to adopt RFID technologies, and if so, what type or con<sup>fi</sup>guration of RFID applications they should adopt.

The total in<sup>fl</sup>uence matrix $T _ { c }$ for the criteria.

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td> $C_7$ </td><td> $C_8$ </td><td> $C_9$ </td><td> $C_{10}$ </td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td></tr><tr><td> $C_1$ </td><td>0.471</td><td>0.444</td><td>0.492</td><td>0.513</td><td>0.432</td><td>0.519</td><td>0.457</td><td>0.479</td><td>0.423</td><td>0.480</td><td>0.501</td><td>0.526</td><td>0.543</td></tr><tr><td> $C_2$ </td><td>0.485</td><td>0.335</td><td>0.470</td><td>0.467</td><td>0.374</td><td>0.456</td><td>0.425</td><td>0.410</td><td>0.418</td><td>0.415</td><td>0.435</td><td>0.462</td><td>0.461</td></tr><tr><td> $C_3$ </td><td>0.496</td><td>0.408</td><td>0.384</td><td>0.488</td><td>0.379</td><td>0.451</td><td>0.424</td><td>0.420</td><td>0.437</td><td>0.430</td><td>0.439</td><td>0.456</td><td>0.467</td></tr><tr><td> $C_4$ </td><td>0.604</td><td>0.467</td><td>0.536</td><td>0.479</td><td>0.483</td><td>0.565</td><td>0.493</td><td>0.488</td><td>0.480</td><td>0.507</td><td>0.528</td><td>0.560</td><td>0.579</td></tr><tr><td> $C_5$ </td><td>0.493</td><td>0.399</td><td>0.449</td><td>0.469</td><td>0.346</td><td>0.481</td><td>0.421</td><td>0.406</td><td>0.401</td><td>0.450</td><td>0.448</td><td>0.470</td><td>0.492</td></tr><tr><td> $C_6$ </td><td>0.489</td><td>0.391</td><td>0.451</td><td>0.471</td><td>0.411</td><td>0.397</td><td>0.418</td><td>0.430</td><td>0.409</td><td>0.414</td><td>0.423</td><td>0.482</td><td>0.483</td></tr><tr><td> $C_7$ </td><td>0.441</td><td>0.357</td><td>0.402</td><td>0.430</td><td>0.366</td><td>0.427</td><td>0.323</td><td>0.372</td><td>0.348</td><td>0.377</td><td>0.391</td><td>0.431</td><td>0.436</td></tr><tr><td> $C_8$ </td><td>0.497</td><td>0.410</td><td>0.454</td><td>0.468</td><td>0.391</td><td>0.469</td><td>0.442</td><td>0.357</td><td>0.384</td><td>0.432</td><td>0.447</td><td>0.480</td><td>0.480</td></tr><tr><td> $C_9$ </td><td>0.538</td><td>0.407</td><td>0.486</td><td>0.507</td><td>0.428</td><td>0.492</td><td>0.452</td><td>0.448</td><td>0.361</td><td>0.454</td><td>0.447</td><td>0.492</td><td>0.520</td></tr><tr><td> $C_{10}$ </td><td>0.488</td><td>0.387</td><td>0.413</td><td>0.453</td><td>0.397</td><td>0.445</td><td>0.402</td><td>0.398</td><td>0.381</td><td>0.356</td><td>0.434</td><td>0.466</td><td>0.488</td></tr><tr><td> $C_{11}$ </td><td>0.514</td><td>0.384</td><td>0.453</td><td>0.468</td><td>0.404</td><td>0.459</td><td>0.409</td><td>0.401</td><td>0.380</td><td>0.434</td><td>0.374</td><td>0.480</td><td>0.475</td></tr><tr><td> $C_{12}$ </td><td>0.535</td><td>0.425</td><td>0.467</td><td>0.504</td><td>0.436</td><td>0.494</td><td>0.443</td><td>0.433</td><td>0.426</td><td>0.461</td><td>0.476</td><td>0.430</td><td>0.533</td></tr><tr><td> $C_{13}$ </td><td>0.521</td><td>0.409</td><td>0.449</td><td>0.485</td><td>0.435</td><td>0.482</td><td>0.448</td><td>0.443</td><td>0.398</td><td>0.449</td><td>0.454</td><td>0.482</td><td>0.429</td></tr></table>

Note: $\frac { 1 } { \eta ^ { 2 } } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \frac { \left| t _ { i j } ^ { p } - t _ { i j } ^ { p - 1 } \right| } { t _ { i j } ^ { p } }$ 100% = 2.439% b 5%, i.e., signi<sup>fi</sup>cant con<sup>fi</sup>dence level is 97.561%, where $p = 1 5$ denotes the number of experts and $t _ { i j } ^ { p }$ is the average in<sup>fl</sup>uence of criterion ion criterion j. Here n denotes the number of criteria, with n = 13 and $n ^ { 2 } = 1 6 9 .$

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

Table 5  
The total in<sup>fl</sup>uence matrix $T _ { D }$ for the dimensions.

<table><tr><td>Dimensions</td><td> $D_1$ </td><td> $D_2$ </td><td> $D_3$ </td><td> $D_4$ </td></tr><tr><td> $D_1$  technology</td><td>0.443</td><td>0.453</td><td>0.433</td><td>0.468</td></tr><tr><td> $D_2$  organization</td><td>0.475</td><td>0.456</td><td>0.438</td><td>0.486</td></tr><tr><td> $D_3$  environment</td><td>0.444</td><td>0.442</td><td>0.387</td><td>0.449</td></tr><tr><td> $D_4$  cost</td><td>0.454</td><td>0.455</td><td>0.414</td><td>0.451</td></tr></table>

Table 6  
The sum of in<sup>fl</sup>uences given and received on the dimensions

<table><tr><td>Dimensions</td><td> $r_i$ </td><td> $s_i$ </td><td> $r_i + s_i$ </td><td> $r_i - s_i$ </td></tr><tr><td> $D_1$  technology</td><td>1.796</td><td>1.815</td><td>3.612</td><td>-0.019</td></tr><tr><td> $D_2$  organization</td><td>1.856</td><td>1.806</td><td>3.662</td><td>0.050</td></tr><tr><td> $D_3$  environment</td><td>1.722</td><td>1.672</td><td>3.394</td><td>0.050</td></tr><tr><td> $d_4$  cost</td><td>1.774</td><td>1.854</td><td>3.628</td><td>-0.081</td></tr></table>

## 4.2. Data collection

The data in this study were collected from 15 experts with professional management and decision-making experience in the healthcare industry. Most of these experts had worked in the healthcare industry for more than ten years, and their responses were collected via personal interviews and questionnaires in May 2011. The objects of this questionnaire are the experts and not the users, with the goal of analyzing user behavior. In this respect, it is not the distribution of the sample size that is at issue but rather the consensus of the expert opinions. In other words, we need to test the consensus of the experts. If the number of experts increases, the degree of consensus should increase so that the differences in their responses will decrease. For the <sup>fi</sup>fteen experts, a 97.561% signi<sup>fi</sup>cance con<sup>fi</sup>dence level is obtained (see the notes below Table 4).

## 4.3. Construct the network relation map using DEMATEL

The DEMATEL technique introduced in Section 3.1 is used to analyze the interrelationships between the 13 criteria summarized from the literature. First, the direct in<sup>fl</sup>uence matrix A for the criteria is obtained (see Table 2). Next, the normalized direct-in<sup>fl</sup>uence matrix D for criteria can be calculated by Eq. (1) (see Table $^ { 3 ) }$ . Third, the total direct in<sup>fl</sup>uence matrices T for the criteria and $\pmb { T } _ { D }$ for the dimensions are calculated based on Eq. (3) (see Tables 4 and 5). Finally, the in<sup>fl</sup>uence network relation map (INRM) can be constructed using the vectors r and s in the total direct in<sup>fl</sup>uence matrix $\mathbf { T } _ { D }$ (see Table 6), as shown in Fig. 1.

## 4.4. Using DANP to calculate the influence weights for each criterion

The in<sup>fl</sup>uence weights (global weights) for the 13 criteria can be calculated by using DANP, as shown in Tables 7–9. The results show that the experts consider technology integration, top management support, and organizational readiness as the most important criteria, with in<sup>fl</sup>uence weights of 0.094, 0.089, and 0.088, respectively; they are least concerned with software costs and hardware costs, with in<sup>fl</sup>uence weights of 0.062 and 0.061, respectively. In the technology dimension, the experts consider technology integration to be the most important criterion. In the organization dimension, the experts think that top management support is the most important criterion. In the environment dimension, the experts consider competitive pressure to be the most important criterion. In the cost dimension, the experts consider maintenance costs to be the most important criterion. These <sup>fi</sup>ndings reveal that the experts believe technology integration should not be overlooked by managers when selecting a method to evaluate the RFID adoption process. Additionally, we <sup>fi</sup>nd that the experts are less concerned about technology and environmental dimensions, as the means of these dimensions are substantially lower than those of the other dimensions.

## 4.5. Compromise ranking by using VIKOR

We apply the VIKOR method to determine the compromise rankings after calculating the in<sup>fl</sup>uence weights for the criteria using DANP in Section 4.4. The results of our calculations (Table 10) show that the total gaps are the largest in asset tracking management performance (0.408), meaning that the alternative program should <sup>fi</sup>rst improve

![](/api/attachments/K88HMUKQ/fulltext/images/0499738f0e6aec63f9e432c40e7560eeba2c2d6c99df7c3efba5eb569634ba07.jpg)  
Fig. 1. The impact of RFID adoption's decision

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

M.-T. Lu et al. / Decision Support Systems xxx (2013) xxx–xxx

Table 8  
Table 7  
The unweighted supermatrix $\pmb { W } = ( \pmb { T } _ { c } ^ { \alpha } ) ^ { \prime }$

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td> $C_7$ </td><td> $C_8$ </td><td> $C_9$ </td><td> $C_{10}$ </td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td></tr><tr><td> $C_1$ </td><td>0.335</td><td>0.375</td><td>0.381</td><td>0.374</td><td>0.366</td><td>0.365</td><td>0.365</td><td>0.364</td><td>0.373</td><td>0.374</td><td>0.374</td><td>0.371</td><td>0.373</td></tr><tr><td> $C_2$ </td><td>0.313</td><td>0.264</td><td>0.315</td><td>0.291</td><td>0.299</td><td>0.296</td><td>0.299</td><td>0.302</td><td>0.288</td><td>0.301</td><td>0.289</td><td>0.299</td><td>0.298</td></tr><tr><td> $C_3$ </td><td>0.351</td><td>0.361</td><td>0.303</td><td>0.335</td><td>0.336</td><td>0.339</td><td>0.336</td><td>0.335</td><td>0.339</td><td>0.325</td><td>0.337</td><td>0.330</td><td>0.329</td></tr><tr><td> $C_4$ </td><td>0.367</td><td>0.377</td><td>0.386</td><td>0.333</td><td>0.376</td><td>0.385</td><td>0.368</td><td>0.368</td><td>0.372</td><td>0.367</td><td>0.369</td><td>0.370</td><td>0.365</td></tr><tr><td> $C_5$ </td><td>0.262</td><td>0.256</td><td>0.256</td><td>0.281</td><td>0.238</td><td>0.285</td><td>0.267</td><td>0.262</td><td>0.265</td><td>0.272</td><td>0.270</td><td>0.270</td><td>0.277</td></tr><tr><td> $C_6$ </td><td>0.371</td><td>0.366</td><td>0.359</td><td>0.386</td><td>0.386</td><td>0.330</td><td>0.365</td><td>0.370</td><td>0.363</td><td>0.361</td><td>0.362</td><td>0.360</td><td>0.359</td></tr><tr><td> $C_7$ </td><td>0.338</td><td>0.340</td><td>0.334</td><td>0.338</td><td>0.343</td><td>0.335</td><td>0.313</td><td>0.369</td><td>0.357</td><td>0.341</td><td>0.344</td><td>0.343</td><td>0.348</td></tr><tr><td> $C_8$ </td><td>0.351</td><td>0.330</td><td>0.330</td><td>0.334</td><td>0.332</td><td>0.341</td><td>0.354</td><td>0.305</td><td>0.353</td><td>0.337</td><td>0.337</td><td>0.332</td><td>0.341</td></tr><tr><td> $C_9$ </td><td>0.311</td><td>0.330</td><td>0.336</td><td>0.328</td><td>0.325</td><td>0.324</td><td>0.333</td><td>0.326</td><td>0.290</td><td>0.322</td><td>0.320</td><td>0.325</td><td>0.311</td></tr><tr><td> $C_{10}$ </td><td>0.231</td><td>0.231</td><td>0.237</td><td>0.231</td><td>0.239</td><td>0.228</td><td>0.229</td><td>0.233</td><td>0.234</td><td>0.205</td><td>0.241</td><td>0.239</td><td>0.242</td></tr><tr><td> $C_{11}$ </td><td>0.249</td><td>0.249</td><td>0.248</td><td>0.246</td><td>0.243</td><td>0.242</td><td>0.244</td><td>0.247</td><td>0.239</td><td>0.253</td><td>0.220</td><td>0.255</td><td>0.254</td></tr><tr><td> $C_{12}$ </td><td>0.260</td><td>0.262</td><td>0.257</td><td>0.260</td><td>0.256</td><td>0.267</td><td>0.264</td><td>0.262</td><td>0.259</td><td>0.269</td><td>0.273</td><td>0.232</td><td>0.268</td></tr><tr><td> $C_{13}$ </td><td>0.260</td><td>0.258</td><td>0.258</td><td>0.263</td><td>0.262</td><td>0.263</td><td>0.263</td><td>0.258</td><td>0.267</td><td>0.273</td><td>0.267</td><td>0.274</td><td>0.236</td></tr></table>

asset tracking management performance and then improve patienttracking management performance. Therefore, in the optimal RFID adoption application, managers should focus on how to improve asset tracking management performance to achieve the desired level of performance.

## 4.6. Implications and discussion

costs [3,11]. Similar to the <sup>fi</sup>ndings in other industries studies of new technology adoption, we <sup>fi</sup>nd that a <sup>fi</sup>rm's ability to convert new technology into core capabilities is essential and that technology integration is the most signi<sup>fi</sup>cant factor when evaluating RFID adoption in the healthcare industry.

There are several important results of our study. First, according to our DANP results, technology integration is the most important criterion for evaluating RFID adoption with an in<sup>fl</sup>uence weight of 0.094. By reducing the incompatibility between legacy systems and enhancing the responsiveness of information systems, technology integration exerts an important effect on the adoption and diffusion of new technologies in an organization and helps improve performance via a reduction in cycle times, better customer services, and lower procurement

Second, top management support is the second most important criterion, with an in<sup>fl</sup>uence weight of 0.089. This <sup>fi</sup>nding also echoes the results obtained in previous studies, where top management support is shown to be a key factor in overcoming resistance to changes caused by new technology adoption and diffusion [13]. Thus, managers in the healthcare industry should regard strong commitment and support within top management as key to successful RFID adoption.

Third, compromise ranking from VIKOR (see Table 10) shows that, between the choice of the two RFID applications, the system with better patient-tracking management system (total gaps = 0.373) is preferred to the system with better asset-tracking management system

The normalized supermatrix $\pmb { W } ^ { \alpha } = \pmb { T } _ { D } ^ { \alpha } \pmb { W } .$

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td> $C_7$ </td><td> $C_8$ </td><td> $C_9$ </td><td> $C_{10}$ </td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td></tr><tr><td> $C_1$ </td><td>0.083</td><td>0.078</td><td>0.086</td><td>0.088</td><td>0.074</td><td>0.089</td><td>0.081</td><td>0.085</td><td>0.075</td><td>0.061</td><td>0.064</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_2$ </td><td>0.093</td><td>0.064</td><td>0.090</td><td>0.091</td><td>0.073</td><td>0.089</td><td>0.082</td><td>0.079</td><td>0.080</td><td>0.061</td><td>0.064</td><td>0.068</td><td>0.068</td></tr><tr><td> $C_3$ </td><td>0.095</td><td>0.078</td><td>0.073</td><td>0.093</td><td>0.073</td><td>0.086</td><td>0.080</td><td>0.079</td><td>0.082</td><td>0.063</td><td>0.064</td><td>0.066</td><td>0.068</td></tr><tr><td> $C_4$ </td><td>0.096</td><td>0.075</td><td>0.085</td><td>0.077</td><td>0.078</td><td>0.091</td><td>0.080</td><td>0.079</td><td>0.078</td><td>0.061</td><td>0.064</td><td>0.068</td><td>0.070</td></tr><tr><td> $C_5$ </td><td>0.094</td><td>0.076</td><td>0.086</td><td>0.089</td><td>0.066</td><td>0.091</td><td>0.081</td><td>0.078</td><td>0.077</td><td>0.063</td><td>0.063</td><td>0.066</td><td>0.069</td></tr><tr><td> $C_6$ </td><td>0.094</td><td>0.075</td><td>0.087</td><td>0.090</td><td>0.079</td><td>0.076</td><td>0.079</td><td>0.081</td><td>0.077</td><td>0.060</td><td>0.061</td><td>0.070</td><td>0.070</td></tr><tr><td> $C_7$ </td><td>0.095</td><td>0.077</td><td>0.086</td><td>0.090</td><td>0.077</td><td>0.090</td><td>0.070</td><td>0.080</td><td>0.075</td><td>0.060</td><td>0.062</td><td>0.069</td><td>0.069</td></tr><tr><td> $C_8$ </td><td>0.094</td><td>0.078</td><td>0.086</td><td>0.090</td><td>0.076</td><td>0.091</td><td>0.084</td><td>0.068</td><td>0.073</td><td>0.061</td><td>0.063</td><td>0.068</td><td>0.068</td></tr><tr><td> $C_9$ </td><td>0.097</td><td>0.073</td><td>0.087</td><td>0.091</td><td>0.077</td><td>0.089</td><td>0.081</td><td>0.080</td><td>0.064</td><td>0.062</td><td>0.061</td><td>0.067</td><td>0.071</td></tr><tr><td> $C_{10}$ </td><td>0.097</td><td>0.077</td><td>0.082</td><td>0.090</td><td>0.079</td><td>0.088</td><td>0.079</td><td>0.079</td><td>0.075</td><td>0.052</td><td>0.063</td><td>0.068</td><td>0.071</td></tr><tr><td> $C_{11}$ </td><td>0.097</td><td>0.073</td><td>0.086</td><td>0.090</td><td>0.078</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.074</td><td>0.063</td><td>0.054</td><td>0.069</td><td>0.069</td></tr><tr><td> $C_{12}$ </td><td>0.096</td><td>0.076</td><td>0.084</td><td>0.090</td><td>0.078</td><td>0.088</td><td>0.079</td><td>0.078</td><td>0.076</td><td>0.062</td><td>0.064</td><td>0.058</td><td>0.071</td></tr><tr><td> $C_{13}$ </td><td>0.097</td><td>0.076</td><td>0.083</td><td>0.089</td><td>0.080</td><td>0.088</td><td>0.081</td><td>0.080</td><td>0.072</td><td>0.063</td><td>0.064</td><td>0.068</td><td>0.060</td></tr></table>

Table 9  
The stable matrix of DANP when the power limit is $g  \infty ,$ i.e., $\begin{array} { r } { \operatorname* { l i m } _ { g \to \infty } \left( \pmb { W } ^ { \alpha } \right) ^ { g } . } \end{array}$

<table><tr><td>Criteria</td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td> $C_7$ </td><td> $C_8$ </td><td> $C_9$ </td><td> $C_{10}$ </td><td> $C_{11}$ </td><td> $C_{12}$ </td><td> $C_{13}$ </td></tr><tr><td> $C_1$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_2$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_3$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_4$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_5$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_6$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.063</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_7$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.063</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_8$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.076</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_9$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.076</td><td>0.061</td><td>0.063</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_{10}$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_{11}$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.063</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_{12}$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.075</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr><tr><td> $C_{13}$ </td><td>0.094</td><td>0.075</td><td>0.085</td><td>0.089</td><td>0.076</td><td>0.088</td><td>0.080</td><td>0.079</td><td>0.076</td><td>0.061</td><td>0.062</td><td>0.067</td><td>0.069</td></tr></table>

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

0 094 0 075 0 085 0 254 weight c equals 0 094 0 254 <sup>þ þ ¼</sup>0:371; …; then 0:371 0:295 0:334 1:

The in<sup>fl</sup>uence weights for the criteria used in evaluating the alternatives and improving total performance by VIKOR.

<table><tr><td>Dimensions/ criteria</td><td>Local weight</td><td>Global weight (by DANP)</td><td>Patient tracking management performance ( $A_1$ )</td><td>Asset tracking management performance ( $A_2$ )</td></tr><tr><td>Technology ( $D_1$ )</td><td>0.254</td><td>← - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td><td>0.181</td><td>0.210</td></tr><tr><td>Technology integration ( $c_1$ )</td><td>0.371</td><td>0.094 (1)</td><td>0.140</td><td>0.180</td></tr><tr><td>Technology competence ( $c_2$ )</td><td>0.295</td><td>0.075 (9)</td><td>0.280</td><td>0.260</td></tr><tr><td>Security concern ( $c_3$ )</td><td>0.334</td><td>0.085 (4)</td><td>0.140</td><td>0.200</td></tr><tr><td>Organization ( $D_2$ )</td><td>0.253</td><td>← - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td><td>0,390</td><td>0.342</td></tr><tr><td>Top management support ( $c_4$ )</td><td>0.353</td><td>0.089 (2)</td><td>0.400</td><td>0.320</td></tr><tr><td>Firm size ( $c_5$ )</td><td>0.299</td><td>0.076 (7)</td><td>0.460</td><td>0.440</td></tr><tr><td>Organizational readiness ( $c_6$ )</td><td>0.348</td><td>0.088 (3)</td><td>0.320</td><td>0.280</td></tr><tr><td>Environment ( $D_3$ )</td><td>0.234</td><td>← - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td><td>0.316</td><td>0.374</td></tr><tr><td>Competitive pressure ( $c_7$ )</td><td>0.340</td><td>0.080 (5)</td><td>0.500</td><td>0.480</td></tr><tr><td>Partner readiness ( $c_8$ )</td><td>0.337</td><td>0.079 (6)</td><td>0.260</td><td>0.300</td></tr><tr><td>Regulatory support ( $c_9$ )</td><td>0.323</td><td>0.075 (8)</td><td>0.180</td><td>0.340</td></tr><tr><td>Cost ( $D_4$ )</td><td>0.259</td><td>← - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td><td></td><td></td></tr><tr><td>Hardware cost ( $c_{10}$ )</td><td>0.235</td><td>0.061 (13)</td><td>0.340</td><td>0.260</td></tr><tr><td>Software cost ( $c_{11}$ )</td><td>0.241</td><td>0.062 (12)</td><td>0.300</td><td>0.320</td></tr><tr><td>Implement cost ( $c_{12}$ )</td><td>0.259</td><td>0.067 (11)</td><td>0.220</td><td>0.360</td></tr><tr><td>Maintenance cost ( $c_{13}$ )</td><td>0.265</td><td>0.069 (10)</td><td>0.300</td><td>0.360</td></tr><tr><td rowspan="2"> $A_k$ </td><td rowspan="2">-</td><td rowspan="2">1.00</td><td colspan="2">Total gaps</td></tr><tr><td>0.373</td><td>0.408</td></tr></table>

Notes:  
1. Example for local weights calculations from global weights:  
– The local weight for D (sum global weights from criteria $\left( c _ { 1 } , c _ { 2 } , c _ { 3 } \right) )$ was calculated as follows.  
– The local weight for $D _ { 2 }$ (sum global weights from criteria $( c _ { 4 } , c _ { 5 } , c _ { 6 } ) )$ ,was calculated as follows.

$$
\begin{array}{l} 0. 0 8 9 + 0. 0 7 6 + 0. 0 8 8 = \mathbf {0 . 2 5 3} \text { and   weight } c _ {4} \text { equals } 0. 0 8 9 \div 0. 2 5 3 \\ = 0. 3 5 3, \ldots , \text { then } 0. 3 5 3 + 0. 2 9 9 + 0. 3 4 8 = 1. \end{array}
$$

– The local weight for $D _ { 3 }$ (sum global weights from criteria $\left( c _ { 7 } , c _ { 8 } , c _ { 9 } \right) )$ , was calculated as follows.

$$
\begin{array}{l} 0. 0 8 0 + 0. 0 7 9 + 0. 0 7 5 = \mathbf {0 . 2 3 4} \text { and   weight } c _ {7} \text { equals } 0. 0 8 0 \div 0. 2 3 4 \\ = 0. 3 4 1, \ldots , \text { then } 0. 3 4 0 + 0. 3 3 7 + 0. 3 2 3 = 1. \end{array}
$$

– The local weight for $D _ { 4 }$ (sum global weights from criteria $( c _ { 1 0 } , c _ { 1 1 } , c _ { 1 2 } , c _ { 1 3 } ) ) , \mathrm { w a s }$ calculated as follows.

$$
= 0. 2 3 5, \dots ,
$$

$$
0. 2 3 5 + 0. 2 4 1 + 0. 2 5 9 + 0. 2 6 5 = 1
$$

– The local weight for overall dimensions was calculated as follows: $0 . 2 5 4 + 0 . 2 5 3 + 0 . 2 3 4 + 0 . 2 5 9 = 1 .$

2. Example for gaps performance for patient tracking management performance: – Calculating total performance by global weights:

$$
\begin{array}{l} 0. 0 9 4 \times 0. 1 4 1 + 0. 0 7 5 \times 0. 2 8 0 + 0. 0 8 5 \times 0. 1 4 0 + 0. 0 8 9 \times 0. 4 0 0 + \dots + 0. 0 6 9 \\ \times 0. 3 0 0 \\ = \mathbf {0}. \mathbf {3 7 3}. \end{array}
$$

– Calculating total performance by local weights:

$$
0. 2 5 4 \times 0. 1 8 1 + 0. 2 5 4 \times 0. 3 9 0 + 0. 2 3 4 \times 0. 3 1 6 + 0. 2 5 4 \times 0. 2 8 9 = \mathbf {0}. \mathbf {3 7 3}.
$$

– Integrating performance from criteria $\left( c _ { 1 } , c _ { 2 } , c _ { 3 } \right)$ to dimension $( D _ { 2 } )$ by local weights (C1, C2, C3)

$$
0. 3 7 1 \times 0. 1 4 0 + 0. 2 9 5 \times 0. 2 8 0 + 0. 3 3 4 \times 0. 1 4 0 = \mathbf {0 . 1 8 1}.
$$

(total gaps = 0.408). As mentioned previously, a patient-tracking management system that used RFID in the check-in process demonstrated the utility of automated outbound logistical processes. In the healthcare setting, this means getting the right patient to the right place at the right time. In addition, using RFID effectively could reduce the number of staff required to manage the patient check-in process, which results in an overall improvement in patient-tracking management performance. RFID can also be used to track healthcare assets, such as wheelchairs, infusion pumps, and crash carts. In the healthcare environment, assets (both equipment and staff) are essential to providing healthcare services to a patient.

Fourth, according to DEMATEL, we could look at the interrelationship among dimensions and criteria based on the in<sup>fl</sup>uence network relation map (INRM) to help improve each dimension and criterion (see $\mathrm { F i g } . 2 )$ . The INRM shows that the environment dimension $\left( D _ { 3 } \right)$ and the organization dimension $\left( D _ { 2 } \right)$ are the highest priority for improvement. This <sup>fi</sup>nding means that managers should <sup>fi</sup>rst improve these two dimensions because they are the most important relative to the other dimensions. Thus, the environment and the organization dimensions can be regarded as the critical dimension for evaluating and improving the RFID adoption process in the healthcare industry. In addition, with respect to the technology dimension $( D _ { 1 } ) \colon$ : technology competence $\left( C _ { 2 } \right)$ is the most in<sup>fl</sup>uential criterion and should be improved upon <sup>fi</sup>rst, followed by technology integration $\left( C _ { 1 } \right)$ and security concerns $\left( C _ { 3 } \right)$ (see Fig. 2 for more details). In addition, with respect to the organization dimension $( D _ { 2 } ) ,$ top management support $( C _ { 4 } )$ is the most in<sup>fl</sup>uential criterion and should be improved upon <sup>fi</sup>rst, followed by <sup>fi</sup>rm size $\left( C _ { 5 } \right)$ and organizational readiness. With respect to the environment dimension $\left( D _ { 3 } \right)$ , regulatory support $\left( C _ { 9 } \right)$ is the most in<sup>fl</sup>uential criterion and should be improved upon <sup>fi</sup>rst, followed by partner readiness $\left( C _ { 8 } \right)$ and competitive pressure. With respect to the cost dimension $( D _ { 4 } ) _ { \cdot }$ , hardware costs $\left( C _ { 1 0 } \right)$ is the most in<sup>fl</sup>uential criterion and should be improved upon <sup>fi</sup>rst, followed by implementation costs $( C _ { 1 2 } ) _ { \cdot }$ , software costs $\left( C _ { 1 1 } \right)$ , and maintenance costs $\left( C _ { 1 3 } \right)$ . Each of the evaluation dimensions and criteria identify the necessary behaviors for inducing RFID adoption in the healthcare industry. Therefore, managers should evaluate all of the dimensions and criteria for the RFID adoption process in accordance with Fig. 2. While this evaluation method could in principle be used by most of the healthcare industries in the world, differences do exist, and the relative importance of the 13 criteria may vary according to the particulars of each healthcare industry. Managers should compare the evaluation methods for each RFID adoption model before deciding upon the best RFID application to suit their needs.

## 5. Conclusions

The dimensions and criteria outlined in this study serve as bridging mechanisms for the evaluation of RFID adoption processes. Prior literature has identi<sup>fi</sup>ed the dimensions and criteria that in<sup>fl</sup>uence the evaluation of adopting RFID. The main contributions of this study are twofold. First, the evaluation of technology adoption is a decision-making problem that is composed of complex dependences and interactions. In this paper we used previous studies to develop a TOEC framework to evaluate RFID adoption in the healthcare industry. Second, we combine the DEMATEL, DANP and VIKOR methods to develop an evaluation method known as DDANPV to prioritize the relative in<sup>fl</sup>uence-weights of the TOEC dimensions and criteria. DDANPV could handle the complex interactions and interdependences among dimensions and criteria and produce results that allow us to build a visual cause-and-effect diagram for evaluating the various adoption processes. Additionally, we demonstrate how the results could provide guidance to managers by identifying the key criteria for decision-making and <sup>fi</sup>nding the best way to improve existing RFID adoption processes.

This DDANPV method provides a general evaluation framework for industry evaluation and adoption of RFID and a guide for future managers in the healthcare industry even if they do not completely understand how to evaluate the details of the various RFID adoption

M.-T. Lu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/K88HMUKQ/fulltext/images/6656ccb2a60dac5a7863a809af91e46e2ffc4890ea6e87c871e86863d20ad5ef.jpg)  
Fig. 2. The in<sup>fl</sup>uential network relation map (INRM) for each dimension and criterion.

models. Moreover, the INRM diagram helps decision makers understand how to improve their evaluations of RFID adoption processes. Future research could expand the DDANPV method into a general evaluation framework for industry adoption of new technologies.

There are several limitations to this study that require further examination. First, this study was conducted by surveying a relatively limited number of experts. A larger sample would have allowed for a more sophisticated analysis of evaluation procedures, which would have generalized the results of this study. Second, this study uses crisp numbers as opposed to fuzzy numbers. Future studies could incorporate fuzzy numbers to estimate the relative in<sup>fl</sup>uenceweights of each in<sup>fl</sup>uence on the evaluation method. Third, the TOEC evaluation criteria are selected from a review of prior literature on TOE and cost evaluation, which excluded some possible in<sup>fl</sup>uences on the RFID evaluation process. Future studies could use different methods, such as longitudinal studies and interviews, to identify other criteria. Finally, to provide more objective information on the applicability of the proposed TOEC evaluation model, future studies could use case studies of particular performance evaluations and thus prove the practicality of the general evaluation framework for the industry evaluation and adoption of RFID proposed in this study.

## References

[1] Z. Asif, M. Mandviwalla, Integrating the supply chain with RFID: a technical and business analysis Communications of the Association for Information Systems 15 (24) (2005) 393–427

[2] J. Ayoade, Security implications in RFID and authentication processing framework Computer and Security 25 (3) (2006) 207–212.

[3] A. Barua, P. Konana, A.B. Whinston, F. Yin, An empirical investigation of Net-enabled business value: an exploratory investigation, MIS Quarterly 28 (4) (2004) 585–620.

[4] E. Bendoly, A. Citurs, B. Konsynski, Internal infrastructural impacts of RFID perceptions and commitment: knowledge, operational procedures, and informationprocessing standards, Decision Sciences 38 (3) (2007) 423–449.

[5] B. Bilge, I. Ozkarahan, Strategic tactical and operational production-distribution models: a review, International Journal of Technology Management 28 (2) (2004) 151-171

[6] I. Brown, J. Russell, Radio frequency identi<sup>fi</sup>cation technology: an exploratory study on adoption in the South African retail sector, International Journal of Information Management 27 (4) (2007) 250–265.

[7] N.G. Carr, IT doesn't matter, Harvard Business Review 81 (5) (2003) 41–49

[8] F.H. Chen, T.S. Hsu, G.H. Tzeng, A balanced scorecard approach to establish a performance evaluation and relationship model for hot spring hotels based on a hybrid MCDM model combining DEMATEL and ANP, International Journal of Hospitality Management 30 (4) (2011) 908–932.

[9] C.C. Chao, J.M. Yang, W.Y. Jen, Determining technology trends and forecasts of RFID by historical review and bibliometric analysis from 1991 to 2005. Technovation 27 (5) (2007) 268–279.

[10] M. Freimer, P.L. Yu, Some new results on compromise solutions for group decision problems Management Science 22 (6) (1976) 688–693.

Please cite this article as: M.-T. Lu, et al., Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.06.006

[11] D.L. Goodhue, M.D. Wybo, L.J. Kirsch, The impact of data integration on the costs and bene<sup>fi</sup>ts of information systems, MIS Quarterly 16 (3) (1992) 293–311.

[12] W. Hong, K. Zhu, Migrating to internet-based e-commerce: factors affecting e-commerce adoption and migration at the firm level Information Management 43 (2) (2006) 204–221.

[13] M.T. Hoske, RFID: adoption increases despite costs, Control Engineering 51 (7) (2004) 46–47.

[14] Y.H. Hung, S.C. Chou, G.H. Tzeng, Knowledge management adoption and assessment for SMEs by a novel MCDM approach, Decision Support Systems 51 (2) (2011) 270–291.

[15] C.Y. Huang, J.Z. Shyu, G.H. Tzeng, Recon<sup>fi</sup>guring the innovation policy portfolios for Taiwan's SIP mall industry, Technovation 27 (12) (2007) 744–765.

[16] M.C. Jones, R.C. Beatty, Towards the development of measures of perceived bene<sup>fi</sup>ts and compatibility of EDI: a comparative assessment of competing <sup>fi</sup>rst order factor models, European Journal of Information Systems 7 (3) (1998) 210–220.

[17] P. Jones, C. Clarke-Hill, D. Hillier, D. Comfort, The bene<sup>fi</sup>ts, challenges and impacts of radio frequency identification (RFID) for retailers in the UK. Marketing Intelligence and Planning 23 (4) (2005) 395–402.

[18] P. Jones, C. Clarke-Hill, P. Shears, D. Hillier, D. Comfort, Radio frequency identi<sup>fi</sup>cation in retailing and privacy and public policy issues, Management Research News 27 (8/9) (2004) 46–56.

[19] B. Kaplan, The medical computing “lag”: perceptions of barriers to the application of computers to medicine, International Journal of Technology Assessment in Health Care 3 (1) (1987) 123–126.

[20] B. Kinsella, The Wal-mart factor, Industrial Engineer 35 (11) (2003) 32–36.

[21] L.S. Lee, K.D. Fiedler, J.S. Smith, Radio frequency identi<sup>fi</sup>cation (RFID) implementation in the service sector: a customer-facing diffusion model, International Journal of Production Economics 112 (2) (2008) 587–600.

[22] S.H. Lee, A.W. Ng, K. Zhang, The quest to improve Chinese healthcare: some fundamental issues, International Journal of Health Care Quality Assurance 20 (5) (2007) 416–428.

[23] J.J.H. Liou, G.H. Tzeng, H.C. Chang, Airline safety measurement using a hybrid model, Journal of Air Transport Management 13 (4) (2007) 243–249.

[24] C.H. Liu, G.H. Tzeng, M.H. Ming-Huei Lee, Improving tourism policy implementation — the use of hybrid MCDM models, Tourism Management 33 (2) (2012) 239–488.

[25] C. Loebbecke, J. Palmer, RFID in the fashion industry: Kaufhof Department Stores AG and Gerry Weber International AG, fashion manufacturer, MIS Quarterly Executive 5 (2) (2006) 15–25.

[26] E.W.T. Ngai, T.C.E. Cheng, S. Au, K. Lai, Mobile commerce integrated with RFID technology in a contained depot, Decision Support Systems 43 (1) (2007) 62–76.

[27] S. Opricovic, Multicriteria Optimization of Civil Engineering Systems, Faculty of Civil Engineering, Belgrade, 1998. , (in Serbian).

[28] S. Opricovic, G.H. Tzeng, Multicriteria planning of post-earthquake sustainable reconstruction, Computer-Aided Civil and Infrastructure Engineering 17 (3) (2002) 211–220.

[29] S. Opricovic, G.H. Tzeng, Fuzzy multicriteria model for post-earthquake land-use planning, Natural Hazards Review 4 (2) (2003) 59–64.

[30] S. Opricovic, G.H. Tzeng, Compromise solution by MCDM methods: a comparative analysis of VIKOR and TOPSIS, European Journal of Operational Research 156 (2) (2004) 445–455.

[31] S. Opricovic, G.H. Tzeng, Extended VIKOR method in comparison with outranking methods. European Journal of Operational Research 178 (2) (2007) 514–529.

[32] W. Orlikowski. CASE tools as organisational change: investigating incremental and radical changes in systems development, MIS Quarterly 17 (3) (1993) 309–340.

[33] Y.P. Ou Yang, H.M. Shieh, J.D. Leu, G.H. Tzeng, A novel hybrid MCDM model combined with DEMATEL and ANP with applications, International Journal of Operations Research 5 (3)(2008) 160-168.

[34] B. Öztaysi, S. Baysan, F. Akpinar, Radio frequency identi<sup>fi</sup>cation (RFID) in hospitality, Technovation 29 (9) (2009) 618–624.

[35] A. Oztekin, F.M. Pajouh, D. Delen, L.K. Swim, An RFID network design methodology for asset tracking in healthcare, Decision Support Systems 49 (1) (2010) 100–109.

[36] G. Premkumar, M. Roberts, Adoption of new information technologies in rural small businesses, International Journal of Management Science 27 (4) (1999) 467–484.

[37] C. Ranganathan, S. Jha, Adoption of RFID technology: an exploratory examination from supplier's perspective, Proceedings of the Eleventh American Conference on Information Systems, 11–14 August, Omaha, USA, 2005, pp. 2195–2199.

[38] P. Schmitt, F. Thiesse, E. Fleisch, Adoption and diffusion of RFID technology in the automotive industry, in: H. Österle, J. Schelp, R. Winter (Eds.), Proceedings of the 15th European Conference on Information Systems, St Gallen, Switzerland, 2007.

[39] A. Sharma, A. Citurs, Radio frequency identi<sup>fi</sup>cation (RFID) adoption drivers: a radical innovation adoption perspective, Proceedings of the Fleventh American Conference on Information Systems, 11–14 August, Omaha, USA, 2005, pp. 1213–1218.

[40] G.H. Tzeng, S.H. Tsaur, Y.D. Laiw, S. Opricovic, Multicriteria analysis of environmental quality in Taipei: public preferences and improvement strategies, Journal of Environmental Management 65 (2) (2002) 109–120.

[41] G.H. Tzeng, M.H. Teng, J.J. Chen, S. Opricovic, Multicriteria selection for a restaurant location in Taipei, International Journal of Hospitality Management 21 (2) (2002) 171-187

[42] G.H. Tzeng, C.W. Lin, S. Opricovic, Multi-criteria analysis of alternative-fuel buses for public transportation, Energy Policy 33 (11) (2005) 1373–1383.

[43] G.H. Tzeng, C.H. Chiang, C.W. Li, Evaluating intertwined effects in e-learning programs: a novel hybrid MCDM model based on factor analysis and DEMATEL, Expert Systems with Applications 32 (4) (2007) 1028–1044.

[44] P.L. Yu, A class of solutions for group decision problems, Management Science 19 (8) (1973) 936–946.

[45] Y.M. Wang, Y.S. Wang, Y.F. Yang, Understanding the determinants of RFID adoption in the manufacturing industry, Technological Forecasting and Social Change 77 (5) (2010) 803–815.

[46] J. Woods, K. Peterson, C. Hirst, Maturing open RFID applications will reshape SCM. , Available at http://www4.gartner.com/DisplayDocument?doc\_cd=112865S2003, (Accessed 12 September 2005).

[47] N.C. Wu, M.A. Nystrom, H.A. Lin, H.C. Yu, Challenges to global RFID adoption, Technovation 26 (12) (2006) 1317–1323.

[48] Q. Zhou, W. Huang, Y. Zhang, Identifying critical success factors in emergency management using a fuzzy DEMATEL method, Safety Science 49 (2) (2011) 243–252.

[49] K. Zhu, S. Dong, S.X. Xu, K.L. Kraemer, Innovation diffusion in global dimensions: determinants of post-adoption digital transformation of European companies, European Journal of Information Systems 15 (6) (2006) 601–616.

[50] K. Zhu, K.L. Kraemer, Post-adoption variations in usage and value of E-business by organizations: cross-country evidence from the retail industry, Information Systems Research 16 (1) (2005) 61–84.

[51] K. Zhu, K.L. Kraemer, S. Xu, The process of innovation assimilation by <sup>fi</sup>rms in different countries: a technology diffusion perspective on e-business, Management Science 52 (10) (2006) 1557–1576.

Ming-Tsang Lu is a Ph.D. student in the graduate institute of management science, National Chiao Tung University, Taiwan. His research interests include Multiple Criteria Decision Making, application of fuzzy theory to information systems, and information technology.

Shi-Woei Lin is a risk and decision analyst. His current research interests include the application of game theory to risk-informed regulation and the use of mathematical models to aggregate experts' uncertainty judgments. Other interests include decision biases and methods for effective risk communication, both to decision makers and to the general public.

Gwo-Hshiung Tzeng was born in 1943 in Taiwan. In 1967, he received a bachelor's degree in business management from the Tatung Institute of Technology (now Tatung University), Taiwan. In 1971, he received a master's degree in urban planning from Chung Hsing University (Now Taipei University), Taiwan. In 1977, he received a Ph.D. in management science from Osaka University, Osaka, Japan.

Gwo-Hshiung Tzeng was an Associate Professor at Chiao Tung University, Taiwan, from 1977 to 1981, a Research Associate at Argonne National Laboratory from July 1981 to January 1982, a Visiting Professor in the Department of Civil Engineering at the University of Maryland, College Park, MD, from August 1989 to August 1990, a Visiting Professor in the Department of Engineering and Economic System, Energy Modeling Forum at Stanford University from August 1997 to August 1998, a professor at Chaio Tung University from 1981 to 2003, and a Chair Professor at Chiao Tung University. He was named a National Distinguished Chair Professor (Highest Honor offered by the Ministry of Education Affairs, Taiwan) and Distinguished Research Fellow (Highest Honor Offered by NSC, Taiwan) in 2000. His current research interests include statistics, multivariate analysis, networks, routing and scheduling, multiple criteria decision making, fuzzy theory, application of hierarchical structure analysis to technology management, energy, the environment, transportation systems, transportation investment, logistics, locations, urban planning, tourism, technology management, electronic commerce, global supply chain, etc. He was awarded a Highly Cited Paper (March 13, 2009) ESI “Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS” as published in the “EUROPEAN JOURNAL OF OPERATIONAL RESEARCH” on July 16th, 156(2), 445–455, 2004, which has recently been identi<sup>fi</sup>ed by Thomson Reuters' Essential Science Indicators SM as one of the most cited papers in the <sup>fi</sup>eld of Economics and Business

He received the MCDM Edgeworth-Pareto Award from the International Society on Multiple Criteria Decision Making (June 2009), the world Pinnacle of Achievement Award in 2005, and the National Distinguished Chair Professor Award (highest honor offered) of the Ministry of Education Affairs of Taiwan; additionally, he is a three time recipient of a distinguished research award and was twice named a distinguished research fellow (highest honor offered) of the National Science Council of Taiwan. He is also a Fellow IEEE Member (since September 30, 2002). He organized a Taiwan af<sup>fi</sup>liate chapter of the International Association of Energy Economics in 1984 and he was the Chairman of the Tenth International Conference on Multiple Criteria Decision Making, July 19–24, 1992, in Taipei, the Co-Chairman of the 36th International Conference on Computers and Industrial Engineering, June 20-23 2006 Taipei Taiwan and the Chairman of the International Summer School on Multiple Criteria Decision Making 2006, July 2–14, Kainan University, Taiwan. He is a member of IEEE, IAEE, ISMCDM, World Transport, the Operations Research Society of Japan, the Society of Instrument and Control Engineers Society of Japan, the City Planning Institute of Japan, the Behavior Metric Society of Japan, and the Japan Society for Fuzzy Theory and Systems and participates in many societies of Taiwan. He is an editor-in-chief of the International Journal of Information Systems for Logistics and Management.
