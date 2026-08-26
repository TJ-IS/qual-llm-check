---
otero_id: 5112
otero_key: "EGR62QQJ"
title: "Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance"
authors: "Mario Silic; Paul Benjamin Lowry"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1705512"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance

Mario Silic & Paul Benjamin Lowry

To cite this article: Mario Silic & Paul Benjamin Lowry (2020) Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance, Journal of Management Information Systems, 37:1, 129-161, DOI: 10.1080/07421222.2019.1705512

To link to this article: https://doi.org/10.1080/07421222.2019.1705512

![](/api/attachments/EGR62QQJ/fulltext/images/284b6077285cd7b6af3bdc2d7f01a500c81cbea4b9fed1d458cc3a4bcbeb3819.jpg)

View supplementary material

![](/api/attachments/EGR62QQJ/fulltext/images/d3b0a3c6e382e28cbf3525a4323c30b715681135c3cc7e4a2ad3d75e9e5b3081.jpg)

Published online: 01 Mar 2020.

![](/api/attachments/EGR62QQJ/fulltext/images/494afcc3d5b54bebcc7dae2cd2e0b2e0f33033f19aaee4cf0a61581985020205.jpg)

Submit your article to this journal

![](/api/attachments/EGR62QQJ/fulltext/images/ff69f6491299e948ba4ea5e4f206d67d0e06f46515ff3738e93d4530c2578ab7.jpg)

View related articles

![](/api/attachments/EGR62QQJ/fulltext/images/652d2f21bf8e8d6846a14abec948484660f328a475b4966fbb8031077d938316.jpg)

View Crossmark data

Check for updates

# Using Design-Science Based Gami<sup>fi</sup>cation to Improve Organizational Security Training and Compliance

Mario Silic<sup>a</sup> and Paul Benjamin Lowry <sup>b</sup>

<sup>a</sup>Institute of Information Management, University of St. Gallen, St. Gallen, Switzerland; <sup>b</sup>Department of Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, VA, USA

## ABSTRACT

We conducted a design-science research project to improve an organization’s compound problems of (1) unsuccessful employee phishing prevention and (2) poorly received internal security training. To do so, we created a gami<sup>fi</sup>ed security training system focusing on two factors: (1) enhancing intrinsic motivation through gami<sup>fi</sup>cation and (2) improving security learning and e<sup>fi</sup>cacy. Our key theoretical contribution is proposing a recontextualized kernel theory from the hedonic-motivation system adoption model that can be used to assess employee security constructs along with their intrinsic motivations and coping for learning and compliance. A six-month <sup>fi</sup>eld study with 420 participants shows that ful<sup>fi</sup>lling users’ motivations and coping needs through gami<sup>fi</sup>ed security training can result in statistically signi<sup>fi</sup>cant positive behavioral changes. We also provide a novel empirical demonstration of the conceptual importance of “appropriate challenge” in this context. We vet our work using the principles of proof-of-concept and proof-of-value, and we conclude with a research agenda that leads toward <sup>fi</sup>nal proof-in-use.

## KEYWORDS

computer security; gami<sup>fi</sup>cation; design science research; hedonic motivation; system adoption model; immersion; <sup>fl</sup>ow; security compliance; security education; training; awareness; SETA

## Introduction

Information technology (IT) security compliance deals with techniques and processes that motivate employees to behave more securely when engaging with organizational systems and information [cf. 14]. Such compliance is of increasing concern for management and executives because of the global explosion of organizational security issues. Generally, IT security compliance has three objectives: (1) to mitigate or avoid security incidents and risks often caused by negligent employees [22, 65, 102], (2) to thwart criminal security behavior and computer abuse [65, 101, 102], and (3) to encourage prosocial and protective security behaviors in employees [45, 84]. A number of promising studies have applied various techniques to motivate employees to adopt secure intentions and behavior — from deterrence techniques [26, 101, 102] and discouraging employee neutralization [e.g., 91] to increasing the awareness of the risks and potential costs of noncompliance [e.g., 14], to increasing accountability [94, 95], to leveraging positive psychology or a<sup>f</sup>ect [15, 28], and even using more explicit threats and fear appeals [11, 52, 83]. Despite these e<sup>f</sup>orts, employees remain the “weakest link” in organizational IT security because employee behavior can easily undermine it [102]; moreover, it is ultimately the employees’ responsibility to comply, and they often do not [22, 83].

Understandably, researchers have questioned whether extant organizational security approaches are e<sup>fi</sup>cacious. For example, deterrence techniques were designed for criminal behavior and may be inappropriate for security policy noncompliance [26, 102]. Techniques that employ threats and intensi<sup>fi</sup>ed risks can have unintended consequences, including negative employee reactance [63, 65].

In contrast, security education, training, and awareness (SETA) programs can leverage a more positive approach. SETA programs aim to provide employees with the knowledge and motivation necessary to comply with security policies when confronted with a security risk [21]. However, it is evident that many of the current compliance-related training approaches are relatively ine<sup>f</sup>ective; many employees continue to be noncompliant [102]. This is troubling, as SETA programs have long been considered fundamental to organizational security governance, and despite repeated calls to address this promising research area, researchers have not examined how to make SETA programs more e<sup>f</sup>ective, with a few promising exceptions [e.g., 21].

Employee training is notorious for failing, as even though it often delivers the right content, employees often lack the motivation to embrace the training and apply it in their everyday work, thus causing performance and even reputational failures [67]. Employees also have di<sup>fi</sup>culty focusing on lengthy training sessions, especially when they are concerned about their actual work tasks. This is especially true in the context of security, in which most employees are not experts and lack e<sup>fi</sup>cacy. Most employees do not recognize the importance of caring about security in the context of everyday work. Thus, changing users’ security-related behaviors through training is highly complex and prone to failure [57]. This is a common problem in employee training, during which employees lack conscientiousness and thus do not develop the e<sup>fi</sup>cacy needed to apply what they have learned [67]. Ferguson [36] essentially declared SETA programs useless after conducting an experiment involving four hours of training, as the participants were generally unmotivated and 90 percent failed to detect a phishing attack.

Rather than similarly concluding that SETA programs are ine<sup>f</sup>ective, we instead aim to improve them. We propose that a solution must begin with the recognition that most security training is not enjoyable or motivating—it is perfunctory, arcane, and outside employees’ normal practice and expertise. We posit that security training based on gamification principles<sup>1</sup> (e.g., game-like features applied to nongaming contexts) is an e<sup>f</sup>ective approach for improving intrinsic motivation, learning, coping skills, and subsequent security compliance. People are more motivated and conscientious when they have an enjoyable, immersive experience. However, a recent cross-sectional study complicates our proposition: although Baxter et al. [8] established that their gami<sup>fi</sup>ed security training system was fun, enjoyable, and preferred over other methods, no statistically signi<sup>fi</sup>cant evidence showed that the gami<sup>fi</sup>ed system actually increased the users’ knowledge.<sup>2</sup>

With the <sup>fi</sup>nal goal of improving security training in organizations, our study strengthens the promising foundation of this literature and applies an approach to gami<sup>fi</sup>cation grounded in both motivation theory and design-science research (DSR). Our aim is to improve not only the delivery of organizational security training through gami<sup>fi</sup>cation, but also the security-related motivations, e<sup>fi</sup>cacy, learning, intentions, and behaviors of employees receiving such training. Our six-month <sup>fi</sup>eld study in an actual organization with 420 participants shows that ful<sup>fi</sup>lling users’ motivations and coping needs through gami<sup>fi</sup>ed security training can result in statistically signi<sup>fi</sup>cant changes—including an improved ability to e<sup>fi</sup>caciously respond to actual phishing attempts.

## Gami<sup>fi</sup>cation Literature Review

Gami<sup>fi</sup>cation applies knowledge from gaming theory and flow theory [23, 24, 92] to nongaming contexts. Thus, gamification is “the application of lessons from the gaming domain in order to change stakeholder behaviors and outcomes in non-game situations” [85, p. 352]. Gami<sup>fi</sup>cation was <sup>fi</sup>rst implemented in an organizational context during the “Cold War” when workers and factories in the Soviet Union used a points-based system of competition to increase productivity (which was detached from economic reality and thus back<sup>fi</sup>red) [71]. In 1984, Coonradt [19] became one of the <sup>fi</sup>rst researchers to apply gami<sup>fi</sup>cation to a business context to motivate employees by including frequent feedback, clear goals, personal choice, and gaming features. Although gami<sup>fi</sup>cation emerged from the <sup>fl</sup>ow literature as it applied to gaming, scholars have not reached a consensus regarding gami<sup>fi</sup>cation’s de<sup>fi</sup>nition [92]. Similarly, Liu et al. [59] concluded

The common themes that emerge from the various de<sup>fi</sup>nitions over the past decade are: gami<sup>fi</sup>ed systems must have speci<sup>fi</sup>c user engagement and instrumental goals, and the way to achieve these is by the selection of game design elements. (p. 3)

Another key gami<sup>fi</sup>cation concept is that a game-like user experience activates users’ individual motives [22, 61].<sup>3</sup> Summarizing the various de<sup>fi</sup>nitions of gami<sup>fi</sup>cation in the literature, we propose the following working de<sup>fi</sup>nitions of gami<sup>fi</sup>cation:

● Gamification is the use of game-like IT design artifacts and system processes to strengthen motivations and encourage specific behavioral changes in users for specific instrumental goals.

● Security gamification is applying game-like design artifacts and system processes to strengthen employees’ motivations to encourage learning, eficacy, and increased employee compliance with organizational security initiatives.

Previous research has suggested that game design can include the use of goals, rewards, and storytelling [53] to stimulate experiences of challenge and curiosity [33] and that the conceptualization of gaming elements is highly important for user–game engagement [58]. However, Bui et al.’s [13] review of gami<sup>fi</sup>cation design artifacts o<sup>f</sup>ered two interesting conclusions: (1) most studies did not explain the technological elements of the gami<sup>fi</sup>ed systems, such as how these artifacts foster gami<sup>fi</sup>cation, and (2) there is a

… large gap in research of potential relevance to organizations … more research is needed on employees interacting with group systems resulting in collaboration dynamics and longerterm behavioral outcomes [13, p. 11].

Bui et al.’s review supports three of our study’s core assumptions. First, a careful DSR approach should be used to create gami<sup>fi</sup>ed systems. Second, gami<sup>fi</sup>cation must be applied in a realistic organizational context using longer-term approaches that focus on meaningful engagement to produce meaningful results. Third, the DSR kernel theory must be carefully contextualized to the instrumental goal of the gami<sup>fi</sup>cation task—in our context, improving organizational security through training interventions.<sup>4</sup>

Several researchers have posited that gami<sup>fi</sup>cation can foster employees’ training and subsequent compliance with organizational security [e.g., 2, 8]. These studies are reviewed in Online Table A.1. This research stream faces several challenges, which we address fully in our research: (1) the majority of the studies used one-time cross-sectional data, and none used long-term or longitudinal data; (2) the participants were mainly students, and thus many of the tasks had no ecologically valid relationship to actual organizational security in practice [cf. 60]; (3) the research designs lacked control groups, so there was no way to empirically establish that the gami<sup>fi</sup>cation context was an improvement over the status quo; (4) actual behaviors were not measured; (5) many studies did not use theory, and none developed a cohesive theoretical foundation; (6) most did not involve a working system; and (7) most did not achieve meaningful engagement or articulate the importance of instrumental (e.g., improved IT security compliance) and interaction outcomes (e.g., measurable increased immersion) [cf. 59].<sup>6</sup>

## DSR Applied To Gami<sup>fi</sup>ed Security Training

Given the compelling opportunities in the literature, we argue that an improved approach is needed. Likewise Liu et al. [59] concluded that the gami<sup>fi</sup>cation literature in general does not explain

these design elements should be chosen for <sup>fi</sup> , and  they interact among <sup>how speci c tasks how</sup>themselves and create the desired user interactions that and lead to the <sup>engage the</sup>intended   (p. 3) [emphasis added in bold typeface].

We thus propose that gami<sup>fi</sup>ed security training represents a natural opportunity to apply a DSR approach to bridge the related opportunities in design, theory, methodology, and practice from our introduction.

## Overview of Our DSR Approach

Previous gami<sup>fi</sup>cation studies have largely lacked a systematic DSR approach [13] to the security context. In a non-gami<sup>fi</sup>ed security context, Vance et al. [95] explained that although there is no single, authoritative approach to DSR, a common expectation of DSR is that the solution can be described and evaluated in terms of proof-of-concept and proof-of-value [e.g., 38, 41, 77, 93]:

Proof-of-concept is the point at which enough evidence exists to show that the described conceptual solution of design is feasible and promising, at least in a limited context … . In contrast, proof-of-value is achieved when researchers show that an IT artifact actually works in reality. [95, p. A6] [emphasis added in bold typeface]

