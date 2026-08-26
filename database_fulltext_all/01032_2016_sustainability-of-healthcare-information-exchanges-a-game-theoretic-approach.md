---
otero_id: 1032
otero_key: "CYEN9VEX"
title: "Sustainability of Healthcare Information Exchanges: A Game-Theoretic Approach"
authors: "Emre M. Demirezen; Subodha Kumar; Arun Sen"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0626"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/CYEN9VEX/fulltext/images/877df5d307b2ed0175f9f548630cab04535e299a4d1c84ed86d2c45dba2e451a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Sustainability of Healthcare Information Exchanges: A Game-Theoretic Approach

Emre M. Demirezen, Subodha Kumar, Arun Sen

To cite this article:

Emre M. Demirezen, Subodha Kumar, Arun Sen (2016) Sustainability of Healthcare Information Exchanges: A Game-Theoretic Approach. Information Systems Research 27(2):240-258. http://dx.doi.org/10.1287/isre.2016.0626

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/CYEN9VEX/fulltext/images/a5f6bc57ca57dbb387d2e0377d9083c9f05b0f6fd6d3271003e2b1b110bffef0.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Sustainability of Healthcare Information Exchanges: A Game-Theoretic Approach

Emre M. Demirezen

School of Management, Binghamton University, State University of New York, Binghamton, New York 13902, edemirez@binghamton.edu

Subodha Kumar, Arun Sen

Mays Business School, Texas A&M University, College Station, Texas 77843 {skumar@mays.tamu.edu, asen@mays.tamu.edu}

ased on our interactions with the key personnel of three different healthcare information exchange (HIE) providers in Texas, we develop models to study the sustainability of HIEs and participation levels in these networks. We first examine how heterogeneity among healthcare practitioners (HPs) (in terms of their expected benefit from the HIE membership) affects participation of HPs in HIEs. We find that, under certain conditions, low-gain HPs choose not to join HIEs. Hence, we explore several measures that can encourage more participation in these networks and find that it might be beneficial to (i) establish a second HIE in the region, (ii) propose more value to the low-gain HPs, or (iii) offer or incentivize value-added services. We present several other interesting and useful results that are somewhat counterintuitive. For example, increasing the highest benefit the HPs can get from the HIE might decrease the number of HPs that want to join the HIE. Furthermore, since the amount of funds from the government and the other agencies often changes (and will eventually cease), we analyze how the changes in the benefit HPs obtain from the HIE affect (i) participation in the network, (ii) the HIE subscription fee and the fee for value-added service, (iii) the number of HPs that request value-added service, and (iv) the net values of the HIE provider and HPs. We also provide guidelines for policy makers and HIE providers that may help them improve the sustainability of HIEs and increase the participation levels in these networks

Keywords: healthcare management; HIE networks; network externalities; game theory

History: Kai-Lung Hui, Senior Editor; Giri Kumar Tayi, Associate Editor. This paper was received on November 24, 2014, and was with the authors 6 months for 2 revisions. Published online in Articles in Advance May 3, 2016.

The promise of health information exchanges is not in question, but whether they can be sustained and thrived is.

—Douglas Page, “Health Information Exchanges Hold Promise, Pose Perils” (2010, p. 12)

## 1. Introduction

Healthcare spending in the United States is increasing rapidly. In 2012, it grew 3.7% to reach \$2.8 trillion, or around \$9,000 per person (Centers for Medicare and Medicaid Services 2014). More importantly, healthcare spending accounted for 17.2% of the nation’s gross domestic product in 2012. Therefore, the national effort on healthcare is becoming more pronounced to reduce costs and increase the quality of the system (Menon et al. 2000, Agarwal et al. 2010c, Aron et al. 2011, Menon and Kohli 2013). There are numerous reasons for high healthcare spending, such as overuse and misuse of diagnostic testing and emergency department services, avoidable hospitalization and rehospitalization, and fragmented information infrastructure or technology that supports patient care (Bohmer 2011, Weinberger 2011, Mishra et al. 2012). In this paper, we focus and study the dynamics of the healthcare information exchange (HIE) networks that relieve the problems due to the fragmentation of patient healthcare records or information. Patient health records are fragmented because patients tend to move from one healthcare practitioner (HP) to another, but their records do not move. Therefore, the U.S. government has been incentivizing HIEs to connect HPs effectively (Walker et al. 2005, Adler-Milstein et al. 2011, Hall 2013).

Because of the inherent benefits of HIE networks, spending to establish such networks has increased dramatically. According to a Black Book HIE survey, the industry spending was expected to triple by 2014 (PRWeb 2012). In this survey, 84% of the executives indicated that they were actively discussing regional alignment and solution purchases to address stakeholder interoperability—in particular HIEs. Despite their promise, HIEs are still far from meeting the expectations (Agarwal et al. 2010a). Some of the barriers that hinder extracting the full potential of HIE services are willingness to share information or privacy concerns (Angst and Agarwal 2009, Anderson and Agarwal

2011), adoption and network effects (Agarwal et al. 2010c; Romanow et al. 2012; Yaraghi et al. 2013, 2014), problems in governmental regulations (Ozdemir et al. 2011), and, maybe more importantly, sustainability and other financial factors (Fontaine et al. 2010, Terry 2013). The growth and the success of these HIE networks depend heavily on the decisions taken by the HIE providers and HPs (Walker et al. 2005). Agarwal et al. (2010b) argue that the longevity of HIEs is in question without government support, and they state that offering value-added services is one of the possible business strategies that can help sustain a healthy HIE. Hence, HIEs around the United States focus on how to financially sustain their operations (Hall 2013).

In this paper, we analyze the sustainability of HIEs (with a focus on participation levels) and derive the equilibrium behaviors of an HIE provider and the HPs in a game-theoretic setting. Our proposed model is primarily based on our interactions with a number of HIEs in Texas (Calhoun 2013, Samuels 2013, Smitherman 2013). In §1.1, we briefly discuss some preliminaries and the background of HIEs.

## 1.1. Preliminaries and the Background of HIEs

HIEs can be defined as information-sharing technologies or mechanisms that automate the transfer and sharing of health-related information typically stored in multiple organizations, while maintaining the context and integrity of the information being exchanged (Healthcare Information and Management Systems Society 2009a). An HIE provides access to and retrieval of patient information to authorized users to provide safe, efficient, effective, and timely patient care. HIEs are typically formed by a group of participants from a specific area or a region. A true HIE involves multidirectional flows of information electronically among HPs such as hospitals, physicians, clinics, labs, etc. Furthermore, an HIE is not only about moving clinical information to the right place; it also affects the clinical workflows by making the data available to doctors and nurses when they need them to make decisions. Thus, it provides improved patient safety by sharing their medical data. In addition, cost reductions due to HIEs include the elimination of duplicate tests; recovery of missing patient health data; elimination of paper, ink, and manual document printing; and reduction of phone calls and follow-ups with labs for test results. An HIE assures a strong chain of custody of patient data and their movements. It also helps in providing accurate feedback to public health registries (Fontaine et al. 2010). Finally, participating in HIEs is a requirement for HPs to receive stimulus funds (Page 2010).

The HIEs got their start in the early 1990s when the healthcare industry set up community health information networks to share patient medical records among HPs (see Figure 1). These networks were encumbered by pre-Internet connectivity costs and did not live up to expectations (Lorenzi 2003). Some, however, have endured and are still in operation, such as the Indiana Health Information Exchange (IHIE), the Utah Health Information Network (UHIN), and Health-Bridge in Cincinnati, Ohio. The current era of HIEs began in earnest in 2004 with the creation of the Office of National Coordinator (ONC) by the Department of Health and Human Services (HHS). Since then, as Figure 1 illustrates, HIE development has been encouraged by the federal government with many nationwide projects like the Nationwide Health Information Network (NHIN or NwHIN), which has since taken the name eHealth Exchange; the Meaningful Use Incentives program from the Center of Medicare and Medicaid Services (CMS), the Regional Extension Center (REC) program, and the State HIE Cooperative Agreement program (Kolkman and Brown 2011). According to the eHealth Initiative report, there were a dozen HIE initiatives in 2004, but this number grew to approximately 255 by 2011. More importantly, this number was expected to grow significantly after 2012 (PRWeb 2012). Next, we discuss the research questions that we study in this paper along with our contributions.

## 1.2. Research Questions and Contributions

There has been substantial progress in making HIEs a reality that will benefit patients and HPs (Agency for Healthcare Research and Quality 2006). However, challenges and barriers remain—most notably funding, sustainability, and adoption levels (Healthcare Information and Management Systems Society 2009b, Agarwal et al. 2010b, Sridhar et al. 2012). Hence, HIEs in the United States need to focus on financially sustaining their operations (Hall 2013). In general, HIEs can be not for profit, public utility, physician collaborative, or for profit (Berry and Johnson 2012). However, to remain or become sustainable, especially after the governmental funds cease, all HIEs strive or will have to strive to maximize their profits. Therefore, independent of their nature, we regard HIEs as profit-maximizing organizations in our research.

Most of the well-established HIEs and some of the newly established HIEs offer value-added services. Hence, our main model enables us to examine the dynamics of an HIE network (i.e., sustainability and participation levels) in which the HIE provider offers value-added services in addition to the base HIE connectivity. We also consider a special case of our model (referred to as the benchmark case) where we assume that the HIE provider does not offer value-added services, but just the base HIE connectivity. This model represents business practices of most of the newly established HIEs since they usually do not offer valueadded services. In our main model (and its benchmark case), we use a game-theoretic framework to derive how the HIE provider should set the membership fee and the characteristics of HPs that join the HIE.

Figure 1 HIE Landscape  
![](/api/attachments/CYEN9VEX/fulltext/images/466e56014821c7ea203c06b56188e9b571af89b4f3dd9afa462739bb91bfb8bd.jpg)

After characterizing the solution, we first find that the cost of accommodating each HP in the HIE has the most important role in determining whether an HIE should be established or not. We then ask and answer the following question: How does heterogeneity among HPs (in terms of their expected benefit from the HIE membership) affect participation levels if the HIE is established, and what other factors impact the extent of participation? Our results show that if the cost of accommodating each HP in the HIE is not prohibitive or if there is enough government support (so that the HIE is established), the heterogeneity among the HPs plays a big role in determining the extent of participation. More specifically, in general, heterogeneity among HPs decreases the number of participating HPs, and full participation is not possible if the heterogeneity is high. We also find that some low-gain HPs choose not to join the HIE if there are more high-gain HPs in the region.<sup>1</sup>

Hence, we analyze the following important question: What could be done to increase the participation level in an HIE? We find that the policy makers and the HIE provider may employ different strategies to encourage participation. First, the minimum benefit the HPs can obtain from joining the HIE could be increased. For example, if small HPs do not have functional electronic health record (EHR) systems, HIE providers might offer EHR applications for free or at a discount. In the United States, several HIE providers are currently offering this incentive. However, we find that these incentives cannot entice all HPs to join the network if the heterogeneity among the HPs is high. Contrary to intuition, as the maximum benefit the HPs can obtain from the HIE increases, participation in the HIE might be lower in some cases. The second possible strategy for increasing the participation is establishing more than one HIE. In some scenarios, establishing a second HIE in the same region (where one of them focuses more on the low-gain HPs) entices more HPs to join these HIEs. Hence, there might be an incentive for policy makers to establish more than one HIE in the same region. The third option for the HIE providers is to offer HIE related value-added services. Offering valueadded services is the main difference between our main model and the benchmark case. Hence, comparing them provides several useful insights regarding the benefits and management of value-added services. In particular, we derive how the HIE provider decides on the level of the value-added service and its fee, and which HPs request this service. This analysis also helps us outline the conditions under which the network expands because of the value-added service.

Finally, there is another critical issue that we focus on in this paper: the amount of funds available from the government and other agencies often changes and will eventually cease. Therefore, we ask the following question: How does the changes in the benefit HPs obtain from the HIE affect (i) the participation in the network, (ii) the HIE subscription fee and the fee for value-added services, (iii) the number of HPs that request the value-added service, and (iv) the net values of the HIE provider and the HPs? In addition, we present several other insights that may be useful for the HIE provider, the HPs, and the policy makers. In §1.3, we review the related literature and highlight our contributions with respect to past studies.

