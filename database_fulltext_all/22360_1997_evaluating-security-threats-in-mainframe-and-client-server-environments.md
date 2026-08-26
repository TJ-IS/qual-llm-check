---
otero_id: 22360
otero_key: "D5RYWUSH"
title: "Evaluating security threats in mainframe and client/server environments"
authors: "S.D. Ryan; B. Bordoloi"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00013-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Evaluating security threats in mainframe and client/server environments

S.D. Ryan $^{*}$ , B. Bordoloi

Department of Information Systems and Management Sciences, University of Texas at Arlington, Arlington, TX 76019, USA

## Abstract

Recently, client/server computing has become a serious alternative to mainframe computing in industry. It offers some benefits, but it also exposes the computing environment to additional risks: the flexibility that makes it attractive can also make it more vulnerable to security breaches. This paper reports the results of a study that explored how companies that were moving from a mainframe environment to one that included client/server technology, evaluated and took measures to protect against potential information security threats. Apparently, although security measures in the mainframe environment have been well implemented relative to their perceived threat, the same cannot be said about the client/server environment. Certain critical areas in the client/server environment in which security exposure is likely are discussed. Organizations must become aware of these critical areas and ensure that appropriate security measures are implemented to reduce the possibility of loss. © 1997 Elsevier Science B.V.

Keywords: Client/server systems; Computer security; Information security; Security concern; Management of security

## 1. Introduction

Industry is continuing to examine client/server computing as a possible system architecture. Although benefits can be achieved during the transition to client/server, there are costs and exposures. Organizations are concerned with the impact of multiple systems located throughout the organization rather than a centralized mainframe system. This has a number of implications. First, data are physically dispersed and therefore their access controls are also dispersed. Next, client/server systems may have differing access control mechanisms. And because these systems may have evolved for several years, the hardware and software architectures in departments across the organization may differ. Heterogeneity in a client/server environment amplifies the problem of disparate access control. Also, as technology moves closer to the end user, that person's computer sophistication is generally required to increase [4]. However, one negative factor that results from the users' increased proficiency is that they may, unintentionally, wreak havoc on the system.

Medium-to-large organizations have generally given considerable thought to mainframe security and integrity. However, a major concern in the literature is that standards and security measures have not been implemented properly at the client/server level. The initial focus of the client/server movement has been on implementation strategies. As the utilization of client/server architectures increases, this focus needs to include potential risk areas, such as security, recovery, and integrity concerns, especially for applications involving business transaction processing in a client/server environment. As mission critical applications are developed or migrated to run on client/server systems, it is imperative that organizations understand potential exposures and proactively implement measures to prevent loss.

The purpose of this study was to explore three research questions:

\- Is the seriousness of a potential security threat perceived differently in the client/server and the mainframe environments?

\- Is the degree of preparation against a potential security threat different in the two environments?

\- For each of the two environments, are measures taken to prepare against a potential threat commensurate with its perceived seriousness?

## 2. Significance of information security

The goal of information security is to ensure the availability of information and information processing resources, and provide means to establish and retain the integrity and confidentiality of information within the system [11, 28]. Conservative estimates of annual losses due to security breaches begin at \$80 million. Some survey firms (e.g. USA Research in Portland, OR) indicate that the losses may actually be in the billions of dollars [2]. Fried [10] estimates that a related cost of system downtime is around \$4 billion a year with a loss of 37 million hours in worker productivity. On an individual organization level, Hoffer and Straub's [15] study shows that a single breach in security can cost hundreds of thousands of dollars.

Yet, the total loss resulting from security breaches is unknown. Public knowledge of security violations and resulting losses is often suppressed. Lack of information concerning the total cost of security breaches and the number of actual incidents of security abuse may promote an erroneous level of comfort regarding systems security. Many organizations do not introduce appropriate security measures until a major breach in security has occurred.

Today's security managers must grapple with the challenge of developing a security strategy that achieves a balance between reasonable security precautions and excessively costly measures. When managers do not implement adequate security measures, they place their organizations at risk [8].

## 3. The client/server environment

Although there is no single, well accepted definition of client/server computing, it is generally described as an environment that distributes the application processing between a client and a server. A client is usually conceptualized as a single-user workstation that provides presentation services and appropriate computing, connectivity, and interfaces. The server typically verifies the access rights of the user and provides computing, connectivity and/or database services to one or more clients [21]. A client/server application is one in which the client and the server share the application workload.

