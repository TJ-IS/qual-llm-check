---
otero_id: 21941
otero_key: "ZS9ZAF89"
title: "Security threats to Internet: a Korean multi-industry investigation"
authors: "Bumsuk Jung; Ingoo Han; Sangjae Lee"
year: "2001"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00071-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Security threats to Internet: a Korean multi-industry investigation

Bumsuk Jung $^{a,1}$ , Ingoo Han $^{b,*}$ , Sangjae Lee $^{c,2}$

$^{a}$ Enterprise Solution Division, Tong Yang Systemhouse Corporation 24, Ogum-Dong, Songpa-gu, Seoul 138-130, South Korea

$^{b}$ Graduate School of Management, Techno-Management Research Institute, Korea Advanced Institute of Science and Technology,

207-43 Cheongryangri-Dong Dongdaemun-Gu, Seoul 130-012, South Korea

$^{c}$ College of Business and Economics, Hanyang University, 1271 Sa-1 Dong Ansan, Kyunggi-Do 425-791, South Korea

Accepted 14 September 2000

## Abstract

In recent years, a number of security problems with the Internet became apparent. New and current Internet users need to be aware of the likelihood of security incidents and the steps they should take to secure their sites. Before designing a secure system, it is advisable to identify the specific threats against which protection is required. The threats may be classified into interruption, interception, modification, and fabrication. The extents of these threats are examined across four industries in Korea — manufacturing, banking/financial, research institution/university, and distribution/service. Banking/financial firms generally perceive the four categories of threats more seriously than other industries. The companies in the manufacturing industry consider interruption to be the most serious. Research institutions/universities and distribution/service companies regard modification and interruption as critical threats. The appropriate security technique is recommended for each threat. © 2001 Elsevier Science B.V. All rights reserved.

Keywords: Internet; Threat; Security; Interruption; Interception; Modification; Fabrication

## 1. Introduction

The term Internet, refers to the world wide interconnection of a vast number of backbone, regional, and local (enterprise) networks that operate transmission control protocol/Internet protocol (TCP/IP), open system interconnection (OSI), and other protocols for communications [25]. The component networks are interconnected at various points to provide multiple routes and a high degree of service to users. Spurred by developments in high-speed networking technology, many academic, business, government organizations, and individuals are considering the Internet as a means for expanding their research, operational interests, and communications. Consequently, the Internet is now growing faster than any other telecommunication system. Over 100 million users world wide had access to more than 100 000 servers by 1997. Until 2002, the total amount of goods and sold on-line will reach US\$ 327 billion according to the prediction of Forrester Research Inc. [8].

The initial, research-oriented Internet and its protocols were designed for a more benign environment. It was a collegial environment in which the users and host computer systems were mutually trusting and interested in unrestrained sharing of information.

The new environment in which the Internet must operate is much less collegial. It contains all the situations, people, and risks that we find in the society as a whole $[17,18]$ . In recent years, a number of security problems with the Internet have become apparent $[4,6,7,26,32]$ . The problem lies in securing the internal business applications and office networks $[13]$ . Many concerns stem from the flexible design techniques in the World Wide Web, it is very hard to understand exactly where data and requests are coming from or where the outgoing data will go. Newspapers tell stories of high-profile ‘cracker’ attacks against government, business, and academic sites. Crackers roam the Internet with impunity, covering their tracks by moving from system to system. Intruders illegally use systems to exchange copyrighted software, to obtain sensitive information (such as business secrets), and, in general, to cause mischief.

New users of the Internet may fail to realize that their sites could be at risk to intruders who use the system as a means for attacking and causing various security incidents. Therefore, new Internet sites are often prime targets for malicious activity, including break-in, file tampering, and service disruption. Such activities may be difficult to discover and correct, highly embarrassing to the organization, and very costly in terms of lost productivity and damage to important data.

New and existing Internet users need to be aware of the steps they should take to secure their sites. Before designing a secure system, it is advisable to identify the specific threats. This is termed threat assessment. Many measures and mechanisms exist to provide sites with a higher level of assurance and protection. The likelihood of an attack can no longer be seen as insignificant.

The purpose of this paper is to present the threats and to examine the difference in each across four industries. The threats are classified into interception, fabrication, modification, and interruption. The extents of these threats are measured across four industries — manufacturing, banking/financial, research institution/university, and distribution/service. Each site has different needs, for instance, the security needs of a corporation might well be different from those of an academic institution [9]. Any security plan has to conform to the needs of the site. The exact needs, however, will vary across industries.

## 2. Security threats through the Internet

Threats to IS have the potential to cause or harm $[23]$ . The threats to data and system security encompass natural and man-made disasters, errors by internal employees, and overt act of hackers and competitors. Threats can be classified into three types $[21]$ : natural disasters, errors or omissions, and intentional acts. The first two are accidental. The last includes mischief, computer fraud, embezzlement, and theft.

