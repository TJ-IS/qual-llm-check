---
otero_id: 15024
otero_key: "XBYF2GSJ"
title: "When Being Hot Is Not Cool: Monitoring Hot Lists for Information Security"
authors: "Yonghua Ji; Subodha Kumar; Vijay Mookerjee"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0677"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.133.8.114] On: 29 November 2016, At: 16:19 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/XBYF2GSJ/fulltext/images/d42099a28d7fada6df182261569a3d0b3b2918eb327c4e39d851958c87e1b6e5.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## When Being Hot Is Not Cool: Monitoring Hot Lists for Information Security

Yonghua Ji, Subodha Kumar, Vijay Mookerjee

To cite this article:

Yonghua Ji, Subodha Kumar, Vijay Mookerjee (2016) When Being Hot Is Not Cool: Monitoring Hot Lists for Information Security. Information Systems Research

Published online in Articles in Advance 29 Nov 2016

http://dx.doi.org/10.1287/isre.2016.0677

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XBYF2GSJ/fulltext/images/3d2bc00cb3ffd0c47b6d8350dd75ecf76237b9166e0eaabc3e37791f4bb8120e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# When Being Hot Is Not Cool: Monitoring Hot Lists for Information Security

Yonghua Ji

School of Business, University of Alberta, Edmonton, Alberta T6G 2R6, Canada, yji@ualberta.ca

Subodha Kumar

Mays Business School, Texas A&M University, College Station, Texas 77840, subodha@tamu.edu

Vijay Mookerjee

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75083, vijaym@utdallas.edu

W<sup>e</sup> <sup>study</sup> <sup>operational</sup> <sup>and</sup> <sup>managerial</sup> <sup>problems</sup> <sup>arising</sup> <sup>in</sup> <sup>the</sup> <sup>context</sup> <sup>of</sup> <sup>security</sup> <sup>monitoring</sup> <sup>where</sup> <sup>sessions,</sup> rather than raw individual events, are monitored to prevent attacks. The objective of the monitoring problem is to maximize the benefit of monitoring minus the monitoring cost. The key trade-off in our model is that as more sessions are monitored, the attack costs should decrease. However, the monitoring cost would likely increase with the number of sessions being monitored. A key step in solving the problem is to derive the probability density of a system with n sessions being monitored with a session’s age measured as the time elapsed since it last generated a suspicious event. We next optimize the number of sessions monitored by trading off the attack cost saved with the cost of monitoring. A profiling step is added prior to monitoring and a resulting two-dimensional optimization problem is studied. Through numerical simulation, we find that a simple size-based policy is quite robust for a very reasonable range of values and, under typical situations, performs almost as well as the two more sophisticated policies do. Also, we find that adopting a simplified policy without using the option of managing sessions using age threshold can greatly increase the ease of finding an optimal solution, and reduce operational overhead with little performance loss compared with a policy using such an option. The insights gained from the mechanics of profiling and monitoring are leveraged to suggest a socially optimal contract for outsourcing these activities in a reward-based contract. We also study penalty-based contracts. Such contracts (specifically, when the penalty is levied as a percentage of the monthly service fee) do not achieve the social optimum. We show how an appropriate penalty coefficient can be chosen to implement a socially optimal penalty-based contract. In addition, we provide a high-level comparison between rewardand penalty-based contracts. In a penalty-based contract, the setting of the fixed payment can be challenging because it requires additional knowledge of the total expected malicious event rate, which needs to be observed through a period of no monitoring.

Keywords: IT security; monitoring and profiling; outsourcing; optimization

History: Rob Fichman, Ram Gopal, Alok Gupta, Sam Ransbotham, Senior Editors; Ram Gopal, Associate Editor. This paper was received on March 1, 2015, and was with the authors 8 months for 2 revisions. Published online in Articles in Advance November 29, 2016.

Whether it’s phishing or botnets, spyware or malware, and now ransomware, these attacks are getting more and more sophisticated every day. So we’ve got to be just as fast and flexible and nimble in constantly evolving our defenses.

—President Barack Obama (The White House 2015)

## 1. Introduction

Since the last decade, information technology (IT) security has become an extremely important issue for business and society (Ransbotham and Mitra 2009, August and Tunca 2011, August et al. 2014). Reports of security breaches have reached new heights in 2014, following the iCloud and Sony hacks (Kim 2015). Not surprisingly, the worldwide spending on information security was around \$71.1 billion in 2014 (an increase of 7.9% over 2013), and is expected to grow a further 8.2% in 2015 to reach \$76.9 billion (Gartner 2014).

A variety of technologies and security protocols are being developed to counter the pandemic threat of security breaches. Some of the most commonly used ones are firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS) (Cavusoglu et al. 2009). An IDS monitors the events occurring in a computer system or network, and analyzes them for signs of possible malicious intent and imminent security threats (Pietro and Mancini 2008). An IPS not only detects intrusions but may also stop damaging incidents that could result from an intrusion. Most security experts agree that firewalls and antivirus software are not enough to provide full protection; hence, organizations are increasingly implementing IDS and IPS to protect their critical information against various types of attacks (Sandhu et al. 2011).

Table 1 Types of Security Policy Violation

<table><tr><td>Policy violation type</td><td>Examples of violation</td><td>Description</td></tr><tr><td rowspan="2">HTTP protocol compliance violation</td><td>Bad HTTP version</td><td>The request likely comes from programs, not browsers</td></tr><tr><td>Bad parameter parsing</td><td>The request could contain malicious code which targets the HTTP parser in a Web server.</td></tr><tr><td rowspan="2">Access violation</td><td>Cross-site request forgery</td><td>The request comes from a JavaScript in another program; such a request might try to execute unauthorized commands through an authorized account.</td></tr><tr><td>Forceful browsing</td><td>The request references a URL which is not an entry point. Someone could try to access documents directly without going through proper links</td></tr><tr><td rowspan="2">Input violation</td><td>Disallowed file upload content</td><td>The user attempted to upload a binary executable file, which is not allowed by the security policy</td></tr><tr><td>Illegal attachment</td><td>The incoming request contains a message in which there is an attachment not permitted by the security policy</td></tr><tr><td>...</td><td>...</td><td>...</td></tr></table>

## 1.1. Study of Current Practice and Context

Recent new-generation monitoring technology such as ContextCorrelation in Cisco Security MARS (Cisco 2015) enables session-based monitoring by converting raw network packets into meaningful session-level data. Motivated by the new industrial trend on deploying session monitoring technology, we study a model of session-based monitoring with prioritization. A session could generate a flow of events, some of which could be detected as, whether intentionally or unintentionally, violation of predefined security policies such as access violation, HTTP protocol compliance failure, etc. (F5 Networks 2013). For example, an event that sends a request for a URL not defined as an entry point could be considered an access violation (see Table 1 for a list of examples; we refer interested readers to (F5 Networks 2013) for a more complete description). Such violations are then forwarded to a security operations center (SOC) continuously for further analysis and monitoring by security analysts who are “on watch around the clock, all year round, to stop digital intrusions as they occur” (Santor 2015). If necessary, security analysts bring in information from other sources and sensors, correlate all events (including seemingly normal events), and make decisions such as modifying access control lists (Smith 2015).

Session-based data are considered the most important data source in security monitoring (Bejtlich 2004). Using such data, an SOC can prioritize real-time monitoring based on sessions (instead of raw events), as done in a traditional IDS. Thus triage is a key element in the process-flow of a modern SOC (Hewlett-Packard 2013). The triage is dynamic, i.e., sessions that are less likely to cause damage will be removed from the monitored list. Thus the valuable resources of security analysts—a major component of operating cost (Dell 2015)—are saved. Therefore, while profiling is a static way of conducting traffic triage, the idea of maintaining a hot list constitutes dynamic triage: low-risk sessions are initially monitored but later removed from monitoring. On the other hand, high-risk traffic is monitored longer.

## 1.2. Problem and Motivation

In this paper, we study the problem of monitoring a hot list of sessions. We first address the question of optimizing the size of a hot list with and without profiling. Then, we analyze the design of contracts for outsourcing monitoring and profiling activities.

A shop detective analogy helps motivate our study. Imagine a high-end store selling expensive merchandise (e.g., jewelry, fashion goods, electronics, etc.) that employs shop detectives to prevent stealing and other criminal activities. Customers walk into the store and their activities are monitored. If the customer makes any attempt to steal (or what appears to be an attempt), a detective makes sure that the attempt is abortive (e.g., the detective walks up to the customer and makes it obvious that the suspicious activity is being watched). The policy of the jewelry store is to prevent potential damage from activities, rather than ousting customers who perform suspicious activities. This is because innocent customers can sometimes do things that appear malicious (e.g., attempt to touch something behind the display counter). Criminal attempts made by the nonmonitored customers have a positive probability of being successful, but those originated by monitored customers are never successful. A likely, but more sophisticated variant of the above setting is when only some of the entering customers are profiled and flagged at the entrance as being in need of monitoring. Another variant is one where some people are simply not allowed to enter the store.

Figure 1 High-Level Problem Description  
![](/api/attachments/XBYF2GSJ/fulltext/images/80dd6c2bc6766e6c4acf05d92b5b52aaa0b5af6e2161c1b10add2a4130c1f9df.jpg)

In the IT security context, an entrance guard who does not permit some customers to enter corresponds to a firewall. The set of shop detectives correspond to session monitoring technologies: a combination of intrusion detection and prevention methods. When a new session arrives, then another session (that has not generated suspicious events for a while) is removed from the hot list to accommodate the new arrival in the hot list. Figure 1 summarizes the high-level interactions in our model and highlights the focus of our work. The incoming traffic represents the arrival of external or internal sessions that potentially need monitoring, subject to clearance by the firewall. Next, the traffic past the firewall is examined by a profiler that uses attributes of the traffic to determine whether it should be subject to monitoring.

Figure 1 also suggests that the tasks of profiling and monitoring can be performed in-house or outsourced to a security vendor. Firms often hire managed security service providers (MSSPs) for security monitoring. For example, in 2009, 60% of Fortune 500 companies used an MSSP and about 25% of enterprise firewalls were under remote monitoring or management (Kavanagh and Pescatore 2009). This approach is especially beneficial to firms that lack internal security expertise or have a high cost of insourced monitoring (Fitzparick 2008, Brown 2012, Lord 2015).

## 1.3. Objectives and Contribution

It has been widely recognized by both practitioners and academicians that the focus of IT security management is shifting from what is technically possible to what is economically efficient (Cavusoglu et al. 2004a, Baayer et al. 2014). Hence, the objective of the monitoring problem is to maximize the benefit of avoiding damage from suspicious events minus the monitoring cost. The key trade-off in our model is that as more sessions are monitored, the damage avoidance increases. However, the monitoring cost would also likely increase with the number of sessions being monitored.

Traditional monitoring methods focus on the detection of raw events as they are generated. Session-based monitoring is a more recent monitoring paradigm that can better detect more sophisticated attacks (Cisco 2015). However, there has not been any thorough analysis of session-based monitoring policies. Our research attempts to fill this gap. Our study also contributes to management of the relationship between a firm and its security vendor. Despite the benefits of outsourcing security, writing MSSP contracts that align the incentives of the security vendor with those of the firm can be challenging. According to the IT director of a large firm, “managing an outsourcing contract can be as hard or harder than finding a few good staffers” (Kaplan 2003, p. 48). Also recently, Data Guardian (a large MSSP) asked a panel of data security professionals to provide recommendations for vendor selection and contract management (Lord 2015). Hence, an important issue for both industry and academia is, How should MSSP contracts be written so that the social benefits of outsourcing can be maximized (Ding and Yurcik 2005, Cezar et al. 2014)? Given that the issues surrounding security contracting are a subject of ongoing debate, we leverage our analysis of the mechanics of security monitoring to study the design of socially optimal outsourcing contracts. Here, we study and compare two broad contracting structures: (1) based on rewards (for detection), and (2) based on penalties (for missing detection).

The rest of this paper is organized as follows. In Section 2, we provide a review of the related literature. In Section 3, we use a differential equation model to describe the dynamics of the session-based monitoring process. Section 4 optimizes the number of sessions being monitored by trading off the damage cost saved with the cost of monitoring. In Section 5, we introduce a profiling step prior to monitoring that creates interesting and nonobvious operational trade-offs. Section 6 uses our insights into the mechanics of profiling and monitoring to understand how these activities may be outsourced. Section 7 provides a detailed numerical study and Section 8 concludes the paper.

## 2. Literature Review

Monitoring systems examine events (in network traffic, operating systems, etc.) and match them to known patterns that are emblematic of malicious traffic (Himberger et al. 2006). An alarm is raised if the events are believed to be symptoms of an intrusion, and creates a log for human study (Kubota 2005, Scarfone and Mell 2007). Typically, humans (e.g., security administrators) are actively involved in the process of monitoring. The outputs from the monitoring process (the alarms and the logs) are usually processed by a system administrator who analyzes them to filter out false alarms, prevents possible damage, and attempts to verify if compromise has occurred, e.g., by investigating the affected system directly (Axelsson 2000, Werlinger et al. 2010, Sommestad and Hunstad 2013). For recent surveys of modern monitoring techniques, please see works by Peng et al. (2007) and Mitchell and Chen (2014).

The expertise of a system administrator has been shown to be an important factor in effective monitoring (Goodall et al. 2004; Werlinger et al. 2008, 2009). For example, Goodall et al. (2009) show that monitoring requires expertise in computer networks and security as well as a high degree of situated expertise and problem solving ability. According to Schneier (2007, p. 4), “software can only provide generic information; real understanding requires experts0 0 0 To make network monitoring work, people are needed every step of the way. Software doesn’t think, doesn’t question, doesn’t adapt. Without people, computer security software is just a static defense.”

Security experts are costly (Fitzparick 2008). As a result, the administrative cost is usually a major component of the total monitoring cost of IDS (Fitzparick 2008, Brown 2012), and it increases with the number of sessions being monitored (Cavusoglu et al. 2004b). Since a limited number of security experts can be used, only a limited number of sessions can be monitored (Fitzparick 2008). Our study examines the economic trade-offs to find the optimal number of sessions that should be monitored.

We next discuss the related literature in the following streams: (i) design and configuration of monitoring technologies; (ii) outsourcing of information security; and (iii) related security issues in other domains. Here, we also highlight our contributions by comparing and contrasting our study with past literature.

## 2.1. Design and Configuration of Monitoring Technologies

The design of monitoring systems mainly focuses on the development and improvement of algorithms using two broad approaches: signature based and anomaly based. For the details of signature-based algorithms, readers can refer to Kumar and Spafford (1996) and Monrose and Rubin (1997). The anomaly based algorithms are discussed in Neumann and Porras (1999) and Zamboni and Spafford (1999). Our paper focuses on configuration issues faced by firms that deploy monitoring technologies. However, the specifics of the algorithms used in detection techniques are outside the scope of our problem.

The research on monitoring configuration is more recent. Cavusoglu et al. (2005) represent the monitoring configuration by detection (true positive) and false alarm (false positive) rates, and show that an improperly configured monitoring system may encourage more hacking, resulting in a higher loss for the firm. Hence, to determine the optimal configuration, Ulvila and Gaffney (2004) propose a decision analytic approach, and Cavusoglu et al. (2008) compare decision analytic and game-theoretic approaches. Ogut et al. (2008) examine various waiting time policies to deal with the problem of false alarms in monitoring systems, and Cavusoglu et al. (2009) analyze configuration issues when multiple technologies are deployed as part of a layered security architecture. Finally, Baayer et al. (2014) propose a new optimization cost model for monitoring systems that trades off damage costs with false positive costs. Although these studies are related to the configuration issue considered in this paper, none of these studies consider the issue of optimizing the number of sessions being monitored, which is the focus of our study.

