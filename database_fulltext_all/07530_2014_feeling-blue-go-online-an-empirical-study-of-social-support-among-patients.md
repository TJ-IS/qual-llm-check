---
otero_id: 7530
otero_key: "TNPSHYBP"
title: "Feeling Blue? Go Online: An Empirical Study of Social Support Among Patients"
authors: "Lu Yan; Yong Tan"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0538"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.2.19.100] On: 01 February 2015, At: 06:36 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/TNPSHYBP/fulltext/images/bfce1a100f3eefb2d8b3ec38ba0ad5c3209087b8ad0de0c719a3f75ab442fcb4.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Feeling Blue? Go Online: An Empirical Study of Social Support Among Patients

Lu Yan, Yong Tan

## To cite this article:

Lu Yan, Yong Tan (2014) Feeling Blue? Go Online: An Empirical Study of Social Support Among Patients. Information Systems Research 25(4):690-709. http://dx.doi.org/10.1287/isre.2014.0538

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/TNPSHYBP/fulltext/images/2b0704ec1525f4d6646106f30243de8bff38e607f4f9ecac81e16f00f883e4ed.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Feeling Blue? Go Online: An Empirical Study of Social Support Among Patients

Lu Yan

Department of Operations and Decision Technologies, Kelley School of Business, Indiana University, Bloomington, Indiana 47405, yanlucy@indiana.edu

Yong Tan

Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195, ytan@uw.edu

n this paper, we investigate whether social support exchanged in an online healthcare community bene-Ifits patients’ mental health. We propose a nonhomogeneous Partially Observed Markov Decision Process (POMDP) model to examine the latent health outcomes for online health community members. The transition between different health states is modeled as a probability function that incorporates different forms of social support that patients exchange via discussion board posts. We find that patients benefit from learning from others and that their participation in the online community helps them to improve their health and to better engage in their disease self-management process. Our results also reveal differences in the influence of various forms of social support exchanged on the evolution of patients’ health conditions. We find evidence that informational support is the most prevalent type in the online healthcare community. Nevertheless, emotional support plays the most significant role in helping patients move to a healthier state. Overall, the influence of social support is found to vary depending on patients’ health conditions. Finally, we demonstrate that our proposed POMDP model can provide accurate predictions for patients’ health states and can be used to recover missing or unavailable information on patients’ health conditions.

Keywords: healthcare; social networks; social support; partially observed Markov decision process; user-generated content

History: Robert Fichman, Senior Editor; Ravi Bapna, Associate Editor. This paper was received on February 21, 2011, and was with the authors 21 months for 4 revisions. Published online in Articles in Advance October 28, 2014.

## 1. Introduction

The Internet is changing the way that people learn about health and illness (Ziebland et al. 2004). According to the Pew Research Center, 61% of Americans sought health information online in 2008, an increase of 25% from 2000 (Fox and Jones 2009). In 2010, 59% of American adults who used the Internet to research health problems constituted 80% of Internet users (Fox 2011). The Internet’s features, such as its costefficient reach to a vast audience, 24/7 accessibility, and user anonymity make it a venue to which people can turn for social support at any time. Disease sufferers do not need to be spatially and temporally co-present when they use the Internet, which can provide a means to access nonthreatening and supportive communication (Coulson 2005).

The intersection of healthcare and the Internet provides enormous potential for facilitating health services and, perhaps more important, for the development of mental health programs that would be accessible to many who do not or cannot seek professional treatment (Christensen and Griffiths 2000). Mental health is defined as an individual’s ability to respond to the many, varied experiences of life with flexibility and a sense of purpose (Oluwole et al. 2011). People with serious mental problems have difficulty balancing their lives, those of other people, and the surrounding environment. According to the National Institute of Mental Health (NIMH), there were 33,000 suicides in the United States in 2006; more than 90% of those individuals had been diagnosed with a mental disorder.

Much research over the past few decades indicates that the level of social support in people’s lives affects their physical and mental health conditions (Clark 2006). People with chronic illnesses, especially mental problems, however, may find it difficult to develop and maintain relationships in the “real world” (Leung 2011). As a result, many individuals with chronic illnesses report spending the majority of their time alone and, as a result, experience feelings of social isolation or loneliness (McCorkle et al. 2008). Nevertheless, many of these same individuals find online social interactions attractive and effective for obtaining much needed emotional support and companionship (Leung 2011). In view of this, online health communities and health social networking are booming (Agarwal et al. 2010) and can be considered an emerging patient-driven healthcare model.

Despite the increasingly important role of online health communities, how helpful this patient-driven healthcare model is for patients is largely unknown (Lamberg 2003). To our knowledge, little research has systematically examined how the social influence of patient participation in online healthcare communities and the sharing of disease information affects patients’ health conditions. Thus, the objective of this study is to examine the impact of patients’ activities in online social networks on their health conditions. In particular, we examine how the amount of social support exchanged<sup>1</sup> (as measured by the number of forum posts made by an individual) affects a patient’s health condition (a latent construct measured by a three-level variable, i.e., an aggregate of factors such as current mood, distress level, and detailed distress components).

The challenge of studying this problem is the difficulty of measuring perceived utility through patients’ online behaviors in online healthcare communities, especially when patients’ health conditions are largely unobservable. To overcome this obstacle, we propose a Partially Observed Markov Decision Process (POMDP) model, whereby a patient’s health condition is partially observed and is assumed to vary over time. The transition between different health condition states is determined by a set of covariates on the benefits that patients receive from their activities in an online healthcare community. The number of health condition states is selected so as to best fit the data of patients’ online behavior. To control for individualspecific characteristics, we include a set of randomeffect coefficients that capture this unobserved heterogeneity. Finally, we conduct a maximum likelihood estimation procedure for this POMDP model.

The POMDP model that we propose identifies dynamic changes in health conditions according to patients’ online activities and provides evidence for the benefits of online healthcare communities. Through incorporating partially observed patients’ health conditions as a means of examining (latent) dynamic changes, we find that patients give and receive various forms of social support through their online activities and that participation in discussion board activity has a positive impact on their health conditions. Although information is the major type of social support that patients exchange in online healthcare communities, emotional support has a higher magnitude of influence in helping patients improve their health condition.

To our knowledge, this is the first study to focus on online healthcare communities, whereby patients share their medical histories and health information to help one another. We investigate how patients’ social interactions affect their health conditions. Our work bridges the social networking and healthcare fields and offers the following contributions. First, we study patients with chronic mental health problems and their online activities. We find quantitative evidence that online healthcare communities help patients to better cope with their diseases. Users who directly participate in social support exchanges experience support in various forms, such as receiving information about their condition or the knowledge that others are experiencing similar stressful situations. Social support helps them to stop blaming themselves for their illness and presents them with opportunities to actively engage in mutual aid and self-assistance. Our findings on the effectiveness of informational support suggest that an online healthcare community acts as a health repository with a massive library of health knowledge data and a visual networking tool. Patients who are managing their disease and understand its progression are a tremendous resource for other patients who suffer from similar problems. For rarer conditions, in particular, online health networking might be the only means for patients to interact with other, similar sufferers, who are likely to be geographically scattered. Second, the proposed POMDP model can help to recover patients’ missing or unavailable information. It takes time and effort for patients to keep track of their health condition. Some patients may not even take the opportunity to get their health condition assessed. Under such conditions, our work postulates a way to effectively and accurately reveal the unobservable information. Practically, this model provides a cost-free and nonintrusive diagnostic tool to infer a patient’s health condition from observable online behavior.

The rest of the paper is organized as follows. In §2, we review the literature and develop the theoretical framework. In §3, we present the research context of online health social networking and online health data. The empirical model is presented in §4. We explain the data set and key variables in §5, and present the results in §6. In §7, we provide further discussion on the model and analyses. Section 8 provides concluding remarks, implications of our study, and discussion of future avenues for research.

## 2. Theory and Hypotheses

This study is set in the context of the emerging literature on health social networking and patientdriven healthcare models. Social capital, the resources embedded in social networks, is widely believed to influence health (Abbott and Freeth 2008). It is believed that social media are well suited for the healthcare domain and represent a promising arena for improving healthcare effectiveness (Fichman et al. 2011). As such, we have observed the emergence of many healthcare-related social networking websites that have, over the years, evolved to virtual platforms to bring together patients with shared interests to communicate with and help each other (Swan 2009).

Following Merton’s (1976) description of the role of the “good doctor,” Radley and Billig (1996) advocated that a “good patient” must be more than a patient to receive this entitlement. For this reason, internal attitude plays an important role in defining patients’ health conditions. Many of those who join online healthcare communities are active in their selfcare process. An online healthcare community provides opportunities to gain support within a virtual network of individuals who are dealing with similar issues. Different from the widely used, email-based type of support group, an online healthcare community offers significant advantages, such as access to a voluminous amount of data (the aggregated knowledge generated by members) and live online discussions. These modern social media-based communities are constructed on a commons-based, peer production basis (Benkler 2002, Fichman et al. 2011) and are especially attractive to individuals with rare diseases or chronic health problems. For many who participate in online healthcare communities, the platform supplements traditional offline support methods. For others, the online venues may be the only social support available.

## 2.1. Types of Social Support

Social support is an exchange of resources between at least two individuals (Shumaker and Brownell 1984). Therefore, it reflects both the support that a person gives and the support they receive. A positive relationship between health and social support has long been recognized (Langford et al. 1997). Social support is one of the most important predictors of overall physical health (Chernomas and Clarke 2010, Clark 2006). Cobb (1976) explained that supportive interactions protect against the health consequences of stress. McCorkle et al. (2008) found that social support increases adherence to treatments and enhances recovery. Based on these findings, researchers across disciplines have been studying the social support in various scenarios. Today, a major body of sociology research categorizes social support in four forms: informational support, emotional support, companionship, and instrumental assistance (Berkman et al. 2000, Wortman and Conway 1985). Our hypotheses focus on the effects of different types of social support (informational, emotional, and companionship) on health conditions.

2.1.1. Informational Support. Informational support involves the transmission of information, including advice and referrals. The vast amount of information on health-related topics makes such topics among the most popular searches on the Internet (McMullan 2006). In particular, the Internet is a source for mental health information for over 10% of the general population and for over 20% of those who have a history of mental health problems (Powell and Clarke 2006). A significant amount of research also shows the extensive use of online healthcare communities. Members of online healthcare communities create health profiles or blogs to share geographic and demographic information, such as age and gender, and to track the effects of various medical treatments. Online health profiles help patients to conveniently keep track of their treatment progress and medications, thus freeing them from sorting through huge piles of test results and other paperwork. This, in turn, simplifies medical interpretation and fosters a better understanding of their conditions and attendant treatment decisions (McMullan 2006).

Bandura (2004, p. 144) constructed a theoretical framework based on social cognitive theory to examine health promotion. This theory “specifies a core set of determinants, the mechanism through which they work, and the optimal ways of translating this knowledge into effective health practices.” One of its core determinants is knowledge of health risks and benefits, which creates the precondition for a change in individual health behaviors. Access to shared health information, medical experiences, and treatment history in online healthcare communities can produce more informed patients. The knowledge gained from informational support exchanges can help provide a greater understanding of problems and possible solutions. The more health information that patients obtain, the better they understand their condition and the better they can take steps to care for themselves (Kassirer 2000, McMullan 2006, Wanless 2002). Gaining experiential information from other patients’ profiles benefits an individual in many ways. For instance, it provides the patient with other’s second opinions, enables her to get information that is “difficult” to ask directly, and assists her in making sense of the stage of the disease (Ziebland et al. 2004). All of these make the Internet and online healthcare communities an attractive resource for information about new treatments.