Security threats to network and controls are diverse and have been studied in various contexts. Bayle [1] reviewed the security requirement for open system networks and analyzed the threats that may arise in the context of an open system networks. Further, he defined the security services and mechanisms provided by the ISO/OSI security standards to counter those threats. Loch et al. [15] have discussed the threats to information systems and resident data. They investigated MIS executive's concern for 12 threats, including computer viruses. They also evaluated MIS executive's perception of threats for microcomputer, mainframe computer, and network environments. Their respondents seemed well aware of the threats but viewed their risk to be moderately low. Carnahan [3] suggested the perceived threats and vulnerabilities for a local area network (LAN) and discussed security services and security mechanisms to improve LAN security.

Park et al. [20] classified the computer crimes related with networks and provided a scheme for technical prevention against those crimes. They also described a security architecture based on the typical OSI reference model and security services, security mechanisms, and applicable layers needed to counter those crimes. Jung [10] stated the major threats in networks, security service definitions, security mechanism definitions, a mapping of services to layers, and a mapping of mechanisms to services; these are the starting point for an Internet security architecture.

Our study concentrates on the threats entering through the Internet. Physical sources (like equipment failure, fire, accidental threats and natural hazards) are not included. We consider a number of security methods, including: physical, personnel, administrative, computer (S/W, H/W), and data communication [5,28]. The security methods in this study focus on computer and data communication security.

Organizations and people that use computers must describe their needs for information security in terms of three major requirements: confidentiality, integrity, and availability (e.g. [30]).

1. Confidentiality: a requirement whose purpose is to keep sensitive information from being disclosed to unauthorized recipients. It indicates that assets must be accessible only by authorized users. The access involves reading, printing, or viewing. Confidentiality is important for national security, law enforcement, competitive advantage, and personal privacy.

2. Integrity: a requirement meant to ensure that information and programs are changed only in a specified and authorized manner. It is important to keep data consistent or to allow data to be changed only in an approved manner. Integrity is an indication of the information's accuracy and reliability.

3. Availability: a requirement intended to ensure that systems work promptly and that service is not denied to authorized users. Those objects to which an authorized user has legitimate access should be available on demand. This requires the ability to protect against and recover from a damaging event or attack. The availability of properly functioning computer systems is essential to the operation of many large enterprises and sometimes for preserving lives.

Lee [14] suggested that the goal of network security is to prevent data from being modified or deleted when passing over the network. Network security involves confidentiality, integrity and availability [16,19,33]. The “threats” to assets are circumstances that have the potential to cause loss or harm; human attacks are examples of threats, as are natural disasters, inadvertent human errors, and internal hardware and software flaws [5,23].

Security attack can be defined as any action that compromises the security of information owned by an organization $[31]$ . Threats may originate from physical sources, unauthorized access, and authorized access $[27]$ . Since the threats in the Internet are covered here, physical sources like equipment failure, fire and destruction to facility by humans, and authorized access (i.e. internal sources) are not included.

Many authors have discussed the varied threats to assets considering them as either active or passive attack. In an active attack, the intruder engages in tampering with the information being exchanged. In a passive attack, the intruder merely observes the information passing through the channel without interfering with its flow or content. Communication security threats can be categorized as interception, alteration, jamming, and loss of integrity plus improper access attempts (including those of hackers). Pernul [22] suggested that information must be protected from the three kinds of threats: unauthorized disclosure, loss or destruction, and undesired use or modification.

In this study, network security threats are categorized as interruption, interception, modification, fabrication. These can be described as follows:

1. Interruption: an asset of the system is destroyed or becomes unavailable. Examples include: destruction of a piece of hardware, the disabling of the file management system, erasure of a program or data file, and failure of an operating system manager.

2. Interception: an unauthorized party gains access to an asset. The party could be a person, a program, or a computer. Examples include: wiretapping, the illicit copying of files or programs, and traffic analysis.

3. Modification: the content of a data transmission is altered and results in an unauthorized action or result. Examples include: changing values of items, altering a program so that it performs incorrectly, and modifying the incoming messages.

4. Fabrication: an unauthorized party inserts counterfeit objects into the system. Examples include: insertion of spurious messages or the addition of records to a file.

Threats on the security of a network can be characterized by viewing the function of the computer system that is providing information. In general, there is a flow of information from a source to a destination.

This is the basis for the most descriptions of security threats, as shown in Table 1.

Three major requirements are related to the four threats. Interruption is a threat to availability. Interception badly affects confidentiality of an asset.

Table 1
Four categories of threats

