---
otero_id: 6198
otero_key: "XHKGEXGS"
title: "An Empirical Study of Free Product Sampling and Rating Bias"
authors: "Zhijie Lin; Ying Zhang; Yong Tan"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0801"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.215.17.190] On: 26 March 2019, At: 23:27 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/XHKGEXGS/fulltext/images/d52645c1f0c8f2358fd688da1e022ab34b0ddb8a071b938e92be59ad034294ed.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## An Empirical Study of Free Product Sampling and Rating Bias

Zhijie Lin, Ying Zhang, Yong Tan

To cite this article: Zhijie Lin, Ying Zhang, Yong Tan (2019) An Empirical Study of Free Product Sampling and Rating Bias. Information Systems Research

Published online in Articles in Advance 05 Mar 2019

https://doi.org/10.1287/isre.2018.0801

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Empirical Study of Free Product Sampling and Rating Bias

Zhijie Lin,<sup>a,b</sup> Ying Zhang,<sup>c</sup> Yong Tan<sup>d</sup>

<sup>a</sup> School of Business, Nanjing University, Nanjing 210093, China; <sup>b</sup> School of Economics and Management, Tsinghua University, Beijing 100084, China; <sup>c</sup> School of Computing, National University of Singapore, 117418 Republic of Singapore; <sup>d</sup> Michael G. Foster Schoo of Business, University of Washington, Seattle, Washington 98195

Contact: dr.zhijie.lin@gmail.com, http://orcid.org/0000-0003-0770-2390 (ZL); zhangying@u.nus.edu (YZ); ytan@uw.edu, http://orcid.org/0000-0001-8087-3423 (YT)

Received: September 16, 2016 Revised: April 15, 2017; March 8, 2018 Accepted: April 12, 2018 Published Online in Articles in Advance: March 5, 2019

https://doi.org/10.1287/isre.2018.080

Copyright: © 2019 INFORMS

Abstract. Free product sampling has increasingly become a popular promotional strategy and served as a new mechanism of product review generation in e-commerce. We empirically analyze how a product’s engagement in free product sampling affects the product’s review rating, and we also examine important contingent factors of product pricing and product popularity. Using a rich data set from Taobao.com and multiple identification strategies and estimation methods, we find that engaging in free product sampling increases product rating by 1.1%. We argue that it is consumers’ reciprocal behavior of giving higher ratings as a return to retailers’ beneficial actions that causes rating bias. We further find that the bias would be larger with higher original price but smaller with larger price discount and higher product popularity. Our empirical findings provide important contributions to the literature on product sampling and word-of-mouth and offer critical managerial implications to online retailers, rating system designers, and consumers.

History: Paul Pavlou, Senior Editor; Xue Bai, Associate Editor.

Funding: This work was supported in part by the National Natural Science Foundation of China [Grants 71872080, 71502079, and 71729001].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2018.0801.

Keywords: product sampling • product trial • rating bias • product review • word-of-mouth • electronic commerce • econometric analysis

## 1. Introduction

Online product reviews have long become an important information source for consumer decision making (Chevalier and Mayzlin 2006, Chen and Xie 2008, Duan et al. 2008). According to the recent Local Consumer Review Survey (BrightLocal 2016), 84% of consumers trust online reviews as much as a personal recommendation, and 58% of consumers say that the star rating of a business is most important. Given that consumers have much reliance on product reviews, the value of consumer reviews, especially in terms of ratings, mostly lies in the effectiveness in reflecting consumers’ truthful expressions of their evaluations of the products (Wang et al. 2018).

Electronic commerce (e-commerce) sites are one of the common contexts in which product reviews are generated. Typically, textual reviews and numerical ratings of a product can be generated after consumers’ purchase and usage of the product, which has become the most dominant mechanism of product review generation in e-commerce. Recently, free product sampling has become an additional mechanism. Free product sampling is a popular promotional strategy that has long been employed by firms to boast product sales (Schultz et al. 1998). This strategy was first used for physical goods (e.g., food and cosmetics) in the offline context (Marks and Kamins 1988, Heiman et al. 2001 Bawa and Shoemaker 2004) and then information goods (e.g., software and movie) in the online context (Chellappa and Shivendu 2005, Cheng and Liu 2012, Lee and Tan 2013, Niculescu and Wu 2014), and recently physical goods in e-commerce. Many e-commerce firms (e.g., Taobao.com, JD.com, and YHD.com)<sup>1</sup> have increasingly launched their own platforms for product sampling promotions. Typically, e-commerce retailers will provide some number of free samples of a sampling product<sup>2</sup> during the product sampling promotion. Consumers can then apply for a free sample, and successful applicants can receive it. After consumers ex perience the product, as a return, they need to write a review for the product to be integrated with the existing product reviews.

Prior research on free product sampling has documented the existence of reciprocity in consumer behavior (Bawa and Shoemaker 2004). When consumers are given a product for free, they may have feelings of obligation to behave more friendly in response to retailers’ beneficial actions (Cialdini 1993, Fehr and Gachter ¨ 2000). Given that providing review ratings is a typical way for consumers to respond to retailers in e-commerce, we thus conjecture that, in the context of e-commerce product sampling, consumers who receive a free product are likely to behave more friendly by providing a higher rating for the product when writing the review, which may eventually result in deviations in the overall product rating from its “true” level. Consequently, the usefulness and value of product ratings could be undermined. Moreover, prior literature has also argued that the extent of reciprocity is contingent upon the imputed value of the benefit received (Gouldner 1960), which suggests that rating deviations are likely to depend on product characteristics, such as pricing (e.g., list price and price discount) and popularity, that could signal the value of a product. As free product sampling is getting more and more popular in e-commerce, deviations in product ratings are likely to have significant consequences. Therefore, we are interested in understanding how free sampling promotion of a product affects the product’s rating and the roles of important contingent factors, including (1) product pricing (i.e., list price and price discount) and (2) product popularity.

We answer these questions using a rich panel data set from the largest e-commerce website in China, Taobao. com, on 2,524 products from January 2016 to March 2016. Empirically identifying the impact of product sampling on product rating is challenging due to the potential endogeneity issue of sampling promotion of a product. We thus address the endogeneity using multiple identification strategies. Furthermore, we conduct various additional tests to rule out alternative explanations and check the robustness of our research findings.

We find robust evidence that conducting free sampling promotion for a product increases the product’s rating. Specifically, our estimate shows that, on average, a product’s engagement in free product sampling increases the product’s rating by 1.1%. Our additional investigations of the contingent factors find that the impact of free sampling on product rating would be stronger with higher product list price but weaker with larger price discount and higher product popularity.

This research contributes to the literature in several ways. First, we enrich and extend the product sampling literature by studying free product sampling of physical goods in e-commerce. Second, we contribute to the word-of-mouth (WOM) literature by empirically documenting the existence of rating bias due to free product sampling. Third, this research adds insights to the literature on product sampling and WOM by studying and validating several important contingent factors. The notable findings from this research also offer important implications for managerial practices.

## 2. Theoretical Development

## 2.1. Related Literature

Free product sampling or trial is a common and important promotional tool that has long been employed by retailers to allow consumers to try the product and thereby motivate them to make a purchase (Biswas et al. 2010). This marketing strategy is effective as it helps consumers learn about a product directly to reduce consumers’ perceived quality uncertainty (Shoemaker and Shoaf 1975, Rothschild and Gaidis 1981, Goering 1985, Jamieson and Bass 1989). Free product sampling has always been considered more effective than other marketing strategies (Smith and Swinyard 1983, Ailloni-Charas 1984, Jain et al. 1995, Smith 1993).

This effective marketing strategy has attracted considerable research effort (Scott 1976; Shiv and Nowli 2004; Nowlis and Shiv 2005; Wadhwa et al. 2008; Biswas et al. 2010, 2014), which can be generally classified into two streams. The first stream of studies focused on how product sampling affects consumers beliefs and attitudes toward the product (Marks and Kamins 1988), brand evaluations (Kempf and Smith 1998), product quality expectation (Goering 1985), product value perception (Büyükkurt 1986), product preference (Biswas et al. 2010, 2014), product satisfaction (Mano and Oliver 1993), purchase intentions (Smith 1993, Heiman and Muller 1996, Heiman et al. 2001), and repeat purchase intentions (Scott 1976). Other than focusing on these psychological outcomes, the second stream of studies examined how product sampling affects consumers’ actual behaviors in terms of product adoption and purchase (Shoemake and Shoaf 1975, Jamieson and Bass 1989, Mizik and Jacobson 2004, Montoya et al. 2010), product choice (Nowlis and Shiv 2005, Shiv and Nowlis 2004), and reward-seeking (Wadhwa et al. 2008), and also economic outcomes such as product sales (Hahn et al 1994), brand sales (Bawa and Shoemaker 2004), and firm profits (Cheng and Liu 2012). Although research on free product sampling has been abundant, existing studies have only focused either on product sampling of physical goods in the offline context (e.g., Heiman et al. 2001. Marks and Kamins 1988. Bawa and Shoemaker 2004) or that of information goods in the online context (e.g., Chellappa and Shivendu 2005, Cheng and Liu 2012, Lee and Tan 2013, Niculescu and Wu 2014). There has been little research on product sampling of physical goods in e-commerce. Furthermore, the product sampling literature has not examined the potential relationship between free product sampling and bias in product reviews or WOM.