A recent survey indicated that organizations often invest in client/server computing to enhance the flexibility, functionality, and responsiveness of their business systems $[5]$ . However, the flexibility that makes client/server attractive can also make it more vulnerable to attack. The dispersion of processing power and data throughout the organization allows the designer to put computer resources where they are needed. Yet, extending the boundaries of the computing environment exposes the organization to additional risks. Consideration must be given to protecting information in the extended enterprise, not merely at the central mainframe site. Although distributing data through the organization may provide greater flexibility for users, it also entails a greater burden in terms of considering access and security policies for multiple locations throughout the organization.

The mixture of hardware and software products that make up many client/server systems adds to the complexity of standardizing and administering an organizational security policy. Access control methods that validate the actions of legitimate system users vary, depending upon the particular hardware and software products installed. Therefore, a single methodology for securing the enterprise computing environment is often not feasible.

As the use of client/server computing expands in an organization, the number of computer-literate employees also increases [20]. An undesirable side effect of users' increased computer familiarity is that users may become more proficient at various types of computer abuse. For example, in an uncontrolled client/server environment, employees may now have the ability to access files that have previously been inaccessible.

## 4. Methodology

Previous studies have investigated concerns about a variety of threats in various IS architectural environments: mainframe, stand-alone microcomputers, and micro-mainframe linked [1]. This study continues this research and examines security threats to organizations. However, we specifically investigated the client/server versus the mainframe environment. Further, we investigated the perceived seriousness of potential threats in the two environments and also attempted to gauge the extent to which firms had taken measures to protect themselves against these threats. In addition, we examined whether the measures were commensurate with the perceived seriousness of the potential threats.

Based upon a literature review and input from several industry consultants, we developed a list of fifteen major security threats. These are shown in Table 1. A questionnaire was then designed incorporating these potential threats. Although some of the items may not be considered security threats in the strict sense of the term, they may matter very much to the continued existence of the organization. We therefore included them in our survey and report them here as important to good IT management and practice.

We distributed our questionnaire to attendees of client/server sessions at an industry technical conference. Conference attendees were IS technical professionals, primarily from medium-to-large corporations. The majority of the attendees were from the United States; however approximately 15% were international attendees.

<table><tr><td>1.</td><td>Access to data/system by outsiders (hackers, etc.)</td></tr><tr><td>2.</td><td>Accidental destruction of data by employees</td></tr><tr><td>3.</td><td>Accidental entry of erroneous data by employees</td></tr><tr><td>4.</td><td>Inadequate audit trails</td></tr><tr><td>5.</td><td>Inadequate or nonexistent logon procedures</td></tr><tr><td>6.</td><td>Intentional destruction of data by employees</td></tr><tr><td>7.</td><td>Intentional entry of erroneous data by employees</td></tr><tr><td>8.</td><td>Loss due to inadequate backups or log files</td></tr><tr><td>9.</td><td>Natural disaster: fire, flood, loss of power, etc.</td></tr><tr><td>10.</td><td>Sharing of passwords</td></tr><tr><td>11.</td><td>Single point of failure</td></tr><tr><td>12.</td><td>Uncontrolled read and/or update access</td></tr><tr><td>13.</td><td>Uncontrolled user privilege</td></tr><tr><td>14.</td><td>Viruses, bombs, worms</td></tr><tr><td>15.</td><td>Weak/ineffective or inadequate physical control</td></tr></table>

One hundred twenty questionnaires were distributed, 52 were returned and usable. Twenty-four (47%) survey respondents were from medium size companies, employing 1,000–10,000 employees. Twenty-eight (53%) were from large companies with more than 10,000 employees. As was expected from medium-to-large size companies, all the respondents reported that the mainframe had been their company's primary business computing system in the past. Eighteen (35%) of the respondents' corporations were piloting client/server applications. Thirty-two (62%) were in production of at least one client/server application. The other 2 were only investigating it. The respondents were from a variety of industries, with the heaviest concentrations from the finance (19%), insurance (23%) and manufacturing (23%) sectors.

The questionnaire asked the respondents to rate the seriousness of the 15 potential threats to their company, in both a mainframe and a client/server environment. A scale ranging from 1 to 10 was used: a rating of 1 meant that the potential threat was not a concern to their company; a rating of 10 meant that the threat was a very critical concern. They were also asked to rate the degree to which their company had taken measures to protect against potential risks in each of the two environments. For this question the same scale was used: a rating of 1 meant that no measures were taken against a potential threat; a rating of 10 meant that all possible measures were taken.

## 5. Findings and analysis

## 5.1. Perceived seriousness of a potential security threat

