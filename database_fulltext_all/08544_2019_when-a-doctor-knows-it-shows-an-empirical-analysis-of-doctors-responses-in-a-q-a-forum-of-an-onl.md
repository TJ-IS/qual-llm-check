---
otero_id: 8544
otero_key: "C2XM7EED"
title: "When a Doctor Knows, It Shows: An Empirical Analysis of Doctors’ Responses in a Q&A Forum of an Online Healthcare Portal"
authors: "Sandeep Khurana; Liangfei Qiu; Subodha Kumar"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0836"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/C2XM7EED/fulltext/images/5bbffaedc917abd1b0b05ba8231c097cd94c09e91b2b7d51b3c41bfa526afead.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# When a Doctor Knows, It Shows: An Empirical Analysis of Doctors’ Responses in a Q&A Forum of an Online Healthcare Portal

Sandeep Khurana, Liangfei Qiu, Subodha Kumar

To cite this article: Sandeep Khurana, Liangfei Qiu, Subodha Kumar (2019) When a Doctor Knows, It Shows: An Empirical Analysis of Doctors Responses in a Q&A Forum of an Online Healthcare Portal. Information Systems Research

Published online in Articles in Advance 12 Jul 2019

https://doi.org/10.1287/isre.2019.0836

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# When a Doctor Knows, It Shows: An Empirical Analysis of Doctors Responses in a Q&A Forum of an Online Healthcare Portal

Sandeep Khurana,<sup>a</sup> Liangfei Qiu,<sup>b</sup> Subodha Kumar<sup>c</sup>

<sup>a</sup> Indian School of Business, Gachibowli, Hyderabad, Telangana 500032, India; <sup>b</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>c</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122 Contact: Sandeep\_Khurana@isb.edu (SaK); liangfei.qiu@warrington.ufl.edu, http://orcid.org/0000-0002-8771-9389 (LQ) subodha@temple.edu, http://orcid.org/0000-0002-4401-7950 (SuK)

Received: July 6, 2017 Revised: February 15, 2018; September 1, 2018 Accepted: November 12, 2018 Published Online in Articles in Advance: July 12, 2019

https://doi.org/10.1287/isre.2019.0836

Copyright: © 2019 INFORMS

Abstract. Question-and-answer (Q&A) forums are gaining popularity as a user-engagement tool to drive traffic on multiservice portals. In a platform market model, demand-side users seek answers from supply-side users because such answers can indicate value offered, reduce buyer uncertainty, and offer social proof. Analyzing user-generated content on the Q&A forum of a prominent healthcare portal, we find that the introduction of doctors responses has a significant causal impact on demand-side user perception of medical services offered. More importantly, our research suggests that doctors’ specialty, experience, qualifications, transparency in appointment booking, service fees, and response quality moderate the effect of doctors’ Q&A responses on user recommendations. These results demonstrate that because of information asymmetry in healthcare, doctors use thoughtful online responses not only to socially interact with patients but also to signal their expertise.

History: Ram Gopal, Senior Editor; Param Singh, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0836.

Keywords: healthcare • Q&A forums • digital platforms • user-generated content

Let users decide what interests them, encourage them to participate, then sit back and pinch yourself for being allowed into this virtual focus group.

—Mary Fearon

(Forbes Communication Council 2016)

## 1. Introduction

According to a recent survey, when making online purchases, 97% of users trust content produced by other users over other forms of online content (KeyIn 2015). With the rise in online user engagement, the range of formats of user-generated content (UGC) has also increased to meet varied user needs and to sustain their interests. With 57% of B2C marketers expected to increase content marketing budget in 2019 compared to 2018 (Murton Beets and Handley 2018), it is also imperative from a marketers’ viewpoint to offer a variety of options for users to engage through different forums. Question-and-answer (Q&A) forum sites have steadily gained in popularity for more discerning web users because of the quality content hosted on these sites. Q&A forums could be hosted on Q&A-only sites or as user-engagement tools on portals, such as e-commerce sites. As user interest rises, Q&A sites are becoming increasingly domain specific and niche.

Online healthcare Q&A forums are rapidly being embraced by users and professional physicians alike (Lovitt 2016). Patients and other users seek expert opinions, taking advantage of the convenience, anonymity, and low search and transaction costs offered by these forums. Doctors and healthcare service professionals engage with users in an online marketplace not merely for Q&A but also for paid services. Research into user activities on these online Q&A forums, however, is in a nascent stage, and the dynamics of UGC on Q&A forums have not been analyzed empirically. In this research, we attempt to address this important issue.

## 1.1. Motivation

For services delivered through healthcare portals, the user reviews, given the inherent variance and subjectivity involved in experience of services, are being complemented with other user-engagement forums, such as Q&A forums and blogs, to woo users with informed-choice options. In knowledge- or expertise-intensive specialist services, for example, physician selection, such UGC is of interest to stakeholders. Features provided by portals are observed to be increasing as they seek to engage more users and generate more activities. Because this is a recent phenomenon, healthcare portals could gain from research in the area.

In the case of the platform marketplace model, motivations of either side in supplying UGC could vary (Daugherty et al. 2008). Contributors of UGC could be motivated by extrinsic rewards, such as economic or social gains, or intrinsic rewards, such as varying levels of altruism (Poch and Martin 2015). Demand-side users seek content from both sides of the market—from other peers in the form of reviews and from the supply side in the form of indicators of performance, quality, and value. Negative reviews could also be motivated by bad customer experience (Presi et al. 2014) and require careful management. In such light, a Q&A forum that is designed to provide responses to users’ questions could aid supply-side service producers with content requiring lesser management effort.

Figure 1. Research Framework  
![](/api/attachments/C2XM7EED/fulltext/images/b061056136ad514c4a571128138e9f5636b441230c1e41a3535eac36518fe43e.jpg)

The primary healthcare market is regulated in most countries. The delivery of healthcare services is governed by local laws (e.g., in India<sup>1</sup>) that discourage or prohibit promotions by doctors. In the interest of enabling informed decisions by users of such services, Q&A forums and blogs serve as useful supply-side content, reducing information asymmetry. As “uberization” of online markets grows<sup>2</sup> and the marketplace model is extended to sectors and services (Nurvala 2015), sites have an option to create their own user-engagement platform or leverage social networking sites for e-commerce. Increasingly, niche sites seek to provide exclusivity of UGC and exercise greater control over user experience through their own content-sharing platforms. For all these reasons, it is of a marketer’s interest to study forums exchanging UGC (Q&A forums) other than product reviews. Our research fills this gap by investigating the impact of supply-side UGC in a Q&A forum of healthcare portals.

## 1.2. Research Model and Contributions

Research in UGC has centered primarily on analyses of product or service reviews by users. Analyses of such reviews have linked them with purchase intentions and decisions of other users (Chevalier and Mayzlin 2006). Unlike reviews, content in the form of answers by supply-side users to demand-side users of services, however, is joint creation on a digital platform. A direct consequence of this key difference is that the control of the supply side on UGC (their own response) is greater on Q&A forums and, hence, worthy of study. In the case of a platform connecting the two sides of professional services, such content can reduce information asymmetry about the supply side for the demand side. Such a causal role of content jointly created by the two sides has not been explored in prior research. Figure 1 shows our research framework.

The prior literature on the use of information technology (IT) in healthcare has focused mainly on demand-side physician reviews (Gao et al. 2015, Xu et al. 2016). However, from the supply side, the impact of doctors’ responses has not been well understood. Hence, we first explore the focal impact of doctors’ responses on the recommendations provided by patients, which highlights the motivation of doctors in answering patients’ questions for free. We seek to know whether the introduction of the doctors response feature has an impact on the satisfaction level of patients.<sup>3</sup> Responses by a doctor could signal quality and reputation, and hence, it is expected to elicit greater recommendations. Accordingly, we ask (1) what the impact of responses to patients’ questions on recommendations for responding doctors is. It may seem obvious that the introduction of the doctors’ response feature may benefit responding doctors. However, an empirical challenge lies in establishing the causal effect of doctors’ responses because the decision to respond to patients’ question is endogenously determined. In our study, we combine several causal identification strategies to provide a complete understanding of doctors’ responses on Q&A forums. In particular, our data set provides detailed information on user recommendations for a doctor before and after the introduction of the Q&A feature. Doctors who adopt this feature actively engage with users by responding to questions, and such answers (along with questions) show up on the home pages of the doctors. However, the choice to respond is self-selected by doctors in a competitive setting.

Not only is estimating the causal impact of responses to patients’ questions theoretically important, but it also has practical implications. Adoption of the new response feature by doctors and subsequent engagement with patients could be a resource-intensive and time-consuming endeavor. Without quantifying the benefit of responding to patients’ questions, it is not clear whether doctors should embrace and respond to patients’ questions actively.

It is worth noting that our study context of the healthcare industry is unique: the market for medical care is inherently flawed because of asymmetric information (Arrow 1963, Gaynor 1994). Doctors have more information than patients. As a result, doctors can recommend unnecessary care that enhances their incomes even though it may be of no benefit to patients. Doctors might also recommend one drug over another or one medical device over another because of their financial relationships with the producers. Because of their limited knowledge, patients have no reliable way of evaluating the quality of the advice they are getting. Even after the medical service is delivered, patients still may not be able to evaluate the quality of the service.

In this specific healthcare context, the role of doctors online responses becomes important for the following reasons. First, although information asymmetry also exists in other industries, such as hotels and restaurants (Proserpio and Zervas 2017, Kumar et al. 2018), it is less severe. Therefore, doctors use thoughtful online responses not only to socially interact with patients but also to signal their expertise. This strategy is consistent with the signaling literature in game theory (Spence 1973): one party can credibly convey some private information about itself to another party by sending signals. In our context, a good doctor can credibly convey the quality of information about the medical service to patients by providing thoughtful online responses. There are two preconditions for the application of the signaling theory: (1) information asymmetry between a signaler and receiver (in our context, doctors know more than patients) and (2) the potential for divergence or conflict of interest between the signaler and receiver. In our context, doctors may not serve the best interest of patients and benefit from information asymmetry. For example, doctors who own testing facilities or treatment centers may preferentially refer patients to these facilities for unnecessary care and may benefit financially from doing so. Without either of these two conditions, there is no need for signals because the problem is merely one of communication. When these two conditions are satisfied simultaneously, signals have to be used by signalers to prove to receivers their underlying hidden types (in our context, the hidden type is the quality of medical service). If a high-expertise doctor can credibly convey the quality information by providing thoughtful online responses, then the doctor is likely to receive more recommendations from patients. The informational value of signals relies on whether highexpertise doctors can separate themselves from lowexpertise doctors.

Second, information asymmetry may lead some doctors to recommend more treatment than a patient would have chosen had the patient been fully informed. Patients can exert pressure on their doctors by potentially seeking a second opinion in online healthcare Q&A forums (Rochaix 1989).

