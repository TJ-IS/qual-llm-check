---
otero_id: 9406
otero_key: "NPU8SAEG"
title: "Disentangling consumer recommendations: Explaining and predicting airline recommendations based on online reviews"
authors: "Michael Siering; Amit V. Deokar; Christian Janze"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.01.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30002-2</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2018.01.002</td></tr><tr><td>Reference:</td><td>DECSUP 12917</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>12 June 2017</td></tr><tr><td>Revised date:</td><td>7 November 2017</td></tr><tr><td>Accepted date:</td><td>6 January 2018</td></tr></table>

## Accepted Manuscript

Disentangling consumer recommendations: Explaining and predicting airline recommendations based on online reviews

Michael Siering, Amit V. Deokar, Christian Janze

![](/api/attachments/NPU8SAEG/fulltext/images/bcb3d6db19e3b36bd79bf6357b1f51015e9b5d4f95a7e44b7b95fb2caa254b34.jpg)

Please cite this article as: Michael Siering, Amit V. Deokar, Christian Janze , Disentangling consumer recommendations: Explaining and predicting airline recommendations based on online reviews. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), https://doi.org/10.1016 j.dss.2018.01.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Disentangling Consumer Recommendations: Explaining and Predicting Airline Recommendations based on Online Reviews

Michael Siering

Goethe University Frankfurt

Amit V. Deokar

Theodor-W.-Adorno-Platz 4

(Corresponding Author)

University of Massachusetts Lowell

60323 Frankfurt, Germany

Robert J. Manning School of Business

siering@wiwi.uni-frankfurt.de

One University Avenue

Lowell, MA 01854

amit\_deokar@uml.edu

Christian Janze

Goethe University Frankfurt

Theodor-W.-Adorno-Platz 4

60323 Frankfurt, Germany

janze@wiwi.uni-frankfurt.de

Michael Siering is a postdoctoral research associate at Goethe University Frankfurt and a research associate at the E-Finance Lab, an industry-academic partnership between Goethe University Frankfurt and several industry partners. He has been a visiting scholar at Penn State University. His research focuses on decision support systems in electronic markets, with a focus on the analysis of user generated content by means of sentiment analysis and text mining. His work has been published in the Journal of Management Information Systems, Journal of Information Technology, Decision Support Systems and conference proceedings such as ICIS, ECIS and HICSS. He holds a M.Sc. and a Ph.D. in business administration from Goethe University Frankfurt.

Amit V. Deokar is an Assistant Professor of Management Information Systems in the Robert J. Manning School of Business at the University of Massachusetts Lowell. Dr. Deokar received his PhD in Management Information Systems from the University of Arizona. He also earned a MS in Industrial Engineering from the University of Arizona and a BE in Mechanical Engineering from VJTI, University of Mumbai. His research interests include data analytics, enterprise data management, business intelligence, business process management, and collaboration processes. His work has been published in journals such as Journal of Management Information Systems, Decision Support Systems (DSS), The DATA BASE for Advances in Information Systems, Information Systems Frontiers, Business Process Management Journal (BPMJ) and IEEE Transactions. He is currently a member of the editorial board of DSS and BPMJ journals. He has been serving as the Decision Support and Analytics Track Chair at the international AMCIS 2014-17 conferences, and is currently the Chair of the AIS Special Interest Group on Decision Support and Analytics (SIGDSA). He was recognized with the 2014 IBM Faculty Award for his research and teaching in the areas of analytics and big data.

Christian Janze is a doctoral candidate at Goethe University Frankfurt and a research assistant at the E-Finance Lab, an industry-academic partnership between Goethe University Frankfurt and several industry partners. In addition, he is part of the doctoral program of DZ BANK.

He holds a Master’s degree in Management from Goethe University Frankfurt and was a scholar of the German National Academic Foundation. His research focuses on user generated content, online reviews and market efficiency and has appeared in ICIS Proceedings.

# Disentangling Consumer Recommendations: Explaining and Predicting Airline Recommendations based on Online Reviews

## Abstract

Consumer recommendations of products and services are important performance indicators for organizations to gain feedback on their offerings. Furthermore, they are important for prospective customers to learn from prior consumer experiences. In this study, we focus on user-generated content, in particular online reviews, to investigate which service aspects are evaluated by consumers and how these factors explain a consumer’s recommendation. Further, we investigate how recommendations can be predicted automatically based on such user-driven responses. We disentangle the recommendation decision by performing explanatory and predictive analyses focusing on a sample of airline reviews. We identify core and augmented service aspects expressed in the online review. We then show that service aspect-specific sentiment indicators drive the decision to recommend an airline and that these factors can be incorporated in a predictive model using data mining techniques. We also find that the business model of an airline being reviewed, whether low cost or full service, is also an applicable consideration. Our results are highly relevant for practitioners to analyze and act on consumer feedback in a prompt manner, along with the ability of gaining a deeper understanding of the service from multiple aspects. Also, potential travelers can benefit from this approach by getting an aggregated view on service quality.

Keywords: Consumer Recommendation, Promoter Score, Online Review, Sentiment Analysis, Data Mining.

# ACCEPTED MANUSCRIPT

## 1. Introduction

Sensing and understanding consumer perceptions is important for corporations to deal with positive and negative consumer feedback as well as to engage prospective consumers with their product or service offerings. Previous research indicates that performance metrics in form of promoter scores are invaluable to corporations to estimate consumer satisfaction (Reichheld, 2003). For determining such metrics, corporations take into account whether consumers recommend a specific service or not in order to learn whether consumers are satisfied.

Nowadays, consumers increasingly rely on electronic word-of-mouth as a mechanism to share their experiences of their own volition and express their satisfaction in experiencing a product or service (Sparks, Perkins, & Buckley, 2013; Ye, Law, Gu, & Chen, 2011). Online reviews usually appear as freeform text and often embed a multitude of experiences and opinions regarding different aspects of the reviewed service. However, not all reviewers directly express by means of a standardized field whether they recommend the evaluated service which makes it hard for corporations to calculate promoter scores.

The availability of rich information buried in the reviews’ texts provides an opportunity to enhance the decision-making capabilities of stakeholders in this context, i.e., prospective consumers as well as service providers. First, examining whether the textual contents of each review can uncover reviewers’ assessment of recommending the service or not, which can be informative itself. Second, the ability to disentangle the recommendation decision to examine how specific service aspects are being evaluated by prior consumers and how they drive the overall recommendation decision can further inform the stakeholders. A decision support approach analyzing distinct service aspects and inferring recommendations expressed in online reviews is thus needed to address these relevant issues.

The vital role of online reviews as a key data source in tourism has also been shown in recent studies which focus on the use of online reviews and their role in influencing consumer behavior and decision-making (Rhee & Yang, 2015; Sotiriadis & van Zyl, 2013). Furthermore, especially the helpfulness of online reviews has been analyzed (Korfiatis, García-Bariocanal, & Sánchez-Alonso, 2012; Kuan, Hui, Prasarnphanich, & Lai, 2015; Mudambi & Schuff, 2010; Siering & Muntermann, 2013b). Nevertheless, despite these valuable and interesting

# ACCEPTED MANUSCRIPT

aspects of online reviews, the recommendation decision and its influencing factors, as key aspects of online reviews, have not been addressed so far.

This study focuses on analyzing and inferring recommendations expressed by reviewers in online reviews in tourism services, particularly airline services, from multiple perspectives. First, we examine which service aspects are expressed in the textual contents of airline reviews, where we specifically delve into analyzing the role of core and augmented service aspects (Ozment & Morash, 1994; Ravald & Grönroos, 1996). We also investigate whether reviewers’ recommendations of a service can be explained through service aspects extracted from online reviews. Drawing on theoretical foundations of accessibility-diagnosticity model and multiple pathway anchoring and adjustment model, we posit that services such as airline services are perceived and assessed based on different aspects of the service, and that only a few prominent service aspects play a key role in collectively forming an overall assessment about the service based on which the recommendation decision is reached. This explanatory analysis is particularly useful to service providers in understanding which service aspects are influencing consumer word-of-mouth promotion through online reviews. Second, the study builds on the results from the previous analysis to examine whether reviewers’ recommendations of a service can be predicted using contents expressed in online reviews. In building the predictive models, overall content-based sentiments as well as service aspect-specific sentiments are investigated and compared to a classic text mining approach based on a bag-of-words model. The analysis is relevant for both prospective consumers as well as service providers from a decision support standpoint. Consumers can make informed decisions using the predicted recommendation scores, while service providers can obtain performance indicators to be integrated in managerial dashboards for service management. Third, the study also analyzes the role of service business models in the explanation and prediction of service recommendations from online reviews. Given that different service providers have distinct business models such as low-cost carriers versus full-service network carriers in the airline industry, it may be expected that travelers have different expectations about the service, which will likely inform their review and eventual recommendation. The analysis sheds light on these differences in service models.

The remainder of this paper is structured as follows. Section 2 provides an overview on the background of this study, taking into account the recommendation decision as well as the role of online reviews. In this context, the theoretical models underlying our rationale are presented as well. Next, section 3 focuses on the research methodology applied, including the explanatory and predictive analyses performed. Section 4 presents the results of our analyses. Section 5 discusses issues related to our findings, and section 6 concludes the article.

## 2. Background and Research Questions

## 2.1 Consumer Recommendations

For corporations, customer feedback is essential, not only for driving business performance and growth, but also for product and service innovation as well as for improving customer experience. Managers traditionally rely on customer feedback metrics including average customer satisfaction, top- ox customer satisfaction, proportion of customers complaining, repurchase likelihood of customers as well as word-of-mouth communication such as number of recommendations or promoters (Morgan & Rego, 2006).

In the field of consumer recommendations, Reichheld (2003) proposed the notion of word-of-mouth product or service recommendations, aggregated as the Net Promoter Score (NPS), to be the single most reliable metric NPS is computed simply as the difference in percentage between promoters and detractors. This proposition has received much scrutiny by academics and practitioners alike over the past decade. Previous research has found that a growth in NPS is correlated with a growth in business (Marsden, Samson, & Upton, 2005). In support of Reichheld’s arguments, it was also found that promoter scores are one of the best customer feedback metrics in predicting customer retention (Haan, Verhoef, & Wiesel, 2015). In industry, promoter scores have been leveraged to gain insight into the customer base and in turn to drive market share growth (Khan, 2011). Thus, programs based on promoter scores are particularly effective in underscoring the overall strategy of listening to customers, and substantiating changes transparently by attributing them to relevant testimonies (Khan, 2011).

Given the importance of customer engagement, loyalty, and feedback, as reflected in promoter scores, it is also imperative to understand the factors that influence positive word-of-mouth, i.e. service or product

## ACCEPTED MANUSCRIPT

