---
otero_id: 1056
otero_key: "WB2GRRDW"
title: "Kernel-based features for predicting population health indices from geocoded social media data"
authors: "Thin Nguyen; Mark E. Larsen; Bridianne O’Dea; Duc Thanh Nguyen; John Yearwood; Dinh Phung; Svetha Venkatesh; Helen Christensen"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.06.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Kernel-based features for predicting population health indices from geocoded social media data

Thin Nguyen<sup>a,</sup>\*, Mark E. Larsen<sup>b</sup>, Bridianne O’Dea<sup>b</sup>, Duc Thanh Nguyen<sup>a</sup>, John Yearwood<sup>a</sup>, Dinh Phung<sup>a</sup>, Svetha Venkatesh<sup>a</sup>, Helen Christensen<sup>b</sup>

<sup>a</sup> Deakin University, Australia

<sup>b</sup> Black Dog Institute, University of New South Wales, Australia

## A R T I C L E I N F O

Article history: Received 21 September 2016 Received in revised form 27 May 2017 Accepted 30 June 2017 Available online xxxx

Keywords: Spatial decision support system Georeferenced social media Spatial big data Health rankings Twitter Kernel function

## A B S T R A C T

When using tweets to predict population health index, due to the large scale of data, an aggregation of tweets by population has been a popular practice in learning features to characterize the population. This would alleviate the computational cost for extracting features on each individual tweet. On the other hand, much information on the population could be lost as the distribution of textual features of a population could be important for identifying the health index of that population. In addition, there could be relationships between features and those relationships could also convey predictive information of the health index. In this paper, we propose mid-level features namely kernel-based features for prediction of health indices of populations from social media data. The kernel-based features are extracted on the distributions of textual features over population tweets and encode the relationships between individual textual features in a kernel function. We implemented our features using three different kernel functions and applied them for two case studies of population health prediction: across-year prediction and across-county prediction. The kernel-based features were evaluated and compared with existing features on a dataset collected from the Behavioral Risk Factor Surveillance System dataset. Experimental results show that the kernel-based features gained significantly higher prediction performance than existing techniques, by up to 16.3%, sug gesting the potential and applicability of the proposed features in a wide spectrum of applications on data analytics at population levels.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

Local health data are crucial for providing indicators of health outcomes and identifying local needs. However, traditional datasets take several years to collate and to become publicly available. Geocoded social media data can provide an alternative, real-time, reflection of local health trends. Social media has improved health care quality with better communication between patients and clinicians. It offers patients an online platform to record and share health data about themselves through which people might learn eficient ways to deal with their own disease. Through Facebook or Twitter, for example, social media provides a novel channel that quickly disseminates information to a large number of people at no cost [7].

This paper aims to assess whether Twitter data can be used to predict population health indices. These indices are measured based on responses to health-related questions in the Behavioral Risk Factor Surveillance System (BRFSS), annually conducted by the United States Centers for Disease Control and Prevention (CDC). The questions, for years 2013 and 2014, include i) “Would you say that in general your health is excellent, very good, good, fair, or poor?”, ii) “Thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?”, and iii) “Thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?” [2, 3].

When using tweets to predict the health index of a population, textual features are extracted from the tweets and are used in predictive models. The Linguistic Inquiry and Word Count (LIWC) [36], a set of handcrafted features capturing the psychological meaning of

T. Nguyen et al. / Decision Support Systems xxx (2017) xxx–xxx

words, can be used. Alternatively, latent topics can also be used as the features. The topics are not directly observed from corpus data but can be extracted automatically using latent Dirichlet allocation (LDA) [4].

Due to the large scale of data, often in the billions of tweets, aggregating the tweets at a population level is common practice [11, 45]. Textual features are then extracted on the aggregated tweets and the prediction of the health index can be performed using a regression model. This approach alleviates the computational cost of big data analysis. However, at the same time, the aggregation operation loses information on the distribution of the textual data over the population, and such information may be important for identifying the health index of the population. In addition, there could be relationships between features and those relationships could also convey predictive information of the health index. In this paper, we propose novel features which are able to overcome the above issues. In particular, our contributions include

• Kernel-based features. The proposed kernel-based features are mid-level features and constructed on-top of various lowlevel textual features, e.g. latent topics learned using the LDA method [4] or LIWC features [36]. The kernel-based features are formed by taking into account the textual features over the population of tweets and encode the relationships between individual textual features in a kernel function. They capture both the characteristics of the textual information and the correlation between individual textual features at a population level and, hence, fit well with population-level text analytics tasks. We implemented the proposed kernel-based features on two different textual features including the latent topics extracted using the LDA method [4] and LIWC features [36]. We investigated the kernel-based features with three different kernel types including polynomial, Gaussian radial basis function (RBF), and sigmoidal kernel.

• Applications of kernel-based features in social media analytics for population health prediction. We applied the proposed kernel-based features in the prediction of health indices for US counties. Two prediction applications were conducted: across-year prediction and across-county prediction. We adopted the Lasso regression [16] as the predictive model and fed the model with our proposed kernel-based features. We extensively evaluated the performance of the prediction tasks on the CDC dataset for years 2013 and 2014 [2, 3]. In this dataset, counties were ranked according to three criteria: i) self-reported poor health, ii) days of poor physical health, and iii) days of poor mental health. A contemporaneous dataset of 1.96 billion tweets containing latitude and longitude coordinates was collected, and linked to the health data via the Federal Information Processing Standard (FIPS, e.g., Los Angeles County: FIPS code 06037) county code, mapped from latitude and longitude information using the 2013 cartographic boundary shapefiles provided by the US Census Bureau.<sup>1</sup> The data were then partitioned such that 70% of the data were randomly selected for training, and the remaining 30% were used for testing. The Spearman rank correlation coeficient (rho) between the actual health values (from the BRFSS) and estimated health values was used to evaluate prediction performance. Experimental results favorably show the improvement gained by our approach using kernel-based features in comparison to extracting textual features from aggregated tweets, e.g., [11, 45]. The improvement is substantial (up to 16.3%) and consistent over different prediction tasks. These results show the correlation between publicly available health indices and linguistic data extracted from geospatially coded Twitter data. This confirms that the real-time analysis of social media data can provide timely insights into the health of populations.

The remainder of the paper is organized as follows. Section 2 briefly reviews related work. Section 3 presents the proposed kernelbased features. The experiments are presented in Section 4, with the results reported in Section 5.Section 6 concludes the paper and provides remarks.

## 2. Related work

## 2.1. Social media and health care

Social media has been integrated into medical practice and has reshaped health care services in several ways, including (1) Communication: Social media has improved health care quality with better communication between patients and clinicians, either through generic channels such as Facebook or Twitter [7], or via special sites such as PatientsLikeMe<sup>2</sup> for patients or Sermo<sup>3</sup> for clinicians; (2) Health surveillance: Social media can be used to effectively build novel disease surveillance systems that detect, track and respond to infectious diseases, such as in the case of the 2009 H1N1 Influenza [6]; (3) Promotional health: The new media was found to be feasible for effectively promoting healthy behavior, such as weight loss programs [49] or sexual health promotion [50]; and (4) Medical intervention: Social media has been used to treat stress and depression in first-year medical students [17] and deliver an online cognitive-behavioral therapy [26].

## 2.2. Spatial-temporal analytics with social media data

