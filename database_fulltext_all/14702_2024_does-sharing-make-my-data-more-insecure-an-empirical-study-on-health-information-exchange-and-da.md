---
otero_id: 14702
otero_key: "7TTMQQGR"
title: "Does Sharing Make My Data More Insecure? An Empirical Study on Health Information Exchange and Data Breaches"
authors: "Leting Zhang; Sunil Wattal; Min-Seok Pang"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17479"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DOES SHARING MAKE MY DATA MORE INSECURE? AN EMPIRICAL STUDY ON HEALTH INFORMATION EXCHANGE AND DATA BREACHES<sup>1</sup>

Leting Zhang Lerner College of Business and Economics, University of Delaware Delaware, DE, U.S.A {letingz@udel.edu}

Sunil Wattal Fox School of Business, Temple University Philadelphia, PA, U.S.A. {sunil.wattal@temple.edu}

Min-Seok Pang Wisconsin School of Business, University of Wisconsin-Madison Madison, WI, U.S.A. {mpang9@wisc.edu}

This paper examines the information security implications of hospitals participating in health information exchanges (HIE). While data security threats may increase when hospitals join HIEs to share data across organizational boundaries, HIEs institute “secure exchange” and promote security practices among participants. Due to these countervailing effects, it is unclear how joining an HIE affects hospitals’ data breach risk. This study seeks to understand the security implications of HIEs from the lens of governance and coordination. We compiled a panel dataset of more than 3,000 hospitals over six years. By leveraging different identification strategies, including difference-in-differences design, matching, and instrumental variables, we found that the likelihood of a hospital experiencing a data breach decreased by more than 35.37 % after joining an HIE. We further show that the effect was more pronounced among HIE member hospitals with more sophisticated clinical IT systems or after HIE security laws were enacted. We discuss the implications for research and practice.

Keywords: Information security, data breaches, health information exchange, interorganizational system, IT governance

## Introduction

Healthcare data security has attracted increasing attention among scholars and healthcare stakeholders (Rubright, 2023; Heath et al., 2022). The associated stakes are notably high, and the ramifications affect healthcare providers and patients. According to a 2023 IBM report, healthcare security breaches cost an average of \$11 million per incident, the highest of any industry in terms of cost (IBM Security, 2023). Moreover, healthcare providers who experience breaches face substantial financial losses due to penalties, remediation, and reputation damage (Mckeon, 2022). Patients also suffer from these breaches as their personal and health information may be illegally used for financial and medical identity thefts (Greig, 2022). Many practitioners and scholars attribute the escalated risk to digitalization initiatives in the healthcare sector (Seh et al., 2020; Kim & Kwon, 2019; Perlroth, 2011; Sittig & Singh, 2011). One such initiative is the health information exchange (HIE).

As one of the most important initiatives in healthcare digital transformation, HIEs promote interoperability standards in the healthcare sector, which allow different health IT systems to communicate and work together. It aims to facilitate efficient sharing of electronic patient information between unaffiliated health systems. Specifically, hospitals joining an HIE can electronically exchange patient information with external providers through a module in their electronic health records (EHR) system or a stand-alone portal. Many studies show that sharing patient information via HIEs can benefit the healthcare sector by improving the quality of care, reducing duplicate costs, and lowering Medicare expenditures, among other benefits (Adjerid et al., 2018; Atasoy et al., 2018; Ayabakan et al., 2017). Because of these benefits, HIEs have drawn substantial attention from healthcare stakeholders. In 2009, the passage of the Health Information Technology for Economic and Clinical Health Act in the United States promoted the adoption of EHR and HIE by healthcare providers through monetary incentives (Burde, 2011). By 2018, approximately 70% of the acute care hospitals were connected to more than one HIE with a nationwide scope (Monica, 2018). As the scale of shared healthcare data increases, there are growing discussions among HIE stakeholders and policymakers about data security in HIEs.

On the one hand, many argue that participation in an HIE lowers a hospital’s security risk. HIE governance, which refers to the set of policies, standards, and practices that govern the exchange of health information among different participants in an HIE, is critical in coordinating data sharing (Adjerid et al., 2018; McGowan et al., 2012). Typically, a governing body or a steering committee oversees the governance process, establishes the roles and responsibilities of stakeholders, defines the legal and ethical principles that guide data exchange, and outlines the technical requirements for data sharing. Effective governance is critical to ensure that HIEs are secure, reliable, and trusted by participants, patients, and the broader healthcare community (Marshall et al., 2009). Due to these HIE governance mechanisms, hospitals in HIEs are likely to realize a reduction in their data breach risk.

On the other hand, joining an interorganizational system (IOS) such as an HIE can also raise concerns about additional threats to data security. HIEs aggregate data, expand data access, and render key components of risk no longer isolated to any individual participant (Huang et al., 2014). For example, in July 2016, an unauthorized person at Codman Square Health Center obtained access to the New England Healthcare Exchange Network, compromising the data of 140 Codman’s patients and over 4,000 others in the HIE (McGee, 2016). In 2022, a Chicago-based HIE, CommonSpirit Health, experienced a ransomware attack. The incident involved patients’ data from more than 100 organizations (Wider, 2023). HIE data breaches typically involve a significant number of patients from various healthcare organizations and can result in reputational damage for multiple healthcare organizations and a loss of trust from patients in the HIE organization (Hirsch, 2016). Consequently, there are substantial security concerns surrounding HIE. According to a survey conducted by the Ponemon Institute, over 72% of healthcare providers have only some or no confidence in sharing patient data on HIEs (Ponemon Institute, 2012). Additionally, data security is regarded as one of the main barriers to HIE implementation (Mello et al., 2018; Adler-Milstein & Jha, 2014).

Considering the strategic importance of HIE and its countervailing effects on data security, it becomes imperative to examine the impact of HIEs on the data security landscape. With this motivation, we propose our main research question: Does joining a health information exchange affect a hospital’s overall data breach risk? Furthermore, we investigate whether the HIE’s impact varies based on the complexity of a hospital’s clinical IT system and the enforcement of state HIE security laws. These factors can affect hospitals’ data protection costs and the effectiveness of HIE governance. A clinical IT system is an essential component of a hospital’s IT infrastructure. Its complexity usually represents a hospital’s IT capability and affects data protection efficiency. Yet there is a notable variance in the complexity of clinical IT systems across hospitals. Moreover, HIE security laws aim to ensure data sharing security and potentially improve HIE governance effectiveness. However, not every state has enforced these laws. Therefore, we want to understand how HIEs affect data breaches and how the variations in the two key factors affect the HIE’s impact.

To investigate these questions based on a theoretical foundation, we examine the channels through which HIEs impact hospitals’ security outcomes. Drawing on the cost structure of security protection, we set up an analytical model to explore how the equilibria of a hospital’s cybersecurity investment and data breach risk shift when the hospital joins an HIE. Guided by the model’s results, we conducted empirical analyses by compiling a six-year (2010- 2015) panel dataset that covers comprehensive characteristics of hospitals and healthcare markets. To infer the causal impact of joining an HIE on hospitals’ breach risk, we mainly used difference-in-differences, matching, and instrumental variables approaches.

The main findings of our paper can be summarized as follows. First, we find that joining an HIE reduces the likelihood that a hospital experiences a data breach, contrary to concerns over data security in HIEs. Furthermore, our analyses demonstrate that a hospital increases its IT security investment after joining an HIE. Additionally, the complexity of hospitals’ clinical IT systems and the enforcement of state-level HIE security laws enhance the impact of HIEs in lowering data breach risk. These findings remain consistent through different identification strategies and robustness checks.

We contribute to the existing literature in several ways. This study is the first to empirically analyze how joining an HIE affects hospitals’ data breach risk from a security cost structure lens. It complements prior studies on interdependent security, IOS governance, and organizational information security management. Furthermore, we offer several practical implications for hospitals, HIE administrators, and policymakers. Our findings suggest that providing securityrelated technical support to hospitals with less complex health IT systems would be beneficial. Furthermore, local governments can enforce HIE security laws to further reduce HIE hospitals’ breach risk. Our findings and recommendations can also shed light on other sectors where exchanging business-related or operational data through IOSs is prevalent, such as finance and manufacturing.

## Literature Review

## Interdependent Security

Interdependent security refers to situations where different parties’ actions mutually affect each other’s cybersecurity outcomes. Studies in this field typically use analytical models that characterize the security cost structure to examine equilibrium security investment and outcomes in various settings (e.g., Huang et al., 2014; Jayanth et al., 2011). Our study is related to two topics in this field. The first focuses on cybersecurity information sharing among organizations and highlights its impact on enhancing organizations’ capability to prevent, discover, and fix security incidents (Gordon et al., 2003). The second looks at security in network systems and argues that interdependency may lead to lower cybersecurity expenditure and worse security outcomes (e.g., Acemoglu et al., 2016; Anderson & Moore, 2006).

Similar to these two board topics, our study focuses on HIEs, which involve cooperation from participating hospitals but with distinct characteristics. First, joining an HIE does not inherently improve security. The purpose of an HIE is primarily to exchange patients’ healthcare information (Ayabakan et al., 2017) not security-specific information. Second, using an HIE requires hospitals to adopt new software and routines, which may disrupt the current workflows and impair data security (Kim & Kwon, 2019). Third, institutional factors are critical in building trust and cooperation among hospitals in the same HIE (Karahanna et al., 2019), but this has received limited attention in interdependent security. To shed light on the impact of HIE, we consider these distinctions. Hence, building on the previous model of security costs, we introduce a stylized analytical model that incorporates the HIE’s characteristics, which provides a theoretical framework to guide our empirical analyses and generalize our findings.

## Interorganizational Systems and Governance

An HIE is a type of interorganizational system that enables efficient data exchange across organizational boundaries and improves production efficiencies (Wang & Seidmann, 1995; Bakos, 1991). Unlike information systems that operate within a single organization, IOSs integrate IT systems from multiple unaffiliated organizations with varying objectives and processes. Consequently, their implementation may face substantial challenges that may hinder beneficial outcomes (Hamre & Monteiro, 2013). Many studies argue that an IOS may not always improve business performance, and governance is the critical antecedent of IOS success (Roehrich et al., 2020; Adjerid et al., 2018; Chatterjee & Ravichandran, 2004). This is because the governance mechanisms, including norms, policies, contracts, and standards, can shape the behaviors of IOS participants (Chatterjee & Ravichandran, 2013; Fischer et al., 2012; Grover & Kohli, 2012).

While the security implications of data sharing in an IOS have received increased attention in the industry, most academic research focuses on business objectives rather than information security since improving security outcomes is not the main purpose of implementing IOS. Additionally, information security risk is often viewed as an operational risk with technical complexity. Our paper contributes to the IOS literature by investigating the relationship between IOS adoption and information security performance, positioning IOS governance as a mechanism for this relationship. Furthermore, we examine the role of IOS participants’ IT characteristics and regional policy requirements, providing new insights into improving information security performance within an IOS.

## Organizational Information Security Management

The information systems (IS) literature extensively investigates organizational security performance from the perspectives of primary security protection practices (Straub & Nance, 1990) and security compromise paths (Ransbotham & Mitra, 2009). An increasing amount of research empirically evaluates the performance of organizational information security investments (e.g., Kim & Kwon, 2019; Kwon & Johnson, 2014; Miller & Tucker, 2011). Drawing from empirical studies on organizational security, our research focuses on two key areas: hospitals and interorganizational IT systems.

Previous studies investigate different antecedents of hospitals’ data breaches, including IT characteristics (Kwon & Johnson, 2018; Miller & Tucker, 2011a), institutional factors (Angst et al., 2017a), and security investment strategies (Kwon & Johnson, 2014). However, to the best of our understanding, no study has examined how HIEs affect hospitals’ data breach risk. Furthermore, few studies empirically test the impact of cross-organizational links on security outcomes and report contradictory findings. For instance, Tanriverdi et al. (2019) argue that establishing external IT interlinkages weakens a firm’s security performance, while Baskerville et al. (2018) demonstrate that a firm with a higher level of external IT system integration uses more cybersecurity countermeasures. These contradictory findings imply that connecting to external organizations can have heterogeneous impacts on information security outcomes. Our study contributes to the literature in two main ways. First, we enhance the understanding of the security implications of one type of health IT—the HIE. Second, we provide insights into “security beyond organization boundaries” from the governance perspective.

## HIEs and Data Security

HIE systems serve as a platform for healthcare providers to share electronic health information. An HIE system is typically administered by third-party technology service organizations such as regional health information organizations.<sup>2</sup> As interorganizational systems, HIEs rely on a combination of technologies and a trusting community. To theorize the impact of joining an HIE on hospitals’ breach risk, we discuss the information security implications of an HIE from both governance and risk perspectives.

## HIEs’ Data Security Governance

Ensuring data security is a critical component of IOS governance in an HIE network. The Office of the National Coordinator for Health Information Technology (ONC) released HIE framework documents in 2013 that emphasized security protection (ONC, 2013). In practice, HIE stakeholders decide on the governance framework during the planning phase and implement practices in the operational phase (Adjerid et al., 2018). HIE governance plays a crucial role in safeguarding participating hospitals’ data security by enhancing their data security awareness and imposing accountability for security incidents. All participants are required to sign participant agreements when joining an HIE to ensure compliance with necessary security requirements. (HHS, 2015). HIE governance encourages risk assessment practices that enable hospitals to identify risks and implement mitigation measures (McGowan et al., 2012; AHIMA/HIMSS, 2011; Scholl et al., 2010). Furthermore, HIE governance ensures that participants are held accountable for any security breaches that occur. If a data breach occurs, the responsible participant must notify other participants and take proper measures to remedy the breach. Failure to do so may result in the termination of data sharing with uncooperative participants.<sup>3</sup> Lastly, HIE governance standardizes technical specifications to ensure data access and transmission security (Snell, 2015). In a step further, the technical infrastructure of data transmission enables HIE administrators to monitor data exchange activities (Scholl et al., 2010), and identify abnormalities in the data sharing processes.

## Data Breach Risk of Joining an HIE

Despite the presence of HIE governance, hospitals and the public have expressed concern regarding HIE’s impact on hospitals’ data security. These concerns stem from several factors related to the increased breach risk that hospitals may face after they join an HIE.