recommendation. As consumers nowadays express their experiences within online reviews, it is essential for corporations to monitor this form of electronic word-of-mouth in order to understand consumers and to identify the aspects influencing the recommendation decision. Nevertheless, many businesses struggle to utilize online reviews to create business value (He, Liu, & Xiong, 2016). This is because most reviews are not directly tied to a service or product recommendation score, i.e., the issue of whether a customer recommends the service to another potential customer. Thus, a research gap exists in the area of automatically extracting information from online reviews to accurately derive indirect recommendation intentions, disentangling the recommendation decision into different service aspects expressed, and to ultimately incorporate them within a promoter score.

Notably, promoter scores based on consumer recommendations differ from typical online recommendations considering the major variable of interest: Whereas the rich research stream on online recommendations focuses on the question of how a specific product or service can be selected from a set of products or services and be recommended to a consumer, the research stream on consumer recommendations investigates whether consumers recommend a specific product or service of interest. Whereas numerous studies in the field of product recommendation agents providing online recommendations do exist (De Bruyn, Liechty, Huizingh, & Lilien, 2008; Wang & Benbasat, 2008; Xiao & Benbasat, 2007), there is a research gap in the field of extracting consumer recommendations from online reviews.

## 2.2 Online Reviews

Consumers increasingly rely on online reviews as an important information source to base their purchase decisions on (Jang, Prasad, & Ratchford, 2012). In this context, previous research indicates that online reviews can be seen as information cues during the different phases of the purchase decision making process (Dorner, Ivanova, & Scholz, 2013) and that online reviews consequently influence the demand for the services reviewed (Chevalier & Mayzlin, 2006). Furthermore, online reviews are of high value for online retailers as they attract consumers who then, in a next step, might also potentially purchase the reviewed service (Mudambi & Schuff, 2010).

There are different research streams focusing on this type of electronic word of mouth. Extant literature indicates a variety of studies relating online reviews to sales figures, whereas these studies report a significant

# ACCEPTED MANUSCRIPT

influence of online reviews on the corresponding demand related to a specific service (Forman, Ghose, & Wiesenfeld, 2008; Ghose & Ipeirotis, 2011). Another stream of research focuses on the question of what makes online reviews helpful and credible. In this context, different characteristics like a review’s depth or specific review contents (Ngo-Ye & Sinha, 2014; Schindler & Bickart, 2012; Yin, Bond, & Zhang, 2014), the presentation of the reviews in terms of their order (Huang, Tan, Ke, & Wei, 2014) or community membership (Luo, Luo, Xu, Warkentin, & Sia, 2015) have been shown to be relevant. From a practical standpoint, product strategies (Qi, Zhang, Jeon, & Zhou, 2016). Yet another research stream foc s on the reviewers contributing online reviews and mainly investigates the factors that motivate reviewers to contribute content on social commerce platforms (Hennig-Thurau, Gwinner, Walsh, & Gremler, 2004; Siering & Muntermann, 2013a).

Studies specifically focusing on tourism show that travelers make use of user-generated content such as suggest that a total of 20-45% of travelers use user-generate d reviews to inform and/or guide their decision share their experiences ex-post (Chung, Han, & Koo, 2015; Tilly, Fischbach, & Schoder, 2015). Furthermore, Xiang, Schwartz, Gerdes, and Uysal (2015) have studied the nature of hotel guest experiences expressed in customer reviews and examine the role of salient aspects of hotel guest experience in explaining guest satisfaction. The study, however, does not study the sentiment of the service aspects and their role as predictors of consumer recommendation. In the same domain, Rhee and Yang (2015) examine the varied importance of hotel service aspects in different hotel segments. While these studies provide valuable insights regarding the role of online reviews in the field of consumer purchase decision making, an important aspect of the consumer recommendation of services in relation to online reviews has not received much attention: An examination of drivers of a recommendation decision and the automatic extraction of the overall recommendation decision from unstructured user-generated online reviews can be valuable to various stakeholders in the tourism industry.

# ACCEPTED MANUSCRIPT

## 2.3 Text Analytics of User Generated Content

Text analytics or text mining techniques allow for the analysis of unstructured text documents, such as online reviews, to extract meaningful information pieces and derive structured variables for subsequent analyses. Text analytics includes several focus areas such as search and information retrieval, document classification, document clustering, web mining, information extraction, natural language processing, and concept extraction (Miner, 2012). This study focuses on a text mining approach, referred to as ‘text data mining’ by Hotho, Nürnberger, and Paaß (2005) that entails using information extraction and text pre-processing steps in order to extract data from text, and subsequently applying data mining algorithms on the extracted data.

Bag-of-words is a standard technique used in text data mining applications (e.g., Groth, Siering, & Gomber, 2014) that relies on the frequency of occurrence of words in a collection of documents (e.g., online reviews) to derive structured data from the text. In this technique, the specific words in the review text are used as features to represent the review and their weight is most commonly determined by constructing term frequency – inverse matrix is then used for applying data mining techniques like classification.

With the widespread adoption of social media, sentiment analysis or opinion mining, has emerged as a novel area within text analytics (Feldman & Sanger, 2007). Sentiment analysis of user-generated content, such as online reviews, may be conducted at document-level (coarse) or sentence-level (granular) when the entire review a specific entity, e.g., airline service experience. Another form of sentiment analysis called aspect-based sentiment analysis is appropriate when several different aspects of a service are discussed within a given review and the goal is to tease out the opinions regarding each service aspect (Feldman & Sanger, 2007). A review of the related literature suggests that studies utilizing aspect-based sentiment analysis techniques are limited to a few instances within the e-commerce domain concerning the extraction and examination of product features (Hu & Liu, 2004; Popescu & Etzioni, 2007). However, to the best of our knowledge, this study is a first such application in the context of tourism services, particularly airline services, with the objective of explaining and predicting consumer recommendations from unstructured usergenerated online reviews.

## 2.4 Research Questions

We describe theoretical underpinnings that drive our approach in creating explanatory and predictive models for consumer recommendation scores of products or services. Extant research in online ratings has focused on how consumers perceive online ratings and use them in decision-making in using products or services (Jeong & Koo, 2015; Kwark, Chen, & Raghunathan, 2014). In a distinct yet analogous manner, we posit that reviewers themselves are also involved in a decision-making process, one that is aimed at assimilating their own experiences with the service at hand in the form of a review, analyzing the service with the view of whether it is worth recommending to someone else.

The accessibility-diagnosticity (AD) model (Feldman & Lynch, 1988; Lynch Jr, John G, Marmorstein, & Weigold, 1988) explains how people form attitudes that guide behavior (or proximate determinants of behavior such as judgments in their decision-making process) based on relative accessibility and diagnosticity characteristics of inputs. In the case of online reviews, the service experience generates sentiments that serve as a set of inputs that are based on different aspects of that service. For instance, in evaluating a restaurant, reviewers may rely on their experience with various aspects of the service such as ambience, freshness of food, and so airlines, customers may rely on service-specific aspects such as seat comfort, inflight entertainment, and so forth. Drawing on the AD model, reviewers’ judgment of a service (in terms of their recommendation) is likely to be influenced by their sentiments formed in relation to individual service-specific aspects that are relatively accessible to them, and therefore, come to their mind readily at the time of recommendation formation. Further, customers’ sentiments about specific aspects of the service that are perceived to be relevant or diagnostic are likely to influence their recommendations (Lynch Jr, John G et al., 1988).

The Multiple Pathway Anchoring and Adjustment (MPAA) model (Cohen & Reed, 2006) allows to explain the process of the recommendation formation further in terms of how sentiments regarding specific aspects of a service are formed. The MPAA model underscores the idea of multiple pathways to sentiment or attitude formation, including outside-in (object-centered) and inside-out (person-centered) pathways. In the case of online reviews for a service, on one hand, the experience with a certain aspect of a service provides the objectcentered pathway to sentiment generation regarding that service aspect. On the other hand, personal factors that customers experience due to the specific context, situation or personal disposition provide the person-centered pathway to their sentiment generation. Lynch (2006) elaborates on the complementary nature of the AD and the MPAA models. The MPAA model delves in the attitude formation process, whereas the AD model is silent on how customers may form sentiment regarding a certain service aspect. In a manner similar to the diagnosticity mechanism in the AD model, the MPAA model suggests representational sufficiency as a mechanism of how erall judgement distinctively positive or negative than others are said to be diagnostic in forming the overall service recommendation.

We argue that most services such as hotel stays or flights can be dissected in terms of service aspects that together make up the service experience. For example, a hotel service may be characterized with aspects such as & Yang, 2015). The AD and MPAA theoretical models together suggest that online reviews implicitly capture the sentiment expressed by the consumers along service aspects which are accessible and diagnostic. Thus, an online review of a service can be said to express a reviewer’s synthesized mental model of one or more service aspects that were perceived as salient during the service experience. Further, based on the MPAA model, each of the service aspects is a possible pathway to express his sentiment or opinion about the service. As such, considering multiple aspectoriented sentiments and assessments is important to explaining the overall recommendation of the service. The online review, as a holistic unit, may express a certain sentiment, which may be segmented into sentiments regarding specific service aspects.

Thus, we posit that the recommendation about the overall service collectively expresses sentiments of individual service aspects. In our study, we first focus on gaining an understanding about which service aspects are expressed. Toward that end, we differentiate between core and augmented service aspects. In this context, core service aspects represent all aspects related to the basic service and the basic customer benefit received, whereas augmented service aspects encompass all aspects which are facilitating or ancillary to the core service, i.e. aspects where the company can differentiate itself from others and that consequently “surround” the service (Ozment & Morash, 1994; Ravald & Grönroos, 1996). Further, we investigate whether they can explain reviewers’ choice to recommend the service to other consumers or not. Drawing on the theories discussed, we investigate:

Research Question 1a (RQ1a): Which core and augmented service aspects are expressed in online reviews? Research Question 1b (RQ1b): Are sentiments about service aspects extracted from online reviews valuable in service aspects?

Building on the knowledge derived about the aspects that contribute to service recommendations, we are interested in investigating the predictive nature of these service aspects. From a practical standpoint, potential consumers can be presented with predicted recommendation scores along with the reviews to assist in their decision-making process. Also, it is highly relevant for service providers and intermediaries to potentially leverage textual contents of online reviews to derive corporate performance indicators, ultimately to be incorporated in performance dashboards for managerial decision-making. In regard to predicting customer recommendations, we are also interested in learning about the predictive ability of the sentiment expressed regarding different aspects of the service, also compared to review text in a generic sense based on the content itself (i.e., represented by the classical text mining approach based on the bag-of-words model). Thus, the next research question inquires about the predictive power of the textual contents of a review in predicting a service recommendation, particularly in the absence of explicit recommendation information.

Research Question 2 (RQ2): Is sentiment expressed about service aspects valuable in order to predict reviewers’ recommendations of a service, and what is the predictive power compared to a classical text mining approach?

