---
otero_id: 13588
otero_key: "JH67U9V7"
title: "Detecting complex account fraud in the enterprise: The role of technical and non-technical controls"
authors: "Sigi Goode; David Lacey"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detecting complex account fraud in the enterprise: The role of technical and non-technical controls

Sigi Goode ⁎, David Lacey

School of Accounting and Business Information Systems, College of Business and Economics, The Australian National University, Acton 0200, Australia

a r t i c l e i n f o

Available online 19 August 2010

Keywords: Fraud Controls Security Time exposure Loss

## a b s t r a c t

Complex fraud, involving heightened offender knowledge of organizational processes, can be especially damaging to the <sup>fi</sup>rm. Much research has focused on technical, quantitative detection methods. This paper uses multidimensional scaling of empirical fraud event data from a large telecommunications <sup>fi</sup>rm to illustrate how technical and socio-technical fraud controls are used to detect fraud at varying levels of time exposure and dollar loss. The evidence suggests that technical controls only detect one third of fraud cases with zero time exposure and loss. More complex fraud is detected with a range of technical and sociotechnical controls from inside and outside the <sup>fi</sup>rm. Interviews with twelve fraud managers and investigators are used to con<sup>fi</sup>rm the <sup>fi</sup>ndings.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Corporate and <sup>fi</sup>nancial fraud, the obtaining of money, goods and services through illicit or deceptive means, is a serious ongoing problem for the modern enterprise [4,37]. Holtfreter [34] cites <sup>fi</sup>gures of up to US\$600 billion in employee-related frauds. Newer threats to the <sup>fi</sup>nancial sector, involving techniques of social engineering to gather account details and remote network-based attacks [13], are increasingly the purview of organized criminal networks [69]. The popular literature, in particular, provides coverage to a range of these types of fraud, including intellectual property theft, <sup>fi</sup>nancial mismanagement, identity and ownership fraud. A number of authors argue that general fraud levels are increasing [35,74].

Scholarly research in the area of fraud is dif<sup>fi</sup>cult. Studies of <sup>fi</sup>nancial fraud are hampered by problems of access to offender, organization and offence data. Firms can also be reluctant to admit that they have a security or fraud problem within their operations. Managers may not wish to open their <sup>fi</sup>rm to enquiry or analysis from outside groups, including academic researchers, lest it affect their reputation in the market. It is rare for external researchers to be granted access to original, unsanitized data. In addition, empirical analysis of fraud incidents is made harder because the data itself can be poorly organized or incomplete [22]. Further, many authors hold that this control environment is the purview of the audit function [16,51], comprising a signi<sup>fi</sup>cant political and regulatory mandate [26]. Indeed, formal normative control frameworks exist for the purposes of effective audit conduct [12].

Amid the problem of increasing fraud levels on one hand, and the dif<sup>fi</sup>culty associated with researching fraud on the other, important gaps exist in research understanding of fraud identi<sup>fi</sup>cation and fraud detection. Much prior work has focused on theoretical approaches for developing technical detection systems (such as [4,7,20,30,37,49]) and operational methods for fraud prevention and awareness (such as [66]). However, as Caplan [8, p.103] notes, “fraud risk factors cannot easily be combined into effective predictive models”. We know little of the system controls actually used in <sup>fi</sup>rms to detect and handle fraud [21], and the social approaches that complement these technical means [3]. In the words of D'Arcy and Hovav [17, p.117], the “disproportionate focus on technical security countermeasures may partially explain why IS misuse remains a signi<sup>fi</sup>cant problem”. The research corpus needs input on the types of controls that comprise the <sup>fi</sup>rm's security posture and how these controls interact with each other with respect to different threat types.

A second gap in understanding exists with respect to the response of controls to new fraud species. Much prior work has also focused on individual fraud types, such as identity theft [29], intellectual property fraud [31] or insurance fraud [14]. However, given the modern <sup>fi</sup>rm's level of popularity and interconnection, it may not be feasible to focus on just one kind of fraud at the expense of all others that could befall the <sup>fi</sup>rm. Also, in order to obtain the greatest business case value, managers will likely need to be able to justify control funding based on detection success rates: employing networks of controls is hence a cost-effective approach to detect and prosecute fraud. Non-technical (or socio-technical) controls may also assist in this context. In the words of Dhillon and Backhouse [21, p.126], “computer security is not, per se, a technical problem. It is a social and organizational problem because the technical systems have to be operated and used by people”. To further complicate matters, analysis of real world data is made more dif<sup>fi</sup>cult by the number of organizational and individual actors that interact with the <sup>fi</sup>rm with respect to fraud commission, detection and prevention. Neither the <sup>fi</sup>rm nor the offenders operate in isolation: they share information and techniques, altering their behavior and strategy accordingly. An analysis method is hence needed that can effectively simplify our view of these control mechanisms.

This paper presents a case study of a large telecommunications carrier in the Asia Paci<sup>fi</sup>c region. The paper reveals the types of controls used to detect account-related fraud. This detection is compared against the degree of loss (equivalent dollars lost) and time exposure (the length of time for which the offender has been able to execute damage in the <sup>fi</sup>rm).

The aim of this paper is to illustrate and explore how technical and non-technical controls relate to each other in order to detect and investigate fraud. The goal of this paper is not to develop a new method for detecting fraud, but rather to highlight the use of nontechnical controls as part of the control mix. In doing so, we aim to answer calls from authors such as [22,39,60] for further work into non-technical organizational security controls. The paper contributes in two ways. First, analysis by way of empirical data is rare in the published research literature. This paper provides insight into both the theatre of real world threats and the methods used to detect fraud in an actual <sup>fi</sup>rm. Second, this paper provides some of the <sup>fi</sup>rst published evidence of the use of different control combinations to detect and ameliorate different fraud types and their complexities. This work hence illustrates the effectiveness of quantitative detection response with respect to fraud complexity.

This discussion leads to the study's research questions:

What is the relationship between technical and non-technical controls in preventing and detecting fraud losses?

How does this relationship change in the context of time exposure and the prevention and detection of losses?

The rest of this paper is structured as follows. The next section provides a brief overview of prior theory on control and detection management. The paper then details the research method, including the multidimensional scaling (MDS) technique for data analysis. This is followed by an overview of the fraud environment at play with respect to the case <sup>fi</sup>rm. In order to lend context to the analysis, the paper <sup>fi</sup>rst presents an overview of the types of fraud seen in the case <sup>fi</sup>rm. The paper then presents the analysis of the controls in use, dividing the analysis into quantitative controls used to detect fraud at its inception, and the collections of controls used to detect more complex fraud with positive time exposure levels. Finally, conclusions are offered.

## 2. Theory on controls

The modern enterprise is a complex interaction of individuals and groups. Heightened internetworking between <sup>fi</sup>rms has also contributed to this complexity, as <sup>fi</sup>rms join together for the bene<sup>fi</sup>ts of partnership and cooperation. These <sup>fi</sup>rms operate within a complex environment, comprising real and perceived threats from both within and outside the <sup>fi</sup>rm. The concept of organizational control has received considerable coverage in the business literature [27,50]. Managerial control systems play various important roles in the <sup>fi</sup>rm [33]. They act as a platform for audits, they support the validation and benchmarking of organizational units and business areas, and they assist in aligning managerial performance and remuneration in the context of agency effects. Ultimately, these managerial control systems are integral to effective organizational governance. Understandably, <sup>fi</sup>rms may be keen to reveal, discuss and even advertise their managerial control methods in order to encourage investor and shareholder con<sup>fi</sup>dence. Recent highly publicized problems of <sup>fi</sup>nancial mismanagement and corporate collapses have resulted in heightened scrutiny and expectations of internal systems and services of these <sup>fi</sup>rms. In the same way that managerial control preserves the <sup>fi</sup>nancial operations of the <sup>fi</sup>rm, so security controls preserve the mechanics and effectiveness of the <sup>fi</sup>rm's information systems.

However, <sup>fi</sup>rms are more reluctant to reveal their security models to outside scrutiny, and empirical literature coverage of security controls has been more sparse. To varying levels, the <sup>fi</sup>rm must open its operations to these groups, accepting and distributing information, products and services as needed. Firms commonly employ controls to manage and maintain the integrity of these operations [54]. Such controls aid in detecting and preventing fraud [8]. The primary purpose of such functions in the <sup>fi</sup>rm is to keep the organization's <sup>fi</sup>nancial and non-<sup>fi</sup>nancial systems running to speci<sup>fi</sup>cation [32,59]. In this respect, controls rely on the information present in the <sup>fi</sup>rm, provided by the <sup>fi</sup>rm's systems, actors and other functions.

Categorizing the roles played by different controls has been an important aspect of prior work. In the context of security and fraud control, a signi<sup>fi</sup>cant amount of prior theoretical work in IS has focused on the dual principles of deterrence and prevention, to varying degrees [71]. The value of this dual perspective lies in stopping illegitimate activity from affecting the system in the <sup>fi</sup>rst instance. Not all such deterrence is effective, and another body of work has sought to examine fraud once it has entered the system [62]. Krishnan et al. [42] discuss the role of controls in preventing and detecting data error. Bagchi and Udo [2] discuss detection and prevention techniques for online threats.