<table><tr><td>Sources</td><td>Interruption</td><td>Interception</td><td>Modification</td><td>Fabrication</td></tr><tr><td>[28]</td><td>Denial of message service</td><td>Release of message contents, traffic analysis</td><td>Message stream modification</td><td>Spurious, association, initiation</td></tr><tr><td>[1]</td><td>Denial of service</td><td>Disclosure of information, wiretapping</td><td>Modification of messages</td><td>Masquerade, replay</td></tr><tr><td>[5]</td><td>Virus, worm, denial of service</td><td>Wiretapping</td><td>Alteration</td><td>Masquerade</td></tr><tr><td>[23]</td><td>Denial of service (H/W), deletion of S/W, loss of data</td><td>Interception of S/W</td><td>Modification of data, modification of S/W</td><td>Fabrication of data</td></tr><tr><td>[16]</td><td>Denial of message service</td><td>Message content, learning, traffic analysis</td><td>Message stream modification</td><td>Spurious, connection, initiation</td></tr><tr><td>[27]</td><td>Virus, bomb, worms</td><td>Disclosure of data</td><td>Modification of Data</td><td>Phantom nodes on network</td></tr><tr><td>[3]</td><td>Disruption of functionalities</td><td>Masquerade, compromise of data, compromise of traffic</td><td>Modification of data, modification of S/W, modification of traffic</td><td>Masquerade (playback)</td></tr><tr><td>[20]</td><td>Denial of service</td><td>Interception of S/W, traffic analysis, wiretapping</td><td>Modification of data</td><td></td></tr><tr><td>[14]</td><td>Denial of service, virus, worms</td><td>Passive wiretapping, traffic analysis</td><td>Active wiretapping</td><td>Impersonation, replay</td></tr><tr><td>[31]</td><td>Denial of service</td><td>Release of message contents, traffic analysis</td><td>Modification of messages</td><td>Masquerade, replay</td></tr></table>

Modification of assets becomes a threat to integrity. Fabrication lowers integrity of an asset.

The weight given to each of the three major requirements describing needs for information security — confidentiality, integrity, and availability depends strongly on circumstances. For example, a system that must be restored within an hour after disruption requires a more demanding set of policies and controls than does one that need not be restored for days. There are differences among the industries in the overall level of threats to the security requirement in the Internet.

Organizations were arbitrarily categorized into following four industries.

1. Manufacturing: the secrets might be important for reasons of competitive advantage. The risk of loss of confidentiality will change with time, e.g. early disclosure of a product may jeopardize competitive advantage but disclosure just before an announcement may be insignificant.

2. Banking/financial: these organizations must protect the integrity of account records and individual transaction. Protection of personal privacy (credit histories) is important, but not as critical as large money transfer corruption.

3. Research institution/university: the product of these organizations is accumulated research records but security is important for private information; interception is the most important threat. Safe retention of research data is also important.

4. Distribution/service: the availability of properly functioning computer systems (e.g. for handling airline reservations) is essential to the operation of many firms.

## 3. Security services for the Internet

Security services defined in the ISO security architecture are equally relevant to the TCP/IP suite and directly applicable to the Internet architecture $[11,12]$ . Security services are the collection of security mechanisms, procedures, etc. that are implemented to help reduce the risk of associated threats. They differ from security mechanisms, which are concrete measures for implementing security services. The ISO security architecture defines five primary security services; data confidentiality, access control, authentication, data integrity, and non-repudiation (see Table 2).

## 3.1. Authentication

Two types of authentication services are defined in ISO 7498-2: data origin and peer-entity. Data origin authentication is tightly coupled to data integrity, in that it does not seem very useful to be assured of the source of data if its integrity cannot be established. Peer-entity authentication implies timeliness, because of the binding of the identity of the peer entity to a specific association. Thus, the attacks involving the replay of data associated with another association can be thwarted through reliance on the service. Here there is a natural coupling with connection-oriented integrity. In addition, this service must assure that the connection is not interfered with in such a way that a third party can masquerade as one of the two legitimate parties for the purpose of unauthorized transmission or reception.

<table><tr><td colspan="2">ISO security services</td></tr><tr><td>Security services</td><td>Description</td></tr><tr><td>Authentication</td><td>Authentication service provides the corroboration that the source of data received and a peer entity in an association is as claimed</td></tr><tr><td>Access control</td><td>Access control service provides protection against unauthorized use of a resource. This is applied to various types of access to a resource (e.g. the reading, writing, or deletion of an information resource or the execution of a program resource) or to all accesses to a resource</td></tr><tr><td>Data confidentiality</td><td>Data confidentiality service helps to protect data on workstations, file servers, etc. This service can be provided by an encryption mechanism</td></tr><tr><td>Data integrity</td><td>Data integrity service provides integrity for all user data or some selected fields in message exchange. It detects any modification, insertion, deletions or replay</td></tr><tr><td>Non-repudiation</td><td>Non-repudiation prevents either sender or receiver from denying the contents and existence of a transmitted message</td></tr></table>

## 3.2. Access control

Access control provides the prevention of unauthorized use of a resource, including that of a resource in an unauthorized manner. Sometimes there is confusion between access control and confidentiality. However, access control may encompass more than ‘read’ access to data and, thus, it may address more than just confidentiality. Conversely, some techniques for providing confidentiality do not control access to data, thus, the two services are not equivalent.

## 3.3. Data confidentiality

