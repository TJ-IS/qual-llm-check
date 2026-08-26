---
otero_id: 15676
otero_key: "2A2HED32"
title: "Triadic Closure, Homophily, and Reciprocation: An Empirical Investigation of Social Ties Between Content Providers"
authors: "Tingting Song; Qian Tang; Jinghua Huang"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0838"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.235.66.10] On: 09 September 2019, At: 17:32 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/2A2HED32/fulltext/images/64ba2495339b80a398ec8dcd4b7183e10bd4715afa682d5ac958c053b6329599.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Triadic Closure, Homophily, and Reciprocation: An Empirical Investigation of Social Ties Between Content Providers

Tingting Song, Qian Tang, Jinghua Huang

To cite this article: Tingting Song, Qian Tang, Jinghua Huang (2019) Triadic Closure, Homophily, and Reciprocation: An Empirical Investigation of Social Ties Between Content Providers. Information Systems Research

Published online in Articles in Advance 29 Aug 2019

https://doi.org/10.1287/isre.2019.0838

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Triadic Closure, Homophily, and Reciprocation: An Empirical Investigation of Social Ties Between Content Providers

Tingting Song,<sup>a</sup> Qian Tang,<sup>b</sup> Jinghua Huang<sup>c</sup>

<sup>a</sup> Antai College of Economics and Management, Shanghai Jiao Tong University, Shanghai, China 200030; <sup>b</sup> School of Information Systems, Singapore Management University, Singapore 178902; <sup>c</sup> Research Center for Contemporary Management, School of Economics and Management, Tsinghua University, Beijing, China 100084

Contact: songtt@sjtu.edu.cn, http://orcid.org/0000-0002-5079-5652 (TS); qiantang@smu.edu.sg,

http://orcid.org/0000-0003-3122-8668 (QT); huangjh@sem.tsinghua.edu.cn, http://orcid.org/0000-0003-4344-7884 (JH)

Received: Revised: April 18, 2017; February 12, 2018: April 18, Accepted: Published Online in Articles in Advance: August 29, 2019

https://doi.org/10.1287/isre.2019.0838

Copyright:

Abstract. In social media, a content provider can initiate outgoing ties to other providers to promote their content, thus inviting reciprocal promotion. We investigate how the reciprocation benefit for the initiating provider is affected by homophily and triadic closure, the two major mechanisms of tie formation. Specifically, we examine how the increase in subscribers and viewership of the initiating provider’s content attributable to the responding providers’ reciprocation is moderated by common ties and content similarit between the two linked providers. Using panel data on 27,356 YouTube video providers, we specify a switching regression model to estimate the influence of content similarity and common ties on reciprocation impact while correcting for their influence on reciprocation probability. Confirming that reciprocation is generally beneficial for the initiator, we find that although content similarity and common ties increase reciprocation probability, they reduce the reciprocation benefit for the initiator in terms of subscriber growth. We also find a positive interaction effect between content similarity and common ties on reciprocation impact, reducing their individual effects. Combining their respective influence on reciprocation probability and benefit, we further examine how content similarity and common ties affect the expected benefit for the initiator and derive practical implications for content providers and social media platforms.

History: Paul Pavlou, Senior Editor; Gal Oestreicher-Singer, Associate Editor Funding: J. Huang received financial support from the National Natural Science Foundation of China [Grants 71490721 and 71272028]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0838

Keywords: social networking • user-generated content • reciprocation • switching regression model • homophily • triadic closure

## 1. Introduction

Over the past decade, social media have revolutionized interpersonal communication by integrating the explosive growth of user-generated content (UGC) with enormous social networking opportunities. Networking functions allow content consumers both to become friends with other consumers and to follow content providers, thereby discovering content of interest. Recently, many social media platforms have launched additional networking functions that enable providers to link and collaborate. Such collaboration often starts with a provider initiating a one-way tie to other providers. For example, bloggers can unilaterally link their posts to others’ posts through permalinks, and You-Tube providers can unilaterally link to other providers by listing them as “Featured Channels” on their You-Tube channels (Figure 1). These one-way links help direct consumers to the linked posts or providers. For the platform, linking among providers facilitates consumers’ content discovery and extends their overall viewing sessions. The initiators, however, do not benefit until the other providers reciprocate.<sup>1</sup>

Many studies on the formation and impact of social ties focus on either the ties between content consumers in the “friends” format (e.g., Granovetter 1973, Brown and Reingen 1987, Godes and Mayzlin 2009, Bapna and Umyarov 2015) or the ties between con sumers and providers in the “following” or “subscription” format (e.g., Sheldon et al. 2011, Susarla et al. 2012, Tang et al. 2012, Goes et al. 2014, Shi et al. 2014). The ties between content providers have not been well understood, especially with respect to their reciprocation. The scarce literature on ties between providers has studied how providers’ content affects their linking behavior (Ma 2010), how ties induce the linked providers to change content (Zeng and Wei 2013, Wang et al. 2018), and how one-way ties benefit the initiators (Katona and Sarvary 2008, Mayzlin and Yoganarasimhan 2012) and the providers to which they link (Stephen and Toubia 2010

Figure 1. (Color online) Featured Channels of a Sample YouTube Provider  
![](/api/attachments/2A2HED32/fulltext/images/94522a72e1b0279ca183a2bfbaf202dd9e0ccf0f3ed75f3c59fbdca493634b49.jpg)

Jabr and Zheng 2014). Gaudeul and Giannetti (2013) in particular investigate the reciprocation of ties between bloggers and its impact on the bloggers’ social capital.

In social networks, reciprocation in general occurs when individuals send ties to those from whom they receive ties. This phenomenon is commonly explained by social exchange theory, which suggests that people invest in social relations and expect rewards in return (Emerson 1976, Rusbult and Buunk 1993). Therefore, not only is reciprocation important for the emergence of relations, but reciprocal relations are also more stable than unilateral ones (Hallinan 1978, Runger and Wasserman 1979). Eventually, unreciprocated links are very likely to be dropped. However, reciprocation is often studied as one of the mechanisms underlying network evolution without investigating the mechanisms of reciprocation. For the formation of nondirectional ties, homophily and triadic closure are two of the most observed phenomena (Kossinets and Watts 2009, Easley and Kleinberg 2010). Whereas homophily refers to the tendency of individuals to form ties with people similar to themselves, triadic closure describes the tie formation between two people by means of common ties. However, the issue of whether homophily and triadic closure similarly drive reciprocation for directional ties has not yet been tested. Additionally, it is more important to understand the roles of homophily and triadic closure in the impact of reciprocation on the initiators. As confirmed by Gaudeul and Giannetti (2013), reciprocation increases the social capital (e.g., audience size) of the initiating providers. Nevertheless, it remains unclear what moderates the impact of tie reciprocation.

Our primary goal in this study is to propose a theoretical framework that links homophily and triadic forces to reciprocation and its impact on the initiating providers, extending social tie theories beyond tie formation to the impact of social ties. With homophily and triadic closure, we examine how the impact of social ties is affected by the similarities of the nodes and the commonalities of the nodes’ existing ties. The interaction between homophily and triadic closure is also explored. The influence of homophily and triadic closure on the formation of reciprocating ties serves as a test of existing social tie theories in the context of reciprocation of directional ties. It is also included to control for the endogeneity of reciprocation when studying the impact of reciprocating ties.

To achieve our research objectives, we collected a panel data set from YouTube on the “Featured Channel” links for 27,356 video providers. Using rare longitudinal network data on these providers (Kossinets and Watts 2006), we identified 4,478 provider pairs whose tie initiation occurred during our study period. Using a switching regression model, we find that although common ties and content similarity increase reciprocation probability, they negatively moderate the reciprocation impact for the initiating providers. Furthermore, common ties and content similarity have a significantly positive interaction effect on reciprocation impact, reducing their negative individual effects. Combining their influence on both reciprocation probability and impact, we further examine their impacts on the expected benefit for the initiator. Holding all other variables at the sample averages, we find that the relationship between the expected benefit and common ties and the relationship between the expected benefit and content similarity are both inverted-U shaped. Moreover, the expected benefit generally increases as content similarity increases when the number of common ties is small, but it decreases as similarity increases when the number of common ties is large.

## 2. Theoretical Background and Hypotheses

For the initiators, the reciprocating ties from the responding providers add to their social capital (Lin 2001), which can provide information and resource benefits (Burt 1992, Powell et al. 1996), and coordination benefits (Coleman 1990, Uzzi 1997). In particular, reciprocating ties create value by bringing in potential consumers and making the initiators content more accessible (Stephen and Toubia 2010). According to the previous studies, homophily and triadic closure have extremely pronounced effects on the formation of social ties (Ruef et al. 2003) and social capital (Rodan and Galunic 2004). Homophily—that is, the dyad similarity—considers the extrinsic characteristics of the network content; whereas triadic closure—that is, the overlap in the triadic connections to others (Fracassi 2017, Peng et al. 2018)—is an intrinsic characteristic of the network structure (Hong et al. 2018).

## 2.1. Triadic Closure

From a network structural perspective, triadic closure, also called transitivity or clustering, refers to tie formation in open triads, which tends to close over time (Kossinets and Watts 2006). According to the triadic closure principle, two people with a common friend have an increased likelihood of becoming friends themselves through the social influence (i.e., opportunities to meet each other, a basis for trusting each other, and latent pressure) of their common friends (Easley and Kleinberg 2010, Zhang et al. 2018). It is necessary to think of triadic closure not only for a single triad but also for the triads within a large group or even the entire network. As one mutual connection increases the probability of tie formation between two individuals, multiple mutual connections increase the probability even more (Louch 2000). Previous research has established that a greater number of mutual third-party connections between the influencer and the target amplify the peer influence on the target in terms of cooperation and trust (Aral and Walker 2014, Bapna et al. 2017a, Hong et al. 2018). Accordingly, triadic closure predicts increased reciprocation probability from the responding providers, who share more common ties with the initiating providers.

