---
otero_id: 8050
otero_key: "Q43BN5PA"
title: "Word-of-Mouth System Implementation and Customer Conversion: A Randomized Field Experiment"
authors: "Ni Huang; Tianshu Sun; Peiyu Chen; Joseph M. Golden"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0832"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [139.184.14.150] On: 22 July 2019, At: 06:09 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/Q43BN5PA/fulltext/images/16b89e88c165de836740f4a0d72e492563bf2856a0a40b2b489a78106af0ba87.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Word-of-Mouth System Implementation and Customer Conversion: A Randomized Field Experiment

Ni Huang, Tianshu Sun, Peiyu Chen, Joseph M. Golden

To cite this article: Ni Huang, Tianshu Sun, Peiyu Chen, Joseph M. Golden (2019) Word-of-Mouth System Implementation and Customer Conversion: A Randomized Field Experiment. Information Systems Research

Published online in Articles in Advance 24 Jun 2019

https://doi.org/10.1287/isre.2018.0832

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Word-of-Mouth System Implementation and Customer Conversion: A Randomized Field Experiment

Ni Huang,<sup>a</sup> Tianshu Sun,<sup>b</sup> Peiyu Chen,<sup>a</sup> Joseph M. Golden<sup>c</sup>

<sup>a</sup> W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287; <sup>b</sup> Marshall School of Business, University of Southern California, Los Angeles, California 90089; <sup>c</sup> Collage.com, San Francisco, California 94122

Contact: ni.huang@asu.edu, https://orcid.org/0000-0003-3416-513X (NH); tianshus@marshall.usc.edu

https://orcid.org/0000-0002-9786-044X (TS); peiyu.chen@asu.edu, https://orcid.org/0000-0002-1937-9159 (PC); joe@collage.com (JMG)

Received: May 16, 2017 Revised: May 15, 2018; October 1, 2018 Accepted: October 7, 2018 Published Online in Articles in Advance: June 24, 2019

https://doi.org/10.1287/isre.2018.0832

Copyright: © 2019 INFORMS

Abstract. E-commerce firms often face the decision on whether they should implement a word-of-mouth (WOM) system on their websites. An in-site WOM system can potentially boost customer conversion by conveying signals and information about product popu larity and quality. However, implementing such a system might also have unintended consequences, hindering product sales because of the lack of control over WOM volume and content. This study examines how implementing a WOM system (through social media integration) on an e-commerce website affects customer conversion in the two stages of the consumer purchase funnel, namely, adding a product to the cart and placing an order. Identifying the causal effect of WOM system implementation is challenging because e-commerce websites usually make their decisions based on private information about the potential impact of the system and may have simultaneously implemented other initiatives that could confound the effect. As a result, we conducted a randomized field experiment in collaboration with a large e-commerce website in the United States by testing two versions of a web page: one with a WOM system (treatment) and one without (control). We find that the impact of a WOM system implementation on customer conversion is moderated by WOM volume such that its effect is positive above a threshold of volume (measured by the number of comments) and negative below the threshold. Additionally, we find that WOM valence reinforces the impact of a WOM system on customer conversion. These results suggest that a social-learning mechanism is in play. Furthermore, our results show that the impact of a WOM system mostly occurs at the consideration stage in the upper purchase funnel (adding a product to the cart) rather than at the evaluation stage in the lower funnel (placing an order) Our study not only contributes to research on online system design but also offers practica implications for implementing and managing WOM systems on e-commerce websites.

History: Xiaoquan (Michael) Zhang, Senior Editor; Animesh Animesh, Associate Editor

Keywords: word-of-mouth (WOM) system • randomized <sup>fi</sup>eld experiment • consumer purchase funnel • social learning

## 1. Introduction

Although online word of mouth (WOM)<sup>1</sup> has become an important source of information for consumers purchase decisions (e.g., Godes and Mayzlin 2004, Zhu and Zhang 2010, You et al. 2015), there is a lack of understanding on whether and how e-commerce firms should implement a WOM system on their own websites. Industry practice has shown significant divergence in WOM system implementation. Some e-commerce websites choose to rely on external WOM and opt not to have an in-site WOM system (e.g., Tiffany.com and Tjmaxx.com), whereas others implement and manage an internal WOM system (e.g., Amazon.com and Macys.com). Although new digital capabilities supported by social media integration<sup>2</sup> have drastically reduced the sizable upfront development cost of implementing an internal WOM system, there is still a large variation in industry practice about whether to embrace a WOM system on one’s own website (Gu et al. 2012).

Such divergence in industry practice may trace back to the concern that the impact of implementing a WOM system on the performance of an e-commerce website is not readily clear. Firms face important trade-offs when deciding whether to implement a WOM system. On the one hand, an in-site WOM system creates a public communication channel between the firm and users (Kane et al. 2009). The volume and content of the in-site WOM may help prospective customers infer product popularity and quality (Zhu and Zhang 2010), as well as reveal useful product information (Kietzmann et al. 2011). On the other hand, implementing a WOM system on an e-commerce website can be risky, because there could be unintended consequences. For example, a low volume of WOM in an existing WOM system might signal product or website unpopularity, which, in turn, could negatively affect the website’s product sales (e.g., Zhang 2010, Tucker and Zhang 2011). Additionally, negative WOM in the system can outright damage a product’s or website’s reputation (Proserpio and Zervas 2017). Given the potential benefits and risks involved, it is critical for e-commerce websites to understand the causal impact of an in-site WOM system when they make an implementation decision. Building on prior research that highlights the importance of internal WOM systems in e-commerce (Gu et al. 2012), our study seeks to fill the void in the literature related to WOM system implementation and information technology (IT) artifact design (e.g., Jiang and Guo 2015, Yi et al. 2017, Chen et al. 2018). We empirically evaluate the impact of implementing a WOM system on an e-commerce website, via an integration with the Facebook comment system, on customer conversion in the two stages of the consumer purchase funnel (adding a product to the cart and placing an order). Formally, we address the following questions:

1. What is the impact of implementing a WOM system on customer conversion in an e-commerce website?

2. How does the effect vary across different stages of the consumer purchase funnel?

3. What are the potential mechanisms underlying the observed effect?

In answering these research questions, we seek to identify the causal effect of adopting a WOM system on customer conversion<sup>3</sup> in an e-commerce website and explore the mechanism through which the effect manifests. Prior research on WOM and online system design offers limited insight on this matter because of multiple major hurdles. To begin with, identifying the causal impact of WOM system implementation on customer conversion from observational data can be empirically challenging because different e-commerce websites’ adoption decisions may be endogenous— for example, driven by the websites’ private information about its potential impact and accompanied by marketing initiatives or other related campaigns. Empirical analyses using archival data cannot fully address the various endogeneity issues, such as private information and confounding campaigns. Alternatively, laboratory experiments may be used to mimic online purchase scenarios, but subjects’ conversion intentions or behaviors are subject to a laboratory setting’s common limitations, such as the Hawthorne effect and other demand effects, and the experiment sample might offer limited external validity. Therefore, to achieve clean identification on the causal effect of WOM system implementation on customer conversion, one ideally needs to conduct a randomized field experiment in collaboration with an e-commerce website that has competent IT capability and is willing to take the financial risk of testing an in site WOM system. In addition to the identification challenge, it is also difficult to gain access to granular data on customer browsing behavior and product sales from e-commerce websites because firms consider such data highly sensitive (Dedman and Lennox 2009). Our study not only gathers the individual-leve transactional data on customers’ purchases but also taps into their digital footprints on the e-commerce website by using event analytics.

