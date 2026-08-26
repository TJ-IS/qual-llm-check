---
otero_id: 7830
otero_key: "8JAAZ7FJ"
title: "Understanding Physicians’ Online-Offline Behavior Dynamics: An Empirical Study"
authors: "Liuan Wang; Lu (Lucy) Yan; Tongxin Zhou; Xitong Guo; Gregory R. Heim"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0901"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/8JAAZ7FJ/fulltext/images/7419ab4e72e0184d9e0de8d7c23f860a4fffde142d7b9c60998ddca077778447.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Understanding Physicians’ Online-Offline Behavior Dynamics: An Empirical Study

Liuan Wang, Lu (Lucy) Yan, Tongxin Zhou, Xitong Guo\*, Gregory R. Heim

To cite this article:

Liuan Wang, Lu (Lucy) Yan, Tongxin Zhou, Xitong Guo\*, Gregory R. Heim (2020) Understanding Physicians’ Online-Offline Behavior Dynamics: An Empirical Study. Information Systems Research

Published online in Articles in Advance 08 May 2020

https://doi.org/10.1287/isre.2019.0901

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Understanding Physicians’ Online-Of<sup>fl</sup>ine Behavior Dynamics: An Empirical Study

Liuan Wang,<sup>a</sup> Lu (Lucy) Yan,<sup>b</sup> Tongxin Zhou,<sup>c</sup> Xitong Guo,<sup>d,</sup>\* Gregory R. Heim<sup>e</sup>

<sup>a</sup> School of Economics and Management, Beihang University, Beijing 100191, China; <sup>b</sup> Department of Operations and Decision Technologies, Kelley School of Business, Indiana University, Bloomington, Indiana 47405; <sup>c</sup> Department of Information Systems and Operations Management, Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>d</sup> School of Management, Harbin Institute of Technology, Harbin 150080, China; <sup>e</sup> Department of Information & Operations Management, Mays Business School, Texas A&M University, College Station, Texas 77843

\*Corresponding author

Contact: wangliuan1973@gmail.com, https://orcid.org/0000-0003-1011-4936 (LW); yanlucy@indiana.edu, https://orcid.org/0000-0001-8408-0404 (L(L)Y); txzhou5@uw.edu, https://orcid.org/0000-0001-8505-4021 (TZ); xitongguo@hit.edu.cn, https://orcid.org/0000-0002-9569-0299 (XG); gheim@mays.tamu.edu, https://orcid.org/0000-0002-3770-5384 (GH)

Received: Revised: June 28, 2018; March 26, 2019 June 28, Accepted: Published Online in Articles in Advance: May 8, 2020

https://doi.org/10.1287/isre.2019.090

Copyright:

Abstract. Physicians’ participation in online healthcare platforms serves to integrate online healthcare resources with the offline medical system. This integration brings opportunities for reshaping healthcare delivery systems. In the field of telemedicine, there has been an extensive discussion about physician participation, but little is known about how physicians actually participate in online healthcare platforms and offline medical systems. Understanding physicians’ participation dynamics between online and offline channels is of great importance to academic researchers, practitioners, and policy makers. Such an understanding can reveal insights into how healthcare is actually delivered to patients through both channels, how to contribute to quantifying the social impacts of online healthcare services (Health 2.0), and how to improve healthcare delivery systems. Thus, in this study, we investigate physicians’ online-offline behavior dynamics using data from both online and offline channels to conduct our analysis. As physicians’ online and offline activities are highly endogenous, we deploy a time-series technique and develop a structural vector autoregression model to examine the behavior dynamics. We find that physicians online activities can lead to a higher service quantity in offline channels, whereas offline activities may reduce physicians’ online services because of resource constraints. Our results also show that the more offline patients physicians serve, the more articles the physicians will likely share online. These findings are robust to various econometric specifications and estimation methods. Our research advocates for the benefits Health 2.0 produces and provides evidence of the value of online healthcare communities and the policies that support them.

History: Giri Kumar Tayi, Senior Editor; Param Singh, Associate Editor Funding: X. Guo acknowledges the financial support from the National Science Foundation of China [Grants 71622002, 71531007, and 71471048]. Supplemental Material: The online supplement is available at https://doi.org/10.1287/isre.2019.0901.

Keywords: physicians’ online participation • online-of<sup>fl</sup>ine behavior dynamics • endogenous system • structural vector autoregressio (SVAR) models

## 1. Introduction

Online healthcare platforms are prospering and have significantly changed how physicians provide services to patients (Eysenbach 2008, Goh et al. 2011). This change can be seen in physicians’ increasing participation in online healthcare platforms as a means of interacting with patients in regard to health concerns or medical issues (Das et al. 2015, Roettl et al. 2016). In the past, physicians typically provided healthcare services through office visits. However, patients themselves decide whether, when, and how to seek medical attention, known as “self-triage” in the medical literature (Mettler and Kemper 2003, Cooper and

Humphreys 2008, Eijk et al. 2014). Because most patients lack professional training in health and healthcare, their decisions to request medical help may not be timely, which could lead to disease complications and other unfavorable consequences that require more complex, lengthy medical attention (Kaplan et al. 1989, Mettler and Kemper 2003).

Physicians, by contrast, are healthcare specialists who provide professional assistance in addressing patients’ health concerns. Finding a new way to enable physicians to interact with patients in a timely and cost-effective manner not only helps patients reduce the delay that may result from their self-triage decisions prior to offline visits but also increases physicians’ service levels and enhances public engagement in health management (Hawn 2009, Goh et al. 2016). Research has shown that physicians’ participation in online healthcare platforms can help patients to make better clinical decisions (Raghupathi and Raghupathi 2014, Li et al. 2016), alleviate rural-urban health disparities (Muñoz 2010, Goh et al. 2016), and improve the physician-patient relationship (Hewitt-Taylor and Bond 2012, Detz et al. 2013). Thus, it is not surprising that there is a growing trend toward promoting cost-effective online interactions between physicians and patients (Coelho et al. 2005) and that an increasing number of physicians are participating in online healthcare platforms to provide professional assistance to meet patients’ healthcare needs (Roettl et al. 2016).

Despite the potential impact of online healthcare platforms that bridge online healthcare service to offline healthcare delivery systems (Agarwal et al. 2010, Fichman et al. 2011), few studies have explored physicians’ participation dynamics between online and offline activities. Given that physicians are the major medical service suppliers and are restricted by available time and resources (Dugdale et al. 1999), it is intuitive that their offline healthcare activities likely affect their participation in these online healthcare platforms. For example, in regard to the observation of patients’ common symptoms during, for example, flu season, physicians can use online platforms to share instructions on how to anticipate and prevent relevant health issues with a broad audience base. Likewise, online activities may, in turn, affect physicians’ offline medical services. For example, through online participation, physicians can use their professional knowledge to help patients make better judgments about their conditions in a timely manner, which will reduce help-seeking failures offline (Eysenbach 2000, Mettler and Kemper 2003).

Thus, in this study, we are interested in examining physicians’ online-offline behavior dynamics. In particular, we ask, “How do physicians’ online activities affect their offline activities, and vice versa?” To address this question, we utilize two unique data sets collected from online and offline channels. The first data set is from a physician-patient social mediabased online healthcare platform that allows physicians to communicate directly with patients and provide health services at little or no financial cost to the patient. In this data set, we collected physicians’ online activities: consultation services provided in response to patient inquiries and articles posted on the platform to disseminate professional knowledge. This data set also contains patients’ feedback about physicians’ services, which may influence physicians online-offline behavior and participation dynamics.

The second data set involves clinical visits (e.g., the number of outpatients in a hospital at the national level). This data set is collected and provided by the National Health Commission of China (Nationa Health Commission 2017).

One of the most obvious challenges in this study is that physicians’ online and offline activities are highly endogenous, creating barriers for adopting traditional econometric methods. Problems, such as endogeneity in the interdependent evolution of physicians’ online and offline activities, and other biases, such as autocorrelation and reversed causality, may make traditional econometric methods not suitable for this study (Adomavicius et al. 2012, Luo et al. 2013). Therefore, we developed a structural vector autoregression (SVAR) model, which allows us to track the dynamics of temporal relationships in an endogenous system. By incorporating additional contemporaneous structure into a standard vector autoregression (VAR) model, the proposed SVAR model can likewise address potential simultaneity among variables in the system. In particular, our empirical model consists of five variables that capture physicians’ online consultations, knowledge sharing, fulfillment of offline healthcare service activities, and patients’ feedback about the physicians’ online and offline services. Because we allow these variables to interact with each other, we are able to track physicians’ online-offline behavior dynamics throughout this ecosystem.

There are several important findings from our empirical analysis. First, we find that an increase in the number of online consultations and online articles can lead to more outpatient visits in subsequent periods, suggesting that physicians’ online activities can lead to increased service quantity at hospitals. By contrast, we find that an increase in the number of outpatient visits leads to fewer online consultations. That is, an increased offline workload may reduce physicians’ availability to provide online services, as physicians are constrained by time and resource limits (Dugdale et al. 1999). Third, we find that an increase in the number of outpatient inquiries can lead to physicians sharing more online articles in the following time period, indicating that their daily practice activities in hospitals trigger their knowl edge sharing in online healthcare platforms. This finding is in keeping with our observation from the data set that physicians often post about their clinical specialty and answer patients’ frequently asked questions in their online articles. In addition, we find that the impact of outpatient inquiries on online articles is different from that on online consultations Compared with online consultations, which require physicians to spend time addressing patients’ health problems and concerns, posting online articles requires much less time and effort. This further reveals that online articles and online consultations are fundamentally distinct online activities and that different mechanisms are at work. These findings are robust for various system configurations and variable permutations.

