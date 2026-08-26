---
otero_id: 15088
otero_key: "5S8W9Z2V"
title: "The “Most Popular News” Recommender: Count Amplification and Manipulation Resistance"
authors: "Shankar Prawesh; Balaji Padmanabhan"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0529"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/5S8W9Z2V/fulltext/images/9ab9bcf7c8e4ecbef1d6da85bb879874395d45e1421a686aa6b1943a10c9b95f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The “Most Popular News” Recommender: Count Amplification and Manipulation Resistance

Shankar Prawesh, Balaji Padmanabhan

To cite this article:

Shankar Prawesh, Balaji Padmanabhan (2014) The “Most Popular News” Recommender: Count Amplification and Manipulation Resistance. Information Systems Research

Published online in Articles in Advance 13 Aug 2014

http://dx.doi.org/10.1287/isre.2014.0529

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/5S8W9Z2V/fulltext/images/6d4fc58f8c0e4a656fb09e1d140a073e63faf33c22456d0a47e4c596793642b2.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The “Most Popular News” Recommender: Count Amplification and Manipulation Resistance

Shankar Prawesh, Balaji Padmanabhan College of Business, University of South Florida, Tampa, Florida 33620 {sprawesh@outlook.com, bp@usf.edu}

broad motivation for our research is to build manipulation resistant news recommender systems. There are several algorithms that can be used to generate news recommendations, and the strategies for manipulation resistance are likely specific to the algorithm (or class of algorithm) used. In this paper, we will focus on a common method used on the front page by many media sites of recommending the N most popular articles (e.g., New York Times, BBC, CNN, Wall Street Journal all prominently use this). We show that whereas recommendation of the N most read articles is easily susceptible to manipulation, a probabilistic variant is more robust to common manipulation strategies. Furthermore, for the “N most popular” recommender, probabilistic selection has other desirable properties. Specifically, the 4N + 15th article, which may have just missed making the cut-off, is unduly penalized under common user models. Small differences are easily amplified initially, an observation that can be used by manipulators. Probabilistic selection, on the other hand, creates no such artificial penalty. We use classical results from urn models to derive theoretical results for special cases and study specific properties of the probabilistic recommender.

Keywords: recommender systems; news recommendation; polya urn; zipf; power law; sampling; manipulation History: Gediminas Adomavicius, Senior Editor; Maytal Saar-Tsechansky, Associate Editor. This paper was received on January 2, 2012, and was with the authors 14 months for 3 revisions. Published online in Articles in Advance.

## 1. Introduction

Historically, mass media has played an important role in creating and sustaining mass opinion in society on issues ranging from policy, violence, new product adoption, family and health related topics (Rogers 1976, Myers 2000). Traditionally, editorial perspectives have driven decisions of what news to present to readers; media editors have therefore been in positions to form and shape opinion. However, that trend is changing with technology-driven decisions that are being used instead, or in conjunction with editorial decisions.

In the last ten years the Web has become the primary news source for many users. At the same time there has been a greater penetration of social media such as tweets, Facebook posts, and online videos (Economist 2011b). The Economist has noted that this change in news consumption behavior has “turned the news industry upside down, making it more participatory, social, diverse and partisan” (Economist 2011b, p. 3-5). Readers often volunteer to submit, share, and comment on news articles. Referrals from social networks are the fastest growing source of traffic for some news websites and, as the Economist writes, “the most popular stories cause a flood of traffic as recommendations ripple across social networks” (Economist 2011b, p. 3-5). Hence, once an article reaches a most popular list, there can be a self-reinforcing effect that can further impact its ultimate readership or influence. Figure 1 presents some variants of most popular lists displayed by popular media sites.

The focus of this research is to investigate the phenomena emerging through reader interaction with News Recommendation Systems (NRS) and to address the issue of manipulation in NRS. While little work has addressed the issue of recommender manipulation for news, this topic is important because significant public opinion in society is known to be influenced by user exposure to news. For example, Phillips (1974) studied the effect of publicity given to suicide stories and found that there was an immediate increase in suicide cases after such news was publicized.

To distort opinion, recommender systems are an easy target for manipulators. For example, Lerman (2007a) describes a Digg controversy in which a user posted an analysis proving that the top 30 users of Digg were responsible for a disproportionate fraction of the front page. The allegation was that the top users conspired to promote their own articles at the expense of other articles, leading to an increased concentration. In response, Digg modified the algorithm to devalue votes from friends. Also, there are special groups of online users known to be in existence, such as the Internet Water Army (Chen et al. 2011) who are paid to post comments, threads, and news articles. These groups are known to flood the Internet with purposeful comments and articles. Chen et al. (2011) discuss techniques to identify such manipulators from behavioral and semantic data. The implication is that by identifying and removing such users, manipulation might decrease.

Figure 1 Variants of the “Most-Popular” Recommender  
![](/api/attachments/5S8W9Z2V/fulltext/images/5b3dc7e1e0711bf37860f99f5307931c9307b0fda81682472c1b9a799af1a73a.jpg)

The susceptibility of most popular lists towards manipulation has been demonstrated by Weber (2010), Managing Editor of Newsweek. To demonstrate that these systems can be easily gamed, he had a group place a relatively old science story in the most emailed list of the New York Times. The snapshot of that event is shown in Figure 2. Article 3 was the manipulated article (Weber 2010).

These examples highlight the context of our research agenda. Furthermore, NRS, in comparison to other recommender systems, operates in a fundamentally different environment due to a constant stream of news. Such an environment needs more effective recommender systems, yet suffers from potentially easier manipulation due to several factors such as the greater use of implicit feedback mechanisms where clicks are counted as votes, sparseness in various topic categories, and current incentive mechanisms that encourage greater clicks for higher advertising revenue.

In this paper we study two very different selection mechanisms and discuss the trade-off between them. One of these mechanisms is the widely used most popular (or Top-N ) list. Note that the term Top-N is also used in the context of personalized recommender

Figure 2 A Relatively Old Science Story Being Placed in the Most Emailed List  
![](/api/attachments/5S8W9Z2V/fulltext/images/4aec0f8422a0fe67bcc2314fbb48833d92d5d6506b2757131b06c43dbd6a72f1.jpg)  
The author instructed a group of people to e-mail the highlighted article within a relatively short timeframe

Source. Weber (2010).

systems (Deshpande and Karypis 2004). Here we use it to refer to the most popular news recommender and its variants such as most e-mailed or most viewed. The other selection mechanism, a probabilistic variant, is introduced in this research.

We present our findings in two ways. First using simulation, we show that the most popular recommender is prone to artificial amplification of small differences. The 4N + 15th article, which may have just missed the cut-off, is often unduly penalized in terms of readership counts in the long run. The probabilistic variant is shown instead to be robust. The weakness of the most popular recommender can also be exploited by manipulators who seek to gain popularity for their articles. Under manipulation we show that the probabilistic mechanism is again more robust. The simulation results are based, in part, on data on popularity distribution of articles from five different local news websites. Second, building on statistical results on Pólya’s and Bernard Friedman’s classical urn models (Freedman 1965), we derive some theoretical insights for special cases. The trade-off between the Top-N NRS and the proposed probabilistic variant is discussed in terms of count distortion and information quality.<sup>1</sup> Whereas we do observe some loss of information quality in probabilistic NRS, it is robust towards minimizing artificial amplification in the counts of the recommended articles in comparison with the Top-N NRS. We present results on manipulation for the probabilistic NRS in comparison with an adapted Influence Limiter heuristic (Resnick and Sami 2007). Finally, an extension of probabilistic selection has been introduced and we demonstrate that this extended model can be used to address an interesting issue of social desirability between the Top-N and probabilistic selection mechanisms. These are all unique contributions of this paper.

The rest of the paper is organized as follows. Section 2 discusses related work. The model used in this research is described in §3, and §4 discusses the empirical and simulation results. The intuition behind the analytical modeling and the theoretical results are presented in §5.

Section 6 presents further analyses of the probabilistic NRS. In $\ S { \dot { 7 } } ,$ we address the issue of social desirability of different selection processes for NRS. Section 8 concludes with implications and discussion.

## 2. Related Work

In one of the earliest research articles in online manipulation, Dellarocas (2006) presented theoretical analysis of manipulation strategies and its impact on the firm and consumers assuming that the main source of quality information for consumers is an online product review forum. This work has established various results on the effects of online forum manipulation in a simple monopoly setting. The analysis of results shows the existence of a setting where forum manipulation is equivalent to a form of quality signaling that benefits consumers. Also, if consumers expect firms to manipulate, as the volume and quality of user-generated online content increases there will be a certain threshold beyond which firms will have to engage in profitreducing online manipulation practices. The findings from closed-form solutions have also been generalized in a wide range of multifirm settings and for a broad class of consumer utilities, firm payoff functions, and signal distributions. Finally, the paper also proposed filtering technologies that make it more costly for firms to manipulate. We take a similar approach to study NRS through simulation and develop analytical results.

Manipulation resistant recommender systems discussed in the literature and also related to our work include Resnick and Sami (2007, 2008). Resnick and Sami (2007) introduced the Influence Limiter algorithm for item recommendation, controlling rater’s influence on recommender systems through reputation acquired over time. The authors show that the optimal strategy of a rater is to induce predictions that accurately reveal the rater’s information about the item. Using an information-theoretic measure, the authors establish that the negative impact of any rater is bounded by a given limit.

In their subsequent work Resnick and Sami (2008) establishes the trade-off between resistance to manipulation by an attacker and optimal use of genuine ratings in recommender systems. A lower bound on how much information must be discarded is also provided. Lee and Zhu (2012) have studied shilling attacks detection on recommender systems and propose a two phase procedure. First, they use multidimensional scaling to identify distinct behavior and to narrow the detection space by filtering out noise profiles. In the second phase, they use a clustering based method to discriminate the attackers.

Van Roy and Yan (2010) studied linear collaborative filtering (CF) algorithms and have shown they are robust compared to the nearest neighbor algorithms widely used in commercial systems. This analysis of linear CF algorithms shows that as a user rates an increasing number of products, the average accuracy becomes insensitive to manipulated data. The authors establish bounds on distortion as a function of the percentage of manipulated data and the number of products rated by a user whose future rating will be predicted.

In particular for NRS, Largillier et al. (2010) discuss a robust voting system for social news websites based on SpotRank. Considering voting as a recommendation, Largillier et al. (2010) present a set of heuristics that demotes the effects of manipulation. SpotRank is built over ad-hoc statistical filters, a collusion detection mechanism, and the reputation of users and proposed news.

In their work they discuss several issues of social NRS such as the existence of cabals (i.e., collusion of a large group of users that vote for each other), those who try to manipulate the system using daily mailing lists, some users posting many links to flood the system, and using several IP addresses to vote for themselves. Lerman (2007b) discuss a model for the news aggregation process by Digg for news recommendation and ratings.

In the context of social influence Salganik et al. (2006) found that the presence of social influence leads to greater inequality and unpredictability in the popularity of songs. In a broader context, Easley and Kleinberg (2010) address the issue of popularity, arguing that the power law seems to dominate in cases where the quantity being measured can be viewed as any kind of popularity.

## 3. Model

We present the main findings of our study using a thought experiment implemented as a simulation. This has been a powerful tool to address various issues related to social sciences and public policy (Maroulis et al. 2010, Schelling 1971). For instance, using a thought experiment Schelling (1971) showed that a small preference for one’s neighbors to be of the same color could lead to total segregation of society. Using a similar methodology Maroulis et al. (2010) studied the survival of public schools based on individual choices.

## 3.1. Model Description

We set up the simulation model as follows. We maintain a Comprehensive List (CL) of articles and their corresponding counts (or clicks). From $C L ,$ N articles are selected for display as recommendations. Before the simulation starts articles are assigned counts in some range (e.g., between 0 and 1,000). Details about the distribution of popularity of articles are discussed in the following section. Articles are sorted in decreasing order of their initial counts and the articles with high counts are selected for the Display List (DL). Furthermore, the

