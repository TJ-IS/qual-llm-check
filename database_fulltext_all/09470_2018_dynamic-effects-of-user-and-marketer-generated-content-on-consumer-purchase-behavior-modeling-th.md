---
otero_id: 9470
otero_key: "REQ4RH9N"
title: "Dynamic effects of user- and marketer-generated content on consumer purchase behavior: Modeling the hierarchical structure of social media websites"
authors: "Michael Scholz; Joachim Schnurbus; Harry Haupt; Verena Dorner; Andrea Landherr; Florian Probst"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.07.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Dynamic Effects of User- and Marketer-Generated Content on Consumer Purchase Behavior: Modeling the Hierarchical Structure of Social Media Websites

Michael Scholz, Joachim Schnurbus, Harry Haupt, Verena Dorner, Andrea Landherr, Florian Probst

![](/api/attachments/REQ4RH9N/fulltext/images/27403f1497d1998662a06de8a329f94471e3a73723feaabe932c9377ed7d34b2.jpg)

PII: S0167-9236(18)30110-6

DOI: doi:10.1016/j.dss.2018.07.001

Reference:

DECSUP 12971

To appear in: Decision Support Systems

Received date: 15 March 2018

Revised date: 8 July 2018

Accepted date: 10 July 2018

Please cite this article as: Michael Scholz, Joachim Schnurbus, Harry Haupt, Verena Dorner, Andrea Landherr, Florian Probst , Dynamic Effects of User- and Marketer-Generated Content on Consumer Purchase Behavior: Modeling the Hierarchical Structure of Social Media Websites. Decsup (2018), doi:10.1016/j.dss.2018.07.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Dynamic Efects of User- and Marketer-Generated Content on Consumer Purchase Behavior: Modeling the Hierarchical Structure of Social Media Websites

Michael Scholz<sup>a,∗</sup>, Joachim Schnurbus<sup>a</sup>, Harry Haupt<sup>a</sup>, Verena Dorner<sup>b</sup>, Andrea Landherr<sup>c</sup>, Florian Probst<sup>c</sup>

<sup>a</sup>Faculty of Business Administration, University of Passau, Passau, Germany <sup>b</sup>Faculty of Business Administration and Economics, Karlsruhe Institute of Technology, Karlsruhe, Germany <sup>c</sup>FIM Research Center, University of Augsburg, Augsburg, Germany

## Abstract

User- and marketer-generated content items on social media platforms are supposed to have an impact on economic target variables, such as variables measuring consumers’ purchase behavior. The position of each content item – and thus the impact on economic variables – changes with newly appearing items. We propose a hierarchy score to capture the dynamics of the content items on social media platforms. In order to mimic the reduced visibility of earlier content items, our hierarchy score computes the position of content items based on the number of text line equivalents of content items above a particular item. Employing the proposed hierarchy score in a dynamic regression framework for data of a large online store yields improved estimates and predictions compared to a variety of other models.

Keywords: social media, user-generated content, marketer-generated content, content hierarchy, dynamic regression

## 1. Introduction

Social media platforms have become very popular for individual users but also for companies in recent years, ofering companies special services for social media marketing. Companies can, for example, set up business fanpages on social media platforms in order to foster their communication with customers and to implement social media marketing campaigns. Other social media platforms provide information about “hot deals” and companies can use these websites to announce their price promotion campaigns. According to Statista (2016), approximately 90% of online retailers worldwide used social media marketing in 2016 and 41% of them believed that social media marketing was the most efective marketing strategy.

Recent research has investigated the efect of content items on several economic variables, such as sales, an online store’s conversion rate, or the rate of product returns (e.g., Duan et al., 2008a; Trusov et al., 2009; Sonnier et al., 2011; Albuquerque et al., 2012; Goh et al., 2013; Scholz et al., 2013; Kumar et al., 2016; Minnema et al., 2016). Direction and size of this efect might depend on the content, the sentiment, as well as the creator of the content. This efect might be, however, influenced by the efort consumers must invest in order to become aware of a particular content item. The more content items are listed above a particular item, and thus the more efort a consumer must invest to scroll down to a particular item, the less pronounced might be the efect of this item on economic variables. Each content item will be initially positioned at the top of the hierarchy of content items but will change its position as soon as other items will be submitted. Thus, the position of content items should be taken into account when estimating the efect of content items on economic variables. A content item with an extensive price promotion might have a very diferent efect on an online store’s revenue when this item remains on the top position for a very long time versus it gets displaced immediately by several other items. Furthermore, a new content item that is submitted to a social media platform reduces the position of other items in this hierarchy. Estimating the efect of a particular content item or a category of items (e.g., price promotion) on economic variables is hence challenging. Deciding when to create the next content item in what length is finally also impossible without a valid estimation of the efect of content items on economic variables. Recent research has either ignored the position of a content item (Scholz et al., 2013) or approximated it by the item’s timestamp (Meire et al., 2016).

We propose to model the efect of a content item’s position in the hierarchy of all content items on a social media platform. We therefore develop a hierarchy score that transforms the size of posts in text line equivalents and calculates the average number of text lines above any particular content item at a day. This value is then transformed into a standardized and easily interpretable variable expressing the chance that an average consumer will consider the content item. Our proposed hierarchy score can be applied to capture the dynamics of social media platforms as it allows to investigate the efects of marketer-generated content (MGC) and user-generated content (UGC) on economic variables on an aggregated level. Our study hence complements existing research (e.g., Trusov et al., 2009; Albuquerque et al., 2012; Goh et al., 2013;

Scholz et al., 2013) by providing a method to i) estimate the short- and long-run efects of MGC and UGC with regard to the dynamic changes on social media platforms, ii) supporting marketing managers’ decision about when to create what kind of content item in what length, and iii) predicting economic variables based on diferent strategies for publishing MGC.

With an empirical evaluation on social media data for a period of 280 days from a large German online store, we demonstrate how our proposed hierarchy score can be used to estimate and predict the impact of several MGC and UGC characteristics on economic variables. An important aspect of our empirical illustration is that the hierarchy score clearly contributes to the explanation and short-term predictability of a store’s conversion rate (as economic variable in our empirical investigation).

The remainder of this article is organized as follows. In the next section, we review related work and show how this study contributes to existing studies. We develop our hierarchy score based on the methodological issues of social media platform dynamics in Section 3. We employ our hierarchy score in Section 4 to investigate the efects of MGC and UGC on a large German retailer’s online store conversion rate. The results of this analysis are presented in Section 5. In Section 5, we furthermore demonstrate how our proposed hierarchy score can be used to support companies’ decision about when and in what length to post information on social media platforms. In Section 6 we provide a robustness check, while we discuss our findings with respect to existing studies and give a summary of the implications of our study for researchers as well as practitioners in Section 7.

## 2. Related Literature

Recent research has investigated the efects of MGC and several types of UGC on economic variables. Kumar et al. (2016), for example, provide evidence that MGC positively influence a consumer’s purchase decision, especially in the case of an experienced consumer. Goh et al. (2013) demonstrate that UGC has a stronger impact on consumers’ purchase decision processes than MGC. However, the impact of both, UGC and MGC, and hence the ratio between these impacts on purchase decision processes, can vary significantly over time. According to Chevalier and Mayzlin (2006); Duan et al. (2008b); Forman et al. (2008); Zhu and Zhang (2010), the number of customer reviews (as one type of UGC) positively influences sales. Jang et al. (2012) show that customer reviews are more important for the formation of a consideration set than for the final choice of a consumer. Customer reviews directly influence a consumer’s purchase probability and thus finally a retailer’s conversion rate (Ludwig et al., 2013). Social media posts as another type of UGC have been found to afect sales in a similar way than customer reviews – positive posts lead to an increase in sales, consumers purchase expenditure, and firm value (e.g., Sonnier et al., 2011; Goh et al., 2013). Rosario et al. (2016) provide a meta analysis of 96 studies on the efect of UGC on sales and conclude that UGC has a positive influence on sales and that the UGC-volume is more important (for sales) than the UGC-valence. Lee et al. (2018) show that the content of Facebook posts has an influence on user engagement. Brand personality-related content positively influences user engagement whereas informative content negatively influences engagement. A user’s engagement on a company’s Facebook fanpage can be interpreted as the user’s loyalty to the company and might be positively correlated to the user’s propensity to convert to a purchaser.

An investigation of the efect of MGC and UGC on sales is subject to two statistical challenges. First, the causal relationship between purchase decisions and the creation of UGC and MGC for that product is supposed to be simultaneous. Second, the set of MGC and UGC available for a product (and thus the visibility of each existing post) dynamically changes and so does the efect of each content item on sales.

The first challenge, mutual causality between economic variables and social media posts, is inherent to some degree in online purchase processes (Duan et al., 2008b): The more consumers buy a particular product, the more are prepared to create UGC. The more UGC’s are available, the more consumers might be attracted to ultimately buy the product. This challenge has been largely addressed in recent research Forman et al. (2008), for instance, use the diference in the number of reviews from month t−1 to month t as an explanatory variable for sales. Ho-Dac et al. (2013) use time-demeaned values of their explanatory UGC variables as instruments. Several studies tackle this issue by using lags of UGC- and/or MGC-covariates in a regression framework (e.g., Godes and Mayzlin, 2009; Zhu and Zhang, 2010; Goh et al., 2013). We estimate autoregressive distributed lag models containing both, lags of the dependent variable and of the regressors, hence providing natural instruments for potentially endogenous covariates.

The second challenge, dynamic changes of the hierarchy of content items, arises due to the submission of new posts. New posts will be positioned above older posts and thus dynamically change the hierarchy of posts on a social media platform. These dynamic changes afect the efort (in terms of scrolling down) consumers need to invest in order to read and recognize older posts. The higher the efort a consumer must invest to recognize and consider a particular post, the less is this post’s chance of being considered by an average consumer and the less is also this post’s efect on economic variables. Recent research has largely ignored these dynamic changes (Albuquerque et al., 2012; Scholz et al., 2013). Lee et al. (2018) propose a strategy for investigating the efect of content items that are generated by Facebook’s targeting algorithm EdgeRank. However, they do not control for hierarchy efects of MGC and UGC. Because individual interactions with MGC and UGC are usually latent, our strategy explicitly takes into account the hierarchy of all posts and thus the dynamics of a social media platform. We calculate MGC and UGC covariates with regard to the dynamic changes during a day and use them to explain and predict the daily changes of an economic variable. In the next section, we introduce a hierarchy score that captures the dynamic changes of content items on social media platforms.

