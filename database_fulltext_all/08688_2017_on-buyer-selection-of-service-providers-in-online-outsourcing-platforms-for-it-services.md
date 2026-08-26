---
otero_id: 8688
otero_key: "DQYFDMHR"
title: "On Buyer Selection of Service Providers in Online Outsourcing Platforms for IT Services"
authors: "Yili Hong; Paul A. Pavlou"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0709"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/DQYFDMHR/fulltext/images/8c3b858607bdca973e44e7005695f95a2cb6adf3ad2191f24090d5330e6c7028.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# On Buyer Selection of Service Providers in Online Outsourcing Platforms for IT Services

Yili Hong, https://doi.org/0000-0002-8830-5727Paul A. Pavlou

To cite this article:

Yili Hong, https://doi.org/0000-0002-8830-5727Paul A. Pavlou (2017) On Buyer Selection of Service Providers in Online Outsourcing Platforms for IT Services. Information Systems Research

Published online in Articles in Advance 20 Apr 2017

http://dx.doi.org/10.1287/isre.2017.0709

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/DQYFDMHR/fulltext/images/deb1131b9b80679df0923f179cebe0559342b77bb3297909d77c5dbb2124e142.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# On Buyer Selection of Service Providers in Online Outsourcing Platforms for IT Services

Yili Hong,<sup>a</sup> Paul A. Pavlou<sup>b</sup>

<sup>a</sup> W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287; <sup>b</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122

Contact: hong@asu.edu (YH); pavlou@temple.edu, https://doi.org/0000-0002-8830-5727 (PAP)

Received: June 17, 2015 Revised: July 11, 2016; November 8, 2016 Accepted: December 19, 2016 Published Online in Articles in Advance: April 20, 2017

https://doi.org/10.1287/isre.2017.070

Copyright: © 2017 INFORMS

Abstract. The Internet has presumably created a level playing field that allows any service provider across the globe to compete for contracts on online outsourcing platforms for information technology (IT) services. In this paper, we empirically examine (a) how country (language, time zone, cultural) diferences and the country’s IT development afect buyers’ selection of service providers in online outsourcing platforms; and (b) how the reputation of service providers moderates the proposed efects of country diferences and the country’s IT development. We integrated a unique data set formed by a sample of 11,541 software development projects from an online outsourcing platform matched with archival sources on the language, time zone, culture, and IT development of countries. Since price is typically endogenous in any supply demand system, we used the exogenous variation of the normalized exchange rate of the currency among countries, as a “cost-shifter” type instrumental variable (IV) for econometric identification. Our panel data analyses results (both with and without IV) show that buyers are negatively afected by country diferences in terms of language, time zone, and culture, and prefer service providers from countries with higher IT development. Notably, the reputation of service providers attenuates the negative efects of language and cultural (but not time zone) diferences, while it substitutes the positive efect of the country’s IT development. We discuss the study’s theoretical and managerial implications for understanding the global dynamics of online outsourcing platforms and better designing these platforms.

History: Il-Horn Hann, Senior Editor; Sunil Mithas, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0709.

Keywords: online outsourcing platforms • IT services • country diferences • country IT development • reputation

## 1. Introduction

Online outsourcing platforms (also known as “online labor markets”) are Internet-enabled systems that bring together service providers and buyers<sup>1</sup> from around the world to contract information technology (IT) services, such as software development. Because of the Internet’s ubiquitous access, online outsourcing platforms, such as Freelancer, eLance, and oDesk, emerged as a viable means for outsourcing IT services across the globe. As early as 1998, an article featured in the Harvard Business Review by Malone and Laubacher (1998) had envisioned the “gig economy,”<sup>2</sup> alluding to the proliferation of online outsourcing platforms.<sup>3</sup> Besides attracting attention from the popular media, online outsourcing platforms have also received academic attention, with a central focus on how the individual reputation of service providers ofered by their feedback ratings (through the reputation system) (e.g., Lin et al. 2017, Kokkodis and Ipeirotis 2015, Moreno and Terwiesch 2014, Yoganarasimhan 2013) afect the buyers’ selection of service providers.

As the majority of online outsourcing platforms follow a buyer-determined, reverse auction mechanism (Hong et al. 2016), the buyers’ selection of service providers is a major step in the outsourcing process. When making a selection, because of the geographically distributed environment, unfamiliar service providers, and the complexity of software development, buyers are unable to perfectly assess the service providers’ functional competency to manage the software development process and their technical competency to ensure software quality (Grönroos 1984, Malone and Crowston 1994). While some have asserted that online outsourcing platforms provide ubiquitous access with no geographical constraints (Friedman 2007), country diferences still matter in many contexts such as prosocial lending (Burtch et al. 2014), bank loans (Giannetti and Yafeh 2012), and outsourcing (Nakatsu and Iacovou 2009). In the context of this study—online outsourcing platforms for IT services— any service provider across the globe could bid to ofer IT services. On one hand, like other online markets, online outsourcing platforms reduce search costs that buyers would likely incur of-line (e.g., Forman et al. 2009, Hann and Terwiesch 2003). On the other hand, online outsourcing platforms inevitably lead to country diferences between buyers and service providers (herein termed “buyer–service provider country diferences”), such as language, time zone, and culture, which makes it challenging for service providers and buyers to work together (Herbsleb and Grinter 1999). This is because language, time zone, and cultural diferences may undermine the service providers’ functional com petency to communicate and coordinate efectively in IT projects. Since service providers come from countries with diferent levels of IT development in terms of IT infrastructure and IT access (herein termed “country IT development”), they could be perceived to possess diferent levels of technical competency. This leads to a country-level IT reputation efect, such that buyers may view service providers from countries with a higher level of IT development to possess a higher technical competency. Therefore, it is not clear whether online outsourcing platforms are level playing fields where worthy service providers are denied contracts because of the IT reputation of their country (Leamer 2007). In sum, besides the factors of bid price and the individual reputation of service providers on which the literature has focused and for which we control (e.g., Ba and Pavlou 2002, Kokkodis and Ipeirotis 2015, Moreno and Terwiesch 2014, Lin et al. 2017, Yoganarasimhan 2013), we have a limited understanding of the buyer– service provider country diferences and the service providers’ country IT development as important determinants of the buyers’ selection of service providers in online outsourcing platforms (besides price, quality, and reputation). Notably, extending prior research that has found that the individual reputation of service providers may help to address the information asymmetry that plagues online outsourcing platforms (Pavlou et al. 2007), in this study, we seek to examine whether the service providers’ individual reputation moderates the proposed efects of country diferences and the country’s IT development on the buyers’ selection of service providers. Accordingly, in this study, we seek to answer the following research questions:

(a) How do country diferences—language, time zone, and cultural—between buyers and service providers afect the buyers’ selection decision of service providers in online outsourcing platforms?

(b) How does the service provider’s level of country IT development afect the buyer’s selection decision?

(c) How does the service provider’s individual reputation moderate the efects of country diferences and the service provider’s level of country IT development on the buyers’ selection of service providers?

To answer these research questions and guide our empirical examination, we integrated the literature on IT outsourcing and software development services with the emerging literature on online outsourcing platforms to propose a set of hypotheses on the efects of country diferences (language, time zone, cultural) and country IT development, and the moderating role of the service providers’ reputation on the proposed direct efects. Utilizing a proprietary database of a leading online outsourcing platform, we directly observe buyers’ selection decisions of service providers. We merged the proprietary database with a number of publicly available data sets, namely, the GeoDist Database, the CIA World Factbook, the International Telecommunication Union, the World Value Survey, the International Monetary Fund (IMF), and the World Economic Forum, to construct an integrated panel data set. To address potential endogeneity from the bid price of service providers, our econometric identification hinges on the exogenous variation of the normalized exchange rate of diferent currencies against the U.S. dollar as a “cost-shifter” type of instrumental variable (IV). With this IV approach, we estimated the efects of country diferences and country IT development on the buyers’ selection decision. The results show that buyers avoid all three proposed country diferences (language, time zone, and cultural) with service providers, while they prefer service providers from countries with a high level of IT development. Finally, the individual reputation of service providers attenuates the negative efects of language and cultural (but not time zone) diferences, while it attenuates the positive efect of country IT development on buyers’ selection of service providers.

This paper makes three contributions. First, it contributes to the IT outsourcing literature by empirically evaluating whether global online outsourcing platforms are a level playing field. Second, it contributes to the emerging literature on country diferences by conceptualizing that country diferences undermine the service providers’ functional competency and empirically showing their negative efects on buyer selection. Third, the study shows the moderating role of service providers’ individual reputation to (a) attenuate the observed negative efect of language and cultural (but not time zone) diferences, and (b) to attenuate the observed positive efect of the service providers’ country IT development. These findings provide theoretical implications for understanding the nature and global dynamics of online outsourcing platforms and practical implications for designing efective online outsourcing platforms.

## 2. Background and Related Literature 2.1. Study Context

Online outsourcing platforms for IT services, such as Freelancer (www.freelancer.com) and Upwork (www .upwork.com), serve as online intermediaries that bring together buyers and service providers for small to medium sized IT service projects, such as software development. Our corporate partner is a leading online outsourcing platform that uses buyerdetermined reverse auctions, a mechanism where buyers solicit bids from service providers to complete an IT service for a certain price and promised quality (e.g., Asker and Cantillon 2010). When the auction ends, the buyer evaluates the service providers’ bid prices and nonprice attributes, such as their prior work, feedback ratings, and residing country, and decides on which service provider to select (award the contract). The platform maintains a reputation system, which keeps track of the feedback ratings that service providers had received from buyers in previous projects. Interested readers can read a detailed description of the research site in Online Appendix 1.

## 2.2. Software Development Services