4N + 15th article was deliberately assigned a count of exactly one less than the count of N th article.

The selection of articles in the DL is updated at a preselected time step, and this selection of articles is based on two different selection processes, i.e., the Top-N and probabilistic selection. The Top-N selection is a hard cut-off, which selects N articles for display corresponding to the highest counts. This is how most online news sites display the most popular or viewed articles, typically in a prominent box or sidebar.

Probabilistic selection, on the other hand, is a mechanism proposed here wherein articles are selected probabilistically based on their counts thus far. In this mechanism, every article in CL will have some probability, based on its count, to appear in DL.

Probabilistic selection of articles is based on probabilistic sampling without replacement for N articles. The probability that an article will be selected in DL is given by prob $\begin{array} { r } { ( a ) = c o u n t _ { a } / \sum _ { j } c o u n t _ { j } , } \end{array}$ , where $c o u n t _ { a }$ represents the count of an article $" a "$ at a given time step and $\textstyle \sum _ { j }$ count represents the total counts of articles not yet selected for DL.

This sampling process is repeated N times to generate the N recommendations in DL. Pseudo code for the implementation of these selection processes is discussed later in this section.

The user models we implement here are based on the notion that online users face information overload due to the vast amount of news articles available through various sources. These users face the problem of distributing their finite attention, and in this context the top-N selection mechanism presented to them provides an important cue in helping them navigate the space of articles. Users may scan the list beginning from the top article and then look for other articles until they get bored or distracted. This is consistent with recent research in social media that shows that such limited attention models can result in more accurate user models of online behavior (Kang et al. 2013).

The discussion above helped us to develop reader models to examine in this simulation. Two different reader models were implemented. In both models a user is assumed to select an article from DL with some probability p or from the remaining list RL 4= CL − DL5 with probability $1 - p .$

In the first model, a reader randomly selects an article from DL. Whereas, in the second model the top-most article in the DL has the highest probability of being selected and the bottom-most has the lowest probability, with a linear decrease in the selection probability between top-most and bottom-most articles.

For the second reader model the probability of a particular article with rank $i , i \in \{ 1 , \bar { 2 } , \dots , N \}$ in DL being read (selected) is given by $\begin{array} { r } { r _ { i } = ( N + 1 - i ) / \sum _ { i = 1 } ^ { N } i . } \end{array}$ Here, we define rank as the order in which articles are displayed in the recommended list.

For ease of exposition, the present model intentionally leaves out other complicated factors of news arrival and reader behavior based on front-page display of news websites. However, the selection mechanism of articles by readers is based on a real world distribution of article counts that gives rise to the power law distribution in popularity.

3.1.1. Implementation of NRS. Pseudo code for the simulation and probabilistic selection is presented below. (Select can be count-based or probabilistic; while Choose can be based on either of the two reader models described above.)

```txt
for each reader
    Sort the updated count and select N articles for DL
    If selected article is from DL (i.e., with probability p)
    Choose an article from DL and increase its count by 1
    else
    Choose an article from RL using Zipf distribution; (RL = CL - DL) and increase its count by 1
```

## Algorithm 1 (Probabilistic selection)

```txt
Algorithm 1 (Probabilistic selection)

The count of articles are c[1], c[2], ..., c[n]

count[1] = 0

for x = 2 to n + 1

    count[x] = count[x - 1] + c[x - 1]

end for

for y = 1 to N

    generate a random integer (R) between 0 and count[n + 1]

    determine the indices between which R lies, as (i, i + 1)

    select article corresponding to the count c[i]

    for DL

    j ← c[i]

    While (i < k ≤ n)

    count[k] = count[k + 1] - j

    end while

    n = n - 1

end for
```

## 3.2. Measures

To compare different user models and selection mechanisms we introduce two specific measures. Both are based on the counts of N th and 4N + 15th articles over the complete simulation. Both N th and 4N + 15th articles selected are based on the initial counts of articles before the simulation starts.

Measure M1. This is defined as the logarithmic-ratio of the counts of N th and 4N + 15th articles at each time-step as follows:

$M 1 ( i ) = \ln ( c o u n t _ { N i } ) - \ln ( c o u n t _ { ( N + 1 ) i } ) = \ln ( c o u n t _ { N i } /$ $c o u n t _ { ( N + 1 ) i } )$ at the ith iteration of the simulation.

This measures the relative change in the counts of N th and 4N + 15th article, hence count amplification between the articles. We chose this measure to demonstrate the fact that even if N th article barely makes it into the DL, in the count-based selection in the long run it will have significantly higher popularity than the 4N + 15th article simply by virtue of being in such a prominent list. We also use this measure to demonstrate how a manipulator can exploit the self-reinforcing nature of top-N lists. At the start of the simulation $c o u n t ( N ) \sim \hat { c o u n t } ( N + 1 )$ , hence M1405 ∼ 0.

Measure M2. This is defined as the count of the jth article divided by the total number of counts (hits) at a given time. We denote it as M2 and at the ith iteration it will be $\begin{array} { r } { M 2 ( i ) = c o u n t _ { j i } / \sum _ { k = 1 } ^ { n } c o u n t _ { k i } . } \end{array}$ . It represents the share of the counts for any particular article j in the NRS over iterations, and can be understood as a success measure of an article in a given selection mechanism. All things being equal, articles with higher market shares can be considered more successful than others.

## 3.3. Update Rule

At each time period the model proceeds as follows: One reader arrives at each time step. Upon arrival, the reader selects probabilistically to read an article either from the displayed list 4DL5 or the remaining list 4RL5 of articles. The probability of selection of an article from DL or RL is controlled in the simulation. If a reader selects an article from RL, then the selection of an article is performed according to Zipf distribution. The count of the selected article is increased by 1.

If a reader selects an article from the DL, then random selection of an article is performed for Reader Model 1 and selection of an article is performed according to probability $r _ { i }$ for the Reader Model 2. The count of the selected article is increased by 1.

For the two different NRS, count-based and probabilistic, the selection of N articles for DL is made, and the DL is updated at each time step.

## 3.4. Manipulation

To study manipulation, we assume that a manipulator can create artificial clicks to raise the counts of a selected article (for instance by creating fake IDs). These fake counts are randomly distributed over the given interval, and are created by malicious readers, who, on arrival, increase the count of a particular article by 1. The particular article selected for manipulation in the present model is the 4N + 15th, mentioned earlier in §3.1, as this is the article that would have just missed the hard top-N cut-off. Also, we study two types of manipulation, early and uniform, to examine what impact each might have. In early manipulation, the fake clicks are assumed to be distributed early in the time period; in uniform manipulation the fake clicks are uniformly distributed over the entire time interval. We also examine the extent of manipulation (high and low, based on how many fake counts are generated) and the impact it can have.

## 4. Simulation Results

In the case of news articles, where the majority of queries are driven by front page display or recommended articles, we expect popularity to exhibit some kind of power law distribution. The rationale for powerlaw distribution of popularity, especially in web-based systems, has been suggested by Easley and Kleinberg (2010). This assumption of popularity distribution is also consistent with the effect of social influence discussed by Salganik et al. (2006). In their experiment for an artificial music market, they found that in the presence of social influence such as media sites, we observe greater inequality, i.e., popular entities are more popular and unpopular entities are less popular.

From a given power-law distribution its corresponding Zipf distribution can also be obtained (Adamic 2000). Let us assume that the probability density function of power law is given by $f ( k ) = \dot { a } / k ^ { c } ,$ , for some exponent c and the constant of proportionality a. f 4k5 represents the fraction of articles that have popularity k. Cumulative distribution of power law follows Zipf’s law (Newman 2005). The Zipf’s probability mass function of an article ranked k, when the total number of articles in the system is N , is given by

$$
p (k; s, N) = \frac {1 / k ^ {s}}{\sum_ {n = 1} ^ {N} (1 / n ^ {s})}.\tag{1}
$$

In the above expression the value of s characterizes the behavior of the system. Furthermore, between a given Zipf’s distribution and its corresponding powerlaw distribution the following relation holds between the exponents $c = 1 + 1 / s$ (Adamic 2000). We will use this relationship between exponents in the simulation model.

To validate the popularity distribution of articles, we obtained data on popularity of articles from DailyMe Inc., a company that provides news personalization technology to a large number of media sites. There are five data sets from five different local news websites serving markets in Connecticut, Pennsylvania, New York, Colorado, and Massachusetts, collected from February 2012 to April 2012. The data listed specific articles along with cookie IDs and time stamps across the five different local news websites.

## 4.1. Empirical Analysis of Popularity Distribution of Articles

Figure 3 depicts the histogram plot for the popularity of articles on each of the five sites. In all cases popularity distribution is L-shaped. The X axis is article counts, binned in intervals of width 100. The Y axis is the number of news articles in the period that have the corresponding count.

Figure 3 Distribution of the Number of Articles Receiving a Given Number of Counts  
![](/api/attachments/5S8W9Z2V/fulltext/images/bc951fb2a447c53c4b747d49e41814c8a9f418741df23029088fe1aa4e51cb44.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/5e217c0f1725aebcedec167112ec27ef4cb36dbc1f79cc93366997d875fee41b.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/b30e2fadb3f0a1872aa30faa00052aedf0f5ab6bc348c7370b22c7ff69eda712.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/91ce0c41d2c4e46611282414fc8833caab724733305dda399325c81081a852ac.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/392f43b30a6846dacc32728c852b30462c8dcb83be66bf3c4b32a76ea7909684.jpg)  
Notes. The X -axis has been binned in the intervals of length 100. The Y -axis corresponds to the number of articles falling in that range.

We further plotted the normalized frequency distribution on log–log scale using the logarithmic binning with a multiplier of 2. This is similar to the procedure described by Newman (2005). Findings in this case are provided in Figure 4, with the slope of curves. The X-axis corresponds to the natural log value of bins and the Y -axis corresponds to the natural log value of normalized frequencies.

