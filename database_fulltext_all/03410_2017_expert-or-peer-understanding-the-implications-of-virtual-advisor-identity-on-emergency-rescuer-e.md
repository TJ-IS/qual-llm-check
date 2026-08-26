---
otero_id: 3410
otero_key: "YS9CYY9S"
title: "Expert or peer? Understanding the implications of virtual advisor identity on emergency rescuer empowerment in mobile psychological self-help services"
authors: "Manning Li; Zhenhui (Jack) Jiang; Zhiping Fan; Jie Hou"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2017.01.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Expert or Peer? Understanding the Implications of Virtual Agent Identity on Emergency Rescuer Empowerment in Mobile Psychological Self-help Services

![](/api/attachments/YS9CYY9S/fulltext/images/89eecfca90a6d184f3fdf9936b3b9a91f17d78ff489e4ad5a1d03651432cf1a5.jpg)

```html
Author: <ce:author id="aut0005" biographyid="vt0005" author-id="S037872061730006X-3c78dccfbc37f14668992e4b8ca906cc">Manning Li<ce:author id="aut0010" biographyid="vt0010" author-id="S037872061730006X-f1a9e166c6a5b427e73dd8f3885d3db7">Jack Zhenhui Jiang<ce:author id="aut0015" biographyid="vt0015" author-id="S037872061730006X-054cb553d15824454ac2996382e372db">Zhiping Fan<ce:author id="aut0020" biographyid="vt0020" author-id="S037872061730006X-70735036e3b8ec5d271a25f49e15ea2b">Jie Hou
```

PII: S0378-7206(17)30006-X

DOI: http://dx.doi.org/doi:10.1016/j.im.2017.01.002

Reference: INFMAN 2970

To appear in: INFMAN

Received date: 11-4-2015

Revised date: 6-10-2016

Accepted date: 5-1-2017

Please cite this article as: Manning Li, Jack Zhenhui Jiang, Zhiping Fan, Jie Hou, Expert or Peer? Understanding the Implications of Virtual Agent Identity on Emergency Rescuer Empowerment in Mobile Psychological Self-help Services, Information and Management http://dx.doi.org/10.1016/j.im.2017.01.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Expert or Peer? Understanding the Implications of Virtual Agent Identity on Emergency Rescuer Empowerment in Mobile Psychological Self-help Services

## \*Manning Li

Department of Information Management and Decision Sciences, School of Business Administration, Northeastern University, Shenyang 110819, China

## \*Jack Zhenhui Jiang

School of Computing, The National University of Singapore (NUS), 117417, Singapore

## Zhiping Fan

Department of Information Management and Decision Sciences, School of Business Administration, Northeastern University, Shenyang 110819, China

## Jie Hou

Institute of Cyber-physical Systems, School of Information Science and Engineering, Northeastern University, Shenyang 110819, China

\*Corresponding author 1: Jack Zhenhui Jiang Email: jiang@comp.nus.edu.sg Postal Address: School of Computing, The National University of Singapore (NUS), 117417, Singapore

\*Corresponding author 2: Manning Li Email: mnli@mail.neu.edu.cn Postal Address: Department of Information Management and Decision Sciences, School of Business Administration, Northeastern University, Shenyang 110819, China

## Abstract

#

Psychological self-help services on mobile devices play a vital role in supporting emergency rescuers, who engage in highly stressful and self-devoting careers with frequent exposure to dangers and traumatic scenes right after disaster strikes. In this study, we propose and design a low-cost and widely-deployable strategy for empowering emergency rescuers, through an intelligent mobile psychological self-help tool named ERMS. This is to remedy the gap between the limited number of qualified professional counsellors and the high demand for timely psychological support by rescuers. We start with a thorough investigation of user requirements, extant work and relevant IS design theories to inform our system design choices, among which we identified ‘virtual advisor identity’ as needing further research. We then empirically examined how virtual advisor identity influences the empowerment effect of ERMS. Involving 120 emergency rescuers who have just finished rescue tasks, our experiment shows that virtual advisor identity has important impacts on a user’s cognitive and emotional routes, which are significant empowering enablers leading to positive empowerment outcomes. Interestingly, virtual peer advisor empowers users mostly through evoking emotional resonance from them, while virtual expert advisor is better at empowering users through cognitive channels. Important theoretical and practical implications of the findings are then discussed.

Keywords: mobile health advisory services; psychological self-help systems; empowerment theory; symbols of authority; emergency rescuers

## 1. INTRODUCTION

When disaster occurs, a large number of emergency rescuers need to react urgently to the situation and rush to the field of disasters. In face of extreme stressors such as catastrophic scenes, disaster victims and intense work-load, there is a high chance (around 1/3) that they will suffer from Acute Stress Disorder (ASD), which, without timely and proper intervention, can develop into life-long chronic mental problems [1]. However due to a lack of qualified psychologists, there are not sufficient resources to conduct large-scale intervention strategies in developing countries.

The e-health Task Force Report ‘Redesigning health in Europe for 2020’ recommends that people actively manage their health via virtual devices or tools [2]. Increasingly, citizen empowerment through innovative online self-help services becomes popular strategies advocated by governments and health agencies in many parts of the world. Further inspired by the recent champion of online psychological therapies in countries such as UK and Australia [3-5], our study proposes the design of an effective online mental health self-help system to empower emergency rescuers – so that it facilitates their healing, personal growth and mental well-being, to ensure that they continue their invaluable services to the community. This study is also enlightened by the recent emergence of a large number of virtual advisory services on user mobile devices in many fields [6-9], such as healthcare, travel, commerce and academia. These virtual advisory services play a vital role in people’s lives by providing timely and effective advice for users to accomplish a variety of tasks. Yet, limited practical HCI design guidelines are in place to support practitioners in their system design and development, in particular for health advisory systems.

In literature, while there is sufficient attention dedicated to ‘virtual therapies’ alone [4, 10-14], very few studies empirically examine various aspects of the human-computer

##

interaction (HCI) system design implications and the resultant empowerment effects on health consumers. Further, ‘empowerment’, which means ‘to give power to’ people to actively take the initiative to support or help themselves [15], is shown to be of paramount importance to assist patients in need of psychological and physical support in the healthcare sector [16]; to boost the moral of employees in the management discipline [15, 17]; to make the general public more informed and feel transparent about public policy in the public administration sector [18], and to provide support for the relatively underserved minority or disadvantaged groups in the society [19]. Given that one of the ultimate purposes of having online mental health self-help system is to empower emergency rescuers to actively take the initiative to ‘self-help’ through assessing and managing their psychological well-beings, empowerment theory, which needs more empirical verification in the information systems (IS) discipline, is examined further in this mental self-help context. Consequently, there is an urgent need to advance design theories for mental self-help systems from an empowerment perspective in the Information Systems discipline.

In particular, based on our thorough investigation of existing studies, more research is warranted concerning the design characteristics of the virtual advisors, which are popular elements in many innovative virtual advisory systems. Virtual advisor identity is considered to be among the most important HCI design factors for intelligent agents in virtual environments, with other factors being facial expressions, body gestures and speech [20-22]. Little prior study has investigated the impact of these design factors on user empowerment. A detailed scrutinization and synthesis of popular virtual advisory systems in use in the healthcare domain (c.f., Table 1) also led us to focus on the strategies for adopting different ‘virtual advisor identity’ for rescuer empowerment, as have been revealed in our analyses of existing systems.

Motivated by the compelling need in practice and the gaps in the literature, we designed and developed a mobile Emergency Rescuer Mental health Self-help system (ERMS) to provide psychological first-aid to emergency rescuers, in terms of personalized stress-relief and health promotion strategies, with high interoperability, ubiquity, security and adaptivity [23]. Consequently, we research into the following questions:

(1) What are the key factors in the system design that influence the value of ERMS?

(2) How does virtual advisor identity impact the empowerment effect of virtual ERMS for emergency rescuers?

To delimit the scope, throughout the paper, emergency rescuers refer to people serving in organizations that ensure public safety by addressing different major emergencies, such as tsunami, earthquake, fire or flood. The ‘value’ of the virtual advisory system refers to the potential service usage outcome that users can obtain from being empowered through positive experiences in interacting with an appropriately designed system. Further, it is important to note that mental self-help systems are frequently used to complement existing psychological resources in the national health framework, rather than aiming at replacing those health services provided by professionals.

In summary, the study aims at making the following contributions: from a theoretical and methodological perspective, we propose a theoretically founded innovative approach to address one of the key challenges in post-disaster management. To the best of our knowledge, the ERMS system is the first mobile mental health self-help system targeting at emergency rescuers. This study also serves as an interesting example of HCI research for mobile applications that provokes further thoughts on how such studies could be both of high-relevance to practice and design theories in the IS field. The impact of virtual advisor identity on the empowerment effect of mental self-help systems provides insights on how similarity-attractiveness theory underlies the empowerment processes and outcomes related to virtual advisory systems. From a practical perspective, the results of this study are expected to provide concrete advice on virtual advisor design choices for practitioners working in the area of mobile self-help systems. It also aims at drawing more attention and resources of support from the public and the government for emergency rescuers who are devoting themselves to this self-less career. Most importantly, this research will provide meaningful lessons for the national mental-health support network in developing low-cost, effective and large-scale intervention strategies for the long run.

The remainder of this paper is organized as follows. We first present the research background for ERMS, weaving together theories, applicability checks and user requirements underlying the design of such a system. Next, based on in-depth discussions of research hypotheses, we developed our research model. We then present our experiment results and related important findings. Finally, we conclude the study with theoretical and practical implications.

## 2. RESEARCH BACKGROUND

In this study, we developed a mid-range theoretical model. According to Gregor[24], mid-range models are “moderately abstract, have limited scope, and can easily lead to testable hypotheses” and are particularly important for practice disciplines like information systems (p.616). This process involves the following activities that complement and inform each other: a) examining relevant literature; b) preliminary data collection to conduct applicability checks to ground user requirements. This results in constant reflection of the research model, along with adjustments in our understanding and refinement of the model.

## 2.1 Literature review

## 2.1.1 Virtual advisor identity (VAI) in virtual advisory systems

For face-to-face advisories, our immediate cognitive and emotional response after the interaction can be largely shaped by whom we believe we have been talking to and what our perceived ‘self-presentations’ or identities are relative to that advisor [25]. Likewise, in an online advisory session, the identity of the virtual advisor also has important implications for the intervention outcomes of such services, both cognitively and emotionally [20-22].

To ensure the study considers multiple design perspectives drawn from prior research and the industry, we scrutinized a series of virtual health services and psychological health applications in literature and on various platforms, with exemplar ones shown in Table 1. While existing systems in practice represent the status quo, those systems reported in research labs showcase the trends of development for this field. Drawing on the merits of prior systems, we found that the presence of humanoid virtual advisor is a popular strategy adopted by online advisory systems to support users cognitively or emotionally. During our review, we also note an interesting phenomenon in virtual advisor identity (VAI) design: in many instances the virtual advisor’s identity either appears as a ‘domain expert’ ( e.g., such as ‘Dr. Schueler’ in Table 1), providing systematic guidance on people’s wellbeing [12, 26, 27]; or a ‘self-referent character’ (e.g., features that explicitly or implicitly pointing to the self, such as ‘depressed little prince’ in Table 1), which can potentially invoke feelings of social presence and experiential resonances during interactions [3, 4, 6, 28]. Correspondingly, we term these two types of virtual advisors as virtual expert advisors (VEA) and virtual peer advisors (VPA) for the rest of this study.

Questions then emerged from these observations: what are the design considerations behind up-taking these different virtual advisor identities (i.e., VEA vs. VPA); and in particular, how does virtual advisor identity impact the empowerment effect of ERMS on emergency rescuers? Nevertheless, consulting prior work, it is not clear which design choices are considered more ideal for ERMS - little study has investigated the potential effect of virtual advisor identity on emergency rescuer empowerment [29].

As a result, we focus on examining the perplexing issue of virtual advisor identity in ERMS design from an HCI perspective. In particular, our observation and analysis of humanoid virtual advisors in existing systems revealed primarily two types of virtual advisor identities (VAI) , namely VPA and VEA – with interesting and possibly diverse impacts on user empowerment through the virtual advisory systems. With these preliminary findings and design questions in mind, we then explored the theories behind this phenomenon in virtual advisory services .

Table 1 Sample systems in the healthcare self-services area  
(Note: 1: classification based on Barak (1999) and Liu et al.(2011))

<table><tr><td>Source</td><td>Virtual Advisor Identity (VAI)</td><td>System Description1</td><td>Sample Screenshots</td></tr><tr><td>Depressed little prince[28]depression.edu.hk</td><td>Self-referent VPA</td><td>Educational tool;self-help guide; discussion groupsProvide important and fundamental knowledge of depressionMental health self-assessmentParticipate in virtual discussion groups to share experiences and gain insights from other users</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/721bf9a9bf8744768216e42c7576b7180389a8e0cd21b741af3605f284d03da9.jpg"/></td></tr><tr><td>FreeMDfreemd.com</td><td>Domain expert VEA</td><td>Decision support tool.Dr. Schueler analyse a variety of symptoms by step-by-step guidance.Generate reports on the potential causes of symptoms.Help users determine the most appropriate time and place to receive face-to-face healthcare services</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/7ebb32cd2f1b1be974fbf971395705521a48fc3d4534333343d16ac71e157201.jpg"/></td></tr><tr><td>Simcoach[4]simcoach.org</td><td>Self-referent VPA</td><td>Medical information references and psychological self-assessment toolProvide critical information on psychological health and self-recovery skills via interactive dialoguesInformation on seeking appropriate care from healthcare providersOptions of neurocognitive and psychological testing</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/9dac7322ac78bcc84009083367f11739c8f53760e9b966cd57a5f1e21a01a10a.jpg"/></td></tr><tr><td>Virtual nurse agents[12]</td><td>Domain expert VEA</td><td>Tracking tool; Educational toolEducate/counsel hospital patients via interactive dialoguesTest patients' comprehensionProduce a machine-readable index file, specifying the spatial location of the information that will be discussedDisplay unresolved issues to human nurse</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/9d44024ec94cac1fa1e5d3de27ee7517bc8e5bdafa5b51179994ff7cd612a226.jpg"/></td></tr><tr><td>Beating the bluesBeatingtheblues.co.uk</td><td>Self-referentVPA</td><td>Self-help guide-Contain a video introduction in the form of comics-Provide treatment via eight weekly sessions of cognitive behaviour therapy-Arrange homework after each section and then receive feedback from the system.For reference or use by both patients and practitioners</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/1ad877161b2e6f8b6389df2dce7137efe8c8a8eb8d700a4bd8e8ec292ec5b0de.jpg"/></td></tr><tr><td>MoodGYMmoodgym.anu.edu.au</td><td>Self-referentVPA</td><td>Psychological testing and assessment;Self-help guide-Teach the concepts of cognitive restructuring and behaviour therapy-Train assertiveness and self-esteem-Test depression and anxiety.Act as an adjunct to treatment by health professionals.</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/e374c085367bfbe57e8942b95b7f75260c03c641379745cab0c689088262509a.jpg"/></td></tr><tr><td>iCoach CBTAvailable in iTunes Store</td><td>Self-referentVPA</td><td>Medical information references; Tracking tool :self-help guide-Help users who have experienced symptoms of insomnia and would like to improve their sleeping habits-Guide users to learn about sleeping-Develop positive sleeping routines-Information on improving users' sleeping environment.Ideal tool for health providers and patients who have symptoms of insomnia</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/c72679a7f927ad5642b572df209c3402f207cb5d2398089b5f22ab1e91a388bf.jpg"/></td></tr><tr><td>The Stress and Anxiety ManagerChangingstates.co.uk</td><td>Domain ExpertVEA</td><td>Educational tool: self-help guide-Advice on coping with stress and anxiety via multimedia and animations-Provide basic information for learning psychological knowledge-Provide corporate service-Show clients' feedback and comments in the system.Allow users to make appointments online</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/b24ed17942981d17e75351eb2205a7ce47c0f416cf0f0cc89ce72cee4f160059.jpg"/></td></tr><tr><td>OneHealthonehealth.com (acquired by Viverae in 2014)</td><td>Self-referentVPA</td><td>Discussion groups-Access to communities (e.g., depression, anxiety and parent support) and network of peer health coaches, expert discussions and group chats-Access services from browsers or mobile applications-Encourage positive behaviour change-Game mechanics-Check in 'emotionally' to see how other members are feeling</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/79f8be82a730b24ef72618cbcecc9f256bb4757a01418f1f9d32daad38fab705.jpg"/></td></tr></table>