The scale of geotagged social media data enables useful spatial analytics. Firstly, the huge volume of user-generated data points with geotags ensures high quality estimation of geographic densities for a concept, helping to better understanding how the concept is distributed in the regions of interest. The density could be at global scale [28] or local scale [15]. Secondly, spatial big data provides material for geographic clustering, suggesting clusters of data geographically close and having similar characteristics. For example, a majority of Twitter users within a geographic span, such as the geographical dispersion of one’s followers, were found to have geographically local networks [40]. Lastly, large-scale geo-tagged datasets enable spatial reasoning. For example, geo-referenced photos voluntarily posted online help determine spatial correlations, such as between various crimes, or between crimes and number of photos, among regions of interest [39]. All of these analytics helps spatial knowledge discovery, such as in [41], where geotagged Flickr photos and their corresponding votes were utilized to identify the happiest route from A to B, instead of the fastest routes as commonly requested, suggesting Googling for happy maps and supporting urban planning.

The temporal dimension tagged in social media data allows geotemporal analytics. For example, the time-stamp of tweets, along with the locations where the posters are and where the posts are made, inferred from the geotags, provides information of human activity in both space and time. Indeed, they were utilized to discover global mobility patterns [22]. In addition to spatial patterns, such as the inflow-outflow balance of a region, temporal patterns, such as the seasonality of international mobility, were also discovered.

T. Nguyen et al. / Decision Support Systems xxx (2017) xxx–xxx

## 2.3. Volunteered geographic information (VGI) for decision support

Of the user-generated content on the Web, the geographic information voluntarily provided by Internet users, namely volunteered geographic information (VGI), has become pervasive, making each citizen a sensor [19]. The most obvious application of VGI is found in crisis and disaster decision support systems (DSS). For example, VGI has been integrated with wireless sensor networks to develop a spatial decision support system for managing flood risks [23]. The integration showed improvement in coverage of monitored areas. In the same line of research, VGI was utilized in estimation of flood damage, an essential component of disaster management system with focus on response and recovery phases [37]. In addition to disaster managements, other areas also benefit from utilizing VGI information, such as urban planning [54], environmental monitoring [10], land administration [48], or community health monitoring [20].

## 2.4. Twitter for decision-making

Twitter has been considered an ideal data source for decision support for the scale (in the factor of millions), the cost (virtually at no charge), and the information tagged, such as spatial and temporal coordinates [18]. Tagged with geographic information, Twitter has been found in many disaster management systems, including (1) GIS-SM-DDSS (Geographic information system - social media - dynamic decision support system): supporting collective actions for public evacuation in tsunami disasters [1]; (2) TWRsms (Tsunami Warning and Response Social Media System): providing early warning and supporting planning for tsunami disasters [27], rather than supporting responses, as in GIS-SM-DDSS; and (3) SME-DSS (social media-enhanced decision support systems): assessing social responses to social and environmental hazard events [46]. Through volunteered geographic information provided in tweets, several geo-localization techniques were used to identify areas at risk of natural disasters promptly, supporting coordination in emergency responses [34]. Also, by monitoring geotagged tweets, 96% of earthquakes are detected, providing the base for building earthquake reporting systems [43]. In this work, Kalman filtering and particle filtering were used to estimate the trajectory of earthquakes with each Twitter user considered as a sensor.

For business in general, potential customers can be identified from the large number of Twitter users, helping to make better business decisions, such as providing personalized service to prospective customers [31]. Tweets have also been used to estimate movie sales based on comments and reviewers [42]. The results suggest important managerial implications, such as identifying influential users or opinion leaders in the social broadcasting network [29].

For marketing, Twitter has been used as a platform to identify consumer attitudes towards brands, such as the Uber transportation network [38]. This helps marketers uncover prevailing topics and corresponding sentiment tendencies on their products, for example, negative reviews for service and support, and positive reviews for promotion. These findings in turn could result in further decisions, such as improving the negative aspects. Also for marketing, tweets have been used to capture brand awareness and popularity, as well as the route of brands moving on the Web [51]. Furthermore, tweets have been utilized to derive marketing intelligence information, automatically providing decision makers related to market trends for their products [30].

There also exists the use of tweets in building decision support systems in other domains. For example, for journalism, Twitter has been utilized to build “Journalist Decision Support System”,<sup>4</sup> supporting journalists to debunk fake news. In the system, tweets are also geoparsed to help journalists identify where ‘possible eyewitness’events are happening [33]. It has also been evidenced in crime prediction that the performance improves for 19 of 25 crime types when Twitter data is augmented to the standard approach [18]. In the betting industry, the sentiment conveyed in tweets has been found to be a predictor of match outcomes, possibly providing supplemental sources when building automated wagering systems [44].

## 2.5. Tweets as proxy for population health indices

Tweets have been utilized as a sensor in several health care applications, for example, in public health surveillance. Signorini et al. [47] illustrated that information extracted from Twitter can provide a real-time, effective indicator of public sentiment and influenza disease activity. Chunara et al. [9] found that the trend of the 2010 Haitian cholera outbreak derived from tweets was significantly correlated with that of oficial case data. Furthermore, the reports from these studies were available up to two weeks earlier than conventional surveillance reports.

Twitter allows users to geotag their tweets with a precise location, and, although these data are only present in approximately 2% of posts [28], they provide a rich subset of data allowing analysis at the county-level. For example, topics and language styles extracted from tweets by county were claimed to be strong markers of life satisfaction at county level [45]. Language styles of tweets were also found to estimate well several county health statistics, such as obesity or teen birth rates [11]. The same features of tweets were said to be powerful predictors of heart disease mortality across counties [14]. Also, future-orientation, one of the language features, was found to link with county-level HIV prevalence [24].

In these works, due to the large-scale of data, such as 82 million county-mapped tweets in [45], extracting features for each individual tweet would have been computationally expensive. Therefore, the popular practice has been to aggregate tweets by county to reduce the number of documents to be processed from millions to thousands, and hence reducing computational cost. However, much information could be lost by the aggregation operation. In addition, the distribution of the textual data within a county captures the characteristics of that county and thus may be useful for identifying the health indices. We therefore apply a kernel function to our dataset, as described in the following section.

## 3. Kernel-based features

As presented in the introductory section, the distribution of textual features within a county could be informative and predictive for the health index of that county. Moreover, the relationships between textual features may also be important. In this paper, we propose mid-level features encoding the correlation between individual lowlevel textual features via kernel functions. Specifically, let C be a county in which a set of N tweets $\big \{ t _ { 1 } , t _ { 2 } , \dots , t _ { N _ { C } } \big \}$ are collected. Suppose that d different feature types (e.g., latent topics) are used to describe a tweet, i.e., each tweet t is encoded by a set of textual features $\mathbf { v } _ { i } ~ = ~ [ \nu _ { i , 1 } , \nu _ { i , 2 } , \ldots , \nu _ { i , d } ] ~ \in ~ \mathbb { R } ^ { d }$ . We can construct a matrix $M _ { C } \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { N _ { C } }$ as follows,

$$
M _ {C} = \left( \begin{array}{c c c c} v _ {1, 1} & v _ {2, 1} & \dots & v _ {N _ {C}, 1} \\ v _ {1, 2} & v _ {2, 2} & \dots \dots & v _ {N _ {C}, 2} \\ \dots & \dots & \dots & \dots \\ v _ {1, d} & v _ {2, d} & \dots & v _ {N _ {C}, d} \end{array} \right)\tag{1}
$$

