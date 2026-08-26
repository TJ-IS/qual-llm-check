---
otero_id: 12736
otero_key: "B64MJW4S"
title: "Effects of the design of mobile security notifications and mobile app usability on users’ security perceptions and continued use intention"
authors: "Dezhi Wu; Gregory D. Moody; Jun Zhang; Paul Benjamin Lowry"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103235"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Effects of the Design of Mobile Security Notifications and Mobile App Usability on Users’ Security Perceptions and Continued-Use Intention

Dezhi Wu, Gregory D. Moody, Jun Zhang, Paul Benjamin Lowry

![](/api/attachments/B64MJW4S/fulltext/images/2e13fdbb0819853a6e48011f2cdef810a1aa7135ac7c3934857f1edddb904456.jpg)

PII: S0378-7206(17)30131-3

DOI: https://doi.org/10.1016/j.im.2019.103235

Reference: INFMAN 103235

To appear in: Information & Management

Received Date: 13 February 2017

Revised Date: 6 November 2019

Accepted Date: 11 November 2019

Please cite this article as: Wu D, Moody GD, Zhang J, Lowry PB, Effects of the Design of Mobile Security Notifications and Mobile App Usability on Users’ Security Perceptions and Continued-Use Intention, Information and amp; Management (2019), doi: https://doi.org/10.1016/j.im.2019.103235

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# Effects of the Design of Mobile Security Notifications and Mobile App Usability on Users’ Security Perceptions and Continued-Use Intention

Dezhi Wu Department of Integrated Information Technology

University of South Carolina

Columbia, SC, USA

dezhiwu@cec.sc.edu

Gregory D. Moody Department of MIS

Lee School of Business

University of Nevada

Las Vegas, NV, USA

greg.moody@unlv.edu

Jun Zhang School of Management

University of Science and Technology of China

Hefei, China

jzhang90@ustc.edu.cn

\*Paul Benjamin Lowry Pamplin College of Business

Virginia Tech

Blacksburg, VA, USA

Paul.Lowry.PhD@gmail.com

\*submitting and corresponding author

## Highlights

 Apps users routinely ignore security notifications

 Apps users have flawed perception on safety of apps

 We find that disruptive mobile security notifications cause irritation

 Irritation negatively influences users’ perception security and usability

 Security and usability influence apps continuance

## ABSTRACT

The explosive global adoption of mobile applications $( \mathrm { i . e . , a p p s } )$ has been fraught with security and privacy issues. App users typically have a poor understanding of information security; worse, they routinely ignore security notifications designed to increase security on apps. By considering both mobile app interface usability and mobile security notification (MSN) design, we investigate how security perceptions of apps are formed and how these perceptions influence users’ intentions to continue using apps. Accordingly, we designed and conducted a set of controlled survey experiments with 317 participants in different MSN interface scenarios by manipulating the types of MSN interfaces (i.e., high vs. low disruption), the context (hedonic vs. utilitarian scenarios), and the degree of MSN intrusiveness (high vs. low intrusiveness). We found that both app interface usability and the design of MSNs significantly impacted users’ perceived security, which, in turn, has a positive influence on users’ intention to continue using the app. In addition, we identified an important conundrum: disruptive MSNs—a common approach to delivering MSNs—irritate users and negatively influence their perceptions of app security. Thus, our results directly challenge current practice. If these results hold,

current practice should shift away from MSNs that interrupt task performance.

## KEYWORDS

Mobile device; mobile security; human–computer interaction(HCI); mobile applications (apps); perceived security; dual-task interference; mobile security notification (MSN)

## 1. INTRODUCTION

The adoption of mobile devices continues at an unprecedented rate throughout the world, such that it has become common to own multiple mobile devices. Consequently, the use of mobile applications (i.e., apps) has also grown dramatically. As mobile user experiences are increasingly enriched by various customized apps, apps have inevitably come to involve greater security risks (Goode, 2010; Keith et al., 2013). Mobile apps have enabled new and rich functionality, but they also pose security risks to users, because mobile devices contain sensitive and personal data that apps can access, and thus represents a potential security issue. It is crucial to identify mechanisms that can increase users’ mobile security awareness and help them make informed decisions about mobile app security management.

It is of great concern that malicious apps (i.e., apps that access or share more data than is required for the functionality or purpose of the app without the express knowledge of the mobile device owner) are frequently detected in official app repositories by both Apple and Google (Felt et al., 2011; Keith et al., 2013; Zhou et al., 2012). According to Zacks (2018), although malware on personal computers has continuously decreased in recent years, the amount of malware on mobile platforms (including both the iOS and Android platforms) continues to increase rapidly, with an compound annual growth rate of about 125% from 2011 to 2018. In 2019, more than 24,000 malicious mobile apps were detected and blocked every day (Sobers, 2019). Mobile devices, especially those with an Android operating system (OS), are the most vulnerable and most poorly protected computer devices (Harborth et al., 2019).

A key issue in app security is the lack of effective security controls, because traditional controls have not transferred well to the new security and design paradigms of mobile platforms (Rouse, 2012). A related problem is that app users exhibit a serious lack of security awareness (Allam et al., 2014; Goode,

2010; Lu et al., 2008; Mylonas et al., 2013). All app users face issues of data protection and the sharing of data with third parties, but few have access to reliable information about the ramifications of their security choices (Rouse, 2012). According to McDaniel & Enck (2010), most users have little knowledge about app security features. Moreover, apps often request nearly unfettered access to mobile device data, which can easily result in malicious access or unnecessary sharing of private data with third parties (Keith et al., 2013). Because the majority of users have poor mobile security awareness (Mylonas et al., 2013), most users trust apps and their respective branded app stores (e.g., Google Play and Apple’s App Store), regarding them as risk free, and grant all apps access to the data stored on their mobile devices. As a result of this perception, users fail to enable their mobile devices’ security controls and disregard security warnings during app selection and installation (Keith et al., 2013; Rouse, 2012).

Given that users generally have a poor understanding of app and mobile data security, push notifications from apps have emerged to keep users informed of updates and to improve their security awareness (Warren et al., 2014). Mobile security notifications (MSNs), through push technology, have become the main method of alerting users to the presence of incoming calls, messages, emails, and other user activities (Pielot et al., 2014). Although the purpose of MSNs is to keep mobile devices and users upto-date through an event-triggered mechanism in which remote servers “push” information or messages to client apps, MSNs have been shown to irritate users because the notifications interrupt their usual flow of activities (Ochs, 2014; Warner et al., 1998). In many situations, such notifications are unwelcome to app users and ignored or disabled (Felt et al., 2011; Kelley et al., 2012; Modic & Anderson, 2014; Mylonas et al., 2013). They not only fail to increase users’ security awareness, but also backfire because they irritate users by inducing dual-task interference during app usage.

In our research context, MSN-induced dual-task interference refers to the difficulty of paying attention to MSNs while performing other tasks. To carefully process and cope with MSNs, users have to stop their primary tasks on the app. Researchers have explored how notifications can be designed to minimize interruptions of users’ primary tasks (Bailey & Iqbal, 2008; Cutrell et al., 2001; Czerwinski &

Horvitz, 2002; De Vries et al., 2013; Fischer et al., 2010; Garlan et al., 2002; Iqbal & Bailey, 2010; Pielot et al., 2014; Wiberg & Whittaker, 2005). However, in the extant literature, the negative consequences of MSN-induced dual-task interference have not been thoroughly investigated (Dhillon et al., 2016), despite the importance of these consequences. In this study, we empirically examine the negative impact of disruptive MSNs on perceived app security and argue that various MSN designs that interrupt users ongoing primary tasks may not increase users’ perceived security and may even decrease it. We propose that when an app user perceives a higher level of security, they will have stronger intentions to continue using the app. In addition to MSN-related design, we propose that app interface usability is another determinant of users’ perceived app security. We propose a theoretical model of the joint influence of mobile app interface usability and MSNs on users’ perceived security and their intentions to continue using the app.

We test our theoretical model by conducting a 2\*2\*2 factorial experiment, in which the MSN designs were manipulated based on (1) the levels of MSN disruption and (2) the levels of intrusiveness of MSN in (3) two app usage contexts (utilitarian vs. hedonic context). Our proposed model is largely supported by the data analysis results, which support a comprehensive understanding of how MSNs affect users’ perceived security and their intentions to continue using the app.

Our study contributes to the literature by addressing several research gaps. First, this study examines how the design of MSNs and app usability influence users’ security perceptions when users do not have sufficient knowledge to accurately assess the app’s security level. We posit that users rely heavily on explicit cues to make such assessments. Specifically, we identified two determinants of perceived app security: MSN design and app interface usability. If MSNs are user friendly and designed to avoid dual-task interference and if the app interface itself is well designed, users will perceive the app as more secure.

Second, because our paper is among the first empirical studies of mobile app security, we systematically tested an entire set of MSN designs based on the levels of MSN intrusiveness and disruption in a realistic mobile app context. Furthermore, we examined these MSN designs while users were engaged in a dual-task process. This dual-task experimental environment, using the participants’ own devices, makes our MSN designs and testing more realistic, generalizable, and ecologically valid, which are crucial considerations in leading security research (Lowry et al., 2017).

Third, this study identifies an important paradox: the expected MSN design goals may not be achieved due to potential conflicts with the perceptions of mobile users. The common practice of push notifications might actually undermine app security as perceived by the user, not improve it. By designing and examining a set of MSN designs, we found that highly disruptive MSNs can backfire in shaping users’ security perceptions of serious security violations.

## 2. RELATED WORK

## 2.1. Notifications

A notification is “a visual cue, auditory signal, or haptic alert generated by an application or service that relays information to a user outside her current focus of attention” (Iqbal & Bailey, 2008, p. 15:2). Today’s mobile apps use proactive push notifications to inform users, even inactive ones, about new, unattended messages or events (Pielot et al., 2014) through sounds, vibrations, icons, badges on the app’s icons, or auditory-tactile cues, which are core features of many mobile apps. Mobile device users commonly handle many app notifications on a daily basis; Pielot et al. (2014) reported an average of 63.5 mobile notifications per day.

Most research on notifications has focused on information workers in desktop environments, where notifications usually have negative effects on completing primary computer tasks. Czerwinski et al. (2004) found that it is difficult for users to return to a task after being interrupted, whether by calls, push notifications through instant messages, or interactions with colleagues. Cutrell et al. (2001) reported that the negative effect is more pronounced when the task is more cognitively demanding. Leiva et al. (2012) found that phone calls interrupting the use of an app significantly increase the time a user spends completing the initial task. De Vries et al. (2013) showed that depending on the mental workload, a

notification’s level of politeness impacts how irritated and disrupted users feel. This could be particularly problematic in a security context, because the processing of serious security threats may involve higher cognitive demands than does the processing of minor threats.

Notifications have clear benefits and costs. Computer system notifications can be delivered to users instantly, thereby reducing their use of cognitive resources to visually scan or repeatedly check information resources (Iqbal & Bailey, 2010). Research has also reported many other benefits of using notifications in a computer-supported work setting, such as improved peer communication (Czerwinski & Horvitz, 2002), heightened awareness of collaboration activities (Dabbish & Kraut, 2004), and the relay of application assistance at opportune moments (Maes, 1994). Again, the negative effects of notifications include irritating interruptions of users’ ongoing tasks.

Several studies have examined the trade-off between the disruptions and heightened awareness caused by notifications (Czerwinski et al., 2004; Iqbal & Bailey, 2010; Iqbal & Horvitz, 2010; Lin et al., 2013). Many have also reported innovative solutions to design notification systems based on employing a range of amplitudes (Ryu et al., 2008), frequencies (Hwang & Hwang, 2009; Ryu et al., 2008; Yao et al., 2010), vibrations (Saket et al., 2013), vibration directions (Hwang & Hwang, 2009), intensities (White, 2011), and tactile cues (Qian et al., 2009). Iqbal & Bailey (2010) designed and tested a notification system called Oasis, which aligns notification scheduling with the perceptual structure of user tasks and reduces interruptions of desktop computing tasks. Modic & Anderson (2014) examined the various reasons why desktop users often turn off their browser malware warnings, and they provided design guidelines for delivering fewer but more effective security warnings.

## 2.2. Mobile Notifications

