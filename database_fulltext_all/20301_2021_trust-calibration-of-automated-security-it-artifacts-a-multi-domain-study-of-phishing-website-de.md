---
otero_id: 20301
otero_key: "4HJFE7F8"
title: "Trust calibration of automated security IT artifacts: A multi-domain study of phishing-website detection tools"
authors: "Yan Chen; Fatemeh Mariam Zahedi; Ahmed Abbasi; David Dobolyi"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103394"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Trust Calibration of Automated Security IT Artifacts: A Multi-Domain Study of Phishing-Website Detection Tools

Yan Chen, Fatemeh Mariam Zahedi, Ahmed Abbasi, David Dobolyi

![](/api/attachments/4HJFE7F8/fulltext/images/6e1bd44027777496a6aa62767d5b4acca7a69d9ecb6d2b548a9f1cca74e270d3.jpg)

PII: S0378-7206(20)30332-3

DOI: https://doi.org/10.1016/j.im.2020.103394

Reference: INFMAN 103394

To appear in: Information & Management

Received Date: 13 November 2019

Revised Date: 16 November 2020

Accepted Date: 18 November 2020

Please cite this article as: Chen Y, Zahedi FM, Abbasi A, Dobolyi D, Trust Calibration of Automated Security IT Artifacts: A Multi-Domain Study of Phishing-Website Detection Tools, Information and amp; Management (2020), doi: https://doi.org/10.1016/j.im.2020.103394

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Trust Calibration of Automated Security IT Artifacts: A Multi-Domain Study of Phishing-Website Detection Tools

Yan Chen<sup>a</sup>\*, Fatemeh Mariam Zahedi<sup>b</sup> Ahmed Abbasi<sup>c</sup>, David Dobolyi<sup>d</sup>

<sup>a</sup> College of Business, Florida International University, 11200 S.W. 8th St., RB 203A, Miami, FL 33199, United States. Email: yachen@fiu.edu

<sup>b</sup> Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee, 3202 N Maryland Ave, Milwaukee, WI 53202, United States. Email: zahedi@uwm.edu

<sup>c</sup> Mendoza College of Business, University of Notre Dame, 204 Mendoza College of Business, Notre Dame, IN 46556, United States. Email: aabbasi@nd.edu

<sup>d</sup> Mendoza College of Business, University of Notre Dame, 204 Mendoza College of Business, Notre Dame, IN 46556, United States. Email: ddobolyi@nd.edu

\*Corresponding Author

## Abstract

Phishing websites become a critical cybersecurity threat affecting individuals and organizations Phishing-website detection tools are designed to protect users against such sites. Nevertheless, detection tools face serious user trust and suboptimal performance issues which require trust calibration to align trust with the tool’s capabilities. We employ the theoretical framework of automation trust and reliance as a kernel theory to develop the trust calibration model for phishing-website detection tools. We test the model using a controlled lab experiment. The results of our analysis show that users’ trust in detection tools can be calibrated by trust calibrators. Moreover, users’ calibrated trust has significant consequences, including users’ tool reliance, use, and performance against phishing websites.

Keywords: trust calibration, automated security IT, phishing websites, detection tools, Trust in IT

## Introduction

Phishing websites victimize millions of Internet users, exacting significant monetary losses and social costs for individuals and organizations (Abbasi et al. 2015; Frauenstein and Flowerday 2020; Zahedi et al. 2015). An FBI announcement showed that phishing rendered \$26 billion damage over a three-year period from 2016 to 2019 (FBI 2019). About \$1.1 million per hour is lost to phishing attacks (RiskIQ 2019).

Phishing websites come in two forms: spoof and concocted. Spoof sites mimic existing, generally well-known websites to engage in identity theft or malware dissemination (Aaron and Rasmussen 2017; Abbasi et al. 2010). Concocted sites are fictional websites designed to conduct social engineering, fraudulent online advertising, or black-hat search engine optimization-based attacks for monetary gains or malware propagations. Both categories of phishing websites have serious implications for Internet users and organizations, such as damaging brand equity and increasing customer churn rates (Aaron and Rasmussen 2017). Concocted websites also frequently appear in top-ranked search results (Whittaker 2017) and routinely disseminate malware to unsuspecting site visitors (Abbasi et al. 2012). Phishing-website detection tools

These detection tools belong to a subcategory of IT called automated security IT and are defined as a type of security IT that uses certain mechanisms to automatically classify an event/objective as normal or malicious (Cavusoglu and Raghunathan 2004) while allowing users to make the final security decision (Cranor 2008). There are many phishing-website detection tools, but reports indicate that users often ignore or disuse their advice (Bravo-Lillo et al. 2013; Reeder et al. 2018). A survey of Internet users found that 60% of respondents do not use the web

##

browsers’ built-in phishing-website detection tools (Symantec 2010). Many users rely solely on intuition to judge the credibility of a website despite the fact that spoof rates can be as high as 33%-45% when users rely on their own mental model (Abbasi et al. 2012; Dhamija et al. 2006; Goel et al. 2017). While research shows that user accuracy in detecting phishing websites is much lower than the accuracy of the detection tools (Abbasi et al. 2015), the rate of ignoring certain types of warnings in some browsers (e.g., SSL warnings) can be as high as 60% (Akhawe and Felt 2013). These results suggest that detection tools face serious trust issues in users. Addressing these issues demands a novel approach to investigate user trust vis-à-vis characteristics of detection tools.

Research shows that IT characteristics influence users’ various perceptions, emotions, attitudes, and behaviors (Cyr 2008; Gefen et al. 2003; Lankton et al. 2015; Song and Zahedi 2008). Similarly, the characteristics of security detection tools have multiple influences and have been examined from multiple points of view, such as design of warning signals (Chen et al. 2011), neurophysiological impacts (Anderson et al. 2016; Vance et al. 2018), and threat and coping appraisal perceptions (Zahedi et al. 2015).

One of the most important factors impacted by the IT characteristics is trust in IT. Information Systems (IS) research has extensively investigated trust in IT at both organizational and individual levels (e.g., Lankton et al. 2016; McKnight et al. 2011; Vance et al. 2008; Wang and Benbasat 2008). However, the research has focused mainly on general-purpose IT and ecommerce—also referred to as positive IT (Dinev and Hu 2007). Positive IT strives for high levels of trust in order to increase user adoption and usage (Lankton et al. 2015; McKnight et al. 2002). However, this is not necessarily the case for security detection tools. An “inappropriate”

level of trust in detection tools can have negative financial and privacy consequences for users, leading to subsequent loss of their trust and use (Li et al. 2014; Reeder et al. 2018).

We address the issue of inappropriate trust by arguing that trust in such detection tools should be calibrated by closely aligning trust to the capability of the tool. Proper trust in detection tools requires matching trust with the tools’ capability to identify phishing websites. Detection tools with high capabilities should enjoy higher levels of users’ trust relative to those with low capabilities. Hence, we posit that calibrating users’ trust in detection tools should play an important role in promoting protection against phishing websites.

Trust calibration is a concept developed in automation research. It is defined as the process of creating correspondence between the extent of users’ trust in an automated tool and the capability of that tool (Hoffman et al. 2013; Lee and See 2004; Madhavan and Wiegmann 2007). Calibrated trust is the level of trust that matches the capability of the tool—the level of user trust after gaining knowledge about the tool’s capability (Lee and See 2004). In spite of its importance, IS research has not addressed inappropriate trust and trust calibration in automated security IT. In practice, while automation research has reported that providing accurate and trustworthy information on automation capability and process (e.g., via display or interface design) influences trust calibration (Schaefer et al. 2016), detection tools do not provide such information. Our paper addresses this research gap with the focus on phishing-website detection tools as a type of automated security IT that allows users to make the final decision.

This paper takes a theoretical approach to identify the salient factors (or trust calibrators) in calibrating trust in phishing-website detection tools and the outcomes of calibrated trust in such tools for individual users. Therefore, the research questions in this paper are as follows—What are the antecedents of calibrated trust in phishing-website detection tools for individual users?

What are the consequences of calibrated trust in these tools for individual users?

To address these research questions, we employ the theoretical framework of automation trust and reliance (ATR) (Lee and See 2004) as a kernel theory to develop the trust calibration model for phishing-website detection tools (referred to as the TC model for brevity). We test the TC model using a controlled lab experiment. The results uncover the importance of detection rate and outcome severity in calibrating trust in phishing-website detection tools and the central role of calibrated trust in users’ higher reliance, use, and protection against phishing websites. We discuss the theoretical and practical implications of our work for individuals, organizations, and security IT tool designers.

## Literature Review

Automated security IT artifacts carry out partially or fully automatic protective functions such as detecting, deterring, disabling, or eliminating the security threats a user could encounter when using IT. As such, phishing-website detection tools fall under automation, defined as a technology that “accomplishes (partially or fully) a function that was previously, or conceivably could be, carried out (partially or fully) by a human operator” (Parasuraman et al. 2000, p. 287). Different from automated security IT artifacts with no user choice (e.g., firewalls), phishingwebsite detection tools give users the choice of accepting or rejecting their advices (Cranor 2008). The automatic nature of security detection tools with user choice plays a critical role in their trust calibration, and places the study of such calibration within the domain of automated security IT.

While trust in general-purpose IT is viewed as desirable—the higher the trust, the more usage (Lankton et al. 2015; McKnight et al. 2002), this is not necessarily the case for automated security IT that end users can ignore its advice. For such IT, only an “appropriate” level of trust

##

is desirable in order to protect users from harms and losses. Overtrust may cause abuse—people overly rely on it and incur losses due to its errors in detecting threats. Undertrust leads to disuse—people reject its capabilities and incur losses due to ignoring its advice. This is shown to be true for all automated tools that are imperfect (Hoff and Bashir 2015; Kraus et al. 2019; Lee and See 2004; Lu and Sarter 2019; Madhavan and Wiegmann 2007). Therefore, trust calibration is critical for a proper level of trust. Without calibrated trust, phishing-website detection tools

Past research on trust in IT has focused on general-purpose IT and sought to increase trust based on the assumption that the higher the trust, the higher the usage (see the summary of our literature review in Table B-1 of Appendix B). Another assumption is that IT has social presence and users have opportunities to interact with IT to form or increase their trust (Lankton et al. 2015). As such, trustworthiness beliefs are defined as trust antecedents, and these beliefs are critical in forming and increasing trust. Research has borrowed ability, integrity, and benevolence as trustworthiness beliefs from interpersonal trust studies to investigate trust in IT, including more recent studies on trust in artificial intelligence IT (e.g., Glikson and Woolley 2020), and found that such beliefs are shown to be significant in increasing trust (Glikson and Woolley 2020; Vance et al. 2008). When the IT artifact has social presence (such as recommendation agents that act as human agents and Facebook with its features for interpersonal interactions), the literature suggests that interpersonal trustworthiness beliefs (ability, integrity, and benevolence) explain users’ perceptions and behaviors (Glikson and Woolley 2020; Lankton et al. 2015; Vance et al. 2008).

However, the role of such trustworthiness beliefs has come under question when IT artifacts lack social presence (e.g., MS Access) (Lankton et al. 2015). Research suggests that for IT

artifacts without social presence, trust should be based on system features (Lankton et al. 2015; McKnight et al. 2011). Studies of trust in artifacts without social presence is scarce. Research in trust in automated security IT is almost non-existent. One exception is a study on antivirus software (Paravastu et al. 2014), which reports performance, predictability, and subjective norms as predictors of trust in and satisfaction with the artifact and argues that some of these predictors partially overlap interpersonal trustworthiness beliefs.

Automated security IT that advises users is different by nature from general-purpose IT (see the summary in Table 1). In addition to its lack of social presence, it runs automatically in the background with minimal human-computer interactions and is not the primary focus of users’ activities. As a result, users tend to ignore security tools’ warnings for the expediency of accomplishing their primary task—access to their intended websites. Even when they follow the advice of the tool, they do so with little knowledge about and feedback from the tool. In other words, users have no detailed information about or interactions with the tool to calibrate their trust, so they end up making security-related decisions in the dark. Moreover, the “security” such tools provide is an abstract concept for users (West 2008; Whitten and Tygar 1999) as security is invisible and its desirable consequence is a non-event. “The reward for being more secure is that nothing bad happens” (West 2008, p. 37). More importantly, such tools deal with changing and morphing adversaries who try to undermine tools’ performance and victimize users. In summary, these unique characteristics demand a fresh perspective and theory-based analysis on trust in automated security IT with user choice in general and phishing-website detection tools in particular.

