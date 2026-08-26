---
otero_id: 594
otero_key: "SRACN4B8"
title: "Public decision support for low population density areas: An imbalance-aware hyper-ensemble for spatio-temporal crime prediction"
authors: "Cristina Kadar; Rudolf Maculan; Stefan Feuerriegel"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.03.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Public decision support for low population density areas: An imbalanceaware hyper-ensemble for spatio-temporal crime prediction

![](/api/attachments/SRACN4B8/fulltext/images/985473d81e39825fe6562081159445e62d3091857515c9538e4587f6ed3dacb4.jpg)

Cristina Kadar<sup>⁎,1</sup>, Rudolf Maculan<sup>1</sup>, Stefan Feuerriegel

ETH Zurich, Weinbergstr. 56/58, 8092 Zurich, Switzerland

## A R T I C L E I N F O

Keywords: Crime prediction Machine learning Imbalanced data Spatio-temporal modeling Public decision support

## A B S T R A C T

Crime events are known to reveal spatio-temporal patterns, which can be used for predictive modeling and subsequent decision support. While the focus has hitherto been placed on areas with high population density, we address the challenging undertaking of predicting crime hotspots in regions with low population densities and highly unequally-distributed crime. This results in a severe sparsity (i. e., class imbalance) of the outcome variable, which impedes predictive modeling. To alleviate this, we develop machine learning models for spatiotemporal prediction that are specifically adjusted for an imbalanced distribution of the class labels and test them in an actual setting with state-of-the-art predictors (i. e., socio-economic, geographical, temporal, meteorological, and crime variables in fine resolution). The proposed imbalance-aware hyper-ensemble increases the hit ratio considerably from 18.1% to 24.6% when aiming for the top 5% of hotspots, and from 53.1% to 60.4% when aiming for the top 20% of hotspots. As direct implications, the findings help decision-makers in law enforcement and contribute to public decision support in low population density regions.

## 1. Introduction

Crime inflicts immense financial losses upon individuals, businesses, and organizations, and can even threaten the stability of societies. For instance, according to recent figures from the Federal Bureau of Investigation, annual financial losses due to burglary alone in the United States amount to 3.6 bn USD, with an average cost of 2361 USD per incident.<sup>2</sup> Beyond the financial damage, crime incidents are also known to trigger negative social and psychological efects, since victims sufer from a heightened level of perceived risk, which has been found to result in a significant decrease in the quality of life [11]. Hence, it is the obiective of decision-makers in the private and public sectors to find strategies for efective crime prevention.

In the efort to reduce crime, governments and law enforcement agencies, such as US police departments, have recently started experi menting with techniques for predictive policing in order to optimize the use of resources and to increase the chancesof deterring, as well as preventing, crime events.<sup>3</sup> The term predictive policing refers to the use of predictive analytics with the aim of identifying the potential locations of criminal activity prior to such an event taking place [27]. Formally, this approach draws upon historical records of crime events in order to make spatio-temporal forecasts [4,19].<sup>4</sup> In addition, the predictive models are often extended by further information related to the socio-economic status of the resident population and to nearby points-of-interest (POI) [18,28,33,36,38], basic temporal variables [28,36], or even social media, telecom, or mobility data [3,14,17,33,34], in order to better adapt to the spatio-temporal nature of crime events.

Forecasts from predictive policing improve situational awareness at both the tactical and strategic levels for law enforcement bodies and help them develop strategies for more eficient and efective policing ([23], p. 2). Fig. 1 summarizes the main steps involved in deriving tactical decision support from predictive policing. In doing so, predictive policing is based on the assumption that the presence of police ofers at crime hotspots leads to decreasing crime rates, which has been recently validated in randomized controlled trials [20].

![](/api/attachments/SRACN4B8/fulltext/images/138152c1594d21879670b3daefa869a5dbf058184b53572e92363117d0652cb1.jpg)  
Fig. 1. Schematic illustration of how predictive policing delivers spatial decision support for law enforcement.

Previous research has developed models for crime prediction that target highly populated areas. Examples include cities such as Los Angeles [14], London [3], and Liverpool [4]. Other studies even narrow the focus to individual districts such as the San Fernando Valley in Los Angeles [19]. Yet there is scant evidence that predictive policing can also be applied to areas with lower population density. In fact, prior literature has overlooked sparsely-populated regions, despite the fact that over 50% of household burglaries in the USoccur in such areas.<sup>5</sup> However, this segment of society is currently not benefiting from novel, data-driven techniques for public decision support.

The key contribution of this work is to adapt predictive policing to areas with low population density. The unique features of these regions require extensive modifications to current models used in predictive policing. More specifically, they are characterized by low population densities and crime incidents that are distributed sparsely. In fact, only 0.06% of the total daily observations in our study reflect a crime event. As a consequence, the outcome variable is afected by a severe sparsity, which, in machine learning, is called class imbalance. Due to it, tradi tional approaches to predictive modeling struggle achieving a forecast performance beyond a random vote. As a remedy, we follow recent suggestions for handling class imbalances, and develop a hyper-ensemble for spatio-temporal crime prediction that is specifically suited to an extreme class imbalance and, thus, to low population density areas.

Our evaluation demonstrates the capacity of crime prediction in a real-world, low population density setting. Our results reveal the challenge of forecasting spatio-temporal crime patterns with naïve predictive models, since these outperform the default hit rate of a majority vote by a mere 18.1 percentage points in identifying the top 5% of crime hotspots. To improve the predictive power, we propose a hyper-ensemble that combines the benefits of under-sampling and ensemble learning, thereby modeling decisive relationships between predictors and outcomes even in the presence of sparse crime events and thus extreme class imbalances. As a result, our hyper-ensemble consistently yields considerable performance improvements over common baselines: it increases the hit ratio significantly from 18.1% to 24.6% when aiming for the top 5% of hotspots, and from 53.1% to 60.4% when aiming for the top 20% of hotspots.

Our work entails immediate implications for decision support, especially across the public sector.

This manuscript helps to further develop decision-making in public bodies by incorporating spatial analytics for data-driven decision support. Furthermore, literature commonly studies decision support in high population density regions, while neglecting a major share of the population that lives in areas with lower population density. Here we provide specific levers for translating existing prediction algorithms, such as those used for managing rescue units or trafic flow, to these settings. This is a direct remedy for an acute societal challenge, since sparsely-populated areas already experience lower average incomes and are now additionally excluded from the potential benefits of more

eficient decision-making.

The remainder of this paper is structured as follows. Section 2 reviews theoretical and empirical eforts concerning crime prediction, thereby revealing the dearth of evidence in low population density environments. To close this gap, Section 3 proposes our hyper-ensemble for crime prediction in the case of extreme class imbalance. Its performance is evaluated in Section 4, revealing considerable improvements over traditional predictive models. Section 5 discusses our findings in the context of managerial implications and public decision support, while Section 6 concludes.

## 2. Related work

This section provides a detailed overview of the theoretical foundations, drawn from the field of criminology, based on which we motivate common choices in predictive modeling of crime incidents.

## 2.1. Theoretical foundation

The spatial nature of crime has been subject to extensive theory development. In this regard, under the umbrella of crime pattern theory, individual locations have been categorized according to whether they act as crime generators, crime attractors or crime detractors [5]. For instance, locations where large crowds assemble are supposed to serve as crime generators (e. g., sporting events), while the intrinsic characteristics of others function as crime attractors (e. g., bars)or crime detractors (e. g., police stations). In practice, these patterns can be modeled by the inclusion of POI and other infrastructure characteristics as factors in predictive modeling, an approach that we also follow in our work. In addition,the social disorganization theory [30] and its further ofshoots link crime levels to the ecological attributes of the neighborhood such as socio-economic status, residential stability, and ethnic diversity. This motivates our choice of predictors in order to account for socio-demographic and economic variations among the resident population.

