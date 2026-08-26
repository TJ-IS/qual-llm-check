---
otero_id: 28035
otero_key: "U435FGRW"
title: "When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems"
authors: "Pan Li; Alexander Tuzhilin"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0053"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

Pan Li,<sup>a,</sup>\* Alexander Tuzhilin<sup>b</sup>

<sup>a</sup> Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30332; <sup>b</sup> Stern School of Business, New York University, New York, New York 10012

Contact: pli95@gatech.edu, https://orcid.org/0000-0003-4957-3064 (PL); at2@stern.nyu.edu (AT)

Received: January 27, 2021 Revised: October 27, 2021; August 19, 2022; July 6, 2023 Accepted: August 25, 2023 Published Online in Articles in Advance: October 4, 2023

https://doi.org/10.1287/isre.2021.0053

Copyright: © 2023 INFORMS

Abstract. Variety seekers are those customers who easily get bored with the products they purchased before and, therefore, prefer new and fresh content to expand their horizons. Despite its prevalence, variety-seeking behavior is hardly studied in recommendation applications because of various limitations in existing variety-seeking measures. To fill the research gap, we present a variety-seeking framework in this paper to measure the level of variety-seeking behavior of customers in recommendations based on their consumption records. We validate the effectiveness of our framework through user questionnaire studies conducted at Alibaba, where our variety-seeking measures match well with consumers self-reported levels of their variety-seeking behaviors. Furthermore, we present a recommendation framework that combines the identified variety-seeking levels with unexpected recommender systems in the data mining literature to address consumers’ heterogenous desire for product variety, in which we provide more unexpected product recommendations to variety-seeking consumers and vice versa. Through off-line experiments on three different recommendation scenarios and a large-scale online controlled experiment at a major video-streaming platform, we demonstrate that those models following our recommendation framework significantly increase various business performance metrics and generate tangible economic impact for the company. Our findings lead to important managerial implications to better understand consumers’ variety-seeking behaviors and design recommender systems. As a result, the best-performing model in our proposed frameworks has been deployed by the company to serve all consumers on the video-streaming platform.

History: Ahmed Abbasi, Senior Editor; Gautam Pant, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0053.

Keywords: variety seeking • recommender system • unexpected recommendations

## 1. Introduction

Variety-seeking characterizes consumers’ motives to explore products they have not thought about before when they get tired of their customary purchased products (McAlister and Pessemier 1982). For example, thriller lovers may switch to a romantic comedy after binge-watching multiple thrillers on a Friday night even though their movie interests are predominately confined to thrillers. It constitutes an important dimension of exploratory consumer behavior as varied experiences provide stimulation to reduce user boredom (Faison 1977, Bench and Lench 2019), satisfy innate human curiosity (Raju 1980), and improve consumer satisfaction with their purchases (Ratner et al. 1999). Variety seekers also tend to increase their overall consumption quantity (Read and Loewenstein 1995, Kahn and Wansink 2004) and are more open to promotions (Ailawadi et al. 2001), therefore constituting an important segment of consumers in marketing applications.

Whereas variety seeking is studied extensively in marketing (McAlister and Pessemier 1982, Kahn et al. 1986, Zeithammer and Thomadsen 2013), it is noticeably underexplored in the field of recommender systems because of the following issues. First, existing variety-seeking measures, such as those presented in Kim et al. (2002) and Van Trijp et al. (1996), only operate at the category or brand levels using classic feature-based techniques when computing the differences between consumed products. In contrast, it is crucial for modern recommendation methods (Adomavicius and Tuzhilin 2005, Zhang et al. 2019) to capture the heterogeneity of consumer preferences at the (fine-grained) individual product level, which is typically done in the latent space of product embed dings (Covington et al. 2016). Traditional explicit feature based models are also not scalable to most industrial platforms (Hinton and Salakhutdinov 2006), resulting in high latency and performance downgrades (Covington et al. 2016). Second, whereas the importance of time-varying factors in modeling consumer variety-seeking behaviors is demonstrated in (Alba et al. 1992, Helsen and Schmittlein 1993, Braun and Moe 2013), existing variety-seeking models do not consider the dwell-time information between purchasing actions, leading to significantly less effective measures. Third, existing marketing methods hardly study long-term, variety-seeking properties, such as stationarity, making it difficult to extract and generalize useful behavioral patterns (Gorgoglione et al. 2019).

To address the aforementioned issues and incorporate variety-seeking behaviors into the design of recommender systems, we propose a variety-seeking framework that specifies the class of effective variety-seeking measures of each consumer based on consumption records without requiring explicit consumer feedback on the desire for product variety as is typically done in existing methods (McAlister and Pessemier 1982, Kahn 1995, Baumgartner and Steenkamp 1996). This proposed framework consists of three key components: a distance function between consumed products, a time-decay function specifying how quickly past consumption memories fade, and the stationarity property of variety-seeking behaviors. When we make specific assumptions about the exact nature of these components, we obtain a specific variety-seeking measure for our framework that corresponds to these assumptions. We demonstrate through a questionnaire study that they provide significant performance improvements over existing measures (Givon 1984, Gullo et al. 2019) in modeling consumers’ variety-seeking behaviors.

Furthermore, in this paper, we connect the desire of consumers to seek product variety with the paradigm of unexpected recommender systems (Adamopoulos and Tuzhilin 2014) that simultaneously provide novel and satisfying recommendations to them. Note that the concept of unexpectedness comes from the data-mining literature (Silberschatz and Tuzhilin 1996, Padmanabhan and Tuzhilin 1998) and measures how distant the recommended product is from consumer expectations in a product-centric manner, whereas the concept of variety seeking comes from the marketing literature and measures the consumer propensity to seek significantly different content, especially unexpected products, in a consumer-centric manner. Therefore, we hypothesize in this paper that those two concepts are complementary to each other and need to be properly combined to achieve optimal recommendation performance. In particular, we demonstrate that those consumers with a high level of variety-seeking behavior prefer more unexpected products, and we need to increase the degree of unexpectedness in recommendations accordingly to accommodate their desire and vice versa. Therefore, we propose a recommendation framework that automatically adjusts the degree of unexpectedness in recommendations according to the level of variety seeking of each consumer, which significantly enhances the level of personalization in unexpected recommender systems (Adamopoulos and Tuzhilin 2014). Under the proposed framework, we construct a series of recommendation models with different operationalizations that all lead to significant performance improvements over the existing unexpected recommender systems (Adamopoulos and Tuzhilin 2014, Li and Tuzhilin 2020), which we demonstrate through off-line experiments conducted on three data sets from Yelp, MovieLens, and Alibaba, respectively. Furthermore, we conduct a large-scale online controlled experiment at a major video-streaming platform in China, where we compare the best performing model in our framework with the latest production system. The results demonstrate significant business performance improvements and lead to tangible economic impact for the company in both the short term and long run. Therefore, we bridge the gap between academic research on variety-seeking behaviors and real-world applications in need of fulfilling consumers’ desire for product variety and improving business performance.

In this paper, we make the following research contributions. First, we propose a variety-seeking framework that measures various aspects of the variety-seeking behaviors of consumers in recommender systems. Second, we propose a recommendation framework that combines the concepts of unexpectedness and variety seeking to address the heterogeneous desires of consumers for product variety in recommendations. Finally, we construct multiple variety seeking–based recommendation models fitting these frameworks and demonstrate through a mixture of user questionnaire studies, off-line experiments, and online controlled experiments that these models achieve significant performance improvements over the state-of-the-art solutions described in the marketing and computer science (CS) literature and the latest production system in the company, leading to actionable managerial implications on how to effectively incorporate variety-seeking behaviors into modern recommendation platforms. The significant economic impact of our proposed frameworks has led the company to deploy our best performing variety-seeking model into production, serving consumers on the entire video-streaming platform.

## 2. Literature Review

## 2.1. Variety-Seeking Behavior

Variety seeking represents the consumer behavior of selecting novel and diversified products (Read and Loewenstein 1995, Ratner et al. 1999) to fulfill consumer curi osity (Fiske and Maddi 1961). These behaviors can be driven by self-motivation for stimulation (McAlister and Pessemier 1982, Steenkamp and Baumgartner 1992) or situational factors (Kahn and Isen 1993, Menon and Kahn 1995), such as social desirability (Ratner and Kahn 2002) and compromised personal privacy (Levav and Zhu 2009). In addition, consumers tend to seek more variety in their consumption after being exposed to a sequence of novel products (Xu et al. 2014, Huang and Wyer 2015), leading to increased overall consumption quantity (Read and Loewenstein 1995, Kahn and Wansink 2004) and openness to promotions (Ailawadi et al. 2001). Researchers also study the impact of varietyseeking behaviors in terms of intensity, brand preferences, and consumer surplus (Bawa 1990, Feinberg et al. 1992, Woratschek and Horbel 2006, Seetharaman and Che 2009, Sajeesh and Raju 2010).

Because of all these important benefits, extensive research stems from both marketing and information systems communities around the topic of variety seeking that is related to our work. Specifically, variety-seeking behaviors of blog readers are identified by Singh et al. (2014) as they dynamically switch from reading one set of topics to another. Researchers show that consumers prefer more diversified mobile apps when making download decisions because of their variety-seeking behaviors (Lee et al. 2020). The positive effects of product tags and socially endorsed information on consumers’ perceived serendipity are also studied (Cheng et al. 2017), which encourages consumers to conduct more serendipitous searches. The downstream effects of variety seeking on product demand distribution are also analyzed in Tan et al. (2017) and Fong (2017). In addition, the nonconscious effects of consistency seeking, the opposite of variety seeking, are also explored in sequential consumer decisions (Fishbach et al. 2011).

