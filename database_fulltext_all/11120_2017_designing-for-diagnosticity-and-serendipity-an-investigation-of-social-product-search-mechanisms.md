---
otero_id: 11120
otero_key: "GTS3AR8U"
title: "Designing for Diagnosticity and Serendipity: An Investigation of Social Product-Search Mechanisms"
authors: "Cheng Yi; Zhenhui (Jack) Jiang; Izak Benbasat"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0695"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/GTS3AR8U/fulltext/images/4e59e712139700c0e6c5c374628587562aca0ab76936aa2bc8a0189411368d6e.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Designing for Diagnosticity and Serendipity: An Investigation of Social Product-Search Mechanisms

Cheng Yi, Zhenhui (Jack) Jiang, Izak Benbasat

To cite this article:

Cheng Yi, Zhenhui (Jack) Jiang, Izak Benbasat (2017) Designing for Diagnosticity and Serendipity: An Investigation of Social Product-Search Mechanisms. Information Systems Research

Published online in Articles in Advance 20 Apr 2017

http://dx.doi.org/10.1287/isre.2017.0695

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GTS3AR8U/fulltext/images/b87d46534bae1b915668e108639c1c3f93194e71f49e894f3621d3e0a8129cb0.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Designing for Diagnosticity and Serendipity: An Investigation of Social Product-Search Mechanisms

Cheng Yi,<sup>a,b</sup> Zhenhui (Jack) Jiang,<sup>c</sup> Izak Benbasat<sup>d</sup>

<sup>a</sup> Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, 100084 Beĳing, China; <sup>b</sup> Institute of Internet Industry, Tsinghua University, 100084 Beĳing, China; <sup>c</sup> Department of Information Systems, School of Computing, National University of Singapore, Singapore 117418; <sup>d</sup> Sauder School of Business, University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada

Contact: yich@sem.tsinghua.edu.cn (CY); jiang@comp.nus.edu.sg (Z(J)J); izak.benbasat@ubc.ca (IB)

Received: December 4, 2014 Revised: September 22, 2015; June 18, 2016; October 6, 2016; November 7, 2016 Accepted: November 10, 2016 Published Online in Articles in Advance: April 20, 2017

https://doi.org/10.1287/isre.2017.069

Copyright: © 2017 INFORMS

Abstract. Users are increasingly sharing their product interests and experiences with others on e-commerce websites. For example, users can “tag” products using their own words, and these “product tags” then serve as navigation cues for other users who want to search for products. Also, socially endorsed information contributors are sometimes highlighted on websites and serve as direct information sources. This study examines the efects of these two distinct social product search cues, product tags and socially endorsed people, on users’ perceived diagnosticity and serendipity of their product search experience. While product tags support product navigation via a variety of product features tagged by the community, access to socially endorsed people enables users to browse diverse and high-quality alternatives favored by these individuals. We constructed an experimental website using real data from one of the largest social-network-based product-search websites in China to conduct an empirical study. The results of this study show that product tags help users to locate and evaluate relevant alternatives, thus enhancing the perceived diagnosticity of product search, whereas the integration of product tags and access to socially endorsed people enables users to conduct even more serendipitous searches. In addition, both perceived diagnosticity and perceived serendipity of a search experience positively afect users’ decision satisfaction.

History: Mark Keil, Senior Editor; Yulin Fang, Associate Editor. 5

Funding: The authors thank the National Natural Science Foundation of China [Project 71402079 and 71110107027], Tsinghua University Independent Research Project [Grant 20151080393], and the Ministry of Education of Singapore [Grant T1 251RES1613] for financial support. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0695.

Keywords: user-generated content • product tags • socially endorsed people • information foraging • perceived diagnosticity perceived serendipity • decision satisfaction • product search

## Introduction

Consumers often want to search for available products in the market before making a purchase. Past research has generally focused on how to improve online product search tools, such as online catalogues, recommendation agents, or search engines, to help users to directly access products with preferred attributes, either elicited from users in the form of keywords or inferred based on their past behavior (e.g., Ho and Bodof 2014, Kamis et al. 2008, Xiao and Benbasat 2007). Yet, evidence suggests that consumers may not always want to search for information by relying on preset preferences or keywords—either because they are not clear about what they really need at the beginning of a search or because their preferences can change during a search process (e.g., David et al. 2007, Lee and Ariely 2006). Indeed, recent research suggests that users often work with a set of malleable preferences that are sensitive to the information encountered during the search process (e.g., Adomavicius et al. 2013), and hence their final choices may not necessarily closely relate to their original intentions. In other words, users’ information seeking tends to be adaptive (McKenzie 2003, Sin and Kim 2013). Accordingly, an important research question is how a product search experience can be designed to facilitate both diagnostic search, which is accomplished by following users’ desired criteria, and serendipitous discoveries that are not expected but can satisfy users’ latent needs (Agarwal 2015). While being able to follow one’s search criteria to logically retrieve relevant results is certainly important in building users’ trust in a search system (e.g., Swearingen and Sinha 2001), the significance of serendipity in innovative discoveries has increasingly been recognized in various domains (Ashman et al. 2014, Foster and Ford 2003, Graebner 2004, Rivoal and Salazar 2013, Trier and Molka-Danielson 2013). A search process that is both diagnostic and serendipitous will allow users to preserve logical continuity in search and prevent them from being lost in cyberspace, and, at the same time, will enable them to discover pleasant surprises beyond their existing tastes and preferences.

In particular, a growing trend is for users to search for information on large and open platforms, such as Digg, Pinterest, and Yelp, where people share their interests, bookmarks, product consumption experiences, etc. The sheer amount of user-generated content (UGC) on these platforms allows users high flexibility in choosing what content to follow, from a variety of social information cues as well as other community users’ personal collections. Under these circumstances, users’ search routes can be largely adaptive and nonlinear compared with those following traditional indexing and filtering tools such as search engines and recommendation systems (Chi 2009, Evans and Chi 2008). Users may find needed items as intended, or they may also find useful items without expecting it a priori. In the context of social commerce platforms, many studies have investigated how UGC features such as “likes” and consumer reviews afect users’ product evaluations, but less attention has been paid to UGC features that facilitate both product evaluation and navigation across products. This study thus focuses on two navigation-enabled UGC features, namely, product tags and socially endorsed people, and examines how they shape users’ perceptions of the diagnosticity and serendipity of a product search experience.

Specifically, tags are user-generated product “labels,” which are often aggregated for each product and semantically depict various features of a product (e.g., Zeng and Wei 2013). For example, on Amazon.com, tags of the book Linked include “social networks,” “Internet,” “business,” “popular science,” etc. Clicking on any tag of interest, users will be directed to a list of products that share the tagged feature, and then they can conduct further product evaluation and comparison. Tags thus serve as highly visible product-feature-based navigational cues. Socially endorsed people, by contrast, signal access to high-quality individual information sources. For example, social commerce platforms such as Stylehive.com and Wanelo.com feature on product pages a handful of individuals who have been endorsed by a large number of other community users for their past useful information contributions such as reviews and favorite item collections. When visiting their personal profiles, other users can choose to click on any of the collected products that they like and then perform an in-depth evaluation (Goldenberg et al. 2012). Overall, while tags support product navigation based on various product features reflecting collective judgment, socially endorsed people help users to easily access a set of items favored by those endorsed individuals.

To investigate how users’ product search is directed by these social search cues, we draw on information foraging theory (IFT) as the overarching theory, which describes how users appraise and follow the “scent” of search cues in the environment and acquire information (Pirolli 2007, Pirolli and Card 1999). In our context, product tags and socially endorsed people are search cues that lead users to diferent pages or “patches” of products and related information. While tags convey scent related to product features, socially endorsed people convey scent related to information sources. Users need to assess the expected gains and costs of following diferent search cues before they decide where or how to search. This assessment thus determines how diagnostic and serendipitous their search experience is. Our findings show that tags and socially endorsed people as diferent types of search cues direct users to take distinct search routes, but they also reinforce each other in facilitating a serendipitous search. In addition, we also test whether perceived diagnosticity and perceived serendipity of a search experience will afect users’ decision satisfaction.

This study makes several important contributions. First, diferent from traditional search contexts where explicit user preferences are incorporated as inputs to search tools, this study focuses on product search in a more flexible UGC environment. Our findings suggest that user-generated search cues, in particular, product tags and socially endorsed people, can efectively shape one’s search experience. Second, while traditional models of human information search behavior generally do not include the notion of serendipity (Agarwal 2015), this study incorporates users’ perception of serendipity as an important aspect of their search experience and reveals that conducting diagnostic search and making serendipitous discoveries both contribute to reaching a satisfactory decision. Third, past information foraging studies have generally modeled users’ navigational choices based on search cues that provide descriptive information about the linked content (Pirolli 2007). This study investigates how diferent types of UGC-based search cues, that is, cues conveying product-feature-related information and those signaling quality of an information source, may complement each other in afecting users’ search experience.

## Two Mechanisms to Facilitate Social Navigation: Product Tags and Socially Endorsed People Product Tags

Collaborative tagging systems allow ordinary consumers to annotate products using their own vocabulary in the form of keywords. In the presence of tags, users can easily recognize a variety of features of each product. Specifically, unlike a catalog system, which typically organizes products within depths of category hierarchies, user-generated tags are often displayed in a flat structure on a product information page and simultaneously reveal a wide range of product properties. The popularity of each tag for a given product, that is, the number of users who have assigned the tag to the product, is often denoted as well. Clicking on a particular tag associated with the product, users will be directed to a list of products possessing the tagged property. Users can then choose another product for evaluation, and, if interested, they can further explore other tags associated with that product. This kind of navigation is termed “pivot browsing”; i.e., users can easily recognize diferent navigation options and adjust their search criteria and navigation paths at any moment (Millen et al. 2006, Shami et al. 2011).