As indicated in Table 2, the average ratings of 7 of the 15 potential threats were found to be significantly different ( $\alpha = 0.05$ ) for the two computing environments. In each of these cases, the average perceived risk was rated higher in the mainframe environment. Three of the seven threats were related to major loss of computer resources or data: natural disaster, single point of failure, and loss due to inadequate backups or log files. In a mainframe environment, the damage sustained from the realization of these threats could be widespread across the organization whereas the damage in a client/server environment might tend to be localized.

The other four threats that were statistically different between the two environments dealt with employees, either accidentally or intentionally, destroying or altering data. More employees across the organization could potentially have access to a mainframe than to an individual client/server system. Thus, the severity of potential damage increased.

The threat of viruses has not been identified as a key concern in all computing environments. In 1992, Loch et al. [19] found that viruses ranked fourth out of 12 potential threats in the network environment, sixth in the microcomputer environment, and eleventh in the mainframe environment. Our study shows that viruses, bombs, and worms are of paramount concern in the client/server environment. Further, the mean rating for this potential threat in the mainframe environment was 7 on a scale of 1–10. This indicates that, although not as important, viruses are still considered an important threat in the mainframe environment also. Perhaps the media attention given to viruses in recent times has heightened the awareness of this particular threat. In the last several years, there has been extensive publicity about the damages viruses can cause, and a large number of viruses has been identified.

In the mainframe environment the threat rated highest, on average, was the threat of natural disasters, such as fire, floods, loss of power, etc. Catastrophic events such as the First Interstate Bank fire (Los Angeles), the bombing of the World Trade Center (New York), and the Los Angeles/Northridge earthquake have caused executives to reevaluate and widen the scope of their company's disaster recovery plans [14]. According to Contingency Planning Research, out of the disasters they have tracked over the past 13 years, $15.1\%$ were due to power outages, $13.2\%$ were due to fires, and $12.8\%$ were due to earthquakes. These were the top three [22]. New government regulations may also provide the impetus for reevaluating or augmenting disaster recovery plans. In addition, as competition continues to become more fierce and sophisticated, companies are concerned about their operations being incapacitated while their competitors have full operational capabilities [7].

Table 2  
Rating of potential threats (Scale 1–10: 1 – Not a concern; 10 – Very critical concern)

<table><tr><td>Client/Server (Mean)</td><td>Mainframe (Mean)</td><td>Potential threat</td><td>p-value</td></tr><tr><td>7.46</td><td>8.43</td><td>Access to data/system by outsiders (hackers, etc.)</td><td>0.07</td></tr><tr><td>5.75</td><td>7.23</td><td>Accidental destruction of data by employees</td><td>0.01*</td></tr><tr><td>5.69</td><td>7.65</td><td>Accidental entry of erroneous data by employees</td><td>0.01*</td></tr><tr><td>5.71</td><td>6.37</td><td>Inadequate audit trails</td><td>0.22</td></tr><tr><td>7.88</td><td>7.63</td><td>Inadequate or nonexistent logon procedures</td><td>0.66</td></tr><tr><td>5.69</td><td>7.47</td><td>Intentional destruction of data by employees</td><td>0.01*</td></tr><tr><td>5.82</td><td>7.59</td><td>Intentional entry of erroneous data by employees</td><td>0.01*</td></tr><tr><td>6.75</td><td>7.94</td><td>Loss due to inadequate backups</td><td>0.03*</td></tr><tr><td>6.08</td><td>8.48</td><td>Natural disaster: fire, flood, loss of power, etc.</td><td>0.01*</td></tr><tr><td>6.31</td><td>7.31</td><td>Sharing of passwords by users</td><td>0.06</td></tr><tr><td>5.49</td><td>7.00</td><td>Single point of failure</td><td>0.01*</td></tr><tr><td>6.69</td><td>7.63</td><td>Uncontrolled read and/or update access</td><td>0.08</td></tr><tr><td>6.46</td><td>7.25</td><td>Uncontrolled user privilege</td><td>0.19</td></tr><tr><td>8.02</td><td>7.00</td><td>Viruses, bombs, worms</td><td>0.08</td></tr><tr><td>6.35</td><td>6.96</td><td>Weak/ineffective or inadequate physical control</td><td>0.28</td></tr></table>

\* Statistically significant at $\alpha \leq 0.05$

Rating of measures company have taken to protect against potential risks (Scale 1–10: 1 – No measures taken; 10 – All possible measures taken)

