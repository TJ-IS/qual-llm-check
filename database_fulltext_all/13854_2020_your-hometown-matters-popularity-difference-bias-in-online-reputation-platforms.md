---
otero_id: 13854
otero_key: "V7RKT2T2"
title: "Your Hometown Matters: Popularity-Difference Bias in Online Reputation Platforms"
authors: "Marios Kokkodis; Theodoros Lappas"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0895"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.238.7.40] On: 11 May 2020, At: 18:44 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/V7RKT2T2/fulltext/images/8053806404c088cb073227e62b1817e43fa0087602c9aec392dc505546ae674d.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Your Hometown Matters: Popularity-Difference Bias in Online Reputation Platforms

Marios Kokkodis, Theodoros Lappas

To cite this article: Marios Kokkodis, Theodoros Lappas (2020) Your Hometown Matters: Popularity-Difference Bias in Online Reputation Platforms. Information Systems Research

Published online in Articles in Advance 08 May 2020

https://doi.org/10.1287/isre.2019.0895

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individua professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Your Hometown Matters: Popularity-Difference Bias in Online Reputation Platforms

Marios Kokkodis,<sup>a</sup> Theodoros Lappas<sup>b</sup>

<sup>a</sup> Carroll School of Management, Boston College, Chestnut Hill, Massachusetts 02467; <sup>b</sup> School of Business, Stevens Institute of Technology, Hoboken, New Jersey 07030

Contact: kokkodis@bc.edu, https://orcid.org/0000-0002-5037-6060 (MK); tlappas@stevens.edu, https://orcid.org/0000-0002-4669-4170 (TL)

Received: Revised: Augu Accepted: Published Online in Articles in Advance: May 8, 2020

https://doi.org/10.1287/isre.2019.089

Copyright:

Abstract. We study a new source of bias in online review platforms that originates from the popularity difference between the traveling reviewer’s hometown and destination (popularity-difference bias). In particular, we model popularity-difference bias as a function of two opposing forces: (1) the travelers’ evaluation of performance and (2) the travelers’ expectations. The net result of these two forces leads to two competing views regarding the nature of popularity-difference bias: the first view is performance-dominant, whereas the second one is expectation-dominant. Through analyzing a large set of res taurant reviews from a major online reputation platform, we find empirical evidence in support of the performance-dominant view. Specifically, we find that popularity difference bias affects both the assigned rating and the text-encoded sentiment of a review. When reviewers travel to a less popular location than their hometown, popularity difference bias is negative. To the contrary, when reviewers travel to a more popular location than their hometown, popularity-difference bias is positive. Popularity-difference bias affects the average rating of restaurants up to 11%. As a result, a restaurant’s ratings skew lower if the restaurant tends to attract guests from more popular locations, whereas they skew higher if the restaurant tends to attract guests from less popular locations. This effect on ratings alters the probability that an average customer will consider a restaurant by up to 16%. Finally, awareness of popularity-difference bias allows managers to improve the design of their ranking systems: we show that such improvements can lead to up to 12% higher reviewer satisfaction, and up to 24% more diversified top restaurant recommendations.

History: Saby Mitra, Senior Editor; Prasanna Tambe, Associate Editor. Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2019.0895.

Keywords: online reputation systems • online reviews • hometown bias • popularity-difference bia

## 1. Introduction

Online reputation platforms such as TripAdvisor and Yelp are a rich and ubiquitous source of information for potential customers (Chevalier and Mayzlin 2006, Zhu and Zhang 2010, Luca 2018). Consumers can visit such platforms, read reviews on competitive products and services, identify advantages and disadvantages, and ultimately, make an informed purchase decision. As a result, product reviews and ratings have a strong impact on consumer consideration (Duan et al. 2008a, Vermeulen and Seegers 2009) and sales (Forman et al. 2008) across a wide range of domains, including movies (Duan et al. 2008a), books (Chevalier and Mayzlin 2006), electronics (Ghose and Ipeirotis 2011, Cui et al. 2012), hotels (Ye et al. 2009), and local businesses (Zhang et al. 2010, Lu et al. 2013, Luca 2018).

The well-documented impact of online review platforms on product sales has motivated researchers to consider endogenous and exogenous characteristics that affect the review-authoring process, such as self selection (Li and Hitt 2008, Koh et al. 2010, Hu et al 2017), reviewer popularity (Goes et al. 2014), and social identity (Li et al. 2017, Wang et al. 2018). Recently, location-based characteristics and their effects on the review-authoring process have attracted interest from both academia (Huang et al. 2016, Neumann et al. 2017, Gao et al. 2018, Park et al. 2019) and industry (Soups 2015, Bialik 2017). Specifically, these works show that the spatial distance traveled by the reviewer has a positive effect on review ratings in the restaurant domain (Huang et al. 2016, Neumann et al. 2017) and an inverted U-shaped effect on the service ratings in the hotel domain (Park et al. 2019). But how do differences between locations affect the reviewauthoring process?

To investigate, we focus on the popularity difference between a reviewer’s hometown and visiting destination. A destination’s popularity is shaped by various characteristics, including attractions, indoor and outdoor activities, museums, and theater (Silberberg 1995, Bennett 2005, Suh and West 2010, Gonzalez-´ Rivera 2018). As a result, it affects the satisfaction surplus (or deficit) that travelers receive during a visit. Prior work (Teas 1993) suggests that a travelers satisfaction is captured by two components: (1) the travelers’ perceived performance of the reviewed venue and (2) the travelers’ venue expectations. We argue that popularity difference affects both of these components. In particular, a destination with a higher popularity than the reviewer’s hometown increases both the reviewer’s perceived performance of the venue and the reviewer’s expectations from the venue (positive popularity difference spills over to both performance and expectations). To the contrary, a destination with a lower popularity than the reviewer’s hometown decreases the reviewer’s perceived performance of the venue and the reviewer’s expectations from the venue (negative popularity difference spills over to performance and expectations). The net result of the two competing forces (spillovers to performance versus spillovers to expectations) leads to two competing hypotheses regarding the nature of popularity-difference bias: the first view is performance-dominant (spillovers to performance are larger than spillovers to expectations), whereas the second one is expectation-dominant (spillovers on expectations are larger than spillovers on performance).

We test the proposed theoretical framework by collecting and analyzing a set of 763,658 restaurant reviews from 1,484 cities in the continental United States. We operationalize a location’s popularity through the location’s total number of hotel reviews. To isolate the hypothesized effect, we control for a set of time-varying observed and static unobserved characteristics. Text analysis of the reviews shows additional evidence of popularity-difference spillovers to travelers’ satisfaction. Robustness checks and secondary analyses (subsampling analysis on restaurant chains and matched restaurants, propensity score matching, population segmentation and undersampling, alternative modeling choices, alternative measures of popularity difference) increase the confidence in the observed results.

The empirical analysis supports the performancedominant view and provides the following novel findings:

• Popularity-difference spillovers on reviewers’ performance evaluations are stronger than on reviewers expectations. As a result, the popularity difference between the traveling reviewer’s hometown and destination biases the review-authoring process.

• The direction of popularity-difference bias depends on whether the destination is less or more popular than the reviewer’s hometown. In the former scenario (i.e., traveling to a more popular location), popularity-difference bias is positive. In the latter scenario (i.e., traveling to a less popular location), popularity-difference bias is negative.

• Popularity-difference bias manifests in both the rating and the text-encoded sentiment of a traveler’s review.

Our work extends research on biases in online reviews by revealing, explaining, and measuring popularity-difference bias in online review platforms. It empirically shows that reviewer expectations and performance evaluations are shaped, in part, by the reviewers’ hometown. This existence of popularitydifference bias has an economic impact on the participating businesses. Restaurants that are prone to travelers from more popular locations experience a negative bias that decreases their average ratings by up to 11%. On the other hand, restaurants that are prone to travelers from less popular locations experience a positive bias that increases their average ratings by up to 4%. Popularity-difference bias affects 98% of the restaurants in our data set. Review-based rankings that reputation platforms use to organize and present competing businesses are also subject to popularity-difference bias, which alters the probability that a potential customer will consider a restaurant by up to 16%. A reduction (unbiased-tobiased) of 16% in consideration probability means that an affected restaurant never has the opportunity to convert 16 out of every 100 travelers that it would have access to in a bias-free setting. These findings guide design actions that platforms can take to either alleviate or exploit popularity-difference bias: through personalized rankings that leverage popularity difference, we show that platforms can increase reviewer satisfaction by up to 12% while diversifying their top-recommended restaurants by up to 22%.

## 2. Research Context and Hypotheses Development

Online reputation systems that rely on reviews and ratings resolve various information asymmetries in online marketplaces (Dellarocas 2003, 2006; Bolton et al. 2004; Bakos and Dellarocas 2011; Kokkodis and Ipeirotis 2013, 2016; Lappas 2012). As a result, these systems have a strong economic impact (Chevalier and Mayzlin 2006; Duan et al. 2008a, 2009; Forman et al. 2008; Archak et al. 2011; Gu et al. 2012; Kokkodis 2012; Sun 2012; Lu et al. 2013; Jabr and Zheng 2014; Kwark et al. 2014; Jiang and Guo 2015; Kokkodis and Lappas 2016). This well-documented effect of reviews and ratings on product sales has motivated a stream of research that studies the characteristics and drivers of the review-authoring process.

## 2.1. Biases in Online Review Platforms

Both endogenous and exogenous characteristics can bias the review-authoring process. Self-selection bias, which is often driven by disconfirmation (Ho et al. 2017), results in a J-shaped online rating distribution (Hu et al. 2017, Kokkodis 2019) and decreases consumer surplus (Li and Hitt 2008). Positive rating environments increase posting incidence, whereas negative rating environments discourage it (Moe and Schweidel 2012). Social identity (Li et al. 2017, Wang et al. 2018), social norm (Burtch et al. 2017), monetary incentives (Khern-am nuai et al. 2018), prior ratings (Moe and Trusov 2011, Lee et al. 2015), the reviewer and product popularity (Goes et al. 2014, Lee et al. 2015), market competition (Gutt et al. 2019), and demographics (Bakhshi et al. 2014) further introduce biases to the assigned ratings (Dai et al. 2018).

Location-based effects can also affect the reviewauthoring process (Huang et al. 2016, Neumann et al. 2017, Gao et al. 2018, Park et al. 2019). Travelers from countries with high societal inequality (high power distance) rate with a negative predisposition (Gao et al. 2018). Traveled geographical distance between the reviewer’s domicile and the location of the reviewed business has a positive effect on restaurant ratings (Huang et al. 2016, Neumann et al. 2017) and an inverted U-shaped effect on hotels service ratings (Park et al. 2019). This study extends this line of work by investigating how differences between the reviewer’s hometown and destination environments affect both the ratings and the sentiment expressed in the review text.

## 2.2. The Emergence of Popularity-Difference Bias

Compared with unpopular destinations that are not frequently visited by travelers, popular destinations (such as New York, Chicago, and Las Vegas) have an abundance of characteristics that can elevate a traveler’s experience (Silberberg 1995, Bennett 2005, Suh and West 2010, Gonzalez-Rivera´ 2018). Examples of such destination characteristics include attractions, indoor and outdoor activities, retail shops, museums, theater, hotels, and restaurants. The availability and quality of such characteristics shape the destination’s popularity, which is reflected by the number of visitors that the destination receives (Silberberg 1995, Grass 2017, Gonzalez-Rivera´ 2018).