Third, the Indian healthcare market has unique institutional contexts.<sup>4</sup> In the United States, patients need to see family doctors and then be referred to other specialist doctors. In contrast, in India, many patients need to directly find their specialist doctors in the healthcare market. In principle, the doctor referral system would be more efficient and accurate if patients were triaged by general physicians for correct specialist identification and corresponding referral. However, “the actual practice of referral is entirely different than that is laid down in principle. Anyone can go to any level of [the] health care system without any referral.”<sup>5</sup> In India, an estimated 60%– 75% of specialist referrals are self-referred (Deogaonkar 2004). In addition, the number of family doctors is decreasing in India: over the last 50 years, much of medical care has fragmented into organ-based specialty domains. This trend has become more prominent with the arrival of the “super specialist” and “super specialist hospital” culture over the last three decades (Kumar 2016). Without recommendations from family doctors, online recommendations from other patients become much more important in the decision-making process of a patient. Therefore, responding to patients’ questions is critical in doctors reputation management in our specific context of the Indian healthcare market.

Next, we consider important factors that can moderate the impact of doctors’ responses. More specifically, we examine the following factors: (1) doctors’ specialties, (2) whether an online appointment-booking option is available, (3) service fees, (4) years of experience, and (5) doctor qualifications. For the moderating effect of a doctor’s specialty, we investigate whether a doctor’s specialty is in traditional/alternative medicine (e.g., acupuncture, Ayurveda, homeopath, etc.) or in mainstream medicine (e.g., cardiology, otorhinolaryngology, dermatology, etc.). AYUSH, an acronym for “Ayurveda, Yoga and naturopathy, Unani, Siddha, Sowa-Rigpa, and Homeopathy,” represents the traditional/ alternative medicine recognized by the government of India (Rudra et al. 2017).<sup>6</sup> According to a recent survey conducted by the World Health Organization, 11.7% respondents in India use traditional/alternative medicine as a frequent source of care (Oyebode et al. 2016).

As stated earlier, in our theoretical framework of signaling, doctors’ online responses can be interpreted as a signal of medical-service quality. In signaling theory (Spence 1973), the informational value of a signal comes from the fact that the receiver believes the signal is positively correlated with having greater ability and is difficult for a low-ability signaler to obtain. Therefore, the signal enables the receiver to reliably distinguish high-ability signalers from lowability ones. In our healthcare context, thoughtfu online responses are positively correlated with having greater expertise and are difficult for low-expertise doctors to provide. There are two key equilibrium concepts in signaling: a separating equilibrium versus a pooling equilibrium. In a separating equilibrium, highand low-ability signalers choose different signals. In our context, this means that high-expertise doctors choose to write online responses, and low-expertise doctors choose not to write online responses. In a pooling equilibrium, low-ability signalers try to mimic high-ability ones and send the same signals. In our context, this means that low-expertise doctors can mimic highexpertise ones and write thoughtful online responses.

When we consider the two equilibrium concepts in signaling, we are more likely to observe a separating equilibrium in mainstream medicine: high-expertise doctors can separate themselves from low-expertise ones by using online responses. The reason is that mainstream medicine has more rigorous scientific evidence and framework, and it is possible to give rational and logical explanations in short online responses. The knowledge structure of doctors in mainstream medicine is similar, and the online responses of one doctor can be verified or refuted by another doctor. In other words, the criteria for thoughtful online responses in mainstream medicine are relatively clear. Therefore, in mainstream medicine, it is difficult for low-expertise doctors to mimic high-expertise ones and write thoughtful online responses simply because low-expertise ones do not have the expertise. As a result, providing thoughtful online responses enables patients to distinguish high-expertise doctors from low-expertise ones to a certain extent.

In contrast with mainstream medicine, traditional/ alternative medicine often relies on historical evidence rather than scientific evidence to support or invalidate a particular therapy. Doctors in traditional/alternative medicine may have different knowledge structures and use different terms (Oyebode et al. 2016, Rudra et al. 2017). In other words, traditional/alternative medicine does not have a rigorous scientific basis and sometimes is impossible to explain logically in short online responses. For example, many types of traditional/alternative medicine, such as meditation and healing by touch, rely heavily on face-to-face interactions and are difficult to explain in written online responses.<sup>7</sup> Therefore, in traditional/alternative medicine, the criteria for thoughtful online responses are not that clear, and online responses are less likely to enable patients to distinguish high-expertise doctors from low-expertise ones. Actually, doctors’ online responses are weaker signals for medical-service quality than face-to-face interactions in traditional/ alternative medicine. As a result, we are more likely to observe a pooling equilibrium in traditional/alternative medicine, and providing online responses is expected to be less beneficial for a doctor with a specialty in traditional/alternative medicine than in mainstream medicine. Hence, we ask (2) whether doctors with a specialty in mainstream medicine get higher recommendations by responding to questions than those with a specialty in traditional/alternative medicine.

The attributes of doctors may also influence the impact of doctors’ responses to questions on recommendations by users. Hence, we ask (3) whether a doctor’s choice of transparency levels in an appointmentbooking option influences the impact of doctors’ responses on user recommendations. The answer to this question is not trivial. The site offers different levels of transparency in booking appointments: (1) full schedule up to each slot of 15 minutes available transparently through a direct login from the platform website itself or (2) only the address and name of a doctor listed with no booking facility. The effect of doctors responding to questions could be viewed as a substitute for transparency in appointment booking. It is, however, likely that more transparency in both appointment booking and responses to questions is driven by consistency in doctors’ strategies.

We could expect lower fees to signal a lower quality of service and a perceived lower satisfaction from answered questions by such a doctor. Accordingly, we would expect the recommendations to be lower for doctors charging lower fees. However, doctors with lower fees could compensate for or counter perceptions by putting in extra attention and effort in providing quality answers, thus leading to higher recommendations by users. It is even possible that the market has different needs, and price-conscious consumers do not care much for the quality of responses. Doctors offering low-priced services thus are not affected adversely in recommendations. Accordingly, we ask (4) whether the impact of doctors’ responses is larger for doctors charging higher service fees.

Likewise, a more experienced doctor could mean greater credibility in the responses to questions and, hence, more recommendations from users. By contrast, a doctor with lesser experience would be expected to compensate for such a limitation by providing more thoughtful responses of higher quality. Both cases are theoretically plausible, which presents a viable opportunity for empirical tests. Therefore, our next question is (5) whether higher experience of a doctor leads to a greater impact of answered questions on recommendations by users, A similar dilemma exists for the number of qualifications that a doctor has. More qualifications add credibility to a doctor’s answers, leading to more recommendations. Mindful of such competitive responses, a lesser count of qualifications would mean greater and conscious compensatory effort in providing responses. Hence, we seek to know (6) whether a higher count of qualifications leads to a greater impact of a doctor’s responses on user recommendations.

Investigating these moderating factors helps doctors and the healthcare platform to comprehensively evaluate the effectiveness of a doctor’s responses. Although, in general, the benefit of responding to patients’ questions is considerable, the magnitude of the benefit could vary based on different doctor characteristics. A complete understanding of how moderating factors affect the impact of doctors’ responses is important for doctors to precisely estimate the benefit of responding to patients’ questions according to their own characteristics and provides a better guidance to devise appropriate online response strategies.

## 2. Literature Review

The study of UGC has evinced keen interest in research because of a rapid increase in digital content in the past decade. Our study is related to three different research streams: (1) collaborative content creation, (2) online reputation building, and (3) use of IT in healthcare.

## 2.1. Collaborative Content Creation

e-Commerce and social media sites provide information sourced in the form of UGC. Their roles are found to be complementary with an equal trust in either type of site (Bronner and de Hoog 2010). Most research is restricted to either the content being in the form of user reviews on a product or service or management responses to such reviews, as in Gu and Ye (2014). Q&A forums, however, provide a platform by which other users, experts, or service providers respond to users’ questions based on the underlying model of the site. Research is scant in the area of investigating the impacts of responses provided by professional service providers in Q&A forums. In physician services especially, because advertising is discouraged through regulatory guidelines in most countries, service providers rely on reputation build ing through responses to users on the other side of the online marketplace. Our Q&A data set involves a broad range of general questions from users on the subject on which expert service providers or doctors get to respond. This helps investigate the linkages between Q&A activities and doctor reputation to provide novel research insights.

Identity-relevant information of content-generating experts shapes the judgments of consumers about the products and such reviews (Forman et al. 2008). Unlike products, a service provider is not distinguishable from the underlying service, for example, in the case of physicians. Our research examines whether this finding on products can be extended to services provided by these experts themselves. Research on collaborative content creation on Q&A forums has been around sites on which expert users respond to other users. On such forums, Paul et al. (2012) find past contributions and social voting as indicators of experts’ reputation to identify experts. Consistent good answers help to build a good reputation that can be captured by online social voting systems. For novice information-seeking users, such an online social reputation is a good indicator of answer quality (Hart and Sarma 2014). We capture Q&A response measures, reputation, and ranking separately, thereby distinguishing them from each other, to enable us to build further on research in expert identification.

## 2.2. Online Reputation Building

Our paper is also related to a large body of literature on online reputation building. Online interaction in Q&A platforms is an effective way for service providers to engage consumers and build reputation. Prior research has shown that successful relations between online trading parties depends critically on reputation built through (1) online feedback mechanisms (Ba and Pavlou 2002, Bolton et al. 2004, Rice 2012, Ye et al. 2014) or (ii) social interactions (Bapna et al. 2017a).

The first stream of research focuses on online feedback mechanisms in bilateral review platforms on which sellers can also rate buyers. For example, Ba and Pavlou (2002) examine the impact of the numerical ratings in online reputational feedback mechanisms. Bolton et al. (2004) and Rice (2012) use laboratory experiments to study the effect of online feedback mechanisms on the level of trust. Ye et al. (2014) quantify the causal impact of online reputation mechanisms on sellers’ strategic behavior using a natural experiment. In the second stream of literature focusing on social interactions, Bapna et al. (2017a) examine the role of social ties in online reputation building. In our study, a high-expertise doctor can accumulate online reputation by providing thoughtful online responses because the doctor’s past online responses can be observed by all patients. Therefore, the practice of responding to consumer/patient comments is one type of online reputation management strategy that can build reputation through social interactions and engagement with consumers/patients (Proserpio and Zervas 2017, Kumar et al. 2018).

## 2.3. Use of IT in Healthcare

Physician selection for primary healthcare varies globally as it is governed by models of healthcare infrastructure, regulation, and other factors. Board certification (Freed et al. 2010), distance, fees, wait time, accessibility, education, and experience (Hanna et al. 1995) are factors that go into the selection of a physician by patients. Physician communications (Deledda et al. 2013), patient self-awareness, and availability of information for search (Butler and McGlone 2002, Abraham et al. 2011) also influence physician selection. Online healthcare communities are popular and use social features, such as personal experiences, opinions, and answers, and social support exchange (Lau and Kwok 2009; Yan and Tan 2014, 2017). Common motives of users in healthcare communities are information seeking and social support (Nambisan 2011). To the best of our knowledge, very few studies have examined supply-side answers to demand-side questions in the healthcare domain. We deem these new features and research therein as important for either side as they affect the selection decision by the demand side and the physician engagement strategies in the supply-side competitive markets.

More broadly, our research is also related to the literature on the use of IT in the healthcare domain. Bardhan et al. (2014) propose a novel predictive model to study the association between hospital usage of health information technology (HIT) and readmission risk. Yaraghi et al. (2014) explore the drivers of health information exchange (HIE) adoption and use at the level of medical practices. Demirezen et al. (2016) analyze the sustainability of HIE and participation levels in an analytical model. In our study, we focus on a different type of HIT, online doctors responses, and empirically show the causal impact on patient recommendations.