Recognizing the identification and data challenges, we partnered with a leading national e-commerce website in the United States to conduct this study. Specifically, we designed and conducted an individual-level randomized field experiment involving more than 47,000 customers to examine the effect of implementing a WOM system on users’ shopping behaviors on the website Our experiment leads to several interesting findings. To begin with, we find that implementing a WOM system on an e-commerce website can result in either a positive or a negative effect on customer conversion depending on the WOM volume and valence. Specifically, we find that an in-site WOM system has a pos itive effect on user conversion when there is a relatively high volume of WOM (i.e., many comments) on the product page, but its effect is negative when the volume of WOM is relatively low (i.e., few comments), suggesting that social learning<sup>4</sup> is an important mechanism through which a WOM system affects customer behavior. Meanwhile, WOM valence (i.e., the sentiment expressed in the content of the comments) also plays a role such that positive WOM valence enhances the effect of WOM system implementation. Furthermore, considering the multistaged nature of the consumer purchase funnel, our results show that WOM system implementation primarily affects customer conversion at the consideration stage in the upper funnel, where a consumer adds a product to the cart, rather than at the evaluation stage in the lower funnel, where a consumer places an order after having already added a product to the cart. These results are both statistically significant and economically meaning ful, especially considering the negligible cost of imple menting a WOM system on e-commerce websites vi social media integration.

Our study contributes to prior research related to WOM (e.g., Zhu and Zhang 2010, Gu et al. 2012, Oh et al. 2016) and IT system design (e.g., Zhu et al. 2010, Animesh et al. 2011, Xiao and Benbasat 2015, Mojumder et al. 2018). This study adds to the WOM literature by considering a previously overlooked, but important, scenario wherein an e-commerce website decides on whether to implement an in-site WOM system in the first place. Our study demonstrates that integrating an in-site WOM system is a valuable design option for e-commerce websites if the firm can stimulate enough WOM comments on product pages after initial implementation. However, failure to do so may lead to a negative effect on conversion, because customers may infer product unpopularity when seeing a WOM system lacking WOM on the product page. Additionally, although prior studies consider product sales as a single-stage outcome, we are able to unpack the causal effects of WOM on the different stages of the customer purchase funnel (i.e., consideration stage in the upper funnel and evaluation stage in the lower funnel) by combining transactional data with customers’ digital footprints in the event-analytics database. Furthermore, our study adds to the literature on social learning (e.g., Cai et al. 2009, Zhang 2010, Tucker et al. 2013), by providing evidence of both positive and negative learning, with WOM volume being a key moderator in the process. Although previous studies have found a null effect of a negative social-learning signal on product sales (Chen et al. 2011), our results suggest that when implementing a WOM system, a negative social-learning signal from low WOM volume could be detrimental to user conversion on an

Given the wide divergence in industry practice, our findings also offer important implications for e-commerce managers. In particular, this study provides actionable design implications on whether and how e-commerce websites should embrace an in-site WOM system and manage its WOM functions. For instance, although implementing an in-site WOM system through social media integration appears to be a convenient and lowcost option, an e-commerce website’s managers should carefully consider the expected WOM volume and valence. An in-site WOM system helps increase customer conversion, conditional on enough WOM volume and positive or neutral WOM valence in the system. Therefore, on implementing an in-site WOM system, the e-commerce managers might want to seek effective approaches to actively seed WOM, stimulate WOM generation, and actively manage WOM valence. As an example of the practical implication in action, based on our experiment’s outcome, our collaborating firm immediately implemented the WOM system at full scale.

## 2. Related Research

This study is closely related to prior research on online WOM in general and WOM system design in particular. Online WOM has become an indispensable component of business strategy in e-commerce (e.g., Dellarocas et al. 2007, Oh et al. 2016) because extensive body of work has demonstrated the significant impact of online WOM on consumer purchases and firm performance (e.g., Forman et al. 2008, Zhu and Zhang 2010). For example, previous research found that WOM volume and valence are important predictors of product sales (e.g., Chevalier and Mayzlin 2006, Chen and Lurie 2013), and the linguistic characteristics of WOM may also influence consumers’ purchase decisions (e.g., Yin et al. 2016, Packard and Berger 2017). Additionally, Gu et al. (2012) showed that WOM hosting location (i.e., from an external review website or from an internal WOM system on the e-commerce website) matters when it comes to the influence of WOM on product sales.

Most of the prior literature on online WOM and business performance takes the WOM system as a given (e.g., Lu et al. 2013, Goes et al. 2014, You et al. 2015). To the best of our knowledge, previous studies have not yet empirically explored the situation in which an e-commerce website implements an in-site WOM system and accumulates WOM content from the ground up. Many e-commerce websites often find themselves in such a scenario, facing the question of whether they should implement an in-site WOM system. However, previous research has provided limited insight on this important issue. Aiming to fill this gap in the literature, our study investigates how the transition from the absence to the implementation of an in-site WOM system and the accumulation of WOM volume and valence causally affect customer conver sion on an e-commerce website.

Furthermore, prior research on WOM has primarily treated product sales as a single-stage outcome (e.g., Chevalier and Mayzlin 2006, You et al. 2015). It has not empirically examined the role of WOM in the consumer purchase funnel, which proposes that consumers’ decision-making process comprises multiple stages (e.g., Bettman et al. 1998, Lambrecht et al. 2011, Moriguchi et al. 2016). In the e-commerce context, when a website user enters a product page, the user is located in the upper part of the purchase funnel, the consideration stage, where he or she engages in information-seeking behavior and may temporarily add the product to the cart. Subsequently, the user enters the lower funnel, the evaluation stage, where he or she further assesses the product and may ultimately place an order (Moriguchi et al. 2016). Contributing to prior literature related to the economic impact of WOM, our study explores the effects of WOM on the different stages of the consumer purchase funnel at the individual level, deepening our understanding of the conversion process.

Finally, our study also adds to the growing stream of work that explores WOM system design (e.g., Jiang and Guo 2015, Chen et al. 2018). For instance, Jiang and Guo (2015) employed an analytical approach to examine the design implications on a WOM rating system. The authors concluded that a website would benefit from adopting a rating system conditional on product ratings being higher than a certain threshold.

Additionally, Chen et al. (2018) explored the influence of a multidimensional rating system (versus a singledimensional rating system) on customer satisfaction. The authors show that a multidimensional rating system better matches prospective customers’ preferences with restaurants’ attributes, leading to higher customer satisfaction. Contributing to the related prior work, our study aims to offer design implications not only on the implementation of an in-site WOM system but also on the management of WOM content on an e-commerce website.

## 3. Theoretical Overview

## 3.1. Social Learning

We theorize that implementing an in-site WOM system may affect users’ purchasing behavior on an e-commerce website through a social-learning mechanism. Social learning refers to the process by which individuals learn from others when making decisions (Bandura 1977).<sup>6</sup> In our study context, when prospective customers have limited cues on product popularity and quality, after the implementation of a WOM system, they may use WOM volume and valence accumulated through the WOM system as indicators of such.<sup>7</sup> Behavior such as this is consistent with a social-learning mechanism (e.g., Zhang 2010, Zhang and Liu 2012, Sun et al. 2019), wherein buyers follow their peers choices and opinions as they infer a product’s popularity (Tucker and Zhang 2011) or quality (Banerjee 1992, Bikhchandani et al. 1992) from signals and information transmitted by their peers.

We consider that a WOM system on an e-commerce website could potentially provide a positive or negative learning signal to website visitors.<sup>8</sup> On WOM system implementation, WOM volume and content begin to accumulate on the e-commerce web pages (Cavusoglu et al. 2016). When a relatively high volume of WOM has accrued from the WOM system, ceteris paribus, prospective customers might infer that a product is popular and possibly of high quality (Hellofs and Jacobson 1999, Zhu and Zhang 2010, Qiu et al. 2015). High WOM volume may also contain helpful WOM content about products and services for prospective buyers who just landed on the product web page (Chevalier and Mayzlin 2006, Kwark et al. 2014). For example, WOM accumulated in the system could provide useful information about product quality for prospective customers because they observe prior customers’ sentiment in their textual comments (WOM valence) toward the product features and their purchase experiences. In summary, positive social learning occurs when a WOM system accumulates a relatively high WOM volume or valence, from which prospective customers indirectly infer product quality through its popularity and directly obtain information on product quality, respectively.

