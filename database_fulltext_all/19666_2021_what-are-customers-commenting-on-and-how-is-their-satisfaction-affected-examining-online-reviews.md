---
otero_id: 19666
otero_key: "8EGC2TNM"
title: "What are customers commenting on, and how is their satisfaction affected? Examining online reviews in the on-demand food service context"
authors: "Xun Xu"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113467"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

What are customers commenting on, and how is their satisfaction affected? Examining online reviews in the on-demand food service context

ELSEVIER Decision Support Systems

Xun Xu

![](/api/attachments/8EGC2TNM/fulltext/images/94b50f9bba78670b7609a828cc14a06cc3daace0429f626d0e609f3a69d4fa8c.jpg)

PII: S0167-9236(20)30222-0

DOI: https://doi.org/10.1016/j.dss.2020.113467

Reference: DECSUP 113467

To appear in: Decision Support Systems

Received date: 10 July 2020

Revised date: 27 November 2020

Accepted date: 27 November 2020

Please cite this article as: X. Xu, What are customers commenting on, and how is their satisfaction affected? Examining online reviews in the on-demand food service context, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113467

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# What Are Customers Commenting On, and How Is Their Satisfaction Affected? Examining Online Reviews in the On-Demand Food Service Context

Xun Xu

Department of Management, Operations, and Marketing, College of Business Administration, California State University, Stanislaus, One University Circle, Turlock, CA, 95382, United States (xxu@csustan.edu) Abstract

The on-demand economy has prospered with the rapid development of digital platforms. Many customers use on-demand service platforms to order services and then post online reviews. Using textmining approaches, this study examines customers’ online review-writing behavior and their overall ratings in their reviews to measure their overall satisfaction. We find that customers comment on the main service provider, the restaurants, and the auxiliary service providers, which include the drivers and on-demand service platform; in their online customer reviews, which are posted on the restaurants’ web pages on the on-demand service platform. From text regressions, we found the determinants of customer satisfaction with the restaurants through their online reviews. There is a spillover effect from the performance of auxiliary providers on customer satisfaction with the main provider. That is, the performance of the drivers and the platform affects customers’ overall satisfaction with the restaurants. offered by the restaurants to show their overall satisfaction. Further, we find the type of listed merchants categorized by their properties (i.e., chain or independent) and participation in the platform programs affect the influence of the various attributes, offered by different providers, on customer satisfaction with the main provider. The findings shed light on the determinants of customers’ overall satisfaction and urge improvement in collaboration and coordination between various participants in the on-demand service context.

Keywords: On-demand service, customer satisfaction, online customer reviews, spillover effect

## 1. INTRODUCTION

With the rapid development of information technology, the platform economy is emerging and developing swiftly (Dann et al., 2020). More and more customers tend to utilize the advantage of the digital platforms to shop online and then write and post their reviews (Biswas et al., 2020). Online customer reviews have two aspects of significance to their business value. First, they can affect future customer demand through the electronic word-of-mouth (eWOM) effect. Second, they can help businesses understand customers’ consumption experiences and satisfaction.

Previous studies about online customer reviews (e.g., Mitra & Jenamani, 2020; Moon et al., 2019) have focused mainly on customers’ online reviews of the main provider of a product or service. For example, Mitra and Jenamani (2020) analyzed customers’ online comments about products posted on business-to-consumer (B2C) or consumer-to-consumer (C2C) e-commerce platforms, and Moon et al. (2019) focused on customers’ comments about hotels on third-party booking platforms. These platforms ompanies expand their distribution channels to reach customers.

The development of the platform economy has triggered more varieties of platforms (Dann et al., 2020). One of these forms is the on-demand service platform, which has accumulated a large customer d service platforms is to match customer demand with an intermediary upon receiving customer orders instead of encouraging customers to make reservations in advance (Bai et al., 2019). This requires the platform to respond quickly to customers’ orders and to seek optimal solutions to match supply and demand (Choi et al., 2020). On-demand service platforms, such as Uber in the United States, Didi in China, and Ola in India, have been proliferating worldwide (Tong et al., 2020). These on-demand service platforms facilitate the prosperity of the on-demand economy (Taylor, 2018).

The on-demand service platform in the on-demand economy is multifunctional in addition to being a traditional online distributor (Choi et al., 2020). In addition to attracting customer demand, it seeks an optimal solution for the supply, such as merchants and drivers to fill orders. In this way, a successfully completed order requires a high level of real-time coordination among various participants in addition to the merchants as the main providers (Bai et al., 2019). Customers seek service and support from the listed merchants and from other participants, such as the deliverymen and the platform.

Although previous studies (e.g., Xiang et al., 2015; Xu, 2020) have focused mainly on online customer reviews within the traditional platform context, online customer reviews in the on-demand service platform context have been rarely discussed. To fill this gap in the literature, via the empirical evidence from the on-demand food service platform Grubhub.com, we analyzed online customer reviews about the restaurants in the on-demand economy context using text-mining approaches, including latent semantic analysis and text regression. The on-demand food service platforms serve as typical examples that incorporate the common characteristics of general on-demand service platforms (Tong et al., 2020). On-demand food service platforms are popular all over the world: for example, Eleme and Meituan in China; Deliveryhero in Germany; Deliveroo and Just Eat in the United Kingdom; and DoorDash, Grubhub, and Uber Eats in the United States (Tong et al., 2020). The trend of onincrease further in upcoming years (Technavio, 2020).

The objective of this study is to examine the determinants of customers’ overall satisfaction with raised three research questions, which are based on the features of the on-demand food service economy. First, although customers are asked to comment on and evaluate their satisfaction with the main provider, (the restaurant), the production and fulfillment of orders require a high level of coordination among various participants, including the on-demand service platform and the driver. Therefore, customers may comment in their online reviews on both the main provider—the restaurant—and auxiliary service providers, such as the platform and drivers, which affects their overall satisfaction. Figure 1 presents a sample of online customer reviews about their consumption experience from a restaurant that participated in the Grubhub Plus program network from Grubhub.com, a popular on-demand food service platform.

## Figure 1. Online Customer Reviews on Grubhub.com

I ordered about 45 minutes before the restaurant closed. Grubhub wasn't updating the status of my order's arrival, so I called India Quality. It was after closing, but the gentleman who answered the phone knew exactly what and where my order was was. He said it would be arriving any minute. In fact, while I was on the phone with him, the driver was calling. Excellent customer service! Plus, the food arrived wellpackaged and piping hot. Portions were generous and absolutely delicious! I'll definitely order from India Quality agin!

![](/api/attachments/8EGC2TNM/fulltext/images/2027aac444eb62231c95fee62d8468d7bdb30c38aced6489b361cce887fb9029.jpg)

From Figure 1, we can see that customers not only comment on the product (i.e., food) and customer service, but also comment on the drivers and the platform. Thus, in this study, we seek to investigate the existence of the spillover effect from the performance of the auxiliary providers on customers’ overall satisfaction with the main provider. In other words, how do the performances of the platform and driver, as the auxiliary providers, affect the customers’ overall satisfaction with the main provider? In this study, we use customers’ overall ratings of their orders as a measure of their overall satisfaction (Chatterjee, 2019). In this way, our first research question is as follows: Do customers comment on the platform and drivers when they evaluate the restaurants? And if the answer is yes, how does the performance of the platform and the driver affect customers’ overall satisfaction with the restaurant?

Second, customers place orders that cost different amounts. Higher costs increase the perceived risk of the online purchase and affect the perceived performance of the service providers (Homburg et al., 2005). This may then influence customers’ online review behavior and overall satisfaction. Therefore, we raised the second research question: How does the cost of the order affect the influence of the various attributes, offered by different providers, on the customer’s overall satisfaction?

Third, the restaurants have various types, depending on whether they are chain or independent. Chain restaurants have standardized operations, product and service offerings, and brand effects

(Mandabach et al., 2005). Thus, customers may be highly familiar with them, which affects their expectations and consequent satisfaction (Park et al., 2019). Therefore, our third research question is as follows: Do the types of the restaurants (i.e., chain versus independent) affect the influence of various attributes, offered by different providers, on customer satisfaction?

Fourth, restaurants can choose various options when participating in the programs offered by the on-demand service platform. Restaurants that participate in the program usually meet certain criteria suggested by the platform, have certain common features, and are recommended by the platform (Xu, 2020). These factors may all influence the satisfaction of customers when they receive products and services (Zhang et al., 2010). Therefore, our fourth research question is as follows: What is the moderating role of the restaurants’ involvement with the programs offered by the on-demand service satisfaction? This study’s findings provide an opportunity for participants in the on-demand service satisfaction. These findings urge various participants to collaborate with each other to improve.

The contribution of this study mainly lies in the following aspects. First, this is the first study to analyze how the performance of auxiliary providers affects customer satisfaction with the main providers. Thus, it is the first study to reveal how the interrelationships between the performances of all participants affect customer satisfaction in the on-demand service context. Second, we discuss how the cost of the order, the type of the merchant, and the programs offered by the platform affect the influence of various attributes on their overall satisfaction. The findings of this study urge improvement and provide guidance for various participants to engage in intensive collaboration and coordination in the on-demand service context.