Table 1. Characteristics of Automated Security IT Compared to General IT

<table><tr><td>Automated Security IT with User Choice*</td><td>General IT</td></tr><tr><td>Automated security IT lacks social presence.</td><td>General IT has a certain level of social presence.</td></tr><tr><td>Automated security IT deals with security tasks that are secondary to end-users (Dhamija et al. 2006; Whitten and Tygar 1999). When detecting fraud, security IT interferes with users' primary tasks. Consequently, users are less willing to focus on or attend to the advice of security IT.</td><td>General IT is a part of users' primary tasks, on which users focus and pay full attention.</td></tr><tr><td>Automated security IT works in the background, hidden from users. As such, characteristics of security IT are invisible to users. Consequently, users make security decisions with little knowledge about the tool (Whitten and Tygar 1999).</td><td>General IT interacts with users via human-computer interactions. IT characteristics are more visible to users.</td></tr><tr><td>Automated security IT provides security, which is an abstract concept to users (West 2008; Whitten and Tygar 1999).</td><td>General IT assists users to improve performance, efficiency, and productivity of the task, which are concrete gains to users.</td></tr><tr><td>Automated security IT has persistent adversaries who try to undermine security tools' performance and victimize their users.</td><td>General IT does not have adversaries, who actively and persistently try to undermine the tools' performance.</td></tr><tr><td colspan="2">* In this study, we study phishing-website detection tools as exemplars of automated security IT that allows users the choice of accepting or rejecting its advice.</td></tr></table>

Trust calibration in automation has been studied (as reported in Table B-2 of Appendix B). As shown in those studies, various characteristics and performance metrics can be used to calibrate trust. Trust calibration is one of the most important design strategies that leads to proper reliance and human-automation performance (Hoffman et al. 2013; Kraus et al. 2019; Lee and See 2004; Lu and Sarter 2019; Madhavan and Wiegmann 2007; Stowers et al. 2020). Automation literature reports that trust in automation is turbulent, fragile, and tentative. It must be properly and promptly calibrated by salient calibrators that inform users about the key characteristics of the automated tools. Automated security artifacts too have various characteristics and form a category of automation. As such, trust in these artifacts needs to be calibrated.

Research in the fields such as automation and human factors has identified some salient calibrators—"error rate” as a calibrator for an automated route planner (De Vries et al. 2003), “accuracy” for an automated screener (Merritt et al. 2015a), and “reliability” for systems such as vehicle control system, automated signaling system, automatic decision aids system for detecting infight icing events (Chancey et al. 2017; Kraus et al. 2019; Lu and Sarter 2019; McGuirl and Sarter 2006; Stowers et al. 2020). Research in these fields has taken a focus on mechanistic approaches (e.g., experiments) and paid less attention to theory building and development. Additionally, IS research has overlooked the concept of trust calibration and its significance along with trust calibrators and their effects especially in the context of automated security IT with user choice. One exception is a study by Chen et al. (2018). The study examined differences in trust by manipulating the calibrators (e.g., reliability and feedback) of a phishingemail detection, without offering much theorization for its work.

In this study, we focus on phishing-website detections tools (referred to as detectors) as exemplars of automated security IT that allows users the choice for accepting or rejecting its advice. We rely on a theoretical framework—the ATR framework—to identify salient trust calibrators and to examine the consequences of calibrated trust in detectors. Hence, the critical components of ATR and their relationships guide the conceptualization of our research model. As trust calibration requires knowledge of trust calibrators and repeated use of the detector, we test our conceptualized model with data obtained from a complex controlled experimental design with repeated observations and exposures to trust calibrators.

## Theoretical Framework

IS research on trust in IT has relied on a variety of theories such as trust beliefs (ability, integrity, and benevolence) (e.g., Wang and Benbasat 2008), expectation disconfirmation theory (e.g., Lankton et al. 2015; Paravastu et al. 2014), and theory of reasoned action (e.g., Vance et al. 2008). Phishing-website detections tools are highly automated, work behind the scenes, and need trust calibration—features that trust theories in prior research do not address. We use

##

automation trust and reliance (ATR) as our theoretical framework because ATR focuses on the automated nature of security IT, draws a clear distinction between trust in automation and trust in humans, and provides an integrated perspective on trust calibration. We rely on the key components of ATR to identify the salient characteristics of phishing-website detection tools (as a specific category of automated security IT). According to ATR, users need to be informed about these characteristics for trust calibration process (Lee and See 2004).

ATR has three main components, as shown in Figure 1. The first component consists of the salient characteristics of the automation that calibrate trust. Calibrated trust is the result of trust evolution with the repeated use of the automation. This calibration depends on informing users of the salient characteristics (ex. via displays or prompts). The second main component of ATR consists of the outcomes of calibrated trust, such as intention formation and proper reliance on the automation (Lee and See 2004). The third component of ATR is contexts, including individual, organizational, and environmental contexts (Lee and See 2004).

In the first component, ATR identifies three characteristics of automation: performance, process, and purpose—called trust calibrators in this study. ATR argues that trust calibrators in automation are the counterparts of trust beliefs (ability, integrity, and benevolence) and that they become the antecedents of trust (Lee and See 2004). Performance describes what the automated tool can do. It demonstrates the ability of the automation including predictability, accuracy, and reliability. Process reveals the underlining mechanisms and operations of the automation. Process as an antecedent of trust shows the openness and integrity of the automation (Lee and See 2004). Purpose explains why the automation exists and reflects the developer’s intent and motivation. Purpose as a basis for trust shows how the automation intends to address users needs (Lee and See 2004). ATR empathizes the importance of displaying the key characteristics

of the automation to calibrate trust.

![](/api/attachments/4HJFE7F8/fulltext/images/f3355fc7b64a5d99394a5b06bafed4dfbdae77a2dcb8d597f02a252f11246837.jpg)  
Figure 1. The Framework of Automation Trust and Reliance (ATR) (Adapted from Lee and See (2004)).

The second component we draw from the ATR framework is the outcomes of calibrated trust, which include reliance, performance, and intention aligned with automation capability. Reliance refers to how users behaviorally depend on automatic aids. Performance shows the results of using the automation. Intention projects use in the near future.

The third component we draw from the ATR framework is the influence of contexts in trust calibration, such as individual, organizational, and environmental contexts (Lee and See 2004). Individual differences such as habit and past experience may influence trust in automation. Organizational contexts such as reputation, gossip, organizational structures, values, and norms play a role in trust formation. Environmental variables, such as the environment in which the

automation is used, also impact trust calibration (Lee and See 2004).

We rely on the three ATR components to formulate our model—(i) characteristics of automation as antecedents of calibrated trust; (ii) outcomes of calibrated trust including reliance and use; and (iii) automation contexts—individual and environmental. Organizational context was not used as the unit of analysis in this study is at the individual level.

ATR posits the dynamic of trust calibration in automation—trust evolves through this process in which the experience of using the automation provides feedback for trust calibration (Lee and See 2004). Following research in the fields of automation and human factors (Chen et al. 2018; De Vries et al. 2003; Hancock et al. 2011; Merritt et al. 2015b), we incorporate the dynamic of trust calibration in the process trust calibration through multiple experiences of using the security tool in two distinct domains (health and finance). We measure participants calibrated trust as their responses to the trust calibrators of the phishing-website detection tool after multiple experiences of using the tool in the experiment.

## Model of Trust Calibration for Phishing-Website Detection Tools

The critical components and their relationships in ATR form the theoretical foundation on which we conceptualize the trust calibration model for automated security IT in the context of phishingwebsite detection tools (the TC model) (see Figure 2). Briefly, the TC model shows the influence of trust calibrators on calibrated trust (H1-H3). H4-H7 capture the ATR-based outcomes of calibrated trust. The environmental context is captured through the moderation of domain type. Individual contextual factors are represented as control variables. Currently, the TC model focuses on how individual users respond to trust stimuli (i.e., calibrators) of the detector.

![](/api/attachments/4HJFE7F8/fulltext/images/25697c763e387c895d455f0c8c3dd46b7cc3be223790dd4277e8288fd6765415.jpg)  
Figure 2. Trust Calibration Model for Phishing-Website Detection Tools.

Performance: Detector AccuracyCalibrated Trust (H1). According to ATR, performance relates to what an automated tool does, including how reliably it can fulfill its expected purpose (Lee and See 2004). An important aspect of reliability is accuracy. Prior research indeed showed the effectiveness of accuracy as a performance-based trust calibrator (Dzindolet et al. 2002; Hoff and Bashir 2015). Accuracy-related assessment on automation was also found to play a critical role in shaping or reshaping users’ trust in automation (Madhavan and Wiegmann 2007). Users are less likely to ignore a highly-accurate automation aid when they are informed of the details regarding the aid’s performance (Dzindolet et al. 2002).

In reality, automated tools often cannot consistently produce perfect results, and users are keenly aware of this discrepancy. In certain contexts, users will discount automated tools despite high accuracy because of their misjudgment of the discrepancy (Madhavan and Wiegmann 2007; Madhavan et al. 2006). In the context of automated security IT, such misjudgment could happen more often as security is a secondary, background task to users (Dhamija et al. 2006) and

security tools generally provide very little performance information to users (West 2008). With little or no information to draw upon, users tend to make a quick, even impatient, judgment about performance. Explicit detection accuracy information allows users to make a more accurate judgment about the discrepancy and thus calibrate their trust.

In terms of phishing, the detection rates of commonly used state-of-the-art detection tools currently range from approximately 60% to 95% (Abbasi et al. 2015). For detectors in some popular browsers, given the advances in detection accuracy, we would expect very low clickthrough rates (Akhawe and Felt 2013). However, this is not the case (Akhawe and Felt 2013). We argue that users need to know the tool’s accuracy. When users are exposed to information about the detector’s accuracy, they can calibrate their trust accordingly. Hence, H1. Detector accuracy is positively associated with users’ calibrated trust in the detector.

Process: Detector Run-TimeCalibrated Trust (H2). The second trust calibrator in the ATR framework is process, which relates to how an automated tool functions (Lee and See 2004). A critical aspect of process is transparency of the tool’s mechanisms to users (Lee and See 2004). Although tools typically do not provide visible information regarding the details of the underlying analytical methods, users are often keenly aware of the run-time, particularly when the tool is perceived as slow. Run-time metrics are commonly used to assess credibility and performance for a wide range of automated tools, including phishing-websites detectors (Abbasi et al. 2010; Xiang et al. 2011). Nevertheless, run-time is often shown on the interface as a progress bar or circle that provides a symbolic indicator of process and visual feedback that the system is running and operating on the task. Improving run-time is a well-established way to improve user experience in terms of trust and satisfaction (Bouch et al. 2000).

##

Phishing-website detection tools use sophisticated machine learning algorithms, pattern matching, and various large datasets in their detection process. However, users do not have the expertise and time to assess details of tools’ methods. Detection tools often use a progress bar to indicate run-time, and thus run-time is the only aspect of a tool’s detection process that users directly experience and feel its impact when accessing websites. When the process is slow, users become annoyed and frustrated because the detector is a secondary operation working behind the scenes. Its slow operation can hinder users’ primary tasks (Jenkins et al. 2016). Slow run-time could even cause users to suspect that the system’s security is compromised and thus not trustworthy (Bouch et al. 2000; Hohenstein et al. 2016). The prolonged interruption (a long runtime) challenges users’ patience and potentially implies process inferiority to users of the tool. Hence,

## H2. Shorter detector run-time is positively associated with users’ calibrated trust in the detector.

Purpose: Outcome Severity Due to Wrong DecisionCalibrated Trust (H3a). The third trust calibrator in the ATR framework is purpose, which relates to why an automated tool exists (Lee and See 2004). A main purpose of security IT is to help users prevent and eliminate damaging consequences from security threats (Dinev and Hu 2007). If a security tool fails to accurately alert a user about a potential security threat, it fails to fulfill its intended purpose. Automation research shows that the potential outcomes from such failure are often costly and sometime even disastrous, leading to a decline in trust (Madhavan and Wiegmann 2007; McBride et al. 2014). Automation research also suggests that users tend to attribute the damage caused by their wrong decision to the automation, leading to trust reduction, even though they are ultimately responsible for the decision whether to heed the automation’s warning (Pop et al. 2015).