## 2.2. Outsourcing of Information Security

For monitoring, organizations today have two options: insource it or outsource it to an MSSP. A few years ago, most organizations were limited to the insource option, because the MSSPs were not sophisticated enough, firms were not ready to trust third parties with their sensitive data, and network security problems were not as complex (Brown 2012). However, today MSSPs are part of a multibillion-dollar industry, and they manage security for some of the world’s most sophisticated organizations. For any organization, the two key reasons for outsourcing the monitoring activities are the high cost of insource monitoring and the lack of technology (Fitzparick 2008, Brown 2012).

Since our paper also considers outsourcing, we would like to contrast our work with the outsourcing literature. Outsourcing has a vast literature in IT (e.g., Lacity et al. 2009) and in other contexts, such as manufacturing. Rather than attempting to identify the link between our paper and the voluminous outsourcing literature, we confine our discussion to the part of the literature that deals with analytical models in IT and information security outsourcing. In one of the earliest papers on IT outsourcing, Whang (1992) analyzes a multiperiod software development contract between a firm and an outside developer, and derives an optimal contract that replicates the equilibrium outcome of a benchmark in-house development. In the information security context, Ding and Yurcik (2005, 2006) examine the characteristics of optimal MSSP contracts under moral hazard, and find that an optimal contract should be performance based. Fitzparick (2008) and Brown (2012) discuss various factors that need to be considered while deciding between insourcing and outsourcing. Finally, Cezar et al. (2014) consider two different but related security services, and analyze the following question: Should IT security be outsourced to the same or two different MSSPs? Although these papers analyze the outsourcing problem, none of these study how to design a contract for outsourcing profiling and monitoring, which is one of the contributions of our research.

A few papers on information security analyze issues such as interdependent security risks among firms in managed security services and the formation and growth of MSSP networks (Gupta and Zhdanov 2012, Zhao and Whinston 2013). Their focus is on how to attain critical mass for network profitably. Hence, they consider scale economies of security infrastructure investment and network externalities associated with being served by the same MSSP. Clearly, our focus is different from these studies as well.

## 2.3. Network Cache Management

In terms of maintaining a list of objects, our model is closely related to cache management literature. Datta et al. (2003) provide a review of the various caching strategies to reduce the delay in serving document requests while a survey by Podlipnig and Bszrmenyi (2003) focuses specifically on the Web cache replacement strategies; one of the replacement strategies, the LRU (least recently used) strategy is studied analytically by Mookerjee and Tan (2002). Kelly and Reeves (2001) study the problem of optimizing the storage capacity for Web caches in a hierarchical caching model. The work by Fang et al. (2006) introduces an Internet-based network storage system and proposes a data-mining-based caching approach through prefetching to improve the system performance. By using game theory, Hosanagar and Tan (2011) perform a theoretic analysis of document duplication in a cooperative caching setting. Their focus is on studying the optimal duplication strategy by each player.

There are two important aspects that distinguish our study from the past caching literature. First, from a monitoring cost perspective, the operational cost of security monitoring depends on the current occupancy in the hot list. On the other hand, caching costs do not depend on actual occupancy, but on the total predetermined cache size. Second and more importantly, the notion of a hit is very different between caching and monitoring. In caching, a hit is a request for a document in the cache and reduces delay. In security, an event is similar to a hit. However, what classifies as an event depends on an MSSP’s definition of suspicious activity. If an MSSP is paid based on events detected, there will be an incentive to label anything as suspicious no matter how harmless it really might be.

There is some work in cache management that screens documents as cacheable and uncacheable (Kaya et al. 2009). The idea of screening documents is similar to profiling before monitoring. However, an important difference is that screening is usually based on factual attributes such as document size or document loading time. On the other hand, profiling is an imperfect process and is based on (relatively weak) symptoms of malicious or benign intent. Thus, screening can be considered to be a special case of profiling.

## 2.4. Related Security Issues in Other Domains

Several aspects of aviation security are similar to IT security. In the aviation security context, researchers investigate the usefulness of airport screening and baggage systems using optimization, simulation, and probability models (e.g., McLay et al. 2006). Virta et al. (2003) analyze the cost effectiveness of checking the baggage of only those passengers selected by the Computer Assisted Passenger Prescreening System (CAPPS). Using a numerical analysis, McLay et al. (2008) find that the accuracy of a prescreening system in assessing the passenger risk is more important than the effectiveness of the baggage screening system in detecting threats. Finally, Cavusoglu et al. (2010) show that, if the administration manually inspects all those passengers classified as likely attackers and sends others through a screening system, it is superior to no profiling if and only if the quality of the profiler visà-vis that of the screening system is sufficiently high. Although these studies are related to our research, none of these are applicable in our setting because they do not consider how to optimize the number of passengers being monitored.

Another domain that has recently gained a lot of attention in information security is healthcare security. In this domain, Garfinkel et al. (2007) consider security issues involved in releasing microdata, including individual identifiers. Furthermore, Bai et al. (2014) develop a two-stage decision-making methodology to optimize the healthcare workflow task assignments and mitigate information disclosure risks. Although these studies address important information security issues, they are not directly related to our work.

## 3. Probabilistic Analysis of Monitoring Policy

In this section, we derive a model of an age-based monitoring policy as follows. At any point in time, a hot list of n sessions is maintained. Whenever a new session (i.e., a new user) arrives, this session is assigned an age of zero and it is added to the top of the hot list. To accommodate the new arrival, the oldest session is removed. The ages of the sessions are $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ These ages are calculated as the time elapsed since a session last generated a suspicious event. Thus, when a session generates a suspicious event, its age is reset to zero. The joint probability density function (pdf) of the ages of n sessions is $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ , where $x _ { n }$ is the oldest age. Otherwise, $x _ { 1 } , x _ { 2 } , \dotsc , x _ { n - 1 }$ are not sorted.

Table 2 Summary of Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $x_{i}$ </td><td>Time elapsed since the last event from the  $i$ th session</td></tr><tr><td> $f(x_{1}, x_{2}, \ldots, x_{n})$ </td><td>Joint probability density function of the ages of  $n$  sessions</td></tr><tr><td> $P_{0}$ </td><td>Percentage of initial malicious traffic</td></tr><tr><td> $P_{d}$ </td><td>Probability of profiling a malicious session correctly as malicious</td></tr><tr><td> $P_{f}$ </td><td>Probability of profiling a benign session falsely as malicious</td></tr><tr><td> $q$ </td><td>Quality of profiling technology at the firm</td></tr><tr><td> $P$ </td><td>Percentage of malicious traffic coming to the system</td></tr><tr><td> $\lambda_{0}$ </td><td>Arrival rate of sessions to the profiling system</td></tr><tr><td> $\lambda$ </td><td>Arrival rate of sessions to the system after traffic profiling</td></tr><tr><td> $a$ </td><td>Excess event rate of a malicious session</td></tr><tr><td> $\theta(x)$ </td><td>Event intensity for a session with age  $x$ </td></tr><tr><td> $H$ </td><td>Expected number of events per unit time</td></tr><tr><td> $c_{a}$ </td><td>Benefit per event blocked</td></tr><tr><td> $c_{0}$ </td><td>Firm&#x27;s monitoring cost</td></tr><tr><td> $\alpha$ </td><td>Age sensitive parameter in the mean rate of event generation</td></tr><tr><td> $\beta$ </td><td>Inverse of the maximum mean rate of event generation</td></tr><tr><td> $r_{0}, r_{1}; \rho_{0}, \rho_{1}, \rho_{2}$ </td><td>Coefficients used in outsourcing contracts</td></tr></table>

We begin this section with the assumptions about the underlying pattern of events. We next specify a system of differential equations that describe the generation of suspicious events and the monitoring policy. The solution to these differential equations provides the functional form for joint probability density $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . Table 2 contains a summary of the key variables used in this paper.

## 3.1. Assumptions

Before deriving the joint probability density, we discuss the assumptions of our analytical model. In Section $^ { 7 , }$ we conduct a simulation study where we relax these assumptions.

• Poisson arrival. New sessions arrive at the system following a Poisson process. This is a standard assumption made for tractability. In addition, a Poisson process is also a good model of an arrival process where the causes of arrival are numerous and unobserved. In past studies (Jonsson and Olovsson 1997, Moitra and Konda 2000), the arrival of visitors to a website has been assumed to follow a Poisson process.

• Arrival rate is sufficiently high. We assume that the only way a session stops being monitored is when a new arrival replaces this session in the hot list. This implies that new arrivals occur fast enough and the sojourn of a session in the system is long enough so that it does not naturally end before being displaced by another (younger) session that is in need of monitoring. This assumption is quite reasonable. For example, a typical e-commerce site that monitors 100 sessions could have arrival rates in the order of 5 per second. Typical sessions, however, are likely to last several minutes (Bucklin and Sismeiro 2003), which is much longer than $\textstyle { \frac { 1 } { 5 } } \times 1 0 0 = 2 0$ seconds.

• Sessions are not terminated. When a session generates a suspicious event, it is prevented from doing any damage to the system. However, the session is not automatically “killed.” This assumption is reasonable for two reasons. First, the appearance of a suspicious event may be misleading, i.e., what appears to be an attack may be benign activity. Second, if the cost of wrongly terminating a session is sufficiently high, then it is better to thwart what appears to be an attack event rather than terminating the session. In practice, the rules pertaining to what needs to be done when a session generates a suspicious event are flexible and can be coded by security administrators. We are assuming that we are operating in an environment where the decision to refuse resources to a session has already been made at the firewall level. Beyond the firewall, sessions are permitted to operate, but monitored to prevent any potential damage.

• Event intensity depends on time since last event. In past studies, the arrival of suspicious events has been modeled as a Poisson process (Jonsson and Olovsson 1997, Moitra and Konda 2000). We build on this assumption, but allow for the possibility that the event generation could be in-homogeneous Poisson process (varying mean). We assume that the intensity of suspicious events originating from a session depends on the time that has elapsed since the last suspicious event was generated by the session. Thus, we model that the intensity of suspicious events (events per unit time) from a session with age x to follow a Poisson distribution with an instantaneous mean rate 4x5. Our model of the event generation process is based on the premise that the recency of events generated by a session is a predictor of its future behavior. This premise is consistent with practice: security products (e.g., BIG-IP Application Security Manager; F5 Networks 2015) often use a sliding window policy. In this policy, a session’s level of threat depends on the number of suspicious events generated by it within a certain time window. Events before the time window are forgiven. A variant of the sliding window policy is a K-event scheme. Here, the time for the last K events generated by a session is tracked. In this study, we set K = 1 for simplicity and because in most situations, suspicious events are not likely to be very frequent.

## 3.2. Differential Equations

Given the above model setting, the evolution in time of the ages of the sessions can be described by one differential equation and a second equation that describes a boundary condition. The equations below are solved to yield the probability density of the age of the n monitored sessions. Once an expression for the probability density is found, this expression is used to derive the expected rate of suspicious events generated from the sessions being monitored.

3.2.1. Differential Equation of System Dynamics. We first derive the differential equation that the pdf $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ satisfies when $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ are strictly positive. To do so, we determine a continuous-state transition function of a Markov chain (Zwillinger 2011) where $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ are the n states. Starting from $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) , x _ { i } > 0$ and after a very small amount of time $\delta ,$ this transition function is given by the product of the following two terms:

• the probability ç45 that there are no events in this small interval $\delta ,$

• the probability that no new sessions arrive in this interval, equal to 1 − .

To determine ç45, we use the property that the probability of two or more events from a Poisson process in a short time interval  can be ignored. The probability of one event from any session with age x within interval  is given by

$$
\int_ {x _ {i}} ^ {x _ {i} + \delta} \theta (x _ {i}) d x _ {i}.
$$

Therefore, ç45, the probability that no events take place in  time units, is given by

$$
\Pi (\delta) = 1 - \sum_ {i = 1} ^ {n} \int_ {x _ {i}} ^ {x _ {i} + \delta} \theta (x _ {i}) d x _ {i},\tag{1}
$$

by summarizing the probability of one event over n sessions. Then the pdf $f ( x _ { 1 } + \delta , x _ { 2 } + \delta , \dots , x _ { n } + \delta )$ after time  is given by the multiplication of the transition function $\Pi ( \delta ) ( \bar { 1 } - \lambda \delta )$ and the starting pdf $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$

$$
\begin{array}{l} f (x _ {1} + \delta , x _ {2} + \delta , \ldots , x _ {n} + \delta) \\ = \Pi (\delta) (1 - \lambda \delta) f (x _ {1}, x _ {2}, \ldots , x _ {n}). \end{array}\tag{2}
$$

Expanding both sides of (2) in terms of  up to the first order and taking necessary limits, we can obtain the following steady state equation that $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ satisfies:

$$
\sum_ {i = 1} ^ {n} \frac {\partial f (x _ {1} , \dots , x _ {n})}{\partial x _ {i}} = - \left(\lambda + \sum_ {i = 1} ^ {n} \theta (x _ {i})\right) f (x _ {1}, \dots , x _ {n}).\tag{3}
$$

3.2.2. Boundary Condition. In addition to the differential equation (3), the system dynamics also involve a boundary condition. Note that a session of age 0 is caused by the following two scenarios: (i) an event generated by the session resets the age of this session to zero, and (ii) a new session arrives and is assigned age zero (causing the oldest session to be removed from the monitored list). Without loss of generality, let $x _ { i } = 0$ . Then the pdf $f ( x _ { 1 } , \ldots , x _ { i } = 0 , \ldots , x _ { n } )$ that there is one session of 0 age and the others are of positive ages is given by the sum of the following probability densities:

$f _ { 1 } ( x _ { 1 } , \ldots , x _ { i } = 0 , \ldots , x _ { n } ) .$ , a component arising from an event generated by session $i ,$

$f _ { 2 } ( x _ { 1 } , \ldots , x _ { i } = 0 , \ldots , x _ { n } ) .$ , a component arising from the addition of a new session to the monitored list.

The pdf $f _ { 1 } ( x _ { 1 } , \ldots , x _ { i } = 0 , \ldots , x _ { n } )$ is the probability density of a system with all sessions of positive ages multiplied by the probability that any session in the system generates a suspicious event (note that it is not possible to have two or more events simultaneously because the event generation process is Poisson). When an event occurs, we need to consider two cases: (1) session i is the oldest session, or (2) session i is not the oldest session. Therefore, we have

$$
\begin{array}{l} f _ {1} (x _ {1}, \ldots , x _ {i} = 0, \ldots , x _ {n}) \\ \qquad = \int_ {0} ^ {x _ {n}} \theta (x _ {i}) f (x _ {1}, \ldots , x _ {i}, \ldots , x _ {n}) d x _ {i} \\ \qquad + \int_ {x _ {n}} ^ {\infty} \theta (x) f (x _ {1}, \ldots , x _ {i - 1}, x _ {i + 1}, \ldots , x _ {n}, x) d x. \end{array}\tag{4}
$$