Other signi<sup>fi</sup>cant work has classi<sup>fi</sup>ed security controls according to functional and threat categories. In part, this work has arisen out of a need to identify effective control structures in the face of investment returns, demand for business value and rising incidences of threats. For example, Straub [61] surveyed a group of <sup>fi</sup>rms to ascertain their approaches to deterrence and prevention, in addition to motivational and environmental factors. Loch et al. [47] surveyed 131 managers to determine their understanding of threats to the enterprise. Holtfreter [34] surveyed 663 organizational victims of internal fraud in the United States. Respondents were asked to report on the type and number of control mechanisms organizations used to detect and prevent fraud.

Recent work has highlighted the ability of the <sup>fi</sup>rm to adapt to the complexity of the threat environment. Operational and transactional data can be unclean and poorly kept [1]. Different investigators have different specialties (e.g. analysts, <sup>fi</sup>eld specialists, technical specialists, etc.) with correspondingly different abilities and priorities for data-entry and management. Similarly, offenders are aware that, <sup>fi</sup>rst, the data they provide could be used to track and curtail their behavior and, second, that well organized and more complete data is likely to make the investigative process easier. Offenders can muddy the analytical waters by altering spellings, dates and other personal information in order to confound these investigative processes. Point of sale staff, sometimes involving off-shore call centers, can also be a weak point, open to social engineering. Finally, individual fraud cases may not be wholly self-contained, and may actually be part of a larger fraud program, perpetrated by multiple identities [46]. Analysis methods that depend on clean and pure data are unlikely to be effective. In these circumstances, non-technical approaches are likely to be more useful. To this end, Dhillon and Backhouse [21, p.128] argued, “While technical controls are vital, especially with regard to who accesses computer systems and to what they are allowed to do once admitted, sophisticated future users of information systems will have to address the organizational problems at a time when the form the organization takes is being revolutionized”.

Accordingly, recent research has worked to explore the role played by social countermeasures, by differentiating between technical and non-technical controls. Technical controls may be largely automated, quantitatively weighing historical data against incoming cases and using detection algorithms based on probability (such as Bentham's Law) and extraordinary behavior. Non-technical controls typically involve investigative processes, are often invoked by human investigators and may require signi<sup>fi</sup>cant effort and time to develop. In this vein, Baker and Wallace [3] differentiate between technical controls and operational and management controls. Wilton [67] divides controls into technical and non-technical types. D'Arcy and Hovav [17] and D'Arcy and Hovav [18] distinguish between technical controls and procedural controls in deterring information system misuse.

## 3. The case study <sup>fi</sup>rm

The case <sup>fi</sup>rm in this study was a large, well known telecommunications provider in the Asia Paci<sup>fi</sup>c region. The <sup>fi</sup>rm provides telecommunications products and services to a range of individuals and <sup>fi</sup>rms. The <sup>fi</sup>rm offers a range of hardware products and telecommunications services. These include conventional voice services, such as landline, long-distance and mobile voice communications, as well as data services such as both broadband and dialup internet access. These services are in addition to conventional telecommunications services such as reverse-charges and international trunk dialing. These products and services are sold both by the <sup>fi</sup>rm, and through a network of agent dealers spread across the region. Fig. 1 illustrates the position of the <sup>fi</sup>rm with respect to its operating environment. Importantly, this diagram shows how the fraud unit must interact with a variety of stakeholders, regulators and observers.

As a major provider of communications services, the <sup>fi</sup>rm is constantly open to new threats. On one hand, the <sup>fi</sup>rm possesses signi<sup>fi</sup>cant fraud detection methods. On the other hand, both this <sup>fi</sup>rm and others like it are justi<sup>fi</sup>ably concerned about revealing too much of their internal operations to external scrutiny and publication (consistent with [40]). The researchers took an approach of careful relationship building with the case <sup>fi</sup>rm in order to gain access to the unvarnished data materials used in this study. Amid certain con<sup>fi</sup>dentiality requirements, the researchers were given unrestricted access to these data materials.

As is the case with many modern <sup>fi</sup>rms, this organization takes a structured approach to new customer procedures, using a range of standard general and application controls to verify identity and intention at the account creation stage. These controls include written policies, physical and electronic access devices, user logging, semantic and syntactic data checks, application credit histories and objective identi<sup>fi</sup>cation checks. A variety of case-based data matching algorithms were also used.

The <sup>fi</sup>rm's fraud unit routinely explored the behavior of new and current customers, in addition to older, deprecated customer accounts. This study focused on cases of detection, whereby the fraud unit was actively identifying new cases of fraud befalling the <sup>fi</sup>rm. For this study, the researchers randomly selected 1000 fraud cases that were detected while the offender was a customer or agent of the <sup>fi</sup>rm (in contrast to those cases that were detected after the customer's relationship had been terminated or those accounts that have already been terminated but the extent of the transgression is not yet completely known).

## 4. Research method

This study aims to examine the relation between fraud controls and the types of fraud detected by these controls. As is the case with much criminality, the fraud environment is complex, and the fraud types seen by modern <sup>fi</sup>rms are evolving. Similarly, control structures at many <sup>fi</sup>rms are also complex, as the <sup>fi</sup>rm moves to build effective means to detect new threats [4]. Firms cannot viably control for every fraud, so some simpli<sup>fi</sup>cation is needed. Also, from an analysis perspective, it is more useful to reduce complexity in order to understand the main trends and patterns [70]. Accordingly, a method of classi<sup>fi</sup>cation is needed to reduce this complexity, thereby revealing underlying relationships and structures [6]. Classi<sup>fi</sup>cation has seen prior application in information systems security research, notably in [23,52] and forms the basis of much work in initial detection, such as [10,73].

A variety of classi<sup>fi</sup>cation methods exist in prior literature. Traditional classi<sup>fi</sup>cation methods were typically subjective, using perceptions of criminal behavior to theorize classi<sup>fi</sup>cations and groups. Similar methods included count-based techniques to sort crimes or criminals into discrete categories (such as [11]). Some of these methods have been criticized for their subjectivity, and their insensitivity to complex crime types.

Newer classi<sup>fi</sup>cation methods have relied more on quantitative approaches that support larger data sets and afford greater control over data relationships and testing. For example, prior criminology work has used Monothetic Division Methods to divide cases into natural groups without relying on strict data assumptions. Alternatively, agglomerative clustering techniques have been used to develop classi<sup>fi</sup>cations of offender types by grouping cases according to the researcher's chosen number of groups. However, such methods may not adequately identify data relationships [48] or may provide unreliable solutions [6].

![](/api/attachments/JH67U9V7/fulltext/images/41b0d6914d1d03ece070d5de947462f48b2bb396cb0e6a733fda16f8acd47fde.jpg)  
Fig. 1. Conceptual operating environment of the case <sup>fi</sup>rm

## 4.1. Multidimensional scaling

The study used a multidimensional technique to explore the use of controls in the <sup>fi</sup>rm's investigative process. MDS was selected as the most appropriate method for statistically analyzing the controls in the case <sup>fi</sup>rm. The method was deemed suitable for four reasons. First, the method is suitable for exploring novel or complex data structures and relationships, where the underlying groups are not otherwise easy to identify [5,64]. Second, the method allows the researcher to analyze groups of items in terms of proximity [25], graphically representing complex phenomena and relationships in low dimensional space. Third, the method makes few assumptions about the underlying constructs and the data set. For example, the data items may be nonmetric (such as consumer attitudes or product rankings) [44]. This contrasts with the requirements placed on data by factor analysis and other approaches. Finally, the method has a rich <sup>fi</sup>eld of prior use in the research literature [19].

Much prior work employing MDS techniques in the area of fraud has focused on exploring perceptions of crime. Sherman and Dowdle [58] used MDS to explore perceptions and effects of criminal activity. Forgas [28] examined individual differences, such as gender and political orientation, and their relation to perceptions of crime. Robinson and Bennett [55] used MDS to develop a four-category model of occupational and workplace deviance. Hughes et al. [38] examined crime perceptions held by females.

Aside from perception-based work, there have been other studies that use MDS to organize and extract patterns in criminal and offence data. For example, Coles and Hodgkinson [15] used an MDS approach to categorize IT risks in the workplace, in terms of personal effects and organizational outcomes. Raveh and Landau [53] conducted a smallest space analysis of 18 crime types using criminal statistics in the United Kingdom.

The MDS method uses theory developed by [25,43–45] and proceeds in <sup>fi</sup>ve steps as follows. First, the researcher gathers a set of n items (factors, statements, concepts, or constructs) for analysis. Second, the researcher requires a measure of the similarity or distance between each two items, possibly by way of a correlation matrix [25]. If two items are conceptually similar, then they will have a smaller distance between them than two items that are conceptually different. If items e and f are similar (s), and items g and h are different (d), then in Dunn-Rankin's terms:

$$
d _ {e f} <   d _ {g h}
$$

and

$$
S _ {e f} > S _ {g h}
$$

The third stage requires the researcher to select the number of dimensions in which the data will be represented. This is an important problem, as the researcher must <sup>fi</sup>nd a balance between raising the number of dimensions in order to capture conceptual complexity and reducing the number of dimensions in order to support conceptual simplicity. Cattell's scree/Stress test [9], affords some quantitative assessment of the number of dimensions to use. The scree test constitutes the sum of squared differences of observed and reproduced distances. Explicitly:

$$
P h i = \Sigma [ d e f - f (\delta_ {\mathrm{ef}}) ] ^ {2}
$$

The lower the value of squared differences (Phi), the lower the Stress value and the better the model-to-data <sup>fi</sup>t. The Stress value is calculated and plotted for each number of dimensions. The researcher may assess the suitability of each dimensional model based on the magnitude of the corresponding Stress value. The scree test alone does not provide a complete indication of the number of dimensions to use: it should be noted that, for n items, a perfect Stress value can be obtained by modeling the items along n dimensions.

The fourth step is to move the items into the dimensional space such that the distance between pairs of objects in the plot are related to their measure of proximity. Dunn-Rankin [25] discussed this process in terms of squared deviations, where distance measures between items are taken before and after they are moved. Deviations are taken between these two measurements for each item and then squared. In an ideal scale model, the sum of squared deviations is minimized.

The <sup>fi</sup>nal step is to interpret the resultant scale diagram. The literature appears to argue that this interpretation is largely a matter of researcher discernment. This step should be conducted with reference to the research literature or analytical argument.

## 4.2. Data preparation and constructs

The case <sup>fi</sup>les, comprising fraud event data and the additional investigation notes, were <sup>fi</sup>rst examined for completeness and data integrity. It was immediately apparent that a collection of investigators had been responsible for contributing data items to the database. Some investigators had used short-hand writing styles to make quick notes during the investigation, while others had provided lengthy details of their cases. Some entries in the dataset contained spelling errors or were otherwise incomplete. While some of these errors and omissions were undoubtedly due to human or data entry errors on the part of the investigators, it was also clear that a signi<sup>fi</sup>cant number of these errors had arisen either at the initial data collection stage (such as at the off-shore customer call centre, the retail agent or the website) or from the original customer (by way of deliberate deception). Within these errors, there were also cases of legitimate customer or applicant errors, often the product of identity theft, which had signi<sup>fi</sup>cantly hampered the investigative process.

The case <sup>fi</sup>les and investigation notes were analyzed using textual post-coding methods [41,65]. The coding was conducted by the authors, with involvement from two fraud investigators at the case <sup>fi</sup>rm. A third senior academic checked the coding once it was complete. This coding process allowed the researchers to analyze the types of information systems and processes used in the investigative process. Importantly, the coding analysis process also revealed the extent of formal and informal control use, and the degree to which these controls were used alone or in groups to build chains of investigative evidence

An example entry from the investigation <sup>fi</sup>le is provided below. In this case, an identity thief had altered an existing account to point to a different residential address and telephone number. They then initially used the account to gather further identity information (for example, requesting new bank or telephone account statements) so that they could continue the identity fraud with another provider at a later date once this fraud had been discovered. An investigator from the case <sup>fi</sup>rm called the listed number, and was suspicious about their responses. Within two days of this investigator contact, the account had been used as part of a call selling operation to two hot destinations. In the style of Strauss and Corbin [63] and Ryan and Bernard [56], relevant text is underlined and the descriptive factor follows in square brackets. Names and dates have been changed to preserve con<sup>fi</sup>dentiality.

Credit Agency file on record however many recent transactions (out of character).

## 2 x telco enquiries. [Telco\_Alert]

Enquiry from ABC Bank. [Bank\_Alert]

Emma rang home phone sw male who advised he was customer. Cust began chatting as William. During conversation became James. [Suspicious\_Customer\_Behaviour] Stated cust is a female, male said it was his wife and she was at work. [Customer\_Uncontactable]

Massive debt on Mob Iraq & Turkey [Hot\_Destination] \$2500.00 no rebill yet. [High\_Toll\_Report] Sent to Cancellations to terminate. Suspect this account is tied to the Box Hill file

The coding process revealed some 40 controls in investigative use. Some of these controls had been experimental, temporary or pursuant to particular management strategies in the <sup>fi</sup>rm. This group was narrowed down to a collection of the most commonly used controls. Table 1 describes the controls used in the case <sup>fi</sup>rm and reveals a number of interesting points. First, and most importantly, it gives some insight into the number of controls at play in the detection space at the case <sup>fi</sup>rm. The volume of controls also speaks to the complex inter-dependence of the underlying systems for each of these controls. While some of these controls are frequently employed individually, others are used in concert to produce an effective investigative outcome. The table also provides evidence of how different controls play different roles in the detection process. Some controls, such as the Dealer Audit, are for detection and elimination, while others simply work to gather more information for subsequent analysis. In the case study <sup>fi</sup>rm, seven of the eighteen fraud control categories were technical in deployment. In other words, these controls were initiated largely through the aid of automated information system processes. The remaining non-technical controls were invoked by the case <sup>fi</sup>rm manually, often with signi<sup>fi</sup>cant or complete human intervention. These controls often relied on prior social and behavioral understanding and perceptions, hence the overall socio-technical control map of the case <sup>fi</sup>rm.

The number of controls employed, and the combinations in which these controls are effected, gives some insight into the complexity of the <sup>fi</sup>rm's overall control ecology. For some fraud types, single controls were effective in detecting and eliminating the case. For other fraud types, combinations of controls were needed to develop the chain of con<sup>fi</sup>rmation. The complexity of both the fraud and control environments highlight the need for an analytical method that can reduce this complexity yet still provide an accurate indicator of control use.

The controls shown in Table 1 were further analyzed in order to reduce overlap. Involvement of senior fraud investigators at the <sup>fi</sup>rm proved useful in exploring these control de<sup>fi</sup>nitions and roles. Matrices were developed by coding as follows. First, instances of control use were used as inputs to a set of pair comparison matrices. For each fraud case, a list of the controls used in the investigation was developed. For each incident, an individual matrix was developed. This matrix had n columns and rows, where n was equal to the number of fraud controls in the study. Where controls were observed in the same incident, a number “1” was placed into those controls' columns across the matrix. All other cells contained zeros, to re<sup>fl</sup>ect no perceived relationship between control dimensions for that incident. These individual incident matrices were then added together in order to produce a group similarity matrix [64]. This process yielded a matrix of control relationships across the <sup>fi</sup>rm's fraud detection and investigation history.

The two main constructs used in the analysis were the dollar loss and the time exposure attributed to the fraud. As with the control analysis presented above, the de<sup>fi</sup>nitions of both of these constructs was developed with the involvement from the <sup>fi</sup>rm's fraud managers and investigators. Dollar loss comprised the total dollar amount of hardware (such as mobile phone handsets), services (costs of network use) and rebilling (costs of other providers' network use, billed to the <sup>fi</sup>rm) lost in the fraud. Time exposure comprised the length of time for which the offender had been active in the <sup>fi</sup>rm's system. Time exposure was de<sup>fi</sup>ned in this way in order to capture legitimate accounts that had subsequently gone bad through compromise by identity theft or other means. The fraud unit kept records of both of these constructs as a component of their standard operating procedure.

## 5. Analysis of the fraud environment

Paper length precludes in-depth analysis of the nature of offences, however several observations are worth noting here. First, analysis of the fraud data records revealed that the <sup>fi</sup>rm was subject to approximately three new fraud cases each day, every day over its period of operation. This volume of fraud activity speaks to the speed at which the threat environment moves, the magnitude of the offender population and attractiveness of the modern telecommunications <sup>fi</sup>rm as a vector for complex fraud. It also highlights the volume of new threats affecting the contemporary enterprise, emphasizing the importance of short-term learning and information sharing among security staff. In this regard, ineffective quantitative fraud detection systems could pose a signi<sup>fi</sup>cant barrier to knowledge sharing and fraud investigation.

Fraud controls used in the case <sup>fi</sup>rm.

