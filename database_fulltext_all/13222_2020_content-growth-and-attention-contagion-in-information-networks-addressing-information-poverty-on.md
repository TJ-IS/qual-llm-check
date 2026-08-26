---
otero_id: 13222
otero_key: "8MD9CQBM"
title: "Content Growth and Attention Contagion in Information Networks: Addressing Information Poverty on Wikipedia"
authors: "Kai Zhu; Dylan Walker; Lev Muchnik"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0899"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.238.7.40] On: 13 June 2020, At: 06:08 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/8MD9CQBM/fulltext/images/a2b23d1100fb9058387a6ec8a20df3479f3941956f6401bfcce15875f88cd0da.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Content Growth and Attention Contagion in Information Networks: Addressing Information Poverty on Wikipedia

Kai Zhu, Dylan Walker, Lev Muchnik

To cite this article: Kai Zhu, Dylan Walker, Lev Muchnik (2020) Content Growth and Attention Contagion in Information Networks: Addressing Information Poverty on Wikipedia. Information Systems Research

Published online in Articles in Advance 10 Jun 2020

https://doi.org/10.1287/isre.2019.0899

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Content Growth and Attention Contagion in Information Networks: Addressing Information Poverty on Wikipedia

Kai Zhu,<sup>a</sup> Dylan Walker,<sup>a</sup> Lev Muchnik<sup>b</sup>

<sup>a</sup> Desautels Faculty of Management, McGill University, Montreal, Quebec H3A 1G5, Canada; <sup>b</sup> Jerusalem School of Business Administration, The Hebrew University of Jerusalem, 91905 Jerusalem, Israel

Contact: kaizhu@bu.edu (KZ); dtwalker@bu.edu, https://orcid.org/0000-0002-1354-4969 (DW); lev.muchnik@mail.huji.ac.il (LM)

Received: November 7, 2018 Revised: July 19, 2019 Accepted: September 23, 2019 Published Online in Articles in Advance: June 10, 2020

https://doi.org/10.1287/isre.2019.089

Copyright: © 2020 INFORMS

Abstract. Open collaboration platforms have fundamentally changed the way that knowledge is produced, disseminated, and consumed. In these systems, contributions arise organically with little to no central governance. Although such decentralization provides many benefits, a lack of broad oversight and coordination can leave questions of information poverty and skewness to the mercy of the system’s natural dynamics. Unfortunately, we still lack a basic understanding of the dynamics at play in these systems and specifically, how contribution and attention interact and propagate through in formation networks. We leverage a large-scale natural experiment to study how exogenous content contributions to Wikipedia articles affect the attention that they attract and how that attention spills over to other articles in the network. Results reveal that exogenously added content leads to significant, substantial, and long-term increases in both content consumption and subsequent contributions. Furthermore, we find significant attention spillover to downstream hyperlinked articles. Through both analytical estimation and empirically informed simulation, we evaluate policies to harness this attention contagion to address the problem of information poverty and skewness. We find that harnessing attention contagion can lead to as much as a twofold increase in the total attention flow t clusters of disadvantaged articles. Our findings have important policy implications for open collaboration platforms and information networks.

History: Anandasivam Gopal, Senior Editor; Maytal Saar-Tsechansky, Associate Editor. Funding: L. Muchnik acknowledges financial support from the Israel Science Foundation [Grant 1777/ 17]. D. Walker acknowledges the NVIDIA Corporation for their donation of GPU hardware used in this research. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0899.

Keywords: user-generated content • open collaboration platform • information consumption • attention contagion • spillover effect

## 1. Introduction

Wikipedia is one of the most successful examples of open collaboration platforms, serving millions of information seekers daily. It is both a repository of free knowledge and the most visited educational resource on the planet.<sup>1</sup> By the end of 2017, a mere 16 years since its inception, the English language Wikipedia alone contained over 5.5 million articles and a total of over 3.1 billion words, over 60 times as many as the next largest English language encyclopedia, Encyclopedia Britannica.<sup>2</sup> It consists of millions of articles written by a global network of volunteers and is accessible to anyone with an internet connection. Wikipedia represents a new generation of internet-based collaborative tools that strive to be open, accessible, and egalitarian.

However, Wikipedia’s reliance on open and distributed collaboration as well as community governance is not without its problems. As noted by Wikipedia itself, volunteers do not always contribute to the content that people need the most.<sup>3</sup> Large proportions of articles are incomplete or insufficiently supported with references.<sup>4</sup> Because of Wikipedia’s open and distributed production model, it is difficult to direct contributors’ attention to articles that most need improvement. Hence, not only are these articles incomplete, but they are likely to remain so. As a consequence, the coverage and depth of knowledge in Wikipedia articles are uneven. Although well-developed articles are considerably longer than their analogues in Encyclopedia Britannica, many articles are still of poor quality, and they are on average half as long as their professionally edited analogues.<sup>5</sup> Importantly, coverage also seems to be uneven across both geographical areas and knowledge domains (Halavais and Lackaff 2008, Kittur et al. 2009, Graham et al. 2014). For example, Wikipedia has strong coverage of military history and political events in America, but articles on biology, law, medicine, and information on developing countries are often absent or underdeveloped.<sup>6</sup>

Left unchecked, the societal implications of uneven coverage are deeply troubling. Despite the openness of Wikipedia, there are growing concerns that geographical areas and knowledge domains that are left out or underrepresented will remain so or become even further underrepresented relative to the growing knowledge base in a kind of poor-get-poorer phenomenon. Geographical informational skews can act to further limit our understandings of, attention to, and interactions with impoverished areas in terms of regional economic, social, political, and cultural concerns (Norris 2001, Yu 2006, Forman et al. 2012, Graham et al. 2014). Knowledge domain information skews can compound insularity, lead to domainbased siloing, and push information seekers toward alternative, domain-specific information platforms that are less open and are not free. Informational skew may reinforce or even compound existing biases in worldviews and exacerbate information poverty. Existing research has shown that information (un-)availability has a surprisingly strong impact on real-world outcomes in financial markets, scientific advancement, and the tourist industry (Xu and Zhang 2013, Xiaoquan and Lihong 2015, Hinnosaar et al. 2017, Thompson and Hanley 2017). These studies further emphasize the salience of the skewed coverage problem in Wikipedia. Importantly, although we focus on Wikipedia, concerns of uneven coverage exist in a variety of platforms that facilitate collaborative content production, including open source software (e.g., GitHub), knowledge markets (e.g., Stack Overflow or Quora), and product reviews (e.g., Amazon or Steam).

It is unclear whether Wikipedia’s uneven coverage is driven by selection effects on the part of Wikipedia editors owing to their intrinsic interests (Kuznetsov 2006, Nov 2007), natural emerging trends and exogenous factors (Kampf et al.¨ 2012, 2015; Keegan et al. 2013), or a systematic tendency for well-developed articles to continue to receive more attention via the “rich-get-richer” dynamic (Barabasi and Albert´ 1999, Aaltonen and Seiler 2016). Most existing work on knowledge contribution behavior on Wikipedia has focused primarily on the motivation of its editors (Harhoff et al. 2003, Nov 2007, Zhang and Zhu 2011, Lampe et al. 2012, Zhu et al. 2013, Gallus 2017). However, it is critical that we understand the factors that govern the evolution and lifecycle of articles, which are central to the dynamics of Wikipedia as a system. Such factors are also likely important determinants of uneven coverage. Unfortunately, our understanding of how open collaboration platforms evolve and attract attention is still very limited.

There are three streams of research in the literature that are relevant to our study. The first stream of research emphasizes the dynamic coevolution of knowledge consumption and knowledge production. The open collaboration model allows consumers of knowledge to react to existing content and potentially, also become contributors. However, how do production and con sumption of knowledge interact in this complex dynamic system (Wilkinson and Huberman 2008, Kampf¨ et al. 2012)? Aaltonen and Seiler (2016) find that longer Wikipedia articles tend to receive more editing in the future. Kummer (2019) studied how attention shocks arising from natural disasters affect contributions. Kane and Ransbotham (2016) investigate the feedback loop between consumption and contribution of articles in WikiProject Medicine and find that the state of content moderates this feedback loop. It is noteworthy that they argue that this feedback loop in open collaboration platforms has been underresearched and that a deeper understanding is warranted

The second stream of research emphasizes the network perspective by recognizing that, similar to the web as a whole, Wikipedia is an information network of hyperlinked articles. This has important implications: at least some of the traffic (attention) arriving at a particular article flows outward along links to other downstream articles. The importance of this network perspective derives from a long tradition of relating a node’s relative importance to its network properties—an assumption that is implicit to the wellknown PageRank algorithm. The overall exposure of an article in Wikipedia is determined by the various ways that an information seeker can arrive at it via both external (e.g., search engines) and internal sources (upstream Wikipedia articles). Previous research has shown that the network position of an article is correlated with its content consumption and production (Kane 2009, Ransbotham et al. 2012, Kummer et al. 2016). Moreover, the structural embeddedness of an article in the content-contributor network is positively related to its viewership and information quality (Ransbotham et al. 2012, Kane and Ransbotham 2016). Beyond information networks, Lin et al. (2017) examined a product recommendation network and found that both network diversity and stability are significantly associated with product demand. These findings suggest that articles that are disadvantaged in terms of network position may receive less attention, further limiting their future evolution.

