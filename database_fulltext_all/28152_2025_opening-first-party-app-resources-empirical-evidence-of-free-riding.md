---
otero_id: 28152
otero_key: "FSUP5W7C"
title: "Opening First-Party App Resources: Empirical Evidence of Free-Riding"
authors: "Franck Soh; Pankaj Setia; Varun Grover"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0607"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Opening First-Party App Resources: Empirical Evidence of Free-Riding

Franck Soh,<sup>a,</sup>\* Pankaj Setia,<sup>b</sup> Varun Grover<sup>c</sup>

<sup>a</sup> Neeley School of Business, Texas Christian University, Fort Worth, Texas 76109; <sup>b</sup> Indian Institute of Management Ahmedabad, Ahmedabad, Gujarat 380015, India; <sup>c</sup> Walton College of Business, University of Arkansas, Fayetteville, Arkansas 72701

Contact: f.l.sohnoume@tcu.edu, https://orcid.org/0000-0002-6131-5861 (FS); pankajsetia@iima.ac.in (PS); VGrover@walton.uark.edu (VG)

Received: December 1, 2021 Revised: June 13, 2022; April 21, 2023; December 9, 2023; March 16, 2024 Accepted: April 25, 2024 Published Online in Articles in Advance: July 26, 2024

https://doi.org/10.1287/isre.2021.0607

Copyright: © 2024 INFORMS

Abstract. Platform owners are releasing their own apps on their platforms. These firstparty apps (FPAs) typically leverage platform resources more effectively, competitively threatening rivals. Although the impact of FPAs on rivals’ innovation has been the subject of extensive study, the dominant view in previous research assumes that these FPAs are closed to third-party apps (TPAs). However, there is an increasing trend of FPAs opening their resources to TPAs, as they provide application programming interfaces (APIs) allowing TPAs to access their resources. Rivals still exist, as many TPAs choose not to have access to FPAs’ open resources because of their limited control over these resources. Does opening an FPA’s resources impact rivals’ innovation? The answer to the question is largely unknown. We exploit the release of the Apple Health Records API, a feature that opens Apple Health Records to TPAs, to design a quasi-experiment that investigates whether and how opening an FPA’s resources influence rivals’ innovations. Through several analyses, we conclude that opening an FPA’s resources to TPAs generates free-riding benefits for rivals. Moreover, these benefits mainly arise because of the growing presence of TPAs that do not adopt FPAs’ open resources in the market. We discuss the theoretical contributions and practical implications of our findings.

History: Paul A. Pavlou, Senior Editor; Khim Yong Goh, Associate Editor. Funding: This work was funded in part through an endowed chair at the Sam M. Walton College of Business, University of Arkansas. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0607.

Keywords: openness • mobile platform • innovation • competition • spillover

## 1. Introduction

The relationship between third-party apps (TPAs) and first-party apps (FPAs) is a complex one characterized by both rivalry and sharing dynamics. An FPA is an app created by the platform owner.<sup>1</sup> An FPA’s rivals (called rivals from now on for simplicity) are TPAs (i.e., apps created by third-party developers) that belong to the same market as the FPA and do not share the FPA’s resources.<sup>2</sup> Because FPAs benefit from tighter integration with the platform (Li and Agarwal 2017), the issue of how rivals can overcome the FPA advantage in the same market has been a concern for scholars for several years. Failure to compete can threaten the survival of rivals, and ultimately the platform. The dominant approach in the research studying this issue assumes that FPAs have exclusive access to their resources, that is, FPAs do not share their resources with any TPA (Foerderer et al. 2018, Wen and Zhu 2019). As one example, Wen and Zhu (2019) indicate that FPAs exclusive resources give FPAs an innovation advantage over rivals by demonstrating that Google’s entry into the market (as an FPA) reduces rivals’ innovation.

Recently, many FPAs have challenged the assumption of exclusive access to platform resources. There are several cases of coopetition between FPAs and TPAs through FPAs’ openness, as the latter share the FPAs resources. FPAs relinquish their resource exclusivity by opening up their resources to TPAs to foster innovation and consumer demand in the market<sup>3</sup> (see Huang et al. 2020). FPAs’ openness occurs through application programming interfaces (APIs) that enable resource openness (e.g., open data). This is different from platformlevel openness. Compared with FPAs’ openness, which highlights coopetition (i.e., both rivalry and cooperation) between FPAs and TPAs, platform-level openness does not involve rivalry between the platform and TPAs as the emphasis is on cooperation.<sup>4</sup> Examples of FPAs opening their data with TPAs include the Health Record app (FPA) and medical apps (TPAs) through the Health Records API, Apple Weather app (FPA) and weather apps (TPAs) through WeatherKit, Apple Music app (FPA) and music apps (TPAs) through the Music API and MusicKit, and Health app (FPA) and health and fitness apps (TPAs) through HealthKit. Although TPAs may choose to access an FPA’s open resources, many of them see this access as a competitive initiative by the FPA and maintain a rivalry with the FPA.

Openness is a new platform paradigm influencing the relationship between FPAs and TPAs. It changes the platform dynamics and might challenge previous findings, as the relationship in the new paradigm is not just about rivalry but also involves cooperation between FPAs and TPAs. Openness complicates the relationship (by catalyzing coopetition) between FPAs and TPAs in general and between FPAs and rivals in particular (Foerderer et al. 2018, Wen and Zhu 2019). Notably, even though FPAs and their rivals do not share resources (i.e., rivals are not direct beneficiaries of FPAs’ open resources), opening FPAs’ resources may increase the overall market size. Established mechanisms such as racing<sup>5</sup> and spillover<sup>6</sup> (Foerderer et al. 2018) commonly used in prior findings do not account for resource openness. Specifically, it is still unclear whether and how opening an FPA’s resources influence innovation by rivals (i.e., TPAs that do not participate in sharing the FPA’s open resources). Addressing this research gap is particularly important and will contribute to a deeper understanding of platform dynamics beyond how an FPA with closed resources impacts rivals’ innovation (e.g., Foerderer et al. 2018). Therefore, we tackle this gap by answering the following research question: how does FPAs’ openness impact rivals’ innovation?

We use the theoretical arguments from the alliances literature to examine the research question. The literature on alliances is relevant for our study as rivals do not have access to resources shared in the alliance, and thus may not benefit directly from the alliance. Previous research on alliances suggests that two mechanisms could explain the impact of FPAs’ openness on rivals (Oxley et al. 2009, Han et al. 2012). According to the competitiveness-enhancement mechanism, an alliance weakens rivals as they miss out on resource accumulation (i.e., access to additional resources). Based on this mechanism, we underline that FPAs’ openness enhances an FPA’s competitiveness as it allows seamless integration with TPAs, making its rivals weaker competitors. In contrast, according to the positive market growth mechanism, an alliance increases market size, resulting in positive abnormal returns for rivals. Based on this mechanism, we argue that FPAs’ openness enables rivals to take advantage of free-riding effects through greater overall market demand (i.e., an increase in the market size). In summary, following alliances literature, we expect competitiveness enhancement and positive market growth to be two competing mechanisms that may explain the impact of FPAs openness on rivals’ innovations.

In accordance with prior research on alliances, our focus on rivals allows us to disentangle the two mechanisms as these two mechanisms have distinct (i.e., negative and positive) effects on rivals (see Oxley et al. 2009). To do so, we use a novel empirical approach by assessing the impact of an FPA with open resources on rivals’ innovation. We disentangle the two mecha nisms associated with the FPA’s openness by (a) conducting a quasi-experiment designed around the release of the Apple Health Records API and (b) focusing on rivals. Our analyses yield multiple findings.

First, our findings show support for the positive market growth mechanism, demonstrating the existence of free-riding benefits for rivals. Specifically, we found that FPAs’ openness increases the consumer demand for rivals. Second, in light of the previous finding and as a follow-up to our previous research question, we answer the following research question: how does positive market growth occur? Although prior literature suggests that a spillover effect (Foerderer et al. 2018) is a potential source that causes an increase in consumer demand, it is unclear how this effect occurs when FPAs open their resources in the market. We propose that spillover could happen directly as consumers join the market because they can have improved experiences (e.g., better customization) in TPAs adopting FPAs open resources, or indirectly as consumers join the market because they can access a greater number of offerings from TPAs that do not adopt FPAs’ open resources but still complement them. We call these TPAs that do not adopt FPAs’ open resources alternatives because they are alternatives to rivals.<sup>7</sup> As a result of more consumers joining the market, some of the added consumer demand may spill over to rivals, leading to an increase in rivals’ consumer demand.