Data from these five local news websites show the pattern of power law in popularity. Based on our findings, and the value of the exponent for commonly occurring power-law distributions in nature<sup>2</sup> (Newman 2005), we choose the exponent that is close to the average of the power-law exponents of the five different sites but slightly higher. In particular, we use c = 107 (s = 1045 as the power-law exponent to discuss results in the simulation model. We use the power-law distribution with exponent 1.7 to generate the initial distribution of article counts in the simulation. Note that these are relatively smaller local news websites and we do not therefore make broader generalizations about the power law based on these alone. However, the results provide valuable insights for the simulation results.

## 4.2. Simulation Setup

The analyses of our results are separated into two sections: (1) without manipulation, and (2) with manipulation. The simulation results for without manipulation explain the phenomenon that emerges using different NRS based on different selection mechanisms. In particular, we compare the two measures M1 and M2 for N th and 4N + 15th articles and discuss findings based on them. We introduce manipulation to demonstrate the susceptibility of the Top-N NRS to certain types of attacks and the robustness of the proposed probabilistic NRS as an alternative. Manipulation has been introduced in two stages to study the effects of early manipulation and manipulation over a large period of time. In the first case, the manipulated counts are distributed uniformly between the time stamps 0 and 100 and in the second case manipulated counts are distributed uniformly between the time stamps 0 and 2,000. We consider different scenarios based on (a) the reader models (two), (b) the existence of manipulation (two), and (c) the selection mechanism (two: count-based and probabilistic) as described in the tree in Figure 5. The leaves of the tree correspond to specific simulation scenarios. As Figure 5 shows, there are 12 leaves for some specific choice of global simulation parameters.

Figure 4 Log–Log Plot for Popularity of Articles at Five Different Sites  
![](/api/attachments/5S8W9Z2V/fulltext/images/4a86b3e755cbe35bcd7b9cdfe54847cf1a5ef5a5dddb1f99cae031fffd3c1e43.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/426fb6e16d11ad25bbf4047dfda17f26513a32be95018bbe556435fd0c527316.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/a70e62cd0a8126b39b60e92cc2f9fd8e3adeab47feba723d1abb98bbb3c14a4d.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/f81689193ff539719e27e446f2f01c03d6f316d3c8ca499399dfcbf34a10794b.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/4434ce147447641996a09a6517a2eae8c83585cf551958b01b367158e50f264e.jpg)

Two of the global simulation parameters are (1) probability of a reader selecting an article from DL (varied as 0.9, 0.5, 0.25, 0.1), and (2) the extent of manipulation (high or low, implemented in the simulation as manipulated counts). The value of simulation parameters used is listed in Table 1. For any specific choice of these two parameters we have 12 graphs in the results (corresponding to the 12 leaves of the tree).

Though we considered different selection probabilities from the DL, in the context of the present research we have developed our discussion for a case of influential $( p = 0 . 9 )$ NRS (the different simulation paths in the graphs are better seen in color). While the probabilities of article selection from Top-N recommended lists are generally not known, and may also be specific to each media site, this special case is interesting because it captures a setting in which NRS particularly influence readership.

The discussion here on simulation results is based on findings from multiple runs of the simulation model. For illustration, the figures below show sample paths corresponding to specific runs of the simulation.

## 4.3. Results Without Manipulation

We summarize our findings based on the measures M1 and M2 through selected simulation scenarios. The selected simulation results are presented in Figures 6–11, where left panels are for the M2 measure while the right panels are for the M1 measure. The list of various abbreviations used in these figures is given in Table 2. In all figures, the X-axis corresponds to time steps in the simulation (which corresponds to increasing number of clicks received by articles), and the Y -axis corresponds to values of the measures M1 or M2.

Figure 5 Scenarios for Specific Selection of Global Parameters  
![](/api/attachments/5S8W9Z2V/fulltext/images/2145cbe4ac3c2c60752451cf311e2f647f1299deb600359baa091df3dc4bc117.jpg)

When there is a high probability that a reader will click on the article recommended by the NRS (or DL), even a negligible initial difference between the counts of N th and 4N + 15th article is heavily amplified in the count-based NRS, as it is evident from the consistently increasing pattern of M1\_count in Figures 6 and 7 for both reader models. For the probabilistic selection mechanism, the value of M1\_p remains close to its initial value (Figures 6 and 7). Furthermore, the extent of amplification in reader model-1 is much higher than the reader model-2.

The path followed by M2 for N th and 4N + 15th articles in the probabilistic NRS (for both reader models) stays close to its initial value, whereas in the case of hard cut-off we observe a consistent increasing and decreasing pattern for the N th and the 4N + 15th article, respectively. In other words, for the count-based NRS the difference in share between the displayed (M2\_d)

Table 1 The Model Parameters Used in the Simulation

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>No. of readers</td><td>2,000</td></tr><tr><td>No. of articles in DL</td><td>10</td></tr><tr><td>No. of articles in CL</td><td>200</td></tr><tr><td>Initial counts of  $articles^a$ </td><td>Random integer between 0 and 1,000 generated using Zipf distribution with exponent 1.4</td></tr><tr><td>Manipulation counts</td><td>10 and 50</td></tr><tr><td>Probability of selection of an article from DL (p)</td><td>0.9, 0.5, 0.25, 0.1</td></tr></table>

<sup>a</sup>Except Nth and 4N + 15th articles. Counts for these articles were assigned such that count 4N + 15 = count 4N5 − 1. This was done deliberately to test how the hard cut-off treats very small initial differences in quality between articles.

and nondisplayed (M2\_u) article shows a consistent increasing pattern even though the initial difference between displayed and nondisplayed article was negligible (recall that the only difference between the N th and 4N + 15th article was a single count). This observation highlights the issue of inequality in future success of articles created due to the presence of the hard cut-off NRS.

In a natural system we expect that the share of counts for articles that are almost identical will not vary much. Hence these findings suggest that popular mechanisms using hard cut-offs may be susceptible to fundamentally creating, or amplifying, differences that may be undesirable. Probabilistic selection, on the other hand, is a robust mechanism from this perspective. Another way of looking at this might be that the top-N selection is prone to amplifying naturally occurring errors in the ranking of articles given the self-reinforcing behavior it facilitates.

## 4.4. Results with Manipulation

In this section we will discuss the effect of different manipulation scenarios on both kinds of NRS. Manipulation counts are uniformly distributed over initial 100 (early manipulation) and over the entire 2,000 article counts (uniform manipulation). Two manipulation counts considered are 10 (low) and 50 (high) when the system is slightly and heavily manipulated. In total we have four different scenarios of manipulation.

• Low fake counts uniformly distributed early.

Table 2 Abbreviations Used in the Figures

<table><tr><td>M2_d</td><td>M2 for the Nth article in Top-N NRS</td></tr><tr><td>M2_u</td><td>M2 for the (N+1)th article in Top-N NRS</td></tr><tr><td>p_M2_d</td><td>M2 for the Nth article in probabilistic NRS</td></tr><tr><td>p_M2_u</td><td>M2 for the (N+1)th article in probabilistic NRS</td></tr><tr><td>M1_count</td><td>M1 for Nth and (N+1)th article in Top-N NRS</td></tr><tr><td>M1_p</td><td>M1 for Nth and (N+1)th article in probabilistic NRS</td></tr><tr><td>p</td><td>Represents the probability that an article will be read from the DL</td></tr></table>

Figure 6 Simulation Results for the User-Model 1 Without Manipulation 4p = 0095  
![](/api/attachments/5S8W9Z2V/fulltext/images/d1fff0e3dab9db8c212c32f01f7501dfe387d07aedf7950577ead9da5e03358c.jpg)

• Low fake counts uniformly distributed over the entire process.

• High fake counts uniformly distributed early.

• High fake counts uniformly distributed over the entire process.

First we will discuss the findings of low manipulated counts. For the 4N + 15th article in RL its count was randomly increased by 10, but early in the process. However, findings in this case were completely reversed from the findings in nonmanipulated systems, as the reversal of the M1 paths in the right panel of Figures 8 and 9 shows.

Figure 8 presents the case of user model with random selection of articles from the top-10 list. Both measures M1 and M2 (Figure 8) suggest that the difference in count for the manipulated 44N + 15th) and the nonmanipulated article (N th) is amplified even if genuine readers access the system. For the second user model, in which selection of an article is based on $r _ { i } ,$ the count amplification phenomenon is again observed, but to a lesser extent (Figure 9).

This suggests that, for the case of the most popular NRS mechanism, once a manipulator is successful in getting his article on the DL, the implicit feedback mechanism of count-based NRS will help the manipulated article to gain more counts as more readers gain access to the system. Because of this characteristic of the Top-N NRS, manipulators need invest little time to increase the counts of a particular article to make it appear on the $D L ,$ , after which no further manipulation may be required.

![](/api/attachments/5S8W9Z2V/fulltext/images/78ffd87210c5170f0c9729bf99bebc4f3102160660dd32b80d9377c9eca17c99.jpg)

However, for the probabilistic NRS, manipulation seems to have little or no effect (Figures 8 and 9). For low fake counts distributed uniformly the findings are similar to the case of nonmanipulated count-based and probabilistic NRS (similar to Figures 6 and 7). This suggests that a manipulation strategy may not be successful if the effort of a manipulator is distributed over a large period of time.

We used the second manipulation strategy with high fake counts to compare the performance of both NRS when the system is heavily attacked by manipulators. In the first case, 50 counts are randomly distributed over the first 100 counts, i.e., the system is heavily manipulated in the early stage. The benefit of probabilistic NRS is very pronounced (Figures 10 and 11). Probabilistic NRS shows stable results in which M1 and M2 are not amplified after the manipulation, whereas the performance of count-based NRS is highly distorted for high probability of selection of articles from the DL, as shown by the declining M1\_count trajectory (Figure 10). In the second reader model, when top ranked recommended articles receive higher attention, successful manipulation activity in the most popular NRS requires substantially more clicks to maintain the higher popularity of the target article (Figure 11). For example in Figure 11 (right panel), even in the case of heavy early manipulation, though the downward trend of M1 still continues, results do not appear to be as encouraging for a manipulator as in the case of uniform distribution (Figure 10). In both reader models, for the 50 fake counts distributed over 2,000 counts, the differential benefit of manipulation for Top-N selection compared to the nonmanipulated case was negligible, as the manipulation effort was distributed over a large period of time.

Figure 7 Simulation Results for the User-Model 2 Without Manipulation 4p = 0095  
![](/api/attachments/5S8W9Z2V/fulltext/images/8b7bf7bef0db5d66e27d3f0ba6bc862f1f72a3ec6e9d31d9821f0f42653c1e5f.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/701efa40d3bfbde83509af9bc1ef5662b67898b1889d395cae5ee062c3ca923e.jpg)

Figure 8 Simulation Results for the User-Model 1 with Little Early Manipulation 4p = 0095  
![](/api/attachments/5S8W9Z2V/fulltext/images/76291c11daca27129915749da50212118de599d816ac44cc11eabdc19c28c0ee.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/8169fc58c4795faa27629755ce7c9837bf4033bd0774c419953ac01d9e188de7.jpg)

Figure 9 Simulation Results for the User-Model 2 with Little Early Manipulation 4p = 0095  
![](/api/attachments/5S8W9Z2V/fulltext/images/e30c22c54754ddab42f3b888d465d03f13b81c13fb7bb229462f8bc19e3e7f5c.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/e06868e40e6b4ab3c0b1b858f930b5e90392272202e751d55722dbf7c4aaeda7.jpg)

Figure 10 Simulation Results for the User-Model 1 with Heavy Early Manipulation 4p = 0095  
![](/api/attachments/5S8W9Z2V/fulltext/images/70e5d36e7b0b347b930bf3d5629d65693f9f3de52852cc271c4ebf1573170744.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/6c9c626a5e56f4f51e1876e482598fa12cfba451997916bdd1fdd4ee845adaf6.jpg)

Figure 11 Simulation Results for the User-Model 2 with Heavy Early Manipulation 4p = 0095  
![](/api/attachments/5S8W9Z2V/fulltext/images/89ed9df7ccc2500df2299f209beee62bb8ed6beadc301f2f6e3927afd5b1d209.jpg)

![](/api/attachments/5S8W9Z2V/fulltext/images/e59ed67118d3cbf86cfce0378eedd643b88a8115c7ccfebfc9550700a33882ef.jpg)

## 5. Analytical Results

To understand how easily amplification can happen for hard cut-off NRS and the robustness of probabilistic NRS toward amplification, we present insights on processes generated through both NRS in a simple setting of a two article case. For illustrative purposes, the following discussion (in §5.1) provides an intuitive explanation of the phenomenon for a single time step. Section 5.2 and the appendix extend this idea and presents theoretical results for any n time steps.

## 5.1. Assumptions

1. Two articles are available for readers recommendation (article-a and article-b).

This assumption helps us to establish the analogy between NRS and urn models.

2. Reader on arrival reads the recommended article with probability p or reads the other with probability $1 - p .$

3. The natural counts for article-a and article-b at time t = 0 are given by $n _ { 0 }$ and $m _ { 0 }$ respectively.

The natural counts can be interpreted as overall readers preferences for these two articles before any recommender was put in place. Further, without loss of generality, we assume $n _ { 0 } > m _ { 0 }$

## 5.2. Illustration

Let us denote the initial share of article-a and article-b by $p _ { a }$ and ${ \mathit { p } } _ { b } ,$ respectively, and they are (initial share) given by $n _ { 0 } / ( n _ { 0 } + m _ { 0 } )$ and $m _ { 0 } / ( n _ { 0 } + m _ { 0 } )$ . In this simple one time period model the NRS results in amplification of the count of recommended article if at the next step due to recommendation $E ( p _ { a } ) > n _ { 0 } / ( n _ { 0 } + m _ { 0 } )$