Unsurprisingly, as a central feature of today’s mobile apps, notifications now play an even more crucial role in proactively informing users of updates, immediate or upcoming events, and system updates (Weber et al., 2015). Mobile notifications are typically delivered at the moment data are being sent, whether from games, location-based services (Streefkerk et al., 2008), or communication-related apps (Chang & Tang, 2015). Depending on the content of notifications, users may have various perceptions of mobile notifications when they are performing tasks in different contexts. If the app is not perceived as useful, mobile notifications can make users irritated enough to cease using it (Felt et al., 2012). Conversely, if users consider notifications interesting, entertaining, relevant, and actionable (Fischer et al., 2010), they will be more engaged.

Furthermore, in terms of mobile notification design, visual and auditory cues and vibrations may increase user acceptance. Based on a one-week, in situ (i.e., stationary) study, Pielot et al. (2014) reported that regardless of whether or not a mobile device is in silent mode, notifications are typically viewed within minutes. Like desktop notifications, mobile notifications cause cognitive overload, which results in negative emotions and reduced work productivity due to limited resources for focused attention on current tasks (Garlan et al., 2002). Mashhadi et al. (2014) demonstrated that compared to auditory or vibrational cues, visual cues are more effective reminders to return to unread mobile notifications and to quickly deduce the source and importance of these notifications. Moreover, Balebako et al. (2013) observed that mobile device users can be irritated by frequent notifications and experience sounds as more irritating than vibrations. Despite the disruptive nature of notifications, users do appreciate the awareness they facilitate (Iqbal & Horvitz, 2010). Due to the importance of MSNs, this study focuses on visual cues in notification design, because they are the most effective and common approach for notifying mobile device users.

## 2.3. Design of MSNs and User Perceptions

Because apps are widely used in mobile users’ daily routines, the number of security threats to apps is rapidly increasing, including malware, phishing and social engineering, direct attacks by hackers, data communications interception and spoofing, malicious insider actions, and user policy violations (Friedman & Hoffman, 2008). Worse, managing security effectively in mobile environments is a challenge due to a number of technical factors (Oberheide & Jahanian, 2010): (1) the mobility and small size of mobile devices, (2) the inability to take advantage of a mobile platform’s hardware architecture, (3) obscurity between the platforms (mobile vs. fixed environments) and the underdeveloped understanding of how mobile networks function, (4) the sheer number of mobile attacks, which exhibit a wide variety of attack vectors, and (5) mobile device usability issues. App users are exposed to a mindnumbing barrage of complex security services and mechanisms, which can be confusing for users and result in their underutilization to protect personal data. Again, mobile notifications represent the mainstream technique for increasing user awareness of mobile security issues.

Jøsang & Sanderud (2003) suggested making the security services and mechanisms as transparent as possible so that users can easily understand the security process. However, users are often completely oblivious to the security vulnerabilities of their mobile devices, and many users lack an understanding of the security-related services and mechanisms on their mobile devices (McDaniel & Enck, 2010). Although users have a general sense of the harm to which desktop computers can be subjected due to malware, security vulnerabilities, and so on, they often have no such awareness regarding the vulnerability of their mobile devices (Mylonas et al., 2013).

Users desire more fine-grained controls with which to manage their notifications, such as the ability to prioritize notifications depending on their content and source (Shirazi et al., 2014). Similarly, Mashhadi et al. (2014) reported that users want to control notification settings in a way that includes different modalities for notifications of varying priorities. However, they also observed that although users are aware of notification controls, they rarely act to change their settings, for two possible reasons: (1) they do not know how to modify their control settings, and (2) they prefer not to go to the trouble of navigating the system settings. The same user behaviors have been associated with security notifications (Felt et al., 2011; Kelley et al., 2012; Mylonas et al., 2013).

Considering the negative attitudes of app users toward MSNs, stakeholders—including mobile OS designers, app designers, and antivirus program companies—face the challenge of how to design userfriendly MSNs without irritating users and thereby causing them to ignore the notifications. However, the academic understanding of mobile app notifications is limited. Consequently, it is crucial to conduct indepth research to gain a systematic understanding of how the various types of disruptive notifications inform mobile app users’ perceived security and their intentions to continue using the app.

Due to the lack of security education and awareness, app users often make the mistake of disregarding security-related notifications. Without a realistic understanding of the threats inherent in mobile platforms and their apps, users form their own, often misguided, perceptions. Ideally, notifications can inform these perceptions, aligning them with security realities, but little is known about how users’ security perceptions are formed. In this study, we investigate how app interfaces and the design of MSNs impact users’ perceived security and how perceived security, in turn, impacts users’ intentions to continue using an app they perceive as secure or insecure.

Because users form perceptions based on the available cues, we examine apps’ interface usability as a likely source of the cues used to form security perceptions. The related e-commerce research has shown that website interface quality is an important environmental cue from which users form their security beliefs about websites (Chang & Chen, 2009). Mobile device users have even fewer cues and, therefore, less ability to fully evaluate the security level of the apps on their devices, so they must rely instead on the usability of the app interface to form their security perceptions and their intentions to continue using the app. Given the scarcity of cues available in the mobile environment compared to the traditional desktop environment, it is likely that the mobile app interface design and its usability will exert a stronger influence on the formation of users’ perceptions (Botha et al., 2009). Jøsang & Sanderud (2003) maintained that it is critical to design mobile security interfaces in an intuitive and intelligent way; we thus assume that the mobile app interface and users’ perceptions of its usability play important roles in forming users’ perceived security.

## 3. THEORETICAL MODEL

As discussed, app users often do not have enough knowledge or efficacy to accurately assess the security of a mobile app. They rely on multiple observable design elements of the interface to make their assessment. These observable elements and cues include both app interface usability and the design of

## MSN.

Consequently, we first focus on mobile app usability to examine users’ awareness of and ability to respond to various disruptive MSNs. We draw on the Apple Usability Guidelines (Apple Inc., 2013; Venkatesh & Ramesh, 2006) as a usability foundation for our model, which proposes how the usability of an app interface influences users’ security-related perceptions, which in turn influence users’ intentions to continue using the app. This portion of our model provides a practice-infused baseline with which to assess the general usability of an app. Likewise, we adopt validated measures of app interface usability from Hoehle & Venkatesh (2015), in which the direct visual user interface elements relevant to our study include (1) user interface graphics, (2) user interface input, (3) user interface output, and (4) user interface structure.

Given this baseline, we also investigate how disruptive and user-unfriendly MSN designs may decrease users’ security perceptions and inhibit sustained usage of the app. Specifically, we explore how MSNs interrupt users’ cognitive processing and thus irritate them. This portion of the model builds on the research conducted by McCoy et al. (2008), extending their Web-based premises and manipulations to the mobile context. Referencing dual-task interference literature (Navon & Gopher, 1979; Pashler, 1989), we propose that more frequent and disruptive MSNs in the mobile context will lead to more conflicts in processing information, thus causing further user irritation with the app. When notifications interrupt the operations of the mobile device or app and force users to attend to them, they elicit a general sense of dissatisfaction that is likely to have a negative influence on users’ continued use of the app. Figure 1 summarizes our proposed research model, which we explain in more detail in the following section.

## 3.1. The Relationship between App Interface Usability and Perceived Security

Research has explored the importance of mobile security in various contexts, such as mobile ecommerce (Ghosh & Swaminatha, 2001), mobile e-banking (Schierholz & Laukkanen, 2007), and communication with mobile devices (Kindberg et al., 2004). However, the antecedents of perceived security have received less attention, in part because, in most situations, it is difficult for mobile users without advanced knowledge of information technology (IT) security to determine whether an app is secure. According to inference theory, when consumers do not have clear knowledge of product quality and value, relevant environmental cues help them form perceptions and make judgments (Chang & Chen, 2009). For instance, in the context of shopping in physical stores, when consumers do not know the exact

![](/api/attachments/B64MJW4S/fulltext/images/cefebe6496d9fce25e31013c24b0379f30fcdec0b6964a3267f4c151c0d554a5.jpg)  
Figure 1. Proposed Theoretical Model and Hypotheses

quality and real value of a product, they rely on environmental cues such as store layout design, store music style, and the number of employees to form their perceptions of quality and price (Baker et al., 2002). Similarly, previous research has shown that when users perceive systems as having higher quality of interface design, they perceive the systems themselves as being of higher quality (Cyr et al., 2006). When visiting websites for the first time, consumers infer quality and trust partially on the basis of website design artifacts and the cobranding of known quality brands or logos (Lowry et al., 2008; Lowry et al., 2014).

Thus, in our context, when users lack expert knowledge, they leverage heuristic cues. For example, e-commerce research has shown that website interface quality is an important influence on consumers’ perceptions of the security of the website (Chang & Chen, 2009). If the website interface is well designed, consumers may assume that the website is also willing to invest in website security and regard the website as trustworthy. We extend these findings to the mobile security context by proposing that when users perceive an app as being of high quality, they perceive it in a more favorable light and thus as more secure. This proposition aligns with the cognitive psychological theory of attitude consistency, which emphasizes that individuals tend to align beliefs about the same object (i.e., in this case, the app) to avoid inconsistency (Thompson & Zanna, 1995). Traditionally, usability has been broadly regarded as “quality of use” and “a quality aspect of products” (Hassenzahl, 2001, p. 481). Thus, when users believe that app interfaces are of high quality, they will infer that other attributes of the apps are likely to have equally high usability, even without any information to corroborate this belief (Alba & Hutchinson, 1987). In summary, an app that is perceived as having high interface usability will be positively related to users’ perceived security of the app:

H1. A mobile app’s interface usability (consisting of interface graphics, interface input, interface output, and interface structure) is positively related to users’ perceived security of the app.

## 3.2 How Intrusive MSN Design Decreases Users’ Perceived Security

Here, we discuss the negative consequences associated with intrusive and user-unfriendly MSN designs. We argue that if an MSN is poorly designed, it not only negatively affects users’ security behaviors, but also backfires by decreasing users’ security-related perceptions of the app. Next, we explain how the intrusiveness of MSNs arouses the negative emotion of irritation in users, and we then discuss how irritation leads to an attitude change and decreases perceived app security.

## 3.2.1. The relationship between the intrusiveness of app notifications and user irritation

According to research on dual-task interference, humans have a limited capacity to process information as well as a limited ability to perform multiple tasks simultaneously (Jeuris & Bardram, 2016; Navon & Gopher, 1979; Pashler, 1989; Srivastava, 2013). Moreover, when multiple tasks require the same type of information processing resources (e.g., reading articles and writing simultaneously), the task interference will be higher (McCann & Johnston, 1992; Wickens, 1981). Research has suggested that when a secondary task interrupts the performance of a primary task, not only is the person’s task performance

##

diminished, but his or her emotions are negatively affected (Zijlstra et al., 1999); that is, the person gets irritated.

It has also been found that security notifications/alerts interfere with the flow of IT use, especially in the mobile context (Felt et al., 2011; Warner et al., 1998). In view of the limited cognitive resources humans can devote to information processing, Stuijfzand et al. (2016) suggested that the cognitive load of using IT is determined mainly by the amount of information the user needs to process. Further, when the cognitive load is too high, the individual perceives the information as intrusive. Dealing with security notifications requires not only cognitive resources for processing text and graphic information but also hardware resources (from the mobile device) for the presentation of security-related content on a relatively small screen. Thus, an apps’ disruptive MSNs conflict strongly with intended tasks, and the message is perceived as intrusive. Worse, as Warner et al. (1998) found, when users’ typical flow of activity is interrupted by unexpected security messages, which are frequently sent to their mobile devices, users get irritated. Rettie (2001) offered similar findings in a study of flow disruptions during Internet use. McCoy et al. (2008) investigated the conflict between using e-commerce websites and dealing with disruptive pop-ups and inline ads, and they demonstrated a positive link between online ad intrusiveness and user irritation (in their context, intrusiveness referred to the ad appearing without invitation or in an unwelcome fashion, as perceived by the user; irritation was defined as the user’s negative reaction to the ad).

We thus build on the findings of McCoy et al. (2008) to predict that when MSNs are perceived as information or the same type of notification, which represents an interferential secondary task, is likely to exhaust the cognitive resources required for information processing. Individuals are likely to perceive this disruption as a meddling force that disturbs their use of the app (Lee et al., 2013). Following this logic, we propose that when the user perceives a notification as intrusive, they will experience feelings of irritation. Thus,