## 3. Developing a Hierarchy Score

Content items on a social media platform can either be in form of an initial post or a follow-up comment. The impact a particular content item has on consumers’ purchase decision processes is likely to depend on the position of this content item in the hierarchy of content items on a social media platform. Figure 1 shows an edited screenshot of a fictive social media platform. Yesterday, the retailer Cambrio announced a prize draw. The efect of this content item (i.e., post) on consumers changes with each new post that is published above. The lower the prize draw post is positioned in the hierarchy of posts, the less likely it will be that consumers will recognize this post, hence decreasing the impact of this post on consumers’ purchase decision processes.

The rate at which posts are published on a social media platform is not constant over time. Hence, considering only those posts which have been published during the most recent time interval (e.g., during the last day) does not seem to be a meaningful solution. Some posts might be on the top position for just a few minutes whereas others will be on top of the hierarchy for days. We propose a score H that measures post p’s average position at day t in the hierarchy of posts on a social media platform. The average position per day is finally transformed into a score that expresses a post’s chance to be considered by a consumer. All variables used for computing the score are shown in Table 1.

Posts are typically ordered by their creation date on a social media platform (Meire et al., 2016). Creation date as well as the size of posts<sup>1</sup> newer than post p determine p’s position in the hierarchy of posts. Some social media platforms ofer push mechanisms that can be configured to actively push individually filtered content items to users. The economic impacts of pushed content items thus does not depend on the hierarchy of items on the social media platform. However, those users who visit the social media website

# ACCEPTED MANUSCRIPT

<table><tr><td colspan="2"><img src="/api/attachments/REQ4RH9N/fulltext/images/fe2cb3aed49a176c5c33d61c71e674caa41d5614d5014b0ad7aa39adad67d310.jpg"/> HannaTodayI recently order some clothers at RustyCage.com and was amazed to find a small gift in the package. Thanks! Post 1</td></tr><tr><td colspan="2">[RXY4C] RustyCageYesterdayWe are pleased to celebrate our online store&#x27;s 10th birthday with you.Visit our store today and save up to 50%. [70W7] SeppTodayWow!!! Let&#x27;s celebrate. Post 2</td></tr><tr><td colspan="2"><img src="/api/attachments/REQ4RH9N/fulltext/images/f59bbc1ac3d6484d72f47eb772fb605388aead4f07dd402b4152e1c1922276f7.jpg"/> Cambrio2 Days AgoYour views are very important to us. Fill in our survey and you will be entered into our prize draw. <img src="/api/attachments/REQ4RH9N/fulltext/images/3ccaa7e515966177d115355c90cd29ba22a11be45b5214e2d5948351dbae97ec.jpg"/> Post 3</td></tr><tr><td colspan="2"><img src="/api/attachments/REQ4RH9N/fulltext/images/771bd4a0eb5390d072ab3be572e344982be5e509922455dba25978bba4d87d05.jpg"/> PalTodayGod, damn, a blank ... [770T] AliceYesterdayWow, I got it. I indeed have won $100.</td></tr></table>

Figure 1: Hierarchy of contents on a social media platform.

will be especially influenced by content items being on top of the hierarchy. Furthermore, various social media platforms ofer the possibility of a push mechanism that sends out a weekly or daily email with the most recent content items in a chronological order (e.g., hotukdeals.com, mydealz.com). The position of a content item in the hierarchy of items in one email thus might moderate the economic efect of the content items.

We compute the hierarchy score $H _ { p , t }$ of post p at day t based on the average number of text lines $\Lambda _ { p , t }$ above post $p$ for the time this post was available online at day t. Note that the size of all components of a post (e.g., headings, pictures, text, footers) is measured in an equivalent number of text lines. The average number of text lines $\Lambda _ { p , t }$ above p at t is transformed into a hierarchy score by (i) calculating the efort for an average consumer to scroll down to p and (ii) weighting $\Lambda _ { p , t }$ by the time (in seconds) $S _ { p , t }$ with

Table 1: List of Variables

<table><tr><td>Symbol</td><td>Description</td></tr><tr><td> $p$ </td><td>Post</td></tr><tr><td> $t$ </td><td>Day</td></tr><tr><td> $e$ </td><td>Event</td></tr><tr><td> $s_e$ </td><td>Second in which event  $e$  occurs</td></tr><tr><td> $M$ </td><td>Average number of text lines visible on a social media platform before scrolling down</td></tr><tr><td> $\lambda_{p,s_e}$ </td><td>Number of lines above post  $p$  at the time event  $e$  occurs</td></tr><tr><td> $\Lambda_{p,t}$ </td><td>Average number of lines above post  $p$  for the time  $p$  was available online at day  $t$ </td></tr><tr><td> $S_{p,t}$ </td><td>Total time in seconds post  $p$  was available on the social media platform at day  $t$ </td></tr><tr><td> $H_{p,t}$ </td><td>Hierarchy score for post  $p$  at day  $t$ </td></tr></table>

$S _ { p , t } \in [ 0 ; 8 6 , 4 0 0 ]$ post $p$ was available at day t. The position score is finally computed by the equation

$$
H _ {p, t} = \left(\frac {S _ {p , t}}{8 6 , 4 0 0}\right) \left(\frac {1}{1 + \frac {\Lambda_ {p , t}}{M}}\right).\tag{1}
$$

We assume that a consumer sees on average M text lines from the content on a social media platform In order to view further content items, the consumer must invest efort and scroll down. The second term of Equation (1) calculates the efort for scrolling down to $p$ as a value in [0; 1] where 1 expresses no and 0 $p$

Post $p \mathrm { ^ { \circ } s }$ position depends on the number of posts that are above $p$ and the size of the above listed posts. We propose calculating the average number of text lines $\Lambda _ { p , t }$ above $p$ as weighted average of the number of lines of the subsequent posts (with respect to $p )$ between two events on day t. There are five event types relevant for computing the average number of text lines above a post $p$ on day t: new posts, new comments, updated posts, updated comments and start/end of a day. We use the time (in seconds) between two events to weigh the number of text lines above a post $p$ between the two events. Until event e there are $I _ { e - 1 }$ posts on a website. The posts are enumerated according to their creation date. We use the sum of all posts that are (i) available before event e occurs and (ii) having a higher number than post $p$ to compute the number of lines above $p .$ The average number of text lines above $p$ at t is finally calculated in three steps as