The matrix $M _ { C }$ represents the distribution of textual features $\mathbf { v } _ { i }$ over the county C. Based on $M _ { C } ,$ we define a vector $\bar { \textbf { v } } \in \mathbb { R } ^ { d }$ which contains the mean values of feature types $j , j = 1 , 2 , \dotsc , d$ over $N _ { C }$ tweets as follows,

$$
\bar {\mathbf {v}} = [ \bar {v} _ {1}, \bar {v} _ {2}, \dots , \bar {v} _ {d} ] = \left[ \frac {\sum_ {i = 1} ^ {N _ {C}} v _ {i , 1}}{N _ {C}}, \frac {\sum_ {i = 1} ^ {N _ {C}} v _ {i , 2}}{N _ {C}}, \dots , \frac {\sum_ {i = 1} ^ {N _ {C}} v _ {i , d}}{N _ {C}} \right]\tag{2}
$$

We define a centric-normalized matrix $\hat { M } _ { \mathrm { C } }$ which can be obtained by translating $M _ { C }$ by v¯ and normalizing it by $\sqrt { N _ { C } }$ . In particular, we compute

$$
\hat {M} _ {C} = \frac {1}{\sqrt {N _ {C}}} \left(M _ {C} - \bar {\mathbf {v}} ^ {\top} \mathbf {1}\right)\tag{3}
$$

$$
= \left( \begin{array}{c c c c} \frac {v _ {1 , 1} - \bar {v} _ {1}}{\sqrt {N _ {C}}} & \frac {v _ {2 , 1} - \bar {v} _ {1}}{\sqrt {N _ {C}}} & \dots & \frac {v _ {N _ {C} , 1} - \bar {v} _ {1}}{\sqrt {N _ {C}}} \\ \frac {v _ {1 , 2} - \bar {v} _ {2}}{\sqrt {N _ {C}}} & \frac {v _ {2 , 2} - \bar {v} _ {2}}{\sqrt {N _ {C}}} & \dots \dots & \frac {v _ {N _ {C} , 2} - \bar {v} _ {2}}{\sqrt {N _ {C}}} \\ \dots & \dots & \dots & \dots \\ \frac {v _ {1 , d} - \bar {v} _ {d}}{\sqrt {N _ {C}}} & \frac {v _ {2 , d} - \bar {v} _ {d}}{\sqrt {N _ {C}}} & \dots & \frac {v _ {N _ {C} , d} - \bar {v} _ {d}}{\sqrt {N _ {C}}} \end{array} \right)\tag{4}
$$

where $\mathbf { 1 } = [ 1 , 1 , \ldots , 1 ] \in \mathbb { R } ^ { N _ { C } }$

Finally, we define a set of kernel-based features $\begin{array} { r l } { \mathbf { D } _ { C } } & { { } = } \end{array}$ $[ D _ { C , 1 , 2 } , D _ { C , 1 , 3 } , \ldots , D _ { C , d - 1 , d } ] \in \mathbb { R } ^ { \frac { d ( d - 1 ) } { 2 } }$ in which each element $D _ { C , j , k }$ is the result of a kernel function K applied on two rows j and k of $\hat { M } _ { C }$ . In particular, let $\hat { M } _ { C } ( j )$ and ${ \hat { M } } _ { C } ( k )$ respectively denote the j-th and k-th row of M<sup>ˆ</sup> , $D _ { C , j , k }$ is calculated as,

$$
D _ {C, j, k} = K \left(\hat {M} _ {C} (j), \hat {M} _ {C} (k)\right) = \left\langle \Phi \left(\hat {M} _ {C} (j)\right), \Phi \left(\hat {M} _ {C} (k)\right) \right\rangle\tag{5}
$$

where $\Phi ( \mathbf { x } )$ is an implicit function that maps a vector x in a lowdimensional space (e.g., of L dimensions) to a higher (possible infinite) dimensional space and $\langle \cdot , \cdot \rangle$ is the inner product of two vectors.

Note that the kernel-based features D are extracted on $\hat { M } _ { C }$ instead of $M _ { C }$ because $\hat { M } _ { C }$ has been aligned by v¯ and thus captures the variation of features which could be important to encode the characteristics of the textual information at population level. We also note that the normalized factor $\sqrt { N _ { C } }$ is used in $\hat { M } _ { C }$ to compensate the variation of numbers of tweets acrossing counties. In this paper, we investigate three kernel types which have been commonly used. The kernels are defined as follows,

Polynomial kernel

$$
K \left(\hat {M} _ {C} (j), \hat {M} _ {C} (k)\right) = \left\langle \hat {M} _ {C} (j), \hat {M} _ {C} (k) \right\rangle^ {p}\tag{6}
$$

where p is the degree of the kernel. Gaussian radial basis function (RBF) kernel

$$
K \left(\hat {M} _ {C} (j), \hat {M} _ {C} (k)\right) = \exp \left(- \frac {\left\| \hat {M} _ {C} (j) - \hat {M} _ {C} (k) \right\| _ {2} ^ {2}}{2 \sigma^ {2}}\right)\tag{7}
$$

where $\| \cdot \| _ { 2 }$ is the L -norm and s is a user parameter set to 0.1 in our experiments. Sigmoidal kernel

$$
K \left(\hat {M} _ {C} (j), \hat {M} _ {C} (k)\right) = \tanh \left(\left\langle \hat {M} _ {C} (j), \hat {M} _ {C} (k) \right\rangle\right)\tag{8}
$$

where tanh $\begin{array} { r } { \mathfrak { i } ( z ) = \frac { e ^ { z } - e ^ { - z } } { e ^ { z } + e ^ { - z } } } \end{array}$

Using kernels for feature construction holds several advantages. First, if the kernel function K can be represented in the form the inner product of V $\left( \hat { M } _ { C } ( j ) \right)$ and V $\left( \hat { M } _ { C } ( \boldsymbol { k } ) \right)$ , as shown in Eq. (5), the function V is not necessary to be known. Second, instead of working on a high dimensional space , all the computations can be done in a lower dimensional space . As defined in Eq. (5), the feature set $\mathbf { D } _ { C }$ captures both the characteristics of the textual information and the correlation between individual textual features j and k of county C.

Intuitively, kernels can be considered as distance functions measuring the similarity between data points. For example, when the p-degree of a polynomial kernel is 1, the kernel is the dot product of two vectors. When the two vectors are unit vectors, their dot product is the cosine of the angle between them and hence represents their proximity. For RBF kernels, the distance between two data points is expressed in a Gaussian and diminished by the radius parameter s.

With the above advantageous properties, kernel methods have been often used in machine learning in building discriminative classifiers. For example, in two-class support vector machines, one could use kernels for comparing data points with support vectors in a high dimensional space which could be better separated. In this paper, we make use of kernels in constructing mid-level features which capture the pairwise relationships (e.g. distances) between individual low-level textual features in tweets across a population (e.g. county). For example, the polynomial kernel defined in Eq. (6) becomes the covariance of low-level textual features when the $p -$ degree is 1. In other words, kernel-based features are distances and such features may be important to encode latent trends in tweeting of a population.

Although it is not necessary to obtain an explicit definition of the mapping function V, it could be also determined in several specific cases. For example, with the polynomial kernel presented in Eq. (6), it can be shown that V has the form as