The third stream of research focuses on attention flow or spillover in information networks and policies to optimally leverage spillover. West and Leskovec (2012) used an experimental game to study the dynamics of attention flow in Wikipedia through the lens of goal-oriented search. Kummer (2014) studied spillovers from articles that are featured on the home page of German Wikipedia. Wu and Huberman (2007) study the dynamics of attention to articles on the news aggregator Digg.com and show how attention to articles decays with their novelty. Several works have focused on how content and particularly, perception of its importance can drive attention. Salganik et al. (2006) conducted a series of randomized online experiments to determine the impact of music track ranking on consumption. Muchnik et al. (2013a) demonstrated that perceived popularity of comments not only attracts attention and additional votes but can lead to herding phenomena, where “likes” beget additional “likes.” Carmi et al. (2017) carried this idea further and studied how demand shocks generate not only attention but also, attention spillover in the product recommendation networks of Amazon.com, yielding substantial benefits to downstream recommended products. Finally, Aral et al. (2013) studied seeding strategies for policies that leverage spillover in the context of social networks. These studies suggest that attention spillover has a significant impact on real-world outcomes and that policies that leverage spillover can be beneficial.

Although all three streams of research have enriched our understanding of knowledge production and consumption in information networks, much of the work on open collaboration platforms, like Wikipedia, relies on endogenous observational data, making it difficult to draw valid causal conclusions. In addition, existing work has focused only on the local direct effect of attention spillover. It has not addressed how heterogeneous characteristics of articles moderate spillover. Additionally, it has not considered the systemic effect of spillover and its broader policy implications.

Yet, a rigorous understanding of the dynamics at play in the Wikipedia network and collaborative information systems in general is indispensable for understanding how information evolves in these systems. Such an understanding is vital to the mission of global empowerment through open knowledge production and dissemination. Moreover, it is an important precursor to the development of sound policies, such as incentivizing contributions to achieve more robust coverage.<sup>7</sup> Randomized, controlled experiments are the gold standard for causal inference, but they are difficult to conduct on platforms like Wikipedia. Apart from the technical challenges and ethical concerns associated with experiments in this context, the continued survival and operations of these platforms depend completely on the community of contributors, who are highly sensitive to sudden and unvetted policy changes. However, natural experiments that create exogenous variation in otherwise endogenous relationships can also permit valid causal inference.

In this study, we leverage a natural experiment to examine how exogenous content contributions to a Wikipedia article affect future activities surrounding the article in terms of both pageview dynamics and editing behavior. More interestingly, we examine how the attention that an article attracts can spill over to other articles that it links to and hence, further propagate through the network. Furthermore, we consider the broader policy implications of spillover. We conduct policy simulations to understand how spillovers concentrated in the clusters of the network, which we term attention contagion, could impact the evolution of Wikipedia as a system and how it could be harnessed and incorporated into policies to address impoverished regions in information networks.

The goal of the policy simulation is to integrate our findings into an empirically calibrated attention diffusion model and guide policy decisions through the analysis of counterfactuals. Although the platform can answer some policy questions through analysis of observational data and through experimentation, many relevant counterfactuals for policy recommendation are not directly recoverable from direct estimates. They may be too costly or even impossible to test. In our context, interpreting the spillover effect of individual articles on the whole system is not straightforward. In particular, the effect of spillovers might be amplified when editorial efforts are directed at a group of interconnected articles. The key idea behind the policy simulation approach is that reduced form analysis is used to estimate parameters of a model of the system so that the model can be used to extrapolate findings to more complex or more interesting policies at the cost of imposing additional model assumptions (Taylor and Eckles 2018).

Our study provides three major contributions. First, we confirm and obtain causal estimates of the feedback loop between contribution and attention. We find that contribution drives sustained increase in future atten tion (12% on average, with stronger impact for more significant contributions) and future contributions (3.6 more edits and two more unique editors over a sixmonth period). Second, we determine the article and network characteristics that most amplify spillover or attention contagion. We find that spillovers have the most impact (as much as 22%) for less popular articles that are hyperlinked from focal articles through newly created links. Third, we provide insights from comparisons of policies to address information-impoverished regions of the network based on analytic derivation and empirically calibrated simulations. We demonstrate that a policy designed to leverage attention contagion can yield substantial increases in attention (as much as twofold) to impoverished regions of information networks. These results are directly relevant to concerns of societal equity and have managerial importance for collaborative information platforms.

## 2. Natural Experiment and Data

Since 2010, the Wikipedia Education Foundation has been collaborating with university course instructors to encourage students in the United States and Canada to expand and improve Wikipedia articles through course assignments. The mission of this endeavor is to cultivate students’ skills, such as media literacy, writing, and critical thinking, while leveraging student effort to fill content gaps on Wikipedia. Since its launch, university instructors participating in the program have guided their students to add content to approximately 46,000 course-related articles on Wikipedia. About 35,000 students have contributed more than 35 million words to Wikipedia, equivalent to 22 volumes of a printed encyclopedia. These student-edited articles have collectively received 282 million views by the end of 2017.<sup>8</sup>

In this study, we leverage the exogenous content contributions that result from this campaign to enrich our understanding of the dynamics in open collaboration platforms. The identification derives from the assumption that the content contributions by students are exogenous to the natural evolution of the articles and would not have occurred during the same time period in the absence of the Wiki Education campaign. This is likely to hold for two reasons. First, many of the treated articles pertain to topics that do not naturally relate to current events (e.g., detailed topics in fundamental sciences, such as properties of molecules, etc.). Second, the timing of contribution is exogenous. The content addition occurs during a fixed time period that corresponds to an arbitrary class period—that is to say, that the contribution would not have occurred during the same time period in the absence of the assignment. We seek to learn three things from this natural experiment: first, whether efforts that focus on developing underdeveloped pages can lead to longterm, sustained impact; second and more generally, how contribution and attention dynamically interact and how this interaction depends on article attributes; and third, whether and to what extent attention propagates through the information network (that is, the phenomenon of attention contagion). Finally, we seek to combine insights in order to synthesize and assess policies that address information poverty and skewness.

For this study, we collected all of the articles that received content contribution from students through this campaign in the year of 2016.<sup>9</sup> For each article, we retrieved its title, URL, the time period of the course (i.e., the shock period), and the number of characters added to the article by the assigned student from the website of Wiki Education Dashboard.<sup>10</sup> In our analysis, we retain only articles that existed prior to the campaign (excluding new articles created by students) and those that received substantive contributions (of at least 500 added characters during the shock period). This leaves us with 3,296 unique treated articles in the sample.

To assess the impact of the content shock, we consider the number of pageviews of an article, a widely used measure of information consumption. In addition, we parse the complete revision history of each article to obtain the time series of edits and authorship (i.e., the number of unique editors who worked on the ar ticle over time). Both the pageviews and revisions are collected through the public Application Programming Interface (API) developed and maintained by the Wikimedia Foundation.<sup>11</sup>

## 2.1. Matching and Control Group

Rates of Wikipedia content creation and consumption are subject to seasonality and other temporal patterns. A simple comparison of quantities of interest (for example, pageviews and revisions) before and after the content shock may, therefore, be misleading. Observed changes can be attributed to alteration of the page content but also, to naturally occurring trends. Statistical modeling techniques alone are often insufficient to fully account for seasonality and other complex temporal patterns of article activity. We address this issue by constructing a sample of treated and control articles matched across multiple attributes. The control group is used to identify the average outcomes corresponding to the counterfactual state that would have occurred for articles in the treatment group had they not received the content contribution during the shock period.

The control group is chosen via the following procedure. First, we pick candidates for the control group by choosing a random sample of 100,000 Wikipedi articles that did not receive content contribution from students. Second, we define the hypothetical shock period for each control article by randomly sampling from the pool of shock periods of treated articles and measure the preshock article characteristics for contro articles. Third, we use coarsened exact matching (CEM) (Iacus et al. 2012) based on each article’s preshock characteristics of tenure, size, and popularity (calculated based on average historical pageviews) to obtain a matched sample by pruning articles that have no close match in the treated and control groups We opt for a k-to-k matching solution (i.e., an equal number of treated and control units), which is accomplished by pruning observations from a CEM solution within each stratum until the solution contains the same number of treated and control units in all strata. Pruning occurs within a stratum through nearest neighbor selection using a Euclidean distance function.

Matching is a frequently used technique for drawing causal conclusions from observational data based on the assumption of selection on observables (Rosenbaum and Rubin 1983, Ho et al. 2007). It emulates a randomized experiment after the data have been collected by constructing a balanced data set in which samples in the control group are similar to the samples in the treated set in observed characteristics. We confirm that the constructed control group closely mirrors the treatment group in seasonality and natural time trends. This can be verified in the model-free plots of pageviews over time in Section 2.3 and by comparing article attributes in each group as displayed in Table 1. The averages of all three covariates are very close across groups, and t-tests fails to reject the null hypothesis that they have the same mean value. In addition, this between-group panel research design lends itself neatly to a standard difference-in-difference estimation of the effect of content contribution.

Table 1. Balanced Check for Matched Sample

<table><tr><td></td><td>Size (characters)</td><td>Popularity (weekly pageviews)</td><td>Tenure (weeks)</td></tr><tr><td>Control</td><td>16,228</td><td>1,575</td><td>506</td></tr><tr><td>Treatment</td><td>16,255</td><td>1,574</td><td>506</td></tr><tr><td>t-test (p-value)</td><td>0.70</td><td>0.93</td><td>0.51</td></tr></table>

Notes. This table illustrates the quality of our matching procedure. It compares preshock characteristics of articles in the matched groups; t-tests indicate that we cannot reject the null hypothesis that articles in treatment and control groups have the same mean across all three characteristics.

The above procedure yields 2,766 pairs of matched treated and control articles. For each article, we construct a panel of weekly pageviews from 26 weeks before the shock to 26 weeks after (excluding the shock period itself). Our final sample consists of a balanced panel of 52 periods for 5,532 articles or 287,664 observations at the article-week level. Our results are robust to other matching procedure choices. For example, we evaluated an alternative matching procedure that incorporates matching on article topic and find that the direct effect results are qualitatively similar with only small changes in the magnitude of effect sizes. In addition, we also demonstrate that our results are robust to matching based on network characteristics of articles (see the online appendix for further details).

## 2.2. Links and Hyperlink Articles

