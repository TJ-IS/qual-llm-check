---
otero_id: 27979
otero_key: "67YDYAV2"
title: "Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?"
authors: "Xiang (Shawn) Wan; Anuj Kumar; Xitong Li"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0560"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?

Xiang (Shawn) Wan,<sup>a</sup> Anuj Kumar,<sup>b,</sup>\* Xitong Li<sup>c</sup>

<sup>a</sup> Leavey School of Business, Santa Clara University, Santa Clara, California 95053; <sup>b</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>c</sup> Department of Information Systems and Operations Management, HEC Paris, 78351 Jouy-en-Josas, France \*Corresponding author

Contact: xwan@scu.edu, https://orcid.org/0000-0003-1076-7945 (X(S)W); akumar1@ufl.edu, https://orcid.org/0000-0002-2727-3784 (AK) lix@hec.fr, https://orcid.org/0000-0002-8005-7212 (XL)

Received: October 28, 2020 Revised: May 18, 2022; March 18, 2023; May 16, 2023 Accepted: May 30, 2023 Published Online in Articles in Advance: October 16, 2023

https://doi.org/10.1287/isre.2020.0560

Copyright: © 2023 INFORMS

Abstract. Although the effects of algorithmic product recommendations on product sales are understood, the differential effects of retargeted recommendations (recommended products a user has previously viewed) versus generic recommendations (recommended pro ducts a user has not previously viewed) are unclear. We conduct a field experiment to empirically examine the relative effect of retargeted versus generic recommendations on product sales at different stages of users’ purchase funnel. The product recommendations can affect sales by influencing the number of product impressions and their conversion rates (purchase probability conditional on impression). We separately estimate the effect of retargeted and generic recommendations on product impressions and conversion rates. We find that (i) generic recommendations increase conversion rates only in the early purchase funnel stage, but retargeted recommendations do not affect conversion rates, and (ii) both recommendations result in a higher number of impressions of recommended products. Overall, retargeted (generic) recommendations result in higher recommended and total product sales in the late (early) purchase funnel stage. We also conducted a controlled experiment on Amazon MTurk to unveil that retargeting (showing previously viewed products to users) drives the effect of retargeted recommendations. Our counterfactual simulations show that the retailer can obtain up to three percent higher product sales by applying our findings to the existing recommendation systems. Our research has implications for online retailers and the design of algorithmic product recommendation systems.

History: Param Singh, Senior Editor; Idris Adjerid, Associate Editor. Funding: This work was supported by the Leavey School of Business at Santa Clara University [Grant 102720].

Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2020.0560.

Keywords: algorithmic product recommendations • recommendation systems • collaborative filtering • retargeted recommendations purchase funnel • field experiment • randomized online experiment

## 1. Introduction

Most recommendation systems on e-commerce websites recommend a few related products on a focal product’s page based on their co-views and co-purchases by other users (Lin et al. 2017; Adomavicius et al. 2018; Adomavicius et al. 2019; Kumar and Hosanagar 2019; Lee and Hosanagar 2019, 2021; Li et al. 2022; Peng and Liang 2023; Wan et al. 2023).<sup>1</sup> These collaborative filter-based recommendation systems infer what a user would prefer to view or buy after viewing a focal product based on other users’ browsing behavior (Linden et al. 2003, Kumar and Hosanagar 2019). We call such recommendations generic recommendations. However, sometimes such recommendations are also previously viewed by the consumers, which we call retargeted recommendations.<sup>2</sup> Some recommendation systems especially show retargeted products to the consumers, such as Adobe Commerce (recently viewed) and Oracle (last viewed).<sup>3</sup>

Knowing which types of recommendations are better for users and offering them could increase sales.

The relative benefits of retargeted versus generic recommendations may vary with a user’s needs at different stages of his or her purchase process (i.e., purchase funnel). Generic recommendations could be helpful to users in the early stage of a user’s purchase funnel if it helps the user discover related products from an extensive product assortment. In contrast, retargeted recommenda tions could be helpful in the later stage of the purchase funnel when the users’ preferences have narrowed down, possibly because it reminds them of the earlier viewed products. Offering more suitable recommendations to users at the appropriate purchase funnel stage could significantly improve sales. However, prior research on product recommendations provides little guidance on the relative efficacy of retargeted versus generic recommen dations at different purchase funnel stages.

Although studies in the display ad literature examine the relative effect of generic versus retargeted ads on the conversion rates of ad impressions, their findings may not apply in the context of product recommendations (Lambrecht and Tucker 2013, Bleier and Eisenbeiss 2015, Sahni et al. 2019). Usually, generic or retargeted ads are shown to consumers on a third party’s website, affecting ad conversion rates (Lambrecht and Tucker 2013). In contrast, recommendation systems recommend products on other related products’ pages while consumers shop on the firm’s website. Showing product recommendations could affect the number of recommended product impressions and their purchase probability conditional on their impression (conversion rate). To our knowledge, no prior study has examined recommendations’ effect on the number of recommended product impressions and their conversion rates.

Therefore, we answer the following questions. (i) When is it beneficial to show retargeted versus generic recommendations, and why? (ii) Are the relative benefits of retargeted versus generic recommendations contingent on consumers’ situational factors (i.e., the early versus late stage of a purchase funnel)? (iii) What are the sales gains by selectively offering retargeted and generic recommendations at appropriate stages of the purchase funnel?

We answer the above research questions with a field experiment on the website of a midsize U.S. apparel and home goods retailer. Visitors to the website were randomly assigned to view one of the two versions of the website. The website’s treated version recommended four related products (hereafter RPs) on the focal product’s (hereafter FP) web page. The website’s control version hid the RPs on FP’s page. If a visitor had viewed (not viewed) the RP in his or her past sessions, it is called retargeted (generic) RP recommendation or impression. Thus, visitors received four RP impressions on an FP’s page; some could be retargeted and others generic. Following the literature on retargeted ads (Bleier and Eisenbeiss 2015, Sahni et al. 2019), we consider all visitor sessions after (before) a visitor had carted a product in a product category as the late (early) stage of his or her purchase funnel.

We found that presenting either type (retargeted or generic) of product recommendations leads to more RP impressions. However, only generic recommendations in the early stage of the purchase funnel increase RP conversion rates. The retargeted recommendations do not affect the RP conversion rates in the early or late purchase funnel stage. For visitors in the early purchase funnel, showing either type of product recommendation increases RP sales, but generic recommendations have a higher effect. In contrast, only retargeted recommendations increase RP sales for visitors in the late stage of the purchase funnel, but generic recommendations have no effect.

Retargeted recommendations in our field experiment were both previously viewed products and identified by the recommendation algorithm. Thus, the resulting higher sales could be because of the previous views (retargeting effect), determined by the collaborative filtering algorithm (generic recommendations), or both. We conducted a controlled online experiment on Amazon MTurk to tease out the underlying reason for this result. In this experiment, we randomly assigned visitors to view either pure retargeted products (products they viewed in the early phase but not identified by the recommendation algorithm) or generic recommended products in the later phase of the experiment. We found that visitors purchase more retargeted products than generic recommendations in the late purchase funnel stage. The combined reading of the field and online experiments results indicate that visitors purchase retargeted recommendations more because of the retargeting effect in the late purchase funnel stage.

Although our findings indicate the relative benefits of retargeted and generic recommendations on RP sales, their effects on the total product (FP + RP) sales are man agerially more relevant. Because RPs belong to FP’s product subcategory, higher RP sales may cannibalize FP sales. Therefore, we estimate the effect of recommendations on the combined FP and RP sales. Similar to ou findings on RP sales, we find that generic (retargeted) recommendations benefit the total product sales in the early (late) purchase funnel stage. We simulated the counterfactual FP and RP sales by replacing the existing retargeted (generic) recommendations and found up to a three percent increase in the total product sales.

Our findings contribute to the growing research on recommender systems in the IS literature (Lin et al. 2017; Adomavicius et al. 2018; Adomavicius et al. 2019; Kumar and Hosanagar 2019; Lee and Hosanagar 2019, 2021; Li et al. 2022; Peng and Liang 2023; Wan et al. 2023). First, our study estimates how the impact of product recommendations would vary with visitors’ situational factors, such as whether the visitor has viewed the recommended product before and is in the early or late stage of his or her purchase funnel. Second, we uncover the relative benefits of two types (retargeted and generic) of product recommendations across consumers’ path-to-purchase products in different stages of their purchase process. Third, our findings can significantly increase online sales when incorporated with the widely used item-based collaborative filtering recommendation system.

## 2. Literature Review

## 2.1. Product Recommendations

We begin with a brief review of the technical literature on different types of recommendation systems and then focus on the IS literature on the economic value of recommendation systems.

2.1.1. Types of Product Recommendation Systems. Recommender systems have become an important research area in academics and industry since the mid-1990s (Resnick et al. 1994, Adomavicius and Tuzhilin 2005, Batmaz et al. 2019). The recommender systems are classified into three categories based on the information they use: collaborative filtering-based recommender systems, content-based recommender systems, and hybrid recommender systems (Adomavicius and Tuzhilin 2005).

The collaborative filtering (CF) systems recommend items to a user that others with similar tastes previously liked. CF techniques require many existing users’ ratings or purchase/browsing data. Memory-based and model-based CF algorithms are the two types of CF recommender systems. The memory-based CF algorithms can be either itembased (Sarwar et al. 2001, Linden et al. 2003) or user-based (Resnick et al. 1994), which recommend products based on the similarity between items or users using the useritem rating matrix. The model-based CF algorithms generate recommendations based on models developed by machine-learning techniques. Model-based CF has several limitations, such as expensive model building and loss of valuable information because of dimensionality reduction techniques. Compared with model-based CF, memory-based CF techniques are much easier to implement. Content-based systems recommend items similar to the ones the user liked in the past by leveraging the descriptive characteristics of products and profiles of users (Batmaz et al. 2019). Such techniques are efficient when recommending new items not yet rated by users. However, such techniques also have limitations, such as limited content analysis (i.e., insufficient features to distinguish items) and overspecialization (i.e., unable to show unexpected items) (Lops et al. 2011). Whereas CF-based techniques leverage the user-item rating data to make predictions, content-based techniques rely on the features of items and users. The hybrid systems combine the two methods, such as the weighted average of the predictions from the two systems (Basilico and Hofmann 2004, Thorat et al. 2015). Although hybrid strategies overcome some limitations of CF- and content-based methods, they have high complexity and implementation costs.

The CF-based technique is the most popular model in practice (Lee and Hosanagar 2021).<sup>4</sup> For this reason, most academic studies have examined the CF-based recommender systems (Lin et al. 2017; Adomavicius et al. 2018; Adomavicius et al. 2019; Kumar and Hosanagar 2019; Lee and Hosanagar 2019, 2021; Li et al. 2022; Peng and Liang 2023; Wan et al. 2023).

2.1.2. Economic Value of Product Recommendations. Our research is closely related to the IS literature that examines the effect of product recommendations on sales. De et al. (2010) found that the recommender system positively affects the sales of promoted and nonpromoted products. Lee and Hosanagar (2019) showed that purchase-based CF increases product views by 0.5% and sales volume by 5%. In contrast, view-based collabo rative filtering increases product views only by 11% and sales volume by 0.8%. Lee and Hosanagar (2021) found that using recommender systems can, on average, increase product views by 15.3% and the final conversion rate by 7.5%.