Research on services dates back to the 18th century (Smith 1776). Academic scholars have conjectured the everincreasing importance of services in the industrial economy (e.g., Chandler 1977, Clark 1967). Today’s economy has even been characterized as a “services economy” (Vargo and Lusch 2004), especially as productivity growth is fueled by IT services (e.g., Brynjolfsson and McAfee 2011). By reviewing the literature on services, Chase and Apte (2007, p. 380), concluded, “service performances cannot be guaranteed since they are generally delivered by human beings who are known to be less predictable than machines.” Software development services add another layer of complexity on services (e.g., Banker et al. 1998, Banker and Slaughter 2000) because they are cocreated by service providers and buyers (Kristensson et al. 2008) and typically require multiple iterations in the development process (Larman and Basili 2003). This additional layer of complexity requires that the buyer and the service provider efectively communicate and coordinate to successfully complete a project. Compared to commodity products, software development services are more idiosyncratic, complex, and intractable (e.g., Snir and Hitt 2003), noncontractible (e.g., Brynjolfsson and Smith 2000, Mithas and Krishnan 2008), with highly variable quality (e.g., Rust et al. 1999), and are often highly customized (e.g., Lin et al. 2017) since they involve specific configurations to match a buyer’s specific needs (e.g., Susarla and Barua 2011). Similarly, in contrast to the sales of commodity products in online markets (e.g., eBay or Amazon) that can be easily contracted on product descriptions, condition, and warranties, service quality has two distinct dimensions— technical quality and functional quality (e.g., Grönroos 1984)—which cannot be perfectly described ex ante (e.g., Spence 1973), nor easily contracted upon (e.g., Bakos and Brynjolfsson 1993). Noncontractible technical quality refers to the service providers’ technical competency, such as their coding and programming skills; on the other hand, noncontractible functional quality refers to service providers’ functional competency in managing the iterative development process, such as their responsiveness in communication and coordination.

Our study is also informed by the extensive information systems (IS) literature on IT outsourcing (e.g., Ang and Straub 1998, Mithas and Jones 2007, Ravindran et al. 2015, Susarla 2012, Susarla et al. 2010), which has placed much emphasis on the antecedents and consequences of transaction costs and contract design. Furthermore, we rely on the literature on distributed software development (e.g., Agerfalk et al. 2009, Cummings et al. 2009, King and Torkzadeh 2008), which has primarily focused on coordination challenges in geographically distributed development teams. Thus, software development in the context of online outsourcing platforms is at the intersection of these two literatures, and provides a unique context to extend both literatures.

## 2.3. Emerging Literature on Online Outsourcing Platforms

The emerging literature on online outsourcing platforms has primarily focused on addressing the information asymmetry between the buyers and the service providers, as the geographical dispersion between buyers and service providers renders online outsourcing platforms susceptible to deteriorating into markets of “lemons” due to adverse selection (lack of ex ante face-to-face screening) and moral hazard (lack of ex post monitoring) (Akerlof 1970). Mechanisms that mitigate asymmetric information, such as reputation, are prevalent topics in published studies (e.g., Banker and Hwang 2008, Kokkodis and Ipeirotis 2015, Moreno and Terwiesch 2014, Lin et al. 2017, Yoganarasimhan 2013) and also in working papers (e.g., Scholz and Haas 2011, Mill 2011). Other studies modeled the role of online outsourcing platforms to facilitate communication among buyers and service providers (Allon et al. 2012), enable diferent auction designs (e.g., Hong et al. 2016), and assess the service providers’ decision to use third-party certifications (e.g., Lin and Goes 2012). Finally, since a key function of online outsourcing platforms is to match buyers with service providers (Horton 2015), conventional wisdom notes that online outsourcing platforms reduce search or transaction costs (Friedman 2007, Malone and Laubacher 1998). The global reach of these online outsourcing platforms, however, naturally creates diferences across countries that may lead to practical challenges for buyers and service providers to communicate and coordinate efectively. However, extant studies largely ignored the country diferences in online outsourcing platforms, which poses a literature gap that this study seeks to fill. In terms of country diferences, prior research has ofered fragmented evidence on their efects in various business contexts. For example, Burtch et al. (2014) studied the interaction between geographical and cultural diferences in prosocial lending. Other factors, such as time zone and language diferences, have also been proposed (e.g., Gefen and Carmel 2008, Nakatsu and Iacovou 2009). Country diferences exacerbate impediments in requirements specification, communication, coordination, and the efective management of buyer–service provider interdependencies (Malone and Crowston 1994), which are important in predicting the success of software development projects (Dibbern et al. 2008). Extending the emerging literature on country diferences, we seek to comprehensively examine three major dimensions of country diferences and potential global frictions, and whether the service providers’ individual reputation could overcome their negative efects on the buyers’ selection of service providers.

## 3. Hypotheses Development

Integrating the emerging literature on country diferences (e.g., Burtch et al. 2014, Gefen and Carmel 2008, Giannetti and Yafeh 2012) and the literature on service quality (e.g., Grönroos 1984), we focus on two distinct dimensions of service providers’ competencies that determine the buyers’ selection criteria: technical competency and functional competency.<sup>4</sup> First, the service provider’s technical competency is essential to ensure the end result (e.g., the usability of the software) to be satisfactory to the buyer, as software development services are complex and specialized. Second, the provider’s functional competency in managing the iterative software development process has an impact on the service quality perceptions (e.g., Surprenant and Solomon 1987, Bitner et al. 1994, Hartline and Ferrell 1996) because buyers need to expend considerable time and efort in working with the service provider during the software development process (e.g., reviewing prototypes, providing feedback), especially with agile development approaches (Martin 2003). Below, we propose how the country (language, time zone, and cultural) diferences among buyers and service providers and the level of IT development of the service provider’s country afect the buyers’ selection of service providers in online outsourcing platforms by shaping their expectations of the service providers’ functional competency and technical competency, respectively.

## 3.1. Buyer–Service Provider Country Diferences

We now theorize the efects of buyer–service provider country diferences on the buyer’s selection. Following the emerging literature on country diferences (e.g., Burtch et al. 2014, Ghemawat 2013, Nakatsu and

Iacovou 2009), we propose three country diferences: language, time zone, and culture.

First, language barriers may impose hurdles in efective communication between service providers and buyers during the software development process. Accurate and proper use of language in communications (e.g., emails, teleconferences) can eliminate ambiguity, reduce communication costs, and avoid redundant work. As the ubiquitous access of the Internet has allowed service providers from around the world to participate in the same online outsourcing platform, often service providers and buyers from different countries speak diferent languages. As substantial communication is involved in the iterative software development process (Larman and Basili 2003) and language is the necessary medium of communication, it appears logical to propose that language diference would lead to a loss of eficiency in the software development process. The reality is that, even if the service provider does possess professional proficiency in the buyer’s primary language, the language diference might still lead to a loss of the service provider’s functional competency perceived by the buyer, and consequently, afect buyers’ selection decision.

Second, because of geographical separation, the difference in time zones in which the service providers and the buyers physically reside may lead to expected transaction costs in the software development process (Ang and Straub 1998). As most firms have fixed working hours (e.g., 9 a.m. to 5 p.m.), time zone diferences naturally impose coordination challenges for service providers and buyers because of temporal boundaries that prevent synchronized communication for integral routines of the iterative software development process, such as conference calls for updates, feedback, and sudden changes in requirements. For example, an Indian service provider cannot easily work during the same hours as a buyer in the United States, thus creating challenges for the buyer and increasing her transaction costs. Even with asynchronous communication technologies, such as email, which allow buyers and service providers to interact intermittently, coordination challenges in countries with nonoverlapping work hours cannot be easily overcome (Cummings et al. 2009). Therefore, time zone diference is likely to lead to a perceived loss of functional competency of service providers to efectively manage the coordination of the development process, thus potentially afecting a buyer’s selection.

Third, because culture is typically internalized by individuals in context-specific knowledge structures (Gilbert 1991, Morris and Fu 2001, Su 2015), buyers and service providers from diferent cultures are likely to have challenges in efectively working together as they may not share the same practices and norms (Rogers and Bhowmik 1970). For example, compared with service providers from individualist countries, service providers from countries that promote high conformism would need the upfront requirements specifications to be very detailed; accordingly, such cultural diferences may increase specification efort (Dibbern et al. 2008). Also, negotiation and information gathering are important aspects of precontractual activities because of the complexity of software development. Cultural diferences could make negotiations more cumbersome (Giannetti and Yafeh 2012) and reduce trust (Rai et al. 2009) between service providers and buyers, increasing the cost of contracting and information gathering. Cultural diferences are thus also likely to lead to a perceived loss of functional competency of service providers and afect buyers’ selection.

In sum, these three proposed country diferences (time zone, language, and cultural) between buyers and service providers could undermine the buyers’ perceived functional competency of service providers, specifically in terms of their ability to efectively negotiate, communicate, and coordinate with the buyers in the software development process. Therefore, we propose the following hypothesis for testing:

Hypothesis 1 (H1). Buyers prefer service providers with small country diferences, specifically (a) language diference, (b) time zone diference, and (c) cultural diference.

## 3.2. Country IT Development

We propose that variations in the IT development of the service providers’ residing countries afect the buyer’s selection decisions. Adopting the World Economic Forum’s conceptualization, we define the country IT development as the economic development that focuses on the country’s IT infrastructure, its citizen’s access to IT, and their overall IT skills (Dutta et al. 2015). Country IT development may indicate the countrylevel reputation for technical competency based on the following rationale: First, IT development at the country level reflects the country’s overall IT infrastructure. Service providers in countries with higher IT development may benefit from easier access to advanced IT infrastructure, and they are expected to deliver higher quality IT services. Second, it is well known that countries have diferent qualities in terms of IT education and training, and countries with higher IT development generally have earlier and higher quality IT education, which enables service providers to gain better IT skills. Based on the above theorization, buyers prefer service providers from countries where IT development is higher. Accordingly, we propose the following:

Hypothesis 2 (H2). Buyers prefer service providers from countries with a higher level of IT development.

## 3.3. Moderating Role of the Individual Reputation of Service Providers

An important function of the reputation system in online outsourcing platforms is to diferentiate competent service providers from incompetent ones (Lin et al. 2017, Moreno and Terwiesch 2014). Reputation is based on the service providers’ past performance (Banker and Hwang 2008), and it reflects either the service provider’s technical competency to deliver a high-quality software or his functional competency to efectively manage the software development process. We argue that the service provider’s reputation could substitute (or overcome the lack of) the competencies that are perceptual to the buyer.

First, as noted earlier, buyer–service provider country diferences undermine the service provider’s functional competency. If a service provider has a stellar reputation, the buyer’s concern about his functional competency may be alleviated. Therefore, reputation may attenuate the negative efects of country diferences on buyer selection of service providers, as we detail for each of the three proposed country diferences. Among the proposed country diferences, time zone diference is the least perceptual, and reputation could not overcome the coordination challenges due to time zone diferences. Nevertheless, it is possible that the buyer may perceive the service provider with a better reputation to be more cooperative in adjusting his work schedule to accommodate the time zone diference. Language diference is relatively more perceptual, because, for example, even if a service provider is not from a country where English is the oficial language, he could still have full working proficiency in the English language. Thus, reputation is likely to alleviate the lack of functional competency because of language diferences. Similarly, for cultural diferences, the same rationale for language diferences could apply. Furthermore, we posit that with greater country diferences, information asymmetry between buyers and service providers is greater. Therefore, buyers may care more about individual reputation as a selection criterion. By contrast, with smaller country diferences, information asymmetry may be less of an issue for buyers, and hence the service providers’ individual reputation may be less important to buyers. Accordingly, we propose the following:

Hypothesis 3A (H3A). The service provider’s individual reputation attenuates the negative efects of buyer–service provider country diferences on a buyer’s selection probability of a service provider.

Second, as discussed earlier, country IT development could endow service providers with a higher (countrylevel) reputation for their technical competency. Yet, a service provider’s technical competency based on their country’s IT development is not factual, but rather perceptual. For example, compared with Singapore,

Bangladesh has a very limited level of IT development; thus, ceteris paribus, a service provider from Bangladesh may be perceived to be less technically competent than a service provider from Singapore. Such country-level reputation efects have been documented in the literature (e.g., Han 1989). Based on signaling theory (Spence 1973), buyers may use the IT development level of the service provider’s country as an image attribute cue (e.g., Lefkof-Hagius and Mason 1993, Li and Wyer 1994) to infer the service provider’s technical competency, particularly when other credible signals are unavailable. Such inference may lead to aggregation bias (James 1982), such that perfectly competent service providers from countries with low IT development have a lower probability of landing contracts. However, when the service provider from Bangladesh can signal his technical competency through his individual reputation based on past performance, the positive efect of country IT development will be attenuated because the buyer no longer needs to rely on the country image to infer the service provider’s technical competency. Furthermore, we posit the opposite side of the same moderation efect that, when service providers are from countries with high levels of IT development, buyers’ concerns for technical competency may be alleviated, and therefore individual reputation would play a less important role in buyers’ selection decision. Hence, we propose the following:

Hypothesis 3B (H3B). A service provider’s individual reputation attenuates the positive efect of the country’s IT development on the buyer’s selection probability of a service provider.

## 4. Methodology

## 4.1. Data Set

We integrated a set of six archival data sources to compile our data set.

First, our main data source is the proprietary database of our corporate partner. We obtained a sample of 11,541 software development projects between August 1, 2009 and February 27, 2010. This database allows us to observe detailed information on projects, bids, buyers, and service providers. Given the scope of this study, we exclude sealed bid or time and materials contracts and only focus on open bid, fixed price projects. Also, we dropped trial projects and projects/bids submitted by spam robot agents because those projects tend to be quite diferent from normal projects and those bids were immediately removed by the platform after being identified as spam. An average project had a budget of \$380 and received about 10 bids. The public archival data sets were preprocessed and merged with the main transaction data set. The archival data sources are summarized in Table 1.

Table 1. Data Sources

<table><tr><td>Data</td><td>Source</td></tr><tr><td>Project, user, and bid characteristics data</td><td>Database of our corporate partner</td></tr><tr><td>Language data</td><td>GeoDist database, CIA World Factbook</td></tr><tr><td>Time zone data</td><td>International Telecommunication Union</td></tr><tr><td>Cultural distance data</td><td>World Value Survey</td></tr><tr><td>Exchange rate data</td><td>International Monetary Fund</td></tr><tr><td>Country IT development: Networked Readiness Index</td><td>World Economic Forum&#x27;s Global Information Technology Report</td></tr></table>

Second, we drew on a data set by Mayer and Zignago (2005) called the “GeoDist” database, that includes all oficial languages for 246 countries and independent regions, as well as an indicator of shared major languages (a binary indicator reflecting the existence of at least one language, spoken in both countries, by at least 7% of the population). We chose a binary indicator of at least one shared language. Wherever possible, additional data on language was supplemented from the CIA World Factbook to replace missing values.

Third, based on the time zone database<sup>5</sup> and location information of each buyer and service provider provided by the online outsourcing platform, we obtained our raw data on the time zone of the physical locations of service providers and buyers. We then computed the absolute time zone distance (in hours) for each service provider–buyer pair.

Fourth, we drew on a data set by the World Value Survey on the cultural diference. This data set was used in studies about the efects of cultural diference on lending decisions (Giannetti and Yafeh 2012, Burtch et al. 2014). We used a measure by Inglehart and Welzel (2010) that captures the Euclidean distance between pairs of countries regarding two dimensions of culture: traditional/secular-rational values (whether the society emphasizes religious values versus secular values) and survival/self-expression orientations (whether the society emphasizes survival values versus self-expression).

Fifth, we obtained measures for country IT development from the Global Information Technology Report released by the World Economic Forum. Data for the composite measure for country IT development— Networked Readiness Index (NRI)—for Year 2010 was used in the analyses.

Sixth, we obtained exchange rates data from the International Monetary Fund website,<sup>6</sup> which we used to construct the measure of the IV.

## 4.2. Key Measures

Buyer’s selection was measured by the variable Selection, which is captured as a dummy variable with value one if a service provider is selected, and zero if a service provider is not selected. For all of the projects used in our main analyses, the buyer selected one service provider to contract with. Note that in the data set there are projects with no buyer selection. As a robustness check, we report an analysis that uses all projects, including those that did not result in a buyer selection, in Online Appendix 2. Furthermore, we reported the results for an alternative dependent variable termed “contract,” which measures whether the project reaches a final contract after the contract is ofered to the service provider, also in Online Appendix 2. The estimated efects in these two additional analyses were qualitatively the same with those of the main analysis.

Bid Price of a service provider is an independent variable in the buyer selection model and the dependent variable in the provider pricing model. In our analysis, we use the natural logarithm of the bid price (ln(bid)), consistent with prior studies $( \mathrm { i . e . , }$ Snir and Hitt 2003, Banker and Hwang 2008, Gefen and Carmel 2008). The distribution of log-transformed data shows low skewness, a desired property for a dependent variable.

Country Diferences are measured with three variables. The first variable (language diference) measures whether the residing countries of the buyer and the service provider share any of the oficial languages (0) or not (1). The second variable (time zone diference) measures the absolute hour diference of the time zones between the service provider’s and the buyer’s cities. The third variable (cultural diference) measures the Euclidean distance between two countries on the world cultural map (Inglehart and Welzel 2010).

Country $I T$ Development was measured with the World Economic Forum’s NRI. NRI is a composite measure that comprehensively captures country-level diferences of development in IT, such as the country’s IT infrastructure, access to IT by the country’s citizens, and citizens’ IT skills of the country. The World Economic Forum is a highly regarded organization, and its Global Information Technology Report is highly cited by academic research based on Google Scholar.

Service Provider’s Reputation: We use the most commonly agreed reputation signal in online outsourcing platforms: the feedback rating (e.g., Scholz and Haas 2011, Stoll and Zöttl 2012, Yoganarasimhan 2013, Moreno and Terwiesch 2014, Lin et al. 2017) as it is visible, clear, credible, and diferentially costly (Rao and Monroe 1989, Dimoka et al. 2012). Based on prior research, we expect buyers to prefer service providers with a higher feedback rating because it is a sanctioning device that reduces the likelihood of provider shirking (Dellarocas 2006). The feedback rating is obtained from the firm database, which is actively maintained by the platform and is shown on service providers’ profile pages. As we discuss in Section 4.4.4, as a robustness check, we replaced feedback rating with service provider’s project experience and repeat the analyses, and the results were consistent (Tables A2 and A3 in Online Appendix 2).

The description and measures for the control variables are provided in Table $^ { 2 , }$ and descriptive statistics of the key variables are reported in Table 3.

## 4.3. Empirical Model and Identification

4.3.1. Panel Data Structure. Our observations are at the bid level. For each project, a buyer faces multiple bids that are submitted by service providers from diferent countries and ofer a contract to a service provider. Thus, our panel variable is the project identifier. Because of the fact that one project can only be created by one buyer, the project-level fixed efect also controls for buyer-level unobserved characteristics that are time invariant.

4.3.2. Buyer’s Selection Process. Buyer i’s utility derived from a bid submitted by a service provider j for project k is given by $\mathbf { W } _ { i j } \gamma + Z _ { j } \delta + \mathbf { X } _ { j k } \beta + p _ { j k } \lambda + u _ { i j k } ,$ where $u _ { i j k }$ are unobservable characteristics afecting the buyer’s selection of service providers. The buyer’s expected utility is a function of a number of factors, including a service provider’s functional competency, exogenously determined by buyer–service provider country (language, time zone, cultural) diferences, $\mathbf { W } _ { i j } ,$ with a common parameter vector $\gamma ;$ country IT development, $Z _ { j } ,$ , with a parameter δ; and price $p _ { j k }$ with a parameter λ, and providers’ time variant factors, $\mathbf { X } _ { i k } ,$ average feedback rating, and project experience with a common parameter vector β. We include $c _ { i k }$ and $u _ { i j k }$ in the estimation equation to capture the project-level fixed efect and individual random error, respectively. Because a project is submitted by a buyer, the project-level fixed efect also captures the buyerlevel time-invariant factors. In such an empirical setup, we do not directly observe the buyer’s utility. Instead, we observe the buyer’s selection of a service provider. Assuming the buyer selects a service provider to maximize her expected utility, we could have Equation (1) and estimate it using a linear probability model or logit model. We opt for the linear approach for two main reasons, first, note that in this estimation, the service providers’ bidding price is potentially endogenous. To address endogeneity, two-stage least squares provides the most consistent estimator. Second, since we seek to subsequently evaluate the interaction efects, a linear approach provides straightforward and reliable methods for calculating marginal efects for interpretation, whereas interaction efects in nonlinear models are typically dificult to interpret

$$
\text { Selection } _ {i j k} = \mathbf {W} _ {i j} \boldsymbol {\gamma} + Z _ {j} \delta + \mathbf {X} _ {j k} \boldsymbol {\beta} + p _ {j k} \lambda + c _ {i k} + u _ {i j k}.\tag{1}
$$