Finally, we are also interested in finding whether the results vary based on the type of business model adopted, such as low cost model and full service model. Over the past two decades, low cost carriers (LCCs) and full service network carriers (FSNCs) have been noted as distinct business models within the airline service industry (Boeing, 2016; Gillen & Lall, 2004). On one hand, LCCs are broadly characterized as airlines having low operating costs and offering “no frills” service experience with a lower baseline ticket cost, but adding substantive charges for features like bags, seat selection, in-flight entertainment, and other amenities. On the other hand, FSNCs are characterized as mega-brand airlines with global networks and offering amenities such as club lounges, first class cabins, and more. Travelers are likely to have different expectations from a service experience with a LCC compared to a FSNC (O’Connell & Williams, 2005). Accordingly, travelers’ may be expected to express sentiments more about different service aspects in these two categories based on both how salient a service aspect was in their service experience and its alignment with initial expectations, which might therefore also influence the recommendation. Thus, we investigate:

Research Question 3 (RQ3): Does the type of the service (e.g., full service versus low-cost service) impact the explanation and prediction of service recommendations?

Using data from an online review platform for airlines, we address these research questions by systematically analyzing the relationship between textual contents of online reviews and consumer recommendations, and demonstrating that the approach can be applied to infer consumer recommendations from online reviews.

## 3. Research Methodology

## 3.1 Research Process

To investigate the three research questions, focused on examining which service aspects are expressed in online reviews and whether a reviewer’s recommendation can be explained by sentiment on core and augmented service aspects expressed in the review (i.e., RQ1a/b), whether the review’s contents have predictive power to infer the recommendation (i.e., RQ2), and whether the type of business model impacts the explanation and prediction of service recommendations (i.e., RQ3), we adapt the structured knowledge discovery process proposed by Han and Kamber (2006).

At the beginning, we select and transform an appropriate dataset and identify and extract the specific service aspects (RQ1a). Following this, we perform an explanatory analysis to understand the significance of the sentiment expressed related to the service aspects discussed (RQ1b). This is also used to determine the variables to be used as predictors in the subsequent predictive analysis that investigates RQ2. In predictive modeling of the data, we evaluate the applicability of different machine learning algorithms to infer the consumer recommendation of the service. We evaluate the different predictive models using a stratified 10-fold crossvalidation approach to draw conclusions about the applicability of the proposed aspect-oriented sentiment variables as well as a classic text mining approach. Last, but not least, we conduct the explanatory and predictive analyses for distinct service types, addressing RQ3. Figure 1 provides an overview of our research process. The specific analyses have been performed with Stata and RapidMiner.

![](/api/attachments/NPU8SAEG/fulltext/images/54f8523115d2ddec749c782f87c99fe060de97d02008867f84875c74f6c8b50f.jpg)  
Figure 1. Research Process Followed

## 3.2 Data Acquisition

In this study, we rely on random sampling of airline reviews that are published on the airline evaluation platform airlinequality.com. This platform represents a comprehensive information source where travelers can evaluate and research the quality of different airlines and their services offered. The platform offers the ability for a traveler to post detailed textual review regarding a flight experience with an airline. Furthermore, users can publish their evaluation of the airline, information regarding the flight purchased (e.g. the date as well as the route taken) as well as evaluations of different aspects of the flight experience (e.g., seat comfort, food service, etc.). In addition, the platform provides an option for the travelers to explicitly respond to the question of whether they would recommend the airline to other travelers or not.

In the following, three samples, each consisting of 1000 airlines reviews and originating from the same platform are considered. The first sample is a random sample from the airline review platform, covering in total 195 different airlines. The other two samples are stratified random samples based on the type of airline, namely (a) low cost airline and (b) network airline only. Each of the three samples is balanced, i.e., they contain equal numbers of reviews recommending and not recommending an airline. This allows to properly perform the analyses and to evaluate the different machine learning classifiers. For each review, we take into account the review’s text, the airline discussed and the overall recommendation decision.

# ACCEPTED MANUSCRIPT

## 3.3 Data Preprocessing and Projection

On airlinequality.com, travelers also have the ability to provide star ratings to express their evaluation about specific service aspects regarding their flight experience with the airline such as seat comfort and ground service. Nevertheless, as these fields are not mandatory, they are not provided in every review, and thus missing in a significant portion of the reviews in our dataset. As such, these ratings cannot be used reliably as variables or predictors of customer recommendation in further analysis. However, this again highlights the need for be integrated in performance dashboards, and to further determine overall key performance indicators, for instance, in form of promoter scores. In the absence of specific star ratings corresponding to each service aspect, we perform an automated content analysis of the different online reviews’ texts guided by the AD and MPAA theoretical models. As shown by previous research, the opinion expressed within online reviews can be extracted by means of sentiment analysis (Feldman, 2013; Pang & Lee, 2008). We extend this approach further by aiming to extract the sentiment expressed towards the service as well as each of its specific aspects.

In order to extract the sentiment expressed within a review, we leverage the Harvard General Inquirer negative sentiment) (Stone, Dunphy, & Smith, 1966). We specifically take into account the word lists for positive (pos) and negative (neg) words that are used to determine the sentiment polarity expressed within the different reviews, as shown in Equation 1 (Tetlock, Saar-Tsechansky, & Macskassy, 2008). We summarize the occurrences of positive and negative words while taking negations into consideration (in case of a negation preceding the sentiment-bearing term, its orientation is reversed). As shown in Equation 1, sentiment polarity ranges from -1 (negative) to 1 (positive). Arguably, several terms in a review might indicate neutral sentiment. However, based on the AD theoretical model, we note that the diagnosticity, i.e., polarity of sentiment of a service-aspect, rather than a neutral stance, is likely to influence its recommendation by the reviewer.

$$
P o l a r i t y = \frac {p o s - n e g}{p o s + n e g} \quad (\text {Range: - 1 to 1})\tag{1}
$$

In order to further focus on the different service aspects within an online review, we additionally determine aspect-oriented sentiment measures. Given that such measures have not been previously applied in the field of airline reviews, we adopt a two-step approach: First, we identify service aspects and develop domain-specific word lists for topic detection in order to determine whether a specific part of a review deals with a certain topic (aspect) of interest. Next, we determine the sentiment polarity for each service aspect focusing on parts of the review that actually deal with those topics of interest. These two steps are described next.

For identifying the service aspects expressed and for developing domain-specific word lists that can be applied for topic detection, we adapt the approach proposed by Loughran and McDonald (2011). We analyze the different words which are contained in the whole corpus of online reviews. We manually analyze each word occurring in more than 2.5% of the online reviews. On the one hand, we check whether it belongs to the main airline service aspects that represent evaluation categories available for rating flight experiences on airlinequality.com, namely: Seat Comfort, Cabin Staff Service, Inflight Entertainment, Food & Beverages, Ground Service, Value For Money, and Wifi & Connectivity and map ese to the core and augmented service categories, i.e. whether they relate to the core service (e.g. seat comfort) or whether they can be regarded as ancillary (e.g. food or entertainment, see Table 1). On the other hand, we focus on the core and augmented service concept as well as past empirical studies (i.e. Aksoy, Atilgan, and Akinci (2003), Anderson, Pearo, and Widener (2008), Chen and Chang (2005) and Gilbert and Wong (2003)) to identify aspects beyond the categories available on airlinequality.com. Following this procedure, we also identify Punctuality, Safety, and Aircraft as additional service aspects of interest. We recognize Value for Money as neither a core nor an augmented service aspect. Table 1 summarizes the resulting word lists.

After creating the word lists, we determine the sentiment polarity for each service aspect. For that purpose, we split a review into sentence-level units, and analyze whether at least one term related to a service aspect is contained in the sentences. For each sentence of the review fulfilling this condition, we then calculate the sentiment polarity according to Equation 1. Finally, we determine the average sentiment polarity related to each aspect on a review-level. As the punctuality category contains positive and negative words, we calculate punctuality based on Equation 1. The specific variable operationalization is summarized in Table 2.

Table 1. Developed Word Lists to Extract Service Aspects from Online Reviews

<table><tr><td>Category</td><td></td><td>Name</td><td>Identifying Words</td></tr><tr><td rowspan="6">Core Service Aspects</td><td>Aircraft</td><td>aircraft</td><td>aeroplane, airplane, airbus, aircraft, boeing, plane</td></tr><tr><td>Seat Comfort</td><td>seat</td><td>legroom, room, seat, space</td></tr><tr><td rowspan="2">Safety</td><td rowspan="2">safety</td><td>positive: reliable, safe, stable</td></tr><tr><td>negative: unreliable, unsafe, instable,</td></tr><tr><td rowspan="2">Punctuality</td><td rowspan="2">punctuality</td><td>positive: punctual, on time, quick, on schedule</td></tr><tr><td>negative: delay, cancel, wait, miss, reschedule, late, postpone, slow</td></tr><tr><td rowspan="5">Augmented Service Aspects</td><td>Ground Service</td><td>ground_service</td><td>baggage, ground, lounge, terminal</td></tr><tr><td>Cabin Staff Service</td><td>cabin_staff</td><td>crew, staff</td></tr><tr><td>Food &amp; Beverages</td><td>food_beverages</td><td>beverage, breakfast, coffee, dinner, drink, food, lunch, meal, sandwich, snack</td></tr><tr><td>Inflight Entertainment</td><td>entertainment</td><td>entertainment, movie, TV</td></tr><tr><td>Wifi &amp; Connectivity</td><td>wifi</td><td>online, wifi, wi-fi</td></tr><tr><td>Value For Money</td><td></td><td>value_money</td><td>cost, pay, price, ticket, value</td></tr></table>

Table 2. Variable Operationalization of Independent (IV) and Dependent Variables (DV)

<table><tr><td>Type</td><td>Variable</td><td>Description</td><td>Definition</td></tr><tr><td>DV</td><td>recommended</td><td>Binary variable measuring the reviewer&#x27;s recommendation of an airline.</td><td>0 = not recommended1 = recommended</td></tr><tr><td rowspan="12">IV</td><td>overall_sentiment</td><td>Measures the overall sentiment polarity expressed within the online review, based on the positive and negative word lists of the General Inquirer.</td><td>(pos - neg) / (pos + neg)Range: -1, 1</td></tr><tr><td>aircraft</td><td></td><td></td></tr><tr><td>seat</td><td></td><td></td></tr><tr><td>safety</td><td rowspan="8">Aspect-oriented sentiment variables that measure the sentiment expressed (sentiment polarity based on the General Inquirer) specifically related to the different aspects of the airline (measured at a sentence level). Covered aspects are aircraft type, seats, safety, staff, entertainment, food and beverages, ground service, value for money, wifi, and punctuality.</td><td rowspan="8">Average sentiment, ranging from -1 to 1, expressed in those sentences where the specific aspect is discussed.</td></tr><tr><td>punctuality</td></tr><tr><td>ground_service</td></tr><tr><td>cabin_staff</td></tr><tr><td>food_beverages</td></tr><tr><td>entertainment</td></tr><tr><td>wifi</td></tr><tr><td>value_money</td></tr><tr><td>words</td><td>Measures the quantity of words the online review consists of.</td><td>Number of words of the review</td></tr></table>

# ACCEPTED MANUSCRIPT

## 3.4 Explanatory Analysis

