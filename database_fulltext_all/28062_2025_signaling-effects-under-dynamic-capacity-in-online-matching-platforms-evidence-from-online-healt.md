---
otero_id: 28062
otero_key: "3PTB2BT4"
title: "Signaling Effects Under Dynamic Capacity in Online Matching Platforms: Evidence from Online Health Consultation Communities"
authors: "Liwei Chen; Arun Rai; Wei Chen; Xitong Guo"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0150"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Signaling Effects Under Dynamic Capacity in Online Matching Platforms: Evidence from Online Health Consultation Communities

Liwei Chen,<sup>a,</sup>\* Arun Rai,<sup>b</sup> Wei Chen,<sup>c</sup> Xitong Guo<sup>d,</sup>\*

<sup>a</sup> Carl H. Lindner College of Business, University of Cincinnati, Cincinnati, Ohio 45221; <sup>b</sup> Robinson College of Business, Georgia State University, Atlanta, Georgia 30303; <sup>c</sup> School of Business, University of Connecticut, Stamford, Connecticut 06901; <sup>d</sup> School of Management, Harbin Institute of Technology, Harbin, China

\*Corresponding authors

Contact: liwei.chen@uc.edu, https://orcid.org/0000-0002-7596-9890 (LC); arunrai@gsu.edu, https://orcid.org/0000-0002-3655-7543 (AR); weichen@uconn.edu, https://orcid.org/0000-0002-0963-7839 (WC); xitongguo@hit.edu.cn, https://orcid.org/0000-0002-9569-0299 (XG)

Received: March 13, 2021 Revised: October 1, 2022; July 26, 2023; November 27, 2023 Accepted: January 18, 2024 Published Online in Articles in Advance: March 28, 2024

https://doi.org/10.1287/isre.2021.0150

Copyright: © 2024 INFORMS

Abstract. Match formation is challenging in online matching platforms where suppliers are subject to dynamic capacity constraints. We provide a theoretical foundation for understanding how online matching platforms support the transmission and triangulation of multisource information for consumers to infer provider service quality and dynamic capacity states, and achieve desirable matching outcomes. Situating this study in the context of an online health consultation community (OHCC) and drawing upon signaling theory, we theorize how physicians’ owned and earned signals influence physicians’ voluntary online consultations with new patients they have not consulted with previously. Importantly, we articulate how these signaling effects are contingent upon physicians’ dynamic capacity in OHCC. We collected longitudinal data from a large OHCC in China and used a hidden Markov model (HMM) to characterize the dynamic physician capacity in the OHCC and test the hypotheses. Our findings reveal that service professionals’ owned and earned signals interactively work together to balance supply and demand dynamically, and thereby facilitating matchmaking. In OHCCs, where physicians provide voluntary service beyond their primary jobs at hospitals, we find that owned and earned signals increase patient consultations in different patterns contingent upon physicians’ capacity states. In addition, we discover the complementary and substitute relationships between owned signals and earned signals change when physicians are in different capacity states. The findings have significant implications for our understand ing of online match formation under dynamic capacity constraints and the design of OHCCs.

History: Yulin Fang, Senior Editor; Choon Ling Sia, Associate Editor.

Funding: X. Guo acknowledges the support from the National Natural Science of China [Grants 72125001, 72071054, 72293584].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0150.

Keywords: online match formation • dynamic capacity states • hidden Markov model • online health consultation communities • signaling theory • complementary and substitute relationships

## 1. Introduction

Online matching platforms have drastically changed how people search for, select, and form matches in various domains. For example, online labor markets, such as Upwork and MTurk, help match employers and freelancers; home-sharing platforms, such as Airbnb, enable homeowners to provide short-term rental services to travelers; and online health consultation communities (OHCCs), such as DoctorOnDemand and WebMD, allow physicians to provide remote health consultations to patients.

Despite the prevalence of these online matching platforms, achieving a successful match typically requires extensive search and screening and thus remains a costly process. To form satisfactory matches, platforms have designed information technology (IT) artifacts to facilitate the utilization of informative signals and reduce user uncertainty in the matching process (Arnosti et al. 2021). While prior research has demonstrated how signaling can help improve matching outcomes (Coles et al. 2013, Halaburda et al. 2018), emerging evidence indicates that signaling may not always be beneficial (Arnosti et al. 2021). Misaligned signaling can even reduce matches and increase congestion on platforms (Kushnir 2013, Arnosti et al. 2021).

Signaling for match formation on online platforms is challenging due to the involvement of multiple stakeholders, the utilization of various types of signals, and suppliers’ dynamic capacity constraints. To start with, online matching involves signaling among multiple stakeholders (Guo et al. 2017, Wang et al. 2021). As stakeholders may bring unique expertise and experience when interacting with others in a community, they may generate different types of signals regarding unobservable characteristics (Mollick and Nanda 2016). For example, while suppliers can present their professional credentials, customers can also often share their service experiences on platforms to indicate suppliers service quality. As a result, effective signaling among multiple stakeholders is essential for successful matching. Second, online matching platforms serve as conduits not only for conveying signals suppliers already have prior to onboarding but also for offering additional channels through which suppliers can acquire new signals by virtue of their activities on such platforms (Zhou et al. 2022). These signals can be generated by algorithms and data analytics that monitor suppliers’ performance and can also be aggregated from discrete feedback, such as reviews, ratings, and endorsements. Acquiring such signals is mutually beneficial as they enhance suppliers’ reputation on platforms while also providing customers valuable information for their matching requests and outcomes. Third, online matching relies on suppliers’ capacity (Bojd and Yoganarasimhan 2022). Since suppliers can autonomously adjust the amount of time and effort they allocate to online platforms, such allocation is time variant, unobservable, and uncertain, which we refer to as their dynamic capacity (Horton 2019). The dynamic capacity suppliers devote to online matching platforms may derive from their overall workload and availability. For example, freelancers may be temporarily occupied by multiple projects and not able to accept new ones. Similarly, on a particular day, physicians may find themselves overwhelmed with their primary jobs to voluntarily consult with online patients.

The above features collectively make online matching platforms a context with tremendous uncertainty. Moreover, the uncertainty in suppliers’ capacity is often not reflected on their profiles or observable to platforms (Horton 2019). Such uncertainty requires suppliers and customers to make matching decisions with incomplete information and may influence how suppliers can be differentiated by distinct types of signals. Specifically, the sources of such signals are not limited to suppliers but also involve users based on their experiences with suppliers, as well as platforms based on the types of information they make visible. In this situation, the distinctive characteristics of online matching platforms requires a novel lens to understand the typology of signals in this context and how they work individually and interactively in supporting matchmaking under uncertainty.

Motivated by this overarching objective, we extend signaling theory and identify suppliers’ dynamic capacity as a contingency that may affect the effectiveness of different types of signals. Reviewing the literature on signaling effectiveness under capacity constraints, we find that recent work has explored different interventions for improving signaling efficacy and match formation in various contexts, such as disclosing workers’ capacity information in online labor markets (Horton 2019), implementing personalized ranking algorithms in Airbnb search engines (Fradkin 2017), and pairing demand information with framing cues in online dating platforms (Huang et al. 2022a). Most of these studies have assumed that suppliers capacity is static and have discussed how uncertainty about suppliers’ capacity impedes signaling effectiveness and matching efficiency on different online matching platforms (Fradkin 2017, Horton 2019). However, suppliers’ capacity often exhibits significant dynamism and fluctuates over time. In general, fitting a static model to data generated by a dynamic process may result in misleading findings (Chen et al. 2018). To our knowledge, no prior work has explicitly considered the uncertain changes in supply-side capacity that may influence the effectiveness of signaling for match formation on online platforms. Thus, there remains an essential gap in our understanding of how signaling effects on match formation are contingent upon changes in supply-side capacity.

To bridge this knowledge gap, we situate our study in the context of an online health consultation community where physicians provide voluntary remote consultations to patients. OHCCs are platforms where physicians offer voluntary consultations to patients, often without a direct affiliation to a specific hospital. In OHCCs, match formation involves efforts from both physicians and potential patients. Potential patients search, select, and request consultation services from physicians. The pursued physicians determine whether to accept or reject the requests based on their current capacity. The two sides collectively determine the matched patient consultations. An unsuccessful pursuit may be consequential to an OHCC platform as it requires additional resources to redirect the request to alternate physicians. It also takes the patient longer to obtain the necessary consultation and hurts the platform in the long term due to inefficient matching. In the context of OHCCs, match formation refers to physicians’ online consultations matched with new patients who they have not consulted with previously (hereafter referred to as matched patient consultations). Accord ingly, our first research question (RQ1) is, how are the signaling effects on matched patient consultations contingent upon physicians’ dynamic capacity in OHCCs?

Regarding the signals, we primarily focus on differentiating between two categories of signals in OHCCs based on how the signals are generated. First, owned signals reflect credentials or professional status possessed by physicians that indicate unobservable service characteristics (Li et al. 2019b, Chen et al. 2020b, Huang et al. 2022b). For example, physicians can display their competence attributes, such as professional credentials and career achievements, in their OHCC digital profiles (i.e., competence-attribute signals). Second, earned signals refer to information generated through service providers’ efforts in the OHCC that indicate unobservable service characteristics. On the one hand, OHCCs can trace, aggregate, and disclose physicians’ prosocial behaviors (i.e., prosocial-behavior signals). These behaviors may signal physicians’ level of activity and commitment in contributing to the OHCC beyond consultations. On the other hand, physicians’ efforts in helping patients can also be reflected by the aggregated experience shared by a large pool of peer patients.<sup>1</sup> OHCCs consolidate extensive, varied, and uncoordinated individual service experiences reported by patients and display the aggregated collective experience to potential patients (e.g., volume and valence of patient reviews). Instead of collecting discrete information from personal networks, potential patients can easily, quickly, and frequently access physicians’ earned signals in an OHCC and thereby infer their service quality.

Physicians’ owned and earned signals are prominently displayed in an OHCC. These signals are commonly used as indicators of physicians’ service quality and are, consequently, integral to the decision-making process of potential patients. It is crucial to understand, though, that neither type of signal alone is sufficient to mitigate potential patients’ uncertainty regarding physicians’ services. These signals may also be interpreted as a representation of physicians’ capacity, adding another layer to the decision-making process. The timevariant nature of physicians’ actual capacity further complicates this interpretation and the matching between patients and physicians. As a result, the collective impact of physicians’ signals on matched patient consultations remains unclear when physicians’ capacity is unobservable and fluctuates over time. This scenario sets the stage for our second research question (RQ2): how do physicians’ owned and earned signals individually and interactively influence matched patient consultations given physicians’ dynamic capacity in OHCCs?

To account for physicians’ dynamic and unobservable capacity, we use a hidden Markov model (HMM) approach, which allows latent capacity states to change across physicians over time. This HMM approach captures the matching process by incorporating timevariant capacity states and accounting for the transitions between these states. We employ Bayesian estimation to jointly estimate the state-transition probability and the signaling effects on matching outcomes conditional on the dynamic capacity states. Situating our empirical work in one of the largest OHCCs in China where physicians offer voluntary consultations without a fee, we collected data from 526 cardiovascular medicine physicians’ profile pages in the OHCC over two years. We find that physicians’ capacity may fluctuate between two latent states: a low-capacity state (i.e., phy sicians have a lower capacity to provide online consultation services—State L) and a high-capacity state (i.e., physicians have a higher capacity to provide online consultation services—State H). While owned and earned signals influence potential patients’ choice of physicians, their influence on the final matching, i.e., physicians’ acceptance of patient consultation requests, can vary significantly by physicians’ latent capacity states. We found an intriguing interaction between owned and earned signals. Specifically, when physicians are in a low-capacity state, their prosocial-behavior signals amplify the impact of their competence-attribute signals on matched patient consultations to a greater extent. However, when physicians are in a high-capacity state, volume and valence of patient reviews of the physician substitute for competence-attribute signals to a greater extent.

Our work makes several contributions. Theoretically, we contribute to signaling theory by theorizing a typol ogy of signals and uncovering suppliers’ dynamic capacity as a contingency in altering the effectiveness of different signals. We provide a theoretical explanation for how different signals work individually and interac tively in supporting matchmaking under uncertainty. We also extend the online matching platform literature by introducing the time-variant and uncertain nature of supply-side capacity in match formation. We use HMM as a novel approach to explicitly capture the timevariant hidden capacity in our model. In particular, we explore the impacts of signals on physician-patient matching at different levels of physicians’ time-variant latent capacity. In addition, we differentiate between owned and earned signals in an OHCC, theorize the dual roles of these signals in indicating physicians’ service quality and capacity, and discover the respective and interactive impacts of these signals on matching physicians with potential patients. Practically, we con tribute to how OHCC platforms can be designed by providing an HMM approach to capture physicians time-variant capacity states. Platform designers may utilize such information to provide customized recommendations and prioritize the presentation of different signals. We also offer suggestions for physicians to manage their signaling strategies in OHCCs and enhance matched patient consultations based on their dynamic capacity states.

## 2. Theoretical Background 2.1. Match Formation in OHCCs

OHCCs are emerging online matching platforms that allow physicians to provide remote health consultations to patients. Revamping the process of health consultations, OHCCs have attracted growing research interest and attention in the information systems (IS)

