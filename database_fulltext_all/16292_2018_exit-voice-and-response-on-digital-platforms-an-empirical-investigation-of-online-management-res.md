---
otero_id: 16292
otero_key: "58CNQBDC"
title: "Exit, Voice, and Response on Digital Platforms: An Empirical Investigation of Online Management Response Strategies"
authors: "Naveen Kumar; Liangfei Qiu; Subodha Kumar"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0749"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [139.184.14.150] On: 10 August 2018, At: 05:59 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/58CNQBDC/fulltext/images/13a4e743994cc5c008cb0dfa07361f501384e0feae32620304d1bd596ead4dd0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Exit, Voice, and Response on Digital Platforms: An Empirical Investigation of Online Management Response Strategies

Naveen Kumar, Liangfei Qiu, Subodha Kumar

To cite this article: Naveen Kumar, Liangfei Qiu, Subodha Kumar (2018) Exit, Voice, and Response on Digital Platforms: An Empirical Investigation of Online Management Response Strategies. Information Systems Research

Published online in Articles in Advance 09 Aug 2018

https://doi.org/10.1287/isre.2017.0749

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Exit, Voice, and Response on Digital Platforms: An Empirical Investigation of Online Management Response Strategies

Naveen Kumar,<sup>a</sup> Liangfei Qiu,<sup>b</sup> Subodha Kumar<sup>c</sup>

<sup>a</sup> School of Business, University of Washington Bothell, Bothell, Washington 98011; <sup>b</sup> Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>c</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122

Contact: nkchawla@uw.edu (NK); liangfei.qiu@warrington.ufl.edu, http://orcid.org/0000-0002-8771-9389 (LQ); subodha@temple.edu, http://orcid.org/0000-0002-4401-7950 (SK)

Received: August 12, 2016 Revised: May 5, 2017 Accepted: August 2, 2017 Published Online in Articles in Advance: August 9, 2018

https://doi.org/10.1287/isre.2017.074

Copyright: © 2018 INFORMS

Abstract. In the past decade, we have witnessed the growing importance of management responses to online reviews on digital platforms. In this study, we examine the impact of online management responses on business performance and their spillover efect on nearby businesses. By adopting multiple causal identification strategies to address the issue of self-selected responses, we find that the responses by a business owner play a significant role in the performance of the focal business as well as in the performance of the nearby businesses. We observe that, in general, the launch of the new management response feature benefits businesses. What is more interesting is that the benefit is not observed in a consistent manner across all businesses. Only the businesses that choose to use the management response feature observe increases in check-ins. On the other hand, the businesses that are unaware of the management response feature launch on digital platforms, or are aware but choose not to use the management response feature, tend to remain at a disadvantage. Interestingly, we also uncover that the spillover efect (externality) of online management responses on the nearby businesses crucially depends on whether the focal business and the nearby businesses are in direct competition. Furthermore, we identify conditions under which business owners are more likely to respond to consumer comments. Our findings have direct implications for both business owners and digital platforms: Digital platforms can help businesses develop the right engagement strategies by taking the online response strategies of the nearby businesses into account.

History: Yong Tan, Senior Editor; Xue Bai, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0749.

Keywords: online management responses • digital platforms • spillover efect • self-selected responses

The more you engage with customers the clearer things become and the easier it is to determine what you should be doing. —John Russell, managing director, Harley-Davidson Europe (Walter 2014)

## 1. Introduction

Consumers’ searches for online reviews have become increasingly important when making decisions about purchasing any products or using any services. According to a recent survey, nearly 67% of consumers report that their purchasing decisions were influenced by online reviews (Hinckley 2015). Because of a surge in online reviews and consumer reliance on digital media, businesses now have strong incentives to engage with consumers and influence their online rating. Negative reviews posted by consumers can hurt businesses by leaving other consumers to second-guess their choices. This second-guessing results in delayed purchasing (Elejalde-Ruiz 2015), whereas positive reviews can help businesses improve their online brand reputation and increase sales (Luca and Zervas 2016). In another survey, 87% of consumers report that positive online reviews strengthen their purchasing decisions, while 80% report that negative online reviews have led them to change their minds (Duncan 2011). Hence, it is important for businesses to engage with less satisfied customers, respond to their online reviews, and positively influence their future experiences to increase satisfaction (Gu and Ye 2014). At the same time, online engagement with highly satisfied customers can create loyalty for a business and help improve its online rating.

Online review platforms, such as Yelp, TripAdvisor, and Angie’s List, provide consumers with reviews and ratings of local businesses and service providers. These sites have also launched new features for business owners that allow them to embrace and directly engage with consumers using their digital platforms. In this paper, we examine the impact of the adoption of the business owner response feature on business performance measures in a systematic fashion. We also provide insights for researchers and practitioners as to situations in which businesses should spend time and resources embracing the new online engagement features supported through online review sites to remain competitive.

Prior literature has mainly focused on the demand side of online reviews, i.e., characterizing the role of online reviews on purchasing decisions of consumers (e.g., Chevalier and Mayzlin 2006, Liu 2006, Goh et al. 2013). However, from the supply side, the dynamics of business owner engagement with consumers using online social media have not been well understood. In general, the firm-side strategy for online consumer reviews includes online review manipulation (illegal) and online management responses (legal): A firm may increase its product review ratings by conducting review manipulation or by responding to consumer reviews. Online review manipulation refers to a firm’s strategic use of fake accounts or the hiring of real individual accounts to post overly positive (biased) messages to boost product demand (Mayzlin 2006, Mayzlin et al. 2014, Luca and Zervas 2016). The goal of manipulation is to purposely influence perceptions of product popularity. On the other hand, firms can use resources to respond to consumer comments or complaints. Although researchers and practitioners have begun to realize the important role of business owner responses to consumer comments, their focus has been limited to the impact of business owner responses on consumer satisfaction (e.g., Ye et al. 2010, Evans et al. 2012, Thomas et al. 2012, Gu and Ye 2014). To our knowledge, little is known about the impact of online management responses and engagement on the business performance measures, as well as the spillover efect of online management responses on nearby businesses.

To systematically bridge this research gap, we begin by asking our first research question: (1) What is the impact of online management responses on the business performance of a focal restaurant? More specifically, in our data, we can observe the introduction of a new business feature allowing business owners to respond to consumer comments in an online review platform. It may be obvious that the launch of a new business owner response feature benefits those businesses that adopt and embrace the new features to engage with their consumers. However, an empirical challenge lies in establishing the causal efect of online management response on business performance because the decision to respond to consumer comments is endogenous (self-selected). The restaurants that embrace and respond to consumer comments might be systematically diferent from the restaurants that choose not to. Without addressing the self-selection of a restaurant’s decision to respond to consumer comments, the estimation of the efect of online management response would be biased. Using several causal identification strategies, our study is, to our knowledge, the first to provide an empirically driven, comprehensive understanding of the unique situations in which businesses should spend time and resources to embrace the new online engagement features.

Not only is estimating the causal impact of online management responses theoretically important, it also has practical implications. Adoption of the new feature by businesses, especially local and small businesses, and subsequent engagement with consumers could be a resource-intensive and time-consuming endeavor. Without quantifying the benefit of responding to consumer comments (the causal impact of online management responses on business performance), it is unclear whether local businesses should actively embrace and respond to consumer comments.

Online management responses not only afect focal businesses’ performances but also those of nearby businesses. Past research has not directly addressed the externality of online management responses, which leads to our second research question: (2) What is the spillover efect of online management responses on nearby businesses’ performance? On one hand, focal businesses’ online management responses may attract consumers from nearby businesses (competition efect). Therefore, the spillover efect might be negative: Responding to consumer comments will lower nearby businesses’ performances. However, one could also argue that focal businesses’ online management responses may help bring more potential consumers to the neighborhood and benefit nearby businesses by generating positive spillovers (Liu et al. 2014). Both cases are theoretically plausible, presenting a viable opportunity for empirical testing. Our empirical results provide a complete picture of the spillover efect by reconciling these two diferent views in a unified framework: We find that, when businesses are in direct competition (e.g., restaurants belong to the same category), the spillover efect of online management responses is negative; however, the spillover efect is positive when businesses are not in direct competition (e.g., restaurants belong to diferent categories).

Understanding spillover efects of nearby direct and indirect competitors is critical for a focal restaurant to develop appropriate strategies in response to the actions taken by nearby competitors. In the marketing literature, spillover efect across products (e.g., advertising spillovers) has attracted attention (Lewis and Nguyen 2015). However, to our knowledge, this is the first study to empirically quantify the spillover efect of online management responses and how the spillover efect is moderated by direct or indirect competition.

To gain a deeper understanding of businesses’ motives to respond to consumer comments, we ask our third research question: (3) When is a business owner more likely to respond to consumer reviews? More specifically, we examine the impact of competition intensity and average review rating on business owners’ propensity to respond to reviews while controlling for the restaurant category and demographic information, specifically the zip-code level information. We use instrumental variables (IV) to correct possible endogeneity issues.

Section 2 reviews the literature relevant to our study and develops our research hypotheses. Subsequent sections present the data and summary statistics, empirical models, and the results. We conclude by discussing the contributions of this work and implications for theory and practice.

## 2. Literature Review and Hypothesis Development

In this section, we review the literature from four diferent aspects: (i) impact of online management responses on consumer satisfaction, (ii) impact of online reviews on consumer purchasing decisions, (iii) online product review manipulation (supply side), and (iv) social media digital platforms and spillover efects. We also highlight our contributions by comparing and contrasting our work with past studies. Figure 1 shows our research context.

## 2.1. Online Management Response and Consumer Satisfaction

Business owner response and engagement in online social media play an important role in consumer satisfaction. Evans et al. (2012) conduct an experimental study to test the efectiveness of business owner response to negative reviews by analyzing a reader’s propensity to visit a restaurant. They find that the readers are least likely to visit the restaurant after seeing no response to a negative comment. However, positive and constructive responses from the owner can improve, though not completely eliminate, the damage created by the negative review. Gu and Ye (2014) empirically study the responses hosted on a third-party review website in China and find that the business owner response to reviews of customers with low satisfaction has a positive influence on their future online rating. However, the impact of response on other customers is found to be limited. An extensive body of literature and practitioners’ guidelines on management response tends to focus on the qualitative strategies for businesses to respond to online reviews (Thomas et al. 2012). Our study difers from this stream of research by focusing on the impact of online management responses on business performance (including the performance of a focal business as well as the performances of nearby businesses).

Figure 1. Research Context  
![](/api/attachments/58CNQBDC/fulltext/images/79e1ad1a0495a5c1a2da39cccc7f6e5bf2cab34074a3f692ebbc5b098b5b38cf.jpg)

## 2.2. Online Product Reviews and Consumer Purchasing Decisions

Online product reviews on the demand side have been extensively studied in the literature and have been found to influence the purchasing decisions of consumers. Chevalier and Mayzlin (2006) study the efect of online consumer reviews on book sales at Amazon.com and Barnesandnoble.com. Liu (2006) measures the impact of electronic word-of-mouth for movies on the box ofice revenue, and finds that the volume but not the valence of word-of-mouth influences aggregate and weekly box ofice revenue, especially in the early weeks of a new movie’s release. Goh et al. (2013) investigate the diferential impact of user-generated and marketergenerated content on consumers’ purchasing decisions. Goes et al. (2014) and Shen et al. (2015) study users’ various incentives to write online reviews. Besides encouraging users to write more online reviews, our research shows that responding to the existing online reviews is also an efective strategy to boost business performance.

## 2.3. Online Product Review Manipulation

Several studies have empirically shown the existence of widespread manipulation practices on online social media sites. Mayzlin (2006) constructs an analytical model to examine firms’ manipulative behaviors. Hu et al. (2012) develop a statistical method and examine the presence of strategic manipulation in product reviews. Mukherjee et al. (2013) use statistical and machine-learning techniques to identify and estimate the prevalence of opinion spam using customers’ behavior features. Mayzlin et al. (2014) use a diferencein-diferences (DID) approach to study how hotel characteristics and ownership structure afect the level of review manipulation on travel websites Expedia.com and TripAdvisor.com. Anderson and Simester (2014) ofer a diferent perspective on the nature of deceptive reviews. They find that, in addition to firms’ strategic behaviors, customers without clear financial incentives to manipulate product ratings may still write reviews on products they did not purchase. Luca and Zervas (2016) investigate the presence of restaurant review fraud on a review website, Yelp.com. They find that positive review fraud is related to reputational concerns, whereas negative review fraud is more likely due to competition. Given the illegal nature of online review manipulation, responding to consumer comments is an alternative, legal strategy that can address concerns about low review ratings. The potential benefits of this strategy motivate us to quantify the impact of online management responses.

