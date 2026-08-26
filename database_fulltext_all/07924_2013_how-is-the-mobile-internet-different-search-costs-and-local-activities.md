---
otero_id: 7924
otero_key: "GS9ZADZ5"
title: "How Is the Mobile Internet Different? Search Costs and Local Activities"
authors: "Anindya Ghose; Avi Goldfarb; Sang Pil Han"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0453"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How Is the Mobile Internet Different? Search Costs and Local Activities

Anindya Ghose

Stern School of Business, New York University, New York, New York 10012, aghose@stern.nyu.edu

Avi Goldfarb

Rotman School of Management, University of Toronto, Toronto, Ontario M5S 3E6, Canada, agoldfarb@rotman.utoronto.ca

Sang Pil Han

College of Business, City University of Hong Kong, Kowloon, Hong Kong, sangphan@cityu.edu.hk

W<sup>e</sup> <sup>explore</sup> <sup>how</sup> <sup>Internet</sup> <sup>browsing</sup> <sup>behavior</sup> <sup>varies</sup> <sup>between</sup> <sup>mobile</sup> <sup>phones</sup> <sup>and</sup> <sup>personal</sup> <sup>computers.</sup> <sup>Smaller</sup> a wider range of offline locations for mobile Internet usage suggests that local activities are particularly important. Using data on user behavior at a (Twitter-like) microblogging service, we exploit exogenous variation in the ranking mechanism of posts to identify the ranking effects. We show that (1) ranking effects are higher on mobile phones suggesting higher search costs: links that appear at the top of the screen are especially likely to be clicked on mobile phones and (2) the benefit of browsing for geographically close matches is higher on mobile phones: stores located in close proximity to a user’s home are much more likely to be clicked on mobile phones. Thus, the mobile Internet is somewhat less “Internet-like”: search costs are higher and distance matters more. We speculate on how these changes may affect the future direction of Internet commerce.

Key words: mobile Internet; search costs; ranking effects; cognitive load; recency effects; local interests; microblogging; social media; hierarchical Bayesian methods

History: Ram Gopal, Senior Editor; Ramnath Chellappa, Accociate Editor. This paper was received on October 31, 2011, and was with the authors 1 month for 1 revision. Published online in Articles in Advance

## 1. Introduction

After nearly two decades of research on the economic consequences of the Internet, two findings have consistently appeared in the literature: the Internet can overcome geographic isolation (Balasubramanian 1998, Forman et al. 2009, Choi and Bell 2011, etc.) and search costs are lower online (Bakos 1997, Baye et al. 2009, etc.). The geographic isolation results emphasize both physical travel costs and spatial dimensions of preferences. The search cost results emphasize the ease of surfing from one website to another and of comparing lists of products and prices, though they note that search costs are not zero. In particular, search costs are constrained above zero by the cognitive effort required to read through a list. The rank ordering of a list of links substantially impacts click-throughs in a variety of contexts including yellow pages ads, music choices of unknown songs, Google listings, movie or hotel listings, etc. (Ansari and Mela 2003, Drèze and Zufryden 2004, Baye et al. 2009, Ghose and Yang 2009, Yang and Ghose 2010, Brynjolfsson et al. 2010, Yao and Mela 2011, Agarwal et al. 2011, etc.) Reduced geographic isolation and reduced effort in the collection of information suggest that the addition of the Internet channel has generated increased competition for both online and offline firms. Although companies try to mitigate these effects with obfuscation, differentiation, and targeting (Ellison and Ellison 2009, Brynjolfsson et al. 2010, etc.), the fundamental shift is to an increasingly competitive e-commerce environment.

As consumers increasingly use mobile phones to access the Internet, it is important to understand when and how these results on geography and cognitive effort transfer to the use of different devices. Currently, we have little understanding of whether mobile user behavior matches behavior on personal computers (PCs). There are reasons to expect both similarities and differences. The two are similar because both provide instant access to roughly the same Internet sources with vast amounts of information. The browsing experience, however, is different for three main reasons. First, mobile phones typically have smaller screens than do PCs. Second, mobile phones are, by definition, portable and not fixed to a location. Third, because of the portability, mobile users have access to timely information.

The purpose of this paper is to empirically examine how user browsing behavior differs between a mobile phone and a PC. In an online world that is increasingly accessed with mobile phones, the results have important implications for the academic discussion of Internet commerce, social media, and digital marketing.

We examine both search costs and the role of geographic proximity based on user behavior on the mobile Internet and the PC-based Internet.<sup>1</sup> Because consumers exert more cognitive effort (and perhaps more physical effort) while scrolling down a list of items displayed on small screens, we expect the ranking effect based search costs to be higher on a mobile phone as compared to a PC. We expect this to be true regardless of whether users engage in directed search or undirected browsing. In addition, because it might be both particularly easy and particularly valuable for mobile phone users to visit nearby stores, we expect geographic proximity to be more important on a mobile phone than on a PC.

We examine these relationships using data from a South Korean microblogging website similar to Twitter. As on Twitter, users share their thoughts in short posts distributed by the mobile phone-based or PC-based Web. A microblog differs from a traditional blog in that its content is typically much smaller in size, consisting of a short sentence or fragment described within a limit of 140 characters. The central feature of microblogging is a stream of messages (i.e., tweets) that a user receives from those he or she follows. In our setting, these messages are listed in reverse chronological order and contain clickable links. Users log into the website to browse posts and click on links that interest them. We have information on all such links related to brands for 260 distinct users between November 29, 2009, and March 6, 2010.

We estimate whether the user clicked on the link as a function of the access technology (mobile phones or PCs), the rank of the link on the screen, and the geographical distance between the user’s address and the retail location of the brand mentioned in the link. Rank allows us to measure the search cost incurred because of ranking effects. Higher ranking effects mean that it is more valuable to be ranked near the top. Distance allows us to examine the role of geography and local activities of users. User decisions are captured and estimated with a revealed preference econometric model of user clicking behavior that controls for recency effects, user and post heterogeneity, and other factors.

For identification of ranking effects, we exploit a source of randomization in the ranking mechanism that generates these microblog posting feeds. The rank is determined only by the timing of the posting by the creator, the frequency of log-in by the user, and the number of feeds that the user follows, independent of any prior click-through decisions by users and brand advertisement by advertisers. Therefore we identify the ranking effect in a setting where lists are not ordered to an intrinsic valuation of the items on the list. We use post-specific fixed effects to control for post quality. To control for user heterogeneity beyond our controls (specifically, post tenure, age, gender, and the number of followees), we also include user-level random coefficients in a hierarchical Bayesian framework and estimate it with Markov Chain Monte Carlo methods, using an adaptive Metropolis-Hastings algorithm. Focusing on the first appearance of a brand post, the posting mechanism provides exogenous variation in the ranking under the assumption that our controls capture the user-level potential confounds. In this way, variation in the posting mechanism can be seen as something like a natural experiment in ranking.

Our analysis yields two main results. First, the negative and statistically significant relationship between the rank of a post and a click on that post is much stronger for mobile users than for PC users. For PC users, moving one position upward in rank yields an increase in the odds of clicking on that brand post by 25%. For mobile phone users, a one position upward increase in rank yields an increase in the odds of clicking on that brand post by 37%. This result suggests that ranking effects are higher on mobile phones.

Second, we find that the benefit of browsing for geographically proximate brands is higher on mobile phones. For PC users, a one mile decrease in distance between a user and a brand store yields an increase in the odds of clicking on that brand post by 12%. For mobile users, a one mile decrease in distance between a user and a brand store yields an increase in the odds of clicking on that brand post by 23%. This result suggests that there are stronger local interests for mobile users than for PC users. These results are robust to a variety of alternative specifications and controls.

In this way, the mobile Internet is somewhat less “Internet-like”: ranking effects are higher and distance matters more. Given that high ranking effects suggest increased cognitive effort required for information processing, search, whether directed or undirected, will be more costly on the mobile Internet. Speculatively, this suggests that the features of the Internet market that depend on low search costs and reduced geographic isolation will change as the mobile Internet becomes proportionately larger.

In addition, the coefficient estimates on one of our controls are suggestive of a likely exception to interpreting our ranking effects results to mean that search costs are higher on the mobile Internet: the cost of acquiring timely information is lower on a mobile phone than on a PC. That is, our results suggest that more recent posts are more likely to be clicked on a mobile phone.

Overall, this paper provides an understanding of how the mobile Internet is different from the PC-based Internet. Such an understanding is important as online search, browsing, and purchase behavior increasingly move to mobile devices. However, to our knowledge, no prior academic work has scientifically documented how the mobile Internet is different or similar to the PC-based Internet. By demonstrating that users’ preferences for proximate brands are stronger when using a mobile phone and that ranking effects are higher when using a mobile phone, our paper provides insight for managers regarding the future potential of mobile commerce.

## 2. Related Literature

In this section, we explain why it is important to examine ranking effects and distance effects. We also discuss some other related literature.

## 2.1. Why Do Ranking Effects Matter?

A long literature suggests that there are primacy effects on choice, or benefits to being first or early in a sequence (Becker 1954, Miller and Krosnick 1998, Carney and Banaji 2008, etc.). Most people start browsing from the top of lists, so higher ranked items are likely to receive more attention. These effects have been documented in a variety of contexts such as food and beverages (Coney 1977, Dean 1980), elections (Miller and Krosnick 1998), and elsewhere. In the online context, a number of papers have shown that primacy effects have important market consequences. For example, better ranked links are more likely to be clicked in desktop environments (Ansari and Mela 2003, Drèze and Zufryden 2004, Baye et al. 2009, Ghose and Yang 2009, Yang and Ghose 2010, Agarwal et al. 2011).

Ranking effects matter because they have implications for managerial strategies and equilibrium outcomes. The literature on ranking effects suggests that they are driven by the effort required to scroll down a list of items. Higher ranking effects suggest a higher degree of effort required. When the list of items represents the outcome of a directed search, such effort is clearly related to a search cost. Even when the list of items represents the outcome of browsing or undirected surfing, such effort is still related to the likelihood of scanning all items on a list and therefore can be viewed as a search cost in an undirected search. Ranking effects are therefore often interpreted as a type of search cost in an online setting (e.g., Yao and Mela 2011). Brynjolfsson et al. (2010) have quantified such search costs as quite substantial in online settings when users are exposed to multiple offers on a computer screen, as in a shopbot setting. In this way, even in our setting of undirected browsing, ranking effects may have an impact similar to those of the search costs modeled in the PC-based Internet literature.

A small screen may increase ranking effects because the narrow view can cause information chunking and users to lose a global perspective of the task, incurring cognitive load (Nunamaker et al. 1987, 1988). Numerous studies have documented that the small screens of mobile phones create a serious obstacle to users’ navigation activities and perceptions (Chae and Kim 2004); hence, they reduce the effectiveness of the learning experience using mobile devices (Maniar et al. 2008), of mobile marketing activities (Shankar et al. 2010), of visualization design for mobile devices (Luca 2006), etc. Because of the inherent input restrictions and limited display capabilities, users need to scroll up/down and left/right continuously within a Web page, making it difficult to find target information (Jones et al. 1999, Sweeney and Crestani 2006). These search processes place a heavy cognitive load on users (Albers and Kim 2000). Because of the small screen, users need to remember the content and context of a Web page that they have already viewed, which further increases the cognitive load and the potential for error (Davison and Wickens 1999). Hence, adapting the presentation of Web pages to the unique mobile context is critical to enabling effective mobile Web browsing and information searching (Adipat et al. 2011).

We interpret this literature to suggest that the small screen is likely to increase the burden associated with information gathering (whether directed or not) on the Internet. When put in microeconomic language, this increased burden of information gathering suggests higher search costs. In this way, our paper informs the literature on search costs in the online environment. This literature has emphasized that the reduction in search costs associated with the Internet affected prices, price dispersion, product quality, online demand, market structure, unemployment, and many other areas of economic life (see Lynch and Ariely 2000, Autor 2001, Ellison and Ellison 2009, Kim et al. 2010, etc.).

