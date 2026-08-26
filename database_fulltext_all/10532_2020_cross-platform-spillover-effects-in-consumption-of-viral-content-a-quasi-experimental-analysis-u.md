---
otero_id: 10532
otero_key: "ZAUR8TA7"
title: "Cross-Platform Spillover Effects in Consumption of Viral Content: A Quasi-Experimental Analysis Using Synthetic Controls"
authors: "Haris Krijestorac; Rajiv Garg; Vijay Mahajan"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0897"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.100.58.76] On: 17 May 2020, At: 02:35 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/ZAUR8TA7/fulltext/images/3fe98cedb40428ce3d3a669508f8a4ba46b821f515fa7b6b409dcd7417071794.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Cross-Platform Spillover Effects in Consumption of Viral Content: A Quasi-Experimental Analysis Using Synthetic Controls

Haris Krijestorac, Rajiv Garg, Vijay Mahajan

Haris Krijestorac, Rajiv Garg, Vijay Mahajan (2020) Cross-Platform Spillover Effects in Consumption of Viral Content: A Quasi-Experimental Analysis Using Synthetic Controls. Information Systems Research

Published online in Articles in Advance 15 May 2020

https://doi.org/10.1287/isre.2019.0897

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Cross-Platform Spillover Effects in Consumption of Viral Content: A Quasi-Experimental Analysis Using Synthetic Controls

Haris Krijestorac,<sup>a</sup> Rajiv Garg,<sup>a</sup> Vijay Mahajan<sup>a</sup>

<sup>a</sup> McCombs School of Business, The University of Texas at Austin, Austin, Texas 78705

Contact: haris.krijestorac@utexas.edu (HK); rgarg@alumni.cmu.edu, https://orcid.org/0000-0002-5710-5458 (RG); vijay.mahajan@utexas.edu (VM)

Received: Revised: Accepted: <sup>August 28, 2019</sup>Published Online in Articles in Advance: May 15, 2020

https://doi.org/10.1287/isre.2019.0897

Copyright:

Abstract. To inform product release and distribution strategies, research has analyzed crossmarket spillovers in new product adoption. However, models that examine these effects for digital and viral media are still evolving. Given resistance to advertising, firms often seek to promote their own viral content to boost brand awareness. However, a key shortcoming of virality is its ephemeral nature. To gain insight into sustaining virality, we develop a quasiexperimental approach that estimates the backward spillover onto a focal platform by introducing a piece of content onto a new platform. We posit that introducing content to the audience of a new platform can generate word of mouth, which may affect its consumption within an earlier platform. We estimate these spillovers using data on 381 viral videos on 26 platforms (e.g., YouTube, Vimeo) and observe how consumption of videos on an initial “lead” platform is affected by their subsequent introduction onto “lag” platforms. This spillover is estimated as follows: for each multiplatform video, we compare its view growth after being introduced onto a new platform to that of a synthetic control based on similar single-platform videos. Analysis of 275 such spillover scenarios reveals that introducing a video onto a lag platform roughly doubles its subsequent view growth in the lead platform. This positive cross-platform spillover is persistent, bursty, and strongest in the first 42 days. We find that spillover is boosted when the video is consumed more in the lag platform, when the consumption rate peaks earlier in the lag platform, and when the lag platform targets a foreign market. Delaying a video’s introduction onto a lag platform affects spillover concavely, whereas its introduction onto additional platforms shows diminishing returns We find further support for positive spillover through a small-scale randomized field experiment. Implications are discussed for platforms, content creators, and policy makers.

History: Ravi Bapna, Senior Editor; Sunil Wattal, Associate Editor

Keywords: spillover effect • quasi experiments • synthetic control • information diffusion • viral marketing

## 1. Introduction

The popularization of content through word of mouth (WOM) has led to the phenomenon of “virality,” which is considered the holy grail of digital marketing (Akpinar and Berger 2017). Although viral campaigns may help firms increase brand awareness, a key drawback of viral content is that the buzz it creates tends to be short-lived (Bampo et al. 2008). Although viral media have appealing qualities that help them generate strong initial WOM, there is little guidance on how to sustain this momentum to maximize viral potential. However, it has been shown that introducing a product (e.g., movies, home computers) into a new market may affect its adoptions in existing markets (Putsis et al. 1997, Neelamegham and Chintagunta 1999). By extension, we propose that introducing viral content onto new digital platforms may affect its adoption on existing platforms. Understanding these cross-platform spillover effects can help firms improve their distribution strategies for viral content.

Creating popular digital media is vital to firms today given consumer resistance to advertising (Wright 1975, Rumbo 2002) and the increasing use of adblockers. Trends in marketing strategy confirm that firms are increasingly investing in original content, rather than focusing merely on advertising (Corcoran 2009). In lieu of advertising, WOM enabled by the internet helps firms leverage crowds to promote their content; in fact, 59% of individuals actively share online content with their peers (Allsop et al. 2007). Through sufficient sharing and WOM, content may “go viral” and be consumed by many individuals. However, achieving virality is a monumental challenge. The internet seems to reward very select content, while drowning out the rest; for example, only 2% of YouTube videos achieve over 100,000 views, and a mere 0.33% achieve over 1 million views.<sup>2</sup> One reason for this inequality may be that new content is constantly emerging online, which is supported by Eric Schmidt’s claim that we create as much content every two days as we did from the beginning of time until 2003 (Siegler 2010). This influx of new media may make it hard for older content to remain attractive (Wu and Huberman 2007). As a result, strategies to sustain the popularity of viral media remain elusive.

Extant research has considered intraplatform spillover effects (i.e., users of a particular platform informing each other of available content) as potent driver of consumption (Van Alstyne et al. 2016). Still, relatively little is known about how this spillover travels across platforms. Furthermore, research on spillover in physical markets suggests that consuming products (offline) in one market (e.g., a country or region) tends to affect consumption in other markets (Putsis et al. 1997, Neelamegham and Chintagunta 1999). Through the spread of WOM across these markets, consumers in one market may be either encouraged or discouraged by consumers in other markets to adopt a product. Analogously, we propose that WOM across digital platforms may exhibit similar spillovers. Still, although offline markets may be similar to online platforms in having distinct audiences that exhibit some cross-communication, there are also significant differences between online and offline channels in terms of amount of content produced and the rate of spread and decay of WOM. Moreover, the cost of consuming digital media is much smaller (virtually “zero”) compared with physical goods, leading to experience-driven consumption (e.g., viewing the first few seconds of a video) rather than consumption driven by product characteristics (e.g., price, features). Nevertheless, it remains important for firms to penetrate numerous online platforms (e.g., Instagram, Snapchat), as they have done with traditional markets (e.g., countries, demographics). Despite the important changes associated with the rise of digital platforms, it remains unclear whether introducing a piece of content into multiple platforms would lead to cannibalization (i.e., negative spillover) or whether such a strategy could yield positive spillovers that boost consumption within each platform. A better understanding of this cross-platform spillover may help firms and content creators understand how to seed their content across these platforms, and thus promote their viral content more effectively.

In this study, we present an approach to explore the nature (i.e., valence, magnitude, change over time) of spillover effects in consumption of digital media across platforms. We also examine how characteristics of the various platforms affect these spillovers. Specifically, we pose the following research questions: (1) How does the introduction of viral content onto a new online platform affect (i.e., lift) its consumption in previous online platforms? (2) How do the characteristics of the new online platform affect this lift? (3) How does the timing of a viral video’s entry into the new platform affect this lift?

To address these questions, we introduce a quasiexperimental approach to estimate the effect of introducing a piece of content onto a new platform on its consumption in a prior platform. Our data set consists of daily view statistics for 1,382 online videos viewed over 26 platforms (e.g., YouTube, Vimeo) over 671 days. Among these videos, we identify 381 videos that achieve over 100,000 views; these videos can thus be considered viral for our analysis. These viral videos consist of 349 single-platform videos and 32 multiplatform videos. Within the 32 multiplatform videos, there are 289 pairs of platforms in which a video is introduced sequentially onto one platform (the lead platform) before the other (the lag platform). Each of these 289 platform pairs presents a potential spillover, which constitutes our unit of analysis. To estimate the extent of backward spillover onto th lead platform created by a video’s subsequent introduction onto a lag platform, we compare the view growth of videos on their lead platforms after their introduction onto lag platforms to that of comparable single-platform videos. Considering a video’s introduction onto a lag platform as a “treatment,” we construct a synthetic “control” through a matching algorithm that identifies single-platform videos with consumption patterns that are similar up until the time of treatment. Because the past consumption o digital media is a strong predictor of its future consumption (Szabo and Huberman 2010, Pinto et al. 2013), one can argue that any significant and systematic differences in posttreatment views between treated videos and controls will likely be due to some exogenous shock (i.e., treatment). To measure the effect of this intervention, we construct a lift metric defined as a ratio of view growth of a treated video to that of a control within a given time window.

We employ a synthetic control approach in our quasi-experimental analysis, because synthetic controls are appropriate for evaluating causal effects of shocks and policies in scenarios where largescale experimental inferences cannot easily be conducted (as is the case with viral content; Abadie and Gardeazabal 2003, Abadie et al. 2010). For this reason, synthetic control has been referred to as “the most important innovation in the policy evaluation literature in the last 15 years” (Athey and Imbens 2017, p. 9). Synthetic controls help establish causality even when there is only one or a few treated observations (Abadie and Gardeazabal 2003, Abadie et al. 2010, Hinrichs 2010, Billmeier and Nannicini 2012, Coffman and Noy 2012, Eren and Ozbeklik 2016, Tirunillai and Tellis 2017). For example, in the seminal paper that develops the synthetic control method, Abadie and

Gardeazabal (2003) estimate causal effects of terrorism on economic indicators in Spain’s autonomous Basque Country. They achieve causal identification by comparing economic outcomes after a terrorist act (the treatment) to the same economic outcomes associated with a combination of other Spanish regions that exhibited similar pretreatment economic performance. Hence, these regions can be considered comparable in terms of all relevant indicators, suggesting that any substantial differences in posttreatment economic performance were likely due to the treatment itself. More recently, Tirunillai and Tellis (2017) estimated causal effects of television advertising on online chatter, by comparing online chatter of a given brand after its television ad to that of rival brands that did not advertise on television.

In addition to its ability to extract causal insights from limited data, the synthetic control approach helps us satisfy the parallel trends assumption<sup>3</sup> that is necessary for all matching approaches like propensity score matching (PSM; Rosenbaum and Rubin 1983). Although PSM assumes that endogeneity between treated and untreated items can be minimized using observable characteristics of these items, these observables may not always be relevant indicators of the propensity of an observation to receive treatment; moreover, there may be relevant unobserved characteristics that can affect this propensity (Aral et al. 2009, Oestreicher-Singer and Zalmanson 2010). By matching treated and control videos based on their pretreatment consumption patterns, we implicitly account for any latent factors (e.g., video length, number of channel subscribers) that may affect a video’s expected future consumption in absence of treatment. Although new approaches such as lookahead PSM (Bapna et al. 2018) offer alternative ways to account for latent characteristics, they rely on having large data sets, which are difficult to obtain on viral videos. In adapting the synthetic control methodology to the context of information diffusion, this study joins a growing body of research (e.g., Hoban and Bucklin 2015, Arora et al. 2017, Johnson et al. 2017, Tirunillai and Tellis 2017) that introduces data-driven methods to address causal questions that have so far eluded answers.

Our analysis reveals a positive spillover (i.e., lift) across video-sharing platforms. Specifically, we find that introducing a video onto a new platform grows the consumption of that video to about twice as much on the initial platform as it would have otherwise. Lift is strongest within the first few days after the video is introduced onto the new platform, before declining rapidly, and exhibiting sharp bursts around days 18 and 42. It eventually stabilizes and remains significant in the long run. This suggests that introducing a video onto a new platform may create awareness that spills over onto prior platforms, thereby boosting adoption of the video in these platforms. We validate these results and our quasi-experimental method using a small-scale field experiment, which shows very similar lift estimates.

To understand how platform characteristics affec spillover, we consider a video’s diffusion pattern in the lag platform, the type of the lag platform (i.e., foreign, niche, funny), and the timing of its introduction onto this platform. To parameterize diffusion patterns, we employ the nonuniform influence (NUI) model (Easingwood et al. 1983) that estimates the effects of advertising and WOM on diffusion patterns. Our analysis suggests that videos that generate earlier peak WOM in the lag platform produce stronger spillover and thus increased consumption on the lead platform. Analysis also reveals that lag platforms targeting a foreign (i.e., non-English-language) audience create greater spillover. This result is analogous to prior findings that suggest that introducing a physical product to a new geographic market may generate positive spillovers onto an existing market (Putsis et al. 1997). In terms of timing, we find that the delay between a video’s introduction into lead and lag platforms affects spillover concavely; in other words, delaying the introduction of a video onto a new platform increases spillover, but delaying too long diminishes the spillover. Furthermore, we find that the spillover created by introducing a video onto each successive platform shows diminishing returns in spillover to the original lead platform.

This paper adds to literature on WOM and spillover effects by developing a methodology to estimate spillovers in the context of information diffusion and showing evidence of positive spillover across platforms for viral media consumption. Our results suggest that rather than cannibalizing each other’s usage, digital platforms may increase awareness of each other’s content through WOM. Furthermore, our findings on the characteristics of platforms that generate spillovers may offer hints into the mechanisms behind cross-platform spillover. Finally, our findings on the shape of lift may have implications for viral marketing, as they suggest specific times during which spillover tends to be strongest.