4.3.3. Service Provider’s Bidding Process. For the service provider’s bidding model, we control for project-level heterogeneities (e.g., project cost, number

Table 2. Descriptions and Measures of Control Variables

Service Provider–Project Skill Match Whether a service provider’s skills match the project requirement may afect the buyer’s perceived fit uncertainty (Hong and Pavlou 2014), which afect the willingness to ofer a contract. We used a text analytic approach to measure the similarity between the service provider’s skill and the project requirements. For each service provider–project pair, we first obtained textual data (documents) on user profile and project description, lowercased each word, removed all punctuation marks, and tokenized the documents with the NLTK (Natural Language Processing Toolkit) in Python (Bird et al. 2009). After further standard preprocessing, including removing stop words and stemming, we calculate the TF-IDF, i.e., term frequency–inverse document frequency (Leskovec et al. 2014) of the documents with the Scikit–Learn package in Python. Finally, we computed the cosine similarity (Tan et al. 2005, p. 500) between the two documents (service provider’s profile and project description) for each project–service provider pair. Service Provider’s Project Experience The service provider’s project experience is measured with the number of completed projects. This variable is log transformed because of skewness. Note that although we use service provider’s feedback rating as the main reputation variable as suggested by the literature, project experience could also indicate reputation. Those two variables are distinct yet conceptually and empirically related. In Online Appendix 2, we provide an additional robustness check by using the service provider’s project experience on the platform as the main reputation variable. Prior Familiarity Familiarity is important in software development projects, especially in the outsourcing context. Prior studies showed that a prior relationship between a service provider and a buyer can increase the chance of the service provider winning a contract (Gefen and Carmel 2008) because past experience helps reassure the buyer that the service provider can perform up to her expectations. Newly formed relationships may lack familiarity, such as common agreements about the requirements and work routine of the other party on the team (Littlepage et al. 1997). Familiarity between service providers and buyers also helps them become familiar with the task domain of their interactions (Katz 1982), handle complexity associated with software development efectively (Espinosa et al. 2007), and develop a common knowledge base (Alavi and Leidner 2001). Thus, prior familiarity alleviates the service provider’s transaction uncertainty with the buyer. With lower uncertainty, service providers are more willing to bid lower prices to buyers. We measured prior familiarity by the number of prior transactions between the provider and the buyer. Service Provider’s Hourly Rate The service provider’s hourly rate could signal his quality and thus reservation utility; therefore, it is controlled on both the buyer’s hiring and service provider’s pricing. In our data, the service provider’s hourly rate is self-reported by the service provider and shown on the service provider’s profile page. Invited Service Provider Buyers can invite providers to bid on their projects’ call for bids (CFBs). Invited providers could have a much higher chance of winning. The invited service provider measures whether a service provider was invited by the buyer to bid on the project. Buyer Experience Buyer experience is captured by the number of projects completed on the platform, at the time a project was posted. This variable is log transformed because of skewness. Bid Sequence We also control for bid sequence, based on when the provider submitted the bid, because late bidders are likely to have more information and may have a higher probability of winning a contract. One caveat we note is that bidders can revise their bids. For those cases, the platform we work with only recorded the last bid submitted in the database. Therefore, bid submission time may not be an error-free measure. Fortunately, we were able to identify those revised bids and calculate the percentage of bids that have been revised. Overall, only 8.09% of the total bids were revised. Therefore, although not perfect, the measurement error for this variable should not be substantial. We also found that those bids that had been revised are more likely to be selected Preceding Bid We control for the preceding bid for the service provider bidding model because the preceding bid could serve as an “anchor” for the current bid. For the first bid (no preceding bids), we use the project budget as the “anchor.” Because of the same reason as we noted above, this may not be an error-free measure. Service Provider Past Bidding Activity We also computed the number of projects the service provider has bid on the platform in the past 7, 14, and 30 days. Service providers’ bidding activity may be related to their bid prices because a higher level of bidding activity may suggest providers’ intention to command the highest price among diferent projects to which they submitted bids.

of overlapping projects) using the panel data, projectlevel fixed efects model. Such an approach allows us to look within IT projects to understand how country diferences, the country’s IT development, and the service provider’s individual reputation may afect his bid price. With such a modeling strategy, a provider j would place a bid $p _ { i j k }$ for project k that is initiated by buyer i. Similar to the buyer selection model, $\mathbf { W } _ { i j }$ are provider–buyer specific vector regressors (e.g., country diferences); $Z _ { j }$ is the service providers’ country IT development; $\mathbf { \boldsymbol { X } } _ { j k }$ are observed time variant vector regressors related to the service provider (e.g., the service provider’s feedback rating and his project experience); $\alpha _ { i k }$ is the unobserved project-level fixed efect (e.g., project cost or the buyer’s attributes); $\mathcal { E } _ { i j k }$ is the unobserved individual random error for each bid, which are only known by the service provider but cannot be observed by us. The estimation model is shown in Equation (2). For project-level fixed efect $\alpha _ { i k . }$ , within transformation approach is used

Table 3. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Selection</td><td>0.099</td><td>0.298</td><td>0.000</td><td>1.000</td></tr><tr><td>Bid Price</td><td>284.607</td><td>492.697</td><td>1.000</td><td>5,000.000</td></tr><tr><td>Language Difference</td><td>0.492</td><td>0.500</td><td>0.000</td><td>1.000</td></tr><tr><td>Time Zone Difference</td><td>4.921</td><td>3.250</td><td>0.000</td><td>12.000</td></tr><tr><td>Cultural Difference (Euclidean)</td><td>1.662</td><td>0.852</td><td>0.000</td><td>3.915</td></tr><tr><td>Provider&#x27;s Country IT Development</td><td>3.969</td><td>0.481</td><td>3.318</td><td>5.941</td></tr><tr><td>Feedback Rating</td><td>3.644</td><td>3.456</td><td>0.000</td><td>10.000</td></tr><tr><td>Skill Match</td><td>0.083</td><td>0.086</td><td>0.000</td><td>0.773</td></tr><tr><td>Prior Transactions</td><td>0.221</td><td>6.461</td><td>0.000</td><td>341.000</td></tr><tr><td>Provider Experience</td><td>27.408</td><td>79.538</td><td>0.000</td><td>1,457.000</td></tr><tr><td>Buyer Experience</td><td>70.523</td><td>202.804</td><td>0.000</td><td>1,681.000</td></tr><tr><td>Invited Provider</td><td>0.010</td><td>0.101</td><td>0.000</td><td>1.000</td></tr><tr><td>Provider Hourly Rate</td><td>14.355</td><td>19.450</td><td>0.000</td><td>999.000</td></tr><tr><td>Bid Sequence</td><td>11.294</td><td>12.057</td><td>1.000</td><td>164.000</td></tr><tr><td>Provider Bidding Activity (seven days)</td><td>24.684</td><td>33.594</td><td>1.000</td><td>351.000</td></tr><tr><td>XRate</td><td>1.020</td><td>0.025</td><td>0.827</td><td>1.129</td></tr></table>

$$
p _ {i j t} = \mathbf {W} _ {i j} \pmb {\theta} + Z _ {j} \vartheta + \mathbf {X} _ {j k} \pmb {\varphi} + \alpha_ {i k} + \varepsilon_ {i j k}.\tag{2}
$$

4.3.4. Identification Strategy. The key parameters to be estimated are the buyer–service provider country diferences and the service providers’ country IT development. We have four sets of independent variables (Equation (1)). First, country diferences $( \mathbf { W } _ { i j } )$ and diferences in the service provider’s country’s IT development $( Z _ { j } )$ is exogenous to the buyer’s selection because neither the service provider nor the buyer can change from where they come. Second, the service providers’ individual reputation signals $( { \pmb X } _ { j k } )$ are maintained and disclosed by the platform and not subject to any service providers’ manipulation; therefore, consistent with the literature (Banker and Hwang 2008), they are considered exogenous to the buyer’s selection decision as well. Third, the bid price of service providers, as a strategic decision of the service provider, is endogenous because a service provider sets his price in response to the expected probability that the buyer would select him, and buyers change their demand for the service provider in response to the provider’s bid price. Therefore, given the endogeneity of price in the demand system, if no valid IV is used, the estimation could be biased. A key to addressing price endogeneity is a valid IV that would exogenously determine a service provider’s bid price but has no efect on the buyers’ selection decision except through its efect on the bid price. Also, given the panel nature of the data (provider–project panel), ideally, this IV should also show a reasonable variation within the project level. To address price endogeneity, the literature has suggested three types of IVs: costshifters (e.g., Nevo 2000), price in other markets (Ghose et al. 2012), and the characteristics of competing products (e.g., Berry et al. 1995). In this study, we adopted the cost-shifter approach, which is deemed to be the most appropriate for our context.

We used the exchange rate of the local currency of the service provider as an IV. On most online outsourcing platforms (including our corporate partner at the time of our data collection), service providers submit bids in U.S. dollars (USD), whereas funds are paid in the local currency through financial institutions, such as banks and PayPal. The rationale behind using the exchange rate as an IV is that when the exchange rate against the U.S. dollar goes down (\$1 exchanges more local currency), the service provider needs a higher compensation to have the same amount of local currency to maintain the same level of income; thus, he will bid a higher price. For example, our baseline exchange rate for the Indian Rupee (INR) against the U.S. dollar on August 27, 2009 was 48.98 INR per 1 USD; whereas the exchange rate was 46.22 INR per 1 USD on December 3, 2009. Hence, the exchange rate is a natural and exogenous factor for the cost of service providers, thereby qualifying as a “cost-shifter” type of IV (Nevo 2000). The exchange rate should not afect the buyer’s preference for a given service provider since generally the fluctuation of the exchange rate will not have an impact on a country’s reputation in a short time window. We constructed a standardized measure for exchange rate (xrate) to adjust for country-specific diferences. First, the exchange rate is denoted as the amount of local currency needed to exchange for one U.S. dollar, on a daily basis, using exchange rate data provided by the IMF. Second, for each country, the exchange rate against the U.S. dollar is divided by its baseline exchange rate (the exchange rate against the U.S. dollar on July 31, 2009) to construct the variable xrate. Specifically, the IV normalized exchange rate is computed as per Equation (3)

$$
x r a t e (c, t) = \frac {e x \_ r a t e \_ t o U S D (c , t)}{e x \_ r a t e \_ t o U S D (c , 7 / 3 1 / 2 0 0 9)},\tag{3}
$$

where c indexes a currency, such as Indian Rupee, CNY, British Pound, etc., and t indexes a date.