We separate indirect spillover into two subtypes depending on the type of alternatives: (a) samemarket alternatives refer to the alternatives whose pri mary market overlaps with the focal app’s primary market and (b) other-market alternatives refer to alter natives whose secondary market overlaps with the focal app’s primary market. In mobile platforms, a TPA has two markets: a primary one and a secondary one. This engenders two types of alternatives including same-market and other-market alternatives. For exam ple, for a medication management TPA (i.e., a TPA whose primary market is the medication management market), all TPAs whose primary market is the medica tion management market are same-market alternatives, and all TPAs whose secondary market is the medication management market are other-market alternatives. Because our focal apps are rivals (i.e., TPAs that do not adopt FPAs’ open resources), in addition to having their primary or secondary market equate to the rival’s market, alternatives also do not adopt FPAs’ open resources.

We empirically test the indirect spillover effect through the creation of alternatives. Our findings indicate that the number and differentiation of othermarket alternatives (i.e., lack of similarity between rivals and other-market alternatives) increase rivals consumer demand, thus explaining the positive market growth mechanism. Interestingly, a greater number and differentiation of same-market alternatives (i.e., lack of similarity between rivals and same-market alternatives) reduce rivals’ consumer demand.<sup>8</sup> This is consistent with prior research suggesting that product expansion may reduce consumer demand when competition is intense (Aghion and Griffith 2008, Boudreau 2012). After accounting for the number and differentiation of alternatives, the direct effect of FPAs’ openness on the consumer demand for rivals is statistically insignificant, suggesting that direct spillover is not the main driver of positive market growth, but indirect spillover is. The two types of spillover suggest two types of consumers joining the market as a result of FPAs’ open resources. Because we find significance for indirect spillover, it implies that rivals attract more consumers joining because of complementary offerings through alternatives, rather than consumers joining because of improved experiences through TPAs that adopt FPAs open resources. Finally, in a set of additional analyses, we confirm that capable and resourceful developers (i.e., developers with high portfolio size and diversification) are more likely to be motivated by positive market growth to innovate.

## 2. Theoretical Background

## 2.1. Theoretical Mechanisms

2.1.1. Competitiveness-Enhancement and Positive Market Growth Mechanisms. Previous research examining value creation in alliances proposes two underlying mechanisms (Oxley et al. 2009). The first mechanism, called the competitiveness-enhancement mechanism, indicates that an alliance lowers rivals’ market value as the alliance gets more competitive by sharing their resources (Oxley et al. 2009). The second mechanism, called the positive market growth mechanism, indicates that an alliance increases the overall market demand (or economic pie), resulting in higher market value for both the alliance and its rivals (Han et al. 2012).

According to the competitiveness-enhancement mechanism, the main motivation for forming alliances is to increase the technological resource base (Teece 1992, Inkpen and Dinur 1998, Lane and Lubatkin 1998). A key premise is that the sharing of resources provides an alliance a competitive advantage over its rivals, for example, by facilitating seamless integration in the alliance (Nakamura et al. 1996, Khanna et al. 1998). According to the positive market growth mechanism, alliances can benefit the market by increasing market size, benefiting both the alliance and its rivals (Han et al. 2012).

In the context of FPA and TPAs,<sup>9</sup> we expect that competitiveness enhancement is a potential mechanism as one could argue that the FPA becomes more competitive than its rivals because opening the FPA’s resources may facilitate seamless integration of the FPA with TPAs.<sup>10</sup> This may lead to a reduction in the market valuation of rivals. We also expect that positive market growth is a potential mechanism as one could argue that opening FPAs’ resources increases the economic pie (because of increased market demand), enabling both the FPA and its rivals to receive greater consumer demand.<sup>11</sup>

The two mechanisms coexist in the market, and in some situations, one may dominate the other. For instance, the competitiveness-enhancement mechanism is likely to dominate the positive market growth mechanism in situations where resource sharing occurs in a closed arrangement (i.e., only a small number of TPAs can integrate FPAs’ resources). Examples of such arrangements include Apple Siri and Shazam in 2014, Apple Siri and Wikipedia in 2013, Apple Siri and Twitter in 2013, and Apple Siri and Facebook in 2013. However, in an open network environment, this exclusivity could be tempered. The positive market growth mechanism is likely to dominate the competitiveness-enhancement mechanism in situations wherein the overall market size increases significantly. For example, several FPAs’ openness initiatives (e.g., MusicKit, WeatherKit, and Health-Kit) on iOS allow any TPA to integrate with Apple Music, Weather, and Health apps, respectively. Rivals benefit from such market expansion even without integrating FPAs’ resources.

Prior literature on alliances discusses the coexistence of competitiveness enhancement and positive market growth forces by highlighting that firms’ motives for joining an alliance include competitiveness enhancement and positive market growth (Han et al. 2012). Thus, following this literature, we expect competitiveness enhancement and positive market growth to be two competing mechanisms that explain the impact of FPAs’ openness on rivals’ innovation. If competitiveness enhancement is dominant, rivals respond to an FPA becoming a stronger competitor by increasing their innovation (see Foerderer et al. (2018) for a discussion on racing). If positive market growth is dominant, we suggest that an increased consumer demand offers new opportunities for rivals to innovate (see Foerderer et al. (2018) for a discussion on consumer demand spillover).

2.1.2. Spillover Effects. Spillover effects are common sources of consumer demand growth (Foerderer et al. 2018). An FPA’s openness enables the FPA to share resources with TPAs, facilitating the creation of tailored consumer experiences in TPAs, thus driving up the consumer demand in the market. For instance, Apple’s

Health Records (FPA) enables TPAs (like Medisafe) to access customer data that allow them to customize their prescription services. In preparation for the public release of FPAs’ openness, platform owners demonstrate this experience customization benefit by working with TPAs (also called launch TPAs) and extensively promoting the advantages of FPA open resources to consumers through press releases, media interviews, and outreach events (e.g., worldwide developer conference (WWDC) events) (Apple 2018b). By doing so, platform owners ensure that FPAs’ openness drives more consumer demand in the market from which rivals benefit. In this study, we refer to this form of spillover as direct spillover. Numerous studies in consumer research discuss demand spillover between first-party products and rivals (Foerderer et al. 2018, He et al. 2020). For example, Foerderer et al. (2018) suggest that increased consumer attention in the market due to the release of the FPA (Google Photo app) may spill over to rivals (apps in the Photography category).

There is another form of spillover that has been less explored in prior literature which explains the impact of FPAs on rivals’ innovation. This spillover manifests as FPAs’ openness stimulating alternatives (i.e., TPAs that do not adopt FPAs’ open resources) to join the market because such alternatives could complement FPAs’ open resources. For example, the Health Records API allows patients to access medication records directly from their medical institution. TPAs can focus on complementary features (e.g., drug-to-drug interactions, reminder scheduling, etc.). The logic is that consumers may use FPA open resources to import their medication records from their medical institution. Next, they could add these records manually in the TPAs to access complementary offerings. We refer to this form of spillover as indirect spillover.

According to the generativity effect,<sup>12</sup> a greater number and differentiation of TPAs attract more consumers in the market (Boudreau 2012),<sup>13</sup> of which rivals attract some. This is built on the premise that a greater number and differentiation of TPAs increase consumers’ selection of TPAs. Still, per the generativity effect, a greater number and differentiation of TPAs in one category may drive an expansion of users in a different category. However, a greater number and differentiation of TPAs in the same category may intensify competition and reduce consumer demand. Hence, product expansion may drive consumer demand, but intense competition may reduce consumer demand<sup>14</sup> (Aghion and Griffith 2008, Boudreau 2012).