<table><tr><td>Client/Server (Mean)</td><td>Mainframe (Mean)</td><td>Potential Threat</td><td>p-value</td></tr><tr><td>5.79</td><td>8.84</td><td>Access to data/system by outsiders (hackers, etc.)</td><td>0.01*</td></tr><tr><td>4.63</td><td>8.06</td><td>Accidental destruction of data by employees</td><td>0.01*</td></tr><tr><td>4.67</td><td>7.65</td><td>Accidental entry of erroneous data by employees</td><td>0.01*</td></tr><tr><td>4.26</td><td>7.60</td><td>Inadequate audit trails</td><td>0.01*</td></tr><tr><td>6.28</td><td>9.06</td><td>Inadequate or nonexistent logon procedures</td><td>0.01*</td></tr><tr><td>4.82</td><td>8.14</td><td>Intentional destruction of data by employees</td><td>0.01*</td></tr><tr><td>4.97</td><td>8.16</td><td>Intentional entry of erroneous data by employees</td><td>0.01*</td></tr><tr><td>5.06</td><td>8.63</td><td>Loss due to inadequate backups or log files</td><td>0.01*</td></tr><tr><td>5.13</td><td>8.56</td><td>Natural disaster: fire, flood, loss of power, etc.</td><td>0.01*</td></tr><tr><td>5.46</td><td>7.50</td><td>Sharing of passwords by users</td><td>0.01*</td></tr><tr><td>4.49</td><td>7.29</td><td>Single point of failure</td><td>0.01*</td></tr><tr><td>5.56</td><td>8.51</td><td>Uncontrolled read and/or update access</td><td>0.01*</td></tr><tr><td>4.96</td><td>8.38</td><td>Uncontrolled user privilege</td><td>0.01*</td></tr><tr><td>5.98</td><td>7.34</td><td>Viruses, bombs, worms</td><td>0.01*</td></tr><tr><td>5.58</td><td>8.58</td><td>Weak/ineffective or inadequate physical control</td><td>0.01*</td></tr></table>

Statistically significant at $\alpha \leq 0.05$

## 5.2. The degree of preparation against potential threats

The respondents were asked to rate the measures that their company had taken to protect against the potential security threats in both mainframe and client/server environments. Table 3 presents the mean ratings of measures taken for each threat in the two environments.

The results imply that companies are less prepared and have taken fewer measures to protect against potential security threats in client/server environments as compared with the mainframe setting. This is probably because mainframe DBMS and similar software is much more mature in provision of data controls. For every threat listed, there was a significant difference in the ratings of preparedness for the mainframe versus the client/server environment. Further, the mean rating for client/server environment was lower than that for the mainframe environment. It is possible that IS managers are yet to fully comprehend the security issues and/or do not have the appropriate tools to cope with security threats in the client/server environment.

Initially, the client/server environment was primarily used for decision support and query applications. However, as more critical business applications are moved to the client/server environment, the risk of losing data or processing increases. IS managers need to ensure that measures are taken to safeguard against potential risks.

## 5.3. Implementation of measures relative to the perceived seriousness of threats

As already discussed, measures taken against potential security threats were lower in the client/server environment. However, mean ratings of the perceived seriousness of the risks were also, in general, lower in the client/server environment. A natural question arises as to whether the measures taken to prepare against the potential threats are commensurate with the perceived seriousness of the threats. Results of answers to this question are summarized in Tables 4 and 5 for each of the two environments.

The ratings of measures taken against the potential threats in the mainframe environment were generally higher than the concern for the threats themselves – the rating difference being significant in four cases. In contrast, the results for the client/server environment were just the opposite: the preparedness ratings for the client/server environment, in general, were lower than the potential threat ratings – the difference being statistically significant in eight cases. These findings suggest that although security measures in mainframe environments have been well implemented relative to their perceived threat, the same has not been done in client/server environments.

Table 4  
Potential threat rating vs. preparedness rating - Mainframe