First, joining an HIE leads to an increase in the volume of data available to hospitals, making them more attractive targets for attackers. Hospitals retrieve and store other hospitals’ data from the HIE network and, in turn, make their own data accessible to the HIE network (Yaraghi et al., 2015). As a result, an increasing amount of health records from various departments or labs are digitized and transferred to a hospital’s IT systems, which increases the payoffs of illegally accessing the IT systems. According to rational choice theory, the increased payoffs make malicious attackers more likely to target the hospital (Becker, 1968). <sup>4</sup> Second, the implementation of HIE systems introduces digital transformation, thereby disrupting data processing routines and employees’ workflows (Adler-Milstein et al., 2011) and increasing the likelihood of data misuse (D’Arcy et al., 2020). Third, HIE network links may be vulnerable to illegal access and attacks during transmission, posing a risk to other participants in the same network. Attackers may exploit the weakest point in the network to gain unauthorized access to another system (Zhao et al., 2013; Hui et al., 2012).

To summarize, participation in an HIE makes hospitals subject to governance mechanisms and exposes them to higher risk. These dynamics can impact a hospital’s decision to make IT security investments. To better understand hospitals’ decision and security outcomes, we utilize a stylized model and derive several theoretical propositions.

## Theoretical Model

In this section, we present a theoretical model to analyze the impact of HIEs on hospitals’ data breach risk. Drawing on the cost structure of security protection, we compare equilibrium security outcomes of two cases: (1) a hospital that does not join an HIE and (2) a hospital that joins an HIE. Our focus is on understanding the strategic responses of hospitals to cybersecurity investment and the realized security risk. To investigate this, we developed a complete information game where hospitals make simultaneous decisions regarding the level of IT security investment based on their HIE statuses (Join or Not Join).

Based on the models, we theoretically analyze the following questions:

1. How does joining an HIE affect hospitals’ data breach risk?

2. How do hospital-level factors, such as the unit cost of protection, and HIE-level factors, such as the effectiveness of HIE governance, affect the changes in data breach risk?

To answer these questions, we considered two scenarios: (1) a baseline case where two hospitals (Hospitals A and B) do not share data, and (2) a case where the two hospitals agree to share data with each other. Note that the hospitals’ decisions to share data are exogenous, and the two hospitals are identical in terms of size, protection costs, and many other characteristics.<sup>5</sup> To protect their digital assets, the hospitals invest in cybersecurity protection $( C _ { i } )$ . This investment is an increasing function of the protection level $( p _ { i } )$ . Specifically, it is given by:

$$
C _ {i} = \frac {1}{2} c p _ {i} ^ {2} i \in (A, B),\tag{1}
$$

where c is the unit cost of protection that is assumed to be positive. As shown in Equation (1), $C _ { i }$ is a convex function of $p _ { i }$ , which is a common cost structure in security investment models (August et al., 2014; Lee et al., 2013). Hospitals incur costs related to both security losses and cybersecurity investments, and the main objective is to minimize the total cost.

## A Baseline Case

In the baseline case, the two hospitals do not share information. We posit that the probability of a breach $I _ { 0 i }$ for hospital i is given by:

$$
I _ {0 i} = B _ {0} - \beta p _ {0 i},\tag{2}
$$

where $B _ { 0 }$ refers to the level of threats in the absence of any security protection for either hospital, and $p _ { 0 i }$ is the protection level of hospital i in the no information sharing case. The amount of expected damage is a function of the breach probability and is given by $\alpha I _ { 0 i }$ where ?? refers to the damage (cost) the hospital would suffer from a security breach. The hospital’s objective function can be written as:

$$
\min _ {p _ {0 i}} R _ {0 i} = \alpha I _ {0 i} + C _ {i} = \alpha (B _ {0} - \beta p _ {0 i}) + \frac {1}{2} c p _ {0 i} ^ {2}\tag{3}
$$

The hospital chooses the level of protection $( p _ { 0 i } )$ that minimizes the total cost $R _ { 0 i }$ . Solving the first-order condition gives the optimal protection level in equilibrium:

$$
p _ {0 i} ^ {*} = \frac {\alpha \beta}{c}\tag{4) \( ^{6} \}
$$

The breach probability in the baseline case is:

$$
I _ {0 i} ^ {*} = B _ {0} - \frac {\alpha \beta^ {2}}{c}\tag{5}
$$

## A Case with Information Exchange

Next, we examine the case where the two hospitals agree to exchange their information via an HIE. After a hospital joins an HIE, its data breach risk may increase or decrease. On the one hand, the HIE governance may improve the hospital’s security protection and thereby lower its data breach risk. On the other hand, joining an HIE may increase the hospital’s data breach risk by introducing technical changes.

To further investigate the equilibrium of security outcomes, we need to examine the hospital’s cybersecurity investment choice given the decision in the exchange case.

In this scenario, the probability of an intrusion into one hospital depends on its risk $( p _ { 1 i } , i \in ( A , B ) )$ , its security level, and the interdependent risk associated with its counterpart. Specifically, in the two-hospital network, Hospital $\mathbf { A } ^ { * } \mathbf { s }$ security breach is likely to be associated with Hospital B because of the data exchange between them. Although this type of risk is extensively examined in the network setting (Acemoglu et al., 2016; Lee et al., 2016), the roles of governance and operational risk are seldom examined. First, since the ex ante risk is recognized, stakeholders, including HIE organizations and hospital administrators, will design and enforce a governance framework to control the risk. As discussed in the HIEs’ Data Security Governance section, anecdotal evidence supports that HIE governance includes security policies, accountability, and IT standards. Therefore, we consider how the effectiveness of HIE governance (??) can enhance the hospital’s protection and lower the indirect risk. Second, operational risk increases after a hospital joins an HIE, as discussed in the Data Breach Risk of Joining an HIE section. Therefore, we introduce Assumption 1 to account for the fact that the hospitals’ data volume and access will increase after the data exchange because each hospital will store data from both hospitals.

Taking all these attack possibilities into account, we characterize the probability of intrusion for Hospitals A and B in the presence of information exchange as follows:

$$
I _ {1 i} = B _ {1} - \left(\beta p _ {1 i} + \gamma p _ {1 i} p _ {1 j}\right) (i, j \in \{A, B \})\tag{6}
$$

Here $B _ { 1 }$ refers to the level of threat in the absence of any security protection, as in Equation (2).

???????????????????? ??: ??<sub>1</sub> > ??<sub>0</sub>

In Equation (6), the second term, $\beta p _ { 1 i }$ , denotes the prevention of direct attacks against Hospitals A and B. The third term, $\gamma p _ { 1 i } p _ { 1 j }$ , indicates the prevention of an indirect attack on the system of Hospital A through Hospital B or vice versa. Suppose Hospital B has low protection (low $p _ { 1 B } )$ and fails to deter attacks. In that case, Hospital A can still prevent an indirect attack through Hospital B by raising its protection level (high $p _ { 1 A } )$ , such as by deploying effective data segmentation or access control techniques.

In equilibrium, both hospitals choose a positive level of protection in equilibrium. As in the baseline case, each organization determines the protection level $( \mathbf { \nabla } p _ { 1 i } \mathbf { \nabla } )$ that minimizes the sum of the expected damage $( \alpha p _ { 1 i } )$ and the protection cost $( C _ { i } )$

$$
\underset {p _ {1 i}} {\mathrm{Min}} R _ {1 i} = \alpha I _ {1 i} + C _ {i} = \alpha \big (B _ {1} - \beta p _ {1 i} - \gamma p _ {1 i} p _ {1 j} \big) + \frac {1}{2} c p _ {1 i} ^ {2}\tag{7}
$$

Solving the first-order conditions results in a Nash equilibrium for the security protection level of two hospitals, and we obtain:

$$
p _ {1 i} ^ {*} = \frac {\alpha \beta}{c - \alpha \gamma}\tag{8) \( ^{7} \}
$$

In that case, the breach probability is:

$$
I _ {1 i} ^ {*} = B _ {1} - \frac {\alpha \beta^ {2} c}{(c - \alpha r) ^ {2}}\tag{9}
$$

## Comparison of the Two Cases

Lemma 1: After establishing information exchange, both hospitals will increase the level of security protection, as given by $p _ { 1 i } ^ { * } > p _ { 0 i } ^ { * }$

Comparing Equation (4) $( p _ { 0 i } ^ { * } = \frac { \alpha \beta } { c } )$ and Equation (8) $( p _ { 1 i } ^ { * } =$ $\frac { \alpha \beta } { c - \alpha \gamma } ) .$ , we can see that the hospital increases its security protection investment. We also find that:

$$
\frac {\partial p _ {1} (*)}{\partial \gamma} = \frac {\alpha^ {2} \beta}{(c - \alpha \gamma) ^ {2}}.\tag{10}
$$

In other words, the more effective the HIE governance (??) is in improving protection against indirect attacks, the higher the level of protection the hospital is incentivized to pursue. Next, we explore how joining an HIE affects the data breach risk by comparing the predicted probability of intrusions $( { { I } _ { 0 i } ^ { * } }$ and $I _ { 1 i } ^ { * }$ ); we find that the change is:

$$
I _ {1 i} ^ {*} - I _ {0 i} ^ {*} = B _ {1} - \frac {\alpha \beta^ {2} c}{(c - \alpha r) ^ {2}} - B _ {0} + \frac {\alpha \beta^ {2}}{c}
$$