Direct and indirect spillovers provide different reasons for the increase in consumer demand in the market.<sup>15</sup> The former suggests that consumers join the market looking for improved (more individualized) experiences in TPAs that adopt FPAs’ open resources, whereas the latter posits that consumers join the market as the number and variety of complementary offerings through alternatives (i.e., TPAs not adopting FPAs open resources) increase. According to the spillover effect, the increased demand in the market may spill over to rivals in the same market. The new demand and feedback enable innovation (Liu et al. 2014, Li and Agarwal 2017, Foerderer et al. 2018). Notably, they provide new ideas and opportunities on which rivals can build to innovate. Following this rationale, FPAs’ openness may increase consumer demand for rivals through the direct or indirect spillover effect, stimulating more innovation by these rivals. Figure 1 presents the conceptual framework.

## 2.2. Openness

In prior literature, the impact of FPA on rivals’ innovation does not account for FPAs’ openness (Foerderer et al. 2018). FPAs’ openness provides TPAs access to the FPAs’ resources, through boundary resources such as APIs made available by the platform owners (Karhu et al. 2018). For example, the release of the Apple Health Records API enables TPAs to access the health record data of iOS users after obtaining the permission of the iOS users. FPAs’ openness promotes the creation of TPAs, including those that do not use the FPA’s APIs.

We argue that FPAs’ openness increases the number of alternatives (i.e., TPAs not adopting FPAs’ open resources). FPAs’ openness creates complementarity opportunities between FPAs’ open resources and alternatives, thus stimulating the development of alternatives. Moreover, FPAs’ openness draws app developer attention to the market because platform owners promote FPAs’ open resources (e.g., in press releases) and increase FPAs’ open resources visibility by announcing them at large developer events. Platform owners can reach a virtually limitless and heterogeneous pool of developers (Baldwin and Clark 2000, Chesbrough 2006, Yoo et al. 2010). As a result, FPAs’ openness encourages the development of alternatives that seek to complement FPAs’ open resources.

FPAs’ openness facilitates the creation of more or less differentiated alternatives as the relationship between FPAs’ openness and alternatives’ differentiation is unclear. On one hand, creating more differenti ated alternatives incurs more innovation risks (i.e., more uncertainty regarding innovation rents) as, at their creation, alternatives do not have an established position in the market. The lack of an established consumer base makes experimentation challenging and competition with rivals risky. On the other hand, creating more differentiated alternatives incurs fewer innovation risks if the alternatives and the rivals do not have the same main market. This happens because competition between alternatives and rivals is reduced when they do not have the same main market. Thus, we posit that FPAs’ openness increases the differentiation of other-market alternatives but reduces that of same-market alternatives.

Figure 1. Conceptual Framework  
![](/api/attachments/FSUP5W7C/fulltext/images/a8d2d136de010d6bfa1fcdb3adf20718d0d5dd079a7de6748c2c2ceddbc02023.jpg)

In situations where competition is not intense, a high number and differentiation of alternatives (i.e., product expansion) increase the overall market demand in the market (because of the generativity effect) and ultimately rivals’ consumer demand. Because of this, we expect that the number and differentiation of othermarket alternatives increase rivals’ consumer demand. In situations where competition is intense, product expansion $( \mathrm { i . e . , }$ an increase in the number and differentiation of alternatives) reduces rivals’ consumer demand (Aghion and Griffith 2008, Boudreau 2012). Because of this, we expect that the number and differentiation of same-market alternatives diminish rivals consumer demand.

## 3. Methods

## 3.1. Empirical Context: Release of Apple Health Records API

We investigate the impact of FPAs’ openness, notably through the Apple Health Records API, on rivals’ innovation. Health Records is an iOS feature that enables patients to access medical information from hundreds of medical institutions (Apple 2018a). The Apple Health Records API contributes to patients’ engagement in their healthcare. Notably, through the API, iOS users allow the sharing of their medical records with their favorite trusted TPAs, hence contributing to health improvement. With the permission of iOS users, TPAs can customize individual experiences to the user’s unique health history across categories such as medication tracking, disease management, and nutrition planning. Apple introduced the Health Records feature as part of iOS 11.3 in March 2018. iOS 11.3 beta was available to Apple’s public beta testing group and iOS third-party developers in January 2018. Hence, third-party developers could prepare their responses when the Health Records feature became public in March 2018. Despite its public release in March 2018, the Health Records feature remained closed to TPAs until September 2018 when Apple made available the public release of iOS 12 (i.e., no TPA could use the Health Records API before September 2018). The iOS 12 beta was available to third-party developers from June 2018 onward, giving time to third-party developers to respond (e.g., by integrating APIs such as the Apple Health Records API) before the public release date (i.e., September 2018). Medisafe is an example of TPAs that made available a feature supporting the Apple Health Records API to users publicly a few days after the public release date of the Apple Health Records API in September 2018. By releasing the Health Records API, Apple seeks to build seamless integration with TPAs to improve the management of diseases, nutrition plans, medications, and more (Apple 2018b).

## 3.2. Research Design

Because the release of the Apple Health Records API is an exogenous shock to rivals, we used it as part of our identification strategy to assess the impact of FPAs openness on rivals’ innovation (see Online Appendix A). We focus on public releases instead of beta releases because any feature that third-party developers build by integrating the API will not be accessible to users before the public release of iOS. Beta versions of iOS are available to third-party developers to test-drive the API before the public release of iOS. Hence, any impact of the API on rivals’ innovation will be observable from the date of the public release of iOS. We conduct a quasi-experiment by exploiting the public release of the Apple Health Records API, which is part of iOS 12. We assess the impact of the Health Records API on the innovation of rivals. The prerelease period is from April 1, 2018, to August 31, 2018. The postrelease period is from October 1, 2018, to July 31, 2019. We exclude September 2018 because Apple’s Health Records API $\left( \mathrm { i . e . , i O S } \right)$ official public release date is September 17, 2018.

We use topic modeling Latent Dirichlet Allocation (LDA) to identify markets in the Medical and Health &

Fitness app categories. Text-based approaches such as topic modeling to determine markets are a common practice in prior literature (Leyden 2022). We follow standard text cleaning and processing approaches including (a) removing web links from apps’ descriptions; (b) replacing abbreviated negations (e.g., “hasn’t” with “has not”); (c) keeping nouns and proper nouns (i.e., ‘NN’, ‘NNS’, ‘NNP’, and ‘NNPS’ tags); (d) excluding dates, times, and geographical entities (e.g., countries, states, cities); (e) removing punctuation and words not composed of letters; and (f) stemming remaining words (see Pan et al. 2019). The topics created using LDA topic modeling are taken as markets. Hence, the topic with the highest weight corresponds to the main market of the app. We validate our topic modeling by ensuring that it is comparable to prior studies’ topic modeling. For example, the topics (e.g., workout, running, nutrition, yoga, and pregnancy) obtained from the Health & Fitness category match the topics created by Kang and Suarez (2022).

We design a quasi-experiment. Considering that the Health Records API allows the sharing of the data types allergies, conditions, immunizations, laboratory results, medications, procedures, and vitals, we focus on medication management TPAs as they are directly impacted by Apple Health Records. As indicated before, some TPAs (e.g., Medisafe) in the medication management market integrate the Apple Health Records API. Hence, our treatment group consists of rivals (i.e., medication management TPAs that do not integrate the Apple Health Records API). The control group consists of TPAs in the workout market. Out of all the app categories in the App Store, Health & Fitness is the app category that is the most similar to the Medical app category. We confirm this by enumerating the secondary category listed by all TPAs whose primary category is Medical. Health & Fitness ranks first. Because medication management is a subcategory of the Medical category, we choose workout, which is a subcategory of the Health & Fitness category, to identify the control group. Workout TPAs are not affected by Apple Health Records because workout data are not a type of data managed by Apple Health Records (i.e., allergies, conditions, immunizations, laboratory results, medications, procedures, and vitals).