Meanwhile, variety seeking remains underexplored in recommender systems, resulting in suboptimal performance and repeated types of product recommendations that do not take into account consumers’ desire for product variety. In this paper, we identify several dimensions for measuring the variety-seeking level of each consumer and incorporate such information into the design of unexpected recommender systems. Our method is motivated by the theoretical model of variety seeking in Hoyer and Ridgway (1984), in which researchers hypothesize purchasing exploration to be an interaction between individual-level characteristics (e.g. exploration motivation) and product-level characteristics (e.g. product content or hedonic/utilitarian characteristics; Li et al. 2020a). We extend the theoretical analysis to the application of recommender systems, and we focus on the interaction between the consumer-centric variety-seeking behavior and the product-centric unexpectedness property. The idea of providing more unexpected recommendations to variety seekers is also motivated by the existing literature (Menon and Kahn 1995, Maimaran and Wheeler 2008), in which researchers show through laboratory experiments that consumers’ need for stimulation can be met by providing more variety to them. We extend the results in laboratory experiments and propose to provide variety in a personalized manner through the concept of unexpectedness in data mining, resulting in significant performance improvements. Our research sheds light on the business impact of addressing consumers’ desire for product variety as we demonstrate through off-line and online experiments.

## 2.2. Unexpectedness and Related Concepts in Recommender System

Recommender systems provide numerous economic ben efits across various industries (Senecal and Nantel 2004, Hosanagar et al. 2014, Panniello et al. 2016). However, typical methods recommend only similar products (Adomavicius and Tuzhilin 2005), ignoring the dispersion of consumer preference (Givon 1984) and raising the problem of overspecialization and user boredom (Adamopoulos and Tuzhilin 2014, Li and Tuzhilin 2020) that negatively affect model performance. To address these issues, data-mining researchers identify the concept of unexpectedness (Kaminskas and Bridge 2016) as a powerful tool to tackle the problem of exploration–exploitation (Schwartz et al. 2017, Zhang et al. 2020). Unexpectednessbased methods identify those products that depart from consumers’ expectations to meet their satisfaction (Adamopoulos and Tuzhilin 2014, Li and Tuzhilin 2020). Specifically, they deploy a hybrid utility function consisting of the relevance and unexpectedness objectives, whereas the degree of unexpectedness is only manually determined as a fixed value for all consumers (Adamopoulos and Tuzhilin 2014, Li and Tuzhilin 2020). Therefore, consumers’ heterogeneous propensity toward unexpected products and their variety-seeking levels are not taken into account, resulting in deteriorating consumer experiences (Chen et al. 2019) as some consumers prefer to stay within their comfort zones and receive familiar recommendations.

In this paper, we focus on modeling the concept of variety seeking in recommender systems in tandem with unexpectedness. Specifically, we propose a recommendation framework that incorporates variety-seeking behavior to determine the degree of unexpectedness in recommendations. By doing so, we significantly improve the level of personalization in unexpected recommendations and address consumers’ heterogeneous desire to seek product variety. We now present our variety seeking framework.

## 3. Variety-Seeking Framework

One of the key considerations in measuring the level of variety-seeking behavior of a consumer is the consumer’s propensity to explore new products and to seek significantly different content (McAlister and Pessemier 1982, Givon 1984), by which the differences between the currently selected and previously chosen products are defined in terms of a distance function that can be introduced in various ways as is explained subsequently. Another fundamental assumption in our framework is that the difference between two products x and y consumed at the corresponding periods $t _ { x }$ and $t _ { y }$ is becoming less relevant if time interval $\mid t _ { x } - t _ { y } \mid$ increases because consumers “forget” their experiences from the distant past and are less motivated to seek products different from the past as time goes by. For example, if a person consumed a pasta dish in an Italian restaurant a while ago, the person is more willing to eat another pasta dish compared with the case when the person just had it last night. In other words, the second component is the time-decay function that monotonically contracts differences between consumed products as the time interval increases. Finally, to assign a certain level of varietyseeking measure to a particular consumer, we assume that this propensity should be stable in the long run, and therefore, the process of seeking product variety in recommendations should be stationary over time, albeit experiencing small changes in the short term.

Mathematically, these components can be formally captured as follows: if consumer i purchased products $\{ i _ { 1 } , i _ { 2 } , \ldots , i _ { k } \}$ at time $\{ t _ { 1 } , t _ { 2 } , \ldots , t _ { k } \}$ , then the variety of product j at time t is defined as

$$
\text { Product\_Variety } (i, j, t) = \sum_ {k} \mu (t - t _ {k}) * \rho (i _ {k}, j),\tag{1}
$$

where $\mu ( \cdot )$ is a time-decay function, $\rho ( . , . )$ is a distance function measuring the differences between two products, and $i _ { k }$ represents the kth product consumed at time t . As explained before, when we examine how different the previously consumed products are from product j (that is consumed at time t) based on Equation (1), these differences should be stationary and do not depend on particular product j or time t because variety seeking is a property of consumer i and should be stable over time. Although this stationarity assumption can be modeled in several ways, the most natural approach is to take the average value of product variety levels over all previous products as follows (n is the number of con sumptions):

$$
\text { Variety\_Seeking } (i) = \frac {1}{n} \sum_ {k = 1} ^ {n} \text { Product\_Variety } (i, i _ {k}, t _ {k}).\tag{2}
$$

To summarize, our variety-seeking framework consists of the following three components that collectively define the concept of variety seeking of each consumer in Equation (2):

• The distance function $\pmb { \rho } ( . , . )$ measures the differences between recommended and consumed products.

• The time-decay function $\pmb { \mu } ( \cdot )$ specifies the phenomenon that consumers forget about similarities between the previously consumed products over time.

• The stationarity assumption, in which we assume the process of seeking product variety should be an intrinsic characteristic of each consumer and, therefore, should be stationary over time.

When we make specific assumptions about the exact nature of these three components, in Equation (2), we obtain the specific models of variety-seeking measures corresponding to our variety-seeking framework. We visualize our framework in Figure 1 and now describe these three specific components in detail.

## 3.1. Distance Function

The idea of computing distances between various products is studied in the variety-seeking literature (McAlister and Pessemier 1982), in which the level of variety seeking is computed as a binary value, depending on whether the candidate product appears in the consumption record before or not (Givon 1984, Kahn et al. 1986). However, it does not take into account the degree of dif ferences between various products as some products can be very similar to each other, whereas others are not. Therefore, researchers propose to measure the level of variety seeking as the proportion of explicit features with same values between two products among all feature dimensions (Van Trijp et al. 1996, Gullo et al. 2019). These feature-based measures manage to achieve significant performance improvements versus the binary method (Kim et al. 2002).

Figure 1. Diagram of Our Variety-Seeking Measurement and Recommendation Frameworks  
![](/api/attachments/U435FGRW/fulltext/images/d90280fcaf75817aacef00aead550ca56563ca4623c5b93b949d8eaeccffb1a6.jpg)

In this paper, we present another method to measure distances in the latent space using the deep learning–based method (Zhang et al. 2019) to model variety seeking in a more nuanced way than previous distances in the feature space. It also effectively captures heterogeneous and complex relationships along different feature dimensions (He et al. 2017, Zhang et al. 2019) and automatically determines the relative importance of them when comparing the differences. These tasks, however, are generally hard for feature-based methods (Boatwright et al. 2008, Sahoo et al. 2012). It also consolidates high-dimensional explicit features into low-dimensional latent embeddings (Hinton and Salakhutdinov 2006), making computations much more efficient and preserving the essence of feature information.

Whereas a wide range of latent representation models is proposed in the CS literature, we focus on the autoencoding (AE) (Hinton and Salakhutdinov 2006) model in this paper as it is the most popular method deployed in industrial platforms (Zhang et al. 2019), such as Alibaba (Li et al. 2020b) and Amazon (Hardesty 2022). It is also flexible, scalable, and memory efficient, making it easier to incorporate into recommendation designs (Zhang et al. 2019), such as variety seeking in our paper. The AE model learns two separate neural networks simultaneously: the encoder network $F _ { e n c o d e r . }$ , which maps explicit features into latent representations, and the decoder network $F _ { d e c o d e r }$ , which reconstructs explicit features from latent representations. These two networks are jointly optimized by minimizing the reconstruction loss for explicit features x: $L _ { A E } ( x ) = \bar { F } _ { d e c o d e r } ( F _ { e n c o d e r } ( x ) )$ . The product representations are then obtained by applying the encoder network: $W _ { x } = F _ { e n c o d e r } ( x )$ . Therefore, to compute the differences between products x and $y ,$ we only need to compute the distance between their latent representations $\bar { d } ( W _ { x } , W _ { y } )$ , which is formulated as the most popular Euclidean distance or other alternative distance metrics in the latent space.

To summarize, the distance function between new and previously consumed products is an important component for modeling the level of variety seeking, which can be defined either as the classic feature-based distances or through the Euclidean or other types of distances between latent product representations. As we demonstrate in Section 3.5, the latent Euclidean distance function performs significantly better than other distance metrics as it fits well with the Euclidean space of product embeddings and is most suitable for recommendation tasks as shown in the literature (Covington et al. 2016, Zhang et al. 2019).

## 3.2. Time-Decay Function

We now introduce another important dimension in the variety-seeking framework: the time decay function $\mu ( \cdot )$

which specifies the phenomenon that consumers forget about similarities between the previously consumed products over time as has been the case in other marketing applications, such as advertising (Braun and Moe 2013) and product sales (Helsen and Schmittlein 1993). The most popular time-decay function for consumer modeling is the exponential decay function (Helsen and Schmittlein 1993), which follows the proportional hazard and accelerated failure time models that apply an exponential penalty for time-related covariates (Chintagunta 1998). Other methods include the hyperbolic discounting (Laib son 1997, Machado and Sinha 2007) and additive risk (Seetharaman 2004) models, which use the hyperbolic function to model time-decay effects. These time-decay functions model dwell-time information and obtain a more effective estimation of variety levels of new products as a result.

Meanwhile, time-varying factors are not properly taken into account in prior variety-seeking models (Van Trijp et al. 1996, Kim et al. 2002), which is unfortunate as they play important roles in shaping consumer online experience, such as accumulating consumer dissatisfaction with repeated choices over time (LaBarbera and Mazursky 1983). In particular, consumer decisions are significantly affected by contextual, time-related factors in recommender systems (Panniello et al. 2016), such as the dwell time between two purchase actions. We demonstrate through the user questionnaire analysis in Section 3.5 that the time-decay function $\mu ( \cdot )$ is an integral component for measuring variety-seeking behavior in recommendations.