$$
\Phi \left(\hat {M} _ {C} (j)\right) = \sqrt {\left(\frac {p !}{r _ {1} ! r _ {2} ! \dots r _ {N _ {C}} !}\right)} \left[ \hat {M} _ {C} (j, 1) \right] ^ {r _ {1}} \left[ \hat {M} _ {C} (j, 2) \right] ^ {r _ {2}} \dots \left[ \hat {M} _ {C} (j, N _ {C}) \right] ^ {r _ {N _ {C}}}
$$

where $r _ { l } \ge 0 , \forall l = 1 , 2 , \hdots , N _ { C }$ and $\begin{array} { r } { \sum _ { l = 1 } ^ { N _ { C } } r _ { l } = p , } \end{array}$ and $\hat { M } _ { C } ( j , l )$ is the element at row j and column l of matrix M<sup>ˆ</sup> .

In addition, as shown in [8], the dimension of the mapping space of a p-degree polynomial kernel working on an N -dimensional space (as each row in $\hat { M } _ { C }$ has $N _ { C }$ elements) will be $\binom { N _ { C } + p - 1 } { p }$ . For example, if we are to process $N _ { C } = 2 0 0$ tweets using a polynomial kernel of $p = 3$ degree, then ${ \mathcal { H } } = \Phi ( { \mathcal { L } } )$ will have 1,353,400 dimensions. It is also noticeable that the mapping space can also have infinite dimensions. For example, as proved in [8], for the RBF kernel, since $K \left( \hat { M } _ { C } ( j ) , \hat { M } _ { C } ( k ) \right) \to 0 \mathrm { a s } \left\| \hat { M } _ { C } ( j ) - \hat { M } _ { C } ( k ) \right\| _ { , } \to \infty ,$ will be an infinite dimensional space. However, irrespective of the high dimensionality of the mapping space ${ \mathcal { H } } ,$ we are still able to perform all the operations, $\mathbf { e . g . }$ , calculating inner products, distances, on the lower dimensional space $\mathcal { L }$ while getting the same effect on without increasing any computations. For example, there would be no computational cost incurred when the degree of the polynomial kernel increases as the main operation with this kernel is the inner product which does not depend on the degree p.

## 4. Experimental setup

In this section, we describe our experimental setup including dataset, textual features on which the proposed kernel-based features are extracted, two conducted case studies, and the computing environment.

Please cite this article as: T. Nguyen et al., Kernel-based features for predicting population health indices from geocoded social media data, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.010

## 4.1. Dataset

## 4.1.1. Tweets

From 7 June 2013 to 14 July 2016, tweets geo-tagged within a bounding box of the USA (−170.0,18.0, −60.0,72.0) were streamed using the Twitter API.<sup>5</sup> This resulted in a corpus of 1,961,536,285 non-re-tweeted tweets, posted by 15,635,491 users, and archived in 5414 gigabytes of storage.

Latitude and longitude information of the location where the tweets were made were mapped to US counties using the 2013 cartographic boundary shapefiles provided by US Census Bureau.<sup>6</sup> Only the tweets for 2013 and 2014 were used in this study, and 768,791,808 tweets were mapped to 3221 US counties and equivalents.

## 4.1.2. County health indices

All data for county-level health indices was drawn from BRFSS [2, 3]. The indices include i) poor mental health days (referred to as “mental health”) –the average number of mentally unhealthy days per month, ii) poor physical health days (referred to as “physical health”) –the average number of physically unhealthy days per month, and iii) self-reported poor or fair health (referred to as “general health”) –the percent of adults that report fair or poor health.

The BRFSS is an ongoing telephone-based population health survey, conducted by the CDC. Survey results are published online annually. At the time of writing, the most recent data available were for the year 2014. As tweet data were available from 2013 onwards, county health indices for 2013 and 2014 were used.

## 4.2. Textual features

We applied our proposed kernel-based features on two textual features: latent topics and language style. Those textual features are often used in the practice of text analytics [13, 32]. We note that compared with raw tweets possibly composing hundreds of thousands of unique words, the latent topics and language style features are more compact and thus would enable large-scale analysis.

## 4.2.1. Latent topics

To extract latent topics, latent Dirichlet allocation [4], a Bayesian probabilistic modeling framework, was used. For the inference part, we implemented Gibbs inference detailed in [21]. We set the number of topics to 80, comparable to the number of language style features. We ran the Gibbs sampling for 5000 samples and used the last Gibbs sample to estimate P(topic — word) - the probability of a topic given a word. We used tweet data for the year 2013 to learn these probabilities. The distribution of topics for an input tweet is computed as:

$$
P (\text { topic } | \text { tweet }) = \sum_ {\text { word } \in \text { topic }} P (\text { topic } | \text { word }) \times P (\text { word } | \text { tweet })\tag{9}
$$

## 4.2.2. Language style

To extract the language style of tweets, we used the LIWC 2015 package [36]. For an input tweet, the package returns 78 psycholinguistic categories, such as linguistic, social, affective, cognitive, perceptual, biological, relativity, time orientations, drives, personal concerns, and informal language.

## 4.3. Case studies

We conducted two case studies for the prediction of health indices: across-year prediction and across-county prediction. As defined in [2, 3], we predicted the three health indices: “mental health”, “physical health”, and “general health”. These three indices are chosen in our study because they are considered as the major health outcomes in surveys and widely used in existing works, e.g. [5, 25]. Fig. 1 shows the two case studies.

(a)  
![](/api/attachments/WB2GRRDW/fulltext/images/10879059f60739bddb6e0d13db04e34b64c3c73447a38d326628fb94da04370d.jpg)

(b)  
![](/api/attachments/WB2GRRDW/fulltext/images/5bf4b3966dbf7ef354e0875f3f4608c8150265951dd2ac3b7fced6fdb1f805a5.jpg)  
Fig. 1. Procedure of deriving county health ranking from tweets and evaluation with oficial ranking.

Linking raw tweets represented by textual features to health indices is performed via a predictive model. In our experiments, linear regression is adopted for the prediction. The model maps input variables, which consists of features, to an output variable, that is a particular CDC health index. In particular, let $y _ { i }$ denote the value of a health index variable Y for an observation unit i (an individual county). Let x be the input (i.e., features) of the unit i. The relationship between $. y _ { i }$ and $x _ { i }$ is modeled as follows,

$$
y _ {i} = \beta_ {0} + \beta^ {T} x _ {i} + e _ {i}\tag{10}
$$

where $e _ { i }$ is an error term.

The regression model can be learned by fitting the coeficient vector $\beta .$ This task is equivalent to minimizing the prediction error and hence can be regularized by a Lasso constraint b $\parallel _ { 1 } < c ,$ , where the threshold c was determined via 5-fold cross validation [16].

Table 1  
Correlation (Spearman’s rho) between the health ranking derived from tweets and CDC ranking (Topics as features). Best results for each prediction case study and health index are highlighted.

<table><tr><td rowspan="2"></td><td colspan="3">Across-year prediction</td><td colspan="3">Across-county prediction</td></tr><tr><td>Mental</td><td>Physical</td><td>General</td><td>Mental</td><td>Physical</td><td>General</td></tr><tr><td>Polynomial (p=1)</td><td>61.2</td><td>65.5</td><td>70.3</td><td>72.7</td><td>68.2</td><td>71.8</td></tr><tr><td>Polynomial (p=2)</td><td>61.2</td><td>65.5</td><td>70.3</td><td>72.8</td><td>68.3</td><td>71.8</td></tr><tr><td>Polynomial (p=3)</td><td>61.3</td><td>65.5</td><td>70.3</td><td>72.8</td><td>68.3</td><td>71.8</td></tr><tr><td>RBF</td><td>59.7</td><td>65.0</td><td>71.2</td><td>75.7</td><td>71.6</td><td>74.1</td></tr><tr><td>Sigmoidal</td><td>61.2</td><td>65.5</td><td>70.3</td><td>72.7</td><td>68.2</td><td>71.8</td></tr><tr><td>Aggregated</td><td>49.3</td><td>49.2</td><td>56.2</td><td>64.0</td><td>55.7</td><td>58.3</td></tr></table>