## 2.1.2 Emergency rescuer empowerment through virtual advisory systems

Empowerment helps people to cope with disaster and deal with challenging environmental demands - it is vital not only for the survival and recovery of disaster victims, but also for the life quality of emergency rescuers [29]. Emergency rescuers are both witnesses and participants in these traumatic events – they are very likely to perceive feelings of disempowerment, including losing their inner emotional control and a sense of powerlessness facing with stressful scenes and challenging work situations on a regular basis [30]. The high stress and increasing suicide among emergency rescuers has recently drawn much attention from government agencies and the society[31]. There is also an increased awareness of research studies and availability of support programs for emergency rescuers. Along with these positive changes, views of mental health and wellness within the emergency service community have gradually transformed over the years. What was once suffered in silence is now recognized as being integral to an emergency rescuer’s health and career sustainability. Emergency rescuers face challenging and traumatic events that can impact their mental wellbeing daily in an intensive way. A high percentage of them suffered from emotional problems such as anxiety, fear or depression, and are struggling for maintaining their inner sense of control and the confidence to face with work challenges and continue their rescue career [30-32]. Without strategies for proper and timely intervention, these may develop into a series of post-traumatic stress disorder (PTSD) symptoms such as sleeping disorder, vomiting or frequent nightmare, or even destructive behaviors such as self-injury, alcohol or drug addictions or suicidal behaviors [29, 31].

Early intervention is key to resolve the current issue. Therefore, emergency rescuer empowerment through always-accessible, low-cost and large scale ICT intervention strategies helps to ensure the sustainability of this critical public resource, which supports the safety and wellbeing of the public and the society[29, 32]. To empower emergency rescuers through online ERMS means that, through the provision of an intelligent psychological advisory tool to assist emergency rescuers in recognizing, managing and seeking assistance for their mental health issues, they are more prepared to combat the aforementioned issues of disempowerment. Through the resources provided by ERMS, emergency rescuers become more familiar with mental health issues and are also more aware of ways to maintain their inner emotional control and their perceived confidence or power to deal with work challenges, facilitating the general well-being of the rescue career [32].

Empowerment as an identifiable concept originally emerged from the research areas of organizational science and management [33-35], psychology[36, 37] and health and nursing [38-40]. The different conceptualization of empowerment include: “to give power to” [33]( p.666); “to enable people to do things that they would otherwise be unable to do”[41] ( p.37); “encourage them[people] to be more involved in decisions and activities” [35](p. 9); and “a process by which people, organizations, and communities gain mastery over issues of concern to them” [37] (p.581). Specifically, in the context of patient and healthcare provider interactions, empowerment is defined as ‘a social process of recognizing, promoting, and enhancing people’s abilities to meet their own needs, solve their own problems and mobilize the necessary resources in order to control their lives’[38]. Empowerment theory is said to be applicable to both the micro level (e.g., individuals), as well as the macro level including organizations and communities, which interact and influence each other. Moreover, at the individual level, the empowerment of people can be achieved via two major dimensions: empowering them through 1) cognitions (e.g., learning new knowledge or skills) and 2) emotions (e.g., feelings of support and affiliation) [33, 37, 38, 42-44].

A thorough scrutinization of relevant literature identified a wide range of theories and factors in system design that potentially affect the value of virtual advisory services [45-53]. However, as suggested by Swearing et al. [53], designers should be clear that they need to focus on the ‘purported role’ of the advisory system, that is, ‘it’s primary purpose’. Thus, despite the rich set of design dimensions and constructs raised in literature, we centered our study around the theme of ‘emergency rescuer empowerment’ due to its high relevance for healthcare systems and in particular the ‘patient self-help’ domain as pointed out in a number of prior studies [38, 54]. In the context of this study, emergency rescuer empowerment means to give power to emergency rescuers to self-help through virtual mental-health advisory systems to achieve more power and control over their lives. Further, Zimmerman [15] pointed out that it is essential to differentiate between two components of the empowerment theory: empowering enabler/processes and empowerment outcomes. Empowering enablers can be viewed as the resources or opportunities that allows patients to control their own fate or influence their decision-making and behavior [15]. On the other hand, empowered outcomes refer to achieving a sense of control and perceived power as consequences of the interventions or mechanisms designed for an empowering process[15, 55], as discussed further below.

## a. Empowering Enablers

Literature suggested that people, such as employees, patients or consumers, can be empowered mostly through two major dimensions, namely the cognitive and emotional dimensions [33, 37, 38, 42-44]. Typical strategies for empowering people through their cognitive dimensions include allowing them to acquire new knowledge or skills, or equipping them with capabilities to solve their own problems that they otherwise unable to achieve [35, 38]; whereas empowering people through emotions or feelings can be achieved through promoting their feelings of affiliation, support, or other positive affects within a certain context [37, 43, 44]. Considering the role of ERMS, this above classification aligns well with Benbasat’s [56] idea that IT artefacts are not only productivity-enhancing tools, but also enablers for ‘interpersonal’ communications, in which they are regarded as social actors or agents. In other words, except for serving as educational tools (e.g., to acquire knowledge), a rich set of emotive interactions such as human-like behavior, emotions and personalities can also be attributed to virtual advisory services that potentially invoke different user feelings [57]. If appropriately designed, ERMS can not only pass on psychological knowledge for emergency rescuers, but also potentially create feelings of social and interpersonal interactions for them. Furthermore, a number of salient studies in the IS field analyzed the impact of virtual advisory systems or web stores on users from two aspects, namely the cognitive and emotional (or affective) aspects [50, 58] .

Drawing on the above understandings, we investigate the role of ERMS in emergency rescuers’ empowering processes from two major dimensions: (1) the cognitive aspects (e.g., knowledge acquisition); and (2) the emotional aspects (e.g., feelings of social emotional support).

The cognitive aspects of user experiences include the processing of information (e.g., attention and memory), applying knowledge or changing preferences, which can be a natural or artificial, conscious or unconscious process [59]. In health promotion, the development of cognitive skills of patients plays a critical role in empowerment, and determine the motivation and ability to obtain, understand and use the information to stay healthy [17]. The social cognitive paradigm also states that people’s cognitive ability has a significant influence on people’s judgment and behavior [60]. Given that one of the primary purposes of ERMS is the effective delivery of psychological knowledge, it is reasonable to expect that the cognitive empowering enablers or processes is primarily demonstrated via users’ enhanced level of perceived understanding (PU) and actual understanding (AU) of psychological knowledge, which has significant values for the mental well-being of emergency rescuers. Besides, we study both perceived understanding and actual understanding to differentiate between people’s own perception and the actual knowledge obtained, which allows for a comprehensive understanding of how ERMS pass on knowledge to users. Similar approaches have been demonstrated effective in digging more insights behind complex problems of enquiry [48]. To elaborate, perceived understanding reflects the extent to which the

##

knowledge is considered as easy to read and understand [61]. This can be enhanced through appropriate service delivery mechanisms, such as the choosing a suitable style of presentation of the information content, or providing animations or live examples in explanations [62]. Emergency rescuers with a higher level of perceived understanding of psychological knowledge, are more likely to feel empowered through this cognitive empowering process. In contrast, while using a virtual advisory system, actual understanding reflects a user’s actual absorption of knowledge, which potentially influence the subsequent application of this knowledge. Prior studies show that information contents that originates from authoritative sources can promote users’ actual understanding of advisory contents [63], which subsequently influence users’ confidence and effectiveness [64]. Therefore, from the cognitive dimensions, we consider both perceived understanding and actual understanding as among the key empowering enablers, affecting emergency rescuers’ empowerment outcomes after using ERMS.

From an emotional perspective, social emotional support are well-established strategies for the empowerment and healing of people with mental problems to regain a sense of control and power over their lives[44]. Obtaining social companionship (i.e., social presence) and empathy (i.e., experiential resonance) are the two most important elements to attain empowerment affectively [44, 65, 66]. For example, traditional mutual-help groups are found to be extremely effective in promoting a sense of empowerment for people [67]. Support from peers or similar others can help people obtain emotional relief and resonance through sharing similar experiences or confusion - this can create empathy and support fostering personal empowerment [55]. The demand for such emotional support from ERMS, including a sense of social presence and feelings of experiential resonance, has also been raised by emergency rescuers[32]. To elaborate, social presence refers to feelings that ‘an artefact is perceived as sociable, warm, personal, or intimate when interacting with it’ [68]. People have a higher sense of involvement and companionship when interacting with human-like elements in the virtual environment, which results in a sense of social presence [45]. This is also reflected in the requirements elicitation process, in which emergency rescuers wish to communicate with a virtual advisor who can make them feel warm and sociable. In addition, experiential resonance is another important emotional empowering dimension examined in this study. It describes the ability of information to move through available affective channels to the client, subsequently invoking that client’s mental models about themselves [69]. Social interactions, through availability of rich mediums, are found to be able to enhance users’ sense of resonance [69]. Moreover, resonance or empathy can also be evoked by performing similar actions or experiencing a similar emotion [22]. Thus, emergency rescuers are expected to go through experiential resonance during their interactions with virtual advisors in ERMS, especially when the advisor exhibits similar traits in a number of important dimensions. In summary, we consider social presence (SP) and perceived experiential resonance (ER) as two key elements of the user’s emotional empowering aspects after using ERMS.

## b. Empowerment Outcomes

Sense of control and perceived power, which are considered two key dimensions of empowerment as raised by Zimmerman [15], are critical for forming a sense of ‘emotional safety’ for emergency rescuers when dealing with external threats such as catastrophic scenes or inner threats such as stress or depression [70].

A number of studies have shown that, when people become empowered during a certain interaction process, they perceive a greater sense of self-control over their mental conditions or life values, and generated greater power or confidence towards challenging situations [15, 16, 36, 37]. If appropriately designed, the cognitive and emotional empowering processes via ERMS are also expected to reduce emergency rescuers’ feelings of helplessness [55], subsequently allowing them to gain more control and power over their lives [16, 67]. Therefore, we focus on ‘sense of control’ and ‘perceived power’ as two primary dimensions of empowerment outcomes to be assessed in our research model.

In summary, in the scope of ERMS being a virtual advisory system in the health domain, we have taken an empowerment theory perspective in examining the effectiveness of our system design. This rationale is also supported by ‘emergency rescuer empowerment’ being a core theme underpinning the idea of designing ERMS - to empower rescuers with readily available psychological knowledge and feelings of social support to boost their inner sense of control and perceived power towards future work challenges.

## 2.1.3 Virtual advisory identity (VAI) and empowerment

Identity has been viewed by many theorists as ‘the joining point’ between an individual person and the society. It occurs in any communications or interactions, in which a person internalize on a self-ascribed role and project these understandings onto the other communicator [25]. During social interactions, people’s cognitive and emotional responses are frequently manipulated by the identity of the other interaction party – just as you may respond differently to advices offered by your friends and those offered by your parents. The same holds for online interactions. A very recent study on online P2D (Patient-2-Doctor) community uncovers that patients consider information from physicians and peers as two distinct sources and they value both sources differently [71]. In particular, patients regard physicians as authoritative experts who are able to provide ‘reliable’ and evidence-based information based on scientific research; while advice from peers is considered to be experience-based information, which results in more personal reflections or self-resonance.

To explore further what different virtual advisor identities (e.g., virtual expert advisors and virtual peer advisors) mean for ERMS user empowerment, the ‘symbols of authority’ and ‘similarity-attraction’ view in literature provide unique lenses that help us uncover users’ underlying cognitive and emotional reactions towards virtual health advisors with authoritative or similar identities.

‘Symbols of authority’ are frequently reported to lead to mental shortcuts that make people

##

believe that they should be listening to the party exhibiting these traits, including behavior, manner, title, appearance and others [46]. Hewgill and Miller[72] found that the same communicator, when manipulated to dress up in Professor style, gain more appreciation and trust from message recipients, compared with dressing up in High school sophomore style. Participants also perceive the message content as more credible. Another interesting study by Bickman shows the ‘social power of the uniform’, that a person imposed as a security guard to ask strangers to do things achieved more compliance than a person wearing normal clothes [73]. Hofling et al. revealed that the title of “Dr.” was a compliance-gaining device for effective persuasion[74]. In particular, uniforms are recognized symbol of authority which can potentially bring about monotonous compliance [46]. In real life, emergency rescuers are people who frequently need to follow instructions from their officers or group leaders to ensure a rescue task being carried out effectively. We expect that when the virtual advisor appears in virtual expert advisor style, users are more likely to accept and follow the persuasive message and psychological knowledge, which potentially leads to better empowerment outcomes including heightened sense of perceived power towards work challenges and better inner sense of control.

In contrast, the similarity-attraction view states that individuals are attracted by persons who share similar character traits with themselves [75]. People who are similar can get along well with each other and improve mutual understanding, which can result in spiritual and emotional support. In Theories of human communications, Littlejohn and Foss [25] state that when communicators discover similarities with each other, ‘their attraction to one another goes up, and their apparent need for more information goes down’ (p. 131). A number of researchers have investigated similarity theory in different contexts, such as facial similarity, personality similarity, behavior similarity, decision process similarity and communication style similarity [25, 46, 76, 77] . Nevertheless, little study has focused on the influence of identity similarity on system users in the information system discipline. To elaborate, identity

#

similarity means that people share similar social identities-they might have suffered from similar experiences, which could enhance their feelings of social rapport or support [78]. In our study, emergency rescuers can consult a virtual peer advisor who has gone through similar difficulties or distress in their work. The helpful advices from a virtual fellow mate who shares his/her own experiences on effectively ways of dealing with troubles and problems in an online environment, can bring users emotionally closer and create feelings of social presence and experiential resonance [44]. Moreover, peer support is of pivotal importance to personal empowerment - interacting with a peer advisor can strengthen people’s personal competence, self-determination and social engagement [67]. Consequently, through interacting with a virtual peer advisor that potentially evokes feelings of social presence and experiential resonance, emergency rescuers are expected to feel empowered, having more self-control over inner emotions and more confidence or power in dealing with external challenges in social environments [78].