H2. The perceived intrusiveness of MSNs is positively related to app user irritation.

## 3.2.2 The relationship between user irritation and negative outcomes

Building on the psychological research on attitude change (Petty & Wegener, 1998), we propose that as users’ negative emotions regarding apps increase, their intentions or perceptions regarding the mobile devices will also be negatively affected. Irritation toward e-commerce websites and online ads will negatively affect users’ value perception and their online shopping behaviors (Dehghani et al., 2016). According to Zuwerink & Devine (1996), irritation caused by strong, persuasive messages increases the likelihood of inducing negative attitudes. Thus, when users become irritated by persuasive messages, not only will they be less likely to comply with the message, but they will also be more likely to generate negative affect toward the persuaders. This suggests that in our context, even though app users often understand that the purpose of MSNs is to enhance security and privacy, they still regard MSNs that disrupt their primary tasks as irritating (Balebako et al., 2013). A large body of research on human– computer interaction has concluded that negative affect toward systems use can have wide-ranging negative consequences for various systems perceptions, including performance, satisfaction, usability, and use (Hudlicka, 2003). It is then likely that feelings of irritation resulting from app use will negatively influence users’ perception of app security: In summary,

H3. The feelings of irritation caused by MSNs are negatively related to users’ perceived security of the app.

3.3. The Relationship between Perceived Security and the Intention to Continue Using the App Users of IT have basic needs for information security. As Belanger et al. (2002) pointed out, it is only after users’ concerns for information security have been satisfactorily addressed that they will consider using the technology more often. The relationship between perceived security and user intention has been widely tested in various contexts. For instance, e-commerce researchers have found that users with higher perceived security with respect to the technology are more likely to adopt an e-banking system (Cheng et al., 2006), use an e-commerce platform (Suh & Han, 2003), and purchase from a website (Salisbury et al., 2001). Shin (2010) found that security beliefs are associated with the intention to use social networking sites. In the mobile context, studies have shown that the perceived security of the technology is related to the use of mobile e-banking (Luarn & Lin, 2005), the intention to use the app (Wang et al., 2006), and the intention to use mobile cloud storage services (Arpaci, 2016). We thus propose that when users believe an app is secure, they will have strengthened intentions to continue using the app, because they will assume that a negative future event (e.g., a data breach) is unlikely to occur:

H4. Users’ perceived security of an app is positively related to intentions to continue using it.

## 3.4 Moderation Effects of Utilitarian and Hedonic Use Scenarios

Here, we discuss how utilitarian and hedonic scenarios moderate the influence of irritation on perceived security. In a utilitarian scenario, users are engaged in cognitive tasks such as reading articles and learning (Lowry et al., 2015). In a hedonic scenario, users are engaged in enjoyable tasks such as playing a mobile game, which leads to higher emotional arousal (Liu et al., 2013; Lowry et al., 2013). Moreover, according to Huang & Korfiatis (2015), the emotional process often plays a more salient role in determining users’ attitude and behavior in a hedonic context than it does in a utilitarian context. Thus, in a hedonic context, people tend to have a stronger cognitive response to emotional elements. In our study, when playing a mobile game (hedonic scenario), users will be in a more highly aroused state than in a utilitarian scenario, and their cognitive assessment of app security at this moment will be more emotionally driven.

Consequently, the negative impact of irritation on perceived security will be stronger. By contrast, when reading articles (utilitarian scenario), users are relatively more rational and less emotionally driven than in a hedonic task scenario. Even though the disruptive MSNs irritate them, they are more likely to carefully assess the security level of the app using their existing knowledge and cognitive judgment, and thus less likely to be influenced by irritation. The negative impact of irritation on perceived security will be weaker. We thus hypothesize:

H5. In a hedonic app-use scenario, the negative influence of irritation on perceived security will be stronger than that of a utilitarian app-use scenario.

## 3.5 Moderation Effects of High and Low Disruption of MSNs

We now explain how the degree of MSN disruption moderates the influence of app usability on perceived security. Details of how MSN disruption is operationalized can be found in section 4.2.1, Figure 2, Figure 3, and Appendix A.

As discussed in section 3.1, app interface usability has a positive influence on perceived security, because when perceived interface usability is high, users can more effectively interact with the system. Higher interface usability leads to an increase in the flow of use (Fonseca et al., 2014). As a result, users perceive the app as having a higher interface quality when interface usability is high, and this positive disruptive MSNs may undermine the positive experience brought about by high-quality interface usability. For instance, even when an interface enables effective inputs and outputs, more disruptive MSNs require users to respond to the input and output requests during their app usage. MSNs that entail a high degree of dual-task interference can be disruptive and annoying (Fonseca et al., 2014; Jenkins et al., 2016). In the presence of such poorly designed MSNs, even high-quality interface usability cannot result in effective human–computer interactions; such ineffective interaction in turn are likely to decrease users’ perceptions of interface quality and perceived security. Thus,

H6. In a high-disruption scenario, the positive influence of app interface usability will be weaker than that in a low-disruption scenario.

## 4. RESEARCH METHODOLOGY

## 4.1. Study Design and Pilot Testing

We assessed the efficacy of our theoretical model through a controlled survey experiment in a mobile device setting with eight randomized treatment groups (high vs. low MSN intrusiveness, high vs. low MSN disruption, and hedonic vs. utilitarian scenarios) and two control groups without MSNs (hedonic and utilitarian).<sup>ii</sup> Both hedonic and utilitarian apps were used, because individuals’ behavioral patterns and decision-making may differ between hedonic and utilitarian tasks (Lowry et al., 2013), and we wanted to control for these differences. According to Nasco et al. (2008, p. 989), utilitarian tasks are “cognitively driven” and “reasoning based” activities “in which the person’s motivations are focused on problem solving”; by contrast, hedonic tasks “are primarily characterized by an affective and sensory

experience of aesthetic or sensual pleasure, fantasy, or fun.” Utilitarian tasks require more cognitive resources, so in this context individuals should be more cognitively driven. Conversely, our hedonic task should lead to higher emotional arousal, so the individuals should be more emotionally driven (Nasco et al., 2008; Valacich et al., 2007). Given that our study involves both cognitive and affective factors that can drive individuals’ perceptions and behaviors, we control for both hedonic and utilitarian conditions through our manipulations. In our study, the cognitive element of app interface usability and the affective element may jointly influence users’ security perceptions and continued intention to use; we thus decided to observe the potential differences in utilitarian and hedonic conditions. As suggested by Kim & Sundar (2014, p. 470), adding a manipulation of hedonic/utilitarian tasks can effectively increase the generalizability of the study and the “ecological validity of the experiment.”

Following the work of Lowry et al. (2015), we conducted a survey experiment that allowed subjects to interact with the mobile application in a naturalistic setting on their own mobile device. Although this approach greatly increases the realism of the methodology, it also greatly diminishes the level of control placed on the experiment and does not allow for strict expectations about the resulting manipulation levels (Burton-Jones & Straub Jr, 2006; Gefen et al., 2003a; 2003b). This approach has been used in many information system studies (Burton-Jones & Straub Jr, 2006; Gefen et al., 2003a; 2003b; Lowry et al., 2012; Lowry et al., 2008; Vance et al., 2008). This methodology allowed us to increase the realism and thus the relevance of the study for the participants, which in this case were college students. Specifically, having the participants use their own devices intensified the relevance of the perceived security of their personal data; this would not have been the case with an impersonal laboratory computer.

We also designed randomly applied treatment conditions with different degrees of MSN intrusiveness (i.e., high vs. low) and notification disruptiveness (see Appendix A) in order to create variance in participants’ perceptions of MSN intrusiveness and perceived security and in order to ensure that our findings would be valid under a wide variety of conditions. Information security research based on protection motivation theory has proposed that a message’s level of severity affects the likelihood of whether the recipient will or will not respond (Boss et al., 2015; Burns et al., 2017; Johnston & Warkentin, 2010; Menard et al., 2018; Posey et al., 2015). We thus introduced high- and lowintrusiveness conditions to account for these previously established effects.

To examine our research framework and all hypotheses, we designed and implemented an app security notification system that can be run by various mobile device platforms. The prototype was built using PHP, JavaScript, HTML5, MySQL, and other mobile-responsive technologies. The mobile app user interfaces were pilot tested with 23 participants to ensure that users experienced the same user interfaces across multiple experimental conditions, while either playing a game or reading a Wikipedia article (see Figures 2 and 3). Our design of the utilitarian vs. hedonic conditions was consistent with the definitions of utilitarian and hedonic tasks (Lowry et al., 2015) as well as with the common practice adopted by prior research. According to Huang (2003) and Hollingsworth & Randolph (2015), reading articles and learning are typical utilitarian tasks, whereas playing a game is a typical hedonic task (Lowry et al., 2013; Murray & Bellman, 2011).

Notably, due to the small screen size of a mobile phone and the different frequencies of MSNs pushed to the users’ devices, the captured screenshots often had a slightly different visual appearance, but the primary task backgrounds remained identical while users were scrolling up and down to perform their primary tasks. The MSN system we designed for this study had an automatic function by which it randomly assigned users to different experimental conditions. Based on participant feedback, we improved the system’s interface design and usability before running the official controlled experiments.

## 4.2. Study Procedures and Conditions

As part of the recruitment process, the participants were first instructed by the researchers about the experiment’s procedures in the classroom, and they were then randomly assigned to one of 10 different experimental groups by the experimental server, as shown in Table 1. Not all of our 10 experimental conditions had the same number of participants, for several reasons. First, the server used true random distribution of subjects to conditions; moreover, some subjects had missing or invalid data entries, some were dropped because of Wi-Fi-related issues, and some withdrew from the experiment. We noticed that some subjects became uncomfortable with participating because the MSNs pushed to their mobile phones caused them to perceive a loss of device security. The experiment took participants 15–20 minutes to complete. Before the experiment started, participants were asked to fill out a presurvey about their

Table 1. Summary of Experimental Conditions and Number of Participants

<table><tr><td rowspan="3" colspan="2">Experimental Conditions</td><td colspan="4">MSN Disruption</td><td colspan="2">Control Group (No MSN)</td></tr><tr><td colspan="2">Hedonic App</td><td colspan="2">Utilitarian App</td><td rowspan="2">Hedonic App</td><td rowspan="2">Utilitarian App</td></tr><tr><td>High</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td rowspan="2">MSN Intrusiveness</td><td>High</td><td>43</td><td>25</td><td>32</td><td>39</td><td rowspan="2">17 (not used in SEM analysis)</td><td rowspan="2">29 (not used in SEM analysis)</td></tr><tr><td>Low</td><td>29</td><td>30</td><td>39</td><td>32</td></tr></table>

demographics, background, and mobile experiences. After they finished the experiment, they were asked to complete an exit questionnaire that assessed the study’s major constructs. All participants used mobile phones equipped with our custom-built MSN app, which was designed to manipulate the experimental conditions (see screenshots in Figures 2 and 3 and Appendix A).

<table><tr><td>Baseline condition (without MSN)</td><td>High disruption</td><td>Low disruption</td></tr><tr><td></td><td></td><td></td></tr></table>

Figure 2. MSNs Displayed in Hedonic Scenarios

<table><tr><td>Baseline condition (without MSN)</td><td>High disruption</td><td>Low disruption</td></tr></table>

![](/api/attachments/B64MJW4S/fulltext/images/f3200f028bfd70496465db5db18d45a24cbd92cee608ed3f23f73e24be1cfc35.jpg)  
Figure 3. MSNs Displayed in Utilitarian Scenarios

## 4.2.1 Manipulating the degree of MSN disruption