Lemma 2: After establishing information exchange between the two hospitals, the probability of a data breach will decrease $( I _ { 1 i } ^ { * } < I _ { 0 i } ^ { * } )$ if and only if the effectiveness of governance $( \gamma )$ is sufficiently high (i.e., $\gamma > \frac { ( c ) \left( 1 - \frac { \beta \sqrt { \alpha H } } { H } \right) } { \alpha } \ : ,$ where $H = \alpha \beta ^ { 2 } +$ $( B _ { 1 } - B _ { 0 } ) c .$

<table><tr><td colspan="2">Table 1. A Summary of Lemmas</td></tr><tr><td>Number</td><td>Lemma</td></tr><tr><td>1</td><td>After joining HIE, a hospital increases IT security investment.</td></tr><tr><td>2</td><td>Joining HIE may or may not decrease the data breach risk.</td></tr><tr><td>3a</td><td>If joining HIE lowers the data breach risk, the impact would be reduced for hospitals with a higher unit cost of protection.</td></tr><tr><td>3b</td><td>If joining HIE lowers the data breach risk, the impact would be enhanced when the effectiveness of IOS governance increases.</td></tr><tr><td>4a</td><td>If joining HIE increases the data breach risk, the impact would be enhanced on hospitals with a higher unit cost of protection.</td></tr><tr><td>4b</td><td>If joining HIE increases the data breach risk, the impact would be reduced when the effectiveness of IOS governance increases.</td></tr></table>

According to this lemma, the hospital’s data breach risk will decrease if HIE governance is adequately effective (high γ). There are two channels through which the effect is realized. First, HIE governance directly reduces the risk of an indirect attack (via the HIE) given the same protection level. Second, it incentivizes hospitals to increase their security protection levels, leading to a decrease in the risk of a direct attack.

Next, we explore the second question: How do hospital-level factors (i.e., the unit cost of protection) and governancelevel factors (i.e., the effectiveness of governance) affect the change in data breach risk? Specifically, we examine how the focal hospital’s unit cost of security protection (??) and the effectiveness of governance (??) affect the change in the probability of data breach risk $( I _ { 1 i } ^ { * } - I _ { 0 1 } ^ { * } )$ . Based on previous results, we derive the following lemmas:

Lemma 3: If the breach risk decreases after the exchange of information $( I _ { 1 i } - I _ { 0 i } < 0 )$

(a) the magnitude of the decrease will be negatively associated with the hospital’s unit cost of protection (??) $\begin{array} { r } { ( i . e . , \frac { \partial | I _ { 1 i } ^ { * } - I _ { 0 i } ^ { * } | } { \partial c } < 0 ) } \end{array}$ , and (b) the magnitude of the decrease will be positively associated with the effectiveness of HIE governance $\begin{array} { r } { \left( \gamma \right) ( i . e . , \frac { \partial | I _ { 1 i } ^ { * } - I _ { 0 i } ^ { * } | } { \partial r } > 0 ) } \end{array}$

Lemma 4: If the breach risk increases after the exchange of information $( I _ { 1 i } - I _ { 0 i } > 0 )$

(a) the magnitude of the increase will be positively associated with the hospital’s unit cost of protection (??) $\begin{array} { r } { ( i . e . , \frac { \partial | I _ { 1 i } ^ { * } - I _ { 0 i } ^ { * } | } { \partial c } > 0 ) , } \end{array}$ , and (b) the magnitude of the decrease will be negatively associated with the effectiveness of HIE governance $\begin{array} { r } { ( \gamma ) ( i . e . , \frac { \partial | I _ { 1 i } ^ { * } - I _ { 0 i } ^ { * } | } { \partial r } < 0 ) } \end{array}$

In the case where a hospital’s data breach risk decreases, two key variables determine the extent of the risk reduction: the unit cost of protection ( ?? ) and the effectiveness of HIE governance (??). According to Lemma 3a, if a hospital has a lower unit cost of data protection, the benefits of reduction in loss due to a data breach will outweigh the data protection expenditure. Therefore, the hospital will prefer to allocate more resources to data protection, leading to a larger magnitude decrease in breach risk. Furthermore, Lemma 3b reveals the importance of effectively reducing interdependent risk, as more effective link protection results in a more substantial decrease in individual hospitals’ breach risk. Effective governance can reduce the indirect risk and internalize the losses of data breaches, thereby leading the focal hospital to increase data protection spending and improve its security.

Additionally, if joining an HIE increases a hospital’s data breach risk, the magnitude of the increase is positively associated with the hospital’s unit cost of security (Lemma 4a) and negatively associated with the effectiveness of HIE governance (Lemma 4b). We paraphrase all lemmas and summarize them in Table 1. To substantiate the practical implications of the proposed lemmas, it is necessary to test them in real-world settings. Therefore, we employed empirical approaches, as described in the next section.

## Data Description

To empirically analyze the main research questions, we constructed a six-year (2010-2015) panel dataset of more than 3,000 hospitals in the United States. We chose 2010 as the starting year of our analyses because data breach incidents were more likely to be reported after that time. The shift is attributed to the enactment of several health data breach notification laws as part of the American Recovery and Reinvestment Act of 2009. These laws include the Federal Trade Commission (FTC) Health Breach

Notification Rule<sup>8</sup> and the Department of Health and Human Services (HHS) Breach Notification for Unsecured Protected Health Information.<sup>9</sup> Additionally, the earliest reported date of breach incidents in the official HHS breach portal is October 2009. <sup>10</sup> These factors ensure that data from 2010 onward capture a comprehensive overview of hospital breach incidents.

We collected data from multiple sources, including (1) security breaches from the Privacy Rights Clearinghouse and the U.S. Department of Health and Human Services (HHS) breach portal, (2) hospitals’ organizational characteristics and IT practices from HIMSS Analytics data, (3) health referral region characteristics from the Dartmouth Health Atlas, and (4) regional population and economic data from the U.S. Bureau of Labor Statistics. We report the main variables’ summary statistics in Table 2 and their correlation matrix in Table A1 of the Appendix.

## Outcome and Treatment Variables

The main outcome variable in our study is the occurrence of data breach incidents. We collected hospitals’ security breach incidents from two sources—the Privacy Rights Clearing House and the U.S. Department of Health and Human Services (HHS)—which have been commonly used in previous data breach research (e.g., Kim & Kwon, 2019; Kwon & Johnson, 2018; Angst et al., 2017a). The dataset provides detailed information on each incident, including breached hospital names and breach dates. After merging the hospital and breach incident data, we can identify each breached hospital.

The treatment variable is HIE status, which indicates whether a hospital has joined an HIE. We obtained the HIE data from the HIMSS Analytics database, which is widely used in health IT studies. (e.g., Angst et al., 2017a; Kwon & Johnson, 2014; Miller & Tucker, 2009). We collected data on hospitals’ HIE statuses from the dataset similar to previous studies (e.g., Ayer et al., 2019; Atasoy et al., 2018). The dataset features a binary indicator for whether a hospital has joined an HIE.<sup>11</sup> Figure 1 shows the state-level participation rates of HIEs in 2010 and 2015. The change in hospitals’ HIE status constitutes the main variation in our analyses.

## Control Variables

We collected data on hospitals’ characteristics and regional characteristics that are likely to affect a hospital’s propensities to join an HIE and its susceptibility to data breaches. Hospitals’ basic organizational information includes the number of beds in a hospital’s health system, total operating expenses, total payroll expenses, and total admissions. Hospitals’ IT characteristics include the number of live IT applications, clinical IT applications (such as management, laboratory, nursing, pharmacy, radiology & PACS, ED/operating rooms/respiratory, and clinical systems apps), strategy IT applications, and advanced electronic medical record systems, which include the adoption of computerized provider order entry (CPOE) and physician documentation. These categorizations of HIT applications have also been used in previous studies (Hydari et al., 2018; Kwon & Johnson, 2018; Dranove et al., 2014; Miller & Tucker, 2011b). Additionally, we captured whether a hospital has plans to revamp its IT systems. Lastly, we implicitly captured the impact of previous breaches by controlling for hospitals’ operating expenses and the number of adopted IT apps because breach incidents act as shocks to hospitals’ financial performance and IT strategies (Seh et al., 2020).<sup>12</sup>

In addition to hospitals’ characteristics, regional characteristics are also relevant factors that may influence HIE participation and data breach risk, such as competition, healthcare service complexity, and economic conditions. Some regional shocks, such as policy interventions or economic recessions, could influence the establishment of HIE and hospitals’ strategies at the same time. To capture these dynamics, we considered related characteristics at the hospital referral region (HRR) level as a regional healthcare market (Adjerid et al., 2018). We obtained HRR data from the Dartmouth Health Atlas and identified 306 HRRs across the U.S. We constructed an HRR-level Herfindahl-Hirschman Index to proxy for competition, following previous studies (Gaynor et al., 2012). Furthermore, we captured healthcare complexity by using the HRR Case Mix Index from Dartmouth Health Atlas.<sup>13</sup> Lastly, we incorporated HRR-level per capita income, population, and capital unemployment percentage using data from the U.S. Department of Housing and Urban Development (HUD) and the Census Bureau. Specifically, we used two cross-walk files provided by the Dartmouth Health Atlas and HUD to map zipcode, county, and HRR and then calculated a weighted average for those variables (Adjerid et al., 2018; Fu et al., 2013).

![](/api/attachments/7TTMQQGR/fulltext/images/c61669ebac0ff105952bbbae7fea3eae54524fe64928fb764c13ba3ef4857890.jpg)

<table><tr><td colspan="5">Table 2. Summary Statistics of Main Variables</td></tr><tr><td>Variable</td><td>Description (hospital i, hospital referral region h, state s at year t)</td><td>Mean</td><td>SD</td><td>Sources</td></tr><tr><td colspan="5">Outcome variables</td></tr><tr><td> $Data\text{Breach}_{it}$ </td><td>Binary indicator for whether a hospital i experiences data breaches at year t</td><td>0.0441</td><td>0.2052</td><td>Privacy Rights Clearinghouse, HHS breach portal</td></tr><tr><td colspan="5">Treatment variable</td></tr><tr><td> $Join\text{HIE}_{it}$ </td><td>Binary indicator for whether a hospital i joins an HIE at year t</td><td>0.4148</td><td>0.4927</td><td>HIMSS</td></tr><tr><td colspan="5">Other variables</td></tr><tr><td> $Size_{it}$ </td><td>Log of the number of beds in a health system size</td><td>6.7723</td><td>2.1222</td><td>HIMSS</td></tr><tr><td> $Operation\text{Expense}_{it}$ </td><td>Log of the total amount of operational expenses</td><td>18.0126</td><td>1.3914</td><td>HIMSS</td></tr><tr><td> $Payroll\text{Expenses}_{it}$ </td><td>Log of the total amount of payroll expenses</td><td>17.0857</td><td>1.3682</td><td>HIMSS</td></tr><tr><td> $IT\text{Apps}_{it}$ </td><td>Log of the total number of live apps</td><td>4.0856</td><td>0.4005</td><td>HIMSS</td></tr><tr><td> $Strategy\text{Apps}_{it}$ </td><td>The total number of live strategy apps</td><td>10.9638</td><td>4.2030</td><td>HIMSS</td></tr><tr><td> $Clinic\text{Apps}_{it}$ </td><td>The total number of live clinical apps</td><td>22.1942</td><td>8.8576</td><td>HIMSS</td></tr><tr><td> $Advanced\text{EMR}_{it}$ </td><td>The adoption of advanced electronic medical record apps</td><td>1.1246</td><td>0.9003</td><td>HIMSS</td></tr><tr><td> $IS\text{Plan}_{it}$ </td><td>Binary indicator for whether a hospital has information system strategic plans</td><td>0.7072</td><td>0.4551</td><td>HIMSS</td></tr><tr><td> $Total\text{Admission}_{it}$ </td><td>Log of the total admission</td><td>8.0024</td><td>1.5570</td><td>HIMSS</td></tr><tr><td> $HHI_{ht}$ </td><td>The competition index (HRR)</td><td>7.2148</td><td>0.7548</td><td>Dartmouth Health Atlas</td></tr><tr><td> $CMI_{ht}$ </td><td>The case mix index (HRR)</td><td>1.4825</td><td>0.1437</td><td>Dartmouth Health Atlas</td></tr><tr><td> $Income_{ht}$ </td><td>Log of per capita income (HRR)</td><td>16.0884</td><td>1.4381</td><td>HUD, Census Bureau</td></tr><tr><td> $Unemployment_{ht}$ </td><td>Unemployment percentage (HRR)</td><td>7.5748</td><td>2.3304</td><td>HUD, Census Bureau</td></tr><tr><td> $Population_{ht}$ </td><td>Log of population (HRR)</td><td>12.3197</td><td>1.3475</td><td>HUD, Census Bureau</td></tr><tr><td> $HIE\text{Security Laws}_{st}$ </td><td>Binary indicator for whether a state enacted HIE security-related laws</td><td>0.2236</td><td>0.4167</td><td>State Health IT Policy Levers Compendium, Health Privacy Project</td></tr><tr><td> $MSA_i$ </td><td>Binary indicator for whether a hospital is in a metropolitan area</td><td>0.6845</td><td>0.4647</td><td>HIMSS</td></tr><tr><td> $Academic_i$ </td><td>Binary indicator for whether a hospital is academic</td><td>0.0467</td><td>0.2111</td><td>HIMSS</td></tr><tr><td> $ForProfit_i$ </td><td>Binary indicator for whether a hospital is for-profit</td><td>0.1881</td><td>0.3908</td><td>HIMSS</td></tr></table>

![](/api/attachments/7TTMQQGR/fulltext/images/267331181f8d93748f488f59a791829bb1a3901843035f1dc1c59d878137be74.jpg)  
Figure 1. HIE State-Level Participation Rates

## Research Design

Our primary goal is to empirically examine how joining an HIE affects the likelihood that a hospital will experience a data breach. To ensure rigor and mitigate potential biases, we address this question by designing and using three main approaches: difference-in-differences, matching, and instrumental variables analyses.

## Difference-in-Differences

First, we used hospitals’ staggered HIE adoptions as a quasiexperiment setting and evaluated the effect with a difference-indifferences (DiD) approach. We estimated linear probability models (LPM) with two-way fixed effects for two primary reasons. First, LPM enabled us to avoid an incidental parameters problem that causes inconsistency in a nonlinear model with fixed effects (Miller & Tucker, 2009). Second, the results are generally consistent with estimates in nonlinear models and are more interpretable (Angrist & Pischke, 2009). The specification of the baseline model is as follows:

$$
D a t a B r e a c h _ {i t} = f (J o i n H I E _ {i t}, X _ {i t}, \gamma_ {i}, \mu_ {t}, \epsilon_ {i t})
$$

In this specification, the outcome variable ?????????????????? $h _ { i t }$ indicates whether hospital ?? experienced at least one security breach in year ??. Our primary variable of interest is $J o i n H I E _ { i t } ,$ which captures whether hospital ?? is a member of an HIE in year ??. Furthermore, we incorporated a vector of time-varying characteristics of hospitals $X _ { i t }$ . To control for time-invariant heterogeneity across different hospitals and time trends, we used hospital fixed effects $( \mathrm { i . e . , } \gamma _ { i } )$ and a year fixed effect (i.e., ${ \mu } _ { t } ~ )$ . Lastly, $\epsilon _ { i t }$ represents independently and identically distributed errors. We report standard errors clustered at the hospital level since the common practice is to cluster at the unit where the treatment was assigned (Abadie et al., 2023).<sup>14</sup>

Recent studies highlight a potential issue in time-varying treatment DiD analyses with two-way fixed effects (Baker et al., 2022; Goodman-Bacon, 2021; Callaway & Sant’Anna, 2020). The estimator for the two-way fixed effects model is a weighted average of all possible 2×2 DiD estimators. However, the variation in treatment effects across time may bias the estimates. Specifically, units in Timing groups, who received treatment at different times, may serve as each other’s control groups or as treated groups. The comparison could potentially bias the result (Baker et al., 2022).

To test the validity of our DiD, we used the Bacon decomposition to identify the weights of the estimated effect (Goodman-Bacon et al., 2019). Our results, presented in Table 3 and Figure 2, include several main comparisons between different groups: namely Timing, Always vs. Timing, Never vs. Timing, and Always vs. Never.<sup>15</sup> We report three main findings that confirm the appropriateness of our estimated treatment effect. First, more than 50% of the estimated treatment effects are from the Never vs. Timing group comparison, which is a reasonable comparison between treated units (Timing) and control units (Never). Second, the magnitude of the Never vs. Timing group treatment effect is similar to the average treatment effect in our main model. Third, the weight of the Timing groups is fairly low (0.064), suggesting that the variation in treatment effects did not substantially bias our results. In summary, these results alleviate the concern that the DiD estimate is biased in our setting.

## Matching Strategies

In our context, self-selection is a major concern because hospitals can choose whether to join an HIE. In other words, there could be many hospital-level confounding factors. For instance, hospitals’ governance structures can affect digitization decisions, confounding the HIE’s impact on data breach risk. To alleviate endogeneity concerns, we use matching strategies commonly implemented in empirical studies in healthcare (Sun et al., 2020; Ayer et al., 2019; Kwon & Johnson, 2018). Matching is useful in the healthcare context where significant disparities exist among U.S. hospitals in terms of financial performance and digital capabilities. Effective matching can construct a sample with a “better balance between the treated and control groups” (Iacus et al., 2012, p. 1). In our case, the treatment assignment (i.e., Joining HIE) should resemble a randomized experiment after effective matching.

We used propensity score matching (PSM) to leverage observable covariates to identify a nontreated unit (i.e., not in an HIE) that would have been likely to be treated (i.e., in an HIE). These covariates include the hospital’s basic characteristics, IT practices, and IT security capability. We used the pretreated mean of those covariates to estimate the hospital’s propensity score of joining an HIE. We also incorporated variables that did not change over time for most

Always vs never treated = -9.1692896 (weight = .00762645)

hospitals, including $M S A _ { i }$ (a hospital in a metropolitan statistical area), ???????????????? (a hospital focused more on academic research and teaching), $F o r P r o f i t _ { i }$ (a for-profit hospital), and ???????????????????????? (a hospital affiliated with a multihospital health system) since these are essential factors in hospitals’ health IT strategies (Angst et al., 2017b).

Next, we keep observations that are matched based on propensity scores. We performed probit regression and Knearest-neighbor matching (K = 3) with a caliper size of 0.01. This practice yields 1,637 matched hospitals (8,778 observations) and 1,543 unmatched hospitals (8,170 observations). To check the balance of the matched sample, we present descriptive analyses of covariates in Table 4. Before matching, there are substantial differences between the treated group and the control group. Hospitals in HIEs are more likely to be not-for-profit, academic, in metropolitan areas, and have a higher level of digitalization. The outcomes are consistent with the literature on HIE participation (Adler-Milstein & Jha, 2014; Adler-Milstein et al., 2011). After matching, the difference between the treated and control groups is insignificant across all covariates, suggesting that our matching strategies generate a balanced sample. Therefore, our estimation is less likely to be biased after using the matched sample.

## Instrumental Variables

To complement the DiD and matching strategies, we employed instrumental variables (IVs) and two-stage least square estimations to examine the impact of HIE on hospitals’ data breach occurrence. Similar to previous studies (e.g., Miller & Tucker, 2009; Angrist & Pischke, 2008), we used a linear probability model with IVs. We chose two regional-level variables as instruments based on the assumption that they exert a strong impact on HIE participation and satisfy the exclusion restriction.

<table><tr><td colspan="3">Table 3. Bacon Decomposition Results</td></tr><tr><td>Groups</td><td>Coeff.</td><td>Weight</td></tr><tr><td>Timing groups</td><td>-0.003</td><td>0.064</td></tr><tr><td>Always vs. Timing</td><td>-0.029</td><td>0.382</td></tr><tr><td>Never vs. Timing</td><td>-0.029</td><td>0.546</td></tr><tr><td>Always vs. Never</td><td>-9.169</td><td>0.000</td></tr><tr><td>Within</td><td>-0.020</td><td>0.008</td></tr></table>

![](/api/attachments/7TTMQQGR/fulltext/images/d77548b6eae9220030191324fd5291b152da56023513d615382a2af08bda92f7.jpg)  
Overall DD Estimate = -.02803842

<table><tr><td colspan="9">Table 4. Propensity Score Matching: Descriptive Analyses</td></tr><tr><td></td><td colspan="4">Before matching</td><td colspan="4">After matching</td></tr><tr><td>Variable</td><td>Treated mean</td><td>Control mean</td><td>Bias%</td><td>p-value</td><td>Treated mean</td><td>Control mean</td><td>Bias%</td><td>p-value</td></tr><tr><td>Health system size</td><td>6.76</td><td>6.84</td><td>-3.90</td><td>0.39</td><td>6.71</td><td>6.72</td><td>-0.50</td><td>0.92</td></tr><tr><td>Operating expenses</td><td>18.13</td><td>17.70</td><td>33.90</td><td>0.00</td><td>18.08</td><td>18.09</td><td>-1.00</td><td>0.97</td></tr><tr><td>Payroll expense</td><td>17.23</td><td>16.77</td><td>36.20</td><td>0.00</td><td>17.17</td><td>17.19</td><td>-1.30</td><td>0.80</td></tr><tr><td>Total admission</td><td>8.14</td><td>7.73</td><td>28.40</td><td>0.00</td><td>8.10</td><td>8.14</td><td>-2.90</td><td>0.57</td></tr><tr><td>IT apps</td><td>4.12</td><td>3.99</td><td>42.70</td><td>0.00</td><td>4.11</td><td>4.10</td><td>2.30</td><td>0.63</td></tr><tr><td>IT security apps</td><td>3.80</td><td>3.93</td><td>-8.50</td><td>0.05</td><td>4.11</td><td>4.11</td><td>-0.10</td><td>0.98</td></tr><tr><td>strategy apps</td><td>11.21</td><td>9.81</td><td>40.60</td><td>0.00</td><td>10.95</td><td>10.94</td><td>0.30</td><td>0.95</td></tr><tr><td>clinical apps</td><td>22.77</td><td>19.68</td><td>39.70</td><td>0.00</td><td>22.49</td><td>22.63</td><td>-1.90</td><td>0.70</td></tr><tr><td>Advanced EHR</td><td>1.38</td><td>1.30</td><td>15.70</td><td>0.00</td><td>1.05</td><td>1.10</td><td>-8.10</td><td>0.10</td></tr><tr><td>IS plan</td><td>0.73</td><td>0.67</td><td>15.30</td><td>0.00</td><td>0.72</td><td>0.71</td><td>3.40</td><td>0.51</td></tr><tr><td>MSA</td><td>0.72</td><td>0.64</td><td>17.80</td><td>0.00</td><td>0.71</td><td>0.68</td><td>6.50</td><td>0.20</td></tr><tr><td>Academic</td><td>0.05</td><td>0.02</td><td>15.80</td><td>0.00</td><td>0.03</td><td>0.04</td><td>-5.50</td><td>0.31</td></tr><tr><td>For-profit</td><td>0.14</td><td>0.34</td><td>-48.20</td><td>0.00</td><td>0.15</td><td>0.13</td><td>4.40</td><td>0.29</td></tr><tr><td>System member</td><td>0.64</td><td>0.64</td><td>-0.70</td><td>0.87</td><td>0.63</td><td>0.63</td><td>-0.60</td><td>0.90</td></tr><tr><td>Competition</td><td>7.20</td><td>7.25</td><td>-6.40</td><td>0.15</td><td>7.22</td><td>7.16</td><td>8.30</td><td>0.11</td></tr></table>

The first instrument is the percentage of hospitals joining HIEs in hospital referral regions (HRRs). The rationales are threefold. First, the HIE participation ratio can capture regional-level incentives that motivate hospitals to join HIEs (Rudin et al., 2014; Ross et al., 2010). Second, HIEs exhibit network effects such that the value of an HIE increases as more hospitals join that HIE (Demirezen et al., 2016; Miller & Tucker, 2014). Third, the instrument represents the normative pressure facilitating HIE participation (Hsu et al., 2012; Robey et al., 2008). Hence, the instrument should be positively associated with a hospital’s likelihood of joining an HIE. At the same time, the exclusion restriction is satisfied because HIE participation in a region is unlikely to be directly correlated with a hospital’s data breach risk, conditional on the hospital’s and the HRR’s characteristics. It could be asked if the instrument might affect breach risk through communication channels and mutual learning among hospitals in the same HRR. However, if that were the case, we would expect the instrument to be negatively associated with the breach risk of no-HIE hospitals. We empirically tested this argument by regressing the instrument on the breach occurrences of no-HIE hospitals and did not find a significant association.<sup>16</sup> Therefore, HIE participation is likely the only channel through which the instrument affects a hospital’s data breach risk.

The second instrument is the number of health systems in the HRR. A health system consists of two or more healthcare provider organizations that have common ownership or cooperate closely (AHRQ, 2017). Some well-known healthcare systems include the Mayo Clinic, HealthOne, and Allina Health. A hospital in an HHR with more unique health systems is less likely to join HIE, mainly because system fragmentation in the local healthcare market is positively associated with the coordination costs of HIE organizations because of different policies and operations. Furthermore, different health systems are likely to adopt health IT from various vendors, making it challenging to achieve interoperability (Everson & Adler-Milstein, 2016). It could be questioned whether the instrument might impact the demand for healthcare services, thereby affecting hospitals security strategies. To test this, we examined if healthcare services demand, measured by the Case Mix Index and total Medicare reimbursements per enrollee in the HRR affected hospitals’ breach likelihoods. <sup>17</sup> The results do not show significant relationships, suggesting that the instrument meets the exclusion restriction criteria. In the HIE and Data Breaches section, we provide detailed explanations and evidence supporting the validity of the instrumental variables. The next section presents the main findings based on these main identification strategies.

## Analyses

In this section, we empirically analyze the lemmas from our analytical model, as presented in Table 1.

## HIE and IT Security Investment

Lemma 1 posits that hospitals will increase IT security investment after joining an HIE. We aim to verify the validity of this lemma using our data. Therefore, it is critical to know the amount of investment a hospital makes in IT security. Following the approach commonly used in organizational IT security studies (Angst et al., 2017a; Kwon & Johnson, 2014), we used the number of adopted IT security applications as a proxy for IT security investments. The IT security applications in the HIMSS database include encryption, firewall, single sign-on, spam/spyware filter, fingerprint scanning, and 10 other applications, which we use to operationalize IT security investments.<sup>18</sup>

Considering that the outcome is a count variable, we examined two types of estimators. We first used OLS to estimate the impact of joining an HIE on the number of adopted IT security applications. We further used a Poisson quasi-maximum likelihood estimator (PQML), which is commonly used in estimating outcomes as count variables (Dobkin et al., 2018; Greenwood & Wattal, 2017). This method allows for the creation of robust standard errors and does not require that the dependent variable’s distribution be Poisson or negative binomial.<sup>19</sup> The results in Table 5 indicate that the coefficient of Join HIE is significantly positive, suggesting that hospitals adopt more IT security applications after joining an HIE and providing support for Lemma 1. However, it’s important to note that increasing IT security investment does not necessarily lead to better security performance. As our theoretical model suggests, security threats increase after a hospital joins an HIE. Even though a hospital adopts more security applications, the increased protection may not offset the heightened threats. Therefore, it is critical to empirically test how joining an HIE affects the hospital’s data breach risk.

## HIE and Data Breaches

According to Lemma 2 in our theoretical model, joining an HIE may or may not increase the data breach risk depending on the effectiveness of HIE governance. We present our empirical findings in Table 6. The results indicate significant negative coefficients of HIE participation. Specifically, in Column 1, we give the total sample without control variables. Column 2 shows that the results of a model with all control variables are similar to those in Column 1. In Column 3, we report the results of using the matched sample to estimate the main effect. Using PSM (K = 3), <sup>20</sup> we obtained 8,778 matched observations. We observe R-squared increases in the matched sample, demonstrating model fitness improvement. Column 3 shows that the coefficient of ???????????????? is –0.0156, suggesting that the data breach likelihood decreases by 1.56 percentage points if a hospital joins an HIE. Considering that the mean value of the data breach indicator in our sample is 0.0441, the magnitude of reduction is around 35.37% (0.0156/0.0441 = 0.3537).

<table><tr><td colspan="3">Table 5. HIE&#x27;s Impact on IT Security Investment</td></tr><tr><td rowspan="2">DV: No. IT security applications</td><td>(1)</td><td>(2)</td></tr><tr><td>OLS</td><td>PQML</td></tr><tr><td>Join HIE</td><td>0.2898***(0.0607)</td><td>0.0370**(0.0121)</td></tr><tr><td>R-squared / log-likelihood</td><td>0.791</td><td>-9458.761</td></tr><tr><td>Observations</td><td>7941</td><td>7941</td></tr><tr><td>No. hospitals</td><td>1627</td><td>1627</td></tr><tr><td>Hospital &amp; year FE</td><td>YES</td><td>YES</td></tr><tr><td>Control variables</td><td>YES</td><td>YES</td></tr></table>

Note: All estimations used cluster-adjusted robust standard errors (clustered at the hospital level). We used a matched sample in these analyses (we elaborate on how to choose a matched sample in the Matching Strategies section). \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, +p < 0.1

<table><tr><td colspan="7">Table 6. HIE&#x27;s Impact on Data Breach Occurrence</td></tr><tr><td>DV:</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td></td><td colspan="3">DiD analyses</td><td colspan="3">IV analyses</td></tr><tr><td>Data Breach occurrence</td><td>Control Variables</td><td>PSM</td><td>Heterogeneity</td><td>First stage</td><td>Main impact</td><td>Heterogeneity</td></tr><tr><td>Join HIE</td><td>-0.0220***(0.0066)</td><td>-0.0156*(0.0073)</td><td>0.0193(0.0167)</td><td></td><td>-0.0575***(0.0171)</td><td>0.0369(0.0350)</td></tr><tr><td>Join HIE * No. clinical apps</td><td></td><td></td><td>-0.0011+(0.0006)</td><td></td><td></td><td>-0.0199+(0.0111)</td></tr><tr><td>Join HIE * HIE security laws</td><td></td><td></td><td>-0.0219+(0.0121)</td><td></td><td></td><td>-0.0034**(0.0012)</td></tr><tr><td>HRR HIE participation</td><td></td><td></td><td></td><td>0.9647***(0.0344)</td><td></td><td></td></tr><tr><td>HRR unique system</td><td></td><td></td><td></td><td>-0.0063(0.0059)</td><td></td><td></td></tr><tr><td>HIE security laws</td><td></td><td></td><td>0.0014(0.0092)</td><td>-0.0073(0.0142)</td><td></td><td></td></tr><tr><td>Health system size</td><td>0.0202***(0.0036)</td><td>0.0242***(0.0052)</td><td>0.0248***(0.0052)</td><td>-0.0148**(0.0055)</td><td>0.0199***(0.0036)</td><td>0.0206***(0.0037)</td></tr><tr><td>Operation expense</td><td>0.0227+(0.0137)</td><td>0.0084(0.0147)</td><td>0.0090(0.0147)</td><td>-0.0073(0.0142)</td><td>0.0221(0.0137)</td><td>0.0214(0.0136)</td></tr><tr><td>Payroll expense</td><td>-0.0283*(0.0112)</td><td>-0.0060(0.0099)</td><td>-0.0056(0.0098)</td><td>-0.0097(0.0106)</td><td>-0.0289*(0.0113)</td><td>-0.0277*(0.0112)</td></tr><tr><td>IT apps</td><td>-0.0052(0.0187)</td><td>0.0554*(0.0257)</td><td>0.0529*(0.0259)</td><td>0.1397***(0.0330)</td><td>0.0003(0.0187)</td><td>-0.0110(0.0192)</td></tr><tr><td>Strategy apps</td><td>0.0018(0.0016)</td><td>-0.0031+(0.0019)</td><td>-0.0030(0.0019)</td><td>-0.0049*(0.0021)</td><td>0.0015(0.0016)</td><td>0.0019(0.0016)</td></tr><tr><td>Clinical apps</td><td>-0.0001(0.0007)</td><td>-0.0002(0.0010)</td><td>0.0000(0.0010)</td><td>-0.0014(0.0012)</td><td>-0.0002(0.0007)</td><td>0.0018+(0.0009)</td></tr><tr><td>Advanced EHR</td><td>-0.0026(0.0041)</td><td>0.0005(0.0053)</td><td>0.0005(0.0053)</td><td>0.0050(0.0057)</td><td>-0.0025(0.0041)</td><td>-0.0027(0.0041)</td></tr><tr><td>IS plan</td><td>-0.0114(0.0080)</td><td>-0.0270**(0.0101)</td><td>-0.0270**(0.0101)</td><td>0.0009(0.0117)</td><td>-0.0118(0.0080)</td><td>-0.0137+(0.0081)</td></tr><tr><td>Total admission</td><td>-0.0059(0.0076)</td><td>-0.0143*(0.0068)</td><td>-0.0139*(0.0068)</td><td>0.0116(0.0107)</td><td>-0.0051(0.0076)</td><td>-0.0037(0.0075)</td></tr><tr><td>Competition</td><td>-0.0514*(0.0217)</td><td>-0.0701*(0.0273)</td><td>-0.0691*(0.0274)</td><td>0.0086(0.0472)</td><td>-0.0532*(0.0219)</td><td>-0.0533*(0.0219)</td></tr><tr><td>HRR CMI</td><td>-0.0269(0.0375)</td><td>-0.0774+(0.0449)</td><td>-0.0806+(0.0451)</td><td>0.0265(0.0660)</td><td>-0.0312(0.0377)</td><td>-0.0333(0.0377)</td></tr><tr><td>HRR personal income</td><td>0.1793*(0.0748)</td><td>0.1020(0.0916)</td><td>0.1030(0.0913)</td><td>-0.0313(0.1018)</td><td>0.1820*(0.0749)</td><td>0.1776*(0.0750)</td></tr><tr><td>HRR unemployment</td><td>-0.0045+(0.0024)</td><td>0.0018(0.0030)</td><td>0.0017(0.0030)</td><td>0.0010(0.0044)</td><td>-0.0045+(0.0024)</td><td>-0.0048+(0.0024)</td></tr><tr><td>HRR population</td><td>-0.1837*(0.0919)</td><td>-0.1303(0.1132)</td><td>-0.1320(0.1128)</td><td>0.0013(0.1243)</td><td>-0.1847*(0.0918)</td><td>-0.1867*(0.0919)</td></tr><tr><td>R-squared</td><td>0.277</td><td>0.326</td><td>0.327</td><td>/</td><td>/</td><td>/</td></tr><tr><td>Observations</td><td>16948</td><td>8778</td><td>8778</td><td>16948</td><td>16948</td><td>16948</td></tr><tr><td>No. hospitals</td><td>3180</td><td>1637</td><td>1637</td><td>3180</td><td>3180</td><td>3180</td></tr><tr><td>Hospital &amp; year FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr></table>

Note: All estimations used cluster-adjusted robust standard errors (clustered at the hospital level). For Columns 5 and 6, the LM-statistic are 393 and 105, the Hansen J statistics are 0.367 and 4.910, and the Hansen J p-values are 0.545 and $0 . 1 7 9 . ^ { \star \star \star } p < 0 . 0 0 1 , ^ { \star \star } p < 0 . 0 1 , ^ { \star } p <$ 0.05, +p < 0.1

To test the robustness of our findings, we used a two-stage least squares (2SLS) estimation with IVs. Before presenting the results, we discuss the evidence of IV validity. First, the IVs exerted a substantial impact on HIE participation. The second stage of 2SLS reports that Kleibergen-Paap rk LM statistics are more than 70, which is substantially larger than the rule-of-thumb value of 10 (Staiger & Stock, 1997). Second, the IVs are exogenous. The overidentifying restriction tests show that Hansen J p-values are higher than 0.1, suggesting we cannot reject the hypothesis that IVs are uncorrelated with the residual terms. <sup>21</sup> In Table 6, the IV results in Column 5 are in line with the previous finding that joining an HIE lowers a hospital’s data breach risk. The magnitude of the coefficient is larger than its OLS counterpart for two possible reasons. First, the OLS estimate in DiD may be subject to a downward bias because hospitals that value security tend to be less likely to join HIEs (Mello et al., 2018; Adler-Milstein & Jha, 2014). Second, the 2SLS estimate captures a “local average treatment effect” (LATE) (Angrist et al., 1996). In our context, the LATE captures the impacts of HIE on hospitals that are most responsive to the influence of IVs (i.e., the HRR-level shocks).

## Clinical IT System Complexity

According to Lemma 3a, when a hospital has a higher unit cost of data protection, it is less likely to improve its IT security after joining an HIE. Thus, if a hospital’s unit cost of strengthening IT security is higher, we should observe a weaker impact of HIE participation on the reduction in data breach risk. According to economies of scale and organization learning theory, the unit cost of production should be negatively associated with factors such as scale, specialization, and accumulated experience in the production process (Salomon & Martin, 2008; Stigler, 1958). While we may not directly observe a hospital’s security protection as a production process, we can measure the extent of a hospital’s digitalization and defense needs by measuring the complexity of its clinical IT system. In other words, by considering a hospital’s clinical IT system complexity, we can indirectly assess the requirements and demands placed on its security measures.

As the complexity of a hospital’s IT clinical system increases, the efficiency of the security investment required or recommended by HIE governance also increases for several reasons. First, hospitals with more clinical systems are more likely to take advantage of economies of scale. Those hospitals typically own more protected healthcare data and data access, which can make them more vulnerable to data breaches (Tanriverdi et al., 2019). Therefore, standardized countermeasures are more beneficial for such hospitals. Furthermore, since HIE requires data interoperability, healthcare IT systems in different hospital units should also follow similar standards and protocols. Therefore, hospitals implementing complex clinical IT systems usually achieve more cost-effective investments in data protection. Second, implementing sophisticated digital systems in clinical care allows hospital management and employees to accumulate IT resources and knowledge. Previous experience and related knowledge contribute to better performance in new practices (Roberts et al., 2012; Bharadwaj, 2000; Cohen & Levinthal, 1990). When hospitals face increased threats and new compliance requirements (i.e., joining an HIE in our context), those that are more digitalized are usually more capable of IT process changes. For instance, sharing patient data electronically across hospital units involves data audit and access management (Appari et al., 2009). With the experience and capability from previous practices in clinical IT systems, hospitals are more likely to internalize the new data protection countermeasures introduced by HIE governance.

To examine the role of clinical IT system complexity, we incorporated the interaction term in the main model. The results are presented in Table 6. As shown in Columns 3 and 6, the coefficient of the interaction term is significantly negative, indicating that hospitals with more complex clinical IT systems benefit more from joining an HIE in terms of breach risk reduction. This finding supports Lemma 3a, which suggests that hospitals with higher unit data protection costs are less likely to improve their data security after joining an HIE.

## HIE Security Laws

Lemma 3b suggests that hospitals are more likely to achieve better security performance after joining an HIE when the governance is more effective. State-level HIE security laws aim to increase accountability for data security on HIEs and impose specific data exchange standards. For example, New Hampshire enacted HIE security laws on September 9, 2014 (N.H. Rev. Stat. § 332-I:10). They require HIEs to “implement recognized national standards for interoperability and transmission security. Transmission security standards shall guard against unauthorized access to electronic health information transmitted over an electronic communications network and include appropriate integrity controls and encryption mechanisms following HIPAA security regulations.” Although the HIE governance is based on mutual benefits among organizations, its effect on data breach risk may be suboptimal. HIE security laws may improve the effectiveness of HIE governance on data security protection.

We compiled a comprehensive list of state HIE security laws by collecting data from the State Health IT Policy Levers Compendium<sup>22</sup> and Health Privacy Project at Georgetown University,<sup>23</sup> which track state privacy and security policies related to Health IT. To ensure that these laws cover HIEs, we followed the practices outlined in Schmit et al. (2018) and manually searched for keywords such as “HIE,” “Security,” and “Breach” in the Westlaw legal database. We only coded laws as state-level HIE security laws if they specifically address safeguards to protect HIE data and do not refer to other state or federal laws. Our analysis included a dummy variable that took the value of 1 if the states had an HIE security law in a specific year and 0 otherwise.<sup>24</sup> We also incorporated an interaction term into the model and present our results in Table 6. Columns 3 and 6 in Table 6 indicate significantly negative coefficients of the interaction term, suggesting that HIE security laws can lower hospitals security breach risk. Thus, Lemma 3b is supported.

## Robustness Checks

## Endogeneity Concerns and Additional Tests

In an ideal experiment, hospitals would be randomly assigned to join HIEs; however, this is not feasible in practice. Therefore, our observational study may be subject to biases from three sources: confounding factors, reverse causality, and selection bias. To address these concerns, we conducted additional tests and robustness analyses as follows.

First, reverse causality may pose a concern. For instance, hospitals with a better security posture may be more likely to join HIEs. The administrators of such hospitals may believe that they can learn more about security practices by joining an HIE. To address potential reverse causality, we used relative-time models incorporating lead and lagged HIE participation indicators (see the Relative Time Models section). The results show no significantly decreasing trend in breach risk before hospitals joined HIEs, which mitigates concerns about reverse causality.

Second, confounding factors can simultaneously affect hospitals’ data breach risk and their likelihood of joining an HIE. For example, if more patients visit a hospital, the hospital may face higher losses in a breach incident. Consequently, the hospital may be motivated to improve its data security protection. At the same time, the propensity to join an HIE would also increase since the hospital needs historical diagnosis information on their patients from different sources to improve its service quality. In addition to the identification strategies we used in the main analyses, we performed different robustness checks. We discuss them in the Sensitivity Tests section to ensure the main effects of HIE are robust and to tease out alternative explanations.

Third, selection bias may be a concern with our data. On the one hand, one could argue that HIEs select their participants based on their IT profiles and security postures. However, this is unlikely to happen in the real world. In most cases, HIEs are incentivized to attract more healthcare providers to join their networks in order to increase their value (Demirezen et al., 2016). As a result, they are unlikely to select participants based on their IT security performance. Moreover, predicting future security breaches is challenging due to the complexity of causes. On the other hand, there may be self-selection issues associated with hospitals’ decisions to join an HIE. If hospitals that value data security are more likely to join HIEs, the impact of HIEs on breach probability may be spurious. Nevertheless, previous studies suggest that concerns about increasing security risk in data sharing are significant barriers to joining HIEs (Mello et al., 2018; Adler-Milstein & Jha, 2014). In other words, hospitals that value data security less are more likely to join HIEs, making our results more conservative when the associations between HIE participation and data breaches are negative. Additionally, we employed alternative models to test our main findings further. Table 7 summarizes the main concerns in analyses and the related robustness tests.

## Relative Time Models

The validity of DiD estimation relies heavily on the parallel trend assumption, which assumes that the treatment and control groups follow a similar trend in the outcome variable over time when the treatment is absent. To test this assumption in our study, we need to examine whether hospitals in the treated group (i.e., those that join HIE) had a lower data breach risk before joining an HIE. To accomplish this, we used relative time models that incorporate relative time dummies to indicate the relative yearly sequential distance between an observation year, ??, and the year when a hospital joined an HIE, ??. This approach is consistent with previous studies (e.g., Adjerid et al., 2018; Chan & Ghose, 2014). In our analyses, we excluded hospitals already in an HIE at the start of our data collection period in 2010, as we could not determine the exact year they joined the HIE. As a result, we lost approximately 2.3% of observations when estimating relative time models.

In Table 8, we present the results of relative-time models with and without control variables, demonstrating the validity of our DiD analysis. Specifically, Columns 1 and 2 show that the coefficients of $J o i n H I E _ { t - 3 }$ and $J o i n H I E _ { t - 2 }$ are insignificant, suggesting that there are no pretreated trends. Furthermore, the significantly negative coefficients of $J o i n H I E _ { t + 0 } , J o i n H I E _ { t + 1 }$ , and $J o i n H I E _ { t + 2 }$ suggest that the effect is realized in the same year the hospital joins the HIE and lasts at least two years. It implies that the governance accompanied by increased IT security investment takes effect without long learning periods and shifts the security equilibrium in longer terms.

## Sensitivity Tests

To examine the sensitivity of our primary findings in response to some major empirical concerns, we perform a series of diagnostics and robustness checks. One major concern is that state-level policies regarding information security or health information technology could confound the impact of HIE. To address this, we incorporate stateyear-specific trends to capture all state-level shocks. Our results remain robust, as presented in Column 1 of Table A4 in the Appendix.

<table><tr><td colspan="4">Table 7. Summary of Robustness Tests</td></tr><tr><td>Concerns</td><td>Tests</td><td>Findings</td><td>Locations</td></tr><tr><td>Reverse causality</td><td>Relative-time model</td><td>There is no pretreated trend, and the results remain consistent</td><td>Table 8</td></tr><tr><td>Matching results are sensitive</td><td>Different matching strategies</td><td>Results remain consistent</td><td>Table A2</td></tr><tr><td>State-level policy confounds the main impact</td><td>State-specific trends</td><td>Results remain consistent</td><td>Table A4</td></tr><tr><td>Results are sensitive to model specification</td><td>Nonlinear models</td><td>Results remain consistent</td><td>Table A4</td></tr><tr><td>The validity of previous instrumental variables</td><td>Alternative instrumental variable</td><td>Results remain consistent</td><td>Table A4</td></tr><tr><td>Omitted variables and alternative explanations</td><td>Additional control variables</td><td>Results remain consistent</td><td>Table A4</td></tr></table>

<table><tr><td colspan="3">Table 8. Relative-time Model</td></tr><tr><td rowspan="2">DV: Data breach occurrence</td><td>(1)</td><td>(2)</td></tr><tr><td>Baseline</td><td>Control variables</td></tr><tr><td>t - 3</td><td>-0.0073(0.0076)</td><td>-0.0074(0.0084)</td></tr><tr><td>t - 2</td><td>-0.0065(0.0095)</td><td>-0.0104(0.0100)</td></tr><tr><td>t + 0</td><td>-0.0236*(0.0095)</td><td>-0.0326**(0.0101)</td></tr><tr><td>t + 1</td><td>-0.0326***(0.0092)</td><td>-0.0361***(0.0101)</td></tr><tr><td>t + 2</td><td>-0.0588***(0.0109)</td><td>-0.0576***(0.0120)</td></tr><tr><td>R-squared</td><td>0.247</td><td>0.278</td></tr><tr><td>Observations</td><td>19405</td><td>16536</td></tr><tr><td>No. hospitals</td><td>3247</td><td>3090</td></tr><tr><td>Hospital &amp; year FE</td><td>YES</td><td>YES</td></tr><tr><td>Control variables</td><td>NO</td><td>YES</td></tr></table>

Note: All estimations use cluster-adjusted robust standard errors (clustered at the hospital level). \*\*\* $p < 0 . 0 0 1 , ^ { \star \star } p < 0 . 0 1 , ^ { \star } p < 0 . 0 5 , + p < 0 . 1$

Another alternative explanation of HIE’s impact is that hospitals might revamp their security posture after implementing IT applications that require data aggregation and reorganizations. If that were the case, hospitals adopting other similar IT applications, such as a clinical data repository (CRD) or CPOE, should also experience lower data breach risk. We incorporate indicators of CRD and CPOE presence in our models and estimate their impact on data breaches as placebo tests. The results in Column 2 of Table A4 demonstrate that the presence of CRD and CPOE do not significantly affect data breaches. Column 3 of Table A4 of the Appendix shows that the impact of HIE remains consistent when the model includes CRD and CPOE adoption as control variables.

Next, we used alternative instrumental variables to test if HIE’s impact would still hold. Specifically, we used the readmission rate in a health referral region instead of the number of unique health systems. The intuition is that hospitals in an HHR with a higher readmission rate are more likely to join an HIE because it enables physicians to access patients’ previous treatment records and make better decisions in order to reduce readmission rates. After 2011, this incentive was enhanced because of the introduction of the Hospital Readmission Reduction Program, which punishes general acute care hospitals when the readmission rate of Medicare patients exceeded a threshold. At the same time, the readmission rate in an HHR is plausibly independent of a hospital’s data breach risk, conditional on the hospital’s characteristics. We report the results in Column 4 of Table A4 in the Appendix. Lastly, we tested whether we could obtain similar results from nonlinear models. Since the outcome variable is binary, we used probit models and logit models with fixed effects to estimate the above analyses. We report the results in Columns 5 and 6 of Table A4. All results are consistent with our previous findings.

## Discussion

## Main Findings

Our study investigates how sharing electronic health data via health information exchanges (HIEs) affects hospitals’ data breach risk. While the public and healthcare providers have expressed concerns about increased data security risk when hospitals start to exchange data across their boundaries in HIEs, it is possible that HIE governance may lower this risk by enhancing IT security protections among hospitals. Therefore, we explored the tension between increased security risk and HIE governance. Using an analytical model, we demonstrate that hospitals’ security breach likelihood may increase or decrease when it joins an HIE. Furthermore, our findings indicate that hospitals tend to increase their IT security investment after joining an HIE and that the improvement of data security is of a larger magnitude for hospitals with a lower unit cost of protection or when the effectiveness of HIE governance increases.

To examine the insights from our theoretical model, we empirically tested the effect of HIE participation on hospitals data breach risk. Our findings indicate that hospitals’ data breach risk decreases after joining an HIE. In a further step, we found that after joining an HIE, hospitals tend to adopt more IT security applications, and the complexity of their clinical IT system positively affects the magnitude of the data breach risk reduction. Additionally, we found that external enforcement of HIE security laws furthers the reduction in breach risk for HIE hospitals. Our results are robust to omitted variables, reverse causality, and selfselection considerations.

## Implications for Research

This study contributes to three main streams of literature in the information systems field. First, we extend the information security literature in the IOS context. Most studies on organizational information security performances focus on internal management or external security policies (D’Arcy et al., 2020; Angst et al., 2017b; Hui et al., 2017; Kwon & Johnson, 2014; Romanosky et al., 2011). The impact of general data sharing through IOSs is much more nuanced, and most existing studies only use analytical models to explore the topic (Fang et al., 2014; Huang et al., 2014). While a few recent studies empirically examine the security dynamics in cross-organizational scenarios in recent years, the findings are mixed (Tanriverdi et al., 2019; Baskerville et al., 2018). To reconcile these discrepancies, our study investigates realized security risk changes after hospitals start sharing data electronically across organizational boundaries.

Second, this study contributes to the IOS literature. Previous studies in this field associate IOSs with various benefits within technical, organizational, and political spheres (Gil-Garcia & Sayogo, 2016; Dawes, 1996). However, security risks, which are considered major conflicts in IOSs (Kumar & Van Dissel, 1996), are seldom examined. IOS governance is also needed to address the conflicts (Chatterjee & Ravichandran, 2013), leading to interesting dynamics in realized outcomes. Nevertheless, we are not aware of any empirical study that quantifies the impact of IOS adoption on security risks. Our findings illustrate the unexpected effects of breaking information silos among organizations— coordination in the information security field.

Third, this study contributes to the health IT literature. HIEs, as large-scale health IT initiatives in the United States, enable data sharing among disparate healthcare providers and improve healthcare efficiency in many aspects (Adjerid et al., 2018; Atasoy et al., 2018; Ayabakan et al., 2017). However, security risks have always been considered the main obstacles to HIE adoption. Our results suggest that HIE governance facilitates coordination in the cybersecurity landscape, which improves overall security performance in hospitals. The findings complement previous studies on health IT and hospital security posture (Kim & Kwon, 2019; Miller & Tucker, 2011a). Furthermore, this study suggests that HIEs are used for more than providing a channel for hospitals to exchange medical information and knowledge. The governance in the process is critical in mitigating risk, which is worthy of further investigation. Our results also reveal that reductions in data security risk are of a larger magnitude in hospitals with higher complexity of clinical IT systems, emphasizing the importance of providing additional support or incentives to participants with low data protection.

## Implications for Practice

The study offers several implications for practitioners and policymakers. First, stakeholders need to recognize the impact of joining HIEs on the security postures of adopting hospitals, given the increasing prominence of data sharing privacy and security. Policymakers and HIE administrators should prioritize policies and practices that address public concerns and enhance data protection efforts to build trust among different parties, facilitate collaborations, and promote data interoperability. Our analytical model assumes that increased security risk is possible when data begins to flow. Hence, the improvement in security posture will only be realized when hospitals can protect data effectively at a lower cost and when the likelihood of shared risk is relatively low.

The efficiency of hospitals’ data protection plays a critical role in improving data security. While the hospitals’ data security performance improves after joining an HIE, the magnitude of improvement is lower for hospitals that adopt fewer clinical IT systems. This finding is particularly important since risk can involve other participants in the same HIE network. Therefore, policymakers and HIE administrators need to identify these hospitals and provide them with more assistance to enhance their capability to protect patient data. For example, HIEs can offer training or subsidies to help member hospitals that experience difficulties in digital transformations and data protection.

Furthermore, as the number of breach incidents caused by third parties continues to rise, practitioners are recognizing the importance of “risks across walls.” However, crossorganizational data governance is not well understood. Our study suggests that the HIE model could serve as a reference for other IOSs to reduce risk. While IOSs may differ in technical infrastructures, complexity, and openness, the core concept is to bridge data sharing among organizations. Managers and chief information security officers should establish a practical governance framework to control network risks. Furthermore, assessing participants’ security risk is critical before sharing data. The prevalence of third-party risk assessment businesses shows that data security posture has become a key metric when evaluating collaborators.

## Limitations and Future Directions

This study is subject to a few limitations. First, our measurements have some limitations. For instance, we used a binary indicator to measure hospitals’ HIE status for the treatment variable. However, a lack of HIE-level data makes it challenging to capture more detailed mechanisms. Future studies could investigate how variations in HIEs organizational, governance, and technical structure affect the overall data breach risk. For example, investigating whether HIE service fees, which potentially encompass administrative and operational costs, are associated with the likelihood of data breaches in HIE hospitals would be an intriguing avenue to explore. Furthermore, our outcome variable cannot reveal whether breach incidents involved the health records of multiple hospitals. Future studies could enhance the granularity of analysis by leveraging more comprehensive data breach outcomes that capture such details.

Second, as with many observational studies, endogeneity is a major concern in our research. Although we address these issues using a set of identification strategies to carefully exclude the confounding impacts and address reverse causality and selection biases, establishing full causality using secondary data such as ours is not possible.

Third, this study is based on the healthcare context, where data security is highly valued and regulated by HIPAA, HHS data breach notifications, and state laws. In industries where data protection regulations are not strict, IOS adoption may increase data breach risk. Our analytical models and empirical results can still offer insights into IOS adoption in other industries despite the differences in institutions. First, organizations should have sufficient experience in IT security performance to improve their security posture. Secondly, IOS governance should seek to reduce shared risk to incentivize organizations to enhance their data protection. Given the limited research on security data sharing across organizational boundaries, we call for further studies in other settings. There are still many interesting and unanswered questions about IOSs and information security, which could serve as potential directions for future research.

## Acknowledgments

The authors sincerely thank the senior editor, Corey Angst, the associate editor, and all three reviewers for all their invaluable comments and insights throughout the development of our study. The authors also thank HIMSS Analytics for providing the data used in the study. The authors also thank John D’Arcy, Taha Havakhor, Qiuhong Wang, and Anthony Vance for their constructive suggestions, which enhanced the study. The study also benefitted from helpful feedback from reviewers and participants at the Workshop on the Economics of Information Security (2019) and the International Conference on Information Systems (2019).

## References

Abadie, A., Athey, S., Imbens, G. W. & Wooldridge, J. M. (2023). When should you adjust standard errors for clustering? Quarterly Journal of Economics, 138(1), 1-35. https://doi.org/10.1093/qje/qjac038

Acemoglu, D., Malekian, A. & Ozdaglar, A. (2016). Network security and contagion. Journal of Economic Theory, 166, 536- 585. https://doi.org/10.1016/j.jet.2016.09.009

Adjerid, I., Adler-Milstein, J. & Angst, C. (2018). Reducing medicare spending through electronic health information exchange: the role of incentives and exchange maturity. Information Systems Research, 29(2), 341-361. https://doi.org/ 10.1287/isre.2017.0745

Adler-Milstein, J., DesRoches, C. M. & Jha, A. K. (2011). Health information exchange among us hospitals. American Journal of Managed Care, 17(11), 761-768.

Adler-Milstein, J. & Jha, A. K. (2014). Health information exchange among u.s. hospitals: Who’s in, who’s out, and why? Healthcare, 2(1), 26-32. https://doi.org/10.1016/j.hjdsi.2013. 12.005

AHIMA/HIMSS. (2011). The privacy and security gaps in health information exchanges. https://bok.ahima.org/PdfView? oid=104470

AHRQ. (2017). Defining Health Systems. https://www.ahrq.gov/chsp/chsp-reports/resources-forunderstanding-health-systems/defining-health-systems.html

Anderson, R. & Moore, T. (2006). The economics of information security. Science, 314(5799), 610-613. https://doi.org/10.1126/ science.1130992

Angrist, J. D., Imbens, G. W. & Rubin, D. B. (1996). Identification of causal effects using instrumental variables. Journal of the American Statistical Association, 91(434), 444-455. https://doi.org/10.1080/01621459.1996.10476902

Angrist, J. D. & Pischke, J.-S. (2009). Mostly harmless econometrics: An empiricist’s companion. Princeton University Press. https://doi.org/10.2307/j.ctvcm4j72

Angst, C. M., Block, E. S., Arcy, J. D. & Kelley, K. (2017). When do it security investments matter? Accounting for the influence of institutional factors in the context of healthcare data breaches. MIS Quarterly, 41(3), 893-916. https://doi.org/ 10.25300/MISQ/2017/41.3.10

Angst, C. M., Wowak, K. D., Handley, S. M. & Kelley, K. (2017). Antecedents of information systems sourcing strategies in u.s. hospitals: A longitudinal study. MIS Quarterly, 41(4), 1-18.

https://doi.org/10.25300/MISQ/2017/41.4.06

Appari, A., Johnson, M. E. & L. Anthony, D. (2009). HIPAA compliance: An institutional theory perspective. AMCIS 2009 Proceedings. http://aisel.aisnet.org/amcis2009/252

Atasoy, H., Chen, P. yu & Ganju, K. (2018). The spillover effects of health it investments on regional healthcare costs. Management Science, 64(6), 2515-2534. https://doi.org/ 10.1287/mnsc.2017.2750

August, T., Niculescu, M. F. & Shin, H. (2014). Cloud implications on software network structure and security risks. Information Systems Research, 25(3), 489-510. https://doi.org/10.1287/ isre.2014.0527

Ayabakan, S., Bardhan, I., Zheng, Z. & Kirksey, K. (2017). The impact of health information sharing on duplicate testing. MIS Quarterly, 41(4), 1083-1103. https://doi.org/10.25300/MISQ/ 2017/41.4.04

Ayer, T., Ayvaci, M. U. S., Karaca, Z. & Vlachy, J. (2019). The impact of health information exchanges on emergency department length of stay. Production and Operations Management, 28(3), 740-758. https://doi.org/10.1111/poms. 12953

Baker, A. C., Larcker, D. F. & Wang, C. C. Y. (2022). How much should we trust staggered difference-in-differences estimates? Journal of Financial Economics, 144(2), 370-395. https://doi.org/10.1016/j.jfineco.2022.01.004

Bakos, J. Y. (1991). Information links and electronic marketplaces : The role of interorganizational information systems in vertical markets. Journal of Management Information Systems, 8(2), 31-52. https://doi.org/10.1080/07421222.1991.11517920

Baskerville, R., Rowe, F. & Wolff, F.-C. (2018). Integration of information systems and cybersecurity countermeasures. The Data Base for Advances in Information Systems, 49(1), 33-52. https://doi.org/10.1145/3184444.3184448

Becker, G. S. (1968). Crime and punishment : An economic approach. Journal of Political Economy, 76(2), 169-217. https://doi.org/10.1086/259394

Bharadwaj, A. S. (2000). A resource-based perspective on information technology capability and firm performance: an empirical investigation. MIS Quarterly, 24(1), 169-193. https://doi.org/10.2307/3250983

Burde, H. (2011). The hitech act: an overview. American Medical Association Journal of Ethics, 13(3), 172-175. https://doi.org/ 10.1001/virtualmentor.2011.13.3.hlaw1-1103

Callaway, B. & Sant’Anna, P. H. C. (2020). Difference-indifferences with multiple time periods. Journal of Econometrics, 255(2), 200-230. https://doi.org/10.1016/ j.jeconom.2020.12.001

Chan, J. & Ghose, A. (2014). Internet’s dirty secret: Assessing the impact of online intermediaries on hiv transmission. MIS Quarterly, 38(4), 955-975. https://doi.org/10.25300/MISQ/ 2014/38.4.01

Chatterjee, D. & Ravichandran, T. (2004). Inter-organizational information systems research: A critical review and an integrative framework. In Proceedings of the 37th Annual Hawaii International Conference on System Sciences. https://doi.org/10.1109/hicss.2004.1265398

Chatterjee, Dipanjan & Ravichandran, T. (2013). Governance of interorganizational information systems: a resource dependence perspective. Information Systems Research, 24(2), 261-278. https://doi.org/10.1287/isre.1120.0432

Chatterjee, Dipanjan & T.Ravichandran. (2013). Governance of interorganizational information systems : A resource dependence perspective. Information Systems Research, 24(2), 261-278. https://doi.org/10.1287/isre.1120.0432

Cohen, W. M. & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. Administrative Science Quarterly, 35(1), 128-152. https://doi.org/10.2307/ 2393553

D’Arcy, J., Adjerid, I., Angst, C. M. & Glavas, A. (2020). Too good to be true: Firm social performance and the risk of data breach. Information Systems Research, 31(4), 1200-1223. https://doi. org/10.1287/isre.2020.0939

Dawes, S. S. (1996). Interagency information sharing: Expected benefits, manageable risks. Journal of Policy Analysis and Management, 15(3), 377-394. https://doi.org/10.1002/ (SICI)1520-6688(199622)15:3<377::AID-PAM3>3.0.CO;2-F

Demirezen, E. M., Kumar, S. & Sen, A. (2016). Sustainability of healthcare information exchanges : A game-theoretic approach. Information Systems Research, 27(2), 240-258. https://doi.org/ 10.1287/isre.2016.0626

Dobkin, C., Finkelstein, A., Kluender, R. & Notowidigdo, M. J. (2018). The economic consequences of hospital admissions. American Economic Review, 108(2), 308-352. https://doi.org/ 10.1257/aer.20161038

Dranove, D., Forman, C., Goldfarb, A. & Greenste, S. (2014). The trillion dollar conundrum: Complementarities and health information technology. American Economic Journal : Economic Policy, 6(4), 239-270. https://doi.org/10.1257/ pol.6.4.239

Everson, J. & Adler-Milstein, J. (2016). Engagement in hospital health information exchange is associated with vendor marketplace dominance. Health Affairs, 35(7), 1286-1293. https://doi.org/10.1377/hlthaff.2015.1215

Fang, F., Parameswaran, M., Zhao, X. & Whinston, A. B. (2014). An economic mechanism to manage operational security risks for inter-organizational information systems. Information Systems Frontiers, 16(3), 399-416. https://doi.org/10.1007/ s10796-012-9348-y

Fischer, T., Huber, T., Dibbern, J. & Hirschheim, R. (2012). The Evolution of Contractual and Relational Governance in IS Outsourcing (Working Paper, Issue 242, Institute of Information Systems, University of Bern). SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=2109211

Fu, M. C., Buerba, R. A., Gruskay, J. & Grauer, J. N. (2013). Longitudinal urban-rural discrepancies in the us orthopaedic surgeon workforce. Clinical Orthopaedics and Related Research, 471(10), 3074-3081. https://doi.org/10.1007/ s11999-013-3131-3

Gaynor, M. S., Hydari, M. Z. & Telang, R. (2012). Is patient data better protected in competitive healthcare markets? In Proceedings of the Workshop on the Economics of Information Security. https://econinfosec.org/archive/weis2012/papers/ Gaynor\_WEIS2012.pdf

Gil-Garcia, J. R. & Sayogo, D. S. (2016). Government interorganizational information sharing initiatives: understanding the main determinants of success. Government Information Quarterly, 33(3), 572-582. https://doi.org/10.1016/j.giq.2016. 01.006

Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Journal of Econometrics, 225(2),

254-277. https://doi.org/10.1016/j.jeconom.2021.03.014

Goodman-Bacon, A., Goldring, T. & Nichols, A. (2019). BACONDECOMP: Stata module to perform a Bacon decomposition of difference-in-differences estimation (Statistical Software Components S458676). Boston College Department of Economics.

Gordon, L. A., Loeb, M. P. & Lucyshyn, W. (2003). Sharing information on computer systems security: An economic analysis. Journal of Accounting and Public Policy, 22(6), 461- 485. https://doi.org/10.1016/j.jaccpubpol.2003.09.001

Greenwood, B. N. & Wattal, S. (2017). Show me the way to go home: An empirical investigation of ride-sharing and alcohol related motor vehicle fatalities. MIS Quarterly, 41(1), 163-187. https://doi.org/10.25300/MISQ/2017/41.1.08

Greig, J. (2022). Data breach: Broward Health warns 1.3 million patients, staff of “medical identity theft.” ZDNET. https://www.zdnet.com/article/broward-health-warns-1-3- million-patients-staff-of-medical-identity-theft-after-databreach/

Grover, V. & Kohli, R. (2012). Cocreating it value: new capabilities and metrics for multifirm environments. MIS Quarterly, 36(1), 225-232. https://doi.org/10.2307/41410415

Hamre, G. A. & Monteiro, E. (2013). Towards a socio-technically resilient collaborative medication process. In Proceedings of the European Workshop on Practical Aspects of Health Informatics.

Heath, M., Porter, T. H. & Silvera, G. (2022). Hospital characteristics associated with hipaa breaches. International Journal of Healthcare Management, 15(2), 171-180. https://doi.org/10.1080/20479700.2020.1870349

HHS. (2015). The HIPAA Privacy Rule and Electronic Health Information Exchange in a Networked Environment. https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/unde rstanding/special/healthit/introduction.pdf

Hirsch, M. D. (2016). Editor’s Corner: HIE breach raises new, unanticipated questions. Fierce Healthcare. https://www.fierce healthcare.com/it/hie-s-breach-raises-new-unanticipatedquestions

Hsu, C., Lee, J. N. & Straub, D. W. (2012). Institutional influences on information systems security innovations. Information Systems Research, 23(3.2), 918-939. https://doi.org/10.1287/ isre.1110.0393

Huang, C. D., Behara, R. S. & Goo, J. (2014). Optimal information security investment in a healthcare information exchange: An economic analysis. Decision Support Systems, 61(1), 1-11. https://doi.org/10.1016/j.dss.2013.10.011

Hui, K.-L., Hui, W. & Yue, W. T. (2012). Information security outsourcing with system interdependency and mandatory security requirement. Journal of Management Information Systems, 29(3), 117-156. https://doi.org/10.2753/MIS0742- 1222290304

Hui, K.-L., Kim, S. H. & Wang, Q.-H. (2017). Cybercrime deterrence and international legislation: Evidence from distributed denial of service attacks. MIS Quarterly, 41(2), 497- A11. https://doi.org/10.25300/MISQ/2017/41.2.08

Hydari, M. Z., Telang, R. & Marella, W. M. (2018). Saving patient ryan can advanced electronic medical records make patient care safer? Management Science, 65(5), 2041-2059. https://doi.org/ 10.1287/mnsc.2018.3042

Iacus, S. M., King, G. & Porro, G. (2012). Causal inference without

balance checking: Coarsened exact matching. Political Analysis, 20(1), 1-24. https://doi.org/10.1093/pan/mpr013

IBM Security. (2023). Cost of a data breach report 2023. https://doi.org/10.1016/s1361-3723(21)00082-8

Jayanth, R., Jacob, V. S. & Radhakrishnan, S. (2011). Vendor and client interaction for requirements assessment in software development: Implications for feedback process. Information Systems Research, 22(2), 289-305. https://doi.org/10.1287/isre. 1090.0248

Karahanna, E., Chen, A., Ben Liu, Q. & Serrano, C. (2019). Capitalizing on health information technology to enable digital advantage in u.s. hospitals. MIS Quarterly, 43(1), 113-140. https://doi.org/10.25300/misq/2019/12743

Kim, S. H. & Kwon, J. (2019). How do ehrs and a meaningful use initiative affect breaches of patient information? Information Systems Research, 30(4), 1184-1202. https://doi.org/10.1287/ isre.2019.0858

Kumar, K. & Van Dissel, H. G. (1996). Sustainable collaboration: managing conflict and cooperation in interorganizational systems. MIS Quarterly, 20(3), 279-300. https://doi.org/ 10.2307/249657

Kwon, J. & Johnson, M. E. (2014). Proactive versus reactive security investments in the healthcare sector. MIS Quarterly, 38(2), 451-471. https://doi.org/10.1017/CBO9781107415324. 004

Kwon, J. & Johnson, M. E. (2018). Meaningful healthcare security: does meaningful-use attestation improve information security performance? MIS Quarterly, 42(4), 1043-1067. https://doi. org/10.25300/MISQ/2018/13580

Lee, C. H., Geng, X. & Raghunathan, S. (2013). Contracting information security in the presence of double moral hazard. Information Systems Research, 24(2), 295-311. https://doi.org/ 10.1287/isre.1120.0447

Lee, C. H., Geng, X. & Raghunathan, S. (2016). Mandatory standards and organizational information security. Information Systems Research, 27(1), 70-86. https://doi.org/10.1287/isre. 2015.0607

Marshall, G. F., Gillespie, W., & Fox, S. J. (2009). Privacy and security in Pennsylvania: Ensuring privacy and security of health information exchange in Pennsylvania. Journal of Healthcare Information Management, 23(2), 38-44.

McGee, M. K. (2016). Clinic reports security incident involving HIE access. CareersInfoSecurity https://www.careersinfo security.com/clinic-reports-security-incident-involving-hieaccess-a-9413

McGowan, J. J., Kuperman, G. J., Olinger, L. & Russell, C. (2012). Strengthening health information exchange: Final report HIE unintended consequences work group. The Office of the National Coordinator for Health Information Technology. https://www.healthit.gov/sites/default/files/hie\_uc\_workgroup \_final\_report.pdf

Mckeon, J. (2022). Key Ways to Manage the Legal Risks of a Healthcare Data Breach. TechTarget. https://www.techtarget. com/healthtechsecurity/answer/Key-Ways-to-Manage-the-Legal-Risks-of-a-Healthcare-Data-Breach

Mello, M. M., Adler-Milstein, J., Ding, K. L. . & Savage, L. (2018). Legal barriers to the growth of health information exchange— Boulders or pebbles? The Milbank Quarterly, 96(31), 110-143. https://doi.org/10.1111/1468-0009.12212

Miller, A. R. & Tucker, C. (2009). Privacy protection and

technology diffusion: The case of electronic medical records. Management Science, 55(7), 1077-1093. https://doi.org/ 10.1287/mnsc.1090.1014

Miller, A. R. & Tucker, C. (2014). Health information exchange, system size and information silos. Journal of Health Economics, 33(1), 28-42. https://doi.org/10.1016/j.jhealeco. 2013.10.004

Miller, A. R. & Tucker, C. E. (2011a). Can health care information technology save babies? Journal of Political Economy, 119(2), 289-324. https://doi.org/10.1086/660083

Miller, A. R. & Tucker, C. E. (2011b). Encryption and the loss of patient data. Journal of Policy Analysis and Management, 30(3), 534-556. https://doi.org/10.1002/pam.20590

Monica, K. (2018). 70% of hospitals participated in nationwide HIE networks in 2017. https://ehrintelligence.com/news/70-ofhospitals-participated-in-nationwide-hie-networks-in-2017

ONC. (2013). Governance framework for trusted electronic health information exchange. Office of the National Coordinator for Health Information Technology https://www.healthit.gov/ sites/default/files/governanceframeworktrustedehie\_final.pdf

Perlroth, N. (2011). Digital data on patients raises risk of breaches. The New York Times. https://www.nytimes.com/2011/12/19/ technology/as-patient-records-are-digitized-data-breaches-areon-the-rise.html

Ponemon Institute. (2012). Third Annual Benchmark Study on Patient Privacy & Data Security. https://www.ponemon.org/ local/upload/file/Third\_Annual\_Study\_Patient\_Privacy\_FINA L.pdf

Ransbotham, S. & Mitra, S. (2009). Choice and chance: A conceptual model of paths to information security compromise. Information Systems Research, 20(1), 121-139. https://doi.org/ 10.1287/isre.1080.0174

Roberts, N., Galluch, P. S., Din, M. & Grover, V. (2012). Absorptive capacity and information systems research: Review, synthesis, and directions for future research. MIS Quarterly, 36(2), 625-648. https://doi.org/10.1017/CBO978 1107415324.004

Robey, D., Im, G. & Wareham, J. D. (2008). Theoretical foundations of empirical research on interorganizational systems: Assessing past contributions and guiding future directions. Journal of the Association for Information Systems, 9(9), 497-518. https://doi.org/10.17705/1jais.00171

Roehrich, J. K., Selviaridis, K., Kalra, J., Van der Valk, W. & Fang, F. (2020). Inter-organizational governance: A review, conceptualisation and extension. Production Planning and Control, 31(6), 453-469. https://doi.org/10.1080/09537287. 2019.1647364

Romanosky, S., Telang, R. & Acquisti, A. (2011). Do data breach disclosure laws reduce identity theft. Journal of Policy Analysis and Management, 32(2), 296-322. https://doi.org/10.1002/ pam.20567

Ross, S. E., Schilling, L. M., Fernald, D. H., Davidson, A. J. & West, D. R. (2010). Health information exchange in small-tomedium sized family medicine practices: Motivators, barriers, and potential facilitators of adoption. International Journal of Medical Informatics, 79(2), 123-129. https://doi.org/10.1016/ j.ijmedinf.2009.12.001

Rubright, N. (2023). 10 Ways to protect your practice from a data breach. Physician’s Practice. https://www.physicianspractice. com/view/10-ways-to-protect-your-practice-from-a-data-

breach

Rudin, R. S., Motala, A., Goldzweig, C. L. & Shekelle, P. G. (2014). Usage and effect of health information exchange: A systematic review. Annals of Internal Medicine, 161(11), 803- 811. https://doi.org/10.7326/M14-0877

Salomon, R. & Martin, X. (2008). Learning, knowledge transfer, and technology implementation performance: A study of timeto-build in the global semiconductor industry. Management Science, 54(7), 1266-1280. https://doi.org/10.1287/mnsc.1080. 0866

Schmit, C. D., Wetter, S. A. & Kash, B. A. (2017). Falling short: how state laws can address health information exchange barriers and enablers. Journal of the American Medical Informatics Association, 25(6), 635-644. https://doi.org/10. 1093/jamia/ocx122

Scholl, M., Stine, K., Lin, K., & Steinberg, D. (2010). Security architecture design process for health information exchanges (HIEs). NIST. https://doi.org/10.6028/NIST.IR.7497

Seh, A. H., Zarour, M., Alenezi, M., Sarkar, A. K., Agrawal, A., Kumar, R. & Ahmad Khan, R. (2020). Healthcare data breaches: insights and implications. Healthcare, 8(2), Article 133. https://doi.org/10.3390/healthcare8020133

Sittig, D. F. & Singh, H. (2011). Legal, ethical, and financial dilemmas in electronic health record adoption and use. Pediatrics, 127(4), e1042-e1047. https://doi.org/10.1542/peds. 2010-2184

Snell, E. (2015). How to improve health data privacy, security in HIE. TechTarget. https://healthitsecurity.com/news/how-toimprove-health-data-privacy-security-in-hie

Staiger, D. & Stock, J. H. (1997). Instrumental variables regression with weak instruments. Econometrica, 65(3), 557-586. https://doi.org/10.2307/2171753

Stigler, G. J. (1958). The economies of scale. The Journel of Law & Economics, 1, 54-71. https://doi.org/10.1086/466541

Straub, D. W. & Nance, W. D. (1990). Discovering and disciplining computer abuse in organizations: A field study. MIS Quarterly, 14(1), 45-60. https://doi.org/10.2307/249307

Sun, S., Lu, S. F. & Rui, H. (2020). Does telemedicine reduce emergency room congestion? Evidence from new york state. Information Systems Research, 31(3), 972-986. https://doi.org/ 10.1287/ISRE.2020.0926

Tanriverdi, H., Roumani, Y. & Nwankpa, J. K. (2019). Structural complexity and data breach risk. In Proceedings of the 40th International Conference on Information Systems.

Wang, E. T. G. & Seidmann, A. (1995). Electronic data interchange: competitive externalities and strategic implementation policies. Management Science, 41(3), 401- 418. https://doi.org/10.1287/mnsc.41.3.401

Wider, J. (2023). CommonSpirit health updates privacy breach notice. Healthcare Innovation. https://www.hcinnovation group.com/cybersecurity/news/53056820/commonspirithealth-updates-privacy-breach-notice

Yaraghi, N., Du, A. Y., Sharman, R., Gopal, R. D. & Ramesh, R. (2015). Health information exchange as a multisided platform: Adoption, usage, and practice involvement in service coproduction. Information Systems Research, 26(1), 1-18.

https://doi.org/10.1287/isre.2014.0547

Zhao, X., Xue, L. & Whinston, A. (2013). Managing interdependent information security risks: Cyberinsurance, managed security services, and risk pooling arrangements. Journal of Management Information Systems, 30(1), 123-152. https://doi.org/10.2753/MIS0742-1222300104

## About the Authors

Leting Zhang is an assistant professor of management information systems at the Lerner College of Business and Economics, University of Delaware. She received her Ph.D. in management information systems from the Fox School of Business, Temple University. Her research focuses on the impact of information technology on digital risks, healthcare, and labor market. Her research has been published in top-tier academic journals such as MIS Quarterly and Information Systems Research.

Sunil Wattal is the associate dean of Research and Doctoral Programs and is a professor of management information systems and a Harold Schaefer Senior Fellow at the Fox School of Business, Temple University. Sunil’s expertise focuses on the economics of information systems, the sharing economy, digital platforms, and privacy. His work has been published in top academic journals such as MIS Quarterly, Information Systems Research, Management Science, Journal of Management Information Systems, Journal of the Association of Information Systems, and IEEE Transactions on Software Engineering. He has served as an associate editor for MIS Quarterly and Information Systems Research. Sunil received his Ph.D. from the Tepper School of Business, Carnegie Mellon University.

Min-Seok Pang is a professor of information systems and analytics at Wisconsin School of Business, University of Wisconsin-Madison. He has received a B.S. in industrial engineering and an M.S. in management from the Korea Advanced Institute of Science and Technology (KAIST) and holds a Ph.D. in business administration from the University of Michigan. His research interests include, among others, strategic management of information technology in the public sector and technologyenabled public policies. His research has been published in top-tier academic journals such as Management Science, MIS Quarterly, Information Systems Research, and Strategic Management Journal. He received the INFORMS ISS Sandra Slaughter Early Career Award and Outstanding Associate Editor of the Year Award from MIS Quarterly. His research has been featured in several news outlets such as The Wall Street Journal, Computerworld, Federal Computer Week, and TechCrunch. He currently serves as a senior editor for Journal of the Association for Information System and as a co-editor for the MIS Quarterly Special Issue on Digital Technologies and Social Justice. ORCID: https://orcid.org/0000- 0001-9010-6260

## Appendix

<table><tr><td colspan="11">Table A1. Correlation Matrix of Main Variables</td></tr><tr><td>Variables</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td></tr><tr><td>(1) Data breach</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Join HIE</td><td>0.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Health system size</td><td>0.12</td><td>0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) Operation expenditure</td><td>0.15</td><td>0.23</td><td>0.29</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Payroll expense</td><td>0.14</td><td>0.23</td><td>0.26</td><td>0.98</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) IT apps</td><td>0.10</td><td>0.30</td><td>0.24</td><td>0.59</td><td>0.58</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(7) Strategy apps</td><td>0.06</td><td>0.26</td><td>0.27</td><td>0.40</td><td>0.38</td><td>0.83</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(8) Clinical apps</td><td>0.11</td><td>0.27</td><td>0.12</td><td>0.62</td><td>0.61</td><td>0.90</td><td>0.67</td><td>1.00</td><td></td><td></td></tr><tr><td>(9) Advanced EHR</td><td>0.06</td><td>0.17</td><td>0.04</td><td>0.17</td><td>0.17</td><td>0.56</td><td>0.63</td><td>0.50</td><td>1.00</td><td></td></tr><tr><td>(10) IS plan</td><td>0.01</td><td>0.12</td><td>0.31</td><td>0.18</td><td>0.17</td><td>0.28</td><td>0.28</td><td>0.19</td><td>0.11</td><td>1.00</td></tr><tr><td>(11) Total admission</td><td>0.14</td><td>0.17</td><td>0.32</td><td>0.93</td><td>0.92</td><td>0.57</td><td>0.37</td><td>0.62</td><td>0.14</td><td>0.15</td></tr><tr><td>(12) Competition</td><td>-0.04</td><td>-0.03</td><td>-0.11</td><td>-0.15</td><td>-0.14</td><td>-0.08</td><td>-0.07</td><td>-0.06</td><td>-0.04</td><td>-0.05</td></tr><tr><td>(13) Total admission</td><td>0.05</td><td>0.08</td><td>0.08</td><td>0.16</td><td>0.15</td><td>0.13</td><td>0.10</td><td>0.11</td><td>0.08</td><td>0.13</td></tr><tr><td>(14) HRR CMI</td><td>0.10</td><td>0.02</td><td>0.24</td><td>0.39</td><td>0.38</td><td>0.18</td><td>0.15</td><td>0.16</td><td>0.08</td><td>0.14</td></tr><tr><td>(15) HRR income</td><td>-0.02</td><td>-0.16</td><td>0.08</td><td>0.15</td><td>0.14</td><td>-0.08</td><td>-0.10</td><td>-0.06</td><td>-0.19</td><td>-0.05</td></tr><tr><td>(16) HRR population</td><td>0.10</td><td>0.01</td><td>0.25</td><td>0.38</td><td>0.37</td><td>0.17</td><td>0.14</td><td>0.15</td><td>0.07</td><td>0.13</td></tr><tr><td>(17) HIE security laws</td><td>0.01</td><td>0.05</td><td>-0.02</td><td>-0.08</td><td>-0.09</td><td>0.03</td><td>0.04</td><td>0.03</td><td>0.08</td><td>0.02</td></tr><tr><td>(18) MSA</td><td>0.08</td><td>0.10</td><td>0.40</td><td>0.55</td><td>0.53</td><td>0.31</td><td>0.26</td><td>0.25</td><td>0.07</td><td>0.21</td></tr><tr><td>(19) Academic</td><td>0.08</td><td>0.13</td><td>0.05</td><td>0.37</td><td>0.37</td><td>0.16</td><td>0.13</td><td>0.17</td><td>0.08</td><td>0.01</td></tr><tr><td>(20) For-profit</td><td>-0.04</td><td>-0.30</td><td>0.41</td><td>-0.19</td><td>-0.22</td><td>-0.24</td><td>-0.11</td><td>-0.33</td><td>-0.10</td><td>-0.00</td></tr><tr><td>Variables</td><td>(11)</td><td>(12)</td><td>(13)</td><td>(14)</td><td>(15)</td><td>(16)</td><td>(17)</td><td>(18)</td><td>(19)</td><td>(20)</td></tr><tr><td>(11) Total admission</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(12) Competition</td><td>-0.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(13) Total admission</td><td>0.07</td><td>-0.08</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(14) HRR CMI</td><td>0.35</td><td>-0.54</td><td>0.33</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(15) HRR income</td><td>0.20</td><td>-0.02</td><td>-0.13</td><td>0.13</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(16) HRR population</td><td>0.36</td><td>-0.52</td><td>0.31</td><td>0.99</td><td>0.21</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(17) HIE security laws</td><td>-0.13</td><td>0.01</td><td>0.14</td><td>0.03</td><td>-0.32</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(18) MSA</td><td>0.51</td><td>-0.15</td><td>0.17</td><td>0.47</td><td>0.18</td><td>0.47</td><td>-0.07</td><td>1.00</td><td></td><td></td></tr><tr><td>(19) Academic</td><td>0.30</td><td>-0.08</td><td>0.04</td><td>0.16</td><td>0.01</td><td>0.14</td><td>-0.03</td><td>0.16</td><td>1.00</td><td></td></tr><tr><td>(20) For-profit</td><td>-0.15</td><td>-0.07</td><td>-0.03</td><td>0.10</td><td>0.08</td><td>0.11</td><td>-0.02</td><td>0.12</td><td>-0.09</td><td>1.00</td></tr></table>

