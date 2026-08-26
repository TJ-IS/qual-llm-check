---
otero_id: 14884
otero_key: "QREHQW4M"
title: "IS OPRAH CONTAGIOUS? THE DEPTH OF DIFFUSION OF DEMAND SHOCKS IN A PRODUCT NETWORK"
authors: "Eyal Carmi; Gal Oestreicher-Singer; Uriel Stettner; Arun Sundararajan"
year: "2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.1.10"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# IS OPRAH CONTAGIOUS? THE DEPTH OF DIFFUSION OF DEMAND SHOCKS IN A PRODUCT NETWORK<sup>1</sup>

Eyal Carmi Google, 76 Ninth Avenue, New York, NY 10011 U.S.A. {eyal.carmi@gmail.com}

Gal Oestreicher-Singer and Uriel Stettner Coller School of Management, Tel Aviv University, Tel Aviv 69978 ISRAEL {galos@tau.ac.il} {urielste@tau.ac.il}

Arun Sundararajan Stern School of Business, New York University, 44 West 4<sup>th</sup> Street, New York, NY 10012 U.S.A. {asundara@stern.nyu.edu}

Recent studies have documented that the contagion of information and behaviors in social networks is generally quite limited. We examine whether this pattern characterizes exogenous demand shocks diffusing in a product network. To this end, we analyze a unique series of demand shocks induced by mass-media book reviews on the Oprah Winfrey television show and in The New York Times. Our identification strategy is based on a difference-in-differences model estimated using two different groups as control, based on propensity-scorebased matching and network proximity to a reviewed book, respectively. Our results show that the diffusion of exogenous demand shocks in the Amazon.com product network is relatively shallow, typically about three edges deep into the network, although the economic impact of this diffusion can often be significant. We link our results to recent findings in the context of diffusion in social networks and discuss managerial implications.

Keywords: Networks and communities, social networks, product networks, diffusion, electronic commerce, exogenous demand shock

## Introduction and Research Questions<sup>1</sup>

Diffusion and contagion in networks have received a great deal of attention from researchers in a variety of fields that include information systems, marketing and computer science (for a review, see Sndararajan et al. 2013). Given the documented influence that linked entities have on each other, coupled with findings on the short average distances between entities in social networks (also known as the “small world” phenomenon), it is natural to expect both information and behaviors to propagate via social networks. However, a striking observation that emerges from recent empirical analysis is that the scope of contagion in social networks is, in fact, surprisingly limited. Although individuals may exert significant influence on their immediate friends, this influence does not immediately translate into changes in behaviors of one’s friends’ friends, on their friends, and so on. In particular, initial evidence from marketing (Yoganarasimhan 2012), information sharing (Bakshy et al. 2011), medicine (Christakis and Fowler 2007), and computer science (Leskovec et al. 2007) suggests that the influence of a focal actor in a realworld network is limited to a small area of the network, and that the depth of diffusion of information and behavior is quite different from what might be predicted, for example, by epidemiological models of contagion.

In this study, our research objective is to study the depth of diffusion in a product network—the visible network structure underlying most electronic commerce websites, in which products are nodes and the hyperlinks between products (e.g., recommendation or co-purchase links) are edges. Prior research by Oestreicher-Singer and Sundararajan (2012b) has identified and quantified the incremental correlation in book sales attributable to the product network’s visibility. To isolate this correlation, those authors identified and controlled for confounding sources of demand correlation, including what might arise from product complementarity. However, the focus of that initial study was on normal daily demand spillovers across products, averaged across many days. In contrast, we focus on whether the abnormal returns associated with a large change in the demand for a product propagate across the product network. Additionally, our study contrasts with prior work that studied the effect that linked entities have on each other by its focus on the propagation of demand shocks across the network (rather than between pairs of linked entities), that is, the depth of diffusion. Specifically, this study seeks to address the question of whether exogenous demand shocks diffuse through product networks, and, if so, to determine the depth of this “spillover effect” across products.

A typical diffusion pattern of a demand shock is illustrated in the following example (Figure 1).<sup>2</sup> In September 2007, the book Louder than Words by Jenny McCarthy (A) was featured on The Oprah Winfrey Show. Sales for the book spiked dramatically after this television appearance, and demand for copies increased over 200-fold on Amazon.com<sup>3</sup> soon after the show aired. This by itself is not especially surprising; the positive economic impacts of being featured on Oprah’s Book Club are well documented (Balogh 2008; Illouz 2003; Rooney 2005). However, analyzing Amazon’s sales data reveals that the economic impact of McCarthy’s appearance on Oprah was not restricted to the specific book discussed during the show. Rather, there were corresponding demand increases for books that were recommended on the reviewed book’s page, and even for books located several recommendation clicks away. For example, the book Life Laughs: The Naked Truth about Motherhood, Marriage, and Moving On (B1), and the book Ten Things Every Child with Autism Wishes You Knew (B2), each located one click away on Amazon’s co-purchase network, experienced a 16-fold and a six-fold increase in demand, respectively.<sup>4</sup> We have documented statistically significant demand increases in response to this event for a number of other books located two (C) and three (D) clicks away from the reviewed book.<sup>5</sup> The question is, to what extent are those increases the result of the existence of a visible product network?

An ideal experiment that would enable us to answer this question would be to randomly split up consumers such that one group observes recommendation links, whereas the other does not, and to compare the two groups’ purchase behavior following exposure to exogenous events that might trigger demand shocks. Clearly, however, this would be impossible to achieve using a real-world retail site such as Amazon.com, and an experiment in a controlled, simulated environment would probably offer only limited information. Thus, it seems that the best option is to find a means of making use of the rich observational data available to us—namely, data from the product network on Amazon.com, coupled with a unique series of exogenous demand shocks caused by mass-media book reviews on the Oprah Winfrey television show and in The New York Times “Sunday Book Review.” At the same time, it is crucial to take steps to mitigate the biases introduced by the inherent endogeneity of the process of influence in question.

Specifically, one may expect that a reviewed book’s network neighbors share both observed and unobserved characteristics with the reviewed book, and thus are potentially more susceptible to being affected by the review (due to group affiliation), regardless of the existence of a visible hyperlink. To address this endogeneity, we adopt an identification strategy based on a difference-in-differences extension of propensity-scorebased matching, and, in addition, we utilize the network structure to separate contagion from other sources of demand complementarity.

![](/api/attachments/QREHQW4M/fulltext/images/0da7665b2db7993dd9689d5eef25e7071eb7de305bb3077d34a0f05bbc32d58a.jpg)  
Figure 1. Example of the Spillover of Exogenous Demand Shocks Across a Product Network

Our empirical results show that the visible network has a significant average influence on neighbors up to three or four links away from the reviewed book, and that this effect decays rapidly with distance from the source of the shock. These results provide new evidence that exogenous demand shocks diffuse in patterns similar to those observed in social networks.

The rest of this paper is organized as follows: We review the related literature; we then describe the data used for the empirical part of the paper and the operationalization of variables. The depth of the spillover effect and the associated identification issues are discussed and analyzed. Finally, we conclude, summarize key managerial insights, and provide avenues for future research.

## Related Work

This study draws on and adds to two research streams: We draw selectively from the network analysis literature, in particular from studies on the contagion process in networks; and, as our focus is on contagion in product networks, we add to the study of the economic impact of the emergence of product networks.

Numerous studies on contagion in networks, especially in the context of epidemiology (Jeger et al. 2007), the spread of computer viruses (Lloyd and May 2001), and word-of-mouth/ information diffusion (Aral et al. 2009; Bapna and Umyarov 2015; Cointet and Roth 2007; Garg et al. 2011; Libai et al. 2013), treat diffusion as an unbounded process (stochastic or deterministic). These studies focus on the conditions that may cause an event such as a disease outbreak, computer virus infection, technology innovation, or product adoption to spread across the network until the entire network is affected. In so doing, these studies generally focus on the base-rate of contagion or the network characteristics. However, some recent evidence suggests that the influence of an actor in a real-world network is limited to a small area in the network. For example, Christakis and Fowler (2007), who analyzed a large social network of participants in the Framingham Heart Study, identified a significantly higher-than-average risk of obesity among individuals who were socially connected to an obese person by up to three degrees of separation. This increased risk dropped with distance: A person who was connected to an obese individual by four degrees of separation or more did not have an increased likelihood of being obese. Three degrees of influence have also been documented in cooperation games (Fowler and Christakis 2010). Bakshy et al. (2011) document how over 99% of “events” on Twitter do not diffuse more than one edge deep into the network. A follow-up study by Goel et al. (2012) that examined the contagion of information and product adoption across a range of networks including Twitter found that the vast majority of cascades in social networks are small, and about 95% of the influence terminates within one degree of the initial adoption seed. Similarly, Leskovec et al. (2006) and Leskovec et al. (2007) studied cascades in a large person-to-person recommendation network and demonstrated that cascades tend to be shallow, but that occasional large bursts of propagation can occur. Characteristics of the diffusion process have further been elucidated in the context of YouTube videos. Specifically, Yoganarasimhan (2012) showed that a video’s diffusion is positively influenced by the video “author’s” first- and second-degree connectivity in YouTube’s social network, and that the local structure of the social network affects this diffusion process. In the context of alliance networks, Chellappa and Saraf (2010) showed that a focal firm may benefit from resources controlled by other firms with which it does not explicitly collaborate. Our work extends this literature to the context of product networks and, to the best of our knowledge, is the first to use exogenous demand shocks to study the depth of spillover in such networks.

We also add to the literature on the economic impact of product networks. While social networks have received much attention from researchers in a variety of fields such as business, economics, epidemiology, and computer science, the literature on product networks is, perhaps surprisingly, relatively sparse. Several papers, while not mentioning product networks explicitly, do study networks formed between the landing pages of “consumed” items. These include a study of networks of videos on YouTube (Oh et al. 2012), networks of blogs (Mayzlin and Yoganarasimhan 2012),<sup>6</sup> and networks of news reports (Dellarocas et al. 2012). Oestreicher-Singer and Sundararajan (2012a) investigated the effect of product networks on the evenness of demand across products, and Goldenberg et al. (2012) studied the interaction between product networks and social networks in the context of YouTube. Most relevant to the current study, Oestreicher-Singer and Sundararajan (2012b) studied the network of books on Amazon.com and quantified the incremental correlation in book sales attributable to the product network’s visibility. To isolate this correlation, the authors identified and controlled for confounding sources of demand correlation, including what might arise from product complementarity. They find that the explicit visibility of a co-purchase relationship can lead to up to a threefold amplification of the average influence that complementary products have on each other’s demand levels. Lin et al. (2017) extend this work to study the effects of network diversity and stability in different categories of product networks and across different types of recommendations.