As shown in Figures 2 and 3 and Appendix A, a combination of (1) different user interfaces of MSNs and (2) different message contents were designed to manipulate the degrees of MSN disruption. In the highly disruptive treatment condition, participants were exposed to MSNs with high-threat content. They were unable to continue with any other task until they read the entire MSN and then approved or disapproved of the exemption requested by the app. They were then returned to the screen they had been using before the MSN appeared. In the low-disruption condition, an MSN with low-threat content was pushed to participants’ mobile phones; these MSNs were minimally inserted (i.e., as a watermarked banner) into the working. According to Zijlstra et al. (1999), the extent to which a secondary task interrupts a primary task (i.e., the degree of disruption) can be evaluated by the extent to which one can continue performing the primary task. If the disruptiveness is low, one can continue to perform (1) task-related actions and (2) supportive actions associated with the primary task. If the disruptiveness is high, one cannot continue to perform the primary task and must react by performing (3) interruption-handling actions or (4) irrelevant actions.

## 4.2.2 Manipulating the utilitarian and hedonic use conditions

We also designed two different scenarios for this experiment: a hedonic environment (i.e., an open-source mobile game) and a utilitarian environment (i.e., a Wikipedia article on the subject “computers”). In line with the definitions of utilitarian and hedonic tasks proposed by Nasco et al. (2008), Huang (2003) and Hollingsworth & Randolph (2015) suggested that learning on the basis of reading an article is a typical utilitarian task, and Murray & Bellman (2011) suggested that playing a game is a typical hedonic task. We designed our utilitarian and hedonic conditions based on these definitions and on design examples from prior literature. In both scenarios, the participants were exposed to MSNs with different levels of perceived disruptiveness and threat. See Figures 2 and 3 and Appendix A for screenshots of these treatments.

## 4.2.3 Manipulating the perceived intrusiveness of MSNs

To manipulate perceived intrusiveness, MSNs were presented to each treatment group of users with a different frequency. Prior research on pop-up ads has suggested that the frequency of pop-up messages has a significant influence on perceived message intrusiveness; thus, this treatment was widely adopted in experimental designs of studies on pop-up ads to manipulate the intrusiveness of pop-up messages (Li & Meeds, 2005; Li et al., 2002; Rejón-Guardia & Martínez-López, 2014; Ying et al., 2009). In this study, users in the high-intrusiveness groups received an MSN every 40 seconds that reminded them to cope with the potential threats; those in the low-intrusiveness groups received an MSN every 80 seconds.

## 4.3. Data Collection

For the main experimental data collection, we recruited 317 participants from six universities in the United States. The corresponding institutional review boards approved the study, and all participants gave their informed consent to participate. The students’ incentive for participating in this study was to earn extra credit in their courses. Our sample consisted of 216 males (68.6%) and 99 females (31.4%), and the gender of two participants was unspecified (0.6%). The average age was 24.3 years (SD = 6.0 years). The average number of years completed at a university was 2.1 $( \mathrm { S D } = 1 . 0 \mathrm { y e a r } )$ . The participants identified themselves either as part-time students (n = 70, 22.2%), full-time students only (n = 111, 35.1%), or working full-time while being students $\left( n = 1 3 5 , 4 2 . 7 \% \right)$ , with one unspecified (n = 1, 0.3%). Among these 317 participants, 271 were assigned to the eight (2\*2\*2) treatment groups (groups 1–8). The other

46 participants were assigned to the control groups (groups 9–10); they did not receive any MSNs, so they were ineligible to answer questions related to MSNs (e.g., perceived intrusiveness and perceived irritation). The two control groups were set up to ensure that the general presence of MSNs did not induce any confounding effects beyond the 2\*2\*2 treatments. Specifically, app usability was an important predictor of perceived security and continued intention to use; therefore, a comparison between the eight treatment groups and two control groups indicates that the general presence of MSN itself does not affect perceived app usability (see Appendix C). In this way, the general presence of MSNs in our experiment is intended not to induce any confounding effects on the outcome variables, so all influences on perceived app security and continued intention are induced by our 2\*2\*2 treatments.

After the main experimental data collection, supplementary data collection was conducted for the purpose of manipulation checks. A total of 101 study participants were recruited, and they participated in the supplementary manipulation check study. The use of a supplementary sample for manipulation checks is a common practice, because it is assumed that effective manipulations can be replicated (Edwards et al., 2002).

All the experimental data collection procedures are presented in Appendix D.

## 4.4. Measures

After investigating possible validated constructs from the existing theoretical and empirical literature, we obtained the reliable measurement items based on scales from the literature. All construct items were reflectively measured with multiple items on 7-point Likert-type scales. The mobile device user interface constructs were app graphics, user interface input/output, and structure, as adapted from Hoehle & Venkatesh (2015). Notably, that study included six constructs in its instrument development, two of which we did not include (i.e., app design and app utility), because they are not directly related to our mobile security study context. The four constructs we included represented the visual interface design elements of the app. Each of these constructs was a reflective subconstruct of mobile app usability design, and we modeled each of them as separate yet related constructs to explore how the various design

elements of the mobile interface influenced our model. The intention-to-continue measurement items were adapted from the unified technology acceptance model (Venkatesh et al., 2003). The perceived security construct was based on that of Anderson & Agarwal (2010), and the intrusiveness-of-MSN and irritation constructs were adapted from McCoy et al. (2008). The details are presented in Appendix B.

## 5. ANALYSES

## 5.1. Manipulation Checks

For the supplementary sample, 101 study participants were recruited and participated in our manipulation check study. They were randomly assigned to the eight (2\*2\*2) treatment conditions, ensuring an adequate sample size for the supplementary manipulation check.<sup>iii</sup> The participants were asked to answer a set of manipulation checks, as shown in Appendix B. Following the standard procedures for manipulation checks, a series of independent samples t-tests were conducted (Yin et al., 2017).

## 5.1.1 Manipulation check on the MSN disruption treatment

Participants in the manipulation check study were asked to rate the following statement: “When the security warning appeared, I could continue using the app without responding to the warning message” (1 = strongly disagree, 7 = strongly agree) (Jenkins et al., 2016). Based on our manipulation check analysis, we found that the high-MSN-disruption groups (mean = 4.97, SD = 2.01) rated this statement significantly higher than the low-MSN-disruption group $( \mathrm { m e a n } = 2 . 7 9 , \mathrm { S D } = 1 . 7 5 )$ , with $t = 5 . 7 4 8$ and $p =$ 0.001. These results demonstrated that our manipulation of MSN disruption was successful.

## 5.1.2 Manipulation check on the utilitarian/hedonic treatment

To check our manipulation of the utilitarian/hedonic treatment, participants were asked to rate the following two statements: when using the app, they were required to complete some tasks (1) for fun (a hedonic purpose) (0 = completely disagree, 100 = completely agree) or (2) for learning (a utilitarian purpose) (0 = completely disagree, 100 = completely agree) (Siddiqui et al., 2018).

The results of the independent samples t-test on this manipulation suggested that participants in the game conditions had a higher hedonic purpose (mean = 68.72, SD = 31.62) than those in the

Wikipedia conditions $( \mathrm { m e a n } = 4 0 . 2 3 , \mathrm { S D } = 3 7 . 9 3 )$ , with $t = 3 . 8 2 8$ and $p = 0 . 0 0 1$ . Conversely, participants in the Wikipedia conditions had a higher utilitarian purpose $( \mathrm { m e a n } = 7 3 . 7 4 , \mathrm { S D } = 3 1 . 4 0 )$ than those in the game conditions $( \mathrm { m e a n } = 3 6 . 5 0 , \mathrm { S D } = 3 4 . 2 1 )$ ), with $t = 5 . 5 2 8$ and $p = 0 . 0 0 1$ . The above results confirmed that our manipulation of the utilitarian and hedonic app use conditions was successful.

## 5.1.3 Manipulation check on MSN intrusiveness

The manipulation check on MSN intrusiveness was conducted by comparing the degrees of perceived MSN intrusiveness of the high-intrusiveness and low-intrusiveness groups. The results of the independent samples t-test indicate that participants in the high-intrusiveness groups $( \mathrm { m e a n } = 5 . 8 3 , \mathrm { S D } = 1 . 2 3 )$ reported a significantly higher degree of perceived MSN intrusiveness than those in the low-intrusiveness groups $( \mathrm { m e a n } = 4 . 4 4 , \mathrm { S D } = 1 . 4 7 )$ , with a $t = 5 . 1 5 8$ and $p = 0 . 0 0 1$ . Thus, we concluded that our manipulation successfully created variance in users’ perceived MSN intrusiveness. See Table 2.

Table 2. Summary Results of Manipulation Checks Manipulation check on high/low MSN disruption

<table><tr><td colspan="7">Manipulation check on high/low MSN disruption</td></tr><tr><td rowspan="2">Degree of disruption</td><td colspan="2">High-disruption group (mean/SD)</td><td colspan="2">Low-disruption group (mean/SD)</td><td>t-statistic</td><td>p-value</td></tr><tr><td>4.97</td><td>2.01</td><td>2.79</td><td>1.75</td><td>5.748</td><td>0.001</td></tr><tr><td colspan="7">Manipulation check on utilitarian/hedonic treatment</td></tr><tr><td></td><td colspan="2">Hedonic condition (mean/SD)</td><td colspan="2">Utilitarian condition (mean/SD)</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Hedonic purpose</td><td>68.72</td><td>31.62</td><td>40.23</td><td>37.93</td><td>3.828</td><td>0.001</td></tr><tr><td>Utilitarian purpose</td><td>36.50</td><td>34.21</td><td>73.74</td><td>31.40</td><td>5.528</td><td>0.001</td></tr><tr><td colspan="7">Manipulation check on high/low MSN intrusiveness</td></tr><tr><td rowspan="2">Perceived intrusiveness</td><td colspan="2">High-intrusiveness condition (mean/SD)</td><td colspan="2">Low-intrusiveness condition (mean/SD)</td><td>t-statistic</td><td>p-value</td></tr><tr><td>5.83</td><td>1.23</td><td>4.44</td><td>1.47</td><td>5.158</td><td>0.001</td></tr></table>

## 5.2. Measurement Reliability and Validity

Again, participants in the two control groups (group 9 and group 10) did not answer manipulated checks related to MSNs (e.g., perceived intrusiveness and perceived irritation), because they did not receive any MSNs in their experimental conditions. Accordingly, the control group data were not included in the following analysis, which used structural equation modeling (SEM). All the following analyses on manipulation checks and hypothesis testing were conducted using samples in groups 1–8 (271 valid responses), which exactly follow our 2\*2\*2 manipulations. Data analyses were performed using AMOS

22. This is a common approach to analyzing controlled survey experimental data using SEM estimations (Angst & Agarwal, 2009; Boss et al., 2015), and it was especially effective in demonstrating the underlying mechanisms of how the treatment variables influence the outcome variables. Before manipulation checks and hypothesis testing, the reliability, convergent validity, and discriminant validity of measures were assessed using AMOS 22. A few measurement items were dropped in the confirmatory factor analysis to improve the measurement validity and model fit. For the final measurement model, the model fit was good: $\chi ^ { 2 } { } _ { 3 9 1 } = 6 0 1 . 2 0 0 ; \nonumber$ $\chi ^ { 2 } / \mathrm { d f } = 1 . 5 3 8 $ ; $\mathrm { C F I } = 0 . 9 7 3 $ ; $\mathrm { T L I } = 0 . 9 7 0 $ ; RMSEA = 0.045; PCLOSE $= 1 . 0 0 0$ . Convergent validity was supported by large and standardized loadings for all constructs $( p <$ .001) and t-values that exceeded statistical significance. Convergent validity was also supported by calculating the ratio of factor loadings to their respective standard errors, which exceeded |10.0| $( p <$ .001). The summary statistics of the constructs are presented in Table 3.

Table 3. Correlations among Latent Constructs

<table><tr><td>Constructs</td><td>Mean</td><td>SD</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1. App interface usability</td><td>4.22</td><td>1.38</td><td>0.888</td><td></td><td></td><td></td><td></td></tr><tr><td>2. Continued intention to use</td><td>3.68</td><td>1.88</td><td>0.371</td><td>0.911</td><td></td><td></td><td></td></tr><tr><td>3. Perceived intrusiveness</td><td>4.96</td><td>1.59</td><td>-0.065</td><td>-0.107</td><td>0.791</td><td></td><td></td></tr><tr><td>4. Perceived security</td><td>2.50</td><td>1.45</td><td>0.400</td><td>0.522</td><td>-0.313</td><td>0.851</td><td></td></tr><tr><td>5. Irritation</td><td>5.04</td><td>1.57</td><td>-0.118</td><td>-0.193</td><td>0.713</td><td>-0.324</td><td>0.797</td></tr></table>