In our research context, the purpose of a phishing-website detector is to protect users from unwittingly visiting phishing sites. Failure to do so would result in users’ exposure to significant personal, professional, and/or financial risks such as identity theft or financial loss. If a phishingwebsite detector fails to accurately alert a user about a potential phishing site, it fails to fulfill its intended purpose. When the user follows the detector’s incorrect advice, the outcomes can be costly and thus not easily forgotten or forgiven (Abbasi et al. 2015). In fact, a single wrong decision can cause a long-lasting, biased view about the tool (Koepke et al. 2012).

Research has found that the cost of decision error influences users’ perceptions of a detection tool (Zahedi et al. 2015). When the severity of outcomes due to errors of an automated system increases, users’ trust in the system declines (Khasawneh et al. 2004; McBride et al. 2014). Applied to phishing-website detectors, we argue that if the outcome of a wrong decision is more severe, users form lower trust in the detector. Hence,

H3a. Outcome severity due to wrong decision is negatively associated with users’ calibrated trust in the detector.

Purpose: Type of ThreatCalibrated Trust (H3b). ATR argues that gaining a clearer understanding of the specific goal an automated tool is designed to achieve may lead users to place more proper trust in the tool (Lee and See 2004). Purpose-based information informs users about “the specific problem that the automation might have been designed to solve, as well as lower-level objectives that the automation was designed to meet” (Duez et al. 2006, p. 3). Thus, a deeper understanding of an automated tool’s purpose allows users to better determine if the tool meets their goals. This also allows users to foresee situations in which the tool might understandably fail (Duez et al. 2006; Lee and See 2004). As a result, users are able to place more appropriate trust in the tool (Duez et al. 2006; Lee and See 2004).

In terms of phishing-website detectors, although all automated detectors are to detect and protect users from visiting phishing websites, some detectors have a more limited purpose. For example, the purpose of eBay’s Account Guard toolbar is to detect spoof websites mimicking eBay. Other tools such as AZProtect and browsers’ built-in anti-phishing tools are multi-purpose and designed to detect both spoof and concocted websites in all domains (Abbasi et al. 2015; Reeder et al. 2018). Another example is that if a tool is designed to detect phishing websites in a specific language, it is unable to detect such phishing websites in other languages because it has no capabilities to properly parse other languages (Aaron and Rasmussen 2017). In general, many existing detectors focus on detecting a single type of phishing site, and their detection capabilities across both concocted and spoof sites are different (Abbasi et al. 2010).

Thus, the type of threat a detector handles (i.e., concocted and/or spoof) provides information about the detector’s specific purpose and the scope of its detection capabilities. As concocted and spoof sites use different deceptive tactics to defraud, users behave differently toward each type of threat and the detector targeting it (Abbasi et al. 2010; Grazioli and Jarvenpaa 2003). When facing a concocted site, users are often influenced by its aesthetic and professional appearance; in dealing with a spoof site, they judge its legitimacy based on their past experience with the legitimate counterpart. Providing the information of threat types affords users a deeper understanding of the detector and allows them to rationally adjust their expectations regarding the detector (Abbasi et al. 2010), as well as adjust their detection strategies based on the type of the phishing website they encounter. We argue that such understanding enables users to better calibrate their trust in the tool. Hence,

H3b. Type of threat is associated with users’ calibrated trust in the detector.

Outcomes: Calibrated TrustReliance on the Detector (H4). ATR argues that once the automated advisor is adopted, reliance on its advice depends on the extent of user trust (Lee and See 2004). Calibrated trust “guides reliance when complexity and unanticipated situations make a complete understanding of the automation impractical” (Lee and See 2004, p. 50). In other words, reliance is a behavior outcome of trust under uncertainty, making trust an antecedent of reliance on automation (Duez et al. 2006; Merritt 2011).

It has been observed that people often turn to manual control to reduce their reliance on the automatic system if they do not trust it (Elkins et al. 2013; Jensen et al. 2011; Lee and See 2004). In contrast, excessive, misplaced trust in automation may lead to over-reliance, which in turn leads to complacency, decreased vigilance, and less effort in monitoring automation performance. These findings show that calibrated trust is needed for an appropriate level of reliance (Culley and Madhavan 2013; Drnec et al. 2016; Parasuraman and Manzey 2010).

In the context of phishing website detection, a lack of trust in a detection tool can significantly reduce users’ reliance on its advice, causing them to turn to their own judgment when assessing the legitimacy of a website. This results in inadequate performance in detection of phishing websites (Reeder et al. 2018). Following this logic, we hypothesize,

Outcomes: Calibrated TrustFuture Use (H5). According to the ATR framework, another outcome of trust in automation is intention to use (Lee and See 2004). In the IS field, abundant empirical evidence has supported the relationship between trust and intentions in various contexts (e.g., Gefen et al. 2003; Lankton and McKnight 2011; McKnight et al. 2002; Song and Zahedi 2008; Vance et al. 2008). For example, trust has been found to be a predictor of technology acceptance intentions (Gefen et al. 2003), and trust in the IT artifact has also been found to be associated with intention to use the artifact (Lankton and McKnight 2011; Vance et al. 2008). Given that research has extensively documented the relationship between trust and intention to use, we argue that this relationship can also be applied to the current research context. Hence,

H5. Users’ calibrated trust in the detector is positively associated with their intention to use the detector in the future.

Outcomes: Reliance on the DetectorFuture Use (H6). ATR posits that reliance is the dependence exhibits inertia (Gao and Lee 2006). This means that present reliance and positive experiences with the automation can result in an intention to continue using it in the near future. Prior IS research has also demonstrated the link between current behaviors and continuance intentions (Kim et al. 2005). Additionally, reliance is based on trust beliefs surrounding automation performance, openness and integrity in process, and automation intent and motivation (Lee and See 2004). As long as these beliefs remain unbroken, reliance on automation will remain strong and use will continue (Lee and See 2004; Madhavan and Wiegmann 2007).

In the current research context, reliance is built upon calibrated trust that matches the capabilities of the detector. Thus, we argue that reliance will demonstrate inertia in that present positive interactions with the detector are a motivation of intention to use in the future. In other words, users tend to maintain their intention to use the detector if current reliance on the detector is properly established. Following this logic, we hypothesize,

H6. Users’ reliance on the detector’s advice is positively associated with their intention to use the detector in the future.

Outcomes: Reliance on the DetectorUser Performance (H7). ATR argues that proper reliance determined by calibrated trust is the key to improving user performance. Prior research has shown that humans are remarkably poor in detecting deceptions. In some circumstances, professionals and novices alike can achieve only slightly better detection accuracy than that of flipping a coin (Elkins et al. 2013; Jensen et al. 2010). As such, when automated tools have relatively high accuracy, humans are often the weak link in making correct decisions (Cranor 2008; Drnec et al. 2016). Their reliance on such tools could lead to better user performance in avoiding deception (Cranor 2008).

Phishing websites use deceptive tactics to lure in users by manipulating and misrepresenting cues that are present in many legitimate websites (Grazioli and Jarvenpaa 2003; Reeder et al. 2018). For instance, the visual appearance of a website, which can be easily manipulated, has been reported to be a prominent factor impacting users’ credibility judgment about the website (Reeder et al. 2018). Not surprisingly, users who rely solely on their own judgment and abilities routinely fail to identify 35% to 45% of phishing websites encountered, with misclassification rates as high as 70% in some instances (Dhamija et al. 2006; Jagatic et al. 2007). In contrast, state-of-the-art detection tools’ misclassification rates for phishing websites are only roughly 10% (Abbasi et al. 2015; Abbasi et al. 2010). Thus, relying on the tool’s advice results in better user performance (Akhawe and Felt 2013). Therefore, under the current research context, we expect that high reliance (resulting from a calibrated trust) leads to users’ higher ability to avoid phishing websites. Hence,

H7. Users’ reliance on the detector is positively associated with users’ performance in terms of their ability to avoid phishing websites.

Contextual Controls. ATR emphasizes the importance of the contextual controls in which trust is calibrated. Following this framework, we examine the environmental context for the phishing-website detectors by moderating domain type. Research has reported that context and domain play an important role in the implementation of behavioral theories (Whetten et al.

##

2009). For example, it is shown that domain has a significant effect on people’s disclosure of their private information online (Bansal et al. 2008). For this reason, we chose to test the model in two domains—online pharmacy and online banking. Phishing attacks are prevalent in both domains, causing users to suffer identity theft and monetary losses (Hellerman 2013). The two domains have distinct security risks. Purchasing drugs from online pharmacies carries a high risk of encountering concocted online pharmacies and counterfeit products (Greenberg 2008; Hellerman 2013). Online banking websites face more spoof attacks that attempt to directly defraud victims for financial gain (Aaron and Rasmussen 2017) .

Finally, ATR recognizes the importance of controlling for individual contextual factors that influence calibrated trust (Lee and See 2004). Thus, we include age, gender, education, security habit, and past encounters with phishing websites as the individual context.

## Research Methodology

We conducted a between-subject controlled lab experiment using a phishing-website detection tool (detector). The experiment consisted of a 2 (threat domain: bank vs. pharmacy) x 2 (type of threat: spoof vs. concocted) x 2 (accuracy of detector: high [90%] vs. low [60%]) x 2 (run-time of detector: fast [1s] vs. slow [4s]) x 2 (outcome severity due to wrong decision: high [\$10] vs. low [\$1]) full-factorial design with a total of 32 conditions.

We created an inventory that contains the clones of 15 spoof, 15 concocted, and 15 legitimate websites for each domain. We collected phishing websites from reputable sources (e.g., LegitScript, PhishTank) and legitimate websites using a spidering program that preserved the original link structure, content, and images of the websites of the legitimate companies. To avoid company-size bias, the inventory included an equal number of large, medium, and small companies for the 15 legitimate websites.

##

Before the experiment, participants were informed of the experimental procedures and trained about the key concepts such as threat types (spoof vs. concocted) and detection accuracy (the percentage of all websites that are correctly classified) so that they would have a clear understanding of the goal and purpose of the detector and the type of threat they could encounter. Participants then completed a pre-experiment survey about their past experiences, security habits, and other relevant questions. To simulate a real condition, participants received mon

In the experiment, participants were randomly assigned five legitimate and five phishing (either spoof or concocted) websites and asked to perform a task according to their assigned domain (either the online pharmacy domain or the online bank domain). Hence, they had ten opportunities (10 trials) to use the detector and calibrate their trust in the detector.

ATR posits that exposure to salient trust calibrators is critical in trust calibration (Lee and See 2004). Research has shown that explicitly providing real-time confidence levels helped calibrate users’ trust in automation aids (Hoff and Bashir 2015). Thus, in the experiment, participants were explicitly informed of the accuracy, run-time, and outcome severity of a wrong decision by a display on the top of screen during the entire period of the experiment. Figure 3 shows the interface of the experiment with the links to the 10 assigned websites along with the information of the trust calibrators on the top bar (see the yellow highlights in Figure 3).

![](/api/attachments/4HJFE7F8/fulltext/images/686ec7d03bd34d3dfd0e293b0775e05e24b7cbf0b59b5305ee8c3dfd41641acb.jpg)  
Figure 3. Experiment Interface with Information on Trust Calibrators.

When participants click a link, the detector shows the progress bar for 1 or 4 seconds and then delivers the detection outcome. For the run-time, we used a progress bar to visually show the time it took to run the detector in the background. While the labexperiment method permits designs that deviate from real experiences, we chose to preserve the realism in our experimental design by using a progress bar. The progress bar communicated the run-time information in a familiar and easily understandable way to the participants without distracting them from their main tasks. Figure 4-Panel A shows an example of the warning to participants when a website was detected as a phishing site, while Figure 4-Panel B shows that participants directly accessed the webpage without any warning block when a website is classified as legitimate. In doing so, we ensured participants’ trust was calibrated by the trust calibrator information displayed on Figure 3 and by their repeated interactions with the tool.

![](/api/attachments/4HJFE7F8/fulltext/images/022fcafb83a3abc777f81d720279c9c0149936c9c684b070315d730e6671a9b0.jpg)  
Figure 4. Detection Outcome Examples.

We informed participants of their detection performance after the participants finished with the 10 repeated trials and before answering the post-experiment questions. We used this design because, in reality, security detection tools are not 100% accurate and cannot give immediate feedback on the correctness of users’ decisions. People also do not see the consequences (e.g., identity theft) of detection errors right away. Additionally, if we provided performance feedback after each trial to participants, they could have guessed the correctness of the detection outcome during the remaining trials.