Moreover, because workout TPAs belong to the Health & Fitness category, we excluded workout TPAs whose secondary category is the Medical category to avoid any overlap with the treatment group. Furthermore, we ensure that all workout TPAs in our sample do not integrate the Health Records API. We also ensure that in the postrelease period, no other significant Health-related API and feature were released by either Apple or Google on their platforms. Finally, we use propensity score matching (PSM) to ensure that TPAs in control and treatment groups match during the prerelease period using one-on-one nearest neighbor matching without replacement. The variables used for PSM include average ratings, the logarithm of the number of reviews, the number of months since the release of the app, pricing, and major updates (see Online Appendix C).

## 3.3. Variables

3.3.1. App Updates. We distinguish between minor and major app updates, following prior studies (Leyden 2022). A major update corresponds to an update that adds additional functionality and content. A minor update corresponds to performance improvements, adjustments to ensure compatibility with the latest version of iOS, changes to an existing feature, and bug fix ing. Our approach uses machine-learning predictions to identify major and minor app updates (please see Online Appendix D for more details on the approach).

3.3.2. Competitiveness Enhancement and Positive Market Growth. Following Foerderer et al. (2018), we use the monthly difference in the number of app reviews to measure positive market growth. The num ber of app reviews is commonly used to measure consumer attention (i.e., level of consumer interest in the app) as primary data about consumer attention are challenging to obtain (Foerderer et al. 2018). We log transform the number of app reviews. Moreover, we use the monthly difference in average app ratings to measure competitiveness enhancement. We derive this measure from the approach of Foerderer et al. (2018) to measuring racing. App ratings are scores from one to five with higher values indicating greater app quality (i.e., consumer satisfaction with the implementation of the app’s features) (Foerderer 2020).

3.3.3. Alternatives. We calculate monthly differences in the number and differentiation of alternatives. We separate alternatives into two groups: samemarket alternatives and other-market alternatives. We compute the monthly differences in alternatives by counting the alternatives that enter the market in a given month and applying a natural logarithm transformation. Next, we compute the monthly differences in alternatives’ differentiation by assessing the text similarity between a rival and alternatives that enter the market in a given month. The more similarity that exists between a rival and alternatives that enter the market, the less differentiated are the alternatives. In a given month, for each alternative, we create two documents: the first document contains the description of the alternative that enters the market, and the second document contains the description of the rival. We follow standard text cleaning and processing approaches (already discussed above in the LDA step) before calculating cosine similarity. We compute the cosine similarity between the two documents using term frequency-inverse document frequency (TF-IDF) weights (Pan et al. 2019) (see equation below). Then, we calculate the average of all similarity scores across alternatives.

$$
S I M _ {j _ {1} j _ {2}} = \frac {\overrightarrow {T F - I D F} _ {j _ {1}} \times \overrightarrow {T F - I D F} _ {j _ {2}}}{\left| \overrightarrow {T F - I D F} _ {j _ {1}} \right| \times \left| \overrightarrow {T F - I D F} _ {j _ {2}} \right|},
$$

where $S I M _ { j _ { 1 } j _ { 2 } }$ is the cosine similarity between documents $j _ { 1 }$ and $j _ { 2 , \ L }$ , and $T F \ – I D F _ { j _ { 1 } }$ and $T F \ – I D F _ { j _ { 2 } }$ represent the vectors of TF-IDF weights of documents $j _ { 1 }$ and $j _ { 2 } ,$ respectively. The level of similarity is a score between zero and one. The level of differentiation equals one minus the similarity score. Online Appendix B describes the measurement of all variables in our study.

## 3.4. Econometric Models

The specification in Equation (1) describes the effect of FPAs’ openness through the release of the Apple Health Records API on rivals’ major updates. The specifications in Equations (2)–(4) test positive market growth and competition enhancement by assessing the mediation effects of the monthly differences in the number of reviews and average app ratings, respectively. First, we specify the equations to estimate the effect of FPAs’ openness through the release of the Apple Health Records API on the two mediators (see Equations (2) and (3)). Next, we specify the equation to estimate the effects of the two mediators on rivals’ major updates while controlling the effect of FPAs’ openness through the release of the Apple Health Records API (see Equation (4)).

$$
\begin{array}{r l} \text { MAJOR   UPDATE } _ {i, t} & = \beta_ {0} + \beta_ {1} \text { AFTER } _ {t} \times \text { OPENNESS } _ {i} \\ & + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \end{array} \tag {7}\tag{1}
$$

$$
\begin{array}{r l} R E V I E W S D I F F _ {i, t} & = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} \\ & + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \end{array}\tag{2}
$$

$$
\begin{array}{c} R A T I N G D I F F _ {i, t} = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} \\ + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \end{array}\tag{3}
$$

$$
\begin{array}{r l} M A J O R U P D A T E _ {i, t} & = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} \\ & \quad + \beta_ {2} R E V I E W S D I F F _ {i, t} \\ & \quad + \beta_ {3} R A T I N G D I F F _ {i, t} + \theta_ {i} + \mu_ {t} \\ & \quad + \varepsilon_ {i, t} \end{array}\tag{4}
$$

The following specifications represent the equations used to test the indirect spillover effect by assessing the mediation effects of the number and differentiation of alternatives. First, we specify the equations to estimate the effect of FPAs’ openness through the release of the Apple Health Records API on the mediators (see Equations (5)–(8)). Next, we specify the equations to assess the effects of the mediators on the monthly differences in the number of reviews while controlling the effect of FPAs’ openness through the release of the Apple

Health Records API (see Equation (9)).

$$
S A M E M A R K E T A L T E R N A T I V E S _ {i, t}
$$

$$
= \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t}\tag{5}
$$

$$
S A M E M A R K E T A L T E R N A T I V E S D I F F _ {i, t}
$$

$$
= \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t}\tag{6}
$$

$$
O T H E R M A R K E T A L T E R N A T I V E S _ {i, t}
$$

$$
\begin{array}{c} = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \\ O T H E R M A R K E T A L T E R N A T I V E S D I F F _ {i, t} \end{array}\tag{7}
$$

$$
\begin{array}{c} = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \\ R E V I E W D I F F _ {i, t} \end{array}\tag{8}
$$

$$
\begin{array}{l} = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times O P E N N E S S _ {i} \\ \quad + \beta_ {2} S A M E M A R K E T A L T E R N A T I V E S _ {i, t} \\ \quad + \beta_ {3} S A M E M A R K E T A L T E R N A T I V E S D I F F _ {i, t} \\ \quad + \beta_ {4} O T H E R M A R K E T A L T E R N A T I V E S _ {i, t} \\ \quad + \beta_ {5} O T H E R M A R K E T A L T E R N A T I V E S D I F F _ {i, t} \\ \quad + \theta_ {i} + \mu_ {t} + \varepsilon_ {i, t} \end{array}\tag{9}
$$

SAMEMARKETALTERNATIVES , SAMEMARKET-ALTERNATIVESDIFF , OTHERMARKETALTERNA-$T I V E S _ { i , t } ,$ OTHERMARKETALTERNATIVESDIFF , MAJOR $U P D A T E _ { i , t } ,$ $R E V I E W S D I F F _ { i , t } ,$ and RATING $D I F F _ { i , t }$ are measured in month t for TPA $i , A F T E R _ { t }$ equals one if the current month is after the release of the Apple Health Records API, OPENNESS equals one if the TPA belongs to the treatment group, $\theta _ { i }$ are the app fixed effects, $\mu _ { t }$ are the time fixed effects, and $\varepsilon _ { i , t }$ is the error term.

In Equations (1)–(9), we omit the main effects of After and Openness because they are collinear with the app and time fixed effects. The level of analysis is the app-month level. We use difference-in-difference and propensity score matching (DiD + PSM) to estimate the above empirical models. Moreover, following Foerderer et al. (2018), all our empirical models with a major update as the dependent variable are specified as linear probability models (LPM) because they are more robust than a logit formulation when estimating a large number of fixed effects. Table 1 presents the descriptive statistics and correlations.

## 3.5. Results

3.5.1. Impact of Apple Health Records API on Rivals Innovation. We investigate the impact of FPAs’ open ness (i.e., the Apple Health Records API) on rivals’ innovation. Model 1 (see Table 2) indicates that AFTER × OPENNESS increases MAJOR UPDATE. The results show that the probability of major updates increases by 0.0035 $( p < 0 . 0 5 )$ after the release of the Apple Health Records API. Such an increase suggests that FPAs’ openness through the Apple Health Records API enhances rivals’ innovation. This change is significant considering that the average probability of a major update is 0.0034. Figure 2 illustrates the marginal probabilities of a major update with the vertical line representing the release of the Health Records API.