Note: The average variance extracted squared is indicated by the bolded numbers on the diagonal.

Discriminant validity was tested by showing that the measurement model had a significantly better model fit than a competing model with a single latent construct and was better than all other competing models in which pairs of latent constructs were joined. The $\mathsf { \pmb { \chi } } ^ { 2 }$ differences between the competing models (omitted for the sake of brevity) were significantly larger than that of the original model, as suggested by factor loadings, modification indices, and residuals (Marsh & Hocevar, 1985). In summary, these tests confirmed convergent and discriminant validities.

Construct reliability was assessed using Cronbach’s α. All measures exceeded 0.70 (see Table 4), suggesting strong reliability. Reliability was also supported because the average variance extracted (Hair et al., 2006) exceeded 0.50 for all factors. Furthermore, common method bias was assessed via procedures outlined in Podsakoff et al. (2012), indicating that common method bias was not a concern for this study.<sup>iv</sup>

Table 4. Construct Reliability and Validity Scores

<table><tr><td>Construct</td><td>Cronbach&#x27;s α</td><td>AVE</td><td>CR</td></tr><tr><td>1. App interface usability</td><td>0.933</td><td>0.788</td><td>0.937</td></tr><tr><td>2. Continued intention to use</td><td>0.861</td><td>0.830</td><td>0.951</td></tr><tr><td>3. Perceived intrusiveness</td><td>0.890</td><td>0.625</td><td>0.868</td></tr><tr><td>4. Perceived security</td><td>0.910</td><td>0.725</td><td>0.913</td></tr><tr><td>5. Irritation</td><td>0.964</td><td>0.635</td><td>0.873</td></tr></table>

## 5.3. Hypothesis Testing for the Direct Effects in H1–H4

We first tested the baseline model, which included only the direct relationships (H1–H4). The structural model was assessed using AMOS 22. Common fit indices showed that the model fit was acceptable: χ<sup>2</sup><sub>394</sub> $= 6 1 0 . 0 8 5 ; \gamma ^ { 2 } / \mathrm { d f } = 1 . 5 4 8 ; { \mathrm { C F I } } = 0 . 9 7 2 ; { \mathrm { T L I } } = 0 . 9 6 9 ; { \mathrm { R M S E A } } = 0 . 0 4 5 ; { \mathrm { P C L O S E } } = 1 . 0 0 0 . { \mathrm { A l l ~ c o n t r o l } }$ variables (age, gender, level of education, work status, Internet experience, and previous privacy victim status) were nonsignificant predictors of our dependent variables. Figure 4 shows the results of the baseline model test, which are detailed in Table 5. As indicated in Figure 4 and Table 5, the model explained approximately 51.4% of variance in irritation, 24.4% of variance in perceived security, and 28.1% of variance in continued intention to use.

Figure 4. Hypothesis Testing for H1–H4  
![](/api/attachments/B64MJW4S/fulltext/images/8b4a7cb88bfff6c56609a66392658affb45fe73fa19ae142bacf0cc94ffe2a8c.jpg)  
\*\*\* p < .001, \*\* p < .01, \* p < .05, ns = nonsignificant

Table 5. Hypothesis Testing for H1–H4

<table><tr><td>Hypothesis</td><td>β</td><td>S.E.</td><td>t</td><td>p</td><td>Support?</td></tr><tr><td>H1: Mobile app interface usability → Perceived security</td><td>0.380</td><td>0.065</td><td>5.993</td><td>&lt; 0.001</td><td>Yes</td></tr><tr><td>H2: Perceived intrusiveness of MSN → Irritation</td><td>0.717</td><td>0.096</td><td>9,280</td><td>&lt; 0.001</td><td>Yes</td></tr><tr><td>H3: Irritation → Perceived security</td><td>-0.296</td><td>0.057</td><td>-4.741</td><td>&lt; 0.001</td><td>Yes</td></tr><tr><td>H4: Perceived security → Continued intention to use</td><td>0.530</td><td>0.084</td><td>8.358</td><td>&lt; 0.001</td><td>Yes</td></tr></table>

First, we confirmed that the perceived security of the mobile app was influenced by users’ cognitive evaluation of the mobile interface design $( \beta = 0 . 3 8 0 , p < . 0 0 1$ , H1 supported). With a betterdesigned interface and improved interface usability, users perceived the app as more secure. Second, we found that user-unfriendly MSNs decreased perceived security due to the negative emotion of irritation. Perceived MSN intrusiveness significantly influenced irritation $( \beta = 0 . 7 1 7 , p < . 0 0 1$ 1, H2 supported), which in turn resulted in a decrease in the perceived security of the app $( \beta = - 0 . 2 9 6 , p < . 0 0 1 , \mathrm { H } 3$ supported). Finally, perceived app security was a crucial determinant of continued intention to use the app $( \beta = 0 . 5 3 0 , p < . 0 0 1$ , H4 supported).

## 5.4. Hypothesis Testing for Moderation Effects

Next, we tested the contingent factors that moderate the influence of interface usability and MSN-induced irritation on perceived security (H5 and H6).

## 5.4.1 Contingent effect of utilitarian and hedonic scenarios

H5 suggested that the negative effect of irritation is more pronounced in hedonic scenarios than in utilitarian scenarios. To test this hypothesis, we performed the multigroup analysis in AMOS (chi-square test) as well as the differences-in-slopes test suggested by Chin (2000). The multigroup analysis results are summarized in Table 6. The $\chi ^ { 2 }$ differences between the constrained models (for the two subgroups, the coefficient of the relationship irritat onperceived security was constrained to be equal) were significantly larger than that of the original unconstrained model, suggesting that the effect proposed in H3 was significantly different across the utilitarian and hedonic scenarios.

Table 6. Multigroup Analysis for Utilitarian and Hedonic Scenarios

<table><tr><td rowspan="2">Relationship</td><td colspan="2">Unstandardized coefficients (in unconstrained model)</td></tr><tr><td>Utilitarian scenario</td><td>Hedonic scenario</td></tr><tr><td>H1: Mobile app interface usability →Perceived security</td><td>0.44</td><td>0.32</td></tr><tr><td>H2: Perceived intrusiveness of MSN →</td><td>0.96</td><td>0.91</td></tr></table>

<table><tr><td>H3: Irritation → Perceived security</td><td>-0.10</td><td>-0.51</td></tr><tr><td>H4: Perceived security → Continued intention to use</td><td>0.83</td><td>0.65</td></tr></table>

Parameter constraint: coefficients in H3 are equal across utilitarian and hedonic scenarios.  
$\Delta \chi ^ { 2 } / \Delta \mathrm { d f } = 1 7 . 5 7 0 , p < . 0 0 1$ . The influence of irritation perceived security is significantly different across utilitarian and hedonic scenarios.

Next, we performed the differences-in-slopes test based on Chin (2000) using the formula below:

$$
t = \frac {\text {Path} _ {\text {sample} _ {1}} - \text {Path} _ {\text {sample} _ {2}}}{\left[ \sqrt {\frac {(m - 1) ^ {2}}{(m + n - 2)} * S . E _ {\cdot s a m p l e 1} ^ {2} + \frac {(n - 1) ^ {2}}{(m + n - 2)} * S . E _ {\cdot s a m p l e 2} ^ {2}} \right] * \left[ \sqrt {\frac {1}{m} + \frac {1}{n}} \right]}
$$

The results summarized in Table 7 indicate that the negative influence of irritation on perceived security was stronger in hedonic scenarios; thus, H5 was supported.

Table 7. Differences-in-Slopes Test for Utilitarian and Hedonic Scenarios

<table><tr><td></td><td>Hedonic scenario</td><td>Utilitarian scenario</td></tr><tr><td>Sample Size</td><td>129</td><td>142</td></tr><tr><td>Regression Weight</td><td>-0.51</td><td>-0.10</td></tr><tr><td>Standard Error (S.E.)</td><td>0.065</td><td>0.068</td></tr><tr><td>t-statistic</td><td>4.355</td><td></td></tr><tr><td>p-value (two-tailed)</td><td>&lt; 0.001</td><td></td></tr></table>

## 5.4.2 Contingent effect of high/low disruption of MSNs

We then tested H6 using the procedures described in the previous section, and the results are listed in Tables 8 and 9. H6 was supported, because significant differences were found in the coefficients for highand low-disruption conditions. Along with the increase in MSN disruption, the positive influence of interface usability on perceived security was weakened.

Table 8. Multigroup Analysis for High- and Low-Disruption Conditions

<table><tr><td rowspan="2">Relationship</td><td colspan="2">Unstandardized coefficients (in unconstrained model)</td></tr><tr><td>High disruption</td><td>Low disruption</td></tr><tr><td>H1: Mobile app interface usability → Perceived security</td><td>0.30</td><td>0.54</td></tr><tr><td>H2: Perceived intrusiveness of MSN → Irritation</td><td>1.04</td><td>0.85</td></tr><tr><td>H3: Irritation → Perceived security</td><td>-0.30</td><td>-0.26</td></tr><tr><td>H4: Perceived security → Continued intention to use</td><td>0.70</td><td>0.80</td></tr></table>

Parameter constraint: coefficients in H1 are equal across utilitarian and hedonic scenarios.  
Δχ<sup>2</sup>/Δdf = 4.371, p = .037. The influence of interface usability  perceived security is significantly different across high- and low-disruption conditions.

Table 9. Differences-in-Slopes Test for High- and Low-Disruption Conditions

<table><tr><td></td><td>High disruption</td><td>Low disruption</td></tr><tr><td>Sample Size</td><td>145</td><td>126</td></tr><tr><td>Regression Weight</td><td>0.30</td><td>0.54</td></tr><tr><td>Standard Error (S.E.)</td><td>0.089</td><td>0.072</td></tr><tr><td>t-statistic</td><td>2.064</td><td></td></tr><tr><td>p-value (two-tailed)</td><td>0.040</td><td></td></tr></table>

## 6. DISCUSSION

Daily use of mobile devices is becoming a common way of life throughout the world. Although substantial research has investigated the adoption of mobile apps, little research has focused on how to make app users aware of the security issues inherent in mobile apps. Given the increasing pervasiveness of app security issues, this is particularly problematic. Although most users are aware of how viruses,

phishing attacks, and other malware can affect their personal computers and laptops, few are aware of similar threats for mobile apps, know how to cope with them, or take them seriously. Worse, users routinely ignore security push notifications from apps, which are essential to improving users’ app security. Users also tend to find these notifications irritating, which may negatively influence their intentions to use the app.

Accordingly, the purpose of this study is to explain and predict how mobile app interface usability and the design of MSNs influence users’ perceived security and their intentions to continue using apps. We conducted a set of survey experiments in which 317 smartphone users were exposed to different levels of security-related notifications and various levels of security-related threats on their own devices. Our results indicate that (1) interface usability and perception of MSN designs are two important determinants of perceived security of the mobile app, (2) perceived mobile app security is positively associated with continued intention to use the mobile app, and (3) the influences of interface usability and irritation on perceived security are contingent on the context of use (utilitarian/hedonic) and the MSN type (high disruption/low disruption).

## 6.1. Contributions to Research, Theory, and Practice

Our first key contribution is to explain the influence of MSNs on users’ security perception and continued-use intentions. During the experiment, we were able to verify the existence of user irritation caused by the MSNs while users were performing a primary task. Our findings also challenge the current literature, because they indicate that our mobile users’ decision-making process regarding whether they would continue to use the mobile app was not easily influenced by their negative emotions caused by the disruptive MSNs. This suggests that our participants (and possibly today’s mobile users more generally) were more rational than most of the current literature claims. We thus call for research that more accurately characterizes today’s mobile user behaviors, especially with respect to mobile security.

We validated our proposition that the disruptive effects of MSNs can backfire and decrease users’ perceived security. This is a counterintuitive and novel notion that requires further study. That is, we

found that if MSNs are not properly designed, they can reduce users’ security perceptions. In this study, we explain the antecedents of users’ perceived security of apps, considering that most users do not have the professional knowledge with which to accurately evaluate security levels. We thus conclude that if designers can more clearly present notification information and increase the ease of information entry, app users’ security perceptions will be enhanced. Given the scant empirical research on mobile security, no study to date has reported antecedents that increase users’ perceived security of mobile devices or their accompanying apps. Moreover, this is the first empirical study to systematically examine whether MSNs designed to disrupt the user decrease perceived security.