All participants performed a domain-related task. In the online pharmacy domain, the experimental task was to purchase Rogaine, a popular over-the-counter hair restoration drug. This product was chosen because it is familiar and carried by most online pharmacies. Moreover, counterfeit Rogaine is often sold by phishing websites. In the online bank domain, the experimental task was to open an online saving account, which is a basic function provided by most online banks. This task is relevant as providing personal and financial information to a phishing bank website poses great risk of financial loss and identity theft. Regardless of domain, participants had to make a series of decisions about each website they encountered, including whether to visit or browse the website, whether they considered the website legitimate or phishing and whether they would transact with the website (see Figure 3). Visiting and browsing behavior during the experiment was measured using web analytics software that tracked users’ clicks. This experiment design also allowed participants to have multiple interactions with the detector for appropriate trust calibration.

All participants started with a cash box of \$100 (hypothetical money). Every time they made a wrong decision, they would lose money (\$1 or \$10, depending on threat severity). Visiting a phishing website was also penalized as a wrong decision as visiting such a website carries the risk of being victimized by malware and other security threats (Koepke et al. 2012). Participants were compensated with a uniform base plus extra compensation depending on the money left in their cash box. This performance-dependent compensation was designed to increase the motivation of participants to perform well in the experiment. A final performance score for each participant was computed based on all their decisions regarding their 10 assigned websites. Based on the final scores, participants were paid a minimum of \$10 and a maximum of \$30 or extra credit for their participation (depending upon their preferences). The experiment was conducted using a Java-based software tool specifically developed for this study. Appendix C provides additional details on the experiment protocol and the role of the Java tool in administrating the protocol.

After the experiment, participants were informed of their detection performance. They then completed a post-experiment survey consisting of manipulation checks and perceptual questions.

Overall, this full-factorial, controlled lab experiment design allowed us to directly establish the causality between trust calibrators and calibrated trust. We randomly varied the levels of tool capability (and other calibrators) assigned to each participant, while fully controlling for other sources of variation. Each participant learned about the trust calibrators of the tool assigned to them from the start, made his/her detection dections based on what he/she was informed, and

was compensated depending on his/her security protection performance. We measured calibrated trust as well as the outcome variables at the end to capture the causality between trust calibrators and calibrated trust and its consequences.

## Scale Development and Data Collection

To ensure validity whenever possible, measurement scales of the constructs in the TC model were adopted from existing literature. In addition, all items were converted to semantic differential scales to ensure content validity and reduce the threat of common method bias (Chin et al. 2008; Podsakoff et al. 2003). The items for calibrated trust in the detector were selfdeveloped based on Bansal et al. (2010), Gefen et al. (2003), and Madsen and Gregor (2000). In the fields such as automation and human factors, most studies on trust calibration use a 5- or 7- point scale (Chen et al. 2018; De Vries et al. 2003; Merritt et al. 2015b) or short version of 3- item construct adopted from the trust literature to measure calibrated trust (e.g., Kraus et al. 2019). This is to reduce frustration of the participants in the face of multiple trials in the studies. Those studies also suggest that such a measure is able to capture calibrated trust after subjects interact with the stimuli/calibrators of the automation manipulated in research (Hancock et al. 2011). In the IS field, three dimensions of competence/functionality, integrity/reliability, and benevolence/helpfulness are used to measure trust beliefs in various contexts. Considering the practice in these research fields, we used three items to measure calibrated trust. In detail, the item of “not reliable at all/very reliable for sure” is based on the reliability dimension for trust in (Madsen and Gregor 2000), the item of “not dependable at all/very dependable for sure” is based on the technical competence dimension for trust in Madsen and Gregor (2000) and the opportunistic/dependable dimension for trust in Gefen et al. (2003) and Bansal et al. (2010), and the item of “not trustworthy at all/very trustworthy for sure” is based on honesty/benevolence

dimension in Gefen et al. (2003) and Bansal et al. (2010). Intention items to use the detector in the future were adapted from Davis et al. (1989). Finally, the items for reliance on the detector were adapted from Davis et al. (1989) and Venkatesh (2003). All the latent constructs are reflective.

Participants’ ability to detect phishing websites was measured objectively by evaluating participants’ decisions for each of their assigned websites in terms of: 1) avoiding to visit the phishing website (i.e., heeding the warning); 2) clicking the link to open the phishing website homepage but avoiding to browse it; 3) correctly identifying it as a legitimate or phishing website; and 4) avoiding transactions with the phishing website. Each participant was scored as a percentage of correct decisions. Accuracy, run-time, outcome severity of wrong decision, and type of threat were manipulated, and the corresponding information was provided to participants in the experiment.

In terms of controls, the items for security habit were adopted from Pavlou and Fygenson (2006), and the items for past encounters with phishing websites and familiarity with domain were developed in this study. Appendix D contains the definition of constructs and the sources used for their measurement. Appendix E reports the instrument.

The construct items, experiment protocol, and experiment instructions were pretested and pilot-tested. We recruited subjects from multiple groups—university students at a Midwestern university, staff, faculty and the community. In order to reach the community, we posted flyers and placed ads on social media (e.g., Craigslist). We also used the word-of-mouth approach to recruit participants from local communities. The recruitment resulted in a total of 865 participants. Appendix F reports the participant profiles. Participants’ education ranged from no degree to doctoral degree, with 72% falling in the “some college/college student” category. This category had the highest percentage of daily Internet use. The age of participants ranged from 18 to above 58 years, with 88% falling in 18-25 age category. Gender distribution was 62% male and 38% female.

The Internet-use data in the U.S. for 2019 shows that 100% young adults between the age of 18-29 are Internet users<sup>1</sup> and are the highest users of social media.<sup>2</sup> Young adults with some most vulnerable to website-phishing attacks. Indeed, research shows that college students frequently fall victim to various online threats including phishing (Goel et al. 2017). Additionally, research has found that the results from student samples are consistent with those from the public panel (Steelman et al. 2014). Thus, we consider our sample to be suitable for testing the model.

## Analysis and Results

Prior to validating our trust calibration (TC) model, we conducted a series of analyses to check our experiment manipulations, trust calibration, and construct validity. First, we performed a series of ANOVAs on the manipulated variables based on participants’ responses to our manipulation check questions. The questions asked participants to validate their assigned level of detector accuracy, run-time, and outcome severity in the experiment.<sup>4</sup> As shown in Appendix G, all the ANOVA tests were significant, indicating that our manipulations were successful.

Second, we assessed whether participants calibrated their trust during the experiment. Specifically, we collected data on participants’ disagreement with the detector’s

recommendations about whether a website was safe to visit. We examined how participants adjusted their disagreement during the 10 trials in two groups: high accuracy (i.e., the detector with 90% accuracy) and low accuracy (i.e., 60% accuracy) groups. Here, disagreement refers to situations where the participant deemed the website to be legitimate and the detector considered it to be a phishing, or vice versa. Figure 5 shows the range as well as the mean percentage of disagreement rates (y-axis) for each of the 10 websites encountered by participants in the 10 repeated trails. The mean is presented as a dot, and the range is shown as a vertical bar. The xaxis depicts the order in which the participant made his/her final decision (e.g., 1=the first trial) The chart on the right shows percentage disagreement rates for participants in the high accuracy group. The chart on the left shows disagreement rates for those in the low accuracy group.

![](/api/attachments/4HJFE7F8/fulltext/images/549f5c598b0e6749b03f30332b8b9666346e00c1be67d84ea54dc6376a1b1e1d.jpg)

![](/api/attachments/4HJFE7F8/fulltext/images/beb611ffbde4fe779d74e4ba3097009c4d93df95fddba600ed28bd7e289c2075.jpg)  
Figure 5: User Percentage Disagreement with Detector by Trial.

In the low accuracy group, the range of disagreement rate was 23%-33% with a mean of 28% in the first trial. The disagreement rate steadily increased over the trials. By the $1 0 ^ { \mathrm { t h } }$ trial, the range was 33%-44% with a mean of 38%. Hence, the results indicate that participants’ trust in the detector was calibrated over the 10 trials.

In the high accuracy group, the range of disagreement rate started at 15%-24% with a mean of 20% at the first trial, fluctuated over the trials, and at the end remained in a similar range— 20%-28% with a mean of 19%. Given that the sequence of safe vs. unsafe websites was random and varied for each participant, the presence of warnings about unsafe websites varied for each participant. Such variations could cause small random fluctuations. These results shed light on how users’ trust was calibrated during the experiment, albeit at an aggregate level.

Third, we assessed construct reliability, as reported in Table 2. All alpha values were above the threshold of .70 (Nunnally and Bernstein 1978), composite factor reliability (CFR) values were greater than the cutoff value of .70 (Segars 1997), and the average variance extracted (AVE) values were above the threshold of .50 (Segars 1997), providing support for construct reliability. In addition, we conducted exploratory factor analyses (EFAs) to assess convergent and discriminant validities of our experimental constructs, including controls.

As reported in Appendix H, all items loaded on their respective constructs as expected, with all loadings greater than .85 and no cross loadings greater than .40. These results support the convergent and discriminant validity of our constructs (McKnight et al. 2002).

Table 2. Construct Reliability Checks

<table><tr><td rowspan="2">Constructs</td><td colspan="3">Pharmacy</td><td colspan="3">Bank</td></tr><tr><td>Cronbach&#x27;s α</td><td>CFR</td><td>AVE</td><td>Cronbach&#x27;s</td><td>CFR</td><td>AVE</td></tr><tr><td>Calibrated trust in the detector</td><td>0.97</td><td>0.97</td><td>0.92</td><td>0.97</td><td>0.97</td><td>0.92</td></tr><tr><td>Reliance on detector</td><td>0.94</td><td>0.96</td><td>0.86</td><td>0.94</td><td>0.96</td><td>0.87</td></tr><tr><td>Intention to use in the future</td><td>0.98</td><td>0.98</td><td>0.95</td><td>0.98</td><td>0.98</td><td>0.94</td></tr><tr><td>Past encounters with phishing site</td><td>0.88</td><td>0.89</td><td>0.74</td><td>0.91</td><td>0.91</td><td>0.78</td></tr><tr><td>Security habit</td><td>0.95</td><td>0.95</td><td>0.87</td><td>0.96</td><td>0.96</td><td>0.88</td></tr></table>

We also compared the square root of the AVE for each construct with its correlations with all correlation values with the other constructs, as reported in Table 3. The results lend further credence to the discriminant validity of our constructs.

Table 3. Construct Correlations and Comparison with Square Root of AVEs

<table><tr><td>Constructs (Pharmacy)</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1. Past encounters with phishing</td><td> $0.86^a$ </td><td></td><td></td><td></td><td></td></tr><tr><td>2. Security habit</td><td>-0.01</td><td>0.93</td><td></td><td></td><td></td></tr><tr><td>3. Calibrated trust in the detector</td><td>-0.01</td><td>-0.03</td><td>0.93</td><td></td><td></td></tr><tr><td>4. Reliance on detector</td><td>-0.02</td><td>-0.06</td><td>0.51</td><td>0.96</td><td></td></tr><tr><td>5. Intention to use in the future</td><td>-0.02</td><td>-0.04</td><td>0.45</td><td>0.74</td><td>0.98</td></tr><tr><td>Constructs (Bank)</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1. Past encounters with phishing</td><td>0.88</td><td></td><td></td><td></td><td></td></tr><tr><td>2. Security habit</td><td>0.03</td><td>0.94</td><td></td><td></td><td></td></tr><tr><td>3. Calibrated trust in the detector</td><td>0.01</td><td>0.06</td><td>0.93</td><td></td><td></td></tr><tr><td>4. Reliance on detector</td><td>0.03</td><td>0.12</td><td>0.48</td><td>0.96</td><td></td></tr><tr><td>5. Intention to use in the future</td><td>0.02</td><td>0.09</td><td>0.46</td><td>0.75</td><td>0.97</td></tr></table>

The square root values of the AVEs are reported in boldface on the diagonal.

To counter the possibility of common method variance (CMV), we collected perceptual data both before and after the experiment. We also developed the instrument items using semantic differential scales. Moreover, we incorporated an objective variable in the model—ability to detect phishing websites—which was likely to further reduce the threat of CMV. It is worth noting that, in the EFA analysis, no single factor emerged as dominant. Finally, we used a marker variable in our instrument to purify our data prior to analysis (Bagozzi 2011; Podsakoff et al. 2003). The purified data was used in our model estimation to partial-out any potential CMV (Bagozzi 2011; Podsakoff et al. 2003). With all these remedies, we believe that CMV did not pose a major threat to this study.