Prior studies on collaborative tagging have focused on issues such as people’s incentives for generating tags (e.g., Ames and Naaman 2007), the growth patterns of tags (e.g., Golder and Huberman 2006, Fu 2008), information organization eficiency using tagging systems (Pak et al. 2009), and the information dissemination efect of tagging in social networks (Choi et al. 2015). In the organizational context, recent studies have suggested that tagging systems can be beneficial to employees in terms of discovering relevant and novel information (Gray et al. 2011, McAfee 2006). In particular, providing employees with the ability to selectively and unobtrusively discover information that others have collected via their bookmarks (i.e., a form of tags) can positively influence one’s personal innovativeness because of the social diversity of information sources. Nonetheless, research that theorizes how product tags direct consumers’ online product search behavior has been rare.

## Socially Endorsed People

On social commerce platforms, users can access other shoppers’ profiles and acquire knowledge from them. In particular, a small number of shoppers in the community who have received wide social endorsement for their past contributions (e.g., a large number of “thumbs-ups” or “likes” from other users) are often featured prominently on the pages of the products that they have commented on (Metzger and Flanagin 2013). Their profiles usually contain high-quality content that is endorsed by many peers and thus appeals to a wide range of community users. Users can visit a socially endorsed individual’s profile to see her views on the focal products as well as her collections or views of many other products. Since one often posts a variety of content to reflect her diverse interests and preferences, a socially endorsed individual featured on a webpage can function as a bridge between different types of products beyond providing information directly related to the products being evaluated (Goldenberg et al. 2012).

Researchers have paid great attention to socially endorsed users in online social networks and found that these individuals have a disproportionately large influence on other users (Berry and Keller 2003, Gladwell 2002). These users are sometimes called gurus (Biel and Gatica-Perez 2009), opinion leaders (Burt 1999), or mavens (Gladwell 2002) in diferent contexts. Related studies have investigated the characteristics of these users (e.g., Kratzer and Lettl 2009), methods of identifying these users in a network (e.g., Iyengar et al. 2011, Trusov et al. 2010), their information contribution behavior (e.g., Goes et al. 2014), and their roles and commercial impacts in various contexts (e.g., Franke et al. 2006, Iyengar et al. 2011, Zhang et al. 2015). Examining how consumers leverage information from these endorsed users to adjust and refine their product searches on e-commerce websites may thus provide opportunities for enriching our understanding of information search in the social Web and developing principles for designing online social features.

## Theoretical Foundations

In online environments, users often want to collect necessary information pertaining to their needs for product evaluation and comparison prior to making final decisions. As they acquire more information, their needs may evolve (Lawrance et al. 2010, Lee and Ariely 2006, Yi et al. 2014) and they may reformulate or refine their search criteria (David et al. 2007, Payne et al. 1992). Accordingly, users’ interaction with an information environment is a process of search, sensemaking, adaptation, and investigation. In particular, the current study focuses on how online users follow social search cues to identify relevant products and make product selection decisions. Studies suggest that such a process can be explained by IFT (Pirolli 2007, Pirolli and Card 1999), which presents a cognitive model to predict users’ cue-following behavior during information search. While the use of IFT in information systems (IS) literature has been limited, it has been cited widely in the practitioner literature (e.g., Krug 2006, Nielsen 2003) and applied to various contexts to understand users’ information search behavior. Online Appendix A presents a summary of the research related to IFT.

## Scent-Based Information Foraging

IFT suggests that information on a given subject is often dispersed in the environment in diferent patches. Some patches may be more “profitable” than others, i.e., yield a higher rate of relevant resources (Pirolli and Card 1999). An information forager has to expend some amount of time locating potentially profitable information patches and processing information within the patches. IFT generally posits that since people have constraints on their ability to process information (Simon 1955), they often seek to maximize the value of information gained per unit cost of interaction. Information foraging cost normally arises from two activities: accessing a new patch (i.e., betweenpatch cost) and consuming information within a patch (i.e., within-patch cost). In selecting an information patch to access, foragers will not necessarily attempt to locate the absolute best one, but rather will identify one that is good enough and can be accessed and processed easily. They will focus on exploring a profitable information patch until the value of additional information (i.e., the anticipated benefits less the cost to acquire) can only be increased by moving to a new patch.

On the Web, an information patch often consists of a set of linked webpages. Online foragers may start exploring a patch by accessing certain cues, such as hyperlinked text or images. They use these concise cues to assess the profitability (i.e., the gain–cost ratio) of subsequent linked pages that are not immediately evident and make navigation path selections accordingly. In IFT, the estimated profitability of the distal information is referred to as the scent of the cues conveyed to users. Typically, if the semantic similarity between an information cue and foragers’ existing or latent needs is high, then foragers’ goal-related cognitive processing is likely activated by the cue, suggesting that the scent emitted from this cue is strong (Moody and Galletta 2015, Otter and Johnson 2000). IFT argues that information foragers will parse the available cues and select a cue with a good enough scent for further access. If none of the scents is strong enough to warrant further attention, they will backtrack or conduct a random walk. Overall, information foraging is a series of sensemaking and information-gathering activities in which users attempt to attain maximum information gain for minimum efort.

Social Information Foraging and Source Evaluation Social information foraging (SIF) theory extends IFT to a social context and argues that a group of people can more eficiently and thoroughly discover knowledge than a single user because social information sharing reduces much of the cost of information gathering (Giraldeau and Caraco 2000, Gray et al. 2011, Pirolli 2007). Specifically, SIF theory assumes that different individuals specialize in diferent information domains; hence, it is unlikely that a single mind can discover and make sense of all of the information. However, when many individuals with diferent expertise and perspectives devote their respective eforts to sharing hints with others to indicate the likely locations of particular pieces of valuable information, a greater diversity of information cues become readily available (Pirolli 2009). Increased accessibility of information cues allows users to easily identify and switch to another patch, thus lowering patch access cost. For example, technologies such as collaborative tagging allow all community users to annotate products using tags, leading to a variety of perspectives presented for each product. Other users can search for products via accessing any tag of interest and also change their search directions easily by switching to another tag (Gupta et al. 2011).

SIF theory has also pointed out the importance of a handful of well-experienced individuals in the community in achieving efective social foraging. These individuals have often accumulated more experiences and knowledge than most others (Pirolli 2007, 2009). Getting information from these experienced users thus yields additional value by expanding one’s search space rather than producing redundancy. However, with the abundance of information contributors on social platforms, one primary task for information foragers is to identify contributors that are worth attention to maximize the relevance and quality of the information gained (Canini et al. 2011). In this regard, while IFT and SIF studies mainly focus on topical relevance as one determinant of the scent of navigation cues, a few recent studies have suggested that perceived quality of information sources is also important in shaping foragers’ navigation behavior, especially on social platforms where foragers can directly source information from peers. In particular, it was found that online users usually base their source quality assessments on social endorsement, such as “likes” and “thumbs-ups,” because people tend to perceive the quality of a knowledge source as high if others find it useful (Banerjee 1992, Chaiken 1987, Metzger and Flanagin 2013). Since wide social endorsement suggests high utility of the associated information, it is reasonable to expect that socially endorsed information sources convey a strong scent via signaling the quality of linked information (in their profiles), which also helps users make navigation decisions. Accordingly, the content generated by a widely endorsed user is likely to be sought by foragers.

Overall, SIF and related studies suggest that foragers can discover information more efectively by foraging in groups, and some socially endorsed individuals may serve as important conduits to valuable and unique information for ordinary foragers. Drawing on IFT and SIF, this research thus investigates how users interact with social search cues and benefit from cooperative foraging mechanisms in the context of online product search.

## Hypothesis Development

## Dependent Variables: Perceived Diagnosticity, Perceived Serendipity, and Decision Satisfaction Percelved Serendipity, and Decislon Satisfaction

This study examines the efects of product tags and socially endorsed people on users’ product search experience. Product search involves screening and evaluating alternatives before arriving at a decision. One important and fundamental aspect of a search experience is the extent to which users can follow their search criteria to find and evaluate relevant alternatives efectively. This aspect is characterized as the perceived diagnosticity of product search experience. Perceived diagnosticity is previously defined as the extent to which a site visitor believes that a website is helpful in terms of evaluating a given product (Jiang and Benbasat 2004). Prior studies have shown that perceived diagnosticity can be afected by users’ interactive product experience on a website (Jiang and Benbasat 2004), and that it also influences users’ uncertainty about product quality and attitudes toward purchasing (Pavlou and Fygenson 2006, Pavlou et al. 2007). Since the current study focuses on users’ product search experience, which involves accessing and evaluating multiple alternatives according to search needs, we define perceived diagnosticity of a search experience as the extent to which a user believes that a website helps her to efectively access and evaluate relevant products in a search process. Obtaining a diagnostic search experience thus implies that users can logically scout, evaluate, and compare alternatives in accordance with their desired search criteria.

