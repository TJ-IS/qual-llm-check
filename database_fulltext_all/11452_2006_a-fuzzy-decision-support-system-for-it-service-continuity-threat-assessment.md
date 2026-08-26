---
otero_id: 11452
otero_key: "E7J3PX3C"
title: "A fuzzy decision support system for IT Service Continuity threat assessment"
authors: "Bartel Van de Walle; Anne-Francoise Rutkowski"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.05.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A fuzzy decision support system for IT Service Continuity threat assessment

Bartel Van de Walle <sup>⁎</sup>, Anne-Francoise Rutkowski

Department of Information Systems and Management, Tilburg University, The Netherlands

Received 11 July 2005; received in revised form 18 January 2006; accepted 10 May 2006 Available online 13 July 2006

## Abstract

Using fuzzy relational modeling for preference visualization, the FURIA fuzzy decision support system aims to facilitate preference alignment and group agreement. Findings are presented from a field study on IT Service Continuity threat assessments by IT and business managers that motivate the design and development of the FURIA prototype. The results of a pilot evaluation indicate that groups using FURIA are more satisfied with their decision process, consider the process to be better coordinated and show more agreement with the group decision as compared to groups not using FURIA. Therefore, the results indicate that the prototype performs to expectations. © 2006 Elsevier B.V. All rights reserved

Keywords: Fuzzy sets; Decision support systems; IT Service Continuity; Threat analysis

## 1. Introduction

IT Service Continuity (ITSC) management focuses on the continuity of IT services within the organization to provide a pre-determined and agreed level of IT services to support the minimum business requirements following an interruption to the business. ITSC management is typically part of a larger Business Continuity Management (BCM) program, which expands beyond IT to include all business services within an organization. ITSC management allows an organization to identify, assess and take responsibility for managing its risks or threats to IT. The increased attention to ITSC in recent years has led many organizations to list all possible threats and risks to the continuity of their IT services. Ideally, such a list or risk registry is complete and tailored to the organization. A key problem in the construction of this list and the ensuing ITSC management is that the different stakeholders involved – such as staff, customers or shareholders – perceive the impact, likelihood and scope of the threats posed to the IT services in a different way [25].

The research findings reported here result from a field research program conducted within a large multinational organization's IT Service Continuity management division for nearly 2 years. In the course of our research, we were confronted with a lack of alignment between IT and business managers regarding the identification of ITSC risks and preferences for the corresponding mitigation measures. On several occasions, this was leading to significant communication clashes between both groups, provoking lengthy discussions during which no consensus was reached on the importance of the risks nor the measures needed. We have reported elsewhere how the use of Group Support Systems (GSS) technology and decision workshops enabled management to successfully arrive at a fairly comprehensive agreed list of key ITSC risks, including risks that were originally identified by just a few or even single members of one of the stakeholder groups [39,40].

Although the use of GSS technology and methods was perceived as a success, the division's managers remained concerned about the lack of agreement and convergence of the discussion within and among the IT and business groups. It was argued that if members of both groups could assess how close – or how far apart – their individual preferences are at any stage of the discussion, communication would be more effective and agreement would be easier to reach. In response to this concern, we designed and developed FURIA (Fuzzy Relational Incident Analysis), a prototype fuzzy decision support system allowing individual group members to compare their individual assessment of a decision alternative (such as an ITSC risk) to the assessments of the other group members. At the very core of FURIA is an interactive graphical display visualizing group members' relative preference positions. Earlier research has indeed demonstrated that any person has a fundamental need to evaluate his abilities and opinion by comparing him or herself to others, and this particularly in the absence of clearly defined criteria [18]. When carefully balanced, this process of social comparison contributes to better group decision-making [36].

The main objective of this paper is to present the development and a successful experimental evaluation of FURIA – and in particular its visualization of individual preferences – to address preference alignment problems among group members. Although the actual use of FURIA is context independent, we choose to focus on IT Service Continuity as this provides for the organizational context in which the motivation for the design and development of FURIA was clearly pronounced. We hence introduce IT Service Continuity management and clarify the importance of threats and organizational controls in the following section. The response to a threat and the potential contribution of decision support systems for better threat response decision-making is discussed as well. Section 3 summarizes the mathematical foundations from fuzzy set theory on which the design of FURIA is based, the development of which is presented in Section 4. The experimental evaluation of FURIA is presented in Section 5, and we conclude by summarizing our findings and indicating future research in Section 6.

## 2. IT Service Continuity management

Business Continuity Management (BCM) can be broadly defined as the management process that is concerned with the continuity or resuming of all critical services upon which the business depends within a predefined time after a disruption. As IT is one of these services, IT Service Continuity (ITSC) management is focused on the continuity of IT and is an important part of the overall BCM process [22] as shown in Fig. 1.

IT Service Continuity management requires an organization to identify, assess and take responsibility for managing its threats to IT, thus enabling it to better understand the environment in which it operates, to decide which threats it wants to prevent from becoming real, and to act positively to protect the interests of all stakeholders, which include employees, customers, shareholders, partners, suppliers, etc. [2,33].

## 2.1. IT Service Continuity: threats and controls

A threat is defined as any act, entity, event or phenomenon with the potential to harm a person or thing. In other words, a threat is a source of potential harm. Sometimes the word hazard or risk is used as a synonym for threat. As listed in Table 1, common threat sources can be human, natural or environmental, and threats range from terrorist activities, computer virus attacks and uncontrolled fire, to sabotage by employees.

To counter human threats, intrusion detection tools are becoming more prevalent, and government and industry organizations continuously collect data on security events, thereby improving the ability to realistically assess threats [15]. However, it should be noted that many businesses and governments do not want to draw attention to successful attacks upon their systems for fear of other attacks. Therefore, available statistics about threats are not always complete and might be biased [5,43].

In order for the threat to cause harm, it must find a weakness in the protection of a person or thing that can be accidentally triggered or intentionally exploited. The methodology needed to determine whether vulnerabilities are present varies depending on the nature of the information systems and the phase of the software development lifecycle [14]:

• Design phase: The search for vulnerabilities should focus on the organization's security policies, planned security procedures and system requirement definitions, and the vendor's or developer's security product analysis.