## 1.3. Literature Review

Our study is broadly related to two streams of literature: (i) HIE research and (ii) network externalities/platform adoption. Since 2010, several case studies (Fontaine et al. 2010, Feldman et al. 2013), progress reports (Agarwal et al. 2010b), white papers (Covich et al. 2011), and surveys (Patel et al. 2012, PRWeb 2012) have been published regarding different aspects of HIEs. As discussed in these studies, key benefits for HPs from joining an HIE include facilitation of compliance with state and federal mandates, cost savings, and improved quality of patient care (Fontaine et al. 2010, Joshi 2010). The HIE literature further discusses how the values gained from the HIE can be converted to a sustainable business model for HIE providers (Marchibroda 2007). In this paper, we analyze whether the benefits of joining the HIE outweigh the costs involved in a setting with multiple HPs. We also analyze the effect of value-added services on the participation in the HIE network and on the net values of the HIE provider and the HPs. We formulate our model based on the HIE literature and our interactions with different HIE providers.

There are two other streams of research in the HIE literature. The first stream is related to the HIE policy. HIE policies are dependent on government requirements for different types of reporting, such as those required by the CMS. Interested readers can refer to Marchibroda (2007), Adler-Milstein et al. (2011), and Adjerid et al. (2011) for details. The second HIE research stream studies the technical aspect of networks and is not directly related to our study. Interested readers can refer to the representative papers by Lorenzi (2003) and Vest and Jasperson (2010).

Network effect or network externality implies that the value of a product or service (sometimes through adoption of a platform) depends on the total number of users. For an extensive review of network effects and competition, see Farrell and Klemperer (2007). Literature on network externalities and platform adoption focuses on switching costs, lock-in effects, or competition among different platforms, each of which displays network effects. In this literature, users can usually adopt only one network out of all networks. Hence, the focus is on (i) which platform or network product dominates and (ii) whether competition allows excess profits to network owners or increases values of consumers. Unlike most of the past studies, our focus is on participation levels in the network under different conditions.

Furthermore, in classic network externality models, the network externality is equally valuable to all customers. In particular, customers are assumed to have homogeneous network valuations although they have heterogeneous product valuations (Fudenberg and Tirole 2000, Jing 2007, Prasad et al. 2010, Niculescu et al. 2012). In some models, product valuations and the benefits customers obtain from the network are correlated (e.g., Sundararajan 2003, 2004). In particular, a customer with a high (respectively, low) product or service valuation also has a high (respectively, low) valuation for the network. Our paper is similar to the latter group of papers since the types of HPs determine both their valuation of the HIE membership and the valuation of the HIE-related value-added services. However, our paper is unique in the sense that we have two simultaneous network externalities, in particular, one because of base HIE services and the other because of HIE related value-added services. In addition, the membership to the value-added service network requires membership for the HIE network. Another different aspect of our model is that the HIE provider can determine the level of value-added service it will offer to its participants. To our knowledge, none of the past studies analyzes two simultaneous network externalities where one of them requires membership to the other, and the optimization of the level of service offered to the participants in the second network.

The rest of this paper is organized as follows. In §2, we present the details of two representative HIEs that form the underpinnings of our model and its benchmark case. Next, in §3, we present the formulation of our model. In §4, we present the solutions of our model and its benchmark and provide useful managerial insights. Finally, §5 summarizes the implications for HIE providers, HPs, and the policy makers.

## 2. HIE Scenarios

We present our main model and its benchmark case in §3. In formulating our model, we worked with several HIE providers to understand the critical issues involved in their sustainability. In our main model, the HIE provider offers value-added services related to HIE in addition to the base HIE service. This business practice is prevalent among well-established HIEs, as in the case of Integrated Care Collaboration (ICC) and Critical Connection, which are based in Texas. In the benchmark case, the HIE provider offers the base HIE service, but not the value-added services. Most of the newly established HIE providers follow this practice and focus only on the base service, as in the case of a start-up HIE Southeast Texas Health Systems (SETHS). For our modeling purpose, ICC and Critical Connection are similar in nature, and therefore we provide the details of only ICC and SETHS. Although our model is developed in the context of these HIEs, many HIE providers in the nation either have plans for offering or already offer HIE related value-added services. However, some of the HIE providers focus only on the base HIE services (especially, in the case of newly established HIEs), and therefore we study this business setting in the benchmark case in §3.2. Hence, our model is generic, and the results as well as insights are applicable to most of the HIE settings.

## 2.1. An HIE Provider That Offers Value-Added Services: ICC

Integrated Care Collaboration<sup>2</sup> is an established HIE that is located in Central Texas and dedicated to the collection, analysis, and sharing of health information. The primary objective of ICC is to create and operate a regional HIE that is sufficiently trusted and valued by the stakeholders to enable improved care coordination and a foundation for sustainability. ICC includes around 70 hospitals and 5,600 physicians located in Central and Eastern Texas. ICC, established in 2002, uses a web-based community health record called ICare that stores patient demographic and encounter information. Recently, ICare 2.0 was launched based on an opensource HIE technology that is accessible through a webbased portal. The redesigned ICare solution integrates a robust open-source HIE platform that includes an interface, integration, a clinical data repository, and a master patient index with data warehousing solutions. The portal provides access to an aggregate patient medical record to the participating HPs. The ICare system is being further extended by custom Java and web-based development efforts provided by Centex System Support Services that was formed to operate as the technology arm of ICC. The combination of open source technologies and in-house development expertise not only reduces short-term and long-term development, maintenance, and operational costs but also facilitates ICC’s ability to offer additional services to the interested participating HPs in its network.

As most of the HIE organizations like ICC mature, they provide other value-added services in addition to the base HIE functionality (Agarwal et al. 2010b, Covich et al. 2011). As discussed earlier, the base HIE subscription and the value-added services offer two simultaneous network externalities for the participating HPs. To increase their net value that would help them sustain their businesses, the HIE providers need to strategically set the fee for joining the HIE, the price of the value-added service, and the level of the valueadded service (Agarwal et al. 2010b, Samuels 2013, Smitherman 2013). A higher subscription fee and/or fee of the value-added service (or a reduced level of service) increases the marginal revenue of the HIE provider, but may decrease the number of HPs that decide to join the HIE or the number of HPs that request the value-added service. This effect may be amplified because of the network externalities. Hence, the HIE provider needs to obtain the equilibrium values of (i) the subscription fee, (ii) the price of the value-added service, and (iii) the level of the valueadded service, such that its net value is maximized considering the effects of two simultaneous network externalities.

In §2.2, we briefly discuss a newly established HIE provider, SETHS.

## 2.2. An HIE Provider That Focuses on Base Service: SETHS

The Southeast Texas Health Systems<sup>3</sup> is a start-up HIE, which is a cooperation of rural hospitals in Southeast Texas. One of the main objectives of SETHS is to implement and sustain an HIE among healthcare practitioners to ultimately improve the health status of the population in Southeast Texas. SETHS’s plan is to develop and operate a high-quality, cost-effective healthcare data exchange system for small and rural HPs. Other goals include (i) supporting interoperability with the eHealth Exchange, (ii) supporting core components of an interoperable HIE, (iii) assisting in the exchange of health and personal information from disparate source systems, (iv) developing a permissions and messaging infrastructure that allows stakeholder access to data in compliance with all applicable privacy/security and standards regulations, (v) aiding the continuity of patient care by facilitating referrals and transitions of care between HPs, and finally (vi) aligning with the statewide healthcare infrastructure in Texas. According to the executive director of SETHS, such an HIE will provide the following benefits to its members: (i) create incentives to share data with other HPs, (ii) improve the ability to negotiate reimbursements by demonstrating evidence-based clinical decision support, and (iii) provide capacity to develop protocols and goals for outcomes (Calhoun 2013).

The technical architecture of the HIE operated by SETHS (called SOPHIE) is based on an open-source HIE gateway called HIEOS that supports core HIE services for its members like patient management, record locator provision, repository management, crosscommunity shared patients locator facility, and secured and encrypted communication. An application integration platform mechanism is also used to interface with EHR systems in member hospitals. SOPHIE currently does not have additional service offerings, such as e-prescribing or patient management tools. Rather, they focus only on base HIE service. This practice is common among most of the start-up HIEs (Calhoun 2013).

The start-up HIE providers, such as SETHS, need to maximize their net value to improve sustainability (Calhoun 2013). They achieve this objective by setting the subscription fee appropriately. A higher subscription fee increases the marginal revenue for the HIE provider, but it decreases the number of HPs that decide to join. Furthermore, the more participants in the HIE, the more beneficial the HIE becomes to participating HPs because there is additional information to share. Hence, the HIE provider needs to obtain the equilibrium subscription fee such that its net value is maximized considering the effect of network externality. As we discuss in detail later, the benchmark case presented in §3.2 represents the business practices of most startup HIEs like SETHS since they usually do not offer value-added services.

## 3. Model

In line with the first HIE scenario discussed in §2.1, here we consider that the HIE provider offers HIE-related value-added services to the participating HPs if they request them. Value-added services can range from e-prescribing to patient management tools (Covich et al. 2011). We analyze the equilibrium behavior of HPs and the HIE provider in this environment. In particular, we are interested in the optimal level of value-added service that the HIE provider should offer, the equilibrium network size, the number of HPs that request the value-added service, the subscription fee of the base HIE service, the price of the value-added service, and the conditions that would help the valueadded service increase the network size. We denote the total number of potential HPs that consider joining the HIE by N . These include hospitals, laboratories, family practice clinics, wellness centers, rehab centers, and federally qualified health centers.

## 3.1. Details of the Main Model

The net benefit of an HP from joining the HIE (that excludes the benefits from value-added services) is the difference between the gains and the costs of joining the HIE (adjusted to a month). As discussed earlier, different benefits of the base HIE service include improved patient safety; cost reductions due to elimination of duplicate tests; recovery of missing patient health data;

elimination of paper, ink, and manual document printing; and reduction of phone calls and follow-ups with labs for test results. In addition, participation in HIEs is a requirement for HPs to receive stimulus funds from the government (Page 2010). It is possible to categorize the benefits as operational and quality benefits as well as the monthly portion of the long-term funds and reimbursements awarded by the federal government and other agencies (Dixon et al. 2010). On the other hand, the costs include the average monthly cost of purchases and maintenance of equipment; IT infrastructure, including the cost of interface construction; and personnel training.

Before joining the network, all HPs can estimate the net benefit using the methodologies mentioned in the HIE value analysis literature (e.g., Walker et al. 2005). If there are more participants in the network, there is additional information to share, and therefore the HIE membership becomes more valuable to its members. Hence, the benefit any HP expects from the collaboration increases in the network size and is proportional to the number of participating HPs in the network (Calhoun 2013). Therefore, given that the average monthly benefit parameter for HP i is $r _ { i }$ and the expected network size is $\mathbb { E } [ N _ { b } ]$ , the expected net benefit HP i would obtain from the collaboration is $\mathbb { E } [ r _ { i } N _ { b } ]$ . Our approach is in line with several models that consider the network externalities to be linear in the size of the consumer base (e.g., Fudenberg and Tirole 2000, Prasad et al. 2010).

Please note that the benefit parameters are not necessarily correlated with observables such as the size of HPs. For example, a large HP that already has a sophisticated IT system in place might find the benefit of HIE low compared to a small HP that has only basic IT functionalities. In addition, some HPs that have large amounts of patient data might be reluctant to share this data. Hence, they would find the HIE less beneficial. Moreover, in the general course of providing care, some HPs might already share some medical information among each other. However, since such transactions are generally not automated, these HPs should still benefit from the HIE membership. In general, because of such complications, it is usually not possible for the HIE provider to determine the amount of benefit each HP gains from joining the network. Therefore, we consider that the information about $r _ { i }$ is private in our model; i.e., it is unknown to the HIE provider and other $\mathrm { H P s } ,$ but known to HP i. Hence, we use $r$ to denote the stochastic counterpart of the benefit parameter. However, the parties can estimate the “distribution” of r based on the available information regarding HPs.