Adding to a growing literature on applications of social media platforms in broader information systems studies, our study makes four contributions. First, the behavioral dynamics of physicians revealed by our study illustrate the social value of online healthcare platforms for the entire healthcare delivery system. We show that physicians’ participation in online healthcare platforms can serve to integrate online healthcare resources with offline healthcare systems. Despite the recent promotion of Health 2.0 and Medicine 2.0—the application of participationenhancing tools enabled by Web 2.0—and related discussions about telemedicine, our study, to the best of our knowledge, is the first to examine the integration of physicians’ online and offline activities and to quantify the impact of such integration. Second, our work contributes to the literature on online professional activities. Consistent with prior studies (Lerner and Tirole 2002, Singh et al. 2011b, Hwang et al. 2015), our study provides evidence that physicians’ online professional activities tend to improve their offline activities. We extend this research stream by linking both online and offline professional activities in the healthcare context. Third, our work is related to resource-based theories, which suggest that an investment in one type of activity may decrease the investment in another type because of resource constraints (Dugdale et al. 1999, Butler 2001). We find that physicians’ offline workloads may decrease their online professional activities because of limited time and capabilities. This finding also extends the research on community sustainability and the longterm effects of online platforms, as online communities require a significant number of users—physicians, in our case—to participate and contribute actively. Finally, our work contributes to the stream of literature on the motivations for knowledge sharing in online environments. We show that work-related concerns may serve as a driving factor for professionals to share knowledge online.

Our work is also of interest to healthcare practitioners and policy makers. First, our results provide evidence for the positive impact of physicians’ online healthcare service activities on offline medical systems. We show that online healthcare platforms supplement offline healthcare delivery systems, and we recommend that policy makers and healthcare providers develop social media strategies to integrate online resources with offline systems more effectively. Our findings also provide support for the Chinese government’s new medical policy, “Internet plus Medical” (China State Council 2015), which aims to encourage the development of the online healthcare industry. Second, our results demonstrate that physicians’ offline workloads can negatively affect their participation in online consultations. Thus, the sustainability of online healthcare resources requires the improvement of online-offline coordination and better system design. Finally, although our findings are based in the healthcare context, they can be applied to other professional industries in which individuals are able to provide professional services in both online and offline channels, such as opensource communities.

The rest of this paper is organized as follows. In Section 2, we explain our research context and discuss the related literature. In Section 3, we describe the data sets and variables. Then, in Section 4, we introduce the SVAR framework and propose our empirical model. We present our analysis results and main findings in Section 5. In Section 6, we summarize our work and discuss its theoretical contributions as well as managerial insights.

## 2. Research Background and Literature Review

To understand how physicians’ online and offline activities are linked to healthcare delivery systems, we examine physician-patient online healthcare platforms, emerging online healthcare communities that enable physicians to provide healthcare services to patients through the web or mobile devices and thus have the potential to shape healthcare delivery systems. In the following, we first describe physician-patient online healthcare platforms and related findings in the extant literature. We then discuss theories that are related to physicians’ online and offline activities. On the basis of this discussion, we propose an ecosystem that describes physicians’ online-offline dynamics, which serves as the theoretical foundation for our study.

2.1. Physician-Patient Online Healthcare Platforms Physician-patient online healthcare platforms are online healthcare communities that allow physicians to interact directly with patients regarding health-related issues. Different from patient-oriented online healthcare communities that promote patients’ roles in their own health management, physician-patient online healthcare communities facilitate moving physicians professional services from physical offices to virtual offices. Just like outpatient office visits, the physician patient conversation can include multiple information exchanges. The outcome of this type of conversation may either eliminate patients’ health concerns or lead to a hospital visit for proper medical attention. Physicians also can use online platforms to disseminate general information, such as guidelines on disease prevention or articles related to their area of medical expertise.

This digital transformation of health and healthcare can stimulate more cost-effective service delivery, quality, efficiency, and user experience (Eysenbach 2008, Agarwal et al. 2010, Fichman et al. 2011). Compared with a face-to-face office visit, online communication between physicians and patients has important advantages, such as reduced waiting times, low travel expenses, and minimized operational costs. Thus, it is not surprising that physician-patient online platforms are becoming popular (Roettl et al. 2016). For example, the Mayo Clinic has started to provide online services to patients with the aim of providing high-quality medical services at a lower cost (Das et al. 2015, Tieu et al. 2015). There are also third-party physician-patient platforms such as AskTheDoctor.com and HealthTap.com that facilitate physician-patient interactions. Physicians welcome such initiatives and consider online healthcare platforms as a way to approach and interact with patients and a means to show their professional responsibility and competency (Das et al. 2015).

Observing the potential important impacts of social media-enabled applications on health and healthcare systems, an emerging area of research has focused on how physician-patient online healthcare platforms can be utilized to improve information flow from healthcare specialists to patients. Research has found that the internet can facilitate efficient communication between physicians and patients, which helps to improve the physician-patient relationship (Ball and Lillis 2001, Hewitt-Taylor and Bond 2012, Detz et al. 2013), empower patients in care-seeking processes (Santana et al. 2010, Li et al. 2016), and rebalance healthcare resource allocation in rural and urban areas (Muñoz 2010, Goh et al. 2016, Hwang et al. 2017).

Our research is related to this stream of literature in how it evaluates physicians’ engagement with patients through physician-patient online healthcare communities. Our study, however, is distinct because we consider the entire healthcare service system, both online and offline, as an integrated ecosystem and investigate physicians’ behavior dynamics within this phenomenon. As a result, our research adds to this area of literature by exploring opportunities beyond information flow from physicians to patients. Moreover, our study considers not only the interdependence of physicians’ online and offline activities but also stimuli that improve the entire healthcare delivery system, such as work-related concerns motivating professional knowledge sharing.

## 2.2. Literature Review

In addition to the literature on social media in healthcare, our study is also related to three other research streams. The first comprises research on individuals’ professional activities in an online environment. We add to this literature by linking physicians’ online and offline activities and presenting the interdependent connections of these activities. The second area concerns self-motivated posting activities in professional communities. Knowledge sharing is a core component of professional communities, and we contribute to the extant literature by including both physicians and patients as recipients. The third stream concerns the feedback system in online healthcare platforms. We extend this literature by showing how patients’ online feedback can affect physicians online-offline behavior dynamics.

2.2.1. Participation in Online Professional Communities. Social media have enabled individuals to use online platforms to communicate, participate, and contribute to many aspects of their lives, including professional services. Online professional communities are virtual places that allow individuals to practice their expertise and to perform professional activities (Wenger and Snyder 2000). Examples of such communities include physician-patient healthcare communities, where physicians provide medical assistance to patients outside of office visits; opensource communities, where software developers work on side projects to improve their programming skills; and enterprise platforms, where employees communicate and share work-related experiences to improve their professional skills. These professional communities, when integrating online resources with similar offline tasks, are found to be helpful in improving work efficiency in the physical world. Open-source communities, for example, are found to be effective in improving developers’ professional skills through their participation in online project development and other learning opportunities obtained from being connected to the community (Singh et al. 2011b). Their performance rankings also are related to their participation level in the community (Roberts et al 2006). The more work they have done, the more they will be allowed to do, leading to exposure to more diverse and challenging tasks that can further enhance their professional skills and experience.

Likewise, in the healthcare context, physicians online activities can be integrated with their offline professional work. Physicians can communicate with patients through online platforms to address certain medical concerns, handle follow-ups of clinical care online to reduce office visits, improve resource allocation efficiency, and help patients avoid travel expenses (Goldzweig et al. 2009, Das et al. 2015). These online professional consultations not only help improve operational efficiency in offline healthcare systems (Griffiths et al. 2006, Tate et al. 2009) but also allow physicians to transmit medical information and their professional opinions to patients in a timely manner as well as improve diagnosis efficiency and treatment outcomes in offline channels (Tate et al. 2009, Li et al. 2016). They also lead to an improved physician-patient relationship (Ball and Lillis 2001, Hewitt-Taylor and Bond 2012, Detz et al. 2013).

Although there are significant benefits related to physicians’ participation in online professional communities, physicians’ online activities have limits. Resource-based theories state that individuals need to invest time and effort, among other resources, to acquire benefits from online activities (Dugdale et al. 1999, Butler 2001). In other words, physicians’ online participation and their offline clinic schedule are interdependent. When a physician has a full offline services schedule, his or her availability to provide online consultations will be largely reduced. Because offline activities are still the main responsibility in most professional industries, online professional activities need to be performed in one’s off-duty time. Thus, physicians’ online professional activities may only supplement, but not replace, offline healthcare services (Farnan et al. 2013). Nevertheless, as physicians use online communities to educate patients and improve healthcare efficiency, such online professional activities may lead to reductions in physicians’ offline workloads as a result of reductions in-office visits. How physicians’ online and offline activities may interact, however, remains unclear— specifically, how, given limitations of time and resources, physicians’ online activities are integrated with offline activities. Our work contributes to the literature on professional activities in an online environment by studying how physicians’ online and offline activities can form an integrated system.

2.2.2. Knowledge Sharing in Professional Communities. Knowledge sharing through online social networks has been widely studied in the literature. There is substantial evidence, revealed in prior studies on user-generated content and information diffusion, that online knowledge sharing can help individuals make informed decisions (Miranda and Saunders 2003, Goh et al. 2013) and that there is a small group of people, the opinion leaders, who exert social influence on others’ opinions (Iyengar et al. 2011, Lu et al. 2013). Similarly, physicians in online healthcare communities can be considered opinion leaders, as they facilitate information diffusion to patients and help them to understand their health conditions better. Yet, compared with the relationship between the traditional role of opinion leaders and susceptible social media users, there are two important aspects that make professional communities different from other online contexts. First, knowledge sharing in professional communities is typically work related and includes workplace experiences or one’s work-related expertise or skills (Lin et al. 2009, Huang et al. 2015). For instance, in online healthcare communities, physicians often share medical expertise and clinical ex perience with their professional peers to increase their knowledge and awareness of a topic or disseminate healthcare information or guidelines to inform patients and improve patients’ health management. Both opinion leaders and other media users can be active content contributors, but in our context, physicians are the main information source that facilitates the information diffusion process while patients are the information recipients. Second, studies on opin ion leaders typically explore the diffusion pattern within a social context, without expanding the possible online influence to the offline physical world. However, such a relationship could exist in professional communities.