A few studies in this literature examine the effect of co-view or co-purchase relationships between products on product sales (Goldenberg et al. 2012).<sup>5</sup> For example, Oestreicher-Singer and Sundararajan (2012) found that explicit visibility of the co-purchase relationship can lead to an average threefold amplification of complementary products’ influence on each other’s demands. Kumar and Tan (2015) found that joint product display not only increases the FP sales (direct effect) but also increases the complementary products’ sales (spillove effect). Whereas the jointly displayed products are often complementary in the study (e.g., apparel and accessories) (Kumar and Tan 2015), Kumar and Hosanagar (2019) examined the situation where the FP and the RP were substitute products. They found that, on average, a product’s recommendation links lead to increased sales of substitute RPs. Their detailed analysis reveals that a recommendation link increases the daily number of FP page views by 7%, reduces FP sales conditional on the page views by 8.5%, and increases the RPs’ sales by 24.5%. Lin et al. (2017) explored the effects of the diver sity of the product recommendation network and found that a 1% increase in the category diversity of the incoming (outgoing) co-purchase network of a product is associated with a 0.011% increase (decrease) in product sales.

Although the above studies examined how the effect of recommendations on sales may vary with product characteristics, they largely overlooked how their impact would vary with visitors’ situational factors, for example, whether the user has previously viewed the recommended product or is in the early versus late stage of the purchase funnel. Understanding the impact of product recommendations on such factors is theoretically and managerially relevant.

The recommendation systems create a network of interconnected products on a website by recommending related products on other product pages. Such a recommendationgenerated product network could influence users’ browsing and purchasing on the website (Oestreicher-Singer and Sundararajan 2012, Oestreicher-Singer et al. 2013, Kumar and Hosanagar 2019). The recommendations-generated interconnection between related products could increase the visibility and, thus, the number of impressions of RPs on the website. Moreover, showing a related product on the FP’s page could also increase the RP’s purchase probability conditional on its impression. A few prior stud ies have examined the effect of product recommendations on both of these mechanisms (Oestreicher-Singer et al. 2013, Kumar and Hosanagar 2019).

Our paper adds to this literature by examining the effects of the two types of product recommendations (retargeted and generic) on both outcomes (number of impressions and purchase probability conditional on impression) for visitors in the early versus late stages of a purchase funnel. To our knowledge, this is the first study that examines the effects of different product recommendations at such a granular level.

## 2.2. Retargeted Ads

Our research is also related to the literature on display ads. Prior research in this literature primarily documents that display ads’ effectiveness can differ for consumers at different stages of their purchase funnels (Hoban and Bucklin 2015, Ghose and Todri 2016, Todri et al. 2020). Ad retargeting is an increasingly popular display ad method that leverages the “big data” of consumers browsing behaviors across websites (Shen and Miguel Villas-Boas 2018, Choi et al. 2019). Specifically, advertisers display ads for products and brands that consumers have previously browsed on other third-party websites (called retargeted ads).

Prior studies in the retargeted ads literature have examined conversion rates of ad impressions under different conditions by exogenously showing ad impressions on third-party websites (Lambrecht and Tucker 2013, Bleier and Eisenbeiss 2015, Sahni et al. 2019). Lambrecht and Tucker (2013) showed consumers a generic or a dynamic retargeted ad when they visited a thirdparty’s website after viewing the focal firm’s website in their field experiment. Unlike retargeted ads shown on the third party’s website, product recommendations are shown on the FPs’ pages while consumers are still shopping on a website. Thus, displaying product recommendations on FPs’ pages could affect the number of RPs impressions and the conversion rate conditional on its impressions. To understand the relative value of showing retargeted recommendations over generic recommendations, it is deemed that examining their effects on the number of impressions and purchase probability of RPs is necessary.

## 2.3. Stages of Consumer Purchase Process

Our research is also related to the literature on the consumer purchase process or purchase funnel stages. Consumer purchase paths typically involve several discrete stages. The classical AIDA (i.e., awareness, interest, desire, and action) model postulates that every advertising process begins by capturing attention and then moves on to information assimilation and comprehension, which results in desirability and is concluded with action (Strong 1925). Different variants based on the AIDA model have been proposed, and the most widely used model constitutes three stages: awareness, consideration, and purchase (Abhishek et al. 2012, Bleier and Eisenbeiss 2015, Venkatraman et al. 2015). Because awareness and consideration are largely unobservable, prior researchers either model them as latent or proxy them with observable consumer behaviors.

One stream of literature models funnels stages as latent. The hidden Markov model is widely used to capture the dynamics of consumer behavior. Abhishek et al. (2012) modeled the consumer’s path to purchase using a dynamic hidden Markov model and then used it to solve the problem of advertising attribution. Zhang et al. (2019) proposed a forward-looking structural Markov model to detect the consumer latent engagement stages and identify four engagement stages: aware, exploring, active, and addicted. To capture the annoying effects of ads, Todri et al. (2020) proposed a hidden Markov model consisting of three hidden states (i.e., annoyance, awareness, and interest) and one observed state (i.e., the purchase state).

The other stream of literature explicitly proxied consumers’ purchase funnel stages with their observable behaviors. For example, Bleier and Eisenbeiss (2015) considered three stages of the purchase funnel (i.e., information state, consideration state, and post-purchase state) and proxied them with observables. Specifically, (i) a consumer was defined to be in an early information state if he or she was at the beginning of the purchase process and had conducted no further purchase-related actions during the most recent online store visit; (ii) a consumer was defined to be in the consideration state if he or she used the virtual shopping cart but still made no purchase; and (iii) a consumer was defined to be in a postpurchase state if he or she completed a purchase before exiting the online store. Sahni et al. (2019) considered three stages of the purchase process: viewing pages, creating shopping carts, and making purchases. Consumers were considered in their purchase process in the early (later) stage if they were product viewers (cart creators). Specifically, a user was defined as (i) a product viewer if he or she exited the website after viewing a product page without purchasing or creating a shopping cart and (ii) a cart creator if he or she exited the website after creating a shopping cart but without purchasing.

Following the second literature stream (Bleier and Eisenbeiss 2015, Sahni et al. 2019), we consider all sessions after (before) a visitor carts a product in a product category as his or her late (early) purchase funnel stage.

## 3. Field Setup

We run a field experiment on a U.S. midsize apparel and home goods retailer’s website (hereafter, the firm). The firm’s annual sales exceed \$400 million, of which 10% comes from online sales.

## 3.1. Website Organization

The firm has more than 35,000 products for sale on its website. These products are classified into different categories: women’s clothing, men’s clothing, etc. Products under each category are further classified into subcategories. The main page of a product subcategory displays thumbnail-sized images of products in that subcategory. Figure 1 illustrates a product page example. In Figure 1, we call the product with a larger image the focal product (FP), and the four products under the heading “MORE OPTIONS” are the recommended products (RPs). The visitor can access an RP’s description page by clicking its small image on the FP’s page. Once on the RP’s product description page, this RP becomes an FP with its four related RPs.

## 3.2. Product Recommendations

The firm employs two rules in choosing RPs on an FP’s page. First, the firm uses the IBM Coremetrics algorithm to compute the affinity score between an FP and an RP.<sup>6</sup> An FP-RP pair’s affinity score is calculated based on their co-views and co-purchases in all sessions in the last 30 days. Specifically, the system computes four scores: (1) the number of times that a visitor viewed both products in the same session (view-to-view score), (2) the number of times that a visitor bought the RP after viewing the FP in the same session (view-to-buy score), (3) the number of times that a visitor abandoned the carted FP and bought the RP in the same session (abandon-to-buy score), and (4) the number of times that a visitor bought both the FP and RP but not necessarily in the same session (buy-to-buy score). The affinity score is the weighted average of these four scores: 70 × view-to-view score + 20 × view-to-buy score + 5 × buy-to-buy score + 5 × abandonto-buy score.<sup>7</sup>

In addition to the affinity score, the recommendation engine applies a business rule of recommending only products in the FP’s product subcategory. In this way, the RPs on the FPs’ pages are substitutes. The system computes each product’s affinity scores daily with all other products on the website and stores the top 15 products with the highest affinity scores. The recommendation system recommends the top four products as RPs on each FP’s page.

## 3.3. Effect of Retargeted vs. Generic Recommendations

Because the recommendation system infers the relationship (closeness) between the RP and an FP from the crowd’s co-browsing (co-purchase) behavior, we call it generic recommendations. Like a web page view with a displayed ad is called an ad impression, FP’s pageview with a displayed RP is called an RP impression in our study.

Figure 1. (Color online) Product Page of an FP with Four RPs  
![](/api/attachments/67YDYAV2/fulltext/images/81443a13121710b20bc869440a7df880c6fda48de1a1da0184a4cd2840e392b5.jpg)

Thus, an FP’s pageview results in four RP impressions corresponding to the four shown RPs. A visitor may have viewed some of the RPs displayed on an FP’s page in past sessions. We call such RP impressions retargeted or generic RP impressions, depending on whether the visitor has viewed the RP impressions before or not.<sup>8</sup>

RPs for an FP in generic recommendations are chosen based on what most visitors on the firm’s website have viewed or purchased after visiting the FP’s page. Thus, a visitor may know the relationship between such RPs and FP, even when the FP’s page does not display them. Moreover, the visitor could also find out the related RP for an FP from other tools (such as search tools) or their contiguous display on other pages on the firm’s website. Thus, visitors may view and purchase RPs after visiting their FPs’ pages because of their interrelationship, even when the FPs’ pages do not explicitly display RPs (Oestreicher-Singer and Sundararajan 2012).

Explicitly displaying an RP on the FP’s page has two additional effects on its purchase. First, the RP’s additional visibility on the FP’s page would enhance its chances of discovery and hence, its purchase. Second, the visibility of a related RP on the FP’s page may further help consumers learn about their similarities (Oestreicher-Singer and Sundararajan 2012). Thus, the true effect of generic RP impressions on RP purchase is the difference in RP purchase when it is recommended on the FP’s page versus not.

Whereas generic RP impressions are what others have browsed in their past sessions, retargeted RP impressions are what a visitor has browsed in past sessions. A recommended product that a user previously viewed is different from the one that he or she has not viewed because the repeated exposure of a product could (i) increase the probability of the user registering it, (ii) signal its higher relevance to the user, (iii) help the user recall the previously explored product, and (iv) indicate that the user may have seen most products in that category. In other words, the effect of retargeted RP impressions on RP sales may differ from that of generic recommendations.

Besides having an overall differential effect on RP sales, the effects of retargeted and generic recommendations may differ based on a visitor’s stage in his or her purchase process (purchase funnel). Visitors are in the exploratory phase in the early stage of their purchase process, because their preferences are malleable. Therefore, generic recommendations based on others’ preferences may be more helpful to visitors in the early stage of their purchase process. In contrast, the visitors may be less receptive to the generic recommendations later in their purchase process after their preferences have narrowed down. The retargeted recommendations may be more helpful in the later stages if they signal higher relevance or help visitors recall the product they saw earlier.