Alternatively, when the WOM system is implemented and prominently displayed such that website visitors are aware that other buyers and visitors had the opportunity to generate WOM using the system and yet there is relatively low or even no WOM volume, prospective customers might perceive that the product is unpopular and unattractive.<sup>9</sup> Additionally, the deficiency of information in the relatively low volume of WOM on a product’s web page could also lead to elevated product-quality uncertainty (e.g., Dimoka et al. 2012, Kwark et al. 2014) or product-fit uncertainty (e.g., Hong and Pavlou 2014, Sahoo et al. 2018) for prospective customers. In this scenario, when a WOM system accumulates relatively low WOM volume about a product after implementation of the system on the product web page, negative social learning might occur, wherein prospective customers might be less likely to be interested in the product than when there is no in-site WOM system on the web page at all.

## 3.2. Consumer Purchase Funnel

The idea of a consumer purchase funnel derives from information-processing theory, which proposes that consumers’ purchase decision-making process might comprise multiple stages (e.g., Bettman et al. 1998, Lambrecht et al. 2011). It is likely that social learning with a WOM system may not manifest at both stages of the consumer purchase funnel. This is because WOM is most effective when customers are seeking information and formulating their expectations and preferences (Lambrecht and Tucker 2013). At the consideration stage, consumers actively engage in information-seeking behavior on the product web page before adding a product to the cart (e.g., Bleier and Eisenbeiss 2015, Moriguchi et al. 2016). Socia learning is likely to happen at this stage when consumers are acquiring signals and information on product popularity and quality from the WOM system to form expected utilities about the product. If the expected utilities are high, then they will proceed to add the product to the cart.

By contrast, at the evaluation stage of the consumer purchase funnel, consumers are making a final decision about whether to purchase the product in the cart. Such a decision often builds on further cost– benefit analysis of other factors beyond the signals and information acquired from the WOM system, such as shipping cost and promotion availability (e.g., Chandon et al. 2000, Lewis et al. 2006). As a result, consumers are unlikely to place an order solely based on WOM, especially when the influence was not perceived strongly enough or if consumers have other evaluation criteria for making a purchase decision (e.g., Moriguchi et al. 2016). Bearing the preceding in mind, we expect that WOM plays a more prominent role in consumers considering a product and adding the product to the cart. Additionally, given that the WOM effect is subsumed in the decision as to whether to add a product to the cart, we do not expect that it further influences the subsequent decision from adding a product to the cart to making a purchase.

## 4. Randomized Field Experiment 4.1. Study Context

We collaborated with a large e-commerce website in the United States to conduct our randomized field experiment,<sup>10</sup> which continuously ran for 3 weeks.<sup>11</sup> This e-commerce website operates in a business-toconsumer model and sells various types of customized photo prints with different designs on different materials, such as blankets, canvas, and photobooks.<sup>12</sup> It is the leading business in the industry and had over \$20 million in revenue in 2015. We collaborated with the partner website and implemented an in-site WOM system via a plugged-in Facebook comment function, which enables website users with Facebook credentials to post comments and have conversations with the website’s customer service or other visitors (Grinberg 2011, SimilarTech 2016).

## 4.2. Experimental Design

Before our field experiment, the company had never implemented a WOM system on its website. During the time of the experiment, we employed a randomized between-subjects design at the individual customer level. Our experimental system randomly directs incoming customer traffic into one of two versions of a web page: one with a WOM system (treatment group) and one without (control group). The randomization is executed when a prospective customer enters the website. Once a user is assigned to an experimental condition, the user will remain in the same condition and consistently see the same version of the web page across the website during the experimental period of 3 weeks. Users who participated in the experiment come from 4,834 different cities [as identified by the unique Internet Protocol (IP) addresses in the IP2Location V11 database]. Thus, offline user contamination was unlikely. Also, there were no concurrent experiments on the website during the experiment period, eliminating cross-contamination of treatments.

Figure 1 presents examples of web pages with the WOM system (treatment) and without (control). The web page in the treatment group differs from the control page only in its inclusion of an in-site WOM system with WOM information displayed. In other words, other than the difference of with versus without a WOM system, the two versions of the web page show identical information. As mentioned earlier, the WOM system was constructed through a Facebook comment function,<sup>13</sup> which supports website users with Facebook credentials posting comments and replying to each other on the web page. The section on WOM system contains information about the number of total comments, as well as details of the most recent 10 comments. Customers can click on the “Load 10 more comments” button at the end of the section if they want to read more. The collaborating firm did not reply or moderate any WOM in the system during the experiment.

## 5. Data

We combine data from several different sources to conduct analyses for this study. The data-generating process involves different database systems recording user information (browser and IP address) and user behavior on the website (e.g., add-to-cart, user purchase, and product customization). The transactional database records users’ purchase behavior and purchase history (e.g., time of purchase, past purchases, etc.). We also accessed the company’s event logs through the Snowplow Analytics system.<sup>14</sup> Given the system’s capabilities, we obtained data on users’ various activities, such as whether a user added a product to the online shopping cart, the time of the users’ events, and users’ IP addresses. We looked up users’ locations based on their IP address, using the IP2Location V11 database.<sup>15</sup> We are therefore able to control for location and time-zone effects resulting from geographic variations in internet use and assess the possible offline user contamination issue. We further match these two data sets onto the experimental assignment data set, which includes the test condition that each user is assigned, as well as the time a user enters the experiment.

Additionally, we obtained all WOM content from the Facebook comment system administration tool managed by the company, including the details of each comment (e.g., wording and commenter name) and the time stamp when the comment was posted. In doing so, we construct the scenario and the number of comments (WOM volume) each user had seen when the user entered the web page. We obtain the measure on WOM valence by leveraging the Linguistic Inquiry and Word Count (LIWC) dictionary.<sup>16</sup> LIWC has been used frequently in the psychology (e.g., Tausczik and Pennebaker 2010, Boyd and Pennebaker 2015) and marketing literature (e.g., Sridhar and Srinivasan 2012, Ransbotham et al. 2019) and is becoming increasingly popular for text analytics in the information systems field (e.g., Yin et al. 2014, Huang et al. 2017). Users of the LIWC dictionary can measure linguistic characteristics, such as positive and negative valence, based on the percentage of matches between the text document and a predefined keyword list (Pennebaker et al. 2015).

Figure 1. (Color online) Examples of the Web Pages in the Field Experiment  
![](/api/attachments/Q43BN5PA/fulltext/images/3205d2e8778444f0587167c46a8f179f2b7957098308015fd03a1c05b94e7766.jpg)  
Notes. The Facebook comments section is highlighted in the red box by the authors. Same as the control group, the treatment group also contains the product information titled “What You’re Getting” and “Make Your $5 0 ^ { \prime \prime } \times 6 0 ^ { \prime \prime }$ Fleece Photo Blanket” at the bottom of the web page, which is not shown in the figure due to the length limit of the screen size. Additionally, during the experiment period, the Facebook like button did no display the total number of likes. Thus, the consumers do not observe the number of Facebook likes on the product pages in the field experiment

In our case, we used the LIWC dictionary to compute the linguistic measures for each comment based on positive and negative valence (i.e., LIWC’s “posemo” and “negemo” measures) and then calculate each incoming user’s observed WOM valence by averaging the net sentiment scores<sup>17</sup> for the top 10 comments (or all comments if there were fewer than 10) shown on the user’s arrival at the web page.<sup>18</sup> A higher WOM valence number suggests that more positive comments are displayed on the product page.

Table 1 presents the variable list and descriptions. Tables 2 and 3 show the descriptive statistics and the correlation matrix, respectively. Table 4 reports the results of a randomization check. We performed a randomization balance check between the treatment and control groups for both observable user characteristics (e.g., user IDs, location, and time zone) and behaviors (e.g., browser, previous orders, total previous spending, and mail preference). As shown in Table 4, we did not find any significant difference for any of the observable factors, attesting to the validity of our randomization procedure.

## 6. Analyses and Results 6.1. Mean Comparisons

