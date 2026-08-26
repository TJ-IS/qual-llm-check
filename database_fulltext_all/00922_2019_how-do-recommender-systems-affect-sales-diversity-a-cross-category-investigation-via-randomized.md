---
otero_id: 922
otero_key: "5QCJZEAF"
title: "How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment"
authors: "Dokyun Lee; Kartik Hosanagar"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0800"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.250.144.144] On: 20 April 2019, At: 13:21 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/5QCJZEAF/fulltext/images/f3328b00d4346dd25f3f27ade74762e2a64e2f6c35d9820f75fd4d31e150265e.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment

Dokyun Lee, Kartik Hosanagar

To cite this article: Dokyun Lee, Kartik Hosanagar (2019) How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment. Information Systems Research 30(1):239-259. https://doi.org/10.1287/isre.2018.0800

## Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment

Dokyun Lee,<sup>a</sup> Kartik Hosanagar<sup>b</sup>

<sup>a</sup> Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15293; <sup>b</sup> The Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104

Contact: dokyun@cmu.edu, https://orcid.org/0000-0002-3186-3349 (DL); kartikh@wharton.upenn.edu (KH)

Received: June 23, 2015 Revised: June 1, 2017; March 15, 2018 Accepted: June 15, 2018 Published Online in Articles in Advance: March 5, 2019

https://doi.org/10.1287/isre.2018.0800

Copyright: © 2019 INFORMS

Abstract. We investigate the impact of collaborative filtering recommender algorithms (e.g., Amazon’s “Customers who bought this item also bought”) commonly used in e-commerce on sales diversity. We use data from a randomized field experiment run on the website of a top retailer in North America across 82,290 products and 1,138,238 users. We report four main findings. First, we demonstrate and quantify across a wide range of product categories that the use of traditional collaborative filters (CFs) is associated with a decrease in sales diversity relative to a world without product recommendations. Furthermore, the design of the CF matters. CFs based on purchase data are associated with a greater effect size than those based on product views. Second, the decrease in aggregate sales diversity may not always be accompanied by a corresponding decrease in individual-level consumption diversity. In fact, it is even possible for individual consumption diversity to increase while aggregate sales diversity decreases. Third, copurchase network analyses show that while recommenders can help individuals explore new products, similar users still end up ex ploring the same kinds of products, resulting in concentration bias at the aggregate level. Fourth and finally, there is a difference between absolute and relative impact on niche items. Specifically, absolute sales and views for niche items in fact increase, but their gains are smaller compared with the gains in views and sales for popular items. Thus, whereas niche items gain in absolute terms, they lose out in terms of market share. We discuss economic impacts and managerial implications.

Funding: The authors gratefully acknowledge financial support from the Jay H. Baker Retailing Center, the Wharton Risk Management and Decision Processes Center, the Mack Institute for Innovation Management, and the Fishman-Davidson Center for Service and Operations Management. History: Gediminas Adomavicius, Senior Editor; Wolfgang Ketter, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2018.0800.

Keywords: e-commerce • personalization • recommender systems • sales diversity • consumer purchase behavior • collaborative <sup>fi</sup>ltering Gini coef<sup>fi</sup>cient

## 1. Introduction

Recommender systems (RS) are widely used across a number of industries, ranging from online retail (e.g., Amazon’s product recommendations), to music (e.g., Spotify’s weekly recommendations), video streaming (e.g., YouTube and Netflix), and news (e.g., Google News). These systems attempt to predict items of interest to users based on information about the users and items. The most common recommender design used in e-commerce is the collaborative filter, which is a recommender that finds other users whose product views or purchases are most similar to the focal user and recommends other items that they have viewed or purchased (Schafer et al. 1999). Examples include Amazon’s “people who bought X also bought Y” and Netflix’s “people like you liked X.”

Recommenders are an interesting example of a marketing technology that offers significant value to both consumers and firms. For consumers, recommenders help them learn about new products (Resnick and Varian 1997) and sort through large choice sets (Haubl and¨ Trifts 2000). For firms, they help convert browsers to buyers (Tam and Ho 2005, Dias et al. 2008, De et al. 2010, Pathak et al. 2010, Oestreicher-Singer and Sundararajan 2012), promote cross-selling (Pathak et al. 2010), and increase loyalty by providing a custom browsing experience (Schafer et al. 1999). As a result, most of the major online firms use recommenders. A recent survey indicated that 94% of the top e-commerce companies agree that personalization is critical to their success online.<sup>1</sup> They also indicate that recommenders have a major impact on consumer choice—for example, 60% of media choices on Netflix (Thompson 2008) and nearly 35% of sales at Amazon (Lamere and Green 2008) originate from recommendations.

Whereas we know that recommenders influence in dividual choice, there is growing interest in understanding how they affect sales diversity, i.e., the overal distribution of sales. Some believe recommender systems will help consumers discover new products by lowering their search costs (Anderson 2008, Brynjolfsson et al. 2011). For example, in the book The Long Tail, Chris Anderson suggests that “the main effect of recommenders will be to help people move from the world of hits to the world of niches.” On the other hand, another viewpoint holds that common recommender systems—in particular collaborative filters (CFs)—will decrease sales diversity (Mooney and Roy 2000, Celma and Cano 2008, Fleder and Hosanagar 2009, Wu et al. 2011). Hosanagar and Fleder present an analytical model and simulation study to show that CFs only reinforce the popularity of already well-known titles. They argue that this is because CFs rely on past purchase or view data and cannot recommend items with limited historical information. Pariser (2011) similarly argues that various forms of online personalization, including recommender systems, confine users into an echo chamber or a “filter bubble,” in which they are repeatedly presented with content they usually consume.

The issue of sales diversity has interesting implications for the fields of marketing, information systems (IS), and operations management (OM). In marketing, there has been a lot of interest in understanding sales concentration and the long tail phenomenon and their implications (Van Herpen and Pieters 2002, Borle et al. 2005, Jiang et al. 2011) for consumer surplus (Elberse 2008). If recommender systems lower consumers’ search costs and help them find better product matches that they would have otherwise missed, then they are a highly appealing marketing technology. From an IS standpoint, we are interested in understanding whether the tacit design choices we make for decision support tools have a marked impact on consumer product consumption patterns. From an OM perspective, to the extent that these systems change sales diversity, there are implications for the firms’ product assortment (Walter et al. 2012, Jiang et al. 2014). In addition, recent research has shown that inventory levels and inventory costs increase with sales dispersion (Kok et al. 2008, Walter et al. 2012, Gallino et al. 2017) and, further, different levels of sales dispersion can call for different supply chain structures (Fisher 2003). Thus, there can be significant operational adjustments needed in response to sales distribution changes caused by recommenders.

Despite the interest in the topic and its potential implications, there exists little to no empirical evidence to date that can help us reconcile these different views on the impact of recommenders on sales diversity. We believe a potential driver of this may be the lack of data that provides a contrast between users exposed and unexposed to recommendations.<sup>2</sup> Without such a contrast, it is hard to empirically identify and quantify recommenders’ impact. Through this study, we make the following contributions to the literature. First, ou empirical investigation via A/B testing identifies both the direction and magnitude of the impact of recommenders on sales diversity, thereby reconciling the different viewpoints from the long tail and recommender literature. Specifically, we use data from randomized field experiment run by a major online retailer to investigate how recommenders affect sales diversity across all the product categories sold on the website. We also show and discuss the quantified changes in sales concentration has significant economic impact. Second, we provide our results on multiple categories of product sold on this site, thereby increasing generalizability and providing the first multicategory large-scale A/B testing empirical result in the literature. Third, because much of the debate on recommenders’ impact on sales diversity is related to CFs, we focus only on CFs in the study. However, even among CFs, there can be designs based on purchases (“Customers who purchased this also purchased”) or views (“Customers who viewed this also viewed”). Accordingly, we also investigate how the design choice of CFs affects the answer by incorporating both viewand purchase-based designs.<sup>3</sup> Throughout the paper, we refer to view-based collaborative filtering as “VBCF” and purchase-based collaborative filtering as “PBCF.” Fourth, we then explore the mechanism behind the diversity shift across different categories using copurchase network analyses and top N most purchased subcategory market share analyses. Lastly, delving deeper into the impact of recommenders on the long tail phenomenon, we present a nuanced perspective on a recommender’s influence on niche items via looking into absolute sales versus relative sales (market share) and provide implications for managers.

We report four main findings. First, we demonstrate across a wide range of product categories that the use of traditional collaborative filters is associated with a decrease in sales diversity relative to a world without product recommendations. We also quantify the effect. Second, we find that the decrease in aggregate sales diversity may not always be accompanied by a corresponding decrease in individual-level consumption diversity. In fact, it is even possible for individual consumption diversity to increase as aggregate sales diversity decreases. Third, our analysis of the copurchase network shows that while recommenders do help individuals explore new product categories, similar users end up exploring the same kinds of products. Thus, any increase in individual diversity does not show up at an aggregate level because of the correlated exploration across individuals. Fourth, we show that there is a difference between relative and absolute gains for niche items. Specifically, absolute sales and views for niche items, in fact, increase, but their gains are smaller compared with the gains in views and sales for popular items. Thus, while niche items gain in absolute terms, they lose out in terms of market shares. Together, these results present the most comprehensive empirical perspective to date on how traditional collaborative filters affect sales diversity.