• Implementation phase: The identification of vulnerabilities should be expanded to include more specific information, such as the planned security features described in the security design documentation and the results of system certification test and evaluation.

Business Continuity Management  
![](/api/attachments/E7J3PX3C/fulltext/images/d909a606298afb1f9dcb8ecb30c0108f78993b785f09a62addf8c46e340b3e75.jpg)  
Fig. 1. IT Service Continuity management as part of business continuity management.

• Operational phase: The process of identifying vulnerabilities should include an analysis of the information system security features and the security controls, technical and procedural, used to protect the system.

Sometimes, historical data are available that can provide information on how likely it is that a threat will cause harm within a specific period of time. However, in the more likely case when no or insufficient historical data are present, additional research is needed to determine the likelihood of threats, for instance through interviewing experts or distributing questionnaires. An important indicator is the Annualized Rate of Occurrence (ARO) of a threat. For example, a threat occurring once in 10 years has an ARO of 0.1; a threat occurring 10 times a year has an ARO of 10 [1,7]. The Australian Department of Commerce uses a likelihood distribution of threats over seven levels, converted into Annual Rates of Occurrence as shown in Table 2.

A control or safeguard is any action, device, procedure, technique or other measure that has been implemented by the organization to minimize or eliminate the likelihood of a threat's exercising a system vulnerability [14,30,43]. Controls encompass the use of technical and non-technical methods. Technical controls are safeguards that are incorporated into computer hardware or software. Non-technical controls are management and operational controls such as security policies, operational procedures, and personnel, physical and environmental security. Both techni cal and non-technical control methods can be further classified as either preventive or detective. Preventive controls inhibit attempts to violate security policy and include controls such as access control enforcement, encryption and authentication. Detective controls warn of violations or attempted violations of security policy. An example of a detective control is an intrusion detection method.

Table 1  
Common threat sources (Stoneburner et al. [43])

<table><tr><td>Common threat sources</td><td>Examples</td></tr><tr><td colspan="2">Human threats</td></tr><tr><td>Unintentional acts</td><td>Inadvertent data entry</td></tr><tr><td>Intentional acts</td><td>Network based attacks, malicious software upload, unauthorized access to confidential information</td></tr><tr><td>Natural threats</td><td>Floods, earthquakes, tornadoes, landslides, avalanches</td></tr><tr><td>Environmental threats</td><td>Long-term power failure, pollutions, chemicals, liquid leakage</td></tr></table>

Table 2  
Threat likelihood transformed to annual rate of occurrence

<table><tr><td>Likelihood</td><td>Description</td><td>ARO (frequency per annum)</td></tr><tr><td>Negligible</td><td>Unlikely to occur (&lt; twice every 5 years)</td><td>0.05</td></tr><tr><td>Very Low</td><td>2–3 times every 5 years</td><td>0.6</td></tr><tr><td>Low</td><td>≤ once per year</td><td>1.0</td></tr><tr><td>Medium</td><td>≤ once every 6 months</td><td>2.0</td></tr><tr><td>High</td><td>≤ once per month</td><td>12.0</td></tr><tr><td>Very high</td><td>≥ once per month</td><td>36.0</td></tr><tr><td>Extreme</td><td>≥ once per day</td><td>365.0</td></tr></table>

When a threat realizes by exploiting vulnerabilities in the protection despite the controls implemented by the organization, the organization wants this disaster to be mitigated and brought to an end as quickly as possible. This process is called disaster response and recovery, and the procedures to follow in case of a disaster are described in disaster response and recovery plans. A good plan should prepare the organization to deal with any kind of event that could halt or slow down business processes [49].

## 2.2. Threat assessment and decision-making

Organizational failures due to inadequate disaster response plans have been widely documented in management literature, and a general awareness exists among managers about the possibly fatal consequences of inadequate disaster response planning [41]. Nevertheless, the process of threat assessment and analysis often proves to be a challenge. At the organization introduced above, for instance, we found that the quality of the response to a threat was hampered by a lack of awareness and information exchange among individuals or groups [39]. Business and IT managers at that organization perceived the threats and the financial consequences very differently, and neither group was aware of all threats. Hence, convergence towards a common list of key risks and counter-measures proved challenging. It has been well documented in literature that the chance of defective group decisionmaking, such as group think, is higher when the situation is very stressful and the group is too cohesive and socially isolated [23]. The participants involved in the decision are cognitively overloaded, and the group fails to adequately determine its objectives and alternatives, fails to explore all the options and also fails to assess the risks associated with the group's decision itself. Janis [23] also introduced the concept of “hypervigilance”, an excessive alertness to signs of threats. Hypervigilance causes people to make “illconsidered decisions that are frequently followed by postdecisional conflict and frustration”. The “threat-rigidity” hypothesis, first developed by Staw, Sandelands and Dutton [42] and further discussed by Rice [35], states that individuals undergoing stress, anxiety and psychological arousal tend to increase their reliance on internal hypotheses and focus on dominant cues to emit well-learned responses. In other words, the potential decision response to a crisis situation is to ‘go by the book’ based on learned responses. However, if the response situation does not fit the original training, the resulting decision may be ineffective and even make the crisis situation worse. In order to counter this bias, Turoff et al. [44] state that crisis response teams must be encouraged and trained to make flexible and creative decisions. The attitude of those responding to the crisis and the cohesive nature of the teams involved is critical to the success of the effort [26].

Decision Support Systems (DSS), Group Decision Support Systems (GDSS) and Group Support Systems (GSS) have been developed to support and facilitate individuals and groups in handling complex problems [20,24], such as managing the response to a crisis [4,44]. Despite differences in the conceptualization of various GSS, all approaches agree on the necessity to facilitate the interactive sharing and use of information among group members [13]. GSS aim to facilitate the development of new beliefs in groups by supporting processes of negotiation of meanings between participants [17]. As such, GSS facilitate group decision-making and problem solving, support the sharing of information and the development of consensus and creativity [11,31].

## 3. Preference modeling framework and fuzzy relational analysis

## 3.1. Preference modeling and fuzzy relations

