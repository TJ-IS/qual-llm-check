---
otero_id: 19922
otero_key: "K786C8ST"
title: "Incorporating FAT and privacy aware AI modeling approaches into business decision making frameworks"
authors: "Dmitry Zhdanov; Sudip Bhattacharjee; Mikhail A. Bragin"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113715"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Incorporating FAT and privacy aware AI modeling approaches into business decision making frameworks

![](/api/attachments/K786C8ST/fulltext/images/3bb68e729aef09ec762e4e2deb17dd2267011fe4fc030f797c7cc2cacc46f616.jpg)

Dmitry Zhdanov <sup>a,\*</sup>, Sudip Bhattacharjee <sup>b</sup>, Mikhail A. Bragin <sup>c</sup>

<sup>a</sup> J. Mack Robinson College of Business, Georgia State University, Atlanta, GA 30303, USA

<sup>b</sup> School of Business, University of Connecticut, Storrs, CT 06269, USA

<sup>c</sup> School of Engineering, University of Connecticut, Storrs, CT 06269, USA

## A R T I C L E I N F O

Keywords: Explainable AI Fairness Transparency Accountability Responsible computing

## A B S T R A C T

We present a formal approach to build and evaluate AI systems that include principles of Fairness, Accountability and Transparency (FAT), which are extremely important in various domains where AI models are used, yet their utilization in business settings is scant. We develop and instantiate a FAT-based framework with a privacyconstrained dataset and build a model to demonstrate the balance among these 3 dimensions. These princi ples are gaining prominence with higher awareness of privacy and fairness in business and society. Our results indicate that FAT can co-exist in a well-designed system. Our contribution lies in presenting and evaluating a functional, FAT-based machine learning model in an affinity prediction scenario. Contrary to common belief, we show that explainable AI/ML systems need not have a major negative impact on predictive performance. Our approach is applicable in a variety of fields such as insurance, health diagnostics, government funds allocation and other business settings. Our work has broad policy implications as well, by making AI and AI-based decisions more ethical, less controversial, and hence, trustworthy. Our work contributes to emerging AI policy perspective worldwide.

## 1. Introduction

Artificial intelligence (AI) approaches in multiple spheres of human activities – from product recommendation and judicial prediction to cyber intrusion detection and health diagnostics – need to become trusted and accepted by the populations they impact as well as to follow regulations. Most research in AI and machine learning (ML) based sys tems, however, is traditionally focused on system performance and ac curacy while showing a tendency to be “black box” methods (e.g., neural networks), which may be highly precise but difficult to explain and interpret for decision making. Further, such systems may be biased (either via data labels or systemic social biases), and possibly unethical. For example, see mistakes made in predictions by Google Flu [25] and YouTube [32].

New concerns about AI are arising in the context of AI ethics [30]. While we are more willing to trust AI in mapping driving paths for our commute or even in trading stocks, there are scenarios where AI-based decision making presents ethical challenges, e.g. criminal justice. Meant to predict recidivism, profiling systems over-predicted rates of recidivism for Black defendants, leading to questions of fairness in judgments [24]. Similarly, Amazon’s recruiting engine showed bias against women [9]. Lack of transparency in AI-based decision making is often at the core of disputes regarding insurance decisions. States such as Massachusetts, Hawaii and California ban the use of credit-based in surance scores for underwriting, in part due to the lack of transparency [44]. Moreover, with AI making tangible decisions such as in self-driving cars [41], accountability becomes more important.

Therefore, there is an emergent need to include dimensions of Fair ness, Accountability and Transparency (FAT) into AI. This approach is already being reflected in policy space (e.g., EU<sup>1</sup> and Singapore<sup>2</sup>) and corporate responsibility (e.g., Microsoft<sup>3</sup>). Singapore explicitly states that AI should be Fair, Accountable and Transparent. The EU has these three criteria in its list of seven key requirements that AI systems should meet. Therefore, the study of FAT-enabled AI systems is both timely and critical for society in general, and the field of information systems in particular. While there is active research in individual elements of FAT (such as algorithmic bias reduction, explainability of black box models, etc.) there is relatively little systematic work that looks at all three FAT considerations simultaneously. Our research addresses this gap.

In addition, there is an emergent trend to protect an individual’s privacy in machine learning systems – as evidenced by laws such as EU General Data Protection Directive (GDPR) and California Consumer Privacy Act (CCPA). Therefore, data analysis methods used for AI sys tems that use individual level data need to be privacy preserving and may have access to a limited number of attributes to protect privacy.

We develop a framework of a FAT-enabled AI system, and instantiate it in a scenario involving an affinity prediction in a privacy constrained dataset. Our results indicate that all elements of FAT can be balanced in a well-designed system. Our theoretical contribution lies in developing and evaluating a functional FAT-based machine learning method that incorporates all its dimensions, and not a subset, as in existing research. Our framework fulfills the urgent call for explainable models in datadriven decisions and policy analyses. The managerial impact of our work provides more confidence in decision making, with fair, trans parent and accountable AI/ML systems that enhance AI acceptance and trust among decision makers and constituents.

## 2. Background and framework

We base our analysis on the FAT approach to interpretable pre dictions. While all three components of an interpretable prediction need to be present, there is a practical balance between the three that needs to be considered, which occurs in the operationalization of the concepts.

A comprehensive meta-review of Explainable AI by Arrieta et al. [4] present important elements of explainability. These include target au diences of XAI, key concepts, reasons, and purposes for XAI use, resulting in six principles of responsible AI: Fairness, Accountability, Transparency, Privacy, Security, and Ethics. Other research largely ar gues for the need for such an approach, either in AI in general or in specific application areas, but do not address all three FAT dimensions. In addition, we have not found any formal application of the FAT framework in business or information systems research.

Most existing research highlights the need for governance in AI/ML without detailing the specifics of algorithms, and how to accomplish FAT goals. For example, Vollmer et al. [47] argue that “the literature as a whole lacks transparency; clear reporting to facilitate replicability; exploration for potential ethical concerns; and clear demonstration of effectiveness”. Our aim is to bridge this gap specifically in the business context while developing an effective, transparent, and replicable approach to interpretable predictions.

Papers on governance provide guidance on a possible construction of interpretable AI systems, however, none go much into implementation details. Angelov et al. [3] define explainability as an interface between humans and an AI system. Gilpin et al. [15] argue that explanations must be meaningful to the users and gain their trust. Wachter et al. [49] call for precise regulation and audit of inscrutable systems, among others. Gasser and Almeida [13] introduce a layered model of AI governance with a social layer on top of ethical, and then technical layers.

In terms of application areas, the most work in interpretable pre dictions is performed – perhaps unsurprisingly – in health/medicine [1,17,47] and criminal justice [14,38]. There are also emerging ap proaches in the military [45] and education [54].

One cross-cutting concern is the need to provide adequate privacy in AI systems [13,17]. There are two main viewpoints related to algo rithmic privacy: end user and system designer. From the end-user perspective, Park and Shin [34] show that individual privacy concerns may limit trust and acceptance of technology such as AI-based systems. From the designer perspective, Arrieta et al. [4] raise the issue of privacy in the presence of data fusion (where data comes from multiple sources and/or processed by multiple entities). One method of addressing privacy explicitly is to use low-attribute data sets – which both addresses individual user concerns via anonymization and the data fusion con cerns by explicitly blocking additional data sources and elements. We show that our method performs admirably on such datasets without using any external attributes of users.

Several other research explore possible avenues to provide explain ability. A set of work incorporating explainability into algorithms fo cuses essentially on linear methods and transformations – ordinary/ logistic regressions, decision trees, linear optimization, fuzzy inference [18,38]. Our work immediately contributes to this methodological area, as we build our method around generalized linear models. Not only are these models explainable, they are also stable, replicable, and generalizable.

Finally, to measure the dimensions of the FAT framework, most focus on fairness [5,11] – depicted as having some tradeoff with accuracy. The proposed measure of fairness is a disparate impact (e.g., a protected class should have the same distribution of predictions as others). It should be noted that current fairness-enhancing algorithms are not very stable or replicable.