The pdf $f _ { 2 } ( x _ { 1 } , \ldots , x _ { i } = 0 , \ldots , x _ { n } )$ can be calculated by the probability that one new session arrives, multiplied by the probability density of a system with all other sessions of positive ages. In this case, a session with an age older than $x _ { n }$ is removed from the monitored list. Then we have

$$
\begin{array}{l} f _ {2} (x _ {1}, \ldots , x _ {i} = 0, \ldots , x _ {n}) \\ \qquad = \lambda \int_ {x _ {n}} ^ {\infty} f (x _ {1}, \ldots , x _ {i - 1}, x _ {i + 1}, \ldots , x _ {n}, x)   d x. \end{array}\tag{5}
$$

Combining (4) and (5), we get the boundary condition for $f ( x _ { 1 } , \ldots , x _ { n } )$

$$
\begin{array}{l} f (x _ {1}, \ldots , x _ {i} = 0, \ldots , x _ {n}) \\ = \int_ {0} ^ {x _ {n}} \theta (x _ {i}) f (x _ {1}, \ldots , x _ {i}, \ldots , x _ {n})   d x _ {i} \\ \quad + \int_ {x _ {n}} ^ {\infty} (\lambda + \theta (x)) f (x _ {1}, \ldots , x _ {i - 1}, x _ {i + 1}, \ldots , x _ {n}, x)   d x. \end{array}\tag{6}
$$

3.2.3. Solution. An analytical solution for the function $f ( x _ { 1 } , \ldots , x _ { n } )$ given the differential equation (3) and its associated boundary condition (6)

is