In order to analyze the recommendation decision, we perform a logistic regression analysis as it is suitable for binary dependent variables. We analyze three different models, each explaining the binary dependent variable of whether a specific airline has been recommended by the reviewer or not. Model 1 (Equation 2) only takes into account the review’s length, i.e., number of words in the review, as a control variable. It provides a baseline for comparing Models 2 and 3. Model 2 (Equation 3) takes into account the overall sentiment expressed within the review as an explanatory variable, while also controlling for the review’s length. Finally, Model 3 (Equation 4) takes into account each of the aspect-oriented sentiment variables for explaining the decision to recommend a specific airline, also while controlling for the review’s length. In all models, standard errors are clustered at airline level.

Pr(?????????????????????? = 1) = ??(???????????????? + ?? ?????????? + ??)

$$
w h e r e F \left(\beta^ {\prime} X\right) = e ^ {\beta^ {\prime} X} / \left(1 + e ^ {\beta^ {\prime} X}\right)\tag{2}
$$

Pr(?????????????????????? = 1) = ??(???????????????? + ?? ??????????????\_?????????????????? + ?? ?????????? + ??)

$$
w h e r e F \big (\beta^ {\prime} X \big) = e ^ {\beta^ {\prime} X} / (1 + e ^ {\beta^ {\prime} X})\tag{3}
$$

$$
\begin{array}{r l} \operatorname * {P r} (R e c o m m e n d e d = 1) & = F (c o n s t a n t + \beta_ {1} a i r c r a f t + \beta_ {2} s e a t \\ & + \beta_ {3} s a f e t y + \beta_ {4} p u n c t u a l i t y + \beta_ {5} g r o u n d \_ s e r v i c e + \beta_ {6} c a b i n \_ s t a f f + \beta_ {7} f o o d \_ b e v e r a g e s \\ & + \beta_ {8} e n t e r t a i n m e n t + \beta_ {9} w i f i + \beta_ {1 0} v a l u e \_ m o n e y + \beta_ {1 1} w o r d s + \varepsilon) \end{array}\tag{4}
$$

??ℎ?????? $F \big ( \beta ^ { \prime } X \big ) = e ^ { \beta ^ { \prime } X } / ( 1 + e ^ { \beta ^ { \prime } X } )$

## 3.5 Predictive Analysis

In assessing the ability of a review’s text contents to accurately predict a reviewer’s recommendation to other travelers, we build different predictive models and evaluate their performance. Toward that end, we propose specific model configurations incorporating different attributes to predict the airline recommendation. Furthermore, we evaluate different machine learning techniques. Finally, we validate our results with a recommended evaluation methodology in the machine learning field to ensure that the results are realistic and not an artifact of model overfitting.

## 3.5.1 Model Configuration

The different model configurations are summarized in Table 3, and differ with respect to predictors used. Model Configurations A and B take into account the different sentiment variables. Whereas Configuration A takes into account the overall sentiment of the airline review, Configuration B takes into account the more granular service aspect-oriented variables. Particularly, only those specific aspect-oriented sentiment variables that are found to have a significant influence on the airline recommendation are considered as Configuration B builds on the results from the explanatory analysis.

Finally, Configuration C uses a classical text mining approach, bag-of-words, that is based on the different words of the text and thus has a more comprehensive feature set. This model configuration is later used to compare the results for models involving sentiment analysis. To be able to generate the term document matrix, we preprocess the reviews by means of tokenization, stop word filtering, stemming, n-gram generation and feature selection (Miner, 2012).

Table 3. Model Configurations

<table><tr><td>Configuration</td><td>Name</td><td>Description</td></tr><tr><td>A</td><td>Overall-Sentiment</td><td>Model that takes into account overall_sentiment as input variable</td></tr><tr><td>B</td><td>Aspect-Specific-Sentiment</td><td>Model that takes into account the different significant aspect-oriented sentiment variables into account</td></tr><tr><td>C</td><td>Bag-of-Words</td><td>Classical text mining approach based on a bag-of-words model, takes into account a review&#x27;s words</td></tr></table>

## 3.5.2 Machine Learning Techniques

We evaluate the performance of different machine learning techniques in predicting the recommendation decision. Toward that goal, we perform supervised learning and learn from pre-labeled examples, i.e. the online reviews and the indication of the reviewer expressing the airline recommendation. In this context, we concentrate on Naïve Bayes (NB) as a rather simple learning algorithm as well as Neural Network (NN) and Support Vector Machine (SVM) representing more complex learning algorithms (Kotsiantis, 2007).

Naïve Bayes represents a simple machine learning technology relying on the Bayes theorem. Classifiers built upon the Bayes theorem are assumed to be naïve as they assume the independence of the different input variables. In Naïve Bayes classifiers, instances are classified based on the joint probabilities of their input variables. Although Naïve Bayes classifiers are rather simple and rely on potentially unrealistic assumptions, they have nevertheless been proven to generally perform well and in fact have the advantage of requiring low computational effort and thus being more time-efficient (Langley, Iba, & Thompson, 1992).

Neural Networks consist of a variety of (computational) neurons appearing in interconnected input, hidden, and output layers, and are intended to mimic the behavior of human neural networks. To achieve this behavior, weights are assigned to the connections between different neurons. Furthermore, each neuron has an activation function which is used to process the input of the neuron. The output neuron uses, as input, the weighted sum of outputs from neurons in the previous layer (or input variables in case of the initial input layer), and applies the activation function to the input (Han & Kamber, 2006). When a neural network is trained, the weights of the different neurons are updated so that the overall neural network’s output corresponds to the actual classification (Nisbet, Elder, & Miner, 2009). In this study, we apply a feed-forward neural network using backpropagation. As activation function, we use the most commonly adopted sigmoid function (Fuller, Biros, & Wilson, 2009).

Support Vector Machine (Vapnik, 1995) represents another machine learning technique that is based upon the principle of finding the maximum margin hyperplane that maximizes the distances between instances of different classes (Kotsiantis, 2007). As a linear separation of observations is not always possible, transformations are conducted by means of kernel functions that enable a separation of the observations according to their appropriate kernel. We select the parameters of the kernel function by means of the grid-search heuristic proposed by (Hsu et al., 2003).

## 3.5.3 Evaluation Methodology

In order to evaluate the different predictive models, we perform stratified 10-fold cross-validation (Kohavi, 1995). This evaluation procedure is advantageous as it avoids overfitting based on the notion that classifier training and classifier testing are performed on separate observations (Mitchell, 1997). Furthermore, previous research has found that 10-fold stratified cross-validation performs best for evaluating models trained with realworld datasets such as the one in this study (Kohavi, 1995).

Within stratified 10-fold cross-validation, the whole sample is split into 10 different parts with equal class distributions. Next, nine parts are used for classifier training, whereas the remaining part is used for testing. This procedure is repeated by changing the different folds, so that each part is used nine times for training and one time for testing. After each iteration, the classification performance is determined by the number of correctly (true positives (TP), true negatives (TN)) as well as incorrectly classified (false positives (FP), false negatives (FN)) examples. These are depicted in an illustrative confusion matrix shown in Table 4.

Table 4. Illustrative Confusion Matrix

<table><tr><td></td><td>Actual recommended</td><td>Actual not recommended</td></tr><tr><td>Predicted recommended</td><td>TP</td><td>FP</td></tr><tr><td>Predicted not recommended</td><td>FN</td><td>TN</td></tr></table>

At the end of 10-fold cross-validation, different performance measures can be calculated. These performance measures are presented in Equations 5-8 (displayed for class positive: recommended=1).

$$
A c c u r a c y = \frac {T P + T N}{T P + F P + T N + F N}\tag{5}
$$

$$
R e c a l l = \frac {T P}{T P + F N}\tag{6}
$$

$$
P r e c i s i o n = \frac {T P}{T P + F P}\tag{7}
$$

$$
F _ {1} = 2 \cdot \frac {\text {Precision} \cdot \text {Recall}}{\text {Precision} + \text {Recall}}\tag{8}
$$

To summarize, accuracy measures the total number of observations classified correctly (TP+TN), divided by the total number of observations (TP+FP+TN+FN). Precision measures how precise a classifier is, i.e. whether an example classified to belong to a specific class actually belongs to that class (TP / (TP+FP)) respectively (TN / (TN + FN)). Similarly, recall measures the percentage of many observations of a specific class are actually identified to belong to that class (TP / (TP + FN), TN / (TN + FP)). The $\mathrm { F } _ { 1 }$ measure aggregates precision and recall using their harmonic mean. This is worth noting, as often, precision and recall are related to each other and a high precision is accompanied by a low recall, and vice versa.

## 4. Empirical Study

## 4.1 Descriptive Statistics

Table 5 shows the descriptive statistics of the sample of airline reviews analyzed within this study. We observe that the overall sentiment as well as most aspect-oriented sentiment variables differ between (a) online reviews that recommend an airline and (b) online reviews that do not recommend an airline.

Interestingly, the overall sentiment is much more positive for recommending reviews than for nonrecommending reviews. Regarding the different aspects of the service offered, the descriptive statistics show that the friendliness of the cabin staff is usually evaluated with much more positive sentiment than the ground service. It is interesting to note that the sentiment expressed regarding the “value for money” aspect is positive even for non-recommending reviews. Finally, the number of words related to non-recommending reviews is significantly larger than the number of words of This provides an indication that nonrecommending reviews might provide a stronger rationale for not recommending a certain airline based on flight experiences.

Table 5. Descriptive Statistics

<table><tr><td rowspan="3">Variable</td><td colspan="4">Random Sample</td><td rowspan="2" colspan="2">LCC Airline Random Sample</td><td rowspan="2" colspan="2">FSNC Airline Random Sample</td></tr><tr><td colspan="2">Airline Not Recommended</td><td colspan="2">Airline Recommended</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>overall_sentiment</td><td>-0.024</td><td>0.381</td><td>0.388</td><td>0.358</td><td>0.166</td><td>0.421</td><td>0.154</td><td>0.414</td></tr><tr><td>aircraft</td><td>-0.017</td><td>0.394</td><td>0.082</td><td>0.392</td><td>0.038</td><td>0.369</td><td>0.032</td><td>0.390</td></tr><tr><td>seat</td><td>-0.050</td><td>0.434</td><td>0.214</td><td>0.499</td><td>0.082</td><td>0.426</td><td>0.112</td><td>0.486</td></tr><tr><td>safety</td><td>0.034</td><td>0.192</td><td>0.030</td><td>0.171</td><td>0.035</td><td>0.189</td><td>0.025</td><td>0.191</td></tr><tr><td>punctuality</td><td>-0.141</td><td>0.623</td><td>0.225</td><td>0.640</td><td>0.063</td><td>0.699</td><td>0.042</td><td>0.668</td></tr><tr><td>ground_service</td><td>-0.031</td><td>0.254</td><td>0.081</td><td>0.321</td><td>0.020</td><td>0.268</td><td>0.023</td><td>0.319</td></tr><tr><td>cabin_staff</td><td>-0.013</td><td>0.448</td><td>0.324</td><td>0.500</td><td>0.153</td><td>0.471</td><td>0.143</td><td>0.479</td></tr><tr><td>food_beverages</td><td>-0.042</td><td>0.459</td><td>0.264</td><td>0.484</td><td>0.064</td><td>0.332</td><td>0.131</td><td>0.482</td></tr><tr><td>entertainment</td><td>0.030</td><td>0.313</td><td>0.151</td><td>0.381</td><td>0.020</td><td>0.204</td><td>0.088</td><td>0.353</td></tr><tr><td>wifi</td><td>0.002</td><td>0.154</td><td>0.004</td><td>0.145</td><td>0.010</td><td>0.183</td><td>0.007</td><td>0.142</td></tr><tr><td>value_money</td><td>0.048</td><td>0.399</td><td>0.088</td><td>0.365</td><td>0.087</td><td>0.397</td><td>0.069</td><td>0.358</td></tr><tr><td>words</td><td>139.124</td><td>89.804</td><td>97.466</td><td>58.684</td><td>119.568</td><td>75.792</td><td>132.782</td><td>81.123</td></tr></table>