<table><tr><td>Potential threat rating</td><td>Preparedness rating</td><td></td><td></td></tr><tr><td>(Mean)</td><td>(Mean)</td><td>Potential Threat</td><td>p-value</td></tr><tr><td>8.48</td><td>8.84</td><td>Access to data/system by outsiders (hackers, etc.)</td><td>0.33</td></tr><tr><td>7.23</td><td>8.06</td><td>Accidental destruction of data by employees</td><td>0.06</td></tr><tr><td>7.42</td><td>7.65</td><td>Accidental entry of erroneous data by employees</td><td>0.62</td></tr><tr><td>6.37</td><td>7.60</td><td>Inadequate audit trails</td><td>0.02*</td></tr><tr><td>7.63</td><td>9.06</td><td>Inadequate or nonexistent logon</td><td>0.01*</td></tr><tr><td>7.47</td><td>8.14</td><td>Intentional destruction of data by employees</td><td>0.18</td></tr><tr><td>7.59</td><td>8.16</td><td>Intentional entry of erroneous data by employees</td><td>0.22</td></tr><tr><td>7.94</td><td>8.63</td><td>Loss due to inadequate backups</td><td>0.12</td></tr><tr><td>8.48</td><td>8.56</td><td>Natural disaster: fire, flood, loss of power, etc.</td><td>0.54</td></tr><tr><td>7.31</td><td>7.50</td><td>Sharing of passwords</td><td>0.73</td></tr><tr><td>7.00</td><td>7.29</td><td>Single point of failure</td><td>0.59</td></tr><tr><td>7.63</td><td>8.51</td><td>Uncontrolled read and/or update access</td><td>0.07</td></tr><tr><td>7.25</td><td>8.38</td><td>Uncontrolled user privilege</td><td>0.03*</td></tr><tr><td>7.00</td><td>7.34</td><td>Viruses, bombs, worms</td><td>0.58</td></tr><tr><td>6.96</td><td>8.58</td><td>Weak/ineffective or inadequate physical control</td><td>0.01*</td></tr></table>

\* Statistically significant at $\alpha \leq 0.05$

Table 5  
Rating vs. Preparedness - Client/Server

<table><tr><td>Potential threat rating</td><td>Preparedness rating</td><td></td><td></td></tr><tr><td>(Mean)</td><td>(Mean)</td><td>Potential Threat</td><td>p-value</td></tr><tr><td>7.46</td><td>5.79</td><td>Access to data/system by outsiders (hackers, etc.)</td><td>0.01*</td></tr><tr><td>5.75</td><td>4.63</td><td>Accidental destruction of data by employees</td><td>0.05*</td></tr><tr><td>5.69</td><td>4.67</td><td>Accidental entry of erroneous data by employees</td><td>0.07</td></tr><tr><td>5.71</td><td>4.26</td><td>Inadequate audit trails</td><td>0.01*</td></tr><tr><td>7.88</td><td>6.28</td><td>Inadequate or nonexistent logon</td><td>0.01*</td></tr><tr><td>5.69</td><td>4.82</td><td>Intentional destruction of data by employees</td><td>0.16</td></tr><tr><td>5.82</td><td>4.97</td><td>Intentional entry of erroneous data by employees</td><td>0.15</td></tr><tr><td>6.75</td><td>5.06</td><td>Loss due to inadequate backups</td><td>0.01*</td></tr><tr><td>6.08</td><td>5.13</td><td>Natural disaster: fire, flood, loss of power, etc.</td><td>0.11</td></tr><tr><td>6.31</td><td>5.46</td><td>Sharing of passwords</td><td>0.14</td></tr><tr><td>5.49</td><td>4.49</td><td>Single point of failure</td><td>0.10</td></tr><tr><td>6.69</td><td>5.56</td><td>Uncontrolled read and/or update access</td><td>0.04*</td></tr><tr><td>6.46</td><td>4.96</td><td>Uncontrolled user privilege</td><td>0.01*</td></tr><tr><td>8.02</td><td>5.98</td><td>Viruses, bombs, worms</td><td>0.01*</td></tr><tr><td>6.35</td><td>5.58</td><td>Weak/ineffective or inadequate physical control</td><td>0.16</td></tr></table>

\* Statistically significant at $\alpha \leq 0.05$

Organizations must become aware of the critical security areas, grapple with implementation difficulties, and proceed to enact solutions so that their client/server systems will not be at risk. Eight critical (statistically significant) areas exist with unreasonable security exposures in the client/server environment.

## 5.3.1. Viruses, bombs, worms

Although these threats were perceived, on average, as the most serious in the client/server environment, it appears that organizations still do not feel adequately prepared to address it. The dramatic increase in the number of known viruses has heightened awareness of this issue. Although controls and regulations, such as not permitting disks from outside the organization, can be stipulated, this may be difficult to enforce. Certainly, user awareness and training should be included as a protective measure. Virus scanners are also essential. Management attention can highlight the importance of users following these organizational security policies.

## 5.3.2. Inadequate or non-existent logon security

Logon protection is typically inexpensive, straightforward, and effective. According to Waltman [32], it is one of the most overlooked and subsequently abused areas of computer systems. Although the use of a password is a well-established authentication technique, most of today's major microcomputer operating systems were developed without any consideration for security. Either they offer no security capability at all, or the security and control features were merely added as an afterthought [17]. Ensuring that the client/server systems have adequate logon procedures is critical.