The rest of the study is organized as follows. Section two elaborates the theoretical foundation of this study and reviews the relevant literature. Section three develops the hypotheses. Section four describes the data and research methodology. Section five presents the results, which are discussed in section six. Section seven discusses the theoretical and managerial implications. Section eight concludes the study and proposes directions for future studies.

## 2. THEORETICAL BACKGROUND AND LITERATURE REVIEW

## 2.1 Theoretical Background

The theoretical background of this paper lies mainly in the integrative service qualitysatisfaction theory (De Ruyter et al., 1997). The integrative service quality-satisfaction theory (De Ruyter et al., 1997) highlights the roles of three important elements in determining customer satisfaction: expectation, service quality, and the customers’ satisfaction with the entire consumption experience.

The integrative service quality-satisfaction theory (De Ruyter et al., 1997) aligns with a series of theories about customer satisfaction. The integrative service quality-satisfaction theory shares a coherent foundation with the SERVQUAL model that elaborates customers’ perceived service quality (Parasuraman et al., 1988, 1991). The SERVQUAL model explains the process that customers use to al., 1988, 1991). That is, customers’ overall satisfaction is determined by the gap between their preconsumption expectation and the perceived quality of the service or product. When the perceived quality meets or exceeds the customers’ expectation, the customers are satisfied; otherwise, the customers are dissatisfied.

The on-demand food delivery service is offered by a group of providers including restaurants, which are the main providers of the products (the food) and service offerings (e.g., the packaging of the food). The on-demand service platform offers the technology to facilitate customers’ information search, the transaction, and other steps in the ordering process. Both the restaurants and the platform offer aftersales service communication with customers to deal with ordering issues. Additionally, the platform and the driver oversee the fulfillment process. The platform is responsible for matching demand for the food by supplying the driver, who is the person who executes the delivery process (Tong et al., 2020).

The integrative service quality-satisfaction theory (De Ruyter et al., 1997) characterizes customers’ satisfaction with consumption with their feelings about the entire consumption experience and describes its important role in affecting customers’ overall satisfaction. This aligns with the cognitive-affective model (Caro & García, 2007), which describes customers’ cognitions, such as the evaluation of the providers, their affective elements, and the way the customers’ emotions influence their satisfaction. This provides the theoretical groundwork for the formation of customer satisfaction with the restaurant. Instead of being determined solely by the service quality of the restaurant, customer satisfaction can be affected by the whole consumption experience and all the providers related to this consumption, including the on-demand service platform and the providers who fill the order.

## 2.2 Literature Review

Our study is related to two fields of literature: online customer reviews and on-demand service

## 2.2.1 Online Customer Reviews

The literature for online customer reviews is extensive. Previous studies have examined two flect their satisfaction: the content and its linguistic characteristics. Regarding content, online customer re provide an open structure for customers to describe their consumption experi the providers. Berezina et al. (2016) used text analytic methods to identify the determinants o customer satisfaction and dissatisfaction through online customer reviews of hotels. Xiang et al. (20 15) focused on the frequencies of the keywords that customers used in their online reviews to infer their role in affecting customer satisfaction. Regarding linguistic characteristics, previous studies (e.g., Salehan & Kim, 2016; Zhao et al., 2019) have focused on the diversity, length, readability, sentiment, and subjectivity of online customer reviews. Zhao et al. (2019) found that the linguistic styles of online customer reviews indicate customer satisfaction with the consumption experience. They found that attributes such as higher diversity and sentiment, lower subjectivity and readability, and the longer length of reviews show customers are more satisfied. Additionally, Salehan and Kim (2016) discussed the sentiment and length of the review title in addition to the review text, and they found that the linguistic characteristics of the review title and the text play different roles. Our study focused on how the content of online reviews reflects customer overall

satisfaction, and thus it is categorized as the first type of online review research following the research approach of topic modeling (Huang et al., 2018).

Online customer reviews are often posted on platforms. The majority of previous studies examining online customer reviews (e.g., Berezina et al. 2016; Xu, 2020) mainly focused on customers’ comments about the products and services offered by the providers. These providers are usually from a single party, such as accommodation providers in guest reviews (e.g., Xu, 2020), airlines in passenger reviews (Sezgen et al., 2019), and hospitals or physicians in patient reviews (e.g., Ko et al., 2019). Our study examines online customer reviews from a comprehensive perspective as reflected in three facts. First, we examine how customers post their reviews on the on-demand service platform to comment on how various providers, rather than a single party, fulfill their orders. Seco d, we analyze how the cost of different providers on customer overall satisfaction. Third, we examine the moderating effect of different types of providers on customer reviews from the perspective of both the restaurant and the platform program.

## 2.2.2 On-Demand Service Platforms

Traditional platforms serve as an intermediary, helping merchants expand their distribution channels to connect with customers (Roma et al., 2016). Thus, customers mainly comment on the merchants, who are the only providers to fill their orders (Berezina et al., 2016). However, ondemand service platforms are quite different from traditional platforms, as is reflected in the following three aspects. First, the on-demand service platforms play multiple roles in addition to being distributors (Taylor, 2018). A key objective for an on-demand food platform is to ensure a match between the supply (e.g., the drivers) and the demand (e.g., customers’ orders). Thus, the platform has various functions and responsibilities, including facilitating a list of merchants and the customers’ information search, recruiting and assigning drivers to fulfill the orders, and providing customer service and support. Second, various participants are involved in the completion of a customer’s order (Choi et al., 2020). For an on-demand food platform, restaurants are the main provider, offering the product, food, and related packaging service that are the core reasons for customer purchases. Drivers are assigned by the platforms and physically deliver the food to customers. Customers seek support for information and service from the platforms when issues occur. Thus, significant coordination is needed among the various stakeholders to fulfill the order (Tong et al., 2020). Third, the supply and demand for the ondemand platforms is dynamic and varies in real time. Both the supply and demand are difficult to predict, and order fulfillment requires quick response times and dynamic analytics (Bai et al., 2019).

Van der Burg et al. (2019) summarized the three interrelated characteristics of on-demand services, which are high availability, quick responsiveness, and high scalability. The high degree of availability includes three dimensions, which are quantity, time, and location. The quick quick responsiveness is defined by the interval between the customers’ service requests and consumption. High scalability entails on-demand service that provides the exact amount of required resources with high accuracy during the required time. Customers value the flexibility and functionality of the unique services offered by on-demand service platforms, which increase their incentives to adopt the platform which may result in loss aversion behavior and sensitivity to the performance of the on-demand services (Choi et al., 2020; Delgosha & Hajiheydari, 2020).

Although on-demand service platforms are rapidly emerging and developing, relatively few distribution platforms. In particular, customers’ satisfaction with the products and services offered by the on-demand service platform and the listed merchants has barely been discussed. Although previous studies have discussed online customer reviews of the merchants (e.g., Xiang et al., 2015; Xu, 2020), few studies, if any, have focused on online customer review behavior and their reflected satisfaction in the context of on-demand service platforms. This study fills in the aforementioned gaps in the literature by analyzing customer online reviews and reflected satisfaction.

## 3. HYPOTHESIS DEVELOPMENT

## 3.1 The Influence of Auxiliary Service on Customer Satisfaction with the Main Provider

Customers mainly pay for the core products and services for their consumption (Stangl et al., 2017). However, the core and auxiliary products and services affect their overall satisfaction, although the core attributes have greater influence (Zhao & Dholakia, 2009). According to the integrative service quality-satisfaction theory (De Ruyter et al., 1997), the perception of the entire consumption experience affects customer satisfaction with the main provider. The influence of the auxiliary service, offered by the on-demand service platform and driver, on customer satisfaction with the main provider can be either direct or indirect. Directly, the high-quality performance of customer support from the platform facilitates both the customers’ information search and the transaction process, which together reduce their hassle costs, and thus increase their satisfaction (Zhao & Dholakia, 2009). A driver who demonstrates high-quality performance ensures prompt delivery, which preserves the quality of the food (Tong et al., 2020). Indirectly, the appropriate attitude and behavior of the driver and the platform employees enhances the customers’ positive consumption emotions, which increase their satisfaction (Lee et al., 2012).

According to attribution theory (Fiske & Taylor, 1991), when customers evaluate the main use information to form causal judgements and ons that cause the high or low performance of the ev tion. However, customers can attribute the main providers’ possible reasons. First, information asymmetry may make it difficult to identify the exact reason for the performance (Mavlanova et al., 2012). For example, cold food could be caused by late delivery, inappropriate food production, or both. In this way, customers may attribute the low performance of the core product to restaurants instead of the drivers. Second, according to cognitive bias theory (Haselton et al., 2005), customers may have a cognitive bias that leads them to illogically interpret the causes of poor performance. Customers can be emotional and subjective, which results in perceptual distortion and inaccurate judgement (Kahneman & Tversky, 1972) and, thus, they may attribute the poor performance caused by the platform or the driver to the restaurant. Third, according to the unconscious thought theory (Dijksterhuis, 2004), customers may be performing subconscious information processing that includes both cognitive and affective elements, leading to evaluations of the main providers that include various unconscious elements about the platform and the driver. Therefore, based on the preceding discussion, this study raises the following hypothesis:

H1: In the on-demand service context, customers’ comments on auxiliary providers’ performance in online reviews affect their satisfaction with main providers.