## ACCEPTED MANUSCRIPT

Focusing on the distinction between LCC and FSNC airlines, we observe that especially seat comfort as core service aspect as well as entertainment and food as augmented service aspects are evaluated much more positive in case of FSNC Airlines. This is specifically related to the business model of LCC airlines, which provide fewer amenities for lower prices. Interestingly, the punctuality is slightly more positive in case of LCC than for FSNC which can also be explained by the business model of LCC as they try to implement more efficient business processes (e.g. shorter and more efficient ground handling) in order to increase profit.

Table 6. Variable Correlations

<table><tr><td></td><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>1</td><td>recommended</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>overall_sentiment</td><td>0.49</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>aircraft</td><td>0.13</td><td>0.28</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>seat</td><td>0.27</td><td>0.43</td><td>0.19</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>safety</td><td>0.28</td><td>0.26</td><td>0.12</td><td>0.09</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>punctuality</td><td>-0.01</td><td>0.04</td><td>0.00</td><td>-0.07</td><td>0.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>ground_service</td><td>0.19</td><td>0.20</td><td>0.09</td><td>0.11</td><td>0.04</td><td>0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>cabin_staff</td><td>0.33</td><td>0.45</td><td>0.12</td><td>0.16</td><td>0.17</td><td>0.06</td><td>0.17</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>food_beverages</td><td>0.31</td><td>0.41</td><td>0.11</td><td>0.21</td><td>0.04</td><td>-0.04</td><td>0.07</td><td>0.23</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>entertainment</td><td>0.17</td><td>0.24</td><td>0.04</td><td>0.12</td><td>0.03</td><td>-0.01</td><td>0.01</td><td>0.11</td><td>0.21</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>11</td><td>wifi</td><td>0.01</td><td>0.07</td><td>-0.01</td><td>0.06</td><td>0.04</td><td>0.00</td><td>0.06</td><td>0.00</td><td>0.06</td><td>0.01</td><td>1.00</td><td></td><td></td></tr><tr><td>12</td><td>value_money</td><td>0.05</td><td>0.24</td><td>0.09</td><td>0.12</td><td>0.04</td><td>-0.01</td><td>0.03</td><td>0.01</td><td>0.08</td><td>0.04</td><td>0.04</td><td>1.00</td><td></td></tr><tr><td>13</td><td>words</td><td>-0.27</td><td>-0.18</td><td>-0.07</td><td>-0.11</td><td>-0.04</td><td>0.09</td><td>-0.05</td><td>-0.07</td><td>-0.04</td><td>0.02</td><td>-0.02</td><td>0.04</td><td>1.00</td></tr></table>

Table 6 provides an overview on the correlations of the different variables taken into account. We note a high correlation between the overall sentiment of the review and the recommendation expressed by a reviewer. The correlations among the various service aspect-oriented sentiment variables are observed to be very low. Based on this, these variables can be assumed to be measuring distinct aspects of the review and do not indicate concern for multicollinearity when taken into account concurrently within the explanatory analysis. Furthermore, it can be observed that several aspect-oriented sentiment variables are moderately correlated with the overall sentiment expressed in the review. This observation validates the decision to consider the overall sentiment and the aspect-oriented variables in separate explanatory models (Equations 3 and 4) to avoid potential side-effects.

## 4.2 Explanatory Analysis

Table 7 shows the results of the explanatory analysis. In this analysis, we first take into account the control variables only (Model 1), overall sentiment (Model 2), as well as the aspect-specific sentiment in order to disentangle the recommendation decision, also focusing on the business model (Models 3 through 5). Furthermore, we also determine the explanatory power of core and augmented service aspects.

Table 7. Logit Regression Results  
Explaining Airline Recommendations by Means of Textual Review Aspects (n=1,000)

<table><tr><td rowspan="2">Variable</td><td colspan="2">(1) Base Model (Random Sample)</td><td colspan="2">(2) Overall Sentiment (Random Sample)</td><td colspan="2">(3) Aspect-Oriented Sentiment (Random Sample)</td><td colspan="2">(4) Aspect-Oriented Sentiment (LCC Sample)</td><td colspan="2">(5) Aspect-Oriented Sentiment (FSNC Sample)</td></tr><tr><td>Coef.</td><td>p-value</td><td>Coef.</td><td>p-value</td><td>Coef.</td><td>p-value</td><td>Coef.</td><td>p-value</td><td>Coef.</td><td>p-value</td></tr><tr><td>Constant</td><td>0.937</td><td>&lt;0.01***</td><td>0.235</td><td>0.157</td><td>0.567</td><td>&lt;0.01***</td><td>0.447</td><td>0.06*</td><td>0.343</td><td>0.49</td></tr><tr><td>overall_sentiment</td><td></td><td></td><td>2.892</td><td>&lt;0.01***</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>aircraft</td><td></td><td></td><td></td><td></td><td>0.011</td><td>0.96</td><td>0.515</td><td>0.16</td><td>0.423</td><td>0.01**</td></tr><tr><td>seat</td><td></td><td></td><td></td><td></td><td>0.822</td><td>&lt;0.01***</td><td>0.466</td><td>&lt;0.01***</td><td>0.948</td><td>&lt;0.01***</td></tr><tr><td>safety</td><td></td><td></td><td></td><td></td><td>-0.009</td><td>0.98</td><td>0.715</td><td>&lt;0.01***</td><td>0.647</td><td>0.16</td></tr><tr><td>punctuality</td><td></td><td></td><td></td><td></td><td>0.860</td><td>&lt;0.01***</td><td>0.765</td><td>&lt;0.01***</td><td>0.949</td><td>&lt;0.01***</td></tr><tr><td>ground_service</td><td></td><td></td><td></td><td></td><td>1.312</td><td>&lt;0.01***</td><td>0.349</td><td>0.21</td><td>0.377</td><td>0.23</td></tr><tr><td>cabin_staff</td><td></td><td></td><td></td><td></td><td>1.052</td><td>&lt;0.01***</td><td>1.657</td><td>&lt;0.01***</td><td>1.025</td><td>&lt;0.01***</td></tr><tr><td>food_beverages</td><td></td><td></td><td></td><td></td><td>1.164</td><td>&lt;0.01***</td><td>0.951</td><td>&lt;0.01***</td><td>1.124</td><td>&lt;0.01***</td></tr><tr><td>entertainment</td><td></td><td></td><td></td><td></td><td>0.853</td><td>&lt;0.01***</td><td>0.195</td><td>0.23</td><td>0.706</td><td>&lt;0.01***</td></tr><tr><td>wifi</td><td></td><td></td><td></td><td></td><td>-0.627</td><td>0.28</td><td>0.646</td><td>0.15</td><td>0.857</td><td>0.39</td></tr><tr><td>value_money</td><td></td><td></td><td></td><td></td><td>0.108</td><td>0.66</td><td>-0.377</td><td>0.01**</td><td>0.106</td><td>0.49</td></tr><tr><td>words</td><td>-0.008</td><td>&lt;0.01***</td><td>-0.006</td><td>&lt;0.01***</td><td>-0.009</td><td>&lt;0.01***</td><td>-0.007</td><td>&lt;0.01***</td><td>-0.006</td><td>&lt;0.01***</td></tr><tr><td> $p > \chi^2$ </td><td></td><td>&lt;0.01***</td><td></td><td>&lt;0.01***</td><td></td><td>&lt;0.01***</td><td></td><td>&lt;0.01***</td><td></td><td>&lt;0.01***</td></tr><tr><td>Pseudo  $R^2$ </td><td></td><td>0.056</td><td></td><td>0.224</td><td></td><td>0.273</td><td></td><td>0.221</td><td></td><td>0.256</td></tr><tr><td>Δ Pseudo  $R^2$ </td><td></td><td></td><td></td><td>+0.168</td><td></td><td>+0.217</td><td></td><td></td><td></td><td></td></tr><tr><td>Δ core</td><td></td><td></td><td></td><td></td><td></td><td>+0.058</td><td></td><td>+0.054</td><td></td><td>+0.080</td></tr><tr><td>Δ augmented</td><td></td><td></td><td></td><td></td><td></td><td>+0.117</td><td></td><td>+0.091</td><td></td><td>+0.087</td></tr></table>

Significance Levels: \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.10

Focusing on Model 1 (Equation 2), which only takes into account the number of words of the review as a baseline setup, we observe that the number of words has a negative influence on the question of whether a specific airline is recommended (significant at a 1% level). Consequently, it can be argued that reviewers not recommending a specific product put more emphasis on describing the specific reasons of their decision, which in turn increases the review’s length.

In case of Model 2 (Equation 3) that takes into account the overall sentiment expressed within the review, we observe a positive impact of the overall sentiment expressed on the reviewer’s decision to recommend the airline service (significant at a 1% level). In other words, reviewers who are more positive about a flight experience are more likely to recommend the airline to others. This result shows that textual aspects of the reviews are valuable.

Model 3 (Equation 4) provides further insights into the drivers of the airline recommendation by analyzing whether the sentiment expressed towards individual service aspects of the service influences the airline recommendation. The results indicate that the reviewer’s perception of the airline’s seats, the punctuality, the ground service offered, the friendliness of the cabin staff, the quality of the food offered as well as the entertainment have a positive influence on the recommendation decisi nsequently, if reviewers express a positive sentiment towards these aspects, they are likely to reco nd the airline. Interestingly, the perception of the wifi connectivity and of the value for money have no significant influence on the recommendation decision, suggesting that once a traveler has decided to select a specific airline for a specific price level, other aspects of the service experience become more salient determining the perceived experience.

Taking into account the differences in case of LCC and FSNC airlines, we observe that customers focusing Instead, value for money has a slightly negative effect and safety is important. In case of FSNC airlines, the aircraft has a positive influence.