Accuracy measures usually focus on the scoring systems, and use standard ROC-type measures (true positives vs false positives, area under curve, etc. [11,33,38]. For affinity data, MAE and RMSE are commonly used.

Most research does not study three-way FAT balance but focuses on pairwise subsets. For instance, Rudin and Ustun [38] argue that accu racy and fairness are specified as constraints in the optimization prob lem (thus, are pre-set in advance). Shin and Park [42] even argue that transparency and accuracy cannot be measured as these are subjective. We explicitly analyze the three-way FAT balance.

In a very complete treatment of the FAT framework, Shin and Park [42] discuss all three dimensions, along with constituent elements. However, their work is based on a user survey and thus has some pos sibility for confusion – e.g., people expressed accuracy as related to fairness rather than accountability. Their conceptual model has fairness expressed as indiscrimination, impartiality and accuracy; accountability as responsibility, auditability and equity; and transparency as under standability, explainability and observability. We adopt this conceptual approach with some modifications. We develop an algorithmic approach to implement FAT in the form of an iterative decision process, which is described next.

## 3. Modeling approach

Modifying Shin and Park [42], we define FAT as:

i. Fairness: Ensures lack of bias in model prediction. Bias may come from two sources: dataset serving as input (data bias), or internal specification of a model (model bias). Data bias occurs external to the system, but can be partially corrected if recognized, using tools such as over/undersampling, weighted models, etc. Model bias is internal and manifests in unfair influence of model fitting or other procedures on the outcome. Attempts to improve fairness can result in a decrease of performance on accountability and transparency.

ii. Accountability: Has two sub-dimensions – prediction accuracy and coverage. While exact prediction accuracy remains the holy grail, it is seldom achievable. Even small incremental improvement in prediction accuracy requires a disproportionately high increase in computational effort and complexity, leading to brittle models that can fail under slightly different circumstances [16]. In addition, complex models can deter explainability. Therefore, a manager needs to decide on the level of accuracy that is satis factory for business requirements. On the other hand, coverage is defined as the percentage of data points where reliable pre dictions can be computed. Reasons for non-computation of pre diction may include insufficient data, sub-optimal tuning of an algorithm, and interruptions during the computation process. The basic question is whether the system should generate a high number of unreliable predictions or a lower number of high quality predictions, illustrating the tradeoff between coverage and accuracy.

iii. Transparency: Is a function of the modeling method. Some methods are transparent by design – such as linear models where regression coefficients can be interpreted in terms of individual factor contributions to the model result (in absolute terms for classic regression and as ratios for logistic regression). However, there are also “black box” models such as neural nets (NN) – which can compute predictions accurately but cannot succinctly explain the inner logic. Recent interest in NN methods is driven by a troubling quest solely for accuracy [26] and illustrates the tradeoff with transparency. Interestingly, to provide “explain ability” to black box models, computer scientists are falling back on local linear models such as Local Interpretable Model-Agnostic Explanations (LIME; [37]) and Shapley Additive Explanations (SHAP; [27]), complemented with visualizations and other graphical models [8,22,29]

As illustrated above, an interpretable approach to AI-based FAT is gaining attention in several fields. Of particular interest is a set of problems which can be called affinity problems – i.e., a propensity or association relationship between people and certain actions or out comes. Examples in criminal justice include the propensity to commit crime (e.g., COMPAS system), and in healthcare is a propensity to develop a disease (such as diabetes). All FAT dimensions play important roles in these scenarios, as conclusions reached by the AI system need to be actionable, while considering the consequences of decisions made based on AI models.

In business research, such affinity scenarios are traditionally placed in the domain of user behavior prediction and item recommendation. To date, the major focus of such work was solely on accuracy, without much attention to the fairness or transparency of the methods. However, as in criminal justice or healthcare, there are growing calls for these AI sys tems to be acceptable and trusted by users and decision makers. Such acceptance requires addressing all three dimensions of FAT explicitly. Our research is focused on this notion.

Fig. 1 represents an iterative approach to creating fair, accountable and transparent models for business scenarios. The approach begins with the selection of a general modeling method, which usually fulfills the transparency requirement. Some methods such as linear models and decision trees are inherently more transparent than neural networks or matrix decomposition methods. Next, a set of predictors need to be identified based on the specific situation studied. This is a critical requirement in solving a real problem [21], where the focus is not on the development of a method per se, but on finding a workable solution that fits regulatory and policy requirements. These predictors are then computed based on the chosen initial model.

Next, a set of checks are necessary for accountability conditions, where the traditional focus is on creating very good predictions (accu racy) for the desired portion of the dataset (coverage). These two subdimensions of accountability are extensively studied and well under stood. However, accountability also involves model stability (consistent performance with minor changes in underlying data) and replicability (consistent performance on different instantiations of the same prob lem). If accountability thresholds are not met, the model should fail.

If accuracy thresholds are met, the subsequent evaluation deals with model fairness. Fairness minimizes two types of bias – model bias and data bias, as defined above. Dealing with data bias may require a change to the computation of predictors. In our approach, we remove outliers (and check to see their effect on solution metrics), and partition the dataset into relevant subsets for calculation. Dealing with model bias may require re-processing the dataset and repeating computation of predictors with different approaches.

Finally, there is a check for desired transparency. Even though it is largely driven by the initial choice of a modeling approach, transparency may deteriorate in the process of computation and iterative model modifications. Only after all three FAT dimensions are addressed in a satisfactory manner, the model computations stop.

## 4. Modeling method

We present an instantiation of the prediction problem for an affinity dataset and demonstrate how FAT principles can be applied in building explainable AI models. The development of affinity ideas demonstrates attempts to include additional information into the prediction process; however, actual methods and metrics used did not change dramatically in the last decade. The focus has been on calibration of existing methods for a particular scenario: SVD and clustering remain main model-based approaches, and nearest neighbor methods are common in memorybased approaches [57]. Testing and evaluation approaches in affinity modeling are well established, with MAE and RMSE being the most common metrics [46,55]. One growing area of inquiry is the use of neural networks for predictions [6], which is a driving force behind renewed interest in artificial intelligence.

![](/api/attachments/K786C8ST/fulltext/images/2ec0894fab1a5efe463f0797308b7a6728e9ba560ec650e006a17ff2252c4cd8.jpg)  
Fig. 1. Conceptual model of FAT approach.

However, “for artificial intelligence to thrive, it must explain itself” [10]. We focus on building a well-performing and explainable model, without relying on external contextual information. We begin with a discussion of predictors, followed by similarity measures, prediction approach and model calibration.

## 4.1. General approach for affinity models

A typical affinity problem can be presented in terms of two lists: subjects (or users) $U = \{ u _ { 1 } , u _ { 2 , \cdots , u _ { m } } \}$ and objects (or items) $I = \{ i _ { 1 } , i _ { 2 , . . . } ,$ i } [40]. Each subject also has a list of objects $I _ { u i }$ that she has associated with (or rated – this set can be empty). The prediction problem then becomes one of finding a numerical value $P _ { a , j }$ which reflects the pre dicted likeness of the object $i _ { j } \notin I _ { u a }$ for the focal subject $u _ { a }$ on the same scale as the one used to express previous association strength. There are two approaches – memory-based and model-based. In memory-based al gorithms, the prediction is computed based on some weighted measure of the past ratings of the user and the ratings of other users on the item. According to Breese et al. [7], a memory-based prediction can be formally expressed as

$$
P _ {a, j} = \overline {{v}} _ {a} + k \sum_ {i = 1} ^ {n} w (a, i) \left(v _ {i, j} - \overline {{v}} _ {i}\right)
$$

where k is the normalization factor, v are user votes and w are weights that may reflect distance, correlation or another similarity metric be tween the users.

Alternatively, in a model-based algorithm, the prediction is computed as an expected value of a user’s vote based on the prior information about the user. If the votes are cast on an integer scale with range of 1 to m, then the formal expression for the prediction is

$$
P _ {a, j} = E \left(v _ {a, j}\right) = \sum_ {\mathrm{i} = 1} ^ {m} P r \left(v _ {a, j} = i \mid v _ {a, k}, k \in I _ {u _ {a}}\right) * i
$$

Common examples of memory-based approaches include methods using correlation or vector similarity metrics, and model-based ap proaches are exemplified by clustering and Bayesian networks methods [7]. We rely mainly on memory-based techniques, enhanced with model-based ideas, to create a hybrid prediction mechanism, which has gained popularity to surpass individual limitations of both memory based and model-based methods [19,35,50].

## 4.2. Data

The dataset was used in the Netflix Prize contest (which ran in 2006–2009). While the Netflix Prize was focused on accuracy of recommender systems, it completely ignored FAT principles for AI modeling. The outcome of the contest was such that the models from the contest were not useable by Netflix. Hence, we state explicitly that our focus is not in the context of recommender systems, or the Netflix Prize. While the contest provided models with high accountability (accuracy and coverage), those algorithms lacked stability and replicability, and did not address transparency or fairness dimensions at all.

Our approach specifically focuses on the overarching FAT view of interpretable AI and explicitly addresses all features, balancing di mensions of accountability (accuracy, coverage, stability, and replica bility) with the transparency and fairness perspectives. We chose this dataset because it possesses the following features:

\- It incorporates a privacy criterion, as there are no identifiable user or product attributes available for analysis.

\- It has established benchmarks in accuracy – which is one, but not all of the metrics we need to evaluate [31]. Coverage was not reported at all.<sup>4</sup>

We reiterate that our goal is different from replicating or improving Netflix prize algorithms. Our goal is to demonstrate the process of building an explainable AI system which balances accuracy with other dimensions of fairness, transparency and accountability.

The dataset contains 100,480,507 data points spanning approxi mately 7 years. Each tuple has a movie ID, used ID, an actual rating of a movie, and the rating date, and no other attribute. Each movie can be rated only once by a user, effectively creating a unique “movie-user pair”. Hence essentially there are three data elements – user ID, movie ID, and rating date.

Our approach is akin to a statistical estimation, and omits outliers for a statically valid, stable, and robust analysis. Outliers relate to movies with extremely sparse ratings.<sup>5</sup> We utilize Chebyshev’s theorem to include 97% of the data (which lies within six standard deviations<sup>6</sup>). The final dataset size is 97,454,043 data points, with 480,051 users and 8322 movies.

## 4.3. Instantiation of the FAT framework and overview of evaluation

We instantiate the FAT framework presented in Fig. 1, in accordance with the features of the particular problem we study. Fig. 2 represents a view of the FAT framework as it applies to the user/movie affinity problem.

The first decision involves feature extraction. When the number of attributes available for prediction is limited – as in this scenario – it is necessary to identify latent patterns and linkages in the data. In this work, feature extraction is operationalized through data partitioning over some dimension(s) allows for grouping of relevant data points together, thus increasing accuracy while also improving fairness via reduction of data bias. However, the partitioning may have a negative effect on coverage if some important linkages are lost between partitions. We report on our experiments with a varying number of partitions.

The second decision relates to the choice of affinity (distance) metric. Pearson correlation is a conventional measure of similarity. To overcome its limitations, we introduce a modified version of cosine similarity based on the “distance” between vectors/scalars. The choice of affinity metric impacts two aspects of Accountability – coverage of the dataset and accuracy of predictions. Our analysis shows that modified cosine similarity improves coverage without a loss of accuracy, compared to Pearson Correlation.

The third decision relates to the choice of the general modeling approach. The primary evaluation criteria here is transparency, and in many cases, it is binary: the approach is either transparent or not $( \mathrm { i . e . , }$ black box<sup>7</sup>). Examples of non-transparent approaches include neural networks and singular value decomposition (SVD), while linear models are transparent regarding the interpretation of model coefficients. Another issue related to the choice of a modeling approach is stability (a dimension of accountability). For example, SVD is sensitive to minor changes in input data, while linear models are more consistent. Another consideration here is the possibility of introducing model bias, which impacts fairness [12,20,23]. In our analysis, we chose the Generalized Linear Model (GLM) which provides transparency and stability.

Table 1  
![](/api/attachments/K786C8ST/fulltext/images/cb55b6f3693beea4b77716a72b7e22ca9befb1cda6eb8b5eddc3ed83e3c7a4c4.jpg)  
Fig. 2. Instantiation of the FAT framework for affinity modeling.

The final decision involves predictors and parameter optimization. The focus here is on coverage and accuracy as dimensions of account ability; this is also an opportunity to address fairness through data bias, if any. The driving factors here are the depth of search, and specific thresholds on similarity measures. Insufficient depth and strict thresh olds negatively impact coverage, while excessive depth and loose thresholds reduce the accuracy of predictions.

We iteratively calibrate the model to make sure that we achieve acceptable performance in all three dimensions of Fairness, Account ability and Transparency.

## 4.4. Predictors

The choice of predictors is problem specific. This dataset is one of the largest, most complex and privacy preserving datasets available (see above). The objects of the dataset are movies, and the subjects are users of the service, and the affinity relationship takes the form of the rating given to a movie by a specific user. These are the three of four elements in the dataset, the fourth being date of prediction. The task is to accu rately estimate the rating given by a user to a movie, while adhering to FAT principles in a privacy-preserving dataset. Hence, we identify four predictors. (A different problem set can elicit a different set of predictors.)

Following previous research, these predictors are based on “neigh borhood" and “similarity" concepts. The first two predictors. denoted M\_Avg and U\_Avg, estimate the temporal neighborhood behavior of a given movie or user. The third and fourth predictors, M\_Pred and U\_Pred, incorporate the notion of similarity between a movie and others (or a user and others) in a given neighborhood. Each predictor is computed for a given “movie-user-rating date” tuple. The parameters and variables to compute the predictors are listed in Table 1. Appendix A details how the predictors are calculated, and Figs. 3–6 present the al gorithms for computing them.

## 4.5. Similarity measure

Two commonly used similarity measures in prediction problems are Pearson correlation and cosine similarity. Classic cosine correlation $\rho =$

<table><tr><td>Parameter name</td><td>Description</td><td>Used to compute</td></tr><tr><td colspan="3">Model predictors</td></tr><tr><td>M_Avg(m,t)</td><td>Predictor estimating temporal behavior of a movie, henceforth M_Avg</td><td></td></tr><tr><td>U_Avg(u,t)</td><td>Predictor estimating temporal behavior of a user, henceforth U_Avg</td><td></td></tr><tr><td>M_Pred(m,t)</td><td>Neighborhood similarity-based predictor for a movie, henceforth M_Pred</td><td></td></tr><tr><td>U_Pred(u,t)</td><td>Neighborhood similarity-based predictor for a user, henceforth U_Pred</td><td></td></tr><tr><td colspan="3">Model parameters</td></tr><tr><td>C</td><td>Correlation threshold (movies with correlation with target movie below C are not included in the predictor calculation)</td><td>M_Pred</td></tr><tr><td>Dm</td><td>Movie-based depth of history (how far back from the date of prediction do we look for the relevant information)</td><td>M_Avg, M_Pred, U_Pred</td></tr><tr><td>Du</td><td>User-based depth of history (how far back from the date of prediction do we look for the relevant information)</td><td>U_Avg, U_Pred, M_Pred</td></tr><tr><td>R(p)</td><td>Vector of ratings of movie p</td><td>C</td></tr><tr><td>R(q)</td><td>Vector of ratings of movie q</td><td>C</td></tr><tr><td>T_date</td><td>Value of the specific date for the prediction (target) tuple</td><td>All predictors</td></tr><tr><td>T_mid</td><td>Value of the specific movie id for the prediction (target) tuple</td><td>All predictors</td></tr><tr><td>T_uid</td><td>Value of the specific user id for the prediction (target) tuple</td><td>All predictors</td></tr></table>

X∙Y measures cosine of an angle between two vectors. However, experimental results suggest that some adjusted version of cosine simi larity may lead to better predictions, as measured by the reduction in prediction error [40,46]. To match subject or object similarities better, we derive a function that specifically measures the distance between points in the prediction space. We define our modified cosine similarity (MCS) as

![](/api/attachments/K786C8ST/fulltext/images/00b16b5a9139ce2bd10730879d50870afb63b60ac652eda01803b3122904ef31.jpg)  
Fig. 3. Computation algorithm for M\_Avg predictor.

![](/api/attachments/K786C8ST/fulltext/images/9cf99f655b4f8f8eacfd4af51cf071930249e0751161dc88264424fd4900516a.jpg)  
Fig. 4. Computation algorithm for U\_Avg predictor.

![](/api/attachments/K786C8ST/fulltext/images/6652d8592f738f54dbd9ac732d975668b13a376635bbcb08747ecbeb97b707ef.jpg)  
Fig. 5. Computation algorithm for M\_Pred predictor.

$$
M C S = \cos \left(\frac {\sum_ {i = 1} ^ {n} \left| x _ {i} - y _ {i} \right|}{r n} \pi\right),
$$

where r is the range of R(p) and R(q), p and q are two items whose similarity are being measured, vectors R(p) and R(a) are ratings of items p and q respectively, and n is the number of observations. For example, in M\_Pred, we find a similarity of the target movie p to some “compa rable movie” q. In our dataset, $r = 4 ,$ since the theoretical minimum and maximum value of a rating are 1 and 5, respectively; therefore $r = 5 \mathrm { - } 1 =$ 4. Assume $\operatorname { R } ( p ) = ( 5 ; 4 ; 5 ; 3 ; 5 )$ and $\operatorname { R } ( q ) = ( 5 ; 4 ; 4 ; 3 ; 4 )$ , which suggests very similar rating for these two movies p and q. The similarity measure between these two vectors is calculated as:

![](/api/attachments/K786C8ST/fulltext/images/f4cf5075efaabfcf0139c5265f8e285d43c9fa87124f5ac0d965aa88aec245c5.jpg)  
Fig. 6. Computation algorithm for U\_Pred predictor.

$$
M C S = \cos \left(\frac {\sum_ {i = 1} ^ {n} \left| x _ {i} - y _ {i} \right|}{r n} \pi\right) = \cos \left(\frac {\left[ (5 - 5) + (4 - 4) + (5 - 4) + (3 - 3) + (5 - 4) \right] * \pi}{4 * 5}\right) = 0. 9 5 1.
$$

The Pearson correlation for the same set of items is 0.791. It is easy to see that if two movies in a neighborhood receive exactly the same rat ings, then MCS will be equal to cos(0) = 1, and if the movies receive opposite ratings $( \mathrm { i . e . , }$ each time a user rates movie p as 5, she rates movie q as 1), the cosine similarity will be equal to cos(π) = − 1. Thus, our proposed metric is bound in the interval [− 1,1], and captures the dis tance between two rating patterns. The similarity between users is calculated this way as well. Comparatively, MCS performs much better than Pearson correlation in affinity prediction. We omit those results here for brevity.

## 4.6. Generalized Linear Model (GLM)

To improve transparency and explainability of the FAT approach, we choose a GLM formulation on the predictors to build the predictive models (see Step 3 of Fig. 2, and related discussion above). GLM is a very popular predictive tool in diverse fields such as actuarial science [52] and medicine [56], where GLMs as predictive tools have several ad vantages – among those being able to do more with less data, and not being “black box” tools, thus allowing the analyst to clearly understand how each of the predictors influences the prediction. Linear regression, when used in predictive modeling, is orders of magnitude faster, and more accurate for smaller datasets, than neighborhood-based ap proaches [48].

If the data is partitioned in Step 1 (Fig. 2) using certain intrinsic problem criteria. it is inefficient to estimate one single model for all partitions. Arguably, using different model estimations for each of the natural partitions would increase the fit and accuracy of each model. If there are natural sub-partitions that are observed during model esti mation. it would be worthwhile to investigate whether separate models should be estimated for each sub-partition. The overall procedure to estimate the predictive models for each partition is as follows:

• Generate a full set of predictor variables necessary to build a seconddegree generalized linear regression model, including base pre dictors identified above (4 variables), square of each base predictor (4 variables), and pairwise interaction terms (6 variables). Hence, we estimate a model with a total of 14 candidate variables:

Actual rating = f M Pred, U Pred,M Avg,U Avg

• Using the “best subsets” approach, identify the best two models for each size (best models of 2 variables, 3 variables, …, 14 variables). The models which are chosen as “best” have the highest $\mathrm { R } ^ { 2 }$ for their respective sizes: however, it is not the only factor in consideration Model fit can be simply improved by including more variables in the model. However, our aim is for a “best” parsimonious model which functions as well as a full model. This is important, as our focus is on usability and managerially relevant variables.

• Several approaches exist in the literature to identify the best “parsimonious” model – such as adjusted $\mathbb { R } , ^ { 2 }$ Aikake’s information criteria (AIC) and Mallows’ Cp. We use Mallows’ Cp [28], where the “best model” has the lowest Cp value for any given number of vari ables in the model. We examine the output of “best subsets” to find the lowest Cp, which helps to choose the best model size and pre dictors for a given model.

Having identified the “best” model size and composition, we esti mate a GLM for each data partition. The model is then used to predict the movie-user rating for the corresponding holdout subset of this partition, as follows:

Predicted rating = g M Pred, U Pred,M Avg,U Avg .

The difference between the predicted rating and actual rating given by each user is used in the computation of root mean square error (RMSE) – the integrated metric of model performance.

## 5. Results

## 5.1. Dataset partitioning and feature extraction

The dataset size is 97,454,043 data points, with 480,051 users and 8322 movies over 7 years, split into a predictor estimation set (PES) consists of 96,100,127 points and a model generation set (MGS) contains 1,353,916 points. All movies in PES are also present in MGS, yet these are two distinct subsets with respect to “movie-user-rating-date” pairs. We utilize this characteristic to build predictors (Section 4.4) using PES, which comprises 98.6% of the dataset and captures the rich temporal information of the dataset. Using the PES to train the explainable AI model could result in overfitting. Hence MGS is used to train and vali date the prediction model

Partitioning data based on some latent similarity can cluster similar items together and help to build a cogent model of that cluster. Models on similar items can better capture the inherent characteristic of that cluster, and lead to fairness in the models developed. We partition both datasets iteratively to explore the balance between fairness and accountability.

Specific partition boundaries or sizes are not suggested by an algo rithm. This decision needs to be made by a specialist who understands the domain of the problem [53]. Since there were no movie or user at tributes present in the data set, a latent partition of the dataset was undertaken using the number of ratings received by each given movie. Existing research has shown that the number of ratings is highest for items that are either highly popular or controversial, with a drop in the number of ratings for other items [36,39,43]. Wang et al. [51] note that partitioning based on user activity (defined as users who rated a given number of movies) is problematic, as 60% of the users in the dataset gave less than 100 ratings. This would result in incorrect computation of correlations within this group as well as with other users. The distri bution of movie ratings is much more balanced and well behaved. Hence, we choose to partition the dataset on movie ratings. We exper iment with several sets of partitions and observe that while a lower number of partitions created richer neighborhoods for similarity com putations, the resulting computational times were prohibitively expen sive (several weeks). We illustrate our full results with 11 partitions of the overall dataset and show that FAT parameters are stable across different sets of partitions. Analysis of different partition sets is pre sented in Section 5.5.3.

To extract latent features from the data, each of the four predictors is computed for a “movie-user-rating date” tuple present in MGS using data from PES (Figs. 3–6 and Appendix A). PES provides a substantial timeline for each tuple in a partition to be sufficiently represented to compute predictors accurately from the extensive dataset.

## 5.2. Computation of predictors

Partitioning narrows the neighborhood region that is used to compute each predictor. We set some empirically determined neigh borhood criteria to compute each predictor. For example, Fig. 2 shows the input parameter depth of movie history (Dm) for computing M\_Avg. This demonstrates a framework where prediction accuracy, coverage and fairness are adequately balanced for the problem setting and computation environment. For example, the final depth of movie history (Du) for computing M\_Avg is 30 days, while that for U\_Avg is 120 days. A typical movie, for example, receives more ratings in 30 days than a typical user provides. Hence, we find that a neighborhood of 30 days is sufficient to compute M\_Avg, however a larger neighborhood of 120 days is necessary for U\_Avg. Similarly, the correlation cutoff C for M\_Pred is iteratively set at 0.825. This specifies the value of MCS where any vector that is not “similar” is not used as part of the computation, preserving the neighborhood similarity of the computation. Hence our approach balances dataset coverage with a tight neighborhood for each partition.

As a result of the decision of neighborhood criteria, not all predictors are computed for some tuples in each partition. Four sets of outcomes generate a bulk of usable data points – i) all four predictors are computed (labeled NoNulls), ii) only M\_Pred is missing (i.e., not computed due to low number of data points), labeled MPred is Null, iii) only U\_Avg is missing, labeled UAvg is Null, and iv) two predictors are not computed, labeled Two Nulls.