5.2.1. Count-Based NRS. The probability of the recommended article being read is given by p. In the hard cut-off NRS, article-a is always recommended since it has the higher count. Hence, any reading probability $p > n _ { 0 } / ( n _ { 0 } + m _ { 0 } )$ will result in amplification of the counts for the recommended article. Consider a case wherein $n _ { 0 } \sim m _ { 0 } , { \bf e . g . } , n _ { 0 } = m _ { 0 } + 1 ;$ hard cut-off NRS will be susceptible to amplification if $p > 0 . 5$ Given the two article case we expect $p$ to be greater than 0.5 for the recommended article.

5.2.2. Probabilistic NRS. In probabilistic NRS, article-a can be read in two ways. The article is in the recommended list (with probability $p _ { a } )$ and the reader chooses to read the recommended article (with probability p5; or article-a can be in the other list RL (with probability $1 - p _ { a } )$ and the reader chooses to read the unrecommended article (with probability $1 - p )$

The total probability that an article-a will be read is therefore given by

$$
p (r e a d) = p \cdot p _ {a} + (1 - p) \cdot (1 - p _ {a}).
$$

So, in case of probabilistic NRS the amplification will happen for the recommended article if

$$
\begin{array}{r l} & p \frac {n _ {0}}{n _ {0} + m _ {0}} + (1 - p) \frac {m _ {0}}{n _ {0} + m _ {0}} > \frac {n _ {0}}{n _ {0} + m _ {0}} \\ & \quad \Longleftrightarrow \quad m _ {0} + p (n _ {0} - m _ {0}) > n _ {0} \\ & \quad \Leftrightarrow \quad p (n _ {0} - m _ {0}) > n _ {0} - m _ {0}. \end{array}
$$

The above condition will never be true for any probability $p .$ It is easy to see that when the counts are similar, the probabilistic NRS does not create amplification (reading probabilities will both be 0.5).

Below we present results for the general case wherein we examine counts at the end of n iterations.

## 5.3. NRS Properties

<sup>Proposition</sup> <sup>1.</sup> In the Top-N NRS total expected count (denoted as $E ( A _ { n } ^ { h } ) )$ for article-a after n iterations is given by $( n _ { 0 } + n p )$

<sup>Proposition</sup> <sup>2.</sup> In the probabilistic NRS total expected count (denoted as $E ( A _ { n } ^ { p } ) )$ for article-a after n iterations is bounded by the interval $( I _ { 1 } , I _ { 2 } )$ . Where $I _ { 1 } = ( ( n _ { 0 } + m _ { 0 } - 1 ) /$ $( n _ { 0 } + m _ { 0 } + n - 1 ) ) ( ( n _ { 0 } - m _ { 0 } ) / 2 ) + ( n _ { 0 } + m _ { 0 } + n ) / 2$ and

$$
I _ {2} = \frac {n _ {0}}{n _ {0} + m _ {0}} (n _ {0} + m _ {0} + n).
$$

We discuss the implications of these propositions in §5.3.1. First, we briefly comment on the proofs (presented in the appendix). We use a simple binomial process to establish Proposition 1. Whereas for Proposition 2, we use modeling based on an urn framework from probability theory.

To our knowledge, the only prior work that has used urn models in the context of recommender systems is Fleder and Hosanagar (2009) where they study the impact of recommender systems on sales diversity. However, our use of Pólya’s and Bernard Friedman’s urn models to derive analytical results is novel and our analytical results have been established in a substantially different manner. Below we discuss our use of these urn models in the proofs.

The probability of article-a being recommended in probabilistic NRS is given by $p _ { a t . }$ , where $p _ { a t }$ represents the share of the article-a at any given time $t ;$ initially we have $p _ { a 0 } > p _ { b 0 }$ (Assumption 3).

For $t > 0$ the total probability of the article-a being read at time t in probabilistic NRS is

$$
p _ {t} (r e a d) = p \cdot p _ {a t} + (1 - p) \cdot (1 - p _ {a t}).\tag{2}
$$

Each time an article is read its count is increased by 1. We also define two parallel processes that start with the same initial condition. However, for these processes reading probabilities $( \mathrm { i . e . , } p )$ for the recommended article is given by 0 and 1, respectively, at each time step.

We denote reading probabilities for these processes at each time step as

$$
p _ {t l} (r e a d) = 1 - p _ {a t},\tag{3}
$$

$$
p _ {t u} (r e a d) = p _ {a t}.\tag{4}
$$

Let us denote the count of article-a being $A _ { n } ^ { p } , A _ { n l } ^ { p } ,$ and $A _ { n u } ^ { p }$ after n time steps for the processes defined by Equations (2)–(4), respectively. Suppose, for example, $\tau _ { n }$ denotes the total counts of articles in the system at any given time n. The value of $\tau _ { n }$ at a given time n is known a priori and is equal to $n _ { 0 } + m _ { 0 } + n$

Since $p _ { t l } ( r e a d ) \leq p _ { t } ( r e a d ) \leq p _ { t u } ( r e a d )$ , the following relation holds for the processes defined by Equations (2)–(4)

$$
E (A _ {n l} ^ {p}) \leq E (A _ {n} ^ {p}) \leq E (A _ {n u} ^ {p}).\tag{5}
$$

$E ( A _ { n l } ^ { p } ) , E ( A _ { n u } ^ { p } )$ are the values of $I _ { 1 }$ and $I _ { 2 }$ respectively, mentioned in Proposition 2; that will be derived in this section based on the urn formulation.

Before that, however, we present the urn problem as described by Bernard Friedman (Freedman 1965). An urn contains $W _ { n }$ white balls and $B _ { n }$ black balls at time n. One ball is drawn at random and then replaced, while  balls of the same color as the ball drawn and the $\beta$ balls of the opposite color are added to the urn. Now, let us consider two cases that will be used in the present research.

Case 1: $\beta = 0$ describes the Pólya urn mechanism in the above section where selection probability of a white ball (and vice versa for a black ball) at each time step is given by its share, a characteristic of the problem proposed by Pólya to model contagion (Eggenberger and Pólya 1923). When $p _ { t } ( r e a d ) = p _ { a t }$ (i.e., share of the article $^ { a ) , }$ the path followed by $A _ { n } ^ { p }$ is obtained through the Pólya urn mechanism with $\alpha = 1$

Case 2: The special case of Friedman’s urn with $\alpha = 0 , \beta = 1$ helps us to establish lower bound for $E ( A _ { n } ^ { p } )$ In this case the selection probability of a ball is given by 1-(share of a ball in the urn). When $p _ { t } ( r e a d ) = \bar { ( 1 - p _ { a t } ) }$ (i.e., 1-{share of the article a}), the path followed by $A _ { n } ^ { p }$ is obtained through a special case of Friedman’s urn formulation described here.

Figure 12 depicts the urn processes. The proofs of the propositions are completed in the appendix.

5.3.1. Implications. From Propositions 1 and 2 we have $E ( A _ { n } ^ { h } ) = n _ { 0 } + n \cdot p$ and

$$
\begin{array}{c} \frac {n _ {0} + m _ {0} - 1}{n _ {0} + m _ {0} + n - 1} \frac {n _ {0} - m _ {0}}{2} + \frac {n _ {0} + m _ {0} + n}{2} \\ \leq E (A _ {n} ^ {p}) \leq n _ {0} + \frac {n _ {0}}{n _ {0} + m _ {0}} n. \end{array}
$$

## Figure 12 The Two Urn Models

![](/api/attachments/5S8W9Z2V/fulltext/images/408835576af9eeabf256ecbf07e62b4bdcb5a7349f2415776733295384eff993.jpg)  
The Pólya urn

![](/api/attachments/5S8W9Z2V/fulltext/images/ebb0f2696262635ce3770c19670fbcea12bb120af8b8c4edb4dc3ef1346adde4.jpg)  
A Bernard Friedman urn

Now consider a case wherein NRS has fairly strong influence on reading behavior, $\mathrm { i . e . , } p \sim 1$ and the difference in the sufficiently large natural counts after which articles a and b make in NRS is negligible, i.e., $n _ { 0 } - m _ { 0 } \sim 0$ . In particular let us assume $n _ { 0 } = m _ { 0 } + 1$ . So, the approximate value of expected count of article-a in hard cut-off NRS and probabilistic NRS is given by

$$
E (A _ {n} ^ {h}) = m _ {0} + 1 + n,\tag{6}
$$

and

$$
\begin{array}{c} \frac {m _ {0}}{2 m _ {0} + n} + \frac {2 m _ {0} + n + 1}{2} \leq E (A _ {n} ^ {p}) \\ \leq m _ {0} + 1 + \frac {m _ {0} + 1}{2 m _ {0} + 1} n. \end{array}\tag{7}
$$

An increase in the counts of Top-N selection and probabilistic selection NRS due to recommendation can be obtained by subtracting the initial count of article-a in expressions (6) and (7). So, we have

$$
E (A _ {n} ^ {h}) - (m _ {0} + 1) = n,\tag{8}
$$

and

$$
\frac {m _ {0}}{2 m _ {0} + n} + \frac {n - 1}{2} \leq E (A _ {n} ^ {p}) - (m _ {0} + 1) \leq \frac {m _ {0} + 1}{2 m _ {0} + 1} n.\tag{9}
$$

Using approximation $( ( m _ { 0 } + 1 ) / ( 2 m _ { 0 } + 1 ) ) \sim \frac { 1 } { 2 }$ in expression (9) for sufficiently large m gives us the following condition:

$$
\frac {m _ {0}}{2 m _ {0} + n} + \frac {n}{2} - \frac {1}{2} \leq E (A _ {n} ^ {p}) - (m _ {0} + 1) \leq \frac {n}{2}.\tag{10}
$$

For large n, from (8) and (10)

$$
E (A _ {n} ^ {h}) - (m _ {0} + 1) \rightarrow n \quad \text { and } \quad E (A _ {n} ^ {p}) - (m _ {0} + 1) \rightarrow \frac {n}{2}.
$$

${ \mathrm { S o } } ,$ from the above expressions we conclude that for two equally good articles, probabilistic NRS is less susceptible to artificial amplification in counts for the recommended article, whereas hard cut-off

![](/api/attachments/5S8W9Z2V/fulltext/images/5dfaf71eedc60ab7a92fbef0b6ebeb71f2ba39efaecd4ca8e3fa767bcc81708a.jpg)  
NRS generates processes that lead to highly amplified counts for the recommended article when the NRS is fairly influential $( p$ is very high). This is the case since two articles with the same counts should initially increase their respective counts by $\sim n / 2$ at the end of n iterations. This happens with the probabilistic mechanism only.

## 5.4. NRS Manipulation

Proposition 3 (Effectiveness of Early Manipu-<sup>lation).</sup> Consider two scenarios in which an article is manipulated once at two different time steps $t _ { 1 }$ and $t _ { 2 }$ such that $t _ { 1 } < t _ { 2 } ( t _ { 1 } , t _ { 2 } < n , t _ { 0 } = 0 )$ for any NRS; where n represents the total number of new counts for both articles over the entire time. We call these manipulation strategies Ma1 and Ma2. Then for any NRS (Top-N or probabilistic) Ma1 will be more beneficial for a manipulator than Ma2.

<sup>Proof.</sup> By contrast, let us assume that (late) manipulation at $t _ { 2 }$ will be more beneficial for a manipulator than $t _ { 1 }$ . Then we can find a new time point $t _ { 0 } ^ { * } = t _ { 2 } - t _ { 1 }$ such that $t _ { 3 } > t _ { 2 }$ and $t _ { 3 } = t _ { 2 } + ( t _ { 2 } - t _ { 1 } ) = 2 t _ { 2 } - t _ { 1 }$ which will be more beneficial for manipulation than implementing manipulation at $t _ { 2 }$ and hence also from $t _ { 1 }$ (difference between $t _ { 0 } ^ { * }$ and $t _ { 2 }$ is $t _ { 1 } )$ . Applying the same argument again we obtain a time point $t _ { 0 } ^ { * } = 2 t _ { 2 } - t _ { 1 } -$ $t _ { 1 } \stackrel { - } { = } 2 t _ { 2 } - 2 t _ { 1 }$ such that $t _ { 4 } > t _ { 3 }$ and $t _ { 4 } = 3 t _ { 2 } - 2 t _ { 1 }$ will be more beneficial for manipulation than implementing manipulation at $t _ { 3 }$ and hence from $t _ { 1 } .$ . In general, we find an integer $m > ( n - t _ { 2 } ) / ( t _ { 2 } - t _ { 1 } )$ such that applying the above argument m times gives us a time point $t _ { m } > n$ that will be beneficial for manipulation. Hence under the above assumptions a manipulator will get maximum benefit without introducing any manipulated count in the system. This cannot be the case since the act of manipulation in this model provides a strictly higher count for the article being manipulated and is assumed to have no additional cost to the manipulator. Hence, by contrast, the proposition holds.

To examine the bounds for both Top-N and probabilistic NRS we consider a case wherein manipulation is introduced in both NRS at a very early stage. Let both NRS operate until n total new counts are received in the system. At extreme if all  fake counts are introduced consecutively at the very early stage, then the total count of article-b after manipulation will be $m _ { 0 } + \epsilon$ Further assume that manipulation  introduced in the system is such that $( m _ { 0 } + \epsilon ) > n _ { 0 } .$ . After manipulation both NRS can be viewed to operate as genuine NRS but with distorted initial counts $n _ { 0 } , \left( m _ { 0 } + \epsilon \right)$ for article-a and article-b respectively.

<sup>Proposition</sup> <sup>4.</sup> For a manipulator who injects  fake counts in the probabilistic NRS the increase in counts $o f$ article-b after manipulation is bounded by $( ( m _ { 0 } + \epsilon ) / ( n _ { 0 } +$ $m _ { 0 } + \epsilon ) ) ( n - \epsilon )$ where n is the total number of new counts for both articles over the entire time.

<sup>Proof.</sup> We denote the distorted share of article a and b at time t after injection of manipulation as $p _ { a t } ^ { \prime }$ and $p _ { b t } ^ { \prime } ,$ respectively. Clearly $p _ { b t } ^ { \prime } > p _ { a t } ^ { \prime }$ and probability that the article b will be read at time t will have the following property:

$$
\begin{array}{l} p _ {b t} ^ {\prime} (r e a d) = p \cdot p _ {b t} ^ {\prime} + (1 - p) \cdot (1 - p _ {b t} ^ {\prime}), \\ p _ {b t} ^ {\prime} (r e a d) \leq p _ {b t} ^ {\prime}. \end{array}\tag{11}
$$

Let us denote the count of article b being $B _ { n } ^ { \prime p }$ and $B _ { n u } ^ { \prime p }$ after n time steps $( \mathrm { i } . \mathrm { e } . , n - \epsilon$ time steps after manipulation) for the processes where $p _ { b t } ^ { \prime } ( r e a d )$ is given by $\{ p \cdot p _ { b t } ^ { \prime } + ( 1 - p ) \cdot ( \bar { 1 } - p _ { b t } ^ { \prime } ) \}$ and $p _ { b t } ^ { \prime } .$ , respectively. For these processes the expected count of article b after n time steps satisfies the following relation:

$$
E (B _ {n - \epsilon} ^ {\prime p}) \leq E (B _ {n - \epsilon u} ^ {\prime p}).\tag{12}
$$

For the random processes when $p _ { b t } ^ { \prime } ( r e a d ) = p _ { b t } ^ { \prime } ~ ( \mathrm { i . e . , }$ $p = 1 )$ , the path followed by the count of article-b is similar to the Pólya’s urn mechanism as discussed earlier in §5.3. Yet, in the present case the initial count of article a and b has been changed to $n _ { 0 }$ and $m _ { 0 } + \epsilon$ The expression for $E ( B _ { n - \epsilon u } ^ { \prime p } )$ can be similarly obtained as discussed in the appendix (for Proposition 2) to obtain the upper bound $( \mathrm { i } . \mathrm { e } . , I _ { 2 } )$ . So,

$$
E (B _ {n - \epsilon u} ^ {\prime p}) = (m _ {0} + \epsilon) + (n - \epsilon) \frac {m _ {0} + \epsilon}{n _ {0} + m _ {0} + \epsilon}.\tag{13}
$$

Using the inequality (12) and the result (13)

$$
E (B _ {n - \epsilon} ^ {\prime p}) - (m _ {0} + \epsilon) \leq \frac {m _ {0} + \epsilon}{n _ {0} + m _ {0} + \epsilon} (n - \epsilon).\tag{14}
$$

<sup>Corollary</sup> <sup>4.1.</sup> When the distorted initial counts of articles a and b are $n _ { 0 } , m _ { 0 } + \epsilon$ respectively, the increase in the expected count of article-b after manipulation in hard cut-off NRS is equal to 4n − 5 · p where n is the total number of new counts of both articles over the entire time.

The above result can be established with the simple binomial model used in Proposition 1 over $n - \epsilon$ time steps with $B _ { n } ^ { \prime h } = ( m _ { 0 } + \epsilon )$ initially. Let $B _ { n } ^ { \prime h }$ represent the total count of article-b after nth iteration in the hard cut-off NRS. Then

$$
E (B _ {n} ^ {\prime h}) = m _ {0} + \epsilon + (n - \epsilon) \cdot p.\tag{15}
$$

5.4.1. Implications. When NRS has fairly strong influence on reading behavior, i.e., $p \sim 1$ a manipulator can drive the majority of the reader’s attention towards the manipulated article as illustrated in expression (15) $E ( B _ { n } ^ { \prime h } ) - \bar { ( } m _ { 0 } + \epsilon )  n - \epsilon$ for any  that satisfies the condition $( m _ { 0 } + \epsilon ) > n _ { 0 }$

To illustrate this, consider a special case wherein $n _ { 0 } = m _ { 0 } + 1$ . For this condition by injecting any fake count $\epsilon > 1$ , e.g.,  = 2 initially, the hard cut-off NRS can be rigged. Whereas, in the case of probabilistic NRS, $E ( B _ { n - \epsilon } ^ { \prime \prime ^ { - } } ) - ( m _ { 0 } + \epsilon ) \le ( ( m _ { 0 } + \epsilon ) / ( \tilde { n _ { 0 } + } m _ { 0 } + \epsilon ) ) ( n - \epsilon ) ,$ and hence its performance is not disturbed by small manipulation efforts, as for a small value of  the expression in (14) can be approximated as $\sim n / 2$ for large n.

Hence in a special case we show analytically that (1) early manipulation can pay off well for a manipulator, and (2) this is true only for the Top-N recommender, as the probabilistic mechanism is shown to be robust against such manipulation.

## 6. Analysis of Probabilistic NRS

In this section we further analyze probabilistic NRS in two ways. First, we present and discuss an accuracydistortion trade-off. Then we compare it to a novel adaptation of the Influence Limiter algorithm.

## 6.1. Comparison of News Recommender

Systems—The Accuracy/Distortion Trade-off Accuracy 4MAE5. One drawback of the probabilistic recommendations is that it potentially chooses articles to recommend that might not be on the current best list. To quantify that loss in the recommendation process, the Top-N and the probabilistic NRS are compared based on the quality (measured as popularity) of the articles appearing on the recommended list.

To quantify the loss due to probabilistic recommender, both selection mechanisms were implemented in parallel for a given choice of simulation parameters. We express the accuracy loss in terms of mean absolute error (MAE). This is an efficient means of measuring the statistical accuracy of predictions of articles appearing in the Top-N recommendation (Ziegler et al. 2005). We assume zero accuracy loss in the case of top-N recommender, the counts of which are assumed to be the ground truth to operationalize the MAE metric. Hence, a low MAE value shows that the articles corresponding to highest counts receive more viewership through probabilistic selection mechanism and vice-versa for the articles corresponding to low counts.

Let us denote the count of ith article appearing in count-based NRS at jth time step as $\hat { N } _ { i j } ^ { h }$ and in probabilistic NRS as $N _ { i j } ^ { p }$ . The accuracy metric at time $j ,$ denoted as $| E | _ { j }$ is defined as

$$
| E | _ {j} = \frac {\sum_ {i} N _ {i j} ^ {h} - \sum_ {i} N _ {i j} ^ {p}}{\sum_ {i} N _ {i j} ^ {h}}.
$$

In the above expression $\textstyle \sum _ { i } N _ { i j } ^ { h }$ and $\textstyle \sum _ { i } N _ { i j } ^ { p }$ represent the sum of the counts of all articles that appear in DL for the count-based and the probabilistic NRS, respectively, at the jth time step. As the simulation progresses, the accuracy metric has been averaged over the number of iterations to obtain MAE

$$
| \bar {E} | = \frac {1}{| t |} \sum_ {j = 1} ^ {t} \frac {\sum_ {i} N _ {i j} ^ {h} - \sum_ {i} N _ {i j} ^ {p}}{\sum_ {i} N _ {i j} ^ {h}}.\tag{16}
$$

This metric presents accuracy loss in terms of high ranked articles assuming that users will have little or no interest in the low ranked articles, averaged over the complete simulation.

Distortion 4KL5. Assuming that the initial share of articles represents the true readers preference, the distortion created by each NRS compared to their initial share is given by the Kullback-Leibler (KL) distortion measure (Kullback and Leibler 1951). Let us denote the probability distribution for articles in each NRS (probabilistic and Top-N NRS) at the iteration t as $q _ { t } ( x _ { i } )$ Then the KL distortion for the articles $\left\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \right\}$ is given by