Regarding the overall quality of our results, the null hypothesis that none of the explanatory variables have an impact on the airline recommendation is rejected with a high level of confidence in all models (p < 0.01) in favor of the alternative hypothesis. Thus, results of the analysis can be regarded as valuable. Furthermore, in regards to Model 2, it can be noted that taking into account the overall sentiment considerably improves the model compared to the baseline (Regression 2, ∆ Pseudo R² = +0.168). Furthermore, with Model 3, we find that taking into account the sentiment related to the different airline service aspects separately also improves the model compared to the baseline (Regression 3, ∆ Pseudo $\mathrm { R } ^ { 2 } = + 0 . 2 1 7 )$ . As the increase in Pseudo R² for Model 3 is higher than in case of Model 2, this shows that the sentiments of service-specific aspects contained in the review are important for explaining the recommendation decision. Nevertheless, as also shown by the results, this increase in explanatory power is also dependent on the business model.

Finally, considering the explanatory power of core and augmented service aspects, we observe that augmented service aspects have a higher influence on the explanatory power than core service aspects. However, when analyzing based on the business model, we also find that while augmented service aspects are almost equally important in case of LCC and FSNC airlines (influence on Pseudo R² +0.091 and +0.087), core service aspects are much more important in case of FSNC airlines (influence on Pseudo R² +0.054 and +0.080).

## 4.3 Predictive Analysis

Table 8. Classifier Evaluation, Random Sample  
Metrics are based on stratified 10-fold cross-validation

<table><tr><td rowspan="2">Classifier</td><td rowspan="2">Configuration</td><td rowspan="2">Algorithm</td><td rowspan="2">Accuracy</td><td colspan="3">Recommended</td><td colspan="3">Not Recommended</td></tr><tr><td>Prec.</td><td>Recall</td><td>F1</td><td>Prec.</td><td>Recall</td><td>F1</td></tr><tr><td>A</td><td rowspan="3">Overall-Sentiment</td><td>Naïve Bayes</td><td>72.70</td><td>70.38</td><td>78.40</td><td>74.17</td><td>75.62</td><td>67.00</td><td>71.05</td></tr><tr><td>B</td><td>Neural Network</td><td>75.00</td><td>73.23</td><td>78.80</td><td>75.91</td><td>77.06</td><td>71.20</td><td>74.01</td></tr><tr><td>C</td><td>SVM</td><td>74.70</td><td>74.26</td><td>75.60</td><td>74.92</td><td>75.15</td><td>73.80</td><td>74.47</td></tr><tr><td>D</td><td rowspan="3">Aspect-Specific-Sentiment</td><td>Naïve Bayes</td><td>73.90</td><td>75.59</td><td>70.60</td><td>73.01</td><td>72.42</td><td>77.20</td><td>74.73</td></tr><tr><td>E</td><td>Neural Network</td><td>73.80</td><td>74.79</td><td>71.80</td><td>73.26</td><td>72.88</td><td>75.80</td><td>74.31</td></tr><tr><td>F</td><td>SVM</td><td>75.80</td><td>76.54</td><td>74.40</td><td>75.45</td><td>75.10</td><td>77.20</td><td>76.14</td></tr><tr><td>G</td><td rowspan="3">Bag-of-Words</td><td>Naïve Bayes</td><td>77.70</td><td>75.51</td><td>82.00</td><td>78.62</td><td>80.31</td><td>73.40</td><td>76.70</td></tr><tr><td>H</td><td>Neural Network</td><td>75.70</td><td>71.82</td><td>85.60</td><td>78.11</td><td>81.27</td><td>66.80</td><td>73.33</td></tr><tr><td>I</td><td>SVM</td><td>80.80</td><td>80.43</td><td>81.40</td><td>80.91</td><td>81.17</td><td>80.20</td><td>80.68</td></tr></table>

The results of the predictive analysis in case of the random airline sample are shown in Table 8. The results show that the classifiers built upon the overall review sentiment (Classifiers A-C) as well as the individual service aspect-specific sentiment (Classifiers D-F) have a comparable predictive accuracy (up to 75.80%). Further, classifiers based on the bag-of-words features (Classifiers G-I) exhibit very good performance when predicting the overall recommendation hidden in unstructured online service reviews (predictive accuracy up to

80.80%). These results show that machine learning classifiers trained on the bag-of-words features as well as sentiment-based features allow to predict whether an online reviewer would ultimately recommend a specific airline and that the bag-of-words model outperforms the other configurations.

Table 9. Classifier Evaluation, LCC Airline Sample Metrics are based on stratified 10-fold cross-validation

<table><tr><td rowspan="2">Classifier</td><td rowspan="2">Configuration</td><td rowspan="2">Algorithm</td><td rowspan="2">Accuracy</td><td colspan="3">Recommended</td><td colspan="3">Not Recommended</td></tr><tr><td>Prec.</td><td>Recall</td><td>F1</td><td>Prec.</td><td>Recall</td><td>F1</td></tr><tr><td>A</td><td rowspan="3">Overall-Sentiment</td><td>Naïve Bayes</td><td>71.30</td><td>71.43</td><td>71.00</td><td>71.21</td><td>71.17</td><td>71.60</td><td>71.38</td></tr><tr><td>B</td><td>Neural Network</td><td>70.20</td><td>70.12</td><td>70.40</td><td>70.26</td><td>70.28</td><td>70.00</td><td>70.14</td></tr><tr><td>C</td><td>SVM</td><td>69.50</td><td>71.71</td><td>64.40</td><td>67.86</td><td>67.70</td><td>74.60</td><td>70.98</td></tr><tr><td>D</td><td rowspan="3">Aspect-Specific-Sentiment</td><td>Naïve Bayes</td><td>69.80</td><td>77.05</td><td>56.40</td><td>65.13</td><td>65.62</td><td>83.20</td><td>73.37</td></tr><tr><td>E</td><td>Neural Network</td><td>73.20</td><td>76.24</td><td>67.40</td><td>71.55</td><td>70.79</td><td>79.00</td><td>74.67</td></tr><tr><td>F</td><td>SVM</td><td>73.70</td><td>77.12</td><td>67.40</td><td>71.93</td><td>71.05</td><td>80.00</td><td>75.26</td></tr><tr><td>G</td><td rowspan="3">Bag-of-Words</td><td>Naïve Bayes</td><td>81.60</td><td>82.24</td><td>80.60</td><td>81.41</td><td>80.98</td><td>82.60</td><td>81.78</td></tr><tr><td>H</td><td>Neural Network</td><td>80.00</td><td>85.89</td><td>71.80</td><td>78.22</td><td>75.77</td><td>88.20</td><td>81.51</td></tr><tr><td>I</td><td>SVM</td><td>82.60</td><td>83.27</td><td>81.60</td><td>82.43</td><td>81.96</td><td>83.60</td><td>82.77</td></tr></table>

Table 10. Classifier Evaluation, FSNC Airline Sample Metrics are based on stratified 10-fold cross-validation

<table><tr><td rowspan="2">Classifier</td><td rowspan="2">Configuration</td><td rowspan="2">Algorithm</td><td rowspan="2">Accuracy</td><td colspan="3">Recommended</td><td colspan="3">Not Recommended</td></tr><tr><td>Prec.</td><td>Recall</td><td>F1</td><td>Prec.</td><td>Recall</td><td>F1</td></tr><tr><td>A</td><td rowspan="3">Overall-Sentiment</td><td>Naïve Bayes</td><td>74.00</td><td>73.53</td><td>75.00</td><td>74.26</td><td>74.49</td><td>73.00</td><td>73.74</td></tr><tr><td>B</td><td>Neural Network</td><td>72.70</td><td>72.65</td><td>72.80</td><td>72.72</td><td>72.75</td><td>72.60</td><td>72.67</td></tr><tr><td>C</td><td>SVM</td><td>75.00</td><td>74.51</td><td>76.00</td><td>75.25</td><td>75.51</td><td>74.00</td><td>74.75</td></tr><tr><td>D</td><td rowspan="3">Aspect-Specific-Sentiment</td><td>Naïve Bayes</td><td>74.60</td><td>76.39</td><td>71.20</td><td>73.70</td><td>73.03</td><td>78.00</td><td>75.43</td></tr><tr><td>E</td><td>Neural Network</td><td>73.70</td><td>73.94</td><td>73.20</td><td>73.57</td><td>73.20</td><td>74.20</td><td>73.70</td></tr><tr><td>F</td><td>SVM</td><td>75.30</td><td>76.41</td><td>73.20</td><td>74.77</td><td>74.20</td><td>77.40</td><td>75.77</td></tr><tr><td>G</td><td rowspan="3">Bag-of-Words</td><td>Naïve Bayes</td><td>82.30</td><td>78.99</td><td>88.00</td><td>83.25</td><td>86.46</td><td>76.60</td><td>81.23</td></tr><tr><td>H</td><td>Neural Network</td><td>84.60</td><td>82.64</td><td>87.60</td><td>85.05</td><td>86.81</td><td>81.60</td><td>84.12</td></tr><tr><td>I</td><td>SVM</td><td>85.00</td><td>84.45</td><td>85.80</td><td>85.12</td><td>85.57</td><td>84.20</td><td>84.88</td></tr></table>

Table 9 and Table 10 show the results of the classifier evaluation in case of the LCC and FSNC airline sample. Here, the sentiment-based classifiers show comparable performance. Interestingly, in case of the bag-of words classifiers, a slightly improved performance (predictive accuracy up to 82.60% and 85.00% for LCC and FSNC samples respectively) can be observed. This can be attributed to the more specific adaptation to the specific language used in case of LCC and FSNC airline reviews.

Regarding the different machine learning algorithms, we observe that Neural Networks and SVM perform slightly better than Naïve Bayes in predicting the airline recommendation from unstructured user-generated online reviews. Interestingly, it is observed that classifiers taking into account only the overall sentiment achieve a comparable predictive accuracy when compared with classifiers focusing on aspect-oriented sentiment. Furthermore, from the point of view of predicting the consumer recommendation with high racy as well as with high precision and recall, it makes sense to focus on the bag-of-words classifier. Thus, classifiers built upon the contents of the online review are valuable to assess reviews that do not contain specific hints regarding the reviewer’s recommendation decision. Such a predictive model can be used to compute promoter scores directly based on customer sentiments in online reviews.

Last, but not least, the transparency gained from using individual service aspect-oriented sentiment measures cannot be understated as well. In contrast to a bag-of-words-model, a model based on aspect-oriented sentiment breaks down the online review to specific metrics instead of taking into account the single words in the review. Thus, models using aspect-oriented sentiment metrics as performance indicators for specific service aspects are very applicable in enterprise performance dashboards as they provide more transparency although accompanied with slightly lower performance. The aforementioned approaches can thus be conceived to be on a spectrum with three levels: (a) highest predictive accuracy with little to no understanding of the underlying predictors, (b) relatively high predictive accuracy with high-level understanding of prediction based on overall sentiment expressed, (c) relatively high predictive accuracy with granular depiction of sentiment for various service aspects as contributors to the prediction.

## 5. Discussion