We first report the model-free results based on mean comparisons between treatment and control groups. Figure 2 shows the average treatment effects of implementing the WOM system on the two-stage key outcomes: adding a product to the cart and placing an order. In the theoretical overview on the consumer purchase funnel, we consider that the consumers social-learning process, in which consumers acquire signals from the WOM system, should primarily occur when they are browsing a product web page. As a result, we expect that the influence of a WOM system on customer conversion is more likely to occur at the consideration stage in the upper purchase funnel (consumers browsing the product web page and then adding a product to the cart) rather than the evaluation stage in the lower purchase funnel (consumers further progressing through the purchase funnel to place an order). We find evidence in support of our expectation. Compared with the control group (without the WOM system), users in the treatment group (with the WOM system) show a higher likelihood of adding a product to the cart $( M _ { \mathrm { c o n t r o l } } = 0 . 1 1 2$ versus $M _ { \mathrm { t r e a t } } = 0 . 1 \dot { 1 } 9 ; t = 2 . 2 5 7 , p < 0 . 0 5 )$ , translating to a 6.25% lift. Nonetheless, there appears to be no significant difference between the control and treatment groups in the likelihood of placing an order after adding a product to the cart $( \tilde { M _ { \mathrm { c o n t r o l } } } = 0 . 1 4 1 $ versus $M _ { \mathrm { t r e a t } } = 0 . 1 3 8 ; t = - 0 . 3 0 3 , p > 0 . 1 0 )$ 19

Table 1. Variable Definitions

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td>add_to_cart</td><td>Whether a website visitor added the product to the online shopping cart (0 = did not add to the cart, 1 = added to the cart).</td></tr><tr><td>place_order</td><td>After having added a product to the cart, whether a consumer placed one or more orders for the product.</td></tr><tr><td>WOM_system</td><td>Whether the website visitor is in the control (web page without the WOM system) or treatment (web page with the WOM system) group.</td></tr><tr><td>WOM_volume</td><td>Number of comments in the WOM system when the consumer first enters the website.</td></tr><tr><td>WOM_valence</td><td>Average net WOM valence of the comments that a website user observes when arriving at the product web page.</td></tr><tr><td>prior_orders</td><td>Total number of previous orders a website user has placed with the collaborating firm.</td></tr></table>

Table 2. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>add_to_cart</td><td>0.116</td><td>0.320</td><td>0</td><td>1</td></tr><tr><td>place_order</td><td>0.140</td><td>0.347</td><td>0</td><td>1</td></tr><tr><td>WOM_system</td><td>0.501</td><td>0.500</td><td>0</td><td>1</td></tr><tr><td>WOM_volume</td><td>16.772</td><td>10.587</td><td>0</td><td>33</td></tr><tr><td>WOM_valence</td><td>0.084</td><td>0.119</td><td>0</td><td>0.5</td></tr><tr><td>prior_orders</td><td>0.046</td><td>1.114</td><td>0</td><td>118</td></tr></table>

## 6.2. Main Effects

We proceed to conduct a set of regression analyses by controlling for observable covariates to ensure that the findings reported in Section 6.1 were not driven by other covariates. For example, the day and hour the user enters the website and the user’s location may systematically affect the results, and explicitly controlling for these covariates helps us further ascertain that the effects were not systematically driven by temporal or geographic factors. Specifically, we estimate Equation (1) with a linear probability model (LPM). In Equation (1), i indexes the website visitors, j indexes states, and t indexes time (i.e., date-hour); J<sub>j</sub> represents a vector of state dummies, and $\Sigma T _ { t }$ captures a time fixed effect using a within transformation.

Table 3. Correlation Matrix

<table><tr><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>add_to_cart</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>place_order</td><td>.</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>WOM_system</td><td>0.010</td><td>-0.004</td><td>1</td><td></td><td></td><td></td></tr><tr><td>WOM_volume</td><td>0.040</td><td>-0.025</td><td>-0.002</td><td>1</td><td></td><td></td></tr><tr><td>WOM_valence</td><td>0.018</td><td>0.025</td><td>0.017</td><td>-0.082</td><td>1</td><td></td></tr><tr><td>prior_orders</td><td>0.067</td><td>0.101</td><td>-0.001</td><td>-0.006</td><td>0.050</td><td>1</td></tr></table>

Table 4. Randomization Check

<table><tr><td>Variable</td><td>t-Value</td><td>p-Value</td></tr><tr><td>user_id</td><td>0.958</td><td>0.338</td></tr><tr><td>browser_id</td><td>-1.135</td><td>0.257</td></tr><tr><td>prior_orders</td><td>0.123</td><td>0.902</td></tr><tr><td>total_spending</td><td>0.792</td><td>0.428</td></tr><tr><td>mail_preference</td><td>1.178</td><td>0.239</td></tr><tr><td>state_id</td><td>-0.524</td><td>0.600</td></tr><tr><td>time_zone</td><td>-1.051</td><td>0.293</td></tr><tr><td>distance_firm</td><td>-0.664</td><td>0.507</td></tr></table>

Notes. Pairwise t-test statistics with no adjustment are reported. The pairwise comparisons show no significant differences between the treatment and the control group in observed covariates.

$$
\begin{array}{c} \text {Outcome} _ {i j t} = \beta_ {0} + \beta_ {1} ^ {*} \text {WOM\_system} _ {i} + \beta_ {2} ^ {*} \text {Control} _ {i t} \\ + \sum J _ {j} + \sum T _ {t} + \varepsilon_ {i j t}. \end{array}\tag{1}
$$

The advantages of a linear probability model include its high estimation efficiency and straightforwardness in interpreting the coefficients, especially interaction terms, which we will add when estimating the heterogeneous treatment effects. One drawback of the linear probability model is that it may generate predicted probabilities outside the [0, 1] range. Following the approach of Horrace and Oaxaca (2006), we further performed a postestimation inspection, which shows that only 9 observations of over 46,753 observations (for model 1, see the first column of Table 5) and 4 observations (for model 2, see the second column of Table 5) predicted that probabilities remain outside the [0, 1] range. Reestimating the model with these observations dropped did not change the respective estimates. Additionally, we also estimated the models using logistic regressions.

Table 5 reports the LPM estimation results with a time fixed effect (using a date-hour fixed effect) and a state fixed effect (using a vector of state dummies). The results of the regression analyses confirm our findings from the mean comparisons. The coefficient of WOM\_system, which indicates the average treatment effect of WOM system implementation, shows a significant and positive effect $\bar { ( p } < 0 . 0 5 )$ on the probability that a website visitor adds a product to the shopping cart, suggesting that a product becomes more likely to be considered for purchase given the presence of a WOM system. Furthermore, as ex pected, we do not find the WOM system to positively affect the final purchase (insignificant influence on a consumer’s likelihood of placing an order after adding a product to the cart). Additionally, in line with previous work on the predictive value of consumer purchase history (e.g., Rossi et al. 1996,

Figure 2. Mean Comparisons Between Treatment and Control Groups  
![](/api/attachments/Q43BN5PA/fulltext/images/81b37e84bffce147527621ff0b984bb564c6ad47781a0a20c2715180394da996.jpg)

![](/api/attachments/Q43BN5PA/fulltext/images/6b02459c2984c8fbbdb4f5e3810565c224f7f64cbedd15bcbacf8193df2cf4d8.jpg)  
Note. The error bars in the figures are based on 95% confidence intervals of the respective means.

Reinartz and Kumar 2003), our results show that the consumers who have purchased from the website before (repeat customers) are more likely to purchase from the website again. Table 5 also reports the estimations of the logistic regressions, which are consistent with the results of LPM. Meanwhile, the marginal effects of the logit estimates are consistent with the LPM estimates in direction and significance.

Here it is worth noting that in Table 5 we examine the effect of the WOM system on the two separate and sequential stages of the consumer conversion funnel, namely, adding a product to the cart and placing an order. To estimate the economic impact of WOM system implementation on the overall customer conversion, one needs to consider an overarching purchase outcome that combines the two stages of the conversion funnel. Therefore, we performed analyses on the combined overall outcome and found that the direct effect of WOM system implementation on consumers final conversion is positive and significant $( \beta = 0 . 0 0 2 5 ,$ $p = 0 . 0 5 6 )$ . This impact of WOM system implementation on customer conversion is not only statistically significant but also economically meaningful. Considering the fact that the customers’ average conversion rate on the e-commerce website is merely 2.2%, integrating an in-site WOM system with enough volume and neutral or positive valence can lead to an 11.36% increase in customer conversion.<sup>20</sup> Such a significant lift in overall purchase likelihood can directly translate to substantial increases in the e-commerce website’s revenue, amounting to over \$1 million each year in our case.

