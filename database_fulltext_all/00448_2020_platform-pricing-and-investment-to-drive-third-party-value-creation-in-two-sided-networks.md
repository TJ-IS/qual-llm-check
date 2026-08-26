---
otero_id: 448
otero_key: "G5ZKZPRS"
title: "Platform Pricing and Investment to Drive Third-Party Value Creation in Two-Sided Networks"
authors: "Burcu Tan; Edward G. Anderson; Geoffrey G. Parker"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0882"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [46.161.62.181] On: 21 February 2020, At: 02:46 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/G5ZKZPRS/fulltext/images/7b9fb749032e7115d9c7e49db3e1b3be7f95f95558fcbb43ab3fb537e073b1d0.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Platform Pricing and Investment to Drive Third-Party Value Creation in Two-Sided Networks

Burcu Tan, Edward G. Anderson,Jr., Geoffrey G. Parker

To cite this article:

Burcu Tan, Edward G. Anderson,Jr., Geoffrey G. Parker (2020) Platform Pricing and Investment to Drive Third-Party Value Creation in Two-Sided Networks. Information Systems Research

Published online in Articles in Advance 19 Feb 2020

https://doi.org/10.1287/isre.2019.0882

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, The Author(s)

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Platform Pricing and Investment to Drive Third-Party Value Creation in Two-Sided Networks

Burcu Tan,<sup>a</sup> Edward G. Anderson, Jr.,<sup>b</sup> Geoffrey G. Parker<sup>c</sup>

<sup>a</sup> Anderson School of Management, The University of New Mexico, Albuquerque, New Mexico 87106; <sup>b</sup> McCombs School of Business, University of Texas, Austin, Texas 78705; <sup>c</sup> Thayer School of Engineering, Dartmouth College, Hanover, New Hampshire 03755 Contact: btan@unm.edu, https://orcid.org/0000-0002-9869-1908 (BT); edward.anderson@mccombs.utexas.edu, https://orcid.org/0000-0002-7747-1607 (EGA); geoffrey.g.parker@dartmouth.edu, http://orcid.org/0000-0002-7160-6451 (GGP)

Received: October 10, 2016 Revised: February 1, 2018; December 4, 2018; April 28, 2019 Accepted: May 23, 2019 Published Online in Articles in Advance: February 19, 2020

https://doi.org/10.1287/isre.2019.0882

Copyright: © 2020 The Author(s)

Abstract. Many two-sided platforms (for example, eBay, Google, iOS, Android, Twitter, and Amazon) provide integration tools, such as modular interfaces, interactive devel opment environments, application programming interfaces, and help desks, to reduce the costs and improve the functionality of third-party content developed for the platform. The need for such investment is increasing with the rise of major new markets as the resul of technologies, such as the “Internet of Things.” Although crucial to platform success, platform integration tools are costly to create. We develop an analytic model to explore the key tradeoffs behind investment in integration tools and how that investment interacts with pricing decisions in a two-sided market. We model these decisions for hardware/ software platforms as well as hybrid retail platforms and analyze them under various scenarios, including monopoly and competition. Our results suggest that considering integration investment can create market regimes in which the standard pricing results from the extant platform literature no longer hold. For example, the tendency to reduce prices to one side of a market in response to increasing the benefit of the network to the other side may be suboptimal in the presence of integration investment. Therefore, integration investments must be well coordinated with pricing decisions made for both sides of the market. In general, higher levels of investment by hardware/software platforms into integration become desirable when the platform (1) has access to a large pool of conten providers and consumers, (2) is able to develop integration tools that are highly effective in reducing third-party development costs, and (3) operates in a market in which content providers earn a high-enough profit margin creating content that is highly valued by the consumer market. Hybrid retail platforms often show similar behavior. However, there are some nuances. For example, business to business platforms can make investments in integration to facilitate participation by both sides of the market. We find that these in vestments are complements, not—as one might expect—substitutes. We conclude b discussing this work’s implications for theory and practice.

![](/api/attachments/G5ZKZPRS/fulltext/images/162bac6f5e03832c2adb5e85cfe9a158b8ab049325fce2b977019da6b594d52d.jpg)

History: Robert Fichman, Senior Editor; Marius Niculescu, Associate Editor

Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as “Information Systems Research. Copyright © 2020 The Author(s). https://doi.org/10.1287/ isre.2019.0882, used under a Creative Commons Attribution License: https://creativecommons.org licenses/bv/4.0/."

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0882.

Keywords: two-sided markets • network externality • application programming interface • developers • integration • ecosystem

## 1. Introduction

In the last two decades, many industries have been transformed with the proliferation of two-sided platforms that bring together consumers and content providers. Platforms are everywhere in the information exchange and retail space, from shopping sites (e.g., Amazon.com and eBay) and social media (e.g., Facebook and Twitter) to video games (e.g., Xbox and Wii) and operating systems (e.g., iOS and Android). Now, they are beginning to embed themselves even more deeply into our lives as home automation platforms begin to encompass sensors and actuators throughout the household to automate and control functions, like thermostats, lighting, security, and home entertainment. Eventually, this “Internet of Things” (IoT) is forecast to extend even to urban functions, such as traffic control and garbage collection (Barrie 2015, Shueh 2016), making the importance of platforms to society ever more pronounced (Evans and Annunziata 2012).

In areas where platforms have gained traction, the ability of a platform to encourage the development of a variety of content (such as games, productivity applications, and videos) and integrate that content into a seamless user experience has become crucial in determining a platform’s success. Thus, it is in the best interest of platform providers to make their platforms attractive and effective development environments for third-party content providers. The problematic experience of mobile application development for electronic healthcare record platforms, such as EPIC, shows, however, that such a seamless environment for integrating the content and functionality of third-party content providers is not automatic (Lim and Anderson 2016). For example, one digital healthcare entrepreneur described how his engineers “tried valiantly to integrate (hack) antiquated databases in order to get our patient engagement software to speak securely to legacy systems” (Kim 2015). Another startup chief executive officer said, “Lack of [tools for easy integration] for electronic healthcare records programs is killing mobile-health applications” (Anderson 2015). This difficulty suggests that, like any other technical product, platforms must invest resources and time in developing an environment that promotes the easy integration of third-party content; otherwise, their attractiveness to third-party content providers, and ultimately, customers will be stunted (Anderson and Parker 2013b).

In the information exchange space, there are a number of tools to promote such product integration (Anderson et al. 2018), the most obvious example being integrated development environments; selfcontained tasks with well-specified interfaces; standards; organizational structures (such as help desks); software development kits (SDKs), which create specialized development environments; and application programming interfaces (APIs), which improve platform modularity. Among these tools, APIs have gained significant traction in recent years (Figure 1). An API is a set of programming instructions for building software applications for a platform and gaining access to important data streams. Platforms ranging from Amazon and eBay to YouTube, Twitter, and Netflix have invested in providing powerful and user-friendly APIs (Kane 2010). Platform providers offer publicly available APIs to reduce third-party content providers’ cost of content development, which makes the platform more attractive to the content provider community (Benzell et al. 2019). A good API makes the platform more modular by providing well-defined interfaces for the application to the platform, hence reducing development costs for the third-party con tent provider. Furthermore, additional investment in “bullet proofing” APIs can make the platform more reliable and provide users with a more seamless experience. Other integration tools, such as SDKs, also reduce costs to develop superior, well-integrated content by providing essential building blocks and development environments, which further improve the attractiveness of the platform for the content provider community. When the content providers are on board, consumers are more likely to follow.

Figure 1. (Color online) Growth of the API Economy  
![](/api/attachments/G5ZKZPRS/fulltext/images/458f30793212d8973d44542bdaa96c88f09c57681f27339a21105c670d87534b.jpg)  
Source. Data are taken from ProgrammableWeb.com.

Platform investment in integration tools (as shown in the depiction of the growth of public APIs over time in Figure 1) has been increasing rapidly over time. The need for integration investment will likely only accelerate with the arrival of IoT platforms. By 2020, as many as 30 billion “things” are expected to connect to each other over the IoT (MacGillvray 2016). For an IoT platform to generate the benefits anticipated by industry experts (Reisinger 2015), physical device developers will need a low-cost way to exchange data across the platform as well as give the platform the means to control these devices. For example, a lightswitch manufacturer with products that generally cost less than \$2 will need a Wi-Fi transmitter and software to hook up to a home IoT platform. It is also argued that a mature IoT will require common standards within and across literally hundreds to thousands of device types for communication and connectivity and that translators will be needed to bridge the gap between legacy devices and the ones designed with IoT in mind (MacGillivray 2016). This will be expensive for platform firms. However, the reason that they need to do this is that low-margin developers, like the light-switch manufacturer discussed above, cannot afford to invest in mating up to multiple Wi-Fi and software protocol standards. This is where investing in carefully crafted integration tools will be critical. With such tight developer margins, anything the platform can do to reduce developer costs is of the utmost importance, because an IoT platform can only be as powerful as the number of third-party sensors and actuators that integrate with it.

It is well known in the product development literature that the development of product integration tools and organizational structures, such as modularity, standards, and help desks, is expensive but of decisive importance for market success (Baldwin and Clark 2000). A notable example is Jeff Bezos’s famous mandate at Amazon: “All teams will henceforth expose their data and functionality through service interfaces. All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions” (Rosoff 2011). Thus, the fact that platforms clearly make large investments in integration tools, such as APIs, SDKs, standards, specifications, and help desks, to facilitate third-party content development is clearly documented. Yet, with a few exceptions (e.g., the empirical study by Li and Agarwal (2016)), research in the twosided platforms literature that examines the level of investment in integration tools is remarkably sparse. Even more so is guidance on how to optimally coordinate that investment with pricing decisions. Our paper leverages the literature on product integration (Iansiti 1998, Anderson and Parker 2013b) to begin to fill this gap. By doing so, we hope to provide a guide to platforms on how to better coordinate such decisions with other strategic decisions, particularly as platforms move out of the information exchange and retail industries into newer, less forgiving fields, such as healthcare and ultimately, IoT.

To investigate this crucial integration investment decision at a deeper level, we build a strategic model to analyze the optimal integration tool investment by two-sided platforms. In order to delineate potential differences in integration strategy between platforms with significantly different business models, we devote separate sections to two platform types: hardware/ software platforms (e.g., Android and PlayStation) and hybrid retail platforms (e.g., Amazon, eBay, and Wal mart). Hardware/software platforms rely on thirdparty content providers to extend the functionality of their systems and provide content services for consumers. Hybrid retail platforms rely on third-party merchants to supply “long-tail” products that platforms would otherwise find prohibitively expensive to carry. A firm like Amazon finds itself acting as both a merchant reseller, taking inventory risk and profiting from the spread between wholesale and retail prices, and a platform that profits from fees levied on completed transactions. Figure 2 illustrates the participants in the ecosystem and the financial transactions between the participants for these two platform types.

We first examine decisions made by a monopolist hardware/software platform by focusing on the interplay between integration tool investment and pricing decisions. A number of interesting insights emerge from this analysis. One important observation is that, when integration investment is considered some standard results from the two-sided market literature do not always hold. For example, a standard result from the two-sided market literature is that, if the benefit of the platform’s network exter nalities to one side of the two-sided market increases, then the price charged to the opposite side should decrease (Parker and Van Alstyne 2000b, 2005; Rochet and Tirole 2003). However, our results suggest that it may be optimal to increase the content provider participation fee when consumer utility from content goes up. The reason is that investing in integration tools and reducing the participation fee are partially substitutable actions in terms of attracting content providers. When integration investment is very effective in reducing content providers’ fixed costs, the platform provider can increase both the participation fee and consumer price in response to increasing consumer utility from content and still have higher participation across content providers and consumers. Our results also show that the optimal consumer price may decrease when consumer utility from content goes up, even though the existing literature would suggest otherwise (Parker and Van Alstyne 2000b, 2005; Armstrong 2006). This is more likely to happen when content price is high and consumer gross utility from content is low. In such a setting, the cross-side network effect is stronger for content providers. Thus, it may be more profitable to increase both the content provider participation fee and integration investment in response to increasing consumer utility from content rather than increase the consumer price. These observations highlight the importance of considering the effect of integration investment when making twosided pricing decisions.

Figure 2. (Color online) Transactions Between the Participants in the Platform Ecosystem  
![](/api/attachments/G5ZKZPRS/fulltext/images/5f5bd152a2a506e94b2bcee35a7ff85669d2952c87534a2880328658c0976b31.jpg)  
Notes. (a) Hardware/software platforms. (b) Retail platforms.  
\*In practice, the merchandise/service payment flows from buyer to platfrom to seller.