As discussed earlier, each participating HP may request the value-added service in addition to the base HIE service. The HIE provider bundles the valueadded services it offers, and we denote the level of this service by s. Note that our analysis can be extended to analyze more than one service bundle, but that would not affect our key findings in this paper—it merely creates more cases to examine. Value-added services, such as e-prescribing, patient management tools, and quality reporting, have positive network affects. This implies that if more HPs in the network sign up for the value-added services, these services will be perceived as more valuable by HPs that have already signed up. In contrast to the general trend in network externality literature (Fudenberg and Tirole 2000, Jing 2007, Prasad et al. 2010, Niculescu et al. 2012), we do not assume that the benefit of value-added service is the same for all HPs. In some recent models, product valuations and the benefits customers obtain from the network are correlated (e.g., Sundararajan 2003, 2004). The latter approach is more appropriate in the case of HIEs. Hence, we consider that the valuations of both the base HIE service and the value-added service are different for each HP.

Therefore, we formulate the expected benefit of HP i from the value-added service as $r _ { i } s \mathbb { E } [ N _ { v } ] d ,$ , where $r _ { i }$ is the benefit parameter of HP $i ,$ s is the level of the value-added service that is determined by the HIE provider, $N _ { v }$ is the number of HPs that request the value-added service from the HIE provider, $\mathbb { E } [ N _ { v } ]$ is its expectation, and d is a scaling parameter. Hence, if HP i requests the value-added service, its expected net value from the HIE is $r _ { i } s \mathbb { E } [ N _ { v } ] d + r _ { i } \mathbb { E } [ N _ { b } ]$

In this setting, an HP must be part of the HIE network to request value-added service. As discussed before, there are two networks with separate but related externalities, and membership to one of them is a requirement for the membership to the other. Binary decision variables $q _ { b i }$ and $q _ { v i }$ equal to one if $\mathrm { H P \ } i$ decides to join the HIE and requests the value-added service. If it does not join the HIE, both $q _ { b i }$ and $q _ { v i }$ are equal to zero. Otherwise, if it joins the HIE but does not request value-added service, then $q _ { b i }$ equals to one and $q _ { v i }$ equals to zero. All possible values for $q _ { b i }$ and $q _ { v i }$ are summarized in Table 1. Since value-added service requires base HIE subscription, we have $q _ { b i } \geq q _ { v i } .$ This condition implies $N _ { b } \geq N _ { v } ;$ i.e., the number of HPs that request the value-added service cannot be more than the number of participating HPs in the network. Note that the value-added service may help increase the network size—in such a case, some HPs start participating in the network to benefit from valueadded service. However, as we discuss in Lemma 5 in detail, the value-added service does not always encourage new HPs to join the HIE network.

If HP i does not request the value-added service but participates in the network, its objective function value is $r _ { i } \hat { \mathbb { E } } [ N _ { b } ] - p _ { b } ,$ i.e., the difference between benefit and fee of the network subscription.<sup>4</sup> In order for HP i to stay in the network, its benefit and cost difference needs to be positive (either when it merely joins the HIE or when it joins the HIE and requests value-added service). The HIE provider collects fees from all HPs that join. Hence, the higher price it sets, the more revenue it collects per $\mathrm { H } \mathbf { \check { P } }$ in the network. However, a high price for the HIE service deters the HPs for two reasons: (i) the direct effect of the higher fee and (ii) the reduction in the benefit from the network externalities. In effect, a price increase implies fewer participants in the network, and in-turn even lower benefits to the remaining participants. Therefore, the HIE provider needs to balance the subscription price and determines the most beneficial network size. In addition, the HIE provider needs to determine (i) the fee of value-added service (denoted by $p _ { v } )$ that is collected from all HPs that request the value-added service and (ii) the level of value-added service (denoted by s) that is offered to the participants. The HIE provider also needs to take into account the effects of $p _ { v }$ and s on the network dynamics.

Table 1 Possible Decisions of HP i

<table><tr><td>Decisions of HP i</td><td>Joins the HIE?</td><td>Requests the value-added service?</td></tr><tr><td> $q_{bi} = 0, q_{vi} = 0$ </td><td>No</td><td>No</td></tr><tr><td> $q_{bi} = 1, q_{vi} = 0$ </td><td>Yes</td><td>No</td></tr><tr><td> $q_{bi} = 1, q_{vi} = 1$ </td><td>Yes</td><td>Yes</td></tr></table>

In addition to the subscription fees for the base HIE service and value-added service, the HIE provider receives funds from the government and other third parties. These funds are provided to reimburse part of the cost incurred by the HIE provider to maintain its network. Some of these funds are directly proportional to the network size, whereas some others are fixed (independent of the network size) (Covich et al. 2011). We model the network dependent reimbursement as $N _ { b } g ,$ , where $g \geq 0 ,$ and the fixed part as J .

On the other hand, the costs of maintaining the HIE include implementation costs, hosting and data services costs, and administrative and operational costs (Covich et al. 2011). According to Mostashari et al. (2009), the cost of maintaining the network is positively correlated to the network size. Therefore, we model this cost as $c _ { b } N _ { b } + H _ { b }$ . In this formulation, $H _ { b }$ denotes the monthly adjusted fixed cost of establishing and maintaining the HIE network, and $c _ { b }$ is the monthly cost of providing base HIE service to each HP in the HIE. Since this cost is not “fully” subsidized by governmental or other funds (Covich et al. 2011, Samuels 2013, Smitherman 2013), we consider that $g < c _ { b }$

In addition, the total cost of providing the valueadded service increases with the total number of HPs that request it $( \mathrm { i } . \mathrm { e } . , N _ { v } )$ . Our discussions with the HIE providers also reveal that they incorporate less costly, more valuable value-added services first in the bundle they offer. This implies that there are decreasing returns to scale with respect to the offered level of value-added service. Hence, we formulate the total cost of offering value-added service as $c _ { v } N _ { v } s ^ { 2 } + H _ { v } . ^ { 5 }$ Here, $c _ { v }$ is the cost multiplier term per HP that requests value-added services, and $H _ { v }$ is the periodic fixed cost of providing value-added service.

The game played among the HIE provider and each HP $i ,$ and the constraints can be summarized as

$$
\max _ {s, p _ {v}, p _ {b}} \left\{p _ {v} \mathbb {E} [ N _ {v} ] + p _ {b} \mathbb {E} [ N _ {b} ] + g \mathbb {E} [ N _ {b} ] - c _ {b} \mathbb {E} [ N _ {b} ] \right.
$$

$$
\left. - c _ {v} \mathbb {E} [ N _ {v} ] s ^ {2} - H _ {b} - H _ {v} + J \right\}\tag{1}
$$

$$
\max _ {q _ {b i}, q _ {v i}} \left\{q _ {b i} (r _ {i} \mathbb {E} [ N _ {b} ] - p _ {b}) \right.
$$

$$
\left. + q _ {v i} (r _ {i} s \mathbb {E} [ N _ {v} ] d - p _ {v}) \right\}\tag{2}
$$

subject to $q _ { b i } \geq q _ { v i }$

$$
p _ {v} \mathbb {E} [ N _ {v} ] + p _ {b} \mathbb {E} [ N _ {b} ] + g \mathbb {E} [ N _ {b} ] - c _ {b} \mathbb {E} [ N _ {b} ]\tag{3}
$$

$$
- c _ {v} \mathbb {E} [ N _ {v} ] s ^ {2} - H _ {b} - H _ {v} + J \geq 0,\tag{4}
$$

$$
q _ {b i}, q _ {v i} \in \{0, 1 \} \quad \forall i.\tag{5}
$$

In this formulation, Expression (1) is the objective function of the HIE provider that tries to maximize its expected net value. Here, the decision variables of the HIE provider are the level of the value-added service, the fee for the value-added service, and the fee for the HIE subscription. Expression (2) and Constraint (3) depict that each HP chooses among (i) staying out of the HIE network, (ii) joining the ${ \mathrm { H I E } } ,$ and (iii) joining the HIE and requesting value-added service. Moreover, because of Constraint (3), an HP cannot request valueadded service if it does not join the HIE network. Next, Constraint (4) ensures that the expected value of the HIE provider is nonnegative. Finally, Constraint (5) lists the binary decision variables. In §3.2, we present the benchmark case of our model.

## 3.2. Details of the Benchmark Case

In this subsection, we present the benchmark case of our model where the HIE provider does not offer HIE related value-added service. As discussed in §2.2, this setting represents most of the newly established HIEs because they generally do not focus on valueadded service. After removing the benefit and cost components related to the value-added services, we present the following benchmark case:

$$
\max _ {p _ {b}} \left\{p _ {b} \mathbb {E} [ N _ {b} ] + g \mathbb {E} [ N _ {b} ] - c _ {b} \mathbb {E} [ N _ {b} ] - H _ {b} + J \right\}\tag{6}
$$

$$
\max _ {q _ {i}} q _ {i} (r _ {i} \mathbb {E} [ N _ {b} ] - p _ {b})\tag{7}
$$

$$
\text { subject   to } \quad q _ {i} \in \{0, 1 \} \quad \forall i,\tag{8}
$$

$$
p _ {b} \mathbb {E} [ N _ {b} ] + g \mathbb {E} [ N _ {b} ] - c _ {b} \mathbb {E} [ N _ {b} ] - H _ {b} + J \geq 0.\tag{9}
$$

In this formulation, Expression (6) is the objective function of the HIE provider that tries to maximize its expected net value. Here, the decision variable of the HIE provider is the subscription fee $( \mathrm { i . e . , } p _ { b } )$ . On the other hand, Expression (7) and Constraint (8) imply that each HP joins the HIE only if its gain is positive. If it joins $( \mathrm { i . e . , ~ } q _ { i } = 1 )$ , it receives value in the amount of $r _ { i } \mathbb { E } [ N _ { b } ] - p _ { b }$ . Otherwise, it stays out $( \mathrm { i . e . , ~ } q _ { i } = 0 )$ and obtains no value. Finally, Constraint (9) implies that the expected value of the HIE provider is nonnegative. This constraint implies that for the HIE provider to establish the network, the business needs to be sustainable.

Note that parameters $H _ { b } , H _ { v } ,$ and J are fixed amounts, and hence they do not have a significant effect on our analysis. Therefore, to keep the discussions and analysis concise in both the main model and its benchmark case, we set them to zero hereafter. However, key insights remain the same with nonzero levels of these parameters. In §4, we present our results and managerial insights.

## 4. Results and Managerial Insights

In this section, we discuss our key findings and present meaningful insights. In §4.1, we present the results of the benchmark case of our model. After that, we provide the results of the main model.

## 4.1. The Benchmark Case

As discussed earlier, the HIE provider determines the price, and depending on this price, each HP decides whether to join or not. Furthermore, the decisions of other HPs (regarding whether they will join or not) affect the benefits of all participating members. Taking these into consideration, together with the fact that any HP will join the HIE only if it expects to have positive net value, we can write the following recursive relationship:

$$
\mathbb {E} [ N _ {b} \mid p _ {b} ] = N \cdot \mathbb {P} [ r   \mathbb {E} [ N _ {b} \mid p _ {b} ] - p _ {b} \geq 0 ].\tag{10}
$$

Without loss of generality, order $r _ { i }$ such that $r _ { i } <$ $r _ { i + 1 } \ \forall i .$ . Observe that if HP i joins the HIE, so does $\mathrm { H P } \ j$ where $j > i .$ In addition, if HP $i ^ { * }$ is the HP with the lowest benefit parameter that joins the HIE, we can write Ɛ $\cdot N _ { b } \mid p _ { b } ] \stackrel {  } { = } N ( 1 - F ( r _ { i ^ { * } } ) )$ , where $F ( \cdot )$ is the cumulative distribution function of r. In such a case, the HIE provider needs to set $p _ { b }$ to $r _ { i ^ { * } } \mathbb { E } [ N _ { b } | p _ { b } ] =$ $N r _ { i ^ { * } } ( 1 - F ( r _ { i ^ { * } } ) )$ 5. In other words, the HIE provider would not leave any value to the HP that is indifferent between joining the HIE or not. This is the price it would charge to all participating HPs. One interesting result is that the relationship between the price $p _ { b }$ and network size is not monotonic. This is because $r _ { i } ( 1 - F ( r _ { i } ) )$ is not necessarily concave or convex in $r _ { i } ;$ in particular, the behavior depends on the distribution.