## 2.4. Social Media Digital Platforms and Spillover Efects

Our research is also related to a stream of literature on social media platforms. Prior literature has demonstrated the impact of various digital platform strategies. For instance, Mantena et al. (2010) develop a model to understand the competition between two platforms in an industry with indirect network efects. Anderson et al. (2013) find that ofering a lower performance platform with greater availability of content may be optimal in markets that exhibit two-sided network externalities. Li and Agarwal (2017) empirically demonstrate the impact of the integration of Facebook’s platform with Instagram. Van Alstyne et al. (2016a, b) review diferent strategies of simultaneously attracting producers and consumers to a new digital platform, emphasizing the importance of understanding how platforms operate and compete. Our study provides a unique perspective on the role of facilitating communication between consumers and businesses in social media platforms. More specifically, we quantify the focal and spillover efects of the introduction of online management responses in Yelp on business performance.

A stream of literature has examined the impact of introducing social media fan pages on consumers’ brand evaluations (Malthouse et al. 2013). On social media fan pages, firms can place brand posts (containing videos, messages, and other material). Consumers can become fans of these social media fan pages, and then like the brand post or comment on it. De Vries et al. (2012) explore what factors drive brand post popularity. Naylor et al. (2012) find that the demographic characteristics of a brand’s online supporters can influence a target consumer’s brand evaluations and purchase intentions. Gensler et al. (2013) investigate the negative reputation damaging efect when consumers spread negative messages on social media fan pages. Rishika et al. (2013) examine the efect of customers’ participation on social media fan pages. These studies have mainly focused on the impact on consumers’ brand evaluations or purchase intentions, measured by survey or social media metrics (e.g., the number of Facebook “likes”). Little is known about the efect of online management responses on consumers’ actual behavior. In particular, the link between online management responses and the return on firms’ social media eforts has not been established because consumers’ brand evaluations or purchase intentions are indirect measures of consumers’ actual purchase behavior. The aim of our research is to empirically quantify the impact of online management responses on consumers’ actual mobile restaurant check-ins, which is a more concrete and accurate measure of consumers’ actual purchase behavior and of restaurant performance.

Prior studies have found the existence of spillover efects to rivals in advertising (Anderson and Simester 2013), brand scandals (Roehm and Tybout 2006), and product recalls (Borah and Tellis 2016). Companies with positive brand equity (brand value) can benefit from a positive spillover from other products that share the same brand name. Extending the prior studies on brand spillover efects of marketing activities, our paper examines a specific form of spillover efect, i.e., the spillover of online management responses. More important, the literature has focused on how spillover efects take place through traditional media (e.g., newspapers or TV). By contrast, we investigate the spillover of online management responses on a digital platform: Firms are competing ofline as well as on digital platforms.

## 2.5. Hypothesis Development

We formally develop a series of hypotheses on online management responses. Our study draws on marketing, sociology, and economics theories to investigate online management responses. More specifically, we examine the impact of online management responses and businesses’ motivations to respond to consumer comments. The proposed theoretical model is shown in Figure 2.

2.5.1. Impact of Online Management Responses on Focal Business Performance. The emotional dimension of customer-vendor interactions has been extensively studied in the sociology literature (Rafaeli 1989). Early studies focused on the customer-vendor interactions in ofline settings. Customer emotions may be elicited by a wide range of in-store features and salespersons’ responses (Sherman et al. 1997). An important objective of salespersons’ responses is to prevent consumers from experiencing negative emotions: Such responses can be successful interactions with consumers and lead to greater customer satisfaction (Menon and Dubé 2000).

The rise of social media and digital platforms is transforming the traditional notion of customer relationship management. It is increasingly important to interact with consumers because they can easily express and distribute their opinions to large audiences on social media fan pages (Malthouse et al. 2013). Online interactions with consumers have been shown to be efective in influencing brand evaluations (De Vries et al. 2012, Naylor et al. 2012). More specifically, Gu and Ye (2014) find that online management responses increase the future satisfaction of complaining consumers. Thus, we hypothesize:

Hypothesis 1 (H1). Online management responses increase focal business performance.

2.5.2. Impact of Online Management Responses on Nearby Business Performance. Online management responses also have spillover efects on nearby businesses. The prior marketing literature has explained the spillover efects based on the accessibility–diagnosticity framework (Feldman and Lynch 1988). In brief, this framework suggests that information spillover can occur when information is accessible and diagnostic for the other product (Roehm and Tybout 2006). Roehm and Tybout (2006) extend this theory to the context of brand scandals: Spillover to a competitor is more likely to occur if the scandal for one brand is diagnostic to the competitive brand. In the context of local competition, if a nearby business is in direct competition (same product category) with a focal business, then the focal business’ proactive strategy (e.g., price discount, online management responses, etc.) may attract consumers from nearby businesses (Mallett and Sen 2001, Goldfarb and Xiao 2011, Forman et al. 2009). However, if they are not in direct competition (diferentiated products), the competitive efect might be negligible (Dranove et al. 2003). In some cases, the focal business’ proactive strategy may even help bring more potential consumers to the neighborhood and benefit nearby businesses by generating positive spillovers (Liu et al. 2014). Hence, we hypothesize:

Hypothesis 2 (H2). When firms are in direct competition, online management responses lower nearby business performance; when firms are not in direct competition, online management responses benefit nearby businesses.

2.5.3. Impact of Online Review Rating on Business Owners Propensity to Respond to Consumer Reviews. Social media and digital platforms have changed the balance of power between firms and consumers (Xia 2013). On one hand, consumer complaints and criticism damage companies’ reputations and dampen consumers’ purchase intentions (Zeithaml et al. 1996). In particular, a negative online review hurts more than a positive online review helps (Chevalier and Mayzlin 2006). However, dissatisfied customers, once persuaded to stay with the company, are thereafter more loyal and more likely to generate positive word-of-mouth (Pizzutti and Fernandes 2010, Xia 2013). On the other hand, although online management responses are found to be highly efective among low satisfaction consumers, they have limited influence on other consumers (Gu and Ye 2014). Therefore, business owners have a greater incentive to respond to consumer comments when the online review rating is lower. Accordingly, we hypothesize:

Figure 2. A Conceptual Model and Research Hypotheses  
![](/api/attachments/58CNQBDC/fulltext/images/f172a6e8934c0d3a9f853a1165bbeca7f09ca88e43e65c637f8bf22f1441062c.jpg)

![](/api/attachments/58CNQBDC/fulltext/images/947e9ddf0bf38afff83e84c4f9ba603ecc4b62e43bc964ea049d42f001d02da2.jpg)

Hypothesis 3 (H3). A business owner is more likely to respond to consumer reviews when the online review rating is lower.

2.5.4. Impact of Competition Intensity on Business Owners Propensity to Respond to Consumer Reviews. To survive in a highly competitive environment, business owners need to engage in proactive activities (Auh and Menguc 2005). Zahra (1993, p. 234) states: “When rivalry is fierce, companies must innovate in both products and processes, explore new markets, find novel ways to compete, and examine how they will diferentiate themselves from competitors.” Gatignon and Xuereb (1997) show that when competition is more intense, firms are more likely to conduct innovations. More specifically, firms’ information technology (IT) investment decisions have been influenced to a great extent by the actions of competitors (Clemons 1991): Firms facing more intense competition tend to invest more in IT (Iacovou et al. 1995). Engaging with consumers in online digital platforms is one type of IT investment. Therefore, we hypothesize:

Hypothesis 4 (H4). A business owner is more likely to respond to consumer reviews when the competition is more intense.

## 3. Data Description and Summary Statistics

One of the major sources of data we use to understand the impact of business owners’ responses on restaurant performance is Yelp.com. Yelp is a major restaurant review platform that provides consumer reviews and ratings of local businesses and service providers by allowing consumers to write reviews and share their experiences about local businesses. Yelp was founded in 2004 as a third-party review hosting social media platform. It had hosted more than 102 million reviews by the end of the first quarter of 2016 (Yelp 2016).

Yelp had a monthly average of 21 million unique visitors who visited Yelp via the Yelp app and 69 million unique visitors who visited Yelp via mobile web in the first quarter of 2016 (Yelp 2016). We conducted an automated search of 2,000 restaurants on Google. Based on the search engine results, we found that Yelp is consistently ranked among the top five sites in general and among the top sites in restaurant review categories. Its prominence is a clear reason that Yelp was chosen for this study.

In April 2009, Yelp launched a new feature allowing business owners to respond to individual online reviews posted by customers (Lowensohn 2009). This feature allows business owners to directly engage with their customers by responding to their comments or acknowledging their experience. The responses are appended to the end of the reviews and are publicly viewable by all users reading the reviews (see Figure 3).