We used the structural equations modeling (SEM) as the estimation method due to the fact that the TC model has multiple latent variables and accounts for a number of simultaneous equations involving antecedents, consequents, and control variables of calibrated trust. We used SEM Group analysis in MPlus software. This SEM Group method allows for further simultaneity by estimating the two domains (online pharmacy and online bank) as two distinct groups in the same estimation process. This controls for any dependency that may exist across equations and groups. The estimation method for both the measurement model and the TC model was the mean-adjusted maximum likelihood (MLM) method in MPlus. MLM adjusts the estimations for non-normality in the data. Appendix I reports the factor loadings in the measurement model. All factor loadings were above .80 with significant t-statistics and high $\mathbf { R } ^ { 2 }$ values, providing further support for the discriminant and convergent validity of the constructs. Fit indices of the measurement model are reported in the second column of Table 4.

Table 4. Fit Indices for the Measurement Model and TC Model Estimations

<table><tr><td>Fit Index</td><td>Measurement Model</td><td>TC Model</td><td>Threshold*</td></tr><tr><td>Normed  $\chi^{2}$ </td><td>1.19</td><td>1.68</td><td>&lt;3</td></tr><tr><td>CFI (Comparative Fit Index)</td><td>0.997</td><td>0.986</td><td>&gt;0.90</td></tr><tr><td>TLI (Tucker-Lewis Index)</td><td>0.997</td><td>0.984</td><td>&gt;0.90</td></tr><tr><td>RMSEA (Root Mean Square Error of Approximation)</td><td>0.021</td><td>0.040</td><td>&lt;0.06</td></tr><tr><td>SRMR (Standardized Root Mean Square Residual)</td><td>0.021</td><td>0.051</td><td>&lt;0.10</td></tr><tr><td colspan="4">*(Gefen et al. 2011)</td></tr></table>

All values fell within the desired thresholds and supported the model fit. Moreover, the two groups contributed equally to the estimated chi-square, indicating equal fit. We also tested and successfully confirmed measurement invariance between the two groups (Doll et al. 1998).

The estimation of the TC model also had satisfactory fit indices, as shown in the third column of Table 4. The two groups had approximately equal contributions to the chi-square domains.

Figure 6 shows the estimated TC model, reporting path coefficients, p-values, and $\mathbf { R } ^ { 2 }$ values. The top values in Figure 6 are for the online pharmacy domain, and the bottom values are for the $\mathbf { R } ^ { 2 }$ values of the endogenous variables in the model were statistically significant in both domains, showing that the TC model had reasonable explanatory power. The TC model estimation supported our conceptual model: all hypotheses were statistically significant in both domains, with the exception of H2 in both domains and H3b in the bank domain.

![](/api/attachments/4HJFE7F8/fulltext/images/904dbd76394122ff45f9fa173b9618b981f44cd8d2e505ed6168955baf9b4857.jpg)  
Figure 6. Estimated Trust Calibration Model.

Hypothesis H1, the influence of the trust calibrator—detector accuracy—on trust in the detector, was supported in both online pharmacy and online bank domains, with path coefficients of .28 in the online pharmacy and .31 in the online bank domain. Surprisingly, hypothesis H2 was not supported as run-time speed had no significant calibrating impact on trust in the detector.

Hypothesis H3a was supported in both domains such that more severe outcomes reduced calibrated trust. Hypothesis H3b was partially supported. In the online pharmacy domain, users showed significant differences in calibrated trust based on type of threat.

With respect to H4 and H5, our findings demonstrated that calibrated trust was positively associated with users’ reliance on the detector’s advice (H4) and intention of future use (H5), with high path coefficient values across both domains. H4 had path coefficients of .52 (pharmacy) and .49 (bank), and H5 had path coefficients of .69 (pharmacy) and .70 (bank).

Hypotheses H6 and H7 postulated the influence of reliance on future use intention and on users’ ability to detect phishing websites. Both hypotheses were supported across both domains, with path coefficients of .09 (pharmacy) and .12 (bank) in H6 and path coefficients of .41 (pharmacy) and .38 (bank) in H7.

Of the control variables, security habit had a significant positive impact on trust in the detector in the online bank domain only, with a path coefficient of .13 and $\mathrm { p } { < } 0 . 0 1$ , indicating that security habit has a lock-in effect—users habitually act based on prior knowledge. One possible reason that security habit was not significant in the online pharmacy domain is that our participants were relatively young and likely healthy, meaning they had less experience with online pharmacies. Familiarity with domain had significant positive effects on calibrated trust in the detector in the online pharmacy domain—with a path coefficient of .14 and $\mathsf { p } { < } 0 . 0 1$ . The results showed that those who were more familiar with the online pharmacy domain trusted more in the detector. Finally, gender was significantly associated with trust in the detector in the online pharmacy domain—with a path coefficient of .15 and p <0.01—in that female participants showed higher trust. Age, education, and past encounters with phishing websites showed no significant effects on calibrated trust.

## Discussion

We developed the trust calibration model for detectors (the TC model) by using the automation trust and reliance (ATR) framework as a kernel theory (Lee and See 2004). The focus was calibrated trust and its antecedents (trust calibrators H1-H3) and consequents (reliance, observed user performance, and future intention to use H4-H7).

Trust Calibrators. Regarding the first set of hypotheses, we found that Hypothesis H1 was fully supported. The results showed that tool accuracy as a performance-based trust calibrator (i.e. informing users of it) was significant across both online pharmacy and online bank domains, with users showing greater trust when the tool accuracy was 90% than when it was 60%. This finding underscores the point that users need to be informed about the accuracy of automated tools to prevent their misjudgment on the capability of tools and consequent improper trust and improper reliance (Merritt et al. 2015b). Using accuracy as a trust calibrator is particularly important for automated security IT that detects and eliminates security threats, such as anti phishing software, as users have consistently shown a predilection to ignore such tools even when the tool’s accuracy is high (Abbasi et al. 2015).

According to Hypothesis H2, we expected that tool run-time—a process-based trust calibrator—would also influence the level of trust that users placed in the tool. This hypothesis was not supported in either of the two domains. There are several possible explanations for this finding. It is possible that the difference between the one-second and four-second delay was not sufficient for users to consider run-time to be a concern. Another explanation is that users may follow different rationales to interpret run-time depending on how they understand the complexity of the detection task carried out by the tool. For example, a slow run-time may be interpreted as 1) the tool’s algorithm being complex and needing a longer time to process or 2) the tool being poorly developed and therefore inefficient and slow. The third explanation is that when users have security in mind, they may be willing to tolerate a few seconds of delay. Lastly, it is also possible that users attribute the delay to other factors, such as a slow Internet or web server, instead of to the detector.

Hypothesis H3a was fully supported across both domains. Our results confirmed outcome severity as a purpose-based trust calibrator—more severe outcomes are associated with greater decreased trust in the tool than less severe outcomes. This finding is important as users often ignore tool warnings despite the fact that the cost of a single security incident may be exceedingly high (Abbasi et al. 2015). In an effort to create proper tool reliance, designers of automated security IT artifacts need to spend additional effort making users aware of the magnitude of risk associated with ignoring tool warnings. The design of security warnings should draw broadly from the literature across domains, including findings on how best to display viscerally aversive warnings (Black et al. 2017). With such design, we could impr users’ understanding of their decision outcome in the context of automated security I

In accordance with Hypothesis H3b, we found that users in the online pharmacy domain showed greater trust in the detector for concocted websites than for spoof websites, while users in the online banking domain showed no significant difference in trust based on type of threat. This finding suggests that users may tend to trust the detector more in detecting concocted than spoof phishing websites within certain domains. One possible explanation for this is that in unfamiliar domains, users do not have a well-known legitimate online entity they can reference when detecting a concocted site. Consequently, they may rely more on the tool and less on themselves to assess the credibility of the novel website as they have less existing information to draw upon.

Comparing the standardized path coefficients in the estimated TC model, we found the effects of our antecedent trust calibrators on trust are different based on the relevant path loadings (see Figure 6). Detector accuracy and outcome severity have higher path coefficients and are more effective trust calibrators than detector run-time and threat type. This finding implies that when users assess the key characteristics of automated security IT to form trust, their assessment is based more on the performance (accuracy) and purpose (outcome severity due to wrong decision) calibrators than the process calibrators. Designers of automated security IT

artifacts would benefit from the design of warning displays that emphasize the most effective trust calibrators, which in our case are performance and purpose calibraators. Designers may also benefit from designs that provide users with information on the most effective trust calibrators to build their proper trust.

We also examined the effect size of trust calibrators on calibrated trust for those significant paths and found that the effect size (f<sup>2</sup>) values ranged from 0.015 to 0.115 (see Appendix J). A 30-year review on effect size (Aguinis et al. 2005) shows that the median observed effect size (f<sup>2</sup>) is .002. Thus, we argue that our trust calibrators are effective in calibrating trust with the above median effect size.

Finally, we conducted a post hoc analysis on the interaction effect of trust calibrators on calibrated trust and found no significant interaction effect.

Outcomes. With regard to the latter four hypotheses concerning the effects of calibrated trust on user performance outcomes, all found support within the TC model across both online pharmacy and online banking domains. First, the findings from H4 and H5 confirmed the strong positive association between trust in the detector and reliance on it and between trust in the detector and future intention to use it. Along with the findings from H1-H3, the significance of hypotheses H4 and H5 underscores the utility and value of the TC model: with proper antecedent trust calibrators in place, it is possible to change users’ security behaviors and ensure their from trust calibratorscalibrated trust in detector reliance on and use of detector. These findings highlight that trust in the detector is a central conduit that connects trust calibrators to desirable user behavior and improved tool performance. The findings also imply that designers of automated security IT need to be transparent about their tools and manage users’ mental

models to foster their proper understanding of security IT characteristics. Otherwise, users tend to be self-reliant even when the automated tool outperforms them (Abbasi et al. 2015).

We conducted a post hoc analysis to validate the mediating role of calibrated trust in bridging trust calibrators and desirable outcomes from the detector. We used the bootstrapping mediation test in Mplus for the analysis (Muthén and Muthén 2012). As shown in Appendix K, all mediating effects were significant when the path from the trust calibrator to calibrated trust was significant. The findings further confirm the effects of the trust calibrators and the central role of calibrated trust.

Phishing website detection tools are known to suffer from disuse and suboptimal performance even when the tool’s accuracy is high (Abbasi et al. 2015; Chen et al. 2011; Reeder et al. 2018; Symantec 2010). Thus, to change users’ security behaviors and increase their reliance on the advice of tools, it is critical that tool designers effectively improve trust calibrators and inform users about them. In this respect, our study answers a call for research on “active exploration for trusting” (AET), a methodology that promotes frequent trust calibration and enables trust calibration from an ante hoc perspective (Hoffman et al. 2013). We may need more empirical and analytical methods to identify users’ inappropriate trust and ongoing misuse or disuse behaviors in a timely manner so that we can promptly initiate the trust calibration process.

Reliance on the tool has two important positive consequences: future intention to use (H6) and an observed increase in user performance (H7). Comparing the standardized path coefficients in Figure 6, we found that reliance on the detector leads to higher user performance in avoiding phishing websites compared to a weaker path coefficient of future intention to use. This finding is interesting, as it reveals the tenuous nature of human-to-automation interactions.

While human-to-human interactions with positive outcomes may lead to strong loyalty (Zahedi et al. 2010), human-to-automation interactions do not benefit from the emotional bonds found in interpersonal relationships. When it comes to users’ reliance on automated tools, today’s acceptance of advice does not necessarily translate into future use. Any misjudgment developed during usage could break prior established trust. This finding is a microcosm of a larger problem with enterprise security: while security managers are constantly looking to upgrade existing security IT artifacts and add new ones, they also have to continually increase employees’ security awareness and motivation to use security tools and comply with security policies (Chen et al. 2013). According to a Gartner survey (2017), enterprise security expenditures increased an estimated 8% each year since 2016 due to the persistent threat landscape and more high-profile cyberattacks. Our findings suggest that increasing expenditures with the goal of having more advanced automated security systems including detection systems may be just one pillar required to achieve strong security. Routinely educating employees and calibrating their trust in such systems for proper use and reliance may be a second key pillar.