Table 2 presents the predictor generation results, which account for about 81.42% overall coverage of MGS. In other words, our partition and predictor computation approach identifies and predicts four-fifths of all tuples in MGS. It is important to note that full coverage, although ideal and possible, has a tradeoff with fairness, model complexity, and prediction accuracy. For example, a correlation threshold C of 0.825 for M\_Pred leads to 474,236 tuples with missing M\_Pred (Table 2). A lower cutoff value would decrease this number; however it has a significant negative impact on prediction accuracy. Hence our input parameters are designed to balance dataset coverage and prediction accuracy, in addition to a relevant neighborhood.

## 5.3. Generalized Linear Model (GLM) estimation

Next, these predictors are incorporated in a GLM model formulation. MGS is used to train and validate models for each partition, some with all 4 predictors computed, and others with one or more predictors not computed. For each partition, we have 4 sets of tuples with the following characteristics: i) NoNulls, ii) M\_Pred is Null, iii) U\_Avg is Null and iv) Two Nulls. Extending the logic of partitioning, which creates natural clusters of similar tuples, we argue that these 4 sets also exhibit a natural affinity within themselves.

For 11 partitions in MGS, and with 4 sets of tuples in each partition, we estimate 44 different predictive GLM models – one for each of 44 “sub-partitions”. For an “honest” comparison, we split each subpartition into analysis/holdout at 70%–30%, using random sampling.<sup>8</sup> Following the process detailed in Section 4.6, we estimate a GLM with the full set of available predictors to build a second-degree linear regression model, and use the “best subsets” approach to find a most parsimonious model. All but one of the models contain between 3 and 7 variables (out of a possible 14), which illustrates the parsimonious na ture of the approach. Further, we find that U\_Pred, M\_Pred and U\_Avg are “dominant” model variables that are used in at least 19 of the 44 models. Each of these variables are easy to interpret and understand, lending credence to the managerial relevance of the models. The structure of all 44 models is omitted for brevity.

