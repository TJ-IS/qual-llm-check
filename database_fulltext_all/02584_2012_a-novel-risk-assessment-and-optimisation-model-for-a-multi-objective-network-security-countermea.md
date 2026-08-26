---
otero_id: 2584
otero_key: "B84F758E"
title: "A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem"
authors: "Valentina Viduto; Carsten Maple; Wei Huang; David López-Peréz"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem<sup>☆</sup>

Valentina Viduto <sup>a,</sup>⁎, Carsten Maple <sup>a</sup>, Wei Huang <sup>a</sup>, David López-Peréz <sup>b</sup>

<sup>a</sup> Institute for Research in Applicable Computing, University of Bedfordshire, Park Square, Luton, Bedfordshire, LU1 3JU, United Kingdom h Centre for Telecommunications Research, King's College London, Strand, WC2R 2LS, United Kingdom

## a r t i c l e i n f o

Article history: Received 6 June 2011 Received in revised form 4 April 2012 Accepted 5 April 2012 Available online 20 April 2012

Keywords: Financial decision support Risk assessment Countermeasure selection problem Multi-objective optimisation Tabu search

## a b s t r a c t

Budget cuts and the high demand in strengthening the security of computer systems and services constitute a challenge. Poor system knowledge and inappropriate selection of security measures may lead to unexpected <sup>fi</sup>nancial and data losses. This paper proposes a novel Risk Assessment and Optimisation Model (RAOM) to solve a security countermeasure selection problem, where variables such as <sup>fi</sup>nancial cost and risk may affect a <sup>fi</sup>nal decision. A Multi-Objective Tabu Search (MOTS) algorithm has been developed to construct an ef<sup>fi</sup>cient frontier of non-dominated solutions, which can satisfy organisational security needs in a costeffective manner.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the IT sector, most organisations implement security standards to be competitive and trustworthy parties that run highly integrated and secure businesses [20]. However, despite regulations, laws and awareness of security measures, data breaches continue to grow and evolve. According to recent surveys, around 84% of UK organisations suffered at least one data breach in 2007 [16]. When an organisation performs regular risk assessments of assets and services, the risk of experiencing a data breach may decrease. However, decisions on the type of security measures to be implemented are frequently made based on the personal experiences of decision makers, who may be unaware of speci<sup>fi</sup>c system weaknesses and new threats. In order to solve this issue, researchers have proposed a number of models relating to qualitative and quantitative risk assessment approaches, where attack trees and attack graphs are used to estimate the shortest attack paths and related security costs [2,3,15,24,36]. However, these models lack practical sense and cannot support cost-effective security decisions.

A cost-effective and coherent risk assessment should study the relationships among system vulnerabilities, threats and countermeasures. Knowing potential risks enables organisations to facilitate effective decisions on what security countermeasures should be implemented before any potential threat can successfully exploit system vulnerabilities. NIST SP800-30, ISO 27001 and ISO 17799 are common methodologies, which provide some guidelines on how risk should be assessed and how countermeasures should be selected [10,11,25]. Yet, these guidelines do not provide a speci<sup>fi</sup>c method for assessing risk related factors, such as vulnerabilities and threats, and addressing them via security countermeasures.

Security countermeasure selection problems have received a great deal of attention in the recent literature [4,8,20,21]. However, current approaches deal with this problem from very different perspectives. Gupta et al. [8] analyse the countermeasure selection in relation to residual vulnerabilities, which are represented as uncovered vulnerabilities. The idea behind their approach is to maximise the coverage of existing vulnerabilities by implementing a set of countermeasures, and thus, minimising the residual vulnerability (uncovered). Another approach is to select a portfolio of countermeasures in relation to investment costs by analysing the residual damage in the system if a system hole is not <sup>fi</sup>xed [4] and considering a set of controls in a form of disabling, enabling or patching a service or application.

Although they are very detailed in some aspects, current countermeasure selection approaches miss some other details. For example, applying a countermeasure may eliminate some risks, but generate new ones under certain circumstances. Therefore, it is not enough performing risk assessments and independently selecting security countermeasures, but it is necessary to understand the bi-directional relationship between them both. This provides a cost-effective way for organisations to be aware of possible data losses and ensure that adequate security countermeasures are in place.

Due to the lack of studies on this topic, this paper investigates risk assessment methodologies and provides a tool to select security countermeasures taking <sup>fi</sup>nancial costs and residual risks into account. More speci<sup>fi</sup>cally, based on NIST SP800-30 guidelines, we propose a Risk Assessment and Optimisation Model (RAOM) to satisfy organisational security needs in a cost-effective manner, systematically present our security countermeasure selection problem and formulate it as a multi-objective optimisation problem, where variables such as <sup>fi</sup>nancial cost and risk may affect the <sup>fi</sup>nal solution. We also propose a tailored multi-objective Tabu Search (MOTS)- based heuristic approach to solve the proposed multi-objective optimisation problem and asses the qualities of its solutions with respect to optimal ones. Decisions on what security measures should be implemented are time sensitive and sometimes require instantaneous actions, because identi<sup>fi</sup>ed threats can take advantage over existing vulnerabilities and have adverse effect on the whole networked system [22]. For this reason, computationally ef<sup>fi</sup>cient, in terms of speed, methods can serve as an accompanying tool during decision making process. It is worth noting, that in dynamic network environments risks identi<sup>fi</sup>ed today, may not be the same tomorrow, hence the risk assessment should be undertaken on a regular basis to maximally protect the network from threats. RAOM facilitates time sensitive, strategic and cost effective decision making, and increases its ability to ef<sup>fi</sup>ciently respond to identi<sup>fi</sup>ed threats.

## 2. Risk Assessment and Optimisation Model (RAOM)

In this section we present our risk assessment model, compare it to NIST SP800-30 framework and formally de<sup>fi</sup>ne our multi-objective optimisation problem. RAOM consists of two processes, risk assessment and optimisation routine. The purpose of the proposed RAOM is to provide the foundation of an effective risk assessment procedure, containing practical methods necessary for assessing risks and cost-effectively minimising them through security countermeasures.

The RAOM divides risk assessment process into eleven steps, listed as follows (Fig. 1, PART A):

1. Identify organisations' essential functions—the goal of this step is to identify the functions, which cannot be interrupted under any circumstances.

2. Identify essential systems—the goal of this step is to identify essential systems that should be protected.

3. Assess systems for vulnerabilities—the goal of this step is to perform a vulnerability assessment on these essential systems.

4. Analyse vulnerabilities—the goal of this step is to list identi<sup>fi</sup>ed vulnerabilities.

5. Analyse vulnerability properties—the goal of this step is to analyse vulnerability's properties and identify potential threats. Development of attack scenarios using visualisation techniques is a useful technique to be applied at this step.

6. Vulnerability to attack exist—the goal of this step is to de<sup>fi</sup>ne if there is a chance for an attack to exist.

7. Impact analysis—the goal of this step is to analyse the real impact on CIA a vulnerability introduce.

8. Threat-vulnerability analysis—vulnerabilities can only be translated into risk if there is a threat able to exploit them.

![](/api/attachments/B84F758E/fulltext/images/648e294a71f97934163031d76f7f7da415a80faab53173f71a6fc83758eb5e10.jpg)  
Fig. 1. Risk assessment and optimisation model (RAOM) <sup>fl</sup>ow chart.

Table 1

9. Likelihood determination—the goal of this step is to determine the likelihood that a potential vulnerability will be exploited.

10. Risk level determination—the goal of this step is to estimate the initial risk before any countermeasures are implemented. Decision makers should be aware of this value in order to select a set of countermeasures which would reduce it.

11. Security control recommendation—the goal of this step is to propose a list of generic countermeasures that are able to provide a cost-effective solution to the countermeasure selection problem.

Part B introduces an optimisation routine, which is used to <sup>fi</sup>nd optimal solutions in a cost effective manner.

RAOM steps 1–6 can be treated as qualitative assessment stages, where information is gathered by running questionnaires, workshops, or just consulting with security specialist. For this assessment method we propose a use of visualisation techniques, which can be used to build attack scenarios and identify potential threat-vulnerability sources [17,34,35]. Vulnerabilities, technical or nontechnical, can be identi<sup>fi</sup>ed in four ways: using automated vulnerability scanning tools, performing penetration tests on systems, using vulnerability modelling techniques and assessing previous risk assessment IT documentation. Once the vulnerabilities are characterised, it is important to identify the threats that can exploit them. Vulnerabilities can only be translated into risk if there is a threat able to exploit them. If we can estimate vulnerabilities and threats, we can derive the level of risk in an organisation. Our aim is then to reduce this level of risk by selecting the appropriate set of countermeasures in a cost-effective manner.

## 2.1. Definition of vulnerabilities and impact analysis

Vulnerabilities are the weaknesses or <sup>fl</sup>aws in system security procedures, design or internal controls that can be triggered or intentionally exploited, resulting in a security breach or a violation of security policy.