The second key aspect of product search experience is serendipity, which is described as “happy accidents” (Golin1957,p. 2084), “unintendedfinding” (Andel1994, p. 631), or “accidental discovery” (Roberts 1989) in past studies. While serendipity has been explored in various contexts such as organizational science (Graebner 2004), information science (Foster and Ford 2003), entrepreneurship (Dew 2009), and medicine (Klein 2008), attention to this concept in IS research is still scarce. This study focuses on perceived serendipity, which is the extent to which a user believes that a website helps her to discover useful products beyond her original expectation in a search process (McCay-Peet and Toms 2011, Sun et al. 2013). Findings are perceived as serendipitous if they fit a user’s latent preferences but are not expected with respect to the user’s deliberate and known search criteria. The definition of serendipity thus integrates both relevance (i.e., usefulness in satisfying users’ information needs) and unexpectedness (i.e., suficient divergence from users’ initial perceptions of search results; Sun et al. 2013).

It is important to note that perceived diagnosticity and serendipity characterize a user’s search experience from two important and distinct aspects, but they are not contrasted concepts. While making serendipitous discoveries likely leads to changes or adaptations of users’ search criteria, diagnosticity captures the efectiveness of search and evaluation along particular search criteria. A search experience can be both diagnostic and serendipitous. For example, users may discover serendipitous findings in a search process, while their entire search experience can be diagnostic if their search before and after the unexpected finding yields relevant results in accordance with their search criteria.

This study further examines the efects of search diagnosticity and serendipity on users’ search outcomes. In the current context, since we are looking at a preferential choice task and people often have heterogeneous and dynamically constructed preferences, it is hard to use fixed objective criteria to define the “best” choice. Hence, we focus on users’ decision satisfaction as their search outcome (Haubl and Trift 2000, Kamis et al. 2008). Prior research has shown that users’ satisfaction with their task outcome is a pertinent measure to assess the quality of an information system and will strongly influence users’ future use of the system (Wixom and Todd 2005, Xiao and Benbasat 2007). The research framework is presented in Figure 1.

## The Efects of Product Tags

Tags on a product page display a wide range of product characteristics, and each tag leads users to an information patch, i.e., a list of products sharing the same tagged characteristic. These characteristics are created by community users and reflect consumers’ own terminology, and hence users are likely to quickly interpret them against their search needs (Fu 2008, Golder and Huberman 2006). In particular, highly popular tags (i.e., tags that are used by a large number of users to describe the product) often represent accurate descriptions of the prominent product features based on community consensus. Hence, given a variety of user-generated tags associated with each product along with the popularity indicators of each tag, it is relatively easy for users to recognize tags that match their search needs. These tags are expected to efectively activate users’ goal-related cognitive processing and convey a strong scent to them (Katz and Byrne 2003, Larson and Czerwinski 1998). As IFT suggests, users will follow the information scent and focus on selected scentful cues to explore deeply (e.g., Gupta et al. 2011, Lawrance et al. 2007). Accordingly, in the presence of tags, users can easily recognize a desired dimension to start their search and may focus on the selected path to consistently access a patch of products possessing the tagged property. This will lead to a diagnostic evaluation and comparison experience. By contrast, without tags, it would be more costly for users to find scentful cues to access, and users may have to manually construct meaningful search keywords and try to improve the keywords in each round of exploration (Katz and Byrne 2003). In this case, locating a relevant search dimension to follow is more dificult, and hence it is less likely for users to maintain a consistent and diagnostic search process. We thus expect that the presence of tags will increase the ease and likelihood of accessing high-scent search cues and help users to systematically evaluate and compare relevant alternatives. Therefore, we propose the following:

Figure 1. Research Framework  
![](/api/attachments/GTS3AR8U/fulltext/images/3055c3a77c1f47afff43d9bb03c217553280c7f350cb27a735134556b043d9bb.jpg)

Hypothesis 1 (H1). Social commerce websites with product tags will lead to a higher level of perceived diagnosticity of product search than those without product tags.

SIF theory suggests that collective information sharing leads to greater information diversity, which is likely to expand individual foragers’ search horizons (Chi 2009). Product tags are created by community users at their discretion and presented aggregately in a flat structure for each product. When tags are present, users are exposed to various descriptors of a product simultaneously, which reflect the diferent perspectives and preferences of community users pertaining to the product. The presence of these diverse annotations may thus stimulate users’ cognitive processing on some latent interests that are related to their current pursuit but may not have been recognized. Moreover, the concurrence of diferent tags is likely to increase foragers’ between-patch search activities because of the low cost of switching between tags (i.e., pivot browsing). In particular, when a certain tag stimulates a user’s latent interest and conveys a strong scent, the user may pursue the new line of search immediately via a click. Such quick and low-cost adaptation of search paths allows users to capture and follow their newly identified interests in a timely manner, leading to more serendipitous discoveries. For example, a user looking for a juicer may first follow the tag “juicer.” While evaluating a juicer, she may be exposed to other associated tags such as “healthy eating,” which she can click on to reach other related and interesting kitchenware for cooking healthy food at home, such as a machine to make homemade all-natural peanut butter. Such a discovery (i.e., from a juicer to a peanut butter machine) would not be possible if the user’s cognitive processing on the latent interest (i.e., healthy eating) was not activated by explicit search cues, or if she did not have a low-cost access to another information patch like that enabled by tags. Therefore, we propose the following:

Hypothesis 2 (H2). Social commerce websites with product tags will lead to a higher level of perceived serendipity of product search than those without product tags.

## The Efects of Socially Endorsed People

Besides following community-generated product tags, people can also seek advice and reach more products via visiting specific community members’ profiles. As SIF theory and related studies suggest, a handful of well-recognized individuals in the community is key to achieving efective social foraging because of their richer experience and knowledge compared to average users (Pirolli 2009). Information from these individuals is often deemed nonredundant and valuable by ordinary information seekers. Some social commerce platforms, such as Stylehive.com and Wanelo.com, showcase a handful of popular people in the community on product pages, e.g., those who have been endorsed by a large number of community users for their past useful contributions. Since these individuals have commented on the product being browsed and their contributions are widely endorsed in general, search cues enabling access to these high-quality information sources are likely to convey a strong scent to users (Metzger and Flanagin 2013). On one hand, users can visit these people’s profiles to obtain the owners’ opinions about the focal products based on their own product experiences. Indeed, recent studies have shown that information from highly knowledgeable people in the community greatly helps users with product assessment (Zhang et al. 2015). On the other hand, users may also discover other related highquality alternatives favored by those endorsed people (Goldenberg et al. 2012). Overall, with access to socially endorsed people of the community, users will be able to assimilate their valuable opinions, efectively assess products being viewed, and discover other related options. This will increase users’ perceived diagnosticity of the search experience. Therefore, we propose the following:

Hypothesis 3 (H3). Social commerce websites that feature socially endorsed people will lead to a higher level of perceived diagnosticity of product search than those that do not feature socially endorsed people.

Studies have also suggested that a few well-recognized individuals in a community can be sources of fresh ideas that are unlikely to be discovered by the general population (Nahapiet and Ghoshal 1998, Pirolli 2007). In the current context, socially endorsed individuals often post reviews and their favorite products in their profiles (e.g., Goldenberg et al. 2012), and such information is considered highly valuable by many other users. Eficient access to this diverse and valuable information thus enables information foragers to discover high-quality products that are likely beyond their original search intentions. For example, a user browsing a French restaurant may be interested in looking at some other good restaurants collected by an endorsed individual who has ofered useful comments on the French restaurant. This individual’s profile may contain her personal collections that may be related to other cuisine types and have other features not deliberately sought by the user. The diferent findings may stimulate the user’s cognitive processes on new and creative ideas and prompt her to consider a wider range of restaurants, such as Mexican restaurants. Overall, cues leading to profiles of socially endorsed people will attract other users to explore these personal profiles and discover alternatives beyond their own limited horizons. This will lead to a more explorative and serendipitous search compared to when such cues are not provided. Therefore, we propose the following:

Hypothesis 4 (H4). Social commerce websites that feature socially endorsed people will lead to a higher level of perceived serendipity of product search than those that do not feature socially endorsed people.

The Interaction Efects Between Product Tags and Socially Endorsed People on Perceived Serendipity We have argued that the presence of tags allows users to easily identify interesting and unforeseen attributes of a product, and tracing the corresponding tags will likely yield unexpected interesting product findings (i.e., high perceived serendipity). This efect will be further strengthened if users can eficiently spot some products that lead them to identify interesting and unexpected tags to follow subsequently. As SIF theory suggests, the efectiveness of tracing social information cues (such as tags) to discover new information depends on the ease of identifying some breakthrough ideas that are worth their subsequent foraging eforts and lead users beyond their regular search domains. In the current context, this means that if socially endorsed people can bridge products across diferent domains and help users to spot an interesting scent that may not be discovered otherwise, subsequent tag-based search is more likely to expand to novel domains and achieve an even higher perceived serendipity.

Specifically, featuring socially endorsed people helps users access rich collections by those endorsed individuals, which usually contain some high-quality products that may not be strictly related to users’ existing search criteria. The surprising products discovered in a socially endorsed individual’s profile are likely associated with various interesting and novel tags, and following these tags may easily lead to further unexpected interesting products and other related tags.

In other words, the presence of socially endorsed people plays an important role in helping users discover breakthrough ideas worthy of further investigation. Subsequently, as users continuously explore potentially interesting options via the associated tags, the efect of tags on perceived serendipity is amplified. By contrast, if users are not exposed to socially endorsed people, it will be relatively more dificult for them to identify diverse high-quality products and to trace the interesting and novel tags associated with these products. Hence, the impact of tags on perceived search serendipity will be much stronger when socially endorsed people are featured.