With this study, we first identify the different core and augmented service aspects expressed in online reviews focusing on airline services (referring to RQ1a). The results of the study clearly show that a reviewer’s recommendation can be explained by service aspects expressed in online reviews (RQ1b) and thus confirm our

## ACCEPTED MANUSCRIPT

theoretical reasoning based on the accessibility-diagnosticity as well as the multiple pathway anchoring and adjustment model. As shown by the explanatory analysis, the sentiment expressed within airline reviews has a significant influence on the question of whether a reviewer recommends a specific airline or not. Furthermore, the reviewer’s perception of the specific aspects of the service offered, i.e. the sentiment expressed regarding aspects like food or ground service, also has a significant influence on the expressed recommendation. From a managerial standpoint, the service aspects that are found to be significant in influencing customer recommendation can form the basis for actionable improvements in the airline service offerings, and can guide further customer-based research studies.

In addition, as shown by the predictive analysis, we demonstrate that aspect-specific sentiment extracted from the reviews also has predictive power in case of forecasting airline recommendations (RQ2). We show that predictive models taking into account specific airline-related aspects perform well and that the generic bag-ofwords model is valuable. Here, bag-of-words classifiers directly adapt to the language used for a specific category of airline and thus perform slightly better than sentiment assifiers. In contrast, sentiment-based classifiers can be considered to be more general as they foc ore general textual aspects. However, the different service categories that has a clear pragmatic interpretation, compared to the different words of the text within the bag-of-words classifiers.

The classifiers built upon the overall sentiment perform comparable to classifiers based on the specific aspect-related sentiment scores. This shows that for predicting the recommendation decision with high-level sentiment understanding of the review, an overall analysis of the review may be sufficient. Nevertheless, specific scores are valuable if an airline wants to understand drivers of the consumer evaluation of different service aspects. The predictive analysis and the results of the stratified 10-fold cross-validation suggest that although the Pseudo R² of the explanatory analysis is not very high, a satisfactory classification performance can be achieved by applying machine learning methodologies.

In case of LCC and FSNC airlines (RQ3), slightly differing results are observed when focusing on the differences of the business model, mainly concerning the amenities offered. In that regard, core and augmented service aspects are found to be of relevance. The results suggest that LCC airlines should particularly improve augmented service aspects in order to foster consumer recommendations, which is interesting as the business model of LCC airlines is typically focused on providing the core service. Also, interestingly, value for money has no (or even a slightly negative) impact on the recommendation decision. A possible rationale for this result is the notion that as soon as a specific airline is selected according to a customer’s willingness to pay, other aspects come to the forefront when deciding whether an airline can be recommended or not. If mentioned in the case of but also criticizes other service aspects (e.g. “the prices are great, but…”). Additionally, the changing environmental conditions have now blurred the lines between LCC and FSNC to some extent, where LCC ticket prices are not always drastically cheaper than FSNCs, mainly due to operating efficiency gains by FSNCs over the years.

We are also aware of several limitations of our study. First, we are aware of the risk of overfitting related to predictive models which might lead to overoptimistic results. In order to avoid the results in this study being influenced by overfitting, we specifically take care that the predictive models are never trained and evaluated by taking into account the same observations. This is ensured by applying stratified 10-fold cross-validation model evaluation strategy that alleviates the risk of model overfitting.

Due to our supervised learning approach, the different online reviews under investigation have to include the recommendation decision (“yes” or “no”) in order to be able to train and evaluate the model. Based on the 10- fold cross-validation evaluation, the results are generalizable out-of-sample and can be considered to also hold when the recommendation decision is not given at all– assuming that the structure of the online reviews is the same. Despite this issue, through our approach we demonstrate how to extract the specific service aspects from online reviews, which is valuable by itself, for instance, to aggregate the information given in numerous online reviews and to display this information in performance dashboards. Nevertheless, realistically, we assume this structural change to be unlikely, given that the main aim of online reviews, i.e., evaluating the product or service and providing support during the purchase decision making process, can be expected to be the same in all cases.

## ACCEPTED MANUSCRIPT

We are also cognizant that other factors apart from aspects discussed in the online review might influence the recommendation of a service. For instance, specific aspects of an airline such as the image of the airline’s home country might also affect the recommendation. Given that such background information is not available, we indirectly cover this aspect by clustering the standard errors in the explanatory analysis taking into account the different airlines.

As previous research has shown, there might be a rating inflation regarding online review star ratings (Wolff-Mann, 2016). Assuming that online reviews constantly get more positive, it can also be presumed that this is resembled in the service aspects as well as in the question of whether a specific product or service is recommended, where the percentage of customers recommending the product or service might also be increased. Thus, as both variables can be assumed to increase, realistically, even in case of rating inflation, the observed relationships can be assumed to hold.

Finally, we recognize that our study analyzes a sample of airline reviews and thus, the proposed methodology of determining aspect-oriented sentiment is tailored to the aspects determining the decision to recommend a specific airline. Consequently, if the methodology is to be applied to services other than those were not deemed relevant in the context of airline reviews. Nevertheless, as shown in this study, the proposed methodology to develop word lists related to specific service aspects leads to valuable measures of aspect-oriented sentiment and can thus also be followed within these contexts.

## 6. Conclusion

Within this study, we investigate whether user-generated content in form of online reviews can be leveraged to explain and predict the recommendation decision. Building upon the accessibility-diagnosticity model and the multiple pathway anchoring and adjustment model, we argue that the consumer recommendation of service is a collective expression of the sentiments regarding distinct service aspects, and emphasized by particularly those aspects that are perceived as salient during the service experience. Based on this rationale, we conduct explanatory and predictive analyses in order to analyze the drivers of the recommendation decision.

## ACCEPTED MANUSCRIPT

We find that the overall sentiment expressed in the review is significantly related to the question of whether a reviewer actually recommends a specific service. When disentangling the overall sentiment to the sentiment expressed towards the different service aspects, we show that aspect-related sentiment on core as well as augmented service aspects influences the recommendation decision as well and thus provides valuable information regarding the service dimensions. By means of a predictive analysis, we show that a bag-of-words model is best for predicting consumer recommendations with high accuracy. Furthermore, we show that the sentiment-related variables extracted from the review are valuable for providing transparent predictions of the recommendation decision. Finally, we also observe that the specific business model has an impact on explaining and predicting consumer recommendations.

Through this study, we contribute to the body of knowledge in several ways. First, we contribute to the literature explaining the recommendation decision by disentangling the recommendation of airlines: we show that the different core and augmented service-aspects offered by the airline are elaborated upon and evaluated in the service review and that the recommendation is driven by these as . We also contribute to the literature on service or product reviews which has so far mostly focused on the perceived helpfulness as well as on sales impact. With this study, we extend the previous understanding of such user generated content by focusing on the service recommendation expressed within the online review. Finally, we propose a novel approach to disentangle the overall sentiment expressed in the review and to take into account different aspects of a product or service.

The study allows stakeholders in the tourism ecosystem, particularly those related to airline services, to leverage the power of user generated content in the form of online reviews. In that regard, this study is highly relevant for practitioners. First, the predictive models proposed within this study can be used to classify online reviews without a specific indication of whether a service is recommended or not. Such a feature is very important for corporations that want to calculate a promoter score. Furthermore, this methodology enables corporations to take into account the opinions of a larger number of consumers than in case of directly contacting a panel of (potential) customers. The developed word lists can be used in order to automatically detect contents and related sentiments within online reviews. In that respect, our research allows suppliers of tourism related services to utilize machine learning algorithms to gain insights into user evaluations hidden in large amounts of unstructured, user-generated content. Additionally, the proposed methodology can also be used in order to provide decision support to consumers during their purchase process.

Finally, as shown by the explanatory analysis, sentiment related to different service aspects also significantly influences the recommendation decision. Consequently, the proposed sentiment indicators are also valuable and can be used in performance dashboards to show the specific customer evaluation of specific service aspects. This is also important having in mind the price, intangibility, emotional involvement and the risks associated with tourism related services (Tilly et al., 2015) and thus satisfies the demand of travelers for risk reducing recommender systems (Buhalis & Amaranggana, 2015).

This study provides several avenues for further research: As the current study is focused on the recommendations of airlines, other areas of the tourism industry can be taken into account to further disentangle the recommendation decision. Furthermore, as the specific sentiment indicators are also relevant on a standalone basis, a future design-oriented study could evaluate the specific configuration of an appropriate performance dashboard for both consumers and suppliers of tourism related services. Further research may also investigate alternative text analysis methods based on topic detection and clustering to improve upon the service aspect identification. Finally, future research might analyze the question of whether survey-based promoter scores and scores based on textual analysis change in tandem or whether one of these measures can be used as an early indicator for changes in consumer perceptions.

## References

Aksoy, S., Atilgan, E., & Akinci, S. (2003). Airline services marketing by domestic and foreign firms: differences from the customers’ viewpoint. Journal of Air Transport Management, 9(6), 343–351.

Anderson, S., Pearo, L. K., & Widener, S. K. (2008). Drivers of service satisfaction linking customer satisfaction to the service concept and customer characteristics. Journal of service Research, 10(4), 365–381.

De Bruyn A., Liechty, J. C., Huizingh, E. & Lilien, G. L. (2008). Offering Online Recommendations with Minimum Customer Input Through Conjoint-Based Decision Aids. Marketing Science, 27(3), 443–460.

Boeing. (2016). Airline strategies and business models. Available online: http://www.boeing.com/ commercial/market/long-term-market/airline-strategies-and-business-models/ (accessed: 09/26/2016),

Buhalis, D., & Amaranggana, A. (2015). Smart Tourism Destinations Enhancing Tourism Experience Through Personalisation of Services. Information and Communication Technologies in Tourism 2015, 377–389.

Chen, F.-Y., & Chang, Y.-H. (2005). Examining airline service quality from a process perspective. Journal of Air Transport Management, 11(2), 79–87.

Chevalier, J. A., & Mayzlin, D. (2006). The Effect of Word of Mouth on Sales: Online Book Reviews. Journal of Marketing Research, 43(3), 345–354.

Chung, N., Han, H., & Koo, C. (2015). Adoption of travel information in user-generated content on social media: the moderating effect of social presence. Behaviour & Information Technology, 34(9), 902–919.

Cohen, J. B., & Reed, A. (2006). A multiple pathway anchoring and adjustment (MPAA) model of attitude generation and recruitment. Journal of Consumer Research, 33(1), 1–15.

Dorner, V., Ivanova, O., & Scholz, M. (2013). Think Twice Before You Buy! How Recommendations Affect Three-Stage Purchase Decision Processes. ICIS 2013 Proceedings,

Feldman, J., & Lynch, J. (1988). Self-Generated Validity and Other Effects of Measurement on Belief, Attitude, Intention, and Behavior. Journal of Applied Psychology, 73(3), 421–435.

Feldman, R. (2013). Techniques and Applications for Sentiment Analysis. Comm. of the ACM, 56(4), 82–89.