The National Vulnerability Database (NVD) provides a source of technical vulnerabilities [23] with the full overview of the vulnerabilities, their impacts and corresponding CVE (Common Vulnerabilities and Exposures) numbers. The severity of every vulnerability in the NVD is calculated using CVSS (Common Vulnerability Scoring System) based scoring system [18]. CVSS provides standardised vulnerability scores based on intrinsic and fundamental characteristics of a vulnerability. Other scoring systems also exists, such as provided by CERT Coordination Center(CERT/CC), Microsoft's proprietary scoring system, however they differ by what they measure [19,31]. The NVD is the only of<sup>fi</sup>cial and “practically sound” source that provides impact levels on Con<sup>fi</sup>dentiality, Integrity and Availability (CIA) [23]. According to the NVD provided CVSS score system, there are three impact levels: partial (P), complete (C) and none (N) [18].

The highest impact corresponds to the CCC combination, standing for complete impact on con<sup>fi</sup>dentiality, integrity and availability. For every CVE numbered vulnerability, the impact can be retrieved from [23]. Table 1 provides an example of potential impact combinations on CIA of some real case vulnerabilities taken for demonstration purposes only.

In order to measure risk, at the further RAOM stages, in relation to CIA impact across all identi<sup>fi</sup>ed vulnerabilities and threats, we group different PCN combinations and adopt an impact scale [10,50,100] taken from [25].