$$
D _ {K L} (p \mid | q _ {t}) = \sum_ {i = 1} ^ {n} p (x _ {i}) \ln \frac {p (x _ {i})}{q _ {t} (x _ {i})}.\tag{17}
$$

In other words, the above expression represents the inefficiency of distribution $q$ when the true distribution of articles is $p$ (given initially).

Because the emergence of counts of the articles in a given NRS is a probabilistic process, the data was generated through 15 replications of the complete simulation for the different values of reading probabilities for both reader models. The results discussed below are based on the mean value of metric over 15 replications, plotted against different choices of the reading probabilities.

The particular case of interest for the NRS is when the system has a high impact on reading behavior. To analyze different features of recommender systems, we restrict the discussion for high reading probabilities. Considering the performance based on MAE (Equation (16)) where ground truth is assumed to be the Top-N recommender with zero accuracy loss, we observe that Top-N seems to perform better than probabilistic NRS (Figure 13), as the findings are established from both reader models in the simulation. The MAE value represents the accuracy loss an implementer may face due to implementation of probabilistic selection, considering the Top-N selection as the benchmark after t time-steps.

Figure 13 Mean Absolute Error vs. Reading Probability  
![](/api/attachments/5S8W9Z2V/fulltext/images/138138c5acdbed1c7695ea8e6fae0bc15e6d8f28da019e5d56787452590f4fe0.jpg)

However, under the second metric (KL, Equation (17)) wherein the ground truth is that the initial shares of articles represent the natural preference of readers, the probabilistic NRS outperforms the Top-N NRS for both reader models (Figure 14), in terms of assuaging the amplification of counts of few articles. In the case of hard-cut-off we observed that the distortion measure exhibits an approximate L-shape for different values of p. A gradual increasing pattern in KL distortion was observed for beginning $p \sim 0 . 6$

The above findings present the trade-off between the two NRS. While the probabilistic NRS seems to have a small accuracy loss (in terms of counts of articles it recommends) it is truer to the natural shares of the articles and does not create distortions that can otherwise occur. After the counts of articles have achieved a steady state in a natural system we expect that the share of articles will deviate little. This system behavior is achieved through probabilistic NRS, with a slight loss in recommendation accuracy.

## 6.2. Comparison to an Adapted Influence Limiter Heuristic

We discussed the advantage of probabilistic mechanism in terms of its robustness towards manipulability.

