---
otero_id: 2054
otero_key: "TQ93J75Q"
title: "Quantifying the Impact of Social Influence on the Information Technology Implementation Process by Physicians: A Hierarchical Bayesian Learning Approach"
authors: "Haijing Hao; Rema Padman; Baohong Sun; Rahul Telang"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0746"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/TQ93J75Q/fulltext/images/a6c5358cf8ac49d0d8db89431f561d1f2b4f2262cec49b81c58f238956975fb0.jpg)

# Information Systems Research

![](/api/attachments/TQ93J75Q/fulltext/images/986b4a90b6ff6db5b69f90024b49ff131034c2bcc6834b9adfe64a79e9769299.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Quantifying the Impact of Social Influence on the Information Technology Implementation Process by Physicians: A Hierarchical Bayesian Learning Approach

Haijing Hao, Rema Padman, Baohong Sun, Rahul Telang

## To cite this article:

Haijing Hao, Rema Padman, Baohong Sun, Rahul Telang (2018) Quantifying the Impact of Social Influence on the Information Technology Implementation Process by Physicians: A Hierarchical Bayesian Learning Approach. Information Systems Research

Published online in Articles in Advance 05 Feb 2018

https://doi.org/10.1287/isre.2017.0746

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/TQ93J75Q/fulltext/images/c92576d6dd19579ef760b4313fd627e4bd573300e11d70401465f0d7a05ddb14.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Quantifying the Impact of Social Influence on the Information Technology Implementation Process by Physicians: A Hierarchical Bayesian Learning Approach

Haijing Hao,<sup>a</sup> Rema Padman,<sup>b</sup> Baohong Sun,<sup>c</sup> Rahul Telang<sup>b</sup>

<sup>a</sup> Department of Management Science and Information Systems, University of Massachusetts Boston, Boston, Massachusetts 02125; <sup>b</sup> Heinz College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213; <sup>c</sup> Cheung Kong Graduate School of Business, New York, New York 10022

Contact: haĳing.hao@umb.edu, http://orcid.org/0000-0003-3071-2538 (HH); rpadman@cmu.edu (RP); bhsun@ckgsb.edu.cn (BS); rtelang@andrew.cmu.edu (RT)

Received: June 12, 2013 Revised: March 14, 2015; June 5, 2016; June 17, 2017 Accepted: June 27, 2017 Published Online in Articles in Advance: February 5, 2018

https://doi.org/10.1287/isre.2017.0746

Copyright: © 2018 INFORMS

Abstract. Technology implementation at the individual level within an organization, after the organization has adopted the technology, has been an ongoing challenge in every field. In this study, we develop a hierarchical Bayesian learning model to examine the impact of social learning, through both targeted early adopter efects and general peer efects, and experiential learning on the information technology implementation process by physicians in a community health system. Our unique data allow us to disentangle the most common and challenging endogeneity issues associated with most social influence studies. We find that the experiential learning signal is more accurate than the social learning signals in the technology implementation process; and, between the two types of social learning signals studied here, targeted early adopter efects are much more informative than general peer efects. Furthermore, we experiment with several policy simulations to illustrate and quantify the two diferent types of social influence on this implementation process. The simulation results suggest that maintaining consistency in technology usage by targeted early adopters is more efective than increasing the frequency of their technology usage in reducing their colleagues’ perceptions of uncertainty about the new technology. More specifically, we find that technology implementation probability would increase: (a) by 15%, on average, by adding a targeted early adopter to a group without early adopters; (b) by 25% by adding peer efects to solo users; and (c) by 47% by adding early adopter efects to solo users. The model can be adapted and generalized to other similar settings that examine social influence on the technology implementation process and also provide quantifiable measures of the improvements that the interventions may produce.

History: Sanjeev Dewan, Senior Editor; Anjana Susarla, Associate Editor.

Keywords: information technology implementation • social influence • early adopter efects • peer efects • social learning • experiential learning • Bayesian learning

## 1. Introduction

Many studies in the information systems (IS) literature have examined technology adoption at the organization level (Cooper and Zmud 1990, Armstrong and Sambamurthy 1999, Fichman and Kemerer 1997, Fichman 2000) and information technology (IT) implementation at the individual level (Morris and Venkatesh 2000, Kim and Son 2009, Hong and Tam 2006, Yang and Folly 2008, Duan et al. 2008). Fichman and Kemerer (1997, 1999) and Fichman (2000) also found that a key challenge has been technology assimilation that, despite the potential benefits of the new technology, many individual users may not incorporate the new technology smoothly into their daily work even after their organizations have deployed the new technology. Mishra et al. (2012) examined the assimilation of electronic health record (EHR) systems in physician practices using a motivation-ability theoretical framework. Difusion of innovation studies also pointed out that innovation diffusion within an organization is not a conventional adoption study, i.e., the decision to use an innovation, but rather an implementation study, i.e., putting an innovation into use (Zaltman et al. 1973, Rogers 2003). Thus, the present study combines these elements to develop actionable insights on how to promote technology implementation at the individual level after an organization has adopted a new technology.

Personal choice on technology adoption and implementation has been a topic of major interest to both researchers and practitioners in many fields, such as consumers’ selection of local telephone service/ wireless service in marketing research (Narayanan et al. 2007, Iyengar et al. 2007), consumers’ adoption of electronic service or automated teller machines in finance (Gowrisankaran and Stavins 2004, Yang and Ching 2014), physician adoption of diferent types of EHR systems in healthcare (Ash et al. 2003, Zheng et al. 2010, Johnson et al. 2014, Sykes et al. 2011, Davidson and Chismar 2007, Lapointe and Rivard 2007), and many others. However, healthcare IT has been the victim of a slow uptake at the individual level, where, despite a governmental or organizational push, physicians and staf have been slow to come on board and to implement or assimilate IT in their daily work for many reasons (Blumenthal 2009, Angst et al. 2010, Mishra et al. 2012, Conn 2014). Even if there is marginal adoption/implementation, there is a significant variation in actual usage (HIMSS 2010). The U.S. government’s mandates on IT use in provider organizations by ofering subsidies are one approach that has produced some results (Jamoom et al. 2012). Insurance firms also follow the carrot and stick approach to force a large takeup of eficient technologies (BCBS 2009). However, use of financial incentives is not always possible or eficient, and the actual use of various EHR functionalities, such as public health reporting, is still very low (Furukawa et al. 2014, 2015; Conn 2014). In the United States, physicians are deeply ingrained in how they run their practices, they are quite independent, and many of them have been providing care delivery in their own clinics according to their own unique way for a long time (Emanuel and Pearson 2012). Gaining their acceptance for putting into use a new IT can be very challenging (Fichman et al. 2011). Hence, the present study explores multiple mechanisms associated with technology implementation by physicians within a community health system that includes many independent clinics.

Firms engage in a variety of mechanisms like education, training, incentives, and so on to spur technology implementation, all with limited success. A key idea that has gained ground in the past decade is the concept of social influence on individuals’ product adoption or technology implementation process (Nair et al. 2010, Iyengar et al. 2011). The widely cited study on innovation difusion by Rogers (2003) states that social influence provided by early adopters or peers has the ability to significantly impact the adoption behavior of the people around them. (Early adopters in the present study refers to early adopters or implementers at the individual level, with the terms used interchangeably with early implementers hereafter.)

Studies have linked diferences in EHR use in ambulatory care with individual physicians’ perceptions of uncertainty (Lanham et al. 2014) and have shown that physicians difer in how they perceive and respond to uncertainty (Allison et al. 1998, Politi et al. 2011). Drawing on these studies, Rogers’ difusion of innovation theory (Rogers 2003), and Bandura’s social learning theory (1976), we argue that a key reason for the lack of IT implementation at an individual level in healthcare is the uncertainty surrounding the value of a new technology. We hypothesize that social influence, by early adopters and general peers, plays an important role in reducing this uncertainty during the technology implementation process.

A key challenge in estimating social influence is causal identification. Without an exogeneous variation in the data, it is very hard to causally estimate the efects of early adopters or peer learning. This is particularly challenging in a real healthcare setting where running a randomized experiment is almost impossible. In this study, we use a unique panel data set obtained from a typical American community health system to examine the social influence on the technology implementation process. This data set includes individual level data of the health system’s physicians’ technology usage behavior over approximately two years. The physician practices had diferent numbers of physicians, and a few of the practices had physician(s) who were targeted by the hospitals for adoption of new mobile technology portals and personal digital assistants (PDAs). Since the distribution of these early targeted physicians across practices was random,<sup>1</sup> it allows us to study how the early adopting physicians influenced the technology adoption of other physicians in their practice. Once we establish the efect using reduced form specification, we extend the model and build a hierarchical Bayesian learning model to elicit the underlying mechanism of how social influence impacts the reduction of uncertainty about the quality of a new technology over time. This is a new perspective in the technology implementation field. We then formulate a Bayesian learning model to quantify the impact of social influence on physicians’ technology implementation process. Our simulation results show that adding targeted early adopters to a group practice leads to this practice’s physicians increasing their technology implementation probability by 15%, on average, and adding targeted early adopter efects to solo practitioners, resulting in their average technology implementation probability increasing by 47%, which is the most striking result from our model. To a limited extent, we are also able to estimate general peer efects and find that adding a peer to a solo practice can increase the average implementation probability by as much as 25%.

The rest of the paper is organized as follows. Section 2 provides a literature review. Section 3 introduces the healthcare delivery context and the data used for this study. Section 4 develops a reduced form model, followed by a hierarchical Bayesian learning model for technology implementation applied to this study context. Section 5 discusses the results of multiple policy simulations and summarizes the insights from these experiments. Section 6 concludes with a discussion, limitations of this study, and future research.

## 2. Literature Review

Three streams of research are relevant for this study. The first is on difusion of innovations (DOIs), drawing on the work of Rogers (2003); the second is on social learning theory (Bandura 1976); and the third stream draws on the literature on physicians’ perceptions of uncertainty in a complex healthcare delivery system (Eddy 1984). We apply the Bayesian learning process to examine and quantify the impact of social influence on this uncertainty associated with the technology implementation process.

DOI originated from observing the agricultural innovation difusions in a rural community, such as the difusion of a new variety of corn, which then extended to many kinds of innovation difusions, such as new prescription drugs, consumer products, or services. These observations, methods, and practices have developed into a mature framework and the theory that has been validated across domains over the past several decades (Rogers 2003). According to Rogers (2003), innovation difusion is a process. In the context of a new technology or a new product introduction, initially people perceive using the new technology as uncertain and risky; thus, many may not adopt the new technology in the beginning. Instead, they may seek out others around them who have already adopted the innovation (the early adopters), whose input may help to reduce their uncertainty, resulting in subsequent adoption. Thus, the innovation will difuse from the early adopters to their circle of acquaintances over time. Rogers (2003) emphasizes two points for such an adoption process: first, it is a learning process over time, and second, an adoption behavior does not happen in an isolated manner but via a social system under social influence. In this context, Zaltman et al. (1973) distinguished an innovation process occurring within an organization as an implementation study, not an adoption study. They argue that the focus of an innovation difusing within an organization that has already acquired or adopted the new technology is on encouraging employees to put the technology into actual usage. This is exactly the situation in the present study, where the health system has adopted and deployed a new IT that the physicians were expected to use and incorporate into their daily work. Furthermore, Rogers (2003) also noted that with increasing use of computerized IT in organizations, digital data can be used for IT difusion studies, unlike the survey-based field studies in traditional difusion research. Accordingly, the present study uses panel data of physicians’ technology usage drawn from the server log files of the participating health system.

Another stream that is related to DOI and our study is social learning theory by Bandura (1976) from the field of psychology. It states that people will mimic the behavior of others around them with limited need for verbal communication. This is similar to the concept of trial opportunity for learning in DOI, which indicates that during the decision stage of an innovation difusion, having a trial opportunity is an important way to cope with the uncertainty about an innovation, where the trial is either by users themselves or by their peers (Rogers 2003). Furthermore, Rogers (2003) acknowledged that social learning and DOIs have much in common. Social learning theory has been applied in many deviation behavior or criminal behavior studies (Hamblin et al. 1973, 1979; Kunkel 1977; Pitcher et al. 1978; Akers 1998).

Recent research on the adoption of health information technology (HIT) by medical practices indicates that HIT adoption by practices does not necessarily lead to physicians using HIT (McClellan et al. 2013). Allison et al. (1998), Gerrity et al. (1990), and Politi et al. (2011) have demonstrated that physicians difer in their perception and response to uncertainty in a variety of clinical decision settings. Lapointe and Rivard (2005, 2007) also showed that physicians had varied technology implementation and resistance behaviors to clinical IS by case studies. The current study aims to examine and quantify how social influence may reduce physicians’ uncertainty about the new technology, thus improving EHR use over time using a Bayesian learning model.

There are many empirical studies on social influence, both peer efects and early adopter efects, on technology or product adoption (Nair et al. 2010, Van den Bulte and Lilien 2001, Iyengar et al. 2011, Lu et al. 2013, Wattal et al. 2010, Hao and Padman 2016). However, identifying the social influence on technology adoption or implementation process in an empirical setting has been extremely challenging due to the dificulty in identifying peer efects exogenously from the reference group as Manski (1993) has discussed. Since distribution of physicians who were targeted for early adoption is essentially random, our data describes a unique social system that allows us to make causal claims.

While the reduced form models are useful for identification, they do not always provide insights into the underlying mechanisms for the individual implementation process, such as how and why the technology usage happens. We construct a structural Bayesian learning model to explore how the social influence impacts the technology implementation process and thus the technology implementation behavior. Bayesian learning models have been used to investigate how advertisements, personal experience, or product price may assist consumers to solve the uncertainty about a new product, and impact consumer brand choice decision from marketing research (Erdem and Keane 1996, Mehta et al. 2008, Erdem et al. 2008). The seminal paper by Erdem and Keane (1996) assumed that when a new brand of product came to market, consumers would be uncertain about the quality of the new brand, and try to learn about the brand attributes via various signals arising from the users’ own usage experiences and advertising exposures. When consumers receive more and more signals, their uncertainty about the new products would be decreased; thus, they may learn about the true quality of the new products, which leads to a product choice decision. However, a general reduced form logit choice model does not provide this dynamic insight and merely shows that past consumption experience associates with current brand choice but not the underlying mechanism of how. The present study develops a Bayesian learning model to examine how the social learning signals and experiential signals would assist physicians to reduce their uncertainty of the new technology; thus, they could learn about the quality of the new technology, and then they would adopt or implement the new technology into their work.

Many empirical studies have used Bayesian learning models in marketing and prescription drug adoption (Narayanan et al. 2005, Ching and Ishihara 2010). However, none of these studies has incorporated or examined how social influence impact consumers’ uncertainty in this learning process, which is the focus of the present study.

## 3. Study Context and Data

The study site is a community-based healthcare system located in southwestern Pennsylvania. In partnership with about 250 physicians and nearly 4,000 other medical staf and employees, the health system ofers a broad range of medical, diagnostic, and surgical services at many medical practices and two major hospital campuses with over 500 beds, spread over a large geographic area. In June 2006, the health system deployed a mobile clinical access portal (MCAP), which is a secure, wireless, client-server solution providing physicians with online clinical data access from PDAs via a Wi-Fi connection. Physicians were provided the PDAs free of charge and were able to use them to access MCAP anywhere, anytime, at their convenience, such as in the ofice, at home, or while traveling. Physicians’ use of MCAP was completely voluntary and optional to the health system’s desktop electronic medical records (EMR) system, with no requirements or incentives for using it. All MCAP applications were accessed via menu clicks and were extremely easy to use, such as looking up patient demographics, searching for a patient, prescribing medications, ordering labs, checking lab results, etc. No complicated inputs or diagnostic features were available on this handheld device. Thus, we assume that use of the MCAP application over time primarily reflects physicians’ personal preferences, based on the utility associated with using it.

The chief information oficer (CIO) and technical staf of the community health system provided four data sets: (1) individual-level demographic data on 250 physicians; (2) data on physician practice group formation, i.e., which physicians practiced together in a medical group practice; (3) data on physicians’ MCAP usage over 22 months from the MCAP system server’s log file, extracted by the technical personnel; and (4) data on the volume of physician-patient encounters over 21 months in 4 categories—inpatient, outpatient, emergency, and ofice visits, also extracted from the server log files. Of the 250 physicians, 58 had missing demographic information or missing patient visit information; hence, it was necessary to exclude them, leaving data on 192 physicians in the merged file for the analysis reported in this study. Since almost 23% (58 out of 250) of the physicians were dropped because of incomplete data, we performed a series of t-tests for bias check. None of the checks raised any statistical concerns.

## 3.1. Important Concepts and Variables

The present study focuses on examining the impact of social influence on IT implementation within an organization; hence, understanding the organization’s social structure and how to construct the peer group is critical for identifying the social influence.

First, the social structure of this community health system is typical of the healthcare delivery setting in the United States, with many medical practices spread throughout the community, and they are physically and financially autonomous and independent entities. With clinics located quite far from one another, diferent group practices do not generally have interactions with each other, and opportunities for cross group connections are very limited. The health system does have a staf meeting each month, but the attendance rate by physicians is always quite low according to the administrators, thus potentially limiting the influence of other practices and physicians on a given clinic.

We identified targeted early adopters based on empirical data on those physicians who were given the earliest access to the new technology and implemented immediately thereafter. More specifically, after the health system adopted MCAP, those physicians who had encouraged the health system to adopt the new technology also expressed enthusiasm about trying it. Thus, they were given access to the PDA as the first users of the MCAP. Within the first two months of receiving the PDAs, their usage pattern indicated that they were not only enthusiastic but also were early implementers. Hence, we define them as the targeted early adopters.

The remaining physicians in the health system received the PDAs gradually over time after the third month. There was no clear timeline or deployment plan for when to give the PDAs to which physicians. Generally, this deployment process was a little random based on physicians’ interest or technical staf’s schedule, resulting in an unbalanced panel data of MCAP usage.

Table 1. Two Sample t-Tests for Diferences in Demographic Distributions Between Early Implementer and Nonearly Implementer Groups

<table><tr><td></td><td>Total no. of physicians</td><td>% Male</td><td>% Age ≤ 45</td><td>% Age 46–55</td><td>% Age ≥ 56</td><td>% General practice</td></tr><tr><td>Nonearly implementer group</td><td>86</td><td>0.78</td><td>0.31</td><td>0.47</td><td>0.22</td><td>0.42</td></tr><tr><td>Early implementer group</td><td>34</td><td>0.79</td><td>0.44</td><td>0.29</td><td>0.26</td><td>0.68</td></tr><tr><td>Difference</td><td></td><td>-0.01</td><td>-0.13</td><td>0.18</td><td>-0.04</td><td>-0.26</td></tr><tr><td>Pooled equal t-test</td><td></td><td>-0.18</td><td>-1.32</td><td>1.72</td><td>-0.51</td><td>-2.6</td></tr></table>

Second, the peer group formation and how the targeted early adopters are distributed across groups are critical to disentangle social influence from endogeneity efects. We empirically examined that there is no indication that the targeted early adopters are strategically distributed across group practices, because there is no association with gender, age, or medical specialty distribution, as shown in Table 1. In particular, physicians’ choice of practice group is uncorrelated with the group’s mobile technology preference or the presence of a targeted early adopter in the group because the majority of group practices were formed a long time ago, much earlier than the implementation of MCAP. Also, the practice group formation is based on physicians’ medical specialties and the size of each group is based on market demand, not on physicians’ preferences or knowledge regarding IT or interests in MCAP. Therefore, we believe that when a physician chooses a group practice, technology use (such as MCAP) is not a criterion for making this choice. In short, it is highly unlikely that a group practice will be formed on the basis of mutual technology afinity among physicians, which is a critical endogeneity issue that most social influence studies are concerned about (Manski 1993).

Third, another important concept for this research is the definition of technology implementation at the individual level, after an organization has adopted the technology (Zaltman et al. 1973; Van de Ven et al. 1989, 1999). Much research exists on technology adoption behavior using observational data that defines “the use or purchase of a new technology/product one time” as the adoption indicator (Erdem and Keane 1996, Mehta et al. 2008, Coleman et al. 1966), or conducting a survey to ask users questions on adoption or intention to adopt (Agarwal and Prasad 1997, Venkatesh 2000). In this way, we argue that the definition of technology implementation should depend on the user and technology context.

We define technology implementation in a sustainable way since many information technologies are services with anticipated long-term and repeated use, not one-time use or one-time purchase, such as online banking, a mobile app, or a teaching service website such as a Blackboard system. Hence, any user has to use the new technology, MCAP, a certain number of times within a given time period to be called implemented. Discussions with the health system administrators and conducting many exploratory trials from 25 times per month to 40 times per month helped us determine that 30 times per month was a reasonable threshold value for the implementation variable. Within a range of 25 to 40 times per month of usage, the number of users who implemented the technology (the dependent variable) does not change too much, and the model results are quite robust. Note that this quantitative definition of technology implementation can be varied across diferent technologies and diferent organizations.

Furthermore, this study only examines the physicians’ behavior up to the time when their usage reached 30 times in a month or reached the initial implementation threshold. Behavior after this initial implementation threshold will be considered long-term implementation behavior, which deserves a separate study and is beyond the scope of this paper.

## 3.2. Descriptive Statistics

For better data analysis and interpretability of results, we divided the 30 clinical specialty areas into two categories to examine and control for how medical specialty areas may afect physicians’ implementation of MCAP. The two categories are general practitioners, which include physicians from internal medicine, family practice, and pediatrics, and specialists, which include physicians from the remaining specialty areas. In addition, given the age range of this physician population, age is less likely to have a linear impact on technology implementation behavior; hence, we grouped the physicians into three reasonably evenly distributed, nominal age cohorts: under 45 years of age, between 46 and 55 years of age, and above 56 years of age for the data analysis, similar to other studies in the literature (Cooper et al. 2012). Empirical tests indicate no significant impact when age grouping changes marginally.

Tables 2 and 3 show the descriptive statistics for 18 targeted early adopters and 171 remaining physicians who practice in groups (after removing three solo practice targeted early implementers and individual physicians with missing demographic data), respectively. Based on those two tables, we observe that the physicians working in groups with targeted early adopters have a higher implementation rate (90%) than physicians working in groups without targeted early adopters (63%), and a higher rate than solo practice physicians (56%). It is also important to note that all of the targeted early adopters in this study reached the implementation threshold. Almost 90% of targeted early adopters are male and have a higher average use of MCAP and a higher average monthly volume of patient visits in every category.

Table 2. Descriptive Statistics for 171 Physician Users (No Targeted Early Adopters)

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Total implementation rate</td><td>66% (113)</td><td></td><td>Total number of users</td><td>171</td></tr><tr><td>Implementation rate by solo users</td><td>56% (29)</td><td></td><td>Number of solo users</td><td>51</td></tr><tr><td>Implementation rate by users in nontargeted early adopter group</td><td>63% (55)</td><td colspan="2">Number of users in non-targeted early adopter group</td><td>88</td></tr><tr><td>Implementation rate by users in targeted early adopter group</td><td>90% (29)</td><td colspan="2">Number of users in targeted early adopter group</td><td>32</td></tr><tr><td>Male</td><td>78%</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Age</td><td>50</td><td>9.8</td><td>30</td><td>78</td></tr><tr><td>Age 45 years and under</td><td>34.5%</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Age between 46 and 55 years</td><td>35.7%</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Age 56 years and above</td><td>29.8%</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>General practitioner</td><td>45%</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Group size</td><td>3.4</td><td>3</td><td>1</td><td>12</td></tr><tr><td>Total months of MCAP usage</td><td>15</td><td>5.2</td><td>1</td><td>20</td></tr><tr><td>Total MCAP use</td><td>796</td><td>1,857</td><td>1</td><td>13,438</td></tr><tr><td>A physician&#x27;s average monthly MCAP use</td><td>36</td><td>84</td><td>0.05</td><td>611</td></tr><tr><td>A physician&#x27;s average monthly inpatient visits</td><td>42</td><td>40</td><td>0</td><td>177</td></tr><tr><td>A physician&#x27;s average monthly outpatient visits</td><td>444</td><td>514</td><td>0</td><td>2,153</td></tr><tr><td>A physician&#x27;s average monthly physician office visits</td><td>355</td><td>435</td><td>0</td><td>2,170</td></tr><tr><td>A physician&#x27;s average monthly emergency visits</td><td>45</td><td>95</td><td>0</td><td>601</td></tr></table>

Table 3. Descriptive Statistics for 18 Targeted Early Adopters Who Practice in Groups

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Implementation rate</td><td>100% (18)</td><td>N/A</td><td>1</td><td>1</td></tr><tr><td>Male</td><td>89% (16)</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Age</td><td>49.5</td><td>6.69</td><td>39</td><td>60</td></tr><tr><td>Age 45 years and under</td><td>33% (6)</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Age between 46 and 55 years</td><td>50% (9)</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Age 56 years and above</td><td>16% (3)</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Group size</td><td>4.1</td><td>2.25</td><td>2</td><td>12</td></tr><tr><td>General practitioner</td><td>78% (14)</td><td>N/A</td><td>0</td><td>1</td></tr><tr><td>Total MCAP use</td><td>5,655</td><td>8,372</td><td>196</td><td>35,027</td></tr><tr><td>Total months used</td><td>15</td><td>5</td><td>1</td><td>20</td></tr><tr><td>A physician&#x27;s average monthly MCAP use</td><td>257</td><td>380</td><td>9</td><td>1,592</td></tr><tr><td>A physician&#x27;s average monthly inpatient visits</td><td>91</td><td>46</td><td>25</td><td>170</td></tr><tr><td>A physician&#x27;s average monthly outpatient visits</td><td>1,149</td><td>736</td><td>36</td><td>2,584</td></tr><tr><td>A physician&#x27;s average monthly physician office visits</td><td>706</td><td>589</td><td>1</td><td>1,998</td></tr><tr><td>A physician&#x27;s average monthly emergency visits</td><td>69</td><td>49</td><td>0</td><td>184</td></tr></table>

## 4. Model

## 4.1. Baseline Model

First, we construct a reduced form model to examine evidence on targeted early adopter efects on technology implementation. We specify the implementation decision as a function of physicians’ demographic characteristics, being in solo practice or group practice, the presence or absence of an early adopter in the group, and the four types of patient visit volume. The proposed model is as follows:

$$
\begin{array}{r l} \operatorname{logit} (Y _ {i}) & = \beta_ {0} + \beta_ {1} \text {Solo} _ {i} + \beta_ {2} \text { Early\_Group} _ {i} + \beta_ {3} \text { Male } _ {i} \\ & \quad + \beta_ {4} \text { Age\_45 } _ {i} + \beta_ {5} \text { Age\_55 } _ {i} + \beta_ {6} \text { General\_Practice } _ {i} \\ & \quad + \beta_ {7} \text { InPt\_v } _ {i} + \beta_ {8} \text { OutPt\_v } _ {i} + \beta_ {9} \text { PhyOff\_v } _ {i} \\ & \quad + \beta_ {1 0} \text { Emergency\_v } _ {i} + \varepsilon_ {i}. \end{array}\tag{1}
$$

$Y _ { i }$ is a binary variable, and $Y _ { i }$ equals 1 if physician i implemented the new technology during the first two years of the technology implementation, and 0 otherwise. Although our study focuses on targeted early adopter efects, we also note that some physicians are solo practitioners. Solo is 1 if physician i practices alone and 0 otherwise. Early\_Group is an indicator variable recording that physician i is in a group practice, which includes a targeted early adopter(s). Male, Age\_45, Age\_55, and General\_Practice are the indicator variables for gender, age under 45 years, age between 45 years and 55 years, and being a general practitioner. There are also four types of patient visit volume in the model, such as inpatient visit, outpatient visit, physician ofice visit, and emergency visit, which are proxies for physician i’s working environment and working load; we use the average monthly patient visit volume for each type in model (1). Error term $\varepsilon _ { i }$ includes all of the unobserved random efects. Conventionally, we assume $\varepsilon _ { i }$ follows a Gumbel distribution or type I extreme value distribution; thus, Model (1) can be estimated by logistic regression.

From the logistic regression results in Table 4, we observe that being in a targeted early adopter group has a statistically significant impact on implementation behavior. That is, if a physician practices in a group with a targeted early adopter, the physician will be about five times more likely to implement the MCAP in work than a physician practicing in a group without a targeted early adopter. Since all of the targeted early adopters implemented MCAP in their work in the first two months after they received the PDA, this indicates that targeted early adopter efects are positive. Solo practitioners seem to be less likely to implement the new technology compared to the physicians practicing in a group without targeted early adopters, but it is not statistically significant. Other demographic variables and patient visit volume variables in the model are not statistically significant either.

Although the logit regression model shows that targeted early adopters’ presence has a positive efect on physician’s technology implementation, the dynamic implementation process over time is still an unknown black box. Thus, we develop a new model to further explore the underlying mechanism of this black box in Section 4.2.

## 4.2. A Choice Model with Learning

Intuitively, a rational person’s decision to use a new technology depends on the utility of the technology, and the utility of the technology depends on the quality of the technology (Erdem and Keane 1996, Roberts and Urban 1988).

However, the true quality of a new technology is not observable. We assume that a technology or a product has a true quality, α, which is unobservable but does exist. Furthermore, through direct experience or secondhand experience, users can obtain more information about the technology and learn about the true quality of the technology over time. Since users cannot acquire the true quality immediately, we let $A _ { i t }$ denote the experienced quality of the new technology that is perceived by user i at time period t. The experienced quality, $A _ { i t } ,$ of the new technology has some variability, or randomness, around the true quality for a couple of reasons. First, the technology itself may have hardware or software quality issues with imperfect attributes, leading to variability or random shock. Second, users’ subjective feelings about using the new technology may not be exactly the same each time they use it, and some random shocks may exist also. Therefore, the experienced quality, $A _ { i t } ,$ is a random variable around the true quality of the new technology, α, with the noisy variance $\sigma _ { i t } ^ { 2 }$ (the construction of this noisy variance will be shown in Section 4.3).

Following Erdem and Keane (1996), we assume the utility of using this new technology can be approximated by a quadratic functional form of technology’s experienced quality. More specifically, we assume a physician user $i \prime \mathrm { s }$ utility function at time period t for using a new technology can be expressed as follows:

Table 4. Logistic Regression Result for Targeted Early Adopter Efects on Technology Implementation

<table><tr><td>Dependent = Implementation</td><td>Odds ratio</td><td colspan="2">95% Wald confidence limit</td></tr><tr><td>Solo users</td><td>0.985</td><td>0.431</td><td>2.248</td></tr><tr><td>Users in targeted early adopter groups</td><td>4.963*</td><td>1.325</td><td>18.591</td></tr><tr><td>Male</td><td>2.204</td><td>0.881</td><td>5.516</td></tr><tr><td>Age under 45 years old</td><td>1.815</td><td>0.733</td><td>4.492</td></tr><tr><td>Age between 46 and 55 years old</td><td>1.294</td><td>0.556</td><td>3.014</td></tr><tr><td>General practitioner</td><td>1.359</td><td>0.568</td><td>3.253</td></tr><tr><td>A physician&#x27;s average monthly inpatient visit</td><td>0.997</td><td>0.982</td><td>1.012</td></tr><tr><td>A physician&#x27;s average monthly outpatient visit</td><td>1.000</td><td>0.999</td><td>1.002</td></tr><tr><td>A physician&#x27;s average monthly physician office visit</td><td>1.000</td><td>0.999</td><td>1.001</td></tr><tr><td>A physician&#x27;s average monthly emergency patient visit</td><td>0.998</td><td>0.994</td><td>1.003</td></tr><tr><td></td><td>-2 log L</td><td></td><td>200.063</td></tr><tr><td></td><td>AIC</td><td></td><td>222.063</td></tr><tr><td>Model fit statistics</td><td>Pseudo-R square</td><td></td><td>0.1051</td></tr></table>

Notes. The data size for this regression is N <sup></sup> 171. The practice group reference is solo practice physicians; the age reference group is the 56 years and older group.  
<sup>∗</sup>Statistically significant at 5%.

$$
\begin{array}{r} U _ {i t} = A _ {i t} - r _ {i} \cdot A _ {i t} ^ {2} + \beta_ {1} \cdot I n \_ P _ {i t} + \beta_ {2} \cdot O u t \_ P _ {i t} \\ + \beta_ {3} \cdot P h y \_ P _ {i t} + \beta_ {4} \cdot E m \_ P _ {i t} + \varepsilon_ {i t}, \end{array}\tag{2}
$$

where $A _ { i t }$ is the experienced quality of the new technology perceived by physician user i at time period t. The coeficient of its squared term, $\boldsymbol { r } _ { i } ,$ is the risk coeficient for physician $i ,$ and its sign will be estimated by the data. In this Model (2) structure, a preassigned negative sign in front of the r means that if the estimated $r _ { i }$ is positive, then the physician i is risk averse, and if negative, then risk seeking. The real sign of $r _ { i }$ is independent of which way we structure the Model (2). Variables In\_P, Out\_P, Phy\_P, and Em\_P are the number of inpatient visits, outpatient visits, physician ofice visits, and emergency visits of physician i at time period $t ,$ and $\beta ^ { \prime } \mathbf { s }$ are their coeficients, respectively. We include these variables to take into account the physicians’ work environment and workload, which may afect the user’s utility as well. The $\varepsilon _ { i t }$ is a random shock known only to the user.

The expected utility to user i from using the new technology at time period t is

$$
\begin{array}{r l} & E [ U _ {i t} ] = E [ A _ {i t} ] - r _ {i} \cdot (E [ A _ {i t} ]) ^ {2} - r _ {i} \cdot \sigma_ {i t} ^ {2} + \beta_ {1} \cdot I n \_ P _ {i t} \\ & \qquad + \beta_ {2} \cdot O u t \_ P _ {i t} + \beta_ {3} \cdot P h y \_ P _ {i t} + \beta_ {4} \cdot E m \_ P _ {i t} + \varepsilon_ {i t}. \end{array}\tag{3}
$$

Again, if $r _ { i } > 0 .$ , the technology utility will be concave in $A _ { i t } ,$ or users will be risk averse; if $r _ { i } < 0 .$ , then the technology utility will be convex, and users will be risk seeking; if $r _ { i } = 0 .$ , then the utility function will be reduced to a linear form (which is usually unrealistic). Thus, our model allows users to make the usage decision based on their utility with regard to the new technology as well as the user’s risk attitude.

However, the critical point of model (3) is how to formulate the experienced technology quality, $A _ { i t } ,$ as a time varying variable, which also can incorporate users’ dynamic learning process over time.

## 4.3. Experiential Learning and Social Learning via a Bayesian Learning Process

4.3.1. Bayesian Learning Process. We assume that users are Bayesian learners, not memoryless. Hence, eliciting the experienced technology quality by physicians can be formulated via a Bayesian learning process.

A Bayesian learning process assumes that the true quality value, α, of a new technology or a product is unlikely to be known at the beginning of its availability, resulting in user’s uncertainty regarding the technology’s value (Erdem and Keane 1996). However, users can learn, via a Bayesian updating mechanism, about the true quality of this new technology over time through exposure to various signals, thus reducing the uncertainty about the quality. Usually, when a user is introduced to a new technology, before using it, she may have some general expectation about the value or the “quality” of this new technology, which is called prior belief. Then, as time goes by, the user may learn more about the new technology via various information sources, or signals, at a certain time period (time period t), and will update the user’s prior belief about the technology’s quality to a new level based on those signals; this new level is referred to as the posterior belief. This posterior belief at the end of time period t will be a prior belief for the next time period $t + 1$ . Thus, this learning-updating-learning cycle can be repeated again and again. Over time, while the total noisy variance keeps decreasing, the user’s belief about the new technology quality will converge to the true “quality value,” α. Also, the time efect of Bayesian learning is naturally built into the user’s perception of the new technology. Conceptually, this Bayesian learning process is also consistent with Rogers’ framework of innovation difusion theory that technology adoption starts from early adopters to others in a social network (Rogers 2003).

Based on the above concept, we formulate the Bayesian learning process mathematically as follows. At the beginning of period 1, all users start with a prior belief about the quality of the new technology, $A _ { 0 } ,$ which is normally distributed with mean $\alpha _ { 0 }$ and variance $\sigma _ { 0 } ^ { 2 }$

$$
\text { Prior: } \quad A _ {0} \sim N (\alpha_ {0}, \sigma_ {0} ^ {2}).\tag{4}
$$

Over subsequent time periods t $( t = 1 , 2 , \ldots , n )$ , user i receives one or more signals about the quality of the new technology. In the present research context, we assume that users can update their belief based on experiential learning signals from their personal exposure to the technology and social learning signals from observing the technology usage behavior of the targeted early adopters and general peers. We assume that targeted early adopters and general peers may have different impacts on physicians’ learning, but the reality depends on the model result, which is also our study focus. Specifically, the three signals are as follows: an intrinsic signal 1 (experiential learning efects), $S _ { i t 1 } ;$ an extrinsic signal 2 (general peer efects), $S _ { i t 2 } ;$ and another extrinsic signal 3 (targeted early adopter efects) for user i at time period t. All these signals provide some noisy information around the true quality, $\alpha ,$ with random errors, $Q _ { i t 1 } , Q _ { i t 2 } ,$ and $Q _ { i t 3 } ,$ respectively (as modeled in (5), (5’), and $( 5 ^ { \prime \prime } )$ . To simplify the Bayesian updating mechanism, we also assume that all three noise categories follow normal distributions with mean zero and variances $\sigma _ { \varsigma 1 } ^ { 2 } , \ \sigma _ { \varsigma 2 } ^ { 2 } ,$ and $\sigma _ { \varsigma 3 } ^ { 2 }$ from experiential learning, peer efect learning, and targeted early adopter efect learning, respectively, which reflect the fact that the signals around the product quality of a user’s experience are not precise. Hence, users’ perceived quality distributions mixed with the signals around the true quality value, $\alpha ,$ are denoted as shown in (6), (6’), and (6”)

Noise 1 distribution: $Q _ { i t 1 } \sim N ( 0 , \sigma _ { \varsigma 1 } ^ { 2 } ) ,$

(5)

$$
\text { Signal   1: } S _ {i t 1} = \alpha + Q _ {i t 1}, S _ {i t 1} \sim N (\alpha , \sigma_ {\varsigma 1} ^ {2}),\tag{6}
$$

Noise 2 distribution: $Q _ { i t 2 } \sim N ( 0 , \sigma _ { \odot 2 } ^ { 2 } ) ,$

$$
\text { Signal   2: } S _ {i t 2} = \alpha + Q _ {i t 2}, S _ {i t 2} \sim N (\alpha , \sigma_ {\varsigma 2} ^ {2}),\tag{6'}
$$

Noise 3 distribution: Q<sub>it3</sub> <sup>∼</sup> N<sup>(</sup>0, σ<sup>2 )</sup>,

(5”)

$$
\text { Signal   3: } S _ {i t 3} = \alpha + Q _ {i t 3}, S _ {i t 3} \sim N (\alpha , \sigma_ {\varsigma 3} ^ {2}).\tag{6"}
$$

Since both the prior belief (4) and the signals ((5), (5’), and $( 5 ^ { \prime \prime } ) )$ follow normal distributions, the posterior belief of the quality of this new technology at the end of time period $t , A _ { i t } ,$ is also normally distributed with a mean $\alpha _ { i t }$ and variance $\sigma _ { i 1 } ^ { 2 }$ (DeGroot 1970), as shown in (7)–(9)

$$
A _ {i t} \sim N (\alpha_ {i t} \sigma_ {i 1} ^ {2}),\tag{7}
$$

$$
\begin{array}{r} \alpha_ {i t} = \alpha_ {i, t - 1} + D _ {i t 1} \cdot \beta_ {i t 1} (S _ {i t 1} - \alpha_ {i, t - 1}) \\ + D _ {i t 2} \cdot \beta_ {i t 2} (S _ {i t 2} - \alpha_ {i, t - 1}) + D _ {i t 3} \cdot \beta_ {i t 3} (S _ {i t 3} - \alpha_ {i, t - 1}) \end{array}
$$

$$
\mathrm{with} \beta_ {i t 1} = \frac {\sigma_ {i t} ^ {2}}{\sigma_ {i t} ^ {2} + \sigma_ {\varsigma 1} ^ {2}}, \beta_ {i t 2} = \frac {\sigma_ {i t} ^ {2}}{\sigma_ {i t} ^ {2} + \sigma_ {\varsigma 2} ^ {2}},
$$

$$
\mathrm{and} \beta_ {i t 3} = \frac {\sigma_ {i t} ^ {2}}{\sigma_ {i t} ^ {2} + \sigma_ {\varsigma 3} ^ {2}},\tag{8}
$$

$$
\sigma_ {i t} ^ {2} = 1 \cdot \left(\frac {1}{\sigma_ {0} ^ {2}} + \frac {\sum_ {\tau = 1} ^ {t} D _ {i \tau 1}}{\sigma_ {\varsigma 1} ^ {2}} + \frac {\sum_ {\tau = 1} ^ {t} D _ {i \tau 2}}{\sigma_ {\varsigma 2} ^ {2}} + \frac {\sum_ {\tau = 1} ^ {t} D _ {i \tau 3}}{\sigma_ {\varsigma 3} ^ {2}}\right) ^ {- 1}.\tag{9}
$$

Here $D _ { i t 1 }$ is an indicator of how many instances of signal 1 a user actually received. If user i received n instances of signal 1 at time period $t ,$ then $D _ { i t 1 }$ will be n $( n = 1 , 2 , \ldots )$ . Otherwise, $D _ { i t 1 }$ will be $0 ,$ and the mean of prior belief and the variance of the prior belief will not be updated for the corresponding terms as Equations (8) and (9) show. The same logic applies to $D _ { i t 2 }$ and $D _ { i t 3 }$ . The posterior information for time period $t ,$ as models $( 7 ) - ( 9 )$ show, is also the prior information for time period $t + 1$ . The same Bayesian mechanism can be iterated repeatedly until convergence to the true value of quality. Over an extended number of periods, the noisy variance, or the uncertainty about the quality of the new technology, will reduce to zero, and the user will get to understand the true quality.

A user’s previous month’s usage is assumed to be a proxy for the experiential learning signal, indicating how many experiential learning signals the user receives. That is, if a user tries the PDA a few times in a previous time period, then those experiential learning signals will assist her to learn about MCAP via her own experience, which may afect her perception of the quality of the new technology, thus afecting usage in the current time period. Furthermore, in addition to experiential learning, a physician user also learns about the new technology through social learning, observing their social peers’ technology usage if they have any, which we call social learning efects. We assume that the instances of social learning signal from targeted early adopters can be represented by the total number of times the technology was used by the targeted early adopters in the same time period. Finally, to avoid an endogeneity issue associated with peers’ usage, we assume that the previous month’s technology usage by peer physicians is the proxy for the peer efect signal, as a previous study did (Sorensen 2006). Targeted early adopters are exogenous, so we do not have the endogenous issue.

4.3.2. User Heterogeneity. Building on the research associating physicians’ perceptions regarding uncertainty and risk to EHR use (Lanham et al. 2014), we expect users’ attitudes to risk to vary across users. We allow the risk coeficient, $\boldsymbol { r } _ { i } ,$ to be explained by a combination of the observed individual demographic characteristics and the unobserved individual heterogeneity across users. More specifically, we introduce individual-level risk perception into the model with a hierarchical Bayesian structure (Rossi et al. 2006), as shown below

$$
\begin{array}{c} r _ {i} = \partial_ {i} + \delta_ {1} \cdot M a l e _ {i} + \delta_ {2} \cdot A g e _ {i} \\ + \delta_ {3} \cdot G e n e r a l P r a c t i t i o n e r _ {i} + e _ {i}. \end{array}\tag{10}
$$

The demographic variables such as gender/male, age, and general practitioner capture the observable risk perception. If the estimated $\delta _ { 1 }$ is positive, it means that male physicians are more risk averse than female physicians (because we constructed risk aversion as the default in the utility function). The intercept, $\partial _ { i }$ is estimated for physician i, which captures the unobserved heterogeneity of each physician.

For estimation simplicity, the random shock $\varepsilon _ { i t } ,$ in model (3) is assumed to follow i.i.d. Gumbel distribution. Thus, the choice probability for implementing the new technology (or using up to 30 times in a month) for user i at time t is a typical logit function of the form

$$
P _ {i t} = \frac {e ^ {E [ U _ {i t} ]}}{1 + e ^ {E [ U _ {i t} ]}}.\tag{11}
$$

Based on Equation (11), a Bayesian estimation algorithm is used to estimate this Bayesian learning model, incorporating a demographic heterogeneous risk coefficient.

## 4.4. Empirical Results

4.4.1. Bayesian Estimation. Identification and estimation issues in the evolution of learning parameters in a Bayesian learning model have been challenging because of its diferent perspective from conventional regression models (Erdem and Keane 1996, Narayanan et al. 2005, Erdem et al. 2008). From a pure Bayesian conjugate family of distributions’ perspective, as long as the total number of learning time periods is large enough, or users receive enough learning signals, regardless of the initial values of the prior distribution, the posterior distribution will converge to the true distribution (DeGroot 1970).

We estimate the parameters of the Bayesian learning model, with a hierarchical structure for users’ risk coefficients, using a Markov Chain Monte Carlo method (Gelman et al. 2004, Rossi et al. 2006), diferentiating this study from prior research from a methodological perspective. The Bayesian estimation procedure is executed for 20,000 iterations, and the first 10,000 iterations are regarded as the burn-in period. For generating the posterior distributions, we use 20 as the thinning interval. The upper graph in Figure 1 displays the rejection rate of the Metropolis–Hastings algorithm (Rossi et al. 2006). Every 20th draw is retained for analysis. The rejection rate gets stable and within a reasonable range as Figure 1 shows. The lower graph in Figure 1 displays the log likelihood values of the data evaluated at posterior draws of individual level estimates, where every 20th draw is again retained for analysis.

4.4.2. Parameter Estimates. Table 5 presents the average posterior means and posterior standard deviations for the estimated parameters of the Bayesian learning model. These parameters include the experiential learning variance $\mathsf { \widehat { \Pi } } ( \sigma _ { \varsigma 1 } ^ { 2 } )$ , the peer efect variance $( \sigma _ { c 2 } ^ { 2 } ) _ { . }$ the targeted early adopter efect variance $( \sigma _ { \zeta 3 } ^ { 2 } )$ , the mean quality of the new MCAP technology (α), the heterogeneous risk coeficient $( r _ { i } )$ with demographic characteristics at the individual level, and the covariance for random efects $r _ { i } ~ ( V _ { \beta } )$ . First, we see that the experiential learning efect signal variance is the smallest or the most accurate signal, followed by the targeted early adopter efect signal, then the peer efect signal. This result is consistent with our expectation because people generally trust their own experiences (experiential learning) more than the signals from others, either general peers or targeted early adopters. Furthermore, our model result shows that between the targeted early adopters’ signals and general peer colleagues’ signals, people are more likely to trust targeted early adopters’ signals than general peer colleagues’ signals, which is also consistent with our expectation and literature regarding targeted early adopters; people seek advice from early adopters (Rogers 2003). Note that all signal variance parameters are values relative to the initial variance, and the absolute values do not have literal meanings but only ordinal meaning.

Figure 1. (Color online) MCMC Estimation of Hierarchical Bayesian Learning Model  
![](/api/attachments/TQ93J75Q/fulltext/images/0232dfc337dc40ee523cb67666ec88016c61916e989afc7999d3f2535455a729.jpg)

Outpatient visit and physician ofice visit are positively correlated with the utility of using the new technology, which indicates that the higher the volume of patient visits, the more likely the physician is to implement the new technology. This result may suggest that the new mobile technology is helpful for physicians who have many patient visits in those two clinical settings. Inpatient visit is negatively correlated with the utility of using the new technology, which indicates that physicians may use the new technology less when they see their inpatients, probably because they are more familiar with their patients who have had surgery or specific medical procedures by them, and there is no need to use this mobile PDA to look up the patient information. Also, the higher the volume of emergency patient visits, the less likely the physician is to implement the new technology. This is likely due to the nature of care delivery in the emergency setting where patients need physicians’ immediate attention with physical evaluation and urgent action; thus, there is limited time to search and review patient data, if the system has any data about the patient, from the MCAP system.

There is substantial heterogeneity across individual users as seen in the risk-aversion coeficient, even after controlling for demographic variables, which is consistent with prior studies (Lanham et al. 2014). Among the demographic groups, male users are less risk averse than female users, and they more actively seek to try MCAP. Users in the age group under 45 years are less risk averse than users in the group of 56 years old and above, which is consistent with previous research that the younger users are more likely to accept new IT than the older users (Yang and Folly 2008). Also, general practitioners are slightly more risk averse than specialists in using this new technology, which is at variance with the results of survey-based research (McClellan et al. 2013). Still, the largest impact on the risk coeficient is the intercept, which indicates that heterogeneity is strong across users. The covariance of the heterogeneous risk coeficient is also rather significant, which is another indicator of the heterogeneity across the individual users. To our knowledge, these results provide the first quantitative evidence of the differences in perceptions of uncertainty among physician users of HIT.

Table 5. Estimated Bayesian Learning Model Parameters

<table><tr><td>Parameter</td><td></td><td>Posterior mean</td><td>Posterior std. dev.</td></tr><tr><td>Experiential learning signal variance</td><td> $\sigma_{c1}^{2}$ </td><td>2.591</td><td>11.764</td></tr><tr><td>Peer effect signal variance</td><td> $\sigma_{c2}^{2}$ </td><td>40.391</td><td>41.296</td></tr><tr><td>Targeted early adopter effect signal variance</td><td> $\sigma_{c3}^{2}$ </td><td>20.923</td><td>33.615</td></tr><tr><td>Technology true mean quality</td><td> $\alpha$ </td><td>2.186</td><td>0.173</td></tr><tr><td>Physician office visits</td><td>Phy</td><td>0.249</td><td>0.133</td></tr><tr><td>Inpatient visits</td><td>Inp</td><td>-0.261</td><td>0.328</td></tr><tr><td>Outpatient visits</td><td>Outp</td><td>0.604</td><td>0.288</td></tr><tr><td>Emergency visits</td><td>Emp</td><td>-0.142</td><td>0.250</td></tr><tr><td>Heterogeneous risk aversion</td><td> $r_{i}$ </td><td>1.307</td><td>0.908</td></tr><tr><td colspan="4">Heterogeneous risk coefficient</td></tr><tr><td>Intercept</td><td></td><td>1.690</td><td>0.198</td></tr><tr><td>Age  $\leq$  45</td><td></td><td>-0.320</td><td>0.129</td></tr><tr><td>Age between 46 and 55</td><td></td><td>0.130</td><td>0.123</td></tr><tr><td>General practice</td><td></td><td>0.002</td><td>0.159</td></tr><tr><td>Male</td><td></td><td>-0.424</td><td>0.127</td></tr><tr><td>Covariance</td><td> $V_{\beta}$ </td><td>0.996</td><td>0.136</td></tr><tr><td>Model fit statistics</td><td> $-\log L$ </td><td>345.448</td><td></td></tr></table>

Note. The reference gender group is female; the reference age group is the group with age above 56 years old; the reference group for medical practice is the specialists group.

## 5. Discussion

The hierarchical Bayesian learning model that we have developed and estimated in this paper provides interesting insights on how experiential learning and social learning reduce uncertainty associated with a new technology over time. Nominally, the experiential learning signal is a more accurate signal, but it is always challenging to encourage the efect of experiential learning because it requires every physician to use the new technology. Thus, it is less practical than encouraging the efect of social learning, which means that we can first promote the new technology among a group of physicians, targeted early adopters, to encourage them to implement the new technology first. Once the targeted early adopters implement the new technology, they will influence their colleagues to use the new technology in a natural setting. In this context, it is useful to understand how much a targeted early adopter can afect their colleagues’ learning of the new technology and their implementation behavior. However, the Bayesian learning model cannot be interpreted directly as the coeficients of conventional regression models do, because either experiential learning efect variance or social learning efect variance is not observable directly. Thus, we execute a series of policy simulations based on the Bayesian learning model to quantify the social influence, particularly the targeted early adopter efects and peer efects. A distinct advantage of the structural Bayesian learning model in comparison to the conventional reduced form model is the ability to exercise policy simulations (Erdem and Keane 1996) because Bayesian learning model estimates users’ utility function, which does not change with the input variables; thus, the policy simulation results are reliable.

If we look at the Bayesian learning model carefully, we can see that a user’s Bayesian learning process about the new technology can be afected by both the technology use frequency (observable directly) and the signal variance (not observable directly). Particularly, the signal variance is a special estimate obtained from the Bayesian learning model only. Thus, we experiment with a few policy simulations to demonstrate the impact of social influence on physician users’ technology implementation. We simulate how changes in the targeted early adopters’ (1) technology use frequency and (2) signal variance may impact users’ technology implementation probability. Furthermore, we also simulate the impact of (3) adding targeted early adopter efects to groups without targeted early adopters, and (4) adding peer efects or (5) targeted early adopter efects to solo practitioners on the users’ implementation probability.

## 5.1. Policy Simulations and Results

In this section, we examine the above five distinct simulation scenarios to quantify social influence, in the form of targeted early adopter efects and general peer efects, on physicians’ technology implementation. Does increasing usage of the technology by targeted early adopters increase the likelihood of implementation of the technology by physicians who work around the early adopters? For each policy simulation, we estimate both the new implementation probability and the reduced uncertainty (or learning variance) over time. In summary, all our policy simulations resonate with previous studies in marketing; for example, on how TV commercials (another kind of social influence) impact consumers’ learning about a new brand (Erdem and Keane 1996).

Figure 2. (Color online) Simulation: Implementation Probability When Targeted Early Adopters’ Use Increase by 10 Instances per Time Period (Increased 2% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/4416896134496008bc60c21ce771bc09e8f51ef3979f20b3af54754e9e0043be.jpg)

## 5.2. Leveraging Social Influence on Group Practitioners

5.2.1. Increasing the Technology Use Frequency. Increasing the observable technology use frequency by targeted early adopters is simulated for two scenarios: an increase in MCAP use by 10 instances in each time period versus doubling the MCAP usage in each time period, by all early adopters. Figures 2 and 4 display the simulation results for the physicians’ implementation probability. The solid line is the original aggregated MCAP implementation probability by physicians who had targeted early adopters in their group practices; the dashed line is the simulated aggregated MCAP implementation probability of the same physicians under the simulated scenarios: targeted early adopters increase MCAP usage by 10 instances and doubling the MCAP usage in each time period. Both results show that the simulated implementation probabilities by physicians increased over the 20 months by a modest 2% and 2.7%, respectively, on average. These are neither notable nor significant. Figures 3 and 5 show the simulated targeted early adopter efects on physicians’ learning variance, or the uncertainty associated with the quality of the new technology, over time. From a modeling perspective, uncertainty is the learning variance. The smaller the variance is, the smaller the uncertainty is. Both figures indicate that physicians’ uncertainty with the new technology decreased over time at a slightly higher rate than under the original usage levels, but not significantly.

Figure 3. (Color online) Simulation: Learning Variance When Targeted Early Adopters’ Use Increased by 10 per Time Period (Decreased by 7% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/f66c6ff7559e9c9f9ba0cf024ac0019dc6b55aa073f5e8c46cb7f8f577a9dc4c.jpg)

Figure 4. (Color online) Simulation: Implementation Probability When Targeted Early Adopters’ Use Doubled per Time Period (Increased 2.7% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/cef4c6e34597eac582287d98d7c91efea7dd704a67873fd5f29d03ba178d6208.jpg)

5.2.2. Increasing the Technology Use Consistency. As mentioned earlier, an important advantage of a Bayesian learning model is that it specifically estimates the unobservable signal variances, such as experiential learning signal variance and social learning signal variance. In the present simulation, we examine changes in the user’s implementation probability when their targeted early adopters give more consistent (or precise) signals (means smaller variance). For example, the health system may suggest that targeted early adopters behave more consistently when they use the new technology to help the physicians around them to reduce the uncertainty or to learn about the new technology, thus leading to a higher implementation probability of the new technology.

Figure 5. (Color online) Simulation: Learning Variance When Targeted Early Adopters’ Use Doubled per Time Period (Decreased by 9% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/470adb1ba72823517034ab1544fc31e0563b1065dfb79ad72be85e5ea41a1a19.jpg)

Figure 6. (Color online) Simulation: Implementation Probability When Targeted Early Adopter’s Variance Increase by 50% per Time Period (Increased 11.6% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/eab2302fe928388a6890183bbeb130fb120f7f3579313f6508c1f198eb8f3d08.jpg)

Figures 6 and 7 display the simulation results for implementation probability change and learning signal variance change when the variability in targeted early adopter signal is decreased by 50% from current levels. We observe that the users’ aggregate implementation probability increases significantly—by 11.6% on average over the 20 time periods, and the average learning variance decreases by 35% on average over the same time periods. This suggests that if targeted early adopters adjust their signals (which are supposed to include both actual technology usage behavior and other verbal communications) to be more consistent, or less variable, their physician colleagues’ uncertainty about the new technology will decrease faster, resulting in quicker learning about the new technology, and a higher likelihood of implementation. This finding, thus, has a very practical policy implication. Contradicting the common belief that the more targeted early adopters use the technology, the more people around them would be influenced, our simulations suggest that increasing usage frequency (giving more signals randomly) is far less efective than maintaining the usage consistency (giving consistent or precise signals).

5.2.3. Adding a Targeted Early Adopter. Thus far, we have simulated the impact of targeted early adopters’ technology use behaviors, such as the use frequency and use consistency, on their physician colleagues’ implementation probability and learning variance over time. However, what would be the impact if an organization is able to add or train a targeted early adopter in a group that currently does not have a targeted early adopter? Figures 8 and 9 display the impact of adding simulated targeted early adopters (using 30 instances per targeted early adopter in each time period, which meets the implementation criterion) to groups that were originally without early adopters. We observe that the average implementation probability (the figure ignores the first two time periods when no regular physicians are using the technology) increased by 15%, and the average learning variance decreased by 26%, a significant improvement from status quo. This may be due to two possible reasons. First, adding a targeted early adopter introduces a key signal of influence to physician users who had no targeted early adopters in their groups. Second, since we add the technology use frequency by the simulated targeted early implementer evenly to each time period for simulation, which means that the simulated targeted early adopter’s use is consistent over time, this consistency will also increase the implementation probability, as we discussed in the previous simulation.

Figure 7. (Color online) Simulation: Learning Variance When Targeted Early Adopter’s Variance Decreased by 50% (Decreased by 35% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/242a85345e374269884c22288c9b4d2ac303b5249ddf0af894f6d815c656cb4c.jpg)

## 5.3. Leveraging Social Influence on Solo Practitioners

Recent surveys indicate that the number of solo practices in the United States has been steadily declining over the past few decades, dropping from about 40%

Figure 8. (Color online) Simulation: Implementation Probability When Adding a Targeted Early Adopter to Groups Without Targeted Early Adopter (Increased 15% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/82ad8870371aaead1fa28be5587de6f4b7f9ea2e22f92c07bdd37a92f88c104a.jpg)

Figure 9. (Color online) Simulation: Learning Variance When Adding a Targeted Early Adopter to Groups Without Targeted Early Adopter (Decreased by 26% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/1e74c96c1471967ab6bdbbb8e2a64be07dc1bdb27f243c6efe46a0738f526fb8.jpg)

30 years ago to 30% in 1994, 25% in 2012, and 17% in 2014, with physicians joining group practices or loosely formed networks, or seeking hospital employment (The Physicians Foundation 2014). Motivated by this development, we explore how healthcare organizations may leverage peer efects or targeted early adopter efects in promoting IT implementation among their solo practices by forming them into groups.

5.3.1. Adding a General Peer to a Solo Practice. Our simulation assumes that each solo user is now in a group practice with a simulated physician, a general peer, who uses 12 instances of the new technology each month (which is the average monthly usage by a solo physician). Figures 10 and 11 indicate the simulated impact of adding peer efects to the original solo practices. Again, the increased implementation probability on average is 25%, and decreased learning variance or uncertainty on average is 61%, which are much larger when compared to the status quo.

5.3.2. Adding a Targeted Early Adopter to a Solo Practice. Figures 12 and 13 show the simulated impact of adding targeted early adopter efects (using 30 instances in each time period by the simulated early adopter) to the original solo practices. The averaged implementation probability increases by 47% and the averaged learning variance decreases by 78% over time, which is further improved from the solo setting and group setting without targeted early adopters. This is also consistent with the model results of estimated targeted early adopter signal variance and peer efect signal variance, where targeted early adopter signals are more informative than the peer efect signals; hence, it has a greater impact in reducing uncertainty regarding the true value of the technology, thus increasing the implementation probability.

Figure 10. (Color online) Simulation: Implementation Probability When Adding a Peer to Solos (Increased 25% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/a5223fb0eb7475388e6fde90fa5a5f2e6e1acec0c99671d1e73cb40dc78cb0d2.jpg)

Figure 11. (Color online) Simulation: Learning Variance When Adding a Peer to Solos (Decreased by 61% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/3699a8df7db8d2d2c2cde17406a0a438703e737762b3c1fb4f4885f88a5ff54c.jpg)

Figure 12. (Color online) Simulation: Implementation Probability When Adding a Targeted Early Adopter to Solos (Increased 47% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/568ab80eda1acb4a577316e02aab8d5e7c5e0d584cf87ec6baaa4db90cca899d.jpg)

Figure 13. (Color online) Simulation: Learning Variance When Adding a Targeted Early Adopter to Solos (Decreased by 78% on Average)  
![](/api/attachments/TQ93J75Q/fulltext/images/ff4f169946a0fede469af7197e774bd2e8e46aa7b52caf7da4ad36cb6c39935d.jpg)

## 6. Conclusions

Building on the literature on technology implementation from difusion of innovation, social learning theory, and perceptions of uncertainty reduction experienced by end users, this study makes several contributions in explaining the underlying dynamic mechanism of learning of a new information technology by physicians. First, to our knowledge, this is the first study that draws on three diverse theoretical perspectives to formulate a hierarchical Bayesian learning model to investigate the technology dynamic implementation process at the individual level. We use panel data to elicit the underlying mechanism of how social influence impacts the uncertainty reduction over time by incorporating social learning and experiential learning signals to the uncertainty decreasing process, thus enabling the users to learn about the quality of the new technology in the technology implementation process. Second, we quantify social influence on the technology implementation process using policy experiments. The simulation results show that social learning signals from targeted early adopters are much stronger than the social learning signals from general peer efects. Finally, this paper also quantitatively diferentiates targeted early adopter efects and general peer efects within the same context, which has not been examined by other studies to date.

This study provides a few policy implications. The first is how to leverage social influence, particularly in comparison to experiential learning, to encourage technology implementation at the individual level within an organization. Experiential learning is more challenging to influence than social learning because experiential learning requires that each and every user be targeted with appropriate strategies for improving technology implementation. For example, if an organization wants to encourage experiential learning, they may need to develop an organization-wide campaign to encourage everyone to use the new technology. Yet the success of a campaign to influence everyone or even a majority is doubtful. However, social influence is relatively easy to be leveraged because targeted early adopters are a small fraction of the entire user population; hence, it is more practical for an organization to target just this small group of early adopters. Once the targeted early adopters implement the new technology, they are more likely to subsequently influence their colleagues and promote the new technology implementation as a natural progression, as our study shows. Therefore, although targeted early adopter signals are less efective than the experiential learning signals, targeted early adopter efects are a practical lever to be used for promoting technology implementation, which is the focus of this research.

Furthermore, our policy simulations suggest that targeted early adopters’ consistent signals are much more efective than frequent use of the technology. This is a useful new perspective on targeted early adopter efects. This simulation result has a very practical policy implication that when an organization educates the targeted early adopters for technology implementation, they should advise those targeted early adopters that consistent technology usage behavior signals are more efective than merely increasing usage at random, which is similar to what marketing research has shown (Erdem and Keane 1996).

Empirically, our policy simulations quantify and demonstrate social influence, both targeted early adopter efects and general peer efects, in several ways: (a) adding a targeted early adopter to a group without targeted early adopters can potentially increase the group users’ technology implementation probability by 15%, on average; (b) adding peer efects to solo users may increase the average technology implementation probability by 25%; and (c) adding targeted early adopter efects to solo users may further increase the average technology implementation probability by 47%, compared to the original situations. These results suggest that social influence is a strong and practical approach for technology implementation. Even without special training or treatment, assembling solo users into groups can increase the technology implementation probability of solo users. Furthermore, if an organization invests in training targeted early adopters, then the implementation probability of users around those targeted early adopters will also increase. Finally, the model and policy interventions examined in this study should be generalizable to other settings that examine social influence in the context of technology implementation and provide quantifiable measures of the improvements that the interventions can produce.

This research has some limitations. First, due to data limitations, the model only includes experiential learning and social learning signals to represent a user’s learning process associated with a new IT, which may not represent reality. Future studies could collect and incorporate more learning signals and use more accurate learning signal proxies, such as training sessions, self-learning hours, and direct interactive conversations with colleagues or early adopters to develop a more comprehensive model and results. Second, we do not have access to the exact workload or working environment information of the physicians, but instead we use the number of patient visits as the workload and use the type of patient visit as the working environment indicator. This may not be completely accurate and may vary by physical location in the community, physicians’ personal choice (such as inpatient or outpatient practice), demographics of the patient population, or medical specialties. Third, we simplify the social interactions such that targeted early adopter efects and general peer efects are only within the physicians’ practice group, not across the groups, due to a lack of access to the necessary information. Yet we believe that cross group influence is quite minor, as we discussed earlier. A future study could construct a more accurate social network of the organization to investigate the broader impact of social influence, including both the professional network and personal friendship network, on technology implementation. Also, the assumption that every user is a Bayesian learner may be somewhat strong. Some people may be forgetful sometimes; thus, they do not learn about a new technology using Bayesian updating all of the time. Yet since we have the entire physician population of the community health system, this assumption is reasonable for the majority of physicians. Last, a future study that investigates users’ learning behavior at the post initial implementation stage with a longer technology learning process is warranted and may be another research opportunity to pursue.

## Acknowledgments

The authors thank the community health system for providing the data used for this study.

## Endnote

<sup>1</sup> More precisely it is uncorrelated with the regression error term. The physicians who were targeted were no diferent from any other physicians in the practice on any observable characteristics.

## References

Agarwal R, Prasad J (1997) The role of innovation characteristics and perceived voluntariness in the acceptance of information technologies. Decision Sci. 28:557–582.

Akers RL (1998) Social Learning and Social Structure: A General Theory of Crime and Deviance (Northeastern University Press, Boston).

Allison JJ, Kiefe CI, Cook EF (1998) The association of physician attitudes about uncertainty and risk taking with resource use in Medicare HMO. Medical Decision Making 18:320–329.

Angst CM, Agarwal R, Sambamurthy V, Keley K (2010) Social contagion and information technology difusion: The adoption of electronic medical records in U.S. hospitals. Management Sci. 56(8):1219–1241.

Armstrong CP, Sambamurthy V (1999) Information technology assimilation in firms: The influence of senior leadership and IT infrastructures. Inform. Systems Res. 10(4):304–327.

Ash JS, Stavri PZ, Dykstra R, Fournier L (2003) Implementing computerized physician order entry: The importance of special people. Internat. J. Medical Informatics 69:235–250.

Bandura A (1976) Social Learning Theory (Prentice-Hall, Englewood Clifs, NJ).

BCBS (2009) 5 reasons to love electronic health records. https:// www.bcbsri.com/learn-insurance-basics/topic/5-reasons-love -electronic-health-records.

Blumenthal D (2009) Stimulating the adoption of health information technology. New England J. Medicine 360:1477–1479.

Ching A, Ishihara M (2010) The efects of detailing on prescribing decisions under quality uncertainty. Quant. Marketing Econom. 8:123–165.

Coleman J, Ktaz E, Menzel H (1966) Medical Innovation, A Difusion Study (Bobbs-Merrill Company, Inc., Indianapolis).

Conn J (2014) EHR adoption rate slows, with physicians facing big hurdles for meeting Stage 2, survey finds. Modern Healthcare (January 20), http://www.modernhealthcare.com/ article/20140120/NEWS/301209957/ehr-adoption-rate-slows -with-physicians-facing-big-hurdles-for.

Cooper CP, Gelb CA, Rim SH, Hawkins NA, Rodriguez JL, Polonec L (2012) Physicians who use social media and other Internet-based communication technologies. J. Amer. Medical Inform. Assoc. 19(6):960–964.

Cooper RB, Zmud RW (1990) Information technology implementation research: A technological difusion approach. Management Sci. 36(2):123–139.

Davidson EJ, Chismar WG (2007) The interaction of institutionally triggered and technology-triggered social structure change: An investigation of computerized physician order entry. MIS Quart. 31(4):739–758.

DeGroot MH (1970) Optimal Statistical Decisions (McGraw-Hill, New York).

Duan W, Gu B, Whinston AB (2008) Informational cascades and software adoption on the Internet: An empirical investigation. MIS Quart. 33(1):23–48.

Eddy DM (1984) Variations in physician practice: The role of uncertainty. Health Afairs 3:74–89.

Emanuel EJ, Pearson SD (2012) Physician autonomy and health care reform. JAMA 307(4):367–368.

Erdem T, Keane MP (1996) Decision-making under uncertainty: Capturing dynamic brand choice processes in turbulent consumer goods markets. Marketing Sci. 15(1):1–20.

Erdem T, Keane MP, Sun B (2008) A dynamic model of brand choice when price and advertising signal product quality. Marketing Sci. 27(6):1111–1125.

Fichman R (2000) The difusion and assimilation of information technology innovations. Zmud RW, ed. Framing the Domains of IT Management: Projecting the Future Through the Past (Pinnaflex Educational Resources, Inc., Cincinnati), 105–128.

Fichman R, Kemerer C (1997) The assimilation of software process innovations: An organizational learning perspective. Management Sci. 43(6):1345–1363.

Fichman R, Kemerer C (1999) The illusory difusion of innovation: An examination of assimilation gaps. Inform. Systems Res. 10(3):255–275.

Fichman R, Kohli R, Krishnan R (2011) The role of information systems in healthcare: Current research and future trends. Inform. Systems Res. 22(3):419–428.

Furukawa MF, King J, Patel V (2015) Physician attitudes on ease of use of EHR functionalities related to meaningful use. Amer. J. Managed Care 21(12):e684–e692.

Furukawa MF, King J, Patel V, Hsiao C, Adler-Milstein J, Ashish J (2014) Despite substantial progress in EHR adoption, health information exchange and patient engagement remain low in ofice settings. Health Afairs 33(9):1672–1679.

Gelman A, Carlin JB, Stern HS, Rubin DB (2004) Bayesian Data Analysis, 2nd ed. (Chapman & Hall/CRC, Boca Raton, FL).

Gerrity MS, DeVellis RF, Earp JA (1990) Physicians’ reactions to uncertainty in patient care. A new measure and new insights. Medical Care 28(8):724–736.

Gowrisankaran G, Stavins J (2004) Network externalities and technology adoption: Lessons from electronic payments. RAND J. Econom. 35:260–276.

Hamblin RL, Jacobson RB, Miller JL (1973) A Mathematical Theory of Social Change (Wiley, New York).

Hamblin RL, Miller JLL, Saxton DE (1979) Modeling use difusion. Soc. Forces 57(3):799–811.

Hao H, Padman R (2016) An empirical study of opinion leader efects on mobile technology implementation by physicians in an American community health system. J. Health Informatics, ePub ahead of print December 21, https://doi.org/10.1177/1460458216675499.

HIMSS (2010) Essentials of the U.S. hospital IT market, 6th ed. HIMSS Analytics, Chicago.

Hong SJ, Tam KY (2006) Understanding the adoption of multipurpose information appliances: The case of mobile data services. Inform. Systems Res. 17(2):162–179.

Iyengar R, Ansari A, Gupta S (2007) A model of consumer learning for service quality and usage. J. Marketing Res. 44(4):529–544.

Iyengar R, Van den Bulte C, Valente TW (2011) Opinion leadership and social contagion in new product difusion. Marketing Sci. 30(2):195–212.

Jamoom E, Beatty P, Bercovitz A, Woodwell D, Palso K, Rechtsteiner E (2012) Physician adoption of electronic health record systems: United States, 2011. NCHS Data Brief. 98:1–8.

Johnson MP, Zheng K, Padman P (2014) Modeling the longitudinality of user acceptance of technology with an evidence-adaptive clinical decision support system. Decision Support Systems 57: 444–453.

Kim SS, Son JY (2009) Out of dedication or constraint? A dual model of post-adoption phenomena and its empirical test in the context of online service. MIS Quart. 33:49–70.

Kunkel JH (1977) The behavioral perspective of social dynamics. Hamblin R, Kunkel JH, eds. Behavioral Theory in Sociology: Essays in Honor of George C. Homans (Transaction Books, New Brunswick, NJ), 433–468.

Lanham HJ, Sittig DF, Leykum LK, Parchman ML, Pugh JA, McDaniel RR (2014) Understanding diferences in electronic health record (EHR) use: Linking individual physicians’ perceptions of uncertainty and EHR use patterns in ambulatory care. J. Amer. Medical Inform. Assoc. 21(1):73–81.

Lapointe L, Rivard S (2005) A multilevel model of resistance to information technology implementation. MIS Quart. 29(3):461–491.

Lapointe L, Rivard S (2007) A triple take on information system implementation. Inform. Systems Res. 18(1):89–107.

Lu Y, Jerath K, Singh P (2013) The emergence of opinion leaders in a networked online community: A dyadic model with time dynamics and a heuristic for fast estimation. Management Sci. 59(8):1783–1799.

Manski C (1993) Identification of endogenous social efects: The reflection problem. Rev. Econom. Stud. 60:531–542.

McClellan S, Casalino LP, Shortell SM, Rittenhouse DR (2013) When does adoption of health information technology by physician practices lead to use by physicians within the practice? J. Amer. Medical Informatics Assoc. 20(e1):e26–e32.

Mehta N, Chen X, Narasimhan O (2008) Informing, transforming, and persuading: Disentangling the multiple efects of advertising on brand choice decisions. Marketing Sci. 27(3):334–355.

Mishra AN, Anderson C, Angst CM, Agarwal R (2012) Electronic health records assimilation and physician identity evolution: An identity theory perspective. Inform. Systems Res. 23(3-part-1):738–760.

Morris M, Venkatesh V (2000) Age diferences in technology adoption decisions: Implications for a changing work force. Personnel Psych. 53:375–403.

Nair HS, Manchanda P, Bhatia T (2010) Asymmetric social interactions in physician prescription behavior: The role of opinion leaders. J. Marketing Res. 47(5):883–895.

Narayanan S, Chintagunta PK, Miravete EJ (2007) The role of selfselection, usage uncertainty and learning in the demand for local telephone service. Quant. Marketing Econom. 5:1–34.

Narayanan S, Manchanda P, Chintagunta PK (2005) Temporal diferences in the role of marketing communication in new product categories. J. Marketing Res. 42(3):278–290.

Pitcher BL, Hamblin RL, Miller JLL (1978) The difusion of collective violence. Amer. Sociol. Rev. 43:23–25.

Politi MC, Clark MA, Ombao H (2011) The impact of physicians’ reactions to uncertainty on patients’ decision satisfaction. J. Evaluation Clinical Practice 17:575–578.

Roberts JH, Urban GL (1988) Modeling multi-attribute utility, risk, and belief dynamics for new consumer durable brand choice. Management Sci. 34(2):167–185.

Rogers EM (2003) Difusion of Innovations, 5th ed. (Free Press, New York).

Rossi PE, Allenby G, McCulloch R (2006) Bayesian Statistics and Marketing (John Wiley & Sons, West Sussex, UK).

Sorensen AT (2006) Social learning and health plan choice. RAND J. Econom. 37(4):929–945.

Sykes TA, Venkatesh V, Rai A (2011) Explaining physicians’ use of EMR systems and performance in the shakedown phase. J. Amer. Medical Informatics Assoc. 18:125–130.

The Physicians Foundation (2014) 2014 survey of America’s physicians: Practice patterns and perspectives. Accessed May 1, 2016, http://www.physiciansfoundation.org/uploads/default/ 2014\_Physicians\_Foundation\_Biennial\_Physician\_Survey\_Report .pdf.

Van de Ven AH, Angle HA, Poole MS, eds. (1989) Research on the Management of Innovation: The Minnesota Studies (Ballinger/Harper and Row, New York).

Van de Ven AH, Polley DE, Garud R, Venkataramam S (1999) The Innovation Journey (Oxford University Press, New York).

Van den Bulte C, Lilien G (2001) Medical innovation revisited: Social contagion versus marketing efort. Amer. J. Sociol. 106(5): 1409–1435.

Venkatesh V (2000) Determinants of perceived ease of use: Integrating control, intrinsic motivation, and emotion into the technology acceptance model. Inform. Systems Res. 11(4):342–365.

Wattal S, Racherla P, Mandviwalla M (2010) Network externalities and technology use: A quantitative analysis of intraorganizational blogs. J. Management Inform. Systems 27(1):145–174.

Yang B, Ching A (2014) Dynamics of consumer adoption of financial innovation: The case of ATM cards. Management Sci. 60(4): 903–922.

Yang K, Folly LD (2008) Age cohort analysis in adoption of mobile data services: Gen Xers versus baby boomers. J. Consumer Marketing 25:272–280.

Zaltman G, Duncan R, Holbek J (1973) Innovations and Organizations (John Wiley and Sons, New York).

Zheng K, Padman P, Krackhardt D, Johnson M (2010) Social networks and physician adoption of electronic health records: Insights from an empirical study. J. Amer. Medical Informatics Assoc. 17(3):328–336.