In this study, we use a panel data set of an 11-year period (pre- and post- business owner response feature

Figure 3. (Color online) A Screenshot of a Business Owner’s Response

So, I came in with a friend to get brunch-- looked like a really nice place. Not much to say, not a lot to choose from for a brunch, which isn't a huge problem, but food was super expensive. I don't mind paying for good food, but in the end, food was mediocre. A club sandwich was totally not worth \$17, and three small glasses of sprite for \$9?? My friends salad was \$16, he agreed that it was alright but definitely not worth the price. Once again, I don't mind small or average portions at a high price, assuming the food is really good. In this case, it was totally not worth it at all.

I would not come here again.

I do NOT recommend this place to others.

Was this review ...?

Comment from Steven P. of Good Restaurant Business Owner

6/27/2016 · Piotr, I'm sorry that you didn't have a better brunch experience with us. We aim to deliver high quality with fair menu pricing & it seems you didn't feel that was the case. I'm actually surprised that you found our menu "super expensive" considering we are actually moderately-priced compared to many other restaurants in the area. Regardless, we want you to thoroughly enjoy your meal (and wish you wouldn't try steering others away) so I hope you'll think again & allow us another visit to prove we can leave you happy. Steven P. Read less

Table 1. Summary Statistics of Restaurants and Reviews

<table><tr><td>Variables</td><td>Min</td><td>Mean</td><td>Max</td><td>SD</td></tr><tr><td>Number of customers mobile check-ins by restaurant</td><td>0</td><td>2.7</td><td>767</td><td>7.6</td></tr><tr><td>Number of restaurants in a zip-code region</td><td>1</td><td>44.27</td><td>320</td><td>60.83</td></tr><tr><td>Temperature (by month)</td><td>36.17</td><td>59.85</td><td>88.44</td><td>4.76</td></tr><tr><td>Number of rainy days (by month)</td><td>0</td><td>10.43</td><td>28</td><td>14.45</td></tr><tr><td>Number of days below freezing (by month)</td><td>0</td><td>3.03</td><td>23</td><td>5.34</td></tr><tr><td>Fraction of responding restaurants (by month) in the zip-code region of a restaurant</td><td>0</td><td>0.013</td><td>1</td><td>0.017</td></tr><tr><td>Fraction of responding restaurants (by month) with similar category in the zip-code region of a restaurant</td><td>0</td><td>0.016</td><td>1</td><td>0.075</td></tr><tr><td>Fraction of responding restaurants (by month) with different category in the zip-code region of a restaurant</td><td>0</td><td>0.012</td><td>0.333</td><td>0.017</td></tr><tr><td>Driving distance of centroid of each restaurant zip-code from the nearest highway</td><td>0</td><td>1.87</td><td>12.48</td><td>1.89</td></tr><tr><td>Review word length</td><td>1</td><td>111.7</td><td>1,015</td><td>101.09</td></tr></table>

launch) from Yelp.com. We have collected the full history of review information for each posting, including review date, review rating, review content, and the business owner response to the review for each restaurant under study.

In Table 1, we provide the summary statistics for some of the key variables used in this study. Our data set has a total of 4,922 restaurants with 587,903 customer reviews. Yelp reviews each customer review using its proprietary filtering algorithm to filter fraudulent or seemingly deceptive reviews (Luca and Zervas 2016). We rely on Yelp’s system to filter out deceptive messages and use only unfiltered reviews in this study. Each review consists of a star rating, which takes on a value from 1 to 5 (where 1-star signifies least satisfied and 5- stars signifies most satisfied), and text as a descriptive parameter. Figure 4 shows a distribution of the review ratings. We observed that 48,386 (<sup>∼</sup>8%) reviews belong to the 1-star rating; 53,390 (<sup>∼</sup>9%) reviews belong to the 2-star rating; 84,118 (<sup>∼</sup>14%) reviews belong to the 3-star rating; 189,675 (<sup>∼</sup>32%) reviews belong to the 4-star rating; and 212,334 (<sup>∼</sup>36%) reviews belong to the 5-star rating. The overwhelmingly favorable response represented by the J-shaped distribution observed in our sample data is consistent with what has been reported in the literature (Hu et al. 2009), which indicates that our data sample is representative of the underlying review population.

Figure 4. (Color online) Review Rating Distribution  
![](/api/attachments/58CNQBDC/fulltext/images/d8201ef08125d24ff9ff8ff8c1e718ba37271ccd48305ceb6ebf30331792b522.jpg)

The first restaurant owner response that was captured in our sample data set is from April 2009. The number of restaurants that have responded at least once to a customer review is 743, i.e., an overall 15.10% business owner response rate. Given that our data set represents the underlying review population, the low percentage of restaurants with management responses indicates that restaurant owners on social media have not increasingly used the online management response feature. This finding further strengthens the importance of investigating and understanding the impact, if there is one, of using business owner response features on business performance metrics.

To control for geographical diferences on how reviews are written and how business owners respond, we collected business owners’ responses and reviews with specific characteristics of restaurants that are geographically separate. Specifically, we focused on all of the restaurants listed on Yelp from the Seattle, Washington and Memphis, Tennessee metropolitan areas. Each restaurant in these cities belongs to a specific category, such as African, Arabian, and Brazilian. Our data set includes 87 unique categories of restaurants.

We combine Yelp data with information about the demography and the weather conditions of the two cities of interest. In particular, we integrate the Yelp data set with the following data sources: (i) demographic data collected from the U.S. Census Bureau through the web-based query portal, (ii) weather data, and (iii) driving distance from the nearest highway. By collecting the demographic data from the U.S. Census Bureau, we focus on median age of all households in the zip-code region of a restaurant and mean income of all households in the zip-code region of a restaurant. Income and age are also important characteristics that influence consumer behavior (Reynolds and Wells 1977) and how individuals engage with usergenerated content including review ratings on online social media and digital platforms (Sorce et al. 2005). We obtain weather data from the National Oceanic and Atmospheric Administration (NOAA) website.<sup>1</sup> The data has information about precipitation as well as the minimum and maximum temperature for each day. We use Google application programming interface (API)

to get the driving distance of centroid of each restaurant zip-code from the nearest highway in our study.

## 4. Empirical Model Specification and Analysis

## 4.1. Impact of Business Owner Responses on Restaurant Performance

In this section, we analyze our first research question, which addresses the impact of the introduction of business owner response features on restaurant performance when (i) they choose to use the feature; and (ii) they choose not to use the feature. While the business owner response feature was launched in early 2009, we use the panel data of an 11-year preand post-launch period from Yelp.com. Following Liu et al. (2014) and Wang et al. (2015), we use the number of mobile check-ins to measure restaurant business performance. Wang et al. (2015) argue that, in this mobile commerce age, if a restaurant cannot get enough mobile visits, it is probably not attractive to modern customers and it will be dificult for the restaurant to survive. In practice, businesses also monitor real-time, mobile check-ins to evaluate their own and their competitors’ performances because the number of check-ins tends to be highly correlated with store trafic (Liu et al. 2014). For instance, Jef Glueck, the CEO of Foursquare, used mobile check-ins of users to accurately predict that Chipotle’s first-quarter sales in 2016 would be down nearly 30% (Turner 2016).

Following Zhang and Zhu (2011), we examine the change of each restaurant’s check-ins after the introduction of the business owner response feature in the following benchmark regression model:

$$
\begin{array}{c} \log (c h e c k i n _ {i t}) = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t} \\ + \beta_ {2} C o n t r o l s + \varepsilon_ {i t}, \end{array}\tag{1}
$$

where the dependent variable, $\log ( c h e c k i n _ { i t } ) ,$ , is the log number of mobile check-ins of restaurant i in time period t (that measures restaurant performance), $c _ { i }$ is the unobserved restaurant fixed efect, and PostLaunch is a dummy variable indicating whether the feature of business owner responses is launched (1 indicates the post-launch period; 0 indicates the prelaunch period). Controls include: (i) review related information, such as average review rating (AveReview-Rating), standard error of review ratings (SeReview-Rating), average review length (AveReviewLength), and the number of reviews for this business (ReviewCount); (ii) weather information, such as monthly average temperature (MonthlyAveTemp) and three weather variables: BelowFreezingDays (the number of days in a month with the minimum temperature below 32<sup>◦</sup>F for the restaurant city), RainDays (the number of days in a month with rain for the restaurant city), and Snow-Days (the number of days in a month with snow for the restaurant city); and (iii) monthly time dummies.

The fixed efects estimation results are presented in columns 1 and 2 of Table 2. We are interested in the coeficient on PostLaunch . In column 1 of Table $^ { 2 , }$ we find that the coeficient on $P o s t L a u n c h _ { t }$ is significantly positive: After the launch of the feature of business owner responses, in general, the number of mobile check-ins of restaurants increases by 6.19%. In column $^ { 2 , }$ we compute the robust statistics and the results are similar.

Next we examine whether a business owner actually responds after the launch of the new business feature. Following Tucker and Zhang (2011), we extend our baseline specification to the following DID specification with panel fixed efects:

$$
\begin{array}{r l} \log (\text { checkin } _ {i t}) & = c _ {i} + \beta_ {0} + \beta_ {1} \text { PostLaunch } _ {t} \\ & \quad + \beta_ {2} (\text { PostLaunch } _ {t} \times \text { OwnerBinaryResp } _ {i t}) \\ & \quad + \beta_ {3} \text { Controls } + \varepsilon_ {i t}, \end{array} \tag {2}
$$

where $c _ { i }$ is the fixed efect, and OwnerBinaryResp is a binary response variable indicating whether restaurant i responds to customers’ comments in month t (0: no response; 1: response). In column 3 of Table 2, we find that the coeficient of PostLaunch is significantly negative, but the coeficient of the interaction term is significantly positive. It suggests that after the launch of the feature of business owner responses, the restaurants that actually respond to customer comments have a higher level of performance than before: The number of restaurant check-ins increases by $9 . 7 2 - 1 . 2 8 = 8 . 4 4 \%$ However, the restaurants that can respond to customer comments but choose not to do so have a lower level of performance than before: The number of restaurant check-ins decreases by 1.28%. To alleviate concerns about the failure to meet standard regression assumptions (such as clustering and heteroscedasticity), we report the robust statistics in column 4 of Table 2.

Our findings from the regression Equations (1) and (2) imply that, in general, the launch of business owners’ responses can improve restaurant performance. However, this new feature does not benefit every restaurant: It benefits the restaurants that actually respond to customer comments, but it hurts the restaurants that can respond to customer comments but choose not to do so. This result is interesting in the sense that the introduction of the new feature tends to hurt the restaurants that do not respond to customer comments in the post-launch periods. Thus, customers punish the restaurants that do not respond to their concerns using this new feature.

A striking pattern in the data is that the number of restaurant check-ins is remarkably skewed. Quantile regression analysis is particularly useful when the conditional distribution of check-ins is not symmetric and does not have a “standard” shape (Koenker and Hallock 2001). The quantile regression models allow us to account for unobserved heterogeneity and heterogeneous covariates efects. We estimate regression Equation (2) using quantile regressions in Online Appendix B.

Table 2. The Impact of Business Owner Responses on Restaurant Performance

<table><tr><td>Variables</td><td>(1) FE</td><td>(2) FE, robust S.E.</td><td>(3) FE</td><td>(4) FE, robust S.E.</td></tr><tr><td>PostLaunch</td><td>0.0619***[15.53]</td><td>0.0619***[16.72]</td><td>-0.0128**[-2.234]</td><td>-0.0128**[-2.154]</td></tr><tr><td>PostLaunch × OwnerBinaryResp</td><td></td><td></td><td>0.0972***[4.325]</td><td>0.0972***[3.253]</td></tr><tr><td>AveReviewRating</td><td>0.0253***[28.22]</td><td>0.0253***[24.98]</td><td>0.0258***[25.13]</td><td>0.0258***[22.48]</td></tr><tr><td>SeReviewRating</td><td>-0.0970***[-39.01]</td><td>-0.0970***[-40.64]</td><td>-0.0965***[-37.99]</td><td>-0.0965***[-38.91]</td></tr><tr><td>AveReviewLength</td><td>0.000302***[22.73]</td><td>0.000302***[16.48]</td><td>0.000303***[22.73]</td><td>0.000303***[16.44]</td></tr><tr><td>ReviewCount</td><td>0.00757***[25.88]</td><td>0.00757***[7.340]</td><td>0.00761***[25.76]</td><td>0.00761***[7.209]</td></tr><tr><td>MonthlyAveTemp</td><td>0.000554***[3.246]</td><td>0.000554***[2.886]</td><td>0.000503***[3.238]</td><td>0.000553***[2.878]</td></tr><tr><td>BelowFreezingDay</td><td>-0.000259**[-2.068]</td><td>-0.000259**[-2.104]</td><td>-0.000260**[-2.125]</td><td>-0.000260**[-2.011]</td></tr><tr><td>RainDay</td><td>-0.000371***[-3.575]</td><td>-0.000371***[-3.514]</td><td>-0.000382***[-3.574]</td><td>-0.000382***[-3.513]</td></tr><tr><td>SnowDay</td><td>-0.00109***[-3.889]</td><td>-0.00109***[-3.054]</td><td>-0.00140***[-3.897]</td><td>-0.00140***[-3.062]</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.0447***[3.372]</td><td>0.0447***[2.943]</td><td>0.0466***[3.478]</td><td>0.0466***[3.278]</td></tr><tr><td>Observations</td><td>163,757</td><td>163,757</td><td>163,757</td><td>163,757</td></tr></table>

Note. t or robust t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Note that the key argument of the DID method is the “parallel paths” assumption, which posits that the average change in the control group represents the counterfactual change in the treatment group had there been no treatments (Abadie 2005). In other words, aside from those changes resulting from the treatment, any diferences between the treatment and control groups should be random. In our specific context, the control group is the restaurants that do not respond to customer comments after the launch of the new feature, and the treatment group is the restaurants that respond to customer comments. A typical endogeneity concern is that restaurants are self-selected to respond to consumer reviews, and hence the “parallel paths” assumption may not be satisfied. In other words, the treated restaurants are not randomly selected: The restaurants that choose to respond might be systematically diferent from the restaurants that choose not to respond. In Section 4.2, we conduct various analyses to address the endogeneity concerns.

## 4.2. Endogeneity Concerns of Self-Selected Responses

4.2.1. Causal Identification Strategies in Addressing Endogeneity Concerns. To address diferent endogeneity mechanisms of self-selected response, we use various identification strategies depicted in Figure 5. If the underlying selection process is known, we can use the Heckman-type model to explicitly account for the selection process (see Section 4.2.2). For example, a restaurant may decide to respond to consumer comments because its online review rating has been decreasing. This selection mechanism can be explicitly modeled in our Heckman-type model. If the selection process is unknown, we have four cases with diferent identification assumptions: (i) The selection process is driven by observable characteristics, and the diferences between the control and treatment groups caused by the observable characteristics are stable over time in their influence on mobile check-ins (timeinvariant shock); (ii) The selection process is driven by unobserved characteristics, and the diferences between the control and treatment groups caused by the unobserved characteristics are stable over time in their influence on mobile check-ins; (iii) The selection process is driven by observable characteristics, and the diferences between the control and treatment groups caused by the observable characteristics change over time in their influence on mobile checkins (time-variant shock); and (iv) The selection process is driven by unobserved characteristics, and the diferences between the control and treatment groups caused by the unobserved characteristics change over time in their influence on mobile check-ins.