Our second key contribution is to explain the effect of mobile app usability on perceived app security and continued intention to use the app. The extant security literature has a major research gap concerning how mobile device users evaluate their apps in terms of perceived security. In this study, we found that when users lack sufficient knowledge to accurately evaluate app security, their assessments rely heavily on explicit heuristic cues. We found that app users evaluate mobile app security based on perceived app interface usability. Much research has demonstrated the importance of perceived ease of use and perceived usefulness with respect to continued use; however, the influence of app interface usability and MSN design on mobile security perceptions had not been systematically explored prior to this study. The latter finding is particularly interesting, because evidence from other studies shows that app users have low security awareness and routinely dismiss MSNs. However, despite this lack of awareness and attention to notifications, our results show that if users merely perceive the app as secure, they will be more likely to continue using it. Given the lack of user training on security, app designers could focus instead on environmental cues (such as usability design) to increase security perceptions, because users are most likely to rely on such cues to make credibility and trust assessments. If our results hold, practitioners should focus their usability interaction design on four key dimensions: graphics, input, output, and structure.

As a third contribution, we extended our findings by comparing the coefficients of different conditions (hedonic vs. utilitarian scenarios and high- vs. low-disruption notifications). The different degrees of threat violation and message intrusiveness can effectively induce different degrees of dual-task interference and can create sufficient variation in mobile app users’ emotional states (e.g., irritation) and security-related perceptions. As a result, we were able to observe the differences in users’ cognitive and emotional responses to MSNs when they were subjected to different degrees of disruption. Moreover, we found that the negative impact of intrusive MSNs and the negative emotions caused by dual-task interference are more pronounced in hedonic scenarios than in utilitarian scenarios. This comparison not only increases the generalizability of our conclusions but also provides insights into task–technology fit that enhance the understanding of MSN design.

To illustrate, although MSNs are important in fostering app users’ security awareness, when MSNs interrupt the typical workflow of app users, they feel even less secure; our results show a decrease in perceived security. By examining how users perceived low- and high-disruption notifications across different app usage scenarios, we developed a practical guideline of focusing on low-disruption notifications rather than high- or no-disruption notifications. Given the predominance of highly disruptive notifications that require an action from the user to proceed, this finding has strong practical implications, because users perceive such notifications as indications that the app is less secure. Even if the notification focuses on how the app is blocking a malicious attempt or attack, users still experience a decrease in perceived security, which then further reduces their intention to continue using the app. Thus, app designers should focus on conveying information through MSNs by means of a less disruptive method, which would increase users’ perceived security and support their intention to continue using the app. As an example, MSNs with high threats should be pushed less frequently to minimize the disruptions to users’ primary tasks. Instead of fully controlling the entire smartphone screen to disable users’ current primary tasks, we suggest using less-intrusive visual or audio cues (such as highlights, alarm tones, or similar “nudges”).

## 6.2. Limitations and Future Research

Our study had several limitations that suggest promising research opportunities. First, the generalizability of our conclusions was limited by our use of students and by our experimental design. On the one hand, a student sample was acceptable for this study because students are heavy app users. We also followed recent guidelines for enhancing ecological validity (which is distinct from generalizability and crucial to security research) (Lowry et al., 2017) by having the participants use their own devices, which made the security concerns, threats, and irritation more realistic than using laboratory devices. On the other hand, differences may exist between students, professionals, and older consumers in terms of security awareness, perceived security, and what constitutes an irritating disruption. In fact, given that millennials and post-millennials are the most tech-savvy generation and the generation most prone to multitasking, it is possible that the more disruptive notifications cause them more irritation than other populations, but this has not been empirically studied.

Second, we adopted an experimental approach that engaged app users in several different scenarios. Unsurprisingly, the study results were partially influenced by the specific app and notification messages we provided. Our experiments could be substantially improved by the addition of a user attention check, which would ask participants to answer questions about whether they noticed any disruptions during the experimental period. This could be particularly useful, because users in lowviolation conditions in the current study did not have to act in response to the MSNs pushed to their mobile phones.

In addition, to enhance ecological validity, it is also crucial to expand this study into business environments in future research (Lowry et al., 2017). This would fit naturally with our study, because the bring-your-own-device (BYOD) work trend poses a threat to organizational security (Allam et al., 2014). Many other aspects of security could be explored, such as mobile security policy, offensive security, network security architecture, intrusion detection and prevention systems, honeypots, and data breaches.

Although this study compared high- and low-security violation conditions, high- and lowdisruption notifications, and hedonic and utilitarian conditions, future research should examine more individual-level factors that could influence the outcomes. Such factors could include individual traits, cultural differences, self-efficacy, security awareness, and different types of mobile devices. Given that we have shown the importance of irritation in this setting, we surmise that other recent research on the further role of positive psychology (Burns et al., 2017), and positive and negative emotions in security settings (Burns et al., 2019; D’Arcy & Lowry, 2019), could be particularly useful to consider. This is particularly compelling in our context as emotions and system design interact, and these can affect security perceptions (and subsequent behaviors) positively or negatively.

Likewise, future research should explore whether notification type corresponds to the degree of threat that is broadcast via the notification and whether outcomes improve if users can better assess the level of threats. For example, highly threatening notifications may produce better outcomes if they are highly disruptive, even though users find such disruptiveness irritating. Similarly, it might be better for low-threat notifications to be less disruptive. This implies that differentiating and customizing the design of MSNs in various contexts may improve the design of today’s apps.

Our findings also demonstrated the importance of MSNs in increasing users’ security awareness. This idea could be expanded into mobile security training that uses various security scenarios to teach app users to make sound decisions regarding the use of their mobile devices in the workplace. This practice may be beneficial to businesses as well as individual app users.

Finally, we showed that app interface design and security-related notifications influence users’ perceived security. Thus, future research could refine apps or MSNs not only to enhance mobile security interface design but also to increase user security awareness. Furthermore, we cannot ignore the fact that poorly designed notifications can cause user irritation, which negatively affects users’ perceived security. To advance knowledge in this area, we call for MSN-design research that further differentiates levels of MSN intrusiveness by examining the designs of malicious and regular low-intrusive MSNs and their impacts on user behaviors. Thus, researchers should carefully consider the design of MSNs customized to different mobile devices, different users, and different security contexts (Ochs, 2014).

## 7. CONCLUSION

In this study, we proposed that two important app design artifacts strongly influence users’ perceived security and intentions to continue using the app: mobile app interface usability and the design of MSNs. Drawing on the literature on dual-task interference and attitude change, we explored how negative perceptions caused by disruptive designs can interfere with the flow of activity during app use and decrease perceived security and the intention to continue using the app. Our model’s results provide an opportunity for future research to explore the underlying mechanisms of and influences on perceived security in different situations. Moreover, future research could investigate the security compliance and coping behaviors associated with security-related designs, which this study did not address.

## REFERENCES

Alba, J. W. & Hutchinson, J. W. (1987). Dimensions of consumer expertise. Journal of Consumer Research, 13(4), 411-454.

Allam, S., Flowerday, S. V., & Flowerday, E. (2014). Smartphone information security awareness: A victim of operational pressures. Computers & Security, 42(May), 56-65.

Anderson, C. L. & Agarwal, R. (2010). Practicing safe computing: A multimethod empirical examination of home computer user security behavioral intentions. MIS Quarterly, 34(3), 613-643.

Angst, C. M. & Agarwal, R. (2009). Adoption of electronic health records in the presence of privacy concerns: The elaboration likelihood model and individual persuasion. MIS Quarterly, 33(2), 339-370.

Apple Inc. (2013). User Experience Guidelines. Retrieved June 4, 2014, from https://developer.apple.com/library/mac/documentation/userexperience/conceptual/applehiguideli nes/UEGuidelines/UEGuidelines.html

Arpaci, I. (2016). Understanding and predicting students' intention to use mobile cloud storage services. Computers in Human Behavior, 58(150-157.

Bailey, B. P. & Iqbal, S. T. (2008). Understanding changes in mental workload during execution of goaldirected tasks and its application for interruption management. ACM Transactions on Computer-Human Interaction, 14(4), 1-28.

Baker, J., Parasuraman, A., Grewal, D., & Voss, G. B. (2002). The influence of multiple store environment cues on perceived merchandise value and patronage intentions. Journal of Marketing, 66(2), 120-141.

Balebako, R., Jung, J., Lu, W., Cranor, L. F., & Nguyen, C. (2013). 'Little brothers watching you': Raising awareness of data leaks on smartphones, Proceedings of the Ninth Symposium on Usable Privacy and Security (1-14). Newcastle, UK: ACM.

Belanger, F., Hiller, J. S., & Smith, W. J. (2002). Trustworthiness in electronic commerce: the role of privacy, security, and site attributes. Journal of Strategic Information Systems, 11(3), 245-270.

Boss, S., Galletta, D., Lowry, P. B., Moody, G. D., & Polak, P. (2015). What do systems users have to fear? Using fear appeals to engender threats and fear that motivate protective security behaviors. MIS Quarterly, 39(4), 837-864.

Botha, R. A., Furnell, S. M., & Clarke, N. L. (2009). From desktop to mobile: Examining the security experience. Computers & Security, 28(3), 130-137.

Burns, A. J., Roberts, T. L., Posey, C., & Lowry, P. B. (2017). Examining the influence of organizational insiders’ psychological capital on information security threat and coping appraisals. Computers in Human Behavior, 68(March), 190-209.

Burns, A. J., Roberts, T. L., Posey, C., & Lowry, P. B. (2019). The adaptive roles of positive and negative emotions in organizational insiders’ engagement in security-based precaution taking. Information Systems Research, 2019(forthcoming).

Burton-Jones, A. & Straub Jr, D. W. (2006). Reconceptualizing system usage: An approach and empirical test. Information Systems Research, 17(3), 228-246.

Chang, H. H. & Chen, S. W. (2009). Consumer perception of interface quality, security, and loyalty in electronic commerce. Information & Management, 46(7), 411-417.

Chang, Y.-J. & Tang, J. C. (2015). Investigating mobile users' ringer mode usage and attentiveness and responsiveness to communication, Proceedings of the 17th International Conference on Human-Computer Interaction with Mobile Devices and Services (6-15). Copenhagen, Denmark: ACM.

Cheng, T., Lam, D. Y., & Yeung, A. C. (2006). Adoption of internet banking: An empirical study in Hong Kong. Decision Support Systems, 42(3), 1558-1572.

Chin, W. W. (2000). Frequently Asked Questions - Partial Least Squares & PLS-Graph, from http://discnt.cba.uh.edu/chin/plsfaq.htm

Cutrell, M., Czerwinski, E., & Horvitz, E. (2001). Notification, disruption, and memory: Effects of messaging interruptions on memory and performance. In M. Hirose (Ed.), Proceedings of Human-computer Interaction: INTERACT'01: IFIP TC. 13 International Conference on Human-Computer Interaction (263-269). Tokyo, Japan: IOS Press.

Cyr, D., Head, M., & Ivanov, A. (2006). Design aesthetics leading to m-loyalty in mobile commerce. Information & Management, 43(8), 950-963.

Czerwinski, M. & Horvitz, E. (2002). An investigation of memory for daily computing events, In X. Faulkner, J. Finlay & F. Détienne (Eds.), People and Computers XVI - Memorable Yet Invisible: Proceedings of HCI 2002 (229-245). London: Springer London.

Czerwinski, M., Horvitz, E., & Wilhite, S. (2004). A diary study of task switching and interruptions, Proceedings of the Conference on Human Factors in Computing Systems (175-182). Vienna, Austria: ACM.

D’Arcy, J. & Lowry, P. B. (2019). Cognitive-affective drivers of employees’ daily compliance with information security policies: A multilevel, longitudinal Study. Information Systems Journal, 29(1), 43-69.

Dabbish, L. & Kraut, R. E. (2004). Controlling interruptions: Awareness displays and social motivation for coordination, Proceedings of the 2004 ACM Conference on Computer Supported Cooperative Work (182-191). Chicago, IL.