Data confidentiality is defined as the property that information is not made available or disclosed to unauthorized individuals, entities, or processes. These services are of special concern in networks where disclosure might occur at any one of many points in a communication path.

## 3.4. Data integrity

The integrity service provides for the detection of any modification, insertion, deletion, or replay of any data within a packet sequence. The use of this, in conjunction with peer-entity authentication, provides a high degree of protection against a wide range of active attacks.

## 3.5. Non-repudiation

Non-repudiation is defined as preventing denial by one of the entities from participation in all or part of the communication. Two forms are defined: non-repudiation with proof of origin and with proof of delivery.

Security requirements, security threats, and security services need to be viewed interdependently. When a security planner develops these independently, he or she faces the difficult task of deciding when each element is adequately addressed. This leads to inconsistent depth of planning, which may manifest itself as holes in the security [24].

![](/api/attachments/ZS9ZAF89/fulltext/images/f8b273db95fbd9783b17d52ac0141dc9377b9d3086fccfa3d10a997a8a7effdf.jpg)  
Fig. 1. Mapping threats to security services.

Because security elements map to the requirements, the mapping provides the framework for developing the protection measures. This bounds the scope of the other elements, and clarifies the effort required to address each element. Categorizing threat events or methods is of great importance, because protection mechanisms are based on the intrusion methods that may be used by perpetrators. The list of threat should define the types of threat events or methods that pertain to the Internet. A given countermeasure may partially negate several threats, but to negate a threat fully, more than one countermeasure may be needed.

As depicted in Fig. 1, security threats map to those services. Based on the several literatures, the threats are mapped to security services.

## 4. Methods

## 4.1. Research design

The research on Korean organizational use of security for their Internet usage addressed two questions: (1) what is the general state of Internet security? and (2) what is the difference in four kids of threats (interception, fabrication, modification and interruption) across industries (manufacturing, banking/financial, research institution/university, distribution/service)? The draft of the questionnaire used to determine the answer was developed based on the literature discussed above. To check for external validity and relevancy, the questionnaire was pilot-tested by several graduate students at Korea Advanced Institute of Science and Technology. A copy of the revised version of the instrument used is presented in the Appendix A.

The questionnaire consists of four parts: (1) general questions, such as name of organization, industrial classification, etc.; (2) questions about the Internet and security including: the types of connection, the purpose, the organized level of department in charge of security, the level of documentation on the security policy, etc.; (3) evaluate the extent of damage to your system and operation, assuming each threat is manifest.

## 4.2. Data collection

The data used were obtained through a mail survey. The questionnaire was sent to a random sample of 1006 senior MIS managers and data processing center managers in Korea. The respondents were those in charge of a MIS department or data processing center. The organizations were randomly drawn from the Internet Web that introduces Korean organizations. A total of 150 organizations returned the instruments, for a response rate of 14.9%, which is normal for a mail survey. Some participants may have refused to respond to selected questions due to unfamiliarity with the subject.

Table 3 shows a classification of the sample by the industry of the sampled organizations.

Table 4 provides information on the total number of the sampled organizations.

Tables 5–8 present information on the types of connection to the Internet, the purpose of using the Internet, the organized level of department in charge of security, the level of documentation of Internet controls, respectively.

Table 3  
Distribution of four industries

<table><tr><td>Industry</td><td>Total number</td><td>Percentage of organizations</td></tr><tr><td>Manufacturing</td><td>43</td><td>28.7</td></tr><tr><td>Banking/financial</td><td>38</td><td>25.3</td></tr><tr><td>Research/university</td><td>41</td><td>27.3</td></tr><tr><td>Distribution/service</td><td>25</td><td>16.7</td></tr><tr><td>Others</td><td>3</td><td>2.0</td></tr><tr><td>Total</td><td>150</td><td>100</td></tr></table>

Number of employees of organizations responding

<table><tr><td>Size</td><td>Total number</td><td>Percentage</td></tr><tr><td>Less than 100</td><td>21</td><td>13.7</td></tr><tr><td>Between 100 and 500</td><td>53</td><td>35.2</td></tr><tr><td>Between 500 and 1000</td><td>33</td><td>22.3</td></tr><tr><td>Between 1000 and 5000</td><td>35</td><td>23.8</td></tr><tr><td>Greater than 5000</td><td>8</td><td>5.0</td></tr><tr><td>Total</td><td>150</td><td>100</td></tr></table>

The percentage of dial-in connection is relatively high in manufacturing and banking/financial firm. Table 6 indicates that most organizations use the Internet for the purpose of collecting the information for their normal operation. Table 7 shows that the security function is less widely implemented in some Korean industries. Among responding organizations, the number of organizations that have department of security or security policy is small. Table 8 shows that the Internet security policy, procedure, and standard, the Internet security countermeasures implemented are almost undocumented.

Types of connection to the Internet