On tie formation, triadic closure also affects the social capital value of the formed tie by influencing its information benefits for the linked parties. As shown by Shi et al. (2014), information novelty increases information benefits for audiences. Moreover, different audiences perceive the novelty of the same information differently depending on the strength of their social ties to the information source (Granovetter 1973). Tie strength is commonly measured by either the intensity of the relationship (i.e., interaction frequency) between two people or the degree of overlap in their friendship (i.e., common friends). The latter is preferred, especially in online social media platforms where the network structural properties (e.g., triadic closure) are prevalent. Using this measure, extant research has shown that it is often the information transmitted via bridging or weak ties (ties with fewer common friends) between diverse and disconnected groups that allows people to receive novel information (Granovetter 1983, Levin and Cross 2004, Godes and Mayzlin 2009, Shi et al. 2014). This is because nodes developing ties with disconnected groups gain access to a broader array of ideas and opportunities, whereas information tends to be relatively redundant within a group (Granovetter 1973, Burt 1992). For example, when students seek information about which professor’s course to take, the information gained from virtual strangers in online forums weights more than the information from friends (Steffes and Burgee 2009). In sum, ties that connect two individuals who do not share common friends provide more information benefits, as these ties most enhance their access to novel information and resources (Stephen and Toubia 2010).

In our context, from the network structural perspective, when the responding and initiating providers have more common ties before reciprocation, the responding provider’s viewers are more likely to have been aware of the initiating provider indirectly (through their common ties) prior to the reciprocation. The reciprocation can enhance the accessibility and novelty of the initiating provider’s content to a lesser extent with preexisting common ties than without Consequently, with more common ties with the initiating provider, the responding provider’s reciprocation is more likely to result in network redundancy in the social structure through which her consumers can obtain novel information (Reagans and Zuckerman 2008). Triadic closure thus predicts that common ties reduce the benefits of reciprocation for the initiating provider, leading to the following hypothesis:

Hypothesis 1. As the number of common ties between the initiating provider and the responding provider prior to reciprocation increases, the benefit of reciprocation for the initiating provider decreases.

## 2.2. Homophily

In addition to triadic closure, tie formation between two people can be attributed to homophily—that is, people with similar characteristics are more likely to establish social ties (McPherson et al. 2001, Zeng and Wei 2013, Aral and Walker 2014, Gu et al. 2014, Ma et al. 2015, Wang et al. 2018). Homophily is attributable to the selection effect whereby people tend to associate with similar others (Easley and Kleinberg 2010) under the a priori notion that they are more likely to be accepted by self-similar others, whereas heterophilous relationships are more likely to break apart (Rivera et al. 2010). Selection based on similarity may operate at different levels of intentionality. Either the provider may intend to interact with similar others or the implicit social environment may favor opportunities to form ties with similar others (Easley and Kleinberg 2010). For instance, a provider of entertainment videos may prefer to feature other providers of entertainment videos or have more opportunities to discover other providers of entertainment videos. In either case, homophily predicts that providers with similar content are more likely to reciprocate.

Whereas homophilous ties are more likely to reciprocate and cooperate, heterophilous ties reflect both different resources and the likelihood of obtaining new resources (Lin 2008). In other words, homogeneous groups may indeed be more harmonious and exhibit higher network density, but their performance can be limited by the relative redundancy of their members’ perspectives, information, and resources (e.g., Bantel and Jackson 1989, Ancona and Caldwell 1992, Pelled et al. 1999). At the individual level, Gu et al. (2014) find that heterophilous ties generate more information exchange benefits for investors in virtual investment communities. Quantitatively, Lin et al. (2017) show that a 1% increase in the category diversity of the incoming copurchase network of a product is associated with a 0.011% increase in the product’s demand. At the group level, Reagans and Zuckerman (2001) demonstrate that the R&D teams with close contact between individuals of the same organizational tenure are less productive. At the organization level, Maurer and Ebers (2006) find that although cohesion in homogeneous ties is crucial for successful start-ups, only firms with a diverse connection to external partners can access the broader array of information, resources, and opportunities necessary to succeed in the development stage.

These findings show that the value of social capital increases with homophily when the key underlying factor is coordination but decreases when information and resource access are more important to performance outcome. In our context, coordination is the key for reciprocation to occur, but resource access is the key for reciprocation to provide a benefit. From the provider’s perspective, the initiating providers tend to benefit more from the reciprocation of the responding providers who are more different from themselves, as these responding providers can provide the initiators with a diverse incoming network of a different set of consumers, expanding the initiators existing consumer base (Lin et al. 2017). The exposure of the focal provider will be increased, and the demand may increase because of this heightened exposure (Carmi et al. 2017). From the consumers perspective, directed from the responding providers channels, they are more likely to view or subscribe to the initiating providers whose content is different from that of the responding providers. This is because content consumers of the similar responding providers are more likely to have been aware of the initiating provider prior to reciprocation because content similarity increases the likelihood of the initiating provider’s content being discovered by and recommended to these consumers by YouTube’s recommender system (Covington et al. 2016). For reciprocity in particular, Ye et al. (2018) show that reciprocal relationships are more valuable when they enable users to find new products and new exchange partners. Accordingly, homophily negatively moderates the benefit of reciprocation on the initiating provider. We thus propose Hypothesis 2:

Hypothesis 2. As the content similarity between the initiating provider and the responding provider prior to reciprocation increases, the benefit of reciprocation for the initiating provider decreases.

2.3. Interaction of Homophily and Triadic Closure Moreover, homophily and triadic closure may interact with each other in affecting reciprocation. It has been suggested that the preference for similar others will be more important when people face high uncertainty (Kanter 1977, Gakaskiewicz and Shatin 1981, Ibarra 1993). Gu et al. (2014) conclude that investors’ tendency to exhibit homophily is amplified with high uncertainty when stock volatility is high. They argue that uncertainty creates discomfort in the minds of individuals and, accordingly, investors gain exposure to familiar information while avoiding conflicting information (Festinger 1954, Gray et al. 2011). In our context, the higher the number of shared common ties with other providers, the higher the trust (Bapna et al. 2017a) and the lower the level of perceived uncertainty of the responding provider toward the initiating provider. With lower uncertainty, responding providers have a greater tendency toward heterophily when reciprocating. In other words, responding providers would be more likely to reciprocate the ties from the initiating providers with different content when they share more common ties with the initiating providers. As such, content similarity and common ties have a negative interaction effect on the probability of reciprocation.

Homophily also interacts with triadic force in its moderating role on the reciprocation benefit for the initiators. The existing studies have suggested that

relational embeddedness or common ties can attenuate the negative effect of homophily (Coleman 1990, Gnyawali and Madhavan 2001, Makarevich 2016). First, common ties facilitate a faster and more efficient flow of information because of the many interconnections for information collection and distribution (Coleman 1990, Valente 1995). With more common ties, the responding provider’s viewers are more likely to be familiar with the initiating provider’s content. Second, common ties also facilitate trust between the two providers, which is essential for a cohesive alliance and causes them to adhere to more collaborative interactions despite competition (Makarevich 2016). Accordingly, although the two providers are also competing for viewers, responding providers with common ties are more likely to focus on alliance success (e.g., speaking highly of the initiating providers’ content among one’s viewers). From this perspective, common ties increase viewers’ familiarity and the responding providers’ recommendation of the initiator. Both would reduce the viewers’ reliance on content similarity in evaluating the information value of the initiator’s content (Gnyawali and Madhavan 2001). As such, the negative effect of content similarity would be reduced by common ties. Lastly, Rodan and Galunic (2004) show that there is a positive interaction between knowledge heterogeneity and network sparseness for managerial performance. This is because the advantages of structural holes will be diminished if the two providers with brokering ties are similar in content. Similarly, content heterogeneity and a lack of common ties interact positively for reciprocation benefit. Therefore, we propose the following:

Hypothesis 3. Content similarity and common ties have a positive interaction effect on the reciprocation impact for the initiating provider. In other words, the negative effect of content similarity on reciprocation impact becomes less negative when the two providers share more common ties.

## 3. Data and Measures

We collected a panel of data on YouTube video providers over a period of 68 days from May 10 to July 16, 2014. The providers were selected using a snowball sampling method.<sup>2</sup> At the beginning of the data period, our sample consisted of 27,356 providers and 158,923 ties between featured channels. For each sample provider, three sets of information were collected on a daily basis: (1) social ties, including all of the outgoing ties to featured providers and incoming ties from other sample providers; (2) channel information, including the provider’s tenure on YouTube, videos uploaded, video views, and subscribers; and (3) the categories of the provider’s videos. With an average daily increase of 165 featured channels, the total number of featuring ties increased by 7% during our data period. The variable descriptions and sample statistics are shown in Table 1.