To summarize, we expect the effect of retargeted and generic recommendations to differ based on whether the FP’s page explicitly shows RPs and whether the visitor is in the early or late stages of his or her purchase process. Therefore, we estimate the relative efficacy of retargeted over generic recommendations with the experimental design shown in Table 1.

## 3.4. Experimental Design

The firm created two versions of product pages on its website. In the treated version, an FP’s page displays four RPs identified by the recommendation system, as shown in Figure 1. In contrast, the four RPs identified by the recommendation system were not displayed on the FP’s page in the control version. The field experiment ran for nine weeks from April 8, 2015. During this experiment, half of the visitors to the website were randomly selected (treated visitors) and assigned to the treated version, and the remaining half (control visitors) to the control version. If a visitor is assigned to the product page’s treated (control) version in his or her first session, he or she consistently sees the same version in repeated sessions.<sup>10</sup> Therefore, there are two possibilities for RP impressions in this experimental setup: explicitly shown RP impressions in the treated sessions and hidden RP impressions in the control sessions. If a treated (control) visitor has viewed the RP shown (hidden) on an FP’s page in his or her past session, it is a retargeted RP impression. Otherwise, it is a generic RP impression.

Visitors may view RP impressions at different stages of their purchase process. To examine this, we created a visitor’s purchase funnel based on various sessions in which a visitor views a product under a product subcategory. A visitor’s purchase funnel begins in the session in which he or she starts viewing products in a product subcategory. All subsequent sessions in which the visitor views and carts products in that subcategory are the continuations of the visitor’s purchase funnel. The visitor’s purchase funnel ends when he or she purchases a product in that subcategory. We classify all sessions by a visitor in a product subcategory into two stages of his or her purchase funnel: early and late. Usually, visitors first explore products in a product subcategory and cart those products that they would like to consider for purchase. Thus, if a visitor carts product(s) in a product subcategory, he or she has narrowed down his or her choices (or preferences) and is closer to the purchase decision. Accordingly, we consider all sessions after the session in which a visitor carts product(s) in a subcategory to be in the late stage of his or her purchase funnel. The remaining visitor sessions in a product subcategory are considered the early purchase funnel stage (Hoban and Bucklin 2015, Sahni et al. 2019).

Table 1. Experiment Design

<table><tr><td rowspan="2"></td><td rowspan="2">RP viewed in the past sessions</td><td colspan="2">RP displayed on the FP&#x27;s page</td><td rowspan="2">Effect of recommendations</td><td rowspan="2">Relative effect of retargeted recommendations over generic recommendations</td></tr><tr><td>No</td><td>Yes</td></tr><tr><td rowspan="2">Early stage of the purchase funnel</td><td>No (generic)</td><td> $RPPur_1$ </td><td> $RPPur_2$ </td><td> $RPPur_2 - RPPur_1$ </td><td> $(RPPur_4 - RPPur_3)$ </td></tr><tr><td>Yes (retargeted)</td><td> $RPPur_3$ </td><td> $RPPur_4$ </td><td> $RPPur_4 - RPPur_3$ </td><td> $-(RPPur_2 - RPPur_1)$ </td></tr><tr><td rowspan="2">Late stage of the purchase funnel</td><td>No (generic)</td><td> $RPPur_5$ </td><td> $RPPur_6$ </td><td> $RPPur_6 - RPPur_5$ </td><td> $(RPPur_8 - RPPur_7)$ </td></tr><tr><td>Yes (retargeted)</td><td> $RPPur_7$ </td><td> $RPPur_8$ </td><td> $RPPur_8 - RPPur_7$ </td><td> $-(RPPur_6 - RPPur_5)$ </td></tr></table>

Notes. FP and RP denote the focal and recommended products. RPPur in each cell represents the RP purchases under that condition

We collect data on RP impressions on FP page views in visitor sessions during the experiment. An RP impression in our data can be under eight possible combinations of (i) treated versus control sessions, (ii) retargeted versus generic RP impression, and (iii) late versus early stage of purchase funnel. We estimate the relative efficacy of retargeted over generic recommendations in the early and late stages of visitors’ purchase funnels using the experimental design shown in Table 1.

However, the field experiment design has two limitations. First, the retargeted recommendations in our field setup are both previously viewed products (retargeting) and identified by the collaborative filtering algorithm (generic recommendations). Thus, it is unclear whether the effect of retargeted recommendations is due to retargeting, generic recommendations, or both. An answer to this question would unveil the mechanisms for the relative benefit of retargeted recommendations in the late purchase funnel stage. Second, the retargeted and generic recommendations are not exogenously generated in the field setup. Thus, our empirical estimation of the effects of these recommendations may be biased because of unobserved factors. We address these limitations by additionally conducting a controlled online experiment in which we randomly show some visitors pure retargeted recommendations (independent of generic recommendations) and other generic recommendations. We describe the online experiment in Section 5.2 of the paper.

## 4. Data Description

We needed data on at least two sessions for a visitor to identify his or her retargeted RP impressions. Accordingly, we examine the purchase behavior of only those visitors who visit the firm’s website for more than one session.<sup>11,12</sup> We have 70,881 sessions by 47,697 visitors with at least one product’s page view during the experiment. Of these sessions, 35,459 (50.03%) were for the control visitors, and the remaining were for the treated visitors. We conduct the balance check in Online Appendix A. We find statistically similar characteristics for the treated and control visitors, supporting our random assignment’s validity. These visi tors browsed 212,657 product pages, among which 52.2% were in treated sessions.<sup>13</sup>

Whereas 25% of the time visitors view one of the RPs after visiting the FP’s page in the treated sessions, they do so 17% of the time in the control sessions. The high percentage of RP views in the control sessions, when not explicitly shown on their FP’s pages, indicates that visitors know the relationship between FP and RP.

## 5. Analysis and Results

We estimate the relative value of retargeted over generic recommendations in two steps. First, we examine their effects on the different components of RP sales. Then, we estimate the impact on total product sales.

## 5.1. Effect of Recommendations on RP Sales

A visitor may choose to visit an RP’s page, and if it meets the visitor’s expectations, he or she may purchase it. Thus, a visitor’s path to purchase for an RP on the firm’s website is as follows. (i) The visitor receives an RP impression on an FP’s page; (ii) the visitor views the RP’s page on receiving an RP impression (RP View | RP Impression → click-through rate); and (iii) the visitor purchases the RP after its page view (RP Purchase | RP View → conditional conversion rate). The overall conversion rate (RP purchase | RP impression) is the multiplication of click-through and conditional conversion rates. The total RP sales are, in turn, the multiplication of the number of its impressions and the conversion rate.

In the following sections, we conduct separate analyses to estimate the relative effects of retargeted versus generic recommendations at different stages of the purchase funnel on the conversion rates and the number of RP impressions. Finally, we combine these results to estimate the effect of the two types of recommendations on daily RP sales.

5.1.1. Effect of Recommendations on RP Conversion Rates. This section examines the RP’s conversion rates conditional on its impression on the FP’s page. We study how the three types of RP conversion rates, as defined in Section 5.1, vary depending on the kind of visitor session (treated versus control session) and the nature of the RP impression (retargeted versus generic) for visitors in the early/late purchase funnel stage. In the following, we describe our data, present model-free evidence, conduct a regression analysis, and discuss the results.

5.1.1.1. Data Description. We organize each $\mathrm { F P ^ { \prime } s }$ page view in the visitor session data into four RP impressions. We have 846,804 RP impressions for $2 1 2 , 6 5 \dot { 7 }$ FP page views in our data. Of these, 441,849 (52.2%) are in the treated sessions. Among the RP impressions in the treated sessions, 33,703 (7.6%) are retargeted, and the rest are generic. We consider visitors’ FP page views to constitute RP impressions for the hidden RPs on the FP page. Among the RP impressions in the control sessions, 22,722 (5.6%) were retargeted. For the total RP impressions in our data, 700,533 (82.7%) are in the early purchase funnel stage, and the rest are in the late purchase funnel stage.

5.1.1.2. Model-free Evidence. Table 2 reports the summary statistics of the different conversion rates in the eight possible conditions of RP impressions, as described in Table 1. Several preliminary results emerge from the summary statistics. First, we find that explicit RP impressions on the $\mathrm { F P ^ { \prime } s }$ page (in treated sessions) increase the probability of the RP page view (click-through rates) in all circumstances. Second, explicit RP impressions have a lower conditional conversion rate (RPPur|RPView) in all circumstances. Overall, whereas showing generic $\mathrm { R P }$ impressions results in higher conversion rates in the early stages of the purchase funnel, showing retargeted RP impressions leads to lower conversion rates in both the early and late stages of the purchase funnel.

5.1.1.3. Empirical Specification and Identification. To examine the relative effect of retargeted over generic recommendations at different stages of the visitors’ purchase funnel, we separate the data into two subsamples: early and late purchase funnel stages. Then, we separately estimate the following fixed effects Logit Specification (1) for the two subsamples,<sup>14</sup>

$$
\begin{array}{l} Y _ {i j _ {i} v s t} ^ {\text {Stage}} = \beta_ {1} \operatorname{Rec} _ {i j _ {i} s t} + \beta_ {2} \operatorname{ReTar} _ {i j _ {i} s t} + \beta_ {3} \operatorname{Rec} _ {i j _ {i} s t} \times \operatorname{ReTar} _ {i j _ {i} s t} \\ + \sum_ {k} \delta_ {k} X _ {v c _ {i} s t} + \alpha_ {i} + \varepsilon_ {i j _ {i} v s t}; \end{array} \tag {1}
$$

where i denotes $\mathrm { R P } , j _ { i }$ denotes the FP of $i , v$ denotes visitors, s denotes visitor sessions, $c _ { \mathrm { i } }$ denotes the product subcategory o $^ { \mathrm { ~ ~ } } i ,$ and t denotes days. The unit of analysis is an impression of $\mathrm { R P } \ i$ i on the product page of $\mathrm { F P } j _ { i }$ in a session s by a visitor v on day t.