## 3. Data Description and Summary Statistics

We collected data from the largest online doctor search and appointment-booking platform (www .practo.com) in the world that connects doctors with customers much like Uber connects drivers with customers.<sup>8</sup> The site lists a representative segment of nearly 10% of total registered doctors in urban India with all top 47 cities and all specialties included. The site claims to book 40 million appointments every year (Srikanth 2015). The site allows users to search for doctors by city, location, and specialty. Search results contain an overview of each doctor and a link to the home page of each doctor on the site, rank ordered based on the combined criteria of distance, fees, recommendations, experience of the doctor qualifications, and appointment experience score.

Our data set takes advantage of a unique Q&A feature that the healthcare portal introduced in doctor home pages (see sample home page in Figure 2) on its site in April 2016. The feature allowed users to see all the answers given by each doctor on the community Q&A forum of the health portal and on each doctor’s home page. This allows us to study the impact of the newly added doctors’ response feature on patient recommendations. The design of the web page before and after the introduction of the Q&A feature can be found in Online Appendix D. The time span of our study is from March 2016 to August 2016.

The attributes of doctors, city and specialty-wise search rankings, and various measures for Q&A comprise the data set. Doctor’s attributes include fees, experience, number of recommendations, number of qualifications, specialty, city, and locality. Super specialties are grouped under specialty because that represents the way results get filtered by search criteria.

We enriched the data set from the site with city wise demographic data: total population, gender ratio, literacy ratio, per capita income, and number of children under the age of six years. Variables were normalized for analysis. Income, age, and gender are important indicators of healthcare expenditure. Urban out-of-pocket healthcare expenditure is mostly for allopathic doctors<sup>9</sup> (90%), and of that, 70% is from private care providers listed on the site (Jayakrishnan et al. 2016). City-wise population, income, age, and gender data are collected from India Census reports.<sup>10</sup> Descriptive statistics for key variables are presented in Table 1.

## 4. Empirical Model Speci<sup>fi</sup>cation and Analysis

In this section, we present our empirical analysis and results. We begin with examining the impact of doctors responses on patient recommendations.

## 4.1. Impact of Doctors’ Responses on Patient Recommendations

In this section, we examine our first research question: the impact of the introduction of doctors’ response features on patient recommendations when (1) doctors choose to use the feature and (2) they choose not to use the feature.<sup>11</sup> Following Tucker and Zhang (2011), we look at the following difference-in-differences (DID) specifications with panel fixed effects:

Figure 2. (Color online) A Screenshot of Doctor Home Page with Q&A Feature  
![](/api/attachments/C2XM7EED/fulltext/images/940e3265280056ac9bdebb6824556855ba9cae10f8e578a6650f5ccef6551f54.jpg)

$$
\begin{array}{r l} & {r e c c o s _ {i t} = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t}} \\ & {\qquad + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t})} \\ & {\qquad + \beta_ {3} C o n t r o l s + \varepsilon_ {i t},} \\ & {r e c c o s _ {i t} = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t}} \\ & {\qquad + \beta_ {2} (P o s t L a u n c h _ {t} \times c o n s u l t _ {i t})} \\ & {\qquad + \beta_ {3} C o n t r o l s + \varepsilon_ {i t},} \end{array}\tag{1}
$$

(2)

where the dependent variable, reccos , is the number of patient recommendations for doctor i at time t (the time unit is a week); $c _ { i }$ is the fixed effect; PostLaunch is a dummy variable indicating whether the feature of doctors’ responses is launched (1 = postlaunch period; 0 = prelaunch period); yn consult<sub>it</sub> is a binary response variable indicating whether doctor i responds to patients’ questions at time t (0 = no response; 1 = response); consult indicates the number of questions by users answered by doctor i at time $t ;$ and Controls include (1) city\_serp, city search result page ranking of a doctor, (2) max\_city\_serp, maximum rank for that city at time t (essentially, it is the number of available doctors, which measures the intensity of competi tion), (3) fees, fees in Indian rupees (INR) of the doctor, (4) mbbs, a binary variable indicating whether a doctor is certified to practice in allopathic medicine, (5) bds, a binary variable indicating whether a doctor is certified to practice dentistry, (6) bams, a binary variable indicating whether a doctor is certified to practice in Ayurveda (traditional Indian medicine),<sup>12</sup> (7) bhms, a binary variable indicating whether a doctor is certified to practice in homeopathic medicine, and (8) apptbook, whether an online appointment-booking option is available (0 = online appointment-booking option is not available; 1 = online appointmentbooking option is available). All these control variables are time variant. We also control for time dummies.<sup>13</sup> Note that $y n \_ c o n s u l t _ { i t }$ and consu $l t _ { i t }$ are not included in regression Equations (1) and (2) because the values of these variables are zero before the introduction of the response feature.

It is worth noting that, in practice, strategic market ing effort from doctors, such as fake recommendations, may contaminate our dependent variable, which measures the demand-side user perception of medical service offered. However, the online healthcare portal has elaborate guidelines on patients posting feedback on doctors on the site and claims expert moderators and a verification process to ensure that any fake/ inflated/promotional feedback is rejected (the details can be found in Online Appendix D).

Table 1. Descriptive Statistics

<table><tr><td>Variables</td><td>Minimum</td><td>Mean</td><td>Maximum</td><td>Standard deviation</td></tr><tr><td>Number of listed doctors on the site from same city</td><td>144</td><td>6,929.7</td><td>15,366</td><td>5,058.1</td></tr><tr><td>Number of answers by a doctor</td><td>0</td><td>0.34</td><td>4,203</td><td>19</td></tr><tr><td>Number of doctors in a specialty</td><td>132</td><td>4,244.4</td><td>40,582</td><td>7,336.7</td></tr><tr><td>Fees of doctor (in rupees)</td><td>0</td><td>301.3</td><td>30,000</td><td>464.8</td></tr><tr><td>Experience of doctor (in years)</td><td>1</td><td>15.6</td><td>80</td><td>10.6</td></tr><tr><td>Number of recommendations for a doctor</td><td>0</td><td>70.2</td><td>4,538</td><td>185.6</td></tr><tr><td>City population</td><td>101,520</td><td>8,353,321</td><td>18,414,288</td><td>6,124,822</td></tr><tr><td>Gender ratio in a listed city</td><td>0.754</td><td>0.90</td><td>1.07</td><td>0.05</td></tr><tr><td>Children under age of six years in a city</td><td>0.075</td><td>0.14</td><td>0.10</td><td>0.012</td></tr><tr><td>Per capita income in a listed city</td><td>39,907</td><td>96,888</td><td>384,706</td><td>55,864</td></tr></table>

In column (1) of Table 2, we find that the coefficients of PostLaunch and the interaction term $( P o s t L a u n c h _ { t } \times y n _ { - } c o n s u l t _ { i t } )$ are significantly positive, but the coefficients of the interaction term are much larger than the coefficient of PostLaunch . After the launch of the feature of doctors’ responses, there is a small increase in the level of patient recommendations for doctors who can respond to patients’ comments but choose not to do so. However, doctors who actually respond to patients’ comments have a much higher level of performance than before. A possible reason for the small increase in the level of patient recommendations for doctors who choose not to respond to patients’ comments is that the launch of the feature of doctors’ responses reduces information asymmetry and attracts more patients to use the online portal. Therefore, introduction of the online response feature can increase the overall customer traffic of the online portal and benefit the listed doctors who can respond to patients’ comments but choose not to do so.

Table 2. The Impact of Doctors’ Responses on Recommendations by Patients

<table><tr><td>Variables</td><td>(1) Fixed effects</td><td>(2) Fixed effects, robust standard error</td><td>(3) Fixed effects</td><td>(4) Fixed effects, robust standard error</td></tr><tr><td>PostLaunch</td><td>6.603***(15.68)</td><td>6.603***(17.61)</td><td>7.895***(18.66)</td><td>7.895***(20.78)</td></tr><tr><td> $PostLaunch \times yn\_consult$ </td><td>58.80***(30.76)</td><td>58.80***(14.00)</td><td></td><td></td></tr><tr><td> $PostLaunch \times consult$ </td><td></td><td></td><td>0.0761***(8.311)</td><td>0.0761*(1.936)</td></tr><tr><td> $city\_serp$ </td><td>-0.000937***(-3.765)</td><td>-0.000937***(-6.130)</td><td>-0.00109***(-4.343)</td><td>-0.00109***(-7.152)</td></tr><tr><td> $max\_city\_serp$ </td><td>-0.00125***(-11.71)</td><td>-0.00125***(-10.56)</td><td>-0.00128***(-11.91)</td><td>-0.00128***(-10.72)</td></tr><tr><td>fees</td><td>0.00209(0.794)</td><td>0.00209(0.779)</td><td>0.00270(1.015)</td><td>0.00270(0.996)</td></tr><tr><td>mbbs</td><td>-5.496**(-2.147)</td><td>-5.496(-1.255)</td><td>-5.601**(-2.166)</td><td>-5.601(-1.276)</td></tr><tr><td>bds</td><td>7.120(1.448)</td><td>7.120(1.567)</td><td>8.267*(1.665)</td><td>8.267*(1.859)</td></tr><tr><td>bams</td><td>-15.98(-1.367)</td><td>-15.98***(-3.646)</td><td>-10.48(-0.888)</td><td>-10.48**(-2.561)</td></tr><tr><td>bhms</td><td>-6.131(-0.650)</td><td>-6.131(-1.217)</td><td>-4.435(-0.465)</td><td>-4.435(-0.756)</td></tr><tr><td>apptbook</td><td>2.132**(1.964)</td><td>2.132*(1.950)</td><td>1.612(1.470)</td><td>1.612(1.482)</td></tr><tr><td>Time dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>48.79(0.734)</td><td>48.79(1.521)</td><td>51.28(0.764)</td><td>51.28(1.612)</td></tr><tr><td>Observations</td><td>131,201</td><td>131,201</td><td>131,201</td><td>131,201</td></tr></table>

\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.  
Note. t- or robust t-statistics in parentheses.

To alleviate concerns about the failure to meet standard regression assumptions (such as clustering and heteroskedasticity), we follow Stock (2010) and report the robust statistics in column (2) of Table 2. The estimation results for regression Equation (2) are presented in columns (3) (ordinary t-statistics) and (4) (robust t-statistics). To explore the sensitivity of treatment effects to the inclusion of observed controls, we compare the result from a model without the control variables with our results from Table 2 in Online Appendix C. It is reassuring that the coefficients on the focal variables are stable after inclusion of the observed controls, indicating that our results are unlikely to be driven by omitted variables bias (Chiappori et al. 2012).

Our findings from regression Equations (1) and (2) imply that, in general, the launch of the doctors’ response feature can increase patient recommendations. However, this new feature does not benefit every doctor equally: it benefits the doctors who actually respond to patients’ questions more than the doctors who can respond to patients’ questions but choose not to do so (Brambor et al. 2005). In Online Appendix E, we estimate the models using a longer time window, and the results are robust.