These findings have implications for retailers, producers, and recommender designers. Consistent with prior literature, we find that retailers clearly benefit from increased sales under recommendations. However, for retailers whose strategy is to offer greater product variety—under the premise that consumers will find better-suited products—the use of traditional CF designs may not be fully consistent with that strategy. Our results suggest that retailers offering a broader product assortment might benefit from modifying off-the-shelf designs to allow discovery of relevant items with limited historical views and/or purchases. Additionally, to the extent that managers have to optimize inventory based on sales dispersion, as shown by Gallino et al. (2017), our paper serves as a complimentary study to quantify how recommenders may influence sales dispersion. For producers of niche titles, one of the promises of the internet is that such products can be efficiently matched to their customers through online tools, thereby allowing one to profitably produce and sell niche products. However, our results show that producers cannot passively rely on search tools like recommenders. Instead, such producers will need to continue exerting effort to ensure product discovery. Finally, from a design science standpoint, it is useful for system designers to recognize the inherent popularity bias in CFs. If there exist better product matches outside of the relatively popular titles, it might be useful to modify CF designs to ensure discovery of relevant items with limited views and purchases. We point to extant research on different recommender designs to shift sales concentration in our conclusion.

## 2. Prior Work

The vast majority of work on recommenders is focused on their design. A common taxonomy of recommenders broadly classifies them into content-based recommenders and collaborative filtering (CF) algorithms (Adomavicius and Tuzhilin 2005). Content-based systems analyze product attributes to suggest products that are similar in this attribute space to products that a consumer has bought or liked in the past. A drawback of content-based designs is that they need rich metadata about the products, which can be expensive to collect. Furthermore, they do not work well when a retailer sells multiple categories of products.<sup>4</sup> CFs were designed to address these limitations. CFs are unaware of product attributes and recommend products either purchased or liked by similar consumers, where similarity is measured by historical purchase (or like) data. Because they are easy to build and do not require detailed product attribute information, they are the most widely used class of recommenders in e-commerce. Hence, they are also the focus of this study. CFs can themselves be of many types, including those based on item similarity (item-based CFs such as in Sarwar et al. 2001) and those based on user similarity (Breese et al. 1998). Even among item-based CFs, they can be based on product views (“People who viewed this also viewed”) or purchases (“People who bought this also bought”). It is well documented that the demand effects of co-view and copurchase recommendations differ (Lin et al. 2017). This may be because purchase-based CFs are more likely to recommend complementary rather than substitute products (and vice versa for view-based CFs) (Lin et al. 2017). Our study is based on a retailer’s implementation of item-based CF. We consider both view- and purchase-based designs.

While the vast majority of work in computer science has focused on the design of recommender algorithms, an emerging thread of research has started to explore their impact at the individual and market levels. Senecal and Nantel (2004) show experimentally that recommendations do influence choice and that online recommendations can be more influential than human recommendations. Cooke et al. (2002) examine how purchase decisions under recommendations depend on the context and familiarity with the recommended items. De et al. (2010) and Hinz and Eckert (2010) show that this influence on consumer choice is not merely a product substitution effect: They also help drive an increase in sales. While these studies ask how recommenders affect individual choices, our interest is the aggregate effect they have on product markets. In particular, we are interested in how recommenders affect sales diversity.

Brynjolfsson et al. (2006) and Anderson (2008) find that sales diversity can be higher on the internet than in offline channels. They suggest supply-side causes such as the lower cost of offering a wide product assortment and several demand-side causes, such as active tools (search engines) and passive tools (recommender systems). However, they do not isolate the specific effect of recommenders from the other factors. Holding the product supply as fixed, Brynjolfsson et al. (2011) find that sales diversity for an apparel retailer’s internet channel is greater than its catalog channel. Because their interest is also in channel differences, they also do not isolate the effect of recommenders relative to other factors such as search tools. Further more, the retailer in their study did not use a CF. Other studies that suggest recommenders might help increase sales diversity include Hinz and Eckert (2010), Zhou et al. (2010), and Oestreicher-Singer and Sundararajan (2012). In contrast, Fleder and Hosanagar (2009) use simulations to show that CFs are more likely to recommend items that have been viewed or purchased often, thereby reducing sales diversity. Similarly, Celma and Cano (2008), Wu et al. (2011), Jannach et al. (2013) also argue or show that the use of CFs will decrease aggregate sales diversity. Table 1 summarizes these academic papers and their main claims. In sum, there is no consensus among either popular or academic literature on how recommenders will affect sales diversity.

Table 1. Literature on Impact of Recommender Systems and Claims

<table><tr><td>Study</td><td>Method and data</td><td>Sales diversity</td></tr><tr><td>Hinz and Eckert (2010)</td><td>MovieLens data and simulation</td><td>Increased niche product consumption leading to increase in aggregate sales diversity</td></tr><tr><td>Fleder and Hosanagar (2009)</td><td>Theoretical models and simulation</td><td>Decrease in aggregate sales diversity but increase in individual sales diversity</td></tr><tr><td>Hosanagar et al. (2014)</td><td>Archival data and econometrics</td><td>Content-based RS increase aggregate sales diversity and increase overlap/commonality in consumption</td></tr><tr><td>Oestreicher-Singer and Sundararajan (2012)</td><td>Crawled Amazon data and econometrics</td><td>Recommender shifts demand to niche item increasing aggregate sales diversity</td></tr><tr><td>Jannach et al. (2013)</td><td>MovieLens data and simulation</td><td>Different algorithms have different effects</td></tr><tr><td>Wu et al. (2011)</td><td>MovieLens data and simulation</td><td>Mixed result based on different algorithms; collaborative filtering decreases aggregate diversity, whereas content-based increases it</td></tr><tr><td>Celma and Cano (2008)</td><td>last.fm and Allmusic.com API data and correlational analysis</td><td>Collaborative filtering algorithm is linked to popularity bias suggesting decreased aggregate consumption diversity</td></tr><tr><td>Zhou et al. (2010)</td><td>Crawled YouTube data and correlational analysis</td><td>RS increases aggregate consumption diversity</td></tr></table>

We believe this lack of consensus arises for many reasons. First, different studies use different algorithms. While it appears as though content-based recommenders might increase sales diversity (see, for example, Hosanagar et al. 2014), the disagreement appears to be primarily about CFs. Thus, this is the design we study in this paper. Additionally, many studies are based on lab experiments or simulations calibrated to archival data, which makes generalization more difficult. Other studies measure nonpurchase attributes like purchase intentions, use intentions, and satisfaction rather than the actual views or purchases. The few based on field data are constrained by the limitations of observational data including (i) the inability to separate the impact of recommenders from other supply- and demand-side factor, and (ii) the lack of a contrast between users exposed to recommendations and an otherwise similar group of users who are unexposed to recommendations.

In this study, we isolate that effect of recommenders by varying their availability while also holding supplyside factors and other demand-side factors constant. We carry out a randomized field experiment on a large e-commerce website using multiple recommender algorithms. By doing so, we are able to offer compelling evidence that commonly used recommender designs affect sales concentration.

## 3. Problem Statement and Study Design

This section formally sets up research questions, experimental study designs, and empirical strategies.

## 3.1. Research Question

We are interested in studying the impact of recommenders on sales diversity. We measure the sales diversity of the products sold with a measure called the Gini coefficient. The Gini coefficient has been widely adopted in the long tail and RS literature as a measure of sales diversity (Fleder and Hosanagar 2009, Brynjolfsson et al. 2011). It is computed based on the Lorenz curve. Let L u be the Lorenz curve denoting the percentage of the sales generated by the lowest 100u% of items as shown in Figure 1. The Gini coefficient is defined as $\begin{array} { r } { G \equiv \frac { A } { A + B } . } \end{array}$ . It ranges from 0, representing the least amount of concentration or highest diversity, to 1, representing the highest amount of concentration or lowest diversity. A Gini coefficient of 0 means that all products have equal sales, whereas values near 1 mean that a few broad-appeal blockbuster items account for most of the sales.

Figure 1. Lorenz Curve  
![](/api/attachments/5QCJZEAF/fulltext/images/44eac44156ed9e24c73558d12efeb75b7ec35704c3704d699211c6d6ffe1151d.jpg)

We approach this problem with a field experiment in which consumers visiting a website are randomly assigned to a control or treatment group. The treatment group is shown a panel of different recommendations, much like Amazon’s “Customers who bought this item also bought” recommenders. The control group is shown nothing. For each group, we analyze the following variables of interest for sales diversity.

1. Aggregate firm-level view and sales diversity: This measures how the recommenders affect product view/ sales diversity at the aggregate level (for each treatment group) and is measured by the Gini coefficient.

2. Individual average view and purchase diversity: This measures how the recommenders affect the diversity of products individuals view or purchase. Again, the Gini coefficient is used, but it is computed separately for each individual based only on their own purchases.

## 3.2. Treatment Conditions

We compare the sales diversity of users exposed to recommendations with that of another set of users unexposed to recommendations. Note that, in theory, it is always possible to design a recommender that increases concentration (recommend bestsellers) or diversity (recommend items with lowest sales). However, our question is not whether there are designs that can achieve these effects. Instead, our empirical focus is on the impact of common designs. Accordingly, we use item-based CFs in this study. These CF designs have a long history (Sarwar et al. 2001) and continue to be very popular designs even today. There are three groups in our study:

1. Control (no recommendations)

2. View-based collaborative filtering (“People who viewed this item also viewed”) (henceforth VBCF).

3. Purchase-based collaborative filtering (“People who purchased this item also purchased”) (henceforth PBCF).