Given the above theoretical backgrounds, we find it important and interesting to scrutinize empirically how these two types of virtual advisor identities impact on the empowerment effect of ERMS.

## 2.2 Exploratory reality check to ground user requirements

As an integral part of the research process, conducting ‘reality check’ (a.k.a., applicability check) prior to the core part of the research activities is advocated in the seminal work by Rosemann and Vessey [79]. When carried out prior to the core research activities, this approach helps to ensure the research problem ‘was grounded in practice’.

In order to ground our study in user requirements, we interviewed ten emergency rescuers randomly chosen from a fire brigade in a large city in China. The average age of the participants is 25 years old. When we arrived at the interview site, we were told that due to the special nature of this occupation, most of the on-site rescuers are male. Thus, our

##

interview participants are male. Eight participants graduated from senior high school and the other two participants graduated from colleges. Their working experiences in the rescue field ranged from two to ten years. In addition, all reported that they had accessed the Internet through both personal computers and mobile phones. A semi-structured and in-depth approach was taken to interview each emergency rescuer on their psychological needs in their work contexts and their requirements for ERMS [80]. Each interview lasts from 30 minutes to 50 minutes. During the interview, we center around two major issues: a) reality checks on the problem context to explore whether there is any actual need for psychological support from emergency rescuers. Typical questions include: “How do you feel after completing your recue tasks?” and “Do you think the current supporting strategies from your organizations are sufficient in this aspect?”; and b) what emergency rescuers need from ERMS to empower them. The core questions include: “What do you wish to see in an emergency rescuer mental self-help system?” and “How do you want such a system to help/support you?” After data collection, open, axial and selective coding methods were used to analyze the transcribed interview data, following the procedures of qualitative data analysis proposed by Corbin and Strauss [81, 82] (Appendix Table A-2). Two coders independently conducted the coding of the transcript. The Cohen’s Kappa scores averaged 0.82, indicating a high level of inter-coder reliability based on Landis and Koch’s criteria[83]. Based on feedback from the respondents, the major findings were summarized as follows.

## a. reality checks on the research context

First, the need for ongoing emotional support for the rescuer occupation has been raised. Emergency rescuers, especially the novices, frequently experience negative emotions such as fear, anxiety, insecurity, or even the related symptoms of physical discomfort (e.g., vomiting or apocleisis). A number of them frequently felt upset or experienced reoccurring nightmares in which the traumatic scenes are reproduced after rescue tasks. They report feeling worse while being alone or at night. Existing mental health supporting strategies are neither timely nor sufficient to address these issues. In addition, while being exposed to traumatic scenes or after completing difficult rescue tasks, some of them had occasions of feeling powerlessness or losing confidence towards their future work challenges. It is also mentioned that some people resign from rescue careers or change their role/positions due to the great psychological pressure they encounter.

Second, emergency rescuers are currently lack of readily access to appropriate psychological self-help knowledge. A few traditional intervention measures have been taken by their organizations, such as paper-based screening tests or award ceremonies, to boost rescuers’ morale. However, emergency rescuers call for more readily access to psychological support, such as on-going self-assessment and tailored advice to maintain their psychological well-being. Many have limited psychological self-help knowledge and biased view such as ‘bearing with these negative emotions’ is the only way to resolve their psychological unfitness. Further, most new recruits have not received sufficient formal training on mental health prior to beginning rescue tasks. They mainly rely on themselves or talking to more experienced peers to alleviate their negative emotions.

Based on the reality check, we identified the compelling need from emergency rescuers for more readily cognitive and emotional support and confirmed that the current situation urgently calls for large-scale intervention strategies targeting emergency rescuers’ psychological wellbeing.

## b. requirements for ERMS

To address these aforementioned issues, respondents felt that for ERMS to be truly empowering, the following requirements should be met, as summarized below.

First, in terms of cognitive empowerment through ERMS, they proposed that ERMS should be able to provide tailored professional psychological knowledge targeted at the rescuer occupation, displaying this information and knowledge in a lively and intuitive way,

#

either as text, video or animation to facilitate their knowledge acquisition and understanding. In addition, ERMS should also have psychological self-assessment functions, and capabilities to generate personalized health evaluation reports for further reference, to ‘empower’ them to have a better understanding of their own situation which they otherwise normally would not be able to achieve. Emergency rescuers also mentioned that it would be good to incorporate the functionalities of monitoring emergency rescuers’ physical and mental indices with mobile devices or portable hardware devices into ERMS. They also raised the idea of displaying physiological information that reflects the mental status of rescuers intuitively in the form of graphs or column diagrams, and providing timely and effective practical advice.

Second, to fulfill their needs of emotional empowerment through ERMS, they commented that ERMS designer should take note to include functions that can help with adjusting the psychological pressure of rescuers, including 1) feelings of human warmth and accompany, and also 2) emotional support and resonance from those who share similar occupational experiences with them. For example, they reflected that the company of an always-available, friendly and intelligent virtual advisor would give them more control over their emotional status and confidence in dealing with negative emotions and work challenges. Besides, some rescuers suggested social networking functions, while highlighting the importance of protecting their privacy.

Finally, what forms a difficult, yet interesting design choice is that some emergency rescuers suggested having a counselor type virtual advisor (i.e., Virtual Expert Advisor, VEA); whereas others preferred having someone with similar experiences to interact with (i.e., Virtual Peer Advisor, VPA). There is no consensus among these rescuers. Further, it remains unclear how virtual advisor identity impact the aforementioned empowerment effect of ERMS for emergency rescuers. Therefore, the impact of virtual advisor identity (VEA vs. VPA）on the value of ERMS needs further exploration.

##

Given these feedback from emergency rescuers during the reality check, we are confident in the high relevance and value of this research issue. Moreover, through subsequent user requirements elicitation for ERMS, we identified how ERMS can empower emergency rescuer both cognitively and emotionally. We also noticed an important design concern of virtual advisor identity (VAI) that potentially impact on the above value of ERMS and thus needs further empirical examination. Our preliminary interview results aligns very well with literature in that the main identified concepts conforms to our theory predictions. To elaborate, in terms of cognitive empowerment, emergency rescuers need a good understanding of psychological knowledge facilitated by such a system. While for emotional support, emergency rescuers are longing for a sense of accompany (i.e., social presence) and empathy (i.e., experiential resonance) from such an intelligent advisory system. Therefore, we analyze user experiences with ERMS surrounding these key concepts underpinned by empowerment theory in our research model.

## 3. RESEARCH MODEL AND HYPOTHESES DEVELOPMENT

As discussed in the ‘Research Background’ section, the virtual advisor’s identity either appears as a virtual expert advisor (VEA), who delivers knowledge in the style of a domain expert; or in the form of a virtual peer advisor (VPA), a self-referent character providing support as peer workers. Virtual advisor identity is deemed an important aspect of the system design choice for impacting on the intended empowerment outcomes of a psychological self-help system. Yet, for this relatively under-researched topic, more attention is warranted to understand the potential effects of virtual advisor identity on user perceptions. From exemplar systems in Table 1, we can see that ‘self-referent’ features, which usually appear in forms of virtual advisors sharing similar identities with the users, can potentially attract users and enhance their feelings of familiarity, support and experiential resonance. On the other hand, systems that use ‘domain experts’ with authoritative or professional images are shown to have the potential to provide users with systematic guidance that can enhance their understanding of psychological knowledge. The implications of virtual advisor identity for ERMS design are discussed in each hypothesis in further detail below.

ERMS aims at empowering emergency rescuers both cognitively and emotionally. Thus knowledge is one of the most important resources to equip emergency rescuers with the necessary cognitive skills to cope with difficult situations. Perceived understanding in this study refers to how informed the user felt that he or she is on the knowledge learnt through ERMS. Literature has shown that, in contrast to non-professionals, knowledge provided by experts is regarded as more authoritative and professional [71]. Prior studies also raised that people frequently ‘embrace the short cut of assuming that people who simply display symbols of authority should be listened to’[46] (p.460). A number of interesting empirical studies also revealed that people would think higher of and follow those who dressed up with uniforms that show more authoritative identities such as professors or security guards [12, 72]. As a result, the majority of people are likely to perceive knowledge provided by experts as more acceptable [84]. Further, compared with peer advisors, experts’ advice can facilitate users’ trust in information with increased sense of transparency [85]. Therefore, people tend to perceive that they are more informed about the knowledge being transferred to them through expert advisors than peer advisors. Consequently, we anticipate the same holds for emergency rescuers while interacting with virtual advisors.

H1: In contrast to virtual peer advisors (VPA), emergency rescuers’ perceived understanding of the psychological knowledge provided by the mental health advisory system is better with virtual expert advisors (VEA).

In comparison with perceived understanding, actual understanding refers to how much actual knowledge users have grasped through using the virtual advisory system. A number of empirical studies have proved that there is a gap between perceived understanding and actual

#

understanding of knowledge (Southwell et al., 2012). While perceived understanding resembles more of the user’s satisfaction, actual understanding represents how much exactly the users have learnt. Assessing the users’ actual understanding of knowledge through quizzes or tests is a common consensus among educators and researchers - we have therefore taken the same approach in this research. In literature, the reputation of the sources of recommendation agents is reported to influence users’ acceptance of the tool and the advice, including the recommendation agent’s competence, benevolence and integrity in users perception [63, 86]. There is also a social norm that people in general would regard those who seek for expert advice as more competent than those seeking advice from non-experts [87]. In addition, significant increase in advice utilization has been observed when the user perceives that the advisor has higher level of task-related expertise [86]. Literature has also shown that knowledge that is systematically elaborated by an authoritative source can satisfy patients and promote more in-depth actual understanding of the knowledge [12]. People would also achieve better performance through accepting experts’ advice, compared with non-professional sources [86] Hence, it is likely that emergency rescuers process knowledge provided by virtual expert advisors with more serious attitude and cognitive effort, compared with those provided by virtual peer advisors. Moreover, when emergency rescuers form positive perceptions towards the online advices given by credible sources like experts, they are more likely to digest and follow the advice to a greater extent and achieve good learning outcomes [88]. Thus, for emergency rescuers, who are frequently trained to follow instructions from officers and authorities in their occupation, it is expected that they will accept and digest the psychological knowledge from virtual expert advisors in a more in-depth way.

H2: In contrast to VPA, emergency rescuers’ actual understanding of the psychological knowledge provided by the mental health advisory system is better with VEA.

#

Social presence refers to the users’ feelings that the virtual advisor in ERMS is perceived as ‘sociable, warm, personal, or intimate when interacting with it’ [68]. The existence of humanoid virtual advisors can potentially make individuals perceive that they are coexisting with other social beings [89]. When appropriately designed, this addresses one of the primary emotional needs of emergency rescuers – feelings of having human support, warmth and accompany. Abundant literature suggests that individuals enjoy communicating with people with similar traits to themselves [25]. This is because during social interactions, people have the anxiety to reduce uncertainty about the other party so as to predict his or her behavior and other relevant consequences of this interaction. Similar personal traits such as body gestures, dressing styles or social identity help to eliminate this uncertainty and tend to bring people closer emotionally [25]. On the other hand, authoritative figures such as virtual expert advisors are more likely to generate emotional distancing. Prior study has also revealed that users perceive stronger social presence when interacting with advisors with similar backgrounds such as ethnicity or similar decision processes [46, 90]. Likewise, we expect that, for emergency rescuers who are seeking for emotional and cognitive support from ERMS, VPA will make rescuers perceive more rapport and human warmth than VEA and are therefore expected to enhance the users’ feelings of social presence.

H3: In contrast to VEA, VPA will result in higher sense of social presence for emergency rescuers while using the system.

Perceived experiential resonance refers to people’s perceptions that the virtual advisor in the system shares traits of similar personal experiences as they themselves have gone through. Thus, they are considered as ‘in-group’. The special feelings of having gone through similar events or things in life can greatly facilitate the formation of a relationship of mutual understanding, trust and agreement [25]. ‘I have gone through similar things in life’ is considered to be of utmost importance while establishing rapports with emergency rescuers. People who share similar experiences, expertise or preferences have similar interpersonal traits [91], which can arouse a sense of emotional resonance. Prior study also demonstrated that performing similar activities or experiencing similar emotions or situations can evoke interpersonal resonance among people [22]. Through interacting with a peer advisor, emergency rescuers have the feeling that this advisor has a high degree of overlap and commonality with them, such as in beliefs, expectations, perceptions about career goals and professional knowledge. Goal similarity was also demonstrated to have positive impacts on interpersonal attraction in literature [92]. In addition, shared understanding can be helpful in bringing people together, in particular with establishing rapport, commitment, satisfaction and longevity in collaborations [93]. Therefore, if emergency rescuers consult a VPA who is regarded as sharing common career goals, understanding and experiences with them, they are likely to feel more experiential resonance during the consultation process. Hence, we expect that VPA can positively influence perceived experiential resonance compared with VEA.

H4: In contrast to VEA, emergency rescuers perceive VPA as more capable in triggering their experiential resonance while using the system.

(Inner) sense of control in this context refers to emergency rescuers’ belief that their voluntary activity of using ERMS can have a positive influence on their inner mental status, such as becoming more calm and emotionally stable. Sense of control is said to be closely related to people’s thought patterns, emotional arousal and changes in behavior [50] and is therefore considered as one of the most important empowerment outcomes for emergency rescuers. Gibson sees empowerment as a social process through which people mobilize the necessary resources to obtain sense of control of their own lives. In this process, people proactively recognize, promote and enhance their own abilities to fulfil their own needs and solve their own problems [38]. While using ERMS, emergency rescuers actively mobilize their cognitive resources (i.e., knowledge learnt from virtual advisors) to gain a better sense of control over their inner status.

##

Literature suggests that perceived mental transparency enables users to enjoy a high level of sense of control [50]. To elaborate, this is because perceived clarity about what will be experienced and what the process will be like, potentially leads to greater predictability and consequently greater sense of control [94]. Besides, actual knowledge acquisition as a result of using an advisory system significantly impacts user’s sense of control [95]. Knowledge has been demonstrated in healthcare literature to significantly increase patient’s sense of control [96]. Furthermore, one key assumption underlying empowerment theory is that acquiring psychological skills or information can enhance patients’ sense of autonomy, self-efficacy and self-awareness [16]. While ERMS are knowledge-based resources that allows emergency rescuers to conduct self-help with autonomy, we expect that such a cognitive support can make emergency rescuers feel more calm and emotionally stable, which means a higher sense of control over their inner emotional status. Thus, we expect that both perceived understanding and actual understanding of psychological knowledge can contribute to a better sense of control over their inner mental status for emergency rescuers.

H5 Improvement of perceived understanding will increase emergency rescuer’s sense of control.

H6: Improvement of actual understanding will increase emergency rescuer’s sense of control.

Emotional support is also of paramount importance for emergency rescuers in developing a sense of inner control over their mental status. Studies have shown that social presence is a significant antecedent to users’ behavior and attitudes in the context of virtual worlds [97] and individuals perceive more self-control while experiencing social presence [98]. Likewise, when emergency rescuers perceive a higher sense of human warmth and accompany through interacting with the virtual advisor in ERMS, they are more likely to develop a sense of inner strengths and control. Moreover, sense of control can also be enhanced through self-referent mechanisms [99], a core mechanism for invoking personal experiential resonance. This happens as a result of reflecting on one’s own situation upon witnessing or listening to other people’s story in similar contexts. It is found in literature that people perceive more sense of control and support while sharing common experiences with each other on social networking sites [70]. Prior research has also uncovered that shared languages and codes in social networks are positively associated with a sense of control [100]. We thus expect that feelings of heightened experiential resonance while interacting with ERMS will lead to a higher sense of control as perceived by emergency rescuers. Therefore, we hypothesize:

H7: A better sense of social presence will increase emergency rescuer’s sense of control.

H8: A higher level of perceived experiential resonance will increase emergency rescuer’s sense of control.

(External) perceived power in this study is defined as rescuers’ sense of confidence to mobilize the motivation and cognitive resources, and course of action in dealing with external difficulties and challenges [101]. In contrast to sense of control over inner emotions, perceived power focuses more on rescuers’ outward reactions to external threats or tasks.

Informativeness or perceived understanding is a key element during the empowerment process, which can enhance people’s perceptions of their power and self-efficacy [15]. A number of studies have demonstrated that messages with high transparency are more persuasive and effective in building confidence, and are therefore expected to be more effective in increasing emergency rescuers’ perceived power after using the system [25, 102]. To elaborate, when emergency rescuers perceive that they have developed a clearer understanding through ERMS on questions such as why they are experiencing certain mood swings, and how to actively manage their mental wellbeing, they are more likely to feel more powerful towards upcoming work challenges. Besides, equipping emergency rescuers with actual psychological knowledge or self-help expertise is also expected to have positive impact on their perceived power. In healthcare settings, patients feel empowered through acquiring knowledge from experts, which allows them to be actively involved in self-care [12]. It is also found that high-quality advice, which enhances the extent of actual understanding, makes users of recommender systems feel more confident and comfortable [46].

H9: Improvement of perceived understanding will increase emergency rescuer’s perceived power.

H10: Improvement of actual understanding will increase emergency rescuer’s perceived power.

Emotional support from empathetic virtual advisors can be effective facilitators of learner interest and confidence. Prior studies have indicated that stronger social presence can help boosting people’s positive emotions, in particular self-assurance or confidence [103]. As pointed out by Cummins, social presence of an online learning community can empower student learning outcomes [104]. Specifically, positive social presence enhances social persuasion and leads to positive affect and increased level of learner confidence [105]. Hence, we expect that a stronger sense of social presence, which means feelings of human warmth and support, can strengthen emergency rescuers’ perceived capability to overcome dilemma and to handle challenging situations in future rescue tasks. Further, studies surrounding people’s perceived power indicate that individuals can obtain a higher level of confidence from similar others with experiential resonance [106]. For example, researchers would gain more confidence when they meet regularly with other researchers in social work to share their experiences and insights [107]; Survivors who were traumatized by the experience of natural disasters such as bush fire benefited greatly from the experience sharing and encouragement of group members, in terms of letting out emotions and building confidence[108]. Similarly, virtual advisors that can trigger a user’s experiential resonance, are considered as ‘in-group by emergency rescuers and thus easier to probe their true feelings. Encouragements and advices from ‘in-group’ advisors, who are considered to share common emergency rescue experiences, have stronger effects in boosting the rescuer’s perceived power in dealing with challenging situations. Consequently, it is expected that both social presence and perceived experiential resonance are expected to positively influence users’ perceived power.

H11: A better sense of social presence will increase emergency rescuer’s perceived power after using the system.

H12: A higher level of perceived experiential resonance will increase emergency rescuer’s perceived power after using the system.

Individual difference plays an important role in people’s perceptions and behaviors when using information systems [109-111]. Goldberg classifies personality into five aspects, including: agreeableness, conscientiousness, openness, extraversion and neuroticism [112]. Agreeableness (AG) is most concerned with orientations of experiential resonance [113]. Moreover, this dimension tests persons’ traits of trusting, generous, sympathetic, cooperative, aggressive, and cold [114]. In other words, AG to a large extent assesses whether people are welcoming or hostile, which is very likely to impact on their reactions towards advices given by virtual expert advisors (VEA) or virtual peer advisors (VPA). Therefore, we consider individual character, in particular, agreeableness as a moderating variable that potentially affect the dependent variables in our research model.

Based on the above discussions, we propose our research model for the virtual ERMS (see Figure 2).

![](/api/attachments/YS9CYY9S/fulltext/images/4def6ea01e3204bec7cb6316596c1fd734dab421120582af5a85effcd169fbf6.jpg)  
Figure 2 Research Model

## 4. EXPERIMENTS

## 4.1 Participants

The subjects were 120 emergency rescuers serving in a remote country border area that the research team traveled long distance to arrive at [location suppressed due to anonymity], including police officers and soldiers. The experiment was conducted in meeting rooms. Of the 120 subjects, 83.6% had performed a rescue mission and all of them were male. The average age was about 20 years, 99.2% were not married. 60.5% of the participants education levels are senior high school, 34.2% are secondary school and the remaining 5.3% graduated from colleges. 22.8% of the subjects had installed healthcare applications on their mobile phones, and 29.8% of the subjects reported experiencing mental health dilemmas to consult. We sampled our respondents from this distant area because this region had just experienced serious floods in August 2013 and these officers and soldiers had just returned from their emergency tasks when we arrived on the site.

![](/api/attachments/YS9CYY9S/fulltext/images/c25f26313f71d5ac7948c7f619f60b61aa97f2d9f597bb6eb81b28b94b2dcbd8.jpg)  
Figure 3 Exemplar screenshots of VEA(left) vs. VPA(right)

## 4.2 Experiment system descriptions

The ERMS system was designed with two versions of virtual advisor identities tested in our research model, that is, virtual peer advisor (VPA) and virtual expert advisor (VEA) (Figure 3). Based on 1) analyses of the extant literature in the IS discipline, including existing systems in practice and research laboratories 2) semi-structured and in-depth interviews with emergency rescuers, we designed and developed the mobile ERMS, a tool that addresses the psychological needs of emergency rescuers whenever and wherever they wish to access to such support. More technical details of the ERMS system and other exemplar screen shots were shown in Appendix Table A-3.