The across-year prediction model was derived for each health index using the data from all counties in year 2013. In other words, each training data point came from a county at year 2013 and the data of that county in 2014 was used for testing and evaluation.

For the across-county prediction, the data from year 2014 was used for both model training and testing. In this case study, the 3221 counties were randomly sampled into a training group of 2255 counties (70%) and a validation group of 966 counties (30%).

To evaluate and compare feature types, the Spearman rank correlation coeficient between the actual health values from CDC and the values estimated from tweets was adopted as the measure of prediction performance.

## 4.4. Computing environment

To compute the proposed kernel-based features, the latent topics and the LIWC for each tweet have to be extracted and the number of tweets to be handled is up to several hundred millions. To deal with this data volume, we made use of Apache Spark, an emerging cluster computing platform [53]. Spark is shown to perform better than Hadoop [12] in both optimization using gradient descent and interactive analytics, e.g., querying large corpora [52, 53]. The key difference is that while MapReduce of Hadoop is a disk-based system, Spark is an in-memory one. For example, in performing gradient descent, while MapReduce reads the same data from disks repeatedly for every iteration, Spark loads the data once and keeps it in memory for the following iterations [52, 53]. In addition, Spark enables distributed and parallel computations and thus makes the computations eficiently and practically.

In our experiments, a Spark cluster of eight worker nodes was employed. Each node was featured by a dual eight-core Intel® Xeon® E5-2670@2.60 GHz processors, 128 gigabytes of main memory, and CentOS 7.2 operating system.

## 5. Results and comparisons

## 5.1. Results using latent topics

We first evaluated the proposed kernel-based features computed on latent topics in two case studies: across-year prediction and across-county prediction. In particular, we measured the Spearman rank correlation coeficient between the actual health ranking and estimated health ranking when different kernel types were applied on the case studies. The results of different kernel types on acrossyear prediction and across-county prediction case study are reported in Table 1. We also highlight the best results for each prediction case study and health index.

As shown in our experiments, for the across-year prediction case study, the polynomial kernel achieved the best performance when predicting both the mental health and physical health indices. However, the RBF and sigmoidal kernels also show a comparable performance to the polynomial kernel; they also performed best on the prediction of the general and physical health indices, respectively. Fig. 2a visually shows the best performance of the kernels for across-year prediction.

In contrast to the across-year prediction, for the across-county prediction case study, the RBF kernel shows a dominance over other kernel types and on all health indices. Compared with the polynomial and sigmoidal kernels, the RBF kernel consistently improved the performance on all health indices. For example, the RBF kernel improved 3.4% on the prediction accuracy for physical health, in comparison with the sigmoidal kernel (71.6% versus 68.2%). In both case studies, the polynomial kernel achieved near-identical performance for every degree $p ~ \in ~ \{ 1 , 2 , 3 \}$ . The prediction performance of the best kernel-based feature (i.e., the RBF kernel features) for across-county prediction case study is illustrated in Fig. 2b.

## 5.2. Results using linguistic features

We repeated the experiments using LIWC features. In our experiments, the LIWC features are extracted using the software in [36]. Based on the LIWC features, the proposed kernel-based features are applied. Table 2 summarizes the prediction results of applying different kernel types on the LIWC features in across-year prediction and across-county prediction case studies. The best performances for each prediction case and health index are also highlighted.

As shown in Table 2, the sigmoidal kernel consistently outperforms the other two kernels in both prediction case studies and on all health indices. The sigmoidal kernel increased the correlation scores from 0.3% (51.7% versus 51.4% by the polynomial kernel with p = 1 on the prediction of mental health crossing years) to 2.2% (68.8% versus 66.0% by the polynomial kernel with p = 1 on the prediction of general health across years). There was a slight difference in the performance of the polynomial kernel when the degree p varied and the highest correlation was obtained when p = 1 in each case, i.e. the polynomial kernel became the covariance. The prediction performance using the sigmoidal kernel is visualized for both case studies in Fig. 3.

Experimental results also show that on the use of LIWC features, the prediction of general health is more reliable than that of mental health for all the kernel types and in both across-year prediction (about 16.2% on average) and across-county prediction (about 9.3% on average). On the use of LDA topics, similar phenomenon is observed in across-year prediction while, on contradictory, the prediction of mental health surpasses that of general health for all the kernel types in across-county prediction. In general, across-county prediction is more accurate than across-year prediction and this is consistent for both LDA topics and LIWC features and on all health indices. This is probably because there could be major climatic and social events in particular periods of time and those factors may have influenced the social life of the population, which consequently have affected the population health [35].

(a)  
![](/api/attachments/WB2GRRDW/fulltext/images/f50c45bbe0d90d4d9e507d6abb8c56041734d3b5b7666edb1354cae35e5a4229.jpg)  
Mental health index

![](/api/attachments/WB2GRRDW/fulltext/images/75ff6c59aa6868d183222047e1ff51674860e319dbb20808be0d97b0e445a770.jpg)  
Physical health index

![](/api/attachments/WB2GRRDW/fulltext/images/fa8d588bd63ef7bd7b14918b358e1a8f0ebd7c84e235dafa44939baf23c97bd5.jpg)  
General health index

(b)  
![](/api/attachments/WB2GRRDW/fulltext/images/88d407962b9d682e382de9b5926b0f93b8e716e57563ceb7b56986cb1d428333.jpg)  
Mental health index

![](/api/attachments/WB2GRRDW/fulltext/images/4c0b0b359f2002f058aec82aacd6ea5c490bfdcfedf62e1ef721875f9676f84d.jpg)  
Physical health index

![](/api/attachments/WB2GRRDW/fulltext/images/43229ee45a3f25b650924abc807d6772d9e13c5ff15b5cb3200bf7dcc85be3b1.jpg)  
General health index  
Fig. 2. Prediction performance of the three kernels on the latent topic features. Predicted health indices are compared against the ground-truth values from CDC

## 5.3. Comparison

In addition to evaluation of the proposed kernel-based features, we also compared our approach with the conventional approach [11, 45] which aggregates tweets in counties and then extracts latent topics and LIWC features on the aggregated tweets. This kind of features is labeled as “aggregated feature”. The aggregated tweets are formed accordingly with the case studies. For example, in the acrosscounty case, each county is represented by one tweet aggregated from all the tweets in that county made in the year 2014. In the across-year case, the aggregation on a county is applied for the year 2013 to collect the training data and applied for the year 2014 to create the test data.

Tables 1 and 2 show the comparison between our kernel-based features and the aggregated feature obtained from both latent topics and LIWC respectively. As shown in the tables, in overall, our kernelbased features significantly outperform the aggregated feature when different textual feature types are used and in both prediction case studies for the different health indices.

For topics (see Table 1), for across-year prediction, the improvement gained by the proposed kernel-based features over the aggregated feature is up to 16.3% in the prediction of physical health by either the polynomial or sigmoidal kernels (65.5% versus 49.2%). For across-county prediction, the RBF kernel achieved the highest performance in the prediction of physical health (71.6% versus 55.7%).