## 5.4. Prediction accuracy

We use the 44 holdout subsets and compute predicted ratings based on the estimated GLMs. Errors are used to compute RMSE by partition and overall. Table 3 presents the prediction accuracy on holdout subsets of MGS. RMSE is an open-ended scale and is difficult to interpret the accuracy of models without a relevant benchmark. For this reason, we use the Cinematch RMSE benchmark provided for this dataset [31].

Overall, prediction accuracy improves as the average number of ratings for a movie increases. For movies with less than 5000 ratings, the predictions are uniformly less accurate, which is not surprising, since items with sparse ratings, in general, do not have good prediction ac curacy. For every partition of a number of movie ratings of 5 k and higher, models with all 4 predictors and that with 3 predictors (UAvg is Null) beats the benchmark, sometimes by a large margin. Models that do not have M\_Pred, or any two predictors, fare poorly.

Table 2  
Dataset coverage for each partition by computed predictors (MCS correlation).

<table><tr><td rowspan="2">Partition name (number of ratings)</td><td rowspan="2">Tuples in model generation set (MGS)</td><td rowspan="2">Tuples in predictor estimation set (PES)</td><td colspan="4">Tuples computed (usable points)</td><td rowspan="2">Total tuples computed</td></tr><tr><td>NoNulls</td><td>MPred is Null</td><td>UAvg is Null</td><td>Two Nulls</td></tr><tr><td>0–5 k</td><td>183,546</td><td>9,638,908</td><td>100,847</td><td>27,283</td><td>10,777</td><td>20,906</td><td>87.07%</td></tr><tr><td>5 k–8 k</td><td>78,343</td><td>4,766,740</td><td>21,475</td><td>24,669</td><td>2707</td><td>14,258</td><td>80.55%</td></tr><tr><td>8 k–15 k</td><td>110,778</td><td>8,784,752</td><td>33,636</td><td>39,669</td><td>3283</td><td>18,749</td><td>86.06%</td></tr><tr><td>15 k–20 k</td><td>78,020</td><td>5,187,763</td><td>15,623</td><td>30,029</td><td>1605</td><td>15,991</td><td>81.07%</td></tr><tr><td>20 k–30 k</td><td>122,280</td><td>9,455,830</td><td>31,322</td><td>49,516</td><td>2767</td><td>20,566</td><td>85.19%</td></tr><tr><td>30 k–35 k</td><td>53,651</td><td>4,196,956</td><td>6814</td><td>20,561</td><td>1106</td><td>12,254</td><td>75.93%</td></tr><tr><td>35 k–50 k</td><td>148,942</td><td>10,089,627</td><td>43,501</td><td>58,215</td><td>4223</td><td>23,891</td><td>87.17%</td></tr><tr><td>50 k–65 k</td><td>102,307</td><td>8,267,276</td><td>13,492</td><td>49,525</td><td>1371</td><td>19,460</td><td>81.96%</td></tr><tr><td>65 k–90 k</td><td>132,582</td><td>11,773,215</td><td>25,789</td><td>51,272</td><td>3141</td><td>22,587</td><td>77.53%</td></tr><tr><td>90 k–120 k</td><td>188,001</td><td>11,594,361</td><td>31,494</td><td>85,261</td><td>3283</td><td>32,276</td><td>81.02%</td></tr><tr><td>120 k–230 k</td><td>155,466</td><td>12,344,699</td><td>37,307</td><td>38,236</td><td>6099</td><td>25,457</td><td>68.89%</td></tr><tr><td>Overall:</td><td>1,353,916</td><td>9,638,908</td><td>361,300</td><td>474,236</td><td>40,362</td><td>226,395</td><td>81.42%</td></tr></table>