For example, on last.fm (an online music-sharing platform), a user searching for Beatles songs may find tags like “60s,” “rock,” and “British,” which are typical descriptors of Beatles songs. Without direct access to socially endorsed people, the user is likely to trace these relatively common tags of Beatles songs and find some related interesting music. However, the chances of making highly unexpected and pleasant discoveries may still be relatively low as the user may not be able to eficiently identify interesting tags that are somewhat distant from her existing tastes on the Beatles. If socially endorsed individuals are featured, a user may be attracted by some of them while browsing to a Beatles song. The user may then find other songs from a wider assortment of artists (e.g., Muse) in the personal collections of these socially endorsed people and note other interesting tags associated with those songs (beyond the common tags related to the Beatles) such as “indie” and “chillout,” which trigger her to expand her search to unexpected interesting domains. Following these tags allows the user to discover even more songs that she had not expected from the outset as well as other interesting tags associated. In this case, the user’s music search will be much wider, and the impact of tags on perceived search serendipity is thus more evident.

Overall, the efects of tags on facilitating serendipitous search will be strengthened when socially endorsed people are featured to bring more diversity and surprises into the search process. Therefore, we propose the following:

Hypothesis 5 (H5). The efects of product tags on perceived serendipity will be stronger when socially endorsed people are featured than when they are not featured.

## The Efects of Search Experience on Decision Satisfaction

Decision satisfaction captures the extent to which users are content with their decision outcomes derived from the product search process (Haubl and Trift 2000, Kamis et al. 2008). In the current context, perceived diagnosticity of product search represents the extent to which users are able to follow their search criteria and conduct search logically and efectively. Past research has shown that a shopping experience that enables users to logically find relevant information for decision making can make them feel informed (e.g., Jiang and Benbasat 2004). A diagnostic search experience may also decrease confusion and frustration as users are unlikely to feel disoriented in the search space (Kamis et al. 2008, Speier and Morris 2003). Accordingly, users are likely to be more satisfied with their decisions when they can carry out a diagnostic search pertaining to their specified needs. Therefore, we propose the following:

Hypothesis 6 (H6). A higher level of perceived diagnosticity of product search will lead to higher decision satisfaction.

Consumers’ decision satisfaction may also be related to how much the search experience includes novel and potentially valuable discoveries (e.g., Herlocker et al. 2004). High perceived serendipity of a product search experience implies that users may encounter interesting and valuable findings that are beyond their expectations. Studies suggest that people enjoy and remain highly engaged in a search experience as they discover new items and new directions that would not have been otherwise considered (Foster and Ford 2003, Sun et al. 2013, Yi et al. 2015). They are likely to view such a process as creative and fulfilling and thus the chance of regretting the final choice is lower. Overall, a serendipitous search experience has been shown to lead to improved user satisfaction over the decision outcomes (Zhang et al. 2012, Ziegler et al. 2005). Therefore, we propose the following:

Hypothesis 7 (H7). A higher level of perceived serendipity of product search will lead to higher decision satisfaction.

## Research Methodology Experimental Website Design

An empirical study was conducted to test the hypotheses proposed. To enhance the realism and the generalizability of the findings, we collaborated with one of the largest social commerce platforms in China, ABC.com.<sup>1</sup> This website combines tags, reviews, socially endorsed users, and social networking functionalities for consumers to search for, evaluate, and discuss local businesses, consisting mainly of restaurants and other dining services. ABC.com shared with us their database of about 1,000 restaurants in Shanghai plus over 60,000 registered users,<sup>2</sup> a data set that formed a well-connected social network clique. To remove brand identification of the website, we developed our own experimental website by adopting a diferent interface style, such as color scheme and page layout, as well as a diferent domain name. Specifically, from the main page, users could search and browse all of the restaurants featured on the website. Each restaurant information page showed the name of the restaurant, its detailed location together with a map, its telephone number, a picture of the restaurant, and an overall star rating (based on a five-star rating scale) of the restaurant and all of the user reviews. Each user’s profile page contained basic information about the user and her contributed contents, including her past restaurant reviews and favorite restaurant collections (see Online Appendix B).

We implemented a 2 (presence versus absence of product tags) <sup>×</sup> 2 (presence versus absence of featured socially endorsed people) between-subject experimental design. The provision of product tags and socially endorsed people were both manipulated on restaurant information pages. The treatment condition for the manipulation of product tags presented tags associated with every restaurant. These tags comprised a large number of user-generated vocabularies that depicted restaurant attributes such as featured dishes and cuisine type. If users recognized an interesting tag of a restaurant, they could click on the tag and then be directed to a list of other restaurants that were also tagged by the community with the same keyword. By contrast, the control condition did not show any product tags.

Similarly, in the treatment condition for the manipulation of socially endorsed people, a small handful of individuals, represented through their thumbnail pictures and names, were featured on the righthand panel of every restaurant’s information page and indicated as the socially endorsed people. These individuals were determined based on the overall social endorsement (such as the number of “likes” or “thumbs-ups”) received by their contributed information on ABC.com. By contrast, the control condition did not feature any endorsed people on a restaurant’s webpage, although users could still find these individuals among the reviewers of the restaurant.

The screenshot of a restaurant information page in the condition with both product tags and featured socially endorsed people is provided in Online Appendix C.

## Experimental Procedures

The participants consisted of 118 undergraduate and graduate students (29–30 subjects per group, with four experimental groups) recruited from a major university in Shanghai. According to Cohen (1988), this group size could assure suficient statistical power of 0.8 for a medium efect size ( f <sup></sup> 0.25). The participants were assigned randomly to an experimental condition and asked to fill in a preexperiment questionnaire that measured their demographic information. They were then briefed on the features of the website and given several minutes to get familiar with how to use it. Afterward they were instructed to perform the task of looking for a restaurant to dine with friends in the coming weekend. Since the university is located in the city area of Shanghai (the most populous city in China) and it is common for students to dine in local restaurants, the task of searching for restaurants is considered relevant for the participants. Their entire search process was captured by Camtasia Studio, a software application that could record users’ page browsing behavior. On average, the participants spent around 16 minutes searching for restaurants and making a decision. After making the restaurant choice, the participants completed a postexperiment questionnaire that measured their search experience and decision outcome, and they were paid around US\$6 each as a participation reward.

## Measurement

Measurement items for perceived diagnosticity of product search were adapted from Jiang and Benbasat (2004). However, since the current study concerned users’ search and evaluation of multiple alternatives rather than the evaluation of a single product, the items were adapted to focus on the efectiveness of the website in supporting systematic access to and evaluation of multiple products. Items for perceived serendipity of product search were adapted from Oku and Hattori (2012), which focused on the two characteristics of serendipitous findings, that is, surprising and useful. Items for decision satisfaction were adapted from Pereira (2001). All items were measured using sevenpoint Likert scales. The appendix lists all of the measurement items. Since the experiment was conducted in China, the questionnaire was translated into Chinese first, and a backward translation was conducted to ensure consistency between the Chinese and English versions.

## Data Analysis

## Subject Background Information

The student participants (with 71.6% undergraduates) were from 34 diferent academic departments, representing diverse backgrounds. Their average age was 22. In general, they were very familiar with using the Internet (mean <sup></sup> 6.02, seven-point scale). They were, on average, fairly interested in exploring restaurants in Shanghai (mean <sup></sup> 5.21), which also suggested that the experimental task was quite relevant to the participants. There was no diference in these variables across the diferent conditions.

## Manipulation Check

To check whether the participants noted and made use of the manipulated search cues, we captured their actual use of product tags and socially endorsed people. Our recorded data indicated that in the conditions where tags were present, the participants accessed, on average, three diferent tags, and 93% of the participants accessed at least one tag. When socially endorsed people were present, the participants visited, on average, three diferent users’ profiles, and 83% of the participants accessed at least one user’s profile. Overall, the manipulations of product tags and socially endorsed people were successful.

## Perceived Diagnosticity of Product Search

The Cronbach’s alphas for perceived diagnosticity and perceived serendipity are 0.81 and 0.90, respectively, demonstrating adequate internal consistency of the measurement (i.e., above 0.70). Multivariate analysis of variance (MANOVA) was first conducted on both perceived diagnosticity and perceived serendipity. We included users’ interest in exploring local restaurants as a control variable. Pillai’s trace test revealed a significant main efect of product tags $( p < 0 . 0 0 1 )$ as well as a significant interaction efect between tags and socially endorsed people $( p < 0 . 0 5 )$ . We then used follow-up ANOVAs to test the efects on the two dependent variables separately.

ANOVA results on perceived diagnosticity showed that there was a significant main efect of product tags (F<sup>(</sup>1, 113<sup>)</sup> <sup></sup> 20.62, p < 0.001); that is, the website with tags led to a significantly higher level of perceived diagnosticity than the website without tags. Hence, H1 was supported. However, the presence of socially endorsed people did not have a significant efect $( F ( 1 , 1 1 3 ) \bar { = } 0 . 0 \bar { 3 } , p > 0 . 0 5 )$ ; hence, H3 was not supported. There was no significant interaction efect between tags and socially endorsed people either (F<sup>(</sup>1, 113<sup>) </sup> 2.90, p > 0.05; see Tables 1 and 2).

Table 1. ANOVA Test—Main and Interaction Efects