According to the triadic closure process for nondirectional networks, common ties increase the likelihood of two people becoming friends themselves because they (1) increase the opportunity for the two to meet and cooperate, and (2) provide a basis for establishing trust (Easley and Kleinberg

Table 1. Variable Descriptions and Sample Statistics

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td colspan="6">For provider i at time t</td></tr><tr><td> $Subs_{it}$ </td><td>Number of i&#x27;s subscribers</td><td>89,285</td><td>303,404</td><td>0</td><td>6.0e+06</td></tr><tr><td> $Views_{it}$ </td><td>Number of views of all of i&#x27;s videos</td><td>2.0e+07</td><td>1.0e+08</td><td>0</td><td>2.5e+09</td></tr><tr><td> $Outdegree_{it}$ </td><td>Number ofi&#x27;s featured providers (outgoing ties)</td><td>15.0</td><td>16.1</td><td>0</td><td>100</td></tr><tr><td> $Indegree_{it}$ </td><td>Number of sample providers featuring i (incoming ties)</td><td>8.5</td><td>15.9</td><td>1</td><td>349</td></tr><tr><td> $Videos_{it}$ </td><td>Number of videos posted by i</td><td>326</td><td>1,054</td><td>0</td><td>22,661</td></tr><tr><td> $Categories_{it}$ </td><td>Number of categories of i&#x27;s posted videos</td><td>3.7</td><td>3.0</td><td>0</td><td>16</td></tr><tr><td> $CAge_{it}$ </td><td>i&#x27;s tenure on YouTube measured in days</td><td>1,336</td><td>875</td><td>4</td><td>3,320</td></tr><tr><td> $OutdegreeSubs_{it}$ </td><td>Number of subscribers toi&#x27;s featured providers</td><td>3.7e+06</td><td>6.3e+06</td><td>0</td><td>8.8e+07</td></tr><tr><td> $OutdegreeViews_{it}$ </td><td>Number of views of all the videos byi&#x27;s featured providers</td><td>8.0e+08</td><td>1.4e+09</td><td>0</td><td>2.0e+10</td></tr><tr><td> $IndegreeSubs_{it}$ </td><td>Number of subscribers to providers featuring i</td><td>994270</td><td>2.6e+06</td><td>0</td><td>5.7e+07</td></tr><tr><td> $IndegreeViews_{it}$ </td><td>Number of views of all videos by providers featuringi</td><td>2.4e+08</td><td>7.5e+08</td><td>0</td><td>2.4e+10</td></tr><tr><td colspan="6">For initiating and responding provider pair i-j at time t</td></tr><tr><td> $FB_{ijt}$ </td><td>1 if j reciprocates by featuring i in return and 0 otherwise</td><td>0.08</td><td>0.27</td><td>0</td><td>1</td></tr><tr><td> $CommonFeaturing_{ijt}$ </td><td>Number of third providers featured by both i and j</td><td>1.1</td><td>3.0</td><td>0</td><td>25</td></tr><tr><td> $IndirectPath_{ijt}$ </td><td>Number of providers featured by j and featuring i</td><td>0.9</td><td>2.1</td><td>0</td><td>22</td></tr><tr><td> $FeaOrder_{ijt}$ </td><td>Rank of j on the list of i&#x27;s featured providers</td><td>9.2</td><td>11.4</td><td>1</td><td>100</td></tr><tr><td> $CommonCategories_{ijt}$ </td><td>Number of common categories between i&#x27;s and j&#x27;s videos</td><td>1.9</td><td>1.8</td><td>0</td><td>14</td></tr></table>

2010). Adapting this definition for directional ties, for provider j to reciprocate i, a common tie should increase the opportunity for j to (1) discover i’s channel and (2) trust i’s content. For a directional triad, a common tie between two providers can take on four formats (Table 2). Because the direction of featuring represents the direction of discovering and trust, among the four types, only IndirectPath increases the chance for j to discover and trust i. We thus use IndirectPath s as the primary measure of common ties.<sup>3</sup>

Content similarity describes the similarity between the two providers’ content. Because YouTube defines 16 categories for videos but not for providers, we measure the content similarity between two providers by their video categories. Because most providers post videos in multiple categories, we use a vector to describe the content category for provider i at time t:

$$
\begin{array}{r} C a t e g o r y _ {i t} = [ C a t e g o r y _ {i t} ^ {1}, C a t e g o r y _ {i t} ^ {2}, \ldots , \ldots , C a t e g o r y _ {i t} ^ {k}, \\ \ldots , \ldots , C a t e g o r y _ {i t} ^ {1 6} ], k = 1, 2 \ldots , 1 6, \end{array}
$$

where Category<sup>k</sup> is the percent of i’s videos in the k th category among all of i’s videos posted by time t. Next, cosine similarity is calculated for content similarity (Manning et al. 2009, Zeng and Wei 2013):

$$
\text { Similarity } _ {i j t} = \frac {\sum_ {k = 1} ^ {1 6} (\text { Category } _ {i t} ^ {k} * \text { Category } _ {j t} ^ {k})}{\sqrt {\sum_ {k = 1} ^ {1 6} (\text { Category } _ {i t} ^ {k}) ^ {2} \sum_ {k = 1} ^ {1 6} (\text { Category } _ {j t} ^ {k}) ^ {2}}}.
$$

Figure 2 presents the distributions of content similarity and common ties across sample provider pairs. Other similarity measures such as dice similarity and Jaccard similarity are widely used to calculate the similarity between tags and resources in social bookmarking systems (Cha 2007, Zadeh and Goel 2013) and are used as robustness checks for cosine similarity. We also use topological overlap as an alternative measure for common ties. Their measurements are detailed in Online Appendix A.

For the reciprocation impact on the initiating provider, we are mostly interested in how a reciprocating tie from the responding provider affects the number of subscribers or views received during each period. Therefore, our main dependent variable is the new subscribers (log-transformed) that the initiating provider i gained in period t, which is denoted as

$$
L o g \Delta S u b _ {i t} = \log (S u b s _ {i t + 1} - S u b s _ {i t} + 1).
$$

Accordingly, the alternative dependent variable, the number of views gained is denoted as

$$
L o g \Delta V i e w _ {i t} = \log (V i e w s _ {i t + 1} - V i e w s _ {i t} + 1).
$$

Both number of subscribers and the number of views can measure the performance of a UGC provider with slight differences. We prefer subscribers over views as the main dependent variable for several reasons. First, the number of views can be inflated by the number of videos the provider has posted, as one viewer can watch multiple videos. In comparison, the number of subscribers more accurately measures the consumer base. Second, subscription better represents the satisfactory outcome of viewing. Consumers’ viewing of content can be exploratory and thus does not necessarily reflect their true preferences, whereas their subscriptions to providers can only be achieved after the match between providers’ content and their preferences is realized. Third, while viewing existing content is a one-time contribution to a provider’s performance, subscription leads to repeat viewings of all future content in the long run.

We conducted several preliminary analyses to understand the data and provide model-free evidence. According to the correlation matrix (Online Appendix B), common ties and content similarity are positively correlated with increased subscribers and viewers. Pre liminary analyses of reciprocation probability show that most initiating providers received reciprocation from the responding providers within three days after initiating ties, and reciprocation rarely occurs beyond two weeks after initiation (Online Appendix C). For reciprocation impact on the initiating provider, we compare the average number of new subscribers and views of the providers who received reciprocation with those who did not receive reciprocation. As demonstrated in Figure 3, the reciprocated initiators have much higher growth in both subscribers and views, suggesting a positive impact of reciprocation on the initiating provider. Figure 3 also shows that the two groups demonstrate very similar time trends in both Log<sup>Δ</sup>Sub and Log<sup>Δ</sup>View. Moreover, at the network level, we find

Table 2. Comparison of Measures for Common Ties in a Directional Network

<table><tr><td>Type</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td rowspan="2">Triadic structure</td><td></td><td></td><td></td><td></td></tr><tr><td>CommonFeaturing</td><td>IndirectPath</td><td>ReversedIndirectPath</td><td>CommonFeatured</td></tr><tr><td>Opportunity for j to discover i</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Basis for j to trust i</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr></table>

Figure 2. Distribution of Content Similarity and Common Ties  
![](/api/attachments/2A2HED32/fulltext/images/58cf11415c935b050b56ae98c2b08a123f430d12f2327de08c397a88fbb7f05a.jpg)

![](/api/attachments/2A2HED32/fulltext/images/507b970c6d638e2e4a2511cca5af9954af90fba8b4a3238c33b84c139ae6dbc4.jpg)  
that tie reciprocation improves the overall status of the providers within the network (Online Appendix D).

## 4. Empirical Model and Estimation Procedure

To examine the impact of reciprocation on the initiating provider, we model the new subscribers gained by the initiating provider i during period t to be determined by a set of observable and unobservable characteristics of the provider:

$$
L o g \Delta S u b _ {i t, F B} = W _ {i j t} \beta_ {F B} + Z _ {i t} \varphi + l _ {t} + c _ {i j, F B} + u _ {i j t, F B}.\tag{1}
$$