Table 3  
Prediction accuracy and model comparison in each sub-partition (MCS corr.)

<table><tr><td rowspan="2">Partition name</td><td colspan="4">RMSE by category</td><td colspan="4">Improvement vs. baseline</td></tr><tr><td>NoNulls</td><td>Mpred is Null</td><td>UAvg is Null</td><td>Two Nulls</td><td>NoNulls</td><td>Mpred is Null</td><td>UAvg is Null</td><td>Two Nulls</td></tr><tr><td>0–5 K</td><td>0.96538</td><td>1.09314</td><td>1.06281</td><td>1.10301</td><td>-1.35%</td><td>-14.77%</td><td>-11.58%</td><td>-15.80%</td></tr><tr><td>5 k–8 k</td><td>0.87605</td><td>1.02449</td><td>0.96075</td><td>1.05708</td><td>8.03%</td><td>-7.56%</td><td>-0.87%</td><td>-10.98%</td></tr><tr><td>8 k–15 k</td><td>0.85872</td><td>1.02496</td><td>0.94349</td><td>1.06114</td><td>9.85%</td><td>-7.61%</td><td>0.95%</td><td>-11.41%</td></tr><tr><td>15 k–20 k</td><td>0.85800</td><td>1.00883</td><td>0.86723</td><td>1.04775</td><td>9.92%</td><td>-5.91%</td><td>8.95%</td><td>-10.00%</td></tr><tr><td>20 k–30 k</td><td>0.83639</td><td>1.01462</td><td>0.94041</td><td>1.05338</td><td>12.19%</td><td>-6.52%</td><td>1.27%</td><td>-10.59%</td></tr><tr><td>30 k–35 k</td><td>0.83692</td><td>1.01234</td><td>0.91943</td><td>1.03112</td><td>12.13%</td><td>-6.28%</td><td>3.47%</td><td>-8.25%</td></tr><tr><td>35 k–50 k</td><td>0.83642</td><td>0.99528</td><td>0.87460</td><td>1.03551</td><td>12.19%</td><td>-4.49%</td><td>8.18%</td><td>-8.72%</td></tr><tr><td>50 k–65 k</td><td>0.82247</td><td>1.0222</td><td>0.90966</td><td>1.06220</td><td>13.65%</td><td>-7.32%</td><td>4.50%</td><td>-11.52%</td></tr><tr><td>65 k–90 k</td><td>0.82902</td><td>1.00113</td><td>0.82462</td><td>1.0283</td><td>12.96%</td><td>-5.11%</td><td>13.43%</td><td>-7.96%</td></tr><tr><td>90 k–120 k</td><td>0.81993</td><td>1.03242</td><td>0.87815</td><td>1.04464</td><td>13.92%</td><td>-8.39%</td><td>7.81%</td><td>-9.67%</td></tr><tr><td>120 k–230 k</td><td>0.82260</td><td>1.00008</td><td>0.87337</td><td>1.00571</td><td>13.64%</td><td>-5.00%</td><td>8.31%</td><td>-5.59%</td></tr><tr><td>Overall</td><td></td><td></td><td></td><td></td><td>8.08%</td><td>-7.01%</td><td>1.14%</td><td>-9.95%</td></tr></table>

A deeper look at sub-partitions, where all predictors are computed, shows our model handily beats the original benchmark of the dataset (identified earlier) by 8–14% in all other partitions, with an improve ment in prediction accuracy of over 12% for movies with more than 20,000 ratings (Table 3). For movies with 5000 to 20,000 ratings, there is a prediction improvement between 8.03% and 9.92%, which is impressive considering the simplicity of the model.

Table 3 also suggests that M\_Pred is possibly the most critical pre dictor here. All tuples where M\_Pred is Null have prediction accuracy below the benchmark. Since M\_Pred measures the hidden commonal ities between a target movie and others, it is imperative to understand such linkages between items. For movies, such commonalities can include genre, artists, directors, and other measures. It is common practice to incorporate such external data; however, we do not add those to preserve the data privacy in our approach.

The average user rating (U\_Avg) is also an important predictor and has varying impact across sub-partitions. Missing U\_Avg has a more pronounced negative impact in movies with smaller number of ratings (0-15 k), where it does not beat the benchmark. Without U\_Avg, there is 8.95% improvement over the benchmark for movies for a narrow neighborhood of 15 k–20 k ratings. There is also more than 8–13% improvement in partitions 35 k–50 k, 65 k–90 k and 120 k–230 k, which all have significantly larger neighborhoods.

Table 3 shows that a significant number of our models in several partitions beat the benchmark, and models with all four predictors (NoNulls) achieve commendable improvement of 8–14% over the benchmark for almost all partitions (except 0-5 k). This demonstrates the overall power and accuracy of our framework to predict a large dataset without any external augmentation while using a simple parsi monious modeling approach that is interpretable. It also demonstrates the stability of the prediction accuracy over multiple types of latent partitions of the data, which signify item cohesiveness.

## 5.5. Evaluation of FAT components

The results here evaluate accountability (accuracy of predictions vs coverage of the dataset) and fairness (data bias impact). Transparency is addressed explicitly at the modeling method choice stage. The complexity of the overall model, in terms of a number of variables, is also indicative of transparency. The model input parameters were held constant across partitions to enable us to study the intrinsic differences of the properties of each partition.

## 5.5.1. Evaluating accountability

Table 4 lists the relative ranks of coverage and accuracy for different data partition sizes. We do not find a dominant pattern between the

## Table 4

Balancing accuracy and coverage.

<table><tr><td rowspan="2">Partition name</td><td rowspan="2">Coverage rank</td><td colspan="4">Rank of prediction accuracy</td></tr><tr><td>NoNulls</td><td>Mpred is Null</td><td>UAvg is Null</td><td>Two Nulls</td></tr><tr><td>0–5 k</td><td>2</td><td>11</td><td>11</td><td>11</td><td>11</td></tr><tr><td>5 k–8 k</td><td>8</td><td>10</td><td>8</td><td>10</td><td>8</td></tr><tr><td>8 k–15 k</td><td>3</td><td>9</td><td>9</td><td>9</td><td>9</td></tr><tr><td>15 k–20 k</td><td>6</td><td>8</td><td>4</td><td>2</td><td>6</td></tr><tr><td>20 k–30 k</td><td>4</td><td>6</td><td>6</td><td>8</td><td>7</td></tr><tr><td>30 k–35 k</td><td>10</td><td>7</td><td>5</td><td>7</td><td>3</td></tr><tr><td>35 k–50 k</td><td>1</td><td>5</td><td>1</td><td>4</td><td>4</td></tr><tr><td>50 k–65 k</td><td>5</td><td>2</td><td>7</td><td>6</td><td>10</td></tr><tr><td>65 k–90 k</td><td>9</td><td>4</td><td>3</td><td>1</td><td>2</td></tr><tr><td>90 k–120 k</td><td>7</td><td>1</td><td>10</td><td>5</td><td>5</td></tr><tr><td>120 k–230 k</td><td>11</td><td>3</td><td>2</td><td>3</td><td>1</td></tr></table>