We provide first a short introduction to the preference modeling framework we will utilize further. In essence, preference modeling techniques allow a decision-maker to express his or her preferences regarding the available decision alternatives such that a meaningful rank order of the alternatives can be obtained [38,48]. In general, any relationship between decision alternatives can be expressed by means of one of three possible preference relations: (strict) preference, indifference and incomparability. More formally, these three preference relations are defined as follows [37]:

• A couple of alternatives (such as, for instance, a couple of threats $( t _ { a } , t _ { b } ) )$ belongs to the strict preference relation $P$ if and only if the decision-maker prefers threat $t _ { a }$ to threat $t _ { b }$ (‘preferring’ threat $t _ { a }$ to threat $t _ { b }$ indicating in this case for instance that threat $t _ { a }$ has a lower potential impact than threat $t _ { b } )$ ;

• A couple of alternatives $( t _ { a } , t _ { b } )$ belongs to the indifference relation I if and only if the decision-maker is indifferent between alternatives $t _ { a }$ and $t _ { b } ;$

• A couple of alternatives $( t _ { a } , t _ { b } )$ belongs to the incomparability relation J if and only if the decision-maker is unable to compare alternatives $t _ { a }$ and $t _ { b } ,$ for instance caused by conflicting or insufficient information.

These relations provide a crisp classification of a decision-maker's preferences: a decision-maker either expresses his or her strict preference or indifference among any two alternatives, or declares the alternatives to be incomparable. It is not always very easy for a decisionmaker, however, to assign a couple of alternatives to one of these relations unequivocally. To overcome this ‘crisp’ classification problem, one established approach is to introduce a gradual transition from membership (e.g., definitely preferred) to non-membership (e.g., definitely not preferred), and allowing for partial degrees of membership. This approach brings us in the realm of fuzzy set theory [16,50].