De Vries, R. A. J., Lohse, M., Winterboer, A., Groen, F. C. A., & Evers, V. (2013). Combining social strategies and workload: A new design to reduce the negative effects of task interruptions, CHI '13 Extended Abstracts on Human Factors in Computing Systems (175-180). Paris, France: ACM.

Dehghani, M., Niaki, M. K., Ramezani, I., & Sali, R. (2016). Evaluating the influence of YouTube advertising for attraction of young customers. Computers in Human Behavior, 59(June), 165-172.

Dhillon, G., Oliveira, T., Susarapu, S., & Caldeira, M. (2016). Deciding between information security and usability: Developing value based objectives. Computers in Human Behavior, 61(August), 656- 666.

Edwards, S. M., Li, H., & Lee, J.-H. (2002). Forced Exposure and Psychological Reactance: Antecedents and Consequences of the Perceived Intrusiveness of Pop-Up Ads. Journal of Advertising, 31(3), 83-95.

Felt, A. P., Egelman, S., & Wagner, D. (2012). I've got 99 problems, but vibration ain't one: a survey of smartphone users' concerns, Proceedings of the Second ACM Workshop on Security and Privacy

in Smartphones and Mobile Devices (33-44). Raleigh, NC: ACM.

Felt, A. P., Finifter, M., Chin, E., Hanna, S., & Wagner, D. (2011). A survey of mobile malware in the wild, 1st ACM Workshop on Security and Privacy in Smartphones and Mobile Devices (3-14). Chicago, IL: ACM.

Fischer, J. E., Yee, N., Bellotti, V., Good, N., Benford, S., & Greenhalgh, C. (2010). Effects of content and time of delivery on receptivity to mobile interruptions, Proceedings of the 12th International Conference on Human Computer Interaction with Mobile Devices and Services (103-112). Lisbon, Portugal: ACM.

Fonseca, D., Martí, N., Redondo, E., Navarro, I., & Sánchez, A. (2014). Relationship between student profile, tool use, participation, and academic performance with the use of Augmented Reality technology for visualized architecture models. Computers in Human Behavior, 31(February), 434-445.

Friedman, J. & Hoffman, D. V. (2008). Protecting data on mobile devices: A taxonomy of security threats to mobile computing and review of applicable defenses. Information Knowledge Systems Management, 7(1/2), 159-180.

Garlan, D., Siewiorek, D. P., Smailagic, A., & Steenkiste, P. (2002). Project Aura: Toward distractionfree pervasive computing. IEEE Pervasive Computing, 1(2), 22-31.

Gefen, D., Karahanna, E., & Straub, D. W. (2003a). Inexperience and experience with online stores: The importance of TAM and trust. IEEE Transactions on Engineering Management, 50(3), 307-321.

Gefen, D., Karahanna, E., & Straub, D. W. (2003b). Trust and TAM in online shopping: An integrated model. MIS Quarterly, 27(1), 51-90.

Ghosh, A. K. & Swaminatha, T. M. (2001). Software security and privacy risks in mobile e-commerce. Communications of the ACM, 44(2), 51-57.

Goode, A. (2010). Managing mobile security: How are we doing? Network Security, 2010(2), 12-15.

Hair, J. F., Tatham, R. L., Anderson, R. E., & Black, W. (2006). Multivariate Data Analysis (Vol. 6). Upper Saddle River, NJ: Pearson Prentice Hall.

Harborth, D., Hatamian, M., Tesfay, W. B., & Rannenberg, K. (January 8-11, 2019). A two-pillar approach to analyze the privacy policies and resource access behaviors of mobile augmented reality applications. Paper presented at the Proceedings of the 52nd Hawaii International Conference on System Sciences, Maui, HI,

Hassenzahl, M. (2001). The effect of perceived hedonic quality on product appealingness. International Journal of Human-Computer Interaction, 13(4), 481-499.

Hoehle, H. & Venkatesh, V. (2015). Mobile application usability: Conceptualization and instrument development. MIS Quarterly, 39(2), 435-472.

Hollingsworth, C. L. & Randolph, A. B. (2015). Using NeuroIS to better understand activities performed on mobile devices, In Information Systems and Neuroscience (213-219): Springer.

Huang, G.-H. & Korfiatis, N. (2015). Trying Before Buying: The Moderating Role of Online Reviews in Trial Attitude Formation Toward Mobile Applications. International Journal of Electronic Commerce, 19(4), 77-111.

Huang, M.-H. (2003). Designing website attributes to induce experiential encounters. Computers in Human Behavior, 19(4), 425-442.

Hudlicka, E. (2003). To feel or not to feel: The role of affect in human–computer interaction. International Journal of Human-Computer Studies, 59(1–2), 1-32.

Hwang, J. & Hwang, W. (2009). Vibration perception and excitatory direction for haptic devices. Journal of Intelligent Manufacturing, 22(1), 17-27.

Iqbal, S. T. & Bailey, B. P. (2008). Effects of intelligent notification management on users and their tasks, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (93-102). Florence, Italy: ACM.

Iqbal, S. T. & Bailey, B. P. (2010). Oasis: A framework for linking notification delivery to the perceptual structure of goal-directed tasks. ACM Transactions on Computer-Human Interaction, 17(4), 1-28.

Iqbal, S. T. & Horvitz, E. (2010). Notifications and awareness: A field study of alert usage and preferences, Proceedings of the 2010 ACM Conference on Computer Supported Cooperative Work (27-30). Savannah, GA: ACM.

Jenkins, J. L., Anderson, B. B., Vance, A., Kirwan, C. B., & Eargle, D. (2016). More harm than good? How messages that interrupt can make us vulnerable. Information Systems Research, 27(4), 880- 896.

Jeuris, S. & Bardram, J. E. (2016). Dedicated workspaces: Faster resumption times and reduced cognitive load in sequential multitasking. Computers in Human Behavior, 62(September), 404-414.

Johnston, A. C. & Warkentin, M. (2010). Fear appeals and information security behaviors: An empirical study. MIS Quarterly, 34(3), 549-566.

Jøsang, A. & Sanderud, G. (2003). Security in mobile communications: challenges and opportunities, Proceedings of the Australasian Information Security Workshop Conference on ACSW Frontiers 2003, Volume 21 (43-48): Australian Computer Society.

Keith, M. J., Thompson, S. C., Hale, J., Lowry, P. B., & Greer, C. (2013). Information disclosure on mobile devices: Re-examining privacy calculus with actual user behavior. International Journal of Human-Computer Studies, 71(12), 1163-1173.

Kelley, P. G., Consolvo, S., Cranor, L. F., Jung, J., Sadeh, N., & Wetherall, D. (2012). A conundrum of permissions: Installing applications on an Android smartphone, In Financial Cryptography and Data Security: Lecture Notes in Computer Science (68-79). Heidelberg, Germany: Springer.

Kim, K. J. & Sundar, S. S. (2014). Does screen size matter for smartphones? Utilitarian and hedonic effects of screen size on smartphone adoption. Cyberpsychology, Behavior, and Social Networking, 17(7), 466-473.

Kindberg, T., Sellen, A., & Geelhoed, E. (2004). Security and trust in mobile interactions: A study of users’ perceptions and reasoning, In N. Davies, E. Mynatt & I. Siio (Eds.), UbiComp 2004: Ubiquitous Computing (Vol. 3205, 196-213). Heidelberg, Germany: Springer

Lee, D., Chung, J. Y., & Kim, H. (2013). Text me when it becomes dangerous: Exploring the determinants of college students’ adoption of mobile-based text alerts short message service. Computers in Human Behavior, 29(3), 563-569.

Leiva, L., Böhmer, M., Gehring, S., & Krüger, A. (2012). Back to the app: the costs of mobile application interruptions, Proceedings of the 14th International Conference on Human-Computer Interaction with Mobile Devices and Services (291-294). San Francisco, CA: ACM.

Li, C. & Meeds, R. (2005). Different forced-exposure levels of internet advertising: An experimental study on pop-up ads and interstitials. Paper presented at the Proceedings of the 2005 Conference of the American Academy of Advertising, East Lansing, MI, 200-207.

Li, H., Edwards, S. M., & Lee, J.-H. (2002). Measuring the intrusiveness of advertisements: Scale development and validation. Journal of Advertising, 31(2), 37-47.

Lin, B. C., Kain, J. M., & Fritz, C. (2013). Don’t interrupt me! An examination of the relationship between intrusions at work and employee strain. International Journal of Stress Management, 20(2), 77-94.

Liu, D., Li, X., & Santhanam, R. (2013). Digital games and beyond: What happens when players compete. MIS Quarterly, 37(1), 111-124.

Lowry, P. B., Dinev, T., & Willison, R. (2017). Why security and privacy research lies at the centre of the information systems (IS) artefact: Proposing a bold research agenda. European Journal of Information Systems, 26(6), 546-563.

Lowry, P. B., Gaskin, J., & Moody, G. D. (2015). Proposing the multimotive information systems continuance model (MISC) to better explain end-user system evaluations and continuance intentions. Journal of the Association for Information Systems, 16(7), 515-579.

Lowry, P. B., Gaskin, J., Twyman, N. W., Hammer, B., & Roberts, T. L. (2013). Taking "fun and games" seriously: Proposing the hedonic-motivation system adoption model (HMSAM). Journal of the Association for Information Systems, 14(11), 617-671.

Lowry, P. B., Moody, G., Vance, A., Jensen, M., Jenkins, J., & Wells, T. (2012). Using an elaboration likelihood approach to better understand the persuasiveness of website privacy assurance cues for online consumers. Journal of the Association for Information Science and Technology, 63(4), 755-776.

Lowry, P. B., Vance, A., Moody, G., Beckman, B., & Read, A. (2008). Explaining and predicting the impact of branding alliances and web site quality on initial consumer trust of e-commerce web sites. Journal of Management Information Systems, 24(4), 199-224.

Lowry, P. B., Wilson, D. W., & Haig, W. L. (2014). A picture is worth a thousand words: Source credibility theory applied to logo and website design for heightened credibility and consumer trust. International Journal of Human-Computer Interaction, 30(1), 63-93.

Lu, J., Liu, C., Yu, C.-S., & Wang, K. (2008). Determinants of accepting wireless mobile data services in China. Information & Management, 45(1), 52-64.

Luarn, P. & Lin, H.-H. (2005). Toward an understanding of the behavioral intention to use mobile banking. Computers in Human Behavior, 21(6), 873-891.

Maes, P. (1994). Agents that reduce work and information overload. Communications of the ACM, 37(7), 30-40.

Marsh, H. W. & Hocevar, D. (1985). Application of confirmatory factor analysis to the study of selfconcept: First- and higher order factor models and their invariance across groups. Psychological Bulletin, 97(3), 562-582.

Mashhadi, A., Mathur, A., & Kawsar, F. (2014). The myth of subtle notifications, Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing: Adjunct Publication (111-114). Seattle, WA: ACM.

McCann, R. S. & Johnston, J. C. (1992). Locus of the single-channel bottleneck in dual-task interference. Journal of Experimental Psychology: Human Perception and Performance, 18(2), 471-484.

McCoy, S., Everard, A., Polak, P., & Galletta, D. F. (2008). An experimental study of antecedents and consequences of online ad intrusiveness. International Journal of Human-Computer Interaction, 24(7), 672-699.

McDaniel, P. & Enck, W. (2010). Not so great expectations: Why application markets haven't failed security. IEEE Security & Privacy, 8(5), 76-78.

Menard, P., Warkentin, M., & Lowry, P. B. (2018). The impact of collectivism and psychological ownership on protection motivation: A cross-cultural examination. Computers & Security, 75(June), 147-166.

Modic, D. & Anderson, R. (2014). Reading this may harm your computer: The psychology of malware warnings. Computers in Human Behavior, 41(December), 71-79.

Murray, K. B. & Bellman, S. (2011). Productive play time: the effect of practice on consumer demand for hedonic experiences. Journal of the Academy of Marketing Science, 39(3), 376-391.

Mylonas, A., Kastania, A., & Gritzalis, D. (2013). Delegate the smartphone user? Security awareness in smartphone platforms. Computers & Security, 34(May), 47-66.