Because we are also interested in attention spillovers from treated articles to downstream hyperlinked articles, we parse content revisions to retrieve the outgoing hyperlinks from focal articles. Following the links, we retrieve all articles linked to by treated and control articles. There are millions of such hyperlinked articles. To avoid confounds that may arise from multiple exposures to the treatment, we retain only hyperlinked articles that are linked to from one and only one treated article (Walker and Muchnik 2014). For parity, we treat articles downstream of control articles in the same manner. This allows us to obtain a clean estimate of the spillover effect from each link. This procedure yields 131,974 hyperlinked articles that are downstream from directly treated articles. The spillover treated and spillover control articles constitute our sample for analyzing the spillover effect of the content contribution. This is illustrated in Figure 1.

## 2.3. Model-free Evidence

In this section, we present model-free evidence regarding the direct and spillover impact of the content shock in terms of both pageview dynamics and editing behavior. A model-free examination of the evidence can reveal important effects while avoiding modeling assumptions.

2.3.1. Pageviews Dynamic. Because articles are highly heterogeneous, they experienced a large variance in activities (such as pageviews) even prior to treatment, a phenomenon that is typical for complex social systems (Muchnik et al. 2013b). To compensate for large baseline variation, we scaled pageviews for each article relative to its own preshock popularity, which is computed as average weekly pageviews over 26 weeks (about six months)<sup>12</sup> prior to its shock period:

$$
s c a l e d P a g e v i e w _ {i, t} = \frac {p a g e v i e w _ {i , t}}{p r e S h o c k P o p u l a r i t y _ {i}},\tag{1}
$$

where preShockPopulari $y _ { i } { = } 1 / 2 6 \sum _ { \mu { = } 1 } ^ { 2 6 } p a g e v i e w _ { i , \tau - \mu }$ and τ is the week when the content shock begins for article i. Because courses in our sample begin at different weeks and have different durations, we align their start dates and exclude the duration of shock period itself from the analysis. We consider relative time before or after the shock. Figure 2 plots the mean and standard deviation of weekly scaled pageviews in the six months prior to and after the shock period for treated and control articles.

This model-free view of the data displays a clear seasonal trend for both treatment and control group articles, indicating the need for careful construction of a control group as a counterfactual. Prior to the shock, articles in the control group mimic the time trend of those in the treatment group well, highlighting the success of our CEM procedure. We can also see the significant and relatively long-lasting impact of the treatment on postshock pageviews. Treated articles received approximately 10% more traffic than control articles, and this effect persisted for at least 26 weeks after the contribution shock. Evidently, Wikimedia’s campaign efforts to develop underdeveloped pages both worked and had a relatively long-term impact, suggesting the potential for a policy approach to fill impoverished regions in Wikipedia’s information network.

Figure 1. (Color online) Research Design—Direct Effect and Spillover Effect  
![](/api/attachments/8MD9CQBM/fulltext/images/78ad50bcdff1707d3952bc2a396b8a3632d3076612b45eccf707ec08221f75c3.jpg)  
Notes. This figure illustrates the direct treated and direct control articles, which constitute our matched sample for analyzing the direct effect of the treatment. Similarly, the spillover treated and spillover control articles constitute our sample for analyzing the spillover effect of the content contribution.

Figure 3 plots the mean and standard deviation of weekly scaled pageviews in the 26 weeks prior to and after the shock period for articles in the spillover treated and spillover control groups. Although pageviews of spillover treated articles seem to exceed those of spillover control articles after week 10, it is unclear from this model-free evidence alone whether the effect is significant. It should be noted that there is little doubt that spillover of attention occurs on Wikipedia—this can be seen explicitly from published clickstream data of actual traffic flowing over hyperlinks from one article to another (see Section 3.1.3 for further discussion). What is unclear is the extent and heterogeneity of treatment spillover effect and whether it can be teased out. Downstream articles, by virtue of being selectively linked to, tend to be more popular and have a larger variance in pageviews, suggesting that the effect, if it exists, may require econometric strategies to uncover. For example, it could be the case that the spillover is significant for only less popular articles, which may themselves be underdeveloped.

Figure 2. (Color online) Impact of Content Shock on Pageviews  
![](/api/attachments/8MD9CQBM/fulltext/images/b970cf1c29af7d5517e5c7420309e942f94e39decdd8f0e4467970883440ddfc.jpg)  
Notes. This figure displays the pageviews dynamics for articles in the treatment and control groups. Time is measured relative to the shock period (which is excluded) up to 26 weeks before and after. Dots and whiskers represent the means and standard deviations, respectively, o scaled pageviews in each bin.

Figure 3. (Color online) Spillover Effect on Hyperlinked Articles  
![](/api/attachments/8MD9CQBM/fulltext/images/20a38dd8ee9f2a0977d40894a3a3e6bc92759b5fd9b1a9067fec475ca72605fd.jpg)  
Notes. This figure displays the pageviews dynamics for articles to which treatment and control group articles link. Time is measured relative to the shock period (which is excluded), up to 26 weeks before and after. Dots and whiskers represent the means and standard deviations, respectively, of scaled pageviews in each bin

During the shock period, students also added new links to downstream pages as part of their contribution efforts. Newly added links are interesting in terms of attention spillover, because they may function to “open the valve” of attention flow between articles. Intuitively, old links can convey only changes in attention to downstream articles. In contrast, a newly added link can convey the totality of attention to downstream articles. This is illustrated in a simple conceptual model:

$$
\begin{array}{c} \Delta p a g e v i e w s _ {i, j} ^ {s p i l l o v e r} \propto p a g e v i e w s _ {i} \times n e w L i n k _ {i, j} \\ + \Delta p a g e v i e w s _ {i} ^ {t r e a t e d}, \end{array}\tag{2}
$$

where newL ${ . i n k _ { i , j } }$ can be thought of as an indicator variable (equal to one for new links and zero for old links). This suggests that attention spillover may be more clearly visible in model-free evidence if we look only at newly linked downstream articles (i.e., those downstream articles that were linked to from treated articles during the shock period). Figure 4 is similar to Figure 3 but distinguishes spillover populations by whether the link from the directly treated article was preexisting (old link) or added during the shock period (new link). New link articles in the spillover control group are not displayed, because they did not receive sufficient new links during the shock period.

The model-free plot of the spillover effect for new links confirms our reasoning. Spillover of attention across newly created links is clearly significant, and the temporal pattern of spillover closely follows the pattern of the postshock pageviews of directly treated articles. Compared with an old link, a new link can convey an additional 15% pageviews to target articles on average.

2.3.2. Editing Behaviors. Prior research has suggested that content contributions are self-promoting—that, in addition to boosting future attention (consumption), they also drive future contributions. We ex amine model-free evidence to determine whether the exogenous content contribution to articles leads to future contributions to those articles. We retrieved the full revision history of all articles in our sample and constructed two measures of editing behavior: the number of total edits and the number of unique editors in the six months prior to and after the shock period for each article. Because contribution behavior is relatively rare, we collapse the time series into “pre” and “post” periods. For each article, we look at the editing behavior before and after the content shock and their difference across treatment and control groups (Table 2).

Editing behavior is similar across treatment and control groups during the preshock period as expected: t-tests fail to reject the null hypothesis that the treatment and control groups have the same mean number of total edits $( p = 0 . 4 { \bar { 5 } } )$ ) and number of unique editors $( p = 0 . 3 6 )$ prior to the shock. For treated articles, in the six-month period after the contribution shock, the number of total edits increased by $3 . 7 ( p <$ 1e-9), and the number of unique editors increased by 2.2 persons $\left( p < 1 \mathrm { e } { - } 1 6 \right)$ . In contrast, control group articles did not experience any significant increase in number of total edits or number of unique editors. These results confirm that exogenous content shocks significantly drive future editing behavior.

Figure 4. (Color online) Spillover Effect—New Link  
![](/api/attachments/8MD9CQBM/fulltext/images/979bf587b7b0f905eb72859306e30b1babf524cc583690796fdb42b76022be34.jpg)  
Notes. This figure displays the pageviews dynamics for hyperlink articles based on whether the downstream article is connected through a new link or an old link. The time period is from 26 weeks prior to the contribution shock to 26 weeks after. Dots represent mean values of scaled pageviews in each bin, and whiskers represent the corresponding standard deviations.

Table 2. Editing Behavior Before and After the Shock Period

<table><tr><td rowspan="2"></td><td colspan="3">Total edits</td><td colspan="3">Unique editors</td></tr><tr><td>Before</td><td>After</td><td> $\Delta$ </td><td>Before</td><td>After</td><td> $\Delta$ </td></tr><tr><td>Control</td><td>11.2</td><td>11.3</td><td>0.1</td><td>6.2</td><td>6.5</td><td>0.2</td></tr><tr><td>Treatment</td><td>11.7</td><td>15.4</td><td>3.7</td><td>6.7</td><td>9</td><td>2.2</td></tr><tr><td>t-test (p-value)</td><td>0.45</td><td>—</td><td>&lt;1e-9</td><td>0.36</td><td>—</td><td>&lt;1e-16</td></tr></table>

Notes. The values displayed in the columns “Before” and $\ " \mathrm { A f t e r } ^ { \prime \prime }$ are counts of total edits and unique editors in the six months before and after the shock period, respectively. <sup>Δ</sup> = After <sup>−</sup> Before. The values in the row $\mathbf { \mu } ^ { \prime \prime } t \mathbf { - } \mathrm { t e s t } ^ { \prime \prime }$ are p-values from a two-sided t-test of the null hy pothesis that control and treatment groups have the same mean.

Overall, the model-free evidence confirms that exogenous content contributions drive future attention and editing behavior and that spillover of attention occurs significantly for newly added links. To capture the impact of varying intensity of treatment and heterogenous treatment impact, we turn to econometric modeling.

