---
otero_id: 10178
otero_key: "U3SDPBP6"
title: "Evaluating information assurance strategies"
authors: "J.Todd Hamill; Richard F. Deckro; Jack M. Kloeber"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.11.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Evaluating information assurance strategies<sup>\$</sup>

J. Todd Hamill\*, Richard F. Deckro, Jack M. Kloeber Jr.

Department of Operational Sciences, Air Force Institute of Technology, USA

Received 1 December 2000; accepted 1 November 2003 Available online 22 April 2004

## Abstract

The information revolution has provided new and improved capabilities to rapidly disseminate and employ information in decision-making. Enhancing and enabling for today’s modern industry, these capabilities are critical to our national infrastructures. These capabilities, however, often rely upon systems interconnected throughout the world, resulting in potentially increased vulnerability to attack and compromise of data by globally dispersed threats.

This paper develops a methodology facilitating the generation of information assurance strategies and implementing measures to assess them. Upon reviewing key factors and features of information assurance, value focused thinking is used to develop an information assurance analysis framework. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Information assurance; Information technology; Computer security; Decision analysis

## 1. Introduction

The tremendous worldwide increase in reliance upon information technologies (IT) reaps huge benefits for their users but also threatens significant drawbacks. These technologies afford decision-makers with the capability to quickly fuse data from multiple sources, make informed decisions, and disseminate those decisions at nearly the speed of light. IT capabilities have become essential for day-to-day operations in today’s global economy.

The Advanced Research Projects Agency Network (ARPANET) evolved into today’s Internet. However, the ‘‘ARPANET protocols. . .were originally designed for openness and flexibility, not for security’’ [20]. The initial approach that permitted ‘‘unrestricted insiders’’ to easily share information is no longer appropriate for today’s commercial and government use [20]. While the Internet now effectively spans the entire globe, organizations often deal with the subsequent vulnerabilities that develop on an after-the-fact basis, or worse, not at all.

Internet and internal threats employ widely available tools and easily obtainable technology to seek out and capitalize upon IT vulnerabilities. The President’s Commission on Critical Infrastructure Protection (PCCIP) addressed these vulnerabilities on a national scale by identifying five sectors of industry that share common characteristics. In particular, the Commission highlighted the interconnectedness of these key sectors and their heavy reliance upon information technology. The five sectors include:

1. Information and Communications

2. Banking and Finance

3. Energy (Including Electrical Power, Oil and Gas)

4. Physical Distribution

5. Vital Human Services [24:2]

Information systems now monitor and control many of the operations of various other infrastructures. These systems are often an ad hoc mixture of components, processes and software, which were not often designed to inter-operate in a secure fashion. The resulting interdependencies and relatively easy access for a number of threats puts all sectors at risk.

The increasing need for Information Assurance (IA) of government, commercial and individual information systems stems from the growing number of threats with their increasing capabilities to inflict damage upon information systems. Those techniques that provided an advantage in the past now pose a threat to not only our national infrastructure, but to industry’s current and future capabilities.

Fig. 1 illustrates the increasing trend in incidents handled by the Computer Emergency Response Team (CERT). Noting the fact that these incidents are only those that were detected and reported implies that a much larger number of attacks may have actually occurred. Military exercises like ‘‘Eligible Receiver’’ have demonstrated, with relative ease, hackers’ ability to ‘‘cripple U.S. military and civilian computer networks. . .’’ [12]. The Melissa virus and the ‘‘Love Bug’’ further reveal the potential threat to an organization’s information infrastructure. The increasing trends in cyber assaults show that IA is, and will continue to be, a vital corporate strategy. As time and technology continue to advance, maintaining normal day-to-day operations and capability at any given moment will hinge on the continuous development, implementation and improvement of the level of IA.

To provide information assurance, the level of assurance attained must often be balanced with potential reductions in operational capability and the consumption of valuable resources (e.g. time, money and people). This paper develops a decision support tool to facilitate a three-dimensional, quantitative tradeoff analysis between the level of IA gained by a collection of capabilities, the resulting effect on operational capability, and the resources required for their implementation.

![](/api/attachments/U3SDPBP6/fulltext/images/aa9eddf9f0d58874fa3e6da14757d346a118c3a1a71c14623dbbb65860293f63.jpg)  
Fig. 1. Security incidents [4].

## 2. Background