While research on the connection between product sampling and WOM has been absent, extensive research effort has been devoted to examining the role of WOM (Dellarocas 2003, Mayzlin 2006, Chen and Xie 2008, Godes and Mayzlin 2009, Li and Hitt 2010, Mudambi and Schuff 2010). For instance, prior studies have widely documented that WOM has critical impacts on consumer decision making (Pavlou and Dimoka 2006, Goh et al. 2013, Xu and Zhang 2013), product sales (Chevalier and Mayzlin 2006, Clemons et al. 2006, Liu 2006, Duan et al. 2008, Forman et al. 2008, Chintagunta et al. 2010, Zhu and Zhang 2010, Gu et al. 2012, Lin 2014), and firm performance (Antweiler and Frank 2004, Das and Chen 2007, Tirunillai and Tellis 2012, Chen et al. 2014).

Given the influential role of WOM, its value largely depends on how effective it can deliver true information regarding consumers’ product evaluations. However unfortunately, the WOM literature has documented some factors and mechanisms that could cause biases in WOM, or more specifically, product rating (e.g., Li and Hitt 2008, Wu and Huberman 2008, Godes and Silva 2012, Lin and Heng 2015). For instance, Li and Hitt (2008) analyzed book review data from Amazon to show the existence of self-selection bias due to the fact that early and later consumers have different preferences about the quality of a product, and readers of early reviews may not successfully correct for these differences when making purchase decisions. Moreover, Wu and Huberman (2008) uncovered that later reviewers may be affected by previous reviews to have a trend-following tendency. Godes and Silva (2012) explored the dynamic aspects of product ratings and argued that later consumers have decreasing ability to assess similarity with past reviewers and then will have more purchase errors. Interestingly, through the lens of expectation-confirmation theory (Oliver 1977, 1980), Lin and Heng (2015) also analyzed the dynamic aspects of product ratings and discovered that extremely high ratings are more likely to attract negative reviews subsequently due to consumers’ higher perceived impact of reviewing, which may result in an underreporting bias.

In addition to these dynamic aspects, some studies also reported social factors that could lead to biases in WOM (e.g., Schlosser 2005, Moe and Trusov 2011, Wang et al. 2018). For instance, Schlosser (2005) demonstrated that users may adjust their attitudes in the presence of social concerns (e.g., self-presentational concerns). Moe and Trusov (2011) identified that there are substantial social dynamics in a rating environment, and consumers’ ratings can be affected by others’ ratings. Recently, Wang et al. (2018) studied the impacts of online friend relationship on product ratings and uncovered that rating similarity between friends is significantly higher after the formation of the friend relationships. The authors claimed that observational learning (Zhang 2010) and peer pressure (Mas and Moretti 2009) should be the underlying influencing mechanisms.

Given that free product sampling has become increasingly popular and served as a new mechanism to generate WOM in e-commerce, how the use of free product sampling by retailers has brought changes to WOM thus becomes an important research gap in the literature that our study attempts to address. In essence, our study differs from related prior studies by empirically analyzing the impact of free product sampling on WOM in terms of product rating and examining the moderating roles of product pricing (i.e., list price and price discount) and product popularity. We seek to make significant theoretical and practical contributions through these important investigations.

## 2.2. Research Model and Hypotheses

On the basis of the discussions above, we present our research model in Figure 1. We first study the main effect of free product sampling promotion engagement on product rating. After establishing this relationship, we then investigate the moderating effects of product list price, product price discount, and product popularity. We next develop our research hypotheses.

Social psychology literature has long documented the existence of reciprocity as a social rule about repaying (Cialdini 1993). In many social contexts, if individuals receive benefits for free from others, they may have feelings of obligation to behave more friendly or cooperative in response to others’ beneficial actions (Gouldner 1960). In the context of e-commerce free product sampling, reciprocity may occur for two reasons. First, from consumers’ perspective, retailers purpose of conducting free product sampling is to seek to gather favorable feedback (in terms of higher product ratings) from consumers, which may further increase product sales. In other words, consumers should be aware of this social norm that free sample recipients are expected to provide higher product ratings. As psychology literature has widely suggested that individuals tend to comply with social norms (Ajzen and Fishbein 1972), we posit that consumers who receive free samples are likely to be reciprocal and give higher product ratings. Second, individuals are reciprocal sometimes because they seek to build a continuing social relationship for future benefits (Blau 1964). Specifically, free sampling is not a one-off interaction between retailers and consumers, as retailers can conduct free sampling promotions and consumers can apply for free samples again in the future. Therefore, consumers are likely to give higher ratings to help retailers, expecting retailers to be reciprocal as well by increasing consumers’ chance of receiving free samples in future promotions. In sum, we hypothesize that free sampling is likely to lead to consumer reciprocity and increase product ratings.

Hypothesis 1 (H1). Free product sampling promotion engagement has a positive impact on product rating.

Prior literature on reciprocity has also stated that the extent of reciprocity is contingent upon the imputed value of the benefit received (Gouldner 1960). This suggests that product characteristics that may influence consumers’ perception of received value are likely to moderate the relationship between free sampling and product ratings. First, we argue that list price is likely to enhance the positive effect of free sampling on product ratings. Marketing studies have shown that list price has been serving as an indicator of product value (Zeithaml 1988). Because consumers receive the product for free, the higher list price of the product, the higher value and benefit consumers may perceive. Consequently, consumers are likely to become more reciprocal and give even higher ratings.

Figure 1. Research Model  
![](/api/attachments/XHKGEXGS/fulltext/images/f32f5e5e5fc5461d287f2d36f6076d7d0872dab3be14e384245fd7dac24e088d.jpg)

Hypothesis 2 (H2). The positive impact of free product sampling promotion engagement on product rating will be stronger with a higher product list price.

Second, we posit that price discount is likely to “discount” the positive impact of free sampling on product ratings. Specifically, product list price (without discount) is the amount of money consumers need to pay to obtain the product through regular purchase, and it also indicates the value and benefit consumers perceive through free sampling. However, human judgments are always determined by “reference points” used (Mussweiler 2003). Thus, a larger discount, which implies that consumers now can pay less to obtain the product, may cause free sample recipients to perceive less value and benefit, compared with other consumers who obtain the product through regular purchase. As a result, they may engage in less reciprocal behavior and the rating increase may be less salient.

Hypothesis 3 (H3). The positive impact of free product sampling promotion engagement on product rating will be weaker with a larger product price discount.

Third, product popularity may have a moderating effect as well. A more popular product is generally more recognized and favored by the public, perhaps because the product is physically more up-to-date or has a higher level of excellence (Tucker and Zhang 2011). The possession of a more popular object may also allow individuals to engage in social activities more easily as individuals could have more common discussion topics (Schwartz et al. 2006). Given that a more popular product could offer more physical and social benefits to consumers, consumers may thus become more reciprocal and give higher ratings if they obtain more popular products through free sampling

Hypothesis 4 (H4). The positive impact of free product sampling promotion engagement on product rating will be stronger with a higher product popularity.

## 3. Data

To empirically address the above research questions, we obtain data from the largest e-commerce website in China, Taobao.com. Taobao has about 500 million registered users, more than 60 million daily active users, and more than 800 million products (Taobao 2017). Taobao is an independent e-commerce platform that facilitates the transactions between individua retailers/stores and consumers. That is, there are numerous online stores on Taobao, and each store itself can decide what products to sell in the store. Thus, it is possible that a product can be sold in multiple stores at the same time. This thus provides us a convenient setting to observe an identical pair of products with one engaging in product sampling but not the other. Thus, we would be able to construct a “control group”

of nonsampling products for identification purposes. Typically, each product has an independent web page, displaying product information such as product title, original list price, discounted price, product review, past sales, delivery cost, after-sales service, and payment mode.