accountability goals of coverage and accuracy. Statistically, there is no significant correlation between any pair of these goals. Since the input parameters are fixed at the global level, any potential dominance in performance would be a consequence of the inherent attributes of the partition. Since we do not observe any dominant relationship between partitions, we conclude that our methodological framework is balanced and suitable for a wide variety of partitions and intrinsic product characteristics.

As discussed above, if significant coverage is a dominant goal here, the model input parameters can be modified to achieve it, with the understanding that other goals may be sacrificed in the process. This demonstrates the necessity of expert managerial inputs in determining the bounds of such goals, and the flexibility of our framework.

## 5.5.2. Evaluating transparency

As Table 5 illustrates, our predictive models across all partitions utilize between 3 and 7 variables, with a solitary exception. These re sults highlight the parsimonious nature of the decision support param eters from our models that can be managerially acted upon within a bounded rationality framework. A low number of variables involved in the models facilitates the goal of transparency and explainability in de cision making. Further, our ability to understand the impact of each predictor variable on accuracy and coverage is another function of transparency.

## 5.5.3. Evaluating fairness

To evaluate fairness (data bias), we perform iterations of Sections 5.1–5.4 with successively increasing partition sizes, and report 3 cases involving 4, 6 and 11 partitions. For consistency, we iteratively combine or split partitions together, resulting in the following configurations: 4 partitions – 0-15 K, 15 k-35 K, 35 K–90 K and 90-230 K; and 6 partitions – 0-5 K, 5 K–15 K, 15 K–30 K, 30 K–50 K, 50 K–90 K and 90 K–230 K. Table 6 presents the performance comparison in terms of accuracy as the number of partitions vary. The general performance structure does not change – No Nulls case is easiest to predict across the board, followed by UAvg is Null, MPred is Null, and Two Nulls, respectively. Regardless of the scale of partitions, our results are stable and consistent across FAT pa rameters. Therefore, our framework is robust to the number of partitions (data bias) and demonstrates fairness in the framework.

For increasing partition sizes, while accuracy stays between a narrow range of 7.52–8.55% for NoNulls, and –1.84-2.73% for UAyg is Null, it increases monotonically from − 14.36% to − 9.95% for Two Nulls. There is no uniform “best” set of partitions regarding accuracy. 6 partitions produced the best results in No Nulls and UAvg is Null scenarios, while 11 partitions were better in MPred is Null and Two Nulls situations. Inter estingly, 4 partitions produced the worst results across the board. We conclude that partitioning of large datasets into finer segments help improve prediction accuracy, which indirectly points to increasing fairness across diverse segments of items. The most likely reason is the presence of non-similar data in large datasets, which can lead to worse models and reduce the accuracy of point predictions. Partitioning uti lizes the latent differences among movies and filters out noise from unrelated movies.

Table 5  
Parsimonious models leading to transparency.

<table><tr><td rowspan="2">Partition name</td><td colspan="4">Number of variables in GLM</td></tr><tr><td>NoNulls</td><td>Mpred is Null</td><td>UAvg is Null</td><td>Two Nulls</td></tr><tr><td>0–5 k</td><td>12</td><td>4</td><td>5</td><td>4</td></tr><tr><td>5 k–8 k</td><td>6</td><td>7</td><td>6</td><td>4</td></tr><tr><td>8 k–15 k</td><td>7</td><td>7</td><td>4</td><td>4</td></tr><tr><td>15 k–20 k</td><td>7</td><td>7</td><td>3</td><td>3</td></tr><tr><td>20 k–30 k</td><td>7</td><td>7</td><td>3</td><td>4</td></tr><tr><td>30 k–35 k</td><td>7</td><td>7</td><td>3</td><td>4</td></tr><tr><td>35 k–50 k</td><td>7</td><td>7</td><td>3</td><td>4</td></tr><tr><td>50 k–65 k</td><td>6</td><td>7</td><td>3</td><td>5</td></tr><tr><td>65 k–90 k</td><td>7</td><td>7</td><td>3</td><td>4</td></tr><tr><td>90 k–120 k</td><td>6</td><td>7</td><td>3</td><td>4</td></tr><tr><td>120 k–230 k</td><td>7</td><td>4</td><td>6</td><td>4</td></tr></table>

Table 6  
Accuracy comparisons based on the number of partitions (vs benchmark).

<table><tr><td>Partition count</td><td>NoNulls</td><td>Mpred is Null</td><td>UAvg is Null</td><td>Two Nulls</td></tr><tr><td>4 partitions</td><td>7.52%</td><td>-9.69%</td><td>-1.84%</td><td>-14.36%</td></tr><tr><td>6 partitions</td><td>8.55%</td><td>-8.31%</td><td>2.73%</td><td>-11.32%</td></tr><tr><td>11 partitions</td><td>8.08%</td><td>-7.01%</td><td>1.14%</td><td>-9.95%</td></tr></table>

## 5.5.4. Balancing FAT dimensions

While model accuracy is improved with more partitions, coverage suffers predictably. The 11-partition solution resulted in coverage of 81.42% (in terms of computed data points), a 6-partition solution pro duced coverage of 86.03% and a 4-partition model produced coverage of 88.21%. This reinforces the tradeoff between coverage and accuracy. It is a business decision to either accept a large number of middling pre dictions or a smaller number of good predictions.

In terms of the structure of the predictors used for GLM in different partition sizes, results are qualitatively similar to those in Table 5. Both in a 6-partition and a 4-partition situation, the number of predictors was between 3 and 7, with one very sparse case using 11 predictors. The variation in partition counts did not impact the variable structure.

Table 7 summarizes the overall performance of our method. All three goals of Fairness, Accountability and Transparency are achieved. Trans parency is present as the result of our choice of an interpretable model. Accountability is evident in terms of comparable performance to the benchmark, while covering over 80% of the dataset and maintaining model stability. Fairness is demonstrated by the fact that despite a varying number and size of partitions, the predictive performance be tween these scenarios is very similar. Even partitioning by latent fea tures/demographics/classes/other dimensions, which are important determinants of fairness, our framework shows consistent results for fairness.

To increase Accountability (either accuracy or coverage), a black-box model instead of GLM may be needed, thus reducing Transparency. Increasing the number of partitions increases inherent fairness but de creases coverage (accountability). Hence, a FAT-based AI system can achieve all three goals. In summary, the choice of the specific configu ration for the FAT framework instantiation should be driven by the specific predictive tasks and goals.

## 6. Discussion and conclusion

We present a systematic framework to build and evaluate explain able AI systems, building on emergent conceptual foundations ([4,42], and others). We discuss an approach to AI explainability which includes the dimensions of Fairness, Accountability and Transparency (FAT). We then instantiate a FAT-based framework in an affinity prediction sce nario with a privacy-constrained dataset. Our results indicate that FAT principles can co-exist in a well-designed system without major loss of any one factor.

Our theoretical contribution lies in presenting and evaluating a functional, FAT-based machine learning method. Contrary to common belief, we show that the explainability of AI/ML systems does not need to have a major negative impact on predictive performance. Our modeling approach is rigorous and detailed.

Table 7  
Evaluation of performance in relation to FAT framework.

<table><tr><td colspan="3">Accountability</td><td>Fairness</td><td>Transparency</td></tr><tr><td>Accuracy (RMSE vs benchmark)</td><td>Coverage</td><td>Stability</td><td># Partitions</td><td>Model for prediction</td></tr><tr><td>0.9834 (-3.25%)</td><td>88.21%</td><td>Yes</td><td>4</td><td>Yes</td></tr><tr><td>0.9719 (-2.04%)</td><td>86.03%</td><td>Yes</td><td>6</td><td>Yes</td></tr><tr><td>0.9777 (-2.65%)</td><td>81.42%</td><td>Yes</td><td>11</td><td>Yes</td></tr></table>

Our framework fulfills the urgent call for explainable models in the data-driven decision and policy analysis space. While accuracy is important, fairness, accountability and transparency have seen increasing priority in many critically important business and policy contexts, such as healthcare, criminal justice, population forecasts, and fiduciary duty, where reputation, well-being or even lives are at stake from each individual decision. In many domains, the accuracy of a model is not enough – the inner workings of such complex models are mandated to be transparent. In our case, the explainable and transparent approach allows us to understand the relative importance of the pre dictors. Dataset coverage and model stability establish accountability, while consistency across different partitions demonstrates the fairness of the modeling approach and outcome.

Acceptance of AI models is low in decision and policy making circles – reinforcing the need for explainability and transparency. The chal lenge increases with privacy-preserving datasets, which can hinder ac curate and fair model building and assessment. Our work provides a path forward, through the development of an explainable model on a low-attribute dataset, using ML approaches that preserve accuracy, and is transparent and reliable for decision making.