Another positive consequence of reliance on the detector is users’ improved ability to detect phishing websites, per H7. People generally perform poorly when it comes to detecting deception, and individuals are particularly ill-equipped to detect phishing websites (Abbasi et al. 2015; Dhamija et al. 2006). Our findings regarding H7, combined with the findings from H1-H4, provide holistic support and value for the TC model: calibrated trust based on carefully selected trust calibrators can improve users’ detection capabilities.

Specifically, we have shown an important pathway that could lead to increased tool performance: carefully identified and employed trust calibratorscalibrated trustproper reliance on tool adviceimproved users’ ability to avoid phishing websites.

##

Figure 7 further illustrates this pathway for participants using the 90% accurate detector (averaged across the three antecedent trust calibrators of accuracy, severity of decision outcome, and run-time). We divided participants into quartiles based on their calibrated trust (measured on a scale of 1-10). Panel A in Figure 7 shows the histogram of calibrated trust with the top quartile (top 25%) in solid-line columns (green color) and the bottom quartile (bottom 25%) in dash-line columns (peach color). Panel B compares the tool reliance of the top and bottom trusting quartiles. Our calculations showed that 78% of the top-quartile users (solid line) reported high use of the tool as compared to only 26% of the bottom-quartile users (dash-line). Here, we define ‘high use’ as an average of 7 or greater on a 1-10 scale. Panel C shows the distribution of participants’ agreement with detector for the top (solid line) and bottom (dashline) quartiles. Likewise, we found the most trusting users (top quartile) were generally 20% to 25% more likely to agree with and heed the tool’s recommendations regarding spoof and concocted websites associated with either domain based on objective performance data.

Panel D shows participants’ performance for the top and bottom quartiles. Our computation showed that compared to the least trusting users (bottom quartile), the most trusting users (top quartile) were 23% less likely to visit phishing websites, 22% less likely to browse multiple pages on them, 38% less likely to consider phishing websites legitimate, and 39% less willing to transact with phishing websites. Collectively, Figure 7 panels demonstrate our key points when applied to high performing tools (e.g., 90% accuracy): users’ trust in detector tools should be calibrated, users’ calibrated trust aligns with the tools’ performance, and calibrated trust leads to increased users’ reliance on the tool and better ability to avoid threats.

![](/api/attachments/4HJFE7F8/fulltext/images/6437975ec9082a665ab231bcb084d562e7ce3e9c800c2aef1f36642f74058b4f.jpg)  
Figure 7. Appropriate Trust – Impact of Trust in Detector on Reliance and Performance.

## Theoretical and Practical Implications

This study has significant theoretical and practical implications as discussed below.

Theoretical Implications. This study makes several contributions to IS research. First, this study contributes to IS literature on trust in security IT. By identifying phishing-website security tools as a type of automated security IT with user choice, this study introduces calibrated trust as a type of trust that needs to be calibrated by the trust calibrators to align with the capability of detection tools. Prior research in other fields such as human factors has long recognized the significance of this concept in automation, including in new automated systems (e.g., adaptive cruise control) (Kraus et al. 2019; Lu and Sarter 2019; Stowers et al. 2020). However, IS research has been silent about trust calibration in security IT. Our study is a significant addition to IS research in trust and opens an avenue for the theory-based research in this area.

##

Second, this study argues for a theory-guided trust calibration for automated security IT, and applies the key theme of automation trust and reliance (ATR) framework into the context of phishing-website detection tools as exemplars of automated security IT. To the best of our knowledge, the ATR framework has not been applied to the IS field, especially to the automated security IT research. The contextualization of this theory to the study of automated security IT provides a new theoretical foundation for future research in this area (Chen and Zahedi 2016; Karjalainen et al. 2019; Whetten et al. 2009). Through the contextualization, we propose a theoretical model for trust calibration for phishing-website detection tools (referred to as the TC model). The TC model contributes to theory in several ways. It identifies salient antecedent trust calibrators that are necessary for users to form an appropriate degree of trust in an automated security detection tool. It provides a theoretical basis for the need to inform users about salient trust calibrators to promote an appropriate level of users’ trust in detection tools. It provides insight into consequent performance outcomes of properly calibrated trust, including tool reliance, future usage intentions, and improved detection performance. It builds a theoretical foundation for trust calibration in the context of automated security IT. More importantly, it presents a key pathway from identifying and employing trust calibrators of a security tool, to calibrating proper user trust in the tool, to achieving desirable performance outcomes. Thus, the contextualization of ATR and the resulting TC model are significant theoretical contributions to trust research, especially trust research in security IT.

Third, the empirical validation of the TC model also contributes to IS research. More importantly, the study provides empirical evidence that we can calibrate trust in the context of automated security IT that allows users to make final decisions. With this evidence in hand, this study highlights “calibratability” of trust in security IT, an area that has not received much

attention from IS researchers.

Lastly, the TC model can be used to guide the investigation of trust and trust calibration for other security tools and systems. More specifically, the TC model can serve as a theoretical model to guide the selection of proper calibrators for trust calibration in other security IT artifacts and validate their effectiveness. In addition, the TC model may be applied to other automated detection tools and systems for trust calibration, such as deception detection systems (Proudfoot et al. 2016) and automated interviewing systems (Pentland et al. 2017). Detection accuracy of such tools and systems is well below 100%, and thus a proper level of trust needs to be established for increased human-automation performance.

Practical Implications. This study addresses a call for research in the relationships between trust and IT in general and between trust and automated security IT in particular (Gefen et al. 2008; McKnight et al. 2011). As shown in Figure 7, while using the tool with the same accuracy, users demonstrated significant differences in trust and detection performance. Thus, when designing automated security IT artifacts, designers must inform users of trust calibrators, particularly the tools’ detection accuracy rate. An implementation method, we suggest to deliver trust calibrator information to users through warning messages (see Panel A in Figure 4). Warning science suggests that an effective warning text may consist of four types of message information: a signal word, description of the threat, potential negative consequences, and instructions on how to avoid the hazard (Black et al. 2017). The information on trust calibrators can be part of the instruction information of warning messges devlivered by the detector. Designers can carefully design warnings and their displays to create calibration effects and keep users in the feedback loop when using the detector. Vendors of detection tools with a high detection rate can gain a business edge by publicizing their high detection rates via finding

effective ways to communicate them to their customers in use of the tool.

The results of this study also have important implications for IT managers, Chief Information Officers (CIOs), and Chief Security Officers (CSOs) tasked with enterprise security. Based on findings pertaining to the TC model, organizations must consider together the following two avenues of their security practice:

1. Adopting accurate security systems/tools with effective trust calibration features whenever possible. In the context of phishing website detection, benchmarking studies show that state-ofthe-art tools are approximately 95% accurate, including proprietary and enterprise-grade tools (Abbasi et al. 2015; Ding et al. 2019; Sahingoz et al. 2019). Relatively low accuracy can be found in some automated systems dealing with complex decisions and tasks (Strickland 2019). Moreover, even with a highly accurate but “imperfect” automated system, users still demonstrate low performance due to unjustified trust and reliance (Akhawe and Felt 2013). Thus, when investing in high performance security systems/tools, organizations need to understand the subjective nature of trust in automated security IT and consider adopting state-of-the art security systems/tools with built-in design features that facilitate trust calibration as much as possible. For example, it may be worth preferring tools that provide “visible” feedback to users when necessary (e.g., when detecting a high click-through rate and low reliance). Ultimately, the key is to allow the user to establish an appropriate level of trust in the tool that is consistent with its capabilities.

2. Allocating resources for education and training programs about security and trust calibration of security systems/tools. Academics and practitioners both agree that removing users entirely from the security loop sometimes is impractical, particularly in the context of phishing website detection (Cranor 2008). Based on our findings regarding the TC model, organizations

need to appreciate the importance of trust calibration and allocate resources for security training and education programs that highlight the performance, process, and purpose of security systems/tools to foster employees’ better understanding of automated security tools capabilities—a fundamental prerequisite for establishing an appropriate level of trust in automated tools. Security education and training programs should not only enhance knowledge pertaining to security threats such as phishing websites, but endorse a solution- and tool-centric training paradigm in which trust calibration is purposefully incorporated. The TC model can serve as an evaluative model to assess the effectiveness of such training.

Our work also has implications for experts and individual users. Our work has highlighted the importance of trust calibrators for increased use and protection against phishing websites. Security experts need to increase their focus on detailed reviews of security detections tools in terms of trust calibrators. In order to increase their protection performance, individuals should insist on having the detailed information about trust calibrators and give preference to vendors who provide such information.

## Limitations and Future Research Directions

There are limitations in this study. Although we conducted our experiment in two distinct domains—online pharmacies and online banks—care should be taken when generalizing our results to other domains. In addition, our participants interacted with a complex and customwritten detection tool (by the necessity of controlled experimental design) instead of interacting with a well-known existing program or plug-in. Further care should be taken to consider possible influences of tool brand names and participants’ varying experiences and prior knowledge of such tools. Moreover, this study was conducted in the U.S., and our sample consisted mainly of young participants. Research should replicate our work with data from other countries and older

##

populations. Moreover, calibrated trust can fluctuate under different conditions, and can change along with long-term interactions with the system (Hoff and Bashir 2015; Hoffman et al. 2013; Kraus et al. 2019; Lee and See 2004). It would be of interest to examine how calibrated trust fluctuates as a result of experiencing loss due to attacks and other events while using the tools. Future research needs to develop measures specific to calibrated trust in the context of automated security tools. Furthermore, for the sake of realism, we used a progress bar to visualize run-time, representing the tool’s process. More work is needed to identify additional proxies for the inner processes of detection tools, including alternative methods of informing users about the detector’s run-time, such as a progress bar with text information, animation, or other visualization methods.

Our research opens several new research avenues. First, the TC model demonstrates the importance of identifying proper trust calibrators. As shown in our results, not all calibrators exhibited significant calibrating effects. In our case, the tool’s performance-based feature of accuracy and its purpose-based feature of decision outcome severity are more influential calibrators than the other two calibrators. Thus, more research may be needed to understand the difference in effect size of trust calibrators by addressing the following research question: Do all trust calibrators exhibit the same (or similar) calibrating effects on automated security IT artifacts that perform different tasks or have different levels in user control? Answering this question would help further strengthen our understanding within the TC model framework.

Second, there is no endpoint to trust calibration, and trust evolves over time (Hoff and Bashir 2015; Kraus et al. 2019). Researchers need to investigate how trust in automated security IT with user choice changes in response to personal and social events and experiences. Additionally, once a disuse behavior or overuse behavior has already occurred, it is often too late to change the damaging effects of the behavior via trust calibration (Drnec et al. 2016). Therefore, finding ways to identify a user’s misplaced trust and the best time to calibrate/recalibrate it to build and maintain an appropriate level of trust remains a challenging research question that warrants an answer (Hoff and Bashir 2015; Hoffman et al. 2013). Indeed, finding the optimal level of trust is also a research challenge (Hoffman et al. 2013). Moreover, finding an effective way to convey the information about trust is another interesting topic for future research.

Further, finding an effective way to convey the information of trust calibrators of a security tool to users (e.g., through security warnings) is also an important topic. Both warning sciences and Lee and See (2004) suggest that where, how, and when to display such information could influence the effect of trust calibration. The design of the interface and placement of the trust calibrators constitute important areas for further research.

Another direction for future research is to evaluate the TC model in alternate domains such as social media, which is increasingly being targeted by phishing attacks and has important strategic implications for organizations that use it for internal communication (e.g., Slack) or customer engagement and support (e.g., Twitter). Moreover, this study focuses on individual users without exploring trust calibrators related to other external contexts—such as organizational and cultural contexts. Future research may also consider investigating the trust calibration effects on security IT in such contexts.

Finally, it would also be beneficial to explore the influence of different IT platforms on security behavior and trust calibration of security IT, such as mobile computing, cloud computing, and other platforms. In all these cases, the TC model may provide a clear path for conducting future research along these avenues.

## Author Statement

All persons who meet authorship criteria are listed as authors, and all authors certify that they have participated sufficiently in the work to take public responsibility for the content, including participation in the concept, design, analysis, writing, or revision of the manuscript. Furthermore, each author certifies that this material or similar material has not been and will not be submitted to or published in any other publication before its appearance in Information and Management journal.

## Acknowledgement

The research was supported through a grant from the National Science Foundation's Secure and Trustworthy Computing program: CNS-1049497. We would also like to thank our partners at McAfee Security for their invaluable feedback on the constructs, experiment design, survey instrument, and data analysis.