Price effects have been documented in a variety of industries including books and CDs (Brynjolfsson and Smith 2000), life insurance (Brown and Goolsbee 2002), and automobiles (Scott Morton et al. 2001). Overall, however, the evidence suggests that lower search costs online lead to lower prices and lower price dispersion. If rank-related search costs on the mobile Internet differ from those on the PC-based Internet, and especially if this extends to directed search contexts, price dispersion online may change. Product variety effects have also been documented. Because it is possible for consumers to find even obscure products relatively easily (and because inventory costs are lower), Brynjolfsson et al. (2003) argue that the Internet increases the variety of products available. Similarly, Kuksov (2004) argues that lower search costs increase the incentives to differentiate. Broadly, although the inventory costs do not change whether consumers access the Internet through a PC or a mobile phone, differences in the ease with which consumers can scroll through these product listings on a computer screen might affect the benefit to firms of holding variety.

Overall, our results draw on the literature on ranking effects and the literature on cognitive load in human-computer interaction to suggest that ranking effects are likely to be higher on mobile phones and that this increase in ranking effects can be interpreted as a particular type of increased search cost. We add to this literature by measuring the overall magnitude in a direct comparison of mobile phones and PCs in a real-world setting, by linking it to the existing literature on the economics of the Internet and by comparing it to changes in distance effects.

## 2.2. Why Do Distance Effects Matter?

A long literature documents the role of distance in social and economic behavior. Tobler’s (1970, p. 236) first law of geography is that “all things are related, but near things are more related than far things.” The Internet reduces the cost of communication. Therefore, the popular press has frequently emphasized the ability of the Internet to bring about the “Death of Distance” (Cairncross 1997) or a “Flat World” (Friedman 2005). In the academic literature, this idea has been explored in depth. Balasubramanian (1998) and Zhang (2009) analytically discuss the role of distance to offline stores in substitution between online and offline retail channels. Several empirical studies show that the online channel is more valuable when consumers have to travel further to reach an offline store (Forman et al. 2009, Anderson et al. 2010). Therefore, the online channel helps reduce the importance of distance in many ways, generally increasing the competition faced by any particular firm.

Still, the consequences of lowered communications costs depend on several local factors. Therefore, much online behavior is local. Blum and Goldfarb (2006) show that surfing behavior is disproportionately local and Hampton and Wellman (2002) find that online social interactions are also disproportionately local. Overall, the literature suggests an important role for distance in determining online behavior.

The emergence of location-based services and location-sharing applications suggests that location may play a different role on the mobile Internet. Location-based services are tools that tailor retrieved information based on the location at which a query was made (Brimicombe and Li 2006, Jiang and Yao 2006). The location-based services allow for “where’s my nearest” services. For example, they include searches for local news, weather or sports reports, navigation, friend-finder services, and location-based gaming (Mountain et al. 2009). Researchers studying such services have examined reasons people use FourSquare (Lindqvist et al. 2011), privacy concerns in location-sharing applications (Barkuus and Dey 2003), and the effects of location-based services on the relationships between people (Fusco et al. 2010). Implicit in these studies is the suggestion that the mobile Internet is an important driver of the rise of location-based services.

If the benefit of accessing local information is different when people access the Internet on a mobile phone, even though communication costs fall, it suggests that online behavior more broadly may change. Hence, if surfing behavior becomes more local, then local retailers may disproportionately benefit. For example, people might access the Internet on a mobile phone to sort or filter information by location to make it more relevant to their surroundings (Mountain et al. 2009).

In summary, we combine the insight that locationbased services are driven by the mobile Internet with the perspective that distance matters less online to ask how distance effects compare on the mobile Internet and the PC-based Internet. To the best of our knowledge, no previous study has examined the distance effect in a mobile phone setting. Hence, the overall magnitude of the distance effect on mobile phones as opposed to on PCs is also an important empirical question.

## 2.3. Other Related Literature

Our paper is related to the literatures on usergenerated content in social media platforms and on mobile marketing. By studying microblogs, we examine an increasingly popular form of user-generated content that can potentially have a strong economic and social impact. An emerging stream of relevant work has investigated the economic and social impact of user-generated multimedia content on the mobile Internet by mapping the interdependence between content generation and usage (Ghose and Han 2011) and modeling how consumers learn about different kinds of content (Ghose and Han 2010). A handful of papers has focused on microblogs in particular, including, for example, Java et al. (2007) and Boyd et al. (2010). Dover et al. (2012) use data from Twitter to study transmission activity as a driver of retransmission and diffusion in online social networks.

Our paper builds on and relates to the literature on mobile marketing. We examine ranking effects and distance effects on the mobile Internet. This can have important managerial implications for firms’ mobile marketing strategies. An emerging stream of relevant literature has discussed the role of mobile technologies in marketing. Shankar and Balasubramanian (2009) provide an extensive review of mobile marketing. Shankar et al. (2010) develop a conceptual framework on mobile marketing in the retailing environment and provide discussions on retailers’ mobile marketing practices. For example, retailers can communicate with consumers near their stores via mobile phones by transmitting relevant information such as the store’s location, product availability, quality, price, and coupon in its response to the customer’s mobile phone-initiated requests. Moreover, specific consumer segments such as the Gen Y youth market increasingly use mobile phones as single-source communication devices (Sultan et al. 2009) to gain greater access to social circles, location-based information, and content. Sinisalo (2011) examines the role of the mobile medium among other channels within multichannel customer relationship management (CRM) communication. Ghose and Han (2012) estimate demand for mobile apps on both Apple and Android platforms and discuss implications for mobile advertising.

## 3. Data Description

In this section, we provide details on our empirical setting and describe the data.

## 3.1. Empirical Setting

Our data come from a microblogging service company in South Korea. The company was founded in November 2008. As of November 2009, there were about 40,000 registered members. Members can post a message about what they are doing or what they are thinking, and they can read posts created by other members. There are PC and mobile phone application (iPhone and Android) versions of the service. However, the service features offered are the same regardless of whether a user accesses the service through a PC or a mobile phone.

Users are primarily browsing on the website. When users log into the service, they see a list of posting feeds that looks much like the news feed of a Facebook account or the results of a search engine query. The initial views of the posts are limited to 140 characters. The brand posts in our empirical setting are generated by users and have time stamp information. For example, a post might say “I had a great meal at Gotham Bar and Grill! (10 <sup>p.m.</sup> May 1 2011).” Although one can check these postings at one’s leisure time using a PC, the primary reason why people use microblogging services through a mobile phone is to receive and to deliver extremely brief bursts of current information or/and news, an activity that is well suited to mobile devices (Java et al. 2007). Some of these posts clearly publicize temporary price promotions and location-specific deals.

Importantly, 92% of postings in our sample exceed the 140 character limit, and therefore users are often motivated to click on the post in order to read the full content. In addition, when they click on a brand post, they can also view content from related posts. Unlike Facebook and other popular social networking services, the microblogging service in our empirical setting does not support any clipping or bookmarking function. Even if a user wants to see the full content of the same link again, then the user needs to click the link on the posting again. (In our empirical analysis, we do not include such multiple clicking activities from the same user for a given posting.)

From a purely rational model of behavior, it is puzzling why users might post at all. Given our focus, we do not attempt to answer this question. Instead, we rely on prior literature to suggest reasons for posting. Specifically, Xia et al. (2012) suggest that reciprocity stemming from social exchange theory (Homans 1958) plays a critical role in online content sharing. They document that the more a user benefits from the contributions of other users, the more that user is willing to create and share content. We believe such nonmonetary incentives, including altruism and reputation, are important drivers of information sharing in our empirical context. Furthermore, many of the posts in our microblogging service include mentions of a particular brand and sometimes include some location-specific and time-specific deals, coupons, and promotions. In such cases, with altruistic or reputation-building motivations, many users may choose to pass such information to their followers.

To summarize, we study a microblogging service where users browse 140 character snippets of longer messages posted by others. The snippets often contain brand information. Users click on these snippets to read the full messages.

## 3.2. Data Description

Our sample is randomly drawn from brand-related posts created by members of the microblogging service between November 29, 2009, and March 6, 2010. We have data on users’ click behavior at the microblogging site using both their PCs and their mobile phones. To be specific, the data set consists of 440 brand-related posts created by 88 distinct users and whether each post is viewed and clicked by 260 other users (i.e., followers). The unit of analysis is the post-user, and the data set contains 8,896 such observations. Our data set contains all brand-related posts viewed by these users (defined as a post that mentions a brand). Brands range from prominent international brands like Starbucks and McDonalds to the relatively unknown. Table 1 shows summary statistics of the key variables in the sample.

Table 1 Summary Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td colspan="5">Brand level</td></tr><tr><td>Brand profile tenure (days)</td><td>274</td><td>159</td><td>1</td><td>501</td></tr><tr><td>Post tenure (days)</td><td>8.380</td><td>14.269</td><td>0</td><td>97.1</td></tr><tr><td colspan="5">User level</td></tr><tr><td>Age</td><td>24.987</td><td>11.818</td><td>11</td><td>54</td></tr><tr><td>Gender (Male = 1, Female = 0)</td><td>0.769</td><td>0.422</td><td>0</td><td>1</td></tr><tr><td>Number of followees(those one follows)</td><td>10.414</td><td>30.609</td><td>0</td><td>373.6</td></tr><tr><td>Number of subscriptions</td><td>15.711</td><td>56.946</td><td>0</td><td>350</td></tr><tr><td colspan="5">User and brand post level</td></tr><tr><td>Mobile phone access rate</td><td>0.130</td><td>0.335</td><td>0</td><td>1</td></tr><tr><td colspan="5">Mobile phones</td></tr><tr><td>Rank of brand post</td><td>8.511</td><td>5.908</td><td>1</td><td>21</td></tr><tr><td>Distance between a user and a brand store (miles)</td><td>21.623</td><td>83.786</td><td>0.062</td><td>715.6</td></tr><tr><td>Click-through on brand posts</td><td>0.068</td><td>0.252</td><td>0</td><td>1</td></tr><tr><td colspan="5">PCs</td></tr><tr><td>Rank of brand post</td><td>35.789</td><td>25.825</td><td>1</td><td>90</td></tr><tr><td>Distance between a user and a brand store (miles)</td><td>33.084</td><td>98.675</td><td>0.058</td><td>730.9</td></tr><tr><td>Click-through on brand posts</td><td>0.033</td><td>0.179</td><td>0</td><td>1</td></tr></table>

There are two sources of brand-related feeds in our setting: (1) brand-related updates from other members that one is following (i.e., followees) and (2) updates posted at a brand site to which one has subscribed. Brand-specific variables include brand category (refer to Figure 1 for the complete list), brand profile tenure (days since brand first appeared on the website), post tenure (days since post first appeared on the website), and number of subscriptions. Userspecific variables include age, gender, number of followees, and type of access channel. Our data set has only two types of user access technologies—PCs and mobile phones. It does not include tablets. Therefore our definition of the mobile Internet is Internet access through mobile phones only. Importantly, users that access the website by both channels might be fundamentally different from the users that use only mobile phones or only PCs. So we focus our analysis on the 1,940 total brand post views by those users who accessed the website at least once with each channel to ensure the results are driven by unobserved heterogeneity across users in the sample.

The brand- and user-specific variables include the rank of a brand post on a user’s login page, the distance between the user and the brand store, and whether a user clicked that brand post or not. Summary statistics of these variables are given for each channel separately in Table 1. For example, the clickthrough rates are 6.8% in mobile phones and 3.3% in PCs. Moreover, the ranking of clicks are different across platforms. Figure 2 illustrates that users are more likely to click on better ranked posts when they access the site through mobile phones as opposed to PCs. Crucially, the rank of the same post varies across users and we exploit this variation for identification (see §4.1 for details).

Figure 1 Brand Categories  
![](/api/attachments/GS9ZADZ5/fulltext/images/110f7a7c8575c014cf9e53e69b937614ba331e6d367b9a0edf0bd1ed1ffa18d0.jpg)  
All brands