Similar approaches to proof-of-concept and proof-of-value have recently been introduced in contexts such as cyberbullying [64], autonomous scienti<sup>fi</sup>cally controlled screening systems [93], and a video-based screening system [82]. However, according to [75, p. 16], the third concept of proof-of-use can also be applied to DSR. To support our DSR approach, we adhered to a DSR methodology that closely follows the method advocated by Nunamaker et al. [76] and elaborated on by Pe<sup>f</sup>ers et al. [81].

We systematically established proof-of-concept and proof-of-value and moved toward ongoing proof-of-use by implementing a system actually used in practice. Next, we explain how we systematically combined relevance with theoretical rigor, leveraging additional DSR principles to embody the principles of the “last research mile” as advocated by Nunamaker et al. [75]. This involved an extensive, iterative process based on the security gami<sup>fi</sup>cation literature, DSR, system development, and feedback from the target organization. Despite its iterative nature, the DSR process we leveraged can be described in the following seven steps (two <sup>fi</sup>nal steps are addressed in the discussion section).

## Establish the Gami<sup>fi</sup>ed Design as an Artifact

We followed Liu et al. [59], who proposed a key gami<sup>fi</sup>cation design principles illustrated by a running case (HealthyMe). Although we applied the majority of their design principles, some were inapplicable to our organizational security context or speci<sup>fi</sup>c design choices.<sup>7</sup> Figure 1 depicts our <sup>fi</sup>nal design framework in which we were able to focus on design as an artifact [cf. 41]. Liu et al. [59] suggested focusing on the design and development of the gami<sup>fi</sup>ed system before focusing on the outcomes. We did so following the DSR approach advocated by Nunamaker et al. [76] and shown in Figure A.1 (Supplemental Appendix A): (1) theory building, (2) systems development, (3) experimentation, and (4) observations. These steps encapsulate several subprocesses, such as those of Pe<sup>f</sup>ers et al. [81].

## Focus on Design Problem Relevance

Our research started when the French company invited one of the authors to help create a system that would encourage better employee IT security compliance through online training. The company had faced an ongoing problem of employee carelessness regarding security issues, including falling for phishing attacks. Their existing e-mail-based training system was not positively viewed within the <sup>fi</sup>rm.

Moreover, our literature review revealed that the traditional approach of encouraging IT security compliance through sanctions is inconsistent and can back<sup>fi</sup>re. We also learned that gami<sup>fi</sup>cation could potentially positively in<sup>fl</sup>uence employee training and motivation. However, no prior research has established clear empirical evidence that employees security learning and e<sup>fi</sup>cacy perceptions could be positively in<sup>fl</sup>uenced by gami<sup>fi</sup>cation.

![](/api/attachments/EGR62QQJ/fulltext/images/b08749942f322dbc070826e5d8ed8d937c6659a5b8f5eeefd7d53ea25d31276a.jpg)  
Framework for design and research of gami<sup>fi</sup>ed systems (adapted from Liu et al. [59]).

## Create Objectives for Design Evaluation

Our objectives were to build a gami<sup>fi</sup>ed training system based on a native information systems (IS) motivational theory as the kernel theory that was tested in an ecologically valid manner using a long-term <sup>fi</sup>eld experiment. We thus undertook an iterative process of design and development, balancing concepts, designs, and concepts from the literature with the client’s training requirements. We unit tested the system and then ran a pilot test with human subjects to further evaluate the design objectives.

## Apply a DSR Kernel Theory Contextualized to Gami<sup>fi</sup>cation

A key step of designing a gami<sup>fi</sup>ed system is to carefully choose the gami<sup>fi</sup>cation design principles that serve as the bridge between the system and meaningful engagement [59]. This step establishes the user-interaction processes that occur between user-system-user actors. We <sup>fi</sup>rst analyzed kernel theories [73] that would support and motivate the employees’ security learning and behavioral change. We surmised that the hedonicmotivation system adoption model (HMSAM) [62] was particularly suitable as a kernel theory and evaluation model when extended to the security context and coping support. This extended model consisted of two main components that further inspired design principles: (1) motivation fulfillment to inspire gami<sup>fi</sup>ed systems use and (2) coping support so the users can deal with security issues and engage in security-related behavioral change.

To proceed with context-speci<sup>fi</sup>c theorizing, we used a framework similar to the one suggested by Hong et al. [43], which suggests that the technology artifact is an additional element in theorizing that should be considered. In IS research, contextualization usually involves the introduction of contextual features into previously established general models, as in the contextualization of the uni<sup>fi</sup>ed theory of acceptance and use of technology [96] to the adoption and use of collaboration technologies [12]. Our most important contextualization consisted of adding context-speci<sup>fi</sup>c factors—learning, security response e<sup>fi</sup>cacy, and security self-e<sup>fi</sup>cacy—to HMSAM.

## Propose Guiding Design Principles to Bridge DSR Design Objectives and the DSR Kernel Theory

Following DSR, the subsequent design principles needed to rely on carefully chosen design elements. Thus, we proposed the <sup>fi</sup>rst design principle:

Design principle #1: The gami<sup>fi</sup>ed training system should incorporate di<sup>f</sup>erent design elements that increase employees’ motivation and ful<sup>fi</sup>llment.

Regarding coping support, it is crucial that the new system has features that sustain and leverage employees’ knowledge in such a way that employees will not only be intrinsically motivated through enjoyment but will also acquire the new knowledge e<sup>f</sup>ectively. This led to the second design principle:

Design principle #2: The gami<sup>fi</sup>ed training system should provide new knowledge through a learning process that is meaningful, entertaining, and fun.

Here, there are three conceptual design issues that need to be addressed [73]: The <sup>fi</sup>rst is the “conceptual distance between a latent independent variable (cause) and its corresponding design items” [73, p. 311], which in our case translates into the potential for both intrinsic and extrinsic motivations to positively in<sup>fl</sup>uence security learning and behavioral change. Both intrinsic and extrinsic motivations can positively in<sup>fl</sup>uence an individual’s security behavioral change [e.g., 14, 40]. However, extrinsic motivations may provide only temporary compliance [55] and intrinsic motivations are more powerful in driving employee’s behaviors [78]. Likewise, intrinsically motivated learners were found to demonstrate higher achievements in learning [9]. To satisfy this meta-requirement, we focused primarily on intrinsic motivations when designing the system, although there may be some spillover into extrinsic motivations.

The second issue concerns the “conceptual distance between a latent dependent variable (e<sup>f</sup>ect) and its corresponding measurements” [73, p. 312]. Here, the challenge involves choosing the right measurement items, which is especially important for DSR so that design evaluation and research rigor can be established [41]. We thus carefully reviewed the literature and, whenever possible, selected established measures, as further documented in the method section.

The third and <sup>fi</sup>nal conceptual design issue concerns the “potential interdependence of simultaneously implemented design items” [73, p. 312]. This is the problem of confounding design elements that may have di<sup>f</sup>erent e<sup>f</sup>ects on the artifact evaluation. For example, we had to decide whether to guide the learning process through a recorded video or through a series of brief, interactive lessons that used graphical examples of phishing mistakes typically made by employees. Here, the design decision in<sup>fl</sup>uenced the evaluation of the artifact. Our target organizations placed a premium on simplicity; thus, we chose short informative lessons. Such decisions can in<sup>fl</sup>uence the “solution space for other design decisions; however, this may lead to lock-in situations with respect to the <sup>fi</sup>nal artifact” [73, p. 312].

## Establish Proof-of-Concept

We followed four primary steps to establish proof-of-concept [cf. 81] before we proceeded to empirical testing. The company was pleased by the positive results, and the feedback from employees was highly positive. Thus, the solution worked well in practice, which provided evidence of proof-of-concept [80].

Step 1: Before creating a working prototype, we reviewed the gami<sup>fi</sup>ed security literature to learn about gami<sup>fi</sup>cation features that may work well in a security context and understand why this is the case.

This review is detailed in Supplemental Appendix A (see Tables A.1–A.2).

Step 2: We then created Table A.3 to propose how gami<sup>fi</sup>cation elements should be implemented in our context and that we followed to implement multiple versions of our security training system. We also mapped these elements to the various ways that <sup>fl</sup>ow (in our context, immersion) can be fostered [24] and mapped the elements to the intrinsic motivations they could potentially ful<sup>fi</sup>ll.

Step 3: We then further bridged design and theory by systematically applying our kernel theory, HMSAM, by mapping the derived gami<sup>fi</sup>cation element relationships to HMSAM constructs, as shown in Table A.4. This allowed us to conceptually check whether our design could ful<sup>fi</sup>ll intrinsic motivations and provide an “appropriate challenge.”

Step 4: Finally, in Table A.5 we mapped speci<sup>fi</sup>c motivations to each of the gami<sup>fi</sup>cation design elements. We used a taxonomy of major motivations for system use in [61] where the motivations were suited for the security training context. By analyzing mappings from Table A.4 and Table A.5, we observed the same relationships with motivations. For example, play/ enjoyment/fun can be found in 11 gami<sup>fi</sup>cation design elements (Table A.5.).

## Establish Proof-of-Value

To establish proof-of-value, once the system was deemed ready, we <sup>fi</sup>rst formally pilot tested it and the kernel theory with students. However, the key step in establishing proofof-value involved a long-term <sup>fi</sup>eld experiment with actual employees using the gami<sup>fi</sup>ed security training system. These details, and the subsequent rigorous analyses, are addressed fully in the section after the next section. Before addressing the full proof-ofvalue methodologies and analyses, the next section details how we operationalized our kernel theory, HMSAM, to develop testable hypotheses for empirically establishing proofof-value.

## Kernel Theory Foundation for Proof-of-Concept and Proof-of-Value

The key role of our kernel theory, HMSAM, was twofold: to guide the design and help establish proof-of-concept, and to be operationalized to test it for further proof-of-value. Again, this process was iterative such that what we learned in developing hypotheses informed design, and vice versa. Here, our focus is on the derived operationalized hypotheses and the logic behind them.

HMSAM was chosen primarily because it is a native IS theory that focuses heavily on intrinsic motivations in systems use [62], which we found to be a natural <sup>fi</sup>t for our gami<sup>fi</sup>ed context. Namely, HMSAM was designed to explain how ful<sup>fi</sup>lling motivations can lead to increased immersion and behavioral intention (BI) and ultimately to behavioral change [62]. These explanations are more theoretically powerful and appropriate predictors of BI than traditional factors, such as perceived ease of use (PEOU) or joy [62]. HMSAM builds on <sup>fl</sup>ow theory by re-envisioning the original conceptualization of cognitive absorption (CA) developed in [3]. The CA construct was inspired by <sup>fl</sup>ow theory, which was not proposed with systems in mind, and is de<sup>fi</sup>ned as a deep state of involvement with systems (i.e., immersive systems use). Gami<sup>fi</sup>ed systems thus represent an ideal setting in which to investigate CA, which has a<sup>f</sup>ective and cognitive components and is an intrinsic motivator. Whereas the original conceptualization of CA assumed that its components (curiosity, joy, control, and immersion) occurred simultaneously as one formative construct [3], HMSAM examines CA’s components independently and explains how the ful<sup>fi</sup>llment of intrinsic motivations fosters associated BI (or, in the original HMSAM, system acceptance intentions). Lowry et al. [62] argued that this approach is more consistent with <sup>fl</sup>ow theory’s understanding of <sup>fl</sup>ow as a process that unfolds over time and involves multiple constructs.

HMSAM also leverages the technology acceptance model (TAM) to explain that intrinsic TAM elements are lower-order factors in the creation of immersion and BI. Consequently, HMSAM is a process-variance model in which intrinsic TAM elements, like PEOU and enjoyment, are lower-order elements that precede immersion and combine to change BI.

Figure 2 depicts the HMSAM that we extend for the new context of BI related to security learning and compliance. Our extensions are shown as hypotheses; all remaining paths are replications of HMSAM. Our model suggests that the factors of improved security learning, e<sup>fi</sup>cacy perceptions, and the ability to cope with security challenges encourage positive behavioral change by strengthening employees’ intentions to follow security policies and improving their phishing-response behaviors.

![](/api/attachments/EGR62QQJ/fulltext/images/d1a85f8c4247bfc641f8899b75bd107030d6b06b73e6edbec3eed589a5ab0d46.jpg)  
Operationalized and extended Kernel theory: HMSAM. PEOU, perceived ease of use; PIU, <sup>Figure 2.</sup>perceived intrinsic usefulness; BI, behavioral intention to follow security policies; OSC, organization security communication; TMSC, top management security commitment; OCM, organization computer monitoring.

## Core Kernel Theory Assumptions for Achieving Immersion

A core assumption of our operationalized kernel theory is that the experience of <sup>fl</sup>ow (and thus, in our context, immersion) arises from the satisfaction of three conditions: (1) clear goals, (2) unambiguous

feedback, and (3) a balance of challenges and skills [29]. The <sup>fi</sup>rst condition indicates the importance of instrumental goals, as stressed by Liu et al. [59], which suggests that the gami<sup>fi</sup>cation system should