In our research context, patients participate in ongoing discussions via the public discussion forum of an online healthcare community to exchange social support. As such, social support reflects both the support that a patient gives and the support received. Because of the limitations of our data, we cannot discern the support offered from that which was sought or received. Therefore, we measure the support experienced from both receiving and offering activities. While the health effect of receiving support is more or less expected, the effect of giving support is less obvious. We argue, however, that seeking or giving support helps a patient to experience better health. The act of seeking or giving support immediately triggers opportunities to receive support, and so can be viewed as a proxy measure of support received. This is self-evident in the case of seeking support; often the first step in getting support is seeking it. In particular, by seeking informational support, patients express an active rather than a passive attitude when facing their health problems. For patients who give informational support, the helping and sharing process not only offers the opportunity to help others but also provides an occasion for them to learn new things. During communication and social support exchange, those who give information will often receive it as well, either immediately or in the future. We have observed that many posts initiated to obtain information for particular cases often lead to broader discussions and more informational support. Patients may also receive implicit informational support through reading others’ posts before replying.

All of these are anecdotes of reciprocity in social support, which has been extensively examined in the literature (Antonucci and Jackson 1990). Putnam (1993, p. 172) defined generalized reciprocity as $\mathbf { \check { a } }$ continuing relationship of exchange that is at any given time unrequited or imbalanced, but that involves mutual expectations that a benefit granted now should be repaid in the future.” This means that, by helping others, you help yourself in the long run. In short, what goes around comes around. Jung (1990) examined three aspects of social support: amount received, amount given, and reciprocity in relationship to coping with stress. Reciprocity was found to have a stronger relationship with reduced symptoms than the amount of social support that was received or provided. Jou and Fukada (2002) developed a questionnaire to measure the support provided for, requested by, requested of, and received from, others and then constructed a measure for reciprocity of support. They found that the health of participants in reciprocal relationships is better than that of participants in nonreciprocal relationships.

Whereas the social reciprocity literature provides the rationale that giving support can help patients improve their health conditions, our argument is also supported by the concept of altruism and its relationship to health. Researchers have suggested that altruistic (other-centered) emotions and behaviors are associated with greater well-being, health, happiness, and longevity (Post 2005). According to Midlarsky (1991), altruism results in deeper social integration, distraction from personal problems, enhanced meaningfulness, increased perception of self-efficacy and competence, and improved mood or a more physically active lifestyle and, hence, leads to better mental and physical health. Therefore, “it’s good to be good.” This notion is supported by empirical evidence. For example, Schwartz et al. (2003) investigated altruistic social behaviors, such as helping others, among more than 2,000 members of the Presbyterian Church throughout the United States. They found that both helping others and receiving help were associated with better mental health. However, giving help was associated with higher levels of mental health, above and beyond the benefits of receiving help.

<sup>Hypothesis</sup> <sup>1.</sup> Informational support given and received in online healthcare communities has a positive effect on patients’ health conditions.

2.1.2. Emotional Support. Emotional support comes in the form of sharing happiness or sadness or of expressing caring and concern. It sends a signal that one is not alone, that one is taken care of and valued. This kind of support is especially important for patients with chronic mental problems. First, patients with mental health issues have difficulty in developing and maintaining relationships as a means to receive meaningful help. At different stages, the disease can inhibit the ability of patients to cope with their illness. Family relationships can become strained and support withdrawn due to the various burdens that stem from the disease (Weinberg et al. 1995, Wright 2000). Second, due to the limits of time and resources, it may be difficult for offline relations to provide support when it is needed. However, with no geographic boundaries, online healthcare communities make it possible for patients to talk with other patients who suffer from similar illnesses at any time (Bambina 2007, Lamberg 2003). Third, and most important, knowing that others have faced a similar problem, and even have overcome it, can provide both relief from personal blame and renewed strength (Bambina 2007, Weiss 1974, Wills 1985). Research has shown that online healthcare community members often develop intimate and trusting relationships; among other things, they provide referrals and encourage each other to continue with therapy (Lamberg 2003).

As noted in the earlier discussion about informational support, patients benefit from both giving and receiving support. The same applies to emotional support. We have observed that many who post emotionally supportive words often receive supportive messages immediately in return from other participants of the thread. In addition to explicit emotional support exchanges, patients, before replying to a post with a supportive message, “read the entire thread,” got the sense of “I am not alone,” and experienced implicit emotional support (Swan 2009).

<sup>Hypothesis</sup> <sup>2.</sup> Emotional support given and received in online healthcare communities has a positive effect on patients’ health conditions.

2.1.3. Companionship. Companionship can consist of group meetings, chatting, and other social activities. It provides support by making individuals feel that there are others who enjoy their presence and that they are a valuable part of something bigger than themselves (Wellman and Wortley 1990). In an online healthcare community, such support is usually exchanged by participating in a discussion forum. The various activities in online healthcare communities act as “talk” therapy and can make people feel that they are not isolated from the world and have social connections. Finally, instrumental or practical support refers to assistance in finding life-related resources. This kind of support is usually not available in online healthcare community settings, as it requires that individuals reveal their real-life identity. In this study, social support is classified as informational, emotional, or companionship. Their respective effects cannot be empirically identified simultaneously. We have selected companionship as the base category; thus, the effects of informational or emotional support are relative to that of companionship.

## 2.2. Social Support as a Process

While it is important to differentiate the types of social support, Jacobson (1986) pointed out that the “timing” or sequence of social support can affect its effectiveness. A medical problem may need different types of support as it moves through its disease stages (Pearlin 1985). This calls for social support to be examined as a dynamic process rather than just a resource or outcome (King et al. 2006). This perspective is supported by prior studies that emphasized the importance of social-exchange processes in social support (Antonucci and Jackson 1990). In the context of this study, this dynamic process is characterized by a patient’s changing her health conditions over time.

Cohen and Wills (1985) have proposed two models, the direct-effect and stress-buffering model, to explain the influence of social support on stress and health. The direct-effect model asserts that social support protects health, irrespective of whether stress is present. However, according to the stress-buffering model, social support is less effective, or relatively unimportant, for patients who experience low levels of stress. While our Hypotheses 1 and 2 support the direct-effect model, the stress-buffering model and the process view of social support suggest that the helpfulness of social support may vary depending on patients’ current health conditions.

<sup>Hypothesis</sup> <sup>3.</sup> The effect of social support in online healthcare communities is moderated by patients’ health conditions.

## 2.3. Antecedents of Social Support

A social network is the vehicle through which social support, for example, the “give and take” of helpfulness and protections, is provided (Langford et al. 1997). In the context of an online healthcare community, the network is the structure of an interactive process that allows patients to share and research information, seek help, make treatment decisions, construct social connections, and find alternative therapies for advocacy, escape, and prevention (Greco et al. 2001, Ziebland et al. 2004).

The virtual relationships that are developed in a virtual community play an important role in meeting patients’ social needs (Leung 2011). Online health social networking has taken on aspects of crowdsourcing in that it allows individuals to observe and react to information provided by others, especially in regard to learning how to interpret data. The shared medical information, practical tips, and online advice help patients to develop quasi-professional knowledge of their health conditions (Griffiths et al. 2012). The collective learning and experience of others can be leveraged and is particularly related to health conditions (Swan 2009). The opportunity to display familiarity with a remarkable body of medical and experiential knowledge about the illness enables a patient to gain a modicum of competence and social fitness in the face of serious health problems (Ziebland et al. 2004). In addition to this enhanced competence, the increased connectedness to others in the healthcare community also changes the patient’s relationship with illness. Some degree of connectedness in the network indicates a patient’s social embeddedness and how support is derived from the environment. Research has shown that, with strong social embeddedness, even those who are experiencing difficulties do not suffer to the same extent as those who are more isolated (Berkman and Breslow 1984).

<sup>Hypothesis</sup> <sup>4.</sup> Social embeddedness and social competence in online healthcare communities illustrate the depth and strength of social support and thus have a positive effect on patients’ health conditions.

Figure 1 shows the conceptual framework whereby social support influences patients’ health conditions, and that there is a moderating effect. It is theorized that patients’ health conditions consequently affect their online activities and moderate other control variables.

## 3. Research Context

In this paper, we focus on a Health 2.0 website that is primarily directed toward patients and which provides a means for them to interact with each other. This communication platform offers patients an opportunity to find others in similar health situations and to share information about conditions, symptoms, treatments, and other needs. The key benefits thus include the provision of a more comprehensive look at a patient’s health condition.

Figure 1 Conceptual Framework  
![](/api/attachments/TNPSHYBP/fulltext/images/c7ca90bdd9a56f75d35c4a70bf7eeda6ae3893bcf3edaa05637cde44bbcf0c1b.jpg)

## 3.1. Data Description

Like other social network websites, this virtual site provides registration forms for patients to share their medical history and disease details as well as communication platforms. To provide direct help and good service, this website is organized by health problems. Patients are routed to their target communities based on the type of their disease. Members are required to disclose their health condition at the time of registration and are thereafter directed to the targeted community at every login. Each community is a closed environment, based on the belief that patients who suffer from similar diseases will better understand each other and thus exchange social support more efficiently. Although members in different communities can view each other’s profiles, information access is limited, and patients from different communities cannot leave comments or initiate threads in any forum other than their own. In other words, the boundaries of this online healthcare community are defined by the website structure.

3.1.1. Individual Profile and Shared Health Information. In the community that serves people with mental problems, patients must first create their personal profiles. Similar to other online social networking sites, users must provide basic information to introduce themselves (e.g., create a username with geographic and demographic information, provide an email address). In the context of an online healthcare community, however, the “basic information” focuses more on the patient’s health, such as the type of her major problem (and perhaps a second or third health problem), the date of the first symptom, and the results of any diagnostic testing. Depending on how much health information a patient shares in the community, the value of a profile is identified and controlled by incrementing an indicator based on the volume and quality of information.

There are four levels of data quality on patients’ profiles, indicated by 0 to 3 stars. If there is only basic membership information with no health data, the profile receives no stars. One star is assigned to a patient who completes a profile with biographical and condition history information. Another star is added if the patient updates treatments, symptoms, and mood maps for three months. Patients are also asked to provide names of prescription medications as well as significant supplements, equipment used, and other interventions. After completing four mood maps, patients receive a third star, which indicates that the profile is complete. Thus, the profile keeps each member’s shared information and online activities up-to-date. There is also a medical application in the profile that allows patients to update health data and display it in chart form, which makes it is easy for patients to track their health history. Consecutive records on health conditions help a patient to better understand her disease progress and offer an integrated overview to the patient’s healthcare providers.