The managerial impact of our work provides more confidence in decisions, especially when individual decision-making responsibility is present. By demonstrating that an AI/ML system can be fair, trans parent, and accountable, we can foster success with AI system accep tance and trust – both from decision makers and constituents impacted by such decisions. Our approach has applications in a variety of fields from criminal justice to insurance, and government funds allocation to healthcare, and beyond.

Our work has broader policy implications as well, by making AI and AI-based decisions more open, ethical, and hence less controversial. Our work aligns with emerging policy perspectives in governance such as in the EU and Singapore, which continues to grow worldwide.

We instantiated and tested the FAT framework in a scenario of af finity predictions. By its very nature, any general approach needs to be customized to a specific problem domain and data configuration. Some metrics of Fairness, Accountability and Transparency, as well as the pro cess of model calibration, will be necessarily different in areas such as text, image, or geolocation analytics. However, our general framework can be successfully applied to these diverse problem spaces. We look forward to researchers continuing exploration of FAT-based AI/ML systems across a variety of societal and business scenarios.

## Appendix A. Example of predictor calculation

Computing U\_Pred:

For movies, we generally obtain substantially more “comparable movies” – thus averaging out is acceptable. For users, we usually get lower number of “comparative users”. We are trying to build a model of “identical twin” (with Correlation =1) using regression. This is similar to the use of “Slope One” method (Lemire, D., & Maclachlan, A. (2005). Slope One Predictors for Online Rating-Based Collaborative Filtering. SDM.) – which is efficient and reasonably accurate.

The process for computing M\_Pred is as follows:

1. Start with the tuple we need to predict (movieID, userID, date).

2. Since prediction is to be done on the movie basis, we start by fixing the target user (userID = T\_uid)

3. Find which other movies were rated by T\_uid, result is “comparable movies list”.

4. For these movies, find which other users provided ratings, resulting in “user list”. Note that this list will be quite extensive.

5. Filter out “user list” by checking which of them actually rated the target movie. For those relevant users, collect how they rated the target movie.

6. Correlate the ratings of target user and other relevant users based on common ratings they give to comparable movies.

7. Make the prediction for the target movie based on a) how relevant users have rated it and b) correlation coefficient for the target user.

Consider the following simplified example:

We need to predict a rating for movie A by user X on a date D.

\- Find which other movies were rated by user X. Suppose there are only movies B and C.

\- Find which users also rated movies B and C within time frame based on D. Suppose there are users Y and Z.

\- Check whether Y and Z have rated movie A. Suppose Y did and Z did not. Drop user Z from consideration.

\- Compare ratings of user X vs Y given to movies B and C. Suppose user X rated both as 5 and user Y rated both as 1. Cosine correlation be tween these two users equals − 1.

\- Suppose user Y rated movie A as 5. To make the needed prediction (X - > A), take a known prediction of Y and adjust for the correlation coefficient. Since Y liked move A very much and they have opposite tastes to X, we predict that X will rate movie A as 1.

## References

[1] A. Abdul, J. Vermeulen, D. Wang, B. Lim, M. Kankanhalli, Trends and trajectories for explainable, accountable and intelligible systems: an HCI research agenda, in: Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems. 2018, pp. 1–18.

[2] G. Adomavicius, A. Gupta, D. Zhdanov, Designing intelligent software agents for auctions with limited information feedback, Inf. Syst. Res. 20 (4) (2009) 507–526.

[3] P.P. Angelov, E.A. Soares, R. Jiang, N.I. Arnold, P.M. Atkinson, Explainable artificial intelligence: an analytical review, Wiley Interdiscip. Rev. Data Min. Knowl. Discov. 11 (5) (2021), e1424.

[4] A.B. Arrieta, N. Díaz-Rodríguez, J. Del Ser, A. Bennetot, S. Tabik, A. Barbado, S. Garcia. S. Gil-Lopez. D. Molina. R. Beniamins. R. Chatila. E. Herrera. Explainable artificial intelligence (XAI): concepts, taxonomies, opportunities and challenges toward responsible AL. Inf, Fusion 58 (2020) 82–115

[5] R. Bellamy, K. Dey, M. Hind, S. Hoffman, S. Houde, K. Kannan, P. Lohia, J. Martino, S. Mehta, A. Mojsilovic, S. Nagar, K. Ramamurthy, J. Richards, D. Saha, P. Sattigeri, M. Singh, K. Varshney, Y. Zhang, AI fairness 360: an extensible toolkit for detecting and mitigating algorithmic bias, IBM J. Res. Dev. 63 (4/5) (2019), pp. 4:1-4:15.

[6] A. Beutel, P. Covington, S. Jain, C. Xu, J. Li, V. Gatto, E. Chi, Latent cross: making use of context in recurrent recommender systems. in: Proceedings of WSDM’18 2018. pp. 46–54.

[7] JS. Breese. D. Heckerman. C. Kadie. Empirical analysis of predictive algorithms for collaborative filering. Proceedings of the Fourteenth conference on Uncertainty in artificial intelligence (UAI’98). Morgan Kaufmann Publishers Inc., San Francisco,

[8] C. Chen, K. Lin, C. Rudin, Y. Shaposhnik, S. Wang, T. Wang, A holistic approach to interpretability in financial lending: models, visualizations, and summary explanations, Decis. Support, Syst. 152 (2022), 113647.

[9] J. Dastin, Amazon scraps secret AI recruiting tool that showed bias against women, Reuters (2018). October 10. Retrieved from. https://www,reuters.com/article/us -amazon-com-iobs-automation-insight-idUSKCN1MK08G. on 5/27/2021

[10] ’Economist, For Artificial Intelligence to Thrive, It Must Explain Itself, 2018 (February 17).

[11] S. Friedler, C. Scheidegger, S. Venkatasubramanian, S. Choudhary, E. Hamilton. D. Roth, A comparative study of fairness-enhancing interventions in machine learning, in: Proceedings of the Conference on Fairness, Accountability, and Transparency, 2019, pp. 329–338.

[12] R. Fu, Y. Huang, P. Singh, Artificial intelligence and algorithmic bias: source, detection, mitigation and implications, INFORMS TutORials in Operations Research (2020) 39–63

[13] U. Gasser, V. Almeida, A layered model for AI governance, IEEE Internet Comput.

[14], B Gilford Criminal justice algorithms: AL in the courtroom, Proctor February 2018 (2018).32–33

[15] L.H. Gilpin, D. Bau, B.Z. Yuan, A. Bajwa, M. Specter, L. Kagal, Explaining explanations: an overview of interpretability of machine learning, in: IEEE 5th International Conference on Data Science and Advanced Analytics (DSAA). 2018 pp. 80–89.

[16] A. Gosiewska, A. Kozak, P. Biecek, Simpler is better: lifting interpretabilityperformance trade-off via automated feature engineering, Decis. Support. Syst. 150 (2021), 113556.

[17] A.P. Holzinger, E. Kieseberg, A. Tjoa Weippl, Current advances, trends and challenges of machine learning and knowledge extraction: from machine learning to explainable AI, Lect. Notes Comput. Sci 11015 (2018) 1–8.

[18] M.E. Irarrazaval, ´ S. Maldonado, J. P´erez, C. Vairetti, Telecom traffic pumping analytics via explainable data science. Decis. Support. Syst. 150 (2021). 113559.

[19] M. Jamali, M. Ester, TrustWalker: a random walk model for combining trust-based and item-based recommendation, in: Proceedings of the 15<sup>th</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD ‘09), ACM, New York, NY, USA, 2009, pp. 397–406.

[20] N. Kallus, X. Mao, A. Zhou, Assessing algorithmic fairness with unobserved protected class using data combination, Manag. Sci. (2021) 1–23. Articles in Advance.

[21] H. Kerner, Too many AI researchers think real-world problems are not relevant, MIT Technol. Rev. (2020). August 18. Retrieved from, https://www.technology review.com/2020/08/18/1007196/ai-research-machine-learning-applicationsproblems-opinion/, on 6/10/2021.

[22] B. Kim, J. Park, J. Suh, Transparency and accountability in AI decision support: explaining and visualizing convolutional neural networks for text information, Decis. Support. Syst. 134 (2020), 113302.

[23] A. Lambrecht, C. Tucker, Algorithmic Bias? An empirical study of apparent genderbased discrimination in the display if STEM career ads, Manag. Sci. 65 (7) (2019) 2966–2981.

[24] J. Larson, S. Mattu, L. Kirchner, J. Angwin, Machine bias, Pro Publica (2016). May 23. Retrieved from, https://www.propublica.org/article/machine-bias-risk-assess ments-in-criminal-sentencing. on 5/27/2021.

[25] D. Lazer, R. Kennedy, G. King, A. Vespignani, The parable of Google flu: traps in big data analysis, Science 343 (6176) (2014) 1203–1205.

[26] Z.C. Lipton, J. Steinhardt, Troubling trends in machine learning scholarship: some ML, papers suffer from flaws that could mislead the public and stymie future research, ACM Oueue 17 (1) (2019) 45–77

[27] S. Lundberg, S. Lee, A unified approach to interpreting model predictions, in: 31<sup>st</sup> Conference on Neural Information Processing Systems, 2017.