<table><tr><td>Control type</td><td>Control name</td><td>Description</td></tr><tr><td>Technical</td><td>Internal_Fraud_CheckAssociated_AccountsBilling_Debit_ReferralHot_DestinationHigh_Toll_ReportCredit_Agency_ReportDealer_High_Spend</td><td>Matching applicant attributes against fraud database upon initial detection (i.e. not at point of application)This case relates to another investigation that is already in the firm&#x27;s fraud databaseAutomated referral from billing of suspected fraud based on charge back/rejection of upfront handsetMonitoring of customer calling activity against international dialing codes (e.g. Iran, Syria, Iraq, Sri Lanka, and Pakistan)Call usage and account balance alert, generated automatically across the firm&#x27;s service range and portfolioNational credit agency credit report at the point of application identifies suspected or proven history of fraudInternally generated report based on accounts with high spend/owed amounts were clustered against a dealer</td></tr><tr><td rowspan="5">Non-technical</td><td>Customer_UncontactableSuspicious_Customer_Behaviour</td><td>An investigator in the firm&#x27;s fraud unit has attempted to contact the suspect, but was unable to make contactAn investigator within the firm&#x27;s fraud unit contacted the suspect, but their behavior was evasive, inconsistent or otherwise suspicious</td></tr><tr><td>Bill_RTSPoint_of_Application_ReferralCustomer_Detection</td><td>Bill has been returned to sender. These may also arrive internally from a ‘collections’ team to the fraud departmentInternal email message from frontline applications unit, containing information about suspect applicationsSuspected identity theft victims questioning bill received from the firm, claiming they had not acquired the service.May also involve verification of customer identity (e.g. fax photo and compare against application)</td></tr><tr><td>Telco_AlertBank_Alert</td><td>Other telecommunications carriers informally share information on suspect persons, groups or organizationsInformal group of firms, mostly banks, who distribute information about known or suspected fraudulent customers, behaviors and schemes</td></tr><tr><td>Law_Enf_EnquiryEmployer_CheckOther_External</td><td>Police enquiries give an indicator to the firm of persons and groups of interestEmployer check resulted in either the applicant not working where stated in their application or the employer not existingOther external controls, such as notifications for the Telecommunications Industry Ombudsman, or a ‘tip off’ from an external source</td></tr><tr><td>Dealer_Audit</td><td>An ordered investigation into the affairs and documentation of a dealer</td></tr></table>

Table 2  
Types and descriptions of telecommunications fraud seen in the case <sup>fi</sup>rm.

<table><tr><td>Type</td><td>Description</td><td></td></tr><tr><td rowspan="5">Tools: the initial deception method used to compromise the system.</td><td>Identity fraud</td><td>The offender modified their own identity or created a new identity to gain access to the system. This may have involved changing the spelling of their name, using their maiden name, or using a fictitious address.</td></tr><tr><td>Identity theft</td><td>The offender gained plausible access to another person&#x27;s identity. The victim may have been an existing customer, or someone otherwise unrelated to the case firm.</td></tr><tr><td>No direct interface</td><td>The fraudster executed the fraud without having any direct contact with the firm. For example, they may have stolen someone else&#x27;s handset during a robbery. Alternatively, an offender may have executed a fraud on a partner institution&#x27;s network which routes some calls through the case firm&#x27;s network.</td></tr><tr><td>Dealer fraud</td><td>A dealer or other agent of the firm compromises the system directly, by altering paperwork, fabricating or altering applications, or capturing new customer details for later use.</td></tr><tr><td>Perpetrator&#x27;s real identity</td><td>The offender has used their own identity to gain access to the system. This may be through a lack of planning, ineptitude, or in order to set up a future identity-related fraud.</td></tr><tr><td rowspan="7">Accesses: the logical or physical method used to gain entry to the system. These access vectors may have an inherent weakness or vulnerability, or may be compromised by social means.</td><td>Phone</td><td>The offender used a landline telephone or a mobile cell phone to access the system.</td></tr><tr><td>Online</td><td>The offender created a new account using the website&#x27;s online sign-up process.</td></tr><tr><td>Physical store</td><td>The offender created an account or modified an existing account at a physical shopfront wholly owned and operated by the case firm.</td></tr><tr><td>Mail</td><td>The offender submitted their account documentation via a postal mail signup system. Associated documentation may have been photocopied.</td></tr><tr><td>Subscription</td><td>The offender gains access to a new or existing subscription (such as a mobile cell phone plan) in order to use or sell the service to others.</td></tr><tr><td>Dealer</td><td>The offender created a new account or modified an existing account using the services of a dealer or agent for the firm. Alternatively, the agent or dealer may have been the offender.</td></tr><tr><td>Internal Infrastructure</td><td>The offender was a member of the firm and gained direct access to the case firm&#x27;s system or paperwork. The offender exploited a weakness or opening in the firm&#x27;s technical infrastructure, perhaps using malware, a physical bridge in a network box or an unsecured FTP site.</td></tr><tr><td rowspan="8">Results: the fraud that results from the initial compromise. These results may be end states in themselves, or may be used as a new tool in another fraud.</td><td>Hardware theft</td><td>The offender sells the telecommunications hardware (such as a mobile handset or a modem) on the black market, including online auction sites.</td></tr><tr><td>SMS fraud</td><td>The offender spoofs a sender&#x27;s address in order to send SMS messages or in order to dupe a recipient into divulging information or unlocking their handset.</td></tr><tr><td>Premium rate fraud</td><td>The offender compels another user to use or subscribe to premium rate services.</td></tr><tr><td>Roaming fraud</td><td>An offender gains access to a mobile handset, and then makes international calls by roaming to other telecommunications networks.</td></tr><tr><td>Mobile cloning</td><td>An offender duplicates an existing customer&#x27;s mobile phone or SIM card, allowing them to use services and make calls on the original subscriber&#x27;s bill.</td></tr><tr><td>Call selling</td><td>An offender allows others to make discounted calls (possibly to sensitive or otherwise restricted destinations) using a stolen phone.</td></tr><tr><td>Mobile phishing</td><td>An offender uses an SMS message or a direct call to compel another user to surrender banking or other identity-related details.</td></tr><tr><td>SIM-boxing</td><td>An offender clones multiple SIM cards in order to bypass standard interconnection protocols (particularly for expensive international calls).</td></tr></table>

Table 2 gives an overview of the types of fraud seen in the case <sup>fi</sup>rm. Howard's taxonomy [36] is used, describing the tools (the initial method or process of compromise), access (the methods used to gain access to the system) and results of fraud (the ensuing fraud types and their degree of technical sophistication). Fraud identi<sup>fi</sup>ed in this stage of the analysis revealed a range of crimes including on-selling services at discounted rates (for example, by cloning a mobile telephone Subscriber Identi<sup>fi</sup>cation Module card), acquiring bills and account statements to reinforce fraudulent identities and commit criminal acts elsewhere, acquiring hardware devices to sell on the black market, and colluding with sales staff and dealers in order to access services without satisfying credit requirements. However, there were three principal fraud vectors for these crime types, being Dealer Fraud, Identity Theft and Identity Fraud. Importantly, these vectors could be related, heightening the complicated nature of the threat. For example, a dealer could set up operations with the express purpose of obtaining collecting identities, and then using these identities in later fraudulent activities. In a small number of cases, the offender made no attempt to conceal their identity.

The table illustrates a number of important points. First, not all fraud types require the same level of cognitive, resource and networking investment on the part of the offender: some frauds are more lucrative and easy to effect than others. Second, some fraud types are more frequently committed, suggesting that ongoing behavioral data would be more easily acquired and available for these fraud types. However, this ease of data acquisition does not diminish the importance of effective detection management, as these basic fraud types could comprise part of a larger or more complex fraud (such as using an authentic telephone bill used as part of a larger identity fraud). Other frauds that are less frequent, and may require signi<sup>fi</sup>cant investment overhead on the part of the offender: these frauds are likely to be dif<sup>fi</sup>cult to detect and dif<sup>fi</sup>cult for which to automate detection. Finally, some fraud types are likely to take a signi<sup>fi</sup>cant amount of time to execute. For example, in several cases, offenders waited almost a full year to use the services or the fraudulent identity they had acquired. These events provide some indication of the ‘sleeper’ nature of telecommunications fraud, whereby little or no activity may be observed for a long period of time on a fraudulently acquired account, prior to dramatic and intense periods of use. Such delays can complicate detection.

## 6. Analysis of control use

Three sets of this analysis were conducted. The <sup>fi</sup>rst focused on fraud cases that were detected on their date of inception, with zero time exposure, and with zero dollar loss to the <sup>fi</sup>rm. The second analysis focused on the controls used in those cases with positive time exposure, but that had not yet resulted in <sup>fi</sup>nancial losses to the <sup>fi</sup>rm. The third analysis explored those controls that detected more complex cases of fraud, resulting in both positive time exposure and <sup>fi</sup>nancial loss to the <sup>fi</sup>rm.

A fourth analysis, involving cases of zero time exposure and positive loss, was planned but not conducted due to a lack of suf<sup>fi</sup>cient data. Fraud events of this type include cases of roaming fraud and call selling, where an offender has penetrated another telecommunications <sup>fi</sup>rm, perhaps by stealing a handset or using a fraudulent identity, to sell calls. Alternatively, the offender may be in another country, using the case <sup>fi</sup>rm's telecommunications network indirectly to make unauthorized calls. In these cases, the offender executes fraudulent activity and obtains a bene<sup>fi</sup>t without direct access to the <sup>fi</sup>rm.

## 6.1. Zero time exposure, zero loss control combinations