Logon security is a trade-off for the user between convenience and system security. Users often seem to have trouble keeping their passwords secret, forgetting or losing them, or choosing ones that are relatively easy for hackers to deduce, such as their names, birth dates, or names of children. [18]. The organization must continually make employees aware of potential security exposures that result from practices such as choosing passwords that are easy to deduce, etc. [9]. Measures can be taken, such as creating user profiles that limit the physical locations from which users can logon, the time of day, and the number of incorrect logon attempts. Security routines that verify proposed passwords should also be in place to reject previously used passwords or words that are common [16].

In today's enterprise-wide computing environment, the goal is to have a single logon. In practice, however, multiple logons may be obligatory. For example, one logon may be required for a connection to the mainframe plus an additional logon for each server. This often creates considerable administrative challenge, both in initially registering user-ids and passwords as well as in periodically updating the latter. If the user is required to remember and update passwords on multiple systems the situation may become unmanageable. Fortunately, software is becoming available, on some computing platforms, to propagate password changes to multiple attached systems (e.g. IBM's Network Signon Coordinator's tool). Yet, more robust solutions are required. In 1996, the Network Applications Consortium (NAC) issued a white paper which called for a single logon that lets a user access any network resource without having to sign on to multiple applications. The paper stated that Open Software Foundation's Distributed Computing Environment (DCE) was moving in the right direction. The DCE mechanism, called Kerberos, uses an authentication brokering technique such that a user logs on to a server once and then that server authenticates the user to other servers. Many, however, are looking for simpler and less expensive solutions [3].

Authentication techniques that require both a password and a token are becoming more widely used. One popular token is a hand-held device that generates and displays a nonrepeatable session code. The user must enter this code on the client computer. This code must match the code in the server, (which stays synchronized with the code in the hand-held device). Security breaches are less common in this environment because perpetrators must have access to both the password and the corresponding token before they can access the system [30].

## 5.3.3. Access to data/system by outsiders (hackers/phantom nodes on the network)

The requirements for connectivity beyond the boundaries of an organization's internal network have increased in the last decade. Forces that have contributed to this trend include the increased globalization of business, the popularity of just-in-time manufacturing, the demand by customers for enhanced service for decreased product delivery times, and the growing possibilities of the World Wide Web [13]. Electronic Data Interchange (EDI) is one example of a frequently used type of interorganizational system that necessitates external connectivity [29]. Increased external connectivity of any type gives rise to at least two concerns.

First, the increase in unauthorized access as a result of the increase in the number of entry points to and from the internal network. In the past, for many organizations, securing mainframes linked over a private line was relatively easy. However, in an environment which includes distributed client/server systems, multiple servers might be used as entry and exit points into an organization's internal network. Securing such an environment can be difficult. Modems are especially susceptible to an outside hacker's attack. A possible solution is the use of dial-back modems that can limit unauthorized access from outside users. When authorized outside users dial up the dial-back modem, they enter a special numeric code or password. The dial-back modem then breaks the connection and dials out from the system using the number stored in its modem line directory to reconnect with the authorized user.

Second, is the security of the organization's data as it flows across an external network. In a distributed client/server environment, intruders may be able to observe network traffic, they can then replay authentication protocols in order to masquerade as legitimate users. To prevent phantom nodes and ensure the legitimacy of each partner node, measures, such as two-party authentication, can be implemented. Another possibility is a third party authentication system in which a separate hardware or software product is responsible for validating the legitimacy of each client or server node [6].

## 5.3.4. Loss due to inadequate backups or log files

On client systems, users are often responsible for maintaining their own files. Yet, frequently users do not back up their own files on a systematic basis. To circumvent potential data loss, some organizations are mandating that all data be stored only on server machines. Other organizations are installing 'diskless' computers as client workstations to prevent the possibility of data storage on the client system [26].

## 5.3.5. Uncontrolled read and/or update access

The issue of uncontrolled read and/or update access is really one of access control. The purpose of access control is to limit the actions that a legitimate user of a computer system can perform [27]. On mainframe systems, extensive levels of authorization are often used. However, in a client/server environment, procedures may tend to be more relaxed. If the data is sensitive, it should be controlled regardless of where it is stored.

One method used in client/server systems is access control lists. This, like the simple UNIX file system, describes all actions each user is allowed to perform on a given object. In addition to individual user capabilities, many systems allow group capabilities whereby privileges can be given to a particular class of users (e.g. all users from the Accounting department may be given read authorization of the payroll file). Mandatory security must be enforced before any such group capabilities are added. In a distributed client/server environment it is necessary to evaluate the access requirements for all users, not only those who are locally attached to the server.