Taobao has started providing product sampling services by launching the largest e-commerce product sampling center in China in 2011, i.e., Taobao sampling center (http://try.taobao.com). A typical sampling promotion campaign follows these five steps. First, a retailer submits a sampling campaign application to the sampling center regarding her product. Second, the sampling center approves the application and places the target product in the “Coming soon” section, including information such as product title, product list price, sampling size (i.e., the number of free samples provided), and promotion starting date. This step is commonly done several days before the start of the actual promotion. Third, the sampling center moves the target product to the “Ongoing” section when the promotion starts and allows Taobao users to apply for a free sample of the target product. This step lasts for 7 days, after which the target product will be moved to the “Sampling review” section. Fourth, the sampling center and retailer select the successful applicants and deliver a free sample to each of them. Fifth, after these successful applicants receive and try the free sample, they are required to write a review for the product within 20 days. These reviews will be integrated with the existing product reviews on the product web page in the corresponding store. Figures 2–4 provide illustrations of the product sampling center, product web page, and product review. Typically, a complete free sampling campaign lasts for about a month. The typical number of free samples provided of a product could range from one (mostly) to hundreds.

We design a Python-based crawler for data collection. We record products that appear in the “Coming soon” section, which are sampling products but have not yet engaged in sampling promotion. For each of these sampling products on the same day, we manually identify a certain number of stores selling this identical, but nonsampling, product. The number of identical nonsampling comparison products mostly range from 1 to 3, which depends on the availability on Taobao. The crawler will be executed on a daily basis to go through the web pages of all the recorded products collect all observable product information. Overall, our final unbalanced panel-level data set includes 120,820 observations for 2,524 products (i.e., 26,259 observations

(Ongoing) (Coming soon) (Sampling review)  
Figure 2. (Color online) Product Sampling Center  
![](/api/attachments/XHKGEXGS/fulltext/images/11ebbc87eb0d3a3eb272fdd0b9cd0f144c41b7dfde86e34dd026aa364f0e6c48.jpg)

很高兴抽到试用，面膜怠装有档次，面膜的尺寸是我用过的最大的，上至额头，下包住整个下巴，很服帖，精华液充足，补水效果非常好

![](/api/attachments/XHKGEXGS/fulltext/images/4893bb8199d07cfde33f56fb8e32c679b1118593ee4e1dd528658253fe6f5857.jpg)

![](/api/attachments/XHKGEXGS/fulltext/images/66f65713a00048876c0b94b04bc8a1623f842a4fb055e6378cfb2bbb1f0322a3.jpg)

Figure 3. (Color online) Product Web Page  
(Product name) 茜茜雨露面膜纳豆正品女十深层补水保湿清洁滋润提亮肤色收缩毛孔  
![](/api/attachments/XHKGEXGS/fulltext/images/35286017dccec337f1a3469f152c5a2ad60d01c19717f85d93a236f4e7be9210.jpg)

Figure 4. (Color online) Product Review  
(Product detail)(Product review)  
![](/api/attachments/XHKGEXGS/fulltext/images/5019bd599893b05ac553b3a9d049b7ed14224e048642a3eee6579cb555e10f49.jpg)

化妆品净含量：30g

![](/api/attachments/XHKGEXGS/fulltext/images/657d0c8a6788398609d22c41fb21c7c651c53b80b7aa83108504f28ef69fa973.jpg)

第一次抽到试用，，兴奋死。，一直都很倒霉。.，谢谢卖家给这次机会。，一直没时间，昨天数了一片，挺好的，很多精华液。。最主要的是我是敏感肌肤，没过敏！！！祝生意兴隆！

化妆品净含量：30g

for 536 sampling products and 94,561 observations for 1,988 nonsampling products), spanning from January to March 2016. On the basis of Taobao’s categorization, all the products are grouped into nine categories, including (1) apparels, (2) household items, (3) home appliances, (4) digital products, (5) skincare products, (6) makeups and perfumes, (7) maternal and child products, (8) health food, and (9) other products.

## 4. Model and Analysis 4.1. Empirical Model

On the basis of this panel-level data set, we conduct our analysis at the product-day level to construct all our model variables. Let subscript i denote each individual product in our data set, and subscript t denote each day. To investigate the impact of product sampling engagement on product rating, our independent variable, $S P _ { i t } ,$ is a binary indicator for product sampling engagement. That is, $S P _ { i t } = 1$ if product i has already engaged in product sampling promotion on day $t ,$ zero otherwise. Our dependent variable, $R R _ { i t } ,$ indicates the product i review rating on day t. Finally, the control variables are gathered from those identified in prior literature (e.g., Chevalier and Mayzlin 2006, Lin et al. 2017) and from the available information in our data set. Specifically, we include control variables at the individual product, product category, and time unit levels: (1) product original list price<sup>4</sup> $\dot { ( L P _ { i t } ) } ,$ , (2) product price discount<sup>5</sup> $( D C _ { i t } ) , \mathsf { \bar { ( 3 ) } }$ product review volume $( R V _ { i t } )$ (4) product past sales<sup>6</sup> $( P \bar { S } _ { i t } ) ,$ , (5) free delivery $( F D _ { i t } ) ,$ , (6) after-sales service<sup>8</sup> $( A S _ { i t } ) ,$ ), (7) payment mode<sup>9</sup> $( P M _ { i t } ) ,$ (8) product category dummies (C ), and (9) time dummies at the daily level (T ). Control variables 1–7 are included because they are all product attributes displayed on each product’s web page on Taobao, which can be easily observed by consumers to influence their decision making. Control variables 8 and 9 are included to capture the fixed effects at the product category and time unit levels.

To address our first research question, we model the influence of $S P _ { i , t - 1 }$ on $R R _ { i t } ,$ to allow for a lagged effect from free product sampling to consumers’ provision of review ratings, and also to avoid potential simultaneity issues.<sup>10</sup> The panel-level linear model is specified in Equation (1):

$$
\begin{array}{r} R R _ {i t} = \beta_ {1} S P _ {i, t - 1} + \beta_ {2} L P _ {i t} + \beta_ {3} D C _ {i t} + \beta_ {4} R V _ {i t} + \beta_ {5} P S _ {i t} \\ + \beta_ {6} F D _ {i t} + \beta_ {7} A S _ {i t} + \beta_ {8} P M _ {i t} + C _ {i} \gamma + T _ {t} \omega \\ + \alpha_ {i} + \varepsilon_ {i t}, \end{array}
$$

(1)

where $\beta , \gamma ,$ , and ω are the model coefficients, $\alpha _ { i }$ captures unobserved product-specific effect, and $\varepsilon _ { i t }$ indicates the residual random error term. Noteworthy, as products in our sample all come from different stores, $\alpha _ { i }$ in the above product-level (and thus accordingly, store-level) model can capture unobserved store-specific effect as well. Tables 1 and 2 present the descriptive statistics and the correlation matrix of our model variables based on all the 2,524 products. The descriptive statistics of these variables based on sampling and nonsampling products separately are presented in the online appendix.

## 4.2. Result

We first estimate a fixed effects (FE) model of product review rating (RR) on all the control variables. As reported in Table 3, column (1), various control variables have significant relationships with product review rating. Specifically, consumers prefer lower product price and larger price discount; thus, LP has a negative relationship, whereas DC has a positive relationship with RR. Next, both RV and PS have a negative relationship with RR. This might be because more product sales, and thus more product reviews made by consumers, are likely to impede the increase in product review rating, as a product needs to attract more con sistent positive reviews in order to enjoy rating increase given a larger volume of reviews. Lastly, more payment modes PM provide more convenience to consumers purchases, and thus are likely to result in a higher level of consumer satisfaction and perhaps higher rating consequently. Overall, these significant relationships imply that our control variables have good explanatory power. We also estimate a random effects (RE) model of RR on these control variables and find similar results in Table 3, column (2).

Table 1. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>RR (Review rating)</td><td>4.300</td><td>1.560</td><td>0.000</td><td>5.000</td></tr><tr><td>SP (Product sampling engagement)</td><td>0.938</td><td>0.241</td><td>0.000</td><td>1.000</td></tr><tr><td>LP (Product list price, in thousands)</td><td>0.805</td><td>1.389</td><td>0.008</td><td>13.900</td></tr><tr><td>DC (Product price discount, in thousands)</td><td>0.387</td><td>0.899</td><td>0.000</td><td>11.120</td></tr><tr><td>RV (Product review volume, in thousands)</td><td>2.470</td><td>11.764</td><td>0.000</td><td>284.491</td></tr><tr><td>PS (Product past sales, in thousands)</td><td>0.456</td><td>2.154</td><td>0.000</td><td>71.834</td></tr><tr><td>FD (Free delivery)</td><td>0.052</td><td>0.223</td><td>0.000</td><td>1.000</td></tr><tr><td>AS (Number of after-sales services)</td><td>0.976</td><td>0.488</td><td>0.000</td><td>7.000</td></tr><tr><td>PM (Number of payment modes)</td><td>3.862</td><td>0.480</td><td>1.000</td><td>5.000</td></tr></table>

Notes. Number of observations, 120,820; number of sampling products, 536; number of nonsampling products, 1,988; number of days, 66. All variables are at the product-day level.

Table 2. Correlation Matrix