Prior research suggests that a destination’s characteristics and popularity can create a satisfaction surplus (or deficit) that travelers will receive during a visit to the destination (Chon 1990, Echtner et al. 1991, Silberberg 1995, Pike 2002, Tasci et al. 2007, Chi and Qu 2008, Stepchenkova and Mills 2010, Ramseook-Munhurrun et al. 2015, Grass 2017, Gonzalez-Rivera´ 2018). This popularity effect on traveler satisfaction manifests as the difference of two fundamental components (Teas 1993): perceived performance and expectations. In particula $^ { \mathrm { ~ r ~ } , }$ for a traveler i who visits a venue $j ,$ satisfaction $S _ { i j }$ is:

$$
S _ {i j} = P _ {i j} - E _ {i j} + u _ {i j},\tag{1}
$$

where $P _ { i j }$ is the perceived performance of traveler i for venue $j , E _ { i j }$ are the expectations of traveler i for venue $j ,$ and $u _ { i j }$ captures both exogenous $( \mathrm { e . g . }$ , distance traveled, population, or income differences between hometown and visiting locations) and en dogenous (e.g., unobserved quality of the venue) characteristics that could affect satisfaction.

$P _ { i j }$ and $E _ { i j }$ in Equation (1) are traveler-specific, as not all travelers are created equal. In this work, we argue that one of the dimensions that affect both $P _ { i j }$ and $E _ { i j }$ is the difference in popularity between a traveler $^ \prime _ { \mathrm { { S } } }$ hometown and visiting location. Consider for instance a traveler planning to visit a destination that is significantly more popular than the traveler $' _ { \mathrm { { S } } }$ hometown. Due to the positive popularity difference between destination and hometown, travelers’ expectations will likely increase more than they would have if the popularity difference between the two locations were insignificant. Similarly, when the traveler actually visits the destination and experi ences the reasons that drive the difference in popularity (e.g., through more options, better services, amenities, attractions), then the traveler’s perceived performance of the destination’s services will increase according to the experienced difference between the two locations.<sup>1</sup>

Based on this discussion, we argue that $P _ { i j }$ and $E _ { i j }$ include components that represent both the venue (r) and the popularity difference (δ) between the traveler’s hometown and destination. The venue component captures the traveler’s perceived performance of the venue $( P _ { i j } ^ { r } )$ and prior venue expectations $( E _ { i j } ^ { r } )$ The popularity difference component accounts for potential spillover effects that popularity difference has on both the traveler’s perceived performance of the venue $( P _ { i j } ^ { \delta } )$ ) and the traveler’s expectations from the venue $( E _ { i j } ^ { \delta } )$ . By formalizing these components, Equation (1) becomes:

$$
S _ {i j} = P _ {i j} ^ {r} + P _ {i j} ^ {\delta} - \left(E _ {i j} ^ {r} + E _ {i j} ^ {\delta}\right) + u _ {i j}.\tag{2}
$$

As we discuss next, the design of the $P _ { i j } ^ { \delta }$ and $E _ { i j } ^ { \delta }$ constructs relies on the susceptibility of expectations and perceived performance to spillover effects.

2.2.1. Popularity-Difference Spillover Effects on Perfor mance Evaluation $( P _ { i j } ^ { \delta } )$ ). Subjective performance evaluations are sensitive to spillover effects from peripheral factors (Bol and Smith 2011). Prior performance information (Murphy et al. 1985. Huber et al. 1987

Kravitz and Balzer 1992), information from different sources (Blakely 1993, Murphy and Cleveland 1995, Bono and Colbert 2005) and other external dimensions (Bol and Smith 2011, Ramseook-Munhurrun et al. 2015) can bias performance evaluation in ways that cannot be controlled by the evaluated entity. In our context, the popularity difference between the traveler’s hometown and the visiting location is a peripheral uncontrollable factor that spills over to the traveler’s perceived performance of the venue (i.e., the traveler’s performance evaluation of the venue).

2.2.2. Popularity-Difference Spillover Effects on Expectations (<sup>Eδ</sup><sub>ij</sub> ). Similarly, the impact of spillover effects on traveler expectations has been documented in multiple domains, including (1) national brand identity, where a nation’s reputation shapes traveler expectations (Agarwal and Sikri 1996, Fan 2006, Roshan et al. 2017), (2) e-commerce platforms, where the platform’s trust extents to the platform’s sellers (Verhagen et al. 2006, Chen et al. 2015), and (3) brand extension, where consumers shape positive expectations on new products because of the products’ brands (Bhat and Reddy 2001, Shen 2014). In our context, these studies suggest that popularity difference will spill over to travelers’ expectations of the visited venue.

It is important to highlight that popularity difference spillovers to performance evaluations and expectations are not directly relevant to the restaurant’s quality (Litvin et al. 2008, Kim and Stepchenkova 2015, Abubakar and Ilkan 2016). For instance, due to popularity difference spillovers, a traveler that arrives in a significantly more popular touristic city is likely to have increased expectations from the city’s restaurants (Phelps 1986, Gronroos¨ 1990, Font 1997, Bigne et al. 2001, Litvin et al. 2008, Wang et al. 2009,

Wang and Pizam 2011, Prayag and Ryan 2012, Kim and Stepchenkova 2015, Abubakar and Ilkan 2016). If these high expectations are not met during dining, the traveler will be disappointed. Similarly, compared with the traveler’s hometown offerings, the many higher-quality offerings of a popular city (Silberberg 1995, Bennett 2005, Suh and West 2010, Gonzalez-´ Rivera 2018) will have a positive spillover effect on the way a visitor perceives the performance of a local restaurant, independent of the restaurant’s actual quality (Pike 2002, Tasci et al. 2007, Chi and Qu 2008, Stepchenkova and Mills 2010, Ramseook-Munhurrun et al. 2015).

As a result, and based on this discussion, we expect (i) positive (or zero) spillover effects on both expectations and performance when travelers visit more popular destinations than their hometowns, and (ii) negative (or zero) spillover effects when travelers visit less popular destinations than their hometowns.

According to Equation (2), performance spillovers $( P _ { i j } ^ { \delta } )$ and expectation spillovers $( E _ { i j } ^ { \delta } )$ are at odds (performance-expectation tension): higher perceived performance has a positive effect on satisfaction, whereas higher expectations have a negative effect. As a result, the net popularity-difference bias (b<sup>δ</sup>) in a traveler’s satisfaction is as follows:

$$
\text { Popularity - difference   bias } := b ^ {\delta} = P _ {i j} ^ {\delta} - E _ {i j} ^ {\delta}.\tag{3}
$$

Figure 1 schematically describes the discussed hypothesized mechanism that shapes popularity-difference bias.

Equation (3) assumes that the size of the bias is the same regardless of whether the traveler visits a location with a higher (δ > 0) or a lower popularity (δ < 0) compared with the traveler’s hometown. To allow for direction-specific magnitudes for both the popularity-difference performance $( P _ { i j } ^ { \delta } )$ and expectation $( \check { E _ { i j } ^ { \delta } } )$ spillovers, we rewrite Equation (3) as follows:

Figure 1. (Color online) The Generation Process of Popularity-Difference Bias  
![](/api/attachments/V7RKT2T2/fulltext/images/6e23c8455a18b953abea8d75082d266e06eb99432207a1bfd2d233dd091bd745.jpg)  
Notes. The figure summarizes how the popularity difference between a traveler ’s hometown and destination spills over to performance evaluations and expectations, thus shaping popularity-difference bias.

$$
P _ {i j} ^ {\delta} = \Big (P _ {i j} ^ {\delta > 0} \mathbb {1} _ {\delta > 0} + P _ {i j} ^ {\delta <   0} \mathbb {1} _ {\delta <   0} \Big) f (\delta),\tag{4}
$$

$$
E _ {i j} ^ {\delta} = \Big (E _ {i j} ^ {\delta > 0} \mathbb {1} _ {\delta > 0} + E _ {i j} ^ {\delta <   0} \mathbb {1} _ {\delta <   0} \Big) f (\delta),\tag{5}
$$

where $\mathbb { 1 } _ { c o n d }$ is an indicator function that is true only when the condition cond is true, and $f ( \delta )$ is a normalizing function that regulates the effect of the differences (δ) and is sign-preserving. As a result, the function $f ( \delta )$ determines the positive or negative $d i -$ rection of the effect, whereas $\dot { E } _ { i j } ^ { \delta < 0 } , E _ { i j } ^ { \delta > 0 } , P _ { i j } ^ { \delta < 0 } .$ , and $P _ { i j } ^ { \delta < \mathrm { C } }$ encode the size of their respective effects and are thus greater or equal to zero. Combining Equations (4) and (5), Equation (3) becomes:

$$
b ^ {\delta} = f (\delta) \times \Big [ \mathbb {1} _ {\delta > 0} \left(P _ {i j} ^ {\delta > 0} - E _ {i j} ^ {\delta > 0}\right) + \mathbb {1} _ {\delta <   0} \left(P _ {i j} ^ {\delta <   0} - E _ {i j} ^ {\delta <   0}\right) \Big ].\tag{6}
$$

Based on Equation (6), in order for popularity-difference bias to actually affect a traveler’s satisfaction, one of the two components (i.e., performance spillover or expectation spillover) has to be significantly larger than the other. This generates two types of competing hypotheses: performance-dominant and expectation-dominant.

For the performance-dominant view, we hypothesize the following:

Hypothesis 1a (Performance-Dominant with $\delta > 0 )$ . If the popularity of the traveler’s destination is higher than that of the traveler’s hometown $( \delta > 0 )$ , then the popularitydifference spillovers to perceived performance will exceed the popularity-difference spillovers to expectations $( P _ { i j } ^ { \delta > 0 } >$ $E _ { i j } ^ { \delta > 0 } )$ . As a result, popularity-difference bias will be positive (Equation (6), $b ^ { \delta } > 0 )$

Hypothesis 1b (Performance-Dominant with $\delta < 0 )$ . If the popularity of the traveler’s destination is lower than that of the traveler’s hometown $( \delta < 0 )$ , then the popularitydifference spillovers to perceived performance will exceed the popularity-difference spillovers to expectations $( P _ { i j } ^ { \delta < 0 } >$ $E _ { i j } ^ { \delta < 0 } )$ . As a result, popularity-difference bias will be negative (Equation (6), $b ^ { \delta } < 0 )$

Similarly, for the competing expectation-dominant view, we hypothesize the following:

Hypothesis 2a (Expectation-Dominant with $\delta > 0 )$ . If the popularity of the traveler’s destination is higher than that of the traveler’s hometown $( \delta > 0 )$ , then the popularitydifference spillovers to expectations will exceed the popularity-difference spillovers to perceived performance $( \dot { P } _ { i j } ^ { \delta > 0 } < \dot { E } _ { i j } ^ { \delta > 0 } )$ . As a result, popularity-difference bias will be negative (Equation (6), $b ^ { \delta } < 0 )$ 1