<table><tr><td>Source</td><td>Dependent variable</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td rowspan="2">Product tags</td><td>Diagnosticity</td><td>1</td><td>22.47</td><td>20.62</td><td>0.00</td></tr><tr><td>Serendipity</td><td>1</td><td>4.39</td><td>4.34</td><td>0.04</td></tr><tr><td rowspan="2">Socially endorsed people</td><td>Diagnosticity</td><td>1</td><td>0.03</td><td>0.03</td><td>0.87</td></tr><tr><td>Serendipity</td><td>1</td><td>0.17</td><td>0.17</td><td>0.68</td></tr><tr><td rowspan="2">Tags × Socially endorsed people</td><td>Diagnosticity</td><td>1</td><td>3.16</td><td>2.90</td><td>0.10</td></tr><tr><td>Serendipity</td><td>1</td><td>7.58</td><td>7.49</td><td>0.01</td></tr></table>

Note. The control variable, users’ interest in exploring local restaurants, does not have a significant efect on any of the dependent variables.

Table 2. Means and Standard Deviations of the Four Conditions

<table><tr><td></td><td>With socially endorsed people</td><td>Without socially endorsed people</td></tr><tr><td colspan="3">Perceived diagnosticity</td></tr><tr><td>No tags</td><td>4.49 (1.30)</td><td>4.78 (1.07)</td></tr><tr><td>With tags</td><td>5.68 (0.85)</td><td>5.27 (1.04)</td></tr><tr><td colspan="3">Perceived serendipity</td></tr><tr><td>No tags</td><td>5.08 (0.97)</td><td>5.52 (0.99)</td></tr><tr><td>With tags</td><td>5.97 (0.85)</td><td>5.38 (1.26)</td></tr></table>

## Perceived Serendipity of Product Search

ANOVA results on perceived serendipity showed that the presence of tags had a significant main efect $( F ( 1 , \bar { 1 } 1 3 ) = 4 . 3 4 , \ p \ \stackrel { . } { < } 0 . 0 5 ) ;$ that ${ \mathrm { i } } \mathbf { s } ,$ the website with tags led to a higher level of perceived serendipity than the website without tags. Hence, H2 was supported. However, the presence of socially endorsed people did not have a significant efect on perceived serendipity $( F ( 1 , 1 1 3 ) = 0 . { \overset { \vartriangle } { 1 7 } } , \ p > 0 . 0 5 ) ;$ ; hence, H4 was not supported. There was a significant interaction efect between tags and socially endorsed people $( F ( 1 , 1 1 3 ) =$ 7.49, $p < 0 . 0 1 ;$ see Tables 1 and 2 and Figure 2). A simple main efect analysis showed that the website with product tags led to significantly higher perceived serendipity than the website without tags when socially endorsed people were featured $( p < 0 . 0 0 1 )$ but the efect of tags was not evident without socially endorsed people. A simple slope analysis also confirmed that the availability of tags positively afected perceived serendipity only when socially endorsed people were also present $( t = 3 . 1 7 , p < 0 . 0 1 )$ . Hence, H5 was supported.

## Decision Satisfaction

Partial least squares (PLS) was used to test the structural model regarding the efects of perceived diagnosticity and perceived serendipity on decision satisfaction. First, the measurement model was assessed. The measurement items generally loaded heavily on their respective constructs, with loadings above 0.70, demonstrating adequate reliability (Table 3). The high composite reliability and Cronbach alpha scores shown in Table 4 lent support to satisfactory internal consistency. Table 4 also shows that the square root of the average variance extracted (AVE) of each latent variable was greater than the correlations between that latent variable and all other latent variables, which indicated adequate discriminant validity (Barclay et al. 1995). Moreover, as shown in Table 3, the loadings of indicators on their respective latent variables were higher than the loadings of other indicators on these latent variables and the loadings of these indicators on other latent variables, thus lending further support to discriminant validity.

Figure 2. Interaction Plot on Perceived Serendipity  
![](/api/attachments/GTS3AR8U/fulltext/images/9623af12c90b3873590e208f22c3a2327e158aa744cd6f54059b01839bd8666b.jpg)

Table 3. Loadings and Cross-Loadings of Measures

<table><tr><td></td><td>Perceived diagnosticity</td><td>Perceived serendipity</td><td>Decision satisfaction</td></tr><tr><td>Diagnosticity1</td><td>0.82</td><td>0.34</td><td>0.37</td></tr><tr><td>Diagnosticity2</td><td>0.80</td><td>0.31</td><td>0.30</td></tr><tr><td>Diagnosticity3</td><td>0.79</td><td>0.29</td><td>0.40</td></tr><tr><td>Diagnosticity4</td><td>0.78</td><td>0.30</td><td>0.40</td></tr><tr><td>Serendipity1</td><td>0.29</td><td>0.87</td><td>0.35</td></tr><tr><td>Serendipity2</td><td>0.38</td><td>0.90</td><td>0.41</td></tr><tr><td>Serendipity3</td><td>0.40</td><td>0.88</td><td>0.47</td></tr><tr><td>Serendipity4</td><td>0.29</td><td>0.85</td><td>0.47</td></tr><tr><td>DecSat1</td><td>0.39</td><td>0.45</td><td>0.88</td></tr><tr><td>DecSat2</td><td>0.41</td><td>0.47</td><td>0.91</td></tr><tr><td>DecSat3</td><td>0.46</td><td>0.41</td><td>0.89</td></tr></table>

We next analyzed the structural model to examine the path significance. Results showed that both perceived diagnosticity $( \beta = 0 . 3 2 , p < 0 . 0 0 1 )$ and serendipity $( \beta = 0 . 3 7 , ~ p < 0 . 0 0 1 )$ had a significant and positive efect on decision satisfaction $( R ^ { 2 } = 3 3 . 3 \% )$ see Figure 3). Hence, H6 and H7 were supported. To further assess common method variance (CMV), we used the correlational marker-variable technique<sup>3</sup> (Malhotra et al. 2006) and found that the original correlations between decision satisfaction and diagnosticity as well as between decision satisfaction and serendipity did not difer much from their CMV-adjusted correlations $( \Delta r < 0 . 0 3 )$ , and the adjusted correlations were still significant $( p < 0 . 0 0 1 )$ . Hence, common method biases were not substantial.

To further verify that the two aspects of search experience indeed mediated the efect of the search mechanisms on decision satisfaction, a mediation analysis based on the bootstrap test was conducted in SPSS using the macro provided in Preacher and Hayes (2004) (with 5,000 bootstrap samples and 95% bias-corrected confidence intervals). The results showed that the indirect efect of product tags through search experience on decision satisfaction was positive and significant (95% $\mathrm { C I } = 0 . 1 7 \mathrm { t o } 0 . 2 3 ; p < 0 . 0 5 )$ while the direct efect became non-significant $( p > 0 . 0 5 )$ ; that is, perceived diagnosticity and serendipity mediated the efects of product tags on decision satisfaction. As tags were found to afect perceived serendipity only when socially endorsed people were featured, we then tested a moderated mediation model in which the indirect efect of product tags was presumed to be moderated by the presence of socially endorsed people. Using the SPSS macro introduced in Hayes (2013), we conducted a bootstrapping test and found that when socially endorsed people were present, the conditional indirect efect of tags through perceived serendipity of the search experience on decision satisfaction was significant (95% CI <sup></sup> 0.07 to 0.25; $p < 0 . 0 5 )$ , whereas this indirect efect was not evident when socially endorsed people were not featured (95% $\mathrm { C I } = - 0 . { \dot { 1 } } 4$ to $0 . 0 7 ; p > 0 . 0 5 )$ . Overall, the results suggested that perceived diagnosticity mediated the efects of product tags on decision satisfaction, while perceived serendipity mediated the efects of tags on decision satisfaction when endorsed people were featured.

Figure 3. Research Framework: Testing Results  
![](/api/attachments/GTS3AR8U/fulltext/images/bb2c17a554f8467d4568ce9c120e181dde42af47d4901e793c4502ea3a7a4eb9.jpg)

Table 4. Internal Consistency and Discriminant Validity of Constructs

<table><tr><td></td><td>Composite reliability</td><td>Cronbach&#x27;s alpha</td><td>Perceived diagnosticity</td><td>Perceived serendipity</td><td>Decision satisfaction</td></tr><tr><td>Perceived diagnosticity</td><td>0.88</td><td>0.81</td><td>0.80</td><td></td><td></td></tr><tr><td>Perceived serendipity</td><td>0.93</td><td>0.90</td><td>0.39</td><td>0.87</td><td></td></tr><tr><td>Decision satisfaction</td><td>0.92</td><td>0.88</td><td>0.47</td><td>0.49</td><td>0.89</td></tr></table>

Notes. Bold numbers show the square roots of the AVE values, while the of-diagonal elements are the correlations between the variables.

## Discussion and Supplementary Analyses

The experimental results of this study have provided valuable insights into the impacts of product tags and socially endorsed people on users’ product search experience. First, product tags were found to facilitate diagnostic product search, since they enable navigation among products that share common attributes. By contrast, featuring socially endorsed people alone does not facilitate a diagnostic product search. A plausible reason is that while access to these people’s profiles allows a user to obtain some valuable opinions, its potential benefit of facilitating coherent and logical product search and comparison is still limited since products favored by a socially endorsed individual can be diverse and some may not directly meet the user’s existing search needs. To further understand users’ actual search process and supplement these findings, we investigated the participants’ search sets, i.e., the sets of restaurants they accessed in the search process. In particular, we examined the efects of tags and socially endorsed people on the coherence of a search set, which indicated the extent to which a user’s product search was organized along particular themes or criteria. The coherence of a search set was estimated by calculating the average similarity of every two consecutively accessed restaurants.<sup>4</sup> The ANOVA results showed that users who were provided with tags had a more coherent search set than those who were not $( p <$ 0.05), whereas featuring socially endorsed people did not have such an efect. The results thus corroborate the main efects of tags on perceived diagnosticity and provide further support to our arguments that tags may convey a strong scent and attract users to follow them to access other alternatives with selected properties.