ERMS was deemed to be an ideal experimental tool, since we can realize easy manipulation and control for different design aspects according to our experimental design. To realize two practical identities (i.e., VEA vs. VPA) in the current application context, we treat the virtual advisor’s identity as a unity encompassing qualification symbols of their appearance along with the respective customized language such as appellations and greetings they use in their conversation addressing their identity. This is based on findings from literature that identity can be established by appearance and addressing of identity in the language [115, 116]. It is also important for the addressing of identity in the language to conform to the actual identity to avoid ambivalence and psychological discomfort, so as to

##

address each interlocutor in a meaningful, natural and believable way [115-117]. Except for the above manipulations surrounding the identity changes, all advisory contents were held consistent to ensure rigor of the experiment design. Besides, we have fully considered the different gender options for the virtual advisors. Consulting literature, Qiu and Benbasat [90] has taken a strategy of matching the ethnics and gender of the VA to make the advisory process more compatible and comfortable for the users. In another study on advisor gender choices, it is revealed that for the tutoring context, male tutors are considered more competent in many aspects than female tutors [118]. However, for the psychological counselling context, female virtual advisors are preferred by both male and female patients given that female counsellors are generally perceived as more empathetic, attentive, caring and soft [119, 120]. Therefore, in our experiment, we have set the genders of virtual advisors for both groups to be female, with a sole focus on comparing virtual advisor identities. This is also confirmed during our pilot testing with emergency rescuers, most of whom expressed their preferences for female advisors. This ERMS prototype will also be continuously refined and used in future field studies, to ensure that our project has high relevance for practice and will eventually benefit emergency rescuers in the real life. More technical details are not explained further here due to our focus on HCI issues in this study.

## 4.3 Measurement scales

The questionnaire used to collect participant feedback consisted of seven parameters: Perceived Understanding (PU), Actual Understanding (AU), Social Presence (SP), Experiential Resonance (ER), Sense of Control (SC), Perceived Power (PP) and Agreeableness (AG). The measures for the subjective constructs utilized in the questionnaires were all derived from existing scales that exhibited good psychometric properties. Table A-1 in Appendix outlines all the scales in the questionnaire along with their sources. All psychometric questions used a seven-point Likert scale. For actual understanding (AU),

#

evaluating the users’ actual understanding of knowledge through quizzes or tests is a common strategy used among many educators and researchers [121], therefore questions were tested on the mental health knowledge provided by the virtual health advisor during system user interactions, with the full mark scaled down to the same base to facilitate further statistical analysis. Typical multiple choice questions in the quizzes include “which of the following statements are the effective methods in reducing stress as suggested by the virtual advisor”; “Based on your understanding of the virtual advisor’s advice, which of the following falls under the umbrella of ‘positive attribution’”; and “according to the virtual advisor, which of the following statements belong to the category of the ‘locus of control’” and others.

## 4.4 Pilot

Before conducting the experiment, we performed a pre-test with ten subjects to check the experiment material including questionnaires and videos, and fine-tune the experiment procedures. The subjects were also asked to provide feedback on system performance. Most were able to complete the whole process within 40 minutes. Feedback from the subjects in the pre-test indicated the experiment design and the experiment material were appropriate. They also confirmed their preferences for a female counselor. In addition, these subjects considered the system performance to be well-accepted except that the loading time took a bit long on a few occasions. However, most commented that this did not interrupt their tasks.

## 4.5 Experiment procedures

The experiment consisted of three phases: (1) watching a five-minute video that described the virtual ERMS; (2) demonstrating to rescuers how to use the virtual advisory system through exemplar use cases; and (3) completing a questionnaire. This approach ensures maximum control over user experiences with ERMS. In particular, video and real-time demonstration was used due to primarily three reasons. First, within the iterative prototyping

##

process, this approach is considered more practical in case user misuse of this novel information system distort the intended experiment control. Second, with limited ICT resources near the country boarder location, limited opportunities and given-time to capture emergency rescuers’ responses immediately after the natural disaster result in precious data collected yet with some compromise; it is also not yet feasible at the current stage for us to install our prototyping software on each users’ mobile with many different versions of operating systems – this procedure may introduce chaos and intervening factors to the experiment design that greatly exceed the permitted time and hinder experiment control during the process. Finally, our sole focus on the design choice of virtual advisor identity also means video and live demonstration is sufficient for imposing this experimental condition on the participants, while achieving maximum control over what participants are exposed to on the user interface of the prototype. In the industry, conceptual video is a popular strategy adopted by many high-tech companies to introduce innovative product prototypes to potential customers to gather feedback while protecting the product from being overly-explored, in situations such as patent application. For example, Google has used conceptual video to showcase Project Glass, and Drew Houston has also released his Dropbox video for similar purposes.

A two-group between-subject design yielded two conditions in the experiment (1) the virtual expert advisor (VEA) group and (2) the virtual peer advisor (VPA) group (Figure 4). All subjects were randomly assigned to one of the two groups. Due to the differences in their arrival times, emergency rescuers returned from their rescue tasks in teams and were guided into different conference rooms. This resulted in two groups, one with 64 persons and the other with 56 persons. The two groups were randomly assigned to two different conference rooms, where ERMS was available with different virtual advisors. We then gave the subjects a brief introduction to the research. Next, we played a video that described the system comprehensively to set the background context for the following demonstration. For one

##

group (n=64), we played a video in which the advisor was an emergency rescue worker (i.e., a virtual peer advisor); for the other group (n=56), the advisor was a professional psychologist (i.e., a virtual expert advisor). Then we demonstrated live interactions with the corresponding version of the systems. The procedures were held consistent with the only difference being the identity of virtual advisor in each group. During the live demonstration, the experimenter projected the use of the software onto the wall screen, with the presence of another observer and helper in the same room. The live demonstration not only allowed us to observe and gather richer user implicit reactions, but also ensured a better match and control of the pace of user information digestion during the demo, such as user facial expressions of interest or confusion and body languages of nodding or shaking heads. To ensure roughly consistent timing and procedure for the two groups, we trained our experimenters before the formal experiment and during the pilot testing phase. The experimenters had also done several rounds of rehearsal in front of each other with timers to ensure consistency across the two groups. Afterwards, we issued paper-based survey questionnaires and asked users to answer the questions based on their own feelings. The whole experiment process lasted for about 40 minutes. Finally every participant received a thank-you gift for their time.

![](/api/attachments/YS9CYY9S/fulltext/images/2a58d25992d50bf8570448ff541623536cddab1e6fab2c7b7ea94e4fc45bed75.jpg)  
Figure 4 Experiment procedures

The subjects’ perceptions of the virtual advisor’s identity were used to verify that the advisors’ identity was effective. As a manipulation check, subjects were asked to answer a question: was the virtual advisor you consulted with a rescuer worker or a psychological expert? Out of the 114 effective questionnaires, approximately 81.5% of the subjects answered the virtual advisor’s identity correctly, with 81.3% in the VPA group and 81.8% in the VEA group respectively. Following the methods in [122], a chi-square analysis of the result yielded significant results $( \mathrm { X } \ ^ { 2 } ^ { = } 4 5 . 4 6 ^ { , } \mathrm { p } < 0 . 0 1 )$ ), showing that the two conditions are designed in a distinguishable way as perceived by most participants. Hence, we are confident that our manipulation of the experiment condition as VEA and VPA was successful.

## 4.6 Control variables

To investigate other potential effects, we performed analysis of variance (ANOVA) and T-tests to examine whether demographics data had effects on these dependent variables. The results showed that user demographics such as age, marital status, educational level, rescue experience and mobile application experiences had no significant effect on the dependent variables. Further, it is believed that user characters are likely to impact on the way they react to other people’s advice – in this context, the advice from virtual expert advisors or virtual peer advisors. Thus, to alleviate the impact of user’s characters on the research model, as suggested by [123], we analyzed it with partial least squares (PLS) method and the outcome indicated that only the agreeableness (AG) construct had significant influence on the dependent variables, while conscientiousness, openness, extraversion and neuroticism were found to have no effect on dependent variables. Consequently, ‘agreeableness’ aspect of the character, which to a large extent describes whether a user is more welcoming or hostile, was used as a moderating variable in further investigations.

## 5. EXPERIMENTS RESULTS

Six questionnaires were removed from 120 cases due to initial data screening and checking for incompleteness. Hence, a sample of 114 subjects was used in the following analysis. After preliminary data screening, we analyzed our research model using the Partial Least Squares (PLS) method. PLS was used because 1）it is suited to testing predictive research models where the emphasis is on early theory development that characterizes this study [124]; 2) PLS can easily cope with statistical identification and potential convergence problems with formative constructs in a complex model [125, 126]; 3) PLS has limited requirements on significant sample size and data distribution properties [126]; and finally based on the suggestion by Dijkstra and Henseler[127], if the composite model holds, PLS should be the method of choice (p.311), which is the case in our study. The model was mainly evaluated from two aspects: 1) the measurement model and 2) the structural model, as elaborated below.