Feldman, R., & Sanger, J. (2007). The text mining handbook: advanced approaches in analyzing unstructured data: Cambridge University Press.

Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examining the Relationship Between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets. Information Systems Research, 19(3), 291–313.

Fuller, C. M., Biros, D. P., & Wilson, R. L. (2009). Decision support for determining veracity via linguisticbased cues. Wireless in the Healthcare, 46(3), 695–703.

Ghose, A., & Ipeirotis, P. G. (2011). Estimating the Helpfulness and Economic Impact of Product Reviews: Mining Text and Reviewer Characteristics. IEEE Trans. on Knowledge and Data Eng., 23(10), 1498–1512.

Gilbert, D., & Wong, R. K. C. (2003). Passenger expectations and airline services: a Hong Kong based study. Tourism Management, 24(5), 519–532.

Gillen, D., & Lall, A. (2004). Competitive advantage of low-cost carriers: some implications for airports. Journal of Air Transport Management, 10(1), 41–50.

Groth, S. S., Siering, M., & Gomber, P. (2014). How to Enable Automated Trading Engines to Cope with News-Related Liquidity Shocks? Extracting Signals from Unstructured Data. Decision Support Systems, 62, 32–42.

Haan, E. de, Verhoef, P. C., & Wiesel, T. (2015). The predictive ability of different customer feedback metrics for retention. International Journal of Research in Marketing, 32(2), 195–206.

Han, J., & Kamber, M. (2006). Data mining: Concepts and techniques (2nd ed.). San Francisco: Elsevier; Morgan Kaufmann.

He, J., Liu, H., & Xiong, H. (2016). SocoTraveler: Travel-package recommendations leveraging social influence of different relationship types. Information & Management, 53(8), 934–950.

Hennig-Thurau, T., Gwinner, K. P., Walsh, G., & Gremler, D. D. (2004). Electronic word-of-mouth via consumer-opinion platforms: What motivates consumers to articulate themselves on the Internet? Journal of Interactive Marketing, 18(1), 38–52.

Hotho, A., Nürnberger, A., & Paaß, G. (2005). A Brief Survey of Text Mining. GLDV Journal for Computational Linguistics, 20(1), 19–62.

Hsu, C. W., Chang, C. C., & Lin, C. J. (2003). A practical guide to support vector classification. National Taiwan University, http://www.csie.ntu.edu.tw/\~cjlin/papers/guide/guide.pdf (accessed on 10/16/2011).

Hu, M., & Liu, B. (2004). Mining and Summarizing Customer Reviews. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Seattle, Washington, USA,

Huang, L., Tan, C.-H., Ke, W., & Wei, K.-K. (2014). Do we order product review information display? How? Information & Management, 51(7), 883–894.

Jang, S., Prasad, A., & Ratchford, B. (2012). How consumers use product reviews in the purchase decision process. Marketing Letters, 23(3), 825-838.

Jeong, H.-J., & Koo, D.-M. (2015). Combined effects of valence and attributes of e-WOM on consumer judgment for message and product: The moderating effect of brand community type. Internet Research, 25(1), 2–29.

Khan, S. (2011). How Philips Uses Net Promoter Scores to Understand Customers. Harvard Business Review Online, https://hbr.org/2011/05/how-philips-uses-net-promoter (accessed on 2016/05/28),

Kohavi, R. (1995). A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection. Proceedings of the International Joint Conference on Artificial Intelligence, Montreal, Quebec, Canada, 14(2).

Korfiatis, N., García-Bariocanal, E., & Sánchez-Alonso, S. (2012). Evaluating content quality and helpfulness of online product reviews: The interplay of review helpfulness vs. review content. Electronic Commerce Research and Applications, 11(3), 205–217.

Kotsiantis, S. B. (2007). Supervised Machine Learning: A Review of Classification Techniques. Informatica, 31(3), 249–268.

Kuan, K. K., Hui, K.-L., Prasarnphanich, P., & Lai, H.-Y. (2015). What Makes a Review Voted? An Empirical Investigation of Review Voting in Online Review Systems. Journal of the Association for Information Systems, 16(1), 48–71.

Kwark, Y., Chen, J., & Raghunathan, S. (2014). Online product reviews: Implications for retailers and competing manufacturers. Information Systems Research, 25(1), 93–110.

Langley, P., Iba, W., & Thompson, K. (1992). An analysis of Bayesian classifiers. Proceedings of the Tenth National Conference on Artificial Intelligence, Seattle, WA,

Lewis, D. (1992). Representation and Learning in Information Retrieval: Dissertation, University of Massachusetts.

Loughran, T., & McDonald, B. (2011). When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks. The Journal of Finance, 66(1), 35–65.

Luo, C., Luo, X., Xu, Y., Warkentin, M., & Sia, C. L. (2015). Examining the moderating role of sense of membership in online review evaluations. Information & Management, 52(3), 305–316.

Lynch, J. G. (2006). Accessibility-diagnosticity and the multiple pathway anchoring and adjustment model. Journal of Consumer Research, 33(1), 25–27.

Lynch Jr, John G, Marmorstein, H., & Weigold, M. F. (1988). Choices from sets including remembered brands: Use of recalled attributes and prior overall evaluations. Journal of Consumer Research, 169–184.

Marsden, P., Samson, A., & Upton, N. (2005). Advocacy drives growth. Brand strategy, (198), 45–47.

Miner, G. (2012). Practical text mining and statistical analysis for non-structured text data applications: Academic Press.

Mitchell, T. (1997). Machine learning. London: McGraw-Hill.

Morgan, N. A., & Rego, L. L. (2006). The value of different customer satisfaction and loyalty metrics in predicting business performance. Marketing Science, 25(5), 426–439.

Mudambi, S. M., & Schuff, D. (2010). What Makes a Helpful Online Review? A Study of Customer Reviews on amazon.com. MIS Quarterly, 34(1), 185–200.

Ngo-Ye, T. L., & Sinha, A. P. (2014). The influence of reviewer engagement characteristics on online review helpfulness: A text regression model. Decision Support Systems, 61, 47–58.

Nisbet, R., Elder, J. F., & Miner, G. (2009). Handbook of statistical analysis and data mining applications. Amsterdam, Boston: Academic Press/Elsevier.

O’Connell, J. F., & Williams, G. (2005). Passengers’ perceptions of low cost airlines and full service carriers: A case study involving Ryanair, Aer Lingus, Air Asia and Malaysia Airlines. Journal of Air Transport Management, 11(4), 259–272.

Ozment, J., & Morash, E. A. (1994). The augmented service offering for perceived and actual service quality. Journal of the Academy of Marketing Science, 22(4), 352–363.

Pang, B., & Lee, L. (2008). Opinion Mining and Sentiment Analysis. Foundations and Trends in Information Retrieval, 2(1-2), 1–135.

Popescu, A.-M., & Etzioni, O. (2007). Extracting product features and opinions from reviews. Natural language processing and text mining, 9–28.

Qi, J., Zhang, Z., Jeon, S., & Zhou, Y. (2016). Mining customer requirements from online reviews: A product improvement perspective. Information & Management, 53(8), 951–963.

Ravald, A., & Grönroos, C. (1996). The value concept and relationship marketing. European Journal of Marketing, 30(2), 19–30.

Reichheld, F. F. (2003). The one number you need to grow. Harvard business review, 81(12), 46–55.

Rhee, H. T., & Yang, S.-B. (2015). How does hotel attribute importance vary among different travelers? An exploratory case study based on a conjoint analysis. Electronic Markets, 25(3), 211–226.

Schindler, R. M., & Bickart, B. (2012). Perceived helpfulness of online consumer reviews: The role of message content and style. Journal of Consumer Behaviour, 11(3), 234–243.

Siering, M., & Muntermann, J. (2013a). How to Identify Tomorrow's Most Active Social Commerce Contributors? Inviting Starlets to the Reviewer Hall of Fame. Proceedings of the 34th International Conference on Information Systems, Milan, Italy,

Siering, M., & Muntermann, J. (2013b). What Drives the Helpfulness of Online Product Reviews? From Stars to Facts and Emotions. Proc. of the 11th International Conference on Wirtschaftsinformatik, Leipzig, Germany,

Sotiriadis, M. D., & van Zyl, C. (2013). Electronic word-of-mouth and online reviews in tourism services: the

Sparks, B. A., Perkins, H. E., & Buckley, R. (2013). Online travel reviews as persuasive communication: The effects of content type, source, and certification logos on consumer behavior. Tourism Management, 39, 1–9.

Stone, P. J., Dunphy, D. C., & Smith, M. S. (1966). The General Inquirer: A Computer Approach to Content Analysis. Cambridge, MA: MIT Press.

Tetlock, P. C., Saar-Tsechansky, M., & Macskassy, S. (2008). More Than Words: Quantifying Language to Measure Firms' Fundamentals. The Journal of Finance, 63(3), 1437–1467.

Tilly, R., Fischbach, K., & Schoder, D. (2015). Mineable or messy? Assessing the quality of macro-level tourism information derived from social media. Electronic Markets, 25(3), 227–241.

Vapnik, V. (1995). The Nature of Statistical Learning Theory. New York, USA: Springer.

Wang, W., & Benbasat, I. (2008). Attributions of Trust in Decision Support Technologies: A Study of Recommendation Agents for E-Commerce. Journal of Management Information Systems, 24(4), 249–273.

Wolff-Mann, E. (2016). When did a 4-star review become a bad review? Time, http://time.com/money/page/online-reviews-trust-fix/ (accessed: 2017/08/15),

Xiang, Z., Schwartz, Z., Gerdes, J. H., & Uysal, M. (2015). What can big data and text analytics tell us about hotel guest experience and satisfaction? International Journal of Hospitality Management, 44, 120–130.

Xiao, B., & Benbasat, I. (2007). E-commerce product recommendation agents: use, characteristics, and impact. MIS Quarterly, 31(1), 137–209.

Ye, Q., Law, R., Gu, B., & Chen, W. (2011). The influence of user-generated content on traveler behavior: An empirical investigation on the effects of e-word-of-mouth to hotel online bookings. Computers in Human Behavior, 27(2), 634–639.

Yin, D., Bond, S. D., & Zhang, H. (2014). Anxious or Angry? Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews. MIS Quarterly, 38(2), 539–560.

# Disentangling Consumer Recommendations: Explaining and Predicting Airline Recommendations based on Online Reviews

## Highlights

 We highlight the importance of analyzing and inferring recommendations expressed in online reviews in the context of tourism services, for prospective consumers as well as for service providers to compute key performance indicators like promoter scores.

 We propose a systematic methodology to identify and extract service aspects expressed in the textual contents of airline reviews, considering both core and augmented service aspects.

 The methodology is also used to extract aspect-oriented sentiment from online reviews.

 We show which factors expressed in online reviews explain the airline recommendation decision, and predict the recommendation decision by means of machine learning techniques.

 We analyze the role of service business models in the explanation and prediction of service

 We outline the importance of aspect-oriented sentiment as key performance indicator in the context of smart tourism