discipline. Prior literature has discussed the potential of online health consultations to create value, such as improving patients’ health outcomes and well-being (Johnston et al. 2013, Yan and Tan 2014, Liu et al. 2020), generating social and economic returns for physicians (Guo et al. 2017), increasing service demand in offline healthcare channels (Wang et al. 2020), and reducing rural-urban health disparities (Goh et al. 2016).

Despite the potential value of online health consultations, successful matchmaking between physicians and potential patients remains challenging. One important source of this challenge arises from physicians’ unobservable dynamic capacity. In ${ \mathrm { O H C } } { \bar { \mathrm { C } } } s ,$ physicians are not obligated to provide a fixed amount of service and have the autonomy to decide their level of service supply. They may not be able to accept all the service requests they receive, especially if the requests exceed their allocated capacity for the focal OHCC. While physicians’ capacity for online health consultations may change significantly due to their unpredictable schedules at their primary hospital jobs (Yu et al. 2020) or changes in their motivation, these changes are not visible to OHCC platforms or to potential patients.

## 2.2. Supply-Side Capacity and Dynamics

The supply-side capacity constraint challenge is not unique to the OHCC context and has been identified in recent literature as a crucial factor that obstructs matchmaking in online matching platforms more generally (Allon et al. 2012, Fradkin 2015). When a supplier faces an increase in demand, the supplier might have limited bandwidth to meet the additional demand, reducing the matching rate and market efficiency. This supplyside capacity constraint is prevalent across online matching platforms, including home-sharing platforms (Burdett et al. 2001), online dating markets (Huang et al. 2022a), and online labor markets (Horton 2019).

Recognizing this challenge, platform design scholars have explored mechanisms to enhance matchmaking under constrained supply capacity. For example, Fradkin (2015) proposed a personalized ranking algorithm for demand-side search results to reduce search friction and increase matches. Viewing information disclosure as a matching mechanism (Tadelis and Zettelmeyer 2015), Horton (2019) explored the value of disclosing workers’ capacity information in online labor markets. Indeed, workers who self-report their availability receive and accept more invitations, thus reducing market congestion. In an online dating market, Huang et al. (2022a) went a step further to explore the disclosure of demand information as an informational intervention to mitigate market congestion. They separated dating requests into those targeting high-demand and lowdemand peers and observed that disclosing demand information shifts attention from high-demand peers to low-demand peers.

A notable yet under-discussed feature of online matching platforms is the dynamic nature of supplyside capacity. Bojd and Yoganarasimhan (2022) noted that suppliers’ past demand is negatively associated with their current demand, indicating that supply-side capacity is not necessarily static but may vary over time. Such uncertain changes in supply-side capacity are especially salient in online health consultations. Physicians, as voluntary service providers in ${ \mathrm { O H C C s } } ,$ are not constrained to a fixed amount of service supply. Instead, they may provide a varying amount of online consultation services over time in an uncertain and time-variant pattern. This dynamic capacity of physicians may stem from multiple sources. First, physicians may be motivated by their interactions with online patients (e.g., gifts from online patients) and reciprocally allocate a different amount of capacity for online health consultations in a time-variant manner. Second, physicians’ primary jobs in hospitals take up a considerable portion of their schedules and may change thei availability for online services (Pan et al. 2021, Yang et al. 2021). These unique features lead to supply-side capacity fluctuations. OHCCs thus serve as an ideal context for exploring the time-variant nature of supply side capacity and its role in matchmaking on online platforms.

## 2.3. Demand-Triggering Signals in OHCCs

In addition to physicians’ dynamic capacity, another factor that makes matchmaking challenging in OHCCs is the triangulation and interpretation of multiple signals by potential patients. To reduce potential patients uncertainty about the quality and capacity of physicians’ online services (Miller and Derse 2002, Li et al. 2018), ${ \mathrm { O H C C s } } ^ { 2 }$ have designed IT features (see Table 1) to convey multiple signals about physicians’ services and help patients make selection decisions.

Based on how the signals are generated, we categorize these signals into two groups: owned signals and earned signals. Owned signals are attributes possessed by service providers that indicate unobservable service characteristics (Xie and Lee 2015, Lovett and Staelin 2016). These signals are independent of the matching platform, are often endorsed by professional institu tions or associations, and are construed as reliable indicators of a provider’s service characteristics. In particular, we focus specifically on competence-attribute (CA) signals, which concern physicians’ education, awards, certifications, experience, and professional credentials. CA signals, which are costly to develop through education and professional training, have been found to reflect their accumulated expertise and be effective in indicating providers’ superior competence in online marketplaces (Lanzolla and Frankort 2016). In OHCCs, physicians display CA signals using selfpresentation tools, such as personal webpages. These signals demonstrate physicians’ competence and ability to deliver effective and reliable health consultations.

Table 1. Physicians’ Service Signals Transmitted by IT Artifacts in OHCCs

<table><tr><td></td><td>General definitions</td><td>Contextual definitions</td><td>Associated IT artifacts</td></tr><tr><td>Owned signals</td><td>Credentials or professional status possessed by service providers that indicate unobservable service characteristics.</td><td>Competence-attribute (CA) signals: A physicians&#x27; education, awards, certifications, experience, and professional credentials that help potential patients infer their unobservable service characteristics.</td><td>Self-presentation tools: a physician&#x27;s personal web page displaying personal attributes, including professional credentials and awards.</td></tr><tr><td>Earned signals</td><td>Information generated through the efforts of service providers in the OHCC that indicate unobservable service characteristics.</td><td>Prosocial-behavior (PB) signals: A physician&#x27;s historical prosocial behaviors in contributing to an OHCC beyond consultations that help potential patients infer their unobservable service characteristics.Volume and valence: Aggregation of individual service experiences with a physician reported by patients in an OHCC.</td><td>Interaction archive: a physician&#x27;s interaction archive recording all the online activities they have engaged in an OHCC.Feedback system: a patient rating system aggregating patients&#x27; varied, uncoordinated ratings of physicians and reflecting patients&#x27; collective experiences with a physician.</td></tr></table>

Earned signals are not directly possessed by service providers but are generated through providers’ servicerelated efforts that can be used to infer unobservable service characteristics (Xie and Lee 2015). In an OHCC, physicians’ efforts can manifest through their participation behaviors in the community and through the aggregation of feedback on service experiences shared by their patients in the community (Chen et al. 2021). To start with, prosocial-behavior (PB) signals effectively communicate the participatory tendencies of physicians in OHCCs, reflecting their degree of engagement and dedication toward advancing the well-being of the community (Zhou et al. 2022). Exemplary prosocial behaviors include providing medical advice for public audiences and disseminating knowledge about specific health conditions. Interaction archives, such as deep profiling tools in OHCCs, keep track of these activities and make them transparent to all community members. As a result, physicians’ prosocial behaviors, which are costly to produce, reflect the extent to which physicians are willing to make an effort and help patients with their health concerns beyond consultations.

Besides physicians’ prosocial behaviors, earned signals can also manifest through the aggregated individual service experiences reported by patients. In particular, patient rating systems aggregate patients extensive, varied, and uncoordinated experiences interacting with physicians and make this aggregated information both transparent through OHCC platforms and broadly accessible to potential patients (Li et al. 2019a, Shukla et al. 2021). In this study, we focus on the volume and the average favorability of the experiences with physicians that are shared by patients (hereafter referred to as volume and valence, respectively) as another two earned signals.

The public disclosure of the above owned and earned signals in OHCCs may lead to different interpretations by potential patients, which collectively influence their interest in pursuing consultation with a given physician. On one hand, potential patients may view these signals as indicators of physicians’ service quality (Chen et al. 2021). On the other hand, these signals may help potential patients anticipate physicians’ service capacity and adjust their expectations and selection decisions (Huang et al. 2022b). We are interested in understanding how potential patients interpret the earned and owned signals about a physician’s service. Such interpretations may influence how the multiple signals work together as substitutes or complements in affecting successful matches for patient consultations given physicians’ dynamic capacity. Accordingly, we propose the research model in Figure 1 and theorize the hypotheses in detail below.

## 3. Hypothesis Development

Drawing upon signaling theory, we adopt a dynamic perspective to understand how physicians’ signals and dynamic capacity influence matched patient consulta tions. In general, effective signals lead to a separation between physicians who do and do not have the signaled qualities (Spence 1973). As potential patients make their selection decisions using signals to infer physicians’ service quality and capacity, physicians decide whether they will accept requests, thereby collectively determining whether matched patient consultations will occur. Our overarching proposition is that the effects of physicians’ signals on matched patient consultations are contingent on their dynamic capacity states. We start with the main effect of each signal and then present the interaction effects between owned and earned signals.

Figure 1. Research Model  
![](/api/attachments/3PTB2BT4/fulltext/images/3953513ba256f00e1fe6f6ccdec30d850da2a3ec66e57b20a06e99f6f31f3429.jpg)

## 3.1. Owned Signals’ Effect on Matched Patient Consultations

First, we expect that CA signals increase matched patient consultations and that this effect is more salient when the physician is in a high-capacity state. As physicians must invest considerable time and effort to undergo professional training and earn certifications (Liu et al. 2019, Fan et al. 2022), physicians with a senior professional title emit a high CA signal that they are more competent to provide high-quality services. From this perspective, CA signals, as an indicator of service quality, attract more demand from potential patients.

When in a high-capacity state, physicians with high CA signals are likely to be seen as more competent to meet increased service demand. In this situation, CA signals likely increase matched patient consultations to a greater extent. However, physicians cannot continuously accept service requests given their limited time and capacity. As accepted requests increase their workload, physicians implicitly transition to a low-capacity state. In this circumstance, high CA signals may not necessarily enhance matched patient consultations since physicians’ limited capacity prevents them from responding to the rising demand. In other words, the effect of CA signals in facilitating successful matches is weakened when physicians are in a low-capacity state. In short, we propose:

Hypothesis 1. CA signals increase matched patient con sultations, and this effect is stronger when a physician is in a high-capacity state.

## 3.2. Earned Signals’ Effect on Matched Patient Consultations

In addition to owned signals, potential patients can access earned signals, including a physician’s prosocial behaviors and the aggregated information about patients experiences with a physician in an OHCC (Li et al. 2019a). We now theorize how earned signals affect successful matches for patient consultations given physicians’ dynamic capacity.

When selecting physicians, potential patients consider not only physicians’ professional competence but also the extent to which they are committed to engaging in OHCC activities (Frampton et al. 2013, Cameron et al. 2015). PB signals capture a physician’s ongoing voluntary behaviors to participate in and contribute to an OHCC. Such prosocial behaviors include how frequently the physician updates their profile and responds to questions in public question-and-answer (Q&A) pools. These behaviors collectively indicate the physician’s credible commitment to fostering physician-patient relationships beyond consultations in the OHCC (Gelhaus 2012).

From potential patients’ perspective, PB signals may indicate two aspects of physicians’ services. As a service-quality cue, PB signals are costly to maintain and require physicians’ ongoing efforts. As a capacity cue, PB signals indicate physicians’ availability to contribute to OHCCs. Collectively, potential patients are more likely to select physicians with high PB signals because they expect these physicians to be willing and available to help them and provide services in OHCCs.

PB signals may be more influential in increasing matched patient consultations when physicians are in a high-capacity state compared with a low-capacity state. With high capacity, physicians with stronger PB signals are motivated and available to accept the service demand, leading to more matched patient consultations. By contrast, in a low-capacity state, although physicians may have revealed their preference to increase their supply of services, the high service demand derived from PB signals may not necessarily yield more matched patient consultations due to physicians’ limited bandwidth. Therefore, we propose the following:

Hypothesis 2. PB signals increase matched patient consultations, and this effect is stronger when a physician is in a high-capacity state.

In terms of the aggregated information about patients experiences, high volume indicates that more patients have previously selected a physician for services and are willing to share their individual experiences with the community. In addition, high valence indicates that patients have shared more favorable experiences with a physician in the community.

Volume and valence may serve as signals of service quality. Consumers tend to focus their attention asymmetrically on popular and more favorable service providers (Huang et al. 2022a). In OHCCs, higher volume or more positive valence may attract potential patients to follow others’ selection and send requests. Potential patients may also use volume and valence to infer physicians’ capacity. They may expect physicians with high volume or high valence to be in high demand and perhaps less likely to accept all the service requests.

From the supply side, physicians may develop a sense of reward when they receive a larger number of ratings or more positive ratings from patients. As a result, they might be more motivated to reciprocate to the focal OHCC and make the effort to accept patient consultation requests. It is easier for physicians to make such extra effort when they are in a high-capacity state. Therefore, we expect the impacts of volume and valence on matched patient consultations are more salient when physicians are in a high-capacity state. Thus, we propose:

Hypothesis 3a. Volume increases matched patient consultations, and this effect is stronger when a physician is in a high-capacity state.

Hypothesis 3b. Valence increases matched patient consultations, and this effect is stronger when a physician is in a high-capacity state.

## 3.3. Owned Signals and Earned Signals Interactive Effect on Matched Patient Consultations

The coexistence of signals provides potential patients with information from multiple sources and can reduce their uncertainty about physicians’ service quality and capacity when selecting a physician. Accordingly, we theorize the interaction effects between owned signals (i.e., CA signals) and earned signals (i.e., PB signals, vol ume, and valence) on matched patient consultations.