Our current study differs from the work of Oestreicher-Singer and Sundararajan (2012b) in several ways. First, while both papers study the effects of a visible product network on demand, they address different, although complementary, research questions: The former paper focused on the effect of (1) immediate neighbors (2) averaged over a long period of time during which demand was “normal.”<sup>7</sup> In contrast, the current study focuses on (1) the depth of diffusion in the case of (2) abnormal sales activity (shocks). Second, by focusing on exogenous shocks, the current study focuses on the behaviors of a subset of consumers rather than all those exposed to and potentially influenced by visible product recommendations. Indeed, prior research has presented a taxonomy of behavior for online retail shoppers, classifying shoppers according to their motivations and goals (Moe 2003), and distinguishing the conversion rates of visitors motivated by a planned purchase from the conversion rates associated with hedonic browsing (Moe and Fader 2004). Our paper emphasizes the ripple effect generated by consumers who seek out a book that has recently been reviewed, that is, consumers making planned purchases. The fact that such a ripple effect occurs in the context of planned purchases is particularly notable, given that such shopping sessions are not meant to “explore the market and expand the consideration set” (Moe 2003, p. 31). Finally, given the vast differences in foci, the current paper deploys a very different methodology: use of a series of demand shocks combined with a difference-in-differences approach. Accordingly, it uses different data, including new data sets constructed from the websites of The Oprah Winfrey Show and of The New York Times. From a methodological point of view, our paper contributes to the emerging body of literature that aims to distinguish actual spillovers from other causes of correlated outcomes between neighboring nodes in complex networks.

## Data

The following section provides an overview of our data set and of the operationalization of variables we use. We combine data collected from three main sources: (1) information about network structure and demand for books on the Amazon.com website, (2) information about book reviews that appeared on The Oprah Winfrey Show on television, and (3) information about book reviews that appeared in the “Sunday Book Review” section of the online edition of The New York Times. Oprah Winfrey’s endorsement has been shown to have a powerful economic (and political) impact (Balogh 2008; Illouz 2003; Rooney 2005). Similarly, book reviews published in The New York Times newspaper significantly increase the sales of the reviewed books (Deschatres and Sornette 2005; Sorensen and Rasmussen 2004). Our use of two different sources for exogenous demand shocks contributes to the robustness of the results of this research.

## Network Structure and Demand Data from Amazon.com

To analyze the patterns of cross-product spillover processes on Amazon.com following exogenous shocks, we constructed a data set comprising daily product, pricing, demand, and network-related information for over 700,000 books sold on Amazon.com between January 2006 and June 2008. Each focal product has an associated webpage, displaying a set of “co-purchase links”: hyperlinks to the products on Amazon. com that were most frequently co-purchased with the focal product. The co-purchase set for each webpage is limited to five<sup>8</sup> items and is listed under the heading: “Customers who bought this item also bought....” Conceptually, the copurchase network is a directed graph in which nodes correspond to products, and edges to directed co-purchase links (see Appendix C for details).

Data on this graph are collected using a Java-based crawler that starts from a popular book and follows the co-purchase links using a depth-first algorithm. At each page, the crawler gathers and records information on the main book featured on the page, as well as the co-purchase links on that page, and terminates when the entire connected component of the graph is collected. This process is repeated daily. The size of the daily collected connected component varies and is 260,000 books on average. The algorithm used for data collection is provided in the Appendix A.

We use the following data for each book: ASIN (a unique serial number given to each book by Amazon.com), list price, sales price (the price on the Amazon.com website that day), co-purchases (ASINs of the five books that appear on the copurchase list), Sales Rank (a number associated with each product on Amazon.com that measures its demand relative to other products), author, category, number of user reviews, and average star rating.<sup>9</sup>

## Exogenous Shocks from The Oprah Winfrey TV Show

To analyze the patterns of cross-product spillover processes associated with book reviews featured on The Oprah Winfrey Show, we collected information about book reviews that appeared on a dedicated webpage on the Oprah.com website (see Figure 2). We collected review-related data from January 2006 to April 2008. The data set contains 400 book reviews. For each review, the book’s title, author, and review date were collected using a PHP-based crawler and were then manually verified.

## Exogenous Shocks from The New York Times

For robustness, we also collected data about book reviews that appeared in the “Sunday Book Review” section of the online edition of The New York Times. Use of this additional data set enables us to examine multiple review sources (both television and online newspaper content) as well as to consider books that are likely to be of a different nature compared with the books selected by Oprah Winfrey, given that the two review sources cater to somewhat different audiences. In particular, a comparison of the categories associated with the reviewed books indicates that whereas Oprah Winfrey tends to review books related to topics such as personal growth, relationships, and lifestyle, The New York Times tends to focus on topics such as autobiographies, biographies, and fiction.

The New York Times data set contains over 2,000 book reviews, published between January 2006 and June 2008. The “Sunday Book Review” section appears weekly on NYTimes.com, and each issue contains between 10 and 15 book reviews. Each book review in the “Sunday Book Review” has a dedicated webpage on the NYTimes.com website (see Figure 2). The collection method and data are similar to those described above for the Oprah Winfrey reviews.

## Event Networks

Each review event was linked to the corresponding network and sales data from Amazon.com. The data went through a series of manual and automatic data cleaning procedures (see Appendix B for details).

## Operationalization of Variables

We developed several measures to represent the magnitude of an exogenous demand shock:

Sales Rank (SR) is a number associated with each product on Amazon.com that measures the product’s demand relative to other products.<sup>10</sup> The best-selling product is therefore ranked

![](/api/attachments/QREHQW4M/fulltext/images/10eac1523a3f48fec5ab005a79d22a3e5de95a13e7b204311416de5cbf96c474.jpg)  
Figure 2. Book Reviews Taken from “Books Seen on the Show” Page on Oprah.com (left-hand image) and the “Sunday Book Review” Section of the Online Edition of The New York Times (right-hand image)

1, followed by 2, 3, and so on. The Sales Rank of each product on Amazon is updated several times a day, and there are intra-day fluctuations; therefore, we use a 24-hour average of the Sales Rank.

Prior literature has developed measures of estimated demand levels, based on Sales Rank data (Ghose and Gu 2006; Ghose et al. 2006; Oestreicher-Singer and Sundararajan 2012a). However, those conversion measures are inappropriate when discussing high-selling products, such as some of the books in our sample (for an extended discussion on conversion of Sales Rank to demand and an evaluation of robustness, see Appendix E). We therefore use the Sales Rank for our analysis, and report on using demand in our discussion of robustness checks.

Pre-Event Average Sales Rank – To assess the <sub>( )</sub>SR magnitude of response to the exogenous shock, we follow a common procedure in extreme event studies (Chollete 2009) and compute the pre-event average Sales Rank of each <sub>( )</sub>SR product. This variable is used as the baseline against which the post-shock demand is compared. The use of this variable is based on the assumption that every book has a stable preevent Sales Rank, which can be estimated using the average Sales Rank in the two weeks prior to the day of the review. The estimations reported here use a 14-day window. Note that choosing a large window is problematic, since it increases the likelihood of interference from uncontrolled exogenous events. On the other hand, we would like to use the largest possible window in order to best characterize the pre-event patterns. We experimented with various window sizes; results were found to be robust with window sizes of 1 to 4 weeks.

SalesRankRatio (SRR) measures the magnitude of the event at time t and is defined as: $S R R _ { i , t } = \sqrt { \frac { S R _ { i , t } } { S R _ { i } } }$ , where $S R _ { i , t }$ is the average daily Sales Rank of book i on day $t . ^ { 1 1 }$ This measure is computed daily for each book in the sample (the reviewed books and their network neighbors) for the period ranging from two weeks prior to the date of the review until two months after the date of the review.

Distance of a book is defined as the number of links on the minimal path extending across the network to the reviewed book. By definition, the reviewed book has a distance of 0, its first neighbors have a distance of 1, its second neighbors have a distance of 2, and so on. In graph theoretic terminology, distance is the geodesic distance between the reviewed book and the book being observed in the network. Note that distance is measured according to the network structure at the time of review. Clearly, the network structure may change over the period immediately following a review. To evaluate the extent to which such changes occur, we computed the average change of the local networks as the percentage of added or deleted neighbors up to a distance of four links away from each reviewed book, averaged across the review events within a window of two weeks before and after each review event. We find that the average daily change in the network structure is 1.43% (for a detailed analysis of this network, see Oestreicher-Singer and Sundararajan, 2012a). Hence, while we are unable to capture those changes in our operationalization of variables, we believe the change in network structure within the small time window analyzed here is not a major concern. Nevertheless, exploring the dynamics of the network structure following a demand shock is an interesting avenue for future research.

## Identification of Cross-Product Spillovers

One initial measure of the depth of exogenous shock diffusion in the online product network is obtained by evaluating the average Sales Rank of the reviewed book and the Sales Ranks of its neighbors in the three-day period preceding the review and comparing them to the average Sales Ranks of the same products in the three-day period immediately following the review. We find that, on average, neighbors up to three clicks away from a reviewed book experience a demand shock immediately following the event, and this shock is both economically and statistically significant. Following a review by Oprah Winfrey, we observe, on average, a 29.57-fold increase in the Sales Rank of first neighbors of the reviewed book, a 3.65-fold increase in Sales Rank for second neighbors, and a 2.07-fold increase in Sales Rank for third neighbors (see Table 1 for more details). Although the effect of the network beyond third-degree neighbors is not significant on average, increases in demand can be observed as far as the fourth and fifth neighbors. These results provide initial evidence of the role of the product network in the spillover of exogenous shocks.

## Identification Challenges and Ideal Experiments

The results presented above, however, may be subject to selection bias. Specifically, in our context, selection bias is introduced by two sources: (1) selection of the product to be reviewed and (2) selection of network neighbors to be featured on the product’s page. Books featured on The Oprah Winfrey Show are presumably not randomly selected for review, but rather are identified by some underlying process of selection such as compatibility with tastes of existing fans, popularity, the agenda Oprah Winfrey wishes to promote, or various marketing efforts exerted by publishers. It is therefore possible that Oprah Winfrey selects books that have an unobserved set of shared characteristics. We partially control for this source of bias by using two very different independent sources of exogenous shocks (i.e., The New York Times and The Oprah Winfrey Show). Moreover, we also verified that the category distributions of the books reviewed on Oprah and in The New York Times are very different. Acknowledging this identification effect, we note that its extent in our setting is assumed to be minimal given that we focus on the effect of the demand shock on the network neighbors and not the effect of the review on the reviewed book. Put differently, it is unlikely that the producers of Oprah or the publishers of The New York Times have any influence in selecting the network neighbors of reviewed books,<sup>12</sup> which are instead chosen by an algorithm on Amazon.com.

The second source of selection bias is introduced by the recommendation algorithm’s selection of network neighbors. Simply put, the treatment assignment in our case is not random, and the network structure cannot be assumed to be independent of the shock.<sup>13</sup> We would expect that the network neighbors of a reviewed book share observed and unobserved characteristics with that book, and thus are potentially more susceptible to being affected by the review (due to group affiliation), regardless of the existence of a visible hyperlink. For example, books that share an author with a reviewed book are more likely to experience an increase in sales following the review and are also highly likely to be network neighbors. Thus, the increase in demand for such a neighbor may be mistakenly attributed to the presence of the visible link. We need to address the endogeneity caused by this source of selection bias to be able to conclude that spillover does, in fact, occur across the network as a result of the visibility of the links. An ideal experiment in our context would correct for the latter source of selection bias. To clearly measure the effect of the visible links on the diffusion of exogenous demand shocks in a product network such as Amazon.com, we would need to randomly split the Amazon buyers into two groups: the treatment group gets to see the Amazon co-purchase network of a book reviewed by Oprah Winfrey (or reviewed by The New York Times), while the other group does not get to see the network of that same book. Note that in this case, both groups of users are exposed to the review itself (i.e., exposed to the source of the shock). In this hypothetical scenario, any differences between the demand patterns for the books in the co-purchase network (and specifically, the propagation of a shock versus a lack thereof) would be attributable to the visibility of the co-purchase network. Unfortunately, it seems virtually impossible to construct an experiment that approximates this ideal scenario.