Correlation (Spearman’s rho) between the health ranking derived from tweets and CDC ranking (Language styles as features). Best results for each prediction case study and health index are highlighted.

<table><tr><td rowspan="2"></td><td colspan="3">Across-year prediction</td><td colspan="3">Across-county prediction</td></tr><tr><td>Mental</td><td>Physical</td><td>General</td><td>Mental</td><td>Physical</td><td>General</td></tr><tr><td>Polynomial (p=1)</td><td>51.4</td><td>55.8</td><td>66.6</td><td>62.5</td><td>64.0</td><td>70.5</td></tr><tr><td>Polynomial (p=2)</td><td>50.8</td><td>55.4</td><td>66.3</td><td>61.7</td><td>63.5</td><td>70.2</td></tr><tr><td>Polynomial (p=3)</td><td>49.9</td><td>54.8</td><td>66.1</td><td>60.7</td><td>62.9</td><td>69.8</td></tr><tr><td>RBF</td><td>49.8</td><td>55.3</td><td>66.0</td><td>60.7</td><td>63.3</td><td>70.3</td></tr><tr><td>Sigmoidal</td><td>51.7</td><td>57.0</td><td>68.8</td><td>64.3</td><td>64.9</td><td>71.9</td></tr><tr><td>Aggregated</td><td>48.4</td><td>50.6</td><td>65.2</td><td>56.3</td><td>60.2</td><td>69.5</td></tr></table>

Please cite this article as: T. Nguyen et al., Kernel-based features for predicting population health indices from geocoded social media data, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.010

Mental health index

(a)  
![](/api/attachments/WB2GRRDW/fulltext/images/9f4802438e24119a006f009d2886bd39c6e82dfda403e15017dacb754c34b7a7.jpg)

![](/api/attachments/WB2GRRDW/fulltext/images/80cd889745f06f65e78a3f5d560b62df08d439f66d885b198e1a13d570ca42b8.jpg)  
Physical health index

![](/api/attachments/WB2GRRDW/fulltext/images/e0dd025e254804e2174acdbe6d200a50e9c3e3b31ca8deab4c29b6063589a94b.jpg)  
General health index

(b)  
![](/api/attachments/WB2GRRDW/fulltext/images/021a8f88122b035b3e9e0eff74811587529435cbb69b800a9e21ae8185e7b60a.jpg)  
Mental health index

![](/api/attachments/WB2GRRDW/fulltext/images/4292e4eecd2e703a8208d590c2b5d0b67b7385664a43ffb9189183193cc0f80f.jpg)  
Physical health index

![](/api/attachments/WB2GRRDW/fulltext/images/cbad6b65bc5c6b06bac97c0e2719862b55702bf217594f6f34a5cbddfffc6148.jpg)  
General health index  
Fig. 3. Prediction performance of sigmoidal kernel on the LIWC features. Predicted health indices are compared against the ground-truth values from CDC

For language styles, the sigmoidal kernel gained the best improvement over the aggregated feature in all the prediction case studies and health indices (see the last two rows in Table 2). The largest difference is 8% in the prediction of mental health across counties (64.3% versus 56.3%).

## 6. Conclusion

This paper proposes kernel-based features for prediction of population health indices. The proposed kernel-based features are formed by considering the distributions of textual features over the population of tweets and encoding the relationships between individual textual features in a kernel function. The kernel-based features are applied on-top of textual features and thus present in mid-level of description and able to capture the characteristics in the corpus data of populations and communities.

We evaluated the kernel-based features with various textual features, kernel types, and on two case studies: health index prediction crossing years and crossing counties and on a big dataset of hundred millions geospatially coded tweets. Experimental results show that the use of kernel-based features significantly outperforms (up to 16.3%) the conventional approach of extracting features by aggregating tweets at population level. This suggests the potential and applicability of the proposed features in a wide spectrum of applications requiring data analytics at population levels.

Although both LDA and LIWC have been adopted widely as standard ways in social media data analysis, the topics learned by the LDA and linguistic style features extracted by the LIWC may not be meaningful and/or well related to health issues. We consider finding health-related tweets as our future work.

## References

[1] F. Ai, L.K. Comfort, Y. Dong, T. Znati, A dynamic decision support system based on geographical information and mobile social networks: a model for tsunami risk mitigation in Padang, Indonesia, Saf. Sci. 90 (2016) 62–74.

[2] Behavioral Risk Factor Surveillance System, 2013 Behavioral Risk Factor Surveillance System Questionnaire, 2012, December. http://bit.ly/2aF9ujO, retrieved May 2016.

[3] Behavioral Risk Factor Surveillance System, 2014 Behavioral Risk Factor Surveillance System Questionnaire, 2013, December. http://bit.ly/2aJOXIl, retrieved May 2016.

[4] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent Dirichlet allocation, J. Mach. Learn. Res. 3 (2003) 993–1022.

[5] D.W. Brown, L.S. Balluz, G.W. Heath, D.G. Moriarty, E.S. Ford, W.H. Giles, A.H. Mokdad, Associations between recommended levels of physical activity and health-related quality of life: findings from the 2001 behavioral risk factor surveillance system (BRFSS) survey, Prev. Med. 37 (5) (2003) 520–528.

[6] J.S. Brownstein, C.C. Freifeld, E.H. Chan, M. Keller, A.L. Sonricker, S.R. Mekaru, D.L. Buckeridge, Information technology and global surveillance of cases of 2009 h1n1 influenza., N. Engl. J. Med. 362 (18) (2010) 1731–1735.

[7] S.S. Bull, L.T. Breslin, E.E. Wright, S.R. Black, D. Levine, J.S. Santelli, Case study: an ethics case study of HIV prevention research on facebook: the just/us study, J. Pediatr. Psychol. 36 (10) (2011) 1082–1092.

[8] J.C.B. Christopher, A tutorial on support vector machines for pattern recognition, Data Min. Knowl. Disc. 2 (2) (1998) 121–167.

[9] R. Chunara, J.R. Andrews, J.S. Brownstein, Social and news media enable estimation of epidemiological patterns early in the 2010 Haitian cholera outbreak, Am. J. Trop. Med. Hyg. 86 (1) (2012) 39–45.

[10] J.P. Connors, S. Lei, M. Kelly, Citizen Science in the age of neogeography utilizing volunteered geographic information for environmental monitoring, Ann. Assoc. Am. Geogr. 102 (6) (2012) 1267–1289.

[11] A. Culotta, Estimating county health statistics with Twitter, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM. 2014, pp. 1335–1344.

[12] J. Dean, S. Ghemawat, Mapreduce: simplified data processing on large clusters, Commun. ACM 51 (1) (2008) 107–113.

[13] A. Duric, F. Song, Feature selection for sentiment analysis based on content and syntax models, Decis. Support. Syst. 53 (4) (2012) 704–711.

[14] J.C. Eichstaedt, H.A. Schwartz, M.L. Kern, G. Park, D.R. Labarthe, R.M. Merchant, S. Jha, M. Agrawal, L.A. Dziurzynski, M. Sap, Psychological language on Twitter predicts county-level heart disease mortality, Psychol. Sci. 26 (2) (2015) 159–169.

[15] U. França, H. Sayama, C. McSwiggen, R. Daneshvar, Y. Bar-Yam, Visualizing the ‘Heartbeat’ of a City with Tweets, Complexity, 2015.