$$
\Lambda_ {p, t} = \left\{ \begin{array}{l l} \underbrace {\frac {1}{S _ {p , t}} \sum_ {e = 2} ^ {E _ {t}} \left[ (s _ {e} - s _ {e - 1}) \underbrace {\sum_ {i = p + 1} ^ {I _ {e - 1}} \lambda_ {i , s _ {e - 1}}} _ {\text {   Step   1   }} \right]} _ {\text {   Step   2   }} & \text {   if   } S _ {p, t} > 0, \\ 0 & \text {   otherwise.   } \end{array} \right.\tag{2}
$$

Step 1 calculates the total number of lines above post $p$ in second s<sub>e−1</sub> (i.e., the time the last event occurred). The number of lines of each post i being above $p$ immediately after $s _ { e - 1 }$ is given by $\lambda _ { i , s _ { e - 1 } }$ . Step 2 weighs the total number of lines computed in Step 1 by the time diference between the previous event $e - 1$ and the current event e. Step 3 finally computes the average number of lines above a post p with respect to all events occurring on day t. Note that $\Lambda _ { p , t }$ expresses the average number of lines above $p$ for the time p was available online at t. Equation (1) thus multiplies the scrolling efort (as $\Lambda _ { p , t } )$ by the share of a day (i.e., 86,400 seconds) $p$ was available online. A numerical example for calculating $\Lambda _ { p , t }$ and $H _ { p , t }$ is presented in the Appendix.

## 4. Data Structure, Variable Construction, and Statistical Model

We test our proposed hierarchy score on empirical data from a large German online retailer and the social media platform Facebook. More specifically, we use the hierarchy score to model and estimate the efect posts on the Facebook fanpage of this retailer have on the conversion rate of the retailer’s online store<sup>2</sup>.

## 4.1. Data

We employ data provided by a large German retailer for books, movies, music, and computer games. products. The company has a strong presence on its Facebook fanpage, which is its only marketing channel; no marketing instruments other than MGC on its fanpage were used. The retailer provided us with its online store statistics for customers who accessed the store through its fanpage between May 16th 2011 and February 19th 2012 (280 days). Data (on a daily basis) included the number of fanpage users that visited the online store (visitors), the daily number of likes, and the conversion rate of those visitors defined as the number of purchasers divided by the number of visitors (see Figure 2).

![](/api/attachments/REQ4RH9N/fulltext/images/806e0c8b82165d886e18fd02d6d453f77ecdb99333460f029288496d83eb36c5.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/02ad9c05fb9f7ea29f34b22e8ed51adf9c2ee114353a0be82eb76755fd6bbc49.jpg)  
Figure 2: Time series of the number of visitors and the conversion rate.

We also accessed the internal fanpage statistics, including data on the number of unique active users on a daily basis. We extracted MGC (wall posts and comments) and UGC (wall posts and comments) from the fanpage, collecting 485 MGC items and 302 UGC items. A content item has been listed on position 1 in the hierarchy of content items for on average 30,470 seconds. However, the minimal time a content item has been listed on the top position was only 3 seconds whereas the maximal time was 267,770 seconds (approx. 3 days). Both, MGC and UGC, were sorted into categories depending on their content and were assigned to one of three sentiment categories (i.e., positive, neutral, or negative). We describe the post categories and the assignment process in the next subsection.

## 4.2. Post Categories and Sentiment

Post categories describe the content of posts. We sorted each MGC and UGC item into one or multiple of the content categories given in Table 2. An MGC post is on average assigned to 1.19 categories and an UGC post is assigned to 1.20 categories on average.

Table 2: Observed number of posts for five MGC and UGC post categories.

<table><tr><td>Category</td><td>Description</td><td>Example</td><td># MGC</td><td># UGC</td></tr><tr><td>Price Promotion</td><td>Discounts, special deals and other posts that focus on product price</td><td>Good morning dear fans, our current deal – the Simvalley Dual Sim Smartphone with GPS Android 2.2 for only 99,99 Euros or 23% price savings – runs just under one hour.</td><td>47</td><td>9</td></tr><tr><td>Product Promotion</td><td>Announcement of new products and other posts that focus on exactly one product</td><td>Dear Twilight fans, we are pleased to offer you &quot;The Official Illustrated Guide&quot; from Stephenie Meyer.</td><td>113</td><td>130</td></tr><tr><td>Indirect Promotion</td><td>Indirect promotion of products or product categories</td><td>Attention Twilight fans: Are you a vampire, werewolf or human;-)? Take part in our personality test and find out.</td><td>131</td><td>24</td></tr><tr><td>Socializing</td><td>Community-centric posts that do not promote products or prices</td><td>Many of you are very enthusiastic about reading. But, have you ever written, for example, a story or poems, etc.? And if so on the same topics that you like to read?</td><td>272</td><td>84</td></tr><tr><td>Feedback</td><td>Questions, critical and positive feedback and acknowledgments</td><td>Hi, I have a question about the shipping. How many days does it take before I can read my ordered book?</td><td>13</td><td>115</td></tr></table>

Sentiment describes the overall opinion of a content item. Since MGC is generally neutral (Rishika et al., 2013), we did not classify it by sentiment. UGC items were classified as positive, negative, or neutral in sentiment. For classifying UGC sentiment, we used a manual rather than an automated classification, due to the limitations of text mining algorithms in correctly processing textual features like slang, irony, or sarcasm (Stieglitz and Kruger, 2011).¨

Category and sentiment classification was carried out by a team of undergraduate students who were all familiar with Facebook. A common understanding of the classification criteria was obtained by giving the students a short tutorial explaining the criteria (as suggested by Garc´ıa-Crespo et al., 2010; Laros and Steenkamp, 2005). As proposed in prior coding studies (Liu, 2006), each item was classified by at least three diferent students. We may assume reasonably high validity for our classification: for large numbers of items, even classification by only one person yields good results (Chelaru et al., 2012). Items were

# ACCEPTED MANUSCRIPT

considered as successfully classified when all three students agreed on the same categories. If they did not, other students re-classified the items until a common set of categories led by at least three votes. In the next subsection, we explain the specific application of the hierarchy score for the collected data.

## 4.3. Calculation of the Hierarchy Score

We compute post p’s position in the hierarchy of posts based on the number of text lines of all posts above p at time t as described in Section 3. All components of a post are therefore converted into text line equivalents. Each post consists of four components – header, body, footer, and comments (optional) (see Figure 3). Header and footer have a static size and are approximately as large as 4 lines of text in the body. A text line in the body has a size of $6 0 0 \times 2 4$ pixels and consists on average of $1 2 \mathrm { w o r d s } ^ { 3 }$ . Comments have a body and a footer if there are more than two comments. The footer is approximately 1 text line. A text line of a comment also consists of 12 words on average and takes $2 / 3$ of the height of a text line in the post body (i.e., 16 pixels). We furthermore assume that a typical graphical device at the time of our data displays about M = 50 text lines simultaneously. We computed the size of posts and finally the hierarchy score based on these assumptions. Our hierarchy score can be applied to other social media platforms by simply adapting the size values.

![](/api/attachments/REQ4RH9N/fulltext/images/b2ce96676d2f3fa6bb5ab57591c96672622a3b4be322f7728fa5e64945fd7691.jpg)  
Figure 3: Components of a Facebook post.

The resulting distribution of the calculated hierarchy scores for each post and each day is depicted in Figure 4. The hierarchy score rather follows a triangular distribution because the hierarchy score for a particular post p decreases over time when more and more posts will be published at the top of the hierarchy Thus, there is a large amount of hierarchy score value that are rather small (produced by the posts at the end of the hierarchy) and a large amount of rather high hierarchy scores (produced by the posts on top positions at a particular day).

![](/api/attachments/REQ4RH9N/fulltext/images/a76f407185c9754e57b873845c2ec8a44d5e56f32817f695d2429fc25c1c1132.jpg)  
Figure 4: Distribution of the Hierarchy Score.

## 4.4. Category-based Hierarchy Scores

Hierarchy scores are aggregated per content category c to estimate category-specific efects. Since a post might belong to more than one category, we divide a post’s hierarchy score by the number of categories the post belongs to. Finally, these weighted hierarchy scores are summarized to get the category-specific hierarchy score $H _ { c , t }$ with

$$
H _ {c, t} = \sum_ {p \in c} \frac {H _ {p , t}}{\# c _ {p , t}},\tag{3}
$$

where $\# c _ { p , t }$ denotes the number of categories to which a particular post $p$ belongs to on day t. We standardize the hierarchy score according to

$$
z _ {c, t} = \frac {H _ {c , t}}{\sum_ {c} H _ {c , t}} 1 0 0,\tag{4}
$$

such that $0 \leq z _ { c , t } \leq 1 0 0$ for every c and all t. In this form, $z _ { c , t }$ has the straightforward interpretation of being the percentage of post visibility of category c on day t w.r.t. all user- and marketer-generated posts up to day t.

## 4.5. Statistical Model

The regression estimation framework we use in this paper are autoregressive distributed lag (ARDL) models (e.g., Hendry, 1984; Pesaran and Shin, 1999; Stock and Watson, 2012). Due to the common social media platform hierarchy, some of the category covariates are highly dependent and have a high persistence (i.e., unit roots). As none of the variables has unit roots of a higher order, we use a model formulation in first diferences under the assumption that the latter are weakly stationary. In our application, we assume that the data generating process is nested in the general ARDL(7,7) model

$$
\Delta y _ {t} = \mu_ {0} + \sum_ {j = 1} ^ {7} \alpha_ {j} \cdot \Delta y _ {t - j} + \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {7} \beta_ {k, l} \cdot \Delta x _ {k, t - l} + \sum_ {c = 1} ^ {C} \sum_ {h = 1} ^ {7} \gamma_ {c, h} \cdot \Delta z _ {c, t - h} + \varepsilon_ {t},\tag{5}
$$

implying a dynamically complete specification based on the assumption

$$
E [ \varepsilon_ {t} | \mathcal {F} _ {t - 1} ] = 0,\tag{6}
$$

where $\mathcal { F } _ { t - 1 } = \{ \Delta y _ { t - 1 } , \Delta y _ { t - 2 } , \hdots , \Delta x _ { t - 1 } , \Delta x _ { t - 2 } , \hdots , \Delta z _ { t - 1 } , \Delta z _ { t - 2 } , \hdots \}$ , and j, l, and h denote the indexes of the lags of the endogenous, K non-post-related, and $C$ post-related regressors, respectively.

Model (5) is a predictive regression allowing to calculate one-step out-of-sample predictions

$$
\widehat {\Delta y} _ {T + 1 | T} = \widehat {\mu_ {0}} + \sum_ {j = 1} ^ {7} \widehat {\alpha} _ {j} \cdot \Delta y _ {T + 1 - j} + \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {7} \widehat {\beta} _ {k, l} \cdot \Delta x _ {k, T + 1 - l} + \sum_ {c = 1} ^ {C} \sum_ {h = 1} ^ {7} \widehat {\gamma} _ {c, h} \cdot \Delta z _ {c, T + 1 - h}
$$

based on observed data. Whenever $\Delta y _ { T + 1 | T }$ is a consistent estimator of $E [ \Delta y _ { T + 1 } | \mathcal { F } _ { T } ]$ , assumption (6) implies that $\widehat { \Delta y } _ { T + 1 | T }$ has the smallest estimated one-step root mean squared prediction error (RMSPE) of any prediction based on $\mathcal { F } _ { T }$

$$
R M S P E = \sqrt {\frac {1}{Q} \sum_ {q = 1} ^ {Q} \left(\Delta y _ {T + q} - \widehat {\Delta y} _ {T + q | T + q - 1}\right) ^ {2}},
$$

and $\Delta y _ { T + q } - \widehat { \Delta y } _ { T + q | T + q - 1 }$ is the one-step prediction error and Q prediction errors are averaged.

The ARDL model (5) can be estimated by ordinary least squares (OLS) and allows for an analysis of dynamic efects of the covariates on the response variable. Note that OLS is consistent under standard assumptions such that all model variables $\Delta y _ { t } , \Delta x _ { t } , \Delta z _ { t }$ , and $\varepsilon _ { t }$ are jointly weakly stationary with absolutely summable autocovariances, and $\scriptstyle \varepsilon _ { t }$ is serially uncorrelated (which is implied by assumption (6)). Note also that endogeneity issues are unlikely to arise in ARDL models as long as the error process $\left\{ \varepsilon _ { t } \right\}$ is serially uncorrelated due to inclusion of lags of regressors and the dependent variable.

# ACCEPTED MANUSCRIPT

The dependent variable $y$ in our model is the online store’s daily conversion rate CVR, and the autoregressive part contains lagged values of CVR. We consider two groups of covariates: First, lags of non-post-related variables. These variables are the number of daily online store visitors (i.e., fanpage users that visited the online store) and the number of daily likes (see Subsection 4.1) captured by the regressors $x _ { k }$ . Second, captured by the regressors $z _ { c } ,$ lags of post-related variables, i.e., the category specific hierarchy scores and lags of sentiment variables (see Subsections 4.2 to 4.4).

The short-run day-to-day efects of covariates $x _ { k }$ and $z _ { c }$ coincide with the estimated parameters ${ \widehat { \beta } } _ { k }$ and $\widehat { \gamma _ { c } }$ , while the cumulated dynamic long-run efects can be determined by

$$
\frac {\sum_ {l = 1} ^ {7} \widehat {\beta} _ {k , l}}{1 - \sum_ {j = 1} ^ {7} \widehat {\alpha} _ {j}} \quad \text { and } \quad \frac {\sum_ {h = 1} ^ {7} \widehat {\gamma} _ {c , h}}{1 - \sum_ {j = 1} ^ {7} \widehat {\alpha} _ {j}}.\tag{7}
$$

The standard errors can be computed by using the Delta method to determine the corresponding estimated variances. Tests of model parameter stability and out-of-sample accuracy are calculated by recursive estimation and one-step-ahead prediction of model (5) using extending sub-samples of the data.

## 5. Descriptives, estimation diagnostics, and results

The empirical illustration starts with a few descriptive details. Table 3 displays Tukey’s five for the response variable CVR, the covariates DailyLikes, Visits (both measured in 1,000 users), and the MGC and UGC covariates defined in Equation (4). We also observe that the range of visibilities (i.e., aggregated standardized hierarchy score per content category) varies considerably across MGC and UGC. Interestingly, Table 2 suggests that the overall number of MGC is clearly higher than that of UGC. With respect to visibility (which will be considered in model M6 in the following subsection) the picture changes dramatically: over the sample period, the overall UGC visibility ranges from around 65 to 75 percent (see also Figure 5).

## 5.1. Model Comparison and Diagnostic Checks

We compare several models ranging from a simple statistical benchmark to the general dynamic model motivated in the previous section: Model M1 is an AR(7)-model for the change in CVR and serves as our baseline for all other models. Model M2 contains in addition to the covariates of M1 the covariate Visits, but no MGC- or UGC-related covariates. Model M3 contains in addition to M1 the hierarchy score in Equation (1), but for the computation of $\Lambda _ { p , t }$ in Equation (2) $\lambda _ { i , t _ { e - 1 } } = 1$ is applied, treating all posts in the hierarchy, as if they had an equal size (equal to a single line of text). Model M4 contains in addition to M2 the number of likes as post-specific covariate, because likes have been found to significantly afect sales in recent research (Lee et al., 2015; Ding et al., 2017). Another approach for the inclusion of post-specific information due to diferent hierarchy score versions is pursued in Models M5 to M7. Model M5 contains in addition to M2 a basic version of the hierarchy score $H _ { p , t }$ being equal to 1 whenever a post exists at day

![](/api/attachments/REQ4RH9N/fulltext/images/116611dd9a134f9b808e294f07a2154852dfa4cbb4309d24c33d76388969e6ca.jpg)  
Figure 5: Percentage of aggregated standardized MGC-/UGC-hierarchy scores over time. Blue shaded area indicates MGC, orange shaded area indicates UGC.

Table 3: Tukey’s five of response CVR, covariate Visits, and the MGC-/UGC-covariates.

<table><tr><td></td><td>Min.</td><td>Q25</td><td>Q50</td><td>Q75</td><td>Max.</td></tr><tr><td>CVR</td><td>0.000</td><td>1.370</td><td>2.025</td><td>2.860</td><td>16.550</td></tr><tr><td>DailyLikes</td><td>0.009</td><td>0.035</td><td>0.049</td><td>0.069</td><td>1.247</td></tr><tr><td>Visits</td><td>0.102</td><td>0.262</td><td>0.336</td><td>0.420</td><td>1.112</td></tr><tr><td>MGC_PricePromotion</td><td>0.154</td><td>0.166</td><td>0.179</td><td>0.375</td><td>0.525</td></tr><tr><td>MGC_ProductPromotion</td><td>4.690</td><td>9.463</td><td>11.811</td><td>14.004</td><td>18.763</td></tr><tr><td>MGC_IndirectPromotion</td><td>1.479</td><td>2.262</td><td>2.691</td><td>3.135</td><td>3.574</td></tr><tr><td>MGC_Socializing</td><td>8.047</td><td>12.997</td><td>16.051</td><td>18.560</td><td>24.685</td></tr><tr><td>MGC_Feedback</td><td>0.029</td><td>0.065</td><td>0.110</td><td>0.141</td><td>0.160</td></tr><tr><td>UGC_PricePromotion</td><td>0.000</td><td>0.008</td><td>0.015</td><td>0.019</td><td>0.024</td></tr><tr><td>UGC_ProductPromotion</td><td>3.940</td><td>7.031</td><td>8.037</td><td>9.560</td><td>14.862</td></tr><tr><td>UGC_IndirectPromotion</td><td>1.931</td><td>2.152</td><td>2.341</td><td>2.555</td><td>3.739</td></tr><tr><td>UGC_Socializing</td><td>32.553</td><td>36.283</td><td>38.693</td><td>41.443</td><td>51.068</td></tr><tr><td>UGC_Feedback</td><td>16.187</td><td>17.870</td><td>19.262</td><td>20.768</td><td>27.405</td></tr></table>

# ACCEPTED MANUSCRIPT

t, otherwise being equal to 0. Basically, this reflects the number of posts. Model M6 contains in addition to M3 the covariate Visits. Model M7 contains in addition to M2 the proposed hierarchy score defined in Equation (4). A summary of all models is presented in Table 4.

Table 4: Description of the models.

<table><tr><td>Model</td><td>Description</td><td>Visits</td><td>Likes</td><td>Number of Posts</td><td>Recency Effect</td><td>Post Size</td></tr><tr><td>M1</td><td>Baseline model</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>M2</td><td>M1 + Visits</td><td>yes</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>M3</td><td>M1 + Recency Effect</td><td>no</td><td>no</td><td>no</td><td>yes</td><td>no</td></tr><tr><td>M4</td><td>M2 + Likes</td><td>yes</td><td>yes</td><td>no</td><td>yes</td><td>no</td></tr><tr><td>M5</td><td>M2 + Number of Posts</td><td>yes</td><td>no</td><td>yes</td><td>no</td><td>no</td></tr><tr><td>M6</td><td>M2 + Recency Effect</td><td>yes</td><td>no</td><td>yes</td><td>yes</td><td>no</td></tr><tr><td>M7</td><td>M2 + Hierarchy Score</td><td>yes</td><td>no</td><td>yes</td><td>yes</td><td>yes</td></tr></table>

Table 5 displays several results of our model comparison: The Akaike and Bayesian information criterion (AIC and BIC) for assessing the in-sample performance and trade-of between fit and model complexity, as well as the estimated one-step ahead RMSPE defined above, as measure of pseudo out-of-sample prediction performance (e.g., Stock and Watson, 2012).

Before we can reliably discuss our empirical results, such as parameter estimates and corresponding standard errors, we have to check some model diagnostics. Due to the use of lags of the dependent variable, OLS is consistent only if residuals do not exhibit patterns of serial correlation. A Box-Pierce test for independence of the errors of M7 yields a p-value of 0.43 (considering 21 lags, i.e. three weeks), and inspection of the autocorrelation functions suggest that the OLS residuals are serially uncorrelated. The stability of our results can be assessed by re-estimating Equation (5) with subsets of the given data to produce recursive statistics, for example for regression coeficients and standard errors. Our results suggest that all obtained estimates are relatively stable over time, supporting the use of the ARDL modeling framework. Figure 6 displays recursive estimates for the short-run (left displays) and long-run (right displays) efect of the post-related covariates for subsets based on extending windows between week 31 and 40. Although there is some variance in the short-run as well as the long-run efects, both efects are quite stable over time for all covariates and significantly diferent from 0 throughout the whole period at a significance level of 5%.

UGC Indirect promotion (cumulated dynamics)  
UGC Socializing (cumulated dynamics)  
UGC Socializing (day−to−day)  
MGC C\_Feedback (cumulated dynamics)  
![](/api/attachments/REQ4RH9N/fulltext/images/9fe2c109cb754099b3a6d04a3667b29bd254f4681ca911fc797f5b2705b8bc57.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/c65569c535f2758998fc50b2ed50ade6579b6e706428da11e2a806523092fac7.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/fe62ec98b75b0095e7507fbd5ac4662582d489b432e045aad4557c417f031de9.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/a28d40e0d0c81ba83c70469d03f47b588736509a29d2d414b3fe5930ffdbbdfe.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/38020fa8c81111a08d0b78d1b53921f7b2686a76dc6a1fd6423dae9f79b1be41.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/67f92b1965b8adad93e7ddeba95b88baf18edded3371b78b287e94fb9fe5a800.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/06adf39fbf88f428f59a8aaac2ffada92f7e02265706bef16bcf16eef7a620a8.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/4254975f5b30a0595003e270c697631f0269bf581f3898988d90a139829de676.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/4e600a331c3462f323b8bbcc22496cd5ee62ffd6c8b4fac6a6250098a4c735c9.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/d03ab48a29d3dfda621f89ad202031ed99a1ee305ea1bdb050aa556e96c25bc7.jpg)  
Figure 6: Estimated short-run (left displays) and long-run (right displays) efect for ARDL model M7 using recursive (extending window) estimation for week 31–40 for the post-related covariates with 90% confidence intervals.

Table 5: Adjusted R<sup>2</sup>, Akaike and Bayesian Information Criterion as well as root mean square prediction error (based on extending window one-step-ahead predictions for the most recent seventy days of the sample) for the models of Table 4.

<table><tr><td>Model</td><td>Adj.  $R^{2}$ </td><td>AIC</td><td>BIC</td><td>RMSPE</td></tr><tr><td>M1</td><td>0.411</td><td>1025.5</td><td>1058.0</td><td>1.226</td></tr><tr><td>M2</td><td>0.413</td><td>1025.5</td><td>1061.6</td><td>1.225</td></tr><tr><td>M3</td><td>0.425</td><td>1025.8</td><td>1083.5</td><td>1.209</td></tr><tr><td>M4</td><td>0.417</td><td>1025.5</td><td>1068.7</td><td>1.211</td></tr><tr><td>M5</td><td>0.454</td><td>1027.9</td><td>1078.4</td><td>1.234</td></tr><tr><td>M6</td><td>0.433</td><td>1020.4</td><td>1070.9</td><td>1.204</td></tr><tr><td>M7</td><td>0.517</td><td>979.2</td><td>1029.7</td><td>1.174</td></tr></table>

## 5.2. Interpretation of Estimated Efects on the Conversion Rate

The results displayed in Table 5 suggest that M7 outperforms all other models. Furthermore, we observe that the simple autoregressive model M1 is more parsimonious w.r.t. BIC compared to models M2-M6. Including a lag of Visits in Model M2 improves both, fit and (though slightly) prediction performance, suggesting that the change in Visits is Granger-causal for the change in CVR. In this vein, the changes in our hierarchy score variables are also Granger-causal for the change in CVR. Model M3 adds recency efects of the posts to M1 and M6 adds recency efects to M2. Both models show a good predictive accuracy compared to models M1 and M2, but both are inferior to M7. The reversed role between absolute posts and post visibility for MGC versus UGC discussed in the previous subsection plays an important role for fit and predictive accuracy: Considering a hierarchy of posts such as in M6 outperforms the model based on absolute numbers in M5 as well as M4 including the number of likes as post-specific information, while our hierarchy score based model M7 outperforms all other competitors (w.r.t. all criteria). Table 6 displays the estimation results for model M7, based on Equation (5).

First of all, our results indicate that the variables capturing the sentiment of the posts do not afect the online store’s conversion rate. That may not seem very intuitive at first, but the post categories are closely related to sentiment, as for example UGC socializing posts are usually positive, while the promotion categories usually tend to be neutral. UGC feedback contains praise as well as criticism and is thus the only post category with a remarkable number of posts of either sentiment. Hence, the post categories shown in Table 2 for UGC and MGC already capture the sentiment information. Due to their insignificance, the sentiment variables have been omitted from the regression model. The estimates in Table 6 reveal that an increase in the number of fanpage users who visited the online store (Visits) in the previous week significantly decreases the current conversion rate.<sup>4</sup> Some posts might especially attract a high number of users that are engaged in hedonic browsing (e.g., Arnold and Reynolds, 2003; Moe and Fader, 2004). Such posts will keep up consumers’ interest for a certain amount of time. Thereafter the number of visitors aiming at hedonic browsing rather than shopping will significantly drop down and increase the store’s conversion rate.

Table 6: Estimated parameters (OLS) of the ARDL model M7. The response variable is ∆CVR<sub>t</sub>.

<table><tr><td>Coefficient type</td><td>Covariate</td><td>Estimate</td><td>Std. Error</td><td>t value</td><td>p-value</td></tr><tr><td rowspan="7"> $\alpha$ </td><td> $\Delta CVR_{t-1}$ </td><td>-0.699</td><td>0.058</td><td>-12.131</td><td>&lt; 0.001</td></tr><tr><td> $\Delta CVR_{t-2}$ </td><td>-0.598</td><td>0.072</td><td>-8.355</td><td>&lt; 0.001</td></tr><tr><td> $\Delta CVR_{t-3}$ </td><td>-0.427</td><td>0.080</td><td>-5.367</td><td>&lt; 0.001</td></tr><tr><td> $\Delta CVR_{t-4}$ </td><td>-0.411</td><td>0.080</td><td>-5.136</td><td>&lt; 0.001</td></tr><tr><td> $\Delta CVR_{t-5}$ </td><td>-0.240</td><td>0.081</td><td>-2.961</td><td>0.003</td></tr><tr><td> $\Delta CVR_{t-6}$ </td><td>-0.145</td><td>0.072</td><td>-2.010</td><td>0.045</td></tr><tr><td> $\Delta CVR_{t-7}$ </td><td>-0.130</td><td>0.056</td><td>-2.314</td><td>0.021</td></tr><tr><td> $\beta$ </td><td> $\Delta Visits_{t-7}$ </td><td>-1.175</td><td>0.647</td><td>-1.816</td><td>0.070</td></tr><tr><td rowspan="5"> $\gamma$ </td><td> $\Delta MGC\_ProductPromotion_{t-7}$ </td><td>-0.048</td><td>0.021</td><td>-2.325</td><td>0.021</td></tr><tr><td> $\Delta MGC\_Feedback_{t-1}$ </td><td>66.457</td><td>25.938</td><td>2.562</td><td>0.011</td></tr><tr><td> $\Delta UGC\_IndirectPromotion_{t-1}$ </td><td>2.640</td><td>0.711</td><td>3.712</td><td>&lt; 0.001</td></tr><tr><td> $\Delta UGC\_Socializing_{t-1}$ </td><td>0.342</td><td>0.070</td><td>4.883</td><td>&lt; 0.001</td></tr><tr><td> $\Delta UGC\_Feedback_{t-1}$ </td><td>-0.901</td><td>0.155</td><td>-5.809</td><td>&lt; 0.001</td></tr></table>

MGC product promotion and MGC feedback are the only company variables exerting a significant impact on the conversion rate. Company feedback seems to have a positive impact, contrary to user feedback that is usually associated with criticism that raises concerns about the overall shop quality and thus might lower the willingness to buy.

Company product promotion have the tendency of a negative impact on the conversion rate. UGC indirect promotions and UGC socializing increase the conversion rate. This indicates that the company should motivate users to especially create socializing posts or to indirectly promote their online store rather than to generate promotional posts by itself.

Company-generated feedback posts (MGC Feedback) have a large positive impact (c.f. Figure 5). The short-run efect is $\widehat { \gamma } _ { M G C . F e e d b a c k _ { t - 1 } } = 6 6 . 4 5 7 .$ , i.e., if the percentage of feedback posts in the hierarchy could be increased by one percentage point, the conversion rate increases on average by about 66.5 percentage points, ceteris paribus. Of course, this is nearly impossible to achieve, as company feedback is usually a reaction to certain user posts (often user feedback); also compare the range of the covariate in Table 3. Nevertheless should the number of company feedback posts (currently only 13) be increased. Because this efect is the largest, we use this variable to demonstrate the computation of the long-run efect. The estimated long-run efect of company-generated feedback posts calculated according to Equation (7) equals $\begin{array} { r } { \frac { \gamma _ { M G C , F e e d b a c k _ { t - 1 } } } { 1 - \left( \widehat { \alpha } _ { \Delta C V R _ { t - 1 } } + \widehat { \alpha } _ { \Delta C V R _ { t - 2 } } + \widehat { \alpha } _ { \Delta C V R _ { t - 3 } } + \widehat { \alpha } _ { \Delta C V R _ { t - 4 } } + \widehat { \alpha } _ { \Delta C V R _ { t - 5 } } + \widehat { \alpha } _ { \Delta C V R _ { t - 6 } } + \widehat { \alpha } _ { \Delta C V R _ { t - 6 } } \right) } = 1 8 . 2 0 7 4 } \end{array}$ . We observe that the long-run efect of company-generated feedback posts is significantly positive, although the long-run impact in general is only about one fourth of the immediate impact.

## 5.3. Post Creation Decision Support

Results such as the ones presented in Subsection 5.2 provide support for business decisions on timing and content of social media post. Table 6 indicates that the company should strive to encourage their customers to write socializing and indirect promotion posts. The company should furthermore create feedback posts. However, a long feedback post will reduce the visibility of former posts. This may result in a negative overall efect (on the conversion rate) if the former posts are user-generated socializing and/or indirect promotion posts. Assume for example that the hierarchy score for marketer-generated feedback is rising from 0.001 to 0.002. This will positively afect the diference of the conversion rate by 0.0665. At the same time the hierarchy score for a user-generated indirect promotion post might fall from 0.1 to 0.07 which reduces the diference of the conversion rate by 0.0792. The total efect of this virtual feedback post might hence be negative. A shorter feedback post leads to a smaller reduction of the hierarchy score of other post categories and might, for example, reduce the score for user-generated indirect promotion posts by only 0.02 so that we expect a positive efect on the diference of the conversion rate in total after submitting the new virtual feedback post. A shorter feedback post is meaningful if the former posts are user-generated indirect promotion or socializing posts whereas a long marketer-generated feedback post helps limiting the negative efect of user-generated feedback posts.

# ACCEPTED MANUSCRIPT

The efect of the post categories is specific for the investigated company. It might be worth for other companies to post price and product promotion posts. Based on our proposed hierarchy score, companies can investigate the efect of possible posts and ultimately decide when to submit, for example the next promotion post and in what length. In general, companies need to consider the efect of a new post as well as the efect of former posts that will be displaced by the new post. Our hierarchy score especially helps to determine the impact of a new post on the visibility of older posts and hence to consider decreasing efects of older posts on economic variables, such as the conversion rate.

## 6. Robustness Check

For the calculation of the hierarchy score, we assume that a typical graphical device displays about $M = 5 0$ text lines simultaneously. This assumption might be biased in two ways. First, the true average number of text lines that can be simultaneously presented on a typical device might difer from 50. And second, there might be a high variance in the number of simultaneously displayable text lines. Thus, we analyzed the robustness of our results under diferent values for M. More specifically, we set $M \in \{ 1 0 , 2 5 , 5 0 , 1 0 0 , 2 0 0 , 5 0 0 \}$ } and computed the performance for model M7 and each level of M.

The results in Table 7 show that M = 50 is the best performing assumption for the number of simultaneously displayable text lines. Model $\mathbf { M } 7 , \mathbf { h o w e v e r } .$ , also outperforms models M1–M6 with all other tested levels for M. This clearly indicates that our hierarchy score is robust to changes in the assumption that 50 text lines can be simultaneously displayed on a device at the time we observed our data.

Table 7: Adjusted R<sup>2</sup>, Akaike and Bayesian Information Criterion as well as root mean square prediction error for model M7 and diferent levels of M (i.e. number of text lines displayed simultaneously on screen).

<table><tr><td>M</td><td>Adj. R2</td><td>AIC</td><td>BIC</td><td>RMSPE</td></tr><tr><td>10</td><td>0.473</td><td>1002.8</td><td>1064.1</td><td>1.179</td></tr><tr><td>25</td><td>0.490</td><td>994.0</td><td>1055.3</td><td>1.193</td></tr><tr><td>50</td><td>0.517</td><td>979.2</td><td>1029.7</td><td>1.174</td></tr><tr><td>100</td><td>0.516</td><td>979.7</td><td>1041.0</td><td>1.193</td></tr><tr><td>200</td><td>0.487</td><td>995.6</td><td>1056.9</td><td>1.163</td></tr><tr><td>500</td><td>0.459</td><td>1010.1</td><td>1071.4</td><td>1.157</td></tr></table>

# ACCEPTED MANUSCRIPT

## 7. Discussion

We argue that the dynamic changes on the hierarchy of content items on a social media platform have a strong efect on the impact of marketer-generated contents (MGC) and user-generated contents (UGC) on purchase decision processes. In order to model such dynamic changes in econometric analyses, we propose a hierarchy score that expresses the chance of a content item to be considered by an average consumer. More text line equivalents. The average number of text lines above a content item at a day is finally transformed into a number between 0 and 1 that can be interpreted as the chance that a certain consumer will view the content item.

In an empirical analysis of data from a large German retailer, we demonstrate that our proposed hierarchy score improves the explanation and prediction of the conversion rate of those consumers who first visited the retailer’s fanpage and subsequently the retailer’s online store. This underlines our conjecture that dynamic changes on the hierarchy of contents significantly afect consumers’ purchase decision processes and allow for controlling and predicting from a managerial point of view.

In detail, our empirical analysis shows that MGC and UGC have a significant in- and out-of-sample impact on the conversion rate of the retailer’s online store. We find an economically large positive efect of MGC feedback and an economically rather small negative, though significant efect of MGC product promotion. UGC that fall in either the category indirect promotion or socializing have been found to positively influence the conversion rate, whereas a negative efect has been found for UGC feedback. All UGC based efects have an economically moderate size. In contrast to Goh et al. (2013), we did not find a higher efect of UGC rather than MGC on consumers’ purchase decision processes in our regression results. Note that our data show a considerably diferent ratio between UGC and MGC than the data used by Goh et al. (2013). Goh et al. (2013) analyzed a social media platform with many more UGC than MGC whereas in our case most of the content items have been created by the marketer. This dominance of marketer-generated content items might hence result in a rather low impact of UGC. Noteworthy, we also found that throughout the sample the UGC posts dominate with respect to the cumulated hierarchy score (c.f. Figure 5).

## 7.1. Research Implications

The contribution to existing research is twofold. First, we provide an algorithm for calculating the chance of a content item to be considered by a user of a social media platform. Our approach is applicable to all social media platforms that generate and present a stack of content items. Recent research has either

# ACCEPTED MANUSCRIPT

not modeled hierarchy efects (e.g., Albuquerque et al., 2012; Scholz et al., 2013) or analyzed the efects of social media contents on an individual level based on consumer behavior observations (Goh et al., 2013) Second, we provide first insights on the efect of several content types (e.g., product promotion, indirect promotion, socializing) on the conversion rate of a retailer’s online store. We show that items that are subject to indirect promotion or socializing improve the conversion rate if they are generated by consumers. Product promotion, if initiated by the marketer, seems counterproductive.

Recent research has intensively investigated the efects of content item characteristics, such as valence (e.g., Sonnier et al., 2011; Ho-Dac et al., 2013; Yin et al., 2016), information type (Goh et al., 2013), linguistic style (Ludwig et al., 2013; Ordenes et al., 2017), and content creator (Goh et al., 2013; Scholz et al., 2013). Although we include valence and content creator as content characteristics, our proposed hierarchy score could also be used to analyze the impact of other content characteristics, such as the type of information (persuasive or informative) or the linguistic style of the content items. Our proposed approach is also directly applicable to other economic variables, such as number of sales or the number of items in the online customers shopping carts.

## 7.2. Managerial Implications

From a managerial point of view, our method enables retailers to better understand, control, and predict the efect of the contents on their social media pages on economic variables, such as the conversion rate. Retailers can then adapt their social media strategy and especially post content items that have a positive impact on the online store’s conversion rate. Our proposed analytical method thus helps retailers to better manage an important aspect of “the future of retailing” – multifaceted data from multichannel environments (Grewal et al., 2017).

Our proposed hierarchy score is a tool that helps to explain and predict economic efects that are caused by any hierarchy of contents. Managers hence can apply our proposed score not only to estimate at least a partial efect of Facebook fanpage posts on economic figures, but also to investigate the economic impact of, for example, a hierarchy of promotional messages in a weekly or monthly newsletter, a hierarchy of news items on informational websites, such as agriculture.com, or a hierarchy of search results from online store search engines.

## 7.3. Limitations

A limitation of our study is that our data is for only one retailer. However, the goal of this paper is to establish a method for controlling the hierarchy efects of social media content items on economic variables.

# ACCEPTED MANUSCRIPT

Thus, we demonstrated the usage and benefits of our proposed method on only one data set. Future research should strive to apply the proposed method in order to analyze the impact of social media contents with regard to the position and hence the chance to consider distinct types of content items.

We furthermore parameterized our hierarchy score to be usable for analyzing fanpage contents. Content items on other platforms will often have a diferent layout which can be addressed by a diferent parametrization of the configuration of our hierarchy score. Future research may investigate the efect of social media contents from other platforms and therefore adapt our proposed method. A further avenue for future research is to include further parameters in the calculation of the hierarchy score in order to more accurately identify economic efects. The probability that users will visit a fanpage and an online store is not equally distributed over the hours of a day. If there is clear evidence that consumers do not visit a fanpage, for example, between 11pm and 5am, it seems promising to incorporate a parameter in the calculation of the hierarchy score that controls for such time efects.

Our proposed hierarchy score can be used to investigate position efects of content items on economic variables, such as the conversion rate. It can be hence applied to all social media platforms that present their content in some predefined order. Several platforms ofer further possibilities, like email newsletters and news feeds, to get access to their content. Furthermore, the hierarchy of content items might be individuall configurable (e.g., see Facebook’s Timeline). Although we argue that the position of content items also plays a significant role for investigating the economic impact if these possibilities are ofered by a social media platform, the application of our proposed hierarchy score is rather dificult, because researchers need to know in which order content items are presented in a newsletter, a news feed or on an individually configurable landing page. However, various online platforms present content items in the same order on their website as they do in an email newsletter. Also, various users still visit a social media website, such as hotukdeals.com, from time to time rather than subscribing to a news feed or a newsletter. Our proposed hierarchy score hence helps to uncover at least a part of the economic efects of content items. Further research is necessary to develop methods and procedures for investigating the economic efect of content items that are presented in an individually configurable hierarchy.

Especially social media platforms allow both, companies and users to post messages. A post creation decision support system might suggest to publish a price promotion post in exactly one hour. However, the decision support system does not know when users will submit their posts. In the worst case, various users might submit a post a few minutes after the company has published their price promotion. We however, argue the a post creation decision support systems still will help companies to decide when to create a post because several statistical figures about when and how often users submit a post can be estimated from former posts. This information can further be incorporated in a post creation decision support system. Furthermore, user posts are not allowed on all social media platforms. Facebook, for example, nowadays only allows their users to comment posts on a fanpage, but not to create posts by their own.

## Appendix - Numerical Example

This section is intended to exemplify the computation of the hierarchy score $H _ { p , t }$ defined in Equation (3). The crucial part is the computation of $\Lambda _ { p , t }$ (the average number of lines above a visible post $p$ for the time $p$ was available at day t), where we focus on the following computational steps<sup>5</sup>

$$
\Lambda_ {p, t} = \left\{ \begin{array}{l l} \frac {1}{S _ {p , t}} \sum_ {e = 2} ^ {E _ {t}} \underbrace {\left[ (s _ {e} - s _ {e - 1}) \underbrace {\sum_ {i = p + 1} ^ {I _ {e - 1}} \lambda_ {i , s _ {e - 1}}} _ {\text {   Step   1   }} \right]} _ {\text {   Step   2   }} & \text { if } \quad S _ {p, t} > 0, \\ \underbrace {\underbrace {\text {   Step   3a   }} _ {\text {   Step   3   }}} _ {0 \quad \text {   otherwise. }} & \end{array} \right.\tag{8}
$$

We choose a time frame of two days, four posts (P1 to P4) and two comments (C1 and C2) to demonstrate the computation of $\Lambda _ { p , t }$ and finally the hierarchy score $H _ { p , t }$ . Table 8 shows the configuration of our example $\lambda _ { p , s _ { e } }$

P1 is posted at 7:00:00 a.m. on day 1, yielding an event time of 25,200 (as 7·3 600 seconds have passed since the start of day 1). The end of day t = 1 (second $s = 8 6 , 4 0 0 )$ is equivalent to the start of day $t = 2$ (second $s = 0 )$ . The post size is 0 before a post exists. The size of an existing post $p$ will only change, if there are additional comments or if the post was edited (the latter does not occur in our example). Event 4 at day 1 is a comment (C1) that extends the size of P1 from 3 to 4 text lines (equivalently P3 is extended by C2 at event 3 at day 2).

Table 9 covers the determination of Step 1 of Equation (8). Step 1 corresponds to the determination of the number of lines above a post p at day t until event e occurs.

Table 8: Configuration of example and $\lambda _ { p , s _ { \epsilon } }$

<table><tr><td>Event</td><td>t</td><td> $e_t$ </td><td> $s_e$ </td><td> $λ_{1,s_e}$ </td><td> $λ_{2,s_e}$ </td><td> $λ_{3,s_e}$ </td><td> $λ_{4,s_e}$ </td></tr><tr><td>Day 1 starts</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>P1 at 7:00:00 a.m. (3 text lines)</td><td>1</td><td>2</td><td>25,200</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>P2 at 1:15:00 p.m. (9 text lines)</td><td>1</td><td>3</td><td>47,700</td><td>3</td><td>9</td><td>0</td><td>0</td></tr><tr><td>C1 for P1 at 2:00:00 p.m. (1 text line)</td><td>1</td><td>4</td><td>50,400</td><td>4</td><td>9</td><td>0</td><td>0</td></tr><tr><td>P3 at 4:00:00 p.m. (1 text line)</td><td>1</td><td>5</td><td>57,600</td><td>4</td><td>9</td><td>5</td><td>0</td></tr><tr><td>Day 1 ends</td><td>1</td><td>6</td><td>86,400</td><td>4</td><td>9</td><td>5</td><td>0</td></tr><tr><td>Day 2 starts</td><td>2</td><td>1</td><td>0</td><td>4</td><td>9</td><td>5</td><td>0</td></tr><tr><td>P4 at 8:25:00 a.m. (6 text lines)</td><td>2</td><td>2</td><td>30,300</td><td>4</td><td>9</td><td>5</td><td>6</td></tr><tr><td>C2 for P3 at 2:01:40 p.m. (1 text line)</td><td>2</td><td>3</td><td>50,500</td><td>4</td><td>9</td><td>6</td><td>6</td></tr><tr><td>Day 2 ends</td><td>2</td><td>4</td><td>86,400</td><td>4</td><td>9</td><td>6</td><td>6</td></tr></table>

Post P1 is the most recent post (i.e., located at the top of the hierarchy) until post P2 occurs. As P2 and P3 cover 9 and 5 textlines, P1 has 9 textlines above, when P2 occurs and 14 textlines above, when P3 occurs. Even though C2 appears after P4, the size of C2 does not afect the number of lines above P4 as C2 is related to P3 and thus extends the number of lines above P1 and P2 only. In Step 1 we use the number of textlines until $e _ { t }$ occurs which translates to using the sum of the $\lambda _ { i , s _ { e - 1 } }$ instead of the sum of the $\lambda _ { i , s _ { e } }$ . The reason for this will become apparent in Steps 2 and 3a.

Tables 10 and 11 cover steps 2 and 3a of Equation (8) for the events of day 1 and day 2.

For the computation of Step $2 , s _ { e } - s _ { e - 1 }$ is required, representing the number of seconds that have passed from the previous event to event e (e.g., P2 appears 22,500 seconds after P1). If this number is multiplied by the output of Step 1, we get the weighted number of lines above p at day t (i.e., output of Step 2). The output of Step 2 for $P 1$ is obtained for event 6 of day 1 as 28 800 · 14 = 403 200. The sum of all weighted numbers of textlines above $p$ at t is than used as input for Step 3a. The entries for event 1 at each day are omitted, as event 1 (day t starts) has no previous events at t. Hence, the summation starts from $e _ { t } = 2$

Table 12 covers the computation of $S _ { p , d } , \Lambda _ { p , d } .$ , and $H _ { p , d } .$

$S _ { p , t }$ represents the number of seconds, post $p$ is available at day t. As P1 appears at 7:00:00 a.m. at day 1, $S _ { 1 , 1 } = 8 6 , 4 0 0 - 2 5 , 2 0 0 = 6 1 , 2 0 0 . \ \Lambda _ { p , t }$ is obtained by dividing the Step 3a-value by the corresponding number of seconds $S _ { p , t }$ post $p$ was available at $t ,$ if the latter is positive (e.g., 492 300 61 200 ≈ 8 04). Hence, on average around 8 lines are above post P1 at day 1 (around 18.3 lines at day 2). The hierarchy score $H _ { p , t }$ is finally computed via Equation (1); for example

Table 9: Computation of Step 1 of Equation (8).

<table><tr><td rowspan="2"> $t$ </td><td rowspan="2"> $e_{t}$ </td><td rowspan="2"> $\lambda_{1,s_{e}}$ </td><td rowspan="2"> $\lambda_{2,s_{e}}$ </td><td rowspan="2"> $\lambda_{3,s_{e}}$ </td><td rowspan="2"> $\lambda_{4,s_{e}}$ </td><td colspan="4">Step 1:  $\sum_{i=p+1}^{I_{e-1}}\lambda_{i,s_{e-1}}$ </td></tr><tr><td> $p=1$ </td><td> $p=2$ </td><td> $p=3$ </td><td> $p=4$ </td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>3</td><td>3</td><td>9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>4</td><td>4</td><td>9</td><td>0</td><td>0</td><td>9</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>5</td><td>4</td><td>9</td><td>5</td><td>0</td><td>9</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>6</td><td>4</td><td>9</td><td>5</td><td>0</td><td>14</td><td>5</td><td>0</td><td>0</td></tr><tr><td>2</td><td>1</td><td>4</td><td>9</td><td>5</td><td>0</td><td>14</td><td>5</td><td>0</td><td>0</td></tr><tr><td>2</td><td>2</td><td>4</td><td>9</td><td>5</td><td>6</td><td>14</td><td>5</td><td>0</td><td>0</td></tr><tr><td>2</td><td>3</td><td>4</td><td>9</td><td>6</td><td>6</td><td>20</td><td>11</td><td>6</td><td>0</td></tr><tr><td>2</td><td>4</td><td>4</td><td>9</td><td>6</td><td>6</td><td>21</td><td>12</td><td>6</td><td>0</td></tr></table>

$$
H _ {1, 1} = \left(\frac {6 1 , 2 0 0}{8 6 , 4 0 0}\right) \left(\frac {1}{1 + \frac {4 9 2 , 3 0 0 / 6 1 , 2 0 0}{5 0}}\right) = 0. 6 1 0 1 6 8 1.
$$

It holds that $H _ { p , t } \in [ 0 , 1 ]$ . A hierarchy score of 1 is obtained if and only if post $p$ is available for $S _ { p , t } = 8 6$ 400 seconds at day t and there are no lines above $p$ (i.e., $\Lambda _ { p , t } = 0 )$ . $H _ { p , t } = 0$ can only be obtained, if a post is not available at day t. Note that $H _ { p , t }$ increases for larger values of $S _ { p , t }$ (meaning that a post is available for a longer period of time at day t) and smaller values of $\Lambda _ { p , t }$ (meaning that less lines are above a post on a certain day). Table 8 shows that despite P1 having the largest $\Lambda _ { p , 1 }$ , it also has the highest hierarchy score at day 1 due to early appearing at day 1 (highest $S _ { p , 1 , }$ . For day 2, we can see that despite P4 has no lines above, its post position score is less than that of the three other posts, since P1 to P3 were available all the day long $( \mathrm { i . e . , } S _ { p , 2 } = 8 6 , 4 0 0 )$ .

Table 10: Computation of Steps 2 and 3a of Equation (8) for day 1.

<table><tr><td> $t$ </td><td> $e_t$ </td><td> $s_e$ </td><td> $s_e - s_{e-1}$ </td><td colspan="4">Step 1:  $\sum_{i=p+1}^{I_{e-1}} \lambda_{i,s_{e-1}}$  $p = 1$   $p = 2$   $p = 3$   $p = 4$ </td><td colspan="4">Step 2:  $\left[(s_e - s_{e-1})\sum_{i=p+1}^{I_{e-1}}\lambda_{i,s_{e-1}}\right]$  $p = 1$   $p = 2$   $p = 3$   $p = 4$ </td></tr><tr><td>1</td><td>1</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>25,200</td><td>25,200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>3</td><td>47,700</td><td>22,500</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>4</td><td>50,400</td><td>2,700</td><td>9</td><td>0</td><td>0</td><td>0</td><td>24,300</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>5</td><td>57,600</td><td>7,200</td><td>9</td><td>0</td><td>0</td><td>0</td><td>64,800</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>6</td><td>86,400</td><td>28,800</td><td>14</td><td>5</td><td>0</td><td>0</td><td>403,200</td><td>144,000</td><td>0</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Step 3a: $\sum_{e=2}^{E_1} [\cdot]$ </td><td>492,300</td><td>144,000</td><td>0</td><td>0</td></tr></table>

Table 11: Computation of Steps 2 and 3a of Equation (8) for day 2.

<table><tr><td rowspan="2"> $dt$ </td><td rowspan="2"> $e_t$ </td><td rowspan="2"> $s_e$ </td><td rowspan="2"> $s_e - s_{e-1}$ </td><td colspan="4">Step 1:  $\sum_{i=p+1}^{I_{e-1}} \lambda_{i,s_{e-1}}$ </td><td colspan="4">Step 2:  $\left[(s_e - s_{e-1})\sum_{i=p+1}^{I_{e-1}}\lambda_{i,s_{e-1}}\right]$ </td></tr><tr><td>p = 1</td><td>p = 2</td><td>p = 3</td><td>p = 4</td><td>p = 1</td><td>p = 2</td><td>p = 3</td><td>p = 4</td></tr><tr><td>2</td><td>1</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>2</td><td>30,300</td><td>30,300</td><td>14</td><td>5</td><td>0</td><td>0</td><td>424,200</td><td>151,500</td><td>0</td><td>0</td></tr><tr><td>2</td><td>3</td><td>50,500</td><td>20,200</td><td>20</td><td>11</td><td>6</td><td>0</td><td>404,000</td><td>222,200</td><td>121,200</td><td>0</td></tr><tr><td>2</td><td>4</td><td>86,400</td><td>35,900</td><td>21</td><td>12</td><td>6</td><td>0</td><td>753,900</td><td>430,800</td><td>215,400</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Step 3a: $\sum_{e=2}^{E_2} [\cdot]$ </td><td>1,582,100</td><td>804,500</td><td>336,600</td><td>0</td></tr></table>

Table 12: Computation of $\Lambda _ { p , t }$ and $H _ { p , }$ <sub>t</sub> .

<table><tr><td rowspan="2">t</td><td rowspan="2">p</td><td colspan="4">Step 3a:</td></tr><tr><td> $\sum_{e=2}^{E_t} [\cdot]$ </td><td> $S_{p,t}$ </td><td> $\Lambda_{p,t}$ </td><td> $H_{p,t}$ </td></tr><tr><td>1</td><td>1</td><td>492,300</td><td>61,200</td><td>8.04</td><td>0.610</td></tr><tr><td>1</td><td>2</td><td>144,000</td><td>38,700</td><td>3.72</td><td>0.417</td></tr><tr><td>1</td><td>3</td><td>0</td><td>28,800</td><td>0</td><td>0.333</td></tr><tr><td>1</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>1</td><td>158,2100</td><td>86,400</td><td>18.31</td><td>0.732</td></tr><tr><td>2</td><td>2</td><td>804,500</td><td>86,400</td><td>9.31</td><td>0.843</td></tr><tr><td>2</td><td>3</td><td>336,600</td><td>86,400</td><td>3.90</td><td>0.928</td></tr><tr><td>2</td><td>4</td><td>0</td><td>56,100</td><td>0</td><td>0.649</td></tr></table>

## References

Albuquerque, P., Pavlidis, P., Chatow, U., Chen, K.-Y., Jamal, Z., 2012. Evaluating promotional activities in an online two-sided market of user-generated content. Marketing Science 31 (3), 406–432.

Arnold, M. J., Reynolds, K. E., 2003. Hedonic shopping motivations. Journal of Retailing 79 (2), 77–95.

Chelaru, S., Altingovde, I. S., Siersdorfer, S., 2012. Analyzing the polarity of opinionated queries. In: Baeza-Yates, R., de Vries, A. P., Zaragoza, H., Murdock, V., Lempel, R., Silvestri, F. (Eds.), 34th European Conference on IR Research. Vol. 7224. Springer, Ch. Posters, pp. 463–467.

Chevalier, J. A., Mayzlin, D., 2006. The efect of word of mouth on sales: Online book reviews. Journal of Marketing Research 43 (3), 345–354.

Ding, C., Cheng, H. K., Duan, Y., Jin, Y., 2017. The power of the “like” button: The impact of social media on box ofice. Decision Support Systems 94, 77–84

Duan, W., Gu, B., Whinston, A. B., 2008a. Do online reviews matter? – an empirical investigation of panel data. Decision Support Systems 45 (4), 1007–1016

Duan, W., Gu, B., Whinston, A. B., 2008b. The dynamics of online word-of-mouth and product sales – an empirical investigation of the movie industry. Journal of Retailing 84 (2), 233–242.

Forman, C., Ghose, A., Wiesenfeld, B., 2008. Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Information Systems Research 19 (3), 291–313.

Garc´ıa-Crespo, A., Colomo-Palacios, R., Gomez-Berbis, J. M., Ruiz-Mezcua, B., 2010. Semo: a framework for customer social´ network analysis based on semantics. Journal of Information Technology 25 (2), 175–188.

Godes, D., Mayzlin, D., 2009. Firm-created word-of-mouth communication: Evidence from a filed test. Marketing Science 28 (4), 721–739.

Goh, K.-Y., Heng, C.-S., Lin, Z., 2013. Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Information Systems Resarch 24 (1), 88–107.

Grewal, D., Roggeveen, A. L., Nordfalt, J., 2017. The future of retailing. Journal of Retailing 93 (1), 1–6.¨

Hendry, D. F., 1984. Dynamic specification. In: Griliches, Z., Intriligator, M. D. (Eds.), Handbook of Econometrics. Vol. 2. Amsterdam: North Holland, Ch. 18.

Ho-Dac, N. N., Carson, S. J., Moore, W. L., 2013. The efects of positive and negative online customer reviews: Do brand strength and category maturity matter? Journal of Marketing 77 (6), 37–53.

Jang, S., Prasad, A., Ratchford, B. T., 2012. How consumers use product reviews in the purchase decision process. Marketing Letters 23 (3), 825–838.

Kumar, A., Bezawada, R., Rishika, R., Janakiraman, R., Kannan, P., 2016. From social to sale: The efects of firm-generated content in social media on customer behavior. Journal of Marketing 80 (1), 7–25.

Laros, F. J. M., Steenkamp, J.-B. E. M., 2005. Emotions in consumer behavior: A hierarchical approach. Journal of Business Research 58 (10), 1437–1445.

Lee, D., Hosanagar, K., Nair, H., 2018. Advertising content and consumer engagement on social media: Evidence from facebook. Management Science forthcoming.

Lee, K., Lee, B., Oh, W., 2015. Thumbs up, sales up? the contingent efect of facebook likes on sales performance in social

commerce. Journal of Management Information Systems 32 (4), 109–143.

Liu, Y., 2006. Word of mouth for movies: Its dynamics and impact on box ofice revenue. Journal of Marketing 70 (3), 74–89.

Ludwig, S., De Ruyter, K., Friedman, M., Brggen, E. C., Wetzels, M., Pfann, G., 2013. More than words: The influence of afectiv content and linguistic style matches in online reviews on conversion rates. Journal of Marketing 77 (1), 87–103.

Meire, M., Ballings, M., Van den Poel, D., 2016. The added value of auxiliary data in sentiment analysis of Facebook posts Decision Support Systems 89, 98–112.

Minnema, A., Bijmolt, T. H., Gensler, S., Wiesel, T., 2016. To keep or not to keep: Efects of online customer reviews on product returns. Journal of Retailing 92 (3), 253–267.

Moe, W. W., Fader, P. S., 2004. Dynamic conversion behavior at e-commerce sites. Management Science 50 (3), 326–335.

Ordenes, F. V., Ludwig, S., De Ruyter, K., Grewal, D., Wetzels, M., 2017. Unveiling what is written in the stars: Analyzing explicit, implicit, and discourse patterns of sentiment in social media. Journal of Consumer Research 43 (6), 875–894.

Pesaran, M., Shin, Y., 1999. An autoregressive distributed lag modelling approach to cointegration analysis. In: Strom, S. (Ed.), Econometrics and Economic Theory in the 20th Century: The Ragnar Frisch Centennial Symposium. Cambridge University Press, Ch. 11.

Rishika, R., Kumar, A., Janakiraman, R., Bezawada, R., 2013. The efect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Information Systems Research 24 (1), 108–127.

Rosario, A. B., Sotgiu, F., de Valck, K., Bijmolt, T. H., 2016. The efect of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric factors. Journal of Marketing Research 53 (3), 297–318.

Scholz, M., Dorner, V., Landherr, A., Probst, F., 2013. Awareness, interest, and purchase: The efects of user- and marketergenerated content on purchase decision processes. In: Proceedings of the 34th International Conference on Information Systems. Milan, Italy.

Sonnier, G. P., Leigh, M., Rutz, O. J., 2011. A dynamic model of the efect of online communications on firm sales. Marketing Science 30 (4), 702–716.

Statista, 2016. Statistics and facts about social media marketing in the united states. URL https://www.statista.com/topics/1538/social-media-marketing/

Stieglitz, S., Kruger, N., 2011. Analysis of sentiments in corporate twitter communication – a case study on an issue of toyota. In:¨ Proceedings of the 22nd Australasian Conference on Information Systems. Sydney, Australia.

Stock, J. H., Watson, Mark, M., 2012. Introduction to Econometrics. Pearson.

Trusov, M., Bucklin, R. E., Pauwels, K., 2009. Efects of word-of-mouth versus traditional marketing: Findings from an internet social networking site. Journal of Marketing 73 (5), 90–102

Yin, D., Mitra, S., Zhang, H., 2016. When do consumers value positive vs. negative reviews? an empirical investigation of confirmation bias in online word of mouth. Information Systems Research 27 (1), 131–144.

Zhu, F., Zhang, M. Z., 2010. Impact of online consumer reviews on sales: The moderating role of product and consumer charac teristics. Journal of Marketing 74 (2), 133–148.

## Highlights

• We develop a score covering position efect of social media contents.

• The score helps analyzing the efect of contents on individuals and organizations.

• We apply our score to investigate economic efect of Facebook fanpage contents.

• We show that our score improves econometric models for predicting economic efect.

• We show that a retailer’s conversion rate depends on its social media contents.

# ACCEPTED MANUSCRIPT

## Biography

Michael Scholz is Assistant Professor for Information Systems at the University of Passau. His research is focused on the economic impact of e-commerce technologies and algorithms for e-commerce applications. He is author of several papers in journals, such as the European Journal of Operational Research, Decision Support Systems, Journal of Statistical Software, Electronic Markets, and Business & Information Systems Engineering.

Joachim Schnurbus is Assistant Professor for Statistics at the University of Passau. His research is focused on estimation and forecasting of complex time series and panel data. He is author of several papers in journals, such as the Journal of Applied Econometrics, the Journal of Applied Statistics, and Econometrics and Statistics.

Harry Haupt holds the Chair of Statistics at the University of Passau and is Vice-President of Research at the University of Passau. His research is focused on statistical and econometric models and quantile regression. He is author of several papers in journals, such as Econometric Theory, Journal of Applied Econometrics, Journal of Multivariate Analysis, Regional Science and Urban Economics, and Econometrics and Statistics.

Verena Dorner is Assistant Professor for Information Systems at the Karlsruhe Institute of Technology. Her research is focused on e-commerce, decision support and online user behavior. She is author of several papers in journals, such as the Journal of the AIS, the European Journal of Operational Research, Decision Support Systems, Economics Letters.

Andrea Landherr studied Business Mathematics at the University of Augsburg and Finance and Information Management at the University of Augsburg and the Technical University of Munich and holds a Ph.D. in Information Systems from the University of Augsburg. Her research interest is in the area of social networks and customer relationship management. She has published in journals, such as Business & Information Systems Engineering, Electronic Markets, Journal of Management Control, and Information Systems and e-Business Management.

Florian Probst studied Business Administration at the University of Augsburg and holds a Ph.D. in Information Systems also from the University of Augsburg. His research interest is in the area of social media, information technology and big data. He has published in journals, such as the Communications of the AIS, Computer Networks, Business & Information Systems Engineering, and Information Systems and e-Business Management.

![](/api/attachments/REQ4RH9N/fulltext/images/619cc253b00e4887610dd9cc65aa606223eb4db37973d2f2280ea2190680f2ae.jpg)

Today

Post 1

I recently order some clothers at RustyCage.com and was amazed to find a small gift in the package. Thanks!

![](/api/attachments/REQ4RH9N/fulltext/images/42f2b0384c00622a69f0d2806aa1ca0a2d180573adf686b2daa6a8f081a1ecf5.jpg)

Yesterday

Post 2

We are pleased to celebrate our online store's 10th birthday with you.

Visit our store today and save up to 50%.

![](/api/attachments/REQ4RH9N/fulltext/images/28ed1dad98c1935d942343ab982a08ef2b35b2c51d52bd0692d27223cee582ea.jpg)

Sepp Today

Wow!!! Let's celebrate.

![](/api/attachments/REQ4RH9N/fulltext/images/fb0a12898f777f623d5b00e85d434a4627305f5e265facd2c2d3c4fc4b3a2237.jpg)

2 Days Ago

Post 3

Your views are very important to us. Fill in our survey and you will be entered into our prize draw

![](/api/attachments/REQ4RH9N/fulltext/images/b055d0273835a861142c60846d2d55279cf8dcf0bd26e1abe63348fecdf58bec.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/ea5a6e67f02a1738d95ef38412a4985cd7808fd6534ecf3a66e4c31acb8ada49.jpg)

Today

God, damn, a blank ...

![](/api/attachments/REQ4RH9N/fulltext/images/e28829e9c2c5040a29a159f083e40be45531e0926f61a5133b82bfacbc58fa9b.jpg)

Alice Yesterday

Wow, I got it. I indeed have won \$100.

![](/api/attachments/REQ4RH9N/fulltext/images/621edd57cf2bd55542336b221a3c791451743cc13ee087b8c0905602eb54677f.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/e46f2c03c7f54dc42fb19084ae5e4d2111cfa5a9cdf22c81e570a1566387ee71.jpg)  
Figure 2

Gefäll mir Kommentieren TeililnFOOTlER

![](/api/attachments/REQ4RH9N/fulltext/images/9d853290ed684e9d3e1d892153b6be5c38304bdd532a9082c9d24e82255f7a1d.jpg)

![](/api/attachments/REQ4RH9N/fulltext/images/0c41250363a6f70776d79e8f3654c71945f4b7e7a62637dae885c7453f542214.jpg)  
Figure 4

![](/api/attachments/REQ4RH9N/fulltext/images/0a0c649983ada8f48750c37203ce71293514c1b6a113f8436ecdef70d34e96f1.jpg)  
Figure 5

![](/api/attachments/REQ4RH9N/fulltext/images/062fbc4ce09cefd180756d95a7ef5c51c83bbaf7497d94dcae8813f16c16d88a.jpg)