## 3. Empirical Methods

## 3.1. Direct Impact of Contribution Shock

In this section, we use econometric models to infer how differing intensities of content shocks affected treated articles contingent on article characteristics in terms of future content consumption and future editing behavior. We further investigate the source of attention increases to treated articles by analyzing the internal and external inbound traffic to treated pages.

3.1.1. Content Consumption. We estimate the average treatment effect on the treated (ATT) for content consumption using the following simple specification as the baseline model:

$$
P a g e v i e w s _ {i t} = \alpha P o s t S h o c k _ {i t} + \gamma_ {i} + \delta_ {t} + e _ {i t},\tag{3}
$$

where i is a Wikipedia article and t indexes the week. The dependent variable $P a g e v i e w s _ { i t }$ is the scaled pageviews for article i at week t as defined in Equation (1). For brevity, we have defined $P o s t S h o c k _ { i t } =$ PostShockPeriod × Treatment , a dummy variable equal to one if the period t is after shock and the article i is a treated article and zero otherwise. We include article and week fixed effects (γ and δ ) to account for articlelevel heterogeneity and common pageviews trends over time on the platform. Equation (3) estimates a simple difference-in-difference model of the impact of exogenous content contribution.

However, content contribution may have different impacts on articles with different characteristics. For example, less popular articles (with less average attention prior to the shock) may have been more or less affected. Article characteristics include article length, tenure, and popularity (defined as average pageviews over the six-months period before the shock). Moreover, not all treated pages received equal contributions during the shock period. Actual contributions varied significantly across treated articles, ranging from hundreds to tens of thousands of characters added through the course of student edits. To account for varying treatment intensity and allow for heterogeneous treatment effects, we estimate the following model:

$$
\begin{array}{r l} P a g e v i e w s _ {i t} & = \beta_ {1} P o s t S h o c k _ {i t} \times \log (c h a r C o u n t _ {i}) \\ & + \beta_ {2} P o s t S h o c k _ {i t} \times X _ {i} \\ & + \gamma_ {i} + \delta_ {t} + e _ {i t}, \end{array}\tag{4}
$$

where log charCount is the logarithm of the number of characters added to article i by a student during the shock period.<sup>13</sup> It represents the variation of treatment intensity. $X _ { i }$ is a vector of article characteristics measured before the content shock, including article tenure, size, and popularity. To provide better interpretability of model estimates and avoid the assumption of linearity, we bin these three continuous variables to low and high levels by their median value and include dummy variables that are equal to one when the value is high and zero otherwise (i.e., older article, longer article, and more popular article) in the vector $X _ { i } .$ Diagnostic tests show that two bins for our continuous variable are a reasonable choice (see the online appendix for more detail). The interaction term of $P o s t S \bar { h o } c k _ { i t }$ and $X _ { i }$ allows us to investigate heterogeneous treatment effects. We retain article fixed effects and week fixed effects. The parameters of interest are $\beta _ { 1 }$ and $\beta _ { 2 }$

Table 3. The Impact of Content Contribution on Consumption

<table><tr><td rowspan="2"></td><td colspan="3">Scaled pageviews</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>PostShock</td><td>0.119***(0.017)</td><td></td><td></td></tr><tr><td>PostShock × log(charCount)</td><td></td><td>0.035***(0.005)</td><td>0.065***(0.008)</td></tr><tr><td>PostShock × old article</td><td></td><td></td><td>-0.041*(0.024)</td></tr><tr><td>PostShock × popular article</td><td></td><td></td><td>-0.142***(0.025)</td></tr><tr><td>PostShock × long article</td><td></td><td></td><td>-0.015(0.025)</td></tr><tr><td>Article fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>287,664</td><td>287,664</td><td>287,664</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.122</td><td>0.122</td><td>0.124</td></tr></table>

Notes. In Models (2) and (3), we include PostShock × log(charCount) and exclude a bare PostShock term, because log(charCount) captures the intensity of a treatment (and every article that received a contribution as a consequence of treatment had some number of characters added).  
\*Significant at the 10% level; \*\*\*significant at the 1% level.

We use linear regression to estimate the above models, and results are reported in Table 3.<sup>14</sup> Because we scale the pageviews of each article with respect to its average pageviews over the six months prior to the shock, all estimates can be conveniently interpreted as the percentage changes of pageviews relative to their preshock average. Following the suggestion of Bertrand et al.(2004), all reported standard errors allow for arbitrary serial correlation across time and heteroscedasticity across articles to properly gauge the uncertainty around the estimates for serially correlated outcomes in panel data.

Overall, we find that postshock pageviews for treated article increased by 12% on average. The magnitude of the treatment effect is positively correlated with treatment intensity, and the impact is stronger for articles that are younger and less popular. The effect is both economically and statistically significant. Based on the model estimates in (3), a relatively young and less popular article with 6,000 characters added (the average number of characters added for treated articles in our sample) during the shock period experienced a 25% boost in postshock pageviews. The impact is even larger for similar articles that received a more intense treatment.

We perform diagnostics to assess our modeling assumptions in terms of linear interaction effects and common support. Results show that both assumptions are satisfied. For robustness, we also estimated alternative specifications. Using linear regression, we drop article fixed effects $\gamma _ { i }$ and retain only a simple treatment indicator, and all estimates are similar (see the online appendix for more details).

3.1.2. Editing Behavior. Beyond the impact on attention, we are also interested in whether exogenous content contributions spur future editing behavior. Because editing behavior is typically sparse for a Wikipedia article, for modeling purposes, we collapse the time series into just “pre” and “post” periods for the six months prior to and after the contribution shock. For each article, this yields two six-month time periods, during which we count the number of total edits and number of unique editors, and these comprise the dependent variables. Compared with alternative approaches (such as multistage, zero-inflated models), this transformation permits a simpler linear model, which retains interpretability and avoids more restrictive modeling assumptions (such as distributional assump tions on the error term that are required by Poisson or negative binomial regression). In addition, as suggested by Bertrand et al. (2004), the “pre” and “post” time series collapse allows us to obtain a consistent estimator for the standard errors of the treatment effect in the difference-in-difference model. The models estimated here are similar to models in Equations (3) and (4) for content consumption, apart from the time period collapse and the exchange of the dependent variable for editing behavior. For the sake of interpretability, we report the results from a linear regression, but results from Poisson regression and negative binomial regression are qualitatively similar (see the online appendix for details).

As we can see from Table 4, the contribution shock has a significant impact on future editing behavior in terms of both number of total edits and number of unique editors. Based on model estimates from columns (1) and (4) in Table $^ { 4 , }$ an article that received content contribution in the shock period had approximately 3.6 more edits and two more unique editors in the six months after the shock period compared with articles that did not receive exogenous content contribution. Similar to our findings for content consumption, the magnitude of the treatment effect increases with treatment intensity. Based on the estimates from columns (2) and (4) in Table 4, an article with 6,000 characters added during the shock period attracts 4.5 more edits and 2.5 editors in the six-month postshock period. As for heterogeneous treatment effects, the most significant factor was weaker impact for articles that already have a substantial amount of content.

Table 4. The Impact of Contribution Shock on Future Editing Behavior

<table><tr><td rowspan="2"></td><td colspan="3">Number of total edits</td><td colspan="3">Number of unique editors</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>PostShock</td><td>3.596***(0.855)</td><td></td><td></td><td>1.996***(0.243)</td><td></td><td></td></tr><tr><td> $PostShock \times log(charCount)$ </td><td></td><td>1.173***(0.229)</td><td>1.186***(0.234)</td><td></td><td>0.640***(0.068)</td><td>0.606***(0.065)</td></tr><tr><td> $PostShock \times old article$ </td><td></td><td></td><td>1.446(0.957)</td><td></td><td></td><td>0.691**(0.339)</td></tr><tr><td> $PostShock \times long article$ </td><td></td><td></td><td>-1.840**(0.926)</td><td></td><td></td><td>-0.829***(0.305)</td></tr><tr><td> $PostShock \times popular article$ </td><td></td><td></td><td>0.241(0.856)</td><td></td><td></td><td>0.333(0.326)</td></tr><tr><td>Article fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>10,964</td><td>10,964</td><td>10,964</td><td>10,964</td><td>10,964</td><td>10,964</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.63</td><td>0.63</td><td>0.63</td><td>0.82</td><td>0.82</td><td>0.82</td></tr></table>

\*\*Significant at the 5% level; \*\*\*significant at the 1% level.

3.1.3. Sources of Increased Attention. Both model-free results and estimates from statistical models confirm that exogenous contributions to articles drive future attention. However, from where does this increased attention originate? In general, articles can receive attention directly from external sources (e.g., traffic arriving to an article from outside of the information network, such as through search engine discovery or links from external websites) and internal sources (e.g., traffic flowing to an article from another upstream article). This distinction is interesting and meaningful from a policy perspective, because some articles may act to pull attention into the information network from external sources, thereby increasing the overall attention to the platform. Articles also play a role in the redistribution of attention throughout the platform, which is relevant from the standpoint of information equity. An article’s role in the flow of attention on the information network is illustrated in Figure 5.

For many large-scale real-world information systems, we cannot directly observe the detailed flow of attention (traffic). However, recently released data of monthly Wikipedia clickstream<sup>15</sup> snapshots provide exactly this level of detail for all Wikipedia articles. The clickstream data show how users arrive at an article and what links they click on within the article over the course of a given month aggregated at the article level. They contain counts of (referrer, resource) pairs extracted from the Wikipedia HTTP request logs, where a referrer is an HTTP header field that identifies the address of the web page that linked to the resource being requested. In other words, the clickstream data give a weighted network of articles and external sites, where the weight of each edge corresponds to the traffic flow along that edge. These counts are aggregated at the monthly level, and any (referrer, resource) pair with greater than 10 observations in a month is included in the data set. To give a sense of the scale of the data, the August 2016 release contains 25.8 million (referrer, resource) pairs from a total of 7.5 billion requests for about 4.4 million English Wikipedia articles. Figure 6 displays an example from the Wikimedia website, which illustrates in coming and outgoing traffic to the page “London” on English Wikipedia.