The importance of knowledge sharing in professional organizations has been well recognized in organizational science and sociology literature (Nonaka 1994, Spender and Grant 1996). Although knowledge sharing through online posts is not directly linked to professional practice, such behavior in professional communities can potentially positively affect the associated offline activities. For example, sharing knowledge among professionals can facilitate innovations in offline working practices and increase firms’ competitiveness (Nonaka and Takeuchi 1995, Stewart and Ruckdeschel 1998), help employees to execute routine tasks more efficiently (Hall 2001, Hwang et al. 2015), improve individuals’ understanding about the work environment and coworkers (Hall 2001, Huang et al. 2015), and create opportunities to garner experience and gain skills (Wenger and Snyder 2000, Singh et al. 2011a, Hwang et al. 2015). Knowledg sharing can also result in one’s continuing contributions to professional communities. When one is expecting career-related benefits from knowledge sharing, he or she will be more likely to share knowledge (Bock et al. 2005, Hsu et al. 2007) related to such endeavors as skill development, reputation building, and career advancement (Sharratt and Usoro 2003, Shah 2006). Furthermore, healthcare professionals tend to share knowledge with their peers in online communities that help to improve their realworld practices (Hara and Foon Hew 2007).

Our study is related to this literature stream through our investigation of physicians’ knowledge sharing behaviors in a physician-patient online healthcare platform. Different from prior studies on knowledge sharing among professional peers is that, in our study, the knowledge physicians share is available to both professional peers and laymen (i.e., patients). We also demonstrate how offline professional practices affect online knowledge sharing, and thus, we extend prior studies on the motivations for knowledge sharing in online professional communities.

2.2.3. Patients’ Reviews in Online Healthcare Platforms. Tools that allow for feedback, such as user reviews or ratings, are popular social media applications, as they enable individuals to share their experiences on product or service quality (Dellarocas 2003, Chen and Xie 2008) and to gather information for potential decisions about getting said product or service. Professional industries, such as healthcare, are often associated with high information asymmetry (Gao et al. 2012, Goh et al. 2016), which makes it difficult for consumers to assess the quality of professional services. In most physician-patient online healthcare platforms, patients can write and share reviews about their firsthand medical experiences and rate their physicians. Patients’ online feedback can help other potential patients to assess physicians medical services better and increase transparency in healthcare (Gao et al. 2012).

Whereas prior studies suggest that feedback about physicians may not be a reliable indicator of quality of care (Gao et al. 2012, Okike et al. 2016), other studies find that these reviews are useful for patients to learn from others’ treatment experiences so that they can perform self-experience comparisons related to concerns such as the severity of side effects or proper dosages (Yan et al. 2019), assess the effectiveness of a treatment (Yan and Tan 2017), and increase their adherence to medical instructions and the proper use of prescriptions (Horne and Weinman 1999). Feedback from patients also enables physicians and other professionals in the healthcare sector to understand patients’ concerns better and to gather treatment data for medical improvement (Kallinikos and Tempini 2014, Emmert et al. 2016).

Our work is related to this stream of literature by considering the effect of patients’ feedback on physicians’ online and offline services. Whereas reviews for physicians’ offline healthcare services may affect patients, and online inquiries and feedback about physicians’ online activities may shape the number of physicians’ offline service requests, we add the potential role patients’ feedback plays in terms of physicians’ online-offline behavior dynamics. In this way, we extend the literature on the social value of reviews shared by individual users.

## 2.3. The Ecosystem of Physicians’ Online-Of<sup>fl</sup>ine Professional Activities

On the basis of the literature presented, we apply theories to physician-patient online healthcare communities and construct an ecosystem that captures physicians’ online-offline behavior dynamics.

The ecosystem has four basic components: physicians’ online professional services (e.g., online consultations), knowledge sharing activities (e.g., online articles), physicians’ offline services, and online feedback provided by patients regarding physicians service quality. Online service and knowledge sharing capture two different types of physicians’ online activities. Offline service is measured by the number of offline services physicians performed. The inclusion of the online feedback component allows us to capture the indirect influence on physicians’ behaviors. That is, certain behaviors may not affect other behaviors directly but may exert an indirect influence through online feedback. Capturing the indirect influence on physician behaviors is important to understand the dynamic changes of the entire system over time. Figure 1 provides a graphic presentation of the online-offline ecosystem, for which each arrow represents a potential interaction between two components.

According to theories related to interactions between online and offline professional activities, professionals’ online activities can be integrated into their offline professions to improve work efficiency (Singh et al. 2011b, Li et al. 2016). Likewise, physicians’ online consultations can have positive effects on offline patients’ clinical visits, leading to informed patients with requests for medical help offline (arrow 1). At the same time, physicians’ offline services may affect their online professional activities (arrow 2). This is because, as suggested by resource-based theory (Dugdale et al. 1999, Butler 2001), physicians are constrained by the time and energy needed to perform their offline duties, which are their main responsibilities, and this will affect their participation in online communities.

Figure 1. Physicians’ Behavior Ecosystem  
![](/api/attachments/8JAAZ7FJ/fulltext/images/bbb5478498e5f9f49710a97257b1e45e7a5b7e481569cf45cd340d6a90a97236.jpg)

Theories of online knowledge sharing also suggest the existence of interdependencies between physicians’ online and offline activities. Specifically, physicians’ online service and knowledge sharing may influence patients’ health management (Tate et al. 2009, Li et al. 2016) and, consequently, affect the amount of service that physicians need to perform offline (arrows 1 and 3). In addition, as potential work-related benefits can serve as a motivation for knowledge sharing (Bock et al. 2005, Hsu et al. 2007), physicians’ offline practices may, in turn, influence their online knowledge sharing behaviors (arrow 4). For instance, physicians’ offline interactions with patients allow physicians to collect clinical experience and patients’ frequently asked questions so that they can utilize the online platform for knowledge sharing. Furthermore, theories of online feedback mechanisms indicate that patients’ online reviews can provide information about physicians’ expertise and disease treatments (Gao et al. 2012, Yan et al. 2019). As such, online feedback may potentially affect physicians online and offline services (arrows 8 and 9). Likewise, physicians’ online and offline services can affect the feedback they receive (arrows 7 and 10).

On the basis of the theories about Health 2.0 and online healthcare communities (Eysenbach 2008, Agarwal et al. 2010, Fichman et al. 2011), we also include other potential interdependencies in our conceptual framework, such as that between physicians’ online service and knowledge sharing (arrows 5 and 6). We include these interdependencies because physicians’ sharing of information with the public will answer some of the questions that patients would have to ask directly through an offline appointment otherwise. In turn, online service may affect knowledge sharing, as physicians’ interactions with online patients also may trigger physicians to share more knowledge. In addition to the interdependencies, we also consider self-interactions. That is, we assume each component to be self-correlated as a time series.

## 3. Data and Variables

We utilize two data sets to study physicians’ onlineoffline behavior dynamics. The first data set comes from a popular Chinese online healthcare platform for physician-patient online communication. The second data set contains national clinical survey data, which are collected and published by the National Health Commission of China. In Section 3.1, we introduce the focal online healthcare platform and then describe the data and construct variables for the analysis.

## 3.1. Focal Online Healthcare Platform

We study a leading physician-patient healthcare platform in China, established in 2006. By 2017, more than 170,000 doctors across the country were registered as platform users (see Section A1 of the online supplement for more information). The registration process requires physicians to provide their certificate of practice as well as information about their employer, job title, and expertise. Only after the platform verifies this information can physicians provide services to patients online. On the platform, physicians can participate in two types of activities: providing healthcare services to patients and sharing healthcare knowledge by posting articles on their home pages. Physicians’ healthcare services on the platform refer to online consultations, including text consultations and telephone consultations. The former allows patients to communicate with physicians through online chats and the latter through telephone calls. In both types of consultations, physicians can only offer advice. To obtain a prescription or any other treatment, patients still need to go to offline healthcare facilities. In our main analysis, we consider physicians’ online consultations over chats (text messages). (Telephone consultations will be discussed in Section 5.3.)

It is important to differentiate physicians’ engagement in online consultations and sharing healthcare knowledge because each reflects a different aspect of their online behaviors. Online consultations require interactions between physicians and patients, whereas publishing articles requires only physicians intellectual efforts. In online consultations, patients initiate the conversation by asking specific healthrelated questions, and physicians offer their professional advice in response to the patients’ requests In online articles, physicians proactively share medical knowledge. On the basis of how physicians are involved in the knowledge sharing process, we distinguish between the two types of behaviors, with the former representing physicians who offer reactive professional services and the latter representing proactive knowledge sharing. In addition, online consultations and online articles satisfy patients’ needs differently. Online consultations allow physicians to offer personalized advice based on the information patients provide. In online articles, however, physicians can choose to provide any medical knowledge that they would like to share with other platform users. Usually, the content shared in the articles is more general compared with what is shared in online consultations. These articles answer patients’ frequently asked questions, give instructions for outpatient visits and procedures, or discuss medical innovations, as shown in Figure 2. It is conceivable that the time and effort required for online consultations and sharing knowledge are significantly different, as online consultations involve an interactive process in which physicians need to engage in understanding patients’ symptoms, disease histories, and concerns, whereas sharing an article is according to physicians autonomy. Thus, we consider it necessary to include both types of activities and to investigate their effects separately.

