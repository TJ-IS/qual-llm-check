---
otero_id: 1350
otero_key: "ZRKHUW2H"
title: "Ad-Blockers: A Blessing or a Curse?"
authors: "Manmohan Aseri; Milind Dawande; Ganesh Janakiraman; Vijay S. Mookerjee"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0906"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.238.7.40] On: 09 June 2020, At: 00:10 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/ZRKHUW2H/fulltext/images/22126d8fca8652fecbe8f88cbbf7dc4ebc171e98b70ca1fb88e8e8193b79a5c3.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Ad-Blockers: A Blessing or a Curse?

Manmohan Aseri, Milind Dawande, Ganesh Janakiraman, Vijay S. Mookerjee

To cite this article: Manmohan Aseri, Milind Dawande, Ganesh Janakiraman, Vijay S. Mookerjee (2020) Ad-Blockers: A Blessing or a Curse?. Information Systems Research

Published online in Articles in Advance 04 Jun 2020

https://doi.org/10.1287/isre.2019.0906

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Ad-Blockers: A Blessing or a Curse?

Manmohan Aseri,<sup>a</sup> Milind Dawande,<sup>b</sup> Ganesh Janakiraman,<sup>b</sup> Vijay S. Mookerjee<sup>b</sup>

<sup>a</sup> Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213; <sup>b</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080

Contact: maseri@andrew.cmu.edu, https://orcid.org/0000-0001-6943-2432 (MA); milind@utdallas.edu, https://orcid.org/0000-0001-6956-0856 (MD); ganesh@utdallas.edu, https://orcid.org/0000-0001-7386-4318 (GJ); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VSM)

Received: Revised: May 1 Accepted: Published Online in Articles in Advance: June 4.2020

https://doi.org/10.1287/isre.2019.090

Copyright:

Abstract. Users who have an ad-blocker installed present a genuine predicament for a website (also known as the publisher): On the one hand, these users do not generate revenue for the website; on the other hand, denying them access can shrink the user base and adversely affect the popularity of the website, ultimately reducing traffic over the long run. This has led some websites to require that ad-block users “white-list” them for obtaining access to an “ad-light” experience. We model the decision problem for a website facing two user segments: regular users and ad-block users. The first-level decision or gating strategy is whether to allow ad-free access to ad-block users or require them to white-list the website for gaining access. When ad block users are allowed ad-free access, the second-level decision is the level of advertising (or ad-intensity) for regular users. When ad-block users are required to white-list, the second-level decisions are the ad-intensities for regular users and ad-block users. The net utility of a user from visiting the website depends on the intrinsic value of the website’s content, the value obtained due to network effects driven by the amount of traffic/popularity of the website, and the cost incurred due to the presence of ads. We derive an optimal gating and ad-intensit strategy for the website and also solve an identical model for a world without ad-block software. We show that the website can increase its revenue by discriminating between regular and ad-block users via the ad-intensities shown to them. More interestingly, we find that the discriminatory power bestowed on the website by ad-blockers can increase the social surplus and, in particular, increase the surplus of both user segments, namely, regular users and adblock users, when the utility from their outside option is below a threshold. Thus, the advent of ad-blockers can lead to a win-win for both the website and its users. Finally, we propose a superior selective-gating strategy in which only a fraction of ad-block users are gated. We establish the robustness of our conclusions under several enhancements to our base setting: (a) heterogeneous profitabilities from regular users and ad-block users, (b) endogenous adoption of ad-blockers, (c) the presence of a subscription option, and (d) negative externality due to increased traffic. Our analysis ends with recommendations for three stakeholders in this problem, namely, publishers, web-browser developers, and policy makers.

History: Ram Gopal, Senior Editor; Sanjukta Smith, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2019.0906.

Keywords: ad-blocking • web advertising • rational expectations equilibrium • revenue maximizatio

## 1. Introduction

Online advertisements have been pivotal in keeping the internet largely free of cost for users. Many websites, small and large, rely solely on advertising revenue for their survival. Although it is a lifeline for a free internet, online advertising has been widely criticized for deteriorating consumer experience by displaying an excessive amount of irrelevant ads to users (Elliott 2017). Perhaps as an inevitable systemic retaliation, recent advancements in technology have allowed consumers of digital content to block advertisements by using a type of software that is now commonly referred to as an Ad-Blocker (e.g., Adblock Plus). A typical adblocker works by blocking ads at their source, that is, by preventing communication to ad-servers that deliver ads. Therefore, the use of ad-blockers not only improves the visual experience of the user but also results in other advantages, including reduced data download and website loading time and efficient use of battery power. It has been reported that websites load nearly four times faster with an ad-blocker and use about 50% less data (DigitBin 2018, Wakabayash and Marshall 2015).

Motivated by these benefits, companies like Apple and Samsung—that do not rely heavily on ad revenues—have welcomed ad-blockers on their mobile devices by adding the functionality to integrate third-party ad-blockers. According to a highly cited recent report by PageFair,<sup>1</sup> ad-blocking penetration in the United States is currently around 18% and in some other countries, such as Indonesia, has reached above 50%. It is estimated that publishers in the United States will lose about \$12.1 billion due to the use of ad-blockers in 2020 (Statista 2019).

Most ad-blockers come with a “white-listing” feature, that allows web-users to create a list of websites, referred to as a white-list, in which the ad-blocker will not prevent ads from appearing. If an adblocker is detected on a user’s device, the target website can ask the user to white-list the website, failing which access to the website can be denied; examples include http://www.forbes.com and http://www.businessinsider.com. Thus, websites do have a choice in allowing or denying access to adblock users. This raises a genuine predicament: on the one hand, ad-block users do not generate revenue for the website; on the other hand, denying them access can shrink the user base and adversely affect the popularity of the website, ultimately reducing traffic over the long run (we refer to this phenomenon as a network effect). Indeed, many publishers who reacted to the increase in ad-block users by denying them access quickly stepped back and stopped doing so (e.g., http://www.ratemyprofessors.com). To our knowledge, no clear strategy has yet emerged to resolve this dilemma. Although many websites have reacted to the phenomenon of ad-blocking by denying access to users, some websites have maintained a cautious silence. Near-monopolistic websites, such as Facebook, YouTube, and Google, which rely heavily on advertisement revenue, have continued to allow users to block ads. Our analysis sheds light on why some websites choose to deny access, whereas others continue to allow users to block ads.

We model the decision problem for a publisher facing two user segments: regular users (hereafter referred to as regulars) and ad-blockers.<sup>2</sup> Regulars are potential users of the website who do not use any adblock software, whereas ad-blockers are potential users of the website who also use some ad-block software. The first-level decision or gating strategy is whether to (a) allow ad-free access to ad-block users or (b) require white-listing by ad-block users in order to allow them access. Under (a), the second-level decision for the website is the level of advertising (ad-intensity) to regular users. Under (b), the secondlevel decisions are the ad-intensities to be used for regular users and for ad-block users.<sup>3</sup> The website’s revenue depends directly on the ad-intensity it chooses and the traffic it generates from each of the two user segments. Moreover, the traffic it generates depends on the net utility that each individual user receives from visiting the website and the value of the best alternative to the website (i.e., the outside option). The net utility offered by the website depends on (i) the intrinsic value of the website’s content; (ii) the value users obtain because of network effects, that is, value derived as a result of the amount of traffic/ popularity of the website; and (iii) a negative utility or cost incurred because of the presence of ads, driven by the overall past experience of ads as a nuisance; regular and ad-block users differ in terms of these adviewing costs. Using this model, we derive an optimal gating and ad-intensity strategy for the website. We also solve an identical model for a world without adblock software. We show analytically that the presence of such software can be used by the website to increase its revenue by discriminating between regular and ad-block users in terms of the ad-intensities shown to them. Clearly, this was not possible in the absence of such software.

One naturally wonders if the website’s benefit in the post-ad-block world comes at the expense of consumer welfare. Interestingly, we establish the precise condition—the utility users get from their outside option is lower than a threshold—under which the website and its consumers (both regular users and ad-block users) benefit after the advent of ad-block software. Intuitively, when the website is able to customize ad-intensities for regulars and ad blockers, the total traffic to the website increases. When the outside option offers a low utility, these additional users not only obtain a higher net utility (relative to the pre-ad-block world) but also increase the value of the website, which in turn also increases the net utility of the existing users. Our analysis also reveals interesting features of the website’s optimal gating strategy with an increase in the maximum value that users can obtain from the website; in particular, the website’s optimal gating decision can first switch from gating to not gating and then switch again from not gating to gating.

Instead of gating either all or none of the users (integral gating), one can consider a more-general selective gating strategy in which only a fraction of the adblock users are asked to white-list the website. We show that this can increase the website’s revenue significantly from that under integral gating. This analysis also helps us derive insights on the optimal selective gating strategy, with respect to the strength of the network effect and the ad-blocking rate (the fraction of the potential user population that uses ad-blockers).

The remainder of the paper is organized as follows. We review the related literature in Section 2. In Section 3, we formally define the basic model of gating and ad-intensity decisions in which either all ad-block users are allowed ad-free access to the website or al ad-block users are asked to white-list the website in order to access it (integral gating). In Section 4, we present our analysis of the optimal gating decision and ad-intensities in the post-ad-block world as well as the optimal ad-intensity in the pre-ad-block world. Using these results, Section 4.3 analyzes the impact of ad-block software on the publisher’s revenue and the level of advertising shown to users, and Section 4.5 examines the impact on consumers and social welfare. The possibility of selectively gating some adblock users is modeled and analyzed in Section 5. This analysis is then used to examine the impact of the relative strength of the network effect and the adblocking rate on the optimal gating decision and on the increase in the website’s revenue. Section 6 establishes the robustness of our conclusions under several enhancements to our base setting. Section 6.1 discusses our recommendations for publishers, webbrowser developers, and policy makers.

## 2. Brief Review of the Related Literature

Our work is related to the following streams of literature: (i) ad-avoidance, (ii) versioning, and (iii) freeriding. We now review each of these streams in detail.

## Ad Avoidance

The stream of literature that is closest to our work is the one on ad-avoidance. The main focus of this literature is on the consequences of ad-avoidance for advertisers and consumers; see, for example, Hann et al. 2008, Johnson 2013, and Goh et al. 2015. The modus operandi to avoid ads that have been examined here include, among others, avoiding TV ads by switching channels, avoiding telemarketing ads by registering on Do-Not-Call lists, and ignoring marketing emails. There also exist studies that investigate the impact of ad-avoidance on the revenue of the facilitators of advertising content; for example, TV broadcasters and print media (Stühmeier and Wenzel 2011). However, the ramifications of ad-avoidance on web-based advertising and the creation of effective response strategies for publishers is a relatively understudied subject. This is expected, because contracts for advertising on TV and telephone are long-term delivery contracts, where the facilitator usually gets paid regardless of whether the ad is actually seen by the consumer (in some cases, the payments are adjusted based on overall viewership statistics). Consequently, facilitators remain largely insulated from the ad-avoidance behavior of consumers. In contrast, a majority of present-day digital advertising content is cleared via real-time bidding for ad space, with publishers often getting paid only when an ad is clicked upon by the consumer (i.e., pay-per-click payments). Therefore, in web-based advertising, ad-avoidance by consumers can significantly dent the revenue of publishers. With ad-blockers being the latest tool that consumers are increasingly adopting to avoid web ads, the question of how publishers should react intelligently to ad-blockers naturally gains importance. One key dif ference between ad-blocking on websites and adavoidance in traditional media (e.g., TV, radio) is the ability of facilitators to deliver ads: In contrast to traditional media, an ad cannot even be delivered on a website in the presence of an ad-blocker because it is blocked at its source. Further, relative to traditional media, web-based advertising presents a much richer setting to counter ad-avoidance because, here, the publisher has the ability to interact with each user individually, for example, by asking a user to white-list the website. Accordingly, there is scope to develop novel “microlevel” strategies for publishers, investigate their structural properties, and assess their impact on revenue. Our work is an attempt to contribute in these directions. Two recent papers analyze settings that also involve the adoption of ad-blockers by users. Ray et al. (2017) analyze strategic interactions among content providers (websites), ad blocking platforms, users, and advertisers. The content provider decides the quality of content, and the ad-blocking platform decides the prices to charge users (for installation) and advertisers (for not blocking their ads). Given the quality of content provided by websites and the prices set by the platform, the users and advertisers decide whether to adopt the platform. The paper derives useful insights on the optimal pricing structure for the platform, the adoption of the platform by users and advertisers, and the quality of content provided by websites. Despotakis et al. (2017) analyze the impact of ad-blockers in a setting of two competing websites. Consistent with one of our results, this study also finds that the advent of ad-blockers can benefit the two websites; however, the analysis in this study does not consider the presence of network effects, which play a critical role in our analysis for deriving a website’s optimal strategy in reacting to ad-block users.

The work that is perhaps closest to our study is Hann et al. (2008). However, along with the abovementioned finer granularity of decision making in our context, there are several other important differences in the analysis. In Hann et al. (2008), the value of the product being advertised does not depend on the number of users of the product. On the other hand, the network effect is at the core of our paper and plays a critical role in the website’s decisions. Further, in Hann et al. (2008), there are two consumer segments, low-benefit and high-benefit, that differ in the profitability they offer to the decision maker. In contrast, the consumer segments in our analysis are equally profitable from the website’s viewpoint. It is in their individual sensitivities to ads (i.e., their respective ad-viewing costs) that these segments differ.