<table><tr><td>Types of connection</td><td>Manufacturing</td><td>Banking/financial</td><td>Research/university</td><td>Distribution/service</td><td>All</td></tr><tr><td>Dedicated connection</td><td>11.6</td><td>2.6</td><td>52.0</td><td>58.5</td><td>28.7</td></tr><tr><td>Dial-in connection</td><td>65.1</td><td>63.2</td><td>44.0</td><td>14.6</td><td>46.7</td></tr><tr><td>Both of above</td><td>0.0</td><td>0.0</td><td>4.0</td><td>14.6</td><td>5.3</td></tr><tr><td>No connection</td><td>7.0</td><td>18.4</td><td>0.0</td><td>4.9</td><td>8.7</td></tr><tr><td>Under consideration</td><td>16.3</td><td>15.8</td><td>0.0</td><td>7.3</td><td>10.7</td></tr><tr><td>Total</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr></table>

Table 6  
Purpose of using the Internet

<table><tr><td> $Purpose^a$ </td><td>Manufacturing</td><td>Banking/financial</td><td>Research/university</td><td>Distribution/service</td><td>All</td></tr><tr><td>Collecting information</td><td>81.4</td><td>76.3</td><td>100.0</td><td>90.2</td><td>85.3</td></tr><tr><td>e-mail</td><td>16.3</td><td>10.5</td><td>40.0</td><td>70.7</td><td>33.3</td></tr><tr><td>Electronic commerce</td><td>0.0</td><td>0.0</td><td>16.0</td><td>0.0</td><td>2.7</td></tr><tr><td>Publicity</td><td>9.3</td><td>18.4</td><td>24.0</td><td>36.6</td><td>22.0</td></tr><tr><td>Others</td><td>2.3</td><td>2.6</td><td>0.0</td><td>12.2</td><td>4.7</td></tr><tr><td>Total</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr></table>

$^{a}$ Since multiple answers were allowed for this question, the total percentage might exceed 100%.

Table 7  
Organized level of department in charge of security

<table><tr><td>Security department</td><td>Manufacturing</td><td>Banking/financial</td><td>Research/university</td><td>Distribution/service</td><td>All</td></tr><tr><td>Exists</td><td>0.0</td><td>15.8</td><td>8.0</td><td>9.8</td><td>8.0</td></tr><tr><td>Security staff exists</td><td>27.9</td><td>21.2</td><td>40.0</td><td>36.6</td><td>30.7</td></tr><tr><td>None</td><td>72.1</td><td>63.2</td><td>52.0</td><td>53.7</td><td>61.3</td></tr><tr><td>Total</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr></table>

Table 8  
Level of documentation of the Internet security controls

<table><tr><td>Levels of documentation</td><td>Manufacturing</td><td>Banking/financial</td><td>Research/university</td><td>Distribution/service</td><td>All</td></tr><tr><td>Documented</td><td>2.3</td><td>2.6</td><td>16.0</td><td>7.3</td><td>6.0</td></tr><tr><td>Under consideration</td><td>51.2</td><td>50.0</td><td>36.0</td><td>68.3</td><td>52.7</td></tr><tr><td>Not under consideration</td><td>46.5</td><td>47.4</td><td>48.0</td><td>24.4</td><td>41.3</td></tr><tr><td>Total</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr></table>

## 5. Data analysis and results

Analysis of variance (ANOVA) was used to test whether there are significant group differences with respect to the overall level of threats from the Internet, the result is presented in Table 9. The overall level of threats is represented by the mean values of the threats. The F-probability (F-value = 7.01, P-value = 0.0002) indicates a strong support for our expectations regarding the differences between industries for overall level of threats. The threat value for banking/financial industry (18.84) is higher than other industries.

Table 9  
Result of ANOVA — differences in threats

<table><tr><td>Industry</td><td>Mean</td><td>S.D.</td><td>F-value</td><td>P-value</td></tr><tr><td>Manufacturing</td><td>16.14</td><td>3.59</td><td>7.01</td><td>0.0002</td></tr><tr><td>Banking/financial</td><td>18.84</td><td>2.27</td><td></td><td></td></tr><tr><td>Research/university</td><td>15.80</td><td>3.64</td><td></td><td></td></tr><tr><td>Distribution/service</td><td>16.08</td><td>3.56</td><td></td><td></td></tr></table>

The t-tests of group differences were conducted between industries to see the difference in the overall level of threats. The threat values between two industries were compared using t-test. Table 10 shows that banking/financial firms perceive the overall level of threats most seriously. While there are statistically significant differences between banking/financial firms and others (for example, t-value is 4.09 for the difference between banking/financial and manufacturing firms), there are no significant differences between other pairs.

Table 10  
Results of t-test of differences in threats $^{a}$

<table><tr><td>Industry</td><td>Manufacturing</td><td>Banking/financial</td><td>Research/university</td><td>Distribution/service</td></tr><tr><td>Manufacturing</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Banking/financial</td><td>-4.09 (0.000)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Research/university</td><td>0.43 (0.668)</td><td>4.49 (0.000)</td><td>-</td><td>-</td></tr><tr><td>Distribution/service</td><td>0.07 (0.943)</td><td>3.45 (0.001)</td><td>-0.30 (0.765)</td><td>-</td></tr></table>