Enable the accomplishment of dual goals, in which both sides can see bene<sup>fi</sup>ts (e.g., improved security knowledge for the employee and fewer security breaches for the company). Unambiguous feedback can be delivered by providing gami<sup>fi</sup>ed feedback in the training itself. In the gami<sup>fi</sup>ed system, this could be augmented with leaderboards, points, measurement against goals, features that convey a sense of general progress, and the presence of a gamemaster [2, 8, 42]. Balancing challenge and skills, fostered through learning and the e<sup>fi</sup>cacy and coping derived from it, is a core focus of the remainder of this section.

## Infusing Learning and Security Coping into Our Context

Like motivations, positive coping skills can foster behavioral change. A key way to deliver coping skills is through SETA programs [e.g., 21]. Our gami<sup>fi</sup>ed environment provides common SETA-based training related to organizational security systems, particularly to help employees learn how to identify and avoid phishing attacks and suspicious e-mails. Research has found a link between learning and behavioral engagement [44]. The more employees learn, the more they will be prepared to implement protective security behaviors [cf. 84]. Employees who have a deeper knowledge of security risks and ways to thwart them are more likely to believe they can comply and protect their organizations. Conversely, employees who have little knowledge in this area are more likely to be uncertain and make poor security decisions. Research shows that the learning process strengthens one’s abilities; as a result, one pays more attention to the context, content, and environment, all of which must be properly assessed to make e<sup>f</sup>ective security decisions [51]. Thus,

Hypothesis 1. Increased perceived learning in a gamified security training context is associated with increased BI.

Such learning fosters general coping abilities, most commonly termed “security response e<sup>fi</sup>cacy” and “security self-e<sup>fi</sup>cacy” [e.g., 11, 52]. Response eficacy is “the belief that the adaptive response will work, that taking the protective action will be e<sup>f</sup>ective in protecting the self or others” [37, p. 411]. Self-eficacy is the degree to which individuals believe they are capable of preventing threats [11]. Security researchers have reconceptualized these concepts extensively and from several perspectives [11, 49, 52, 99, 100]. In our context, security response eficacy means that employees believe that what they were told to do in their security/phishing training will work to prevent the threat, and security selfeficacy means that they believe they can deal with the security response themselves. Thus, if employees learn a new protocol that is purported to mitigate phishing attacks and they believe the process is e<sup>fi</sup>cacious, they will be more likely to follow it.

Research [79] has also found that goal-oriented individuals demonstrate higher levels of task-speci<sup>fi</sup>c e<sup>fi</sup>cacy. Our gami<sup>fi</sup>ed environment fosters a goal orientation with a clear task objective and concrete feedback. Performance and achievement lead to higher levels of self-e<sup>fi</sup>cacy, and an informal social learning environment directly in<sup>fl</sup>uences employee e<sup>fi</sup>cacy levels [68]. This suggests that employees will not only demonstrate higher levels of e<sup>fi</sup>cacy but also be more certain of their ability to apply newly acquired knowledge in practice. Learning also leads to greater e<sup>fi</sup>cacy, which in turn generates more interest and more learning [51]. Thus, it is likely that there are feedback mechanisms between e<sup>fi</sup>cacy and learning. However, for concision, we predict:

Hypothesis 2a–b. Increased perceived learning in a gamified security learning context is associated with increased (a) security response eficacy and (b) security self-eficacy.

## Coping and Behavioral Change

Research has demonstrated the importance of improving coping skills as a means of encouraging behavioral changes in employees that result in better adherence to security policies [e.g., 11, 14, 52, 100]. Recent research [100] has identi<sup>fi</sup>ed a clear link between coping adaptiveness (e.g., task-focused coping) and perceived phishing detection e<sup>fi</sup>cacy. This is partially supported by recent <sup>fi</sup>ndings that awareness and motivation are crucial for security compliance [16].

E<sup>fi</sup>cacy should increase not only as a result of learning but also speci<sup>fi</sup>cally as a result of learning through a gami<sup>fi</sup>ed system, because such systems make learning more e<sup>fi</sup>cacious. Gami<sup>fi</sup>ed systems provide “powerful social psychological processes such as self-e<sup>fi</sup>cacy … [that] provide rewards … [and] drive most of the long-term participation” [31, p.16]. Per Bandura [6], setting and assigning goals (e.g., badges or levels in gami<sup>fi</sup>ed systems) enhances self-e<sup>fi</sup>cacy.

Thus, the increased self-e<sup>fi</sup>cacy and response e<sup>fi</sup>cacy resulting from gami<sup>fi</sup>ed systems should lead to an increased intention to act securely, as more employees will feel capable of acting securely and believe that the desired security decision will be e<sup>f</sup>ective.

Hypothesis 3a–b. Both (a) increased security response eficacy and (b) security self-eficacy in a gamified security training context are associated with increased BI.

## Balancing Skills and Challenges

Again, the third condition of achieving immersion, per Davis and Csikszentmihalyi [29], is balancing skills and challenges. In gami<sup>fi</sup>ed contexts, <sup>fl</sup>ow occurs when perceived skill and challenge levels are balanced; however, if such levels are initially low, apathy instead of engagement can occur [20]. Likewise, a key role of gami<sup>fi</sup>ed components is to stimulate experiences of both curiosity and challenge [33], with challenges driving immersive engagement [47]. Thus, “if stimuli from an experience are either too challenging or not challenging enough, interest and curiosity decline” [61, p. 539].

Thus, we add to HMSAM the concept of challenges, which when met can ful<sup>fi</sup>ll motivations and ultimately facilitate immersion. However, the key limiting assumption of this addition is that a challenge is most likely to be useful if it takes the form of an appropriate challenge, which is “the degree to which the perceived positive challenge of an activity matches the perceived skills of the user” [61, p. 539]. Thus, as it relates to an employee’s instrumental goals, learning, and e<sup>fi</sup>cacy, a gami<sup>fi</sup>ed training task should be neither too challenging nor too facile. The greater the challenge, the greater the behavioral engagement required to overcome it [89]. Likewise, we assume that the challenge should become more di<sup>fi</sup>cult (e.g., “levels up”) as the employee learns and becomes more e<sup>fi</sup>cacious [e.g., 7]. Otherwise, curiosity will be undermined, and boredom can ensue.

Meng et al. [69] argued that the optimal challenge leads to optimal immersion. We likewise argue that (1) good gami<sup>fi</sup>cation delivery involves progressive challenges, but (2) such challenges must be appropriate, and thus, a challenge might become “too much” for an end user and cause diminishing returns. This state represents an inverted U-shaped relationship in which a “relationship exists if the dependent variable Y <sup>fi</sup>rst increases with the independent variable X at a decreasing rate to reach a maximum, after which Y decreases at an increasing rate” [39, p. 4]. A recent study [66] employed the twoplayer StopWatch game to con<sup>fi</sup>rm through electrophysiological evidence that this inverted U-shaped relationship exists between perceived challenges and one’s intrinsic motivation. Namely, in situations in which the challenge is optimal, one’s immersion should increase up to the apex of the curve, whereas further increases of the challenge beyond the optimal point should lead to decreased immersion. Thus,

Hypothesis 4. Perceived challenge will have a positive and curvilinear (inverted U-shaped) relationship with perceived immersion in a gamified security training context.

## Ful<sup>fi</sup>lling Motivations for Behavioral Change

CA theory [3] predicts that immersion is positively associated with BI, which has been replicated in HMSAM gaming research [62]. However, we have extended HMSAM, such that BI is parallel to our context and thus involves the intention to follow security policies, not the intention to use a system. This is a theoretically reasonable extension, because HMSAM’s behavioral predictions are rooted in TAM, which is rooted in the theory of reasoned action (TRA) [5]. TAM, the TRA, and the related theory of planned behavior (TPB) [4] consistently exhibit a strong link between attitude formation, intention, and behavior that extends far beyond mere system usage. This is the case regardless of shifts in the behavioral target, as long as the target is in the same context.

Gami<sup>fi</sup>cation and immersion are powerful in<sup>fl</sup>uences on behavioral change in individuals, and they should be especially apt in our gami<sup>fi</sup>ed security training context. An earlier study [72] predicted, but did not empirically show, that meaningful gami<sup>fi</sup>cation should motivate and lead to long-term behavioral changes. A key reason for this is that motivations can be ful<sup>fi</sup>lled through immersion. Immersion in gaming contexts is the experience of being engaged in the game-playing experience while having partial awareness of reality [62]. In learning contexts, immersion occurs as a result of appealing to intrinsic motivations, such as learning new things and being engaged [35].

Immersion is an experience of total involvement that causes external demands to be ignored [3, 62]. This increased focus, combined with the ful<sup>fi</sup>llment of motivations, creates ideal conditions for learning and behavioral change. Research [98] has found that higher levels of immersion lead to greater usage intentions than lower levels of immersion. By in<sup>fl</sup>uencing the state of <sup>fl</sup>ow/immersion, gami<sup>fi</sup>cation positively and continuously in<sup>fl</sup>uences intentions and actual behaviors. Numerous studies have found that intrinsic motivations are strong predictors of meaningful user behavioral change outcomes, such as satisfaction, continuance intentions, and perceived performance [25, 61].

The underlying causal mechanisms are not just cognitive, as inferred by the TRA, but also physiological. Thus, they are surprisingly powerful. Prior research has identi<sup>fi</sup>ed several neurological causal mechanisms involved in <sup>fl</sup>ow and gaming, showing that games lead to numerous neurological changes: (1) the brain releases more dopamine, which is associated with pleasure and consequently increases motivation [54]; (2) testosterone is increased, a<sup>f</sup>ecting energy, mood, and self-esteem [34]; and (3) memory is improved by training the amygdala, the brain’s memory and decision center, to better respond to similar situations in the future [10]. These factors can lead to dramatic behavioral changes.<sup>8</sup> Thus, assuming that the underlying mechanisms of the TRA and of the gami<sup>fi</sup>cation of intrinsic motivations and learning hold true in our context, employees should be motivated to strengthen their context-related intentions when they have a more immersive learning experience.

Hypothesis 5. Increased immersion in a gamified security training context is associated with increased BI to comply with the security policies employees are learning

Moreover, both the TRA [5] and the TPB [4] predict a strong link between intention and behavior. In the information security context, several studies have suggested that it is more realistic and valid to measure actual behaviors than intentions [11, 22, 60]. It is particularly important to measure actual behaviors, as it is clear that good intentions do not always lead to good behaviors in organizational security contexts, as employees often have con<sup>fl</sup>icting roles and motivations with respect to security requirements [11, 22, 83].

Measuring behaviors is an excellent way to further determine whether gami<sup>fi</sup>cation can result in meaningful security training and behavioral changes. Thus,

Hypothesis 6. Increased BI should be associated with an increased actual phishing response, when following the same security policies.

## Modeling Counter-explanations Through Control Variables

Testing counter-explanations of other possible predictors has pragmatic relevance in IS security research [83]. We do so by modeling common demographic covariates and alternative security constructs, as follows: age, gender, experience, education, organization computer monitoring (OCM) [27], organization security communication (OSC) [17, 88]; and top management security commitment (TMSC) [46].

## Procedures for Design Evaluation for Proof-of-Value

## Pilot Study for Proof-of-Value

Once we deemed the system to have achieved reasonable proof-of-concept, we prepared to rigorously establish its proof-of-value. Thus, we <sup>fi</sup>rst conducted a pilot study with university students (N = 45). The study spanned three months and included monthly data collection. This allowed us to re<sup>fi</sup>ne the procedures and test the instruments’ validity and reliability.<sup>9</sup>

## Main Study Design for Proof-of-Value in Actual Use

The <sup>fi</sup>nal study for formal proof-of-value in actual use was designed as a controlled <sup>fi</sup>eld experiment using an unbalanced design of two treatment and one control groups. A total of 800 employees from a large international French company were invited to participate, who were con<sup>fi</sup>rmed from HR records to have not received security training. Only o<sup>fi</sup>ces in which English was the main language (i.e., the United Kingdom, the United States, and Australia) participated to prevent potential language issues and website localization. The 488 employees who positively responded<sup>10</sup> were randomly assigned to one of two groups: the gami<sup>fi</sup>ed system treatment group (420 employees) or the e-mail treatment group (68 employees); they were determined to be demographically equivalent. The control group (38 employees) was not explicitly invited so they would not know they were used as controls; this was created using a random sample from the organization’s HR database of employees. The participation rate of over 50 percent is high for organizational <sup>fi</sup>eld studies. Thirty-six participants were removed because of implausibly short response times [under eight minutes], incomplete answers, and illogical response patterns. The <sup>fi</sup>nal sample included 384 responses. The average age of the participants was 33.4 years (SD = 11.2 years); 52 percent were male and 48 percent were female.