Nasco, S. A., Kulviwat, S., Kumar, A., Bruner, I., & Gordon, C. (2008). The CAT model: Extensions and moderators of dominance in technology acceptance. Psychology & Marketing, 25(10), 987-1005.

Navon, D. & Gopher, D. (1979). On the economy of the human-processing system. Psychological Review, 86(3), 214-255.

Oberheide, J. & Jahanian, F. (2010). When mobile is harder than fixed (and vice versa): demystifying security challenges in mobile environments, Proceedings of the Eleventh Workshop on Mobile Computing Systems and Applications (43-48). Annapolis, MD: ACM.

Ochs, S. (2014). Meet the company that's making push notifications smarter. Macworld, 31(6), 30.

Pashler, H. (1989). Dissociations and dependencies between speed and accuracy: Evidence for a twocomponent theory of divided attention in simple tasks. Cognitive Psychology, 21(4), 469-514.

Petty, R. E. & Wegener, D. T. (1998). Attitude change: Multiple roles for persuasion variables, In The Handbook of Social Psychology (323-390). New York, NY: McGraw-Hill.

Pielot, M., Church, K., & Oliveira, R. d. (2014). An in-situ study of mobile phone notifications, Proceedings of the 16th International Conference on Human-Computer Interaction with Mobile Devices and Services (233-242). Toronto, ON, Canada: ACM.

Podsakoff, P. M., MacKenzie, S. B., & Podsakoff, N. P. (2012). Sources of method bias in social science research and recommendations on how to control it. Annual Review of Psychology, 63(January), 539-569.

Posey, C., Roberts, T. L., & Lowry, P. B. (2015). The impact of organizational commitment on insiders’ motivation to protect organizational information assets. Journal of Management Information Systems, 32(4), 179-214.

Qian, H., Kuber, R., & Sears, A. (2009). Towards identifying distinguishable tactons for use with mobile devices, Proceedings of the 11th International ACM SIGACCESS Conference on Computers and Accessibility (257-258). Pittsburgh, PA: ACM.

Rejón-Guardia, F. & Martínez-López, F. J. (2014). Online advertising intrusiveness and consumers’ avoidance behaviors, In F. J. Martínez-López (Ed.), Handbook of Strategic e-Business Management (565-586). Berlin, Heidelberg: Springer Berlin Heidelberg.

Rettie, R. (2001). An exploration of flow during Internet use. Internet Research: Electronic Networking Applications and Policy, 11(2), 103-113.

Rouse, J. (2012). Mobile devices – the most hostile environment for security? Network Security, 2012(3), 11-13.

Ryu, J., Jung, J., & Choi, S. (2008). Perceived magnitudes of vibrations transmitted through mobile device, Symposium on Haptic Interfaces for Virtual Environments and Teleoperator Systems 2008 (139-140). Reno, NV.

Saket, B., Prasojo, C., Huang, Y., & Zhao, S. (2013). Designing an effective vibration-based notification interface for mobile phones, Proceedings of the 2013 Conference on Computer Supported Cooperative Work (1499-1504). San Antonio, TX: ACM.

Salisbury, W. D., Pearson, R. A., Pearson, A. W., & Miller, D. W. (2001). Perceived security and World Wide Web purchase intention. Industrial Management & Data Systems, 101(4), 165-177.

Schierholz, R. & Laukkanen, T. (2007). Internet vs mobile banking: Comparing customer value perceptions. Business Process Management Journal, 13(6), 788-797.

Shin, D.-H. (2010). The effects of trust, security and privacy in social networking: A security-based approach to understand the pattern of adoption. Interacting with Computers, 22(5), 428-438.

Shirazi, A. S., Henze, N., Dingler, T., Pielot, M., Weber, D., & Schmidt, A. (2014). Large-scale assessment of mobile notifications, Proceedings of the 32nd Annual ACM Conference on Human Factors in Computing Systems (3055-3064). Toronto, Ontario, Canada: ACM.

Siddiqui, R. A., Monga, A., & Buechel, E. C. (2018). When intertemporal rewards are hedonic, larger units of wait time boost patience. Journal of Consumer Psychology, 28(4), 612-628.

Sobers, R. (2019). 60 Must-Know Cybersecurity Statistics for 2019. Retrieved April 13, 2019, from https://www.varonis.com/blog/cybersecurity-statistics/

Srivastava, J. (2013). Media multitasking performance: Role of message relevance and formatting cues in online environments. Computers in Human Behavior, 29(3), 888-895.

Streefkerk, J. W., Esch-Bussemakers, M. P. v., & Neerincx, M. A. (2008). Field evaluation of a mobile location-based notification system for police officers, Proceedings of the 10th International Conference on Human Computer Interaction with Mobile Devices and Services (101-108). Amsterdam, The Netherlands: ACM.

Stuijfzand, B. G., van der Schaaf, M. F., Kirschner, F. C., Ravesloot, C. J., van der Gijp, A., & Vincken, K. L. (2016). Medical students' cognitive load in volumetric image interpretation: Insights from human-computer interaction and eye movements. Computers in Human Behavior, 62(September), 394-403.

Suh, B. & Han, I. (2003). The impact of customer trust and perception of security control on the acceptance of electronic commerce. International Journal of Electronic Commerce, 7(3), 135-

161.

Thompson, M. M. & Zanna, M. P. (1995). The conflicted individual: Personality-based and domainspecific antecedents of ambivalent. Journal of Personality, 63(2), 259-288.

Valacich, J. S., Parboteeah, D. V., & Wells, J. D. (2007). The online consumer's hierarchy of needs. Communications of the ACM, 50(9), 84-90.

Vance, A., Elie-Dit-Cosaque, C., & Straub, D. W. (2008). Examining trust in information technology artifacts: The effects of system quality and culture. Journal of Management Information Systems, 24(4), 73-100.

Venkatesh, V., Morris, M. G., Gordon, B. D., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.

Venkatesh, V. & Ramesh, V. (2006). Web and wireless site usability: Understanding differences and modeling use. MIS Quarterly, 30(1), 181-206.

Wang, Y. S., Lin, H. H., & Luarn, P. (2006). Predicting consumer intention to use mobile service. Information Systems Journal, 16(2), 157-179.

Warner, J. H. R., Miller, S., Jennings, K., Lundsgaarde, H., Pincetl, P., Robinson Jr, E. N., et al. (1998). Clinical event management using push technology--implementation and evaluation at two health care centers, Proceedings of the AMIA Symposium (106-110): American Medical Informatics Association.

Warren, I., Meads, A., Srirama, S., Weerasinghe, T., & Paniagua, C. (2014). Push notification mechanisms for pervasive smartphone applications. IEEE Pervasive Computing, 13(2), 61-71.

Weber, D., Shirazi, A. S., & Henze, N. (2015). Towards smart notifications using research in the large, Proceedings of the 17th International Conference on Human-Computer Interaction with Mobile Devices and Services Adjunct (1117-1122). Copenhagen, Denmark: ACM.

White, T. L. (2011. Last updated). The perceived urgency of tactile patterns: Human Research and Engineering Directorate, Army Research Laboratory, ARL-TR-5557. Retrieved

Wiberg, M. & Whittaker, S. (2005). Managing availability: Supporting lightweight negotiations to handle interruptions. ACM Transactions on Computer-Human Interaction, 12(4), 356-387.

Wickens, C. D. (1981). Processing Resources in Attention, Dual Task Performance, and Workload Assessment. Fort Belvoir, VA: Defense Technical Information Center.

Yao, H.-Y., Grant, D., & Cruz, M. (2010). Perceived vibration strength in mobile devices: The effect of weight and frequency. IEEE Transactions on Haptics, 3(1), 56-62.

Yin, D., Bond, S. D., & Zhang, H. A. N. (2017). Keep your cool or let it out: Nonlinear effects of expressed arousal on perceptions of consumer reviews. Journal of Marketing Research, 54(3), 447-463.

Ying, L., Korneliussen, T., & Grønhaug, K. (2009). The effect of ad value, ad placement and ad execution on the perceived intrusiveness of web advertisements. International Journal of Advertising, 28(4), 623-638.

Zacks, A. (2018). Malware Statistics, Trends and Facts in 2019. Retrieved April 13, 2019, from https://www.safetydetective.com/blog/malware-statistics/

Zhou, Y., Wang, Z., Zhou, W., & Jiang, X. (2012). Hey, you, get off of my market: Detecting malicious apps in official and alternative Android markets, 19th Network and Distributed System Security Symposium (NDSS'12). San Diego, CA: Internet Society.

Zijlstra, F. R. H., Roe, R. A., Leonora, A. B., & Krediet, I. (1999). Temporal factors in mental work: Effects of interrupted activities. Journal of Occupational & Organizational Psychology, 72(2), 163-185.

Zuwerink, J. R. & Devine, P. G. (1996). Attitude importance and resistance to persuasion: It's not just the thought that counts. Journal of Personality and Social Psychology, 70(5), 931-944.

## Authors’ Bios

Dr. Dezhi Wu (dezhiwu@cec.sc.edu) is an associate professor in the Department of Integrated Information Technology, University of South Carolina, Columbia, SC, USA. She explores how users interact with computers, the Internet, robotics and smart devices, as well as other emerging technologies, to accomplish their goals. Her passion also extends to creating innovative and cutting-edge interfaces and designing transformative experiences that fill the gaps between users and today's evolving technologies. Her research has been widely published in the Computers in Human Behavior, Information & Management, Communications of the Association for Information Systems, Journal of Information Systems Security, Computers & Education, IEEE Internet Computing, and others in addition to ICIS, HICSS, AMCIS, PACIS and HCII conference proceedings. She served as the Chair for AIS SIGHCI (http://sighci.org/) and is currently serving as an advisory board member for the SIGHCI. She regularly chairs the HCI tracks and workshops for several leading conferences including ICIS, AMCIS, PACIS and HCII. She is currently serving as an associate editor for AIS Transactions on Human-Computer Systems.

Dr. Gregory D. Moody (greg.moody@unlv.edu) is currently the Lee Professor of Information Systems in the Management, Entrepreneurship and Technology Department in the Lee Business School at the University of Nevada, Las Vegas and Director of the Graduate MIS program. Her received a Ph.D. from the University of Pittsburgh and a Ph.D. from the University of Oulu. He has published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, JAIS, EJIS, ISJ, and other journals. His interests include IS security and privacy, e-business (electronic markets, trust) and human–computer interaction (Web site browsing, entertainment). He is currently a senior editor for ISJ

and associate editor for AIS Transactions on Human-Computer Interaction (THCI), the previous president of Special Interest Group on Human-Computer Interaction (SIGHCI), and the Managing Editor for THCI.

Dr. Jun Zhang (jzhang90@ustc.edu.cn) is currently an assistant professor in MIS at the International Institute of Finance, School of Management, University of Science and Technology of China. He holds a Ph.D. in information systems from City University of Hong Kong. His research centers on online deviant behaviors, information privacy and security, and IT-enabled health behavior change. His research has been published in journals such as Information Systems Research, Journal of Management Information Systems, and Computers in Human Behavior. He has served as a guest associate editor at the EJIS and an associate editor at ICIS 2018. He has also co-chaired the mini-track of “The Dark Usage of Information Technology” at the Americas Conference on Information Systems (AMCIS) 2019.

Professor Paul Benjamin (paul.lowry.phd@gmail.com) is the Suzanne Parker Thornhill Chair Professor and Eminent Scholar in Business Information Technology at the Pamplin College of Business at Virginia Tech. He is also the BIT Ph.D. program director. He is a former tenured Full Professor at the City University of Hong Kong and The University of Hong Kong. He received his Ph.D. in Management Information Systems from the University of Arizona and an MBA from the Marriott School of Management. He has published 125+ journal articles in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, J. of the AIS, Information System J., European J. of Information System, J. of Strategic IS, J. of IT, Decision Sciences J., Information & Management, and others. He is a department editor at Decision Sciences J. He also is an SE at JMIS, JAIS, and ISJ, and an AE at the EJIS. He has also served multiple times as track co-chair at ICIS, ECIS, and PACIS. His research interests include (1) organizational and behavioral security and privacy; (2) online deviance, online harassment, and computer ethics; (3) HCI, social media, and gamification; and (4) business

analytics, decision sciences, innovation, and supply chains.