Let us denote the HP that is indifferent between joining and not joining at the equilibrium by $i ^ { * }$ , and the probability density function of r by $f ( \cdot )$ . Using the above arguments, the objective function of the HIE provider can be rewritten as

$$
N (1 - F (r _ {i})) (r _ {i} N (1 - F (r _ {i})) - c _ {b} + g).\tag{11}
$$

The first order condition reveals

$$
r _ {i ^ {*}} = \frac {N (1 - F (r _ {i ^ {*}})) ^ {2} + f (r _ {i ^ {*}}) (c _ {b} - g)}{2 N f (r _ {i ^ {*}}) (1 - F (r _ {i ^ {*}}))}.\tag{12}
$$

In addition, the second order condition requires

$$
\begin{array}{r l} & f ^ {\prime} (r _ {i ^ {*}}) (c _ {b} + 2 N r _ {i ^ {*}} F (r _ {i ^ {*}}) - g - 2 N r _ {i ^ {*}}) \\ & \qquad + 2 N f (r _ {i ^ {*}}) (r _ {i ^ {*}} f (r _ {i ^ {*}}) + 2 F (r _ {i ^ {*}}) - 2) <   0. \end{array}
$$

Hence, from this recursive relationship, we can derive the equilibrium network size. The above equality helps us glean some other insights, with some assumptions on the distribution of r. For example, if the distribution of r has a decreasing failure rate, the equilibrium price “may” decrease with $c _ { b } .$ In such a case, the HIE provider should not decrease the network size by increasing the price, even though increasing the price would make the HIE provider collect more value from each of the remaining participants. Instead, the HIE provider should increase the network size by decreasing the price and collect more value in total from all of the participants in the HIE.

Next, we would like to answer the following questions using the results of our model: (i) how does variation in the distribution affect participation in the

HIE network? and (ii) how does the behavior of net values of the parties change with respect to different characteristics of HPs and HIE provider? To explore the answers to these questions and several others, more structure in the distribution of r is needed. All of our key insights hold with any distribution that is bounded from above and below, and is unimodal. Furthermore, most of our insights hold with any distribution that is unimodal (but not necessarily bounded). However, to be conservative about the variance of the distribution, we consider that r follows a uniform distribution with lower and upper bounds r and $\bar { r } , \mathrm { i . e . , } r \sim \mathcal { U } ( \underline { { r } } , \bar { r } )$ . For the rest of this paper, the heterogeneity refers to the variability in benefit parameters of HPs. In particular, we measure the heterogeneity with the range of the distribution, i.e., ${ \bar { r } } - \underline { { r } } .$

The solution of the game among the parties reveals the equilibrium network size that is presented in Lemma 1. Different parts of this lemma are depicted in Figure $^ { 2 , }$ and all proofs are presented in the online appendix (available as supplemental material at http:// dx.doi.org/10.1287/isre.2016.0626).

<sup>Lemma</sup> <sup>1.</sup> The equilibrium network size is

(a) $( N \bar { r } + \sqrt { N ( N \bar { r } ^ { 2 } - 3 ( \bar { r } - \underline { { r } } ) ( c _ { b } - g ) ) } ) / ( 3 ( \bar { r } - \underline { { r } } ) )$ if $c _ { b } \leq g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and $\underline { { r } } \le \bar { r } / 3 - g / ( 3 N )$ , or $g +$ $N ( 3 \underline { { r } } - \bar { r } ) \le c _ { b } \le g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and ${ \bar { r } } / 3 - g / ( 3 N ) \leq$ $\underline { { r } } < \bar { r } / 2 ,$

(b) N $\begin{array} { r } { i f c _ { b } \le g + N ( 3 \underline { { r } } - \bar { r } ) } \end{array}$ and $\bar { r } / 3 - g / ( 3 N ) \le \underline { { r } } \le \bar { r } / 2$ or $c _ { b } \leq g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and $\underline { { r } } \geq \bar { r } / 2 ,$

$$
\text {(c)} 0 \text { if } c _ {b} > g + \bar {r} ^ {2} N / (4 (\bar {r} - \underline {{r}})).
$$

If heterogeneity is large, or if both heterogeneity and the cost of keeping each HP in the HIE are at medium levels, then a partial network is established where some HPs join but not all (as presented in part (a) of Lemma 1). The second and third cases, on the other hand, depict the cases where every HP joins the HIE and where the HIE is not established, respectively. The key factor that determines whether or not the HIE is established is the cost for hosting each HP in the network. If $c _ { b }$ is more than the threshold $g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ , the HIE provider cannot sustain an HIE and it does not establish one (as shown in part (c) of Lemma 1). This threshold value decreases with an increase in the maximum benefit HPs can get from the HIE $( \mathrm { i } . \mathrm { e } . , \bar { r } )$ when the heterogeneity among the HPs is small (in particular, if $\underline { { r } } > \bar { r } / 2 )$ . Hence, if the heterogeneity is small, contrary to intuition, when the maximum benefit HPs can get from the HIE increases, the cost of accommodating each HP in the network has to be even lower to establish the HIE.

Figure 2 Lemma 1: Equilibrium Network Size  
![](/api/attachments/CYEN9VEX/fulltext/images/9f99ffcd7f64d8a0fc70e308d512f1ba8b81077fe994105aeca4c0bc8c380cc5.jpg)

It is interesting to note that if the above condition is satisfied $( \mathrm { i } . \mathrm { e } . , \bar { r } < 2 \underline { { r } } )$ and the cost is less than the above mentioned threshold value, then it is better for the HIE provider to serve all HPs by setting the subscription fee $p _ { b }$ to $\underline { r } N$ . Hence, in this case, all of the HPs decide to join the HIE network (as shown in part (b) of Lemma 1). On the other hand, if the heterogeneity is relatively higher $( \mathrm { i . e . , ~ } 2 \underline { { r } } \le \bar { r } \le 3 \underline { { r } } )$ ), the cost needs to be even less than $g + N ( 3 \underline { { r } } - \bar { r } )$ for full participation. If the heterogeneity is even higher $( \bar { r } > \bar { 3 } r )$ , full participation is not possible if government and third-party incentives do not cover the entire subscription fee $( { \mathrm { i . e . , ~ } } g \neq c _ { b } )$ . In such a case, the HIE provider finds it more beneficial to increase the subscription fee and collect more value from the participating $\mathrm { H P s } ,$ rather than setting a low price and enticing all HPs to join the network. We summarize this finding in the following proposition.

<sup>Proposition</sup> <sup>1.</sup> In general, heterogeneity among HPs decrease the number of HPs in the network. Also, full participation is not possible if the heterogeneity among the HPs is high, i.e., $\underline { { r } } < \bar { r } / 3 - g / ( 3 N )$ .

Hence, when the heterogeneity is high, or when costs related to providing HIE services are high, policy makers and HIE providers may employ the following strategies to encourage participation. First, the government or HIE providers can focus on providing more incentives to HPs so that the minimum benefit HPs can get from the participation is increased. For example, if small HPs do not have functional EHR implementations, HIE providers might offer EHR applications for free or at a very low price. In the United States, several HIE providers are already offering this incentive. However, as apparent in Proposition 1, these incentives cannot entice all HPs to join the network when the heterogeneity among HPs is high. Hence, the second option to entice more HPs is to provide HIE-related value-added services that we analyze in §4.2. The third option to entice more HPs is to establish more than one HIE in the region. Establishing a second HIE in the same region that focuses more on low-gain HPs might increase the benefits of low-gain HPs, and in turn, more of them might decide to join the HIE. Hence, under certain conditions, there might be an incentive for the policy makers to establish more than one HIE in a region. Even if there is a second HIE provider, it might not be able to induce full participation, but it can at least increase participation. To examine this issue further, we consider a setting with two HIE providers in §4.1.1.

Our analysis and the results in Lemma 1 also reveal that if the HIE network is established, a significantly large number of HPs in the region find it beneficial to join the network. We summarize this finding in the following proposition.

<sup>Proposition</sup> <sup>2.</sup> If the HIE is established, the number of HPs in the region that join the network at the equilibrium should be sufficiently large, in particular, $N _ { b } \ge \dot { N } / 2$

As discussed earlier, the number of participating HPs affects the benefits of the HPs that are in the network. Proposition 2 reveals that if any party conjectures that the HIE will not be beneficial to a sufficiently large number of HPs in the region, then the HIE will not be established. Therefore, the HIE provider and the policy makers should consider this when they are designing incentive schemes that affect how much the HIEs will be beneficial to the participating HPs.

If the government changes the amount of incentives for HPs, these are reflected in changes in the upper and lower bounds of the distribution of the benefit parameter (hence, in heterogeneity as well). Therefore, in the following proposition, we examine how network size is affected if the benefit parameters change. We focus on the partial network case presented in part (a) of Lemma 1 since the other cases are trivial.

<sup>Proposition</sup> <sup>3.</sup> When there is a partial network, its size

(a) increases with the lowest benefit HPs can get from the HIE $( \underline { { r } } ) ,$

(b) increases with the highest benefit HPs can get from the HIE 4r¯5 if and only if the heterogeneity and the cost of accommodating each $H \dot { P }$ in the HIE are both moderately high, in particular, if and only if $\bar { r } > 4 \underline { { r } }$ and $c _ { b } > g + ( 4 \underline { { r } } N ) / 3 .$

A higher lower bound r (while keeping the upper bound r¯ constant) implies that the heterogeneity decreases. In such a case, as stated in the first part of Proposition 3, participation in the HIE increases. On the other hand, as presented in the second part of Proposition 3, under certain conditions, the equilibrium network size increases with an increase in heterogeneity. This happens when both heterogeneity and the cost are moderately high. In such a case, the HIE provider finds it more beneficial to entice more HPs into the network. On the other hand, if the heterogeneity is not large, in particular, if $\hat { r } < 4 \underline { { r } } ,$ introducing more benefits to the HPs by increasing the upper bound actually decreases the participation in the network. In those cases, the HIE provider focuses on high-gain HPs to collect more value from them. Since the goal of the policy makers is to increase participation in HIEs, they should be careful when designing incentive schemes for HPs.

Next, we present the equilibrium subscription fee that is collected from each participating $\mathrm { H \bar { P } }$ for the case when there is partial participation in the HIE. Equilibrium subscription fees for full participation and no participation cases are trivial, and hence not reported. The subscription fee presented in Lemma 2 enables the HIE provider to collect the most value from the network given that it enables the provider to extract all value from the HP that is indifferent between joining and not joining the HIE.

<sup>Lemma</sup> <sup>2.</sup> When there is partial participation, the equilibrium subscription fee that is collected from each HP in the HIE is given by

$$
p _ {b} ^ {*} = \frac {N \bar {r} ^ {2} + 3 (\bar {r} - \underline {{r}}) (c _ {b} - g) + \bar {r} \sqrt {N (N \bar {r} ^ {2} - 3 (\bar {r} - \underline {{r}}) (c _ {b} - g))}}{9 (\bar {r} - \underline {{r}})}.
$$

Clearly, the expected network size decreases in network subscription price $p _ { b } .$ . In addition, sensitivity analysis of $p _ { b } ^ { * }$ (given in Lemma 2) with respect to r and $\dot { \bar { r } }$ reveals that it increases in r and $\bar { r }$ (this result is formally shown in the proof of Lemma 2 in the online appendix). This finding seems reasonable because as the participants expect more benefits, the HIE provider extracts more value from them by increasing the price. Now, based on Lemmas 1 and 2, we present and discuss the objective function values of the HPs and the HIE provider. Again, we present the results only for the case when a partial network is formed.

<sup>Lemma</sup> <sup>3.</sup> When a partial network is formed, the values different HPs obtain from the HIE and the value of the HIE provider are as follows:

(a) The value of HP i is