## References

1. Aaron, G., and Rasmussen, R. Global phishing survey: Trends and domain name use in 2016. APWG. 2017, June 26. Available at

https://docs.apwg.org/reports/APWG\_Global\_Phishing\_Report\_2015-2016.pdf. (accessed on August 18, 2018).

2. Abbasi, A., Zahedi, F., and Chen, Y. Impact of anti-phishing tool performance on attack success rates. Intelligence and Security Informatics (ISI), 2012 IEEE International Conference on: IEEE, 2012, pp. 12-17.

3. Abbasi, A., Zahedi, F., Zeng, D., Chen, Y., Chen, H.C., and Nunamaker, J.F. Enhancing predictive analytics for anti-phishing by exploiting website genre information. Journal of Management Information Systems, 31, 4 (2015), 109-157.

4. Abbasi, A., Zhang, Z., Zimbra, D., Chen, H., and Nunamaker, J.F. Detecting fake websites: The contribution of statistical learning theory. MIS Quarterly, 34, 3 (2010), 435-461.

5. Aguinis, H., Beaty, J.C., Boik, R.J., and Pierce, C.A. Effect size and power in assessing moderating effects of categorical variables using multiple regression: A 30-year review. Journal of Applied Psychology, 90, 1 (2005), 94-107.

6. Akhawe, D., and Felt, A.P. Alice in warningland: A large-scale field study of browser security warning effectiveness. USENIX Security Symposium, 2013.

7. Anderson, B.B., Vance, A., Kirwan, C.B., Eargle, D., and Jenkins, J.L. How users perceive and respond to security messages: A neurois research agenda and empirical study. European Journal of Information Systems, 25, 4 (2016), 364-390.

9. Bagozzi, R.P. Measurement and meaning in information systems and organizational research: Methodological and philosophical foundations. MIS Quarterly, 35, 2 (2011), 261-292.

10. Bansal, G., Zahedi, F., and Gefen, D. The moderating influence of privacy concern on the efficacy of privacy assurance mechanisms for building trust: A multiple-context investigation. the International Conference on Information Systems (ICIS), Paris, France, 2008.

11. Bansal, G., Zahedi, F., and Gefen, D. The impact of personal dispositions on information sensitivity, privacy concern and trust in disclosing health information online. Decision support systems, 49, 2 (2010), 138-150.

12. Black, A., Luna, P., Lund, O., and Walker, S. Information design: Research and practice. Routledge, 2017.

13. Bouch, A., Kuchinsky, A., and Bhatti, N. Quality is in the eye of the beholder: Meeting users requirements for internet quality of service. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, The Hague, Netherlands ACM, 2000, pp. 297-304.

14. Bravo-Lillo, C., Komanduri, S., Cranor, L.F., Reeder, R.W., Sleeper, M., Downs, J., and Schechter, S. Your attention please: Designing security-decision uis to make genuine risks harder to ignore. Proceedings of the Ninth Symposium on Usable Privacy and Security: ACM, 2013.

15. Cavusoglu, H., and Raghunathan, S. Configuration of detection software: A comparison of decision and game theory approaches. Decision Analysis, 1, 3 (2004), 131-148.

16. Chancey, E.T., Bliss, J.P., Yamani, Y., and Handley, H.A. Trust and the compliance–reliance paradigm: The effects of risk, error bias, and reliability on trust and dependence. Human Factors, 59, 3 (2017), 333-345.

17. Chen, J., Mishler, S., Hu, B., Li, N., and Proctor, R.W. The description-experience gap in the effect of warning reliability on user trust and performance in a phishing-detection context. International Journal of Human-Computer Studies, 119 (2018), 35-47.

18. Chen, Y., Ramamurthy, K., and Wen, K.W. Organizations' information security policy compliance: Stick or carrot approach? Journal of Management Information Systems, 29, 3 (2013), 157- 188.

19. Chen, Y., and Zahedi, F.M. Individuals' internet security perceptions and behaviors: Polycontextual contrasts between the united states and china. MIS Quarterly, 40, 1 (2016), 205-222.

20. Chen, Y., Zahedi, F.M., and Abbasi, A. Interface design elements for anti-phishing systems. International Conference on Design Science Research in Information Systems: Springer, 2011, pp. 253- 265.

21. Chin, W.W., Johnson, N., and Schwarz, A. A fast form approach to measuring technology acceptance and other constructs. MIS Quarterly, 32, 4 (2008), 687-703.

23. Cranor, L.F. A framework for reasoning about the human in the loop. the Conference on Usability, Psychology, and Security, Berkeley, CA, 2008.

24. Culley, K.E., and Madhavan, P. Trust in automation and automation designers: Implications for hci and hmi. Computers in Human Behavior, 6, 29 (2013), 2208-2210.

25. Cyr, D. Modeling web site design across cultures: Relationships to trust, satisfaction, and eloyalty. Journal of Management Information Systems, 24, 4 (2008), 47-72.

27. Davis, F.D., Bagozzi, R.P., and Warshaw, P.R. User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35, 8 (1989), 982-1003.

28. De Vries, P., Midden, C., and Bouwhuis, D. The effects of errors on system trust, self-confidence, and the allocation of control in route planning. International Journal of Human-Computer Studies, 58, 6 (2003), 719-735.

29. Dhamija, R., Tygar, J.D., and Hearst, M. Why phishing works. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Montreal, Canada: ACM, 2006, pp. 581-590.

30. Dinev, T., and Hu, Q. The centrality of awareness in the formation of user behavioral intention toward protective information technologies. Journal of the Association for Information Systems, 8, 7 (2007), 386-408.

31. Ding, Y., Luktarhan, N., Li, K., and Slamu, W. A keyword-based combination approach for detecting phishing webpages. Computers & Security, 84 (2019), 256-275.

32. Doll, W.J., Hendrickson, A., and Deng, X. Using davis's perceived usefulness and ease‐ of‐ use instruments for decision making: A confirmatory and multigroup invariance analysis. Decision Sciences, 29, 4 (1998), 839-869.

33. Drnec, K., Marathe, A.R., Lukos, J.R., and Metcalfe, J.S. From trust in automation to decision neuroscience: Applying cognitive neuroscience methods to understand and improve interaction decisions involved in human automation interaction. Frontiers in Human Neuroscience, 10 (2016), 290.

34. Duez, P.P., Zuliani, M.J., and Jamieson, G.A. Trust by design: Information requirements for appropriate trust in automation. Proceedings of the 2006 Conference of the Center for Advanced Studies on Collaborative Research: IBM Corp., 2006.

35. Dzindolet, M.T., Pierce, L.G., Beck, H.P., and Dawe, L.A. The perceived utility of human and automated aids in a visual detection task. Human Factors, 44, 1 (2002), 79-94.

36. Elkins, A.C., Dunbar, N.E., Adame, B., and Nunamaker, J.F. Are users threatened by credibility assessment systems? Journal of Management Information Systems, 29, 4 (2013), 249-261.

38. FBI. Business email compromise the \$26 billion scam. 2019. Available at https://www.ic3.gov/media/2019/190910.aspx. (accessed on Feburary 18, 2020).

39. Frauenstein, E.D., and Flowerday, S. Susceptibility to phishing on social network sites: A personality information processing model. Computers & Security (2020), 101862.

40. Gao, J., and Lee, J.D. Extending the decision field theory to model operators' reliance on automation in supervisory control situations. IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans, 36, 5 (2006), 943-959.

41. Gartner. Gartner forecasts worldwide security spending will reach \$96 billion in 2018, up 8 percent from 2017. 2017, December 7. Available at https://www.gartner.com/newsroom/id/3836563. (accessed on January, 8, 2018).

43. Gefen, D., Benbasat, I., and Pavlou, P. A research agenda for trust in online environments. Journal of Management Information Systems, 24, 4 (2008), 275-286.

44. Gefen, D., Karahanna, E., and Straub, D.W. Trust and tam in online shopping: An integrated model. MIS Quarterly, 27, 1 (2003), 51-90.

45. Gefen, D., Rigdon, E.E., and Straub, D. An update and extension to sem guidelines for administrative and social science research. MIS Quarterly, 35, 2 (2011), Iii-Xiv.

46. Glikson, E.G., and Woolley, A.W. Human trust in artificial intelligence: Review of empirical research. Academy of Management Annals, 14, 2 (2020).

47. Goel, S., Williams, K., and Dincelli, E. Got phished? Internet security and human vulnerability. Journal of the Association for Information Systems, 18, 1 (2017), 22-44.

48. Grazioli, S., and Jarvenpaa, S.L. Consumer and business deception on the internet: Content analysis of documentary evidence. International Journal of Electronic Commerce, 7, 4 (2003), 93-118.

49. Greenberg, A. Pharma’s black market boom. Forbes.com. 2008, August 26. Available at https://www.forbes.com/2008/08/25/online-pharma-scams-tech-securitycx\_ag\_0826drugscam.html#140e76d8e709. (accessed on May 8, 2018).

50. Hancock, P.A., Billings, D.R., Schaefer, K.E., Chen, J.Y., De Visser, E.J., and Parasuraman, R. A meta-analysis of factors affecting trust in human-robot interaction. Human Factors, 53, 5 (2011), 517- 527.

51. Hellerman, C. Fda shuts down 1,677 online pharmacies. CNN. 2013, June 23. Available at https://www.cnn.com/2013/06/27/health/online-pharmacies-closed/index.html. (accessed on May 8, 2018).

52. Hoff, K.A., and Bashir, M. Trust in automation: Integrating empirical evidence on factors that influence trust. Human Factors, 57, 3 (2015), 407-434.

53. Hoffman, R.R., Johnson, M., Bradshaw, J.M., and Underbrink, A. Trust in automation. IEEE Intelligent Systems, 28, 1 (2013), 84-88.

54. Hohenstein, J., Khan, H., Canfield, K., Tung, S., and Perez Cano, R. Shorter wait times: The effects of various loading screens on perceived performance. Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems: ACM, 2016, pp. 3084-3090.

55. Jagatic, T.N., Johnson, N.A., Jakobsson, M., and Menczer, F. Social phishing. Communications of the ACM, 50, 10 (2007), 94-100.

56. Jenkins, J.L., Anderson, B.B., Vance, A., Kirwan, C.B., and Eargle, D. More harm than good? How messages that interrupt can make us vulnerable. Information Systems Research, 27, 4 (2016), 880- 896.

57. Jensen, M.L., Lowry, P.B., Burgoon, J.K., and Nunamaker, J.F. Technology dominance in complex decision making: The case of aided credibility assessment. Journal of Management Information Systems, 27, 1 (2010), 175-201.

58. Jensen, M.L., Lowry, P.B., and Jenkins, J.L. Effects of automated and participative decision support in computer-aided credibility assessment. Journal of Management Information Systems, 28, 1 (2011), 201-233.

59. Karjalainen, M., Sarker, S., and Siponen, M. Toward a theory of information systems security behaviors of organizational employees: A dialectical process perspective. Information Systems Research, 30, 2 (2019), 687-704.

60. Khasawneh, M.T., Bowling, S.R., Jiang, X., Gramopadhye, A.K., and Melloy, B.J. Effect of error severity on human trust in hybrid systems. Proceedings of the Human Factors and Ergonomics Society Annual Meeting: SAGE Publications Sage CA: Los Angeles, CA, 2004, pp. 439-443.

61. Kim, S.S., Malhotra, N.K., and Narasimhan, S. Two competing perspectives on automatic use: A theoretical and empirical comparison. Information Systems Research, 16, 4 (2005), 418-432.

62. Koepke, J., Kaza, S., and Abbasi, A. Exploratory experiments to identify fake websites by using features from the network stack. Intelligence and Security Informatics (ISI), IEEE International Conference on: IEEE, 2012, pp. 126-128.

63. Kraus, J., Scholz, D., Stiegemeier, D., and Baumann, M. The more you know: Trust dynamics and calibration in highly automated driving and the effects of take-overs, system malfunction, and system transparency. Human Factors (2019), 0018720819853686.

64. Lankton, N.K., and McKnight, D.H. What does it mean to trust facebook?: Examining technology and interpersonal trust beliefs. ACM SIGMIS Database: the DATABASE for Advances in Information Systems, 42, 2 (2011), 32-54.

65. Lankton, N.K., McKnight, D.H., and Tripp, J. Technology, humanness, and trust: Rethinking trust in technology. Journal of the Association for Information Systems, 16, 10 (2015), 880-918.