Hypothesis 2b (Expectation-Dominant with $\delta < 0 )$ . If the popularity of the traveler’s destination is lower than that of the traveler’s hometown $( \delta < 0 )$ , then the popularitydifference spillovers to expectations will exceed the popularitydifference spillovers to perceived performance $( P _ { i j } ^ { \delta \dot { < } 0 } < E _ { i j } ^ { \delta < \tilde { 0 } } )$ As a result, popularity-difference bias will be positive (Equation (6), $b ^ { \dot { \delta } } > 0 )$

Next, we discuss the empirical setting that facilitates the investigation of the performance-expectation tension (Figure 1).

## 3. Research Setting

We collect and analyze a unique set of reviews from one of the largest travel reputation platforms, RepPlatform (pseudonym). RepPlatform is a major online review-hosting platform that receives hundreds of millions of monthly travelers and hosts more than half a billion online reviews. For our analysis, we devise a data set of 763,658 reviews posted by 31,812 reviewers on 50,194 restaurants. All the reviewers and restaurants are located in 1,484 cities and towns of the continental United States. The reviews were posted in a span of 14 years, between 2004 and 2018. Table 1 presents the diversity of the data set in terms of reviewers, restaurants, and locations.

The discussion in Section 2.2 structures the following empirical specification for capturing a reviewer’s satisfaction:

Reviewer satisfaction<sub>ij</sub>

$$
\begin{array}{l} = f (\delta) \times \left[ \mathbb {1} _ {\delta > 0} \overbrace {\left(P _ {i j} ^ {\delta > 0} - E _ {i j} ^ {\delta > 0}\right)} ^ {\alpha^ {\delta > 0}} + \mathbb {1} _ {\delta <   0} \overbrace {\left(P _ {i j} ^ {\delta <   0} - E _ {i j} ^ {\delta <   0}\right)} ^ {\alpha^ {\delta <   0}} \right] \\ \quad + \boldsymbol {\beta} \boldsymbol {X} _ {i j t} + \mathrm{REV} _ {i} + \mathrm{REST} _ {j} + \mathrm{T} _ {t} + \varepsilon_ {i j t}, \end{array}\tag{7}
$$

where $X _ { i j t }$ is a vector of time-varying restaurant, reviewer, exogenous and experience characteristics, REV captures reviewer $i ^ { \prime } \mathrm { s }$ fixed effects, REST restaurant $\hat { j } ^ { \prime } { \bf s }$ fixed effects, and $\mathrm { T } _ { t }$ captures time-fixed effects. In the next paragraphs, we discuss the operationalization of reviewer satisfaction and popularity difference (δ), and we describe the set of control variables that form vector $X _ { i j t }$

## 3.1. Operationalization of Reviewer Satisfaction

We utilize two different manifestations of reviewer satisfaction: (1) the review’s star rating (1–5), and (2) the review’s text-encoded sentiment. Although these two measures are typically correlated (Ganu et al. 2009), their alignment is not perfect (Garcia and Schweitzer 2011, Terzi et al. 2011, Mudambi et al 2014). Studying both dimensions is particularly important because they both affect recommender systems (Xiang et al. 2015, Guo et al. 2017), sales (Hu et al. 2014), and review helpfulness (Tsang and Prendergast 2009, Hong et al. 2016).

Table 1. Data Overview

<table><tr><td></td><td>Mean</td><td>Median</td><td>Min</td><td>Max</td><td>Standard Deviation</td></tr><tr><td>Reviewer reviews as local</td><td>8</td><td>4</td><td>1</td><td>359</td><td>13</td></tr><tr><td>Reviewer reviews as traveler</td><td>16</td><td>9</td><td>1</td><td>639</td><td>22</td></tr><tr><td>Reviews per reviewer</td><td>24</td><td>15</td><td>3</td><td>661</td><td>29</td></tr><tr><td>Restaurant reviews</td><td>15</td><td>9</td><td>3</td><td>1,187</td><td>21</td></tr><tr><td>Restaurant price range ($-$$$)</td><td>2.14</td><td>2</td><td>1</td><td>4</td><td>0.77</td></tr><tr><td>Restaurant mean rate</td><td>4.01</td><td>4</td><td>1.43</td><td>5</td><td>0.43</td></tr><tr><td>Location restaurants</td><td>34</td><td>13</td><td>1</td><td>1,744</td><td>92</td></tr><tr><td>Location population</td><td>83,239</td><td>35,255</td><td>576</td><td>8,537,673</td><td>289,351</td></tr><tr><td>Location income</td><td>50,241</td><td>48,138</td><td>21,883</td><td>106,143</td><td>12,413</td></tr><tr><td>Location restaurant reviews</td><td>518</td><td>180</td><td>4</td><td>15,785</td><td>1,261</td></tr><tr><td>Location hotel reviews (ξ, location popularity)</td><td>10,671</td><td>2,958</td><td>1</td><td>918,387</td><td>42,212</td></tr></table>

Notes. The data set includes 763,658 reviews posted by 31,812 reviewers on 50,194 restaurants. All the reviewers and restaurants are located in 1,484 cities in the continental United States. The reviews span 14 years (2004–2018). In the data set, 340,562 reviews were posted from reviewers who traveled to more popular locations (δ > 0), 168,506 from reviewers who traveled to less popular locations $( \delta < 0 )$ , and 254,577 reviews from reviewers who did not travel (δ 0).

The star rating of each review is readily available in our data set. To evaluate the valence encoded in the review text, we utilize the Linguistic Inquiry and Word Count (LIWC) text analysis software (LIWC 2018). LIWC adopts a dictionary-based approach and has recently been successfully used to estimate sentiment and emotionality in online reviews (Sridhar and Srinivasan 2012, Goes et al. 2014, Yin et al. 2014, Hong et al. 2016). In our own context, we use the number of positive and the number of negative words (as reported by LIWC) to encode the positive and negative sentiment in each review. We then estimate the ratio of positive to negative terms $\textstyle { \binom { P + 1 } { N + 1 } }$ as a measure of the review’s sentiment (Doshi et al. 2010, Maynard and Funk 2011, Dehkharghani et al. 2012). This ratio allows us to combine the two counts in a variable that has a similar behavior as the review’s rating: a lower ratio value represents negative sentiment, whereas a higher ratio value represents positive sentiment.

## 3.2. Operationalization of Popularity Difference

We operationalize popularity via the total number of hotel reviews posted in that location (ξ). Our approach is grounded on the need for (1) a measure that is applicable across hundreds of distinct locations, and (2) our focus on online review systems. Hence, we define popularity difference δ to be the difference in hotel reviews between the baseline (hometown, ξ ) and destination $( \xi _ { d } )$ of the traveler. Table 1 shows that ξ has a long tail. As a result, we log-transform it and define popularity difference δ as follows:<sup>2</sup>

$$
\begin{array}{c} \text { Popularity   difference   : =   \delta = \log(\xi_ {d}) - \log(\xi_ {h})} \\ = \log \left(\frac {\xi_ {d}}{\xi_ {h}}\right). \end{array}\tag{8}
$$

We assume that popularity difference will have diminishing effects: the marginal increase of $\Delta \delta$ has a different meaning when δ is small than when it is large. For instance, traveling from a small town with one hotel and 10 hotel reviews to New York ( 918, 000 reviews) is not much different than traveling from the same town to Los Angeles ( 185, 000 reviews), even though New York has almost five times more RepPlatform hotel reviews than Los Angeles. Figure 2 visualizes such diminishing effects of popularity difference under the two competing sets of hypotheses and reveals that, to encode this intuition, function f δ must regulate δ into a sigmoid

To find an appropriate function that is signpreserving and has a sigmoid shape, we draw on the extensive literature on neural networks (Haykin 1994). Four activation functions are natural options for our scenario: tanh, arctan, softsign, and the inverse square root unit (Haykin 1994). Table D13 in Appendix D.4 compares the performance of these functions (along with a linear and a quadratic transformation). The results show that the arctan transformation yields the highest fit for our data. Hence, we choose the following:

$$
f (\delta) = \arctan (\delta).\tag{9}
$$

## 3.3. Control Variables

Our goal is to identify any manifestation of popularitydifference bias on customer reviews. To reiterate, various endogenous and exogenous characteristics affect the review-authoring process, including selfselection (Ho et al. 2017, Hu et al. 2017), social identity (Li et al. 2017, Wang et al. 2018), social norm (Burtch et al. 2017), monetary incentives (Khern-am nuai et al. 2018), prior ratings (Moe and Trusov 2011,

Figure 2. (Color online) Diminishing Effects of Popularity Difference  
![](/api/attachments/V7RKT2T2/fulltext/images/226a3fb8d890ba860d37e630ccd19cf50adcbe69efd72844fd24c72d21ef4647.jpg)  
Note. Shape and sign of popularity-difference bias according to the two competing hypotheses.

Lee et al. 2015), the reviewer and product popularity (Goes et al. 2014, Lee et al. 2015), market competition (Gutt et al. 2019), and demographics (Bakhshi et al. 2014). To control for many of these factors, we create a set of observed, time-varying variables:

3.3.1. Time-Varying Exogenous Characteristics. Equation (2) includes terms that capture how exogenous factors affect satisfaction. In our specifications, we control for the distance traveled (“distance traveled,” Huang et al. 2016), for monetary (“income difference”), and for population-specific (“population ratio”) differences between the reviewer’s hometown and the visiting location.

3.3.2. Time-Varying Reviewer Characteristics. Over time, reviewers evolve and adjust their preferences both in terms of places that they visit and dine in, as well as in terms of the way they evaluate their experience. To capture this evolution, we control for a number of time-varying characteristics. Specifically, we measure (1) the familiarity of the reviewer (“destination familiarity”) with the visited location through the number of repeated visits, (2) the reviewer’s current rating trend (“reviewer current baseline”) through the average rating of the previously posted reviews, (3) the reviewer’s local-to-visitor ratio of reviewed restaurants (“reviewer local-to-traveler ratio”), which controls for reviewers who review either more or less as travelers than as locals, (4) the experience (“reviewer number of reviews”) of a reviewer in reviewing restaurants, (5) the average ratings (“reviewer type (rate)”), and price-range (“reviewer type (price range)”) of previously visited restaurants.

3.3.3. Time-Varying Restaurant Characteristics. Similar to reviewers, restaurants evolve over time. They change menus, hire different chefs, and renovate their interiors. To capture any potential effects of such time-varying characteristics of restaurants on the review-authoring process, we control for (1) the percentile position of the restaurant in its city (“restaurant position”), which captures how a restaurant ranks among its local competitors, (2) the current average rating of the restaurant (“restaurant rate”), (3) the current ratio of local-to-visitor guests of the restaurant (“restaurant local-to-traveler ratio”), which captures the affinity of the restaurant to tourists and locals, and (4) the current popularity of the restaurant through its number of total reviews (“restaurant number of reviews”).

3.3.4. Experience-Speci<sup>fi</sup>c Characteristics. The timevarying observed controls capture a generic observable state of the environment, reviewer, and restaurant. However, they do not fully describe hidden features that could have affected the dining experience. At the same time, reviewers sometimes reveal some of these hidden experience-specific characteristics in their review text. To extract these characteristics from the review text, we use a Distributed Memory Model (DMM; Le and Mikolov 2014), which maps each review into a vector of real numbers. The primary parameter of this process is the dimensionality of the embedding space. We set this value to 30 because higher values did not improve the fit of our models. As a result, we get 30 additional variables that control for experience-specific information the reviewers mention in the review text (e.g., trip purpose and visit-specific events). We name these variables as “deep learning attributes.” Finally, we also control for the review length (“review length (log)”), which is known to be correlated with the assigned ratings (Kokkodis and Lappas 2016, Kokkodis et al. 2019).