Figure 5. Research Design in Addressing Endogeneity Concerns  
![](/api/attachments/58CNQBDC/fulltext/images/ca91dda1cf8e432b4d57bce1c3865067d30054cd05f2b6a58d5132acc502d550.jpg)

In cases (i) and (ii), our regression Equation (2) in Section 4.1 (DID model with panel fixed efects) is sufficient to address the endogeneity concern because the “parallel paths” assumption holds, and the observable or unobserved confounding factors cancel out. In our context, examples of an observable characteristic in case (i) and an unobserved characteristic in case (ii) are mean household income in the zip-code region of a restaurant and the unobserved restaurant quality, respectively. If treated restaurants are in zip-code regions with larger mean household income or have a higher level of unobserved restaurant quality, it might be reasonable to assume that the diferences between the control and treatment groups caused by these characteristics are stable over time.

In case (iii), we use a DID approach combined with propensity score matching (PSM) to correct the possible endogeneity (see Section 4.2.3). An example of an observable characteristic in case (iii) is competition intensity. More competing restaurants may afect the diferences between control and treatment groups dynamically over time because of the word-of-mouth efect. Case (iv) is the most complicated scenario, and we address the endogeneity concern by using a quasiexperimental design (see Section 4.2.4), which is essentially a combination of the traditional DID model and the Look-Ahead Propensity Score Matching (LA-PSM, see Bapna et al. 2016). In our context, an example of an unobserved characteristic in case (iv) is unobserved restaurant promotions or deals that may change the diferences between the control and treatment groups over time. Note that DID<sup>+</sup>PSM and DID<sup>+</sup>LA-PSM are more robust methods because the former can take care of the endogeneity in cases (i), (ii), and (iii), and the latter can take care of the endogeneity in all four cases. We also rule out pretreatment trends in Section 4.2.5.

4.2.2. Heckman-Type Model. We begin by considering a Heckman-type model (Brown and Mergoupis 2010) to directly specify the selection process. Our key DID model is still the regression Equation (2). However, we directly model whether a restaurant chooses to respond to consumer reviews by looking at a Probit model. The selection equation is given as follows:

$$
\begin{array}{r l} w _ {i t} ^ {*} = a _ {i} + \gamma_ {0} + \gamma_ {1} \text { CountRest } _ {i} + \gamma_ {2} \text { AveReviewRating } _ {i t} \\ & + \gamma_ {3} \text { Controls } + e _ {i t}, \end{array}\tag{3}
$$

where $\boldsymbol { w } _ { i t } ^ { * }$ is a latent variable, $a _ { i }$ is the random effect, $e _ { i t }$ follows from a standard normal distribution, CountRest is the number of restaurants in the zipcode region of restaurant i (that captures the competition intensity), and AveReviewRating is the average review rating of restaurant i at time t. The vector Controls includes: (i) all zip-code level information of restaurant i, such as the population of each zip-code region, the median age in each zip-code region, and the mean household income in each zip-code region; and (ii) restaurant category dummies, monthly time dummies, and city dummies.<sup>2</sup>

The indicator OwnerBinaryResp <sup></sup>1 if $w _ { i t } ^ { * } \geq 0 ;$ Owner-Binary $R e s p _ { i t } = 0$ otherwise. Taking this selection process into account, we jointly estimate Equations (2) and (3), and the endogeneity issue in our DID method is less of a concern. The estimation results of the DID model combined with the Heckman-type selection equation are consistent with our DID model, and are presented in column 1 of Table 3.

Note that the treatment in our context is diferent from the standard binary treatment. When the treatment is binary, each subject could receive the treatment or not receive it. By contrast, multivalued treatments refer to cases in which each subject could receive one of several diferent treatments or not receive treatment at all. In our context, a restaurant may respond to consumer comments several times. We conduct a robustness check based on a Heckman-type model with multivalued treatments.

Table 3. The Impact of Business Owner Responses on Restaurant Performance: Addressing Endogeneity Concerns of Self-Selected Responses

<table><tr><td>Variables</td><td>(1) Heckman-type model</td><td>(2) DID + PSM</td><td>(3) DID + LA-PSM</td><td>(4) Heckman with multivalued treatments</td></tr><tr><td>PostLaunch</td><td>-0.0105**[-2.032]</td><td>-0.0152***[-2.842]</td><td>-0.0139***[-2.434]</td><td>-0.0134**[-2.216]</td></tr><tr><td>PostLaunch × OwnerBinaryResp</td><td>0.0654***[2.852]</td><td>0.0682***[3.126]</td><td>0.0675***[2.926]</td><td></td></tr><tr><td>PostLaunch × OwnerResponse</td><td></td><td></td><td></td><td>0.0267***[3.814]</td></tr><tr><td>AveReviewRating</td><td>0.0327***[16.87]</td><td>0.0294***[11.07]</td><td>0.0316***[14.83]</td><td>0.0263***[12.46]</td></tr><tr><td>SeReviewRating</td><td>-0.0721***[-31.06]</td><td>-0.0633***[-28.22]</td><td>-0.0827***[-26.84]</td><td>-0.0535***[-22.14]</td></tr><tr><td>AveReviewLength</td><td>0.000384***[18.33]</td><td>0.000316***[14.21]</td><td>0.000347***[21.46]</td><td>0.000523***[12.64]</td></tr><tr><td>ReviewCount</td><td>0.00322***[4.352]</td><td>0.00533***[6.179]</td><td>0.00428***[6.548]</td><td>0.00454***[3.284]</td></tr><tr><td>MonthlyAveTemp</td><td>0.000276***[2.633]</td><td>0.000432***[3.368]</td><td>0.000328**[2.115]</td><td>0.000354***[2.945]</td></tr><tr><td>BelowFreezingDay</td><td>-0.000284**[-2.148]</td><td>-0.000224**[-2.036]</td><td>-0.000252**[-2.034]</td><td>-0.000225**[-2.011]</td></tr><tr><td>RainDay</td><td>-0.000469***[-3.854]</td><td>-0.000548***[-4.135]</td><td>-0.000602***[-3.218]</td><td>-0.000533***[-4.325]</td></tr><tr><td>SnowDay</td><td>-0.00185***[-3.387]</td><td>-0.00149***[-3.633]</td><td>-0.00166***[-3.272]</td><td>-0.00137***[-2.842]</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note. t-statistics or robust t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Following Cameron and Trivedi (2009), we modify the selection equation in our original Heckmantype model using a Poisson (count data) model. More specifically, the treatment (the count number of restaurant responses) is a Poisson model with a mean as follows:

$$
\text { OwnerResponse } _ {i t} \sim \text { Poisson } (\mu_ {i t}),\tag{4}
$$

$$
\begin{array}{c} \mu_ {i t} = \exp \bigl (\beta_ {0} + \beta_ {1}   C o u n t R e s t _ {i} + \beta_ {2}   A v e R e v i e w R a t i n g _ {i t} \\ + \beta_ {3}   C o n t r o l s + u _ {i t} \bigr), ^ {3} \end{array}\tag{5}
$$

where OwnerResponse is our dependent variable indicating the number of times restaurant i responded to consumers’ comments at time t. Our main regression is Equation (2), and the error term is $\varepsilon _ { i t }$ . Assume that the errors $\varepsilon _ { i t }$ and $u _ { i t }$ follow a bivariate normal with mean zero and covariance matrix $\left[ { \sigma } _ { \varepsilon } ^ { 2 } \quad \rho \right]$ . Following Cameron and Trivedi (2009), we use a two-step procedure to jointly estimate Equations (2), (4), and (5). The estimation results are robust and are presented in column 4 of Table 3.

4.2.3. DID Combined with PSM. A weakness of Heckman-type models is the strong assumption that we need to have a complete understanding of the selection process. In other words, we assume that Equation (3) characterizes the true selection process. To avoid model dependence, we also consider a DID model combined with matching techniques, such as PSM. Following Goh et al. (2013) and Li (2016), we first create a “proper” control group for treated restaurants by using PSM. We ensure that the control and treated groups are comparable in terms of observable characteristics. Then, we run the DID regression Equation (2).

Note that the traditional PSM takes care of only observable characteristics and may be biased in the case of selection-on-unobservables (Mithas and Krishnan 2009). However, in the implementation of the DID approach combined with PSM, even if treated units differ in important unobserved characteristics from those in the control group, so long as such diferences between the control and treatment groups are stable over time in their influence on mobile check-ins, our specification can eliminate the bias resulting from the diferences between treated units and control units. On the other hand, the traditional DID approach relies on the strong “parallel paths” assumption. If the violation of the “parallel paths” assumption is caused by the differences in observable characteristics, augmenting DID with PSM is an efective method to correct the possible bias.

In the matching process, the treated restaurants are those that respond to consumer reviews after the introduction of the new business feature. Using PSM, we match each treated restaurant to the most “similar” control restaurant (closest propensity score) in terms of the following characteristics: (i) zip-code level information, such as the zip-code population, the median age in each zip-code region, and the mean household income in each zip-code region; (ii) competition intensity measure, CountRest and CountSameRest ; and (iii) restaurant category dummies and city dummies. The number of matched pairs is 743 because the number of restaurants that have responded at least once to consumer reviews (treated restaurants) is 743 in our sample.

We first sort all restaurants in a random order to ensure that the ordering does not afect the subsequent matching. Then, we run a logit regression based on the pretreatment variables mentioned earlier and obtain the predicted propensity scores. We use the nearest neighbor-matching algorithm in which each treated unit is matched with the control unit with the closest propensity score. Note that PSM does not have multiple criteria applied to each of the continuous matching variables. Instead, all information contained in matching variables is summarized in the predicted propensity scores. To assess the quality of matching, we perform t-tests of equality of means before and after the matching to check whether our PSM adequately balances characteristics between the treatment and the control group units. The results are presented Table 4:

In Table 4, there is clear evidence of covariate imbalance between groups. After the matching, the diferences of mean are no longer statistically significant, suggesting that matching helps reduce the bias associated with the observable characteristics. Following Hosanagar et al. (2014), we also check the number of restaurant check-ins for the control and treatment groups (after the matching) before the introduction of the response feature. We find that after the matching, the number of restaurant check-ins before the introduction of the response feature for the control group is not statistically diferent from that for the treatment group: This also suggests that our matching is successful. Additional details on PSM are provided in Online Appendix H. Next, we re-estimate our DID model (2) using the new sample created by PSM; the results are presented in column 2 of Table 3. The basic findings are consistent with those in our DID model and Heckmantype model.

4.2.4. A Quasi-Experimental Design (DID Combined with LA-PSM). The gold standard of establishing convincing causality is to run randomized experiments (Bapna and Umyarov 2015). In our context, an ideal experiment is to randomly assign restaurants into a control or treatment group (whether they respond to consumer reviews). However, randomized trials are not always available because they are expensive. Following similar identification ideas to those in Garg et al. (2011), Bapna et al. (2016), and Wang et al. (2018), we use a quasi-experimental design to account for the diferences between the control and treatment groups caused by unobserved characteristics.

The intuition of our quasi-experiment research design is to exploit the time sequence of business owners’ responses and identify a more similar control group in terms of unobserved characteristics. For example, an econometric challenge in Garg et al. (2011) and Wang et al. (2018) is to separate causal peer influence from homophily (the tendency of individuals to associate with similar others). Empirically, it is not dificult to find that a focal user’s behavior is more likely to be correlated with her online friends’ behaviors than with anonymous users. However, this empirical finding can be driven by causal peer influence or homophily. The dificulty of establishing causal inference of peer influence is the result of lacking a “proper” control group. A focal user’s friends (treatment group) can be very diferent from anonymous users (control group) in many characteristics. To ensure similarity between the control and treatment groups, Garg et al. (2011) and Wang et al. (2018) identify a “proper” control group by observing new social ties formed in a future time period: A proper control unit is a person who is not the focal user’s online friend now but will be her online friend at a future point in time. This quasi-experiment research design ensures that the treated units and the control units are similar in unobserved characteristics.