To establish the validity of the IV, we checked for the essential assumptions (e.g., Angrist et al. 1996, Wooldridge 2002). First, the exchange rate variable shows a reasonable level of variation. Based on our data, for the most common currencies, there is a sufficient variation. For example, there is a 9.8% diference between the two dates when the Indian Rupee is the most expensive (December 3, 2009) and the date when the Indian Rupee is the cheapest (August 27, 2009) relative to the U.S. dollar; similarly, there is about a 12% diference with the British Pound. Second, to qualify as a valid instrument, the exchange rate should be correlated with the service providers’ bid prices. In this respect, the economics literature showed evidence that exchange rates have robust power in predicting global commodity prices (Chen et al. 2010). Within our sample, we observe that there is model-free evidence that a significant correlation exists between the exchange rate with the bid price $( p < 0 . 0 0 1 )$ .

## 4.4. Estimation Results and Hypotheses Testing

4.4.1. Main Efects. As detailed in Angrist and Pischke (2008), two-stage least squares (2SLS) is the most consistent and unbiased estimator for panel data with endogenous variable(s). The standard oficial panel data IV estimation procedure “xtivreg” in Stata V14, a 2SLS within estimator, was used for parameter estimation, and the results are reported in column 1 of Table 4. The strength of the instrument was assessed with a first-stage Angrist–Pischke multivariate F test of excluded instruments (details in Table 6) and also the Cragg–Donald Wald F statistic and Kleibergen–Paap Wald F statistic. Based on these diagnostic statistics, we concluded with confidence that weak instrument is not a concern. We further report estimation results for a fixed efects model without instrumenting for bid price in column 2 of Table 5.

The key estimates are reported in column 1 of Table 4. Column 2 provides qualitatively similar results using a fixed efect ordinary least squares (OLS) approach without instrumenting for bid prices. Based on the sign of the estimates, we find support for H1 and H2. First, language diference $( \beta = - 0 . 0 1 9 6 , p <$ 0.01) has a negative efect on the buyer’s selection decision. Time zone diference $( \beta = - 0 . 0 0 2 5 , p < 0 . 0 1 )$ and cultural diference $( \beta = - 0 . 0 1 5 6 , \ p < 0 . 0 1 )$ also negatively afect the buyer’s hiring decision. By contrast, the service provider’s country IT development has a positive efect on the buyer’s selection decision $( \beta = 0 . 0 4 0 6 ,$ $p < 0 . 0 1 )$ . Besides the estimates for the key variables reported above, as expected, we found bid price to have a negative efect on the buyer’s selection, whereas the service provider–project skill match, service provider– project prior transactions, the service provider’s experience, invited service provider, the service provider’s self-reported hourly rate, and bid sequence have a positive relationship with the buyer’s selection.

We used the delta method (Cameron and Trivedi 2009) to calculate the marginal efects at the means for the key independent variables. We estimated that language diference reduces the probability of being selected by 21.60%, one-hour time diference reduces the probability of being selected by 2.51%, while onepoint (1.17 S.D.) increases on the cultural distance scale reduces the probability of being selected by 14.00%. Also, a one-point (2.08 S.D.) increase on the NRI index increases the probability of being selected by 33.74%. Finally, a one-point increase in the service provider’s rating increase the probability of being selected by 4.95%.

4.4.2. Moderating Efects of the Service Provider’s Individual Reputation. We proceed to examine the moderating role of the service provider’s individual reputation on the efects of country diferences and the service providers’ country IT development on the buyer’s selection. The same approach that estimated the main efect is used to estimate the interaction efects. The key estimates are reported in column 1 of Table 5. Again, column 2 provides qualitatively similar results using a fixed efects OLS approach without instrumenting for bid prices. Based on the sign and significance of the estimates, we found partial support for H3A and full support for H3B.

Table 4. Estimation Results for Buyer Selection of Service Providers (Main Efect)

<table><tr><td>Estimation methodDV</td><td>(1) IV-2SLSSelection</td><td>(2) OLS FESelection</td></tr><tr><td>ln(bid)</td><td>-0.5416***(0.0347)</td><td>-0.0722***(0.0019)</td></tr><tr><td>Language Difference</td><td>-0.0196***(0.0036)</td><td>-0.0242***(0.0029)</td></tr><tr><td>Time Zone Difference</td><td>-0.0025***(0.0007)</td><td>-0.0024***(0.0006)</td></tr><tr><td>Cultural Difference</td><td>-0.0156***(0.0028)</td><td>-0.0107***(0.0023)</td></tr><tr><td>NRI</td><td>0.0406***(0.0031)</td><td>0.0206***(0.0022)</td></tr><tr><td>Provider Rating</td><td>0.0038***(0.0005)</td><td>0.0068***(0.0004)</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Skill Match</td><td>0.0740***(0.0154)</td><td>0.0888***(0.0114)</td></tr><tr><td>Prior Transactions</td><td>0.0044***(0.0002)</td><td>0.0047***(0.0003)</td></tr><tr><td>ln(Experience)</td><td>0.0296***(0.0013)</td><td>0.0154***(0.0007)</td></tr><tr><td>Invited Provider</td><td>0.4333***(0.0134)</td><td>0.4602***(0.0225)</td></tr><tr><td>Provider Hourly Rate</td><td>0.0010***(0.0001)</td><td>0.0001***(0.0000)</td></tr><tr><td>Bid Sequence</td><td>0.0013***(0.0001)</td><td>0.0010***(0.0001)</td></tr><tr><td>Constant</td><td>2.5045***(0.1616)</td><td>0.3264***(0.0137)</td></tr><tr><td>Project fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of observations</td><td>117,105</td><td>117,105</td></tr><tr><td>No. of projects</td><td>11,541</td><td>11,541</td></tr><tr><td>Wald Chi $^{2}$ </td><td>12,901.32***</td><td>—</td></tr><tr><td>Within R $^{2}$ </td><td>—</td><td>0.0747</td></tr><tr><td>Cragg–Donald Wald F</td><td>144.20</td><td>—</td></tr><tr><td>Kleibergen–Paap Wald rk F</td><td>151.93</td><td>—</td></tr></table>

Notes. Cluster robust standard errors are reported in parentheses. Stock and Yogo (2005) critical value for relative bias >5% is 13.91. $^ { * } p < 0 . 1 ; ^ { * * } \breve { p } < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

Based on Table 5, first, in the interaction efects model, all direct efects of the buyer–service provider diferences and service providers’ country IT development are consistent in sign with the main efects model reported in Table 4. Second, the observed negative efect of language diference is moderated by the service provider’s reputation $( \beta = 0 . 0 0 1 5 , p < 0 . 0 { \dot { 5 } } )$ , and so is cultural diference $( \beta = 0 . 0 0 1 0 , p < 0 . 0 1 )$ , yet the negative efect of time zone diference is not moderated by the service provider’s reputation. Furthermore, the positive efect of the service provider’s country IT development, measured by the NRI, is attenuated by the service provider’s feedback rating $( \beta = - 0 . 0 0 3 \dot { 2 } ,$ $p < 0 . 0 1 )$ , indicating a substitution efect between the service providers’ country IT development and their reputation.

4.4.3. First-Stage Estimation of Bid Price. For the first-stage estimation, the project-level fixed efects esti-

Table 5. Estimation Results for Buyer Selection of Service Provider (Interaction Efect)

<table><tr><td>Estimation methodDV</td><td>(1) IV-2SLSSelection</td><td>(2) OLS FESelection</td></tr><tr><td>ln(bid)</td><td>-0.5398*** (0.0347)</td><td>-0.0723*** (0.0019)</td></tr><tr><td>Language Difference</td><td>-0.0133*** (0.0044)</td><td>-0.0159*** (0.0031)</td></tr><tr><td>Time Zone Difference</td><td>-0.0024*** (0.0008)</td><td>-0.0022*** (0.0006)</td></tr><tr><td>Cultural Difference</td><td>-0.0192*** (0.0032)</td><td>-0.0129*** (0.0024)</td></tr><tr><td>NRI</td><td>0.0500*** (0.0039)</td><td>0.0242*** (0.0025)</td></tr><tr><td>Provider Rating</td><td>0.0141*** (0.0031)</td><td>0.0102*** (0.0027)</td></tr><tr><td>Provider Rating × Language Difference</td><td>0.0015** (0.0007)</td><td>0.0021*** (0.0005)</td></tr><tr><td>Provider Rating × Time Zone Difference</td><td>-0.0000 (0.0001)</td><td>-0.0001 (0.0001)</td></tr><tr><td>Provider Rating × Cultural Difference</td><td>0.0010** (0.0005)</td><td>0.0006* (0.0004)</td></tr><tr><td>Provider Rating × NRI</td><td>-0.0032*** (0.0007)</td><td>-0.0013** (0.0006)</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Skill Match</td><td>0.0702*** (0.0155)</td><td>0.0871*** (0.0114)</td></tr><tr><td>Prior Transactions</td><td>0.0044*** (0.0002)</td><td>0.0047*** (0.0003)</td></tr><tr><td>ln(Experience)</td><td>0.0290*** (0.0013)</td><td>0.0151*** (0.0007)</td></tr><tr><td>Invited Provider</td><td>0.4337*** (0.0133)</td><td>0.4602*** (0.0226)</td></tr><tr><td>Provider Hourly Rate</td><td>0.0010*** (0.0001)</td><td>0.0001*** (0.0000)</td></tr><tr><td>Bid Sequence</td><td>0.0014*** (0.0001)</td><td>0.0010*** (0.0001)</td></tr><tr><td>Constant</td><td>2.4614*** (0.1606)</td><td>0.3104*** (0.0146)</td></tr><tr><td>Project fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of observations</td><td>117,105</td><td>117,105</td></tr><tr><td>No. of projects</td><td>11,541</td><td>11,541</td></tr><tr><td>Wald Chi2</td><td>12,959.17***</td><td>—</td></tr><tr><td>Within R2</td><td>—</td><td>0.0750</td></tr><tr><td>Cragg-Donald Wald F</td><td>143.49</td><td>—</td></tr><tr><td>Kleibergen-Paap Wald rk F</td><td>151.27</td><td>—</td></tr></table>

Notes. Cluster robust standard errors are reported in parentheses. Stock and Yogo (2005) critical value for relative bias >5% is 13.91. $^ { * } p < 0 . 1 ; ^ { * * } \bar { p } < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