$Y _ { i j v s t } ^ { S t a g e }$ are the various outcome variables in the early $( Y _ { i j _ { i } v s t } ^ { E a \dot { r } l y } )$ and late stages $( Y _ { i j _ { i } v s t } ^ { L a t e } )$ . Outcome variables of interest are the different conversion rates in consumers’ path to purchase conditional on receiving the impression of $\mathrm { R P } i ,$ including $R P V i e w _ { i j _ { i } v s t } , R P P u r _ { i j _ { i } v s t } \mid R P V i e w _ { i j _ { i } v s t } .$ , and $R P P u r _ { i j _ { i } v s t }$ which measure click-through rate, conditional conversion rate, and (unconditional) conversion rate, respectively. $R e c _ { i j _ { i } \mathrm s t }$ is a dummy variable indicating whether the impression of RP i is visible on the page of $\mathrm { F P } j _ { i } \left( = 1 \right)$ or not. $R e T a r _ { i j _ { i } s t }$ is a dummy variable equal to one if the RP impression i is retargeted; otherwise, it is equal to zero. Equation (1) includes a set of control variables $X _ { v c _ { i } s t }$ related to RP i and visitor v that may be associated with conversion rates of $\mathrm { R P } \{ \cdot ^ { 1 5 } ( \mathrm { i } ) \ P o s _ { j _ { i } t }$ denotes the position of RP i on $\mathrm { F P ~ } j _ { i } \mathrm { \ p a g e }$ . Its value varies from one to four; one indicates the top position; (ii) $L A f f S c o r e _ { j _ { i } t }$ is the log of affinity score between RP i and FP $j _ { i } \rangle$ (iii) $N P F n l _ { v c _ { i } s t }$ is the number of purchase funnels for visitor v in subcategory $c _ { \mathrm { i } }$ before session $s ;$ (iv) $N S e s _ { v c _ { i } s t }$ is the number of sessions in which visitor v has viewed products in product subcategory $c _ { \mathrm { i } }$ before session $s ; ~ \mathrm { ( v ) }$ $C u m N P V i e w _ { v c _ { i } s t }$ is the cumulative number of products viewed by visitor v before session s in product subcategory $c _ { \mathrm { i } } \mathrm { : }$ and (vi) $N P C a t _ { v s t }$ denotes the number of product subcategories browsed by visitor v in session s.

Table 2. Model-Free Evidence on Conversion Rates

<table><tr><td rowspan="2">Purchase funnel stage</td><td rowspan="2">Rec. type</td><td rowspan="2">Conversion rates</td><td colspan="2">Control sessions</td><td colspan="2">Treated sessions</td><td rowspan="2">Diff. in means (t-stats)</td></tr><tr><td>Obs.</td><td>Mean (SD)</td><td>Obs.</td><td>Mean (SD)</td></tr><tr><td rowspan="6">Early</td><td rowspan="3">Generic</td><td>RPView</td><td>322,447</td><td>0.0450(0.2074)</td><td>345,626</td><td>0.0746(0.2628)</td><td>0.0296***(50.82)</td></tr><tr><td>RPPur | RPView</td><td>14,522</td><td>0.0746(0.2627)</td><td>25,786</td><td>0.0672(0.2504)</td><td>-0.0074**(-2.79)</td></tr><tr><td>RPPur</td><td>322,447</td><td>0.0034(0.0579)</td><td>345,626</td><td>0.0050(0.0706)</td><td>0.0017***(10.44)</td></tr><tr><td rowspan="3">Retargeted</td><td>RPView</td><td>12,853</td><td>0.1780(0.3825)</td><td>19,607</td><td>0.2222(0.4157)</td><td>0.0442***(9.66)</td></tr><tr><td>RPPur | RPView</td><td>2,288</td><td>0.1141(0.3180)</td><td>4,356</td><td>0.0769(0.2665)</td><td>-0.0372***(-5.05)</td></tr><tr><td>RPPur</td><td>12,853</td><td>0.0203(0.1411)</td><td>19,607</td><td>0.0171(0.1296)</td><td>-0.0032*(-2.11)</td></tr><tr><td rowspan="6">Late</td><td rowspan="3">Generic</td><td>RPView</td><td>59,786</td><td>0.0360(0.1863)</td><td>62,520</td><td>0.0567(0.2313)</td><td>0.0207***(17.19)</td></tr><tr><td>RPPur | RPView</td><td>2,153</td><td>0.0971(0.2961)</td><td>3,546</td><td>0.0626(0.2423)</td><td>-0.0345***(-4.78)</td></tr><tr><td>RPPur</td><td>59,786</td><td>0.0035(0.0590)</td><td>62,520</td><td>0.0036(0.0595)</td><td>0.0001(0.16)</td></tr><tr><td rowspan="3">Retargeted</td><td>RPView</td><td>9,869</td><td>0.2586(0.4379)</td><td>14,096</td><td>0.2692(0.4435)</td><td>0.0106+(1.82)</td></tr><tr><td>RPPur | RPView</td><td>2,552</td><td>0.2108(0.4080)</td><td>3,794</td><td>0.1790(0.3834)</td><td>-0.0318**(-3.16)</td></tr><tr><td>RPPur</td><td>9,869</td><td>0.0545(0.2270)</td><td>14,096</td><td>0.0482(0.2141)</td><td>-0.0063*(-2.20)</td></tr></table>

Note. Diff. in means � Treated – control.  
<sup>+</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01, \*\*\*p < 0.001.

Table 3 diagrammatically shows the effects of interest in terms of different coefficients in Equation (1). The relative benefit of retargeted (generic) recommendations over not showing it in the early (late) purchase funnel stage is estimated by $\beta _ { 1 } + \beta _ { 3 } \left( \beta _ { 1 } \right)$ . The relative effect of retargeted recommendations over generic recommendations in the early (late) purchase funnel stage is $\beta _ { 3 } .$ . Below, we discuss how we cleanly identify the interaction coefficients in Equation (1).

Unobserved factors may simultaneously correlate with key indicator variables (Rec and ReTar) and the dependent variable in Equation (1). We categorize the potential unobserved factors into the product-level and visitor-level factors.

The product-level factors include unobserved product characteristics (such as quality) and promotions that can increase the likelihood of its recommendations and purchase. For example, a popular product (RP or FP) is likely to have more page views and hence, is expected to be viewed with many other products. Consequently, popular products are more likely to appear as retargeted and generic impressions than unpopular ones. Moreover, popular products are likely to have higher sales than unpopular ones. In other words, the unobserved product level factors (such as popularity) may affect both the probability of its recommendations $( R e c = 1$ and $R e T a r = 1 )$ and purchase, making key independent variables (Rec and ReTar) endogenous in Equation (1). We account for the RP-level confounders by including the RP fixed effects (α<sub>i</sub>) in Equation (1). Variable Rec is uncorrelated to unobserved visitor-level factors because of the randomly assigned recommendations across visitors. However, variable Rec could be endogenous because of unobserved product level factors. After controlling RP fixed effects, variable Rec becomes exogenous to both visitor and product-level unobserved factors.

However, products may also receive time-varying shocks to their popularity/demand on the website, such as a celebrity or other endorsements and price/nonprice promotions. Such demand shocks could also affect product impressions and sales. To control the possible time-varying confounders, we include two time-varying variables, $P o s _ { j _ { i } t }$ $( \mathrm { R P ^ { \prime } s }$ position on the FP’s page) and $L \bar { A } f f S c o r e _ { j _ { i } t }$ (log of affinity score between RP and FP), as control variables in Equation (1). We also account for unobserved time-varying shocks to product demand with RP-day/FP-day/FP-RPday fixed effects and found qualitatively similar results.<sup>16</sup> Online Appendix D shows the estimates from the most exacting FP-RP-day fixed effect model.<sup>17</sup>

Visitor-level factors include visitor characteristics unobserved in our data that may increase their probability of receiving recommendations (Rec) and purchasing RP. For example, a more engaged and loyal customer may view more products and thus receive more RP impressions, and he or she is more likely to buy products. The random assignment of recommendations across visitors ensures that the population of visitors in the treated and control sessions is statistically similar; that is, the variable Rec is exogenous conditional on controlling for RP fixed effects in Equation $( 1 ) . ^ { 1 8 }$ However, visitor-level factors may still make the variable ReTar endogenous in Equation (1). The engaged visitors view/ cart/purchase more products. They could receive more retargeted RP impressions (Retar � 1). Because recommendations are based on co-views and co-purchases of the crowd, visitors with preferences similar to others have a higher likelihood of receiving retargeted RP impressions (ReTar � 1). In contrast, visitors with niche preferences are more likely to receive generic (but not retargeted) recommendations. We also account for the unobserved visitor characteristics by including the visitorand FP-RP-day fixed effect model in Equation (1) and find qualitatively similar results in Online Appendix E.

Table 3. Interpretation of Coefficients

<table><tr><td>Purchase funnel stage</td><td>RP impressions</td><td>Control sessions (Rec = 0)</td><td>Treated sessions (Rec = 1)</td><td>Effect of recommendations</td><td>Differential effect of retargeted recommendations</td></tr><tr><td rowspan="2">Early/late</td><td>Generic (ReTar = 0)</td><td>0</td><td> $\beta_1$ </td><td>Generic ( $\beta_1$ )</td><td> $\beta_3$ </td></tr><tr><td>Retargeted (ReTar = 1)</td><td> $\beta_2$ </td><td> $\beta_1 + \beta_2 + \beta_3$ </td><td>Retargeted ( $\beta_1 + \beta_3$ )</td><td></td></tr></table>

Notes. Early and late denote the early and late purchase funnel stages. Retargeted and generic, respectively, denote the retargeted and generi recommendations

However, we are interested in the coefficients of interaction terms in Equation (1). As long as the endogenous variables (ReTar) are included as covariates, the coefficients of their interaction with the variable Rec will be unbiased after controlling for RP fixed effects in Equation (1) (Kumar and Tan 2015).<sup>19</sup> The basic intuition for this result is that after partialing out the correlation with endogenous covariates, the remainder of Equation (1)’s error term is uncorrelated to the interaction terms. Besides, we control for visitors’ browsing behaviors by including a set of control variables $- N P F n l _ { v c _ { i } s t } , N S e s _ { v c _ { i } s t } ,$ $C u m N P \hat { V } i e w _ { v c _ { i } s t } ,$ and $N P C a t _ { v s t }$ (see the definitions presented above) — in Equation (1). These four variables can additionally control for the visitor-level confounding factors.

To summarize, the combination of random assignment of recommendations across visitors, the inclusion of endogenous variables as covariates, RP/RP-day/FPday/FP-RP-day fixed effects, visitor fixed effects, and observed product- and visitor-level control variables allow us to identify the unbiased coefficient estimates for the interaction terms in Equation (1).

5.1.1.4. Results and Discussion. Because we are interested primarily in the effects of retargeted/generic recommendations under different conditions and not individual coefficient estimates from Equation (1), we report these coefficients in Online Appendix C. We use these estimated coefficients to derive the point estimates and the significance levels for the effect of retargeted/ generic recommendations at the early/late purchase funnel stage and report them in Table 4.

The results in Table 4 are consistent mainly with the model-free evidence in Table 2. First, showing an RP impression on the FP’s page, compared with hiding it, increases the probability of the RP view (a higher clickthrough rate) because consumers can easily navigate from one product’s page to another (increased exposure and easier navigation). Showing related RPs on FPs’ pages can increase the probability of its view under all conditions, as shown in Column (1).

Second, we expect the conversion rates in treated sessions to be lower than those in control sessions. The rationale is as follows. When the FP’s page displays an RP, visitors may view it even when they are not seriously interested, because it requires little effort. In con trast, when an RP is hidden (not shown) on the FP’s page, visitors must search for the RP on the product category/subcategory pages that present many alternatives. In such cases, the visitors will view the RP only if they are seriously interested. Therefore, visitors would have a higher probability of purchasing the RP condi tional on viewing it (i.e., a higher conditional conversion rate) in control sessions than in treated sessions. However, once their preferences have narrowed down in the late purchase funnel stage, visitors may click on the retargeted RP impression (explored in the past session) only when they are seriously interested in buying it. These explain our results in Column (2) of Table 4 that an RP impression on the FP’s page leads to a lower conditional conversion rate in all circumstances except the retargeted RP impression in the late purchase funnel stage.

Finally, the increased click-through rates could be largely offset by their decreased conditional conversion rates, leading to the null effect on total conversion rates in all conditions except for the generic RP impression in the early stage of the purchase funnel. This fact explains our results in Column (3) of Table 4. Overall, only showing a generic RP impression for visitors in the early purchase funnel stage leads to higher RP conversion rates.

5.1.2. Effect of Recommendations on RP Impressions and Sales. In this section, we examine the impact of retargeted and generic recommendations on the number of daily RP impressions and sales in the early and late purchase funnel stages.

5.1.2.1. Data Description. Visitors received 22,051 unique RP impressions during the experiment period. Visitors may not receive the impressions of all RPs every day, because many RPs may not be recommended on FPs’ pages daily. On average, the impressions of an RP appear for 13 days during our 63-day experiment.

Table 4. Effects on Path-to-Purchase Conversion Rates

<table><tr><td>Purchase funnel stage</td><td>Rec. type</td><td>(1) Click-through rate (RPView | Impression)</td><td>(2) Conditional conversion rate (RPPur | RPView)</td><td>(3) Conversion rate (RPPur | Impression)</td><td>Diff. effect of retarget over generic rec.</td></tr><tr><td rowspan="2">Early</td><td>Generic</td><td>0.5340***</td><td>-0.1408+</td><td>0.4008***</td><td>-0.5856***</td></tr><tr><td>Retargeted</td><td>0.2883***</td><td>-0.5413***</td><td>-0.1848</td><td></td></tr><tr><td rowspan="2">Late</td><td>Generic</td><td>0.4763***</td><td>-0.4218+</td><td>0.0275</td><td>-0.1110</td></tr><tr><td>Retargeted</td><td>0.1012*</td><td>-0.2008</td><td>-0.0835</td><td></td></tr></table>

Notes. <sup>+</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Table 5. Summary Statistics of the Daily Number of RP Impressions and Sales

<table><tr><td rowspan="2">Purchase funnel stage</td><td rowspan="2">Rec. type</td><td rowspan="2">Daily impression or sales</td><td rowspan="2">Obs.</td><td colspan="2">Control sessions</td><td colspan="2">Treated sessions</td><td rowspan="2">Diff. in means (t-stats)</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td rowspan="4">Early</td><td rowspan="2">Generic</td><td>Impressions</td><td>299,788</td><td>1.0755</td><td>2.2126</td><td>1.1528</td><td>2.3758</td><td>0.0773***(13.04)</td></tr><tr><td>Sales</td><td>299,788</td><td>0.0037</td><td>0.0829</td><td>0.0058</td><td>0.1166</td><td>0.0022***(8.38)</td></tr><tr><td rowspan="2">Retargeted</td><td>Impressions</td><td>299,788</td><td>0.0430</td><td>0.4344</td><td>0.0655</td><td>0.5524</td><td>0.0225***(17.56)</td></tr><tr><td>Sales</td><td>299,788</td><td>0.0009</td><td>0.0422</td><td>0.0011</td><td>0.0501</td><td>0.0002*(2.09)</td></tr><tr><td rowspan="4">Late</td><td rowspan="2">Generic</td><td>Impressions</td><td>299,788</td><td>0.1994</td><td>0.6862</td><td>0.2085</td><td>0.6970</td><td>0.0091***(5.10)</td></tr><tr><td>Sales</td><td>299,788</td><td>0.0007</td><td>0.0412</td><td>0.00074</td><td>0.0379</td><td>0.00004(0.43)</td></tr><tr><td rowspan="2">Retargeted</td><td>Impressions</td><td>299,788</td><td>0.0330</td><td>0.2963</td><td>0.0471</td><td>0.3783</td><td>0.0141***(16.07)</td></tr><tr><td>Sales</td><td>299,788</td><td>0.0018</td><td>0.0560</td><td>0.0023</td><td>0.0656</td><td>0.0005**(3.03)</td></tr></table>

Notes. Diff. in means � Treated – control.  
<sup>+</sup>p < 0.1; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Visitors could see RP impressions under different conditions corresponding to the possible combinations of the two indicator variables $( \tilde { R e c } = 0 / 1 , R e T a r = 0 / 1 )$ for visitors in the early/late purchase funnel stage, as shown in Table 1. If an RP is viewed in at least one condition on a day, then the number of RP impressions for the remaining conditions is considered zero. This way, we can compare the differences in the number of RP impressions under different conditions. As a result, we have 299,788 RP-day impression values under each condition in our data.

5.1.2.2. Model-Free Evidence. Table 5 reports the summary statistics of the daily RP impressions and sales in the eight conditions of RP impressions, as described in Table 1. Several results emerge from the summary statistics. First, we find higher daily RP impressions (sales) in the treated than in control sessions in all cases, except for RP sales in generic recommendations in the late purchase funnel stage. Second, the number of RP impressions for both recommendations is higher in the early stage of the purchase funnel than in the late stage. Interestingly, we find a higher (lower) sales value for the retargeted (generic) recommendation in the late stage than in the early stage of the purchase funnel. Third, we find that generic recommendations are more (less) effective than the retargeted recommendation in the purchase funnel’s early (late) stage.

5.1.2.3. Empirical Specification. To estimate the effect of retargeted versus generic recommendations on the number of daily RP impressions and sales for the two subsamples (i.e., early and late purchase funnel stages) separately, we estimate the following econometric

specification,

$$
\begin{array}{r l} Y _ {i k t} ^ {\text {Stage}} & = \beta_ {1} \operatorname{Rec} _ {i k t} + \beta_ {2} \operatorname{ReTar} _ {i k t} + \beta_ {3} \operatorname{Rec} _ {i k t} \times \operatorname{ReTar} _ {i k t} + \alpha_ {i} \\ & + \varepsilon_ {i k t}; \end{array}\tag{2}
$$

where all variables have the same meaning as in Equation (1), and the unit of analysis in Equation (2) is the daily impression (sales) of an RP i under condition k. We have four conditions as four combinations of Rec 0/1 and ReTar 0/1. Dependent variables $Y _ { i k t } ^ { S t a g e }$ are $N R P I m p _ { i k t } ^ { S t a g e }$ or $N R P S a l e s _ { i k t } ^ { S t a g e }$ , which are the number of RP i impressions and sales on day t under condition k for the early and late stages (Stage � Early/Late) separately.

5.1.2.4. Results and Discussions. Online Appendix C reports the estimated OLS coefficients from Equation (2) with RP fixed effects for the daily number of RP impres sions and sales. We use these coefficient estimates to derive the point estimates and significance levels for the effects of retargeted/generic recommendations in the early/late purchase funnel stage on the number of RP impressions and sales as per Table 3. We first compare the daily RP impressions/sales under retargeted and generic recommendations with no recommendations. Then, we compare the relative benefit of retargeted over generic recommendations for different stages of the visitors’ purchase funnel. Because the total RP sales are the multiplication of its conversion rate and daily impressions, we also provide the estimates of RP conversion rates in Table 6 for easy comparison.

Table 6 reports several interesting findings. First, both types of recommendations in both stages result in more RP impressions than in the corresponding control sessions. This finding is per our expectations because visitors view more products in treated than in contro sessions. Second, whereas both recommendations result in higher RP sales than no recommendations in the early purchase funnel stage, only retargeted recommendations increase RP sales in the late purchase funnel stage. The higher number of daily RP impressions primarily drives the higher RP sales under recommendations. Whereas generic recommendations in the early purchase funnel stage positively affect conversion rate, the conversion rates are similar with and without recommendations in all other cases.

Table 6. Estimates for the Daily Number of RP Impressions and Sales

<table><tr><td rowspan="2">Purchase funnel stage</td><td rowspan="2">Rec. type</td><td colspan="3">Diff. Effect of Rec. over No Rec.</td><td>Diff. Effect of Retarget over Generic Rec.</td></tr><tr><td>Conversion rate (RPPur | Impression)</td><td>Daily RP impressions</td><td>Daily RP sales</td><td>Daily RP sales</td></tr><tr><td rowspan="2">Early</td><td>Generic</td><td>0.4008***</td><td>0.0773***</td><td>0.0022***</td><td>-0.0019***</td></tr><tr><td>Retargeted</td><td>-0.1848</td><td>0.0225**</td><td>0.0003**</td><td></td></tr><tr><td rowspan="2">Late</td><td>Generic</td><td>0.0275</td><td>0.0091***</td><td>0.00004</td><td>0.0004*</td></tr><tr><td>Retargeted</td><td>-0.0835</td><td>0.0141***</td><td>0.0005**</td><td></td></tr></table>

<sup>+</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Based on the point estimates in Table 6 and the average values for control sessions in Table 5, RP sales under retargeted recommendations compared with the control sessions increased by 33.3% (� 0.0003/0.0009) in the early and 33.3% (� 0.0006/0.0018) in the late stage of the purchase funnel.<sup>20</sup> The RP sales under generic recommendations compared with the control sessions increased by 59.5% (� 0.0022/0.0037) in the early purchase funnel stage.<sup>21</sup> Thus, although presenting generic recommendations in the early stage is beneficial, retargeted recommendations are better in the late purchase funnel stage.

## 5.1.2.5. Robustness Checks on RP Sales Analysis. In this section, we conduct several analyses to check the robustness of our results.

1. We include the following controls in our econometric specification to address the concern of endogenous retargeted (generic) recommendations:

a. Product, visitor, and time-related fixed effects model: We included visitor- and FP-RP-day fixed effects to account for the unobserved visitor, product, and time-invariant factors and find qualitatively similar results, indicating the robustness of the findings (Online Appendix D and E).

b. Control variables: We also included several control variables for other relevant factors affecting product sales, such as time-varying affinity scores and rank order of RPs.

2. We found similar results by including data for visitors with only one session. We assume that these visitors were in the early purchase funnel stage, and their RP impressions were generic (Online Appendix F.1).

3. We constructed visitors’ purchase funnel based on their observed behavior during our experiment. If a visitor has carted products in a subcategory before the experiment, our analysis would wrongly consider the visitor to be in the early purchase funnel stage. This possibility may be similar across the randomly assigned treated and control sessions, and thus its effect may cancel out in our analysis. However, we conduct additional analysis on a subsample of visitors who visit the firm’s website for the first time during the experiment. We have complete data on such visitors’ purchase journeys, so we accurately construct their purchase funnels. Online Appendix F.2 reports the results of our analysis on the subsample of new customers. We find that our results remain qualitatively similar.

4. We check the robustness of our findings by analyzing only those visitors who appear in both stages of the purchase funnel. We find qualitatively similar results in Online Appendix F.3.

5. The higher effectiveness of retargeted recommendations in the late purchase funnel stage could be because the retargeted products are carted (or highly similar to carted) products in the early stage. To rule out this alternative explanation, we check whether the higher benefit of showing retargeted versus generic recommendations in the late purchase funnel stage holds when we exclude the retargeted products that are carted or are highly similar to the carted products. We report the subsample analysis in Online Appendix F.4. We find qualitatively similar results, indicating that retargeting is the reason for higher RP sales.

6. We also conduct two falsification tests (placebo stud ies). We consider the randomly selected users as treated users in the first test and randomly selected recommendations as retargeted recommendations in the second test. We find qualitatively similar results in Online Appendix G.

## 5.2. Online Experiment

As stated in Section 3.4, we designed an online experiment to address the limitations of the field experiment.

5.2.1. Experimental Design. We created an experimental website for selling women’s tops. We randomly chose more than a hundred women’s tops from a live website.

The average price of these tops was \$38.06, comparable to that of women’s tops on the retailer’s website in the field setup. We displayed one RP on each FP’s page. We kept the experimental website’s web page organization, navigation across web pages, and product presentation identical to our field study website.

We conducted a two-phase experiment on Amazon MTurk. We invited MTurk workers to explore the experimental website in the first phase. Participants could add products that they found interesting to the shopping cart. If a participant carts at least one product in the first phase, he or she is considered in the late purchase funnel stage in the second phase of the online experiment. Otherwise, the participant is considered in the early stage. In the second phase of the online experiment, we show (hide) the RP on FP’s page for randomly selected 70 (30) percent of the participants in both purchase funnel stages.

5.2.2. Separate Algorithms for Generic and Retargeted Recommendation. We implemented the “Slope-One” algorithm, an item-based collaborative filtering algorithm, to identify the generic recommendation for each FP on our experimental website. This algorithm is widely used in practice and academic research (Adomavicius and Zhang 2016, Kokkodis 2021, Kokkodis and Ipeirotis 2021, Li et al. 2022). Following the recent study by Li et al. (2022), we collected evaluations of the products on our experimental website from 1,000 female Amazon MTurk workers in the United States. Specifically, we asked each participant to evaluate a random set of 20 products on a five-point scale from “Extremely dislike” (� 1) to “Extremely like” (� 5). We used these evaluations as inputs to the “Slop-One” algorithm to generate product similarity scores for each pair of products.

When a participant arrived at an FP’s page, we randomly generated a retargeted or generic recommendation for the FP with an equal chance. We randomly selected one of the products the participant viewed in the first phase as the retargeted recommendation on the FP’s page. We selected the product with the highest similarity score with the FP as the generic recommendation. If the participant viewed the product with the highest similarity in the first phase, we selected the product with the second-highest similarity score with the FP, and so on.<sup>22</sup> This way, we ensured that the participant did not view the generic RP in the first phase. Thus, we used two separate algorithms to generate the retargeted and generic RP and randomly displayed them on the FP’s page for treated participants.

5.2.3. Experiment Implementation. We first conducted two pilot studies, one at the behavioral laboratory of a U.S. university and another at Amazon MTurk. We sought detailed feedback from the pilot study participants to validate and improve the design of our main study.<sup>23</sup> Finally, we recruited 1,200 U.S. women from Amazon

MTurk to participate in the two-phase experiment. We allowed only workers in the CloudResearch Approved List to participate in the experiment to ensure high data quality. The workers were paid \$0.50 for completing each of the two phases of the experiment. To encourage participants to complete the two phases, they were eligible for a \$100 lottery upon completing the second phase.

In the first phase, we observed (i) the products explored by participants and (ii) whether they carted any products. Between three to seven days after the first phase, we invited participants who had viewed at least one product page in the first phase to participate in the second phase.<sup>24</sup> In the second phase, we randomly assigned 30% of participants to the control group and the remaining to the treatment group, independent of their purchase funnel stages. When a treated participant arrived at an FP’s page, the participant received either retargeted or a generic recommendation with equal chance. The participant could buy the products in the second phase.

We implemented an incentive alignment mechanism to ensure that participants bought only their desired products (Ha¨ubl and Trifts 2000, Li et al. 2022). Specifically, before exploring the website, participants were notified that “(1) At the end of the experiment, we will randomly select four participants to win the lottery of \$100 each. (2) If you win the lottery, you will get the product you purchased at your chosen address. We would also reimburse you the remaining amount � \$100 � the price of your purchased product. (3) If you win the lottery and have not purchased any product, we will reimburse you \$100. (4) Your chance of winning the lottery will not be affected by whether you make a purchase.”

At the beginning of the experiment, participants answered questions about their demographic information (such as age) and experience on Amazon MTurk (such as the number of years working on MTurk). We used these pieces of information to check the validity of our random assignment. After completing the experiment’s first phase, participants answered a few attention-check questions about their shopping experience on the website. We used only those participants who correctly answered the attention-check questions in our analysis.<sup>25</sup>

5.2.4. Data and Analysis. In the experiment’s first phase, 861 of the 1,200 Amazon MTurk participants viewed at least one product page on the experimental website. After excluding inattentive participants based on the attention-check questions, we had 768 valid participants in the second phase of the online experiment. Of the 768 participants, 196 (who did not cart any product in the first phase) were in the early purchase funnel stage, and the remaining 572 were in the late purchase funnel stage. Like our field analysis, we organized each FP’s page view as the RP impression.

We use Specification (1) with the RP fixed effect Logit model on the experimental data to estimate the impacts of retargeted versus generic recommendations on the RP purchase probability for participants at different purchase funnel stages.<sup>26</sup> To evaluate the effect of retargeted versus generic recommendations on the number of RP impressions and sales, we aggregate the number of impressions and sales of each RP under each condition and estimate Specification (2) with the RP fixed-effect model on the data. We report the estimated coefficients in Online Appendix H.4. We use these estimated coefficients to derive the point estimates and significance levels for the effect of retargeted/generic recommendations at the early/late purchase funnel stage. Table 7 reports the results.

Table 7 reveals several interesting findings. First, only showing a generic RP impression for participants in the early purchase funnel leads to a higher conversion rate. Second, treated participants received higher RP impressions than control participants in all cases. Lastly, although showing either type of recommendation results in higher RP sales than no recommendations in the early purchase funnel stage, retargeted recommendations are more beneficial for RP sales only in the late purchase funnel stage. These results indicate that generic (retargeted) recommendations have a higher effect on RP sales than retargeted (generic) recommendations in the early (late) purchase funnel stage. Overall, the results from the online experiment are consistent with our findings in the field setup (see Table 6).

5.2.5. Discussions and Additional Analysis. In the field experiment, the retargeted RP was the previously viewed product with a high-affinity score with the FP. But in the online experiment, we randomly chose the retargeted RP from the products that a customer viewed in the experiment’s first phase. The qualitatively similar results from the online experiment fulfilled two objectives. First, it identified that a consumer in the late purchase funnel stage purchased retargeted RPs primarily because of the retargeting (aligned to the consumer’s tastes) regardless of its affinity/similarity score (aligned to other consumers’ tastes). Second, it showed the robustness of our field experiment estimates to the possibility of endogeneity in the retargeted recommendations.

Furthermore, we conducted subsample analyses on the data of the online experiment by utilizing the variations in the affinity scores of the randomly chosen retargeted products with the FP in the second phase of the experiment. Specifically, we showed that the results remained statistically similar no matter whether the retargeted RPs had high- or low-similarity scores with the FP. We report the results in Online Appendix I.

The retargeted RPs are a consumer’s previously viewed products and thus aligned with the consumer’s preference, whereas generic recommended RPs are determined based on the average preference of the consumer population. A consumer may purchase a retargeted product because it is aligned with his or her taste, regardless of its similarity with the preferences of other consumers. Consumers may decide to buy a retargeted RP in the late purchase funnel stage because its repeated exposure could (i) increase the probability of them registering it, (ii) signal its higher relevance, and (iii) help them recall the previously explored product. These mechanisms indicate that the extent to which a retargeted RP is similar to the average preference of other consumers would not have an additional effect on consumers’ choices for the retargeted RP. For this reason, we observe similar results for the high and low-similarity score retargeted RPs.

## 5.3. Effect of Recommendations on the Total Focal and Recommended Product Sales

Visitors may purchase RP instead of FP when recommended on the FP’s page. From the managerial perspective, it is important to understand the effect of generic (retargeted) recommendations on the total FP and RP sales. Like Section 5.1, we estimate the effect of generic (retargeted) recommendations on the FP + RP conversion rates, the number of daily FP page impressions, and daily FP + RP sales.

We estimate the effect of generic/retargeted recommendations in the early/late purchase funnel stage on the conversion rate of FP + RPs given FP page view with the following specifications,

$$
\begin{array}{r} Y _ {j v s t} ^ {S t a g e} = \beta_ {1} R e c _ {j s t} + \beta_ {2} I n d \_ R e T a r _ {j s t} + \beta_ {3} R e c _ {j s t} \\ \times I n d \_ R e T a r _ {j s t} + \sum_ {k} \delta_ {k} X _ {v c _ {j} s t} + \alpha_ {i} + \varepsilon_ {i j v s t}; \end{array}\tag{3}
$$

where j denotes the FP, v denotes visitors, s denotes visi tor sessions, c denotes the product subcategory of j, and t denotes days. The unit of analysis is the product page j in a session s by a visitor v on day t. Dependent variable $Y _ { j v s t } ^ { S t a g e }$ is the conversion rate of (FP j + its RPs) after the FP’s page view in the early $( Y _ { j v s t } ^ { E a r l y } )$ and late stages $( Y _ { j v s t } ^ { L a t e } )$ Variable $R e c _ { j s t }$ denotes the indicator variable for RPs recommendations on the FP’s page. Variable Ind\_ $R e T a r _ { j s t }$ is an indicator variable equal to one if there is at least one retargeted RP on the FP’s page. Equation (3) includes a set of control variables $X _ { v c _ { j } s t }$ related to $\mathrm { F P } j$ and visitor v that may be associated with the purchase probability of FP and RPs on the $\mathrm { F P ^ { \prime } s }$ page: (i) $L A v e A f f S c o r e _ { j t }$ is the log of the average affinity score between FP and its four RPs; (ii) $N P F n l _ { v c _ { j } s t }$ is the number of purchase funnels for visitor v in product subcategory $c _ { j }$ before session $s ; ( \mathrm { i i i } ) N S e s _ { v c _ { j } s t }$ is the number of sessions in which visitor v has viewed products in product subcategory $c _ { j }$ before session s; (iv) $C u m N P V i e w _ { v c _ { j } s t }$ is the cumulative number of products viewed by visitor v before session s in product subcategory c<sub>j</sub>; and (v) $N P C a t _ { v s t }$ denotes the number of product categories browsed by visitor v in session s.

Table 7. Estimates Based on the Online Experiment

<table><tr><td rowspan="2"></td><td rowspan="2">Rec. type</td><td colspan="4">Diff. effect of rec. over no rec. and diff. effect of retarget over generic rec.</td></tr><tr><td>Conversion rate (RPPur | Impression)</td><td>RP impressions</td><td>RP sales</td><td>Diff. in Sales</td></tr><tr><td rowspan="2">Early</td><td>Generic</td><td>3.3567**</td><td>2.0619*</td><td>0.7216**</td><td>-0.4227*</td></tr><tr><td>Retargeted</td><td>-0.1236</td><td>0.8041**</td><td>0.2990*</td><td></td></tr><tr><td rowspan="2">Late</td><td>Generic</td><td>0.1213</td><td>4.1237*</td><td>0.1959</td><td>0.5361*</td></tr><tr><td>Retargeted</td><td>-0.1108</td><td>3.6186***</td><td>0.7320***</td><td></td></tr></table>

<sup>+</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

We further estimate the effect of retargeted/generic recommendations in the early/late purchase funnel stage on the number of daily FP impressions and $\mathrm { F P + }$ RPs sales with the following specification,

$$
\begin{array}{r} Y _ {j k t} ^ {S t a g e} = \beta_ {1} R e c _ {j k t} + \beta_ {2} I n d \_ R e T a r _ {j k t} + \beta_ {3} R e c _ {j k t} \\ \times I n d \_ R e T a r _ {j k t} + \alpha_ {i} + \varepsilon_ {j k t}; \end{array}\tag{4}
$$

where all variables have the same meaning as in previous specifications. The unit of analysis in Equation (4) is the daily FP j impressions under condition k. Our conditions correspond to four combinations of Rec 0/1 and ReTar 0/1 for the early/late purchase funnel stage. Dependent variables $Y _ { j k t } ^ { S t a g e }$ is $N F P I m p _ { j k t } \mathrm { o r } N F P R P S a l e s _ { j k t } ,$ indicating the number of FP j impressions and FP + RPs sales on day t in the early/late purchase funnel stage, respectively.

As before, we use Table 3 to derive the point estimates and levels of significance for the effects of our interest from the estimated coefficients in specifications (3) and (4) for conversion rates and sales of FP + RPs and report them in Table $8 . ^ { 2 7 }$ The results in Table 8 are similar to that in Table 6, suggesting that our main findings for RP sales apply to the total FP + RP sales: generic (retargeted) recommendations are more beneficial in the early (late) purchase funnel stage.

## 6. Simulation Analysis: Sales Gains from Replacement of Recommendations

In this section, we conduct a simulation study to estimate the sales gain from replacing a generic (retargeted) RP with a retargeted (generic) RP on the FP’s page in the late (early) purchase funnel stage per our findings.

We identify a suitable retargeted (generic) alternative for the existing recommendations in the following manner. The retailer’s recommendation system identifies the top 15 products with the highest affinity scores and in the product category of the FP but recommends only the top four products on the $\mathrm { F P ^ { \prime } s }$ page. Based on his or her past views, we label each of the 15 products as retargeted (generic) RPs for a visitor. Thus, alternative retargeted (generic) recommendations are available in the 5th- to 15th-ranked RPs to replace the existing top four ranked RPs. If a visitor is in the late (early) stage, we replace the generic (retargeted) RP in the top four RPs with the 5thto 15th-ranked retargeted (generic) RP with marginally lower affinity scores.

Next, we compute the increase in the total FP + RP sales with such RP replacements. We use right-hand side variables for the replaced RP in Specification (1) to predict the counterfactual RP and FP purchase probabilities for each FP page view in our data. Then, we multiply these purchase probabilities with the prevailing FP and RP price to compute the total FP and RP sales during the experiment. We considered Logit, fixed-effect Logit, linear probability, and fixed-effect linear probability models. Using k-fold cross-validation, we found that the Logit model had a better prediction performance.<sup>2</sup> Therefore, we performed the counterfactual simulation using the Logit model.

We conduct simulations for four alternative replacement strategies: replace when the eligible RP is in the fourth rank; third and fourth rank; second, third, and fourth rank; and first to the fourth ranks. Because the higher-ranked RPs have higher affinity scores with the FP, replacing eligible higher-ranked RPs with lowerranked RPs may lower RP sales. Table 9 reports the results of the four alternative simulations.

Table 8. Estimates for Total FP and RP Sales

<table><tr><td rowspan="2">Purchase funnel stage</td><td rowspan="2">Rec. type</td><td colspan="3">Diff. Effect of Rec. over No Rec.</td><td>Diff. Effect of Retarget over Generic Rec.</td></tr><tr><td>Conversion rate (FP + RPs Purchase | FP impressions)</td><td>Daily FP impressions</td><td>Daily FP + RPs sales</td><td>Daily FP + RPs sales</td></tr><tr><td rowspan="2">Early</td><td>Generic</td><td>0.0614*</td><td>0.0253***</td><td>0.0031***</td><td>-0.0015*</td></tr><tr><td>Retargeted</td><td>-0.0517</td><td>0.2261***</td><td>0.0016***</td><td></td></tr><tr><td rowspan="2">Late</td><td>Generic</td><td>-0.0767</td><td>-0.0028*</td><td>-0.0009*</td><td>0.0028***</td></tr><tr><td>Retargeted</td><td>-0.0784</td><td>0.0139***</td><td>0.0019***</td><td></td></tr></table>

<sup>+</sup>p < 0.10; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Table 9. Simulation Analysis: Sales Gains from Replacing Recommendations

<table><tr><td>RP replacement strategy</td><td>Number of eligible replacements</td><td>Original (RPs + FP) sales in U.S. $</td><td>FP sales gain in U.S. $ after replacement</td><td>RP sales gain in U.S. $ after replacement</td><td>Total sales gain in U.S. $ after replacement</td><td>Sales gain in % after replacement</td></tr><tr><td>Fourth-ranked RP</td><td>8,726</td><td>160,072</td><td>-341</td><td>4,370</td><td>4,028</td><td>2.52%</td></tr><tr><td>Third- and fourth-ranked RPs</td><td>15,369</td><td>160,072</td><td>-523</td><td>5,630</td><td>5,107</td><td>3.19%</td></tr><tr><td>Second-, third-, and fourth-ranked RPs</td><td>21,599</td><td>160,072</td><td>-1,019</td><td>5,229</td><td>4,209</td><td>2.63%</td></tr><tr><td>First- to fourth-ranked RPs</td><td>28,765</td><td>160,072</td><td>-1,381</td><td>2,676</td><td>1,295</td><td>0.81%</td></tr></table>

The retailer could gain up to a 3.19% increase in FP + RPs sales over the original total sales of \$160,072 during the experiment period under different replacement strategies. We find a significantly lower increase (0.81%) in total product sales by replacing all four eligible RPs, because losses from lower affinity scores may offset the gains from changing the type of recommendations. The simulation results show that replacing the third- and fourth-ranked eligible RPs with a minor redesign in the recommendation systems can result in an economically significant (3.19%) increase in total product sales.

Because firms can access visitors’ session data on their websites, they can construct visitors’ purchase funnels and classify visitors’ recommendations into retargeted and generic. Therefore, our findings can improve sales when combined with the available collaborative filterbased recommendation systems.

## 7. Discussion and Conclusions 7.1. Contributions

We introduce “retargeted” recommendations in the recommendation literature by borrowing the concept of “retargeting” from the retargeted ad literature (Lambrecht and Tucker 2013). Retargeting in the two contexts is similar because both refer to a user’s previously viewed ad or recommendation. However, whereas retargeted ads affect the ad conversion rates, retargeted recommendations could affect both the RP conversion rate and the number of RP impressions. Therefore, findings in the display ad literature provide limited guidance regarding product recommendations. Our study is perhaps the first to distinguish retargeted and generic recommendations and compare their relative effects on users’ path to recommended products’ purchase, that is, RP impressions and conversion rates.

We find that generic recommendations are more beneficial in the early stage of the purchase funnel, but retargeted recommendations are more effective at the later stage. The main cause for increased RP sales under recommendations is the increased RP visibility but not RP conversion rates, except for generic recommendations in the early purchase funnel stage. These underlying mechanisms that drive the effects of (retargeted/ generic) recommendations are not yet documented in the extant literature.

## 7.2. Managerial Implications

Existing item-based collaborative filtering (CF) systems use product co-views and co-purchases as main inputs. Our results suggest that item-based CF recommendation systems’ performance could be improved by considering visitors’ situational factors, such as what products a visi tor has previously viewed and where the visitor is in his or her purchase funnel. Online retailers can infer the purchase funnel stage of their consumers based on the history of online browsing (e.g., whether they carted a product or not). Online retailers can also classify a recommendation into retargeted (and generic) based on whether (or not) users have viewed the recommended product in their previous session. For a visitor in the late (early) stage, the retailer should replace the original generic (retargeted) RP in the top four RPs with lowerranked retargeted (generic) RP with marginally lower affinity scores.

Our simulation results show that replacing the thirdand fourth-ranked eligible RPs, as per our findings, can result in overall higher total product sales. In this strategy, the increase in product sales because of appropriate retargeted/generic recommendation in a purchase funnel stage, on average, exceeds the sales loss due to showing lower affinity score products. The online retailers can compute the net sales gains from such replacement in each case and decide whether to follow this policy. In other words, the retailer can realize higher sales by following case-based replacement rather than the uniform replacement strategy.

## 7.3. Generalizability of Findings

Our findings apply to the item-based CF recommendation systems, the most widely used recommendation system in practice users (Lin et al. 2017; Adomavicius et al. 2018; Adomavicius et al. 2019; Kumar and Hosanagar

2019; Lee and Hosanagar 2019, 2021; Li et al. 2022; Peng and Liang 2023; Wan et al. 2023). Our results are for apparel, accessories, and home goods, which account for a large e-commerce market share.<sup>29</sup> We found qualitatively similar results with a different CF algorithm (slopeone algorithm) in our online experiment, which supports the generalizability of our findings to other item-based CF algorithms. Thus, our results on a popular recommendation system used in such a large market segment are academically and managerially significant. Future research can examine whether our findings still hold for other categories of recommendation algorithms, such as modelbased recommendation algorithms.

## 7.4. Limitations and Future Research Directions

The retargeted and generic recommendations are not exogenously generated in the field experiment, which could bias our estimated effects. We estimated many exacting fixed effect specifications and conducted several falsification tests to support our results. We also conducted an online experiment to show qualitatively similar results. Still, we caution readers about our estimates. We hope future studies design a randomized experiment to estimate the unbiased effects of retargeted/generic recommendations in different purchase funnel stages.

Using a consumer’s observable states to proxy consumers’ latent purchase funnel stage is widely used in current studies (Bleier and Eisenbeiss 2015, Sahni et al. 2019, Gopalakrishnan and Park 2021, Sun et al. 2022) because it can provide actionable managerial takeaways. Incorporating latent consumer states is an exciting direction for future research. Future research could use more precise modeling of the consumer purchase funnel stage.

Our paper separately estimates the relative benefit of retargeted versus generic recommendations for consumers in the early and later purchase funnel stages. Future research could extend our work to explore the effect of retargeted versus generic recommendations unconditional on the purchase funnel stage by exogenously manipulating consumers’ purchase funnel stages.

## Acknowledgments

The authors acknowledge generous research support from the Public Utility Research Center (PURC) of the University of Florida, Hi!PARIS Fellowship, HEC Foundation, and the Leavey School of Business of Santa Clara University. The authors thank the senior editor, associate editor, and the three anonymous reviewers for their constructive and insightful suggestions.

## Endnotes

<sup>1</sup> These recommendation systems are classified as item-based collaborative filtering recommendation systems. Many prestigious technology firms (such as IBM) have developed commercial itembased collaborative filtering recommendation systems that are widely used on the prominent retailers’ websites.

<sup>2</sup> If a product recommended by a collaborative filtering recommendation engine has been previously viewed by the user, such a generic recommendation would also be a retargeted recommendation for the user. However, the effect of a recommended product that a user has previously viewed may differ from the effect of a recommended product that the user has never viewed before.

<sup>3</sup> Sources: https://experienceleague.adobe.com/docs/commercemerchant-services/product-recommendations/admin/type.html?lang=en and https://www.oracle.com/cx/marketing/digital-intelligence customer-recommendations/.

4 According to “Recommendation Engine Market Report 2021–2028,” the global recommendation engine market size was valued at \$1.77 bil lion in 2020. The collaborative filtering category, which accounted fo more than 40.0% of revenue in 2020, is expected to maintain its lead throughout the forecast period. https://www.grandviewresearch.com/ industry-analysis/recommendation-engine-market-report.

<sup>5</sup> Recommendation algorithms based on such co-view (co-purchase) relationships between products belong to item-based collaborativ filtering recommendation algorithms.

<sup>6</sup> Coremetrics digital recommendation is a successful and widely used commercial item-based collaborative filtering recommendation system of IBM.

<sup>7</sup> We used the default formula of the Coremetrics recommendation system for recommending products. Item-based CF algorithms compute the similarity scores between products to identify what product to recommend on the focal product’s page. Although different item-based CF algorithms may use different implementations or formulas to compute the similarity scores between products, all item-based CF algorithms, including the formula used by the IBM Coremetrics recommendation engine, share the same key idea.

<sup>8</sup> We borrow the retargeted recommendations from the online display ad literature where showing an ad that a user has previously viewed is called a retargeted ad (Lambrecht and Tucker 2013).

<sup>9</sup> Kumar and Hosanagar (2019) showed an example of a focal women’s top and its recommended top being shown together in the search result page (for the keyword search “Women’s top”) and th main page of the Women’s top product subcategory on www. macys.com.

<sup>10</sup> The recommendation engine can use the IP address and cookies to identify whether multiple sessions come from the same machine and thus can consistently assign the visitors to the same version as their first visit.

<sup>11</sup> We conduct additional analysis by including visitors with only one session in Online Appendix F.1.

<sup>12</sup> Our data are truncated at the start of the experiment. This may result in some inaccuracies in the formation of visitors’ purchase funnels and designation of retargeted recommendations. However, these inaccuracies are equally likely in the treated and control visitors because of the random assignment of visitors to sessions in our experiment. We examine this issue in greater detail in the robustness section and Online Appendix F.2.

<sup>13</sup> We include all visitors (those only in the early purchase funnel stage and those in both stages) in our analysis. We check the robustness of our findings by analyzing visitors only in both stages of the purchase funnel. We find qualitatively similar results in Online Appendix F.3.

<sup>14</sup> We note that such “subgroup” analyses are consistent with the retargeting ad studies of Bleier and Eisenbeiss (2015) and Sahni et al. (2019).

<sup>16</sup> We also conduct additional analysis by including product-related characteristics as control variables. We find qualitatively similar results, which indicates that our results are robust. Note that the product-related time-invariant and time-varying variables (e.g., price, promotions, quality, reviews) are partially or all dropped with the product-day fixed effects.

<sup>17</sup> Estimates for FP-day and RP-day fixed effects are available on request from the authors.

<sup>18</sup> We consider a customer as a loyal customer if he or she has more than three visitor sessions (75th percentiles in the distribution of total number of sessions by a visitor). In Online Appendix A, we show that the distribution of loyal (i.e., high-value) customers is statistically indistinguishable in the treated and control sessions.

<sup>19</sup> The detailed proof of the same is provided in the appendix in Kumar and Tan (2015).

<sup>20</sup> Where 0.0009 and 0.0018 are the average RP sales in Table 5 under retargeted recommendations in control sessions in the early and late purchase funnel stages, respectively.

<sup>21</sup> Where 0.0037 is the average RP sales in Table 5 under generic recommendations in control sessions in the early purchase funnel stage.

<sup>22</sup> In only 3.4% of the cases, RP of the highest similarity score with the FP was viewed in the first phase. We reran our analysis after excluding these cases and found qualitatively similar results.

<sup>23</sup> We describe our pilot studies in Online Appendix H.1.

<sup>24</sup> We excluded the participants who did not view any product page in the first phase because it was impossible to generate retargeted recommendations for such participants in the second phase.

<sup>25</sup> We provide more details about the instructions and the screenshot of the page that participants saw for the two-phase online experiment in Online Appendix H.

<sup>26</sup> Similar to our field setup, our analysis relies on the user’s endogenous selection of the purchase funnel stage rather than exogenously varying the purchase funnel stage in the online experiment. We note that our conditional analyses based on the purchase funnel stage (or subsample analysis) are also consistent with the estimation approaches of the retargeting ad studies of Bleier and Eisenbeiss (2015) and Sahni et al. (2019).

<sup>27</sup> The coefficient estimates of Equations (3) and (4) are available on request from the authors.

<sup>28</sup> We report the prediction performance in Online Appendix J.

29 Apparel and accessories sales account for 20.2% of total retail e-Commerce sales (ranked 2nd) and will grow by 18.9% (ranked 1st). Accessed on https://www.grandviewresearch.com/industry analysis/recommendation-engine-market-report.

## References

Abhishek V, Fader P, Hosanagar K (2012) Media exposure through the funnel: A model of multi-stage attribution. Preprint, submit ted October 8, https://dx.doi.org/10.2139/ssrn.2158421.

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and pos sible extensions. IEEE Trans. Knowl. Data Eng. 17(6):734–749.

Adomavicius G, Zhang J (2016) Classification, ranking, and top-K stability of recommendation algorithms. INFORMS J. Comput. 28(1):129–147.

Adomavicius G, Bockstedt J, Curley S, Zhang J (2019) Reducing recommender systems biases: An investigation of rating display designs. Management Inform. Systems Quart. 43(4):1321–1341.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2018) Effects of online recommendations on consumers’ willingness to pay. Inform. Systems. Res. 29(1):84–102.