The relation between integration investment and the content provider participation fee deserves particular attention. Even though increasing integration investment and reducing participation fees may be partially substitutable, there is an important distinction between the two levers: integration investment is a nonrival strategy in the sense that it is a fixed cost that does not increase no matter how many content providers join. In contrast, reducing participation fees is akin to a variable cost, because the total impact increases with the number of content providers joining the platform. Thus, the decision to increase integration investment versus the decision to reduce content provider participation fees is not entirely comparable. This paper aims to provide guidance around how to trade these decisions off, because not only is the level of integration investment a crucial decision, but it is also a decision that must be carefully coordinated with pricing decisions in order to obtain its maximum benefit for both consumers and content providers.

Next, we analyze how competitive pressures shape the integration investment and the pricing decisions for hardware/software platforms. We first confirm that the interplay between integration investment and participation fee described above still holds under competition. However, for symmetric platforms, consumer prices under competition respond to the changes in market parameters differently from those under a monopolist. Generally, competitive pressure to attract the consumer side tends to create scenarios in which potential gains to platforms from increasing the “size of the pie” are competed away by reducing the consumer price. We also demonstrate that investing in better capabilities for facilitating third-party development may be a significant success factor for a platform under competition. Specifically, if consumers value content highly and if integration tools are very effective in reducing content development costs, a platform that is able to create a more favorable integration environment can capture a larger market share than a platform with a higher standalone value but lower integration capability. Indeed, as we discuss in Section 3.2.2, better integration capabilities played an important role in Facebook’s victory over Myspace, because the latter had an arcane architecture “hated by the developer community” (Gillette 2011). Research in Motion, sponsor of the Blackberry platform, also lost a dominant position because of failing to mobilize a sufficiently competitive ecosystem (Jacobides 2013). Based on our prior discussion of IoT’s dependency on integrating numerous actuators and sensors, we would expect similar effects to play out in the IoT space, perhaps with even greater magnitude.

Additionally, we move our focus to hybrid retail platforms. The main difference between the business model of hardware/software platforms and hybrid retail platforms is that the latter only charges the seller side. We find that, although the integration investment strategy for hybrid retail platforms is similar to that for hardware/software platforms, the interplay between integration investment and seller participation fee shows some differences, particularly for monopolist hybrid retail platforms. For example, unlike hardware/software platforms, any change in market parameters that potentially increases buyer or seller surplus always results in a higher seller participation fee in the case of a monopolist hybrid retail platform. This is mainly because hybrid retail platforms only charge the seller side. In the absence of consumer price as a strategic lever, it is no longer possible to reduce the participation fee and recoup the loss through an increase in consumer price. Thus, a hybrid retail platform’s participation fee choice mimics one-sided pricing decisions in a standard supply chain. To better understand the role of integration investment in the monopolistic hybrid retail platform setting, we compare seller participation fee with or without the ability to invest in integration. Not surprisingly, integration investment enables the platform provider to set a higher price for sellers. More importantly, we find that, in the absence of integration investment, the optimal seller fee does not depend on buyers’ crossside network benefits, which means that the platform provider does not increase the seller participation fee when buyers’ utility from content increases. In contrast, in the presence of integration investment, the platform is able to increase the seller participation fee and still obtain a higher market share on both sides of the market. Thus, integration investment restores an important strategic lever to hybrid retail platforms.

We also analyze the strategic behavior of business to business (B2B) platforms that can use a two-sided integration investment strategy. For example, they can invest in integration tools to increase not only seller but also, buyer participation. We find that integration investment directed toward one side of the market (seller or buyer) increases with the margina benefit of integration investment directed toward the opposite side. This shows that there are spillover benefits of integration investment from one side of the market to the other side, implying that integration investments on different sides of the market act as complements rather than substitutes. Thus, integration investment helps the platform to better capture the increased buyer surplus from cross-side network effects. This spillover effect also shows that the necessity to coordinate integration and pricing strategy becomes even more urgent and complex in B2B platforms.

The remainder of the paper proceeds as follows. Section 2 reviews the related literature. In Section 3, we study integration investment for hardware/software platforms in both monopolistic and competitive settings, whereas in Section 4, we consider hybrid retail platforms. Finally, policy implications of the results are discussed in Section 5 along with the limitations of this analysis and possible extensions. We conclude the paper in Section 6. For ease of narration, proofs are suppressed to the online appendix.

## 2. Literature Review

This paper contributes to the two-sided markets and platform literature by analyzing the strategic choice of platform investment in integration tools and resources (e.g., APIs, SDKs, technical specification, help desks, etc.) to facilitate third-party content development. The two-sided markets literature (Parker and Van Alstyne 2000b, 2005; Rochet and Tirole 2003) explores novel strategies for two-sided platforms that leverage network externalities, primarily cross-side network effects that result in strategies that favor and many times, even subsidize one side of the market in order to attract the other side (Eisenmann et al. 2006)

The growing body of work on two-sided markets has primarily focused on two-sided pricing strategies (Parker and Van Alstyne 2000a, 2005; Caillaud and Jullien 2003; Rochet and Tirole 2003, 2006; Armstrong 2006; Hagiu 2006; Weyl 2010). The key insight from this body of research is that platforms should charge lower prices to the side that derives less utility from the presence of the other side. Either side of the market may be subsidized depending on the relative strengths of the cross-side network effects (Parker and Van Alstyne 2000a, 2005; Armstrong 2006; Rochet and Tirole 2006). For example, search engines, such as Google, subsidize searchers while charging the advertisers, whereas operating systems, such as Windows, may subsidize application developers while charging consumers (Eisenmann et al. 2006).

There is also a burgeoning stream of research in the two-sided markets literature that focuses on the use of nonprice strategic levers by platforms (Gawer and Cusumano 2002, Boudreau and Hagiu 2011, Eisenmann et al. 2011, Parker et al. 2017, Parker and Van Alstyne 2018). For example, Bhargava and Choudhary (2004) analyze the product line design problem of an information intermediary. Zhu and Iansiti (2011) consider competition between an incumbent and an entrant on the basis of platform quality and installed base and show that installed base does not necessarily present barriers to entry A number of recent papers study platform investments in contexts other than integration investment For example, Hagiu and Spulber (2013) analyze platform providers’ investment into first-party content as a means to overcome unfavorable expectations and thereby, attract buyers to the platform. Platform papers on net neutrality examine internet service provider (ISP) incentives for network capacity investment under different pricing schemes (Musacchio et al. 2009, Pil Choi and Kim 2010, Cheng et al. 2011, Gupta et al. 2011, Economides and Hermalin 2012, Kramer and Wiewiorra¨ 2012, Bourreau et al. 2015). Although this stream of net neutrality research also studies the interplay between investment and pricing decisions, its focus is on understanding the welfare implications of neutral versus discriminatory pricing regimes between ISPs and content providers. In contrast, our paper focuses on the impact of platform integration strategy on two-sided pricing decisions. In a study that is closer to this paper, Bakos and Katsamakas (2008) analyze a platform’s investment into increasing the strength of network effects. Although our paper is also looking at strategic investments to increase user participation, we treat the per user level of network effects as exogenous in our model and instead, analyze a platform’s investment into integration tools that facilitate third-party development, thereby increasing participation on both sides of the market. In this way, platforms can affect the aggregate impact of the network effect.

Our paper is most closely related to that of Anderson et al. (2014), which explore how the choice of platform performance (“quality”) level during a product development cycle affects the amount of third-party content created for that platform. The primary finding of that paper is that, although increasing a platform’s performance attracts more consumers by improving one aspect of consumer utility, it also discourages the entry of third-party content developers, which reduces another aspect of consumer utility. Hence, the optimal strategy is often “rightsizing” platform performance so that consumers obtain both a reasonable level of platform performance and a sufficiently large ecosystem of third-party content. In contrast, we do not model platform performance. Rather, the goal of this paper is to focus on the choice of direct investments into resources that facilitate third-party development as a tool to increase participation on both sides of the market and how these investments interact with two-sided pricing decisions. Thus, we differ from Anderson et al. (2014) by shifting from a focus on core platform performance investment to a focus on ecosystem investment. This is facilitated by (1) ignoring platform performance, (2) directly considering investment in platform integration that reduces thirdparty content development costs, (3) making content provider payments to the platform endogenous, and (4) expanding the analysis to hybrid retail platforms in addition to hardware/software platforms and delineating the differences in platform strategy between the two platform types. Hence, our results are generally orthogonal to that paper’s results. Importantly, our results sometimes revise or clarify the prior literature. For example, one finding in this paper is that allowing integration investment creates regimes in which platform pricing decisions respond to environmental parameter changes in a manner directionally opposite to what would be predicted by standard two-sided network models.

Integration tools, whether APIs and other investments in increasing platform modularity, SDKs and other dedicated information systems, specialized organizational structures, or better specifications, etc., all provide a means to facilitate the integration of third-party applications more effectively into the platform. There is a stream of research that focuses on the issues surrounding integration when “knowledge work” (such as product, process, or software development) is distributed across multiple organizations (see the review by Anderson and Parker 2013). Coordinating complex knowledge work projects that span organizational boundaries is more difficult than coordinating those that remain within an organization’s boundaries (Parker and Anderson 2002, Sosa et al. 2004, Amaral et al. 2011). The literature on integration suggests that investing in integration tools and capability increases a firm’s overall performance (Iansiti 1995a, b, 1998; Dyer and Singh 1998; Frohlich and Westbrook 2001; Gopal and Gosain 2010; Anderson and Parker 2013a; Davies and Joglekar 2013). However, none of the papers in this literature focus on quantifying the optimal amount of investment in these capabilities, and they do not examine these questions in a platform context with the exception of the empirical study by Li and Agarwal (2016). Their work analyzes the impact of integration of an application by a platform on the application ecosystem as a whole. However, they primarily focus on how platforms manage the tensior between first-party content and third-party content and do not quantify the optimal amount of invest ment in integration capabilities. We attempt to bridge this gap in the literature by analyzing how much platform should optimally invest in integration tools in order to facilitate the integration of third-party applications.

Providing publicly available integration tools, such as APIs, is a common way to open a platform to the content provider side (Parker and Van Alstyne 2009); thus, the integration investment decision is a part of the platform’s “openness” strategy. In addition to the vast literature on open source software (Lerner and Tirole 2001, 2002, 2005; Johnson 2002; Lee and Mendelson 2003; von Hippel and von Krogh 2003;

Economides and Katsamakas 2006), there is a growing stream of research that studies open platforms (Gawer and Cusumano 2002, West 2003, Gawer and Henderson 2007, Eisenmann et al. 2009, Boudreau 2010, Parker and Van Alstyne 2018). Eisenmann et al. (2009) define openness of a platform as placing no restrictions on participation, development, or use across the platform’s distinct roles whether it involves the content provider side or the end user side. A firm considering whether to open its platform faces a tradeoff between adoption and appropriability (West 2003). One way to reconcile this tradeoff is to “partially” open the platform; for example, publicly providing APIs partially opens a platform’s source code but retains the concept of platform owner (Boudreau and Hagiu 2011). Parker and Van Alstyne (2018) build one of the few mathematical models that studies the decision to partially open a platform. Specifically, in their dynamic model of platform openness and innovation, the platform provider chooses the percentage of code base to open and the length of the period of proprietary developer protection. Our paper is different from these studies, because we do not focus on the tradeoff between adoption and appropriability. Instead, we assume that the platform provider has already decided to grant access to third-party content providers and examine the optimal level of integration investment to facilitate content provider participation.

## 3. Hardware/Software Platforms

In this section, we analyze a hardware/software platform’s strategic investment in integration tools in coordination with its pricing decisions. We first start with the monopoly model and then, analyze competing platforms.

## 3.1. Monopolistic Hardware/Software Platforms

In line with the two-sided markets literature (Armstrong 2006, Hagiu and Spulber 2013, Anderson et al. 2014), we first formulate the utility function for the consumers and the profit function for the content providers. Then, we calculate the participation on both sides of the market for a given set of platform decisions.