We leverage these data to shed light on the sources from which increased attention originates. The click stream data snapshots are only available for a limited number of months during the period of our natural experiment. To look at the change of traffic flow, we need to compare snapshots before and after the shock period. Fortunately, the Wikimedia Foundation released clickstream snapshots for both August 2016 and January 2017, which are just before and after articles were treated in the fall semester of 2016.

For each article, we calculate its total inbound traffic (combined internal and external traffic arriving at the article), total outbound traffic (traffic leaving the article), internal inbound traffic<sup>16</sup> (traffic flow to the article from other articles in the network), and external inbound traffic (traffic flow to the article from a search engine or other external website). We use CEM to ensure that articles in the treatment group and control group are comparable across all traffic measures prior to the start of the natural experiment (i.e., in the August 2016 snapshot). The k-to-k CEM procedure leaves us with 1,017 articles in both the treatment and control groups (see the online appendix for distribution and balance checks for clickstream data).

Figure 5. (Color online) Flow of Attention on Information Networks with Respect to a Particular Article in Terms of Flow In (Internal and External) and Flow Out  
![](/api/attachments/8MD9CQBM/fulltext/images/81250b46c5a42af37c2ff97e823629049befc79f88016270b0b3eff7e8d21f56.jpg)

We first look at changes in network structure in terms of newly created incoming links. During the shock period, it is likely that links to articles in either the treatment or control group were created either by student editors or as part of the natural evolution of the information network. Matching the 2,024 treatment and control articles in our sample with the clickstream data snapshots (for August 2016 and January 2017), we find that the number of active incoming links<sup>17</sup> for treated articles grew significantly faster compared with control group articles. As we see in Table 5, articles in the treatment group received on average 0.9 more active links during the shock period (compared with 0.4 for articles in control group). New incoming links make an article more discoverable by creating new channels to capture attention flow within the network. These increased channels may explain how contributions ul timately drive attention.

Attention from external sources can also explain the attention increases that we observed. To determine th extent to which observed attention increases derive from internal or external sources, we compare pre-/postshock changes in internal, external, and total incoming traffic across treatment and control articles in Table 6. The control group serves as a counterfactual to account for natural fluctuations arising from seasonal or other pageview trends, leading to a simple DID style estimator.

Figure 6. (Color online) Sources of Incoming and Outgoing Traffic for the “London” Wikipedia Article as Determined from the Clickstream Monthly Data Snapshots Provided by the Wikimedia Foundation  
![](/api/attachments/8MD9CQBM/fulltext/images/922fc87ba5a4567ef7478bd6cd1050ae64a6a4a4dcd6f280f8365b814299e62c.jpg)

Table 5. Number of Incoming Links

<table><tr><td rowspan="2"></td><td colspan="3">Number of incoming links per articles</td></tr><tr><td>Before</td><td>After</td><td>Δ</td></tr><tr><td>Control</td><td>6.6</td><td>7.0</td><td>0.4</td></tr><tr><td>Treatment</td><td>6.6</td><td>7.5</td><td>0.9</td></tr><tr><td>t-test (p-value)</td><td>0.96</td><td>—</td><td>&lt;1e-15</td></tr></table>

Notes. The values displayed in the columns “Before” and $\ " { } \mathrm { A f t e r } ^ { \prime \prime }$ are the average numbers of incoming links per articles in the six months before and after the shock period, respectively. <sup>Δ</sup> = After <sup>−</sup> Before. The values in the row “t-test” are p-values from a two-sided t-test of the nul hypothesis that control and treatment groups have the same mean.

From Table 6, we see that the total incoming traffic increased by 14.6 pageviews per article per day for the treatment group relative to 8.2 for the control group. The extra 6.4 pageviews can be interpreted as the ATT, which is about a 14% increase relative to the preshock average. This result is consistent with our prior estimates, which were based on article-level pageviews data. Hence, we demonstrate the impact of content shock using two different data sources (clickstream data and pageviews data) and find similar effect sizes. We can also see that both internal and external sources conveyed increased attention, indicating that content contributions yield attention gains from within the information network and from without. We suggest that attention gains from external sources are likely the result of increased visibility of the articles in search engine results.<sup>18</sup> Modern search engine algorithms are clearly sensitive to the recency of content changes. Although we do not know the actual details of search engine ranking algorithms (proprietary information), more incoming hyperlinks to a page convey a higher ranking in ordinary PageRank. We define the ratio of internal to external traffic as $R ( T ) = T ^ { i n t e r n a l } / T ^ { e x t e r n a l }$ <sup>l</sup>. New traffic has a higher ratio $( R ( \Delta T ) = 0 . 4 )$ relative to the preshock ratio $( R ( T _ { B e f o r e } ) =$ 0.3), indicating that new traffic originates slightly more from internal sources.

## 3.2. Attention Spillover

The impact of content shocks is not limited to directly treated articles. Attention resulting from the shock can also spill over onto other downstream articles through the hyperlink network. Conceptually, we can think of the spillover as a dyadic relationship between each source (directly treated or control) and target article. As our consideration of model-free evidence showed, new links, which build bridges between source and target articles, seem to play a critical role in facilitating spillover. It also seems plausible that the popularity of source and target articles may moderate the extent of the spillover. We test these hypotheses with the following model:

$$
\begin{array}{r l} P a g e v i e w s _ {i t} & = \beta_ {0} P o s t S h o c k _ {i t} + \beta_ {1} P o s t S h o c k _ {i t} \\ & \times s t P o p u l a r i t y _ {i} + \beta_ {2} P o s t S h o c k _ {i t} \\ & \times n e w L i n k _ {i} + \beta_ {3} P o s t S h o c k _ {i t} \\ & \times s t P o p u l a r i t y _ {i} \times n e w L i n k _ {i} \\ & + \gamma_ {i} + \delta_ {t} + e _ {i t}, \end{array}\tag{5}
$$