Table 2 summarizes the descriptive statistics for the dependent, focal, and control variables. (We show the descriptive statistics of the 30 deep learning attributes in Appendix H, Table H17.) All time-varying controls are estimated at the time of each posted review by using complete snapshots of reviewer and restaurant histories.

Table 2. Descriptive Statistics of the Dependent, Focal, and Control Variables

<table><tr><td></td><td>Mean</td><td>Median</td><td>Min</td><td>Max</td><td>Standard Deviation</td></tr><tr><td colspan="6">Dependent variables</td></tr><tr><td>Rating</td><td>4.07</td><td>4</td><td>1</td><td>5</td><td>0.94</td></tr><tr><td>Text-encoded sentiment</td><td>3.85</td><td>3</td><td>0.06</td><td>43</td><td>2.67</td></tr><tr><td colspan="6">Focal variable</td></tr><tr><td>Popularity difference (δ)</td><td>0.71</td><td>0</td><td>-13.73</td><td>13.73</td><td>2.2</td></tr><tr><td colspan="6">Time-varying exogenous characteristics</td></tr><tr><td>Distance traveled</td><td>415</td><td>78.59</td><td>0</td><td>3,980</td><td>622</td></tr><tr><td>Population ratio</td><td>9.31</td><td>1</td><td>0</td><td>9,260</td><td>70.09</td></tr><tr><td>Income difference (in thousands $)</td><td>-0.25</td><td>0</td><td>-68.95</td><td>72.31</td><td>11.64</td></tr><tr><td colspan="6">Time-varying reviewer characteristics</td></tr><tr><td>Destination familiarity</td><td>1.58</td><td>1.39</td><td>0</td><td>5.46</td><td>0.9</td></tr><tr><td>Reviewer current baseline</td><td>4.08</td><td>4.08</td><td>1</td><td>5</td><td>0.43</td></tr><tr><td>Reviewer local-to-traveler ratio</td><td>0.43</td><td>0.38</td><td>0</td><td>1</td><td>0.38</td></tr><tr><td>Reviewer type (rate)</td><td>4.12</td><td>4.12</td><td>1.5</td><td>5</td><td>0.13</td></tr><tr><td>Reviewer number of reviews</td><td>2.16</td><td>1.39</td><td>0.69</td><td>6.84</td><td>1.55</td></tr><tr><td>Reviewer type (price range)</td><td>1.92</td><td>1.91</td><td>1</td><td>3</td><td>0.2</td></tr><tr><td colspan="6">Time-varying restaurant characteristics</td></tr><tr><td>Restaurant position</td><td>0.49</td><td>0.45</td><td>0</td><td>1</td><td>0.23</td></tr><tr><td>Restaurant rate</td><td>4.05</td><td>4.09</td><td>1</td><td>5</td><td>0.44</td></tr><tr><td>Restaurant local-to-traveler ratio</td><td>0.41</td><td>0.4</td><td>0</td><td>1</td><td>0.32</td></tr><tr><td>Restaurant number of reviews</td><td>2.66</td><td>2.48</td><td>0.69</td><td>7.4</td><td>1.16</td></tr></table>

## 4. Results

The specification of Equation (7) controls for observed and unobserved characteristics that could endogenize our analysis. In particular, the control variables capture the observed time-varying heterogeneity across the population of different restaurants, reviewers, locations, and experiences. The fixed effects control for time-invariant unobserved heterogeneity that originates from the reviewers, the restaurants, the locations, and the timing of the review. Furthermore, restaurant fixed effects control for any unobserved time-invariant effects of the destination city because the location of the restaurant does not change over time. Similarly, reviewer fixed effects control for the unobserved static effect of the reviewer’s hometown. Finally, our data set allows us to mitigate part of the selection bias that originates from the heterogeneity in the reviewers’ choice to review: because we compare reviews of the same reviewer both as a traveler and as a local $( \mathrm { i . e . , }$ all the reviewers we consider post reviews both as locals and as travelers), the reviews of any given reviewer are a result of the same basic underlying review-authoring process (static part of self-selection to review).

## 4.1. Main Empirical Analysis

Table 3 shows the results of a series of different specifications. For the rating, we start from very simple models (A1) that do not control for many of the possible confounding factors, and then increase the level of conservatism as we move to column (A5), which represents the complete specification of Equation (7). For the text-encoded sentiment, column (B1)

of Table 3 presents the complete specification of Equation (7). (Appendix B shows fewer conservative estimates.) In all specifications, the coefficients of interest are positive and statistically significant $( p \mathrm { - v a l u e < 0 . 0 1 } )$ This provides support for the performance-dominant Hypotheses 1a and 1b: the popularity-difference effect on perceived performance is larger than the popularity-difference effect on expectations.

Table 3 further shows that the coefficient $\alpha ^ { \delta < 0 }$ is consistently greater than the coefficient $\alpha ^ { \delta > 0 }$ , in all specifications (p value < 0.001). In fact, in the most conservative specification for the rating (A5), $\alpha ^ { \delta < 0 }$ is almost three times larger than $\alpha ^ { \delta > 0 }$ . Potentially this asymmetry is an artifact of the inflated data distribution: given that the average rating is 4.07, there is more room for reviewers to deviate from this in the negative than in the positive direction. This observation further explains why there is less asymmetry in the text-encoded sentiment (column B1).

To find additional empirical evidence in support of the hypothesized mechanism (Section 2), we look into the raw review text, and we perform a topic modeling analysis (Blei et al. 2003). One of the recovered topics stands out as “destination characteristics.” It includes words such as:

{culture, painting, outdoor patio, beach, water, river, boat, bay, ocean, lake, pier, harbor, hill, area, picnic}.

Figure 3 shows that as popularity difference increases (in both directions), the prevalence of the focal topic also increases $( p < 0 . 0 0 1 )$ ). This suggests that, as predicted by our theoretical framework, the higher the popularity difference the stronger are the destination characteristics spillovers in the reviewer satisfaction, which is captured by the review text.

Table 3. Popularity-Difference Effects on Rating and Text-Encoded Sentiment

<table><tr><td></td><td>(A1)</td><td>(A2)</td><td>(A3)</td><td>(A4)</td><td>(A5)</td><td>(B1)</td></tr><tr><td>Popularity difference δ &gt;0</td><td>0.06***(0.003)</td><td>0.05***(0.002)</td><td>0.05***(0.003)</td><td>0.04***(0.003)</td><td>0.03***(0.005)</td><td>0.03*(0.015)</td></tr><tr><td>Popularity difference δ &lt; 0</td><td>0.11***(0.003)</td><td>0.09***(0.003)</td><td>0.08***(0.003)</td><td>0.09***(0.003)</td><td>0.07***(0.004)</td><td>0.06***(0.014)</td></tr><tr><td>Distance traveled (log)</td><td>0.01***(0.001)</td><td>0.01***(0.001)</td><td>0.01***(0.001)</td><td>0.01***(0.001)</td><td>0.01***(0.001)</td><td>0.01***(0.002)</td></tr><tr><td>Destination familiarity</td><td>-0.02***(0.001)</td><td>-0.01***(0.001)</td><td>-0.03***(0.001)</td><td>-0.02***(0.001)</td><td>-0.03***(0.002)</td><td>-0.03***(0.005)</td></tr><tr><td>Restaurant position</td><td>-0.14***(0.009)</td><td>-0.10***(0.009)</td><td>-0.09***(0.010)</td><td>-0.33***(0.013)</td><td>-0.32***(0.014)</td><td>-0.26***(0.041)</td></tr><tr><td>Restaurant rate</td><td>0.75***(0.005)</td><td>0.63***(0.005)</td><td>0.62***(0.005)</td><td>0.79***(0.006)</td><td>0.78***(0.007)</td><td>0.51***(0.019)</td></tr><tr><td>Restaurant local-to-traveler ratio</td><td>0.06***(0.004)</td><td>0.05***(0.003)</td><td>0.05***(0.004)</td><td>0.05***(0.007)</td><td>0.05***(0.008)</td><td>0.05(0.026)</td></tr><tr><td>Restaurant number of reviews</td><td>0.01***(0.001)</td><td>0.00**(0.001)</td><td>0.00(0.001)</td><td>-0.03***(0.003)</td><td>-0.03***(0.003)</td><td>-0.06***(0.010)</td></tr><tr><td>Reviewer current baseline</td><td>0.82***(0.002)</td><td>0.69***(0.002)</td><td>0.86***(0.006)</td><td>0.69***(0.003)</td><td>0.85***(0.006)</td><td>0.45***(0.016)</td></tr><tr><td>Reviewer local-to-traveler ratio</td><td>0.00(0.003)</td><td>0.00(0.003)</td><td>-0.02***(0.004)</td><td>0.01*(0.003)</td><td>-0.01**(0.004)</td><td>-0.01(0.013)</td></tr><tr><td>Reviewer type (rate)</td><td>-0.55***(0.007)</td><td>-0.55***(0.007)</td><td>-0.52***(0.013)</td><td>-0.60***(0.008)</td><td>-0.55***(0.014)</td><td>-0.34***(0.045)</td></tr><tr><td>Reviewer number of reviews</td><td>0.00***(0.001)</td><td>-0.01***(0.001)</td><td>0.00(0.002)</td><td>-0.01***(0.001)</td><td>0.00*(0.002)</td><td>0.02**(0.007)</td></tr><tr><td>Population ratio (log)</td><td>0.00***(0.001)</td><td>0.00***(0.001)</td><td>0.01***(0.001)</td><td>0.01***(0.001)</td><td>0.00(0.009)</td><td>-0.00(0.027)</td></tr><tr><td>Income difference</td><td>0.00**(0.000)</td><td>0.00*(0.000)</td><td>0.00(0.000)</td><td>0.00***(0.000)</td><td>-0.00(0.001)</td><td>0.00(0.004)</td></tr><tr><td>Reviewer type (price range)</td><td>-0.06***(0.005)</td><td>-0.12***(0.005)</td><td>-0.03**(0.010)</td><td>-0.16***(0.005)</td><td>-0.09***(0.011)</td><td>-0.04(0.035)</td></tr><tr><td>Review length (log)</td><td>-0.76***(0.009)</td><td>-0.44***(0.011)</td><td>-0.60***(0.017)</td><td>-0.47***(0.012)</td><td>-0.68***(0.018)</td><td>3.05***(0.059)</td></tr><tr><td>Deep learning attributes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>User FE</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Restaurant FE</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>763,658</td><td>763,658</td><td>763,658</td><td>763,658</td><td>763,658</td><td>763,658</td></tr><tr><td> $R^2$ </td><td>0.339</td><td>0.434</td><td>0.478</td><td>0.483</td><td>0.525</td><td>0.316</td></tr></table>

Notes. Standard errors in parentheses, robust for (A1) and (A2) and clustered for (A3) to (A5). DV, dependent variable. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