We have two different treatment groups corresponding to two different recommender algorithms, plus a control group that was not shown any recommendations. One treatment is based on views (“People who viewed this item also viewed”) and the other is based on purchases (“People who purchased this item also purchased”). We consider these two treatments because they are two of the most commonly used types of collaborative filtering algorithms. Furthermore, while both are CF designs, they recommend very different kinds of products, as discussed in Section 2. When we study the impact of recommenders, it is worth asking “relative to what?” We compare sales diversity under these designs against a group that receives no recommendations. This is how the problem has been framed in the literature (Fleder and Hosanagar 2009 Jannach and Hegelich 2009, Hinz and Eckert 2010). One could alternatively study the impact of recommender systems relative to a random recommender or to a system that showcases the most popular items. These alternatives are unappealing for multiple reasons. From a practical perspective, when a consumer is on a specific product page, showing randomly generated recommendations or globally popular items will effectively show irrelevant items. As a result, it is not a format that is used by any retailer that we know of.

Our recommender system implements an item-based collaborative filtering algorithm using Apache Mahout (mahout.apache.org), an open-source, machine learning framework widely used in online retail.<sup>5</sup> The itembased CF we implement in this experiment computes item-item similarity with preexisting consumer purchase/ view data. Then, the algorithm takes as an input, the focal item (the product a user is viewing) and the user’s past product purchases/views. The top N candidate products that are not yet purchased/viewed by the consumer are then recommended. We follow the details as described by Sarwar et al. (2001). Take, for example, VBCF: When a new user first visits a focal item page P with no prior history on the website, the recommendations are generalized and the same for all brand-new users. As the user views different items on the site, the user’s view vector changes. After visiting the website, the view-based recommendations (for the same focal item P) change to a new set of items based on the newly updated view-history vector.

The algorithm uses the purchase/view data of the entire website 60 days prior to the start of the experimentation and the item-item similarity matrix is recomputed every 3 days. The number of products displayed is a function of the width of the user’s screen, but the default is 6. We discuss more details of our treatment setup and data in Section 4. Next, we discuss our empirical strategies given data from this field experiment setup.

## 3.3. Study Design

Let g represent group $i ,$ and let f represent a function that calculates an aggregate measure of interest, $D _ { i } ,$ for the given group (e.g., the group-level purchase Gini coefficient). We define the following quantity of interest:

The difference in the aggregate measure, $D ,$ shows how different Group 1 is from Group 2. Let $\mu \equiv { \mathbb E } [ D ]$ with the distribution of D unknown. All hypotheses testing takes the form:

<table><tr><td>Aggregate measure f of Group 1</td><td> $D_{1} \equiv f(g_{1})$ </td></tr><tr><td>Aggregate measure f of Group 2</td><td> $D_{2} \equiv f(g_{2})$ </td></tr><tr><td>Difference in aggregate measures</td><td> $D \equiv D_{1} - D_{2}$ </td></tr></table>

Note that we carry out the hypotheses tests as twosided tests (equal or not equal rather than greater than or less than) to remain conservative. Furthermore, because we have one aggregate measure (or statistic)

<table><tr><td>Null hypothesis  $H_0$ </td><td> $\mu \equiv \mathbb{E}[D] = 0$ </td></tr><tr><td>Alternate hypothesis  $H_a$ </td><td> $\mu \equiv \mathbb{E}[D] \neq 0$ </td></tr></table>

for each group, in order to produce a p-value, we utilize a permutation test technique (Good 2005) that allows us to calculate a null distribution for a given aggregate measure. We choose to utilize permutation tests because (1) they do not make any distributional assumptions; (2) they can be utilized for any aggregate statistics; and (3) they are well-fitted to handle unbalanced designs, as in our case where there are more control users. The permutation test works as follows. Suppose the null hypothesis is true and control and treated groups are similar: Then, randomly relabeling some control users as treated or treated users as control users is unlikely to affect our test. A permutation test involves repeatedly and randomly relabeling individuals into Groups 1 and 2 (e.g., control and treated) to produce a null distribution for any test statistics. In each iteration, we randomly take half of the sample from the control group and the other half from the treated group. By comparing statistics from null distributions to the actual test statistics from the real distribution and tallying how often null distribution statistics exceed the actual distribution statistic, we can determine the p-value. For more details, see Good (2005). In our study, we use 1,000 iterations to get an accurate p-value up to 0.001.

## 4. Data Description

Our data set comes from a field experiment on the Canadian website of one of the top five retailers in North America. The experiment was conducted over two weeks between August 8 and 22, 2013. The main data set records item views and purchases of 1,138,238 unique users across all the product categories sold on the website (which spans 82,290 unique SKUs). The data set has 2.8 million rows of individual-itemlevel data.

The field experiment was run by the retail company using a state-of-the-art $\mathrm { A } / \mathrm { B } / \mathrm { n }$ testing platform. This embeds snippets of code on the retailer’s website, much like Google Analytics, and controls all facets of $\mathbf { A } / \mathbf { B } / \mathbf { n }$ testing via a backend analytics dashboard. The A/B/n platform implements advanced cross-device customer identification strategies that combine IP addresses, cookies, log-in information, etc. with algorithms such as customer matching to assign a unique visitor ID to a customer.<sup>6</sup> The visitors’ behavior is then tracked over the course of the experiment. This enables the website to track individuals’ viewing logs and purchases over many days. Users (both old and new) are randomly chosen to be in the control or one of the treatment groups, and their treatment status is fixed during the course of the experiment. When the company ran the field experiment, it wanted to test the recommenders with a small fraction of its visitors to reduce potentia unwanted impact on the website. We first randomly assign the treatment labels (i.e., equally among VBCF or PBCF or control) at the user-level. Then, within the treatment labels, with $p = 0 . 3 3 ,$ , we actually show th users recommender panel. This gives overall treatment group probability of approximately 0.1 (0.33 × 0.33) for each treatment VBCF and PBCF. This design lets us carry out randomization checks with the untreated users within treatment labels as later discussed in Table 2. Therefore, we randomly allocated 10% of all visitors to each collaborative filtering treatment group. Upon clicking and viewing a particular item, the visitors are shown the appropriate recommender panel Figure 2 shows a collaborative filtering recommender based on views (“People who viewed this item also viewed”)—which we call VBCF. Similarly, there is also a purchase-based collaborative filter—which we cal PBCF. Users in the control group do not see this panel. At the end of the experiment, we have each consumer’s view logs and purchase logs at the item level. The algorithms were retrained every three days to propagate the influence of users’ purchase history multiple times over the period of the experiment. About half of the users in our data set were returning users; the other half were completely new. Finally, with the untreated users in each treatment labels, we also confirm that the user-level randomization holds via Kolmogorov Smirnov (KS) test on variables such as total number of item views, purchases, and wallet sizes. We report the p-values of KS test in Table 2.

After the experiment was completed, we were concerned that the product information (e.g., review stars and numbers) displayed in the recommender panels might have influenced user click behavior, and eventually the impact of recommenders.<sup>7</sup> Thus, we ran t-test on the average price, average review star rating, and average review number of all the viewed items in each treatment and control (user-number normalized) one against another and found that no comparisons were statistically significant.

Table 2. User-Level Randomization Check Using Kolmogorov-Smirnov Test

<table><tr><td>Description</td><td>PBCF vs. controlp-value</td><td>VBCF vs. controlp-value</td></tr><tr><td>Number of item views</td><td>0.89</td><td>0.45</td></tr><tr><td>Number of item purchases</td><td>0.66</td><td>0.87</td></tr><tr><td>Wallet size</td><td>0.37</td><td>0.86</td></tr></table>

Note. p-values reported.

Figure 2. (Color online) Recommender Example  
![](/api/attachments/5QCJZEAF/fulltext/images/cc68d67bbcbcd43a2ae323652b5ed194337ebcadbd2762d953b470d93918e99e.jpg)  
Notes. Example of a recommender shown to a consumer. This consumer was in the treatment group of collaborative filtering based on views

Figure 3 shows that most users in our data set visit the retail website only once during our data collection. While many of the users view only one item, there are also many users who view multiple items in the retailer’s catalog. Finally, the vast majority of buyers buy only one item during the two weeks of the experiment. There is also a reasonable tail of heavy users (15.1% of buyers buy four or more items in the two-week period). Table 3 presents summary statistics by treatment group. Together, they show that the recommenders help increase purchase activity by either driving an increase in the percentage of users who buy (Table 3, row 3) or the average number of purchases per buying user (Table 3, row 4) or both.

## 4.1. Cross-Category Data

The retailer maintains manually coded hierarchies of well-defined product categories and subcategories. There are in total four levels of categorization in which an individual SKU could be classified. The first level has 16 categories, the second has 153, the third has 963, and the fourth has 503 (not all products have a level-4 subcategory). Figure 4 shows all 16 categories at the highest level (on the left) and 100 randomly chosen subcategories at the second level (right). Table 4 shows the number of rows in our data set associated with the 16 top-level categories. Lastly, Figure 5 visualizes the number of unique users in each of the two treated groups who have either viewed or purchased products at the category level. Both groups show similar patterns. For example, many visitors view and purchase products in categories such as Electronics and Home and Pets, but very few do so in Jewelry and Watches. In both groups, visitors view products in Automotive, but they rarely purchase products in that category.

Given that the recommender systems in our field experiment were active within 16 main categories, we conduct our analysis of sales diversity by category. Within a category, we can generate Lorenz curves by measuring sales at the item level, level-2 subcategory or level-3 subcategory.<sup>8</sup> Throughout our main analysis, we measure sales and compute Gini coefficients at the level-3 subcategory. Our results are qualitatively similar at other levels of analyses.