We address the issue of multicollinearity in regression Equations (1) and (2) by looking at the variance inflation factors (VIFs). The VIF quantifies the severity of multicollinearity in a regression. When the independent variables are correlated, the estimated standard errors of the fitted coefficients are inflated, which can be used to check for the presence of multicollinearity (Chatterjee and Hadi 2012). In the absence of any linear relationship among independent variable j and other independent variables, VIF would be one. The deviation of the VIF value from 1 indicates a departure from orthogonality and a tendency toward collinearity. VIFs are widely used in the information systems literature to establish whether multicollinearity is an issue (e.g., Burtch et al. 2013, Aral and Walker 2014, Singh et al. 2014). Most prior studies rely on informal rules of thumb applied to the VIF. For instance, in Chatterjee and Hadi (2012, p. 250), “values of variance inflation factors greater than 10 is often taken as a signal that the data have collinearity problems.” In Table $^ { 3 , }$ , we examine the VIFs of $y n \_ c o n s u l t _ { i t }$ and $c o n s u l t _ { i t }$ in two separate multiple regressions to assess possible multicollinearity among model covariates. We find that the VIFs associated with each variable are less than 2.5, which is well below the conventionally accepted threshold (VIF < 10), indicating that multicollinearity is not an issue in our model and does not significantly impact our findings.

Because our dependent variable, the number of patient recommendations, takes on nonnegative integer values, we also run count data models (Poisson and negative binomial models) and a log-transformation model as robustness checks. The estimation results of the Poisson and negative binomial models are presented in Table 4. We find that these results are con sistent with those in our baseline models: the launch of the doctors’ response feature increases patient recommendations.

Table 3. Collinearity Diagnostics

<table><tr><td></td><td>VIF</td><td>VIF</td></tr><tr><td>PostLaunch</td><td>1.24</td><td>1.22</td></tr><tr><td>Yn_consult</td><td>1.03</td><td></td></tr><tr><td>consult</td><td></td><td>1.00</td></tr><tr><td>city_serp</td><td>2.43</td><td>2.42</td></tr><tr><td>max_city_serp</td><td>2.34</td><td>2.34</td></tr><tr><td>Fees</td><td>1.07</td><td>1.07</td></tr><tr><td>Mbbs</td><td>1.82</td><td>1.82</td></tr><tr><td>Bds</td><td>1.62</td><td>1.62</td></tr><tr><td>Bams</td><td>1.21</td><td>1.21</td></tr><tr><td>Bhms</td><td>1.23</td><td>1.23</td></tr><tr><td>apptbook</td><td>1.14</td><td>1.13</td></tr><tr><td>Mean VIF</td><td>1.51</td><td>1.51</td></tr></table>

For the log-transformation model, we estimate the following regression equations:

$$
\begin{array}{r l} & {\log (r e c c o s _ {i t}) = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t}} \\ & {\qquad + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t})} \\ & {\qquad + \beta_ {3} C o n t r o l s + \varepsilon_ {i t},} \end{array}\tag{3}
$$

$$
\begin{array}{r l} & {\log (r e c c o s _ {i t}) = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t}} \\ & {\qquad + \beta_ {2} (P o s t L a u n c h _ {t} \times \log (c o n s u l t _ {i t}))} \\ & {\qquad + \beta_ {3} C o n t r o l s + \varepsilon_ {i t}.} \end{array}\tag{4}
$$

The estimation results are robust and are presented in Table 5.

It is worth noting that the key argument of the DID method is the “parallel paths” assumption, which posits that the average change in the control group represents the counterfactual change in the treatment group had there been no treatments (Abadie 2005). In other words, aside from the changes resulting from the treatment, any differences between the treatment and control groups should be random. In our specific context, the control group is the doctors who do not respond to patient questions after the launch of the new feature, and the treatment group is the doctors who respond to patient questions. A typical endogeneity concern is that doctors are self-selected to respond to patient questions, and hence, the parallel paths assumption may not be satisfied. In other words, the treated doctors are not randomly selected: the doctors who choose to respond might be systematically different from the doctors who choose not to respond. Hence, in the following section, we conduct various analyses to address the endogeneity concerns.

Table 4. The Impact of Doctors’ Responses on Recommendations by Patients: Count Data Models

<table><tr><td>Variables</td><td>(1) Poisson model</td><td>(2) Poisson model</td><td>(3) Negative binomial model</td><td>(4) Negative binomial model</td></tr><tr><td>PostLaunch</td><td>0.500***(227.2)</td><td>0.542***(247.8)</td><td>0.997***(45.23)</td><td>1.046***(47.46)</td></tr><tr><td>PostLaunch × yn_consult</td><td>0.455***(189.8)</td><td></td><td>1.155***(13.12)</td><td></td></tr><tr><td>PostLaunch × consult</td><td></td><td>0.000708***(73.72)</td><td></td><td>0.00642***(3.674)</td></tr><tr><td>city_serp</td><td>-0.00178***(-1,098)</td><td>-0.00180***(-1,111)</td><td>-0.000923***(-127.4)</td><td>-0.000927***(-127.5)</td></tr><tr><td>max_city_serp</td><td>-6.55e-06***(-13.30)</td><td>-9.19e-06***(-18.67)</td><td>0.000258***(73.01)</td><td>0.000258***(72.85)</td></tr><tr><td>Fees</td><td>4.47e-05***(138.8)</td><td>4.47e-05***(137.7)</td><td>0.00261***(43.44)</td><td>0.00261***(43.31)</td></tr><tr><td>Mbbs</td><td>0.0202***(9.027)</td><td>0.00402*(1.799)</td><td>0.600***(18.09)</td><td>0.609***(18.34)</td></tr><tr><td>Bds</td><td>0.627***(270.4)</td><td>0.628***(270.8)</td><td>0.560***(16.53)</td><td>0.557***(16.36)</td></tr><tr><td>Bams</td><td>-0.0884***(-17.62)</td><td>-0.0807***(-16.09)</td><td>-0.958***(-19.31)</td><td>-0.968***(-19.47)</td></tr><tr><td>Bhms</td><td>0.162***(41.60)</td><td>0.178***(45.61)</td><td>0.834***(17.75)</td><td>0.833***(17.70)</td></tr><tr><td>apptbook</td><td>1.083***(637.6)</td><td>1.098***(648.3)</td><td>2.284***(85.41)</td><td>2.303***(85.96)</td></tr><tr><td>Time dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>2.009***(227.5)</td><td>1.999***(226.2)</td><td>-0.0539(-1.401)</td><td>-0.0466(-1.207)</td></tr><tr><td>Observations</td><td>131,201</td><td>131,201</td><td>131,201</td><td>131,201</td></tr></table>

Note. t-statistics in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 4.2. Moderating Factors That Govern the Impact of Doctors’ Responses

In this section, we examine how factors, such as doctor specialty, doctor experience, doctor qualification, online booking systems, and service fees, moderate the impact of doctors’ responses. In regression Equation (5), we look at the moderating role of specialty:

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times t r a d i t i o n a l _ {i}) \\ & + \beta_ {4} C o n t r o l s + \varepsilon_ {i t}, \end{array}\tag{5}
$$

where traditional is a binary variable indicating whether a doctor’s specialty is in traditional/alternative medicine (value is 1) or in mainstream medicine (value is 0). In the regressions on moderating factors, we have the same controls as in regression Equation (1). The estimation results are presented in column (1) of Table 6. We find that the coefficient on the triple interaction term is significantly negative, which suggests that responding to patient questions is more beneficial for a doctor with a specialty in mainstream medicine than in traditional/alternative medicine This result confirms our expectation in the signaling framework discussed in Section 1: online responses are less likely to enable patients to distinguish high-expertise doctors from low-expertise ones in traditional/alternative medicine than in mainstream medicine.

In regression Equation (6), we investigate the role of doctor experience (experience ). We report the estimation results in column (2) of Table 6 and find that the coefficient on the triple interaction term is significantly positive. It implies that the impact of doctors’ responses on patient recommendations is stronger for more experienced doctors.

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times e x p e r i e n c e _ {i t}) \\ & + \beta_ {4} C o n t r o l s + \varepsilon_ {i t}. \end{array}\tag{6}
$$

In regression Equation (7), we examine the role of doctor qualifications (qual ). The estimation results are reported in column (3) of Table 6. Once again, the coefficient on the triple interaction term is significantly

Table 5. The Impact of Doctors’ Responses: Log-Transformation Models

<table><tr><td>Variables</td><td>(1) Log-model</td><td>(2) Log-model</td></tr><tr><td>PostLaunch</td><td>0.292***(23.97)</td><td>0.290***(23.80)</td></tr><tr><td>PostLaunch × yn_consult</td><td>0.486***(13.99)</td><td></td></tr><tr><td>PostLaunch × Log(consult)</td><td></td><td>0.165***(12.83)</td></tr><tr><td>Log(city_serp)</td><td>-0.184***(-19.87)</td><td>-0.184***(-19.82)</td></tr><tr><td>Log(max_city_serp)</td><td>-0.634***(-18.87)</td><td>-0.636***(-18.87)</td></tr><tr><td>Log(fees)</td><td>0.00496(0.415)</td><td>0.00624(0.512)</td></tr><tr><td>Mbbs</td><td>0.109***(2.634)</td><td>0.109***(2.622)</td></tr><tr><td>Bds</td><td>0.168**(1.965)</td><td>0.179**(2.088)</td></tr><tr><td>Bams</td><td>-0.121(-0.943)</td><td>-0.0993(-0.733)</td></tr><tr><td>Bhms</td><td>0.0436(0.522)</td><td>0.0557(0.672)</td></tr><tr><td>apptbook</td><td>0.126***(7.132)</td><td>0.124***(7.035)</td></tr><tr><td>Time dummies</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.944**(1.988)</td><td>0.943**(1.983)</td></tr><tr><td>Observations</td><td>131,201</td><td>131,201</td></tr></table>

Note. Robust t-statistics in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

positive, which means that the impact of doctors’ responses on patient recommendations is stronger for doctors with a larger number of qualifications. Moreover, the coefficient on PostLaunch × yn consult is not significant in column (3) of Table 6. The implication is that responding to patients only benefits doctors who have some minimum qualifications. For doctors who do not have some minimum qualifications, actually answering patients’ questions may not help (not statistically significant).

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times q u a l _ {i t}) \\ & + \beta_ {4} C o n t r o l s + \varepsilon_ {i t}. \end{array}\tag{7}
$$

In our signaling framework, we can provide cohesive explanations for our results on moderating factors experience and qual . A doctor with a higher level of experience and qualifications is more likely to be able to provide thoughtful responses, which are stronger signals for medical-service quality. Therefore, the impact of online responses is larger for more experienced doctors or doctors with a larger number of qualifications.

Then, in regression Equation (8), we explore the moderating impact of whether an appointment-booking option is available online. In column (4) of Table $6 ,$ we find that the coefficient on the triple interaction term is significantly positive, which suggests that the impact of doctors’ responses on patient recommendations is stronger for doctors who have an appointment-booking option available online.

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times a p p t b o o k _ {i t}) \\ & + \beta_ {4} C o n t r o l s + \varepsilon_ {i t}. \end{array}\tag{8}
$$