The results on perceived serendipity reveal that the efects of product tags and socially endorsed people reinforce each other, such that the presence of endorsed people enhances the efect of product tags on enabling unexpected useful discoveries. As we argued earlier, this is because access to endorsed people’s profiles may expose users to various diferent but interesting products, and such exposure enables users to identify an unexpected strong scent, thus augmenting the efect of tags on the perceived serendipity of subsequent search. To further support the assertion, we first examined the efects of socially endorsed people on the number of product clusters within a search set, which indicated the variety of the types of restaurants that users had considered during the process. Specifically, we classified and grouped restaurants in each search set based on their cuisine types. The ANOVA results revealed that featuring socially endorsed people led to a larger number of product clusters in a search set than when they were not featured $( p = 0 . 0 8 )$ . In other words, featuring socially endorsed people enabled users to access and consider more diversified alternatives in the search process. We then looked at how featuring socially endorsed people actually afected users’ access of product tags. We found that there was a significant diference between the condition with and without featured socially endorsed people in terms of the total number of distinct tags accessed. When socially endorsed people were present, participants on average accessed 4.2 distinct tags in the search process, whereas when socially endorsed people were absent, participants accessed only 2.3 distinct tags on average (p < 0.05).<sup>5</sup> This result indicates that information from socially endorsed people has indeed invoked users’ interests in exploring diverse search dimensions represented by tags.

However, our main results also show that featuring socially endorsed people alone does not improve the perceived serendipity of the search experience. A plausible reason is that the mere exposure to diversified alternatives without an efective way to conduct subsequent search and investigation does not help users make sense of the options or connect them with their needs. As a result, users are unlikely to take advantage of the unexpected findings and hence serendipity may not occur. In fact, foraging for more information and making sense of the findings often form a feedback loop that underpins an information search process (Pirolli and Card 2005). Agarwal (2015) also suggests that a serendipitous discovery is always an encounter followed by a period of attaching insight and value to the information encountered. In the current context, without the availability of product tags, users are unlikely to act on the new findings from a socially endorsed user’s profile because of the dificulty in conducting a follow-up investigation to understand each alternative and compare it with others, and hence they may not perceive the new findings as useful. To minimize the cognitive efort spent on processing these diverse unexpected findings, users may even become less open and explorative. This may also help explain the slightly lower level of perceived serendip ity (albeit insignificant) in the condition where socially endorsed people are featured compared with the condition where they are not (in the absence of product tags). The presence of tags associated with each product, on the other hand, may help users eficiently recognize, appreciate, and trace the unique features of the products discovered from the socially endorsed individuals’ profiles, leading to other related serendipitous findings in new domains. This is consistent with the central argument of IFT, i.e., foragers tend to pursue a new search route if it can provide an information gain with a minimized cost of exploration. Overall, tag-based logical search is critical to further realizing the value of the interesting findings encountered via people-based search and to achieving quality and serendipity in search.

It is worthwhile to note that both perceived diagnosticity and serendipity positively afect decision satisfaction, and they also mediate the influence of product tags on decision satisfaction. While prior research has advocated the use of decision aids or recommendation agents that can improve users’ decision quality by eficiently matching information with established needs, we suggest that users can be motivated by rich environmental cues and benefit from exploring both expected and unexpected options. These findings thus point to the importance of understanding how consumers actually search for products and make satisfying choices.

## Implications of Findings Theoretical Implications

This study focuses on two important social search features on social commerce platforms—product tags and socially endorsed people—and examines their efects on consumers’ perceived diagnosticity and serendipity of their product search experience. Specifically, through collaboration with one of the largest socialnetwork-based product search websites in China, this study evaluated these design features in a wellcontrolled lab experiment using real data about products, users, and user-generated information. Such a research setting allows us to clearly investigate the separate and joint influences of the two search features. This study has several theoretical implications.

First, this study investigates product search in a new context, i.e., search based on user-generated information. Prior IS studies have investigated various online product search tools, such as online catalogues, recommendation agents, and search engines, which typically incorporate explicit search keywords or users’ past behavior patterns to provide focused and personalized suggestions (e.g., Adomavicius and Tuzhilin 2005, Ho and Bodof 2014, Kamis et al. 2008, Xiao and Benbasat 2007). With the widespread availability of social commerce platforms, a number of new features based on user-generated information have emerged to support users’ information searches. Compared to traditional search tools, social search features are often less structured and allow users more flexibility in choosing what content to follow. Hence, they are conducive to adaptive product search. This research thus contributes to the IS literature by focusing on two social search features, namely, product tags and socially endorsed people, and showing how they jointly influence users’ product search experience.

Second, while considerable knowledge on human information search behavior has accrued over the past two decades (e.g., Browne et al. 2007, Johnson et al. 2004, Kim 2009), the concept of serendipity is often overlooked in theoretical models of informationseeking behavior (Agarwal 2015). Most prior research related to IFT also studies an information forager’s linkfollowing behavior in a context where the forager has a fully formed goal and looks for a precise answer (e.g., Lawrance et al. 2010, Olston and Chi 2003). A resulting prescription is that search systems should facilitate an eficient search process centered at a defined need (e.g., Fang et al. 2012). However, users’ preferences may change as they encounter new information, and their selection of search cues reflects their dynamic goals. This research thus fills in this gap by studying how the design of search cues afects the quality of users’ search experience in terms of both diagnosticity and serendipity. Our findings suggest that users may be intrigued and attracted by unexpected interesting information en route (e.g., from endorsed people’s profiles) and conduct unplanned exploration if navigation is facilitated (e.g., via product tags). A satisfying final choice can result from a diagnostic process that enables a logical and coherent way of product search and comparison, and also from a serendipitous process that reveals unexpected valuable findings during the course of search. Overall, divergent and serendipitous discovery together with coherent search pertaining to a specific agenda provide a holistic approach to studying social information acquisition and decision making.

Third, this study adopts IFT as an overarching theory to explain the efects of product tags and socially endorsed people on users’ perceived diagnosticity and serendipity of search. Prior IFT studies have advocated the design of scentful cues that clearly describe the linked content (termed as “trigger words”; Nielsen 2003, Spool et al. 2004). Our study identifies two types of scentful cues in the UGC context, namely, product tags and socially endorsed people. While the former are a natural form of semantic search cues that may explicitly match or invoke users’ information needs in terms of product features, the latter do not directly convey topically relevant or descriptive product information, but serve as high-quality information sources that appear scentful to foragers. More important, our study further reveals that diferent scentful cues do not function independently, but can reinforce each other in enabling users to make and consider unexpected discoveries.

## Practical Implications

The most direct message to website designers is that organizing and exploiting the potential of large-scale UGC is crucial. The provision of rich social information and enabling tag-based traceability among content is important in constructing a well-connected product network. In this way, users’ ability to search and evaluate products can be largely improved. More important is that identifying and providing connections to widely endorsed members within the community is critical to realizing the efects of tag-based product navigation on creating a serendipitous search. This is because browsing these individuals’ collections may increase users’ exposure to novel and promising products and hence the associated interesting tags, which enables subsequent tag-based search to expand to novel domains. However, merely providing users with the access to endorsed people will not be helpful in improving users’ product searches, since users may easily get disoriented when they are exposed to a large amount of diverse information without other clues (such as tags) to make sense of the information. Our research thus highlights the importance of integrating the two distinct forms of social navigation mechanisms, i.e., tag-based and people-based navigation, on social commerce platforms.

## Limitations

This study is not without limitations. First, the applicability of our findings may be contingent on product categories. Compared with evaluating many physical goods, consumers tend to rely on word-of-mouth information when searching for and evaluating restaurants. Hence, restaurants are often categorized as experience goods, that is, products or services whose evaluation is often based on subjective views rather than objective descriptions (Nelson 1970). We thus believe that restaurant search is a proper context to reveal the efects of social search cues such as tags and socially endorsed users. Nonetheless, generalization of the current results to other products must be made cautiously.

Second, the findings of our study are best applied to product search tasks with a general search goal so that users tend to perform scent-based information foraging (e.g., searching for a restaurant for friends’ gathering in our study; David et al. 2007). They cannot directly address many of the other ways in which users might use tags and social networks. For example, people may browse information completely out of curiosity or entertainment without a general search goal, which represents a form of lightweight learning (Millen et al. 2006) and renders logical investigation less relevant. On the contrary, highly structured information searches with clear, predetermined targets may make serendipitous discoveries generally inapplicable. When users have established well-defined specific goals, they tend to focus on goal attainment and are generally less receptive to novel information. Hence, the efects of tag-based and people-based search may difer for diferent search tasks.

Third, participants in this study were college students. Since this study was conducted in a university located in a large city and it was common for students to dine in local restaurants, the experimental task and context were reflective of a typical search situation for those students. However, we do note that since student consumers are relatively young, they may not precisely represent the overall population of online shoppers. For example, it is possible that other consumer segments are more motivated and experienced in restaurant search, and hence conduct searches in diferent ways (e.g., Pak et al. 2009). Future research may want to extend the current study by examining online product search behavior of other consumer segments.

## Suggestions for Future Research