Following Anderson et al. (2014), we adopt an additive form for the consumer utility function. Specifically, we divide the value that a consumer obtains from purchasing a platform into two additive components: available content and the base value of the platform before addons (V). For simplicity, we assume that each content provider develops one unit of content; thus, the number of content providers that join the platform, $N _ { D } ,$ is equivalent to the amount of content available on the platform. A consumer gains a net utility of $\alpha ( g )$ from an additional unit of content, where g represents content price (equivalently, con tent providers’ profit margin as described below). Intuitively, $\begin{array} { r } { \frac { \partial \alpha ( g ) } { \partial g } < 0 . } \end{array}$ . For simplicity, we assume a linear form of $\alpha ( g ) = \alpha - g$ , where $\alpha > g . ^ { 1 }$ In addition to utility from access to content, the platform provides a standalone value independent of the number of third-party content providers that join the platform. For example, a computer game console, such as Sony PS4, delivers some value to users through the utility of Blu-ray DVD playback even in the absence of applications or games

We assume that consumers differ in their preferences for certain attributes. We model this heterogeneity using a framework that is akin to the Hotelling linear city model (Hotelling 1929). Specifically, we assume that consumers are uniformly distributed along a unit interval based on a taste parameter. The platform is located at one end of the interval.<sup>2</sup> The greater the distance between a consumer’s location and the platform, the bigger the disutility from unmatched preferences. Analogous to the transportation cost parameter in the Hotelling model, we define t as the mismatch cost, which measures the disutility per unit deviation from the ideal product. A higher t represents a market where consumers feel more strongly about their preferences being matched. Without loss of generality, assuming that the platform sits at 0 on the interval, a consumer with location z 0, 1 obtains the following utility by purchasing the platform:

$$
U (z) = V - t z + (\alpha - g) N _ {D} - p,\tag{1}
$$

where $p$ is the consumer price for the platform. Let $z ^ { * }$ be the consumer who is indifferent between purchasing and not. Assuming an outside option value of $v _ { o } , \ z ^ { * }$ is given by $z ^ { * } = \bar { ( } V - v _ { o } + ( \alpha - \bar { g } ) N _ { D } - p ) / t .$ Consumers with $z \leq z ^ { * }$ will purchase the platform. Given that z is uniformly distributed over [0,1], we can calculate the participation rate of consumers as $z ^ { * }$ . Assuming that there are a total of N potential consumers in the market, consumer market size becomes $N z ^ { * }$

Third-party content providers are assumed to be profit maximizers. Again following Anderson et al. (2014), we assume that content providers each have one title over which they have a local monopoly Hence, each content provider sets its content (title) price at g; that is, a content provider earns g from each unit of content sold, which is also a proxy for the unit profit margin, because the variable cost is normalized to zero.<sup>3</sup> Without loss of generality, we assume that consumers purchase every unit of content developed for the platform, though this assumption can easily be relaxed without directionally affecting the results by assuming that each consumer on average buys a certain fraction of the available content. The platform provider charges the content providers a participation fee of w to join the platform.<sup>4</sup> Note that, in some cases, w may be negative, indicating a direct subsidy. Content providers incur a development cost, which varies from content provider to content provider as a result of differences in engineering efficiency. Specifically, the fixed cost of development <sup>˜</sup>f is assumed to be uniformly distributed on $[ \dot { f } - F / 2 , \dot { f } + F / 2 ]$ , where $f _ { \mathrm { m i n } } = f - F / \dot { 2 } > 0$ . To model the effect of platform investment in integration tools (e.g., APIs and SDKs), we assume that such investment reduces content development cost (in man-hours). Not all integration tools are equally effective in reducing content providers’ costs; the benefit depends on the functionality provided within the tool. Thus, in our model, the platform provider chooses the integration tool functionality level to invest in. Specifically, for an integration tool functionality level of $x ,$ a content provider’s fixed cost is reduced by $\beta x ,$ , where $\beta$ is integration tool effectiveness with respect to cost reduction.<sup>5</sup> Realistically, even the highest possible level of integration tool functionality cannot completely eliminate the fixed cost of content development. For simplicity, we assume that the cost reduction benefit $\beta x$ cannot exceed the minimum possible development cost, f . This implies that integration tool functionality $x ^ { * }$ is bounded above by $f _ { \mathrm { m i n } } / \beta .$ . Consequently, the profit function of content provider i is given by

$$
\pi_ {i} (N _ {C}, x, w) = g N _ {C} - w - \bigl (f _ {i} - \beta x \bigr),\tag{2}
$$

where $N _ { C }$ is the number of consumers who join the platform and $f _ { i }$ is the content provider $i ^ { \prime } \mathrm { s }$ fixed cost, which is uniformly distributed on $\left[ f - F / 2 , f + F / 2 \right]$ or equivalently, in $[ \dot { f } _ { \mathrm { m i n } } , F + f _ { \mathrm { m i n } } ]$ . We normalize the outside option value for content providers to zero. Assuming that there are a total of $M _ { D }$ content providers in the content provider community, the number of content providers that join the platform as a function of consumer participation and platform decisions is given by

$$
N _ {D} (N _ {C}, w, x) = \max \bigl \{M _ {D} \bigl (g N _ {C} - w - f _ {\min} + \beta x \bigr) / F, 0 \bigr \}.\tag{3}
$$

Similarly, assuming that there are a total of N potential consumers in the market, the number of consumers who join the platform as a function of content provider participation and platform decisions is given by

$$
N _ {C} (p, N _ {D}) = \max \left\{N \frac {V - v _ {o} + (\alpha - g) N _ {D} - p}{t}, 0 \right\}.\tag{4}
$$

Solving (3) and (4) simultaneously gives $N _ { D } ( x , w , p )$ and $N _ { C } ( x , p , w )$

$$
\begin{array}{l} N _ {C} (x, w, p) \\ = \max \left\{\frac {N \big (M _ {D} (\alpha - g) (- f _ {\min} - w + \beta x) + F (V - p - v _ {o}) \big)}{F t - g M _ {D} N (\alpha - g)}, 0 \right\} \end{array}\tag{5}
$$

$$
\begin{array}{l} N _ {D} (x, w, p) \\ = \max \biggl \{\frac {M _ {D} \bigl (g N \bigl (V - p - v _ {o} \bigr) + t \bigl (- f _ {\min} - w + \beta x \bigr) \bigr)}{F t - g M _ {D} N (\alpha - g)}, 0 \biggr \}. \end{array}\tag{6}
$$

The platform provider enjoys two revenue streams: purchases of the platform by consumers at price p and the participation fee w charged to each content provider that joins the platform. In addition to the pricing decisions, the platform provider has to decide how much to invest in integration tool functionality. We assume that it is increasingly costly to provide integration tools that have higher functionality. Thus, the fixed cost of providing integration tools is a convex increasing function of integration tool functionality x specified as $k x ^ { 2 }$ . The platform monopolist chooses price $p ,$ participation fee $w ,$ and integration tool functionality level x to maximize its profit given by

$$
\Pi (x, w, p) = (p - c) N _ {C} (x, w, p) + w N _ {D} (x, w, p) - k x ^ {2},\tag{7}
$$

where c is the marginal cost of production for the platform, and $N _ { C } ( x , w , p )$ and $N _ { D } ( \boldsymbol { x } , \boldsymbol { w } , p )$ are given by (5) and (6), respectively. Accordingly, the platform provider’s optimization problem is as follows:

$$
\max _ {x, w, p} \Pi (x, w, p) = (p - c) N _ {C} + w N _ {D} - k x ^ {2}.\tag{8}
$$

Summary of Notation and Assumptions. The notation related to the base model is summarized in Table 1 A summary of model assumptions is as follows.

Assumption 1. Consumers are uniformly distributed alon a unit line according to a taste parameter.

Assumption 2. Content providers’ fixed cost of development is uniformly distributed in $[ f { \stackrel { . } { - } } F / 2 , f + F { \dot { / } } 2 ]$

Assumption 3. Consumers purchase every unit of content developed for the platform (this assumption can easily be relaxed without directionally affecting the results by assuming that each consumer on average buys a certain fraction of the available content).

Assumption 4. Content providers are homogenous in the benefit that they gain from integration investment (this can easily be relaxed by assuming that there are two content provider types with different benefit levels) (see Section A.2.1 in the online appendix).

Table 1. Notation

<table><tr><td></td><td>Decision variables and model primitives</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td>x</td><td>Integration tool functionality level</td></tr><tr><td>p</td><td>Price of platform paid by the consumer</td></tr><tr><td>w</td><td>Participation fee charged to content providers or sellers</td></tr><tr><td>y</td><td>Integration tool functionality level for integration on the buyer side</td></tr><tr><td colspan="2">Model primitives</td></tr><tr><td>g</td><td>Content providers&#x27; marginal profit per consumer</td></tr><tr><td>α</td><td>Consumer gross utility from an additional unit of content</td></tr><tr><td>α(g) = α - g &gt; 0</td><td>Consumer (net) utility from an additional unit of content</td></tr><tr><td>V</td><td>Maximum standalone value for the platform</td></tr><tr><td>vo</td><td>The value of outside option for consumers</td></tr><tr><td>N</td><td>Total number of consumers in the market</td></tr><tr><td>β</td><td>Fixed cost reduction per unit of integration tool functionality</td></tr><tr><td>f</td><td>Average fixed cost incurred by content providers</td></tr><tr><td>fmin</td><td>Minimum possible fixed cost incurred by content providers in the absence of integration tools defined as f - F/2</td></tr><tr><td>F</td><td>The range of fixed cost incurred by content providers, the fixed cost being uniform in [fmin, F + fmin]</td></tr><tr><td>MD</td><td>Total number of content providers in the market</td></tr><tr><td>k</td><td>Platform&#x27;s cost per unit of integration tool functionality squared</td></tr><tr><td>c</td><td>Platform&#x27;s variable cost of production</td></tr><tr><td>t</td><td>Mismatch cost (that is, the disutility per unit deviation from the ideal product)</td></tr><tr><td>γ</td><td>Effectiveness of integration investment on the buyer side</td></tr></table>

Assumption 5. Consumers are homogenous in their utility from content (this can easily be relaxed by assuming that there are two consumer types with different utilities from content) (see Section A.2.5 in the online appendix).

Assumption 6. Cost reduction benefit from integration is a linear function of integration functionality level (see Section A.2.2 in the online appendix for an analysis where this assumption is relaxed).

Assumption 7. The platform charges content providers a participation fee (see Section A.2.3 in the online appendix for an extension based on a transaction fee model).

Assumption 8. Throughout the analysis in the next section, it is assumed that $x ^ { * }$ is an interior solution, satisfying $\frac { f _ { \operatorname* { m i n } } } { \beta } \geq x ^ { * } \geq 0$ . In the online appendix, conditions necessary to ensure $\begin{array} { r } { \frac { f _ { \operatorname* { m i n } } } { \beta } \geq x ^ { * } \geq 0 } \end{array}$ are derived, and boundary conditions are discussed.

## Assumption 9. Content price (g) is exogenous and constant.

By simultaneously solving the first-order conditions for $x , w ,$ and $p ,$ we obtain the optimal decisions for the platform provider stated in Lemma 1.

Lemma 1. The optimal integration functionality level and two-sided pricing decisions for a monopolist hardware/ software platform are given by

$$
\begin{array}{r l} & x _ {H S} ^ {*} = \frac {M _ {D} \beta (N \alpha (V - c - v _ {o}) - 2 f _ {\min} t)}{2 (4 F k t - k M _ {D} N \alpha^ {2} - M _ {D} t \beta^ {2})} \\ & \qquad \left(2 k (c F N (\alpha - 2 g) - 2 f _ {\min} F t + \alpha f _ {\min} M _ {D} N (\alpha - g) \right. \\ & w _ {H S} ^ {*} = \frac {(+ F N (2 g - \alpha) (V - v _ {o})) + \beta^ {2} M _ {D} N (\alpha - g) (V - c - v _ {o}))}{2 (4 F k t - k M _ {D} N \alpha^ {2} - M _ {D} t \beta^ {2})} \\ & \qquad \left(2 k (2 t (F (V + c - v _ {o}) + f _ {\min} g M _ {D}) \right. \\ & \qquad \left. - \alpha M _ {D} (g N (V - c - v _ {o}) + f _ {\min} t)\right) \\ & p _ {H S} ^ {*} = \frac {- \alpha^ {2} c M _ {D} N) - \beta^ {2} M _ {D} t (V + c - v _ {o}))}{2 (4 F k t - k M _ {D} N \alpha^ {2} - M _ {D} t \beta^ {2})}. \end{array}
$$