## 6.3. Interaction Effects of WOM System and WOM Characteristics

We examine the interaction effect of the WOM system with WOM characteristics (i.e., volume and valence) to explore the possible mechanisms underlying the observed main effects. As discussed in the theoretical overview, we theorize that a WOM system influences consumer conversion on an e-commerce website through a social-learning mechanism (e.g., Bandura 1977, Zhang and Liu 2012). Specifically, after the adoption of a WOM system, prospective customers could use WOM volume and valence accumulated through the system to infer product popularity and quality. When WOM volume is relatively high, presenting positive social-learning signals, users might perceive that a product is popular and possibly of high quality (e.g., Duan et al. 2008, Zhu and Zhang 2010). As a result, we expect that the effect of a WOM system on customer conversion, particularly its effect on adding a product to the cart, is positive and significant. By contrast, when a WOM system is prominently displayed and there is an absence of WOM volume or the WOM volume is relatively low on a product page, the lack of WOM volume might become a negative social-learning signal, suggesting that the product is unpopular and unattractive (e.g., Zhang 2010, Chen et al. 2011). Consequently, this product may be less likely to be considered by consumers than it would be absent a WOM system. Bearing the preceding in mind, we anticipate that the impact of a WOM system on adding a product to the cart might become negative and significant in this situation.

Table 5. The Effect of WOM System on Customer Conversion: Add Product to Cart and Place Order

<table><tr><td rowspan="2">Variable</td><td colspan="2">LPM</td><td colspan="2">Logit</td></tr><tr><td>(1) Add to cart</td><td>(2) Place order</td><td>(3) Add to cart</td><td>(4) Place order</td></tr><tr><td>WOM_system</td><td>0.0072*(0.0029)</td><td>0.0041(0.0094)</td><td>0.0721*(0.0293)</td><td>0.0526(0.0837)</td></tr><tr><td>ln(prior_orders)</td><td>0.2621***(0.0157)</td><td>0.2695***(0.0243)</td><td>1.4775***(0.0758)</td><td>1.4622***(0.1088)</td></tr><tr><td>Constant</td><td>0.0808(0.0589)</td><td>0.0120(0.0801)</td><td>-2.1011**(0.7469)</td><td>-0.3466(1.3873)</td></tr><tr><td>Observations</td><td>46,753</td><td>5,404</td><td>46,752</td><td>5,387</td></tr><tr><td> $R^2/Pseudo\ R^2$ </td><td>0.0320</td><td>0.1656</td><td>0.0213</td><td>0.0912</td></tr><tr><td>F-test/ $chi^2$ </td><td>6.955***</td><td>4.272***</td><td>712.41***</td><td>397.97***</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>State fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note. Robust standard errors in the LPM estimation.  
\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Meanwhile, in line with prior literature (e.g., Yin et al. 2016), we also expect that WOM valence might play an important role in consumer conversion, with high WOM valence reinforcing the positive impact of a WOM system on customer conversion. Equation (2) outlines the estimation models for the interaction effects of a WOM system with WOM volume and valence. In Equation (2), i indexes the website visitors, j denotes states, and t indexes time (date-hour). Table 6 reports the regression results of the interaction effects. We mean centered the variables WOM\_volume [Mean = 0, standard deviation (S.D.) = 10.59] and WOM\_valence (Mean = 0, S.D. = 0.12), so the coefficient of WOM\_ system represents the main effect of WOM system adoption when the two variables related to WOM characteristics are equal to their respective means.

$$
\begin{array}{l} \text {Outcome} _ {i j t} \\ = \beta_ {0} + \beta_ {1} * W O M _ {s y s t e m _ {i}} + \beta_ {2} * W O M _ {s y s t e m _ {i}} \times W O M _ {v o l u m e _ {i t}} \\ \quad + \beta_ {3} * W O M _ {s y s t e m _ {i}} \times W O M _ {v a l e n c e _ {i t}} + \beta_ {4} * C o n t r o l _ {i t} \\ \quad + \sum J _ {j} + \sum T _ {t} + \varepsilon_ {i j t}. \end{array}\tag{2}
$$

Several insights emerge from the results in Table 6. Given that the range of the mean-centered variable WOM\_volume goes from negative to positive (Minimum = –16.77, Maximum = 16.23), ceteris paribus, the treatment effect of a WOM system on customer conversion is negative when there are few comments. 21 This result supports our expectation that low WOM volume after implementing a WOM system might be perceived as a negative social-learning signal and could consequently hinder customer conversion. Moreover, as the volume of WOM grows (accumu lating more comments), the impact of a WOM system on customer conversion turns positive. This result supports our theorization that high WOM volume might convey a positive social-learning signal and thereby increase customer conversion.

Table 6. Interaction Effects of WOM System with WOM Characteristics: Volume and Valence

<table><tr><td>Variable</td><td>(1) Add to cart</td><td>(2) Place order</td></tr><tr><td rowspan="2">WOM_system</td><td>0.0069*</td><td>0.0028</td></tr><tr><td>(0.0029)</td><td>(0.0095)</td></tr><tr><td rowspan="2">WOM_system × WOM_volume</td><td>0.0005+</td><td>0.0015</td></tr><tr><td>(0.0003)</td><td>(0.0009)</td></tr><tr><td rowspan="2">WOM_system × WOM_valence</td><td>0.0493+</td><td>-0.0700</td></tr><tr><td>(0.0262)</td><td>(0.0747)</td></tr><tr><td rowspan="2">ln(prior_orders)</td><td>0.2622***</td><td>0.2694***</td></tr><tr><td>(0.0157)</td><td>(0.0242)</td></tr><tr><td rowspan="2">Constant</td><td>0.0796</td><td>0.0207</td></tr><tr><td>(0.0588)</td><td>(0.0833)</td></tr><tr><td>Observations</td><td>46,752</td><td>5,404</td></tr><tr><td>R2</td><td>0.0322</td><td>0.1662</td></tr><tr><td>F-test</td><td>6.797***</td><td>4.242***</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>State fixed effect</td><td>Yes</td><td>Yes</td></tr></table>

Note. Robust standard errors are in parentheses.  
\*p < 0.05; \*\*\*p < 0.001; <sup>+</sup>p < 0.10.

To further illustrate how a WOM system interacts with WOM volume to influence customer conversion over time, we plot the likelihood of a customer adding a product to the cart by experimental groups with the daily accumulation of comments (as shown in Figure 3). Based on our regression analysis, we find that the turning point for negative versus positive social-learning signals on customer conversion is four comments. When there were no comments, the effect of a WOM system on the consumer adding to the cart was negative, whereas the effect of a WOM system on customer conversion became positive when there were more than four comments on the product web page through the system. In our experiment, the number of comments on the landing page reached the turning point of four on March 9, 2015. The graphic evidence in Figure 3 shows patterns of the conversion rates that are consistent with our regression results. Before March 9, the number of comments in the WOM system was less than four, and the likelihood of a customer adding a product to the cart was higher in the control group than in the treatment group. As the number of comments accumulated and passed the threshold of four comments after March 9, the average conversion rate of adding a product to the cart became higher in the 22 treatment group than in the control group.

Figure 3. Graphic Evidence on Customer Adding Product to Cart Over Time  
![](/api/attachments/Q43BN5PA/fulltext/images/080d747d4a8eff566d314dc91f4a35473fc6ec5f5a3bbd50f3dcb9a5eb3731f6.jpg)