Table 1. Descriptive Statistics and Correlation Matrix

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1. ReviewsDiff</td><td>0.0221</td><td>0.2023</td><td>0</td><td>6.2066</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. RatingDiff</td><td>-0.0004</td><td>0.2153</td><td>-3.8571</td><td>3.9385</td><td>0.2083*</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Major Update</td><td>0.0034</td><td>0.0579</td><td>0</td><td>1</td><td>0.1574*</td><td>0.0103*</td><td>1</td><td></td><td></td><td></td></tr><tr><td>4. SameMarketAlternativesDiff</td><td>0.7727</td><td>0.1167</td><td>0.2268</td><td>0.9991</td><td>-0.0543*</td><td>0.0007</td><td>-0.0134*</td><td>1</td><td></td><td></td></tr><tr><td>5. OtherMarketAlternativesDiff</td><td>0.8247</td><td>0.0778</td><td>0.4678</td><td>0.9971</td><td>-0.0669*</td><td>-0.0001</td><td>-0.0254*</td><td>0.6647*</td><td>1</td><td></td></tr><tr><td>6. SameMarketAlternatives</td><td>4.9331</td><td>0.9566</td><td>3.2189</td><td>6.1924</td><td>0.0050*</td><td>-0.0014</td><td>-0.0101*</td><td>-0.1618*</td><td>0.0650*</td><td>1</td></tr><tr><td>7. OtherMarketAlternatives</td><td>4.6041</td><td>0.3804</td><td>3.9512</td><td>5.2364</td><td>0.0046*</td><td>0.0002</td><td>-0.0092*</td><td>-0.0474*</td><td>-0.0028</td><td>0.5495*</td></tr></table>

Note. N � 231,042.  
\*p < 0.05.

3.5.2. Test of Competitiveness-Enhancement and Positive Market Growth Mechanisms. We test the competitiveness-enhancement and positive market growth mechanisms by assessing the mediating effects of the monthly differences in the average ratings, and the number of reviews, respectively. Baron and Kenny’s (1986) three-step mediation analysis procedure shows empirical support for the positive market growth mechanism.

The first step consists of estimating the effect of AFTER × OPENNESS on MAJOR UPDATE. Model 1 of Table 2 indicates that such an effect is positive and significant. In the second step, we assess the effect of the mediators on MAJOR UPDATE. Model 2 of Table 2 shows that REVIEWSDIFF increases MAJOR UPDATE $( \beta = 0 . 0 3 2 2 , p < 0 . 0 0 1 )$ , but RATINGDIFF does not (β � �0.0002, p > 0.1). In the third step, we assess the effect of AFTER × OPENNESS on the mediators. Model 1 of Table 3 shows that AFTER × OPENNESS increases REVIEWSDIFF (β � 0.0121, p < 0.001). The overall result from the three-step mediation reveals a mediation of the effect of AFTER × OPENNESS on MAJOR UPDATE via REVIEWSDIFF, which is supported by the Sobel (statistic � 3.1012, p < 0.01) test. Hence, the positive market growth mechanism is the underlying mechanism explaining the impact of FPAs’ openness on rivals innovation.

Table 2. Effect of FPA’s Openness on Rivals’ Innovation

<table><tr><td rowspan="2"></td><td colspan="2">Major update</td></tr><tr><td>Model 1</td><td>Model 2</td></tr><tr><td rowspan="2">After × Openness</td><td>0.0035*</td><td>0.0032+</td></tr><tr><td>(0.0017)</td><td>(0.0017)</td></tr><tr><td rowspan="2">ReviewsDiff</td><td></td><td>0.0322***</td></tr><tr><td></td><td>(0.0087)</td></tr><tr><td rowspan="2">RatingDiff</td><td></td><td>-0.00023</td></tr><tr><td></td><td>(0.0013)</td></tr><tr><td rowspan="2">Constant</td><td>-0.0252*</td><td>-0.0245*</td></tr><tr><td>(0.0124)</td><td>(0.0123)</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>231,042</td><td>231,042</td></tr><tr><td>N of groups</td><td>15,418</td><td>15,418</td></tr><tr><td>R2</td><td>0.001</td><td>0.002</td></tr></table>

Notes. Estimator � fixed effects with robust standard errors, that is, standard errors clustered by app. We control for the number of alternatives that are incumbent or exiting. Ninety-five percent confidence intervals are included.  
<sup>+</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

3.5.3. Test of Spillover Effects. After confirming that positive market growth is the mechanism through which FPAs’ openness influences rivals’ innovation, we test whether positive market growth occurs because of direct or indirect spillover. We test the indirect spill over effect by assessing the mediating effects of the number and differentiation of alternatives. We use external instruments to address self-selection bias asso ciated with product expansion (i.e., the decision to create alternatives in a chosen market). We identify three instruments, namely, competitors’ competitors’ market uncertainty (i.e., complexity and dynamism) and growth (i.e., growth of consumer demand). As illustrated in Figure 3, we keep only competitors’ competitors that belong to the market closest to the focal market. Based on Figure 3, our instruments are market uncertainty and growth in the market composed of P. The instruments are valid because (a) P directly influences product expansion in M’s market by encouraging entry and imitation in M’s market, and (b) P is uncorrelated with M’s consumer demand because of not overlapping in the markets.<sup>16</sup> Considering that our outcome variable is the rival’s consumer demand, the above explanation justifies the exclusion criteria. A similar approach has been previously used to identify external instruments (Fan 2013, Karanam et al. 2020).

We use the volatility of the market demand to calculate market dynamism (see Xue et al. 2011). We obtain market demand volatility using a two-step approach. First, we regress the natural logarithm of market total demand against an index variable of months, over a period of six months. Second, we compute the antilog of the standard error of the regression coefficient. The antilog is the measure of market dynamism as it estimates the unpredictability of market demand growth. We use the natural logarithm of the reciprocal of the Herfindahl-Hirschman Index to measure market complexity. Finally, we calculate market growth using the natural logarithm of market total demand growth. Because we do not have downloads, we use the number of reviews as a proxy of consumer demand (see Foerderer et al. 2018).

Figure 2. Marginal Probability of MAJOR UPDATE  
![](/api/attachments/FSUP5W7C/fulltext/images/420b851752726e694133fff85b39e1146008ae6e10f49e44b4db831402342277.jpg)

We use two-stage least squares in our identification strategy. In the first stage, we regress the endogenous variables using the instruments and control variables (see Online Appendix Q for results of the first stage). In the second stage, we use the predicted value of the endogenous variables to investigate the mediations.

The Cragg-Donald Wald F statistics of Model 2, Model 3, and Model 4 (see Table 3) are above 30 (specifically, 1,027.298, 38.178, and 339.017, respectively), thus indicating that our instruments are not weak. Additionally, the Sargan-Hansen J-statistics are 0.159 $( p = 0 . 6 8 9 8 ) .$ 0.089 (p � 0.7652), and 0.169 (p � 0.6811). In all three cases, the results do not reject the overidentification restriction.

Baron and Kenny’s (1986) three-step mediation analysis procedure shows empirical support for the indirect spillover effect. The first step consists of estimating the effect of AFTER × OPENNESS on REVIEWSDIFF. Model 1 of Table 3 indicates that such an effect is positive and significant $( \beta = 0 . 0 1 2 1 , p < 0 . 0 0 1 )$ ). In the second step, we assess the effect of the mediators on REVIEWSDIFF.

Table 3. Effect of FPA’s Openness on Rivals’ ReviewsDiff