## 4.2. Data Limitations

Even though our data are relatively clean, and causal effects are easier to extract compared with observational data, they have limitations—the most important being that we only implement two particular recommender system algorithms at one online retailer. We cannot fully control what the company is willing to implement, and so we could not implement all wellknown variants of recommender systems. To this end, we discuss how the results are generalizable. First, we used one of the most often implemented item-based collaborative filters, as described in a seminal paper by Sarwar et al. (2001). We used both of the commonly used variants—view- and purchase-based. Then, in im plementing the algorithm, we also utilized a leading open-source platform, Apache Mahout. Additionally, our implementation of the CF used default parameter settings (e.g., how many days of historical data to use, how often to retrain the algorithm) that the A/B testing firm used across all clients. Finally, in consulting a collaborating A/B testing analytics firm,<sup>10</sup> we learned that out of several hundred clients that implement recommenders, only two utilized content-based recommenders. All of this suggests that our findings have wide applicability across many e-commerce companies.

An additional limitation is that we do not have purchase data beyond the experiment’s two-week duration; it is possible, however, that recommendations could have driven purchases after the experiment. Specifically, users may have viewed recommendations but taken some time to finalize their purchase decisions. Given that we observe that recommendations drive an increase in purchases, it is possible that our estimate of that increase is conservative. On the other hand, it is also possible that the early response to recommendations might be initially enthusiastic but wil decline over time. In this case, our estimates may be too aggressive. Nevertheless, our focus here is on sales diversity not volume. Because our recommenders were trained on entire website 60 days prior to the experiments, the change in the recommended item list may be small even for an extended period of months. Thus, we do not expect later purchases to be systematically directed toward niche (or popular) products and we therefore believe that this limitation will not systematically bias our results in any one direction.

Figure 3. User Visit Frequency, Item No. View Frequency, Item No. Purchase Frequency  
![](/api/attachments/5QCJZEAF/fulltext/images/0a2c59d79468f525ab7468be97d9b96f40b3316611488554458c81f066081aed.jpg)

![](/api/attachments/5QCJZEAF/fulltext/images/d0c78342612af5848f4b011bd7923a257b6a46846d134a788664ff71087fa8fe.jpg)

![](/api/attachments/5QCJZEAF/fulltext/images/a6aea28b80166fa34543f4fedd3279df6eac85f39deb9a45de96098a46ba556d.jpg)

Table 3. Summary Statistics

<table><tr><td>Description</td><td>Total</td><td>Control</td><td>Treated PBCF</td><td>Treated VBCF</td></tr><tr><td>Unique users who have viewed at least one item</td><td>1,138,238</td><td>876,301</td><td>137,167</td><td>124,770</td></tr><tr><td>Unique users who have made purchases</td><td>16,774</td><td>12,851</td><td>2,019</td><td>1,904</td></tr><tr><td>Percentage of users who have made purchases</td><td>0.0147</td><td>0.0146</td><td>0.0147</td><td>0.0152</td></tr><tr><td>Number of purchases per buying user</td><td>2.460</td><td>2.444</td><td>2.560</td><td>2.461</td></tr><tr><td>Unique products viewed by users</td><td>82,290</td><td>76,820</td><td>45,611</td><td>44,899</td></tr><tr><td>Unique products purchased by users</td><td>12,976</td><td>10,910</td><td>2,825</td><td>2,646</td></tr><tr><td>Total number of item views</td><td>3,659,885</td><td>2,484,971</td><td>394,007</td><td>420,022</td></tr><tr><td>Total number of purchases</td><td>41,266</td><td>31,409</td><td>5,170</td><td>4,687</td></tr><tr><td>Total purchase/total users</td><td>0.0362</td><td>0.0358</td><td>0.0376</td><td>0.0375</td></tr></table>

Figure 4. Category Level 1 and Level 2 (100 Random)  
![](/api/attachments/5QCJZEAF/fulltext/images/faf1947728bed6849e794ab225627b1c1c439d7116697de3ba147e239c7abd26.jpg)  
Note. We show the names of category level 1 on the left and 100 randomly chosen subcategory level 2 sold by this retailer on the right.

## 5. Results

In this section, we first analyze the effect of recommenders on aggregate and individual diversity of a pooled data set. Next, we repeat our analysis by category for each of the major product categories on the retailer’s website. This is to test whether our results are qualitatively different based on the product category under consideration. Then, we conduct additional analysis to identify likely mechanisms that explain the changes in diversity that we observe. We conduct our analysis at both the item (SKU) level as well as the level-3 subcategory (not all items have a level-4 subcategory). In this section, we present our results at the subcategory level because it gives us more conservative estimates than the item level analyses. Online Appendix B shows the results at the item level, and our main findings are robust.

## 5.1. Pooled Aggregate and Individual Diversity Results

Figure 6 plots the Lorenz curve for aggregate sales at the firm. The unit of analysis is subcategory level 3 of the firm’s product catalog. For each subcategory, we calculate the total views and sales associated with it The Lorenz curve is then obtained based on these totals. The plots suggest a decrease in diversity of purchases for CF treatments relative to the control.

In Figure 7, we compute the Gini coefficients and test this more systematically for product views as well as purchases and at the aggregate and individual levels.<sup>11</sup> In the top panel, we plot the Gini coefficients for the control group and the two treatments groups. The graph on the left computes the Gini of views, and the one on the right plots the Gini of purchases. Control group statistics are average of 1,000 random samplings to normalize for the number of user differences. Each treated bar is also marked with the p-value stars if the difference from the control group is statistically significant. For both views and purchases, the control groups Gini coefficients are lower than that of either VBCF or PBCF. The differences between the control group and the treated groups are significant at p < 0.001. Both

Table 4. Product Categories Occurring in the Data Set (Level 1)

<table><tr><td>Apparel49,082</td><td>Appliances160,655</td><td>Automotive61,324</td><td>Baby154,772</td></tr><tr><td>Electronics239,966</td><td>Grocery52,424</td><td>Health and beauty153,812</td><td>Holiday gift center41,276</td></tr><tr><td>Home and pets301,066</td><td>Jewelry and watches22,897</td><td>Movies, music, and books146,165</td><td>Office and stationery83,516</td></tr><tr><td>Outdoor living49,871</td><td>Sports and recreation154,096</td><td>Toys132,181</td><td>Video games62,416</td></tr></table>

Note. The numbers represent rows in data.

Figure 5. Number of Users Who Viewed or Purchased Products in Each Category Unique Users Who Viewed Products Across Categories  
![](/api/attachments/5QCJZEAF/fulltext/images/21c9489b82c212c51d81b14472f5ccd340584e16b99434a19bbf0237e0e03306.jpg)

![](/api/attachments/5QCJZEAF/fulltext/images/c9acfafd20a4b44f6c2250da9fe31bc3a6f35fd08e5ef047d559cd636cf14ea0.jpg)

types of collaborative filtering are causing consumers to view and purchase less variety of products in aggregate. Finally, the PBCF’s Gini coefficients were higher than those of the VBCF for both the views and purchases, suggesting that the concentration effect was stronger for PBCF. The bottom two graphs of the figure plot average view and purchase diversity at the individual level. Interestingly, we do not observe a concentration bias of the CFs at the individual level. In fact, directionally, the treated groups’ Gini coefficients are lower than the control even though the differences were not statistically significant. Thus, it appears that while aggregate sales and view diversity decrease under CFs, individuals may or may not be exploring less.

Economic Impact of Gini Coef<sup>fi</sup>cient Changes. While the Gini coefficient is the choice of measurement in the long tail and recommender systems literature, it is hard to grasp the economic significance of small changes in the Gini coefficient. In this subsection, we provide some additional information to help readers assess the implications of the reported Gini coefficient changes. Take

Figure 6. (Color online) Lorenz Curves for Subcategory Level 3 Purchased  
![](/api/attachments/5QCJZEAF/fulltext/images/bb71816b28ffefc351712f24b58acf47e43bef1ebbff97e37b2f15af267eca9f.jpg)

![](/api/attachments/5QCJZEAF/fulltext/images/37178a9cce2d9bb6c62f1cca557f74a0ddfa934a68b7cc0f7e8d9c74355a641b.jpg)  
Note. These Lorenz curves show that firm-level aggregate sales diversity is lower for both collaborative filtering algorithms relative to the control.

PBCF’s impact, for example, Figure 7 shows that aggregate purchase Gini increased by 0.054 0.825829 0.771437 and individual average purchase decreased by 0.00004 0.998405 0.998365 . Are these changes economically significant? A recent study by Tan et al. (2017) puts raw Gini coefficient changes into perspective. The paper studies the impact of expanded product variety on demand concentration using the movie rental industry spanning around 20,000 unique SKUs, which is comparable to the number of SKUs we have at 82,290. With regard to how aggregate Gini coefficient changes influence market share, they report the following:

We find that increasing product variety by 1,000 titles may increase the Gini coefficient of DVD rentals by 0.0029, which translates to increasing the market share of the top 1% of DVDs by 1.96% and the market share of the top 10% of DVDs by 0.58%. At the same time, the market share of the bottom 1% of DVDs is reduced by 21.29%, while the market share of the bottom 10% of DVDs is reduced by 5.28%.