![](/api/attachments/GS9ZADZ5/fulltext/images/da81fac15b9b57f898dfdb101352069ba3664589bb748cc3c5f669dde23b273a.jpg)  
Clicked brands only

Regarding the distance variable, we compute the geographic distance between a user’s home address and the retail location of the brand mentioned in the post. Because many brands do not have a physical store (including several common categories such as books, computer games, and multimedia clips), we only have distance information for brands in 48% of the observations in our main sample. To ensure the lack of distance information for some observations does not drive our distance coefficients, we use brand post-level fixed effects. These controls capture situations when distance is missing (i.e., posts that mention brands with no physical store).

Figure 2 Ranking of Clicks Across Platforms  
![](/api/attachments/GS9ZADZ5/fulltext/images/2e0b6e9bbf8283a25172173e009223cdb5c34816052795d3af641265abfb6912.jpg)

## 4. Econometric Analysis

To formally characterize our econometric model, we model user click-through decisions in terms of brand attributes, user characteristics, and brand-and-user characteristics. A user can navigate all posting feeds when he logs on the microblog platform using a PC or a mobile phone. In our model, a user decides to click a post that provides the maximum expected utility to explore the content of the post. To better control for heterogeneity, we characterize our model in a hierarchical Bayesian framework and estimate it using Markov Chain Monte Carlo methods. The rest of this section is organized as follows: a brief sketch of our research design using a natural experiment, the econometric model, the estimation method, and a discussion of the identification strategy.

## 4.1. Research Design: Exogenous Variation in Ranking

We treat the posting of a new brand-related message by users as an “event” in a natural experiment-like setting. Upon a posting event, after logging in, all followers of the post creator and subscribers of the brand can view the post and click on it to read the full content of the post.<sup>2</sup> Users view the same brand post message regardless of platforms. In each posting event, we examine the impact of a post rank, distance between a user and the offline location of the posting brand’s store, and other factors upon clicking decisions. Thus, we control for any post-specific unobserved quality issues when it comes to mapping their click-through rates. The rationale for this control is that some postings attract more user clicks than others for their unobserved inherent characteristics (i.e., length, sentiment, theme, relevance).

In addition, the microblogging service in our setting provides an ideal setting for identifying the impact of post rank because it provides a unique source of variation in the ranking mechanism. When a user generates a post, the same post would appear at different positions (ranks) for different users. However, unlike in sponsored search engines, the rank order in our empirical context is determined independently of any prior click-through decisions by users and of brand advertisements by advertisers.<sup>3</sup> Instead, given that users play a dual role as both consumers (i.e., read posts created by other members) and suppliers (i.e., generate new posts) in the microblogging context, the rank order is solely determined by user traits (e.g., login frequency and posting frequency). For example, the more frequently a user logs in, the less quickly the rank of a given post increases, and the more frequently a user’s followee creates posts, the more quickly the rank of a given post increases. We control for these factors directly with covariates and therefore ascribe all remaining variation in rank to factors that are exogenous to the propensity to click. In this way, it is something like a natural experiment. As described below, to the extent that our controls do not address all user-level heterogeneity in these dimensions, we further control for user-level differences with random coefficients in a hierarchical Bayes framework.

We use only the first appearance of a brand post on a user’s screen in our analysis to avoid the following potential confound. Suppose a user is unlikely to click on the same post across successive login sessions. By construction, any given brand post can reappear to the same user at worse ranks across login sessions (i.e., an older post will be located toward to the bottom of the screen). Also by construction, the likelihood that a user has already clicked on a link increases across login sessions. Hence, even without a preference for rank, better ranked items would be clicked more often. Furthermore, if there is just a short period between a current login and a previous login, it is more likely that lower ranked posts have already been seen, which makes it more likely that a user clicks on a top ranked post. If a user logs in more often on a mobile phone than on a PC, this could bias the results.

We also excluded brand posts that were displayed to only one user, in order to identify effects through comparing across users. Moreover, we emphasize results that include only those users who have accessed the microblogging platform via both mobile phones and PCs (i.e., dual channel users). This helps us to identify the “within-user” moderating effect of access channels on user click decisions. However, our results are robust to the use of the entire sample of users in our data.

## 4.2. Econometric Model

Our model consists of two distinct levels: (1) a postlevel latent utility model and (2) a population-level model with user and brand post-level heterogeneity. Notation and variable descriptions are provided in Table 2.

Table 2 Notations and Variable Descriptions

<table><tr><td> $u_{ijk}$ </td><td>Latent utility of clicking and visiting a brand post  $k$  by user  $i$  at time  $j$ </td></tr><tr><td> $Rank_{ijk}$ </td><td>Rank of brand post  $k$  on user  $i$ &#x27;s login screen at time  $j$ </td></tr><tr><td> $Distance_{ik}$ </td><td>Euclidian log distance between user  $i$ &#x27;s place and brand post  $k$ &#x27;s physical store</td></tr><tr><td> $Mobile_{ij}$ </td><td>Access channel of user  $i$  at time  $j$  (1 = mobile, 0 = PC)</td></tr><tr><td> $Followee_{ij}$ </td><td>Number of users user  $i$  is following at time  $j$ </td></tr><tr><td> $Subscription_{ij}$ </td><td>Number of brands user  $i$  is following at time  $j$ </td></tr><tr><td> $Age_i$ </td><td>Age of user  $i$ </td></tr><tr><td> $Gender_i$ </td><td>Gender of user  $i$  (1 = male, 0 = female)</td></tr><tr><td> $BrandTenure_{jk}$ </td><td>Days elapsed since the brand profile of post  $k$  was created until day  $j$ </td></tr><tr><td> $PostTenure_{jk}$ </td><td>Days elapsed since brand post  $k$  was created/posted until day  $j$ </td></tr><tr><td> $NongeographicBrand_k$ </td><td>Missing distance indicator for post  $k$  (1 = missing, 0 = nonmissing)</td></tr></table>

4.2.1. Post-Level Model. The observed user’s binary response $( \mathrm { i . e . , }$ whether to click or not) can be modeled using a random-utility framework. We posit that users click on a posting feed when the utility for reading the full content of the post exceeds a certain threshold. For a given brand post $k ,$ at time $j ,$ the relationship between the observed response $y _ { i j k }$ and the latent utility $u _ { i j k }$ of clicking for user i can be written as

$$
\begin{array}{c l} y _ {i j k} = 0 & \text {if} u _ {i j k} \leq 0 \\ 1 & \text {if} u _ {i j k}. \end{array}\tag{1}
$$

We model the latent utility $u _ { i j k }$ from clicking on a post k at time j for user i as the function of observed and unobserved post and user characteristics in the following way. This is not a fully specified structural model of user behavior. Instead, it should be seen as a reduced form of a broader latent utility model that allows us to estimate the effects of interest. Specifically, we are primarily interested in the effect of rank and distance on a user’s propensity to click on a brand posting that appears on his screen. Rank allows us to measure ranking effects. It is more valuable to be ranked near the top, and hence such high ranked postings are likely to get higher click-throughs. Distance allows us to examine the role of geography and local activities of users. Higher click-through rates on postings involving brands located closer to the user imply that consumers have a preference for geographically local activities. Because the address information of brand stores is often provided to users, we assume that users are fully informed about the locations of brand stores that appear in the posts. Our main findings emphasize how these effects vary between a mobile phone and a PC.

We also control for user-level observed heterogeneity by including access channel (mobile phone or PC), number of followees, number of subscriptions, age, and gender of each user. For example, the motivation for browsing and clicking may differ between mobile phones and PCs. We capture such variation in propensity to click by including an indicator of whether a user accessed the service through a mobile phone as opposed to through a PC. Also, because the duration of time since the establishment of a brand profile increases, the likelihood of a click on that brand may change. We capture such brand-level observed heterogeneity by including brand tenure. We add a control for the recency of the information capturing time elapsed since posting $( \mathrm { i . e . , }$ post tenure). The rationale for including this control is that users might place higher valuation on higher ranked posts because the posts are ordered and presented by time. Hence, if users have higher valuation for timely posts, they will be more likely to click on higher ranked posts. Furthermore, to control for the different value of timely posts across channels, we also include an interaction between post tenure and access channel. Lastly, we control for the nongeographic brand posts that are missing distance information (beyond the post fixed effect) with an interaction between a dummy for nongeographic brands and mobile phone access.

Thus, for a given brand post ${ \bar { k } } ,$ we specify that user i’s latent utility at time j is a function of rank, distance, and other factors as follows for $k = 1 , 2 , \ldots , s \colon$

$$
\begin{array}{l} u _ {i j k} = \beta_ {i k} + \beta_ {i j 1} \text {Rank} _ {i j k} + \beta_ {i j 2} \text {Distance} _ {i k} \\ \quad + \beta_ {i j 3} \text {Rank} _ {i j k} \text {Distance} _ {i k} + \alpha_ {1} \text {Mobile} _ {i j} + \alpha_ {2} \text {Followee} _ {i j} \\ \quad + \alpha_ {3} \text {Subscription} _ {i j} + \alpha_ {4} \text {Age} _ {i} + \alpha_ {5} \text {Gender} _ {i} \\ \quad + \alpha_ {6} \text {BrandTenure} _ {j k} + \alpha_ {7} \text {PostTenure} _ {j k} \\ \quad + \alpha_ {8} \text {PostTenure} _ {j k} \text {Mobile} _ {i j} \\ \quad + \alpha_ {9} \text {NongeographicBrand} _ {k} \text {Mobile} _ {i j} + e _ {i j k}, \end{array} \tag {2}
$$

$$
u _ {i j s + 1} = e _ {i j s + 1}.\tag{3}
$$

We assume the error term $e _ { i j k }$ is i.i.d from a type I extreme value distribution. The utility from not clicking on the brand post k is denoted as $e _ { i j s + 1 } .$ As mentioned above, our choice model is binary rather than multinomial. This means we do not include information about the other posts that appear at the same time as the focal branded post of interest. Therefore, implicit in our i.i.d. error assumption is an assumption that the other (unmodeled) posts that appear along with the focal post are randomly drawn across observations.

4.2.2. Population-Level Model. Hierarchical Bayesian methods allow for better control for unobserved heterogeneity. In the population model, the hierarchical Bayesian framework provides individualspecific estimates of the ranking and distance effects, unobserved heterogeneity covariance estimates, and other model parameters. Specifically, user heterogeneity is further captured by the population-level model by specifying user-specific random coefficients $( \mathrm { i . e . , } \beta _ { i j 1 } \mathrm { \stackrel { . } { - } } \bar { \beta } _ { i j 3 } )$ , which capture differences across users in their responses to post rank, user-brand store distance, and their interaction. To be specific, we allow the impact of the key independent variables in Equation (2) (e.g., Rank, Distance, and RankDistance) to interact with user-specific characteristics such as access channel (mobile phone or PC), number of followees, number of subscriptions, age, and gender. For example, we allow $\beta _ { i j 1 }$ to vary by whether a user accesses the Internet through a mobile phone or a PC, in order to assess the extent to which the mobile Internet moderates the effect of rank on user click-through decisions. We also allow the coefficients of Rank, Distance, and RankDistance in Equation (2) to vary along the respective population mean (i.e., $\bar { \beta } _ { 1 } - \bar { \beta } _ { 3 } )$ . We model unobserved heterogeneity across users by including $\lambda _ { i 1 } , \lambda _ { i 2 } ,$ and $\lambda _ { i 3 }$ in each random coefficient as follows:

$$
\begin{array}{c} \beta_ {i j 1} = \bar {\beta} _ {1} + \alpha_ {1 0} M o b i l e _ {i j} + \alpha_ {1 1} F o l l o w e e _ {i j} \\ \qquad + \alpha_ {1 2} S u b s c r i p t i o n _ {i j} + \alpha_ {1 3} A g e _ {i} \\ \qquad + \alpha_ {1 4} G e n d e r _ {i} + \lambda_ {i 1}, \end{array}\tag{4}
$$