We note that, if the fixed cost of even the most efficient content providers, $f _ { \mathrm { m i n } } ,$ is very high $( \mathrm { i } . \mathrm { e } . , f _ { \mathrm { m i n } } >$ $\frac { N \alpha ( V - c - v _ { o } ) } { 2 t } )$ , then the platform provider cannot profitably attract third-party content providers. Under that scenario, the platform fails to build a content provider ecosystem, but as long as the maximum standalone value of the platform, $V ,$ is high enough $( V > c + v o )$ , the platform provider can still serve the consumer side.

Next, in Proposition 1, we analyze the effect of important market parameters on the integration investment strategy.

Proposition 1. Based on the optimal solution described in Lemma $1 , ^ { 6 }$ the following hold.

(i) Integration investment increases in consumer gross utility from additional content, α.

(ii) Integration investment increases in integration tool effectiveness, $\beta .$

(iii) Integration investment decreases in consumers outside option value, $v _ { o } ,$ , and content providers’ minimum fixed cost, $f _ { \mathrm { m i n } }$

(iv) Integration investment decreases in the mismatch cost, t.

Proposition 1 presents important observations about the nature of the integration investment strategy. The optimal functionality level of integration tools always increases with consumer gross utility from content and integration tool effectiveness. Note that an increase in any of these parameters potentially increases the size of the pie that the platform can capture in the market and may allow the platform to charge higher prices. Thus, the platform provider gets a higher return on integration investment, which triggers a higher level of investment. In contrast, an increase in consumers’ outside option value $v _ { o , }$ , content providers’ minimum fixed cost $f _ { \mathrm { m i n . } }$ , or mismatch cost t makes it harder to attract consumers and content providers, shrinking the potential size of the pie. As a result, optimal integration investment goes down.

The effect of content price $g$ on the integration investment strategy is not as straightforward. An increase in g increases content providers’ profit margin but reduces consumer net utility from content, $\alpha ( g )$ . In the base model where $\alpha ( g )$ is defined as $\alpha - g ,$ these opposite effects balance each other out such that a marginal increase in $g$ does not change the potential size of the pie. As a result, the integration investment decision is unaffected. The two opposite effects of $g$ may not always balance out, however, if net utility from content $\alpha ( g )$ has a different structure. For example, we find that, ${ \mathfrak { i f } } \alpha ( g ) = \alpha / g$ , integration investment may increase or decrease in content price depending on the sign of $\alpha / g - g \colon$ that is, depending on the relative strength of the cross-side network effects. Similarly, if $\alpha ( g ) = \alpha - b g$ , integration investment increases in $g$ if and only if $b < 1 . ^ { 7 }$ Note that, if $b < 1$ (similarly, if $\alpha / g < g )$ , when g increases, the marginal increase in content provider profit margin is higher than the marginal decrease in consumer net utility from content. Thus, the potential size of the pie is growing. As a result, the return on integration investment is higher, which triggers a larger integration investment. The opposite is true for $b < 1$ (similarly, for $\alpha / g < g )$ . Integration investment increasing in g may be counterintuitive at first glance; one could argue that, because content providers are already doing better thanks to the higher marginal profit, there is less need to invest in integration tool functionality. However, by increasing the integration investment in these instances, the platform provider can generally charge a higher participation fee, compensating for the investment cost.

Finally, through numeric analysis as shown in Figure $^ { 3 , }$ we find that, if the variability in content providers’ fixed cost (F) increases, the platform provider tends to invest less in integration tool functionality as long as the average cost f is not prohibitively high and consumer utility from content α is strong. This is mainly because with a smaller variance in the cost distribution, a unit increase in integration tool func tionality results in a larger increase in the content provider participation rate. Thus, the return on integration investment is higher when the variability in content providers’ costs is lower, and as a result, integration investment decreases as the cost variability increases. When the average cost is very high and cross-side effects (α and g) are somewhat low, however, an increase in cost variability puts the platform in a tough spot in terms of attracting content providers. Thus, the platform provider is better off increasing integration investment so as to guarantee content provider participation and then, relying more on the consumer side to make money.

We also uncover interesting observations about the interplay between integration investment and two-sided pricing decisions through numeric analysis as summarized in Remark 1.

Figure 3. (Color online) Integration Investment Can Increase or Decrease with Content Providers’ Fixed Cost Variability  
![](/api/attachments/G5ZKZPRS/fulltext/images/3d32d908a425381d7df7ad6df320327ef849eea0b06e0b551e54152bdc049fae.jpg)  
Notes. The figure characterizes the sign of $\partial x ^ { * } / \partial F$ as a function of α and f , whereas the values of other parameters are set as follows: $k = \dot { 2 } , V = 1 . 3 , M _ { D } = 1 , N = 1 , \beta = 2 , \tilde { F } = 5 , c = 0 . 2 , v _ { o } = 0 , g = 0 . 6 ,$ , and t 1. Please note that the illustrated behavior of the derivative is not sensitive to the specific value of F.

Remark 1. The following observations can be made about two-sided pricing decisions for a monopolist hardware/software platform in the presence of integration investment as an additional strategic lever.

(i) Content provider participation fee w may increase or decrease with $\alpha ,$ consumer gross utility from content.

(ii) Consumer price p may increase or decrease with $\alpha ,$ consumer gross utility from content.

Remark 1 shows that integration investment may result in two-sided pricing policies that are not seen in the extant literature as explained in Section 1. For example, an increase in consumer gross utility from additional content, $\alpha ,$ implies that consumers now care more about content provider adoption. When this is the case, the previous two-sided markets literature suggests that the platform provider should cut the content provider participation fee in order to increase content availability (Parker and Van Alstyne 2005, Armstrong 2006). However, as Figure 4 shows, it may be optimal to increase the participation fee instead (later, for the competition model, we derive the exact conditions for this result). This is because in our model, the platform provider has an extra lever: integration investment. Investing in integration tool functionality and reducing the participation fee are partially substitutable actions in terms of attracting content providers. As a result, the platform provider can increase the participation fee in response to increasing consumer utility from content and still have higher participation across content providers and consumers. This is more likely to happen if the content provider profit margin (g), the potential content provider market size $( M _ { D } )$ , and the integration tool effectiveness (β) are high, all of which increase the potential return on integration investment. As a result, increasing integration investment becomes a viable substitute for reducing the content provider partici pation fee.

Similarly, Figure 5 shows that an increase in consumer utility from content (through an increase in α) may result in a reduction in consumer price, even though the existing literature would suggest otherwise (Parker and Van Alstyne 2000b, 2005; Armstrong 2006). This is more likely to happen when content price (g) is high relative to consumer gross utility from content (α), which means that consumer net utility from content $\alpha - g$ is low. In such a setting, the crossside network effect is weaker for the consumer side; that is, consumers derive less value from the presence of content providers than the value content providers derive from the presence of consumers. As a result, the consumer side is harder to attract. Thus, when α increases, it may be more profitable to increase the content provider participation fee and integration investment rather than increase the consumer price. In a high-g setting, increased consumer participation owing to lower price coupled with increased integration investment because of higher α can easily compensate for the increased participation fee.

Figure 4. (Color online) Content Provider Participation Fee May Increase or Decrease with Consumer Utility from Content  
![](/api/attachments/G5ZKZPRS/fulltext/images/04e8e7ecdfe2c13e0b86dd7d4a64afec8dac0415577781eacc2ad516cc61a836.jpg)

![](/api/attachments/G5ZKZPRS/fulltext/images/06c90ef76050605fcf177ec4bcd588d1e367128b4074b3d0f5553f01421579e1.jpg)  
x-axis: Content provider potential market size (MD)  
Notes. The figure characterizes the sign of ∂w∗/∂α as a function of $M _ { D }$ and g, whereas the values of other parameters are set as follows: $k = 2 ,$ $V = 1 . 2 , N = \stackrel { \smile } { 1 } , \alpha = 2 . 2 , f _ { \mathrm { m i n } } = 1 , F = \stackrel { \smile } { 5 } , c = 0 . 2 , v _ { o } = 0 ,$ , and t 1. In the left panel, $\beta = 2 ,$ , whereas in right panel, $\beta = 3 .$

Figure 5. (Color online) Consumer Price May Increase or Decrease with Consumer Utility from Content  
![](/api/attachments/G5ZKZPRS/fulltext/images/d618aed8991135a74c128111cd01e1920544977db39bfe3c6115dba0664d6730.jpg)  
Notes. The figure characterizes the sign of ∂p∗/∂α as a function of α and g, whereas the values of other parameters are set as follows: $k = 2 ,$ $V = \bar { 1 } . 2 , N = 1 , M _ { D } = 1 , f _ { \operatorname* { m i n } } = 1 , \bar { F = 5 } , c = 0 . 2 , v _ { o } = 0 , t = 1 , \mathrm { a n d } \beta = 2 .$

Next, we look at the effect of other parameters on the two-sided pricing strategy in Corollary 1.

Corollary 1. Based on the optimal solution described in Lemma 1, the following hold.

(i) Consumer price decreases and content provider participation fee increases with content provider marginal profit $g .$

(ii) Content provider participation fee w increases with integration tool effectiveness, $\beta ,$ if and only if $2 F t >$ $M _ { D } N \alpha ( \alpha - g )$

(iii) Consumer price p increases with integration tool effectiveness, $\beta ,$ if and only if $\alpha - g > g$

Corollary 1(i) shows that the effect of content price on the two-sided pricing strategy is in line with the extant literature. An increase in content price implies that content providers now gain more value from the participation of the consumer side. When this is the case, similar to the results in the literature, our model suggests that the platform provider should cut the consumer price in order to increase consumer adoption and should compensate by increasing the content provider participation fee. Note that, when the effect of content price on consumer net utility from content, $\alpha ( g ) _ { \cdot }$ , is more complex than that in the base model (such as when $\alpha ( g ) = \alpha / g$ or $\alpha ( g ) = \alpha - b g )$ , it is possible to find optimal two-sided pricing strategies that go against this intuition.

Corollary 1, (ii) and (iii), looks at the effect of increasing integration tool effectiveness β on the pricing decisions and shows that, in response to an increase in integration tool effectiveness, prices on either side of the market can go up or down. Recall that, when $\beta$ increases, integration investment always increases. Therefore, one would expect that the developer side would always be charged higher as a result in response to a higher β. Corollary 1 shows that this is not always the case. If consumer net utility from content $\alpha - g$ is large enough, it may be more profitable to reduce participation fee and increase the consumer price instead.

The interplay between two-sided pricing decisions and integration investment highlighted in this section shows the importance of considering pricing and integration investment simultaneously when forming a platform strategy. In the next section, we analyze the same interplay between pricing and integration decisions in a competitive setting.

## 3.2. Competing Hardware/Software Platforms

In this section, we study competition between two platforms building on the model concepts developed in Section 3.1. We first start with symmetric platforms.

3.2.1. Symmetric Duopoly. In this section, we assume that content providers may choose to affiliate with more than one platform or “multihome,” whereas consumers join at most one platform or “single home.” This scenario fits a number of important industries. For example, for smartphones, app developers typically release their applications on both Android and iOS (VisionMobile 2014), whereas most consumers affiliate with only one of these platforms. Similarly, in the video game industry, game developers tend to develop for multiple consoles (Corts and Lederman 2009), but a majority of consumers choose one console in a given generation.

Content providers decide whether to join a platform independent of their participation decision for the other platform (ignoring any budget constraints), because they are able to multihome. Thus, the content provider demand is derived the same way as in Section 3.1:

$$
N _ {D} ^ {i} \big (x _ {i}, p _ {i}, w _ {i}, N _ {C} ^ {i} \big) = \frac {M _ {D} \big (g N _ {C} ^ {i} - f _ {\mathrm{min}} + \beta x _ {i} - w _ {i} \big)}{F}.\tag{9}
$$

Consumers, however, must decide which platform to join, thus creating competition between the platforms to attract them. Depending on the consumer prices $( p _ { 1 } , p _ { 2 } )$ , participation fees $( w _ { 1 } , w _ { 2 } )$ , and integration tool functionality $( x _ { 1 } , x _ { 2 } )$ set by platforms 1 and $^ { 2 , }$ platform i gets $N _ { C } ^ { i }$ consumers and $N _ { D } ^ { i }$ content providers $( i = 1 , 2 )$ . The prospect of these market sizes plays a major role in determining which platform is chosen by consumers.