mation was applied with the “xtivreg” procedure. This estimation strategy has two advantages. First, project fixed efects is aligned with our data structure. As noted earlier, if a cross-sectional analysis is used, the variation in project supply could afect the service provider’s bidding; whereas with a project-level fixed efects estimation, we automatically controlled for the number of overlapping projects that are open for bidding because the number of open projects for each bidder of a specific project is roughly the same. Second, a project fixed efects estimation efectively controlled for the common cost component since online outsourcing platforms resemble common value auctions where providers’ cost is interdependent (Hong et al. 2016). Specifically, cluster-correlated robust standard errors (Williams 2000, Wooldridge 2002) were constructed for the fixed efects model. An ex post robust Hausman test for fixed efects (Wooldridge 2002, Schafer and Stillman 2006), following the suggestion of Cameron and Trivedi (2009), rejects the null hypothesis that random efects estimation provides consistent estimates, further indicating the necessity to use the fixed efects model in the first stage. Besides normalized exchange rate, we also included the preceding bid and service providers’ bidding activity in the past seven days as additional instruments. The first-stage estimation shows a significant efect for our key IV of the normalized exchange rate. Furthermore, the Angrist–Pischke multivariate F test of excluded instruments is well above 10, alleviating the weak instrument concern (e.g., Angrist and Pischke 2008, Staiger and Stock 1997), beyond the standard Stock–Yogo test statistic. Last, to evaluate instrument exogeneity, we checked the Sargan statistic from the over-identification test. The Sargan statistic is insignificant <sup>(</sup>p > 0.1<sup>)</sup>, indicating that the null hypothesis that the IVs are exogenous is not rejected. Please note that for the variable bidding activity, we reported the estimation results for 7 days’ bidding activity, yet, replacing this measure with 14 days’ bidding activity or 30 days bidding activity yields similar estimates for all variables.

Based on estimation results from Table 6, we first found the exchange rate to significantly predict bid price. Furthermore, we found service providers bid a lower price when they have a cultural diference from the buyer. This is likely because in equilibrium, the service provider would understand the buyer’s general preferences, and because the buyer shows an aversion for cultural diference, the service provider bids a lower price to enhance his probability of being selected. This result indicates that the service provider is not sensitive to cultural diferences. We do not find a significant efect for either language diference or time zone difference on bid price. We surmise that the reason could be that service providers are also negatively afected by these diferences, which ofsets their incentive to bid a lower price to compensate the negative efect for the buyer. Finally, we found that service providers from countries with a higher IT development bid a higher price. This is likely because, on average, service providers from countries with low levels of IT development have to rely more on price competition, whereas service providers from developed countries with higher levels of IT development may use a higher price as a signal of higher quality. However, when the service providers’ individual reputation is high, they tend to lower their premium for their country’s IT development since the quality signal may be delivered through their own individual reputation.

4.4.4. Robustness Checks. Besides the main efects and interaction efects estimations reported above, we report a number of robustness checks in Online Appendix 2. Specifically, we conducted four additional analyses. First, we used an alternative dependent variable (contract) to assess the robustness of our findings. Second, we estimated the moderating role of buyer experience on buyer–service provider country diferences and the service provider’s country IT development. Third, we used an alternative measure for the service provider’s reputation. Specifically, we replaced service providers’ feedback ratings with their project experience as the main reputation variable, and we repeated the interaction efect analyses. Fourth, we reported an analysis with all projects, including those for which buyers did not select a service provider. Notably, the “xtivreg” procedure in Stata does not drop those observations even though there is no withinproject variation in the dependent variable. The additional analyses indicate that the estimation results we reported are stable and robust.

Table 6. First Stage Estimation Results (DV <sup></sup> ln(Bid))

<table><tr><td>Variables</td><td colspan="2">(1)</td><td colspan="2">(2)</td></tr><tr><td>XRate</td><td>0.4658***</td><td>(0.0903)</td><td>0.4853***</td><td>(0.0905)</td></tr><tr><td>Language Difference</td><td>-0.0036</td><td>(0.0057)</td><td>-0.0060</td><td>(0.0072)</td></tr><tr><td>Time Zone Difference</td><td>-0.0006</td><td>(0.0011)</td><td>-0.0011</td><td>(0.0014)</td></tr><tr><td>Cultural Difference</td><td>-0.0097**</td><td>(0.0043)</td><td>-0.0130**</td><td>(0.0052)</td></tr><tr><td>NRI</td><td>0.0471***</td><td>(0.0043)</td><td>0.0585***</td><td>(0.0058)</td></tr><tr><td>Provider Rating</td><td>-0.0045***</td><td>(0.0007)</td><td>0.0090*</td><td>(0.0048)</td></tr><tr><td>Provider Rating × Language Difference</td><td></td><td></td><td>-0.0007</td><td>(0.0011)</td></tr><tr><td>Provider Rating × Time Zone Difference</td><td></td><td></td><td>0.0001</td><td>(0.0002)</td></tr><tr><td>Provider Rating × Cultural Difference</td><td></td><td></td><td>0.0009</td><td>(0.0008)</td></tr><tr><td>Provider Rating × NRI</td><td></td><td></td><td>-0.0038***</td><td>(0.0011)</td></tr><tr><td>Skill Match</td><td>-0.0330</td><td>(0.0228)</td><td>-0.0372</td><td>(0.0228)</td></tr><tr><td>Prior Transactions</td><td>-0.0004***</td><td>(0.0001)</td><td>-0.0004***</td><td>(0.0001)</td></tr><tr><td>ln(Experience)</td><td>0.0182***</td><td>(0.0014)</td><td>0.0176***</td><td>(0.0014)</td></tr><tr><td>Invited Provider</td><td>-0.0511**</td><td>(0.0204)</td><td>-0.0507**</td><td>(0.0205)</td></tr><tr><td>Provider Hourly Rate</td><td>0.0020***</td><td>(0.0002)</td><td>0.0020***</td><td>(0.0002)</td></tr><tr><td>Bid Sequence</td><td>0.0004**</td><td>(0.0002)</td><td>0.0005**</td><td>(0.0002)</td></tr><tr><td>ln(Preceding Bid)</td><td>-0.0434***</td><td>(0.0037)</td><td>-0.0434***</td><td>(0.0037)</td></tr><tr><td>Past Bidding Activity (7 days)</td><td>0.0011***</td><td>(0.0001)</td><td>0.0011***</td><td>(0.0001)</td></tr><tr><td>Constant</td><td>4.3660***</td><td>(0.0978)</td><td>4.3096***</td><td>(0.1004)</td></tr><tr><td>Project fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>No. of observations</td><td colspan="2">117,105</td><td colspan="2">117,105</td></tr><tr><td>No. of projects</td><td colspan="2">11,541</td><td colspan="2">11,541</td></tr><tr><td>Angrist-Pischke multivariate F test</td><td colspan="2">151.93***</td><td colspan="2">151.27***</td></tr><tr><td>F statistic</td><td colspan="2">128.11***</td><td colspan="2">100.34***</td></tr></table>

Note. Cluster robust standard errors are reported in parentheses. <sup>∗</sup>p < 0.05; <sup>∗∗</sup>p < 0.01; <sup>∗∗∗</sup>p < 0.001.

## 5. Discussion

## 5.1. Key Findings

Our empirical evidence ofers answers to our research questions about the role of country diferences and the service providers’ country IT development in the buyers’ selection of service providers. The key findings are summarized in Figure 1. First, despite attracting buyers and service providers from all around the world, online outsourcing platforms are still subject to challenges because of the proposed three country diferences since buyers are averse to country diferences with service providers, in the form of (a) language, (b) time zone, and (c) cultural diferences. We attribute the negative efect of these three dyadic country diferences to the buyers’ expectations of the service providers’ functional competency in managing the software development process. Second, the country’s level of IT development has a positive efect on a buyer’s selection of service providers, which suggests a positive bias toward service providers from countries with higher levels of IT development. We attribute the role of country IT development to buyers’ evaluation of the service providers’ technical competency in delivering quality software because of the country image cue. Third, in terms of the moderating role of reputation, we found the service provider’s reputation to attenuate the negative efects of language and cultural diferences (albeit not that of time zone diference).

Also, we found the service provider’s reputation to substitute the positive efect of country-level reputation (country IT development), that is, when a service provider signals his individual reputation, his country’s IT development level plays a smaller role in determining his chances of being ofered a contract by a buyer. The results imply that the reputation system could serve as a valuable tool to overcome some (albeit not all) negative efects of country diferences (or global frictions), and that the reputation system also corrects the bias in a buyer’s selection induced by the country’s IT development.

## 5.2. Contributions and Implications for Theory and Practice

This study provides several contributions and implications for theory and practice, as we detail below.

First, our results provide insights on whether online outsourcing platforms are level playing fields (e.g., Friedman 2007, Leamer 2007, Ghemawat 2013). As an emerging market, online outsourcing platforms may have reduced certain transaction and search costs (e.g., Forman et al. 2009, Hann and Terwiesch 2003); however, at the same time they also inevitably created country (language, time zone, cultural) diferences between buyers and service providers that may increase transaction costs. The “flat world” hypothesis is supported by the explicit rules in online outsourcing platforms that do not favor any service provider, irrespective of language, location, culture, or country of origin (Leamer 2007). However, the proposed country diferences do afect how buyers select service providers. Also, contrary to results from prior work (e.g., Gefen and Carmel 2008), we show evidence that buyers are more willing to ofer contracts to those service providers from countries with a higher level of IT development, most likely because of the reputation of those countries for superior IT infrastructure, and access to IT and IT skills by the country’s citizens. Thus, our study indicates that in the knowledge-intensive context of IT services (such as software development), service providers may be endowed with their country’s overall IT reputation.

Figure 1. Summary of Key Findings  
![](/api/attachments/DQYFDMHR/fulltext/images/af3351548551f1386e1defbdf640c48ace95ce84294d4743636214614f1cb15d.jpg)

Second, our study extends the emerging literature on the efect of country diferences in various business settings (e.g., Giannetti and Yafeh 2012, Burtch et al. 2014) to online outsourcing platforms. While the literature has predominantly focused on a certain type of country diference (cultural diference), we studied three country diferences to study how each afects the service providers’ functional competency in managing the software development process (e.g., negotiation, communication, and coordination) and afects buyer selection. As most projects on online outsourcing platforms are software development projects, it is of paramount importance for online outsourcing platforms to facilitate efective buyer–service provider communication and coordination (Agerfalk and Fitzgerald 2008, Allon et al. 2012) to address the complexity of globally distributed software development projects (e.g., Espinosa et al. 2007, Cummings et al. 2009).