3.3.1. Amplification of CA Signals by PB Signals. We expect that PB signals amplify the impact of CA signals on matched patient consultations. As theorized in Section 3.1, high CA signals, which require rigorous validation of physicians’ knowledge and skills, indicate a high level of professional competence to deliver high quality services. While high CA signals underscore competence, they might inadvertently hint at a physician’s potential limited availability. This is where PB signals come to play a role. High PB signals complement CA signals and amplify the impact of CA signals on matched patient consultations. Representing a physician’s behavioral commitment, PB signals demonstrate a physician’s committed willingness and continuous effort to help patients. When combined with professional competence, they offer a holistic view of a physician’s value proposition to potential patients.

The synergy between CA and PB signals creates an amplification effect. A physician’s competence, as indicated by CA signals, establishes foundational trust with potential patients. However, it is the behavioral commitment, as evidenced by PB signals, that elevates this trust, making it more profound and influential. When patients perceive both high competence and high commitment from a physician, they are more likely to trust their assessments of the physician’s quality of care and feel reassured about the physician’s service capacity when making their selection decisions. As a result, matched patient consultations are more likely to be influenced by the physician’s competence when accompanied by a high level of behavioral commitment.

We expect this amplification effect to become even more pronounced in a low-capacity state. In such scenarios, the physician’s dedication, as evidenced by high PB signals, becomes a benchmark of trust. Given the constraints in bandwidth, a physician’s commitment to not just maintain but elevate the quality of care becomes a distinguishing factor. This commitment, especially in the face of rising service demands, is likely to resonate deeply with potential patients. It assures them that the physician is not just competent but is also genuinely invested, by virtue of their revealed behaviors, in the welfare of the OHCC community. Furthermore, in a low-capacity state, mere competence might not suffice. Patients seek assurance that their selected physician will exhibit an exceptional level of dedication, even under capacity constraints. High PB signals offer this assurance, making physicians indispensable under such conditions. Therefore, PB signals likely play a more significant role in enhancing the impact of CA signals and converting stimulated service demand into matched patient consultations when physicians are in a low-capacity state. Hence, we expect the following:

Hypothesis 4. The effect of CA signals on matched patient consultations are amplified by physicians’ PB signals, and this amplification effect is more salient when a physician is in a low-capacity state.

3.3.2. Compensation of CA Signals by Volume and Valence. While CA and PB signals provide a comprehensive understanding of a physician’s competence and commitment, volume and valence offer alternative cues that potential patients consider, especially when CA signals are ambiguous or insufficient. We expect volume and valence compensate for the impact of CA signals on matched patient consultations. A single CA signal, while indicative of a physician’s professional credentials, may not provide enough information for a patient to make a definitive judgment about a physician’s service quality and competence. For example, when a physician presents low CA signals with junior professional credentials in an OHCC, signal receivers may expect the physician to have high capacity while being cautious about service quality. In contrast, observing a physician’s high CA signals with senior professional credentials, potential patients may draw stronger inferences about the physician’s competence and service quality while having uncertain expectations of their capacity. In both cases, potential patients are likely attentive to alternative information. Volume and valence of reviews emerge as compensatory cues, helping patients navigate their uncertainties on CA signals as service-quality and service-capacity cues.

High volume, representing a multitude of patient experiences, acts as a robust form of social testimony. It provides potential patients with a broader perspective on a physician’s expertise and competence. When numerous patients share their experiences, it offers a more diversified and comprehensive understanding of the physician’s service quality. Therefore, as the volume of patient reviews increases, its weight in influencing patient decisions grows. Potential patients may be less reliant on CA signals, meaning the impact of CA signals on matched patient consultations decreases as volume increases.

High valence, on the other hand, signifies consistent positive patient experiences. It serves as an endorsement of a physician’s consistent track record in delivering quality care. The positive sentiments in the shared experiences can reassure patients about the quality of care they can expect, regardless of the physician’s professional credentials. Thus, when the average patient rating is more positive, potential patients may rely less on CA signals and more on the collective opinion of patients as a form of social proof to make informed decisions about seeking care from the physician.

Furthermore, the capacity state of physicians may play a significant role in the above compensatory effect between CA signals and volume/valence. In a highcapacity state, physicians have sufficient bandwidth to respond to increasing service demand, making the compensatory effects of volume and valence more salient. However, as they transition to a low-capacity state, their ability to cater to additional service demands diminishes. In such situations, while volume and valence might stimulate interest and demand, the actual conversion into matched patient consultations might be limited due to capacity constraints. Therefore, we predict the following:

Hypothesis 5a. The effect of CA signals on matched patient consultations are compensated for by volume, and this compensatory effect is more salient when a physician is in a high-capacity state.

Hypothesis 5b. The effect of CA signals on matched patient consultations are compensated for by valence, and this compensatory effect is more salient when a physician is in a high-capacity state.

## 4. Methodology

## 4.1. Research Site

We collected data from one of the largest OHCCs in China. Since 2006, this community has promoted its collaboration mostly with top-ranked hospitals and has stored and generated information for thousands of physicians from different regions across the nation. The OHCC allows licensed physicians to verify their identities, register in the community, and provide text-based consultations as a free service.<sup>3</sup> In addition to the consultation interactions between physicians and patients, the community is an open platform for patients to exchange information and share their experiences (Hao 2015, Hao et al. 2017).

Because of the large user base in terms of both physicians and patients, and the rich interactions among patients and between physicians and patients, this community<sup>4</sup> has served as a unique setting for scholars to understand the role of OHCCs in strengthening the physician-patient relationship and transforming health consultations (Guo et al. 2018, Zhang et al. 2019). We collected empirical materials from this community to test our hypotheses.

## 4.2. Research Design

We developed an HMM to characterize physicians dynamic capacity in the OHCC, as shown in Figure 2. The figure illustrates how physicians’ matched patient consultations depend on their capacity states and how they can switch between capacity states through interactions on the platform. Our HMM has three major elements:

1. We model physicians with different hidden capacity states, with 1 being the lowest and J the highest. At any time t, a physician is in only one state. The state captures the capacity a physician devotes to matched patient consultations.

Figure 2. Hidden Markov Model of Physicians’ Matched Patient Consultations  
![](/api/attachments/3PTB2BT4/fulltext/images/83fb2763be7607e819ac0293b87d29bc72c60ffff5bda2bec80d26606f626a49.jpg)

2. From time t � 1 to t, physicians can switch to any state with a certain probability, which is affected by the physicians’ interactions with the OHCC, such as their prior workload in the OHCC, tenure length, and symbolic incentives (e.g., virtual gifts) they receive from the platform.

3. Conditional on the capacity state at t, a physician may respond differently to patient requests. This statedependent response can be observed as the number of matched patient consultations at t.

Because the capacity constraints of physicians are inherently unobservable to the platform, we argue that the hidden and evolving states in the HMM are a good fit to capture the dynamics of physicians’ capacity. Our goal is to characterize the effects of owned and earned signals conditional on the capacity states. We provide additional details about the model development in Section 5.

## 4.3. Sampling

We used automated Java scripts to gather data by accessing and parsing Hyper Text Markup Language (HTML) and Extensible Markup Language (XML) code on each physician’s personal page in the OHCC. The data collection was conducted between April 2014 and October 2016. We sampled all of the cardiovascular medicine physicians in the OHCC who worked in tertiary A hospitals<sup>5</sup> and joined the OHCC during our observation window. Our sampling strategy of including physicians who joined the OHCC during our observation window allowed us to investigate how physicians build their online consultation services given their dynamic capacity states from the early stages of their engagement in the OHCC. Our focus on physicians at top-ranked hospitals mitigates the potential confounding effects of hospital quality and/or regulatory differences on matched patient consultations. Further, we focused on cardiovascular medicine physicians for two primary reasons. First, cardiovascular medicine is one of the most active specialties in OHCCs (Saner and van der Velde 2016, Turakhia et al. 2016). Second, prior research has demonstrated the effectiveness of online consultation for chronic diseases in general and cardiovascular conditions in particular (Artinian 2007, Merriel et al. 2014, Willis and Royne 2016, Chen et al. 2019). The main reason for this effec tiveness has been attributed to the standard procedures used in the diagnosis, treatment, and long-term management of chronic cardiovascular conditions. Accordingly, people often use OHCCs to obtain second opinions on diagnoses and treatment plans and engage in long-term care management of their chronic cardiovascular conditions.

Based on our research design, we collected the timeinvariant and time-variant data for the physicians as well as their patient satisfaction ratings. We excluded inactive physicians who had not received any patient satisfaction ratings, had not conducted any online health consultations in the OHCC, and/or had not logged into the OHCC during our observation window. We constructed a data set of 7,755 biweekly physician observations involving 526 cardiovascular medicine physicians spanning two years.

## 4.4. Measures

Table 2 provides details about the measures for our key constructs. Our dependent variable is matched patient consultations (PC ). We used the number of online consultations with patients<sup>6</sup> for physician i within time period t to capture the number of successful matches for physician i during t.

We categorized two sets of explanatory variables that affect physicians’ conditional consultations and statetransition probability. The first set (vector X, which we explain in Section 5.1) contains owned and earned signals that may influence potential patients’ selection decisions and the resulting matched patient consultations. First, we used the physician’s professional rank as a proxy for CA Signal<sub>it</sub>. A well-established tier system in China ranks physicians with the professional titles (from the lowest to the highest) resident physician, attending physician, associate chief physician, and chief physician. For reasons of simplicity, we coded chief physicians as 1 to indicate a high CA signal and physicians with other titles as 0 to indicate a low CA signal.<sup>7</sup>

Table 2. Measures of Key Constructs

<table><tr><td>Constructs</td><td>Measures</td></tr><tr><td>Dependent variable (Yit)</td><td></td></tr><tr><td>PCit</td><td>The number of online health consultations matched with patients for physician i in time period t.</td></tr><tr><td>Vector influencing the emission probability (Xit)</td><td></td></tr><tr><td>Owned signal: CA Signalit</td><td>Professional seniority disclosed by physician i at t (1 if professional title is chief physician, 0 if professional title is other ranks).</td></tr><tr><td>Earned signal: PB Signalit</td><td>The level of prosocial behaviors exhibited by physician i in the OHCC at time t. It is measured by as the cumulative prosocial behavior score for physician i at t. The prosocial behavior is provided by the OHCC and is calculated based on the number of articles posted by a physician, the frequency of the physician&#x27;s updates on their personal profile, and the frequency of the physician&#x27;s replies to the general Q&amp;A board.</td></tr><tr><td>Earned signal: Volumeit</td><td>The total number of patient satisfaction ratings for physician i at t.</td></tr><tr><td>Earned signal: Valenceit</td><td>The mean of patient satisfaction ratings based on a five-point scale for physician i at t.</td></tr><tr><td>Vector influencing the state-transition probability (Wit)</td><td></td></tr><tr><td>OHCC Tenureit-1</td><td>The number of days since physician i joined the OHCC at t - 1.</td></tr><tr><td>Prior Workloadit-1</td><td>The cumulative number of patient consultations by physician i at t - 1.</td></tr><tr><td>SymInctvit-1</td><td>The number of virtual gifts a physician i receives from patients during t - 1.</td></tr></table>

Note. $\mathrm { P C } _ { i t } ,$ matched patient consultations; CA Signal , competence-attribute signal; PB Signal , prosocial-behavior signal; Volume , volume of patient ratings; Valence , valence of patient ratings; SymInctv , symbolic incentives.

Second, we used a physician’s cumulative participation score at time t to capture PB Signal<sub>it</sub> as a physiciangenerated earned signal. Each physician’s participation score was provided by the investigated OHCC platform. The score was automatically calculated based on the extent to which physicians engaged in various activities in the OHCC to share their expertise and help patients. These behaviors included frequently responding to the general Q&A board (requests not directed to a specific physician), posting articles for patient education, and updating personal profiles in a timely manner. 8

Third, we focused on Volume and Valence as two earned signals aggregated from patients’ shared experiences in the OHCC. We followed the established method used by prior studies (e.g., Duan et al. 2008, Sun 2012, Babic ´ Rosario et al. 2016) to aggregate patient satisfaction ratings at the physician-time level. We created a proxy for Volume with the total number of patient satisfaction ratings for physician i at t. Finally, we captured $V a l e n c e _ { i t }$ as the mean of patient satisfaction ratings based on a five-point scale for physician i at t.

The second set (vector W, which we explain in Section 5.1) contains previous community interactions<sup>9</sup> that may influence physicians’ capacity and thus play a role in state transitions. First, as a physician engages with the OHCC over a longer time, they may have established a balance between the demand and their capacity, thus influencing the transition probability between high- and low-capacity states. Thus, we calculated the number of days since physician i joined the OHCC to capture OHCC Tenure<sub>it�1</sub>.

Second, prior workload influences the capacity state because a higher amount of prior work may indicate that a physician is more likely to be in a high-capacity state (Fradkin 2015, Horton 2019). We used a lagged measure of physicians’ cumulative number of patient consultations to capture their Prior Workload<sub>it�1</sub>.

Third, symbolic incentives likely play a role in capacity-state transition. Physicians may respond to symbolic incentives by allocating more time to online consultations. These incentives may shift a physician from a low-capacity state to a high-capacity state. In the investigated OHCC, there is no fee for the physicians voluntary services during our study period, but patients can show their appreciation for services with virtual gifts (which are transferred to different monetary rewards for physicians). Accordingly, we measured symbolic incentives as the number of virtual gifts that physician i receives from patients during t�1 (SymInctv<sub>it�1</sub>).