<table><tr><td colspan="2">Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1</td><td>RR (Review rating)</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>SP (Product sampling engagement)</td><td>0.033</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>LP (Product list price)</td><td>0.011</td><td>0.003</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>DC (Product price discount)</td><td>0.037</td><td>-0.001</td><td>0.847</td><td>—</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>RV (Product review volume)</td><td>0.074</td><td>0.006</td><td>-0.034</td><td>-0.019</td><td>—</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>PS (Product past sales)</td><td>0.074</td><td>0.014</td><td>-0.046</td><td>-0.032</td><td>0.652</td><td>—</td><td></td><td></td><td></td></tr><tr><td>7</td><td>FD (Free delivery)</td><td>0.044</td><td>-0.002</td><td>-0.061</td><td>-0.040</td><td>-0.026</td><td>-0.031</td><td>—</td><td></td><td></td></tr><tr><td>8</td><td>AS (Number of after-sales services)</td><td>-0.001</td><td>0.002</td><td>0.056</td><td>0.001</td><td>-0.012</td><td>-0.000</td><td>-0.014</td><td>—</td><td></td></tr><tr><td>9</td><td>PM (Number of payment modes)</td><td>0.035</td><td>0.208</td><td>0.067</td><td>0.049</td><td>0.009</td><td>0.021</td><td>0.004</td><td>-0.128</td><td>—</td></tr></table>

Beyond these control variables, we then estimate a full FE model by further including the independent variable of product sampling engagement SP. We summarize the results in Table 3, column (3). As indicated, the estimated coefficient of SP, 0.046 (±0.007), is positive and statistically significant, suggesting a positive relationship with RR. In addition to the full FE model, we further estimate a full RE model of RR on all the independent and control variables and summarize the results in Table $^ { 3 , }$ column (4). Consistently, the estimated coefficient of SP, 0.045 (±0.007), is almost identical to that of the FE estimate. The Hausman test result $( \chi ^ { 2 } = 1 0 6 . 1 1 , p = 0 . 0 0 5 5 )$ shows that RE estimates would be inconsistent as the unobserved productspecific effect $\alpha _ { i }$ is correlated with the explanatory variables. Thus, we consider the results of the FE model in column (3) as our preferred baseline results. On the basis of this baseline model, we further estimate and report the elasticity of product rating, RR, with respect to product sampling engagement, SP. As indicated in column (3), the estimated elasticity suggests that a product’s engagement in product sampling promotion increases the product’s review rating by 1.1%.

Table 3. Result: Free Product Sampling Engagement

<table><tr><td>Variable</td><td>FE control (1)</td><td>RE control (2)</td><td>FE full (3)</td><td>RE full (4)</td></tr><tr><td rowspan="2">SP (Product sampling engagement)</td><td></td><td></td><td>0.046***</td><td>0.045***</td></tr><tr><td></td><td></td><td>(0.007)</td><td>(0.007)</td></tr><tr><td rowspan="2">LP (Product list price)</td><td>-0.044**</td><td>-0.032**</td><td>-0.036*</td><td>-0.027*</td></tr><tr><td>(0.020)</td><td>(0.016)</td><td>(0.020)</td><td>(0.016)</td></tr><tr><td rowspan="2">DC (Product price discount)</td><td>0.016**</td><td>0.018***</td><td>0.015**</td><td>0.016**</td></tr><tr><td>(0.007)</td><td>(0.007)</td><td>(0.006)</td><td>(0.006)</td></tr><tr><td rowspan="2">RV (Product review volume)</td><td>-0.029***</td><td>-0.004*</td><td>-0.029***</td><td>-0.004*</td></tr><tr><td>(0.004)</td><td>(0.002)</td><td>(0.004)</td><td>(0.002)</td></tr><tr><td rowspan="2">PS (Product past sales)</td><td>-0.006**</td><td>-0.013***</td><td>-0.006**</td><td>-0.013***</td></tr><tr><td>(0.002)</td><td>(0.002)</td><td>(0.002)</td><td>(0.002)</td></tr><tr><td rowspan="2">FD (Free delivery)</td><td>-0.044</td><td>-0.028</td><td>-0.034</td><td>-0.017</td></tr><tr><td>(0.032)</td><td>(0.031)</td><td>(0.032)</td><td>(0.031)</td></tr><tr><td rowspan="2">AS (Number of after-sales services)</td><td>-0.032**</td><td>-0.027*</td><td>-0.044***</td><td>-0.038**</td></tr><tr><td>(0.015)</td><td>(0.015)</td><td>(0.016)</td><td>(0.015)</td></tr><tr><td rowspan="2">PM (Number of payment modes)</td><td>0.043***</td><td>0.045***</td><td>0.049***</td><td>0.050***</td></tr><tr><td>(0.013)</td><td>(0.012)</td><td>(0.013)</td><td>(0.013)</td></tr><tr><td rowspan="2">Constant</td><td>4.403***</td><td>4.501***</td><td>4.336***</td><td>4.439***</td></tr><tr><td>(0.054)</td><td>(0.113)</td><td>(0.056)</td><td>(0.114)</td></tr><tr><td rowspan="2">Elasticity of SP</td><td></td><td></td><td>0.011***</td><td>0.011***</td></tr><tr><td></td><td></td><td>(0.002)</td><td>(0.002)</td></tr><tr><td>Category dummies</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Time dummies</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Number of sampling products</td><td>536</td><td>536</td><td>536</td><td>536</td></tr><tr><td>Number of nonsampling products</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td></tr><tr><td>Number of products</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td></tr><tr><td>Number of observations</td><td>120,820</td><td>120,820</td><td>117,798</td><td>117,798</td></tr><tr><td>Hausman test</td><td></td><td></td><td colspan="2"> $\chi^2=106.11, p=0.0055$ </td></tr><tr><td>Within  $R^2$ </td><td>0.0305</td><td>0.0301</td><td>0.0296</td><td>0.0292</td></tr><tr><td>Between  $R^2$ </td><td>0.0052</td><td>0.0146</td><td>0.0052</td><td>0.0151</td></tr><tr><td>Overall  $R^2$ </td><td>0.0031</td><td>0.0129</td><td>0.0032</td><td>0.0133</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## 4.3. Identi<sup>fi</sup>cation

The above result in Table 3, column (3), shows that SP indeed has a positive relationship with RR, suggesting the existence of rating bias due to free product sampling. However, the above analysis may be subject to endogeneity issue as SP could be endogenous for reasons such as the omission of relevant important factors. We thus apply multiple identification strategies to address the potential endogeneity concern. For ease of reference, Table 4, column (1), presents the baseline results from Table 3, column (3). For brevity, from this point onward, we only report the major variables of interest.

As discussed above, our unique setting allows us to simultaneously observe the “treatment” group (i.e., sampling products) and “control” group (i.e., identical but nonsampling products). Moreover, for each product in the treatment group, we are also able to observe the period before (i.e., before the “Ongoing” period starts) and after (i.e., after the Ongoing period starts) a product engages in product sampling promotion. Thus, we can exploit differences across products’ sampling engagement decisions and across timing differences in sampling starting dates to use a difference-in-differences (DID) model estimation approach. On the basis of our treatment group and constructed control group, we estimate the DID model:

$$
\begin{array}{r} R R _ {i t} = \beta_ {1} I S \_ S P _ {i} \times A F \_ S P _ {i t} + \beta_ {2} I S \_ S P _ {i} + \beta_ {3} A F \_ S P _ {i t} \\ + \beta_ {4} L P _ {i t} + \beta_ {5} D C _ {i t} + \beta_ {6} R V _ {i t} + \beta_ {7} P S _ {i t} + \beta_ {8} F D _ {i t} \\ + \beta_ {9} A S _ {i t} + \beta_ {1 0} P M _ {i t} + C _ {i} \gamma + T _ {t} \omega + \alpha_ {i} + \varepsilon_ {i t}, \end{array}\tag{2}
$$

where $I S \_ S P _ { i }$ is a binary indicator for product sampling engagement decision, with one indicating sampling product and zero otherwise. $A F _ { - } S P _ { i t }$ is a binary indicator for the post sampling period of product i and its comparison product on day $t . A F _ { - } S P _ { i t }$ equals one for the day when the product i sampling promotion starts and all the subsequent days and equals zero otherwise. On the basis of Equation $( 2 ) , \beta _ { 1 }$ is the DID estimator which represents the impact of sampling promotion on product rating.

Our data set has the treatment group of 536 sampling products, and 1,988 identical nonsampling products. Thus, we can make use of the 1,988 nonsampling products to properly construct the control group. Our first control group can be constructed by randomly selecting 536 nonsampling products.<sup>11</sup> We estimate the DID model based on the treatment group and this control group, and summarize the results in Table $^ { 4 , }$ column (2). The positive and significant coefficient of $I S \_ S P \times A F \_ S P , \mathrm { { 0 . 0 4 5 \ ( \pm 0 . 0 1 7 ) } }$ , which is close to the baseline estimate of SP, also suggests that sampling promotion has a positive impact on product rating.

Table 4. Identification: Free Product Sampling Engagement