This suggests that, at the aggregate level, even a small Gini coefficient increase of 0.0029 results in considerable changes in market share for top products (including even double digit percentage change in the market share for bottom 1% products). Our aggregate Gini change is 0.054, which is 18.6 × 0.054/0.0029 that of the change assessed by Tan et al. (2017). Thus, the changes in aggregate sales concentration reported in our study are economically significant.

To understand the Gini coefficient changes at the individual level (0.00004), we present a simple simulation study. The average individual purchase Gini coefficient for control users is 0.998405 in our data If, for example, all purchasing users (on average purchased 1.74 unique items) end up purchasing one more unique item than they have purchased, this would decrease the average individual purchase Gini coefficient by 0.0000672. Our Gini coefficient shift (0.00004) corresponds to approximately 60% of this hypothetical situation. Put another way, the Gini coefficient shift of 0.00004 corresponds to the results if everyone were to purchase 34% (0.6/1.74 0.34) more number of unique items than they had purchased on average.

In summary, the changes in sales diversity due to the recommender system are economically significant. We next turn to analyze these results by product category to determine whether heterogeneity in effects across a diverse set of product categories might explain the findings.

## 5.2. Diversity By Product Category

Our partner firm has 16 high-level categories as listed in Section 4.1. We now conduct our analysis separately for each of these 16 categories. This allows us to investigate heterogeneity in results across product categories. Furthermore, because recommended products are usually from the same level-1 category as a focal product, there is additional merit in analyzing the results by category. For space and clarity, we present our results in graphic formats here. Please see Online Appendix A for the result table.

AGGREGATE Gini Coefficient for VIEWS

Figure 7. Aggregate and Individual Gini Coefficient Differences Under Different Treatments  
![](/api/attachments/5QCJZEAF/fulltext/images/c31abe51d10caad3a42c9ff44cf7684f6b830522b5b6344ad1b688178def911a.jpg)

AGGREGATE Gini Coefficient for PURCHASES  
![](/api/attachments/5QCJZEAF/fulltext/images/c50e1b7fca5174a1bd97d43647911cbabe0633ee3807a4615b47019e003eedbe.jpg)

![](/api/attachments/5QCJZEAF/fulltext/images/327302594ed89691b1f882cf9dbe62921438229d43cab8a614cd3d368e823b34.jpg)

![](/api/attachments/5QCJZEAF/fulltext/images/c8fda531dd4c1ff694e9b1f3bc524c566415d19aaef2b796121ba0fe2fa0d1e4.jpg)

<table><tr><td></td><td>Control</td><td>VBCF</td><td>PBCF</td></tr><tr><td>Aggregate View</td><td>0.720997</td><td>0.747055***</td><td>0.760807***</td></tr><tr><td>Aggregate Purchase</td><td>0.771437</td><td>0.799075***</td><td>0.825829***</td></tr><tr><td>Individual Avg View</td><td>0.997803</td><td>0.997755●</td><td>0.997781</td></tr><tr><td>Individual Avg Purchase</td><td>0.998405</td><td>0.998378</td><td>0.998365*</td></tr></table>

Note. Tables show actual values and significance.  
<sup>•</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Figure 8 presents the results by category. The first three graphs show the change in aggregate view diversity for (1) control–view-based collaborative filtering (VBCF), (2) control–purchase-based collaborative filtering (PBCF), (3) VBCF-PBCF. The next three graphs show the results for change in aggregate purchase

(a)

Figure 8. Aggregate Diversity Results Across Cross Categorie  
![](/api/attachments/5QCJZEAF/fulltext/images/4730759550a3a68afbf5e673f9f2edc30add5b10e09e14f3e62682ad268f8daf.jpg)  
(c)

Category-Level Aggregated View Gini Difference: Treated(View-Based CF)-Treated(Purchase-Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/3dc44891a9751731ae6b04aded76e83e8506919c987dfb294403bac569ef5adb.jpg)  
(e)

Category-Level Aggregated Purchase Gini Difference: Control-Treated(Purchase-Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/5ca3c59cc64fe2520b119836db58509fd91c1c849a0808994074d0b29a63f87c.jpg)  
<sup>•</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

diversity in the same order. The y-axis is the Gini difference. Each test statistic bar is denoted by the p-value stars associated with the value.

In both view diversity graphs at the top of Figure 8, the control-treated Gini differences are negative if they are statistically significant. This shows that both recommenders have a concentration bias and that consumers, as a whole, are viewing and exploring fewer subcategories under the recommenders. We also repeated the analysis at the item level (these are presented in Online Appendix B). The results are even more pronounced at the item level, with Gini differences being negative and statistically significant for every category. Figure 8(c) compares the two different treatment groups (VBCF <sup>−</sup> PBCF). While the differences are usually negative, all the categories are not statistically significant at the $p < 0 . 0 5$ level.

(b)  
![](/api/attachments/5QCJZEAF/fulltext/images/e2605df12221d5b80fdc0dfe47aec7029c1ec1f267d122160e0b0750c81e1247.jpg)