Similar to the monopoly model, we assume that consumers differ in their taste parameter, which translates into different preferences for each platform. These preferences can arise from multiple sources that include having a library of compatible content or belonging to a community that has adopted a specific platform. In other words, keeping prices and content availability the same, each platform would still have a different appeal to each consumer. Specifically, we use a common competitive market model, Hotelling’s linear city, to capture this effect. Similar to the monopoly model, consumers are uniformly distributed along a unit interval according to their ideal specifications, and the platforms are located at the opposite ends of the interval. The greater the distance between a consumer’s location and a platform, the bigger the disutility of unmatched preferences. Let t be the mismatch cost as before. In the competition context, the variable t can be a proxy for the degree of horizontal product differentiation between the platforms in attracting consumers. Note that low t implies less product differentiation and thus, a higher degree of competition. Without loss of generality, assume that platform 1 is located at point $0 ,$ whereas platform 2 is located at point 1. Accordingly, the net utility from joining platform 1 for the consumer z with taste $z \in$ 0, 1 is ${ \bar { U } } _ { 1 } ( z ) = V + ( \alpha - g ) N _ { D } ^ { 1 } - p _ { 1 } - t z = u _ { 1 } - t z .$

By locating the marginal consumer who is indifferent between the two platforms and using the fact that consumers are uniformly distributed on a unit interval, the number of consumers who join platform $i ( i = 1 , 2 )$ can be calculated as

$$
N _ {C} ^ {i} \big (x _ {i}, p _ {i}, w _ {i}, x _ {- i}, p _ {- i}, w _ {- i}, N _ {D} ^ {i}, N _ {D} ^ {- i} \big) = N \Big (1 / 2 + \frac {u _ {i} - u _ {- i}}{2 t} \Big).\tag{10}
$$

We substitute (9) into (10) to get

$$
\begin{array}{l} N _ {C} ^ {i} \big (x _ {i}, p _ {i}, w _ {i}, x _ {- i}, p _ {- i}, w _ {- i} \big) \\ = \frac {\big (F \big (t - p _ {i} + p _ {- i} \big) - M _ {D} (\alpha - g) \big (g N + w _ {i} - w _ {j} - \beta (x _ {i} - x _ {j}) \big) \big)}{2 \big (F t - g M _ {D} N (\alpha - g) \big)}. \end{array}\tag{11}
$$

Accordingly, platform sponsor i’s $( i = 1 , 2 )$ decision problem is as follows:

$$
\max _ {x _ {i}, p _ {i}, w _ {i}} \Pi_ {i} (x _ {i}, p _ {i}, w _ {i}; x _ {- i}, p _ {- i}, w _ {- i}) = (p _ {i} - c) N _ {C} ^ {i} + w _ {i} N _ {D} ^ {i} - k x _ {i} ^ {2}.\tag{12}
$$

<sup>Summary of Assumptions.</sup> In addition to the assumptions highlighted in Section 3.1, throughout this section, we assume the following.

Assumption 10. Consumers single home, whereas content providers potentially multihome.

Assumption 11. Platforms enter the market simultaneously such that both platforms make their decisions without observing the competitor’s decisions.

Assumption 12. Consumer market is covered (see Section A.2.4 in the online appendix for an extension where this assumption is relaxed).

Under these assumptions, the resulting equilibrium is symmetric, with both platforms setting the integration tool functionality level, price, and participation fee as specified in Lemma 2.

Lemma 2. In a symmetric duopoly with content providers multihoming and consumers single homing, the platforms choose the following integration tool functionality and price levels:

$$
\begin{array}{r l} & x _ {C} ^ {*} = \frac {\beta M _ {D} (N \alpha - 2 f _ {\mathrm{min}})}{2 (4 F k - M _ {D} \beta^ {2})} \\ & p _ {C} ^ {*} = c - \frac {g k M _ {D} (N \alpha - 2 f _ {\mathrm{min}})}{4 F k - M _ {D} \beta^ {2}} - \frac {g M _ {D} N (\alpha - g)}{2 F} + t \\ & w _ {C} ^ {*} = \frac {N (g - \alpha)}{2} + \frac {F k (N \alpha - 2 f _ {\mathrm{min}})}{4 F k - M _ {D} \beta^ {2}}. \end{array}
$$

Next, we analyze the effect of market parameters on the optimal decisions.

Proposition 2. Based on the equilibrium described in Lemma $^ { 2 , }$ , the following hold.

(i) Integration investment always increases and consumer price p always decreases with $\alpha ,$ consumer gross utility from additional content. Content provider participation fee w increases with α if and only if $4 F k \ge \dot { M } _ { D } \beta ^ { 2 } \ge 2 F k$

(ii) Integration investment and content provider participation fee w increase, whereas consumer price $p$ decreases with $\beta ,$ integration tool effectiveness.

(iii) Content provider participation fee w increases with $g .$

The integration investment chosen at equilibrium in a symmetric duopoly is qualitatively similar to the choice of a monopolist; it increases with consumer gross utility from content α and integration tool ef fectiveness $\beta .$ Again, similar to the monopolist’s strategy, integration investment is not affected by content provider marginal profi $g$ under the $\alpha ( g ) = \alpha - g$ formulation but may increase or decrease with $g$ under more complex formulations for $\alpha ( g ) _ { \cdot }$ , such as $\alpha ( g ) = \alpha - b g$ or ${ \overset { \cdot } { \alpha } } ( g ) = \alpha / g . ^ { 8 }$ Finally, similar to the monopoly case, expectations from the extant literature (Parker and Van Alstyne 2005, Armstrong 2006) may not hold when consumer gross utility from content, $\alpha ,$ increases. Specifically, the participation fee w increases when consumer gross utility from content, $\alpha ,$ increases as long as $\mathop { M _ { D } ^ { \mathrm { { } } } } \beta ^ { 2 } > 2 F k$ . This is again because of the partial substitutability of integration investment and participation fee reduction. Table 2 summarizes these results.

The pricing decisions of a duopolist on the consumer side, however, present some differences from those of a monopolist. Mainly, competitive pressure to attract the consumer side tends to create scenarios in which any potential gain in the size of the pie is competed away by reducing the consumer price. For example, when consumer gross utility from additional content, α, increases, a monopolist may increase the price, whereas a duopolist always reduces it. To understand this, first note that, in response to an increase in consumer utility from content, the monopolist tends to increase its integration investment at a faster rate compared with the duopolist (because the former has a higher surplus from integration investment compared with the latter). In other words, when α increases, competing platforms fail to ramp up content provider participation as much as a monopolist would. Thus, they engage in a price war to stay competitive in attracting consumers. The result is a reduced consumer price. Note that this price war result is partly because pf the nature of competition portrayed in the Hotelling model. Because the market size is fixed, platforms cannot expand the market strategically and are more likely to engage in a price war. As discussed in Section 5 and Section A.2.4 in the online appendix, when the Hotelling model is extended with the possibility of market expansion, potential gains in the size of the pie are not always competed away by reducing the consumer price, though price war still remains a common outcome.

Another difference in pricing is the response to an increase in integration tool effectiveness β. As discussed in Corollary 1, in a monopolistic hardware/ software platform, developer participation fee may decrease with $\beta ,$ because under some market conditions, it is better to increase consumer price instead. For competing platforms, increasing consumer price is rarely optimal as discussed above. Thus, developer participation fee always increases and consumer price always decreases with increasing β. Finally, numerical analysis shows that consumer price p can increase or decrease with the content price, g, largely depending on the size of the network effects $\alpha - g$ versus g.

3.2.2. Asymmetric Duopoly. In this section, we extend the analysis to asymmetric platforms. When platforms are differentiated, we observe richer market segmentation scenarios. However, the model quickly becomes intractable; thus, we resort to numerical analysis to gain insights. Figure 6 illustrates an example with two platforms that have different costs for providing integration tool functionality (k) and different standalone values (V). The disparity between integration tool capabilities may stem from previous experience in providing and managing these tools, from having a better software development team, or from having a more amenable platform architecture. For example, one of the reasons Myspace failed to keep up with Facebook was its arcane architecture that was based on .NET, which contributed to its inability to rely on third-party content providers for features or other content. As David Siminoff of the dating website JDate put it (Gillette 2011), “Using .NET is like Fred Flintstone building a database. The flexibility is minimal. It is hated by the developer community.”

Although Facebook reaped the benefits of opening its platform to outside developers, Myspace ended up doing everything itself as explained by Chris DeWolfe, cofounder of Myspace (Gillette 2011): “We tried to create every feature in the world and said, ‘O.K., we can do it, why should we let a third party do it?’”

Intuitively, the platform with higher integration capabilities has an advantageous position in attracting content providers with all else being equal. Similarly, the platform with higher standalone value has an advantage in attracting consumers. Suppose that platform 1 has a higher integration capability but a lower standalone value than platform 2. We analyze which platform is the market leader under different parameter settings. The horizontal axis in Figure 6 represents consumer utility from additional content (α), whereas the vertical axis in Figure 6 represents integration tool effectiveness in reducing content providers’ fixed costs (β).

In the absence of integration investment as an additional lever, platform 1 would never gain a bigger market share on both sides of the market. However, Figure 6 illustrates that platform 1 is the market leader when consumer utility from content (α) and integration tool effectiveness (β) are very high. This is because in markets with high α, content availability becomes key. Because platform 1 can afford to provide more integration tool functionality, it has an edge in such cases as long as integration investment is effective enough. For moderate to high values of α and $\beta ,$ we observe that platform 1 gets a bigger share of the content provider market owing to its advantage in providing integration tool functionality, whereas platform 2 gets a bigger share of the consumer market owing to its higher standalone value. Finally, for low to moderate values of α and $\beta ,$ platform 2 is the market leader, because platform 1’s higher integration capability does not give it an edge in these market settings.

Table 2. Comparative Statics for Competing Hardware/Software Platforms

<table><tr><td></td><td>Integration investment</td><td>Content provider fee</td><td>Consumer price</td></tr><tr><td>Consumer gross utility from content,  $\alpha$ </td><td> $\uparrow$ </td><td> $\uparrow$  or  $\downarrow$ </td><td> $\downarrow$ </td></tr><tr><td>Content provider profit margin,  $g$ </td><td>—</td><td> $\uparrow$ </td><td> $\uparrow$  or  $\downarrow$ </td></tr><tr><td>Integration tool effectiveness,  $\beta$ </td><td> $\uparrow$ </td><td> $\uparrow$ </td><td> $\downarrow$ </td></tr></table>

Figure 6. (Color online) An Example of Market Segmentation in a Duopoly with Multihoming Content Providers and Singlehoming Consumers  
![](/api/attachments/G5ZKZPRS/fulltext/images/6d66e84c658782f31bbd78c73a517211c3b5089b4a2f0c5df7dcb13ed09f6af1.jpg)

![](/api/attachments/G5ZKZPRS/fulltext/images/ab1d7673689dd73b4196705e7812980f8cd1778cac2207c3a49372faed344c6d.jpg)  
x-axis: Consumer utility from content  
Notes. $k _ { 1 } = 2 . 8 , k _ { 2 } = 6 , V _ { 1 } = 1 . 6 6 , V _ { 2 } = 1 . 7 , M _ { D } = 2 , N = 1 , g = 0 . 5 , f _ { \mathrm { m i n } } = 0 . 5 , F = 5 . 8 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 2 , S = 0 . 0 0 0 2 S = S = S 0 .$ , and c 0.05. In the left panel, t 1, and in the righ panel, t 0.75.

In the right panel of Figure 6, the degree of product differentiation is lower compared with the base case, implying more intense competition to attract consumers—a situation that puts platform 1 at a disadvantage, because the standalone value that it offers is lower than that of platform 2. Even though the parameter region in which platform 1 is the market leader does not change between the two panels, the region where platform 1 wins only the content provider side is significantly smaller in the right panel of Figure 6. This is because if platform 1 has a hard time attracting consumers, it will also have a hard time attracting content providers. Indeed, platform 1 is able to secure a bigger share of the content provider market only when integration tool effectiveness is very high.

## 4. Hybrid Retail Platforms

In this section, we analyze the integration investment strategy for retail platforms that bring buyers and sellers together. We focus on hybrid retail platforms, like Amazon, which hold their own inventory in addition to providing access to third-party sellers. This modeling choice facilitates a more direct comparison with hardware/software platforms, because similar to hardware/software platforms, hybrid retail platforms also offer (standalone) value to buyers even in the absence of third-party sellers. Hybrid retail platforms are becoming more important in the retail economy as evidenced by recent moves by Walmart to acquire properties, such as Jet.com, to improve its online market reach (Nassauer 2016, Wolfe 2018). Firms are making significant investments in APIs to provide “contextually intelligent real-time experience across all the channels [that firms] sell through” (Columbus 2017). Zhu and Furr (2016) describe Amazon’s transition and how other firms are likely to follow suit with their own hybrid business models. By directly focusing on hybrid platforms, our study complements the literature that delineates the differences between a pure retail platform (“marketplace”) and a reseller (Hagiu and Wright 2013, 2014).