<table><tr><td>Variable</td><td>Baseline (1)</td><td>DID random (2)</td><td>DID PSM one-to-one without replacement (3)</td><td>DID PSM one-to-one with replacement (4)</td><td>DID PSM two-nearest neighbors with replacement (5)</td><td>DID PSM three-nearest neighbors with replacement (6)</td><td>DID PSM one-to-one without replacement parallel trend (7)</td></tr><tr><td>SP (Product sampling engagement)</td><td>0.046*** (0.007)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IS_SP × AF_SP (DID treatment effect)</td><td></td><td>0.045*** (0.017)</td><td>0.036** (0.018)</td><td>0.042** (0.019)</td><td>0.048*** (0.017)</td><td>0.039** (0.016)</td><td>0.090*** (0.015)</td></tr><tr><td>Constant</td><td>4.336*** (0.056)</td><td>4.320*** (0.070)</td><td>4.570*** (0.073)</td><td>4.598*** (0.078)</td><td>4.526*** (0.070)</td><td>4.614*** (0.066)</td><td>4.613*** (0.074)</td></tr><tr><td>Control variables Product-specific trends</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included Included</td></tr><tr><td>Number of sampling products</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td></tr><tr><td>Number of nonsampling products</td><td>1,988</td><td>536</td><td>536</td><td>413</td><td>693</td><td>887</td><td>536</td></tr><tr><td>Number of products</td><td>2,524</td><td>1,072</td><td>1,072</td><td>949</td><td>1,229</td><td>1,423</td><td>1,072</td></tr><tr><td>Number of observations</td><td>117,798</td><td>51,844</td><td>52,379</td><td>46,343</td><td>59,599</td><td>68,842</td><td>52,379</td></tr><tr><td>Within R2</td><td>0.0296</td><td>0.0260</td><td>0.0287</td><td>0.0290</td><td>0.0289</td><td>0.0305</td><td>0.0296</td></tr><tr><td>Between R2</td><td>0.0052</td><td>0.0014</td><td>0.0025</td><td>0.0021</td><td>0.0024</td><td>0.0027</td><td>0.0003</td></tr><tr><td>Overall R2</td><td>0.0032</td><td>0.0005</td><td>0.0006</td><td>0.0006</td><td>0.0012</td><td>0.0012</td><td>0.0000</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.  
Note. Standard errors in parentheses.

However, one could be concerned that, using all the 1,988 nonsampling products in the baseline analysis or the above 536 randomly selected nonsampling products may not generate a “balanced” sample between sampling and nonsampling products. In other words, the sampling engagement decision might not be the major difference between the two groups of products and there could exist other possible factors that might confound our analysis. To rule out this concern and show the robustness of our estimates, we next make use of the Propensity Score Matching (PSM) technique (Rosenbaum and Rubin 1983, Heckman et al. 1998) to construct our second control group. We use a set of observable variables for PSM matching, including (1) product inventory, $I N _ { i t } ,$ , the available quantity of product i for sale on day t; (2) product web page bookmark, $B M _ { i t } ,$ the number of web page bookmarks of product i on day t; (3) product description, $D S _ { i t } ,$ the length (by character count) of descriptions (e.g., highlights of any unique attributes) of product i on day $t ;$ and (4) product category dummies (C ). We expect that a product’s sampling engagement decision, $I \bar { S } _ { - } S P _ { i } ,$ be related to these factors because of the following reasons. First, if the retailer intends to conduct sampling promotion for a product, then the retailer may expect an increase in product exposure and accordingly prepare a larger IN. Second, BM may indicate the extent to which consumers are interested in the product, which could serve as a criterion for the retailer’s choice of product to engage in sampling promotion. Third, DS implies the retailer’s marketing effort to introduce the product to the public and thus is likely to correlate with the retailer’s decision of conducting free sampling promotion for the product, which is another marketing strategy. Lastly, we expect retailers on Taobao to have preferences for choosing certain product categories for sampling promotion, which could be captured by product category dummies C.

On the basis of the above factors, we perform PSM matching with the one-to-one nearest-neighbor matching (without replacement) algorithm,<sup>12</sup> which is recognized as the optimal matching method in the literature (Austin 2010), to construct the control group. The online appendix summarizes the t-test results of the mean differences between the treatment and control groups in terms of the above variables used for matching. After matching, the two groups have no significant differences across all variables. This implies that our PSM matching is successful such that the difference between the two groups mainly comes from the sampling engagement decision. We then estimate the DID model based on this PSM-constructed control group, and summarize the results in Table $^ { 4 , }$ column (3). Similarly, the coefficient of $I S \_ S P \times A F \_ S P , 0 . 0 3 6 ( \pm 0 . 0 1 8 )$ remains positive and significant.

To further establish the robustness of our results across different PSM matching algorithms, we also construct the control group by performing PSM matching based on the one-to-one nearest-neighbor matching (with replacement) algorithm, the two nearest-neighbors matching (with replacement) algorithm, and the three nearest-neighbors matching (with replacement) algorithm. We estimate the DID model and summarize the results in Table $^ { 4 , }$ columns (4) to (6), respectively. As indicated, all the coefficients of $I S \_ S P \times \bar { A F } \_ S P$ remain positive and significant.

Lastly, we highlight that we have satisfied the parallel trend assumption of DID. First, we employ the PSM matching approach based on product category dummies and various product attributes. Thus, the treatment group and the control group are similar, such that the parallel trend assumption could be satisfied. Moreover, to account for the heterogeneity in the pretreatment trends between the treatment and control groups, we follow Angrist and Pischke (2008) to incorporate and control for product-specific trends in our model estimation. As indicated in Table 4, column (7), our DID estimate remains consistently positive and significant.

In sum, after addressing the potential endogeneity issue based on the above various strategies, we find that sampling promotion has a positive impact on product rating. In other words, our estimation results show that product sampling promotion can, indeed, lead to bias (inflated) in product rating.

## 4.4. Robustness

We further corroborate our findings by ruling out alternative explanations and checking the robustness and consistency in multiple ways. For ease of reference, Table 5, column (1), and Table $6 ,$ column (1), present the baseline results from Table $^ { 3 , }$ column (3).

First, the process of reviewing a product is highly subjective (Lin and Heng 2015), and a product’s rating could fluctuate around its “true” level over time. Thus, some may be concerned that the change in product rating is simply the result of this rating fluctuation, instead of the influence of product sampling engagement. To address this concern, we construct the rating variance variable (i.e., RR\_VAR, the variance of rating across all the previous days) as a measure for rating fluctuation. After controlling for this fluctuation impact in our model, our estimate of SP in Table 5, column (2), remains consistent with that in column (1).

Table 5. Robustness: Free Product Sampling Engagement (1)

<table><tr><td>Variable</td><td>Baseline(1)</td><td>Ratingvariance(2)</td><td>Centralization(3)</td><td>Standardization(4)</td><td>Robuststandard error(5)</td><td>PA(6)</td><td>ML(7)</td></tr><tr><td>SP (Product sampling engagement)</td><td>0.046***(0.007)</td><td>0.019***(0.004)</td><td>0.046***(0.007)</td><td>0.011***(0.002)</td><td>0.046***(0.017)</td><td>0.045***(0.008)</td><td>0.045***(0.007)</td></tr><tr><td>RR_VAR (Rating variance)</td><td></td><td>0.813***(0.001)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Constant</td><td>4.336***(0.056)</td><td>4.046***(0.029)</td><td>4.426***(0.011)</td><td>4.426***(0.011)</td><td>4.336***(0.120)</td><td>4.431***(0.115)</td><td>4.440***(0.115)</td></tr><tr><td>Control variables</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Number of sampling products</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td></tr><tr><td>Number of nonsampling products</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td></tr><tr><td>Number of products</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td></tr><tr><td>Number of observations</td><td>117,798</td><td>117,798</td><td>117,798</td><td>117,798</td><td>117,798</td><td>117,798</td><td>117,798</td></tr><tr><td>Within  $R^2$ </td><td>0.0296</td><td>0.7440</td><td>0.0296</td><td>0.0296</td><td>0.0296</td><td></td><td></td></tr><tr><td>Between  $R^2$ </td><td>0.0052</td><td>0.0124</td><td>0.0052</td><td>0.0052</td><td>0.0052</td><td></td><td></td></tr><tr><td>Overall  $R^2$ </td><td>0.0032</td><td>0.0047</td><td>0.0032</td><td>0.0032</td><td>0.0032</td><td></td><td></td></tr><tr><td>Wald  $\chi^2$ </td><td></td><td></td><td></td><td></td><td></td><td>2,971</td><td></td></tr><tr><td>Log-likelihood</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-94,011</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Second, a possible concern is the potential collinearity among our model variables. We thus perform mean-subtracted centralization, and standardization, to all the explanatory variables. We reestimate our model based on these centralized or standardized variables and summarize the results in Table 5, columns (3) and (4). The estimates of SP are similar to that in column (1).

Third, one may be concerned about the potential existence of heteroskedasticity and serial correlation, which may bias the estimated standard errors. We thus reestimate our model and report robust standard errors to account for these potential issues. As indicated in Table 5, column (5), the estimated impact of SP remains consistent with that in column (1), suggesting that our finding is robust to heteroskedasticity and serial correlation.