Category-Level Aggregated Purchase Gini Difference: Control-Treated(View-Based CF  
![](/api/attachments/5QCJZEAF/fulltext/images/148b93724731bfffdbf27cf380c6ea58acec51be7686e409158b835dfc790a2d.jpg)  
(f)

Category-Level Aggregate Purchase Gini Difference: Treated (View-Based ČF) - Treated (Purchase-Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/3f3240cc6a1282dae958782f4380f05a2fb7bc0a9147556393722e07072a0c69.jpg)

The same pattern emerges for changes in aggregate purchase diversity in Figure 8(d)–(f). When significant, the test statistics are always negative for the controltreated (for both VBCF and PBCF), which suggests that consumers are buying less variety of subcategories within all categories under the influence of recommenders. Once again, the analysis in Online Appendix B shows that the results are more pronounced at the item level and uniformly negative and statistically significant for all categories. In summary, the use of recommenders is once again associated with a decrease in the aggregate view and purchase diversity across multiple product categories.

Finally, one could ask whether the concentration bias is more pronounced in certain product categories. The magnitude of the concentration bias is, indeed, different across categories. Thus, in order to investigate whether certain category level attributes influence the concentration bias, we ran a simple linear regression with Gini coefficient differences as the y-variable and category level characteristics as the x-variables. For the x-variables, we have included the following category specific variables: (1) the number of unique SKUs in each category, (2) the number of unique category level 2 and level 3, (3) average price, (4) price variance, (5) average review number, and (6) average review ratings. However, this regression did not produce any statistically significant results. We think this is because with 16 categories at one firm, we do not have enough cross-sectional variation to explain whether the magnitude of the impact is systematically explained by category-specific attributes. With larger-scale crossfirm analysis, future studies may be able to identify category-level attributes that may influence concentration bias.

We next repeat the analyses at the individual level. This is done as in the previous section except that the analysis is done separately for each of the 16 product categories. Figure 9 presents the results. While aggregate results show a clear concentration bias, there is not compelling evidence of it at the individual level. Results are often not statistically significant, and, when they are, they lack directional consistency. The lack of statistical significance could be due to the fact that many users in our data set only purchase one product, leading to a dearth of in-depth individual level data, unlike in aggregate cases where the impact was more pronounced and easier to measure. A simple solution would have been to run the experiment for a longer period of time, but this was not feasible because of practical constraints at the collaborating company.

In summary, separately analyzing each of the main categories shows the same set of results that we found in our firm-level analysis. At the aggregate level, there is strong evidence of concentration bias. At the individual level, it is not clear whether user views or purchases are becoming less diverse. In the next two sections, we investigate product networks and analyze the impact on absolute sales of niche items in order to explain the differences at the aggregate and individual levels.

## 5.3. The Source of Diversity Shift: Copurchase Network Analyses

In this section, we visualize our results and explore how recommenders cause the shift in aggregate diversity. We use movies, one of the most studied product types, to illustrate and visualize our findings. Movies are a level-2 subcategory in our retailer’s catalog (within “Movies, Music & Books”). The main reason we choose movies is that its level-3 subcategory is genre, which is easy to understand and interpret. Later in the section, we demonstrate that these observations are not unique to movies.

In total, there were 71,122 users who viewed 15,064 unique movie-related items (total 151,709 views) and 993 users who actually ended up buying 1,478 (total 1,933) unique movie-related products, which include DVDs and Blu-Ray discs. Our analysis of view and sales diversity for movies showed that aggregate diversity decreased under recommenders, whereas individual diversity increased (both results were statistically significant). These results are omitted because of space constraints.

We construct copurchase networks for the contro group and the PBCF normalized by sample size (graphs and tables for VBCF are omitted because of space constraints, but the observations are qualitatively similar, albeit sometimes less pronounced in magnitude). Each node in the graph represents a level-3 subcategory (movie genre), and the size of the node is proportional to the percent of overall sales that went to the genre. An edge between two nodes indicates that there was a user who purchased from these genres, and the thickness of the edge is proportional to the number of such users who exist. Thus, the relative sizes of the nodes convey the extent to which sales were (un)evenly distributed at the aggregate level, and the edges convey the extent to which individuals explored content in diverse genres. Figure 10 compares the network graphs for PBCF and control group side by side.

When visually comparing the two graphs, we note the following:

1. The relative size of the nodes shows that the majority of purchases by the control group is distributed across a few genres: action, drama, and comedy. In the purchase-based CF, however, comedy is much bigger than the rest, indicating that purchases were more concentrated in comedy. This might be because comedy titles were recommended more often by the algorithms or because consumers are more willing to explore and trust the recommender for comedy.

2. The purchase-based CF graph is more wellconnected (i.e., denser) than the control group. This indicates that there are more users who are buying across genres in the purchase-based CF group, or, more specifically, there is greater individual cross-buying behavior. The connectedness of the purchase-based CF

$$
^ {\bullet} p <   0. 1; ^ {*} p <   0. 0 5; ^ {* *} p <   0. 0 1; ^ {* * *} p <   0. 0 0 1.
$$

Figure 9. Individual Average Diversity Results Across Cross Categories  
(a)  
![](/api/attachments/5QCJZEAF/fulltext/images/5d3715ee693fd243e07f3de236e97a007adb0078bf0db13b694047a79e270e2d.jpg)  
(c)

Category−Level Individual View Gini Difference: Treated(View−Based CF)−Treated(Purchase−Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/42845541a3b05e3589c0893599d9edc33970c613d3e00d6382e1cec5070a55d3.jpg)  
(e)

![](/api/attachments/5QCJZEAF/fulltext/images/d40fd7e4cbc4eb03f039cdf4551c75eba4d1c63e8f5d43cd3ffde70ab8b03745.jpg)

graph reflects the increase in individual diversity that we noted previously. Individual users may be exploring more genres, whereas sales may be simultaneously concentrated in a few genres at the aggregate level.

In summary, the purchase-based collaborative filtering algorithm shifts users to buy a few top genres at the aggregate level while increasing individual diversity through a cross-buying behavior that is aided by a few “pathway” genres. To formally test these differences, we use a permutation test to evaluate the market share of the top genres in each graph (market share of top N nodes). Table 5 shows the difference between the market share statistics for the CFs and control group, as well as the corresponding p-values obtained via permutation tests. We replicated the analysis for the top {1, 5, 10} genres. We see a clear shift to the top genres with the CFs. Under the purchase-based CF, the top genre—comedy—took 11% more of the market share compared with the top genre in the control group, action. VBCF demonstrates a similar pattern.

(b)  
![](/api/attachments/5QCJZEAF/fulltext/images/4c0f9d39356cc03d1d0e5cd8fa4d4d64f619f8762b28797ea33ae6cbaf3a6e0d.jpg)  
(d)

Category−Level Individual Purchase Gini Difference: Control−Treated(View−Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/3d131b336267c85903f8ce7544a59744dd2652def5c4e13e75afaa6303df9734.jpg)  
(f)

Category−Level Individual Purchase Gini Difference: Treated(View−Based CF)−Treated(Purchase−Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/dda136af3f7cb0a8dfa1768bee6e337fc3946aeb67d2cde5e0ee3ca92af82287.jpg)

To ensure that our observations with copurchase networks generalize beyond movies, we replicate the above analysis across all level-3 subcategories in the firm’s catalog. We again construct copurchase network in which each node in the graph represents a level-3 subcategory in the catalog (e.g., for the Electronics category, “Speakers” and “Desktop Computers” would be level-3 subcategories). The size of a node indicates its market share. An edge between two nodes again indicates that there were consumers who purchased from these two subcategories. We report two main measures associated with the networks. First, we compute the market share of the top N nodes in the network as we did above. In addition, we compute the average degree of top N nodes. The degree of a node is simply its number of edges. The average degree of top N nodes is obtained by taking the degrees of each of the nodes that are among the top N nodes and averaging them. The market shares indicate aggregate diversity and the average degrees indicate the extent to which users cross-purchased across subcategories.

Figure 10. (Color online) Copurchase Network Graphs of Genre Purchases Under Control and Purchase-Based Collaborative Filtering  
![](/api/attachments/5QCJZEAF/fulltext/images/b94b07f9a44f092c4a4dbf6b7ce8bed8b91d641a6e64b99ce16eee538c06c1d1.jpg)  
Edge Thickness: Number of consumers in commor Node Size: Purchase Volume Control

![](/api/attachments/5QCJZEAF/fulltext/images/0187a892ff8a4ef0e26232021982838972e2879bf6187adc39ec163923eb66c5.jpg)  
Edge Thickness: Number of consumers in commor Node Size: Purchase Volume  
Purchase-based Collaborative Filtering

Table 6 presents the results for market share shift in the treated group versus the control group. The table presents the market share of top {1, 5, first quartile, second quartile} subcategories for the control group, PBCF group, control-treated and p-value associated with the differences. For all rows, the recommender has increased the market share of the top nodes. The differences are statistically significant as well. This suggests that PBCF is increasing the concentration bias by increasing market share of the top subcategories. Table 7 presents the results for the average degree differences. The result suggests that PBCF is associated with a higher average degree for the top {1, 5, first quartile, second quartile} subcategories, meaning that even though users gravitate toward the top subcategories, they are also cross-purchasing across subcategories.

Table 5. Permutation Test Results for Copurchase Network Comparisons: Purchase-Based CF vs. Control

<table><tr><td rowspan="2"></td><td colspan="3">CF market share – control market share (p-value)</td></tr><tr><td>Top 1 genre</td><td>Top 5 genres</td><td>Top 10 genres</td></tr><tr><td>Purchase-based CF</td><td>0.11 (0.04)</td><td>0.10 (0.04)</td><td>0.08 (0.004)</td></tr></table>

Table 6. Market Share of Top N Subcategory Permutation Test Results

<table><tr><td>Top N</td><td>Control statistic</td><td>PBCF statistic</td><td>Control – treat</td><td>p-value</td></tr><tr><td>1</td><td>0.022</td><td>0.056</td><td>-0.034</td><td>0.024</td></tr><tr><td>5</td><td>0.100</td><td>0.145</td><td>-0.045</td><td>0.016</td></tr><tr><td>First quartile</td><td>0.815</td><td>0.840</td><td>-0.025</td><td>0.016</td></tr><tr><td>Second quartile</td><td>0.961</td><td>0.968</td><td>-0.006</td><td>0.134</td></tr></table>

Taken together, the results in this section imply that consumers are cross-purchasing more, but at the same time, their explorations are highly correlated because of the nature of the CF (recall that a CF uses data on other users’ views and purchases to recommend items). Owing to this highly correlated exploration among users, the market share for the top-selling products keeps increasing, creating a rich-get-richer concentration bias.

## 5.4. CFs’ Impact on Absolute Sales of Niche Item

Our analyses thus far reveal that CFs cause market share concentration; i.e., popular items obtain increased market share, whereas niche items lose market share. The market share and the Gini coefficient analyses ultimately reflect relative gains for popular versus niche items in the seller’s catalog. An important question is what happens at an absolute level. Table 8 suggests that recommenders increase total views and sales for the retailer. Specifically, the PBCF caused a 0.5% lift in views and a 5% lift in purchases and the VBCF showed an 11% lift in views and a 0.8% lift in purchases for our retailer (permutation tests reveal that these changes are statistically significant for PBCF purchase and VBCF views).<sup>12</sup> It is worth noting that VBCFs are more effective in increasing views, whereas PBCFs are more effective in increasing purchases, relatively speaking. Given this increase in total volume, the question is whether niche items lose out in absolute terms as well. If so, these items are strictly worse off because of the use of CFs. On the other hand, if absolute views and purchases of niche items increase and their market share goes down, it reveals a more nuanced view of the impact of CFs. This would suggest that whereas all kinds of products benefit from CFs, mainstream producers benefit more so than niche producers.

Figure 11 is a modified Lorenz curve that shows the absolute purchase count for all items (instead of the market share) with items rank ordered by sales volume. The charts are normalized by the number of users in the treated group to allow direct comparison of treated and control groups. The x-axis orders the level-3 subcategories from the least popular to the most popular The y-axis shows cumulative absolute purchase counts. For both charts, the treated dotted lines are clearly above the control in all support. This suggests that under the influence of CFs, all items, regardless of popularity, obtain increased absolute sales.

To formalize this finding, we ran t-tests comparing treated and control cumulative purchase counts for bottom {25th, 50th, all} percentile ranked products. The alternative hypothesis is “true difference in means is greater than zero.” Rejecting the null would mean that the treated group’s cumulative purchase count is statistically significantly greater than that for the control group. We show the results in Table 9. In all ranges, for both PBCF and VBCF, we reject the null hypothesis and the t-test results corroborate the intuition from the modified Lorenz curve in Figure 6.

Thus, although CFs show concentration bias in favor of popular items, they also manage to increase absolute sales for niche items. The increase in sales is more pronounced for the popular items, resulting in market share concentration bias. We obtain qualitatively similar results for view counts (as opposed to purchase counts) and for an analysis at the item level (as opposed to level-3 subcategory).

## 5.5. Robustness Checks

We ran several different robustness checks for the entire data to ensure that our results are not sensitive to certain choices we made for data analysis. They include the following:

R1. Our analysis thus far is based on treatment groups smaller than control group sizes. We replicated the analysis by randomly sampling a fixed number of users in each group, ex ante before the permutation test, so that each group has an equal number of consumers.

Table 7. Average Degree of Top N Subcategory Permutation Test Results

<table><tr><td>Top N</td><td>Control statistic</td><td>PBCF statistic</td><td>Control – treat</td><td>p-value</td></tr><tr><td>1</td><td>43</td><td>61</td><td>-18</td><td>&lt;0.001</td></tr><tr><td>5</td><td>36.2</td><td>51.8</td><td>-15.6</td><td>&lt;0.001</td></tr><tr><td>First quartile</td><td>10.27</td><td>13.90</td><td>-3.63</td><td>0.160</td></tr><tr><td>Second quartile</td><td>5.16</td><td>7.46</td><td>-2.3</td><td>&lt;0.001</td></tr></table>

Table 8. Sales Volume Effect of Recommenders Using Permutation Test

<table><tr><td></td><td>Control statistic</td><td>PBCF statistic (p-value of treat – control)</td><td>VBCF statistic (p-value of treat – control)</td><td>PBCF statistic increase from control</td><td>VBCF statistic increase from control</td></tr><tr><td>Average no. items viewed</td><td>10.32</td><td>10.38 (0.778)</td><td>11.50 (&lt;0.001)</td><td>0.5%</td><td>11%</td></tr><tr><td>Average no. items purchased</td><td>2.44</td><td>2.56 (0.034)</td><td>2.46 (0.210)</td><td>5%</td><td>0.8%</td></tr></table>

Notes. The statistics represent average number of items purchased or viewed over 1,000 iterations. The test was carried out with users who have made purchases. Results in bold are statistically significant.

R2. We removed consumers who are outliers in terms of number of views and purchased items. Specifically, we replicated the analysis excluding those users whose views or purchases exceeded three standard deviations from the mean.

R3. We replicated the analysis by using 1 or 0 (binary variable) for subcategories or items viewed (or purchased) instead of actual counts. This allows us to explore the notion of diversity from the perspective of number of unique subcategories or items viewed/purchased as opposed to proportion of sales.

R4. We replicated the analysis only for consumers who bought more than one item.

In all of these robustness checks, the findings are qualitatively similar to our main result. Summary results of the robustness checks are presented in Online Appendix C.

## 6. Discussion and Conclusions

Recommenders and personalization technologies are fast taking over nearly every aspect of consumer interaction on the web. Their use spans the purchase of physical products (books, DVDs, clothing, electronics, etc.), digital media (movies and news), and even online services such as dating and peer-to-peer lending. Despite their ubiquity, we still have much to learn about how different recommender algorithms influence markets and society.

Our study contributes to emerging literature on the impact of personalization technologies by studying the impact of recommender algorithms on sales diversity with an expansive data set from a field experiment run on the website of a top North American retailer. The data set spans 16 categories, 82,290 SKUs, and 1,138,238 users. Table 10 summarizes our results on the sales diversity impact of recommenders across a wide variety of different product categories based on one of the most popular implementation of CF algorithms, Apache Mahout. We have shown that collaborative filtering recommenders cause aggregate view and sales diversity to decrease, pushing consumers as a whole to explore and purchase less variety of products across all categories sold on this site. The result holds true whether diversity is analyzed at the item level or the subcategory level. It highlights a potential drawback of widely used collaborative filtering designs in terms of their ability to aid discovery of truly niche items. Interestingly, however, the individual average Gini coefficients were not significantly and consistently influenced by the recommender systems. We found that for some product categories, individual-level diversity may even increase. We investigated the source of diversity shift by analyzing copurchase networks and comparing relative versus absolute purchase volume. Copurchase analysis shows that individual users do explore new products and genres. However, their explorations are correlated, resulting in concentration at the aggregate level. Furthermore, we find that the absolute volume of views and purchases of niche items, in fact, increase. However, the increase in views and purchases is far greater for popular products, such that market share concentration increases. This suggests a nuanced view of the impact of recommenders. To the extent that scale helps—for example, by lowering per-unit costs or allowing producers to invest in better equipment—this shift helps niche producers. To the extent that market share helps—for example, by allowing producers to have greater consumer mindshare—this shift hurts niche producers.

Figure 11. Cumulative Absolute Purchase Counts Compared  
Cumulative Absolute Purchase Count Compared (Purchase Based CF  
![](/api/attachments/5QCJZEAF/fulltext/images/95bae2d2ee4fa66003101ef3d1a60e2b6c9f8d1b292d9d55fbfe8e48247c9f1f.jpg)

Cumulative Absolute Purchase Count Compared (View Based CF)  
![](/api/attachments/5QCJZEAF/fulltext/images/5dcb7e73544f685393adfdf93e52d06ecaa923e4a45d89b8aa46c2bc69e9b104.jpg)  
Note. The absolute cumulative purchase counts are normalized by dividing by each group’s unique number of users.

Table 9. The t-Test Results Comparing Treated Group Cumulative Purchase Count

<table><tr><td>Percentile</td><td>Test</td><td>t-statistic</td><td>p-value</td></tr><tr><td>0.25</td><td>PBCF vs. control</td><td>21.73560655</td><td>&lt; 0.001</td></tr><tr><td>0.5</td><td>PBCF vs. control</td><td>11.32599092</td><td>&lt; 0.001</td></tr><tr><td>1</td><td>PBCF vs. control</td><td>2.09396685</td><td>0.018</td></tr><tr><td>0.25</td><td>VBCF vs. control</td><td>20.74169952</td><td>&lt; 0.001</td></tr><tr><td>0.5</td><td>VBCF vs. control</td><td>14.04737241</td><td>&lt; 0.001</td></tr><tr><td>1</td><td>VBCF vs. control</td><td>1.69023882</td><td>0.045</td></tr></table>

Note. Purchase count is greater than that of control group for bottom {25th, 50th, all} percentile.

These results have significant managerial relevance. As the amount of consumer data available to firms grows exponentially, many retailers have aggressively adopted data mining and personalization technologies without a deep understanding of how different designs may contribute toward (or deter) broader strategic goals. For example, a firm interested in exposing consumers to a broader assortment of products may prefer a different design from another simply interested in maximizing sales. To the extent that a firm is interested in pushing its “back catalog,” it may seek to augment traditional collaborative filtering algorithms so that it is possible to identify relevant products with limited historical data (past views/purchases) and/or increase diversity, serendipity, or novelty of the recommended products using techniques from the extant literature (e.g., Oh et al. 2011, Adomavicius and Kwon 2014, Adamopoulos and Tuzhilin 2015). Jannach et al. (2015)

presents in-depth analyses of existing recommender methods that seek to balance accuracy and concentration bias, whereas Jannach and Adomavicius (2016) give an overview of connecting recommender systems with specific business goals. Furthermore, our study quantifies the magnitude of a recommender’s influence on sales dispersion, which, combined with the Gallino et al. (2017) study on the implications of sales dispersion/concentration on inventory management policies, provides an actionable plan for retailers to plan inventory policies in concert with recommender implementations on their e-commerce sites.

For producers of niche products, it is important to recognize that copurchase networks can be an important driver of consumer purchase decisions. As a result, producers might benefit from marketing strategies that seek to strategically place one’s product in the copurchase network of other relevant products. For ex ample, a publisher might initially discount its book (or target its advertising) for readers of another closely related, but popular, title. This can help ensure that the product enters the copurchase network of the popular title. This is particularly relevant for producers of niche products. One of the main promises of the internet is its ability to support niche product markets. The internet has reduced entry costs for producers in several markets such as books (Brynjolfsson and Smith 2000), music (Graham et al. 2005), and movies (Zhu 2001) and also made it feasible for retailers to carry niche products because of lower stocking costs (Brynjolfsson et al. 2006). On the demand side, search engines and recommenders lower consumer search costs. However, that alone might not be sufficient. Producers might need to exert additional marketing efforts to enable product discovery by relevant customer segments.

We conclude by discussing some limitations of our study and opportunities for future work. First, our study focused on the two most commonly used collaborative filtering designs. It appears from our study that purchase-based collaborative filters have a greater impact than CFs based on views. This may be because (1) the algorithm based on purchases might simply be better at delivering the best-fit products, (2) consumers might be more influenced by the “purchased also

## Table 10. Result Summary

## Results

purchased” signal than the “view also viewed” signal, or (3) both. On a related issue, the observed decrease in aggregate diversity may either be due to a reduced diversity of recommendations offered by the CF or due to the manner in which consumers selectively respond to recommendations. Because we do not have data on the actual recommendations made by the CF and are unable to recreate the recommendation list from our data set, we were unable to determine how much of the observed changes are attributable to different factors of CFs or the diversity of recommendations versus selective consumer response. Future work based on the actual products that were recommended and the consumer response to each individual recommendation would be a worthwhile extension of our work. Second, it is worth investigating the impact of other recommender designs, such as content-based and social network–based recommenders. Third, a valuable continuation on our work will be the studies that develop behavioral theories on how and why people react differently to different recommender systems and signals. Lab studies can be highly useful in this regard. Finally, we found that the magnitude of the changes in diversity is different for different product categories. The results of future work that documents whether there are systematic patterns in terms of how the diversities are changed may depend on the product category in consideration.

## Acknowledgments

The authors thank Adit Bharat Sanghvi for research assistance. All errors are the authors’ own.

## Endnotes

<sup>1</sup> https://econsultancy.com/reports/the-realities-of-online-personalisation -report/.

<sup>2</sup> For example, Jannach et al. (2015, p. 428) states, “Usually, no real system is available for researchers, for example, to conduct A/B tests in which the effects of different recommendation strategies or user interface variants can be explored.”

<sup>3</sup> Implemented with http://mahout.apache.org/.

A retailer wanting to implement content-based recommender has to (1) map out the characteristics of products, (2) find out product characteristics that are informative of customer’s preferences, and (3) content-code product characteristics for each SKU (Stock Keeping Unit). For a different category, the retailer has to start this process all from the scratch. This is why content-based recommenders are not favored among cross-category retailers.

<sup>5</sup> According to our data provider, 90% of their clients use Apache Mahout to implement their CF algorithms.

<sup>6</sup> The A/B/n company outsources unique user identification to a specialized firm that utilizes a variety of data, such as IP, useragent, log-in data, session ID, and device to minimize duplicate and multidevice problems. However, it is always possible that a user on one device switches to another device and is not pre cisely identified. At the same time, almost every study based on randomized testing would be subject to this limitation of imperfect identification.

<sup>7</sup> We thank the anonymous reviewer for pointing this out.

<sup>8</sup> Many items do not have a level-4 subcategory so we do not consider that possibility.

<sup>9</sup> The Gini coefficient changes are, in fact, more conservative at the subcategory level than at the item level, making the results more robust. The results are the same at the item level, with more statis tically significant group comparisons. We present item-level analysis in Online Appendix B.

<sup>10</sup> According to the North American Internet Retailer Top 500 Guide (https://www.digitalcommerce360.com/product/top-500), more com panies in the IR 500 relied on this particular A/B/n analytics company in implementing and testing personalization than any other provide on the market.

<sup>11</sup> For individual Gini measure, we standardize the length of the purchase or view vector to include all genres/items on the site for all users. This ensures that the measures are comparable across differen groups.

<sup>12</sup> Large effect sizes were observed for subcategories such as movies where PBCF cause a 25% lift in views and a 35% lift in the number of items purchased over the control group (no recommender). VBCF also showed a 3% lift in views and a 9% lift in the number of items purchased.

## References

Adamopoulos P, Tuzhilin A (2015) On unexpectedness in recommender systems: Or how to better expect the unexpected. ACM Trans. Intelligent Systems Tech. 5(4):1–:32.

Adomavicius G, Kwon Y (2014) Optimization-based approaches for maximizing aggregate recommendation diversity. INFORMS J. Comput. 26(2):351–369.

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6): 734–749.

Anderson C (2008) The Long Tail: Why The Future Of Business Is Selling Less Of More (Hyperion Books, New York).

Borle S, Boatwright P, Kadane JB, Nunes JC, Galit S (2005) The effect of product assortment changes on customer retention. Marketing Sci. 24(4):616–622.

Breese JS, Heckerman D, Kadie C (1998) Empirical analysis of predictive algorithms for collaborative filtering. Cooper GF, Moral S, eds. Proc. 14th Conf. Uncertainty Artificial Intelligence (Morgan Kaufmann Publishers, San Francisco), 43–52.

Brynjolfsson E, Smith MD (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Brynjolfsson E, Hu YJ, Smith MD (2006) From niches to riches: Anatomy of the long tail. MIT Sloan Management Rev. 47(4):67–71.

Brynjolfsson E, Hu YJ, Simester D (2011) Goodbye Pareto principle, hello long tail: The effect of search costs on the concentration of product sales. Management Sci. 57(8):1373–1386.

Celma O, Cano P (2008) From hits to niches? Or how popular artists<sup>\`</sup> can bias music recommendation and discovery. Proc. 2nd KDD Workshop Large-Scale Recommender Systems Netflix Prize Compe tition (ACM, New York), 1–8.

Cooke AD, Sujan H, Sujan M, Weitz BA (2002) Marketing the unfamiliar: The role of context and item-specific information in electronic agent recommendations. J. Marketing Res. 39(4): 488-497

De P, Hu Y, Rahman MS (2010), Technology usage and online sales: An empirical study. Management Sci. 56(11):1930–1945.

Dias MB, Locher D, Li M, El-Deredy W, Lisboa PJG (2008) The value of personalised recommender systems to e-business: A case study. Proc. 2008 ACM Conf. Recommender Systems (ACM, New York), 291–294.

Elberse A (2008) Should you invest in the long tail? Harvard Bus. Rev. 86(7/8):88.

Fisher ML (2003) What is the right supply chain for your product. Lewis MA, Slack N, eds. Operations Management: Critical Perspec tives on Business and Management, vol. 4 (Routledge, London), 73.

Fleder D, Hosanagar K (2009), Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55(5):697–712.

Gallino S, Moreno A, Stamatopoulos I (2017) Channel integration, sales dispersion, and inventory management. Management Sci. 63(9):2813–2831.

Good P (2005) Permutation, Parametric and Bootstrap Tests of Hypotheses (Springer, New York).

Graham G, Lewis GJ, Graham G, Hardaker G (2005) Evaluating the impact of the internet on barriers to entry in the music industry. Supply Chain Management 10(5):349–356.

Haubl G, Trifts V (2000) Consumer decision making in online¨ shopping environments: The effects of interactive decision aids. Marketing Sci. 19(1):4–21.

Hinz O, Eckert J (2010) The impact of search and recommendation systems on sales in electronic commerce. Bus. Inform. System Engrg. 2(2):67–77.

Hosanagar K, Fleder DM, Lee D, Buja A (2014) Will the global village fracture into tribes: Recommender systems and their effects on consumers. Management Sci. 60(4):805–823.

Jannach D, Adomavicius G (2016) Recommendations with a purpose. Proc. 10th ACM Conf. Recommender Systems (ACM, New York), 7–10.

Jannach D, Hegelich K (2009) A case study on the effectiveness of recommendations in the mobile internet. Proc. 3rd ACM Conf. Recommender Systems (ACM, New York), 205.

Jannach D, Lerche L, Gedikli F, Bonnin G (2013) What recommenders recommend – An analysis of accuracy, popularity, and sales diversity effects. Carberry S, Weibelzahl S, Micarelli A, Semeraro G, eds. User Modeling, Adaptation, and Personalization. UMAP 2013. Lecture Notes in Computer Science, vol. 7899 (Springer, Berlin), 25–37.

Jannach D, Lerche L, Kamehkhosh I, Jugovac M (2015) What recommenders recommend: An analysis of recommendation biases and possible countermeasures. User Model. User-Adapt. Interaction 25(5):427–491.

Jiang B, Jerath K, Srinivasan K (2011) Firm strategies in the mid tail of platform-based retailing. Marketing Sci. 30(5):757–775.

Jiang H, Qi X, Sun H (2014) Choice-based recommender systems: A unified approach to achieving relevancy and diversity. Oper. Res. 62(5):973–993.

Kok AG, Fisher ML, Vaidyanathan R (2008) Assortment planning: Review of literature and industry practice. Retail Supply Chain Management (Springer, New York), 99–153.

Lamere P, Green S (2008) Project Aura: Recommendation for the rest of us. Presentation, Sun JavaOne Conference. Accessed July 27, 2018, http://www.oracle.com/technetwork/systems/ts-5841-159144.pdf.

Lin Z, Goh KY, Heng CS (2017) The demand effects of product recommendation networks: An empirical analysis of network diversity and stability. Management Inform. Systems Quart. 41(2):397–426.

Mooney RJ, Roy L (2000) Content-based book recommending using learning for text categorization. Proc. 5th ACM Conf. on Digital Libraries (ACM, New York), 195–204.

Oestreicher-Singer G, Sundararajan A (2012) Recommendation networks and the long tail of electronic commerce. MIS Quart. 36(1):65–84

Oh J, Park S, Yu H, Song M, Park S-T (2011) Novel recommendation based on personal popularity tendency. Data Mining (ICDM), 2011 IEEE 11th Internat. Conf. (IEEE, New York), 507–516.

Pariser E (2011) The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think (Penguin Books, St. James Ward, UK).

Pathak B, Garfinkel R, Gopal RD, Venkatesan R, Yin F (2010) Em pirical analysis of the impact of recommender systems on sales. J. Management Inform. Systems 27(2):159–188

Resnick P, Varian HR (1997) Recommender systems. Comm. ACM 40(3):56–58.

Sarwar B, Karypis G, Konstan J, Riedl J (2001) Item-based collabo rative filtering recommendation algorithms. Proc. 10th Internat. Conf. World Wide Web (ACM, New York), 285–295.

Schafer JB, Konstan J, Riedl J (1999) Recommender systems in ecommerce. Proc. 1st ACM Conf. Electronic Commerce (ACM, New York), 158–166.

Senecal S, Nantel J (2004) The influence of online product recommen dations on consumers online choices. J. Retailing 80(2):159–169.

Tam KY, Ho SY (2005) Web personalization as a persuasion strategy: An elaboration likelihood model perspective. Inform. Systems Res. 16(3):271–291

Tan TF, Netessine S, Hitt L (2017) Is Tom Cruise threatened? An empirical study of the impact of product variety on demand concentration. Inform. Systems Res. 28(3):643–660.

Thompson C (2008) If you liked this, you’re sure to love that. New York Times (November 21), https://www.nytimes.com/2008 11/23/magazine/23Netflix-t.html.

Van Herpen E, Pieters R (2002) The variety of an assortment: An ex tension to the attribute-based approach. Marketing Sci. 21(3):331–341.

Walter FE, Battiston S, Yildirim M, Schweitzer F (2012) Moving recommender systems from on-line commerce to retail stores. Inform. Systems E-Bus. Management 10(3):367–393.

Wu L-L, Joung Y-J, Chiang T-E (2011) Recommendation systems and sales concentration: The moderating effects of consumers product awareness and acceptance to recommendations. 2011 44th Hawaii Internat. Conf. System Sci. (IEEE, New York), 1–10.

Zhou R, Khemmarat S, Gao L (2010) The impact of Youtube recommendation system on video views. Proc. 10th ACM SIGCOMM Conf. Internet Measurement (ACM, New York), 404–410.

Zhu K (2001) Internet-based distribution of digital videos: The economic impacts of digitization on the motion picture industry Electronic Markets 11(4):273–280.