Hann et al. (2008) find that when low-benefit consumers conceal themselves, advertising becomes cost-effective and leads sellers to advertise more to the remaining users. One of our findings—actions by some consumers (i.e., ad-block users) to avoid advertisements affects other consumers—is consistent with the above result in Hann et al. (2008). However, the force behind these two results is different. In Hann et al. (2008), the externality arises from the advertising becoming cost-effective. In our analysis, instead, the externality arises from (i) the ability of the website to discriminate users on the basis of their ad-viewing costs and (ii) the presence of the network effect. In practice, the extent of such externalities has been empirically established in Goh et al. (2015), in the context of consumers registering on Do-Not-Call lists to avoid marketing solicitations.

In our analysis, a website derives value from two components: an intrinsic component based on the website’s content and another based on network effect (driven by the traffic/popularity of the website). This decomposition has been well established in the literature, dating back at least to the work of Katz and Shapiro (1985). In their classic paper, Parker and Van Alstyne (2005) examine the reasons behind the practice of firms giving away free products. They argue that for firms that produce complementary goods, it may sometimes be profitable to provide a good for free. Intuitively, the cost incurred in providing a free good can be more than offset by the resulting increase in the demand for a “premium” good because of network effect. This result bears similarity to one of our results; in the ad-blocking context, allowing some ad-block users ad-free access increases the website’s traffic and thereby its value (because of network effect) and in turn leads to an increase in the number of regular (non-ad-block) users. The notion of network effect has been exploited in several other contexts, for example, to examine the strategic interactions between service providers and their users (Nair et al. 2015). to measure the de: pendence between user-generated content and social ties in online social networks (Shriver et al. 2013), and to measure the financial value of retaining and acquiring content contributors for a website that provides user-generated content (Zhang et al. 2012). Dou et al. (2013) examine how firms can engineer network externalities to their advantage, and Kauffman et al. (2000) examine the impact of network externalities on the adoption of a network. For a comprehensive discussion of network effects, we refer the reader to Gallaugher (2008).

## Versioning

A website’s decision to allow ad-block users to access the website without being subject to ads is akin to a firm providing a free version of its product or service; see, for example, Chellappa and Shivendu (2010),

Niculescu and Wu (2014), and Lambrecht and Misra (2016). Typically, free versions offer a limited set of features, relative to the premium varieties. In our context, however, ad-blockers (if allowed to access the website) and regular users experience the same content.

The beneficial discrimination of the user population is an idea that our work shares with the versioning literature; see, for example, Varian 1997, Chellappa and Shivendu 2005, Bhargava and Choudhary 2008 Wu and Chen 2008, Lahiri and Dey 2013, Wei and Nault 2014, and Ma 2015. There are significant differences, however, in our setting relative to what is typical in a traditional versioning problem and also in how discrimination is operationalized. We now discuss some of these differences. Note that, in our context, all the users of the focal website have access to the same content; the basis for discrimination is the disutility they incur because of advertisements. In other words, all the users experience the same consumption utility (the equilibrium value of the website), but the two subgroups of users (namely, white-listers and regulars) incur different disutilities from ads. This is in contrast with the typical versioning setting, where price is the discriminating tool and a premium version usually offers a higher consumption utility than the “standard” version; for example, the former typically offers more features than the latter. Further, in our setting, the absence of price as a discriminatory tool generates an interesting contrast in the following sense: In a typical versioning problem, the firm’s revenue is determined by the consumption utility the product offers to the consumer (the price paid by the consumer equals the revenue the firm makes). In our setting, because users do not pay anything, it is the disutility imposed on them—and the extent of it—that indirectly generates revenue for the website (higher ad-intensities result in higher advertising revenue). Also, the notions of “high-type” and “low-type” consumers, which are common in the versioning literature, are not apparent in our setting. For instance, it is typical to find a high-type consumer incur more cost (because she buys the premium version, which is priced higher). On the other hand, in our context, a regular visitor is shown a relatively higher ad-intensity but his ad-sensitivity is relatively lower; thus, the cost (disutility) he incurs is not directly comparable to that for an ad-block user.

The outside option and the network effect are two important differentiators of our work from the traditional versioning literature. The combined consideration of these two features allows us to characterize the precise condition under which both consumer and social surplus increase in the post-ad-block world (relative to that in the pre-ad-block world). Specifically, we show that consumer and social surplus increase in the post-ad-block world if and only if the utility offered to the users by their outside option is below a parameter-dependent threshold that depends on the strength of the network effect. Further, under this condition, the surplus of both segments, namely, adblock users and regular users, increases.

The network effect plays a crucial role in the abovementioned results. Broadly, ad-blockers enable the website to adjust ad-intensities according to the adsensitivity of the user group. This smart adjustment of ad-sensitivities leads to a higher traffic for the website, and eventually leads to a higher value of the website for everybody. In other words, the size of the pie grows and a win-win situation is created. Typically, in the versioning literature, the benefit of second-degree discrimination (via versioning) is confined to the firm. However, as discussed above, these benefits can spill over to the consumers too in the presence of the network effect.

The discrimination of users based on their adviewing costs further gives rise to interesting operational possibilities such as selective gating (Section 5), where a subset of ad-block users is given ad-free access to exploit network effects (in the versioning setting, this would correspond to distributing a premium version free to a subset of consumers). One can also combine nonmonetary and monetary levers to improve our capability to discriminate. For instance, in Section $^ { 6 , }$ we study a setting in which the website offers potential users the option of paid subscription to access ad-free content in addition to the option of viewing ad-supported free content by white-listing the website. Thus, via the use of different ad-intensities, selective gating, and the subscription option, a website can have four types of users: (i) ad-block users who get ad-free access, (ii) white-listers (who get an ad-light experience), (iii) regular users (who get a relatively ad-heavy experience), and (iv) subscribers (who are given (paid) ad-free access).

## Free-Riding

A website that survives on advertising revenue can afford to let some ad-block users free-ride by enjoying ad-free content if it can generate sufficient revenue from non–ad-block users. In this sense, our work is related to the free-riding phenomenon. Shin (2007) analyzes the free-riding behavior of a discount retailer who does not provide presale customer service (say, helping customers choose the right product) and, therefore, incurs lower operating costs, leading to lower prices. The author finds that if customers are heterogeneous in terms of their opportunity cost of visiting the discount retailer after receiving presale customer service from another retailer who provides such a service, then the latter can benefit because of the free-riding behavior of the former. In our context, it is the heterogeneity in users’ ad-viewing cost that drives the increase in revenue of the website in the post-ad-block world. Asvanund et al. (2004) empirically examine the impact of free-riding by users in a peer-to-peer (P2P) network and find that the extent of free-riding increases as the size of the network increases; Johar et al. (2011) analyze congestion in P2P networks and provide a mechanism to induce socially optimal sharing.

The advent of ad-blockers has triggered an arms race between publishers and firms that develop adblock software: developers continue to devise new techniques to evade the detection of their ad-blockers, and publishers react by working out ways to detect an ad-blocker’s presence. This has generated a significant amount of work in the computer science literature; for instance, new ad-blocking techniques (see, $\mathrm { e . g . }$ ., Krammer 2008, Storey et al. 2017), legal implications and impact on privacy (see, e.g., Krammer 2008, Vallade 2008, Gervais et al. 2017, and Garimella et al. 2017), and anti–ad-blocking reactions and the impact of ad-blockers on the targeting ability of publishers (see, e.g., Johnson 2013 and Nithyanand et al. 2016).

## 3. Model

We consider a publisher (a website) whose entire revenue comes from advertisements and whose potential user population consists of two segments: adblockers (potential users of the website, who use some ad-block software) and regulars (potential users of the website, who do not use any ad-block software). 4 We denote the size of the potential user population by N, the fraction corresponding to ad-blockers by $B ,$ , and the fraction corresponding to regulars by ${ \bar { B } } : = 1 - B .$ We assume that the content-creation cost for this website is sunk, and the cost of serving that content to a user is zero. We consider the following two decisions for this publisher (see Figure 1 for a real-world illustration of these decisions):

• Gating: The publisher could allow ad-blockers to access the website for free (i.e., without showing any ads) or require them to white-list this website in order to access it. We use $I _ { G } \in \{ 0 , 1 \}$ to denote this gating decision, with $I _ { G } = 0$ denoting ad-free access and $I _ { G } = 1$ the white-listing requirement.

• Ad-Intensity: If $I _ { G } = 1 $ , the publisher decides two ad-intensities, $, a _ { r }$ and ${ a } _ { b } ,$ , respectively, for regulars and ad-blockers who white-list (we refer to these as whitelisters). $\mathrm { I f } I _ { G } = 0 .$ , the publisher decides an ad-intensity $a _ { r }$ for regulars; because ad-blockers are allowed to access the website without seeing ads, ${ a _ { b } = 0 }$ in this case. Driven by practical considerations (e.g., the minimum level necessary to grab user attention and/ or the minimum amount dictated by the need to

Figure 1. The Message Shown by Forbes.com to an Ad-Block User

## CONTINUE TO SITE >

## Forbes QUOTEOF

present you with an ad-light experience.

Notes. The message highlights the following two actions: (i) The user is not allowed access to the website unless she disables the adblocker. (ii) Upon white-listing, the user will be offered an ad-light experience.

complete ad campaigns in a timely manner), if ads are shown, the publisher is required to maintain a minimum ad-intensi $\mathrm { t y } ^ { 5 }$ of $a _ { \mathrm { m i n } } > 0$ . Thus,

$$
a _ {r}, a _ {b} \in \{0 \} \cup [ a _ {\min}, \infty); \text { moreover }, a _ {b} = 0 \text {   if   } I _ {G} = 0.
$$

Although users do occasionally find ads useful, they are on average (based on past experience) typically perceived as a nuisance. Accordingly, we assume that users have a negative average perception of ads; in other words, users incur nonnegative ad-viewing costs. We model heterogeneous ad-viewing costs for potential users. For a randomly picked regular (adblocker) who is shown an ad-intensity of one, the ad-viewing cost is a random variable denoted by $\tilde { c } _ { r } \sim$ $U [ 0 , \ C _ { r } ] \ \tilde { ( c _ { b } } \sim U [ 0 , \ C _ { b } ] )$ . Therefore, when a regular (ad-blocker) is shown an ad-intensity of $a _ { r } \ \left( a _ { b } \right)$ , he incurs an ad-viewing cost of $a _ { r } \tilde { c } _ { r } \left( a _ { b } \tilde { c } _ { b } \right)$ . Thus, the two segments of potential users differ in their distributions of ad-viewing costs for any given ad-intensity. We also refer to $\tilde { c } _ { b }$ and $\tilde { c } _ { r }$ as the ad-sensitivity of an ad-blocker and a regular user, respectively. We assume that $C _ { b } \geq C _ { r }$ to reflect the idea that ad-blockers are likely to perceive ads as being a greater nuisance than what regulars perceive. For every user visiting the website, the publisher makes a revenue of $r \cdot a$ if the ad-intensity is a; thus, r is the ad revenue per user from an ad-intensity of one.<sup>6</sup>

Let v denote the gross value that users obtain by accessing the website (excluding ad-viewing costs). This value, v, has two independent components: One component is the intrinsic value of the website generated through its content, and the other component is the network value of the website generated through the usage of the website. This decomposition is consistent with the literature (see, e.g., Katz and Shapiro 1985, Lee and Mendelson 2007, Li and Chen 2012) as is our assumption of uniformly distributed ad-viewing costs (see, e.g., Anderson and Gans 2011). When users beneficially communicate and exchange information among themselves, the value of the website increases with the number of users. For instance, platforms such as Uber operate under very high two-sided network effects—an increase in the number of drivers increases the value of the platform for riders. Likewise, an increase in the number of riders increases the attractiveness of the platform for drivers. Platforms such as eBay and Amazon derive value from the interactions among their participants: the more number of participants, the more is this value. An increase in the user base of a website increases its popularity and can, in turn, lead to an increase in the links (on other websites) that point to that website; this can improve its PageRank on Google search. Social media can also fuel network effects. For example, for a website such as Forbes.com, network value can be created by an increase in readership because of traffic enabled via social media by the sharing of content between existing users. Let n represent the number of users of this website out of the total population of N potential users. We assume the following functional form for v:

$$
v = v _ {0} + \theta \frac {n}{N},\tag{1}
$$

The fraction $n / N$ denotes the extent of market penetration by this website. The constant $v _ { 0 }$ denotes the intrinsic value generated from the website’s content whereas θn/N denotes the value generated by network effects. We, therefore, refer to θ as the networkeffect parameter.