In Equation (1), $L o g \Delta S u b _ { i t , F B }$ is conditional on FB, the reciprocation status at time $t , F B = 1$ for provider i that is reciprocated by provider j at time t, and 0 otherwise. $W _ { i j t } = \overline { { [ 1 , X _ { i t } , X _ { j t } , ] } } \overline { { Y _ { i j t } } } ] .$ , where $X _ { i t } = [ L o g S u b _ { i t } , L o g V i e w _ { i t } ,$ $\_ O u t D e g r e e _ { i t } ,$ InDegree<sub>it</sub>, Entropy<sub>it</sub>, Ratio LikesViews<sub>it</sub>, $L o g \Delta V i d e o _ { i t } ]$ is a vector of i’s observable characteristics, including status (measured by subscribers and views), outdegree (outgoing ties to other providers), indegree (incoming ties from other providers), entropy (diversity in the observed categories of $i ^ { \prime } \mathrm { s }$ videos, detailed in Online Appendix A), content quality (measured by the ratio between the log-transformed daily increased video likes and the log-transformed daily increased video views),<sup>4</sup> and recent productivity (the log-transformed number of new videos posted on day $t ) ;$ similarly, $X _ { j t } = [ L o g S u b _ { j t } , L o g V i e w _ { j t } , O \ ' u t D e g r e e _ { j t } ,$ $I n D e g r e e _ { j t } ,$ ,Entropy<sub>jt]</sub> is a vector of j’s observable characteristics, and $\ddot { Y } _ { i j t } = [ S i m i l a r i t y _ { i j t } , C o m m o n T i e _ { i j t } ]$ is a vector of content similarity and common ties between i and j. With $\beta _ { F B ^ { \prime } }$ we allow variables in $W _ { i j t }$ to have different impacts on $L o g \Delta S u b _ { i t }$ for reciprocated and nonreciprocated providers to examine the moderating effects of the key variables on the reciprocation impact. $Z _ { i t }$ is a vector of $i ^ { \prime } \mathrm { s }$ other observable characteristics $( \mathrm { i . e . } ,$ , subscribers and views of $i ^ { \prime } \mathrm { s }$ incoming and outgoing ties) that have the same influence on $L o g \Delta S u b _ { i t }$ for reciprocated and nonreciprocated pairs. $l _ { t }$ is a time-specific effect, $c _ { i j , F B }$ is a pair-reciprocation specific effect, and $u _ { i j t , F B }$ is a pair-time-reciprocation specific random error.

Figure 3. Average Log<sup>Δ</sup>Sub and Log<sup>Δ</sup>View over Time by Provider Groups  
![](/api/attachments/2A2HED32/fulltext/images/9c3edad9227413cba63b60333ec4502a06abe1c32934628584aa98d1228e7022.jpg)

We aim to estimate the moderating roles of content similarity and common ties on the reciprocation impact, the differences between $\beta _ { 0 }$ and $\beta _ { 1 }$ . Ideally, they can be identified by comparing the reciprocated providers with the not-yet-reciprocated providers if the two groups are comparable in terms of similarity and common ties. However, this does not hold be cause of reciprocation tendency toward providers with similar content and more common ties. To address this issue, we explicitly model the responding provider’s reciprocation decision as a discrete choice affected by observable and unobservable characteristics:

$$
F B _ {i j t} = 1 \Big [ W _ {i j t} ^ {\prime} \gamma + \varepsilon_ {i j t} > 0 \Big ],\tag{2}
$$

where $F B _ { i j t } = 1$ if the initiating provider i is reciprocated by the responding provider j at time t and 0 otherwise. $\cup ^ { \prime } { } _ { i j t } = [ 1 , \dot { X ^ { \prime } } { } _ { i t } , X _ { j t } , \dot { Y _ { i j t } } ]$ , where $X ^ { \prime } { } _ { i t } = [ X _ { i t } , L o g V i d e o _ { i t } ] , X _ { j t } ,$ and $Y _ { i j t }$ are the same as in Equation (1). $L o g V i d e o _ { i t }$ is the (log-transformed) accumulative number of videos since initiating providers registered on YouTube at day t, used to control for the influence of the initiating provider’s overall productivity on reciprocation probability.<sup>5</sup> The error term can be decomposed as $\varepsilon _ { i j t } = m _ { i j } + k _ { t } + \epsilon _ { i j t } ,$ , where $m _ { i j }$ is the pair-specific effect, $\mathbf { \nabla } . k _ { t }$ is a time-specific effect, and $\epsilon _ { i j t }$ is a random error. Instead of using fixed effects methods for nonlinear models, which results in incidental parameters and inconsistent estimators (Greene et al. 2002, Arellano and Hahn 2007), we use a binary response correlated random effects model following the Chamberlain– Mundlak approach, such that

![](/api/attachments/2A2HED32/fulltext/images/467fb14e34c1624e135a6535d9104a207ae11ef8a03b8e67f82305bcf2ce9c2c.jpg)  
— reciprocated providers ---- not-reciprocated providers

$$
F B _ {i j t} = 1 \Big [ W _ {i j t} ^ {\prime} \gamma + \overline {{W ^ {\prime}}} _ {i j} \omega + k _ {t} + \epsilon_ {i j t} > 0 \Big ].\tag{3}
$$

Without provider-pair fixed effects, $\begin{array} { r } { \overline { { W ^ { \prime } } } _ { i j } = T ^ { - 1 } \sum _ { t = 1 } ^ { T } W ^ { \prime } { } _ { i j t } } \end{array}$ is the time averages (averaged across the panel) of the covariates (excluding the constant) added as additional explanatory variables to account for heterogeneity and potential correlation between $W ^ { \prime } { } _ { i j t }$ and the original error term $\varepsilon _ { i j t }$ (Mundlak 1978, Murtazashvili and Wooldridge 2016).

Estimating model (1) separately from model (3) will generate biased results because of the endogenous sample selection issue in model (3). Following the switching regression model (Murtazashvili and Wooldridge 2016), we estimate the two models jointly to allow for the correlation of the error terms in both equations. Unlike instrumental variables and propensity score methods, the switching regression model enables us to directly model the selection bias of reciprocated providers to estimate reciprocation impacts. Moreover, we apply the switching regression model directly to the panel data to better utilize the information on time-varying variables. The drawback is that, for identification purposes, we must make several assumptions after undertaking several data-cleaning measures (see Online Appendix E for details). Under these assumptions, the two-stage estimation procedure below produces consistent and asymptotically normal estimators for coefficients, and the standard errors of the second stage are derived with bootstrapping (Murtazashvili and Wooldridge 2016):

: Run a probit regression of $F B _ { i j t }$ on the time <sup>Stage 1</sup>dummies $W _ { i j t } ^ { \prime }$ and $\overline { { W ^ { \prime } } } _ { i j }$ to obtain $k _ { t } , \hat { \gamma }$ , and ωˆ . Calculate the generalized residuals as follows:

$$
\begin{array}{r l} & {\widehat {g r} _ {i j t} = h \Big (F B _ {i j t}, W ^ {\prime} _ {i j t} \widehat {\gamma} + \overline {{W ^ {\prime}}} _ {i j} \widehat {\omega} + \widehat {k} _ {t} \Big)} \\ & {\quad = F B _ {i j t} \lambda \Big (W ^ {\prime} _ {i j t} \widehat {\gamma} + \overline {{W ^ {\prime}}} _ {i j} \widehat {\omega} + \widehat {k} _ {t} \Big)} \\ & {\qquad - \Big (1 - F B _ {i j t} \Big) \lambda \Big (- W ^ {\prime} _ {i j t} \widehat {\gamma} - \overline {{W ^ {\prime}}} _ {i j} \widehat {\omega} - \widehat {k} _ {t} \Big),} \end{array}\tag{4}
$$

where $h ( \cdot )$ is the generalized error function, and $\lambda ( \cdot ) \equiv \phi ( \cdot ) / \Phi ( \cdot )$ is the inverse Mills ratio (Vella and Verbeek 1999, Murtazashvili and Wooldridge 2016).

: Run an OLS estimation of the equation

$$
\begin{array}{r} L o g \Delta S u b _ {i t} = W _ {i j t} \beta_ {0} + F B _ {i j t} W _ {i j t} \delta_ {1} ^ {\prime} \overline {{W}} _ {i j} \rho_ {0} + F B _ {i j t} \overline {{W}} _ {i j} \rho_ {1} \\ + \xi_ {0} \widehat {g r} _ {i j t} + \xi_ {1} F B _ {i j t} \widehat {g r} _ {i j t} + Z _ {i t} \varphi + l _ {t} + \tau_ {i j t}. \end{array}\tag{5}
$$

## 5. Results

## 5.1. Main Results

Table 3 presents the estimation results where the first stage is the probit estimation for reciprocation probability and the second stage is the OLS regression for reciprocation impact on the initiating provider after adjusting for the first-stage residuals. The estimation in column (1) includes time-specific effects. In addition to time-specific effects, estimations in columns (2) and (3) include the entropy of both providers’ video categories (Entropy<sub>i</sub> and Entropy<sub>j</sub>). Moreover, the second-stage estimations in columns (2) and (3) also account for the log-transformed subscribers and viewers of all the other providers featured by the initiating provider $( L o g O u t D e g r e e S u b _ { i t }$ and LogOutDegreeView ) and those featuring the initiating provider (LogIn $D e g r e e S u b _ { i t }$ and $L o g I n D e g r e e V i e w _ { i t } )$ to control for the influence of other ties of the initiator. These estimations use $L o g \Delta S u b _ { i t }$ and $L o g \Delta V i e w _ { i t }$ as dependent variables, respectively. Column (4) includes the interaction effect between common ties and content similarity.

Regarding the reciprocation impact on the initiating provider, our second-stage results consistently yield statistically significant and positive coefficients for $F B _ { i j t }$ throughout the various specifications, demonstrating that the responding provider’s reciprocation is beneficial for the initiator by attracting new views and subscribers. The reciprocation benefit is also economically significant such that the reciprocated initiator can have subscriber growth at approximately 10 times $( = \exp ( 2 . 3 9 7 ) - 1 )$ the growth of the nonreciprocated initiators on average when both content similarity and the number of common ties are zero. The coefficient of $F B _ { i j t } { ^ { * } C o m m o n T i e _ { i j t } }$ is consistently negative and statistically significant, suggesting that the more indirect path ties from the responding provider to the initiating provider there are prior to reciprocation, the less the reciprocation will benefit the initiator. Hypothesis 1 is thus supported. Quantitatively, one additional tie from j to i reduces i’s reciprocation benefits by 12.6% (= 1 <sup>−</sup> exp (<sup>−</sup>0.135)) based on the results of column (2)). When the number of common ties increases by 10, i’s reciprocation benefits reduce by $7 4 . 1 \% ( = 1 - \mathrm { { e x p } ( - 0 . 1 3 5 ^ { * } \bar { 1 } 0 ) ) ; }$ when the number of common ties increases by 30, i’s reciprocation benefits become almost negligible.

The coefficient of $F B _ { i j t } { } ^ { * } S i m i l a r i t y _ { i j t }$ is consistently negative and statistically significant when the dependent variable is $L o g \Delta S u b _ { i t } ,$ , suggesting that the more similar content the two providers produce, the fewer additional subscribers the reciprocation will generate for the initiator. Quantitatively, when $S i m i l a r i t y _ { i j t } = 1 _ { \cdot }$ , i’s reciprocation benefits are only approximately $4 \% ( = \exp ( - 3 . 1 7 5 ) )$ ) of the benefits when

Table 3. Two-Stage Estimation Results