Increasingly more websites nowadays are exploiting the power of resource sharing and social connection to help users with product information seeking and decision making. This study adopts IFT as the overarching theory to understand users’ product search behavior on social commerce platforms. We use the cognitive rules suggested in IFT (i.e., people follow a scent to look for information, seeking to minimize eforts) to explain how users will follow social search cues to gather various alternatives. Future studies are encouraged to operationalize the core concepts in IFT (such as information scent) and test the theory formally in the context of information search on platforms with rich UGC.

This study demonstrates that users can benefit from knowledge shared by others whom they may not have known previously, be it through tags or people profiles. In particular, this study focuses on socially endorsed people as a type of search cue, as these individuals are likely to be perceived as high-quality information sources based on community judgment. Future studies can extend the current research by looking at how expert users or opinion leaders certified by the information platform (without explicit social endorsement) or even other “unpopular” people may facilitate users information search. It will be interesting to examine how diferent types of “scent” related to information sources (other than social endorsement) direct users’ search. Another possibility is to enable connections to users’ existing friends while they shop online (Zhu et al. 2010). For example, Facebook Connect aims to bring users’ identities and existing social connections to various other websites. Future research can thus investigate the efectiveness of search features based on connectivity among users who are already acquainted with each other.

Future studies can also extend the investigation of search serendipity by seeking other measures of serendipity. While this study measures users’ perception of search serendipity, future studies may examine users’ serendipitous search behavior in a field setting with information about their past and current search preferences and measure the deviations between them. A combination of objective and subjective indicators should further contribute to our understanding of serendipitous information search. In addition, social search features such as tags have been applied to various products and services on diferent social commerce platforms. It would be interesting to investigate how social information facilitates serendipitous search of diferent types of goods in a field setting.

## Conclusion

Despite the widespread availability of social commerce platforms, significant research progress on users’ information behavior in such context is yet to be made. This study represents one of the first attempts to investigate how UGC-based product search features on social commerce platforms shape the diagnosticity and serendipity of users’ product search experience. Our results reveal that product tags enable users to locate and evaluate relevant alternatives, thus enhancing the perceived search diagnosticity, whereas the integration of tags and featured socially endorsed people enables users to discover more unexpected interesting alternatives. These findings serve as a basis for future theoretical development in the area of consumer information search and yield valuable insights for social commerce practitioners.

## Appendix. Measurement Items for Dependent Variables

A.1. Perceived Diagnosticity of the Product Search Experience (adapted from Jiang and Benbasat 2004, Kempf and Smith 1998)

• This website helps me to systematically and efectively search among and compare many diferent restaurants in order to find the most suitable one.

• This website helps me to efectively evaluate the restaurants I browsed in the search process based on information from other consumers.

• This website provides me a chance to search among and assess many restaurants in a systematic and efective way.

• Through this website I can quickly obtain a good understanding of the main features of the restaurants that I browsed in the search process.

## A.2. Perceived Serendipity of the Product Search Experience (adapted from Oku and Hattori 2012)

• The restaurant search experience I just had helped me discover some restaurants which suit my needs but I had not planned for.

• My restaurant search on this website provided some unexpected but useful findings.

• In the search process I encountered many good restaurants which were worth a try but were beyond my initial search plans.

• The website experience provided me with some surprising yet interesting findings about restaurants in the search process.

## A.3. Decision Satisfaction (adapted from

Pereira 2001)

• I am satisfied with my decision when picking restaurants.

• I believe that my choice of restaurant meets my needs well.

• I am happy with my choice of restaurant on this website.

## Endnotes

<sup>1</sup> We mask the real name of the company for confidentiality purposes.

<sup>2</sup> The identities of the users were anonymized.

<sup>3</sup> The marker variable used in this study was users’ Internet experience, which was unrelated to other study variables and used the same measurement scale as the other variables. CMV-adjusted correlations were computed by partialling out the average correlation between the marker variable and the other variables from the uncorrected correlations.

<sup>4</sup> Specifically, we measured the similarity of two restaurants in terms of the type of cuisine, which was the major defining characteristic of restaurants. If the cuisine types of two restaurants were the same, their similarity was coded 1. Otherwise, it was coded 0. We then computed the average similarity of every pair of restaurants consecutively accessed to represent the coherence of the entire search set.

<sup>5</sup> We also found that 82% of distinct tag accesses (across conditions) centered on the top five most popular tags (indicated by the associated numbers) on the page (among approximately 20 tags on a page); that is, the more popular tags were generally more often accessed, plausibly because these tags also described the most important and salient product properties likely to be sought for, hence conveying a stronger scent than less popular tags. This also strengthens our main argument that the mechanism of product tagging enables users to find scentful search cues.

## References

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6):734–749.

Adomavicius G, Bockstedt JC, Shawn PC, Zhang J (2013) Do recommender systems manipulate consumer preferences? A study of anchoring efects. Inform. Systems Res. 24(4):956–975.

Agarwal NK (2015) Towards a definition of serendipity in information behaviour. Inform. Res. 20(3):Paper 675.

Ames M, Naaman M (2007) Why we tag: Motivations for annotation in mobile and online media. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 971–980.

Andel PV (1994) Anatomy of the unsought finding. Serendipity: Origin, history, domains, traditions, appearances, patterns and programmability. British J. Philos. Sci. 45(2):631–648.

Ashman H, Brailsford T, Cristea AI, Sheng QZ, Stewart C, Toms EG, Wade V (2014) The ethical and social implications of personalization technologies for e-learning. Inform. Management 51(6):819–832.

Banerjee AV (1992) A simple model of herd behavior. Quart. J. Econom. 107(3):797–817.

Barclay D, Thompson R, Higgins C (1995) The partial least squares (PLS) approach to causal modeling: Personal computer adoption and use as an illustration. Tech. Stud. 2(2):285–309.

Berry J, Keller E (2003) The Influentials: One American in Ten Tells the Other Nine How to Vote, Where to Eat, and What to Buy (Free Press, New York).

Biel JI, Gatica-Perez D (2009) Wearing a YouTube hat: Directors, comedians, gurus, and user aggregated behavior. Proc. 17th ACM Internat. Conf. Multimedia (ACM, New York), 833–836.

Browne GJ, Pitts MG, Wetherbe JC (2007) Cognitive stopping rules for terminating information search in online task. MIS Quart. 31(1):89–104.

Burt RS (1999) The social capital of opinion leaders. Ann. Amer. Acad. Political Soc. Sci. 566(1):37–54.

Canini KR, Suh B, Pirolli P (2011) Finding credible information sources in social networks based on content and social structure. Third IEEE Internat. Conf. Soc. Comput., Boston.

Chaiken S (1987) The heuristic model of persuasion. Zanna MP, Olsen JM, Herman CP, eds. Social Influence: The Ontario Symposium, Vol. 5 (Lawrence Erlbaum, Hillsdale, NJ), 3–39.

Chi EH (2009) Information seeking can be social. Computer 42(3): 42–46.

Choi B, Jiang Z, Xiao B, Kim S (2015) Embarrassing exposures in online social networks: An integrated perspective of relationship bonding and privacy invasion. Inform. Systems Res. 26(4): 675–694.

Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences (Lawrence Erlbaum, Hillsdale, NJ).

David P, Song M, Hayes A, Fredin ES (2007) A cyclic model of information seeking in hyperlinked environment: The role of goals, self-eficacy, and intrinsic motivation. Internat. J. Human-Comput. Stud. 65(2):170–182.

Dew N (2009) Serendipity in entrepreneurship. Organ. Stud. 30(7): 735–753.

Evans B, Chi E (2008) Towards a model of understanding social search. Proc. 2008 ACM Comput. Supported Cooperative Work <sup>(</sup>CSCW<sup>)</sup> (ACM, New York), 485–494.

Fang X, Hu PJH, Chau M, Hu HF, Yang Z, Sheng ORL (2012) A datadriven approach to measure Web site navigability. J. Management Inform. Systems 29(2):173–212.

Foster A, Ford N (2003) Serendipity and information seeking: An empirical study. J. Documentation 59(3):321–340.

Franke N, Hippel EV, Schreier M (2006) Finding commercially attractive user innovation: A test of lead-user theory. J. Product Innovation Management 23(4):301–315.

Fu WT (2008) The microstructures of social tagging: A rational model. Proc. 2008 ACM Comput. Supported Cooperative Work (ACM, New York), 229–238.

Giraldeau L-A, Caraco T (2000) Social Foraging Theory (Princeton University Press, Princeton, NJ).

Gladwell M (2002) The Tipping Point: How Little Things Can Make a Big Diference (Little, Brown and Company, Boston).

Goes P, Lin M, Yeung CA (2014) “Popularity efect” in user-generated content. Inform. Systems Res. 25(2):222–238.

Goldenberg J, Oestreicher-Singer G, Reichman S (2012) The quest for content: How user-generated links can facilitate online exploration. J. Marketing Res. 49(4):452–468.

Golder SA, Huberman BA (2006) Usage patterns of collaborative tagging systems. J. Inform. Sci. 32(2):198–208.

Golin M (1957) Serendipity—Big word in medical progress. J. Amer. Medical Assoc. 165(16):2084–2087.

Graebner ME (2004) Momentum and serendipity: How acquired leaders create value in the integration of technology firms. Strategic Management J. 25(8–9):751–777.

Gray PH, Parise S, Iyer B (2011) Innovative impacts of using social bookmarking systems. MIS Quart. 35(3):629–643.