<table><tr><td rowspan="2"></td><td colspan="5">ReviewsDiff</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td>After × Openness</td><td>0.0121***(0.0030)</td><td>0.0073**(0.0024)</td><td>0.0051*(0.0023)</td><td>0.0027(0.0024)</td><td>0.0007(0.0022)</td></tr><tr><td>SameMarketAlternativesDiff</td><td></td><td>-0.5501**(0.1803)</td><td>-0.5954**(0.1871)</td><td></td><td>-0.5582**(0.1863)</td></tr><tr><td>OtherMarketAlternativesDiff</td><td></td><td></td><td>0.1553*(0.0759)</td><td></td><td>0.1501*(0.0736)</td></tr><tr><td>SameMarketAlternatives</td><td></td><td>-0.1312***(0.0314)</td><td></td><td>-0.1521***(0.0361)</td><td>-0.0332**(0.0116)</td></tr><tr><td>OtherMarketAlternatives</td><td></td><td></td><td></td><td>0.0572**(0.0183)</td><td>0.0313***(0.0084)</td></tr><tr><td>Constant</td><td>-0.0179(0.0215)</td><td>0.5001***(0.1241)</td><td>-0.0744(0.0527)</td><td>0.4951***(0.1241)</td><td>-0.0327(0.0598)</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>231,042</td><td>231,042</td><td>231,042</td><td>231,042</td><td>231,042</td></tr><tr><td>N of groups</td><td>15,418</td><td>15,418</td><td>15,418</td><td>15,418</td><td>15,418</td></tr><tr><td> $R^2$ </td><td>0.0021</td><td>0.0030</td><td>0.0031</td><td>0.0032</td><td>0.0034</td></tr></table>

Notes. Estimator � fixed effects with robust standard errors, that is, standard errors clustered by app. We control for the number of months sinc the last major update and the number of alternatives that are incumbent or exiting. Ninety-five percent confidence intervals are included <sup>+</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Figure 3. Instruments  
![](/api/attachments/FSUP5W7C/fulltext/images/90fa9bb3837fbcfb75ff474c8e9dd156c1d6c5b71c786f8670ee38a3c2795e96.jpg)

The results of the second step are presented in Model 5 of Table 3. The coefficients of SAMEMARKETAL-TERNATIVES and SAMEMARKETALTERNATIVES-DIFF are significant and negative. An increase of SAME-MARKETALTERNATIVES and SAMEMARKETALTER-NATIVESDIFF creates a situation of intense competition leading to a reduction of REVIEWSDIFF (β � �0.0332, p < 0.01, and β � �0.5582, p < 0.01). However, an increase of OTHERMARKETALTERNATIVES and OTHERMAR-KETALTERNATIVESDIFF increases REVIEWSDIFF (β � 0.0313, p < 0.001, and β � 0.1501, p < 0.05). Compared with same-market alternatives, other-market alternatives do not exercise high competition pressure on the focal TPA. This is consistent with prior literature which suggests that the number and differentiation of alternatives increase rivals’ consumer demand except when competition is intense, in which case the number and differentiation of alternatives may negatively affect rivals’ consumer demand (Boudreau 2012).

In the third step, we assess the effect of AFTER × OPENNESS on the mediators. Models 2 and 4 of Table 4 show that AFTER × OPENNESS increases OTHERMAR-KETALTERNATIVES and OTHERMARKETALTERNA-TIVESDIFF $( \beta = 0 . 0 3 0 7 , p < 0 . 0 0 1$ , and $\beta = 0 . 0 0 1 6 , p <$ 0.001). Moreover, Models 1 and 3 of Table 4 indicate that AFTER × OPENNESS increases SAMEMARKET-ALTERNATIVES and decreases SAMEMARKETALTER-NATIVESDIFF (β � 0.0381, p < 0.001, and $\beta = - 0 . 0 0 4 4 ,$ p < 0.001). The overall result from the three-step mediation reveals a mediation of the effect of AFTER × OPENNESS on REVIEWSDIFF via OTHERMARKET ALTERNATIVES, OTHERMARKETALTERNATIVES DIFF, SAMEMARKETALTERNATIVES, and SAME-MARKETALTERNATIVESDIFF, which is supported by the Sobel (statistic � 3.7251, p < 0.001; statistic � 2.0230, p < 0.05; statistic � �2.8613, p < 0.01; statistic � 2.9893, p < 0.01, respectively) test. We can conclude that the direct spillover is absent and the indirect spillover is present as the mediation is a full mediation (i.e., the direct effect is not significant after controlling for the monthly number and differentiation of alternatives). Online Appendix T summarizes the testing of the proposed mechanisms.

3.5.4. Heterogeneous Treatment Effects. Our main findings suggest that the release of the Apple Health Records API drives rivals’ innovation. Following prior research that suggests that capable and resourceful developers are less likely to be threatened by FPAs actions, but rather are more likely to be motivated to innovate (Foerderer et al. 2018), we investigate the mod erating effects of developer portfolio size and diversification. Developer portfolio diversification and size are measured using the number of categories wherein the developer has published apps before the release of the FPA’s API, and the number of apps published by the developer before the release of the FPA’s API. Simi lar measures have been used in Foerderer et al. (2018).

We split the sample into three quantile groups based on developer portfolio diversification (low, medium, high), and developer portfolio size (low, medium, high). In Table 5, we report split sample analyses contrasting low and high quantiles. Consistent with prior research, the positive effect of AFTER × OPENNESS on MAJOR UPDATE is higher for more developers with greater portfolio size and diversification (β\_LowSize � 0.0022 and β\_HighSize � 0.0045, β\_LowDiv � 0.0028 and β\_HighDiv � 0.0049). Moreover, the positive effect of REVIEWSDIFF on MAJOR UPDATE is greater for developers with greater portfolio size and diversification (β\_LowSize � 0.0217 and β\_HighSize � 0.0253, β\_LowDiv � 0.0281 and β\_HighDiv � 0.0288).

Table 4. Effect of FPA’s Openness on Alternatives

<table><tr><td rowspan="2"></td><td colspan="2">Market alternatives</td><td colspan="2">Market alternatives diff</td></tr><tr><td>Model 1 (same)</td><td>Model 2 (other)</td><td>Model 3 (same)</td><td>Model 4 (other)</td></tr><tr><td>After × Openness</td><td>0.0381***(0.0003)</td><td>0.0307***(0.0002)</td><td>-0.0044***(0.0001)</td><td>0.0016***(0.0001)</td></tr><tr><td>Constant</td><td>4.6602***(0.0015)</td><td>4.9102***(0.0013)</td><td>-0.2536***(0.0004)</td><td>-0.2601***(0.0009)</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>231,042</td><td>231,042</td><td>231,042</td><td>231,042</td></tr><tr><td>N of groups</td><td>15,418</td><td>15,418</td><td>15,418</td><td>15,418</td></tr><tr><td> $R^2$ </td><td>0.9982</td><td>0.9963</td><td>0.9474</td><td>0.7783</td></tr></table>