is presented in the following proposition (proofs are available in the online appendix (available as supplemental material at https://doi.org/10.1287/ isre.2016.0677)):

Proposition 1. <sub>The</sub> <sub>joint</sub> <sub>pdf</sub> $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ given by

$$
f (x _ {1}, x _ {2}, \ldots , x _ {n}) = e ^ {- [ \lambda x _ {n} + \sum_ {i = 1} ^ {n} \phi (x _ {i}) ]} / \omega ,\tag{7}
$$

where $\begin{array} { r } { \phi ( x ) = \int _ { 0 } ^ { x } \theta ( y ) \ d y } \end{array}$ dy and  is the normalization constant ensuring that $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ integrates to unity over the appropriate limits

$$
\omega = \int_ {0} ^ {\infty} d x _ {n} e ^ {- (\lambda x _ {n} + \phi (x _ {n}))} \left[ \int_ {0} ^ {x _ {n}} d x e ^ {- \phi (x)} \right] ^ {n - 1}.\tag{8}
$$

3.3. Specification of the Mean Rate for Attacks We propose the following form for the mean rate of event generation from a session with age x:

$$
\theta (x) = \frac {1}{\alpha x + \beta}, \quad \alpha > 0, \beta > 0.\tag{9}
$$

In equation (9),  is the age-sensitivity parameter that captures the idea that a session with a younger age x tends to cause more events than a session with an older age x. In other words, if a session has behaved normally for a long time, it is less likely to generate suspicious events. We obtain

$$
\phi (x) = \int_ {0} ^ {x} \theta (y) d y = \frac {1}{\alpha} \ln \frac {\alpha x + \beta}{\beta},\tag{10}
$$

and

$$
\begin{array}{c} \int_ {0} ^ {x} d y e ^ {- \phi (y)} = \int_ {0} ^ {x} d y \bigg (\frac {\alpha y + \beta}{\beta} \bigg) ^ {- 1 / \alpha} \\ = \frac {\beta}{1 - \alpha} \bigg [ 1 - \bigg (\frac {\alpha x + \beta}{\beta} \bigg) ^ {1 - 1 / \alpha} \bigg ]. \end{array}\tag{11}
$$

Plugging (10) into (7), we get

$$
f (x _ {1}, x _ {2}, \dots , x _ {n}) = \frac {1}{\omega} e ^ {- \lambda x _ {n}} \prod_ {i = 1} ^ {n} \left(\frac {\alpha x _ {i} + \beta}{\beta}\right) ^ {- 1 / \alpha}.\tag{12}
$$

Plugging (11) into (8), we can write the normalization constant  as

$$
\begin{array}{c} \omega = \left(\frac {\beta}{1 - \alpha}\right) ^ {n - 1} \int_ {0} ^ {\infty} e ^ {- \lambda x _ {n}} \left(\frac {\alpha x _ {n} + \beta}{\beta}\right) ^ {- 1 / \alpha} \\ \cdot \left[ 1 - \left(\frac {\alpha x _ {n} + \beta}{\beta}\right) ^ {1 - 1 / \alpha} \right] ^ {n - 1} d x _ {n}. \end{array}\tag{13}
$$

## 3.4. The Objective Function

Our objective is to maximize the value of the damage that is prevented by blocking suspicious activities during monitoring. Of course, we must consider the monitoring cost. Out of the events H blocked by monitoring, some may have been caused by benign traffic and are therefore not likely to be harmful. As a result, suspicious events by benign traffic should be ignored. Therefore, we weigh the number of attacks H by the percentage of the malicious traffic P to obtain the expected damage avoided $c _ { a } P H$ , where $c _ { a }$ is the benefit to the firm from blocking a suspicious event. Taking into account the cost $c _ { 0 } n$ of monitoring n sessions, we wish to maximize the following net benefit of monitoring by optimally choosing n:

$$
J = c _ {a} P H - c _ {0} n.\tag{14}
$$

Before we discuss the optimal choice of n, we need to simplify the expression for H (a function of n). In its exact form, H (the expected number of suspicious events blocked per unit time) is complicated, given by

$$
H = \int_ {0} ^ {\infty} d x _ {n} \int_ {0} ^ {x _ {n}} d x _ {n - 1} \dots \int_ {0} ^ {x _ {n}} d x _ {1} f (x _ {1}, x _ {2}, \dots , x _ {n}) \sum_ {i = 1} ^ {n} \theta (x _ {i}).\tag{15}
$$

As a first step, we prove the following lemma:

Lemma 1.

$$
H = \frac {(1 - \alpha) \int_ {1} ^ {\infty} d y g _ {n - 1} (y) f (y)}{\beta \int_ {1} ^ {\infty} d y g _ {n} (y)},\tag{16}
$$

where

$$
y = \frac {\alpha x _ {n} + \beta}{\beta},\tag{17}
$$

$$
f (y) = (n - 1) \left(1 - y ^ {- 1 / \alpha}\right) + \frac {1}{1 - \alpha} \frac {1}{y} \left(1 - y ^ {1 - 1 / \alpha}\right),\tag{18}
$$

$$
g _ {n} (y) = e ^ {- (\beta \lambda / \alpha) y} y ^ {- 1 / \alpha} (1 - y ^ {1 - 1 / \alpha}) ^ {n - 1}.\tag{19}
$$

## 3.5. Peak Approximation

To simplify the expression for H in (16), we utilize a useful property of $g _ { n } ( y )$ and $g _ { n - 1 } ( y )$ . An examination of the expression for $g _ { n }$ in (19), shows that the term $e ^ { - ( \beta \lambda / \alpha ) y }$ decreases sharply with y when $\beta \lambda / \alpha$ is reasonably large. On the other hand, the term $( 1 - y ^ { 1 - 1 / \alpha } ) ^ { n - 1 } .$ is very small when y is close to 1 and n is not small. As a result, there is a sharp peak in the functions $g _ { n }$ and $g _ { n - 1 } f$ . To visually illustrate this behavior, we plot these functions using some benchmark parameter values that will be identified in Section 7 where we conduct a detailed numerical study. We can observe that both $g _ { n - 1 } f$ and $g _ { n }$ have very sharp peak values (see Figure 2). Therefore, we can use a peak approximation to simplify H since the contribution to the integral is mainly from the small region around the peak value.

Figure 2 Plots of the Integrands of the Numerator and Denominator in (16)  
![](/api/attachments/XBYF2GSJ/fulltext/images/1ec673eb230ebab1dfc17b097d423764564d041b7a77367f8c26926a71e90bfb.jpg)

(b) Plot of g<sub>n</sub>( y)  
![](/api/attachments/XBYF2GSJ/fulltext/images/e46c22b9107a140353d279d081bcc7ba04a7e8b1fbd51cc8f5c23cd2b9352e23.jpg)

Using this fact, we can evaluate the integrals in both the numerator and denominator in (16) by simply evaluating the integrands at their peak values. We can also see that the locations of the peak values (on the horizontal axis) are almost the same. If we denote this peak location of y on the horizontal axis as $\boldsymbol { Y } ,$ the ratio of the two integrals can be approximated as

$$
\frac {\int_ {1} ^ {\infty} d y g _ {n - 1} (y) f (y)}{\int_ {1} ^ {\infty} d y g _ {n} (y)} \approx \frac {g _ {n - 1} (Y) f (Y)}{g _ {n} (Y)}.
$$

We will see in the numerical study section (Section 7) that such a peak approximation is very accurate. Using the above peak approximation, we can approximate the expected number of events blocked per unit of time (H ) as the following:

Proposition 2.

$$
H = - \lambda + \left(\lambda + \frac {1}{\beta Y}\right) Y ^ {1 / \alpha},\tag{20}
$$

where Y is the peak of $g _ { n } ( y )$ and satisfies the first-order condition of $\dot { \cdot } \partial g _ { n } ( y ) / \partial \dot { y } | _ { y = Y } = 0$

$$
\left(\lambda + \frac {1}{\beta Y}\right) (Y ^ {1 / \alpha} - Y) = \frac {(n - 1) (1 - \alpha)}{\beta}, \quad Y > 1.\tag{21}
$$

To further simplify our analysis in the following sections, we make an assumption about the arrival rate of  to the system:

Assumption 1 (High-Traffic Assumption). <sub>We</sub> <sub>as-</sub> sume that the arrival rate is relatively high such that $\lambda \gg$ $1 / \beta .$ . Conceptually, this is a very reasonable assumption: the total arrival rate of sessions to the system is much greater than the maximum rate of suspicious events generated by one session.

Using the peak approximation and the high-traffic approximation, we can finally write

$$
\lambda (Y ^ {1 / \alpha} - Y) = \frac {(n - 1) (1 - \alpha)}{\beta}\tag{22}
$$

and

$$
H = \lambda (Y ^ {1 / \alpha} - 1).\tag{23}
$$

## 4. Optimal Monitoring Policy

To maximize the objective function $J , \mathsf { a }$ firm would choose the number of sessions n to monitor

$$
\max _ {n} J = \max _ {n} (c _ {a} P H - c _ {0} n).\tag{24}
$$

From Equation (24), we get a first-order condition in n that satisfies

$$
c _ {a} P \lambda \frac {1}{\alpha} Y ^ {1 / \alpha - 1} \frac {\partial Y}{\partial n} - c _ {0} = 0.\tag{25}
$$

We prove the following lemma necessary for finding the optimal $n ^ { * }$ :

<sup>Lemma</sup> <sup>2.</sup> When Assumption 1 holds, the objective function is concave in $n , i . e . , \partial ^ { 2 } \dot { J } / \partial n ^ { 2 } > 0$

Define

$$
A \equiv \left[ \frac {c _ {0} \alpha \beta}{c _ {0} \beta - c _ {a} P (1 - \alpha)} \right] ^ {1 / (1 - \alpha)}.
$$

In the following proposition, we show that the optimal n should satisfy the following:

<sup>Proposition</sup> <sup>3.</sup> When Assumption 1 holds, then $n ^ { * }$ and $Y ^ { * }$ are given by

$$
Y ^ {*} = A ^ {\alpha},\tag{26}
$$

$$
n ^ {*} = 1 + \frac {\beta \lambda}{1 - \alpha} (A - A ^ {\alpha}).\tag{27}
$$

Using Proposition $^ { 3 , }$ we can further study how the optimal value of the decision variable n is affected by various parameters. The first parameter we are interested in studying is the cost of monitoring per session $c _ { 0 } .$ . Also, the arrival rate to the system  and the percentage of malicious traffic P are exogenous parameters of interest. A comparative static analysis yields the following results:

<sup>Corollary</sup> <sup>1.</sup> The optimal monitoring size n decreases with the cost of monitoring $c _ { 0 }$ and increases with the percentage of malicious traffic and the arrival rate . That is $\partial n ^ { * } / \partial c _ { 0 } < 0 , \partial n ^ { * } / \partial P > 0 ,$ , and ¡n $\dot { } / \partial \lambda > 0$

From Corollary 1, we can see that as the monitoring cost per session $c _ { 0 }$ becomes more expensive, we should reduce the number of sessions to be monitored. When the percentage of malicious traffic P increases, the likelihood of an event being generated from a malicious session increases, leading to a rise of the marginal benefit of monitoring. Therefore the monitoring size n should increase. When the arrival rate of sessions  increases, there are more malicious incoming sessions per unit of time. As a result, more events generated by malicious sessions will be blocked per each monitored session, causing the marginal benefit of monitoring to increase. Thus n<sup>∗</sup> should increase.

The results in Corollary 1 are intuitive. In Section $5 ,$ we will introduce the notion of profiling, a method by which only a part of the incoming traffic will be filtered for monitoring. Profiling followed by monitoring generates some nonobvious trade-offs in security operations.

## 5. Joint Profiling and Monitoring

In this section, we introduce the notion of profiling, i.e., we consider that the incoming traffic to the system is first met by a profiler that filters a part of the traffic for monitoring. The remaining traffic is not monitored. A special case of profiling is when all of the traffic is monitored. Hence, we can always get back the situation where there is no profiling, implying that profiling should weakly improve the objective function value.

To distinguish from the notation used earlier, we now denote the session arrival rate as $\lambda _ { 0 }$ and the percentage of malicious traffic as $P _ { 0 } .$ . The profiler is governed by the characteristic equation, $\dot { \boldsymbol { P } } _ { d } = \boldsymbol { P } _ { f } ^ { q } .$ , where $0 < q < 1$ is the quality of the profiler. When $\overset { \cdot } { q } = 0 ,$ the profiler is of perfect quality. Under profiling, a portion $P _ { d }$ of the traffic is correctly identified as suspicious and marked for monitoring. In addition, a portion $P _ { f }$ is mistakenly sent for monitoring. Thus the percentage of malicious traffic in the portion sent for monitoring is given by

$$
P = \frac {P _ {d} P _ {0}}{P _ {d} P _ {0} + P _ {f} (1 - P _ {0})},\tag{28}
$$

and $\lambda ,$ the total traffic sent for monitoring, is given by

$$
\lambda = \lambda_ {0} (P _ {d} P _ {0} + P _ {f} (1 - P _ {0})).\tag{29}
$$

When a firm can optimize both system components (profiling and monitoring), the monitored traffic characteristics ( and P ) can be influenced. These characteristics are functions of $P _ { f }$ and $P _ { d }$ as can be seen from Equations (28) and (29). Given that $P _ { f }$ and $P _ { d }$ are functionally related $( P _ { d } = P _ { f } ^ { q } )$ , to influence the characteristics of the monitored traffic, we can choose either $P _ { f }$ or $P _ { d }$ as a decision variable. We choose the false positive rate $P _ { f }$ as a second decision variable, in addition to the monitoring size, n. The firm now faces the following optimization problem:

$$
\max _ {n, P _ {f}} J = \max _ {n, P _ {f}} (c _ {a} P H - c _ {0} n).\tag{30}
$$

After profiling, the event generation rate (9) needs to be modified to account for the fact that the concentration of malicious sessions in the monitored traffic has increased. We propose the following form to accommodate the impact of profiling:

$$
\theta (x) = \frac {1 + a (P - P _ {0})}{\alpha_ {0} x + \beta_ {0}}, \quad a > 0.\tag{31}
$$

The above form has several reasonable features as discussed below.

• When a profiler has no discrimination ability $( q = 1 )$ , then $\bar { P _ { d } _ { d } } = \bar { P _ { f } _ { f } }$ and $P = P _ { 0 }$ according to (28). Then there is no change in the percentage of malicious traffic after profiling. From (9) we have $\theta ( x ) = \theta _ { 0 } ( x ) \equiv$ $1 / ( \alpha _ { 0 } x + \bar { \beta } _ { 0 } )$ , which is the original attack rate before profiling.

• When there is no difference in event generation rates between benign and malicious sessions $( a = 0 )$ then we also have $\bar { { \boldsymbol { \theta } } } ( x ) = { \boldsymbol { \theta } } _ { 0 } ( x )$ , i.e., event generation rate does not change after profiling.

• Another important property in Equation (31) is that event generation is conserved, i.e., before and after profiling, the event generation rate is the same. With regard to the rate of malicious traffic, we must have $\lambda _ { 0 } \mathbf { \breve { P } } _ { 0 } = \lambda \mathbf { \bar { \it P } } + ( \lambda _ { 0 } - \lambda ) \tilde { \it P } .$ , where

$$
\tilde {P} = \frac {(1 - P _ {d}) P _ {0}}{(1 - P _ {d}) P _ {0} + (1 - P _ {f}) (1 - P _ {0})}
$$

is the percentage of malicious traffic in the nonmonitored traffic after profiling with arrival rate $( \lambda _ { 0 } - \lambda )$ . The event generation rates in the monitored and unmonitored traffic are given by

$$
\begin{array}{l} \theta_ {1} (x) = \frac {1 + a (P - P _ {0})}{\alpha_ {0} (x) + \beta_ {0}}, \\ \theta_ {2} (x) = \frac {1 + a (\tilde {P} - P _ {0})}{\alpha_ {0} (x) + \beta_ {0}}. \end{array}
$$

It is easy to see that $\lambda _ { 0 } \theta _ { 0 } ( x ) = \lambda \theta _ { 1 } ( x ) + ( \lambda _ { 0 } - \lambda ) \theta _ { 2 } ( x )$

For ease of exposition, we redefine

$$
\alpha = \frac {\alpha_ {0}}{1 + a (P - P _ {0})} \quad \text { and } \quad \beta = \frac {\beta_ {0}}{1 + a (P - P _ {0})}.
$$

Then we have

$$
\theta (x) = \frac {1}{\alpha x + \beta}.\tag{32}
$$

The parameter a captures the idea that malicious sessions tend to generate more suspicious events than do benign sessions. While benign sessions could inadvertently generate events that can look suspicious, such events can be expected to be less frequent. Therefore, the higher the percentage of malicious traffic $P ,$ the higher the mean event generation rate $\theta ( x )$

## 5.1. Optimization

To find $n ^ { * }$ , from the objective function (30), we obtain the same first-order condition $\partial J / \partial n = 0$ as the one in (25) and the same approximation leads to the one in (26). Furthermore, the first-order condition with respect to $P _ { f }$ under Assumption 1 is given by

$$
\begin{array}{l} q P _ {f} ^ {q - 1} (Y ^ {1 / \alpha} - 1) + P _ {d} \frac {1}{1 - \alpha Y ^ {(\alpha - 1) / \alpha}} \\ \cdot \bigg [ (n - 1) \frac {\partial}{\partial P _ {f}} \frac {1 - \alpha}{\beta \lambda} + Y \mathrm{ln} [ Y ^ {1 / \alpha} ] \frac {\partial \alpha}{\partial P _ {f}} \bigg ] = 0. \end{array}\tag{33}
$$

The solutions for optimal $n ^ { * }$ and $P _ { f } ^ { * }$ can be obtained by simultaneously solving Equations (26), (27), and (33). While obtaining closed-form solutions for $n ^ { * }$ and $P _ { f } ^ { * }$ is difficult, we can still gain useful insights about the behavior of $n ^ { * }$ and $P _ { f } ^ { * }$ through a comparative statics study.

5.2. Comparative Statics with Regard to $\lambda _ { 0 }$ and $c _ { 0 }$ We first study the impact of traffic arrival rate $\lambda _ { 0 }$ on $n ^ { * }$ and $P _ { f } ^ { * } .$ , and the result is the following:

<sup>Lemma</sup> <sup>3.</sup> When the arrival rate $\lambda _ { 0 }$ increases, the optimal monitoring size n<sup>∗</sup> increases while the optimal false positive rate $P _ { f } ^ { * }$ stays the same. That is, $( n ^ { * } - 1 ) / \lambda _ { 0 } = c o n s t a n t$ and $\partial P _ { f } ^ { * } / \partial \acute { \lambda } _ { 0 } = \acute { 0 }$

Similar to Corollary 1, Lemma 3 shows that the monitoring size $n ^ { * }$ increases with the arrival rate $\lambda _ { 0 }$ One might expect the optimal false positive rate $P _ { f } ^ { * }$ to decrease since profiling can be made more selective with more candidate sessions to choose from. However, $P _ { f } ^ { * }$ stays the same in this case. We can explain this result as follows. The monitoring size $n ^ { * }$ is chosen such that the marginal benefit of increasing $n ^ { * }$ equals the marginal cost of doing so. When the arrival rate increases, one can increase $n ^ { * }$ (by keeping $( n ^ { * } - 1 ) / \lambda _ { 0 }$ as a constant) to make the marginal benefit and cost equal without changing $P _ { f } ^ { * }$ . Therefore, one can deal with the increase in traffic volume by only increasing the monitoring size (without adjusting the profiler’s configuration).

Next, we study the impact of increase in monitoring cost $c _ { 0 }$ on $n ^ { * }$ and $\bar { P } _ { f } ^ { * }$ . We state the following proposition:

Proposition 4. <sub>When</sub> $c _ { 0 }$ increases, $n ^ { * }$ decreases; however, $P _ { f } ^ { * }$ decreases or increases, depending on the critical value of monitoring cost ${ \bar { c } } _ { 0 } .$ Mathematically, ¡n<sup>∗</sup> $/ \partial c _ { 0 } < 0$ When parameter a in (31) is small, we have $\partial P _ { f } ^ { * } / \partial c _ { 0 } > 0 \ i j$ the monitoring cost $c _ { 0 } < \bar { c } _ { 0 }$ and $\partial P _ { f } ^ { * } / \partial c _ { 0 } < 0$ otherwise.

Proposition 4 shows that as it becomes more expensive to monitor sessions, we should reduce the optimal size of the monitoring list $n ^ { * }$ . This result is intuitive and expected. On the other hand, the impact of the monitoring cost $( c _ { 0 } )$ on the optimal false positive rate $( P _ { f } ^ { * } )$ is quite interesting and nonintuitive. As the monitoring cost increases, to accommodate the reduced monitoring size, the profiler could attempt to send more sessions for monitoring. This would be done in the hope that fresher sessions would be monitored and thereby more events would be detected. Therefore, as $c _ { 0 }$ increases, the optimal false positive rate $P _ { f } ^ { * }$ could increase from a freshness effect (see Equation (29)). Thus at first glance, it would appear that $n ^ { * }$ and $P _ { f } ^ { * }$ behave as substitutes when the monitoring cost increases. However, to complete the story, we need to consider the other (opposing) effect of increasing $P _ { f } ^ { * }$ . As seen above, an increase in $P _ { f } ^ { * }$ means that the profiler sends more sessions for monitoring. Consequently, the incoming traffic for monitoring would have a lower percentage of malicious sessions since P decreases with an increase in $P _ { f }$ (Equation (28)). This dilution effect can sometimes be significant.

The above discussion suggests that we need to balance these two effects of increasing the optimal false positive rate (namely, freshness and dilution). Proposition 4 shows that when the monitoring cost is small $\left( c _ { 0 } < \bar { c } _ { 0 } \right)$ and it increases, bringing fresher sessions is more important and $P _ { f } ^ { * }$ (and ) should be increased. More sessions are classified as in need of monitoring to compensate for the reduction in the optimal monitoring size; here, the optimal monitoring size and the false positive rate act as substitutes. As the monitoring cost increases and $c _ { 0 } \geq \bar { c } _ { 0 } ,$ the optimal monitoring size is forced downward. Here, the adverse impact of dilution is more than the benefit from freshness and hence, the profiler tries to concentrate the traffic to bring a higher percentage of malicious traffic. Hence, the optimal false positive rate is decreased. Here, $n ^ { * }$ and $P _ { f } ^ { * }$ (and ) become complements.

To summarize, the result in Proposition 4 contrasts sharply with the result in Corollary 1. Under joint optimization of monitoring and profiling, the optimal monitoring size and the optimal percentage of malicious events $( n , P _ { f } )$ are substitutes in some cases and complements in other cases. On the other hand, the result in Corollary 1 is that the number of sessions monitored and the percentage of malicious events are always complements. If the result in Corollary 1 is applied, with an increase in monitoring cost (and hence a reduction in monitoring size), security managers would tend to send more traffic for monitoring. However, sometimes, the exact opposite should be done, i.e., send less traffic for monitoring. Corollary 1 therefore provides a good motivation for the need to jointly optimize profiling and monitoring. Although it is difficult to obtain closed-form expressions of the optimal solution, we are still able to gain some useful insights from Proposition 4. For example, if the monitoring cost changes, without needing to run a complicated model, Proposition 4 allows a manager to change monitoring and profiling decisions in the right direction.

## 5.3. Region-Based Profiling: An Illustrative Example

We provide an illustrative example to better understand Proposition 4. Suppose the traffic to a firm comes from three different geographic regions with distinct characteristics. For this illustrative example, let us imagine that we are only allowed to profile by region. That is, either all of the traffic from a region is monitored or none of it is monitored. We need to determine which region(s) to monitor to maximize the objective function. Assume that the incoming traffic has the following characteristics: $\lambda _ { 1 } = 1 0 , P _ { 1 } \stackrel {  } { = } 0 . 1 2 , \lambda _ { 2 } = 1 5 , P _ { 2 } =$ 0008, $\bar { \lambda _ { 3 } } = 1 4$ , and $P _ { 3 } = 0 . 0 4$ . The rest of the parameter values are $\alpha _ { 0 } = 0 . 9 5 , \beta _ { 0 } = 3 . 5 , a = 0 . 5$ , and $c _ { a } = 1 5 0$

In Table 3, we see that the initial strategy is to only monitor traffic from Region 1. However, as the monitoring cost changes from 1050 to 1075, we monitor more regions; all three regions are monitored. This is the region where the optimal false positive rate and the optimal monitoring size are substitutes (implicitly, as more regions are monitored, the false positive rate would increase). When the cost of monitoring is very high, we again monitor traffic from Region 1 only. Conceptually, when the monitoring cost is changed from 2000 to 2025, the optimal false positive rate and the optimal monitoring size act as complements. Finally, if the monitoring cost is too high, then it is not worth monitoring any traffic. We can also observe that the optimal monitoring size and the optimal objective function value steadily decrease with the monitoring cost.

In the last two columns of Table 3 we display what happens when there is no profiling, i.e., either all of the traffic is monitored or no traffic is monitored. As can be seen, when profiling is not an option, the extent of monitoring (monitoring size) is suboptimal. When $c _ { 0 } = 1 . 5 $ , the monitoring size is less than optimal. Conversely, when $c _ { 0 } = 2 . 2 5 ,$ , excessive monitoring occurs, whereas when $c _ { 0 } = 3 . 7 5$ monitoring is prematurely abandoned.

6. Outsourcing Monitoring Operations Two key reasons for outsourcing monitoring activities are the high cost of insource monitoring, and the lack of technology (Fitzparick 2008, Brown 2012). An MSSP (also referred to as “security vendor”) can usually obtain superior security technology or valuable security expertise much cheaper (owing to scale economies) and keep up-to-date on vulnerabilities and security products (Schneier 2002, Cezar et al. 2014). Therefore, similar to past studies (e.g., Cezar et al. 2014), we consider that the MSSP has two advantages. First, the monitoring cost of the MSSP $( c _ { 1 } )$ is lower, i.e., $c _ { 1 } < c _ { 0 }$ Second, the MSSP has superior profiling technology, i.e., $q _ { 1 } < q$

If the firm and the security vendor are assumed to be risk neutral, the socially optimal solution $( n _ { c } ^ { * } , P _ { f c } ^ { * } )$ is obtained by solving the following problem:

$$
\max _ {n _ {c}, P _ {f c}} (c _ {a} P H - c _ {1} n _ {c}).\tag{34}
$$

The specific details of the above problem are the same as those in (26), (27), and (33) with $c _ { 0 }$ and $q$ being replaced by $c _ { 1 }$ and $q _ { 1 }$ .

## 6.1. Reward-Based Contract

We first consider the following outsourcing setting using a reward-based contract, similar to the previous literature (Hui et al. 2012, Cezar et al. 2014):

• A firm designs an outsourcing contract, where the payment to the security vendor is based on the number of detected attacks $\tilde { N } \colon \dot { r } _ { 0 } + r _ { 1 } \tilde { N }$

• The security vendor accepts the contract and chooses its optimal $P _ { f s } ^ { * }$ and $n _ { s } ^ { * }$ .

• The number of detected attacks N is realized and the payment is made out.

Since $E [ { \tilde { N } } ] = H$ , we can write the firm’s outsourcing problem in Program N

[Program N]

$$
\begin{array}{c} \underset {r _ {0}, r _ {1}} {\max} J = \underset {r _ {0}, r _ {1}} {\max} [ c _ {a} P (P _ {f s} ^ {*}) H (P _ {f s} ^ {*}, n _ {s} ^ {*}) \\ - (r _ {0} + r _ {1} H (P _ {f s} ^ {*}, n _ {s} ^ {*})) ] \end{array}\tag{35}
$$

subject to

$$
I C \text { constraint: } \pi^ {*} = \max _ {P _ {f s}, n _ {s}} [ (r _ {0} + r _ {1} H) - c _ {1} n _ {s} ],\tag{36}
$$

I R constraint2 $\pi ^ { * } \geq \pi _ { 0 } ,$

(37)

where $\pi _ { 0 }$ is the minimum profit the security vendor can obtain using its resources elsewhere (outside option).

Define

$$
A _ {1} \equiv \left[ \frac {c _ {1} \alpha \beta}{c _ {1} \beta - r _ {1} (1 - \alpha)} \right] ^ {1 / (1 - \alpha)}.
$$

Table 3 Impact of Monitoring Cost on Monitoring Strategies

<table><tr><td rowspan="2"> $c_0$ </td><td colspan="3">Profiling</td><td colspan="2">No profiling</td></tr><tr><td> $n_P^*$ </td><td> $J_P^*$ </td><td>Regions monitored</td><td> $n_{NP}^*$ </td><td> $J_{NP}^*$ </td></tr><tr><td>1.25</td><td> $5.26 \times 10^{3}$ </td><td> $1.35 \times 10^{3}$ </td><td>1</td><td> $3.5 \times 10^{3}$ </td><td> $1.16 \times 10^{3}$ </td></tr><tr><td>1.50</td><td> $1.64 \times 10^{3}$ </td><td> $5.95 \times 10^{2}$ </td><td>1</td><td> $1.43 \times 10^{3}$ </td><td> $5.93 \times 10^{2}$ </td></tr><tr><td>1.75</td><td> $7.16 \times 10^{2}$ </td><td> $3.39 \times 10^{2}$ </td><td>1, 2, 3</td><td> $7.16 \times 10^{2}$ </td><td> $3.39 \times 10^{2}$ </td></tr><tr><td>2.00</td><td> $4.05 \times 10^{2}$ </td><td> $2.03 \times 10^{2}$ </td><td>1, 2, 3</td><td> $4.05 \times 10^{2}$ </td><td> $2.03 \times 10^{2}$ </td></tr><tr><td>2.25</td><td> $2.13 \times 10^{2}$ </td><td> $1.26 \times 10^{2}$ </td><td>1</td><td> $2.47 \times 10^{2}$ </td><td> $1.24 \times 10^{2}$ </td></tr><tr><td>3.75</td><td>22.9</td><td>8.54</td><td>1</td><td colspan="2">No monitoring</td></tr><tr><td>4.50</td><td></td><td>No monitoring</td><td></td><td colspan="2">No monitoring</td></tr></table>

By backward induction, in the second stage, we can get a security vendor’s optimal decision on n<sup>∗</sup> and $P _ { f s } ^ { * }$ in a way similar to how we obtain $n ^ { * }$ and $P _ { f } ^ { * }$ in (26) and (33)

$$
n _ {s} ^ {*} = 1 + \frac {\beta \lambda}{1 - \alpha} (A _ {1} - A _ {1} ^ {\alpha}),\tag{38}
$$

$$
[ P _ {0} q _ {1} P _ {f s} ^ {q _ {1} - 1} + (1 - P _ {0}) ] (A _ {1} - 1) + \frac {\lambda}{\lambda_ {0}} \frac {1}{1 - \alpha A _ {1} ^ {\alpha - 1}}
$$

$$
\cdot \left[ (n - 1) \frac {\partial}{\partial P _ {f s}} \frac {1 - \alpha}{\beta \lambda} + A _ {1} ^ {\alpha} \mathrm{ln} [ A _ {1} ] \frac {\partial \alpha}{\partial P _ {f s}} \right] = 0.\tag{39}
$$

In the first stage, the firm determines $r _ { 0 }$ and $r _ { 1 } .$ First parameter $r _ { 0 }$ is obtained by setting the IR constraint to be binding

$$
r _ {0} = \pi_ {0} + c _ {1} n _ {s} ^ {*} - r _ {1} H.\tag{40}
$$

Then plugging Equation (40) into (35), we can obtain $r _ { 1 }$ by maximizing J . A socially optimal solution $( n _ { c } ^ { * } , P _ { f c } ^ { * } )$ yields the highest benefit for the firm and the security vendor as a whole. Since the fixed component of $r _ { 0 }$ makes the security vendor earn its reservation profit $( \pi _ { 0 } )$ by setting its IR constraint to bind, then the firm attempts to obtain the socially optimal solution and maximize its benefit through the outsourcing contract. However, the following proposition shows that a contract based on the number of events detected cannot achieve social optimality.

<sup>Proposition</sup> <sup>5.</sup> An outsourcing firm cannot achieve the social optimal solution $( n _ { c } ^ { * } , P _ { f c } ^ { * } )$ in [Program N].

Proof by Contradiction. <sub>For</sub> <sub>a</sub> <sub>given</sub> <sub>contract</sub> $r _ { 0 } +$ $r _ { 1 } \tilde { N } ,$ , the first-order condition with respect to $P _ { f s }$ is derived from a security firm’s IC constraint

$$
r _ {1} \frac {\partial H}{\partial P _ {f s}} = 0.\tag{41}
$$

Suppose a socially optimal solution $( n _ { c } ^ { * } , P _ { f c } ^ { * } )$ is achieved under this contract. Then $n _ { f s } = n _ { c } ^ { * }$ and $P _ { f s } = P _ { f c } ^ { * }$ . In addition, $P _ { f c } ^ { * }$ satisfies the following first-order condition from (34):

$$
c _ {a} \left(\frac {\partial P}{\partial P _ {f c}} H + P \frac {\partial H}{\partial P _ {f c}}\right) = 0.\tag{42}
$$

Given that $\partial P / \partial P _ { f c } < 0 .$ , both (41) and (42) cannot be satisfied simultaneously. Therefore, a social optimally solution is not achievable under [Program N]. <sup></sup>

Parameter $r _ { 0 }$ makes the security vendor’s IR constraint bind but does not affect the choice of n<sup>∗</sup> and $P _ { f s } ^ { * } .$ Therefore by adjusting $r _ { 1 }$ alone, an outsourcing firm cannot obtain the socially optimal solution. Figure 3 depicts an analogy to better understand the incentive problem in the above contract. Think of a population of fish: a red (green) fish represents a malicious (benign) session. The profiler imperfectly distinguishes between red and green fish and sends the reddish ones for monitoring. Through profiling, red fish become more concentrated in the traffic being monitored. A client firm only values red fish while the security vendor would be color blind in the current reward-based contract. Thus the vendor lets more green fish through the profiler to catch more fish with less effort. Mathematically, the firm cares not only about the expected number of detected events H but also the concentration of these events (captured by weighting H by P in the objective). However, a contract of the form $( r _ { 0 } + r _ { 1 } H )$ only rewards the expected number of events H. Thus the vendor has an incentive to ignore P and only maximize H by choosing $n _ { s } ^ { * }$ and $P _ { f s } ^ { * }$ in a suboptimal way. How would a client firm design a contract that can incentivize a security vendor to catch more red fish? We next study such a reward-based contract.

6.2. Additional Reporting by the Security Vendor To correct this vendor’s incentive problem, the firm needs to use an additional observable outcome (i.e., in addition to the number of suspicious events detected) from the security vendor’s report to the firm. We can expect that the security vendor would, at the very least, report a log of the suspicious events detected during the period of the contract (say a month). Without such a report, there would be no way to tell whether the vendor is doing any monitoring! However, simply reporting the details of suspicious events detected is not sufficient. This is because the percentage of malicious traffic P cannot be deduced from such a report, since an event generated with malicious intent cannot be easily distinguished from one generated with benign intent.

Figure 3 (Color online) Profiling Increases the Concentration of Malicious Traffic  
![](/api/attachments/XBYF2GSJ/fulltext/images/cf3856525a3dc7e2651aeb4d9ef312c05583ae16490ed9c874fed458fd0d302e.jpg)  
For this, the vendor should be required to report suspicious activity by session. That is, the report should have the format (session-ID, list of events detected, etc.). For sessions with no suspicious activity, the list of events detected would be blank. From such a report, it is possible for the firm to deduce the concentration of the traffic being monitored by the vendor. The number of sessions monitored (say, M<sup>˜</sup> ) and the total number of suspicious events (N<sup>˜</sup> ) in these sessions can be used to estimate the concentration of the traffic being monitored by the vendor. For the same number of events detected, a lower number of sessions monitored indicates a higher percentage of malicious traffic P . Therefore, we propose to include M<sup>˜</sup> as part of the contract. In the new contract, the vendor would be paid based on

$$
\rho_ {0} + \rho_ {1} \tilde {N} + \rho_ {2} \tilde {M}.
$$

The sequence of the outsourcing arrangement is the same as before. Given that $E [ \tilde { N } ] = H$ and $\ { \tilde { E } } [ { \tilde { M } } ] = \lambda$ , we can write this outsourcing problem in [Program NM]. [Program NM]

$$
\begin{array}{c} \max _ {\rho_ {0}, \rho_ {1}, \rho_ {2}} J = \max _ {\rho_ {0}, \rho_ {1}, \rho_ {2}} [ c _ {a} P (P _ {f s} ^ {*}) H (P _ {f s} ^ {*}, n _ {s} ^ {*}) \\ - (\rho_ {0} + \rho_ {1} H (P _ {f s} ^ {*}, n _ {s} ^ {*}) + \rho_ {2} \lambda (P _ {f s} ^ {*})) ] \end{array}\tag{43}
$$

subject to

$$
I C \text { constraint: } \pi^ {*} = \max _ {P _ {f s}, n _ {s}} [ (\rho_ {0} + \rho_ {1} H + \rho_ {2} \lambda) - c _ {1} n _ {s} ],\tag{44}
$$

I R constraint2 $\pi ^ { * } \geq \pi _ { 0 }$

(45)

Define

$$
A _ {2} \equiv \left[ \frac {c _ {1} \alpha \beta}{c _ {1} \beta - \rho_ {1} (1 - \alpha)} \right] ^ {1 / (1 - \alpha)}.
$$

A security vendor’s optimal decision on $n _ { s } ^ { * }$ and $P _ { f s } ^ { * }$ is obtained in the same way as before

$$
n _ {s} ^ {*} = 1 + \frac {\beta \lambda}{1 - \alpha} (A _ {2} - A _ {2} ^ {\alpha}),\tag{46}
$$

$$
\begin{array}{l} \left[ P _ {0} q _ {1} P _ {f} ^ {q _ {1} - 1} + \left(1 - P _ {0}\right) \right] \left[ \rho_ {1} \left(A _ {2} - 1\right) + \rho_ {2} \right] + \frac {\lambda}{\lambda_ {0}} \rho_ {1} \frac {1}{1 - \alpha A _ {2} ^ {\alpha - 1}} \\ \cdot \left[ (n - 1) \frac {\partial}{\partial P _ {f}} \frac {1 - \alpha}{\beta \lambda} + A _ {2} ^ {\alpha} \ln \left[ A _ {2} \right] \frac {\partial \alpha}{\partial P _ {f}} \right] = 0. \end{array} \tag {47}
$$

To achieve the socially optimal solution $( n _ { c } ^ { * } , ~ P _ { f c } ^ { * } ) _ { . }$ , we equate $A _ { 2 } = A$ and $\overset { \cdot } { ( 4 7 ) } = \left( 3 3 \right)$ with $c _ { 0 }$ and $\dot { q }$ being replaced by $c _ { 1 }$ and $q _ { 1 }$ . Then from these two equations, we can obtain the optimal values of parameters $\rho _ { 1 }$ and $\rho _ { 2 }$

$$
\rho_ {1} = c _ {a} P,\tag{48}
$$

$$
\rho_ {2} = \frac {c _ {a} (A _ {2} - 1) [ P _ {0} q _ {1} P _ {f c} ^ {q _ {1} - 1} (1 - P) - (1 - P _ {0}) P ]}{P _ {0} q _ {1} P _ {f c} ^ {q _ {1} - 1} + (1 - P _ {0})},\tag{49}
$$

and we can get

$$
\rho_ {0} = \pi_ {0} + c _ {1} n _ {s} ^ {*} - (\rho_ {1} H + \rho_ {2} \lambda),\tag{50}
$$

by setting a security vendor’s IR constraint to be binding. The settings for $\rho _ { 0 } , \rho _ { 1 } ,$ , and $\rho _ { 2 }$ ensure that the security vendor would earn its reservation profit $\pi _ { 0 }$ . Also, the firm would earn the maximum surplus provided by the socially optimal solution.

## 6.3. Penalty-Based Contract

We next study penalty-based contracts as an alternative to reward-based contracts for information security outsourcing. Conversations with IT managers and a study of documents available from MSSP firms (Verizon 2012, IBM 2015) confirm that penalty-based contracts are actually used.

A typical penalty-based contract (IBM 2015) is the following: a client pays the MSSP a fixed fee $r _ { 0 }$ each period and the MSSP pays a penalty $r _ { 1 }$ per missing event. Then the payment from a client to the MSSP can be written as $r _ { 0 } - r _ { 1 } \tilde { m } .$ , where m˜ is the number of malicious events experienced by a client. Then the expected utility of the MSSP is given by

$$
\pi = r _ {0} - r _ {1} (L - P H) - c _ {1} n,\tag{51}
$$

where L is the total expected number of malicious events per period. Similarly, we can calculate the optimal contract coefficients $r _ { 0 }$ and $r _ { 1 }$ using the approach in Section 6.1 to reach the social optimum: $r _ { 1 } = c _ { a } , r _ { 0 } =$ $\pi _ { 0 } + [ r _ { 1 } ( L - P H ) + c _ { 1 } n ] | _ { n _ { c } ^ { * } , P _ { \epsilon _ { c } } ^ { * } }$

The issue with such a contract is that we need to know L before a contract is signed. Without the knowledge of $L ,$ an MSSP will not accept the contract when provided a pair of $( r _ { 0 } , r _ { 1 } )$ since the IR constraint might not be satisfied; similarly, a client cannot provide a value of $r _ { 0 }$ without knowing L. To determine the value of $L ,$ we need to have a period of no monitoring to correctly observe L. It is hard to do since no monitoring causes great damage to the client. Therefore an MSSP will have an incentive to overstate the value of L. The solution is for a client to ask an MSSP to report both on the number of malicious events blocked and the number of malicious events missed; the expected value of the sum of two numbers gives L.

Table 4 Parameter Baseline Values

<table><tr><td>Parameter</td><td>Baseline value</td><td>Parameter</td><td>Baseline value</td></tr><tr><td> $P_0$ </td><td>25%</td><td>q</td><td>0.75</td></tr><tr><td> $λ_0$ </td><td>20/second</td><td>a</td><td>0.1</td></tr><tr><td> $c_a$ </td><td>$100</td><td> $c_0$ </td><td>$2</td></tr><tr><td> $α_0$ </td><td>0.95</td><td> $β_0$ </td><td>10</td></tr></table>

Even if accurate information on L is publicly known, one still needs to be careful about the implementation of penalty-based contracts in the real world since the penalty is being tied to the monthly fee in the form of penalty ratio $r _ { 1 } / r _ { 0 } , \mathrm { e . g . }$ , one day credit for one missed malicious event in (IBM 2015). To achieve a social optimal outcome, we should set such a ratio as close to the social optimal ratio as possible: $r _ { 1 } / r _ { 0 } = c _ { a } / [ \pi _ { 0 } +$ $[ r _ { 1 } ( L - P H ) \bar { + } c _ { 1 } n ] | _ { n _ { c } ^ { * } , { \cal P } _ { \bar { t } c } ^ { * } } ]$ . Therefore, our study provides a direction for setting the proper fraction from the perspective of a client firm.

We will study more about outsourcing settings in Section 7.

## 7. Numerical Analysis

To further gain managerial insights, we conduct an extensive set of numerical studies to explore the impact of various model parameters on the properties of optimal decision variables and other important performance measures. Before this, we numerically establish the accuracy of the approximation methods proposed earlier, namely, the Peak Approximation and the High-Traffic Approximation.

We first list reasonable, albeit hypothetical, baseline (or default) values for model parameters in Table 4. Unless noted specifically, we vary one parameter at a time while holding other parameters constant at the baseline values in numerical experiments. Some justifications for the choices of parameter values are provided below.

According to a recent report by the security firm Incapsula (Kerr 2013), more than 60% of Internet traffic is now generated by bots, and 50% of bot traffic from malicious bots such as scrapers, hacking tools, and spammers. Therefore we let the percentage of initial malicious traffic $P _ { 0 } = 2 5 \%$ . The quality $q$ of a profiler is chosen to be 0.75 with 1 being the worst. A typical U.S. retail website, such as Walmart and Target, faces 50 million unique monthly visitors (Statista 2015). This yields the initial arrival rate $\lambda _ { 0 } = 2 0 / \mathrm { s e c o n d }$ . The relative cost of breaching versus monitoring is set to be 50: $c _ { a } / c _ { 0 } = 5 0$ . Values of $\alpha _ { 0 }$ and $\beta _ { 0 }$ are chosen such that the attack rate in (9) decreases by half at the age of $x = 1 0$ seconds.

Furthermore, to examine whether theoretical results hold in more general settings and gain additional insights, we use discrete-event simulation (Law 2014) (pseudocode listed in the online appendix) coded in C# that makes the simulation very efficient and crossplatform portable. First, without relaxing any assumptions, the simulation is used to validate the theoretical results in Sections 7.1 and 7.2. The simulation matches the theoretical results with high accuracy. Then, in Section 7.4, we conduct simulation studies in a more generalized setting by relaxing certain assumptions.

## 7.1. Accuracy of Approximation

The first numerical study we carry out is to verify the accuracy of peak approximation used in Section 3.4 that was used to derive the expected number of events H in (20). The peak approximation has value in itself: it provides an efficient way to evaluate the objective function values for a given set of parameters and decision variables. From an outsourcing perspective, it would allow the firm to get a quick estimate of the payment to the security vendor for a particular level of monitoring. The peak approximation can also provide a good starting point for finding optimal solutions to (16) using numerical search. The peaks of integrands in (16) are steep, and vary a lot for different parameter values. Knowing the rough location of these peaks can greatly reduce the search effort and improve the robustness of finding optimal solutions. In addition to the peak approximation, we also proposed a hightraffic assumption to estimate H in (23). The value of the high-traffic approximation is that it provides a closed-form solution to the problem of finding the optimal monitoring size.

In Table $5 ,$ we examine the accuracy of the peak approximation (Peak) and that of the peak approximation plus the high-traffic approximation (Peak + HT ). The peak approximation is seen to be very accurate: $H _ { \mathrm { p e a k } }$ and $H _ { \mathrm { a c c u r a t e } }$ are very close. Even with the additional high-traffic approximation, $H _ { \mathrm { p e a k } + H T }$ still matches $H _ { \mathrm { a c c u r a t e } }$ well, except when n and $P _ { f }$ are small in the low-traffic region. The peak approximation works well for two reasons: the integrands of the numerator and the denominator of (16) have very sharp peaks and the locations of these two peaks are very close.

Also, in Table $5 ,$ we display the H values obtained via simulation as $H _ { \mathrm { s i m } }$ . The simulation matches the theoretical results with high accuracy; the percentage deviation between simulation and theoretical results $( H _ { \mathrm { a c c u r a t e } } )$ is less than 005% over a large range of parameter values. Next, we examine how well the peak plus high-traffic approximation works to find the optimal solution.

Table 6 compares the value of the objective function (J ) obtained using the peak and high-traffic approximation with the optimal value. To find $J _ { \mathrm { { a p p r o x } } } ,$ , we use the approximation to get $( n ^ { * } , P _ { f } ^ { * } )$ from Section $5 ,$ and plug them into (16) to get $H _ { \mathrm { a p p r o x } } ,$ and finally get J<sub>approx</sub> from (14). To get $J _ { \mathrm { { a c c u r a t e } } } ,$ we perform an exhaustive two-dimensional search in a sufficiently large enough space to find $n _ { \mathrm { a c c } } ^ { * }$ and $P _ { f , \mathrm { a c c } } ^ { * }$ that maximizes (14). Table 6 shows that the values of the decision pair $( n ^ { * }$ $P _ { f } ^ { * } )$ obtained using the approximation are very close to $n _ { \mathrm { a c c } } ^ { * }$ and $P _ { f , \mathrm { a c c } ^ { \prime } } ^ { * }$ so is the value of the objective function, although the error increases slightly as $c _ { 0 } ~ \mathrm { g r o w s }$

Table 5 Comparing H Values Obtained Through Approximations, Direct Integration, and Simulation

<table><tr><td colspan="4">Parameter values</td><td colspan="4">H values</td></tr><tr><td> $\lambda_0$ </td><td> $α_0$ </td><td>n</td><td> $P_f$ </td><td> $H_{peak}$ </td><td> $H_{peak+HT}$ </td><td> $H_{accurate}$ </td><td> $H_{sim}$ </td></tr><tr><td>20</td><td>0.95</td><td>300</td><td>0.9</td><td>21.28</td><td>21.33</td><td>21.27</td><td>21.31</td></tr><tr><td>20</td><td>0.95</td><td>300</td><td>0.05</td><td>12.55</td><td>12.63</td><td>12.54</td><td>12.55</td></tr><tr><td>20</td><td>0.95</td><td>10</td><td>0.9</td><td>0.98</td><td>0.98</td><td>0.97</td><td>0.97</td></tr><tr><td>20</td><td>0.95</td><td>10</td><td>0.05</td><td>0.82</td><td>0.85</td><td>0.80</td><td>0.80</td></tr><tr><td>20</td><td>0.1</td><td>300</td><td>0.9</td><td>28.82</td><td>28.96</td><td>28.82</td><td>28.88</td></tr><tr><td>20</td><td>0.1</td><td>300</td><td>0.05</td><td>27.95</td><td>29.56</td><td>27.95</td><td>28.00</td></tr><tr><td>20</td><td>0.1</td><td>10</td><td>0.9</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>20</td><td>0.1</td><td>10</td><td>0.05</td><td>0.99</td><td>1.06</td><td>0.99</td><td>0.99</td></tr><tr><td>2</td><td>0.95</td><td>300</td><td>0.9</td><td>13.17</td><td>13.26</td><td>13.16</td><td>13.20</td></tr><tr><td>2</td><td>0.95</td><td>10</td><td>0.9</td><td>0.84</td><td>0.87</td><td>0.83</td><td>0.83</td></tr><tr><td>2</td><td>0.95</td><td>10</td><td>0.05</td><td>0.53</td><td>0.60</td><td>0.52</td><td>0.52</td></tr><tr><td>2</td><td>0.1</td><td>300</td><td>0.9</td><td>27.60</td><td>28.73</td><td>27.59</td><td>27.66</td></tr><tr><td>2</td><td>0.1</td><td>10</td><td>0.9</td><td>0.98</td><td>1.03</td><td>0.98</td><td>0.98</td></tr><tr><td>2</td><td>0.1</td><td>10</td><td>0.05</td><td>0.95</td><td>1.49</td><td>0.94</td><td>0.94</td></tr></table>

Table 6 Comparing J Values Obtained Through Approximation and Exhaustive Search Methods

<table><tr><td rowspan="2"> $c_0$ </td><td colspan="3">Approximation</td><td colspan="3">Exhaustive search</td></tr><tr><td> $n^*$ </td><td> $P_f^*$ </td><td> $J_{\text{approx}}$ </td><td> $n_{\text{acc}}^*$ </td><td> $P_{f,\text{acc}}^*$ </td><td> $J_{\text{accurate}}$ </td></tr><tr><td>1.50</td><td>260.99</td><td>0.468</td><td>96.184</td><td>260.18</td><td>0.470</td><td>96.185</td></tr><tr><td>1.75</td><td>124.15</td><td>0.256</td><td>50.722</td><td>123.27</td><td>0.258</td><td>50.724</td></tr><tr><td>2.00</td><td>64.30</td><td>0.148</td><td>28.335</td><td>63.42</td><td>0.151</td><td>28.340</td></tr><tr><td>2.30</td><td>31.85</td><td>0.081</td><td>14.835</td><td>30.91</td><td>0.084</td><td>14.847</td></tr><tr><td>2.60</td><td>17.05</td><td>0.047</td><td>8.033</td><td>16.11</td><td>0.050</td><td>8.059</td></tr><tr><td>3.00</td><td>8.24</td><td>0.024</td><td>3.575</td><td>7.26</td><td>0.027</td><td>3.640</td></tr></table>

To summarize, our approximation method (Peak + HT ) is both accurate and stable in a large parameter space. Therefore we only report results using the approximation method in the rest of this numerical study. To further compare simulated and analytical results, we display simulation results (obtained via exhaustive search) as points on top of the curves obtained using the approximation method. As one can see in Figures 4 and ${ 5 , }$ simulation results match the theoretical results quite well.

## 7.2. Sensitivity Results

7.2.1. Impact of $P _ { 0 }$ and $\alpha _ { 0 } .$ We study the impact of the percentage of initial malicious traffic $P _ { 0 }$ and the age-sensitivity parameter $\alpha _ { 0 }$ on the optimal decisions $n ^ { * }$ and $P _ { f } ^ { * }$ . As $P _ { 0 }$ increases, the rate of events detected per monitored session grows, leading to a higher marginal benefit of n and therefore a higher $n ^ { * }$ , as shown in Figure 4(a). Also, as the original traffic becomes more concentrated, we can gain the benefit of more traffic through a higher false positive rate $P _ { f } ^ { * }$ without overdiluting it, as shown in Figure 4(b). With regard to the age-sensitivity parameter $\alpha _ { 0 } ,$ as $\alpha _ { 0 }$ increases, the overall attack rate would decrease according to (32); as a result, it is optimal to monitor less and $n ^ { * }$ decreases, as shown in Figure 4(a). However, as the event generation rate becomes more sensitive to age, younger sessions become more important and more traffic should be monitored, causing $P _ { f } ^ { * }$ (and ) to increase. To summarize, both $n ^ { * }$ and $P _ { f }$ increase when $P _ { 0 }$ increases but they move in opposite directions when $\alpha _ { 0 }$ changes.

7.2.2. Impact of Monitoring Cost $c _ { 0 }$ and Profiling Quality q. Extending Proposition $^ { 4 , }$ we study the joint impact of $c _ { 0 }$ and the profiling quality $q$ on the optimal decisions $n ^ { * }$ and $P _ { f } ^ { * }$

First, Figure 5(a) verifies the results in Proposition 4: as it becomes more expensive to monitor, the optimal monitoring size $n ^ { * }$ decreases. As shown in Figure $5 ( \mathsf { a } ) _ { \mathsf { \cdot } }$ , as the profiling quality $q$ increases, a firm should monitor more sessions. With better profiling quality $q$ (a smaller $q )$ , more concentrated traffic $( \mathrm { i . e . , }$ with a higher percentage of malicious sessions) can be chosen for monitoring. Therefore, the marginal benefit of n increases, causing $n ^ { * }$ to increase.

Figure 5(b) shows that as the monitoring cost increases, the false positive rate $P _ { f }$ could decrease monotonically, or increase and then decrease, depending on the value of $q .$ It also shows that better profiling quality leads to a lower false positive rate (and less traffic to monitor). This is different from the result in Figure 4(b) where we find that when $P _ { 0 }$ increases, the false positive rate is higher and more traffic is sent for monitoring. This result can be explained using the red and green fish analogy. It is more important for a firm to detect suspicious events that arise from malicious traffic (catch more red fish), rather than just detect more total events (or simply catch more fish). Hence, we have the factor P multiplying H in the objective function (14). Therefore, an improvement in profiling quality could lead to less traffic arriving for monitoring (the number of fish being targeted reduces, but more red fish are caught).

## 7.3. Outsourcing

The numerics in this section study the impact of the monitoring cost on the performance of [Program N] and [Program NM]. Under the baseline values given in Table 4, the value of objective function $J = 2 8 . 3 4 _ { \cdot }$ $n \approx 6 4 ,$ and $\lambda = 3 . 4 1$ . We set $q _ { 1 } = 0 . 7$ for the security vendor, and without losing generality, set the vendor’s reservation profit $\pi _ { 0 }$ to be zero.

Figure 4 Sensitivity with Regard to $P _ { 0 }$  
(a) Monitoring size (n<sup>\*</sup>) vs. $P _ { 0 }$  
![](/api/attachments/XBYF2GSJ/fulltext/images/8bc696fb8bd9471de2547629337cb881e1b24612e347166d455e1cfde55c5838.jpg)  
Figure 5 Sensitivity with Regard to $c _ { 0 }$  
(a) Monitoring size (n<sup>\*</sup>) vs. $c _ { 0 }$

(b) False positive rate (P<sub>f</sub>) vs. $P _ { 0 }$  
![](/api/attachments/XBYF2GSJ/fulltext/images/6653d2ce044965084798f0410f1609af6453ab0f299d188a314e831625c774d3.jpg)

![](/api/attachments/XBYF2GSJ/fulltext/images/596cdcc6bb0857ac6f8a41ce34bb6c078e7d359cd8ca6cb42cb0aa75351aa023.jpg)

(b) False positive rate $( P _ { f } )$ vs. $c _ { 0 }$  
![](/api/attachments/XBYF2GSJ/fulltext/images/040568f1e35f05b2239d5f128cf696c95f2d8f184b63261696c375bfc11d44c4.jpg)

We first show the results of [Program N] in Table 7. The lowest value $c _ { 1 }$ can go is 1.5. Below that, Y in (26) becomes negative and the peak approximation is not suitable. We can see from Table $7$ that even if a security vendor has a profiling advantage and a very low monitoring cost $( c _ { 1 } = 1 . 5$ which is much smaller than $c _ { 0 } = 2 . 0 )$ , the resulting surplus J is still much smaller than 28.34, the value a firm can obtain by insourcing monitoring and profiling operations. The reason is that [Program N] only rewards the number of events detected and ignores the nature of traffic that generates such events. Therefore, a security vendor has an incentive to deviate from the social optimal solution and choose to set a much smaller monitoring size (n ≈ 4) and monitor all of the traffic $( P _ { f } = 1 )$ . Therefore, under [Program N], the firm forgoes the potential benefit from outsourcing and chooses to insource, despite very favorable outsourcing conditions $( c _ { 1 } < c _ { 0 } = 2 . 0$ and $q _ { 1 } = 0 . 7 < q _ { 0 } = 0 . 7 5 )$ . This leads us to numerically study the virtues of [Program NM] below.

Table 7 Results of [Program N]

<table><tr><td> $c_{1}$ </td><td> $r_{0}$ </td><td> $r_{1}$ </td><td> $n^{*}$ </td><td> $P_{f}$ </td><td> $\lambda$ </td><td> $J$ </td></tr><tr><td>1.5</td><td>1.48</td><td>15.184</td><td>3.59</td><td>1</td><td>20</td><td>1.08</td></tr><tr><td>1.6</td><td>1.57</td><td>16.196</td><td>3.58</td><td>1</td><td>20</td><td>0.72</td></tr><tr><td>1.7</td><td>1.67</td><td>17.209</td><td>3.60</td><td>1</td><td>20</td><td>0.36</td></tr></table>

Table 8 shows the results of [Program NM]. We first note that $\rho _ { 1 }$ is positive since, everything else held constant, it is socially optimal to reward more events detected. The parameter $\rho _ { 2 }$ is negative since a socially optimal contract should discourage monitoring more traffic solely for the sake of detecting more events. When the vendor’s monitoring cost $( c _ { 1 } ^ { \phantom { + } } )$ increases, initially, the vendor is incentivized to detect fewer events by paying less per event $( \rho _ { 1 }$ increases). At the same time, the penalty for dilute traffic is lowered $( | \rho _ { 2 } |$ is reduced) so the vendor is incentivized to increase the false positive rate and monitor more traffic. As the vendor’s monitoring cost increases further, the incentive for detecting events increases, but the penalty for dilute traffic continues to decrease. The results from [Program NM] show that, unlike [Program N], a firm can benefit from outsourcing in many situations $( J > 2 8 . 3 4 )$ Interestingly, outsourcing can be beneficial even when the vendor has a higher monitoring cost $( c _ { 1 } = 2 . 1 ,$ $c _ { 0 } = 2 . 0 )$ but has better profiling technology $( q _ { 1 } = 0 . 7$ and $q _ { 0 } = 0 . 7 5 )$ .

Table 8 Results of [Program NM]

<table><tr><td> $c_1$ </td><td> $ρ_0$ </td><td> $ρ_1$ </td><td> $ρ_2$ </td><td> $n^*$ </td><td> $P_f$ </td><td> $λ$ </td><td> $J$ </td></tr><tr><td>1.55</td><td>-4.9</td><td>41.6</td><td>-51.5</td><td>268.0</td><td>0.080</td><td>2.04</td><td>110.09</td></tr><tr><td>1.6</td><td>-3.8</td><td>40.9</td><td>-42.4</td><td>229.4</td><td>0.087</td><td>2.21</td><td>97.70</td></tr><tr><td>1.7</td><td>-2.4</td><td>40.7</td><td>-33.3</td><td>173.0</td><td>0.089</td><td>2.26</td><td>77.76</td></tr><tr><td>1.8</td><td>-1.5</td><td>41.1</td><td>-28.2</td><td>133.6</td><td>0.085</td><td>2.17</td><td>62.54</td></tr><tr><td>1.9</td><td>-0.7</td><td>41.7</td><td>-24.8</td><td>104.8</td><td>0.078</td><td>2.02</td><td>50.69</td></tr><tr><td>2.0</td><td>-0.2</td><td>42.4</td><td>-22.3</td><td>88.3</td><td>0.071</td><td>1.85</td><td>41.33</td></tr><tr><td>2.1</td><td>0.3</td><td>43.2</td><td>-20.3</td><td>67.0</td><td>0.064</td><td>1.68</td><td>33.85</td></tr><tr><td>2.2</td><td>0.7</td><td>44.1</td><td>-18.7</td><td>54.4</td><td>0.057</td><td>1.52</td><td>27.81</td></tr></table>

7.4. Simulation Study in a Generalized Setting In this section, we study the robustness of our analytical results and generate additional insights via simulation.

7.4.1. Robustness Check of Analytical Results. We relax several assumptions to check the robustness of our analytical results. First, we generalize the session arrival process to be a Markov-modulated Poisson process (MMPP) (Fisher and Meier-Hellstern 1993), a model that is widely used in the area of network communications. In particular, we use a two-state MMPP process $( \mathrm { i . e . , }$ an MMPP(2) process), a popular model for bursty traffic (Heindl 2003). Here, the event arrival process has two states of arrival intensities $( \lambda _ { H }$ and $\lambda _ { L } )$ with H (L) representing the high (low) arrival rate of sessions. The corresponding switching intensities are $( \omega _ { H }$ and $\omega _ { L } )$ with $1 / \bar { \omega } _ { i }$ being the expected duration of state i before switching to a different state. The burstiness of Web traffic is captured through ratios $\lambda _ { H } / \lambda _ { L }$ and $\omega _ { H } / \omega _ { L }$ . In addition, we consider batch arrival that allows multiple sessions to arrive at the same time. In the simulation, the number of batch arrivals follows uniform distribution between $[ 1 , N _ { \mathrm { m a x } } ]$ with the average being $( 1 + N _ { \operatorname* { m a x } } ) / 2 ;$ we hold $\lambda _ { L } = 1 0$ and $\omega _ { I . } = 0 . 0 0 0 1$

In Table 9, we define

$$
\bar {H} \equiv \frac {(H _ {\mathrm{peak}} | _ {\lambda_ {H} (1 + N _ {\mathrm{max}}) / 2}) / \omega_ {H} + (H _ {\mathrm{peak}} | _ {\lambda_ {L} (1 + N _ {\mathrm{max}}) / 2}) / \omega_ {L}}{1 / \omega_ {H} + 1 / \omega_ {L}},
$$

$\mathrm { i . e . , } \bar { H }$ is weighted by the inverse of process switching intensities. In Table 9, $H _ { \mathrm { s i m } }$ is the detection rate obtained through simulation for different parameter values. We can see that the values of $H _ { \mathrm { s i m } }$ and H<sup>¯</sup> are close over a wide range of parameter values with a maximum percentage error of less than 3%. The instances with slightly larger deviations occur when the batch size is large relative to the maximum size of the monitored list $( \mathrm { e . g . }$ , when $n = 1 0 , P _ { f } = 0 . 0 5 ,$ , and $N _ { \mathrm { m a x } } { = } 6 )$ . Otherwise, $H _ { \mathrm { s i m } }$ and H<sup>¯</sup> are virtually the same. Thus, batch arrival is easily handled by the theoretical model: if the size of the monitored list is 100, we can easily allow batch sizes as large as 20.

Table 9 Comparing H Values Obtained Through Simulation and Approximation

<table><tr><td colspan="7">Parameter values</td></tr><tr><td> $\lambda_H$ </td><td> $\omega_H$ </td><td>n</td><td> $P_f$ </td><td> $N_{max}$ </td><td> $H_{sim}$ </td><td> $\bar{H}$ </td></tr><tr><td>100</td><td>0.001</td><td>10</td><td>0.05</td><td>1</td><td>0.74</td><td>0.74</td></tr><tr><td>100</td><td>0.001</td><td>10</td><td>0.9</td><td>1</td><td>0.95</td><td>0.95</td></tr><tr><td>100</td><td>0.001</td><td>10</td><td>0.05</td><td>6</td><td>0.856</td><td>0.878</td></tr><tr><td>100</td><td>0.001</td><td>10</td><td>0.9</td><td>6</td><td>0.982</td><td>0.986</td></tr><tr><td>100</td><td>0.001</td><td>30</td><td>0.05</td><td>6</td><td>2.279</td><td>2.294</td></tr><tr><td>100</td><td>0.001</td><td>300</td><td>0.05</td><td>1</td><td>11.24</td><td>11.52</td></tr><tr><td>100</td><td>0.001</td><td>300</td><td>0.9</td><td>1</td><td>19.92</td><td>19.32</td></tr><tr><td>100</td><td>0.001</td><td>300</td><td>0.05</td><td>6</td><td>14.86</td><td>14.86</td></tr><tr><td>100</td><td>0.001</td><td>300</td><td>0.9</td><td>6</td><td>23.81</td><td>23.87</td></tr><tr><td>1,000</td><td>0.01</td><td>10</td><td>0.05</td><td>1</td><td>0.72</td><td>0.72</td></tr><tr><td>1,000</td><td>0.01</td><td>10</td><td>0.9</td><td>1</td><td>0.95</td><td>0.95</td></tr><tr><td>1,000</td><td>0.01</td><td>10</td><td>0.05</td><td>6</td><td>0.843</td><td>0.868</td></tr><tr><td>1,000</td><td>0.01</td><td>10</td><td>0.9</td><td>6</td><td>0.980</td><td>0.985</td></tr><tr><td>1,000</td><td>0.01</td><td>30</td><td>0.05</td><td>6</td><td>2.215</td><td>2.243</td></tr><tr><td>1,000</td><td>0.01</td><td>300</td><td>0.05</td><td>1</td><td>11.11</td><td>11.06</td></tr><tr><td>1,000</td><td>0.01</td><td>300</td><td>0.9</td><td>1</td><td>18.73</td><td>18.69</td></tr><tr><td>1,000</td><td>0.01</td><td>300</td><td>0.05</td><td>6</td><td>14.23</td><td>14.24</td></tr><tr><td>1,000</td><td>0.01</td><td>300</td><td>0.9</td><td>6</td><td>23.45</td><td>23.44</td></tr></table>

7.4.2. Finite Session Lifetime and $( n , P _ { f } , \tau )$ Policy. We next relax the assumption of long session lifetime relative to the arrival rate and consider the possibility that a monitored session dies before being evicted from the hot list. We assume that sessions have a finite lifetime following an exponential distribution. To study the effect of session death, we introduce a new $( n , \bar { P _ { f } } , \tau )$ policy where  is the age threshold of monitored sessions. The values of n and  as well as $P _ { f }$ are chosen in the first stage. Then, in real time, if a monitored session reaches age $\tau ,$ it is dropped from the monitoring list. Thus, the number of sessions being monitored changes with time. The size-based $( n , P _ { f } )$ policy studied in Section 5 drops a session (with the oldest age) only when a new session arrives. We study how the $( n , P _ { f } , \tau )$ policy compares against this sizebased policy. Once we introduce the option of dropping a session older than $\tau ,$ the hot list no longer has a constant number of sessions in steady state. In other words, the number of sessions becomes a random variable whose distribution is very difficult to solve. As a result, it is difficult to solve the $( n , P _ { f } , \tau )$ policy analytically. Therefore, we resort to simulation to study the $( n , P _ { f } , \tau )$ policy. We also study an $( n , P _ { f } , \infty )$ policy that chooses n as well as $P _ { f }$ optimally in the first stage but sets  to be infinity. Unlike the size-based policy, the $( n , P _ { f } , \infty )$ policy assumes the same session lifetime distribution as the $( n , P _ { f } , \tau )$ policy.

Table 10 Comparing Three Monitoring Policies

<table><tr><td rowspan="2"> $I_0$ </td><td> $(n, P_f) policy$ </td><td colspan="5"> $(n, P_f, \tau) policy$ </td><td colspan="4"> $(n, P_f, \infty) policy$ </td></tr><tr><td> $J_n$ </td><td> $n^*$ </td><td> $P_f^*$ </td><td> $\tau^*$ </td><td> $J^*$ </td><td> $(J^* - J_n)/J_n (\%)$ </td><td> $n^*$ </td><td> $P_f^*$ </td><td> $J^*$ </td><td> $(J^* - J_n)/J_n (\%)$ </td></tr><tr><td>20</td><td>24.02</td><td>62</td><td>0.23</td><td>12.8</td><td>27.17</td><td>13.1</td><td>60</td><td>0.22</td><td>27.11</td><td>12.9</td></tr><tr><td>40</td><td>28.11</td><td>71</td><td>0.15</td><td>13.4</td><td>28.55</td><td>1.7</td><td>65</td><td>0.18</td><td>28.32</td><td>0.9</td></tr><tr><td>80</td><td>28.43</td><td>74</td><td>0.15</td><td>12.8</td><td>28.99</td><td>2.0</td><td>70</td><td>0.15</td><td>28.48</td><td>0.2</td></tr><tr><td>100</td><td>28.43</td><td>74</td><td>0.14</td><td>13.3</td><td>28.95</td><td>2.0</td><td>68</td><td>0.16</td><td>28.50</td><td>0.4</td></tr><tr><td>200</td><td>28.46</td><td>77</td><td>0.15</td><td>12.6</td><td>29.00</td><td>1.9</td><td>66</td><td>0.16</td><td>28.53</td><td>0.2</td></tr></table>

In our simulation, we assume that the session lifetime is distributed as $l _ { 0 } + \tilde { x }$ where x˜ is an exponential random variable. The parameter $l _ { 0 }$ represents the minimum lifetime of a session. We next compare the performance of the three policies; the results are shown in Table 10.

To better understand the insights from Table 10, we first note that the total traffic sent for monitoring under the size policy is given by Equation (29) and found to be $3 . 4 / s$ under $P _ { f } = 0 . 1 4 8$ for the baseline values given in Table 4. Since the hot list size is about 65 under the size policy (see Table 6), it takes approximately $T _ { \mathrm { f i l l } } =$ $6 5 / 3 \bar { . } 4 \approx \dot { 2 } 0$ seconds to fill the hot list. From Table $^ { 1 0 , }$ when the multiplier of $l _ { 0 } / T _ { f l l }$ is small (around 1), the $( n , P _ { f } , \tau )$ policy can improve performance (over the size policy) by more than 10%. However, if the multiplier of $\dot { l } _ { 0 } / T _ { f l l } ^ { \dot {  } }$ is greater than 2, then the simple size policy with a fixed n and $P _ { f }$ given by Table 6 performs quite well; the more sophisticated $( n , P _ { f } , \tau )$ or $( n , P _ { f } , \infty )$ policy can only improve the performance by no more than 2%. Thus the size policy should perform well in a typical Web browsing environment where a session typically lasts more than several minutes (Bucklin and Sismeiro 2003), i.e., $l _ { 0 } > 1 0 0 s .$ Furthermore, the performance improvement of $( n , P _ { f } , \tau )$ policy over $( n , P _ { f } , \infty )$ policy is also no more than 2%. This result implies that an optimization over two variables $( n , P _ { f } )$ (instead of over three variables $( n , P _ { f } , \tau )$ as in the $\left( \boldsymbol { n } , \boldsymbol { P _ { f } } , \tau \right)$ policy) is sufficient, thus greatly reducing the search space and the time needed to find an optimal solution.

One might expect that the optimal monitoring size under the $( n , P _ { f } , \tau )$ policy is larger than that under the size policy since the option of dropping older sessions would make the marginal value of a session higher under the $( n , P _ { f } , \tau )$ policy. However, simulation shows that this is not always true when a session is likely to end before being dropped from the hot list, $\mathrm { i . e . , }$ the multiplier $l _ { 0 } / T _ { f i l l }$ is small. Such a counterintuitive result arises from the opposing effects of the option of dropping a session and of the early ending of a session. When the session ending effect dominates the session dropping option, it is less valuable to monitor a session. Therefore, the optimal $n ^ { * }$ under the $( n , P _ { f } , \tau )$ policy decreases, as we can see in the case of $\dot { l } _ { 0 } =$ 20: the optimal $n ^ { * }$ is $6 2 ,$ lower than that of the size policy given in Table 6. When $l _ { 0 }$ increases, the early ending effect becomes less significant, and the monitoring size increases, consistent with the notion of the option of dropping a session. The value of the dropping option under the $( n , P _ { f } , \tau )$ policy converges to a constant (≤ 2%) as $l _ { 0 }$ becomes very large.

## 8. Conclusion

In this work, we analyzed a size-based security monitoring policy with and without profiling. Through accurate approximation methods, we are able to obtain closed-form solutions for a single dimensional optimization problem (no-profiling case) and reduce a complex, two-dimensional optimization problem to a one-dimensional one. One interesting result from the analysis is that monitoring size and traffic volume can be either complements or substitutes when both profiling and monitoring are chosen optimally. When monitoring costs are relatively large, they are complements. When monitoring costs are relatively small, they behave as substitutes: an increased monitoring cost leads to reduced monitoring size, but more traffic is monitored. This is different from what happens when profiling is not an option: higher traffic always implies more monitoring. Another interesting finding is that when traffic profiling is more effective (or when the traffic is less age sensitive), less traffic is monitored coupled with a larger monitoring size; once again traffic volume and monitoring are substitutes. However they become complements with regard to initial malicious traffic: more traffic is monitored coupled with a larger monitoring size as the percentage of initial malicious traffic increases.

We also conducted an extensive set of simulation by allowing more general session arrival processes and finite session lifetime. The results show that our analytical results are quite robust. In addition, through policy comparison, we find that a simple size-based policy is quite robust for a very reasonable range of values for the lifetime of sessions and, under typical situations, is expected to perform almost as well as more sophisticated policies do. A monitoring policy that evicts sessions older than a certain age can only do marginally better than one that evicts sessions only when a new session arrives to take its place. There are two practical benefits of the reduced problem, where eviction is initiated by new arrivals. First, it greatly reduces the time to find an optimal solution. Second, a monitoring policy that uses age in the eviction decision complicates policy implementation without a significant improvement in performance.

An important practical implication from our results is related to the design of an outsourcing contract for profiling and monitoring. In a reward-based contract where a security vendor is paid based on the number of suspicious events detected, to obtain a socially optimal outsourcing solution, we propose a modified form based on the volume of traffic monitored, in addition to the number of suspicious events detected. This is done to prevent the security vendor from indiscriminately monitoring traffic for the sake of increasing the number of suspicious events.

We also studied penalty-based contracts. An interesting result from our analysis is that penalty schemes commonly used in practice (specifically, when the penalty is levied as a percentage of the monthly service fee) do not achieve the social optimum. We show how an appropriate penalty coefficient can be chosen to implement a socially optimal penalty-based contract. In addition, we provide a high-level comparison between reward- and penalty-based contracts. In a penalty-based contract, the setting of the fixed payment can be challenging since to implement the contract it requires common knowledge of an additional parameter—the expected malicious event rate of the client firm that needs to be observed through a period of no monitoring.

There are several avenues for future work. It will be interesting to explore situations where the attack behavior changes with the extent of monitoring. This may require a differential game-theoretic analysis. It may also be interesting to consider contracts where the tasks of profiling and monitoring are outsourced to different security vendors (or profiling is done in-house, while monitoring is outsourced). Also, this paper has made a few assumptions that can be relaxed. First, the firewall was considered exogenous to the profiling and monitoring tasks. Future research could use the current study as a basis for the global optimization of all three tasks of firewall configuration, profiling, and monitoring. Second, instead of being an exogenous parameter, the quality of profilers can be improved through investment. Last but not least, one can consider the cost of attack events missed by the profilers or because of sessions’ old age, and explore the impact of including such cost on profiling and monitoring.

## Supplemental Material

Supplemental material to this paper is available at https:// doi.org/10.1287/isre.2016.0677.

## Acknowledgments

The authors gratefully acknowledge the support provided by WestGrid and Compute Canada Calcul Canada.

## References

August T, Tunca TI (2011) Who should be responsible for software security? A comparative analysis of liability policies in network environments. Management Sci. 57(5):934–959.

August T, Niculescu MF, Shin H (2014) Cloud implications on software network structure and security risks. Inform. Systems Res. 25(3):499–510.

Axelsson S (2000) Intrusion detection systems: A taxonomy and survey. Technical Report 99–15 Department of Computer Engineering, Chalmers University of Technology, Gothenburg, Sweden.

Baayer J, Regragui B, Baayer A (2014) False positive responses optimization for intrusion detection system. J. Inform. Security 5(2):19–36.

Bai X, Gopal R, Nunez M, Zhdanov D (2014) A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes. Decision Support Systems 57(1):406–416.

Bejtlich R (2004) The Tao of Network Security Monitoring: Beyond Intrusion Detection (Addison-Wesley Professional, Boston).

Brown JD (2012) To outsource or not outsource: That is the network security question. StillSecure White Paper. http://www .hostway.com/managed-security/media/StillSecure%20Insource \_vs\_Outsource\_whitepaper.pdf.

Bucklin R, Sismeiro C (2003) A model of Web site browsing behavior estimated on clickstream data. J. Marketing Res. 40(3):249–267.

Cavusoglu H, Cavusoglu H, Raghunathan S (2004a) Economics of IT security management: Four improvements to current security practices. Comm. Assoc. Inform. Systems 14(3):65–75.

Cavusoglu H, Koh B, Raghunathan S (2010) An analysis of the impact of passenger profiling for transportation security. Oper. Res. 158(5):1287–1302.

Cavusoglu H, Mishra B, Raghunathan S (2004b) A model for evaluating IT security investments. Comm. ACM 47(7):87–92.

Cavusoglu H, Mishra B, Raghunathan S (2005) The value of intrusion detection systems in information technology security architecture. Inform. Systems Res. 16(1):28–46.

Cavusoglu H, Raghunathan S, Cavusoglu H (2009) Configuration of and interaction between information security technologies: The case of firewalls and intrusion detection systems. Inform. Systems Res. 20(2):198–217.

Cavusoglu H, Raghunathan S, Yue WT (2008) Decision-theoretic and game-theoretic approaches to IT security investment. J. Management Inform. Systems 25(2):281–304.

Cezar A, Cavusoglu H, Raghunathan S (2014) Outsourcing information security: Contracting issues and security implications. Management Sci. 60(3):638–657.

Cisco (2015) Cisco security monitoring, analysis, and response system 4.3.1 and 5.3.1. http://goo.gl/7xfIVO.

Datta A, Dutta K, Thomas H, VanderMeet D (2003) World wide wait: A study of Internet scalability and cache-based approaches to alleviate it. Management Sci. 49(10):1425–1444.

Dell (2015) Going the MSSP route. http://www.secureworks.com/ assets/pdf-store/articles/going\_the\_mssp\_route\_-\_tco\_issues .pdf.

Ding W, Yurcik W (2005) Outsourcing Internet security: The effect of transaction costs on managed service providers. Gavish B, ed. Internat. Conf. Telecomm. Systems, Modeling, Anal. (Institute for Information Infrastructure Protection, Washington, DC), 947–958.

Ding W, Yurcik W (2006) Economics of Internet security outsourcing: Simulation results based on the Schneier model. Workshop Econom. Securing Inform. Infrastructure 4WESII5 (American Telecommunications Systems Management Association, Dallas), 23–23.

F5 Networks (2013) Configuration guide for BIG-IP application security manager. Seattle, https://goo.gl/L9s7HZ.

F5 Networks (2015) BIG-IP application security manager online manual. Seattle, https://support.f5.com/kb/en-us/products/ big-ip\_asm.html.

Fang X, Sheng LOR, Gao W, Iyer B (2006) A data-mining-based prefetching approach to caching for network storage systems. INFORMS J. Comput. 18(2):267–282.

Fisher W, Meier-Hellstern K (1993) The Markov-modulated Poisson process (MMPP) cookbook. Performance Evaluation 18(2): 149–171.

Fitzparick V (2008) Intrusion detection and prevention in-sourced or out-sourced. SANS Inst. InfoSec Reading Room, http://www.sans .org/reading-room/whitepapers/intrusion/intrusion-detection -prevention-in-sourced-out-sourced-32854.

Garfinkel R, Gopal R, Thompson S (2007) Releasing individually identifiable microdata with privacy protection against stochastic threat: An application to health information. Inform. Systems Res. 18(1):23–41.

Gartner (2014) Gartner says worldwide information security spending will grow almost 8 percent in 2014 as organizations become more threat-aware. http://www.gartner.com/newsroom/id/ 2828722.

Goodall JR, Lutters WG, Komlodi A (2004) I know my network: Collaboration and expertise in intrusion detection. Herbsleb J, Olson G, eds. Proc. 2004 ACM Conf. Comput. Supported Cooperative Work (ACM, New York), 342–345.

Goodall JR, Lutters WG, Komlodi A (2009) Developing expertise for network intrusion detection. Inform. Tech. People 22(2):92–108.

Gupta A, Zhdanov D (2012) Growth and sustainability of managed security services networks: An economic perspective. MIS Quart. 36(4):1109–1130.

Heindl A (2003) Decomposition of general queueing networks with MMPP inputs and customer losses. Performance Evaluation 51(2–4):117–136.

Hewlett-Packard (2013) Security operations—Building a successful SOC. http://www8.hp.com/h20195/V2/GetPDF.aspx/4AA4 -6169ENW.pdf.

Himberger KD, Jeffries CD, McMillen DM, Ziraldo JA (2006) System, method, and program product for managing an intrusion detection system. US Patent US7084760 B2.

Hosanagar K, Tan Y (2011) Cooperative cashing? An economic analysis of document duplication in cooperative Web caching. Inform. Systems Res. 23(2):356–375.

Hui KL, Hui W, Yue WT (2012) Information security outsourcing with system interdependency and mandatory security requirement. J. Management Inform. Systems 29(3):117–156.

IBM (2015) IBM managed security services for security event and log management. http://www-935.ibm.com/services/us/igs/ pdf-iss-contracts/ireland-7808-00.pdf.

Jonsson E, Olovsson T (1997) A quantitative model of the security intrusion process based on attacker behavior. IEEE Trans. Software Engrg. 23(4):235–245.

Kaplan J (2003) Outsourcing trends—A matter of perspective? Bus. Comm. Rev. 33(8):46–50.

Kavanagh K, Pescatore J (2009) Magic quadrant for MSSPs, North America. Gartner RAS Core Res. Note G00166138. http:// www.tatacommunications.com/downloads/enterprise/Tata \_Communications\_3053.pdf.

Kaya C, Zhang G, Tan Y, Mookerjee V (2009) An admission-control technique for delay reduction in proxy caching. Decision Support Systems 46(2):594–603.

Kelly T, Reeves R (2001) Optimal Web cache sizing: Scalable methods for exact solutions. Comput. Comm. 24(2):163–173.

Kerr D (2013) Bots now running the Internet with 61 percent of Web traffic. CNET (December 12). http://www.cnet.com/ news/bots-now-running-the-internet-with-61-percent-of-web -traffic/.

Kim E (2015) Companies are freaked out about cybersecurity and plan to spend a lot more on it this year. Bus. Insider (January 6) https://goo.gl/XOMTKz.

Kubota M (2005) Intrusion detection and prevention system. US Patent US7757285 B2.

Kumar S, Spafford E (1996) A pattern matching model for misuse intrusion detection. Working paper, Purdue University, West Lafayette, IN.

Lacity MC, Khan SA, Willcocks LP (2009) A review of the IT outsourcing literature: Insights for practice. J. Strategic Inform. Systems 18(3):130–146.

Law A (2014) Simulation Modeling and Analysis, 3rd ed. (McGraw-Hill, Boston).

Lord N (2015) How to hire and evaluate managed security service providers (MSSPs). Digital Guardian, https://goo.gl/UWYdS2.

McLay L, Jacobson S, Kobza J (2006) A multilevel passenger screening problem for aviation security. Naval Res. Logist. 53(3): 183–197.

McLay L, Jacobson S, Kobza J (2008) The trade-off between technology and prescreening intelligence in checked baggage screening for aviation security. J. Transportation Security 1(2):107–126.

Mitchell R, Chen I (2014) A survey of intrusion detection techniques for cyber-physical systems. ACM Comput. Surveys 46(4): Article 55.

Moitra S, Konda S (2000) A simulation model for managing survivability of networked information systems. Technical Report, Carnegie Mellon Software Engineering Institute, Carnegie Mellon University, Pittsburgh.

Monrose F, Rubin A (1997) Authentication via keystroke dynamics. 4th ACM Conf. Comput. Comm. Security (ACM, New York), 48–56.

Mookerjee V, Tan Y (2002) Analysis of a least recently used cache management policy for Web browsers. Oper. Res. 50(2):345–357.

Neumann P, Porras P (1999) Experience with Emerald to date. Ranum M, ed. Proc. 1st USENIX Workshop Intrusion Detection Network Monitoring (USENIX, Berkeley, CA), 73–80.

Ogut H, Cavusoglu H, Raghunathan S (2008) Intrusion-detection policies for IT security breaches. INFORMS J. Comput. 20(1): 112–123.

Peng T, Leckie C, Ramamohanarao K (2007) Survey of networkbased defense mechanisms countering the DoS and DDoS problems. ACM Comput. Surveys 39(1):Article 3.

Pietro RD, Mancini LV (2008) Intrusion Detection Systems (Springer, New York).

Podlipnig S, Bszrmenyi L (2003) A survey of Web cache replacement strategies. ACM Comput. Surveys 35(4):374–398.

Ransbotham S, Mitra S (2009) Choice and chance: A conceptual model of paths to information security compromise. Inform. Systems Res. 20(1):121–139.

Sandhu UA, Haider S, Naseer S, Ateeb OU (2011) A survey of intrusion detection and prevention techniques. Internat. Conf. Inform. Comm. Management (IACSIT Press, Singapore), 66–71.

Santor MSS (2015) NetworkSentry: Efficient network surveillance from Sentor. https://www.sentormss.com/managed-security -services/networksentry-network-surveillance/.

Scarfone K, Mell P (2007) Guide to intrusion detection and prevention systems (IDPS). Technical Report, National Institute of Standards and Technology, Gaithersburg, MD.

Schneier B (2002) The case for outsourcing security. IEEE Comput. 35(4):20–26.

Schneier B (2007) Managed security monitoring: Network security for the 21st century. Report, British Telecommunications, London. http://www2.computable.nl/downloads/Counterpane \_WP5.pdf.

Smith B (2015) Thinking about security monitoring and event correlation. http://www.secureworks.com/resources/articles/ other\_articles/correlation/.

Sommestad T, Hunstad A (2013) Intrusion detection and the role of the system administrator. Inform. Management Comput. Security 21(1):30–40.

Statista (2015) Monthly unique visitors to U.S. retail websites in 3rd quarter 2014. http://www.statista.com/statistics/271450/ monthly-unique-visitors-to-us-retail-websites/.

The White House (2015) Remarks by the President at the cybersecurity and consumer protection summit. http://www.white house.gov/the-press-office/2015/02/13/remarks-president -cybersecurity-and-consumer-protection-summit.

Ulvila JW, Gaffney JE (2004) A decision analysis method for evaluating computer intrusion detection systems. Decision Anal. 1(1):35–50.

Verizon (2012) Managed security services—Premises premium+. https://goo.gl/H1CXdl.

Virta J, Jacobson S, Kobza J (2003) Analyzing the cost of screening selectee and non-selectee baggage. Risk Anal. 23(5):897–908.

Werlinger R, Hawkey K, Muldner K (2008) The challenges of using an intrusion detection system: Is it worth the effort? Proc. 4th Sympos. Usable Privacy Security (ACM, New York), 107–118.

Werlinger R, Muldner K, Hawkey K, Beznosov K (2009) Towards understanding diagnostic work during the detection and investigation of security incidents. Furnell S, Clarke N, eds. Proc. Third Internat. Sympos. Human Aspects Inform. Security Assurance (University of Plymouth, Plymouth, UK), 119–134.

Werlinger R, Muldner K, Hawkey K, Beznosov K (2010) Preparation, detection, and analysis: The diagnostic work of IT security incident response. Inform. Management Comput. Security 18(1):26–42.

Whang S (1992) Contracting for software development. Management Sci. 38(3):307–324.

Zamboni D, Spafford E (1999) New directions for the AAPHID architecture. Spafford G, ed. Workshop Recent Adv. Intrusion Detection (Purdue University, West Lafayette, IN).

Zhao X, Whinston A (2013) Managing interdependent information security risks: Cyberinsurance, managed security services, and risk pooling arrangements. J. Management Inform. Systems 30(1):123–152.

Zwillinger D (2011) CRC Standard Mathematical Tables and Formulae, 32nd ed. (CRC Press, Boca Raton, FL).