## 4.2. Alternative Empirical Analyses

The main analysis relies on observational data, which limits our ability to establish a causal link between the focal variables and the assigned rating. However, additional robustness checks and sensitivity analyses can increase our confidence in the main results. We test the robustness of the observed results in the following scenarios:

• Bias due to differences in reviewers’ dining patterns as travelers and as locals.

• Population imbalance between locals and travelers

• Simulations of time-varying unobserved selection bias.

• Alternative models.

• Sensitivity to outliers.

• Sensitivity to trip purpose.

Table 4 summarizes the results of these robustness checks that provide additional support to the main findings. Appendix C presents the details of these analyses.

Furthermore, to provide additional support for the underlying mechanisms discussed in Section 2, on top of the presented topic models analysis in Section 4, we

Figure 3. (Color online) Destination Spillovers in Text  
![](/api/attachments/V7RKT2T2/fulltext/images/75989bd9547fb0403fc8c97658d48fd202c6be37de4c15d3b09370148b96fed2.jpg)  
Notes. As the popularity difference increases (both in positive and in a negative direction), so does the prevalence of destination spillovers in the review text.

use regular expressions and find empirical evidence that mentions of a destination’s name are positively associated with popularity difference. Finally, we test and eliminate alternative comparison levels (instead of a reviewer’s hometown), and we showcase the appropriation of the proposed operationalization of destination popularity. Table 5 summarizes these results. Appendix D provides the details of these analyses.

## 5. Economic Impact and Implications of Popularity-Difference Bias

What is the economic impact of popularity-difference bias? To investigate this question, we estimate the effect of popularity-difference bias on (1) the average rating and revenue of a venue, and (2) on the venue’s consideration probability. In addition, we examine the heterogeneity of popularity-difference bias across different types of restaurants in the same location, and we conclude this section by showcasing design-science examples of how platforms can mitigate or exploit the existence of popularitydifference bias.

Table 4. Robustness Analysis Summary

<table><tr><td rowspan="2">Methodology</td><td colspan="2">DV: rating</td><td colspan="2">DV: text-encoded sentiment</td><td rowspan="2">Appendix</td></tr><tr><td>H1A</td><td>H1B</td><td>H1A</td><td>H1B</td></tr><tr><td colspan="6">Bias due to differences in reviewers&#x27; dining patterns as travelers and as locals</td></tr><tr><td>Reviewer × chain FE, on reviewers who visit restaurants of the same chain as locals and as travelers</td><td>✓</td><td>✓</td><td>✕</td><td>✕</td><td>C.1</td></tr><tr><td>Reviewer × matched-restaurants FE (matching local with visiting restaurants through nearest neighbor)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>C.1</td></tr><tr><td colspan="6">Selection bias (imbalance between locals and travelers)</td></tr><tr><td>Propensity score matching</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>C.2</td></tr><tr><td>Rosenbaum sensitivity</td><td>1.29</td><td>1.31</td><td>1.15</td><td>1.12</td><td>C.2</td></tr><tr><td colspan="6">Time-varying unobserved selection bias</td></tr><tr><td>Undersampling of populations who travel more/less to destinations with lower/higher popularity, are more positive/negative, and review more/less</td><td>&gt;15%</td><td>&gt;25%</td><td>&gt;20%</td><td>&gt;25%</td><td>C.3</td></tr><tr><td colspan="6">Alternative models</td></tr><tr><td>Ordered logit, &quot;blow-up and cluster&quot; ordered logit, and generalized ordered logit</td><td>✓</td><td>✓</td><td>NA</td><td>NA</td><td>C.4</td></tr><tr><td colspan="6">Outlier sensitivity</td></tr><tr><td>Removing reviewers from the top three locations (New York, Las Vegas, Atlanta)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>C.5</td></tr><tr><td>Removing restaurants from the top three locations (New York, Las Vegas, Chicago)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>C.5</td></tr><tr><td colspan="6">Sensitivity to trip purpose</td></tr><tr><td>Empirical evidence that the deep learning attributes capture trip purpose</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>C.6</td></tr></table>

Notes. 3, hypothesis supported; !, hypothesis not supported at p < 0.05; NA, not applicable. For the undersampling analysis, > prc% shows the maximum percentage prc of the two most adversarial regions of selection biases for which our results remain unchanged (Figures C2–C4).

Table 5. Support for the Theoretical Framework and the Popularity Operationalization

<table><tr><td>Methodology</td><td>Appendix</td></tr><tr><td>Textual evidence in support of underlying mechanisms</td><td></td></tr><tr><td>Regular expression analysis shows that travelers&#x27; mentions of the visited city are positively associated with popularity difference</td><td>D.1</td></tr><tr><td>Empirical elimination of alternative comparison levels</td><td></td></tr><tr><td>Average prior locations</td><td>D.2</td></tr><tr><td>Most frequent location</td><td>D.2</td></tr><tr><td>Appropriation of the popularity measure (ξ)</td><td></td></tr><tr><td>Comparison with various published destination rankings</td><td>D.3</td></tr><tr><td>Alternative popularity difference functions</td><td></td></tr><tr><td>Alternative transformations of δ</td><td>D.4</td></tr></table>

## 5.1. Effect on Restaurant Ratings and Revenue

Previous studies have repeatedly shown the strong effect of online ratings on sales (Duan et al. 2008b, Zhu and Zhang 2010, Sun 2012). To showcase the effect of popularity-difference bias on venue ratings, we estimate the component of the average rating of a restaurant that is attributed to popularity-difference bias through the estimated coefficients of the most conservative specification of Table 3 $( \alpha ^ { \delta > 0 } = 0 . 0 3$ and $\alpha ^ { \delta < 0 } = 0 . 0 7 )$ . For each restaurant j with a total number of reviews $M _ { j }$ in our data set, the respective popularity difference bias $( b _ { j } ^ { \delta } )$ is as follows (Equation (6)):

$$
\begin{array}{l} b _ {j} ^ {\delta} = \frac {1}{| M _ {j} |} \sum_ {m \in M _ {j}} \frac {1}{R ^ {\prime} {} _ {m j}} \arctan (\delta_ {m j}) \\ \qquad \times \left[ (0. 0 3 \mathbb {1} _ {\delta_ {m j} > 0} + 0. 0 7 \mathbb {1} _ {\delta_ {m j} <   0} \right], \end{array}\tag{10}
$$

where ${ R ^ { \prime } } _ { m j }$ is the predicted rating of restaurant j of review m through the coefficients and fixed effects of the complete specification of Equation (7). This bias estimate captures the actual effect on the average restaurant rating according to the location–specific distribution of the restaurant reviewers. For comparison, we also estimate the resulting bias from the traveled distance (d):

Distance-traveled bias on restaurant j ratings :<sub></sub>

$$
\frac {1}{| M _ {j} |} \sum_ {m \in M _ {j}} \frac {1}{R ^ {\prime} {} _ {m j}} 0. 0 1 \times \log (d _ {m j}).\tag{11}
$$

Figure 4 shows the results. The average per-restaurant popularity-difference bias ranges from <sup>−</sup>11% in some cases to almost 3% in others. It further affects 98% of the restaurants (in other words, only 2% of the restaurants in our data set have reviews only from local reviewers). In comparison, the positive effect of distance traveled ranges from 0% to 3%. Figure 5A further shows that popularity difference effects are stronger on restaurants that rank in the lower percentiles.

To get an estimate of the effect of popularity difference on restaurant revenue, we rely on previous work and assume that a one-star rating increase is associated with a $7 \%$ revenue increase (Luca 2018). Then, the average revenue effect for a restaurant j is

Figure 4. (Color online) Popularity-Difference Bias and Distance-Traveled Bias Distributions  
![](/api/attachments/V7RKT2T2/fulltext/images/0949222926858e5ec19daa2ae48d0ee1b20c0897e89c9ce16f56dc9b025df709.jpg)  
Notes. Popularity-difference bias varies from <sup>−</sup>11% to 3%. For comparison, distance-traveled bias varies from 0% to 3%.

Figure 5. (Color online) Popularity-Difference Effect on Average Rating and Revenue by Percentile  
![](/api/attachments/V7RKT2T2/fulltext/images/ba1c29f5ffde6e672d5b4087787c2205ccb52fe0b5b7ba9cc5f69e77287c8b5f.jpg)  
Note. Lower-ranked restaurants experience a stronger (positive or negative) bias effect on their average ratings and revenue.

Popularity-difference bias effect on revenue

$$
:= b _ {j} ^ {\delta} * \bar {R} _ {j} ^ {\prime} \times 0. 0 7,\tag{12}
$$

where ${ \bar { R } } _ { j } ^ { \prime }$ is the average predicted rating of restaurant j through the coefficients and fixed effects of the complete specification of Equation (7). Figure 5B shows the revenue effects for each percentile, which range between 2% and <sup>−</sup>2%.

## 5.2. Effect on Rankings and Consideration Probability

Next, we explore the effects of popularity-difference bias on the consideration probability of each restaurant. The consideration probability is the likelihood that customers will shortlist an item to the set of items that they will ultimately choose from (Andrews and Srinivasan 1995). During a standard session on a review-based reputation platform, the user begins searching for a restaurant by specifying a city and (possibly) a set of other criteria (e.g., price range). The platform then returns a ranking of all the matching restaurants within the city. A significant body of work has verified the importance of such rankings on the ultimate choice (Ghose et al. 2012, 2014; Pan 2015). Although the exact process that users follow when considering a ranking can vary, the consensus is that users follow the ranked list in a top-down fashion and the probability of considering (clicking) a business declines as the user moves down the list (Pan et al. 2007). Having verified the existence of popularitydifference bias in the review ratings, we examine whether the effect of this bias perturbs the reviewbased rankings and changes the consideration probability of each restaurant.

In order to perform this analysis, we need to estimate (i) the ranking-function that RepPlatform employs, and (ii) the consideration model that users follow when processing a ranking. For the first estimation task, we follow previous relevant work (Lappas et al. 2016) and formulate the problem as a constrained optimization task that we then solve by a linear Support Vector Machine (SVM; Joachims 2002). We describe the process in detail in Appendix E. For the second task, rather than assuming a single consideration model, we consider five different models that capture alternative behavioral profiles (Lappas et al. 2016). We visualize the models in Figure 6. The xaxis represents positions in the ranking, whereas the y-axis represents the probability that an item will be considered according to its rank. The linear mode represents users whose consideration probability decays linearly for lower positions in the ranking. The exponential model represents users who focus only on a small set of top-ranked items and exhibit a sharp drop in consideration after that. It is based on the exponential distribution and can thus be tuned via a parameter λ. Finally, the stretched exponential mode is based on the Weibull distribution and adopts the shape parameter k. It stretches user consideration across a larger set of top-ranked items and thus offers a medium between the first two models.

For each of the five consideration models, we use the reviews with and without popularity-difference bias (Equation (10)) to compute the restaurant ranking for each of the cities in our data set. We then compute the absolute difference in the consideration probability of each restaurant in the two scenarios. Figure 7 reports the mean and the 95% confidence intervals of the difference in consideration probability for each position in the (original biased) ranking. We observe that, for all five models, the difference in consideration probability due to popularity-difference bias can be as high as 11%–16%. The size of the effect varies according to the position in the ranking and the consideration model. In steep consideration models, the effect is very large in the top positions and then fades quickly as the consideration probability decreases drastically. On the other hand, for the linear model, the effect slowly rises for lower positions in the ranking and converges at around 11%.

Figure 6. (Color online) Various Expressions of Consideration Probabilities  
![](/api/attachments/V7RKT2T2/fulltext/images/710e120f9ef72716321e8ee5f4fed6d3e6964a59ef14e2e7a90cb5f47ee5caf5.jpg)  
Notes. Exponential consideration probabilities drop rapidly with a rank increase. Stretched exponential consideration probabilities smooth this drop.

Given that a restaurant has to be considered before it is ultimately chosen by the user, this analysis reveals that popularity-difference bias significantly affects a restaurant’s market segment and revenue. For instance, consider a restaurant that has (on average) a 15% probability of being chosen after the user considers it. If the platform gets 10,000 monthly visitors for the restaurant’s city, then a popularity difference bias of 16% is responsible for 240 (more or fewer) customers every month.

## 5.3. Within-Location Heterogeneous Effects of Popularity-Difference Bias

Finally, it is interesting to identify examples of different types of restaurants that experience heterogeneous effects of popularity-difference bias even within the same location. We start by clustering restaurants into different types according to their cuisine and targeted audience (e.g., families, romance, business meetings, etc.). For each cluster, we estimate the within-location average effect of popularity-difference bias. Figures H7 and H8 in Appendix H show the detailed results for eight different locations. These examples show that, even within the same location, some types of restaurants experience negative popularity-difference bias, whereas others experience positive popularity-difference bias. For instance, Greek restaurants in Long Beach, California are hurt the most by popularity-difference bias, whereas cafes in the same location benefit the most (Figure H7A). To the contrary, cafes in San Jose, California are hurt the most, whereas San Jose delis experience strong positive popularity-difference bias (Figure H7C). In Detroit, Michigan, restaurants that focus on business meetings experience a strong negative popularity-difference bias, whereas romantic restaurants experience a positive popularity-difference bias (Figure H8A). To the contrary, romantic restaurants in Temecula, California experience a negative popularity-difference bias, whereas restaurants in the same location with scenic views experience a positive popularity-difference bias (Figure H8C). These examples show how popularity-difference bias might disproportionately hurt or benefit restaurants that are located close by and compete with each other for a better position in the same consideration set.

Figure 7. (Color online) Popularity-Difference Effect on Consideration Probabilities  
![](/api/attachments/V7RKT2T2/fulltext/images/f487213a6a6781fd7eff6b83be36364c73c6e4f16938c7e055b7076d5189d345.jpg)  
Note. Depending on the expression that describes the association of the consideration probability with the ranking position of the restaurant, popularity-difference bias alters consideration probabilities by up to 16%.

## 5.4. Design Implications for Platforms

Given that Popularity-Difference Bias Has a Significant Effect on Restaurant Ratings, Revenue, and Rankings, What Can Platforms Do to Improve Their Ranking Mechanisms Design?

Reputation platforms have long acknowledged the importance of mechanisms that help users quickly eliminate or focus on specific types of reviews that could provide alternative perspectives on the reviewed businesses (Youngblade 2012, Furner and Zinko 2017). For instance, platforms currently provide multiple ranking filters such as “Recommended,” “Highest rated,” and “Most reviewed.” As a result, adding an additional filter would incur a very small marginal cost. Our findings suggest that a meaningful action for platforms would be to generate unbiased rankings and include those in their filtering mechanisms. One way to do so is by considering all the reviews and adjusting for popularity-difference bias according to Equation (10). A second way would be to statistically ignore biased reviews. In particular, platforms can compute whether two locations have significantly different popularity levels. For instance, they can cluster all available locations according to their popularity. Locations in the same cluster would then be considered as not being significantly different. The clustering step can be completed by appropriate methods for one-dimensional clustering, such as Jenks natural breaks optimization (Jenks 1967) or Kernel Density Estimation (Rosenblatt 1956). Alternatively, platforms could utilize percentiles rather than clusters and group locations if the difference between their respective popularity percentiles is smaller than a tolerance parameter.

Platforms can also exploit the existence of popularitydifference bias to generate personalized rankings. Specifically, platforms can generate popularity-specific rankings according to whether people are visiting a local $( \delta = 0 )$ , a more popular $( \delta > 0 )$ , or a less popular destination $( \delta < 0 )$ ). These rankings will only consider reviews from similar travelers: when a traveler i visits a more popular destination, only reviews from travelers for which the focal destination was also more popular would contribute to the personalized ranking for i. Similarly, when a traveler i visits a less popular destination, only reviews from travelers for which the focal destination was also less popular would contribute to the personalized ranking for i. Hence, platforms can generate three types of rankings: one for locals that only consider local reviewers $( \delta = 0 )$ , one for travelers to more popular locations $( \delta > 0 )$ , and one for travelers to less popular locations $( \delta < 0 )$