Figure 2. Composition of Online Article Types  
![](/api/attachments/8JAAZ7FJ/fulltext/images/929fddd81e8ffcb3c9a4e4eb813bfa6a4c589f378aec50361b4c4ee938980b06.jpg)

The platform also provides a review system to gather patients’ feedback. This feedback reflects patients’ satisfaction levels with physicians’ medical services and can be in the form of reviews or virtual gifts. Because offline patients are able to receive treatments from physicians, they can write online reviews about their treatment experiences and comment on physicians’ treatment effectiveness and attitude. For online patients, the main feedback tool is virtual gifts. If patients feel that they are greatly helped by an online consultation with a physician, they can send a virtual gift to the physician to express their gratitude. A screenshot of the focal website is provided in Section A1 of the online supplement.

## 3.2. Data and Variable Description

In this study, as noted, we utilize two data sets. The first data set is from the focal online healthcare platform. We collected time-series data on the number of online consultations, online articles, online reviews, and virtual gifts. Online consultations and publishing online articles are physicians’ two types of online activities. The former reflects physicians online service-providing behaviors, whereas the latter represents physicians’ proactive knowledge sharing. Online reviews and virtual gifts are patients feedback about physicians’ professional services. In particular, online reviews reflect the opinions of patients who received offline services, whereas virtual gifts reflect the satisfaction of patients who consulted a physician on the online platform. We use these feedback data to capture the potential effects of the feedback mechanism on physicians’ online-offline behaviors. The observation period lasted from January 2010 to October 2017.

Figure 3 presents the time-series data on the total number of offline hospitals registered on this platform as well as the total number of physicians who provide online services. In Figure 3, (a) and (b), both time series contain a surge near the end of 2015. This phenomenon is due to the Chinese government’s implementation of a policy regarding the online healthcare industry. The China State Council set forth guidelines on internet healthcare service develop ment in July 2015, “Internet plus Medical” (China State Council 2015), in which the government encouraged the public to participate in the online healthcare industry as a means to improve healthcare services. In November 2015, the guidelines were introduced extensively to the public during the 2015 Internet Plus Health China Conference. This policy implementation generates unique features in our data. Around the date when the policy was introduced to the public, the number of online hospitals and online active physicians significantly increased. We account for this policy change in our later analyses as an exogenous shock.

Figure 4 displays the time series plots of physicians online behaviors and online feedback for physicians. These plots exhibit patterns similar to those of online hospitals and active online physicians (Figure 3), which can be explained by the “Internet plus Medical” policy implementation. The policy resulted in a significant increase in the public’s participation in the online healthcare platform near the end of 2015; accordingly, the level of physicians’ online activities and corresponding online feedback also increased around that time.

As noted, the second data set is from a national clinical survey data set collected by the National Health Commission of China. We downloaded the data from the official website (National Health Commission 2017). The survey is administered on a monthly basis every year and provides us with additional information on the number of outpatient inquiries at hospitals across the country (hereafter, patients’ offline visits). We considered the national hospital distribution and distributions of hospitals that registered on the focal platform and matched this offline data to our online data to measure physicians’ offline activities. Offline visits are depicted in Figure 5. There is a strong periodic pattern shown in the data. The number of offline visits peaks every December, which is typically flu season. This pattern coincides with our observations.

Combining the two data sets, we are able to calibrate physicians’ online and offline activities and study physicians’ behavior dynamics. Table 1 provides the definition of the variables and variable statistics.

## 4. Model Development

In our conceptual framework, physicians’ behaviors are highly endogenous and interdependent. To model such an endogenous system with potential complex dynamic patterns, we employ a time-series technique, a SVAR model. SVAR models are based on the establishment of the underlying VAR model (Sims 1980). In a VAR system, variables are represented by their own lags and that of other variables (Stock and Watson 2001). Adding a contemporaneous structure into a VAR system will form a SVAR model. In a SVAR system, each variable is regressed on its own lags as well as on the current and the lagged values of all other variables. Therefore, SVAR models can address the simultaneity among variables as well as the lagged effects.

Figure 3. Time-Series Plots of Online Hospitals and Online Active Physicians  
(a)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/d1defb9f5194a18a6f4fa5155ad15c4c3408aac967f625b0db25cbc7736cdd3b.jpg)  
No. hospitals registered online

Both VAR and SVAR are designed to analyze the dynamics of multiple time series (Enders 2008). In the literature, VAR has been widely deployed, especially in the field of applied econometrics (Kennedy 2003). Econometricians view VAR as an effective tool in policy analysis because it is able to address reverse causality by tracking the system responses under unexpected shocks. In addition, VAR is able to model all of the possible interactions among variables. In other words, VAR treats all variables as endogenous and does not impose any relationship restrictions. The VAR approach is becoming increasingly popular in the information systems domain. Many researchers have adopted VAR to depict the dynamics within multivariate systems (Adomavicius et al. 2012; Luo et al. 2013, 2017).

The SVAR approach deployed in our study inherits all of the advantages of the VAR model, such as the ability to account for reverse causality and variable endogeneity. This allows us to capture the complex chained effects and feedback loops in the system (Luo et al. 2017). For example, an increase in physicians online activities may result in more offline visits, which may further increase physicians’ subsequent online participation. Modeling these complex interactions among variables and tracking the system responses across time can help us understand how the ecosystem dynamically evolves. Furthermore, the SVAR approach allows us to model the potential simultaneous effects among variables. In our research context, physicians’ online activities and offline activities may be contemporaneously related to each other; for example, too much engagement in offline services may decrease physicians’ online participation in the same period, as physicians have limited time. In the following, we provide a brief discussion about the SVAR framework and then discuss model specification and identification strategies.

(b)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/84f6a5ab7a49179a7a4d6c9b02695e4f54325c5f6502a361a7c08045465ac4b4.jpg)  
No. physicians providing online service

## 4.1. The SVAR Framework

A SVAR model is an n-equation, n-variable linear model, whereby each variable is regressed on its own lags and the current as well as past values of all other variables. That is,

$$
\Gamma \mathbf {Y} _ {t} = B (L) \mathbf {Y} _ {t} + \varepsilon_ {t},\tag{1}
$$

where $Y _ { t }$ is a n-dimensional vector of variables, Γ is a matrix with diagonal normalized to 1, B L represents a set of matrices associated with lagged terms, and $\varepsilon _ { t }$ is a vector of primitive shocks, also known as $^ { \prime \prime } \mathrm { i n - }$ novations.” Assume the variance-covariance matrix of $\varepsilon _ { t }$ is $\Sigma _ { \varepsilon }$ . The forms of SVAR models and structural equation models (SEMs) are the same; in fact, both models address simultaneity among variables. However, the model assumptions and identification methods of the two models are different (Kilian 2013). The major difference is that SEMs interpret $\varepsilon _ { t }$ as errors that contain minor, nonessential influences on the determined variables, whereas in SVAR models, $\varepsilon _ { t }$ is interpreted as unexpected, primitive shocks on the system (Gottschalk 2001). This difference further leads us, in different ways, to place restrictions on the simultaneous structure in the two models for identification purposes. The detailed identification procedure for a SVAR model is discussed in Section 4.3.

A SVAR model starts with a corresponding reduced VAR model (Sims 1980), for which variables are represented by their own lags and that of other variables (Stock and Watson 2001). In particular,

$$
\pmb {\Upsilon} _ {t} = \Gamma^ {- 1} B (L) \pmb {\Upsilon} _ {t} + \Gamma^ {- 1} \varepsilon_ {t},\tag{2}
$$

Figure 4. Time-Series Plots of Physicians’ Online Activities and Online Feedback  
(a)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/e789e3c36948ff925f573f4f62a6156f37d788b7875245a50393aef28fea4348.jpg)

(c)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/666914b9d2b8c446a083f726b1e844052c24be728c540f2173eb75c80fb49856.jpg)

or, equivalently,

$$
\mathbf {Y} _ {t} = B ^ {*} (L) \mathbf {Y} _ {t} + u _ {t}.\tag{3}
$$

In this case, ${ \boldsymbol { B } } ^ { * } = \Gamma ^ { - 1 } { \boldsymbol { B } } , u _ { t } = \Gamma ^ { - 1 } \varepsilon _ { t }$ . In a VAR system, each variable is regressed on the same set of determining variables. Therefore, the reduced VAR model can be estimated by ordinary least squares. Based on the estimation results from corresponding reduced VAR, the SVAR model can be estimated by a simple twostep maximum likelihood procedure (Hamilton 1994).

Despite the connections between SVAR and VAR, there are several fundamental differences between the two models. First, SVAR models formulate the true data-generating dynamics, whereas VAR models can capture only the sampling information from observed data. Second, without restrictions, different SVAR models may have the same reduced VAR form. For instance, if there exists a full rank matrix $\Gamma _ { 0 } ,$ the SVAR model is $\Gamma _ { 0 } \Gamma Y _ { t } = \Gamma _ { 0 } B ( L ) Y _ { t } + \Gamma _ { 0 } \varepsilon _ { t } ,$ , which also can be expressed as

$$
\Gamma^ {\prime} \mathbf {Y} _ {t} = B ^ {\prime} (L) \mathbf {Y} _ {t} + \varepsilon_ {t} ^ {\prime}.\tag{4}
$$

The model has the same reduced VAR form as model (1), where $\Gamma ^ { \prime } = \Gamma _ { 0 } \Gamma , B ^ { \prime } ( L ) = \Gamma _ { 0 } B ( L )$ , and $\varepsilon _ { t } ^ { \prime } = \Gamma _ { 0 } \varepsilon _ { t }$ . It is important to note that the identification of a SVAR model requires putting restrictions on the contemporaneous matrix Γ.

(b)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/1787b9f4b70502646ccb1ea106a64f60f1fdea425d41656cde531f2e3fa2f541.jpg)