$^{a}$ The t-value is provided for the difference between industries in column and row. Number in parenthesis indicates two-tailed significance.

For each category of threats, ANOVA was used to test whether there were significant differences among industries. The F-probabilities in Table 11 provide strong support for the differences.

The threat value for interruption is higher than that for other threats in manufacturing and distribution/service. This shows that manufacturing and distribution/service companies perceive interruption as their most critical threats. This indicates that availability of information is most important for these industries. The key to effective use of the Internet to integrate external information with internal IS applications so that effectiveness and efficiency of the operation can be improved. Better customer service and improved inter-firm relationships are possible through system integration, because customers' needs can be promptly met. This is especially critical in just in time (JIT) and similar production systems such as quick-response retailing systems. The threats of interruption to these systems should be greater, because the response and turnaround times are critical for the success of the system.

The threats of fabrication are slightly more important than others for banking/financial companies. Integrity is critical in payment systems when a large number of transactions occur repetitively and minor errors cannot be tolerated. The threats of interception are less critical than others, reflecting that the occurrence of computer abuse using others' identification is of less concern among IS managers. The threat of modification is greatest than others in research/universities, more than the threat of interception. The respondents in the research institution and universities believe themselves to be at low risk from external intruders. However, they are anxious that the research results might be altered or modified.

Table 11  
Results of ANOVA — differences in threats

<table><tr><td>Industry</td><td>Mean</td><td>S.D.</td><td>F-value</td><td>F-probability</td></tr><tr><td colspan="5">Interruption</td></tr><tr><td>Banking/financial</td><td>4.76</td><td>0.58</td><td></td><td></td></tr><tr><td>Manufacturing</td><td>4.23</td><td>1.02</td><td></td><td></td></tr><tr><td>Distribution/service</td><td>4.10</td><td>1.05</td><td></td><td></td></tr><tr><td>Research/university</td><td>4.01</td><td>0.96</td><td>5.11</td><td>0.0022</td></tr><tr><td colspan="5">Interception</td></tr><tr><td>Banking/financial</td><td>4.53</td><td>0.79</td><td></td><td></td></tr><tr><td>Manufacturing</td><td>4.00</td><td>1.18</td><td></td><td></td></tr><tr><td>Distribution/service</td><td>3.94</td><td>0.91</td><td></td><td></td></tr><tr><td>Research/university</td><td>3.65</td><td>1.06</td><td>5.11</td><td>0.0022</td></tr><tr><td colspan="5">Modification</td></tr><tr><td>Banking/financial</td><td>4.76</td><td>0.62</td><td></td><td></td></tr><tr><td>Research/university</td><td>4.14</td><td>1.07</td><td></td><td></td></tr><tr><td>Manufacturing</td><td>4.08</td><td>1.11</td><td></td><td></td></tr><tr><td>Distribution/service</td><td>3.98</td><td>1.08</td><td>4.52</td><td>0.0040</td></tr><tr><td colspan="5">Fabrication</td></tr><tr><td>Banking/financial</td><td>4.79</td><td>0.57</td><td></td><td></td></tr><tr><td>Distribution/service</td><td>4.06</td><td>1.15</td><td></td><td></td></tr><tr><td>Research/university</td><td>4.01</td><td>1.11</td><td></td><td></td></tr><tr><td>Manufacturing</td><td>3.83</td><td>1.08</td><td>6.31</td><td>0.0005</td></tr></table>

The t-tests of the difference between the mean threat values for the industries were conducted. The results of the t-tests are presented in Table 12; they show that while there are statistically significant differences between banking/financial firms and others at the 0.05 significance level, there were no significant differences between others. Thus, the assumption that there are differences among industries for each threat is supported. Further, it indicates that compared to other industries, banking/financial firms perceive the magnitude of the damage from each category of threats most seriously.

## 6. Implications and conclusions

The results of the survey suggest how Korean practitioners cope with Internet threats. Banking/financial firms generally perceive the four categories of threats to the Internet as being more important than other industries. Poorly controlled risks expose them to fraud that can result in major financial losses and embarrassment. The opportunity to commit a major EFT fraud is much greater than some financial managers expect $[2]$ . The Internet security market in financial application is rapidly responding to threats by providing authentication and encryption technologies to their customers and by implementing new products.

The results indicate strong support for our assumption about the differences between industries in both the overall level of threats and the importance of each threat. Companies in the manufacturing section consider interruption most serious. Research institutions/universities and distribution/service companies regard modification and interruption of service as their most critical threats, respectively. Internet connections will never be 100% secure, an organization should assess the threats it is trying to prevent and weigh the benefits against costs of various security measures [29]. Companies should understand the security requirements of their industry and prepare for appropriate security services. Since available resources are limited, however, it is not possible for IS managers to develop all of the necessary controls. The appropriate levels of control should be determined according to the needs.