Basilico J, Hofmann T (2004) Unifying collaborative and content based filtering. Proc. Twenty-First Internat. Conf. on Machine Learn ing (PMLR, New York), 65–72.

Batmaz Z, Yurekli A, Bilge A, Kaleli C (2019) A review on deep learning for recommender systems: challenges and remedies Artif. Intell. Rev. 52(1):1–37.

Bleier A, Eisenbeiss M (2015) Personalized online advertising effec tiveness: The interplay of what, when, and where. Marketin Sci. 34(5):669–688.

Choi H, Mela CF, Balseiro S, Leary A (2019) Online display advertising markets: A literature review and future directions. Inform. Systems Res. 31(2):556–575.

De P, Hu Y, Rahman MS (2010) Technology usage and online sales An empirical study. Management Sci. 56(11):1930–1945.

Ghose A, Todri V (2016) Toward a digital attribution model: Measuring the impact of display advertising on online consumer behavior. Management Inform. Systems. Quart. 40(4):889–910.

Goldenberg J, Oestreicher-Singer G, Reichman S (2012) The quest for content: How user-generated links can facilitate online exploration. J. Marketing. Res. 49(4):452–468.

Gopalakrishnan A, Park Y-H (2021) The impact of coupons on th visit-to-purchase funnel. Marketing Sci. 40(1):48–61.