Notably, the control group received no training or noti<sup>fi</sup>cations. However, the gami<sup>fi</sup>cation and e-mail groups received the same training content and the same frequency of training, reminders/noti<sup>fi</sup>cations, and quizzes. These two sets of participants were invited to take a quiz after completing each training session. This allowed for a cleaner manipulation between gami<sup>fi</sup>ed interaction versus non-gami<sup>fi</sup>ed e-mail interaction. A custom Web-based gami<sup>fi</sup>cation application was created by one of the researchers using .NET technology, and all design elements were developed based on previously identi<sup>fi</sup>ed game mechanics.

## Gami<sup>fi</sup>ed System and Procedures

The gami<sup>fi</sup>ed system’s objective was to educate users about security topics using various game design elements. In the <sup>fi</sup>rst step, users registered for and signed in the website. Next, users chose an avatar (Supplemental Appendix B, Figure B.1), and after completion, users were redirected to the main screen (see Figure 3).

At the <sup>fi</sup>rst login, the gamemaster appeared and explained the game mechanics (e.g., how to earn points). The gamemaster appeared at di<sup>f</sup>erent stages/levels of the game. For example, if the user had not logged in for over one week, the gamemaster sent an e-mail (the same noti<sup>fi</sup>cation frequency was used for the e-mail group) inviting the user to continue and providing the user with information about current achievements and top scorers (via the leaderboard). The objective of the game was to complete quizzes and read di<sup>f</sup>erent tips related to security education about malicious software (malware), spam, and especially how to avoid falling victim to phishing attempts. By playing di<sup>f</sup>erent rounds, users accumulated points that allowed them to receive additional incentives in the form of monsters (monsters represented trophies) and to advance to another level (bronze, silver, and gold). In addition, a leaderboard of top employees with their corresponding scores was displayed on the main menu interface. Di<sup>f</sup>erent rounds with quizzes and other educational elements were o<sup>f</sup>ered to users every two weeks (again, the same frequency was used for the e-mail group). This gave users time to educate themselves about di<sup>f</sup>erent security and phishing topics and to acquire the knowledge necessary to correctly answer questions.

![](/api/attachments/EGR62QQJ/fulltext/images/be8f2d7a895211260fdfa6ddfd802b78d2740c3ea914f3e3db3d5b197c254941.jpg)  
Main screen of gami<sup>fi</sup>ed system.

The participants in the e-mail control group did not participate in the controlled <sup>fi</sup>eld experiment but followed a more traditional security education approach limited to e-mail communication. E-mail communication (Figure B.5) o<sup>f</sup>ered the same content as the gami<sup>fi</sup>ed system, but the format was less visually appealing and contained more textual explanations. Nonetheless, the content of the e-mail communication was useful, clearly written, and easy for employees to understand.

We chose phishing as a key focus of the training because it is a much more urgent concern for management than behaviors like reading spam or failing to check for viruses. Moreover, responding to a phishing attack is an objectively auditable security behavior. Participants completed a survey at three months and at the end of the game (i.e., six months). To measure users’ security behaviors, we sent a phishing e-mail to employees inboxes without their knowledge. This process was administered by a third-party company that specializes in phishing testing/training. An e-mail was sent to employees asking them to change their passwords by clicking on the internal company’s link (the link led to the third party’s website, which tracked a lack of compliance). Employees’ decisions were coded as binary variables (“0” for not clicking or “1” for clicking), which measured users’ security behaviors. To establish anonymity, and a link between each employee’s security gami<sup>fi</sup>cation platform presence and the phishing e-mail, a unique random number was created for each participant and that number was used for the survey.

## Measures for Design Evaluation

The measurement items were borrowed or adapted from previous studies (see Table C.1). All scales were re<sup>fl</sup>ective, using a seven-point Likert-type scale ranging from completely disagree (1) to completely agree (7). A new measure was created for challenge, which corresponded to the perception of the game’s level of di<sup>fi</sup>culty. The actual phishing behavior construct was a binary value (0 or 1).

## Analysis for Final Proof-of-Value

## Measurement Model

First, a con<sup>fi</sup>rmatory factor analysis was conducted. The results indicated that some items’ standardized regression weights were lower than 0.60 (e.g., JOY1 and PEOU1) and were thus removed. After rerunning the model, all other factor loadings were higher than the recommended 0.60 value. Next, the average variance extracted (AVE) values were checked to ensure that all values exceeded 0.50.

According to all tests, the measurement model exhibited good reliability, and convergent validity and discriminant validity<sup>11</sup> were established. Table D.1, in Supplemental Appendix D, details the loadings. Table D.2 summarizes the discriminant validity and AVEs for the model. Table D.7 presents the statistics used to assess the quality of the measurement model’s measures. We con<sup>fi</sup>rmed that the Cronbach’s α values for all scales were higher than 0.70 and found that multicollinearity was not an issue. In addition to taking several measures to prevent common methods bias, we conducted two tests to demonstrate that it was likely not a factor in our data (see “CMB and Multicollinearity” in Supplemental Appendix D).

## Structural Model Results

We used Mplus 7 software, a covariance-based structural equation modeling (CB-SEM) tool, to test the model. Mplus 7 allowed for the theory and hypotheses to be assessed for model <sup>fi</sup>t and provided a logistic regression analysis for the dichotomous outcome variable (i.e., actual phishing response behavior). Age, gender, experience, and education were included in the analysis as controls for intentions and behaviors; the organizational security constructs of TMSC, OSC, and OCM were added as counter-explanations. Figure 4 depicts the structural model results. Table D.8 summarizes the full structural model testing details, which included three stages of model testing: Model part 1 (HMSAM replication only), Model part 2 (extension to add coping and challenge), and Model part 3 (full model with controls and theoretical counter-explanations). All HMSAM replications were supported, except joy to BI and control to immersion. All hypotheses were supported (Hypothesis 4 is addressed last); our results at month three were similar, but not as strong (Table D.3). When we modeled the data for the e-mail treatment alone, the results were much worse (see Tables D.4 and D.5). Interestingly, the e-mail treatment results worsened or remained the same between the initial three-month period and the six-month period.

Finally, H4 was supported, but because Hypothesis 4 was hypothesized as a nonlinear relationship, we <sup>fi</sup>rst ran the model with original indicators and then estimated the construct that had the proposed nonlinearity.

We then performed the transformation through a squared term and entered this new variable in the SEM model, in which both the main e<sup>f</sup>ect and the squared term were related to the same dependent variable. A similar approach was used in Moody et al. [70], which tested a curvilinear model with covariance-based SEM. The variance in<sup>fl</sup>ation factors (VIFs) increased and ranged from 1.945 to 9.453 with the model <sup>fi</sup>t RMSEA 0.062, SRMR 0.069, CFI 0.929, and TLI 0.923 for the gami<sup>fi</sup>cation treatment and RMSEA 0.072, SRMR 0.078, CFI 0.905, and TLI 0.902 for the e-mail treatment. Although the model <sup>fi</sup>t and VIFs worsened, the values were still within the acceptable ranges and are expected to worsen when including a squared term.

![](/api/attachments/EGR62QQJ/fulltext/images/bcdb4062734f082a6e4284f1d4f0fd2928a865fdb7ba88cd5a3b064e2faedc0a.jpg)  
Structural model testing results of the operationalized Kernel theory at six months<sup>12</sup>.

## Manipulation Checks of Instrumental Goals

Given that the <sup>fi</sup>eld experiment was conducted to determine whether the gami<sup>fi</sup>ed training system could increase learning and immersion as well as decrease employee susceptibility to phishing, a crucial piece of the analysis was the manipulation checks, as they indicated whether the gami<sup>fi</sup>ed system delivered on its instrumental goals to improve security learning and compliance. This was con<sup>fi</sup>rmed by the two manipulation checks. First, we compared the degree to which the small group of randomly selected employees (those in the control group who did not participate in the gami<sup>fi</sup>ed group or e-mail group) and the gami<sup>fi</sup>ed treatment group were successfully phished. The results in Tables 1 and 2 indicate that there was a signi<sup>fi</sup>cant di<sup>f</sup>erence in the expected direction. Strikingly, those with e-mail training performed no better than those who received no training at all.

The treatment e<sup>f</sup>ects that occurred between the e-mail and gami<sup>fi</sup>ed groups in terms of the model variables were also examined. A multivariate analysis of variance (MANOVA)<sup>13</sup> was run to compare the values for signi<sup>fi</sup>cant di<sup>f</sup>erences. Crucially, our group (i.e., cell) sizes were di<sup>f</sup>erent; thus, we carefully checked to ensure that we adhered to the assumptions of MANOVA, which included the con<sup>fi</sup>rmation of Box M (see “Box M and MANOVA assumptions” Supplemental Appendix D). Table D.9 summarizes the means and SDs comparing these two groups at the end of six months (Tables D.6 and D.7 provide the respective correlations). To compare the actual behaviors between the two groups, the Z-score (2.2561, $\mathrm { ~ p ~ < ~ } 0 . 0 5 )$ was calculated, con<sup>fi</sup>rming that the two groups’ actual behaviors were signi<sup>fi</sup>cantly di<sup>f</sup>erent and in the expected direction.

## Discussion

The discussion of our study is guided by the structural example provided by Abbasi et al. [1] and the DSR evaluation principles of Hevner et al. [41]. We also lean heavily on inspiration found in following Liu et al. [59], Nunamaker et al. [76], Pe<sup>f</sup>ers et al. [81], and Gregor and Hevner [38].

Summary of who was and was not phished in the control and treatment groups.

<table><tr><td>Group</td><td>Phished (n = 149)</td><td>Not phished (n = 341)</td></tr><tr><td>Control group* (n = 38)</td><td>17 (44.7 percent)</td><td>21 (55.3 percent)</td></tr><tr><td>Gamified group (n = 384)</td><td>105 (27.3 percent)</td><td>279 (72.7 percent)</td></tr><tr><td>E-mail group (n = 68)</td><td>27 (39.7 percent)</td><td>41 (60.3 percent)</td></tr></table>

\*Note: The control group was a randomly selected group of employees who had not received training through gami<sup>fi</sup>cation or e-mail. The n’s represented in this table were used for the analysis after all data drops.

Comparisons between the treatment <sup>Table 2.</sup>and control groups.

<table><tr><td>Comparison</td><td>Phished (Z-score)*</td></tr><tr><td>Gamified vs. control</td><td>2.2561*</td></tr><tr><td>Gamified vs. e-mail</td><td>2.0664*</td></tr><tr><td>Control vs. e-mail</td><td>0.5041 n/s</td></tr></table>

\*Note: A result is signi<sup>fi</sup>cant at $p < 0 . 0 5$ (assuming a two-tailed hypothesis test).

## Recap of Our General DSR Study Goals

The goals of our DSR study were pragmatically driven from the serendipitous con<sup>fl</sup>uence of several opportunities: First, we were approached by a French international company that wanted help improving their internal SETA program to increase organizational security compliance. Second, we saw gami<sup>fi</sup>ed security training as a way to improve their training, but we observed that previous research e<sup>f</sup>orts in this area were incomplete, with too little focus on the design artifact, long-term data, objective behavioral assessment, use with actual employees, and so on. Third, the recent gami<sup>fi</sup>cation editorial by Liu et al. [59] pointed to similar issues in the gami<sup>fi</sup>cation literature that has thus far largely failed bridge theory, design, and methodology. Fourth, previous gami<sup>fi</sup>cation studies in a security context have largely lacked a systematic DSR approach. Consequently, we thus proposed that gami<sup>fi</sup>ed security training represents a natural opportunity to apply a DSR approach to bridge the related opportunities in design, theory, methodology, and practice.

Applying our goals to practice, we followed rigorous and systematic DSR principles, and created a working gami<sup>fi</sup>ed SETA system based on an iterative application of theory, extant literature, prototyping, and feedback from the target organization. In the <sup>fi</sup>eld, the goal of our study was to extend and recontextualize kernel theory (i.e., HMSAM) to explain how organizations can positively bring about security learning and associated behavioral changes in employees, speci<sup>fi</sup>cally in a gami<sup>fi</sup>ed security training context. We aimed to do so through the novel application of two parallel factors: (1) focusing on positive interventions through gami<sup>fi</sup>ed training (as opposed to traditional manipulations of punishments, fear, and threats) and (2) improving employees’ security learning and e<sup>fi</sup>cacy to strengthen their ability to cope with security challenges (in our context, phishing). Together, these two factors were predicted to result in positive behavioral change in employees through their increased intentions to follow security policies and the alignment of their actual phishing response behaviors with the organizational security policies in which they were trained.

## Recap of Our DSR Approach

To support our DSR approach, we adhered to a DSR methodology that closely followed the method advocated by Nunamaker et al. [76] and elaborated on by Pe<sup>f</sup>ers et al. [81]. This involved an extensive, iterative process based on the security gami<sup>fi</sup>cation literature, DSR, system development, and feedback from the target organization. In doing so, we followed a rigorous but highly iterative process that can be best described in nine steps: (1) established the gami<sup>fi</sup>ed security training system as an artifact; (2) focused on the design problem relevance; (3) created objectives for design evaluation; (4) applied a DSR kernel theory that is contextualized to gami<sup>fi</sup>cation; (5) proposed design principles that bridge DSR design objectives and the DSR kernel theory; (6) established proofof-concept through multiple methods; (7) established proof-of-value through multiple methods; (8) created a working foundation in which proof-in-use can be established over time; and (9) evaluated the results rigorously according to multiple DSR evaluation guidelines.