<table><tr><td colspan="5">Table A2. Matching Strategies - HIE&#x27;s Impact on Data Breach Occurrence</td></tr><tr><td>DV:</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Data breach occurrence</td><td>PSM N = 3</td><td>PSM N = 5</td><td>CEM</td><td>CEM weights</td></tr><tr><td>Join HIE</td><td>-0.0156*(0.0073)</td><td>-0.0167*(0.0072)</td><td>-0.0247*(0.0102)</td><td>-0.0187+(0.0103)</td></tr><tr><td>R-squared</td><td>0.326</td><td>0.324</td><td>0.352</td><td>0.337</td></tr><tr><td>Observations</td><td>8778</td><td>9514</td><td>4532</td><td>4532</td></tr><tr><td>No. hospitals</td><td>1637</td><td>1777</td><td>834</td><td>834</td></tr><tr><td>Hospital &amp; year FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr></table>

Note: All estimations use cluster-adjusted robust standard errors (clustered at the hospital level). \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, +p < 0.1

Table A4. Sensitivity Tests

<table><tr><td colspan="2">Table A3. Exclude Hospitals Experiencing Multiple Breaches</td></tr><tr><td></td><td>(1) Data Breach</td></tr><tr><td>Join HIE</td><td>-0.0127*(0.0054)</td></tr><tr><td>R-squared</td><td>0.181</td></tr><tr><td>Observations</td><td>16086</td></tr><tr><td>No. hospitals</td><td>3022</td></tr><tr><td>Hospital &amp; year FE</td><td>YES</td></tr><tr><td>Control variables</td><td>YES</td></tr></table>