[17] D.R. George, C. Dellasega, M.M. Whitehead, A. Bordon, Facebook-based stress management resources for first-year medical students A multi-method evaluation, Comput. Hum. Behav. 29 (3) (2013) 559–562.

[18] S.G. Matthew, Predicting crime using Twitter and kernel density estimation, Decis. Support. Syst. 61 (2014) 115–125.

[19] F.G. Michael, Citizens as sensors: the world of volunteered geography, Geo J. 69 (4) (2007) 211–221.

[20] G.P. Grifin, J. Jiao, Where does bicycling for health happen? Analysing volunteered geographic information through place and plexus, J. Trans. Health 2 (2) (2015) 238–247.

[21] T.L. Grifiths, M. Steyvers, Finding scientific topics, Proc. Natl. Acad. Sci. 101 (90001) (2004) 5228–5235.

[22] B. Hawelka, I. Sitko, E. Beinat, S. Sobolevsky, P. Kazakopoulos, C. Ratti, Geolocated Twitter as proxy for global mobility patterns, Cartogr. Geogr. Inf. Sci. 41 (3) (2014) 260–271.

[23] F.E. Horita, J.P. de Albuquerque, L.C. Degrossi, E.M. Mendiondo, J. Ueyama, Development of a spatial decision support system for flood risk management in Brazil that combines volunteered geographic information with wireless sensor networks, Comput. Geosci. 80 (2015) 84–94.

[24] M.E. Ireland, H.A. Schwartz, Q. Chen, L.H. Ungar, D. Albarracín, Futureoriented Tweets predict lower county-level HIV prevalence in the United States, Health Psychol. 34 (S) (2015) 1252.

[25] H. Jia, P. Muennig, E.I. Lubetkin, M.R. Gold, Predicting geographical variations in behavioural risk factors: an analysis of physical and mental healthy days, J. Epidemiol. Community Health 58 (2) (2004) 150–155.

[26] D. Kessler, G. Lewis, S. Kaur, N. Wiles, M. King, S. Weich, D.J. Sharp, R. Araya, S. Hollinghurst, T.J. Peters, Therapist-delivered Internet psychotherapy for depression in primary care: a randomised controlled trial, Lancet 374 (9690) (2009) 628–634.

[27] P.M. Landwehr, W. Wei, M. Kowalchuck, K.M. Carley, Using tweets to support disaster planning, warning and response, Saf. Sci. 90 (2016) 33–47.

[28] K. Leetaru, S. Wang, G. Cao, A. Padmanabhan, E. Shook, Mapping the global twitter heartbeat: the geography of Twitter, First Monday 18 (5). (2013)

[29] F. Li, T.C. Du, Listen to me - evaluating the influence of micro-blogs, Decis. Support. Syst. 62 (2014) 119–130.

[30] Y.-M. Li, T.-Y. Li, Deriving market intelligence from microblogs, Decis. Support. Syst. 55 (1) (2013) 206–217.

[31] S.L. Lo, R. Chiong, D. Cornforth, Ranking of high-value social audiences on twitter, Decis. Support. Syst. 85 (2016) 34–48.

[32] A. McCallum, A. Corrada-Emmanuel, X. Wang, Topic and role discovery in social networks, Proceedings of the International Joint Conference on Artificial Intelligence, 2005. pp. 786–791.

[33] E.M. Stuart, V. Krivcovs, Geoparsing and geosemantics for social media: spatio-temporal grounding of content propagating rumours to support trust and veracity analysis during breaking news, ACM Trans. Inf. Syst. 34 (3) (2016) 1–27.

[34] S.E. Middleton, L. Middleton, S. Modafferi, Real-time crisis mapping of natural disasters using social media, IEEE Intell. Syst. 29 (2) (2014) 9–17.

[35] D.G. Moriarty, M.M. Zack, R. Kobau, The Centers for Disease Control and Prevention’s healthy days measures-population tracking of perceived physical and mental health over time, Health Qual. Life Outcomes 1 (1) (2003) 37.

[36] J.W. Pennebaker, R.J. Booth, R.L. Boyd, M.E. Francis, Linguistic Inquiry and Word Count: LIWC 2015 [Computer Software], Pennebaker Conglomerates Inc.. 2015.

[37] K. Poser, D. Dransch, Volunteered geographic information for disaster management with application to rapid flood damage estimation, Geomatica 64 (1) (2010) 89–98.

[38] D.E. Pournarakis, D.N. Sotiropoulos, G.M. Giaglis, A computational model for mining consumer perceptions in social media, Decis. Support. Syst. 93 (2017) 98–110.

[39] D. Quercia, L.M. Aiello, R. Schifanella, A. Davies, The digital life of walkable streets, Proceedings of the International Conference on World Wide Web, 2015 pp. 875–884.

[40] D. Quercia, L. Capra, J. Crowcroft, The social world of Twitter: topics, geography, and emotions, Proceedings of the International AAAI Conference on Weblog and Social Media, vol. 12, 2012. pp. 298–305

[41] D. Quercia, R. Schifanella, L.M. Aiello, The shortest path to happiness: recommending beautiful, quiet, and happy routes in the city, Proceedings of the ACM Conference on Hypertext and Social Media 2014, pp. 116–125.

[42] H. Rui, Y. Liu, A. Whinston, Whose and what chatter matters? The effect of tweets on movie sales, Decis. Support. Syst. 55 (4) (2013) 863–870.

[43] T. Sakaki, M. Okazaki, Y. Matsuo, Earthquake shakes Twitter users: real– time event detection by social sensors, Proceedings of the 19th International Conference on World Wide Web, 2010. pp. 851–860

[44] R.P. Schumaker, A. Tomasz Jarmoszko, C.S. Labedz, Predicting wins and spread in the Premier League using a sentiment analysis of Twitter, Decis. Support. Syst. 88 (2016) 76–84

[45] H.A. Schwartz, J.C. Eichstaedt, M.L. Kern, L. Dziurzynski, R.E. Lucas, M. Agrawal, G.J. Park, S.K. Lakshmikanth, S. Jha, M.E. Seligman, L. Ungar, Characterizing geo graphic variation in well-being using Tweets, Proceedings of the International AAAI Conference on Weblogs and Social Media, 2013. pp. 583–591.

[46] E. Shook, V.K. Turner, The socio-environmental data explorer (SEDE): a social media-enhanced decision support system to explore risk perception to hazard events, Cartogr. Geogr. Inf. Sci. 43 (5) (2016) 427–441.

[47] A. Signorini, A.M. Segre, P.M. Polgreen, The use of Twitter to track levels of disease activity and public concern in the US during the influenza A H1N1 pandemic, PLoS ONE 6 (5) (2011) e19467.

[48] D.N. Siriba, S. Dalyot, Adoption of volunteered geographic information into the formal land administration system in Kenya, Land Use Policy 63 (2017) 279–287.

[49] D.F. Tate, R.R. Wing, R.A. Winett, Using Internet technology to deliver a behavioral weight loss program, J. Am. Med. Assoc. 285 (9) (2001) 1172–1177.

[50] H.J. Veale, R. Sacks-Davis, E.R. Weaver, A.E. Pedrana, M.A. Stoové, M.E. Hellard, The use of social networking platforms for sexual health promotion: identifying key strategies for successful user engagement, BMC Publ. Health 15 (1) (2015) 85–96.