There exists a large collection of documents dealing with what IA should be, methods on achieving assurance, and suggested strategies (‘defense-in-depth’ for example). The principles of IA presented here draw heavily from DoD and government related agencies’ documents. These principles can, and have been, extended to the private sector, it should not be assumed, however, that the DoD is the sole source of Information Assurance literature. A wealth of information regarding IA strategies and measures can be found through the National INFOSEC Education and Training Program webpage (http:// www.nsa.gov/isso/programs/nietp/newspg1.htm). This page links to the web pages of over 20 academic institutions that have qualified as Centers of Academic Excellence for Information Assurance. Each of these pages is a trove of past and on going work in Information Assurance. While all of these sites are valuable, the Center for Education and Research in Information Assurance and Security, (CERIAS) at Purdue University (http://www.cerias. purdue.edu/) and the CERT http://www.cert.org/) and the Center of Academic Excellence in Information Assurance Education (http://www.heinz.cmu.edu/ infosecurity/) at Carnegie Mellon University are excellent starting points. Although a wide array of academic, industrial, and government literature was reviewed for this study, we have restricted the literature reviewed in this paper to those that were directly used in the development of the model for the sponsor, DARPA.

From the DoD perspective, JP 3-13, entitled Joint Doctrine for Information Operations, discusses both offensive and defensive information operations (IO), stating both are equally important to ensure successful military operations. JP 3-13 offers the following, widely accepted, definition of IA.

IA protects and defends information and information systems by ensuring their availability, integrity, identification and authentication, confidentiality, and non-repudiation. This includes providing for the restoration of information systems by incorporating protection, detection, and reaction capabilities. IA employs technologies and processes such as multilevel security, access controls, secure network servers, and intrusion detection software. [6:III-1]

Restated, IA ensures that information and information systems are available to decision-makers when needed, that the information is as accurate and complete as possible, and that control over both the information and the information systems is maintained. In the event that control is lost, the capabilities to detect a loss of control, to regain control, and to restore the information systems to its original state must exist. These objectives are achieved by taking proactive measures (to protect) and allowing for detection and reaction capabilities (to defend) through the integration of secure technologies and best practices into the information system. Specific definitions of these IA requirements are shown in Table 1.

The objectives of IA include information environment protection, attack detection, capability restoration, and IO attack response [6:ix]. Table 2 describes the elements that comprise the information realm.

Information assurance encompasses defensive IO in the context that systems are under continuous scrutiny by varying levels of threats. Although the concepts of defensive IO and IA are similar, the definition of IA is used in this study to develop a hierarchy of main objectives. These objectives, defined in Table 3, include Information and Information System (IS) Protection, Detection, and Reaction capabilities.

Alberts clarifies areas of defensive operations within Information Warfare (IW), an approach closely

Table 1

Definitions of IA objectives

<table><tr><td colspan="2">Definitions of IA objectives</td></tr><tr><td>Availability</td><td>Assured access by authorized users [6].</td></tr><tr><td>Integrity</td><td>Protection from unauthorized change [6].</td></tr><tr><td>Identification</td><td>Process an information system uses to recognize an entity [9].</td></tr><tr><td>Authentication</td><td>Verification of the originator; Security measure designed to establish the validity of a transmission, message, or originator, or a means of verifying an individual&#x27;s authorization to receive specific categories of information [9].</td></tr><tr><td>Confidentiality</td><td>Protection from unauthorized disclosure [6].</td></tr><tr><td>Non-repudiation</td><td>Undeniable proof of participation [6].</td></tr></table>

Table 2

<table><tr><td>Elements of the information realm [6:I-9–11,10]</td></tr><tr><td>Information</td></tr><tr><td>Facts, data, or instructions in any medium or form. This includes the meaning that humans assign to data by means of known conventions used in their representation.</td></tr><tr><td>Information-Based Processes</td></tr><tr><td>Processes that collect, analyze, and disseminate information using any medium or form, that adds value to the decision making process by performing designated functions or provide anticipated services.</td></tr><tr><td>Information System</td></tr><tr><td>The entire infrastructure, organization, personnel, and components that collect, process, store, transmit, display, disseminate, and act on information. The information system also includes information-based processes.</td></tr></table>

related to tackling the problem of IA. This approach formulates the defensive IW problem as

. . .the possible environments that may be faced, one’s options, and the objective that is being sought. This requires an identification of the variables that are relevant, that is, those that can significantly influence the outcome as well as the subset of these relevant variables that are controllable, which form the basis of designing options. [1:19]

Alberts noted five challenges to defensive information warfare capabilities that remain strong today. These included:

 a better understanding of the nature of the threat must be achieved;

 a deterrent strategy against digital attacks must be developed;

 timely notification of indicators and warning regarding impending attacks;

 methods for successfully defending against attacks that do occur; and

 the development of ‘‘appropriate and effective responses to attacks’’ [1:59 – 62].

A number of models and methodologies have been developed to find a solution to this problem. Two models, one with a DoD focus, the other with a commercial enterprise focus, are described below.

The minimum essential information infrastructure (MEII) is defined as a process, rather than a structure [2]. A methodology to attain a feasible MEII is proposed, and the concept is described by the following four principles. The MEII. . .

 does not guarantee security but is instead a type of information system insurance policy by which risks are managed at some reasonable cost while pursuing information age opportunities;

 is not a central system responding to multiple threats but a set of systems defined locally to respond to local vulnerabilities;

 is not a fixed, protected entity, but a virtual functionality on top of the existing infrastructure; and

 is not a static structure, but a dynamic process—a means to protect something, instead of a thing that has to be protected. [2:xiv]

The focus is on military organizations, and it is assumed that as more organizations complete this process, an MEII will evolve, thus securing the defense information infrastructure (DII). This is in agreement with the ‘weakest link’ approach to security in general.

The process Anderson et al define has six steps, shown in Table 4.

The overall process is similar to other risk reduction or risk assessment processes. Categories of security techniques, shown in Table 5, may illustrate desirable attributes of an information system in the context of information assurance.

The Accreditor’s Guideline, written by the National Computer Security Center (NCSC), provides guidance on the certification and accreditation process

## Table 3

IA objective definitions

Table 4  
Six steps of the MEII process [2:xiv – xv]

<table><tr><td colspan="2">Six steps of the MEII process [2:xiv–xv]</td></tr><tr><td>1</td><td>Determine what information functions are essential to successful execution of the unit&#x27;s missions.</td></tr><tr><td>2</td><td>Determine which information “systems” are essential to accomplish those functions.</td></tr><tr><td>3</td><td>For each essential system and its components, identify vulnerabilities to expected threats. In analyzing the system, it could (and perhaps should) be viewed in various ways: as a hierarchical set of subsystems supporting each other at different levels, or as a collection of functional elements like databases, software modules, hardware, etc.</td></tr><tr><td>4</td><td>Identify security techniques to mitigate vulnerabilities.</td></tr><tr><td>5</td><td>Implement the selected security techniques.</td></tr><tr><td>6</td><td>Play the solutions against a set of threat scenarios to see if the solutions are robust against likely threats. It is critical that the success of security enhancements be testable.</td></tr></table>

required for DoD information systems. Within this document, the risk management process is described. Risk is ‘‘something bad that might, or might not, actually come to pass’’ [19:136].

The notion of risk avoidance—‘‘the view that all risks to the information of an information system or network ought to be removed entirely before that system was allowed to operate’’—was once supported by security professionals [22:3-1]. Eventually, it was recognized that some level of risk will always remain, and therefore, tradeoffs between security and functionality must be made [22:3-2]. The current process of risk management approximates the current level of risk within a given system, and relies upon rational decision making to determine if it is at an acceptable level. An overall objective is to facilitate the costeffective placement of countermeasures to mitigate the identified risks.

The limited availability of resources, particularly money, is the most common problem in trying to establish IA when fiscal benefits are not readily available or obvious.

Complex and expensive systems frequently involve lengthy approval cycles and prove to be more difficult in evaluating the benefits of such investments. [21:2]

Materna examined the evaluation processes of ‘‘next generation Information Technology investments. . .’’ and found that a variety of measures existed, but few ascertained the contributions that the investment made to the ‘‘business needs of the firm, however they are defined’’ [21:2].

Table 5  
MEII security technique categories [2:xvii]

<table><tr><td>Heterogeneity</td><td>May be functional (multiple methods for accomplishing an end), anatomic (having a mix of component or platform types), and temporal (employing means to ensure future admixture or ongoing diversity).</td></tr><tr><td>Static resource allocation</td><td>The a priori assignment of resources preferentially, as a result of experience and/or perceived threats, with the goal of precluding damage.</td></tr><tr><td>Dynamic resource allocation</td><td>According some assets or activities greater importance as a threat develops; this technique calls for directed, real-time adaptation to adverse conditions.</td></tr><tr><td>Redundancy</td><td>Maintaining a depth of spare components or duplicated information to replace damaged or compromised assets.</td></tr><tr><td>Resilience and robustness</td><td>Sheer toughness; remaining serviceable while under attack, while defending, and/or when damaged.</td></tr><tr><td>Rapid recovery reconstitution</td><td>Quickly assessing and repairing damaged or degraded components, communications, and transportation routes.</td></tr><tr><td>Deception</td><td>Artifice aimed at inducing enemy behaviors that may be exploited.</td></tr><tr><td>Segmentation, decentralization, and quarantine</td><td>Distributing assets to facilitate independent defense and repair; containing damage locally and preventing propagation of the damaging vector.</td></tr><tr><td>Immunologic identification</td><td>Ability to discriminate between self and non-self; partial matching algorithms (flexible detection); memory and learning; continuous and ubiquitous function.</td></tr><tr><td>Self-organized and collective behavior</td><td>Valuable defensive properties emerging from a collection of autonomous agents interacting in a distributed fashion.</td></tr><tr><td>Personnel management</td><td>Personnel security clearances and training, design of human interfaces to reduce vulnerability of systems to human frailties.</td></tr><tr><td>Centralized management of information resources</td><td>(Self explanatory)</td></tr><tr><td>Threat/warning response structure</td><td>Establishment of a hierarchy of increasing information attack threat levels and concomitant protective measures to be taken.</td></tr></table>

Two types of benefits, ‘‘Hard’’ and ‘‘Soft,’’ are discussed and differentiated. Hard benefits ‘‘refer to those benefits that can be readily quantified using standard measurement techniques,’’ which includes dollars saved or generated, as well as time saved [21:3]. Soft benefits ‘‘refer to those benefits which are often less obvious or difficult to quantify such as worker empowerment, flexibility, or the multifarious aspects of competitive advantage’’ [21:3]. These are also referred to as financial and operational benefits, respectively.

Three general approaches to measuring these benefits of IT investments are discussed by Materna: Economic, Cost Reduction, and Strategic. Economic approaches include such analyses as Net Present Value, Internal Rate-of-Return, Return on Investment, and Breakeven/Payback. Unfortunately, these lend themselves to financially oriented assessments of stand-alone systems, but pose significant weaknesses when applied to interdependent systems that may involve intangible costs or benefits [21:4]. Without valid measures of IA benefits, classic financial analysis is difficult. What is ‘‘fire protection’’ worth to day-today operations when there is no apparent threat? What is that same protection worth when one is surrounded by arsonists?

The cost reduction approaches discussed include cost displacement/avoidance, work value analysis, and the cost of quality. Cost displacement (or cost avoidance) compares ‘‘the cost of the proposed system to the cost it will displace and avoid’’ [21:4]. Technical importance evaluates potential investments by their ability to support the achievement of longterm objectives. Although there may be no return on the investment, future operations may be impossible without it [21:7 – 8]. Clearly, the level of assurance must be balanced against the operational and fiscal costs of that assurance.

Considering the context of this research, employment of the latter, commercially oriented model did not suit the purposes of DoD and the ultimate interests of National Security. There are, however, valuable lessons learned with regards to measuring certain aspects of an information system’s value, and the potential comparison of IA alternatives given subsequent changes in architecture. The former methodology lends itself to a potentially thorough evaluation of a given IS and its associated functions and consequential vulnerabilities. It is hypothesized, however, that in order to limit the resources spent in implementation, the MEII process will require a means to focus on the trades between IA and its resulting costs in the fiscal and operational sense.

## 3. Value focused thinking

## 3.1. Introduction

Operations research is intended to improve decision making; and values, indicating what one wants to achieve, are essential for guiding decision making [16:793]. Values are what we fundamentally care about in decision-making. Alternatives are simply means to achieve our values [16:793]. Keeney defines the typical approach used by most organizations as ‘‘alternative-focused thinking’’—attacking the problem by evaluating the alternatives available and then choosing the best one [17:4].

How to achieve an acceptable level of IA, with a minimum operational impact, at a reasonable cost is the decision opportunity addressed in this research. A focus on values aids in the evaluation of such complex decisions. Even in the alternative-focused approach, the effort of choosing an alternative involves evaluating each alternative based on the underlying values of the decision maker(s). Because we believe a focus on values rather than alternatives is the more correct way to attack such a complex and important issue, we have based the methodology in this study on VFT.

## 3.2. Overview of value model development

A value model is a hierarchical collection of a set of fundamental objectives applicable to the decision problem. These objectives are broken down until they can be measured, allowing the decision-maker (DM) to quantitatively assess the degree to which the objectives are met. Several authors and analysts have proposed desirable properties of objectives contained within a fundamental objectives hierarchy including [3,17 –19]. Keeney’s desirable properties are extensive and include the following: essential, controllable, complete, measurable, operational, decomposable, non-redundant, concise, and understandable [17:82]. Although each of the authors named above submits different lists of desirable properties, they all include, in essence, the three properties we used for our study—complete, non-redundant, and operational.

The top tier of the fundamental objectives hierarchy includes only top-level objectives. The lower level tiers break each of the fundamental objectives down into sub-objectives. This process is called specification. Specification allows the organization to be more specific about what is meant by the fundamental objectives and ties the objective more closely to the achievement of the alternatives in the objectives’ areas. Specification continues until the achievement of each objective is adequately measured through evaluation measures that are complete, non-redundant, and operational.

## 3.3. Measuring the attainment of objectives

In order to assess how well an alternative does, or does not, meet a decision-maker’s objectives, an evaluation measure is developed for each lowest level objective. Each measure has characteristics that make it an appropriate and effective measure. The measure will be expressed in units that are either natural or constructed units and will be either a direct or proxy measure of the attainment of the objective being quantified. The most preferred evaluation measure is a natural-direct measure which is generally the least controversial and most transparent; whereas, a constructed-proxy measure is least preferred and must be more carefully and explicitly described to be useful in scoring the attainment of a particular objective. An indepth discussion of types and characteristics of measures can be found in [19:24].

Once the measures are developed, the ranges of evaluation for each measure are declared and single dimension value functions are built to reflect the appropriate returns-to-scale.

## 3.4. Building single dimension value functions

A single dimension value function is a monotonic (increasing or decreasing) function that captures the value a particular score represents to the DM. We will use the notation $\nu _ { i } ( x _ { i } )$ to indicate the value function for the ith evaluation measure. A particular $\nu _ { i } ( x _ { i } )$ may be discrete, piecewise linear, or continuous, as shown in Fig. 2.

The degree to which the DM prefers a higher score to a lower score level, termed a value increment, is elicited from the DM to build the value functions. However, the infinite number of scores on a continuous function may require an approximation of the functional form. A piecewise-linear function is one form of approximation we have used as well as the simple exponential function and the S-shaped sigmoid function. Methods and example interviews for constructing value functions, can be found in Ref. [19].

Single dimension value functions, allowing consistent returns-to-scale of the real world units identified in the evaluation measures, are developed for all evaluation measures within the hierarchy. Having quantified the preferences of the decision-maker within an evaluation measure, we must also elicit and quantify the preferences between evaluation measures and between objectives.

## 3.5. Multi-objective simple additive value function

A multi-objective value analysis requires a value model that ‘‘combines the multiple evaluation measures into a single measure of the overall value of each alternative’’ under consideration [19:53]. The overall function that combines the values resulting from the single dimension value functions will produce the overall value for each alternative—we will use the simple additive value function (see Eq. (1)). A correctly structured hierarchy assumes the objectives in the hierarchy represent mutually exclusive and collectively exhaustive objectives. Mutual Preferential Independence is another requirement for using the additive value function. The objectives in our hierarchy were specifically defined in order to achieve mutual preferential independence.

![](/api/attachments/U3SDPBP6/fulltext/images/4e491a43ea75dd5582c4ddd10bfc330fd105d0f90c41e15778b80c06d8af568b.jpg)  
Fig. 2. Discrete and piecewise-linear value functions.

$$
v (x) = \sum_ {i = 1} ^ {n} w _ {i} v _ {i} (x _ {1})\tag{1}
$$

Where,

$\textstyle \sum _ { i } w _ { i } = 1$ is the requirement for normalization;

 $x _ { i }$ is the score for the ith evaluation measure

 $n$ is the number of objectives (or the number of single dimension value functions);

 $w _ { i }$ is the global weight for the ith objective;

$\nu _ { i } ( x _ { i } )$ returns the value of the alternative with respect to the ith objective; and,

 v(x) is the overall value of an alternative.

The additive function has been shown to be quite robust with respect to preferential independence, especially for large value hierarchies (number of evaluation measures >6). Bodily has shown the additive model to have no more than 4% error if the hierarchy has been built correctly. The additive model requires only single dimension values from each alternative and global weights. We used the swing weight method described in Ref. [11] for eliciting weights from the Decision Maker.

## 4. Evaluation of IA strategy

Information Assurance, like all major decisions, is replete with tradeoffs. The risk accepted by merely operating an information system within today’s globally connected information infrastructure must be balanced with the needs of the organization to accomplish its intended mission, and with the costs associated with the information technologies and practices that assure information systems and the information within them.

This attempt at modeling these tradeoffs resulted in the construction of three distinct value models, denoted by IA, Operational Capability, and Resource Costs. All of these models are focused on a single decision context—Select the best IA strategy. For the purposes of this analysis, an IA strategy is defined as a collection of technical (hardware, software, and firmware) and non-technical (policies and procedures) means to achieve a desired or improved level of IA. An overview of these models will be presented.

![](/api/attachments/U3SDPBP6/fulltext/images/1cb57ea30602ac4de880a1eb04c5ef64f567f5680714a57dcd703863eb62da4d.jpg)  
Fig. 3. The IA balance [14].

The IA model was developed from a combination of ‘top down’ and ‘bottom up’ analysis of DoD doctrine and open literature. Various experts reviewed portions of this model during its development. Establishing the fundamental objectives was the purpose of the top down analysis. The IA model captures the benefits of information assurance.

The Operational Capability model was developed to provide a better understanding of the enhancements or limitations associated with implementing an IA strategy. In general, more secure environments are less capable than those with unconstrained, unmonitored access. Finally, virtually any IA strategy will incur costs in one or more aspects of funding, time, or personnel. The Resource Costs model was developed to facilitate such cost comparisons between alternatives.

A visual representation of how the three models would be integrated is shown in Fig. 3. Once a set of IA strategies is evaluated with respect to each model, the decision-maker must then ascertain the tradeoffs between the three axes. This may be accomplished by weighting the results of the three models and comparing a single number (of overall value) from each strategy. Another approach could be to analyze the individual tradeoffs between the hierarchies. The following sections describe the underlying rationale used for model development. The interested reader can find detailed discussions of VFT in Ref. [17]; a detailed explanation of the specifics of this value model’s components and underpinnings are presented in Refs. [13,14].

## 5. Modeling information assurance

With the overall goal of achieving Information Assurance in mind, the fundamental objectives important to this goal must be identified. Revisiting the definition of IA, we have (Fig. 4):

Information Assurance ‘‘protects and defends information and information systems by ensuring their availability, integrity, identification and authentication, confidentiality, and non-repudiation. This includes providing for restoration of information systems by incorporating protection, detection, and reaction capabilities.’’ [6:III-1]

The stated fundamental objectives of IA are to ‘protect and defend information and information systems.’ Defense, however, implies that (1) forces must be aware of an impending or ongoing attack [detection], and (2) forces have the capability to retaliate in some manner against the threat [reaction]. From this, the three main values (objectives) that support IA are derived: Information and Information System (IS) Protection, Detection, and Reaction capabilities. Each of these contributes value to the decision-maker by taking part in assuring the intended information and information functions.

![](/api/attachments/U3SDPBP6/fulltext/images/e9bf31c47314bf19c7ced56e14046a1921cfffa9a218f2112cbed7435ac005f2.jpg)  
Fig. 4. IA value hierarchy.

Whether a system is a stand alone, isolated system, on a restricted access LAN, running a supervisory control and data acquisition (SCADA) system over telephone lines, or connected to the world-wide web, it will need protection and that protection will have security, operational, and financial impact. Among the top threats to each infrastructure listed in PCCIP is a cyber attack, often launched via the Internet. Just as a chain is only as strong as its weakest link, a system is only as well defend as the most vulnerable element in the system. ‘‘A risk accepted by one is a risk imposed on all.’’ While the CERTs provide outstanding reactive support and are critical to maintaining security, it is necessary to have a level of information assurance that is appropriate for a system’s tasks. The model presented here, coupled with the associated sensitivity analysis, provides a method to baseline a system, highlight potential system gaps and vulnerabilities, and investigate potential effects. It can be used alone to evaluate a system or in conjunction with other available techniques.

It may be argued that taking active measures to detect and react to attacks (thus mitigating their impact) also support the protection role. In order to clarify these values, and ensure mutual exclusivity in the value hierarchy, the definitions used in this analysis are those provided in Table 3. These specific definitions facilitate an independent assessment of each of the IA values, which are discussed further.

## 6. Information and is protection

The key elements from the definition (availability, confidentiality, and integrity) relate to the desired characteristics of information and information systems in order for them to support decision-making. Threats to information assurance, and to these key characteristics, may be defined as ‘‘any circumstance or event with the potential to harm an information system (IS) [or the information within] through unauthorized access, destruction, disclosure, modification of data, and/or denial of service’’ [23:45]. Note that the threats seek to adversely affect the availability (through destruction and denial of service), the confidentiality (through unauthorized access and disclosure), and the integrity (through modification). The motivation, regardless of means, involves the reduction of the information and IS value to the DM. Therefore, measures protecting these characteristics provide value to the decision-maker.

From the definition of IA, ‘ensuring’ identification and authentication and non-repudiation relates to the means that accomplish the protection of information and information systems. Therefore, the key elements ‘identification and authentication’ and ‘non-repudiation’ will be viewed as processes that support the confidentiality and respond objectives respectively. This is supported simply by the accepted definitions shown in Table 6.

One other value that may be incorporated into information and IS protection is Defense-in-Depth. Joint Publication 1-02 defines defense-in-depth as ‘‘the siting of mutually supporting defense positions designed to absorb and progressively weaken attack, prevent initial observations of the whole position by the enemy, and to allow the commander to maneuver his reserve’’ [7:125]. This area evaluates the cyber- and physical-hardness of a system, either of which may contribute to protecting one or all of the values Availability, Confidentiality, and Integrity.

The final value contributing to Information and IS Protection objective may be termed as Compliance,

Table 6 Other key elements of IA

which evaluates the decision-maker’s desire to minimize the potential exposure of an information system and its information system to known vulnerabilities. Learning from others’ misfortunes is much better than experiencing a similar attack firsthand. Measures that permit the evaluation of this objective account for the efficiency (or lack thereof) by which known vulnerabilities, applicable to the system of interest, are reduced or eliminated altogether. Table A-1 in Appendix A lists the evaluation measures developed for the protection portion of the value hierarchy.

## 7. Detection

History has shown the value and need for reliable, adequate, and timely intelligence, and the harm that results from its inaccuracies and absence. [6:III-5]

In light of the historical perspective of ‘detecting enemy actions, Joint doctrine also emphasizes, ‘‘timely attack detection and reporting are the keys to initiating capability restoration and attack response’’ [6:III-10]. In addition to timely detection, effective defense against IO is ‘‘. . .predicated on how well the intelligence processes function and on the agility of [those involved] to implement protective countermeasures’’ [6:III-2]. This suggests that a certain level of reliability is required to ensure that threats are indeed identified—maximizing the probability of detection and minimizing the probability of false alarms. Additionally, an effective IA strategy must also be robust in that it exhibits timeliness and reliability, regardless of the type of attack.

As stated earlier, regardless of the type of attack, the earlier an attack (or intrusion) is detected, the quicker an appropriate response can be initiated. Because of the speed at which cyber attacks may be accomplished, timeliness is a vital factor. In addition, due to the nature of available countermeasures, a distinction between internal (or ‘‘insider’’) attacks and external attacks must be made.

The timely detection of physical attacks is dependent upon the level of sophistication of the controls in place as well as the level of awareness of authorized personnel. More sophisticated controls rely less upon human ability to detect an intrusion.

Social Engineering is defined as ‘‘a deception technique utilized by hackers to derive information or data about a particular system or operation’’ [8:F-17]. There are a number of methods to accomplish this, all of which focus on the lack of awareness or lack of training (or both) that authorized users possess. Timely detection in this context is assumed to rely upon the awareness of the users.

The reliability of intrusion detection systems (IDS) determines how often they fail to detect a valid intrusion, and how often an anomalous event is construed as an intrusion (false alarms). High false alarm rates can consume valuable resources, and could potentially be used to an adversary’s advantage. However, failing to detect a valid intrusion is assumed the more serious of the two possibilities.

The detection reliability of physical attacks is assumed to be dependent upon a combination of the organization’s physical controls and the level of user awareness. The scope of this model currently appraises those areas under the control of the organization—the information system of interest. However, the connectivity and interdependence of today’s systems will eventually require addressing a larger scope, to include the infrastructure supporting the IS. User Training evaluates the effectiveness of training programs designed to provide authorized users with the knowledge to recognize (detect) a potential interpersonal attack. Table A-2 in Appendix A lists the evaluation measures developed for the detection portion of the value hierarchy.

## 8. Reaction

Joint doctrine addresses the importance of response and restoration capabilities [6:III-10]. In this analysis, respond and restore comprise the sub-objectives for reaction, since both are dependent upon either attack detection, attack warning, or some other, perhaps natural, event that has caused or has the potential to cause some level of disruption. The overall objective of an effective reaction capability is to provide the organization with a properly focused response mechanism and to restore the availability, confidentiality, and integrity of information and information systems to their original or an improved state.

## 8.1. Respond

The Properly Focused objective assesses the ability to correctly identify the individuals involved, the vulnerabilities exploited and the motivation for the attack in order to form the most appropriate response against the attacker (or attackers). This process may be accomplished externally or internally, measured by Indicators and Warning (I and W) Notification and ID Accuracy, respectively.

Once an attack is detected and those responsible have been identified, the organization must act to mitigate the risk posed to the organization. Flexible Deterrence entails taking the appropriate action at the appropriate time. In this study, the appropriate action is either stopping the attack, or collecting evidence to facilitate legal action, or both. Due to scope and security considerations, more active defensive measures have not been captured. The appropriate time required to act upon threats depends upon the type of attack, the subsequent risks, and the capability of the organization.

## 8.2. Restore

The potentially damaging effects of today’s attacks on information and information systems often require that an effective reaction capability also permit their restoration. The reliance upon these systems often requires that this process is accomplished in a timely manner, recovers the information as accurately as possible, and results in improvements to the systems, allowing their protection capability to evolve with the threat capability. Table A-3 in Appendix A lists the evaluation measures developed for the reaction portion of the value hierarchy.

## 9. Consideration of operational capabilities and IA

Increasingly complex information systems are being integrated into traditional warfighting disciplines such as mobility; logistics; and command, control, communications, computers, and intelligence (C4I). Many of these systems are designed and employed with inherent vulnerabilities that are, in many cases, the unavoidable consequences of enhanced functionality, interoperability, efficiency, and convenience to users. [6:I-11]

Functionality, interoperability, efficiency, and convenience all add value to the operational capability of an information system. Just as vulnerabilities stem from trying to achieve these values, countermeasures to eliminate them often detract from the information systems’ value. The Operational Capability hierarchy accounts for the changes that may result from IA strategy implementation. This hierarchy attempts to measure these effects, and assumes that the DM wants to minimize any adverse impact upon the existent system at a reasonable level of information assurance (Fig. 5).

## 10. Functionality

Functionality is defined as the usefulness offered to system clients by providing information and information-related capabilities. Attributes that describe the value of the information system regarding functionality are desired and essential capabilities. Essential capabilities are those services that an organization currently relies heavily upon to accomplish their stated mission. If these services are no longer made available, it is assumed that other means must be found to enable the organization to accomplish mission objectives. Desired capabilities are defined as those capabilities that offer enhanced mission effectiveness, but are not required to perform their stated objectives. To ascertain the changes corresponding with an IA strategy, two constructed measures are developed: Impact on Essential Capabilities and Impact on Desired Capabilities. These assess any impact (good or bad) an IA Strategy may have upon services and information currently accessible to authorized users. This focuses only on those services (or supporting services) that are of value to the DM or the majority of authorized users.

![](/api/attachments/U3SDPBP6/fulltext/images/ea2bc7e2c906952c959062162ec52197a4b5511fcdf3162e9ee4edd6ba6c0cb2.jpg)  
Fig. 5. Value hierarchy for operational capability.

## 11. Interoperability

Systems that are interoperable and can be easily integrated with current and future systems provide immediate and cost-effective value to the DM. In the context of ascertaining the value of an IA strategy, Interoperability issues are measured with the two attributes Upgrade Potential and Risk Factors. These measures focus on the potential impact on future maintenance and/or the possibility for upgrades based upon the uniqueness of the components. Risk Factors evaluate the additional risk that may be associated with implementation of certain types of countermeasures within a strategy. This risk applies to the likelihood of new vulnerabilities being introduced into the system, to include the possibility of incompatibility. It is assumed that the level of this risk is contingent upon the maturity of the technology, which serves as a constructed proxy for these types of risk.

## 12. Efficiency

The efficiency of an information system is dependent upon many factors (e.g. bandwidth, throughput, processing capabilities, routing algorithms, and so forth). Currently, the quality of service (QoS) that an information system provides is predominantly system-specific, based upon the architecture and operating system employed, and is dependent upon the workload at any given time. Therefore, the degradation of QoS due to the addition of components (countermeasures) may not be perceived consistently throughout the IS, if at all. For these reasons, a categorical assessment of the impact that an IA Strategy may have upon information systems’ QoS is offered.

## 13. Convenience

Convenience relates to the level of complexity involved in the human interfaces designed into the information system of interest. The tradeoffs involved include buying more security at the expense of preventing users from employing the IS and its information in an operationally effective, or timely, manner. Attributes of a system that measure its convenience includes the requirements a user must fulfill in order to gain authorized access, and the demands placed upon the user to employ and benefit from the IS once access is gained. These are captured by Requirements of User and Impact on Common Operating Environment, respectively.

Table A-4 in Appendix A lists the measures used to evaluate IA strategies with respect to Operational Capability considerations.

## 14. Consideration of the cost of IA strategies

‘‘Technology that affects an adversary’s information and information systems and protects and defends friendly information and information systems will be pursued at every opportunity to ensure the greatest return on investment’’ [6:I-5]. This statement emphasizes the fact that, in an environment of shrinking budgets, costs associated with implementing an IA strategy must be considered. However, in addition to the acquisition costs, implementation costs must also be taken into account. Fig. 6 illustrates the cost hierarchy addressed in this research.

For the purpose of this study, IA costs are grouped into two categories: Finite-Resource Consumption and

![](/api/attachments/U3SDPBP6/fulltext/images/54cd5595b10f2cf31dd4f2ccf937b64a1ef78788660cbc4acdf829988c68ece2.jpg)  
Fig. 6. Resource cost hierarchy.

Fiscal Resources. Finite-Resource Consumption accounts for the tangible, direct costs incurred in time and people that is required to implement an IA strategy. The Fiscal Resources accounts for the dollar costs associated with acquiring an IA strategy.

It is important to note that for the evaluation of costs, low-cost alternatives provide more value to the DM. Therefore, on a scale from 0 to 10, 0 is least preferred (high cost) and 10 is most preferred (low or no cost). This methodology focuses primarily on the total costs in time, people, and money required to procure and implement an IA strategy. Opportunity costs (in dollars), as well as any sunk costs of the legacy system, are not considered. Additionally, salvage value of items being replaced is not directly addressed, but may be incorporated if the appropriate accounting procedures are available. However, the salvage value of IT items is often relatively low.

## 15. Finite-resource consumption

Finite-Resource consumption captures the amount of time and people required to implement an IA strategy.

## 15.1. Time to effectiveness

The element of time is important due to the rapid evolution of technology, as well as the threats against it, suggesting that an effective IA strategy is one that can be implemented quickly. The time required in order for a particular countermeasure (CM) within an IA strategy to become effective is a function of two things—how long it takes to install the CM, and how long it takes the appropriate personnel to be trained in the CM. A CM that is easy to install and requires no training for it to be effective incurs less ‘‘cost’’ in time than a CM that is difficult and time consuming to install and also requires significant training time before it becomes operationally effective. The longer a CM takes to implement, the longer the system remains vulnerable. It is assumed that the DM prefers to minimize the time that the organization’s information and information system are exposed to vulnerabilities identified.

## 15.2. Human resources

The personnel element is of importance due to the associated training, management, and overhead costs; however, the real concern is that of technological expertise. High training costs and turnover rates of personnel specializing in information technology and management may cause an organization to defer an IA strategy requiring more people [15]. The alternative to new workers is requiring overtime of existing personnel. Although, this approach may potentially be cost effective, it is not without consequences and therefore must be considered when evaluating IA strategies.

## 16. Fiscal resources

Recognizing the dollar costs of IA strategies is a key concern; it has been included in the hierarchy. These fiscal costs were broken down into two categories (hardware and software) to capture DM preferences for each type. Hardware Costs include the dollar costs associated with initial procurement, operations and maintenance (O and M), and supporting training dollar costs associated with hardware. Software Costs are considered in an identical manner to the Hardware Costs.

The assumptions for this evaluation consideration include:

 if salvage costs are known, they are included; otherwise, they are ignored;

 it is assumed that funds are available, and will be procured from the appropriate budget where applicable;

 any IA strategy under consideration is assumed to be within budgetary constraints throughout its life span; and

 an alternative that exceeds the organization’s budget will not be considered.

To account for potentially varying life spans of the components within an IA strategy, the total discounted uniform annual costs (Unacost) are calculated. This provides a means to facilitate equitable comparisons between the long-term monetary impacts of IA strategies. If the DM does not require that the costs be broken down into hardware and software, then all Unacost values may be added together, while still considering only those strategies that are within the organization’s budgetary constraints. Table A-5 in Appendix A lists the measures developed for the Resource Costs considerations.

![](/api/attachments/U3SDPBP6/fulltext/images/f48da8f89e27818b15c677300030708f8bc080d31531db0bd4261ed135b1b031.jpg)  
Fig. 7. IA strategy evaluation process.

Table 7 Notional results

<table><tr><td>Alternative</td><td>IA</td><td>Operational capability</td><td>Resource costs</td></tr><tr><td>“Do Nothing” (Baseline)</td><td>2.3</td><td>6.5</td><td>2.5</td></tr><tr><td>Strategy 1</td><td>3.2</td><td>7.2</td><td>2.6</td></tr><tr><td>Strategy 2</td><td>5.8</td><td>5.0</td><td>6.4</td></tr></table>

## 17. Illustrative example

A notional, illustrative example is offered, demonstrating how the models discussed may be used to support the decision-making process.

Fig. 7 shows the overall process required to implement this methodology. Using the triad of models, the organization must evaluate the levels of performance (for each model) based upon current IA strategies that are already being implemented. This serves two purposes. The first establishes a ‘baseline’ of demonstrated performance, which can be compared to the estimated performance of potential alternatives. Second, this is, in itself, a means to find weaknesses within the current IA strategy of an organization—possibly highlighting other areas that the risk assessment may have missed. Areas that score poorly are potential candidates for improvement. New insight may be gained, offering the potential to find new and potentially better controls to construct better IA strategies.

## 17.1. Achieving a balanced IA strategy

As seen in Table 7, three alternatives are offered: ‘‘Do Nothing’’ (which serves as a baseline), Strategy 1, and Strategy 2. The scales, in this example, are from 0 to 10, signifying the DM preference from least to most preferred, respectively. Although the values for alternatives in the illustrative example were randomly generated for proprietary and classification reasons, the underlying intentions were to demonstrate potential differences between alternatives, and the considerations (or tradeoffs) that must be made during comparisons. Application of this methodology would require (1) elicitation of weights from the decision maker and (2) evaluation of each alternative within the value model. Specifics of weight elicitation techniques can be found in Refs. [18,19].

![](/api/attachments/U3SDPBP6/fulltext/images/4a38a11927fcb9c7fe981ba6f620380bef46fb6caa2db66cb23711b42ed9a281.jpg)  
Fig. 8. IA results.

Through inspection of the table, both of the proposed strategies will yield some level of improvement in the organization’s information assurance. Strategy 1, however, will also provide more operational capability at a slightly less resource cost (note that a score closer to 10 is preferred) than what the organization is currently incurring. Strategy 2 provides a much larger increase in information assurance compared to either Strategy 1 or the status quo, and requires fewer resource costs. However, Strategy 2 will result in a decrease in operational capability, compared to what is currently enjoyed by the organization. It should be noted that each proposed strategy might actually be a ‘basket’ or portfolio of information assurance choices. The remainder of this section assumes that the status quo is an unacceptable option, for one reason or another.

![](/api/attachments/U3SDPBP6/fulltext/images/6acc677bcfaed85c656ee14338905d7c50189bf48ca2664f86ac0b1602123c10.jpg)  
Fig. 9. Operational capability results.

![](/api/attachments/U3SDPBP6/fulltext/images/39d6a0eac1735cdee028d391ce3b8446443b165c040b4449c267e3d89e442675.jpg)  
Fig. 10. Resource costs results.

To gain further insight from the evaluation process, the extent to which each strategy contributes to the decision-maker preferences can be analyzed. For example, Fig. 8 shows the portion of value from each strategy that is attributed to the three main objectives within the IA value model. The ‘Best Case’ at the bottom of the chart shows the weights that would be assigned to each of the objectives. In this example, these correspond to 0.5, 0.3, and 0.2 for Protection (InformationandIS), Detection, and Reaction, respectively.

Again, a similar approach may be taken for the other dimensions of this problem. Fig. 9 shows which objectives each strategy meets (or more importantly, falls short of) the decision-maker’s fundamental objectives within the Operational Capability value model.

![](/api/attachments/U3SDPBP6/fulltext/images/fe4aa65df39d852e40ba97c0c170ea7fe0e7202faee1848168e66c43767af1e0.jpg)  
Fig. 11. Sensitivity analysis results.

Finally, the same type of graphical analysis is shown for the strategies with respect to the Resource Costs value model, shown in Fig. 10. An added benefit to this type of modeling is the capability to assess the sensitivity of the results to the underlying assumptions, particularly the weights.

According to the ‘Best Case’ data in Fig. 10, the current weights are 0.25, 0.25 and 0.5 for the Time to Effectiveness, Human Resources and Fiscal Resources objectives, respectively. Suppose that the DM noted that Strategy 2 was much more cost effective (Fiscal Resources) than Strategy 1; however, evaluation of Strategy 2 revealed that it would take much longer to implement (Time to Effectiveness). If uncertainty exists about the initial weight assigned to the Time to Effectiveness objective, analysis of the sensitivity of the model results to this weight is accomplished, and is shown in Fig. 11.

At the point of the original weight for Time to Effectiveness (0.25), the values (and subsequently the rank order) of the strategies are shown. However, as the weight for Time to Effectiveness is extended beyond (approximately) 0.7, then the preference between the two strategies changes. Note that this only considers changing one weight (within one model) at a time, keeping the relative weighting of all other objectives constant.

![](/api/attachments/U3SDPBP6/fulltext/images/de4451b5eb929f28a164b5acf1b1b58bdde2b03fb10ad9f774cfad57b0a0a7e2.jpg)  
Fig. 12. Notional comparison.

Not only do these methods of analysis enable the decision maker to evaluate the tradeoffs between and within IA strategies from a ‘big picture’ perspective, the results may be broken down to provide information regarding the specific areas where a strategy did (or did not) perform well and why. This further poses a potential for identifying new and improved ways to attain the organization’s objectives in each of the three areas. Fig. 12 shows a method to graphically compare the subsequent results for all three models simultaneously.

## 18. Summary

The formulation of this analytical framework not only facilitates the evaluation of IA strategies, but the development of them as well. This is accomplished by focusing on what the decision-maker values with respect to information assurance, operational capability, and the limited resources available. This focus quantifies the value added for each component within a strategy, providing a method to balancing the three in order to provide the most overall value to the decision-maker.

The outputs of this effort lend themselves to the evaluation of an Information System with the triad of value models created to address Information Assurance, Operational Capability, and Resource Cost considerations.

To evaluate alternative IA strategies, measures were developed to assess the level to which these strategies meet (or do not meet) their objectives. This was accomplished mostly through bottom-up analysis, focusing on how current alternatives (countermeasures) differ and why.

The culmination of these efforts resulted in a fully functional decision support tool (developed in Microsoft Excel<sup>n</sup>) that enables the decision-makers and system experts to implement the current value models. This tool is capable of accepting inputs for each evaluation measure and the weighting criteria required, as well as providing a summary of results. Minor modifications would allow sensitivity analyses and other presentation schema. Additionally, the process required to incorporate new evaluation measures is semi-automated through the use of Visual Basic<sup>n</sup> macros. All of these aspects facilitate the actual implementation of the described methodology.

## 18.1. Recommendations for future research

This methodology assumes that the outcomes of each alternative, with respect to their appropriate evaluation measure scores, are deterministic. However, similar to the methodology developed in Ref. [10] pertaining to offensive IO evaluation, the expected scores, combined with the projected high and low scores, allow the multiobjective value model to give DM’s insight into the relative uncertainty of each alternative [10].

The deterministic nature assumed for this modeling effort may not be entirely appropriate for all circumstances. For example, some controls suggested to mitigate risks are not ‘‘100%’’solutions. The rapid evolution not only of technology, but of the threats against them, also lends the information technology environment to potential uncertainties. The eventual incorporation of utility may prove useful for future decision-makers implementing this model, enabling them to incorporate their own risk preferences in the evaluation of alternatives ‘‘in decisions where there is uncertainty about the specific consequence that will result from selecting a particular alternative’’ [19:245].

Another potential avenue for analytical efforts involves the application of mathematical programming techniques—linear or goal programming, in particular. This assumes that an optimal IA strategy is sought, requiring the maximization of the levels of IA and operational capability while adhering to any applicable resource constraints. One means of approaching this may be accomplished by identifying potential components (technical and non-technical) that comprise the IA strategy alternatives. Once these components are identified, the incremental changes that occur in each of the IA ‘triad of models’ may be determined, serving as the coefficients within the chosen mathematical model. Existing formulations of multi-dimensional knapsack problems with multiple-choice constraints and capital budgeting problems provide promising avenues in such an endeavor [5].

It is also important to note that the focus of this research was taken from an organizational perspective. The connectivity of today’s organizations, and their reliance upon each other (particularly within the realm of our Nation’s information infrastructures), will eventually require a broader scope. This may be accomplished by either: (1) evaluating systems of systems (an inter-organizational perspective), or (2) by building upon current policy, facilitating the creation of a common mental model of the elements that are important to everyone concerning Information Assurance.

Despite the level of the perspective, the values considered in the IA problem should remain constant. However, the level of perspective may change the underlying motivations (and therefore the shapes of the value functions, and perhaps the axis-limits) concerning the benefits received from a strategy, compared to its impact on capabilities and its cost. A strategy that is regarded as least preferred from an individual organization’s viewpoint might be the only acceptable alternative from a National perspective. Fortunately, this is where the strengths of VFT and the set of models will provide common ground to communicate and eliminate weaknesses in our Nation’s Information Assurance posture. Nonetheless, this potential area of concern should be considered in future studies.

There is still much work to be done in this area; the need for Information Assurance will persist as long as information technologies are relied upon. The focus on decision-makers’ values will lead to the development of alternatives that have a better chance of fulfilling their IA objectives. Through the proposed set of models, modeling Information Assurance provides a means to accomplish this goal, and a foundation to build upon—offering insight into the difficult and complex problem of Information Assurance.

## Acknowledgements

This work was supported by a grant from DARPA/IASET program. Additional support was provided by OSD/OT and E. We are also indebted to a vast number of individuals who shared their insights with us. We also wish to thank the editor and the reviewer for their insightful comments and suggestions.

## Appendix A

Table A1. Evaluation Measures Developed for Information and IS Protection

<table><tr><td>Title</td><td>Measure unit</td><td> $Measure type^a$ </td><td>Lower bound</td><td>Upper bound</td></tr><tr><td colspan="5">Defense in Depth</td></tr><tr><td>Time to penetrate essential elements</td><td>Ratio: (time required to attack)/(time required to defend)</td><td>Ratio (S-curve)</td><td>0</td><td>4</td></tr><tr><td>Physical security</td><td>Probability of failure</td><td>Probability (Exponential)</td><td>0</td><td>1</td></tr><tr><td colspan="5">Compliance</td></tr><tr><td>Patches installed</td><td>Percentage of applicable patches installed</td><td>Percentage (Linear)</td><td>0</td><td>100</td></tr><tr><td>Latency-Implementation</td><td>Maximum age of known vulnerability</td><td>Months (Linear)</td><td>0</td><td>6</td></tr><tr><td>Latency-Assessment</td><td>Time since last vulnerability assessment</td><td>Years (Exponential)</td><td>0</td><td>3</td></tr><tr><td colspan="5">Availability</td></tr><tr><td>Essential Service Uptime</td><td>Percentage Availability of Essential Services</td><td>Percentage (S-Curve)</td><td>90</td><td>100</td></tr><tr><td>(Overall) System Uptime</td><td>Percentage Availability of the Overall System</td><td>Percentage (S-Curve)</td><td>75</td><td>100</td></tr><tr><td>Information Redundancy</td><td>Number of Data Sources</td><td>Quantity</td><td>1</td><td>4</td></tr><tr><td colspan="5">Confidentiality</td></tr><tr><td>Filter Technology</td><td>Filter Type</td><td>Category</td><td>Packet</td><td>Hybrid</td></tr><tr><td>Authentication Strength</td><td>Identification and Authentication (I&amp;A) Method</td><td>Category</td><td>None</td><td>Combination</td></tr><tr><td>Supporting Policy</td><td>I and A Support</td><td>Category</td><td>No-Policy</td><td>Policy-Automated</td></tr><tr><td>Encryption Strength</td><td>Encryption Generation Used</td><td>Category</td><td>None</td><td>State of the Art</td></tr><tr><td colspan="5">Integrity</td></tr><tr><td>Data Integrity</td><td>Implementation of Anti-Malicious Code</td><td>Category</td><td>None</td><td>Automated-Full</td></tr><tr><td>System Integrity</td><td>Percentage of Validated Components</td><td>Percentage (Exponential)</td><td>0</td><td>100</td></tr></table>

(Shape) of value function, if applicable.

Table A2. Evaluation Measures Developed for Detection

<table><tr><td>Title</td><td>Measure unit</td><td>Measure type</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td colspan="5">Timely</td></tr><tr><td>Internal Cyber Attacks</td><td>Detection Capability</td><td>Category</td><td>None</td><td>Real-Time(Off Duty)</td></tr><tr><td>External Cyber Attacks</td><td>Detection Capability</td><td>Category</td><td>None</td><td>Real-Time(Off Duty)</td></tr><tr><td>Physical Attacks</td><td>Time to PhysicalIntrusion Detection</td><td>Hours (Exponential)</td><td>0</td><td>72</td></tr><tr><td>Interpersonal Attacks</td><td>User Awareness</td><td>Percentage (Exponential)</td><td>0</td><td>100</td></tr><tr><td colspan="5">Reliable</td></tr><tr><td>Internal Cyber Attacks</td><td>Time Between Configuration</td><td>Days (S-Curve)</td><td>0</td><td>30</td></tr><tr><td>External Cyber Attacks</td><td>Time Between Configuration</td><td>Days (S-Curve)</td><td>0</td><td>30</td></tr><tr><td>Physical Attacks</td><td>Control Sophistication</td><td>Category</td><td>Presence</td><td>Automated</td></tr><tr><td>Interpersonal Attacks</td><td>Training Effectiveness</td><td>Category</td><td>Not Addressed</td><td>Trained and Evaluated</td></tr></table>

Table A3. Evaluation Measures Developed for Reaction

<table><tr><td>Title</td><td>Measure unit</td><td>Measure type</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td colspan="5">Respond (Properly Focused)</td></tr><tr><td>Indicator and Warning Sources</td><td>Number of Sources of Warning</td><td>Quantity</td><td>0</td><td>5</td></tr><tr><td>Identification Accuracy</td><td>Granularity of Non-repudiation</td><td>Category</td><td>None</td><td>Comprehensive</td></tr><tr><td colspan="5">Respond (Flexible Deterrence)</td></tr><tr><td>Timely Initiation of Deterrent Options</td><td>Decision Level Required</td><td>Category</td><td>Automatic</td><td>Higher Level</td></tr><tr><td>Stop Attack</td><td>Process to Stop Attack</td><td>Category</td><td>No Capability</td><td>Automatic</td></tr><tr><td>Collect Evidence</td><td>Capability to Collect Evidence</td><td>Category</td><td>No Capability</td><td>System-Benign</td></tr><tr><td colspan="5">Restore Information and IS (Timely)</td></tr><tr><td>Time to Restore Essential Elements</td><td>Time Required</td><td>Time (Linear)</td><td>0</td><td>Maximum acceptable time specified by organization</td></tr><tr><td>Time to Restore to Fully Operational Capable Level</td><td>Time Required</td><td>Time (Linear)</td><td>0</td><td>Maximum acceptable time specified by organization</td></tr><tr><td colspan="5">Restore Information and IS (Accurately)</td></tr><tr><td>Restoration Accuracy</td><td>Percentage of Information Recoverable</td><td>Percentage (S-Curve)</td><td>0</td><td>100</td></tr><tr><td colspan="5">Restore Information and IS (Improved State)</td></tr><tr><td>Resource Inventory</td><td>Percentage of Components Inventoried</td><td>Percentage (S-Curve)</td><td>0</td><td>100</td></tr><tr><td>Improved State</td><td>Are procedures in place?</td><td>Yes/No</td><td>-</td><td>-</td></tr></table>

Table A4. Measures Developed for Operational Capability Model

<table><tr><td>Title</td><td>Measure unit</td><td>Measure type</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td colspan="5">Functionality</td></tr><tr><td>Impact on Essential Capabilities</td><td>Net Change in Essential Services</td><td>Quantity (Linear)</td><td>-3</td><td>3</td></tr><tr><td>Impact on Desired Capabilities</td><td>Net Change in Desired Services</td><td>Quantity (Linear)</td><td>-3</td><td>3</td></tr><tr><td colspan="5">Interoperability</td></tr><tr><td>Upgrade Potential</td><td>Component Source</td><td>Category</td><td>One-of-a-kind</td><td>COTS</td></tr><tr><td>Risk Factors</td><td>Technology Type</td><td>Category</td><td>Never been used</td><td>Previously used on a similar system with similar configuration</td></tr><tr><td colspan="5">Efficiency</td></tr><tr><td>Quality of Service</td><td>Impact on Network Performance</td><td>Category</td><td>Unacceptable Performance</td><td>Improved Performance</td></tr><tr><td colspan="5">Convenience</td></tr><tr><td>Requirements of User</td><td>Time to Access System</td><td>Time (S-Curve)</td><td>0 (seconds)</td><td>Maximum acceptable time designated by organization</td></tr><tr><td>Impact on Common Operating Environment</td><td>Impact based upon previous system</td><td>Category</td><td>Negative Impact</td><td>Positive Impact</td></tr></table>

Table A5. Measures Developed for Resource Costs Model

<table><tr><td>Title</td><td>Measure unit</td><td>Measure type</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td colspan="5">Finite Resource Consumption (Time to Effectiveness)</td></tr><tr><td>Installation Time</td><td>Days required to install all components within the strategy</td><td>Days (Linear)</td><td>0</td><td>365</td></tr><tr><td>Personnel Training Time</td><td>Days required to complete required training associated with strategy.</td><td>Days (Linear)</td><td>0</td><td>365</td></tr><tr><td colspan="5">Finite Resource Consumption (Human Resources)</td></tr><tr><td>Workforce</td><td>Percentage change in workforce required</td><td>Percentage (Linear)</td><td>0</td><td>100</td></tr><tr><td>Workload</td><td>Overtime hours (per week, per person)</td><td>Hours (Exponential)</td><td>0</td><td>20</td></tr><tr><td colspan="5">Fiscal Resources</td></tr><tr><td>Total Hardware UNACOST</td><td>Uniform Annual Cost</td><td>Dollars (Linear)</td><td>0</td><td>Determined by applicable budget constraints</td></tr><tr><td>Total Software UNACOST</td><td>Uniform Annual Cost</td><td>Dollars (Linear)</td><td>0</td><td>Determined by applicable budget constraints</td></tr></table>

## References

[1] D.S. Alberts, Defensive Information Warfare, National Defense University, Institute for National Strategic Studies, The Center for Advanced Concepts and Technology, Washington, 1996 (August).

[2] R.H. Anderson, P.M. Feldman, S. Gerwehr, B. Houghton, R. Mesic, J.D. Pinder, J. Rothenberg, J. Chiesa, Securing the U.S. Defense Information Infrastructure: A Proposed Approach, RAND, Santa Monica, 1999.

[3] R.T. Clemen, Making Hard Decisions, Brooks/Cole Publishing, Pacific Grove, CA, 1996.

[4] Computer Emergency Response Team/Coordination Center (CERT/CC). CERT/CC Statistics: 1998 – 2001, Carnegie Mellon Software Engineering Institute (Excerpt from published report, http://www.cert.org/stats/cert<sup>\_</sup>stats.html#incidents), Pittsburgh, 2003 (14 Oct).

[5] C.C. Davis, R.F. Deckro, J.A. Jackson, A Methodology for Evaluating and Enhancing C4 Networks, Military Operations Research 4 (2) (1999) 45–60.

[6] Department of Defense, Joint Chiefs of Staff, Joint Publication 3 – 13, Joint doctrine for Information Operations, Pentagon, Washington, 1998 (9 Oct).

[7] Department of Defense, Joint Chiefs of Staff, Joint Publication 1-02, Department of Defense Dictionary of Military and Associated Terms, Pentagon, Washington, 1999 (amended through 29 June).

[8] Department of Defense, Joint Chiefs of Staff, Information Assurance: Legal, Regulatory, Policy and Organizational Legal, Regulatory, Policy and Organizational Considerations, (Fourth Edition), Pentagon, Washington, 1999 (August 1999).

[9] Department of the Air Force, Identification and Authentication, AFMAN 33– 223, HQ USAF, Washington, 1998 (1 June).

[10] M.P. Doyle, R.F. Deckro, J. Kloeber, J.A. Jackson, Measures of merit for offensive information operations courses of action, Military Operations Research 5 (2) (2000) 5 – 18.

[11] W. Edwards, F.H. Barron, SMARTS and SMARTER: Improved Simple Methods for Multiattribute Utility Measurement, Organizational Behavior and Human Decision Processes 60 (1994) 306–325.

[12] B. Gertz, Computer hackers could disable military, The Washington Times, (1998 April 16) A1.

[13] J.T. Hamill, Modeling Information Assurance: A Value Focused Thinking Approach, Masters Thesis, AFIT/GOR/ENS/ 00M-15, Air Force Institute of Technology, Wright-Patterson AFB, OH, 2000 (March).

[14] J.T. Hamill, R.F. Deckro, J. Kloeber, ‘‘A Strategy for Information Assurance,’’ Technical Report number 2000 – 02, Center for Modeling, Simulation, and Analysis, Air Force Institute of Technology, Wright-Patterson AFB, OH, 2000 (September).

[15] Information Operations Symposium: Key Technologies for Information Assurance, San Diego, CA, 1999 (26 – 28 October).

[16] R.L. Keeney, Using values in operations research, Operations Research, (1994 (September – October)) 793 – 813.

[17] R.L. Keeney, Value Focused Thinking: A Path to Creative Decisionmaking, Harvard Univ. Press, Cambridge, 1998.

[18] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Cambridge Univ. Press, Cambridge, 1976.

[19] C.W. Kirkwood, Strategic Decision Making: Multiobjective Decision Analysis with Spreadsheets, Duxbury Press, Belmont, 1997.

[20] T.A. Longstaff, J.T. Ellis, S.V. Hernan, H.F. Lipson, R.D.

McMillan, L.H. Pesante, D. Simmel, Security of the Internet, Carnegie Mellon University, Software Engineering Institute (Excerpt from published article, http://www.cert.org/encyc<sup>\_</sup> article/tocencyc.html) Pittsburgh, 1997.

[21] R.D. Materna, Assessing the Value of Information Technology, Strategic Consulting Group, NCR, Dayton, 1992 (March).

[22] National Computer Security Center (NCSC), Accreditor’s Guideline, NCSC-TG-032, Version 1.6, 1997 (March).

[23] National Security Telecommunications and Information Systems Security Committee (NSTISSI), National Information Systems Security (INFOSEC) Glossary (Revision 1), NSTISSI No. 4009, National Security Agency, Fort Meade, 1999 (January).

[24] President’s Commission on Critical Infrastructure Protection (PCCIP), Critical Foundations: Thinking Differently, GPO, Washington, 1997 (October).

Richard F. Deckro is a Professor of Operations Research in the Department of Operational Sciences at the Air Force Institute of Technology. He holds a BSIE from the State University of New York at Buffalo, and an MBA and a Doctorate of Business Administration in Decision Sciences from Kent State University. Dick’s research and consulting interests are in the areas of infor mation operations, campaign modeling, optimization, project management, scheduling, network models, decision analysis, and multi criteria decision making. It is his pleasure and honor to currently serve as the Vice President of INFORMS’ Military Applications Society and as the Editor of Military Operations Research.

Jonathan Todd Hamill, Major, USAF is a PhD student in the Department of Operational Sciences at the Air Force Institute of Technology. He holds a BS (Operations Research) from the United States Air Force Academy at Colorado Springs, CO, an MSIE from New Mexico State University and an MS (Operations Research) from Air Force Institute of Technology. Todd’s research interests are in the areas of information operations, optimization, network models, simulation, decision analysis, and multi-criteria decision making. He currently serves the Military Operations Research Society as the Information Operations/Information Warfare Working Group Chair for the Military Operations Research Society Symposium.

Jack M. Kloeber Jr. is a retired US Army Lieutenant Colonel with interests in military decision-making, information operations, technology selection, R&D portfolio analysis and decision analysis. He received his PhD in Economic Decision Analysis from the Engineering School at the Georgia Institute of Technology. Having taught graduate-level courses in decision analysis and combat simulation at the Air Force Institute of Technology for six years, Jack retired from the US Army and is now Director, Portfolio Management, Johnson & Johnson Pharmaceutical Research & Development, in Titusville, NJ.