(d)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/d8eadba3d649d9b6206cd615edda089906bdfdd90c73c55729e496ebed19bdce.jpg)

Whereas VAR models are commonly used for simulating system variations under policy shocks (expected or unexpected), SVAR models are used to find the underlying contemporaneous structures of unexpected shocks. Both SVAR and VAR are popular techniques in the field of applied econometrics to analyze complex dynamic systems that contain multiple time series (Kennedy 2003, Enders 2008). Because SVAR models emphasize the contemporaneous structure of unexpected shocks, a typical analysis method for a SVAR model is to simulate impulse response functions (IRFs). The IRF analysis addresses reverse causality by tracking the system responses under unexpected shocks. This technique is becoming increasingly popular in the domain of information systems, especially when analyzing dynamics within multivariate systems (Adomavicius et al. 2012; Luo et al. 2013, 2017).

Figure 5. Time-Series Plot of Physicians’ Offline Activities  
![](/api/attachments/8JAAZ7FJ/fulltext/images/eb86676f8a533468bc6e9120f6c61f193f843b2d800472025591c4518240f84b.jpg)

Table 1. Definition and Descriptive Statistics of the Data

<table><tr><td>Variable</td><td>Definition</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>NON</td><td>The total number of online consultations each month</td><td>307,123.60</td><td>178,760.10</td><td>78,129</td><td>846,578</td></tr><tr><td>NOA</td><td>The total number of online articles physicians post each month</td><td>7,054.85</td><td>1,948.45</td><td>4,404</td><td>12,126</td></tr><tr><td>NOF</td><td>The total number of nationwide offline visits each month</td><td>4,244.61</td><td>1,465.69</td><td>2,165.38</td><td>8,538.97</td></tr><tr><td>NOG</td><td>The total number of virtual gifts given to the physicians each month</td><td>8,914.07</td><td>10,666.56</td><td>0</td><td>40,926</td></tr><tr><td>NOR</td><td>The total number of patients&#x27; online reviews each month</td><td>12,577.06</td><td>12,263.72</td><td>678</td><td>56,616</td></tr></table>

## 4.2. Model Speci<sup>fi</sup>cation

Corresponding to the conceptual framework in Figure 1, we construct a five-equation, five-variable SVAR model. Whereas each of the three variables maps to a component in the behavior ecosystem, the feedback component is further split into two separate components because reviews represent physicians’ offline services and virtual gifts proxy physicians’ online services. In particular, we use the number of online consultations (NON) to measure physicians’ online professional services, the number of online articles (NOA) to measure physicians’ knowledge sharing behavior, and the number of offline visits (NOF) to measure physicians’ offline professional services; and feedback for physicians is depicted by the number of virtual gifts (NOG)—feedback for online services—and the number of reviews (NOR)—feedback for offline services. The SVAR model is able to formulate all of the potential interactions among these variables and thus allows us to investigate physicians’ behavior dynamics in the ecosystem systematically.

To address overdispersion issues (see the discussion in Section A2 of the online supplement), we use the logged values of all variables. We also include a set of exogenous variables to account for the system shocks during our observation window. Our model is defined as

$$
A \left[ \begin{array}{c} N O F _ {t} \\ N O R _ {t} \\ N O N _ {t} \\ N O G _ {t} \\ N O A _ {t} \end{array} \right] = \alpha + \sum_ {j = 1} ^ {K} B _ {j} \left[ \begin{array}{c} N O F _ {t - j} \\ N O R _ {t - j} \\ N O N _ {t - j} \\ N O G _ {t - j} \\ N O A _ {t - j} \end{array} \right] + C X + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \end{array} \right],\tag{5}
$$

where $N O F _ { t } , N O R _ { t } , N O N _ { t } , N O G _ { t } ,$ and $N O A _ { t }$ are the logged values of the number of offline visits, the number of online reviews, the number of online consultations, the number of virtual gifts, and the number of online articles shared in the time period t, respectively. The term α is a vector of constant terms. The matrix A captures the contemporaneous relationships in the system, with ones on the diagonal. Matrix B denotes the lagged effects of variables in the system. A set of exogenous variables is represented by X, including a linear time trend, a dummy variable that controls for flu season, and dummy variables that control for potential exogenous policy changes. There were three policy changes during our investigation window. The first is the implementation of the aforementioned “Internet plus Medical” policy initiated by the Chinese government in November 2015. The second and third ones are platform policy changes in February 2013 and April 2017, respectively. These platform policy changes are related to physicians’ online services on the focal platform and thus may exert exogenous shocks on the system. Controlling for these exogenous shocks allows us to eliminate the common trends that the external changes cause and to avoid spurious conclusions. We initially controlled for all three policy shocks, and the results showed that the two platform policy changes did not have significant effects on the online-offline ecosystem. Therefore, in our main analysis, we include only the dummy variable that controls for the medical policy change made by the Chinese government in November 2015; C contains the corresponding coefficients of the exogenous variables. Finally, $\varepsilon _ { i t } ( i = 1 , 2 , 3 , 4 , 5 )$ represents the structural innovations

## 4.3. Contemporaneous Constraint and Model Identi<sup>fi</sup>cation

According to the literature (Blanchard and Quah 1989, Gali 1999, Blanchard and Perotti 2002, Sims and Zha 2006, Moneta et al. 2011), one has to impose at least $n ( n - 1 ) / 2$ (n is the number of endogenous variables) restrictions on the contemporaneous matrix A to identify a SVAR system. Given our research context, we develop the contemporaneous matrix A as follows:

$$
A = \left[ \begin{array}{c c c c c} 1 & 0 & 0 & 0 & 0 \\ a _ {2 1} & 1 & 0 & 0 & 0 \\ a _ {3 1} & 0 & 1 & 0 & 0 \\ 0 & 0 & a _ {4 3} & 1 & 0 \\ a _ {5 1} & 0 & a _ {5 3} & 0 & 1 \end{array} \right].\tag{6}
$$

Specifically, we consider the first variable in the SVAR system, the number of offline visits (NOF), to be the most exogenous variable in the system because the offline clinical visits are due mainly to seasonal variations and the overall disease rate in the population. Furthermore, NOF is less likely to be affected by other variables in the systems in a contemporaneous manner. Therefore, we set the constraints that the corresponding elements $a _ { 1 2 } , a _ { 1 3 } , a _ { 1 4 } ,$ , and $a _ { 1 5 }$ be zeros.

The next exogenous variable in the system is the number of online reviews (NOR), which can change with the number of offline visits concurrently, as the more offline visits that physicians have, the more likely they are to be reviewed by patients. NOR cannot be affected contemporaneously by the number of online consultations, virtual gifts, and online articles because these activities cannot directly influence how patients write reviews about offline services. Therefore, we set zeros on elements $a _ { 2 3 } , a _ { 2 4 }$ , and $a _ { 2 5 }$ and left $a _ { 2 1 }$ to be estimated.

The third variable, the number of online consultations (NON), is assumed to be affected by concurrent offline visits. This is because physicians have a limited amount of time, and how much time they spend facilitating patients’ offline visits will affect the amount of time that they can spend on online consultations. We also assume that the number of online reviews, virtual gifts, and online articles will not have a contemporaneous impact on NON, as spontaneous demand from online users inherently drives online consultations. However, NON could be affected by the number of online reviews, virtual gifts, and online articles in the previous periods. That is, $a _ { 3 2 } , a _ { 3 4 }$ , and $a _ { 3 5 }$ are set to zeros, and $a _ { 3 1 }$ is left for estimation.

Fourth, the number of virtual gifts (NOG) can change with the number of online consultations contemporaneously—that is, the more online consultations that physicians contribute to, the more virtual gifts they may receive. NOG cannot be affected by other variables concurrently, as physicians can receive virtual gifts only through offering online consultations. As a result, we set zeros on $a _ { 4 1 } , a _ { 4 2 } ,$ and $a _ { 4 5 }$

Finally, we consider that the number of online articles (NOA) can be affected by the number of offline visits and online consultations. This assumption is supported by the observation illustrated by Figure 2:

Table 2. Lag Selection Criteria

<table><tr><td>Lag</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>FPE</td><td>0.0000</td><td>1.4e-06*</td><td>1.6e-06</td><td>1.6e-06</td><td>2.0e-06</td></tr><tr><td>AIC</td><td>3.3702</td><td>0.6828*</td><td>0.8120</td><td>0.7991</td><td>1.0093</td></tr><tr><td>HQIC</td><td>3.4266</td><td>1.0209*</td><td>1.4319</td><td>1.7008</td><td>2.1927</td></tr><tr><td>BIC</td><td>3.5101</td><td>1.5217*</td><td>2.3499</td><td>3.0361</td><td>3.9453</td></tr></table>

Note. The \* indicates the best lag under the lag-order selection criteria.

that physicians often write articles about their clinical experience as well as to answer patients’ frequently asked questions. Therefore, it is possible that the more physicians interact with patients through offline visits and online consultations, the more articles they tend to post online. In addition, we assume that NOA cannot be affected by the number of online reviews and virtual gifts contemporaneously. This assumption can be easily justified, as NOA is not directly related to patients’ feedback. Therefore, we set zero constraints on a<sub>52</sub> and $a _ { 5 4 }$ , whereas $a _ { 5 1 }$ and $a _ { 5 3 }$ need to be estimated.

In addition to the contemporaneous constraints, the modeling procedure of SVAR (Sims and Zha 2006, Enders 2008, Moneta et al. 2011) includes the following steps: (1) unit-root tests to determine the stationarity of variables, (2) cointegration tests to determine the existence of long-term equilibrium among nonstationary variables, and (3) lag order selection.