## 5.3.6. Uncontrolled user privilege levels

Uncontrolled user privilege is closely related to uncontrolled levels of read access. However, user privilege levels describe functions that are performed in the system. For example, some users may selectively be given administrative privileges to create user-ids, update passwords, backup and recover files, or grant access rights to other users. The level of granularity allowed in specifying these functions is dependent on the particular system. Care should be taken to understand user requirements and appropriately delegate user privileges.

## 5.3.7. Accidental destruction of data by employees

Proper training combined with appropriate access control policies can help prevent accidental destruction of data by employees. In a client/server environment, a user may have access to a multiplicity of software applications and tools. While some applications or tools may use the same methods or icons by which data are accessed, updated, and deleted, others may not. If data modification methods differ between software products, it is possible that a user, especially an untrained one, may become confused and unintentionally delete data. As many client/server applications have a graphical user interface, good controls and training are necessary. Training has been found to be directly related to user proficiency [23].

In terms of access control policies, employees who only need to read a file should not be given the right to update or delete it or its contents. By adequately analyzing the functionality needed by users and administering access rights accordingly, the potential number of employees who can modify or delete data may be decreased. Therefore, accidental damage may also be reduced.

## 5.3.8. Inadequate audit trails

Audit controls track what files have been accessed, what programs have been executed, how many reads and writes have been performed, and how many times a client or server has been accessed over a given time period. Although the granularity at which the data are collected can be specified, audit trails may still generate a considerable amount of data. Many vendors furnish audit-trail capabilities in their software products, but do not provide robust analytical tools to go with them.

## 6. Summary and conclusion

Findings indicate that the seriousness of security threats are perceived differently in the client/server and the mainframe environments. Organizations are less prepared and have taken fewer measures to protect against potential security threats in the client/server environment. In the mainframe environment, measures have been well implemented relative to their perceived threat. This is not the situation in the client/server environment. Our study revealed eight critical (statistically significant) areas in the client/server environment in which the protective measures taken were not commensurate with the perceived seriousness of a potential threat. Issues involved in each of these critical areas where security exposures are currently likely were discussed.

While some security models have explicitly included a computer environment factor (e.g. [12, 31]), others have not (e.g. [24] [25]). Environments such as the PC and the mainframe environment had previously been investigated. We have shown that differences also exist between client/server and mainframe environments.

Our study contained responses only from individuals in medium-to-large organizations (1000+ employees). These results may not be generalizable to all sized organizations. Many smaller organizations may not have a mainframe environment, but their business computing systems may evolve from small or stand-alone systems. Therefore, the perception and character of potential security threats may be very different from those of larger organizations. In addition, the focus of this study was on corporations moving from a mainframe-based environment to an environment which included client/server technology. The list of potential client/server security exposures may not be the same for corporations that do not have a legacy system heritage.

Information security continues to be a critical issue as organizations alter not only their internal computing architectures, but also their external alliances with business partners, suppliers, customers. As computer systems evolve, appropriate security plans and measures must also evolve. While this study investigated one computing transition, from a mainframe-centric environment to one that included client/server, organizations may face many transitions in the future. Planning and evaluation of potential security exposures in relation to these transitions is necessary and relevant, both from an academic as well as a practitioner perspective.

We hope that this study will serve as a catalyst for organizations to evaluate exposures specifically in the client/server environment. They should begin by looking at some of the key areas of potential risk that were highlighted; namely, viruses, bombs and worms, inadequate or non-existent logon security, access to data/system by outsiders, loss due to inadequate backups or log files, uncontrolled read and/or update access, uncontrolled user privilege levels, accidental destruction of data by employees, and inadequate audit trails. By proactively addressing security exposures in the client/server environment, organizations can preemptively avoid loss due to security breaches.

## References

[1] J.L. Boockholdt, “Implementing security and integrity in micro-mainframe networks,” MIS Quarterly, June 1989, pp.135–144.

[2] P. Borsook, “Seeking security,” Byte, May 1993, pp.199–128.

[3] C. Burns, “Users to vendors: Give us single logons now,” Network World, 13, 27, July 1996, pp.1–12.

[4] B.S. Collins and S. Mathews, “Securing your business process,” Computers and Security, 12, 1993, pp.629–633.

[5] K. Dec, "Gartner view: Client/server payoff," CIO, April 15, 1996, pp.72-76.

[6] D.E. Denning and S. Miles, "Key escrowing today," IEEE Communications Magazine, September 1994, pp.58–68.

