---
otero_id: 26538
otero_key: "5RTJC5TK"
title: "Motivating Effective Mobile App Adoptions: Evidence from a Large-Scale Randomized Field Experiment"
authors: "Tianshu Sun; Lanfei Shi; Siva Viswanathan; Elena Zheleva"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0815"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [131.172.36.29] On: 26 May 2019, At: 20:51 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

Information Systems Research  
![](/api/attachments/5RTJC5TK/fulltext/images/78abfda69d7bb373c7d9e12a957dd464f65cc2ca4697c34fac7b1b1d7a31b2fd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Motivating Effective Mobile App Adoptions: Evidence from a Large-Scale Randomized Field Experiment

Tianshu Sun, Lanfei Shi, Siva Viswanathan, Elena Zheleva

To cite this article: Tianshu Sun, Lanfei Shi, Siva Viswanathan, Elena Zheleva (2019) Motivating Effective Mobile App Adoptions: Evidence from a Large-Scale Randomized Field Experiment. Information Systems Research

Published online in Articles in Advance 24 May 2019

https://doi.org/10.1287/isre.2018.0815

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Motivating Effective Mobile App Adoptions: Evidence from a Large-Scale Randomized Field Experiment

Tianshu Sun,<sup>a</sup> Lanfei Shi,<sup>b</sup> Siva Viswanathan,<sup>b</sup> Elena Zheleva<sup>c</sup>

<sup>a</sup> Marshall School of Business, University of Southern California, Los Angeles, California 90089; <sup>b</sup> Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20742; <sup>c</sup> Department of Computer Science, University of Illinois at Chicago, Chicago, Illinois 60607

Contact: tianshus@marshall.usc.edu, http://orcid.org/0000-0002-9786-044X (TS); lanfeishi@rhsmith.umd.edu (LS); sviswana@rhsmith.umd.edu, http://orcid.org/0000-0002-2730-0746 (SV); ezheleva@uic.edu (EZ)

Received: June 14, 2017 Revised: February 13, 2018; July 2, 2018 Accepted: July 28, 2018 Published Online in Articles in Advance: May 24, 2019

https://doi.org/10.1287/isre.2018.0815

Copyright: © 2019 INFORMS

Abstract. Prior literature has established a positive association between mobile app adoptions and customers’ purchase behaviors. However, it is not clear whether and how firms can actively influence customers’ mobile app adoptions and increase their purchases through these induced adoptions. Using a randomized field experiment involving over 230,000 customers, we investigate the differential impacts of offering incentives or information on customers’ mobile app adoptions and subsequent purchase behaviors. We find that (1) providing monetary incentives and providing information can both lead to a significant increase in mobile app adoptions and that (2) the causal effect of induced mobile app adoptions varies greatly depending on how customers are motivated. Al though providing monetary incentives leads to a larger increase in mobile app adoptions, such incentive-induced adoptions do not result in more purchases in the long run. In contrast, providing information leads to effective mobile adoptions that sustainably increase customers’ purchases and overall profits for the firm. In further examining customers’ multichannel purchase behaviors, we find that there is a complementary effect between the mobile app and the desktop channel for information-induced app adopters but a substitution effect between the mobile app and the mobile web channel for incentiveinduced app adopters. For information-induced app adopters, the mobile app serves as a discovery tool and helps them find a greater variety of deals. Finally, in exploring the underlying drivers of such differences in the effect of induced adoptions, we find that information compared with incentives serves as a better sorting device and can attract cus tomers who have a greater need for the app and use it more effectively. Our findings provide actionable insights to firms on designing interventions to motivate effective mobile adoptions.

History: Eric Zheng, Senior Editor; Wonseok Oh, Associate Editor. Funding: T. Sun acknowledges the support from Outlier Research Grant from USC Institute of Outlie Research for Business (iORB). Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2018.0815.

Keywords: mobile app • induced adoption • <sup>fi</sup>eld experiment • local average treatment effect • multichannel • online-to-of<sup>fl</sup>ine

## 1. Introduction

The adoption and usage of mobile channels have not only grown significantly but also, has altered users’ experience and behaviors in a multichannel world (Ghose et al. 2013, Luo et al. 2013, Einav et al. 2014, Fang et al. 2015, Shankar et al. 2016, Xu et al. 2016). According to Koetsier (2017), mobile commerce in the November-December 2017 holiday season was predicted to cross \$5 billion, accounting for 54% of retail business spending. Recognizing this disruptive effect, firms have been increasing their investments in mobile channels, with a strong emphasis on the promotion of their own mobile apps (Siwicki 2014, RetailMeNot 2016).

Prior literature has established a positive association between mobile app adoption and business outcomes using observational data. The adoption of mobile apps may lead customers to make more purchases (Xu et al. 2016), be more socially engaged (Jung et al. 2019), and consume more news (Xu et al. 2014). Given the value of mobile app adoptions, a natural question for the firms is whether such findings can be put into action. In other words, can firms actively influence customers to adopt mobile apps, and can such induced adoptions lead to an increase in customers’ purchases? Furthermore, how should firms induce such adoptions? Two interventions are commonly used by firms to encourage technology adoptions: providing information about the benefits of the technology (Guiteras et al. 2015) and providing incentives for adoption (Cohen et al. 2015). When choosing interventions, firms have two goals in mind: (1) to increase mobile app adoptions (“coverage”) and (2) to attract customers who need the app more and will use it more effectively (“sorting”). The ideal intervention is one that helps achieve high coverage (increased adoption) as well as appropriate sorting (effective adoption). However, it is possible that there are inherent tradeoffs between the two goals. Despite the huge stakes involved and an active debate about the best intervention strategy (Ohayon 2011, Miller 2014, Techcrunch 2015a), no empirical research has rigorously investigated this problem.

Our empirical study seeks to fill this gap. Specifically, our study addresses the following questions.

Q1a. (Coverage) What is the effect of incentive versus information on customers’ app adoptions?

Q1b. (Effectiveness) What is the causal effect of induced app adoptions on customers’ behaviors in the long run? Does the effect vary for adoptions induced by incentive versus information?

Q1c. (Profitability) What is the impact of incentive versus information on a firm’s overall profitability?

Q2. (Cross-Channel Effect) How do incentive- and information-induced app adoptions affect customers purchase behaviors across mobile and desktop channels?

Q3. (Mechanisms) What is the underlying driver of the differences between the causal effects of app adoptions induced by incentive versus information?

Answers to these questions are valuable, because they provide direct managerial implications and actionable insights to firms interested in designing active interventions to motivate effective mobile app adoptions and improve business outcomes.

It is pertinent to note that the prior studies on mobile channel adoptions have not examined the causal effect of induced mobile adoption (e.g., Q1b).<sup>1</sup> From a firm’s perspective, there are two types of mobile app adopters: (1) those who would adopt because of factors beyond the firm’s direct intervention, such as organic word-of-mouth (defined as “organic adopter”), and (2) those who would adopt the app only in response to the firm’s direct interventions (defined as “induced adopters”). Previous studies investigate the effect of observed mobile adoptions (i.e., a mix of “organic” and “induced” adopters) (Xu et al. 2016) rather than induced adoptions. As shown in various contexts, including technology adoption (Dupas 2014), customer acquisition (Datta et al. 2015), and multichannel purchases (Neslin and Shankar 2009, Montaguti et al. 2015), induced adopters may differ fundamentally from organic adopters in observed characteristics, such as demographics and historical behaviors. In addition, organic adopters of technology may use it in ways that are different from induced adopters, because the organic adoptions may be driven by unobserved needs or preferences. Such unobserved needs may also drive them to use the app in specific ways that would lead to more (or less) purchases. The same may not hold for customers who are nudged or incentivized to adopt the app. Consequently, it is not clear whether induced mobile adoptions would lead to desirable outcomes and be beneficial to the firms. Because the firms can only actively influence induced adoptions (rather than organic adoptions) using external interventions, it is crucial to understand the causal effect of induced adoptions on customers’ purchase behaviors. More interestingly, the effect of induced app adoptions may depend on how customers are motivated to adopt the app. Customers have private information about their need for the app (how and how often they use the app), and such unobserved “customer types” may determine their long-run behaviors. Different interventions may encourage different types of customers to adopt the app (sorting) and may lead to different customer behaviors and business outcomes in the long run. Therefore, it is important for firms to understand how the effect of app adoptions varies for customers induced by different interventions as well as the underlying mechanisms.

Identifying the causal effect of induced mobile app adoption (Q1b), although relevant and important, is empirical challenging for two reasons. First, just by using observational data on app adoptions, one cannot differentiate between organic adoptions and induced adoptions. Second, the effect of induced adoptions may be confounded by time-varying factors (e.g., concurrent marketing campaigns on adoption and purchase). Thus, without exogenous variations in the level of induced adoptions, it is extremely difficult to identify its causal effect on customers’ purchase behaviors.

To address these challenges, we collaborate with a leading daily deal platform in the United States and conduct a large-scale randomized field experiment to examine whether and how the firms can effectively induce app adoptions. We randomly choose over 230,000 customers who have never downloaded the firm’s mobile app and randomly assign eligible users into one of three experimental groups: Control group with no information or incentives, Treatment 1 (T1) with an email highlighting incentives for adoption (five deal bucks), and Treatment 2 (T2) with an email highlighting information about the benefits of discovering deals using mobile apps. The exogenous variation created by the experiment not only allows us to monitor the cohort of induced adopters over time and isolate the causal effect of app adoptions induced by the different interventions (Q1b) but also, facilitates a straightforward comparison of the effect of interventions on app adoptions and firm profitability (Q1a and Q1c). Specifically, we address Q1b (causal effect of induced app adoptions) using the framework of local average treatment effect (LATE; i.e., using a random assignment of the test group as an instrument for induced app adoptions) (Angrist et al. 1996).

Our experiment generates four main findings. First, both monetary incentives (T1) as well as information (T2) lead to a significant increase in customers’ mobile app adoptions, with relative increases of 466% and 144%, respectively. Second, although providing monetary incentives leads to a larger increase in mobile app adoptions, such induced adoptions do not result in more purchases in the long run. In contrast, providing information leads to more effective mobile adoptions that sustainably increase customers’ purchases, even 12 months after adopting the app. Third, in examining customers’ multichannel purchase behaviors (Q2), we find that information-induced adoptions (T2) lead to a complementarity in customers’ purchases across the mobile app and the desktop channel, whereas incentive-induced adoptions lead to a substitution effect between mobile web and mobile app channel. Fourth, we find that the information intervention (T2) can significantly increase overall profits of the firm (by 2%–3%). In contrast, providing incentives (T1) does not lead to a significant increase in overall profits.

We then explore the underlying drivers of the differences between the effect of app adoption induced by different interventions (Q3) using a new field experiment and a series of analysis. We uncover evidence that indicates that the observed long-run differences in customers’ purchase behaviors across incentive- and information-induced adopters are attributable to sorting. In accordance with our discussions of the underlying mechanisms (Section 3), we find evidence of sorting in customers’ observable characteristics and behaviors as well as in various moderating effects. Interestingly, after controlling for customers’ observable characteristics in LATE, the causal effect of induced adoptions for both treatments remains qualitatively the same, indicating that the effect of induced adoptions is largely attributable to sorting on characteristics unobservable by the firm. These findings are surprising and managerially important. They imply that customers possess private information about their “type” (i.e., their need for the mobile app) that firms are unable to observe. Therefore, firms need to rely on appropriate interventions to encourage sorting (i.e., attracting those customers who would use the mobile app effectively to adopt it).

In summary, our study is among the first to investigate how firms can induce effective app adoptions. The findings of the study provide guidelines for designing interventions to motivate app adoptions and add to our understanding of the mechanisms underlying the effect of induced app adoption (i.e., sorting). The rest of the paper proceeds as follows. Sections 2 and 3 briefly discuss related literature and theoretical grounding. Sections 4–6 introduce the experiment design, empirical strategy, and data. We present the results and discussions in Sections 7 and 8.

## 2. Related Literature and Contributions

There is a growing literature on the role of mobile devices in influencing customers’ engagement and purchase behaviors (Xu et al. 2014, 2016). Our study is closely related to three streams of research that span information systems and marketing among others.

The first and most relevant stream of literature is one that focuses on the causal effects of mobile app adoptions on customers’ engagement and purchase behaviors. Using propensity score matching, difference-in-difference, and other methods on observational data, previous studies have found that customers’ adoption of mobile apps can lead to more purchases (Xu et al. 2016), more social engagement (Jung et al. 2019), more consumption of news (Xu et al. 2014), and higher demand for digital service (Liu et al. 2016). However, from the firms’ perspective, natural questions are whether they can actively influence customers to adopt mobile apps and whether such induced adoptions can increase customers’ purchases and firms’ profits in the long run. Our study contributes to this research stream in two ways. First, previous studies focus on observed adoptions (Xu et al. 2016, Jung et al. 2019). Our study complements these by focusing on the causal effects of induced app adoptions on customers’ purchase behaviors. As noted earlier, induced adopters may differ from organic adopters in fundamental ways in mobile app usage. Because marketers can only actively influence induced adoptions, it is crucial to understand the causal effect of induced adoptions on customer behaviors and business outcomes. Our nuanced results also provide practical guidelines for firms designing interventions to motivate effective mobile adoptions. Second, our study extends previous research by de signing a new identification strategy. Specifically, the usage of a randomized field experiment allows us to cleanly identify the effect of different interventions in driving mobile app adoption (Q1a) and customer profitability (Q1c). The combination of a randomized experiment with an instrumental variable approach (LATE) allows us to isolate the causal effect of induced adoptions on customers’ purchase behaviors (Q1b) (see details in Section 5 and Figure 1).

The second important stream of research relates to factors that drive technology adoption (Dupas 2014, Hann et al. 2016), especially mobile app adoption (Bang et al. 2013, Ghose and Han 2014, Han et al. 2016, Zheng et al. 2016), as well as subsequent usage after adoption (Kato-Lin et al. 2015; Son et al. 2016; Retana et al. 2017, 2018). Although previous studies investigate the two outcomes separately, we highlight a central tradeoff between adoption and effective usage in the context of mobile apps. Our study is among the first to identify the causal effect of external interventions on the two outcomes at the same time. The results imply that firms should use information-related interventions to strike a balance between motivating more adoptions (coverage) and ensuring effectiveness of those adoptions (sorting).

Finally, our study also complements the stream of literature on the role of mobile apps in influencing customers’ purchase behaviors across multiple channels. Recent studies have shown strong interdependence between different channels in the form of substitution or complementarity (Brynjolfsson et al. 2009, Forman et al. 2009). The interdependence has also been confirmed in the context of mobile commerce (Xu et al. 2016) and digital banking (Liu et al. 2016). A recent study using clickstream data (De Haan et al. 2015) hypothesized that mobile and alternative channels may be used separately to fulfill different flows (e.g., information versus transaction) in a customer’s online journey. Our study complements this stream of literature with new evidence on the substitution/complementarity effects between mobile apps and alternate channels. Our analyses also provide new insights that such channel complementarity and substitution may be closely related to how customers are induced to adopt the app (i.e., sorting).

## 3. Theoretical Grounding: Mechanism Underlying the Effect of Induced Adoptions

In this section, we theorize the mechanism underlying the differentiate effect of incentive- and informationinduced adoption. The effects of monetary incentives and information on customers’ purchase behaviors in the short run and long run have been studied in marketing (Deighton et al. 1994, Ailawadi and Neslin 1998) and economics (Nelson 1974, Dupas 2014). In addition, a recent stream of literature has investigated how the use of monetary and nonmonetary incentives for customer acquisition may affect customers’ longterm value (Lewis 2006). A differentiating feature of our study is that, rather than directly influencing customers’ purchase behaviors, incentive or information is used to induce customers to sort (or self-select) into app adoption, and only such induced adoptions influence customers’ purchase behaviors in the long run. To the best of our knowledge, no study has investigated the mechanism underlying such process.

Sorting has its origins in information economics (Stiglitz 1975, Lazear 2000), and it refers to the fact that individuals (job applicants, patients, and customers) could choose certain arrangements (e.g., labor contract, health insurance, and technology adoption) based on their observable attributes and unobservable preferences or information. In our context, customers could have private information on the potential benefits that they can derive from using the app (how and how often). Customers who are induced by information to adopt the app could be different from customers induced by incentive in both their observed characteristics (e.g., preadoption behaviors) as well as unobservable need (e.g., deal discovery). Such observed and unobserved differences would then explain the differential effect of incentive- and information-induced adoptions on customers’ purchase behaviors.

Specifically, previous literature on technology adoption has shown that the provision of incentives may act as a double-edged sword. On the one hand, providing incentives may encourage more trials (Cohen and Dupas 2010) and facilitate habit formation (Charness and Gneezy 2009), thus increasing the effect of technology adoption; on the other hand, the use of short-run incentives may encourage adverse selection—attracting those who will not use or do not need the technology (Ashraf et al. 2010), thus countering the effects of adoption in the long run. Such tradeoff is especially salient in the case of mobile app adoptions. On the one hand, a mobile app is fundamentally an experience good; providing incentives may help customers overcome the fixed cost of downloading the app, setting up payments, and learning. On the other hand, continuous use, rather than one-time adoption, of the app is required to drive purchases and increase the firm’s overall profitability; providing incentives may attract customers who only enjoy short-run incentive and will not use the app in the long run (adverse selection).

In contrast, providing information about the benefits of the mobile app may attract the right type of customers (whose needs are aligned with the benefits provided by the app) and thus, may lead to effective adoptions: information-induced adopters are likely to use the app more, thereby benefiting more from their adoption. Such differences exist from the time of adoption and would lead to different usage patterns and purchase behaviors in the long run.

Overall, there are two types of sorting: sorting on observables and sorting on unobservables (Lazear 2000). Both processes may be at work at the same time. For instance, relating to sorting on observable behaviors or characteristics, providing monetary incentives (T1) may attract those customers who are more sensitive to in centives; and such adoption might only lead to short-run increase on customers’ purchases in first few weeks but may disappear afterward. Relating to sorting on unobservables, app adoptions induced by information (T2) could attract customers who download mobile app for its own value (e.g., convenience in deal browsing). Thus, those induced adopters are more likely to use the mobile app more in the long run, discover more deals, and make more purchases (and in a wider range of deal categories). The above discussions lead to several testable implications. The first two are related to sorting on observable characteristics and behaviors, whereas the latter three are related to sorting on unobserved needs for the app.

1. Adopters in the different treatment groups may differ in their observable characteristics.

2. Adopters in T1 (incentive) are more likely to make purchases through the mobile app in the short run, but the effect disappears in the long run (e.g., after few weeks).

3. After controlling for all differences in observable characteristics, the causal effect of induced adoptions by both treatments still follows a similar pattern, indicating sorting on unobservable.

4. Information-induced adopters (T2) are likely to use the app more and discover more deals, which may lead to a greater variety of deal purchases and more purchases in cities with more deals.

5. Information intervention (T2) does not directly affect customers’ purchases in the long run (it only works by attracting the right type of adopters with a strong need for the app; i.e., sorting).

In summary, we theorize that the effect of induced app adoptions may crucially depend on how customers are induced because of sorting. Incentive and information may attract adopters with different observed and unobserved characteristics, which would then result in differential effects of induced adoptions. We test the implications and further discuss sorting<sup>3</sup> in Section 7.

## 4. Experiment Design

In collaboration with a leading daily deal platform in the United States, we conduct a large-scale randomized field experiment to understand how to motivate effective mobile app adoptions. The platform offers a wide range of daily deals for local services and standard products at a high discount and has a large customer base. Users can use three channels (desktop, mobile web, and mobile app) to browse and purchase deals on the platform. The platform offers a mobile app to its customers. However, at the time of our experiment, only a small portion of the customers had downloaded the mobile app, although a much larger portion of customers has accessed the platform’s email using their mobile device. The platform observes the customers’ mobile device type and app adoption status, and it can target them with information or incentives through email.

Our experiment focuses on customers who (1) have already accessed emails of the platform using an iPhone but have never downloaded its mobile app and (2) have made at least one purchase before the experiment.<sup>4</sup> In practice, such customers are the target audience of mobile app adoption campaigns (DigiDay 2016). We randomly select over 230,000 eligible customers from the platform’s database and randomly assign them into one of the three test groups: (1) Control group with no information or incentives (137,195 subjects), (2) T1 with an email highlighting an incentive (five deal bucks) for app adoption (48,027 subjects), and (3) T2 with an email that highlights information about the ease of discovering deals using the app but that does not contain any incentive for app adoption (48,070 subjects). The template is provided in Figure 2. The sample size of both treatment groups is smaller than that the control group because of the relatively large costs involved in sending out emails and incentives.

The emails to the 96,097 customers in T1 and T2 ar sent out in a single day at the same time. The large-scale campaign allows us to create a large and exogenous shock in the number of induced adoptions within a very short period (i.e., within few days as discussed in Section 7). Customers in the treatment groups receive the email only once during the test period and can click a link to download the app. Customers in incentive treatment (T1) are informed that they will automatically get five deal bucks after they download and log in to the mobile app. The email for T1 also states that (1) the offer to get the deal bucks will expire in a week and that (2) the deal bucks can be used in a deal purchas and would expire in two weeks on assignment. We also designed other aspects of the experiment very carefully. First, we strictly control spillovers across different test groups. Specifically, all of the incentive/ information is provided only through the email channel; thus, customers cannot participate in the campaign through alternative channels. In addition, the five dea bucks incentive is automatically tied to the account identification of the customers in T1; thus, other cus tomers outside T1 are not eligible for the incentive Second, after customers in different groups adopt the app (Control, T1, and T2), they will have exactly the same experience and receive the same information in their mobile app. This ensures that any difference in their future behaviors can be attributed to how they are induced to adopt the app in the first place. The interventions used in the field experiment are common in dustry practice and used by other ecommerce platforms in their email campaigns. For instance, major platforms, such as Amazon and Groupon, have offered monetary incentive (\$5 or \$10 credit) for app adoptions in his torical campaigns, and they have also promoted apps regularly using informational email (Dedman 2011, Techcrunch 2015b). Thus, the external validity of our interventions is assured, and our findings may be generalizable to other settings.

## 5. Empirical Strategy: Identifying the Causal Effect of Induced App Adoptions

With the field experiment, we seek to understand three types of causal effects: (1) the effect of the two treatments (T1: incentive and T2: information) on customers app adoption decisions (Q1a), (2) the differential effect of incentive- and information-induced adoptions on customers’ purchase behaviors (Q1b; LATE), and (3) the

Figure 1. (Color online) Relationship Between Effect of Treatment on Adoption, Effect of Induced Adoptions on Purchases (LATE), and Effect of Treatment on Purchases (ITT)

![](/api/attachments/5RTJC5TK/fulltext/images/42a2251934fba1b25bc0b54044962d5737c0c0efd4de5c1bd670e41bb959e14a.jpg)  
Notes. The three effects correspond to Q1a–Q1c in Section 1. App adoption consists of organic adoptions (solid part) and induced adoptions (dotted part in T1 or dashed part in T2). The “induced adoptions” are influenced by firm’s specific interventions. We use the LATE approach to identify the causal effect of such induced adoptions on customers’ purchase behaviors (Q2) for both incentive treatment (T1) and information treatment (T2).

effect of the two treatments on overall profitability (Q1c; intention-to-treat effect (ITT)). The relationship between the three types of causal effects (adoption, LATE, and ITT) is illustrated in Figure 1. They correspond to Q1a–Q1c highlighted earlier. Specifically, we answer Q1a and Q1c through direct comparisons between test groups and address Q1b using the LATE framework (Imbens and Angrist 1994) (i.e., using the random assignment of the test group as an instrument for induced adoptions). The identification of causal effects in Q1a and Q1c is straightforward, with specifications in Equations (2) and (3) in Section 7; therefore, we focus our discussions on the motivation and intuition behind the LATE approach in identifying the causal effect of induced app adoptions (Q1b).

## LATE Approach—Motivation

An interesting aspect of motivating mobile app adoption is that only a small portion of users would ever be induced to adopt the mobile app.<sup>5</sup> However, these are exactly the users that firms can influence through external interventions. Thus, identifying the causal effect of mobile app adoptions for this population of induced adopters is important for firms. As discussed in Section 1, it is challenging to use observational data to isolate the causal effect of induced app adoptions. First, one cannot differentiate the induced adoptions from organic adoptions in observational data, and furthermore, one cannot distinguish different types of induced adoptions.<sup>6</sup> Second, the identification strategy used in recent observational studies (e.g., matching and difference-in-difference) is based on the assumption that all endogeneity can be controlled by observables. However, this is unlikely in our case. As discussed later, we find evidence of sorting on unobservable (i.e., customers have private information about their future need of the app, and such information cannot be explained by observables). To address both of these challenges, we conduct a field experiment, use interventions to create exogenous variations in induced adoption, and identify the causal effect of induced adoption using LATE. The randomized experiment, with external interventions randomly assigned over control and treatment groups, creates two unique features that are missing in the observational data: (1) a control group where only organic adoptions happen and (2) an exogenous and large shock to generate variation in the induced adoptions The control group serves as a counterfactual (with only organic adoption) and helps us isolate the additional induced adoptions in treatment groups. The exogenous variation in induced adoptions ensures that its effect on customers’ purchases is causal.

## LATE Approach–Intuition

We explain the intuition of LATE using Figure 1. In all three test groups (Control, T1, and T2), a portion of the customers would adopt the app organically. They are denoted as “always-takers” in the LATE framework (Athey and Imbens 2017), and they are represented by the solid squares in Figure 1. In addition, some customers in the two treatment groups may be induced to adopt the mobile app after exposure to the interventions. The adoption decision is contingent on the specific in tervention used by the firm and customers’ own information about their need for the app. Such induced adopters are called “compliers” in LATE framework, and they are represented by dotted squares (for incentive-induced adopters) and dashed squares (for information-induced adopters) in Figure 1. LATE can causally identify the treatment effect on (different types of) compliers based on the following logic. First, the

Figure 2. Email Templates for Treatment 1 and Treatment 2  
(T1) Email Template for Treatment 1: Highlight incentive for app adoption  
![](/api/attachments/5RTJC5TK/fulltext/images/4266e6d440b7082e5a6b0814a5c9dff2866a8c516571ee46601beaa592ff1b53.jpg)

(T2) Email Template for Treatment 2: Highlight information about the benefits of the app  
![](/api/attachments/5RTJC5TK/fulltext/images/b120eeea42220b2a2897c7441402dcb37b11aaacd06bbfa664a604ce1deaf6bc.jpg)  
Notes. (T1) Email template for T1: highlight incentive for app adoption. (T2) Email template for T2: highlight information about the benefits of the app.

experiment incorporates a control group with no intervention and thus, provides a perfect counterfactual. We can observe what would happen if users had not received any interventions (Control in Figure 1). Therefore, we can isolate the compliers at an aggregate level by comparing the adoption decision of customers in the control group with those in each treatment (dotted square for compliers in T1 and dashed area for compliers in T2 in Figure 1). Second, for compliers in each treatment, we can separately identify the effect of induced app adoptions on their future purchase behaviors. Technically, we run a two-stage least square regression using test group assignment as the instrumental variable (see Equation 1) (Imbens and Angrist 1994, Wooldridge 2010). Because the intervention is randomly assigned, the identified effect i not correlated with any confounding factors $( \mathrm { e . g . } ,$ endogenous targeting), and thus, causality is assured (Zhang and Zhu 2011, Qiu and Kumar 2017, Cui et al. 2018):

$$
D o w n l o a d _ {i} = \sum \alpha_ {k} \times T _ {i k} + \varepsilon_ {i},
$$

$$
P u r c h a s e _ {i} = \beta \times \widehat {D o w n l o a d} _ {i} + \sigma_ {i}.\tag{1}
$$

We want to highlight that the characteristics of compliers might be different from those of the average users on the platform. However, it is important to remember that (1) the identification of the treatment effect on those users is perfect because of the use of control group and exogenous interventions and that (2) those users are exactly the population of interest, because firms can only actively induce/influence those users for app adoption using interventions. In contrast, the average users are hardly the (“influenceable”) adopters. Therefore, the causal effect identified by LATE for this population of compliers (dotted area or dashed area in Figure 1) is exactly what firms wish to know. The LATE approach offers two benefits: the causal effect identified by LATE is (1) specific to the compliers (the population of interest) and (2) contingent on the instrument/ intervention that the firm uses (Athey and Imbens 2017). Thus, firms can compare the effect of adoptions induced by different types of interventions.

The identification of LATE is based on two key assumptions. The first is monotonicity (Imbens and Angrist 1994), which requires the probability of app adoption to be increasing when a user is treated (adoption (treated) > adoption (control)). This assumption is satisfied in our context, because our email campaign provides more information or incentive for app adoption. The second assumption is the exclusion restriction, which requires that there be no direct effect of the treatment (receiving email with information or incentive) on the outcome (e.g., purchase behaviors) without being mediated by the mobile app adoption. In other words, all changes in customers’ future purchase behaviors should be driven by the difference in induced app adoptions. In our context, the information treatment (T2) is one time only and only mentions the benefits of the app (rather than encouraging purchases). Thus, it satisfies the exclusion restriction.<sup>7</sup> The incentive treatment (T1) provides a monetary incentive for app adoption (i.e., five deal bucks), but the incentives expire within two weeks of delivery. Thus, we would expect a short-run increase in customers’ purchases in T1 because of the effect of the incentives within the first three weeks (i.e., one week to claim the offer and two weeks to use deal bucks before expiration). However, firms are interested in the long-term effects of induced app adoptions beyond this short window for both T1 and T2. Therefore, we exclude all of the purchases within the first three weeks after the experiment for all test groups when estimating LATE. In this way, we can ensure that our interventions do not directly affect the dependent variable in the second stage (purchase behaviors). Thus, the exclusion restriction is satisfied.<sup>8</sup> Any effect on customers’ purchase behaviors in the long run (6 or 12 months) can be attributed back to the differences in induced app adoptions.

## 6. Research Context and Data

In collaboration with the daily deal platform, we designed and implemented a large-scale randomized field experiment as discussed in Section 4. The randomized field experiment was run on the platform for one day, and we were able to collect information for the entire sample of more than 230,000 unique customers over a long period after the experiment. For every customer, we record information, including the unique hashed identifier of the customers, the assigned test group, the mobile app adoption status (and adoption time), and all purchases before and after the experiment. For each purchase, we record detailed information, including the purchased deal and the revenue/ discount from the purchase as well as the purchase channel (mobile web or desktop). We further augment the purchase data set with rich deal characteristics (price, category, location, and merchant). The resulting data set enables us to analyze the effect of different interventions at an aggregate level as well as a more granular level.

## 7. Results and Discussion

We first check the validity of our randomization. In Table 1, we provide the breakdown of major covariates in the three groups. As shown in the results, there are no significant differences across the groups on all of the covariates (e.g., customer tenure, number of past purchases in total and across channels, and average price of purchased deals). The well-balanced sample indicates that our randomization is at work.

## Q1a: What Is the Effect of Incentive vs. Information on Customers’ App Adoptions?

We examine the effect of incentive (T1) or information (T2) in motivating mobile app adoption by estimating a linear probability model on the full sample as shown in Equation (2). A similar strategy is widely used in field experiment studies as illustrated in Duflo et al. (2008). The results are robust under alternative models, such as Logit and Probit (Online Appendix, Table A.2):

$$
D o w n l o a d _ {i} = \sum \alpha_ {k} \times T _ {i k} + \varepsilon_ {i};\tag{2}
$$

Download is a dummy variable indicating whether the customer i has downloaded the mobile app within a certain timeframe. Because customers can respond any time after receiving the email, we examine the results using different timeframes to understand how the effect changes over time $( \mathrm { e . g . }$ , one day, three days, one week, and two weeks after the experiment). $T _ { i k }$ is the dummy variable of test group k to which the customer i is randomly assigned.

The results are presented in Table 2. Both incentive (T1) and information (T2) lead to a significant increase in customers’ mobile app adoptions, and such effects are consistent across different timeframes (one day, three days, one week, and two weeks).<sup>9</sup> The magnitude of increase is economically significant: providing incentives can lead to a 466% increase in app downloads over that in the control group, whereas providing information leads to a 144% increase over the control group (based on downloads within three days). The stronger effect of monetary incentive (T1) on technology adoption is aligned with previous findings (Dupas 2014). In addition, consistent with the temporary nature of email communication, there is a large increase in mobile app adoption in both T1 and T2 on the first day, and the differences in app adoption (T1 <sup>−</sup> Control and T2 <sup>−</sup> Control) become stable within a week after the intervention (Table 2).

Table 1. Randomization Check

<table><tr><td></td><td>Control, n = 137,195</td><td>T1, n = 48,027</td><td>T2, n = 48,070</td><td>p-Value (Control = T1 = T2)</td></tr><tr><td colspan="5">Customer tenure, days</td></tr><tr><td>Mean</td><td>0</td><td>-1.32</td><td>0.01</td><td>0.407</td></tr><tr><td>SD</td><td>193.4</td><td>192.9</td><td>193.97</td><td></td></tr><tr><td colspan="5">Total no. of purchases</td></tr><tr><td>Mean</td><td>0</td><td>0.01</td><td>0.01</td><td>0.909</td></tr><tr><td>SD</td><td>3.82</td><td>3.69</td><td>3.74</td><td></td></tr><tr><td colspan="5">Total desktop purchases</td></tr><tr><td>Mean</td><td>0</td><td>0.02</td><td>0.01</td><td>0.726</td></tr><tr><td>SD</td><td>3.6</td><td>3.48</td><td>3.52</td><td></td></tr><tr><td colspan="5">Total mobile web purchases</td></tr><tr><td>Mean</td><td>0</td><td>-0.01</td><td>0</td><td>0.384</td></tr><tr><td>SD</td><td>0.84</td><td>0.81</td><td>0.83</td><td></td></tr><tr><td colspan="5">Total revenue</td></tr><tr><td>Mean</td><td>0</td><td>-0.02</td><td>0.21</td><td>0.983</td></tr><tr><td>SD</td><td>237.37</td><td>228.19</td><td>236.89</td><td></td></tr><tr><td colspan="5">Average price of deal purchases</td></tr><tr><td>Mean</td><td>0</td><td>-0.39</td><td>-0.53</td><td>0.481</td></tr><tr><td>SD</td><td>89.88</td><td>82.10</td><td>80.83</td><td></td></tr><tr><td colspan="5">No. of unique deal categories purchased</td></tr><tr><td>Mean</td><td>2.08</td><td>2.08</td><td>2.09</td><td>0.460</td></tr><tr><td>SD</td><td>1.44</td><td>1.46</td><td>1.45</td><td></td></tr></table>

Notes. The figures provided are demeaned values obtained by subtracting the mean value of treatment groups from that of control group. Demeaning preserves the difference in mean value between test groups as well as the t test (i.e., randomization check). SD, standard deviation.

In summary, our results show that firms can effectively motivate customers to adopt mobile apps using external interventions, with monetary incentive leading to significantly more adoptions than pure information. The key questions then are whether such app adoptions induced by external interventions can lead to a significant increase in customers’ purchase behaviors and whether incentive-induced adoption is more effective than information-induced adoption.

## Q1b: What Is the Causal Effect of Induced App Adoptions on Customers’ Behaviors in the Long Run, and Does the Effect Vary for Adoptions Induced by Incentive vs. Information?

We are particularly interested in the causal effect of induced mobile adoptions, rather than organic adoptions,

Table 2. Effect of Treatments on Mobile App Adoptions (Q1a)

<table><tr><td></td><td>Download_1day</td><td>Download_3day</td><td>Download_1week</td><td>Download_2week</td></tr><tr><td>T1</td><td>0.00533***(0.000347)</td><td>0.00931***(0.000497)</td><td>0.00995***(0.000543)</td><td>0.0101***(0.000626)</td></tr><tr><td>T2</td><td>0.00124***(0.000189)</td><td>0.00287***(0.000340)</td><td>0.00328***(0.000398)</td><td>0.00322***(0.000502)</td></tr><tr><td>Constant</td><td>0.000357***(5.10e-05)</td><td>0.00200***(0.000121)</td><td>0.00325***(0.000154)</td><td>0.00666***(0.000220)</td></tr><tr><td>Observations</td><td>233,292</td><td>233,292</td><td>233,292</td><td>233,292</td></tr><tr><td> $p(T1 = T2)$ </td><td>8.08e-26</td><td>7.44e-29</td><td>1.30e-25</td><td>1.35e-20</td></tr></table>

Notes. The coefficients of T1 and T2 are significantly different based on the p-value(T1 = T2). Robust standard errors in parentheses.  
\*\*\*p < 0.01.

Table 3. Customers’ Purchases Within Three Weeks After App Adoption (Short-Run Effect)

<table><tr><td rowspan="2"></td><td rowspan="2">Total purch_3week</td><td colspan="3">Decomposed by channel</td></tr><tr><td>Desktop_3week</td><td>Mobile_App_3week</td><td>Mobile_Web_3week</td></tr><tr><td>T1</td><td>0.00297(0.002138)</td><td>0.00269(0.001837)</td><td>0.00165***(0.0003256)</td><td>-0.000842(0.0008450)</td></tr><tr><td>T2</td><td>0.00288(0.002137)</td><td>0.00313*(0.001836)</td><td>0.000631*(0.0003255)</td><td>-0.00107(0.0008447)</td></tr><tr><td>Constant</td><td>0.114***(0.00109)</td><td>0.0871***(0.000935)</td><td>0.00243***(0.000166)</td><td>0.0198***(0.000430)</td></tr><tr><td> $p(T1 = T2)$ </td><td>0.974</td><td>0.844</td><td>0.010</td><td>0.827</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*\*p < 0.01.

on customers’ purchase behaviors, because firms can actively influence the level of induced adoption by providing incentives or information. We adopt the LATE framework (Imbens and Angrist 1994, Angrist et al. 1996) to identify the causal effect of induced adoptions (Section 5). The causal effect of induced adoptions is identified by LATE, wherein the exogenous treatment assignment serves as the instrument variable to isolate the induced adoptions from organic adoptions. As discussed above, the effect of both incentives and information on app downloads becomes stable after one week. Thus, we use the download within the first week after the experiment as our outcome variable in Stage 1 and the instrument in Stage 2. We choose the timeframe to include as many induced adoptions as possible and also exclude organic adoptions to maintain the power in second-stage estimation.<sup>10</sup> To examine the long-term effects of induced app adoptions on customers’ purchase behaviors, we examine their purchases in two timeframes after the experiment—within six months and within 12 months. Following discussions in Section 5 and consistent with our focus on behavior changes in the long run, we exclude all purchases within the first three weeks when constructing the purchase outcome (the results for purchases within the first three weeks are separately presented in Table 3). The results are robust when we exclude purchases in alternative time windows: the first three months and the first six months (Online Appendix, Table A.1).

We present the results from LATE in Table 4. Interestingly, we find that only app adoptions induced by information (T2) lead to a significant increase in customers’ purchases in the long run. In contrast, app adoptions induced by incentive (T1) have no causal impact on customers’ purchase behaviors. The results suggest that the effect of mobile app adoptions heavily depends on how customers are induced to adopt the app in the first place. Although monetary incentives (T1) are effective in driving people to adopt the app, such a recruitment approach does not lead to more purchases from customers after they download the app. In contrast, providing information leads to a smaller increase in app adoptions, but such adoptions lead a sustainable increase in customers’ purchases in the long term. These findings show the nuanced tradeoffs between motivating mobile app adoption and appropriating value from such adoption, and they provide guidelines to firms on how to encourage effective app adoptions.

Table 4. Effect of Induced App Adoptions on Purchase Behaviors in the Long Run: LATE (Q1b)

<table><tr><td rowspan="2"></td><td colspan="2">T1</td><td colspan="2">T2</td></tr><tr><td>Purch_6month</td><td>Purch_1year</td><td>Purch_6month</td><td>Purch_1year</td></tr><tr><td>Induced adoption</td><td>-0.274(0.830)</td><td>-0.500(1.476)</td><td>5.081**(2.589)</td><td>10.25**(4.650)</td></tr><tr><td>Constant</td><td>0.877***(0.00613)</td><td>1.685***(0.0109)</td><td>0.859***(0.0113)</td><td>1.650***(0.0201)</td></tr><tr><td>Observations</td><td>185,222</td><td>185,222</td><td>185,265</td><td>185,265</td></tr></table>

Notes. We exclude customers’ purchases within the first 3 weeks to maintain exclusion restriction and focus on customers’ purchase behavior in the long run. The results are robust when excluding purchases within the first three months and six months (Online Appendix, Table A.1). Robust standard errors in parentheses.

$$
^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

Table 5. Effect of Treatment on Customer Profitability (Q1c) Measured by Average Number of Purchases

<table><tr><td></td><td>Purch_3month</td><td>Purch_6month</td><td>Purch_1year</td></tr><tr><td>T1</td><td>0.000407(0.00557)</td><td>0.000243(0.00912)</td><td>-0.00201(0.0154)</td></tr><tr><td>T2</td><td>0.00939*(0.00567)</td><td>0.0196**(0.00923)</td><td>0.0365**(0.0157)</td></tr><tr><td>Constant</td><td>0.490***(0.00288)</td><td>0.990***(0.00472)</td><td>1.798***(0.00799)</td></tr><tr><td>Observations</td><td>233,292</td><td>233,292</td><td>233,292</td></tr><tr><td> $p(T1 = T2)$ </td><td>0.188</td><td>0.083</td><td>0.041</td></tr></table>

Note. Robust standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## Q1c: What Is the Impact of Incentive vs. Information on Firm’s Overall Pro<sup>fi</sup>tability?

We run an Ordinary Least Squares (OLS) model on the full sample to examine the effect of two interventions on overall profitability (i.e., number of total purchases as well as net profits) using Equation (3):

$$
P u r c h a s e _ {i} = \sum \gamma_ {k} \times T _ {i k} + \epsilon_ {i};\tag{3}
$$

Purchase is the number of purchases within a timeframe for customer i. We use customers’ purchases within six months and 12 months after the interventions (including the first three weeks) as the outcome measure to investigate the overall effect of our interventions on customer profitability. The results are displayed in Table 5. Consistent with the findings on the causal effect of induced adoption (Q1b), we find that providing information (T2) has a positive and significant effect on customers’ purchases (Table 5) and net profits (Online Appendix, Table A.3) across different timeframes (but does not increase product returns as shown in Narang and Shankar 2016) (Online Appendix, Table A.13). Such an increase is about 2%–3% of net profits from all customers in the treatment group (T2) and amounts to hundreds of thousands of dollars if the information intervention is scaled up to target all active users on the platform. In contrast, providing incentives does not lead to any significant increase in customer profitability as measured by both total purchases (Table 5) and net profits (Online Appendix, Table A.3). After taking into account the cost of incentives for adopters, the firm may lose a good amount of investment in the incentive treatment (T1) group. Overall, our results suggest that providing information may increase customer profitability, whereas monetary incentives may not, although the latter may lead to more app adoptions. Given the lower cost of providing information compared with monetary incentives, our findings indicate that managers should use information provisioning as the main mechanism to encourage mobile app adopters with aligned need.

## Q2: How Do Incentive- and Information-Induced App Adoptions Affect Customers’ Purchase Behaviors Across Mobile and Desktop Channels?

Although the previous analyses consistently support a positive effect of information-induced adoptions and reveal the difference between the effects of informationversus incentive-induced adoption, they do not shed light on the process underlying the treatment effect. In the rest of this section, we delve into the process and explore how app adoption affects customers’ online shopping behavior across channels.

We first investigate the channel interdependencies for different types of induced adoptions by decomposing customers’ purchases into different channels (Xu et al. 2016). There are three channels that customers can use to browse deals and make purchases—desktop (personal computer), mobile web, and mobile app. The mobile web channel provides a smaller and customized view of the desktop website to fit the mobile screen. Mobile app offers the same set of products as the desktop and the mobile web but presents them in a way that is more convenient for mobile browsing and search.

Our objective here is to understand the causal effect of induced mobile app adoptions on customers’ purchases through these different channels. We follow previous literature (Xu et al. 2016) and use the same empirical approach discussed in Q2 by changing our dependent variable to customer’s purchases within each channel (i.e., Desktop\_Purch for desktop purchases, MobileApp\_Purch for mobile app purchases, and MobileWeb\_Purch for mobile web purchases). We use the LATE approach and leverage exogenous treatment assignment as the instrument variable for our identification. The results are presented in Table 6. Recalling our results on overall purchases, induced adoptions by information (T2) lead to a positive and significant effect on customers’ purchases, whereas those by incentive (T1) do not. In examining the results of the analysis of data broken down by channels, we find that adoption induced by monetary incentives (T1) has a significant negative impact on mobile web purchases, whereas it has a positive impact on mobile app purchases (not statistically significant). The two channels substitute each other, resulting in a nonsignificant net effect. In contrast, app adoptions induced by information (T2) have a positive and significant impact on purchases through the desktop channel. This indicates that the desktop and mobile app channels are complementary to each other for information-induced adopters (T2). Such complementarity is aligned with findings in previous literature (Xu et al. 2014, De Haan et al. 2015). The above results indicate that the incentive-induced adopters merely shift their purchases from the mobile web to the mobile app channel (because the latter offers a better shopping experience on the same device) but do not significantly change their total purchases in the long run (because they do not continue using the mobile app), whereas the information-induced adopters still use the desktop intensively but add the mobile app as a complementary channel for deal discovery in their online shopping process. This is consistent with recent observations in recent observational studies (e.g., Xu et al. 2014) and in the industry. For instance, citing various reports, Koetsier (2017) suggested that “retailers need to be aware that the customer journey is not simple. Many will view items on their mobile devices but only purchase on their desktop or laptop computers.”

Table 6. The Causal Effect of Induced Mobile App Adoptions on Customers’ Purchases (LATE) Decomposed by Channel

<table><tr><td></td><td>Desktop</td><td>Mobile app</td><td>Mobile web</td></tr><tr><td>Incentive-induced app adoption (T1)</td><td>0.611(0.693)</td><td>0.176(0.146)</td><td>-0.622*(0.33)</td></tr><tr><td>Information-induced app adoption (T2)</td><td>5.399**(2.176)</td><td>0.887**(0.445)</td><td>-0.401(0.998)</td></tr></table>

Notes. Here, we report purchases within six months. The results are robust for one year. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05.

## Q3: What Is the Underlying Driver of the Differences Between the Causal Effect of App Adoptions Induced by Incentive vs. Information?

As discussed in Section 3, the differential impact of incentive- and information-induced adoption on customers’ purchase behaviors is potentially driven by sorting (i.e., those information-induced adopters are different from those incentive-induced adopters in their observable characteristics and unobserved need). We now empirically explore and test the derived implications in Section 3 related to sorting on observables and unobservables.

We indeed find that adopters across two treatments are different in their observable characteristics (Table 7): the information-induced adopters, who benefit more from app adoption, make fewer purchases before the experiment but on average, purchase more expensive deals. In addition, we also find that the incentive treatment (T1) increases customers’ purchases in the short run (e.g., the first three weeks) in the mobile app channel (Table 3), but the effect disappears after the first three weeks (Table 2). The evidence is aligned with the explanation that incentive may attract users who do not value the mobile app as much but are more interested in the monetary reward. Thus, after using the deal bucks (which were valid for three weeks), they are no longer as active in using the app.

Given the findings on the differences in observables for adopters across different groups, we ask if firms could leverage customers’ observable characteristic to predict who would need the mobile app most (or will increase their purchases most from mobile adoption). If yes (i.e., sorting on observable), then firms can actively target those high-potential customers and encourage app adoptions using incentive. This would enable firms to achieve both coverage and effectiveness in motivating app adoptions. If the answer is no (i.e., sorting on unobservable), then firms would need to design an appropriate intervention (i.e., information provisioning) to encourage sorting and may have to make a tradeoff between coverage and effectiveness in app adoption. We formally test whether sorting is purely based on observables by adding observable covariates in both stages (Imbens and Angrist 1994, Angrist et al. 1996). Interestingly, we find that, after accounting for various observable characteristics, there is still a strong positive relationship between indicator of informational treatment (T2) and the treatment effect (Table 8) (the magnitude of the causal effect is almost the same and highly significant). The results may potentially indicate a strong form of sorting—sorting on unobservables— underlying induced adoptions. In other words, customers possess private information about their needs or potential usage of the mobile app that is unobservable by firms. Thus, firms can only use certain interventions to attract the customers with a higher need to sort into adoption, therefore increasing customers’ purchases in the long run. 11

Table 7. Differences in Observable Characteristics Between Mobile App Adopters in Control, T1, and T2

<table><tr><td></td><td>Download_1day</td><td>Download_3day</td><td>Download_1week</td><td>Download_2week</td></tr><tr><td colspan="5">Preaverage price</td></tr><tr><td>T1</td><td>2.433(8.874)</td><td>1.159(6.724)</td><td>-0.611(5.179)</td><td>-1.485(3.382)</td></tr><tr><td>T2</td><td>29.93***(10.49)</td><td>22.79***(8.092)</td><td>15.67**(6.193)</td><td>9.644**(3.957)</td></tr><tr><td>p(T1 = T2)</td><td>0.0003</td><td>0.0025</td><td>0.0053</td><td>0.0061</td></tr><tr><td colspan="5">Pretotal purchase</td></tr><tr><td>T1</td><td>0.598(0.78)</td><td>0.784**(0.376)</td><td>0.929***(0.313)</td><td>0.840***(0.244)</td></tr><tr><td>T2</td><td>-0.633(0.918)</td><td>-0.255(0.452)</td><td>-0.336(0.373)</td><td>-0.153(0.285)</td></tr><tr><td>p(T1 = T2)</td><td>0.0584</td><td>0.0090</td><td>0.0003</td><td>0.0007</td></tr></table>

Note. Standard errors in parentheses.  
\*\*p < 0.05; \*\*\*p < 0.01.

Table 8. The Causal Effect of Induced Mobile App Adoptions on Customers’ Purchases (LATE) After Controlling for Observable Characteristics

<table><tr><td rowspan="2">LATE</td><td colspan="2">T1</td><td colspan="2">T2</td></tr><tr><td>Purch_6month</td><td>Purch_1year</td><td>Purch_6month</td><td>Purch_1year</td></tr><tr><td>Download_1week</td><td>-0.343(0.753)</td><td>-0.629(1.314)</td><td>4.661**(2.321)</td><td>9.464**(4.087)</td></tr><tr><td>Pre_desktop</td><td>0.180***(0.00105)</td><td>0.340***(0.00183)</td><td>0.181***(0.00111)</td><td>0.341***(0.00196)</td></tr><tr><td>Pre_mobile_web</td><td>0.308***(0.00428)</td><td>0.584***(0.00747)</td><td>0.304***(0.00512)</td><td>0.572***(0.00902)</td></tr></table>

Note. Standard errors in parentheses.  
\*\*p < 0.05; \*\*\*p < 0.01.

We further test implications related to sorting on unobservables. As discussed in Section 3, if sorting is at work, providing information (T2) would attract customers who would use the app more often and discover more deals.<sup>12</sup> Consistent with increased deal browsing as suggested by sorting, we find that those information-induced app adoptions are likely to lead to a larger variety of purchases in general (Table 9). In other words, the information-induced app adoptions increase not only the number of purchases but also, the unique number of deal categories from which a customer purchased, which represents an additional benefit to the platform. In a similar vein, such information-induced adoptions are more likely to lead to a larger increase in customers’ purchases in cities with a higher deal density (Table 10), where customers may benefit more from app usage by exploring more deals. The two findings suggest that firms may encourage more product exploration through information-induced app adoption.

Finally, our intervention (i.e., an information email) may affect the customers’ purchase behaviors in the long run through two mechanisms: sorting and treatment. The treatment mechanism indicates that information-induced adopters would be similar to organic adopters (i.e., no sorting). The difference in the outcomes is only driven by the fact that they have received the information (email), which may directly influence their purchase behavior in the long run. It is notoriously hard to rule out the treatment mechanism using observational data (Wooldridge 2010), because the same intervention (i.e., information email) may induce sorting and a treatment effect at the same time. We, therefore, design and implement an additional randomized experiment to examine the treatment/ influence mechanism (i.e., whether the information treatment would have a direct impact on customers purchase behaviors in the long run). To this end, we carefully choose over 2,800 users who have already adopted the mobile app (existing adopters) and randomly assign them into control and treatment groups (Online Appendix, Table A.18). All users in the treatment group would receive an information email about the app. Using existing app adopters as the experimental subjects allows us to turn off sorting and cleanly identify the effect of the information email (T2). We find that information treatment does not have a significant effect on customers’ purchase (Table 11). These findings rule out the informational treatment mechanism and provide further support of sorting mechanism as the driver behind the differential effect of induced app adoptions.

## 8. Conclusion and Future Research

In summary, our study is among the first to investigate how firms can actively influence customers’ adoption of mobile apps and increase customers’ purchases through induced app adoptions. Our study confirms that firms may motivate effective app adoption and increase net profits but only when using the appropriate intervention. Contrary to the conventional wisdom and common practice, we find that providing incentive may induce negative sorting in mobile app adoption and does not lead to long-run increases in customers’ purchase and firm’s profitability. In contrast, information-based intervention may attract the right type of customers who have strong needs of the app and would use it effectively (i.e., positive sorting). By leveraging a carefully designed randomized field experiment, our study shows that the causal effect of induced app adoptions may critically depend on how customers are motivated. We further look into the underlying driver of such difference in the effect of induced adoption (i.e., sorting on unobservable) and examine how adopters induced by different interventions behave differently in their purchase behaviors across multiple channels. The nuanced findings of the study not only provide guidelines for designing interventions to motivate effective mobile app adoptions but also, add to our understanding of the role of mobile apps in changing customers’ online shopping behaviors.

Table 9. The Causal Effect of Induced Mobile App Adoptions (LATE) on the Diversity of Customers Purchases (Measured by Unique Number of Deal Categories Purchased)

<table><tr><td></td><td>Unique_categories_6month</td><td>Unique_categories_1year</td></tr><tr><td>Induced adoption by T1</td><td>0.261(0.554)</td><td>0.549(0.755)</td></tr><tr><td>Induced adoption by T2</td><td>3.719**(1.718)</td><td>4.111*(2.319)</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05.

Table 10. The Causal Effect of Induced Mobile App Adoptions (LATE) Decomposed by Cities with High/Low Deal Density

<table><tr><td rowspan="2"></td><td colspan="2">Six months</td><td colspan="2">One year</td></tr><tr><td>Low (1~265)</td><td>High (&gt;265)</td><td>Low (1~265)</td><td>High (&gt;265)</td></tr><tr><td rowspan="2">Induced adoption by T1</td><td>-0.381*</td><td>0.148</td><td>-0.352</td><td>-0.117</td></tr><tr><td>(0.198)</td><td>(0.767)</td><td>(0.333)</td><td>(1.333)</td></tr><tr><td rowspan="2">Induced adoption by T2</td><td>1.089*</td><td>3.872*</td><td>3.401***</td><td>6.697*</td></tr><tr><td>(0.616)</td><td>(2.349)</td><td>(1.075)</td><td>(4.084)</td></tr></table>

Notes. We categorize all cities in our sample into high/low based on whether the deal density of the city is above median (i.e., 265 deals). Standard errors in parentheses. $^ { * } p < 0 . 1 ; ^ { * * * } p < 0 . 0 1 .$

We believe that there are a few interesting directions for future research. First, our study shows a fundamental tradeoff that firms are facing when designing intervention to motivate app adoption: how to balance coverage (more adoption) and effectiveness (better adoption)? We show that offering incentives may boost coverage, but providing information, rather than incentives, is what leads to effective adoptions. Ideally, firms want to predict a subset of customers who would positively benefit from induced app adoption and target them with monetary incentive to enhance adoption. However, we find that the difference in treatment effects of induced adoptions cannot be fully predicted by observable characteristics. Thus, firms may rely on the appropriate intervention to encourage sorting. However, to a certain extent, firms may still be able to identify certain customer segments that would benefit more from induced app adoption. For instance, we find that information-induced adoptions are more effective for customers who have only used the desktop channel in their past purchases (Table 12). Future research can extend our study by combining prediction with active intervention in targeting application (L et al. 2015) to achieve better coverage and higher effectiveness of mobile app adoption.

Second, in this study, we keep in-app experience the same for adopters in three test groups and do not vary in-app intervention, because our goal is to identify the causal effect of induced app adoption (rather than inapp intervention) on customers’ purchases. Our study shows that it is important for firms to “get the right adoption” at the beginning, because such adoption may lead to long-run increase in customer profitability. However, on adoption, firms may also use in-app interventions to further engage customers (Kato-Lin et al. 2015, Son et al. 2016). For instance, firms may encourage customers to use the app to initiate more product discovery and purchases, especially for those incentive-induced adopters. Understanding the effect of in-app intervention, contingent on various types of adoption, is thus crucial. Future research may extend our study by examining different types of mobile interventions (Li et al. 2015, Wang et al. 2016, Zhang et al. 2019) after the app adoption. Researchers may also investigate how mobile interventions can be customized for different types of induced adopters (Ma et al. 2007, Ghose 2017, Ghose et al. 2019).

Third, our paper has focused on identifying the effect of app adoptions induced by two of the most commonly used interventions in mobile app campaigns: incentive and information (Ohayon 2011, Techcrunch 2015a).

Table 11. Effect of Information Intervention on Existing Adopter’s Purchase Behaviors

<table><tr><td>Variables</td><td>Purch_1month</td><td>Purch_3month</td></tr><tr><td>Providing information</td><td>-0.0305(0.0324)</td><td>-0.0901(0.0707)</td></tr><tr><td>Constant</td><td>0.363***(0.0177)</td><td>1.058***(0.0377)</td></tr></table>

Notes. We only present the results on treatment effect here. Please see the randomized check for the field experiment in the online appendix. Robust standard errors in parentheses.  
\*\*\*p < 0.01.

Table 12. The Causal Effect of Induced Mobile App Adoptions on Customers’ Purchases (LATE) Across Channels Decomposed by Preexperiment Channel Usage

<table><tr><td rowspan="2">Treatment</td><td colspan="4">Purchases within 6 months</td></tr><tr><td>Total</td><td>Desktop</td><td>Mobile app</td><td>Mobile web</td></tr><tr><td>Desktop only purchasers (n = 190,069)</td><td></td><td></td><td></td><td></td></tr><tr><td>T1</td><td>0.128(0.989)</td><td>1.031(0.876)</td><td>0.118(0.159)</td><td>-0.724***(0.273)</td></tr><tr><td>T2</td><td>5.884**(2.915)</td><td>4.829*(2.577)</td><td>0.882*(0.476)</td><td>0.833(0.798)</td></tr><tr><td>Mobile purchasers (exclude desktop only; n = 43,134)</td><td></td><td></td><td></td><td></td></tr><tr><td>T1</td><td>-1.491(1.637)</td><td>-0.544(1.053)</td><td>0.355(0.314)</td><td>0.061(0.875)</td></tr><tr><td>T2</td><td>1.012(5.459)</td><td>6.818*(4.026)</td><td>0.943(1.052)</td><td>-3.468(3.127)</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Future research may further investigate the effect of app adoptions induced by other types of interventions (e.g., firm-created word-of-mouth).

Fourth, in our experiment, we focus on active users (with at least one purchase before experiment). Future research can extend our study by examining the effect of interventions on the app adoption decisions of less active users as well as the causal effect of induced adoptions for those users. However, given the potentially lower response rate, it would be more challenging to detect significant effect of app adoptions for less active users. Our experimental design and empirical results can serve as a useful reference for designing similar large-scale experiments in future.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three reviewers for insightful and constructive comments. They also thank Vibhanshu Abhishek, Jason Chan, Pedro Ferriera, Anindya Ghose, Jing Gong, Sang-Pil Han, Ian Ho, Tony Ke, Xiao Liu, Xueming Luo, and conference participants at Statistical Challenges in E-Commerce, INFORMS, and Conference on Information Systems and Technology for constructive comments. All errors are the authors’ errors.

## Endnotes

<sup>1</sup> Q1a, Q1c, Q2, and Q3 have also not been addressed in previous studies, most of which use observational data. Answers to those questions require both randomized experiments and active design of interventions.

<sup>2</sup> In China, a huge amount of venture capital funding has gone toward subsidies for mobile app adoptions. Such subsidy in general leads to poor returns because of low customer engagement in the long run (Clover 2016).

studies, self-selection, which indicates that customers who are more likely to make purchases have a higher propensity to adopt the app, may bias the identification of the causal effect of app adoptions. However, in our case, the treatment effect of induced adoptions is perfectly identified using the exogenous interventions in the experi ment. The “sorting effect” simply implies that the identified treatment effects may vary for adopters induced by different interventions. Second, although self-selection means that customers’ adoption decisions may be related to their purchase behaviors (Y), sorting implies that customers may make adoption decisions based on the potential private benefits of app usage (<sup>Δ</sup>Y).

<sup>4</sup> We focus on active users who have made at least one purchase for the following reasons. First, firms often target active users in their mobile campaigns, because they may purchase more on adoption (DigiDay 2016). This is especially true when firms have a large number of active users (as in our case). Second, the response rate is usually very low for app download campaigns. To have enough power to identify the causal effect of induced adoptions, we focus on active users who usually have a higher response rate.

<sup>5</sup> This is true for campaigns across different ecommerce platforms (i.e., as revealed from low conversion rate of app adoption) and technology adoption in general (Ashraf et al. 2010, Dupas 2014).

<sup>6</sup> We want to highlight that, beyond incentive- and informationinduced adoptions, there are potentially other types of induced adoption, such as firm-created word-of-mouth. However, the existence of word-of-mouth or other nonexperimental induced adoptions would be taken care of by the random assignment in our experiment. The blue squares in Figure 1 may include both adopters from un controlled factors (e.g., word-of-mouth), but they are equally distributed across test groups. Our experiment is not designed to identify the exact source of each adoption at the individual cus tomer level. Rather, the randomized experiment assures that any organic or nonexperiment induced adoptions are equally distributed across groups at an aggregate level. Therefore, we can directly attri bute the differences in customers’ app adoptions and the purchase behaviors to the different treatments. Such comparison allows us to cleanly identify the differential effect of treatments tested in the experiment (incentive versus information intervention) without the need to overcome attribution challenges and understand the source of each adoption (e.g., word-of-mouth, delayed effects, or other uncontrolled factors). We sincerely thank the associate editor and one reviewer fo these suggestions.

<sup>7</sup> We also designed and implemented an additional randomized field experiment on existing app adopters to ensure that providing in formation does not directly affect their purchase behavior in the long run. Such experiment further confirms the validity of the instrumental variable. Please see detailed results and discussion in Section 7.

<sup>8</sup> We also conduct robust checks (Online Appendix, Table A.1) and show that the results remain robust when excluding purchases fo different time periods (e.g., first three and six months), indicating that the exclusion restriction is not sensitive to the choice of time window.

<sup>9</sup> The effect of incentive and information on app adoption is also consistent and stable in the long run. See Online Appendix, Table A.5 for the treatment effects in alternative time windows (1, 3, 6, 9, and 12 months).

<sup>10</sup> We also estimated LATE using alternative instruments (i.e., download behavior of three days, two weeks, and three weeks). The results are qualitatively and quantitatively similar to the results using download behavior of one week (Online Appendix, Table A.4).

<sup>11</sup> However, with the emergence of big data, firms may access a richer set of information and have more advanced techniques to understand and predict sorting. Thus, they may be able to combine prediction with induced adoption.

<sup>12</sup> The daily deal platform offers a wide range of deals on local services and standard products, including restaurants, entertainment, outdoor activities, home services, retailing products, fitness activities, travel, beauty, and health services. The vast majority of deals on the platform are local deals. Depending on the location (e.g., big versus small cities), the inventory of deals per city may vary between a few and a few hundred deals. Customers may benefit from looking through daily deals on the mobile app (e.g., deal discovery), especially in cities with a higher deal density.

## References

Ailawadi KL, Neslin SA (1998) The effect of promotion on consumption: Buying more and consuming it faster. J. Marketing Res. 35(3):390–398.

Angrist JD, Imbens GW, Rubin DB (1996) Identification of causal effects using instrumental variables. J. Amer. Statist. Assoc. 91(434): 444–455.

Ashraf N, Berry J, Shapiro JM (2010) Can higher prices stimulate product use? Evidence from a field experiment in Zambia. Amer. Econom. Rev. 100(5):2383–2413.

Athey S, Imbens GW (2017) The econometrics of randomized experiments. Duflo E, Banerjee A, eds. Handbook of Economic Field Experiments, vol. 1 (North-Holland, Amsterdam), 73–140.

Bang Y, Han K, Animesh A, Hwang M (2013) From online to mobile: Linking consumers’ online purchase behaviors with mobile commerce adoption. Proc. 2013 Pacific Asia Conf. Inform. System (PACIS) (Association for Information Systems, Atlanta), https:/ aisel.aisnet.org/pacis2013/128

Brynjolfsson E, Hu Y, Rahman MS (2009) Battle of the retail channels: How product selection and geography drive cross-channel competition. Management Sci. 55(11):1755–1765.

Charness G, Gneezy U (2009) Incentives to exercise. Econometrica 77(3):909–931.

Clover C (2016) China tech: Renminbi to burn. Financial Times (April 10), https://www.ft.com/content/eac1ff4a-fc9d-11e5-b5f5 -070dca6d0a0d.

Cohen J, Dupas P (2010) Free distribution or cost-sharing? Evidence from a randomized malaria prevention experiment. Quart. J. Econom. 125(1):1–45.

Cohen J, Dupas P, Schaner S (2015) Price subsidies, diagnostic tests, and targeting of malaria treatment: Evidence from a randomized controlled trial. Amer. Econom. Rev. 105(2):609–45.

Cui R, Zhang DJ, Bassamboo A (2018) Learning from inventory availability information: Evidence from field experiments on Amazon. Management Sci. 65(3):1216–1235.

Datta H, Foubert B, Van Heerde HJ (2015) The challenge of retaining customers acquired with free trials. J. Marketing Res. 52(2): 217–234.

Dedman C (2011) Groupon mobile rewards offer: Purchase from mobile app get \$10 credit. Accessed February 28, 2016, http://blog .al.com/bargain-mom/2011/05/groupon\_mobile\_rewards\_offer \_p.html.

De Haan E, Kannan PK, Verhoef P, Wiesel T (2015) The role of mobile devices in the online customer journey. Working Paper Series 2015 Report No. 15-124, Marketing Science Institute, Cambridge, MA.

Deighton J, Henderson CM, Neslin SA (1994) The effects of advertising on brand switching and repeat purchasing. J. Marketing Res. 35(1):28–43.

DigiDay (2016) 3 Ways retailers are improving their mobile apps. Accessed June 1, 2016, http://digiday.com/marketing/3-ways -retailers-improving-shop-mobile-apps/.

Duflo E, Glennerster R, Kremer M (2008) Using randomization in development economics research: A toolkit. Schultz T, Strauss J, eds. Handbook of Development Economics, vol. 4 (North-Holland, Amsterdam), 3895–3962.

Dupas P (2014) Short-run subsidies and long-run adoption of new health products: Evidence from a field experiment. Econometrica 82(1):197–228.

Einav L, Levin J, Popov I, Sundaresan N (2014) Growth, adoption, and use of mobile e-commerce. Amer. Econom. Rev. 104(5):489–494.

Fang Z, Gu B, Luo X, Xu Y (2015) Contemporaneous and delayed sales impact of location-based mobile promotions. Inform. Systems Res. 26(3):552–564.

Forman C, Ghose A, Goldfarb A (2009) Competition between local and electronic markets: How the benefit of buying online depends on where you live. Management Sci. 55(1):47–57.

Ghose A (2017) Tap: Unlocking the Mobile Economy (MIT Press, Cambridge, MA).

Ghose A, Han SP (2014) Estimating demand for mobile applications in the new economy. Management Sci. 60(6):1470–1488.

Ghose A, Goldfarb A, Han SP (2013) How is the mobile Internet different? Search costs and local activities. Inform. Systems Res. 24(3):613–631.

Ghose A, Kwon HE, Lee D, Oh W (2019) Seizing the commuting moment: Contextual targeting based on mobile transportation apps. Inform. Systems Res. 30(1):154–174.

Guiteras R, Levinsohn J, Mobarak AM (2015) Encouraging sanitation investment in the developing world: A cluster-randomized trial. Science 348(6237):903–906.

Han SP, Park S, Oh W (2016) Mobile app analytics: A multiple discrete-continuous choice framework. MIS Quart. 40(4):983–1008

Hann IH, Koh B, Niculescu MF (2016) The double-edged sword of backward compatibility: The adoption of multigenerational platforms in the presence of intergenerational services. Inform. Systems Res. 27(1):112–130.

Imbens G, Angrist J (1994) Identification and estimation of local average treatment effects. Econometrica 61(2):467–476.

Jung J, Bapna R, Ramaprasad J, Umyarov A (2019) Love unshackled: Identifying the effect of mobile app adoption in online dating. MIS Quart. Forthcoming.

Kato-Lin Y-C, Padman R, Downs J, Abhishek V (2015) Evaluating consumer m-health services for promoting healthy eating: A randomized field experiment. AMIA Annual Sympos. Proc., San Francisco, 1947–1956

Koetsier J (2017) Holiday ecommerce to hit record \$107B in 2017; mobile will lead in visits. Forbes (November 2), https://www .forbes.com/sites/johnkoetsier/2017/11/02/holiday-ecommerce -to-break-100b-for-first-time-says-1-trillion-visit-adobe-study/ #3ab945393774.

Lazear EP (2000) Performance pay and productivity. Amer. Econom Rev. 90(5):1346–1361.

Lewis M (2006) Customer acquisition promotions and customer asset value. J. Marketing Res. 43(2):195–203

Li Y, Xie Y, Zheng E (2015) Competitive analytics of multi-channel advertising and consumer inertia. Proc. 2015 Americas Conf. Information Systems (AMCIS) (Association for Information Sys tems, Atlanta), https://aisel.aisnet.org/amcis2015/BizAnalytics GeneralPresentations/29/

Liu J, Abhishek V, Li B (2016) The impact of mobile adoption on customer omni-channel banking behavior. Proc. 2016 Internat. Conf. Inform. Systems (ICIS) (Association for Information Systems, Atlanta), https://aisel.aisnet.org/icis2016/EBusiness Presentations/10/.

Luo X, Andrews M, Fang Z, Phang CW (2013) Mobile targeting Management Sci. 60(7):1738–1756.

Ma Z, Pant G, Sheng ORL (2007) Interest-based personalized search ACM Trans. Inform. Systems 25(1):5.

Miller A (2014) Manage your incentivized mobile budget for maximum volume. Accessed February 28, 2016, http://secretsaucehq.com blog/mobile-marketing/manage-your-incentivized-mobile-budget -for-maximum-volume/.

Montaguti E, Neslin SA, Valentini S (2015) Can marketing campaigns induce multichannel buying and more profitable customers? A field experiment. Marketing Sci. 35(2):201–217.

Narang U, Shankar V (2016) The effects of mobile apps on shopper purchases and product returns. Working paper, Mays Business School, Texas A&M University, College Station.

Nelson P (1974) Advertising as information. J. Political Econom. 82(4): 729–754.

Neslin SA, Shankar V (2009) Key issues in multichannel customer management: Current knowledge and future directions. J. Interactive Marketing 23(1):70–81.

Ohayon O (2011) Are incentivized downloads a good thing? Bus. Insider (June 2), http://www.businessinsider.com/are-incentivized -downloads-a-good-thing-2011-6.

Qiu L, Kumar S (2017) Understanding voluntary knowledge provision and content contribution through a social-media-based prediction market: A field experiment. Inform. Systems Res. 28(3):451–679.

RetailMeNot (2016) The rise of mobile marketing spend in retail: 5 Trends to watch in 2016. Accessed December 9, 2016, https://www .retailmenot.com/corp/static/8643c0/filer\_public/e1/65/e1658d4f -9b8c-475a-88d0-f86f9a21f1f9/rmn-wp-kelton-030116-web-v2.pdf.

Retana GF, Forman C, Wu DJ (2018) Proactive customer education, customer retention, and demand for technology support: Evidence from a field experiment. Manufacturing Service Oper. Management 18(1):34–50.

Retana GF, Forman C, Narasimhan S, Niculescu MF, Wu DJ (2017) Technology support and post-adoption IT service use: Evidence from the cloud. MIS Quart. 42(3):961–978.

Shankar V, Kleijnen M, Ramanathan S, Rizley R, Holland S, Morrissey S (2016) Mobile shopper marketing: Key issues, current insights, and future research avenues. J. Interactive Marketing 34:37–48.

Siwicki B (2014) Mobile commerce will be nearly half of e-commerce by 2018. Internet Retailer (March 10), http://www.internetretailer.com 2014/03/10/mobile-commerce-will-benearly-half-e-commerce-2018.

Son Y, Oh W, Han SP, Park S (2016) The adoption and use of mobile application-based reward systems: Implications for offline

purchase and mobile commerce. Proc. 2016 Internat. Conf. Inform. Systems (ICIS), (Association for Information Systems, Atlanta), https://aisel.aisnet.org/icis2016/ITImplementation/Presentations/3/.

Stiglitz JE (1975) The theory of “screening,” education, and the distribution of income. Amer. Econom. Rev. 65(3):283–300.

Techcrunch (2015a) What’s better? Incentivized or non-incentivized app-install campaigns. Accessed February 28, 2016, https:/ techcrunch.com/2015/09/10/whats-better-incentivized-or-non -incentivized-app-install-campaigns/.

Techcrunch (2015b) Amazon rolls out a referral program to encourage more customers to shop on mobile. Accessed February 28, 2016, https://techcrunch.com/2015/12/17/amazon-rolls-out-a -referral-program-to-encourage-more-customers-to-shop-on -mobile/.

Wang Q, Li B, Wang P, Yang J (2016) Using TB-sized data to understand multi-device advertising. Proc. 2016 Internat. Conf. Inform. Systems (ICIS) (Association for Information Systems, Atlanta), https://aisel.aisnet.org/icis2016/DataScience Presentations/13/.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Xu J, Forman C, Kim JB, Van Ittersum K (2014) News media channels: Complements or substitutes? Evidence from mobile phone us age. J. Marketing 78(4):97–112.

Xu K, Chan J, Ghose A, Han S (2016) Battle of the channels: The impact of tablets on digital commerce. Management Sci. 63(5):1469–1492.

Zhang X, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601–1615.

Zhang Y, Li B, Luo X, Wang X (2019) Modeling user engagement in mobile content consumption with tapstream data and field ex periment. Inform. Systems Res. Forthcoming.

Zheng J, Qi Z, Dou Y, Tan Y (2016) How mega is the mega? Measuring the spillover effects of Wechat by machine learning and econometrics. Working paper, Krannert School of Management, Purdue University, West Lafayette, IN.