<table><tr><td></td><td colspan="2">(1)</td><td colspan="2">(2)</td><td colspan="2">(3)</td></tr><tr><td>Stage 1: Reciprocation probability</td><td colspan="6"> $FB_{ijt}$ </td></tr><tr><td> $CommonTie_{ijt}$ </td><td colspan="2">0.247 (0.013)***</td><td colspan="2">0.247 (0.013)***</td><td colspan="2">0.290 (0.018)***</td></tr><tr><td> $Similarity_{ijt}$ </td><td colspan="2">0.787 (0.148)***</td><td colspan="2">1.046 (0.172)***</td><td colspan="2">1.153 (0.176)***</td></tr><tr><td> $CommonTie_{ijt} *Similarity_{ijt}$ </td><td colspan="2"></td><td colspan="2"></td><td colspan="2">-0.089 (0.025)***</td></tr><tr><td> $LogSub_{it}$ </td><td colspan="2">0.043 (0.022)+</td><td colspan="2">0.043 (0.022)*</td><td colspan="2">0.043 (0.022)+</td></tr><tr><td> $LogView_{it}$ </td><td colspan="2">0.085 (0.022)***</td><td colspan="2">0.083 (0.022)***</td><td colspan="2">0.082 (0.022)***</td></tr><tr><td> $Ratio\_Likes\_Views_{it}$ </td><td colspan="2">0.001 (0.040)</td><td colspan="2">-0.0005 (0.040)</td><td colspan="2">-0.002 (0.040)</td></tr><tr><td> $Log\Delta Video_{it}$ </td><td colspan="2">-0.036 (0.019)+</td><td colspan="2">-0.037 (0.019)*</td><td colspan="2">-0.035 (0.019)+</td></tr><tr><td> $LogVideo_{it}$ </td><td colspan="2">-0.143 (0.056)**</td><td colspan="2">-0.148 (0.056)**</td><td colspan="2">-0.153 (0.056)**</td></tr><tr><td> $LogSub_{jt}$ </td><td colspan="2">0.013 (0.040)</td><td colspan="2">0.009 (0.040)</td><td colspan="2">0.014 (0.040)</td></tr><tr><td> $LogView_{jt}$ </td><td colspan="2">-0.005 (0.020)</td><td colspan="2">-0.011 (0.021)</td><td colspan="2">-0.011 (0.021)</td></tr><tr><td>Stage 2: Reciprocation impact</td><td> $Log\Delta Sub_{it}$ </td><td> $Log\Delta View_{it}$ </td><td> $Log\Delta Sub_{it}$ </td><td> $Log\Delta View_{it}$ </td><td> $Log\Delta Sub_{it}$ </td><td> $Log\Delta View_{it}$ </td></tr><tr><td> $FB_{ijt}$ </td><td>2.335 (0.242)***</td><td>2.438 (0.478)***</td><td>2.397 (0.225)***</td><td>2.465 (0.427)***</td><td>2.587 (0.240)***</td><td>2.556 (0.402)***</td></tr><tr><td> $FB_{ijt} *CommonTie_{ijt}$ </td><td>-0.159 (0.028)***</td><td>-0.243 (0.058)***</td><td>-0.135 (0.029)***</td><td>-0.211 (0.069)**</td><td>-0.222 (0.038)***</td><td>-0.324 (0.072)***</td></tr><tr><td> $FB_{ijt} *Similarity_{ijt}$ </td><td>-2.728 (0.467)***</td><td>-0.752 (0.818)</td><td>-3.175 (0.468)***</td><td>-1.100 (0.924)</td><td>-3.297 (0.442)***</td><td>-1.336 (0.913)</td></tr><tr><td> $FB_{ijt} *CommonTie_{ijt} *Similarity_{ijt}$ </td><td colspan="2"></td><td colspan="2"></td><td>0.144 (0.056)**</td><td>0.213 (0.094)*</td></tr><tr><td> $FB_{ijt} *LogSub_{it}$ </td><td>0.139 (0.064)*</td><td>0.178 (0.067)**</td><td>0.135 (0.065)*</td><td>0.173 (0.074)*</td><td>0.137 (0.060)*</td><td>0.177 (0.071)*</td></tr><tr><td> $FB_{ijt} *LogView_{it}$ </td><td>0.066 (0.030)*</td><td>0.225 (0.089)*</td><td>0.059 (0.033)+</td><td>0.217 (0.091)*</td><td>0.059 (0.026)*</td><td>0.220 (0.086)*</td></tr><tr><td> $FB_{ijt} *Ratio\_Likes\_Views_{it}$ </td><td>0.235 (0.099)*</td><td>-0.116 (0.121)</td><td>0.237 (0.074)***</td><td>-0.116 (0.139)</td><td>0.239 (0.064)***</td><td>-0.113 (0.135)</td></tr><tr><td> $FB_{ijt} *Log\Delta Video_{it}$ </td><td>0.041 (0.041)</td><td>-0.011 (0.061)</td><td>0.052 (0.040)</td><td>-0.002 (0.070)</td><td>0.049 (0.036)</td><td>-0.007 (0.083)</td></tr><tr><td> $FB_{ijt} *LogSub_{jt}$ </td><td>-0.244 (0.071)***</td><td>-0.401 (0.108)***</td><td>-0.266 (0.054)***</td><td>-0.444 (0.156)**</td><td>-0.280 (0.054)***</td><td>-0.448 (0.142)**</td></tr><tr><td> $FB_{ijt} *LogView_{jt}$ </td><td>0.257 (0.038)***</td><td>0.361 (0.095)***</td><td>0.261 (0.033)***</td><td>0.360 (0.103)***</td><td>0.260 (0.037)***</td><td>0.360 (0.118)**</td></tr><tr><td> $\widehat{gr}_{ijt}$ </td><td>-0.756 (0.064)***</td><td>-0.452 (0.106)***</td><td>-0.817 (0.055)***</td><td>-0.553 (0.077)***</td><td>-0.861 (0.057)***</td><td>-0.607 (0.069)***</td></tr><tr><td> $FB_{ijt} * \widehat{gr}_{ijt}$ </td><td>-0.811 (0.112)***</td><td>-1.057 (0.204)***</td><td>-0.708 (0.111)***</td><td>-0.879 (0.213)***</td><td>-0.679 (0.096)***</td><td>-0.834 (0.216)***</td></tr><tr><td>Stage-2  $R^2$ </td><td>71.3%</td><td>64.4%</td><td>72.3%</td><td>64.7%</td><td>72.3%</td><td>64.8%</td></tr><tr><td>i&#x27;s and j&#x27;s in- and out-degree</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>i&#x27;s in- and out-degree subscribers/viewers</td><td colspan="2">No</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Category entropy of i and j</td><td colspan="2">No</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Time-specific effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Stage-1 log likelihood</td><td colspan="2">-28,249</td><td colspan="2">-28,211</td><td colspan="2">-28,196</td></tr><tr><td>Observations</td><td colspan="2">112,898</td><td colspan="2">112,818</td><td colspan="2">112,818</td></tr><tr><td>Provider pairs</td><td colspan="2">4,478</td><td colspan="2">4,478</td><td colspan="2">4,478</td></tr></table>

Notes. Stage 1 and 2 are probit and OLS regressions, respectively. Stage 2 standard errors are calculated via bootstrap. $\widehat { g r } _ { i j t }$ is the generalized residual from the first-stage probit regression.  
<sup>+</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Similarit $y _ { i j t } = 0 ;$ increasing content similarity by 10% would decrease i’s reciprocation benefits by 27.2% $( = 1 - \exp ( - 3 . 1 7 5 ^ { * } 1 0 \% ) )$ according to column (2). However, the coefficient becomes insignificant when the dependent variable is Log<sup>Δ</sup>View , implying that content similarity between the two providers does not significantly affect the reciprocation benefit in terms of generating additional views for the initiator. Thus, Hypothesis 2 is supported when the reciprocation benefit is measured by additional subscribers and not views. In other words, when reciprocation brings additional consumers from the reciprocating provider to the initiator, homogeneous content provided by the initiator does not negatively affect these consumers from viewing the content, but it does keep a significant portion of the viewers away from subscribing to the initiator.

According to column (4), common ties and content similarity have a significantly positive interaction effect on reciprocation impact, supporting Hypothesis 3. Because both common ties and content similarity negatively affect reciprocation impact, the positive interaction effect suggests that their individual effects on reciprocation attenuate each other. In other words, the negative impact of similarity (common tie) on reciprocation impact decreases as the number of common ties (similarity) increases. Moreover, when two providers have more than 22 common ties prior to reciprocation, content similarity will positively moderate the reciprocation impact, as the overall effect of similarity becomes positive.

Among the other control variables, we find that both coefficients of $F B _ { i j t } { ^ { * } L 0 g S u b } _ { i t }$ and $F B _ { i j t } { ^ { * } L o g } V i e w _ { i t }$ are positive and statistically significant, suggesting that the initiating providers with higher reputation and popularity also benefit more from reciprocation by the responding providers. FB\*Ratio Likes $. V i e w s _ { i t }$ has a consistently positive and statistically significant effect on reciprocation impact when the dependent variable is $L o g \Delta S u b _ { i t } ,$ , suggesting that an initiator who produces high-quality videos will attract more additional subscribers after reciprocation. We also find that $F B _ { i j t } { } ^ { * } L o g V i e w _ { j t }$ has a consistently positive effect on reciprocation impact, benefits consistent with the intuition that a reciprocating provider with more video views the initiator more after reciprocation. After controlling for the reciprocating provider’s views, the responding provider’s subscribers negatively affect the reciprocation benefit. This result is consistent with the influence of the responding provider’s subscribers in that a higher responding provider’s status would lower the initiating provider’s status in comparison.

The first-stage results confirm that homophily and triadic closure of tie formation for nondirectional ties also apply to our directional ties between content providers, as both content similarity and common ties have significant and positive effects on reciprocation probability. Furthermore, content similarity and common ties have a significantly negative interaction effect on reciprocation probability, confirming our prediction that the responding providers with similar content would be less likely to reciprocate when they share more common ties. This result is consistent with Gu et al. (2014), suggesting that reducing uncertainty can be used as a way to counter homophily tendency in tie formation and to encourage more heterophilous ties. Finally, both coefficients for $\widehat { g r } _ { i j t }$ and $\bar { F } B _ { i j t } { } ^ { * } \widehat g \widehat r _ { i j t }$ are significant, suggesting that the two equations are indeed correlated.

## 5.2. Expected Bene<sup>fi</sup>t for the Initiating Provider

Our main results have shown how common ties and content similarity affect reciprocation probability and impact. Next, we integrate their respective influence on probability and impact to understand their overall influence on the expected benefit for the initiator. For initiating provider $i ,$ the expected benefit from responding provider $j ^ { \prime } \mathrm { s }$ reciprocation at time t can be calculated as follows:

$$
\begin{array}{c} E (B e n e f i t _ {i j t}) = \text {Prob} (F B _ {i j t} = 1) \\ \cdot (L o g \Delta S u b _ {i t, F B = 1} - L o g \Delta S u b _ {i t, F B = 0}), \end{array}\tag{6}
$$

where Prob $F B _ { i j t } = 1 )$ is the probability of reciprocation and can be derived directly from the first-stage result, and $L o g \Delta S u b _ { i t , F B = 1 }$ and $\dot { L } o g \Delta S u b _ { i t , F B = 0 }$ can be derived using the second-stage result for different $F B$ outcomes. Because we are interested in the key factors of common ties and content similarity, when examining the impact of each factor or their joint impacts on the expected benefit, we take the sample average for all the other variables, the parameters as estimated in column (2) of Table 3, and $\stackrel { \cdot } { t } = 3 0 . \stackrel { 6 } { \cdot }$ Therefore, only the variable of interest varies, whereas the rest remain invariant in each simulation.

Holding all other variables constant, Figure 4 plots the expected benefit of reciprocation for the initiating provider as common ties (Figure 4(a)), content similarity (Figure 4(b)), and their joint (Figure 4(c)) change. According to Figure 4(a), as common ties increase, the expected benefit for the initiating provider first increases and then decreases, and the expected benefit reaches its maximum when Common $T i e _ { i j } = 1 3$ and becomes negative when Common $T i e _ { i j } \ge 2 9$

Figure 4(b) shows that the expected benefit for the initiating provider also first increases, then decreases, and reaches its maximum when Similari $t y _ { i j } = 0 . 9 . \mathrm { ~ A c } .$ cording to Figure 4(c), the relationship between com mon ties and the expected benefit remains inverted-U shaped for any value of content similarity, and the peak value decreases as similarity increases. From the other perspective, the expected benefit increases as similarity increases when the number of common ties is small, but it decreases as similarity increases when the number of common ties is large. This result suggests that the initiator can expect a higher reciprocation benefit by linking to more similar providers among providers with few common ties and to more different providers among those with many common ties.

Figure 4. The (Joint) Effects of Common Ties and Content Similarity on the Expected Benefit for the Initiating Provider  
(a)  
![](/api/attachments/2A2HED32/fulltext/images/e05cfa30021e919bca2727997cb919dfc254b282e56a308df080e7f5956e44eb.jpg)

(b)  
![](/api/attachments/2A2HED32/fulltext/images/a3ff3ccfea843decb2a2eb53b22c49bdad385d81037a6cbc3423fdfaad13dd33.jpg)

(c)  
![](/api/attachments/2A2HED32/fulltext/images/3ef05818ae74f2b5f08730939727c11cf998db08195efb6fe7242aab9b2b17d7.jpg)

## 5.3. Robustness Checks

In this section, we conduct robustness checks to validate our findings. First, we need to address the issue of multiple responding providers for the same initiating provider among our sample provider pairs. We may not be able to estimate the reciprocation effect of a specific responding provider on the initiating provider accurately if the initiating provider received multiple reciprocations from more than one responding provider during the same period. To address this concern, for the initiating providers with multiple reciprocations on different days, we slice the entire study period into several periods. Only the observations after the previous reciprocation and before the next reciprocation are included when examining the reciprocation effect from a specific responding provider. This ensures that the only reciprocation for the initiating provider in the estimation period is from that responding provider. For the initiating providers with multiple reciprocations on the same day, we take the averages of the independent variables across reciprocating providers and examine the average effects of these reciprocations. The results in column (1) of Table F (Online Appendix F) remain consistent.

Additionally, even though we control for providerpair–specific effects in the estimation, the fact that many ties are initiated or reciprocated by the same provider may also result in correlated reciprocation impacts with the same initiating or responding provider. Ignoring such a correlation in the observations may underestimate the standard errors and overestimate the significance levels of the coefficient estimates (Allison 1995). Therefore, we cluster the standard errors by either the initiating provider or the responding provider in the first stage and the initiating provider in the second stage (Petersen 2009). The results are presented in Online Appendix G. Our findings still hold.

Second, if tie initiation and reciprocation occur on the same day, we are unable to differentiate between the initiating and responding providers. Among our sample, 260 provider pairs (5.46%) reciprocated on the same day as the tie initiation. We excluded these samples in the main analysis for identification purpose. To examine whether excluding these samples leads to biased results, a robustness check is conducted to test whether adding these samples would change our results. For these same-day-reciprocation samples, we artificially differentiate initiating providers from responding providers using three methods: (1) treating higher-status providers as the initiators, (2) treating lower-status providers as the initiators, and (3) randomly assigning one provider in each pair as the initiator. With same-day reciprocations included, our results are qualitatively the same under all three methods (Online Appendix H).

Third, we test the alternative explanation for triadic closure. Although we argue that triadic closure affects reciprocation and reciprocation impact via the influence of common friends, it can be driven by both homophily and common ties. Common ties may be confounded with similarities between the two providers in some extrinsic characteristics other than their content because more similar providers are more likely to be linked, resulting in more common ties. To rule out homophily as the alternative explanation for triadic closure, we conduct a robustness check to examine the presence of other types of closure. As shown in Table $^ { 2 , }$ we may observe other types of closure due to different types of existing ties to other providers. If homophily instead of common friends is the primary mechanism, common featuring (other providers featured by both initiating and responding providers) and reversed indirect paths (other providers featured by the initiating provider and featuring the responding provider) will also lead to network closure. Therefore, we add CommonFeaturing and ReversedIndirectPath<sup>7</sup> to the estimation. We find that CommonFeaturing and ReversedIndirectPath have no significant positive (negative) effect on reciprocation probability (impact), whereas CommonTie measured in IndirectPath still has a significant positive (negative) effect on reciprocation probability (impact), suggesting that common friends rather than homophily are the mechanism for triadic closure (Online Appendix I).

In addition, we examine alternative measures of content similarity, common ties, and reciprocation. Besides cosine similarity, we calculate similarity measures based on dice similarity and Jaccard similarity. As an alternative to the number of common ties, we use topological overlap to capture the influence of the triads. For reciprocation, instead of using a simple binary indicator, we construct reciprocation weightage, $F B _ { - } w e i g h t _ { j i t } ,$ , as in Equation (7), to reflect the relative importance of the initiating provider among all the responding provider’s featured providers:

$$
F B \_ w e i g h t _ {j i t} = F B _ {i j t} * 1 / (\log (F e a O r d e r _ {j i t}) + 1);\tag{7}
$$

$F e a O r d e r _ { j i t }$ is the rank of i on the list of $j ^ { \prime } \mathbf { s }$ featured providers. Higher rank reflects higher reciprocation weightage. With all of the alternative measures, our results remain qualitatively consistent, and all hypotheses are supported (see Online Appendix J for the details).

Finally, we examine whether our results are robust to an alternative model specification. To estimate the switching regression model for reciprocation impact with panel data, the first-stage equation for reciprocation probability is also estimated with panel data, which essentially assumes that the reciprocation decision is made on a daily basis. Instead, we can also consider reciprocation as a one-time decision and use the cross-sectional model specification. In the crosssectional model specification, the dependent variable for the reciprocation impact equation is the new subscribers received within T days after reciprocation (the 14th day since initiation<sup>8</sup>) for reciprocated (nonreciprocated) pairs. The results for T = 7 and 14 are qualitatively similar to our main results. Online Appendix K presents the detailed model specification, estimation, and results.

## 6. Conclusion and Implications

This study examines the moderating roles of triadic closure and homophily on the reciprocation impact for initiating content providers who can leverage linking as a way to invite reciprocation from other providers for collaboration. Without reciprocation, initiating providers unilaterally direct their viewers to the featured providers’ channels, often at their own cost. Therefore, it is important for providers to selectively initiate links to those whose reciprocations are more beneficial. We focus on the influence of homophily and triadic force, the two mechanisms with the most pronounced effects on the formation of social ties (Ruef et al. 2003) and social capital (Rodan and Galunic 2004). Based on homophily and triadic closure, we examine how the impact of reciprocation is affected by the two providers’ content similarity, common ties, and their interaction effect.

We find that whereas content similarity and common ties increase reciprocation probability, they both reduce the reciprocation benefit in terms of the number of subscribers for the initiating providers. Specifically, our results show that one additional common tie shared by the initiating and responding providers reduces the reciprocation benefit by 12.6% on average and that increasing content similarity between two providers by 10% decreases the benefit by 27.2%. We also find a positive interaction effect between content similarity and common ties on the reciprocation benefit for the initiator, reducing the negative individual effects of both factors. Including the effects of content similarity and common ties on reciprocation probability not only controls for the reciprocation bias for estimating the reciprocation impact, but also allows us to examine their impacts on the expected benefit. Holding all other variables at the sample averages, we find that expected benefit first increases and then decreases as common ties or content similarity increase. For the joint effect, content similarity increases the expected benefit when few common ties exist but decreases the expected benefit when there are many common ties between the two providers. The results for the reciprocation benefit in terms of the number of views are similar except that the negative effect of content similarity is statistically insignificant.

Our results have important practical implications. Content providers can leverage collaboration with other providers through social networking to gain strategic advantage. The networking strategy would require providers to target the right partners according to their specific purposes. To maximize the expected benefit, which integrates both reciprocation probability and reciprocation benefit, a provider should link to more content-similar providers among those with few common ties and more content-different providers among those with many common ties. More over, opposite strategies are recommended for providers to generate more reciprocation and to obtain more beneficial reciprocations. For providers aiming for more reciprocations, for example, new providers, awareness can be increased by initiating ties to providers with similar content or more common ties. However, for well-established providers, more subscribers can be gained by reaching out to providers with fewer common ties. Lastly, the providers focusing on advertising revenue and thus attaching more importance to views instead of subscribers can reach out to more similar providers as content similarity increases the likelihood of reciprocations without significantly decreasing reciprocation benefits in terms of views.