First, the measurement model was examined for internal consistency, convergent validity and discriminant validity [128]. Cronbach's α was used to reflect the internal consistency of the constructs. In Table 5, Cronbach's α for every construct exceeded 0.7, which demonstrated high internal consistency of the corresponding constructs. Then, we look at average variance extracted (AVE) to assess the convergent validity of these constructs. The AVE value of all these constructs exceeded the commonly accepted threshold of 0.5, meaning that at least 50 percent of the construct variance was due to its indicators[129]. A rule for assessing discriminant validity requires that √AVE should be larger than the correlations between constructs. In other words, the bold numbers should be larger than off-diagonal correlations [128]. Thus all constructs in our research model met this requirement.

Table 5 R-square, composite reliability, cronbach's α, AVE and inter-construct correlations

<table><tr><td rowspan="2">Construct</td><td rowspan="2"> $R^2$ </td><td rowspan="2">CR</td><td rowspan="2">Cronbach's alpha</td><td rowspan="2">AVE</td><td colspan="6">Inter-construct correlations</td></tr><tr><td>AU</td><td>PP</td><td>PU</td><td>ER</td><td>SC</td><td>SP</td></tr><tr><td>AU</td><td>0.104</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PP</td><td>0.504</td><td>0.918</td><td>0.897</td><td>0.585</td><td>0.097</td><td>0.765</td><td></td><td></td><td></td><td></td></tr><tr><td>PU</td><td>0.212</td><td>0.926</td><td>0.906</td><td>0.640</td><td>0.271</td><td>0.543</td><td>0.800</td><td></td><td></td><td></td></tr><tr><td>ER</td><td>0.232</td><td>0.961</td><td>0.919</td><td>0.925</td><td>-0.282</td><td>0.395</td><td>0.083</td><td>0.962</td><td></td><td></td></tr><tr><td>SC</td><td>0.579</td><td>0.907</td><td>0.865</td><td>0.710</td><td>0.042</td><td>0.595</td><td>0.380</td><td>0.570</td><td>0.843</td><td></td></tr><tr><td>SP</td><td>0.182</td><td>0.901</td><td>0.862</td><td>0.647</td><td>-0.128</td><td>0.588</td><td>0.304</td><td>0.634</td><td>0.706</td><td>0.804</td></tr></table>

Second, the structural model was analyzed using the bootstrapping technique in PLS. 700 samples was used for bootstrapping iterations following the suggestions in [129]. Controlling for agreeableness, VAI had negative effects on both PU (β = -0.308, $\mathsf { p } < 0 . 0 5 )$ and AU (β = -0.272, $\mathsf { p } < 0 . 0 5 )$ . Besides, VAI positively impacts on SP (β = 0.196, $\mathsf { p } < 0 . 0 5 )$ and ER (β = 0.429, $\mathsf { p } < 0 . 0 5 )$ . On top of this, SP $( \beta = 0 . 1 7 9 $ $\mathsf { p } < 0 . 0 5 )$ , PU (β = 0.498, $\mathsf { p } < 0 . 0 5 )$ and ER (β = 0.283, $\mathfrak { p } < 0 . 0 5 )$ all positively affect participants’ (inner) sense of control. While PU (β = 0.399, $\mathsf { p } < 0 . 0 5 )$ , SP (β = 0.392, $\mathsf { p } < 0 . 0 5 )$ and ER (β = 0.157, $\mathsf { p } < 0 . 0 5 )$ significantly impact on (external) perceived power. However, AU had no significant effect on (inner) sense of control and (external) perceived power $( \beta = 0 . 0 8 5 $ $\mathsf { p } > 0 . 0 5$ ; $\beta = 0 . 0 8 0 $ $\mathsf { p } > 0 . 0 5$ , respectively) (see Table 6). In summary, the above results indicate that Hypotheses 1, 2, 3, 4, 5, 7, 8, 9, 11 and 12 were supported. Hypotheses 6 and 10 were not supported by the data.

Table 6. Path coefficients, t-statistics and p-value

<table><tr><td>Paths</td><td>Path coef.</td><td>t</td><td>Interpretation (S: Supported; NS: Not supported)</td></tr><tr><td>H1 VAI→PU</td><td>-0.308</td><td>3.848</td><td>S: In contrast to virtual peer advisors (VPA), emergency rescuers' perceived understanding of the psychological knowledge provided by the mental health advisory system is better with virtual expert advisors (VEA). (p&lt;0.01).</td></tr><tr><td>H2 VAI→AU</td><td>-0.272</td><td>3.169</td><td>S: In contrast to VPA, emergency rescuers' actual understanding of the psychological knowledge provided by the mental health advisory system is better with VEA.(p&lt;0.01).</td></tr><tr><td>H3VAI→SP</td><td>0.196</td><td>2.311</td><td>S: In contrast to VEA, VPA will result in a higher sense of social presence while using the system. (p&lt;0.05).</td></tr><tr><td>H4VAI→ER</td><td>0.429</td><td>5.650</td><td>S: In contrast to VEA, emergency rescuers perceive VPA as more capable in triggering their experiential resonance while using the system.(p&lt;0.01).</td></tr><tr><td>H5PU→SC</td><td>0.179</td><td>2.190</td><td>S: Perceived understanding had a significant positive effect on sense of control. (p&lt;0.05).</td></tr><tr><td>H6AU→SC</td><td>0.085</td><td>1.940</td><td>NS: Actual understanding had no significant positive effect on sense of control. (p&gt;0.05).</td></tr><tr><td>H7SP→SC</td><td>0.498</td><td>4.914</td><td>S: Social presence had a positive impact on rescuers' sense of control. (p&lt;0.01).</td></tr><tr><td>H8ER→SC</td><td>0.283</td><td>2.777</td><td>S: Experiential resonance significantly impacts rescuer's sense of control .(p&lt;0.01).</td></tr><tr><td>H9PU→PP</td><td>0.399</td><td>4.985</td><td>S: Perceived understanding had a significant positive effect on perceived power. (p&lt;0.01).</td></tr><tr><td>H10AU→PP</td><td>0.080</td><td>0.908</td><td>NS: Actual understanding had no significant impact on perceived power. (p&gt;0.05).</td></tr><tr><td>H11SP→PP</td><td>0.392</td><td>4.611</td><td>S: Social presence was shown to have a significant positive effect on perceived power. (p&lt;0.01).</td></tr><tr><td>H12ER→PP</td><td>0.157</td><td>1.969</td><td>S: Experiential resonance had a significant impact on perceived power. (p&lt;0.05).</td></tr></table>

As for the overall fitness of our model, we can see that most R-square values in Table 5 exhibits moderate to substantial strength in explaining the dependent variables [129]. Among these, actual understanding has got a relatively weak R-square value of ten percent. This happens because actual understanding is a single-value construct without indicator variables (as elaborated in the measurement scales section) [129]. We initially incorporated a series of user demographics and all five factors of personality [112], namely agreeableness, conscientiousness, openness, extraversion and neuroticism in our research model as potential control variables. In these factors, only ‘agreeableness’ was shown to significantly impact on the dependent variables in this study. As a result the model was reanalyzed excluding those insignificant control relationships, with agreeableness (AG) serving as the moderating variable. Altogether, the structural model results of the PLS analysis are shown in Figure 5.

![](/api/attachments/YS9CYY9S/fulltext/images/f38f53b2cf3917ff7b3f6e891252d66554a401a1fcd2c60e16e5ad1b0828a7a2.jpg)  
Figure 5. Structural model results

## 6. AN EXPERIENCE SAMPLING STUDY

Based on a series of research efforts including preliminary interviews, scrutinizing existing systems and field experiments with emergency rescuers right after natural disaster strikes, we identified virtual advisor identity as an important yet largely ignored design consideration and empirically assessed its impact on the empowerment effect of ERMS. To gain further insights on how users would react to the VEA and VPA versions of ERMS after interacting with it for a longer period of time in real-life settings, a third study was designed using the Experience Sampling Method (ESM)[130], an effective tool for tracking user

#

experiences systematically and capturing variations in users’ mental processes in natural environments. This further study centers around the core question of whether different virtual advisor identities make any difference for ERMS users who experienced it for longer. Although in this ESM study we do not have the external major disaster stimuli as in the first field experiment, with the help of biofeedback device of ERMS, we are able to objectively track the overall emotional empowerment effect of ERMS on users via heart rate variability (HRV) [131] in more natural settings and for longer period of time, which allows us to triangulate the previous results and obtain a more comprehensive story of the research issue of concern. That is, these physiological data serve as complements to the analysis of user experience booklet, knowledge quizzes and end-of-period interviews in this ESM study.

To triangulate user emotional empowerment, we analyzed user feedback in the user experience booklet and end-of-period interviews (i.e., comparing the concepts and key themes to those in Figure 5). As an additional measure to gain further insights, we objectively tracked the improvements in user emotional states through HRV-based physiological data [131, 132]. To elaborate, HRV indices capture a user’s psychophysiological coherence, representing sustained positive emotions as well as good mental and emotional stability [133]. Prior studies also used HRV indices to reflect a person’s inner emotional stability, and emotional self-regulatory strength or effort when confronting with challenging situations [131]. In virtual environments, a higher sense of social presence or experiential resonance are frequently coupled with users’ psychophysiological coherence or sustained positive emotional experiences [25, 134] that potentially enhance their inner sense of control and perceived power in dealing with challenges [15]. Therefore, we interpret physiological data as the indirect evidence of the emotional empowerment effect of ERMS for emergency rescuers. For user cognitive empowerment, we assessed this through analyzing self-reported learning experiences on the user experience booklet and psychological knowledge quiz on what the virtual advisor has suggested to emergency rescuers.

##

Moreover, due to difficulty in obtaining long-term usage data with emergency rescuers and the resultant limited sample size, we do not intend to statistically infer complex relationships between all variables in our research model in Figure 2. This has already been done in study 2. Instead, we combine self-reported qualitative data and bio feedback data on system usage via experience sampling method, together with qualitative interviews conducted at the end of the field study period, to triangulate our research findings in the previous stage. A total of 21 emergency rescuers recruited from 4 fire brigades in a large city in China agreed to participate in our study and installed our ERMS software on their mobile phones. Of the 21 subjects, all have experiences of participating in rescue tasks and all of them were male. The average age was about 20 years, with 33% reporting that they have installed various health-related apps on their mobile phones before. To avoid interruptions to their important daytime tasks, we only asked them to complete their self-assessment tasks after work. Given the limited number and the high price of biofeedback devices, 21 emergency rescuers who have compatible Android phones for ERMS, are able to participate in this study.

In a meeting room, participants separately finished informed consent, questionnaire of demographics. They were randomly assigned to experience one of the two versions of ERMS, with 11 people using the VEA version and 10 people using the VPA version. They then received a live demonstration of what they need to do during the two week period of using ERMS. During this process, participants need to measure and record their emotional status before and after using ERMS, towards the end of each day, as well as commenting on their feelings before, during and after using ERMS on a booklet. The bio data was tracked via our hardware devices that measures heart rate variability (HRV), a standard way of reflecting the actual emotional status of a person [131, 132]. We focused on comparing emergency rescuers’ positive emotions score (PES) derived from HRV indices following the methods discussed in [131, 132] for each group, since maintaining a higher level of positive emotions is regarded as the ultimate goal of achieving psychophysiological coherence by prior researchers [133].

#

Towards the end of the field study period, participants were asked to openly comment on their overall experience of using ERMS and complete a psychological knowledge quiz, which consists of multiple choice questions including “which of the following statements are the effective methods in reducing stress as suggested by the virtual advisor”; “Based on your understanding of the virtual advisor’s advice, which of the following falls under the umbrella of ‘positive attribution’”; and “according to the virtual advisor, which of the following statements belong to the category of the ‘locus of control’” and others. The full mark was then scaled to be out of 7 to make it easier for further statistical analysis. Participants were also requested to hand in their user experience booklet, and return the ERMS hardware devices to our research assistants.

During data analysis, one case was discarded due to the participant dropping out halfway on short leave. This left us with two equal-size group of 10 people in each condition. An independent samples T-test was conducted on the two groups to compare the impact of VEA with VPA. The data set meets the basic requirements of T-test including normality and equal population variances (Levene’s test result F=3.74, P >0.05). The result of the study reveal that VPA acts better in improving emotional coherence, as reflected via significantly larger extent of improvement in HRV-based positive emotional score (PES) than VEA (c.f., [131, 132] for deriving PES from HRV indices). To elaborate, comparing the average or mean of PES differences of all individuals for each day in each group, the result of independent T-test shows significant differences between the VPA and VEA group (mean difference (VPA versus VEA) =4.14, T=5.80, p<0.05); comparing the average PES improvement for each person over 14 days, the result of T-test also shows significant differences between VPA and VEA group (mean difference (VPA versus VEA) =3.96, T=3.13, p<0.05). From Figure 6, we can see that in general VPA group performs better in enhancing user positive emotions over the two week observation period. While for the final test of psychological knowledge recall at the end of the two-week period, the VEA group performs significantly better than the VPA group in transferring knowledge (mean difference (VEA versus VPA) =1.15, T= 2.31, p<0.05).

![](/api/attachments/YS9CYY9S/fulltext/images/9e458d7c16e711e07cf3913317a308f17c99a773b868106b8c6de4c6e73b1f1d.jpg)  
Figure 6. Comparing the positive emotion improvement effect of VPA vs. VEA over 2 weeks

Note: The vertical axis shows the mean increase in HRV-based indices as explained in further detail in [131, 132] reflecting the average level of people’s positive emotions for each group on a daily basis

Through analyzing the qualitative interviews using content analysis method, we also identified similar concepts and themes that aligns very well with our research model and previous field experiment results. For example, participants in the VPA group reported that they feel like ‘having the closeness, warmth and intimacy…and their past experiences interests and enlightens me’; ‘talking to a co-worker advisor who seems to share common experiences helps me to relax and cool down‘ and ‘the emotional support from fellow rescuers would make me feel calm and confident’. These findings are congruent with the previous result that virtual peer advisors empower emergency rescuers mostly through emotional channels, including a better sense of social presence and experiential resonance. While participants in the VEA group put more emphasis on what kind of knowledge they obtained and showed more reflections on how they would count on the knowledge to solve their own problems. Typical comments include ‘[the advisor’s] professional advice equipped me with psychological knowledge that allows me to better interpret my current dilemma’; ‘I now feel more powerful towards challenging situations since I got the right knowledge from psychiatrist to tackle them’; ‘with these useful tips from the expert, I expect myself to have good control over my always-fluctuating emotions.’ This supports our findings that virtual expert advisors fair better in empowering rescuers through cognitive channels. Below we only highlight those extra findings apart from the results of the previous field experiment. Based on users’ daily experience data and end-of-period comments, we identified the following key insights:

First, over time, emergency rescuers felt that the longer they use the system, the more they care about the identity of the virtual advisor. For example, virtual advisor identity that seems boring, uninteresting or unrealistic can only be distracting or distancing for the user and cause them to drop out of the service. Second, emergency rescuers noted that improved sense of control and perceived power means different things for them, sometimes they felt internally calm, but when facing with external challenges, they still felt threatened. Therefore, emphasizing both sense of control and perceived power as key empowerment outcomes are essential for ERMS design. Third, a number of them suggested that virtual advisor characters with more comprehensive and concrete identities should be included in the next version of ERMS, possibly with ‘introductions of detailed past experiences of the virtual advisor’ to give users more human sense and thus, to reduce the feelings of interacting with a ‘cold-hearted machine’. Finally, emergency rescuers expect the contents of ERMS to be richer and more dynamic in the long run, having high expectations for the successful implementation of this initiative that has a ‘good potential to generate positive impacts in their life’.

## 7. CONCLUSION AND DISCUSSIONS

## 7.1 Interpretation of the results

In this study, we have empirically shown that the advisor’s identity significantly influences emergency rescuers’ cognitive and emotional aspects after using the system.

#

Further, congruent with theory predictions, emergency rescuers consider virtual expert advisors to be better in transferring knowledge relative to virtual peer advisors. That is, virtual expert advisors have stronger empowerment effect in imparting knowledge (i.e., as assessed via user’s perceived and actual understanding) to emergency rescuers than virtual peer advisors. On the other hand, the positive substantial effects on users’ emotional aspects, as evaluated in terms of social presence and experiential resonance, imply that virtual peer advisors can empower emergency rescuers through a stronger sense of social presence and a better feeling of inner resonance. Overall, bootstrapping results show that cognition and emotion, as important empowering enablers, have substantial influence on empowerment outcomes measured by a sense of control and perceived power. Comparing path coefficients and T-values, we can also see that in general emotional aspects play a more important role on empowerment outcomes relative to users’ cognitive aspects. This provides meaningful lessons for a psychological self-help system, in that emotional support is more critical than merely educating users with psychological knowledge.

In contrast to perceived understanding, actual understanding does not contribute significantly to variations in empowerment outcomes. This might have happened as a result of the participants being unaware of their task score immediately after the tests. For example, a study conducted by Metcalfe and Greene reported that people might report a low level of control even when their performance in a certain task was high [135]. Another possible reason might be due to the fact that information needs time and experience to be processed into knowledge by human brain to empower people [15]. This result also aligns well with Jiang and Benbasat’s [48] empirical findings that it is ‘perceived website diagnosticity’, not ‘actual product knowledge’, that affects users’ attitude towards the website. To elaborate, these results uncover an interesting phenomena that user’s perceived mental transparency related to a certain virtual product or service, is the key factor that matters for the empowerment outcomes of an information system, overriding how much actual knowledge was actually obtained by a user. From another angle, enhancing the transparency of an ERMS, for example through reducing a user’s cognitive load in the system design via methods such as hierarchical decomposition or reasoning [136], is an effective way to boost the value of such a system.

## 7.2 Contributions to research

In terms of theory and methodology, this study has the following contributions.

First, the identity of the virtual advisor is an important design consideration to boost the power of virtual health advisory services. Our study has thus empirically investigated this important and novel aspect - the implications of different design choices of VAI for emergency rescuer empowerment. In this research, we extend existing HCI theories on mobile psychological self-help services through our empirical study. In contrast to the increasing popularity of mobile psychological self-help systems on smart end-user devices, little prior work has been done systematically to investigate the impact of different HCI design strategies on the effectiveness of mobile psychological self-help services. Consequently, this study serves as a good reference for further explorations in this area.

Second, this study has implications for deepening our understanding with the ‘symbols of authority’ theory and similarity theory in the IS discipline. Nass and Moon [137] commented that people construct social relationships, and apply social cues in their relationships with technology. We explored how ‘symbols of authority’ and similarity traits influence users in different ways. When appropriately designed, virtual advisory systems as social actors can exert positive influences on the advisory service recipient, cognitively and emotionally. While resonance-invoking virtual peer advisors, who exhibit identity similarity between the advisory service provider and the recipient, can potentially strengthen the emotional aspects of such positive influence, authoritative virtual expert advisors are better at convincing the users with factual knowledge and sustaining their memory retention. In turn, cognitive and emotional influences can be significant empowering enablers, generating a stronger sense of control and perceived power for advisory system users. As Zimmerman (2000) suggests that through the empowerment process, appropriately designed virtual advisory services can create opportunities for community members to develop skills (emotionally or physically) to master their own fate in a way that are free from merely counting on professionals.

These results also shed light on the underlying reasons of why ‘symbols of authority’ and similarity theory strengthens the empowerment effect of virtual health advisory systems. In the classical theories of human communications, Berger (1991) pointed out that uncertainty reduction is one of the primary dimensions of developing a relationship and attraction or affiliation can help alleviate uncertainty and vigilantness - ‘when communicators discover similarities between them, their attraction to one another goes up, and their apparent need for more information goes down’ [138], thus facilitating the empowerment processes for ERMS. Virtual peer advisors, who exhibit similar features and experiences with the emergency rescuers, can enhance the empowerment outcomes of ERMS - achieved largely through emotional channels such as the heightened sense of experiential resonance and feelings of social presence. This is in contrast to virtual expert advisors, who empower emergency rescuers mostly through cognitive channels, just as prior study suggested this is because we frequently take the mental shortcut and are more likely to believe that people who display ‘symbols of authority’ should be accepted and followed [46].

Moreover, in terms of research methodologies used in the study, we have taken an innovative non-linear and iterative approach in our system artefact design and development. The unique sample of our study also adds significant practical value to our research. Such samples are challenging to approach in real life, especially given that the experiment was carried out when emergency rescuers completed their rescue tasks right after a natural disaster hit Inner Mongolia. As stated by Henver et al., ‘understanding the meaning of design characteristics as they impact the user is known to be elusive and complex from a methodological standpoint’ [139]. To ensure the relevance of our research focus, we collected requirements from emergency rescuers and features of existing systems as inputs, and then centered our study on ‘virtual advisor identity’ as the major design issue of concern. To ensure the rigor of our study in theory development, we consulted the grounding theories and past knowledge for our research project to develop our research model. In system design and development, we iterated through system design and the evaluation of design ‘artefacts’. Through the refinement of a concrete system artefact based on a mixture of research methods, our research methodology ensured both rigor and relevance in our study [140].

## 7.3 Implications for practice

From a practical point of view, the results of this study also provide numerous useful insights for system designers and policy makers.

First, our study results reveal that virtual expert advisors, who appear as authoritative figures, are suitable when the system design emphasis on knowledge acquisition. In other situations, where the system’s focus is on establishing rapport and a sense of support for depressed users, virtual peer advisors should be used, as they appear to exhibit more human warmth and experiential resonance. As an interesting implication to system designers of virtual advisory services, different virtual advisor identities can be used for different scenarios or sections of the system, with innovative design themes to cater for different purposes.

Further, to our knowledge, existing mobile mental-health advisory systems for emergency rescuers are sparse. We have empirically shown that appropriately designed ERMS, can be effective tools for empowering emergency rescuers in actively managing their mental health. Our study therefore hopes to draw more attention and resources from the government and the national health framework to support this self-devoting career.

More interestingly, this project combines mobile technologies with a medical device to monitor emergency rescuers’ physiological indices on the go. While part of this project is under patent application, more details of the system hardware and software design are

available upon request.

Finally, through the experience sampling study, it is revealed that virtual advisors with more comprehensive identities could potentially help with bridging the emotional gap between interacting with a virtual advisory system, and a real human advisor. Therefore, practitioners could consider incorporating detailed introductions of the virtual advisor character such as his/her prior work experiences, life stories or demographics information, to boost the value of virtual advisory services for users.

## 7.4 Limitations and future research

There are a few limitations to note while interpreting the research findings. First, this study focuses on the compelling need of emergency rescuers. Due to the nature of rescue work in emergency settings, the scope of the study is limited to frontline emergency rescuers (i.e., mostly male rescue soldiers) serving in the Chinese army. Future study could examine or extend the research model to other research settings. It would also be interesting to examine further, in different culture backgrounds, how users of both gender would rate their virtual advisors. Second, we have travelled to and sampled our respondents from Inner Mongolia because this region has just experienced natural disaster (in August 2013); these soldiers have just returned from their emergency rescue tasks when we arrived on the site. While we believe these soldiers are usually recruited from different provinces in China, it will also be helpful to investigate the feedback from more sites in different provinces after natural disaster happens. Third, considering less than 60% of total population own smart phones in developing countries [141] and there exist mobile devices with various operating systems such as IOS, Symbian and windows phone, we first played videos and then demonstrated the system functions in a comprehensive and systematic way, instead of installing ERMS on each participants’ mobile phones. While the former approach was chosen in the study to guarantee more control over the experiment design, the latter approach could be undertaken when richer

#

user experiences are needed in field settings in future studies. Further, although the study revealed that it is user’s perceived mental transparency of the obtained psychological knowledge that matters most for user empowerment outcomes right after system usage, we expect actual understanding gradually taking over this important role in user empowerment in the long term. More future research is warranted in examining this confounding ‘taking-over process along the time dimension. In addition, to realize two practical virtual advisor identities in the scope of our current application scenarios, we consider that the language of virtual advisors such as appellations and greetings should be customized to match the respective identity as shown via appearance (e.g., uniforms) of the virtual advisor to ensure more natural and believable interactive experiences for the users, and thus treat these intertwining qualification symbols as an unified “identity social object” that makes an overall impact on the users [115-117]. Future study could consider dissecting and scrutinizing the identity social object more in-depth in different application scenarios and research contexts. While we tried our best to eliminate confounding factors in our research study, one should interpret our findings with these limitations in mind.

Finally, we discuss ideas that potentially inspire further research opportunities. First, future studies could examine the proposed research framework in different settings to investigate its applicability and generalizability. It is also worthwhile to incorporate more comprehensive personal backgrounds to virtual advisor identities in the system and inspect on its related usage outcomes. Second, context-aware features via Internet of Things (IoT) technologies could be integrated into the design of similar systems to enhance the usability and value of such systems for health consumers [142]. The HCI implications of customizing such services through detecting user locations, environments, emotions, body gestures and/or physiological data real-time on mobile devices could be further investigated. These emerging directions in the IS field are expected to tremendously enhance user experiences in various application settings and improve their overall satisfactions with the mobile virtual advisory

## REFERENCES

[1] H. Te Brake, M. Dückers, M. De Vries, D. Van Duin, M. Rooze, C. Spreeuwenberg, Early psychosocial interventions after disasters, terrorism, and other shocking events: Guideline development, Nursing & health sciences, 11 (2009) 336-343.

[2] EC, Redesigning health in europe for 2020, Ehealth task force report, Brussels, (2012).

[3] BTB, Beating the blues, [Online], Available: http://www.beatingtheblues.co.uk [Last accessed 2-20-2014], (2006).

[4] A. Rizzo, K. Sagae, E. Forbell, J. Kim, B. Lange, J. Buckwalter, J. Williams, T. Parsons, P. Kenny, D. Traum, SimCoach: an intelligent virtual human system for providing healthcare information and support, in: The Interservice/Industry Training, Simulation & Education Conference (I/ITSEC), NTSA, 2011.

[5] TMG, The MoodGYM, [Online], Available: https://moodgym.anu.edu.au/ [Last accessed 10-06-2014], (2012).

[6] iCouch, iCouch CBT, [Online], Available: http://itunes.apple.com/gb/app/icouch-cbt/id446115508?mt=8 [Last accessed 12-06-2014], (2012).

[7] OneHealth, One Health Mobile, [Online], Available: http://about.onehealth.com/onthego/ [Last accessed 06-03-2014], (2014).

[8] Kuchbi, Fast food- Top restaurant finder, [Online], Available: https://itunes.apple.com/us/app/fastfood-top-restaurant-finder/id299488453?mt=8 [Last accessed 10-03-2014], (2014).

[9] L.-F. Sugianto, S.P. Smith, C. Wilkin, A. Ceglowski, Pervasive Applications in the Aged Care Service, Pervasive Computing and Communications Design and Deployment: Technologies, Trends and Applications, IGI Global, (2011) 318-335.

[10] G.M. Reger, G.A. Gahm, Virtual reality exposure therapy for active duty soldiers, Journal of Clinical Psychology, 64 (2008) 940-946.

[11] H.G. Hoffman, T. Richards, B. Coda, A. Richards, S.R. Sharar, The illusion of presence in immersive virtua reality during an fMRI brain scan, CyberPsychology & Behavior, 6 (2003) 127-131.

[12] T.W. Bickmore, L.M. Pfeifer, B.W. Jack, Taking the time to care: empowering low health literacy hospital patients with virtual nurse agents, in: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2009, pp. 1265-1274.

[13] D. Thompson, T. Baranowski, R. Buday, J. Baranowski, V. Thompson, R. Jago, M.J. Griffith, Serious video games for health: how behavioral science guided the development of a serious video game, Simulation & gaming, 41 (2010) 587-606.

[14] S. Kethuneni, S.E. August, J.I. Vales, Personal Healthcare Assistant/Companion in Virtual World, 2009 AAAI Fall Symposium Series, (2009).

[15] M.A. Zimmerman, Empowerment theory, Springer US, 2000.

[16] I. Aujoulat, W. d’Hoore, A. Deccache, Patient empowerment in theory and practice: polysemy or cacophony?, Patient education and counseling, 66 (2007) 13-20.

[17] M. Koelen, B. Lindström, Making healthy choices easy choices: the role of empowerment, European Journal of Clinical Nutrition, 59 (2005) S10-S16.

[18] S. Dayal, P. Johnson, A web-based revolution in Australian public administration, Journal of Information, Law and Technology, 1 (2000)

[19] H.J. Lee, S.H. Lee, K.-S. Ha, H.C. Jang, W.-Y. Chung, J.Y. Kim, Y.-S. Chang, D.H. Yoo, Ubiquitous healthcare service using Zigbee and mobile phone for elderly patients, International Journal of Medical Informatics, 78 (2009) 193-198.

[20] G. Castellano, L. Kessous, G. Caridakis, Emotion recognition through multiple modalities: face, body gesture, speech, in: Affect and emotion in human-computer interaction, Springer, 2008, pp. 92-103.

[21] J. Cassell, Embodied conversational agents, MIT press, 2000.

[22] V. Gallese, The Two Sides of Mimesis: Girards Mimetic Theory, Embodied Simulation and Social Identification, Journal of Consciousness Studies, 16 (2009) 21-44.

[23] B. Yahmed, M.A. Bounenni, Z. Chelly, A. Jlassi, A new mobile health application for an ubiquitous information system, in: Wireless and Mobile Networking Conference (WMNC), 2013 6th Joint IFIP, IEEE, 2013, pp. 1-4.

[24] S. Gregor, The nature of theory in information systems, MIS quarterly, 30 (2006) 611-642.

[25] S.W. Littlejohn, K.A. Foss, Theories of human communication, Wadsworth Publishing Company, New York, 2010.