3.1.2. Online Communication and Social Intervention. Being freed of geographic boundaries, the online healthcare community provides a large pool of patients as potential contributors who have differing anecdotal knowledge and motivations (O’Grady et al. 2008). These patients enter qualitative and quantitative health data about their conditions, symptoms, treatments, and overall experiences. To take advantage of these shared resources, each member of the mental online healthcare community can use a search tool to easily find other patients who suffer from similar symptoms or experience similar treatments. Once members find a valuable user, and think that person might have some information that they need, the members can leave comments on the profile or send private messages. As such, the number of communications reflects the quality of a patient’s profile as well as online interactions. In response to someone’s sharing outcome data, other patients can set a flag to express appreciation for the profile host’s hospitality and generosity.

The basic service offered by the online healthcare community is the exchange of social support. The forum, outside of the individual’s profile level, is a social channel for every patient in the online healthcare community. As a broadcast-type of virtual site, members with general access can exchange general information, ask questions, seek help, provide useful information, or just chat. In addition to the functionality of the email-group-based social support, the credence and the value of these conversations can be further differentiated. In particular, each post is evaluated for usefulness by other patients. Another reader can add a utility score to the post if it has been helpful. Thus, although there is no hierarchical structure for social conversations in a forum, patients still receive guidance in finding the discussion that meets their needs.

We argued earlier that being on both the giving and receiving end of social support exchanges should promote health. However, our actual social support measures are based only on the number of posts that patients contribute (produce), not how many they read (consume), as we have no way to measure the latter. While some of these posts take the form of solicitations for help, most are in the form of giving support. Nevertheless, as explained earlier, the act of giving support is often a trigger for receiving support in return. Furthermore, we can expect that active producers of message board content will also be active consumers of message board content. As a result, while our measures directly capture the amount of support that patients give, we believe that they also reflect the amount of social support they receive. Detailed data and variable descriptions are shown in Table 1, while detailed social support measurements are provided in §5.1.

## 3.2. Partially Observed Health States

The health-related information that patients upload to their profiles and share with other patients in the mood community includes their current mood, functionality level, overall distress level, and detailed distress components, treatments, symptoms, and counseling. In addition, patients need to take a weekly multipoint survey to receive an automatically generated virtual diagnosis from the website. This diagnosis communicates a community member’s “functionality level,” which is this online community’s term for an overall assessment of a person’s health condition. For example, the online survey contains detailed questions about symptoms such as sleep quality, headache severity, problems concentrating, stomach pain, nervousness, hopelessness, and treatments such as drug dosage. As functionality level is a more comprehensive measure, we discretize it and use it to operationalize the variable for health condition (state) in our model.

Often it can be overwhelming for patients to fill out such a detailed survey every week. Like the difficulty of keeping doctor visits offline, the time and effort needed to have this virtual diagnosis can reduce patients’ active engagement in the online healthcare community. The lack of effort from patients results in missing information such that only 46.09% of patients’ health condition points can be observed.

## 3.3. Social Network Construction

In our paper, a social network is constructed based on commenting activities on patients’ profiles. Because a comment is a one-way communication that represents a patient’s willingness to interact, the act of leaving a comment establishes a network tie directed from the commenter to the recipient. A directed network is therefore constructed. The degree centrality denotes the extent to which patients are involved with others in the social network. This network is constructed at every time period to reflect changes in patients’ social status and helps to document how much benefit a patient receives from and contributes to the website.

## 4. Empirical Model

One of the challenges in this study is that the health conditions of a patient are only partially observable and evolve over time. This makes it impossible to compare consecutive health conditions and to draw conclusions as to whether patients benefit from social support. To recover latent health conditions, we propose a model based on the POMDP, in which patients’ health conditions can be inferred from other observables, such as their online activities.

## 4.1. Partially Observed Markov Decision Process 4.1. Partially Observed Markov Decision Process

The POMDP starts with the Hidden Markov Model (HMM), which is modified to account for the partial observability of health conditions. HMM is a stochastic process that is not directly observable but which can be inferred through another stochastic process that produces a sequence of observable outcomes (Rabiner 1989). It has been widely applied to different contexts. For example, Netzer et al. (2008) captured customers’ dynamic relationships by modeling latent relationship states; Hauser et al. (2009) studied customers’ cognitive styles in the context of website morphing; and Singh et al. (2011) identified developers’ learning dynamics from their past experiences and interactions with peers in the context of open source software development.

Table 1 Data and Variable Descriptions

<table><tr><td>Variable</td><td>Operational definition</td><td>Description</td></tr><tr><td colspan="3">Profile data</td></tr><tr><td>New posts</td><td>The in-period number of new posts by a patient</td><td></td></tr><tr><td>Gender</td><td>The declared gender by a patient: female = 1, male = 0</td><td></td></tr><tr><td>Membership</td><td> $The\ cumulative^a$ number of days a patient stayed in the forum.</td><td></td></tr><tr><td>Update</td><td>1 if a patient&#x27;s profile was updated in a period; 0 otherwise</td><td></td></tr><tr><td>Info quality</td><td>The cumulative number of stars a patient received for her profile</td><td></td></tr><tr><td>No. treatment</td><td>The in-period number of treatments a patient took and shared on her profile</td><td></td></tr><tr><td>No. symptom</td><td>The in-period number of symptoms a patient suffered and shared on her profile</td><td></td></tr><tr><td>Posts</td><td>The cumulative number of posts on the forum by a patient</td><td>A social competence measurement; the total number of posts a patient has contributed to the forum, indicating her knowledge and attitude toward the health problem</td></tr><tr><td>Usefulness</td><td>The cumulative number of usefulness ratings by other patients for a patient&#x27;s forum posts</td><td>A social competence measurement; it is an index rated by other patients for a patient&#x27;s shared knowledge and experience; also, it can be used as a proxy for the quality of the content</td></tr><tr><td>Views</td><td>The cumulative number of times a patient&#x27;s profile was viewed</td><td>A social embeddedness measurement; it is a visibility proxy for a patient in the community</td></tr><tr><td>Thank you</td><td>The cumulative number of votes for shared personal health information on the profile</td><td>A social embeddedness measurement; it proxies to what extent the patient is recognized in the community</td></tr><tr><td>Comments</td><td>The cumulative number of comments left for a patient&#x27;s profile</td><td>A social embeddedness measurement; it proxies the communication strength of a patient&#x27;s ego-centric network</td></tr><tr><td colspan="3">Social support</td></tr><tr><td>Emo. support</td><td>The in-period number of forum posts  $weighted^b$ by emotional support content</td><td>The amount of emotional support exchanged by a patient</td></tr><tr><td>Info. support</td><td>The in-period number of forum posts weighted by informational support content</td><td>The amount of informational support exchanged by a patient</td></tr><tr><td>Companionship</td><td>The in-period number of forum posts weighted by companionship content</td><td>The amount of companionship exchanged by a patient</td></tr><tr><td colspan="3">Social network</td></tr><tr><td>In-degree</td><td>The number of incoming ties in a patient&#x27;s social network (recomputed each period)</td><td>A social embeddedness measurement; it proxies to what extent a patient is contacted by others in the network</td></tr><tr><td>Out-degree</td><td>The number of connections initiated by a patient (outgoing ties) in her social network (recomputed each period)</td><td>A social competence measurement; it proxies to what extent a patient reaches out to other patients</td></tr></table>

<sup>a</sup>All of the cumulative variables are measured since the time a patient joined the community.  
<sup>b</sup>The weights for the three types of social support in a forum post are obtained using a text mining technique, as described in §5.1.

In this study, we identify a patient’s health condition as the latent state, whenever it is unobservable, and study whether a patient’s online participation helps to change that latent state. Such a transition can be triggered by communication, the exchange of information and knowledge or other interactions with patients in the online healthcare community. The time-variant online activities (the number of new posts in the next period) define the observed outcome sequence for a patient. The Markovian transitions account for the dependence on subsequent behaviors. Figure 2 presents the POMDP in this study. In contrast to HMM, the POMDP diagram shows that a patient’s (latent) health condition is not completely hidden. Therefore, by considering this information, we reduce the randomness of the HMM and redefine the distribution of latent states.