## 3.3. Stationarity of Variety-Seeking Behavior

Finally, we introduce the last dimension in our varietyseeking framework: the stationary property. As discussed earlier in Section 3, it is crucial to guarantee stationarity of the variety-seeking measure over time because variety seeking is an intrinsic characteristic of a consumer and, therefore, should be stable. Whereas many plausible variety-seeking statistics can be applied to the set of prod uct variety levels to match with the stable variety-seeking behavior within our framework, the arithmetic mean statistic stands out, and we use it in this paper because of its stationarity property that we empirically validate in the paper and is also demonstrated in (Gullo et al. 2019). Moreover, several existing marketing studies (Van Trijp et al. 1996, Kim et al. 2002, Gullo et al. 2019) also use the arithmetic mean when defining variety seeking.

Specifically, we formulate the stationarity hypothesis stating that the variety-seeking behavior of a consumer is stable over time in the long run as a stationary time series, assuming that product variety is defined by Equation (1). Whereas it is a simplifying hypothesis and not the only plausible way to specify the variety-seeking measure, it constitutes a practical and reasonable assumption as it matches consumer behavior patterns observed in our studies and manages to provide strong performance results with minimal computational costs as we empirically validate in this section on three off-line data sets and an online controlled experiment. We discuss other methods, such as dynamic variety-seeking measures as our future work.

To start, we analyzed the dynamic patterns of variety in the video-streaming platform studied in our online experiment, in which the average mean and variance of product variety levels are 0.2387 and 0.011, respectively, demonstrating little change in variety-seeking behaviors. We also randomly selected 10,000 consumers following the same demographic distribution of the entire consumer population on the platform and categorized them into variety seekers and consistency seekers based on whether the variety-seeking level is above average or not. We compute the product variety level of the last 10 recently completed videos and first 50 completed videos since they entered the platform and then plot the average computed values in Figure 2. We observe that there are indeed some fluctuations in the initial part of the viewing history but not among the later stage or the last 10 completed videos when consumers have watched sufficient amounts of videos and their variety-seeking patterns have converged, making sense for us to determine the varietyseeking level of each consumer through the arithmetic mean of product variety levels in the consumptions.

In addition to the direct observations, we also conducted the augmented Dickey–Fuller test (ADF) (Dickey and Fuller 1979) to test for the null hypothesis that a unit root is present, whereas the alternative hypothesis is that the time series of product variety levels is stationary. We utilize the data collected from three off-line experiments (Yelp, MovieLens, Alibaba) and the online experiment (Company A), for which the ADF test is conducted separately in the pretreatment and posttreatment periods to ensure that consumers experience the same recommendation model. As we present in Table 1, for those variety-seeking measures formulated under the varietyseeking framework that we summarize in Section 3.4, the average test statistics are all statistically nonsignificant at the 95% confidence level. Therefore, the null hypothesis is rejected, and we verify that the product variety levels are indeed stationary in our off-line and online experiments. We also observe from Table 1 that the time-decay function is an integral component of our framework without which the stationarity property would not hold as consumers’ memory fades over time and they might not remember past experiences with products purchased a long time ago.

To summarize, we empirically demonstrate the stationarity property of our modeling approach to product variety, enabling us to compute the product variety function of a consumer in a practical and useful man ner. We also emphasize that this stationarity property does not focus exclusively on the arithmetic mean statistic and may include various alternative statistics to measure variety seeking, such as weighted mean, geometric mean, harmonic mean, and median, as long as they fit in the stationarity property. However, the arithmetic mean statistic constitutes one simple, reasonable, and effective option that produces better performance over other alternative statistics as we demonstrate in the online appendix (part III).

## 3.4. Summary of the Variety-Seeking Framework We can now summarize our variety-seeking framework defined by Equations (1) and (2):

• The distance function, which can be selected as either a binary or feature-based distance following existing variety-seeking literature (Van Trijp et al. 1996, Kim et al. 2002) or Euclidean or other types of distances in the latent space as discussed in Section 3.1.

• The time-decay function, which can be modeled as exponential decay, hyperbolic discounting (Helsen and

Figure 2. (Color online) Product Variety Levels (with Standard Deviation) in First 50 and Last 10 Completed Videos of Sampled Consumers  
Variety-Seeking Patterns of Last 10 Videos on Sampled Consumers  
![](/api/attachments/U435FGRW/fulltext/images/27a8f050f46060d7c997345b92452de3852e17028c7ad8bef8f2c8cc8b76fc2c.jpg)

Variety-Seeking Patterns of First 50 Videos on Sampled Consumers  
![](/api/attachments/U435FGRW/fulltext/images/03ce1ff89608597a022799eee9ddfa26965edf22beaa3839dde8c3014258228a.jpg)

Table 1. ADF Test Statistics of the Variety-Seeking Levels Under Our Proposed Framework

<table><tr><td>Variety-seeking framework</td><td>Yelp</td><td>MovieLens</td><td>Alibaba</td><td>Online experiment</td></tr><tr><td>Binary+Exponential+Mean</td><td>-7.62</td><td>-17.88</td><td>-9.69</td><td>-11.03</td></tr><tr><td>Binary+Hyperbolic+Mean</td><td>-5.44</td><td>-13.67</td><td>-8.84</td><td>-9.74</td></tr><tr><td>Binary+No Decay+Mean</td><td>-1.12*</td><td>-1.55*</td><td>-0.96*</td><td>-1.68*</td></tr><tr><td>Feature+Exponential+Mean</td><td>-6.97</td><td>-13.66</td><td>-8.87</td><td>-12.55</td></tr><tr><td>Feature+Hyperbolic+Mean</td><td>-5.65</td><td>-11.79</td><td>-8.07</td><td>-10.06</td></tr><tr><td>Feature+No Decay+Mean</td><td>-1.17*</td><td>-1.84*</td><td>-1.33*</td><td>-2.35*</td></tr><tr><td>Euclidean+Exponential+Mean</td><td>-61.62</td><td>-75.33</td><td>-77.64</td><td>-35.12</td></tr><tr><td>Euclidean+Hyperbolic+Mean</td><td>-47.35</td><td>-71.04</td><td>-51.28</td><td>-27.68</td></tr><tr><td>Euclidean+No Decay+Mean</td><td>-2.95*</td><td>-3.12*</td><td>-2.07*</td><td>-2.99*</td></tr><tr><td>Cosine+Exponential+Mean</td><td>-52.77</td><td>-67.94</td><td>-73.65</td><td>-31.07</td></tr><tr><td>Cosine+Hyperbolic+Mean</td><td>-43.36</td><td>-62.49</td><td>-52.97</td><td>-26.95</td></tr><tr><td>Cosine+No Decay+Mean</td><td>-2.99*</td><td>-3.03*</td><td>-2.06*</td><td>-2.94*</td></tr><tr><td>Manhattan+Exponential+Mean</td><td>-17.61</td><td>-57.96</td><td>-61.45</td><td>-12.65</td></tr><tr><td>Manhattan+Hyperbolic+Mean</td><td>-10.86</td><td>-41.17</td><td>-38.86</td><td>-7.74</td></tr><tr><td>Manhattan+No Decay+Mean</td><td>-3.13*</td><td>-3.28*</td><td>-2.77*</td><td>-3.32*</td></tr><tr><td>Chybeshev+Exponential+Mean</td><td>-15.55</td><td>-52.88</td><td>-57.95</td><td>-10.88</td></tr><tr><td>Chybeshev+Hyperbolic+Mean</td><td>-8.82</td><td>-43.79</td><td>-34.41</td><td>-6.26</td></tr><tr><td>Chybeshev+No Decay+Mean</td><td>-3.30*</td><td>-3.04*</td><td>-2.96*</td><td>-3.21*</td></tr></table>

Note. The critical value used to determine the statistical significance at the 95% confidence level is �3.50. \*p < 0.05.

Schmittlein 1993), or other functions discussed in Section 3.2.

• The stationarity assumption, which implies that the variety-seeking propensity is a fundamental characteristic of a consumer and, therefore, should be stable over time. Our framework assumes the deployment of any alternative statistic as long as it fits with the stationary property.

These three components of the variety-seeking framework are summarized in Table 2. Each specific option of components in Table 2 leads to a particular varietyseeking measure. For example, we can assume that is the Euclidean distance function in a latent space, the time decay is exponential, and the summary statistic is the arithmetic mean, which leads us to a particular variety-seeking measure of the consumers. Moreover, we demonstrate in Section 3.5 that this particular measure captures consumer desire for variety most accurately and generates the best performance across several alternative models.

Finally, our variety-seeking framework stems from existing variety-seeking literature (Van Trijp et al. 1996, Zeithammer and Thomadsen 2013, Gullo et al. 2019) and significantly advances them from the following three perspectives. First, the framework supports multiple functions to measure distances between the products in the recommendation context in both the feature and latent spaces, thus leading to a broad set of choices for the distance function. Second, we highlight the importance of adopting the time-decay function to model time-varying factors in the consumer decision-making process, which is largely ignored in the literature. Finally, we empirically validate the stationarity assumption of variety-seeking behavior in recommender systems, which enables us to determine the variety-seeking level through the arithmetic mean. Under our variety-seeking framework, we are able to construct several specific variety-seeking models for designing recommender systems, on which we elaborate in the next section.

## 3.5. Validation of the Variety-Seeking Framework

To further demonstrate the validity of our variety-seeking framework, we follow the standard marketing practice and conduct the consumer questionnaire analysis (Van Trijp and Steenkamp 1992, Wang and Huang 2018) by utilizing a user survey data set collected by Alibaba (Chen et al. 2019) over three weeks starting from December 21, 2017, to January 11, 2018. Specifically, 2,401 consumers (1,651 females versus 750 males) on the grocery shopping platform participated in the survey that evaluates their instant feedback toward the recommended products. Their responses are carefully checked to make sure there are no invalid records (such as consistently responding with the same answer to all questions or missing answers to some questions). In addition, an analysis of their historical activities over the past three months shows that all of them are well familiar with the online recommendation platform of Alibaba as they all clicked at least one recommended product before taking the survey, whereas 98.5% of them had more than 100 clicks.