[26] S.J. Schueler, FreeMD, [Online], Available: http://www.freemd.com/ [Last accessed 2-20-2014], (2011).

[27] B. Frost, Changing States - Hypnotherapy High Wycombe & Central London, [Online], Available: http://www.changingstates.co.uk [Last accessed 02-04-2015], (1998).

[28] DLP, Depressed little prince, [Online], Available: http://www.depression.edu.hk [Last accessed 2-20-2014], (2013).

[29] D. Paton, J.M. Violanti, L.M. Smith, Promoting capabilities to manage posttraumatic stress: Perspectives on resilience, Charles C Thomas Publisher, 2003.

[30] P.J. Morrissette, The pain of helping: Psychological injury of helping professionals, Routledge, 2004.

[31] J. Erich, Earlier Than Too Late: Stopping Stress and Suicide Among Emergency Personnel, http://www.emsworld.com/article/12009260/suicide-stress-and-ptsd-among-emergency-personnel [Online], Available, [Last accessed 08-06-2016], (2014).

[32] D. Paton, D.M. Johnston, Disaster resilience: an integrated approach, Charles C Thomas Publisher, 2006.

[33] K.W. Thomas, B.A. Velthouse, Cognitive elements of empowerment: An “interpretive” model of intrinsic task motivation, Academy of management review, 15 (1990) 666-681.

[34] C. Argyris, Empowerment: The Emperor's New Clothes, Harvard Business Review, 76 (1998) 98-105.

[35] J. Smith, Empowering people: How to bring out the best in your workforce, Kogan Page Limited, 1996.

[36] D.D. Perkins, M.A. Zimmerman, Empowerment theory, research, and application, American journal of community psychology, 23 (1995) 569-579.

[37] M.A. Zimmerman, Psychological empowerment: Issues and illustrations, American journal of community psychology, 23 (1995) 581-599.

[38] C.H. Gibson, A concept analysis of empowerment, Journal of advanced nursing, 16 (1991) 354-361.

[39] H.K.S. Laschinger, J. Finegan, Using empowerment to build trust and respect in the workplace: A strategy for addressing the nursing shortage, Nursing economics, 23 (2005) 6-13.

[40] C.M. Rodwell, An analysis of the concept of empowerment, Journal of advanced nursing, 23 (1996) 305-313.

[41] D. Jenkins, Managing Empowerment: How to make Business Re-engineering Work, in, Century Limited, London, 1996.

[42] P.W. Speer, N.A. Peterson, Psychometric properties of an empowerment scale: Testing cognitive, emotional, and behavioral domains, Social Work Research, 24 (2000) 109-118.

[43] L. Pranic, W.S. Roehl, Rethinking service recovery: a customer empowerment (CE) perspective, Journal of Business Economics and Management, 13 (2012) 242-260.

[44] M. Margalit, M.H. Raskind, Mothers of children with LD and ADHD: Empowerment through online communication, Journal of Special Education Technology, 24 (2009) 39-49.

[45] D. Cyr, M. Head, H. Larios, B. Pan, Exploring human images in website design: a multi-method approach, MIS quarterly, 33 (2009) 539.

[46] F. Ricci, L. Rokach, B. Shapira, P.B. Kantor, Recommender systems handbook, Springer, 2011.

[47] P.S. Smith, Online vicarious-experience: using technology to help consumers evaluate physical products over the Internet, PhD Thesis, University of Melbourne, Melbourne, (2006).

[48] Z. Jiang, I. Benbasat, The effects of presentation formats and task complexity on online consumers' product understanding, MIS Quarterly, (2007) 475-500.

[49] J. Jahng, H. Jain, K. Ramamurthy, Effects of interaction richness on consumer attitudes and behavioral intentions in e-commerce: some experimental results, European Journal of Information Systems, 16 (2007) 254-269.

[50] M. Koufaris, Applying the technology acceptance model and flow theory to online consumer behavior, Information systems research, 13 (2002) 205-223.

[51] R. Agarwal, E. Karahanna, Time flies when you're having fun: cognitive absorption and beliefs about information technology usage, MIS Quarterly, 24 (2000) 665-694.

[52] G. Häubl, K.B. Murray, Double agents: assessing the role of electronic product recommendation systems, Sloan Management Review, 47 (2006) 8-12.

[53] K. Swearingen, R.R. Sinha, Interaction design for recommender systems, Designing Interactive Systems, 6 (2002) 312-334.

[54] R. Ouschan, J.C. Sweeney, L.W. Johnson, Dimensions of patient empowerment: implications for professional services marketing, Health Marketing Quarterly, 18 (2000) 99-114.

[55] I. Aujoulat, R. Marcolongo, L. Bonadiman, A. Deccache, Reconsidering patient empowerment in chronic illness: a critique of models of self-efficacy and bodily control, Social science & medicine, 66 (2008) 1228-1239.

[56] I. Benbasat, HCI research: future challenges and directions, AIS Transactions on Human-Computer Interaction, 2 (2010) 16-21.

[57] S. Al-Natour, I. Benbasat, The adoption and use of IT artifacts: a new interaction-centric model for the study of user-artifact relationships, Journal of the Association for Information Systems, 10 (2009) 661-685.

[58] A. Kamis, M. Koufaris, T. Stern, Using an attribute-based decision support system for user-customized products online: an experimental investigation, MIS Quarterly, 32 (2008) 159-177.

[59] K.S. Saladin, L. Miller, Anatomy & physiology, McGraw-Hill, 1998.

[60] C.-M. Chiu, M.-H. Hsu, E.T. Wang, Understanding knowledge sharing in virtual communities: An integration of social capital and social cognitive theories, Decision support systems, 42 (2006) 1872-1888.

[61] C.H. Braddock, K.A. Edwards, N.M. Hasenberg, T.L. Laidley, W. Levinson, Informed decision making in outpatient practice: time to get back to basics, Jama, 282 (1999) 2313-2320.

[62] Y.C. Xu, Z. Chen, Relevance judgment: What do information users consider beyond topicality?, Journal of the American Society for Information Science and Technology, 57 (2006) 961-973.

[63] B. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, Mis Quarterly, 31 (2007) 137-209.

[64] P. Bharati, A. Chaudhury, An empirical investigation of decision-making satisfaction in web-based decision support systems, Decision Support Systems, 37 (2004) 187-197.

[65] E. Hatzidimitriadou, Political ideology, helping mechanisms and empowerment of mental health self-help/mutual aid groups, Journal of Community & Applied Social Psychology, 12 (2002) 271-285.

[66] J. Choi, A motivational theory of charismatic leadership: Envisioning, empathy, and empowerment, Journal of Leadership & Organizational Studies, 13 (2006) 24-43.

[67] A. Barak, M. Boniel-Nissim, J. Suler, Fostering empowerment in online support groups, Computers in Human Behavior, 24 (2008) 1867-1883.

[68] D. Gefen, D.W. Straub, Managing user trust in B2C e-services, E-service Journal, 2 (2003) 7-24.

[69] T.G. Gill, The single client resonance model: beyond rigor and relevance, Informing Science, 11 (2008) 281-310.

[70] D.W. McMillan, D.M. Chavis, Sense of Community: A Definition and Theory, Journal of Community Psychology 14 (1986) 6-23.

[71] F.D. Vennik, S.A. Adams, M.J. Faber, K. Putters, Expert and experiential knowledge in the same place: patients’ experiences with online communities connecting patients and health professionals, Patient Education and Counseling, In press, forthcoming, 95 (2014) 265-270.

[72] M.A. Hewgill, G.R. Miller, Source credibility and response to fear‐arousing communications, 32 (1965) 95-101.

[73] L. Bickman, The social power of a uniform, Journal of Applied Social Psychology, 4 (1974) 47-61.

[74] C.K. Hofling, E. Brotzman, S. Dalrymple, N. Graves, C.M. Pierce, An experimental study in nurse-physician relationships, The Journal of nervous and mental disease, 143 (1966) 171-180.

[75] D.E. Byrne, The attraction paradigm, Academic Pressing, San Diego, 1971.

[76] H.C.V. Vugt, J.N. Bailenson, J.F. Hoorn, E.A. Konijn, Effects of facial similarity on user responses to embodied agents, ACM Transactions on Computer-Human Interaction (TOCHI), 17 (2010) 7.

[77] M. Li, J. Mao, Hedonic or utilitarian? Exploring the impact of communication style alignment on user's perception of virtual health advisory services, International Journal of Information Management, 35 (2015) 229-243.

[78] C.F. Uden-Kraan, Online peer support for patients with somatic diseases, University of Twente, 2008.

[79] M. Rosemann, I. Vessey, Toward improving the relevance of information systems research to practice: the role of applicability checks, MIS Quarterly, (2008) 1-22.

[80] B.G. Glaser, A.L. Strauss, The discovery of grounded theory: Strategies for qualitative research, Transaction Books, 2009.

[81] J. Corbin, A. Strauss, Basics of qualitative research: Techniques and procedures for developing grounded theory, Thousand Oaks, (2008).

[82] J. Corbin, A. Strauss, Basics of qualitative research: Techniques and procedures for developing grounded theory, Sage publications, 2014.

[83] J.R. Landis, G.G. Koch, The measurement of observer agreement for categorical data, biometrics, (1977) 159-174.

[84] S. Marine, P.J. Embi, M. McCuistion, D. Haag, J.R. Guard, NetWellness 1995–2005: ten years of experience and growth as a nonprofit consumer health information and ask-an-expert service, in: AMIA Annual Symposium Proceedings, Washington, DC, USA, 2005.

[85] L. Levidow, S. Carr, Europeanising advisory expertise: The role of'independent, objective and

transparent'scientific advice in agri-biotech regulation, Environment and Planning C: Government and Policy, 26 (2007) 880-895.

[86] G.E. Schrah, R.S. Dalal, J.A. Sniezek, No decision‐maker is an Island: integrating expert advice with information acquisition, Journal of Behavioral Decision Making, 19 (2006) 43-60.

[87] A.W. Brooks, F. Gino, M.E. Schweitzer, Smart People Ask for (My) Advice: Seeking Advice Boosts Perceptions of Competence, Management Science, 61 (2015) 1421-1435.

[88] P. Briggs, B. Burford, A. De Angeli, P. Lynch, Trust in online advice, Social Science Computer Review, 20 (2002) 321-332.

[89] G. Fontaine, The experience of a sense of presence in intercultural and international encounters, Presence: Teleoperators and Virtual Environments, 1 (1992) 482-490.

[90] L. Qiu, I. Benbasat, A study of demographic embodiments of product recommendation agents in electronic commerce, International Journal of Human-Computer Studies, 68 (2010) 669-688.

[91] D. Boer, R. Fischer, M. Strack, M.H. Bond, E. Lo, J. Lam, How shared preferences in music create bonds between people values as the missing link, Personality and Social Psychology Bulletin, 37 (2011) 1159-1171.

[92] T.-C. Lin, C.-C. Liu, Y.-L. Tsai, Factors Affecting Knowledge Integration-Based On Similarity-Attraction Theory, in: PACIS, 2012, pp. 39.

[93] C.B. Gibson, S.G. Cohen, Virtual teams that work: Creating conditions for virtual team effectiveness, John Wiley & Sons, 2003.

[94] K.A. Wallston, B.S. Wallston, S. Smith, C.J. Dobbins, Perceived control and health, Current Psychology, 6 (1987) 5-25.

[95] M. Li, S. Gregor, Outcomes of effective explanations: Empowering citizens through online advice, Decision support systems, 52 (2011) 119-132.

[96] E. Langer, The psychology of control, Sage, Beverly Hills,CA, 1983.

[97] Y. Jung, Understanding the role of sense of presence and perceived autonomy in users' continued use of social virtual worlds, Journal of Computer‐Mediated Communication, 16 (2011) 492-510.

[98] L. Uziel, Look at me, I’m happy and creative: The effect of impression management on behavior in social presence, Personality and Social Psychology Bulletin, 36 (2010) 1591-1602.

[99] K.Y. Tam, S.Y. Ho, Understanding the impact of web personalization on user information processing and decision outcomes, MIS Quarterly, 30 (2006) 865-890.

[100] D.M. De Carolis, P. Saparito, Social capital, cognition, and entrepreneurial opportunities: A theoretical framework, Entrepreneurship Theory and Practice, 30 (2006) 41-56.

[101] G. Chen, S.M. Gully, D. Eden, Validation of a new general self-efficacy scale, Organizational Research Methods, 4 (2001) 62-83.

[102] E. R.Wendler, Consumer information and confidence: moderating effects of perceived comprehension and risk, Advances in consumer research, 10 (1983) 364-369.

[103] J.J. Argo, D.W. Dahl, R.V. Manchanda, The influence of a mere social presence in a retail context, Journal of Consumer Research, 32 (2005) 207-212.

[104] L. Cummins, Social presence: creating on-line learning communities that empower student learning, in: Learning, 2013.

[105] P. Shea, T. Bidjerano, Learning presence: Towards a theory of self-efficacy, self-regulation, and the development of a communities of inquiry in online and blended learning environments, Computers & Education, 55 (2010) 1721-1731.

[106] K. McLaughlin, M. Moutray, O.T. Muldoon, The role of personality and self‐efficacy in the selection and retention of successful nursing students: a longitudinal study, Journal of advanced nursing, 61 (2008) 211-221.

[107] J. Davison, Dilemmas in research: Issues of vulnerability and disempowerment for the social worker/researcher, Journal of Social Work Practice, 18 (2004) 379-393.

[108] K. McFerran, K. Teggelove, Music therapy with young people in schools: After the Black Saturday Fires, Voices: A World Forum for Music Therapy, 11 (2011).

[109] S. Al-Natour, I. Benbasat, R. Cenfetelli, The adoption of online shopping assistants: perceived similarity as an antecedent to evaluative beliefs, Journal of the Association for Information Systems, 12 (2011) 347-374.

[110] I. Qureshi, Y. Fang, E. Ramsey, P. McCole, P. Ibbotson, D. Compeau, Understanding online customer repurchasing intention and the mediating role of trust–an empirical investigation in two developed countries, European Journal of Information Systems, 18 (2009) 205-222.

[111] G. Bansal, F. Zahedi, D. Gefen, The impact of personal dispositions on information sensitivity, privacy concern and trust in disclosing health information online, Decision support systems, 49 (2010) 138-150.

[112] L.R. Goldberg, An alternative" description of personality": the big-five factor structure, Journal of personality and social psychology, 59 (1990) 1216-1229.

[113] W.G. Graziano, N. Eisenberg, Agreeableness: A dimension of personality, in: Handbook of personality psychology, Academic Press, San Diego, CA, 1997, pp. 795-824.

[114] S.D. Gosling, P.J. Rentfrow, W.B. Swann Jr, A very brief measure of the Big-Five personality domains, Journal of Research in personality, 37 (2003) 504-528.

[115] J.A. Howard, SOCIAL PSYCHOLOGY OF IDENTITIES, Review of Sociology, 26 (2000) 367-393.

[116] E.E. Jones, Life as theater: A dramaturgical sourcebook, Psyccritiques, (1975).

[117] N. Mogi, Japanese ways of addressing people, Investigationes Linguisticae, 8 (2002) 14-22.