Table 6. Robustness: Free Product Sampling Engagement (2)

<table><tr><td>Variable</td><td>Baseline (1)</td><td>Log-level (2)</td><td>Without time lag (3)</td><td>One-week lag (4)</td><td>Two-week lag (5)</td><td>Three-week lag (6)</td><td>Sampling size (7)</td></tr><tr><td>SP (Product sampling engagement)</td><td>0.046***(0.007)</td><td>0.017***(0.003)</td><td>0.048***(0.007)</td><td>0.038***(0.007)</td><td>0.026***(0.006)</td><td>0.009*(0.005)</td><td></td></tr><tr><td>SIZE (Sampling size)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.039***(0.006)</td></tr><tr><td>Constant</td><td>4.336***(0.056)</td><td>1.575***(0.020)</td><td>4.351***(0.054)</td><td>4.367***(0.056)</td><td>4.416***(0.055)</td><td>4.386***(0.053)</td><td>4.407***(0.113)</td></tr><tr><td>Control variables</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Number of sampling products</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td><td>536</td></tr><tr><td>Number of nonsampling products</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td></tr><tr><td>Number of products</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td></tr><tr><td>Number of observations</td><td>117,798</td><td>117,798</td><td>120,820</td><td>102,325</td><td>85,158</td><td>68,511</td><td>117,798</td></tr><tr><td>Within  $R^2$ </td><td>0.0296</td><td>0.0316</td><td>0.0309</td><td>0.0234</td><td>0.0164</td><td>0.0114</td><td>0.0289</td></tr><tr><td>Between  $R^2$ </td><td>0.0052</td><td>0.0053</td><td>0.0051</td><td>0.0045</td><td>0.0049</td><td>0.0046</td><td>0.0298</td></tr><tr><td>Overall  $R^2$ </td><td>0.0032</td><td>0.0031</td><td>0.0031</td><td>0.0034</td><td>0.0040</td><td>0.0041</td><td>0.0258</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Fourth, we check the robustness of our finding across model specifications. We thus estimate a populationaveraged (PA) model that allows for an exchangeable correlation structure of a generalized linear model and a random effects model estimated via maximum likelihood (ML). The results for the PA and ML models are presented in Table $5 ,$ columns (6) and (7), respectively. Both results show similar estimates to that in column (1).

Fifth, we examine whether our finding is robust across functional forms. We thus log-transform<sup>13</sup> RR to estimate a log-level model. The estimate in Table $^ { 6 , }$ column (2), shows the consistent positive and significant impact of SP. The SP estimate based on this log-level model suggests that a product’s engagement in sampling promotion will lead to a 1.7% increase in product rating, which is close to our baseline estimate of 1.1%.

Sixth, we also check whether the results are sensitive to the choice of time lag levels. We first estimate the impact of SP on RR without using a time lag and find consistent results in Table $6 ,$ column (3). We next choose three different time lag levels including one week, two weeks, and three weeks. The three corresponding estimates of SP are summarized in Table $^ { 6 , }$ columns (4)–(6), respectively. As indicated, all three estimates show similar results as the baseline. Interestingly, the drops in magnitude and significance of these three estimates from Columns (4)–(6) suggest that the positive impact of sampling on rating will diminish over time. Furthermore, the significant lagged impacts also alleviate the concern over potential simultaneity issue between SP and RR, based on the rationale that a product’s sampling engagement decision in the past should not have been influenced by the current product rating.

Lastly, we conduct a validation exercise by estimating the impact of a product sampling attribute of sampling size,<sup>14</sup> SIZE, on product rating. The estimate of SIZE in Table 6, column (7), indicates that product sampling size has a positive impact on product rating, providing additional support to our argument that product sampling will lead to rating increase. Interestingly, the calculated elasticity of product rating with respect to sampling size implies that a 1% increase in the sampling size of a product increases the product’s rating by 1.6%, which is also close to the elasticity of SP (elasticity = 1.1%).

In sum, we are confident that all the various checks indicate robustness and consistency of our findings regarding the impact of product sampling engagement on product rating. Thus, H1 is supported.

## 5. Contingent Factors: Product Pricing and Product Popularity

Our various identification strategies and model estimations have found robust evidence that product sampling engagement will positively increase product rating and thus lead to bias in product rating. After addressing our first research question, we next further explore potential contingent factors that may moderate the identified relationship between product sampling engagement and product rating. For ease of reference, Table 7, column (1), presents the baseline results from Table $^ { 3 , }$ column (3).

Table 7. Result: Product Pricing and Popularity

<table><tr><td>Variable</td><td>Baseline (1)</td><td>Product pricing (2)</td><td>Product popularity (3)</td><td>Product pricing and popularity (4)</td></tr><tr><td rowspan="2">SP (Product sampling engagement)</td><td>0.046***</td><td>0.026***</td><td>0.051***</td><td>0.031***</td></tr><tr><td>(0.007)</td><td>(0.008)</td><td>(0.007)</td><td>(0.008)</td></tr><tr><td rowspan="2">SP × LP (Interaction: Product list price)</td><td></td><td>0.042***</td><td></td><td>0.041***</td></tr><tr><td></td><td>(0.006)</td><td></td><td>(0.006)</td></tr><tr><td rowspan="2">SP × DC (Interaction: Product price discount)</td><td></td><td>-0.032***</td><td></td><td>-0.031***</td></tr><tr><td></td><td>(0.007)</td><td></td><td>(0.007)</td></tr><tr><td rowspan="2">SP × RV (Interaction: Product review volume)</td><td></td><td></td><td>-0.003***</td><td>-0.002***</td></tr><tr><td></td><td></td><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">Constant</td><td>4.336***</td><td>4.348***</td><td>4.324***</td><td>4.336***</td></tr><tr><td>(0.056)</td><td>(0.056)</td><td>(0.056)</td><td>(0.056)</td></tr><tr><td>Main effects</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Control variables</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Number of sampling products</td><td>536</td><td>536</td><td>536</td><td>536</td></tr><tr><td>Number of nonsampling products</td><td>1,988</td><td>1,988</td><td>1,988</td><td>1,988</td></tr><tr><td>Number of products</td><td>2,524</td><td>2,524</td><td>2,524</td><td>2,524</td></tr><tr><td>Number of observations</td><td>117,798</td><td>117,798</td><td>117,798</td><td>117,798</td></tr><tr><td>Within  $R^2$ </td><td>0.0296</td><td>0.0300</td><td>0.0298</td><td>0.0301</td></tr><tr><td>Between  $R^2$ </td><td>0.0052</td><td>0.0052</td><td>0.0051</td><td>0.0051</td></tr><tr><td>Overall  $R^2$ </td><td>0.0032</td><td>0.0031</td><td>0.0030</td><td>0.0030</td></tr></table>

Note. Standard errors in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

First, we expect product pricing factors in terms of original list price (LP) and price discount (DC) to exert some moderating effects. To empirically analyze these moderating effects, we first use product list price LP and price discount DC as the moderators. We construct and include the interaction terms of $S P \times L P$ and $S P \times$ DC in our model estimation. As shown in Table $^ { 7 , }$ column (2), the estimate of $S P \times L P$ is positive and significant, whereas the estimate of $S P \times D C$ is negative and significant. These results thus indicate that the impact of $S P$ indeed depends on product pricing factors. The findings show that higher product list price may enhance the impact of product sampling engagement on product rating, whereas larger price discount weakens it. These findings are consistent with our expectations. Thus, H2 and H3 are supported.

Second, we also expect that product popularity may moderate the relationship between product sampling engagement and product rating. To test the moderating effect of product popularity, we use product review volume $R V ,$ which has been widely recognized as an indicator for product popularity<sup>15</sup> in prior WOM research (Forman et al. 2008, Li and Hitt 2008). Similarly, we construct and include the interaction term of $S P \times$ RV in our model estimation. The significant estimate of $S P \times R V$ in Table $^ { 7 , }$ column (3), shows that product popularity indeed moderates the impact of $S P$ on RR, but negatively. That is, higher product popularity instead weakens the impact of product sampling engagement on product rating. Thus, H4 is not supported. There are some plausible reasons for the unexpected effect. Specifically, a more popular product usually has a higher level of awareness among consumers. Retailers are likely to offer a larger number of the product to consumers through free product sampling given retailers’ expectation of the higher consumer awareness and interest. Thus, more consumers are expected to give a rating after their sampling of the product. As such, a larger volume of ratings is more likely to reduce the rating bias as it is harder for the sampling product to receive consistently higher rating as a result of consumers’ consistent reciprocal action. Moreover, given that more consumers are expected to give a rating after the sampling, consumers may face less pressure to give a higher rating to show their reciprocity, as compared with the case with only one or several consumers that are expected to give a rating after the sampling and thus consumers have more pressure to behave friendly as a return to retailers.