## 3.2 The Moderating Role of the Cost of an Order in Affecting the Influence of Various Attributes on Customer Overall Satisfaction

Cost is an important factor that influences customers’ psychology and purchase behavior (Alalwan, 2020). Cost affects customers’ perceptions of the quality and utility of their consumption (Homburg et al., 2005). This can change the relationship between expectation and perceived quality, which influences their perception and satisfaction of their c onsumption experience (Nam et al., 2020). This affects how customers comment in their revie

Although online purchasing in the on-demand service context has brought significant s is the perceived risk caused by the physical distance between customers and providers; thus, customers cannot physically examine products before they purchase them (Forsythe & Shi, 2003). The higher cost of an order increases the perceived risk because of the possible monetary loss if the performance is poor (Zhuang et al., 2018). This makes customers more cautious about their purchases and prompts a more serious attitude toward their consumption before and after their purchases, as reflected in information searches and online customer review writing, respectively (Bauer et al., 2006). In addition, the higher cost of the order tends to make customers more rational about their purchases and prompts them to use their cognition to evaluate their consumption experience (Saab & Botelho, 2020). In this way, they tend to focus on the core product and service attributes to reveal their overall satisfaction with the main provider. Therefore, this study hypothesizes the following:

H2: The cost of the order enhances the influence of the various attributes, offered by different providers, on customer satisfaction with the main provider.

## 3.3 The Moderating Role of the Type of the Merchant in Affecting the Influence of Various

## Attributes on Customer Overall Satisfaction