The remainder of this paper is structured as follows. We first discuss relevant literature on vira marketing, new product diffusion, and spillover effects. We then provide a detailed overview of our data set. Next, we present a synthetic control-based quasiexperimental approach to estimate cross-platform spillovers. We proceed to discuss findings from empirical analysis and offer insights into the role of various factors that affect the magnitude of spillover. We conclude with a discussion of results, including implications and suggestions for future work.

## 2. Literature

In this study, we draw from and contribute to three streams of research: viral marketing, new product diffusion, and spillover effects.

Viral content is characterized as having inherently attractive qualities that encourage consumers to share these media through WOM (Dobele et al. 2005, Leskovec et al. 2007). Viral campaigns are often used to boost awareness of a brand or a product (Ferguson 2008), which may improve sales (Chevalier and Mayzlin 2006, Duan et al. 2008, Chen et al. 2014). Thus, in accordance with some viral marketing literature (e.g., Bampo et al. 2008, van der Lans et al. 2009, Aral and Walker 2011), our study focuses on how to stimulate WOM and increase consumption of viral content.

Because viral content relies on WOM to propagate it, virality may seem chaotic and unmanageable. Hence, there is little insight available on how digital content can achieve its viral potential. Extant research that offers such insights considers the design of viral content (e.g., Aral and Walker 2011, Berger and Milkman 2012, Akpinar and Berger 2017) and can help firms create content that has a greater likelihood of going viral. However, despite their efforts to follow best practices in creating viral content, firms are still at the mercy of the crowd to propagate the content once it gains traction. Consequently, there is no known mechanism available to overcome the ephemeral nature of buzz, which hinders viral content from gaining maximum consumption.

The challenge of boosting adoption of viral content can be likened to that of new product introduction. As a product is consumed by a growing number of individuals, its utility is increasingly demonstrated through social proof, which encourages additional adoptions (Rogers 2003). However, a common challenge with new products is boosting adoption beyond the product’s initial saturation point—an obstacle known as “crossing the chasm.” Although strategies have been proposed to help new technologies break through these saturation points (Moore 2014), there is little insight on how to address similar challenges faced by digital media in sustaining virality.

To explore ways to sustain the popularity of viral media, we look to theory on information spillover. A spillover effect is a phenomenon that broadly refers to the impact of events in one setting on events in a different, seemingly independent setting (Rutherford 2013). In a marketing context, spillovers result from the externalities associated with a product’s adoption, including the spread of WOM across markets. Spillovers have been observed across different advertising channels (Rutz and Bucklin 2011), product categories (Erdem and Sun 2002, Chae et al. 2016), countries (van Everdingen et al. 2009), and even competing brands (Roehm and Tybout 2006, Anderson and Simester 2013, Borah and Tellis 2015)

The effect of introducing a product into a new market on its consumption in prior markets can be referred to more precisely as backward spillover. Such spillovers have been observed in the context of multiple products from a single content creator—for example, the release of a new music album may affect sales of prior albums by that musician (Hendricks and Sorensen 2009). One author of the present paper (Mahajan) observed a backward spillover when the release of his second book boosted sales of his first book. Our research considers backward spillovers in the context of videos that are first introduced onto a focal platform (e.g., YouTube) before being uploaded onto alternative platforms.

Spillover effects can be created by WOM among consumers across different markets, such as physical or geographical locations. Because consumers in different locations may communicate using diverse platforms, introducing a product into a new market may increase awareness of the product in markets where the product already exists (Elberse and Eliashberg 2003, Chae et al. 2016). For example, introducing a product in France may affect the product’s consumption in Germany, as French consumers may communicate with consumers in Germany. This communication may generate greater awareness of the product in Germany, which can stimulate the product’s adoption in the German market (Putsis et al. 1997).

With the digitization of products such as books and music, research has also considered spillover across physical and digital markets. Whereas some studies provide evidence of a negative spillover causing cannibalization of physical product consumption in the presence of digital versions (e.g., Liebowitz 2004, Zentner 2006), other research has failed to show neg ative spillover between physical and digital markets (e.g., Smith and Telang 2009, Danaher et al. 2010). Thus, it can be argued that digital and physical versions of products may attract different consumers, and therefore may not cannibalize each other’s sales

Extant research examines spillovers across physical boundaries (e.g., Putsis et al. 1997, Talukdar et al. 2002, Elberse and Eliashberg 2003) between physical and digital products (e.g., Kannan et al. 2009, Danaher et al. 2010), between online and offline channels (e.g., Brynjolfsson et al. 2003, Zentner et al. 2013), and within online platforms (e.g., Garg et al. 2011, Wang et al. 2018); however, to the best of our knowledge, research has yet to consider spillovers of digital media across online platforms.

Digital media exhibit several distinct properties that may affect the nature of spillovers around them.

Unlike physical products, digital media are “soft goods,” with consumption cost being close to zero. This makes it potentially easier to generate rapid adoption and WOM, as compared with physical goods, and may thus affect WOM across markets. At the same time, digital media are prone to quick perishability, as they may rapidly get drowned out in new content. Because of these differences between physical and digital goods, it remains uncertain whether spillover effects across digital platforms are positive or negative. On the one hand, consuming content on one platform, like Facebook, could be considered a substitute for consuming it on another platform, like Twitter. Hence, the consumption of a piece of content on one platform may cannibalize its consumption on the other, because substitutive products generally exhibit negative spillover (Eliashberg and Robertson 1988, Walters 1991). On the other hand, introducing this content to a new audience may build awareness of it in prior markets, thereby increasing consumption in these earlier markets and creating positive spillover (Gong et al. 2015). Such a result would suggest that different platforms attract different consumers, or that the experience of consuming a piece of content on one platform is not substitutable for the same experience within a different platform. Figure 1 depicts how backward spillover would occur across two online video platforms, which is the context of our study.

Although the above mechanism, as illustrated in Figure 1, has already been demonstrated in numerous contexts, we found support for the existence of this mechanism in our specific context by surveying 29 randomly selected university students. Based on these discussions, we found that 69% of individuals search for and watch online videos based on recommendations from friends. Furthermore, 72% of respondents indicated that if they heard about a video on Vimeo that they wanted to watch, they would search for the video on YouTube to watch it. Finally 66% of respondents told us that if they found a video on Vimeo that they wanted to share, they would share the YouTube version of the video, because YouTube is the platform used by most of their friends. Overall these responses support the importance of WOM as a driver of online video consumption and suggest that this WOM may spread across platforms.

Figure 1. (Color online) Illustration of the Backward Spillover Mechanism

<table><tr><td>t =</td><td>Description</td><td colspan="2">Illustration</td></tr><tr><td rowspan="2">n</td><td rowspan="2">Video exists only on YouTube and has accumulated views</td><td>YouTube</td><td>DailyMotion</td></tr><tr><td><img src="/api/attachments/ZAUR8TA7/fulltext/images/98eb80f6d4181a3c895451c423cb77eaf45d65d95c27a1009e58f022a90af0c0.jpg"/></td><td><img src="/api/attachments/ZAUR8TA7/fulltext/images/f968d690e4094832b7d73685d83929ad6ec0bfc9258173442a3b296ed2ac4b14.jpg"/></td></tr><tr><td rowspan="2"> $n + \Delta t_1$ </td><td rowspan="2">Video introduced onto DailyMotion while YouTube viewership continues to grow</td><td>YouTube</td><td>DailyMotion</td></tr><tr><td><img src="/api/attachments/ZAUR8TA7/fulltext/images/5e04a6160036de82bd99670637d5c112df18a17b916d1abafe97bf233573ad2f.jpg"/></td><td><img src="/api/attachments/ZAUR8TA7/fulltext/images/f51046ba03adafe70c9e52c41311dc6fb64f4a5048e6ca7db409a81cca70970b.jpg"/></td></tr><tr><td> $n + \Delta t_1 + \Delta t_2$ </td><td>New DailyMotion viewers spread WOM to other viewers including YouTube viewers</td><td colspan="2"><img src="/api/attachments/ZAUR8TA7/fulltext/images/de0b5c22d1facca783952834a4c0d108836b8f36b33ff6949aaed5c8031aa68d.jpg"/></td></tr></table>

Given the potential existence of cross-platform spillovers, our research seeks to understand what factors may affect the magnitude of these spillovers. Literature reveals numerous such factors, one of which is the diffusion pattern of videos within a platform. A diffusion pattern refers to how the rate and magnitude of adoption of a product vary over time. Because adoption rates reflect the pattern with which WOM about a product propagates within a market, these rates may affect spillover onto other markets. Such effects have been demonstrated in the context of spillover across geographic markets (Putsis et al. 1997), and may therefore be extended to digital platforms. In addition, the timing of a product’s entry into various markets may affect its diffusion within each of these markets (Kalish et al. 1995). This paper contributes to literature on WOM and spillover effects by developing a novel approach to estimating spillovers in the context of information diffusion. In addition to investigating the nature of backward spillover across digital platforms, we identify the effects of platform characteristics and timing of introduction onto these new platforms on spillover.

## 3. Data