## 5. Model Development

In this section, we describe the details of our HMM, which captures the dynamic capacity states of physicians and their levels of matched patient consultations in the OHCC.

## 5.1. Modeling the Dynamics of Matched Patient Consultations

Our HMM characterizes the dynamics of a physician’s matched patient consultations as two stochastic processes: a process of observed consultations and an unobserved time-variant process of the physician’s capacity states. The hidden capacity state and observed consultations together form a hidden Markov chain (Rabiner 1989). $s _ { i t }$ denotes the state of physician i at time t. A physician can have J hidden capacity states: $s _ { i t } \in S = \{ \bar { 1 , 2 , \ldots , J } \}$ . Note that we allowed J to be arbitrary in our model and use selection criteria to decide J using our sample (details are provided in Section 5.5.2).

We modeled physician $i ^ { \prime } \dot { s }$ matched online patient consultations $Y _ { i t } ^ { * }$ at time t using the function $f ( X _ { i t } , \ W _ { i t } )$ as shown in Equation (1) below:

$$
Y _ {i t} ^ {*} = f (X _ {i t}, W _ {i t}).\tag{1}
$$

This function can change over time with $X _ { i t } ,$ , which is a vector of the physician’s signals, and $W _ { i t } ,$ , which captures the physician’s past interactions with the community. For tractability, we assumed that $f ( X _ { i t } , \ W _ { i t } )$ is linear in $X _ { i t }$ conditional on the capacity state $s _ { i t }$ and that $s _ { i t }$ is further determined by a latent transition propensity $L ( W _ { i t } )$ (details in Section 5.3). We then obtained the following:

$$
Y _ {i t} ^ {*} = X _ {i t} ^ {\prime} \beta_ {s _ {i t}} + \varepsilon_ {i t}, (\varepsilon_ {i t} | X _ {i t}, s _ {i t}) \sim N (0, \sigma^ {2}),\tag{2}
$$

where the error term $\varepsilon _ { i t }$ follows a normal distribution with a mean of zero and a variance of $\sigma ^ { 2 }$ conditional on the physician’s signals and capacity state. Essentially, in our model, physicians’ matched patient consultations could fluctuate because of their time-variant signals in the community and their capacity states.

Our goal is to estimate the coefficient vector $\beta _ { s _ { i t } } ,$ which captures the influence of the physician’s signals $X _ { i t }$ on the physician’s matched patient consultations $Y _ { i t } .$ . Note that vector $\beta _ { s _ { i t } }$ depends on physician i’s capacity state $s _ { i t } ,$ which is associated with physician i’s previous interactions with the community $W _ { i t }$ . We detail the capacity states and their transitions in our model below.

## 5.2. Physicians’ Capacity States in the HMM

The hidden state captures the dynamics of a physician’s capacity—that is, the amount of time and effort the physician can devote to online patient consultations. When a physician has higher capacity at time t (i.e., in a high-capacity state), the physician may be more willing to provide online patient consultations. Based on the capacity state, a physician responds differently to patient consultation requests resulting from signals (i.e., vector $X _ { i t } )$ . For example, a physician in a highcapacity state may be more likely to respond to new consultation requests. Note that this capacity state can be the result of a physician’s primary job in a hospital or their motivations to consult. Both are inherently unobservable to the platform. The HMM approach can properly capture this hidden dynamic process. The observed matched patient consultations could be regarded as a noisy manifestation of the hidden state process.

From time t � 1 to $t , \mathsf { a }$ physician may stay in one state or switch to another. In our HMM, the state process $\{ s _ { i t } \} _ { t \ge 0 }$ is characterized as a first-order Markov chain with state space $S = \{ 1 , 2 , \dots , J \}$ . Together with $Y _ { i t } ,$ , the observed consultations of physician i at time t, we modeled the vector-valued stochastic process $( Y _ { i t } , s _ { i t } )$ as a hidden Markov chain. According to the property of the HMM, the probability of transition from one period to the next can be factorized as follows:

$$
P (Y _ {i t}, s _ {i t} | Y _ {i, t - 1}, s _ {i, t - 1}) = P (Y _ {i t} | s _ {i t}) \cdot p (s _ {i, t - 1}, s _ {i t}),
$$

where $p ( s _ { i , t - 1 } , s _ { i t } )$ is the transition probability from state $s _ { i , t - 1 }$ to state $s _ { i t } ,$ , and $P ( Y _ { i t } | s _ { i t } )$ is the emission probability describing the state-dependent matched patient consultations. We elaborated these two probabilities in the next two subsections, respectively.

## 5.3. Transition Probability of Physicians Capacity States

A physician can switch among all the possible states in S. The transition matrix $P ( s _ { i , t - 1 } , s _ { i t } )$ below characterizes the probability of such transitions:

$$
P (s _ {i, t - 1}, s _ {i t}) = \left[ \begin{array}{c c c c} p (1, 1) & p (1, 2) & \ldots & p (1, J) \\ p (2, 1) & p (2, 2) & \ldots & p (2, J) \\ \vdots & \vdots & \ddots & \vdots \\ p (J, 1) & p (J, 2) & \ldots & p (J, J) \end{array} \right],
$$

where $p ( j , k )$ is the transition probability from state j to state $k ,$ and the probabilities in each row sum up to 1— that is, $\begin{array} { r } { \sum _ { k } p ( j , \hat { k } ) = 1 } \end{array}$ for all $j , k \in S$ . In our model, p(j, k) is influenced by a physician’s interactions with the community. For instance, if a physician receives more symbolic incentives from patient gifts, the physician may be more likely to spend time on online consultations and remain in a high-capacity state. Otherwise, the physician may switch to a low-capacity state.

We modeled the state-transition probability with a probit model (Wooldridge 2010). We assumed that the states are determined by a latent propensity of transition $L _ { i t } .$ :

$$
L _ {i t} = W _ {i t} ^ {\prime} \xi_ {s _ {i, t - 1}} + u _ {i t}, (u _ {i t} | W _ {i t}, s _ {i, t - 1}) \sim N (0, \sigma_ {u} ^ {2})\tag{3}
$$

such that $s _ { i t } = j { \mathrm { ~ i f ~ } } L _ { i t } \in [ \mu _ { i - 1 } , \ \mu _ { i } ) .$ , where $W _ { i t }$ is a vector of lagged variables related to the physician’s previous interactions with the community, $\xi _ { s _ { i , t - 1 } }$ is a vector of the corresponding coefficients, and $u _ { i t }$ is a normal error term from the probit model. In this model, the threshold vector $\{ \mu _ { i } \} , j = 1 , . . . , J ,$ is threshold values with $\mu _ { 0 }$ normalized to negative infinity, $\mu _ { 1 }$ to zero, and $\mu _ { J }$ to infinity. The remaining cutoff points are assumed to satisfy $\mu _ { 2 } \leq \cdots \leq \mu _ { J - 1 }$ so that the cumulative probabil ity is nondecreasing (Chib 2001). Note that $\xi _ { s _ { i , t - 1 } }$ is also state specific, capturing different effects of $\dot { W } _ { i t }$ under different states. Additionally, a physician’s capacity devoted to online patient consultations may be heavily influenced by their primary job in a hospital, which is inherently unobservable to the platform. We captured this using the error term $u _ { i t } .$ . Therefore, we refrained from extensively interpreting factors that may impact these transitions as the focus of this paper is the contingent impact of physicians’ signals in different capacity states.

With the probit assumption of Equation (3), the statetransition probability is obtained as follows:

$$
\begin{array}{r l} & p (j, k) = P (s _ {i t} = k | s _ {i, t - 1} = j, W _ {i t}) \\ & \quad = P (\mu_ {k - 1} \leq L _ {i t} <   \mu_ {k} | s _ {i, t - 1} = j, W _ {i t}) \\ & \quad = P (L _ {i t} <   \mu_ {k} | s _ {i, t - 1} = j, W _ {i t}) \\ & \quad \quad - P (L _ {i t} <   \mu_ {k - 1} | s _ {i, t - 1} = j, W _ {i t}), \\ & \quad = \Phi \bigg (\frac {\mu_ {k} - W _ {i t} ^ {\prime} \xi_ {j}}{\sigma_ {u}} \bigg) - \Phi \bigg (\frac {\mu_ {k - 1} - W _ {i t} ^ {\prime} \xi_ {j}}{\sigma_ {u}} \bigg), \end{array}\tag{5}
$$

where Φ is the standard normal distribution function. When physicians first join the community, we assumed that they have an initial probability $p _ { j }$ to be in capacity state j and that $\textstyle \sum _ { j = 1 } ^ { J } p _ { j } = { \dot { 1 } }$

## 5.4. Physicians’ State-Dependent Matched Patient Consultations

Given physicians’ capacity states described above, the emission probability $( Y _ { i t } | s _ { i t } )$ can be derived to describe the state-dependent matched patient consultations. Since the observed matched patient consultations are nonnegative, we adopted the standard Tobit model (Wooldridge 2010) following the Bayesian literature (Rossi and Allenby 2003):

$$
Y _ {i t} = \max (0, Y _ {i t} ^ {*}),
$$

where $Y _ { i t }$ stands for the observed consultations, and $Y _ { i t } ^ { * }$ was defined in Equation (1). Then, the state-dependent matched patient consultations follow the distribution below. The probability of having no patient consultations is

$$
P (Y _ {i t} = 0 | X _ {i t}, s _ {i t}) = P \left(Y _ {i t} ^ {*} \leq 0 | X _ {i t}, s _ {i t}\right) = 1 - \Phi \left(\frac {X _ {i t} ^ {\prime} \beta_ {s _ {i t}}}{\sigma}\right).
$$

For $Y _ { i t } > 0$ , the probability density function is

$$
f (Y _ {i t} | X _ {i t}, s _ {i t}) = \frac {1}{\sigma} \phi \left(\frac {Y _ {i t} - X _ {i t} ^ {\prime} \beta_ {s _ {i t}}}{\sigma}\right),
$$

where $\phi$ is the standard normal density function. With the transition probability and state-dependent matched patient consultations specified, we now proceed to estimation and identification.

## 5.5. Estimation and Identification

5.5.1. Estimation Procedure. Our goal is to estimate physicians’ state-dependent matched patient consultation parameters $\beta _ { s _ { i t } }$ in Equation (2) and the transition coefficients $\xi _ { s _ { i , t - 1 } }$ in Equation (3). Since $s _ { i t } \in S ,$ , we essentially estimated two parameter vectors: $\boldsymbol { \beta } = ( \beta _ { 1 } , \ldots , \beta _ { I } )$ and $\pmb { \xi } = ( \xi _ { 1 } , \dots , \ \hat { \xi _ { J } } )$ , where $\beta$ captures the effect of the physician’s signals on matched patient consultations, and $\xi$ captures the influence of community interactions on the physician’s state transition probability. To estimate these key parameters, we also estimated the standard deviations σ and $\sigma _ { u }$ as well as the state process $\tilde { S } = \{ s _ { i t } \} , \ t = 1 , \ . . . ,$ $T ; i = 1 , \ldots , N _ { t }$ . For ease of reference, we wrote the parameter space as $\theta = \{ \beta , \ \xi , \ \sigma , \ \sigma _ { u } \}$ and $\tilde { S }$ . Note that the error term $\sigma _ { u }$ in the propensity model, as shown in Equation $( 3 ) ,$ , is inherently unidentified. Therefore, we normalized it to 1 in our estimation.

We followed Chen et al. (2018) to estimate our HMM using a Bayesian procedure developed by Kim and Nelson (1999). The Bayesian estimation algorithm treats θ and $\tilde { S }$ as random variables with prior distributions. The algorithm then updates their joint distributions $\pi ( \theta , { \tilde { S } } | { \tilde { Y } } , X , W )$ using Gibbs sampling (Albert and Chib 1993). Estimations of HMMs may encounter the “label switching” problem (Jasra et al. 2005), which means our posterior distributions of $\theta$ and $\tilde { S }$ may be invariant if we switched the labels. Since the capacity states in our context have self-evident interpretation, we adopted a normalization requirement that the constant terms in $\beta _ { i } \in \beta$ are ordered. The constant term is denoted in $\mathbf { \dot { \boldsymbol { \beta } } } _ { j }$ as $c _ { x j }$ . We permutated $\beta$ according to $c _ { x j }$ such that $c _ { x 1 } \leq \dots \leq c _ { x J }$ in each draw of our Gibbs samplers. This requirement means that without any signals, a physician in a high-capacity state consults more on average than if they were in a low-capacity state. This technique helps identify the states in our model.

5.5.2. Model Selection. In our model specification, the number of capacity states for physicians was not defined a priori. Instead, it had to be determined with the data. To identify the number of states, we adopted several model-selection criteria from the literature. Our selection criteria included the log-likelihood, the com monly used Akaike information criterion (AIC) and Bayesian information criterion (BIC) (Singh et al. 2011, Yan and Tan 2014, Chen et al. 2018), and the Markov switching criterion (MSC), which is specially designed for Markov switching models (Netzer et al. 2008). Given a set of candidate models, the preferred model is the one with the minimum values of the selection criteria.