The temporal nature of crime is often theorized to follow two distinct patterns [13]. On the one hand, the concept of repeat victimization proposes that crime events are more likely to occur at locations at which other crime incidents have previously taken place. The reason for the increased risk level originates from the assumption that ofenders are more likely to exploit suitable opportunities further, for example, by stealing objects replaced after the initial theft. On the other hand, near repeat victimization refers to crime events occurring to close proximity of locations of past incidents. Here theory assumes the concept of risk heterogeneity, which states that the only association between one offense and another is the target involved. Since nearby locations of an existing crime scene are more likely to share certain characteristics, such as escape routes or levels of surveillance, it renders them potential locations for further crime in the short run. Theoretical arguments have been proposed for both patterns [16], and we thus take these theories into consideration by incorporating counts of previous crime incidents into our predictive models.

Finally, the characteristics of an environment can inherently change according to climatic and seasonal conditions. A detailed literature review of diferent studies concerning the impact of weather-related variables on crime was performed in [21]. The fact that both violent and property crimes are significantly correlated with major holidays is documented in [10]. These studies have informed our choice of further temporal factors.

## 2.2. Crime prediction

## 2.2.1. Naïve predictions from historic crime data

Early attempts to identify crime hotspots relied upon non-parametric approaches, thus benefiting from simple estimation procedures but neglecting the prognostic capacity of environmental attributes and all associated spatio-temporal dynamics. For instance, the so-called spatial hotspot model applies a simple kernel density estimation to historic crime events in order to locate areas that were previously associated with a higher likelihood of criminal activity [8]. While this approach proved feasible in high population density settings, the disparate and sparse crime events in less populated areas limit its applicability. Nevertheless, historic crime data serves as one of our baselines for determining locations with a high risk of crime. In fact, our empirical results later establish that basic models without theory-informed crime correlates result in inferior performance as compared to models leveraging spatio-temporal predictors.

## 2.2.2. Machine learning models with spatio-temporal predictors

Machine learning allows for the incorporation of crime correlates in order to improve prediction performance. It can thereby accommodate further theories, such as crime pattern theory and social disorganization theory. As a result, a variety of modelsand predictors have been proposed in the literature, which we summarize in the following (see Table 1).

There is considerable variability in terms of model choice. Past studies have quantified the probability of criminal events by means of generalized additive models [36], logistic regression [14,28], gradient boosting [33], neural networks [28], or random forests [3,33]. However, there is no evidence that any one model is consistently superior to all others. A potential reason might be located in the diferent prediction horizons, which can vary from month-ahead predictions [3,36] and bi-weekly crime counts [33] to ranking hotspots on a daily basis [14]. Notably, these works all deal with urban data and thus avoid having to account for class imbalance. Hence, we later experiment with a wide range of models in order to identify a tailored prediction strategy for our research setting.

Numerous spatio-temporal crime correlates have been used as pre dictors, often in a theory-informed manner. Location features inspired by social disorganization theory and crime pattern theory are common and predominantly include socio-demographic variables, infrastructure and POI data [3,18,28,33,36]. To account for (near) repeat victimization, previous crime has been incorporated into the prediction models [14,36]. Further dynamic features refer to seasonal indicators [28], or urban human dynamics extracted from social media, mobility, or telecom data [3,14,17,33].

We adhere to these works and follow an extensive, theory-informed selection of spatio-temporal predictors in our low population setup.

Table 1 summarizes key studies on short-term crime prediction from the literature. We note that all studies restrict the analysis to an area with high population density (a major city or a region of it) and do not consider areas with low population density. Therefore, the novelty of this work is to expand crime prediction to low population density settings, which necessitates our hyper-ensemble, since it can successfully handle extremely imbalanced distributions of crime events.

## 3. Methods and materials

## 3.1. Research framework

Low population density areas are characterized by a strong sparseness of crimes relative to the total number of instances. Such a setting where the predicted variable in machine learning is subject to sparse outcomes is termed class imbalance. That is, the number of in stances from one class outnumbers the number of instances from the other class. In our particular setting, the dependent variable will be zero (=no crime) almost everywhere and only set to one (=crime) in $< 0 . 1 \%$ of cases. This poses a great challenge for identifying the few crime events through common predictive modeling and necessitates a tailored approach to handle such severe class imbalance.