The <sup>fi</sup>rst stage of control analysis included those cases that had been detected on their inception date, often prior to account activation, resulting in no time exposure to the <sup>fi</sup>rm and therefore no account usage loss. This set of data represents those cases where largely technical controls were used to identify the fraud as it was admitted to the <sup>fi</sup>rm. In total, 348 cases (approximately one third) of cases were detected with zero loss and time exposure. Fig. 2 shows the two dimensional Euclidean Distance Model for the zero time exposure/zero loss cases in the data set. The model shows three main sectors of control use. The <sup>fi</sup>rst cluster, termed ‘First Line Controls’, contained those controls that are most commonly used to detect and investigate frauds at this initial time exposure point. These controls, the Credit Agency Report, Billing Debit Referral and the Internal Fraud Check, are technical controls that operate according to pattern and identity matching using prior behavior. In this regard, these controls illustrate the value of detecting fraud cases with purely quantitative methods. ‘First Line Controls’ also have a high independence on usage or non-usage for zero time exposure zero loss events. This can be interpreted to mean that where these events occur, these controls perform well independently of other controls. The second cluster, termed ‘Contact Controls’, contained the Employer Check and the Customer Uncontactable control. These controls saw signi<sup>fi</sup>cantly less use than the previous three controls, but proved useful in identifying offenders who had fabricated or forged employment, residency or other background details. The third cluster contains the bulk of the other controls: while this cluster employed far less than the other controls, these were still useful in identifying extraordinary behavior.

Fig. 2 shows the three strongest controls used in the zero time exposure point of the fraud detection process: Internal Fraud Check, Credit Agency Report and the Billing Debit Referral. The curved lines emphasize the clustering of controls. Other controls, such as the Bill Return to Sender control, have either little effect or little opportunity for use. The next most common controls rely on low cost, low time and high information detection. These controls, such as the Employer Check and Customer Uncontactable, are related to gathering more information from the customer and their stated employer.

Table 3 shows the results of Stress testing the scaling model for each of one to four dimensions. The low Stress levels suggest that most of the variance in the model has been accounted for: the declining Stress values suggest that the model accounts for less variance as dimensions are added. The study selected two dimensions for representing the fraud control environment. While there is a marked increase in $R ^ { 2 }$ model suitability between one and two dimensions $( R ^ { 2 } = 0 . 0 2 4 7 6 )$ , the difference between two and three or more dimensions is somewhat lower $( R ^ { 2 } = 0 . 0 0 2 5 2 )$ . This effect is also re<sup>fl</sup>ected in the values for the Stress test [9]. Scatterplots of linear <sup>fi</sup>t also revealed the fewest disparities at a two dimensional solution to the model. While three dimensions could still be used in these circumstances, it was felt that the additional interpretability did not warrant the increased model complexity. A priori theoretical requirements and ease of interpretation, in this case, favored model parsimony (consistent with [45,57]).

## 6.2. Positive time exposure, zero loss control combinations

The second stage of the control analysis focused on those fraud cases that progressed beyond the zero time exposure threshold. These cases constituted offences that were more complex or otherwise harder to identify than the zero time exposure cases. In total, 203 cases (or approximately 20% of the cases analyzed) fell into this category. Fig. 3 shows the two dimensional Euclidean Distance Model for the positive time exposure cases in the data set, again using curved lines to emphasize the clustering effect of the results. The derived stimulus con<sup>fi</sup>guration immediately presents a more complex picture of the control environment in use in the <sup>fi</sup>rm, with a number of control clusters present.

![](/api/attachments/JH67U9V7/fulltext/images/225db76f8707e942bacc01fb73733329a06760c1e910e08638db4b1c29a516ed.jpg)  
Fig. 2. Zero time exposure, zero loss Euclidean distance model.

Stress and R<sup>2</sup> values for zero time exposure/zero loss dimensions.

<table><tr><td>Dimensions</td><td>Stress</td><td>ΔStress</td><td> $R^2$ </td><td> $ΔR^2$ </td></tr><tr><td>1</td><td>0.15519</td><td>-0.09349</td><td>0.97129</td><td>0.02476</td></tr><tr><td>2</td><td>0.06170</td><td>-0.02654</td><td>0.99605</td><td>0.00252</td></tr><tr><td>3</td><td>0.03516</td><td>-0.01456</td><td>0.99857</td><td>0.00103</td></tr><tr><td>4</td><td>0.02060</td><td></td><td>0.99960</td><td></td></tr></table>

Fraud cases in this category mainly involved accounts where the customer had legitimately subscribed to the <sup>fi</sup>rm. For example, these cases included identity frauds that had transpired either deliberately on the part of the customer, or other account frauds that had arisen perhaps by way of personal problems on the part of the customer. With no actual loss recorded, this time exposure point required detection through behavioral information and personal association in order to apprehend offenders.

Changes in behavior or social association are also taken as irregularity indicators. Hence, controls for this time exposure point detected instances where the customer had provided fraudulent billing details (such as Billing Debit Referral) or where the customer could be tied to fraudulent social networks (such as the Associated Accounts control).

A number of differences between Fig. 2 and Fig. 3 are evident. In the main, controls for the zero time exposure point were still in use. However, the combinations of these controls have changed. For example, the Internal Fraud Check still sees considerable application. The Associated Accounts control, which had featured only marginally at the zero time exposure point, now features more prominently. This Associated Accounts control becomes more effective as holders of other fraudulent accounts in ongoing or previous investigations become known to investigators. In this regard, a balance is required between gathering additional behavioral information about the offender in order to inform on future frauds, and preventing the offender from executing a loss action. However, like Fig. 3, the positive time exposure zero loss events have little emphasis on transaction process related controls, such as Hot Destination and High Tolling. This is explainable as the account itself for the purposes of transacting or tolling has remained unmoved since account creation.

Table 4 shows the results of Stress testing the scaling model. The Stress analysis reveals a robust model at two dimensions. A high R<sup>2</sup> value also indicates excellent model representation.

## 6.3. Positive time exposure, positive loss control combinations

The third analysis examined those cases that had progressed into positive loss and time exposure. Approximately half the cases analyzed (529) fell into this category of more complex, organized and adapted fraud. A large number of these cases consisted of dealer fraud, whereby approved agents of the <sup>fi</sup>rm were engaging in fraudulent activities. Importantly, these agents had intimate and current knowledge of the <sup>fi</sup>rm's technical controls, and were able to bypass their function in order to commit <sup>fi</sup>nancial fraud themselves or facilitate fraud on behalf of others. Fig. 4 shows the resulting stimulus con<sup>fi</sup>guration for this analysis.

At the positive time exposure and loss point, discretionary nontechnical and externally-based controls assumed the bulk of the detective role. Frauds in this category were usually complex, organized and well-planned. Typically, offenders in this category possessed signi<sup>fi</sup>cant information about the <sup>fi</sup>rm and its technical control measures, and many had developed the skills to execute large scale frauds while remaining unlisted in popular fraud and offender databases. Importantly, many of these offenders understood how to furnish the <sup>fi</sup>rm with convincing, believable personal information in order to bypass conventional application and operations controls. Dealers and other agents of the <sup>fi</sup>rm were common in this category.

![](/api/attachments/JH67U9V7/fulltext/images/c626294387792f4bfc94ce4f430892025025a04f408c0bbff47842ef0736e8fc.jpg)  
Fig. 3. Positive time exposure, zero loss Euclidean distance model.

Table 4  
Stress and R<sup>2</sup> values for positive time exposure/zero loss dimensions.

<table><tr><td>Dimensions</td><td>Stress</td><td>ΔStress</td><td> $R^2$ </td><td> $ΔR^2$ </td></tr><tr><td>1</td><td>0.33075</td><td>-0.16329</td><td>0.82292</td><td>0.12731</td></tr><tr><td>2</td><td>0.16746</td><td>-0.07604</td><td>0.95023</td><td>0.03513</td></tr><tr><td>3</td><td>0.09142</td><td>-0.03425</td><td>0.98536</td><td>0.00887</td></tr><tr><td>4</td><td>0.05717</td><td></td><td>0.99423</td><td></td></tr></table>

These types of stakeholders also tended to perform and/or respond to several of the quantitative technical controls on behalf of the case <sup>fi</sup>rm at account initiation, such as credit checking. For these reasons, quantitative technical controls, such as the Internal Fraud Check, that could typically be used to identify more straightforward frauds, were less common. Instead, discretionary, investigative controls such as the Telco Alert and Employer Check, were most effective. The Associated Accounts control was also used to detect and identify offender social networks.

As offenders in this time exposure point had developed methods for bypassing the quantitative controls in place in the <sup>fi</sup>rm, the interpersonal role of the individual investigator was emphasized. Investigative notes for cases in this category were frequently lengthy as investigators slowly built the chain of evidentiary con<sup>fi</sup>rmation. Controls such as Suspicious Customer Behaviour, where the investigator had made contact with the customer but had determined some inconsistent or otherwise ‘odd’ aspects to their behavior, were important in building the pool of evidence.