Note: All estimations used cluster-adjusted robust standard errors (clustered at the hospital level). \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, +p < 0.1

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>DV: Data breach occurrence</td><td>State-year specific trend</td><td>Placebo test</td><td>Additional control variables</td><td>Alternative IV</td><td>Probit model</td><td>Logit model</td></tr><tr><td>Join HIE</td><td>-0.0169*(0.0078)</td><td></td><td>-0.0153*(0.0073)</td><td>-0.0578***(0.0171)</td><td>-0.2526*(0.1091)</td><td>-0.6483**(0.2142)</td></tr><tr><td>Clinical data repository</td><td></td><td>0.0116(0.0110)</td><td>0.0105(0.0110)</td><td></td><td></td><td></td></tr><tr><td>Computerized provider order entry</td><td></td><td>-0.0043(0.0102)</td><td>-0.0043(0.0102)</td><td></td><td></td><td></td></tr><tr><td>R-squared/likelihood</td><td>0.387</td><td>0.326</td><td>0.326</td><td>0.012</td><td>-1146.816</td><td>-930.119</td></tr><tr><td>Observations</td><td>8766</td><td>8778</td><td>8778</td><td>16948</td><td>8793</td><td>2936</td></tr><tr><td>No. hospitals</td><td>1635</td><td>1637</td><td>1637</td><td>3180</td><td>1652</td><td>538</td></tr><tr><td>Hospital &amp; year FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Control variables</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr></table>