## Establishing Proof-of-Concept

Before moving to proof-of-value, we carefully followed the steps for proof-of-concept suggested by Pe<sup>f</sup>ers et al. [81], as detailed extensively earlier in the paper. Of the many discoveries and design artifacts that were created through this process, perhaps the most fundamental outcome was driven by the ideas from Liu et al. [59] that a key step of designing a gami<sup>fi</sup>ed system is to carefully choose the gami<sup>fi</sup>cation design principles that serve as the bridge between the system and meaningful engagement. This step establishes the user-interaction processes that occur between user-system-user actors. We see this approach as key to tying the design to a meaningful kernel theory (i.e., HMSAM) that further explains meaningful engagement and measures that can be used to evaluate it. We posit that these ideas are core to fostering proof-of-concept.

Thus, HMSAM provided the basis for our kernel theory and evaluation model, which consisted of two main components that further inspire design assumptions and principles: (1) the importance of designing for motivation fulfillment to inspire meaningful and engaged gami<sup>fi</sup>ed systems use and (2) the importance of designing for coping support so the users can deal with security issues and thus encourage security-related behavioral change. These ideas also inspired the two design principles we carefully applied in building our training artifact. These principles were systematically applied with the literature and iterative design sessions, <sup>fi</sup>nally yielding a strong case for proof-ofconcept, as detailed in our earlier DSR section and the supplemental appendices.

## Establishing Overall Proof-of-Value

To establish proof-of-value, once the system was deemed ready, we <sup>fi</sup>rst formally pilot tested it and the kernel theory with students. However, the key step in establishing proofof-value involved a long-term <sup>fi</sup>eld experiment with actual employees using the gami<sup>fi</sup>ed security training system. Our overall proof-of-value is demonstrated in that the DSR artifact worked as intended and as theorized. Their SETA program was thus improved. Going forward, we discuss proof-of-value in three details respects: (1) in actual practice, (2) in research, and (3) in theory.

## Establishing Proof-of-Value in Actual Practice

Our proof-of-value in actual practice was demonstrated in multiple respects. First, our long-term study demonstrated both strong ecological validity<sup>14</sup> and meaningful engagement [59]. Achieving meaningful engagement is an important factor of building gami<sup>fi</sup>ed information systems and should be addressed in view of both instrumental and experiential bene<sup>fi</sup>ts [59]. Not only did the participants use the gami<sup>fi</sup>ed system over six months during their normal course of work, but also a third party phished the unwitting participants and control group to objectively assess whether they followed the phishing response outlined by the organization’s security policies.

Likewise, the employees’ learning, e<sup>fi</sup>cacy, and behaviors were strongly and positively in<sup>fl</sup>uenced (and thus the SETA program), thereby demonstrating the utility of our extended model as well as the value of the gami<sup>fi</sup>ed design elements included in the system. Aside from the strong manipulations and statistical results of our design, we received positive feedback from the organizational leadership and participating employees. Again, we focused solely on manipulating positive motivations and improving participants’ coping responses and did not use typical approaches involving deterrence, threats, or fear.

Gami<sup>fi</sup>ed system design elements contributed to a more immersive experience and appealed to powerful motivations while building employees’ coping capabilities. We thus demonstrated that a gami<sup>fi</sup>ed security training system approach o<sup>f</sup>ers a new and unique way to improve employee security learning and compliance and can be implemented without the usual “carrots and sticks.” Although threats, fear, sanctions, and costs/bene<sup>fi</sup>ts may have an appropriate place in organizations [e.g., 11, 27, 52], these approaches also run the risk of back<sup>fi</sup>ring, causing reactance, a sense of injustice, or employee engagement in “malicious compliance” or other microaggressions [63, 65]. Most employees prefer to work in an enjoyable and supportive work environment rather than one laden with rules, regulations, fear, and punishments. This is also an important consideration when choosing the design characteristics of an organizational e-training system. We demonstrated that adding the abovementioned design elements could improve a system’s e<sup>fi</sup>cacy and lead to higher levels of motivation.

If our results hold, their implications for security training in practice are noteworthy. Our study provides empirical evidence that e-mail training and e-mail noti<sup>fi</sup>cations designed to help employees avoid phishing attacks might be largely futile. This was particularly useful information for the French company with whom we worked, as they used e-mail training extensively and thought it was more e<sup>fi</sup>cacious than our results indicated. It was no surprise that this contrasting approach yielded far less motivation and immersion; after all, it was not a gami<sup>fi</sup>ed system. However, we were surprised that there was no statistically signi<sup>fi</sup>cant di<sup>f</sup>erence in terms of the actual behavior of the e-mail group and the pure control group. The e-mails were thoughtfully constructed, and they used the same content and many of the same visuals as the gami<sup>fi</sup>cation system; however, employees who received the e-mail treatment had the same outcomes as those who received no training. This is clear evidence that pushing security content to end users via e-mail is not e<sup>f</sup>ective in this context; in contrast to a gami<sup>fi</sup>ed training system, it neither fosters motivations nor strengthens coping.

Following Baxter et al.’s [8] conclusions, and in consultation with the French company, we also realized that conducting training in short, spaced-out segments is more helpful and natural to employees than long training segments. Traditional training in corporate environments can be highly disruptive, time-consuming, unmotivating, and even irritating. We suspect this is also likely true with gami<sup>fi</sup>cation itself: it is more likely to remain novel and fresh if introduced in short segments that provide welcome relief from normal work duties.

These overall results provide proof-of-value in actual practice — not just because our system worked as intended, but because meaningful pragmatic change was introduced to improve the client organization through improved systems and practices.

## Establishing Proof-of-Value in Research

Aside from providing proof-of-value in actual practice, our value extends to challenging and extending gami<sup>fi</sup>ed security research. We do so by o<sup>f</sup>ering a study that addresses compelling research gaps and opportunities in this area and uniquely involves all of the following: (1) long-term data collection; (2) actual working employees in large, international for-pro<sup>fi</sup>t organizations; (3) control and treatment conditions; (4) a mix of perceptual and objective measurement; (5) being grounded in a native IS kernel theory (i.e., HMSAM) that was contextualized to gami<sup>fi</sup>ed organizational security training; (6) an actual working gami<sup>fi</sup>ed training system rigorously designed and developed through DSR principles; and (7) actual empirical demonstration of “meaningful engagement” (e.g., improved IT security compliance) and interaction outcomes (e.g., measurable increased immersion) [cf. 59].

Notably, we are the <sup>fi</sup>rst to use a long-term study in a gami<sup>fi</sup>ed security context. This approach has long been recommended for researching technology-related training in the workplace [97]. As noted, related attempts at one-o<sup>f</sup>, cross-sectional SETA [36] and gami<sup>fi</sup>ed security training [8] have failed to produce increased learning and behavioral change. We argue that the likely reasons for this failure are simple: ful<sup>fi</sup>lling motivations, inducing a state of immersion, fostering learning, and developing coping responses all take time, so it is exceedingly di<sup>fi</sup>cult to produce these outcomes over the course of a brief cross-sectional study. We conclude that gami<sup>fi</sup>cation should be studied using a long-term approach because <sup>fl</sup>ow and immersion occur in stages rather than simultaneously [e.g., 48, 62].

Another research contribution is that actual security compliance was measured and a positive relationship between BI and employee actions in response to the phishing attempts they were trained to recognize was con<sup>fi</sup>rmed. This <sup>fi</sup>nding is in line with previous studies in non-security contexts, and researchers have called for additional studies con<sup>fi</sup>rming the link between intentions and actual security behaviors in various security contexts [22]. Our study is the <sup>fi</sup>rst to examine this important relationship in a gami<sup>fi</sup>ed security context.

## Establishing Proof-of-Value in Theory

We not only were able to demonstrate an e<sup>f</sup>ective DSR kernel theory with our HMSAM application, but we also did so in a manner that can contribute to theory development beyond DSR. Our <sup>fi</sup>rst key contribution here is the extension of HMSAM to a gami<sup>fi</sup>ed security training and compliance context. To do so, we added new constructs to the original model (i.e., security self-e<sup>fi</sup>cacy, security response e<sup>fi</sup>cacy, challenge, learning, and actual security behavior). The addition of new constructs was crucial, as it enabled us to build a working prototype that could empirically establish proof-of-value.

As a further empirical demonstration of our theoretical contribution, the $\mathrm { R } ^ { 2 }$ for BI in our baseline replicated HMSAM model was 0.318; furthermore, our modeling extensions (excluding the trivial contributions of the control variables) literally doubled the $\mathrm { R } ^ { 2 }$ for BI to 0.638. In terms of a pragmatic e<sup>f</sup>ect size, this change is statistically huge $\left( { f ^ { 2 } = 0 . 8 8 4 } \right)$ and pseudo F-test results show that the change is highly signi<sup>fi</sup>cant $( F = 3 2 8 . 8 4 , p < 0 . 0 0 1 )$ 15 Moreover, we added the demographic controls and the counter-explanations of TMSC, OSC, and OCM. Only TMSC was signi<sup>fi</sup>cant, and it contributed only to an extremely small increase in $\mathrm { R } ^ { 2 }$ . As with all of these additions, the $\mathrm { R } ^ { 2 }$ for BI only went from 0.638 to 0.645. This change is statistically trivial $\left( { f } ^ { 2 } = 0 . 0 1 9 \right)$ .<sup>16</sup> Because a pseudo F-test may not be strictly correct and can have limited value, we also used the method to compare nested models by calculating AIC/BIC values for the nested models. We found <sup>fi</sup>t statistics of 2,945.3 (Akaike’s information criterion [AIC]) and 2,988.1 (Schwarz’s Bayesian information criterion [BIC]) for true treatment and <sup>fi</sup>t statistics of 2,231.4 (AIC) and 2,362.3 (Schwarz’s BIC) for e-mail treatment. Overall, these tests provide further evidence that our theoretical contribution is both statistically signi<sup>fi</sup>cant and meaningful in terms of its application in the <sup>fi</sup>eld of highly e<sup>fi</sup>cacious gami<sup>fi</sup>cation interventions.

Moreover, the challenge-related <sup>fi</sup>ndings led to a couple of unexpected key contributions that have the capacity to improve theory, research, and practice in gami<sup>fi</sup>ed security training. We showed that challenge did lead to immersion, but this <sup>fi</sup>nding comes with a crucial theoretical limitation: if the challenge is not appropriate, the results might be undermined. This has long been an underlying assumption of gami<sup>fi</sup>cation and <sup>fl</sup>ow theory [24]. Researchers in these <sup>fi</sup>elds [29] have explained that to experience <sup>fl</sup>ow (or immersion), three conditions should be satis<sup>fi</sup>ed: clear goals, unambiguous feedback, and a balance of challenges and skills. However, to the best our knowledge, what constitutes an appropriate challenge has never been empirically con<sup>fi</sup>rmed. Reviewer feedback on our paper led us to realize that if this limiting assumption indeed holds, there is a point at which a challenge becomes detrimental to fostering immersion; it becomes overly challenging and thus inappropriate. If this continues to hold elsewhere, the relationship between challenges and immersion should not be linear; instead, it should be curvilinear and ideally a quadratic, inverted U-shaped curve that reaches a diminishing marginal return at a certain apex.

We thus conducted a follow-up analysis to run two contrasting regression models; one presenting challenge and immersion as a linear relationship and another presenting it as a curvilinear relationship. The curvilinear model was statistically superior, yielding a statistically higher increase in $\mathrm { R } ^ { 2 }$ (a nearly twofold increase).<sup>17</sup> This means that the relationship between challenge and immersion is in fact ideally modeled as curvilinear. When we visually depicted this relationship with <sup>fi</sup>tted regression lines, the best <sup>fi</sup>t was shown by an inverted U-shaped curve (see Figure 5). This is the <sup>fi</sup>rst empirical evidence for two long-held notions: (1) good gami<sup>fi</sup>cation delivery involves progressive challenges, but (2) such challenges must be appropriate and thus there is a certain point at which a challenge can overwhelm an end user and cause diminishing returns.

Given that challenge is essential to our gami<sup>fi</sup>cation context, we also suspected that challenge would not have a similarly bene<sup>fi</sup>cial relationship in the non-gami<sup>fi</sup>ed e-mail treatment. We thus conducted a similar analysis to test whether the relationship between challenge and immersion in this case was curvilinear. We found two unexpected and fascinating results. First, there was no signi<sup>fi</sup>cant di<sup>f</sup>erence in this context between linear or curvilinear modeling;<sup>18</sup> thus, we can conclude that in our non-gami<sup>fi</sup>ed e-mail training context, the relationship between challenge and immersion was linear. We also found that this was a negative relationship, such that challenge was a detrimental factor (see Figure 6). This makes sense, as an e-mail training environment does not o<sup>f</sup>er the gami<sup>fi</sup>ed features that can turn a challenge into a positive factor, with the result that challenge in an e-mail training environment simply becomes a source of frustration for many employees.