Ha¨ubl G, Trifts V (2000) Consumer decision making in online shopping environments: The effects of interactive decision aids. Marketing Sci. 19(1):4–21.

Hoban PR, Bucklin RE (2015) Effects of Internet display advertising in the purchase funnel: Model-based insights from a random ized field experiment. J. Marketing. Res. 52(3):375–393.

Kokkodis M (2021) Dynamic, multidimensional, and skillset-specific rep utation systems for online work. Inform. Systems Res. 32(3):688–712.

Kokkodis M, Ipeirotis PG (2021) Demand-aware career path recommendations: A reinforcement learning approach. Management Sci. 67(7):4362–4383.

Kumar A, Hosanagar K (2019) Measuring the value of recommenda tion links on product demand. Inform. Systems Res. 30(3):819–838.

Kumar A, Tan Y (2015) The demand effects of joint product adver tising in online videos. Management Sci. 61(8):1921–1937.

Lambrecht A, Tucker C (2013) When does retargeting work? Information specificity in online advertising. J. Marketing Res. 50(5): 561–576.

Lee D, Hosanagar K (2019) How do recommender systems affect sales diversity? A cross-category investigation via randomized field experiment. Inform. Systems Res. 30(1):239–259.

Lee D, Hosanagar K (2021) How do product attributes and reviews moderate the impact of recommender systems through purchase stages? Management Sci. 67(1):524–546.