Let $u _ { 0 }$ represent the net utility of an outside option for the potential users. The outside option represents some other website or source where similar content can be accessed (if no such source exists, then $u _ { 0 } = 0 )$ We assume that $u _ { 0 } \leq v _ { 0 } + \theta ,$ , failing which no poten tial user will be interested in visiting this website. Therefore, a regular with an ad-sensitivity of $\widetilde { c } _ { r }$ becomes a user of this website if $v - a _ { r } \tilde { c } _ { r } \geq u _ { 0 }$ . Similarly, an ad-blocker with an ad-sensitivity of $\tilde { c } _ { b }$ becomes a user of this website if the website allows ad-free access to ad-blockers (i.e., does not gate them) and $v \geq$ $u _ { 0 }$ (in this case, $\tilde { c } _ { b }$ is inconsequential); if the website requires ad-blockers to white-list (i.e., gates them), then this ad-blocker white-lists and becomes a user if $v - a _ { b } \tilde { c } _ { b } \geq u _ { 0 }$ . Thus, the publisher faces the following trade-off. On the one hand, an increase in the adintensity leads to a higher revenue from each user. On the other hand, this increase reduces the net utility that potential users obtain from this website and, therefore, reduces the number of users, which, in turn, reduces revenue.

Figure 2 depicts the sequence of events of the game. The website first decides ${ \cal I } _ { G } , ~ a _ { b }$ and $a _ { r } .$ . After the website’s decisions, all the N potential users decide whether to pick the focal website (i.e., become a user)

Figure 2. The Sequence of Events of the Game  
![](/api/attachments/ZRKHUW2H/fulltext/images/ba1ac4bf1fe3ce3e02d7811621bf1ac67c87fad004f9d55c08572931dcfca95d.jpg)  
Notes. First the website decides ${ \cal I } _ { G } , ~ a _ { b } ,$ and $a _ { r }$ . Then, the ad-blockers decide whether to white-list the website, and the regulars decide whether to access the website. The quantities in brackets represent the payoffs received by the website and the user, respectively.

or pick the outside option, based on the comparison of their net utilities from these two sources as explained above. In Figure 2, the two quantities in brackets represent, respectively, the website’s revenue from a potential user and that potential user’s net utility. For every regular user, the website earns a revenue of $r a _ { r }$ . If $I _ { G } = 0$ (that is, the website does not gate adblockers), the website makes no revenues from adblockers. If $I _ { G } = 1 $ , the website makes a revenue of $r a _ { b }$ from every ad-blocker. Table 1 summarizes our main notation. Figure 3 is a graphical representation of the fraction of regulars who become users and the fraction of ad-blockers who become users.

## Rational Expectations Equilibrium

Note that n, the number of users of the website, is the aggregate number of regulars and ad-blockers who decide to become users. These individual decisions are influenced by the value v and their individual adviewing costs. However, v itself depends on n. We follow the standard assumption of rational expectations (see, e.g., Sheffrin 1996). That is, all potential users have a belief on $v ,$ the value of the website, and make their decisions. These decisions, in turn, result in a value for v which is consistent with the belief of the users.

## Website’s Problem

Every choice of $I _ { G } ,$ $a _ { b }$ and $a _ { r }$ will lead to a corresponding (i) equilibrium value of $v$ denoted by $v ( I _ { G } , a _ { b } , a _ { r } ) ;$ ; (ii) equilibrium number of ad-blockers who become users, denoted by $n _ { b } ( I _ { G } , a _ { b } , a _ { r } ) ;$ ; (iii) equilibrium number of regulars who become users, denoted by $n _ { r } ( I _ { G } , a _ { b } , a _ { r } ) ;$ and (iv) equilibrium value of the total traffic $n ,$ denoted by $n ( I _ { G } , a _ { b } , a _ { r } ) = n _ { b } ( I _ { G } , a _ { b } , a _ { r } ) + n _ { r } ( I _ { G } , a _ { b } , a _ { r } )$ . Thus, the equilibrium revenue for the website, denoted by $R ( I _ { G } , a _ { b } , a _ { r } )$ , can be expressed as follows:

$$
R (I _ {G}, a _ {b}, a _ {r}) = r [ n _ {b} (I _ {G}, a _ {b}, a _ {r}) \cdot a _ {b} + n _ {r} (I _ {G}, a _ {b}, a _ {r}) \cdot a _ {r} ].\tag{2}
$$

## 4. Analysis

In this section, we assess the impact of ad-block software on the website’s decisions and its revenue. To this end, we solve for the optimal decisions of the website both before and after the advent of ad-block software and also compare these decisions.

## 4.1. Optimal Decisions After the Advent of Ad-Blockers

The problem for the website after the advent of ad-block software is to maximize its equilibrium revenue, that ${ \mathrm { i } } s ,$

$$
\begin{array}{l} \max _ {I _ {G}, a _ {b}, a _ {r}} R (I _ {G}, a _ {b}, a _ {r}) \quad \text {s.t.} I _ {G} \in \{0, 1 \} \text {and} \\ a _ {r}, a _ {b} \in \{0 \} \cup [ a _ {\min}, \infty). \qquad (P _ {A f t e r}) \end{array}
$$

Let $I _ { G } ^ { * } , \ a _ { b } ^ { * } ,$ and $a _ { r } ^ { * } ,$ , respectively, denote the optimal values of $I _ { G } , a _ { b } ,$ , and $a _ { r } ,$ , and let $v ^ { * } : = v ( I _ { G } ^ { * } , a _ { b } ^ { * } , a _ { r } ^ { * } )$ . We first note some important properties of the optimal solution $( I _ { G } ^ { * } , a _ { b } ^ { * } , a _ { r } ^ { * } )$

• Property A.1 (Ad-Light Experience for White-Listers). The optimal ad-intensities are such that $a _ { b } ^ { * } \leq a _ { r } ^ { * }$

Intuition: We know that $C _ { b } \geq C _ { r } ,$ , that ${ \mathrm { i } } s ,$ , adblockers are more sensitive to ads than regulars. Therefore, the optimal ad-intensity for ad-blockers is less than that for regulars. Property A.1 is derived as part of the proof of Theorem 2 in Online Appendix A. <sup>□</sup>

Table 1. The Main Notation for Our Analysis

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $v$ </td><td>Equilibrium value of the website</td></tr><tr><td> $n$ </td><td>Equilibrium traffic of the website</td></tr><tr><td> $N$ </td><td>Size of the potential user population of the website</td></tr><tr><td> $\theta$ </td><td>Strength of the network effect</td></tr><tr><td> $v_0$ </td><td>Intrinsic value</td></tr><tr><td> $u_0$ </td><td>Net utility of the outside option</td></tr><tr><td> $B$ </td><td>Fraction of ad-block users among all potential users $\bar{B} := 1 - B$ .</td></tr><tr><td> $I_G$ </td><td>Indicator variable representing the gating decision:equals one if the website decides to gate, zero otherwise</td></tr><tr><td> $a_b$ </td><td>Ad-intensity for white-listers</td></tr><tr><td> $a_r$ </td><td>Ad-intensity for regulars</td></tr><tr><td> $a_{\min}$ </td><td>Minimum possible (nonzero) ad-intensity</td></tr><tr><td> $C_b$ </td><td>Maximum ad-viewing cost among ad-block users for an ad-intensity of one</td></tr><tr><td> $C_r$ </td><td>Maximum ad-viewing cost among regular users for an ad-intensity of one</td></tr><tr><td> $r$ </td><td>Ad revenue per user from an ad-intensity of one</td></tr></table>

Figure 3. An Ad-Block User with Ad-Viewing Cost Lower than $v - u _ { 0 }$ White-Lists the Website, Where v is the Value Users Obtain from the Website and $u _ { 0 }$ is the Net Utility of the Outside Option

![](/api/attachments/ZRKHUW2H/fulltext/images/6e418d95e14d64c0e0339977775fc2f602685a2ac93875860c4883d71e4b769b.jpg)  
Note. Similarly, a regular with ad-viewing cost lower than v u accesses the website.

• Property A.2 (Complete Market Penetration). $H a _ { b } ^ { * } > a _ { \mathrm { m i n } } ,$ then $v ^ { * } - a _ { b } ^ { * } C _ { b } = u _ { 0 }$ and $v ^ { * } - a _ { r } ^ { * } C _ { r } = u _ { 0 } ;$ that is, all regulars and ad-blockers become users.

Intuition: A website with a higher value v can advertise at a higher ad-intensity. If the optimal adintensities for both regulars and ad-blockers are both strictly greater than $a _ { \mathrm { m i n } } ,$ then the number of adblockers who become users and the number of regulars who become users are both proportional to the “value premium $\mathit { \Delta } ^ { \prime \prime } v - u _ { 0 }$ and inversely proportional to the respective ad-intensities. Thus, maximizing revenue is equivalent to maximizing v, which, in turn, is equivalent to maximizing the total traffic, n. Clearly, the latter goal is achieved if the website converts all ad-blockers and regulars to users. In turn, this objective is achieved if the website chooses the adintensities for ad-blockers and regulars such that the most ad-sensitive users of both these groups are indifferent between becoming users of the website or consuming the outside option $( { \mathrm { i . e . , } } v ^ { * } - a _ { b } ^ { * } C _ { b } = u _ { 0 }$ and $v ^ { * } - a _ { r } ^ { * } C _ { r } = u _ { 0 } )$ □

• Property A.3 (Rational Belief on Value). The optima solution satisfies the following relations: $0 \leq v ^ { * } - u _ { 0 } \overset { \cdot } { \leq } a _ { r } ^ { * } C _ { r }$ and if $I _ { G } = \mathrm { 1 } , \ v ^ { * } - \bar { u } _ { 0 } \leq a _ { b } ^ { * } \bar { C } _ { b }$

Intuition: In the optimal solution, the net utility $v ^ { * } - u _ { 0 }$ of the website cannot be negative because then the website would attract no traffic. Further, at the optimum, the net utility of the website for the most ad-sensitive users in each group (regulars and adblockers) cannot be strictly positive, because in that case the website can increase the corresponding adintensity slightly without losing a user. □

• Property A.4 (Equilibrium Traf<sup>fi</sup>c). The equilibrium number of regulars and the equilibrium number of adblockers who become users are given by the following expressions:

$$
\begin{array}{r l} & n _ {r} \big (I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*} \big) = N \bar {B} \big (v ^ {*} - u _ {0} \big) / \big (a _ {r} ^ {*} C _ {r} \big), \\ & n _ {b} \big (I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*} \big) = N B \big (v ^ {*} - u _ {0} \big) / \big (a _ {b} ^ {*} C _ {b} \big), i f I _ {G} ^ {*} = 1, a n d \\ & n _ {b} \big (I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*} \big) = N B, i f I _ {G} ^ {*} = 0. \end{array}
$$

Intuition: This result follows directly from Property A.3 and our model of uniformly distributed adviewing costs for regulars and ad-blockers. <sup>□</sup>

The revenue function $R ( I _ { G } , a _ { b } , a _ { r } )$ can now be computed using the expressions in Property A.4. Theorem 1 below states the optimal solution to Problem $P _ { A f t e r } ; \mathsf { a }$ proof of optimality is provided in Online Appendix A. To express the optimal solution, we define the following four parametric constants:

$$
\begin{array}{r l} & u _ {m} = v _ {0} + \theta - \frac {\theta B (B C _ {r} + \bar {B} C _ {b}) a _ {\mathrm{min}}}{\bar {B} (B \theta - a _ {\mathrm{min}} C _ {b}) + (B C _ {r} + \bar {B} C _ {b}) a _ {\mathrm{min}}}, \\ & a _ {g} = \max \biggl \{a _ {\mathrm{min}}, \frac {[ v _ {0} + \theta - \theta B - u _ {0} ] C _ {b} a _ {\mathrm{min}}}{C _ {r} (C _ {b} a _ {\mathrm{min}} - \theta B)} \biggr \}, \\ & \widehat {C} = \frac {v _ {0} + \theta - u _ {0}}{a _ {\mathrm{min}}}, \quad \mathrm{and} \\ & u _ {h} = v _ {0} - \frac {\theta B K _ {2}}{K _ {3} - K _ {2}}, \end{array}
$$

where $\begin{array} { r } { K _ { 2 } = \frac { \hat { B } a _ { \mathrm { m i n } } } { a _ { \mathrm { m i n } } C _ { r } - \theta \hat { B } } } \end{array}$ and $\begin{array} { r } { K _ { 3 } = \frac { ( B C _ { r } + \bar { B } C _ { b } ) a _ { \mathrm { m i n } } } { a _ { \mathrm { m i n } } C _ { b } C _ { r } - \theta ( B C _ { r } + \bar { B } C _ { b } ) } . } \end{array}$

For a chosen set of decisions $\left( I _ { G } , a _ { b } , a _ { r } \right)$ , the value premium offered by the website is $\phi ( I _ { G } , a _ { b } , a _ { r } ) =$ $v ( I _ { G } , a _ { b } , a _ { r } ) - u _ { 0 } .$ . By expressing the equilibrium value v in terms of the decisions (see Equation (13) in Online Appendix A), we obtain

$$
\phi (I _ {G}, a _ {b}, a _ {r}) = \frac {v _ {0} + \theta (1 - I _ {G}) B - u _ {0}}{1 - \theta \left(\frac {I _ {G} B}{C _ {b} a _ {b}} + \frac {1 - B}{C _ {r} a _ {r}}\right)}.
$$

The condition $\phi ( I _ { G } , a _ { b } , a _ { r } ) \geq 0 ,$ , which appears in the result below, can be naturally interpreted as the “survival condition” for the website, in the sense that the website does not receive any traffic if this condition fails

Theorem 1. An optimal solution of Problem $P _ { A f t e r }$ is as follows:

$\bullet \ I f \ C _ { b } , \ C _ { r } < \widehat { C } ,$ then