In regression Equation (9), we examine the moderating role of service fees. From column (5) in Table $^ { 6 , }$ we find that the impact of doctors’ responses on the recommendations by patients is stronger for doctors charging higher fees. The implication is that the highend health-service market is quite different from the low-end health-service market, which is consistent with the findings of Lu et al. (2017) in the context of nursing homes. In the low-end health-service market, responding to patients is less important. However, in the high-end market, it plays a critical role. Facing a quality–price trade-off, patients in the high-end market place a larger weight on medical-service quality, and patients in the low-end market focus more on service prices. As we stated earlier, doctors’ online responses can be interpreted as a signal for medical-service quality. Therefore, the benefit of responding to patients is much higher in the high-end market than in the low-end market.

Table 6. The Impact of Doctors’ Responses on Recommendations: Moderating Factors

<table><tr><td>Variables</td><td>(1) Fixed effects, moderating factor: traditional</td><td>(2) Fixed effects, moderating factor: experience</td><td>(3) Fixed effects, moderating factor: qual</td><td>(4) Fixed effects, moderating factor: apptbook</td><td>(5) Fixed effects, moderating factor: fees</td></tr><tr><td>PostLaunch</td><td>6.247***(13.26)</td><td>7.488***(18.08)</td><td>6.641***(17.75)</td><td>6.587***(17.62)</td><td>6.684***(17.86)</td></tr><tr><td>PostLaunch × yn_consult</td><td>88.45***(14.68)</td><td>23.86***(2.974)</td><td>0.606(0.0665)</td><td>12.66***(5.484)</td><td>44.79***(7.247)</td></tr><tr><td>PostLaunch × yn_consult × moderating factor</td><td>-61.27***(-10.26)</td><td>2.800***(3.774)</td><td>28.04***(5.608)</td><td>77.02***(11.87)</td><td>0.0376**(2.280)</td></tr><tr><td>Observations</td><td>131,201</td><td>101,396</td><td>131,201</td><td>131,201</td><td>131,201</td></tr></table>

Note. Robust t-statistics in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times f e e s _ {i t}) \\ & + \beta_ {4} C o n t r o l s + \varepsilon_ {i t}. \end{array}\tag{9}
$$

It is worth noting that these moderators might be correlated with unobserved characteristics of doctors. After controlling for unobserved characteristics of doctors in our fixed-effects models, the endogeneity of moderators might be less of a concern. In addition, the matching methods (propensity score matching [PSM] and look-ahead propensity score matching [LA-PSM]) help us achieve a more balanced sample. In Online Appendix B, we reestimate the regressions on moderators using the new sample created by different matching methods, and the results are consistent.

## 4.3. Endogeneity Concerns of Self-Selected Responses

4.3.1. Causal Identi<sup>fi</sup>cation Strategies in Addressing Endogeneity Concerns. To address different endogeneity mechanisms of self-selected responses, we use various identification strategies. We have three cases with different identification assumptions: (1) the selection process is driven by observable characteristics (observable to researchers), and the differences between control and treatment groups caused by the observable characteristics are stable over time in their influence on patient recommendations (time-invariant shock), (2) the selection process is driven by observable characteristics, and the differences between control and treatment groups caused by the observable characteristics change over time in their influence on patient recommendations (time-variant shock), and (3) the selection process is driven by unobservable characteristics, and the differences between control and treatment groups caused by the unobservable characteristics change over time in their influence on patient recommendations (time-variant shock).

In case 1, our regression Equations (1) and (2) (DID model with panel fixed effects) is sufficient to take care of the endogeneity concern because the paralle paths assumption holds and the observable or unobserved confounding factors cancel out. In case 2, we use a DID approach combined with PSM to correct the possible endogeneity (see Section 4.3.2.). Note that PSM is not robust against “hidden bias” from unobserved variables that are associated with both assignment to treatment and the dependent variable. We use the approach of Rosenbaum bounds (Rosenbaum 2002) to conduct a sensitivity analysis on PSM. We address the endogeneity concern in case 3 by using a combination of the traditional DID model and the LA-PSM method (see Bapna et al. 2017b, Kumar et al. 2018). In addition, a potential concern in the DID model is whether time-variant unobserved confounders cause heterogeneity in the pretreatment trends between the control and treatment groups (Angrist and Pischke 2008, Greenwood and Wattal 2017). We use the correlated random trend and relative time models to further rule out pretreatment trends (see Sections 4.3.3 and 4.3.4).

4.3.2. DID Combined with PSM. To avoid model dependence, we consider a DID model combined with matching techniques, such as PSM. Following Goh et al. (2013) and Li (2016), we first create a “proper” control group for treated doctors by using PSM. We ensure that the control and treated groups are comparable in terms of observable characteristics. Then we run the DID regression Equation (1).

It is worth noting that the traditional PSM takes care of only observable characteristics and may be biased in the case of selection on unobservables (Mithas and Krishnan 2009). However, in the implementation of the DID approach combined with PSM, even if treated units differ in important unobserved characteristics from those in the control group, as long as such differences between the control and treatment groups are stable over time in their influence on patient recommendations, our specification can eliminate the bias resulting from the differences between treated and control units. By contrast, the traditional DID approach relies on the strong parallel paths assumption. If the violation of the parallel paths assumption is caused by the differences in observable characteristics, augmenting DID with PSM is an effective method to correct the possible bias.

In the matching process, the treated doctors are the ones who answer patient questions after the introduction of the new feature. Using PSM, we match each treated doctor with a most “similar” control doctor in terms of the following characteristics before the introduction of the doctors’ response feature: (1) doctor-level information, such as the experience of the doctor, the specialty of the doctor, whether online appointment-booking option is available, city-search result page ranking of the doctor, and fees in Indian rupees of thedoctor, and (2) city-level information, such as the population of the city in the most recent census (2011), the literacy ratio in the city, and the gross domestic product (GDP) of the city in billions INR in year 2007–2008.

We first sort all doctors in a random order to make sure that the ordering does not affect the subsequent matching. Then we run a logit regression based on the pretreatment variables mentioned earlier and obtain the predicted propensity scores. We use the nearestneighbor matching algorithm in which each treated doctor is matched with a control doctor with the closest propensity score. To assess the quality of matching, we perform t-tests of equality of means before and after the matching to check whether our PSM adequately balances characteristics between the treatment and control group units. The results are presented in Table 7. In this table, there is clear evidence of covariate imbalance between groups. After matching, the differences of mean are no longer statistically significant, suggesting that matching helps reduce the bias associated with the observable characteristics. We also check the number of patient recommendations for the control and treatment groups (after the matching) before the introduction of the doctors’ response feature. We find that after the matching, the number of patient recommendations before the introduction of the doctors’ response feature for the controlled doctors is not statistically different from that for the treated doctors, which also suggests that our matching is successful.

Figure 3 displays a graphical summary of covariate imbalance showing the standardized percentage bias for each covariate. We can see that the covariate imbalance has been greatly reduced after matching.

Common support or an overlap condition is a critical assumption in matching. The prior matching literature (Heinrich et al. 2010) suggests that checking the overlap or region of common support between treatment and control groups can be done through a visual inspection of the propensity score distributions for both the treatment and control groups. Figure 4 graphs the propensity score histogram by treatment status, and it reveals a clear overlapping of the distributions between treatment and control groups.

If there are unobserved variables that simultaneously affect assignment into treatment and outcome variables, PSM may not be robust against this hidden bias. We use the approach of Rosenbaum bounds (Rosenbaum 2002) to conduct a sensitivity analysis. The basic idea of Rosenbaum bounds is to examine whether PSM is sensitive to hidden bias: we can manipulate the estimated odds of receiving a treatment to see how much the estimated treatment effects may vary. In other words, we want to determine how strongly an unmeasured variable must influence the selection process to undermine the inference of the matching analysis.

To estimate the extent to which such “selection on unobservables” may bias our estimation and inference, we present the results of a Rosenbaum bounds sensitivity using Wilcoxon’s signed-rank test (Rosenbaum 2002) in Table 8. This table reports p-values from Wilcoxon signed-rank tests for the averaged treatment effect while setting the level of hidden bias to a certain value Γ. In Table 8, Γ is the odds ratio of treatment assignment, which is a measure of the degree of departure from a study that is free of hidden bias. Our sensitivity analysis considers several possible values of Γ and shows how the inferences might change. When Γ 1, it implies that we assume the absence of unobserved selection bias. In this case, both the upper and lower bounds of p-values are zero (sig+ = 0, sig<sup>−</sup> = 0) in Table 8, indicating that the effect of online responses is significant when there is no hidden bias. We interpret the p-values under different values of Γ in Table 8 as follows: PSM is sensitive to hidden bias if values of Γ close to 1 could lead to inferences that are very different from those obtained assuming that the study is free of hidden bias (Γ 1). PSM is insensitive if extreme values of Γ are required to alter the inference.

The critical level of Γ at which we would have to question the significance of our PSM is between five

Table 7. Differences in Mean Before and After Matching

<table><tr><td rowspan="2">Variables</td><td colspan="5">Before matching</td><td colspan="5">After matching</td></tr><tr><td>Mean treated</td><td>Mean control</td><td>Percentage bias</td><td>t-Statistics</td><td>p-value</td><td>Mean treated</td><td>Mean control</td><td>Percentage bias</td><td>t-Statistics</td><td>p-value</td></tr><tr><td>Experience</td><td>11.418</td><td>15.734</td><td>-47.9</td><td>-15.71***</td><td>0.000</td><td>11.418</td><td>11.192</td><td>2.5</td><td>0.88</td><td>0.378</td></tr><tr><td>Population</td><td>8.0e+06</td><td>7.6e+06</td><td>5.7</td><td>2.19**</td><td>0.029</td><td>8.0e+06</td><td>7.9e+06</td><td>1.3</td><td>0.35</td><td>0.730</td></tr><tr><td>literacy</td><td>0.88302</td><td>0.8765</td><td>17.3</td><td>6.19***</td><td>0.000</td><td>0.88302</td><td>0.88145</td><td>4.2</td><td>1.29</td><td>0.197</td></tr><tr><td>Apptbook</td><td>0.57649</td><td>0.22613</td><td>76.5</td><td>31.98***</td><td>0.000</td><td>0.57649</td><td>0.57649</td><td>0.0</td><td>0.00</td><td>1.000</td></tr><tr><td>GDP</td><td>690.42</td><td>660.79</td><td>4.5</td><td>1.73</td><td>0.083</td><td>690.42</td><td>672.53</td><td>2.7</td><td>0.75</td><td>0.451</td></tr><tr><td>Fees</td><td>363.55</td><td>301.05</td><td>20.4</td><td>7.41***</td><td>0.000</td><td>363.55</td><td>352.42</td><td>3.6</td><td>0.99</td><td>0.321</td></tr><tr><td>City_serp</td><td>1,044</td><td>2,016.1</td><td>-51.8</td><td>-17.41***</td><td>0.000</td><td>1,044</td><td>1,046.5</td><td>-0.1</td><td>-0.05</td><td>0.962</td></tr></table>

\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Figure 3. Standardized Percentage Bias for Each Covariate Before and After Matching