Gupta M, Li R, Yin Z, Han J (2011) An overview of social tagging and applications. Aggarwal C, ed. Social Network Data Analytics (Springer, New York), 447–497.

Haubl G, Trift V (2000) Consumer decision making in online shopping environments: The efects of interactive decision aids. Marketing Sci. 19(1):4–21.

Hayes AF (2013) Introduction to Mediation, Moderation and Conditional Process Analysis (Guilford Press, New York).

Herlocker JL, Konstan JA, Terveen LG, Riedl JT (2004) Evaluating collaborative filtering recommender systems. ACM Trans. Inform. Systems 22(1):5–53.

Ho SY, Bodof D (2014) The efects of Web personalization on user attitude and behavior: An integration of the elaboration likelihood model and consumer search theory. MIS Quart. 38(2): 497–520.

Iyengar R, Van den Bulte C, Valente TW (2011) Opinion leadership and social contagion in new product difusion. Marketing Sci. 30(2):195–212.

Jiang Z, Benbasat I (2004) Virtual product experience: Efects of visual and functional control on perceived diagnosticity in electronic shopping. J. Management Inform. Systems 21(3):111–147.

Johnson EJ, Moe WW, Fader PS, Bellman S, Lohse GL (2004) On the depth and dynamics of online search behavior. Management Sci. 50(3):299–308.

Kamis A, Koufaris M, Stern T (2008) Using an attribute-based DSS for user-customized products online: An experimental investigation. MIS Quart. 32(1):159–177.

Katz MA, Byrne MD (2003) Efects of scent and breadth on use of sitespecific search on e-commerce websites. ACM Trans. Comput.- Human Interaction 10(3):198–220.

Kempf DS, Smith RE (1998) Consumer processing of product trial and the influence of prior advertising: A structural modeling approach. J. Marketing Res. 35(3):325–338.

Kim J (2009) Describing and predicting information-seeking behavior on the Web. J. Amer. Soc. Inform. Sci. Tech. 60(4):679–693.

Klein DE (2008) The loss of serendipity in psychopharmacology. J. Amer. Medical Assoc. 299(9):1063–1065.

Kratzer J, Lettl C (2009) The distinctive role of lead users and opinion leaders in the social networks of schoolchildren. J. Consumer Res. 36(4):646–659.

Krug S (2006) Don’t Make Me Think: A Common Sense Approach to the Web Usability, 2nd ed. (New Riders Publishing, Thousand Oaks, CA).

Larson K, Czerwinski M (1998) Web page design: Implications of memory, structure and scent for information retrieval. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 25–32.

Lawrance J, Bellamy R, Burnett M (2007) Scents in programs: Does information foraging theory apply to program maintenance? Proc. IEEE Sympos. Visual Languages Human-Centric Comput., Coeur d’Alène, Idaho, 15–22.

Lawrance J, Burnett M, Bellamy R, Bogart C, Swart C (2010) Reactive information foraging for evolving goals. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 25–34.

Lee L, Ariely D (2006) Shopping goals, goal concreteness and conditional promotions. J. Consumer Res. 33(1):60–70.

Malhotra NK, Kim SS, Patil A (2006) Common method variance in IS research: A comparison of alternative approaches and a reanalysis of past research. Management Sci. 52(12):1865–1883.

McAfee AP (2006) Enterprise 2.0: The dawn of emergent collaboration. Sloan Management Rev. 47(3):21–28.

McCay-Peet L, Toms EG (2011) Exploring the precipitating conditions of serendipity. Proc. 2nd Annual Graphics, Animation New Media NCE Conf., Vancouver, BC, Canada.

McKenzie PJ (2003) A model of information practices in accounts of everyday-life information seeking. J. Documentation 59(1):19–40.

Metzger MJ, Flanagin AJ (2013) Credibility and trust of information in online environments: The use of cognitive heuristics. J. Pragmatics 59:210–220.

Millen DR, Feinberg J, Kerr B (2006) Dogear: Social bookmarking in the enterprise. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 111–120.

Moody G, Galletta DF (2015) Lost in cyberspace: The impact of information scent and time constraints on stress, performance, and attitudes. J. Management Inform. Systems 32(1):192–224.

Nahapiet J, Ghoshal S (1998) Social capital, intellectual capital, and the organizational advantage. Acad. Management Rev. 23(2): 242–266.

Nelson PJ (1970) Information and consumer behavior. J. Political Econom. 78(2):311–329.

Nielsen J (2003) Information foraging: Why Google makes people leave your site faster. Nielsen Norman Group (June 30), https:// www.nngroup.com/articles/information-scent/.

Oku K, Hattori F (2012) User evaluation of fusion-based approach for serendipity-oriented recommender system. Proc. Workshop Recommendation Utility Evaluation: Beyond RMSE (RUE 2012), Dublin, Ireland, 39–44.

Olston C, Chi EH (2003) ScentTrails: Integrating browsing and searching on the Web. ACM Trans. Comput.-Human Interaction 10(3):177–197.

Otter M, Johnson H (2000) Lost in hyperspace: Metrics and mental models. Interacting Comput. 13(1):1–40.

Pak R, Price MM, Thatcher J (2009) Age-sensitive design of online health information: Comparative usability study. J. Medical Internet Res. 11(4):e45.

Pavlou PA, Fygenson M (2006) Understanding and predicting electronic commerce adoption: An extension of the theory of planned behavior. MIS Quart. 30(1):115–143.

Pavlou PA, Liang H, Xue Y (2007) Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quart. 31(1):105–136.

Payne JW, Bettman JR, Johnson EJ (1992) Behavioral decision research: A constructive processing perspective. Annual Rev. Psych. 43(1):87–131.

Pereira RE (2001) Influence of query-based decision aids on consumer decision making in electronic commerce. Inform. Resources Management J. 14(1):31–48.

Pirolli P (2007) Information Foraging: A Theory of Adaptive Interaction with Information (Oxford University Press, New York).

Pirolli P (2009) An elementary social information foraging model. Proc. SIGCHI Human Factors Comput. Systems Conf. (ACM, New York), 605–614.

Pirolli P, Card SK (1999) Information foraging. Psych. Rev. 106(4): 643–675.

Pirolli P, Card SK (2005) The sensemaking process and leverage points for analyst technology as identified through cognitive task analysis. Proc. Internat. Conf. Intelligence Anal., McLean, VA.

Preacher KJ, Hayes AF (2004) SPSS and SAS procedures for estimating indirect efects in simple mediation models. Behav. Res. Methods, Instruments, Comput. 36(4):717–731.

Rivoal I, Salazar NB (2013) Contemporary ethnographic practice and the value of serendipity. Soc. Anthropology 21(2):178–185.

Roberts RM (1989) Serendipity: Accidental Discoveries in Science (Wiley, New York).

Shami NS, Muller M, Millen D (2011) Browse and discover: Social file sharing in the enterprise. Proc. ACM 2011 Conf. Comput. Supported Cooperative Work (ACM, New York), 295–304.

Simon HA (1955) A behavioral model of rational choice. Quart. J. Econom. 69(1):99–118.

Sin SCJ, Kim KS (2013) International students’ everyday life information seeking: The informational value of social networking sites. Library Inform. Sci. Res. 35(2):107–116.

Speier C, Morris MG (2003) The influence of query interface design on decision-making performance. MIS Quart. 27(3):397–423.

Spool JM, Perfetti C, Brittan D (2004) Designing for the Scent of Information (User Interface Engineering, Middleton, MA).

Sun T, Zhang M, Mei Q (2013) Unexpected relevance: An empirical study of serendipity in retweets. Proc. 7th Internat. Conf. Web Soc. Media, Boston.

Swearingen K, Sinha R (2001) Beyond algorithms: An HCI perspective on recommender systems. Proc. ACM SIGIR 2001 Workshop Recommender Systems, New Orleans.

Trier M, Molka-Danielsen J (2013) Sympathy or strategy: Social capital drivers for collaborative contributions to the IS community. Eur. J. Inform. Systems 22(3):317–335.

Trusov M, Bodapati AV, Bucklin RE (2010) Determining influential users in Internet social networks. J. Marketing Res. 47(4):643–658.

Wixom BH, Todd P (2005) A theoretical integration of user satisfaction and technology acceptance. Inform. Systems Res. 16(1):85–102.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1): 137–209.

Yi C, Jiang Z, Benbasat I (2015) Enticing and engaging consumers via online product presentations: The efects of restricted interaction design. J. Management Inform. Systems 31(4):213–242.

Yi C, Jiang Z, Zhou M (2014) The efects of social popularity and deal scarcity at diferent stages of online shopping. Proc. Internat. Conf. Inform. Systems (ICIS), Auckland, New Zealand.

Zeng X, Wei L (2013) Social ties and user content generation: Evidence from Flickr. Inform. Systems Res. 24(1):71–87.

Zhang J, Liu Y, Chen Y (2015) Social learning in networks of friends versus strangers. Marketing Sci. 37(4):573–589.

Zhang YC, Seaghdha D, Quercia D, Jambor T (2012) Auralist: Introducing serendipity into music recommendation. Proc. 5th ACM Internat. Conf. Web Search Data Mining (ACM, New York), 13–22.

Zhu L, Benbasat I, Jiang Z (2010) Let’s shop online together: An empirical investigation of collaborative online shopping support. Inform. Systems Res. 21(4):872–891.

Ziegler CN, McNee SM, Konstan JA, Lausen G (2005) Improving recommendation lists through topic diversification. Proc. 14th Internat. Conf. World Wide Web (ACM, New York), 22–32.