(1.8 times bigger than New York City) and a population density of 4.72 people/ha (seven times less populated than New York City. Key studies on short-term crime prediction (i. e., up to one month as required in tactical setups). The overview shows the dearth of works that target low population density areas. Aargau has a total surface of 140,400 ha

<table><tr><td>Study</td><td>Population density</td><td>Study area</td><td>Spatial resolution</td><td>Temporal resolution</td><td>Features</td><td>Method</td></tr><tr><td>[4]</td><td>High</td><td>Liverpool</td><td>Grid cells of 50 m × 50 m</td><td>2 days/1 week</td><td>Crime</td><td>Prospective hotspot</td></tr><tr><td>[19]</td><td>High</td><td>Part of Los Angeles</td><td>Grid cells of 200 m × 200 m</td><td>1 day</td><td>Crime</td><td>Self-exciting point processes</td></tr><tr><td>[36]</td><td>High</td><td>Charlottesville</td><td>Grid cells of 32 m × 32 m</td><td>1 month</td><td>Crime, spatial</td><td>Spatio-temporal generalized additive model</td></tr><tr><td>[14]</td><td>High</td><td>Los Angeles</td><td>Points at 200 m × 200 m intervals</td><td>1 day</td><td>Crime, social media</td><td>Logistic regression</td></tr><tr><td>[3]</td><td>High</td><td>London metropolitan area</td><td>Lower layer super output areas (geographic hierarchy)</td><td>1 month</td><td>Crime, spatial, telecom</td><td>Random forest</td></tr><tr><td>[28]</td><td>High</td><td>Unnamed city in Belgium</td><td>Grid cells of 200 m × 200 m</td><td>2 weeks</td><td>Crime, spatial, temporal</td><td>Logistic regression, neural network</td></tr><tr><td>[33]</td><td>High</td><td>New York City</td><td>6cmCensus tracts</td><td></td><td></td><td></td></tr><tr><td>(Geographic hierarchy)</td><td>1 week</td><td>Crime, spatial, social media, mobility</td><td>Random forest, gradient boosting, neural network</td><td></td><td></td><td></td></tr><tr><td>This work</td><td>Low</td><td>Swiss canton Aargau (analogous to an US state)</td><td>Grid cells of 200 m × 200 m</td><td>1 day</td><td>Crime, spatial, temporal</td><td>Hyper-ensemble</td></tr></table>

![](/api/attachments/SRACN4B8/fulltext/images/437d5f94945eba19ed296f93dcf3e76fb106ae6efb1bbd3adf13d6cf0ef591bc.jpg)  
Fig. 2. Research framework combining diferent feature sets in order to generate forecasts of crime hotspots based on imbalance-aware machine learning

Only a few studies in the decision support literature have in vestigated prediction in imbalanced datasets, either as a general methodology [26] or for specific application domains such as bank

## 3.2. Methods for imbalance-aware machine learning

## 3.2.1. Proposed hyper-ensemble

Our proposed hyper-ensemble is intended to address the skewed distribution towards one class in the data and the fact that classical over- and under-sampling approaches are likely to miss discriminative information in the data. To address this and give the learning procedure additional structure, our hyper-ensemble is trained on diferent subsamples of the data and the test set results of these models are averaged in a final single prediction, as detailed in Algorithm 1.

Algorithm 1. Hyper-ensemble of random under-sampling models.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
TRAINING PHASE
Require: Given training set  $D_{train}$  and the number of elements in the ensemble ( $\phi$ )
1: for i = 1 to  $\phi$  do:
2: Create balanced sub-sample  $D_{train}^{i}$  of  $D_{train}$  by randomly drawing instances without replacement from the majority class until the same number of instances as in the minority class is reached
3: Train model  $M^{i}$  with sub-sample  $D_{train}^{i}$ 
4: end for
5: return ensemble  $\{M^{1},\ldots,M^{\phi}\}$ 
PREDICTION PHASE
Require: Given an unseen observation x and the ensemble  $\{M^{1},\ldots,M^{\phi}\}$ 
1: for i = 1 to  $\phi$  do:
2: Apply model  $M^{i}$  to x and obtain the predicted probability  $\hat{y}^{i}$ 
3: end for
4: return final probability whether x is labeled as crime or no-crime by averaging over the ensemble, i.e.,  $\hat{y} = \sum_{i=1}^{\phi} \hat{y}^{i}/\phi$
</div>

ruptcy prediction [32]. However, we later see that the traditional approach of over- or under-sampling is not suficient in the case of such an extreme imbalance and, for this reason, we propose an imbalanceaware hyper-ensemble, which performs repeated under-sampling and should thus be more robust in identifying decisive relationships for predictive purposes.

Fig. 2 summarizes our overarching research framework for identifying the most likely times and locations of burglary in a low po pulation density environment. We investigate our proposed hyperensemble, but also experimentwith various resampling strategies and cost-sensitive models as baselines; see the specification in the subsequent sections.

In this way, we combine the two concepts of under-sampling (i. $\boldsymbol { \mathrm { e } } _ { \cdot , \cdot }$ adjusting the class distribution of the data set) and ensemble learning (i. e., strategically generating and combining multiple models) towards a strategy that exploits more information than a standard under-sampling approach and provides additional structure in comparison to a standard over-sampling approach.

## 3.2.2. Baselines

We evaluate our approach against several baselines.

The most basic baseline is that of the majority class classifier – in our case this classifier will always categorize a spatio-temporal unit as no-crime (majority class). The naïve classifier baseline is that of a normal machine learning classifier, where no adjustments were made to account for the class imbalance.

In addition, a cost-sensitive learning model is implemented by proportionally increasing the cost of classification mistakes of the minority class. This classifier is trained on the entire dataset, and is an instantiation of an algorithmic approach to handling class imbalances.

We further experiment with resampling approaches to class imbalance. Random over-sampling achieves a balanced training dataset by randomly duplicating samples from the minority class until the minority class reaches the same number of samples as the majority class. In turn, random under-sampling yields a balanced training dataset by selecting a random subset of the majority class with the same size as the minority class. Heuristic over-sampling is implemented by means of SMOTE [9], where, in order to over-sample the minority class to the size of the majority class, the following algorithm is applied: for each point p in the minority class, choose a random point r among its three nearest neighbors in the same class and create a random point on the line between p and r. Heuristic under-sampling is performed by applying the NearMiss method [39], where, in order to reach class bal ance, those points in the majority class are retained that are closest to their three nearest neighbors in the minority class.

## 3.3. Estimation procedure

Our resampling strategies make no assumptions regarding the underling base learners, giving us the flexibility to experiment with diferent choices. We have evaluated diferent models,<sup>6</sup> including regularized linear models (logistic regression with L1 and L2 regularization, i. e., LASSO and ridge logistic regressions), bagging (random forests), and boosting (AdaBoost). They all return a prob ability score in a binary classification setup, which we can then sort and use to compute top hotspots. We implement all of the aforementioned base learnersbut, for the sake of brevity, we report exhaustively the results of only one classifier, namely the random forest classifier, since it returned best results across diferent specifications in our experiments. This is in line with prior evidence, as random forests are known to return best benchmarking results across a multitude of problems and metrics [7].

We briefly summarize the idea behind the base learners in the following. Random forests are an ensemble learning method for classification, where an entire set of decision trees are grown at training time, and their mode prediction is output at testing time, thus lowering the variance of the individual trees. AdaBoost is also an ensemble model, but instead of averaging the prediction results of decision trees trained in parallel, it trains sequential decision trees, such that each new learner is optimized to correctly classify instances that have been misclassified by the previous learners. The L1 and L2 logistic regressors are simpler (i. e., linear) models with automatic regularization to avoid overfitting.

In all experiments, the dataset is split into 2/3 training data (first two years) and 1/3 testing data (third year). This split specifically maintains the chronological order of the data, simulating a realworld scenario and avoids over-optimistic inference [12,15]. Furthermore, the classifiers are trained in a 5-fold cross validation setup on the training set in which the optimal hyper-parameters are identified, and results are always reported on the test set. Optimized parameters consist of the number and depth of the decision trees for random forest, number of trees and learning rate for AdaBoost, and regularization strength for regularized logistic regressions.

## 3.4. Prediction performance

For predictive policing, a decision-maker is usually interested in how many of the top hotspots were correctly identified. In machine learning, this is referred to as a ranking task. Domain-specific metrics have been proposed in the literature to evaluate spatio-temporal prediction models. The hit rate metric is the percentage of crime cells within a specified time period falling into the areas where crimes are predicted to occur [8] and is defined as hit rate = n/N, where n represents the number of crime areas correctly predicted, and N refers to the total number of crime areas within the studied area.

The second metric with which to compare geographical prediction models is the prediction accuracy index (PAI) and has been utilized in multiple crime studies [1,8,28]. It incorporates a trade-of between the hit rate of the identified hotspots and their relative size: PAI = hit rate/ coverage area. The greater the number of future crime events in a hotspot area that is smaller in size compared to the whole studied area, the higher the PAI value. The metric is controlled by the coverage area parameter, which defines what percentage of the whole area the police would be able to patrol [1] and is defined as coverage area = a/A, where a is the combined area of all predicted hotspots and A is the total studied area. The coverage area could be set by the decision-maker to, e.g., 5%. Therefore, in the results section, we present the metrics under diferent coverage area specifications. The predictions are made on a daily basis and averaged across all days in the test set.

Finally, a surveillance plot depicts the hit rate values y as a function of increasing coverage area values x [14]. The surveillance plot is a powerful tool: if one were to monitor the top x most threatened areas according to the prediction, one would observe approximately y of all crimes. To produce a scalar summary for surveillance curves, we calculate their total area under the curve (AUC) [14].

## 3.5. Data

Our crime dataset consists of burglary incidents in the Swiss canton<sup>7</sup> of Aargau (i. e., analogous to a State in the US) over the course of three years from January 14, 2014 to January 13, 2017. Switzerland has consistently ranked in past several years as one of the top destinations for burglars in Europe.<sup>8</sup> The canton of Aargau fits our definition of a low population area: given a total size of 140,400 ha, it has a total population of approximately 660,000 inhabitants. Highest population densities (16 to 20 people/ha) are achieved only in the cities of Aarau (20,000 inhabitants), Baden (17,500 inhabitants), Brugg (10,000 inhabitants), and Zofingen (10,500 inhabitants), with the majority of the environment being sparsely populated. The overall population density amounts to only 4.72 people/ha.<sup>9</sup>

Each ofense in the provided crime dataset features the exact geolocation, and the reported time period in which the crime was committed.

Fig. 3 presents a heat map of all burglary incidents. We notice that burglary tends to cluster in three more densely populated areas, although incidents occur in less inhabited areas, as well. All burglary incidents span 32.7%of the cantonal built surface.

We preprocess the data such that we only consider cells with built land-use where a burglary is theoretically possible, like residential and industrial areas, and exclude unbuilt land-use, like forests (see the online supplements for details). This filtering process is based on land use data provided by the cantonal geoportal AGIS<sup>10</sup> and yields a final number of 10,149 grid cells that could be matched with a crime time series. Following this step, the average population density of the cells remains low at 15.6 people/ha. This is, for instance, seven times smaller than the average population density in New York City.

![](/api/attachments/SRACN4B8/fulltext/images/68e3994cfe597d7b58a0fe61cbdca6d7edd6b10b0168d47a8337c0c594263e41.jpg)  
Fig. 3. Heat map of burglary incidents over three years in our study setup.

Spatio-temporal data was collected with a spatial resolution of either point-level or in discretized cells of one hectare (100 m × 100 m) from the original data sources. All spatio-temporal features were then aggregated to grid cells of $2 0 0 \mathrm { m } \times 2 0 0$ m with daily resolution. This choice is consistent with leading studies in the literature [14,19,28] and was made jointly with the decision-maker, i. e., the police analyst. It was essential for the decision-maker that the spatial and temporal unit of analysis be kept at low granularity in order for the police to plan efective preventive actions. The final dataset consists of 11,123,304 spatio-temporal observations (=10,149 cells × 1096 days), out of which only 6266 observations are labeled as containing a burglary event. This amounts to only 0.06% of observations of the positive class, highlighting a very severe class imbalance in the dependent variable.

Finally, each outcome crime/non-crime is predicted based on 64 spatio-temporal features grounded in prior criminological research and listed in Table 2. In order account for (near) repeat victimization, we craft four features based on recent crime history in the cell and its neighbors. In order to account for social disorganization theory, we formulate various socio-demographic, economical, and land-use factors from governmental open data (such as AGIS). For crime pattern theory, we exploit other open data platforms (such as OpenStreetMap<sup>11</sup>) in order to describe nearby POI and road infrastructure. Thisamounts to a total of 52 locational features per cell. Lastly, we include eight public features that are predominantly of temporal nature and refer to calendar, weather, and event attributes of the day in each particular cell (from sources such as the Dark Sky $\mathsf { A P I } ^ { 1 2 } ]$ .

## 4. Results

## 4.1. Overall prediction performance

Table 3 evaluates the diferent methods to cope with class imbalance introduced previously. The majority class model (which always predicts no crime) does not manage – by definition – to predict any hotspot. The second baseline, a random forest with no modification, achieves moderate hit rate and PAI scores. Both over-sampling techniques fail to improve upon these scores, and the first imbalanceaware technique that surpasses the baseline methods in most metrics is the heuristic under-sampling approach. It is followed by the cost-sensitive learning and random under-sampling techniques.

The best-performing method across all metrics is the hyper-ensemble. It benefits from the fact that it is trained on ten diferent undersampled subsets. Through its internal model averaging, its average results outperform those of a single classifier trained on an under-sampled subset. When applied to a coverage area of 5%, the hyper-ensemble achieves a hit rate that is 35.9% higher than the naïve baseline. It even surpasses the best baseline (i. e., random under-sampling) by 5.6%. The same pattern is also observed in the PAI scores.

When varying the coverage area, we notice that the hit rate gen erally improves for the models. Notably, our hyper-ensemble model consistently outperforms all baselines. The most eficient PAI is achieved at the 5% level with a value of 4.932.

We utilize a paired t-test in order to assess whether the mean hit rate and PAI results of the hyper-ensemble model are significantly better than the results of the other classifiers. We find that the results of ou method are significantly better than the results of the naïve baseline at all coverage area levels $( p \ : < \ : 0 . 0 0 1 $ ). Furthermore, the hyper-ensemble also significantly outperforms the random under-sampling approach at 10.

## 4.2. Sensitivity of prediction to base learner

We study the sensitivity with regard to diferent specifications of the base learners and find that the above observations, in terms of models and coverage areas, remain robust. Table 4 lists the performance of the two best model specifications (random under-sampling and hyper-ensemble of random under-sampling) with the four diferent base learners introduced in the previous section. We notice relatively similar performance results, whereby the random forest setup wins in most configurations, followed closely by the AdaBoost setup.

## 4.3. Sensitivity of prediction by population density

We study the sensitivity of the prediction performance across different levels of population density in order to understand whether there are specific regions where the model performs better (or worse). For this purpose, we split the dataset according to percentiles of the population density attribute in order to have three separate datasets with a similar number of samples: low population density (popdens < 2.25 residents/hectare), medium population density (2.25 residents/hec tare ≤ popdens ≤ 16.75 residents/hectare), and high population density (popdens > 16.75 residents/hectare). Most crime occurs in the high population density areas (i. e., 1335 incidents), some in areas of medium population density (i. e., 398 incidents), and considerably less in low population density regions (i. e., 151 incidents).

For each subset, a model was trained analogous to the previous experiment. The performance results are listed in Table $^ { 5 , }$ revealing the following key finding: the higher the population density, the better the models are at rankinghigher risk areas. Still, the overall model, having access to all data, achieves the best hit rates and PAI scores. For example, the hit rate score in the overall model outperforms the hit rate in the less populated areas by as much as 134.3% and the hit rate in the more populated areas by 64.0%.

## 4.4. Sensitivity of prediction to temporal resolution

We also study the sensitivity with regard to the temporal resolution, by processing the target variable and the features at weekly granularity.

Theory-informed choice of crime, locational, and temporal features serving as predictors.

<table><tr><td colspan="6">Theory-informed choice of crime, locational, and temporal features serving as predictors.</td></tr><tr><td>Type</td><td>Theory</td><td>Name</td><td>Dimension</td><td>Description</td><td>Source</td></tr><tr><td>Crime</td><td>(Near) Repeat victimization</td><td>prior1d, prior3d, prior7d, prior14d</td><td>Integer</td><td>Number of offenses in the respective and neighboring cells in the past days</td><td>Aargau cantonal police</td></tr><tr><td rowspan="29">Locational</td><td rowspan="14">Social disorganization theory</td><td>popdens</td><td>People/ha</td><td>Density of total residential population</td><td rowspan="8">AGIS: “Statistik der Bevoelkerung auf Hektarbasis”</td></tr><tr><td>popbirth_nonCH</td><td>Percent</td><td>Fraction of residents not born in Switzerland</td></tr><tr><td>popcit_EU, popcit_europ, popcit_noneurop, popcit_CH</td><td>Percent</td><td>Fraction of residents: EU, non-EU European, non-European, or Swiss citizens</td></tr><tr><td>popcit_dividx</td><td>Real between 0 and 1</td><td>Diversity $^{a}$  of citizenship.</td></tr><tr><td>pop_age1, pop_age2, pop_age3, pop_age4</td><td>Percent</td><td>Fraction of residents between 0 and 19, 20–34, 35–64 and 65+ years of age</td></tr><tr><td>popage_dividx</td><td>Real between 0 and 1</td><td>Diversity of age</td></tr><tr><td>popmale</td><td>percent</td><td>Fraction of male residential population</td></tr><tr><td>popstab</td><td>percent</td><td>Fraction of stable residential population</td></tr><tr><td>busidens</td><td>Businesses/ha</td><td>Density of workplaces</td><td rowspan="6">AGIS: “Statistik der Unternehmensstruktur (STATENT) 2013 auf Hektarbasis”</td></tr><tr><td>busi_sec1, busi_sec2, busi_sec3</td><td>Percent</td><td>Fraction of businesses in sectors 1, 2 and 3</td></tr><tr><td>busisec_dividx</td><td>Real between 0 and 1</td><td>Diversity of workplaces with respect to sector</td></tr><tr><td>emplsec_dividx</td><td>Real between 0 and 1</td><td>Diversity of employees with respect to sector</td></tr><tr><td>empldens</td><td>Employees/ha</td><td>Density of employees</td></tr><tr><td>emplmale</td><td>Percent</td><td>Fraction of male employees</td></tr><tr><td rowspan="15">Crime pattern theory</td><td>land_indust, land_park, land_resi1,...</td><td>Percent</td><td>Fraction of land usage: industry, park, residential area with 1 story buildings,...</td><td rowspan="2">AGIS: “Bauzonen Schweiz (harmonisiert) Ausschnitt AG gemaess MGDM”</td></tr><tr><td>land_dividx</td><td>Real between 0 and 1</td><td>Diversity of land use</td></tr><tr><td>buildgs_arefrac</td><td>Percent</td><td>Fraction of area within a grid cell covered by buildings</td><td rowspan="2">AGIS: “Gebaeude ab Uebersichtsplan 1,5000”</td></tr><tr><td>buildgs_dens</td><td>Buildings/ha</td><td>Density of buildings within a grid cell</td></tr><tr><td>poi_infra</td><td>Points/ha</td><td>Density of infrastructural items such as ATMs, post boxes, waste baskets, etc.</td><td rowspan="5">OpenStreetMap Switzerland</td></tr><tr><td>poi_shop</td><td>Points/ha</td><td>Density of shops</td></tr><tr><td>poi_public</td><td>Points/ha</td><td>Density of public buildings such as police stations, hospitals, etc.</td></tr><tr><td>poi_edu</td><td>Points/ha</td><td>Density of educational institutions such as schools, kindergartens, etc.</td></tr><tr><td>poi_gastro</td><td>Points/ha</td><td>Density of gastronomical amenities such as restaurants, bars, etc.</td></tr><tr><td>pub_hous</td><td>Boolean</td><td>Occurrence of a public housing unit in a grid cell</td><td>Bundesamt fuer Wohnungswesen</td></tr><tr><td>highway_exitis</td><td>Boolean</td><td>Occurrence of a highway exit within 5000 m of the grid cell</td><td rowspan="4">AGIS: “Netz Kantons-strassen und Nationalstrassen”</td></tr><tr><td>border_cross</td><td>Boolean</td><td>Occurrence of a border crossing within 5000 m of the grid cell</td></tr><tr><td>road_type</td><td>Category</td><td>Type of a road in the grid cell: from 0 = no road to 3 = high volume road</td></tr><tr><td>intersection</td><td>Boolean</td><td>Occurrence of a major crossroads in the respective or neighboring grid cells</td></tr><tr><td>pub_trans</td><td>Real between 0 and 1</td><td>Quality measure for public transport</td><td>AGIS: “OeV Gueteklassen”</td></tr><tr><td rowspan="8">Temporal</td><td rowspan="8">Climatic and seasonal</td><td>dow</td><td>Encoded</td><td>The day of the week</td><td>-</td></tr><tr><td>holiday</td><td>Boolean</td><td>Indicator of whether there is a public holiday</td><td>feiertagskalender.ch</td></tr><tr><td>temp</td><td>Degree celsius</td><td>Temperature at 12 am</td><td rowspan="5">Darksky API</td></tr><tr><td>hum</td><td>Percent</td><td>Humidity at 12 am</td></tr><tr><td>discomf</td><td>Real</td><td>Discomfort index</td></tr><tr><td>daylight</td><td>Hours</td><td>Hours of daylight</td></tr><tr><td>moon</td><td>Float between 0 and 1</td><td>Moon phase (1 = full moon)</td></tr><tr><td>event</td><td>Integer</td><td>Number of public events on the specific day for the respective cell</td><td>events.ch</td></tr></table>

a Diversity is computed as the normalized Shannon entropy, given all possible categories for the variable, similarly to the approach in [17]. The resulting value lies between 0 (homogenous) and 1 (diverse).

Table 3  
Test set performance comparison of the machine learning methods proposed to cope with class imbalance. All models are trained using random forests as base learners.

<table><tr><td rowspan="2">Classifier</td><td colspan="2">5% Coverage area</td><td colspan="2">10% Coverage area</td><td colspan="2">20% Coverage area</td><td rowspan="2">AUC</td></tr><tr><td>Hit rate</td><td>PAI</td><td>Hit rate</td><td>PAI</td><td>Hit rate</td><td>PAI</td></tr><tr><td>Majority class classifier</td><td>0.0%</td><td>0.000</td><td>0.0%</td><td>0.000</td><td>0.0%</td><td>0.000</td><td>0.000</td></tr><tr><td>Naive classifier</td><td>18.1%</td><td>3.621</td><td>32.5%</td><td>3.249</td><td>53.0%</td><td>2.651</td><td>0.754</td></tr><tr><td>Cost-sensitive learning</td><td>21.0%</td><td>4.186</td><td>36.1%</td><td>3.611</td><td>58.7%</td><td>2.935</td><td>0.769</td></tr><tr><td>Random over-sampling</td><td>15.5%</td><td>3.094</td><td>25.2%</td><td>2.523</td><td>40.8%</td><td>2.040</td><td>0.593</td></tr><tr><td>Random under-sampling</td><td>23.3%</td><td>4.665</td><td>38.4%</td><td>3.840</td><td>59.1%</td><td>2.953</td><td>0.773</td></tr><tr><td>Heuristic over-sampling</td><td>16.2%</td><td>3.252</td><td>26.5%</td><td>2.649</td><td>41.3%</td><td>2.063</td><td>0.590</td></tr><tr><td>Heuristic under-sampling</td><td>12.5%</td><td>2.495</td><td>21.8%</td><td>2.181</td><td>43.2%</td><td>2.159</td><td>0.721</td></tr><tr><td>Hyper-ensemble</td><td>24.6%</td><td>4.932</td><td>40.2%</td><td>4.020</td><td>60.4%</td><td>3.021</td><td>0.779</td></tr></table>

Table 4  
Test set performance comparison of diferent base learners reveals only marginal sensitivity to the choice of the base learner.

<table><tr><td rowspan="2">Classifier</td><td rowspan="2">Base learner</td><td colspan="2">5% Coverage area</td><td colspan="2">10% Coverage area</td><td colspan="2">20% Coverage area</td><td rowspan="2">AUC</td></tr><tr><td>Hit rate</td><td>PAI</td><td>Hit rate</td><td>PAI</td><td>Hit rate</td><td>PAI</td></tr><tr><td>Random under-sampling</td><td>Random forest</td><td>23.3%</td><td>4.665</td><td>38.4%</td><td>3.840</td><td>59.1%</td><td>2.952</td><td>0.773</td></tr><tr><td>Random under-sampling</td><td>AdaBoost</td><td>23.2%</td><td>4.654</td><td>37.7%</td><td>3.771</td><td>58.7%</td><td>2.933</td><td>0.771</td></tr><tr><td>Random under-sampling</td><td>L2 logistic regression</td><td>24.6%</td><td>4.922</td><td>37.1%</td><td>3.712</td><td>57.3%</td><td>2.866</td><td>0.768</td></tr><tr><td>Random under-sampling</td><td>L1 logistic regression</td><td>21.8%</td><td>4.363</td><td>34.1%</td><td>3.407</td><td>54.4%</td><td>2.717</td><td>0.758</td></tr><tr><td>Hyper-ensemble</td><td>Random forest</td><td>24.6%</td><td>4.932</td><td>40.2%</td><td>4.020</td><td>60.4%</td><td>3.021</td><td>0.779</td></tr><tr><td>Hyper-ensemble</td><td>AdaBoost</td><td>23.3%</td><td>4.659</td><td>38.1%</td><td>3.809</td><td>59.2%</td><td>2.959</td><td>0.772</td></tr><tr><td>Hyper-ensemble</td><td>L2 logistic regression</td><td>24.7%</td><td>4.936</td><td>37.3%</td><td>3.731</td><td>57.4%</td><td>2.868</td><td>0.769</td></tr><tr><td>Hyper-ensemble</td><td>L1 logistic regression</td><td>22.1%</td><td>4.414</td><td>34.1%</td><td>3.409</td><td>54.5%</td><td>2.722</td><td>0.758</td></tr></table>

Table 5  
Test set performance comparison of crime, temporal, spatial, and all features across diferent levels of population density. All models are trained using a hyperensemble of random under-sampling with random forests.

<table><tr><td rowspan="2">Population density</td><td rowspan="2">Feature set</td><td colspan="2">5% Coverage area</td><td colspan="2">10% Coverage area</td><td colspan="2">20% Coverage area</td><td rowspan="2">AUC</td></tr><tr><td>Hit rate</td><td>PAI</td><td>Hit rate</td><td>PAI</td><td>Hit rate</td><td>PAI</td></tr><tr><td rowspan="4">All</td><td>Crime</td><td>16.1%</td><td>3.213</td><td>27.4%</td><td>2.743</td><td>39.0%</td><td>1.949</td><td>0.581</td></tr><tr><td>Temporal</td><td>6.5%</td><td>1.292</td><td>12.5%</td><td>1.255</td><td>21.1%</td><td>1.057</td><td>0.498</td></tr><tr><td>Spatial</td><td>23.3%</td><td>4.655</td><td>37.1%</td><td>3.711</td><td>57.2%</td><td>2.860</td><td>0.771</td></tr><tr><td>All</td><td>24.6%</td><td>4.932</td><td>40.2%</td><td>4.020</td><td>60.4%</td><td>3.021</td><td>0.779</td></tr><tr><td rowspan="4">Low population density</td><td>Crime</td><td>4.0%</td><td>0.813</td><td>5.0%</td><td>0.508</td><td>8.0%</td><td>0.402</td><td>0.157</td></tr><tr><td>Temporal</td><td>0.7%</td><td>0.142</td><td>3.8%</td><td>0.385</td><td>6.5%</td><td>0.324</td><td>0.154</td></tr><tr><td>Spatial</td><td>10.5%</td><td>2.096</td><td>15.7%</td><td>1.568</td><td>21.2%</td><td>1.060</td><td>0.251</td></tr><tr><td>All</td><td>10.5%</td><td>2.096</td><td>15.7%</td><td>1.568</td><td>21.2%</td><td>1.060</td><td>0.251</td></tr><tr><td rowspan="4">Medium population density</td><td>Crime</td><td>8.4%</td><td>1.686</td><td>13.6%</td><td>1.357</td><td>20.4%</td><td>1.019</td><td>0.355</td></tr><tr><td>Temporal</td><td>3.1%</td><td>0.623</td><td>7.6%</td><td>0.763</td><td>14.5%</td><td>0.726</td><td>0.327</td></tr><tr><td>Spatial</td><td>14.0%</td><td>2.805</td><td>20.4%</td><td>2.043</td><td>31.5%</td><td>1.572</td><td>0.447</td></tr><tr><td>All</td><td>15.6%</td><td>3.123</td><td>21.5%</td><td>2.156</td><td>29.9%</td><td>1.493</td><td>0.448</td></tr><tr><td rowspan="4">High population density</td><td>Crime</td><td>11.6%</td><td>2.320</td><td>21.9%</td><td>2.185</td><td>35.1%</td><td>1.756</td><td>0.561</td></tr><tr><td>Temporal</td><td>6.0%</td><td>1.199</td><td>11.3%</td><td>1.132</td><td>21.7%</td><td>1.083</td><td>0.486</td></tr><tr><td>Spatial</td><td>15.1%</td><td>3.033</td><td>23.5%</td><td>2.348</td><td>39.2%</td><td>1.960</td><td>0.633</td></tr><tr><td>All</td><td>15.0%</td><td>3.013</td><td>27.2%</td><td>2.721</td><td>41.8%</td><td>2.091</td><td>0.651</td></tr></table>

This yields a dataset of 1,552,797 spatio-temporal observations (=10,149 grid cells × 153 weeks) with a pronounced class imbalance of 0.56% instances belonging to the positive class (i. e., crime). In this scenario, the winning hyper-ensemble of random under-sampling based on random forests achieves a total AUC of 0.844. This corresponds to a hit rate of 51.9% at 5% coverage level, and to a hit rate of 74.4% at 20% coverage level. As such, weekly burglary hotspots prove to be easier to predict as daily burglary hotspots. Yet, daily predictions are desired for tactical decision-making in law enforcement.

## 4.5. Relevance of feature sets

Finally, we perform a direct comparison of the diferent predictor in terms of their predictive power for predictive policing in areas with low population density. We analyze how the prediction performance varies across three subsets of all candidatefeatures: crime features (recent crime history in the area and surroundings), locational features (socio-demographic, land-use, POI and infrastructure factors), and primarily temporal features (calendar, weather, and event attributes). Per Table 5, we conclude that, in all areas, the locational features yield the best predictive results, approaching the results of the models with all features. This highlights the overall importance of both social dis organization theory and crime pattern theory when modeling crime patterns. Second is the model with features inferred from the recent crime incidents in the area, as per insights from (near) repeat victimi zation. The least predictive features turn out to be the temporal features. For instance, when training on samples spanning all popula tion density levels, the model utilizing the complete feature set outperforms the temporal-only setting by 278.5% and the crime-only set ting by 52.8%. These results refer to the hit rate at 5% coverage level, but, as depicted in Fig. 4, the large improvement of the full model against the crime-only baseline holds at all coverage levels.

![](/api/attachments/SRACN4B8/fulltext/images/168c75445ef41128be9e407c7757228dfb060749e60a6bcbfc5d3e3c2c190b8b.jpg)  
Fig. 4. Surveillance plot: hit rate as a function of coverage area when considering diferent feature sets.

When comparing the diferent levels, we observe that, relative to all other zones, the spatial features perform best in the low-density areas, whereas the past crime features perform best in the high-density areas.

## 5. Discussion

## 5.1. Interpretation and link to the literature

This paper establishes the efectiveness of tailored machine learning in terms of identifying places and times of elevated burglary risk in a wide and heterogeneous region with low population density. The su perior performance of the proposed hyper-ensemble can be attributed to two main factors: (1) an innovative strategy that deals with the strong class imbalance by fusing the concepts of under-sampling and ensemble learning, and (2) the incorporation of state-of-the-art spatio temporal predictors of crime into the model.

The results achieved by our approach in a sparsely-populated en vironment are – despite the methodological challenges – on a par with or better than the latest results achieved in densely-populated environ ments, which, to their advantage, do not sufer from severe class imbalance. As an illustration, [1] report a hit rate of 51.5%, i. e., a PAI of 2.57, for burglary in South Chicago, while [14] reports a hit rate of 45.0%, i. e., a PAI of 2.25, for crime in Los Angeles, both at 20% coverage area. Furthermore, [28] report the optimal values of 25.1% for hit rate and 3.95 for PAI, which were achieved at 20% cut-of probability for home burglary in a Belgian city (this translates to approximately 6% coverage area). Hence, our hit rate of 60.4% at 20% coverage area attains a similar performance, despite the more challenging setting of sparsity.

We further investigate whether the predictive performance varies across diferent levels of population density. We find that the presented system performs better in regions with highest levels of population density. This is not surprising, since such areas: (1) experience more crime and thus provide the algorithm with more training examples of the positive class, and (2) coincide with a wider distribution of the features, which allows the algorithm to discover more discriminative patterns.

As crime in less populated areas might not be equally afected by the diferent spatio-temporal factors considered, we discuss the prognostic capacity of the separate crime, spatial, and temporal feature sets. When looking at the whole study area, we find that the high number of spatial features inspired by the social disorganization and crime pattern theories predict crime best. These are followed by recent crime history features crafted according to the (near) repeat victimization phenomena, whilea model trained on temporal features delivers only marginal improvement over the naïve baseline. Most importantly, the additional features describing the environment and time considerably improve the predictive power of the models relying only on crime features.

Diferent patterns emerge when comparing diferent levels of population density. In that case, the importance of past crime features increases with increasing levels of density. For instance, in less populated areas, the model based on locational features based o social disorganization theory and crime pattern theory achieves the same results as the model trained on all features, while the performance of the model based on crime features is inferior by a factor of about 2.5. For more populated areas, the ratio shrinks to about 1.3. This tendency is consistent with the current literature and practices<sup>13</sup> in urban predictive policing, which rely heavilyon insights derived from the notion of (near) repeat victimization.

## 5.2. Implications for management and academia

A number of studies, including randomized controlled trials, have revealed the operative potential of short-term crime prediction models [8,20]. In response, predictive policing solutions, such as PredPol<sup>1</sup> and HunchLab,<sup>14</sup> have been developed and integrated into the daily work of police oficers in several major cities. This has led the National Research Council Committee to review research on police policies and practices, finding strong evidence that taking a focused geographic approach to the problem of crime can increase the efectiveness of policing and could lead to better public decision-making [22]. This renders our work timely and highly relevant. We contribute to this efort by studying areas with low population density that have been overlooked in pre vious research due to the inherent challenges of this undertaking.

Advances in big data and machine learning over the past decade have enabled the implementation of location and non-location analytics in decision support research [25] by utilizing proprietary and open data for diferent applications such as optimizing car-sharing [2,37], predicting crimes [14,33], or preventing trafic accidents [29]. Spatiallyreferenced data that is usually inaccessible has been made available to academic researchers, allowing us to advance the literature on location analytics for spatial decision support in smart cities [24], with an emphasis on under-researched regions with low population density. Furthermore, our study illustrates the successful integration of several existing theories and their innovative application to public decisionmaking.

The tandem of a constant increase in the ubiquity of data, in combination with exponentially advancing computational power, has led to numerous applications of big data analytics in practice. Based on the lessons learned from the digitalization of the private sector, stakeholders in the public sector are now learning how to adapt their processes and services for the 21st century – with police forces representing one example [31]. Hence, the proposed methodology can be directly leveraged by decision-makers in law enforcement, both private (e. g., private security firms) and especially public (e. g., police forces). We provide a fully-fledged approach that can be integrated as a prediction module in a spatial decision support system, as the one presented in Fig. 1. Based on the current available patrolling resources, a decisionmaker can set the maximum coverage area and identify the top crime hotspots.

In the broader sense and inspired by our work, similar approaches utilizing imbalance-aware machine learning techniques can be envi sioned to forecast other sparse spatio-temporal phenomena such as demand for prescriptions, ambulance calls, or 311/911 calls.

## 5.3. Limitations and potential for future research

With the goal of developing a crime prediction approach for areas with low density population, we have leveraged random forests in a hyper-ensemble approach utilizing a super-set of features that have their origins in criminological theory and empirical studies. Although random forests benefit from strong performance in this predictive setup, the resulting decision rules are largely data-driven and thus lack the same interpretability as theory. Hence, they are not the ideal instrument for testing the theoretical contribution of each individual feature – carefully crafted explanatory models and randomized controlled trials would be proper instruments if that objective was desired.

Future research could explore additional methods for highly imbalanced classifications in the domain of unsupervised learning, such as novelty detection and outlier detection. For novelty detection, the training data is not polluted by outliers, andthe interest is on detecting anomalies in new observations.

Another potential avenue for future work consists of hourly crime prediction. The current limitation lies in the fact that burglaries are often discovered only post hoc. Because of that, the actual time of the burglary is unknown and can merely be approximated. With more efort on precise reporting, hourly analyses could further bolster decision support.

While we already worked with an extensive set of features that adheres to best-practice recommendations from prior research, one could potentially investigate the prognostic capacity of further features, such as, e. g., mobility or social media data, in alow population density setting. The current limitation for these datasets is their extreme sparsity in areas with low population density, making their application unfeasible at the moment. Though with the proliferation of locationbased services, this might be worth revisiting in the future. In addition to expanding the feature set, it would be interesting to evaluate the presented features with respect to other types of crimes, such as theft or assaults.

## 6. Conclusion

The aim of this work was to explore the potential of predictive policing in a low population density setting. While areas with high population density have been subject to extensive research, decision support for law enforcement that is designed for less populated areas and their unique characteristics is scarce. Our results have demon strated the successful application of imbalance-aware machine learning techniques to the task of building a ranking system that identifies re gions and times of elevated burglary risk in a large, heterogeneous area. One of the major challenges in the prediction setup is the sparse nature of crime, which is commonly referred to as a severe class imbalance. In our study, it is coped with by proposing a hyper-ensemble that com bines under-sampling and ensemble learning in an efective strategy. This approach outperforms traditional techniques based on (heuristic) under- and over-sampling, as well as cost-sensitive learning. By incorporating various spatio-temporal crime-correlating factors into the model, we significantly improve upon the predictive performance of models that rely solely on past crime data. When dividing the study area according to three diferent levels of population density, we notice an increase in predictive performance in areas with higher population densities. We conclude that the proposed approach can be useful for areas with low population density, which up to now have been ne glected within the domain of crime forecasting.

## Appendix A. Supplementary material

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.dss.2019.03.001.

## References

[1] M. Adepeju, G. Rosser, T. Cheng, Novel evaluation metrics for sparse spatio-temporal point process hotspot predictions - a crime case study, Int. J. Geogr. Inf. Sci. 30 (2016) 2133–2154.

[2] B. Barann, D. Beverungen, O. Müller, An open-data approach for quantifying th potential of taxi ridesharing, Decis. Support. Syst. 99 (2017) 86–95.

[3] A. Bogomolov, B. Lepri, J. Staiano, N. Oliver, F. Pianesi, A. Pentland, Once upon a crime: Towards crime prediction from demographics and mobile data, International Conference on Multimodal Interaction, 2014, pp. 427–434.

[4] K.J. Bowers, S.D. Johnson, K. Pease, Prospective hot-spotting: the future of crime mapping? Br. J. Criminol. 44 (2004) 641–658.

[5] P. Brantingham, P. Brantingham, Criminality of place, Eur. J. Crim. Pol. Res. 3 (1995) 5–26.

[6] D. Canter, T. Cofey, M. Huntley, C. Missen, Predicting serial killers' home base using a decision support system, J. Ouant, Criminol. 16 (2000) 457–478

[7] R. Caruana, A. Niculescu-Mizil, An empirical comparison of supervised learning algorithms, International Conference on Machine Learning, 2006, pp. 161–168.

[8] S. Chainey, L. Tompson, S. Uhlig, The utility of hotspot mapping for predicting spatial patterns of crime, Secur. J. 21 (2008) 4–28.

[9] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, J. Artif. Intell. Res. 16 (2002) 321–357.

[10] E.G. Cohn, J. Rotton, Even criminals take a holiday: instrumental and expressive crimes on major and minor holidays, J. Crim. Just. 31 (2003) 351–360.

[11] B.J. Doran, M.B. Burgess, Why is fear of crime a serious social problem? Putting Fear of Crime on the Map, Springer New York, New York, NY, 2012, pp. 9–23.

[12] JL. Faraway. Does data splitting improve prediction? Stat, Comput. 26 (2016) 49–60.

[13] G. Farrell, K. Pease, Once bitten, twice bitten: repeat victimisation and its implications for crime prevention, Technical Report, Home Ofice Police Department, 1993.

[14] M.S. Gerber. Predicting crime using Twitter and kernel density estimation, Decis Support. Syst. 61 (2014) 115–125.

[15] R. Hirsch, Validation samples, Biometrics 47 (1991) 1193–1194.

[16] S.D. Johnson, Repeat burglary victimisation: a tale of two theories, J. Exp. Criminol. 4 (2008) 215–240

[17] C. Kadar, I. Pletikosa, Mining large-scale human mobility data for long-term crime prediction, EPJ Data Sci. 7 (26) (2018).

[18] C. Kadar, R. Rosés Brüngger, I. Pletikosa, Measuring ambient population from lo cation-based social networks to describe urban crime, Lect. Notes Comput. Sci 10539 (2017).521–535

[19] G.O. Mohler, M.B. Short, P.J. Brantingham, F.P. Schoenberg, G.E. Tita, Self-exciting point process modeling of crime, J. Am. Stat. Assoc. 106 (2011) 100–108.

[20] G.O. Mohler, M.B. Short, S. Malinowski, M. Johnson, G.E. Tita, A.L. Bertozzi, P.J. Brantingham, Randomized controlled field trials of predictive policing, J. Am. Stat, Assoc, 110 (2015) 1399–1411

[21] R. Murataya, D. Gutierrez, Efects of weather on crime, Int. J. Humanit. Soc. Sci. 3 (2013) 71–75.

[22] National Research Council, Fairness and Efectiveness in Policing, Nationa Academies Press, Washington, DC, 2004.

[23] W.L. Perry, B. McInnes, C.C. Price, S.C. Smith, J.S. Hollywood, Predictive policing: the role of crime forecasting in law enforcement operations, Technical Report, Rand Corporation, 2013.

[24] J.B. Pick, Smart cities in the United States and worldwide: a rich arena for MIS studies, J. Inform, Technol, Case Appl, Res. 19 (2017) 133–144

[25] J.B. Pick, O. Turetken, A.V. Deokar, A. Sarkar, Location analytics and decision support: reflections on recent advancements, a research framework, and the path ahead, Decis. Support. Syst. 99 (2017) 1–8.

[26] S. Piri, D. Delen, T. Liu, A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets, Decis, Support, Syst, 106 (2018) 15–29

[27] J. Ratclife, What is the future… of predictive policing? Translational Criminology, 2014 (pp. 4–5).

[28] A. Rummens, W. Hardyns, L. Pauwels, The use of predictive analysis in spatio temporal crime forecasting: building and testing a model in an urban context. Appl Geogr, 86 (2017) 255–261.

[29] B. Ryder, B. Gahr, P. Egolf, A. Dahlinger, F. Wortmann, Preventing trafic accidents with in-vehicle decision support systems - the impact of accident hotspot warnings on driver behaviour, Decis, Support, Syst, 99 (2017) 64–74.

[30] C.R. Shaw, H.D. McKay, Juvenile Delinquency and Urban Areas, University of Chicago Press, Chicago, 1942.

[31] J. Taylor, The digital policing journey: from concept to reality realising the benefits of transformative technology, Technical Report Deloitte, 2015.

[32] D. Veganzones, E. Séverin, An investigation of bankruptcy prediction in imbalanced datasets, Decis. Support. Syst. 112 (2018) 111–124.

[33] L. Vomfell, W.K. Härdle, S. Lessmann, Improving crime count forecasts using Twitter and taxi data, Decision Support Systems, 2018 (forthcoming).

[34] H Wang D Kifer C Graif Z Li Crime rate inference with Big Data Conference or Knowledge Discovery and Data Mining, 2016

[35] T. Wang, C. Rudin, D. Wagner, R. Sevieri, Learning to detect patterns of crime, European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases, 2013, pp. 515–530.

[36] X. Wang, D.E. Brown, The spatio-temporal modeling for criminal incidents, Secur. Informatics 1 (2) (2012).

[37] C. Willing, K. Klemmer, T. Brandt, D. Neumann, Moving in time and space – location intelligence for carsharing decision support, Decis. Support. Syst. 99 (2017) 75–85.

[38] Y. Xue, D.E. Brown, Spatial analysis with preference specification of latent decision makers for criminal event prediction, Decis. Support. Syst. 41 (2006) 560–573.

[39] S.J. Yen, Y.S. Lee, Under-sampling approaches for improving prediction of the minority class in an imbalanced dataset, Lecture Notes in Control and Inform. Sci. 344 (2006) 731–740.

![](/api/attachments/SRACN4B8/fulltext/images/da48da47df6c48b87bb52a6a04ed3aed372caa8c25205eb4d0247427c29b5fc5.jpg)

Cristina Kadar is a PhD candidate at the Chair of Information Management at ETH Zurich with a focus on applied machine learning, information systems, and computational social science. She holds a Master's degree in Software Engineering (with distinction) from Technical University of Munich and a Bachelor's degree Computer Science from Leibniz University of Hanover. She has coauthored publications at top ranked academic conferences in computer science, artificial intelligence, and information systems.

![](/api/attachments/SRACN4B8/fulltext/images/b7a16b09a248e79fa1306c4a2947abe70fa0a0bc0ab51e78e474ddf79df03be3.jpg)

![](/api/attachments/SRACN4B8/fulltext/images/1ab1fb1b28bcd1b625d3939f6730a86f28a641307c49dda3011b7494bf5d5f62.jpg)

Rudolf Maculan holds a Master's degree in Management, Technology and Economics from ETH Zurich, and wrote his master thesis with the Chair of Information Management. Previously, he obtained his B.Sc. in Mechanical Engineering from ETH Zurich and has work experience in the field of automotive connectivity/connected car. His research in terests are in data mining, geospatial information systems and applied machine learning.

Stefan Feuerriegel is an assistant professor for management information systems at ETH Zurich. His research fo cuses on advanced analytics for management decisionmaking, including Bavesian data science, deep learning and spatial analytics. Previously, he worked as a research group leader at the Chair for Information Systems Research University of Freiburg. He has co-authored research publications in the European Journal of Operational Research, the European Journal of Information Systems, the Journal of Information Technology and Decision Support Systems.