Finally, we learned that the “time dimension” does not favor e-mail treatment. From the initial three months (Table D.4) to six months (Table D.5), we observed stable or decreasing statistical power as time passed, meaning that the e<sup>f</sup>ects of the e-mail treatment diminished over time. The time factor appeared to play an important role in the gami<sup>fi</sup>ed systems (see Figures 5 and 6) because it added a new dimension that should be carefully positioned and built into the gami<sup>fi</sup>ed system. The right balance among time, play, and learning should be carefully designed and chosen so that users do not lose their motivation to learn and play. Our conclusion thus is that the key to improving the French company’s security climate was through gami<sup>fi</sup>ed security training that o<sup>f</sup>ered an appropriate challenge and thus led to a more rewarding and immersive experience that fostered actual behavioral change. If this holds, the theoretical implications are compelling.

![](/api/attachments/EGR62QQJ/fulltext/images/6200db55eb6333f64872f35a1c8d52b43654fe6b9107c8809dd4857ae6e75861.jpg)  
The curvilinear and inverted U-shaped relationship between challenge and immersion. Notes: All the statistics used in this <sup>fi</sup>gure are standardized. Challenge is on the x-axis and immersion is on the y-axis. This shows that challenges are helpful to immersion, but only to a certain point.

![](/api/attachments/EGR62QQJ/fulltext/images/6b3c89f8e5f34680c24b23abda3dd215a2401f2b2a3dd4fc15711b211cba93bc.jpg)  
Linear and negative relationship between challenge and immersion in a non-gami<sup>fi</sup>cation context.

## Research Agenda to Establish Proof-of-Use

Beyond demonstrating proof-of-concept and proof-of-value, according to [75, p. 16], a third concept, proof-of-use can also be applied to DSR. Proof-of-use is demonstrated when DSR

seeks to create self-sustaining and growing communities of practice around a generalizable solution, and to demonstrate that practitioners can successfully create and gain value from their own instances of the generalizable solution.

Thus, proof-of-use is perhaps the greatest limitation and future research opportunity for this research. The <sup>fi</sup>rst obvious issue and opportunity here is that of generalizability. Although we obtained a high degree of ecological validity by using an actual organization and an actual gami<sup>fi</sup>ed security training system, using one organization limits the generalizability of our results. Each organization has slightly di<sup>f</sup>erent and unique security and compliance climates, just as the executives, managers, and employees vary widely. For example, in some organizations, a “shadow IT culture” is widespread [90]. This could produce di<sup>f</sup>erent results, as the security expectations in these organizations are higher than average. Such organizations could exhibit di<sup>f</sup>erences in how employees learn and comply based on individual-level and national-level cultural di<sup>f</sup>erences.

Likewise, building a working prototype was an iterative process in which we actively involved the French organization, as we sought to receive meaningful feedback on the prototype to align it as closely as possible to organizational realities and needs. Consequently, the working prototype may need further modi<sup>fi</sup>cations if adapted to another organization. Regardless, our design principles and kernel theory need to be further modi<sup>fi</sup>ed, applied, and tested, such that the broader practice community is further positively in<sup>fl</sup>uenced — not just the French organization.

Another consideration that needs to be examined for proof-in-use is that we cannot entirely know what outcome would have occurred had traditional manipulations of extrinsic security motivations been used in this setting, as we intentionally did not use them. Again, we took this approach because research indicates that extrinsic motivations are inherently weaker than intrinsic motivations [30, 61] and can back<sup>fi</sup>re in organizational settings. However, mixed motivations are common and can be dealt with e<sup>f</sup>ectively in systems use [61]; thus, it might be possible to create a security environment where the outcomes are maximized through a careful combination of extrinsic and intrinsic motivations. For example, a prize scheme for top performers (e.g., salary increase, bonus payment, or recognition as “security employee of the quarter”) could facilitate further investigations of whether and how these types of motivation in<sup>fl</sup>uence behaviors. It is also important to determine which kinds of extrinsic motivations are the most problematic for this setting.

We also believe this study o<sup>f</sup>ers an ideal opportunity for the kind of future interdisciplinary and programmatic research called for by Nunamaker et al. [74]. For example, our work was conducted over the course of six months with a continual infusion of fresh material. What would happen if the use was extended and the fresh material ran out, such that novelty and challenge diminished? At what point would learning and behavioral change deteriorate? Further research should explore these issues and apply HMSAM to other gami<sup>fi</sup>cation and compliance contexts in which intrinsic motivations and immersion play strong roles. Moreover, the extended gami<sup>fi</sup>ed HMSAM model could likely be applied to other areas of compliance training, such as those related to corporate governance, risk assessment, audit, and other <sup>fi</sup>nancial controls. Our extensions might also work in a compelling manner for iterative IS development processes and requirements engineering.

Moreover, for further proof-in-use, more research needs to examine each element involved in gami<sup>fi</sup>ed security training. We studied an entire system, but each part should also receive further attention. For example, each of the gami<sup>fi</sup>cation elements in Table A.3 could be studied as its own dependent variable with a highly contextualized model and series of studies. Thus, researchers could examine the kinds of avatars that are more likely to enhance a loss of self-consciousness and that are the most autotelic. Or the gamemaster could be the subject of many models and studies. The lack of a gamemaster is a drawback of traditional e-training systems that focus on completion rates or on quantity over quality. The gamemaster, who plays the role of a “positive virtual mentor,” could motivate increased participation. Most employees would likely prefer to be supported by a positive person or positive virtual mentor than nagged by a negative virtual mentor. Based on the analysis of quantitative answers, the gamemaster could provide an individual improvement activity in which learners could improve their knowledge by taking additional quizzes/tests. The gami<sup>fi</sup>cation e<sup>f</sup>ects should then be more e<sup>f</sup>ective and the overall motivation to participate and learn should increase. Consequently, Table A.3 alone points to many possibilities for programmatic research. Another related avenue for future research is to examine in more detail how various levels of media richness (e.g., the use of video, sound, or animation in the communication media) may further in<sup>fl</sup>uence the individual’s security learning process.

## Conclusion

We conducted a DSR project that theoretically and empirically demonstrates that careful design with selected gami<sup>fi</sup>ed IT artifacts can improve extant organizational security training systems. Namely, we show through a long-term <sup>fi</sup>eld experiment that gami<sup>fi</sup>cation can be used to foster training systems that are less invasive of employees’ everyday work routines, that provide intrinsic motivation to learn and comply with security e<sup>f</sup>orts, and that provide the e<sup>fi</sup>cacy necessary so that employees will actually comply. We also demonstrated improvement in actual anti-phishing behaviors by hiring a third-party <sup>fi</sup>rm that phished the employees as a natural experiment to test their reactions. We also provide a novel empirical demonstration of the conceptual importance of “appropriate challenge” in this context. We conclude that a mix of DSR, carefully contextualized kernel theory, and long-term research in an empirical <sup>fi</sup>eld setting is a promising way to e<sup>f</sup>ectively implement gami<sup>fi</sup>cation in organizations.

## Notes

1. Generally, gami<sup>fi</sup>cation is the application of game-like features to nongaming systems to help foster a useful outcome other than entertainment [32, 92]. The features include design elements, such as points, levels, leaderboards, and badges.

2. Namely, they statistically rejected the associated hypotheses “H2: Individuals who receive gami<sup>fi</sup>ed training will exhibit greater knowledge acquisition than individuals who receive non-gami<sup>fi</sup>ed training or no training.” See page 20 of their text for statistical details.

3. Ultimately, users’ behaviors should be in<sup>fl</sup>uenced by the gami<sup>fi</sup>ed tasks in which a <sup>fl</sup>ow experience — or “immersion” in the systems version [3, 22] — is the objective. This objective can be achieved either through intrinsic or extrinsic motivation, but intrinsic motivation tends to be stronger for an instrumental goal [61, 87]. Intrinsic motivation can be involved in the task itself, whereas extrinsic motivation results from external factors (e.g., <sup>fi</sup>nancial rewards or career goals).

4. We aim for both application to practice but also to tackle the challenge of integrating our unique gami<sup>fi</sup>ed security learning context into theory [50]. This is challenging because contextualization is about “linking observations to a set of relevant facts, events, or points of view that make possible research and theory that form part of a larger whole” [86, p. 1]. Following Johns [50], we carefully evaluated, designed, and implemented the implications of contextual appreciation for both theory building and practice to achieve the best possible match between theoretical relevance and practical implications.

5. Meaningful engagement in this context refers to the outcomes of the gami<sup>fi</sup>cation design. That is, the gami<sup>fi</sup>ed system should foster (1) enjoyment, (2) interaction/engagement, and (3) enhanced instrumental task outcomes [59].

6. Other studies have implemented several of the gami<sup>fi</sup>cation design principles, but typically in <sup>fi</sup>elds like computer science. Such studies are especially important for advancing gami<sup>fi</sup>cation-related design and algorithms. However, most either used student subjects, did not advance a “cohesive theoretical foundation,” or did not focus on achieving meaningful engagement, as suggested by Liu et al. [59].

7. The organization we worked with preferred to have a simple system implemented without too much interaction between employees to prevent distractions from their normal work. Thus, we did not apply pie/bar charts, activity stream, giving kudos, social networking, forming teams, providing cash incentives, personalized goals, or social support.

8. For example, a study found that playing the Super Mario Bros. game resulted in a signi<sup>fi</sup>cant gray matter increase, impacting spatial navigation, strategic planning, and working memory [56]. Another example is the use of video games by public safety and military organizations to recruit and train soldiers and to treat their psychological disorders by literally improving their coping and cognitive processes.

9. A couple of the more notable improvements we made included two major adjustments: (1) the number of times a participant could take a quiz was limited because some pilot participants had used automatic clicking tools (such as AutoClicker) as a workaround to earn additional points, and (2) a gamemaster role was implemented, as this role can be an important motivational factor for users.

10. We have no further survey data on the employees who opted to not participate. However, as an accepted surrogate test to assess nonresponse bias, we tested to ensure that there was no statistical di<sup>f</sup>erence between “early” and “late” respondents. We used time stamps of when they accepted joining the project. We grouped early and late respondents and compared their responses to the Likert-type scale questions using a MANOVA test. The results did not reveal any statistical signi<sup>fi</sup>cance (F = 1.976, p = 0.313).

11. The second step of model validation was to test for discriminant validity. Here, we <sup>fi</sup>rst considered whether there was any discriminant overlap in the items in the factor analysis, and we consequently dropped two more items that yielded poor discriminant validity. We then examined overall discriminant validity by placing the square root of the re<sup>fl</sup>ective construct’s AVE on the diagonal line and the correlations between the constructs below it. The square root value of the AVE should be higher than all latent constructs, which was the case.

12. PEOU = perceived ease of use; PIU = perceived intrinsic usefulness; BI = behavioral intentions to follow security policies; OSC = organization security communication; TMSC = top management security commitment; OCM = organization computer monitoring.

13. As the design is unbalanced, we tested the equality of covariance matrices using Box’s M test. The result was not signi<sup>fi</sup>cant.

14. Ecological validity should not be confused with external validity. Ecological validity indicates the degree to which the <sup>fi</sup>ndings of a research study can be generalized to real-life settings, often because they are collected or generated in real-life settings (e.g., actual employees trying to solve real work tasks). Although this form of validity — unlike internal and external validity — is not strictly required for a study to be valid, it is a particularly meaningful but often overlooked consideration for research areas that are highly intertwined with practice, such as security and privacy research [cf. 60].

15. To demonstrate these points empirically, we followed Chin et al. [18] The e<sup>f</sup>ect of adding our contextualized improvements to HMSAM (step 2 of model building) was calculated as follows [18]: $f ^ { 2 }$ (Cohen’s e<sup>f</sup>ect $\mathrm { \dot { s i z e } ) = R _ { \ e x t e n d e d \ m o d e l } ^ { 2 } - R _ { \ H M S A M } ^ { 2 } ) ( . 3 2 0 ) / ( 1 - R _ { \ e x t e n d e d \ m o d e l } ^ { 2 } ) }$ (.362). In this case, $\begin{array} { r } { f ^ { 2 } = 0 . 8 8 4 . } \end{array}$ , which is a $\cdot \mathrm { \Delta } ^ { \mathrm { \omega } _ { \mathrm { h u g e } } ^ { \mathrm { \omega } } \mathrm { \omega } }$ e<sup>f</sup>ect size (anything above 0.35 is considered “large”), is rarely seen in the organizational security literature. To test the statistical signi<sup>fi</sup>cance of this increase, we conducted a pseudo F-test as follows: $f ^ { 2 }$ (Cohen’s e<sup>f</sup>ect size) $^ { * } \left( \mathrm { n - k - 1 } \right)$ , where n is the sample size and k is the number of independent variables. In our case, $\mathrm { n } = 3 8 4 ;$ and we conservatively set k to 11 for all of the constructs preceding BI. This resulted in $\mathrm { F } = 3 2 8 . 8 4 , \mathrm { p } < 0 . 0 0 1$