Figure 14 Mean KL Distortion vs. Reading Probability (Both Reader Models)  
![](/api/attachments/5S8W9Z2V/fulltext/images/23174190eaa5b587e3da2f59670fdf8e3c01f6ecb332002e358d6ae7a3f84cb6.jpg)

However, one limitation in the news recommender research is the lack of a benchmark to which the performance of probabilistic mechanism can be compared towards manipulation. So we adapt the approach of Resnick et al. (2007) in our context to compare the effects of manipulation in NRS.

As mentioned earlier in §2, the Influence Limiter algorithm (Resnick and Sami 2007) generates item recommendations controlling a rater’s influence on recommender systems through the reputation acquired over time. The reputation of a rater is updated based on rating provided by him to an item, and the loss function determined through the prediction made to a target user compared to the actual preference of the target user.

In this research our focus has been the counts of articles. The reader’s individual behavior (or reading pattern) has been left out for ease of exposition. Hence, the approach of Resnick and Sami (2007) cannot directly be used. Instead, we limit the influence of fake counts to generate article recommendations. In a similar vein it should also be noted that in the present analysis counts of articles are updated, instead of the rater’s reputation.

In our approach, we assign reputation for each article based on prior information about the average inter-arrival time of two consecutive clicks for the recommended article, the total counts received by the article, and the time period of observation in which the influence limiting process operates. The influence limiting process operates in a predefined time interval. An article is assigned a reputation based on observation during this period. After this time interval, new counts received by an article are updated based on its reputation score.

Algorithm 2 (An adapted influence limiter heuristic) Get $\tilde { c } _ { 0 j }$ for each article at $t = t _ { 0 }$ for each article $j , c _ { 0 j } \gets 0$ for each $t _ { i } ,$ when $1 \leq t _ { i } \leq t _ { n }$ and $c _ { i j } \geq 2$

for each article j

$$
\beta_ {i j} \leftarrow \min (1, R _ {i j})
$$

![](/api/attachments/5S8W9Z2V/fulltext/images/6f07dcdcfd4be07f9d3d560b8835e49a67a99c5d004201ad1f7fa43ad68c5a21.jpg)

$$
\begin{array}{l} \tilde {c} _ {i j} \leftarrow \tilde {c} _ {i - 1 j} + \beta_ {i j} \cdot c _ {i j} ^ {\prime} \\ c _ {i j} \leftarrow c _ {i - 1 j} + c _ {i j} ^ {\prime} \end{array}
$$

end for

end for

We assume that the average time interval of two consecutive counts received by a recommended article is less than the average time interval of two consecutive counts received by other articles in the system. A measure $\beta _ { i j }$ limits the influence of a manipulator in the Top-N NRS. For article j at time $t _ { i }$ it is defined as

$$
\beta_ {i j} = \min (1, R _ {i j}) = \min \left(1, \frac {t _ {i} - t _ {0}}{\alpha \cdot (c _ {i j} - 1)}\right).\tag{18}
$$

The influence limiting process operates between preselected time intervals $( t _ { 0 } , t _ { n } ) ;$ this can be determined through the designer’s experience, or another appropriate choice can be the time interval when manipulation activity is most observed. For every $t _ { 0 } \leq t _ { i } \leq t _ { n }$ an article $j ^ { \prime } s$ reputation is updated as given in Equation (18). In the expression,  represents the average time interval that is reasonable between two consecutive counts received by a recommended article in the Top-N NRS (this can be determined through the arrival distribution of counts of the recommended articles); $c _ { i j }$ is the number of counts received by the article j in the time interval given by $( t _ { 0 } , t _ { i } )$ . After $t _ { 0 } ,$ at any given time point $t _ { i }$ the new count received by the article j (denoted as $c _ { i j } ^ { \prime } )$ passes through an influence limiting process to generate a modified count given by $\tilde { c } _ { i j }$ as described in Algorithm $2 ( \tilde { c } _ { 0 j }$ represents count received before $t _ { 0 } )$ After $t _ { n }$ each new count received by any of the articles is modified through its reputation $\beta _ { n j }$ at time $t _ { n } .$ When $R _ { i j } \geq 1$ , all weight is on $c _ { i j } ^ { \prime } ,$ i.e., the article j has full credibility.

Let us consider the first user model in our simulation (when the reader randomly selects an article from the recommended list). Note that in the context of manipulation we are concerned about articles appearing in the recommended list. The initial 100 time steps have been selected as the observation period before implementing the modified count (the influence limiting heuristic) for each article. The selection of an article from the recommended list is random, hence the expected count that an article will receive over initial 100 time steps will be $( 1 0 0 / 1 0 ) \cdot p = 1 0 \cdot p ,$ where p is the selected reading probability in the simulation. Hence, the expected time interval between two consecutive counts received by an article in Top-N NRS is given by $\alpha = ( 1 0 0 / ( 1 0 \cdot p ) ) \dot { = } 1 0 / p$ . Based on our choice of time period for the observation $t _ { i } - t _ { 0 }$ will be $t _ { i } .$ Hence, the reputation of an article j at time $t _ { i }$ will be given by (Equation (18))

Figure 15 Comparison of Manipulation Based on M1  
![](/api/attachments/5S8W9Z2V/fulltext/images/f330ba5dabaf1e2f5a779f319e9f3b9906a0dba40d9dfb4991c576e2fbf42ec7.jpg)

$$
\beta_ {i j} = \min \left(1, \frac {t _ {i} \cdot p}{1 0 \cdot (c _ {i j} - 1)}\right).
$$

As established earlier, the major issue of interest is manipulation at the early stage (which was shown to be more effective for the manipulator). Hence, variants examined are heavy and low early manipulation. As before, the articles of interest are also the N th and 4N + 15th articles in the list.

The results suggest that in the case of extreme manipulations, the proposed adapted influence limiter heuristic performs similarly to probabilistic NRS (Figure 15, left panel). This seems to be by design of the adapted influence limiter heuristic; as the manipulator injects more fake counts for the target article, reputation for it decreases $( \beta _ { i j } )$ . In turn new counts received by the manipulated article generate a lower cumulative increase in its count. However, small manipulation efforts (especially if an article has just missed the cutoff for Top-N and the manipulator is in a position to determine this) may go undetected in case of the adapted influence limiter (Figure 15, right panel). Here, probabilistic NRS is still robust.

## 7. Social Desirability

The analysis presented in this paper demonstrates that the probabilistic selection mechanism is effective in addressing some of the key limitations of the Top-N NRS. These limitations were (1) amplifying the negligible initial difference in the counts of N th and 4N + 15th articles, (2) less choice of articles offered to readers’ by Top-N list, and (3) susceptibility to manipulation by artificially inflating the count of a target article.

![](/api/attachments/5S8W9Z2V/fulltext/images/9e8491d035954b261db1f298a33b5281846222d0f6b78f205c81bef154ba2f1d.jpg)

Still, it is difficult to argue universal superiority of one of the two selection processes for recommendations. For example, when an implementer faces a situation with suspected manipulation activities or she wants to create a set of diverse recommendations in the recommended list, then surely, the probabilistic mechanism will be more desirable. However, when an implementer wants to maximize the short-term revenue or to allow a genuine article to (perhaps deservedly) become more popular, then the Top-N NRS may be the appropriate choice.

One approach to framing this issue is to ask which mechanism is socially more desirable. Clearly, the choice of a particular mechanism depends on the goal of an implementer and the desired effect he wants to create through those recommendations. Research performed in other contexts has also framed it in this context. For instance, Salganik et al. (2006) highlight the problem with the measure of quality, through an experimental approach, in the presence of social influence.

Here we do not address this issue directly. Instead we view it as control that the media owners can exercise by their choice of parameters. If viewed in this manner, the natural question is whether there can be some continuous spectrum of control that can be used (possibly fine-tuned) by managers to achieve any outcome or behavior that they may desire. By introducing a feedback parameter we can offer managers an elegant approach to control the behavior of the system such that it can operate in the entire spectrum.

We extend the approach of probabilistic selection to provide greater flexibility for an implementer. In this modified approach, the selection probability of an article a having count $c _ { a } ( t )$ at time t, is given by

$$
p _ {a} (t) = \frac {c _ {a} ^ {\gamma} (t)}{\sum_ {j} c _ {j} ^ {\gamma} (t)}, \quad \gamma \geq 0.\tag{19}
$$

One advantage of this modified probabilistic approach (Equation (19)) is that we can generate different known selection processes by tuning the parameter  in a single unified equation. To understand the behavior of the system for the modified selection process, we consider different values that  can take, and briefly explain the selection processes corresponding to those values.

 = 0: In this case, all articles have the same probability of being selected in the DL, which essentially simulates a random recommender. Also, in this case we do not incorporate any information generated through user’s interaction with NRS. This selection process can be desirable when an implementer wants to completely eliminate the effect of social influence from NRS.

$0 < \gamma <$ 1: For the given probability function, the number of times an article appears on the DL will tend to be in equal proportion for all articles after a very large time interval. In practice, values of the feedback parameter in this range may have very limited application.

 = 1: Here the count evolution process can be analyzed as a combination of Pólya and Bernard Freidman urn problems in a special case, which has been discussed in detail throughout this paper as the main probabilistic selection mechanism. As mentioned earlier, the selection mechanism in this case is desirable to generate an even distribution in popularity, to generate diverse recommendations, and to thwart manipulation efforts.

$1 < \gamma < \infty \colon$ For $\gamma > 1$ , we will have a system with positive feedback for the articles with high counts. In other words, the NRS generates recommendations such that the articles with high counts will have an even higher probability of being selected for the DL at the next time step. In this case, after a finite time, the probabilistic NRS will behave similarly to Top-N NRS, i.e., N articles with high counts will always be selected for recommendation. The feedback-based approach in this range is desirable to mitigate the issue of penalizing the marginal next article (the case with a count-based selection process) and at the same time maintaining the effect of Top-N selection.

 → : In this case, the probabilistic recommendation generated by Equation (19), is essentially a replication of most popular NRS (i.e., identical to the Top-N mechanism considered earlier in this paper). To understand this, consider the expression given by Equation (19)

$$
p _ {a} (t) = \frac {c _ {a} ^ {\gamma} (t)}{\sum_ {j} c _ {j} ^ {\gamma} (t)} = \frac {1}{1 + \sum_ {j \neq a} (c _ {j} (t) / c _ {a} (t)) ^ {\gamma}}.
$$

We assume that all articles have different counts.<sup>3</sup> Then, $\forall j$ such that $\begin{array} { r } { c _ { j } ( t ) / c _ { a } ( t ) < 1 ; \operatorname* { l i m } _ { \gamma \to \infty } ( c _ { j } ( t ) / c _ { a } ( t ) ) ^ { \gamma } \to 0 . \operatorname { S o } _ { } } \end{array}$ for the article with highest count (among those that are not yet selected for DL), the selection probability for the DL will be 1. Hence, N probabilistic selections in this case correspond to selection of N articles with a decreasing order of their counts.

The proposed feedback mechanism in this section provides implementers flexibility in the selection process of articles and also allows users to process the recommended information in different ways. Depending on various scenarios, we can reduce the rich-get-richer effects for articles, amplify them, or steer them in different directions (with articles with low counts becoming more popular for $\gamma < 0 )$ through help of the parameter . Therefore, use of the above feedback model provides a broader range of control that can be exerted to optimize the system behavior for a particular manager. We defer analytical results and a more detailed study of this to future work.

## 8. Discussion and Conclusion

There has been growing evidence of the influence of NRS on users. The Wall Street Journal (WSJ) (Warren and Jurgensen 2007) noted that the influence of NRS is sparking a new form of payola as marketers try to get more votes and allow users to vote for their favorite submissions. This phenomenon has been further propelled by social networking applications such as Facebook and Twitter, as noted by the Economist in a recent review of the news industry (Economist 2011b). The article from WSJ notes that the aggregation process of news through NRS is also giving rise to an “obsessive sub-culture of a few active users who just purely for the thrill of it, are trolling the web-space for news and ideas to share with others.” For example, a Reddit user known for scoping drove about 100,000 visitors to one amateur photographer’s website (Warren et al. 2007). There are also some marketing companies who promise clients front-page exposure in exchange for a fee (Warren et al. 2007). In other cases users can also buy Facebook fans (likes) or tweets to gain popularity.