$$
\begin{array}{c} \beta_ {i j 2} = \bar {\beta} _ {2} + \alpha_ {1 5} M o b i l e _ {i j} + \alpha_ {1 6} F o l l o w e e _ {i j} \\ \qquad + \alpha_ {1 7} S u b s c r i p t i o n _ {i j} + \alpha_ {1 8} A g e _ {i} \\ \qquad + \alpha_ {1 9} G e n d e r _ {i} + \lambda_ {i 2}, \end{array}\tag{5}
$$

$$
\begin{array}{r} \beta_ {i j 3} = \bar {\beta} _ {3} + \alpha_ {2 0} M o b i l e _ {i j} + \alpha_ {2 1} F o l l o w e e _ {i j} \\ + \alpha_ {2 2} S u b s c r i p t i o n _ {i j} + \alpha_ {2 3} A g e _ {i} \\ + \alpha_ {2 4} G e n d e r _ {i} + \lambda_ {i 3}. \end{array}\tag{6}
$$

In addition, each post may have inherent postspecific unobserved quality. Hence, the likelihood of clicking on a post will be associated with the brand post. In Equation (7), we capture the post-level attractiveness with a fixed effect, denoted by $\bar { \beta } _ { 0 k } ,$ , and allow unobserved heterogeneity across users with a random coefficient on the intercept, denoted by $\lambda _ { i 0 }$ as follows:

$$
\beta_ {i k} = \bar {\beta} _ {0 k} + \lambda_ {i 0}.\tag{7}
$$

We model the unobserved covariation among $\lambda _ { i 0 } ,$ $\lambda _ { i 1 } , \lambda _ { i 2 } ,$ and $\lambda _ { i 3 }$ by letting the four error terms be correlated in the following manner:

$$
\left[ \begin{array}{c} \lambda_ {i 0} \\ \lambda_ {i 1} \\ \lambda_ {i 2} \\ \lambda_ {i 3} \end{array} \right] \sim \text {MVN} \left(\left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c c} \Sigma_ {0, 0} ^ {\lambda} & \Sigma_ {0, 1} ^ {\lambda} & \Sigma_ {0, 2} ^ {\lambda} & \Sigma_ {0, 3} ^ {\lambda} \\ \Sigma_ {1, 0} ^ {\lambda} & \Sigma_ {1, 1} ^ {\lambda} & \Sigma_ {1, 2} ^ {\lambda} & \Sigma_ {1, 3} ^ {\lambda} \\ \Sigma_ {2, 0} ^ {\lambda} & \Sigma_ {2, 1} ^ {\lambda} & \Sigma_ {2, 2} ^ {\lambda} & \Sigma_ {2, 3} ^ {\lambda} \\ \Sigma_ {3, 0} ^ {\lambda} & \Sigma_ {3, 1} ^ {\lambda} & \Sigma_ {3, 2} ^ {\lambda} & \Sigma_ {3, 3} ^ {\lambda} \end{array} \right]\right).\tag{8}
$$

4.2.3. Full Model. By replacing $\beta _ { i j 1 } , \beta _ { i j 2 } , \beta _ { i j 3 } ,$ and $\beta _ { i k }$ in Equation (2) with Equations $( 4 ) - ( 7 )$ , we can rewrite Equation (2) for brand post k as follows:

$$
\begin{array}{l} u _ {i j k} = \bar {\beta} _ {0 k} + \alpha_ {1} \text {Mobile} _ {i j} + \alpha_ {2} \text {Followee} _ {i j} + \alpha_ {3} \text {Subscription} _ {i j} \\ \quad + \alpha_ {4} \text {Age} _ {i} + \alpha_ {5} \text {Gender} _ {i} + \alpha_ {6} \text {BrandTenure} _ {j k} \\ \quad + \alpha_ {7} \text {PostTenure} _ {j k} + \alpha_ {8} \text {PostTenure} _ {j k} \text {Mobile} _ {i j} \\ \quad + \alpha_ {9} \text {NongeographicBrand} _ {k} \text {Mobile} _ {i j} \\ \quad + (\bar {\beta} _ {1} + \alpha_ {1 0} \text {Mobile} _ {i j} + \alpha_ {1 1} \text {Followee} _ {i j} \\ \quad + \alpha_ {1 2} \text {Subscription} _ {i j} + \alpha_ {1 3} \text {Age} _ {i} \\ \quad + \alpha_ {1 4} \text {Gender} _ {i}) \text {Rank} _ {i j k} \\ \quad + (\bar {\beta} _ {2} + \alpha_ {1 5} \text {Mobile} _ {i j} + \alpha_ {1 6} \text {Followee} _ {i j} \\ \quad + \alpha_ {1 7} \text {Subscription} _ {i j} + \alpha_ {1 8} \text {Age} _ {i} \\ \quad + \alpha_ {1 9} \text {Gender} _ {i}) \text {Distance} _ {i k} \\ \quad + (\bar {\beta} _ {3} + \alpha_ {2 0} \text {Mobile} _ {i j} + \alpha_ {2 1} \text {Followee} _ {i j} \\ \quad + \alpha_ {2 2} \text {Subscription} _ {i j} + \alpha_ {2 3} \text {Age} _ {i} \\ \quad + \alpha_ {2 4} \text {Gender} _ {i}) \text {Rank} _ {i j k} \text {Distance} _ {i k} \\ \quad + \lambda_ {i 0} + \lambda_ {i 1} \text {Rank} _ {i j k} + \lambda_ {i 2} \text {Distance} _ {i k} \\ \quad + \lambda_ {i 3} \text {Rank} _ {i j k} \text {Distance} _ {i k} + e _ {i j k}. \end{array}
$$

Equation (9) contains both main effects of Rank, Distance, and RankDistance (i.e., $\bar { \beta } _ { 1 } - \bar { \beta } _ { 3 } )$ and moderating effects with individual-specific characteristics such as access channel, number of followees, number of subscriptions, and demographics $( \mathrm { i . e . , } \alpha _ { 1 0 } , \dots , \alpha _ { 2 4 } )$ It also has control variables for brand post-specific intercept, mobile, followee, subscription, age, gender, brand tenure, post tenure, an interaction between post tenure and mobile, and an interaction between a dummy for nongeographic brands and mobile (i.e., $\bar { \beta } _ { 0 k } , \alpha _ { 1 } , \ldots , \alpha _ { 9 } )$

## 4.3. Estimation

4.3.1. Choice Probability. We rewrite user i’s latent utility above as being composed of a systematic part $( \mathrm { i } . \mathrm { e } . , \ v _ { i j k } )$ and a stochastic part $( \mathrm { i } . \mathrm { e } . , \ e _ { i j k } )$ as follows:

$$
u _ {i j k} = v _ {i j k} + e _ {i j k}.\tag{10}
$$

Recall that we assume that $e _ { i j k }$ is i.i.d from type I extreme value distribution. Hence, the probability of user i clicking on brand post k at time j is

$$
\operatorname * {P r} (y _ {i j k} = 1 \mid \underline {{\beta}} _ {i}) = \frac {\exp (v _ {i j k})}{1 + \exp (v _ {i j k})},\tag{11}
$$

where $\underline { { \beta } } _ { i }$ denotes all parameters in the model.

4.3.2. Hierarchical Bayesian Modeling and Estimation. We cast our model in a hierarchical Bayesian framework and estimate it using Markov Chain Monte Carlo (MCMC) methods. We rewrite our main equations as follows:

$$
\underline {{u}} _ {i j} = X _ {i j} ^ {\prime} \underline {{\beta}} _ {i} + \underline {{e}} _ {i j},\tag{12}
$$

$$
\underline {{\beta}} _ {i} = \underline {{Z}} _ {i} ^ {\prime} \underline {{\mu}} + \underline {{\lambda}} _ {i},\tag{13}
$$

where $\mathrm { P r } ( \mu ) = N ( \eta , C ) , \mathrm { ~ } \underline { { { \lambda } } } _ { i } = ( \lambda _ { i 0 } , \dots , \lambda _ { i 3 } ) ^ { \prime } { \sim } N ( 0 , \Lambda ) .$ and Pr $( \Lambda ^ { - 1 } ) = W ( \overline { { { \rho , } } } R ) .$

The corresponding mixed model is as follows.

$$
\underline {{u}} _ {i j} = W _ {i j} ^ {\prime} \underline {{\mu}} + X _ {i j} ^ {\prime} \underline {{\lambda}} _ {i} + \underline {{e}} _ {i j}.\tag{14}
$$

Hence, the full conditionals are (A) $\operatorname* { P r } ( \lambda _ { i } \mid \mu , \Lambda , y _ { i } ) ,$ (B) $\operatorname* { P r } ( \mu \mid \Lambda , \{ \underline { { \lambda } } _ { i } \} _ { i = 1 } ^ { n } , \{ y _ { i } \} _ { i = 1 } ^ { n } )$ , and (C) $\operatorname* { P r } ( \Lambda ^ { - 1 } \overline { { | } } \{ \underline { { \lambda } } _ { i } \} _ { i = 1 } ^ { n } )$ where n is the total number of users in the sample.

In order to gain efficiency in estimation, we use an adaptive Metropolis-Hastings algorithm with a random walk chain (Atchadè 2006, Chib and Greenberg 1995, Hastings 1970) to generate draws of $\underline { { \lambda } } _ { i }$ and $\underline { { \mu } }$ in conditional (A) and (B). Hence we can adjust the tuning constant to vary across individuals (see the appendix for a more detailed description of the MCMC algorithm).<sup>4</sup>

## 4.4. Identification

We briefly discuss both mathematical and empirical identification in our model.

4.4.1. Mathematical Identification. First, we impose a location normalization restriction by setting the constant utility term for any one brand post to be 0. We do this because one can change all the brand post-specific constant terms by adding or subtracting a constant c without changing the choices implied by the model. As a reference brand post, we set the mean value for a brand post in the “local restaurant” category to be 0. The qualitative nature of our results do not change based on the choice of a reference brand post. Second, we impose a scale normalization restriction by allowing the distribution for the error term, $e _ { i j k } , $ to be the type I extreme value distribution. We do this because one can scale all the parameters in Equation (2) by $c ,$ while scaling the error term by $c ,$ without changing the choices implied by the model.

4.4.2. Empirical Identification. The identification of the impact of rank depends on a unique source of variation in the ranking mechanism. Unlike in the search engine context where the rank is determined by algorithms based on popularity and relevance, the rank in our microblog setting is determined by “recency.” Thus, the posts appear on a user’s login screen in reverse chronological order (i.e., the most recent one appears at the top). Because we control directly for recency and individual heterogeneity, this setting reduces concerns for endogeneity issues in rank because previous clicks by users on a post do not affect the rank of that post in any subsequent periods.

Our empirical identification relies on the assumption that, conditional on our specification, the rank order of a post is random and exogenous. We believe this assumption is reasonable because (1) the frequency that a content creator generates a brand post and the system automatically sends the brand post to a user is independent of that user’s login frequency, (2) the user is able to see the rank of a post only after he or she logs in, and (3) we include post fixed effects and therefore identify off variation across users in the rank of the same post. Hence a user’s login decision can be considered as a random stopping decision during the process of continual posting feeds from his followees or subscriptions. Said simply, we can consider users’ login timing decisions as exogenous to the determination of the rank of a post. We can do this if we assume that our controls for recency, user characteristics, and user heterogeneous response (i.e., the random coefficients) adequately control for the differences in rank. The required assumptions for the main results of the paper are somewhat weaker. In particular, given that the main results of the paper rely on the interaction between access device and rank, we need to assume that the controls for recency, user characteristics, device-specific habits, and user heterogeneous response adequately control for all nonrandom differences in rank across devices.

## 5. Results

We ran the MCMC chain for 60,000 iterations and used the last 20,000 iterations to compute the mean and standard deviation of the posterior distribution of the model parameters.<sup>5</sup> Convergence was assessed by monitoring the time series of the draws and by assessing the Gelman-Rubin (Gelman and Rubin 1992) statistics. In all cases, the Gelman-Rubin statistic was less than 1.2, suggesting that convergence was acceptable. We next present our key results on ranking effects and distance effects across the two kinds of access technologies (mobile versus PC). We discuss the economic impact of our results and show robustness to a variety of alternative specifications and samples.