Notes. Estimator � fixed effects with robust standard errors, that is, standard errors clustered by app. We control for the number of months since the last major update and the number of alternatives that are incumbent or exiting. Ninety-five percent confidence intervals are included $^ { + } p < 0 . 1 ; ^ { ' * } p < ^ { \cdot } 0 . 0 5 ; ^ { * * } p < 0 . 0 1 ; ^ { * * * } p < 0 . 0 0 1 .$

Table 5. Moderating Effect of Developer Portfolio Diversification and Size

<table><tr><td rowspan="2"></td><td colspan="4">Major update</td></tr><tr><td>Low dev. diver.</td><td>High dev. diver.</td><td>Low dev. size</td><td>High dev. size</td></tr><tr><td>After × Openness</td><td>0.0028(0.0017)</td><td> $0.0049^{+}$ (0.0025)</td><td>0.0022(0.0026)</td><td> $0.0045^{*}$ (0.0019)</td></tr><tr><td>ReviewsDiff</td><td> $0.0281^{**}$ (0.0095)</td><td> $0.0288^{*}$ (0.0129)</td><td> $0.0217^{+}$ (0.0113)</td><td> $0.0253^{*}$ (0.0123)</td></tr><tr><td>RatingDiff</td><td>-0.0005(0.0014)</td><td>-0.0012(0.0021)</td><td>0.0006(0.0022)</td><td>-0.0002(0.0023)</td></tr><tr><td>Constant</td><td>-0.0151(0.0143)</td><td> $-0.0537^{*}$ (0.0271)</td><td>-0.0225(0.0235)</td><td>-0.0192(0.0129)</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>120,782</td><td>68,428</td><td>83,828</td><td>71,154</td></tr><tr><td>N of groups</td><td>8,706</td><td>4,926</td><td>6,048</td><td>5,098</td></tr><tr><td> $R^2$ </td><td>0.0013</td><td>0.0031</td><td>0.0014</td><td>0.0041</td></tr></table>

Notes. Estimator � fixed effects with robust standard errors, that is, standard errors clustered by app. We control for the number of alternatives that are incumbent or exiting. Ninety-five percent confidence intervals are included. Dev., developer; Diver., diversity. <sup>+</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

## 3.6. Robustness Checks

We conducted a battery of analyses, and all indicate that our findings are robust. First, we ran sensitivity checks using four months in the prerelease and postrelease periods (Online Appendix E). Second, we used an alternative matching algorithm (i.e., coarsened exact matching (Online Appendix F)) and distance metric (i.e., Mahalonis distance (Online Appendix G)). Third, we adopted an alternative measure of similarity (Online Appendix H). Fourth, we changed how we determine major and minor app updates by using the app version number instead of the similarity score (Online Appendix N). Fifth, we tested DiD assumptions using a continuous time trend variable (Online Appendix I) and relative time models (Online Appendix J). Sixth, we ruled out rival explanations by creating a placebo treatment group (Online Appendix K-1) and a fake exogenous shock (Online Appendix K-2). Seventh, we conducted an alternative remedy to selfselection bias based on the Heckman approach (see Online Appendix P). Eighth, we controlled for the characteristics (e.g., number of reviews, ratings, updates) of sharing TPAs as they may influence rivals (e.g., mediators (consumer demand and ratings) and outcome (updates)) (see Online Appendix O). Ninth, we tested whether publicly accessible knowledge about integrating FPAs’ open resources could cause product expansion (see Online Appendix M). Tenth, we controlled for app downloads and revenues (see Online Appendix L) and used two alternative research designs (see Online Appendices R and S).

## 4. Discussion

## 4.1. Theoretical Contributions

This study contributes significantly to the platform literature. Specifically, we articulate our key contributions to the prior literature on platform entry by contrasting an FPA with closed resources and an FPA with open resources (see Online Appendices U and V). Notably, our study is the first to explicitly test for both competitiveness enhancement and positive market growth as FPAs can open their resources to TPAs in the market. Moreover, we distinguish between direct and indirect spillover effects. Direct and indirect spillovers have not been discussed before as two potential explanations to explain the impact of FPA on rivals’ innovation, as the focus of previous research has been on FPAs with closed resources. It is important to note that the spillover effect has been discussed before (Foerderer et al. 2018). However, we argue and demonstrate that spillover has different origins when FPA has open resources by focusing on the type of consumers who join the market. For example, in contrast to Foerderer et al. (2018), we show that rivals are better at attracting consumers who join the market because of complementary offerings through alternatives. This is not the case for consumers who join the market because of improved experiences through TPAs that adopt FPAs open resources, as rivals find it difficult to attract this type of consumer. Hence, we enrich the platform entry literature by unraveling new explanations.

We make three key contributions to the platform openness literature (see Online Appendix W). First, we identify key mechanisms that underline the effects of FPAs’ openness on rivals’ innovation, presenting a more balanced approach, as there is disproportionate attention on competitiveness enhancement in previous research (see Online Appendix W). Presenting a more comprehensive assessment, we highlight both the negative and positive effects that manifest through competitiveness-enhancement and positive market growth mechanisms, respectively. Second, our research goes beyond TPAs’ interdependencies with platform APIs as we are exploring rivals. Studies on the impact of openness do not focus on rivals. For example, prior research on the impact of openness on TPAs’ supplyside outcomes such as imitation (Xue et al. 2019) and the quantity of innovation (Ye and Kankanhalli 2018) focuses only on sharing TPAs. Focusing on rivals is a significant contribution because it allows us to disentangle the competitiveness-enhancement and positive market growth mechanisms. Third, prior research on platform openness focuses on platform-level openness between TPAs and the platform (Eisenmann et al. 2009). As the platform opens itself to TPAs, it does not engage in competition with TPAs. Examples of platform-level openness include toolkits released by platform owners to facilitate third-party development. Contrary to platform-level openness, FPAs’ openness does not exclude rivalry between FPA and TPAs. Hence, the TPAs’ motives for not integrating open resources are different between platform-level and FPAlevel openness, implying that the impact on TPAs differs as well.

## 4.2. Practical Implications

Our findings have important managerial implications for platform owners and third-party developers in platform ecosystems. This study might inform platform owners about possible actions to take considering the impact of FPAs’ openness on rivals’ supply-side outcomes. As FPAs’ openness lowers same-market alternatives’ differentiation, platform owners might provide incentives to attract same-market alternatives that are novel, for example, through contests. Moreover, innovation-enhancing activities such as conferences (e.g., Apple’s Worldwide Developers Conference) might be an appropriate thing to offer as FPAs engage in openness initiatives, to increase innovation rather than imitation. Our study recommends FPAs’ openness initiatives because they are crucial for the evolvability of the ecosystem. Moreover, whether rivals are created by capable and resourceful app developers is an important factor to consider. Rivals realize greater benefits from FPAs’ openness when they are created by capable and resourceful app developers. Thus, our study indicates that app developers who seek to benefit from free-riding may need to take into account their capabilities and resources for innovation.

## 4.3. Limitations and Future Research

Our study has several limitations. First, to have focused empirical estimations, we limit our treatment group to medication management TPAs. Other relevant groups include TPAs on allergies, conditions, immunizations, laboratory results, procedures, and vitals. Future studies might extend our findings by investigating these other types of health records. Second, following prior literature (Foerderer et al. 2018, Foerderer 2020), we focus on the supply-side outcomes (e.g., app updates). Future research might extend our study by investigating other outcomes. For example, studies can highlight the financial performance of rivals, focusing on the costs incurred and revenues generated by rivals.

Third, this study focuses on the short-term impacts of FPAs’ openness on rivals’ innovation. Modeling the long-term impacts of FPAs’ openness on rivals’ innovation requires different models and assumptions. We propose that future studies might use longer panel data to assess the long-term impacts while ruling out any alternate explanations. Fourth, our study suffers from a common limitation of studies examining consumer attention or demand as we use the monthly difference in the number of reviews to measure positive market growth (Foerderer et al. 2018). Although this proxy is widely accepted by scholars, we propose that future research attempt to collect primary data about consumer engagement or usage. Finally, we are unable to directly measure some variables (e.g., improved experience and better customization) that are discussed in our theoretical arguments. Because of this, we cannot provide direct empirical support for these variables. Future research may address this issue.

## Endnotes

<sup>1</sup> In the platform ecosystem, TPAs are apps created by complementors (also called third-party developers).

<sup>7</sup> In other words, any other rival that joins the same market is an alternative.

<sup>8</sup> In the example of the medication management TPA, it means that the number and differentiation of alternatives whose secondary market is medication management increase the TPA’s consumer demand whereas the number and differentiation of alternatives whose primary market is medication management decrease the TPA’s consumer demand.

<sup>9</sup> We suggest that resource sharing between an FPA and TPAs is similar to an alliance. Indeed, an alliance is an economic organization that facilitates resource sharing between participants (Han et al. 2012).

<sup>10</sup> For example, the Apple Health Records app becomes more competitive as it can seamlessly integrate with TPAs (e.g., the Medisafe app) after opening its data (i.e., health records).

<sup>11</sup> The interest in resource sharing between the platform and thirdparty developers took off as openness emerged as a key pillar of digital platforms in late 2000 (De Reuver et al. 2018). Early studies investigated the benefits that may accrue to third-party developers to better understand the growing popularity of resource sharing. For example, Bou dreau (2010) indicates that third-party developers have various motives for integrating the platform’s shared resources. Specifically, third-party developers can access specialized resources (i.e., the platform’s shared IP) and benefit from agglomeration economies. Early works such as Boudreau (2010) were mostly exploratory as they did not empirically disentangle the mechanisms but suggested their existence, and the studies that came out later did not focus on rivals, rendering the distinc tion of the mechanisms challenging (see Online Appendix W).

<sup>12</sup> Direct spillover focuses on consumers who join the market because they seek improved experiences (i.e., more customization) in TPAs. In our study, this happens mostly as existing TPAs (e.g., Medisafe) integrate FPAs’ open resources. Because of that, we choose not to discuss the generativity effect in the direct spillover as the focus of the generativity effect is on product expansion (i.e., creation of new TPAs) whereas the focus of the direct spillover is on improved experiences, which, in our study, happen mostly through existing TPAs (probably because platform owners emphasized improvement of existing apps rather than creation of new apps dur ing the launch event of FPAs’ open resources).

<sup>13</sup> The network effect discussed in Boudreau (2012) is the same as the generativity effect as the idea is the same, that is, product expansion increases user base growth.

<sup>14</sup> App markets are not boundless frontiers, and there is scope for the generativity effect to cause intense competition, especially in mature markets (i.e., markets with market-proven concepts). For example, competition can get intense as it might be simpler for TPAs to copy, vary, or recombine proven concepts in the market. Moreover, an extremely high number of TPAs may create congestion of TPAs, impairing consumers’ ability to make informed deci sions (Simonsohn 2010, Tucker and Zhang 2010).

<sup>15</sup> “Generativity refers to the capacity of a platform to enable unbounded growth of new components that expand the product boundaries of a platform beyond its initial conception and further attract more users” (Fu¨ rstenau et al. 2023, p. 1688).

<sup>16</sup> The logic is that when P experiences a growth in consumer demand, developers will focus on entering P’s market. Because P is M’s closest market, we are likely to observe less entry and imitation in M’s market. In the same way, when P experiences uncertainty because of high complexity and dynamism, developers are more likely to enter other markets. Because P is M’s closest market, we are likely to observe more entry and imitation in M’s market.

## References

Aghion P, Griffith R (2008) Competition and Growth: Reconciling Theory and Evidence (MIT Press, Cambridge, MA).

Apple (2018a) Apple announces effortless solution bringing health records to iPhone. Retrieved November 30, 2021, https://www. apple.com/newsroom/2018/01/apple-announces-effortless-solutionbringing-health-records-to-iPhone/.

Apple (2018b) Apple opens Health Records API to developers. Retrieved November 30, 2021, https://www.apple.com/newsroom/2018/06 apple-opens-health-records-api-to-developers/.

Baldwin C, Clark K (2000) Design Rules: The Power of Modularity (MIT Press, Cambridge, MA).

Baron R, Kenny D (1986) The moderator–mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. J. Personality Soc. Psych. 51(6):1173–1182.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10):1849–1872.