Additionally, consistent with the previous estimation results in Table 5, the results in Table 6 show that the influence of a WOM system in tandem with WOM volume and valence on customer conversion mainly occurs at the consideration stage in the upper purchase funnel, wherein consumers consider adding a product to the cart, but not at the evaluation stage in the lower purchase funnel. Lastly, confirming prior work on WOM valence (e.g., Chevalier and Mayzlin 2006, Yin et al. 2016), our results also suggest that valence positively interacts with the WOM system such that the higher the valence, the stronger is the effect of WOM system implementation on customer conversion.

## 7. Discussion

## 7.1. Key Findings

Should an e-commerce website implement an in-site WOM system? Our study answers this question with clean causal evidence from a randomized field experiment in close collaboration with a large e-commerce website in the United States. In the field experiment, we implemented a manipulation by randomly directing website visitors to one of two versions of web pages: one with a WOM system and one without. Theorizing that a WOM system might influence customer conversion through a social-learning mechanism, we performed empirical analyses on the two stages of outcomes in the consumer purchase funnel, namely, adding a product to the cart and placing an order. Several interesting findings emerge from the experiment. First, we find that the influence of a WOM system on customer conversion is moderated by

WOM volume (measured by number of comments). Specifically, when there are few comments, the effect of a WOM system on customer conversion is negative (suggesting negative social learning), yet as the number of comments accrues, the impact of a WOM system becomes positive (indicating positive social learning). Furthermore, we find evidence that the in fluence of a WOM system on customer conversion mainly takes place at the consideration stage in the upper purchase funnel (adding a product to the cart) rather than at the evaluation stage in the lower funnel (placing an order after adding the product to the cart). Lastly, considering the final purchase outcome combining the two stages of consumer purchase funnel, WOM system implementation effectively raises customer conversion by 11.36%, which translates to considerable increases in the e-commerce website’s sales revenue. In sum, our study shows that an in-site WOM system can be a valuable design option for e-commerce websites as long as the system accrues enough WOM volume and neutral or positive valence.

## 7.2. Implications

Our study contributes to research related to WOM and online system design in several ways. First of all, although there exists extensive literature examining the impact of WOM in an environment in which a WOM system already exists (e.g., Zhu and Zhang 2010, Gu et al. 2012, Oh et al. 2016), we are not aware of any study that looks at the initial implementation of an in-site WOM system and considers the question of whether an e-commerce website should implement a WOM system in the first place. Our study investigates how implementing an in-site WOM system from ground zero influences customer conversion in an e-commerce website. It is also notable that our WOM system was realized through social media integration, a popular yet understudied phenomenon (e.g., Kane et al. 2014, Huang et al. 2017, So et al. 2017).

Additionally, advancing prior work that examines the sales impact of WOM on a single-staged outcome, we elucidate the causal influence of WOM on the different stages of the consumer purchase funnel. We show that the influence of WOM on customer conversion mainly manifests at the consideration stage in the upper purchase funnel and might not progress to the evaluation stage in the lower purchase funnel. Furthermore, our study offers important implications for online system design literature (e.g., Zhu et al. 2010, Animesh et al. 2011, Xiao and Benbasat 2015). Our findings suggest that implementing a WOM system through social media integration can be a valuable design option for e-commerce websites, especially when accompanied by proper WOM volume and valence after implementation.

This study also adds to the prior literature on social learning (e.g., Banerjee 1992, Chen et al. 2011) by providing evidence of both a positive and a negative learning effect in an e-commerce context. Although Chen et al. (2011) found a null effect of a negative social-learning signal on product sales, our results suggest that a negative social-learning signal could be detrimental to user-level conversion when a WOM system is implemented on an e-commerce website. We believe that the inconsistency between our findings and those of Chen et al. (2011) might be driven by the differences in research contexts. Specifically, in the context of a market with heterogeneous products, Chen et al. (2011) explains that a negative sociallearning signal could indicate a product being either an unpopular and low-quality product or a niche and high-quality product. As a result, consumers might perceive a negative social-learning signal as less diagnostic and could become less likely to be influenced by the signal (hence the null effect). However, in our study context, all products on the e-commerce website are relatively homogeneous (products do not substantially differ in being mass-market products or niche products).<sup>23</sup> In the context of homogeneous products, consumers are more likely to interpret a negative social-learning signal as the product being unpopular and less desirable rather than being a niche product (hence the negative effect).

This study also offers important managerial implications for e-commerce practitioners. The design of an e-commerce website can significantly influence the website’s attraction and adoption (Campbell et al. 2013). Given the wide divergence in industry practice, the theoretical ambiguity in the effects of potential mechanisms, and the economic implications of imple menting a WOM system on an e-commerce website, it is crucial that we understand the causal effects of such an implementation on customer conversion. The findings of our study inform e-commerce websites of the circumstances under which they should implement an in-site WOM system through social media integration. In particular, our results suggest that implementing an in-site WOM system through social media integration could either improve or hinder customer conversion depending on WOM volume and valence. High or low WOM volume could be seen as a positive or a negative social-learning signal by prospective customers. As a result, e-commerce website managers should embrace an in-site WOM system with proper forethought on WOM volume and valence. Furthermore, to prevent negative social learning, the website operators might want to encourage or incentivize sufficient and beneficial WOM from users at the beginning of implementing a WOM system. Here we should note that WOM volume and valence will also depend on product types, consumer composition, and other factors (Huang et al. 2016, 2017); monetary and nonmonetary incentives provided by e-commerce websites can also affect WOM characteris tics (Burtch et al. 2017). Thus, e-commerce practitioners should form their content-seeding strategies by taking comprehensive consideration of the various conditions that could affect WOM characteristics. With this being said, once enough comments are accumulated, the effect of WOM system implementation on overall customer conversion is likely positive, translating into sales increases on an e-commerce website. In fact, based on our experiment’s findings, our collaborating website later implemented the WOM system at full scale.

## 7.3. Limitations and Future Research

This study has several limitations, which we believe also offer ample opportunities for future research. First, our study uses the natural accumulation of WOM volume when exploring the effects of a WOM system. This is also the practice of many online websites that have limited resources to actively manage online WOM (e.g., Gallaugher and Ransbotham 2010, Miller and Tucker 2013). However, given that websites can implement WOM systems that support WOM management or response, a fruitful direction for future research is to contribute to the management-response literature (e.g., Kumar et al. 2018, Proserpio and Zervas 2017) and examine how an e-commerce website can effec tively encourage and moderate WOM on its product pages. Second, to minimize the potential negative impact across the website (e.g., negative social learning or unfair treatment of the users in the control group), our experiment was conducted for about 3 weeks to investigate the causal effect of the binary WOM system implementation decision. Thus, we only observe a certain range of variations in sentiment and textual features of the observed comments during our experimental period. Because a WOM system can accumulate more WOM volume and a large variation of WOM content over time, future research can extend our work by further examining how the textual characteristics of comments interact with the system implementation to affect customer conversion on an e-commerce website.

Furthermore, although this study considers social learning as the most plausible mechanism and provides evidence supporting it, there might be other mechanisms underlying the effects of a WOM system on customer conversion. For example, from the perspective of customers, an e-commerce website’s decision to implement a WOM comment system would signal the website’s confidence in its products, which might increase users’ likelihood of purchase. Future research could explore other possible mechanisms using survey methods or laboratory experiments. Another limitation is that we did not record how the users consume WOM (e.g., whether they clicked on the “Load more comments” button on a product web page) during the experiment and thus cannot directly observe their learning behavior. Also, the products on our collaborating website are relatively homogeneous and designed for a homogenous market segment. Therefore, we encourage future research to extend our study by experimenting on WOM system implementation on other websites with heterogeneous products. Finally, it would be interesting to investigate how WOM shifts product demand on an e-commerce website—for instance, whether the product demand shifts from the products with low WOM volume to those with high WOM volume. Investigating this question requires manipulation of WOM volume, and we encourage future research to explore this direction.

## Acknowledgements

The authors thank the senior editor, the associate editor, and two anonymous reviewers for a most insightful and constructive review process. The manuscript has benefited from discussions with and feedback from the participants at the seminars held at Arizona State University, the International Conference on Information Systems, the Conference on Digital Experimentation, the INFORMS Marketing Science Conference, and the Conference on Information Systems and Technology.