We estimated models with different capacity states, the results of which are reported in Table 3. Our benchmark is the one-state static model, which assumes that a physician stays in the same capacity state throughout the observation period.<sup>10</sup> As Table 3 shows, all selection criteria suggest that HMMs with more than one state are superior to the static model. In particular, the twostate HMM is the best-fitting model, outperforming the other models. Therefore, we report the estimation results of the two-state HMM hereafter.

Table 3. Selection of the Number of Capacity States for Physicians

<table><tr><td>Number of states</td><td>-2 * Log-likelihood</td><td>AIC</td><td>BIC</td><td>MSC</td><td>Number of variables</td></tr><tr><td>1</td><td>17,622.66</td><td>17,658.66</td><td>17,783.87</td><td>—</td><td>18</td></tr><tr><td>2</td><td>15,662.11</td><td>15,740.11</td><td>15,906.46</td><td>23,740.23</td><td>39</td></tr><tr><td>3</td><td>16,078.11</td><td>16,196.11</td><td>16,447.76</td><td>24,005.49</td><td>59</td></tr><tr><td>4</td><td>16,039.86</td><td>16,197.86</td><td>16,534.82</td><td>26,313.72</td><td>79</td></tr></table>

5.5.3. Instrumental Variables. Because both the earned signals and matched patient consultations (our dependent variable) could be correlated to physicians’ unobserved service quality, there is an endogeneity concern due to missing variables. To address the potential endogeneity concerns regarding physicians’ signals, we used instrumental variables (IVs) with a control function approach. We first regressed the potential endogenous signals on the IVs and then added the residual from the first-stage regressions to the second-stage estimation (HMM). This approach has been applied in IS and other areas such as operations management and marketing (Zhang et al. 2017, Jin et al. 2022). Note that because the HMM is nonlinear, a normal two-stage least squares estimator does not work (Guo and Smal 2016). Therefore, we adopted the control function approach.

As noted by Angrist and Pischke (2008), good instruments should satisfy the relevance and exclusion restriction conditions. In our context, an ideal IV is related to a physician’s owned and earned signals while being uncorrelated with the physician’s matched patient consultations through channels other than these signals (exclusion restriction). We proposed IVs using the average signals of obstetrician-gynecologists (OB/ GYNs) from the same hospital where doctor i is from: the matched patient consultations of OB/GYNs (PC\_O-$B _ { i t } )$ and the earned signals of OB/GYNs $( P B _ { - } O B _ { i t } ,$ Volume\_ $\_ O B _ { i t } ,$ and $V a l e n c e \_ O B _ { i t } )$ Because both the OB/GYNs and the focal physician in our sample are from the same hospital, their matched patient consultations and subsequent signals could be related due to common characteristics, such as reputation, practice patterns, or institutional signals like being affiliated with a renowned hospital. These common factors make the IVs relevant. This relevance condition is also tested and supported in the first-stage regression.<sup>11</sup> Meanwhile, the OB/GYNs’ matched patient consultations and signals are unlikely to affect the cardiovascular medicine physicians’ patient requests since these physi cians deal with patients with distinct health conditions. Due to the dissimilarities of their patients, OB/GYN consultations and signals are unlikely to affect cardiovascular matched patient consultations through channels other than the cardiologists’ signals. Therefore, matched patient consultations and signals from OB/GYNs are likely valid instruments that satisfy the exclusion restriction assumption.

## 6. Results

## 6.1. Descriptive Statistics

Table 4 reports the distribution of physicians along with the categorical variables in our sample and the physician population in the investigated OHCC. In general, our sample consists of more male physicians (78.33%) than female physicians (21.67%). Compared with the physician population in China (Gong and Huo 2016), our sample also skews toward senior physicians. Moreover, the distribution of our sample by gender and CA signal (i.e., based on professional title) is consistent with the distribution of the cardiovascular medicine physician population in the investigated OHCC.

Table 5 reports descriptive statistics and correlations among the constructs. We observed variations among the physicians in the variables. Although all the physicians’ matched patient consultations started at zero at the beginning of the observation window, their matched patient consultations ranged from 0 to 565 $( \mathrm { m e a n ~ } = \mathrm { ~ \bar { 8 } . 6 6 , ~ S D ~ = ~ 3 0 . 9 0 ) }$ within the observation window. Due to the positively skewed distributions, we applied natural log transformations to our variables (except for the CA signal dummy) prior to analysis.

Table 4. Distribution of the Sampled Physicians

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Categories</td><td colspan="2">Our sample</td><td rowspan="2">Cardiovascular medicine physician population in the investigated OHCC %</td></tr><tr><td>N</td><td>%</td></tr><tr><td rowspan="2">Gender $^{12}$ </td><td>Male</td><td>412</td><td>78.33%</td><td>78.67%</td></tr><tr><td>Female</td><td>114</td><td>21.67%</td><td>21.33%</td></tr><tr><td rowspan="4">CA Signal at  $t_0^{13}$ </td><td>Resident physician</td><td>63</td><td>11.98%</td><td>5.90%</td></tr><tr><td>Attending physician</td><td>129</td><td>24.52%</td><td>25.70%</td></tr><tr><td>Associate chief physician</td><td>220</td><td>41.83%</td><td>35.47%</td></tr><tr><td>Chief physician</td><td>114</td><td>21.67%</td><td>32.94%</td></tr></table>

Table 5. Descriptive Statistics of the Variables and Correlations Among the Variables

<table><tr><td>Variables</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td> $1.PC_{it+1}$ </td><td>8.66</td><td>30.90</td><td>0</td><td>565</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $CA\ Signal_{it}$ </td><td>0.27</td><td>0.45</td><td>0</td><td>1</td><td>-0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $PB\ Signal_{it}$ </td><td>1,308.88</td><td>3,643.70</td><td>0</td><td>37,030</td><td>0.48***</td><td>-0.03***</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td> $Volume_{it}$ </td><td>5.80</td><td>9.30</td><td>1</td><td>91</td><td>0.24***</td><td>0.25***</td><td>0.28***</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td> $Valence_{it}$ </td><td>4.92</td><td>0.25</td><td>2</td><td>5</td><td>0.03**</td><td>-0.07***</td><td>-0.03***</td><td>-0.07***</td><td>1.00</td><td></td><td></td></tr><tr><td> $Prior\ Workload_{it-1}$ </td><td>116.29</td><td>301.71</td><td>0</td><td>2,913</td><td>0.41***</td><td>-0.02**</td><td>0.67***</td><td>0.28***</td><td>-0.05***</td><td>1.00</td><td></td></tr><tr><td> $OHCC\ Tenure_{it-1}$ </td><td>263.07</td><td>201.58</td><td>1</td><td>896</td><td>-0.00</td><td>0.08***</td><td>0.13***</td><td>0.15***</td><td>-0.04***</td><td>0.17***</td><td>1.00</td></tr><tr><td> $SymInctv_{it-1}$ </td><td>0.56</td><td>2.58</td><td>0</td><td>55</td><td>0.61***</td><td>0.00</td><td>0.36***</td><td>0.35***</td><td>0.01</td><td>0.29***</td><td>0.03**</td></tr></table>

\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 6.2. Estimation Results

Table 6 reports the estimated parameters of the twostate HMM based on Bayesian estimation. The two states are referred to as low and high, denoted as State L and State H, respectively. The coefficients in vectors $\beta$ and ξ vary across the two states. We estimated two models of the HMM. In Model 1, only the main effects of the earned and owned signals are included. In Model 2, the interactions of earned signals and the owned signal (i.e., CA signal) are also included to examine the interaction effects. We found that the estimated coefficients are highly consistent across the two models. Therefore, in our discussion below, we focus on the richer specification of Model 2.

From Model 2 in Table 6, the initial probabilities of being in State L and State H are 0.575 and 0.425, respectively. Hence, a physician who is new to the OHCC is slightly more likely to be in State L than in State H. This result demonstrates the importance of understanding physicians’ capacity states and examining the signaling effects across the states in OHCCs.

6.2.1. Emission Probability ( ). We first discuss the estimations of the emission probability (top panel in Model 2 of Table 6). The estimates for the state-specific constant vector $c _ { x }$ are �1.126 (p < 0.01) and 1.388 (p < 0.01) for State L and State H, respectively. The relatively large distance between the states indicates that the states are well identified. The coefficients of the CA signal are 0.065 (p > 0.1) and 0.303 $( p < 0 . 0 1 )$ for State L and State H, respectively. Senior physicians may not conduct more matched patient consultations when they have limited capacity (i.e., in State L). As they move from State L to State H, senior physicians are more responsive to demand and can provide more matched patient consultations. A t-test of the posterior sample means shows that the coefficient of the CA signal in State H is statistically larger than the one in State L $( p <$ $0 . 0 1 ) ^ { 1 4 }$ , thus supporting Hypothesis 1.

Table 6. Results of the HMM Bayesian Estimation (n � 526, N � 7,755)

<table><tr><td>Variable names</td><td colspan="2">Model 1</td><td colspan="2">Model 2</td></tr><tr><td>Y</td><td>State L (low capacity)</td><td>State H (high capacity)</td><td>State L (low capacity)</td><td>State H (high capacity)</td></tr><tr><td> $X_{it}$ </td><td></td><td colspan="3"> $\beta$ —posterior mean (standard deviation)</td></tr><tr><td> $c_x$ </td><td>-1.133*** (0.061)</td><td>1.403*** (0.053)</td><td>-1.126*** (0.066)</td><td>1.388*** (0.062)</td></tr><tr><td>CA  $Signal_{it}$ </td><td>0.007 (0.083)</td><td>0.176*** (0.050)</td><td>0.065 (0.111)</td><td>0.303*** (0.072)</td></tr><tr><td>PB  $Signal_{it}$ </td><td>0.459*** (0.049)</td><td>1.140*** (0.040)</td><td>0.405*** (0.086)</td><td>1.131*** (0.066)</td></tr><tr><td> $Volume_{it}$ </td><td>0.268*** (0.042)</td><td>0.149*** (0.034)</td><td>0.283*** (0.064)</td><td>0.199*** (0.058)</td></tr><tr><td> $Valence_{it}$ </td><td>0.001 (0.063)</td><td>0.051 (0.034)</td><td>0.108 (0.118)</td><td>0.180*** (0.051)</td></tr><tr><td>CA  $Signal_{it}$ * PB  $Signal_{it}$ </td><td></td><td></td><td>0.208** (0.081)</td><td>-0.032 (0.074)</td></tr><tr><td>CA  $Signal_{it}$ *  $Volume_{it}$ </td><td></td><td></td><td>-0.018 (0.076)</td><td>-0.143** (0.057)</td></tr><tr><td>CA  $Signal_{it}$ *  $Valence_{it}$ </td><td></td><td></td><td>-0.161* (0.089)</td><td>-0.262*** (0.071)</td></tr><tr><td>First-Stage Residuals</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>CA Signal * First-Stage Residuals</td><td></td><td></td><td>Yes</td><td>Yes</td></tr><tr><td>Sigma2</td><td colspan="2">1.064*** (0.023)</td><td colspan="2">1.069*** (0.023)</td></tr><tr><td> $W_{it}$ </td><td></td><td colspan="3"> $\xi$ —posterior mean (standard deviation)</td></tr><tr><td> $c_w$ </td><td>-0.909*** (0.098)</td><td>0.423*** (0.053)</td><td>-0.919*** (0.094)</td><td>0.407*** (0.056)</td></tr><tr><td>Prior  $Workload_{it-1}$ </td><td>0.401*** (0.052)</td><td>0.365*** (0.045)</td><td>0.414*** (0.049)</td><td>0.368*** (0.047)</td></tr><tr><td> $OHCC Tenure_{it-1}$ </td><td>-0.364*** (0.038)</td><td>-0.301*** (0.047)</td><td>-0.375*** (0.039)</td><td>-0.304*** (0.044)</td></tr><tr><td> $SymInctv_{it-1}$ </td><td>0.172* (0.104)</td><td>0.047* (0.028)</td><td>0.176* (0.095)</td><td>0.047 (0.029)</td></tr><tr><td>Sigma2u</td><td colspan="2">1(0)</td><td colspan="2">1(0)</td></tr><tr><td>Initial probability</td><td>0.565*** (0.029)</td><td>0.435*** (0.029)</td><td>0.575*** (0.030)</td><td>0.425*** (0.030)</td></tr></table>

Notes. The model estimation also includes the residuals from our first-stage regressions using the instrumental variables from OB/GYN physicians, Residual\_PB, Residual\_Vol, and Residual\_Val. We report the first-stage results and coefficients of these residuals in Section A of the online appendix. Standard deviations for the posterior coefficients are shown in parentheses. State L, low-capacity state; State H, high-capacity state.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Figure 3. Interaction Effect of the CA Signal and the PB Signal on Matched Patient Consultations  
![](/api/attachments/3PTB2BT4/fulltext/images/a64360858c77cb659908205bcf7104722986d624432449e645e52199a08d93a8.jpg)

(b) High-Capacity State  
![](/api/attachments/3PTB2BT4/fulltext/images/e73d611725259b5f56b86a1d9ad8e2391a5c6fc7791ea3a0514f8c1184de597f.jpg)

The coefficients of the PB signal are 0.405 $( p < 0 . 0 1 )$ and 1.131 $( p < 0 . 0 1 )$ for State L and State H, respectively. The positive coefficients suggest that physicians who actively engage in OHCC activities tend to conduct more matched patient consultations. A t-test of the posterior sample means shows that the coefficient of the PB signal in State H is statistically larger than the one in State L $( p < 0 . 0 1 )$ . The increasing magnitude of the coefficients shows that the effect of the PB signal is stronger as physicians move from State L to State H, thus supporting Hypothesis 2.