where i is a target article and t is the week. stPopularity is a two-dimensional vector <sub>(</sub>sourcePopularity<sub>i</sub>, target Popularity representing the popularity of the source article (i.e., the treated article that received an exogenous content contribution) and the target article (that was linked to from the treated article), respectively. The indicator newLink is equal to one if the link between source article and target article was added during the treatment period and zero otherwise. The parameters of interest are $\beta _ { 1 } , \beta _ { 2 } , \beta _ { 3 }$ . We include each term in successive models gradually to investigate how they parcel out the overall spillover effect. The results are displayed in Table 7.

We can see from column (1) of Table 7 that the overall effect (i.e., when averaged over all articles) is small but significant. This result is consistent with the model-free evidence and our intuition given the large heterogeneity across articles. Column (2) of Table 7 shows how the treatment effect varies with the popularity of source and target articles. Evidently, spillover from low-popularity source articles to low-popularity target articles yielded a 2.7% increase in pageviews $( p < 0 . 0 1 )$ . Although this effect size may initially seem small, it is measured with respect to a single outgoing link from the treated article to one target article. In general, treated articles link to multiple downstream target articles, suggesting that the overall collective effect of spillover can be quite substantial. Interestingly, spillover is enhanced when both source and target articles are less popular, which is a typical scenario for underdeveloped pages, particularly in informationally impoverished regions in the Wikipedia network.

Table 6. Incoming Traffic Breakdown

<table><tr><td rowspan="2"></td><td colspan="3">Total incoming traffic</td><td colspan="3">Internal traffic ( $T^{internal}$ )</td><td colspan="3">External traffic ( $T^{external}$ )</td></tr><tr><td>Before</td><td>After</td><td> $\Delta$ </td><td>Before</td><td>After</td><td> $\Delta$ </td><td>Before</td><td>After</td><td> $\Delta$ </td></tr><tr><td>Control</td><td>45.4</td><td>53.6</td><td>8.2</td><td>10.2</td><td>12.2</td><td>2.0</td><td>35.2</td><td>41.4</td><td>6.0</td></tr><tr><td>Treated</td><td>44.7</td><td>59.3</td><td>14.6</td><td>10.2</td><td>14.0</td><td>3.8</td><td>34.4</td><td>45.2</td><td>10.8</td></tr><tr><td>t-test (p-value)</td><td>0.85</td><td>—</td><td>0.01</td><td>0.97</td><td>—</td><td>0.05</td><td>0.80</td><td>—</td><td>0.03</td></tr></table>

Notes. The values displayed in the columns “Before” and “After” are the average traffic per article per day in the six months before and after the shock period, respectively. <sup>Δ</sup> = After <sup>−</sup> Before. The values in the row “t-test” are p-values from a two-sided t-test of the null hypothesis that control and treatment groups have the same mean.

Table 7. The Attention Spillover of Contribution Shock

<table><tr><td rowspan="2"></td><td colspan="4">Scaled pageviews</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>PostShock</td><td>0.008***(0.003)</td><td>0.027***(0.006)</td><td>-0.006(0.004)</td><td>-0.005(0.007)</td></tr><tr><td>PostShock × popularTargetArticle</td><td></td><td>-0.013**(0.005)</td><td></td><td>-0.004(0.005)</td></tr><tr><td>PostShock × popularSourceArticle</td><td></td><td>-0.016**(0.007)</td><td></td><td>0.000(0.007)</td></tr><tr><td>PostShock × newLink</td><td></td><td></td><td>0.129***(0.012)</td><td>0.148***(0.018)</td></tr><tr><td>PostShock × popularTargetArticle × newLink</td><td></td><td></td><td></td><td>-0.138***(0.023)</td></tr><tr><td>PostShock × popularSourceArticle × newLink</td><td></td><td></td><td></td><td>0.073***(0.023)</td></tr><tr><td>Article fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>6,862,648</td><td>6,862,648</td><td>6,862,648</td><td>6,862,648</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.104</td><td>0.104</td><td>0.104</td><td>0.104</td></tr></table>

\*\*Significant at the 5% level; \*\*\*significant at the 1% level.

A more interesting insight emerges when we consider whether the link between source and target articles was new. Surprisingly, for new links, the impact of the spillover can be as large as around 13%, which is close in magnitude to the average direct effect. As illustrated in our discussion of model-free evidence, the rationale is that a new link can “open the valve” between source and target articles and convey both the preexisting and increased attention from the source to the target. We note that old links clearly convey attention (as the clickstream data illustrate). However, they convey only increased attention from the source to the target, and we lack the statistical power to see it directly in this model. Finally, the attention spillover is even larger (14.8%) for new links between less popular source and target articles. Because underdeveloped regions of information networks likely satisfy all of these criteria (i.e., low popularity of articles and lack of preexisting link structures between articles), policies that focus on promoting such regions can benefit from strategies that harness spillover.

## 4. Policy Simulation of Attention Contagion

Our spillover results indicate that attention shocks in Wikipedia have a local network effect. Articles in the system benefit when upstream articles receive attention. Some spillovers direct attention to downstream articles that already receive significant exposure. However, some of this attention may increase exposure to underdeveloped articles. This begs the following question: by focusing attention on connected sets of underdeveloped articles, can we optimally harness spillovers in order to redirect attention to articles that would benefit the most from increased exposure?

To better understand this question, we conduct policy simulations in which we integrate our findings from the econometric estimates into an empirically calibrated attention diffusion model to guide policy decisions through the analysis of counterfactuals. We propose a policy in which editors are encouraged to focus their editorial efforts on a set of targeted underdeveloped articles that are intimately related to one another in order to harness attention contagion and maximize joint exposure. Targeted sets of related articles either will be well connected at the outset (i.e., a set of stub articles that are already well connected but remain underdeveloped) or will become well connected as a consequence of directed editorial efforts. That is, the links between sets of related ar ticles need not exist prior to being edited but can arise as a consequence. The rationale is that attention spill overs to underdeveloped articles are more valuable to the platform (in terms of the information equity that they convey) than spillovers to articles that are already well developed.

## 4.1. Intuition—A Mean Field Estimation

We begin by providing an intuition for how network structure can impact attention spillover using a mean field estimation. To represent a set of related and highly connected articles in a manner that is simple, we consider network cliques defined as a set of n completely connected nodes in a network. To demonstrate our intuition, we analytically calculate the spillover in cliques of size n using mean field assumptions.

For an n clique, assuming that each node receives direct traffic T and where spillover over a single step is given by $T _ { s p i l l o v e r } = f T _ { \cdot }$ , the total spillover exposure gain is given by ${ \textstyle \sum _ { k = 2 } ^ { n } } { \dot { n ! } } / ( n - k ) ! \stackrel { * } { * } f ^ { k - 1 }$ . The summand represents all partial permutations of a set of k nodes, describing the paths of length k 1 that successive spillovers take (each contributing a multiplicative factor of $f )$ from each starting node to each other ending node. Figure 7 displays the total spillover gain for all articles in the clique (i.e., the total additional exposure gained from spillover from each article in the clique onto all other articles).

For example, for a mean spillover of f 0.10 and for cliques of sizes $n = 3 , 4$ , and 5, the total spillover exposure gain is 0.66, 1.46, and 2.73, respectively, as measured in units of proportion of incident direct traffic. This estimate assumes constant spillover ( f ) and equal traffic from any node in the clique to any other, which is unlikely to hold in the real world. Fortunately, we can relax these assumptions by using exact and fine-grained data on traffic flowing on all links in Wikipedia and traffic to all pages from external sources (e.g., traffic from search engines that arrive at Wikipedia pages) from the monthly clickstream snapshots.<sup>19</sup> We leverage these data to estimate spillover and assess policies designed to capture spillover through empirically calibrated simulations.

## 4.2. Diffusion Simulation

Our mean field estimation is useful to obtain stylized estimates of policies that focus attention on clusters of well-connected articles and develop an intuition about why this might work, but it does not account for realworld heterogeneity in actual traffic flow on the links between articles. To address this, we test policies more realistically and comprehensively through simulations of traffic flow that arise from attention perturbations. We define perturbations as increases in incident traffic from external sources. These policy simulations make use of highly detailed clickstream data for calibration to ensure that traffic flow changes follow pathways in proportion to real-world patterns on Wikipedia. To accomplish this, we use a generalization of the personalized PageRank algorithm.<sup>20</sup> PageRank is widely recognized as one of the most important algorithms used for network-based information retrieval. It represents traffic flow as a random walk process on the information network, and it is given in the iterative form by

$$
\vec {r} _ {t + 1} = (1 - \alpha) \vec {r} _ {0} + \alpha G \cdot \vec {r} _ {t},\tag{6}
$$

where $\overline { { r } } _ { t }$ is a vector of the traffic (attention) landing on article i for the tth iteration of the diffusion process; $\overline { { r } } _ { 0 }$ is a vector of the initial distribution of traffic or whenever the process involves “hopping” rather than following a hyperlink from an article to a downstream article. The “hopping” occurs with probability <sub>(</sub>1 <sub>−</sub> α<sub>)</sub>—the so-called damping factor. G is a matrix of normalized outflow of traffic from any article i that hyperlinks to an article j. Convergence of the iterative form of PageRank is achieved for some $\stackrel {  } { r } \equiv \stackrel {  } { r } _ { t + 1 }$ when $| \overline { { r } } _ { t + 1 } - \overline { { r } } _ { t } | < \epsilon$ for a small choice of -. The converged vector r represents the normalized accumulated traffic to each article i that results from the simulated random walk process. We represent this simulation process functionally as $\Vec { r } = \hat { P R } ( \stackrel {  } { r } _ { 0 } , G , \alpha , \epsilon )$

Ordinary PageRank assumes an equal initial distribution of traffic, $\begin{array} { r } { \vec { r } _ { 0 } = 1 / N , } \end{array}$ , and equal probability of outflow along all links, $G _ { i j } = A _ { i j } / k _ { j } ,$ where $A _ { i j }$ is the adjacency matrix and $k _ { j }$ is the degree of article j. The damping factor is conventionally chosen as $( 1 - \alpha ) =$ 0.15. Personalized PageRank relaxes the assumption of equal initial distribution of traffic for an arbitrary normalized ${ \vec { r } } _ { 0 } .$ . To guarantee realism, we relax these assumptions even further and leverage the clickstream data (see Section 3.1.3 for a description) to empirically calibrate internal and external traffic flows in the simulation.<sup>21</sup> In personalized PageRank, we set the vector $\stackrel {  } { r } _ { 0 }$ to the normalized empirical distribution of external incident traffic on each article i and the matrix G to the normalized empirical distribution of outflow traffic from article i to article j. Having defined the simulation process, we are now in a position to assess how perturbations to attention (i.e., increases in incident traffic from external sources—e.g., arising from content contribution shocks) drive accumulated attention to all articles in the network. We represent a general perturbation to some set of articles S as $\begin{array} { r } { \vec { r } _ { 0 p } ^ { S } = \stackrel {  } { r } _ { 0 } + \stackrel {  } { \delta r } _ { 0 p } ^ { S } } \end{array}$ and set the perturbation according to

Figure 7. Mean Field Estimate of Total Spillover to a Clique  
![](/api/attachments/8MD9CQBM/fulltext/images/7f5bee614f0c6eb72caa09b1fcc5457e40734136e67c4377f6d15b27f5dbc19c.jpg)  
Note. For each clique shown, we calculate the mean field estimate of the total spillover to all nodes in the clique under the dynamic process described in the text.

$$
(\delta r _ {0 p}) _ {i} = (r _ {0}) _ {i} \left\{ \begin{array}{l l} p, & \text { for   } i \in S \\ 0, & \text { otherwise }, \end{array} \right.\tag{7}
$$

where $p > 0$ represents a constant percentage increase of attention shock to affected articles (those in the chosen perturbed set S). In other words, we create relative perturbations of attention that are correlated across a set S of chosen articles. For each perturbation, we calculate the resultant PageRank vector $\overrightarrow { r } _ { p } ^ { S } = P R ( \stackrel {  } { r } _ { 0 p } ^ { S } , G , \alpha , \epsilon )$ and compare it with the unperturbed PageRank vector $\Vec { r } = P R ( \Vec { r } _ { 0 } , G , \alpha , \epsilon )$ . Specifically, we are interested in the resultant excess attention (EA) received by underdeveloped articles, which comprise the articles in the perturbed set:

$$
E A (S, p) = \sum_ {i \in S} \frac {r _ {p , i} ^ {S} - r _ {i}}{r _ {i}}.\tag{8}
$$

Because any perturbation of a set of articles will result in those articles receiving excess attention, we compare excess attention across two different policies: (i) an attention contagion policy (ACP), where editorial efforts are focused on clusters of wellconnected, underdeveloped articles, and (ii) an undirected attention policy (UAP), where editorial efforts are focused on randomly chosen underdeveloped articles that are not necessarily (but may incidentally be) connected to one another. The random selection of underdeveloped articles under this latter UAP will lead to contributions to articles that are more spread out across the information network compared with the ACP.<sup>22</sup> The two policies are illustrated in Figure 8. The UAP represents a simple and useful baseline for comparison. It may be that, without guidance, editors already cluster their editorial focus to some extent. However, we do not parametrize clustering under UAP to avoid introducing unnecessary assumptions and additional complexity.

To compare these two policies, we first need to identify sets of well-connected articles in Wikipedia that appear in clickstream data and are good empirical proxies for underdeveloped articles. Importantly, many actual sets of related, underdeveloped articles will likely lack the linking structure that would naturally arise from directed editorial focus. That is to say, although these underdeveloped pages are related to one another, they do not yet possess the linking structure to connect them. To avoid making unnecessary and potentially ill-informed assumptions about unobserved network structure and its relationship to content, we instead focus only on actual links that appear in the clickstream data and that experienced actual traffic flow. To accomplish this, we use the weighted directed graph of traffic

Figure 8. (Color online) Concentration of Attention Across Network Communities or Cliques for the Two Policies flow between articles and seek tightly connected sets of nodes in the form of both cliques and communities. To find cliques, we computed a large sample of maximal cliques via depth-first search with Bron– Kerbosh-style pruning (Tomita et al. 2006). To find communities, we modify the well-known label propagation algorithm (LBA) (Raghavan et al. 2007): to address the instability of the original LBA, we perform the algorithm 200 times and assign articles to the same community if and only if they were assigned to the same community in at least 95% of the runs. This approach produces stable, tightly connected communities with minimal noise. It is also efficient, fast, and able to cope with networks of millions of nodes. We filter maximal cliques and communities and retain only those of small to moderate size $( 2 \leq n \leq 6 )$ . For each such clique or community, we match each article to another article in a different clique or community with the closest external incident traffic. This yielded a set of well-connected articles to perturb according to the attention contagion policy, ${ \bf \bar { \cal S } } _ { c } ^ { A C P } ,$ , and a corresponding matched set of articles to be used in the undirected attention policy, $S _ { m _ { c } } ^ { U A P } .$ , where c labels the clique or community and $m _ { c }$ labels the matched set. Note that the articles in $S _ { c } ^ { A C P }$ belong to the same clique or community (c), whereas articles in $S _ { m _ { c } } ^ { U A P }$ can belong to many different cliques or communities. Because testing large numbers of perturbations is computationally intense, we select a random subset of 600 cliques and communities, and for each clique or community, we simulate the perturbations for both policies and compare the distribution of excess attention $E A ( S _ { c } ^ { A C P } , \hat { p } )$ with $E A ( S _ { m _ { c } } ^ { U A P } , p )$ . The results are displayed in Figure 9 for cliques (Figure 9(a)) and communities (Figure 9(b)) for simulation with $p = 0 . 1$

(a)  
![](/api/attachments/8MD9CQBM/fulltext/images/de2b0054741e25d55f9a277a773f88b15333513341fadbee05c3a6ceff26c134.jpg)

(b)  
![](/api/attachments/8MD9CQBM/fulltext/images/ee4ab2df44a09c0616fc0e798a8116e005a67afd21432f1fe8efe884fa33ad75.jpg)  
Notes. Red nodes receive increased attention (perturbed). Panel (a) illustrates the ACP, where attention to red nodes (which constitute the perturbed set $S _ { c } ^ { A C P }$ for a given clique or community, c) is clustered within a community or clique. Panel (b) illustrates the UAP, where attention is spread out randomly across communities or cliques in the network. To compare policies fairly, red nodes in panel (a) are matched one to one to red nodes in panel (b) (comprising the set $S _ { m _ { c } } ^ { U A \bar { P } }$ as described in the text).

Figure 9. (Color online) Distribution and Kernel Density Estimates of Excess Attention for Perturbative Simulations $( p = 0 . 1 )$ of the ACP and UAP for 600 Cliques and Communities  
![](/api/attachments/8MD9CQBM/fulltext/images/5763ee33931a5a1e76ce6256d525eb18ac12f466157c69c6497ab0c1581ad946.jpg)

(b)  
![](/api/attachments/8MD9CQBM/fulltext/images/7f65bd7c60371cc9dcd1419f4fc97f02cd760ba90fbc30aed385aa1b3c9d55b5.jpg)  
Notes. (a) Cliques. (b) Communities. The ACP leads to significantly more excess attention.

The attention contagion policy clearly leads to significant excess attention directed toward underdeveloped pages compared with the undirected attention policy, yielding a relative increase of mean excess attention (ACP over UAP) of 106% for cliques and 44.2% for communities $( p < 1 \mathrm { e } { - } 7 1 $ from two-sided t-test).<sup>23</sup> Because editors may already cluster their editorial attention to some extent even without a guidance policy, our results should be interpreted as an upper bound to the value conveyed by the attention contagion policy. Excess attention scales linearly with the size of the perturbation, which follows from the definition of excess attention and the expansion of the iterative perturbed PageRank equation. The shape of the distributions of excess attention for either policy is determined entirely from the network structure around the perturbation set, implying that the results are identical up to a scale factor (p) for different choices of perturbation size. Results are also robust to different random samples of cliques or communities (see the online appendix for details).

## 5. Conclusion

Open collaborative platforms have fundamentally changed the way that knowledge is produced, disseminated, and consumed in the digital era. This study directly contributes to our understanding of the interaction between production and consumption of information and the phenomenon of attention contagion on Wikipedia, arguably the largest and most successful example of such platforms. To conduct valid causal inference so that we can inform policy with high confidence, we used a battery of methods, including natural experiment, matching, econometric modeling, and empirically informed simulation. We found that real-world exogenous contributions increase future attention by 12% on average, with stronger impact for more significant contributions They also increase future contribution by 3.6 more edits and two more unique editors to affected articles over a six-month period. This impact is both economically significant and persists for a long time. In addition, we obtained causal estimates of the extent of spillover impact and identified characteristics of articles and links between them that receive the most benefit from spillovers. Specifically, we find that spillover is greatest across new links that point to less popular target articles, yielding an impact as high as 22% for new links from popular source articles to unpopular target articles and 15% for new links from less popular source articles to less popular target articles.

Overall, our results confirm the existence of positive feedback loops of production and consumption of information on Wikipedia. This, unfortunately, also implies that underdeveloped articles experience a poor-get-poorer phenomenon and are, therefore, naturally disadvantaged in the cumulative development process. This observation is deeply troubling, because it suggests that impoverished regions in collaborative information systems will remain impoverished in the absence of policies that are specifically designed to address this problem. More importantly, because information poverty is often correlated with economic poverty (Norris 2001, Yu 2006, Forman et al. 2012, Graham et al. 2014), this phenomenon can act to exacerbate economic, social, political, and cultural inequalities. Fortunately, our findings suggest that less developed regions of information networks can benefit substantially from spillovers. We carry this insight further and propose and compare policies that drive editorial attention using diffusion simulations that are based on real-world traffic flows on Wikipedia. We evaluate the attention contagion policy that leverages spillovers to stimulate development of impoverished regions. We find that this policy can yield up to a twofold increase in excess attention relative to the baseline undirected attention policy. These results are directly relevant to concerns of information equity and have managerial implication for collaborative information platforms. Although we focus on Wikipedia, our findings are relevant to the uneven coverage problem that exists in many platforms that facilitate collaborative content production in domains, such as open source software creation (e.g., GitHub), knowledge markets (e.g., Stack Overflow or Quora), and product reviews (e.g., Amazon or Steam).

Our results suggest that two policies can be effective for encouraging the development of underdeveloped articles or impoverished regions in the information network. First, editors may be encouraged to identify popular articles that should naturally (semantically) link to a focal underdeveloped article. Our results show that creating such a link can harness the largest attention spillover (as much as 22%), although care should be taken to ensure that added links are semantically meaningful. Second and perhaps, more importantly, Wikipedia should consider encouraging coherent development of impoverished regions. Our results show that underdeveloped regions, which typically lack both attention and the linking structure to connect related articles, are precisely positioned to benefit from attention contagion policies. Currently, the quality and importance of Wikipedia articles are assessed through a tagging system implemented on talk pages. Tools exist that use these metrics to allow editors to search for specific articles that are both important and in need of attention. Additional features could be added to these tools to encourage a coherent focus for individual editors or even groups of editors.

This work is not without limitations. This work tackles causality by leveraging a natural experiment, matching, econometric techniques, and empirically informed simulation. However, cleaner causal inference could be achieved in future work through controlled, randomized experiments. As we examine attention spillover owing to a second-order shock to attention (that itself is driven by a contribution shock), we may miss subtle heterogeneous spillover effects. Future work could consider perturbations to link struc ture and real-world experimental tests of attention con tagion policies. Furthermore, Wikipedia is subject to other natural experiments that may be discoverable. In particular, examination of clickstream data may permit the discovery of natural experiments that can help us bet ter understand attention flow in information networks.

## Endnotes

<sup>1</sup> It is the fifth most visited website in the world according to Alexa.

<sup>2</sup> See https://en.wikipedia.org/wiki/Wikipedia:Size\_of\_Wikipedia, accessed November 7, 2019.

<sup>3</sup> See https://wikiedu.org/changing/wikipedia/, accessed November 7, 2019.

<sup>4</sup> See http://time.com/4180414/wikipedia-15th-anniversary/, accessed November 7. 2019

<sup>5</sup> See https://en.wikipedia.org/wiki/Wikipedia:Size\_comparisons, accessed November 7, 2019.

<sup>6</sup> See https://en.wikipedia.org/wiki/Criticism\_of\_Wikipedia, accessed November 7, 2019.

<sup>7</sup> See https://meta.wikimedia.org/wiki/Research:Increasing\_article \_coverage, accessed November 7, 2019.

<sup>8</sup> See https://wikiedu.org/changing/wikipedia/, accessed November 7, 2019.

<sup>9</sup> Wikimedia changed their measurement of pageviews in May 2015 to better filter out bot traffic and incorporate the visits from mobile devices. Looking at the articles edited in 2016 guarantees that we have a consistent measure of pageviews in the six months before and after the content shock.

<sup>10</sup> See https://dashboard.wikiedu.org/, accessed November 7, 2019.

<sup>11</sup> See https://www.mediawiki.org/wiki/API:Main\_page, accessed November 7, 2019.

<sup>12</sup> Note that this normalization simply scales the time series of pageviews of each article by a constant. Examination of the modelfree evidence for scaled and unscaled pageviews reveals that this scaling is appropriate.

<sup>13</sup> For articles in the control group, the value of log charCount is set to zero.

<sup>14</sup> Note that, in Models (2) and (3) in Table 3, we include PostShock × log(charCount) and exclude a bare PostShock term, because log(charCount) captures the intensity of a treatment (and every article that received a contribution as a consequence of treatment had some number of characters added).

<sup>15</sup> See https://meta.wikimedia.org/wiki/Research:Wikipedia\_clickstream, accessed November 7, 2019.

<sup>16</sup> The link traffic only includes links from other Wikipedia articles. The link traffic from other websites outside of the ecosystem of Wikipedia was classified under the external traffic category.

<sup>17</sup> We define an active incoming link as one that conveys at least 10 pageviews in a month. The monthly clickstream data snapshots filter out any (referrer, resource) pairs that do not meet this criterion.

<sup>18</sup> Search engines traffic dominates other external sources, such as external websites, in external traffic.

<sup>19</sup> See Ellery Wulczyn and Dario Taraborelli (2015) Wikipedia clickstream at https://meta.wikimedia.org/wiki/Research:Wikipedia \_clickstream, accessed November 7, 2019.

<sup>20</sup> Personalized PageRank has recently been formally related to the task of community detection in networks (Kloumann et al. 2016).

<sup>21</sup> In prior research, others have calibrated PageRank with internal traffic from Wikipedia clickstream data (Dimitrov et al. 2017) but have not accounted for variation in external traffic.

<sup>22</sup> In fact, because UAP spreads out editorial focus through the network, it conveys excess attention to more unique articles. However, under ACP, more articles receive a larger share of excess attention. For more details, see Figure A11 and the related discussion in the online appendix.

<sup>23</sup> Alternatively, two-sample Kolmogorov-Smirnov tests reject the null hypothesis that the distributions are equal with p < 1e-63.

## References

Aaltonen A, Seiler S (2016) Cumulative growth in user-generated content production: Evidence from Wikipedia. Management Sci. 62(7):2054–2069.

Aral S, Muchnik L, Sundararajan A (2013) Engineering social con tagions: Optimal network seeding in the presence of homophily. Network Sci. 1(2):125–153.

Barabasi AL, Albert R (1999) Emergence of scaling in random net-´ works. Science 286(5439):509–512.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Carmi E, Oestreicher-Singer G, Stettner U, Sundararajan A (2017) Is Oprah contagious? The depth of diffusion of demand shocks in a product network. Management Inform. Systems Quart. 41(1): 207–221.

Dimitrov D, Singer P, Lemmerich F, Strohmaier M (2017) What makes a link successful on Wikipedia? Proc. 26th Internat. Conf. World Wide Web—WWW '17 (ACM Press, New York), 917–926

Forman C, Goldfarb A, Greenstein S (2012) The internet and local wages: A puzzle. Amer. Econom. Rev. 102(1):556–575.

Gallus J (2017) Fostering public good contributions with symbolic awards: A large-scale natural field experiment at Wikipedia. Management Sci. 63(12):3999–4446.

Graham M, Hogan B, Straumann RK, Medhat A (2014) Uneven geographies of user-generated information: Patterns of increasing informational poverty. Ann. Assoc. Amer. Geographers 104(4):746–764

Halavais A, Lackaff D (2008) An analysis of topical coverage of Wikipedia. J. Comput.-Mediated Comm. 13(2):429–440.

Harhoff D, Henkel J, Von Hippel E (2003) Profiting from voluntary information spillovers: How users benefit by freely revealing their innovations. Res. Policy 32(10):1753–1769.

Hinnosaar M, Hinnosaar T, Kummer M, Slivko O (2017) Wikipedia matters. Preprint, submitted October 3, http://dx.doi.org/10.2139 ssrn.3046400.

Ho DE, Imai K, King G, Stuart EA (2007) Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference. Political Anal. 15(3):199–236.

Iacus SM, King G, Porro G (2012) Causal inference without balance checking: Coarsened exact matching. Political Anal. 20(1): 1–24.

Kampf M, Tessenow E, Kenett DY, Kantelhardt JW (2015) The de-¨ tection of emerging trends using Wikipedia traffic data and context networks. PLoS One 10(12):e0141892.

Kampf M, Tismer S, Kantelhardt JW, Muchnik L (2012) Fluctuations¨ in Wikipedia access-rate and edit-event data. Phys. A 391(23): 6101–6111.

Kane GC (2009) It’s a network, not an encyclopedia: A social network perspective on Wikipedia collaboration. Acad. Management J. 2009(1):1–6.

Kane GC, Ransbotham S (2016) Research note—content and collaboration: An affiliation network approach to information quality in online peer production communities. Inform. System Res. 27(2):219–470.

Keegan B, Gergle D, Contractor N (2013) Hot off the Wiki: Structures and dynamics of Wikipedia’s coverage of breaking news events. Amer. Behav. Sci. 57(5):595–622.

Kittur A, Chi EH, Suh B (2009) What’s in Wikipedia? Proc. 27th Internat. Conf. Human Factors Comput. Systems—CHI 09 (ACM Press, New York), 1509–1512.

Kloumann I, Ugander J, Kleinberg J (2016) Block models and per sonalized PageRank. Proc. Natl. Acad. Sci. USA 114(1):33–38.

Kummer ME (2014) Spillovers in networks of user generated content: Evidence from 93 pseudo-experiments on Wikipedia. Preprint, submitted December 29, https://ssrn.com/abstract=2567179.

Kummer ME (2019) Attention in the peer production of user generated content: Evidence from 93 pseudo-experiments on Wikipedia. Pre print, submitted August 2, https://ssrn.com/abstract=3431249.

Kummer ME, Saam M, Halatchliyski I, Giorgidze G (2016) Centralit and content creation in networks: The case of economic topics on German Wikipedia. Inform. Econom. Policy 36:36–52

Kuznetsov S (2006) Motivations of contributors to Wikipedia. ACM SIGCAS Comput. Soc. 36(2):1–7.

Lampe C, Obar J, Ozkaya E, Zube P, Velasquez A (2012) Classroom Wikipedia participation effects on future intentions to contribute. Proc. ACM 2012 Conf. Comput. Supported Cooperative Work—CSCW ’12 (ACM, New York), 403–406.

Lin Z, Goh KY, Heng CS (2017) The demand effects of product recommendation networks: An empirical analysis of network diversity and stability. Management Inform. Systems Quart. 41(2): 397–426.

Muchnik L, Aral S, Taylor SJ (2013a) Social influence bias: A ran domized experiment. Science 341(6146):647–651.

Muchnik L, Pei S, Parra LC, Reis SDS, Andrade JS Jr, Havlin S, Makse HA (2013b) Origins of power-law degree distribution in the heterogeneity of human activity in social networks. Sci. Rep. 3(1): 1783.

Norris P (2001) Digital Divide: Civic Engagement, Information Poverty, and the Internet Worldwide (Cambridge University Press, Cam bridge, UK).

Nov O (2007) What motivates Wikipedians? Comm. ACM 50(11): 60–64.

Raghavan UN, Albert R, Kumara S (2007) Near linear time algo rithm to detect community structures in large-scale networks Physical Rev. E: Statist. Nonlinear Soft Matter Physics 76(3 Pt 2): 036106.

Ransbotham S, Kane G, Lurie NH (2012) Network characteristics and the value of collaborative user generated content. Marketing Sci. 31(3):387–405.

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1): 41–55.

Salganik MJ, Dodds PS, Watts DJ (2006) Experimental study of inequality and unpredictability in an artificial cultural market. Science 311(5762):854–856.

Taylor SJ, Eckles D (2018) Randomized experiments to detect and estimate social influence in networks. Lehmann S, Ahn YY, eds. Complex Spreading Phenomena in Social Systems (Springer In ternational Publishing, Cham, Switzerland), 289–322.

Thompson NC, Hanley D (2017) Science is shaped by Wikipedia: Evidence from a randomized control trial. Preprint, submitted September 20, http://dx.doi.org/10.2139/ssrn.3039505.

Tomita E, Tanaka A, Takahashi H (2006) The worst-case time complexity for generating all maximal cliques and computational experiments. Theoret. Comput. Sci. 363(1):28–42.

Walker D, Muchnik L (2014) Design of randomized experiments in networks. Proc. IEEE 102(12):1940–1951.

West R, Leskovec J (2012) Human wayfinding in information networks. Proc. 21st Internat. Conf. World Wide Web—WWW ’12 (ACM, New York), 619–628.

Wilkinson D, Huberman B (2008) Assessing the value of cooperation in Wikipedia. Preprint, submitted February 1, https://arxiv.org pdf/cs/0702140.pdf.

Wu F, Huberman BA (2007) Novelty and collective attention. Proc Natl. Acad. Sci. USA 104(45):17599–17601.

Xiaoquan Z, Lihong Z (2015) How does the internet affect the fi nancial market? An equilibrium model of internet-facilitated feedback trading. Management Inform. Systems Quart. 39(1):17–38.

Xu SX, Zhang MX (2013) Impact of Wikipedia on market information environment: Evidence on management disclosure and inves tor reaction. Management Inform. Systems Quart. 37(4):1043–1068

Yu L (2006) Understanding information inequality: Making sense of the literature of the information and digital divides. J. Librarianship Inform. Sci. 38(4):229–252.

Zhang X, Zhu F (2011) Group size and incentive to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(June):1–17.

Zhu H, Zhang A, He J, Kraut RE, Kittur A (2013) Effects of pee feedback on contribution: A field experiment in Wikipedia. CHI ’13 Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 2253–2262.