## Endnotes

<sup>2</sup> Social media integration is defined as the integration of a social media site (e.g., Facebook, Twitter, or LinkedIn) or functions thereof with online platforms that support other activities, such as e-commerce transactions and the creation and exchange of WOM (Blanchard 2011).

<sup>3</sup> Customer conversion from the consumer purchase funnel perspective refers to consumers’ probability of proceeding through the funnel (Lambrecht et al. 2011). Specifically, customers first decide whether to add a product to the shopping cart in the consideration stage of the upper funnel, after which they decide on whether to place the order in the evaluation stage of the lower funnel (Moriguch et al. 2016).

<sup>4</sup> The definition and further explanation of social learning appears in Section 3.1.

<sup>5</sup> We further discuss the possible explanations for the difference between our finding on negatively social learning and that of Chen et al. (2011) in the discussion section.

<sup>6</sup> Other terms closely related to social learning in the literature include observational learning, herding behavior, and information cascades (Cai et al. 2009). Observational learning is a special case of social learning through which a person learns from observing others actions/decisions (Chen et al. 2011). Under certain circumstances, social learning may lead to information cascades or herding behavior Herding behavior describes a phenomenon where people make the same decisions as others in an environment where they can observe o communicate with each other (Zhang 2010). Information cascade is an extreme case of herding behavior, when individuals follow their predecessors’ decisions and ignore their private signals (Banerjee 1992, Bikhchandani et al. 1992)

<sup>7</sup> Following Zhu and Zhang (2010), we use number of comments as a proxy of popularity, conditional on an implicit assumption that the products are of a similar nature, which is the case in our study context.

<sup>8</sup> In the same vein as Zhu and Zhang (2010), we define a positive social-learning signal as a relatively high volume of WOM in the WOM system and a negative social-learning signal as a relatively low volume of WOM in the system.

<sup>9</sup> In a market with a large variety of products, it is also possible that a relatively low WOM volume indicates that a product is a niche product with small market size (Chen et al. 2011). A product is considered to be a niche product when it only caters to a small and specific segment of consumers (Krishnan and Gupta 2001, Brynjolfsson et al. 2010). Based on the company’s market research and the company CEO’s testimony, the products sold on the e-commerce website in our study are of similar nature (photo products) and follow the same purchase flow (customization plus purchase); all products on the e-commerce website are fairly homogeneous and are intended for the same market and customer segment (as measured by gender, age, and other demographics). As a result, it is safe to assume that when a website visitor observes a product with a relatively low WOM volume, the visitor is more likely to perceive the product being unpopular rather than being a niche product.

<sup>13</sup> https://developers.facebook.com/docs/plugins/comments.