For social media platforms, linking among providers as an organic recommendation mechanism can make a content search more effective and increase the overall content views and customer retention on the platform. Leveraging the existing viewers of other providers, networking can be an alternative way for providers to reach viewers, which may prevent many new providers from discontinuing their content contribution. However, the current policy of many platforms to encourage providers to network with similar others is not optimal and oftentimes decreases subscriber growth. In addition to provider similarity, networking recommendations can be improved based on the existing network structure and providers’ strategic purposes. Our findings can be generalized to other social media platforms with provider networks such as Twitter and Flickr. More broadly, our findings are applicable to other business collaboration contexts. For instance, many e-retailers that recommend other retailers’ products by displaying hyperlinks to those retailers or their products on their webpages can make better recommendations based on similarity and on their existing network structure. Alliances among firms, which contribute to one-third of their revenue and still increase by approximately 25% every year (Wilson and Tuttle 2008), can also consider business similarity and their common relationships with third-party firms.

Our paper makes several key contributions to the literature. First, to the best of our knowledge, this paper is among the very few to address the strategic networking issue among content providers. Despite numerous studies on network structure and networking activities, most of them only examine tie formation and network evolution (e.g., Aral and Walker 2014, Shi et al. 2014). A few extend to include the benefit of social networking (e.g., Ansari et al. 2018). Studies on UGC focus more on content contribution or consumption (Butler 2001, Tang et al. 2012, Zeng and Wei 2013). We integrate tie formation and content consumption by studying the effect of newly formed ties between providers on the consumption of their content. While Ansari et al. (2018) show that a firm or brand can benefit from stimulating the connections between its customers, we find that enhancing connections with other firms or brands can attract more customers.

Second, our paper complements the prior literature on peer influence of social ties driven by trust, corporation, and forgiveness (Bapna et al. 2017a, b; Hong et al. 2018). By examining the social capital value of social ties in terms of information benefits, we find that persuasive and informational effects are both moderated by homophily and triadic closure but in opposite directions. Our framework provides an effective way to integrate them to derive the overall effects of homophily and triadic closure.

Lastly, we contribute to the literature on reciprocity by addressing the reciprocation issue among content providers in social media. Whereas the prior studies consider the role of reciprocal relationships in exchanges and transactions (e.g., Berg et al. 1995, Buchan et al. 2002, Ye et al. 2018), we study the factors that influence reciprocal relationships. Our results show that although reciprocation is a social behavior driven by social mechanisms such as homophily and triadic closure, it has a significant economic impact. Unlike previous studies that focus on either homophily (Currarini et al. 2009, Miller et al. 2009, Palla et al. 2012, Sarkar et al. 2012) or triadic closure (Solé et al. 2002, Ispolatov et al. 2005), we examine both mechanisms simultaneously and unveil the interplay between them not only in tie formation but also in the impact of ties. Specifically, confirming that homophily and triadic closure drive tie reciprocation for directional networks, we find that they also moderate the benefit of reciprocation negatively because of reduced information benefits. This finding further highlights the access to information and resources as the most important value for social capital in the context of UGC provider networks.

## 7. Limitations

Our work has a few limitations in terms of data and measures. First, our measure of content similarity does not take into account the fact that certain video categories may represent closer semantic groups than others (Cattuto et al. 2008, Zeng and Wei 2013). For example, the “Comedy” category is more closely related to the “Entertainment” category than to the “Nonprofits and Activism” category. Second, snowball sampling captures all of the outgoing ties from providers in the sample, but not necessarily all of the incoming ties. This limitation is common in studies on directed online social graphs for large social networks (Cha et al. 2009). Third, observing the sample providers for two months limits our ability to further explore the long-term reciprocation impact. Future research can collect data over a longer period to study how reciprocation impact changes over time.

In addition, the endogeneity issue may not be fully addressed for observational studies, and our paper is no exception. Besides using provider fixed effects to control for time-invariant factors, we also control for important time-varying factors that may affect both viewers’ subscriptions and the responding providers reciprocations, including the initiating providers popularity and status prior to reciprocations, their video quality, video productivity, networking activities during the study period, and the influence from other social ties. Other activities conducted by the providers such as coproducing videos or hosting events offline are not captured. Lastly, content similarity (homophily) and common friends (triadic closure) may influence each other. By taking their values prior to reciprocations as given, we do not consider their potential correlation in this study.

## Acknowledgments

The authors thank participants at the 2017 Symposium on Statistical Challenges in Electronic Commerce Research and the research workshop at National Technological University for comments and suggestions. They are especially grateful for the constructive comments from Paul Pavlou (senior edi tor), Gal Oestreicher-Singer (associate editor), and three anonymous reviewers.

## Endnotes

<sup>1</sup> Mayzlin and Yoganarasimhan (2012) found that bloggers link to other blogs to signal to readers their ability to discover content. The signaling effect does not apply to our context because the linking is at the provider level, not the content level.

<sup>2</sup> On the first day of our data period, we began with a known provider as the original node (degree 0), expanded the sample by including the provider’s featured providers (degree 1), and repeated the process by including the newly added providers’ featured providers unti degree 7. For the providers in the first 6 degrees, our network data captured all of their outgoing ties to all YouTube providers, and we captured their incoming ties from all sample providers but not necessarily all YouTube providers.

<sup>3</sup> Because the snowball sampling method collects complete information on both i’s and j’s outgoing ties, if a third provider A has an outgoing tie from either i or j, A will be included in our sample with complete observations on the triadic structure of $i { \mathrm { - } } \mathrm { A } { \mathrm { - } } j .$ Therefore, our data provide complete observations on all types except for CommonFeatured, where both i’s and j’s ties with A are incoming. However, this limitation does not affect our measure of CommonTie<sub>ijt</sub>.

<sup>4</sup> We also use the ratio between daily video likes and daily video views of videos uploaded during the research period to measure content quality, and the results are generally unchanged.

<sup>5</sup> We thank the anonymous reviewer for making this suggestion.

<sup>6</sup> We set t = 30 because it is the middle of our data period. The results are qualitatively similar when we use other days.

<sup>7</sup> To avoid double counting, for CommonFeaturing, we deduct those with indirect path ties (mutual ties between the initiating provider); for ReversedIndirectPath, we deduct those with common features or indirect path ties.

<sup>8</sup> Based on our data set, beyond two weeks after the initiation, reciprocation rarely occurs.

## References

Allison PD (1995) Survival Analysis Using SAS: A Practical Guide (SAS Institute, Cary, NC).

Ancona DG, Caldwell DF (1992) Demography and design: Predictors of new product team performance. Organ. Sci. 3(2):321–341.

Ansari A, Stahl F, Heitmann M, Bremer L (2018) Building a social network for success. J. Marketing Res. 55(3):321–338.

Aral S, Walker D (2014) Tie strength, embeddedness, and social in fluence: A large-scale networked experiment. Management Sci. 60(6):1352–1370.

Arellano M, Hahn J (2007) Understanding bias in nonlinear panel models: Some recent developments. Blundell R, Newey W, Persson T, eds. Advances in Economics and Econometrics—Theory and Applications, Ninth World Congress (Cambridge University Press, Cambridge, UK), 381–409.

Bantel KA, Jackson SE (1989) Top management and innovations in banking: Does the composition of the top team make a differ ence? Strategic Management J. 10(2):107–124.

Bapna R, Gupta A, Rice S, Sundararajan A (2017a) Trust and the strength of ties in online social networks: An exploratory field experiment. Management Inform. Systems Quart. 41(1):115–130.

Bapna R, Qiu L, Rice S (2017b) Repeated interactions vs. social ties: Quantifying the economic value of trust, forgiveness, and reputation using a field experiment. Management Inform. Systems Quart. 41(3):841–866.

Bapna R, Umyarov A (2015) Do your online friends make you pay? A randomized field experiment in online social networks. Management Sci. 61(8):1902–1920.

Berg J, Dickhaut J, McCabe K (1995) Trust, reciprocity and social history. Games Econom. Behav. 10:122–142.

Brown JJ, Reingen PH (1987) Social ties and word-of-mouth referral behavior. J. Consumer Res. 14(3):350–362.

Buchan NR, Croson RTA, Dawes RM (2002) Swift neighbors and persistent strangers: A cross-cultural investigation of trust and reciprocity in social exchange. Am. J. Sociol. 108(1):168–206.

Burt RS (1992) Structural Holes (Harvard University Press, Cam bridge, MA).

Butler BS (2001) Membership size, communication activity, and sustainability: A resource-based model of online social structures. Inform. Systems Res. 12(4):346–362.

Carmi E, Oestreicher-Singer G, Stettner U, Sundararajan A (2017) Is Oprah contagious? The depth of diffusion of demand shocks in a product market. Management Inform. Systems Quart. 41(1): 207–221.

Cattuto C, Benz D, Hotho A, Stumme G (2008) Semantic grounding of tag relatedness in social bookmarking systems. Proc. 7th Internat. Conf. Semantic Web (Springer, Berlin), 615–631.

Cha M, Mislove A, Gummadi KP (2009) A measurement-driven analysis of information propagation in the Flickr social network. Proc. 18th Internat. Conf. World Wide Web (Association fo Computing Machinery, New York), 721–730.

Cha S (2007) Comprehensive survey on distance/similarity measures between probability density functions. Internat. J. Math. Model Methods Appl. Sci. 4(1):300–307.

Coleman J (1990) Foundations of Social Theory (Harvard University Press, Cambridge, MA).

Covington P, Adams J, Sargin E (2016) Deep neural networks for YouTube recommendations. Proc. 10th ACM Conf. Recommende Systems (Association for Computing Machinery, New York), 191–198.

Currarini S, Jackson MO, Pin P (2009) An economic model of friendship: Homophily, minorities, and segregation. Econometrica 77(4):1003–1045

Easley D, Kleinberg J (2010) Networks, Crowds, and Markets: Reasoning about a Highly Connected World (Cambridge University Press, Cambridge, UK).