<table><tr><td rowspan="2"></td><td colspan="2">Standardized % bias across covariates</td></tr><tr><td>Unmatched</td><td>Matched</td></tr><tr><td>apptbook</td><td>75</td><td>0</td></tr><tr><td>fees</td><td>20</td><td>0</td></tr><tr><td>literacy</td><td>15</td><td>0</td></tr><tr><td>population</td><td>5</td><td>0</td></tr><tr><td>GDP</td><td>5</td><td>0</td></tr><tr><td>experience</td><td>-45</td><td>0</td></tr><tr><td>city_serp</td><td>-50</td><td>0</td></tr></table>

and six (when Γ <sub></sub> 6, the upper bound p-value is greater than 5%): for the impact of online responses to disappear, the unobserved confounder has to cause the odds ratio of treatment assignment to differ between treatment and control groups by a factor of about six.<sup>14</sup> Note that a Γ value of six is very large (Guo and Fraser 2010, Keele 2010), and it is well above the threshold values used in the prior studies for robust PSM (e.g., Keele 2010, Wei and Lin 2016). It is also worth noting that the Rosenbaum bounds are worstcase scenarios. An insignificant upper bound p-value for Γ = 6 does not mean that there is no true positive effect of online responses on patient recommendations when $\Gamma = 6$ . This result means that the confidence interval for the effect of online responses would include zero if an unobserved variable caused the odds ratio of treatment assignment to differ between treatment and control groups by six. As a summary, the results in Table 8 show that our PSM is robust to a plausible range of unobserved selection bias (hidden bias).

Figure 4. (Color online) Propensity Score Histogram by Treatment Status  
![](/api/attachments/C2XM7EED/fulltext/images/ff63e81ac7392e3575dfc3eabd3592fa3bbfafd1f87846a60d795f4f5a730638.jpg)

Table 8. Rosenbaum Bounds for PSM: Range of Significant Levels for the Signed Rank Statistic

<table><tr><td>Γ</td><td>Sig+</td><td>Sig-</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>2</td><td>5.4e-11</td><td>0</td></tr><tr><td>3</td><td>1.1e-06</td><td>0</td></tr><tr><td>4</td><td>0.000634</td><td>0</td></tr><tr><td>5</td><td>0.0317</td><td>0</td></tr><tr><td>6</td><td>0.270</td><td>0</td></tr><tr><td>7</td><td>0.701</td><td>0</td></tr></table>

Notes. Γ is the odds of differential assignment resulting from unobserved factors. Sign+ is the upper bound significance level, and Sign<sup>−</sup> is the lower bound significance level.

Next, we reestimate our DID model (2) using the new sample created by PSM, and the results are presented in column (1) of Table 9. The basic findings are consistent with those in our DID model.

4.3.3. DID Combined with LA-PSM. If the selection process is driven by unobserved characteristics and the differences between control and treatment groups caused by the unobserved characteristics change over time in their influence on patient recommendations, we can address this concern by using a quasiexperimental design, which is essentially a combination of the DID model and the LA-PSM (Bapna et al. 2017b, Kumar et al. 2018).

Following similar identification ideas to those in Garg et al. (2011), Bapna et al. (2017b), and Wang et al. (2017), we use a quasi-experimental design to account for the differences between control and treatment groups caused by unobserved characteristics. The intuition of our quasi-experiment research design is to exploit the time sequence of doctors’ responses and identify a more similar control group in terms of unobserved characteristics. Doctors who answer patient questions (treated units) can be very different from those who do not answer questions (control units) in terms of observable and unobserved characteristics. If the parallel paths assumption is violated because of observable characteristics, our DID + PSM approach in the preceding section can take care of it. However, if the parallel paths assumption is violated because of unobserved characteristics, we can use the same approach as in Garg et al. (2011) and Wang et al. (2017) to identify a better control group. Basically, a better control unit could be a doctor who has not answered patient questions but will answer patient questions in the future. This quasi-experiment design ensures that the treated and control doctors are similar in unobserved characteristics.

Table 9. The Impact of Doctors’ Responses on Recommendations by Patients: Addressing Endogeneity Concerns of Self-Selected Responses

<table><tr><td>Variables</td><td>(1) DID + PSM</td><td>(2) DID + LA-PSM</td><td>(3) Correlated random trend</td></tr><tr><td>PostLaunch</td><td>5.627***(14.84)</td><td>5.239***(13.74)</td><td>5.416***(14.18)</td></tr><tr><td>PostLaunch × yn_consult</td><td>76.65***(28.71)</td><td>69.74***(26.33)</td><td>72.33***(27.35)</td></tr></table>

Note. Robust t-statistics in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

To account for unobserved characteristics as best as we can, we adopt the LA-PSM method proposed by Bapna et al. (2017b) to identify the proper control group, and then we combine it with the DID approach. More specifically, we first split the whole sample period into two periods according to whether the doctors’ response feature was introduced (the “before introduction” period is time period 0). Then we further split the “after introduction” period into two equally long time periods: time periods 1 and 2. The treatment group in our quasi-experimental design is the doctors who answer patient questions in time period 1. For each treated unit, we match it to a control unit with the closest propensity score among doctors who have not answered patient questions in time period 1 but will respond in time period 2. On the one hand, the closest propensity score ensures that the treated and control units are similar in observable characteristics; on the other hand, choosing doctors from those who have not answered patient questions in time period 1 but will respond in time period 2 ensures that the treated and control units are similar in unobserved characteristics. After creating the proper control group, we construct a new data sample with treated and control units in time periods 0 and 1. We reestimate our DID model using the new data sample. The results are presented in column (2) of Table 9 and are consistent with those in the DID + PSM model.

4.3.4. Pretreatment Trends. If time-variant unobserved confounders cause a significant heterogeneity in the pretreatment trends, it suggests that the pretreatments may disproportionately affect treated units, as opposed to control units, and the parallel path assumption is less likely to be satisfied (Angrist and Pischke 2008, Greenwood and Wattal 2017). In our context, the concern of pretreatment trends arises because doctors’ unobserved efforts in marketing themselves could affect their decisions to answer patient questions. We conduct two robustness checks to address this concern and rule out the impact of pretreatments as an alternative explanation for our results.

In the first check, we follow Angrist and Pischke (2008) to control for individual specific time trends in the correlated random trend model:

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + g _ {i} t + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} C o n t r o l s + \varepsilon_ {i t}, \end{array}\tag{10}
$$

where $g _ { i }$ is a doctor-specific time trend for doctor i. This specification allows treated and control doctors to follow different trends in a limited but potentially revealing way. It is worth noting that in the correlated random trend model, g t can be correlated with yn consult because, in the estimation process, g t will be canceled out by first differencing Equation (10) twice, and our estimation will be unbiased. Therefore, the DID model with correlated random trends is likely to be more robust and convincing (Angrist and Pischke 2008). We estimate Equation (10), and the estimation results of the correlated random trend model are presented in column (3) of Table 9. We find that the estimated effects of interest are changed little by the inclusion of these trends, which rules out individual specific time trends as an alternative explanation for our results.

In the second check, we adopt the following relative time model proposed by Autor (2003):

$$
\begin{array}{l} r e c c o s _ {i t} = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ \qquad + \sum_ {\tau = 0} ^ {m} \beta_ {2, - \tau} (P o s t L a u n c h _ {t - \tau} \times y n \_ c o n s u l t _ {i, t - \tau}) \\ \qquad + \sum_ {\tau = 1} ^ {q} \beta_ {3, + \tau} (P o s t L a u n c h _ {t + \tau} \times y n \_ c o n s u l t _ {i, t + \tau}) \\ \qquad + \beta_ {4} C o n t r o l s + \varepsilon_ {i t}, \end{array}\tag{11}
$$

where the sums on the right-hand side allow for m lags (posttreatment effects) and q leads (anticipatory effects). We set $m = 2$ and $q = 2$ . As argued by Autor (2003) and Angrist and Pischke (2008), the basic idea of the relative time model is in the spirit of the Granger causality test (Granger 1969): if the impact of pretreatment trends is a confounding factor that can affect doctors’ decisions to answer patient questions, we should observe that the past values of reccos can predict $P o s t L a u n c h _ { t } \times y n \_ c o n \bar { s } u l t _ { i , t }$ . By contrast, if the impact of pretreatment trends is less of a concern, we should observe that past values of PostLaunch × $y n _ { - } c o n s u l t _ { i , t }$ can predict reccos , and future values of $P o s t L a u n c h _ { t } \times y n \_ c o n s u l t _ { i , t }$ cannot. The estimation results of the relative time model are presented in Table 10. We find no significant effects in the two-week period before a doctor answers patient questions with sharply increasing effects on the number of patient recommendations in the first few weeks after responses. These results show that the past values of PostLaunch × $y n _ { - } c o n s u l t _ { i , t }$ can predict reccos<sub>it</sub>, and future values of $P o s t L a u n c h _ { t } \times y n \_ c o n s u l t _ { i , t }$ cannot, which rules out the impact of pretreatment trends as a confounding factor.

4.3.5. Placebo Test. We conduct a placebo test to examine whether our results could be driven entirely by chance. The idea of the placebo test proposed here is akin to the framework in Bertrand et al. (2004): we estimate pseudocausal effects that are known to be equal to zero based on a priori knowledge. More specifically, following Bertrand et al. (2004), we randomly generate placebo doctors’ responses, and treated doctors are chosen at random. Because these doctors’ responses are fictitious, a significant “effect” of doctors’ responses at the 5% level (5% significance level) should be found roughly 5% of the time. If, in the placebo test, a significant effect at the 5% level is found at a value much larger than 5% of the time, then our interpretation is that our analysis could be driven by the placebo effect and does not provide significant evidence of a positive effect of doctors’ responses. By contrast, if a significant effect at the 5% level is found at a value about 5%, then our interpretation is that our analysis provides evidence that the positive effect of doctors’ responses is not driven by the placebo effect.

Following Bertrand et al. (2004), we select half the doctors in the sample and designate them as treated doctors.<sup>15</sup> The values of our dependent variable, the number of patient recommendations, do not change. We then estimate regression Equation (1) using these placebo responses. The estimation generates an estimate of the effect of doctors’ responses and a standard error for this estimate. We repeat this ex ercise 1,000 times. Because these doctors’ responses are fictitious, we expect to reject the null hypothesis of no effect roughly 5% of the time (50 times). From our results for the 1,000 runs, we find that the fraction of simulations in which the null hypothesis is rejected is 4.6% (46 times), indicating that our results are unlikely to be driven by the placebo effect.

Table 10. Estimation Results of the Relative Time Model

<table><tr><td>Variables</td><td>(1) Fixed effects</td></tr><tr><td>PostLaunch × yn_consult (t + 2)</td><td>3.145(0.854)</td></tr><tr><td>PostLaunch × yn_consult (t + 1)</td><td>4.075(1.112)</td></tr><tr><td>PostLaunch × yn_consult (t + 0)</td><td>52.31***(3.873)</td></tr><tr><td>PostLaunch × yn_consult (t - 1)</td><td>43.27***(3.554)</td></tr><tr><td>PostLaunch × yn_consult (t - 2)</td><td>21.33***(3.145)</td></tr></table>