## 5.1. Main Results

5.1.1. Estimation Results. We present the results on the coefficients of the main model in Table 3. The first column shows the effect of rank, distance, and their interaction on clicks when users access the microblogging site with a PC. Consistent with prior evidence on the primacy effect, the first column shows that better rank increases clicks (rank is significantly negative). Furthermore, people click on nearby links (distance is significantly negative). This is consistent with a distance decay effect (Fellmann et al. 2000), in which interaction between two entities declines as the distance between them increases. These effects reinforce each other in combination because the interaction of rank and distance is significantly negative.

Table 3 Effect of Rank and Distance on Clicks 4Dual Channel Users; N = 11940

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="9">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brand × Mobile</td></tr><tr><td colspan="11">Coefficient estimates</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.150***(0.004)</td><td>0.002**(0.001)</td><td>0.044***(0.002)</td><td>-0.046***(0.001)</td><td>-0.126***(0.001)</td><td>-0.002**(0.001)</td><td>-0.070***(0.003)</td><td>-0.011***(0.001)</td><td>-0.074(0.642)</td></tr><tr><td>Rank</td><td>-0.225***(0.003)</td><td>-0.089***(0.004)</td><td>0.0003(0.0002)</td><td>-0.004(0.003)</td><td>-0.001(0.001)</td><td>-0.012***(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.110***(0.005)</td><td>-0.098***(0.003)</td><td>-0.001*(0.0006)</td><td>-0.012***(0.002)</td><td>0.011***(0.003)</td><td>0.003(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.065***(0.003)</td><td>-0.010***(0.003)</td><td>0.0002(0.0002)</td><td>-0.001(0.002)</td><td>-0.002**(0.001)</td><td>-0.008***(0.003)</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="2">Intercept</td><td colspan="3">Rank</td><td colspan="3">Distance</td><td>Rank × Distance</td></tr><tr><td colspan="11">Unobserved heterogeneity covariance estimates</td></tr><tr><td>Intercept</td><td></td><td colspan="2">0.030***(0.006)</td><td colspan="3">-0.004(0.008)</td><td colspan="3">-0.009**(0.004)</td><td>-0.008(0.007)</td></tr><tr><td>Rank</td><td></td><td colspan="2"></td><td colspan="3">0.135**(0.050)</td><td colspan="3">-0.015**(0.007)</td><td>0.002(0.033)</td></tr><tr><td>Distance</td><td></td><td colspan="2"></td><td colspan="3"></td><td colspan="3">0.037***(0.007)</td><td>-0.002(0.009)</td></tr><tr><td>Rank × Distance</td><td></td><td colspan="2"></td><td colspan="3"></td><td colspan="3"></td><td>0.120**(0.055)</td></tr></table>

<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.  
Notes. Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects are omitted for brevity

Our primary focus is on the difference between PCs and mobile phones. The second column of Table 3 shows that the estimate for the interaction between the rank and the mobile phone access channel is negative and statistically significant (the coefficient is −00089), implying that the ranking effect is strengthened in a mobile setting. In other words, users are more likely to click on a highly ranked post in a mobile setting, as opposed to in a PC setting in which they see more messages on a given screen shot. As mentioned in Shankar et al. (2010), “real estate” is particularly important in a mobile setting.

We also find that distance matters more in the mobile setting than in the PC setting, even though our measure of the user’s location reflects a physical address. Therefore, this result should not be interpreted as direct evidence of a contextual effect. Instead, it suggests that people tend to prefer local brands that are near their homes on their mobile phones, perhaps because it is easier for them to travel there but perhaps for reasons unrelated to context. The interaction between distance and rank is also stronger in the mobile channel.

Some of the control variables yield interesting insights. Specifically, the estimate for mobile phone access is positive and statistically significant (the coefficient is 0.150). Given that the coefficient of the interaction between Mobile and Rank is −00089, this result suggests that when the rank is 1, a user accessing through mobile phones is more likely to click on brand posts. This also suggests consumers place higher valuation on top ranked posts in the mobile setting, perhaps because they are on the move and/or the screen size is smaller when using mobile phones.

The coefficient on the control for the recency of information, post tenure, can be interpreted as an alternative type of search cost. In particular, because of the ubiquitous access, the cost of acquiring timely information should be lower on a mobile phone than on a PC. The premise of this interpretation is that if the sign of the interaction between the post tenure and the mobile phone access channel is negative, then it suggests that the high search cost interpretation of the screen-related ranking effects in a mobile phone is mitigated for timely information (i.e., more recent posts). Our results confirm this notion (the coefficient of the interaction term is −00011 and p-value < 0001).

5.1.2. Economic Importance of the Effects. We discuss the economic impact of each effect using odds ratios. For PC users, moving one position upward in rank for a brand post yields an increase in the odds of clicking on that post by 25% $( \exp ( 0 . 2 2 5 ) = 1 . 2 5 )$ holding the other variables constant. This is similar to the drop in click-through rates with position found in a shopbot setting by Baye et al. (2009) and the drop in click-through rates with position found in a search engine setting by Ghose and Yang (2009) and Yang and Ghose (2010). For mobile phone users, one position upward increase in rank of a brand post yields an increase in odds of clicking on that post by 37% $( \exp ( 0 . 2 2 5 + 0 . 0 8 9 ) = 1 . 3 7 )$ . So the ratio of the odds (mobile phone versus PCs) is 1.10. Hence, the value increases 10% through mobile phones as compared to PCs for each unit decrease in rank.

The main mobile effect (i.e., the positive propensity to click through mobile phones) alleviates the stronger ranking effect in a mobile setting. The odds of clicking increase 16% for mobile users as compared to PC users. The magnitude of the ranking effects varies by the size of ranks changed, whereas the main mobile effect is fixed. Hence, we examined the overall ranking effects as we gradually increase the rank from 1 to 10. Except when the rank is 1, we find that the overall ranking effects are always dominated by the stronger ranking effects in a mobile setting. For example, the odds ratios of clicking (mobile phones versus PCs) are 1.06, 0.74, and 0.48 when we increase the rank to 1, 5, and 10, respectively. This supports our interpretation that the difference in the ranking effects is the result of a higher cognitive load in a mobile phone setting as compared to a PC setting.

Regarding distance effects, for PC users, a one-mile decrease in distance between a user and a brand store yields an increase in the odds of clicking on that post by 12%. This result is consistent with evidence that people generally have local interests (Hampton and Wellman 2002). For mobile users, moving one mile closer in distance between a user and a brand store yields an increase in the odds of clicking on that post by 23%. So the odds ratio is 1.10. Hence, the odds ratio increases 10% through mobile phones as compared to PCs for each unit decrease in distance. Similarly, we checked the overall distance effects as we increase the distance from 1 to 10.<sup>6</sup> The result also warrants our interpretation that the difference in the distance effects is higher in a mobile phone setting as compared to in a PC setting.

Regarding post tenure, for PC users, an increase in the recency of a post by one day yields an increase in the odds of clicking on that post by 7.1% holding the other variables constant. For mobile phone users, an increase in the recency of a post by one day yields an increase in odds of clicking on that post by 8.3%. Hence, the estimated magnitude of the post time sensitivity effect on the odds of clicking in mobile phone settings is larger than that in PC settings. Lastly, the statistically significant results on unobserved heterogeneity variance-covariance estimates in Table 3 suggest that controlling for unobserved heterogeneity is important in our setting.

## 5.2. Robustness Checks

Tables 4–10 show that the results are robust to a number of alternative specifications. In particular, Table 4 model (1) shows that the results on rank hold without controls for distance. Similarly, model (2) shows that the results on distance hold without the controls for rank. Model (3) shows that excluding the interaction between rank and distance does not affect the qualitative results on rank or distance. Models (4) and (5) show robustness to fewer interaction terms as controls.

Table 5 shows that the results are robust to alternative samples. In particular, sample (1) includes all users, not just the dual channel users. Sample (2) includes only posts from subscribed brands. Because users explicitly opted in to receive these subscribed brand posts, it reduces the likelihood that users will make false quality inferences based on rank.

Potentially, the identified ranking effect across platforms is simply the difference in the number of posts viewable on a single page across platforms. Typically, a PC lists about 30 posts per page and a mobile phone lists about 10 posts per page in this microblogging setting. Hence, we conducted additional robustness checks to only account for the same number of postings that are listed in the first page of a PC and the mobile screen. Table 6 shows that the results are robust to additional subsamples. We have selected three subsamples by including both clicked and unclicked observations when the post rank was $\leq 1 0 , \leq 2 0 .$ , and ≤ 30, respectively. Overall, our key coefficient estimates remain qualitatively the same in terms of the sign and the statistical significance.

An interesting observation from Table 6 is that as we move from the original sample to the top 10 ranked posts subsample, the magnitude of coefficient estimates for the product of rank and mobile increases in an absolute sense from −00089 in the original sample to −00127 in the sample consisting of top 10 posts. This suggests that ranking effects appear to be highest for the top ranked links in mobile settings. This observation should be interpreted with caution because a formal statistical test would not be valid given that the coefficients are identified up to scale. Still, the relatively high value of the coefficient in the sample consisting of top 10 posts is suggestive that ranking effects are relatively high on the mobile Internet even between the top few posts.

Table 4 Robustness to Alternative Specifications 4N = 11940

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="9">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.132***(0.011)</td><td>0.002**(0.001)</td><td>0.032**(0.013)</td><td>-0.040***(0.012)</td><td>-0.127***(0.005)</td><td>-0.004***(0.001)</td><td>-0.072**(0.007)</td><td>-0.011***(0.001)</td><td>-0.070(0.626)</td></tr><tr><td>Rank</td><td>-0.247***(0.016)</td><td>-0.083***(0.004)</td><td>0.0004(0.0003)</td><td>-0.005**(0.002)</td><td>-0.001(0.001)</td><td>-0.017*(0.010)</td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.148***(0.005)</td><td>0.001(0.002)</td><td>0.060***(0.016)</td><td>-0.073***(0.012)</td><td>-0.182***(0.064)</td><td>-0.002(0.003)</td><td>-0.139(0.091)</td><td>-0.008(0.022)</td><td>-0.082(0.674)</td></tr><tr><td>Distance</td><td>-0.163***(0.055)</td><td>-0.155***(0.059)</td><td>0.0005(0.0008)</td><td>-0.029**(0.013)</td><td>0.008**(0.004)</td><td>-0.047(0.045)</td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.153***(0.008)</td><td>0.003***(0.001)</td><td>0.052***(0.004)</td><td>-0.061***(0.007)</td><td>-0.124***(0.008)</td><td>-0.003***(0.001)</td><td>-0.058***(0.008)</td><td>-0.010***(0.001)</td><td>-0.075(0.652)</td></tr><tr><td>Rank</td><td>-0.232***(0.004)</td><td>-0.089***(0.007)</td><td>0.001(0.001)</td><td>-0.005***(0.001)</td><td>-0.001(0.001)</td><td>-0.006(0.010)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.114***(0.005)</td><td>-0.097***(0.006)</td><td>-0.001(0.001)</td><td>-0.010**(0.004)</td><td>0.009***(0.003)</td><td>-0.007(0.005)</td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.149**(0.063)</td><td>0.003***(0.001)</td><td>0.040***(0.010)</td><td>-0.012***(0.004)</td><td>-0.217***(0.050)</td><td>-0.002**(0.001)</td><td>-0.072***(0.020)</td><td>-0.011***(0.001)</td><td>-0.082(0.674)</td></tr><tr><td>Rank</td><td>-0.325***(0.068)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.159***(0.054)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.092***(0.029)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.180***(0.032)</td><td>0.004**(0.002)</td><td>0.085***(0.010)</td><td>-0.019***(0.006)</td><td>-0.087***(0.026)</td><td>-0.003***(0.001)</td><td>-0.076**(0.029)</td><td>-0.011***(0.001)</td><td>-0.084(0.677)</td></tr><tr><td>Rank</td><td>-0.252***(0.080)</td><td>-0.093***(0.030)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.136***(0.043)</td><td>-0.115***(0.040)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.080***(0.019)</td><td>-0.036***(0.009)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.  
Notes. Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity estimates are omitted for brevity.

Table 7 shows robustness to a model in which we included a variable that controls for the distance between a user (i.e., follower) and a post creator (i.e., followee). The rationale for using this control is that geographically close friends tend to click each other’s post. Table 8 shows robustness to including a variable for “time since last login” and its interaction with “Rank” as additional controls, to account for the possibility that different frequency of login behaviors could lead to the different ranking effects. For example, users that check the website frequently see fewer new posts with each login than do users that check in infrequently. Table 9 checks robustness to including a squared rank term to account for the possibility that ranking effects are nonlinear. Table 10 shows robustness to including a “page number” variable as an additional control. Because the page number and the rank variables are highly correlated, similar to Ghose et al. (2012), we used a “rank-within-a-page” variable instead of the original rank variable. When the microblogging website displays post messages, it only shows 30 posts per page in a PC whereas it shows 10 posts in a mobile phone. This restricts the rank order for each post within the range from 1 to 30 in a PC and from 1 to 10 in a mobile phone. The coefficient of the page number variable is negative and statistically significant, suggesting that a post that appears on an earlier page will receive significantly more clicks from users, just as one would expect. Qualitative results are robust to all of these different specifications.

Table 5 Robustness to Alternative Samples

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="9">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td></tr><tr><td colspan="11">(1) All users (not just dual-channel users; N = 8,896)</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.165***(0.005)</td><td>0.002**(0.001)</td><td>0.046***(0.004)</td><td>-0.048***(0.005)</td><td>-0.137***(0.005)</td><td>-0.003***(0.001)</td><td>-0.071***(0.003)</td><td>-0.009***(0.001)</td><td>-0.092(0.714)</td></tr><tr><td>Rank</td><td>-0.212***(0.006)</td><td>-0.080***(0.005)</td><td>0.0001(0.0001)</td><td>-0.004(0.005)</td><td>-0.002(0.002)</td><td>-0.012***(0.004)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.112***(0.004)</td><td>-0.097***(0.004)</td><td>-0.001(0.001)</td><td>-0.013***(0.003)</td><td>0.011***(0.003)</td><td>0.001(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.075***(0.004)</td><td>-0.011***(0.003)</td><td>0.0002(0.0002)</td><td>-0.001(0.003)</td><td>-0.002**(0.001)</td><td>-0.009***(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">(2) Subscribed posts only (N = 985)</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.154***(0.011)</td><td>0.003***(0.001)</td><td>0.043***(0.006)</td><td>-0.040***(0.004)</td><td>-0.141***(0.006)</td><td>-0.002**(0.001)</td><td>-0.068***(0.004)</td><td>-0.009***(0.001)</td><td>-0.086(0.684)</td></tr><tr><td>Rank</td><td>-0.235***(0.007)</td><td>-0.092***(0.005)</td><td>0.0002(0.0003)</td><td>-0.003(0.003)</td><td>-0.001(0.001)</td><td>-0.011**(0.005)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.110***(0.009)</td><td>-0.105***(0.004)</td><td>-0.001(0.001)</td><td>-0.019***(0.005)</td><td>0.016***(0.004)</td><td>0.001(0.007)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.083***(0.013)</td><td>-0.005**(0.002)</td><td>0.0002(0.0002)</td><td>-0.007*(0.004)</td><td>-0.002**(0.001)</td><td>-0.001(0.002)</td><td></td><td></td><td></td><td></td></tr></table>

Notes. Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity estimates are omitted for brevity.  
<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.

Table 6 Robustness to Additional Subsamples

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="9">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td></tr><tr><td></td><td></td><td colspan="9">(1) Rank ≤ 30 (N = 1,512)</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.172***(0.005)</td><td>0.003***(0.001)</td><td>0.040***(0.003)</td><td>-0.063***(0.004)</td><td>-0.120***(0.001)</td><td>-0.002**(0.001)</td><td>-0.081***(0.004)</td><td>-0.009***(0.001)</td><td>-0.094(0.732)</td></tr><tr><td>Rank</td><td>-0.250***(0.007)</td><td>-0.090***(0.006)</td><td>0.0001(0.0002)</td><td>0.003(0.004)</td><td>0.005***(0.001)</td><td>-0.024***(0.006)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.105***(0.003)</td><td>-0.098***(0.009)</td><td>-0.001(0.001)</td><td>-0.013***(0.004)</td><td>0.007**(0.003)</td><td>-0.004(0.006)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.080***(0.012)</td><td>-0.009***(0.003)</td><td>0.0001(0.0001)</td><td>-0.002(0.002)</td><td>0.002***(0.0006)</td><td>-0.007(0.005)</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="9">(2) Rank ≤ 20 (N = 1,355)</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.155***(0.004)</td><td>0.005***(0.001)</td><td>0.042***(0.003)</td><td>-0.073***(0.005)</td><td>-0.137***(0.003)</td><td>-0.001(0.001)</td><td>-0.062***(0.002)</td><td>-0.009***(0.001)</td><td>-0.069(0.625)</td></tr><tr><td>Rank</td><td>-0.235***(0.006)</td><td>-0.092***(0.003)</td><td>0.0001(0.0001)</td><td>-0.012***(0.002)</td><td>0.007***(0.001)</td><td>-0.050***(0.010)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.103***(0.005)</td><td>-0.097***(0.005)</td><td>-0.001(0.001)</td><td>-0.013***(0.002)</td><td>0.009**(0.004)</td><td>0.010***(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.075***(0.003)</td><td>-0.007*(0.004)</td><td>-0.0001(0.0001)</td><td>0.001(0.001)</td><td>0.002**(0.001)</td><td>-0.001(0.003)</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="9">(3) Rank ≤ 10 (N = 839)</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.167***(0.005)</td><td>0.001(0.001)</td><td>0.017*(0.010)</td><td>-0.035***(0.007)</td><td>-0.112***(0.007)</td><td>-0.002**(0.001)</td><td>-0.061***(0.008)</td><td>-0.008***(0.001)</td><td>-0.089(0.714)</td></tr><tr><td>Rank</td><td>-0.262***(0.013)</td><td>-0.127***(0.007)</td><td>0.002***(0.0003)</td><td>-0.101***(0.023)</td><td>-0.001(0.002)</td><td>-0.080***(0.024)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.118***(0.006)</td><td>-0.092***(0.003)</td><td>-0.001(0.001)</td><td>-0.024***(0.008)</td><td>-0.005(0.007)</td><td>0.031***(0.007)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.078***(0.004)</td><td>-0.035***(0.012)</td><td>-0.0005**(0.0002)</td><td>0.018***(0.006)</td><td>-0.004**(0.002)</td><td>-0.052***(0.011)</td><td></td><td></td><td></td><td></td></tr></table>

Notes. Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity estimates are omitted for brevity.  
<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.

Table 7 Robustness to User-Post Creator Distance

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="10">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td><td>User-post creator distance</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.150***(0.005)</td><td>0.002**(0.001)</td><td>0.044***(0.001)</td><td>-0.046***(0.001)</td><td>-0.125***(0.001)</td><td>-0.002**(0.001)</td><td>-0.069***(0.003)</td><td>-0.011***(0.001)</td><td>-0.095(0.549)</td><td>0.002**(0.001)</td></tr><tr><td>Rank</td><td>-0.226***(0.003)</td><td>-0.089***(0.004)</td><td>0.0003(0.0002)</td><td>-0.004(0.003)</td><td>-0.001(0.001)</td><td>-0.012***(0.002)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.112***(0.005)</td><td>-0.097***(0.002)</td><td>-0.001*(0.0006)</td><td>-0.010***(0.002)</td><td>0.012***(0.003)</td><td>0.003(0.002)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.066***(0.005)</td><td>-0.010***(0.003)</td><td>0.0002(0.0002)</td><td>-0.001(0.002)</td><td>-0.002**(0.001)</td><td>-0.008***(0.003)</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes. We used the dual channel user sample (N = 11940). Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity covariance estimates are omitted for brevity.  
<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.

Table 8 Robustness to Time Since Last Login

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="10">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td><td>Time since last login</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.154***(0.006)</td><td>0.002**(0.001)</td><td>0.040***(0.001)</td><td>-0.044***(0.002)</td><td>-0.129***(0.003)</td><td>-0.002**(0.001)</td><td>-0.068***(0.003)</td><td>-0.012***(0.001)</td><td>-0.096(0.751)</td><td>-0.063***(0.014)</td></tr><tr><td>Rank</td><td>-0.264***(0.028)</td><td>-0.094***(0.008)</td><td>0.0003(0.0002)</td><td>-0.004(0.003)</td><td>-0.001(0.001)</td><td>-0.012***(0.002)</td><td></td><td></td><td></td><td></td><td>0.012***(0.004)</td></tr><tr><td>Distance</td><td>-0.113***(0.006)</td><td>-0.093***(0.008)</td><td>-0.001**(0.0005)</td><td>-0.010***(0.002)</td><td>0.010***(0.003)</td><td>0.003(0.002)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.067***(0.008)</td><td>-0.011***(0.003)</td><td>0.0002(0.0002)</td><td>-0.002(0.002)</td><td>-0.002**(0.001)</td><td>-0.010***(0.003)</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes. We used the dual channel user sample (N = 11940). The temporal unit of “time since last login” variable is a “day.” Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity covariance estimates are omitted for brevity <sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.

Table 9 Robustness to Nonlinear Ranking Effects

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="9">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.160***(0.002)</td><td>0.002**(0.001)</td><td>0.046***(0.001)</td><td>-0.044***(0.001)</td><td>-0.127***(0.001)</td><td>-0.002**(0.001)</td><td>-0.069***(0.004)</td><td>-0.012***(0.002)</td><td>-0.083(0.591)</td></tr><tr><td>Rank</td><td>-0.258***(0.009)</td><td>-0.110***(0.010)</td><td>0.0003(0.0002)</td><td>-0.003(0.003)</td><td>-0.001(0.001)</td><td>-0.012***(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.113***(0.004)</td><td>-0.094***(0.005)</td><td>-0.001*(0.0006)</td><td>-0.009***(0.003)</td><td>0.012***(0.003)</td><td>0.003(0.002)</td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.058***(0.004)</td><td>-0.014***(0.002)</td><td>0.0002(0.0002)</td><td>-0.001(0.002)</td><td>-0.002**(0.001)</td><td>-0.009***(0.003)</td><td></td><td></td><td></td><td></td></tr><tr><td> $Rank^2$ </td><td>0.001***(0.0002)</td><td>0.004***(0.001)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes. We used the dual channel user sample (N = 11940). Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity covariance estimates are omitted for brevity.  
<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.

Table 10 Robustness to Page Number

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Main effect</td><td colspan="10">Moderating effect</td></tr><tr><td>Mobile</td><td>Followee</td><td>Sub-scription</td><td>Age</td><td>Male</td><td>Brand tenure</td><td>Post tenure</td><td>Post tenure × Mobile</td><td>Nongeographic brands × Mobile</td><td>Page number</td></tr><tr><td>Intercept</td><td>Brand post fixed effect</td><td>0.251***(0.008)</td><td>0.002**(0.001)</td><td>0.044***(0.002)</td><td>-0.046***(0.002)</td><td>-0.128***(0.001)</td><td>-0.002**(0.001)</td><td>-0.070***(0.003)</td><td>-0.012***(0.002)</td><td>-0.104(0.729)</td><td>-1.549***(0.007)</td></tr><tr><td>Rank</td><td>-0.095***(0.005)</td><td>-0.150***(0.012)</td><td>0.0003(0.0002)</td><td>-0.005(0.004)</td><td>-0.001(0.002)</td><td>-0.009***(0.003)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.088***(0.007)</td><td>-0.091***(0.005)</td><td>-0.001(0.002)</td><td>-0.008***(0.002)</td><td>0.012***(0.003)</td><td>0.003(0.002)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rank × Distance</td><td>-0.052***(0.006)</td><td>-0.011***(0.002)</td><td>0.0002(0.0002)</td><td>-0.001(0.002)</td><td>-0.002**(0.001)</td><td>-0.007**(0.003)</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes. We used the dual channel user sample (N = 11940). Rank refers to a “rank-within-a-page” variable. Posterior means and posterior deviations (in parentheses) are reported. Coefficients for brand post fixed effects and unobserved heterogeneity covariance estimates are omitted for brevity.  
<sup>∗</sup>Denotes significant at 0.10, <sup>∗∗</sup>denotes significant at 0.05, and <sup>∗∗∗</sup>denotes significant at 0.01.

## 6. Discussion and Implications

We examine how the economics of the mobile Internet differ from the economics of the PC-based Internet. Focusing on ranking effects and distance effects, we show that ranking effects are higher on the mobile Internet and preferences for geographically proximate brands are also higher.

This study provides several important insights for managers. First, and most directly, our results can provide microblogging service companies with insights about how they can target access channel-based sponsored messages using the information about whether a user accessed through a PC or a mobile phone. Our results show there are stronger ranking effects in a mobile phone setting compared to a PC setting. This has useful implications for the monetization of social media and user-generated content in such settings. Increasingly, as in sponsored search ads, we see microblogging sites move toward a model of sponsored posts (tweets) in which advertisers can bid on rank. In particular, the asymmetric ranking effect suggests that microblogging companies can charge different prices to advertisers for sponsored messages based on the type of user access channel. For example, the stronger ranking effect on mobile phone users implies that for a given brand advertisement, microblogging platforms such as Twitter can charge more for a high ranking of sponsored messages displayed on mobile phone users as opposed to PC users. Similarly, our results suggest that advertisers that buy positions (rank) in sponsored search listings have an incentive to bid higher for the highest ranked sponsored links in mobile phones as compared to PCs. Of course, to be clear, one would also have to take into account the penetration and reach of such devices in any customized pricing strategy for ads.

Second, our results can provide microblogging companies and advertisers with insights about how they can target location-based sponsored messages using geographical proximity between users and brand stores. Our results show that users in our microblogging setting exhibit strong local interests, particularly on mobile devices. Hence, when sponsored messages are accompanied with user-generated posts, as the proportion of mobile users increases, such messages should be increasingly related to brands with a presence near the user’s geographic location.

Finally, and most generally, our results contrast with the literature on the PC-based Internet that has hypothesized and documented that lower search costs and geographic frictions mean that the PC-based Internet is a particularly competitive environment. If higher ranking effects and increased importance of geographic proximity mean that search costs and geographic frictions are higher on the mobile Internet than on the PC-based Internet, it suggests that competition in the mobile Internet may be relatively muted compared to that on the PC-based Internet. This suggests that product pricing and price dispersion are likely to be somewhat different on the mobile Internet than on the PC-based Internet.

Although we showed these results in the context of microblogging, the implications are potentially broader. Mobile devices are increasingly important tools for accessing the Internet. Although it is possible there are differences from setting to setting, our results can be interpreted to suggest that higher search costs and higher benefits to geographic targeting may impact all aspects of the mobile Internet including search engines, e-commerce sites, and social media sites. Furthermore, and more speculatively, such higher search costs may mean higher equilibrium prices, more price dispersion, less product variety, and more market concentration as the mobile Internet grows in importance. Larger distance effects in the mobile Internet may mean an increasing role for local businesses (and perhaps even local social relationships) in determining online behavior.

Data availability issues suggest that some caution is warranted in this speculation. For example, we do not observe users’ Internet surfing location, only their address. Hence, we cannot claim a “contextual effect” here in which the immediate environment plays a role in consumer’s mobile usage behavior. Moreover, we do not have information about the textual content in a microblog post (e.g., length, sentiment, theme) and therefore cannot examine how specific content matters across channels. Furthermore, our analysis focuses on brand posts in the microblogging setting, and it is possible that the magnitudes of the differences across access channels will vary across settings, particularly settings where users engage in directed search. Our analysis also focuses on a reduced form of a more general utility structure. We cannot separately identify a consideration set and a user’s sequential searching behavior because of limitations in our data. Future work may consider using a model of the underlying search process and structurally estimate search costs (e.g., Hong and Shum 2006, Hortaçsu and Syverson 2004, among others), provided they have data on user browsing patterns. In addition, our analysis assumes linearity of ranking and distance effects, and it is possible that these effects will be nonlinear. Future research may model such nonlinearity and even rank-specific and mile-specific distance effects (e.g., Ghose and Yang 2009, Carare 2011). Finally, our data on the mobile Internet comes from mobile phones only. It does not address tablet computers such as iPads, which have somewhat larger screens than phones but are somewhat heavier and less mobile (Sideways 2011). Future research can examine if consumers’ usage of the Internet on these tablet devices is more similar to PCs or mobile phones.

Notwithstanding these limitations, our analysis documents higher ranking effects associated with the mobile Internet as well as a greater role for geographic proximity. To the extent that ranking effects and geographic proximity affect market outcomes online, the increasing size of the mobile Internet may have profound implications for the future direction of Internet commerce.

## Acknowledgments

The authors thank the Wharton Interactive Media Initiative for support and Ramayya Krishnan; Vandana Ranachandran; Raghuram Iyengar; and seminar participants at SICS 2011, Marketing Science Conference 2011, Second Annual Searle Center Conference on Internet

Search and Innovation 2011, SCECR 2011, WISE 2010, INFORMS-CIST 2010, and the MSI-WIMI Conference on Crossplatform and Multichannel Customer Behavior for helpful comments. Avi Goldfarb thanks SSHRC for generous support. Anindya Ghose acknowledges the financial support from NSF CAREER Award IIS-0643847 and a Google Research grant. Sang Pil Han acknowledges the financial support from City University of Hong Kong Grant [Project 7200265] and a GRF grant from the Research Grants Council of the Hong Kong SAR, City University of Hong Kong [143312]. Support was also provided by a MSI-WIMI research grant. All opinions and errors are the authors’ alone.

## Appendix. The MCMC Algorithm

We ran the MCMC chain for 60,000 iterations and used the last 20,000 iterations to compute the mean and standard deviation of the posterior distribution of the model parameters. We report below the MCMC algorithm for the full model.

Step 1. Draw $\underline { { \lambda } } _ { i } \mathrm { : }$ Conditional (A) can be written as follows:

$$
\operatorname * {P r} (\underline {{\lambda}} _ {i} \mid \underline {{\mu}}, \Lambda , y _ {i}) \propto L _ {i} (\underline {{\lambda}} _ {i} \mid \underline {{\mu}}, y _ {i}) \cdot \operatorname * {P r} (\underline {{\lambda}} _ {i} \mid \Lambda).\tag{15}
$$

Recall that $L _ { i } ( \underline { { \lambda } } _ { i } \mid \underline { { \mu } } , y _ { i } )$ is the same as $L _ { i } ( y _ { i } \mid \underline { { \mu } } , \underline { { \lambda } } _ { i } )$ in a conceptual manner. Then it is important to note that in conditional $( \mathrm { A } )$ we cannot apply normal-normal conjugacy because likelihood is based on type 1 extreme value distribution, whereas the prior is based on normal distribution. When we compute the posterior, we need to multiply the likelihood by the prior. Hence, we use Metropolis-Hasting algorithm to generate draws of $\underline { { \lambda } } _ { i } . ~ \mathrm { A }$ chain of draws for $\underline { { \lambda } } _ { i }$ can be generated in the following way:

$$
\underline {{\lambda}} _ {i} ^ {c} \sim N (\underline {{\lambda}} _ {i} ^ {(m)}, \Omega_ {i} ^ {(m)}),\tag{16}
$$

where $\Omega _ { i } ^ { ( m ) }$ is an individual $i ^ { \prime } \mathrm { s }$ mth iteration. In addition, we use the adaptive Metropolis-Hasting algorithm (Andrieu and Atchadè 2007) to generate draws with higher efficiency while maintaining Markov chain properties with the acceptance probability given by

$$
a (\underline {{\lambda}} _ {i} ^ {(m)}; \underline {{\lambda}} _ {i} ^ {c}) = \min \bigg \{1, \frac {L _ {i} (\underline {{\lambda}} _ {i} ^ {c} \mid y _ {i}) \cdot \operatorname* {P r} (\underline {{\lambda}} _ {i} ^ {c} \mid \underline {{\mu}} , \Lambda)}{L _ {i} (\underline {{\lambda}} _ {i} ^ {(m)} \mid y _ {i}) \cdot \operatorname* {P r} (\underline {{\lambda}} _ {i} ^ {(m)} \mid \underline {{\mu}} , \Lambda)} \bigg \}.\tag{17}
$$

Step 2. Draw $\underline { { \mu } } = [ \bar { \beta } ^ { \prime } , \alpha ^ { \prime } ] \mathrm { : }$ : Conditional (B) can be written as follows:

$$
\begin{array}{c} \operatorname * {P r} (\underline {{\mu}} \mid \Lambda , \{\underline {{\lambda}} _ {i} \} _ {i = 1} ^ {n}, \{y _ {i} \} _ {i = 1} ^ {n}) \\ \propto L (\underline {{\mu}} \mid \{\underline {{\lambda}} _ {i} \} _ {i = 1} ^ {n}, \{y _ {i} \} _ {i = 1} ^ {n}) \cdot \operatorname * {P r} (\underline {{\mu}} \mid \Lambda), \end{array}\tag{18}
$$

where n is the total number of users in the sample. Recall that $L ( \underline { { \mu } } | \{ \underline { { \lambda } } _ { i } \} _ { i = 1 } ^ { n } , \{ y _ { i } \} _ { i = 1 } ^ { n } )$ is the same as $L ( \{ y _ { i } \} _ { i = 1 } ^ { n } | { \bar { \{ \underline { { \lambda } } } }  _ { i } \} _ { i = 1 } ^ { n } , \underline { { \mu } } )$ in a conceptual manner. Then in conditional (B) we cannot apply normal-normal conjugacy because likelihood is based on type 1 extreme value distribution, whereas the prior is based on normal distribution. Hence, we use Metropolis-Hasting algorithm to generate draws of $\mu = [ \bar { \beta } ^ { \prime } , \alpha ^ { \prime } ]$ . A chain of draws for $\mu$ can be generated in the following way:

$$
\underline {{\mu}} ^ {c} \sim N (\underline {{\mu}} ^ {(m)}, \Psi^ {(m)}),\tag{19}
$$

where $\Psi ^ { ( m ) }$ is a tuning constant at mth iteration. We set the multivariate normal prior for $\underline { { \boldsymbol { \mu } } }$ such that $\underline { { \mu } } \sim N ( \underline { { \eta } } , C ) \underline { { \eta } }$ is a zero vector of size npar $( \mathrm { i . e . , }$ , the number of random coefficients in the model) and inversed C is the npar×npar square matrix with 0.001 on the main diagonal and zeros elsewhere. We select these diffuse hyperparameter values (i.e., very small values for the diagonal elements in the inverse of the variance hyperparamer) to ensure that the choice of the multivariate prior distribution becomes less informative. Similar to conditional (A), we use the adaptive Metropolis-Hasting algorithm to generate draws with the acceptance probability given by

$$
\begin{array}{l} a (\underline {{\mu}} ^ {(m)}; \underline {{\mu}} ^ {c}) \\ = \min \bigg \{1, \frac {L (\underline {{\mu}} ^ {c} \mid \{\underline {{\lambda}} _ {i} \} _ {i = 1} ^ {n} , \{y _ {i} \} _ {i = 1} ^ {n}) \cdot \operatorname* {P r} (\underline {{\mu}} ^ {c} \mid \Lambda)}{L (\underline {{\mu}} ^ {(m)} \mid \{\underline {{\lambda}} _ {i} \} _ {i = 1} ^ {n} , \{y _ {i} \} _ {i = 1} ^ {n}) \cdot \operatorname* {P r} (\underline {{\mu}} ^ {(m)} \mid \Lambda)} \bigg \}. \end{array}\tag{20}
$$

Step 3. Draw $\Lambda ^ { - 1 } ;$ Conditional (C) can be computed using Wishart distribution as follows:

$$
\operatorname * {P r} \left(\Lambda^ {- 1} \mid \{\underline {{\lambda}} _ {i} \} _ {i = 1} ^ {n}\right) = W \left(\rho + n, \left(\sum_ {i = 1} ^ {n} \underline {{\lambda}} _ {i} \underline {{\lambda}} _ {i} ^ {\prime} + R ^ {- 1}\right) ^ {- 1}\right).\tag{21}
$$

We set the Wishart prior for $\Lambda ^ { - 1 }$ such that $\Lambda ^ { - 1 } \sim W ( \rho , R )$ where $\rho$ is the degree of freedom and R is a scale matrix. To ensure that the choice of the Wishart prior become less informative, we select the value for $\rho$ as $n p a r + 2$ and we also set the value for R to the identity matrix of size npar. Note that npar is 4 in the main model. We inverse $\Lambda ^ { - \dot { 1 } }$ to generate draws of å.

## References

Adipat B, Zhang D, Zhou L (2011) The effects of tree-view based presentation adaptation on mobile web browsing. Management Inform. Systems Quart. 35(1):99–121.

Agarwal A, Hosanagar K, Smith MD (2011) Location, location, location: An analysis of profitability of position in online advertising markets. J. Marketing Res. 48(6):1057–1073.

Albers M, Kim L (2000) User Web browsing characteristics using Palm handhelds for information retrieval. Proc. IEEE Professional Comm. Soc. Internat. Professional Comm. Conf., Cambridge, MA (IEEE Educational Activities Department, Piscataway, NJ), 125–135.

Anderson E, Fong N, Simester D, Tucker C (2010) How sales taxes affect customer and firm behavior: The role of search on the Internet. J. Marketing Res. 47(2):229–239.

Andrieu C, Atchadè Y (2007) On the efficiency of adaptive MCMC algorithms. Electronic Comm. Probab. 12(December):336–349.

Ansari A, Mela C (2003) E-customization. J. Marketing Res. 40(2):131–145.

Atchadè Y (2006) An adaptive version for the Metropolis adjusted Langevin algorithm with a truncated drift. Methodology Comput. Appl. Probab. 8:235–254.

Autor D (2001) Wiring the labor market. J. Econom. Perspectives 15(1):25–40.

Bakos J (1997) Reducing buyer search costs: Implications for electronic marketplaces. Management Sci. 43(12):1676–1692.

Balasubramanian S (1998) Mail versus mall: A strategic analysis of competition between direct marketers and conventional retailers. Marketing Sci. 17(3):181–195.

Barkuus L, Dey A (2003) Location-based services for mobile telephony: A study of users’ privacy concerns. Proc. 9TH IFIP TC13 Internat. Conf. Human-Comput. Interaction, Zurich, Switzerland, September 1–5 (IOS Press, Lansdale, PA).

Baye M, Gatii R, Kattuman P, Morgan J (2009) Clicks, discontinuities, and firm demand online. J. Econom. Management Strategy 18(4):935–975.

Becker S (1954) Why an order effect? Public Opinion Quart. 18(3):271–278.

Blum B, Goldfarb A (2006) Does the Internet defy the law of gravity? J. Internat. Econom. 70(2):384–405.

Boyd D, Golder S, Lotan G (2010) Tweet, tweet, retweet: Conversational aspects of retweeting on twitter. Proc. 43th Hawaii Internat. Conf. System Sci. (IEEE Computer Society, Washington, DC).

Brimicombe A, Li Y (2006) Mobile space-time envelopes for location-based services. Trans. Geographical Inform. Systems 10(1):5–23.

Brown J, Goolsbee A (2002) Does the Internet make markets more competitive? Evidence from the life insurance industry. J. Political Econom. 110(3):481–507.

Brynjolfsson E, Smith M (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Brynjolfsson E, Dick A, Smith M (2010) A nearly perfect market? Differentiation versus price in consumer choice. Quantit. Marketing Econom. 8(1):1–33.

Brynjolfsson E, Hu YJ, Smith M (2003) Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers. Management Sci. 49(11):1580–1596.

Cairncross F (1997) The Death of Distance (Harvard University Press, Cambridge, MA).

Carare O (2011) The impact of bestseller rank on demand: Evidence from the app market. Internat. Econom. Rev. 53(3):717–742.

Carney DR, Banaji MR (2008) First is best. PLOS ONE 7(6):1–5.

Chae M, Kim J (2004) Do size and structure matter to mobile users? An empirical study of the effects of screen size, information structure, and task complexity on user activities with standard Web phones. Behav. Inform. Tech. 23(3):165–181.

Chib S, Greenberg E (1995) Understanding the Metropolis-Hastings algorithm. Amer. Statistician 49(4):327–335.

Choi J, Bell D (2011) Preference minorities and the Internet. J. Marketing Res. 48(4):670–682.

Coney K (1977) Order bias: The special case of letter preference. Public Opinion Quart. 41(3):385–388.

Davison H, Wickens C (1999) Rotocraft hazard cueing: The effects on attention and trust. Technical Report ARL-99-5/NASA-99-1, University of Illinois, Aviation Research Lab, Savoy, IL.

Dean M (1980) Presentation order effects in product taste tests. J. Psych. 105(1):107–110.

Drèze X, Zufryden F (2004) The measurement of online visibility and its impact on Internet traffic. J. Interactive Marketing 18(1):20–37.

Dover Y, Muchnik L, Goldenberg J (2012) The effect of transmitter activity on information dissemination over online social networks. Working paper, University of Pittsburgh.

Ellison G, Ellison SF (2009) Search, obfuscation, and price elasticities on the Internet. Econometrica 77(2):427–452.

Fellmann J, Getis A, Getis J (2000) Human Geography, 6th ed.(McGraw-Hill, New York).

Forman C, Ghose A, Goldfarb A (2009) Competition between local and electronic markets: How the benefit of buying online depends on where you live. Management Sci. 55(1):47–57.

Friedman T (2005) The World is Flat: A Brief History of the Twenty-First Century (Farrar, Straus, and Giroux, New York).

Fusco SJ, Michael K, Michael MG (2010) Using a social informatics framework to study the effects of location-based social networking on relationships between people: A review of literature. Proc. 2011 IEEE Internat. Sympos. Tech. Soc., June 7–9, Wollongong, NSW, Australia (IEEE Society on Social Implications of Technology, Stamford, CT), 157–171.

Gelman A, Rubin D (1992) Inference from iterative simulation using multiple sequences. Statist. Sci. 7:457–511.

Ghose A, Han S (2010) A dynamic structural model of user learning in mobile media content. Working paper, SSRN.

Ghose A, Han S (2011) An empirical analysis of user content generation and usage behavior on the mobile Internet. Management Sci. 57(9):1671–1691.

Ghose A, Han S (2012) Estimating demand for mobile apps in the new economy. Working paper, New York University, New York.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Ghose A, Ipeirotis P, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowd-sourced content. Marketing Sci. 31(3):493–520.

Hampton K, Wellman B (2002) Neighboring in Netville: How the Internet supports community and social capital in a wired suburb. City Community 2(3):277–311.

Hastings K (1970) Monte Carlo sampling methods using Markov chains and their applications. Biometrika 57(1):97–109.

Holmes C, Held L (2006) Bayesian auxiliary variable models for binary and multinomial regression. Bayesian Anal. 1(1):145–168.

Homans G (1958) Social behaviors as exchange. Amer. J. Sociol. 63(6):597–606.

Hong H, Shum M (2006) Using price distributions to estimate search costs. RAND J. Econom. 37(2):257–275.

Hortaçsu A, Syverson C (2004) Product differentiation, search costs, and competition in the mutual fund industry: A case study of S&P 500 index funds. Quart. J. Econom. 119(2):403–456.

Java A, Song X, Finin T, Tseng B (2007) Why we Twitter: Understanding microblogging usage and communities. Proc. Joint 9th WEBKDD and 1st SNA-KDD Workshop (ACM, New York).

Jiang B, Yao X (2006) Location-based services and GIS in perspective. Comput., Environment Urban Systems 30(6):712–725.

Jones M, Marsden G, Mohd-Nasir N, Boone K (1999) Improving Web interaction on small displays. Comput. Networks 31(11–16):1129–1137.

Kim J, Albuquerque P, Bronnenberg B (2010) Online demand under limited consumer search. Marketing Sci. 29(6):1001–1023.

Kuksov D (2004) Buyer search costs and endogenous product design. Marketing Sci. 23(4):490–499.

Lindqvist J, Cranshaw J, Wiese J, Hong J, Zimmerman J (2011) I’m the mayor of my house: Examining why people use Foursquare—A social-driven location sharing application. CHI 2011 May 7–12, Vancouver, BC, Canada (ACM, New York), 2409–2418.

Luca C (2006) Visualizing information on mobile devices. Computer 39(3):40–45.

Lynch JG, Ariely D (2000) Wine online: Search costs affect competition on price, quality, and distribution. Marketing Sci. 19(1):83–103.

Maniar N, Bennett E, Hand S, Allan G (2008) The effect of mobile phone screen size on video based learning. J. Software 3(4):51–61.

Miller J, Krosnick J (1998) The impact of candidate name order on election outcomes. Public Opinion Quart. 62(3):291–330.

Mountain D, Myrhaug H, Goker A (2009) Mobile search. Göker A, Davis J, eds. Information Retrieval: Searching in the 21st Century (John Wiley & Sons, Chichester, UK), 103–130.

Nunamaker JF, Applegate LM, Konsynski BR (1987) Facilitating group creativity: Experience with a group decision support system. J. Management Inform. Systems 3(4):5–19.

Nunamaker JF, Applegate LM, Konsynski BR (1988) Computeraided deliberation: Model management and group decision support. J. Oper. Res. 36(6):826–848.

Scott Morton F, Zettlemeyer F, Silva-Risso J (2001) Internet car retailing. J. Indust. Econom. 49(4 Dec):501–520.

Shankar V, Balasubramanian S (2009) Mobile marketing: A synthesis and prognosis. J. Interactive Marketing 23(2):118–129.

Shankar V, Venkatesh A, Hofacker C, Naik P (2010) Mobile marketing in the retailing environment: Current insights and future research avenues. J. Interactive Marketing 24(2):111–120.

Sideways (2011) Turning the page: How digital technology is changing the way we read. White paper, http://www.sideways .com/whitepapers/reading\_habits.pdf.

Sinisalo J (2011) The role of the mobile medium in multichannel CRM communication. Internat. J. Electronic Customer Relationship Management 5(1):23–45.

Sultan F, Rohm A, and Gao T (2009) Factors influencing consumer acceptance of mobile marketing: A two country study of youth markets. J. Interactive Marketing 23(4):308–320.

Sweeney S, Crestani F (2006) Effective search results summary size and device screen size: Is there a relationship? Inform. Processing Management 42(4):1056–1074.

Tobler W (1970) A computer movie simulating urban growth in the Detroit region. Econom. Geography 46(2):234–240.

van der Lans R (2011) Bayesian estimation of the multinomial logit model: A comment on Holmes and Held, “Bayesian auxiliary models for binary and multinomial regression.” Bayesian Anal. 6(2):353–356.

Xia M, Huang Y, Duan W, Whiston A (2012) To continue sharing or not to continue sharing? An empirical analysis of user decision in peer-to-peer sharing networks. Inform. Systems Res. 23(1):247–259.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.

Yao S, Mela C (2011) A dynamic model of sponsored search advertising. Marketing Sci. 30(3):447–468.

Zhang X (2009) Retailers’ multichannel and price advertising strategies. Marketing Sci. 28(6):1080–1094.