$$
I _ {i} = \left\{ \begin{array}{l l} \text { Low } (1 0) & \text { when   } \text { CIAI } \{\text { NNP }, \text { NPN }, \text { PNN } \}; \\ \text { Medium } (5 0) & \text { when   } \text { CIAI } \{\text { PPN }, \text { PNP }, \text { NPP }, \text { PPP }, \text { NNC }, \text { NCN }, \text { CNN } \}; \\ \text { High } (1 0 0) & \text { when   } \text { CIAI } \{\text { PPC }, \text { PCP }, \text { CPP }, \text { NCC }, \text { CNC }, \text { CCN }, \text { PCC }, \\ & \text { CPC }, \text { CCP }, \text { CCC } \}; \end{array} \right.
$$

Vulnerability and corresponding CVE, impact information.

<table><tr><td>Representation (Repr.)</td><td>Vulnerability</td><td>CVE number</td><td>Impact on CIA</td></tr><tr><td> $V_1$ </td><td>Default, missing or blank local user password</td><td>1999-0504</td><td>PPP</td></tr><tr><td> $V_2$ </td><td>VirusScan NT 4.0.2 does not modify scan.dat file</td><td>1999-1195</td><td>PPP</td></tr><tr><td> $V_3$ </td><td>Administrator password disclosure</td><td>2006-0561</td><td>CCC</td></tr><tr><td> $V_4$ </td><td>IE version 5.01.5.5 and 6.0</td><td>2003-0344</td><td>PPP</td></tr><tr><td> $V_5$ </td><td>SSH v1 in OpenSSH has various weaknesses</td><td>2001-0572</td><td>PPP</td></tr><tr><td> $V_6$ </td><td>Cisco CSS11000 malformed UDP packet vulnerability</td><td>2004-0352</td><td>NNP</td></tr><tr><td> $V_7$ </td><td>mysqld in MySQL 3.21 stores passwords in log file</td><td>1999-1188</td><td>PPP</td></tr><tr><td> $V_8$ </td><td>MySQL 3.21 allows mysql users to gain root privileges</td><td>2003-0150</td><td>CCC</td></tr><tr><td> $V_9$ </td><td>Execute arbitrary commands in wu-ftpd 2.6.1</td><td>2001-0550</td><td>PPP</td></tr><tr><td> $V_{10}$ </td><td>wu-ftpd 2.6.1 with the restricted-gid option enabled allows local users to bypass access restrictions</td><td>2004-0148</td><td>CCC</td></tr></table>

Let each vulnerability be represented as a single bit in the vulnerability vector:

$$
\vec {V} = \{V _ {i} \} = \{1, 0 \} \forall i, i = 1, 2, \dots , n.\tag{1}
$$

where $V _ { i }$ represents an individual vulnerability. The value 1 indicates the presence of this vulnerability in the information systems, otherwise 0.

## 2.2. Threat analysis

The next step in the model is to perform a threat analysis, which consists of identifying potential threat sources and actions that may exploit system vulnerabilities. An attack can be de<sup>fi</sup>ned as the action, in which a threat exploits a vulnerability that may create some risk in the system. Information about threats can be gathered from the organisation's historical database about the attacks recorded in system log <sup>fi</sup>les or by using threat modelling techniques, which can predict threats not known to the organisation. For example, modelling techniques, such as attack graphs, attack trees or an onion skin model [17,34] have been used to predict new threats in pre-de<sup>fi</sup>ned scenarios.

Let each threat be represented as a single bit in the threat vector:

$$
\vec {T} = \left\{T _ {j} \right\} = \{0, 1 \} \forall j, \quad j = 1, 2, \dots , m.\tag{2}
$$

where $T _ { j }$ represents an individual threat. The value 1 indicates the presence of this threat in the information systems and otherwise 0.

Thereafter, based on data breaches reports, logged attack attempts and self-expertise, we can match threats to vulnerabilities (Table 2) and estimate the likelihood $L _ { j i }$ of a threat $T _ { j }$ acting over a vulnerability $V _ { i } ,$ as shown in Table 3, i.e., $\overset { \cdot } { L } _ { j i } = \langle T _ { j } , V _ { i } , \rangle \ [ 5 , 3 2 , 3 3 ]$

This likelihood $L _ { j i }$ can adopt three values: 0.1, 0.5 and 1, where the value 0.1 represents low likelihood of threat T exploiting vulnerability V , 0.5—medium likelihood and 1—high likelihood [25]. If a threat $T _ { j }$ has no effect on a vulnerability $V _ { i } ,$ there is no risk and thus $L _ { j i } = 0 .$ The value $L _ { j i }$ should be obtained by analysing historical data, log <sup>fi</sup>les, by building various attack scenarios, where a threat can act over a particular vulnerability with some probability. It has been noted from the literature that insider threats are the most common threats to exploit vulnerabilities due to some level of delegated privileges $\left[ 1 6 , 3 4 , 3 5 \right]$ . For example, a disclosure of administrators password $V _ { 3 }$ has high likelihood to be exploited by performing a social engineering attack $T _ { 3 } ,$ or medium likelihood by performing a dictionary/brute force attacks $T _ { 1 4 } .$ However, it should be noted that determination of likelihood values may be subjective and strongly dependent upon the organisations infrastructure and type of business.

Likelihood value $L _ { j i \cdot }$  
Table 2  
Matching threats and vulnerabilities.

<table><tr><td>Threat sources</td><td>Threats/actions</td><td>Repr.</td><td>Matched vulnerability</td></tr><tr><td rowspan="2">Incompetent user</td><td>Unauthorised user gets access to resources</td><td> $T_1$ </td><td> $V_1,V_3, V_7,V_8,V_9,V_{10}$ </td></tr><tr><td>Physical attack</td><td> $T_2$ </td><td> $V_1,V_3, V_7,V_8,V_{10}$ </td></tr><tr><td rowspan="3">Hacker</td><td>Social engineering</td><td> $T_3$ </td><td> $V_3,V_8,V_9$ </td></tr><tr><td>Tamper the protection relevant mechanisms</td><td> $T_4$ </td><td> $V_1,V_2, V_5,V_6,V_{10}$ </td></tr><tr><td>Reckless network administration</td><td> $T_5$ </td><td> $V_1,V_2,V_3,V_4,V_5,V_9,V_{10}$ </td></tr><tr><td rowspan="4">Tactical attack</td><td>Improper management</td><td> $T_6$ </td><td> $V_1,V_3, V_4,V_7,V_8$ </td></tr><tr><td>Viruses, Trojans, Worms</td><td> $T_7$ </td><td> $V_2,V_4, V_6$ </td></tr><tr><td>Architecture, design and implementation flaws</td><td> $T_8$ </td><td> $V_5,V_6, V_9,V_{10}$ </td></tr><tr><td>DoS attack</td><td> $T_9$ </td><td> $V_4,V_6, V_7$ </td></tr><tr><td rowspan="2">Industrial Espionage</td><td>BoF attack</td><td> $T_{10}$ </td><td> $V_4,V_8, V_9,V_{10}$ </td></tr><tr><td>No Audits</td><td> $T_{11}$ </td><td> $V_1,V_3, V_4,V_6,V_8,V_9,V_{10}$ </td></tr><tr><td rowspan="4">Service administrator</td><td>Elevation of privileges</td><td> $T_{12}$ </td><td> $V_1,V_3, V_5,V_7,V_8$ </td></tr><tr><td>Password compromise through plain text communication</td><td> $T_{13}$ </td><td> $V_3,V_4, V_5$ </td></tr><tr><td>Dictionary/Brute Force attack</td><td> $T_{14}$ </td><td> $V_1,V_3, V_5,V_7,V_9$ </td></tr><tr><td>Arbitrary code execution</td><td> $T_{15}$ </td><td> $V_1,V_4, V_5,V_9$ </td></tr></table>

## 2.3. Risk level analysis

$$
\mathrm{TIR} = \sum_ {j = 1} ^ {m} \sum_ {i = 1} ^ {n} L _ {j i} \cdot I _ {i} \cdot V _ {i},
$$

De<sup>fi</sup>nition 1. Total Initial Risk (TIR) is de<sup>fi</sup>ned as the sum of initial risks in an organisation, when no security countermeasure has been applied, and can be computed as follows:

3

<table><tr><td></td><td>V1</td><td>V2</td><td>V3</td><td>V4</td><td>V5</td><td>V6</td><td>V7</td><td>V8</td><td>V9</td><td>V10</td></tr><tr><td>T1</td><td>0.1</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0.1</td><td>0.1</td><td>0.5</td><td>0.1</td></tr><tr><td>T2</td><td>1</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0.1</td><td>0.1</td><td>0</td><td>0.1</td></tr><tr><td>T3</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.1</td><td>0.1</td><td>0</td></tr><tr><td>T4</td><td>0.1</td><td>0.1</td><td>0</td><td>0</td><td>0.5</td><td>0.1</td><td>0</td><td>0</td><td>0</td><td>0.5</td></tr><tr><td>T5</td><td>0.5</td><td>0.5</td><td>1</td><td>0.5</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0.1</td><td>0.1</td></tr><tr><td>T6</td><td>1</td><td>0</td><td>0.5</td><td>0.1</td><td>0</td><td>0</td><td>0.5</td><td>0.1</td><td>0</td><td>0</td></tr><tr><td>T7</td><td>0</td><td>1</td><td>0</td><td>0.5</td><td>0</td><td>0.1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>1</td></tr><tr><td>T9</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0.5</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T10</td><td>0</td><td>0</td><td>0</td><td>0.1</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0.1</td><td>0.5</td></tr><tr><td>T11</td><td>0.5</td><td>0</td><td>0.5</td><td>0.1</td><td>0</td><td>0.1</td><td>0</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>T12</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0.1</td><td>0</td><td>0.5</td><td>1</td><td>0</td><td>0</td></tr><tr><td>T13</td><td>0</td><td>0</td><td>0.5</td><td>0.1</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T14</td><td>1</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0</td><td>1</td><td>0</td><td>0.5</td><td>0</td></tr><tr><td>T15</td><td>0.1</td><td>0</td><td>0</td><td>0.5</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

Table 4  
A generic list of security countermeasures for identi<sup>fi</sup>ed vulnerabilities and threats.

<table><tr><td>Category</td><td>Type</td><td>Countermeasure</td><td>Representation</td></tr><tr><td rowspan="12">Technical</td><td rowspan="4">Support</td><td>Identification</td><td> $S_1$ </td></tr><tr><td>Cryptographic key management</td><td> $S_2$ </td></tr><tr><td>Security administration</td><td> $S_3$ </td></tr><tr><td>System protection</td><td> $S_4$ </td></tr><tr><td rowspan="7">Prevent</td><td>Authentication</td><td> $S_5$ </td></tr><tr><td>Authorisation</td><td> $S_6$ </td></tr><tr><td>Access control enforcement</td><td> $S_7$ </td></tr><tr><td>Non-repudiation</td><td> $S_8$ </td></tr><tr><td>Protected communication</td><td> $S_9$ </td></tr><tr><td>Transaction privacy</td><td> $S_{10}$ </td></tr><tr><td>Audit</td><td> $S_{11}$ </td></tr><tr><td>Detect and recover</td><td>Intrusion detection and Containment</td><td> $S_{12}$ </td></tr><tr><td rowspan="10">Management</td><td rowspan="3"></td><td>Virus detection and eradication</td><td> $S_{13}$ </td></tr><tr><td>Assign security responsibilities</td><td> $S_{14}$ </td></tr><tr><td>Implement separation of duties, least privilege</td><td> $S_{15}$ </td></tr><tr><td rowspan="2">Preventive</td><td>and PC access registration and termination</td><td></td></tr><tr><td>Conduct security awareness and technical training and PC access registration and termination</td><td> $S_{16}$ </td></tr><tr><td rowspan="2">Detection</td><td>Conduct periodic review of security controls</td><td> $S_{17}$ </td></tr><tr><td>Periodic system audits</td><td> $S_{18}$ </td></tr><tr><td rowspan="3">Recovery</td><td>Provide continuity of support and test, maintain it</td><td> $S_{19}$ </td></tr><tr><td>Control data media access and disposal</td><td> $S_{20}$ </td></tr><tr><td>Control software viruses</td><td> $S_{21}$ </td></tr><tr><td rowspan="3">Operational</td><td rowspan="2">Preventive</td><td>Safeguard computing facility (e.g. biometric access control)</td><td> $S_{22}$ </td></tr><tr><td>Protect laptops, personal computers, workstations</td><td> $S_{23}$ </td></tr><tr><td>Detection</td><td>Provide physical security (e.g. motion detectors)</td><td> $S_{24}$ </td></tr></table>

where $\mathrm { T I R } \in \mathbb { R } ^ { + }$ , and $L _ { j i } , I _ { i } , V _ { i }$ are derived during the risk assessment analysis.

Once TIR is known, the organisation becomes aware of how critical identi<sup>fi</sup>ed vulnerabilities are for running a successful business. Thus, the next step is to identify potential security countermeasures that can be applied to reduce TIR.

## 2.4. Control recommendation

In general, security countermeasures can be categorised as technical, management and operational based on the function they provide. We propose a list of generic countermeasures, which we use within the RAOM model (Table 4) to demonstrate how these countermeasures can be selected. Similar classi<sup>fi</sup>cation of countermeasures can be found in the NIST report [25].

Let each countermeasure be represented as a single bit in the countermeasure vector:

$$
\vec {S} = \{S _ {l} \} = \{0, 1 \} \forall l, l = 1, 2,..., k.\tag{4}
$$

where $S _ { l }$ represents an individual countermeasure. The value 1 indicates that this countermeasure is applied to the information system and otherwise 0.

The selection of countermeasures is performed by <sup>fi</sup>rst matching them to identi<sup>fi</sup>ed vulnerabilities as shown in Table 5. Previously countermeasure-to-vulnerability matching idea has been proposed in ref. [1] and later demonstrated in ref. [8], where a matching value is assigned, if a countermeasure can directly address or indirectly address one or more vulnerabilities, indirectly create some vulnerability or directly create some vulnerability. We de<sup>fi</sup>ne matching as $z _ { l i }$ to represent such a match. Each countermeasure–vulnerability combination $z _ { l i }$ may have one of the following <sup>fi</sup>ve possible consequences:

$$
z _ {l i} = \left\{ \begin{array}{l l} 1 & \text { if } S _ {l} \text { directly   addresses } V _ {i}; \\ 0. 5 & \text { if } S _ {l} \text { indirectly   addresses } V _ {i}; \\ 0 & \text { if } S _ {l} \text { and } V _ {i} \text { do   not   match }; \\ - 0. 5 & \text { if } S _ {l} \text { indirectly   creates } V _ {i}; \\ - 1 & \text { if } S _ {l} \text { directly   creates } V _ {i}. \end{array} \right.
$$

In general, $z _ { l i }$ values should be assigned based on the characteristics of a countermeasure and its match with the vulnerability.

Matching countermeasures to vulnerabilities $z _ { l i \cdot }$

<table><tr><td>Vulnerability/countermeasure</td><td> $V_1$ </td><td> $V_2$ </td><td> $V_3$ </td><td> $V_4$ </td><td> $V_5$ </td><td> $V_6$ </td><td> $V_7$ </td><td> $V_8$ </td><td> $V_9$ </td><td> $V_{10}$ </td></tr><tr><td> $S_1$ </td><td>1</td><td>0</td><td>-0.5</td><td>0</td><td>0.5</td><td>0</td><td>-0.5</td><td>-0.5</td><td>0</td><td>-0.5</td></tr><tr><td> $S_2$ </td><td>0</td><td>0</td><td>-0.5</td><td>0</td><td>0.5</td><td>-0.5</td><td>-0.5</td><td>0</td><td>0.5</td><td>0.5</td></tr><tr><td> $S_3$ </td><td>1</td><td>0.5</td><td>-0.5</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.5</td><td>0.5</td></tr><tr><td> $S_4$ </td><td>-0.5</td><td>0</td><td>-1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.5</td><td>0.5</td></tr><tr><td> $S_5$ </td><td>0.5</td><td>0</td><td>-1</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0.5</td><td>-0.5</td><td>-0.5</td></tr><tr><td> $S_6$ </td><td>0.5</td><td>0</td><td>-0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td> $S_7$ </td><td>0</td><td>0.5</td><td>-0.5</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $S_8$ </td><td>0</td><td>0</td><td>-0.5</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $S_9$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.5</td><td>0.5</td><td>-0.5</td><td>0.5</td></tr><tr><td> $S_{10}$ </td><td>0</td><td>0</td><td>-1</td><td>0</td><td>1</td><td>0</td><td>0.5</td><td>0.5</td><td>0</td><td>-0.5</td></tr><tr><td> $S_{11}$ </td><td>0.5</td><td>1</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1</td></tr><tr><td> $S_{12}$ </td><td>0.5</td><td>0.5</td><td>-0.5</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0.5</td><td>1</td><td>0.5</td></tr><tr><td> $S_{13}$ </td><td>0</td><td>1</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td> $S_{14}$ </td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td> $S_{15}$ </td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td></tr><tr><td> $S_{16}$ </td><td>1</td><td>0.5</td><td>1</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $S_{17}$ </td><td>0.5</td><td>0.5</td><td>-0.5</td><td>0.5</td><td>1</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1</td><td>1</td></tr><tr><td> $S_{18}$ </td><td>1</td><td>1</td><td>1</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td> $S_{19}$ </td><td>0.5</td><td>0.5</td><td>-0.5</td><td>0</td><td>-0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td> $S_{20}$ </td><td>-0.5</td><td>0</td><td>-0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $S_{21}$ </td><td>0</td><td>1</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0</td></tr><tr><td> $S_{22}$ </td><td>1</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $S_{23}$ </td><td>0</td><td>-0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $S_{24}$ </td><td>-0.5</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

For example, the “Security administration” $\left( S _ { 3 } \right)$ countermeasure can accidentally, or, indirectly create a vulnerability “Administrator password disclosure ” $\left( V _ { 3 } \right)$ (e.g., system administrator will have a password written down on the piece of paper, left on a desk. However, $S _ { 3 }$ can directly address vulnerabilities $V _ { 1 } , V _ { 5 } , V _ { 6 } , V _ { 7 } , V _ { 8 }$ if implemented. The same vulnerability $V _ { 3 }$ could be also directly addressed by the “Management“ category countermeasures $S _ { 1 6 } S _ { 1 8 } ,$ as these measures increase security awareness of security precautions. Furthermore, $z _ { l i }$ values can be derived through questionnaires and workshops with people from various parts of the organisation such as information security experts, information technology managers and staff, business asset owners and users, and senior managers. In this case, z values (shown in Table 5) were mainly obtained from NIST vulnerability database [23]. However, sources such as refs. [29,30] were also used for some countermeasure categories to deliver concise data about which vulnerabilities can be directly or indirectly created, or addressed, while a countermeasure is implemented.

Each of the listed countermeasures has an associated cost $C _ { l } .$ In this study, we have identi<sup>fi</sup>ed four different costs of implementing a security countermeasure–purchase cost (monetary), operational cost (monetary), training cost (monetary) and man power (monetary). Purchase cost includes all the costs associated with purchasing a certain countermeasure from a vendor. All the additional subcharges, if there are some, are also summed up to the total purchase cost value.

Operational cost can be de<sup>fi</sup>ned as expenses which are related to the operation of a certain countermeasure: this can be <sup>fi</sup>xed or variable costs, such as delivery costs, rent payment or electricity charges. Training cost can be applied for such cases when an additional training is required for an IT staff to increase the professional expertise and maintain security awareness. Man power is calculated in persons per hour required to implement a new countermeasure or re-con<sup>fi</sup>gure the existing one. It is important to note that we are not considering permanent position wages, instead we estimate a cost associated with the accomplishment of particular tasks assigned to a person. For example, if we consider a \$50/h payment rate for a technician to patch systems, we calculate the cost associated as the payment rate multiplied by the time required to complete the task.

The purchase cost values have been taken from online security technology manufacturers, e.g., [9,27,28]. In Table 6, operational costs were only theoretical, as they are subject to variable tariffs on postage, electricity, cooling, etc. The training cost should be assigned only to those countermeasures where an extra knowledge is required for control implementation.

The total cost for a particular security countermeasure $S _ { l }$ is the sum of the four presented sub-costs de<sup>fi</sup>ned in monetary units, i.e.,

$$
C _ {l} = \sum_ {n = 1} ^ {4} C _ {n}\tag{5}
$$

In practice, organisations may face different types of costs related to a particular countermeasure, however, this fact does not change the meaning of a total cost and applicability of the model to real cases.

Table 6  
Estimated cost value in monetary units.

<table><tr><td></td><td>Countermeasure example</td><td>Operational cost ($)</td><td>Man power(e.g. if 50$/h)</td><td>Purchase cost ($)</td><td>Training cost ($)</td><td>Total cost x  $10^{2}$ ( $)</td></tr><tr><td>S1</td><td>Maintain use of passwords to identify users</td><td>0</td><td>0</td><td>0</td><td>2500</td><td>25</td></tr><tr><td>S2</td><td>IBM Tivolikey lifecycle manager(Full version + includes support) [9]</td><td>0</td><td>0</td><td>3180</td><td>0</td><td>31.80</td></tr><tr><td>S3</td><td>System administrator</td><td>200</td><td>1000</td><td>0</td><td>0</td><td>12</td></tr><tr><td>S4</td><td>Turn on the “System Protection” under OS settings</td><td>0</td><td>500</td><td>0</td><td>0</td><td>5</td></tr><tr><td>S5</td><td>Softerra LDAP administratorsingle license [27]</td><td>100</td><td>1500</td><td>250</td><td>0</td><td>18.5</td></tr><tr><td>S6</td><td>run &quot;bos setauth&quot; command</td><td>60</td><td>150</td><td>0</td><td>0</td><td>2.1</td></tr><tr><td>S7</td><td>Configure MAC, DAC</td><td>100</td><td>300</td><td>0</td><td>0</td><td>4</td></tr><tr><td>S8</td><td>Use of digital certificates [28]</td><td>400</td><td>1000</td><td>500</td><td>0</td><td>19</td></tr><tr><td>S9</td><td>Configure VPN</td><td>500</td><td>1000</td><td>0</td><td>2000</td><td>35</td></tr><tr><td>S10</td><td>Enable SSHv2</td><td>100</td><td>50</td><td>0</td><td>0</td><td>1.5</td></tr><tr><td>S11</td><td>E-Z Audit license</td><td>100</td><td>0</td><td>155</td><td>300</td><td>5.5</td></tr><tr><td>S12</td><td>Netgear firewall</td><td>1000</td><td>2500</td><td>1100</td><td>0</td><td>46</td></tr><tr><td>S13</td><td>Symantec Antivirus</td><td>60</td><td>500</td><td>200</td><td>0</td><td>7.6</td></tr><tr><td>S14</td><td>Assign security responsibilities</td><td>0</td><td>2500</td><td>0</td><td>0</td><td>25</td></tr><tr><td>S15</td><td>Separation of duties</td><td>0</td><td>1000</td><td>0</td><td>0</td><td>10</td></tr><tr><td>S16</td><td>Run a training</td><td>300</td><td>0</td><td>0</td><td>2000</td><td>23</td></tr><tr><td>S17</td><td>Penetration testing</td><td>1000</td><td>5000</td><td>0</td><td>0</td><td>60</td></tr><tr><td>S18</td><td>Generate periodic audit reports</td><td>150</td><td>1000</td><td>0</td><td>0</td><td>11.5</td></tr><tr><td>S19</td><td>Hire a consultant</td><td>0</td><td>0</td><td>2500</td><td>0</td><td>25</td></tr><tr><td>S20</td><td>Develop a data disposal policy</td><td>500</td><td>1500</td><td>0</td><td>2000</td><td>40</td></tr><tr><td>S21</td><td>Patching</td><td>500</td><td>200</td><td>0</td><td>0</td><td>7</td></tr><tr><td>S22</td><td>Retina scanner</td><td>100</td><td>1000</td><td>1500</td><td>0</td><td>26</td></tr><tr><td>S23</td><td>Secure locks</td><td>500</td><td>1000</td><td>500</td><td>0</td><td>20</td></tr><tr><td>S24</td><td>CCTV installation</td><td>1000</td><td>300</td><td>3000</td><td>0</td><td>43</td></tr></table>

2.5. Risk Assessment and Optimisation Model (RAOM) as an extension of the NIST SP800-30

The standard NIST SP800-30 approach divides the risk assessment process into nine steps listed as follows [25]:

1. System characterisation—the goal of this step is to establish the scope of the risk assessment and identify the boundaries of the IT system;

2. Threat identi<sup>fi</sup>cation—the goal of this step is to list potential threats along with the motivations;

3. Vulnerability identi<sup>fi</sup>cation—the goal of this step is to develop a list of system vulnerabilities that can be exploited by threats;

4. Control analysis—the goal of this step is to analyse the implemented controls or planned to be implemented;

5. Likelihood determination—the goal of this step is to determine the likelihood. NIST express the likelihood using a scale of high, medium and low represented as [1, 0.5, 0.1] respectively;

6. Impact analysis—the goal of this step is to prioritise the impact levels (high, medium, low on a scale [100, 50, 10] respectively) associated with system mission, data criticality and sensitivity.

7. Risk determination—the goal of this step is to assess the level of risk to the IT system. Risk is derived by constructing a risk level matrix, in which ratings assigned for likelihood and impact are multiplied. The risk as a result is scaled as follows: high (>50 to 100), medium (>10 to 50), low (1 to 10);

8. Control recommendation—the goal of this step is to recommend procedural or technical controls;

9. Results documentation—once the assessment has been completed, the results should be documented in an of<sup>fi</sup>cial report to help deci sion makers to reach decision on policy, budget, system operation and management changes.

The main quantitative improvements proposed in this paper were performed within NIST SP800-30 steps 6 (Impact Analysis) and 7 (Risk Determination). In terms of qualitative assessment method (covered in NIST steps 2, 3, 4), we propose the use of new modelling techniques within RAOM (Fig. 1 steps 1 to 6). More information how these techniques are applied can be found in [17, 34, 35].

Table 7  
Comparison between NIST and RAOM.

<table><tr><td>Task</td><td>NIST</td><td>RAOM</td><td>Explanation</td></tr><tr><td>System Characterisation</td><td>Steps 1, 4</td><td>Steps 1–2</td><td>Both methods use the same idea how to approach this task.</td></tr><tr><td>Identification</td><td>Steps 2–3</td><td>Steps 3–6</td><td>RAOM propose a use of visualisation techniques identify more threats, vulnerabilities.</td></tr><tr><td>Likelihood Determination</td><td>Step 5</td><td>Steps 8, 9</td><td>As was proposed by NIST likelihood can be estimated in scale low, medium, high. RAOM applies it as well.</td></tr><tr><td>Impact Analysis</td><td>Step 6</td><td>Step 7</td><td>NIST analyse impact as cost of loss assets, reputation, RAOM takes real impact on CIA.</td></tr><tr><td>Risk Determination</td><td>Step 7</td><td>Step 10</td><td>NIST scale risk as high, medium, low. RAOM calculates total initial risk which later should be reduced by selecting appropriate set of countermeasures.</td></tr><tr><td>Control Recommendation</td><td>Steps 8, 9</td><td>Step 11</td><td>NIST propose a list of controls, RAOM generates a list of generic controls.</td></tr><tr><td>Control Selection</td><td>n/a</td><td>Part B</td><td>NIST does not guide how controls can be selected, RAOM proposed a multi-objective function</td></tr><tr><td>Optimisation</td><td>n/a</td><td>Part B</td><td>In addition to multi-objective function, RAOM propose an optimisation routine to search for trade-offs between cost and risk objectives.</td></tr></table>

The quantitative changes that RAOM brings towards better risk analysis can be summarised as follows:

• Impact Analysis (Sec.1 RAOM step 7)—based on the identi<sup>fi</sup>ed vulnerabilities and overall qualitative system analysis performed in RAOM steps 1–6, the impact is estimated considering vulnerability's i impact on CIA (con<sup>fi</sup>dentiality, integrity, availability). Based on the C, N, P (Complete, Non, Partial) combinations assigned to vulnerabilities by the NVD, we perform a grouping and assign a scale of [10, 50, 100] to every group of impacts, as proposed by NIST.

• Risk Analysis (Sec.3 RAOM step 10)—instead of just scaling risk (NIST SP800-30 step 7), RAOM propose a way how to estimate the total initial risk TIR considering ratings assigned for likelihood, impact and vulnerabilities (Eq. (3)).

Table 7 summarises the main differences between NIST guidelines and RAOM.

## 3. Problem formulation

We consider two objectives in this study: the total investment cost TC and the risk R. For the $n { = } 1 0$ vulnerabilities listed in Table 1 we have suggested $k = 2 4$ generic security countermeasures (Table 4). As a result, the $2 ^ { 2 4 }$ security countermeasures choices available prove the problem to be hard to solve manually or relying on selfexpertise. Furthermore, the time to <sup>fi</sup>nd a good solution increases when the size of the problem increases, i.e., if the number of countermeasures k increases, the time to <sup>fi</sup>nd the optimal solution also increases.

## De<sup>fi</sup>nition 2. Total investment cost

Given a set of k countermeasures, each having a cost $C _ { l } , \ 1 { \le } l { \le } k$ and having a vector of $\begin{array} { r } { \vec { S } = ( S _ { l } ) , S _ { l } \in \{ 0 , 1 \} \forall l , } \end{array}$ , 1 l k, the total investment cost TC is de<sup>fi</sup>ned as:

$$
T C = \left\{\sum_ {l = 1} ^ {k} C _ {l} S _ {l}: C _ {l} > 0, \forall l (C _ {l}) \right\}\tag{6}
$$

$S _ { i } = { \left\{ \begin{array} { l l } { 1 } \\ { 0 } \end{array} \right. }$ if a countermeasure l is selected in the solution; otherwise:

## De<sup>fi</sup>nition 3. Risk

Given a $T I R , \mathsf { a }$ vector $\vec { S } = ( S _ { l } ) , S _ { l } \in \{ 0 , 1 \} \forall l ,$ 1≤l≤k and a matching matrix $z _ { l i } , z _ { l i } = < S _ { l } , V _ { i } >$ , the risk R is de<sup>fi</sup>ned as:

$$
R = \left\{T I R - \sum_ {l = 1} ^ {k} \sum_ {j = 1} ^ {m} \sum_ {i = 1} ^ {n} L _ {j i} \cdot I _ {i} \cdot z _ {l i} \cdot S _ {l} \right\}\tag{7}
$$

Problem: Given a vector of vulnerabilities $\vec { V } ,$ threats $\vec { T }$ and k security countermeasures, find the vector $\vec { S }$ which minimises total investment cost and risk.

$$
\min _ {s _ {l}} [ T C, R ]\tag{8}
$$

## 3.1. Multi-objective optimisation principles

Most real world scenario problems can be formulated to satisfy single or multiple objectives and a decision choice is made based on these objectives and constraints. However, these objectives and constraints may con<sup>fl</sup>ict with each other, making it dif<sup>fi</sup>cult to <sup>fi</sup>nd an optimal solution. The con<sup>fl</sup>icting nature of multiple objectives cannot be balanced by just <sup>fi</sup>nding a single optimum solution, since a solution that optimises one of the objectives may not have the same effect on the other objectives. Thus, in cases where two or more feasible solutions should be compared, the concept of Pareto front can be used [12].

## De<sup>fi</sup>nition 4. Pareto optimal solution, concept of dominance

Let us consider, a minimisation problem, where x and $x ^ { \prime }$ are two feasible solutions, X is the set of feasible solutions or decision space, $\mathbf { i . e . , } x , x ^ { \prime } { \in } X , p$ is an objective where $1 \leq p \leq P ,$ , where $P$ is the maximum number of objectives, and $f _ { p }$ is the cost function of objective p. Then, solution x strictly dominates or is preferred to solution $x ^ { \prime }$ if each cost function value $f _ { p } ( x )$ of x is no greater than the corresponding cost function value $f _ { p } ( { \boldsymbol { x } } ^ { \prime } )$ of $x ^ { \prime }$ and at least one cost function value is strictly less: that is, $\dot { f } _ { p } ( x ) { \le } f _ { p } ( x ^ { \prime } )$ for each p and $f _ { p } ( x ) { < } f _ { p } ( x ^ { \prime } )$ for some $p .$ The set of all non-dominated elements is referred to as nondominated frontier or a Pareto front [37].

The concept of dominance plays a crucial role for our problem, i.e., minimisation of the security countermeasure cost and risk. A solution that reduces risk will most probably increase cost and vice versa. However, the Pareto front of our problem will provide optimal trade-offs. Generating a Pareto set can be computationally expensive, though, a number of stochastic search methods such as evolutionary algorithms, tabu search or simulated annealing have been developed. In general, these methods do not guarantee optimal solutions, but they often <sup>fi</sup>nd good approximate solutions. However, as evolutionary algorithms posses several desirable characteristics for the multiobjective problems involving multiple con<sup>fl</sup>icting objectives, and intractably large and complex search spaces, these types of search strategies have been successfully used in the literature [37].

## 3.2. Multi-objective Tabu Search (MOTS) for risk optimisation

We developed a multi-objective Tabu Search (MOTS) technique for solving (8).

The elements, parameters and operation that have been used are presented as follows:

• Solution $\vec { S }$ A solution $\dot { S }$ is de<sup>fi</sup>ned as a vector of countermeasures.

• Initial random solution $S _ { \mathrm { r n d } } .$ MOTS algorithm starts creating an initial solution ${ \vec { S } } _ { \mathrm { r n d } } ,$ , which is randomly selected, i.e., each element $S _ { l }$ of solution S is set to 0 or 1 with an equal probability.

• The solution space X. The solution space X.

The solution space X is the set of all possible solutions. The size of X is $2 ^ { l } ,$ where l is the number of available countermeasures.

• Objective function $f _ { p } \left( \vec { S } \right)$ The objective function $\setminus _ { f _ { p } } \left( \vec { S } \right)$ is used to evaluate solution $\vec { S } ^ { \cdot }$ with respect to the objective p. In this case, there are two objective functions, Eqs. (6) and (7).

• Neighbourhood • Neighbourhood $\mathcal { N } _ { s } .$

MOTS moves at each iteration from current solution $\vec { S }$ to a neighbouring one ${ \vec { S } } ^ { \prime }$ based on a tabu selection process.

• Tabu List (tb).

The concept of the tabu list is introduced to prevent the problem of possible cycling or/and in<sup>fi</sup>nite loops [7]. In this case, the tabu list does not allow solutions that have been visited recently.

• Aspiration criteria.

The aspiration criteria is a global rule for allowing a move, even if it is tabu, if it is a non-dominated solution [6].

• Stopping criteria.

MOTS stops iterating when a given condition is reached. The condition could be a given number of iterations, a running time or a solution quality.

Algorithm 1. Pseudo Code for multi-objective TS

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\vec{S} = \vec{S}_{rnd}; f_{cur}^{c} = f_{c}(\vec{S}); f_{cur}^{r} = f_{r}(\vec{S});$  /* random initial solution */
 $\vec{S}_{best} = \vec{S};$  /* initialise best solution */
tb = 0;    /* initialise tabu list */
iter = 0    /* set an iteration counter */

while iter ≤ itermax do
    iter = iter + 1
    neigh = 0    /* initialise checked neighbour counter */

    $\vec{S}_{neigh}^{best}; f_{neigh}^{best}$  /* best neighbour */
    bestNeighList = 0    /* Create best neighbour list */

while neigh ≤ Ns do
    neigh = neigh + 1
    $\vec{S}' = randneigh(\vec{S})$  /* neighbour selection */
    $f_{neigh}^{c} = f_{c}(\vec{S}') ; f_{neigh}^{r} = f_{r}(\vec{S}')$  /* evaluate its cost */
    if dominated == 0 then
    /* Is neighbour dominated by some solution in the Pareto front? */
    $\vec{S}_{best} = \vec{S}' ; f_{best}^{c} = f_{neigh}^{c} ; f_{best}^{r} = f_{neigh}^{r}$  /* save it */
    StoreSolutionInPareto( $\vec{S}'$ )
    break;    /* stop looking for neighbours */
    end
    if movement( $\vec{S}, \vec{S}'$ ) in tb then
    /* Is this movement forbidden? */
    continue;    /* Yes, skip it */
    end
    if neigh == 0,  $f_{c}(\vec{S}') &lt; f_{c}(\vec{S})$  or  $f_{r}(\vec{S}') &lt; f_{r}(\vec{S})$  then
    StoreSolutionInBestNeighList( $\vec{S}'$ )
    end
    neigh = neigh + 1;
end
m = movement( $\vec{S}, \vec{S}_{neigh}^{best}$ )
 $\vec{S} = \vec{S}_{neigh}^{best}; f_{cur}^{c} = f_{neigh}^{best,c}; f_{cur}^{r} = f_{neigh}^{best,r}$  /* Move to best neighbour */
tb = tb + [m]    /* add movement to tabu list */
removeOld(tabu)    /* remove old entries */
end
</div>

When applying MOTS to the minimisation problem proposed in this study, MOTS moves in each iteration from the current solution S to a neighbouring one ${ \vec { S } } ^ { \prime }$ . In our algorithm, neighbouring solutions are always selected randomly, by choosing a random countermeasure S and changing its allowance from 0 to 1 or vice versa.

First of all, in each iteration the neighbourhood $\mathcal { N } _ { s }$ of a current <sup>N</sup>solution S must be de<sup>fi</sup>ned. In our case, we limit the number of visited neighbours to a value $N _ { s } .$ Thus, MOTS moves from current solution S to its best neighbouring one (with the lowest cost and/or risk within the neighbourhood) $\vec { S } ^ { \prime } { \in } N _ { s } .$ . To construct the Pareto frontier, we record the non-dominated solutions by removing dominated ones from the recorded set. The dominated solutions are those, which will satisfy at least one the following constraints:

• If the objective function value for cost $f _ { \mathrm { c } } \left( \vec { S } \right)$ is no greater or equal to the corresponding cost function value of the neighbour, that is, $f _ { \mathrm { c } } \left( \vec { S } \right) { \leq } f _ { \mathrm { c } } \left( \vec { S } ^ { \prime } \right)$ and the objective function value for risk $f _ { \mathrm { r } } \left( \vec { S } \right)$ is strictly less than the corresponding risk function value of the neighbour: that is, $f _ { \mathrm { r } } \left( { \vec { S } } \right) < f _ { \mathrm { r } } \left( { \vec { S } } ^ { \prime } \right)$ ;

• If the objective function value for cost $f _ { \mathrm { c } } \left( \vec { S } \right)$ is no greater than the corresponding cost function value of the neighbour, that is, $f _ { \mathrm { c } } \left( \vec { S } \right) < f _ { \mathrm { c } } \left( \vec { S } ^ { \prime } \right)$ and the objective function value for risk $f _ { \mathrm { r } } \left( \vec { S } \right)$ is no greater or equal to the corresponding risk function value of the neighbour: that is, $f _ { \mathrm { r } } \left( { \vec { S } } \right) \leq f _ { \mathrm { r } } \left( { \vec { S } } ^ { \prime } \right)$

• If the objective function value for cost $f _ { \mathrm { c } } \left( \vec { S } \right)$ is equal to the corresponding cost function value of the neighbour, that is, $f _ { \mathrm { c } } \left( \vec { S } \right) =$ $f _ { \mathrm { c } } \left( \vec { S } ^ { \prime } \right)$ and the objective function value for risk $f _ { \mathrm { r } } \left( \vec { S } \right)$ is equal to the corresponding risk function value of the neighbour: that is, $f _ { \mathrm { r } } \left( \vec { S } \right) = f _ { \mathrm { r } } \left( \vec { S } ^ { \prime } \right)$

It must be noted that in MOTS the objective function $f \biggl ( \vec { S } ^ { ' } \biggr )$ of the best neighbour does not need to improve the current one $f { \ ' } { \vec { S } }$ . To avoid getting stuck in a local minima, MOTS may move from current solution S to a neighbouring one ${ \vec { S } } ^ { \prime }$ even it is worsening the objective function value [7]. The action of moving from current solution $\vec { S }$ to its best neighbour ${ \vec { S } } ^ { \prime }$ is called movement [13]. The pseudo code of the MOTS is given in Algorithm 1.

## 4. Experiments and discussion

In the following section, we demonstrate the validity of the proposed model by applying an optimisation routine to help decision makers to decide the best solution in multi-objective terms. We compare the qualities of MOTS solutions to optimal ones obtained through the traditional exhaustive search (ES) approach. We examine ten cases when the number of iterations is changed from 500 iterations to 30,000 iterations to examine the speed of the MOTS approach in <sup>fi</sup>nding near optimal solutions.

Prior to presenting actual results, it should be noted that the solving method was written in C++ and executed on an AMD Athlon II X2 245 2.8 MHZ processor, 4 GB RAM.

## 4.1. Testing the speed of MOTS

For the <sup>fi</sup>rst experiment, we test the speed of the MOTS for the original problem. Increasing the number of iterations, we have recorded the time. Table 8 summarises the ef<sup>fi</sup>ciency of the MOTS recorded at each case.

The next step of the <sup>fi</sup>rst experiment was to analyse the quality of solutions obtained. Fig. 2(a) shows the non-dominated solutions obtained in 500, 2500, 5000, 8000 and 20,000 iterations.

In comparison, we took 8000 and 20,000 iteration generated solutions. We did not observe any signi<sup>fi</sup>cant change in the non-dominated solutions by varying the algorithm parameters. The Pareto Fronts are shown in Fig. 2(b). As it can be seen, in 8000 iterations MOTS has found similar number of dominated solutions, which also are close to the ones obtained in 20,000 iterations. Once we have noted that the variation in solutions is not large and the speed difference is signi<sup>fi</sup>cant for mentioned cases, we can assume that stopping an algorithm after 8000 iterations yields a high number of near optimal solutions.

(a) Convergence of the Pareto Front  
![](/api/attachments/B84F758E/fulltext/images/f3e03b23caa8abe76c493a2252ad93db893cc1983c8790afc778ac8f9b5742a3.jpg)

(b) Defference in new solutions  
![](/api/attachments/B84F758E/fulltext/images/64964ff7693385803a3c827ef70c75eeadde0e5433c33f6c341f7e1525e3813f.jpg)  
Fig. 2. MOTS obtained Pareto front and difference in solutions.

## 4.2. Testing the quality of solutions

The second experiment was to examine the quality of solutions obtained by MOTS algorithm. We carried it out for the same data set comparing MOTS with exhaustive search method (ES). An ES approach was chosen to this problem for several reasons. Firstly, ES is a search technique to solve multi-objective optimisation problems based on enumerative evaluation of each possible solution from a given <sup>fi</sup>nite set. Secondly and perhaps more importantly, the ES approach is the only way at present to <sup>fi</sup>nd an exact Pareto Front in multi-objective problems [14].

Fig. 3(a) shows the Pareto front obtained by running ES. The algorithm was able to obtain 106 solutions, which surely were optimal ones for this problem. Analysing the quality of solutions, we have compared Pareto fronts obtained by both algorithms, shown in Fig. 3(b). We did not see any change in solutions in the intervals of [(0.6:3)⋅10<sup>4</sup>] by the objective 1 (cost) value and [1400:1750] by the objective 2 (risk). A decision maker, in general, would be interested in these intervals, as they are the middle of the Pareto front with good trade-offs between both objectives.

Table 8  
TS time recorded for ten cases.

<table><tr><td>Case</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Iterations</td><td>500</td><td>1000</td><td>2500</td><td>5000</td><td>8000</td><td>10,000</td><td>12,000</td><td>15,000</td><td>20,000</td><td>30,000</td></tr><tr><td>Time (s)</td><td>5</td><td>14</td><td>44</td><td>99</td><td>163</td><td>221</td><td>261</td><td>336</td><td>450</td><td>598</td></tr></table>

Table 9  
![](/api/attachments/B84F758E/fulltext/images/bb7fc5a8ccd6fd3edca67c7bce4bc38396d4fea977ef237b8995acbc0aa8d781.jpg)

(b) ES compared to TS  
![](/api/attachments/B84F758E/fulltext/images/e4b0b2e3a0665db317df07dfbc38499ab1634df3060080fa7b1326b4272a01af.jpg)  
Fig. 3. Comparison of the Pareto Front obtained by MOTS and ES algorithms.

Despite the fact that ES is the only algorithm that has an ability to obtain optimal solutions for multi-objective problems, the downside of ES is that the search is computationally expensive.

We have recorded the execution time required to generate the Pareto Front for the ES approach and compared it with the MOTS 8000 iterations approach (Table 9).

MOTS search method performed 15 times faster than ES, because ES search technique checks every possible combination $( 2 ^ { 2 4 } )$ . When the input size would increase, the time for ES to check all combinations would increase exponentially. In this study, the size of a problem demonstrated is very close to a real size problems, for example, Practical Threat Analysis(PTA) case study takes into consideration 22 countermeasures, 16 vulnerabilities and 11 threats and corresponding likelihood values [26]. In the current IT climate, the evolving nature of threats and vulnerabilities may dramatically increase the size of a problem in the near future. Thus, ES approach would take weeks, months or maybe years to solve very large size problems. In a real life scenario it is important to know possible solutions in the shortest possible time, as the risk obtained today may not be the same tomorrow.

MOTS and ES comparison data.

<table><tr><td></td><td>MOTS (8000 iterations)</td><td>ES</td></tr><tr><td>Time (s)</td><td>163</td><td>2466</td></tr><tr><td>Number of non-dominated solutions</td><td>54</td><td>106</td></tr></table>

![](/api/attachments/B84F758E/fulltext/images/5b00339d92383ee13ca2d097d9dd473ab0498df9c42423a3b6d24d3846a6db0b.jpg)  
Fig. 4. Euclidean distance between 54 MOTS obtained solutions and 106 ES optimum ones.

To justify the fact that MOTS has found near optimal solutions, we calculated Euclidean distance between solutions obtained by both algorithms. Fig. 4 shows how close these 54 solutions obtained by MOTS were to the optimum one obtained by ES. It was recorded that 31 of the recorded solutions obtained by MOTS coincided exactly with the ones obtained by ES; thus we can say that MOTS has obtained 30% of optimal solutions when the stopping condition was set to 8000 iterations (Table 10). Other solutions though, are very close to optimum ones, as can be seen in Fig. 4.

## 4.3. Testing MOTS for the different problem

For the third experiment, we modi<sup>fi</sup>ed the problem by varying the likelihood $L _ { i j } ,$ impact $I _ { i } ,$ cost C and matching $z _ { l i }$ values.

In terms of speed, MOTS under different data set performed very similarly to the original problem. The time and quality of solutions are summarised in Table 10.

From the experiment, we can claim, that in the intervals of 5000–10000 iterations the decision maker can obtain higher percentage of optimal solutions (\~30%). However, when time is considered as a stopping condition, the best results would be achieved when the algorithm runs between 95 s and 200 s.

With such results, the MOTS approach shows acceptable levels of accuracy in determining optimal solutions.

Table 10  
Result comparison under different data sets.

<table><tr><td rowspan="2">Iterations</td><td colspan="3">Original problem (MOTS)</td><td colspan="3">Different problem (MOTS)</td></tr><tr><td>No. of optimal solutions</td><td>Optimality in %</td><td>Time (s)</td><td>No. of optimal solutions</td><td>Optimality in %</td><td>Time (s)</td></tr><tr><td>500</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>3</td></tr><tr><td>2500</td><td>2</td><td>1.9</td><td>44</td><td>17</td><td>12</td><td>42</td></tr><tr><td>5000</td><td>11</td><td>10</td><td>99</td><td>25</td><td>19</td><td>94</td></tr><tr><td>8000</td><td>31</td><td>30</td><td>163</td><td>34</td><td>26</td><td>158</td></tr><tr><td>10 000</td><td>31</td><td>30</td><td>221</td><td>33</td><td>25</td><td>200</td></tr><tr><td>15 000</td><td>30</td><td>28</td><td>336</td><td>32</td><td>24</td><td>317</td></tr><tr><td>20 000</td><td>29</td><td>28</td><td>450</td><td>31</td><td>23</td><td>433</td></tr><tr><td>ES</td><td>106</td><td>100</td><td>2488</td><td>131</td><td>100</td><td>2842</td></tr></table>

Once a decision maker has a better perspective of the possible solutions, the decision on what set of countermeasures should be selected can be justi<sup>fi</sup>ed by the obtained cost and risk trade-offs. Arguably, the MOTS algorithm thus proves to be an ef<sup>fi</sup>cient way of solving security countermeasure problem when there are two objectives to be minimised.

## 5. Conclusion

The importance of decision making in the area of computer security is well understood. Large body of work has been undertaken to support decision makers, by providing models which deal with the optimisation of <sup>fi</sup>nancial investments in relation to computer security. However, most of the models described in existing studies are hypothetical rather than practical.

This paper has proposed a novel risk assessment and optimisation model (RAOM), which is partially based on NIST SP800-30 guidelines on performing risk assessments in various organisations. We adopted the step-by-step procedure of assessing risk, while making some important modi<sup>fi</sup>cations in calculating impact of vulnerabilities and total risk. Due to the fact that computer security is referred to as CIA, we designed a way of de<sup>fi</sup>ning risk in relation to an impact on CIA that each identi<sup>fi</sup>ed vulnerability introduces.

The RAOM differs from previous attempts on improving computer security by applying optimisation techniques in several ways. First of all, the RAOM seeks to assess risk considering an impact on CIA and likelihood that possible threats will exploit identi<sup>fi</sup>ed vulnerabilities, whereas most recent methodologies exclude this realistic fact and assume that risk is uniformly distributed (e.g. [8]). Moreover, RAOM has an advantage that by applying a MOTS method to solve a multiobjective countermeasure selection problem formulated in this study makes it possible to review the solutions with the good balance between the two considered objectives: risk and cost.

Overall, it can be concluded that RAOM provides a new way to make more justi<sup>fi</sup>ed and informed decisions. Experimental results show that MOTS approach is much faster than the ES approach in searching for the Pareto optimal set. Moreover, the proposed MOTS algorithm shows a good approximation of solutions if compared with the optimal solutions obtained by the ES.

## References

[1] R. Anderson, P. Feldman, S. Gerwehr, B. Houghton, R. Mesic, J. Pinder, J. Rothenberg, J. Chiesa, Securing the U.S. Defense Information Infrastructure: A Proposed Approach, RAND, Santa Monica, CA, 1999.

[2] A. Asosheh, B. Dehmoubed, A. Khani, A new quantitative approach for informa tion security risk assessment, International Conference on Computer Science and Information Technology, 2009, pp. 222–227.

[3] S. Bistarelli, F. Fioravanti, P. Peretti, Defense trees for economic evaluation of security investments, ARES, 2006, pp. 416–423.

[4] R. Dewri, N. Poolsappasit, I. Ray, D. Whitley, Optimal security hardening using multi-objective optimization on attack tree models of networks, ACM Conference on Computer and Communications Security, 2007, pp. 204–213.

[5] DTI, Information Security Breaches Survey, Tech. rep, Department of Trade and Industry, 2004.

[6] M. Gendreau, An introduction to tabu search, International series in operations research and management science 57 (2003) 37–54.

[7] F. Glover, M. Laguna, Tabu Search, Kluwer Academic Publishers, Norwell, MA, USA, 1997.

[8] M. Gupta, J. Rees, A. Chaturvedi, J. Chi, Matching information security vulnerabilities to organizational security pro<sup>fi</sup>les: a genetic algorithm approach, Decision Support Systems 41 (2006) 592–603.

[9] IBM, Software online catalog, http://www-01.ibm.com/software/info/app/ ecatalog, Accessed before 1st of October 2011.

[10] ISO/IEC 17799:2005, Information technology—code of practice for information security management. 2005

[11] ISO/IEC 27001:2005, Information technology—Security techniques—Information security management systems—Requirements, International Organisation for Standardization. 2005.

[12l I. Legriel C. Le Guernic S. Cotton O. Maler, Approximating the pareto front of multi-criteria optimization problems. Tools and Algorithms for the Construction and Analysis of Systems, Vol. 6015, Springer, Berlin/Heidelberg, 2010, pp. 69–83.

[13] D. López-Peréz, Interference avoidance in macrocell-femtocell self-organizing networks: models and optimization, Ph.D. thesis, University of Bedfordshire (2010).

[14] F. Luna, A.J. Nebro, E. Alba, A globus-based distributed enumerative search algorithm for multi-objective optimization, Tech. rep, Departamento de Lenguajes y Ciencias de la Computacion, University of Malaga, 2004.

[15] H. Lv, Research on network risk assessment based on attack probability, International Workshop on Computer Science and Engineering 2 (2009) 376–381.

[16] C. Maple, A. Phillips, UK Security Breach Investigations Report, 7Safe, 2010.

[17] C. Maple, V. Viduto, A visualisation technique for the identi<sup>fi</sup>cation of security threats in networked systems, Information Visualisation, 2010, pp. 551–556.

[18] P. Mell, K. Scarfone, S. Romanosky, A complete guide to the common vulnerability scoring system version 2.0, Tech. rep, 2007.

[19] Microsoft Corporation, Microsoft Security Response Center Security Bulletin Severity Rating System, http://technet.microsoft.com/en-us/security/bulletin rating, Accessed before 1st of February 2011.

[20] T. Neubauer, C. Stummer, E. Weippl, Workshop-based multiobjective security safeguard selection, International Conference on Availability, Reliability and Security, 2006, pp. 366–373.

[21] T. Neubauer, A. Ekelhart, S. Fenz, Interactive selection of ISO 27001 controls under multiple objectives, SEC, 2008, pp. 477–492.

[22] J. Newsome, D. Brumley, D.X. Song, Vulnerability-speci<sup>fi</sup>c execution <sup>fi</sup>ltering for exploit prevention on commodity software, NDSS, 2006.

[23] NIST, National vulnerability database, automating vulnerability management, security measurement and compliance checking, http://nvd.nist.gov/home.cfm Accessed before 1st of December 2010.

[24] S. Noel, S. Jajodia, B. O'Berry, M. Jacobs, Ef<sup>fi</sup>cient minimum-cost network hardening via exploit dependency graphs, ACSAC, 2003, pp. 86–95

[25] PTA, A practical threat analysis case study: next generation call accounting, 2005 accessed before 10 May 2011.

[26] Softerra, Softerra LDAP administrator, http://www.ldapbrowser.com/purchase. htm, Accessed before 1st of October 2011.

[27] G. Stoneburner, A. Goguen, A. Feringa, Risk Management Guide for Information Technology Systems, Special Publication SP800-30, 2002.

[28] Symantec, SSL certi<sup>fi</sup>cates, https://www.verisign.co.uk/ssl Accessed before 1st of October 2011.

[29] M. Templeman, M. Beishon, L. Malachowski, A. Wilson, T. Nash, L. Robertson, Information security—best practice measures for protecting your business, Tech. rep, Department of Trade and Industry, 2005.

[30] US CERT, US-CERT Vulnerability Note Field Descriptions, http://www.kb.cert.org/ vuls/html/<sup>fi</sup>eldhelp, Accessed before 10th of December 2010.

[31] US-CERT, Introduction to recommended practices, http://www.us-cert.gov/ control\_systems/practices/, Accessed before 1st of April 2011.

[32] S. Vadera, C. Potter, A. Beard, Information Security Breaches Survey, Tech. rep, PriceWaterHouseCoopers, 2008.

[33] Verizon, 2008 Data Breach Investigations Report, Tech. rep, Verizon Business RISK Team, 2008

[34] V. Viduto, C. Maple, W. Huang, An analytical evaluation of network security modelling techniques applied to manage threats, International Conference on Broadband Wireless Computing, Communication and Applications (2010) 117–123.

[35] V. Viduto, C. Maple, W. Huang, Managing threats by the use of visualisation techniques, International Journal of Space based and Situated Computing 1 (2/3) (2011) 204–212, http://dx,doi,org/10.1504/IISSC,2011.040347.

[36] L. Wang, S. Noel, S. Jajodia, Minimum-cost network hardening using attack graphs, Computer Communications 29 (2006) 3812–3824

[37] E. Zitzler, M. Laumanns, S. Bleuler, A tutorial on evolutionary multiobjective optimization, in: X. Gandibleux, et al., (Eds.), Metaheuristics for Multiobjective Optimisation, Lecture Notes in Economics and Mathematical Systems, Springer, 2004.

![](/api/attachments/B84F758E/fulltext/images/dc03e1fc873303b91f37ec55a2b23e46e40d6c0876e70f70dc5e6c8bc3d860f6.jpg)

![](/api/attachments/B84F758E/fulltext/images/67b1e983df249eeb6539fbe505a1aa8e810769a48490f5f766b037dbf7a825ec.jpg)  
Valentina Viduto—is a doctoral student in the Institute for Research in Applicable Computing (IRAC) at the University of Bedfordshire. She obtained her BSc (Hons) in Computer Networking in 2009. The same year, she has been accepted as a PhD student on the project funded by EPSRC investigating multi-objective decision support in computer security, risk assessment and optimisation techniques. Her research interests include information security, multi-objective opti misation, visualisation techniques, decision support and risk management.

Prof. Carsten Maple—is the Pro Vice Chancellor for Research & Enterprise at the University of Bedfordshire responsible for developing the University's strategy for research and enterprise activities. He is a member of several professional societies including Council of Professors and Heads of Computing whose remit is to promote public education in Computing, Also. he is a Fellow of the British Computer Society the Chartered Institute for IT and is a Chartered IT professional. His interests include information security and trust, and authentication in distributed systems, cyberstalking.

![](/api/attachments/B84F758E/fulltext/images/04f8de977cfef62d9dcc4820d00e16b641949220863b6d82fc47b5994e4b9c0b.jpg)

Dr. Wei Huang—obtained his BSc and MSc from South China University of Technology and completed his PhD at Loughborough University, where his research was focused upon the scheduling of batch processing plants including development of a constraint model and computer-based scheduling system.

![](/api/attachments/B84F758E/fulltext/images/85652636d984aaf81aaf5783aa1d256f8143049c9d5395459be6a2a45f043b1b.jpg)

Dr. David López-Pérez—David Lopez-Perez is Research Associate at the Centre for Telecommunication Research, King's College London, UK. David received his Bachelor (BSc) and Master (MSc) degrees in Telecommunication from Miguel Hernandez University, Spain, in 2003 and 2006, respectively, and his Doctor in Philosophy (PhD) title from University of Bedfordshire, UK, in 2011. He has been in vited researcher at DOCOMO USA labs, Palo Alto, CA in 2011, and CITI INSA, Lyon, France in 2009. In May 2007, he was awarded with a PhD Marie-Curie fellowship at the Centre for Wireless Network Design (CWiND) at University of Bedfordshire, UK. With 30 years of age, he has published more than 50 book chapters, journal and conference papers in recognised venues, and has been awarded as Exemplary Reviewer for IEEE Communica tions Letters. From February 2006 and for a year, he was with Cork Institute of Technology, Ireland, and from February 2005 and for a year, he was with VODAFONE Spain, Spain. He is or has been guest editor of ACM Springer Mobile Networks and Applications (MONE) Journal and EURASIP Journal of Computer Networks and Communications (JCNC), and editor and/or author of several cellular HetNet related books, i.e. “Heterogeneous Cellular Networks: Theory, Simulation and Deployment” Cambridge University Press, 2012, “Femtocells—Technologies and Deployment”, Wiley 2010, and “Femtocell Networks: Deployment, PHY Techniques, and Resource Management”, Cambridge University Press, 2012. Moreover, he is or has also been cochair of several HetNet related workshops, e.g., the 1st IEEE WCNC Workshop on Broadband Femtocells: Paving the way to HetNets, the 2nd IEEE 2011 GLOBECOM Workshop on Femtocell Networks (FEMnet).