Note: All estimations used cluster-adjusted robust standard errors (clustered at the hospital level). The estimations in Columns 1, 2, 3, and 5 used a matched sample. We used total samples in the estimations in Columns 4 and 6 to focus on a single identification strategy (IV) and to avoid substantially small sample sizes, respectively. \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, +p < 0.1

<table><tr><td>DV: HIE Security law</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>No. breaches</td><td>0.0009 (0.0025)</td><td></td><td></td><td></td></tr><tr><td>No. breaches (t-1)</td><td></td><td>-0.0015 (0.0024)</td><td></td><td></td></tr><tr><td>No. breaches (t - 2)</td><td></td><td></td><td>-0.0035 (0.0028)</td><td></td></tr><tr><td>No. breaches (t - 3)</td><td></td><td></td><td></td><td>-0.0003 (0.0015)</td></tr><tr><td>No. IT jobs</td><td>0.7536 (0.3922)</td><td>0.3377 (0.4200)</td><td>0.1815 (0.3984)</td><td>0.5214 (0.4323)</td></tr><tr><td>Income</td><td>0.3904 (0.7019)</td><td>0.1396 (0.8648)</td><td>-0.4012 (1.0101)</td><td>-0.9268 (0.7774)</td></tr><tr><td>No. jobs</td><td>-0.4683 (1.3270)</td><td>0.4725 (1.1310)</td><td>1.1878 (1.2877)</td><td>0.7845 (1.1262)</td></tr><tr><td>Population</td><td>-0.2658 (2.0996)</td><td>-2.9025 (2.0072)</td><td>-4.8552* (2.4059)</td><td>-3.2004 (2.6413)</td></tr><tr><td>Constant</td><td>-1.0078 (22.1934)</td><td>32.2122 (23.7760)</td><td>58.7720* (23.2632)</td><td>41.7198 (28.2390)</td></tr><tr><td>R-squared</td><td>0.792</td><td>0.851</td><td>0.884</td><td>0.933</td></tr><tr><td>Observations</td><td>306</td><td>255</td><td>204</td><td>153</td></tr><tr><td>No. states</td><td>51</td><td>51</td><td>51</td><td>51</td></tr><tr><td>States &amp; year FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr></table>

Note: We used a state-year panel. All estimations used robust standard errors. \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, +p < 0.1