Lastly, we simultaneously include these three interaction terms for estimations and find similar results in Table 7, column (4).

## 6. Concluding Remarks

Using a rich data set from Taobao and various identification strategies and estimation methods, we discover that if a product engages in free product sampling, its product rating may increase. Quantitatively, product sampling engagement may increase product rating by 1.1%. Furthermore, we also identify important contin gent factors, i.e., product pricing and product popularity. Specifically, higher product list price may enhance the positive impact of product sampling engagement on product rating, whereas larger price discount and higher popularity may weaken the positive impact of product sampling engagement on product rating. Although the magnitude of the main effect of product sampling on product rating (elasticity = 1.1%) is not tremendous, we would like to highlight that this magnitude is still moderated by list price, price discount, and product popularity. In other words, under certain conditions (e.g., high list price, small price discount, and low product popularity), the magnitude may significantly increase. Therefore, the effect of free product sampling on product rating could be practically significant as well.

Our research findings have the following contributions. First, our research serves as the first attempt to empirically investigate free product sampling in the e-commerce context. Prior product sampling literature has either focused on offline sampling of physical goods (e.g., Marks and Kamins 1988, Heiman et al. 2001, Bawa and Shoemaker 2004) or online sampling of information goods (e.g., Chellappa and Shivendu 2005, Cheng and Liu 2012, Lee and Tan 2013, Niculescu and Wu 2014), while online sampling of physical goods is a large research gap that remains in the literature. Our study thus contributes to prior literature by addressing this research gap.

Second, our study has discovered that engaging in free product sampling will increase product rating. In other words, product sampling will lead to rating bias. Past WOM research has reported several factors and mechanisms that may lead to biases in WOM, such as self-selection issues (Li and Hitt 2008), trend-following tendency (Wu and Huberman 2008), dynamic factors (Godes and Silva 2012, Lin and Heng 2015), and social factors (Moe and Trusov 2011, Wang et al. 2018). Our study thus contributes to the WOM literature by identifying a new source of WOM bias, i.e., free product sampling. This also contributes to past product sampling literature by revealing a new role of product sampling, i.e., one of the causes of WOM biases. Additionally, we further contribute by documenting the important contingent factors of product pricing and product popularity that would moderate this biasgenerating process.

Third, this research offers important practical insights to online retailers. Our findings show that if a product engages in free product sampling promotion, its product rating would increase. Thus, if online retailers intend to promote the sales of a product, they could choose to conduct product sampling promotion for the product to influence its rating, and then to influence product sales, as past WOM literature has widely documented that increased rating can lead to increased sales (Chevalier and Mayzlin 2006, Clemons et al. 2006, Chintagunta et al. 2010). Particularly, they could choose products with higher original price, smaller price discount, and lower product popularity to conduct product sampling promotions to increase product ratings more easily. More ideally, as we have reported the elasticity of product rating with respect to product sampling engagement, retailers could thus apply this elasticity, and even compare and integrate with other marketing strategies, to strategically influence product rating and product sales.

Fourth, this study provides guidance to e-commerce platform operators regarding the design of rating systems. The value of a rating system largely relies on its truthfulness in reflecting consumers’ product evaluations (Wang et al. 2018). Because our research findings suggest that product sampling will lead to rating bias, which may undermine the truthfulness of product ratings, rating system designers should be aware of this issue. Designers are advised to develop solutions to help consumers correct the bias. For instance, they could add a label on product web pages to highlight whether a product has engaged in product sampling promotion. Alternatively, because we have quantified the extent of bias, designers could actually adjust the rating values accordingly before displaying them on web pages. By providing additional information or strategically manipulating online ratings, designers could help consumers make better purchase decisions.

Finally, we also offer suggestions to consumers. Consumers have always relied on product ratings as an important information source for their purchase decision making (Chevalier and Mayzlin 2006, Chen and Xie 2008, Duan et al. 2008). However, as we have identified that product sampling could lead to rating biases, consumers should be cautious about ratings of products engaging in free sampling, especially products with higher original list price, smaller price discount, and lower popularity. Specifically, when consumers read and evaluate product ratings, they should identify whether a product has engaged in product sampling promotion, and to correct the bias accordingly based on the size of bias quantified in this study, in order to reduce purchase errors due to rating biases (Godes and Silva 2012).

Although this research has highlighted several notable findings and contributions, we acknowledge some limitations. First, our data and empirical analysis are based on one single e-commerce website; thus, our research findings might not be applied to all other online platforms. Second, our analysis was based on a secondary data set and thus we may not have fully controlled for all potential sources of endogeneity bias. Nevertheless, we have attempted to control for many factors at the various levels, address potential endogeneity issues, rule out alternative explanations, and conduct a series of robustness checks to derive rigorous research findings.

This study can be extended in several ways in future research. First, our empirical analysis is based on an observational data set from an e-commerce website and thus is limited in terms of research questions that could be investigated based on the availability of our data set. Therefore, future research could conduc randomized trials or field experimentations to examine other interesting questions such as how to design a free product sampling promotion or product review policies, such that the bias could be eliminated or at least alleviated. Second, because of data limitations, we were not able to observe daily product sales to further examine how rating bias affects product sales. Thus, future research could consider investigating this issue to better understand the roles of product sampling.

## Acknowledgments

The authors thank the senior editor, associate editor, and the anonymous reviewers for their valuable comments and suggestions.

## Endnotes

<sup>1</sup> Taobao product sampling center: http://try.taobao.com; JD product sampling center: http://try.jd.com; YHD product sampling center: http://try.yhd.com.

<sup>2</sup> In this study, a sampling product refers to a product that engages in a free product sampling promotion.

<sup>3</sup> Noteworthy, all the sampling products in our data set have engaged in only one sampling promotion.

This indicates the original list price of product i on day t.

<sup>5</sup> This indicates the difference between the original price and the actual transaction price of product i on day t.

<sup>6</sup> This indicates the sales quantity of product i during the past month prior to day t.

<sup>7</sup> This is a binary variable indicating whether the retailer provides free delivery for product i on day t, with one indicating free delivery and zero otherwise.

<sup>8</sup> This indicates the total number of different types of after-sales services (e.g., warranty) provided by the retailer to consumers for product i on day t.

<sup>9</sup> This indicates the total number of different modes of payment (e.g., Alipay and credit card) provided by the retailer to consumers for product i on day t.

<sup>10</sup> For robustness checks, we also estimate the model using different time lag levels and find consistent results

<sup>11</sup> To obtain a random set of products as the “control” group, we use a seed value to generate a sequence of random numbers to sort all

the 1,988 nonsampling products, and then select the first 536 nonsampling products. For robustness checks, the online appendix also presents the consistent results of a series of DID estimations based on different seed values used to construct different randomly selected control groups.

<sup>12</sup> PSM also requires a seed value for random sorting of products before matching. For robustness checks, the online appendix also presents the consistent results of a series of DID estimations based on different seed values used to construct different PSM-selected control groups.

<sup>13</sup> We add one to RR to avoid logarithms of zeros. We also find consistent results by adding 0.1 or 0.01 to RR before logarithms.

<sup>14</sup> SIZE equals the number of free samples for sampling products, and zero for nonsampling products. As SIZE is time-invariant and would be omitted in a FE model, we employ a RE model for estimation.

<sup>15</sup> We also use product past sales PS as an alternative indicator for product popularity and find consistent results.

## References

Ailloni-Charas D (1984) Promotion: A Guide to Effective Promotional Planning, Strategies, and Executions (John Wiley & Sons, New York).

Ajzen I, Fishbein M (1972) Attitudes and normative beliefs as factors influencing behavioral intentions. J. Personality Soc. Psych. 21(1): 1–9.

Angrist JD, Pischke J-S (2008) Mostly Harmless Econometrics: An Em piricist’s Companion (Princeton University Press, Princeton, NJ)

Antweiler W, Frank MZ (2004) Is all that talk just noise? The information content of internet stock message boards. J. Finance 59(3):1259–1294.

Austin PC (2010) Statistical criteria for selecting the optimal number of untreated subjects matched to each treated subject when using many-to-one matching on the propensity score. Amer. J. Epidemiology 172(9):1092–1097.

Bawa K, Shoemaker R (2004) The effects of free sample promotions on incremental brand sales. Marketing Sci. 23(3):345–363.

Biswas D, Grewal D, Roggeveen A (2010) How the order of sampled experiential products affects choice. J. Marketing Res. 47(3):508–519.

Biswas D, Labrecque LI, Lehmann DR, Markos E (2014) Making choices while smelling, tasting, and listening: The role of sensory (dis) similarity when sequentially sampling products. J. Marketing 78(1):112–126.

Blau PM (1964) Exchange and Power in Social Life (Wiley, New York).

BrightLocal (2016) Local consumer review survey. Accessed October 21, 2017, https://www.brightlocal.com/learn/local-consumer -review-survey/.