We first perform augmented Dickey–Fuller (ADF) tests to check for the stationarity of variables (Adomavicius et al. 2012, Bang et al. 2013, Thies et al. 2016). The stationarity of time series is a necessary assumption of a SVAR model. In an ADF test, the null hypothesis is that the time series contains a stochastic trend, and the alternative hypothesis is that the time series is stationary. The test statistics are reported in Section A3 of the online supplement. We found that the logged value of the number of online consultations (NON) is the only nonstationary time series. Therefore, we took the first difference in this variable to achieve stationarity. After this process, all the variables in the system are stationary. Because no combination of evolving variables shows evidence of cointegration, as shown in Section A4 of the online supplement, we proceed with estimating our model. More discussions about test results can be found in Sections A2–A7 of the online supplement.

From the above results, we then proceed to select a lag length K. The lag order is selected by the final prediction error (FPE), the Akaike information criterion (AIC), the Hannan and Quinn information criterion (HQIC), and the Bayesian information criterion (BIC) (Luo 2009, Adomavicius et al. 2012, Luo et al. 2013). As shown in Table 2, the optimal lag length is 1 (i.e., one month).

## 5. Empirical Approach and Findings

Different from standard empirical methods, the parameters estimated from SVAR models are not able to provide detailed information for the relationship among variables because of the inherently complicated dynamics (Sims 1980, Blanchard and Quah 1989). Therefore, the analysis and interpretations of a SVAR model typically rely on IRFs (Gottschalk 2001). In this section, we first provide a brief introduction to IRF analysis. Then, we derive IRFs from the estimated SVAR system to depict the impact across time. We present the robustness check results at the end.

## 5.1. IRF Framework and Its Interpretation

Complex interactions within endogenous systems such as VAR/SVAR can be analyzed through IRFs, which simulate the full chain of responses set in motion by an unexpected shock to the system. Specifically, IRFs trace the concurrent and subsequent responses in a system when there is an unexpected shock to the current value of the impulse variable (Stock and Watson 2001). This tracing is done by incorporating both the contemporaneous effects and the lagged effects between variables in a SVAR system. The subsequent system response can be seen as carryover effects as a result of the shock in the earlier period. By simulating IRFs, we are able to track the direction and duration of impacts over time.

In a system with more than two endogenous variables, the carryover effects revealed by IRFs can be the result of both direct and indirect influences. For example, for a system with three endogenous variables $y = \left( { { y } _ { 1 } } , \ { { y } _ { 2 } } , \ { { y } _ { 3 } } \right)$ , assume that $y _ { 1 t }$ and $y _ { 2 t - 1 } , y _ { 1 t }$ and y , and $y _ { 2 t }$ and y are correlated. Suppose that an unexpected shock occurs in variable y at time t. By the interdependencies that we assumed, we can derive that the response in variable $y _ { 1 }$ at time t 2 contains the direct effects of variable $y _ { 3 }$ as well as the indirect effects of variable $y _ { 3 }$ through variable y . In most practical settings, however, tracking such potential influence paths is almost infeasible because of the complex structure among endogenous variables. This is also the reason that econometricians do not interpret VAR/SVAR estimates directly but rely on IRFs instead. We provide further discussion on the IRF framework in Section A8 of the online supplement.

## 5.2. IRF Results

In this paper, we generate orthogonal IRFs (OIRFs) to examine the systematic dynamics in the estimated SVAR model. An OIRF is most appropriate when the terms of the residual series are instantaneously correlated (Sims 1980), which is the case in our study. Given that shocks are orthogonalized, we can derive the response of current and future values of variables to a shock equivalent to a one-standard-deviation (a unit) increase of an impulse variable (Stock and Watson 2001).

There are 25 possible IRFs for the estimated SVAR. Because our main focus is on the interactions between physicians’ online and offline activities, we report the four most relevant IRFs (Figure 6). Each plot in Figure 6 represents the tracking of the corresponding changes in the response variable across time, given a unit shock to the impulse variable at time zero. The remaining IRFs are reported and explained in the online supplement (Section A8). The length of the forecast horizon is chosen to be 12 months, and the significance level is 10%.

The first row of Figure 6 represents how physicians online activities affect their offline visits. Figure 6(a) shows that a unit shock to the number of online consultations (NON) can generate positive responses in the number of offline visits (NOF) and that such positive effects remain significant from months 2 to 6. This result indicates that physicians’ online professional services can increase their offline service quantities, which provides additional evidence for how in dividuals’ online professional strategies can affect offline responsibilities. Figure 6(b) shows that a unit shock to the number of online articles (NOA) can lead to more offline visits (NOF) during months 1–7. This result suggests that physicians’ knowledge-sharing behaviors can increase the number of offline services. This result is in keeping with theories that knowledge sharing in online professional communities can bring work or career-related benefits to offline channels For example, physicians can, through offering online consultations and sharing healthcare knowledge, help patients become more informed about their conditions and seek medical attention in a timely manner, thus leading to the positive effects of online activities on offline service.

The second row in Figure 6 represents how physicians’ offline visits affect their online activities. Figure 6(c) shows that a unit shock to offline visits (NOF) will lead to a decreased number of online consultations (NON) immediately, and this negative impact gradually diminishes and remains significant until month 2. This result confirms the resource-based theory that online services and offline services compete for physicians’ limited time and effort. In practice, the offline profession remains physicians’ main duty. Thus, the increased workload in offline channels can reduce physicians’ online professional services in the same period. The carryover effect can be explained tentatively by noting that physicians may form expectations about their offline workload and adjust their time allocation in advance. In other words, physicians may anticipate a high workload in the following months after seeing an increasing number of offline visits in the current period, and they may reduce their online services accordingly in the near future.

Figure 6. Physicians’ Online-Offline Behavior Dynamics (Impulse → Response)  
(a)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/d48a46aba189065fa10c696d68f3f27ebe91a7189aa21bb8e65a5cf3fda8a554.jpg)

(b)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/706f0b42d9cac3314cbd63377fb135b71da67a96856f484e72b2454114fa3f06.jpg)

(c)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/56a1757fbcbc3c23a051c9385cb787929d8a7794c6f47eab0d6730909668b9c4.jpg)

(d)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/7a8129725ef8013cdcbb723a150677dccf3958eefd7714704a4e0970e172ce5a.jpg)

By contrast, Figure 6(d) shows that a unit shock to the number of offline visits (NOF) can lead to an increase in the number of online articles (NOA). This positive effect is most salient at the beginning and gradually diminishes over time. This result suggests that physicians’ knowledge sharing behaviors can be triggered through offline service delivery. Indeed, physicians on the focal platform usually share their professional experiences and answer patients frequently asked questions in online articles. The more interactions with patients, the more servicerelated information physicians can share with the public and the more motivated physicians become to improve their services by sharing this information. Thus, this finding is consistent with those of prior studies: work-related concerns can serve as a motivational force for professionals’ knowledge sharing. In addition, we do not see a negative effect here, as in Figure 6(d), indicating that physicians’ online professional services and posting behaviors are different types of activities and follow different mechanisms. Summarizing knowledge into an online article involves less time and effort compared with online consultations. Thus, an increase in their offline workloads may not necessarily reduce physicians’ online article contributions.

In sum, these findings illustrate physicians’ onlineoffline behavior dynamics over time. Apart from these results, we also derive several interesting insights regarding patients’ feedback and interactions between physicians’ two types of online activities. For instance, we find that physicians’ offline visits, online consultations, and online articles are all positively related to the number of online reviews. These results suggest that although online reviews are designed for patients to express their opinions about the offline services they receive, whether patients write reviews for physicians may be affected by other factors. A detailed discussion is provided in Section A8 of the online supplement.

## 5.3. Robustness Checks

To ensure the robustness of our findings, we conduct additional analyses. First, we perform a robustness check on the ordering of the variables that are fed into

Figure 7. Robustness Check: Impulse Response Plots (Impulses → Responses)  
(a)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/c958b3c3ab7e5e8b67bd3cacc72db44ee9e468b636d41ce39a483334ae1ee82e.jpg)  
(b)

(c)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/f550343a0739b9b7bb8484d06e8d5560ec5abf24293a92f553134bb1c9381567.jpg)

As shown, most of the IRF results remain unchanged, except for those presented in Figure 7(a). It is suggested that online consultations lose their significant positive impact on offline visits under this new order of variables. Nevertheless, the positive impact of online articles remains positive and significant (Figure 7(b)). In addition, Figure 7(c) and (d) show that offline visits can negatively affect online consultations while positively affecting online articles. These findings are consistent with those in our main analysis. Additional analysis results with different the system. In the main analysis, we order the variables by their endogeneity level. It could be argued that there are potentially different orderings of these variables. Therefore, we consider several different permutations of the variables and reanalyze the SVAR system. One of the permutations that we consider is NOF, NOR, NOA, NON, and NOG. That is, we change the position of NOA to be in front of NON in the variable sequence. We consider this permutation because both NON and NOA measure physicians’ online activities, and their relative endogeneity levels may not be as obvious. Again, we conduct an IRF analysis under the newly estimated SVAR system. Figure 7 displays the four IRFs related to physicians’ onlineoffline behavior dynamics.

![](/api/attachments/8JAAZ7FJ/fulltext/images/700478f9b7b958bdfd5d6d5571d741da296c4da87d7767f69b9eb6e605ff2e8d.jpg)

(d)  
![](/api/attachments/8JAAZ7FJ/fulltext/images/ee270768d596fdbf6a477166f8844a8b53b2b373839469c1c759b343f81714c4.jpg)

permutations of SVAR are reported in Section A9.1 of the online supplement.

Second, in our main analysis, we included only online textual consultations as the measure for the NON variable. It is also possible that physicians could interact with patients online through telephone consultations. Hence, we calculate and construct a variable representing the number of telephone consultations (NTC) to rerun our analysis. By substituting NTC for NON in the SVAR, the IRF results provide evidence to support our main findings. We detail these findings in Section A9.2 of the online supplement.