Table 12  
Differences in each threat between industries $^{a}$

<table><tr><td>Industry</td><td>Manufacturing</td><td>Banking/financial</td><td>Research/university</td><td>Distribution/service</td></tr><tr><td colspan="5">Interruption</td></tr><tr><td>Manufacturing</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Banking/financial</td><td>-2.94 (0.004)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Research/university</td><td>1.02 (0.311)</td><td>4.25 (0.000)</td><td>-</td><td>-</td></tr><tr><td>Distribution/service</td><td>0.50 (0.616)</td><td>2.88 (0.007)</td><td>-0.36 (0.722)</td><td>-</td></tr><tr><td colspan="5">Interception</td></tr><tr><td>Manufacturing</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Banking/financial</td><td>-2.39 (0.019)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Research/university</td><td>1.44 (0.152)</td><td>4.20 (0.000)</td><td>-</td><td>-</td></tr><tr><td>Distribution/service</td><td>0.22 (0.827)</td><td>2.72 (0.008)</td><td>-1.15 (0.254)</td><td>-</td></tr><tr><td colspan="5">Modification</td></tr><tr><td>Manufacturing</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Banking/financial</td><td>-3.45 (0.001)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Research/university</td><td>-0.23 (0.817)</td><td>3.22 (0.002)</td><td>-</td><td>-</td></tr><tr><td>Distribution/service</td><td>0.37 (0.715)</td><td>3.22 (0.002)</td><td>0.58 (0.566)</td><td>-</td></tr><tr><td colspan="5">Fabrication</td></tr><tr><td>Manufacturing</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Banking/financial</td><td>-4.56 (0.000)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Research/university</td><td>-0.70 (0.487)</td><td>3.96 (0.000)</td><td>-</td><td>-</td></tr><tr><td>Distribution/service</td><td>-0.75 (0.456)</td><td>2.95 (0.006)</td><td>-0.17 (0.867)</td><td>-</td></tr></table>

$^{a}$ The t-value is provided for the difference between industries in column and row. Number in parenthesis indicates two-tailed significance.

We also found that the security function is not widely implemented by organizations in Korea, even though they perceive the threats. Few organizations have experienced attacks from intruders, and, thus, with little computer abuse reported, it is difficult for managers to justify the investment of controls. However, the use of the Internet in Korea is rapidly growing, and the significance of some threats may change as the diffusion of Internet-based system proceeds.

## Appendix A

1. The type of your industry is ( )
(1) Manufacturing, (2) Banking/financial, (3) Research/university, (4) Distribution/service, (5) Others

2. Which is the type of connection to the Internet in your company? ( )
(1) Dedicated connection, (2) Dial-in connection, (3) Both of above, (4) No connection, (5) Under consideration.

3. The Internet in your company is used for ( )
(1) Collecting information, (2) e-mail, (3) Electronic commerce, (4) Publicity, (5) Others.

4. Our company has ( )
(1) Security department, (2) Security staff, (3)
No security, staffs or department.

5. The documentation of Internet security controls is ()

(1) Completed, (2) Under consideration, (3) Not under consideration.

Respondents the item 6–9 using the five-point Likert type scales.

6. The extent of damage to your system and operation, assuming that an asset of the system is destroyed or becomes unavailable.

7. The extent of damage to your system and operation, assuming that an unauthorized party gains access to an asset.

8. The extent of damage to your system and operation, assuming that the content of a data transmission is altered without detection and results in an unauthorized effect.

9. The extent of damage to your system and operation, assuming that an unauthorized party inserts counterfeit objects into the system.

## References

[1] A.J. Bayle, Security in open system networks: a tutorial survey, Information Age 10 (3), 1988, pp. 131–145.

[2] A.D. Boef, Assessing electronic funds transfer (EFT) security vulnerabilities in SAP R/3 environments, IS Audit and Control Journal, 1999, pp. 25–28.

[3] L.J. Carnahan, A local area network security architecture, in: Proceedings of the 15th National Computer Security Conference, Korea Management Information Systems Society, 1992, pp. 340–349.

[4] L.K. Cooper, D.J. Duncan, J. Whetstone, Is electronic commerce ready for the Internet? A case study of a financial services provider, Information Systems Management, 1996, pp. 25–36.

[5] J.A. Cooper, Computer and Communication Security, McGraw-Hill, New York, 1989.

[6] S.M. Furnell, M.J. Warren, Computer hacking and cyber terrorism: the real threats in the new millennium, Computers and Security 18, 1999, pp. 28–34.

[7] M.J. Garfield, P.G. McKeown, Planning for Internet security, Information Systems Management, 1997, pp. 41–46.

[8] R.D. Hof, G. McWilliams, The “click here” economy, Business Week, 22 June 1998, pp. 122–128.

[9] P. Holbrook, J. Reynolds, Site Security Handbook, RFC 1244, Internet Engineering Task Force, July 1991.