## 4.1. Monopolistic Hybrid Retail Platforms

The major difference between a hybrid retail platform’s business model and a hardware/software platform’s business model is that hybrid retail platforms typically do not charge a fee to buyers.<sup>9</sup> Thus, we adjust buyers’ utility function as follows:

$$
U (z) = V - t z + (\alpha - g) N _ {D},\tag{13}
$$

where z is uniformly distributed over [0,1]. Note that, in a hybrid retail platform, buyers gain a standalone value from both the core platform and the presence of additional sellers who affiliate with the platform. The seller-side model is kept the same as in Section 3.1. We normalize the variable cost per buyer to zero. Accordingly, the platform provider’s optimization problem becomes<sup>10</sup>

$$
\max _ {w, x} \Pi (w, x) = w N _ {D} - k x ^ {2}.\tag{14}
$$

To summarize, in addition to the assumptions highlighted in Section 3.1, throughout this section, we assume the following.

Assumption 13. Buyers do not pay any fees to join the platform.

Assumption 14. Platform provider’s variable cost per buyer is normalized to zero.

Lemma 3 describes the optimum solution for this problem.

Lemma 3. In a monopolistic hybrid retail platform, the platform provider chooses the following integration tool functionality and seller participation fee:

$$
\begin{array}{r l} & x _ {R M} ^ {*} = \frac {\beta M _ {D} (g N (V - v _ {o}) - f _ {\mathrm{min}} t)}{4 k (F t - g M _ {D} N (\alpha - g)) - M _ {D} \beta^ {2} t} \\ & w _ {R M} ^ {*} = \frac {2 k (g N (V - v _ {o}) - f _ {\mathrm{min}} t) (F t - g M _ {D} N (\alpha - g))}{t (4 k (F t - g M _ {D} N (\alpha - g)) - M _ {D} \beta^ {2} t)}. \end{array}
$$

Next, we analyze the effect of market parameters on the optimal decisions.

Proposition 3. Based on the optimal solution described in Lemma 3, the following hold.

(i) Integration investment and seller participation fees increase in consumer gross utility from additional content, α.

(ii) Integration investment and seller participation fees increase in integration tool effectiveness, $\beta .$

Proposition 3 provides insights into the integration investment strategy for hybrid retail platforms. We find that, despite the different formulation, the investment strategy is similar to that for hardware/ software platforms. However, the pricing strategy for monopolistic hybrid retail platforms is quite different from that for hardware/software platforms, primarily because the platform no longer engages in twosided pricing. In the absence of consumer price as a strategic lever, a hybrid retail platform’s participation fee choice is closer to traditional one-sided pricing decisions; the seller participation fee tends to increase whenever there is a change in market parameters that could increase buyer or seller surplus (for example, an increase in integration tool effectiveness $\beta$ or consumer gross utility from content α). That is because it is no longer possible to reduce the participation fee and recoup the loss through an increase in consumer price, such as was the case in the hardware/software model.<sup>11</sup>

Another difference from the hardware/software monopolist is the effect of content price g. Recall that, in the base model with $\alpha ( g ) = \alpha - g ,$ , content price does not have an effect on the optimal integration investment. For a hybrid retail platform, however, integration investment may increase or decrease with content price. In the absence of consumer price as an additional lever, the two opposing direct effects of increasing g (namely, higher marginal profit for sellers but lower consumer net utility per content) do not cancel out. Numerical analysis suggests that integration investment typically increases with g except for when α $g > 0$ is small and $g$ is relatively high. This is because when $\alpha - g$ is already small, higher content price makes it very hard to attract the consumer side. Thus, the size of the pie tends to shrink, which reduces the return on integration investment and leads to lower investment. Our numerical analysis also shows that the seller participation fee may decrease with $g$ under these circumstances in contrast to the result in hardware/software platforms. This is because the adverse effect of higher g on the buyer side as well as the effect of lower integration investment on the seller side may need to be compensated for by a lower participation fee for the sellers.

To better understand the role of integration investment in the monopolistic hybrid retail platform setting, we solved for the optimal seller fee in the absence of integration investment and found it to be $w ( x = 0 ) =$ $\frac { g N ( V - v _ { o } ) - f _ { \operatorname* { m i n } } t } { 2 t } .$ . It is easy to show that, under market conditions that guarantee a positive integration investment $( x _ { R M } ^ { * } > 0 )$ , this fee is always smaller than $w _ { R M } ^ { * } .$ Thus, not surprisingly, integration investment enables the platform provider to set a higher price for sellers. Additionally, one can see that, in the absence of integration investment, the optimal seller fee is not a function of $\alpha ,$ which means that the platform provider does not increase the seller fee when buyer utility from content increases. In contrast, in the presence of integration investment, the platform is able to increase the seller fee and still increase participation on both sides. Thus, integration investment makes it easier to capture the increased buyer surplus.

## 4.2. Two-sided Integration Strategy

In the previous section, we focused on platforms’ investment into tools to improve seller-side integration, but in a B2B setting, platforms also need to ensure buyer-side integration. In this section, we are looking at the optimal investment level for integration tools directed toward the buyer side as well as the seller side. Some examples of hybrid B2B platforms that wil be familiar to readers include CISCO, Salesforce.com, and SAP. In each of these examples, the core platform provides significant standalone value that is then extended by the presence of a content provider community. The model is the same as the hybrid retail platform model described above except that the consumer utility and platform profit functions are adjusted as below:

$$
\begin{array}{r} U (z) = V + (\alpha - g) N _ {D} + \gamma y - t z \\ \Pi (w, x, y) = w N _ {D} - k x ^ {2} - k y ^ {2}, \end{array}
$$