Formally, a fuzzy set A on a universe X is a mapping from X to the unit interval [0,1], with the value A(x) of A in x of X the degree of membership of x in A. $A ( x ) = 1$ means full membership, A(x) = 0 means non-membership, and all values $A ( x )$ in ]0,1[ denote partial membership. In order to analyze a fuzzy set A in X at a particular membership degree ${ \boldsymbol { \alpha } } \in [ 0 , 1 ]$ , we can ‘cut’ the fuzzy set at that degree and consider only the set of elements x of X that have a membership degree A(x) of at least α. The crisp set constructed in this way is called the α-cut of the fuzzy set A and denoted as $A _ { \alpha } .$ As a fuzzy set can again be reconstructed from its α-cuts, ‘cutting’ is used to switch between a fuzzy set and its crisp cuts, to which ‘traditional’, i.e., non-fuzzy, mathematical analysis techniques can be applied. Just as a fuzzy set extends a classical or crisp set, a fuzzy relation then extends the concept of a crisp relation. In this way, a fuzzy strict preference (or indifference or incomparability) relation expresses the strength of a strict preference (or indifference or incomparability) among any pair of alternatives.

Fuzzy set theory has been used extensively for modeling preferences and analyzing decisions, and has led to the development of various fuzzy decision support systems in many different areas, including risk management (among others, see [12,21,29]).

## 3.2. Fuzzy relational decision analysis

In this subsection, we provide a summary of the fuzzy relational decision analysis technique we will use for our purposes. We refer to earlier work for the mathematical details of the technique [47] and some illustrative applications [46,45]. The technique aims to provide a better understanding of the preference information contained in the fuzzy preference relation P. As indicated above, P contains the decision-maker's preferences regarding all decision alternatives (such as threats) expressed by means of pair-wise comparisons. The i-th row of the matrix representation of P, for example, contains all preferences of the form $P ( a _ { i } , a _ { j } )$ with j from 1 to $n ,$ the number of alternatives, or the preference for alternative $a _ { i }$ as compared to the alternative $a _ { j } .$ As P is a fuzzy relation, $P ( a _ { i } , a _ { j } )$ expresses a degree of preference and therefore takes values in the interval [0,1].

The first step in our analysis consists of a pair-wise comparison of all rows in P. Technically speaking, we compute by means of an inclusion measure how much every row is included in any other row [10,9]. The resulting inclusion degree indicates the degree to which one row is included in another, which in turn reflects how strong a decision-maker's preferences on one alternative are related to his or her preferences on another alternative. We summarize the inclusion information in the new fuzzy matrix D, the so-called dependency matrix. As this relation is not necessarily transitive, we need to construct a transitive closure Q of D, i.e., a least inclusive fuzzy relation which is reflexive and transitive [3]. This new relation Q is a fuzzy (quasiorder) relation, for which every α-cut is a (crisp) quasiorder relation [19]. Finally, we visualize the crisp quasiorder relations by means of a Hasse diagram, displaying the different preferences, indifferences or incomparabilities among the decision alternatives as nodes at a specific cut-level. Fig. 2 summarizes the consecutive steps in the fuzzy analysis technique involving the fuzzy relations D and Q leading to the Hasse diagram visualizations at different α-cuts. A more elaborate step-by-step illustration of the transformation of the fuzzy relation P into the Hasse diagrams through D and Q can be found in [46].

## 4. The fuzzy decision support system FURIA prototype

The fuzzy decision support system FURIA (an acronym for Fuzzy Relational Incident Analysis) prototype has been developed to assess individual and group preferences, so that group members can identify how their preferences relate, bridge preference and communication gaps and move their group towards convergence and agreement. FURIA has been developed in Java JDK 1.4 and runs as a stand-alone Java application. The software requires the installation of Java Virtual Machine and of the Tomcat Application server, and uses MS SQLServer as a database. Based on the fuzzy decision analysis technique we presented in the previous section, FURIA provides a visualization of the different preference relationships through the following three-step process.

![](/api/attachments/E7J3PX3C/fulltext/images/ed06d0e29155e813c8008a0edfe87c29bef12aa63d7a543946bf88769bddc348.jpg)  
Fig. 2. Fuzzy decision analysis overview.

## 4.1. Step 1: define the alternatives, criteria and their evaluations by all group members

First, the relevant decision alternatives and criteria have to be defined in FURIA. FURIA provides easy management capabilities for any number of alternatives and criteria. Next, these alternatives can be evaluated by any group member against these criteria. The output of this first step is – for every member of the group – a traditional decision matrix, the rows of which are the decision alternatives, the columns the decision criteria, and its values are the evaluations of the alternatives on the respective criteria.

## 4.2. Step 2: pair-wise comparison of group member preferences by means of profiles

In this second step, we need to transform the decision matrix we have obtained to a matrix amenable for the fuzzy relational analysis outlined in Section 3. We focus on a specific alternative, and the preferences of all other group members are compared in a pair-wise manner. To facilitate this comparison process, a number of predefined comparison criteria can be used for different measures of comparison. These comparison criteria or ‘preference profiles’ can be adapted by the user by setting the parameters of the different functions. The definitions of the preference profiles that are available in FURIA are given in Table 3, and a visual representation is shown in Fig. 3. We note that these functions are also used in the Promethee multi-criteria decision technique developed by Brans and Vincke [6], albeit for a different purpose.

As shown in Table 3 and Fig. 3, six basic ‘preference profiles’ are available through which the distance d between any two group members' preferences is mapped to a [0,1] scale. Depending on the choice of the preference profile, a particular distance $\scriptstyle d ( a , b )$ will be mapped into a specific preference comparison degree $P ( \boldsymbol { a } , \boldsymbol { b } )$ . In all cases, it holds that the larger the preference comparison value $P ( a , b )$ , the more distant the preference $\cdot _ { b } ,$ (as expressed by group member B) is from the preference $\cdot _ { a } ,$ (as expressed by group member A) on a particular criterion. Note that a particular preference profile H(d) always either defines a preference degree $P ( a , b )$ (if $d ( a ,$ $b ) { \geq } 0 )$ or a preference degree $P ( b , a )$ (if $d ( a , b ) \geq 0 )$ . It also always holds that min $( P ( a , b )$ $P ( b , a ) ) = 0 ;$ i.e., as soon as $P ( a , b ) { > } 0$ , we must have that $P ( b , a ) = 0$ , and vice versa.

<table><tr><td colspan="2">Table 3Preference profiles</td></tr><tr><td>Type I: identity criterion</td><td>Type II: U-shaped criterion</td></tr><tr><td> $H(d) = \begin{cases} 0, & d=0, \\ 1, & |d|>0. \end{cases}$ </td><td> $H(d) = \begin{cases} 0, & |d|\leq q, \\ 1, & |d|>q. \end{cases}$ </td></tr><tr><td>Type III: V-shaped criterion</td><td>The parameter  $q$  is a threshold value to be defined by the user.Type IV: level criterion</td></tr><tr><td> $H(d) = \begin{cases} \frac{|d|}{p}, & |d|\leq p, \\ 1, & |d|>p. \end{cases}$ </td><td> $H(d) = \begin{cases} 0, & |d|\leq q, \\ \frac{1}{2}, & q\leq |d|\leq p, \\ 1, & |d|>q. \end{cases}$ </td></tr><tr><td>The parameter  $p$  is a threshold value to be defined by the user.Type V: V-shaped with indifference criterion</td><td>The parameters  $p$  and  $q$  are threshold values to be defined by the user.Type VI: Gaussian criterion</td></tr><tr><td> $H(d) = \begin{cases} 0, & |d|\leq q, \\ \frac{|d|-q}{p-q}, & q\leq |d|\leq p, \\ 1, & |d|>q. \end{cases}$ </td><td> $H(d) = 1 - e^{\frac{-d^{2}}{s^{2}}}$ .</td></tr><tr><td>The parameters  $p$  and  $q$  are threshold values to be defined by the user.</td><td>Again,  $s$  is a parameter to be defined by the user.</td></tr></table>

![](/api/attachments/E7J3PX3C/fulltext/images/d52b1a1d7bb709a800e482003ad3d8c119f2b7fe46444b44fee45d7b152f4331.jpg)

Type II  
![](/api/attachments/E7J3PX3C/fulltext/images/7fcfdb9a2b12416a29f60077445f150da14113354b13a430526f955c3cf64049.jpg)

The matrix resulting from the pair-wise comparison of all group members' preferences forms the preference matrix which is the starting point for the fuzzy relational analysis as outlined in Section 3.

## 4.3. Step 3: the fuzzy relational analysis and resulting Hasse diagrams

Finally, the fuzzy relational decision analysis produces a family of Hasse diagrams corresponding to different α-cuts.

Consider for example the Hasse diagram shown in Fig. 4, offering a visual representation of the relative positions of eight individual decision-makers' preferences. Assume moreover that these individuals belong to two distinct groups within the organization, say they are either business $\mathrm { ( B _ { 1 } , . . . , B _ { 4 } ) }$ or information technology $( \mathrm { I } _ { 1 } ,$ $\mathrm { . . . , I _ { 4 } ) }$ managers at an ITSC department who have expressed their preferences regarding a specific threat on a number of criteria, such as impact and frequency. In this example, we find three members of IT management at the bottom of the diagram, having the same overall preference regarding a specific threat. All other managers from either group have a stronger preference and are visually situated higher in the diagram. Two business managers $\mathrm { ( B _ { 1 } }$ and $\mathbf { B } _ { 2 } )$ have the strongest preferences regarding this threat, yet their preferences are incomparable. This incomparability may for instance be caused because business manager $\mathrm { B } _ { 1 }$ considers this threat to have a very high impact and a low frequency, while business manager $\mathrm { B } _ { 2 }$ believes just the opposite: a moderate impact and a very large frequency. Interestingly, one IT manager (I ) leans towards the preferences of the business managers — she has slightly different preferences than the other IT managers and may be the ideal go-between to address the (preference) gap between both groups.

## 5. Experimentation and results

![](/api/attachments/E7J3PX3C/fulltext/images/f10e9908397b90526c6879c5c8e1a29a38e11b57806385b08704fad2892695cf.jpg)

## 5.1. Introduction

The key objective of FURIA is to allow members of a decision-making group to assess their preferences regarding the available decision alternatives by offering a visualization of the preference relationships that exist among the various group members, so that they are able to align their preferences and reach agreement.

To experimentally validate this objective, we have designed a pilot experiment in which master students in Information Systems at Tilburg University, assigned to small groups, were asked to assume the role of a threat assessment group in the University's IT Service Continuity management process. The participants were asked to read the following description of this pre-tested experimental task:

Type I  
![](/api/attachments/E7J3PX3C/fulltext/images/fd917f6efd2a09469dff37883c63e05d940f05951f774364aa7956e13af6a2e7.jpg)

![](/api/attachments/E7J3PX3C/fulltext/images/78a9fa2c5365cf941f38eb8feb34904fef6fced9016b82b60d2c1a2ea48518d3.jpg)

Type IV  
![](/api/attachments/E7J3PX3C/fulltext/images/2897f0c0fd1a728803a58945cbf82c95d179459480ef6912027af2538a86702b.jpg)  
Type VI  
Fig. 3. Preference profiles.

![](/api/attachments/E7J3PX3C/fulltext/images/75dba25e5b3b39c59237ffe0fd3b1de1080b4a73e98c93d496c1afe4cfcc519e.jpg)  
Fig. 4. Hasse diagram showing individual business $\mathrm { ( B _ { 1 } , . . . , B _ { 4 } ) }$ and IT $\mathrm { ( I _ { 1 } , . . . , I _ { 4 } ) }$ managers' preference positions.

You are member of a group of students which has been asked by the University's IT Services (ITS) department to advise on its IT Service Continuity management strategy for the coming year. The ITS department has previously identified 7 important IT Service Continuity threats deserving the attention of the department. However, as the department's management budget is limited, only 2 out of these 7 threats can be seriously dealt with in the coming year. Your group is asked to make a final recommendation on what those 2 threats should be. So your group's key task is: Select two threats from the original list of seven threats which your group wants the IT Services department to address in the coming year.

The participants then received a sheet with a list of seven threats identified by the IT Services department as given in Table 4, and they were asked to rate these threats on three different criteria: scope, likelihood and impact, each on a 0 (lowest score) to 10 (highest score) scale. The scope is determined by the potential damage, cost or downtime, or cost of lost opportunity. The likelihood is the chance of this threat realizing in the next year, and the impact indicates how bad this disaster, if it occurs, will hurt the organization. Students were asked to consider the worst case, e.g., the event happening on the busiest time of day, on the busiest day of year.

## 5.2. Data collection — experimental design

## 5.2.1. Hypotheses

The use of GDSS influences the group's dynamic and its outcomes, reduces process losses, and to various degrees affects group cohesion, affective reward and satisfaction [34]. Therefore, we postulate that:

Seven IT Service Continuity threats used in the experiment

<table><tr><td>Threats</td><td>Counter-measure</td></tr><tr><td>Fire (natural or deliberate)</td><td>The department wants to install full fire protection systems in all computer rooms, including sprinkler systems, fire-delaying paint on furniture and walls, fire-proof compartments, etc.</td></tr><tr><td>Power outage</td><td>The department already has UPS systems in place in the major computer rooms for short-duration power outages, but wants to extend this to all other computer rooms on campus. Also, building a large diesel engine power group is planned to deal with longer outages.</td></tr><tr><td>Sabotage of equipment</td><td>Additional security measures are required to avoid sabotage from unauthorized people. Access restriction methods and technologies must be implemented for the major computer rooms.</td></tr><tr><td>ITS employees make unintended mistakes</td><td>Often damage occurs by unintended mistakes from employees. The department will develop and implement a training program, so that focused training can be given to ITS employees who need it. An awareness program will be started to make ITS employees aware of the potential consequences of their mistakes.</td></tr><tr><td>Third party software vendor makes unintended mistakes</td><td>Mistakes can also originate from the outside: a software vendor may upgrade its software and make it incompatible with earlier versions, so that data is lost. The department wants to develop a policy for new third party vendors, and review the liability clauses in current existing contracts.</td></tr><tr><td>Malfunction of software or hardware</td><td>Sometimes software bugs or malfunctioning hardware may cause severe damage to running applications. The department wants to improve its software testing capabilities to better detect possible software errors. The departments also wants to test and implement several new technologies for switching to another server when critical network or file servers crash because of hardware failures.</td></tr><tr><td>Computer worm or virus</td><td>Computer worms or viruses are unavoidable, and in most cases are stopped at the gates of the university network. However, some viruses still manage to penetrate the network and wreck hammock among all users. A critical weakness appears to be caused by wireless network users and file sharing programs. The department wants to develop a policy to better protect wireless network users, and better detect illegal file sharing on the university network.</td></tr></table>

H1. Groups that use FURIA will evaluate their group decision process more positively than groups that did not use the DSS.

Group polarization can be observed as a majority shifts towards extreme information to support their views [27,28]. We postulate here that FURIA should reduce group polarization and group members use less extreme scores in their assessment of the risks:

H2. Groups that did use FURIA will be less subject to polarization as they rate the threats using less extreme scores than groups that did not use FURIA.

## 5.2.2. Experimental design and procedure

In total 34 participants were involved in this pilot experimental evaluation, all of whom were masters students in Information Systems and Management at Tilburg University. The participants were randomly attributed to a small group with group size between 4 and 6, and consequently distributed across the two experimental conditions ‘use of FURIA’ (n = 16) vs. ‘no use of FURIA’ (n = 18). All participants were provided with the task instructions and list of threats as indicated above, and were asked to rate these threats on the three criteria of scope, likelihood and impact. These ratings were consequently collected by the experimenters.

In the experimental condition ‘use of FURIA’, the individual scores of the participants were used as input to FURIA to compute a visual representation of the individual members' positions by means of the Hasse diagrams, as illustrated in the FURIA screen shot shown in Fig. 5. Node numbers in this figure correspond to group member IDs assigned to the participants during the experiment.

These visual representations were shown and explained to every individual member of the group by the experimenters. After that, all participants were instructed to join their group and reach an agreement on the two threats that should be recommended to the university. In the control condition ‘no use of FURIA’, the participants were instructed to join their group without any additional information, and similarly asked to reach an agreement on the two risks that should be recommended to the university. In either condition, the groups had up to 30 min to reach a decision.

Following this experimental task, the participant received a new sheet on which they were asked to rate all threats again on the same three criteria of scope, likelihood and impact. They were also given a post-test questionnaire intended to measure the perceived quality of the group decision-making as well as the individual satisfaction and level of agreement observed in the group.

## 5.3. Results: risk perception analysis and quality of decision-making (pre-test and post-test)

5.3.1. Effect of the use of FURIA on the evaluation of the group decision process

Cronbach's [8] α coefficient was used as an index of internal consistency to validate each instrument. All coefficients did exceed the threshold of 0.6 and are therefore considered as being reliable for our research purposes [32]. They indicated a correct internal consistency reliability of the constructs and scales: pre-test $\left( \alpha { = } 0 . 6 4 3 \right)$ , post-test $( \alpha { = } 0 . 6 8 6 )$ , pre-test/post-test for each of the 21 items (ranged from 0.57 to 0.96), quality of decision-making/consensus (α = 0.716).

The results of the factorial analysis in principal components (rotation method varimax Kaiser normalization) ran on the items (k = 5) extracted two factors. The first one explained 43.9% of the variance and relates to efficiency $( r { = } 0 . 7 5 )$ , transparency $( r { = } 0 . 8 3 8 )$ and satisfaction $( r { = } 0 . 7 6 9 )$ of the decision-making process, while the second factor explained 27.9% of the variance and relate to coordination $( r { = } 0 . 8 1 2 )$ and fairness $\left( r { = } 0 . 8 9 6 \right)$ of the decision-making process. The respective Bartlett factor scores of analysis have been computed and respectively denominated ETS and CF.

The results of the ANOVA conducted on the pre-test on the evaluation of the threats at the individual level revealed no significant effect. In the pre-test, the experimental groups that provided the information shown by FURIA rated the risks on the three criteria of impact, likelihood and scope in a similar way as the experimental groups that did not benefit of the use of FURIA. This draws an interesting baseline that demonstrates that, prior to the group decision task and the experimental manipulation, the groups did not already have a significantly different perspective on the threats.

The scores to the post-test on the evaluation questionnaire relative to the decision-making process were aggregated in groups. The results of the Mann–Whitney test revealed that the groups who benefit of the use of FURIA evaluated the quality of the group decision-making to be significantly more coordinated and fair on the Bartlett regression score $\scriptstyle ( p = 0 . 0 5 )$ than the groups who did not use the DSS. Overall, the groups that use the DSS also report more satisfaction $( p \mathrm { = } 0 . 0 5 )$ and showed more agreement with the group solution $\scriptstyle ( p = 0 . 0 5 )$ than the groups that did not benefit of FURIA. However, the efficiency was not rated differently in both groups.

![](/api/attachments/E7J3PX3C/fulltext/images/6ed31f32ca6c789990bcd3df3a0646f225c916758a3b11ccfd755fa39d97a83d.jpg)  
Fig. 5. FURIA screen with visual representation of group member preferences.

Table 5 presents the means rank generated with the Mann–Whitney test aggregated in group according to a 2 between-subject design: ‘use of FURIA’ versus ‘no use of FURIA’.

The results allow us to conclude that groups using FURIA to assess the threats came to a different decision than groups who did not benefit of the support of FURIA. The second set of results allow us to conclude that groups using FURIA to assess the threats perceived the quality of the decision-making to be better than groups that did not benefit of the support of FURIA. Also, the results indicate that groups that use FURIA expressed a greater satisfaction in the process of decision-making and perceived the decision to be more consensual and showed more agreement with the group solution than groups that did not use the DSS (H1).

## 5.3.2. Effect of the use of FURIA on the polarization effect and threat rigidity

The results of the ANOVA on the post-test revealed that after the use of FURIA the experimental and the control groups differ significantly in their assessment on the ‘impact’ criterion for the threats “sabotage of equipment” and “computer worm or virus” (0.0001b pb 0.04). Of interest, the results indicated that the groups that did not use the DSS score significantly higher on these particular threats. The means and standard deviation for the assessment on the criterion ‘impact’ for these threats are given in Table 6.

Table 5  
Means rank aggregated in groups

<table><tr><td>Construct</td><td>No use of FURIA (n=3)</td><td>Use of FURIA (n=3)</td></tr><tr><td>Efficiency</td><td>2.33</td><td>4.67</td></tr><tr><td>Coordination *</td><td>2</td><td>5</td></tr><tr><td>Fairness</td><td>2.67</td><td>4.33</td></tr><tr><td>Transparency</td><td>2.66</td><td>4.25</td></tr><tr><td>Satisfaction *</td><td>2</td><td>5</td></tr><tr><td>Consensus **</td><td>2.17</td><td>4.83</td></tr><tr><td>Agreement *</td><td>2</td><td>5</td></tr></table>

\*pb0.05.  
\*\*pb0.08.

Means and standard deviation for the risks sabotage and worm: polarization effects

<table><tr><td></td><td>N</td><td></td><td>Sabotage impacta</td><td>Worm impactb</td></tr><tr><td rowspan="2">No use of FURIA</td><td rowspan="2">18</td><td>M</td><td>6.72</td><td>8.16</td></tr><tr><td>S.D.</td><td>1.6</td><td>1.24</td></tr><tr><td rowspan="2">Use of FURIA</td><td rowspan="2">16</td><td>M</td><td>5.68</td><td>6.7</td></tr><tr><td>S.D.</td><td>1.1</td><td>1.8</td></tr></table>

<sup>a</sup> F(1,33)= 4.603, p= 0.04.  
<sup>b</sup> F(1,33) = 6,843, p= 0.013.

This result may lead us to conclude only that groups who used FURIA were less prone to extreme scoring for these two threats on the ‘impact’ criterion than groups that did not use FURIA, and therefore the use of FURIA seems to reduce the polarization within these groups (H2). We however cannot generalize this result to the overall assessment on all criteria for all threats: no significant differences have been found for the other threats, only a similar pattern can be identified. Therefore, H2 is only partially supported.

Finally, we note that all groups who did not use FURIA selected the ‘worm and computer virus’ threat as the top threat – this seems to be an understandable yet rather straightforward choice. However, the groups who used FURIA displayed more diversity in their top threat choices: in addition to one group choosing ‘worm and computer virus’, the other groups chose ‘fire’ and ‘malfunction of software or hardware’ as their top threat, respectively. This finding hints at a reduced threat rigidity effect within these groups.

## 6. Conclusions, limitations and future research

IT Service Continuity today is a major concern for organizations as business processes increasingly depend on IT. Even the smallest of IT service disruptions may cause costly delays; longer outages may lead to significant market share loss or even the demise of the organization. Despite general agreement on the seriousness of these consequences, it is not always evident to an organization what the major threats to its IT Service Continuity process really are. For any stakeholders group involved in assessing these threats, members of the group are likely to express different preferences on the impact, scope and likelihood of the threats [39].

The challenge therefore is to avoid that the group reverts to defective group decision-making, but rather acknowledges the individual members' relative preference positions to achieve a better and more consensual group decision. The fuzzy decision support system FURIA we have presented in this paper has been designed to achieve exactly that objective, by providing individual members of a stakeholders group with a visual representation of his or her preferences and their relationships with the preferences of the other group members, using a fuzzy relational analysis technique. The results of an exploratory experimental evaluation of FURIA for an ITSC case at a university indicate that groups using FURIA causes groups to be more satisfied with the decision process, and to show more agreement with the group decision. In addition, the groups using FURIA are found to be less extreme in their assessment of two threats on one of the decision criteria. Therefore, we may conclude that the results indicate that the prototype performs to expectations.

This research has, obviously, some important limitations. Although the outcome of our pilot experimental evaluation is positive, a more elaborate experimental setting is needed to fully justify the validity of our claims. While the students in our experiment are indeed a ‘valid’ stakeholders group (and indeed formally acknowledged in this role by the university), other stakeholder groups should be included in a full study, such as university management, faculty and the IT Services department as the most obvious candidates. In a follow-up study, we will address these stakeholder groups and analyze the performance of FURIA in this extended setting.

## Acknowledgments

The authors are grateful to three anonymous referees for their insightful remarks, which considerably helped clarify this paper. The support of Jan Pol, Erik Goessens MSc and Johannes van den Bosch MSc in assisting with an ITSC case study in a large international consumer electronics company is acknowledged, as well as the technical assistance of Dr. Veerle Van der Sluys in the development of the FURIA prototype. The first author acknowledges partial funding support by the European Commission through an FP6 Marie Curie Intra-European Fellowship.

## References

[1] Australian Department of Commerce, Office of Information and Communication Technology, Return on Investment for Information Security Guideline, September 2003 version 1.0.

[2] B.M. Ayyub, Risk Analysis in Engineering and Economics, First edition, Chapman & Hall, 2003.

[3] W. Bandler, L.J. Kohout, Fuzzy relational products as a tool for analysis and synthesis of the behavior of complex natural and artificial systems, in: S.K. Wang, P.P. Wang (Eds.), Fuzzy Sets: Theory and Application to Policy Analysis and Information Systems, Plenum Press, New York, 1980, pp. 341–367.

[4] S. Belardo, J. Harrald, A framework for the application of decision support systems to the problem of planning for catastrophic events, IEEE Transactions on Engineering Management 39 (4) (1992) 400–411.

[5] B. Berger, Data-Centric Quantitative Computer Security Risk Assessment, SANS Institute, GSEC Practical Version 1.4b, 2003.

[6] J.P. Brans, Ph. Vincke, A preference ranking organization meth od, Management Science 31 (6) (1985) 647–656.

[7] Business Continuity Institute, Business Continuity Management– Good Practice Guide, Version BCI DJS 1.0, September 2002.

[8] L.J. Cronbach, Coefficient alpha and the internal structure of tests, Psychometrika 16 (1950) 297–334.

[9] B. De Baets, H. De Meyer, H. Naessens, On rational cardinalitybased inclusion measures, Fuzzy Sets and Systems 128 (2002) 169–183.

[10] B. De Baets, H. De Meyer, Transitive approximation of fuzzy relations by alternating closures and openings, Soft Computing 7 (2003) 210–219.

[11] A.R. Dennis, J. Nunamaker Jr., D.R. Vogel, A comparison of laboratory and field research in the study of electronic meetings systems, Journal of Management Information Systems 7 (2) (1991) 107–135.

[12] W.G. De Ru, J.H.P. Eloff, Risk analysis modeling with the use of fuzzy logic, Computer Security 15 (3) (1996) 239–248.

[13] G. DeSanctis, R.G. Gallupe, A foundation for the study of group decision support system, Management Science 33 (1987) 589–609.

[14] M. Devarges, Survival is not compulsory: an introduction to business continuity planning, Computers & Security 18 (1999) 35–46.

[15] S. Drew, Reducing enterprise risk with effective threat management, Information Security Management, 2005, pp. 37–42, Jan uary/February Issue.

[16] D. Dubois, H. Prade, Fuzzy Sets and Systems: Theory and Ap plications, Academic Press, New York, 1980.

[17] C. Eden, F. Ackermann, Making Strategy: The Journey of Strategic Management, Sage Publications, London, 1998.

[18] L. Festinger, A theory of social comparison processes, Human Relations 7 (1954) 117–140.

[19] J. Fodor, M. Roubens, Fuzzy Preference Modeling and Multi criteria Decision Support, Kluwer Academic, Dordrecht, 1994.

[20] S.R. Hiltz, M. Turoff, The Network Nation, Revised Edition, MIT Press, Boston, 1993.

[21] C. Huang, Fuzzy risk assessment of urban natural hazards, Fuzzy Sets and Systems 83 (2) (1996) 271–282.

[22] ITIL Service Support Handbook, Office of Government Commerce, UK, 2000.

[23] I.L. Janis, Groupthink: Psychological Studies of Policy Decisions and Fiascoes, Houghton-Mifflin, Boston, 1982.

[24] L.M. Jessup, J.S. Valacich, Group Support Systems: New Perspectives, MacMillan, New York, 1993.

[25] M. Keil, A. Tiwana, A. Bush, Reconciling user and project manager perceptions of IT project risk: a Delphi study, Information Systems Journal 12 (2002) 103–119.

[26] G. King III, Crisis management and team effectiveness: a closer examination, Journal of Business Ethics 41 (3) (December 2002) 235–249.

[27] C. Lord, L. Ross, M. Lepper, Biased assimilation and attitude of prior theories on subsequently considered evidence, Journal of Personality and Social Psychology 37 (1979) 2098–2109.

[28] S. Moscovici, M. Zavalloni, The group as a polarizer of attitudes, Journal of Personality and Social Psychology 12 (1969) 125–135.

[29] E.W.T. Ngai, F.K.T. Wat, Fuzzy decision support system for risk analysis in e-commerce development, Decision Support Systems 40 (2) (2005) 235–255.

[30] J.D. Nosworthy, A practical risk analysis approach: managing BCM risk, Computers & Security 19 (2000) 596–614.

[31] J. Nunamaker, D.R. Vogel, B. Konsynsky, Interaction of task and technology to support large groups, Decision Support Systems 9 (5) (1989) 139–152.

[32] J. Nunnaly, Psychometric Theory, McGraw-Hill, New York, 1978.

[33] R.K.J.R. Rainer, C.A. Snyder, H.H. Carr, Risk analysis for information technology, Journal of Management Information Systems 8 (1) (1991) 129–147.

[34] B.A. Reinig, B. Shin, The dynamic effects of group support systems on group meetings, Journal of Management Information Systems 19 (2) (2002) 303–325.

[35] R.E. Rice, From adversity to diversity: applications of communication technology to crisis management, Advances in Telecommunications Management 3 (1990) 91–112.

[36] J. Rijsman, M. Poppe, Power difference between players and level of matrix as determinants of competition in a MDG, European Journal of Social Psychology 7 (3) (1977) 347–367.

[37] M. Roubens, Ph. Vincke, Preference Modeling, Lecture Notes in Economics and Mathematical Systems, vol. 250, Springer, Berlin, 1985.

[38] B. Roy, Decision-aid and decision-making, European Journal of Operational Research 45 (1990) 324–331.

[39] A.-F. Rutkowski, B. Van de Walle, W. van Groenendaal, J. Pol, When stakeholders perceive threats and risks differently: the use of group support systems to develop a common understanding and a shared response, Journal of Homeland Security and Emergency Management 2 (1) (2005).

[40] A.-F. Rutkowski, B. Van de Walle, G. Van Den Eede, The effect of group support systems on the emergence of unique information in a risk management process: a field study, to appear in Proceedings of the 39th Hawaii Conference on Systems Sciences, 2006.

[41] J.E. Spillan, M. Hough, Crisis planning in small businesses: importance, impetus and indifference, European Management Journal 21 (3) (2003) 389–407.

[42] B. Staw, I. Sandelands, J. Dutton, Threat-rigidity effects in organizational behavior: a multilevel analysis, Administrative Science Quarterly 26 (1981) 501–524.

[43] G. Stoneburner, A. Goguen, A. Feringa, Risk Management Guide for Information Technology Systems, Recommendations of the National Institute of Standards and Technology, National Institute of Standards and Technology, Technology Administration, U.S. Department of Commerce, NIST Special Publication 800-30, October 2001.

[44] M. Turoff, M. Chumer, B. Van de Walle, X. Yao, The design of a dynamic emergency response management information system, Journal of Information Technology Theory and Applications 5 (4) (2004) 1–36.

[45] B. Van de Walle, A relational analysis of decision makers' preferences, International Journal of Intelligent Systems (Special Issue on Preference Modeling) 18 (2003) 775–791.

[46] B. Van de Walle, B. De Baets, E.E. Kerre, Fuzzy multi-criteria analysis of cutting techniques in a nuclear reactor dismantling project, Fuzzy Sets and Systems 74 (1995) 115–126.

[47] B. Van de Walle, B. De Baets, E.E. Kerre, Characterizable fuzzy preference structures, Annals of Operations Research (Special Issue on Preference Modelling) 80 (1998) 105–136.

[48] Ph. Vincke, Basic concepts of preference modeling, in: Carlos Bana e Costa (Ed.), Readings on Multiple-Criteria Decision Aid, Springer-Verlag, 1990, pp. 101–118.

[49] S. Weiner, Managing effective disaster recovery, The CPA Journal (December 2001) 22–26.

[50] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338–353.

![](/api/attachments/E7J3PX3C/fulltext/images/848f89ea64c3832c877afa003cead3feb7e31384363623dafe0fbbc107def5aa.jpg)

Bartel Van de Walle is Assistant Professor at Tilburg University (the Netherlands) and visiting Research Assistant Professor at the New Jersey Institute of Technology (USA). He received his MS and his PhD in Applied Mathematics and Computer Science from Ghent University (Belgium). His dissertation research was on fuzzy preference modeling and multi-criteria decision analysis, two areas which are still at the basis of his current research on information systems for crisis man-

agement and response (ISCRAM). He is co-founder of the international ISCRAM Community at iscram.org and has organized two conferences in this area. Bartel is serving on the board of the Journal of Information Technology Theory and Applications (JITTA) as a Senior Editor and is on the Editorial Board of the Journal of Homeland Security and Emergency Management. Bartel has been awarded a Marie Curie Intra-European Fellowship for his research on decision support for crisis response teams.

![](/api/attachments/E7J3PX3C/fulltext/images/cd7f125528ba934425313fd2e1d8edd158bab3b5d98b753e5ad31d0e434aca6f.jpg)

Anne-Francoise Rutkowski is Assistant Professor of Information Systems at Tilburg University (the Netherlands). She received her PhD in Cognitive and Social Psychology at Tilburg University in 1999. Since 1994, she has been involved in education and research activities in fundamental psychology (i.e., cognitive dissonance, causal attribution processes, post-modernist theories, fuzzy logic and processes of leadership and negotiation; method of research in human sciences).

Since 1999, her research interests and publications are oriented toward GSS and bridge IS and human sciences in addressing topics such as group decision-making, problem solving, virtual and multi-national