[51] A.H. Zadeh, R. Sharda, Modeling brand post popularity dynamics in online social networks, Decis. Support. Syst. 65 (2014) 59–68.

[52] M. Zaharia, M. Chowdhury, T. Das, A. Dave, J. Ma, M. Mccauley, M. Franklin, S. Shenker, I. Stoica, Fast and Interactive Analytics over Hadoop Data with Spark. ;login:, 37 (4). 2012, 45–51.

[53] M. Zaharia, M. Chowdhury, M.J. Franklin, S. Shenker, I.S. Spark, Cluster comput ing with working sets, Proceedings of the USENIX Conference on Hot Topics in Cloud Computing, 2010. pp. 10.

[54] X. Zhou L. Zhang Crowdsourcing functions of the living city from Twitter and Foursquare data, Cartogr. Geogr. Inf. Sci. 43 (5) (2016) 393–404.

Thin Nguyen is a research scientist in the Centre for Pattern Recognition and Data Analytics at Deakin University, Australia. He received his PhD from Curtin University Australia in 2012 in the area of social media analysis and machine learning. His broad research interests lie in data analytics, pattern recognition, affective understanding and web-scale analysis. In particular, his research work has focused on sentiment anal ysis, personalisation, crowdsourcing in social media and medical Internet research. His current research topic is viewing the Web as a sensing platform and as a surrogate to develop innovative and novel ways to monitor and predict disease outcomes. One example is to exploit population level web search activity behaviour to construct new computational methods to serve as a proxy for chronic disease risk.

Mark Larsen is a Research Fellow at the Black Dog Institute. He completed his DPhil in Biomedical Engineering at the University of Oxford, and has undertaken postdoctoral research at Oxford and Imperial College London in mobile health for condition management and treatment optimisation. His research interests include the develop ment of novel technology enabled interventions, which he is currently working on in the context of mental health and suicide prevention. His research explores the ways in which technology can deliver effective mental health interventions to reduce the risk of suicide amongst young people, particularly among those that have made a previous attempt.

Bridianne O’Dea is a Postdoctoral Research Fellow at the Black Dog Institute. She completed her PhD in Health Sciences at the University of Sydney in 2013 after com pleting an honours degree in e-mental health. Her PhD examined the relationship between social networking sites and emotional wellbeing in early adolescents. Her current research areas include adolescent depression and anxiety, e-health interventions for mental health, and harnessing social media for suicide prevention, O'Dea has extensive expertise in e-health project management, social media, online service delivery and recently developed expertise in machine learning. Dr O'Dea also has formal research affiliations with the Brain and Mind Research Institute Sydney, and the Norwegian Institute of Public Health, Bergen. She is a current recipient of a Society for Mental Health Research Fellowship for her project on suicide prevention and social media. She is currently a member of five professional associations and regularly reviews manuscripts for a number of different journals.

Duc Thanh Nguyen received his B.Sc. in Information Technology from the University of Science of Ho Chi Minh City, Vietnam in 2002, M.Sc. in Computer Science from the Asian Institute of Technology (AIT), Thailand, in 2005, and Ph.D. degree in Computer Science from the University of Wollongong, Australia, in 2012. Currently, he is a lecturer at Deakin University, Australia. His research interests include Computer Vision and Pattern Recognition, Image Processing, and Machine Learning with specialisation in human and object detection, visual feature extraction, and graphical models for machine learning, variational methods, and statistical pattern recognition.

Professor John Yearwood is Head of the School of Information Technology at Deakin University and was previously Executive Dean, Faculty of Science and Technology, and Director, Centre of Informatics and Applied Optimization at Federation University, Australia. He was instrumental in setting up the Internet Commerce Security Laboratory with Westpac, IBM and the Victorian State Government as a joint industryfocused and data-driven laboratory on cyber security in the financial sector. He has held a number of ARC grants and was a QEII Fellow working on computational narrative and argumentation in decision science. Professor Yearwood’s work in data mining and computational intelligence has led to the development of new machine learning and hybrid learning algorithms for artificial neural networks, as well as new data and text mining and pattern recognition approaches. His work in decision science has developed the use of argumentation structures for the modelling of knowledge and collaborative decision making in complex domains. He has published over 200 journal and refereed conference papers including 2 books. Professor Yearwood is currently a CI on the ARC funded Discovery Project ‘Enhancing and supporting deliberation in multidisciplinary team decision-making’. He is Editor-in-Chief of the Journal of Research & Practice in Information Technology and a reviewer for a large number of journals and competitive research grant programs including the Australian Research Council grant program, the NHMRC grant program, and for the Dutch Government in the assessment of their NWO/ToKeN2000

Dinh Phung is currently a professor in the School of Information Technology, Deakin University, Australia. He obtained a bachelor of computer science with a first class honours and a PhD from Curtin University in 2001 and 2005 respectively. His primary research interest is statistical machine learning, graphical models, Bayesian statistics and their applications in pervasive health, multimedia, social computing and healthcare analytics with an established publication record in these areas. Before joining Deakin, he was the recipient of the Curtin Research Fellowship from Curtin University from 2006 to 2011 and was the recipient of an International Research Fellowship from SRI International in 2005. In 2008, he was invited to Dagstuhl school series on the topic of context modelling and understanding in Germany. He further received the Early Career Research and Development Award and the Curtin Innovation Award from Curtin University in 2010 and 2011 respectively.

Svetha Venkatesh is an Alfred Deakin Professor of Computer Science and Director of Centre for Pattern Recognition and Data Analytics (PRaDA) at Deakin University. She is a Fellow of the Australian Academy of Technological Sciences and Engineering and the International Association of Pattern Recognition. She is on the editorial board of IEEE Transactions on Multimedia and was on the board of ACM Transactions on Multimedia (2008-2011). She is a program member of several international conferences such as ACM Multimedia. Venkatesh has developed frontier technologies in large scale pattern recognition exemplified through more than 300 publications and 9 patents. One start-up company, spun out of these patents is Virtual Observer and based on the paradigm shifting methods that leverages mobile cameras to deliver wide area surveillance solutions. The technology won the Runner up in both the WA Inventor of the year (Early stage) and Global Security Challenge (Asia-Pacific) in 2007. A recent spin-out company is iCetana and is based on novel methods to find anomalies in video data. iCetana won the Broadband Innovation Award at the prestigious Tech23 in 2010. Venkatesh has recently made important contributions to the field of health analytics and won the prestigious Barwon Health Researcher of the Year Award in 2013.

Helen Christensen is the Director of the Black Dog Institute, Professor of Mental Health UNSW Australia, Emeritus Professor ANU, (Honorary) Visiting Research Professor Brain and Mind Research Institute, University of Sydney, Public Policy Fellow Institute of Public Policy, ANU, and NHMRC John Cade Fellow in Mental Health. Helen completed her PhD in Psychology at the UNSW Australia in 1989, and undertook post-doctoral training at St Thomas Hospital, London. Prof Christensen’s research focus is in e-health interventions, particularly prevention and treatment of anxiety, depression and suicide, and she has a demonstrated international track record in cognitive ageing, dementia, pregnancy and cognitive function, suicide epidemiology and advanced methodologies for evaluating scales in anxiety and depression. Areas of interest include the evaluation of online programs for prevention and treatment of mental disorders, integration of new technologies into health care, the development of evidence-informed policy and methods to measure impact and dissemination. She has developed 5 interactive online psychological interventions for depression and anxiety and published over 400 research articles, reviews, book chapters, consumer books and invited contributions to date.