Table 5 shows the Stress and $R ^ { 2 }$ values for the third stage of the analysis. Two dimensions were selected for the model representation.

## 7. Con<sup>fi</sup>rmatory interviews

The dimensional models were then validated, as in [68], with four fraud investigators at the case <sup>fi</sup>rm, and investigators at eight other large <sup>fi</sup>nancial and telecommunications <sup>fi</sup>rms, and a law enforcement unit.

Table 5  
Stress and R<sup>2</sup> values for positive loss/positive time exposure dimensions.

<table><tr><td>Dimensions</td><td>Stress</td><td>ΔStress</td><td> $R^2$ </td><td> $ΔR^2$ </td></tr><tr><td>1</td><td>0.34503</td><td>-0.1532</td><td>0.84973</td><td>0.09330</td></tr><tr><td>2</td><td>0.19183</td><td>-0.07633</td><td>0.94303</td><td>0.03754</td></tr><tr><td>3</td><td>0.11550</td><td>-0.03556</td><td>0.98057</td><td>0.00728</td></tr><tr><td>4</td><td>0.07994</td><td></td><td>0.98785</td><td></td></tr></table>

Most interviews were held at the investigators' place of work. The rest were held at a place nominated by the interviewee. A semi-structured interview process was used as it allowed the researchers to probe and expand upon salient points [72]. Two of the interviewees requested a list of questions in advance. These two interviewees and a third did not want to be recorded, so detailed transcriptions were made from memory at the conclusion of the interview. Interviews varied in length, with most going for an hour. One interview went for two hours.

Interviews focused <sup>fi</sup>rst on the terms and approach used in the study. Discussion then proceeded to control structures, including technical and non-technical approaches. This was followed by a discussion of the <sup>fi</sup>ndings and control representations with respect to the loss and time exposure conditions. A range of other topics was discussed, depending on the concepts that arose during each interview.

With regard to terminology, interview respondents contextualized their discussion in terms of time exposure and dollar loss. For example, one respondent noted,

“Exposure or amount of money we could lose is very important. The most important thing. The longer you do nothing, the more you could lose.”

Another manager also emphasized the relationships between time and loss:

“As soon as we know that money has been illegally obtained either through products or services, or from an already existing innocent victim's account, our priority is speed of information capture.”

![](/api/attachments/JH67U9V7/fulltext/images/72f8c005bfa58cae8bb484ca0af9cb2d94f760b89a88b911c5b11592e40a7c07.jpg)  
Fig. 4. Positive time exposure, positive loss Euclidean distance model.

Three of the interviewees also remarked that the number of competing simultaneous threats to the <sup>fi</sup>rm made time an important aspect of fraud control. “You have to work quickly”, one investigator noted, “because there are others waiting in the wings”.

The interviews reinforced the use of and differences between technical and non-technical controls. For example, one fraud manager explained the difference between technical and non-technical controls in terms of sharing fraud information:

“The technicals are always there. So they're useful in that sense. We get together from time to time to talk about the rest of it and there might be times where someone says, ‘this one might be worth formalizing a bit more.’”

Interview respondents also appreciated the value of persistent technical controls that supported routine data capture. Technical controls were also deemed essential for providing data at later stages in the evidence chain for complex fraud cases. Interestingly, one investigator noted, “sometimes it is useful to see what a crook hasn't done”.

Two interviewees also remarked that technical controls were predictably good for catching mistakes and errors. Inadvertent damage could be controlled or ameliorated using technical controls. One manager's comments typi<sup>fi</sup>ed this view:

“You know sometimes someone makes an error…a goof, you know? Well the technical controls should catch most of those. And if one of them comes through that [a technical control] didn't get then yeah we get worried. Heads can roll then.”

With regard to the zero time exposure, zero loss cases, the investigators con<sup>fi</sup>rmed the roles of technical controls in apprehending these fraud incidents. They also highlighted the unique role played by each of the three main technical controls seen in this distance model. Referring to the technical controls in this model, one investigator noted,

“To be honest we're not aiming for 100% because it's just not feasible. We're in cost mitigation and not pro<sup>fi</sup>t generation so we need broad stroke stopgaps to catch as many as we can.”

Another interviewee corroborated this view, noting the importance of observing some frauds as they transpired in order to learn more of the threat environment. For instance, one investigator explained cases where more experienced fraudsters employ groups of people to attempt basic frauds in return for a percentage of the proceeds. By using these inexperienced ‘mules’, the offender can inexpensively but effectively probe the <sup>fi</sup>rm's controls. Another investigator offered a different explanation for the ability for these technical controls to only capture approximately one third of fraud attempts, arguing,

“What you're seeing there is groups of offenders who are trying the front door <sup>fi</sup>rst on the off-chance that it'll work…we have to have [technical controls] running because we'd be a hell of a lot more susceptible if they weren't there.”

Another fraud manager offered an alternative view on the zero time exposure, zero loss cases by framing detection in terms of the ability and experience of the offenders themselves:

“They're not necessarily dummies, these ones. Maybe they're not experienced or not informed or perhaps just desperate?”

The investigators found that the positive time exposure distance models were interesting representations of the fraud response framework. In particular, all of the interviewees observed the relationship that more complex fraud incidents are perpetrated by offenders with a more developed knowledge of the <sup>fi</sup>rm's control structure.

“We have a pretty good reputation as far as detection goes. I mean, we're on the ball, there's no question. But we really have to pay attention to the [offenders] who manage to get into the system. The technical controls will only do so much and then we have to rely on old fashioned hunches and input from our friends in the market.”

Another investigator speculated that these cases could be attributed to offenders with more developed or better organized social networks, saying:

“You can probably tell which [fraudsters] have friends here by the ones that are trying the same old tricks. The positive loss cases are more likely to be talking to each other.”

Reviewing the positive loss and positive time exposure distance model, the fraud managers also commented on the use of control groups to build and collect evidence. In particular, the respondents discussed the number of such complex frauds with respect to sociotechnical controls, observing that the map highlighted the use of nontechnical, social controls to apprehend offenders. One respondent typi<sup>fi</sup>ed this perspective, noting,

“I would have to say that the run of the mill frauds for us are pretty well seen. However, the clever and more sophisticated crooks, that pursue banks from afar using some pretty smart techniques, requires effort and requires us to think outside the square.”

Interviewees were unanimous in their beliefs in the value of nontechnical controls within the <sup>fi</sup>rm's fraud detection ecology. Funding these non-technical control structures was dif<sup>fi</sup>cult, and some interviewees commented on the dif<sup>fi</sup>culty of allocating budgetary value to non-technical controls. While technical controls could be carefully monitored and evaluated on an annual basis (or as funding requirements dictated), non-technical control structures were more dif<sup>fi</sup>cult to cost. However, the use of non-technical controls in detecting complex fraud was crucial. One interviewee argued,

“You will never stop it. It will always happen. Just when you think you have the best controls, they <sup>fi</sup>nd another way to get around it.”

## 8. Discussion and conclusions

This paper examined the relationship between fraud controls and the types of fraud they detected, using a case study of a large telecommunications <sup>fi</sup>rm and a set of con<sup>fi</sup>rmatory interviews. The paper provided insight into fraud control structures at work in a real <sup>fi</sup>rm. The study's <sup>fi</sup>ndings with respect to the research questions are as follows.

What is the relationship between technical and non-technical controls in preventing and detecting fraud losses?

Technical controls are typically suited to well known fraud types where suf<sup>fi</sup>cient behavioral data already exists, and can be drawn upon to build a record of norms. Classi<sup>fi</sup>cation and detection of such well-known cases is typically quick, and need not rely on signi<sup>fi</sup>cant human intervention or judgment. Non-technical controls, on the other hand, play an important role in detecting new, rare or complex types of fraud. Ideally, these non-technical controls may assist in gathering enough case and investigative data to be able to automate their invocation and use, thereby signi<sup>fi</sup>cantly reducing the costs and effort associated with their operation. Interview evidence also highlighted the value of technical controls as tools for error prevention.

## How does this relationship change in the context of time exposure and the prevention and detection of losses?

The evidence presented in this case study revealed that technical controls are a useful method for dealing with straightforward fraud types in a time and cost-effective manner. However, as the fraud and threat environment became more complex and adapted, non-technical controls became more useful in detecting fraud. Multidimensional scaling was used to classify control use according to frauds with respect to losses and time exposure. The scaling analysis <sup>fi</sup>rst revealed that a small number of controls were used to detect the majority of zero exposure, zero loss cases. However, technical controls only detected approximately a third of fraud cases affecting the <sup>fi</sup>rm. Interview evidence suggested that these controls were useful in capturing unprepared offenders, who didn't know about the control structure, or possibly lacked the social networks that could furnish them with information. Positive time exposure, zero loss cases typically included cases where the offender had initially subscribed legitimately to the <sup>fi</sup>rm's services. The scaling revealed the use of controls that focused on behavioral changes or social associations. Technical controls were still used, in order to detect associated accounts also held or controlled by the offender. Positive time exposure, positive loss cases represented more complex and adapted fraud cases. For these fraud events, the scaling revealed signi<sup>fi</sup>cant use of non-technical controls (such as Suspicious Customer Behaviour). This analysis also illustrated the use of controls external to the <sup>fi</sup>rm, involving information from other telecommunications <sup>fi</sup>rms, for example.