Table 2. Summary of Our Variety-Seeking Framework

<table><tr><td>Distance function ρ(·,·)</td><td>Time-decay function μ(·)</td><td>Stationarity property/summary statistics</td></tr><tr><td>Binary distanceFeature-based distanceDistance in latent spaceEuclidean distanceOther distances</td><td>Exponential decayHyperbolic discountingOther time-decay functions</td><td>Summary statistics satisfying stationarity property (e.g., arithmetic mean)Other summary statistics</td></tr></table>

More specifically, each participant is first presented with a recommended product (generated by the company from one of the product domains clothes, toys, home appliances, and foods) together with its name, image, short description, and price and then asked to complete a set of questions shown in the online appendix (part I) based on a five-point Likert scale (i.e., 1 � extremely agree and 5 � extremely disagree) to assess the participant’s feedback on this recommendation. One of the questions, “The item recommended to me is different from the types of products I bought before,” is directly related to the variety level as previous marketing literature (Wang and Huang 2018, Yoon and Kim 2018) adopt similar types of language to evaluate product variety levels. They are then shown the next recommended product and asked to respond to the same set of questions again until the end of the experiment (they can resume from the point at which they left off the previous session), in which they are asked to provide background information and fill out the psychological curiosity quiz, Ten-Item Curiosity and Exploration Inventory II (Kashdan et al. 2009) shown in the online appendix (part I) to determine their curiosity or variety-seeking levels. Finally, all participants were placed in a lottery draw for customized awards as an incentive. The important statistics of consumer responses are reported in Table 3, and other details are reported in the online appendix (part I).

For each recommended product, we compare its product variety value reported by the consumer through the questionnaire and the value computed by Product\_ $V a r i e t y ( i , j , t )$ in Equation (1). We also compare each consumer’s variety-seeking level reported through the curiosity quiz and the value computed by Variety\_Seeking(i) in Equation (2) and two baseline models from the marketing literature: additive parametric function (APF) (Givon 1984, Kim et al. 2002) and product assortment size (PAS) (Van Trijp et al. 1996, Gullo et al. 2019). Results presented in Table 4 show that those variety-seeking measures constructed under our framework obtain the highest correlation with consumers’ self-reported prod uct variety levels and variety-seeking levels, and the improvements over APF and PAS are statistically signi ficant across various configurations. We also identify the best-performing model “Euclidean+ Exponential + Mean,” which selects the Euclidean distance in the latent space as the distance function, the exponential decay as the time-decay function, and the arithmetic mean statistic to construct a consumer variety-seeking measure. Finally, we observe from Table 4 that, if we remove the time-decay function, the resulting varietyseeking measures do not perform well, indicating the importance of time-varying factors in modeling varietyseeking behavior. We also study in the online appendix (part II) the classification performance of consistencyversus variety-seeking consumers, in which we observe similar levels of performance improvements.

To summarize, we demonstrate that our proposed variety-seeking measures defined by Equations (1) and (2) correlate well with variety-oriented measures from the survey described in this section. We also demonstrate that each dimension in our framework, namely, the distance function, time-decay function, and stationarity assumption, is important when modeling the level of variety-seeking behavior of each consumer.

## 4. Recommendation Framework 4.1. The Utility Function Design

Based on the variety-seeking framework, we now focus on building the recommendation framework that incorporates the variety-seeking levels of each consumer in the design of the utility function. In classic recommendation models (Adomavicius and Tuzhilin 2005), the utility value is solely determined by the relevance objective for each product j and consumer i: ${ \cal U } t i l i t y ( i , j ) =$ $R e l e v a n c e ( i , j )$ as the goal is to identify the most relevant types of products for consumers. However, doing so might fail to address consumers’ desire for novel con tent in provided recommendations (Adamopoulos and Tuzhilin 2014), and it is crucial to also take into account the unexpectedness objective to expand consumers horizons (Chen et al. 2019): $U t i l i t y ( i , j ) = R e l e v a n c e ( i , j )$ $+ \alpha \times U n e x p e c t e d n e s s ( i , j ) .$ , where the value of α controls for the degree of unexpectedness and is typically selected as a fixed value for all consumers on the platform (e.g., see Li and Tuzhilin 2020). Note, however, that the varietyseeking levels can vary significantly across different consumers based on the discussions in Section 3 as some of them are more adventurous, whereas others have less propensity for desiring new experiences. In contrast, unexpectedness is the property of individual products measuring their deviations from consumer expectations. Therefore, the concepts of unexpectedness and varietyseeking are complementary to each other in the sense that the variety-seeking level of the consumer can be used to determine the degree of unexpectedness in recommendations to that consumer as we provide more unexpected recommendations to consumers with high variety-seeking levels and are more eager to explore novel content and vice versa. Specifically, these two concepts are integrated into one unified recommendation framework following the multiobjective optimization paradigm:

Table 3. Important Statistics of Consumer Response to the Questionnaire

<table><tr><td>Survey question and response</td><td>Mean</td><td>Standard deviation</td><td>Median</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td>Product variety level: “The item recommended to me is different from the types of products I bought before”</td><td>3.39</td><td>1.215</td><td>4.00</td><td>-0.400</td><td>-0.813</td></tr><tr><td>Variety-seeking level: Ten-Item Curiosity and Exploration Inventory II</td><td>3.13</td><td>0.831</td><td>3.10</td><td>0.088</td><td>-0.402</td></tr></table>

Table 4. Pearson Correlation Coefficients Between Consumers’ Self-Reported Variety-Seeking Levels and Our Variety-Seeking Framework

<table><tr><td>Variety-seeking framework</td><td>Product_Variety(i,j,t)</td><td>Variety_Seeking(i)</td></tr><tr><td>Euclidean+Exponential+Mean</td><td>0.775***(0.004)</td><td>0.618***(0.003)</td></tr><tr><td>(%improved)</td><td>+16.77%</td><td>+8.58%</td></tr><tr><td>Euclidean+Hyperbolic+Mean</td><td>0.761***</td><td>0.612***</td></tr><tr><td>Euclidean+No Decay+Mean</td><td>0.658*</td><td>0.540</td></tr><tr><td>Cosine+Exponential+Mean</td><td>0.758***</td><td>0.609***</td></tr><tr><td>Cosine+Hyperbolic+Mean</td><td>0.756***</td><td>0.607***</td></tr><tr><td>Cosine+No Decay+Mean</td><td>0.659*</td><td>0.541</td></tr><tr><td>Manhattan+Exponential+Mean</td><td>0.696***</td><td>0.588***</td></tr><tr><td>Manhattan+Hyperbolic+Mean</td><td>0.685***</td><td>0.584***</td></tr><tr><td>Manhattan+No Decay+Mean</td><td>0.647</td><td>0.538</td></tr><tr><td>Chebyshev+Exponential+Mean</td><td>0.693***</td><td>0.589***</td></tr><tr><td>Chebyshev+Hyperbolic+Mean</td><td>0.686***</td><td>0.589***</td></tr><tr><td>Chebyshev+No Decay+Mean</td><td>0.645</td><td>0.537</td></tr><tr><td>Feature+Exponential+Mean</td><td>0.688***</td><td>0.591***</td></tr><tr><td>Feature+Hyperbolic+Mean</td><td>0.692***</td><td>0.589***</td></tr><tr><td>Feature+No Decay+Mean</td><td>0.645</td><td>0.565</td></tr><tr><td>Binary+Exponential+Mean</td><td>0.667**</td><td>0.562</td></tr><tr><td>Binary+Hyperbolic+Mean</td><td>0.665**</td><td>0.558</td></tr><tr><td>Binary+No Decay+Mean</td><td>0.631</td><td>0.532</td></tr><tr><td>APF</td><td>0.631</td><td>0.532</td></tr><tr><td>PAS</td><td>0.645</td><td>0.565</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01 (compared with APF and PAS).

$$
\begin{array}{r l} & U t i l i t y (i, j) = R e l e v a n c e (i, j) \\ & \qquad + f (V a r i e t y \_ S e e k i n g (i), U n e x p e c t e d n e s s (i, j)), \end{array}\tag{3}
$$

where $f ( . , . )$ is the aggregation function that models the complementary relationship. Recommendations are subsequently produced by selecting products with the highest utility values. This framework enables us to address consumers’ heterogeneous desire for product variety and improve satisfaction as a result. We also do not need to go through the complex process to determine the value of α described previously because it is automatically determined by variety-seeking measures, making it more manageable and practical.

We summarize a series of configuration options in Table 5 along the relevance, unexpectedness, and aggregation function dimensions. The relevance dimension assumes recommendation methods that focus exclusively on providing relevant content, such as the state-of the-art methods of neural collaborative filtering (NCF) (He et al. 2017) and deep interest network (DIN) (Zhou et al. 2018) that have achieved great success in practice. The second dimension of the framework focuses on the unexpectedness objective that can be formulated through classic feature-based methods (Adamopoulos and Tuzhilin 2014) or latent modeling (Li and Tuzhilin 2020) deployed by Alibaba (Li et al. 2020b). Finally, the aggregation function constitutes the third dimension, and it can be selected as the multiplication function Variety\_ $S e e k i n g ( i ) \times U n e x p e c t e d n e s s ( i , j )$ , the exponential function $e ^ { V a r i e t y \smile S e e k i n g ( i ) } \times \dot { U n e x p e c t e d n e s s } ( i , j )$ , or the power function $U n e x p e c t e d n e s s ( i , j ) ^ { V a r i e t y \_ S e e k i n g ( i ) }$ . We demonstrate in Section 5 that all these options in Table 5 lead to effective unexpected recommender system designs that significantly outperform existing methods and the combination of deep interest network for the relevance objective, latent modeling of the unexpectedness objective, and the multiplication function leads to the best performance.

Table 5. The Variety-Seeking Recommendation Framework