The merchants and programs offered by the platform come in different types, which affect customers’ expectations and perceptions of their consumption experience. The restaurants in this study can be either chain or independent restaurants. Independent restaurants often have unique features that give them competitive advantages, inducing customers to comment on these product or service attributes in their online reviews, which provide more information to other customers for altruistic motives or elaborate on the reasons they like or dislike these restaurants (Xu, 2019). The chain restaurants, which causes customers to be more familiar with them and have clearer expectations (Harris et al., d less time on an information search for chain restaurants when they order (Bauer et al., 2006). Cust may comment less on their products or expected and familiar to the majority of customers (Xu, 2019). Therefore, we propose the following hypothesis:

H3: The type of the listed merchant affects the influence of the various attributes, offered by different

## 3.4 The Moderating Role of the Platform Program in Affecting the Influence of Various

## Attributes on Customer Overall Satisfaction

The programs offered by the platform categorize the merchants into two types: the merchants who participate in the program and those who do not. The merchants who are in the programs have the same characteristics specified by the programs, which creates for customers a consistent and coherent image and expectation of those merchants (Xu, 2020). Customers can show more favor toward the merchants in the programs offered by the platform because they perceive less risk from those merchants as the merchants are endorsed by the platform’s reputation and because the common features of the

merchants in the programs are familiar to the customers (Zhang et al., 2010). Thus, customers tend to commend both the merchants and the platform if the merchants perform well. If customers believe that merchants are more dependent on the platform, customers are more likely to blame both the platform and the listed merchants in the platform program if the merchants perform poorly (Kim et al., 2014). This is because customers believe that the merchants and the platform are interrelated and that the platform should play a more intensive role in regulating and monitoring the performance of the merchants if they are in the program offered by the platform (Carbó-Valverde et al., 2009). Therefore, we propose the following hypothesis:

H4: The platform programs affect the influence of the various attributes, offered by different providers, on customer satisfaction with main provider.

## 4. DATA AND METHODOLOGY

## 4.1 Data Collection

Grubhub featured over 300,000 restaurants in over 4,000 cities in the U.S. Annual sales are nearly \$6 billion, and daily orders are more than 516,000 on average. Grubhub serves more than 24 million active diners (Grubhub, 2019). Customers who order food from Grubhub.com can comment and post their online reviews on Grubhub’s site.

Our search criteria for online customer reviews follow the rules below. First, based on the sample selection methodologies used in previous studies (e.g., Xiang et al., 2015), we searched online customer reviews from restaurants listed on Grubhub that are located in 100 of the largest U.S. cities based on the U.S. Census Bureau’s (2019) population estimate. Second, we narrowed down to the restaurants that have customer comments available. The restaurants that only had average customer ratings but did not have written reviews were filtered out. Third, to ensure that the customer reviews reflected the most updated performance of the restaurants, we collected the reviews from the restaurants’ webpage on Grubhub’s platform, and these reviews needed to have been written within the last six months (from March 15 to September 15, 2020). The data sets contained 27,286 reviews from 8,415

restaurants. For each review, we collected the textual comments, the information about the food the customer ordered, and the customer’s overall rating of the restaurant.

## 4.2 Feature Engineering

Online customer reviews provide a stage for customers to fully describe their consumption experience and evaluate the providers. However, the open structure and the substantial number of online customer reviews can cause information overload, which creates challenges for analysis (Zhu et al., 2018). Traditional text analytical approaches such as content analysis are difficult or even impossible to use when dealing with substantial online customer reviews. In this study, we utilized latent semantic analysis (LSA) to extract the hidden semantic structures from words, phrases, and sentences in the natural language of humans. LSA is one of the typical approaches of topic modeling and can cluster the text into various factors depending on the topics (Xu, 2020).

Following previous studies (e.g., Kulkarni et al., 2014), we used RapidMiner software to conduct LSA in three main steps. The first step was to preprocess the textual reviews. First, to avoid the unnecessary increase of dimensions in the term frequency matrix, we changed all letters into lowercase and removed all trivial words. The trivial words include all tokens that do not have actual meaning, such as ―are‖ and ―the,‖ and all tokens fewer than or equal to two letters, such as ―a‖ and ―an.‖ We then used a term-stemming technique to identify words with the same roots. For example, the words ―excitement,‖ ―excited,‖ and ―exciting‖ have the same roots (―excite‖) and thus were classified as one token. After that, we invoked an n-gram algorithm to identify the phrases that were repeated and appeared frequently. In this study, we set n equal to 3. In this way, the phrases such as ―tasty food,‖ ―restaurant staff,‖ and ―customer support‖ can be identified.

The second step was the transformation of the term ―frequency matrix.‖ In this step, we used a term-frequency–inverse-document-frequency weighting method (Husbands et al., 2001) to achieve term-frequency matrix transformation. In this way, the rare terms can be weighed more heavily, the common terms can be discounted to ensure uniqueness, and the commonality of each document can be identified (Sidorova et al., 2008). The weights $w _ { i j }$ in the transformed term-frequency matrix were calculated using the formula of $w _ { i j } = t f _ { i j } \times i d f _ { i }$ . In detail, the term ―frequency‖ $t f _ { i j }$ was calculated by $t f _ { i j } = n _ { i j } / n _ { j }$ , in which $n _ { j }$ represents the total number of tokens in the entire document j . After that, we calculated the inverse document frequency through the formula of $i d f _ { i } = l o g ( N / d f _ { i } )$ , in which N represents the number of documents in total, and $d f _ { i }$ shows the frequency of token i appearing in the document.

Last, we conducted the third step of LSA, which is singular value decomposition (SVD). Referring to previous research (e.g., Evangelopoulos et al., 2012; Hopcroft & Kannan, 2012), we calculated the SVD matrix X through the product of three matrices, that is, $X _ { _ { a b } } = A _ { _ { a a } } B _ { _ { a b } } C _ { _ { b b } } ^ { T }$ . In detail, matrix A is an orthogonal matrix with the orthonormal eigenvectors of $M M ^ { T }$ as its columns. Matrix B is a a diagonal matrix containing the square root of the $\mathrm { e i _ { \dot { 5 } } } = \dot { ~ }$ values from the matrix of A or C , and matrix C is the transpose of an orthogonal matrix with the orthonormal eigenvectors $M ^ { T } M$ as its columns. In the SVD, matrix A can be viewed as containing a points in a b-dimensional space. Referring to previous studies (e.g., Hopcroft & Kannan, 2012), we calculated the optimal k-dimensional subspace by the algorithms to best fit this set of po distances to the subspace.

## 4.3 Text Regression

After LSA, following previous studies (e.g., Ngo-Ye & Sinha, 2014), we conducted text regressions to analyze the textual vector space of each online customer review for each latent textual factor, namely, the attributes mined from LSA. The independent variables include the following three aspects, as shown in Eq. (1).

$$
\text { Overall\_rating } _ {i} = \beta_ {0} + B _ {1} X _ {1} + B _ {2} X _ {2} + B _ {3} X _ {3} + B _ {3} X _ {4} + \varepsilon_ {i}, \tag {1}
$$

where in Eq. (1), i represents the review $i ; X _ { I }$ is a vector in the form of $\left[ x _ { 1 1 } , x _ { 1 2 } , . . . , x _ { 1 f } \right]$ representing the coordinate values of each review on each latent factor $( 1 , 2 , \ldots f )$ mined from the LSA. Technically, the high coordinate value of the review on a particular latent factor shows that the review has a high loading on the corresponding factor. Practically, it shows the customer comments more on that factor (a specific product or service attribute) in the review. Namely, the review places more relevance on the corresponding latent textual factors. To show this visually, we present Table 1. In the matrix of Table 1, the element $x _ { n f }$ represents the loading (the coordinate value) of review n on factor $\cdot f .$

Table 1. Matrix of Coordinates of Each Review

<table><tr><td rowspan="2">Review #</td><td colspan="5">f latent factors mined from LSA</td></tr><tr><td>Factor 1</td><td>Factor 2</td><td>Factor 3</td><td>...</td><td>Factor f</td></tr><tr><td>Review 1</td><td> $x_{11}$ </td><td> $x_{12}$ </td><td> $x_{13}$ </td><td>...</td><td> $x_{1f}$ </td></tr><tr><td>Review 2</td><td> $x_{21}$ </td><td> $x_{22}$ </td><td> $x_{23}$ </td><td>...</td><td> $x_{2f}$ </td></tr><tr><td>Review 3</td><td> $x_{31}$ </td><td> $x_{32}$ </td><td> $x_{33}$ </td><td>...</td><td> $x_{3f}$ </td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Review n</td><td> $x_{n1}$ </td><td> $x_{n2}$ </td><td> $x_{n3}$ </td><td>...</td><td> $x_{nf}$ </td></tr></table>

Referring to previous studies (e.g., Biswas et al., 2020; Siering et al., 2016), when we investigated the verbal cues of online reviews, we examined both content-based cues, like the abovementioned f latent factors showing the f topics of product and service attributes in the vector of $X _ { I }$ , and linguistic cues in the vector of $X _ { 2 } .$ In detail, in Eq. (1), $X _ { 2 }$ is a vector in the form of $\left[ x _ { 2 1 } , x _ { 2 2 } \right]$ . In this study, referring to previous studies, we incorporated two of the most important measurements—the sentiment polarity of the review (denoted as Sentiment; Salehan & Kim, 2016), and the length of the review (denoted as Length; Mudambi & Schuff, 2010) as the linguistic cues to reflect the construct of affect and complexity of online reviews, respectively (Siering et al., 2016). The sentiment polarity was calculated through sentiment analysis using Sentistrength software (Stieglitz & Dang-Xuan, 2013; Thelwall & Buckley, 2013), and the sentiment polarity value is a number ranged from -4 to 4, in which the more positive (or negative) value indicates that customers use the words with more positive (or negative) sentiments, showing their more positive (or negative) emotions. If the sentiment polarity value is 0, it indicates customers have neutral emotions (Salehan & Kim, 2016). The length of the review was measured by the number of words (Mudambi & Schuff, 2010). Further, $X _ { 3 }$ contains the moderator (denoted as MOD), and $X _ { 4 }$ is a vector containing the interaction terms between the moderator and the f factors and two linguistic characteristics. That is, $X _ { 4 }$ is in the form of

$\left[ M O D \times x _ { 1 1 } , M O D \times x _ { 1 2 } , M O D \times x _ { 1 3 } , . . . M O D \times x _ { 1 _ { f } } , M O D \times x _ { 2 1 } , M O D \times x _ { 2 2 } \right]$ . In this study, to test the hypotheses, we investigated three variables as moderators. The first one is the total cost of the order (denoted as Cost), as shown in customers’ online reviews. The second variable is the type of the restaurant, either chain or independent, with chain coded as 1 (denoted as Chain). The third variable is whether the restaurant participates in the Grubhub Plus (GH+) program offered by the platform, with participation coded as 1 (denoted as Program). Restaurants in the GH+ program network offer options for free delivery with a quick checkout, and customers have access to elite customer service and a match in donations for the Grubhub Community Relief Fund. The dependent variable of LSA is customer overall rating (denoted as Overall\_rating), as a measurement of customer overall satisfaction, ranging from 1 to 5. A higher value of overall rating indicates customers’ higher overall satisfaction, and a lower value of overall rating implies customers’ lower overall satisfaction (Chatterjee, 2019). Referring to previous studies (e.g., Biswas et al., 2020; Decker & Trusov, 2010), due to the dispersion of ratings, we used Poisson regression for the text regression. A brief description of the variables and their descriptive statistics is shown in Table 2. The data analytics procedure is visually shown in Figure 2.

Table 2. Variables’ Description and Descriptive Statistics

<table><tr><td>Variables</td><td>Description</td><td>Type</td><td>Mean</td><td>Std</td><td>Min</td><td>Max</td></tr><tr><td>Cost</td><td>The total cost of the order</td><td>Numeric</td><td>20.90</td><td>14.38</td><td>1.35</td><td>112.00</td></tr><tr><td>Overall_Rating</td><td>The overall evaluation by customers showing their overall satisfaction</td><td>Numeric</td><td>3.32</td><td>1.60</td><td>1.00</td><td>5.00</td></tr><tr><td>Review Attributes</td><td>The coordinate values of reviews on the latent factors mined from LSA</td><td>Numeric</td><td>0.02</td><td>0.04</td><td>0.00</td><td>0.30</td></tr><tr><td>Review Length</td><td>The number of words in the online customer review</td><td>Numeric</td><td>27.92</td><td>23.28</td><td>3.00</td><td>127.00</td></tr><tr><td>Sentiment</td><td>The sentiment polarity of online customer reviews; a higher value shows a more positive emotion</td><td>Numeric</td><td>0.44</td><td>1.49</td><td>-4.00</td><td>4.00</td></tr></table>

## Figure 2. Data Analytics Procedure

## Journal Pre-proof

• Overall Rating of Restaurant

• Online Review Comments

• Online Review Date

• Food Ordered Corresponding to Each Review

![](/api/attachments/8EGC2TNM/fulltext/images/9a725ff3e680bbade13a22b1f20e1ceb421d6c41ffb0d53f1d35db26b0bf2ca1.jpg)

• Preprocessing and Term Reduction

• Term Frequency Matrix Transformation

•Latent Textual Factors From Online Reviews

• Coordinate Value of Review Vector Space on Each Latent Textual Factor

Cost of the Entire Order Based on Food Items Ordered

• Sentiment Polarity and Length of Each R. ew

## Text Regressions

• Dependent Variable: Overall Rating of Restaurant (As A Measurement of(ust. Overall Satisfaction)

• Independent Variables:

Čoordinate Values of Each Comment Vector Space on the Latent xtu 1 Factors

Sentiment Polarity and Length of Each Review

Moderator

The Interaction Term Between Coordinate Values of Each  mn ent Vector Space Or Sentiment or Length and the Moderator (Cost, Chain, P. gram)

## 5. RESULTS AND DISCUSSIONS

## 5.1 Textual Factors of Online Customer Reviews

We used LSA to extract textual factors from online customer comments, with the results shown in Table 3. From Table 3, we find that although the reviews are posted on the webpage of each restaurant, customers do not only comment on the product and service attribute performance of the main provider, but also comment on the performance of other participants, including the driver and the platform. We list the subjects of the comments associated with each latent textual factor showing which the customers comment on. For demonstration purposes, we listed the top 10 terms as the high-loading terms for each textual factor. From Table 3, we find that customers comment on each stage of their ordering process, which includes the food, the food-related service, the value, and the after-sales service offered by the restaurants; the delivery performance and drivers’ attitude and behavior; and customer support from the Grubhub platform.

## Table 3. Factors of Customers’ Online Textual Reviews

Journal Pre-proof

<table><tr><td>Interpretations (Labels) of Factors</td><td>High-loading Terms</td><td>Subject of Comments</td></tr><tr><td>Food</td><td>food, item, piece, vegetable, meal, meat, lunch, taste, ingredient, dish</td><td>Restaurant</td></tr><tr><td>Food-related Service</td><td>pack, straw, box, bag, label, arrange, fork, receipt, wrap, container</td><td>Restaurant</td></tr><tr><td>Delivery</td><td>deliveri, minut, hour, deliver_time, receiv, address, route, sent, order_come, fulfill</td><td>Driver</td></tr><tr><td>Driver</td><td>deliver_person, driver, attitude, drop_off, behave, door, pick, rider, contact_driver walk_in</td><td>Driver</td></tr><tr><td>Value</td><td>price, valu, charg, pai, dollar, cost, spend, monei, cost_monei, list_price</td><td>Restaurant</td></tr><tr><td>Restaurant Service</td><td>call_restaurant, order_place, contact_restaurant, request_service, menu_describ, ask_order, place_menu talk_restaurant, restaurant_staff, contact_order</td><td>Restaurant</td></tr><tr><td>Platform Support</td><td>order, grubhub, customer_support, customer_center, grubuhub_staff, credit_card, account, contact_grubhub, app, refund</td><td>Grubhub Platform</td></tr></table>

## 5.2 Text Regressions

After LSA, we used text regressions to analyze the influence of customers’ comments about each attribute on their overall satisfaction with restaurants. We presented the correlation of variables in therefore all below the threshold of 3, which indicates that multicollinearity is not an issue (Biswas et al., 2020; Hair et al., 2010).

Table 4. Correlation Matrix of Variables

<table><tr><td></td><td>Food</td><td>Food_related_service</td><td>Delivery</td><td>Driver</td><td>Value</td><td>Restaurant Service</td><td>Platform Support</td><td>Cost</td><td>Sentiment</td><td>Length</td></tr><tr><td>Food</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Food_related_service</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Delivery</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Driver</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Value</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Restaurant Service</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Platform Support</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Cost</td><td>0.00</td><td>-0.02</td><td>-0.09</td><td>-0.10</td><td>0.05</td><td>0.16</td><td>-0.02</td><td>1.00</td><td></td><td></td></tr><tr><td>Sentiment</td><td>0.19</td><td>0.00</td><td>0.13</td><td>0.02</td><td>0.03</td><td>-0.07</td><td>-0.11</td><td>-0.03</td><td>1.00</td><td></td></tr><tr><td>Length</td><td>-0.18</td><td>0.01</td><td>-0.10</td><td>-0.02</td><td>-0.03</td><td>0.12</td><td>0.10</td><td>0.16</td><td>-0.19</td><td>1.00</td></tr></table>

Next, we presented the results of the basic model (Model 1) containing the seven attributes in Eq.

(2) in column 1 of Table 5. And then, we tested the moderating effect of cost of the order on the influence of the attributes on customer overall rating (Model 2). We presented the models in Eq. (3) and the results in column 2. Following this, we conducted further analysis to find whether time plays a role in the influence of various attributes on customer satisfaction in the on-demand service context. We divided the sample into two subsamples depending on the date the online customer review posted. The first subsample contains the reviews posted on the first three months (from March 15 to June 15, 2020) and the second subsample contains the reviews posted on the later three months (From June 16 to September 15, 2020). We then ran the same model to test the influence of the attributes on customer overall rating and the moderating role of cost of the order as in Model 2 for subsample 1 (Model 3) and subsample 2 (Model 4), respectively. The results are presented in columns 3 and 4, respectively. Then, we presented the results of the model by testing each of the two moderating effects (chain versus independent, participating in the program or not) on the influence of the attributes on customer overall rating, respectively. We presented the results in columns 5 and 6 in Table 5, respectively. When adding customer overall rating does not change in terms of the significance of the coefficients of the various attributes, which shows the robustness of our results.

$$
\begin{array}{c} \text { Overall\_rating} _ {i} = \beta_ {0} + \beta_ {1} \text { Food } _ {i} + \beta_ {2} \text { Food\_related\_service} _ {i} + \beta_ {3} \text { Delivery } _ {i} + \beta_ {4} \text { Driver } _ {i} + \beta_ {5} \text { Value } _ {i} \\ + \beta_ {6} \text { Restaurant\_Service } _ {i} + \beta_ {7} \text { Platform\_support } _ {i} + \varepsilon_ {i}, \end{array}\tag{2}
$$

$$
\begin{array}{l} \text {Overall\_rating} _ {i} = \beta_ {0} + \beta_ {1} \text {Food} _ {i} \cap \beta_ {2} \text {Food\_related\_service} _ {i} + \beta_ {3} \text {Delivery} _ {i} + \beta_ {4} \text {Driver} _ {i} + \beta_ {5} \text {Value} _ {i} \\ \qquad + \beta_ {6} \text {Restaurant\_Service} _ {i} + \beta_ {7} \text {Platform\_support} _ {i} + \beta_ {8} \text {Sentiment} _ {i} + \beta_ {9} \text {Length} _ {i} \\ \qquad + \beta_ {1 0} \text {MOD} _ {i} + \beta_ {1 1} \text {MOD} _ {i} \times \text {Food} _ {i} + \beta_ {1 2} \text {MOD} _ {i} \times \text {Food\_related\_service} _ {i} \\ \qquad + \beta_ {1 3} \text {MOD} _ {i} \times \text {Delivery} _ {i} + \beta_ {1 4} \text {MOD} _ {i} \times \text {Driver} _ {i} + \beta_ {1 5} \text {MOD} _ {i} \times \text {Value} _ {i} \\ \qquad + \beta_ {1 6} \text {MOD} _ {i} \times \text {Restaurant\_Service} _ {i} + \beta_ {1 7} \text {MOD} _ {i} \times \text {Platform\_support} _ {i} \\ \qquad + \beta_ {1 8} \text {MOD} _ {i} \times \text {Sentiment} _ {i} + \beta_ {1 9} \text {MOD} _ {i} \times \text {Length} _ {i} + \varepsilon_ {i}, \end{array}\tag{3}
$$

where i represents online review i, MOD = Cost, Chain, and Program in Models 2, 5, and 6, respectively.

Table 5. Text Regression Results

<table><tr><td rowspan="3">Variables</td><td colspan="6">Dependent Variable: Customer Overall Rating</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td><td>Model 6</td></tr><tr><td>Basic</td><td>MOD</td><td>MOD</td><td>MOD</td><td>MOD</td><td>MOD =</td></tr><tr><td colspan="7">Journal Pre-proof</td></tr><tr><td></td><td>Model</td><td>= Cost</td><td>= Cost(First 3Months)</td><td>= Cost(Later 3Months)</td><td>= Chain</td><td>Program</td></tr><tr><td>Food</td><td>5.15***</td><td>4.02**</td><td>4.05**</td><td>3.98**</td><td>3.81***</td><td>3.26*</td></tr><tr><td>Food_related_service</td><td>-0.66</td><td>0.12</td><td>0.11</td><td>0.14</td><td>-0.43</td><td>-1.79</td></tr><tr><td>Delivery</td><td>1.65**</td><td>3.44*</td><td>3.40*</td><td>3.49*</td><td>1.66*</td><td>3.37***</td></tr><tr><td>Driver</td><td>-5.19***</td><td>-5.72*</td><td>-5.70*</td><td>-5.75*</td><td>-5.98***</td><td>-6.68**</td></tr><tr><td>Value</td><td>0.31</td><td>0.18</td><td>0.19</td><td>0.16</td><td>0.19</td><td>0.89</td></tr><tr><td>Restaurant_service</td><td>-2.22**</td><td>-3.67*</td><td>-3.61*</td><td>-3.71*</td><td>-1.96*</td><td>-9.88*</td></tr><tr><td>Customer_support</td><td>-4.09**</td><td>-7.53**</td><td>-7.51**</td><td>-7.56**</td><td>-3.90*</td><td>-7.38**</td></tr><tr><td>Sentiment</td><td></td><td>0.25***</td><td>0.26***</td><td>0.23***</td><td>0.25***</td><td>0.27***</td></tr><tr><td>Length</td><td></td><td>-0.01*</td><td>-0.01*</td><td>-0.01*</td><td>-0.01*</td><td>-0.01*</td></tr><tr><td>MOD</td><td></td><td>0.01*</td><td>0.01*</td><td>0.01*</td><td>0.24*</td><td>0.26*</td></tr><tr><td>MOD × Food</td><td></td><td>0.17**</td><td>0.18*</td><td>0.15*</td><td>-3.67*</td><td>-0.75</td></tr><tr><td>MOD ×Food_related_service</td><td></td><td>-0.06</td><td>-0.05</td><td>0.07</td><td>-1.12</td><td>1.58</td></tr><tr><td>MOD × Delivery</td><td></td><td>-0.09</td><td>-0.08</td><td>0.11</td><td>0.17</td><td>2.90*</td></tr><tr><td>MOD × Driver</td><td></td><td>-0.17</td><td>-0.16</td><td>-0.19</td><td>5.84*</td><td>5.95*</td></tr><tr><td>MOD × Value</td><td></td><td>0.00</td><td>0.00</td><td>0.00</td><td>-1.71</td><td>-1.24</td></tr><tr><td>MOD ×Restaurant_service</td><td></td><td>-0.20**</td><td>-0.19**</td><td>-0.22**</td><td>2.63</td><td>9.65*</td></tr><tr><td>MOD ×Customer_support</td><td></td><td>0.11</td><td>0.11</td><td>0.12</td><td>-3.23</td><td>6.88*</td></tr><tr><td>MOD × Sentiment</td><td></td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.03</td><td>0.05</td></tr><tr><td>MOD × Length</td><td></td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.01</td><td>0.00</td></tr></table>

Note. \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01.

## 6. DISCUSSION

## 6.1 The Influence of Driver and Platform Performance on Customer Satisfaction With

## Restaurants

From Table 3, we find that when evaluating the main provider, customers also comment on the performance of the auxiliary service providers, drivers, and platforms. Additionally, from Table 5, comprising all five models, we find that customers often describe the poor performance of the drivers and platforms, which negatively affects their overall satisfaction. This supports H1.

From Table 3 and Table 5, we find that customers exhibit review behavior on the on-demand service platform differently from their review behavior on other e-commerce platforms, such as B2B or B2C platforms or third-party booking websites. The key difference is that customers comment on the performance of the main provider, who produces and sells the products or services to the customers, and customers also comment on other parties who are involved in the order fulfillment process. This is a

unique feature within the on-demand service context, in which various parties must coordinate with each other to complete customer orders.

In addition, from Table 5, we find that customers tend to complain about the inappropriate attitude and behavior of drivers. Although drivers do not produce the food nor provide the food-related service, they are the only staff that physically interact with the customers. Thus, their behavior, when dropping off the food and communicating with the customers, affects the customers’ perceptions of the whole consumption experience and, thus, influences their satisfaction with the restaurant. In addition, the results from Table 5 suggest that for all types of restaurants, customers tend to complain about the platform’s customer support. These complaints are about issues with the apps, accounts, payments, and communications from the platform staff. The poor performance of the platform also negatively affects of the auxiliary providers on customer satisfaction with the main provider.

## 6.2 The Moderating Role of Cost

From Table 5, column 2, we find that higher costs increase the role of product and service attributes in affecting customer overall satisfaction with restaurants. This is also confirmed with the results in columns 3 and 4 for the reviews posted during different time. This shows the positive commend the food more often to show their satisfaction with the restaurant. In addition, customers tend to complain more about the poor performance of customer services, such as communication and interactions with restaurant staff, to express their dissatisfaction with the restaurant. However, for the attributes offered by the drivers and platform, cost does not play a moderating role in the reflection of customer comments about them or their overall satisfaction with restaurants.

Food is the core product customers paid for in the on-demand food service context. The higher costs of the order makes customers more sensitive to the food performance. Thus, they tend to comment more on the food in their online reviews to show their satisfaction when the cost is higher. Although customers pay the platform, which also charges a certain proportion of the cost to the restaurants for the orders, most customers still believe their payment is mostly received by the restaurant (Baxter, 2019). In this sense, customers who place higher-priced orders tend to be more direct in revealing their satisfaction or dissatisfaction with restaurants through their positive or negative comments. They tend to attribute their high or low overall satisfaction of the entire consumption experience to the restaurants’ performance. In this way, although customers acknowledge that their order has been completed by several parties, the restaurants are still perceived as the main product and service providers.

## 6.3 The Moderating Role of Chain Restaurants

The results from column 5 in Table 5 suggest that the types of the restaurants (chain versus independent) affect the influence of various attributes, offered by different providers, on customer satisfaction. This demonstrates the moderating effect of restaurant types, which supports H3.

In detail, column 5 in Table 5 shows that chain restaurants, compared with independent restaurants, reduce the positive effect of the high performance of food on customer satisfaction. They also reduce the negative effect of the poor performance of drivers on customer dissatisfaction. This is because chain restaurants usually have standardized operations, and thus customers are more familiar with them. Thus, they tend to comment less on the various attributes and tend not to reveal their satisfaction so directly, as compared with the customers who order from independent restaurants, who tend to comment and evaluate these attributes more to express their satisfaction.

## 6.4 The Moderating Role of Platform Programs

The results from column 6 in Table 5 suggest that involvement with the programs offered by the on-demand service platform affect the influence of various attributes, offered by different providers, on customer satisfaction. This shows the moderating effect of platform programs, and thus supports H4.

In detail, column 4 in Table 5 shows that when customers order food from restaurants that participate in the Grubhub Plus program, compared with those that do not participate in the program, they tend to comment more about the pros of the delivery performance to reveal their satisfaction. This is because one of the important features of the Grubhub plus program is to let customers have free delivery with a quick checkout. In this way, the program facilitates the fulfillment process and enhances the customers’ positive evaluations of the delivery performance, which positively affects their overall satisfaction with the restaurants.

In addition, we find that the Grubhub Plus program reduces the negative influence of the cons of the drivers’ attitude and behavior, restaurant service and the platform’s customer support on customer satisfaction. This may be because program enrollment enhances the image of drivers and standard of operations for restaurants, and makes customers favor their service. In addition, the program shows the professionalism of the platform’s operations and regulations, which facilitates customers’ positive perceptions and enhances their trust in the platform, thus alleviating the negative influence of the deficiency of the platform on customer satisfaction.

In summary, as an overview of the results from Table 5, we can find that although customers also comment on the food-related service and the value of their orders, these two attributes do not have a significant influence on their overall satisfaction with the restaurants. Customers mainly describe the for future customers. In addition, we find that the sentiment polarity of the reviews always has a positive reflection on customer overall satisfaction. This dem s that customers often show their positive (or negative) emotions in their reviews when they are satisfied (or dissatisfied) overall with the restaurant and consumption experience. Fur her, we find the length of review has a negative reflection on customer overall satisfaction. This is because complaining customers tend to use more words to describe in detail the reasons for their dissatisfaction. This can make their reviews more persuasive. Last, we find the time when customers write online reviews does not significantly affect the influence of various attributes on customer overall satisfaction. This shows the consistency of customer online review behavior and satisfaction over time.

## 7. THEORETICAL AND MANAGERIAL IMPLICATIONS

## 7.1 Theoretical Implications

The theoretical foundation of this paper is the integrative service quality-satisfaction theory (De Ruyter et al., 1997), which emphasizes the impact of customers’ perceptions of the entire consumption experience on their satisfaction. This study’s findings contribute to the existing literature in the following three ways.

First, previous studies about online customer reviews (e.g., Mitra & Jenamani, 2020; Moon et al., 2019) have focused mainly on customers’ comments on the traditional B2B or B2C platforms or thirdparty booking platforms and found that the attributes offered by the product or service provider are the only subjects upon which the customers comment. This study focuses on online customer reviews on the on-demand service platforms and analyzes both the customers’ online review-writing behavior and the reflection of the comments on their satisfaction. We found that customers comment on the main provider—the restaurant—and that they also comment on the performances of all other parties that fulfill their order, including the drivers and the platform. Additionally, the parties that provide the auxiliary services affect customers’ overall satisfaction with the main providers. This reveals how the overall perception of the consumption affects customers’ evaluation and satisfaction of the main providers.

Second, previous studies about online customer reviews (e.g., Berezina et al., 2016; Xu, 2020) have not discussed how the total cost of the order affects the influence of various attributes on customer overall satisfaction. The findings of this study suggest that cost only increases the impact of attributes offered by the restaurants on customers’ overall satisfaction. For the attributes offered by other auxiliary parties, the role of cost is insignificant. This shows that most customers still place more significance on the importance of the main providers’ performance despite acknowledging the role of various participants in completing their orders. They attribute the overall performance to the main provider even more when they place an order with a higher total cost.

Third, most of the previous studies (e.g., Bao & Chang, 2014; Zhao et al., 2019) about online customer reviews did not differentiate customers’ review behavior and their reflected satisfaction among different types of providers. This study’s findings suggest that customers display different reviewwriting behavior and show different levels of satisfaction with the restaurants that have different types (chain versus independent) and involvement in the programs offered by the on-demand service platform.

This reflects the moderating effect of the types of providers on the impact of various attributes of customer satisfaction.

## 7.2 Managerial Implications

Online customer reviews yield significant business value in understanding customers’ satisfaction with their consumption experience and with the providers. Additionally, the reviews serve as intangible assets to generate eWOM to affect future customer demand. Thus, the typical advice about utilizing online customer reviews has already been given in previous studies: understand the customers’ satisfaction and valuation of the providers from their online reviews to improve various product and service attributes.

The above general advice also applies to this study. However, in the on-demand service context, the main providers, namely, the restaurants in the on-demand food service context, must pay additional attention to coordination among various stakeholders. When posting their reviews on the webpages of the restaurants on the on-demand service platform to reveal their overall satisfaction with the restaurants, customers also comment on other participants, such as the drivers and the platform who fulfill the order, and the performance of these participants affects the cus omers’ overall satisfaction with the restaurants. provider compels restaurants to improve their own performance and to coordinate with the drivers and the platform to encourage them to improve their service. The coordination is particularly important in the on-demand service context in which the match of supply and demand is key and requires a rapid response from the providers in real time.

In detail, in addition to offering high-quality food, which is the core product in the on-demand food service context, restaurants should make sure the food is prepared and packaged well to ensure that the pickup process happens on time for the drivers and to facilitate the delivery process and maintain the quality of the food (e.g., temperature and no leaking) during delivery. Restaurants should also keep up with the technology of the platform to ensure order fulfillment happens flawlessly to facilitate order information sharing and resolve order issues that customers report through the platform’s customer

support. The restaurants should understand that performance in terms of successful order completion requires a high level of coordination among all participants and that they are in a community with shared interests. The strategies for implementing collective actions to optimize the benefits for participants, and for technologies facilitating the elimination of information asymmetry between participants, help enhance customers’ satisfaction with the whole consumption experience.

In addition, restaurants should pay extra attention to orders with high total costs. These orders need extra care to ensure that they are fulfilled correctly. This is because the findings of this study suggest that customers are more likely to reveal their satisfaction or dissatisfaction in their comments directly when the orders cost more. This should compel restaurants to meet the challenges of these orders and input the optimal amount of labor and material resources to deal with these focal customers.

Moreover, restaurants should understand how their types and their participation in the programs offered by the platforms affect their operational procedures and influence customer satisfaction. Customers may have a different image and expectation of and familiarity with different types of restaurant. Chain restaurants must strictly follow their standardized operations and keep their ectations. Independent restaurants should amplify their unique characteristics as strengths, which is what customers tend to describe and commend more in their reviews to show their satisfaction. In this way, both chain and independent restaurants can utilize the positive eWOM effect, which can serve as a competitive advantage. Restaurants that do not participate in the programs offered by the platform must make enhancements to show the quality and value of their products and services. For restaurants that participate in the platform programs, their satisfaction from customers is more aligned with that of the platform; thus, both the restaurants and the platform should collaborate to enhance the reputation of the program and the restaurants.

In summary, restaurants in the on-demand service context must first improve their own products and service performance, including food, food-related service, after-sales service, and value. Additionally, they must coordinate with the drivers and the platform to achieve mutual improvement. All participants in the on-demand service context should understand that the customers’ satisfaction is interrelated rather than independent. Therefore, they share the same interests and must strive to implement joint optimal actions to improve the entire order production and fulfillment process and enhance the benefits that they offer to customers.

## 8. CONCLUDING REMARKS

## 8.1 Conclusions

With the development of the on-demand platform economy, more customers are using ondemand service platforms to order services. This study uses text-mining approaches to examine customers’ online review-writing behavior and their reflected overall satisfaction with the restaurants in the on-demand food service context. The findings of our study have answered four corresponding research questions.

First, regarding customers’ comments and their satisfaction, we find that customers comment on both the main service provider—the restaurants—and the auxiliary service providers—the drivers and on-demand service platform—in their online custo mer reviews, which are posted on the restaurants webpages on the on-demand service platform. There is a spillover effect from the performance of the the drivers and the platform affects customers’ overall satisfaction with the restaurants.

Second, regarding the role of total cost of the order, we find that it has a positive moderating effect on the impact of the various attributes offered by different providers on customers’ overall satisfaction. In particular, in the on-demand food service context, cost amplifies the impact of the food and customer service offered by the restaurants on customer overall satisfaction.

Third, regarding the role of the type (chain versus independent) of the restaurants in this study, we find that chain restaurants have a negative moderating effect on the impact of attributes of customer satisfaction. Particularly, for customers who order from a chain restaurant, compared with those from independent restaurants, the impact of the performance of the food and the driver on customers’ overall satisfaction is reduced.

Fourth, we found that the moderating effect of the programs offered by the on-demand service platform is significant for various attributes of customer overall satisfaction. Specifically, the delivery performance plays a more important role in customer satisfaction for customers who order the food from the restaurants that participate in the Grubhub Plus program, compared with those restaurants that do not. In addition, we found the platform program alleviates the negative influence of the poor performance of drivers’ attitude and behavior, customer service offered by the restaurants and of customer support offered by the platform on customer overall satisfaction.

Last, we find that the sentiment polarity of the reviews positively reflects overall customer satisfaction. This demonstrates that customers tend to reveal their $\sum \limits _ { i = 1 } ^ { n - \infty } c _ { i + \infty } \frac { 1 } { 2 }$ (or negative) emotions in their reviews when they are satisfied (or dissatisfied) with the restaurant and consumption experience overall. In addition, we find that the length of a review has a negative reflection on overall customer satisfaction. This demonstrates that customers tend to describe and comment on their consumption experience in more detail to complain about the service providers when they are dissatisfied.

This study provides important managerial implications for businesses. Understanding customers’ online review-writing behavior in the on-demand service context is the first step to understanding the customers’ needs and wants. The findings of this study urge collaboration and coordination between various participants and the on-demand service platform to mutually improve. In this way, customers will be highly satisfied with the entire consumption experience and with each of the providers. Thus, the positive eWOM effect can be generated through the on-demand service platform.

## 8.2 Directions for Future Research

This study provides several directions for future research. First, customers may display herd behavior, which happens when customers’ actions are influenced by their peers’ purchases, which provide a signal effect and encourage customers to trust and follow their predecessors (Banerjee, 1992; Cheung et al., 2014; Shen et al., 2016). Therefore, it is possible that prospective users will read online reviews of restaurants and place orders. Thus, future research can examine how this herd behavior affects customers’ online food purchasing decisions and their satisfaction. Second, our empirical

analysis is of U.S. customers and their satisfaction with the food service from the restaurants listed on Grubhub.com. However, according to Hofstede’s cultural framework (Hofstede & Bond, 1984), customers from different countries can have different cultural backgrounds, including elements such as power distance, individualism/collectivism, masculinity/femininity, uncertainty avoidance, and long/short-term orientation. In this way, customers from different cultural backgrounds may have different perceptions as service receivers, and restaurant servers from different cultural backgrounds may have different perceptions as service providers. A comparison of the influence of various product and service attributes on satisfaction among customers with different cultural backgrounds could be an interesting direction for future research. Last, our study examines the determinants of overall customer satisfaction with restaurants and the ways this is influenced by the performance of other providers. perceptions, such as loyalty and the willingness to pay a premium. For example, future studies can explore how customers’ loyalty toward the platform affects their loyalty to the listed restaurants.

## REFERENCES

Alalwan, A. A. (2020). Mobile food ordering apps: An empirical study of the factors affecting customer esatisfaction and continued intention to reuse. International Journal of Information Management, 50, 28- 44.

Bai, J., So, K. C., Tang, C. S., Chen, X., & Wang, H. (2019). Coordinating supply and demand on an on-

Banerjee, A. V. (1992). A simple model of herd behavior. The Quarterly Journal of Economics, 107(3), 797- 817.

Bao, T., & Chang, T. L. S. (2014). Why Amazon uses both the New York Times Best Seller List and customer reviews: An empirical study of multiplier effects on product sales from multiple earned media. Decision Support Systems, 67, 1-8.

Bauer, H. H., Falk, T., & Hammerschmidt, M. (2006). eTransQual: A transaction process-based approach for capturing service quality in online shopping. Journal of Business Research, 59(7), 866-875.

Berezina, K., Bilgihan, A., Cobanoglu, C., & Okumus, F. (2016). Understanding satisfied and dissatisfied hotel customers: text mining of online hotel reviews. Journal of Hospitality Marketing & Management, 25(1), 1-24.

Biswas, B., Sengupta, P., & Chatterjee, D. (2020). Examining the determinants of the count of customer reviews in peer-to-peer home-sharing platforms using clustering and count regression techniques. Decision Support Systems, 135, 113324.

Baxter, A. (2019). Third-party food delivery apps hurt restaurants. Accessed from https://www.breezejmu.org/opinion/opinion-third-party-food-delivery-apps-hurtrestaurants/article\_9c2bb8d8-eae4-11e9-a555-13452c405481.html. Accessed on September 29, 202

Carbó-Valverde, S., Chakravorti, S., & Rodriguez-Fernandez, F. (2009). Regulating two-sided markets: an empirical investigation. Available at SSRN.

Caro, L. M., & García, J. A. M. (2007). Cognitive–affective model of consumer satisfaction. An exploratory study within the framework of a sporting event. Journal of Business Research, 60(2), 108-114.

Chatterjee, S. (2019). Explaining customer ratings and recommendations by combining qualitative and quantitative user generated contents. Decision Support Systems, 119, 14-22.

Cheung, C. M., Xiao, B. S., & Liu, I. L. (2014). Do actions speak louder than voices? The signaling role of social information cues in influencing consumer purchase decisions. Decision Support Systems, 65, 50- 58.

Choi, T. M., Guo, S., Liu, N., & Shi, X. (2020). Optimal pricing in on-demand-service-platform-operations with hired agents and risk-sensitive customers in the blockchain era. European Journal of Operational Research, 284(3), 1031-1042.

Dann, D., Teubner, T., Adam, M. T., & Weinhardt, C. (2020). Where the host is part of the deal: Social and economic value in the platform economy. Electronic Commerce Research and Applications, 40, 100923.

De Ruyter, K., Bloemer, J., & Peeters, P. (1997). Merging service quality and service satisfaction. An empirical test of an integrative model. Journal of Economic Psychology, 18(4), 387-406.

Decker, R., & Trusov, M. (2010). Estimating aggregate consumer preferences from online product reviews. International Journal of Research in Marketing, 27(4), 293-307.

Delgosha, M. S., & Hajiheydari, N. (2020). On-demand service platforms pro/anti adoption cognition: Examining the context-specific reasons. Journal of Business Research, 121, 180-194.

Dijksterhuis, A. (2004). Think different: the merits of unconscious thought in preference development and decision making. Journal of Personality and Social Psychology, 87(5), 586-598.

Evangelopoulos, N., Zhang, X., & Prybutok, V. R. (2012). Latent semantic analysis: five methodological recommendations. European Journal of Information Systems, 21(1), 70-86.

Fiske, S. T., & Taylor, S. E. (1991). Social cognition (2nd ed.). New York: McGraw-Hill.

Forsythe, S. M., & Shi, B. (2003). Consumer patronage and risk perceptions in Internet shopping. Journal of Business Research, 56(11), 867-875.

Grubhub (2019). What is Grubhub? Accessed from https://about.grubhub.com/about-us/what-isgrubhub/default.aspx. Accessed on June 21, 2020.

Hair, J. F., Black, W. C., Babin, B., & Anderson, R. E. (2010). Multivariate data analysis (7th ed.). New Jersey: Pearson.

Harris, K. J., DiPietro, R. B., Murphy, K. S., & Rivera, G. (2014). Critical food safety violations in Florida: Relationship to location and chain vs. non-chain restaurants. International Journal of Hospitality Management, 38, 57-64.

Haselton, M. G., Nettle, D., & Andrews, P. W. (2005). The evolution of cognitive bias. In D. M. Buss (Ed.), The Handbook of Evolutionary Psychology: Hoboken, NJ, US: John Wiley & Sons Inc. pp. 724-746.

Hofstede, G., & Bond, M. H. (1984). Hofstede's culture dimensions: An independent validation using Rokeach's value survey. Journal of Cross-cultural Psychology, 15(4), 417-433.

Homburg, C., Hoyer, W. D., & Koschate, N. (2005). Customers’ reactions to price increases: do customer satisfaction and perceived motive fairness matter?. Journal of the Academy of Marketing Science, 33(1), 36-49.

Hopcroft, J., & Kannan, R. (2012). Chapter 4 Singular value decomposition in the book of Computer Science Theory for the Information Age. Accessed from https://www.cs.cmu.edu/\~venkatg/teaching/CStheoryinfoage/hopcroft-kannan-feb2012.pdf. Accessed on May 1, 2020.

Huang, A. H., Lehavy, R., Zang, A. Y., & Zheng, R. (2018). Analyst information discovery and interpretation roles: A topic modeling approach. Management Science, 64(6), 2833-2855.

Husbands, P., Simon, H., & Ding, C.H.Q. (2001). On the use of the singular value decomposition for text retrieval. Computational Information Retrieval, 5, 145-156.

Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. Cognitive Psychology, 3(3), 430-454.

Kim, Y., Chang, Y., Wong, S. F., & Park, M. C. (2014). Customer attribution of service failure and its impact in social commerce environment. International Journal of Electronic Customer Relationship Management, 8(1-3), 136-158.

Ko, D. G., Mai, F., Shan, Z., & Zhang, D. (2019). Operational efficiency and patient‐centered health care: A view from online physician reviews. Journal of Operations Management, 65(4), 353-379.

Kulkarni, S. S., Apte, Uday M., & Evangelopoulos, N. E. (2014). The use of Latent Semantic Analysis in operations management research. Decision Sciences, 45(5), 971-994.

Lee, S. M., Lee, D., & Kang, C. Y. (2012). The impact of high-performance work systems in the health-care industry: employee reactions, service quality, customer satisfaction, and customer loyalty. The Service Industries Journal, 32(1), 17-36.

Mandabach, K. H., Ellsworth, A., Vanleeuwen, D. M., Blanch, G., & Waters, H. L. (2005). Restaurant managers' knowledge of food allergies: A comparison of differences by chain or independent affiliation, type of service and size. Journal of Culinary Science & Technology, 4(2-3), 63-77.

Mavlanova, T., Benbunan-Fich, R., & Koufaris, M. (2012). Signaling theory and information asymmetry in online commerce. Information & Management, 49(5), 240-247.

Mitra, S., & Jenamani, M. (2020). OBIM: A computational model to estimate brand image from online consumer review. Journal of Business Research, 114, 213-226.

Moon, S., Kim, M. Y., & Bergey, P. K. (2019). Estimating deception in consumer reviews based on extreme terms: Comparison analysis of open vs. closed hotel reservation platforms. Journal of Business Research, 102, 83-96.

Mudambi, S. M., & Schuff, D. (2010). Research note: What makes a helpful online review? A study of customer reviews on Amazon. com. MIS Quarterly, 34(1), 185-200.

Nam, K., Baker, J., Ahmad, N., & Goo, J. (2020). Determinants of writing positive and negative electronic word-of-mouth: Empirical evidence for two types of expectation confirmation. Decision Support Systems, 129, 113168.

Ngo-Ye, T. L., & Sinha, A. P. (2014). The influence of reviewer engagement characteristics on online review helpfulness: A text regression model. Decision Support Systems, 61, 47-58.

Parasuraman, A., Berry, L. L., & Zeithaml, V. A. (1991). Refinement and reassessment of the SERVQUAL scale. Journal of Retailing, 67(4), 420-450.

Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1988). Servqual: A multiple-item scale for measuring consumer perceptions of service quality. Journal of Retailing, 64(1), 12-40.

Park, J. Y., Back, R. M., Bufquin, D., & Shapoval, V. (2019). Servicescape, positive affect, satisfaction and behavioral intentions: The moderating role of familiarity. International Journal of Hospitality Management, 78, 102-111.

Roma, P., Zambuto, F., & Perrone, G. (201 apps. Decision Support Systems, 91, 1

Saab, A. B., & Botelho, D. (2020). Are organizational buyers rational? Using price heuristics in functional risk judgment. Industrial Marketing Management, 85, 141-151.

Salehan, M., & Kim, D. J. (2016). Predicting the performance of online consumer reviews: A sentiment mining approach to big data analytics. Decision Support Systems, 81, 30-40.

Sezgen, E., Mason, K. J., & Mayer, R. (2019). Voice of airline passenger: A text mining approach to understand customer satisfaction. Journal of Air Transport Management, 77, 65-74.

Shen, X. L., Zhang, K. Z., & Zhao, S. J. (2016). Herd behavior in consumers’ adoption of online reviews. Journal of the Association for Information Science and Technology, 67(11), 2754-2765.

Sidorova, A., Evangelopoulos, N., Valacich, J.S., & Ramakrishnan, T. (2008). Uncovering the intellectual core of the information systems discipline. MIS Quarterly, 32(3), 467-482.

Siering, M., Koch, J. A., & Deokar, A. V. (2016). Detecting fraudulent behavior on crowdfunding platforms: The role of linguistic and content-based cues in static and dynamic contexts. Journal of Management Information Systems, 33(2), 421-455.

Stangl, B., Kastner, M., & Prayag, G. (2017). Pay-what-you-want for high-value priced services: Differences between potential, new, and repeat customers. Journal of Business Research, 74, 168-174.

Stieglitz, S., & Dang-Xuan, L. (2013). Emotions and information diffusion in social media—sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29(4), 217-248.

Taylor, T. A. (2018). On-demand service platforms. Manufacturing & Service Operations Management, 20(4), 704-720.

Technavio (2020). Analysis on Impact of Covid-19- Online On-Demand Food Delivery Services Market 2019-2023. Accessed from https://www.businesswire.com/news/home/20200430005160/en/Analysis-Impact-Covid-19--Online-On-Demand-Food-Delivery. Accessed from June 21, 2020.

Thelwall, M., & Buckley, K. (2013). Topic‐based sentiment analysis for the social web: The role of mood and issue‐related words. Journal of the American Society for Information Science and Technology, 64(8), 1608-1617.

Tong, T., Dai, H., Xiao, Q., & Yan, N. (2020). Will dynamic pricing outperform? Theoretical analysis and empirical evidence from O2O on-demand food service market. International Journal of Production Economics, 219, 375-385.

U.S. Census Bureau (2019). City and Town Population Totals: 2010-2019. Accessed from https://www.census.gov/data/tables/time-series/demo/popest/2010s-total-cities-and-towns.html. Accessed on June 21, 2020.

van der Burg, R. J., Ahaus, K., Wortmann, H., & Huitema, G. B. (2019). Investigating the on-demand service characteristics: an empirical study. Journal of Service Management, 30(6), 739-765.

Xiang, Z., Schwartz, Z., Gerdes Jr, J. H., & Uysal, M. (2015). What can big data and text analytics tell us about hotel guest experience and satisfaction?. International Journal of Hospitality Management, 44, 120-130.

Xu, X. (2019). Examining the relevance of online customer textual reviews on hotels’ product and service attributes. Journal of Hospitality & Tourism Research, 43(1), 141-163.

Xu, X. (2020). Examining an asymmetric effect between online customer reviews emphasis and overall satisfaction determinants. Journal of Business Research, 106, 196-210.

Zhang, Z., Ye, Q., Law, R., & Li, Y. (2010). The impact of e-word-of-mouth on the online popularity of restaurants: A comparison of consumer reviews and editor reviews. International Journal of Hospitality Management, 29(4), 694-700.

Zhao, M., & Dholakia, R. R. (2009). A multi‐attribute model of web site interactivity and customer satisfaction. Managing Service Quality: An International Journal, 19(3), 286-307.

Zhao, Y., Xu, X., & Wang, M. (2019). Predicting overall customer satisfaction: Big data evidence from hotel online textual reviews. International Journal of Hospitality Management, 76, 111-121.

Systems, 107, 116-124.

Zhuang, H., Leszczyc, P. T. P., & Lin, Y. (2018). Why is price dispersion higher online than offline? The impact of retailer type and shopping risk on price dispersion. Journal of Retailing, 94(2), 136-153.

## Author Credit Statement

Xun Xu is the solo author of this paper, and thus contributes the entire task to the study.

## Biographical Note

Xun Xu holds a PhD in Operations Management from the Washington State University. He is currently an Associate Professor in the Department of Management, Operations, and Marketing in College of Business Administration at the California State University, Stanislaus in the United States. He teaches operations management and management science related courses. His research interests include service operations management, supply chain management and coordination, sustainability, e-commerce, data and text mining, and interface of hospitality and operations management. He has published over 40 papers on such journals as Annals of Tourism Research, Computers and Industrial Engineering, Decision Support Systems, European Journal of Operational Research, Journal of Business Research, Journal of the Operational Research Society, Journal of Travel Research, International Journal of Hospitality Management, International Journal of Contemporary Hospitality Management, International Journal of Information

Management, International Journal of Production Economics, International Journal of Production Research, along with others.

## Highlights

 We use text-mining methods to analyze reviews within the on-demand service context.

 Customers comment on both the main and auxiliary providers in their online reviews.

 Auxiliary providers’ performance affects customers’ satisfaction with main providers.

 Cost affects customer review behavior and the reflected satisfaction from reviews.

 Different categories of restaurants affect the influence of attributes on overall satisfaction.