To showcase whether such an approach would yield better results, we generate the three personalized rankings and compare them with the current ranking that considers all available reviews. For each of the three personalized rankings $c \in \{ \delta = 0 , \delta < 0 ,$ $\delta > 0$ , we define the average satisfaction improvement as follows:

$$
\text { Satisfaction   improvement } (\%) = \frac {A V G \left(R _ {p} ^ {c}\right)}{A V G \left(R _ {p} ^ {c \in \text { current }}\right)},\tag{13}
$$

where AVG stands for average, $R _ { p } ^ { c }$ are the ratings for restaurants in the $p ^ { t h }$ percentile according to the c-personalized ranking, and $R _ { p } ^ { c \in \mathrm { c u r r e n t } }$ are the ratings of c-type reviewers for restaurants in the $p ^ { t h }$ percentile according to the current ranking. In other words, satisfaction improvement measures how much higher (or lower) the ratings of c-reviewers are for restaurants in the $p ^ { t h }$ percentile of the c ranking compared with restaurants in the $p ^ { t h }$ percentile of the current ranking that considers all available reviews.

An ideal ranking would clearly separate the highquality restaurants from the low-quality ones. Compared with the current ranking, which our study reveals to be biased, personalized rankings should generate higher satisfaction in the top-ranked percentiles and lower satisfaction in the bottom-ranked ones. Figure 8 shows this pattern for four different cities in our data: New York, New York, which has the highest number of hotel reviews (918,387) and as a result there are no personalized rankings for travelers with $\delta < 0$ , Boston, Massachusetts, which is a big urban center (166,416 hotel reviews), Portland, Ore gon, which is a smaller urban center (84,019 hotel reviews), and finally Aiken, South Carolina, which is a very small town with only 3,346 hotel reviews and has very few travelers visiting from less popular locations. In all cities, personalized rankings yield significantly higher satisfaction (up to 12%) in restaurants that rank in the top $4 0 ^ { t h }$ percentile. At the same time, for restaurants ranked in the bottom $4 0 ^ { t h }$ percentile, personalized rankings generate up to 22% lower satisfaction than the current rankings. These observations suggest that the personalized rankings are more appropriate than current rankings in separating high-satisfaction from low-satisfaction restaurants.

Figure 8. (Color online) Personalized Rankings Yield Higher Customer Satisfaction  
![](/api/attachments/V7RKT2T2/fulltext/images/065e2fc12764ea3255932a9301d0040539b0abf0597d50f6f7f0b86479ae8c5b.jpg)  
Note. In all four cities, personalized rankings promote restaurants that yield high satisfaction (top $5 0 ^ { t h }$ percentile), and discourage customers from visiting restaurants that yield low satisfaction (bottom $5 0 ^ { t h }$ percentile).

Personalized rankings have an additional benefit: because they consider characteristics of different populations, they end up recommending a diversified set of restaurants. Figure 9 shows the improvement in terms of the number of different restaurants that each ranking mechanisms recommends at each percentile. Through the proposed personalized ranking system, there is an increase in diversity of up to 24% in the top 10% recommended restaurants. Simply put, consumers get up to 24% more top-tier restaurants, customized to their expected biases.

## 6. Discussion and Managerial Implications

This work showed that both the perceived performance of a venue and expectations of reviewers are affected by the popularity difference between a visiting destination and the reviewer’s hometown. When reviewers travel to a less popular location than their hometown, popularity-difference spillovers result in a negative bias both in the text and rating of the review. To the contrary, when reviewers travel to a more popular location than their hometown, popularity-difference spillovers positively biases the review-authoring process. Therefore, a restaurant’s ratings will skew lower if the restaurant tends to attract guests from more popular locations, and higher if the restaurant tends to attract guests from less popular locations.

Figure 9. (Color online) Personalized Rankings Yield More Diversified Sets of Recommended Restaurants  
![](/api/attachments/V7RKT2T2/fulltext/images/5b89f45d94b8d67c65ee4d167a342730ffd90a3afaa3e995844ff47e58f0d6bd.jpg)

## 6.1. Research Contributions

A long line of research in information systems has focused on studying biases in the review-authoring process—from early-buyer biases (Li and Hitt 2008), to popularity effects (Goes et al. 2014), to social effects through friends (Wang et al. 2018), to disconfirmation effects (Ho et al. 2017), to acquisition effects (Hu et al. 2017) and distance-traveled effects (Huang et al. 2016). Our work extends this line of research by revealing and explaining a new bias in online reviews that depends on the popularity difference between the reviewer’s hometown and the location of the visited business. Specifically, our findings suggest that popularity-difference spillovers on reviewers performance evaluations are stronger than on reviewers’ expectations. This results into a positive bias when travelers visit destinations that are more popular than their hometown, and into a negative bias when they visit less popular destinations. These biases manifest in assigned product ratings, as well as in the review text. Our work is the first to study this type of bias and measure its effects. Our results show that this bias can have significant effects and greatly distort the online reputation, leading to misrepresented businesses and misinformed users.

Furthermore, our work provides a new theoretical and methodological framework for modeling and evaluating influential effects that are driven by semantic (rather than geographical) differences between locations. Although our focus is on popularity, future efforts can explore alternative semantic dimensions, such as a location’s sociopolitical or cultural aspects.

Finally, even though the empirical evaluation focused on restaurants, our theoretical framework and methodology are applicable to any type of venue. This is critical, as we expect popularity-difference spillovers to be present in performance evaluations and expectations relevant to different types of services and visitor activities.

## 6.2. Managerial Implications

Our study informs platform managers about the existence, nature, and effects of popularity-difference bias: a new type of bias that has not been explored by extant research. Popularity-difference bias affects key functionalities of online review platforms, such as business rankings and average ratings. These functionalities are a critical part of a platform’s design, as they allow users to summarize and navigate and benefit from the thousands of reviews that are available for competitive businesses. Our results demonstrate that popularity-difference bias can significantly distort both rankings and average ratings, and even perturb the actual text of the reviews. Our work thus identifies an influential flaw in current platform design. In Section 5, we discussed alternative designs that can eliminate the effects of popularitydifference bias, as well as designs that leverage this type of bias to deliver personalized rankings and ratings for users according to their respective baselines.

A significant portion of businesses in highly popular, touristic destinations choose to capitalize on the city’s popularity by catering more to specific types of visitors. This choice can be reflected on the menu, decoration, ambiance, and other characteristics. On the other hand, other businesses in the same city target all types of customers, rather than focusing on visitors. Such differences can also emerge organically (e.g., some restaurants might build a reputation among specific types of travelers). Regardless of the cause, the end result is that competing business are often likely to attract populations with a variable sensitivity to popularity-difference bias. For instance, consider a restaurant in New York that tends to attract tourists from far less popular locations in the United States, whereas another competing restaurant migh be popular among visitors from other large and popular cities who come to New York for business purposes. In such settings, the popularity-difference bias will disproportionately boost the ratings and consideration probabilities of the first restaurant, leading to unfair competition between business and inflated evaluations by potential customers.

Furthermore, and in addition to the design science approaches we showcased in Section 5.4, platform managers can consider the discovery of popularity difference bias as an opportunity to improve other platform functions. First, the knowledge that travelers are more likely to be satisfied when they travel to destinations with a higher popularity than their baseline can be taken into account when personal izing the results of the platform’s recommendation and search engines. Second, this knowledge can be incorporated into the review-authoring interface that the platform presents to aspiring reviewers. For instance, on TripAdvisor, the interface includes questions on the purpose of the visit and allows the user to assign ratings to specific aspects of the business (e.g., service or value). By extending this interface with questions related to their expectations and impressions from the destination, the platform could motivate reviewers to comment on such factors and provide valuable context for their reviews. Finally, by tracking business reputation across these population segments, the platform can enhance its analyt ics services to businesses. Analytics services have emerged as additional source of revenue, with multiple platforms offering paid subscription plans for different levels of reputation-based insight (TripAdvisor 2018).

## Acknowledgments

The authors thank Konstantinos Pelechrinis for his contri bution in conceptualizing the problem. The authors thank Sam Ransbotham and Rob Fichman for their suggestions on improving the paper.

## Endnotes

<sup>1</sup> The introduction of the traveler’s hometown as a comparison level is consistent with Comparison Level Theory (CLT). CLT suggests that a consumer’s satisfaction with the outcome of a purchase is determined by the discrepancy between the outcome and a standard of comparison known as the comparison level (LaTour and Peat 1979, Thibaut 2017). Outcomes above the comparison level satisfy, whereas those below the comparison level dissatisfy. We chose a traveler’s hometown as a comparison level because hometowns (1) encode characteristics that travelers are accustomed to and (2) shape travelers’ characters, norms, expectations, and experiences (Park and Peterson 2010, Naik et al. 2015, Chen et al. 2018, Perry 2018). We investigate and empirically eliminate alternative comparison levels in Appendix D.2.

<sup>2</sup> We also considered alternative destination popularity proxies before choosing the number of hotel reviews. In particular, the number of hotels could also work for large cities that boast both many and popular hotels. However, this measure would collapse as we advance to the middle and tail of the distribution, where the number of hotels might not align with their quality or the number of travelers. Similarly, the number of restaurants (or reviews thereof) would be misleading: a city with a large population is likely to have a large number of restaurants and restaurant reviews, regardless of its popularity and whether it is an attractive destination for travelers. Finally, Appendix D.3 provides further support for the appropriateness of our operationalization: destination rankings based on the number of hotel reviews ξ perfectly align with a series of publicly available “top destination” lists.

## References

Abubakar AM, Ilkan M (2016) Impact of online WOM on destination trust and intention to travel: A medical tourism perspective. J. Destination Marketing Management 5(3):192–201.

Agarwal S, Sikri S (1996) Country image: Consumer evaluation of product category extensions. Internat. Marketing Rev. 13(4):23–39.

Andrews RL, Srinivasan TC (1995) Studying consideration effects in empirical choice models using scanner panel data. J. Marketing Res. 32(1):30–41.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Bakhshi S, Kanuparthy P, Gilbert E (2014) Demographics, weather and online reviews: A study of restaurant recommendations. Proc. 23rd Internat. Conf. World Wide Web (ACM, New York), 443–454.

Bakos Y, Dellarocas C (2011) Cooperation without enforcement? A comparative analysis of litigation and online reputation as quality assurance mechanisms. Management Sci. 57(11):1944–1962.

Bennett S (2005) Theatre/tourism. Theatre J. 57(3):407–428.

Bhat S, Reddy SK (2001) The impact of parent brand attribute associations and affect on brand extension evaluation. J. Bus. Res. 53(3):111–122.

Bialik C. (2017) The most locals-only restaurants in San Francisco and San Diego. Accessed July 30, 2018, https://www.yelpblog.com 2017/09/locals-restaurants-san-francisco-san-diego.

Bigne JE, Isabel Sanchez M, Sanchez J (2001) Tourism image, eval uation variables and after purchase behaviour: inter-relation ship. Tourism Management 22(6):607–616.

Blakely GL (1993) The effects of performance rating discrepancies on supervisors and subordinates. Organ. Behav. Human Decision Processes 54(1):57–80.

Blei DM, Ng AY, Jordan MI (2003) Latent Dirichlet allocation. J. Machine Learn. Res. 3(1):993–1022.

Bol JC, Smith SD (2011) Spillover effects in subjective performance evaluation: Bias and the asymmetric influence of controllability. Accounting Rev. 86(4):1213–1230.

Bolton GE, Katok E, Ockenfels A (2004) How effective are electronic reputation mechanisms? An experimental investigation. Man agement Sci. 50(11):1587–1602.

Bono JE, Colbert AE (2005) Understanding responses to multi-source feedback: The role of core self-evaluations. Personnel Psych. 58(1): 171–203.

Burtch G, Hong Y, Bapna R, Griskevicius V (2017) Stimulating online reviews by combining financial incentives and social norms. Management Sci. 64(5):2065–2082.

Chen X, Orum AM, Paulsen KE (2018) Introduction to Cities: How Place and Space Shape Human Experience (John Wiley & Sons, New York).

Chen X, Huang Q, Davison RM, Hua Z (2015) What drives trust transfer? The moderating roles of seller-specific and general institutional mechanisms. Internat. J. Electron. Commerce 20(2): 261–289.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chi CG-Q, Qu H (2008) Examining the structural relationships of destination image, tourist satisfaction and destination loyalty: An integrated approach. Tourist Management 29(4):624–636.

Chon K-S (1990) The role of destination image in tourism: A review and discussion. Tourism Rev. 45(2):2–9.

Corsten D, Gropp R, Markou P (2019) Suppliers as liquidity insurers. Preprint, submitted March 28, https://papers.ssrn.com/sol3 papers.cfm?abstract\_id=2980424.

Cui G, Lui H-K, Guo X (2012) The effect of online consumer reviews on new product sales. Internat. J. Electron. Commerce 17(1):39–58.

Dai W, Jin G, Lee J, Luca M (2018) Aggregation of consumer ratings: An application to yelp.com. Quant. Marketing Econom. 16(3): 289–339.

Dehkharghani R, Yanıkoglu B, Tapucu D, Sayg˘ ın Y (2012) Adaptation and use of subjectivity lexicons for domain dependent sentiment classification. Internat. Conf. Data Mining (IEEE, Piscataway, NJ), 669–673.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407–1424.

Dellarocas C (2006) Reputation mechanisms. Hendershott T, ed. Handbook on Economics and Information Systems (Elsevier, Amster dam), 629–660

Doshi L, Krauss J, Nann S, Gloor P (2010) Predicting movie prices through dynamic social network analysis. Procedia Soc. Behav. Sci. 2(4):6423–6433.

Duan W, Gu B, Whinston AB (2008a) Do online reviews matter? An empirical investigation of panel data. Decision Support System 45(4):1007–1016.

Duan W, Gu B, Whinston AB (2008b) The dynamics of online word of-mouth and product sales: An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Duan W, Gu B, Whinston AB (2009) Informational cascades and software adoption on the Internet: An empirical investigation. Management Inform. Systems Q. 33(1):23–48.

Echtner CM, Brent Ritchie JR (1991) The meaning and measurement of destination image. J. Tourism Studies 2(2):2–12.

Fan Y (2006) Branding the nation: What is being branded? J. Vacation Marketing 12(1):5–14.

Font X (1997) Managing the tourist destination’s image. J. Vacation Marketing 3(2):123–131

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Furner CP, Zinko RA (2017) The influence of information overload on the development of trust and purchase intention based on online product reviews in a mobile vs. web environment: an empirical investigation. Electron. Marketing 27(3):211–224.

Ganu G, Elhadad N, Marian A (2009) Beyond the stars: Improving rating predictions using review text content. 12th Internat. Workshop Web Databases (WebDB 2009), Providence, RI.

Gao B, Li X, Liu S, Fang D (2018) How power distance affects online hotel ratings: the positive moderating roles of hotel chain and reviewers travel experience. Tourism Management 65:176–186.

Garcia D, Schweitzer F (2011) Emotions in product reviews–empirics and models. IEEE 3rd Internat. Conf. Privacy, Security, Risk Trust, 2011 IEEE 3rd Internat. Conf. Soc. Comput. (IEEE, Piscataway, NJ), 483–488.

Ghose A, Ipeirotis PG (2011) Estimating the helpfulness and eco nomic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions Knowledge Data Eng. 23(10): 1498–1512.

Ghose A, Ipeirotis PG, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Sci. 31(3):493–520.

Ghose A, Ipeirotis PG, Li B (2014) Examining the impact of ranking on consumer behavior and search engine revenue. Management Sci. 60(7):1632–1654.

Goes PB, Lin M, Ching-man AY (2014) “Popularity effect” in usergenerated content: Evidence from online product reviews. In form. Systems Res. 25(2):222–238.

Gonzalez-Rivera C (2018) Destination New York. Center for an´ Urban Future. Accessed April 16, 2019, https://nycfuture.org/ research/destination-new-york.

Grass J (2017) The impact of holiday infrastructure and sustainability on the tourism industry. Accessed April 12, 2019, https:/ www.hospitalitynet.org/news/4082427.html.

Gronroos C (1990)¨ Service Management and Marketing: Managing the Moments of Truth in Service Competition (Jossey-Bass, San Francisco).

Gu B, Park J, Konana P (2012) The impact of external word-of-mouth sources on retailer sales of high-involvement products. Inform. Systems Res. 23(1):182–196.

Guo Y, Barnes SJ, Jia Q (2017) Mining meaning from online ratings and reviews: Tourist satisfaction analysis using latent Dirichlet allocation. Tourism Management 59:467–483.

Gutt D, Herrmann P, Rahman MS (2019) Crowd-driven competitive intelligence: Understanding the relationship between local market competition and online rating distributions. Inform. Sys tems Res. 30(3):980–994.

Haykin S (1994) Neural Networks: A Comprehensive Foundation (Prentice Hall PTR, Upper Saddle River, NJ).

Ho Y-C, Wu J, Tan Y (2017) Disconfirmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642.

Hong Y, Huang N, Burtch G, Li C (2016) Culture, conformity, and emotional suppression in online reviews. J. Assoc. Inform. System 17(11):2.

Hu N, Koh NS, Reddy SK (2014) Ratings lead you to the product, reviews help you clinch it? The mediating role of online review sentiments on product sales. Decision Support Systems 57:42–53.

Hu N, Pavlou PA, Zhang J (2017) On self-selection biases in online product reviews. Management Inform. Systems Q. 41(2):449–471.

Huang N, Burtch G, Hong Y, Polman E (2016) Effects of multiple psychological distances on construal and consumer evaluation: A field study of online reviews. J. Consumer Psych. 26(4):474–482.

Huber VL, Neale MA, Nofthcraft GB (1987) Judgment by heuristics: Effects of ratee and rater characteristics and performance standards on performance-related judgments. Organ. Behav. Human Decision Processes 40(2):149-169.

Jabr W, Zheng E (2014) Know yourself and know your enemy: An analysis of firm recommendations and consumer reviews in a competitive environment. Management Inform. Systems Quart. 38(3):635–654.

Jenks GF (1967) The data model concept in statistical mapping. Internat. Yearbook Cartography 7:186–190.

Jiang Y, Guo H (2015) Design of consumer review systems and product pricing. Inform. Systems Res. 26(4):714–730.

Joachims T (2002) Optimizing search engines using clickthrough data Proc. 8th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 133–142.

Khern-am nuai W, Kannan K, Ghasemkhani H (2018) Extrinsic vs. intrinsic rewards for contributing reviews in an online platform Inform. Systems Res. 29(4):779–1068.

Kim H, Stepchenkova S (2015) Effect of tourist photographs on attitudes toward destination: Manifest and latent content. Tourism Management 49:29–41.

Koh NS, Hu N, Clemons EK (2010) Do online reviews reflect a product’s true perceived quality? An investigation of online movie reviews across cultures. Electron. Commerce Res. Appl. 9(5): 374–385.

Kokkodis M (2012) Learning from positive and unlabeled amazon reviews: Toward identifying trustworthy reviewers. Internat. Conf. World Wide Web (ACM, New York), 545–546.

Kokkodis M (2019) Reputation deflation through dynamic expertise assessment in online labor markets. World Wide Web Conf. (ACM New York), 896–905.

Kokkodis M, Ipeirotis PG (2013) Have you done anything like that? Predicting performance using inter-category reputation. Internat. Conf. Web Search Data Mining (ACM, New York), 435–444.

Kokkodis M, Ipeirotis PG (2016) Reputation transferability in online labor markets. Management Sci. 62(6):1687–1706.

Kokkodis M, Lappas T (2016) The relationship between disclosing purchase information and reputation systems in electronic markets. Proc. AIS Internat. Conf. Inform. Systems (ICIS), Dublin, Ireland.

Kokkodis M, Lappas T, Kane G (2019) Direct and indirect benefits of introducing purchase verification in e-commerce platforms: Evidence from a natural experiment. Working paper, Boston College, Boston.

Kravitz DA, Balzer WK (1992) Context effects in performance appraisal: A methodological critique and empirical study. J. Appl. Psychol. 77(1):24–31.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110

Lappas T (2012) Fake reviews: The malicious perspective. Bouma G, Ittoo A, Métais E, Wortmann H, eds. Natural Language Processing and Information Systems, Lecture Notes in Computer Science, vol. 7337 (Springer, Berlin, Heidelberg), 23–34

Lappas T, Sabnis G, Valkanas G (2016) The impact of fake reviews on online visibility: A vulnerability assessment of the hotel indus try. Inform. Systems Res. 27(4):940–961.

LaTour SA, Peat NC (1979) Conceptual and methodological issues in consumer satisfaction research. Adv. Consumer Res. 6:431–437.

Le Q, Mikolov T (2014) Distributed representations of sentences and documents. Proc. 31st Internat. Conf. Machine Learn., Proceedings of Machine Learning Research, vol. 32 (PMLR), 1188–1196.

Lee Y-J, Hosanagar K, Tan Y (2015) Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Sci. 61(9):2241–2258.

Li H, Zhang Z, Meng F, Janakiraman R (2017) Is peer evaluation of consumer online reviews socially embedded? An examination combining reviewer’s social network and social identity. Internat. J. Hospitality Management 67:143–153.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Litvin SW, Goldsmith RE, Pan B (2008) Electronic word-of-mouth in hospitality and tourism management. Tourism Management 29(3): 458–468.

LIWC (2018) Linguistic Inquiry and Word Count. Accessed July 30, 2018, http://liwc.wpengine.com

Lu X, Ba S, Huang L, Feng Y (2013) Promotional marketing or wordof-mouth? Evidence from online restaurant reviews. Inform. Systems Res. 24(3):596–612.

Luca M (2018) Reviews, reputation, and revenue: The case of Yelp.com. Working paper, Harvard Business School, Boston.

Maynard D, Funk A (2011) Automatic detection of political opinions in tweets. Proc. 8th Extended Semantic Web Conf. Semantic Web: Res. Appl. (ESWC'11), 88–99.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Moe WW, Trusov M (2011) The value of social dynamics in online product ratings forums. J. Marketing Res. 48(3):444–456.

Mudambi SM, Schuff D, Zhang Z (2014) Why aren’t the stars aligned? An analysis of online review content and star ratings. Proc. 47th Hawaii Internat. Conf. System Sci. (IEEE, Piscataway, NJ), 3139–3147.

Murphy KR, Balzer WK, Lockhart MC, Eisenman EJ (1985) Effects of previous performance on evaluations of present performance. J. Appl. Psych. 70(1):72–84.

Murphy KR, Cleveland JN (1995) Understanding Performance Ap praisal: Social, Organizational, and Goal-Based Perspectives (Sage, Thousand Oaks, CA).

Naik N, Kominers SD, Raskar R, Glaeser EL, Hidalgo CA (2015) Do people shape cities, or do cities shape people? The co-evolution of physical, social, and economic change in five major US cities. NBER Working Paper No. 21620, National Bureau of Economic Research, Cambridge, MA.

Neumann J, Gutt D, Kundisch D (2017) The traveling reviewer problem: Exploring the relationship between offline locations and online rating behavior. Proc. Internat. Conf. Inform. Systems, Seoul, South Korea.

Pan B (2015) The power of search engine ranking for tourist desti nations. Tourism Management 47:79–87.

Pan B, Hembrooke H, Joachims T, Lorigo L, Gay G, Granka L (2007) In Google we trust: Users decisions on rank, position, and relevance. J. Comput. Mediated Comm. 12(3):801–823.

Park N, Peterson C (2010) Does it matter where we live? The urban psychology of character strengths. Amer. Psych. 65(6):535.

Park S, Yang Y, Wang M (2019) Travel distance and hotel service satisfaction: An inverted u-shaped relationship. Internat. J. Hospitality Management 76:261–270.

Perry F (2018) How does place shape who we are? Thinking City (July 24), https://thinkingcity.org/2018/07/24/how-does-place -shape-who-we-are/.

Phelps A (1986) Holiday destination image–the problem of assessment: An example developed in Menorca. Tourism Management 7(3):168–180.

Pike S (2002) Destination image analysis: A review of 142 papers from 1973 to 2000. Tourism Management 23(5):541–549.

Prayag G, Ryan C (2012) Antecedents of tourists’ loyalty to Mauritius: The role and influence of destination image, place attachment, personal involvement, and satisfaction. J. Travel Res. 51(3): 342–356.

Ramseook-Munhurrun P, Seebaluck VN, Naidoo P (2015) Examining the structural relationships of destination image, perceived value, tourist satisfaction and loyalty: case of Mauritius. Procedia Soc. Behav, Sci, 175(12):252–259.

Rosenblatt M (1956) Remarks on some nonparametric estimates of a density function. Ann. Math. Statist. 27(3):832–837.

Roshan SN, Mahmoudi Maymand M, Jowkar A, Karimi O (2017) Interactions between nation branding and corporate branding. J. Fundamental Appl. Sci. 9(1S):842–852.

Shen F (2014) Perceived fit and deal framing: The moderating effect of perceived fit on sales promotions in line and brand extensions. J. Product Brand Management 23(4/5):295–303.

Silberberg T (1995) Cultural tourism and business opportunities fo museums and heritage sites. Tourism Management 16(5):361–365.

Soups R (2015) Yelp data set challenge is doubling up! (Yelp Engi neering Blog) Accessed July 12, 2018, https://engineeringblog .yelp.com/2015/02/yelp-dataset-challenge-is-doubling-up.html.

Sridhar S, Srinivasan R (2012) Social influence effects in online product ratings. J. Marketing 76(5):70–88.

Stepchenkova S, Mills JE (2010) Destination image: A meta-analysis of 2000–2007 research. J. Hospitality Marketing Management 19(6): 575–609.

Suh E, West JJ (2010) Estimating the impact of entertainment on the restaurant revenues of a Las Vegas hotel casino: An exploratory study. Internat. J. Hospitality Management 29(4):570–575.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Tasci ADA, Gartner WC, Tamer Cavusgil S (2007) Conceptualization and operationalization of destination image. J. Hospitality Tourism Res. 31:194–223.

Teas, R Kenneth. (1993) Expectations, performance evaluation, and consumers’ perceptions of quality. J. Marketing 57(4):18–34.

Terzi M, Ferrario M-A, Whittle J (2011) Free text in user reviews: Their role in recommender systems. Proc. 5th ACM Internat. Conf. Recommender Systems (ACM, New York), 45–48.

Thibaut JW (2017) The Social Psychology of Groups. (Routledge, New York).

TripAdvisor (2018) Better data means better business decisions. Accessed December 11, 2019, https://www.tripadvisor.com BusinessAdvantage#/analytics?\_k=y2uaon

Tsang A, Prendergast G (2009) Is a “star” worth a thousand words? The interplay between product-review texts and rating valences. Eur. J. Marketing 43(11):1269–1280.

Verhagen T, Meents S, Tan Y-H (2006) Perceived risk and trust associated with purchasing at electronic marketplaces. Eur. J. Inform. Systems 15(6):542–555.

Vermeulen IE, Seegers D (2009) Tried and tested: The impact of online hotel reviews on consumer consideration. Tourism Man agement 30(1):123–127.

Wang A, Zhang M, Hann I-H (2018) Socially nudged: A quasi experimental study of friends’ social influence in online prod uct ratings. Inform. Systems Res. 29(3):525–777.

Wang X, Zhang J, Gu C, Zhen F (2009) Examining antecedents and consequences of tourist satisfaction: A structural modeling ap proach. Tsinghua Sci. Tech. 14(3):397–406.

Wang Y, Pizam A (2011) Destination Marketing and Management: Theories and Applications (CABI, Boston)

Xiang Z, Schwartz Z, Gerdes JH Jr, Uysal M (2015) What can big data and text analytics tell us about hotel guest experi ence and satisfaction? Internat. J. Hospitality Management 44: 120–130.

Ye Q, Law R, Gu B (2009) The impact of online user reviews on hotel room sales. Internat. J. Hospitality Management 28(1):180–182.

Yin D, Bond S, Zhang H (2014) Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. Man agement Inform. Systems Q. 38(2):539–560.

Youngblade R (2012) How a restaurant critic uses Yelp. (The Yelp Blog). Accessed July 12, 2018, https://www.yelpblog.com/2012 12/how-a-restaurant-critic-uses-yelp.

Zhang Z, Ye Q, Law R, Li Y (2010) The impact of e-word-of-mouth on the online popularity of restaurants: A comparison of consume reviews and editor reviews. Internat. J. Hospitality Managemen 29(4):694–700.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