In light of all this, NRS should be particularly careful to avoid common manipulative strategies. At present, the articles with highest count or popularity are prominently displayed on the front page on most news sites and thus are seen by millions of people. It is evident from the findings we present in this paper that the practice of using a hard cut-off has the potential to be particularly troublesome. In addition to unduly penalizing the possibly equally good next article that missed this cut-off, this system is quite vulnerable to manipulation. A simple probabilistic mechanism can be used to present popular articles. This has some desirable properties as we show and study in this paper. Readers may also face the problem of information overload through online sources (Kang et al. 2013). In this instance, probabilistic selection can play an enabling role to generate diverse recommendations.

Practically, implementers may choose a more flexible mechanism that may offer the benefits of both Top-N and probabilistic selection. This can be done using a parameterized extension of the probabilistic selection mechanism, as noted earlier. We defer analytical and empirical treatment of the parameterized extension to future work.

Here we have established our main results based on simulation and theoretical results using widely studied urn models. The distributional assumptions of simulation model were driven by real data from local news websites. The performance of the common

Top-N recommender and the probabilistic counterpart proposed here has been analyzed based on two different metrics. The trade-off from using the probabilistic recommender is also shown. Finally, an adapted influence limiter algorithm has been introduced, and its performance has been compared with its probabilistic counterpart. To our knowledge, the problem studied here is novel and these are all unique contributions of our research.

The probabilistic NRS has practical implications in terms of providing a better way of using information generated through users compared to the current Top-N NRS in the recommendation process. Our research also has policy implications, as government and policy think-tanks are increasingly concerned about the entire process of news generation, curation, and distribution (Economist 2011a, Loretta and Brian 2011). In a somewhat light vein, Burt Herman (2011) writes in a prediction for the Nieman Journalism Lab that “in the coming year, social media journalists will #Occupythenews.”

Note also that though we derived our results in a framework of discrete time steps, the statistical distribution of urn functions has been widely studied in continuous cases. For example, Freedman (1965), discusses the asymptotic behavior urn of functions. In future research these functions can be explored to address other issues related to recommender systems research.

Another possible extension of the present research can be examination of the impact of hard cut-off in personalized recommended systems. Though for a given user, even in the context of personalized recommendation, the issue of hard cut-off still exits, it would be interesting to investigate to what extent count amplification can be mitigated at the aggregate level.

On a broader level, algorithms increasingly control what news articles are shown to which user. Some, such as Eli Pariser, author of the popular book “The Filter Bubble,” believe this to be a potential problem. The popular argument is that algorithms will influence thought by controlling news, and that such algorithms tend to become hyper-personalized, creating bubbles wherein each user is in a possibly independent bubble. Others, including many academics in a panel at the 2011 Association for Computing Machinery (ACM) Conference on Recommender Systems in Chicago, believe this problem to be exaggerated, and that algorithms can both personalize as well as provide adequate diversity to limit such problems. In one of the earliest works in the IS area for instance, Adomavicius and Kwon (2012) present methods to enhance diversity. It is in this context though that some important research problems emerge. Studying the specific characteristics of news recommendation algorithms is an important area of research, given that news shapes public opinion on a variety of topics and that algorithms are increasingly influencing its distribution.

As a last thought, while comparing probabilistic approaches for selection in recommender systems, we note that a similar argument can be made not just for news recommendations, but also for any recommender that uses a hard cut-off. For instance, Amazon.com’s product recommendations probably use hard cut-offs based on results generated from collaborative filtering (Linden et al. 2003), and might therefore benefit from using probabilistic variants such as those described in this paper. Currently Amazon’s “Customers who also bought this item also bought...” features a list of specific recommendations on each page. The fate of the next product in that list that misses such a cut-off is similar to the question studied in this paper. However we leave the treatment of this to future work because other types of products $( \mathrm { e . g . }$ , movies, consumer products, etc.) may have other unique characteristics or constraints (Linden et al. 2003).

## Acknowledgments

The authors thank senior editor Gediminas Adomavicius, associate editor Maytal Saar-Tsechansky, and the two anonymous reviewers for their guidance and fruitful comments throughout the review process. The authors also thank the participants at the WITS 2011, INFORMS 2011 Annual Meeting, ACM RecSys 2011, and the participants at the 2011 Winter Conference on Business Intelligence for their helpful comments and discussion. The majority of the research was completed while the first author was a graduate student at the University of South Florida.

## Appendix. Proof of Propositions

Various mathematical notations used to derive analytical results in this section are summarized in Table A.1.

Table A.1 Summary of Terms Used in Analytical Modeling

<table><tr><td>Term</td><td>Definition</td></tr><tr><td> $n_0$ </td><td>Initial natural count of the article-a</td></tr><tr><td> $m_0$ </td><td>Initial natural count of the article-b</td></tr><tr><td>n</td><td>Total number of iterations</td></tr><tr><td>p</td><td>Probability that a reader reads recommended article on arrival</td></tr><tr><td>1 - p</td><td>Probability that a reader reads un-recommended article on arrival</td></tr><tr><td> $A_n^h$ </td><td>The count of article-a in hard cut-off NRS, after n iterations</td></tr><tr><td> $A_{nl}^p$ </td><td>The count of article-a in probabilistic NRS, after n iterations, with p = 0 at every time step</td></tr><tr><td> $A_{nu}^p$ </td><td>The count of article-a in probabilistic NRS, after n iterations, with p = 1 at every time step</td></tr><tr><td> $p_t (read)$ </td><td>Probability of article-a being read in probabilistic NRS at time t</td></tr><tr><td> $p_{at}, p_{bt}$ </td><td>Probabilities of article-a and article-b being recommended in probabilistic NRS</td></tr><tr><td> $p_{tl}(read) = 1 - p_{at}$ </td><td>Probability of article-a being read in probabilistic NRS, with p = 0 at every time step</td></tr><tr><td> $p_{tu}(read) = p_{at}$ </td><td>Probability of article-a being read in probabilistic NRS, with p = 1 at every time step</td></tr><tr><td> $\tau_n$ </td><td>Total count of articles “a” and “b” after n iterations</td></tr><tr><td> $Z_n$ </td><td>Random variable defined as  $Z_n = A_{nl}^p - \tau_n/2$ </td></tr><tr><td> $r_i$ </td><td>Probability of recommended article being read in second user model</td></tr></table>

Proof of Proposition 1. <sub>Let</sub> $A _ { n } ^ { h }$ represent the count of article-a after nth iteration in hard cut-off NRS. Then

$$
\begin{array}{l} E (A _ {n} ^ {h}) = \sum_ {k = 0} ^ {n} {\binom {n} {k}} p ^ {k} (1 - p) ^ {n - k} (n _ {0} + k) \\ = \sum_ {k = 0} ^ {n} {\binom {n} {k}} p ^ {k} (1 - p) ^ {n - k} (n _ {0}) + \sum_ {k = 0} ^ {n} {\binom {n} {k}} p ^ {k} (1 - p) ^ {n - k} (k). \end{array}
$$

Hence, $E ( A _ { n } ^ { h } ) = n _ { 0 } + n \cdot p .$

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>2.</sup> First we derive the expression for $E ( A _ { n l } ^ { p } )$ . As $p _ { t l } ( r e a d ) = 1 - p _ { a t }$ At any time n we have the recurrence relation $P ( A _ { n + 1 l } ^ { p } =$ $A _ { n l } ^ { p } + 0 | { \bf \bar { \cal A } } _ { n l } ^ { p } ) = A _ { n l } ^ { p } / \tau _ { n }$ and $P ( A _ { n + 1 l } ^ { p } = A _ { n l } ^ { p } + 1 \mid A _ { n l } ^ { p } ) = 1 - \stackrel { n } { A } _ { n l } ^ { p } / \tau _ { n } .$ Hence

$$
\begin{array}{c} E (A _ {n + 1 l} ^ {p} \mid A _ {n l} ^ {p}) = (A _ {n l} ^ {p} + 0) \frac {A _ {n l} ^ {p}}{\tau_ {n}} + (A _ {n l} ^ {p} + 1) \bigg (1 - \frac {A _ {n l} ^ {p}}{\tau_ {n}} \bigg) \\ = 1 + A _ {n l} ^ {p} \bigg (1 - \frac {1}{\tau_ {n}} \bigg). \end{array}\tag{A1}
$$

Given the expectation on both sides (A1) and using the property of conditional expectation

$$
E (A _ {n + 1 l} ^ {p}) = 1 + \left(1 - \frac {1}{\tau_ {n}}\right) E (A _ {n l} ^ {p}).\tag{A2}
$$

Using the transformation $( \mathrm { A } 2 ) , A _ { n l } ^ { p } = Z _ { n } + \tau _ { n } / 2$ results in the following relation:

$$
E (Z _ {n + 1}) = \left(1 - \frac {1}{\tau_ {n}}\right) E (Z _ {n}) \quad \text { or } \quad E (Z _ {n}) = \left(1 - \frac {1}{\tau_ {n - 1}}\right) E (Z _ {n - 1}). \tag {A2}
$$

The recurrence relation (A3) results in

(A3)

$$
E (Z _ {n}) = \prod_ {j = 0} ^ {n - 1} \frac {\tau_ {j} - 1}{\tau_ {j}} \left(A _ {0 l} ^ {p} - \frac {\tau_ {0}}{2}\right).\tag{A4}
$$

Using the relation $\tau _ { j - 1 } = \tau _ { j } - 1$ for $n \geq 1$ , the expression in (A4) results in

$$
\begin{array}{c} E (Z _ {n}) = \frac {\tau_ {0} - 1}{\tau_ {0}} \prod_ {j = 1} ^ {n - 1} \biggl (\frac {\tau_ {j - 1}}{\tau_ {j}} \biggr) \biggl (A _ {0 l} ^ {p} - \frac {\tau_ {0}}{2} \biggr) \\ = \frac {\tau_ {0} - 1}{\tau_ {n - 1}} \biggl (A _ {0 l} ^ {p} - \frac {\tau_ {0}}{2} \biggr). \end{array}\tag{A5}
$$

Substituting values (A5), ${ \cal A } _ { 0 l } ^ { p } = n _ { 0 } , \tau _ { 0 } = n _ { 0 } + m _ { 0 } ,$ and $\tau _ { n - 1 } =$ $n _ { 0 } + m _ { 0 } + n - 1$

$$
\begin{array}{c} E (Z _ {n}) = \frac {n _ {0} + m _ {0} - 1}{n _ {0} + m _ {0} + n - 1} \bigg (n _ {0} - \frac {n _ {0} + m _ {0}}{2} \bigg) \\ = \frac {n _ {0} + m _ {0} - 1}{n _ {0} + m _ {0} + n - 1} \bigg (\frac {n _ {0} - m _ {0}}{2} \bigg). \end{array}
$$

Hence, $E ( A _ { n l } ^ { p } - \tau _ { n } / 2 ) = ( ( n _ { 0 } + m _ { 0 } - 1 ) / ( n _ { 0 } + m _ { 0 } + n - 1 ) ) |$ $( ( n _ { 0 } - m _ { 0 } ) / 2 ) .$

Finally, we have

$$
E (A _ {n l} ^ {p}) = \frac {n _ {0} + m _ {0} - 1}{n _ {0} + m _ {0} + n - 1} \frac {n _ {0} - m _ {0}}{2} + \frac {n _ {0} + m _ {0} + n}{2}.\tag{A6}
$$

Now, we derive the expression for $E ( A _ { n u } ^ { p } )$

Probability of the article-a being read at time $t ,$ or in other words, the probability of increase in the count of the article-a at any given time t is

$$
p _ {t u} (r e a d) = p _ {a t}.\tag{A7}
$$