In addition, we estimate a simultaneous equation system that corresponds to the SVAR model. Similar to a SVAR model, a SEM is a system of linear equations that represents the joint dependence of variables. However, SEMs and SVAR models differ in their approach to identification. As such, a comparison between the SEM and SVAR models is able to provide a robustness check of our SVAR results. The detailed model definition is provided in Section A9.3 of the online supplement.

Following a traditional identification approach, we identify this SEM system through three-stage least squares (3SLS), which uses lagged terms as instrumental variables to account for correlations and heteroskedasticity in the error terms (Pauwels and Weiss 2008). This identification strategy is not able to treat all of the variables as endogenous, so it may not capture the dynamic relationships in the system entirely. Thus, we compute and compare the $\check { R } ^ { 2 }$ and root mean squared errors (RMSEs) to evaluate the model performance. We find that the SVAR model has a higher $R ^ { 2 }$ and lower RMSEs than the corresponding SEM for each of the physicians’ behavioral series. The model comparison results are found in Table 3.

Table 3. Comparison of the Simultaneous Equation Model and the SVAR Model

<table><tr><td rowspan="2">Variable</td><td colspan="2">Simultaneous equation model</td><td colspan="2">SVAR model</td></tr><tr><td> $R^2$ </td><td>RMSE</td><td> $R^2$ </td><td>RMSE</td></tr><tr><td>NOF</td><td>0.5486</td><td>0.2086</td><td>0.8511</td><td>0.1261</td></tr><tr><td>NOR</td><td>0.6069</td><td>0.4761</td><td>0.6193</td><td>0.4933</td></tr><tr><td>NON</td><td>-55.1141</td><td>1.4127</td><td>0.3484</td><td>0.1607</td></tr><tr><td>NOG</td><td>0.6039</td><td>1.2498</td><td>0.8844</td><td>0.7110</td></tr><tr><td>NOA</td><td>0.6430</td><td>0.1552</td><td>0.7215</td><td>0.1444</td></tr></table>

In summary, all of these robustness checks indicate that our SVAR results are consistent. Detailed results of the model estimation are provided in Section A9 of the online supplement.

## 6. Discussion and Conclusion

Online healthcare platforms provide physicians with new channels through which to offer their medical services. Compared with offline meetings, online services allow physicians and patients to communicate frequently and in a timely manner. The unique features of online healthcare delivery generate an opportunity to address many issues that exist in the healthcare system but also create an equal amount of uncertainty for the existing offline healthcare system. Whereas research on telemedicine has explored various problems in regard to how online healthcare platforms can reduce healthcare resource disparities and improve diagnosis efficiency, there is little evidence of how physicians’ online and offline activities affect each other and, consequently, the healthcare system. Without such knowledge, hospitals and governments are concerned about whether it is appropriate for physicians to participate in online healthcare communities and whether their participation could lead to a decreased quantity or worse quality of offline medical services. We address these concerns in this study and examine how physicians’ online activities interact with offline health service, and vice versa. By studying physicians’ participation in both online and offline channels, we are able to investigate the social value of online healthcare platforms to healthcare systems because such activities build connections between online healthcare platforms and offline hospitals. This linkage also allows online healthcare platforms to have an impact on offline hospitals through physicians’ behavior dynamics, which can further shape the efficiency of healthcare systems.

To investigate physicians’ online-offline behavior dynamics, we develop a SVAR model that considers physicians’ online activities, physicians’ offline activities, and patients’ feedback as an endogenous ecosystem. In this behavior ecosystem, each component interacts with each other and exhibits serial dynamics. Following a standard analysis procedure for SVAR models, we conduct an IRF analysis to derive our findings. The results provide strong evi dence of the interdependence between physicians online and offline behaviors. First, we find that an increase in physicians’ online consultations or online articles can lead to more offline visits in the subsequent periods, providing insight that physicians online activities can lead to an increased service quantity in hospitals. Second, we find that an increase in physicians’ offline visits leads to a reduced number of online consultations, suggesting that the offline workload may reduce physicians’ availability to provide online services. Third, our results further reveal that an increase in physicians’ offline visits can lead to more articles shared online in the following months, indicating that their daily professional practice in offline channels triggers physicians’ knowledge sharing on online healthcare platforms. We also derive additional insights with regard to the dynamics of online feedback and the interdependencies between physicians’ two types of online activities. These results are robust for various system configurations and variable permutations.

To the best of our knowledge, this study is the first to investigate physicians’ online-offline behavior dynamics and shed light on the social significance of online healthcare platforms to the healthcare system. Physicians’ online participation not only facilitates the integration of online healthcare resources and offline healthcare systems but also provides new opportunities for online healthcare platforms to shape patients’ healthcare-seeking behaviors and, consequently, has an impact on healthcare delivery at offline hospitals. Moreover, our study contributes to the literature on online professional activities. Extending the extant literature that finds professionals can accumulate work or career-related gains from their interactions with peers in an online environment, our work shows that the level of their online participation and the particular activities in which they engage are shaped by their offline practice and workload.

Finally, our study has important practical implications. First, our results show that the number of online consultations positively affects the number of subsequent offline visits. This finding should lessen the concern that physicians’ participation in online healthcare platforms will negatively influence offline healthcare services. On the contrary, our results provide evidence that online healthcare platforms supplement offline services and can even encourage the use of these services. This finding can serve as support for the implementation of “Internet plus Medical” in China (China State Council 2015). Second, we show that physicians’ offline activities have a negative impact on the number of online consultations. This result indicates the need for the improvement of online-offline coordination and better system design, as the sustainability of online platforms, such as physician-patient healthcare communities in our study, requires a substantial number of physicians actively participating and contributing resources. Although our findings are derived from the Chinese healthcare system, they can be readily applied to similar healthcare environments, such as the medical system in Canada (AskTheDoctor.com) or the United States (e.g., HealthTap). Likewise, our findings are also applicable to a broader context in which individuals are able to conduct professional activities through both online and offline channels, such as open-source communities.

## Acknowledgments

The authors thank the department editor, the senior editor, the associate editor, and anonymous referees for their thoughtful suggestions throughout the review process. All mistakes are the authors’ own.

## References

Adomavicius G, Bockstedt J, Gupta A (2012) Modeling supply-side dynamics of IT components, products, and infrastructure: An empirical analysis using vector autoregression. Inform. System Res. 23(2):397–417.

Agarwal R, Gao GD, DesRoches C, Jha AK (2010) The digital transformation of healthcare: Current status and the road ahead. Inform. Systems Res. 21(4):796–809.

Ball MJ, Lillis J (2001) E-health: Transforming the physician/patient relationship. Internat. J. Medical Informatics 61(1):1–10.

Bang Y, Lee D-J, Han K, Hwang M, Ahn J-H (2013) Channel capabilities, product characteristics, and the impacts of mobile channel introduction. J. Management Inform. Systems 30(2): 101–126.

Blanchard O, Perotti R (2002) An empirical characterization of the dynamic effects of changes in government spending and taxes on output. Quart. J. Econom. 117(4):1329–1368.

Blanchard OJ, Quah D (1989) The dynamic effects of aggregate demand and supply disturbances. Amer. Econom. Rev. 79(4): 655–673.

Bock G-W, Zmud RW, Kim Y-G, Lee J-N (2005) Behavioral intention formation in knowledge sharing: Examining the roles of extrinsic motivators, social-psychological forces, and organizational cli mate. MIS Quart. 29(1):87–111.

Butler BS (2001) Membership size, communication activity, and sustainability: A resource-based model of online social structures. Inform. Systems Res. 12(4):346–362.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

China State Council (2015) Guiding opinions of the state council on actively promoting the action of “Internet plus.” (In Chinese.) Accessed January 20, 2016, http://www.gov.cn/zhengce/content 2015-07/04/content\_10002.htm.

Coelho JJ, Arnold A, Nayler J, Tischkowitz M, MacKay J (2005) An assessment of the efficacy of cancer genetic counselling using real-time videoconferencing technology (telemedicine) compared with face-to-face consultations. Eur. J. Cancer Care 41(15): 2257–2261.

Cooper AA, Humphreys KR (2008) The uncertainty is killing me: Self triage decision making and information availability. Sensoria 4(1):1–6.

Das A, Faxvaag A, Svanæs D (2015) The impact of an eHealth portal on healthcare professionals’ interaction with patients: Qualita tive study. J. Medical Internet Res. 17(11):1–10.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407-1424

Detz A, Lopez A, Sarkar U (2013) Long-term doctor-patient re- ´ lationships: Patient perspective from online reviews. J. Medical Internet Res. 15(7):e131.

Dugdale DC, Epstein R, Pantilat SZ (1999) Time and the patientphysician relationship. J. General Internal Medicine 14(Suppl 1): S34–S40.

Eijk ES, Busschbach JJ, Monteban H, Timman R, Wefers Bettink-Remeijer M (2014) Toward patient self-triage in the ophthalmic emergency department: Sensitivity and specificity of a self-triage instrument. Acta Ophthalmol. 92(7):697–700.

Emmert M, Meszmer N, Sander U (2016) Do healthcare providers use online patient ratings to improve the quality of care? Results from an online-based cross-sectional study. J. Medical Interne Res. 18(9):e254.

Enders W (2008) Applied Econometric Time Series (John Wiley & Sons, New York).

Eysenbach G (2000) Recent advances: Consumer health informatics BMJ 320(7251):1713–1716.

Eysenbach G (2008) Medicine 2.0: Social networking, collaboration, participation, apomediation, and openness. J. Medical Interne Res. 10(3):e22.

Farnan JM, Sulmasy LS, Worster BK, Chaudhry HJ, Rhyne JA, Arora VM (2013) Online medical professionalism: Patient and public relationships: Policy statement from the American College of Physicians and the Federation of State Medical Boards. Ann. Internal Medicine 158(8):620–627.