Boudreau K (2012) Let a thousand flowers bloom? An early look at large numbers of software app developers and patterns of innovation. Organ. Sci. 23(5):1409–1427.

Chesbrough HW (2006) Open Business Models: How to Thrive in the New Innovation Landscape (Harvard Business School Press, Boston).

De Reuver M, Sørensen C, Basole RC (2018) The digital platform: A research agenda. J. Inform. Tech. 33(2):124–135.

Eisenmann T, Parker G, Van Alstyne MW (2009) Opening platforms: How, when and why? Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar Publishing, Cheltenham, UK), 131–162.

Fan Y (2013) Ownership consolidation and product characteristics: A study of the US daily newspaper market. Amer. Econom. Rev. 103(5):1598–1628.

Foerderer J (2020) Interfirm exchange and innovation in platform ecosystems: Evidence from Apple’s Worldwide Developers Conference. Management Sci. 66(10):4772–4787.

Foerderer J, Kude T, Mithas S, Heinzl A (2018) Does platform owner’s entry crowd out innovation? Evidence from Google Photos. Inform. Systems Res. 29(2):444–460.

Fu¨ rstenau D, Baiyere A, Schewina K, Schulte-Althoff M, Rothe H (2023) Extended generativity theory on digital platforms. Inform. Systems Res. 34(4):1686–1710.

Han K, Oh W, Im KS, Chang RM, Oh H, Pinsonneault A (2012) Value cocreation and wealth spillover in open innovation alliances. MIS Quart. 36(1):291–315.

He S, Peng J, Li J, Xu L (2020) Impact of platform owner’s entry on third-party stores. Inform. Systems Res. 31(4):1467–1484.

Huang H, Parker G, Tan Y, Xu H (2020) Altruism or shrewd business? Implications of technology openness on innovations and competition. MIS Quart. 44(3):1049–1071.

Inkpen A, Dinur A (1998) Knowledge management processes and international joint ventures. Organ. Sci. 9(4):454–468.

Kang Y, Suarez F (2022) Platform owner entry into complementor spaces under different governance modes. J. Management 49(5): 1766–1800.

Karanam A, Agarwal A, Barua A (2020) Designing for visibility The case of mobile apps. Preprint, submitted June 18, http://dx. doi.org/10.2139/ssrn.3635854.

Karhu K, Gustafsson R, Lyytinen K (2018) Exploiting and defending open digital platforms with boundary resources: Android’s five platform forks. Inform. Systems Res. 29(2):479–497.

Khanna T, Gulati R, Nohria N (1998) The dynamics of learning alliances: Competition, cooperation, and relative scope. Strategic Management J. 19(3):193–210.

Lane P, Lubatkin M (1998) Relative absorptive capacity and interorganizational learning. Strategic Management J. 19(5):461–477.

Leyden BT (2022) There’s an app (update) for that: Understanding product updating under digitization. Working paper, Cornell University, Ithaca, NY.

Li Z, Agarwal A (2017) Platform integration and demand spillovers in complementary markets: Evidence from Facebook’s integra tion of Instagram. Management Sci. 63(10):3438–3458.

Liu CZ, Au YA, Choi HS (2014) Effects of freemium strategy in the mobile app market: An empirical study of Google Play. J. Man agement Inform. Systems 31(3):326–354.

Nakamura M, Shaver J, Yeung B (1996) An empirical investigation of joint venture dynamics: Evidence from US-Japan joint ven tures. Internat. J. Indust. Organ. 14(4):521–541.

Ondrus J, Gannamaneni A, Lyytinen K (2015) The impact of openness on the market potential of multi-sided platforms: A case study of mobile payment platforms. J. Inform. Tech. 30(3):260–275.

Oxley JE, Sampson RC, Silverman BS (2009) Arms race or de´tente? How interfirm alliance announcements change the stock market valuation of rivals. Management Sci. 55(8):1321–1337.

Pan Y, Huang P, Gopal A (2019) Storm clouds on the horizon? New entry threats and R&D investments in the U.S. IT industry. Inform. Systems Res. 30(2):540–562.

Simonsohn U (2010) eBay’s crowded evenings: Competition neglect in market entry decisions. Management Sci. 56(7):1060–1073.

Teece D (1992) Competition, cooperation, and innovation: Organiza tional arrangements for regimes of rapid technological pro gress. J. Econom. Behav. Organ. 18(1):1–25.

Tucker C, Zhang J (2010) Growing two-sided networks by advertising the user base: A field experiment. Marketing Sci. 29(5): 805–814.

Wen W, Zhu F (2019) Threat of platform-owner entry and complementor responses: Evidence from the mobile app market. Strategic Management J. 40(9):1336–1367.

Xue L, Ray G, Gu B (2011) Environmental uncertainty and IT infrastructure governance: A curvilinear relationship. Inform. System Res. 22(2):389–399.

Xue L, Song P, Rai A, Zhang C, Zhao X (2019) Implications of applica tion programming interfaces for third-party new app development and copycatting. Production Oper. Management 28(8):1887–1902.

Ye H, Kankanhalli A (2018) User service innovation on mobile phone platforms: Investigating impacts of lead userness, toolkit support, and design autonomy. MIS Quart. 42(1):165–187.

Yoo Y, Lyytinen K, Boland R, Berente N (2010) The next wave of digital innovation: Opportunities and challenges: A report on the research workshop ‘Digital Challenges in Innovation Research’. Preprint, submitted June 8, http://dx.doi.org/10 2139/ssrn.1622170.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