[10] J.W. Jung, Introduction to network security, in: Proceedings of the First Korea Computer Network Security Workshop, Korea Information Security Agency, 1995, pp. 5–50.

[11] A.T. Karila, Open system security: an architectural framework, 1991, available for anonymous ftp from coast.cs.purdue.edu as/pub/doc/network/arto\_karila\_opensystemssecurity.tar.z.

[12] S. Kent, Architectural security, in: D.C. Lynch, M.T. Rose (Eds.), Internet System Handbook, Addison-Wesley, Reading, MA, 1992, pp. 369–419.

[13] G.L. Kovacich, W.C. Boni, Internet targets, Computers and Security 19, 2000, pp. 133–140.

[14] P.J. Lee, Computer information security, in: Proceedings of the Sixth workshop on Information security and cryptography, Korea Information Security Agency, 1994, pp. 31–83.

[15] K.D. Loch, H.H. Carr, M.E. Warkentin, Threats to information systems: today's reality, yesterday's understanding, MIS Quarterly 16 (6), 1992, pp. 174–186.

[16] S. Muftic, Security Mechanisms for Computer Networks, Wiley, New York, 1989.

[17] NIST, Connecting to the Internet: Security considerations, CSL Bulletin, National Institute of Standards and Technology, 1993.

[18] NIST, Security on the Internet, CSL Bulletin, National Institute of Standards and Technology, 1994.

[19] National Research Council (NRC), Computers at Risk: Safe Guarding in the Information Age, System Security Study Committee, Computer Science and Telecommunications Board, Commission on Physical Sciences, Mathematics, and Applications, National Academy Press, Washington, DC, 1991.

[20] Y.H. Park, S.J. Moon, S.H. Kim, S.K. Kang, J.H. Leem, A study on prevention scheme for communication network from computer crime, Journal of Data Communication Security Institute 4 (2), 1994, pp. 47–55.

[21] D.B. Parker, Computer Security Management, Prentice Hall, Reston, Virginia, 1981.

[22] G. Pernul, Information systems security: scope, state-of-the-art, and evaluation of techniques, International Journal of Information Management 15 (3), 1995, pp. 165–180.

[23] C.P. Pfleeger, Security in Computing, Prentice Hall, Reston, Virginia, 1989.

[24] L.G. Pierson, E.L. Witzke, A security methodology for computer networks, AT&T Technical Journal, May/June 1988.

[25] D.M. Piscitello, A.L. Chapin, Open Systems Networking, Addison-Wesley, Reading, MA, 1993.

[26] A. Prakash, The Internet as a global strategic IS tool, Information Systems Management, 1996, pp. 45–49.

[27] R.K. Rainer, C.A. Snyder, H.H. Carr, Risk analysis for information technology, Journal of Management Information Systems 5 (1), 1991, pp. 129–147.

[28] L.S. Rutledge, L.J. Hoffman, A survey of issues in computer network security, Computer and Security, 1986, pp. 296–308.

[29] R.A. Santos, Internet security, IS Audit and Control Journal, Spring 1999, pp. 33–38.

[30] M.R. Smith, Computer security — threats, vulnerabilities and countermeasures, Information Age 11 (4), 1989, pp. 205–210.

[31] W. Stallings, Network and Inter-network Security Principles and Practice, Prentice Hall, Reston, Virginia, 1995.

[32] S. Webb, Crimes and misdemeanours: how to protect corporate information in the Internet age, Computers and Security 19, 2000, pp. 128–132.

[33] R. Weber, Information Systems Control and Audit, Prentice Hall, Upper Saddle River, NJ, 1999.

![](/api/attachments/ZS9ZAF89/fulltext/images/235e4416b8572eda132626b294a3e51dc6057a9fa8d3c29aeec4a58149561c50.jpg)  
Bumsuk Jung is an assistant manager at Enterprise Solution Division, Tong Yang Systemhouse Corporation. He received MS in Management Information System from Korea Advanced Institute of Science and Technology. He has an interest in information system security and network security.

![](/api/attachments/ZS9ZAF89/fulltext/images/72d1f517ced07247c611d51d0472588ae2a0caa5e242b87d4cf1d1e214673e2c.jpg)

Ingoo Han is an associate professor at the Graduate School of Management, Korea Advanced Institute of Science and Technology. He received PhD from University of Illinois at Urbana-Champaign. His research interests are information systems audit and security, information system evaluation, and AI applications in accounting and finance. The recent research issues include the audit and control under EC, prediction of stock price using neural network, and integration of AI techniques.

![](/api/attachments/ZS9ZAF89/fulltext/images/ddf8a2f4bc628325c9cb4de7bd922d2dd49e705f7319341fcb41396da80fc87a.jpg)

Sangjae Lee is a professor in the College of Business and Economics, Hanyang University. He received PhD in Management Information Systems from the Graduate School of Management, Korea Advanced Institute of Science and Technology. His research interests include electronic commerce, electronic data interchange, information systems control and audit.