In terms of Hypothesis 3, valence has a significant positive impact on matched patient consultations in State H but not in State L $( \beta _ { L } = \stackrel { \cdot } { 0 . 1 0 8 } , p > 0 . 1 ; \beta _ { H } = 0 . 1 8 0 ,$ $p < 0 . 0 1 )$ and that the difference is statistically significant according to a t-test of their posterior sample means $( p < 0 . 0 1 )$ , thus supporting Hypothesis 3b. In addition, we found a positive relationship between volume and matched patient consultations in State L and State H. Contrary to our expectation in Hypothesis 3a, the positive coefficient turns out to be stronger in State L $( \bar { \beta _ { L } } = 0 . 2 8 3 , p < 0 . 0 1 )$ ) than in State H $( \beta _ { H } = 0 . 1 9 9 , p <$ 0.01), with the difference being statistically significant $( p < 0 . 0 1 )$ . This unexpected result reveals the elasticity of physicians’ capacity. A large volume of experiences shared by patients may play a stronger role in suggesting the capacity of physicians and motivating them to accept patient consultations even when they are in a low-capacity state.

Figure 4. Interaction Effect of the CA Signal and Volume on Matched Patient Consultations  
(a) Low-Capacity State  
![](/api/attachments/3PTB2BT4/fulltext/images/44f1ad80b00b4b734525da7a005d1a7d45babc3428b78035f076488b139604fa.jpg)

(b) High-Capacity State  
![](/api/attachments/3PTB2BT4/fulltext/images/ae329c2a4fbae970a609d4607a78f360176c5707db6aa3204d10d2f2870e1a0f.jpg)

Figure 5. Interaction Effect of the CA Signal and Valence on Matched Patient Consultations  
![](/api/attachments/3PTB2BT4/fulltext/images/382c5cc035bc1ea19daac67c7b507b6fbf899ebdc5721d908e9be5cfd1b64841.jpg)

We also found three interesting interaction effects between the owned and earned signals. The PB signal positively moderates the impact of the CA signal on matched patient consultations when physicians are in State L $( \bar { \beta _ { L } } = 0 . 2 0 8 ^ { * * } , p < 0 . 0 5 )$ . However, the moderation effect is not significant in State H $( \beta _ { H } = - 0 . 0 3 2 , p >$ 0.1). The coefficients of the interaction terms between State L and State H are significantly different $( p < 0 . 0 1 )$ We plotted the interactions to facilitate the interpretation of the interaction effects (Figure 3). Consistent with our expectation, the amplification effect between the CA signal and the PB signal on matched patient consultations is salient in State L. When physicians have limited capacity, their active engagement in the OHCC indicates a credible commitment that can amplify the effect of the CA signal to reduce potential patients’ uncertainty about physicians’ service quality or capacity.

By contrast, volume negatively moderates the impact of the CA signal on matched patient consultations when physicians are in State H $( \beta _ { H } = - 0 . 1 4 3 , p < 0 . 0 5 )$ This moderation effect is not significant in State L $( \beta _ { L } =$ $- 0 . 0 1 8 , p > 0 . 1 )$ . The coefficients of the interaction terms between State L and State H are significantly different $( p < 0 . 0 1 )$ (Figure 4). As expected, the compensatory effect of volume and the CA signal on matched patient consultations is salient in State H. We observed that in State H, matched patient consultations are less sensitive to the CA signal when volume is high. In other words, when physicians have more capacity, a large volume of shared patient experiences can compensate for the disadvantages of junior physicians’ CA signal to a greater extent.

![](/api/attachments/3PTB2BT4/fulltext/images/110faed3c09c5fef1421ce0169ac7efbfe7204295b2e3a4aba822995a435983a.jpg)

Finally, valence similarly displays a negative moderating effect on the relationship between the CA signal and matched patient consultations (Figure 5). This moderating effect is stronger when physicians are in State H $( \beta _ { H } = - 0 . 2 6 2 , p < 0 . 0 1 )$ than in State L $( \beta _ { L } =$ $- 0 . 1 6 1 , p < 0 . 1 )$ , with the difference being statistically significant $( p \ < \ 0 . 0 1 )$ ). These results again indicate a compensatory effect between valence and the CA signal on matched patient consultations—that is, more positive shared patient experiences can compensate for the disadvantages of junior physicians’ CA signal to a greater extent.

6.2.2. State-Transition Probability ( ). We now turn to factors that may influence the state-transition probability (bottom panel of Model 2 in Table 6). The constant term $c _ { w } \mathrm { i s } - 0 . 9 1 9 ( p < 0 . 0 1 )$ and 0.407 $( p < 0 . 0 1 )$ for State L and State H, respectively. This result indicates that with other factors remaining constant, physicians are likely to stay in their corresponding states.

Physicians’ tenure with the OHCC drives them to stay in $( \xi = - 0 . 3 7 5 , p < 0 . 0 1 )$ or transfer to $( \xi = - 0 . 3 0 4 ,$ $p < 0 . 0 1 )$ ) a low-capacity state. Symbolic incentives are beneficial in motivating physicians in a low-capacity state and are likely to transfer them from State L to State H $( \xi = 0 . 1 7 6 , p < \mathrm { \dot { 0 } } . 1 )$ . However, the motivational effect of symbolic incentives is not significant when physicians are in a high-capacity state $( \xi = 0 . 0 4 7 , p \stackrel { \cdot } { > } 0 . 1 )$ Contrary to our expectation, prior workload positively affects the state-transition probability. A higher workload in the past does not decrease a physician’s remaining capacity. Instead, it stimulates physicians motivation to stay in $( \xi = 0 . 3 6 8 , p < 0 . 0 1 )$ ) or transfer to $( \xi = 0 . 4 1 4 , p < 0 . 0 \dot { 1 } )$ ) a high-capacity state.

## 6.3. Robustness Checks

We conducted several post hoc analyses to test the robustness of our findings. First, we segmented the CA signal into two groups in the main analysis to ease our interpretation of the results. To show the impact of the CA signal comprehensively, we constructed the CA signal as a set of dummy variables and found the results are largely consistent with those from the main effect analysis (see Table B1 in Section B of the online appendix).

Second, we controlled the effect of other information displayed on physicians’ profile pages. Such information includes the cumulative number of thank-you letters a physician received from patients (i.e., Thanks<sub>it</sub>) and the number of patient votes recommending a physician (i.e., Votes<sub>it</sub>). Table B2 in Section B of the online appendix demonstrates the robustness of our results after the additional factors are controlled for.

Lastly, some may wonder whether the HMM model accurately captures the hidden states. Because the states from the real data are inherently unobservable, simulated data are often utilized to evaluate the accuracy of the HMM. We generate synthetic data with known underlying states and then compare the results obtained from the HMMs with the ground truth (the parameters that generated the data). This approach provides a quantitative assessment of how well the HMMs capture the states and the emission probabilities. By comparing the model’s outputs with the known states, we can gain insights into its accuracy and validate its performance. We reported the estimation on simulated data in Section C of the online appendix, which shows that our estimation can accurately recover the hidden states and model parameters.

## 7. Discussion

We studied signaling effects on matching outcomes when suppliers transition between different capacity states over time in online matching platforms. In the context of OHCCs, we used an HMM to examine the time-variant nature of physicians’ capacity to volitionally supply online health consultation services. Physicians can implicitly switch between high-capacity and low-capacity states in OHCC platforms. In addition, we differentiated between owned and earned signals and delineated how these two types of signals interactively influence matching outcomes given suppliers’ dynamic capacity.

## 7.1. Theoretical Contributions

We adopted a novel lens to theorize signals and signaling effects in an online matching environment where suppliers’ capacity is time variant, unobservable, and uncertain. We contextualized the concepts of owned and earned signals in relation to OHCC platforms and examined how they function differently and interactively under physician’s different dynamic capacity states. Our findings contribute to multiple streams of literature, including online matching platforms and signaling theory (see Table 7).

To begin, our work uncovers the time-variant nature of supply-side capacity in online matching platforms. The dynamic approach is a unique feature of this work as the existing literature has mostly assumed that suppliers’ capacity is static. We challenge this assumption in the context of OHCCs, where physicians’ capacity devoted to volitional online consultations can change over time. Accordingly, we used an HMM to capture physicians’ time-variant capacity and allow physicians to transition between high-capacity and low-capacity states over time. Our findings extend understanding of how signaling effects on matching outcomes can depend on suppliers’ time-variant capacity states. As such, we advance the literature by introducing a novel approach to explicitly model providers’ hidden capacity in the matching process.

The matching market literature has explored several mechanisms to facilitate matching on online platforms. Such mechanisms include reputation systems (Benson et al. 2020), recommendation systems (Ashlagi et al. 2020), and pricing mechanisms (Arnosti et al. 2021). Recent research has recognized that these mechanisms may not always work, especially when the matching formation is based on preference and assignment (Heyman and Ariely 2004, Huang et al. 2022a). Our study contributes to the emerging discussion on informative signals as matching mechanisms and elaborates the respective and interactive roles of signals in achieving a balance between supply and demand and facilitating matching for consultations.

Our work also contributes to signaling theory in several important ways. First, management scholars have pointed out the need to develop a typology that sorts signals into theoretically justifiable and managerially meaningful categories in organizational contexts. In response to this discussion (e.g., Basuroy et al. 2006), our study provides a fresh viewpoint to conceptualize two types of signals for matching platforms: owned and earned signals. In the context of OHCCs, we delineate that potential patients may infer these signals as service-quality and capacity indicators. To the best of our knowledge, this study is among the first to explicitly differentiate the features of signals and theorize the dual interpretations of suppliers’ signals.

Second, this study enriches our understanding of how signals function collectively for match formation in OHCCs. Previous work has shown how external referents, such as other receivers, can change how receivers process a signal (Cheung et al. 2014, Chen et al. 2020a). For example, rankings signal the educational quality of universities, but prospective students calibrate rankings based on the opinions of their peers and adjust their evaluations accordingly to make their selection decisions (Branzei et al. 2004, Connelly et al. 2011). While owned signals are possessed by signalers and usually reflect rigorous professional validation of credentials, earned signals are subject to signalers efforts to generate observable information (e.g., revealed preferences to contribute to the welfare of the focal community) that will lead others to infer the desired service characteristics. Specifically, earned signals can manifest through direct behavioral efforts revealing suppliers’ commitment or through collective experiences based on the opinions of people who have consumed a provider’s services and shared their thoughts with others. Our study extends this line of discussion and uncovers the differential power of earned signals in affecting matching outcomes. This extension also provides insights into the multifaceted functions of online matching platforms. These platforms serve a crucial role not only in conveying signals already owned by suppliers prior to onboarding but also in providing a channel for suppliers to acquire earned signals through persistent prosocial commitment or through accumulating collective feedback from the platforms’ user bases.

Table 7. Summary of Findings and Contributions

<table><tr><td>Objectives</td><td>Findings</td><td>Theoretical Implications</td><td>Practical Implications</td></tr><tr><td>Dynamic capacity states</td><td>Identified two latent capacity states (low and high) for suppliers and discovered how the signaling effects work differently across dynamic capacity states.</td><td>Uncovered the time-variant nature of suppliers&#x27; capacity on online matching platforms.Theorized how signals function differently given the dynamic capacity of physicians in OHCCs.Explicitly modeled physicians&#x27; hidden dynamic capacity states in the context of voluntary consultation services in OHCCs.</td><td>Practitioners should...Incorporate suppliers&#x27; dynamic capacity information into the design of online matching platforms.Prioritize the presentation of signals given predicted supply-side capacity.Differentiate interpretations of a signal and determine the optimal level of granularity to present the signal.Explore the customized and transparent design of informative signals in online matching platforms.</td></tr><tr><td>Types of signals</td><td>Owned signal: CA.Earned signals: PB, volume and valence of patient reviews.</td><td>Contextualized owned and earned signals in relation to OHCC platforms.Differentiated between PB signals and shared experiences (volume and valence) as two types of earned signals.Identified prosocial behaviors as earned signals based on physicians&#x27; revealed preferences (by virtue of their behaviors) to contribute to the welfare of the OHCC.</td><td>Online matching platforms can serve a role in authenticating and presenting different types of signals.Service providers may deliberately choose what signals to display and how to display them to effectively communicate their service quality.</td></tr><tr><td>Interaction between signals and capacity states</td><td>CA signals and valence increase matched patient consultations when physicians are in a high-capacity state.PB signals and volume increase matched patient consultations regardless of physicians&#x27; capacity state.The effect of PB signals is stronger when physicians are in a high-capacity state, whereas the effect of volume is stronger when physicians are in a low-capacity.</td><td>Modeled the data generating the process using an HMM.Revealed that physicians&#x27; acceptance of patient consultation requests is determined by their capacity states, while signals influence patients&#x27; choice of physicians.Uncovered that interactions between signals and physicians&#x27; capacity states contribute to matched patient consultations in OHCCs.</td><td>When and how to deliver CA signals to update PB signals.Senior physicians benefit from their high CA signals in match formation for consultations without undue concern for their earned signals.</td></tr><tr><td>Interaction between owned signals and earned signals</td><td>The impact of CA signals on matched patient consultations is (1) amplified by PB signals when physicians are in a low-capacity state and (2) compensated for by volume and valence when physicians are in a high-capacity state.</td><td>Revealed the differential power of earned signals in moderating the impact of owned signals on matching for consultations.Found that the complementary and substitute relationship between owned signals and earned signals changes when physicians are in different capacity states.</td><td>Physicians&#x27; ongoing engagement in OHCCs creates valuable PB signals, which reinforce the value of owned signals in matching for consultations.OHCCs are valuable platforms that provide opportunities for junior physicians to accumulate online patients. Junior physicians need to put forth effort to generate positive assessments from patients.</td></tr></table>