Note. Robust t-statistics in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 4.4. The Quality of Doctors’ Responses Based on Text Information

In the previous analysis, we have focused on the quantity of doctors’ responses. In this subsection, we further examine the quality of doctors’ responses based on the text information and show that higherquality responses have a larger impact on patient recommendations. Following prior literature on content quality (McClure 1987, Lee et al. 2015), we use two measures to quantify the quality of doctors’ responses: (1) word count and (2) the Flesch reading ease score. In the setting of a Q&A forum, Lee et al. (2015) argue that answers containing more words are more likely to be of high quality. The second measure, the Flesch reading-ease score, is a readability test designed to indicate how difficult a passage in English is to understand (McClure 1987). In the Flesch readingease test, higher scores indicate material that is easier to read; for example, Florida requires that life insurance policies have a Flesch reading-ease score of 45 or greater.<sup>16</sup> In our context, a high-quality response should be easy to understand. We estimate the following regression model:

$$
\begin{array}{r l} r e c c o s _ {i t} = & c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ & + \beta_ {2} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t}) \\ & + \beta_ {3} a v g \_ w o r d s _ {i t} + \beta_ {4} F s c o r e _ {i t} \\ & + \beta_ {5} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times a v g \_ w o r d s _ {i t}) \\ & + \beta_ {6} (P o s t L a u n c h _ {t} \times y n \_ c o n s u l t _ {i t} \times F s c o r e _ {i t}) \\ & + \beta_ {7} C o n t r o l s + \varepsilon_ {i t}, \end{array}\tag{12}
$$

where avg words is the average number of words in a doctor’s response, and Fscore is the average Flesch reading-ease score of a doctor’s responses. In Table 11, we find that the coefficients on the triple interaction terms are significantly positive, which suggests that the impact of higher-quality responses on patient recommendations is stronger.

Table 11. The Moderating Impact of Response Quality

<table><tr><td>Variables</td><td>(1) Fixed effects</td></tr><tr><td>PostLaunch</td><td>5.326***(11.26)</td></tr><tr><td>PostLaunch × yn_consult</td><td>14.27***(10.33)</td></tr><tr><td>PostLaunch × yn_consult × avg_words</td><td>0.225***(3.247)</td></tr><tr><td>PostLaunch × yn_consult × Fscore</td><td>0.954***(5.658)</td></tr></table>

Note. Robust t-statistics in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 5. Managerial Implications

In this study, we have provided insights into the understanding of drivers for increased recommendations for doctors in an online healthcare-services marketplace. The identification of these drivers and their directionality, interplay, and magnitude of impact are all of direct relevance to site promoters and managers as well as users. Our research studies different variables across the field, namely (1) doctor attributes, such as experience, fees, and education, (2) site features, such as activity on the Q&A forum and an appointment-booking option, and (3) the intensity of competition in Q&A responses—all being of significant interest to managers.

Healthcare portals are gaining in popularity, connecting doctors with potential consumers of healthcare services. As online search and transaction marketplaces, they bring both sides of the market onto the same platform. Managers or platform owners seek to create value by increasing the number of users on either side of demand and supply of services. User-generated activity on Q&A forums of such sites reduces information asymmetry and indicates an increased adoption by either side. Because both healthcare portals and the Q&A forums on these portals are relatively new, the dynamics of usage of such portals is an underresearched area, and this paper attempts to fill the gap with insights for managers.

First, our results show the benefit of the introduction of a Q&A feature on healthcare portals from the viewpoint of all stakeholders. For consumers of healthcare services, the Q&A feature provides an additional distinguishing variable in selecting a doctor, as indicated by a rise in overall recommendations for doctors and, more so, a disproportionate rise in recommendations for doctors responding to questions compared with nonrespondents. With the patient recommendations driving business, it is thus in a doctor’s interest to respond to patients’ questions. In particular, a more accurate link between doctors’ responses and patient satisfaction can provide guidance for a doctor with certain characteristics (e.g., experience, qualifications, and specialty in mainstream medicine or in traditional/alternative medicine) about whether to make social media efforts (responding to patient questions). For promoters and managers of healthcare portals, adoption by one side (consumers) creates value for the other side (doctors), and vice versa; it iteratively increases traffic, thereby justifying the introduction of the feature.

Second, our research shows that an experienced doctor attracts more recommendations for answers. An experienced doctor would be expected to attach more value to the doctor’s time, as would the doctor’s patients, compared with a doctor with lesser experience. As such, although answering for free on Q&A forums would seem unattractive because of the opportunity cost of time being higher for experienced doctors, the higher “bang for the buck” in the form of higher recommendations for an answer by an experienced doctor would justify their adoption of this new feature and answering questions on Q&A forums. Given that patients seek quality over quantity in responses, managers should create such features and incentives as recommendations on their home page or likes on answers that make it attractive for experienced doctors to participate in Q&A forums. An interesting finding is also that in the high-end market, prospective patients are quality sensitive. They value a doctor’s recommendations and use Q&A forum responses as indicator of quality. This is not so in the price-conscious low-end market, in which low doctor fees seem to be the dominant criterion for selection (rather than quality).

Finally, a key managerial implication is that the provision of an appointment-booking option can significantly increase recommendations. This feature eases the transaction cost for users and doctors both and is a key driver of value for the platform too. Our research shows increased recommendations for doctors with a higher level of ease of appointment booking. Managers should use this finding to promote site usage among both doctors and users.

## 6. Conclusions

Healthcare portals provide a low-search-cost alternative for prospective healthcare consumers. Additionally, the ease of transaction and the availability of a larger choice pool make the online marketplace for medical services attractive for patients and doctors. The online response feature is not unique in online healthcare portals. For instance, restaurant owners can respond to online consumer reviews on Yelp (Kumar et al. 2018). Our findings can be generalized to the context in which information asymmetry exists between service providers and consumers. Online responses can be an effective way to signal the underlying quality of services and products. A platform owners’ dream scenario is one in which either side iteratively leads to increased adoption of the other side. Responding to consumer comments helps reduce information asymmetry on different UGC platforms, and through this well-engineered feature, user-generated content can drive traffic, influence performance variables, and set in motion a virtuous cycle of growth of markets. Our paper provides critical insights into dynamics of Q&A forums, delineating the role of attributes, competition, and site features.

Our research can be extended and augmented in several ways. Our study indicates the impact of various doctor, site, and environmental factors on recommendations for doctors. Future research could also explore the impact on other performance metrics of doctors, such as the volume of patients and revenue. Second, we could study the differential impact on doctors in individual clinics, midsize multispecialty clinics, and large hospitals to quantify the impact of establishment types on performance. Third, research can also be done into content analysis of responses by doctors to distinguish variability in recommendations from doctors with similar profiles by calculating the variability of topics addressed by the same doctor across the forum, speed of response since posting of a question, sentiment values, and so on. Fourth, the endogeneity of the moderators is a limitation of the present study because we have mainly focused on the endogeneity issues of the main treatment: doctors’ online responses. A potential avenue for further research is to find exogenous shocks for the moderators. Finally, our work also sets the stage for studying the impact of other value-added services on either side of market. For example, addition of blogs by doctors on their home pages, a feature added by the portal recently, could also be studied using similar empirical identification strategies. As online healthcare marketplaces grow in adoption, range of services, and features, research could highlight and provide evidence of levers for such growth.

## Endnotes

<sup>1</sup> In the code of ethics regulation published by the medical council of India, “A physician shall not make use of him/her (or his/her name) as subject of any form or manner of advertising or publicity through any mode either alone or in conjunction with others which is of such a character as to invite attention to him or to his professional position, skill, qualification, achievements, attainments, specialities, appoint ments, associations, affiliations or honours and/or of such character as would ordinarily result in his self-aggrandizement. A physician shall not give to any person, whether for compensation or otherwise, any approval, recommendation, endorsement, certificate, report or statement with respect of any drug, medicine, nostrum remedy, surgical, or therapeutic article, apparatus or appliance or any commercial product or article with respect of any property, quality or use thereof or any test, demonstration or trial thereof, for use in connection with his name, signature, or photograph in any form or manner of advertising through any mode nor shall he boast of cases, operations, cures or remedies or permit the publication of report thereof through any mode. Printing of self-photograph, or any such material of publicity in the letter head or on sign board of the consulting room o any such clinical establishment shall be regarded as acts of self advertisement and unethical conduct on the part of the physician.” See https://www.mciindia.org/documents/rulesAndRegulations Ethics%20Regulations-2002.pdf (last accessed November 24, 2017)

<sup>2</sup> See http://timesofindia.indiatimes.com/business/india-business Uberisation-disrupts-multiple-sectors/articleshow/56027615.cms (last accessed March 5, 2017).

<sup>3</sup> The site in consideration also offers paid questions for which the privacy of users/patients is maintained, but we focus only on free questions on public forums. Also, in this paper, we use the terms “user” and “patient” interchangeably.

<sup>4</sup> The institutional details of the Indian healthcare market can be found in Online Appendix D.

<sup>5</sup> See http://www.bmj.com/content/351/bmj.h5489/rr (last accessed January 5, 2018).

<sup>6</sup> There is a widespread use of traditional medicine across developing countries (Asia, Africa, and Latin America) with rapidly emerging markets in North America and Europe; see http://www.who.int medicines/publications/traditional/trm\_strategy14\_23/en/ (last accessed December 26, 2017).

<sup>7</sup> See https://www.urmc.rochester.edu/encyclopedia/content.aspx? ContentTypeID=85&ContentID=P00189 (last accessed December 27, 2017).

<sup>8</sup> See http://www.thehindu.com/news/cities/bangalore/practo -becomes-worlds-largest-appointment-booking-platform-acquires -qikwell/article7685609.ece (last accessed July 6, 2017).

<sup>9</sup> See https://www.cc-seas.columbia.edu/preprofessional/health/types/ allopathic.php (last accessed July 6, 2017).

<sup>10</sup> See http://www.census2011.co.in/ (last accessed July 6, 2017).

<sup>11</sup> A baseline specification is presented in Online Appendix A.

<sup>12</sup> See http://www.newsmax.com/FastFeatures/Ayurvedic-medicine -Homeopathic-remedies/2010/10/11/id/373236/ (last accessed July 6, 2017).

<sup>13</sup> Note that we have reduced one degree in the time dummies; otherwise, there is a perfect collinearity problem in the regression

<sup>14</sup> Intuitively, this means that for the impact of online responses to disappear, the unobserved confounder has to cause a doctor to be six times as likely as another doctor to receive treatment (assuming that the two doctors have the same observable characteristics).

<sup>15</sup> We also change the number of treated doctors to the empirically observed number in our data and conduct an alternative placebo intervention. The results are similar.

<sup>16</sup> See http://law.onecle.com/florida/title-xxxvii/627.4145.html (last accessed January 26, 2018).

## References

Abadie A (2005) Semiparametric difference-in-differences estimators. Rev. Econom. Stud. 72(1):1-19

Abraham J, Sick B, Anderson J, Berg A, Dehmer C, Tufano A (2011) Selecting a provider: What factors influence patients’ decision making? J. Healthcare Management 56(2):99–116.