Li X, Grahl J, Hinz O (2022) How do recommender systems lead to consumer purchases? A causal mediation analysis of a field experiment. Inform. Systems Res. 33(2):620–637.

Lin Z, Goh KY, Heng CS (2017) The demand effects of product recommendation networks: an empirical analysis of network diversity and stability. Management Inform. Systems Quart. 41(2): 397–426.

Linden G, Smith B, York J (2003) Amazon. com recommendations: Item to-item collaborative filtering. IEEE Internet Comput. 7(1):76–80.

Lops P, Gemmis MD, Semeraro G (2011) Content-based recommender systems: State of the art and trends. Recommender Sys tems Handbook (Springer, Boston), 73–105.

Oestreicher-Singer G, Sundararajan A (2012) The visible hand? De mand effects of recommendation networks in electronic markets. Management Sci. 58(11):1963–1981.

Oestreicher-Singer G, Libai B, Sivan L, Carmi E, Yassin O (2013) The network value of products. J. Marketing 77(3):1–14.

Peng J, Liang C (2023) On the differences between view-based and purchase-based recommender systems. Management Inform. Systems Quart., ePub ahead of print May 22, https://doi.org/10.25300/ MISO/2022/17875

Resnick P, Iacovou N, Suchak M, Bergstrom P, Riedl J (1994) Grouplens: An open architecture for collaborative filtering of netnews. Proc. 1994 ACM Conf. Comput. Supported Cooperative Work (ACM, New York), 175–186.