Third, our study extends both the literature on reputation in online platforms (e.g., Ba and Pavlou 2002, Kokkodis and Ipeirotis 2015, Moreno and Terwiesch 2014, Lin et al. 2017, Yoganarasimhan 2013) and the larger literature on reputation and trust in online markets (e.g., Dellarocas 2003, Pavlou and Gefen 2004). Although prior work has provided abundant evidence on the direct efect of reputation on outcomes such as price premium, transactions, and sales volume, our study generates new insights on the moderating role of reputation in overcoming the negative efect of the proposed country diferences (language and time zone). Also, attested by the clear substitution efect between the provider reputation and country IT development, we herein conclude that the service provider’s individual reputation corrects for the positive bias due to the IT development level of the service provider’s residing country.

Finally, we seek to ofer practical recommendations for the design of online outsourcing platforms for IT services. First, as our results show, buyers are averse to country diferences, particularly when individual reputation signals are not available. For example, ceteris paribus, buyers from English-speaking countries are less likely to select a Chinese service provider than a U.S. provider. Clearly, it would be unfair if the Chinese provider does have full professional proficiency in English. The online outsourcing platform could thus either encourage service providers to demonstrate their language fluency or create language tests for service providers. For time zone diference, the platform could encourage service providers to publish their willingness to work after hours or around the clock, which could partially mitigate the buyers’ concerns that service providers may be unwilling to accommodate their work schedules. Similarly, it will be useful for the online outsourcing platform to allow service providers to describe their cultural flexibility. Also, given the importance of the reputation of service providers, online outsourcing platforms should protect both service providers and buyers by preventing the manipulation of the reputation system (e.g., Hu et al. 2017). Finally, since service providers’ functional competency and technical competency are two distinct aspects buyers care about, online outsourcing platforms should provide multidimensional reputation systems that reflect both the functional competency and technical competency of service providers to mitigate buyers’ uncertainty.

## 5.3. Limitations and Suggestions for Future Research

This study also has limitations, which open up several interesting opportunities for future research.

First, we solely focused on “open-bid” auctioned projects in this paper. About 10% of the total projects on the platform use “sealed bid” auctions, wherein service providers cannot observe each other’s bid price or nonprice attributes when submitting their bids. Similarly, there is a small portion of projects that are based on time and materials contracts. Future research could study how the choice of auction format or diferent contract forms may have an efect on the buyers’ selection criteria.

Second, two of our measures for country diferences—language and culture—are based on aggregate data from archival data sources because of a lack of individual-level data (e.g., a Chinese provider could speak English at a good working proficiency). Although at first blush, the estimated efect could be biased because of ecological fallacy in terms of the unit of analyses, it would not actually jeopardize our estimates because when providers and buyers make decisions, they form a probabilistic expectation on the diferences without actual interactions with each other (e.g., as English is one oficial language of India, a buyer would expect an Indian provider to be fluent in English; however, a buyer may not expect that from a Chinese provider). Similarly, aggregate measures for cultural diferences have been used for individual-level analysis (Giannetti and Yafeh 2012) or individual-level data aggregated to the country level (Burtch et al. 2014). We have shown that when the service provider’s individual reputation is high, buyers tend to place less emphasis on language and cultural diferences. This result implies that buyers expect some characteristics from a service provider from a certain country (e.g., a U.S. buyer expects some cultural diference with a Chinese service provider) unless the service provider signals a high reputation (e.g., when a Chinese provider can signal a high reputation, cultural diference seems to matter less for a U.S. buyer). Nevertheless, we acknowledge that using such aggregate measures is a data limitation that we are not able to address for this study. It would be interesting for future research to examine individual-level information, such as language fluency or certifications of language exams, should such data become available in online markets.

Finally, it may appear that our results are limited in their generalizability, given that we study a type of emerging and evolving online platform. However, we first argue that the results ofer insights into other markets. There are many other online markets for interpersonal or interfirm transactions that bear great risks related to country diferences, for example, online peerto-peer lending markets (such as Kiva.org) (Burtch et al. 2014), where lenders decide whom to lend money to; online consumer to consumer markets (such as eBay.com), where individual buyers purchase goods from sellers; and online procurement markets (such as

Alibaba.com), where firms source materials or products from other firms. Future research could use similar measures based on our study to test the role of country diferences in such online markets. Second, as online outsourcing platforms evolve, new features such as the “recommended service provider” feature in some platforms recently became available.<sup>7</sup> We believe there are ample opportunities to theorize and empirically examine these new features to understand how platform design could afect user behaviors.

## 6. Concluding Remarks

In this paper, we leveraged a unique individual-level data set by integrating proprietary data from a corporate database with a number of public data sets to empirically test our hypotheses on the efects of country diferences, country IT development, and their respective interaction efects with reputation on the buyer’s selection of service providers in the unique context of an online outsourcing platform. We showed the buyers’ aversion for service providers from countries with language, time zone, and cultural diferences, and a strong preference for service providers from countries with high levels of IT development. Furthermore, we also showed that reputation could potentially overcome the negative efect of language and cultural (albeit not time zone) diferences, and individual reputation could correct for the possible positive bias toward service providers from countries with high levels of IT development, and thus help to level the playing field for all service providers around the globe. Finally, our study seeks to entice academics and practitioners to look at the broader global dynamics of online outsourcing platforms for IT services toward developing platforms that service providers can efectively compete on a level playing field.

## Acknowledgments

The authors thank the senior editor and associate editor for a constructive and developmental review process. The authors also thank the anonymous reviewers for their helpful comments and suggestions. Finally, the authors thank Matt Barrie, Pei-yu Chen, Lorin Hitt, Ni Huang, Sanat Sarkar, Sunil Wattal, and seminar participants at the University of Virginia, Nanyang Technological University, Arizona State University, University of Florida, the 2012 International Conference on Information Systems, and the 2013 Statistical Challenges in eCommerce Research for valuable feedback. The authors acknowledge financial support from CIBER (Center for International Business Education and Research) through the U.S. Department of Education and the Fox School’s Young Scholar’s Forum at Temple University.

## Endnotes

<sup>1</sup> The papers we surveyed have used various terms for buyers (e.g., firm, client, project poster) and service providers (e.g., supplier, seller, bidder, freelancer), we herein use “buyer” and “service provider.”

<sup>2</sup> See Manyika et al. (2015).

<sup>3</sup> See Tan (2013).

<sup>4</sup> As part of the collaboration, we conducted a user survey study with the platform in May 2010 on buyer’s uncertainty about the service providers, and we found technical competency and functional competency to be two distinct dimensions in a principal component analysis.

<sup>5</sup>http://www.iana.org/time-zones.

<sup>6</sup>https://www.imf.org/external/np/fin/ert/GUI/Pages/CountryData -Base.aspx.

<sup>7</sup> We thank an anonymous reviewer for suggesting this point. At the time of our data collection, the platform with which we work had not implemented this feature.

## References

Agerfalk PJ, Fitzgerald B (2008) Outsourcing to an unknown workforce: Exploring opensourcing as a global sourcing strategy. MIS Quart. 32(2):385–409.

Agerfalk PJ, Fitzgerald B, Slaughter SA (2009) Flexible and distributed information systems development: State of the art and research challenges. Inform. Systems Res. 20(3):317–328.

Akerlof G (1970) The market for “Lemons”: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3):488–500.

Alavi M, Leidner DE (2001) Review: Knowledge management and knowledge management systems: Conceptual foundations and research issues. MIS Quart. 25(1):107–136.

Allon G, Bassamboo A, Cil EB (2012) Large-scale service markets: The role of the moderating firm. Management Sci. 58(10): 1854–1872.

Ang S, Straub D (1998) Production and transaction economies and IS outsourcing: A study of the U.S. banking industry. MIS Quart. 22(4):535–552.

Angrist JD, Pischke JS (2008) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University Press, Princeton, NJ).

Angrist JD, Imbens GW, Rubin DB (1996) Identification of causal efects using instrumental variables. J. Amer. Statist. Assoc. 91(434): 444–455.

Asker J, Cantillon E (2010) Procurement when price and quality matter. RAND J. Econom. 41(1):1–34.

Ba S, Pavlou PA (2002) Evidence of the efect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quart. 26(3):243–268.

Bakos JY, Brynjolfsson E (1993) From vendors to partners: Information technology and incomplete contracts in buyer–supplier relationships. J. Organ. Comput. Electronic Commerce 3(3):301–328.

Banker R, Hwang I (2008) Importance of measures of past performance: Empirical evidence on quality of e-service providers. Contemporary Accounting Res. 25(2):307–337.

Banker RD, Slaughter SA (2000) The moderating efects of structure on volatility and complexity in software enhancement. Inform. Systems Res. 11(3):219–240.

Banker RD, Davis GB, Slaughter SA (1998) Software development practices, software complexity, and software maintenance performance: A field study. Management Sci. 44(4):433–450.

Berry S, Levinsohn J, Pakes A (1995) Automobile prices in market equilibrium. Econometrica 63(4):841–890.

Bird S, Klein E, Loper E (2009) Natural Language Processing with Python (O’Reilly Media, Sebastopol, CA).

Bitner M, Booms B, Mohr L (1994) Critical service encounters: The employee’s view. J. Marketing 58(4):95–106.

Brynjolfsson E, McAfee A (2011) Race Against the Machine: How the Digital Revolution Is Accelerating Innovation Driving Productivity and Irreversibly Transforming Employment and the Economy (Digital Frontier Press, Lexington, MA).