[7] J. Edwards, "Be prepared," CIO, March 15, 1994, pp.68-72.

[8] J.H.P. Eloff, L. Labuschagne, and K.P. Badenhorst, “A comparative framework for risk analysis methods,” Computers and Security, 12, 1993, pp.597–603.

[9] L. Fried, “Distributed information security: Responsibility, assignments and costs,” Information Systems Management, Summer 1993, pp.56–67.

[10] L. Fried, “Information security and new technology: Potential threats and solutions,” Information Systems Management, Summer 1994, pp.57–63.

[11] J. P. Fry and E. H. Sibley, “Evolution of data-base management systems”, Computing Surveys, 8(1), 1976, pp.7–42.

[12] D.L. Goodhue and D.W. Straub, “Security concerns of system users: A study of perceptions of the adequacy of security,” Information and Management, 20, 1991, pp.13-22.

[13] B. Grant, “Controlling the data resource in an expanding business environment,” Data Resource Management, Spring 1992, pp.22–27.

[14] I.S. Gottfried, "When disaster strikes," Journal of Information Systems Management, Spring 1989, pp.86–89.

[15] J.A. Hoffer and D.W. Straub, Jr. "The 9 to 5 underground: Are you policing computer crimes?" Sloan Management Review, Summer 1989, pp.35–43.

[16] M. Kabay, “Securing a net security plan,” Network World, April 12, 1993, pp.44–46.

[17] R. Kay, “Distributed and secure”, Byte, June 1994, pp.165–178.

[18] R. Levin, “Fundamentals of data security,” Datapro, September 1991, pp. 1–8.

[19] K.D. Loch, H.H. Carr, and M.E. Warkentin, “Threats to information systems: Today’s reality, yesterday’s understanding,” MIS Quarterly, June 1992, pp.173–186.

[20] E.R. McLean and L.A. Kappelman, "The convergence of organizational and end-user computing," Journal of Management Information Systems, Winter 1992–1993, pp.145–155.

[21] F.R. McFadden and J.A. Hoffer, Modern Database Management, 4th edn., Benjamin/Cummings, New York, 1994.

[22] P. Meade, “Taking the risk out of disaster recovery services”, Risk Management, February 1993, pp.20–26.

[23] R.R. Nelson and P.H. Cheney, “Training end users: An exploratory study,” MIS Quarterly, December 1987, pp.547–559.

[24] D.B. Parker, Computer Security Management, Reston Publishing Co., Reston, VA, 1981.

[25] R.K. Rainer Jr., C.A. Snyder, and H.H. Carr, "Risk analysis for information technology," Journal of Management Information Systems, Summer 1991, pp.192–147.

[26] P.E. Renaud, Introduction to Client/Server Systems, John Wiley and Sons, New York, 1993.

[27] R. Sandhu and P. Samarati, “Access control: Principles and practice,” IEEE Communications Magazine, September 1994, pp.40–48.

[28] M. Schlack, "How to keep viruses off your LAN," Datamation, October 15, 1991, pp.87-89.

[29] J.A. Senn, “Electronic Data Interchange: The elements of implementation,” Information Systems Management, Winter 1992, pp. 45–53.

[30] D. Sheehy and G. Trites, "Access denied," CA Magazine, September 1995, pp.50-52.

[31] D.W. Straub and W.D. Nance, “Discovering and disciplining computer abuse in organizations: A field study,” MIS Quarterly, March 1990, pp.45–55.

[32] J. Waltman, “Who’s on the line?,” Security Management, May, 1994, pp.52–56.

![](/api/attachments/D5RYWUSH/fulltext/images/8c82ff1bb5410d9d2cbfe42e4ddc08c01689a563d799a251ceb9483d5f44705c.jpg)  
Sherry D. Ryan is a Ph.D candidate at the University of Texas at Arlington. She received a BS degree in Business Administration from Oral Roberts University and an MBA from the University of Southern California. Prior to joining the doctoral program, she was a systems engineer and an instructor with International Business Machines.

![](/api/attachments/D5RYWUSH/fulltext/images/26eecf2d4f945ec55717db2185a5b1096187118ad17dc9fc310512086012d24d.jpg)

Bijoy Bordoloi is an associate professor of Information Systems Management Sciences at The University of Texas at Arlington. He received his Ph.D in MIS from Indiana University, Bloomington. His current research Interests include data modelling and database design, adoption and diffusion of modern IS technologies, economics of IS, and software complexity metrics. His publications have appeared in several journals

including MIS Quarterly, Journal of Management Information Systems, Information & Management, Journal of Database Management, and Journal of Information Systems Management.