$$
\begin{array}{l} q _ {i} \Big (\big ((N (3 r _ {i} - 2 \bar {r}) + \sqrt {N (N \bar {r} ^ {2} - 3 (\bar {r} - \underline {{r}}) (c _ {b} - g))} \big) \\ \qquad \cdot \big (N \bar {r} + \sqrt {N (N \bar {r} ^ {2} - 3 (\bar {r} - \underline {{r}}) (c _ {b} - g))} \big) \Big) \\ \qquad \cdot (9 N (\bar {r} - \underline {{r}})) ^ {- 1} \Big). \end{array}
$$

(b) The value of the HIE provider is

$$
\begin{array}{l} \Big (\big (N \bar {r} ^ {2} - 6 (\bar {r} - \underline {{r}}) (c _ {b} - g) + \bar {r} \sqrt {N (N \bar {r} ^ {2} - 3 (\bar {r} - \underline {{r}}) (c _ {b} - g))} \big) \\ \cdot \big (N \bar {r} + \sqrt {N (N \bar {r} ^ {2} - 3 (\bar {r} - \underline {{r}}) (c _ {b} - g))} \big) \Big) \\ \cdot (2 7 (\bar {r} - \underline {{r}}) ^ {2}) ^ {- 1}. \end{array}
$$

The sensitivity analyses of the equilibrium values presented in Lemma 3 with respect to different parameters reveal several interesting results. First, for all participating HPs, the net values they receive from the HIE decrease if there is an increase in the highest benefit an HP can get from the network $( \mathrm { i . e . , } \bar { r } )$ , although such an increase seems beneficial to the participating HPs. In such a case, the HIE provider extracts more value from the participating HPs by increasing the price. Hence, the policy makers or the HIE provider should proactively seek ways to propose more value to all participants (by increasing r) when r¯ increases. However, this should be done with a grain of salt. This is because if the benefit parameter of an HP is less than ${ \bar { r } } / 3 ,$ , an increase in r actually decreases its net value. This result might seem counterintuitive, but can be explained as follows. Increasing r increases both the equilibrium subscription price (see the discussion after Lemma 2) and the equilibrium network size (see part (a) of Proposition 3). Therefore, HPs whose benefits are more sensitive to the network size $( \mathrm { i . e . , }$ $r _ { i } > \underline { { r } } / 3 )$ realize a net benefit if r increases in spite of the price increase. The rest of the HPs do not find it beneficial because the extra benefit they get from the larger network cannot compensate for the increase in the subscription fee. We summarize this discussion in the following proposition.

<sup>Proposition</sup> <sup>4.</sup> The value of HP i at the equilibrium:

(a) decreases with the highest benefit HPs can get from joining the HIE,

(b) increases with the lowest benefit HPs can get from joining the HIE if and only $i f r _ { i } > \bar { r } / 3$

The sensitivity analysis of the equilibrium value of the HIE provider (presented in Lemma 3) with respect to r¯ reveals that it increases in r¯ (this result is formally shown in the proof of Proposition 4). On the other hand, we know from part (a) of Proposition 4 that the values of HPs actually decrease in r¯. Hence, an increase in heterogeneity because of an increase in the upper bound is beneficial only to the HIE provider. We now analyze the impact of a decrease in heterogeneity with an increase in the lower bound $\underline { { r } } .$ The sensitivity of the equilibrium value of the HIE provider with respect to r shows that the HIE provider’s value increases with $\underline { { r } } .$ However, as discussed in part (b) of Proposition 4, an increase in $\underline { { r } }$ increases the value of HPs only if they are high-gain HPs, i.e., if $r _ { i } > \bar { r } / 3$ . Hence, decreasing the heterogeneity by increasing $\underline { { r } }$ is also not beneficial to all parties.

In §4.1.1, we examine a setting with two HIE providers.

4.1.1. A Setting with Two HIE Providers. We now present a generalized model with two HIE providers. Here, the focus is on the base HIE connectivity to show that the increase in participation is because of the second HIE network (not because of the value-added services that we analyze in §4.2). The parameters of the model are the same as the original benchmark model except that the additional index takes value 1 or 2 to reflect the corresponding HIE. In addition, if HP i joins the first HIE (respectively, second HIE), $q _ { i 1 } = 1$ (respectively, $q _ { i 2 } = 1 )$ ; otherwise, if it does not join, $q _ { i 1 } = 0$ (respectively, $q _ { i 2 } = 0 )$

$$
\max _ {p _ {b 1}} \left\{p _ {b 1} \mathbb {E} [ N _ {b 1} ] + g _ {1} \mathbb {E} [ N _ {b 1} ] - c _ {b 1} \mathbb {E} [ N _ {b 1} ] \right\}\tag{13}
$$

$$
\max _ {p _ {b 2}} \left\{p _ {b 2} \mathbb {E} [ N _ {b 2} ] + g _ {2} \mathbb {E} [ N _ {b 2} ] - c _ {b 2} \mathbb {E} [ N _ {b 2} ] \right\}
$$

(14)

$$
\max _ {q _ {i 1}, q _ {i 2}} \left\{q _ {i 1} (r _ {i 1} \mathbb {E} [ N _ {b 1} ] - p _ {b 1}) + q _ {i 2} (r _ {i 2} \mathbb {E} [ N _ {b 2} ] - p _ {b 2}) \right\}\tag{15}
$$

$$
\text { subject   to } \quad q _ {i 1} \in \{0, 1 \} \quad \forall i,\tag{16}
$$

$$
q _ {i 2} \in \{0, 1 \} \quad \forall i,\tag{17}
$$

$$
q _ {i 1} + q _ {i 2} \leq 1 \quad \forall i,\tag{18}
$$

$$
p _ {b 1} \mathbb {E} [ N _ {b 1} ] + g _ {1} \mathbb {E} [ N _ {b 1} ] - c _ {b 1} \mathbb {E} [ N _ {b 1} ] \geq 0,\tag{19}
$$

$$
p _ {b 2} \mathbb {E} [ N _ {b 2} ] + g _ {2} \mathbb {E} [ N _ {b 2} ] - c _ {b 2} \mathbb {E} [ N _ {b 2} ] \geq 0.\tag{20}
$$

In this model, as stated in Expressions (13) and (14), the HIE providers maximize their total net value. Moreover, in Expression (15), HP i maximizes its total net value. Constraints (16)–(18) imply that an HP can join a single HIE or does not join any of the HIEs.<sup>6</sup> Last, Constraints (19) and (20) state that an HIE will not be established if it expects a loss from doing business.

The second HIE can be established in several different ways that should be modeled and examined differently. Hence, rather than solving the model for each possible scenario, we provide a numerical example where the goal is to show that the total number of participating HPs can increase if the second HIE is established. It is important to note that the assumptions and the problem setting itself are neither necessary nor sufficient for the participation to increase. Other examples where the participation increases can be developed in completely different settings or in the same setting under different assumptions.

Example. Let us assume that there are 100 potential HPs that may join an HIE in a region (in this case, there is only one HIE). Also, assume that the lower and upper bounds of the distribution of r are 0 and 1. In addition, assume that the cost of keeping an HP in the HIE is 12.5, and the monthly portion of the government reimbursement per participating HP is 0. In such a case, according to Lemmas 1 and 2, the network size would be 60, and the price charged per HP would be 24.

Now, assume that instead of one HIE, two HIEs can be established in this region (or one of them is established after the first one and there is no switching cost). Let us assume that the second HIE provider offers a new service, such as an EHR application, for free. This EHR application will be valuable only to a portion of the HPs in the area, because some HPs already have EHR applications that are probably tied to other applications (such as billing or patient quality analysis tools). For illustration purposes,<sup>7</sup> let us assume that the new service is valuable only to half of the HPs. Furthermore, assume that the benefit distribution is uniform with lower and upper bounds 1 and 2 for these HPs in the second HIE. In particular, assume that the benefit parameters in the first HIE and the second HIE are given by $r _ { i 1 } + 1 = r _ { i 2 }$ for the HPs that find the EHR (and therefore the second HIE) valuable. For the rest of the HPs, let us assume indifference in their choice of HIE providers. Hence, $r _ { i 1 } = r _ { i 2 }$

Next, we propose that the second HIE exclusively serves the HPs whose benefits increase because of the new EHR application. Although this EHR application might be a necessity to be able to participate in the second $\mathrm { H I E ^ { 8 } }$ (certain HIE modules might be built in to (or require) this specific EHR implementation), let us assume that it is not the case to make the example more generalizable. Also, let us assume that since the second HIE supports and maintains EHR solutions at participating HP locations, its cost of maintaining each HP in the network is increased to 50 from $1 2 . 5 . ^ { \circ }$ Similarly, the first HIE exclusively serves the HPs that do not find the EHR solution valuable. In such a case, invoking Lemmas 1 and 2 reveals that the size of the first HIE is 25, and the price charged per HP is 12.5. In the second HIE, there is full participation $( \mathrm { i . e . , }$ , network size is 50), and the price charged per HP is 50.

For this solution to be an equilibrium solution, we need to show that the exclusivity assumption is justified and none of the HPs or the HIE providers finds any other action to be more profitable (by deviating unilaterally):

• First, observe that both HIE providers operate at their costs. Hence, they cannot decrease their prices. If they were not operating at their costs, they could potentially decrease their prices and lure HPs into their network that participate in the other HIE (or those HPs that do not participate in any of the HIEs).

• Increasing the price would only decrease the number of participants in a network, and would not entice any HP that finds the other HIE more valuable (or those HPs that do not participate in any of the HIEs). Hence, the HIE provider would serve a subset of its participants if it increased the price. However, by definition of the equilibrium solution in these exclusive networks, increasing the price and serving a smaller subset of the HPs is not better for any HIE provider. Hence, the HIE providers will not increase their prices.

• To show the exclusivity of the first HIE, let us consider an arbitrary HP m who finds the EHR valuable (hence, $1 \leq r _ { m 2 } \leq 2$ and $r _ { m 1 } + 1 = r _ { m 2 } )$ , but finds it better to join the first HIE (instead of the second HIE). This implies that its net value is higher in the first HIE. In other words, $( 2 5 + 1 ) r _ { m 1 } - 1 \bar { 2 } . 5 > 5 0 r _ { m 2 } - 5 0$ . This condition can be rewritten as $r _ { m 2 } < 0 . 4 8$ . This is not possible because $1 \leq r _ { m 2 } \leq 2$ . Hence, the exclusivity of the first HIE is justified.

• To show the exclusivity of the second HIE, let us consider an arbitrary HP k who does not find the EHR valuable (hence, $0 \leq r _ { k 1 } = r _ { k 2 } \leq 1 )$ , but finds it better to join the second HIE (instead of the first HIE). This implies that its net value is higher in the second HIE. In other words, $( 5 0 + 1 ) r _ { k 2 } - 5 0 > 2 5 r _ { k 1 } - 1 2 . 5$ . This condition can be rewritten as $r _ { k 1 } > 1 . 4 4$ . This is not possible because $0 \leq r _ { k 1 } \leq 1$ . Hence, the exclusivity of the second HIE is also justified.

Therefore, the proposed solution is indeed an equilibrium, and the total number of participants in the case of two HIEs $( \mathrm { i . e . , ~ } 5 0 + 2 5 = 7 5 )$ is more than the number of participants in the case of a single HIE $( \mathrm { i . e . , 6 0 } )$ .

Please note that although most of our assumptions hinder the growth of the networks (e.g., the cost of the second HIE increases by 300% due to offering the EHR free or at a discount), the total participation increases in the HIEs after the establishment of a second HIE. As discussed earlier, under different assumptions, similar results can be found. For example, we checked what would happen if (i) the two HIEs could communicate between each other (so that there was a network of networks) or (ii) if the second HIE could accommodate those HPs that do not find the EHR valuable at reduced cost levels (i.e., less than 50 per HP). The results again show that the total participation increases because of the additional HIE.

The results presented in this subsection not only serve as a benchmark to our main model but also provide several useful guidelines for policy makers and many start-up HIEs, such as SETHS, in setting the subscription fee in those environments where the HIE provider offers only the base HIE service. Now, in §4.2, we discuss our findings in the main model where the HIE provider also offers HIE related value-added services to participating HPs.

## 4.2. Results and Managerial Insights of the Main Model