Suppose $1 \leq i _ { 1 } \leq i _ { 2 } \leq \cdot \cdot \cdot \leq i _ { k } \leq n$ be the time indices when the article-a was read. Then the probability of this particular string will be given by

$$
\begin{array}{l} \frac {m _ {0}}{n _ {0} + m _ {0}} \cdot \frac {m _ {0} + 1}{n _ {0} + m _ {0} + 1} \cdot \dots \cdot \frac {n _ {0}}{n _ {0} + m _ {0} + i _ {1} - 1} \\ \cdot \frac {m _ {0} + i _ {1} - 1}{n _ {0} + m _ {0} + i _ {1}} \cdot \dots \cdot \frac {n _ {0} + 1}{n _ {0} + m _ {0} + i _ {2} - 1} \cdot \frac {m _ {0} + i _ {2} - 2}{n _ {0} + m _ {0} + i _ {2}} \\ \cdot \dots \cdot \frac {n _ {0} + k - 1}{n _ {0} + m _ {0} + i _ {k} - 1} \cdot \dots \cdot \frac {m _ {0} + n - k - 1}{n _ {0} + m _ {0} + n - 1}. \end{array}
$$

These indices can be chosen in $n / k$ ways. So the probability that the article-a was read k times $( A _ { n u } ^ { p } = n _ { 0 } + k )$ is given by

$$
\begin{array}{l} p (A _ {n u} ^ {p} = n _ {0} + k) \\ = \binom {n} {k} \\ \cdot \frac {n _ {0} (n _ {0} + 1) \cdot \ldots \cdot (n _ {0} + k - 1) \cdot m _ {0} (m _ {0} + 1) \cdot \ldots \cdot (m _ {0} + n - k - 1)}{(n _ {0} + m _ {0}) (n _ {0} + m _ {0} + 1) \cdot \ldots \cdot (n _ {0} + m _ {0} + n - 1)}. \end{array}\tag{A8}
$$

Hence

$$
\begin{array}{l} E (A _ {n u} ^ {p}) = \sum_ {k = 0} ^ {n} p (A _ {n u} ^ {p} = n _ {0} + k) \cdot (n _ {0} + k) \\ \qquad = n _ {0} \sum_ {k = 0} ^ {n} p (A _ {n u} ^ {p} = n _ {0} + k) + \sum_ {k = 0} ^ {n} k \cdot p (A _ {n u} ^ {p} = n _ {0} + k). \end{array}\tag{A9}
$$

The expressions $\textstyle \sum _ { k = 0 } ^ { n } p ( A _ { n u } ^ { p } = n _ { 0 } + k ) $ and $\textstyle \sum _ { k = 0 } ^ { n } k \cdot p ( A _ { n u } ^ { p } =$ $n _ { 0 } + k )$ are calculated separately. From the result in Equation (A8) we have

$$
^ {\prime \prime} n ^ {\prime \prime}
$$

Now

$$
\begin{array}{l} \sum_ {k = 0} ^ {n} k \cdot p (A _ {n u} ^ {p} = n _ {0} + k) \\ = \sum_ {k = 1} ^ {n} k \cdot \binom {n} {k} \\ \cdot \frac {n _ {0} (n _ {0} + 1) \cdot \dots \cdot (n _ {0} + k - 1) \cdot m _ {0} \cdot \dots \cdot (m _ {0} + n - k - 1)}{(n _ {0} + m _ {0}) (n _ {0} + m _ {0} + 1) \cdot \dots \cdot (n _ {0} + m _ {0} + n - 1)}. \end{array} \tag {A10}
$$

Using the property $\begin{array} { r } { k \cdot { \binom { n } { k } } = n { \binom { n - 1 } { k - 1 } } } \end{array}$ , the expression A10 takes the following form:

$$
\begin{array}{l} n \sum_ {k = 1} ^ {n} \binom {n - 1} {k - 1} \\ \cdot \frac {n _ {0} (n _ {0} + 1) \cdot \dots \cdot (n _ {0} + k - 1) \cdot m _ {0} (m _ {0} + 1) \cdot \dots \cdot (m _ {0} + n - k - 1)}{(n _ {0} + m _ {0}) (n _ {0} + m _ {0} + 1) \cdot \dots \cdot (n _ {0} + m _ {0} + n - 1)} \\ = n \frac {n _ {0}}{n _ {0} + m _ {0}} \sum_ {k = 1} ^ {n} \binom {n - 1} {k - 1} \\ \cdot \frac {(n _ {0} + 1) \cdot \dots \cdot (n _ {0} + k - 1) \cdot m _ {0} (m _ {0} + 1) \cdot \dots \cdot (m _ {0} + n - k - 1)}{(n _ {0} + m _ {0} + 1) \cdot \dots \cdot (n _ {0} + m _ {0} + n - 1)} \\ = n \frac {n _ {0}}{n _ {0} + m _ {0}} \sum_ {k = 0} ^ {n - 1} \binom {n - 1} {k} \\ \cdot \frac {(n _ {0} + 1) \cdot \dots \cdot (n _ {0} + k) \cdot m _ {0} (m _ {0} + 1) \cdot \dots \cdot (m _ {0} + n - k - 2)}{(n _ {0} + m _ {0} + 1) \cdot \dots \cdot (n _ {0} + m _ {0} + n - 1)} \\ = n \frac {n _ {0}}{n _ {0} + m _ {0}} \cdot 1 = n \frac {n _ {0}}{n _ {0} + m _ {0}}. \end{array} \tag {A11}
$$

The expression in A11 is the total selection probability of either of the articles in $n - 1$ iterations, but with the initial counts of $n _ { 0 } + 1$ and $m _ { 0 }$ for the article a and $b ,$ respectively. So expression A9 becomes

$$
E (A _ {n u} ^ {p}) = n _ {0} + n \frac {n _ {0}}{n _ {0} + m _ {0}} = \frac {n _ {0}}{n _ {0} + m _ {0}} (n _ {0} + m _ {0} + n).\tag{A12}
$$

Proof of Proposition 4.

$$
\begin{array}{l} E (B _ {n} ^ {\prime h}) = \sum_ {k = 0} ^ {n - \epsilon} \binom {n - \epsilon} {k} p ^ {k} (1 - p) ^ {n - k} (m _ {0} + \epsilon + k) \\ \qquad = \sum_ {k = 0} ^ {n - \epsilon} \binom {n - \epsilon} {k} p ^ {k} (1 - p) ^ {n - k} (m _ {0} + \epsilon) \\ \qquad + \sum_ {k = 0} ^ {n - \epsilon} \binom {n - \epsilon} {k} p ^ {k} (1 - p) ^ {n - k} (k) \\ \qquad = m _ {0} + \epsilon + (n - \epsilon) \cdot p. \end{array}
$$

## References

Adamic LA (2000) Zipf, power-laws, and pareto-a ranking tutorial. Xerox Palo Alto Research Center, Palo Alto, CA. Accessed August 1, 2014, www.hpl.hp.com/research/idl/papers/ranking.

Adomavicius G, Kwon Y (2012) Improving aggregate recommendation diversity using ranking-based techniques. IEEE Trans. Knowledge Data Engrg. 24(5):896–911.

Chen C, Wu K, Srinivasan V, Zhang X (2011) Battling the Internet water army: Detection of hidden paid posters. Proc. 2013 IEEE/ACM Internat. Conf. Advances Social Networks Analysis and Mining, ASONAM ‘13 (ACM, New York), 116–120.

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52:1577–1593.

Deshpande M, Karypis G (2004) Item-based top-N recommendation algorithms. ACM Trans. Inform. Syst. 22:143–177.

Easley D, Kleinberg J (2010) Networks, Crowds, and Markets: Reasoning About a Highly Connected World (Cambridge University Press, New York).

Economist, The (2011a) Mind for netiquette, or we’ll mind it for you. The Economist (December 7). http://www.economist.com/blogs/ baggage/2011/12/web-censorship-india.

Economist, The (2011b) Bulletins from the future. The Economist 4US5 400:3.

Eggenberger F, Pólya G (1923) Über die statistik verketteter vorgänge. ZAMM—J. Appl. Math. Mechanics/Zeitschrift Für Angewandte Mathematik und Mechanik 3:279–289.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55:697–712.

Freedman DA (1965) Bernard Friedman’s urn. Ann. Math. Statist. 36:956–970.

Herman B (2011) In the coming year, social media journalists will #Occupythenews. Accessed August 2, 2014, http://www .niemanlab.org/2011/12/burt-herman-in-2012-social-media -journalists-will-occupythenews/.

Kang J-H, Lerman K, Getoor L (2013) La-LDA: A limited attention topic model for social recommendation. Proc. 6th Internat. Conf. Social Computing, Behavioral-Cultural Modeling, and Prediction, SBP ‘13 (Springer, Berlin Heidelberg), 211–220.

Kullback S, Leibler RA (1951) On information and sufficiency. Ann. Math. Statist. 22:79–86.

Largillier T, Peyronnet G, Peyronnet S (2010) Spotrank: A robust voting system for social news websites. Proc. 4th Workshop Inform. Credibility, WICOW ‘10 (ACM, New York), 59–66.

Lee JS, Zhu D (2012) Shilling attack detection—A new approach for a trustworthy recommender system. INFORMS J. Comput. 24:117–131.

Lerman K (2007a) User participation in social media: Digg study. Proc. 2007 IEEE/WIC/ACM Internat. Conf. Web Intelligence and Intelligent Agent Technology Workshop, WI-IATW ‘07 (IEEE Comput. Soc., Washington, DC), 255–258.

Lerman K (2007b) Social information processing in news aggregation. IEEE Internet Comput. 11:16–28.

Linden G, Smith B, York J (2003) Amazon.com recommendations: Item-to-item collaborative filtering. IEEE Internet Comput. 7:76–80.

Loretta C, Brian S (2011) Beijing tightens cyber control. Wall Street Journal (December 17). Accessed August 1, 2014, http:// online.wsj.com/news/articles/SB1000142405297020464380457710 1522579231922.

Maroulis S, Guimerà R, Petryet H, et al. (2010) Complex systems view of educational policy research. Science 330:38–39.

Myers DJ (2000) The diffusion of collective violence: Infectiousness, susceptibility, and mass media networks. Amer. J. Sociology 106:173–208.

Newman MEJ (2005) Power laws, pareto distributions and zipf’s law. Contemporary Phys. 46:323–351.

Phillips D (1974) The influence of suggestion on suicide: Substantive and theoretical implications of the Werther effect. Amer. Sociol. Rev. 39:340.

Resnick P, Sami R (2007) The influence limiter: Provably manipulationresistant recommender systems. Proc. 2007 ACM Conf. Recommender Systems, RecSys ‘07 (ACM, New York), 25–32.

Resnick P, Sami R (2008) The information cost of manipulationresistance in recommender systems. Proc. 2008 ACM Conf. Recommender Systems, RecSys ‘08 (ACM, New York), 147–154.

Rogers EM (1976) New product adoption and diffusion. J. Consumer Res. 2:290–301.

Salganik MJ, Dodds PS, Watts DJ (2006) Experimental study of inequality and unpredictability in an artificial cultural market. Science 311:854–856.

Schelling TC (1971) Dynamic models of segregation. J. Math. Sociology 1:143–186.

Van Roy B, Yan X (2010) Manipulation robustness of collaborative filtering. Management Sci. 56:1911.

Warren J, Jurgensen J (2007) The wizards of buzz. Wall Street Journal (February 11). Accessed August 1, 2014, http://online.wsj.com/ news/articles/SB117106531769704150.

Weber TE (2010) Cracking the New York Times popularity code. Daily Beast (December 19). http://www.thedailybeast.com/ articles/2010/12/20/how-to-crack-the-new-york-times-most -emailed-list.html.

Ziegler C-N, McNee SM, Konstan JA, Lausen G (2005) Improving recommendation lists through topic diversification. Proc. 14th Internat. Conf. World Wide Web, WWW ‘05 (ACM, New York), 22–32.