Third, suppliers’ prosocial commitment and customers’ shared experiences on these platforms are both valuable earned signals and may interact with owned signal to reduce uncertainty regarding service quality and capacity. These findings contribute to signaling theory and provide evidence that receivers may process earned signals differently. Previous studies have demonstrated a bandwagon effect whereby receivers imitate others’ decisions as an approach to coping with uncertainty in decision-making (Sliwka 2007, McNamara et al. 2008). Our study extends this line of work by revealing that behavioral efforts reflecting commitment may complement and reinforce the attractiveness of senior physicians, especially when these physicians have low bandwidth. In contrast, a large volume of experiences or more positive experiences shared by patients may compensate for low CA signals for junior physicians. This compensatory effect is more salient when physicians are in a high-capacity state. In sum, multisource signals combine to help reduce uncertainty and facilitate desirable matching outcomes contingent upon physicians’ capacity states in online environments.

Finally, our work contributes to understanding how motivations, opportunities, and ability of suppliers affect choices in the online matching context. Past work has demonstrated the utility of the motivation, opportunity, and ability (MOA) framework to explain a wide range of behaviors such as consumer choice, social capital activation, and knowledge sharing by employees (Boudreau et al. 2003). This stream of work has been elaborated to surface whether motivation, opportunity or ability is the constraining factor in affecting behaviors (Siemsen et al. 2008). Our work adds to this discourse in important ways. We show the plurality of how motivation and ability of suppliers can be signaled by different stakeholders in an online matching context, arising from advances in how information is generated and presented on matching platforms. While ability can be signaled based on professional credentials which are owned by a supplier, both ability and motivation can be signaled based on the supplier’s revealed behaviors and the cumulative experiences of consumers with the supplier. Furthermore, aligned with the constraining factor model, our work reveals the crucial role of suppliers’ dynamic capacity states in affecting how the signals, individually and interactively, affect realization of opportunities by matching suppliers with customers.

## 7.2. Practical Implications

Besides the above theoretical contributions, this study provides practical guidelines for platform designers and service providers to deal with the coexistence of owned signals and earned signals alongside the dynamic constraint of supply-side capacity to facilitate matching outcomes in online communities.

First, our findings shed light on the design of online matching platforms. Platform designers could apply our HMM approach to capture physicians’ dynamic capacity information and incorporate such information into the design of OHCCs for remote health consultations. It is crucial to recognize the increasing importance of OHCC in shaping the generation and delivery of signals. This influence is exerted through algorithms that process interaction and experiential data, as well as through well-designed user interfaces that encourage customer feedback. Moreover, OHCCs are instrumen tal in optimally presenting these signals to enhance matching outcomes. Based on the predicted capacity of a physician, OHCCs can decide when and how to showcase different signals. For example, a platform could prioritize showcasing physicians’ PB signals when they are predicted to be in a low-capacity state. This customized signaling strategy might serve as a complementary mechanism to Horton’s (2019) suggestion for service providers to disclose their capacity status. Such an integration could potentially enhance matching success on online matching platforms.

Second, platform designers need to be cautious about presenting different types of signals based on their interpretations in specific contexts. OHCCs are expand ing functions to provide more opportunities for physicians to display their professional credentials and demonstrate ongoing prosocial behaviors in a community. Following this trend, deciding how to differentiate various types of signals, including their optimal level of granularity, is a critical decision for OHCC platforms.

Our work opens a new avenue in this direction and encourages future research to explore the customized and transparent design of informative signals in online matching platforms.

Third, this study has important implications regarding how physicians can manage their signaling strategies in OHCCs, considering the various impacts of distinct signals. A low level of owned signals pertaining to competence, such as junior status, are not necessarily detrimental and can be compensated for by earned signals if managed well. Specifically, we suggest that physicians employ different signaling strategies depending on their CA signals. Senior physicians can benefit from their high CA signals, and such benefits are amplified by their behavioral commitment to the welfare of the focal OHCC. Our results generally suggest that physicians should frequently participate in OHCC activities to continuously update their PB signals and communicate their ongoing willingness and commitment to contribute to the community. Potential patients appreciate PB signals, and these signals can even amplify the benefits of owned signals, especially when physicians have limited bandwidth. By contrast, junior physicians need to pay attention to the patient experiences shared on OHCC platforms. In traditional health consultations, junior physicians are often at a disadvantage in obtaining new patients. However, health consultations on online platforms may change this situation. Our findings indicate that OHCCs offer valuable opportunities that may benefit junior physicians. Physicians with junior credentials may achieve more matched patient consultations, especially when patients share abundant or favorable experiences. In other words, junior physicians’ disadvantage stemming from their professional credentials may be compensated for by their earned signals, particularly by reviews by patients based on their experiences, and such compensatory benefits are more salient when physicians have higher capacity.

## 7.3. Limitations and Future Research Directions

The insights and limitations of this study can serve as avenues for future research. First, OHCCs are rapidly evolving because of technological developments in social networking, and new features on online matching platforms may present different formats for signaling information. Future work could leverage the developments of online matching platforms and design field experiments to investigate how new technological features in OHCCs change how information is presented and processed to differentiate suppliers. It would also be promising for future research to explore the generalizability of our findings in other contexts, such as physicians in different specialty areas, with different demographic characteristics (e.g., age, job tenure, and residence location), or in lower-level hospitals or using OHCCs with different technological features.

Second, we conceptualized physicians’ signals as their disclosed information, recorded activities, and earned collective experiences in OHCCs. While we focused on how earned signals interact with owned sig nals to facilitate match formation in this study, future research might explore the interactive effects between owned signals or between earned signals. In addition, signals can be conveyed by different service stakeholders, such as the departments or hospitals with which physicians are affiliated. It would be interesting to investigate the effectiveness of multiple signals of stakeholders at different levels on online matching platforms.

Finally, the interdependency between hospital doctor visits and OHCCs (Huang et al. 2021, Fan et al. 2022, Hwang et al. 2022) deserves further investigation in future research. In our study, the OHCC is not an online channel of a hospital (e.g., a virtual channel of a hospital, such as for telemedicine) for physicians to consult with their offline patients; rather, it is a community platform for physicians to provide voluntary consultations to patients. While patients can communicate with the physicians in the OHCC, this is not the same as consulting with the same physician in an online channel of a hospital. It would be interesting to extend this line of discussion to uncover how to better coordinate the delivery of care between OHCCs and hospitals. On one hand, physicians’ signaling efforts in OHCCs may influence their service demand in hospitals. On the other hand, the service demand in hospitals may, in turn, affect physicians’ signaling efforts and capacity states in OHCCs. The practical constraints associated with access to matched data on doctor visits in hospitals precluded us from pursuing this line of inquiry. Instead, we applied the HMM method, which allowed us to specify error terms and hidden states to capture the unobserved capacity fluctuations arising from physicians’ primary jobs in hospitals. Future work might use alternative methods to focus on the reciprocal impacts of signaling in OHCCs on health consultation success in both hospitals and OHCCs.

## 8. Conclusion

This study extends signaling theory in online matching platforms where suppliers’ capacity changes over time. We provide a theoretical foundation for understanding how suppliers’ dynamic capacity serves as a contingency that affects the triangulation of multisource signals for consumers to infer providers’ service quality and capacity and achieve desirable matching outcomes. Our findings reveal that online matching platforms facilitate the engagement of service professionals through signaling and assist in spreading crowd wisdom regarding service experiences. Interestingly, service professionals’ owned and earned signals are not an either-or choice but rather work together interactively to balance supply and demand and facilitate matchmaking. In the context of OHCCs, where physicians provide voluntary services above and beyond their primary jobs, we show that owned and earned signals increase matched patient consultations in different patterns contingent upon physicians’ capacity states. In addition, PB signals amplify the effectiveness of CA signals when physicians are in a low-capacity state, whereas shared experiences, as signaled by volume and valence, can compensate for the effects of CA signals in the matching process when physicians are in a high-capacity state. Overall, this study offers a novel understanding of the role of signaling in online matching platforms, highlighting their time-variant and uncertain nature. These findings have important implications for practitioners and policymakers looking to improve the effectiveness of online matching platforms, particularly in the healthcare sector, where OHCCs represent critical platforms for voluntary service provision and community engagement.

## Acknowledgments

The authors express their sincere gratitude to the senior editor, the associate editor, and the reviewers for their constructive feedback. Additionally, the authors thank the participants at the ICIS (2015) and INFORMS (2016) conferences, and the research seminar at the University of Cincinnati, where this work was presented and benefited from their feedback. Xitong Guo acknowledges the support from the National Natural Science of China grants [72125001, 72071054, 72293584].

## Endnotes

<sup>1</sup> Peer patients are those with the same health condition who have consulted with the same physician in the OHCC.

<sup>2</sup> We recognize there are various consultation modalities (e.g., audio-based and video-based consultations) in OHCCs. We focus on the commonalities across these modalities regarding how signals can be used to differentiate physicians.

<sup>3</sup> Text-based consultations were all free services in the investigated OHCC during our study period.

The investigated community platform has a fact-checking mechanism to validate physicians and patients and the truthfulness of the information provided before it becomes publicly available. For example, the community platform requests that physicians upload proof of their identities and credentials. In addition, when posting a review, patients must provide a contact phone number, which is available only to the webmaster, who performs random callbacks to verify the truthfulness of consultation experiences (Hao 2015).

According to the hospital classification system of the Ministry of Health of the People’s Republic of China, hospitals in China are classified into primary, secondary, and tertiary hospitals based on whether they provide medical care, provide medical education, and/or conduct medical research (Guo 1990). A tertiary hospital refers to a cross-regional hospital that conducts research and provides comprehensive and specialized medical care and whose physicians have a high level of medical education. Tertiary hospitals are further classified into three subgroups—A, B, and C—according to their service level, size, medical technology, medical equipment, and management and medical quality (Li et al. 2008). In general, tertiary A hospitals are all subject to the same industry regulations and are considered to provide the highest-quality services with physicians who have the highest levels of education and conduct research.

<sup>6</sup> Return patients are not repeatedly counted in the number of consultations. The investigated OHCC consolidates return patients consultations under one single conversation track with timestamps. Thus, the number of consultations does not increase when physicians provide consultations for return patients.

<sup>7</sup> We also report the results using four levels of professional titles in a robustness check in Section 6.3. The results remain qualitatively consistent.

<sup>8</sup> While the factors used by the algorithm to compute physicians’ contribution scores are made public, the OHCC does not reveal how the factors are weighted.

<sup>9</sup> We assume the physicians’ interactions with the OHCC community influence their time-variant capacity in the short run. In the long run, they could be promoted in their primary jobs in hospitals. Longer-term changes in workload in a physician’s primary job could lead to a significant change in their capacity over time. However, this type of demand shift arising from a change in a physician’s primary job is likely to take years, which is beyond the theorization and observation of our study.

<sup>10</sup> The static model follows the Heckman two-step estimation with a participation equation and a contribution equation. We then estimated the model with maximum likelihood estimation. The results are available upon request.

<sup>11</sup> We provide the first-stage results in Section A of the online appendix.

<sup>12</sup> We noticed that our sample is skewed toward male physicians (78.33% male and 21.67% female). This distribution is consistent with the distribution of the cardiovascular medicine physician population in the investigated OHCC, indicating that there are generally more male physicians in cardiovascular medicine.

<sup>13</sup> We noticed that only a few physicians updated their CA signal during our observation window. Among the 526 physicians, 24 were promoted and changed their professional titles to a higher level. We tested our model by excluding these 24 physicians and found the results were consistent, showing the robustness of our findings.

<sup>14</sup> Because we estimated the HMM with a Bayesian approach, we also calculated the difference in the posterior distributions of the two coefficients and calculated the probability that the difference is greater than zero (Kruschke 2014). For the CA signal, the probability that the coefficient in State H is greater than the one in State L, $P ( \beta _ { 1 H } > \beta _ { 1 L } ) ,$ , is 0.97, consistent with our t-test results. We omitted similar discussions for the rest of the hypotheses. The results are available upon request.

## References

Albert JH, Chib S (1993) Bayesian analysis of binary and polychotomous response data. J. Amer. Statist. Assoc. 88(422):669–679

Allon G, Bassamboo A, Cil EB (2012) Large-scale service marketplaces: The role of the moderating firm. Management Sci. 58(10): 1854–1872.

Angrist JD, Pischke JS (2008) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University, Princeton, NJ).

Arnosti N, Johari R, Kanoria Y (2021) Managing congestion in matching markets. Manufacturing Service Oper. Management 23(3):620–636

Artinian NT (2007) Telehealth as a tool for enhancing care for patient with cardiovascular disease. J. Cardiovasc. Nurs. 22(1):25–31.