Angrist JD, Pischke JS (2008) Mostly Harmless Econometrics: An Em piricist’s Companion (Princeton University Press, Princeton, NJ)

Aral S, Walker D (2014) Tie strength, embeddedness, and social in fluence: A large-scale networked experiment. Management Sci. 60(6):1351–1616.

Arrow KJ (1963) Uncertainty and the welfare economics of medical care. Amer. Econom. Rev. 53(5):941–973.

Autor DH (2003) Outsourcing at will: The contribution of unjust dismissal doctrine to the growth of employment outsourcing J. Labor Econom. 21(1):1–42.

Ba S, Pavlou PA (2002) Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. Management Inform. Systems Q. 26(3):243–268.

Bapna R, Qiu L, Rice S (2017a) Repeated interactions vs. social ties: Quantifying the economic value of trust, forgiveness, and reputation using a field experiment. MIS Quart. 41(3):841–866.

Bapna R, Ramaprasad J, Umyarov A (2017b) Monetizing freemium communities: Does paying for premium increase social engagement? MIS Quart. 42(3):719–735.

Bardhan I, Oh JH, Zheng Z, Kirksey K (2014) Predictive analytics for readmission of patients with congestive heart failure. Inform. Systems Res. 26(1):19–39.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1): 249–275.

Bolton GE, Katok E, Ockenfels A (2004) How effective are electronic reputation mechanisms? An experimental investigation. Management Sci. 50(11):1587–1602.

Brambor T, Clark WR, Golder M (2005) Understanding interaction models: Improving empirical analyses. Political Anal. 14(1): 63–82.

Bronner AE, de Hoog R (2010) Consumer generated vs. marketer generated websites in consumer decision making. Internat. J. Market Res. 52(2):231–248.

Burtch G, Ghose A, Wattal S (2013) An empirical examination of the antecedents and consequences of contribution patterns in crowd funded markets. Inform. Systems Res. 24(3):499–519.

Butler ES, McGlone T (2002) Consumers ranking of criteria for selection of a primary care physician. Issues Inform. Systems 3(1): 56–62.

Chatterjee S, Hadi AS (2012). Regression Analysis by Example, 5th ed. (John Wiley & Sons, Hoboken, NJ).

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chiappori PA, Oreffice S, Quintana-Domeque C (2012) Fatter attraction: Anthropometric and socioeconomic matching on the marriage market. J. Political Econom. 120(4):659–695.

Daugherty T, Eastin MS, Bright L (2008) Exploring consumer motivations for creating user-generated content. J. Interactive Advertising 8(2):16–25.

Deledda G. Moretti E. Rimondini M. Zimmermann C (2013) How patients want their doctor to communicate. A literature review on primary care patients’ perspective. Patient Ed. Counseling 90(3):297–306.

Demirezen EM, Kumar S, Sen A (2016) Sustainability of healthcare information exchanges: A game-theoretic approach. Inform. Systems Res. 27(2):240–258.

Deogaonkar M (2004) Day-to-day decision making as a physician in India. Indian J. Medical Ethics 2(3):86–87.

Forbes Communication Council (2016). Five ways to incorporate user generated content into your branding efforts. Forbes. Accessed November 30, 2016, https://www.forbes.com/sites/ forbescommunicationscouncil/2016/11/30/five-ways-to-incorporate -user-generated-content-into-vour-branding-efforts/2/#6c4b8530459e

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Freed GL, Dunham KM, Clark SJ, Davis MM, Pediatrics RA (2010) Perspectives and preferences among the general public regarding physician selection and board certification. J. Pediatrics 156(5): 841–845.

Gao GG, Greenwood BN, Agarwal R, McCullough JS (2015) Vocal minority and silent majority: How do online ratings reflect population perceptions of quality? MIS Quart. 39(3):565–589.

Garg R, Smith MD, Telang R (2011) Measuring information diffusion in an online community. J. Management Inform. Systems 28(2): 11–38.

Gaynor M (1994) Issues in the industrial organization of the market for physician services. J. Econom. Management Strategy 3(1):211–255.

Goh KY, Heng CS, Lin Z (2013) Social media brand community and consumer behavior: Quantifying the relative impact of user-and marketer-generated content. Inform. Systems Res. 24(1):88–107.

Granger CW (1969) Investigating causal relations by econometric models and cross-spectral methods. Econometrica 37(3):424–438.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride sharing and motor vehicle ho micides. MIS Quart. 41(1):163–187.

Gu B, Ye Q (2014) First step in social media: Measuring the influence of online management responses on customer satisfaction. Production Oper. Management 23(4):570–582.

Guo S, Fraser M (2010) Propensity Score Analysis: Statistical Method and Applications (Sage Publications, Los Angeles)

Hanna N, Shoenbachler DD, Gordon GL (1995) Physician choice criteria: Factors influencing patient selection of generalists vs. specialists. Health Marketing Quart. 12(2):29–42.

Hart K, Sarma A (2014). Perceptions of answer quality in an online technical question and answer forum. Proc. 7th Internat. Workshop Cooperative Human Aspects Software Engrg. (ACM, Hyderabad, India), 103–106.

Heinrich CM, Maffioli A, Vazquez G (2010) A Primer for Applying Propensity-Score Matching (Inter-American Development Bank, Washington, DC).

Jayakrishnan T, Jeeja MC, Kuniyil V, Paramasivam S (2016). Increasing out-of-pocket healthcare expenditure in India—Due to supply or demand? Pharmacoeconomics 1:105.

KeyIn (2015). Meet KeyIn: Better purchasing decisions with insigh from peers. Vegastech. Accessed July 22, 2015, https:/ vegastech.com/meet-vegas-tech-startups/meet-keyin-better -purchasing-decisions-with-insight-from-peers/.

Keele L (2010). An overview of rbounds: An R package for Rosenbaum bounds sensitivity analysis with matched data. Working paper, Georgetown University, Washington, DC

Kumar R (2016) Frequently asked questions about family medicine in India. J. Family Medicine Primary Care 5(1):3–6.

Kumar N, Qiu L, Kumar S (2018) Exit, voice, and response in digital platforms: An empirical investigation of online managemen response strategies. Inform. Systems Res. 29(4):849–870.

Lau AY, Kwok TM (2009). Social features in online communities for healthcare consumers—A review. Ozok AA, Zaphiris P, eds. Internat. Conf. Online Communities Social Comput. Lecture Notes in Computer Science, vol. 5621 (Springer, Berlin, Heidelberg), 682–689.

Lee SY, Rui H, Whinston A (2015) Content quality assessment through context-free linguistic features: Application to community-based question answering platforms. Carte T, Heinzl A, Urquhart C, eds. Internat. Conf. Inform. Systems (Association for Information Sys tems, Atlanta).

Li X (2016) Could deal promotion improve merchants’ online reputations? The moderating role of prior reviews. J. Management Inform. Systems 33(1):171–201.

Lovitt R (2016). New research surprising health benefits online health forums. https://insightcenter.realself.com. Accessed June 29, 2016, https://insightscenter.realself.com/new-research-surprising -health-benefits-online-health-forums/.

Lu SF, Rui H, Seidmann A (2017) Does technology substitute fo nurses? Staffing decisions in nursing homes. Management. Sci. 64(4):1842–1859.

McClure GM (1987) Readability formulas: Useful or useless? IEEE Trans. Professional Comm. 30(1):12–15.

Mithas S, Krishnan MS (2009) From association to causation via a potential outcomes approach. Inform. Systems Res. 20(2):295–313.

Murton Beet L, Handley A (2018) B2C Content Marketing—2019 Benchmarks, Budgets, and Trends—North America (Content Marketing Institute, New York).

Nambisan P (2011) Information seeking and social support in online health communities: Impact on patients’ perceived empathy. J. Amer. Medical Informatics Assoc. 18(3):298–304.

Nurvala J-P (2015) Uberisation is the future of the digitalised labour market. Eur. View 14(2):231–239.

Oyebode O, Kandala NB, Chilton PJ, Lilford RJ (2016) Use of traditional medicine in middle-income countries: A WHO-SAGE study. Health Policy Planning 31(8):984–991.

Paul SA, Hong L, Chi EH (2012) Who is authoritative? Understand ing reputation mechanisms in quora. Malone TW, von Ahn L, eds. Collective Intelligence Conf. 2012: Proc.

Poch R, Martin B (2015) Effects of intrinsic and extrinsic motivation on user-generated content. J. Strategic Marketing 23(4):305–317.

Presi C, Saridakis C, Hartmans S (2014) User-generated content behaviour of the dissatisfied service customer. Eur. J. Marketing 48(9/10):1600–1625.

Proserpio D, Zervas G (2017) Online reputation management: Estimating the impact of management responses on consumer reviews. Marketing Sci. 36(5):645–665.

Rice SC (2012) Reputation and uncertainty in online markets: An experimental study. Inform. Systems Res. 23(2):436–452.

Rochaix L (1989) Information asymmetry and search in the market fo physicians’ services. J. Health Econom. 8(1):53–84.

Rosenbaum PR (2002) Observational Studies, 2nd ed. (Springer, New York).

Rudra S, Kalra A, Kumar A, Joe W (2017) Utilization of alternative systems of medicine as healthcare services in India: Evidence on AYUSH care from NSS 2014. PLoS One 12(5):e0176916.

Singh PV, Sahoo N, Mukhopadhyay T (2014) How to attract and retain readers in enterprise blogging? Inform. Systems Res. 25(1): 35–52.

Srikanth RP (2015) Practo is the world’s largest healthcare appointment booking platform: Shashank ND, Founder, Practo. DataQuest India. Accesseded January 5, 2017, http://www.dqindia.com/practo -is-the-worlds-largest-healthcare-appointment-booking-platform -shashank-nd-founder-practo/.

Spence M (1973) Job market signaling. Quart. J. Econom. 87(3): 355–374.

Stock JH (2010) The other transformation in econometric practice: Robust tools for inference. J. Econom. Perspectives 24(2):83–94.

Tucker C, Zhang J (2011) How does popularity information affect choices? A field experiment. Management Sci. 57(5):828–842.

Wang A, Zhang M, Hann IH (2017) Socially nudged: A quasi experimental study of friends’ social influence in online prod uct ratings. Inform. Systems Res. 29(3):641–655.

Wei Z, Lin M (2016) Market mechanisms in online peer-to-pee lending. Management Sci. 63(12):4236–4257.

Xu Y, Armony M, Ghose A (2016) The effect of online reviews on physician demand: A structural model of patient choice. Working paper, University of Illinois at Urbana–Champaign, Champaign.

Yan L, Tan Y (2014) Feeling blue? Go online: An empirical study of social support among patients. Inform. Systems Res. 25(4):690–709.

Yan L, Tan Y (2017) The consensus effect in online health-care communities. J. Management Inform. Systems 34(1):11–39.

Yaraghi N, Du AY, Sharman R, Gopal RD, Ramesh R (2014) Health information exchange as a multisided platform: Adoption, us age, and practice involvement in service co-production. Inform. Systems Res. 26(1):1–18.

Ye S, Gao G, Viswanathan S (2014) Strategic behavior in online reputation systems: Evidence from revoking on eBay. MIS Quart. 38(4):1033–1056.