[28] C.L. Mallows, Some comments on Cp, Technometrics 42 (1) (2000) 87–94. Specia 40th Anniversary Issue.

[29] C.Y. Moreira, M. Chou, C. Velmurugan, R. Ouyang, P. Bruza Sindhatta, LINDA-BN: an interpretable probabilistic approach for demystifying black-box predictive models, Decis. Support. Syst. 150 (2021), 113561.

[30] National Academies of Sciences, Engineering, and Medicine, Roundtable on Data Science Postsecondary Education: A Compilation of Meeting Highlights, The National Academies Press, Washington, DC, 2020, https://doi.org/10.17226/ 25804.

[31] Netflix, Netflix Prize Frequently Asked Questions, Retrieved from, https://netflixp rize.com/faq.html, 2009. on 6/13/2021

[32] J. Nikas. How YouTube drives people to the internet's darkest corners. Wall Street J. (2018). February 18.

[33] Y.J. Park, The Future of Digital Surveillance: Why Digital Monitoring Will Never Lose Its Appeal in a World of Algorithm-Driven AI, University of Michigan Press, Ann Arbor, MI, 2021.

[34] Y.J. Park, D.D. Shin, Contextualizing privacy on health-related use of information technology, Comput. Hum. Behav. 105 (2020), 106204.

[35] D. Pennock. E. Horvitz, S. Lawrence. C. Giles. Collaborative Filtering by Personality Diagnosis: A Hybrid Memory and Model-Based Approach, in: Craig Boutilier, Mois´es Goldszmidt (Eds.), Proceedings of the 16th Conference on Uncertainty in Artificial Intelligence (UAI ’00), Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 2000, pp. 473–480.

[36] A. Rashid, D. Cosley Albert, S. Lam, S. McNee, J. Konstan, J. Riedl, Getting to know you: learning new user preferences in recommender systems, in: Proc. IUI’02, 2002, pp. 127–134.

[37] M. Ribeiro, S. Singh, C. Guestrin, Why should I trust you?: Explaining the predictions of any classifier, in: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016.

[38] C. Rudin, B. Ustun, Optimized scoring systems: toward trust in machine learning for healthcare and criminal justice, INFORMS J. Appl. Anal. 48 (5) (2018) 449–466.

[39] I. Sampaio. G. Ramalho. V. Corruble. R. Prudencio. Acquiring the preferences of new users in recommender systems: the role of item controversy, in: Proc. ECAI 2006 Workshop on Recommender Systems, 2006, pp. 107–110.

[40] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommendation algorithms, in: Proc. of WWW10, 2001. May 1–5, 2001, Hong Kong.

[41] D. Shepardson, Autonomous car accountability in spotlight as US driver charged with homocide. 2020. Retrieved from. https://www.iol.co.za/motoring/industt y-news/autonomous-car-accountability-in-spotlight-as-us-driver-charged-with-h omocide-9b9ea750-f1d2-59e7-ab90-8f05d54e51fa. on 5/27/2021.

[42] D. Shin. Y. Park, Role of fairness, accountability and transparency in algorithmic affordance. Comput, Hum. Behay, 98 (2019) 277–284.

[43] I. Teixeira, F. Carvalho, G. Ramalho, V. Corruble, ActiveCP: a method for speeding up user preferences Acquisition in Collaborative Filtering Systems, Ady. Artif

[44] United Policyholders, Credit Scoring in Insurance: An Unfair Practice, Retrieved from, https://uphelp.org/buying-tips/credit-scoring-in-insurance-an-unfair-p ractice/, 2021. on 5/27/2021.

[45] M. van Lent, W. Fisher, M. Mancuso, An explainable artificial intelligence system for small-unit tactical behavior. in: Proceedings of the 16th Conference on Innovative Applications of Artificial Intelligence, 2004, pp. 900–907.

[46] Norha M. Villegas, Cristian S´anchez, Javier Díaz-Cely, Gabriel Tamura, Characterizing context-aware recommender systems: a systematic literature review. Knowl.-Based Syst. 140 (2018) (2018) 173–200.

[47] S. Vollmer. B. Mateen, G. Bohner. F.J. Király. R. Ghani, P. Jonsson, S. Cumbers A. Jonas, K.S.L. McAllister, P. Myles, D. Grainger, M. Birse, R. Branson, K.G. M. Moons, G.S. Collins, J.P.A. Ioannidis, C. Holmes, H. Hemingway, Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness, BMJ 368 (i6927) (2020)

[48] S. Vucetic, Z. Obradovic, Collaborative filtering using a regression-based approach, Knowl. Inf. Syst. 7 (1) (2005) 1–22.

[49] S. Wachter, B. Mittelstadt, L. Floridi, Transparent, explainable, and accountable Al for robotics, Sci. Robot. 2 (2017) eaan6080.

[50] J. Wang, A. de Vries, M. Reinders, Unifying user-based and item-based collaborative filtering approaches by similarity fusion, in: Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’06), ACM, New York, NY, USA, 2006, pp. 501–508.

[51] J. Wang, J. Wan, Z. Liu, P. Wang, Data mining of mass storage based on cloud computing, in: 2010 Ninth International Conference on Grid and Cloud Computing, 2010, pp. 426–431. Nanjing, 2010.

[52] G. Werner, S. Guven, GLM basic modeling: avoiding common pitfalls, Casualty Actuar. Soc. Forum (2007) 257–272. Winter.

[53] D. Woods, Cognitive technologies: the design of joint human-machine cognitive systems, AI Mag. 6 (4) (1985) 86–92.

[54] S.J.H. Yang, H. Ogata, T. Matsui, N. Chen, Human-centered artificial intelligence in education: seeing the invisible through the visible, Comput. Educ, Artif, Intell. 2 (2021), 100008.

[55] Xiwang Yang, Yang Guo, Yong Liu, Harald Steck, A survey of collaborative filtering based social recommender systems, Comput. Commun. 41 (2014) 1–10.

[56] B. Zheng, A. Agresti, Summarizing a predictive power of a generalized linear model, Stat, Med. 19 (2000) 1771–1781.

[57] Y. Zhou, D. Wilkinson, R. Schreiber, R. Pan, Large scale parallel collaborative filtering for the Netflix prize, in: Rudolf Fleischer, Xu Jinhui (Eds.), Proceedings of the 4th International Conference on Algorithmic Aspects in Information and Management (AAIM ’08), Springer-Verlag, Berlin, Heidelberg, 2008, pp. 337–348.

Dmitry Zhdanov conducts interdisciplinary research in information security and privacy, energy informatics, and economics of information systems. The primary focus of his research is to study how firms make decisions about determining their information technology posture and to develop a normative and prescriptive base for improving decisions regarding organizational information systems design. He served as a Special Issue Editor for Decision Support Systems and as a guest AE for MIS Quarterly. His works were published in leading information systems and business journals such as MIS Ouarterly, Information Systems Research, INFORMS Journal on Computing, Production and Operations Management, ACM Transactions on MIS and Decision Support Systems. Dr. Zhdanov is a Certified Infor mation System Security Professional (CISSP) and a Senior Member of IEEE.

Sudip Bhattacharjee is a Professor in the School of Business, University of Connecticut. His research interests include data driven IT and operations management and policy, in formation systems economics, energy informatics, digital goods and markets, and closed loop supply chains. His research has appeared in premier journals such as Management Science. INFORMS Journal on Computing. Journal of Business. Journal of Law and Economics ACM Transactions, Journal of Management Information Systems, IEEE Transactions, and other leading peer-reviewed publications. He currently serves as Senior Research Fellow. US Census Bureau. Previously, he served as Chief, Center for Big Data Research and Appli cations. US Census Bureau. He is a Visiting Faculty at EMLYON Business School. France and Indian School of Business. He was a Visiting Professor at GE Global Research Center, USA. He has previously served as the Assistant Dept. Head of Operations and Information Management, and as the Executive Director of MBA Programs, both in the School of Business, University of Connecticut. He serves or has served as Associate Editor for Information Systems Research (for 5 years), Special Issue Editor for ACM Transactions on Management Information Systems, guest AE for MIS Ouarterly and Decision Sciences Journal

Mikhail A. Bragin (Member. JEEE, INFORMS. PES) is an Assistant Research Professor in the Department of Electrical and Computer Engineering at the University of Connecticut His research work has been supported by the U.S. National Science Foundation, BNL, MISO, ISO-NE, ABB, CESMII, and AFRL. His research is geared toward solving complex technical and societal challenges within smart grids, supply chains, and artificial intelli gence. Accordingly, his research interests include operations research, mathematical optimization, including power system optimization, grid integration of renewables (wind and solar), energy-based operation optimization of distributed energy systems, stochastic scheduling within manufacturing systems, and machine learning through deep neura networks. His research has appeared in top journals such as Journal of Optimization Theory and Applications, IEEE Transactions on Power Systems, IEEE Transactions on Automation Science and Engineering, and IEEE Robotics and Automation Letters as well as in top confer ences such as INFORMS Annual Meeting and International Joint Conference on Artificial Intelligence