Emerson RM (1976) Social exchange theory. Annual Rev. Sociol 2:335–362.

Festinger L (1954) A theory of social comparison processes. Human Relations 7(2):117–140.

Fracassi C (2017) Corporate finance policies and social networks Management Sci. 63(8):2420–2438.

Gakaskiewicz J, Shatin D (1981) Leadership and networking among neighborhood human service organizations. Admin. Sci. Quart. 26(3):434–448.

Gaudeul A, Giannetti C (2013) The role of reciprocation in social network formation, with an application to LiveJournal. Soc. Networks 35(3):317–330.

Gnyawali DR, Madhavan R (2001) Cooperative networks and competitive dynamics: A structural embeddedness perspec tive. Acad. Management Rev. 26(3):431–445.

Godes D, Mayzlin D (2009) Firm-created word-of-mouth commu nication: Evidence from a field test. Marketing Sci. 28(4):721–739.

Goes PB, Lin M, Yeung CA (2014) Popularity effect in user-generated content: Evidence from online product reviews. Inform. System Res. 25(2):222–238

Granovetter MS (1973) The strength of weak ties. Am. J. Sociol. 78(6): 1360–1380.

Granovetter MS (1983) The strength of weak ties: A network theory revisited. Sociol. Theory 1:201–233.

Gray HM, Ishii K, Ambady N (2011) Misery loves company: When sadness increases the desire for social connectedness. Personalit Soc. Psych. Bull. 37(11):1438–1448.

Greene W, Han C, Schmidt P (2002) The bias of the fixed effects estimator in nonlinear models. Unpublished manuscript, Stern School of Business, New York University, New York.

Gu B, Konana P, Raghunathan R, Chen HM (2014) The allure of homophily in social media: Evidence from investor responses on virtual communities. Inform. Systems Res. 25(3):604–617.

Hallinan MT (1978) The process of friendship formation. Soc. Net works 1(2):193–210.

Hong Y, Hu Y, Burtch G (2018) Embeddedness, pro-sociality, and social influence: Evidence from online crowdfunding. Manage ment Inform. Systems Quart. 42(4):1211–1224.

Ibarra H (1993) Personal networks of women and minorities in management: A conceptual framework. Acad. Management Rev. 18:56–87.

Ispolatov I, Krapivsky PL, Yuryev A (2005) Duplication-divergence model of protein interaction network. Phys. Rev. E Statist. Nonlinear Soft Matter Phys. 71(6, part 1):061911.

Jabr W, Zheng Z (2014) Know yourself and know your enemy: An analysis of firm recommendations and consumer reviews in a competitive environment. Management Inform. Systems Quart. 38(3):635–654.

Kanter RM (1977) Men and Women of the Corporation: New Edition (Basic Books, New York).

Katona Z, Sarvary M (2008) Network formation and the structure of the commercial World Wide Web. Marketing Sci. 27(5):764–778.

Kossinets G, Watts DJ (2006) Empirical analysis of an evolving social network. Science 311(57):88–90.

Kossinets G, Watts DJ (2009) Origins of homophily in an evolving social network. Amer. J. Sociol. 115:405–450.

Levin D, Cross R (2004) The strength of weak ties you can trust: The mediating role of trust in effective knowledge transfer. Management Sci. 50(11):1477–1490.

Lin N (2001) Social Capital: A Theory of Social Structure and Action (Cambridge University Press, Cambridge, UK).

Lin N (2008) A network theory of social capital. Castiglione D, van Deth JW, Wolleb G, eds. The Handbook of Social Capital (Oxford University Press, Oxford, UK), 50–69.

Lin Z, Goh KY, Heng CS (2017) The demand effects of product recommendation networks: An empirical analysis of network diversity and stability. Management Inform. Systems Quart. 41(2):397–426.

Louch H (2000) Personal network integration: Transitivity and homophily in strong-tie relations. Soc. Networks 22(1):45–64

Ma L (2010) A dynamic competitive analysis of content production and link formation of Internet content developers. Working paper, Carnegie Mellon University, Pittsburgh.

Ma L, Krishnan R, Montgomery AL (2015) Latent homophily or social influence? An empirical analysis of purchase within a social network. Management Sci. 61(2):454–473.

Makarevich A (2017) Extra- and intra-alliance behavioral moderators of success in alliances with competitors. Acad. Management Proc., ePub ahead of print November 30, https://doi.org/10.5465/ ambpp.2016.61. 2016(1).

Manning CD, Raghavan P, Schütze H (2009) Introduction to Information Retrieval (Cambridge University Press, Cambridge, UK).

Maurer I, Ebers M (2006) Dynamics of social capital and their performance implications: Lessons from biotechnology start-ups. Admin. Sci. Quart. 51(2):262–292.

Mayzlin D, Yoganarasimhan H (2012) Link to success: How blogs build an audience by promoting rivals. Management Sci. 58(9): 1651–1668.

McPherson M, Smith-Lovin L, Cook JM (2001) Birds of a feather: Homophily in social networks. Annual Rev. Sociol. 27(1):415–444.

Miller KT, Griffiths TL, Jordan MI (2009) Nonparametric latent feature models for link prediction. Adv. Neural Inform. Process. Systems 22:1276–1284.

Mundlak Y (1978) On the pooling of time series and cross-section data. Econometrica 46(1):69–85.

Murtazashvili I, Wooldridge JM (2016) A control function approach to estimating switching regression models with endogenous explanatory variables and endogenous switching. J. Econometrics 190(2):252–266.

Palla K, Knowles DA, Ghahramani Z (2012) An infinite latent attribute model for network data. Proc. 29th Internat. Conf. Machine Learn. (Association for Computing Machinery, New York).

Pelled LH, Eisenhardt KM, Xin KR (1999) Exploring the black box: An analysis of work group diversity, conflict, and performance. Admin. Sci. Quart. 44(1):1–28.

Peng J, Agarwal A, Hosanagar K, Iyengar R (2018) Network overlap and content sharing on social media platforms. J. Marketing Res. 55(4):571–585.

Petersen MA (2009) Estimating standard errors in finance panel data sets: Comparing approaches. Rev. Financial Stud. 22(1):435–480.

Powell WW, Kogut K, Smith-Doerr L (1996) Interorganizational collaboration and the locus of innovation: Networks of learning in biotechnology. Admin. Sci. Quart. 41(1):116–145.

Reagans R, Zuckerman EW (2001) Networks, diversity, and pro ductivity: The social capital of corporate R&D teams. Organ. Sci. 12(4):502–517.

Reagans R, Zuckerman EW (2008) Why knowledge does not equal power: The network redundancy trade-off. Indust. Corporate Change 17(5):903–944.

Rivera MT, Soderstrom S, Uzzi B (2010) Dynamics of dyads in social networks: Assortative, relational, and proximity mechanisms. Rev. Sociol. 36(1):91–115.

Rodan S, Galunic C (2004) More than network structure: How knowledge heterogeneity influences managerial performance and innovativeness. Strategic Management J. 25(6):541–556.

Ruef M, Aldrich HE, Carter NM (2003) The structure of organizational founding teams: Homophily, strong ties, and isolation among U.S. entrepreneurs. Amer. Sociol. Rev. 68(2):195–222

Runger G, Wasserman S (1979) Longitudinal analysis of friendship networks. Soc. Networks 2(2):143–154.

Rusbult CE, Buunk BP (1993) Commitment processes in close relationships: An interdependence analysis. J. Soc. Personal Re lationships 10(2):175–204.

Sarkar P, Chakrabarti D, Jordan MI (2012) Nonparametric link prediction in dynamic networks. Proc. 29th Internat. Conf. Machine Learn. (Association for Computing Machinery, New York).

Sheldon KM, Abad N, Hinsch C (2011) A two-process view of Facebook use and relatedness need-satisfaction: Disconnection drives use, and connection rewards it. J. Personality Soc. Psych. 100(4):766–775.

Shi Z, Rui H, Whinston AB (2014) Content sharing in a social broadcasting environment: Evidence from Twitter. Management Inform. Systems Quart. 38(1):123–142.

Solé RV, Pastor-Satorras R, Smith E, Kepler TB (2002) A model of large-scale proteome evolution. Adv. Complex Systems 5(1):43–54.

Steffes EM, Burgee LE (2009) Social ties and online word of mouth. Internet Res. 19(1):42–59.

Stephen AT, Toubia O (2010) Deriving value from social commerce networks. J. Marketing Res. 47(2):215–228

Susarla A, Oh J, Tan Y (2012) Social networks and the diffusion of user-generated content: Evidence from YouTube. Inform. Systems Res. 23(1):23–41.

Tang Q, Gu B, Whinston AB (2012) Content contribution for revenue sharing and reputation in social media: A dynamic structural model. J. Management Inform. Systems 29(2):41–76.

Uzzi B (1997) Social structure and competition in interfirm networks: The paradox of embeddedness. Admin. Sci. Quart. 42(1):35–67.

Valente T (1995) Network Models of the Diffusion of Innovation (Hampton, Cresskill, NJ)

Vella F, Verbeek M (1999) Two-step estimation of panel data models with censored endogenous variables and selection bias. J. Econometrics 90(2):239–263.

Wang A, Zhang M, Horn I (2018) Socially nudged: A quasiexperimental study of friends’ social influence in online product ratings. Inform. Systems Res. 29(3):641–655.

Wilson S, Tuttle D (2008) The Promise and Pitfalls of Alliances (Deloitte University Press, Westlake, TX).

Ye S, Viswanathan S, Hann IH (2018) The value of reciprocity in online barter markets: An empirical investigation. Management Inform. Systems Quart. 42(2):521–549.

Zadeh RB, Goel A (2013) Dimension independent similarity com putation. J. Machine Learn. Res. 14(1):1605–1626.

Zeng X, Wei L (2013) Social ties and user content generation: Evidence from Flickr. Inform. Systems Res. 24(1):71–87.

Zhang B, Pavlou P, Krishnan R (2018) On direct vs. indirect peer influence in large social networks. Inform. Systems Res. 29(2): 292-314.