However, if we shift our focus away from the users and onto the products in the network, new possibilities begin to emerge. Specifically, an alternative “ideal experiment” that would enable us to test our hypothesis would be to show all users the same network, but to randomly assign the position of the books in it. This means that a user who clicks on a product will see five links to random books (i.e., books that were not necessarily co-purchased with the book the user has clicked on), which are no likelier than any other book to share unobserved characteristics with the focal book. In this case we would need to randomly split the Amazon books (rather than buyers) into two groups: the “treatment” group gets to be positioned in proximity to (i.e., up to a few clicks away from) a book reviewed by Oprah Winfrey (or reviewed by The New York Times), while the other group is positioned far from the networks of reviewed books. A priori, a user who is exposed to a book review is just as likely to purchase a treated book as she is to purchase a non-treated book. This means that if demand shocks propagate among treated books (on average) but do not propagate among non-treated books (on average), the effect is a result of the presence of the visible product network.

<table><tr><td colspan="4">Table 1. Shock Statistics Based on Sales Rank</td></tr><tr><td>Source</td><td>Distance</td><td>Number of Books</td><td>Average Sales Rank Ratio</td></tr><tr><td rowspan="5">NYT</td><td>0 (focal books)</td><td>43</td><td>55.22</td></tr><tr><td>1</td><td>214</td><td>4.34</td></tr><tr><td>2</td><td>625</td><td>4.18</td></tr><tr><td>3</td><td>1539</td><td>2.10</td></tr><tr><td>4</td><td>3435</td><td>1.99</td></tr><tr><td rowspan="5">Oprah</td><td>0 (focal books)</td><td>40</td><td>146.77</td></tr><tr><td>1</td><td>191</td><td>29.57</td></tr><tr><td>2</td><td>419</td><td>3.65</td></tr><tr><td>3</td><td>879</td><td>2.07</td></tr><tr><td>4</td><td>1734</td><td>1.92</td></tr></table>

This ideal experiment is somewhat more straightforward to imitate. Specifically, given that the treatment group (i.e., the co-purchase network) is not random, we need to choose a group as control such that, a priori, a user exposed to a book review (the source of a shock) is equally likely to purchase a treated book or a control book. Possible choices for such groups include books of the same category, or books written by the same author as a reviewed book. However, neither group captures all possible unobserved characteristics that increase the likelihood of a given book to be co-purchased with a reviewed book.

In what follows, we first introduce our difference-in-differences model, and then detail how we construct two different groups to be used as control that attempt to mitigate the potential bias in different ways. The first is based on propensity-score matching, and the other is based on structural variation within the product network.

## Difference-in-Differences Model

The difference-in-differences model is a common statistical method used to analyze observations made across several time periods (before and after a treatment is given) both for a group that received the treatment and for a another group that did not receive the treatment (Meyer 1995). The presence of a control group is used a control for global trends and seasonal factors that might alter overall demand patterns across books in general, as well as for factors other than network membership that might account for correlations among the demand levels of the reviewed book and of other books (more on this later). In our case, treated products are those that are part of the local network around a reviewed book (up to four links away).

Our specification includes four time windows, each of which is three days long: the first (labeled $t _ { 0 } )$ is the three days prior to the event; the second (labeled $t _ { 1 } )$ is three days following the event; the third (labeled $t _ { 2 } )$ is three to five days following the event; and the fourth (labeled $t _ { 3 } )$ is six to eight days following the event. Note that ${ \mathrm { i f } } ,$ as expected, the average Sales Rank in the three days leading to the event (t ) is equal to the average Sales Rank in the two weeks prior to the review event, then the Sales Rank Ratio (SRR) for the first time window is equal to one by definition. For each three-day window we calculate the SRR as defined above (i.e., average SR in the time window compared to the pre-event average Sales Rank). We therefore estimate the following model:

$$
\begin{array}{r l} \log \bigl (S S R _ {i t} \bigr) & = \beta_ {0} + \beta_ {1 t} \text { Period } _ {t} + \beta_ {2 t} \text { Treatment } _ {i} \\ & \quad + \beta_ {3 t} \text { Period } _ {t} \text { Treatment } _ {i} + \beta_ {4} x _ {i t} + \beta_ {5 k} \varphi_ {k} + \varepsilon_ {i t} \end{array}
$$

where t corresponds to each of the four time windows, $t _ { 0 } , t _ { 1 } ,$ $t _ { 2 } , t _ { 3 } .$ Period<sub>t</sub> are time-period fixed effects, Treatment<sub>i</sub> is a binary variable that represents the assignment to treatment groups, $x _ { i t }$ are observed covariates (author, category, average Sales Rank, price, binding, rating, and indegree), $\varepsilon _ { i t }$ are unobserved covariates, and $\varphi _ { k }$ is a vector of either review source or review event fixed effects (with k being the event index). Note that in our linear regression model, using the logarithmic transformation of a book’s SRR instead of its absolute value to fit the data ensures that the rise of one book and the fall of another contribute equally. The main coefficients of interest here are those of the interaction terms (i.e., the $\beta _ { 3 t }$ coefficients). Because we use the logarithmic transformation, we report the results of Exp(β ). We note that each estimation is carried out for a single treatment group comprising all books that are at distance D from a reviewed book (where D = 1, 2, 3, or 4).

## Defining the Appropriate Group to Be Used as a Control

We next describe our construction of two different groups that we use as controls. We design those groups under the assumption that in an ideal experiment the position of a book would be randomly assigned. Given that this is not possible, we are forced to compare between books that are within the local network of the reviewed books and those that are not.

A natural first candidate might include randomly selected products that are not part of the reviewed book’s local network (and thus not treated). However, while this group allows us to control for global fluctuations in demand over time, it does not allow us to control for correlated demand patterns among linked products that stem from factors other than the visibility of the link between them.

## Using Matched Sample to Generate Groups as Control

One way the literature proposes to create a more reliable reference group is to use a matched sample rather than a random set of untreated entities (see Heckman et al. 1998; Rosenbaum and Rubin 1983). We follow prior research (e.g., Garg et al. 2011) that has adopted the idea that each treated entity (in our context, a neighboring book) is paired with a non-treated control entity (i.e., a book that is not a neighbor) that is identical to the treated entity in terms of its observed characteristics. The caveat of such “hard” matching is that it is typically difficult to find candidates that share all observed characteristics. Therefore, many researchers use a matching technique based on the calculation of a logit or probit-based “propensity score” for each entity that reflects its propensity for being treated. Each treated entity is matched to a nontreated entity with the same propensity score. This may result in nonintuitive specific matching while preserving the global distributions over the treatment and control. Thus, instead of grouping products based on observed covariates (such as category or author), we compute the propensity of each book to be treated, and group the books according to propensity score (see also Pearl 2009).

In the context of this study, a book’s propensity score should capture its likelihood of being a neighbor of a given reviewed book. Each treated book (neighbor) is subsequently matched to a non-treated book according to the books’ initial propensity of being a neighbor of the reviewed book. We computed each book’s propensity score using observed book characteristics (i.e., author, category, average Sales Rank, price, binding, and rating). We then created a matched sample based on propensity scores with nearest-neighbor matching (Leuven and Sianesi 2003). That is, for each network neighbor $( b _ { k j } )$ of a reviewed book (b<sup>o</sup><sub>k</sub>), given event $k ,$ we assigned a matched book $( b _ { k j } ^ { ' } )$ to the matched sample such that the probability of $b _ { k j } ^ { ' }$ to be a network neighbor was equal (or nearly equal) to that of $b _ { k j } ,$ on the basis of a specific propensity score. Ideally, one would want the matched book $b _ { k j } ^ { ' }$ to be as similar as possible to the network neighbor $b _ { k j } ,$ , and in general for the distribution of all observed properties of $\{ b _ { k j } \}$ and $\{ b _ { k j } ^ { ' } \}$ to be identical so that the only difference is the treatment. Note that the matching process was repeated separately for books at each distance. Also, clearly, no matching was done to the reviewed book itself, as it is not part of the analysis. Table A1 in Appendix A depicts comparison statistics on the matched sample versus the treatment groups (again, separated by distance).

Note that the control books are from the general population across the network, whereas the treated books are by definition clustered around reviewed books. Hence, we cannot guarantee that two neighboring treated books will necessarily be matched with neighboring control books. For example, assume that book X is reviewed by Oprah Winfrey, and books Y and Z are its neighbors. Because of homophily, Y and Z, which are both connected to X, may share unobserved characteristics and, thus, residuals for these books could be correlated. Next, assume that Y is matched to Y' and Z is matched to Z'. While Y and Z share the same neighbor X, their respective matches $\mathrm { Y } ^ { \prime }$ and Z' do not necessarily share some neighbor X'. This may result in asymmetry between the treatment group and the group used as the control. However, given that we match on observable homophily, we assume that the bias resulting from this asymmetry is not great.

## Using the Network Structure to Generate Groups as Control

One limitation of the matched-sample-based control is that by definition it only uses books that are not part of the event network. Assuming that the network has a high likelihood of being made up of complementary books, by excluding the network we may be excluding these “ideal” candidates. Thus, in what follows, we offer an alternative group as a control based on the network structure that uses only books that are part of the event network. Specifically, given a treatment group containing all of the books at distance D from a reviewed book, we construct a group comprising all of the books that are at distance D+1 from that book. For example, for books at distance 1, we use the books that are at distance 2 as controls; referring back to the example in Figure 1, this means that we would group books B1 and B2 as part of the control for books A1 and A2. Similarly, for books at distance 2, we group the books that are at distance 3 as a control, and so on. Note that the treatment group and the group used as a control in a given estimation need not be the same size (that is, it is possible to pool together all books of distance D as the treatment group and to pool together all books of distance D+1 as the control). This is because the difference-indifferences method used does not require a one-to-one matching of treatment items and control items, but rather a group-to-group matching.

The advantage of the use of this type of control is that, because it is part of the event network, we can assume that the books it comprises are complementary to the reviewed book but do not enjoy the benefit of the treatment group’s proximity to the reviewed book. As a result, the group used as a control has the capacity to serve as a benchmark for the added effects of increased visibility. In fact, this control can be thought of as conservative, given that it is made up books that, as part of the event network, are likely to enjoy some of the spillover effect. That is, given that the group used as control for distance D is the group at distance D+1, our model does not measure the effect of being at distance D, but rather the added value of being one step closer to the reviewed book. Moreover, while we are unable to control for the endogenous link-formation process, the group used as control is based on the results of the same recommendation algorithm and hence partially controls for this endogenous effect.

Table A2 in Appendix A depicts comparison statistics on the network-based control versus the treatment groups.