Table 4. Diferences in Mean Before and After Matching

<table><tr><td rowspan="2">Variables</td><td colspan="5">Before matching</td><td colspan="5">After matching</td></tr><tr><td>Mean treated</td><td>Mean control</td><td>%bias</td><td>t-statistics</td><td>p-value</td><td>Mean treated</td><td>Mean control</td><td>%bias</td><td>t-statistics</td><td>p-value</td></tr><tr><td>CountSameRest</td><td>7.2804</td><td>6.8856</td><td>5.3</td><td>3.11***</td><td>0.002</td><td>7.2804</td><td>7.2978</td><td>-0.2</td><td>-0.11</td><td>0.916</td></tr><tr><td>CountRest</td><td>159.76</td><td>155.18</td><td>5.2</td><td>3.11***</td><td>0.002</td><td>159.76</td><td>159.89</td><td>-0.1</td><td>-0.06</td><td>0.948</td></tr><tr><td>Population</td><td>19,371</td><td>19,547</td><td>-2.0</td><td>-1.24</td><td>0.216</td><td>19,371</td><td>19,371</td><td>-0.0</td><td>-0.00</td><td>0.996</td></tr><tr><td>MedianAge</td><td>35.81</td><td>35.925</td><td>-2.6</td><td>-1.49</td><td>0.135</td><td>35.81</td><td>35.8</td><td>0.2</td><td>0.10</td><td>0.916</td></tr><tr><td>MeanIncome</td><td>90,711</td><td>86,872</td><td>19.8</td><td>11.22***</td><td>0.000</td><td>90,711</td><td>90,676</td><td>0.2</td><td>0.08</td><td>0.932</td></tr></table>

<sup>∗</sup>p < 0.1; <sup>∗∗</sup>p < 0.05; <sup>∗∗∗</sup>p < 0.01.

Their identification intuition also applies to our context. Restaurants that respond to consumer reviews (treated units) can be very diferent from those that do not respond to consumer reviews (control units) in terms of observable and unobserved characteristics. If the “parallel paths” assumption is violated because of observable characteristics, our DID <sup>+</sup> PSM approach in Section 4.2.3 can take care of it. However, if the “parallel paths” assumption is violated because of unobserved characteristics, we can use the same approach as in Garg et al. (2011) and Wang et al. (2018) to identify a better control group. Basically, a better control unit could be a restaurant that has not responded to consumer reviews but will do so in the future. Similarly, this quasi-experiment design in our context ensures that the treated restaurants and the control restaurants are similar in unobserved characteristics.

To account for observable and unobserved characteristics as best as we can, we adopt the LA-PSM method proposed by Bapna et al. (2016) to identify the proper control group, and then we combine it with the DID approach. More specifically, we first split the whole sample period into two periods according to whether the business owner response feature was introduced (period 0 versus periods 1 and 2 in Figure 6). Then, we further split the “after introduction” period into two equally long time periods (period 1 versus period 2 in Figure 6). The treatment group in our quasi-experimental design is the restaurants that respond to consumer reviews in time period 1. For each treated unit, we match it to a control unit with the closest propensity score among restaurants that have not responded to consumer reviews in time period 1 but will respond in time period 2. On one hand, the closest propensity score ensures that the treated and the control units are similar in observable characteristics; on the other hand, choosing restaurants from those that have not responded to consumer reviews in time period 1 but will respond in time period 2 ensures that the treated and the control units are similar in unobserved characteristics. After creating the proper control group, we construct a new data sample with treated and control units in time period 0 and period 1. We reestimate our regression Equation (2) (DID specification with panel fixed efects) using the new data sample. The results are presented in column 3 of Table 3 and are consistent with those in the Heckman-type model and the DID <sup>+</sup> PSM model.

4.2.5. Ruling Out Pretreatment Trends. Another potential concern in the DID model is whether there is a heterogeneity in the pretreatment trends between control and treatment groups (Angrist and Pischke 2008, Greenwood and Wattal 2017). If there is a significant heterogeneity in the pretreatment trends, it suggests that the pretreatments may disproportionately afect treated units, as opposed to control units, and the “parallel path” assumption is less likely to be satisfied. In our context, the concern of pretreatment trends arises because unobserved socioeconomic factors in each local region may cause heterogeneity in the pretreatment trends, and more important, the pretreatment trends could afect restaurants’ decisions to respond to consumer comments. For example, a restaurant may monitor its in-store trafic to decide whether to respond to consumer reviews: When the number of mobile checkins decreases, a restaurant may be more likely to write responses. Following Autor (2003), we conduct two robustness checks to address this concern and rule out the impact of pretreatments as an alternative explanation for our results in Online Appendix G.

4.3. Spillover Efect of Business Owner Responses In this section, we examine the spillover efect of nearby business owners’ responses on the business performance of a focal restaurant. In other words, we want to evaluate if responding to consumer reviews can be an efective competition tool and attract competitors’ customers. We estimate the following equation:

$$
\begin{array}{r l} & {\log (c h e c k i n _ {i t}) = c _ {i} + \beta_ {0} + \beta_ {1} P o s t L a u n c h _ {t}} \\ & {\quad + \beta_ {2} (P o s t L a u n c h _ {t} \times O w n e r B i n a r y R e s p _ {i t})} \\ & {\quad + \beta_ {3} (P o s t L a u n c h _ {t} \times F r a c R e s p _ {i t}) + \beta_ {4} c o n t r o l s + \varepsilon_ {i t},} \end{array}\tag{6}
$$

Figure 6. Identifying Proper Control Group in LA-PSM  
![](/api/attachments/58CNQBDC/fulltext/images/398a2b3ab048671c6a5768145b089aa28789bf80429aa77f8dbbaf30f19dad6a.jpg)

where FracResp is the fraction of responded restaurants in the zip-code region of restaurant i at time t. It is computed as the number of responded restaurants in the zip-code region of restaurant i at time t divided by the number of restaurants in the zip-code region of restaurant i at time t.

The estimation results are presented in Table 5. Column 1 of Table 5 shows that the coeficient on Post-$L a u n c h _ { t } \times F r a c R e s p _ { i t }$ is significantly negative: A percentage increase in responding restaurants in the zip-code region of restaurant i will reduce the number of checkins of restaurant i by 0.439%. The results suggest a negative spillover efect in general (i.e., a competition efect). The intuition is that, if more nearby restaurants choose to respond to consumer reviews, a focal restaurant will face a higher level of competition and lose store trafic. Column 2 of Table 5 shows the robust statistics, and the results are similar.

We further examine the fraction of responded restaurants that have the same category as restaurant i in the zip-code region of restaurant i at time t $( F r a c R e s p S a m e _ { i t } )$

as well as the fraction of responded restaurants that have a diferent category from restaurant i in the zipcode region of restaurant i at time t (FracRespDif <sub>it</sub><sup>)</sup>. Intuitively, nearby restaurants from the same category are direct competitors of a focal restaurant, and nearby restaurants from a diferent category are indirect competitors of a focal restaurant.

We estimate the following regression equation and find that the impact of nearby business owners’ responses is moderated by whether a nearby restaurant is a direct competitor (in the same category):

$$
\begin{array}{l} \log (c h e c k i n _ {i t}) = c _ {i} + \beta_ {0} + \beta_ {1} \text { PostLaunch } _ {t} \\ \quad + \beta_ {2} (\text { PostLaunch } _ {t} \times \text { OwnerBinaryResp } _ {i t}) \\ \quad + \beta_ {3} (\text { PostLaunch } _ {t} \times \text { FracRespSame } _ {i t}) \\ \quad + \beta_ {4} (\text { PostLaunch } _ {t} \times \text { FracRespDiff } _ {i t}) \\ \quad + \beta_ {5} \text { controls } + \varepsilon_ {i t}, \end{array} \tag {7}
$$

where FracRespSame is defined as the number of responded restaurants that have the same category as restaurant i in the zip-code region of restaurant i at time t divided by the number of restaurants that have the same category as restaurant i in the zip-code region of restaurant i at time $t ;$ and FracRespDif is defined as the number of responded restaurants that have a diferent category from restaurant i in the zip-code region of restaurant i at time t divided by the number of restaurants that have a diferent category from restaurant i in the zip-code region of restaurant i at time t.

Table 5. The Spillover Efect of Business Owner Responses

<table><tr><td>Variables</td><td>(1) FE</td><td>(2) FE, robust S.E.</td><td>(3) FE</td><td>(4) FE, robust S.E.</td></tr><tr><td>PostLaunch</td><td>-0.0132**[-2.226]</td><td>-0.0132**[-2.052]</td><td>-0.0184***[-2.941]</td><td>-0.0184***[-2.725]</td></tr><tr><td>PostLaunch × OwnerBinaryResp</td><td>0.0582***(14.41]</td><td>0.0582***(4.825]</td><td>0.0578***(14.28]</td><td>0.0578***(15.14]</td></tr><tr><td>PostLaunch × FracResp</td><td>-0.439***[-5.869]</td><td>-0.439***[-4.771]</td><td></td><td></td></tr><tr><td>PostLaunch × FracRespSame</td><td></td><td></td><td>-0.685***[-5.664]</td><td>-0.685***[-2.736]</td></tr><tr><td>PostLaunch × FracRespDiff</td><td></td><td></td><td>0.119**(2.136]</td><td>0.119***(3.565]</td></tr><tr><td>AveReviewRating</td><td>0.0258***(25.19]</td><td>0.0258***(22.52]</td><td>0.0258***(25.13]</td><td>0.0258***(22.44]</td></tr><tr><td>SeReviewRating</td><td>-0.0966***[-38.04]</td><td>-0.0966***[-38.93]</td><td>-0.0968***[-38.11]</td><td>-0.0968***[-39.13]</td></tr><tr><td>AveReviewLength</td><td>0.000302***(22.66]</td><td>0.000302***(16.40]</td><td>0.000304***(22.79]</td><td>0.000304***(16.46]</td></tr><tr><td>ReviewCount</td><td>0.00756***(25.60]</td><td>0.00756***(7.178]</td><td>0.00755***(25.57]</td><td>0.00755***(7.170]</td></tr><tr><td>MonthlyAveTemp</td><td>0.000553***(3.236]</td><td>0.000553***(2.876]</td><td>0.000551***(3.219]</td><td>0.000551***(2.854]</td></tr><tr><td>BelowFreezingDay</td><td>-0.000263[-0.678]</td><td>-0.000263[-0.615]</td><td>-0.000243[-0.626]</td><td>-0.000243[-0.567]</td></tr><tr><td>RainDay</td><td>-0.000392*[1.662]</td><td>-0.000392[-1.597]</td><td>-0.000384[-1.628]</td><td>-0.000384[-1.562]</td></tr><tr><td>SnowDay</td><td>-0.000706[-0.576]</td><td>-0.000706[-0.680]</td><td>-0.000697[-0.569]</td><td>-0.000697[-0.672]</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.0534***(3.967]</td><td>0.0534***(3.455]</td><td>0.0546***(4.049]</td><td>0.0546***(3.528]</td></tr><tr><td>Observations</td><td>163,757</td><td>163,757</td><td>163,757</td><td>163,757</td></tr></table>

Note. t-statistics or robust t-statistics are in brackets.  
p < 0.1; p < 0.05; p < 0.01.

Column 3 of Table 5 shows that an increase in the fraction of business owners’ responses from direct competitors $( F r a c R e s p S a m e _ { \underline { i } t } )$ has a strong negative impact on a focal business’ performance, which suggests that the spillover efect of direct competitors’ responses is mainly a competition efect (negative spillover efect). However, an increase in the fraction of business owners’ responses from indirect competitors $( F r a c R e s p D i f f _ { i t } )$ has a significantly positive impact on a focal business’ performance, which suggests a positive spillover efect of indirect competitors’ responses. A possible explanation is that a focal restaurant does not have intense competition with a nearby restaurant in a diferent category. In fact, when a nearby restaurant attracts more customers by responding to online reviews, it may unintentionally benefit the focal restaurant. For example, Liu et al. (2014) demonstrate that the venues’ promotions not only significantly increase the number of customers but also bring more consumers to the local neighborhood. In our context, nearby business owners’ responses may attract more customers to their stores, and these customers may become aware of the focal restaurant. Essentially, nearby business owners’ responses may help bring more consumers to the neighborhood and may even benefit the focal restaurant if they are not direct competitors. In another context, Sahni (2016) shows that the ad exposure could remind consumers of other products that are associated with the advertised product in the consumer’s memory. Similarly, in our context, nearby business owners’ responses may remind consumers of the focal restaurant they have visited.