<sup>14</sup> Snowplow Analytics is a web analytics software that supports the collection and analysis of users’ digital event data in website traffic (https://snowplowanalytics.com/services/#data-analytics).

<sup>15</sup> http://www.ip2location.com/databases.

<sup>16</sup> http://liwc.wpengine.com.

<sup>17</sup> We compute the net sentiment score for each comment by subtracting the negative-sentiment measure from the positive-sentiment measure (i.e., net sentiment = positive sentiment – negative sentiment). <sup>18</sup> Here we aim to measure the average WOM valence on a web page in natural display on the day of a user’s visit. Considering that a web page only shows the content of the top 10 comments by default, we obtain the web page’s WOM valence by calculating the average of the net WOM valence scores for the top 10 comments readily visible for a user (or less when there were fewer comments on the page).

<sup>19</sup> Two-sample t-tests with p-values from two-tailed tests are reported. <sup>20</sup> (0.0025/0.022) × 100% = 11.36%.

<sup>21</sup> When there are no comments in the WOM system, the variable WOM\_volume is at its minimum (–16.77). In that case, the effect of the WOM system on a consumer adding a product to the cart is negative and significant (–16.77 × 0.0005 + 0.0069 = –0.0015). Furthermore, the effect of a WOM system on adding a product to the cart becomes positive and significant when there are more than four comments on the product web page (–12.77 × 0.0005 + 0.0069 = 0.0005).

<sup>22</sup> Here we would like to clarify that the threshold of four comments is per web page. That is, within a product type, the effect of a WOM system on a consumer adding a product to the cart is negative when there are fewer than four comments on a product page, whereas the WOM system’s negative effect turns positive when the web page accumulates four or more comments. Nevertheless, it should be kept in mind that although we observe a threshold of four comments as the turning point from negative to positive social-learning signal in our particular experiment, we cannot conclude that the number of four comments is the standard number for all other products because the perceived popularity of each product will depend on other factors, such as product awareness, product uncertainty, and/or product price. <sup>23</sup> All products in the study are customized photo product (prints with user designs on common household materials such as a blanket, pillow, or photobook), intended for the same segment of market/ customers and sold by the same e-commerce website/seller, follow the same transaction flow (customization plus purchase) and are provided by the same manufacturers.

## References

Animesh A, Pinsonneault A, Yang SB, Oh W (2011) An odyssey into virtual worlds: Exploring the impacts of technological and spatial environments on intention to purchase virtual products. MIS Quart. 35(3):789–810.

Bandura A (1977) Social Learning Theory (Prentice Hall, Englewood Cliffs, NJ).

Banerjee AV (1992) A simple model of herd behavior. Quart. J. Econ. 107(3):797–817.

Bettman JR, Luce MF, Payne JW (1998) Constructive consumer choice processes. J. Consum. Res. 25(3):187–217.

Bikhchandani S, Hirshleifer D, Welch I (1992) A theory of fads, fashion, custom, and cultural change as informational cascades. J. Political Econom. 100(5):992–1026.

Blanchard O (2011) Social Media ROI: Managing and Measuring Social Media Efforts in Your Organization (Pearson Education, Boston).

Bleier A, Eisenbeiss M (2015) Personalized online advertising effec tiveness: The interplay of what, when, and where. Marketing Sci. 34(5):669–688.

Boyd RL, Pennebaker JW (2015) Did Shakespeare write Double Falsehood? Identifying individuals by creating psychological signatures with text analysis. Psych. Sci. 26(5):570–582.

Brynjolfsson E, Hu Y, Smith MD (2010) Research commentary—long tails vs. superstars: The effect of information technology on product variety and sales concentration patterns. Inform. Systems Res. 21(4):736–747.

Burtch G, Hong Y, Bapna R, Griskevicius V (2017) Stimulating online reviews by combining financial incentives and social norms. Management Sci. 64(5):2065–2082.

Cai H, Chen Y, Fang H (2009) Social learning: Evidence from a randomized natural field experiment. Amer. Econom. Rev. 99(3): 864–882.

Campbell DE, Wells JD, Valacich JS (2013) Breaking the ice in B2C relationships: Understanding pre-adoption e-commerce attrac tion. Inform. Systems Res. 24(2):219–238.

Cavusoglu H, Phan TQ, Cavusoglu H, Airoldi EM (2016) Assessing the impact of granular privacy controls on content sharing and disclosure on Facebook. Inform. Systems Res. 27(4): 848–879.

Chandon P, Wansink B, Laurent G (2000) A benefit congruency framework of sales promotion effectiveness. J. Marketing 64(4):65–81.

Chen Y, Wang Q, Xie J (2011) Online social interactions: A natural experiment on word of mouth vs. observational learning J. Marketing Res. 48(2):238–254.

Chen Z, Lurie NH (2013) Temporal contiguity and negativity bias in the impact of online word of mouth. J. Marketing Res. 50(4): 463–476.

Chen H, De P, Hu YJ (2015) IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Inform. Systems Res. 26(3):513–531.

Chen PY, Hong Y, Liu Y (2018) The value of multidimensional rating systems: Evidence from a natural experiment and randomized experiments. Management Sci. 64(10):4629–4647.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Claussen J, Kretschmer T, Mayrhofer P (2013) The effects of re warding user engagement: the case of Facebook apps. Inform. Systems Res. 24(1):186–200

Dedman E, Lennox C (2009) Perceived competition, profitability and the withholding of information about sales and the cost of sales. J. Accounting Econom. 48(2):210–230.

Dellarocas C, Awad N, Zhang X (2007) Exploring the value of online reviews to organizations: Implications for revenue forecasting and planning. J. Interactive Marketing 21(4):23–45.

Dimoka A, Hong Y, Pavlou P (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 36(2):395–426.

Duan W, Gu B, Whinston AB (2008) The dynamics of online word-ofmouth and product sales—An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3): 291–313.

Gallaugher J, Ransbotham S (2010) Social media and customer dialog management at Starbucks. MIS Quart. Executive 9(4):197–212.

Goes PB, Lin M, Au Yeung CM (2014) “Popularity effect” in usergenerated content: Evidence from online product reviews. In form. Systems Res. 25(2):222–238.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Grinberg M (2011) 10 ways to add Facebook functionality to your website. Accessed April 16, 2018, http://www.socialmediaexaminer.com/10 -ways-to-add-facebook-functionality-to-your-website/.

Gu B, Park J, Konana P (2012) The impact of external word-of-mouth sources on retailer sales of high-involvement products. Inform. Systems Res. 23(1):182–196.

Hellofs LL, Jacobson R (1999) Market share and customers’ perceptions of quality: When can firms grow their way to higher vs. lower quality? J. Marketing 63(1):16–25.

Hong Y, Pavlou PA (2014) Product fit uncertainty in online markets: Nature, effects, and antecedents. Inform. Systems Res. 25(2):328–344.

Horrace WC, Oaxaca RL (2006) Results on the bias and inconsistency of ordinary least squares for the linear probability model. Econom. Lett. 90(3):321–327.

Huang N, Hong Y, Burtch G (2017) Social network integration and user content generation: Evidence from natural experiments. MIS Quart. 41(4):1035–1058.

Huang N, Burtch G, Hong Y, Polman E (2016) Effects of multiple psychological distances on construal and consumer evaluation: A field study of online reviews. J. Consumer Psych. 26(4): 474–482.

Jiang Y, Guo H (2015) Design of consumer review systems and product pricing. Inform. Systems Res. 26(4):714–730.

Kane GC, Alavi M, Labianca GJ, Borgatti S (2014) What’s different about social media networks? A framework and research agenda. MIS Quart. 38(1):275–304.

Kane GC, Fichman RG, Gallaugher J, Glaser J (2009) Community relations 2.0. Harvard Bus. Rev. 87(11):45–50.

Kietzmann JH, Hermkens K, McCarthy IP, Silvestre BS (2011) Social media? Get serious! Understanding the functional building blocks of social media. Bus. Horizons 54(3):241–251.

Krishnan V, Gupta S (2001) Appropriateness and impact of platform based product development. Management Sci. 47(1):52–68.

Kumar N, Qiu L, Kumar S (2018) Exit, voice, and response on digital platforms: An empirical investigation of online management response strategies. Inform. Systems Res. 29(4):849–870.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Lambrecht A, Tucker C (2013) When does retargeting work? Information specificity in online advertising. J. Marketing Res. 50(5):561–576.

Lambrecht A, Seim K, Tucker C (2011) Stuck in the adoption funnel: The effect of interruptions in the adoption process on usage. Marketing Sci. 30(2):355–367.

Lewis M, Singh V, Fay S (2006) An empirical study of the impact of nonlinear shipping and handling fees on purchase incidence and expenditure decisions. Marketing Sci. 25(1):51–64.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Lu X, Ba S, Huang L, Feng Y (2013) Promotional marketing or wordof-mouth? Evidence from online restaurant reviews. Inform. Systems Res. 24(3):596–612.

Miller AR, Tucker C (2013) Active social media management: The case of healthcare. Inform. Systems Res. 24(1):52–70.

Moriguchi T, Xiong G, Luo X (2016) Retargeting ads for shopping cart recovery: Evidence from online field experiments. Working paper, Waseda University, Tokyo.

Mojumder P, Huang N, Sun T, Lv J, Golden J (2018) Not registered? Please sign-up now: A randomized field experiment on the optimal timing of registration request. Presentation, Conference on Digita Experimentation (CODE@MIT), October 26–27, MIT, Boston.

Oh H, Animesh A, Pinsonneault A (2016) Free vs. for-a-fee: The impact of a paywall on the pattern and effectiveness of word-of-mouth via social media. MIS Quart. 40(1):31–56.

Packard G, Berger J (2017) How language shapes word of mouth’s impact. J. Marketing Res. 54(4):572–588.

Pennebaker JW, Boyd RL, Jordan K, Blackburn K (2015) The development and psychometric properties of LIWC2015. Working paper, University of Texas at Austin, Austin.

Proserpio D, Zervas G (2017) Online reputation management: Esti mating the impact of management responses on consumer re views. Marketing Sci. 36(5):645–665.

Qiu L, Tang Q, Whinston A (2015) Two formulas for success in social media: Social learning and network effects. J. Management Inform. Systems 32(4):78–108.

Ransbotham S, Lurie N, Liu H (2019) Creation and consumption of mobile word-of-mouth: How are mobile reviews different? Marketing Sci., ePub ahead of print January 28, https://doi.org 10.1287/mksc.2018.1115.

Reinartz WJ, Kumar V (2003) The impact of customer relationship characteristics on profitable lifetime duration. J. Marketing 67(1): 77–99.

Rossi PE, McCulloch RE, Allenby GM (1996) The value of purchase history data in target marketing. Marketing Sci. 15(4): 321–340.

Sahoo N, Dellarocas C, Srinivasan S (2018) The impact of online product reviews on product returns. Inform. Systems Res. 29(3): 723–738.

SimilarTech (2016) Facebook comments market share and web usage statistics. Accessed April 16, 2018, https://www.similartech.com technologies/facebook-comments.

So Y, Xin M, Animesh A, Oh W (2017) When logins go social: Effects on purchase behaviors and targeted responses in online markets. Presentation, Proceedings of Workshop on Information Systems and Economics (WISE), Seoul, Korea, December 13<sup>−</sup>15

Sridhar S, Srinivasan R (2012) Social influence effects in online product ratings. J. Marketing 76(5):70–88.

Sun T, Viswanathan S, Zheleva E (2019) Creating social contagion through firm mediated message design: Evidence from a ran domized field experiment. Management Sci. Forthcoming.

Tausczik YR, Pennebaker JW (2010) The psychological meaning of words: LIWC and computerized text analysis methods. J. Language Soc. Psych. 29(1):24–54.

Trusov M, Bucklin RE, Pauwels K (2009) Effects of word-of-mouth vs. traditional marketing: Findings from an Internet social net working site. J. Marketing 73(5):90–102.

Tucker C, Zhang J (2011) How does popularity information affect choices? A field experiment. Management Sci. 57(5): 828–842.

Tucker C, Zhang J, Zhu T (2013) Days on market and home sales. Rand J. Econ. 44(2):337–360.

Xiao B, Benbasat I (2015) Designing warning messages for detecting biased online product recommendations: An empirical in vestigation. Inform. Systems Res. 26(4):793–811.

Yi C, Jiang Z, Benbasat I (2017) Designing for diagnosticity and serendipity: An investigation of social product-search mecha nisms. Inform. Systems Res. 28(2):413–429.

Yin D, Bond S, Zhang H (2014) Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quart. 38(2):539–560

Yin D, Mitra S, Zhang H (2016) When do consumers value posi tive vs. negative reviews? An empirical investigation of con firmation bias in online word of mouth. Inform. Systems Res. 27(1):131–144.

You Y, Vadakkepatt GG, Joshi AM (2015) A meta-analysis of elec tronic word-of-mouth elasticity. J. Marketing 79(2):19–39.

Zhang J (2010) The sound of silence: Social learning in the US kidne market. Marketing Sci. 29(2):315–335.

Zhang J, Liu P (2012) Rational herding in microloan markets. Management Sci. 58(5):892–912.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

Zhu L, Benbasat I, Jiang Z (2010) Let’s shop online together: An empirical investigation of collaborative online shopping support. Inform. Systems Res. 21(4):872–891.