Ashlagi I, Braverman M, Kanoria Y, Shi P (2020) Clearing matching markets efficiently: Informative signals and match recommen dations. Management Sci. 66(5):2163–2193.

Babic ´ Rosario A, Sotgiu F, De Valck K, Bijmolt TH (2016) The effect of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric factors. J. Marketing Res. 53(3):297–318.

Basuroy S, Desai KK, Talukdar D (2006) An empirical investigation of sig naling in the motion picture industry. J. Marketing Res. 43(2):287–295.

Benson A, Sojourner A, Umyarov A (2020) Can reputation discipline the gig economy? Experimental evidence from an online labor market. Management Sci. 66(5):1802–1825.

Bojd B, Yoganarasimhan H (2022) Star-cursed lovers: Role of popularity information in online dating. Marketing Sci. 41(1):73–92.

Boudreau J, Hopp W, McClain JO, Thomas LJ (2003) On the interface between operations and human resources management. Manuf. Serv. Oper. Manag. 5(3):179–202.

Branzei O, Ursacki-Bryant TJ, Vertinsky I, Zhang W (2004) The for mation of green strategies in Chinese firms: Matching corporate environmental responses and individual principles. Strategic Management J. 25(11):1075–1095.

Burdett K, Shi S, Wright R (2001) Pricing and matching with fric tions. J. Political Econom. 109(5):1060–1085.

Cameron RA, Mazer BL, DeLuca JM, Mohile SG, Epstein RM (2015) In search of compassion: A new taxonomy of compassionate physician behaviours. Health Expect. 18(5):1672–1685.

Chen L, Baird A, Straub D (2019) Fostering participant health knowledge and attitudes: An econometric study of a chronic disease-focused online health community. J. Management Inform. Systems 36(1):194–229.

Chen L, Baird A, Straub D (2020a) A linguistic signaling model of social support exchange in online health communities. Decision Support Systems 130:113233.

Chen W, Wei X, Zhu K (2018) Engaging voluntary contributions in online communities: A hidden Markov model. MIS. Quart. 42(1):83–100.

Chen Q, Yan X, Zhang T (2020b) Converting visitors of physicians personal websites to customers in online health communities: Longitudinal study. J. Med. Internet Res. 22(8):e20623.

Chen Q, Jin J, Zhang T, Yan X (2021) The effects of log-in behaviors and web reviews on patient consultation in online health communities: Longitudinal study. J. Med. Internet Res. 23(6):e25367.

Cheung CM, Xiao BS, Liu IL (2014) Do actions speak louder than voices? The signaling role of social information cues in influencing consumer purchase decisions. Decision Support Systems 65:50–58.

Chib S (2001) Markov chain Monte Carlo methods: Computation and inference. Heckman JJ, Leamer E, eds. Handbook of Econometrics, vol. 5 (Elsevier, North-Holland, Amsterdam), 3569–3649.

Coles P, Kushnir A, Niederle M (2013) Preference signaling in matching markets. Amer. Econom. J. Microeconom. 5(2):99–134.

Connelly BL, Certo ST, Ireland RD, Reutzel CR (2011) Signaling the ory: A review and assessment. J. Management 37(1):39–67.

Duan W, Gu B, Whinston AB (2008) Do online reviews matter? An empirical investigation of panel data. Decision Support Systems 45(4):1007–1016.

Fan W, Zhou Q, Qiu L, Kumar S (2022) Should doctors open online consultation services? An empirical investigation of their impact on offline appointments. Inform. Systems Res. 34(2):629–651.

Fradkin A (2015) Search frictions and the design of online marketplaces. Proc. Third Conf. Auctions, Market Mechanisms Their Appl., (Curran Associates, Inc., Red Hook, NY).

Fradkin A (2017) Search, matching, and the role of digital marketplace design in enabling trade: Evidence from Airbnb. Preprint, submitted March 21, https://dx.doi.org/10.2139/ssrn.2939084.

Frampton SB, Guastello S, Lepore M (2013) Compassion as the foun dation of patient-centered care: The importance of compassion in action. J. Comp. Eff. Res. 2(5):443–455.

Gelhaus P (2012) The desired moral attitude of the physician: Com passion. Med. Health Care Philos. 15(4):397.

Goh JM, Gao G, Agarwal R (2016) The creation of social value: Can an online health community reduce rural-urban health dispari ties? MIS Quart. 40(1):247–263.

Gong Y, Huo Y (2016) A survey of national cardiology workforce in China. Eur. Heart J. Suppl. 18:A1–A5.

Guo ZH (1990) Hospital Management (People’s Health Publishing House, Beijing, China).

Guo Z, Small DS (2016) Control function instrumental variable estimation of nonlinear causal effect models. J. Mach. Learn. Res. 17(100):1–35.

Guo S, Guo X, Fang Y, Vogel D (2017) How doctors gain social and eco nomic returns in online health-care communities: A professional capital perspective. J. Management Inform. Systems 34(2):487–519.

Guo S, Guo X, Zhang X, Vogel D (2018) Doctor-patient relationship strength’s impact in an online healthcare community. Inform. Technol. Dev. 24(2):279–300.

Halaburda H, Jan Piskorski M, Yıldırım P (2018) Competing by restricting choice: The case of matching platforms. Management Sci. 64(8):3574–3594.

Hao H (2015) The development of online doctor reviews in China: An analysis of the largest online doctor review website in China. J. Med. Internet Res. 17(6):e134.

Hao H, Zhang K, Wang W, Gao G (2017) A tale of two countries: International comparison of online doctor reviews between China and the United States. Internat. J. Med. Inform. 99:37–44

Heyman J, Ariely D (2004) Effort for payment: A tale of two markets. Psych. Sci. 15(11):787–793.

Horton JJ (2019) Buyer uncertainty about seller capacity: Causes, conse quences, and a partial solution. Management Sci. 65(8):3518–3540.

Huang N, Yan Z, Yin H (2021) Effects of online-offline service integration on e-healthcare providers: A quasi-natural experiment Production Oper. Management 30(8):2359–2378.

Huang N, Burtch G, He Y, Hong Y (2022a) Managing congestion in a matching market via demand information disclosure. Inform. Systems Res. 33(4):1196–1220.

Huang Z, Duan C, Yang Y, Khanal R (2022b) Online selection of a physician by patients: The impression formation perspective. BMC Med. Inform. Decision Making 22(1):1–15.

Hwang EH, Guo X, Tan Y, Dang Y (2022) Delivering healthcare through teleconsultations: Implications for offline healthcare disparity. Inform. Systems Res. 33(2):515–539.

Jasra A, Holmes CC, Stephens DA (2005) Markov chain Monte Carlo methods and the label switching problem in Bayesian mixture modeling. Statist. Sci. 20(1):50–67.

Jin Y, Tan Y, Huang J (2022) Managing contributor performance in knowledge-sharing communities: A dynamic perspective. Production Oper. Management 31(11):3945–3962.

Johnston AC, Worrell JL, Di Gangi PM, Wasko M (2013) Online health communities: An assessment of the influence of participation on patient empowerment outcomes. Inform. Tech. People 26(2):213–235.

Kim CJ, Nelson CR (1999) State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications (The MIT Press, Cambridge, MA).

Kruschke J (2014) Doing Bayesian Data Analysis: A Tutorial with R, JAGS, and Stan. 2nd ed. (Academic Press, New York).

Kushnir A (2013) Harmful signaling in matching markets. Games Econom, Behav, 80:209–218

Lanzolla G, Frankort HT (2016) The online shadow of offline sig nals: Which sellers get contacted in online B2B marketplaces? Acad. Management J. 59(1):207–231.

Li X, Huang J, Zhang H (2008) An analysis of hospital preparedness capacity for public health emergency in four regions of China: Beijing, Shandong, Guangxi, and Hainan. BMC Public Health 8(1):1–11.

Li J, Liu M, Liu X, Ma L (2018) Why and when do patients use e-consultation services? The trust and resource supplementary perspectives. Telemed. J. E. Health 24(1):77–85.

Li Y, Ma X, Song J, Yang Y, Ju X (2019a) Exploring the effects of online rating and the activeness of physicians on the number of patients in an online health community. Telemed. J. E. Health. 25(11):1090–1098.

Li J, Tang J, Jiang L, Yen DC, Liu X (2019b) Economic success of physicians in the online consultation market: A signaling theory perspective. Internat. J. Electron. Commerce 23(2):244–271.

Liu Q, Liu X, Guo X (2020) The effects of participating in a physiciandriven online health community in managing chronic disease: Evidence from two natural experiments. MIS Quart. 44(1):391–419.

Liu J, Bian Y, Ye Q, Jing D (2019) Free for Caring? The effect of offering free online medical-consulting services on physician performance in e-healthcare. Telemed. J. E. Health 25(10):979–986.

Lovett MJ, Staelin R (2016) The role of paid, earned, and owned media in building entertainment brands: Reminding, informing, and enhancing enjoyment. Marketing Sci. 35(1):142–157.

McNamara GM, Haleblian J, Dykes BJ (2008) The performance implications of participating in an acquisition wave: Early mover advantages, bandwagon effects, and the moderating influence of industry characteristics and acquirer tactics. Acad. Management J. 51(1):113–130.

Merriel S, William D, Andrews V, Salisbury C (2014) Telehealth interventions for primary prevention of cardiovascular disease: A systematic review and meta-analysis. Prev. Med. 64:88–95.

Miller TE, Derse AR (2002) Between strangers: The practice of medi cine online. Health Aff. (Millwood) 21(4):168–179.

Mollick E, Nanda R (2016) Wisdom or madness? Comparing crowds with expert evaluation in funding the arts. Management Sci. 62(6):1533-1553

Netzer O, Lattin JM, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2):185–204.

Pan X, Wen H, Wang Z, Song J, Feng XL (2021) Physician ranking optimization based on patients’ browse behaviors and resource capacities. Internet Res. 31(6):2076–2095.

Rabiner L (1989) A tutorial on hidden Markov models and selected applications in speech recognition. Proc. IEEE 77(2):257–286.

Rossi PE, Allenby GM (2003) Bayesian statistics and marketing. Marketing Sci. 22(3):304–328.

Saner H, Van der Velde E (2016) E-health in cardiovascular medi cine: A clinical update. Eur. J. Prev. Cardiol. 23(2):5–12.

Shukla A, Gao G, Agarwal R (2021) How digital word-of-mouth affects consumer decision making: Evidence from doctor appointment booking. Management Sci. 67(3):1546–1568.

Siemsen E, Roth AV, Balasubramanian S (2008) How motivation, opportunity, and ability drive knowledge sharing: The constraining factor model. J. Oper. Management 26(3):426–445.

Singh PV, Tan Y, Youn N (2011) A hidden Markov model of developer learning dynamics in open source software projects. Inform. Systems Res. 22(4):790–807.

Sliwka D (2007) Trust as a signal of a social norm and the hidden costs of incentive schemes. Amer. Econom. Rev. 97(3):999–1012.

Spence M (1973) Job market signaling. Quart. J. Econom. 87(3): 355–379.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Tadelis S, Zettelmeyer F (2015) Information disclosure as a matching mechanism: Theory and evidence from a field experiment. Amer. Econom. Rev. 105(2):886–905.

Turakhia MP, Desai SA, Harrington RA (2016) The outlook of digi tal health for cardiovascular medicine: Challenges but also extraordinary opportunities. JAMA Cardiol. 1(7):743–744.

Wang N, Liang H, Xue Y, Ge S (2021) Mitigating information asymmetry to achieve crowdfunding success: Signaling and onlin communication. J. Assoc. Inform. Systems 22(3):773–796.

Wang L, Yan L, Zhou T, Guo X, Heim GR (2020) Understanding physicians’ online-offline behavior dynamics: An empirical study. Inform. Systems Res. 31(2):537–555.

Willis E, Royne MB (2016) Online health communities and chronic disease self-management. Health Comm. 32(3):269–278.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data, 2nd ed. (The MIT Press, Cambridge, MA).

Xie K, Lee YJ (2015) Social media and brand purchase: Quantifying the effects of exposures to earned and owned social media activities in a two-stage decision making model. J. Management Inform. Systems 32(2):204.

Yan L, Tan Y (2014) Feeling blue? Go online: An empirical study of social support among patients. Inform. Systems Res. 25(4): 690–709.

Yang H, Yan Z, Jia L, Liang H (2021) The impact of team diversity on physician teams’ performance in online health communities Inform. Process. Management 58(1):102421.

Yu H, Wang Y, Wang JN, Chiu YL, Qiu H, Gao M (2020) Causal effect of honorary titles on physicians’ service volumes in online health communities: Retrospective study. J. Med. Interne Res. 22(7):e18527.

Zhang X, Kumar V, Cosguner K (2017) Dynamically managing a profitable email marketing program. J. Marketing Res. 54(6): 851–866.

Zhang X, Guo X, Lai KH, Yi W (2019) How does online interactional unfairness matter for patient–doctor relationship quality in online health consultation? The contingencies of professional seniority and disease severity. Eur. J. Inform. Systems 28(3):336–354.

Zhou J, Kishore R, Amo L, Ye C (2022) Description and demonstra tion signals as complements and substitutes in an online mar ket for mental healthcare. MIS Quart. 46(4):2055–2084.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