[118] A.L. Baylor, The impact of pedagogical agent image on affective outcomes, in: International Conference on Intelligent User Interfaces, San Diego, CA, 2005, pp. 29.

[119] V.L. Stamler, D. Pace, T.A. Rosander, H. Singleton, E. Yarris, Client Preference for Women Therapists: A Reflection of our Changing Environment, Grand Valley Review, 9 (1993) 20.

[120] E.F. Walker, J.E. Stake, Changes in preferences for male and female counselors, Journal of Consulting and Clinical Psychology, 46 (1978) 1153.

[121] C.T. Cox, J. Jordan, M.M. Cooper, R. Stevens, Assessing Student Understanding with Technology Science Teacher, 73 ( 2006) 56-60.

[122] K.-S. Suh, Y.E. Lee, The effects of virtual reality on consumer learning: an empirical investigation, Mis Quarterly, (2005) 673-697.

[123] C.J. Soto, O.P. John, Ten facet scales for the Big Five Inventory: Convergence with NEO PI-R facets, self-peer agreement, and discriminant validity, Journal of Research in Personality, 43 (2009) 84-90.

[124] S. Gregor, G. Klein, Eight obstacles to overcome in the theory testing genre, Journal of Association for Information Systems, 15 (2014) 1-19.

[125] W.W. Chin, The partial least squares approach to structural equation modeling, Modern methods for business research, 295 (1998) 295-336.

[126] C.M. Ringle, M. Sarstedt, D. Straub, A critical look at the use of PLS-SEM in MIS Quarterly, MIS Quarterly (MISQ), 36 (2012) 3-14.

[127] T.K. Dijkstra, J. Henseler, Consistent partial least squares path modeling, MIS Quarterly, 39 (2015) 297-316.

[128] D. Barclay, C. Higgins, R. Thompson, The partial least squares (PLS) approach to causal modeling: personal computer adoption and use as an illustration, Technology studies, 2 (1995) 285-309.

[129] D.G. Garson, Partial least squares: regression and path modeling, Stastical Associates Publishing, NC, USA, 2012.

[130] J.M. Hektner, J.A. Schmidt, M. Csikszentmihalyi, Experience sampling method: Measuring the quality of everyday life, Sage, 2007.

[131] R.T. Bradley, R. McCraty, M. Atkinson, D. Tomasino, A. Daugherty, L. Arguelles, Emotion self-regulation, psychophysiological coherence, and test anxiety: results from an experiment using electrophysiologica measures, Applied psychophysiology and biofeedback, 35 (2010) 261-283.

[132] C.-M. Chen, H.-P. Wang, Using emotion recognition technology to assess the effects of different multimedia materials on learning emotion and performance, Library & Information Science Research, 33 (2011) 244-255.

[133] D. Childre, R. Deborah, Transforming stress, New Harbinger Publications, CA, US, 2005.

[134] S. Shahid, E. Krahmer, M. Swerts, W.A. Melder, M.A. Neerincx, You Make Me Happy: Using an Adaptive Affective Interface to Investigate the Effect of Social Presence on Positive Emotion Induction, in: Affective Computing and Intelligent Interaction and Workshops, Amsterdam 2009.

[135] J. Metcalfe, M.J. Greene, Metacognition of agency, Journal of Experimental Psychology: General, 136 (2007) 184-199.

[136] S. Gregor, I. Benbasat, Explanations from intelligent systems: theoretical foundations and implications for practice, MIS Quarterly, 23 (1999) 497-530.

[137] C. Nass, Y. Moon, Machines and mindlessness: Social responses to computers, Journal of social issues, 56 (2000) 81-103.

[138] C.R. Berger, W.B. Gudykunst, Uncertainty and communication, Progress in communication sciences, 10 (1991) 21-66.

[139] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS quarterly, 28 (2004) 75-105.

[140] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, Management Information Systems Quarterly, 37 (2013) 337-355.

[141] GSMA, The Mobile Economy 2015, [Online], Available: http://gsmamobileeconomy.com/global/ [Last accessed 08-07-2015], (2015).

[142] F. Burstein, A. Zaslavsky, N. Arora, Context-aware mobile agents for decision-making support in healthcare emergency applications, in: Proceedings of the 1st Workshop on Context Modeling and Decision Support Context, Frankrike,Paris, 2005.

[143] P.S. Stephen, Online Vicarious experience: using technology to help consumers evaluate physical products over the Internet, PhD thesis, in: Department of Information Systems, Melbourne University, Melbourne, Australia, 2006.

[144] C.W. Leach, M. van Zomeren, S. Zebel, M.L. Vliek, S.F. Pennekamp, B. Doosje, J.W. Ouwerkerk, R. Spears, Group-level self-definition and self-investment: a hierarchical (multicomponent) model of in-group identification, Journal of personality and social psychology, 95 (2008) 144-165.

## APPENDICES

Table A-1.Variable names, measurement scales, mean, standard deviation and item loadings

<table><tr><td>Variable</td><td>Measure</td><td>Mean(Std.dev)</td><td>Std.Loadings</td></tr><tr><td colspan="4">Perceived Understanding(PU) (7-Point Likert Scale, ranging from “Strongly Disagree” to “Strongly Agree”; adapted from the informativeness scale in [143])Cronbach&#x27;s Alpha: .864.</td></tr><tr><td>PU1</td><td>I feel informed about how to deal with stress.</td><td rowspan="2">5.4950(0.97)</td><td>.785</td></tr><tr><td>PU2</td><td>I feel informed about what is resilience.</td><td>.870</td></tr><tr><td>PU3</td><td>I feel informed about what is positive attribution.</td><td></td><td>.792</td></tr><tr><td>PU4</td><td>I feel informed about what is locus of control.</td><td></td><td>.761</td></tr><tr><td>PU5</td><td>I feel informed about the effective methods to reduce stress.</td><td></td><td>.850</td></tr><tr><td>PU6</td><td>I feel informed about how the system can help me in the future.</td><td></td><td>.778</td></tr><tr><td>PU7</td><td>I feel informed about what I can do if my friends,family members or I encounter similar things in the future.</td><td></td><td>.761</td></tr><tr><td colspan="4">Social Presence(SP) (7-Point Likert Scale, ranging from “Strongly Disagree” to “Strongly Agree”; adopted from [68])Cronbach&#x27;s Alpha: .857.</td></tr><tr><td>SP1</td><td>There is a sense of human contact when interacting with the virtual advisor.</td><td>4.5614(1.14)</td><td>.803</td></tr><tr><td>SP2</td><td>There is a sense of personalness when interacting with the virtual advisor.</td><td></td><td>.717</td></tr><tr><td>SP3</td><td>There is a sense of sociability when interacting with the virtual advisor.</td><td></td><td>.855</td></tr><tr><td>SP4</td><td>There is a sense of human warmth when interacting with the virtual advisor.</td><td></td><td>.855</td></tr><tr><td>SP5</td><td>There is a sense of human sensitivity when interacting with the virtual advisor.</td><td></td><td>.784</td></tr><tr><td colspan="4">Experiential Resonance (ER) (7-Point Likert Scale, ranging from “Strongly Disagree” to“Strongly Agree”; adapted from [144])Cronbach&#x27;s Alpha: .932.</td></tr><tr><td>ER1</td><td>I see the virtual advisor as having a lot in common with me as a person (in our past experiences).</td><td>4.044(1.48)</td><td>.966</td></tr><tr><td>ER2</td><td>I perceive that the virtual advisor is similar to me as a person (with common experiences).</td><td></td><td>.958</td></tr><tr><td colspan="4">(Inner) Sense of Control (SC) (7-Point Likert Scale, ranging from “Strongly Disagree” to“Strongly Agree”; adopted from[50] and[95])Cronbach&#x27;s Alpha: .817</td></tr><tr><td>SC1</td><td>I felt confused after using the system.(R)</td><td rowspan="2">4.6140(1.19)</td><td>.857</td></tr><tr><td>SC2</td><td>I felt calm after using the system.</td><td>.845</td></tr><tr><td>SC3</td><td>I felt in control after using the system.</td><td></td><td>.811</td></tr></table>

##

SC4 I felt frustrated after using the system.(R)

<table><tr><td rowspan="2" colspan="4">(External) Perceived Power(PP) (7-Point Likert Scale, ranging from “Strongly Disagree” to “Strongly Agree”; adapted from the self-efficacy scale in [101])</td></tr><tr></tr><tr><td>PP1</td><td>After using the system, I feel I have power to keep a stable mental status to achieve my goals.</td><td>5.1711(0.95)</td><td>.698</td></tr><tr><td>PP2</td><td>After using the system, I am certain that I can cope with stress when I perform rescue tasks.</td><td></td><td>.794</td></tr><tr><td>PP3</td><td>After using the system, I think I can obtain good state of mind that is important to me during my work.</td><td></td><td>.757</td></tr><tr><td>PP4</td><td>After using the system, I believe that I can succeed to overcome unhealthy emotions when performing tasks.</td><td></td><td>.847</td></tr><tr><td>PP5</td><td>After using the system, I feel that I have power to successfully handle stress when facing many challenges.</td><td></td><td>.808</td></tr><tr><td>PP6</td><td>After using the system, I feel that I can perform effectively on many different tasks in my work while keeping a healthy mental status.</td><td></td><td>.632</td></tr><tr><td>PP7</td><td>After using the system, I have a stronger sense of power to do most tasks well compared with my peers.</td><td></td><td>.765</td></tr><tr><td>PP8</td><td>After using the system, I feel psychologically prepared to be able to perform tough rescue tasks well.</td><td></td><td>.760</td></tr><tr><td colspan="4">Agreeableness(AG) (7-Point Likert Scale, ranging from “Strongly Disagree” to “Strongly Agree”; adopted from[123])</td></tr><tr><td>AG1</td><td>I see myself as someone who tends to find good side of other people.</td><td>5.4800(1.04)</td><td>.801</td></tr><tr><td>AG2</td><td>I think I’m helpful to people and selfless to others.</td><td></td><td>.723</td></tr><tr><td>AG3</td><td>I think I seldom start disputes with other people.</td><td></td><td>.797</td></tr><tr><td>AG4</td><td>I think I have a tolerant nature.</td><td></td><td>.846</td></tr><tr><td>AG5</td><td>I think I am generally trustworthy.</td><td></td><td>.748</td></tr><tr><td>AG6</td><td>I think I am treating others with enthusiasm instead of coldness.</td><td></td><td>.751</td></tr><tr><td>AG7</td><td>I think I am thoughtful and kind to almost all people.</td><td></td><td>.732</td></tr></table>

Table A-2. Overview of coding processes

<table><tr><td>Domain</td><td>Category</td><td>Concepts</td></tr><tr><td rowspan="5">Reality checkCompelling need from emergency rescuers</td><td rowspan="2">The need for emotional support</td><td>The need for capabilities of inner emotion control</td></tr><tr><td>The need for confidence and power in dealing with work challenges</td></tr><tr><td rowspan="3">The need for cognitive support</td><td>Lack of readily access to psychological self-help knowledge</td></tr><tr><td>Limited psychological knowledge and biased view towards consultation</td></tr><tr><td>New staff needs formal training on psychological knowledge</td></tr><tr><td rowspan="3">ERMS empowerment</td><td>Cognitive Empowerment through ERMS</td><td>Psychological Knowledge for empowerment (e.g., self-assessment information, bio data etc.)</td></tr><tr><td rowspan="2">Emotional empowerment through ERMS</td><td>Experiential resonance/empathy for empowerment</td></tr><tr><td>Social presence/accompany for empowerment</td></tr><tr><td>The Choice of VAI for ERMS</td><td>Identity of the virtual advisor (expert vs. peer)</td><td>Divided view on VAI&#x27;s impact on ERMS</td></tr></table>

## Table A-3. A brief Introduction and sample screen shots of ERMS

Note <sup>1</sup>: Here we only provided a brief description of the technical design to give the readers an idea of how ERMS looks like. Due to the current research focus on HCI issues, more technical details are not provided here while it is still under patent application.

<table><tr><td colspan="3">Examples of user interfaces</td><td>Breif  $descriptions^1$ </td></tr><tr><td colspan="3">(main page: left:VPA, right: VEA)</td><td>Consultation service</td></tr><tr><td colspan="2"><img src="/api/attachments/YS9CYY9S/fulltext/images/ff09e9878c2e9782a579cd8d9a13dfda820b758775ff38ca14aaf3f1e0694a2c.jpg"/></td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/51f8f6d6e4208587ef6add1e976dfee57eb9865400a0e306c9b207e857c5d72b.jpg"/></td><td>Users can interact with an animated virtual advisor who exhibits humanoid features including a rich set of facial expressions and movements. Communications via both voice and text. Detailed and transparent psychological knowledge with explanations from professional sources or fellow rescuers.</td></tr><tr><td colspan="3">(same across two versions)</td><td>Self-assessment</td></tr><tr><td colspan="2">.ZWH5]</td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/599e28046e6a9fce933eb410d75d33ad158c1439c0e8bfa403b57f5f319a63e2.jpg"/></td><td>Users can obtain timely and personalised feedback on their mental status via psychological self-assessment tools. There are a comprehensive set of self-assessment questionnaires that were based on established professional sources.</td></tr><tr><td colspan="3">(same across two versions)</td><td>Knowledge inquiry</td></tr><tr><td colspan="2"><img src="/api/attachments/YS9CYY9S/fulltext/images/419b6e1bcf8809a0a920b111801640fba1b3646331edd6d3cadb089e6384508e.jpg"/></td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/cede5d5e6093b82d5f8793d8f8b0134a6b54c20198b810f29ba6086eb9bd71f2.jpg"/></td><td>Users can learn systematic and structured psychological knowledge, covering topics such as methods for coping with depression, insomnia and anxiety, with official and credible references and resources provided based on a comprehensive knowledge base.</td></tr><tr><td colspan="3">(same across two versions)</td><td>Supplementary answer</td></tr><tr><td colspan="2"><img src="/api/attachments/YS9CYY9S/fulltext/images/5ec393285a408bbd40acf5cc2ef1b08e1c052066585db70bcb0b0f95de438491.jpg"/></td><td><img src="/api/attachments/YS9CYY9S/fulltext/images/582fd6c7133114fde996c52a3edcecb7cb5b13e004f3e71ebcf03259e97d531c.jpg"/></td><td>Users can browse questions and responses provided by other users or present their own viewpoints for other people&#x27;s reference, while ensuring privacy. The system can also notify users that he/she has received responses from other users. Professionals need to screen all candidate posts by users to ensure consistency and correctness of the candidate answers.</td></tr></table>

#

<table><tr><td>(same across two versions)</td><td>Physiological monitoring</td></tr><tr><td><img src="/api/attachments/YS9CYY9S/fulltext/images/9e1e2a997bced8d08fb1c13e5da0775d1273ee03a502150209a903a2d078189d.jpg"/></td><td>Users’ physiological indices can be monitored via wearable devices with results presented in the form of graphs and tables. They can view personalized data displayed in an intuitive form. It also allows users to determine the appropriate place and time to receive treatment.</td></tr></table>