In the main problem, as discussed earlier, the HIE provider sets (i) the price of base services $( \mathrm { i . e . , ~ } p _ { b } )$ (ii) the price of value-added services $( \mathbf { i . e . } , p _ { v } )$ , and (iii) the level of the value-added services. Depending on these, each HP decides whether to join the network or not, and whether to request value-added services or not. As discussed before, the decisions of other HPs regarding whether they would join the HIE (respectively, request value-added services) affect the benefits of all participating HPs from joining the HIE (respectively, from value-added services). There are two possible cases: (i) some of the participating HPs do not request value-added services, i.e., $\mathbb { E } [ { \bar { N } } _ { v } ] < \mathbb { E } [ N _ { b } ]$ and (ii) each participating HP requests value-added services, i.e., $\dot { \mathbb { E } } [ N _ { v } ] = \mathbb { E } [ N _ { b } ]$ . For $\mathbb { E } [ \hat { N } _ { v } ] < \mathbb { E } [ N _ { b } ]$ , we can write the following recursive relationships:

$$
\mathbb {E} [ N _ {b} \mid p _ {b} ] = N \cdot \mathbb {P} [ r \mathbb {E} [ N _ {b} \mid p _ {b} ] - p _ {b} \geq 0 ],\tag{21}
$$

$$
\mathbb {E} [ N _ {v} \mid p _ {v} ] = N \cdot \mathbb {P} [ r s \mathbb {E} [ N _ {v} \mid p _ {v} ] d - p _ {v} \geq 0 ].\tag{22}
$$

On the other hand, if the solution of Equations (21) and (22) is infeasible $( \mathrm { i . e . , ~ } \mathbb { E } [ N _ { v } ] > \mathbb { E } [ N _ { b } ] )$ 1 then the derivation of $N _ { b }$ and $N _ { v }$ requires the solution of Equation (23) together with the fact that $N _ { v } = N _ { b }$ at the equilibrium

$$
\begin{array}{c} \mathbb {E} [ N _ {b} \mid p _ {b}, p _ {v} ] = N \cdot \mathbb {P} [ r s \mathbb {E} [ N _ {b} \mid p _ {b}, p _ {v} ] d \\ + r \mathbb {E} [ N _ {b} \mid p _ {b}, p _ {v} ] - p _ {v} - p _ {b} \geq 0 ]. \end{array}\tag{23}
$$

In the proofs of Lemmas 4 and 5 (presented in the online appendix), we provide more details regarding when to use Equations (21) and (22) and when to use Equation (23) to derive the number of HPs that participate in the HIE and the number of HPs that request the value-added service. Without loss of generality, order $r _ { i }$ such that $r _ { i } < r _ { i + 1 }$ ∀i. Observe that if HP i joins the HIE or requests value-added services, so does HP j where $j > i .$ Therefore, if $\mathbb { E } [ N _ { v } ] < \mathbb { E } [ N _ { b } ] .$ , and if HP $i _ { b }$ is the HP with the lowest benefit parameter that joins the HIE, we have $\mathbb { E } [ N _ { b } \mid p _ { b } ] = N ( \hat { 1 } - F ( r _ { i _ { b } } ) )$ . Besides, if HP $i _ { v }$ is the HP with the lowest benefit parameter in the HIE that requests value-added services, we have $\mathbb { E } [ N _ { v } | p _ { v } ] = N ( \hat { 1 } - F ( r _ { i _ { v } } ) )$ . Here, $F ( \cdot )$ is the cumulative distribution function of r. In such a case, the HIE provider needs to set $p _ { b } = r _ { i _ { b } } \mathbb { E } [ N _ { b } \mid p _ { b } ] = N r _ { i _ { b } } ( 1 - F ( r _ { i _ { b } } ) )$ and $p _ { v } = r _ { i _ { v } } s \mathbb { E } [ N _ { v } \mid p _ { v } ] d = r _ { i _ { v } } { \tilde { s } } N ( 1 - F ( r _ { i _ { v } } ) ) d$ . These equalities imply that the HIE provider does not leave any value to the HP that is indifferent between joining and not joining and indifferent between requesting value-added services or not.

It is possible to glean some insights from our model even without making assumptions on the distribution of the benefit parameter r. However, to explore our model to a greater extent and to get more results, more structure in the distribution of r is needed. To be conservative about the variance, we consider that r follows a uniform distribution with lower and upper bounds r and $\bar { r } , \mathrm { i . e . , } r \sim \mathcal { U } ( \underline { { r } } , \bar { r } )$

Denote the HP that is indifferent between joining and not joining at the equilibrium by $i _ { b } ^ { * } ,$ its benefit parameter by $\boldsymbol { r } _ { b } ^ { * } ,$ , the equilibrium subscription price set by the HIE provider by $p _ { b } ^ { * } ,$ and the equilibrium network size by $\bar { \mathbf { \xi } } _ { N _ { b } ^ { * } }$ . In addition, denote the HP that is indifferent between requesting value-added services or not at the equilibrium by $i _ { v } ^ { * } ,$ its benefit parameter by $r _ { v } ^ { * } ,$ the equilibrium price of the value-added service by $p _ { v } ^ { * } ,$ the optimal level of value-added service by $s ^ { * } ,$ , and the number of HPs that request value-added services at the equilibrium by $N _ { v } ^ { * }$ . Hence, it is easy to show that $\mathbb { E } [ N _ { b } | \hat { p _ { b } ^ { * } } ] = N ( ( \bar { r } - \dot { r _ { b } ^ { * } } ) / ( \bar { r } - \underline { { r } } ) )$ 5 and $\mathbb { E } [ N _ { v } | p _ { v } ^ { * } ] =$ $N ( ( \bar { r } - r _ { v } ^ { * } ) / ( \bar { r } - \underline { { r } } ) )$ . Therefore, after substituting these into the objective functions of the HIE provider and the HPs, we can solve the game and derive equilibrium values. In the next lemma, we present the equilibrium levels of the value-added service and the number of HPs that request value-added services.

<sup>Lemma</sup> <sup>4.</sup> When the HIE provider offers value-added services, the equilibrium level of the value-added service $( i . e . , s )$ and the expected number of HPs that request valueadded services given the fee structure $( i . e . , \mathbb { E } [ \dot { N } _ { v } | p _ { v } ^ { * } ] )$ are given by

$$
\begin{array}{r} s = \frac {N r _ {v} ^ {*} (\bar {r} - r _ {v} ^ {*}) d}{2 c _ {v} (\bar {r} - \underline {{r}})}, \\ \mathbb {E} [ N _ {v} | p _ {v} ^ {*} ] = N \frac {\bar {r} - r _ {v} ^ {*}}{\bar {r} - \underline {{r}}}, \end{array}
$$

given that the following holds:

$$
\mathbb {E} [ N _ {v} \mid p _ {v} ^ {*} ] \leq \mathbb {E} [ N _ {b} \mid p _ {b} ^ {*} ].
$$

Lemma 4 implies that there is a recursive relationship between the number of HPs that request the valueadded service and the level of the value-added service. Taking this into account, the HIE provider can optimize the level of value-added service it offers to HPs, the fee of the value-added service, and the fee for participation in the HIE. In Lemma 5, we present the equilibrium number of participants in the HIE, the equilibrium number of HPs that are interested in value-added services, and the conditions that enable the HIE provider to increase the number of participants in the network because of the value-added services. Different parts of this lemma are depicted in Figure 3. We relegate our discussion pertaining to the optimal fee structure to Lemma 6. For conciseness, we use the threshold value â to represent $( 7 2 9 \bar { r } ^ { 5 } N ^ { 3 } d ^ { 2 } ) / ( 3 , 1 2 5 ( \bar { r } - \underline { { r } } )$ $( 3 ( c _ { b } - g ) ( \bar { r } - \underline { { r } } ) ) ( 2 \sqrt { N ( \bar { r } ^ { 2 } N - 3 ( c _ { b } - g ) ( \bar { r } - \underline { { r } } ) ) } + 3 \bar { r } N ) -$ $2 \bar { r } ^ { 2 } N ( \sqrt { N ( \bar { r } ^ { 2 } N - 3 ( c _ { b } - g ) ( \bar { r } - \underline { { r } } ) ) } + \bar { r } N ) ) )$ in part (a) of Lemma 5.

<sup>Lemma</sup> <sup>5.</sup> When the HIE provider optimizes the level of value-added services, the equilibrium network size $( i . e . , N _ { b } ) ,$ and the number of HPs that request value-added services $( i . e . , N _ { v } )$ are given by the following:

(a) If the cost of maintaining each HP in the HIE is high but the cost of providing value-added services for each $H P ~ i s$ low, then the HIE is established because of an interest in the value-added services. On the other hand, if both of these costs are high, the HIE is not established, and hence no HP can request value-added services. In particular:

$( 1 ) \ I f c _ { b } > g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and $c _ { v } < \Gamma ,$ then $0 \leq$ $N _ { b } = N _ { v } \le \operatorname* { m i n } { \{ 3 \bar { r } N / ( 5 ( \bar { r } - \underline { { r } } ) ) , N \} } .$

$( 2 ) \ I f c _ { b } > g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and $c _ { v } > \Gamma .$ , then $N _ { b } =$ $N _ { v } = 0 .$

(b) If the cost of maintaining each HP in the HIE is relatively lower, value-added services help increase the network size in two settings. In particular, $( N \bar { r } +$ $\sqrt { N ( N \bar { r } ^ { 2 } - 3 ( \bar { r } - \underline { { r } } ) ( c _ { b } - g ) ) } ) / ( \tilde { 3 } ( \bar { r } - \underline { { r } } ) ) < N _ { b } = N _ { v } \leq$ min $\{ 3 \bar { r } N / ( 5 ( \bar { r } - \underline { { r } } ) ) , N \} ~ i f$

$( 1 ) \ g + 3 \bar { r } ^ { 2 } N / ( 2 5 ( \bar { r } - \underline { { r } } ) ) \leq c _ { b } \leq g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and $\underline { { r } } < 2 \bar { r } / 5$ or

(2) $g + N ( 3 \underline { { r } } - \bar { r } ) \le c _ { b } \le g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ and $2 \bar { r } / 5 \le \underline { { r } } \le \bar { r } / 2$

(c) If the cost of maintaining each HP in the HIE is low so that all HPs are already in the HIE, some portion or all of the HPs might request the value-added services

## Figure 3 Lemma 5: Equilibrium Network Size

![](/api/attachments/CYEN9VEX/fulltext/images/15472d5636e68620412b34c9dd9727ab85dbb59aeac2c244d5b31574da163a2f.jpg)

under two circumstances. In particular, $N _ { b } = N \geq N _ { v } =$ min $\{ 3 \bar { r } N / ( 5 ( \bar { r } - \underline { { r } } ) ) , N \} ~ i$ f

(1) $c _ { b } \leq g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) ) \ a n d \ \underline { { r } } \geq \bar { r } / 2$ or

(2) $c _ { b } \leq g + N ( 3 \underline { { r } } - \bar { r } )$ and $\bar { r } / 3 - g / ( 3 N ) \le \underline { { r } } \le \bar { r } / 2 .$

(d) If there is a partial network without value-added services, and if the cost is relatively small, only a portion of the HPs in the HIE will request value-added services. This is true under two circumstances. In particular, $N \geq N _ { b } =$ $( N \bar { r } + \sqrt { N ( N \bar { r } ^ { 2 } - 3 ( \bar { r } - \underline { { r } } ) ( c _ { b } - g ) ) } ) / ( 3 ( \bar { r } - \underline { { r } } ) ) \ge N _ { v } =$ $3 { \bar { r } } N / ( 5 { \dot { ( r - \underline { { r } } ) } } ) \ i f$

$$
(1) c _ {b} <   g + 3 \bar {r} ^ {2} N / (2 5 (\bar {r} - \underline {{r}})) a n d \underline {{r}} <   \bar {r} / 3 - g / (3 N)
$$

$( 2 ) \ g + N ( 3 \underline { { r } } - \bar { r } ) < c _ { b } < g + 3 \bar { r } ^ { 2 } N / ( 2 5 ( \bar { r } - \underline { { r } } ) )$ and $\bar { r } / 3 - g / ( 3 N ) \le \underline { { r } } \le 2 \bar { r } / 5 .$