We note that, in constructing a group as a control, it is also necessary to take into account the intersection problem, a common problem in network analysis in which, on the basis of the properties used to define treatment groups and its control, it may be possible to assign some network members to both (see Bapna and Umyarov 2015). Exclusion of these “intersecting” members may lead to statistical differences between the treatment group and the group used as a control. The intersection problem is unlikely to affect the match sampling based control, which, by definition, comprises books in nonoverlapping networks that share similar characteristics. In the second case, however, there may be some overlap between books at different distances from a reviewed book (e.g., books B and C are in the co-purchase network of reviewed book A, and book B is also in the co-purchase network of book C; therefore, book B is both one click away from book A and two clicks away from book A). However, this problem is most likely to affect books with high indegrees (Bapna and Umyarov 2015). Thus, to address this issue we include the indegree as a control in all our model estimations. We include the indegree in the reported descriptive statistics of all control and treatment groups; we note, however, that there does not seem to be a systematic difference in indegree between the groups in our case.

## Model Estimation

We estimated a difference-in-differences regression model for all network neighbors up to four links away from any reviewed book and for their corresponding controls. The dependent variable in the model is the log-transformed SRR, which measures the change in demand relative to the preevent average level. Since the responses of products in the subnetwork related to a single review event may be correlated, we clustered the standard errors at the review event level. Therefore, within each of the 83 review events, all neighboring books are allowed to be correlated.

The results of the analysis using the matched sample based group and the network structure based group as controls and the control based on network structure are shown in Table 2 and Table 3, respectively. The tables depict the values of the difference-in-differences estimator $e x p ( \beta _ { 3 t } )$ and its standard errors for each degree of distance along with the control variables. The results in both tables are organized as follows: Each column reports the results for books at a specific distance. The leftmost column reports the results for the regression of the first neighbors (i.e., books for which distance = 1); the second column reports the results for the second neighbors; the third column reports the results for the third neighbors; and the rightmost column reports the results for the fourth neighbors. Each row represents the differencein-differences estimator $( \beta _ { 3 t } )$ for a different time window. The first row reports the difference-in-differences estimator for $t _ { 1 } ;$ the second row reports the difference-in-differences estimator for $t _ { 2 } ;$ and the third row reports the difference-in-differences estimator for $t _ { 3 } .$

Accordingly, in the model estimation using the matched sample as the control (Table 2), the coefficients of the difference-in-differences estimators are significant and positive with a notable decrease in coefficient size as (1) time elapses after the exogenous shock and (2) the distance from a focal book increases.<sup>14</sup> For example, compared to the matched sample, a first neighbor (distance one) has a 78.6% increase in SRR within the first three days (t<sub>1</sub>) after the book review, a 49.6% increase in SRR within the following three days (t ), and a 26.6% increase in SRR within six to eight days (t ) after the shock.

<table><tr><td colspan="5">Table 2. Results of Difference-in-Differences Model for  $\log(SRR)$  Using Ordinary Least Squares, with the Group Used as a Control Being the Matched Sample</td></tr><tr><td>DV: log(SRR)</td><td>Distance 1</td><td>Distance 2</td><td>Distance 3</td><td>Distance 4</td></tr><tr><td rowspan="2">Exp( $\beta_{3t1}$ ) (Days 0-2)</td><td>1.786***</td><td>1.072*</td><td>1.027</td><td>0.980</td></tr><tr><td>(0.083)</td><td>(0.034)</td><td>(0.020)</td><td>(0.015)</td></tr><tr><td rowspan="2">Exp( $\beta_{3t2}$ ) (Days 3-5)</td><td>1.496***</td><td>1.115*</td><td>1.082***</td><td>1.041*</td></tr><tr><td>(0.078)</td><td>(0.042)</td><td>(0.023)</td><td>(0.017)</td></tr><tr><td rowspan="2">Exp( $\beta_{3t3}$ ) (Days 6-8)</td><td>1.266**</td><td>1.117*</td><td>1.124***</td><td>1.090***</td></tr><tr><td>(0.072)</td><td>(0.043)</td><td>(0.028)</td><td>(0.018)</td></tr><tr><td rowspan="2">Exp(Constant)</td><td>-0.459**</td><td>0.710***</td><td>0.825***</td><td>0.847***</td></tr><tr><td>(0.135)</td><td>(0.062)</td><td>(0.039)</td><td>(0.030)</td></tr><tr><td>Observations</td><td>2452</td><td>6319</td><td>13865</td><td>28989</td></tr><tr><td> $R^2$ </td><td>0.115</td><td>0.046</td><td>0.023</td><td>0.017</td></tr><tr><td>F</td><td>14.08</td><td>11.56</td><td>18.65</td><td>18.53</td></tr></table>

Standard errors in parentheses (clustered at the review event)  
\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

<table><tr><td>DV: log(SRR)</td><td>Distance 1</td><td>Distance 2</td><td>Distance 3</td><td>Distance 4</td></tr><tr><td rowspan="2">Exp( $\beta_{3t1}$ ) (Days 0-2)</td><td>1.621***</td><td>1.081**</td><td>1.040**</td><td>1.004</td></tr><tr><td>(0.932)</td><td>(0.976)</td><td>(0.988)</td><td>(0.992)</td></tr><tr><td rowspan="2">Exp( $\beta_{3t2}$ ) (Days 3-5)</td><td>1.362***</td><td>1.053</td><td>1.024</td><td>0.989</td></tr><tr><td>(0.941)</td><td>(0.971)</td><td>(0.985)</td><td>(0.990)</td></tr><tr><td rowspan="2">Exp( $\beta_{3t3}$ ) (Days 6-8)</td><td>1.190**</td><td>1.029</td><td>1.011</td><td>1.003</td></tr><tr><td>(0.945)</td><td>(0.971)</td><td>(0.984)</td><td>(0.990)</td></tr><tr><td rowspan="2">Exp(Constant)</td><td>0.636***</td><td>0.754***</td><td>0.831***</td><td>0.814***</td></tr><tr><td>(0.900)</td><td>(0.956)</td><td>(0.967)</td><td>(0.967)</td></tr><tr><td>Observations</td><td>5271</td><td>12505</td><td>27076</td><td>55385</td></tr><tr><td> $R^2$ </td><td>0.109</td><td>0.027</td><td>0.013</td><td>0.011</td></tr><tr><td>F</td><td>14.46</td><td>8.545</td><td>11.16</td><td>11.23</td></tr></table>

Standard errors in parentheses (clustered at the review event)  
\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