$$
\left(I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*}\right) = \left(1, \frac {v _ {0} + \theta - u _ {0}}{C _ {b}}, \frac {v _ {0} + \theta - u _ {0}}{C _ {r}}\right).
$$

$\bullet \ I f \ C _ { b } , \ C _ { r } > \widehat { C } ,$ then

$$
\begin{array}{l} \left(I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*}\right) \\ = \left\{ \begin{array}{l l} (0, a _ {\min}, a _ {\min}), & i f u _ {0} > u _ {h}, \phi (0, a _ {\min}, a _ {\min}) \geq 0, \\ (1, a _ {\min}, a _ {\min}), & i f u _ {0} \leq u _ {h}, \phi (1, a _ {\min}, a _ {\min}) \geq 0, \\ (0, 0, 0), & o t h e r w i s e. \end{array} \right. \end{array}
$$

$$
\begin{array}{l} \bullet \text {   If   } C _ {r} \leq \widehat {C} \leq C _ {b}, \text {   then   } \\ (I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*}) \\ = \left\{ \begin{array}{l} \left(0, a _ {\min}, \frac {v _ {0} + \theta - u _ {0}}{C _ {r}}\right), \\ \text {   if   } u _ {0} > u _ {m}, \phi \left(0, a _ {\min}, \frac {v _ {0} + \theta - u _ {0}}{C _ {r}}\right) \geq 0, \\ (1, a _ {\min}, a _ {g}) \\ \text {   if   } u _ {0} \leq u _ {m}, \phi (1, a _ {\min}, a _ {g}) \geq 0, \\ (0, 0, 0), \\ \text {   otherwise.   } \end{array} \right. \end{array}
$$

The three cases in this result signify three types of websites, categorized on the basis of the ad-viewing costs (or, equivalently, ad-sensitivities) of their user population. We elaborate below:

a. Low $C _ { b }$ and low $C _ { r } \ ( C _ { b } , \ C _ { r } < \widehat { C } )$ : This represents the class of websites whose target audience is not very sensitive to ads; for instance, websites that offer discounted deals. Because potential users of such websites are likely to white-list when required to do so, it is optimal to always gate ad-blockers. Moreover, the higher ad-tolerance of the users implies that the website can set relatively high ad-intensities (as compared with the two cases below) for both regulars and ad-blockers.

b. High $C _ { b }$ and high $C _ { r } \left( C _ { b } , \ C _ { r } > \widehat { C } \right)$ : This represents websites which cater to an ad-sensitive population, for example, senior business executives. An ad-sensitive audience necessitates a cautious gating decision: Gate ad-blockers only if the outside option is not very attractive. Understandably, the ad-intensity is at its lowest for both regulars and ad-blockers.

c. High $C _ { b }$ and low $C _ { r } \ ( \bar { C } _ { r } \leq \widehat { C } \leq C _ { b } )$ : In each of the previous two cases, ad-blockers and regulars were similar in that both groups had low (high) ad-sensitivity. This third case represents websites that face a wider variety of ad-sensitivities in their potential users. Here, when the outside option is attractive (i.e., when $u _ { 0 } > u _ { m } )$ , it is optimal not to gate ad-blockers. Further, because the ad-sensitivity of regulars is low, as in case (a) above, the optimal ad-intensity for these users is the same as in that case. When the outside option is not attractive (i.e., when $u _ { 0 } \leq u _ { m } ) .$ , it becomes optimal to gate ad-blockers. Under this possibility, because ad-blockers are highly ad-sensitive, their ad-intensity is the lowest possible. The gating of ad-blockers results in the website losing some of these potential users. To compensate, the website attracts regulars by offering them an ad-intensity that is lower than that in case (a) (it is easy to see that $\begin{array} { r } { a _ { g } \leq \frac { v _ { 0 } + \theta - u _ { 0 } } { C _ { r } } ) } \end{array}$

Note that the special case of $\theta = 0$ corresponds to the complete absence of the network effect. In this case, it is easy to verify that $u _ { h } = u _ { m } = v _ { 0 } ;$ therefore, from Theorem 1, the website’s optimal strategy is to always gate ad-block users. More generally, this strategy is attractive for websites that experience a low network effect, for example, forbes.com and businessinsider.com. On the other hand, a website such as facebook.com relies heavily on the network effect and would, therefore, refrain from always gating ad-block users.

Define $\begin{array} { r } { \beta = \frac { \theta } { v _ { 0 } + \theta } } \end{array}$ and $V _ { \mathrm { m a x } } = v _ { 0 } + \theta$ . Intuitively, $\beta$ represents the relative strength of the network effect and $V _ { \mathrm { m a x } }$ represents the maximum value that users can obtain from the website. The closed-form expressions in Theorem 1 help us establish the monotonicity of the ad-intensities with respect to an increase in the maximum value $V _ { \mathrm { m a x } }$ of the website, for a given gating decision and a given value of $\beta .$ . As $V _ { \mathrm { m a x } }$ increases keeping $\beta$ fixed, the website’s optimal revenue increases monotonically; surprisingly, the website may find it optimal to switch its gating decision from gating to no gating and then again back to gating.

Theorem 2 (Behavior of Ad-Intensities and Gating Decisions). As $V _ { \mathrm { m a x } }$ increases keeping β fixed, the optimal ad-intensities $( \hat { a } _ { b } ( I _ { G } ) , \hat { a } _ { r } ( I _ { G } ) )$ for a given gating decision $I _ { G }$ increase. Further, the website’s optimal revenue increases, and its optimal gating decision $( \hat { I } _ { G } ^ { * } )$ can first switch from gating to not gating and then again switch from not gating to gating.

Interestingly, a website may decide to stop gating with an increase in $V _ { \mathrm { m a x } } ,$ , under certain conditions. Consider, for instance, a website facing (i) a high relative network effect $( { \mathrm { i . e . , ~ } } \beta$ is high), (ii) a low adblocking rate (i.e., B is low), and (iii) a highly adsensitive target audience $( \mathrm { i . e . , } C _ { b }$ and $C _ { r }$ are high). As can been seen from Theorem 1, if the website gates, then a highly ad-sensitive user population makes it optimal to advertise at the minimum level both to regulars and to ad-blockers who white-list. Here, adblockers contribute little to the revenue of the website, because they constitute a small fraction of the potential user population; further, being ad-sensitive, most of them do not white-list. In this situation, an increase in $V _ { \mathrm { m a x } } ,$ , keeping $\beta$ fixed, can make it optimal for the website to stop gating, driven by the following benefits: (i) Because of a strong network effect, allowing ad-free access to ad-blockers increases the value of the website (over and above the increase due to a higher $V _ { \mathrm { m a x } } )$ . (ii) In turn, this increase in value enables the website to attract more regulars and also advertise to them at a higher intensity. Note that a further increase in $V _ { \mathrm { m a x } } ,$ keeping $\beta$ fixed, may make it optimal for the website to start gating again: If the increase in $V _ { \mathrm { m a x } }$ is substantial enough, then despite the loss of ad-blockers who refuse to white-list, the website can (a) further increase the advertising intensity for regulars and (b) generate revenue from ad-blockers who white-list.

To be able to assess the impact of ad-block software on the ad-intensities and the revenue of the website, we next analyze the website’s decisions before the advent of such software.

4.2. Optimal Ad-Intensity in the Pre-Ad-Block World After the advent of ad-block software, the publisher is able to discriminate between the two segments of potential users, namely, regulars and ad-blockers, who differ in their ad-viewing cost distributions. In the world prior to ad-block software, the publisher had no such tool to identify which segment a potential user belongs to and thus used a common ad-intensity for all potential users. Because it could be confusing to refer to the two segments as regulars and ad-blockers in the pre-ad-block world, we refer to these segments as low-cost and high-cost, respectively. The subscript r will refer to the low-cost segment and the subscript b will refer to the high-cost segment. Using the same notation as in the previous section, the pre-ad-blocking world corresponds to the website always gating, that is, $I _ { G } = 1 $ and choosing a common ad-intensity $a _ { b } = a _ { r } = a \left( \mathrm { s a y } \right)$ . Thus, the website’s revenue is $R ( 1 , a , a ) .$ , and we now have the following optimization problem, which we refer to as Problem $P _ { B e f o r e }$

$$
\max _ {a} R (1, a, a) \quad \mathrm{s.t.} a \in \{0 \} \cup [ a _ {\min}, \infty). \quad (P _ {B e f o r e})
$$

Let $a ^ { * }$ be the optimal ad-intensity in Problem $P _ { B e f o r e } .$ Let $v ^ { * } : = v ( 1 , a ^ { * } , a ^ { * } )$ (respectively $\dot { n ( 1 , a ^ { * } , a ^ { * } ) } )$ ) denote the corresponding equilibrium value (respectively equilibrium traffic) of the website. As in Section 4.1, we first present important properties that an optimal solution of Problem $P _ { B e f o r e }$ must satisfy and then use them to derive an optimal solution.

• Property B.1 (Ad-Intensities). Let $\begin{array} { r } { \hat { u } _ { 0 } = v _ { 0 } + \theta - \frac { \theta B \bar { \rho } } { 1 - B } , } \end{array}$ where $\begin{array} { r } { \rho = \frac { B ( \overline { { C } } _ { b } - C _ { r } ) } { C _ { b } } } \end{array}$ and $\bar { \rho } = 1 - \rho . \mathrm { ~ } I f \mathrm { ~ } a ^ { * } > a _ { \operatorname* { m i n } } ,$ then (i) if $u _ { 0 } \leq \hat { u } _ { 0 } ,$ , the optimal ad-intensity $a ^ { * }$ satisfies $v ^ { * } - a ^ { * } C _ { r } = u _ { 0 } ,$ (ii) otherwise, $v ^ { * } - C _ { b } a ^ { * } = u _ { 0 }$

Intuition: When the utility of the outside option is low, the website can hope to attract users even at a high ad-intensity. Driven by this, the optimal adintensity is such that the entire low-cost segment prefers the website to the outside option but only a fraction of the high-cost segment does so. When the outside option is attractive, the website is more conservative and uses a relatively lower ad-intensity, which ensures that both the low-cost and high-cost segments become users.

Property B.1 is derived as part of the proof of Theorem 3 in Online Appendix A. <sup>□</sup>

• Property B.2 (Rational Belief on Value). The optimal ad-intensity $a ^ { * }$ and the equilibrium value $v ^ { * }$ satisfy $0 \leq v ^ { * } - u _ { 0 } \leq a ^ { * } \check { C } _ { b }$

Intuition: The intuition of Property B.2 (as well as its proof) is similar to that of Property A.3 in Section 4.1. <sup>□</sup>

• Property B.3 (Equilibrium Traf<sup>fi</sup>c). The equilibrium number of users is