where y is the integration tool functionality on the buyer side and $\gamma$ is buyers’ benefit from integration investment. To provide a concrete example of increased buyer utility from platform integration investment, consider the rapidly growing market research firm Lucid (https://luc.id). The firm connects providers of survey respondents with brand firms, such as Coca-Cola and Ford, that wish to survey specific buyer segments. By automating the marketplace through the use of APIs, Lucid has dramatically lowered the cost to buyers to participate in the market and procure survey responses.

For simplicity, we assume that the platform incurs the same unit cost k for integration on the buyer side and the seller side. Accordingly, the platform’s optimization problem becomes

$$
\max _ {w, x, y} \Pi (w, x, y) = w N _ {D} - k x ^ {2} - k y ^ {2}.
$$

Lemma 4 describes the optimum solution to this problem.

Lemma 4. In a monopolistic retail platform, the platform provider chooses the following participation fee for the sellers and the integration tool functionality levels for sellers and buyers:

$$
\begin{array}{r l} & {x _ {R T} ^ {*} = \frac {M _ {D} t \beta (g N (V - v _ {o}) - f _ {\mathrm{min}} t)}{t ^ {2} (M _ {D} \beta^ {2} - 4 F k) + g ^ {2} M _ {D} N (\gamma^ {2} N - 4 k t) + 4 \alpha g k M _ {D} N t}} \\ & {y _ {R T} ^ {*} = \frac {g M _ {D} N \gamma (g N (V - v _ {o}) - f _ {\mathrm{min}} t)}{t ^ {2} (M _ {D} \beta^ {2} - 4 F k) + g ^ {2} M _ {D} N (\gamma^ {2} N - 4 k t) + 4 \alpha g k M _ {D} N t}} \\ & {w _ {R T} ^ {*} = \frac {2 k (F t - g M _ {D} N (\alpha - g)) (g N (V - v _ {o}) - f _ {\mathrm{min}} t)}{t (4 k (F t - g M _ {D} N (\alpha - g)) - M _ {D} t \beta^ {2}) - g ^ {2} M _ {D} N ^ {2} \gamma^ {2}}.} \end{array}
$$

The effect of market parameters on the optimal solution is qualitatively the same as the effects summarized in Table 3. One new insight obtained from this mode is the complementarity relation of the two integration investments as highlighted in Corollary 2.

Corollary 2. Integration investment toward the seller side increases in the effectiveness of buyer-side integration tools $( \gamma )$ , and integration investment toward the buyer side increases in the effectiveness of seller-side integration tools (β)

Corollary 2 shows that integration investment on one side of the market (seller or buyer) increases in the marginal benefit of integration on the other side. For example, when integration tool effectiveness for sellers (β) increases, not only integration investment on the seller side $x _ { R T } ^ { * }$ but also, integration investment on the buyer side $y _ { R T } ^ { * }$ increase. This cross-side effect shows that there are spillover benefits of integration investment from one side of the market to the other side. This result shows just how important it is for platforms in B2B settings to take a holistic view in their integration investment strategy in order to fully take full advantage of the spillover benefits from one side of a two-sided market to the other.

Next, we analyze which side of the market (seller or buyer) receives a higher integration investment under different market conditions.

Proposition 4. Integration investment toward the seller side is greater than the integration investment toward the buyer side $( i . e . , x _ { R T } ^ { * } \ge y _ { R T } ^ { * } )$ if and only $i f \beta \geq g N \gamma / t .$

Proposition 4 shows that the platform should put a bigger emphasis on integration of the seller side if $\beta / \gamma \geq g N / \hat { t }$ . In other words, for the seller side to receive a larger integration investment, the cost reduction benefit of seller-side integration (β) must be large enough relative to the benefit of buyer-side integration (γ). Note that the condition $\beta / \gamma \geq g N / t$ is more likely to hold if $g N$ is small. That is, if sellers have a small revenue basis, they are likely to get more integration support than buyers in order to ensure seller participation. Finally, a large mismatch cost t makes the seller-side investment more favorable, because the return on investment on the consumer side is smaller under high t. To sum up, higher integration investment tends to be devoted to the side with potential utility that is smaller (small gN) or integration investment benefit that is higher (high β versus high γ).

Table 3. Comparative Statics for a Monopolistic Retail Platform

<table><tr><td></td><td>Integration investment</td><td>Seller participation fee</td></tr><tr><td>Consumer gross utility from content,  $\alpha$ </td><td> $\uparrow$ </td><td> $\uparrow$ </td></tr><tr><td>Seller profit margin,  $g$ </td><td> $\uparrow$  or  $\downarrow$ </td><td> $\uparrow$  or  $\downarrow$ </td></tr><tr><td>Integration tool effectiveness,  $\beta$ </td><td> $\uparrow$ </td><td> $\uparrow$ </td></tr></table>

## 4.3. Competing Hybrid Retail Platforms

In this section, we analyze competing hybrid retail platforms. We modify the duopoly model in Section 3.2 to the hybrid retail platform environment by eliminating consumer price and normalizing variable cost per buyer to zero. All other assumptions remain the same as stated in that section. Note that, as in the base model, integration investment is directed only to the seller side. Lemma 5 describes the optimal solution for this problem.

Lemma 5. In a symmetric duopoly of hybrid retail platforms, the platform providers choose the following integration tool functionality and seller participation fee levels:

$$
\begin{array}{c} x _ {R C} ^ {*} = \\ \frac {\beta M _ {D} (g N - 2 f _ {\min}) (2 F t - g M _ {D} N (\alpha - g))}{4 F K (4 F t - 3 g M _ {D} N (\alpha - g)) - 2 \beta^ {2} M _ {D} (2 F t - g M _ {D} N (\alpha - g))} \\ w _ {R C} ^ {*} = \\ \frac {2 F k (g N - 2 f _ {\min}) (F t - g M _ {D} N (\alpha - g))}{2 F K (4 F t - 3 g M _ {D} N (\alpha - g)) + \beta^ {2} M _ {D} (g M _ {D} N (\alpha - g) - 2 F t)}. \end{array}
$$

Next, we analyze the effect of market parameters on the optimum decisions.

Proposition 5. Based on the equilibrium described in Lemma 5, the following hold.

(i) Integration investment increases in consumer gross utility from additional content α.

(ii) Integration investment decreases in the degree of platform differentiation t .

(iii) The seller participation fee decreases in buyers’ gross utility from content α if and only if $M _ { D } \beta ^ { 2 } \geq 2 \bar { F } k$

(iv) The seller participation fee decreases in the degree of platform differentiation t if and only if $M _ { D } \beta ^ { 2 } \geq 2 \breve { F } k$

There are a few observations to make about integration investment decisions in a symmetric duopoly of hybrid retail platforms. Similar to monopolistic hybrid retail platforms, integration investment always increases in the buyers’ gross utility from content, α. Numerical analysis suggests that integration investment increases with integration investment effectiveness, β, and content price, g, as well We also see in Proposition 5(ii) that integration investment decreases with the degree of platform differentiation, t. In other words, as the intensity of competition between platforms weakens, platforms choose to invest less in integration. Though not surprising on its own, we note that, for symmetric hardware/ software platforms, integration investment is not affected by the intensity of competition, because that effect is completely absorbed by the consumer price decisions. For symmetric hybrid retail platforms, competition intensity does affect the integration investment and participation fee decisions, because there is no fee for buyers that could absorb the effect of changing competition intensity.

Proposition 5 also highlights some interesting observations on the optimal seller participation fee. As the intensity of competition goes down (i.e., t increases), one would expect the seller participation fee $( w _ { R C } ^ { * } )$ to increase in the absence of a buyer fee to absorb the effect. However, Lemma 5 shows that the seller participation fee decreases if $M _ { D } \beta ^ { 2 } \geq 2 F k$ . To understand why this happens, note that integration investment always goes down when the effect of competition weakens. In an environment with high integration effectiveness, β, a reduction in integration investment could hurt seller participation significantly. Thus, when $M _ { D } \beta ^ { 2 } \geq 2 F k _ { . }$ , competing platforms reduce the seller participation fee instead of increasing it in response to weakening competition intensity Lemma 5 also shows that, similar to hardware/software platforms, the seller participation fee may decrease or increase with the buyers’ gross utility from content (α) This is again owing to the partial substitutability of reducing the participation fee and increasing integration investment.

## 5. Discussion and Limitations

It is well known in the product development literature that investment in integration tools that reduce the costs of third-party content providers and provide a more seamless user experience decisively influences the success of products in the market place (Iansiti 1998). Information platforms (e.g., eBay, Google, Facebook, Nintendo, Android, etc.) are no exception. Some integration tools, particularly APIs, have been used to create thousands of applications: so much so that more than half of the traffic to major platforms, like Twitter and eBay, comes through APIs (Woods 2011), and now, “API as a business strategy” has become part of the platform vocabulary (Jacobson et al. 2011). Platforms that fail to invest in such integration tools, such as the majority of current electronic healthcare records platforms, deter complementary content application development by third parties (Lim and Anderson 2016). However, integration investment will almost certainly impact the success of IoT because of its dependence on third-party content providers. Yet, a formal analysis of investment in integration tools by platforms remains, to the best of our knowledge, absent in the literature.

The key insight from our study is that investment into tools that facilitate content development not only is of crucial importance but also, must be well coordinated with pricing decisions to both sides of the market in order to obtain the maximum benefit. Moreover, the possibility for integration investment may create regimes that depart from traditional results in the platform literature. For example, the standard result obtained from strengthening the network benefit to one side of the market is to increase the price charged by the platform to that side and reduce the price charged to the opposite side. However, our results suggest that, under many market conditions, prices to both sides of the market should optimally increase.

For example, with respect to hardware/software platforms, when consumer utility from content goes up, it may be optimal to increase the content provider participation fee in addition to increasing the consumer price. The reason underlying this and many other nonstandard results is that investing in integration tools and reducing content provider participation fees are partially substitutable actions in terms of attracting content providers. There is an important distinction between the two levers, however. Integration investment is a fixed cost that does not increase as more content providers join. In contrast, reducing participation fees is akin to a variable cost, because the burden increases with the number of content providers joining the platform. Thus, the decision to increase integration investment and the decision to reduce content provider participation fees are not entirely comparable. Guidance around how to trade these decisions off is critical to both senior managers who must make the decisions and investors who must evaluate these decisions.

Our study also highlights the role of integration investment under competition. Specifically, we illustrate that a platform that offers a lower standalone value to consumers than its competitor may become the market leader if it better facilitates third-party content development. This happens in a market in which integration investment is very effective in reducing content provider fixed costs, consumers highly value content availability, and the content provider profit margin is high enough. As discussed in Section 3.2.2, better integration investment indeed played a role in Facebook’s victory over Myspace, because the latter had an arcane site architecture “hated by the developer community” (Gillette 2011).

To summarize, our results suggest that higher levels of integration investment in hardware/software platforms become optimal if the platform has access to a large pool of potential content providers and consumers, is able to develop integration tools that are highly effective in reducing third-party development costs, and operates in a market where content providers earn a high-enough profit margin while creating content that is highly valued by the consumer market. Furthermore, the possibility of integration investment may push markets into different outcomes from those that have been observed under the standard results in the platform literature.

In addition to hardware/software platforms, we also examined the role of integration in hybrid retail platforms. In many ways, the two behave similarly, but there are some important differences in pricing, because hybrid retail platforms use a one-sided pric ing strategy. An interesting result in our study is with respect to B2B platforms (e.g., CISCO, Salesforce.com, and SAP) that can invest in integration tools to facilitate both seller and buyer participation. Integration investment on one side of the market (seller or buyer) increases in the effectiveness of integration for the other side. For example, when integration tool effectiveness for sellers increases, not only integration investment on the seller side but also, integration investment on the buyer side increase. Hence, there are spillover benefits of integration investment from one side of the market to the other side. In other words, integration investment directed to buyers and integration investment directed to sellers are complements, not substitutes as one might expect.

There are a number of limitations to our study. In our model of multihoming content providers, we make a simplifying assumption that content providers do not experience decreasing fixed costs when transplanting content to a different platform. Although this simplification is done for mathematical convenience, spreading fixed costs across both platforms does not qualitatively change our results. When platforms are symmetric, a content provider that develops for one platform also develops for the other. Thus, if content providers experience decreasing fixed costs when they multihome, in effect their overall fixed costs are reduced This reduction would change the optimum levels of the decision variables, but it does not change the structure of the optimum strategy for integration investment.

Throughout the analysis, we assume that all consumers gain the same utility (α g) per additional unit of content. To check the robustness of our analysis with respect to this assumption, we extended the model such that there are two types of consumers: high-type customers who derive more utility from content and low-type customers who derive less. As analyzed in Section A.2.5 in the online appendix, all of the results from the original model still hold qualitatively under this extension. Thus, our results seem to be robust with respect to the assumption of homogenous utility from content. We also assume that consumers purchase every unit of content developed for the platform, though this assumption can easily be relaxed by assuming that each consumer on average buys a certain fraction of the available content. A potential avenue of future work would be extending the model to incorporate consumer preferences over heterogeneous content.

In our analysis of competing platforms, we use the Hotelling model, which is frequently used in the two-sided markets literature (Parker and Van Alstyne 2000a; Armstrong 2002, 2006; Rochet and Tirole 2003; Anderson and Coate 2005; Kaiser and Wright 2006 Armstrong and Wright 2007; Anderson et al. 2014). The Hotelling model in its basic form divides a fixed market size between two firms. Because the market size is fixed, platforms cannot expand the market strategically by lowering prices or increasing investment. As a result, pricing or investment decisions only matter in terms of the price or investment differential between the platforms rather than the actua magnitude of the decisions. This inherent limitation makes it difficult to fully account for strategies that might expand or fail to attract the total market. To examine the robustness of our results with respect to this fixed market size assumption, we performed a numerical analysis using a modified version of the Hotelling model that includes “hinterlands” for each platform (Armstrong and Wright 2009). That is, each platform has a local monopoly over a segment of the population. Under this model specification, potential market size is not fixed, because platforms can strategically expand through their hinterlands. Our analysis, summarized in Section A.2.4 in the online appendix, shows that adding hinterlands ends up further coupling the decision variables. As a result, some of the findings in the base model, such as integration investment level being independent from content price, no longer hold. However, the key model results on integration investment strategy are generally robust to this specification. Consumer price decisions present the biggest differences. Specifically, under the fixed market size assumption, consumer price always decreases in integration tool effectiveness (β) and consumer gross utility from content (α), whereas under the modified version, consumer price may increase in these parameters if the size of the hinterlands is large enough. In other words, having the local monopoly over the hinterlands softens the intensity of competition between the platforms such that they can appropriate some of the increasing consumer surplus by increasing prices.

Another limitation of our model is that the quality of content as well as content price are the same across content providers, and thus, consumers gain the same utility from each additional content regardless of its provider. To see if our results are robust, we extended the base model to include heterogeneity in content quality and price. We modeled two types of content providers: high-type providers that create content with higher quality and low-type providers that develop content with lower quality. We numerically verified that our main results still hold under this extension. We also found that, in general, integration investment increases with the fraction of high-type content in the market. This is primarily because of network externalities; when the average quality of content is higher, the platform is more attractive to consumers, resulting in a bigger surplus from integration investment.

In our analysis of retail platforms, we focus on hybrid retail platforms, like Amazon, which hold their own inventory in addition to providing access to third-party sellers. This modeling choice facilitates better comparison with hardware/software plat forms, because similar to hardware/software platforms, hybrid retail platforms also offer value to buyers even in the absence of third-party sellers. However, as a result of this choice, the results from our analysis do not directly apply to pure retail platforms (marketplaces), such as eBay, which have no value to consumers without independent sellers. Similarly, our analysis setting does not apply to retailers, such as Best Buy, that take ownership of their inventory and then, sell it directly to consumers. This is because in the Best Buy case, there is only core value and no ecosystem value.

Finally, our model covers only a single period. Future work might analyze the interplay between integration investment and pricing in a dynamic framework. For example, an initial investment in integration may enable the platforms to charge higher prices in multiple periods, which would create a stronger case for investing in integration to facilitate third-party content provider participation.

## 6. Conclusion

To conclude, we have developed models of hardware/ software and hybrid retail platforms to explore the key tradeoffs behind investment in integration tools and how that investment interacts with pricing decisions in a two-sided market. Our results provide guidance to firms on how to better internalize the network effects inherent in two-sided markets and make integration investment decisions that are well coordinated with content provider and consumer pricing decisions.

## Acknowledgments

The authors thank Ted Anderson for his game indus try observations that helped to launch this inquiry and

Marshall Van Alstyne for his insightful feedback on this stream of research. They also thank the many seminar and conference participants who provided helpful thoughts and comments. Finally, the authors are grateful to the editors and reviewers for their help and guidance throughout the review process.

## Endnotes

<sup>1</sup> Most results remain qualitatively the same when $\alpha ( g ) = \alpha / g$ . Exceptions are discussed in Section 3.1.

<sup>2</sup> Results are similar if the platform is located in the middle of the interval instead.

<sup>3</sup> Note that the base model can easily be extended to a setting where there are two types of content providers with contents that are sold at different price points, g and g . Such an extension would not change the qualitative results.

<sup>4</sup> In many industries, content providers pay a royalty per each transaction instead of or in addition to a participation fee. Numerical anal ysis summarized in Section A.2.3 in the online appendix confirms that our major results still hold qualitatively for a model with royalties.

<sup>5</sup> We assume that all content providers obtain the same cost reduction benefit from integration tool functionality, even though in practice, some content providers may benefit more from integration tool functionality compared with others. It is straightforward to extend the current model to a setting where there are two types of content providers such that high types benefit more from integration investment (i.e., high β) compared with low types (i.e., low β). As shown in Section A.2.1 in the online appendix, such an extension would not change the qualitative results. We also assume that the cost reduction benefit is a linear function of integration tool quality (βx). A specification with diminishing returns to the integration benefit (β ̅̅x) coupled with a linear cost of integration (kx) gives qualitatively similar results based on numerical analysis as shown in Section A.2.2.

<sup>6</sup> Unless otherwise stated, we use the words increasing and decreasing to refer to weakly increasing and decreasing functions, respectively, throughout the paper.

<sup>7</sup> The proofs for the $\alpha ( g ) = \alpha - b g$ and $\alpha ( g ) = \alpha / g$ formulations are available from the corresponding author on request.

<sup>8</sup> The proofs for the $\alpha ( g ) = \alpha - b g$ and $\alpha ( g ) = \alpha / g$ formulations are available from the corresponding author on request.

<sup>9</sup> We acknowledge that some pure retailers, such as Sam’s Club and Costco, do levy an annual consumer charge, but those are typically pure retailers that are making buyer-side fixed versus variable pricing decisions.

<sup>10</sup> For many retail platforms, sellers pay a transaction fee instead of or in addition to a participation fee. The optimal integration investment remains the same if we switched to a transaction fee framework, and our major results still hold qualitatively as shown in Section A.2.3 in the online appendix.

<sup>11</sup> Interestingly, our numerical analysis summarized in Section A.2.3 in the online appendix shows that, when sellers pay a transaction fee instead of a participation fee, the optimal seller fee may go down with buyers’ gross utility from content. This is because even though the platform charges only the seller side, the total revenue is a function of buyer participation, because the transaction fee is collected per each transaction between sellers and buyers. As a result, just like in the hardware/software model, it may be optimal to reduce the seller participation fee when buyers’ utility from content increases.

## References

Amaral J, Anderson EG, Parker G (2011) Putting it together: How to succeed in distributed product development. Sloan Management Rev. 2(52):51–58.

Anderson EG (2015) Personal communication to authors by health care startup CEO, May 15.

Anderson E, Parker G, Tan B (2014) Platform performance in vestment with network externalities. Inform. Systems Res. 25(1): 152–172.

Anderson EG, Parker GG (2013a) Integration and cospecialization of emerging complementary technologies by startups. Production Oper. Management 22(6):1356–1373.

Anderson EG, Parker G (2013b) Integration of global knowledge networks. Production Oper. Management 22(6):1446–1463.

Anderson EG, Chandrasekaran A, Davis-Blake A, Parker G (2018) Managing distributed product development projects: Integration strategies for time-zone and language barriers. Inform. Systems Res. 29(1):42–69.

Anderson S, Coate S (2005) Market provision of broadcasting: A welfare analysis. Rev. Econom. Stud. 72:947–972.

Armstrong M (2002) The theory of access pricing and interconnection. Cave M, Majumdar S, Vogelsang I, eds. Handbook of Tele communications Economics, vol. 1 (North Holland, Amsterdam), 295–384.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Armstrong M, Wright J (2007) Two-sided markets, competitive bot tlenecks and exclusive contracts. Econom. Theory 32:353–380.

Armstrong M, Wright J (2009) Mobile call termination. Econom. J. (London) 119(538):270–307.

Bakos Y, Katsamakas E (2008) Design and ownership of two-sided networks: Implications for Internet platforms. J. Management In form. Systems 25(2):171–202.

Baldwin CY, Clark KB (2000) Design Rules: The Power of Modularity (MIT Press, Cambridge, MA).

Barrie J (2015) Here’s how the Internet of things will solve traffic jams and take the stress out finding a parking space. Business Insider (January 27), http://www.businessinsider.com/ofcom-report-on -internet-of-things-2015-1.

Benzell S, Hersh JS, Van Alstyne MW, LaGarda G (2019) The paradox of openness: Exposure vs. efficiency of APIs. Working paper, Massachusetts Institute of Technology, Cambridge.

Bhargava HK, Choudhary V (2004) Economics of an information in termediary with aggregation benefits. Inform. Systems Res. 15(1): 22–36.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10):1849–1872.