<table><tr><td>Relevance(i,j)</td><td>Unexpectedness(i,j)</td><td>Aggregation function f(.,.)</td></tr><tr><td>NCF</td><td>Feature-based methods</td><td>Multiplication function</td></tr><tr><td>DIN</td><td>Latent representation methods</td><td>Exponential function</td></tr><tr><td>Other relevance-focused methods</td><td>Other unexpectedness methods</td><td>Power function</td></tr><tr><td></td><td></td><td>Other aggregation function</td></tr></table>

To summarize, our proposed recommendation framework is significantly different from the existing unexpected recommender systems (Adamopoulos and Tuzhilin 2014, Li et al. 2020b) as we determine the degree of unexpectedness in the utility function through the variety-seeking levels identified from the framework that we present in Section 3, resulting in significantly better performance in real business applications vis-a\`-vis state-of-the-art baselines and the latest production system in Company A.

## 4.2. Validation of the Recommendation Framework: Off-line Experiments

In this section, we consider several models fitting the framework and test their performance in the clickthrough rate prediction task, which is the most correlated with the business revenues generated in the recommendation platform (Zhou et al. 2018). We test on three offline data sets collected from industrial platforms of Yelp, MovieLens, and Alibaba. Each data set contains the IDs of consumers and products and the time stamp of purchasing actions. For the Alibaba data set, we also have binary labels of whether consumers click on the recommended product or not. For the Yelp and MovieLens data sets, however, we only obtain ratings (scale of 1–5) toward the recommended product, and we simulate consumer response by transforming ratings into binary labels using the threshold of 3.5, following the common practice in the recommender system literature (Zhang et al. 2019, Li et al. 2020b). We also test for the alternative thresholds of 2.5 and 3 and obtain the same set of empirical findings. To further test the robustness of our proposed framework, we create three subsets of the Alibaba data set with different sparsity levels and summarize them in the online appendix (part VI). Note that the three off-line data sets listed in Table 6 represent three vastly different business applications of catering, movie streaming, and short videos with significant differences in the distribution of variety seekers demonstrated in Figure 3(a)–(c), in which the x-axis represents the “bins” of variety-seeking levels and the y-axis represents the number of consumers in each bin. Consequently, results on these data sets significantly enhance the generalizability of our findings across different applications.

Table 6. Descriptive Statistics of Three Off-line Data Sets

<table><tr><td>Data set</td><td>Yelp</td><td>MovieLens</td><td>Alibaba</td></tr><tr><td>#Consumers</td><td>76,564</td><td>138,493</td><td>46,143</td></tr><tr><td>#Products</td><td>75,231</td><td>15,079</td><td>53,657</td></tr><tr><td>#Transactions</td><td>2,254,589</td><td>19,961,113</td><td>1,806,157</td></tr><tr><td>Sparsity, %</td><td>0.039</td><td>0.956</td><td>0.073</td></tr></table>

We compare the performance with the following four groups of eight state-of-the-art baselines:

1. Relevance-oriented recommendation models, in cluding DIN (Zhou et al. 2018) and DeepFM (Guo et al. 2017), in which we optimize only for the relevance objective: $U t i l i t y ( i , j ) = \mathbf { \hat { R } } e l e v a n c e ( i , j ) .$

2. Unexpectedness-oriented recommendation models, including HOM-LIN (Adamopoulos and Tuzhilin 2014) and PURS (Li et al. 2020b), in which α in the utility function $U t i l i t y ( i , j ) = R e l e v a n c e ( i , j ) + \alpha \times U n e x p e c t e d n e s s ( i , j )$ is determined without taking into account the varietyseeking levels.

3. Diversity-oriented recommendation models, including reranking (Adomavicius and Kwon 2011) and DPP (Chen et al. 2018), which focus on diversity rather than unexpectedness in recommendations.

4. Bandit-learning recommendation models, including LinUCB (Li et al. 2010) and COFIBA (Li et al. 2016), which explore consumer preference in recommenda tion through bandit models.

As we discuss in Section 3, the “Euclidean + Exponential + Mean” method captures variety-seeking behaviors most effectively among all models fitting the variety-seeking framework, and we adopt it to measure Variety\_Seeking(i) in our recommendation framework. To ensure a fair comparison, we use the same set of hyperparameter optimization techniques of Bayesian hy perparameter optimization (Feurer et al. 2015) to identify the optimal configurations for our models and all baselines. As a result, the autoencoder in Section 3.1 is constructed using the MLP network with one input layer, three hidden layers, and one output layer and [256, 128, 16, 128, 256] units in each layer respectively. The neural network parameters are initialized with the Gaussian distribution of mean 0 and standard deviation 0.01 and then optimized by stochastic gradient descent with a learning rate 0.001. We normalize Relevance(i, j), Variety\_ Seeking(i), and $U n e x p e c t e d n e s s ( i , j )$ to between �1 and 1 to facilitate the recommender system training process (Covington et al. 2016) without distorting differences in the ranges of values or losing information.

## 4.3. Off-line Experiment Results

We evaluate the recommendation performance using the standard machine learning–based recommendation metrics area under the curve (AUC) and Hit Rate@10 (Shani and Gunawardana 2011). The off-line experiments are conducted following time-stratified fivefold crossvalidation, and we report the average performance over multiple runs in Table 7. We observe from the table that

Figure 3. (Color online) Distribution of Variety-Seeking Level in Three Off-line Data Sets  
(a)  
![](/api/attachments/U435FGRW/fulltext/images/b70bb776e0a46b2d8e5b1eaa3c8d36625afbff66c41bb04d4da7e6f3a7167269.jpg)

(b)  
![](/api/attachments/U435FGRW/fulltext/images/06d8db9bc3ee60375ce646b107ac6c376947fb1de5f2731a05d5aa9e9f8d8f3a.jpg)

(c)  
![](/api/attachments/U435FGRW/fulltext/images/72644dd268db5908b2c2f952672cd17189cf6009b58829a550b6ee59c9f39473.jpg)  
Notes. (a) Yelp data set. (b) MovieLens data set. (c) Alibaba data set.

all the recommendation models under our recommendation framework significantly outperform all other baselines in terms of evaluation metrics AUC and Hit Rate@10 across all three data sets. On average, we observe an increase of 3.81% for the AUC metric and 3.81% for the HR@10 metric for our proposed models as compared with the second best baseline approach. In particular, we identify one specific model “DIN + Latent + Multiply” that works most effectively, in which we compute the relevance objective using the DIN model, formulate the unexpectedness objective using latent modeling, and combine variety seeking with unexpectedness using the multiplication function. These performance improvements are not only statistically significant, but also demonstrate tangible performance gains in terms of the best practices in the recommender system industry (Hardesty 2022). In addition, the results in the online appendix (part VI) confirm that our proposed framework still performs significantly better across all three Alibaba data sets with different sparsity levels and different consumption quantities for each consumer.

To summarize, as three off-line data sets represent vastly different business applications, sparsity levels, and variety-seeker distributions, these results demonstrate the effectiveness, generalizability, and external validity of our recommendation framework. Specifically, we show that combining variety seeking and unexpectedness is beneficial and works well in practice by providing more unexpected recommendations to variety seekers, and vice versa, we significantly improve the recommendation performance.

Table 7. Off-line Results on the Three Industrial Data Sets

<table><tr><td rowspan="2"></td><td colspan="2">Yelp</td><td colspan="2">MovieLens</td><td colspan="2">Alibaba</td></tr><tr><td>AUC</td><td>HR@10</td><td>AUC</td><td>HR@10</td><td>AUC</td><td>HR@10</td></tr><tr><td>DIN+Latent+Multiply</td><td>0.7071***(0.0071)</td><td>0.7096***(0.0073)</td><td>0.8375***(0.0103)</td><td>0.7004***(0.0092)</td><td>0.7349***(0.0088)</td><td>0.7730***(0.0089)</td></tr><tr><td>(%improved)</td><td>+5.18%</td><td>+4.95%</td><td>+3.52%</td><td>+3.33%</td><td>+2.73%</td><td>+3.15%</td></tr><tr><td>DIN+Latent+Exponential</td><td>0.6973***</td><td>0.7001***</td><td>0.8317***</td><td>0.6949***</td><td>0.7328***</td><td>0.7701***</td></tr><tr><td>DIN+Latent+Power</td><td>0.6932***</td><td>0.6980***</td><td>0.8288***</td><td>0.6952***</td><td>0.7324***</td><td>0.7688***</td></tr><tr><td>DIN+Feature+Multiply</td><td>0.6817**</td><td>0.6974***</td><td>0.8291***</td><td>0.6930***</td><td>0.7299***</td><td>0.7672***</td></tr><tr><td>DIN+Feature+Exponential</td><td>0.6810**</td><td>0.6982***</td><td>0.8269***</td><td>0.6937***</td><td>0.7303***</td><td>0.7654***</td></tr><tr><td>DIN+Feature+Power</td><td>0.6804**</td><td>0.6971***</td><td>0.8269***</td><td>0.6941***</td><td>0.7291***</td><td>0.7658***</td></tr><tr><td>NCF+Latent+Multiply</td><td>0.6776*</td><td>0.6950***</td><td>0.8208**</td><td>0.6873***</td><td>0.7266**</td><td>0.7649***</td></tr><tr><td>NCF+Latent+Exponential</td><td>0.6790**</td><td>0.6977***</td><td>0.8172*</td><td>0.6855**</td><td>0.7261**</td><td>0.7610**</td></tr><tr><td>NCF+Latent+Power</td><td>0.6794**</td><td>0.6956***</td><td>0.8189**</td><td>0.6852**</td><td>0.7249**</td><td>0.7587**</td></tr><tr><td>NCF+Feature+Multiply</td><td>0.6755*</td><td>0.6943***</td><td>0.8192**</td><td>0.6839*</td><td>0.7228**</td><td>0.7599**</td></tr><tr><td>NCF+Feature+Exponential</td><td>0.6753*</td><td>0.6928***</td><td>0.8157*</td><td>0.6851**</td><td>0.7237**</td><td>0.7576**</td></tr><tr><td>NCF+Feature+Power</td><td>0.6771*</td><td>0.6936***</td><td>0.8170*</td><td>0.6851**</td><td>0.7240**</td><td>0.7573**</td></tr><tr><td>DIN</td><td>0.6694</td><td>0.6702</td><td>0.7021</td><td>0.6485</td><td>0.6957</td><td>0.6972</td></tr><tr><td>DeepFM</td><td>0.6396</td><td>0.6682</td><td>0.7056</td><td>0.6169</td><td>0.5519</td><td>0.5164</td></tr><tr><td>PURS</td><td>0.6723</td><td>0.6761</td><td>0.8090</td><td>0.6778</td><td>0.7154</td><td>0.7494</td></tr><tr><td>HOM-LIN</td><td>0.6287</td><td>0.6490</td><td>0.7177</td><td>0.5894</td><td>0.5812</td><td>0.5493</td></tr><tr><td>Re-Ranking</td><td>0.6295</td><td>0.6502</td><td>0.7236</td><td>0.6468</td><td>0.6025</td><td>0.5776</td></tr><tr><td>DPP</td><td>0.6448</td><td>0.6575</td><td>0.7490</td><td>0.6551</td><td>0.6517</td><td>0.7026</td></tr><tr><td>LinUCB</td><td>0.6324</td><td>0.6373</td><td>0.6883</td><td>0.6363</td><td>0.6365</td><td>0.6525</td></tr><tr><td>COFIBA</td><td>0.6411</td><td>0.6417</td><td>0.7162</td><td>0.6485</td><td>0.6471</td><td>0.6913</td></tr></table>

Note. Improvement percentages were reported over the second best baseline models (underlined) \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## 5. Online Controlled Experiments 5.1. Institutional Background

To further demonstrate the economic benefits and practical impact of our proposed framework, we conduct a large-scale online controlled experiment at a major video-streaming company in China (denoted as Company A). On the streaming platform of Company A, users cannot follow any specific accounts or other users, search for specific videos, or share content. Videos are uploaded by users and distributed solely by the personalized recommendation service. Users receive video recommendations immediately when they open the app, and they can either click on the recommended videos or seek a new set of recommendations by scrolling down and refreshing the page. In that sense, consumers have little control over their video exposures, which reduces the moderating effect of selfselection bias and enables us to estimate the average treatment effects through a simple regression in our experiment. Whereas the video-streaming platform at Company A is different from other platforms, such as TikTok or YouTube, and we might not be able to directly extend the business impact to the entire videostreaming industry, the online controlled experiment was conducted to demonstrate the advantages of our proposed frameworks and models, fitting them for a leading recommendation platform at scale (Company A has more than 500 million monthly active users and 800 million daily video views and has developed a powerful recommendation service over the past decade).

The online experiment was conducted over a full month in September 2020 and included 37,965,781 video-watching records by 444,765 users on 8,442,402 videos. The duration of one month is considered to be long term at Company A at which the vast majority of A/B tests are done over only one week and is also suffi cient to demonstrate the treatment effect of recommender system design for Company A, which runs thousands of A/B tests per year. We have confirmed with the company that no other A/B test overlapped with our focal experiment. During the experiment, we record consumer and video features that we summarize in Table 8 and the online appendix (part IV), which constitute exogenous factors that might affect consumer responses and increase the estimation variance. We now introduce our identification strategy.

## 5.2. User Splitting and Identification Strategy

We identify the average treatment effects (ATEs) by diverting the video-watching requests from consumers (Kohavi et al. 2009) following binary hashing (Salakhutdinov and Hinton 2009) over user IDs in the experiment pool, which is also the standard practice at Company $\operatorname { A } ;$ if the hash index is zero, the user is diverted to the control group and receives recommendations from the latest production system in the company described in (Li et al. 2020b): Utility(i, j) � Relevance(i, j) + α × Unexpectedness $( i , j ) ;$ otherwise, the user is diverted to the treatment group and receives recommendations from the best performing model $^ { \prime \prime } \mathrm { D I N } + \mathrm { L a t e n t } + \mathrm { M u l t i p l y } ^ { \prime \prime }$ under our framework $U t i l i t y ( i , j ) = R e l e v a n c e ( i , j ) + V a r i e t y \_ S e e k i n g ( i ) \times$ Unexpectedness $( i , j ) ,$ where Variety\_Seeking(i) is computed through the best performing measure “Euclidean+ Exponential+ Mean” under our variety-seeking framework. In our experiment, product embeddings and Variety\_Seeking(i) are computed off-line and updated on a daily basis, whereas $R e l e v a n c e ( i , j )$ and $U n e x p e c t e d n e s s ( i , j )$ are updated in real time to reflect dynamic consumer preferences. Similar to the off-line experiments, we also normalize the scale of $R e l e v a n c e ( i , j ) ,$ , Variety\_Seeking(i), and $U n e x p e c t e d n e s s ( i , j )$ to between �1 and 1 to facilitate the training process. This user-splitting strategy keeps the balance between the two groups as we demonstrate in Figure $^ { 4 , }$ in which the differences between the propensity score distribution are negligible. Users are also unaware of the assignment in our experiment as the graphical user interface remains the same. Therefore, we validate the randomized setting of our experiment, which enables us to assess ATEs directly through ordinary least squares regression.

Table 8. Summary of Consumer and Video Features Recorded in the Online Experiment

<table><tr><td>Category</td><td>Variable</td><td>Description</td><td>Format</td></tr><tr><td rowspan="8">Consumer features</td><td>Gender</td><td>Gender of the consumer</td><td>Categorical</td></tr><tr><td>Age</td><td>Age of the consumer</td><td>Numerical</td></tr><tr><td>Province</td><td>The province where the consumer lives in</td><td>Categorical</td></tr><tr><td>City</td><td>The city where the consumer lives in</td><td>Categorical</td></tr><tr><td>Operating system</td><td>The operation system on the consumer&#x27;s device</td><td>Categorical</td></tr><tr><td>VIP status</td><td>Subscription to the premium service or not</td><td>Categorical</td></tr><tr><td>Active days</td><td>The number of days that the consumer has logged into the platform over the past month</td><td>Numerical</td></tr><tr><td>Confidential features</td><td>Confidential features developed by the company to describe consumer behaviors/preferences</td><td>Confidential</td></tr><tr><td rowspan="6">Video features</td><td>Genre</td><td>The genre of the video</td><td>Categorical</td></tr><tr><td>View count</td><td>Total view number over the past month</td><td>Numerical</td></tr><tr><td>Comment count</td><td>Total comment number over the past month</td><td>Numerical</td></tr><tr><td>Release days</td><td>Days since it has been released on the platform</td><td>Numerical</td></tr><tr><td>Video length</td><td>The duration of the video</td><td>Numerical</td></tr><tr><td>Confidential features</td><td>Confidential features developed by the company to describe the video&#x27;s content</td><td>Confidential</td></tr></table>

Note. String variables (e.g., city) are converted to categorical features as dummy variables.

We subsequently conduct the two-sample hypothesis test by comparing users’ responses and business performance, respectively, among the two groups. Based on the practical guidelines of Company $\scriptstyle \mathrm { A , }$ the following three performance metrics are the most important business revenue indicators of the video-streaming services: (a) click-through rate (CTR), the binary variable that indicates whether the user has clicked on the recommended video or not; (b) video view, the binary variable that indicates whether the user has finished watching the recommended video or not; and (c) time spent, the continuous variables that record the dwell time the user has spent on the recommended video, and it is zero if the user hasn’t clicked. For each user i and video $j ,$ we specify the ATEs using the following identification:

Figure 4. (Color online) Comparison of Propensity Score Distribution Between the Treatment Group and the Control Group  
![](/api/attachments/U435FGRW/fulltext/images/a5983e711da4a669c0ffc28a642ca8ac71452f81950d0cae5f3623784fb3074b.jpg)

$$
M e t r i c _ {i j} = \alpha_ {0} + \alpha_ {1} * T r e a t m e n t _ {i} + \vec {\alpha_ {2}} * \vec {X _ {i}} + \vec {\alpha_ {3}} * \vec {Y _ {j}} + D _ {t} + \varepsilon_ {i j},\tag{4}
$$

where $M e t r i c _ { i j } \in \{ C T R _ { i j } , V V _ { i j } , T S _ { i j } \}$ , Treatment is the dummy variable, $X _ { i }$ represents user features, $\vec { Y _ { j } }$ represents video features, and $D _ { t }$ represents time fixed effects including dates and hours. Our findings still hold if we adopt various types of alternative identification methods as we show in Section 5.8.

## 5.3. Average Treatment Effect

We start with the regression analysis that directly compares video-watching behaviors between two user groups. We observe in Table 9 that consumers who are assigned to be served by our proposed model are 2.29% more likely to click on the recommended videos and 4.56% more likely to finish watching them compared with the latest production model in Company A. In addition, our model increases the average time spent on each recommended video by 39.219 seconds. These results indicate that, by incorporating consumers’ variety-seeking behavior into the unexpected recommender system, our proposed framework significantly increases video consumption in Company A (having $p { < } 0 . 0 1$ in all experimental settings). We also provide the empirical analysis at the user level and the difference-in-difference analysis in the online appendix (part V), in which we observe significant performance improvements across all the cases.

These improvements, generating a very significant economic impact for the video-streaming platform of Company A, are not at all surprising. By taking into account heterogeneous variety-seeking levels instead of a fixed term α, we provide personalized and properly balanced unexpected recommendations for targeted consumers according to their variety-seeking propensities, which leads to a significant increase in business performance in the treatment group. Our findings demonstrate substantial potential to increase revenues of Company A, which is, in fact, one of the largest improvements that the engineering team has observed during the entire 2020. In addition, as the video-streaming platform of Company A achieved 8,728 million RMB revenue in the fiscal year of 2020, our model would potentially bring an additional US\$30 million revenue to the company based on the 2.29% CTR improvement that is directly related to the platform profits. These significant economic benefits are achieved with only a 1.3% increase in the serving latency and a 0.5% increase in memory usage compared with the existing model, which is negligible according to the engineering team. We also conducted additional product-level, churn rate, and variety-seeking behavior analyses shown in the online appendix (parts VIII–X) to further demonstrate the robustness and impact of our method. Based on the results of this A/B test and the resulting significant business improvements, Company A has already deployed our model to serve customers on the entire video-streaming platform.

Table 9. Average Treatment Effect of Variety-Seeking Based Unexpected Recommendations

<table><tr><td></td><td> $CTR_{ij}$ </td><td> $VV_{ij}$ </td><td> $TS_{ij}$ </td></tr><tr><td> $Treatment_i$ </td><td>0.0229***(0.0043)</td><td>0.0456***(0.0028)</td><td>39.219***(0.9895)</td></tr><tr><td>User and video features</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.0081</td><td>0.0044</td><td>0.2133</td></tr><tr><td>Observations</td><td>37,965,781</td><td>37,965,781</td><td>37,965,781</td></tr></table>

Note. The table shows a regression with robust standard errors in parentheses. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

## 5.4. Heterogeneous Treatment Effects over Variety-Seeking Behavior

In this section, we show that the performance improvements are not uniform for all consumers, but are rather heterogenous across different consumer groups according to their variety-seeking levels, which we categorize into 20 bins, namely, (�0.250, �0.225), (�0.225, �0.200), … , (0.225, 0.250). We select �0.25 and 0.25 as the boundary threshold for this analysis because there are only fewer than 10 consumers in our records whose level of variety seeking is outside of this range. We subsequently identify three business metrics within each bin by adding the interaction term Treatment × Variety\_Seeking and estimate its coefficients accordingly. The results are shown in Figure 5, in which we can make the following observations. First, all consumers in the treatment group, regardless of their variety-seeking levels, enjoy a significant positive effect if served by our variety-seeking recommender system. Second, those consumers who are either truly variety seeking or are strongly opposed to receiving variety in their recommendations obtain even greater positive effects from our model. This result is natural because our model provides more unexpected recommendations to variety seekers and fewer to consistency seekers, which resonates with both groups as our study confirms. By addressing the heterogeneous desire for product variety, we avoid the mistakes of providing too similar products for variety seekers or too irrelevant products for consistency seekers, thus improving business performance. And, finally, those consumers having a medium level of variety-seeking desire still marginally benefit from our model though the benefits are not as great as for those who strongly prefer or are against variety.

Figure 5. (Color online) Heterogeneous Treatment Effects Toward the Business Metric “CTR” over Different Levels of Variety-Seeking Behavior  
![](/api/attachments/U435FGRW/fulltext/images/ab2fdb07560993d1c3c704a88694791a2fb13d797e74d1f6c5f6e75433c16c89.jpg)  
Note. We witness the same phenomena for the other two business metrics as well

## 5.5. Parallel Trend Analysis

In this section, we conduct the parallel trend analysis in Figure 6, in which we observe that there are no statistical differences between the two groups in the pretreatment period and that our proposed model consistently and sig nificantly outperforms the latest production system during the posttreatment period. Specifically, our model achieves significant performance improvements during the first week of deployment, partly because of the novelty effect. Whereas the improvements deteriorate slightly in week 2, they still remain significant, and no further performance decreases are observed after week 2 until the end of the experiment. This observation demonstrates the strong performance of our method in the long term, which is not significantly affected by consumer curiosity or short-term factors. We also conduct additional differencein-difference analysis in the online appendix (part V) to further justify our empirical findings.

Figure 6. (Color online) Parallel Trend Analysis of the Treatment Effect on Click-Through Rate (and the Confidence Inter val) in Our Online Experiment on a Daily Basis  
![](/api/attachments/U435FGRW/fulltext/images/15a66d456f56de962f5dc8291142b2f2ea3145b028acd846410a9cb273087b8c.jpg)

## 5.6. Robustness Check

We also conduct additional experiments to check the robustness of the results, in which we replicate our analysis under the following settings: (a) we include different combinations of consumer features, video features, and time fixed effects in the regression model of Equation (4) to evaluate the treatment effects; (b) we use alternative models to specify the binary outcome variables $C T R _ { i j t }$ and $V V _ { i j t } ,$ including the discrete choice models of logit and probit; (c) we exclude records of video content uploaded by Company A itself; and (d) we drop the records from those users in the regions where the platform was launched recently. The detailed results listed in the online appendix (part VII) demonstrate that our empirical findings still hold under all these conditions, further illustrating the benefits and robustness of our proposed frameworks in this paper.

## 6. Conclusions

Variety seeking plays a significant role in modeling consumers’ intentions and understanding their behaviors, and we need to address consumer desire for product variety in recommendations. To this end, we first propose a variety-seeking framework, in which we identify three key dimensions to measure consumer variety-seeking levels: the distance function, the time-decay function, and the stationarity assumption that are cohesively combined into the framework. We subsequently propose a recommendation framework in which we utilize the identified variety-seeking levels to determine the degree of unexpectedness in the utility function for providing recommendations. By doing so, we can produce more unexpected products for variety seekers and more familiar types of products for those consumers who prefer to stay within their own comfort zones, thus improving consumer satisfaction and business performance significantly.

To demonstrate the validity and effectiveness of our proposed frameworks, we conduct extensive off-line experiments and a large-scale online controlled experiment at a major video-streaming platform in China. We demonstrate that, by incorporating variety-seeking behavior into the design of unexpected recommender systems, we significantly increase the quantity of video consumption compared with the latest production model deployed at the company. We further demonstrate that the improvements in business performance are not homogenous for all consumers: those consumers who either strongly prefer or dislike product variety receive the greatest benefits from our model. Nevertheless, our model has a significant impact on all consumers on the platform as it provides them with additional variety of fresh video content, still delivering usefu recommendations and improving the consumer online experience. Because of the strong economic effect demonstrated at Company $\scriptstyle \mathrm { A , }$ our model has been deployed to serve consumers on the entire platform.

Note that horizontal variety is frequently observed to occur in industries with high rates of consumption, especially entertainment products (Kim et al. 2002), on which we largely focus in this paper. To further understand the consumers’ desire for variety seeking, we plan to also model and incorporate vertically differentiated variety seeking behavior into the design of recommender systems in future work. In addition, as our analysis focuses primarily on the video streaming platform at Company $\scriptstyle \mathrm { A , }$ we plan to conduct similar online experiments on other platforms, such as TikTok and YouTube, and also in other business applications, including music, movies, TV shows, and books. Furthermore, we plan to study more complex formulations of the variety-seeking measures, such as dynamic measures, to relax the stationarity assumption. Finally, we plan to utilize the proposed frameworks to shed light on which video genres or categories are more appealing to consumers, for example, based on their hedonic/utilitarian characteristics (Li et al. 2020a), which would help us to better understand the heterogeneous treatment effect from the product side.

## References

Adamopoulos P, Tuzhilin A (2014) On unexpectedness in recommender systems: Or how to better expect the unexpected. ACM Trans. Intelligent Systems Tech. 5(4):1–32.

Adomavicius G, Kwon Y (2011) Improving aggregate recommendation diversity using ranking-based techniques. IEEE Trans Knowledge Data Engrg. 24(5):896–911.

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6): 734–749.

Ailawadi K, Neslin S, Gedenk K (2001) Pursuing the value-conscious consumer: Store brands vs. national brand promotions. J. Market ing 65(1):71–89.

Alba JW, Marmorstein H, Chattopadhyay A (1992) Transitions in preference over time: The effects of memory on message persuasiveness. J. Marketing Res. 29(4):406–416.

Baumgartner H, Steenkamp J (1996) Exploratory consumer buying behavior: Conceptualization and measurement. Internat. J. Res. Marketing 13(2):121–137.

Bawa K (1990) Modeling inertia and variety seeking tendencies in brand choice behavior. Marketing Sci. 9(3):263–278.

Bench SW, Lench HC (2019) Boredom as a seeking state: Boredom prompts the pursuit of novel (even negative) experiences. Emotion 19(2):242–254.

Boatwright P, Kalra A, Zhang W (2008) Research note—Should consumers use the halo to form product evaluations? Management Sci. 54(1):217–223.

Braun M, Moe WW (2013) Online display advertising: Modeling the effects of multiple creatives and individual impression histories Marketing Sci. 32(5):753–767.

Chen L, Zhang G, Zhou H (2018) Fast greedy map inference for determinantal point process to improve recommendation diversity. NeurIPS 2018 (NIPS, San Diego), 5627–5638.

Chen L, Yang Y, Wang N, Yang K, Yuan Q (2019) How serendipity improves user satisfaction with recommendations? A large-scale user evaluation. WWW Conf. (ACM, New York), 240–250.

Cheng Y, Jiang ZJ, Benbasat I (2017) Designing for diagnosticity and serendipity: An investigation of social product-search mecha nisms. Inform. Systems Res. 28(2):413–429.

Chintagunta PK (1998) Inertia and variety seeking in a model of brand-purchase timing. Marketing Sci. 17(3):253–270.

Covington P, Adams J, Sargin E (2016) Deep neural networks for YouTube recommendations. Proc. 10th ACM Conf. Recommender Systems (ACM, New York), 191–198.

Dickey DA, Fuller WA (1979) Distribution of the estimators for autoregressive time series with a unit root. J. Amer. Statist. Assoc. 74(366):427–431.

Faison EW (1977) The neglected variety drive: A useful concept for consumer behavior. J. Consumer Res. 4(3):172–175.

Feinberg FM, Kahn BE, McAlister L (1992) Market share response when consumers seek variety. J. Marketing Res. 29(2):227–237.

Feurer M, Springenberg J, Hutter F (2015) Initializing Bayesian hyperparameter optimization via meta-learning. AAAI Conf. Artificial Intelligence (AAAI, Palo Alto, CA), 1128–1135.

Fishbach A, Ratner RK, Zhang Y (2011) Inherently loyal or easily bored? Nonconscious activation of consistency vs. variety seeking behavior. J. Consumer Psych. 21(1):38–48.

Fiske DW, Maddi SR (1961) Functions of Varied Experience (Dorsey, Belmont CA).

Fong NM (2017) How targeting affects customer search: A field experiment. Management Sci. 63(7):2353–2364.

Givon M (1984) Variety seeking through brand switching. Marketing Sci. 3(1):1–22.

Gorgoglione M, Panniello U, Tuzhilin A (2019) Recommendation strategies in personalization applications. Inform. Managemen 56(6):103143.

Gullo K, Berger J, Etkin J, Bollinger B (2019) Does time of day affect variety-seeking? J. Consumer Res. 46(1):20–35.

Guo H, Tang R, Ye Y, Li Z, He X (2017) DeepFM: A factorizationmachine based neural network for CTR prediction Proc. 26th Internat. Joint Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA), 1725–1731.

Hardesty L (2022) The history of Amazon’s recommendation algorithm—Amazon Science. Amazon Science (December 2022), www.amazon.science/the-history-of-amazons-recommendationalgorithm.

He X, Liao L, Zhang H, Nie L, Hu X, Chua TS (2017) Neural collaborative filtering. Proc. 26th Internat. Conf. World Wide Web (International World Wide Web Conferences Steering Committee, Geneva), 173–182.

Helsen K, Schmittlein DC (1993) Analyzing duration times in marketing: Evidence for the effectiveness of hazard rate models. Marketing Sci. 12(4):395–414.

Hinton GE, Salakhutdinov RR (2006) Reducing the dimensionality of data with neural networks. Science 313(5786):504–507.

Hosanagar K, Fleder D, Lee D, Buja A (2014) Will the global village fracture into tribes? Recommender systems and their effects on consumer fragmentation. Management Sci. 60(4):805–823.

Hoyer WD, Ridgway NM (1984) Variety seeking as an explanation for exploratory purchase behavior: A theoretical model. Adv. Consumer Res. 11:114–119.

Huang ZT, Wyer RS Jr (2015) Diverging effects of mortality salience on variety seeking: The different roles of death anxiety and semantic concept activation. J. Experiment. Soc. Psych. 58:112–123.

Kahn BE (1995) Consumer variety-seeking among goods and services: An integrative review. J. Retailing Consumer Services 2(3):139–148.

Kahn B, Wansink B (2004) The influence of assortment structure on perceived variety and consumption quantities. J. Consumer Res. 30(4):519–533.

Kahn BE, Isen AM (1993) The influence of positive affect on variety seeking among safe, enjoyable products. J. Consumer Res. 20(2): 257–270.

Kahn BE, Kalwani MU, Morrison DG (1986) Measuring varietyseeking and reinforcement behaviors using panel data. J. Marketing Res. 23(2):89–100.

Kaminskas M, Bridge D (2016) Diversity, serendipity, novelty, and coverage: A survey and empirical analysis of beyond-accuracy objectives in recommender systems. ACM Trans. Interactive Intelligent Systems 7(1):1–42.

Kashdan TB, Gallagher MW, Silvia PJ, Winterstein BP, Breen WE Terhar D, Steger MF (2009) The curiosity and exploration inventory-II: Development, factor structure, and psychometrics. J. Res. Personality 43(6):987–998

Kim J, Allenby GM, Rossi PE (2002) Modeling consumer demand for variety. Marketing Sci. 21(3):229–250.

Kohavi R, Longbotham R, Sommerfield D, Henne RM (2009) Controlled experiments on the web: Survey and practical guide. Data Mining Knowledge Discovery 18:140–181.

LaBarbera PA, Mazursky D (1983) A longitudinal assessment of consumer satisfaction/dissatisfaction: The dynamic aspect of the cognitive process. J. Marketing Res. 20(4):393–404.

Laibson D (1997) Golden eggs and hyperbolic discounting. Quart. J. Econom. 112(2):443–478.

Lee GM, He S, Lee J, Whinston AB (2020) Matching mobile applications for cross-promotion. Inform. Systems Res. 31(3): 865–891.

Levav J, Zhu RJ (2009) Seeking freedom through variety. J. Consumer Res. 36(4):600–610.

Li J, Abbasi A, Cheema A, Abraham LB (2020a) Path to purpose? How online customer journeys differ for hedonic vs. utilitarian purchases. J. Marketing 84(4):127–146.

Li L, Chu W, Langford J, Schapire RE (2010) A contextual-bandit approach to personalized news article recommendation. 19th Conf. World Wide Web (ACM, New York), 661–670.

Li P, Tuzhilin A (2020) Latent unexpected recommendations. ACM Trans. Intelligent Systems Tech. 11(6):1–25.

Li P, Que M, Jiang Z, Hu Y, Tuzhilin A (2020b) PURS: Personalized unexpected recommender system for improving user satisfaction. 14th ACM Conf. RecSys (ACM, New York), 279–288.

Li S, Karatzoglou A, Gentile C (2016) Collaborative filtering bandits Proc. 39th Internat. ACM SIGIR Conf. (ACM, New York) 539–548.

Machado FS, Sinha RK (2007) Smoking cessation: A model of planned vs. actual behavior for time-inconsistent consumers. Marketing Sci. 26(6):834–850.

Maimaran M, Wheeler SC (2008) Circles, squares, and choice: The effect of shape arrays on uniqueness and variety seeking. J. Marketing Res. 45(6):731–740.

McAlister L, Pessemier E (1982) Variety seeking behavior: An interdisciplinary review. J. Consumer Res. 9(3):311–322.

Menon S, Kahn BE (1995) The impact of context on variety seeking in product choices. J. Consumer Res. 22(3):285–295.

Padmanabhan B, Tuzhilin A (1998) A belief-driven method for discovering unexpected patterns. KDD, vol. 98, 94–100.

Panniello U, Gorgoglione M, Tuzhilin A (2016) In CARSs we trust: How context-aware recommendations affect customers’ trust and other business performance measures of recommender sys tems. Inform. Systems Res. 27(1):182–196.

Raju PS (1980) Optimum stimulation level: Its relationship to personality, demographics, and exploratory behavior. J. Consumer Res. 7(3):272–282.

Ratner RK, Kahn BE (2002) The impact of private versus public consumption on variety-seeking behavior. J. Consumer Res. 29(2): 246–257.

Ratner RK, Kahn BE, Kahneman D (1999) Choosing less-preferred experiences for the sake of variety. J. Consumer Res. 26(1):1–15.

Read D, Loewenstein G (1995) Diversification bias: Explaining the discrepancy in variety seeking between combined and separated choices. J. Experiment. Psych. Appl. 1(1):34–39.

Sahoo N, Krishnan R, Duncan G, Callan J (2012) Research note— The halo effect in multicomponent ratings and its implications for recommender systems: The case of Yahoo! movies. Inform. Systems Res. 23(1):231–246.

Sajeesh S, Raju JS (2010) Positioning and pricing in a variety seeking market. Management Sci. 56(6):949–961.

Salakhutdinov R, Hinton G (2009) Semantic hashing. Internat. J. Approximate Reasoning 50(7):969–978.

Schwartz EM, Bradlow ET, Fader PS (2017) Customer acquisition via display advertising using multi-armed bandit experiments. Marketing Sci. 36(4):500–522.

Seetharaman PB (2004) The additive risk model for purchase timing. Marketing Sci. 23(2):234–242.

Seetharaman PB, Che H (2009) Price competition in markets with consumer variety seeking. Marketing Sci. 28(3):516–525.

Senecal S, Nantel J (2004) The influence of online product recommendations on consumers’ online choices. J. Retailing 80(2): 159–169.

Shani G, Gunawardana A (2011) Evaluating recommendation systems. Recommender Systems Handbook (Springer, Boston), 257–297.

Silberschatz A, Tuzhilin A (1996) What makes patterns interesting in knowledge discovery systems. IEEE Trans. Knowledge Data Engrg. 8(6):970–974.

Singh PV, Sahoo N, Mukhopadhyay T (2014) How to attract and retain readers in enterprise blogging? Inform. Systems Res. 25(1): 35–52.

Steenkamp JBEM, Baumgartner H (1992) The role of optimum stimulation level in exploratory consumer behavior. J. Consumer Res. 19(3):434–448.

Tan TF, Netessine S, Hitt L (2017) Is Tom Cruise threatened? An empirical study of the impact of product variety on demand concentration. Inform. Systems Res. 28(3):643–660.

Van Trijp HC, Steenkamp JBE (1992) Consumers’ variety seeking tendency with respect to foods: Measurement and managerial implications. Eur. Rev. Agricultural Econom. 19(2):181–195.

Van Trijp HCM, Hoyer WD, Inman J (1996) Why switch? Product category level explanations for true variety-seeking behavior. J. Marketing Res. 33(3):281–292.

Wang C, Huang Y (2018) “I want to know the answer! Give me fish’n’chips!”: The impact of curiosity on indulgent choice. J. Consumer Res. 44(5):1052–1067.

Woratschek H, Horbel C (2006) Are variety-seekers bad customers? An analysis of the role of recommendations in the service profi chain. J. Relationship Marketing 4(3–4):43–57.

Xu L, Duan JA, Whinston A (2014) Path to purchase: A mutually exciting point process model for online advertising and conversion. Management Sci. 60(6):1392–1412.

Yoon S, Kim HC (2018) Feeling economically stuck: The effect of perceived economic mobility and socioeconomic status on vari ety seeking. J. Consumer Res. 44(5):1141–1156.

Zeithammer R, Thomadsen R (2013) Vertical differentiation with variety-seeking consumers. Management Sci. 59(2):390–401.

Zhang J, Adomavicius G, Gupta A, Ketter W (2020) Consumption and performance: Understanding longitudinal dynamics of recommender systems via an agent-based simulation framework. Inform. Systems Res. 31(1):76–101.

Zhang S, Yao L, Sun A, Tay Y (2019) Deep learning based recommender system: A survey and new perspectives. ACM Comput Surveys 52(1):1–38.

Zhou G, Zhu X, Song C, Fan Y, Zhu H, Ma Y, Yan Y, Jin J, Li H, Gai K (2018) Deep interest network for click-through rate prediction. Proc. 24th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 1059–1068.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