The implication from the estimation result of regression Equations (6) and (7) is that the externality of business owner responses depends on whether restaurants are direct competitors: (i) In general, the spillover efect of nearby restaurants’ responses is negative; (ii) If nearby restaurants are the focal restaurants’ direct competitors (same category), the spillover efect of nearby restaurants’ responses is negative; and (iii) If nearby restaurants are the focal restaurants’ indirect competitors (diferent categories), the spillover efect of nearby restaurants’ responses is positive.

## 4.4. When Do Business Owners Respond to Consumers’ Online Reviews?

In this section, we investigate which factors may afect management’s tendency to respond to customers’ comments. More specifically, we focus on the impact of review rating and competition intensity on business owners’ tendency to respond. Mayzlin et al. (2014) show that the firms have a greater incentive to post negative fake reviews about their competitors when competition is more intense. Similar logic can apply in our context: When competition is more intense, business owners may feel pressure and are more likely to engage with consumers. As for the existing review rating, a restaurant may want to improve its poor rating or keep its high rating by responding to customers comments. Both cases are theoretically plausible, so we examine the impact of review rating on business owners’ tendency to respond empirically. We use the following random efect model:

$$
\begin{array}{r l} O w n e r R e s p o n s e _ {i t} = & a _ {i} + \beta_ {0} + \beta_ {1} C o u n t R e s t _ {i} \\ & + \beta_ {2} A v e R e v i e w R a t i n g _ {i t} \\ & + \beta_ {3} C o n t r o l s + \varepsilon_ {i t}, \end{array}\tag{8}
$$

where OwnerRespons $\dot { \mathbf { \rho } } _ { i t }$ is our dependent variable indicating the number of times restaurant i responds to customers’ comments at time $t , C o u n t R e s t _ { i }$ is the number of restaurants in the zip-code region of restaurant $i ,$ AveReviewRating is the average review rating of restaurant i at time $\stackrel { \cdot \cdot } { t } , { ^ 4 }$ and $a _ { i }$ represents the random efect. We are interested in the coeficients on AveReviewRating and CountRest . However, these two independent variables might be endogenous in our context. In particular, AveReviewRating may be correlated with the unobserved restaurant quality or the restaurant promotions/deals. We will address these issues later using instrumental variables. The vector Control includes all controlled variables, i.e., (i) all zip-code level information of restaurant $i ,$ such as the population of each zip-code region, the median age in each zip-code region, and the mean household income in each zip-code region; and (ii) restaurant category dummies, monthly time dummies, and city dummies. The reason that we use a random efects model instead of a fixed efects model is that CountRest is a time-invariant variable. In a fixed efects model, all time-invariant variables are canceled out in a within transformation, and we can estimate the coeficient on CountRest . However, we can still obtain the coeficient on AveReviewRating , which is a time-varying variable, in a fixed efects model. The results of a fixed efects model will be presented later.

From column 1 of Table $6 ,$ we find that the coeficient on AveReviewRating is significantly negative and the coeficient on CountRest is significantly positive, which suggests that business owners are more likely to respond to consumer reviews when (i) average review rating is lower, and (ii) competition intensity is higher. In column $2$ of Table $6 ,$ the dependent variable is defined as a binary variable indicating whether restaurant i responds to customers’ comments in month t (0: no response; 1: response), and the results are similar. In columns 3 and 4 of Table 6, we use the robust statistics to address concerns about the failure to meet standard regression assumptions, such as unknown heteroskedasticity and possible cluster correlations in error terms. Failure to control for within-cluster error correlations can greatly understate true standard errors (Cameron et al. 2008). In columns 5 and 6 of Table $^ { 6 , }$ we control for more detailed information on restaurant reviews, such as standard error of review ratings at time t (SeReviewRating), average review length at time t (AveReviewLength), the number of reviews for this business at time t (ReviewCount), and the price range of restaurants.<sup>5</sup> The results are robust. In Online Appendix $\mathrm { E } ,$ we conduct additional analyses to further confirm that restaurants are more likely to respond to consumer reviews with very low ratings.

A key concern in our regression Equation (8) is the endogeneity problem of AveReviewRating . As we stated, in a random efects model, AveReviewRating may be correlated with the unobserved restaurant quality or the restaurant-side promotions. To address concerns about endogeneity of AveReviewRating , we use an instrumental variable approach to correct possible biases in columns 1 and 2 of Table 7. Following the prior literature on weather instruments (Moretti 2011, Qiu et al. 2015), we instrument for AveReviewRating with exogenous weather shocks. Moretti (2011) argues that severe weather shocks (e.g., heavy rain and heavy snow) can significantly reduce people’s willingness to ${ \bf g 0 }$ to movie theaters because of an increase in the cost of going out. Our argument is in line with the role of severe weather shocks. Consider a focal restaurant. Our intuition is that, if the weather is severe, only consumers who truly like the restaurant will choose to go because of a significant increase in the cost of going out. When the weather is nice, consumers who moderately like the restaurant may also choose to go because the cost of going out on a nice day is less. Using a simple cost-benefit analysis, we can see that the exogenous severe weather shocks can cause a selection in consumer reviews: Only consumers who truly like the restaurant will choose to go to the restaurant and then write reviews.<sup>6</sup> Therefore, the average review rating of the restaurant is higher during severe weather shocks.

In our specific context, we construct three weather instrumental variables to represent severe weather, i.e., BelowFreezingDays (the number of days in a month with the minimum temperature below 32<sup>◦</sup>F for the restaurant city), RainDays (the number of days in a month

Table 6. The Efect of Review Rating and Competition Intensity on Business Owners’ Responses

<table><tr><td>Variables</td><td>(1) Random effects: Total owner response counts by month as DV</td><td>(2) Random effects: Binary owner response as DV</td><td>(3) Random effects: Total owner response counts by month as DV, robust S.E.</td><td>(4) Random effects: Binary owner response as DV, robust S.E.</td><td>(5) More controls: Total owner response counts by month as DV</td><td>(6) More controls: Binary owner response as DV</td></tr><tr><td>CountRest</td><td>0.000179***[3.746]</td><td>5.78e-05***[4.721]</td><td>0.000179***[3.602]</td><td>5.78e-05***[4.373]</td><td>0.000236***[4.106]</td><td>2.49e-05**[2.024]</td></tr><tr><td>AveReviewRating</td><td>-0.148***[-105.4]</td><td>-0.0644***[-206.7]</td><td>-0.148***[-14.42]</td><td>-0.0644***[-25.43]</td><td>-0.158***[-110.9]</td><td>-0.0673***[-219.4]</td></tr><tr><td>Population</td><td>-1.98e-07[-0.375]</td><td>5.77e-09[0.0425]</td><td>-1.98e-07[-0.308]</td><td>5.77e-09[0.0376]</td><td>-1.34e-07[-0.210]</td><td>8.50e-08[0.608]</td></tr><tr><td>MedianAge</td><td>-0.00275***[-2.911]</td><td>-0.000321[-1.321]</td><td>-0.00275*[-1.829]</td><td>-0.000321[-1.211]</td><td>-0.00362***[-3.188]</td><td>-0.000176[-0.701]</td></tr><tr><td>MeanIncome</td><td>1.04e-06***[5.372]</td><td>3.79e-07***[7.677]</td><td>1.04e-06***[5.410]</td><td>3.79e-07***[7.446]</td><td>9.60e-07***[4.043]</td><td>2.59e-07***[4.945]</td></tr><tr><td>SeReviewRating</td><td></td><td></td><td></td><td></td><td>-0.152***[-37.64]</td><td>-0.0682***[-78.71]</td></tr><tr><td>AveReviewLength</td><td></td><td></td><td></td><td></td><td>-0.000507***[-22.58]</td><td>-0.000177***[-36.79]</td></tr><tr><td>ReviewCount</td><td></td><td></td><td></td><td></td><td>0.0460***[101.3]</td><td>0.00619***[60.74]</td></tr><tr><td>Price</td><td></td><td></td><td></td><td></td><td>0.0688***[8.045]</td><td>0.0125***[6.602]</td></tr><tr><td>Category dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>City dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.563***[14.11]</td><td>0.219***[21.53]</td><td>0.563***[7.884]</td><td>0.219***[15.70]</td><td>0.621***[12.62]</td><td>0.235***[21.76]</td></tr><tr><td>Observations</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td></tr></table>

Note. t statistics or robust t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

Table 7. The Efect of Review Rating and Competition Intensity on Business Owners’ Responses: IV and Other Robustness Checks

<table><tr><td>Variables</td><td>(1) Random effects IV: Total owner response counts by month as DV</td><td>(2) Random effects IV: Binary owner response as DV</td><td>(3) Fixed effects IV: Total owner response counts by month as DV</td><td>(4) Fixed effects IV: Binary owner response as DV</td><td>(5) Poisson regression: Total owner response counts by month as DV, robust S.E.</td><td>(6) Zero-inflated poisson regression</td></tr><tr><td>CountRest</td><td>0.000137***[2.830]</td><td>3.54e-05***[6.412]</td><td></td><td></td><td>0.000719***[3.321]</td><td>0.000778***[6.223]</td></tr><tr><td>AveReviewRating</td><td>-0.102***[-105.2]</td><td>-0.0488***[-212.7]</td><td>-0.146***[-103.6]</td><td>-0.0681***[-217.6]</td><td>-22.14***[-653.2]</td><td>-27.09***[-674.8]</td></tr><tr><td>Population</td><td>-3.23e-07[-0.455]</td><td>-1.13e-07[-0.653]</td><td></td><td></td><td>-6.80e-06*[-1.956]</td><td>-1.69e-06[-1.302]</td></tr><tr><td>MedianAge</td><td>-0.00289***[-2.781]</td><td>-0.000367[-1.461]</td><td></td><td></td><td>-0.0313***[-5.094]</td><td>-0.0572**[-2.176]</td></tr><tr><td>MeanIncome</td><td>1.07e-06***[5.058]</td><td>3.69e-07***[7.185]</td><td></td><td></td><td>2.68e-06*[1.833]</td><td>9.95e-07[1.592]</td></tr><tr><td>SeReviewRating</td><td></td><td></td><td>-0.167***[-42.65]</td><td>-0.0684***[-78.47]</td><td></td><td></td></tr><tr><td>AveReviewLength</td><td></td><td></td><td>-0.000475***[-21.90]</td><td>-0.000179***[-36.98]</td><td></td><td></td></tr><tr><td>ReviewCount</td><td></td><td></td><td>0.0477***[98.59]</td><td>0.00598***[55.65]</td><td></td><td></td></tr><tr><td>Category dummies</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>City dummies</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.573***[10.42]</td><td>0.214***[16.32]</td><td>0.502***[76.92]</td><td>0.288***[197.4]</td><td>1.681***[7.788]</td><td>0.803***[6.772]</td></tr><tr><td>Observations</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td></tr></table>

Note. t statistics or robust t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

with rain for the restaurant city), and SnowDays (the number of days in a month with snow for the restaurant city).

For the exogenous weather to be a valid IV for average review rating, it has to be (i) correlated with the average review rating and (ii) uncorrelated with the error term so that the exogenous variation of weather influences business owners’ responses only through the number of average review ratings. We have already argued that condition (i) is plausible because severe weather shocks can cause a selection in consumer reviews and increase average review rating. We also verify condition (i) by examining the first- stage regression of the IV approach: AveReviewRating are positively correlated with the three weather IVs (p < 0.05 for all three coeficients), which confirms our intuition. It is also well known that, if the correlation specified in condition (i) is weak, IV methods can be ill behaved and may cause severe inconsistency (Stock et al. 2002). To address this concern, we test whether our IVs are weak instruments by calculating the first-stage F statistics based on the method proposed by Stock et al. (2002). A high F statistic (44.65) suggests that the weather shocks are not weak instruments. Condition (ii) is plausible in our context because, depending on the controls included in our empirical model, these weather shocks should be orthogonal to the unobserved factors that could afect business owners’ responses.