Boudreau K, Hagiu A (2011) Platform rules: Multi-sided platforms as regulators. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar Publishing Inc, London), 163–191.

Bourreau M, Kourandi F, Valletti T (2015) Net neutrality with com peting Internet platforms. J. Indust. Econom. 63(1):30–73.

Caillaud B, Jullien B (2003) Chicken and egg: Competition among intermediation service providers. RAND J. Econom. 34(2): 309–328.

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Columbus L (2017) 2017 is quickly becoming the year of the AP economy 2017 is quickly becoming the year of the API economy. Forbes (January 29), https://www.forbes.com/sites/louiscolumbus 2017/01/29/2017-is-quickly-becoming-the-year-of-the-ap -economy/.

Corts K, Lederman M (2009) Software exclusivity and the scope of indirect network effects in the U.S. home video game market. Internat. J. Indust. Organ. 27(2):121–136.

Davies J, Joglekar N (2013) Supply chain integration, product modularity, and market valuation: Evidence from the solar energy industry. Production Oper. Management 22(6):1494–1508

Dyer J, Singh H (1998) The relational view: Cooperative strategy and sources of interorganizational competitive advantage. Acad. Management Rev. 23(4):660–679.

Economides N, Hermalin BE (2012) The economics of network neu trality. RAND J. Econom. 43(4):602–629.

Economides N, Katsamakas E (2006) Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry. Management Sci. 52(7): 1057–1071.

Eisenmann T, Parker G, Van Alstyne M (2006) Strategies for twosided markets. Harvard Bus. Rev. 84(10), 92–101.

Eisenmann T, Parker G, Van Alstyne M (2009) Opening platforms: How, when and why? Gawer A, ed. Platforms, Markets and In novation (Edward Elgar Publishing Inc, London), 131–162.

Eisenmann T, Parker G, Van Alstyne M (2011) Platform envelopment. Strategic Management J. 32(12):1270–1285.

Evans P, Annunziata M (2012) Industrial Internet: Pushing the boundaries of minds and machines. Technical report, General Electric. Accessed September 1, 2019, https://www.ge.com/ docs/chapters/Industrial\_Internet.pdf.

Frohlich M, Westbrook R (2001) Arcs of integration: An international study of supply chain strategies. J. Oper. Management 19(2): 185–200.

Gawer A, Cusumano M (2002) Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation (Harvard Busi ness School Publishing, Boston).

Gawer A, Henderson R (2007) Platform owner entry and innovation in complementary markets: Evidence from Intel. J. Econom. Management Strategy 16(1):1–34.

Gillette F (2011) The rise and inglorious fall of Myspace. Business Week (June 22), https://www.bloomberg.com/news/articles/2011 -06-22/the-rise-and-inglorious-fall-of-myspace.

Gopal A, Gosain S (2010) Research note—the role of organizational controls and boundary spanning in software development outsourcing: Implications for project performance. Internat. Statist. Rev. 21(4):960–982.

Gupta A, Jukic B, Stahl DO, Whinston AB (2011) An analysis of incentives for network infrastructure investment under different pricing strategies. Inform. Systems Res. 22(2):215–232.

Hagiu A (2006) Pricing and commitment by two-sided platforms. RAND J. Econom. 37(3):720–737.

Hagiu A, Spulber D (2013) First-party content and coordination in two-sided markets. Management Sci. 59(4):933–949.

Hagiu A, Wright J (2013) Do you really want to be an ebay? Harvard Bus. Rev. 91(3):102–108.

Hagiu A, Wright J (2014) Marketplace or reseller? Management Sci. 61(1):184–203.

Hotelling H (1929) Stability in competition. Econom. J. (London) 39(153): 41–57.

Iansiti M (1995a) Science based product development: An empirica study of the mainframe computer industry. Production Oper. Management 4(4):335–359.

Iansiti M (1995b) Technology integration: Managing technological evolution in a complex environment. Res. Policy 24(4): 521–542.

Iansiti M (1998) Technology Integration: Making Critical Choices in a Dynamic World (Harvard Business Press, Boston).

Jacobides M (2013) Blackberry forgot to manage the ecosystem. Bus. Strategy Rev. 24(4):8–8.

Jacobson D, Brail G, Woods D (2011) APIs: A Strategy Guide (O’Reilly Media, Sebastopol, CA).

Johnson JP (2002) Open source software: Private provision of a public good. J. Econom. Management Strategy 11(4):637–662.

Kaiser U, Wright J (2006) Price structure in two-sided markets: Evidence from the magazine industry. Internat. J. Indust. Organ. 24(1):1–28.

Kane S (2010) 5 Predictions for APIs in 2011. GigaOm (blog) (December 31), http://gigaom.com/2010/12/31/5-predictions-for-apis-in-2011/.

Kim JS (2015) What’s really killing digital health startups. TechCrunch (October 30), https://techcrunch.com/2015/10/30/whats-really -killing-digital-health-startups/.

Kramer J, Wiewiorra L (2012) Network neutrality and congestion¨ sensitive content providers: Implications for content variety, broadband investment, and regulation. Inform. Systems Res. 23(4):1303–1321.

Lee D, Mendelson H (2003) Divide and conquer: Competing with free technology under network effects. Production Oper. Man agement 17(1):12–28.

Lerner J, Tirole J (2001) The open source movement: Key research questions. Eur. Econom. Rev. 45(4):819–826.

Lerner J, Tirole J (2002) Some simple economics of open source. J. Indust. Econom. 50(2):197–234.

Lerner J, Tirole J (2005) The economics of technology sharing: open source and beyond. J. Econom. Perspect. 19(2):99–120.

Li Z, Agarwal A (2016) Platform integration and demand spillovers in complementary markets: Evidence from Facebook’s integration of Instagram. Management Sci. 63(10):3438–3458.

Lim SY, Anderson EG (2016) Institutional barriers against innovation diffusion: From the perspective of digital health startups. Proc. 49th Hawaii Internat. Conf. System Sci. (HICSS), (IEEE Com puter Society, Washington, DC), 3328–3337.

MacGillivray C (2016) Worldwide Internet of Things Forecast Update: 2015–2019. (International Data Corporation, Framingham, MA).

Musacchio J, Schwartz G, Walrand J (2009) A two-sided market analysis of provider investment incentives with an application to the net-neutrality issue. Rev. Network Econom. 8(1), 22–39.

Nassauer S (2016) Wal-Mart to acquire jet.com for 3.3 billion in cash stock. Wall Street Journal (August 8), https://www.wsj.com articles/wal-mart-to-acquire-jet-com-for-3-3-billion-in-cash -stock-1470659763.

Parker G, Anderson EG (2002) From buyer to integrator: The transformation of the supply chain manager in the vertically disintegrating firm. Production Oper. Management 11(1):75–91.

Parker G, Van Alstyne M (2000a) Information complements, sub stitutes, and strategic product design. Working paper, Dartmouth College, Hanover, NH.

Parker G, Van Alstyne M (2000b) Internetwork externalities and free information goods. Proc. 2nd ACM Conf. Electronic Commerce (ACM, New York), 107–116.

Parker G, Van Alstyne M (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Parker G, Van Alstyne M (2009) Six challenges in platform licensing and open innovation. Comm. Strategies 1(74):17–36.

Parker G, Van Alstyne M (2018) Innovation, openness and platform control. Management Sci. 64(7):3015–3032.

Parker G, Van Alstyne M, Jiang X (2017) Platform ecosystems: How developers invert the firm. Management Inform. Systems Quart. 41(1):255-266

Pil Choi J, Kim B (2010) Net neutrality and investment incentives. RAND J. Econom. 41(3):446–471.

Reisinger D (2015) Here’s why Internet of things really is the next frontier for businesses. Fortune (September 30), http://fortune .com/2015/09/30/internet-of-things-businesses/.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rochet JC, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Rosoff M (2011) Jeff Bezos “makes ordinary control freaks look like stoned hippies,” says former engineer. Business Insider (October 12), http://www.businessinsider.com/jeff-bezos-makes-ordinary -control-freaks-look-like-stoned-hippies-says-former-engineer-2011-10.

Shueh J (2016) Smart garbage startup cuts city trash costs by 40 percent. Government Technology (April 11), http://www.govtech.com/ civic/Smart-Garbage-Startup-Cuts-City-Trash-Costs-by-40 -Percent.html.

Sosa M, Eppinger S, Rowles C (2004) The misalignment of product architecture and organizational structure in complex product development. Management Sci. 50(12):1674–1689.

VisionMobile (2014) Developer economics Q1 2014 state of the developer nation. Retrieved November 14, 2017, http://www .developereconomics.com/reports/q1-2014/.

von Hippel E, von Krogh G (2003) Open source software and the “private-collective” innovation model. Organ. Sci. 14(2):209–223.

West J (2003) How open is open enough?: Melding proprietary and open source platform strategies. Res. Policy. 32(7):1259–1285.

Weyl EG (2010) A price theory of multi-sided platforms. Amer Econom. Rev. 100(4):1642–1672.

Wolfe A (2018) Marc Lore looks to the future of online shopping. Wall Street Journal (January 26), https://www.wsj.com/articles marc-lore-looks-to-the-future-of-online-shopping-1516998700.

Woods D (2011) Explaining the API revolution to your CEO. Forbe (December 15), http://www.forbes.com/sites/danwoods/2011 12/15/explaining-the-api-revolution-to-your-ceo/2/

Zhu F, Furr N (2016) Products to platforms: Making the leap. Harvard Bus. Rev. 94(4):72–78

Zhu F, Iansiti M (2011) Entry into platform-based markets. Strategic Management J. 33(1):88–106