If the HIE provider does not offer value-added services, the HIE network cannot be established when the cost of accommodating each HP in the HIE $( \mathrm { i . e . , } ~ c _ { b } )$ is more than $g + \bar { r } ^ { 2 } N / ( 4 ( \bar { r } - \underline { { r } } ) )$ (as discussed in part (c) of Lemma 1). On the other hand, in such a case, if the value-added service is provided and its cost per HP is sufficiently low $( \mathrm { i } . \mathrm { e } . , c _ { v } < \Gamma )$ , the HIE is established, and each of the participating HPs request the value-added service (as shown in part (a)(1) of Lemma 5). In this case, these HPs join the network mainly because of the value-added service. In some other cases outlined in part (b) of Lemma 5, the value-added service helps the HIE provider enlarge the network. On the other hand, in parts (c) and (d) of Lemma 5, only a portion of the HPs that are already in the network request the value-added service. Therefore, in these cases, the HIE network does not expand because of the value-added service.

Heterogeneity among the HPs does not have a significant role in determining whether or not valueadded services will increase participation in the HIE. However, it is apparent from parts (a) and (b) of Lemma 5 that the cost of accommodating each HP in the HIE $( \mathrm { i . e . , ~ } c _ { b } )$ has an important role. In addition, although the cost of value-added service per HP $( \mathrm { i } . \mathrm { e } . , c _ { v } )$ does not appear in part (b) of Lemma ${ \hat { 5 } } ,$ it affects the participation in the cases depicted in part (a). Hence, the key takeaway is that if the cost of accommodating each HP in the HIE is prohibitively large, the government might consider reimbursing costs related to providing value-added services. That would reduce $c _ { v }$ and may promote participation in the network. On the other hand, if the cost of accommodating each HP in the HIE is not prohibitively large, reimbursing costs related to providing value-added services does not entice more participation in the network.

Now, in the following lemma, we present the optimal levels of the value-added service and the fees, and analyze them in subsequent propositions. For brevity, we present and analyze the results only for part (d) of Lemma 5. This case possibly represents one of the most interesting scenarios where (i) the partial network exists even without the value-added services and (ii) the network size does not increase because of the value-added services. However, for completeness, we also analyze parts (a) and (b) of Lemma 5 and discuss whether the key findings for these cases change compared to those for part (d).

<sup>Lemma</sup> <sup>6.</sup> For part (d) of Lemma 5, the optimal level of value-added service $( i . e . , s ^ { * } )$ , the optimal value-added service fee $( i . e . , p _ { v } ^ { * } )$ , and the optimal HIE network subscription fee $( i . e . , p _ { b } ^ { * } )$ are given by

$$
\begin{array}{c} s ^ {*} = \frac {3 \bar {r} ^ {2} N d}{2 5 c _ {v} (\bar {r} - \underline {{r}})}, \\ p _ {v} ^ {*} = \frac {1 8 \bar {r} ^ {4} N ^ {2} d ^ {2}}{6 2 5 c _ {v} (\bar {r} - \underline {{r}}) ^ {2}}, \\ p _ {b} ^ {*} = \frac {N \bar {r} ^ {2} + 3 (\bar {r} - \underline {{r}}) (c _ {b} - g) + \bar {r} \sqrt {N (N \bar {r} ^ {2} - 3 (\bar {r} - \underline {{r}}) (c _ {b} - g))}}{9 (\bar {r} - \underline {{r}})}. \end{array}
$$

In the proof of Lemma $^ { 6 , }$ we also present the sensitivity analyses of $s ^ { * } , p _ { v } ^ { * } ,$ , and $p _ { b } ^ { * }$ with respect to the upper and lower bounds of the benefit parameter r¯ and r. These sensitivity analyses yield the following insights. First, $s ^ { * } , p _ { v } ^ { * } ,$ and $p _ { b } ^ { * }$ increase with r¯ and r. Hence, an important question arises: When HPs expect more benefits from the HIE $( \mathrm { i } . \mathrm { e } . , \bar { r }$ or r increases), will there be (i) more HPs interested in value-added services (because of the increased level of the service) or (ii) fewer HPs interested in value-added services (because of the increase in fees for both the value-added service and the base HIE subscription)? Interestingly, part (d) of Lemma 5 reveals the following results.

<sup>Proposition</sup> <sup>5.</sup> For part (d) of Lemma 5:

(a) If the minimum benefit $( i . e . , \underline { { r } } )$ increases, more HPs will join the HIE $( i . e . , N _ { b }$ increases) and more HPs will request the value-added service $( i . e . , N _ { \tau }$ increases).

(b) If the maximum benefit (i.e., r¯) is increased, a smaller number of HPs will request the value-added service $( i . e . , N _ { v }$ decreases). The network size $( i . e . , N _ { b } )$ will increase if and only if the heterogeneity and the cost of accommodating each HP in the HIE are both moderately high, in particular, if and only $i f \bar { r } > 1 0 \underline { { r } }$ and $c _ { b } > g + 4 \underline { { r } } N / 3 .$

This result can be explained as follows. When the minimum benefit parameter increases, it is beneficial for the HIE provider to expand its network and provide value-added services to a larger group of HPs. On the other hand, when the maximum benefit increases, similar to Proposition 3, under certain conditions, the equilibrium network size increases with an increase in heterogeneity. This happens when both heterogeneity and the cost (of maintaining each HP in the HIE) are moderately high. In such a case, the HIE provider finds it more beneficial to entice more HPs into the network. On the other hand, if the heterogeneity is not large, in particular, if $\hat { r } < 1 0 \underline { { r } } ,$ introducing more benefits to the HPs by increasing the upper bound actually decreases the participation in the network. In those cases, the HIE provider focuses on high-gain HPs to collect more value from them. Besides, increasing the maximum benefit would reduce the number of HPs that request the value-added service since the HIE provider always finds it more beneficial to focus on high-gain HPs.

Our extensive numerical experiments (presented in the proof of Proposition 5) reveal that the HIE settings outlined in parts (a) and (b) of Lemma 5 depict the same behavior outlined in part (a) of Proposition 5. On the other hand, in these settings, we observe that if r¯ increases, a fewer number of HPs will join the HIE and a fewer number of HPs will request the value-added service. Now, in the following lemma, we present the equilibrium net values of HPs and the HIE provider. Again, we focus on the conditions presented in part (d) of Lemma 5.

<sup>Lemma</sup> <sup>7.</sup> For part (d) of Lemma 5, the net values of HP i (that joins both networks) and the HIE provider at the equilibrium are given by

$$
\begin{array}{r l} & {\frac {9 d ^ {2} N ^ {2} \bar {r} ^ {3} (5 r _ {i} - 2 \bar {r})}{6 2 5 c _ {v} (\bar {r} - \underline {{r}}) ^ {2}} - \frac {(c _ {b} - g)}{3}} \\ & {\qquad + \frac {\sqrt {N (N \bar {r} ^ {2} - 3 (c _ {b} - g) (\bar {r} - \underline {{r}}))}}{9 (\bar {r} - \underline {{r}}) (3 r _ {i} - \bar {r}) ^ {- 1}}} \end{array}
$$

and

$$
\begin{array}{l} \frac {2 7 d ^ {2} N ^ {3} \bar {r} ^ {5}}{3 1 2 5 c _ {v} (\bar {r} - \underline {{r}}) ^ {3}} - \frac {N \bar {r} (c _ {b} - g)}{9 (\bar {r} - \underline {{r}})} \\ + \frac {\sqrt {N (N \bar {r} ^ {2} - 3 (c _ {b} - g) (\bar {r} - \underline {{r}}))} + N \bar {r}}{2 7 (\bar {r} - \underline {{r}}) ^ {2} (2 \bar {r} ^ {2} N - 6 (c _ {b} - g) (\bar {r} - \underline {{r}})) ^ {- 1}} \end{array}
$$

respectively.

Sensitivity analyses of these values with respect to different parameters reveal several interesting results. First, we find that although the heterogeneity among HPs has an important role in determining the behavior of values of all participating HPs, the individual benefit parameters of HPs $( \bar { \mathrm { i } } . \mathrm { e } . , \bar { r _ { i } } )$ have the most vital role. In particular, a change in any parameter might imply opposite effects for high-gain (HPs that have high $r _ { i }$ values) and low-gain HPs (HPs that have low $r _ { i }$ values). We present one such finding in the following proposition, along with some other results, and provide the proof in the online appendix.

<sup>Proposition</sup> <sup>6.</sup> (a) If the highest benefit the HPs can get from the HIE $( i . e . , \bar { r } )$ increases, the value of HP i at the equilibrium

(1) decreases if the benefit parameter $r _ { i }$ is less than ${ \scriptstyle \frac { 4 } { 5 } } \bar { r } ;$

(2) might increase if the benefit parameter $r _ { i }$ is $h i g h ,$ the heterogeneity is high, and the value-added service is highly beneficial $( i . e . ,$ d is high). For example, it increases if $\begin{array} { r } { r _ { i } > \frac { 4 } { 5 } \bar { r } , ~ \underline { { r } } = 0 . } \end{array}$ , and

$$
d > \frac {2 5 \sqrt {c _ {v} (3 (c _ {b} - g) (\bar {r} + 3 r _ {i}) - 2 \bar {r} (\sqrt {\bar {r} N (\bar {r} N - 3 (c _ {b} - g))} + \bar {r} N))}}{9 \sqrt {2} \sqrt {\bar {r} N \sqrt {\bar {r} N (\bar {r} N - 3 (c _ {b} - g))} (5 r _ {i} - 4 \bar {r})}}.
$$

(b) If the minimum benefit HPs can get from the HIE $( i . e . , \underline { { r } } )$ increases, the equilibrium values of all HPs increase.

When the HIE provider does not offer value-added services, an increase in the maximum benefit HPs can get from the HIE decreases the values of all HPs (as explained in part (a) of Proposition 4). Furthermore, our extensive numerical experiments show that the HIE settings outlined in parts (a) and (b) of Lemma 5 also depict the same behavior.<sup>10</sup> However, as stated in Proposition $6 ( \mathsf { a } ) ( 2 )$ , an increase in the highest benefit the HPs can get from the HIE actually increases the value of some participants in some cases. Hence, in part (d) of Lemma 5, i.e., when the HIE provider offers the value-added service (unlike the settings in Proposition 4) and when the cost of providing base HIE service to each HP in the HIE is relatively low (unlike parts (a) and (b) of Lemma 5), the HIE provider might react less aggressively if the highest benefit the HPs can get from the HIE $( \mathrm { i } . \mathrm { e } . , \bar { r } )$ increases. Hence, value-added services, particularly when the cost of providing base HIE service to each HP in the HIE is relatively low, can actually help HPs in extracting more value from their HIE membership even when the heterogeneity among them increases because of an increase in r¯.

Proposition 6(b) shows that the equilibrium values of all HPs increase if the minimum benefit HPs can get from the HIE (i.e., r) increases. Our numerical experiments show that the HIE settings outlined in parts (a) and (b) of Lemma 5 have the same behavior. On the other hand, when the HIE provider does not offer the value-added service, an increase in r does not necessarily increase the values of the participating HPs (as described in part (b) of Proposition 4). Hence, value-added services are beneficial again because they ensure an increase in values of all participating HPs with an increase in $\underline { { r } } .$

Finally, the HIE provider benefits from an increase in both r¯ and $\underline { { r } } .$ This result is the same as that in the benchmark case analyzed in the previous subsection. Now, in $\ S 5 ,$ we discuss the implications of our research for different parties and propose future research topics.

## 5. Implications and Conclusions

Our goal in this paper is to provide useful insights for all of the key parties involved in the sustainability of HIEs: (i) the healthcare practitioners, (ii) the HIE providers, and (iii) the policy makers. To develop our main model, we worked with ICC and Critical Connection, two well-established HIEs based in Texas that offer value-added services to participating HPs in addition to the base HIE service. While building this model, we also interacted with the start-up HIE SETHS (based in Texas) that does not offer value-added services. We model this setting in the benchmark case that helps us understand the issues involved when the HIE provider does not offer value-added services. Although our main model and the benchmark case are based on these three HIEs, they are generic, and the results as well as the insights are applicable to most of the HIE settings. In §5.1, we discuss our key findings.