In our context, weather is an exogenous source of variation, which can avoid many possible confounds. The exclusion restriction is plausible: The weather shocks should afect our dependent variable, i.e., business owners’ responses, only indirectly, through the correlation with the average review rating. Following Acemoglu et al. (2001), we conduct a test on the concern about the exclusion restriction by including the weather shocks in Equation (8): The coeficients on the three weather variables are not statistically significant after controlling for the average review rating. These results are encouraging and generate no evidence of a direct efect of weather shocks on business owners’ responses. The intuition is as follows: Assuming that the only impact of weather shocks on business owners’ responses is through the average review rating, the weather shocks should be insignificant in Equation (8), which also includes the average review rating.

We believe that our competition intensity measure, CountRest , is less likely to be endogenous, but we also instrument it with DistanceFromHighways, the driving distance of the centroid of each restaurant zip-code region from the nearest highway by following the prior literature (Duranton et al. 2014). Similarly, Distance-FromHighways is correlated with the number of restaurants in a zip-code region but is more exogenous. From columns 1 and 2 of Table 7, we find that our estimation results are robust: Business owners are more likely to respond to consumer comments when the average review rating is lower or competition intensity is higher. To further control for unobserved restaurant heterogeneity, we run the fixed efects IV estimation in columns 3 and 4 of Table 7. Note that, in the fixed efects, we are unable to estimate the coefficient on CountRest because all time-invariant variables are canceled out. However, the coeficients on AveReviewRating are similar, which suggests that our results are robust.

Moreover, since total owner response counts by month take on nonnegative integer values, we also examine count data models. In column 5 of Table 7, we conduct an analysis on a Poisson regression model, and the results are robust. Additionally, our count data has an excess of zero counts, so we also run a zero-inflated Poisson regression. The result is presented in column 6 of Table 7.

As a robustness check, we also use the number of restaurants in the same category as restaurant i in the zip-code region of restaurant i (CountSameRest <sup>)</sup> as an alternative competition intensity measure. For example, if restaurant i is a Mexican restaurant, the new measure of competition intensity is the number of Mexican restaurants in the zip-code region of restaurant i. The results are presented in Table 8: The coeficient on CountSameRest in Table 8 is 10 times larger than the coeficient on CountRest in Tables 6 or 7. The intuition is that an increase in the number of restaurants in the same category brings more competition than an increase in the number of restaurants that may come from any category. In Online Appendix A, we conduct an additional analysis on bidirectional dynamics between the online review ratings and the business owners’ responses using the panel vector autoregression (Chen et al. 2015), and visualize the dynamics through techniques such as the impulse response functions.

## 5. Discussion and Conclusions

In this study, we investigate the impact of management engagement, as measured by business owner responses, on the business performance measure using online review website Yelp.com. Our study fills an important gap in the literature by providing a deep understanding of the dynamics of online management engagement on business performance and the spillover efect of management response on nearby businesses. We address the endogeneity concerns posed by selfselected responses by adopting multiple causal identification strategies and establishing a robust quantitative relationship between the online management responses and the business performance measure.

## 5.1. Managerial Implications

Understanding the dynamics of business owner engagement with consumers using online social media platforms and its impact on business performance is a new area of research. Direct engagement through digital platforms is vital to building a relationship of trust with consumers. Businesses that do not connect with consumers using digital platforms may find themselves slowly losing ground, specifically by observing a negative impact on their key business performance measures as time goes by. We provide practical insights for businesses that would like to improve their key business performance measures by engaging with their consumers online to improve their experiences.

Table 8. The Efect of Competition Intensity: Same Category Restaurants

<table><tr><td>Variables</td><td>(1) Random effects: Total owner response counts by month as DV</td><td>(2) Random effects: Binary owner response as DV</td><td>(3) Random effects: Total owner response counts by month as DV, robust S.E.</td><td>(4) Random effects: Binary owner response as DV, robust S.E.</td></tr><tr><td>CountSameRest</td><td>0.00124**[2.098]</td><td>0.000203**[2.337]</td><td>0.00124**[2.087]</td><td>0.000203**[2.176]</td></tr><tr><td>AveReviewRating</td><td>-0.165***[-101.7]</td><td>-0.0854***[-225.7]</td><td>-0.165***[-18.35]</td><td>-0.0854***[-27.28]</td></tr><tr><td>Population</td><td>-5.31e-07[-1.024]</td><td>-1.28e-07[-0.964]</td><td>-5.31e-07[-0.868]</td><td>-1.28e-07[-0.861]</td></tr><tr><td>MedianAge</td><td>-0.00302***[-3.208]</td><td>-0.000419*[-1.728]</td><td>-0.00302**[-2.009]</td><td>-0.000419[-1.581]</td></tr><tr><td>MeanIncome</td><td>1.10e-06***[5.707]</td><td>4.02e-07***[8.170]</td><td>1.10e-06***[5.717]</td><td>4.02e-07***[7.917]</td></tr><tr><td>Category dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>City dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Constant</td><td>0.589***[15.09]</td><td>0.230***[23.00]</td><td>0.589***[8.185]</td><td>0.230***[16.24]</td></tr><tr><td>Observations</td><td>140,206</td><td>140,206</td><td>140,206</td><td>140,206</td></tr></table>

Note. t-statistics or robust t-statistics are in brackets.  
<sup>∗</sup> p < 0.1; <sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

First, our findings have direct implications for the business owners and the digital platforms (online review hosting companies). We observe that, in general, the launch of the new management response feature benefits businesses. This finding may not be surprising to researchers and practitioners. However, what is interesting is that the benefit is not observed in a consistent manner across all businesses. Only the businesses that choose to use the management response feature observe increases in check-ins. On the other hand, the businesses that are unaware of the management response feature launch on digital platforms, or are aware but choose not to use the management response feature, tend to remain at a disadvantage. Specifically, we observe a decrease in the number of check-ins for those restaurants that can, but do not use, the management response feature to engage with their customers. Certainly, ignorance about newly launched features to engage with consumers on social media is not bliss for businesses. Businesses must keep an eye on the dynamic and evolving features ofered by online media to efectively engage with their consumers. This practice becomes even more important for businesses such as local restaurants that may not have suficient resources or the technical know-how to use social media and engage with their consumers online. Such businesses should consider investing resources into engaging with consumers through social media by recruiting personnel or hiring third-party public relations companies that can handle social media and respond to reviews and comments.

Second, we provide insights into the spillover efect of online management responses on the nearby businesses. Despite engaging with consumers using online response features, businesses must pay close attention to the nearby businesses that are engaging with their consumers online. Without taking into account the online response strategies of nearby businesses, a business’ online response strategies may not be optimal. Spillover efect is negative in a scenario when the nearby restaurants are direct competitors. On the other hand, the focal business may benefit through the customer trafic pulled by other (indirect) businesses around the focal restaurants.

Third, spillover efect is dificult to measure directly by a focal business because of the lack of readily available information about the nearby restaurants that are using the online management response feature. A focal business may subtly observe a negative efect on its performance if the nearby competing businesses are also actively engaging online with their consumers. Digital platforms can help by developing a feature for businesses to follow nearby businesses. Instead of manually determining which nearby businesses are engaging with their consumers, businesses can receive regular updates on their dashboards about the names of their competitors, as well as if and when nearby competing businesses respond to consumers through business response features. Digital platforms can also develop analytical algorithms to identify the featured management responses and post them on the front page of the focal restaurant, as well as display them on the dashboard of nearby following restaurants. Such features would not only make the review-hosting site more attractive to its review writers, but would also make it easier for those business owners who do not invest time and efort in writing efective responses. Overall, the new features supported through digital platforms will help businesses develop the right engagement strategy, improve consumer experience, and generate more reviews and consumer trafic, which will ultimately open more revenue generating opportunities for the digital platforms and businesses. With more interactive business owner response features, digital platforms can improve the website’s trafic and possibly attract more business owners and consumers to engage with each other.

## 5.2. Future Research Directions

There are several possible extensions to our research. First, we use the number of mobile check-ins as a measure of business performance primarily because of the lack of availability of any other direct measure (such as restaurant revenue). We realize that the mobile checkin measure may not capture the visits of older consumers because they do not use smartphones or do not check in at restaurants using their smartphones. In other words, we may underestimate the efect of online management responses because older consumers can be afected by online management responses on Yelp, but their visits at restaurants are not reflected in mobile check-ins.<sup>7</sup> In the future, it would be interesting to use other measures of business performance to test the consistency of our results and findings. Second, in our study, we do not measure the efect of specific types of restaurants on the business performance measure. Small, local businesses may function under diferent operating conditions and financial constraints. They may lack awareness about online social media and may have limited resources to engage with consumers through responses to reviews on digital platforms. On the other hand, large-scale chain businesses have the resources and financial support to invest in consumer engagement on digital platforms. In the future, we would like to separately measure the impact of business responses on the performance of local and chain restaurants, and propose customized response strategies tailored to the specific type of restaurants. Third, it would be interesting to conduct more text analyses on online reviews and management responses. In Online Appendix $C ,$ we examine the moderating role of the length of online management responses. Additional analyses based on the content of online reviews and responses can be done in the future. Finally, the impact of online management responses is significantly positive overall, but for a single observation, the efect might be insignificant because a particular restaurant owner may write an inefective response. A future research direction is to examine which types of online management responses are more likely to attract consumers and enhance business performance.

## Acknowledgments

The authors thank the senior editor, associate editor, and anonymous reviewers for their detailed and constructive comments. The authors also thank Ashish Agarwal, Guodong (Gordon) Gao, Kartik Hosanagar, Sunil Mithas, and the seminar participants at Arizona State University, Tulane University, University of Texas at Austin, University of Maryland, Fogelman College of Business and Economics at the University of Memphis, and the 2017 Conference on Information Systems and Technology for helpful feedback/support.

## Endnotes

<sup>1</sup> See https://www.ncdc.noaa.gov/cdo-web/search (accessed July 17, 2016).

<sup>2</sup> CountRest is a time-invariant variable because in our data collection process we can only obtain the number of restaurants in each zipcode region in Yelp. Although this is a limitation of our data, the number of restaurants in a zip-code region should be relatively stable over time.

<sup>3</sup>As Cameron and Trivedi (2009) point out, $u _ { i t }$ induces overdispersion, so that the Poisson model has been generalized to control for overdispersion.

<sup>4</sup> The incentive to write online management responses may difer when restaurants have diferent review ratings. In particular, Yelp aggregates all reviews for a given business and prominently displays the average rating. However, when Yelp computes the average rating they round of to the nearest half star (Anderson and Magruder 2012). We provide an additional analysis on the rounding thresholds in Online Appendix D.

<sup>5</sup> The price range is the approximate cost per person for a meal including one drink, tax, and tip: \$ <sup></sup> inexpensive, \$\$ <sup></sup> moderately expensive, \$\$\$ <sup></sup> expensive, and \$\$\$\$ <sup></sup> very expensive.

<sup>6</sup> As we stated earlier in Section 3, Yelp uses its proprietary filtering algorithm to filter fraudulent or seemingly deceptive reviews. We collected only unfiltered reviews in this study, so the online reviews in our sample are less likely to be faked.

<sup>7</sup> The potential bias should not be large because usually older consumers are less likely to be active on Yelp and less likely to be afected by online management responses on Yelp. Moreover, the small potential bias may not be a problem because we underestimate the impact of online management responses but still find a significant efect. The true efect of online management responses should be larger (our estimates provide a lower bound for the efect of online management responses).

## References

Abadie A (2005) Semiparametric diference-in-diferences estimators. Rev. Econom. Stud. 72(1):1–19.

Acemoglu D, Johnson S, Robinson JA (2001) The colonial origins of comparative development: An empirical investigation. Amer. Econom. Rev. 91(5):1369–1401.

Anderson EG Jr, Parker GG, Tan B (2013) Platform performance investment in the presence of network externalities. Inform. Systems Res. 25(1):152–172.