This paper has illustrated the use of different control combinations for detecting frauds of varying levels of complexity. Controls exhibit differing attributes and effectiveness, depending on the type of fraud and investigation at hand. Some investigations require more than one control to build an effective case. While internal controls can be effective, sharing security information can lead to superior investigative outcomes. Controls are likely to be deployed as part of a process, rather than a simple end-state. This process could involve feedback to other controls in the organization.

The study has highlighted a number of other important lessons regarding fraud management in the modern <sup>fi</sup>rm. First, the analysis has highlighted the idea that the investigator may not know what type of fraud is being committed when the evidence is <sup>fi</sup>rst brought to their attention. Whereas particular controls may detect some degree of irregularity, subsequently reporting the circumstances to the fraud unit, the modern fraud environment is such that a range of different types of fraud could be in progress. The analysis showed different control combinations in use for detecting different severities of fraud. These combinations exist not only to detect the existence of fraud, but also to identify the type of fraud that is taking place.

Second, the evidence highlights the fact that quantitative controls alone may not be enough to detect and extinguish fraud. The paper has presented evidence of a case <sup>fi</sup>rm where certain quantitative controls are used to initially detect a fraudulent act, but then a range of other socio-technical controls are then used to build the evidence chain. Over time, these socio-technical controls could be enshrined as a more quantitative, technical control that is automatically invoked at particular points in the customer management process. However, until such controls are automated, fraud detection relies on ad-hoc, discretionary and even serendipitous instances of fraud detection.

Empirical evidence in this paper suggested that control combinations for detecting complex fraud are more involved than those used to detect more straightforward fraud types. Our empirical evidence reinforces the notion that “technical approaches alone can't solve security problems for the simple reason that information security isn't merely a technical problem” [3, p.37].

With regard to detection effectiveness, the evidence in this paper showed that only a third of fraud cases were identi<sup>fi</sup>ed without time exposure or loss to the <sup>fi</sup>rm. The majority of cases involved some positive loss or time exposure. This <sup>fi</sup>nding, in itself, may be a useful platform on which to highlight the number of fraud cases that can be missed or overlooked through the use of an unduly narrow control environment. This evidence suggests that there is a genuine risk of neglecting particular types of fraud in the interests of maintaining an inexpensive or under-funded control environment.

In the same way that effective technical controls were needed at the application and admission end of the customer management process, so too were effective fraud unit investigators required to detect more complex offender behavior. Some prior research work has categorized controls according to their ability to increase the probability of detection and decrease the probability of commission. For example, Gopal and Sanders [31] developed a theoretical control system in response to software piracy. Their control model was divided into preventive and deterrent controls, using a criminological perspective of rational choice to develop a series of control dimensions. Dhillon et al. [24] adopted a case study approach to examine the inappropriateness of controls prior to the detection of an internal fraud as well as subsequent control introductions following detection. The evidence provided in this paper illustrates how non-technical controls can be effective in detecting complex fraud, and are useful complements to technical methods such as data mining. This <sup>fi</sup>nding adds weight to prior argument from Dhillon and Backhouse [21, p.128] that “elaborate systems of control are much more expensive; informally secure arrangements come free'. Managers can take heart that nontechnical control mechanisms can be just as valuable in the <sup>fi</sup>rm's overall security posture.

The study provided some empirical evidence of the rate at which new fraud attacks confront the <sup>fi</sup>rm. This rate of attack heightens the emphasis to be placed on information sharing and knowledge management in the fraud environment. This sharing occurs in both the threat environment and the fraud units that investigate these frauds. Quantitative methods can assist the modern fraud unit but qualitative discretionary controls are still needed to maintain fraud response effectiveness as the threat element also adapts to the control structure of the <sup>fi</sup>rm. As Im and Baskerville [39] argued, “security should not simply be viewed as a means of protecting something concrete, but need to broaden its horizon by taking into account individuals and their social relationships”.

A number of avenues for further work arise from this study. First, given the mounting <sup>fi</sup>nancial pressures to deliver security value, future work should also focus on detection methods that can identify a range of fraud types. Based on evidence in this paper, authors could examine how networks of controls and detection methods could provide greater value to security managers.

Second, some controls are costly to acquire and maintain. For example, subscriptions to credit monitoring agencies can be expensive both to acquire and to retain. Evidence in this study illustrated the value of having such controls in place (especially for zero time exposure, zero loss cases, in the instance of the Credit Agency Report control). However, the study also showed how a signi<sup>fi</sup>cant number of offenders are able to bypass such controls, allowing them to execute loss actions without detection. Given this problem, future work can help empirically illustrate the cost-effectiveness of these control structures. Such work could explore the degree to which funding should be allocated to groups of operational controls, rather than individual measures.

Third, this study has provided some empirical evidence of the threat posed by agents of the <sup>fi</sup>rm. These actors are better able to command information networks with respect to the principal <sup>fi</sup>rm and hence are in a good position to bypass these controls. However there has been very little empirical work that explores these potential effects. Unfortunately, such agents are frequently vital to ongoing distribution and customer operations: such necessity emphasizes the need for further work in this area.

Finally, focusing on a single fraud control dimension may not only provide an incomplete view of the <sup>fi</sup>rm's security posture, but may also bias understanding towards those individual controls that are best known, most prominent or easiest to identify. This bias could also affect management, funding or budgetary requirements, and understanding of the vulnerability by the threat environment. Future research could focus on social and behavioral controls used in the organizational environment, with an emphasis on rich interpretations. Sociological lenses might yield useful insights in this regard.

## References

[1] M. Artís, M. Ayuso, M. Guillén, Detection of automobile insurance fraud with discrete choice models and misclassi<sup>fi</sup>ed claims, The Journal of Risk and Insurance 69 (3) (2002).

[2] K. Bagchi, G. Udo, An analysis of the growth of computer and internet security breaches, Communications of the AIS 12 (2003).

[3] W.H. Baker, L. Wallace, Is information security under control? Investigating quality in information security management, IEEE Security and Privacy 5 (1) (2007).

[4] R.J. Bolton, D.J. Hand, Statistical fraud detection: a review, Statistical Science 17 (3) (2002).

[5] I. Borg, P. Groenen, Modern Multidimensional Scaling: Theory and Applications 2nd Ed, Springer-Verlag, New York, 2005.

[6] T. Brennan, Classi<sup>fi</sup>cation: an overview of selected methodological issues, Crime and Justice, Prediction and Classi<sup>fi</sup>cation: Criminal Justice Decision Making, Vol. 9, The University of Chicago Press, 1987.

[7] P.L. Brockett, R.A. Derrig, X. Xia, Using Kohonen's self organizing feature map to uncover automobile bodily injury claims fraud, The Journal of Risk and Insurance 65 (1998).

[8] D. Caplan, Internal controls and the detection of management fraud, Journal of Accounting Research 37 (1) (1999).

[9] R.B. Cattell, The scree test for the number of factors, Multivariate Behavioral Research 1 (1966).

[10] H. Cavusoglu, B. Mishra, S. Raghunathan, The value of intrusion detection systems in information technology security architecture, Information Systems Research 16 (1) (2005).

[11] M.R. Chaiken, J.M. Chaiken, Identifying types of offenders for public policy, Crime and Delinquency 30 (2) (1984).

[12] A. Chandra, T.G. Calderon, Toward a biometric security layer in accounting systems, Journal of Information Systems 17 (2) (2003).

[13] W. Chung, H. Chen, W. Chang, S. Chou, Fighting cybercrime: a review and the Taiwan experience, Decision Support Systems 41 (3) (2006).

[14] M. Clarke, The control of insurance fraud: a comparative view, British Journal of Criminology 30 (1) (1990).

[15] R. Coles, G.P. Hodgkinson, A psychometric study of information technology risks in the workplace, Risk Analysis 28 (1) (2008).

[16] C.P. Cullinan, S.G. Sutton, Defrauding the public interest: a critical examination of reengineered audit processes and the likelihood of detecting fraud, Critical Perspectives on Accounting 13 (3) (2002).

[17] J. D'Arcy, A. Hovav, Deterring internal information systems misuse: an end user perspective, Communications of the ACM 50 (10) (2007).

[18] J. D'Arcy, A. Hovav, Does one size <sup>fi</sup>t all? Examining the differential effects of IS security countermeasures, Journal of Business Ethics 89 (1) (2009).

[19], ML Davison Multidimensional Scaling, John Wiley and Sons, New York, 1983

[20] R.A. Derrig, K.M. Ostaszewski, Fuzzy techniques of pattern recognition in risk and claim classi<sup>fi</sup>cation, The Journal of Risk and Insurance 62 (1995).