$$
n \big (1, a ^ {*}, a ^ {*} \big) = \left\{ \begin{array}{l} N (1 - B) \frac {\big (v ^ {*} - u _ {0} \big)}{a ^ {*} C _ {r}} + N B \frac {\big (v ^ {*} - u _ {0} \big)}{a ^ {*} C _ {b}}, \\ \text {if} 0 \leq v ^ {*} - u _ {0} \leq a ^ {*} C _ {r}, \\ N (1 - B) + N B \frac {\big (v ^ {*} - u _ {0} \big)}{a ^ {*} C _ {b}}, \\ \text {if} a ^ {*} C _ {r} \leq v ^ {*} - u _ {0} \leq a ^ {*} C _ {b}. \end{array} \right.\tag{3}
$$

Intuition: This result follows directly from Property B.2 and our model of uniformly distributed ad-viewing costs for high-cost and low-cost users. <sup>□</sup>

The revenue function $R ( 1 , a , a )$ can now be computed using the expression of $n ( 1 , a ^ { * } , a ^ { * } )$ in Equation (3). Theorem 3 below states the optimal solution to Problem $P _ { B e f o r e } ; \mathrm { ~ a ~ }$ proof of optimality is provided in Online Appendix A. To express the optimal solution, we define the following four parametric constants:

$$
\begin{array}{r l} & {\widehat {C} _ {r} = \frac {(v _ {0} + \theta \bar {B} - u _ {0}) C _ {b}}{a _ {\mathrm{min}} C _ {b} - \theta B},} \\ & {u _ {b} = v _ {0} + \theta \bar {B} + \frac {M _ {2}}{M _ {1}},} \\ & {\hat {a} = \frac {v _ {0} + \theta \bar {\rho} - u _ {0}}{C _ {r}},} \\ & {\hat {\hat {a}} = \frac {v _ {0} + \theta - u _ {0}}{C _ {b}},} \end{array}
$$

where $\begin{array} { r } { M _ { 1 } = \frac { \bar { \rho } } { C _ { r } } + \frac { B a _ { \mathrm { m i n } } } { \theta B - C _ { b } a _ { \mathrm { m i n } } } } \end{array}$ and $\begin{array} { r } { M _ { 2 } = \frac { \hat { \rho } \theta - \hat { B } a _ { \mathrm { m i n } } C _ { b } } { C _ { b } } } \end{array}$ . It is easy to show tha $\mathbf { \hat { a } } \geq \hat { \hat { a } }$ and $\widehat { C } \geq \widehat { C } _ { r }$ . As we did in Section 4.1, it is convenient to obtain the expression for the value premium, that is, $v ( a ) - u _ { 0 }$ , offered by the website, for a chosen ad-intensity a. Using the expression for the equilibrium value v (see Equations (23) and (27) in Online Appendix A), we have

$$
\begin{array}{l} v (a) - u _ {0} \\ = \left\{ \begin{array}{l l} \phi_ {l} (a) = \frac {a C _ {r} (v _ {0} - u _ {0})}{a C _ {r} - \theta \bar {\rho}}, & \text { if } C _ {b} \geq \widehat {C}, C _ {r} \geq \widehat {C} _ {r}, \\ \phi_ {h} (a) = \frac {a C _ {b} [ v _ {0} + \theta \bar {B} - u _ {0} ]}{a C _ {b} - \theta B}, & \text { otherwise }. \end{array} \right. \end{array}
$$

Parallel to the meaning of the condition $\phi ( I _ { G } , a _ { b } , a _ { r } ) \ge 0$ in the analysis of Problem $P _ { A f t e r }$ (Section 4.1), here the survival condition for the website (i.e., the website does not receive any traffic if this condition fails) is (i) $\phi _ { l } ( a ) \geq 0$ for a highly ad-sensitive user population and (ii) $\phi _ { h } ( a ) \geq 0$ , otherwise. We use these conditions in the result below.

Theorem 3. An optimal solution of Problem $P _ { B e f o r e }$ is as follows:

$I f C _ { b } , \ C _ { r } < \widehat { C } _ { \ l }$ , then

$$
a ^ {*} = \left\{ \begin{array}{l l} \hat {a}, & \text { if } u _ {0} \leq \hat {u} _ {0}, \phi_ {h} (\hat {a}) \geq 0, \\ \hat {\hat {a}}, & \text { if } u _ {0} > \hat {u} _ {0}, \phi_ {h} \Big (\hat {\hat {a}} \Big) \geq 0, \\ 0, & \text { otherwise }. \end{array} \right.
$$

$I f C _ { b } \geq \widehat { C } , \ C _ { r } \geq \widehat { C } _ { r } ,$ then

$$
a ^ {*} = \left\{ \begin{array}{l l} a _ {\min}, & \text { if } \phi_ {l} (a _ {\min}) \geq 0, \\ 0, & \text { otherwise }. \end{array} \right.
$$

$I f C _ { b } \geq \widehat { C } , C _ { r } < \widehat { C } _ { r } ,$ then

$$
a ^ {*} = \left\{ \begin{array}{l l} \hat {a}, & \text { if } u _ {0} \leq u _ {b}, \phi_ {h} (\hat {a}) \geq 0, \\ a _ {\min}, & \text { if } u _ {0} > u _ {b}, \phi_ {h} (a _ {\min}) \geq 0, \\ 0, & \text { otherwise }. \end{array} \right.
$$

As in Theorem 1, the three cases in the above result represent three categories of websites based on the ad-sensitivities of their potential users.

a. Low $C _ { b }$ and low $\bar { C _ { r } } \left( C _ { b } , \ C _ { r } < \widehat { C } \right)$ : When the outside option is low (high), the website uses a relatively high ad-intensity aˆ (resp., low ad-intensity $\hat { \hat { a } } )$ . Due to the low ad-sensitivity (i.e., high ad-tolerance) of the user population in this category, these intensities are higher than their corresponding values for the other two categories.

b. High $C _ { b }$ and high C $( C _ { b } \geq \widehat { C } , \ C _ { r } \geq \widehat { C } _ { r } )$ : Here, due to the high ad-sensitivity of the user population, it is optimal to keep the ad-intensity at its lowest.

c. High $C _ { b }$ and low $C _ { r } \ ( C _ { b } \overset { \cdot } { \geq } \widehat { C } , \ C _ { r } < \widehat { C } _ { r } ) .$ : In this case, the website serves users with a wider variety of ad-sensitivities. If the outside option is not attractive, then the website advertises at a high adintensity (aˆ); otherwise, it chooses the minimum adintensity.

Analogous to Theorem 2 (which was for Problem $P _ { A f t e r } )$ , the following result establishes the monotonicity of the optimal ad-intensity in Problem $P _ { B e f o r e }$ with respect to the maximum value $V _ { \mathrm { m a x } }$ of the website, for a given value of the relative strength $\beta$ of the network effect. The proof of this result is similar to that of Theorem 2 and, therefore, not provided for brevity.

Theorem 4 (Monotonicity of Ad-Intensity). Fix all other parameters except the website’s intrinsic value $v _ { 0 }$ and the strength of the network effect θ. As $V _ { \mathrm { m a x } } \left( i . e . , v _ { 0 } + \theta \right)$ increases keeping $\beta$ fixed $\begin{array} { r } { ( i . e . , \ \frac { \theta } { v _ { 0 } + \theta } \ f i x e d ) , } \end{array}$ , the optimal adintensity $a ^ { \dot { * } }$ increases.

## 4.3. Impact of Ad-Block Software on Publishers

In the previous section, we obtained the optimal decisions of the publisher before and after the advent of ad-block software. In this section, we use the analysis thus far to assess the impact on (i) the revenue of the website and (ii) the ad-intensities for the two segments of the population.

Theorem 5. (i) Under the optimal decisions derived in Section $^ { 4 , }$ the revenue of the website increases after the advent of ad-block software. That is,

$$
R \big (I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*} \big) \geq R \big (1, a ^ {*}, a ^ {*} \big).
$$

(ii) Compared with the ad-intensity before the advent of ad-block software, the ad-intensity for the high-cost segment decreases and the ad-intensity for the low-cost segment increases after the advent of ad-block software That $i s ,$

$$
a _ {b} ^ {*} \leq a ^ {*} \leq a _ {r} ^ {*}.
$$

The result in part (i) is consistent with the longstanding literature showing that vendors benefit when they are endowed with discriminatory power (see, $\mathrm { e . g . , }$ , Bhargava and Choudhary 2008, Wu and Chen 2008). The intuition behind part (i) is as follows. By definition, $a ^ { * }$ is the optimal ad-intensity of the website before the advent of ad-block software. Consider the following strategy of the website after the advent of ad-block software: $a _ { b } = a _ { r } = a ^ { * } , \ I _ { G } = 1$ In following this strategy, the website continues to keep the same ad-intensity after the advent of adblock software as before and gates all ad-blockers. Because the ad-intensity is the same before and afte the advent of ad-block software and the website gates all ad-blockers, any potential user who became a user in the pre-ad-block world also becomes a user in the post-ad-block world. Thus, the maximum revenue obtained by the publisher before the advent of adblock software is a lower bound on the optima revenue of the website after the advent of ad-block software. This finding is consistent with that of a recent empirical investigation at Forbes (DVorkin 2016) in which ad-blockers were gated and offered an ad-light experience, whereas regulars were offered a higher ad-intensity. The main finding was that, as compared with the earlier setting where ad-blockers were not gated. Forbes was able to deliver 63 million additional ad impressions in two weeks to those users who agreed to white-list, without significantly affecting the total traffic to the website. To put it succinctly, an ad-blocker enables a website to discrimi nate its users on the basis of their ad-sensitivity. This discriminatory power is exploited by the website to increase its revenue.

The intuition for part (ii) of the Theorem 5 is this: Because the two segments of the population differ in terms of their ad-viewing cost distributions, the ability to discriminate between their ad-intensities, in the world with ad-block software, makes it optimal to more aggressively advertise to the low-cost segment and to less aggressively advertise to the high-cost segment than before.

Both Problems $P _ { B e f o r e }$ and $P _ { A f t e r }$ imposed a lower bound, namely, $a _ { \mathrm { m i n } } ,$ , on the ad-intensities. In the absence of this lower bound, that is, when $a _ { \mathrm { m i n } } = 0 ,$ , the optimal solutions of these problems simplify significantly. Using the same notation as in our analysis above, the optimal solution of $P _ { A f t e r }$ when $a _ { \mathrm { m i n } } = 0$ is

$$
\left(I _ {G} ^ {*}, a _ {b} ^ {*}, a _ {r} ^ {*}\right) = \left(1, \frac {v _ {0} + \theta - u _ {0}}{C _ {b}}, \frac {v _ {0} + \theta - u _ {0}}{C _ {r}}\right).
$$

And the optimal solution of Problem $P _ { B e f o r e }$ is

$$
a ^ {*} = \left\{ \begin{array}{l l} \hat {a}, & \text { if } u _ {0} <   \hat {u} _ {0}, \\ \hat {\bar {a}}, & \text { if } \hat {u} _ {0} \leq u _ {0} \leq v _ {0} + \theta \bar {B}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

The key results of our analysis continue to hold when $a _ { \mathrm { m i n } } = 0$ : the website’s revenue increases, white-listers receive an ad-light experience, and regulars are offered a higher ad-intensity in the post-ad-block world.

## 4.4. Comparing Optimal Ad-Intensities in the Pre- and Post-Ad-Block Worlds

Using the optimal solutions in Theorems 1 and 3, we now compare the ad-intensities before and after the advent of ad-block software. Figure 4 is a pictorial comparison of the ad-intensities in the optimal solutions to Problems $P _ { A f t e r }$ and $P _ { B e f o r e }$ . As shown here, for both of these problems, the $( C _ { b } , C _ { r } )$ -space can be decomposed into three regions—I, II, and III—that broadly represent the websites that serve users with low, high, and moderate ad-sensitivities, respectively. In the pre-ad-block world, the websites belonging to Region II found it optimal to keep the ad-intensity at its minimum level, that is, $a _ { \mathrm { m i n } }$ . In the post-ad-block world, the discriminatory power bestowed by adblockers enables the choice of a higher ad-intensity for regular users with $C _ { b } \geq \widehat { C } , \ C _ { r } \in [ \widehat { C } _ { r } , \ \widehat { C } ]$ . Thus, Region II of the pre-ad-block world shrinks in the post-ad-block world (or, equivalently Region III expands). In Region I, where the ad-intensities are always set higher than $a _ { \mathrm { m i n } } .$ , ad-block users receive a lower ad-intensity in the post-ad-block world compared with that in the pre-ad-block world. On the other hand, regular users receive a higher ad-intensity in the post-ad-block world compared with that in the pre-ad-block world.

Thus far, our focus was on the impact of ad-block software on the website’s revenue. We now examine the impact on consumer surplus and social surplus.

## 4.5. Welfare Analysis

We define consumer surplus as the total expected net utility over all the consumers, that is, the sum of the net utilities of all the consumers. Social surplus is defined as the sum of consumer surplus and the revenue of the website. The main takeaway from our analysis in this section is an argument in favor of a website providing niche content to ensure that both the website and the consumers of its content benefit We now proceed with the analysis.

For simplicity of exposition, we focus on the case when the minimum ad-intensity threshold is low, specifically, $\begin{array} { r } { a _ { \mathrm { m i n } } \le \frac { v _ { 0 } + \theta - u _ { 0 } } { C _ { b } } } \end{array}$ . From our analysis of Prob lem $P _ { A f t e r }$ in Section 4, we know that, in this case, $a _ { b } ^ { * } =$ $\begin{array} { r } { \frac { v _ { 0 } + \theta - u _ { 0 } } { C _ { h } } , ~ a _ { r } ^ { * } = \frac { v _ { 0 } + \theta - u _ { 0 } } { C _ { r } } , ~ n = N , } \end{array}$ , and $v = v _ { 0 } + \theta ,$ . Let $C S _ { A f t e r }$ denote the consumer surplus after the advent of ad-block software. An ad-block user with an adsensitivity of $\tilde { c } _ { b }$ receives a net utility of $v _ { 0 } + \theta - a _ { b } ^ { * } \tilde { c } _ { b } .$ Similarly, a regular user with an ad-sensitivity of $\tilde { c } _ { r }$ receives a net utility of $v _ { 0 } + \theta - a _ { r } ^ { * } \tilde { c } _ { r }$ . Because $\tilde { c } _ { b } \sim$ $U [ 0 , \ a _ { b } ^ { * } C _ { b } ]$ and $\tilde { c } _ { r } \sim \dot { U } [ 0 , \ a _ { r } ^ { * } C _ { r } ] .$ , we have

$$
C S _ {A f t e r} = N B \bigg [ v _ {0} + \theta - \frac {a _ {b} ^ {*} C _ {b}}{2} \bigg ] + N \bar {B} \bigg [ v _ {0} + \theta - \frac {a _ {r} ^ {*} C _ {r}}{2} \bigg ].
$$

Using $\begin{array} { r } { a _ { r } ^ { * } = \frac { v _ { 0 } + \theta - u _ { 0 } } { C _ { r } } } \end{array}$ and $\begin{array} { r } { a _ { b } ^ { * } = \frac { v _ { 0 } + \theta - u _ { 0 } } { C _ { b } } } \end{array}$ we get

$$
C S _ {A f t e r} = \frac {N (v _ {0} + \theta + u _ {0})}{2}.\tag{4}
$$

Let $C S _ { B e f o r e }$ denote the consumer surplus before the advent of ad-block software. Using an analysis similar to that above, we have

$$
C S _ {B e f o r e} = \left\{ \begin{array}{c} \frac {N \bar {\rho} (v _ {0} + \theta \bar {\rho} + u _ {0}) + 2 N B \rho u _ {0}}{2}, \\ \text {if} u _ {0} \leq \hat {u} _ {0}, \\ \frac {N \bar {B} [ 2 C _ {b} (v _ {0} + \theta) - C _ {r} (v _ {0} + \theta - u _ {0}) ] + C _ {b} N B (v _ {0} + \theta + u _ {0})}{2 C _ {b}}, \\ \text {otherwise.} \end{array} \right.\tag{5}
$$

For more details on the expressions in Equation (5), we refer the reader to the proof of the following result, which characterizes the increase in consumer surplus after the advent of ad-block software.

Theorem 6. After the advent of ad-block software, consumer and social surplus increase if and only if $u _ { 0 } \leq \hat { u } _ { 0 }$ Further, under this condition, the surplus of both consumer segments, namely, ad-block users and regular users, increases.

We now discuss the intuition behind this result. In the pre-ad-block world, the publisher, who had no tool to segment users based on their ad viewing costs, used a single ad-intensity for all potential users. Not surprisingly, this common ad-intensity is too high for some high-cost potential users, who, therefore, choose not to become users of the website and instead consume the low-utility outside option $( u _ { 0 } \le \hat { u } _ { 0 } )$ However, after the advent of ad-block software, the website is able to discriminate by offering a lower adintensity to such high-cost users, thereby converting them into users of the website and leading to an increase in the total traffic of the website. This increases consumer surplus in two ways: First, all the new users (the users of the website after the advent of ad-block software but not before) obtain a higher net utility compared with the low utility from the outside option, which they were consuming earlier. Second, the increase in traffic increases the value of the website; therefore, the old users (the users of the website both before and after the advent of ad-block software) also obtain a higher net utility from the website. In this manner, consumer surplus increases after the advent of ad-block software when the outside option has low net utility. Because ad-block users receive an ad-light experience in the post-ad-block world, it is intuitive that they are better-off. Interestingly, regular users too are better-off despite being subject to a higher adintensity than that in the pre-ad-block world: the discrimination between the user segments in the postad-block world results in higher traffic, which in turn increases the value of the website because of the network effect. For regular users, this improvement in the value of the website exceeds the disutility from a higher adintensity, leading to a net increase in their surplus.

Figure 4. (Color online) A Pictorial Comparison of the Ad-Intensities in the Optimal Solutions to Problems $P _ { A f t e r }$ and $P _ { B e f o r e }$  
![](/api/attachments/ZRKHUW2H/fulltext/images/9f502f79e4a7eccbafaa45e4a518c89aafd53fa36b3a94b370a9c312bf3c8e99.jpg)

When the outside option offers a high-enough net utility $\left( u _ { 0 } > \hat { u } _ { 0 } \right)$ , then the ad-intensity in the world prior to ad-blockers is itself quite low (see Theorem 3). After the advent of ad-block software, although the website is able to decrease the ad-intensity for highcost users, this decrease is not significant given that the ad-intensity was already low. On the other hand, the ad-intensity increases significantly for low-cost users; although the website is able to retain these users by carefully increasing their ad-intensity, their consumer surplus decreases because of this increase. Overall, the loss of consumer surplus because of the (significant) increase in the ad-intensity for low-cost users more than offsets the gain in consumer surplus because of the (small) decrease in the ad-intensity for high-cost users. As a consequence, the total consumer surplus decreases.

![](/api/attachments/ZRKHUW2H/fulltext/images/a8cf080edc5e4cededd4bae2b587b5d70012f5272b98f2250d07a6cfb4398ddc.jpg)

We now examine the social surplus. Let $W _ { B e f o r e }$ and $W _ { A f t e r } ~ ( \mathrm { r e s p . } , R _ { B e f o r e }$ and $R _ { A f t e r } )$ denote the social surplus (resp., optimal revenue of the website) before and after the advent of ad-block software, respectively. We know that

$$
R _ {B e f o r e} = \left\{ \begin{array}{l l} \frac {N r \bar {\rho} (v _ {0} + \theta \bar {\rho} - u _ {0})}{C _ {r}}, & \text { if } u _ {0} \leq \hat {u} _ {0}, \\ \frac {N r (v _ {0} + \theta - u _ {0})}{C _ {b}}, & \text { otherwise }, \end{array} \right.\tag{6}
$$

and

$$
R _ {A f t e r} = \frac {N r \bar {\rho} (v _ {0} + \theta - u _ {0})}{C _ {r}}.\tag{7}
$$

The expressions for $W _ { B e f o r e }$ and $W _ { A f t e r }$ can be obtained using Equations (4), (5), (6), and $( 7 )$ . Because both the revenue of the website and the consumer surplus increase in the post-ad-block world when $u _ { 0 } \leq \hat { u } _ { 0 } ,$ it follows immediately that the social surplus increases under this condition. In the reverse direction (i.e., when $u _ { 0 } \geq \hat { u } _ { 0 } )$ , although consumer surplus decreases in the post-ad-block world (as discussed above), an attractive outside option for consumers compels the website to choose a low ad-intensity, thereby limiting the increase in its revenue. Consequently, the increase in the website’s revenue is not enough to compensate for the loss of consumer surplus, leading to a net decrease in social surplus.

In summary, relative to the pre-ad-block world, adblock users (white-listers) receive a lower ad-intensity in the post-ad-block world, whereas regular users receive a higher ad-intensity (Theorem 5, part (ii)). As long as the utility of the outside option is below the threshold $\hat { u } _ { 0 } ,$ the surplus of both consumer segments (ad-block users and regular users) as well as the social surplus increase in the post-ad-block world (Theorem 6); the website’s revenue also improves (Theorem 5, part (i)).

The expressions for $R _ { B e f o r e }$ and $R _ { A f t e r }$ in Equations (6) and (7) help us establish the following result.

Corollary 1. Keeping the relative strength of the network effect β fixed, the rate of increase in the website’s optimal revenue with an increase in its maximum value $\dot { V } _ { \mathrm { m a x } }$ is higher in the post-ad-block world, that is, $\frac { \partial R _ { A f t e r } } { \partial V _ { \mathrm { m a x } } } \geq \frac { \partial R _ { B e f o r e } } { \partial V _ { \mathrm { m a x } } } .$ Further, equality holds for $B = 0$ and $B = 1$

In both the pre- and post-ad-block worlds, the increase in the website’s value resulting from an increase in $V _ { \mathrm { m a x } }$ while keeping $\beta$ fixed, enables it to advertise at a higher ad-intensity. However, because of the discriminatory power endowed by ad-blockers in the post-ad-block world, the website can customize the ad-intensity for each of the two user segments, that is, regulars and ad-blockers. This is in contrast to the pre-ad-block world, where a common adintensity had to be chosen for the entire user population. This added advantage results in a relatively higher rate of increase in revenue with an increase in $V _ { \mathrm { m a x } }$ in the post-ad-block world. Clearly, the ability to individually customize the ad-intensities for the two segments can lead to a significant benefit only if both the segments are of sufficient size; that is, the adblocking rate B is sufficiently away from zero and one.

Note that increasing $V _ { \mathrm { m a x } } ,$ while keeping $\beta$ fixed, implies that $v _ { 0 }$ increases. A website can increase v by improving the quality of its content or service and/or by providing niche content. Thus, Corollary 1 implies that the website has a higher incentive to undertake such endeavors post the advent of ad-block software. Further, current ad-blocking rates are fractional for most websites, thus making the effort to increase $v _ { 0 }$ more potent. Finally, from Equations (4) and (7), we also know that both consumer surplus and the website’s revenue increase with $v _ { 0 } ,$ , leading to an increased social surplus. In summary, content managers can view the provision of better/niche content or service as a curative response to ad-block software, one that is beneficial both to the website and its potential consumers and, therefore, generates more social value.

Our analysis assumes that ad-block users do not incur any cost for white-listing the website. However, it is conceivable that users incur or perceive a positive white-listing cost; for example, users may feel annoyed when asked to white-list despite having an ad-blocker installed or non–tech-savvy users may find it difficult to properly white-list the website. In practice, websites try to reduce this cost by providing instructions on how to white-list and by explaining to users that ads are necessary to finance the creation of highquality content. As long as the white-listing cost is sufficiently low, it is easy to show that the main results of our analysis—that the website’s revenue increases after the advent of ad-blockers and that consumers also benefit under a low outside option—continue to hold

Our analysis thus far assumes that the website’s gating decision is binary: either allow ad-free access to all ad-blocker users or require all these users to white-list to gain access. With the aim of further increasing the website’s revenue, we now examine a generalization in which only a fraction of the ad-block users are gated.

## 5. Improving Revenue Further: Selective Gating

Let p denote the fraction of ad-blockers who are gated. The remaining 1 p fraction of ad-blockers are not gated, that is, are allowed to access the website without disabling the ad-block software. We refer to p as the gating intensity and to this strategy as selective gating. There are several ways in which selective gating can be implemented, for example, tossing a coin (with success probability p) at each user visit to decide whether to gate, or randomly choosing a p fraction of users for gating. We will refer to the strategy in Section 4 of gating all or none of the potential users as integral gating, to contrast it with selective gating. Under selective gating, the sequence of events shown in Figure 2 of Section 3 will only change as follows: the indicator $I _ { G } = 1$ is replaced by $p$ and the indicator $I _ { G } = 0$ is replaced by $( 1 - p )$ . Clearly, the equilibrium value of the website v will now be different from that in the case of integral gating $( { \mathrm { i . e . , ~ } } I _ { G } \in \{ 0 , 1 \} )$ . Thus, the decisions of the users change through the change in v. A regular user with an ad-sensitivity of c˜ becomes a user of the website if $v - a _ { r } \tilde { c } _ { r } \geq u _ { 0 }$ . An ad-blocker with an ad-sensitivity of $\tilde { c } _ { b }$ becomes a user of this website under the following conditions: (a) if this user is selected for gating (with probability p) and $v - a _ { b } \tilde { c } _ { b } \geq u _ { 0 } ,$ , (b) if this user is not selected for gating (with probability $1 - p )$ and $v \geq u _ { 0 } ;$ in this case, $\tilde { c } _ { b }$ is inconsequential.

Our goal in this section is to identify the conditions under which the use of selective gating can lead to a substantial increase in the website’s revenue, relative to integral gating. Recall from Theorem 1 that our analysis in Section 4 partitioned the website’s decisions into three cases, based on the ad-viewing cost parameters $C _ { b }$ and $C _ { r } \colon \mathrm { ( i ) } \ C _ { b } , \ C _ { r } < \widehat { C } , \mathrm { ( i i ) } \ C _ { b } , \ C _ { r } > \widehat { C } ,$ and (iii) $C _ { r } \leq \widehat { C } \leq C _ { b }$ . In the first case, using an analysis similar to that in the proof of Theorem 1, we have $p ^ { * } = 1$ that is, the optimal gating intensity under selective gating is naturally integral. Thus, in this case, selective gating does not affect the revenue of the website.

From the other two cases (namely, (ii) and (iii)), for brevity, we only discuss case (ii) in this section, namely,

$C _ { b } , \ C _ { r } > \widehat { C }$ . For this case, using an analysis similar to that in the proof of Theorem 1, we can show that, for any gating intensity $p \in [ 0 , 1 ] , a _ { b } ^ { * } = a _ { r } ^ { * } = a _ { \operatorname* { m i n } }$ . Thus, we only need to obtain the optimal gating intensity $p ^ { * }$ . Let $R ( p , a _ { \mathrm { m i n } } , a _ { \mathrm { m i n } } )$ represent the revenue of the website when gating intensity is $p .$ . Therefore, the website solves the following problem:

$$
\max R (p, a _ {\min}, a _ {\min}) \quad \text {s.t.} p \in [ 0, 1 ]. \quad (P _ {S e l e c t})
$$

Let $p ^ { * }$ be the optimal gating intensity and let $v ^ { * } : = v ( p , a _ { \mathrm { m i n } } , a _ { \mathrm { m i n } } )$ . Let $n ( p ^ { * } , a _ { \mathrm { m i n } } , a _ { \mathrm { m i n } } )$ represent the equilibrium traffic received by the website. Similar to Sections 4.1 and 4.2, we first present some important properties that an optimal solution must satisfy and then use them to derive the optimal solution.

• Property C.1 (Rational Belief on Value). The optima gating intensity $p ^ { * }$ is such that the equilibrium value $v ^ { * }$ satisfies $0 \leq v ^ { * } - u _ { 0 } \leq a _ { \mathrm { m i n } } C _ { r }$

Intuition: For the website to attract a positive traffic, we should necessarily have $v ^ { * } \geq u _ { 0 }$ . Further, because our analysis here is for $C _ { b } , C _ { r } > \widehat { C } ,$ , the website caters to a highly ad-sensitive population. Thus, even at the minimum ad-intensity $a _ { \mathrm { m i n } } ,$ the net utility of the most ad-sensitive regular user is at most that offered by the outside option, that is, $v ^ { * } - a _ { \mathrm { m i n } } C _ { r } \leq u _ { 0 }$ □

• Property C.2 (Equilibrium Traf<sup>fi</sup>c). The equilibrium number of users is

$$
\begin{array}{r} n (p ^ {*}, a _ {\min}, a _ {\min}) = \frac {N B (v ^ {*} - u _ {0}) p ^ {*}}{a _ {\min} C _ {b}} + (1 - p ^ {*}) N B \\ + \frac {N (1 - B) (v ^ {*} - u _ {0})}{a _ {\min} C _ {r}}. \end{array}\tag{8}
$$

Intuition: This result follows directly from Property C.1 and our model of uniformly distributed adviewing costs for ad-blockers and regulars. <sup>□</sup>

The revenue function $R ( p , a _ { \mathrm { m i n } } , a _ { \mathrm { m i n } } )$ can now be computed using Equation (8). It is straightforward to verify that $R ( p , a _ { \mathrm { m i n } } , a _ { \mathrm { m i n } } )$ is a concave function of $p$ (the details of the proof of concavity are provided in Online Appendix A). When $R ^ { \prime } ( 0 ) \overset { \cdot } { \geq } 0$ and $R ^ { \prime } ( 1 ) \leq 0 ,$ let pˆ be such that $R ^ { \prime } ( { \hat { p } } ) = 0 ;$ clearly, such a value exists. Therefore, the optimal gating intensity is given by

$$
p ^ {*} = \left\{ \begin{array}{l l} 0, & \text {if R^{\prime} (0) <   0 ,} \\ 1, & \text {if R^{\prime} (1) > 0 ,} \\ \hat {p}, & \text {if R^{\prime} (0)\geq 0 , R^{\prime} (1)\leq 0 .} \end{array} \right.
$$

Most websites already have the infrastructure in place to randomly select users for $\mathrm { A } / \mathrm { B }$ testing. The same infrastructure can be used for randomly selecting adblock users for gating. Further, the idea of selective gating can perhaps be extended to the case when the website offers a subscription option (e.g., by offering this option to a randomly selected $p$ fraction of adblock users). Along similar lines, the idea of randomization in selective gating can be extended for ad-intensities too. In that case, the ad-intensities can be viewed as the average ad-intensities that users experience on a particular website over time.

We now proceed to examine the benefit of selective gating for the website.

## Illustrating the Bene<sup>fi</sup>t of Selective Gating

To assess the benefit of selective gating, it is instructive to first understand the behavior of the optimal gating intensity $p ^ { * }$ . To illustrate this, we fix the following values: $\dot { C _ { r } } = 1 0 0 , C _ { b } = 2 0 0 , u _ { 0 } = 5 0 , a _ { \mathrm { m i n } } = 1$ $N = 1 , 0 0 { \bar { 0 } } , 0 0 0 , r = 1 .$ , and $V _ { \mathrm { m a x } } = 1 0 0$ . Figure $5 ( \mathrm { a } )$ plots the optimal gating intensity $( p ^ { * } )$ with respect to the relative strength of network effect $\beta = \theta / ( \bar { v } _ { 0 } + \theta )$ and the ad-blocking rate B. Our main observations, which can be viewed as recommendations on the optimal gating intensity for the website based on the relative strength of its network effect and the ad-blocking rate of its user population, are discussed below:

• From the lower half of the figure, we note the following:

When the relative strength of the network effect is low, it is optimal to always gate ad-blockers for all values of the ad-blocking rate, that is, $p ^ { * }$ is one for all values of B.

0 $\mathrm { A s }$ the ad-blocking rate increases, the region in which $p ^ { * }$ is one expands.

The gating of ad-blockers affects a website in two ways: On the one hand, if an ad-blocker agrees to white-list the website, then revenue may be generated from this user who is otherwise a free-rider. On the other hand, if the ad-blocker does not white-list and leaves, then the resulting negative externality can adversely affect the user base of the website. The extent of this externality depends on the strength of the network effect for the website. Thus, when the relative strength of the network effect is low, the latter force is weak relative to the former and, as a result, it becomes optimal to always gate ad-blockers. Moreover, as the ad-blocking rate increases and ad-blockers constitute a larger fraction of the userbase, the conversion of ad-blockers to white-listers becomes even more attractive for the website, resulting in the expansion of the region in which $p ^ { * }$ equals one.

• The upper-left quadrant shows that a near-zero gating intensity is optimal when the ad-blocking rate is low but the relative strength of the network effect is high. Both these features act in tandem toward a low gating intensity: although the strong network effect dissuades the website from gating ad-blockers, the low ad-blocking rate means that there is also no compelling need to react to ad-blockers.

Figure 5. (Color online) The Benefit of Selective Gating is Zero When the Optimal Gating Intensit $\boldsymbol { p } ^ { * }$ is Naturally Integral and is High for Those Combinations of $\beta$ (the Relative Strength of the Network Effect) and B (the Fraction of Ad-Block Users) for Which $p ^ { * }$ is Close to 0.5  
![](/api/attachments/ZRKHUW2H/fulltext/images/7c5cf2961e477e82b65d5c1b2d069bcf2836addaf3ffe1a8e10c77cbc577abda.jpg)

• In the upper-right quadrant, where the relative strength of the network effect is high and the adblocking rate is $\mathrm { \ h i g h } ,$ , a fractional gating intensity is optimal. Here the tradeoff is healthy: although the strong network effect keeps the website from gating ad-blockers aggressively, the high ad-blocking rate also necessitates some action toward ad-blockers. This creates a fertile situation for selective gating to realize its potential, resulting in a fractional value of $p ^ { * }$ . Further, as expected, $p ^ { * }$ reduces as the network effect becomes relatively stronger.

Another interesting observation from Figure 5(a) is that when the ad-blocking rate is low, the optimal gating intensity is largely integral, that is, $p ^ { * }$ is either zero or one. This perhaps explains why selective gating is not yet common in practice: Ad-blocking rates are still quite modest; in the United States, for example, it is currently around 18%. As ad-blockers become prevalent, one can expect to see an increase in the use of the selective-gating strategy.

## Bene<sup>fi</sup>t of Selective Gating Over Integral Gating

Having obtained the website’s optimal revenue under both integral (Section 4) and selective gating, we can now examine the percentage increase in revenue from the latter. For our chosen values, it can be verified that the optimal ad-intensities are $a _ { b } ^ { * } = a _ { r } ^ { * } = a _ { \operatorname* { m i n } }$ under both integral and selective gating. Let

$$
\Theta_ {S e l e c t} = \frac {R (p ^ {*} , a _ {\mathrm{min}} , a _ {\mathrm{min}}) - R (I _ {G} ^ {*} , a _ {\mathrm{min}} , a _ {\mathrm{min}})}{R (I _ {G} ^ {*} , a _ {\mathrm{min}} , a _ {\mathrm{min}})} \times 1 0 0.
$$

Figure 5(b) plots the logarithm (base 10) of $\Theta _ { S e l e c t }$ with respect to the relative strength $\beta$ of the network effect and the ad-blocking rate B. We now discuss our

![](/api/attachments/ZRKHUW2H/fulltext/images/25f9e04c3ac5cc53c40f1913f28827b39098a17f49790a7de6a05bc824c39518.jpg)  
observations in this figure using additional information from Figure 5(a). Obviously, the benefit of selective gating is zero where the optimal gating intensity $p ^ { * }$ is naturally integral. The benefit is highest in the region where $p ^ { \check { * } }$ is around 0.5 (and, therefore, farthest from the integral extreme values). This is precisely the region in which both $\beta$ and B are high. As is clear from our discussion above, concerns over the use of adblockers are particularly important for websites that face both a high relative network effect and a high fraction of ad-block users—these are the websites that can benefit most from selective gating.

## Improvement in Revenue

In Theorem 5, we established that, under the optimal decisions derived in Section 4, the revenue of the website increases after the advent of ad-blockers. Although that result assumed an integral gating decision, selective gating further increases the website’s revenue. Recall from Section 4.2 that the website’s revenue in the pre-ad-block world corresponds (in the post-ad-block world) to the website gating all potential users and using a common ad-intensity $a _ { b } = a _ { r } = a$ . Under our chosen values, using Theorem 3 and the discussion earlier in this section, the website’s revenue in the post-ad-blocker (resp., pre-ad-blocker) world is $R ( p ^ { * } , \bar { a } _ { \operatorname* { m i n } } , a _ { \operatorname* { m i n } } )$ (resp., $R ( 1 , a _ { \mathrm { m i n } } , a _ { \mathrm { m i n } } ) )$ ). Thus, the percentage increase in the website’s revenue after the advent of ad-blockers is

$$
\Upsilon_ {R e v} = \frac {R (p ^ {*} , a _ {\mathrm{min}} , a _ {\mathrm{min}}) - R (1 , a _ {\mathrm{min}} , a _ {\mathrm{min}})}{R (1 , a _ {\mathrm{min}} , a _ {\mathrm{min}})} \times 1 0 0.
$$

Figure 6 plots $\Upsilon _ { R e v }$ with respect to ad-blocking rate B and relative strength $\beta$ of the network effect.

When the network effect is relatively weak, the optimal gating intensity in the post-ad-block world is naturally close to one (recall our earlier discussion for the lower half of Figure 5(a)); therefore, there is little or no increase in revenue. When the network effect is relatively strong, the percentage increase in revenue peaks for a moderate ad-blocking rate B (close to 0.5); this is when the website can fully exploit the ability endowed by ad-blockers to discriminate between the two segments, namely, regulars and ad-blockers.

## 6. Robustness Check

## and Recommendations

We now analyze the following additional features as extensions to our base model in Section 3:

• Heterogeneous profitability of the two user groups, namely, ad-block users and regular users to the website

• The offering of a paid, ad-free subscription option by the website (in addition to the option of viewing ad-supported free content by white-listing the website)

• Endogenous adoption of ad-blockers by users in response to the website’s strategy $( \mathrm { i . e . , }$ its chosen adintensities for white-listers and regular users)

• Negative externality (congestion cost) imposed on the website by an increase in traffic

We add each of these features, one at a time, to our base model and establish the validity of our main conclusions: (i) the revenue of the website increases in the post-ad-block world relative to that in the pre-adblock world; (ii) ad-block users receive an ad-light experience in the post-ad-block world relative to the pre-ad-block world; and (iii) the social surplus can either increase or decrease in the post-ad-block world relative to that in the pre-ad-block world

Figure 6. (Color online) When the Relative Strength of the Network Effect is High, the Percentage Increase in the Website’s Revenue in the Post-Ad-Blocking World Peaks at a Moderate Ad-Blocking Rate B  
![](/api/attachments/ZRKHUW2H/fulltext/images/210d0c7e9a88c44bf0c9d7770a7ab8ca702b47a66e728d397f290b5122bf2016.jpg)  
Note. When the relative strength of the network effect is low, there is little or no increase in revenue.

Recall that, in our base model, the domain for the ad-intensities $a _ { r }$ and $a _ { b }$ (decisions of the website) for, respectively, regular users and white-listers is 0 $[ a _ { \mathrm { m i n } } , \infty ]$ . That is, a (resp., a ) is either zero or at least $a _ { \mathrm { m i n } }$ . For simplicity of exposition, we present the analysis of the above extensions under the assumption $a _ { \mathrm { m i n } } = 0$ . We discuss the setting of subscription option here, and the analysis of rest of the features can be found in Online Appendix B.

Subscription Option. Our basic model of Section 3 considers a website that operates only on advertising revenue. Although this is indeed the case for most websites on the internet, there are websites that also offer a paid subscription option to users for viewing ad-free content. To ad-block users such websites typically give an additional option of subscription after gating them. In this extension, we model a website that offers its users both adsupported free content and ad-free paid content (subscription).

We assume that the website charges a subscription fee f per visit (a decision for the website) for its ad-free content (if the subscription fee is charged periodically, say per year, then it can be appropriately amortized to a per-visit fee). Figure 7 depicts the sequence of events when the website offers the subscription option. If the website decides to gate an ad-block user, then that user has the following three options: (i) white-list the website, (ii) subscribe to the website, or (iii) leave the website and consume the outside option. The website decides the optimal subscription fee f along with the optimal ad-intensities $a _ { b }$ and $a _ { r } .$ . In the pre-ad-block world, the website decides the optimal subscription fee f and the optimal ad-intensity a for the entire user population. The analysis of this extension is in Online Appendix B.2.

Next, we discuss the recommendations offered by our analysis for publishers, web browsers, and policy makers.

## 6.1. Recommendations for Publishers, Browsers, and Policy Makers

Publishers. Although publishers always benefit in the post-ad-block world (Section 4.3), the specific strategy, namely, the gating decision and the adintensities for regulars and ad-blockers, to realize this benefit differs across publishers. Two key characteristics that shape a publisher’s strategy are the strength of the network effect it faces and the adsensitivity of its potential users. Figure 8 summarizes the associated recommendations offered by our analysis: If the network effect is strong and the user population is ad-sensitive, then no gating and a low ad-intensity is recommended. On the other extreme, if the network effect is low and users have a high adtolerance, then always gating and a high ad-intensity is suggested. Otherwise, the website should selectively gate users and advertise at a moderate intensity. In all of these cases, when a website gates, it is recommended that white-listers be offered an adlight experience.

Figure 7. The Sequence of Events of the Game When the Website Offers Both the White-Listing and Subscription Options  
![](/api/attachments/ZRKHUW2H/fulltext/images/aac9ec7ff63a3625a06a49884ad406ff2d392402fa4a52c4f76dcca1fdff7771.jpg)  
Notes. The website first decides $I _ { G } , \ a _ { b } , \ a _ { r } ,$ and f . The ad-blockers then decide whether to white-list (for ad-supported content) or subscribe (fo ad-free content) or consume the outside option. Similarly, the regulars decide whether to access the website with ads or subscribe or consume the outside option. The quantities in brackets represent the payoffs received by the website and the user, respectively

Browsers. Recently, Google announced that it plans to provide an inbuilt ad-blocker for its Chrome web browser (Marshall 2017). There already exist other web browsers that come with an inbuilt ad-blocker, for example, Adblock Browser for mobiles and Opera for both desktops and mobiles. We now discuss the potential impact of the decision of web browsers to provide an inbuilt ad-blocker on the welfare of publishers and consumers. Specifically, let us imagine the following setting: The web browsers of all potential users of the website have an inbuilt ad-blocker with a white-listing feature (both Opera and Adblock Browser offer this feature). Thus, the only way that the website can show ads to its users is by asking them to white-list the website on their browsers.

As our analysis in Sections 4 and 4.3 showed, the conscious decision of users to install an ad-blocker divulges information about their ad-viewing costs, which can then be exploited by the website to tailor their ad-intensities. When the outside option offers low utility, this separation not only benefits publishers but also improves consumer surplus. On the flip side, this discrimination is not powerful enough when the outside option offers a high-enough utility, in the sense that users with low ad-viewing costs can be worse off after the advent of ad-blockers. However, if all potential users have an inbuilt ad-blocker, the publisher cannot distinguish them on the basis of their ad-viewing costs and, therefore, loses the ability to customize their ad-intensities. Thus, we are back to the situation before the advent of ad-blockers. Let $P _ { I n b u i l t }$ refer to the website’s problem for a user population with inbuilt ad-blockers. The analysis of this problem is identical to that in Section 4.2 of Problem $P _ { B e f o r e }$ . The website will gate all users and offer them a single ad-intensity upon white-listing. Thus, the comparison between $P _ { I n b u i l t }$ and $P _ { A f t e r }$ is identical to the comparison between $P _ { A f t e r }$ and $P _ { B e f o r e }$ with the trends reversed. That is, with inbuilt ad-blockers (i) the website’s revenue decreases and (ii) both the consumer surplus and social surplus increase if $u _ { 0 } \geq \hat { u } _ { 0 }$ and decrease otherwise.

Figure 8. (Color online) The Recommended Gating Decision and Advertisement Intensity Based on the Strength of a Website’s Network Effect and the Ad-Sensitivity of Its Potential Users  
![](/api/attachments/ZRKHUW2H/fulltext/images/37239ad62380223f56b5d8892ce0d3d5d2a8806077e30e9a380c1858dd12bc2e.jpg)

It would be safe to assume that the primary goal of a web browser is to provide a compelling browsing experience to its users. Thus, the decision of web browsers to provide an inbuilt ad-blocker is perhaps aimed at improving consumer surplus. However, our analysis suggests that inbuilt ad-blockers increase consumer welfare of only those websites for which the outside option is high $( u _ { 0 } \ge \hat { u } _ { 0 } )$ . Publishers that offer unique content, for example, Facebook, Twitter, and YouTube, arguably have low-utility outside options; their users can be worse off with inbuilt ad-blockers. Overall, we conclude that the well-intentioned intervention to provide inbuilt ad-blockers can have undesirable consequences and should, therefore, be maneuvered carefully. Alternately, it would be best to let the ecosystem evolve organically, that is, let users consciously make a choice to install ad-blockers.

Policy Makers. Publishers and firms that develop adblock software continue to engage in protracted legal battles. With ad revenue being their only source of revenue, publishers have argued for the imposition of a legal ban on ad-block software—a charge that ad-blocking firms have thus far successfully fought against (Meyer 2016, Rodriguez 2017). Also, privacy activists have objected to publishers detecting adblockers in users’ web browsers without their permission (Heilpern 2016). Our analysis derives the conditions under which both publishers and users can benefit from ad-block software and also derives the associated operational decisions for the publisher. Perhaps these results can help the stakeholders better understand the implications of ad-block software and, consequently, de-escalate the conflict between the two parties.

We now conclude with a brief discussion of some potential extensions. A typical website consists of multiple webpages. An underlying assumption of our analysis in this paper was that the website’s decisions, namely, those of gating and choosing the ad-intensities for regulars and ad-blockers, are the same for each page of the website. It is not uncommon, however, for some pages of a website to offer unique content (for instance, an opinion piece on nytimes.com), whereas other pages provide generic content that is easily available elsewhere. Naturally, it is easier for the website to convince potential users to white-list pages that offer unique content. Thus, one can potentially investigate a richer set of decisions for the website, for example, an aggressive gating policy for pages with unique content and a relatively relaxed one for those with generic content. This setting can be challenging to analyze, for example, because of the subtle interaction between the equilibrium traffic on these two types of pages. Another potential enhancement to our setting would be to incorporate the presence of a competing website.

## Endnotes

<sup>1</sup> See https://pagefair.com/blog/2017/adblockreport/.

<sup>2</sup> When no confusion arises in doing so, we use the term “ad-blocker” to interchangeably refer to ad-block software or a user who has in stalled such software.

<sup>3</sup> Websites can detect and track white-listers; see, for example, DVorkin (2016).

<sup>4</sup> For brevity, we refer to the publisher as “she” and a potential user as $\mathrm { \Delta ^ { \prime \prime } h e . \Delta ^ { \prime \prime } }$

<sup>5</sup> The results for the case when there is no positive lower bound on the ad-intensities (i.e., $a _ { \mathrm { m i n } } = 0 )$ are summarized later in Section 4.3

Our analysis and results continue to hold for either of the two most popular payment formats in use today: pay-per-click and pay-perimpression. The revenue r can be interpreted as revenue per impression in the case of the pay-per-impression format or the expected revenue in the case of the pay-per-click format (click probabilit multiplied by per-click revenue).

## References

Anderson SP, Gans JS (2011) Platform siphoning: Ad-avoidance and media content. Amer. Econom. J. Microeconomics 3(4): 1–34.

Asvanund A, Clay K, Krishnan R, Smith MD (2004) An empirical analysis of network externalities in peer-to-peer music-sharing networks. Inform. Systems Res. 15(2):155–174.

Bhargava HK, Choudhary V (2008) Research note—When is versioning optimal for information goods? Management Sci. 54(5): 1029–1035.

Chellappa RK, Shivendu S (2005) Managing piracy: Pricing and sampling strategies for digital experience goods in ver tically segmented markets. Inform. Systems Res. 16(4):400–417.

Chellappa RK, Shivendu S (2010) Mechanism design for “free” but “no free disposal” services: The economics of personalization under privacy concerns. Management Sci. 56(10): 1766–1780.

Despotakis S, Ravi R, Srinivasan K (2017) The beneficial effects of ad blockers. Working paper, City University of Hong Kong, Hong Kong.

DigitBin (2018) Best ad blockers for Android: Block ads and pop-ups. Accessed June 5, 2019, https://www.digitbin.com/ad-blocke -apps-android/.

Dou Y, Niculescu MF, Wu D (2013) Engineering optimal network effects via social media features and seeding in markets fo digital goods and services. Inform. Systems Res. 24(1):164–185.

DVorkin L (2016) Inside Forbes: More numbers on our ad blocking plan–and what’s coming next. Accessed June 5, 2019, https:// www.forbes.com/sites/lewisdvorkin/2016/02/10/inside-forbes -more-numbers-on-our-ad-blocking-plan-and-whats-coming-next/ #6efeea776209.

Elliott C (2017) Yes, there are too many ads online. Yes, you can stop them. Here’s how. HuffPost (February 2), https://www .huffpost.com/entry/yes-there-are-too-many-ads-online-yes -you-can-stop\_b\_589b888de4b02bbb1816c297.

Gallaugher JM (2008) Understanding network effects. Accessed June 5, 2019, http://www.gallaugher.com/Network%20Effects %20Chapter.pdf.

Garimella K, Kostakis O, Mathioudakis M (2017) Ad-blocking: A study on performance, privacy and counter-measures. Preprint, submitted May 9, https://arxiv.org/abs/1705.03193.

Gervais A, Filios A, Lenders V, Capkun S (2017) Quantifying web adblocker privacy. Foley S, Gollmann D, Snekkenes E, eds. 22nd Eur. Sympos. Res. Comp. Security, Lecture Notes in Computer Science, vol. 10493 (Springer, Cham, Switzerland), 21–42.

Goh K-Y, Hui K-L, Png IP (2015) Privacy and marketing externalities: Evidence from do not call. Management Sci. 61(12):2982–3000.

Hann I-H, Hui K-L, Lee S-YT, Png IP (2008) Consumer privacy and marketing avoidance: A static model. Management Sci. 54(6): 1094–1103.

Heilpern W (2016) Websites that detect your ad blocker could be breaking EU law. Accessed June 5, 2019, http://www .businessinsider.com/ad-blocker-blockers-may-be-illegal-in -europe-2016-4.

Johar M, Menon S, Mookerjee V (2011) Analyzing sharing in peerto-peer networks under various congestion measures. Inform. Systems Res. 22(2):325–345.

Johnson JP (2013) Targeted advertising and advertising avoidance. RAND J. Econom. 44(1):128–144.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Kauffman RJ, McAndrews J, Wang Y-M (2000) Opening the “black box” of network externalities in network adoption. Inform. Systems Res. 11(1):61–82.

Krammer V (2008) An effective defense against intrusive web advertising. Proc. 6th Annual Conf. Privacy Security Trust (IEEE Computer Society, Washington, DC), 3–14.

Lahiri A, Dey D (2013) Effects of piracy on quality of information goods. Management Sci. 59(1):245–264.

Lambrecht A, Misra K (2016) Fee or free: When should firms charge for online content? Management Sci. 63(4):1150–1165.

Lee D, Mendelson H (2007) Adoption of information technology under network effects. Inform. Systems Res. 18(4):395–413.

Li X, Chen Y (2012) Corporate IT standardization: Product com patibility, exclusive purchase commitment, and competition effects. Inform. Systems Res. 23(4):1158–1174

Ma D (2015) Push or pull? A website’s strategic choice of content delivery mechanism. J. Management Inform. Systems 32(1):291–321.

Marshall J (2017) Google plans ad-blocking feature in popular Chrome browser. Wall Street Journal (April 20), https://www .wsj.com/articles/google-plans-ad-blocking-feature-in-popular -chrome-browser-1492643233

Meyer D (2016) This popular ad-blocker keeps beating ‘old guard media in court. Accessed June 5, 2019, http://fortune.com/2016 03/30/adblock-plus-sueddeutsche/.

Nair J, Wierman A, Zwart B (2015) Provisioning of large-scale systems: The interplay between network effects and strategic behavior in the user base. Management Sci. 62(6): 1830–1841.

Niculescu MF, Wu DJ (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. System Res. 25(1):173–199.

Nithyanand R, Khattak S, Javed M, Vallina-Rodriguez N, Falahrastegar M, Powles JE, De Cristofaro E, Haddadi H, Murdoch SJ (2016) Ad-blocking and counter blocking: A slice of the arms race. Preprint, submitted July 20, https://arxiv .org/abs/1605.05077.

Parker GG, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10): 1494–1504.

Ray A, Ghasemkhani H, Kannan KN (2017) Ad-blockers: Extortionists or digital age Robin Hoods? Working paper, Purdue University, West Lafayette, IN.

Rodriguez A (2017) The EU is totally fine with publishers blocking ad blockers. Accessed June 5, 2019, https://qz.com/882462 the-eu-is-totally-fine-with-with-publishers-blocking-ad -blockers/.

Sheffrin SM (1996) Rational Expectations (Cambridge University Press, Cambridge, UK).

Shin J (2007) How does free riding on customer service affect com petition? Marketing Sci. 26(4):488–503.

Shriver SK, Nair HS, Hofstetter R (2013) Social ties and usergenerated content: Evidence from an online social network. Management Sci. 59(6):1425–1443.

Statista (2019) Cost of ad blocking in the United States from 2016 to 2020 (in million U.S. dollars). Accessed June 5, 2019, https:/ www.statista.com/statistics/454473/ad-blocking-cost-usa/.

Storey G, Reisman D, Mayer J, Narayanan A (2017) The future of ad blocking: An analytical framework and new techniques. Pre print, submitted May 24, https://arxiv.org/abs/1705.08568

Stühmeier T, Wenzel T (2011) Getting beer during commercials: Adverse effects of ad-avoidance. Inform. Econom. Policy 23(1): 98–106.

Vallade J (2008) Adblock Plus and the legal implications of online commercial-skipping. Rutgers Law Rev. 61:823–853.

Varian HR (1997) Versioning information goods. Working paper, University of California, Berkeley, Berkeley.

Wakabayashi K, Marshall J (2015) Apple’s ad blockers rile publishers. Wall Street Journal (August 30), http://www.wsj.com/articles apples-ad-blockers-raise-tensions-1440974849

Wei XD, Nault BR (2014) Monopoly versioning of information goods when consumers have group tastes. Production Oper. Management 23(6):1067–1081.

Wu S-Y, Chen P-Y (2008) Versioning and piracy control for digital information goods. Oper. Res. 56(1):157–172.

Zhang K, Evgeniou T, Padmanabhan V, Richard E (2012) Content contributor management and network effects in a UGC envi ronment. Marketing Sci. 31(3):433–447.