Anderson ET, Simester D (2013) Advertising in a competitive market: The role of product standards, customer learning, and switching costs. J. Marketing Res. 50(4):489–504.

Anderson ET, Simester DI (2014) Reviews without a purchase: Low ratings, loyal customers, and deception. J. Marketing Res. 51(3):249–269.

Anderson M, Magruder J (2012) Learning from the crowd: Regression discontinuity estimates of the efects of an online review database. Econom. J. 122(563):957–989.

Angrist JD, Pischke JS (2008) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University Press, Princeton, NJ).

Auh S, Menguc B (2005) Balancing exploration and exploitation: The moderating role of competitive intensity. J. Bus. Res. 58(12): 1652–1661.

Autor DH (2003) Outsourcing at will: The contribution of unjust dismissal doctrine to the growth of employment outsourcing. J. Labor Econom. 21(1):1–42.

Bapna R, Umyarov A (2015) Do your online friends make you pay? A randomized field experiment on peer influence in online social networks. Management Sci. 61(8):1902–1920.

Bapna R, Ramaprasad J, Umyarov A (2016) Monetizing freemium communities: Does paying for premium increase social engagement? MIS Quart. Forthcoming.

Borah A, Tellis GJ (2016) Halo (spillover) efects in social media: Do product recalls of one brand hurt or help rival brands? J. Marketing Res. 53(2):143–160.

Brown GK, Mergoupis T (2010) Treatment interactions with nonexperimental data in Stata. Stata J. 11(4):545–555.

Cameron AC, Trivedi PK (2009) Microeconometrics Using Stata (Stata Press, College Station, TX).

Cameron AC, Gelbach JB, Miller DL (2008) Bootstrap-based improvements for inference with clustered errors. Rev. Econom. Statist. 90(3):414–427.

Chen H, De P, Hu YJ (2015) IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Inform. Systems Res. 26(3):513–531.

Chevalier JA, Mayzlin D (2006) The efect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Clemons EK (1991) Evaluation of strategic investments in information technology. Comm. ACM 34(1):22–36.

De Vries L, Gensler S, Leeflang PS (2012) Popularity of brand posts on brand fan pages: An investigation of the efects of social media marketing. J. Interactive Marketing 26(2):83–91.

Dranove D, Gron A, Mazzeo MJ (2003) Diferentiation and competition in HMO markets. J. Indust. Econom. 51(4):433–454.

Duncan G (2011) Survey: Negative online reviews change 80 pct of shoppers’ minds. Digital Trends. Accessed July 18, 2016, http:// www.digitaltrends.com/social-media/survey-negative-online -reviews-change-80-pct-of-shoppers-minds.

Duranton G, Morrow PM, Turner MA (2014) Roads and trade: Evidence from the U.S. Rev. Econom. Stud. 81(2):681–724.

Elejalde-Ruiz A (2015) Survey says more than half of shoppers check online reviews. Chicago Tribune (June 2). Accessed July 18, 2016, http://www.chicagotribune.com/business/ct-mintel-online -reviews-0603-biz-20150602-story.html.

Evans D, Oviatt J, Slaymaker J, Tapado C, Doherty P, Ball A, Saenz D, Wiley E (2012) An experimental study of how restaurantowners’ responses to negative reviews afect readers’ intention to visit. Four Peaks Rev. 2(1):1–13.

Feldman JM, Lynch JG (1988) Self-generated validity and other efects of measurement on belief, attitude, intention, and behavior. J. Appl. Psych. 73(3):421–435.

Forman C, Ghose A, Goldfarb A (2009) Competition between local and electronic markets: How the benefit of buying online depends on where you live. Management Sci. 55(1):47–57.

Garg R, Smith MD, Telang R (2011) Measuring information difusion in an online community. J. Management Inform. Systems 28(2): 11–38.

Gatignon H, Xuereb JM (1997) Strategic orientation of the firm and new product performance. J. Marketing Res. 34(1):77–90.

Gensler S, Völckner F, Liu-Thompkins Y, Wiertz C (2013) Managing brands in the social media environment. J. Interactive Marketing 27(4):242–256.

Goes PB, Lin M, Au Yeung CM (2014) “Popularity Efect” in usergenerated content: Evidence from online product reviews. Inform. Systems Res. 25(2):222–238.

Goh KY, Heng CS, Lin Z (2013) Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Inform. Systems Res. 24(1):88–107.

Goldfarb A, Xiao M (2011) Who thinks about the competition? Managerial ability and strategic entry in U.S. local telephone markets. Amer. Econom. Rev. 101(7):3130–3161.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride-sharing and alcohol related motor vehicle fatalities. MIS Quart. 41(1):163–187.

Gu B, Ye Q (2014) First step in social media: Measuring the influence of online management responses on customer satisfaction. Production Oper. Management 23(4):570–582.

Hinckley D (2015) New study: Data reveals 67% of consumers are influenced by online reviews. MOZ. Accessed July 18, 2016, https://moz.com/blog/new-data-reveals-67-of-consumers-are -influenced-by-online-reviews.

Hosanagar K, Fleder D, Lee D, Buja A (2014) Will the global village fracture into tribes? Recommender systems and their efects on consumer fragmentation. Management Sci. 60(4):805–823.

Hu N, Zhang J, Pavlou PA (2009) Overcoming the J-shaped distribution of product reviews. Comm. ACM 52(10):144–147.

Hu N, Bose I, Koh NS, Liu L (2012) Manipulation of online reviews: An analysis of ratings, readability, and sentiments. Decision Support Systems 52(3):674–684.

Iacovou CL, Benbasat I, Dexter AS (1995) Electronic data interchange and small organizations: Adoption and impact of technology. MIS Quart. 19(4):465–485.

Koenker R, Hallock K (2001) Quantile regression: An introduction. J. Econom. Perspect. 15(4):43–56.

Lewis R, Nguyen D (2015) Display advertising’s competitive spillovers to consumer search. Quant. Marketing Econom. 13(2): 93–115.

Li X (2016) Could deal promotion improve merchants’ online reputations? The moderating role of prior reviews. J. Management Inform. Systems 33(1):171–201.

Li Z, Agarwal A (2017) Platform integration and demand spillovers in complementary markets: Evidence from Facebook’s integration of Instagram. Management Sci. 63(10):3438–3458.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box ofice revenue. J. Marketing 70(3):74–89.

Liu Z, Duan JA, Ter Hofstede F (2014) Marketing spillovers of location-based mobile services. Working paper, University of Texas at Austin, http://ssrn.com/abstract<sup></sup>2578335.

Lowensohn J (2009) Yelp: Businesses may publicly respond to reviews. CNET (April 9). Accessed July 18, 2016, http://www.cnet.com/ news/yelp-businesses-may-publicly-respond-to-reviews/.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Sci. 62(12):3412–3427.

Mallett T, Sen A (2001) Does local competition impact interest rates charged on small business loans? Empirical evidence from Canada. Rev. Indust. Organ. 19(4):435–450.

Malthouse EC, Haenlein M, Skiera B, Wege E, Zhang M (2013) Managing customer relationships in the social media era: Introducing the social CRM house. J. Interactive Marketing 27(4):270–280.

Mantena R, Sankaranarayanan R, Viswanathan S (2010) Platformbased information goods: The economics of exclusivity. Decision Support Systems 50(1):79–92.

Mayzlin D (2006) Promotional chat on the Internet. Marketing Sci. 25(2):155–163.

Mayzlin D, Dover Y, Chevalier J (2014) Promotional reviews: An empirical investigation of online review manipulation. Amer. Econom. Rev. 104(8):2421–2455.

Menon K, Dubé, L (2000) Ensuring greater satisfaction by engineering salesperson response to customer emotions. J. Retailing 76(3):285–307.

Mithas S, Krishnan MS (2009) From association to causation via a potential outcomes approach. Inform. Systems Res. 20(2):295–313.

Moretti E (2011) Social learning and peer efects in consumption: Evidence from movie sales. Rev. Econom. Stud. 78(1):356–393.

Mukherjee A, Kumar A, Liu B, Wang J, Hsu M, Castellanos M, Ghosh R (2013) Spotting opinion spammers using behavioral footprints. Proc. 19th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 632–640.

Naylor RW, Lamberton CP, West PM (2012) Beyond the “like” button: The impact of mere virtual presence on brand evaluations and purchase intentions in social media settings. J. Marketing 76(6):105–120.

Pizzutti C, Fernandes D (2010) Efect of recovery eforts on consumer trust and loyalty in e-tail: A contingency model. Internat. J. Electronic Commerce 14(4):127–160.

Qiu L, Tang Q, Whinston AB (2015) Two formulas for success in social media: Learning and network efects. J. Management Inform. Systems 32(4):78–108.

Rafaeli A (1989) When clerks meet customers: A test of variables related to emotional expressions on the job. J. Appl. Psych. 74(3): 385–393.

Reynolds FD, Wells WD (1977) Consumer Behavior (McGraw Hill, New York).

Rishika R, Kumar A, Janakiraman R, Bezawada R (2013) The efect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Inform. Systems Res. 24(1):108–127.

Roehm ML, Tybout AM (2006) When will a brand scandal spill over, and how should competitors respond? J. Marketing Res. 43(3):366–373.

Sahni NS (2016) Advertising spillovers: Evidence from online fieldexperiments and implications for returns on advertising. J. Marketing Res. 53(4):459–478.

Shen W, Hu YJ, Rees J (2015) Competing for attention: An empirical study of online reviewers’ strategic behaviors. MIS Quart. 39(3):683–696.

Sherman E, Mathur A, Smith RB (1997) Store environment and consumer purchase behavior: Mediating role of consumer emotions. Psych. Marketing 14(4):361–378.

Sorce P, Perotti V, Widrick S (2005) Attitude and age diferences in online buying. Internat. J. Retail Distribution Management 33(2):122–132.

Stock JH, Wright JH, Yogo M (2002) A survey of weak instruments and weak identification in generalized method of moments. J. Bus. Econom. Statist. 20(4):518–529.

Thomas JB, Peters CO, Howell EG, Robbins K (2012) Social media and negative word of mouth: Strategies for handling unexpecting comments. Atlantic Marketing J. 1(2):Article 7.

Tucker C, Zhang J (2011) How does popularity information afect choices? A field experiment. Management Sci. 57(5):828–842.

Turner M (2016) An unlikely source predicted Chipotle’s disastrous quarter, and it says a lot about the future of investing. Business Insider. Accessed July 18, 2016, http://www.businessinsider .com/foursquare-data-predicted-chipotle-results-2016-4.

Van Alstyne MW, Parker GG, Choudary SP (2016a) Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work For You (Norton, New York).

Van Alstyne MW, Parker GG, Choudary SP (2016b) 6 reasons platforms fail. Harvard Bus. Rev. (March 31), https://hbr.org/2016/ 03/6-reasons-platforms-fail.

Walter E (2014) 40 eye-opening customer service quotes. Accessed August 11, 2016, http://www.blackcofee.com/brand-related/ branding-quotes/675.

Wang L, Gopal R, Shankar R, Pancras J (2015) On the brink: Predicting business failure with mobile location-based checkins. Decision Support Systems 76:3–13.

Wang A, Zhang M, Hann IH (2018) Socially nudged: A quasi-experimental study of friends’ social influence in online product ratings. Inform. Systems Res., ePub ahead of print May 10, https://doi .org/10.1287/isre.2017.0741.

Xia L (2013) Efects of companies’ responses to consumer criticism in social media. Internat. J. Electronic Commerce 17(4):73–100.

Ye Q, Gu B, Chen W (2010) Measuring the influence of managerial responses on subsequent online customer reviews—A natural experiment of two online travel agencies. Working paper, Harbin Institute of Technology, Harbin, China, https://ssrn .com/abstract<sup></sup>1639683.

Yelp (2016) 10 things you should know about Yelp. Accessed July 18, 2016. http://www.yelp.com/about.

Zahra SA (1993) Environment, corporate entrepreneurship, and financial performance: A taxonomic approach. J. Bus. Venturing 8(4):319–340.

Zeithaml VA, Berry LL, Parasuraman A (1996) The behavioral consequences of service quality. J. Marketing 60(2):31–46.

Zhang X, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601–1615.