[21l. G. Dhillon L. Backhouse Information system security management in the new millennium, Communications of the ACM 43 (7) (2000).

[22] G. Dhillon, J. Backhouse, Current directions in IS security research: towards socioorganizational perspectives, Information Systems Journal 11 (2) (2001).

[23] G. Dhillon, G. Torkzadeh, Value-focused assessment of information systems security in organizations, Information Systems Journal 16 (3) (2006).

[24] G. Dhillon, L. Silva, J. Backhouse, Computer crime at CEFORMA: a case study, International Journal of Information Management 24 (6) (2004).

[25] P. Dunn-Rankin, Scaling Methods, Lawrence Erlbaum Associates Publishers, London, 1983.

[26] E.M. Fich, A. Shivdasani, Financial fraud, director reputation, and shareholder wealth, Journal of Financial Economics 86 (2) (2007).

[27] E.G. Flamholtz, T.K. Das, A.S. Tsui, Toward an integrative framework of organizational control, accounting, Organizations and Society 10 (1) (1985).

[28] J.P. Forgas, Images of crime: a multidimensional analysis of individual differences in crime perception, International Journal of Psychology 15 (1) (1980).

[29] G.J. Gerard, W. Hillison, C. Pacini, Identity theft: the US legal environment and organizations' related responsibilities, Journal of Financial Crime 12 (1) (2004).

[30] P. Goldschmidt, Managing the false alarms: a framework for assurance and veri<sup>fi</sup>cation of surveillance monitoring, Information Systems Frontiers 9 (5) (2007).

[31] R.D. Gopal, G.L. Sanders, Preventive and deterrent controls for software piracy, Journal of Management Information Systems 13 (4) (1997)

[32] L.A. Gordon, M.P. Loeb, T. Sohail, C. Tseng, L. Zhou, Cybersecurity, capital allocations and management control systems, European Accounting Review 17 (2) (2008).

[33] S.G. Green, M.A. Welsh, Cybernetics and dependence: reframing the control concept, Academy of Management Review 13 (2) (1988).

[34] K. Holtfreter, Fraud in US organisations: an examination of control mechanisms, Journal of Financial Crime 12 (1) (2004).

[35] C. Holton, Identifying disgruntled employee systems fraud risk through text mining: a simple solution for a multi-billion dollar problem, Decision Support Systems 46 (4) (2009).

[36] J.D. Howard, An Analysis of Security Incidents on the Internet, 1989–1995, Department of Engineering and Public Policy, Carnegie Mellon University, Ph.D. Dissertation, 1997.

[37] S. Huang, D.C. Yen, L. Yang, J. Hua, An investigation of Zipf's law for fraud detection, Decision Support Systems 46 (1) (2008).

[38] P.P. Hughes, D. Marshall, C. Sherrill, Multidimensional analysis of fear and con<sup>fi</sup>dence of university women relating to crimes and dangerous situations, Journal of Interpersonal Violence 18 (1) (2003)

[39] G.P. Im, R.L. Baskerville, A longitudinal study of information system threat categories: the enduring problem of human error, Database for Advances in Information Systems 36 (4) (2005).

[40] A.G. Kotulic, J.G. Clark, Why there aren't more information security research studies, Information Management 41 (5) (2004).

[41] K. Krippendorff, Content Analysis: an Introduction to its Methodology, Sage Publications, Beverly Hills, CA, 1980

[42] R. Krishnan, J. Peters, R. Padman, D. Kaplan, On data reliability assessment in accounting information systems, Information Systems Research 16 (3) (2005).

[43] J.B. Kruskal, Nonmetric multidimensional scaling: a numerical method, Psychometrika 29 (2) (1964).

[44] J.B. Kruskal, Multidimensional scaling by optimizing goodness of <sup>fi</sup>t to a nonmetric hypothesis, Psychometrika 29 (1) (1964).

[45] J.B. Kruskal, M. Wish, Multidimensional Scaling, Sage University Paper Series on Quantitative Applications in the Social Sciences, Sage Publications, Beverly Hills CA, 1978.

[46] S. Lin, D.E. Brown, An outlier-based data association method for linking criminal incidents Decision Support Systems 41 (3) (2006)

[47] K.D. Loch, H.H. Carr, M.E. Warkentin, Threats to information systems: today's reality, vesterday's understanding, MIS Ouarterly 16 (2) (1992).

[48] G. Milligan, An examination of the effect of six types of error perturbation on <sup>fi</sup>fteen clustering algorithms, Psychometrika 45 (3) (1980).

[49] D. O'Leary,, Intrusion-detection systems, Journal of Information Systems 6 (1) (1992).

[50] W.G. Ouchi, A conceptual framework for the design of organizational control mechanisms, Management Science 25 (9) (1979).

[51] P. Picard, Auditing claims in the insurance market with fraud: the credibility issue, Journal of Public Economics 63 (1996).

[52] S. Ransbotham, S. Mitra, Choice and chance: a conceptual model of paths to information security compromise, Information Systems Research 20 (1) (2009).

[53] A. Raveh, S.F. Landau, Smallest-space analysis vs. the method of principal components: another look at Ahamad's analysis of crimes, Journal of Quantitative Criminology 2 (3) (1986).

[54] Z. Rezaee, Causes, consequences, and deterrence of <sup>fi</sup>nancial statement fraud, Critical Perspectives on Accounting 16 (3) (2005).

[55] S.L. Robinson, R.J. Bennett, A typology of deviant workplace behaviors: a multidimensional scaling study, Academy of Management Journal 38 (2) (1995).

[56] G.W. Ryan, H.R. Bernard, Data management and analysis methods, in: N.K. Denzin, Y.S. Lincoln (Eds.), Handbook of Qualitative Research, 2nd Ed, Sage Publications, UK, 2000.

[57] S. Schiffman, M.L. Reynolds, F.W. Young, Introduction to Multidimensional Scaling, Academic Press, New York, 1981.

[58l R. Sherman M Dowdle The perception of crime and punishment: a multidimensional scaling analysis, Social Science Research 3 (1974).

[59] R. Simons, Performance Measurement and Control Systems for Implementing Strategy, Prentice Hall, New Jersey, 2000.

[60] M.T. Siponen, Analysis of modern IS security development approaches: towards the next generation of social and adaptable ISS methods Information and Organization 15 (4) (2005).

[61] D.W. Straub, Effective IS security: an empirical analysis, Information Systems Research 1 (3) (1990).

[62] D.W. Straub, R.J. Welke, Coping with systems risk: security planning models for management decision making, MIS Quarterly 22 (4) (1998).

[63] A.L. Strauss, J. Corbin, Basics of Qualitative Research, SAGE Publications, London, UK, 1990.

[64] W.M.K. Trochim, The Concept System, Concept Systems, Ithaca, New York, 1993.

[65] R.P. Weber, Basic Content Analysis, 2nd Ed, Sage Publications, Newbury Park, CA 1990.

[66] R. Willison, J. Backhouse, Opportunities for computer crime: considering systems risk from a criminological perspective, European Journal of Information Systems 15 (4) (2006).

[67] R. Wilton, Identity and privacy in the digital age, International Journal of Intellectual Property Management 2 (4) (2008).

[68] Y. Xiang, M. Chau, H. Atabakhsh, H. Chen, Visualizing criminal relationships: comparison of a hyperbolic tree and a hierarchical list, Decision Support Systems 41 (1) (2005).

[69] J.J. Xu, H. Chen, Fighting organized crimes: using shortest-path algorithms to identify associations in criminal networks, Decision Support Systems 38 (3) (2004).

[70] J. Xu, G. Wang, J. Li, M. Chau, Complex problem solving: identity matching based on social contextual information, Journal of the Association for Information Systems 8 (10) (2007).

[71] Q. Yeh, A.J. Chang, Threats and countermeasures for information system security: a cross-industry study, Information Management 44 (5) (2007).

[72] R.K. Yin, Case Study Research Design and Methods, Sage Publications, Newbury Park, CA, 2003.

[73] W. Yue, M. Çakanyildirim, Intrusion prevention in information systems: reactive and proactive responses, Journal of Management Information Systems 24 (1) (2007).

[74] S. Zahra, R.L. Priem, A.M.A. Rasheed, The antecedents and consequences of top management fraud, Journal of Management 31 (6) (2005).

![](/api/attachments/JH67U9V7/fulltext/images/1836d943a93e7d221f8fb93eedb2ac600efe2792e0133cf65e3995af7e993480.jpg)

Dr. Sigi Goode is an associate professor in information systems at the Australian National University. His research interests lie in behavioural effects in information security intellectual property fraud and open source software.

Dr. David Lacey is a National Manager at the Australian Crime Commission. David has worked in the public and private sectors principally in risk management roles in relation to fraud, money laundering and corruption. His research interests include evaluation of control systems in prevention and detection of <sup>fi</sup>nancial crime and performance management of intelligence and investigative functions.