To better illustrate the significance of an increase in SRR, we can estimate the actual level of demand of a book i at time t from its SalesRank (, using the known conversion equation from Goolsbee and Chevalier (2003) and Brynjolfsson et al. (2009). Goolsbee and Chevalier (2003) suggest the following log-linear conversion model:

$$
\operatorname{Log} \left[ \text { Demand } _ {i t} \right] = a + b \operatorname{Log} \left[ \text { SalesRank } _ {i t} \right]
$$

Their approach is based on making a Pareto distribution (i.e., power law) assumption about the probability distribution of book sales, and then fitting some demand data to this distribution. Brynjolfsson et al. (2009) use book sales data from 2008, provided by a publisher selling on Amazon.com, to estimate the parameters; they obtain a = 8.046, b = -0.613. Hence, an increase of X% in SRR translates (using those conversion equations) to a change of about 0.9 times X% in the demand ratio. For example, a 78.6% increase in SRR will be translated to an increase of 70.74% in sales.

Thus, the extent to which an exogenous shock diffuses to the reviewed product’s network neighbors, as reflected in the coefficients of the estimators, diminishes as we move to neighbors that are more distant. Overall, these results suggest that the shock is limited to a small environment of neighbors that are up to three or four links away from the reviewed book. No significant effect was found five links away from the reviewed book. Note that for third and fourth neighbors we see a positive and significant coefficient only for the second (t ) and third (t ) time periods and have no evidence for the existence of a significant shock on these neighbors within the first three days after the review event. This might suggest a lag in the impact of the shock for neighbors that are more distant.

Similarly, in the model estimation using the network structure as the control (Table 3), the coefficients for the difference-indifferences estimators are significant and positive with a notable decrease in coefficient size as (1) time elapses after the exogenous shock and (2) the distance from a focal book increases. For example, compared to the control sample, a first neighbor (distance one) has a 62.1% increase in SRR within the first three days (t ) after the book review, a 36.2% increase in SRR within the following three days (t<sub>2</sub>), and a 19% increase in SRR within six to eight days (t ) after the shock.

## Robustness Tests

In order to confirm the robustness of our results to any additional unaccounted-for bias attributable to unobserved book characteristics, we conducted the Rosenbaum sensitivity analysis (Rosenbaum 2002). Specifically, we follow DiPrete and Gangl (2004), who extend the Rosenbaum bounds approach to test sensitivity for continuous-outcome variables. Adopting this approach allows us to determine how strongly an unmeasured confounding variable gamma (Γ) must affect selection into treatment in order to undermine the conclusions about causal effects from our matching analysis. Stated differently, the Rosenbaum sensitivity analysis estimates the maximum scale of the hidden bias Γ that our results can withstand and still be significant.

Using Wilcoxon’s signed rank test, the sensitivity analysis shows that the results of our study become sensitive to unobserved bias at Γ = 3.55 (where Γ = 1 represents no hidden bias, i.e., the case in which books are randomly selected for inclusion in the treatment group). This means that our results are robust to hidden bias—expressed as the odds ratio by which Amazon’s recommendation system selects books into treatment groups as opposed to groups used as control—of up to that size (i.e., 3.55).

Second, we repeated these analyses using estimated demand rather than Sales Rank. Prior research has suggested equations to convert Sales Rank data into demand estimations (Brynjolfsson et al. 2003; Brynjolfsson et al. 2009; Goolsbee and Chevalier 2003; see Appendix D for details). We therefore repeated each analysis presented in this paper twice: once using the demand estimations suggested in Brynjolfsson et al. (2003), and once using the demand estimations suggested in Brynjolfsson et al. (2009). We did not find changes in the magnitude or signs of coefficients; all results are available upon request.

Finally, we also sought to determine whether our results might have been affected by books’ popularity, that is, to examine whether a (non-reviewed) book’s popularity influences its susceptibility to a shock that takes place in its local network. This direction was motivated by recent work by Bapna and Umyarov (2015) and Aral and Walker (2012) in the context of social networks. Those studies, in contrast to much of the literature, did not focus solely on the popularity of the source of influence but rather raised the question of the susceptibility of the individual being influenced. We followed the methodology presented in Bapna and Umyarov, who suggested a nonparametric test to showcase heterogeneity in the data as a result of treatment. We looked at two measures of popularity: the book’s Sales Rank and the book’s indegree. Our results showed no association between popularity of the books in the network and the treatment effect.

## Concluding Remarks

This paper investigated the online contagion of exogenous demand shocks created by media events. Recent literature on diffusion in networks has called into question the reach of social influence beyond directly linked entities and triggered a discussion regarding the depth of network contagion. However, any attempt to empirically quantify the depth of diffusion in networks must overcome the significant challenges associated with the inherent endogeneity of the influence process. We used a series of over 100 exogenous demand shocks to be able to identify and measure the depth of spillover in product networks and distinguished this effect from variation caused by hidden product complementarities. The shocks were created by media events, specifically, book reviews featured on The Oprah Winfrey Show or in the “Sunday Book Review” section of The New York Times. We studied the impact and spillover effects of these events on the demand for books that were not explicitly mentioned in a review but were located “close” to reviewed books in the online co-purchase product network of Amazon. Our identification strategy was based on a difference-in-differences extension of propensity-score-based matching as well as utilizing the network structure. We found that, on average, the spillover effect of a demand shock was limited to a relatively small area around the source of the shock.

Our findings carry important managerial implications. From the retailer’s perspective, they may carry implications as to inventory and pricing decisions preceding media events. Publishers, who sell multiple books, may use the product network structure in order to better allocate advertising budgets to maximize their total revenue. More broadly, our work may also carry implications regarding ad sales on those product pages. After all, if a product’s page is about to experience a shock in terms of the amount of attention it receives, ad placement and pricing should be planned accordingly.

Our approach to creating experiment-like data from traditional archived data provides interesting opportunities and benefits for future scholars. Our methodology offers significant advantages over traditional regression-based methodologies in addressing the endogeneity issue, especially in a social networks context. It therefore opens up a variety of research settings that could otherwise not be applicable. Unlike natural experiments in which factors outside the control of the investigators determine the conditions of the experiment, the use of archival data to retrospectively create experimental and control conditions is significantly more flexible. This work also points to interesting avenues for future research. One question is whether there are similar spillover patterns to negative reviews as well. Specifically, future work could incorporate semantic analysis and study the effect of sentiment on the depth of spillover effects. Future work could also study the effect of a shock on the resulting future network structure and link the changes in structure to future demand. In addition, it would be interesting to explore whether a positive review of one product leads to lower sales of another due to substitution. Studying those questions could enrich our understanding of exogenous shocks in online product networks. Finally, at the time of data collection, Amazon’s shipping policy offered free shipping for purchases of \$25 or more. Interestingly, we find that more than 93% of our reviewed books had a sale price of under \$25 and at the same time, in over 99% of cases, the sum of the price of the reviewed book and the price of any book in the local network exceeded the \$25 free shipping threshold. Clearly, Amazon’s shipping policy contributes to consumers’ motivation to continue searching for an additional book after having selected a book for purchase. Future work could focus on the connection between different website shipping policies and resulting spillovers in demand.

## References

Aral, S., Muchnik, L., and Sundararajan, A. 2009. “Distinguishing Influence-Based Contagion from Homophily-Driven Diffusion in Dynamic Networks,” Proceedings of the National Academy of Sciences USA (106), pp. 21544-1549.

Aral, S., and Walker, D. 2012. “Identifying Influential and Susceptible Members of Social Networks,” Science (337:6092), pp. 337-341.

Bakshy, E., Hofman, J. M., Mason, W. A., and Watts, D. J. 2011. “Everyone’s an Influencer: Quantifying Influence on Twitter,” in Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, New York: ACM, pp. 65-74.

Balogh, S. 2008. “Oprah Winfrey Rallies Voters for Barack Obama,” Herald Sun, February 5 (http://www.news.com.au/ national/women-bat-for-obama/story-e6frfkp9-1111115473349).

Bapna, R., and Umyarov, A. 2015. “Do Your Online Friends Make You Pay? A Randomized Field Experiment in an Online Music Social Network,” Management Science (61:8), pp. 1902-1920.

Brynjolfsson, E., Hu, Y., and Smith, M. 2003. “Consumer Surplus in the Digital Economy: Estimating the Value of Increased Product Variety at Online Booksellers,” Management Science (49:11), pp. 1580-1596.

Brynjolfsson, E., Hu, Y., and Smith, M. 2009. “A Longer Tail?: Estimating the Shape of Amazon’s Sales Distribution Curve in 2008,” in Proceedings of the 2009 Workshop on Information Systems and Economics.

Chellappa, R., and Saraf, N., 2010. “Alliances, Rivalry, and Firm Performance in Enterprise Systems Software Markets: A Social Network Approach,” Information Systems Research (21:4), pp. 849-871.

Chollete, L. 2009. “The Propagation of Financial Extremes: An Application to Subprime Market Spillovers,” Discussion Paper, Norwegian School of Economics and Business Administration (https://ideas.repec.org/p/hhs/nhhfms/2008\_002.html).

Christakis, N., and Fowler, J. 2007. “The Spread of Obesity in a Large Social Network over 32 years,” New England Journal of Medicine (357), pp. 370-379.

Cointet, J. P., and Roth, C. 2007. “Information Diffusion on Realistic Networks,” in Proceedings of AlgoTEL 9<sup>th</sup> Francophone Summit on Algorithms for Telecommunications, The Centre for Research in Social Simulation.

Dellarocas, C., Katona, Z., and Rand, W. 2012. “Media, Aggregators and the Link Economy: Strategic Hyperlink Formation in Content Networks,” Working Paper, University of Maryland.

Deschatres, F., and Sornette, D. 2005. “Dynamics of Book Sales: Endogenous Versus Exogenous Shocks in Complex Networks,” Physical Review E (72), p. 016112.

DiPrete, T., and Gangl, M. 2004. “Assessing Bias in the Estimation of Causal Effects: Rosenbaum Bounds on Matching Estimators and Instrumental Variables Estimation with Imperfect Instruments,” Sociological Methodology (34), pp. 271-310.

Fowler, J., and Christakis, N. 2010. “Cooperative Behaviour Cascades in Human Social Networks,” Proceedings of the National Academy of Sciences USA (107), pp. 5334-5338.

Garg, R., Smith, M. D., and Telang, R. 2011. “Measuring Information Diffusion in an Online Community,” Journal of Management Information Systems (28:2), pp. 11-38.

Goel, S., Watts, D. J., and Goldstein, D. G. 2012. “The Structure of Online Diffusion Networks,” paper presented at the 13<sup>th</sup> ACM Conference on Electronic Commerce, Valencia, Spain.

Ghose, A., and Gu, B. 2006. “Search Costs, Demand Structure and Long Tail in Electronic Markets: Theory and Evidence,” NET Institute Working Paper No. 06-19.

Ghose, A., Smith, M., and Telang, R. 2006. “Internet Exchanges for Used Books: An Empirical Analysis for Product Cannibalization and Social Welfare,” Information Systems Research (17:1), pp. 3-19.

Goldenberg, J., Oestreicher-Singer, G., and Reichman, S. 2012. “The Quest for Content: How User-Generated Links Can Facilitate Online Content Exploration,” Journal of Marketing Research (49:4), pp. 452-468.

Goolsbee, A., and Chevalier, J. 2003. “Measuring Prices and Price Competition Online: Amazon and Barnes and Noble,” Quantitative Marketing and Economics (1:2), pp. 203-222.

Heckman, J., Ichimura, H., and Todd, P. 1998. “Matching as an Econometric Evaluation Estimator,” Review of Economic Studies (65:2), pp. 261-294.

Illouz, E. 2003. Oprah Winfrey and the Glamour of Misery: An Essay on Popular Culture, New York: Columbia University Press.

Jeger, M. J., Pautasso, M., Holdenrieder, O., and Shaw, M. W. 2007. “Modelling Disease Spread and Control in Networks: Implications for Plant Sciences,” New Phytologist (174:2), pp. 279-297.

Leskovec, J., Adamic, L., and Huberman, B. 2007. “The Dynamics of Viral Marketing,” ACM Transactions on the Web (1:1).

Leskovec, J., Singh, A., and Kleinberg, L. 2006. “Patterns of Influence in a Recommendation Network,” Advances in Knowledge Discovery and Data Mining (3918), pp. 380-389.

Leuven, E., and Sianesi, B. 2003. “PSMATCH2: Stata Module to Perform Full Mahalanobis and Propensity Score Matching, Common Support Graphing, and Covariate Imbalance Testing, 2 Statistical Software Components S432001, Department of Economics, Boston College.

Libai, B., Muller, E., and Peres, R. 2013. “Decomposing the Value of Word-of-Mouth Seeding Programs: Acceleration Versus Expansion,” Journal of Marketing Research (50:2), pp. 161-176.

Lin, Z., Goh, K. Y., and Heng, C. S. 2017. “The Demand Effects of Product Recommendation Networks: An Empirical Analysis of Network Diversity and Stability,” MIS Quarterly, forthcoming.

Lloyd, A. L., and May, R. M. 2001. “Epidemiology: How Viruses Spread among Computers and People,” Science (292), pp. 1316-1317.

Mayzlin, D., and Yoganarasimhan, H. 2012. “Link to Success: How Blogs Build an Audience by Promoting Rivals,” Management Science (58:9), pp. 1651-1668.

Meyer, B. D. 1995. “Natural and Quasi-Experiments in Economics,” Journal of Business and Economics Statistics (13:2), pp. 151-161.

Moe, W. 2003. “Buying, Searching, or Browsing: Differentiating Between Online Shoppers Using In-Store Navigational Clickstream,” Journal of Consumer Psychology (13:1&2), pp. 29-40.

Moe, W., and Fader. P. F. 2004. “Dynamic Conversion Behavior at E-Commerce Sites,” Management Sciences (50:3), pp. 326-335.

Oestreicher-Singer, G., and Sundararajan, A. 2012a. “Recommendation Networks and the Long Tail of Electronic Commerce,” MIS Quarterly (36:2), pp. 65-83.

Oestreicher-Singer, G., and Sundararajan, A. 2012b. “The Visible Hand? Demand Effects of Recommendation Networks in Electronic Markets,” Management Science (58), pp. 1963-1981.

Oh, J., Susarla, A., and Tan, Y. 2012. “Social Networks and the Diffusion of User-Generated Content: Evidence from YouTube,” Information Systems Research (23:1), pp. 23-41.

Pearl, J. 2009. “Understanding Propensity Scores,” in Causality: Models, Reasoning, and Inference (2<sup>nd</sup> ed.), New York: Cambridge University Press, pp. 348-352.

Rooney, K. 2005. Reading with Oprah: The Book Club That Changed America, Fayetteville, AK: University of Arkansas Press.

Rosenbaum P. R. 2002. Design of Observational Studies, New York: Springer.

Rosenbaum, P., and Rubin, D. 1983. “The Central Role of the Propensity Score in Observational Studies for Causal Effects,” Biometrika (70:1), p. 41-55.

Sorensen, A., and Rasmussen, S. 2004. “Is Any Publicity Good Publicity? A Note on the Impact of Book Reviews,” Working Paper, Stanford University.

Sundararajan, A., Provost, F., Oestreicher-Singer, G., and Aral, S. 2013. “Information in Digital, Economic and Social Networks,” Information Systemsn Research (24:4), pp. 883-905.

Yoganarasimhan, H. 2012. “Impact of Social Network Structure on Content Propagation: A Study Using YouTube Data,” Quantitative Marketing Economics (10:1), pp. 111-150.

## About the Authors

Eyal Carmi is a Tech Lead and Manager on the Google Knowledge Graph project in the Search group at Google NYC. He works on projects related to search quality, ranking, open-domain question answering, applied natural language processing and machine learning, structured data and large-scale network analysis, and graph mining. He received his Ph.D. from the School of Management at Tel-Aviv University and was a visiting scholar at the Stern School of Business at New York University. He also holds a M.Sc. from the School of Computer Science, Tel-Aviv University. His research interests are in the field of economics of IS, in particular, eCommerce, network structure, information diffusion, and econometric analysis.

Gal Oestreicher-Singer is an associate professor at Tel Aviv University’s School of Management. Her research studies the effects of visible networks on electronic markets and the economics of digital rights management. Her prior research has won the 2008 ACM SIGMIS Best Dissertation Award, European Union Marie Curie Early Career Award, an INFORMS CIST Best Paper Award, an ICIS Best Overall Paper award, and a MSI-WIMI User Generated Content Research Competition Award. She received her Ph.D. from New York University in 2008, and holds degrees in law and electrical engineering from the Hebrew University in Jerusalem and Tel Aviv University.

Uriel Stettner is an assistant professor at Tel Aviv University. His research interests include strategic and technological innovation as well as organizational knowledge creation and appropriation. He has published in journals including Strategic Management Journal, Academy of Management Annals, and the International Journal of Industrial Organization and is a frequent reviewer for many scholarly journals including Organization Science, Strategic Management Journal, Strategic Entrepreneurship Journal, Journal of Management Studies, and Journal of Business Venturing. He has had extensive managerial experience and held various technology focused position with several start-up firms operating in the software and semiconductor industries. Uriel received his Ph.D. from Tel Aviv University and completed his post-doctoral research at the Technion – Israel Institute of Technology.

Arun Sundararajan is Professor and the Robert L. and Dale Atkins Rosen Faculty Fellow at New York University’s Leonard N. Stern School of Business, where he is also an affiliated faculty member with the Center for Data Science and the Center for Urban Science and Progress. He has published over 50 peer-reviewed scientific articles. His research has been recognized by six Best Paper awards and two Google Faculty Awards. He has published over 25 op-eds in outlets that include The New York Times, The Financial Times, The Guardian, Wired, Fortune, Le Monde, and El Pais. He has provided expert input about the digital economy as part of Congressional testimony and to a variety of city, state, and federal government agencies. He is a member of the World Economic Forum’s Global Agenda Council for Technology, Values and Policy. His first book, The Sharing Economy, was published by the MIT Press in June 2016.

# IS OPRAH CONTAGIOUS? THE DEPTH OF DIFFUSION OF DEMAND SHOCKS IN A PRODUCT NETWORK

Eyal Carmi Google, 76 Ninth Avenue, New York, NY 10011 U.S.A. {eyal.carmi@gmail.com}

Gal Oestreicher-Singer and Uriel Stettner

Coller School of Management, Tel Aviv University,

Tel Aviv 69978 ISRAEL {galos@tau.ac.il} {urielste@tau.ac.il}

Arun Sundararajan

Stern School of Business, New York University, 44 West 4<sup>th</sup> Street,

New York, NY 10012 U.S.A. {asundara@stern.nyu.edu}

## Appendix A

## Descriptive Statistics

Table A1 depicts comparison statistics on the matched sample versus the treatment groups for each distance. Similarly, Table A2 depicts comparison statistics on the network-based group used as a control versus the treatment groups. The variable Total25 is used to control for Amazon’s \$25 shipping policy, capturing whether the sum of the price of the reviewed book and any of the books in the local network passes the \$25 free shipping threshold; indegree captures the number of books directed to a focal book in the product network; local clustering measures the degree to which books in the product network tend to cluster together to create groups characterized by a their density of ties; same binding indicates whether a purchased book is of the same binding type (e.g., hardcover, paperback) as the reviewed book; sale price controls for the sales price of a purchased book; average rating captures the subjective evaluation of a book as reported by consumers; and sales rank measuring a book’s demand relative to other products.

Table A1. Summary Statistics for the Group Used as a Control Based on a Matched Sample

<table><tr><td rowspan="2"></td><td colspan="4">Control</td><td colspan="4">Treated</td></tr><tr><td>Distance 1</td><td>Distance 2</td><td>Distance 3</td><td>Distance 4</td><td>Distance 1</td><td>Distance 2</td><td>Distance 3</td><td>Distance 4</td></tr><tr><td>Total25</td><td>0.827(0.378)</td><td>0.849(0.358)</td><td>0.861(0.346)</td><td>0.884(0.320)</td><td>0.819(0.385)</td><td>0.836(0.371)</td><td>0.852(0.355)</td><td>0.856(0.351)</td></tr><tr><td>Indegree</td><td>7.599(15.758)</td><td>7.214(15.572)</td><td>6.855(15.406)</td><td>7.229(17.184)</td><td>7.481(14.944)</td><td>6.950(14.794)</td><td>6.792(15.291)</td><td>6.900(16.383)</td></tr><tr><td>Local clustering</td><td>0.450(0.167)</td><td>0.388(0.132)</td><td>0.374(0.128)</td><td>0.365(0.124)</td><td>0.443(0.168)</td><td>0.381(0.132)</td><td>0.368(0.130)</td><td>0.364(0.129)</td></tr><tr><td>Same category</td><td>0.582(0.493)</td><td>0.467(0.499)</td><td>0.458(0.498)</td><td>0.408(0.491)</td><td>0.764(0.425)</td><td>0.605(0.489)</td><td>0.525(0.499)</td><td>0.431(0.495)</td></tr><tr><td>Same binding</td><td>0.401(0.490)</td><td>0.379(0.485)</td><td>0.355(0.479)</td><td>0.333(0.471)</td><td>0.684(0.465)</td><td>0.626(0.484)</td><td>0.556(0.497)</td><td>0.490(0.500)</td></tr><tr><td>Sale price</td><td>2069.605(2515.388)</td><td>1756.587(1691.524)</td><td>1847.640(1808.255)</td><td>1946.760(1918.071)</td><td>1571.420(613.206)</td><td>1568.508(625.593)</td><td>1587.784(735.234)</td><td>1624.669(936.690)</td></tr><tr><td>Average rating</td><td>4.235(0.579)</td><td>4.243(0.561)</td><td>4.226(0.590)</td><td>4.240(0.625)</td><td>4.195(0.534)</td><td>4.171(0.540)</td><td>4.162(0.566)</td><td>4.167(0.558)</td></tr><tr><td>Sales Rank</td><td>116417.400(185952.000)</td><td>129004.200(196460.1)</td><td>158465.200(215149.400)</td><td>181031.200(223633.400)</td><td>76259.260(143612.800)</td><td>86075.950(153471.900)</td><td>96597.280(159435.100)</td><td>113820.500(173966.000)</td></tr></table>

\*Standard errors in parentheses

Table A2. Summary Statistics for the Group Used as a Control Based on Network

<table><tr><td rowspan="2"></td><td colspan="4">Control</td><td colspan="4">Treated</td></tr><tr><td>distance 1</td><td>distance 2</td><td>distance 3</td><td>distance 4</td><td>distance 1</td><td>distance 2</td><td>distance 3</td><td>distance 4</td></tr><tr><td>Total25</td><td>0.836(0.371)</td><td>0.852(0.355)</td><td>0.856(0.351)</td><td>0.865545(0.341145)</td><td>0.819(0.385)</td><td>0.836(0.371)</td><td>0.852(0.355)</td><td>0.856(0.351)</td></tr><tr><td>Indegree</td><td>6.950(14.794)</td><td>6.792(15.291)</td><td>6.900(16.383)</td><td>6.697625(15.75062)</td><td>7.481(14.944)</td><td>6.950(14.794)</td><td>6.792(15.291)</td><td>6.900(16.383)</td></tr><tr><td>Local clustering</td><td>0.381(0.132)</td><td>0.368(0.130)</td><td>0.364(0.129)</td><td>0.35946(0.12478)</td><td>0.443(0.168)</td><td>0.381(0.132)</td><td>0.368(0.130)</td><td>0.364(0.129)</td></tr><tr><td>Same category</td><td>0.605(0.489)</td><td>0.525(0.499)</td><td>0.431(0.495)</td><td>0.382425(0.485986)</td><td>0.764(0.425)</td><td>0.605(0.489)</td><td>0.525(0.499)</td><td>0.431(0.495)</td></tr><tr><td>Same binding</td><td>0.626(0.484)</td><td>0.556(0.497)</td><td>0.490(0.500)</td><td>0.427813(0.494768)</td><td>0.684(0.465)</td><td>0.626(0.484)</td><td>0.556(0.497)</td><td>0.490(0.500)</td></tr><tr><td>Sale price</td><td>1568.508(625.593)</td><td>1587.784(735.234)</td><td>1624.669(936.690)</td><td>1686.151(1203.321)</td><td>1571.420(613.206)</td><td>1568.508(625.593)</td><td>1587.784(735.234)</td><td>1624.669(936.690)</td></tr><tr><td>Average rating</td><td>4.171(0.540)</td><td>4.162(0.566)</td><td>4.167(0.558)</td><td>4.180571(0.582775)</td><td>4.195(0.534)</td><td>4.171(0.540)</td><td>4.162(0.566)</td><td>4.167(0.558)</td></tr><tr><td>Sales Rank</td><td>86075.950(153471.900)</td><td>96597.280(159435.100)</td><td>113820.500(173966.000)</td><td>134070.7(205551.2)</td><td>76259.260(143612.800)</td><td>86075.950(153471.900)</td><td>96597.280(159435.100)</td><td>113820.500(173966.000)</td></tr></table>

\*Standard errors in parentheses

## Appendix B

## Algorithm for Data Collection from Amazon.com

We use two programs for the collection of our data. The first collects graph information and the second collects Sales Rank information. Both use Amazon.com’s XML data service. This service is part of the Amazon Web Services, which gives developers direct access to Amazon’s platform and databases.

Graph Collection: The program that collects the graph starts at a popular book. It then traverses the co-purchase network using a depth-first search. Intuitively, in a depth-first search, one starts at the root (in our case, one popular book was chosen as a seed) and traverses the graph as far as possible along each branch before backtracking. At each page, the crawler gathers and records information for the book whose webpage it is on, as well as the co-purchase links on that page. The ASINs of the co-purchase links are entered into a last-in-first-out (LIFO) stack. If the algorithm finds it is on the page of a product that it has visited already, it “backtracks” and returns to the most recent product for which exploration was not exhausted. The program terminates when the entire connected component of the graph is collected.

For example, in the graph in Figure B1, the nodes are numbered in the order in which the crawler traverses the graph. In this case, collection starts at node 1. Its co-purchase links are nodes 2, 6, and 7. Therefore, these numbers are added to a LIFO stack. The script will then proceed to node 2, whose co-purchases are nodes 3, 4, and 5, and thus, those numbers will be added to the LIFO stack, which will now include 3, 4, 5, 6, and 7. The script will continue to node 3. Since there are no co-purchase links to that node, it will move on to node 4. In the same way, the script will collect data on node 5, node 6 and node 7.

Since node 7 has co-purchase links to nodes 8 and 9 they will be added to the stack. After visiting nodes 8, 9, and 10, data collection will terminate. As can be seen, the script stops only after information about the entire connected component has been collected.

The collection of the entire connected component on Amazon.com takes between 4 and 5 hours. The script is run each day at midnight.

Sales Rank Collection: A second program collects the demand information for all books on the graph at 3-hour intervals for the 24-hour period following the collection of the graph. This script collects the Sales Ranks of all the books that ever appeared in the graph. Therefore, it also tracks the sales of books that are no longer in the graph.

![](/api/attachments/QREHQW4M/fulltext/images/e4f18b79c9a0ea8989e45e56001d2f988eb3cd35edeea03be2d800c7696ac2d9.jpg)  
Figure B1. Illustrates Depth-First Search Used for Graph Traversal

## Appendix C

## Network Statistics

## Co-Purchase Networks

Table C1 presents basic network statistics on each of the daily co-purchase graphs that were collected in the period of 2006–2008. Each daily product network consists of a daily average of 270K books and over 1.2M edges. The average density is very low (\~1.45\*10<sup>-5</sup>) due to the truncation to 5 outgoing links per node<sup>1</sup>; however, the fraction of reciprocal links in the network is very high (55% on average) and the average clustering coefficient is 0.39. These data are reasonable since the network represents co-purchased products.

The global structure of the network is relatively stable over time; we observe a relatively low standard deviation in network properties such as the average clustering coefficient, the average indegree and the fraction of reciprocal links. The degree distribution is stable across days and exhibits a power law shape (see Figure C1 for degree distribution and distribution of betweenness centrality on a sample daily network).

<table><tr><td colspan="6">Table C1. Amazon Co-purchase Networks Statistics</td></tr><tr><td>Variable</td><td># Nodes</td><td># Edges</td><td>Average In Degree</td><td>Fraction of Reciprocal Links</td><td>Average Clustering Coefficient</td></tr><tr><td>Mean</td><td>274,179</td><td>1,246,986</td><td>4.7</td><td>55%</td><td>0.39</td></tr><tr><td>Median</td><td>273,255</td><td>1,230,800</td><td>4.7</td><td>56%</td><td>0.39</td></tr><tr><td>Maximum</td><td>368,760</td><td>1,657,400</td><td>4.8</td><td>56%</td><td>0.40</td></tr><tr><td>Minimum</td><td>120,620</td><td>362,580</td><td>3.5</td><td>43%</td><td>0.27</td></tr><tr><td>Std. Dev.</td><td>40,547</td><td>182,999</td><td>0.1</td><td>2%</td><td>0.01</td></tr><tr><td>Skewness</td><td>-0.37</td><td>-0.71</td><td>-5.3</td><td>-4.56</td><td>-6.46</td></tr><tr><td>Kurtosis</td><td>2.58</td><td>4.43</td><td>42.4</td><td>26.95</td><td>55.09</td></tr><tr><td>Jarque-Bera</td><td>9.80</td><td>55.61</td><td>22,822</td><td>8976</td><td>39355</td></tr><tr><td>Probability</td><td>0.01</td><td>0.00</td><td>0.0</td><td>0.00</td><td>0.00</td></tr><tr><td>Observations</td><td>328</td><td>328</td><td>328</td><td>328</td><td>328</td></tr></table>

$$
\frac {5 n}{n (n - 1)} = \frac {5}{n - 1} \cong 1. 8 \times 1 0 ^ {5}
$$

![](/api/attachments/QREHQW4M/fulltext/images/429b0ea64dab38eaee9c4f68342310adc26a09b9638fc2ee3ab8472c1de875d9.jpg)

![](/api/attachments/QREHQW4M/fulltext/images/59207b835a20a9a68cde3ebf95be74aa966df9608e7ed74abe4a00029b93f8dc.jpg)  
Figure C1. Node Degree Distribution of the Large Connected Component of the Amazon Co-purchase Networks on September 16, 2007. The network has 319,340 nodes and 1,452,602 edges.

## Event Networks

Each review event was cross-referenced with the corresponding network and sales data from Amazon.com and went through a series of manual and automatic cleaning procedures. Details on these procedures are available upon request.

These cleaning procedures resulted in a sample of 123 review events; for each event we extracted a subnetwork from the co-purchase graph starting from the reviewed book and up to a distance of 5 links away (the fifth network neighbor of the reviewed book). Following Deschatres and Sornette (2005), we manually classified the review events into two categories: (1) exogenous shocks and (2) endogenous and multiple shocks (see Figure C2). All econometric models were applied to the final sample of 83 exogenous shocks (40 from the Oprah Winfrey Show and 43 from The New York Times) and to a total of 19,669 books in their subnetworks.

Table C2 presents basic network statistics on the subnetworks up to a distance of five links away (the fifth network neighbor of the reviewed book). The relatively high variance in the average clustering coefficient of these networks (as illustrated in Figure C3) shows that they are significantly different from each other, which may be reflected in the way exogenous shocks diffuse through the network.

![](/api/attachments/QREHQW4M/fulltext/images/83ab1dbc9b59203847f6ff141b38901b0d71c2877398cc4d5ae129eec8b3336a.jpg)

![](/api/attachments/QREHQW4M/fulltext/images/c8fecf7aa11e9d13f6e90d3566851c7fddc54c05e0e7590766d0d2370c46fd17.jpg)  
Figure C2. Reviewed Books Time Series Data, Classified into Two Categories: Exogenous Shocks (top) and Endogenous and Multiple Shocks (bottom)

Table C2. Network Statistics Across the Subnetworks up to the Fifth Network Neighbor for Each of the Reviewed Books’ Events

<table><tr><td colspan="6">Amazon Co-purchase Networks Statistics</td></tr><tr><td>Variable</td><td># Nodes</td><td># Edges</td><td>Average In Degree</td><td>Fraction of Reciprocal Links</td><td>Average Clustering Coefficient</td></tr><tr><td>Mean</td><td>249</td><td>558</td><td>3.6</td><td>48%</td><td>0.33</td></tr><tr><td>Median</td><td>231</td><td>534</td><td>3.6</td><td>47%</td><td>0.31</td></tr><tr><td>Maximum</td><td>813</td><td>1524</td><td>5.0</td><td>80%</td><td>0.84</td></tr><tr><td>Minimum</td><td>8</td><td>40</td><td>3.0</td><td>39%</td><td>0.17</td></tr><tr><td>Std. Dev.</td><td>159</td><td>313</td><td>0.4</td><td>6%</td><td>0.10</td></tr><tr><td>Skewness</td><td>0.72</td><td>0.46</td><td>1.1</td><td>1.62</td><td>1.98</td></tr><tr><td>Kurtosis</td><td>3.33</td><td>2.73</td><td>4.8</td><td>7.77</td><td>9.85</td></tr><tr><td>Jarque-Bera</td><td>11.22</td><td>4.74</td><td>39.7</td><td>170.23</td><td>320.89</td></tr><tr><td>Probability</td><td>0.00</td><td>0.09</td><td>0.0</td><td>0.00</td><td>0.00</td></tr><tr><td>Observations</td><td>123</td><td>123</td><td>123</td><td>123</td><td>123</td></tr></table>

## Appendix D

## Summary Statistics

Summary statistics for a selection of shock constructed variables are given in Table D. We also see that on average, only 19% of the neighbors up to a distance of four clicks belong to the same category as the reviewed book, and only 2% were written by the same author.

To measure category mixing we utilize Amazon’s multi-level category tree (see Table D2 for an example and Table D3 for summary statistics).

Further exploration of the distribution of persistence across different groups of neighbors based on minimal distance from the reviewed book (see Figure D1) shows a considerable amount of variation across books.

Table C1. Summary Statistics for a Selection of Constructed Variables

<table><tr><td>Variable</td><td>Average Sales Rank</td><td>Persistence (Sales Rank)</td><td>SRS</td></tr><tr><td>Mean</td><td>126,759</td><td>1.48</td><td>2.59</td></tr><tr><td>Median</td><td>46,569</td><td>0.00</td><td>1.43</td></tr><tr><td>Max</td><td>4,340,296</td><td>64.00</td><td>477.62</td></tr><tr><td>Min</td><td>10</td><td>0.00</td><td>0.08</td></tr><tr><td>Std. Dev.</td><td>194,163</td><td>4.49</td><td>22.17</td></tr><tr><td>Skewness</td><td>4</td><td>8.14</td><td>66.13</td></tr><tr><td>Kurtosis</td><td>33</td><td>92.05</td><td>4,124.00</td></tr><tr><td>Obs</td><td>19,669</td><td>19,669</td><td>19,669</td></tr></table>

![](/api/attachments/QREHQW4M/fulltext/images/f44b82d5424b461a6cdd4eaa359530285d4cc292e2963ce8e904c9f7e75b77f3.jpg)

![](/api/attachments/QREHQW4M/fulltext/images/2c1c5d46902ce28a9b229bfddf76bd190842eb2da5c97fc19d9159a8b1477fc8.jpg)

![](/api/attachments/QREHQW4M/fulltext/images/a62b2f5b0e5762d0e9b0aa64817f9a8c56b1b3334dfa96725fc2dc29908f8260.jpg)

![](/api/attachments/QREHQW4M/fulltext/images/e3f90d4f3acc64d786a79441a0a37897a01db9a7a00286e31775d94d634bc8c9.jpg)

Defining category similarity is not a trivial task, since books belong to multiple categories at different levels of hierarchy. In the analysis that follows, two books are said to have the same category if they share at least one second-level category path. This definition is relatively liberal and will result in a high fraction of books sharing the same category. We also experimented with several alternative definitions: two books share at least one second-level category path comparing (1) only the top category; (2) only the two top categories; and (3) only the three top categories.

<table><tr><td colspan="2">Table D2. Example of Amazon&#x27;s Multilevel Category Tree, Showing a Subset from the Two Top-Level Categories</td></tr><tr><td>Level 1 Category</td><td>Level 2 Category</td></tr><tr><td>Children&#x27;s Books</td><td>People &amp; Places</td></tr><tr><td>Children&#x27;s Books</td><td>Science, Nature &amp; How It Works</td></tr><tr><td>Children&#x27;s Books</td><td>Animals</td></tr><tr><td>Children&#x27;s Books</td><td>Educational</td></tr><tr><td>Children&#x27;s Books</td><td>Holidays &amp; Festivals</td></tr><tr><td>Literature &amp; Fiction</td><td>History &amp; Criticism</td></tr><tr><td>Literature &amp; Fiction</td><td>Poetry</td></tr><tr><td>Literature &amp; Fiction</td><td>Comic</td></tr><tr><td>Literature &amp; Fiction</td><td>Drama</td></tr><tr><td>Nonfiction</td><td>Education</td></tr><tr><td>Nonfiction</td><td>Social Sciences</td></tr><tr><td>Nonfiction</td><td>Politics</td></tr></table>

<table><tr><td colspan="4">Table D3. Number of Books with at Least (K) Second-Level Categories</td></tr><tr><td>Number of Categories (K)</td><td>Number of Books with at Least K Categories</td><td>Number of Categories (K)</td><td>Number of Books with at Least K Categories</td></tr><tr><td>1</td><td>706,169</td><td>11</td><td>4,521</td></tr><tr><td>2</td><td>637,558</td><td>12</td><td>1,927</td></tr><tr><td>3</td><td>542,354</td><td>13</td><td>823</td></tr><tr><td>4</td><td>403,499</td><td>14</td><td>327</td></tr><tr><td>5</td><td>267,152</td><td>15</td><td>131</td></tr><tr><td>6</td><td>158,153</td><td>16</td><td>50</td></tr><tr><td>7</td><td>86,269</td><td>17</td><td>21</td></tr><tr><td>8</td><td>44,558</td><td>18</td><td>7</td></tr><tr><td>9</td><td>21,603</td><td>19</td><td>4</td></tr><tr><td>10</td><td>10,064</td><td>20</td><td>1</td></tr></table>

Summary statistics for a selection of network/mixing constructed variables are given in Table D4. We also see that, consistently with the findings of Oestreicher-Singer and Sundararajan (2008), on average about 44% of the neighbors up to a distance of five clicks from the reviewed book belong to the same category as the reviewed book, and only 1% were written by the same author.

<table><tr><td colspan="6">Table D4. Summary Statistics for a Selection of Constructed Variables</td></tr><tr><td>Variable</td><td>Network Proximity</td><td> $CC_i$ </td><td>Same Author</td><td>Same Category</td><td>Same Price</td></tr><tr><td>Mean</td><td>0.018</td><td>0.54</td><td>0.01</td><td>0.44</td><td>0.84</td></tr><tr><td>Median</td><td>0.001</td><td>0.53</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>Max</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Min</td><td>0</td><td>0.023</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Std. Dev.</td><td>0.08</td><td>0.17</td><td>0.12</td><td>0.5</td><td>0.37</td></tr><tr><td>Skewness</td><td>9.04</td><td>-0.02</td><td>8.46</td><td>0.24</td><td>-1.82</td></tr><tr><td>Kurtosis</td><td>101.38</td><td>3.29</td><td>72.54</td><td>1.06</td><td>4.31</td></tr><tr><td>Obs.</td><td>19669</td><td>19669</td><td>19669</td><td>19669</td><td>19669</td></tr></table>

Breaking down category and author statistics (see Table D5), one can see that the percentage of books in the same category as the reviewed book drops as the distance from the reviewed book increases. An even sharper drop is seen (as expected) for books with the same author: The percentage of books with the same author among first neighbors is significantly higher.

Table C5. Category and Author Mixing Statistics by Distance from the Reviewed Book

<table><tr><td></td><td colspan="3">Same Category Statistics</td><td colspan="3">Same Author Statistics</td></tr><tr><td>Distance</td><td>All</td><td>Oprah Reviews</td><td>New York Times Reviews</td><td>All</td><td>Oprah Reviews</td><td>New York Times Reviews</td></tr><tr><td rowspan="2">All neighbors (1...5)</td><td>43.9%</td><td>44.4%</td><td>43.7%</td><td>1.3%</td><td>1.8%</td><td>1.1%</td></tr><tr><td>(0.4%)</td><td>(0.6%)</td><td>(0.4%)</td><td>(0.1%)</td><td>(0.2%)</td><td>(0.1%)</td></tr><tr><td rowspan="2">1</td><td>76.6%</td><td>80.4%</td><td>73.1%</td><td>20.7%</td><td>22.5%</td><td>19.3%</td></tr><tr><td>(2.1%)</td><td>(2.9%)</td><td>(3.0%)</td><td>(2.0%)</td><td>(3.1%)</td><td>(2.7%)</td></tr><tr><td rowspan="2">2</td><td>60.5%</td><td>63.6%</td><td>58.4%</td><td>4.6%</td><td>4.3%</td><td>4.8%</td></tr><tr><td>(1.5%)</td><td>(2.3%)</td><td>(2.0%)</td><td>(0.6%)</td><td>(1.0%)</td><td>(0.9%)</td></tr><tr><td rowspan="2">3</td><td>52.1%</td><td>54.6%</td><td>50.8%</td><td>0.9%</td><td>0.6%</td><td>1.1%</td></tr><tr><td>(1.0%)</td><td>(1.7%)</td><td>(1.3%)</td><td>(0.2%)</td><td>(0.3%)</td><td>(0.3%)</td></tr><tr><td rowspan="2">4</td><td>43.9%</td><td>42.3%</td><td>44.6%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>(0.7%)</td><td>(1.2%)</td><td>(0.8%)</td><td>(0.1%)</td><td>(0.1%)</td><td>(0.1%)</td></tr><tr><td rowspan="2">5</td><td>38.6%</td><td>37.0%</td><td>39.3%</td><td>0.1%</td><td>0.0%</td><td>0.1%</td></tr><tr><td>(0.5%)</td><td>(0.9%)</td><td>(0.6%)</td><td>(0.0%)</td><td>(0.0%)</td><td>(0.0%)</td></tr></table>

\*Standard errors between parentheses.

## Appendix E

## Sales Rank Conversion to Demand

To estimate the actual level of demand Demand of a book i at time t on the basis of the book’s SalesRank (SR ), the following log-linear conversion model was suggested (Brynjolfsson et al. 2003; Goolsbee and Chevalier 2003):

$$
\operatorname{Log} \left[ \text { Demand } _ {i t} \right] = a + b \operatorname{Log} \left[ \text { SalesRank } _ {i t} \right]
$$

This equation to convert Sales Rank data into demand estimations was first introduced by Goolsbee and Chevalier 2003. Their approach was based on making an assumption about the probability distribution of book sales, and then fitting some demand data to this distribution. They chose the standard distributional assumption for this type of rank data, which is the Pareto distribution (i.e., power law).

In a later study, Brynjolfsson et al. (2003) used data provided by a publisher selling on Amazon.com to conduct a more robust estimation of the parameters of the equation. They estimated the following parameters based on book sales data from 2000: a = 10.526, b = -0.871.

This conversion model has been used in many studies (see for example, Oestreicher-Singer and Sundararajan 2008; Sornette et al. 2004). However, estimating the actual level of demand is still not a trivial process, since demand patterns in electronic commerce tend to change over time, and the model may need to be updated. Brynjolfsson et al. (2009) recently carried out the estimation a second time, using the above loglinear model, and they found that the “long tail” of Internet book sales has gotten longer over the years. They estimated the coefficients based on book sales data from 2008 as: a = 8.046, b = -0.613.

The authors also suggested a new methodology to better fit the relationship between Sales Rank and sales: using a series of splines, each modeled as a negative binomial regression model (rather than a linear regression). Figure E1 shows the difference between the two estimations, computed over the average Sales Rank of each of the books in our final sample. We can see that our sample spans across a wide range of Sale Rank values and that the two curves cross each other when the Sales Rank equals 14,949.

There are several other known issues regarding the use of converted demand estimations, especially for best-selling books (see the discussion in Chellappa and Chen 2008; Rosenthal 2010; Sornette et al. 2004). These pose a more severe problem in our context, as several of the reviewed books attained best-seller status. We therefore directly use SalesRankRatios to compute the different variables.

Summary statistics for some of the constructed variables are given in Table E1 together with their demand-based counterparts (that is, demand estimated using the suggested estimates from Brynjolfsson et al. (2003) and the suggested estimates from Brynjolfsson et al. (2009)). We can see that the changes in estimation of the demand and Sales Rank actually translate to small changes in the computed persistence. This can also be seen when plotting the distribution of persistence based on each of the three estimation methods (see Figure E2).

Table E1. Summary Statistics for a Selection of Constructed Variables  
![](/api/attachments/QREHQW4M/fulltext/images/8f44f0c1adf08223cc277f18ff8e6f01d92b03bb87a7da5243fa7d90fc7ebdc1.jpg)

![](/api/attachments/QREHQW4M/fulltext/images/544f1d0dccec623c908b01e995b347f017637b63916d725a99edfaa4fb19a36b.jpg)

Figure E1. Sales Rank Conversion to Demand Using 2008 Estimation Versus 2000 Estimations (The graphs present the conversion of the average Sales Rank of the books in our final sample to demand using the two estimations. The same data are presented in (a) normal scale (zoomed in to the range of 0 … 5,000) and (b) logarithmic scale.)

<table><tr><td>Variable</td><td>Mean</td><td>Median</td><td>Max</td><td>Min</td><td>Std. Dev.</td><td>Skewness</td><td>Kurtosis</td><td>Obs</td></tr><tr><td>Average Sales Rank</td><td>126,759</td><td>46,569</td><td>4,340,296</td><td>10</td><td>194,163</td><td>3.67</td><td>32.83</td><td>19669</td></tr><tr><td>Average Demand (2003)</td><td>116.33</td><td>4.34</td><td>27404.55</td><td>0.06</td><td>572.38</td><td>18.66</td><td>669.32</td><td>19669</td></tr><tr><td>Average Demand (2009)</td><td>30.79</td><td>5.17</td><td>2360.51</td><td>0.27</td><td>86.83</td><td>7.12</td><td>95.34</td><td>19669</td></tr><tr><td>Persistence (Sales Rank)</td><td>1.476</td><td>0.000</td><td>64.000</td><td>0.000</td><td>4.486</td><td>8.14</td><td>92.05</td><td>19669</td></tr><tr><td>Persistence (Demand 2003)</td><td>1.332</td><td>0.000</td><td>64.000</td><td>0.000</td><td>4.045</td><td>8.84</td><td>111.57</td><td>19669</td></tr><tr><td>Persistence (Demand 2009)</td><td>1.365</td><td>0.000</td><td>64.000</td><td>0.000</td><td>4.093</td><td>8.68</td><td>107.93</td><td>19669</td></tr></table>

(a) Persistence (Sales Rank)  
![](/api/attachments/QREHQW4M/fulltext/images/1e9c82e39ae4317d818f19868b7a9b5a44d10dc643a6a0e148a984f2712d8e86.jpg)

(b) Persistence (Demand 2003)  
![](/api/attachments/QREHQW4M/fulltext/images/e093ba519638e4b4ac1f06e6d2e6754243ea2574bb98f0d51c5cc29782a2940f.jpg)

(c) Persistence (Demand 2009)  
![](/api/attachments/QREHQW4M/fulltext/images/b7319202414d166ebae9eea6d1b7afeb2f591c12c67e7d3293f49537d6dd6a2f.jpg)

Figure E2. Distribution of Persistence of the Shock Based on (a) Sales Rank, (b) Estimated Demand Using Brynjolfsson et al. (2003), and (c) Estimated Demand Using Brynjolfsson et al. (2009)

## References

Brynjolfsson, E., Hu, Y., and Smith, M. 2003. “Consumer Surplus in the Digital Economy: Estimating the Value of Increased Product Variety at Online Booksellers,” Management Science (49:11), pp. 1580-1596.

Brynjolfsson, E., Hu, Y., and Smith, M. 2009. “A Longer Tail? Estimating the Shape of Amazon’s Sales Distribution Curve in 2008,” in Proceedings of the Workshop on Information Systems and Economics, Phoenix, AZ, December 14-16.

Chellappa, R. K., and Chen, C. 2008. “On the Temporal Nature of Sales-Rank Relationships of Albums and Digital Tracks in the Music Industry: The Relevance of Billboard Charts Post-Digitization,” in Proceedings of the INFORMS Annual Meeting, Washington, DC.

Deschatres, F., and Sornette, D. 2005. “Dynamics of Book Sales: Endogenous Versus Exogenous Shocks in Complex Networks,” Physical Review E 72, 016112.

Goolsbee, A., and Chevalier, J. 2003. “Measuring Prices and Price Competition Online: Amazon and Barnes and Noble,” Quantitative Marketing and Economics (1), pp. 203-222.

Oestreicher-Singer, G., and Sundararajan, A. 2008. “The Visible Hand of Social Networks in Electronic Markets,” Working Paper, New York University.

Rosenthal, M. 2010. “Amazon Sales Rank for Books,” http://www.fonerbooks.com/surfing.htm.

Sornette, D., Deschatres, F., Gilbert, T., and Ageon, Y. 2004. “Endogenous Versus Exogenous Shocks in Complex Networks: An Empirical Test Using Book Sale Rankings. Physical Review Letters 93.228701.

Watts, D. J. 2003. Small Worlds: The Dynamics of Networks between Order and Randomness, Princeton, NJ: Princeton University Press.

Watts, D. J., and Strogatz, S. H. 1998. “Collective Dynamics of ‘Small-World’ Networks,” Nature (393), pp. 440-442.