Büyükkurt BK (1986) Integration of serially sampled price information: Modeling and some findings. J. Consumer Res. 13(3):357–373.

Chellappa RK, Shivendu S (2005) Managing piracy: Pricing and sampling strategies for digital experience goods in vertically segmented markets. Inform. Systems Res. 16(4):400–417.

Chen H, De P, Hu YJ, Hwang B-H (2014) Wisdom of crowds: The value of stock opinions transmitted through social media. Rev. Financial Stud. 27(5):1367–1403.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Cheng HK, Liu Y (2012) Optimal software free trial strategy: The impact of network externalities and consumer uncertainty. In form. Systems Res. 23(2):488–504.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The effects of online user reviews on movie box office performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Cialdini RB (1993) Influence: The Psychology of Persuasion (Quill William Morrow, New York)

Clemons EK, Gao GG, Hitt LM (2006) When online reviews meet hyperdifferentiation: A study of the craft beer industry J. Management Inform. Systems 23(2):149–171.

Das SR, Chen MY (2007) Yahoo! for Amazon: Sentiment extraction from small talk on the web. Management Sci. 53(9):1375–1388.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407–1424.

Duan W, Gu B, Whinston AB (2008) Do online reviews matter? An empirical investigation of panel data. Decision Support System 45(4):1007–1016.

Fehr E, Gachter S (2000) Fairness and retaliation: The economics of¨ reciprocity. J. Econom. Perspect. 14(3):159–181

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity dis closure in electronic markets. Inform. Systems Res. 19(3):291–313.

Godes D, Mayzlin D (2009) Firm-created word-of-mouth commu nication: Evidence from a field test. Marketing Sci. 28(4):721–739.

Godes D, Silva JC (2012) Sequential and temporal dynamics of online opinion. Marketing Sci. 31(3):448–473.

Goering PA (1985) Effects of product trial on consumer expectations, demand, and prices. J. Consumer Res. 12(1):74–82.

Goh K-Y, Heng C-S, Lin Z (2013) Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Inform. Systems Res. 24(1):88–107.

Gouldner AW (1960) The norm of reciprocity: A preliminary state ment. Amer. Sociol. Rev. 25(2):161–178.

Gu B, Park J, Konana P (2012) The impact of external word-of-mouth sources on retailer sales of high-involvement products. Inform Systems Res. 23(1):182–196.

Hahn M, Park S, Krishnamurthi L, Zoltners AA (1994) Analysis of new product diffusion using a four-segment trial-repeat model. Marketing Sci. 13(3):224–247.

Heckman J, Ichimura H, Todd P (1998) Matching as an econometric evaluation estimator. Rev. Econom. Stud. 65(2):261–294.

Heiman A, Muller E (1996) Using demonstration to increase new product acceptance: Controlling demonstration time. J. Marketing Res. 33(4):422–430.

Heiman A, McWilliams B, Shen Z, Zilberman D (2001) Learning and forgetting: Modeling optimal product sampling over time. Management Sci. 47(4):532–546.

Jain D, Mahajan V, Muller E (1995) An approach for determining optimal product sampling for the diffusion of a new product. J. Product Innovation Management 12(2):124–135.

Jamieson LF, Bass FM (1989) Adjusting stated intention measures to predict trial purchase of new products: A comparison of models and methods. J. Marketing Res. 26(3):336–345.

Kempf DS, Smith RE (1998) Consumer processing of product trial and the influence of prior advertising: A structural modeling approach. J. Marketing Res. 35(3):325–338.

Lee Y-J, Tan Y (2013) Effects of different types of free trials and ratings in sampling of consumer software: An empirical study. J. Managemen Inform. Systems 30(3):213–246.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Li X, Hitt LM (2010) Price effects in online product reviews: An analytical model and empirical analysis. MIS Quart. 34(4): 809–831.

Lin Z (2014) An empirical investigation of user and system recom mendations in e-commerce. Decision Support Systems 68:111–124.

Lin Z, Heng C-S (2015) The paradoxes of word of mouth in electronic commerce. J. Management Inform. Systems 32(4):246–284.

Lin Z, Goh K-Y, Heng C-S (2017) The demand effects of product recommendation networks: An empirical analysis of network diversity and stability. MIS Quart. 41(2):397–426.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Mano H, Oliver RL (1993) Assessing the dimensionality and structure of the consumption experience: Evaluation, feeling, and satisfaction. J. Consumer Res. 20(3):451–466.

Marks LJ, Kamins MA (1988) The use of product sampling and advertising: Effects of sequence of exposure and degree of advertising claim exaggeration on consumers’ belief strength, belief confidence, and attitudes. J. Marketing Res. 25(3):266–281.

Mas A, Moretti E (2009) Peers at work. Amer. Econom. Rev. 99(1): 112–145.

Mayzlin D (2006) Promotional chat on the internet. Marketing Sci. 25(2):155–163.

Mizik N, Jacobson R (2004) Are physicians “easy marks”? Quanti fying the effects of detailing and sampling on new prescriptions. Management Sci. 50(12):1704–1715.

Moe WW, Trusov M (2011) The value of social dynamics in online product ratings forums. J. Marketing Res. 48(3):444–456.

Montoya R, Netzer O, Jedidi K (2010) Dynamic allocation of pharmaceutical detailing and sampling for long-term profitability. Marketing Sci. 29(5):909–924.

Mudambi SM, Schuff D (2010) What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quart. 34(1): 185–200.

Mussweiler T (2003) Comparison processes in social judgment: Mechanisms and consequences. Psych. Rev. 110(3):472–489.

Niculescu MF, Wu D (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. Systems Res. 25(1):173–199.

Nowlis SM, Shiv B (2005) The influence of consumer distractions on the effectiveness of food-sampling programs. J. Marketing Res. 42(2):157–168.

Oliver RL (1977) Effect of expectation and disconfirmation on postexposure product evaluations: An alternative interpretation. J. Appl. Psych. 62(4):480–486.

Oliver RL (1980) A cognitive model of the antecedents and consequences of satisfaction decisions. J. Marketing Res. 17(4):460–469.

Pavlou PA, Dimoka A (2006) The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller differentiation. Inform. Systems Res. 17(4):392–414.

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1):41–55.

Rothschild ML, Gaidis WC (1981) Behavioral learning theory: Its relevance to marketing and promotions. J. Marketing 45(2):70–78.

Schlosser AE (2005) Posting versus lurking: Communicating in a multiple audience context. J. Consumer Res. 32(2):260–265.

Schultz DE, Robinson WA, Petrison LA (1998) Sales Promotion Essentials (NTC Business Books, Lincolnwood, IL).

Schwartz D, Gorman AH, Nakamoto J, McKay T (2006) Popularity, social acceptance, and aggression in adolescent peer groups: Links with academic performance and school attendance. Developmental Psych. 42(6):1116–1127.

Scott CA (1976) The effects of trial and incentives on repeat purchase behavior. J. Marketing Res. 13(3):263–269.

Shiv B, Nowlis SM (2004) The effect of distractions while tasting a food sample: The interplay of informational and affective components in subsequent choice. J. Consumer Res. 31(3): 599–608.

Shoemaker RW, Shoaf FR (1975) Behavioral changes in the trial of new products. J. Consumer Res. 2(2):104–109.

Smith RE (1993) Integrating information from advertising and trial: Processes and effects on consumer response to product infor mation. J. Marketing Res. 30(2):204–219.

Smith RE, Swinyard WR (1983) Attitude-behavior consistency: The impact of product trial versus advertising. J. Marketing Res. 20(3): 257–267.

Taobao (2017) About Taobao. Accessed October 21, 2017, http:/ www.taobao.com/about/intro.php.

Tirunillai S, Tellis G (2012) Does chatter really matter? Dynamics of user-generated content and stock performance. Marketing Sci. 31(2):198–215.

Tucker C, Zhang J (2011) How does popularity information affect choices? A field experiment. Management Sci. 57(5):828–842.

Wadhwa M, Shiv B, Nowlis SM (2008) A bite to whet the reward appetite: The influence of sampling on reward-seeking behaviors. J. Marketing Res. 45(4):403–413.

Wang A, Zhang M, Hann I-H (2018) Socially nudged: A quasi experimental study of friends’ social influence in online prod uct ratings. Inform. Systems Res. 29(3):641–655.

Wu F, Huberman B (2008) How public opinion forms. Papadimitriou C, Zhang S, eds. Internet and Network Economics (Springer, Berlin), 334–341.

Xu SX, Zhang X (2013) Impact of Wikipedia on market information environment: Evidence on management disclosure and investo reaction. MIS Quart. 37(4):1043–1068.

Zeithaml VA (1988) Consumer perceptions of price, quality, and value: A means-end model and synthesis of evidence. J. Marketing 52(3):2–22.

Zhang J (2010) The sound of silence: Observational learning in the U.S. kidney market. Marketing Sci. 29(2):315–335.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