## 5.1. Implications

As discussed above, in the benchmark case, we analyze a setting where the HIE provider offers only the base service (typical for many start-up HIEs). As expected, we find that the cost of accommodating each HP in the HIE plays the most important role in determining whether an HIE is established or not. We find that if this cost is not prohibitive or if there is enough government support, the heterogeneity among HPs (in terms of their expected benefit from the HIE membership) determines the extent of participation in the HIE. In particular, we find that some low-gain HPs choose not to join the HIE if there are high-gain HPs in the region. Hence, we propose three different strategies for policy makers and HIE providers that can help boost participation in HIEs: (i) increase the minimum benefit HPs can get from the HIE, (ii) establish additional HIEs to focus more on low-gain HPs, and (iii) incentivize or offer HIE-related value-added services.

Increasing the minimum benefit the HPs can obtain from the HIE entices small HPs to join the network. The policy makers can do so by increasing the amount of proposed funds and incentives. Another possible strategy is to offer electronic health record applications for free or at a very low price to the HPs that do not have functional EHRs. In the United States, several HIE providers are already offering this incentive. On the other hand, increasing the maximum benefit the HPs can obtain from the HIE might even be detrimental to participation under certain circumstances. The reason is that increasing the minimum gain decreases the heterogeneity among HPs, whereas an increase in the maximum benefit increases the heterogeneity.

We also find that, although the incentives by the government and other agencies encourage a larger HIE network, these incentives cannot entice all HPs to join the network when the heterogeneity among the HPs is high. Hence, the policy makers should be careful about when, to whom, and how much incentive to offer. The reason is that, under certain conditions, the HIE provider may try to extract more value if the values of participating HPs are increased. In these cases, it may simply prefer a smaller HP pool that can afford a higher subscription fee, instead of a higher number of HPs with a lower subscription fee. We also find that, in the benchmark case, the HIE provider decides to establish the HIE network only if a substantial portion of the HPs in the region find it beneficial to participate. Hence, the HIE provider should be careful in planning its strategies regarding which HPs to focus on.

The second option is to establish an additional HIE that should focus more on developing solutions for low-gain HPs and increasing their benefits. This would entice more HPs to join the network. Hence, under certain conditions, there is an incentive for the policy makers to establish more than one HIE in the same region. For example, SETHS has a focus on rural hospitals, and this seems to be an effective practice that increases participation.

As a third option, the HIE providers may offer the HIE related value-added services that might help increase participation in their networks. Therefore, in our main model, we examine how the HIE provider decides on the level of the value-added service and its fee, and which HPs request these services. In addition, we analyze the conditions when the value-added services expand the network. We find that, under certain conditions, the value-added services indeed help sustain the HIE. In some of these cases, the HIE is established only when the value-added services are offered to HPs. In some other cases, the value-added services can increase the number of participants in the HIE. Therefore, policy makers should consider incentivizing HIE-related value-added services to increase the number of participants in the HIE. In addition, we glean several other managerial insights that would be useful for policy makers, HIE providers, and HPs.

## 5.2. Future Research Directions

There are several future research possibilities in the domain of sustainability of HIEs. Here, we would like to discuss some of them. We already validated our modeling choices with the HIEs we work with. However, it would be valuable to empirically validate our results using transaction and encounter data from HIE providers. Here, transaction data refers to the data regarding the interactions of an HIE provider with the HPs, and encounter data refers to the interactions of HPs with the patients.

Some HIE providers are trying newer business models that are worth exploring. One such example is co-op services where an HP in the network is bound to make purchases of office or medical supplies from third parties (such as Staples and OfficeMax) that are selected by the HIE provider. In these settings, the HIE provider gets a percentage of the revenues from such transactions. Hence, there are three different parties involved in such a setting. To analyze this setting, one needs to modify our model to include third parties.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0626.

## References

Adjerid I, Acquisti A, Padman R, Telang R, Adler-Milstein J (2011) Impact of health disclosure laws on health information exchanges. Tenth Workshop Econom. Inform. Security, George Mason University, Fairfax, VA).

Adler-Milstein J, DesRoches CM, Jha AK (2011) Health information exchange among U.S. hospitals. Amer. J. Managed Care 17(11): 761–768.

Agarwal R, Angst C, DesRoches CM, Fischer MA (2010a) Technological viewpoints (frames) about electronic prescribing in physician practices. J. Amer. Medical Informatics Assoc. 17(4): 425–431.

Agarwal R, Crowley PK, Mithas S, Khuntia J (2010b) The District of Columbia Regional Health Information Organization (DC RHIO) current progress and the road ahead. Center for Health Information and Decision Systems, Robert H. Smith School of Business, University of Maryland, College Park.

Agarwal R, Gao G, DesRoches C, Jha AK (2010c) Research commentary—The digital transformation of healthcare: Current status and the road ahead. Inform. Systems Res. 21(4): 796–809.

Agency for Healthcare Research and Quality (2006) Evolution of state health information exchange: A study of vision, strategy, and progress. Publication No 06-0057, Agency for Healthcare Research and Quality, Rockville, MD.

Anderson C, Agarwal R (2011) The digitization of healthcare: Boundary risks, emotion, and consumer willingness to disclose personal health information. Inform. Systems Res. 22(3):469–490.

Angst CM, Agarwal R (2009) Adoption of electronic health records in the presence of privacy concerns: The elaboration likelihood model and individual persuasion. MIS Quart. 33(2):339–370.

Aron R, Dutta S, Janakiraman R, Pathak PA (2011) The impact of automation of systems on medical errors: Evidence from field research. Inform. Systems Res. 22(3):429–446.

Berry K, Johnson G (2012) Introduction to HIE landscape. National eHealth Collaborative Seminar Ser.

Bohmer RMJ (2011) The four habits of high-value health care organizations. New England J. Medicine 365(22):2045–2047.

Calhoun S (2013) Executive Director, Southeast Texas Health System. Personal communication with the authors.

Centers for Medicare and Medicaid Services (2014) National health care expenditures data. http://www.cms.gov/Research -Statistics-Data-and-Systems/Statistics-Trends-and-Reports/ NationalHealthExpendData/NationalHealthAccountsHistorical .html.

Covich J, Morris G, Bates M (2011) Determining the path to HIE sustainability. Truven Health and EHealth Initiative, Woodlawn, MD. http://truvenhealth.com/portals/0/assets/GOV\_11559 \_0912\_HIE\_Sustainability\_WP\_Web.pdf.

Dixon B, Zafar A, Overhage JM (2010) A framework for evaluating the costs, effort, and value of nationwide health information exchange. J. Amer. Medical Informatics Assoc. 17(3): 295–301.

Farrell J, Klemperer P (2007) Coordination and lock-in: Competition with switching costs and network effects. Armstrong M, Porter R, eds. Handbook of Industrial Organization, Vol. 3 (North-Holland, Amsterdam), 1967–2072.

Feldman SS, Horan TA, Drew D (2013) Value proposition of health information exchange: The case of uncompensated care cost recovery. Health Systems 2(2):134–146.

Fontaine P, Zink T, Boyle RG, Kralewski J (2010) Health information exchange: Participation by Minnesota primary care practices. Archives Internal Medicine 170(7):622–628.

Fudenberg D, Tirole J (2000) Pricing a network good to deter entry. J. Indust. Econom. 48(4):373–390.

Hall SD (2013) Florida HIE adapts to changing federal rules, focuses on sustainability. Fierce Health IT (February 4), http://www.fiercehealthit.com/story/florida-hie-adapts-changing -federal-rules-focuses-sustainability/2013-02-04.

Healthcare Information and Management Systems Society (2009a) Defining health information exchange. White paper, Healthcare Information and Management Systems Society HIE Guide Work Group, Chicago.

Healthcare Information and Management Systems Society (2009b) HIE evaluation checklist. White paper, Healthcare Information and Management Systems Society HIE Guide Work Group, Chicago.

Jing B (2007) Network externalities and market segmentation in a monopoly. Econom. Lett. 95(1):7–13.

Joshi J (2010) Clinical value-add for health information exchange (HIE). Internet J. Medical Informatics 6(1), http://ispub.com/IJMI/ 6/1/10075.

Kolkman L, Brown B (2011) The Health Information Exchange Formation Guide: The Authoritative Guide for Planning and Forming an HIE in your State, Region or Community (HIMSS, Chicago).

Lorenzi NM (2003) Strategies for creating successful local health information infrastructure initiatives. Success/Failure Report, Reference No. 03EASPE00772, Local Health Information Infrastructure, Nashville.

Marchibroda JM (2007) Health information exchange policy and evaluation. J. Biomedical Informatics 40(6-Suppl1):S11–S16.

Menon NM, Kohli R (2013) Blunting Damocles’ sword: A longitudinal model of healthcare IT impact on malpractice insurance premium and quality of patient care. Inform. Systems Res. 24(4): 918–932.

Menon NM, Lee B, Eldenburg L (2000) Productivity of information systems in the healthcare industry. Inform. Systems Res. 11(1): 83–92.

Mishra AN, Anderson C, Angst C, Agarwal R (2012) Electronic health records assimilation and physician identity evolution: An identity theory perspective. Inform. Systems Res. 23(3): 738–760.

Mostashari F, Tripathi M, Kendall M (2009) A tale of two large community electronic health record extension projects. Health Affairs 28(2):345–356.

Niculescu MF, Shin H, Whang S (2012) Underlying consumer heterogeneity in markets for subscription-based IT services with network effects. Inform. Systems Res. 23(4):1322–1341.

Ozdemir Z, Barron J, Bandyopadhyay S (2011) An analysis of the adoption of digital health records under switching costs. Inform. Systems Res. 22(3):491–503.

Page D (2010) Health information exchanges hold promise, pose perils. Hospitals Health Networks 84(1):12.

Patel VN, Dhopeshwarkar RV, Edwards A, Barron Y, Sparenborg J, Kaushal R (2012) Consumer support for health information exchange and personal health records: A regional health information organization survey. J. Medical Systems 36(3): 1043–1052.

Prasad A, Venkatesh R, Mahajan V (2010) Optimal bundling of technological products with network externality. Management Sci. 56(12):2224–2236.

PRWeb (2012) Healthcare IT spending to grow by triple digits: Black Book HIE survey. (May 31), http://www.prweb.com/releases/ %202012/5/prweb9550653.htm.

Romanow D, Sunyoung C, Straub D (2012) Riding the wave: Past trends and future directions for health IT research. MIS Quart. 36(3):iii–x.

Samuels M (2013) Chief Executive Officer, Centex System Support Services, Integrated Care Collaboration. Personal communication with the authors.

Smitherman M (2013) Chief Executive Officer, Critical Connection. Personal communication with the authors.

Sridhar S, Brennan PF, Wright SJ, Robinson SM (2012) Optimizing financial effects of HIE: A multi-party linear programming approach. J. Amer. Medical Informatics Assoc. 19(6):1082–1088.

Sundararajan A (2003) Network effects, nonlinear pricing and entry deterrence. Working paper, New York University, New York.

Sundararajan A (2004) Nonlinear pricing and type-dependent network effects. Econom. Lett. 83(1):107–113.

Terry K (2013) Health information exchange debate gets fiery. InformationWeek (February 4), http://www.informationweek.com/

interoperability/health-information-exchange-debate-gets -fiery/d/d-id/1108508?.

Vest JR, Jasperson J (2010) What should we measure? Conceptualizing usage in health information exchange. J. Amer. Medical Informatics 17(3):302–307.

Walker J, Pan E, Johnston D, Adler-Milstein J, Bates W, Middleton B (2005) The value of health care information exchange and interoperability. Health Affairs (January):5–18.

Weinberger SE (2011) Providing high-value, cost-conscious care: A critical seventh general competency for physicians. Ann. Internal Medicine 155(6):386–388.

Yaraghi N, Du AY, Sharman R, Gopal R, Ramesh R (2013) Network effects in health information exchange growth. ACM Trans. MIS 4(1):1–26.

Yaraghi N, Du AY, Sharman R, Gopal R, Ramesh R (2014) Professional and geographical proximity effects on HIE adoption. J. Amer. Medical Informatics Assoc. 21(4):671–678.