Brynjolfsson E, Smith M (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Burtch G, Ghose A, Wattal S (2014) Cultural diferences and geography as determinants of online pro-social lending. MIS Quart. 38(3):773–794.

Cameron AC, Trivedi PK (2009) Microeconometrics Using Stata (Stata Press, College Station, TX).

Chandler AD (1977) The Visible Hand: The Managerial Revolution in American Business (Belknap Press, Cambridge, MA).

Chase RB, Apte UM (2007) A history of research in service operations: What’s the big idea? J. Oper. Management 25(2):375–386.

Chen YC, Rogof K, Rossi B (2010) Can exchange rates forecast commodity prices? Quart. J. Econom. 125(3):1145–1194.

Clark C (1967) The Conditions of Economic Progress (Garland Publishing, New York).

Cummings JN, Espinosa JA, Pickering CK (2009) Crossing spatial and temporal boundaries in globally distributed projects: A relational model of coordination delay. Inform. Systems Res. 20(3):420–439.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407–1424.

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

Dibbern J, Winkler J, Heinzl A (2008) Explaining variations in buyer extra costs between software projects ofshored to India. MIS Quart. 32(2):333–366.

Dimoka A, Hong Y, Pavlou P (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 32(2):395–426.

Dutta S, Geiger T, Lanvin B (2015) The global information technology report. World Econom. Forum. http://www3.weforum.org/docs/ WEF\_Global\_IT\_Report\_2015.pdf.

Espinosa JA, Slaughter SA, Kraut RE, Herbsleb JD (2007) Familiarity complexity and team performance in geographically distributed software development. Organ. Sci. 18(4):613–630.

Forman C, Ghose A, Goldfarb A (2009) Competition between local and electronic markets: How the benefit of buying online depends on where you live. Management Sci. 55(1):47–57.

Friedman TL (2007) The World Is Flat: A Brief History of the Twenty-First Century (Picador, New York).

Gefen D, Carmel E (2008) Is the world really flat? A look at ofshoring at an online programming market. MIS Quart. 32(2):367–384.

Ghemawat P (2013) Redefining Global Strategy: Crossing Borders in a World Where Diferences Still Matter (Harvard Business Press, Boston).

Ghose A, Ipeirotis PG, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Sci. 31(3):493–520.

Giannetti M, Yafeh Y (2012) Do cultural diferences between contracting parties matter? Evidence from syndicated bank loans. Management Sci. 58(2):365–383.

Gilbert DT (1991) How mental systems believe. Amer. Psychologist 46(2):107–119.

Grönroos C (1984) A service quality model and its marketing implications. Eur. J. Marketing 18(4):36–44.

Han CM (1989) Country image: Halo or summary construct. J. Marketing Res. 26(2):222–229.

Hann IH, Terwiesch C (2003) Measuring the frictional costs of online transactions: The case of a name-your-own-price channel. Management Sci. 49(11):1563–1579.

Hartline M, Ferrell O (1996) The management of customer contact service employees: An empirical investigation. J. Marketing 60(4):52–70.

Herbsleb JD, Grinter RE (1999) Splitting the organization and integrating the code: Conway’s law revisited. Proc. 21st Internat. Conf. Software Engrg. (ACM, New York), 85–95.

Hong Y, Pavlou PA (2014) Product fit uncertainty in online markets: Nature efects and antecedents. Inform. Systems Res. 25(2): 328–344.

Hong Y, Wang C, Pavlou PA (2016) Comparing open and sealed bid auctions: Evidence from online labor markets. Inform. Systems Res. 27(1):49–69.

Horton JJ (2015) Supply constraints as a market friction: Evidence from an online labor market. Working paper, Stern School of Business, New York University.

Hu N, Pavlou PA, Zhang J (2017) On selection biases in online product reviews. MIS Quart. Forthcoming.

Inglehart R, Welzel C (2010) Changing mass priorities: The link between modernization and democracy. Perspectives Politics 8(2):551–567.

James LR (1982) Aggregation bias in estimates of perceptual agreement. J. Appl. Psych. 67(2):219–229.

Katz R (1982) The efects of group longevity on project communication and performance. Admin. Sci. Quart. 27(1):81–104.

King WR, Torkzadeh G (2008) Information systems ofshoring: Research status and issues. MIS Quart. 32(2):205–225.

Kokkodis M, Ipeirotis PG (2015) Reputation transferability in online labor markets. Management Sci. 62(6):1687–1706.

Kristensson P, Matthing J, Johansson N (2008) Key strategies for the successful involvement of customers in the co-creation of new technology-based services. Internat. J. Service Indust. Management 19(4):474–491.

Larman C, Basili VR (2003) Iterative and incremental development: A brief history. IEEE Comput. 36(6):47–56.

Leamer EE (2007) A flat world, a level playing field, a small world after all, or none of the above? A review of Thomas L. Friedman’s The World is Flat. J. Econom. Literature 41(1):83–126.

Lefkof-Hagius R, Mason CH (1993) Characteristic beneficial and image attributes in consumer judgments of similarity and preference. J. Consumer Res. 20(1):100–110.

Leskovec J, Rajaraman A, Ullman JD (2014) Mining of Massive Data Sets (Cambridge University Press, Cambridge, UK).

Li WK, Wyer RS (1994) The role of country of origin in product evaluations: Informational and standard-of-comparison efects. J. Consumer Psych. 3(2):187–212.

Lin M, Goes P (2012) Does information really “Unravel”? Understanding factors that motivate sellers to seek third-party certifications in an online labor market. Working paper, University of Arizona, Tucson.

Lin M, Liu Y, Viswanathan S (2017) Efectiveness of reputation in contracting for customized production: Evidence from online labor markets. Management Sci. Forthcoming.

Littlepage G, Robison W, Reddington K (1997) Efects of task experience and group experience on group performance member ability and recognition of expertise. Organ. Behav. Human Decision Processes 69(2):133–147.

Malone TW, Crowston K (1994) The interdisciplinary study of coordination. ACM Comput. Surveys 26(1):87–119.

Malone TW, Laubacher RJ (1998) The dawn of the e-lance economy. Harvard Bus. Rev. 76(5):146–152.

Manyika J, Lund S, Robinson K, Valentino J, Dobbs R (2015) Connecting talent with opportunity in the digital age. McKinsey Global Institute Report, http://www.mckinsey.com/global-themes/ employment-and-growth/connecting-talent-with-opportunityin-the-digital-age.

Martin RC (2003) Agile Software Development: Principles Patterns and Practices (Prentice Hall, Upper Saddle River, NJ).

Mayer T, Zignago S (2005) Market access in global and regional trade. CEPII Report, http://www.cepii.fr/PDF\_PUB/wp/2005/ wp2005-02.pdf.

Mill R (2011) Hiring and learning in online global labor markets. Working paper, Stanford University, Palo Alto, CA.

Mithas S, Jones JL (2007) Do auction parameters afect buyer surplus in e-auctions for procurement? Production Oper. Management 16(4):455–470.

Mithas S, Krishnan M (2008) Human capital and institutional efects in the compensation of information technology professionals in the United States. Management Sci. 54(3):415–428.

Moreno A, Terwiesch C (2014) Doing business with strangers: Reputation in online service marketplaces. Inform. Systems Res. 25(4):856–886.

Morris MW, Fu H (2001) How does culture influence conflict resolution: A dynamic constructivist analysis. Soc. Cognition 19(3): 324–349.

Nakatsu RT, Iacovou CL (2009) A comparative study of important risk factors involved in ofshore and domestic outsourcing of software development projects: A two-panel Delphi study. Inform. Management 46(1):57–68.

Nevo A (2000) A practitioner’s guide to estimation of randomcoeficients logit models of demand. J. Econom. Management Strategy 9(4):513–548.

Pavlou PA, Gefen D (2004) Building efective online marketplaces with institution-based trust. Inform. Systems Res. 15(1):27–53.

Pavlou PA, Liang H, Xue Y (2007) Understanding and mitigating uncertainty in online environments: A principal-agent perspective. MIS Quart. 31(1):105–136.

Rai A, Maruping LM, Venkatesh V (2009) Ofshore information systems projects success: The role of social embeddedness and cultural characteristics. MIS Quart. 33(3):617–641.

Rao A, Monroe K (1989) The efect of price brand name and store name on buyers’ perceptions of product quality: An integrative review. J. Marketing Res. 26(3):351–357.

Ravindran K, Susarla A, Mani D, Gurbaxani V (2015) Social capital reputation and contract design in buyer–supplier networks for information technology outsourcing. Inform. Systems Res. 26(2):379–397.

Rogers EM, Bhowmik DK (1970) Homophily–heterophily: Relational concepts for communication research. Public Opinion Quart. 34(4):523–538.

Rust RT, Inman JJ, Jia J, Zahorik A (1999) What you don’t know about customer-perceived quality: The role of customer expectation distributions. Marketing Sci. 18(1):77–92.

Schafer ME, Stillman S (2006) XTOVERID: Stata module to calculate tests of overidentifying restrictions after xtreg, xtivreg, xtivreg2, xthtaylor. Statistical Software Components S456779, Boston College Department of Economics, Chestnut Hill, MA, revised January 5, 2016.

Scholz M, Haas N (2011) Determinants of reverse auction results: An empirical examination of freelancer.com. Proc. Eur. Conf. Inform. Systems, Article 89.

Smith A (1776) The Wealth of Nations. Cannan E, ed. University Paperbacks 14–15 (Methuen, London).

Snir E, Hitt L (2003) Costly bidding in online markets for IT services. Management Sci. 49(11):1504–1520.

Spence M (1973) Job market signaling. Quart. J. Econom. 87(3): 355–374.

Staiger D, Stock JH (1997) Instrumental variables regression with weak instruments. Econometrica 65(3):557–586.

Stock JH, Yogo M (2005) Testing for weak instruments in IV regression. Andrews DWK, Stock JH, eds. Identification and Inference for Econometric Models: A Festschrift in Honor of Thomas Rothenberg (Cambridge University Press, Cambridge, UK), 80–108.

Stoll S, Zöttl G (2012) Information disclosure in dynamic buyerdetermined procurement auctions: An empirical study. Working paper, Department of Economics, University of Munich, Munich, Germany.

Su N (2015) Cultural sensemaking in ofshore information technology service suppliers: A cultural frame perspective. MIS Quart. 39(4):959–983.

Surprenant C, Solomon M (1987) Predictability and personalization in the service encounter. J. Marketing 51(2):86–96.

Susarla A (2012) Contractual flexibility rent seeking and renegotiation design: An empirical analysis of information technology outsourcing contracts. Management Sci. 58(7):1388–1407.

Susarla A, Barua A (2011) Contracting eficiency and new firm survival in markets enabled by information technology. Inform. Systems Res. 22(2):306–324.

Susarla A, Subramanyam P, Karhade P (2010) Contractual provisions to mitigate holdup: Evidence from information technology outsourcing. Inform. Systems Res. 21(1):37–55.

Tan G (2013) Australia’s freelancer soars on IPO debut. Wall Street Journal (November 14), http://blogs.wsj.com/moneybeat/ 2013/11/14/australias-freelancer-soars-on-ipo-debut/.

Tan PN, Steinbach M, Kumar V (2005) Introduction to Data Mining (Addison-Wesley, Boston).

Vargo SL, Lusch RF (2004) Evolving to a new dominant logic for marketing. J. Marketing 68(1):1–17.

Williams RL (2000) A note on robust variance estimation for clustercorrelated data. Biometrics 56(2):645–646.

Wooldridge JM (2002) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA).

Yoganarasimhan H (2013) The value of reputation in an online freelance market. Marketing Sci. 32(6):860–891.