Our data set contains daily view counts of 1,382 videos, viewed over 671 days across 26 platforms. These data were provided by a marketing metrics agency<sup>4</sup> that monitored views of and online chatter around its clients’ videos. The videos correspond to household-name consumer brands and target a mass audience. In terms of product category, the videos mostly promote products that are related to food and beverages, beauty and fashion, and technology. The videos are generally aimed at increasing high-level brand awareness (e.g., HP’s “Let’s Do Amazing”), promoting existing products (e.g., McDonald’s “Filet-$\mathrm { \dot { O } - F i s h { ' } { } ^ { \prime \prime } } ) , ^ { \mathrm { \scriptsize \ 6 } }$ or introducing a new product $\mathrm { ( e . g . , A p p l e ^ { \prime } s }$ “Meet iPad”).<sup>7</sup> These videos do not promote limitedtime offers or other offers with high perishability. They can thus be expected to be comparable in terms of longevity.

Daily view counts for these videos are observed over various date ranges between 2009 and 2012. Although these videos do not necessarily exist within the same date range, view counts for each video are observed within each platform over a period of at least one year. These platforms included various videosharing websites, such as YouTube, Vimeo, and Dailymotion. The videos were seeded onto YouTube by the focal company initially and later uploaded to other platforms by independent users of these platforms.

We constrain the boundaries of our study to viral videos, as it is these videos that are likely to generate WOM. Because spillovers are driven by WOM, it is appropriate to impose this boundary, as videos with few views may not have the minimum attractiveness to generate chatter. For similar reasons, studies on spillovers for physical products have focused on popular consumer goods (e.g., cars, microwaves), rather than less popular or niche products. To this end, we excluded from analysis 807 videos that achieved fewer than 100,000 views. In addition, we screened out 181 videos with missing data. The missing values often occurred at the beginning of the video’s diffusion, possibly because the agency did not identify the video in the platform at its exact time of introduction. Finally, we removed 13 non-English-language videos from consideration. Our final data set includes 381 videos from 348 unique firms that can be considered viral, and for which we have daily view count information.

It is important to note that not all videos exist on every platform. In fact, of the 381 videos, only 32 of them were introduced onto multiple platforms. These multiplatform videos were introduced, on average, onto 4.28 platforms. Nearly half (14) of multiplatform videos are associated with only two platforms (see Figure 2). Videos were seeded onto YouTube initially by the focal firm (e.g., Doritos, Adidas, Intel) and were later uploaded onto other platforms by independent users (e.g., Marinemom, speeders23, razzledog). There were 104 users that uploaded these videos onto 26 platforms. These users appear distinct, as no two of their usernames are identical or similar. Based on our examination of other videos posted by these users, they do not seem to be affiliated with any of the focal companies.

Figure 3 depicts the number of multiplatform videos that are associated with the most popular platforms. The popularity of these platforms is skewed, because all videos are on the most popular platform, YouTube, whereas half (13) of the platforms contain only one of the videos in our data set. These single-video platforms are Viddler, StupidVideos, Youku (Chinese), Rofl, VBox7 (Bulgarian), eBaums World, Guzer, Snotr, Dumpert (Dutch), GameTrailiers, ZappInternet (Spanish), Vidi-Life, and Sevenload (German). Additionally, the percentage distribution of videos across product categories for both single-platform and multiplatform videos is similar, as shown in Table 1.

Figure 2. (Color online) Histogram of Number of Platforms per Multiplatform Video  
![](/api/attachments/ZAUR8TA7/fulltext/images/cb04e2d8fbec56eb4b690d75f8912bf5aed661e852facfadf64366beb616dfeb.jpg)

Figure 3. (Color online) Popularity of Platforms of Multiplatform Videos  
![](/api/attachments/ZAUR8TA7/fulltext/images/01edae1b015c738346e82dccb0cc2130bca5dbb7ac78bf8d3b8499db88630ba5.jpg)

Single-platform videos all exist only on YouTube and were uploaded by the focal company. To compare the inherent consumption potential of singleversus multiplatform videos, we compare early view counts of these two sets of videos, because the early popularity of a video tends to predict its future consumption (Szabo and Huberman 2010, Pinto et al. 2013). The distribution of initial views of singleand multiplatform videos in Figure 4 suggests that these two sets of videos are similar in this regard. A Kolmogorov–Smirnov test reveals no significant differences between these distributions (p = 0.16).

Given the similar consumption potential of singleand multiplatform videos, we analyze how a video’s introduction onto a new platform would affect its views on prior platforms. We can preliminarily examine this effect by comparing total cumulative views achieved by single- versus multiplatform videos over their life span. Although Figure 4 suggests similar initial consumption between single- and multiplat form videos, cumulative view counts in Table 2 indicate that multiplatform videos are, on average, consumed more, both on YouTube and in aggregate.

Because multiplatform videos are introduced onto platforms sequentially, we also account for the times at which videos enter these platforms. On average, these videos are introduced onto new platforms 19.95 days after their entry into the initial platform, with a standard deviation (SD) of 59.44. In addition to the delay between the entry time onto the initial platform and entry onto subsequent platforms, there is a delay between entries of videos onto lead–lag platform pairs in general. For example, a three-platform video has a delay not only in entry onto the third and second platforms relative to the first platform, but also a delay in entry onto the third platform relative to the second platform. The average delay between launches of videos onto lead–lag platform pairs is 17.56 days, with a standard deviation of 45.35.

For multiplatform videos, the introduction of the video onto the nth sequential platform presents n – 1 new opportunities to estimate a spillover, because the nth platform can have a spillover onto each of the n – 1 previous platforms. Over the 32 videos that exist on multiple platforms, there are 289 such opportunities to measure spillover, all of which are considered our analysis.

## 3.1. Characterizing Platforms

We characterize platforms by their diffusion patterns as well as their type (i.e., foreign, niche, funny). Con sidering diffusion patterns allows us to control for how WOM around the content might spread, whereas considering platform type controls for the nature of the video’s target audience.

To account for diffusion patterns, we can leverage numerous models that describe these patterns using a parsimonious set of parameters. Broadly, diffusion models consider the impact of WOM that is internal to a market (i.e., within-market WOM) alone, communications outside of the market (e.g., advertising, mass media) alone, and both simultaneously (Mahajan and

Table 1. Distribution of Videos by Product Category

<table><tr><td></td><td>Single-platform videos (n = 349)</td><td>Multiplatform videos (n = 32)</td><td>All videos (n = 381)</td></tr><tr><td>Food and beverage</td><td>168 (48.14%)</td><td>19 (59.38%)</td><td>187 (49.08%)</td></tr><tr><td>Technology</td><td>45 (12.89%)</td><td>5 (15.63%)</td><td>50 (13.12%)</td></tr><tr><td>Clothing and beauty</td><td>94 (26.93%)</td><td>7 (21.88%)</td><td>101 (26.51%)</td></tr><tr><td>Other</td><td>42 (12.03%)</td><td>1 (3.13%)</td><td>43 (11.29%)</td></tr></table>

Figure 4. Distribution of Initial Views of Single- and Multiplatform Videos  
![](/api/attachments/ZAUR8TA7/fulltext/images/61c2e2653289d25ea9f2a1b880ca966008c9832f171e4c7e828ad6a13b8fb24f.jpg)  
Peterson 1985, chapter 2). In our context, both internal and external WOM are relevant to the diffusion of content within platforms. Internal WOM may influence consumption within platforms, because users of a particular platform may inform each other of available content to encourage consumption (Garg et al. 2011). In addition, advertising and mass media may increase brand awareness, which could also influence a video’s consumption. We will thus describe the diffusion of online videos using a mixedinfluence diffusion model (Mahajan and Peterson 1985, p. 24), which considers both internal and external influence factors.

Perhaps the most popular mixed-influence model that can be considered to represent the diffusion of online videos is the Bass (1969) diffusion model (BDM). However, a drawback of the BDM in our context is its assumption of a symmetrical diffusion pattern. Because online videos often exhibit peak view growth relatively early, we expect that many of these videos may have left-skewed diffusion patterns. To account for this possibility, we employ a variant of the BDM known as the NUI model (Easingwood et al. 1983), which is flexible with regard to the timing of the peak diffusion rate. The NUI model is defined by the hazard model in Equation (1) and estimated using the implied Equation (2):

$$
h (t) = \frac {f (t)}{[ 1 - F (t) ]} = p + q F (t) ^ {\delta},\tag{1}
$$

$$
f (t) = \big [ p + q F (t) ^ {\delta} \big ] [ 1 - F (t) ].\tag{2}
$$

In these equations, f(t) represents the pdf of a diffusion pattern, and $F ( t )$ represents its cumulative diffusion. In Equation (1), h(t) represents the hazard rate, or the probability of a random potential viewer watching the video at time t. Parameters $q , p ,$ and δ are the parameters that characterize the diffusion pattern and that we will estimate. Parameter $q$ is the coefficient of imitation, which represents the extent to which consumption within the platforms is influenced by WOM. This parameter affects the hazard rate in proportion to the cumulative adoption at time $t ,$ because greater market penetration of the video means that more people can spread WOM about it. Parameter p is the coefficient of innovation and affects the hazard rate independently of cumulative adoption. Hence, this parameter is interpreted as the impact of non-WOM factors, such as advertising and mass media. Parameter δ represents the nonuniform influence factor, which indicates when a video reaches its peak diffusion rate, and consequently how the effect of parameter q evolves over time. A value of δ equal to one suggests that the diffusion pattern follows the BDM, exhibiting a symmetrical diffusion pattern with peak WOM when it achieves 50% of its market potential. Values of δ below one would indicate that the peak diffusion rate and effect of WOM occur earlier in the diffusion pattern, whereas values greater than one suggest a later peak in WOM. Although parameters $p$ and $q$ are in the range of zero to one, parameter δ can be of any value greater than zero; however, values of δ substantially greater than one are uncommon (Easingwood et al. 1983). Finally, we consider the market potential of a video within a platform, analogous to Bass (1969) parameter m. This parameter indicates the number of cumulative views achieved by a video within a platform.

To estimate the diffusion parameters of each mul tiplatform video within each platform, we employ the nonlinear least squares approach (Srinivasan and Mason 1986). Although this approach has numerous advantages in obtaining more accurate parameter estimates, it can suffer from convergence failures. Indeed, we observe that of the 137 diffusion patterns we estimate, 12 of them fail to achieve convergence during the estimation procedure. Whereas previous studies have estimated diffusion parameters based on monthly or quarterly data, our daily data are more fine-grained, and thus contains more sudden spikes that may cause such estimation failures. To mitigate this issue, we utilize spline smoothing, a procedure that transforms data to remove noise and identify an underlying trend (Cowpertwait and Metcalfe 2009, pp. 21–22). Smoothing can thus help reduce the sharpness of consumption spikes while maintaining a diffusion pattern that represents the trend of the original data. Spline smoothing requires the selection of λ, a smoothing parameter, of between 0 and 1. A higher value for λ yields a smoother transformed diffusion pattern, but also distorts it more from its original form. To resolve the issue of failed parameter estimations while avoiding excessive data distortion, we select a modest value of 0.4 for λ. This method produces parameter estimates that are summarized in Table 3. Our estimates produce diffusion patterns with an average normalized root mean square error of 15.39, suggesting that the original data are not heavily distorted during the smoothing process. Because spline smoothing transforms these diffusion patterns in a way that emphasizes their trend, smoothing also helps to neutralize seasonal effects in the diffusion of these videos; for example, videos may tend to be viewed more or less on certain days of the week. Because the videos in our data set diffuse over different time windows, any seasonal effects are neutralized.

Table 2. Summary Statistics for Single- and Multiplatform Videos

<table><tr><td></td><td>Cumulative views: Mean (SD)</td></tr><tr><td>Single-platform (YouTube only)</td><td>4,549,000(8,251,427)</td></tr><tr><td>Multiplatform (YouTube only)</td><td>5,873,000(20,953,988)</td></tr><tr><td>Multiplatform (non-YouTube)</td><td>87,812(325,577)</td></tr><tr><td>Multiplatform (all platforms)</td><td>6,163,000(21,436,147)</td></tr></table>

Although a low p is relatively common, the value of q is notably lower than its average of 0.38 for durable goods (Sultan et al. 1990). We believe this result is due to low consumption costs associated with digital media. Whereas durable products often have a monetary cost, the cost of consuming online videos is merely time. As a result, individuals may need less social proof from WOM to motivate them to consume the video. Consequently, the effect of internal influence might be lower for digital media than for consumer durables. Because nonuniform influence factor δ is below one on average, we can infer that the effect of WOM tends to peak before the video reaches half its market potential. YouTube notably has a lower average NUI factor of 0.139, indicating that YouTube videos tend to reach their peak WOM rate particularly early. This may be because of greater competition for attention on a large platform like YouTube, which makes WOM more perishable. From the 137 video– platform combinations in our data, 112 (82%) have an NUI factor below one, whereas only 25 have a factor greater than one. This suggests that for online videos, the effect of WOM tends to wear out over time and is thus perishable. The variance of parameter m, or market size, is notably high, because platforms range from hugely popular websites such as YouTube to more niche platforms.

Finally, we sought to characterize platforms based on their qualitative attributes that might make them more or less effective in generating spillover effects. First, we considered whether platforms are in English or in another language. We expect that foreign-language platforms will tend to target audiences that have less overlap with other platforms’ audiences, and that this may affect the magnitude of spillover. Of the 26 platforms in our data set, 8 of them are in foreign languages, including the Chinese website Youku and the Turkish website VidiVodo. In addition, we consider whether niche platforms, which explicitly target either a specific demographic group or area of interest, have a different effect on spillover than do mass-market platforms such as YouTube or Vimeo. There are 14 such niche platforms in our data set, such as LiveLeak, which targets citizen journalism, and Spike, which focuses on television shows and clips. Finally, we consider whether humor-oriented (funny) platforms exhibit different spillover effects, because emotions such as humor can have a positive effect on sharing (Stieglitz and Dang-Xuan 2013). Our data set contains eight funny platforms, including eBaums World, StupidVideos, and Funny or Die.

## 4. Synthetic Control Methodology

Our goal is to estimate how multiplatform videos differ in their view growth as a result of their introduction onto a new platform. We therefore focus on view growth on the initial (lead) platform, because we are interested in the spillover in awareness generated by the video’s introduction onto the subsequent (lag) platform. Although Table 2 offers model-free evidence of positive spillover onto YouTube, this observational approach is insufficient for establishing causal inference. The limitations of observational data are due to endogeneity issues, on account of unobservable properties that may make a video both more popular and more likely to be introduced into multiple platforms. These endogeneity issues prevent us from ruling out reverse causality, that is, that a video’s popularity causes it to be introduced into more platforms. Separating the effect of the inherent popularity of the video from the effect of its introduction onto a new platform is thus our primary challenge in establishing causality.

Table 3. Summary of Diffusion Parameters

<table><tr><td></td><td>p</td><td>q</td><td>δ</td><td>m</td></tr><tr><td>Mean (SD)</td><td>0.002 (0.006)</td><td>0.054 (0.088)</td><td>0.826 (2.215)</td><td>1,110,680(5,776,315)</td></tr></table>

Although a common approach to remedying endogeneity is to conduct a randomized control experiment, employing this approach in the context of viral videos is extremely challenging. To conduct an experiment, we would need to monitor a large set of videos, of which very few would become viral. Moreover, these videos could be subjected to random treatments outside our control if other users uploaded these videos onto lag platforms. Although we present results from a small-scale experiment to support our findings in Section 5.4.4, conducting a large-scale experiment is not feasible with limited resources.

Recognizing the challenges of conducting a randomized control experiment, we introduce a novel, quasi-experimental method that seeks to address endogeneity concerns. Figure 5 presents an overview of this approach.

Whereas our quasi-experimental framework still views a video’s introduction onto a new platform as a treatment, our key challenge is in estimating an appropriate control. Ideally, this control should represent what would have happened to a multiplatform video had it not been introduced to an additiona platform. To approximate this counterfactual, prior work has constructed synthetic controls using items that are similar to those that are treated (Abadie and Gardeazabal 2003, Abadie et al. 2010). The method of synthetic control advocates that one can identify an “average treatment effect” in a quasi-experimental manner by comparing the performance of each treated item to that of a convex combination of similar, untreated items (Varian 2016). In our context, the similar items would include single-platform $( \mathrm { i . e . , }$ untreated) videos. Thus, for each introduction of a video into a new platform, we construct a synthetic control based on a combination of similar, untreated videos.

Following notation similar to that in Abadie et al. (2010), per Table 4, we use $Y _ { i j k } ^ { I } ( t )$ to denote cumulative views at time t of a multiplatform video i on platform j that is introduced onto platform k. Accordingly, $Y _ { i j k } ^ { N } ( t )$ represents the counterfactual associated with this intervention, that is, how many cumulative views at time t would video i have achieved in platform j had it not been introduced onto platform $k ?$ The treatment effect, $\alpha _ { i j k } ( t )$ , corresponding to the aforementioned scenario can thus be represented by the difference between the cumulative views of the treated video and its counterfactual, as follows:

$$
\alpha_ {i j k} (t) = Y _ {i j k} ^ {I} (t) - Y _ {i j k} ^ {N} (t).
$$

Although cumulative views of a treated video can be empirically observed, the associated counterfactual cannot. The synthetic control approach allows us to approximate such a counterfactual, using a weighted average of observations that are similar to the treated observations in all aspects apart from their treatment status. Per Abadie et al. (2010), we can accordingly represent the treatment effect as follows:

$$
\hat {\alpha} _ {i j k} (t) = Y _ {i j k} (t) - Y _ {i j k} ^ {N} (t) = Y _ {i j k} (t) - \sum_ {N _ {i j k}} \bigl (w _ {i j k} * Y _ {i} ^ {s} (t) \bigr).
$$

Here, $Y _ { i j k } ( t )$ is the observed cumulative view count at time t of a video i in platform j that is later introduced onto platform $k ,$ whereas $\backslash Y _ { i } ^ { s } ( t )$ represents an untreated (i.e., single-platform) video that is similar to the treated video. Additionally, $w _ { i j k }$ represents a weight assigned to the similar video, based on its degree of similarity to video i. These similar videos can then be combined into a weighted average to construct a synthetic control. A valid synthetic control should reasonably approximate the treated observation within the pretreatment time frame. Hence, if $t _ { i k }$ represents the timing of treatment (i.e., time at which video i is introduced onto lag platform k), the weights used to combine control units into a synthetic control should satisfy Equation (3):

$$
Y _ {i j k} (t) \approx \sum_ {j = 1} ^ {N _ {j}} \big (w _ {i j k} * Y _ {i} ^ {s} (t) \big), \forall t \leq t _ {i k}.\tag{3}
$$

Figure 5. Overview of the Synthetic Control Methodology  
![](/api/attachments/ZAUR8TA7/fulltext/images/22d0ffa0779ea21d4e1e3dfa884fe24aa7bd33a1be643702d2c221d50b6a2725.jpg)

Table 4. Codebook for Notation

<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $Y_{ijk}^{I}(t)$ </td><td>Cumulative views on day  $t$  in platform  $j$  of video  $i$  that was introduced into platforms  $j$  and  $k$ </td></tr><tr><td> $Y_{ijk}^{N}(t)$ </td><td>Cumulative views on day  $t$  of synthetic control corresponding to video  $i$  in platform  $j$  up until its entry into platform  $k$ </td></tr><tr><td> $Y_{i}^{s}(t)$ </td><td>Cumulative views on day  $t$  of single-platform video  $s$ </td></tr><tr><td> $v_{ij}$ </td><td>Video  $i$  in platform  $j$  (lead platform)</td></tr><tr><td> $v_{ijk}$ </td><td>Video  $i$  in platform  $j$  that was also introduced into platform  $k$ </td></tr><tr><td> $t_{ij}$ </td><td>Entry time of video  $i$  into platform  $j$ </td></tr><tr><td> $v_{ik}$ </td><td>Video  $i$  in platform  $k$  such that  $t_{ij} < t_{ik}$  (lag platform)</td></tr><tr><td> $v_{s}$ </td><td>Single-platform video  $s$ </td></tr><tr><td> $d_{ijks}$ </td><td>Cosine similarity between consumption pattern of video  $i$  in platform  $j$  to single-platform video  $s$ , up until  $t_{ik}$ </td></tr><tr><td> $w_{ijk}$ </td><td>Weight of control unit associated with entry of video  $i$  in platform  $j$  onto platform  $k$ </td></tr><tr><td> $delay_{ijk}$ </td><td> $t_{ik} - t_{ij}$ </td></tr><tr><td> $\Delta t$ </td><td>Number of days after the time of treatment,  $t_{ik}$ </td></tr><tr><td> $Foreign_{k}$ </td><td>Dummy variable, equals 1 if platform  $k$  is a foreign-language platform (0 otherwise)</td></tr><tr><td> $Niche_{k}$ </td><td>Dummy variable, equals 1 if platform  $k$  is a niche platform (0 otherwise)</td></tr><tr><td> $Funny_{k}$ </td><td>Dummy variable, equals 1 if platform  $k$  focuses on humorous content (0 otherwise)</td></tr><tr><td> $p_{ij}$ </td><td>NUI parameter  $p$  (coefficient of innovation / external influence) of  $v_{ij}$ </td></tr><tr><td> $q_{ij}$ </td><td>NUI parameter  $q$  (coefficient of imitation / internal influence) of  $v_{ij}$ </td></tr><tr><td> $\delta_{ij}$ </td><td>NUI parameter  $\delta$  (nonuniform influence factor) of  $v_{ij}$ </td></tr><tr><td> $m_{ij}$ </td><td>Cumulative number of views of  $v_{ij}$ </td></tr></table>

By strategically selecting weights that minimize pretreatment differences between treated and control units, we increase the likelihood that any systematic posttreatment differences between these observations are due to the treatment itself. Still, to compute these weights, we must decide on a metric with which we can estimate similarity between treated and untreated units. In addition to minimizing pretreatment differences between treated and control videos, this similarity metric must be based on factors that (1) are independent of treatment assignment and (2) verifiably predict future (i.e., posttreatment) outcomes for observations under study (O’Neill et al. 2016). In satisfying these criteria, weights of control units can be combined into a single synthetic control such that each control unit is weighted according to its similarity to the treated unit.

To satisfy the aforementioned matching criteria, prior quasi-experimental approaches have often used product characteristics as the basis for matching (e.g., Thomas 1985, Gatignon et al. 1989, Lenk and Rao 1990, Goldenberg et al. 2009). This approach can be likened to PSM, which similarly assumes that endogeneity between treated and untreated items can be minimized using observable characteristics. However, in our case, there is little assurance that the observable properties of a video (e.g., duration, channel subscribers) would accurately predict video consumption. This may be especially true for viral videos, as is intuitively demonstrated by the fact that even for a specific channel containing a relatively homogenous set of videos $( \mathrm { e . g . } ,$ McDonald’s), only some videos go viral. Hence, even videos that are similar in terms of inherent properties may exhibit heterogeneous outcomes. Consequently, matching based on these properties may not minimize endogeneity between treated and untreated videos. Matching videos based on observable properties via synthetic control or PSM may therefore not be an appropriate approach to estimating treatment effects. We must thus explore alternative similarity metrics that are better predictors of video consumption, while being independent of whether a video is introduced onto additional platforms.

To overcome the aforementioned challenges, our adaptation of synthetic control matches treated and untreated videos based on their observed consumption patterns; that is, for each video’s introduction onto a new platform, we construct a synthetic control using untreated (i.e., single-platform) videos that perform similarly up until the time of treatment. Specifically, our similarity metric is based on the cosine similarity of cumulative daily views between a treated video and potential control, from t = 0 until the time of treatment $( t _ { i k } )$ . Cosine similarity is a convenient and widely used metric for comparing the similarity between vectors (Tan et al. 2006) and is employed in popular matching algorithms such as collaborative filtering (Sarwar et al. 2001). We employ this metric to calculate the similarity d between each treated video and potential control video using Equation (4):

$$
d _ {i j k s} = \frac {\sum_ {t = 0} ^ {t _ {i k}} Y _ {i j k} ^ {I} (t) Y _ {i} ^ {s} (t)}{\sqrt {\sum_ {t = 0} ^ {t _ {i k}} Y _ {i j k} ^ {I} (t) ^ {2}} \cdot \sqrt {\sum_ {t = 0} ^ {t _ {i k}} Y _ {i} ^ {s} (t) ^ {2}}}.\tag{4}
$$

Using this similarity metric, we identify three single platform videos s with consumption patterns most similar to that of video i in platform j, up until its entry into platform k. To account for varying degrees of similarity between s and $v _ { i j } ,$ , we get the relative weight corresponding to s using Equation (5):

$$
w _ {i j k s} = \frac {d (v _ {s} ^ {n} , v _ {i j})}{\sum_ {n = 1} ^ {3} d (v _ {s} ^ {n} , v _ {i j})},\tag{5}
$$

where $v _ { s } ^ { n }$ refers to the single-platform video with the nth most similar consumption pattern to multiplatform video, and $Y _ { i , j , n } ^ { s } ( t )$ refers to the cumulative views of this video at time t. To obtain a synthetic control, we take the weighted average of each control unit at each time, per Equation (6):

$$
Y _ {i j k} ^ {N} (t) = \sum_ {n = 1} ^ {3} w _ {i j k s} \times Y _ {i, j, n} ^ {s} (t).\tag{6}
$$

Inherently, using cosine similarity will help identify videos with pretreatment trajectories similar to those of treated videos, satisfying Equation (3). Furthermore, because the past performance of videos has been shown to be a strong predictor of their future performance (Szabo and Huberman 2010, Pinto et al. 2013), this metric also minimizes endogenous pretreatment differences between treated and control videos, which helps to isolate the effect of the treatment itself. Moreover, matching treated videos with controls that show similar consumption ameliorates the most salient threat to random assignment, namely, that videos are introduced onto additional platforms because they are consumed more. Thus, we can argue that estimating similarity based on pretreatment consumption patterns minimizes the main threats to identification.

Whereas prior studies often rely on few counterfactuals for their synthetic control because of limited data, our approach leverages a comparably large set of 349 controls to algorithmically select the most similar controls using the aforementioned method. This helps us select controls that have high similarity to treated videos, thus effectively minimizing endogeneity between treated and control pairs.

To illustrate our synthetic control approach, Figure 6 depicts the diffusion of a treated video, along with its corresponding synthetic control. The treated video was initially uploaded onto YouTube by Calvin Klein. It was also uploaded onto Dailymotion by an independent user on day 36, marked by the vertical line. Overall, the synthetic control closely matches the consumption of the treated video in the pretreatment period. However, only the treated video exhibits a boost in its trajectory after day 36, suggesting a potential positive spillover onto YouTube based on its introduction onto Dailymotion. Per Table 5, we find similar relative behavior between treated and control videos overall.

Figure 6. (Color online) Example of Cumulative Views of the Treatment Video vs. Synthetic Control  
![](/api/attachments/ZAUR8TA7/fulltext/images/731d1253909c326bd69e88779bf24fe09d7cf97fde5914f22c301b4f01a630c0.jpg)

To empirically validate our approach to obtaining synthetic controls, we make five observations about the resulting treatment–control pairs in the pretreatment period. First, we find that consumption patterns of treated videos and synthetic controls have an average similarity of 0.992 (SD = 0.004, min = 0.974, max = 0.999). This confirms that the controls obtained using Equations (4)–(6) consistently exhibit consumption patterns that are similar to those of the treated video, prior to the time of treatment. Second, we confirm that cumulative view count achieved at the time of treatment by a control is very close to that of its corresponding treated video; the average ratio of views achieved by a synthetic control to those of its corresponding treated video at the time of treatment is 1.014 (min = 0.876, max = 1.077). This suggests that it is unlikely that there are different pretreatment trends between treated and control videos that would bias our estimation of treatment effect. Third, we observe that each of the three control videos is a reasonable representation of the pretreatment consumption trend of the treated video, as demonstrated by their similar weights used in the synthetic control construction, shown in Table 6. Fourth, we find that the distribution of the log of cumulative views at the time of treatment is very similar between treatment and control videos, with a paired t-test showing no significant differences between these distributions. Finally, we observe that of the 349 potential controls, 264 are selected for use. Among these controls, none is employed more than 20 times. Thus, we do not expect that our analysis will be biased by any particular control video.

## 4.1. Lift

To measure treatment effect in a systematic way, we would like to compare the average increase in views of the treated video to that of the control, after the intervention occurs. Although the existing synthetic control approach may consider an increase in views in terms of raw view count (Abadie et al. 2010), we consider this increase in terms of view growth percentage. We do so because growth percentage is less sensitive to market saturation and consumption potential of the video within the platform. For any given day after treatment, we can measure view growth on both the treated and control videos as the ratio of cumulative views on this day to those on the day of treatment. If we then compare the view growth percentage of the treated video to that of the control as a ratio, we can estimate the lift of video i in lead platform j at time window <sup>Δ</sup>t created by introducing video i onto lag platform k using Equation (7):

Table 5. Comparison of Treatment and Control Videos

<table><tr><td></td><td>Average cumulative views (at time of treatment)</td><td>Average cumulative views (20 days after treatment)</td></tr><tr><td>Treated video</td><td>1,468,194(SD = 4,967,133)</td><td>2,726,436(SD = 4,974,143)</td></tr><tr><td>Control videos</td><td>1,474,980(SD = 4,764,194)</td><td>1,936,901(SD = 4,780,291)</td></tr><tr><td>Synthetic control videos (i.e., weighted average of controls)</td><td>1,476,499(SD = 4,944,312)</td><td>1,940,119(SD = 4,944,312)</td></tr></table>

$$
L i f t _ {i, j, k} (\varDelta t) = \frac {Y _ {i j k} ^ {I} (t _ {i k} + \varDelta t) \Big / Y _ {i j k} ^ {I} (t _ {i k}) - 1}{Y _ {i j k} ^ {N} (t _ {i k} + \varDelta t) \Big / Y _ {i j k} ^ {N} (t _ {i k}) - 1}.\tag{7}
$$

Our lift metric represents the ratio of view growth percentage in the treated video to that of the control. We therefore interpret lift as the factor by which a video’s introduction into a new platform increases its subsequent growth percentage on an initial platform. For example, a lift of two would suggest that, after a video’s introduction onto a new platform, the video grew in the initial platform twice as much as it would have otherwise. This quasi-experimental approach allows us to observe lift at any given time window $\Delta t ,$ and thus understand how spillover evolves over time. We thus exploit the advantages of the synthetic control approach to conveniently estimate a stochastic treatment effect (O’Neill et al. 2016, Tirunillai and Tellis 2017).

To achieve clean empirical identification of the treatment effect, several assumptions need to be met. Most importantly, we need to justify the unconfoundedness assumption, which requires that all factors correlated with both with a video’s performance and its treatment assignment are observed (Athey and Imbens 2017). The presence of unobserved “confounding factors” that are correlated with both treatment video selection and treatment outcome could raise concerns over whether the treatment effect is caused by these factors or by the treatment itself. Quasi-experimental methods are indeed prone to biased treatment selection, because we do not assign treatments ourselves. To validate a quasi experiment, we must therefore assess whether the conditions of treatment assignment are approximately random (DiNardo 2008).

Table 6. Weights of Control Videos

<table><tr><td></td><td>Average weight (SD)</td></tr><tr><td>Control video 1</td><td>0.335 (0.006)</td></tr><tr><td>Control video 2</td><td>0.333 (0.002)</td></tr><tr><td>Control video 3</td><td>0.332 (0.004)</td></tr></table>

Perhaps the most intuitive confounding factor in our context would be that a video is introduced onto a new platform because of its popularity, and thus cannot be considered a random treatment assignment. However, our method explicitly accounts for this threat by matching treated videos with control videos that are similar in popularity. We therefore minimize the likelihood that a video was treated because of its consumption level. Because initial performance of digital media is shown to be a strong predictor of its future performance (Szabo and Huberman 2010, Pinto et al. 2013), one can argue that a video’s diffusion up until the time of treatment implicitly captures the inherent properties of the video that would affect its future popularity. Hence, as discussed previously, matching treated and control videos based on their consumption patterns can be considered a robust approach that minimizes the threat of confounders.

The likelihood of random treatment assignment is further improved by the decentralization of control over video treatment; that is, no single agent controls what videos are introduced into a specific platform. Furthermore, based on our observation of individuals uploading content onto new platforms, we found these individuals to be distinct and to have had no affiliation with any of the firms associated with the videos. Thus, the likelihood of strategic seeding can be considered minimal. The fact that video uploads are user driven additionally diminishes the likelihood of firms taking strategic action (e.g., increasing advertising) around the time of a video’s upload onto a new platform. Thus, we can argue that there is ample evidence against the key threats to confoundedness and random assignment. Furthermore, the decentralized control over treatment permits us to assume approximate randomness in the treatment timing, allowing us to estimate the effect of this timing.

## 5. Empirical Models and Results 5.1. Estimating Lift

Using the methodology outlined in Section 4, we proceed to take the average lift for lead–lag platform combinations across all multiplatform videos. We do this by observing average lift over the first 100 days after treatment (i.e., for values of <sup>Δ</sup>t between 1 and 100). In observing these 289 spillovers, we find that several lead–lag platform combinations generate spillovers that are far larger than others, and can thus be considered outliers. These outliers occur because of minimal posttreatment growth in the control videos, making the denominator of the lift formula in Equation (7) close to zero. To prevent these outliers from inflating our lift estimates, we remove them from our main analysis. A visual inspection of lift estimates on day 50 reveals a natural cutoff between spillovers above and below 40. Thus, we remove 14 spillovers above this threshold (ranging from 51 to 13,394) and continue our analysis using the remaining 275 spillovers (ranging from 0.002 to 32).

Based on the remaining 275 spillovers, a plot of the average treatment effect and its confidence interval for each day after treatment can be seen in Figure 7. To verify the robustness of these estimates and to observe a trend line for lift, we perform a bootstrap procedure (Efron and Tibshirani 1993) using 500 random subsamples of 250 lead–lag platform combinations. The horizontal line at Lift = 1 denotes the cutoff for statistical significance, because a lift of one implies that the treated video grew exactly as much as the control.

The above figures suggest a spillover that is positive and significant for all time intervals. Hence, we find that introducing a video onto a new platform increases its consumption in the initial platform. The long–run estimate for lift is around 2, suggesting that after a video is introduced onto a new platform, its consumption on the initial platform will be approximately twice what it would have been otherwise.

In addition to its positive valence, the shape of lift is worth remarking on. We find that, on average, spillover is strongest immediately after the video’s introduction onto the lag platform. The dynamic effects of cross-platform spillover thus differ somewhat from the typically observed effects of traditional (i.e., offline) marketing interventions, which often experience a “wear-in” time, representing a lag between the timing of the intervention and its benefits (Tirunillai and Tellis 2017). This immediate spillover effect may be due to the rapid WOM facilitated by the internet. However, as with other interventions, spillovers across platforms exhibit a slow, downward trend in their benefits, offering evidence of a “wear-out” effect. Still, unlike some other interventions, the benefits of cross-platform spillover persist in the long run.

In terms of shape, it is also noteworthy that spillover exhibits two peaks, on days 18 and 42, generating lifts of 2.76 and 2.51, respectively. These sharp peaks suggest that, as with numerous other phenomena related to human dynamics, cross-platform spillover may exhibit burstiness (Crovella and Bestavros 1997, Barabasi´ 2005), or sudden increases within short time spans. These bursts of spillover may be explained by “threshold models” of behavior (Granovetter 1978, p. 1422), a phenomenon by which individuals tend to wait until a threshold is reached before taking an action. This may suggest that after a threshold of WOM about a video is reached, many more individuals will begin to consume and spread awareness of the video.<sup>8</sup>

5.2. Effect of Lag Platform Characteristics on Lift We estimate several empirical models to examine the role of platform-level factors in generating spillover. These models consider the diffusion patterns of video views within platforms, characteristics of platforms, and the timing of entry onto these platforms.

We first consider the effect of the diffusion pattern of a video in a lag platform on views in the lead platform. These diffusion patterns are characterized by NUI parameter estimates associated with the lag platform. To assess the effect of each NUI parameter on the magnitude of spillover, we regress these parameters on lift. Because the timing may affect the magnitude of the spillover as well, we control for the delay in introducing a video into the lag platform. We consider the possibility that a larger delay in entry affects lift in either a linear or quadratic manner; that is, its effect may either strictly increase/decrease lift over time or it may increase/decrease lift up to a point but decrease/increase it thereafter. We observe that the model that incorporates a quadratic effect for this delay has an Akaike information criterion (AIC) value lower than that of the model with only a linear effect, suggesting that incorporating the quadratic effect is appropriate. Finally, we consider how different types of platforms may create different spillovers. To this end, we include dummy variables for the foreign, niche, and funny platforms in our data set. We thus formulate our main model as follows:

Figure 7. (Color online) Average Lift Across All Lead–Lag Platform Pairs over Time  
![](/api/attachments/ZAUR8TA7/fulltext/images/25a42f985ca4ef5df2dbeccb2446c9ea3e516356082425bb87fcc4272d3fe1f8.jpg)  
Note. Conf. int., confidence interval.

![](/api/attachments/ZAUR8TA7/fulltext/images/0cb1f882f99d5431a2f29bf4d2c2920b8f1144b83c3ba806506c8a2f85f179da.jpg)

$$
\begin{array}{r} L i f t _ {i j k} (\Delta t) = \beta_ {0} + \beta_ {1} p _ {i k} + \beta_ {2} q _ {i k} + \beta_ {3} \delta_ {i k} + \beta_ {4} \log (m _ {i k}) \\ + \beta_ {5} d e l a y _ {i j k} + \beta_ {6} d e l a y _ {i j k} ^ {2} + \beta_ {7} F o r e i g n _ {k} \\ + \beta_ {8} N i c h e _ {k} + \beta_ {9} F u n n y _ {k} + \varepsilon . \end{array}
$$

To observe the effects of the aforementioned factors over time, we observe parameter estimates at time windows of 5, 25, and 50 days in Table 7. Appendix A provides more detail on the range of time windows in which parameter estimates are significant.

We can infer from the significant, negative relationship between NUI parameter δ and lift that platforms that achieve an early peak in WOM generate stronger spillover. This finding would support the argument that positive social signals, reflected in a higher view count for a video, may amplify the effects of WOM (Aral and Walker 2011, Bapna and Umyarov 2015); that is, videos with more views may be more likely to generate buzz than videos with fewer views (Fu and Sim 2011). Consequently, videos that generate buzz early will reap more immediate benefits of the positive social signals associated with higher view count, and thus generate more WOM across platforms. It is interesting that this effect holds in the medium and long run only, because it suggests that a strong, early WOM within the lag platform has benefits down the line. One might interpret this as a lag between the spread of WOM across platforms and users’ actual consumption of the video within the lead platform. Meanwhile, parameters p and q are insignificant, offering no evidence that either external advertising or, more surprisingly, the overall effect of WOM in the lag platform generate spillover onto the lead platform.<sup>9</sup> Although these factors may still promote the video’s overall adoption, they do not seem to affect cross-platform spillover.

Table 7. Model Estimations over Time Windows of 5, 25, and 50 days

<table><tr><td rowspan="2"></td><td colspan="3"> $\Delta t =$ </td></tr><tr><td>5 (short term)</td><td>25 (medium term)</td><td>50 (long term)</td></tr><tr><td> $p$ </td><td>-15.69 (17.09)</td><td>-9.34 (19.61)</td><td>-14.46 (20.73)</td></tr><tr><td> $q$ </td><td>-1.35 (1.24)</td><td>-1.52 (1.36)</td><td>-0.91 (1.44)</td></tr><tr><td> $\delta$ </td><td>-0.10 (0.07)</td><td>-0.18 (0.08)**</td><td>-0.14 (0.09)*</td></tr><tr><td> $\log(m)$ </td><td>0.53 (0.16)**</td><td>0.61 (0.30)**</td><td>0.57 (0.31)*</td></tr><tr><td> $delay$ </td><td>0.03 (0.009)***</td><td>0.03 (0.009)***</td><td>0.04 (0.009)***</td></tr><tr><td> $delay^{2}$ </td><td>-0.00006(0.00002)**</td><td>-0.00006(0.00003)**</td><td>-0.00007(0.00003)***</td></tr><tr><td>Foreign</td><td>0.46 (0.034)</td><td>0.96 (0.37)***</td><td>1.10 (0.38)***</td></tr><tr><td>Niche</td><td>0.22 (0.03)</td><td>-0.004 (0.37)</td><td>-0.10 (0.38)</td></tr><tr><td>Funny</td><td>-0.26 (0.33)</td><td>-0.04 (0.37)</td><td>0.15 (0.38)</td></tr><tr><td> $R^{2}$ </td><td>0.17</td><td>0.17</td><td>0.14</td></tr><tr><td>AIC</td><td>990.62</td><td>1119.63</td><td>1150.00</td></tr></table>

\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Model estimations also suggest spillover is stronger in the medium and long term when market size is greater in the lag platform. This suggests that spillover onto the lead platform is larger when there are more consumers of the content in the lag platform. Specifically, a 100% increase in consumption in the lag platform is associated with an approximate 0.5 unit increase in lift. Additionally, we find that delay has a concave effect on lift; that is, delaying the introduction of a video onto a new platform increases spillover, but delaying too long can be detrimental.

We find that foreign lag platforms tend to generate an approximately one unit marginal increase in spillover. It is reasonable to infer that foreign platforms will generate stronger spillover, given prior findings on positive spillovers across countries (Putsis et al. 1997). Furthermore, foreign platforms may have more distinct audiences from those of the focal platform, suggesting that introducing a video onto a new platform reaches untapped consumers. As more new consumers are exposed to a video, more WOM may be generated, thereby increasing consumption in the lead platform as well.

## 5.3. Effect of Multiple Lag Platforms on Lift

Because firms must invest time and effort into posting content onto a new platform (e.g., creating an account), it may be useful to know whether videos will continue to benefit from positive spillovers as they are introduced onto more platforms. We therefore consider how the order of entry of lag platforms affects lift. Perhaps the lift created by introducing a video onto additional platforms will wear out over time as the video’s market potential saturates, and the spillovers may exhibit diminishing returns. Alternatively, incorporating a video onto additional platforms may create a snowball effect, so that lift increases with each new platform. To observe whether either of these phenomena exists, we estimate the following model:

$$
\begin{array}{r} L i f t _ {i j k} (\Delta t) = \beta_ {0} + \beta_ {1} p _ {i k} + \beta_ {2} q _ {i k} + \beta_ {3} \delta_ {i k} + \beta_ {4} \log (m _ {i k}) \\ + \beta_ {5} d e l a y _ {i j k} + \beta_ {6} d e l a y _ {i j k} ^ {2} + \beta_ {7} N _ {i k} + \varepsilon , \end{array}
$$

where $N _ { i k }$ is the order of introduction of platform k for video i. For example, if platform k is the third platform onto which video i is introduced, then ${ N _ { i k } } ^ { \mathbf { \hat { \alpha } } } = 3 .$ . Observing the negative and statistically significant parameter estimates for this model in Table 8, we find that introducing a video onto subsequent lag platforms has diminishing returns on lift over all time windows.

To gain insight into what a good number of lag platforms would be, we observe average lift across all lead–lag platform combinations conditional on $n \geq h$ for all values of d between 1 and 10 (the maximum number of lag platforms for a single video in our data set). In Figure B.1 in Appendix B, we show that, starting at $h = 5$ , we no longer observe significant lift for most time windows. We therefore do not have evidence to suggest lift will persist for the fifth lag platform and beyond.

## 5.4. Robustness Checks

To evaluate the robustness of our main findings, we observe whether spillover remains positive in key situations. Because a motivation for our paper is creating spillovers onto a focal platform, we observe lift only for cases in which YouTube is the lead platform. Per Figure $^ { 8 , }$ we confirm that spillovers created onto YouTube are similar to our overall results.

5.4.1. Cutoff for Virality. Although we constrain the boundaries of our study to viral videos, it is unclear how many views a video must achieve to be considered viral. Although our cutoff of 100,000 cumulative views allowed us to increase the amount of data we could use for analysis, we could conceivably impose stricter conditions on data selection.<sup>10</sup> To ensure that our lift estimates are not biased by the data selection process, we estimate lift using thresholds of 500,000, 1 million, and 2 million views, as shown in Figure 9. Although the resulting estimates rely on fewer observations, they show shape and magnitude similar to those of our main estimates.

5.4.2. Synthetic Control Composition. The synthetic control methodology requires us to select a fixed number of control units for use in synthetic contro composition; we chose three. Note that there is a trade-off between selecting more versus fewer videos for synthetic control: whereas selecting more videos may provide a less noisy control, selecting fewer videos yields controls that are more similar to the treated videos. To assess the sensitivity of our analysis to varying numbers of control units, we estimate lift using two, four, and five single-platform videos, with resulting estimates shown in Figure 10. Thes estimates are similar in shape and magnitude to our main results, indicating that our findings are not biased by our choice of three control units.

5.4.3. Falsi<sup>fi</sup>cation Test. To ensure that spillover estimates were not biased by our methodology or metrics, we conducted a falsification test in which we applied fake treatments to single-platform videos at random times. We then estimated lift corresponding to videos with fake treatments compared with their synthetic controls, per Equations (4)–(7). As shown in Figure 11, we found that these fake treatments yielded no significant results, in line with expectation. Furthermore, lift associated with these fake treatments is close to one, suggesting that videos with fake treatments showed view growth similar to that of their synthetic controls. This suggests that our method and measures are not biased toward showing significant or positive spillover.

5.4.4. Small-Scale Field Experiment. To support our quasi-experimental results, we conducted a smallscale field experiment over two months using 46 viral videos. Whereas our prior checks help validate the empirical robustness of our estimates, the experiment was designed to alleviate remaining concerns over random treatment selection and endogeneity. To conduct this experiment, we identified a set of early-stage viral YouTube videos, uploaded a random subset of them onto Vimeo with randomized timing, and compared subsequent view growth on YouTube of these two sets of videos. We provide an overview of our experimental approach in Figure 12.

Table 8. Diminishing Returns on Lift of Nth Lag Platform Introduction

<table><tr><td rowspan="2"></td><td colspan="3"> $\Delta t =$ </td></tr><tr><td>5 (short term)</td><td>25 (medium term)</td><td>50 (long term)</td></tr><tr><td>P</td><td>-23.61 (88.33)</td><td>-13.16 (58.64)</td><td>-23.84 (68.72)</td></tr><tr><td>Q</td><td>-3.76 (6.16)</td><td>-3.82 (3.92)</td><td>-1.58 (4.59)</td></tr><tr><td>δ</td><td>-0.62 (0.39)</td><td>-0.61 (0.25)**</td><td>-0.53 (0.29)*</td></tr><tr><td>log(m)</td><td>0.17 (0.22)</td><td>0.08 (0.14)</td><td>0.15 (0.17)</td></tr><tr><td>delay</td><td>0.004 (0.002)*</td><td>0.004 (0.002)*</td><td>0.007 (0.003)**</td></tr><tr><td> $delay^2$ </td><td>-0.00006 (0.00002)***</td><td>-0.00006 (0.00002)***</td><td>-0.00007 (0.00002)***</td></tr><tr><td>N</td><td>-0.01 (0.002)***</td><td>-0.009 (0.002)***</td><td>-0.009 (0.002)***</td></tr><tr><td> $R^2$ </td><td>0.10</td><td>0.12</td><td>0.09</td></tr><tr><td>AIC</td><td>1858.18</td><td>1734.74</td><td>1821.66</td></tr></table>

\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.00

Figure 8. (Color online) Spillover onto YouTube (n = 82)  
![](/api/attachments/ZAUR8TA7/fulltext/images/39ed944199f63d892d8e715f125c678c4af3ceb97ed2d682947dec5c600857b1.jpg)  
Note. Conf. int., confidence interval.

A key challenge in conducting a field experiment with viral videos is identifying such videos in their early stages. To identify these videos, we monitored channels that were likely to contain viral videos and flagged videos as being viral if they achieved more than 100,000 cumulative views within three days of being uploaded. To find appropriate channels for this data collection process, we identified channels that were associated with YouTube trending videos for a four-week period in 2018. Because the trending videos were already in the mature stages of their virality, we did not consider these videos in our experiment; however, we did assume that future videos from these channels may be likely to go viral as well. Using the 313 channels we identified, we used the YouTube application programming interface to collect daily view counts of all new videos from these channels. From the 645 total videos identified from these channels, we selected 46 videos that met our cutoff of 100,000 cumulative views within three days. These videos came from a variety of popular channels, including those of Fortune 500 firms such as United and Apple, talks shows such as The Tonight Show Starring Jimmy Fallon, and informational channels including TED and Vox.

To estimate spillovers associated with introducing videos onto a new platform, we randomly selected 19 of these videos and uploaded them onto Vimeo. To ensure that spillover estimates were robust to variations in timing of a video’s entry into the lag platform, we used a random number generator to select a delay between 3 and 30 days and uploaded our videos onto Vimeo on the selected day. Resulting delays ranged between 3 and 29, with a mean of 15.84 (SD = 8.38). From the remaining 27 videos, we selected 19 videos that were most similar to the treated videos based on their consumption patterns using Equations (4)–(6) Because of the limited data set, we picked only one control video to estimate the cross-platform spillover effect from this experiment.

To evaluate robustness, we make several observa tions about these treatment–control pairs to ensure the validity of our experiment. First, we find that cosine similarities of consumption patterns for treatment– control pairs have a mean of 0.973 (SD = 0.010, min = 0.948, max = 0.998). Thus, despite a smaller sample size, we are able to obtain controls that still reflect pretreatment consumption patterns of the treated videos. Second, we observe that the average ratio of views achieved by control videos to that of treated videos at the time of treatment is 0.992 (min = 0.888, max = 1.100), suggesting no significant pretreatment trends that could bias our lift estimates. Third, we find that the distributions of initial views of treated and control videos are similar, as shown in Figure 13. A Kolmogorov–Smirnov test offers no evidence that these distributions are different $( p = 0 . 3 6 )$ . Fourth, we were unable to find the treated videos on other prominent video platforms $( \mathrm { e . g . , }$ Dailymotion, MetaCafe), suggesting that it is unlikely that there are other spillovers that could bias our lift estimates.

Figure 9. (Color online) Lift Estimates by Minimum View Count Cutoff  
![](/api/attachments/ZAUR8TA7/fulltext/images/19bce163aff820b75af0177a49e9e24c726b8d9df0f2beeeae7a55cf0c34ccd3.jpg)  
Note. Conf. int., confidence interval.

![](/api/attachments/ZAUR8TA7/fulltext/images/ebe3eb473ec2567920214c08271518e1a7a67419e76b831c7f49b8ea1195b377.jpg)

![](/api/attachments/ZAUR8TA7/fulltext/images/eadb614715f5f7f37cdbdf33cceecccf9955f70ebd199780efb85d95d1c44381.jpg)

Figure 10. (Color online) Lift Estimates by Number of Single-Platform Videos Used in the Synthetic Control  
![](/api/attachments/ZAUR8TA7/fulltext/images/49ad8cda495bf14451fdb0b28b561c3bc47b97c4f73293a2d8b60be0df065ac3.jpg)  
Note. Conf. int., confidence interval.

![](/api/attachments/ZAUR8TA7/fulltext/images/88aaf15aeb0ed551db01a70ccf987983bb2d4ee0959d4657aed1dc6f9c8a2320.jpg)

![](/api/attachments/ZAUR8TA7/fulltext/images/6b2bc0f50d85bd5b13736c1fa9ea18c081cf2d7d9eb5bc68850962c8919ef40f.jpg)

Having assessed the validity of our field experiment, we proceed to estimate spillovers associated with each treatment–control video pair over time. We find that the magnitude and shape of these spillovers closely mirror those we observed in our main analysis, supporting the robustness of these findings as well as our synthetic control methodology. We should note, however, that because our field experiment has notably fewer spillovers (19) compared with our main analysis (275), the standard errors associated with these lift estimates may be less reliable and robust.

Figure 11. (Color online) Falsification Test  
![](/api/attachments/ZAUR8TA7/fulltext/images/55422bce56d5f75ff232761d5f2abd2d5be9a7d7434af2939a8bc8ac9cddfe0a.jpg)  
Note. Conf. int., confidence interval.

Still, we find that spillover is positive for all time windows, and significant for most windows as well as shown in Figure 14.

To supplement the aforementioned findings, we estimated lift for the same set of 19 treated videos by pairing them with a synthetic control using singleplatform videos from our original data set. The synthetic control was constructed using a weighted av erage of consumption patterns of three single-platform videos, per Equations (4)–(6). Using this approach, we again find high pretreatment cosine similarities in consumption patterns between treated and control videos (mean = 0.994, SD = 0.003, min = 0.990, max = 0.999). Furthermore, we observe no significant difference in pretreatment trends, given the average ratio of cumulative views of control to treatment of 0.993 $( \mathrm { m i n } = 0 . 9 8 2$ , max = 1.019). Finally, we find no notable differences in consumption potential between treated and untreated videos, given that the distribution of day 1 views between these sets of videos showed no statistically significant differences, per a Kolmogorov–Smirnov test $( p = 0 . 4 1 )$ ). The magnitude of our resulting lift estimates in Figure 15 closely resembles those of our prior analyses. Again, because of the small scale of this experiment, standard errors may not be as reliable as those of our original lift estimates. Still, these results appear to support our finding of positive cross-platform spillover and suggest no bias due to the single-platform videos used in our main analysis.

## 6. Discussion

The methodology and findings introduced in this study have implications for platforms, firms, and copyright policy. Our main finding is that there appears to be a positive, persistent, and bursty crossplatform spillover in the consumption of viral videos. Consistent with previous studies $( \mathrm { e . g . }$ , Putsis et al. 1997), we expect the catalyst behind these spillovers to be WOM between individuals across these platforms. We can infer from this positive spillover that digital platforms cater to different audiences, as has been suggested about physical and digital versions of goods. Thus, in creating these positive spillovers, digital platforms have the potential to increase the market potential of viral content, rather than fragmenting its consumption across platforms.

Figure 12. Overview of the Field Experiment Approach  
![](/api/attachments/ZAUR8TA7/fulltext/images/669039ecf58a64785ab77c30ad156bdec0275f705c004e35b424391b148c9eb7.jpg)

A positive cross-platform spillover has strategic implications for platforms, such as YouTube. Our result suggests that platforms may reinforce each other’s usage, rather than cannibalize each other. In some ways, this contradicts the “winner takes all” hypothesis commonly associated with internet platforms, and supports the counterargument that this hypothesis ignores the value of interactions among platform users (Lee et al. 2006). Thus, a positive crossplatform spillover effect would suggest that YouTube videos might actually have gained views in the presence of competing platforms. Our results also suggest that releasing a video on foreign-language platforms can create stronger spillover onto a dominant platform like YouTube. This result suggests potential opportunities for new platforms with local emphasis.

In addition to their implications for platforms, our results also have clear ramifications for marketers and content creators. Primarily, our results suggest that it is beneficial to upload videos onto multiple platforms, rather than focusing only on the marketleading platform (e.g., YouTube). Although our data show that most videos are introduced onto YouTube only, our results suggest that this may not be the best practice. These findings support the need for multichannel marketing, encouraging firms to develop their presence on a broad set of platforms (e.g., Instagram, Snapchat, Pinterest).

Figure 13. Distribution of Initial Views of Treated and Control Videos (Experiment)  
![](/api/attachments/ZAUR8TA7/fulltext/images/1e65f3de53f8f6012709027c2ca9a0385d95ad320ba1e8a825a9e34884edb931.jpg)

In addition to the diffusion pattern of the video in the lag platform, the timing of entry onto these lag platforms may affect spillover. The concave effect of delaying a video’s entry onto a new platform suggests that a waterfall strategy produces stronger spillover. However, the optimal timing of seeding so as to maximize overall adoption remains in question. To offer insights on this issue, we can look to literature on viral marketing, which emphasizes the importance of creating “information cascades” (Cheng et al. 2014, p. 2). These cascades refer to waves by which many in dividuals make the same decision in short succession because of social influence—in this case, influencing each other to consume a piece of content, either by direct sharing or WOM. Viral marketing strategies can capitalize on these cascades by using timely efforts that generate additional buzz while WOM is spreading rapidly. Because spillovers are bursty, the effectiveness of introducing a video into a new platform may indeed be sensitive to timing. However, by seeding a video into a new platform during one of these bursts, marketers may be able to build stronger cascades to generate greater boosts in awareness of their content. Our results would thus advocate that marketers take advantage of the strong initial spillover by introducing videos onto multiple platforms in short succession. Alternatively, marketers can exploit later bursts by detecting them and introducing videos onto new platforms during these periods.

Figure 14. (Color online) Average Lift in the Small-Scale Field Experiment  
![](/api/attachments/ZAUR8TA7/fulltext/images/4f289e2ee7e9d7dc6f61f291f38c211c6ec53c53d4cc7ca35597f95227ab6060.jpg)  
Note. Conf. int., confidence interval.

Figure 15. (Color online) Average Lift in the Experiment (with Original Single-Platform Videos as Controls)  
![](/api/attachments/ZAUR8TA7/fulltext/images/04c98da63353a23f23ba9697b4922842c7580bb93a39786507b66693a75bb2ca.jpg)  
Note. Conf. int., confidence interval.

Our finding that foreign-language platforms create stronger spillover suggests directions for further research on the role of network structure in crossmarket spillover. We believe that foreign platforms create stronger spillovers because of their relatively nonoverlapping user bases. Because these platforms may contain a larger number of users who were not reached previously though other platforms, introducing a video to a foreign platform may create a larger boost in awareness and cross-platform WOM. Although there is little research on the role of network overlap in information diffusion, extant research demonstrates the importance of network structure on the diffusion of information (e.g., Bampo et al. 2008, Yoganarasimhan 2012). By extension, structural relationships between networks may also affect the diffusion of content across these networks. We hope that a future extension of this work will help explain our finding on foreign-language platforms in more detail.

Our finding of diminishing returns on spillover with the addition of more platforms suggests that firms should not expect to keep producing a spillover by endlessly introducing their content onto additional platforms. Thus, although introducing a viral video onto new platforms may expand its market potential, this potential remains finite. Our analyses suggest that firms can benefit from spillover by introducing their content on up to five lag platforms. Furthermore, firms should seed content onto larger platforms earlier, because a greater spillover is more meaningful to a platform with a larger user base.

Our findings may also offer new perspectives on copyright infringement concerns caused by the copying and uploading of an original video onto new platforms by unaffiliated individuals. Both platforms and content owners (firms) have taken actions to remove these videos from the new platforms under the assumption that user-uploaded videos on other platforms will cannibalize views on the firm’s official channel. However, our analyses suggest that rather than being concerned about individual users uploading original videos onto new platforms, firms should proactively seed their content into numerous platforms. In doing so, firms can reap the benefits both of gaining views on their official channel and of positive spillovers from different platforms.

Our findings may be generalizable to other forms of digital media, such as photos, as well as other platforms, such as Facebook, Twitter, or Reddit. For example, marketers and content creators may consider seeding an infographic onto different platforms in a manner similar to that which we propose for videos. Future work can consider employing the synthetic control methodology characterized by Equations (4)–(6) and our lift metric in Equation (7) to study spillover effects for other forms of content across other platforms.

## 6.1. Limitations and Suggestions for Future Research

Some limitations of our study concern the size and scope of our data, which are common challenges in research on viral content. Having data that included more multiplatform videos and more diversity of content (because all videos are from major consumer brands) would be desirable to explore the role of video-level characteristics in creating spillover. Still, even with limited data, we examine a substantial 275 spillovers, which constitute our unit of analysis in all our findings. Future research can build on these findings using a larger data set by combining our quasi-experimental methodology with a hierarchical model, which could consider spillovers and product level characteristics simultaneously.

In addition, our data do not include information about firms’ marketing activities, which could be considered endogenous factors that bias consumption. However, we would argue that these factors are less relevant in our context for three reasons. First, because our videos correspond to large consumer brands, the intensity of marketing is likely to be consistently strong at all times. This reduces the chance of time-specific shocks in advertising that might coincide with a video’s treatment. Second, because virality is heavily driven by user-generated WOM (Ferguson 2008, Aral and Walker 2011), the role of advertising interventions is likely diminished compared with other contexts. Third, we can consider these shocks to be randomly distributed across treated and untreated videos, thus making a video’s treatment a more likely cause of systematic differences in outcome.

Lack of insight into video-level effects may also raise concerns over the generalizability of our findings to other types of digital media. We believe these findings do likely apply to other media targeting a mass audience, because this is the case for videos in our data set. Although the magnitude of spillover may differ in other contexts because of factors such as consumption costs of content and network structure within platforms, we remain confident of the positive valence of cross-platform spillover as well as the directionality of our other results. We look forward to future work that leverages our quasi-experimental methodology to explore cross-platform spillovers of different forms of media across different platforms.

## Acknowledgments

The authors dedicate this work to the memory of Frenkel ter Hofstede, who was instrumental in this paper’s initiation and development. His intelligence, dedication, and humor are greatly missed.

The authors would also like to thank the participants of the 2017 Marketing Science conference, the 2018 Conference on Statistical Challenges in e-Commerce Research (SCECR), the 2018 Conference of Information Systems and Technology (CIST), and the 2018 International Conference of Information Systems (ICIS). In addition, they would like to acknowledge the feedback and support from Alok Gupta, Gerard Tellis, Rahul Telang, Stathis Tompaidis, and Ioannis Stamatopoulos. They also appreciate the feedback and suggestions for improvement received from the senior editor Ravi Bapna, associate editor Sunil Wattal, and three anonymous reviewers with Information Systems Research. They are thankful for the feedback provided by the attendees of their seminar presentation at the McCombs School of Business. This collection of feedback has helped them improve the rigor and quality of this research.

## Appendix A. Details on the Signi<sup>fi</sup>cance of Parameter Estimates: Range of Time Windows for Which Parameter Estimates Are Signi<sup>fi</sup>cant (<sup>p</sup> < 0.1)

<table><tr><td></td><td>Main model</td><td>Diminishing returns</td></tr><tr><td> $p$ </td><td>None</td><td>None</td></tr><tr><td> $q$ </td><td>None</td><td> $\Delta t = 1 (-)$ </td></tr><tr><td> $\delta$ </td><td> $15 \leq \Delta t \leq 53 (-)$ </td><td> $\Delta t \geq 13 (-)$ </td></tr><tr><td> $\log(m)$ </td><td> $1 \leq \Delta t \leq 13 (+)$  $\Delta t \geq 15 (+)$ </td><td> $\Delta t \geq 82 (+)$ </td></tr><tr><td>Delay</td><td> $\Delta t \geq 1 (+)$ </td><td> $\Delta t \geq 2 (+)$ </td></tr><tr><td> $Delay^{2}$ </td><td> $\Delta t \geq 1 (-)$ </td><td> $\Delta t \geq 1 (-)$ </td></tr><tr><td>Foreign</td><td> $\Delta t \geq 1 (+)$ </td><td></td></tr><tr><td>Niche</td><td>None</td><td></td></tr><tr><td>Funny</td><td>None</td><td></td></tr></table>

## Appendix B.

Figure B.1. (Color online) Illustration of Diminishing Returns: Lift of Lag Platform 5 and Beyond (n = 45)  
![](/api/attachments/ZAUR8TA7/fulltext/images/8739bd67c4bff0c2e891cb6316766475b4bcb6c6893d8529a8e4fae270025461.jpg)  
Note. Conf. int., confidence interval.

## Appendix C. Propensity Score Matching

Propensity score matching is a commonly employed approach to estimate treatment effects using observational data by comparing treated observations to matched controls that are as similar as possible in all aspects besides their treatment assignment. PSM can be an effective method of establishing causality when applied on rich data sets that contain a comprehensive set of variables that are relevant to the outcome of interest.

Although seemingly similar to the synthetic control approach, PSM assumes that endogeneity can be minimized by matching treated and untreated items according to their observable characteristics. As a result, PSM-based analysis often fails to account for factors that are unobserved or hard to operationalize, thus failing to capture potential con founders while matching treated and untreated items (Ara et al. 2009, Oestreicher-Singer and Zalmanson 2010, Bapna et al. 2018). In our context, observable characteristics of videos may include length or characteristics of the associated channel. To our knowledge, extant research does not offer evidence that these characteristics offer predictive power over a video’s diffusion that is sufficiently accurate for our purposes.

Empirical examination of our data confirms the intuition that observable video properties are poor predictors of their long-term consumption. For example, our data contain two single-platform videos from Red Bull, and whereas one of these videos achieved about 800,000 views, the other achieved over 8 million. Similarly, we observe that videos of rival brands (e.g., McDonald’s and Burger King) did no seem to diffuse in a more similar way than did videos as sociated with different industries. Because of the limited availability of video properties that can be conveniently obtained, as well as the limited predictive power of the

<sup>4</sup> This agency wishes to remain anonymous.

Table C.1. Summary Statistics for Treated and Control Videos in PSM

<table><tr><td>Video characteristic</td><td>Treated videos</td><td>Matched control videos</td></tr><tr><td>Duration of video (seconds)a</td><td>67.12 (46.12)</td><td>114.80 (56.98)</td></tr><tr><td>Number of channel subscribersa</td><td>524,602 (1,622,321)</td><td>647,917 (1,775,567)</td></tr><tr><td>Number of videos posted by channela</td><td>359.8 (699.26)</td><td>15,766 (219,055.2)</td></tr><tr><td>Number of videos in category</td><td></td><td></td></tr><tr><td>New and politics</td><td>0</td><td>18</td></tr><tr><td>Entertainment</td><td>12</td><td>77</td></tr><tr><td>Sports</td><td>1</td><td>18</td></tr><tr><td>Music</td><td>2</td><td>8</td></tr><tr><td>Science and technology</td><td>5</td><td>38</td></tr><tr><td>Auto and vehicles</td><td>0</td><td>19</td></tr><tr><td>Film and animation</td><td>3</td><td>23</td></tr><tr><td>How-to and style</td><td>0</td><td>5</td></tr><tr><td>Comedy</td><td>5</td><td>22</td></tr><tr><td>Travel and events</td><td>0</td><td>2</td></tr><tr><td>People and blogs</td><td>3</td><td>6</td></tr><tr><td>Nonprofits and activism</td><td>1</td><td>2</td></tr><tr><td>Education</td><td>0</td><td>2</td></tr></table>

<sup>a</sup>The mean (SD) is shown.

properties we can observe, we chose to avoid PSM for our primary analysis. Although research that demonstrates greater potency of video characteristics for diffusion prediction may emerge, one can still argue that the effect of these characteristics would be reflected in the pretreatment diffusion of videos matched on consumption patterns. Thus, videos with similar observable (or unobservable) characteristics could still be matched based on consumption (e.g., synthetic control approach).

Despite PSM’s drawbacks, it remains empirically feasible to estimate lift using a PSM-based approach. We matched videos based on the four characteristics we had available to us, namely, duration, number of subscribers of the associated channel, number of video uploads by the associated channel, and video category. The latter characteristic is determined by YouTube and can be found under the description of each video. A summary of these video characteristics can be found in Table C.1.<sup>11</sup>

Because a video’s category is a categorical variable, we matched treated videos only with untreated videos within the same category to make PSM implementation feasible. After matching videos on category, we then leveraged standard PSM to do the rest of the matching based on the remaining three variables (Wooldridge 2010). As ex pected, resulting lift in Figure C.1 estimates do not show significance.

Our lack of significant results using PSM suggests that matching videos based on their basic characteristics may not satisfy the parallel trends assumption. That is, videos with similar length, category, or channel characteristics may not follow similar consumption trends. Notably, recent research has analyzed the role of video content in their consumption, showing that some emotional characteristics (e.g., presence of animals) (Tellis et al. 2019), and the personality reflected in a video’s speech captions (Krijestorac et al. 2018) could help predict a video’s popularity. Still, there is little evidence that such features alone can be used to minimize endogeneity between a treated and control video with similar features. Moreover, extracting relevant content features from videos may involve resource-intensive content analysis.

Figure C.1. (Color online) Lift Estimates Using PSM Matching Based on Video Characteristics  
![](/api/attachments/ZAUR8TA7/fulltext/images/1038b082c6cd20b02a8b99e46c5973a83b2967ee99702c524183af180e31f4c8.jpg)  
Note. Conf. int., confidence interval.

## Endnotes

<sup>1</sup> See https://research-doc.credit-suisse.com/docView?document \_id=1073963641, accessed July 31, 2018.

<sup>2</sup> See http://www.businessinsider.com/chart-of-the-day-youtube -videos-by-views-2009-5, accessed July 31, 2018.

<sup>3</sup> This assumption states that in the absence of an intervention (i.e., treatment), the treated and control videos would have followed parallel trends in view growth.

<sup>5</sup> “HP Labs – Let’s Do Amazing,” http://www.youtube.com/watch? v=Yu8Re1mpB8M, posted March 18, 2010.

<sup>6</sup> “McDonald’s Filet-O-Fish Hello,” https://www.youtube.com/watch?v =c5\_mt\_Cdz5o, posted February 19, 2010.

<sup>7</sup> “Apple – Meet iPad,” http://www.youtube.com/watch?v=nZ-yNISb54k, posted March 7, 2010.

<sup>8</sup> Analogously, a popular movie (e.g., Harry Potter and the Philosopher’s Stone) may exhibit strong consumption among its fan base early on. However, after the movie achieves a certain threshold of mainstream popularity and WOM, it also draws in nonfans.

<sup>9</sup> Estimates based on smoothing parameters 0.1, 0.2, and 0.3 are consistent with our main results in terms of significance.

<sup>10</sup> Because all multiplatform videos achieved at least 100,000 views, note that imposing a lower cutoff results in a set of poorerperforming single-platform videos available for synthetic control construction. Hence, lowering the cutoff could decrease views in only the synthetic controls, yielding less conservative lift estimates. Still, because of our matching approach, lift estimates using a 50,000-view cutoff are indistinguishable from our main estimates.

<sup>11</sup> We could not recover data on 72 videos because they no longer exist on YouTube or other platforms.

## References

Abadie A, Diamond A, Hainmueller J (2010) Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program. J. Amer. Statist. Assoc. 105(490):493–505.

Abadie A, Gardeazabal J (2003) The economic costs of conflict: A case study of the Basque Country. Amer. Econom. Rev. 93(1): 113–132.

Akpinar E, Berger J (2017) Valuable virality. J. Marketing Res. 54(2): 318–330.

Allsop DT, Bassett BR, Hoskins JA (2007) Word-of-mouth research: Principles and applications. J. Advertising Res. 47(4):398–411.

Anderson ET, Simester D (2013) Advertising in a competitive market: The role of product standards, customer learning, and switching costs. J. Marketing Res. 50(4):489–504.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Aral S, Muchnik L, Sundararajan A (2009) Distinguishing influencebased contagion from homophily-driven diffusion in dynamic networks. Proc. Natl. Acad. Sci. USA 106(51):21544–21549.

Arora S, ter Hofstede F, Mahajan V (2017) The implications of offering free versions for the performance of paid mobile apps. J. Marketing 81(6):62–78.

Athey S, Imbens GW (2017) The state of applied econometrics: Causality and policy evaluation. J. Econom. Perspect. 31(2):3–32.

Bampo M, Ewing MT, Mather DR, Stewart D, Wallace M (2008) The effects of the social structure of digital networks on viral marketing performance. Inform. Systems Res. 19(3):273–290.

Bapna R, Umyarov A (2015) Do your online friends make you pay? A randomized field experiment on peer influence in online social networks. Management Sci. 61(8):1902–1920.

Bapna R, Ramaprasad J, Umyarov A (2018) Monetizing freemium communities: Does paying for premium increase social engage ment? MIS Quart. 42(3):719–735.

Barabasi AL (2005) The origin of bursts and heavy tails in human´ dynamics. Nature 435(7039):207–211.

Bass FM (1969) A new product growth for model consumer durables. Management Sci. 15(5):215–227.

Berger J, Milkman KL (2012) What makes online content viral? J. Marketing Res. 49(2):192–205.

Billmeier A, Nannicini T (2012) Assessing economic liberalization episodes: A synthetic control approach. Rev. Econom. Statist. 95(3):983–1001.

Borah A, Tellis GJ (2015) Halo (spillover) effects in social media: do product recalls of one brand hurt or help rival brands? J. Mar keting Res. 53(2):143–160.

Brynjolfsson E, Hu Y, Smith MD (2003) Consumer surplus in the digital economy: Estimating the value of increased product vari ety at online booksellers. Management Sci. 49(11):1580–1596.

Chae I, Stephen AT, Bart Y, Yao D (2016) Spillover effects in seeded word-of-mouth marketing campaigns. Marketing Sci. 36(1):89–104.

Chen L, Zhou Y, Chiu DM (2014) A study of user behavior in online VoD services. Comput. Comm. 46(June):66–75.

Cheng J, Adamic LA, Dow PA, Kleinberg J, Leskovec J (2014) Can cascades be predicted? Preprint, submitted March 18, https:/ arxiv.org/abs/1403.4608.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Coffman M, Noy I (2012) Hurricane Iniki: Measuring the long-term economic impact of a natural disaster using synthetic control. Environment Development Econom. 17(2):187–205.

Corcoran S (2009) Defining earned, owned, and paid media. Report, Forrester Research, Cambridge, MA.

Cowpertwait PSP, Metcalfe AV (2009) Introductory Time Series with R (Springer, Dordrecht, Netherlands).

Crovella ME, Bestavros A (1997) Self-similarity in World Wide Web traffic: Evidence and possible causes. IEEE/ACM Trans. Networking 5(6):835–846.

Danaher B, Dhanasobhon S, Smith MD, Telang R (2010) Converting pirates without cannibalizing purchasers: The impact of digital distribution on physical sales and internet piracy. Marketing Sci. 29(6):1138–1151.

DiNardo J (2008) Natural experiments and quasi-natural experi ments. Macmillan P, ed. The New Palgrave Dictionary of Economic (Palgrave Macmillan, London), 1–12.

Dobele A, Toleman D, Beverland M (2005) Controlled infection! Spreading the brand message through viral marketing. Bus. Horizons 48(2):143–149.

Duan W, Gu B, Whinston AB (2008) The dynamics of online word-ofmouth and product sales—An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Easingwood CJ, Mahajan V, Muller E (1983) A nonuniform influence innovation diffusion model of new product acceptance. Marketing Sci. 2(3):273–295.

Efron B, Tibshirani R (1993) An Introduction to the Bootstrap (Chapman & Hall, New York)

Elberse A, Eliashberg J (2003) Demand and supply dynamics for sequentially released products in international markets: The case of motion pictures. Marketing Sci. 22(3):329–354.

Eliashberg J, Robertson TS (1988) New product preannouncing be havior: A market signaling study. J. Marketing Res. 25(3):282–292.

Erdem T, Sun B (2002) An empirical investigation of the spillover effects of advertising and sales promotions in umbrella brand ing. J. Marketing Res. 39(4):408–420.

Eren O, Ozbeklik S (2016) What do right-to-work laws do? Evidence from a synthetic control method analysis. J. Policy Anal. Management 35(1):173–194.

Ferguson R (2008) Word of mouth and viral marketing: Taking the temperature of the hottest trends in marketing. J. Consume Marketing 25(3):179–182.

Fu WW, Sim CC (2011) Aggregate bandwagon effect on online videos’ viewership: Value uncertainty, popularity cues, and heuristics. J. Amer. Soc. Inform. Sci. Tech. 62(12):2382–2395.

Garg R, Smith MD, Telang R (2011) Measuring information diffusion in an online community. J. Management Inform. Systems 28(2):11–38.

Gatignon H, Eliashberg J, Robertson TS (1989) Modeling multinational diffusion patterns: An efficient methodology. Marketing Sci. 8(3):231–247.

Gong J, Smith MD, Telang R (2015) Substitution or promotion? The impact of price discounts on cross-channel sales of digital movies. J. Retailing 91(2):343–357.

Goldenberg J, Han S, Lehmann DR, Hong JW (2009) The role of hubs in the adoption process. J. Marketing 73(2):1–13.

Granovetter M (1978) Threshold models of collective behavior. Amer. J. Sociol. 83(6):1420–1443.

Hendricks K, Sorensen A (2009) Information and the skewness of music sales. J. Political Econom. 117(2):324–369.

Hinrichs P (2010) The effects of affirmative action bans on college enrollment, educational attainment, and the demographic composition of universities. Rev. Econom. Statist. 94(3):712–722.

Hoban PR, Bucklin RE (2015) Effects of internet display advertising in the purchase funnel: Model-based insights from a randomized field experiment. J. Marketing Res. 52(3):375–393.

Johnson GA, Lewis RA, Nubbemeyer EI (2017) Ghost ads: Improving the economics of measuring online ad effectiveness. J. Marketing Res. 54(6):867–884.

Kalish S, Mahajan V, Muller E (1995) Waterfall and sprinkler newproduct strategies in competitive global markets. Internat. J. Res. Marketing 12(2):105–119.

Kannan PK, Pope BK, Jain S (2009) Practice prize winner—Pricing digital content product lines: A model and application for the National Academies Press. Marketing Sci. 28(4):620–636.

Krijestorac H, Garg R, Saar-Tsechansky M (2018) The role of personality in the diffusion of digital media. Internat. Conf. Inform. Systems 2018 Proc. (Association for Information Systems, Atlanta).

Lee E, Lee J, Lee J (2006) Reconsideration of the winner-take-all hypothesis: Complex networks and local bias. Management Sci. 52(12):1838–1848

Lenk PJ, Rao AG (1990) New models from old: Forecasting product adoption by hierarchical Bayes procedures. Marketing Sci. 9(1):42–53.

Leskovec J, Adamic LA, Huberman BA (2007) The dynamics of viral marketing. ACM Trans. Web 1(1):5.

Liebowitz SJ (2004) Will MP3 downloads annihilate the record industry? The evidence so far. Intellectual Property and Entrepreneurship, Advances in the Study of Entrepreneurship, Innovation and Economic Growth, vol. 15 (Emerald Group Publishing Limited, Bradford, UK), 229–260.

Mahajan V, Peterson RA (1985) Models for Innovation Diffusion (Sage Publications, Beverly Hills, CA).

Moore GA (2014) Crossing the Chasm: Marketing and Selling Disruptive Products to Mainstream Customers, 3rd ed. (HarperBusiness, New York).

Neelamegham R, Chintagunta P (1999) A Bayesian model to forecast new product performance in domestic and international markets. Marketing Sci. 18(2):115–136.

Oestreicher-Singer G, Zalmanson L (2010) Who pays “premium” in the age of free services? Findings from a media website. Mediterranean Conf. Inform. Systems 2010 Proc. (Association for Information Systems, Atlanta).

O’Neill S, Kreif N, Grieve R, Sutton M, Sekhon JS (2016) Estimating causal effects: Considering three alternatives to difference-in differences estimation. Health Services Outcomes Res. Methodology 16(1):1–21.

Pinto H, Almeida JM, Gonçalves MA (2013) Using early view patterns to predict the popularity of YouTube videos. Proc. 6th ACM Internat. Conf. Web Search Data Mining (Association for Computing Machinery, New York), 365–374.

Putsis WP, Balasubramanian S, Kaplan EH, Sen SK (1997) Mixing be havior in cross-country diffusion. Marketing Sci. 16(4):354–369.

Roehm ML, Tybout AM (2006) When will a brand scandal spill over, and how should competitors respond? J. Marketing Res. 43(3):366–373.

Rogers EM (2003) Diffusion of Innovations, 5th ed. (Free Press, New York).

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1):41–55.

Rumbo JD (2002) Consumer resistance in a world of advertising clutter: The case of Adbusters. Psych. Marketing 19(2):127–148.

Rutherford D (2013) Routledge Dictionary of Economics, 3rd ed. (Routledge, London).

Rutz OJ, Bucklin RE (2011) From generic to branded: A model of spillover in paid search advertising. J. Marketing Res. 48(1):87–102.

Sarwar B, Karypis G, Konstan J, Riedl J (2001) Item-based collaborative filtering recommendation algorithms. Proc. 10th Internat. Conf. World Wide Web (Association for Computing Machinery, New York), 285–295.

Siegler MG (2010) Eric Schmidt: Every 2 days we create as much information as we did up to 2003. TechCrunch (August 4), https:/ techcrunch.com/2010/08/04/schmidt-data/.

Smith MD, Telang R (2009) Competing with free: The impact of movie broadcasts on DVD sales and internet piracy. MIS Quart. 33(2): 321–338.

Srinivasan V, Mason CH (1986) Technical note—Nonlinear least squares estimation of new product diffusion models. Marketing Sci. 5(2):169–178.

Stieglitz S, Dang-Xuan L (2013) Emotions and information diffusion in social media—Sentiment of microblogs and sharing behavior. J. Management Inform. Systems 29(4):217–248.

Sultan F, Farley JU, Lehmann DR (1990) A meta-analysis of appli cations of diffusion models. J. Marketing Res. 27(1):70–77.

Szabo G, Huberman BA (2010) Predicting the popularity of online content. Comm. ACM 53(8):80–88.

Talukdar D, Sudhir K, Ainslie A (2002) Investigating new product diffusion across products and countries. Marketing Sci. 21(1):97–114.

Tan PN, Steinbach M, Kumar V (2006) Introduction to Data Mining, 1st ed. (Pearson Addison-Wesley, Boston).

Tellis GJ, MacInnis DJ, Tirunillai S, Zhang Y (2019) What drives virality (sharing) of online digital content? The critical role of information, emotion, and brand prominence. J. Marketing 83(4):1–20.

Thomas RJ (1985) Estimating market growth for new products: An analogical diffusion model approach. J. Product Innovation Management 2(1):45–55.

Tirunillai S, Tellis GJ (2017) Does offline TV advertising affect online chatter? Quasi-experimental analysis using synthetic control. Marketing Sci. 36(6):862–878.

Van Alstyne MW, Parker GG, Choudary SP (2016) Pipelines, platforms, and the new rules of strategy. Harvard Bus. Rev. 94(4):54–62.

van der Lans R, van Bruggen G, Eliashberg J, Wierenga B (2009) A viral branching model for predicting the spread of electronic word of mouth. Marketing Sci. 29(2):348–365.

van Everdingen Y, Fok D, Stremersch S (2009) Modeling global spill over of new product takeoff. J. Marketing Res. 46(5):637–652

Varian HR (2016) Causal inference in economics and marketing Proc. Natl. Acad. Sci. USA –

Walters RG (1991) Assessing the impact of retail price promotions on product substitution, complementary purchase, and interstore sales displacement. J. Marketing 55(2):17–28.

Wang C(A), Zhang X(M), Hann IH (2018) Socially nudged: A quasi experimental study of friends’ social influence in online product ratings. Inform. Systems Res. 29(3):641–655.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Pane Data, 2nd ed. (MIT Press, Cambridge, MA).

Wright P (1975) Factors affecting cognitive resistance to advertising. J. Consumer Res. 2(1):1–9.

Wu F, Huberman BA (2007) Novelty and collective attention. Proc Natl. Acad, Sci, USA 104(45):17599–17601

Yoganarasimhan H (2012) Impact of social network structure on content propagation: A study using YouTube data. Quant. Marketing Econom. 10(1):111–150.

Zentner A (2006) Measuring the effect of file sharing on music purchases. J. Law Econom. 49(1):63–90.

Zentner A, Smith M, Kaya C (2013) How video rental patterns change as consumers move online. Management Sci. 59(11):2622–2634.