Sahni NS, Narayanan S, Kalyanam K (2019) An experimental investigation of the effects of retargeted advertising: The role of fre quency and timing. J. Marketing Res. 56(3):401–418.

Sarwar BM, Karypis G, Konstan JA, Riedl J (2001) Item-based collab orative filtering recommendation algorithms. Proc. 10th Internat. Conf. on World Wide Web (ACM, New York), 285–295.

Shen Q, Miguel Villas-Boas J (2018) Behavior-based advertising. Management Sci. 64(5):2047–2064.

Strong EK (1925) The Psychology of Selling and Advertising (McGraw-Hill, New York).

Sun C, Adamopoulos P, Ghose A, Luo X (2022) Predicting stages in omnichannel path to purchase: A deep learning model. Inform. Systems Res. 33(2):429–445.

Thorat PB, Goudar R, Barve S (2015) Survey on collaborative filtering, content-based filtering and hybrid recommendation system. Int. J. Comput. Appl. 110(4):31–36.

Todri V, Ghose A, Singh PV (2020) Trade-Offs in online advertising: Advertising effectiveness and annoyance dynamics across the purchase funnel. Inform. Systems Res. 31(1):102–125.

Venkatraman V, Dimoka A, Pavlou PA, Vo K, Hampton W, Bollinger B, Hershfield HE, Ishihara M, Winer RS (2015) Predicting advertising success beyond traditional measures: New insights from neurophysiological methods and market response modeling. J. Marketing Res. 52(4):436–452.

Wan XS, Kumar A, Li X (2023) How do product recommendation help consumers search? Evidence from a field experiment Management Sci. Forthcoming

Zhang Y, Li B, Luo X, Wang X (2019) Personalized mobile targeting with user engagement stages: Combining a structural hidden markov model and field experiment. Inform. Systems Res. 30(3):787–804.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