16. $f ^ { 2 }$ (Cohen’s e<sup>f</sup>ect size) $= \mathrm { R } ^ { 2 } .$ covariate $\mathrm { m o d e l } - \mathrm { R } ^ { 2 }$ extended model) $\bar { ( } . 0 0 7 ) / ( 1 \cdot \mathrm { R } ^ { 2 }$ ) (.362). In this case, $\displaystyle f ^ { 2 } = 0 . 0 1 9$ , which is $\mathrm { ~ a ~ } ^ { \mathrm { \scriptsize ~ \mathfrak { \alpha } } } \mathrm { t r i v i a l } ^ { \mathrm { \scriptsize ~ \mathfrak { \alpha } } }$ e<sup>f</sup>ect size $( ^ { \mathrm { { s m a l l } ^ { \mathrm { { \prime } } } } }$ requires a size of 0.20 or greater).

17. The model summary statistics between Model 1 (linear) and Model 2 (curvilinear; quadratic) are listed in the following table:

<table><tr><td rowspan="2">Model</td><td rowspan="2">R</td><td rowspan="2"> $R^2$ </td><td rowspan="2">Adjusted  $R^2$ </td><td rowspan="2">Std. Error of the Estimate</td><td colspan="3">Change Statistics</td></tr><tr><td> $R^2$  Change</td><td>F Change</td><td>Sig. F Change</td></tr><tr><td>1</td><td> $.332^a$ </td><td>.111</td><td>.109</td><td>.945</td><td>.111</td><td>55.903</td><td>.000</td></tr><tr><td>2</td><td> $.438^b$ </td><td>.192</td><td>.188</td><td>.902</td><td>.081</td><td>45.070</td><td>.000</td></tr></table>

<sup>a</sup>predictors (constant), challenge; <sup>b</sup>predictors (contact), challenge, challenge<sup>2</sup> (quadratic relationship)

18. Using only the data in the e-mail treatment, the model summary statistics between Model 1 (linear) and Model 2 (curvilinear; quadratic) are listed in the following table:

<table><tr><td rowspan="2">Model</td><td rowspan="2">R</td><td rowspan="2"> $R^2$ </td><td rowspan="2">Adjusted  $R^2$ </td><td rowspan="2">Std. Error of the Estimate</td><td colspan="3">Change Statistics</td></tr><tr><td> $R^2$  Change</td><td>F Change</td><td>Sig. F Change</td></tr><tr><td>1</td><td> $.383^a$ </td><td>.147</td><td>.104</td><td>.9687208</td><td>.147</td><td>3.444</td><td>.078</td></tr><tr><td>2</td><td> $.391^b$ </td><td>.153</td><td>.064</td><td>.9903298</td><td>.006</td><td>.137</td><td>.716</td></tr></table>

<sup>a</sup>predictors (constant), challenge; <sup>b</sup>predictors (contact), challenge, challenge<sup>2</sup> (quadratic relationship)

## ORCID

Paul Benjamin Lowry http://orcid.org/0000-0002-0187-5808

## References

1. Abbasi, A; Zhang, Z; Zimbra, D; Chen, H; and Nunamaker Jr, JF. Detecting fake Websites: The contribution of statistical learning theory. MIS Quarterly, 34, 3 (2010), 435–461.

2. Adams, M and Makramalla, M. Cybersecurity skills training: An attacker-centric gami<sup>fi</sup>ed approach. Technology Innovation Management Review, 5, 1 (2015), 5–14.

3. Agarwal, R and Karahanna, E. Time <sup>fl</sup>ies when you’re having fun: Cognitive absorption and beliefs about information technology usage. MIS Quarterly, 24, 4 (2000), 665–694.

4. Ajzen, I. The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50, 2 (1991), 179–211.

5. Ajzen, I and Fishbein, M. Understanding Attitudes and Predicting Social Behavior. Englewood Cli<sup>f</sup>s, NJ: Prentice-Hall, 1980.

6. Bandura, A. Perceived self-e<sup>fi</sup>cacy in cognitive development and functioning. Educational Psychologist, 28, 2 (1993), 117–148.

7. Ban<sup>fi</sup>eld, J and Wilkerson, B. Increasing student intrinsic motivation and self-e<sup>fi</sup>cacy through gami<sup>fi</sup>cation pedagogy. Contemporary Issues in Education Research, 7, 4 (2014), 291–298.

8. Baxter, RJ; Holderness, DK; and Wood, DA. Applying basic gami<sup>fi</sup>cation techniques to it compliance training: Evidence from the lab and <sup>fi</sup>eld. Journal of Information Systems, 30, 3 (2016), 119–133.

9. Benware, CA and Deci, EL. Quality of learning with an active versus passive motivational set. American Educational Research Journal, 21, 4 (1984), 755–765.

10. Boot, WR; Kramer, AF; Simons, DJ; Fabiani, M; and Gratton, G. The e<sup>f</sup>ects of video game playing on attention, memory, and executive control. Acta Psychologica, 129, 3 (2008), 387–398.

11. Boss, SR; Galletta, DF; Lowry, PB; Moody, GD; and Polak, P. What do users have to fear? Using fear appeals to engender threats and fear that motivate protective security behaviors. MIS Quarterly, 39, 4 (2015), 837–864.

12. Brown, SA; Dennis, AR; and Venkatesh, V. Predicting collaboration technology use: Integrating technology adoption and collaboration research. Journal of Management Information Systems, 27, 2 (2010), 9–54.

13. Bui, A; Veit, D; and Webster, J. Gami<sup>fi</sup>cation–a novel phenomenon or a new wrapping for existing concepts? In Proceedings of International Conference on Information Systems, Fort Worth, US, 2015.

14. Bulgurcu, B; Cavusoglu, H; and Benbasat, I. Information security policy compliance: An empirical study of rationality-based beliefs and information security awareness. MIS Quarterly, 34, 3 (2010), 523–548.

15. Burns, AJ; Roberts, TL; Posey, C; and Lowry, PB. Examining the in<sup>fl</sup>uence of organizational insiders’ psychological capital on information security threat and coping appraisals. Computers in Human Behavior, 68, March (2017), 190–209.

16. Chen, X; Chen, L; and Wu, D. Factors that in<sup>fl</sup>uence employees’ security policy compliance: An awareness-motivation-capability perspective. Journal of Computer Information Systems, 58, 4 (2018), 312–324.

17. Chen, Y; Ramamurthy, K; and Wen, K-W. Organizations’ information security policy compliance: Stick or carrot approach? Journal of Management Information Systems, 29, 3 (2012), 157–188.

18. Chin, W; Marcolin, B; and Newsted, P. A partial least squares latent variable modeling approach for measuring interaction e<sup>f</sup>ects: Results from a Monte Carlo simulation study and an electronic mail emotion/adoption study. Information Systems Research, 14, 2 (2003), 189–217.

19. Coonradt, C. The Game of Work: How to Enjoy Work As Much As Play. Layton, Utah: Gibbs Smith, 2007.

20. Cowley, B; Charles, D; Black, M; and Hickey, R. Toward an understanding of <sup>fl</sup>ow in video games. Computers in Entertainment (CIE), 6, 2 (2008), 20.

21. Crossler, RE and Bélanger, F. The e<sup>f</sup>ects of security education training and awareness programs and individual characteristics on end user security tool usage. Journal of Information System Security, 5, 3 (2009),

22. Crossler, RE; Johnston, AC; Lowry, PB; Hu, Q; Warkentin, M; and Baskerville, R. Future directions for behavioral information security research. Computers & Security, 32, (2013), 90–101.

23. Csikszentmihalyi, M. Finding Flow: The Psychology of Engagement with Everyday Life. New York, NY: Basic Books, 1997.

24. Csikszentmihalyi, M. Beyond Boredom and Anxiety. San Francisco, CA, US: Jossey-Bass, 2000.

25. Cyr, D; Head, M; and Ivanov, A. Perceived interactivity leading to e-loyalty: Development of a model for cognitive-a<sup>f</sup>ective user responses. International Journal of Human Computer Studies, 67, 10 (2009), 850–869.

26. D’Arcy, J and Herath, T. A review and analysis of deterrence theory in the IS security literature: Making sense of the disparate <sup>fi</sup>ndings. European Journal of Information Systems, 20, 6 (2011), 643–658.

27. D’Arcy, J; Hovav, A; and Galletta, D. User awareness of security countermeasures and its impact on information systems misuse: A deterrence approach. Information Systems Research, 20, 1 (2009), 79–98.

28. D’Arcy, J and Lowry, PB. Cognitive-a<sup>f</sup>ective drivers of employees’ daily compliance with information security policies: A multilevel, longitudinal study. Information Systems Journal, 29, 1 (2019), 43–69.

29. Davis, M and Csikszentmihalyi, M. Beyond Boredom and Anxiety: The Experience of Play in Work and Games. Washington, DC: Amer Sociological Assoc, 1977.

30. Deci, EL and Ryan, RM. Intrinsic Motivation and Self-determination in Human Behavior. New York, NY: Plenum Press, 1985.

31. Deterding, S. Gami<sup>fi</sup>cation: Designing for motivation. Interactions, 19, 4 (2012), 14–17.

32. Deterding, S; Dixon, D; Khaled, R; and Nacke, LE. From game design elements to gamefulness: De<sup>fi</sup>ning gami<sup>fi</sup>cation. Presented at 15th International Academic MindTrek Conference: Envisioning Future Media Environments, Tampere, Finland, 2011, pp. 9–15.

33. Domínguez, A; Saenz-de-Navarrete, J; De-Marcos, L; Fernández-Sanz, L; Pagés, C; and Martínez-Herráiz, J-J. Gamifying learning experiences: Practical implications and outcomes. Computers & Education, 63, April (2013), 380–392.

34. Edwards, DA; Wetzel, K; and Wyner, DR. Intercollegiate soccer: Saliva cortisol and testosterone are elevated during competition, and testosterone is related to status and social connectedness with teammates. Physiology & Behavior, 87, 1 (2006), 135–143.

35. Fassbender, E; Richards, D; Bilgin, A; Thompson, WF; and Heiden, W. VirSchool: The e<sup>f</sup>ect of background music and immersive display systems on memory for facts learned in an educational virtual environment. Computers & Education, 58, 1 (2012), 490–500.

36. Ferguson, AJ. Fostering e-mail security awareness: The West Point carronade. EDUCASE Quarterly, 28, 1 (2005), 54–57.

37. Floyd, DL; Prentice-Dunn, S; and Rogers, RW. A meta-analysis of research on protection motivation theory. Journal of Applied Social Psychology, 30, 2 (2000), 407–429.

38. Gregor, S and Hevner, AR. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (2013), 337–355.

39. Haans, RF; Pieters, C; and He, ZL. Thinking about U: Theorizing and testing U-and inverted U-shaped relationships in strategy research. Strategic Management Journal, 37, 7 (2016), 1177–1195.

40. Herath, T and Rao, HR. Encouraging information security behaviors in organizations: Role of penalties, pressures and perceived e<sup>f</sup>ectiveness. Decision Support Systems, 47, 2 (2009), 154–165.

41. Hevner, AR; March, ST; Park, J; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

42. Ho, SM and Warkentin, M. Leader’s dilemma game: An experimental design for cyber insider threat research. Information Systems Frontiers, 19, 2 (2015), 1–20.

43. Hong, W; Chan, FK; Thong, JY; Chasalow, LC; and Dhillon, G. A framework and guidelines for context-speci<sup>fi</sup>c theorizing in information systems research. Information Systems Research, 25, 1 (2013), 111–136.

44. Hsu, C-Y; Tsai, C-C; and Wang, H-Y. Facilitating third graders’ acquisition of scienti<sup>fi</sup>c concepts through digital game-based learning: The e<sup>f</sup>ects of self-explanation principles. The Asia-Pacific Education Researcher, 21, 1 (2012), 71–82.

45. Hsu, JS; Shih, S; Hung, YW; and Lowry, PB. The role of extra-role behaviors and social controls in information security policy e<sup>f</sup>ectiveness. Information Systems Research, 26, 2 (2015), 282–300.

46. Hu, Q; Dinev, T; Hart, P; and Cooke, D. Managing employee compliance with information security policies: The critical role of top management and organizational culture. Decision Sciences, 43, 4 (2012), 615–660.

47. Hwang, G-J; Wu, P-H; and Chen, C-C. An online game approach for improving students learning performance in web-based problem-solving activities. Computers & Education, 59, 4 (2012), 1246–1256.