Following the notation of Rabiner (1989), the proposed POMDP model is a combination of HMM and a probability adjustment process. It consists of three main components and an additional probability recalculation process for the partially observed health condition (state). The components are (1) the initial state distribution, ; (2) the state transition probability distribution, $A ; ( 3 )$ the observed outcome probability distribution, B; and (4) the recalculation of transition probability distribution, $A ^ { \prime } ,$ if the state is observed in the given period. For convenience, we use a compact notation for the overall model: $\lambda { = } \left( A / A ^ { \prime } , B , { \pi } \right)$ . With this model specification, we find the values of parameters in $\lambda { = } \left( A / A ^ { \prime } , B , { \pi } \right)$ to best explain the observed outcome sequence or to maximize the probability P (outcome sequence  5.

## 4.2. State Transition Matrix

We assume that there are n states that discretize health conditions from the lowest health state 1 to the highest health state n. A patient takes medications and receives treatments and other therapies. Even with such external controls, one still observes that, very often, a patient’s health condition changes quite drastically. As the changes in health state can be very random, we relax the assumption of a random walk in a typical POMDP model. The state transition probability is defined as $A = \{ a _ { i t } ( s , m ) \}$ , where $a _ { i t } ( s , m ) =$ $P ( S _ { i t + 1 } = m \mid S _ { i t } = s ) , 1 \leq s , m \leq n ;$ and $S _ { i t }$ denotes the state of patient i at time t. For each state $s ,$ we have $\textstyle \sum _ { m = 1 } ^ { n } a _ { i t } { \bar { ( } } s , m ) = 1$ and $a _ { i t } ( s , m ) \leq 1$

Figure 2 POMDP Diagram  
![](/api/attachments/TNPSHYBP/fulltext/images/6340e353e5bc3ad0ddee3c824aaf434c4d9cd682ba8687d3db3468c0216c79fd.jpg)  
A rectangle indicates an unobserved state, whereas a circle refers to an observed state. A solid arrow denotes a possible path, whereas a dashed arrow indicates a forbidden path. OHC is the acronym for online health community.

As discussed earlier, a patient’s health condition changes according to the exchange of social support through online communication and other activities. A continuous measurement of this propensity needs to be modeled into the probability transition matrix. In other words, a patient can move to a higher health state if the benefit from the online healthcare community is greater than a certain threshold, whereas the patient will transit to a lower state if the aggregate social impact is lower than a low threshold value. Hence, the matrix is defined as an ordered Logit model

$$
a _ {i t} (s, n) = 1 - \frac {\exp (\bar {\omega} _ {s \rightarrow n} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\bar {\omega} _ {s \rightarrow n} - \beta_ {s} X _ {i t} - \xi_ {i})};
$$

$$
\begin{array}{l} a _ {i t} (s, n - 1) = \frac {\exp (\bar {\omega} _ {s \to n} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\bar {\omega} _ {s \to n} - \beta_ {s} X _ {i t} - \xi_ {i})} \\ \qquad - \frac {\exp (\bar {\omega} _ {s \to n - 1} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\bar {\omega} _ {s \to n - 1} - \beta_ {s} X _ {i t} - \xi_ {i})}; \\ \dots \end{array}
$$

$$
\begin{array}{r l} & a _ {i t} (s, s) = \frac {\exp (\bar {\omega} _ {s \to s + 1} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\bar {\omega} _ {s \to s + 1} - \beta_ {s} X _ {i t} - \xi_ {i})} \\ & \qquad - \frac {\exp (\underline {{\omega}} _ {s \to s - 1} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\underline {{\omega}} _ {s \to s - 1} - \beta_ {s} X _ {i t} - \xi_ {i})}; \\ & \qquad \dots \\ & a _ {i t} (s, 2) = \frac {\exp (\underline {{\omega}} _ {s \to 2} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\underline {{\omega}} _ {s \to 2} - \beta_ {s} X _ {i t} - \xi_ {i})} \end{array}
$$

$$
\begin{array}{c} - \frac {\exp (\underline {{\omega}} _ {s \to 1} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\underline {{\omega}} _ {s \to 1} - \beta_ {s} X _ {i t} - \xi_ {i})}; \\ a _ {i t} (s, 1) = \frac {\exp (\underline {{\omega}} _ {s \to 1} - \beta_ {s} X _ {i t} - \xi_ {i})}{1 + \exp (\underline {{\omega}} _ {s \to 1} - \beta_ {s} X _ {i t} - \xi_ {i})}. \end{array}
$$

Here, s is the current state, where $\underline { { \omega } } _ { s  k }$ is the threshold for the current state s to transit to a lower state k $\left( k < s \right)$ and $\bar { \omega } _ { s \to k }$ is the threshold for the current state s to transit to a higher state $k \ ( k > s )$ . For a given s, we have $\bar { \omega } _ { s  n } \geq \bar { \omega } _ { s  n - 1 } \geq \cdots \geq \bar { \omega } _ { s  s + 1 } \geq \underline { { \omega _ { s  s - 1 } } } \geq \cdots \geq$ $\underline { { \omega } } _ { s \to 1 } .$ . The vector $X _ { i t }$ contains variables that have an impact in terms of patients’ switching between states. The vector $\beta _ { s }$ is a set of state dependent parameters. Patients’ specific random effect is represented by $\xi _ { i }$ which accounts for individual unobserved heterogeneity. As shown in Figure 2, patients in the lowest state can move to any one of $n - 1$ higher states or stay idle, while the highest state patient can stay unchanged or move down to any of $n - 1$ lower states. A patient’s health condition in any other state has the probability to move up or down or stay unchanged.

## 4.3. State-Dependent Outcome

In this paper, we choose the number of new forum posts that a patient initiates and answers as the measurement of observed online activity. Following Singh et al. (2011), we model the situation that the number of new posts in a period, a count variable, follows a negative binominal (NB) distribution for a given health condition state

$$
\begin{array}{r l} & P (O _ {i t} | S _ {i t} = s) = f _ {s} (O _ {i t} | Y _ {i t}; \gamma_ {s}, \theta_ {s} ^ {2}) \\ & \qquad = \frac {\Gamma (O _ {i t} + \theta_ {s} ^ {- 2})}{(O _ {i t} !) \Gamma (\theta_ {s} ^ {- 2})} \bigg (\frac {\theta_ {s} ^ {- 2}}{\theta_ {s} ^ {- 2} + \exp (Y _ {i t} \gamma_ {s} + \eta_ {i})} \bigg) ^ {\theta_ {s} ^ {- 2}} \\ & \qquad \cdot \bigg (\frac {\exp (Y _ {i t} \gamma_ {s} + \eta_ {i})}{\theta_ {s} ^ {- 2} + \exp (Y _ {i t} \gamma_ {s} + \eta_ {i})} \bigg) ^ {O _ {i t}}, \end{array}
$$

where $O _ { i t }$ is the number of posts for patient i at time period $t ;$ and $\theta _ { s }$ is the state-dependent parameter to capture the possible over-dispersion in $O _ { i t }$ The vector $Y _ { i t }$ comprises variables that have a direct impact on the outcome for patient i at period $t ; \ \gamma _ { s }$ is the vector that contains state-dependent parameters; and $\exp ( \gamma _ { s } Y _ { i t } + \eta _ { i } )$ specifies the expected value of $O _ { i t } ,$ according to an NB distribution. The symbol $\eta _ { i }$ is the patient-specific random effect that accounts for a patient’s unobserved heterogeneity.

## 4.4. Adjustment for State Transition Probability with Observed Patient Health Condition

The unobserved states are handled by HMM. If patient i’s health state at time period t is observed, the state transition matrix A must be modified. Recall that $a _ { i t } ( s , m ) = P ( S _ { i t + 1 } = m \mid S _ { i t } = s )$ is an element of A. If we observe that $S _ { i t + 1 } = m ^ { \prime }$ , that ${ \mathrm { i } } s ,$ at time period $t + 1 .$ , with certainty, patient i enters a health state of $m ^ { \prime } ,$ then the corresponding state transition probability $a _ { i t } ( s , m )$ is replaced by

$$
a _ {i t} ^ {\prime} (s, m) = \left\{ \begin{array}{l l} 1, & \text { if } m = m ^ {\prime}; \\ 0, & \text { if } m \neq m ^ {\prime}. \end{array} \right.
$$

This adjustment process is in line with that of Kaelbling et al. (1998). For the time period with the observed state information, all states from the previous time period will enter state $m ^ { \prime }$ with a probability of 1, and, for the next time period, the possible routes will be initiated only from this state $m ^ { \prime }$

## 4.5. Likelihood of an Observed Sequence of Outcomes

Consider an observed sequence of outcomes $O ( i ) =$ $O _ { i 1 } O _ { i 2 } . . . O _ { i T }$ for patient i and a sequence of states ${ \cal S } ( i ) = { \cal S } _ { i 1 } { \cal S } _ { i 2 } \ldots { \cal S } _ { i T }$ . The conditional likelihood, for two random effect control variables $\eta$ and $\xi ,$ which account for unobserved patient heterogeneity, is the sum over all possible paths, explicitly

$$
\begin{array}{r l} L (O (i) \mid \eta , \xi) & = \sum_ {s _ {1} = 1} ^ {n} \sum_ {s _ {2} = 1} ^ {n} \dots \sum_ {s _ {T} = 1} ^ {n} P (S _ {i 1} = s _ {1}) \\ & \cdot \prod_ {t = 2} ^ {T} P (S _ {i t} = s _ {t} \mid S _ {i t - 1} = s _ {t - 1}) \\ & \cdot \prod_ {t = 1} ^ {T} P (O _ {i t} \mid S _ {i t} = s _ {t}), \end{array}
$$

where $s _ { t } \in \{ 1 , \ldots , n \}$ is the state in which a patient can possibly reside in time period t. The likelihood of patient i can be obtained by integrating over  and $\xi$

$$
L (O (i)) = \int_ {\eta} \int_ {\xi} L (O (i) \mid \eta , \xi) d H (\xi \mid \eta) d G (\eta),
$$

where the probabilities H and G are evaluated nonparametrically; that is, their supports and corresponding probability masses are considered model parameters to be estimated.

## 5. Variable Set and Description

Our data are sampled weekly for 16 weeks. The sample includes patients’ online activities on the website as well as their interactions with other members. Specifically, we collect both levels of patients’ activities in the online healthcare community, i.e., patients’ forum activities statistics (the total number of posts is the aggregate number of conversation threads, including topic initiations and replies), helpfulness marks (other patients reward the post by marking it as helpful), and profile activities. Table 2 presents the variable sets and shows detailed summary statistics. The correlation matrix is presented in the online appendix (available as supplemental material at http://dx.doi.org/10.1287/isre.2014.0538).

## 5.1. Social Support Measurements

As discussed in §2, there are four forms of social support. Because we focus on online activities in this research, only three are considered: informational support, emotional support, and companionship. We followed the coding scheme proposed by Bambina (2007), and the details are provided in Table 3.

Social support measures are extracted from forum discussions. Unlike the user profile, where comments can be posted, the forum is a place commonly used for various kinds of social interactions and allows for richer insights into the experiences and needs of individuals affected by mental problems. We focused on the patients who participated (and not those who just lurked) in the forum and used LingPipe<sup>2</sup> to conduct a semantic analysis on the forum threads. There are $^ { 5 , 1 9 2 }$ topics initiated in the forum and 371,562 posts made during our data collection period. For each post, a number was returned to indicate the probability that this post belonged in a certain category. Because patients tend to provide multiple pieces of information in each post, it would be improper to classify a post into one category only. Therefore, we assign three probabilities (adding up to 1) to each post, corresponding to the topics addressed. With this classification scheme, we interpret the probability as the amount of social support that a patient exchanges. Consistent with the general perception, informational support is the most exchanged social support type in the online community, followed by emotional support and then companionship. Table 4 gives the statistical details.

## 5.2. Variables That Directly Affect Patients’ Health Conditions

In addition to an analysis of social support, we analyzed variables that may affect patients’ health condition dynamics; these constitute vector $X _ { i t }$ in the proposed model. The cumulative number of posts by patient i until time period t, called “posts,” could indicate social competence. This variable concerns familiarity with medical and experiential knowledge of the illness and, hence, enables a patient to gain a form of competence and social fitness in the face of serious health problems. Another variable involves recognition and appreciation from other patients, which can help a patient to feel capable and valuable. This is measured by “views,” which shows the total number of times that a patient’s profile has been checked by other community members. The number of times a profile is displayed also indicates the visibility of the patient in the community. If members find a profile particularly valuable, “thank you” is the simple way of showing appreciation for sharing information; “comments” involve more detailed communications.

Table 2 Data Statistics

<table><tr><td>Variable set</td><td>Variable</td><td>Type</td><td>Mean</td><td>St. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Online behavior</td><td>New posts</td><td>In-period</td><td>2.814</td><td>1.551</td><td>0</td><td>5</td></tr><tr><td rowspan="6">Personal characteristics</td><td>Gender</td><td>N/A</td><td>0.498</td><td>0.500</td><td>0</td><td>1</td></tr><tr><td>Info quality</td><td>Cumulative</td><td>1.481</td><td>1.117</td><td>0</td><td>3</td></tr><tr><td>Membership</td><td>Cumulative</td><td>45.34</td><td>33.415</td><td>0</td><td>118</td></tr><tr><td>Update</td><td>In-period</td><td>0.436</td><td>0.496</td><td>0</td><td>1</td></tr><tr><td>No. treatment</td><td>In-period</td><td>5.424</td><td>4.423</td><td>0</td><td>28</td></tr><tr><td>No. symptom</td><td>In-period</td><td>4.066</td><td>3.470</td><td>0</td><td>27</td></tr><tr><td colspan="7">Antecedents of social support</td></tr><tr><td rowspan="4">Social embeddedness</td><td>Views</td><td>Cumulative</td><td>14.739</td><td>7.922</td><td>0</td><td>43</td></tr><tr><td>Thank you</td><td>Cumulative</td><td>4.255</td><td>2.724</td><td>0</td><td>15</td></tr><tr><td>Comments</td><td>Cumulative</td><td>4.748</td><td>2.803</td><td>0</td><td>16</td></tr><tr><td>In-degree</td><td>In-period</td><td>8.483</td><td>5.151</td><td>0</td><td>24</td></tr><tr><td rowspan="3">Social competence</td><td>Posts</td><td>Cumulative</td><td>27.028</td><td>14.506</td><td>1</td><td>70</td></tr><tr><td>Usefulness</td><td>Cumulative</td><td>8.991</td><td>5.225</td><td>0</td><td>29</td></tr><tr><td>Out-degree</td><td>In-period</td><td>7.998</td><td>4.892</td><td>0</td><td>23</td></tr></table>

Not all posts contribute equally; some might contain trivial information, while others tend to be more useful. Therefore, “usefulness” is used to measure the value of posts, as assessed by other patients. Each patient can vote only once for any post except her own. Finally, the willingness to communicate with other patients (“out-degree”) captures a patient’s direct online activity initiated by that patient for the purpose of collaborative learning. This behavior concerns perception of the online healthcare community and attitude toward it. In addition, a patient’s medical control, including the symptoms suffered and the treatments taken, can directly affect her health condition.

Table 3 Social Support Coding Scheme

<table><tr><td>Support categories</td><td>Support subcategories</td></tr><tr><td>Informational support</td><td>AdviceReferralTeachingInformation broadcasting/seekingPersonal experience</td></tr><tr><td>Emotional support</td><td>Understanding/empathyEncouragementAffirmation/validationSympathyCaring/concern</td></tr><tr><td>Companionship</td><td>ChattingHumor/teasingGroupness</td></tr></table>

## 5.3. Variables That Directly Affect Patients’ Online Behavior

Certain factors may directly affect a patient’s online behavior pattern. For instance, the quality of a profile (“info quality”) indicates a patient’s level of concern about the disease and, thus, could directly affect her online activities. Female patients may be more active in the online healthcare community, which could lead to a different pattern for observed online behavior, given a certain health state. For example, McPherson et al. (2001) found that gender is significant in predicting communication patterns. Hence, we include a “gender” variable in our model to account for this possibility. The date that a patient joined the online healthcare community (“membership”) and the frequency with which the profile is updated (“update”) describes a patient’s perception of the online healthcare community and attitude toward it.

Table 4 Social Support Statistics<sup>a</sup>

<table><tr><td>Variable</td><td>Type</td><td>Mean</td><td>Median</td><td>St. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Info. support</td><td>In-period</td><td>1.843</td><td>1.680</td><td>1.063</td><td>0.19</td><td>7.92</td></tr><tr><td>Emo. support</td><td>In-period</td><td>0.712</td><td>0.560</td><td>0.578</td><td>0</td><td>3.68</td></tr><tr><td>Companionship</td><td>In-period</td><td>0.542</td><td>0.420</td><td>0.442</td><td>0</td><td>2.80</td></tr></table>

<sup>a</sup>Patients can edit their old posts. We include the edited posts, together with the new posts, in the calculation of social support measures. Therefore, the sum of the three social support measures per period (3.097) is slightly higher than the average of the number of new posts (2.814).

Table 5 Selection of the Number of States

<table><tr><td>Number of states</td><td>Log-likelihood</td><td>Variables</td><td>BIC</td><td>AIC</td></tr><tr><td>1</td><td>-14,583.9</td><td>16</td><td>-14,655.3</td><td>-14,599.9</td></tr><tr><td>2</td><td>-14,346.2</td><td>34</td><td>-14,497.9</td><td>-14,380.2</td></tr><tr><td>3</td><td>-13,847.3</td><td>54</td><td>-14,088.3</td><td>-13,901.3</td></tr><tr><td>4</td><td>-14,205.8</td><td>76</td><td>-14,544.9</td><td>-14,281.8</td></tr></table>

Last, we use a patient’s instant online activity measured by the number of new posts initiated or replied to in the period, to describe state-dependent outcome. A change of this measure could result from a change in the patient’s health condition. In other words, the social support may be insufficient, and the patient needs to communicate in the online healthcare community to receive additional support. The more posts contributed, the more likely it is that the patient’s health condition has changed. Note that the number does not imply that a patient’s health condition has deteriorated or improved. It suggests only that a patient’s online activity relates to the current health state.

## 5.4. Estimation and Model Selection

We started with a latent class model to estimate the initial distribution for the latent health state and then used the maximum likelihood method to estimate the model parameters. To control for patients’ heterogeneity, modeled by $\eta$ and $\xi ,$ we followed the approach by Heckman and Singer (1984). The approximation process for the underlying unknown probability distribution was evaluated by finite sampled supporting points associated with probability mass distributions. After rescaling $\eta$ and $\xi$ by two parameters $C _ { \eta }$ and $C _ { \xi } .$ , respectively, we set the boundary for each of the random effect variables to be between 0 and 1. The number of states n was chosen by the selection criteria of Bayesian Information Criterion (BIC)

$$
B I C = \ln L - k \times \ln P / 2,
$$

where P is the sample size (the number of patients), L is the likelihood of the model, and k is the number of parameters to be estimated. The goal of the model selection process is to choose the model with a probability that approaches 1 as the sample size gets larger (Anderson et al. 1998). The results are shown in Table 5. Our estimation indicates that the three-state POMDP outperforms other models.<sup>3</sup>

## 6. Findings

In this section, we report the results from the POMDP model with three health states (bad, fair, and good). The initial state distribution probabilities are (0.7756, 0.15026, 0.07414) obtained from the latent class model. The estimated parameters are presented in Table $6 ;$ the corresponding standard errors are shown in parentheses.

## 6.1. Hypothesis Test

As shown in Table $^ { 6 , }$ the estimated parameters for the effects of both informational and emotional support are positive and significant across all three states. Hence, both Hypotheses 1 and 2 are supported. To test Hypothesis 3, we compare the estimated parameters across the states for informational or emotional support. We find that the effect of emotional support increases from bad to fair and from fair to good. Informational support is more effective for patients in a bad state. However, there is no significant difference between a fair and good state. Therefore, Hypothesis 3 is partially supported. The impacts of social embeddedness and social competence are discussed in §§6.4.2 and 6.4.3. Overall, our estimated parameters suggest that Hypothesis 4 is partially supported.

## 6.2. State-Dependent Outcome

The parameters for state-dependent outcomes describe the variables that affect a patient’s activities in an online healthcare community at a given health state. It is interesting to note that, as indicated by the state-dependent constants that give the intrinsic propensity to contribute, the patients tend to create fewer posts as they progress to a better health state. In the online appendix, we calculate the expected intrinsic number of new posts, which are 2.75 for a bad state, 1.56 for a fair state, and 1.13 for a good state. These numbers are statistically different. The patients in a bad state want to learn more about their disease and, hence, have relatively more problems or questions to ask than do those in a fair or good state.

As shown in Table $^ { 6 , }$ women participated more actively than did men in the online healthcare community across all health states. Female patients tended to post more when they were in the worst (3.44 more posts than the intrinsic number) or best condition (the additional 0.96 posts). This may be because women are more sensitive to changes in their emotional and physiological states (Hunt et al. 1981). Hence, they are perhaps more willing to express themselves and their emotions in extreme conditions (bad or good). This finding is consistent with those of prior studies (e.g., Hunt et al. 1981, Tessler and Mechanic 1978) that show a gender differentiation in admitting to certain problems.

A patient with good information quality is one who keeps close track of her disease progression. She prefers to seek social support, to determine underlying reasons, and to try to improve her condition. This is confirmed by the significant and positive coefficients in our results. The duration of membership is a measure of the attitude commitment to online healthcare communities. Our results show that a member with a longer tenure, whether the condition is good or bad, tended to contribute more to an online healthcare community than did a newcomer. The significant and negative coefficients for patients’ profile updates for all states suggest the various forms of use of this healthcare social networking platform and its functionality. A patient who prefers to use this online tool as a means of self-reporting and documentation is more focused on her own health condition and experiences and, thus, less likely to participate in the collaborative activities.

Table 6 Estimated Parameters for the Three-State POMDP<sup>a</sup>

<table><tr><td>Parameter</td><td colspan="2">State 1 (bad)</td><td colspan="2">State 2 (fair)</td><td colspan="2">State 3 (good)</td></tr><tr><td>θ Dispersion</td><td>0.7512***</td><td>(0.1213)</td><td>0.4758***</td><td>(0.0254)</td><td>0.5372**</td><td>(0.1982)</td></tr><tr><td colspan="7">Variables that affect state transition</td></tr><tr><td>β1 [views]</td><td>0.9561***</td><td>(0.1837)</td><td>0.9287***</td><td>(0.2382)</td><td>0.7271***</td><td>(0.1642)</td></tr><tr><td>β2 [thank you]</td><td>1.6298***</td><td>(0.1259)</td><td>0.6284***</td><td>(0.1983)</td><td>2.2823***</td><td>(0.3487)</td></tr><tr><td>β3 [comments]</td><td>3.0172***</td><td>(0.1834)</td><td>0.8768***</td><td>(0.2674)</td><td>1.6417**</td><td>(0.7283)</td></tr><tr><td>β4 [usefulness]</td><td>0.9265***</td><td>(0.3342)</td><td>0.3372***</td><td>(0.1028)</td><td>1.4419***</td><td>(0.1482)</td></tr><tr><td>β5 [in-degree]</td><td>-1.0564***</td><td>(0.2166)</td><td>0.2209*</td><td>(0.1192)</td><td>-0.6198***</td><td>(0.2128)</td></tr><tr><td>β6 [out-degree]</td><td>0.8293***</td><td>(0.1698)</td><td>0.2231**</td><td>(0.1012)</td><td>0.6126***</td><td>(0.1871)</td></tr><tr><td>β7 [info. support]</td><td>0.7637***</td><td>(0.1095)</td><td>0.6123***</td><td>(0.1482)</td><td>0.6218***</td><td>(0.1001)</td></tr><tr><td>β8 [emo. support]</td><td>0.6234***</td><td>(0.1243)</td><td>0.8198***</td><td>(0.2031)</td><td>1.0821***</td><td>(0.2237)</td></tr><tr><td>β9 [posts]</td><td>2.4298***</td><td>(0.1771)</td><td>1.8728***</td><td>(0.1749)</td><td>4.4925***</td><td>(0.4548)</td></tr><tr><td>β10 [no. treatment]</td><td>1.2372***</td><td>(0.1210)</td><td>0.7213**</td><td>(0.2845)</td><td>0.8832***</td><td>(0.2837)</td></tr><tr><td>β11 [no. symptom]</td><td>-0.9218***</td><td>(0.0972)</td><td>-1.0023***</td><td>(0.2693)</td><td>-0.2178***</td><td>(0.0415)</td></tr><tr><td colspan="7">Thresholds</td></tr><tr><td>State 1 (bad)</td><td></td><td></td><td>0.9227***</td><td>(0.1894)</td><td>3.1593***</td><td>(0.6831)</td></tr><tr><td>State 2 (fair)</td><td>-2.5327***</td><td>(0.3287)</td><td></td><td></td><td>2.6481***</td><td>(0.4037)</td></tr><tr><td>State 3 (good)</td><td>-3.0126***</td><td>(0.6044)</td><td>-1.0469***</td><td>(0.1362)</td><td></td><td></td></tr><tr><td colspan="7">Variables that affect state dependent outcome</td></tr><tr><td>γ0 [constant]</td><td>1.1126***</td><td>(0.2436)</td><td>-0.5479***</td><td>(0.1928)</td><td>0.2281***</td><td>(0.0244)</td></tr><tr><td>γ1 [gender]</td><td>0.8127***</td><td>(0.1902)</td><td>-0.7487*</td><td>(0.4235)</td><td>0.6127**</td><td>(0.2823)</td></tr><tr><td>γ2 [info quality]</td><td>0.2841***</td><td>(0.0512)</td><td>-0.4120</td><td>(0.2876)</td><td>0.1298***</td><td>(0.0685)</td></tr><tr><td>γ3 [membership]</td><td>0.8236***</td><td>(0.0075)</td><td>0.5824***</td><td>(0.0046)</td><td>0.9237***</td><td>(0.0029)</td></tr><tr><td>γ4 [update]</td><td>-0.7218***</td><td>(0.0951)</td><td>-0.5218</td><td>(0.3827)</td><td>-0.9218***</td><td>(0.1148)</td></tr><tr><td colspan="7">Unobserved heterogeneity (η,ξ)</td></tr><tr><td>Cη = -0.204, Cξ = -0.151</td><td></td><td>η1 = 0</td><td>η2 = 0.3174</td><td></td><td>η3 = 0.5313</td><td>η4 = 1</td></tr><tr><td>Probability G(η)</td><td></td><td>0.0639</td><td>0.3487</td><td></td><td>0.4015</td><td>0.1859</td></tr><tr><td colspan="7">Conditional distribution: H(ξ | η)</td></tr><tr><td>ξ1 = 0</td><td></td><td>0.9417</td><td>0.2312</td><td></td><td>0.1302</td><td>0.9271</td></tr><tr><td>ξ2 = 0.4134</td><td></td><td>0.0295</td><td>0.5675</td><td></td><td>0.1934</td><td>0.0369</td></tr><tr><td>ξ3 = 1</td><td></td><td>0.0288</td><td>0.2013</td><td></td><td>0.6764</td><td>0.0360</td></tr></table>

<sup>a</sup>The following rescaling is performed: “membership” is log transformed; “views,” “thank you,” “comments,” “usefulness,” “in-degree,” and “out-degree” are scaled down by a factor of 100; “posts” is scaled down by a factor of 1,000; “info. support,” “no. treatment,” “no. symptom,” “gender,” “info quality,” and “update” are scaled down by a factor of 10.  
<sup>∗</sup>p < 001; <sup>∗∗</sup>p < 0005; <sup>∗∗∗</sup>p < 0001.

## 6.3. State Transitions and Baseline Results

The thresholds provide the intrinsic propensity to transition from one state to another. As we allow patients to “jump” between different states, these thresholds ensure that moving involves some positive boundary requirements. The intrinsic probabilities<sup>4</sup> to transit between states are shown in Table 7.

Although a patient’s health state could change dramatically (even to the point of jumping to a nonadjacent state in our model), our results showed that patients are indeed relatively stable in their health states. Unlike mood changes, health status concerns a patient’s physical and mental ability. The variation is minimized by medication control. The stickiness, or the high probability of staying, in the current state could result from the effect of medical treatments that patients received for their mental disease. As for mood problems, medication is not always recommended for those with mild depression because the risks outweigh the benefits. In our data set, an average of 35% of patients were undergoing medical treatments. However, without help from external resources, e.g., various services provided in the online healthcare community, a patient has a lower probability of improving her health condition. Without participation in an online healthcare community, a patient is more likely to stay at her current health state or get worse.

Table 7 Intrinsic Transition Matrix

<table><tr><td></td><td>Bad</td><td>Fair</td><td>Good</td></tr><tr><td>Bad</td><td>0.7254</td><td>0.2357</td><td>0.0389</td></tr><tr><td>Fair</td><td>0.0771</td><td>0.8597</td><td>0.0632</td></tr><tr><td>Good</td><td>0.0492</td><td>0.2204</td><td>0.7304</td></tr></table>

## 6.4. Factors That Influence Patients’ Health Transition

As our primary objective was to determine the helpfulness of online healthcare communities in improving patients’ health conditions, we provided detailed discussions of the variables that affect a patient’s health state and consequently influence her behavior in online healthcare communities. Next, we categorize these variables into three groups. The transition probabilities are evaluated with the average value of the focal variable and the values of the other variables set at zero, and are compared with the intrinsic transition probabilities.

6.4.1. Impact of Social Support on Health Condition. Table 8 shows the difference between the changes in transition probabilities, due to informational support, compared to the changes in intrinsic probabilities shown in Table 7 (also shown in parentheses). By communicating with other members, a patient is more likely to obtain useful information and to better understand her health condition. Along with information about medical terms and symptoms, personal advice and referrals make the communication more valuable. The firsthand experience information available from the online healthcare community helps patients muster the strength to fight their disease; the community is also a place to find guidance for selfmanagement. All of this helps to increase the probability that patients will transit to a better health state. For example, compared with intrinsic propensity transition, the probability of a patient in a bad state moving to a fair state is increased by 2.33%<sup>5</sup> after experiencing the average amount of informational support (i.e., 1.843 posts fully weighted in informational support). With a 2.2% increase of probability, a patient already in good condition is more likely to remain so when she receives informational support. Our results also indicate that the possibility of worsening health condition decreases when a patient experiences informational support.

Table 8 Change in Transition Probability: Informational Support

<table><tr><td></td><td>Bad</td><td>Fair</td><td>Good</td></tr><tr><td>Bad</td><td>-0.0289(0.7254)</td><td>0.0233(0.2357)</td><td>0.0056(0.0389)</td></tr><tr><td>Fair</td><td>-0.0077(0.0771)</td><td>0.0006(0.8597)</td><td>0.0070(0.0632)</td></tr><tr><td>Good</td><td>-0.0051(0.0492)</td><td>-0.0169(0.2204)</td><td>0.0220(0.7304)</td></tr></table>

Table 9 Change in Transition Probability: Emotional Support

<table><tr><td></td><td>Bad</td><td>Fair</td><td>Good</td></tr><tr><td>Bad</td><td>-0.0964(0.7254)</td><td>0.0760(0.2357)</td><td>0.0204(0.0389)</td></tr><tr><td>Fair</td><td>-0.0326(0.0771)</td><td>-0.0121(0.8597)</td><td>0.0447(0.0632)</td></tr><tr><td>Good</td><td>-0.0258(0.0492)</td><td>-0.0987(0.2204)</td><td>0.1237(0.7304)</td></tr></table>

Emotional support has a significant influence on patients in different states. As shown in Table 9, we observe the same pattern seen with informational support: The benefits of emotional support are significant and positive in all three states. In other words, such support increases the probability that patients move to a better health condition. Many studies have found that emotional support plays a critical role in a patient’s outcome. For example, in a study of heart failure, emotional support was found to have significant association with risk for heart disease (Krumholz et al. 1998). We also find evidence that supports the importance of emotional support. With the average amount of emotional support (i.e., 0.712 posts fully weighted in emotional support) patients in a bad state had a 7.6% higher possibility of moving to a fair state and a 9.64% lower possibility of staying in a bad state. A patient who was already in a good state was shown to be more likely (a 12.37% higher probability) to remain in good condition.

Severe disease affects patients and changes their everyday activities. Researchers in psychosocial and social science have examined social support in various contexts. Such work includes studying patients’ need for emotional support (e.g., Slevin et al. 1996) and emotional and informational support for patients’ relatives (Eriksson and Lauri 2000). The requirements for such social support change according to the magnitude and time in need. Tables 8 and 9 show that emotional support is overall more influential in changing patients’ conditions, although patients receive more units of informational support in this community.

6.4.2. Impact of Social Embeddedness. Multiple measurements can be used to evaluate how well patients communicate with other community members and how personal images are built in such a virtual world. In searching for similar patients with certain criteria, a patient can learn more from those members by viewing their detailed profiles. Therefore, the number of times that a patient’s profile is viewed indicates how visible a patient is in this community. The coefficient for profile “views” was positively significant and increased the probability that a patient would move to a better health state. For example, consider a patient in a bad state. The probability of moving to a fair state in the next time period increases by 2.33% if her profile has been reviewed 0.1474 times (the average number of views scaled down by a factor of 100),<sup>6</sup> while there is a 2.89% increase in the probability of staying in the same state for the next period.

A large number of “thank you” votes indicated the quality of a patient’s data. It not only confirmed the patient’s effort in disease self-management but also made the patient feel appreciation for helping others. This satisfaction can influence a patient’s ability to move among different health states. We find that patients in a bad state had a 1.13% increase in the probability of moving to a fair state and a 1.4% decrease in the probability of staying in a bad state if she receives 0.04748 comments (the average number of comments scaled down by a factor of 100). Patients in a good state also benefited from confirmation and encouragement and, thus, had a higher probability of staying well.

The measurement for “comments” was intended to signal patients’ profile quality. As shown in Table 6, the number of comments on a patient’s profile had a significant and positive impact on all health states. This may be because the profile owner is encouraged by recognition and care from other patients, which increases the probability that the patient will feel better. Even a patient in a bad health condition who received an average number of comments had a higher probability of moving to a better condition (a 2.37% increase to a fair state) than those who did not receive any comments. If the patient was already in good condition, the possibility of staying well increased 1.51% compared to when this recognition was absent.

Finally, in-degree measures the incoming connections of a patient in the community. It can be considered a proxy for receiving social support from others in the community. As shown in Table 6, the significant and negative coefficients suggest that patients who are in extreme conditions (bad or good) and receive more social support are less likely to seek help. As noted, there are two channels through which patients can communicate: on their profile or in the forum. The social network is constructed at the patients’ profile level, while patients communicate by making comments. These egocentric networks reflect patients’ close contacts and indicate a cluster of patients who are familiar with each other. The preference for talking with her favored cluster of patients and being less likely to participate in community-based communications hinders the patient’s progress to a healthier state (a 1.43% decrease from bad to fair state).

6.4.3. Impact of Displaying Social Competence on Health Condition. The number of posts and the helpfulness of those posts help to determine patients’ social value in this online healthcare community. The number of posts that a patient creates is an indicator of her attitude toward facing the disease and her aggregated knowledge of the disease, which may include valuable information and experience for other patients. The “usefulness” variable measured the effectiveness of the patients’ posts. In addition, out-degree, constructed by counting a patient’s selfmotivated or initiated communication, indicates the patient’s knowledge of a certain disease and helps to identify her familiarity with health problems and the potential value of this familiarity to other patients. Table 6 shows the positive impact of such activities on patients’ health conditions, all of which suggest a patient’s social competence reconstructed in virtual space.

A patient in a bad health state could create posts in the online healthcare community as a means to seek help. This could help the patient express unhappiness and release pressure as well as receive advice about her next move and, hence, prevent her from falling into a worse condition. There was a 1.33% decrease in a patient’s probability of staying in a bad state and a 1.78% smaller probability that a patient in a good state would move to a fair state. The recognition and reward for competence (“usefulness”) also kept patients from getting worse. For example, appreciation gave patients in a bad state a 1.37% greater chance of moving to a fair state. A patient already in good condition increased her probability of staying well by 2.47%. Finally, a patient’s health condition changes with her outreach behavior as indicated by out-degree. There is a higher probability of moving to a better condition (a 2.37% increased likelihood of moving to a fair state) and a 3.3% increased probability that a patient will stay in a good condition.

## 7. Further Analyses and Robustness Checks

The analysis above is based on a POMDP model estimated based on aggregated data over a four-month period, with a focus on social support in the online healthcare community. In this section, we present further analysis that compares the impact of different forms of social support. We then discuss the robustness checks of the qualitative findings and the limitation of the model.

## 7.1. Contrast Between Informational Support and Emotional Support

The informational and emotional support delivered through online healthcare communities may help patients cope better with their mental problems. Bambina (2007) investigated a cancer forum and found that, on average, members receive more informational support than emotional support. However, it remains unclear, due to the lack of prior empirical evidence, which type of support is better for meeting patients’ social needs. Emotional support may be more important than informational support for patients who suffer from mental problems, as they are more emotional and feel lonely due to their inability to maintain social relationships (McCorkle et al. 2008). Their perceptions of insufficient social support hinder their recovery from mental illness. On the contrary, the anecdotal and experiential knowledge shared by individuals as to various treatments and medications create a “wisdom of the crowd” and may have an impact on patients’ health decision making (O’Grady et al. 2008). Therefore, to help improve the effectiveness of online healthcare communities, it is important to first contrast the respective effect of informational and emotional support.

To test this argument, we calculate the difference between the parameters of emotional and informational support, for a given state, and the corresponding standard error. The results, reported in the online appendix, are all significant at the 1% level. Hence, we conclude that, for patients with mental problems, the online emotional support they receive plays a more important role in helping them to progress to healthier conditions than does informational support. That is, our empirical result suggests that emotional support is significantly more effective in helping mental patients to progress to a better state.

## 7.2. Posterior Analysis

Here, we applied the filtering approach proposed by Hamilton (1989) to recover patients’ unobserved health conditions across time periods. Once the model parameters are estimated, the likelihood can be obtained using the information until time t. Posterior probability for a patient in a given state can be calculated using the Bayes rule. This allowed a patient to be classified, in any given time period, into a health state according to the posterior probability calculation. As presented in Figure 3,<sup>7</sup> 45% to 50% of patients were in a bad health condition, and 35% to 40% of patients were in a fair state during the period under study.

Figure 3 Posterior Analysis for Patient Distribution  
![](/api/attachments/TNPSHYBP/fulltext/images/e391f170bf351fd5cfc5f89380adfc33748c0bb01eb0e106cdb1e2a8ecdc794d.jpg)

Figure 4 contains two plots of individual patient behavior. As can be seen, there was no unique pattern: One remained at the same level and was more or less stable, while the other fluctuated among states. Because the observed information on health states from Week 17 was not used to calibrate the model, the results of posterior analysis for Week 17 and beyond were purely predicted. Figure 4 shows that our POMDP model was highly accurate in predicting patients’ health conditions. We have examined all of the patients in our data set and calculated the prediction accuracy, defined as the percentage of correctly predicted health states observable from Week 17 to Week 32. The overall accuracy is 93.25%. As such, our result shows that this is a very effective way for patients and healthcare providers to recover missing or unavailable information.

## 7.3. Robustness Check

Various attempts were made to check the robustness of our results. First, we checked the robustness of observed health conditions. In our data set, the observed functionality level was scaled from 0 to 100. We performed various classifiers to categorize (or discretize) functionality levels. The alternative trials did not produce qualitatively different results, and the likelihood does not exceed the result presented earlier. In addition, we have conducted the following analyses.<sup>8</sup>

Figure 4 Posterior Analysis with Partially Observed Health State  
![](/api/attachments/TNPSHYBP/fulltext/images/b9ef7ce9d3903110623d547f25ccc4b87b85fa6046e2760bf0ba39488ab124ea.jpg)

Exogeneity of random effects $\xi$ and $\eta .$ To verify that the random effects are exogenous, or uncorrelated with the covariates, we follow Wooldridge (2001) to apply a variation (Mundlak 1978) of the Chamberlain device (Chamberlain 1980). Explicitly, we write $\xi _ { i } =$ $\xi ^ { 1 } \bar { x } _ { i } + \xi _ { i } ^ { 0 }$ and $\underline { { \eta } } _ { i } = \eta ^ { 1 } \bar { y } _ { i } + \eta _ { i } ^ { 0 } .$ , where $\begin{array} { r } { \bar { x } _ { i } = T ^ { - 1 } \sum _ { t = 1 } ^ { T } x _ { i t } } \end{array}$ and $\begin{array} { r } { \bar { y } _ { i } = T ^ { - 1 } \sum _ { t = 1 } ^ { T } y _ { i t } } \end{array}$ are vectors of means of covariates; $\xi ^ { 1 }$ and $\eta ^ { 1 }$ are vectors of coefficients to be estimated; and $\xi _ { i } ^ { 0 }$ and $\eta _ { i } ^ { 0 }$ are handled nonparametrically, as before. The estimation results, as presented in the online appendix, show that $\xi ^ { 1 }$ and $\eta ^ { 1 }$ are insignificant, with the exception of membership. While the exogeneity condition is not strictly satisfied, relaxing it with the Chamberlain device does not result in significant differences. Hence, we retain the original model, which is more parsimonious.

Stationarity of NBD. We model the dependent variable and number of new posts using NBD, which is stationary (Morrison and Schmittlein 1988). In general, patients’ online behaviors vary over time. To account for this nonstationary nature, we allow the mean of NBD to change from one period to another. Therefore, the overall process is stationary within a period but nonstationary across periods. As the length of time reduces, this approximation becomes a more accurate presentation. We recalculated the values of covariates using a half-week and two weeks as the time periods, respectively, and reconducted the analysis. The results showed no significant difference. The prediction accuracies are 93.1% and 92.7%, respectively. Hence, we chose one week as the length of time between observations, to coincide with the practice of the online healthcare community, which routinely asked patients to update their profiles weekly.

Effects of missing data. For each patient, we calculated the percentage of data availability. For example, if a patient reported her condition in 8 weeks out of 16, the patient’s data availability is 50%. Figure 5 is a scatterplot of prediction accuracy on data availability for all 7,512 patients in the data set. There is no apparent pattern, and the correlation between the two is insignificant, at <sub>−</sub>0.0069.

![](/api/attachments/TNPSHYBP/fulltext/images/4ae48f3762388281413746a0711cd1264f0c516f36237c88f2339fa90f969952.jpg)

To further analyze the effects of missing data on prediction accuracy, we created stratified subsamples (around 1,000 patients) based on the percentage of observed health states. Three subsamples have 13.37%, 21.91%, and 34.73% of available health states. Because there is a very low correlation of missing patterns between the first 16 weeks of data and the second (holdout), the data availability for the holdout is almost the same (around 37%) for the three subsamples. The prediction accuracies are 86.59%, 87.21%, and 89.18%, which do not differ significantly from each other.

More analyses, as reported in the online appendix, show that the patterns of missing data are not missing completely at random (MCAR). It also appears that some patients report their health information when they are under certain health conditions; hence, it is unlikely that missing at random (MAR) is true. Note that our POMDP framework does not require either of the above conditions to hold. Similarly, we created stratified subsamples based on the variability of data availability across health states, which was operationalized using a coefficient of variation (COV). For example, in the case of three health states, if a patient reported (2, 2, 2) times (a total of 6 times of 16), the COV is zero. The missing data for the patient is independent of her health conditions and, hence, is more likely to be MAR. The other extreme is (6, 0, 0), which is not MAR. The two subsamples have a COV of 0.40 and 1.68, respectively. However, the prediction accuracies are virtually identical, at 89.09% and 89.52%. Therefore, we conclude that our POMDP model is robust with respect to the missing data issues.

Figure 5 Effect of Data Availability on Prediction Accuracy  
![](/api/attachments/TNPSHYBP/fulltext/images/8108e6b1da0ca3e22d699a4527a15885624ddc693910eecbad0072a9c8932c52.jpg)

## 7.4. Limitations

There are several limitations in our study that must be taken into consideration. First, we used quantitative analysis to examine the helpfulness of social support. In our findings, social support is shown to have a significant impact on patients’ health condition changes, but our data set does not allow us to distinguish between active and passive social support. Instead of considering social support as a discrete, time-limit act with immediate or delayed effects (King et al. 2006), we use a different perspective by taking into account the flow of support and the evolving meaning of support over time. Nevertheless, we are unable to separate “providing” from “seeking” social support and, hence, cannot precisely measure the impact of each. Identification of the direction of social support facilitates examination of the reciprocal aspect which better fits the context of an online healthcare community. Second, we use the number of posts as the measure for patients’ online healthcare community outcomes. It is very possible, however, that patients possess different preferences in their online activities. For example, some patients may spend more time observing rather than actively participating in others’ communications. It would be helpful to incorporate more measures of patients’ online behavior patterns. Third, we considered only direct communications among patients. Social support, however, can also be transferred by word-of-mouth via common friends. Therefore, including other network measures could shed more light on the benefit of an online healthcare community to patients.

## 8. Conclusion and Implications

In this paper, we developed a POMDP model to study patients’ dynamic health condition outcomes. The POMDP model was estimated by a maximum likelihood procedure. Three health condition states were identified to best explain the data. Our results offered several insights into the driving forces behind patients’ health condition changes and, hence, demonstrated the usefulness and value of online healthcare communities.

Despite the sizeable body of research on social support and various findings that confirm the positive impact of social support on individuals’ health conditions, there is less attention paid to the magnitude of and differences between the impact of different types of support. In particular, patients’ online behavior patterns and the impact of such online activities on their health are not yet fully understood. Although the use of online healthcare communities, which provide emotional support and information sharing, is thought to be positive for patients’ health, there also is a need for a more careful explanation of the processes by which support (or the lack of it) might affect patients’ health outcomes. Thus, the main contributions of this work are (1) our proposed framework to measure how helpful an online social network can be, and (2) new evidence of the efficiencies and benefits of such online services. Growing participation in online healthcare communities is well documented. While research on how these forms of social networking work and how well they serve patients’ needs is underway, the important question of how social support changes patients’ health outcomes remains (to our knowledge) unanswered (Lamberg 2003). By investigating the online activities of patients who suffer from mental disease, we revealed the benefits and advantages of online healthcare communities in helping patients improve their health conditions.

Our procedure to identify a patient’s unseen health condition distinguishes our model from other social networking studies on healthcare. Extending the sociological research on patient behavior, we used the POMDP model to explain patients’ health condition changes with respect to the social support exchanged online. We found that patients are actively involved in disease self-management. Participation in online discussions enabled them to learn from other patients and to enjoy a partial prevention effect that reduced the possibility of their condition’s deteriorating. These findings can be used to encourage users who are passively participating in online healthcare communities to reduce lurking behaviors. This could result in online healthcare communities’ becoming a place where social support is provided by an even more diverse membership. The investigation of transition distributions for various effects revealed that such communications were more effective for patients in good health conditions. We showed that a healthier patient benefits more from an online healthcare community and has a higher probability of staying well.

We found, in our empirical analysis, that informational support was the most exchanged social support available online. It was the main attraction for patients and their families to join an online healthcare community. However, its impact on changing patients’ health condition was relatively lower than that of emotional support. Our results also indicated that recognition and positive feedback from other patients helped to improve an individual’s health condition and encouraged patients to play their social roles competently. This effect was enhanced in the “sticky” dormant states.

Finally, our work is just a first step. It revealed the importance of studying the role of information systems in the context of healthcare. This is in keeping with Fichman et al. (2011), who noted that the intersection of social media and healthcare is a promising direction for study. Our work combined theoretical modeling and data validation and yielded quantitative results. These findings signify a potential direction for healthcare reform and suggest the effective and encouraging consequences of incorporating patients’ self-assistance efforts into health management. These possibilities are promising for both information systems and healthcare practices research.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2014.0538.

## Acknowledgments

The authors thank the senior editor, associate editor, and the three anonymous reviewers for their constructive suggestions throughout the review process. The authors also thank Prabuddha De, Sanjeev Dewan, Bin Gu, Karthik N. Kannan, Vijay S. Mookerjee, Param Vir Singh, D. J. Wu, and the participants in the research seminars at Arizona State University, Boston University, City University of Hong Kong, Fordham University, Fudan University, George Mason University, Georgia Institute of Technology, Georgia State University, Harbin Institute of Technology, Indiana University, Michigan State University, Purdue University, Rensselaer Polytechnic Institute, Rutgers Business School, University of Alberta, University of Arizona, University of California Irvine, University of Florida, and the University of Texas at Dallas for their helpful comments and discussions.

## References

Abbott S, Freeth D (2008) Social capital and health: Starting to make sense of the role of generalized trust and reciprocity. J. Health Psych. 13(7):874–883.

Agarwal R, Gao G, DesRoches C, Jha AK (2010) The digital transformation of healthcare: Current status and the road ahead. Inform. Systems Res. 21(4):796–809.

Anderson DR, Burnham KP, White GC (1998) Comparison of AIC and CAIC for model selection and statistical inference from capture-recapture studies. J. Appl. Statist. 25(2):263–282.

Antonucci TC, Jackson JS (1990) The role of reciprocity in social support. Sarason BR, Sarason IG, Pierce GR, eds. Social Support: An Interactional View (Wiley, New York), 173–198.

Bambina AD (2007) Online Social Support: The Interplay of Social Networks and Computer-Mediated Communication (Cambria Press, Amherst, NY).

Bandura A (2004) Health promotion by social cognitive means. Health Ed. Behav. 31(2):143–164.

Benkler Y (2002) Coase’s penguin, or, linux and the nature of the firm. Yale Law J. 112(3):369–446.

Berkman LA, Breslow L (1984) Health and ways of living: The Alameda county studies. J. Ambulatory Care Management 7(1):80.

Berkman LF, Glass T, Brissette I, Seeman TE (2000) From social integration to health: Durkheim in the new millennium. Soc. Sci. Medicine 51(6):843–857.

Chamberlain G (1980) Analysis of covariance with qualitative data. Rev. Econom. Stud. 47(1):225–238.

Chernomas WM, Clarke DE (2010) Social support and women living with serious mental illness. Project 23 of the Prairie Women’s Health Centre of Excellence, Winnipeg, Manitoba, Canada.

Christensen H, Griffiths K (2000) The Internet and mental health literacy. Aust N Z J Psychiatry 34(6):975–979.

Clark CM (2006) Relations between social support and physical health. Working paper, Rochester Institute of Technology, Rochester, NY.

Cobb S (1976) Social support as a moderator of life stress. Psychosomatic Medicine 38(5):300–314.

Cohen S, Wills TA (1985) Social support, stress and the buffering hypothesis. Psych. Bull. 98(2):310–357.

Coulson NS (2005) Receiving social support online: An analysis of a computer-mediated support group for individuals living with irritable bowel syndrome. CyberPsychology Behav. 8(6):580–584.

Eriksson E, Lauri S (2000) Informational and emotional support for cancer patients’ relatives. Eur. J. Cancer Care 9(1):8–15.

Fichman RG, Kohli R, Krishnan R, Kane GC (2011) The role of information systems in healthcare: Current research and future trends. Inform. Systems Res. 22(3):419–428.

Fox S (2011) Health topics: 80% of Internet users look for health information online. Pew Internet & American Life Project, Washington, DC.

Fox S, Jones S (2009) The social life of health information: Americans’ pursuit of health takes place within a widening network of both online and offline sources. Pew Internet & American Life Project, Washington, DC.

Greco P, Pendley JS, McDonell K, Reeves G (2001) A peer group intervention for adolescents with type 1 diabetes and their best friends. J. Pediatric Psych. 26(8):485–490.

Griffiths F, Cave J, Boardman F, Ren J, Pawlikowska T, Ball R, Clarke A, Cohen A (2012) Social networks—The future for health care delivery. Soc. Sci. Medicine 75(12):2233–2241.

Hamilton JD (1989) A new approach to the economic-analysis of nonstationary time-series and the business-cycle. Econometrica 57(2):357–384.

Hauser JR, Urban GL, Liberali G, Braun M (2009) Website morphing. Marketing Sci. 28(2):202–223.

Heckman J, Singer B (1984) A method for minimizing the impact of distributional assumptions in econometric models for duration data. Econometrica 52(2):271–320.

Hunt SM, McKenna SP, McEwen J, Williams J, Papp E (1981) The Nottingham health profile—Subjective health-status and medical consultations. Soc. Sci. Medicine Part A-Medical Sociol. 15(3): 221–229.

Jacobson DE (1986) Types and timing of social support. J. Health Soc. Behav. 27(3):250–264.

Jou YH, Fukada H (2002) Stress, health, and reciprocity and sufficiency of social support: The case of university students in Japan. J. Soc. Psych. 142(3):353–370.

Jung J (1990) The role of reciprocity in social support. Basic Appl. Soc. Psych. 11(3):243–253.

Kaelbling LP, Littman ML, Cassandra AR (1998) Planning and acting in partially observable stochastic domains. Artificial Intelligence 101(1–2):99–134.

Kassirer JP (2000) Patients, physicians, and the Internet. Health Affairs 19(6):115–123.

King G, Wiloughby C, Specht JA, Brown E (2006) Social support processes and the adaptation of individuals with chronic disabilities. Qualitative Health Res. 16(7):902–925.

Krumholz HM, Butler J, Miller J, Vaccarino V, Williams CS, Mendes de Leon CF, Seeman TE, Kasl SV, Berkman LF (1998) Prognostic importance of emotional support for elderly patients hospitalized with heart failure. Circulation 97(10):958–964.

Lamberg L (2003) Online empathy for mood disorders-patients turn to Internet support groups. Amer. Medical Association 289(233): 3073–3077.

Langford CP, Bowsher J, Maloney JP, Lillis PP (1997) Social support: A conceptual analysis. J. Adv. Nurs. 25(1):95–100.

Leung L (2011) Loneliness, social support, and preference for online social interaction: The mediating effects of identity experimentation online among children and adolescents. Chinese J. Comm. 4(4):381–399.

McCorkle BH, Rogers ES, Dunn EC, Lyass A, Wan YM (2008) Increasing social support for individuals with serious mental illness: Evaluating the compeer model of intentional friendship. Community Mental Health J. 44(5):359–366.

McMullan M (2006) Patients using the Internet to obtain health information: How this affects the patient-health professional relationship. Patient Ed. Counseling 63(1–2):24–28.

McPherson M, Smith-Lovin L, Cook JM (2001) Birds of a feather: Homophily in social networks? Annu. Rev. Sociol. 27:415–444.

Merton RK (1976) Sociology Ambivalence and Other Essays (Free Press, New York).

Midlarsky E (1991) Helping as coping. Prosocial Behav.: Rev. Personality Soc. Psych. 12:238–264.

Morrison DG, Schmittlein DC (1988) Generalizing the NBD model for customer purchases: What are the implications and is it worth the effort? J. Bus. Econom. Statist. 6(2):145–159.

Mundlak Y (1978) On the pooling of time series and cross section data. Econometrica 46(1):69–85.

Netzer O, Lattin JM, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2): 185–204.

O’Grady LA, Witteman H, Wathen CN (2008) The experiential health information processing model: Supporting collaborative web-based patient education. BMC Medical Informatics Decision Making 8:58.

Oluwole DA, Hammed AT, Awaebe J (2011) Patterns of stress, social support, and mental health among Nigerian women, http://advancingwomen.com/awl/awl\_wordpress/patterns-of -stress-social-support-and-mental-health-among-nigerian -women/.

Pearlin LI (1985) Social structure and processes of social support. Cohen S, Syme SL, eds. Social Support and Health (Academic Press, New York), 43–60.

Post SG (2005) Altruism, happiness, and health: It’s good to be good. Internat. J. Behav. Medicine 12(2):66–77.

Powell J, Clarke A (2006) Internet information-seeking in mental health: Population survey. British J. Psychiatry 189:273–277.

Putnam RD (1993) Making Democracy Work: Civic Traditions in Modern Italy (Princeton University Press, Princeton, NJ).

Rabiner LR (1989) A tutorial on hidden Markov-models and selected applications in speech recognition. Proc. IEEE 77(2): 257–286.

Radley A, Billig M (1996) Accounts of health and illness: Dilemmas and representations. Sociol. Health Illness 18(2):220–240.

Schwartz C, Meisenhelder JB, Ma Y, Reed G (2003) Altruistic social interest behaviors are associated with better mental health. Psychosomatic Medicine 65(5):778–785.

Shumaker SA, Bronwell A (1984) Toward a theory of social support: Closing conceptual gaps. J. Soc. Issues 40(4):11–33.

Singh PV, Tan Y, Youn N (2011) A hidden Markov model of developer learning dynamics in open source software projects. Inform. Systems Res. 22(4):790–807.

Slevin ML, Nichols SE, Downer SM, Wilson P, Lister TA, Arnott S, Maher J, Souhami RL, Tobias JS, Goldstone AH, Cody M (1996) Emotional support for cancer patients: What do patients really want? British J. Cancer 74(8):1275–1279.

Swan M (2009) Emerging patient-driven health care models: An examination of health social networks, consumer personalized medicine and quantified self-tracking. Internat. J. Environ. Res. Public Health 6(2):492–525.

Tessler R, Mechanic D (1978) Psychological distress and perceived health status. J. Health Soc. Behav. 19(3):254–262.

Wanless D (2002) Securing our future health: Taking a long-term view. HM Treasury, London.

Weinberg N, Schmale JD, Uken J, Wessel K (1995) Computermediated support groups. Soc. Work Groups 17(4):43–54.

Weiss RS (1974) The provisions of social relationships. Rubin Z, ed. Doing Unto Others (Prentice-Hall, Englewood Cliffs, NJ), 17–26.

Wellman B, Wortley S (1990) Different strokes from different folks: Community ties and social support. Amer. J. Sociol. 96(3): 558–588.

Wills TA (1985) Supportive functions of interpersonal relationships. Cohen S, Syme SL, eds. Social Support and Health (Academic Press, New York), 61–82.

Wooldrige JM (2001) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Wortman C, Conway T (1985) The role of social support in adaptation and recovery in physical illness. Wortman C, Conway T, eds. Social Support and Health (Academic Press, New York), 281–302.

Wright K (2000) Computer-mediated social support, older adults, and coping. J. Comm. 50(3):100–118.

Ziebland S, Chapple A, Dumelow C, Evans J, Prinjha S, Rozmovits L (2004) How the Internet affects patients’ experience of cancer: A qualitative study. British Medical J. 328(7439):564–569.