Fichman RG, Kohli R, Krishnan R (2011) The role of information systems in healthcare: Current research and future trends. Inform. Systems Res. 22(3):419–428.

Gali J (1999) Technology, employment, and the business cycle: Do technology shocks explain aggregate fluctuations? Amer. Econom. Rev. 89(1):249–271.

Gao GG, McCullough JS, Agarwal R, Jha AK (2012) A changing landscape of physician quality reporting: Analysis of patients online ratings of their physicians over a 5-year period. J. Medica Internet Res. 14(1):e38.

Goh JM, Gao G, Agarwal R (2011) Evolving work routines: Adaptive routinization of information technology in healthcare. Inform. Systems Res. 22(3):565–585.

Goh JM, Gao G, Agarwal R (2016) The creation of social value: Can an online health community reduce rural–urban health disparities? MIS Quart. 40(1):247–263.

Goh K-Y, Heng C-S, Lin Z (2013) Social media brand community and consumer behavior: Quantifying the relative impact of user-and marketer-generated content. Inform. Systems Res. 24(1):88–107.

Goldzweig CL, Towfigh A, Maglione M, Shekelle PG (2009) Costs and benefits of health information technology: New trends from the literature. Health Affairs (Millwood) 28(2):w282–w293.

Gottschalk J (2001) An introduction into the SVAR methodology: Identification, interpretation and limitations of SVAR models. Working paper, Kiel Institute for the World Economy, Kiel, Germany.

Griffiths F, Lindenmeyer A, Powell J, Lowe P, Thorogood M (2006) Why are healthcare interventions delivered over the internet? A systematic review of the published literature. J. Medical Internet Res. 8(2):e10.

Hall H (2001) Input-friendliness: Motivating knowledge sharing across intranets. J. Inform. Sci. 27(3):139–146.

Hamilton JD (1994) Time Series Analysis (Princeton University Press, Princeton, NJ).

Hara N, Foon Hew K (2007) Knowledge-sharing in an online com munity of health-care professionals. Inform. Tech. People 20(3): 235–261.

Hawn C (2009) Take two aspirin and tweet me in the morning: How Twitter, Facebook, and other social media are reshaping health care. Health Affairs (Millwood) 28(2):361–368.

Hewitt-Taylor J, Bond CS (2012) What e-patients want from the doctor-patient relationship: Content analysis of posts on dis cussion boards. J. Medical Internet Res. 14(6):e155.

Horne R, Weinman J (1999) Patients’ beliefs about prescribed medicines and their role in adherence to treatment in chronic physica illness. J. Psychosomatic Res. 47(6):555–567.

Hsu M-H, Ju TL, Yen C-H, Chang C-M (2007) Knowledge sharing behavior in virtual communities: The relationship between trust, self-efficacy, and outcome expectations. Internat. J. Human-Comput. Stud. 65(2):153–169.

Huang Y, Singh PV, Ghose A (2015) A structural model of employee behavioral dynamics in enterprise social media. Management Sci. 61(12):2825–2844

Hwang E, Guo X, Tan Y, Dang Y (2017) Rebalancing geographic healthcare disparity through telemedicine consultations. Working paper, University of Washington, Seattle.

Hwang EH, Singh PV, Argote L (2015) Knowledge sharing in online communities: Learning to cross geographic and hierarchical boundaries. Organ. Sci. 26(6):1593–1611.

Iyengar R, Van den Bulte C, Valente TW (2011) Opinion leadership and social contagion in new product diffusion. Marketing Sci. 30(2):195–212.

Kallinikos J, Tempini N (2014) Patient data as medical facts: Social media practices as a foundation for medical knowledge creation. Inform. Systems Res. 25(4):817–833.

Kaplan SH, Greenfield S, Ware JE Jr (1989) Assessing the effects of physician-patient interactions on the outcomes of chronic disease. Medical Care 27(3 Suppl):S110–S127.

Kennedy P (2003) A Guide to Econometrics (MIT Press, Cambridge, MA).

Kilian L (2013) Structural vector autoregressions. Hashimzade N, Thornton MA, eds. Handbook of Research Methods and Applications in Empirical Macroeconomics (Edward Elgar Publishing, Cam berley, UK), 515–554.

Lerner J, Tirole J (2002) Some simple economics of open source. J. Indust. Econom. 50(2):197–234.

Li J, Zhang Y, Ma L, Liu X (2016) The impact of the internet on health consultation market concentration: An econometric analysis of secondary data. J. Medical Internet Res. 18(10):e276.

Lin M-JJ, Hung S-W, Chen C-J (2009) Fostering the determinants of knowledge sharing in professional virtual communities. Comput. Human Behav. 25(4):929–939.

Lu Y, Jerath K, Singh PV (2013) The emergence of opinion leaders in a networked online community: A dyadic model with time dynamics and a heuristic for fast estimation. Management Sci. 59(8): 1783–1799.

Luo X (2009) Quantifying the long-term impact of negative word of mouth on cash flows and stock prices. Marketing Sci. 28(1): 148–165.

Luo X, Zhang J, Duan W (2013) Social media and firm equity value Inform. Systems Res. 24(1):146–163.

Luo X, Gu B, Zhang J, Phang CW (2017) Expert blogs and consume perceptions of competing brands. Management Inform. System Quart. 41(2):371–395

Mettler M, Kemper DW (2003) Information therapy: Health education one person at a time. Health Promotion Practice 4(3):214–217.

Miranda SM, Saunders CS (2003) The social construction of meaning: An alternative perspective on information sharing. Inform. Systems Res. 14(1):87–106.

Moneta A, Chlaß N, Entner D, Hoyer P (2011) Causal search in structural vector autoregressive models. Florin P, Guyon I, eds. Proc. Machine Learn. Res. (PMLR), 95–114.

Muñoz RF (2010) Using evidence-based internet interventions to reduce health disparities worldwide. J. Medical Internet Res. 12(5): e60.

National Health Commission (2017) Monthly national medical services survey. (In Chinese). Accessed January 15, 2018, http:/ www.nhc.gov.cn/mohwsbwstjxxzx/s2906/new\_list.shtml.

Nonaka I (1994) A dynamic theory of organizational knowledge creation. Organ. Sci. 5(1):14–37.

Nonaka I, Takeuchi H (1995) The Knowledge Creation Company: How Japanese Companies Create the Dynamics of Innovation (Oxford University Press, New York).

Okike K, Peter-Bibb TK, Xie KC, Okike ON (2016) Association between physician online rating and quality of care. J. Medical Internet Res. 18(12):e324.

Pauwels K, Weiss A (2008) Moving from free to fee: How online firms market to change their business model successfully. J. Marketing 72(3):14–31.

Raghupathi W, Raghupathi V (2014) Big data analytics in healthcare: Promise and potential. Health Inform. Sci. Systems 2(1):3–12.

Roberts JA, Hann I-H, Slaughter SA (2006) Understanding the mo tivations, participation, and performance of open source soft ware developers: A longitudinal study of the apache projects. Management Sci. 52(7):984–999

Roettl J, Bidmon S, Terlutter R (2016) What predicts patients’ will ingness to undergo online treatment and pay for online treatment? Results from a web-based survey to investigate the changing patient-physician relationship. J. Medical Internet Res. 18(2):e32.

Santana S, Lausen B, Bujnowska-Fedak M, Chronaki C, Kummervold PE, Rasmussen J, Sorensen T (2010) Online communication be tween doctors and patients in Europe: Status and perspectives. J. Medical Internet Res. 12(2):e20.

Shah SK (2006) Motivation, governance, and the viability of hybrid forms in open source software development. Management Sci. 52(7):1000–1014.

Sharratt M, Usoro A (2003) Understanding knowledge-sharing in online communities of practice. Electronic J. Knowledge Management 1(2):187–196.

Sims CA (1980) Macroeconomics and reality. Econometrica 48(1):1–48.

Sims CA, Zha T (2006) Does monetary policy generate recessions? Macroeconom. Dynam. 10(2):231–272

Singh PV, Tan Y, Mookerjee V (2011a) Network effects: The influence of structural capital on open source project success. MIS Quart. 35(4):813–829.

Singh PV, Tan Y, Youn N (2011b) A hidden Markov model of de veloper learning dynamics in open source software projects. Inform. Systems Res. 22(4):790–807.

Spender JC, Grant RM (1996) Knowledge and the firm: Overview. Strategic Management J. 17(S2):5–9.

Stewart T, Ruckdeschel C (1998) Intellectual capital: The new wealth of organizations. Performance Improvement 37(7):56–59.

Stock JH, Watson MW (2001) Vector autoregressions. J. Econom. Perspect. 15(4):101–115.

Tate DF, Finkelstein EA, Khavjou O, Gustafson A (2009) Cost ef fectiveness of internet interventions: Review and recommendations. Ann. Behav. Medicine 38(1):40–45.

Thies F, Wessel M, Benlian A (2016) Effects of social interaction dy namics on platforms. J. Management Inform. Systems 33(3):843–873.

Tieu L, Sarkar U, Schillinger D, Ralston JD, Ratanawongsa N, Pasick R, Lyles CR (2015) Barriers and facilitators to online portal use

among patients and caregivers in a safety net healthcare system: A qualitative study. J. Medical Internet Res. 17(12):e275.

Wenger EC, Snyder WM (2000) Communities of practice: The organizational frontier. Harvard Bus. Rev. 78(1):139–146.

Yan L, Tan Y (2017) The consensus effect in online health-care communities. J. Management Inform. Systems 34(1):11–39

Yan L, Yan X, Tan Y, Sun SX (2019) Shared minds: How patients use collaborative information sharing via social media platforms. Production Oper. Management 28(1):9–26.