48. Jennett, C; Cox, AL; Cairns, P; Dhoparee, S; Epps, A; Tijs, T; and Walton, A. Measuring and de<sup>fi</sup>ning the experience of immersion in games. International Journal of Human-computer Studies, 66, 9 (2008), 641–661.

49. Jensen, ML; Dinger, M; Wright, RT; and Thatcher, JB. Training to mitigate phishing attacks using mindfulness techniques. Journal of Management Information Systems, 34, 2 (2017), 597–626.

50. Johns, G. The essential impact of context on organizational behavior. Academy of Management Review, 31, 2 (2006), 386–408.

51. Johnson, RD and Marakas, GM. Research report: The role of behavioral modeling in computer skills acquisition: Toward re<sup>fi</sup>nement of the model. Information Systems Research, 11, 4 (2000), 402–417.

52. Johnston, AC; Warkentin, M; and Siponen, M. An enhanced fear appeal rhetorical framework: Leveraging threats to the human asset through sanctioning rhetoric. MIS Quarterly, 39, 1 (2015), 113–134.

53. Kapp, KM. The Gamification of Learning and Instruction: Game-Based Methods and Strategies for Training and Education. San Francisco, US: John Wiley & Sons, 2012.

54. Koepp, MJ; Gunn, RN; Lawrence, AD; Cunningham, VJ; Dagher, A; Jones, T; Brooks, DJ; Bench, C; and Grasby, P. Evidence for striatal dopamine release during a video game. Nature, 93, 6682 (1998), 266–268.

55. Kohn, A. Why incentive plans cannot work. Harvard Business Review, 71, 5 (1993), 54–60.

56. Kühn, S; Gleich, T; Lorenz, R; Lindenberger, U; and Gallinat, J. Playing Super Mario induces structural brain plasticity: Gray matter changes resulting from training with a commercial video game. Molecular Psychiatry, 19, 2 (2014), 265–271.

57. Kumaraguru, P; Sheng, S; Acquisti, A; Cranor, LF; and Hong, J. Teaching Johnny not to fall for phish. ACM Transactions on Internet Technology, 10, 2 (2010), 1–31.

58. Li, M; Jiang, Q; Tan, C-H; and Wei, K-K. Enhancing user-game engagement through software gaming elements. Journal of Management Information Systems, 30, 4 (2014), 115–150.

59. Liu, D; Santhanam, R; and Webster, J. Toward meaningful engagement: A framework for design and research of gami<sup>fi</sup>ed information systems. MIS Quarterly, 41, 4 (2017), 1011–1034.

60. Lowry, PB; Dinev, T; and Willison, R. Why security and privacy research lies at the centre of the information systems (IS) artefact: Proposing a bold research agenda. European Journal of Information Systems, 26, 6 (2017), 546–563.

61. Lowry, PB; Gaskin, J; and Moody, GD. Proposing the multimotive information systems continuance model (misc) to better explain end-user system evaluations and continuance intentions. Journal of the Association for Information Systems, 16, 7 (2015), 515–579.

62. Lowry, PB; Gaskin, J; Twyman, N; Hammer, B; and Roberts, T. Taking “fun and games” seriously: Proposing the hedonic-motivation system adoption model (HMSAM). Journal of the Association for Information Systems, 14, 11 (2013), 617–671.

63. Lowry, PB and Moody, GD. Proposing the control-reactance compliance model (CRCM) to explain opposing motivations to comply with organizational information security policies. Information Systems Journal, 25, 5 (2015), 433–463.

64. Lowry, PB; Moody, GD; and Chatterjee, S. Using IT design to prevent cyberbullying. Journal of Management Information Systems, 34, 3 (2017), 863–901.

65. Lowry, PB; Posey, C; Bennett, RJ; and Roberts, TL. Leveraging fairness and reactance theories to deter reactive computer abuse following enhanced organisational information security policies: An empirical study of the in<sup>fl</sup>uence of counterfactual reasoning and organisational trust. Information Systems Journal, 25, 3 (2015), 193–230.

66. Ma, Q; Pei, G; and Meng, L. Inverted u-shaped curvilinear relationship between challenge and one’s intrinsic motivation: Evidence from event-related potentials. Frontiers in Neuroscience, 11, (2017), 131.

67. Martocchio, JJ and Judge, TA. Relationship between conscientiousness and learning in employee training: Mediating in<sup>fl</sup>uences of self-deception and self-e<sup>fi</sup>cacy. Journal of Applied Psychology, 82, 5 (1997), 764.

68. Mathieu, JE; Martineau, JW; and Tannenbaum, SI. Individual and situational in<sup>fl</sup>uences on the development of self-e<sup>fi</sup>cacy: Implications for training e<sup>f</sup>ectiveness. Personnel Psychology, 46, 1 (1993), 125.

69. Meng, L; Pei, G; Zheng, J; and Ma, Q. Close games versus blowouts: Optimal challenge reinforces one’s intrinsic motivation to win. International Journal of Psychophysiology, 110, December (2016), 102–108.

70. Moody, GD; Lowry, PB; and Galletta, DF. It’s complicated: Explaining the relationship between trust, distrust, and ambivalence in online transaction relationships using polynomial regression analysis and response surface analysis. European Journal of Information Systems, 26, 4 (2017), 379–413.

71. Nelson, MJ. Soviet and American precursors to the gami<sup>fi</sup>cation of work. Presented at Proceedings of the 16th International Academic MindTrek Conference, Tampere, Finland, 2012, pp. 23–26.

72. Nicholson, S. A recipe for meaningful gami<sup>fi</sup>cation. Gamification in Education and Business. Switzerland: Springer International Publishing, 2015, pp. 1–20.

73. Niehaves, B and Ortbach, K. The inner and the outer model in explanatory design theory: The case of designing electronic feedback systems. European Journal of Information Systems, 25, 4 (2016), 303–316.

74. Nunamaker, JF; Twyman, NW; Giboney, JS; and Briggs, RO. Creating high-value real-world impact through systematic programs of research. MIS Quarterly, 41, 2 (2017), 335–351.

75. Nunamaker Jr, JF; Briggs, RO; Derrick, DC; and Schwabe, G. The last research mile: Achieving both rigor and relevance in information systems research. Journal of Management Information Systems, 32, 3 (2015), 10–47.

76. Nunamaker Jr, JF; Chen, M; and Purdin, TD. Systems development in information systems research. Journal of Management Information Systems, 7, 3 (1990), 89–106.

77. Nunamaker Jr., JF and Briggs, RO. Toward a broader vision for information systems. ACM Transactions on Management Information Systems, 2, 4 (2011), 1–12.

78. Osterloh, M and Frey, BS. Motivation, knowledge transfer, and organizational forms. Organization Science, 11, 5 (2000), 538–550.

79. Payne, SC; Youngcourt, SS; and Beaubien, JM. A meta-analytic examination of the goal orientation nomological net. Journal of Applied Psychology, 92, 1 (2007), 128.

80. Pe<sup>f</sup>ers, K; Gengler, CE; and Tuunanen, T. Extending critical success factors methodology to facilitate broadly participative information systems planning. Journal of Management Information Systems, 20, 1 (2003), 51–85.

81. Pe<sup>f</sup>ers, K; Tuunanen, T; Rothenberger, MA; and Chatterjee, S. A design science research methodology for information systems research. Journal of Management Information Systems, 24, 3 (2007), 45–77.

82. Pentland, SJ; Twyman, NW; Burgoon, JK; Nunamaker Jr, JF; and Diller, CB. A video-based screening system for automated risk assessment using nuanced facial features. Journal of Management Information Systems, 34, 4 (2017), 970–993.

83. Posey, C; Roberts, TL; and Lowry, PB. The impact of organizational commitment on insiders’ motivation to protect organizational information assets. Journal of Management Information Systems, 32, 4 (2015), 179–214.

84. Posey, C; Roberts, TL; Lowry, PB; Bennett, RJ; and Courtney, J. Insiders’ protection of organizational information assets: Development of a systematics-based taxonomy and theory of diversity for protection-motivated behaviors. MIS Quarterly, 37, 4 (2013), 1189–1210.

85. Robson, K; Plangger, K; Kietzmann, J; McCarthy, I; and Pitt, L. Understanding gami<sup>fi</sup>cation of consumer experiences. Advances in Consumer Research, 42, (2014), 352–356.

86. Rousseau, DM and Fried, Y. Location, location, location: Contextualizing organizational research. Journal of Organizational Behavior, 22, 1 (2001), 1–13.

87. Ryan, RM and Deci, EL. Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. American Psychologist, 55, 1 (2000), 68.

88. Sen, R; Subramaniam, C; and Nelson, ML. Determinants of the choice of open source software license. Journal of Management Information Systems, 25, 3 (2008), 207–240.

89. Sherno<sup>f</sup>, DJ; Kelly, S; Tonks, SM; Anderson, B; Cavanagh, RF; Sinha, S; and Abdi, B. Student engagement as a function of environmental complexity in high school classrooms. Learning and Instruction, 43, (2016), 52–60.

90. Silic, M and Back, A. Shadow IT–A view from behind the curtain. Computers & Security, 45, (2014), 274–283.

91. Siponen, M and Vance, A. Neutralization: New insights into the problem of employee information systems security policy violations. MIS Quarterly, 34, 3 (2010), 487-502.

92. Treiblmaier, H; Putz, L-M; and Lowry, PB. Setting a de<sup>fi</sup>nition, context, and research agenda for the gami<sup>fi</sup>cation of non-gaming systems. Association for Information Systems Transactions on Human-Computer Interaction, 10, 3 (2018), 129–163.

93. Twyman, NW; Lowry, PB; Burgoon, JK; and Jay F. Nunamaker, J. Autonomous scienti<sup>fi</sup>cally controlled screening systems for detecting information purposely concealed by individuals. Journal of Management Information Systems, 31, 3 (2014), 106–137.

94. Vance, A; Lowry, PB; and Eggett, D. Using accountability to reduce access policy violations in information systems. Journal of Management Information Systems, 29, 4 (2013), 263–289.

95. Vance, A; Lowry, PB; and Eggett, D. A new approach to the problem of access policy violations: Increasing perceptions of accountability through the user interface. MIS Quarterly, 39, 2 (2015), 345–366.

96. Venkatesh, V; Morris, MG; Davis, GB; and Davis, FD. User acceptance of information technology: Toward a uni<sup>fi</sup>ed view. MIS Quarterly, 27, 3 (2003), 425–478.

97. Venkatesh, V and Speier, C. Computer technology training in the workplace: A longitudinal investigation of the e<sup>f</sup>ect of mood. Organizational Behavior and Human-Decision Processes, 79, 1 (1999), 1–28.

98. Wake<sup>fi</sup>eld, RL and Whitten, D. Mobile computing: A user study on hedonic/utilitarian mobile device usage. European Journal of Information Systems, 15, 3 (2006), 292–300.

99. Wang, J; Li, Y; and Rao, HR. Overcon<sup>fi</sup>dence in phishing email detection. Journal of the Association for Information Systems, 17, 11 (2016), 759.

100. Wang, J; Li, Y; and Rao, HR. Coping responses in phishing detection: An investigation of antecedents and consequences. Information Systems Research, 28, 2 (2017), 378–396.

101. Willison, R; Lowry, PB; and Paternoster, R. A tale of two deterrents: Considering the role of absolute and restrictive deterrence in inspiring new directions in behavioral and organizational security. Journal of the Association for Information Systems, 19, 12 (2018), 1187–1216.

102. Willison, R and Warkentin, M. Beyond deterrence: An expanded view of employee computer abuse. MIS Quarterly, 37, 1 (2013), 1–20.

## About the Authors

Mario Silic (mario.silic@unisg.ch) is a post-doctoral researcher at the Institute of Information Management, University of St. Gallen, Switzerland. He holds a Ph.D. from that university. Dr. Silic’s research focuses on information security, open source software, human-computer interaction and mobile commerce. He has published in Journal of Management Information Systems; Security Journal; Information & Management; Computers & Security; and other journals.

Paul Benjamin Lowry (Paul.Lowry.PhD@gmail.com; corresponding author) is the Suzanne Parker Thornhill Chair Professor and Eminent Scholar in Business Information Technology at the Pamplin College of Business at Virginia Tech. He received his Ph.D. in Management Information Systems from the University of Arizona. His research interests include organizational and behavioral security and privacy; online deviance, online harassment, and computer ethics; human-computer interaction, social media, and gami<sup>fi</sup>cation; and business analytics, decision sciences, innovation, and supply chains. Dr. Lowry has published over 130 journal articles in Journal of Management Information Systems (JMIS), MIS Quarterly, Information Systems Research, Journal of the AIS, and other journals. He is a member of the Editorial Board of JMIS, department editor at Decision Sciences Journal, and senior or associate editor of several other journals. He has also served multiple times as track co-chair at the International Conference on Information Systems, European Conference on Information Systems, and Paci<sup>fi</sup>c Asia Conference on Information Systems.