66. Lankton, N.K., McKnight, D.H., Wright, R.T., and Thatcher, J.B. Using expectation disconfirmation theory and polynomial modeling to understand trust in technology. Information Systems Research, 27, 1 (2016), 197-213.

67. Lee, J.D., and See, K.A. Trust in automation: Designing for appropriate reliance. Human Factors, 46, 1 (2004), 50-80.

68. Li, L., Berki, E., Helenius, M., and Ovaska, S. Towards a contingency approach with whitelistand blacklist-based anti-phishing applications: What do usability tests indicate? Behaviour & Information Technology, 33, 11 (2014), 1136-1147.

69. Lu, Y., and Sarter, N. Eye tracking: A process-oriented method for inferring trust in automation as a function of priming and system reliability. IEEE Transactions on Human-Machine Systems, 49, 6 (2019), 560-568.

70. Madhavan, P., and Wiegmann, D.A. Similarities and differences between human–human and human–automation trust: An integrative review. Theoretical Issues in Ergonomics Science, 8, 4 (2007), 277-301.

71. Madhavan, P., Wiegmann, D.A., and Lacson, F.C. Automation failures on tasks easily performed by operators undermine trust in automated aids. Human Factors, 48, 2 (2006), 241-256.

72. Madsen, M., and Gregor, S. Measuring human-computer trust. 11th Australasian Conference on Information Systems, Sydney, Australia: Citeseer, 2000, pp. 6-8.

73. McBride, S.E., Rogers, W.A., and Fisk, A.D. Understanding human management of automation errors. Theoretical Issues in Ergonomics Science, 15, 6 (2014), 545-577.

74. McGuirl, J.M., and Sarter, N.B. Supporting trust calibration and the effective use of decision aids by presenting dynamic system confidence information. Human Factors, 48, 4 (2006), 656-665.

75. McKnight, D.H., Carter, M., Thatcher, J.B., and Clay, P.F. Trust in a specific technology: An investigation of its components and measures. ACM Transactions on Management Information Systems (TMIS), 2, 2 (2011), 12.

76. McKnight, D.H., Choudhury, V., and Kacmar, C. Developing and validating trust measures for ecommerce: An integrative typology. Information Systems Research, 13, 3 (2002), 334-359.

77. Merritt, S.M. Affective processes in human–automation interactions. Human Factors, 53, 4 (2011), 356-370.

78. Merritt, S.M., Lee, D., Unnerstall, J.L., and Huber, K. Are well-calibrated users effective users? Associations between calibration of trust and performance on an automation-aided task. Human Factors, 57, 1 (2015a), 34-47.

79. Merritt, S.M., Unnerstall, J.L., Lee, D., and Huber, K. Measuring individual differences in the perfect automation schema. Human Factors, 57, 5 (2015b), 740-753.

81. Muthén, L.K., and Muthén, B.O. Mplus user’s guide. Los Angeles, CA: Muthén & Muthén, 2012.

82. Nunnally, J.C., and Bernstein, I.H. Psychometric theory. New York: McGraw Hill, 1978.

83. Parasuraman, R., and Manzey, D.H. Complacency and bias in human use of automation: An attentional integration. Human Factors, 52, 3 (2010), 381-410.

84. Parasuraman, R., Sheridan, T.B., and Wickens, C.D. A model for types and levels of human interaction with automation. IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans, 30, 3 (2000), 286-297.

85. Paravastu, N., Gefen, D., and Creason, S.B. Understanding trust in it artifacts: An evaluation of the impact of trustworthiness and trust on satisfaction with antiviral software. ACM SIGMIS Database: the DATABASE for Advances in Information Systems, 45, 4 (2014), 30-50.

86. Pavlou, P.A., and Fygenson, M. Understanding and predicting electronic commerce adoption: An extension of the theory of planned behavior. MIS Quarterly, 30, 1 (2006), 115-143.

87. Pentland, S.J., Twyman, N.W., Burgoon, J.K., Nunamaker, J.F., and Diller, C.B.R. A video-based screening system for automated risk assessment using nuanced facial features. Journal of Management Information Systems, 34, 4 (2017), 970-993.

88. Podsakoff, P.M., MacKenzie, S.B., Lee, J.-Y., and Podsakoff, N.P. Common method biases in behavioral research: A critical review of the literature and recommended remedies. Journal of Applied Psychology, 88, 5 (2003), 879.

89. Pop, V.L., Shrewsbury, A., and Durso, F.T. Individual differences in the calibration of trust in automation. Human Factors, 57, 4 (2015), 545-556.

90. Proudfoot, J.G., Jenkins, J.L., Burgoon, J.K., and Nunamaker, J.F. More than meets the eye: How oculometric behaviors evolve over the course of automated deception detection interactions. Journal of Management Information Systems, 33, 2 (2016), 332-360.

91. Reeder, R.W., Felt, A.P., Consolvo, S., Malkin, N., Thompson, C., and Egelman, S. An experience sampling study of user reactions to browser warnings in the field. Proceedings of the 2018 CHI conference on human factors in computing systems, 2018, pp. 1-13.

92. RiskIQ. The evil internet minute 2019. Available at https://www.riskiq.com/infographic/evilinternet-minute-2019/. (accessed on May 10, 2020).

93. Sahingoz, O.K., Buber, E., Demir, O., and Diri, B. Machine learning based phishing detection from urls. Expert Systems with Applications, 117 (2019), 345-357.

94. Schaefer, K.E., Chen, J.Y., Szalma, J.L., and Hancock, P.A. A meta-analysis of factors influencing the development of trust in automation: Implications for understanding autonomy in future systems. Human Factors, 58, 3 (2016), 377-400.

95. Segars, A.H. Assessing the unidimensionality of measurement: A paradigm and illustration within the context of information systems research. Omega, 25, 1 (1997), 107-121.

96. Song, J., and Zahedi, F. Dynamics of trust revision: Using health infomediaries. Journal of Management Information Systems, 24, 4 (2008), 225-248.

97. Steelman, Z.R., Hammer, B.I., and Limayem, M. Data collection in the digital age: Innovative alternatives to student samples. MIS Quarterly, 38, 2 (2014), 355-378.

98. Stowers, K., Kasdaglis, N., Rupp, M.A., Newton, O.B., Chen, J.Y., and Barnes, M.J. The impact of agent transparency on human performance. IEEE Transactions on Human-Machine Systems (2020).

99. Strickland, E. How ibm watson overpromised and underdelivered on ai health care. 2019. Available at https://spectrum.ieee.org/biomedical/diagnostics/how-ibm-watson-overpromised-andunderdelivered-on-ai-health-care. (accessed on May 10, 2020).

100. Symantec. The norton cybercrime report: The human impact 2010. Available at

https://www.symantec.com/content/en/us/home\_homeoffice/media/pdf/cybercrime\_report/Norton\_USA-Human%20Impact-A4\_Aug4-2.pdf. (accessed on December 8, 2018).

102. Vance, A., Elie-Dit-Cosaque, C., and Straub, D.W. Examining trust in information technology artifacts: The effects of system quality and culture. Journal of Management Information Systems, 24, 4 (2008), 73-100.

103. Vance, A., Jenkins, J.L., Anderson, B.B., Bjornn, D.K., and Kirwan, C.B. Tuning out security warnings: Alongitudinal examination of habituation through fmri, eye tracking, and field experiments. MIS Quarterly, 42, 2 (2018), 355-380.

104. Venkatesh, V., Morris, M.G., Davis, G.B., and Davis, F.D. User acceptance of information technology: Toward a unified view. MIS Quarterly, 27, 3 (2003), 425-478.

106. Wang, W.Q., and Benbasat, I. Attributions of trust in decision support technologies: A study of recommendation agents for e-commerce. Journal of Management Information Systems, 24, 4 (2008), 249- 273.

107. West, R. The psychology of security. Communications of the ACM, 51, 4 (2008), 34-40.

108. Whetten, D.A., Felin, T., and King, B.G. The practice of theory borrowing in organizational studies: Current issues and future directions. Journal of Management, 35, 3 (2009), 537-563.

109. Whittaker, Z. Google let scammers post a perfectly spoofed amazon ad in its search results. ZDNet. 2017. Available at http://www.zdnet.com/article/malicious-google-ad-pointed-millions-to-fakewindows-support-scam/. (accessed on March 8, 2019).

110. Whitten, A., and Tygar, J.D. Why johnny can't encrypt: A usability evaluation of pgp 5.0. USENIX Security Symposium, 1999.

111. Xiang, G., Hong, J., Rose, C.P., and Cranor, L. Cantina+: A feature-rich machine learning framework for detecting phishing web sites. ACM Transactions on Information and System Security (TISSEC), 14, 2 (2011), 21.

112. Zahedi, F.M., Abbasi, A., and Chen, Y. Fake-website detection tools: Identifying elements that promote individuals' use and enhance their performance. Journal of the Association for Information Systems, 16, 6 (2015), 448-484.

113. Zahedi, F.M., Bansal, G., and Ische, J. Success factors in cooperative online marketplaces: Trust as the social capital and value generator in vendors-exchange relationships. Journal of Organizational Computing and Electronic Commerce, 20, 4 (2010), 295-327.

## Author Biography

Yan Chen is an associate professor at the Florida International University. She has received her doctoral degree from University of Wisconsin-Milwaukee. Her research focuses on information security, online fraud, security management, privacy, and e-business. She has published more than 30 referred research papers in academic journals and conference proceedings, including MIS Quarterly, Journal of Management Information Systems, Journal of the Association for Information Systems, Information & Management, and others. She is a recipient of research scholarships and best paper award nominees. She is a member of the Association for Information Systems and has been serving as a reviewer for many IS journals and conferences, including MIS Quarterly, Information Systems Research, Journal of Management Information systems, Decision Sciences, Information & Management, and others.

Fatemeh Mariam Zahedi is University of Wisconsin-Milwaukee Distinguished Professor Emerita at the Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee. She received her doctoral degree from Indiana University. Her research focus has been on IT at the service of individuals. Her present areas of research include web-based systems design and issues including trust, security, privacy, culture, loyalty, personalized intelligent interface, web-based healthcare, and web analytics for health. She has served as senior editor and associate editor of MIS Quarterly, editorial board of JMIS, and AE of ISR. She has published more than 120 referred papers in premier journals and conferences, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Management Science, DSS, Information & Management, IEEE Transactions on Software Engineering, Operations Research, IEEE Transactions on Systems, Man, and Cybernetics, IIE Transactions, and Review of Economics and Statistics, and others. She has been the PI of grants funded by NSF and other agencies. She is the author of two books in Quality Information Systems and Intelligent Systems for Business: Expert Systems with Neural Network. She has received several research, teaching, and best paper awards. Her work has been featured on TV and in print media. The list of Professor Zahedi’s publications is available on her Google Scholar profile.

Ahmed Abbasi is the Joe and Jane Giovanini Endowed Chaired Professor in the Department of IT, Analytics, and Operations in the Mendoza College of Business at the University of Notre Dame. He attained his B.S. and MBA degrees from Virginia Tech and a Ph.D. from the Artificial Intelligence Lab at the University of Arizona. His research interests relate to human-centered analytics, text mining, health, and security. He has published over 90 articles in top journals and conferences, including MIS Quarterly, Journal of Management Information Systems, ACM Transactions on Information Systems, IEEE Transactions on Knowledge and Data Engineering, and IEEE Intelligent Systems. His projects on cyber security, health analytics, and social media have been funded by the National Science Foundation and various industry partners, including AWS, Microsoft Research, and Oracle. He received the IBM Faculty Award, IEEE Technical Achievement Award, and INFORMS Design Science Award for his research on novel applications of machine learning. He has also received best paper awards from MIS Quarterly, the Association for Information Systems, and the Workshop on Information Technologies and Systems. He serves as senior editor at Information Systems Research and associate editor for ACM Transactions on MIS and IEEE Intelligent Systems. His work has been featured in several media outlets, including the Wall Street Journal, Associated Press, WIRED, and CBS.

David Dobolyi is an assistant research professor in the Mendoza College of Business at the University of Notre Dame. He received his Ph.D. in Cognitive Psychology from the University of Virginia, and his primary research interests involve predictive analytics, computer vision, and behavioral experiments, with recent applications including cybercrime and health. He has published in top journals including Science and the Journal of Management Information Systems, and his publications span a broad range of topics including reproducibility in science and the fusion of psychometric and secondary data for user modeling.
