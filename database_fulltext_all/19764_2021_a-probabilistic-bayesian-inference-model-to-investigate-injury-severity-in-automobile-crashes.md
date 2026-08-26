---
otero_id: 19764
otero_key: "ZGCHGNW8"
title: "A probabilistic Bayesian inference model to investigate injury severity in automobile crashes"
authors: "Kazim Topuz; Dursun Delen"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113557"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A probabilistic Bayesian inference model to investigate injury severity in automobile crashes

Kazim Topuz <sup>a</sup>, Dursun Delen <sup>b,c,\*</sup>

<sup>a</sup> School of Finance, Operations Management and International Business, University of Tulsa, Tulsa, OK, USA

<sup>b</sup> Department of Management Science and Information Systems, Oklahoma State University, Stillwater, OK, USA

<sup>c</sup> School of Management, Halic University, Istanbul 34445, Turkey

## A R T I C L E I N F O

Keywords: Data science Bayesian inference Injury severity Decision making Cross-entropy loss function, Bayesian missing data handling

## A B S T R A C T

Big data analytics examines millions, if not billions of records, to unmask hidden patterns, provide actionable insights and interpretable results for various domains. One area that has great potential to leverage the value of big data and analytics is the critical analysis of traffic accidents. Investigation results help in providing an indepth understanding of the risks and provide measures to potentially prevent these risk factors hence enhancing the well-being of individuals who may experience such accidents. This study explains existing models and proposes a data science methodology in a field where probabilistic modeling makes much sense for faster better decision-making. The main objective of this data analytics study is to identify the high-risk factors with their apparent significance to influence the probability of injury severity on automobile crashes using a geographically representative car crash dataset. To obtain reliable, accurate, and intuitive results, a multi-step probabilistic inference model based on Bayesian Belief Network— highly-acclaimed machine learning method ology—is proposed. The underlying inference model provides researchers with a causally accurate way to explore the domain (with the subject matter expert inputs) while disengaging issues related to statistical cor relations and causal effects. In this study, we also used the data to create a web-based probabilistic inference simulator, a Bayesian inference decision support tool, which will be a publicly available/accessible tool, to help decision-makers better understand and to conduct what-if analysis on variable interdependencies.

## 1. Introduction

Companies and organizations are persistently collecting data that is usually characterized by its unprecedented volume, variety, and velocity and is often called “big data.” Whether it is structured, semi-structured, or unstructured, big data is useless unless it portrays value and practical application. Big data analytics look at millions, if not billions of records, to unmask hidden patterns, provide actionable insights and interpret able results for various healthcare topics to operations management [5,12]. One area that has great potential to leverage the value of big data and analytics is the critical analysis of traffic accidents. Examining the risk factors correlated with the severity of injuries after motor vehicle crashes have become a thought-provoking and challenging research problem [32]. Investigation results help in providing an in-depth un derstanding of the risks and provide measures to potentially prevent these risks hence enhancing the well-being of individuals who may experience such accidents. Therefore, road safety is a significant challenge in the United States and elsewhere.

Innovative and upgraded safety measures are continually being developed and integrated into vehicles and highways to minimize car accidents and to alleviate the severity of injuries [14]. Despite relentless efforts to reduce car accidents, there is still a high number of accidents recorded every year. According to the recent statistics from the National Highway Traffic Safety Administration (NHTSA), six million traffic ac cidents recorded, 30,000 lives have been lost, and over 2.5 million people have been injured within a year [24]. On average, four people lost their lives, and almost 300 people sustained injuries on the US roadways every hour. According to the reports presented by the NHTSA, the societal and economic harm amounts to about \$871 billion in a single year. Out of the total estimated amount, \$277 billion got attrib uted to the financial costs, which are nearly about \$900 for each United States individual. The harm from decreased quality of life, pain, and loss of life because of the injuries from car crashes were estimated to be \$594 billion [2,7]. Several factors were found to affect the severity of injuries

in the event of a car accident.

This study explains existing models and proposes an analytic meth odology in a field where probabilistic modeling makes much sense for faster, better decision-making and intuitive understanding of complex relations. We use an example of injury severity in motor vehicle acci dents, but our methodology can be adapted to other fields. In this study, we identify the high-risk factors affecting injury severity using big data that includes a wide range of vehicle crash samples that are geograph ically well-presented. To obtain reliable, accurate, and intuitive results, herein, we proposed a multi-step probabilistic inference model based on Bayesian Belief Network, a relatively recent and highly capable machine learning methodology. Besides, this study presents a web-based proba bilistic inference simulator, a Bayesian inference decision support tool, to help decision-makers to understand the complex interdependencies. Web simulator predicts the probability of the severity level based on user inputs/ beliefs and will be available for public use. We introduce the accident severity classification and analysis system -a system-level taxonomy- to classify accident data into hazard sources and high-level probabilistic factors for a better data interpretation.

The rest of the manuscript is arranged as follows: Section 2 offers an overview of the relevant studies on injury severity in motor vehi cles—with a specific emphasis on the variety of analytics methods and methodologies used. Section 3 defines the proposed methodology and brief explanation of the phases involved, including the handling of data related issues, construction of the probabilistic inference model, devel opment of the web simulator, and the system-level taxonomy. Section 4 presents the results and reveals the findings along with an example using the web-based simulator. The final section, Section 5, summarizes the findings of the study, recognizes the limitations, and discusses potential future research directions along with a summary of the study’s contributions.

## 2. Background

A significant number of articles regarding the investigation of motor vehicle injury severity are reported in respected outlets. Most of the earlier studies used traditional statistical techniques with purposely sampled data, and they have often targeted audiences in technical transportation/accident channels. For instance, dataset limited to a small/specific geographic region (42), a particular crash type [46], or a vehicle type [45], a specific road [43] or environmental conditions (Fountas et al., 2020; [38]). Maybe the primary reason for such restricting features to create a homogeneous set of data that can be ac quired and used to derive more reliable prediction and descriptive models.

Traditional statistical models like multinomial logistic regression and its derivative models (i.e., ordered-logit or ordered-probit) have been the most commonly used techniques in developing injury severity analysis models. An earlier logistic regression study analyzed the probability of fatal outcomes of accidents given that the crash has occurred [46]. The data were acquired from the Fatal Accident Reporting System (FARS), which contained accidents that included at least one fatality. Another study focused on pedestrian injury severity by merging datasets from the City of New York, US (2002–2006), and the City of Montreal, Canada (2003–2006) (Mohamed et al., 2013). Their multinomial logit model found that several factors, including age, intersection type, preceding accident acts, type of vehicle, alcohol involvement, and lighting conditions, influence the prospect of a severe accident. Abay et al. [1] explained the injury severity in crashes, pri marily focusing on the use of seat belts. They employed a Multivariate ordered response probit (MORP) model to analyze two-vehicle crashe in Denmark [1]. A similar study by Uddin and Huynh [38] was inves tigated injury severity of truck-involved crashes under different weather conditions. They used mixed logit models to identify significant contributing factors and found that a good number of contributing fac tors are uniquely associated with weather conditions [38]. Another recent study used a latent class ordered probit model that was conducted within the state of Oregon that focused on the risk factors contributing to injury severity of large truck drivers in run-off-road crashes on rural and urban roadways [44]. Similar studies can be found in extend literature such as mixed logit model generalized [25], ordinal logit model [41], and hierarchical ordered probit model [30], and hierarchical ordered probit model [30]. Like previous analyzes, though, these studies were limited by utilizing a small number of candidate predictors and focus on specific issues. Accordingly, there is a need to use more comprehensive data sets that include a significant number of variables, which can also be conditioned to specific factors to unmask potentially hidden patterns among the different variables, which could affect the underlying com plex relationship outcomes of a vehicle accident. This can be done using advanced machine-learning models.

Some of the recent studies emphasized the mining of big data and ensembled machine learning algorithms to investigate injury severity. Generally, in these studies, data is provided by government agencies such as the NHTSA, environmental protection agency (EPA), and local or national department of transportation agencies. These studies mostly combine various sets of data to create a more comprehensive analysis. For instance, Delen et al. (2017) used a sizable and feature-rich crash dataset along with several predictive analytics algorithms, including artificial neural networks (ANN), support vector machines, classification and regression trees, and logistic regression. They proposed an infor mation fusion-based sensitivity analysis to identify the relative impor tance of the crash-related risk factors. They identified essential factors as seat belt use, manner of the collision, if the driver was ejected from the car, and if the drug test result is positive. A hybrid method of cluster analysis and hierarchical Bayesian model was developed by Li et al. (2018) examined driver injury severities in crashes using two-year crash data (Li et al., 2018). Dataset used in this study was specific to intersection-related crashes in New Mexico. Rahman et al. [31] ensembled decision tree regression models to explore the pedestrian and bicycle crashes [31]. They used Statewide Traffic Analysis Zone (STAZ) data, which includes 16,240 pedestrian, 15,307 bicycle data from Florida. In another pedestrian-involved crash study, the parameter order response model was compared with an artificial neural network (ANN) to explore the nonlinear relationship between explanatory variables and severity outcomes [21]. Sarkar et al. [34] combined both categorical and unstructured datasets -investigation and inspection reports- to predict injury severity. They created an exhaustive design of experiments with six machine learning models and four oversampling techniques. They found random forest algorithm outperforms other prediction algorithms (support vector machine, artificial neural network, Naive Bayes, knearest neighbor, classification, and regression tree analysis) [34].

When combined with various data sources such as weather, popu lation, and social media, crash data is comprehensive but imperfect. Studies that rely on data mining and machine learning methods are capable of handling variable-related assumptions and other restrictions. However, only a handful of researchers considered data issues such as handling missing values, misbalanced representation of target class, and multicollinearity or correlations. These studies employed machinelearning algorithms for the intention of causal inference. Philosophi cally, “given that we see” is different from “given that we do.” Whereas the former reveals the statistical (or observational) inference, causal inference is represented in the latter. Pearl [26] explains that the tran sition from statistical to causal inference is possible under strict condi tions where numerous additional assumptions are stated clearly. In fact, it is a widespread misapprehension to derive causal inference from observational data, which can raise controversies [27].

In this regard, Bayesian networks (BNs) are useful, which provides researchers a causally correct way to explore the domain -with the subject matter expertise input- as well as to disengage statistical corre lation and causal effects. BNs have become popular among PGMs as these models are used to process formerly unrecognized but potentially relevant data found in the networks subject to research [6, 37]. BNs also

![](/api/attachments/ZGCHGNW8/fulltext/images/81e5603c3237f5ca8371e582495f7c616712b4084c794d0a0e2d167ee81a8b93.jpg)  
Fig. 1. A graphical depiction of the Bayesian probabilistic inference methodology.

actively make use of the philosophies from graph and probability the ories, which makes the interpretation of data science intuitive for nontechnical subject-matter experts [6,37]. Recently, the Bayesian method has been gaining popularity in crash modeling research [40]. Very few studies revealed probabilistic interdependencies between fac tors and injury severity. For instance, Mujalli and de Ona ˜ [22] focused on rural highways and proposed a simple BN procedure with 18 dependent variables. Their simplified BBN structure learned from 1500 crash records performed relatively weak compared to other machine learning models (ROC value of 0.62) [22]. Garcia-Herrero et al. (2020) proposed a BN to understand the driver’s behavior and psychophysical conditions [10]. They utilized BN to quantify the overall accident severity, but their study did not give any details about how the Bayesian structure adapted. They found the excess speed and distraction/driver’s errors will have a tendency to raise the probability of serious/fatal injury for drivers of all age groups by 10% and 1.5%, respectively. Most of the studies in the literature did not contemplate missing data analysis, imbalanced data problem, and/or correlation between “independent” variables. Although most of them concentrated on traffic accident re cords limited to specific road type or crash type, and did not consider essential data issues, they have paved the road for more comprehensive probabilistic studies. To the scope of our knowledge, no such studies exist that thoroughly demonstrate a probabilistic inference model that takes account of data issues employing Bayesian Belief Networks (BNs).

This study can be differentiated from those of the previous studies in the following respects. First, we used several innovative techniques to address the data-related issues in a probabilistic graphical model. Sec ond, we showed that the proposed methodology could overcome certain limitations of traditional statistical methods in high-dimensional prob lem domains. Third, the probabilistic inference model is used to capture the potentially nonlinear. highly complex relationships between the related risk factors. Fourth, a web-based simulation tool is developed to provide an interface between data, analytics model, and the underlying calculations so that the data interpretation can be made quickly by a non-data science subject matter expert. Fifth, a system-level taxonomy provided to help group the accident-related variables into high-level causal factors. Lastly, even though this paper is meant to emphasize the usability and generalizability of the methodology independent from the underlying application domain, the obtained results yield new in sights for a subject matter expert in this domain to easily understand and interpret.

## 3. Probabilistic inference model framework

In this study, we propose a five-phase probabilistic inference framework for understanding the critical factors affecting the motor vehicle accident severity by unmasking the hidden causal relations among all variables (input and output). Phase (1) combining dataset from various disjoint data repositories, (2) addressing data issues, (3) building probabilistic Bayesian influence model, estimate joint proba bilities using data, and (4) creating a web-based probabilistic inference calculator to conduct what-if analysis, (5) introducing a system-level taxonomy to classify accident data into high-level causal factors to better interpret the model results.

Phase 1 compromises merging various repositories to create a comprehensive dataset. Crash Report Sampling System (CRSS) dataset used for the study covered all instances for the recent three years available (2015–2017). The complete data set was obtained in the form of twelve separate flat/text files—related to accident, vehicle, distract, and person for each year’s incidents. In Phase 2, we focus on data pre processing, specifically, address the discrepancies, with (a) Bayesian dynamic conditional imputations for missing records, (b) implementing a cross-entropy loss function to handle data imbalance issues, and (c) examining the relationships between the covariates to make sure to include interdependencies in a final probabilistic model to address multicollinearity and correlations between “independent” variables. Phase 3 presents Bayesian probabilistic inference models and data interpretation basics using mutual information and entropy. Phase 4 includes presenting an intuitive web-based inference calculator, which will be an interface between data, analytics, and computation. In the final phase, Phase $^ { 5 , }$ we introduce a systems-level taxonomy that in cludes five different constructs. A graphical depiction of the proposed methodology is shown in Fig. 1.

To perform individual tasks effectively and efficiently in the pro posed methodology, we employed several statistical and data mining software tools. Specifically, we used Python, R, and Tableau for merg ing, understanding, visualization, and preprocessing of the data sources; Python for the development of the machine learning models, BayesiaLab for the unsupervised and supervised probabilistic graphical network development and sensitivity analyses.

## 3.1. Data description

NHTSA is a United States Department of Transportation backed program that offers crash data from 1979 till the present day. NHTSA data, including CRSS, is derived from several sources, including the primary source as police-reported crashes involving various types of automobiles, cyclists, and pedestrians. It includes crashes ranging from minor property-related damages to ones that have led to human fatal ities. CRSS data represents a country-wide sample that was chosen from approximately six million crashes recorded by the police each year. The CSSR considers crash reports originating from carefully selected sixty sites spread across the US, which has the most accurate representation of the population, geography, crashes, and the total miles driven. The data collectors analyze numerous law enforcement agencies’ files, process, and enter thousands of crash reports into an electronic data file annu: ally. There are several quality checks done to authenticate the validity and accuracy of the data [49]. Once this process is concluded, the coded documents are published in a public domain. They interpret the crash data into a code, which is then entered as an electronic data file. A standard format is used containing about 120 data points. The initial dataset comprises information pertaining to property damage, charac teristics of the driver, crash scenario, environmental factors, and the severity of injuries for all participants.

In this study, we merged twelve separate flat/text files—related to the accident, distract, person, and vehicle for the last three years of in cidents available (2015–2017). The accident files contained specific characteristics about the road conditions, environmental conditions, and crash-related settings. The distract files comprised of a variety of information about driver distractions $( \mathbf { e . g . }$ , speaking on your phone, texting, reading messages, eating, drinking, having conversations with the people in the vehicle, playing with the radio or navigation system). The person files included demographics, injury, and situational infor mation about the occupants impacted by the crash. The vehicle files contained variables about the specific features of the vehicle involved in the crash. In order to consolidate the data into a single database, the three years of data are merged within each file type $( \mathrm { i . e . , }$ accident, distract, person, and vehicle), and the resulting files are combined using unique identifiers to create a single dataset. The resulting dataset included person-level records -one record per person- involved in a re ported crash. At this point in the process (before the data cleaning, preprocessing, and slicing/dicing), the complete dataset included 381,607 unique records $( \mathrm { i . e . , }$ persons/occupants involved in crashes) and 120 variables (a combination of accident, distract, person and vehicle-related characteristics).

## 3.2. Data preparation-addressing data-related issues

Since this study is a data-driven analytical investigation, the amount of efforts directed to the data preparation phase is vital as it ensures the quality and, most importantly, the credibility of the result. Over 80% of the total project time was directed on the data processing step, making it the most demanding phase of the study.

To better understanding the dataset, studies conducted most recently have placed additional attention to the injuries sustained solely by the driver (Delen et al., 2017). As evident from the relevant literature, most studies have focused on binomial injury severity, which can limit the actionable information that researchers can extract from the data. Additionally, exploration of the critical factors and their interactions is also limited with a binomial system because the differential focus of the study is on two classes. This study encoded the levels of injury severity as a categorical variable using three levels, no-injury (property damage only), minor injury (low-level non-disabling injury), and major-injury (a combination of disabling injury and mortality). We also included binary results using the same methodology to compare the results and present benchmarking metrics for other studies. Another advantage of the pro posed model is its ability to set the evidence at any level from 0% (none) to 100% to allow for testing of various scenarios. In such cases, the network automatically recalculates joint probabilities based on the updated evidence or belief.

When attempting to consolidate several years of data, we had to mitigate issues arising with the variation in the way variables were represented. We had to utilize a multi-source approach (published literature, statistical analysis, and, most importantly, common sense) in selecting the variables which required to be incorporated into the new model. After merging data, we identified and filtered out post-crash variables such as “HOSPITAL”- whether the person transported to the treatment facility- and “NUM\_INJ”- the number of people injured in the crash. We also eliminated variables that have the same information as the existing variable, such as “ALCOHOL” since “ALCHL\_IM” carries the same information. Each variable was recoded based on the CRSS Analytical User’s Manual. Some new variables were derived from the existing ones. For instance, using crash type (ACC\_TYPE), two new variables, crash type configuration (ACC\_CONF) and crash type category (ACC\_TYPE\_CAT) was created based on the crash type diagram pre sented in the manual. All variables were recoded as such according to the manual and with the help of the subject matter expert. Fig. 2 graphically illustrates the accident type recoding process.

![](/api/attachments/ZGCHGNW8/fulltext/images/185be80ca1b3ca98e72fea203ad7f555bfa2fe21042c9c0ec152d5cf33e757b0.jpg)  
Fig. 2. Recoding example: Accident type.

After the recoding process, we performed a comprehensive missing data analysis. Variables that had many missing records (>50%) and were regarded unimportant by subject matter experts such as “LAND\_ USE” (related to primary sampling unit), and “TRLR1VIN” (trailer identification number) were removed from the study. However, if a variable is considered significant but has more than half of the data missing, we decided to keep that variable such as “TRAV\_SP” (travel speed). Additionally, variables that had no contribution to our study were eliminated, such as ID and invariant variables.

## 3.2.1. Addressing the missing data problem

Although missing data problem is intuitive and affects nearly all quantitative studies, little attention has been given to it by researchers [29]. Missing values are evident in almost all actual data gathering processes, and this study is no different. Missing values that exist in our data illustrated in Fig. 3. The improper handling of missing observations can cause incorrect or misleading interpretations and an inaccurate sense of confidence in findings [35]. This can happen regardless of the number of complete observations exist. Rubin (1976) categorized missing data into three: First, “Missing Completely at Random (MCAR),” is where there is no relationship between a missing data point and in any value in the data set. Second, “Missing at Random (MAR)” is when missingness is affected by other known values and can be explained by the other variables observed in the data. The third type is “Missing Not at Random (MNAR)” when the data is missing in an unmeasured way, referred to a “nonignorable,” the probability of missingness fluctuates for details that are unfamiliar to us. From the perspective of MAR and MCAR, using a standard procedure for imputation implementation has resulted in significant improvements that need to be handled in an unbiased and statistically reasonable fashion (Bhaskaran & Smeeth, 2014). Unfortunately, in many studies, missing data are either elimi nated and/or assumed to be MCAR, and ad-hoc imputations were employed (Afghari et al., 2020; Zhou et al., 2020).

This study uses BNs to address the problem so that more advanta geous over ad-hoc methods that assume the dataset is MAR. First, as Heckerman (2008) noted, BNs provide a cohesive framework to repre sent the joint distribution of the overall and concurrently encode the dependencies with the missing data. Second, BN’s inherently probabi listic nature allows the researcher to manage missing data and their imputation non-deterministically. It implies that the required variance in the imputed data should be made inherently available and not necessarily be artificially generated. BN’s missing data handling can be described as stochastic conditional imputation. Like all other conven tional ad-hoc imputation methods, the imputation approach with BN also makes the MAR assumption. The motivation after the MAR assumption is that missingness in variables might be systematic, but these can be supported by other observed variables. For example, if “TRAV SP" data are missing at random, it might be conditional to some other factors such as “AGE\_IM” (age of the person), “INT\_HWY” (whether the crash occurred on an interstate highway), and “VSPD\_LIM” (posted speed limit). The implemented procedure works as follows:

• Start with the entirely unconnected network and use the available data to estimate the marginal probability distributions of all the variables

• Use structure learning algorithm (in our case Tree Augmented Naïve Bayes method, described in the next session) to form an initial structure then fill its conditional probability tables.

• Use the newly learned network and parameters to impute the missing values by drawing from the posterior probability distributions of the variables, given the values of the observed (not missing or already imputed) variables. This is the Expectation step, i.e., a static impu tation step.

![](/api/attachments/ZGCHGNW8/fulltext/images/ac0d257d9ec5acc5564d22cc2df1a682bbd88635ced2da96392b341058a01f76.jpg)  
Fig. 3. Representation of missing values in the combined dataset.

• Use this new dataset, which no longer contains missing values, to learn the structure and estimate the corresponding parameters. This is the Maximization step.

• The process alternates the Expectation and Maximization steps until convergence is achieved.

• In this process, the Bavesian network (BN) will grow from an initially unconnected network and evolve in its structure until its final state is reached.

Depending on the number of variables, the chosen learning algo rithm, and the network complexity, hundreds or thousands of iterations may be calculated. The final imputed dataset then remains available for subsequent analysis or export. The final data set contained 381,607 records, 62 variables including were selected and linked to offer the most amount of information in determining the levels of injury severity involved in crashes.

## 3.2.2. Addressing the imbalanced data problem

After the completion of data preprocessing, we noted that dependent variable representation had a significantly smaller number of reported cases for high-level injury severity compared to the number of cases for low-level injury severity and no injury (69% vs. 25% vs. 6%). Imbal anced data is an issue because when left unhandled, the prediction re sults would be lopsided towards the majority class [18]. Since there is no best way to handle the imbalanced data issue, after experimenting with standard methods, such as oversampling, under-sampling, and a mixture of over and under-sampling, we decided to adopt a different method for the following reasons: (1) the standard procedures would change the prior probabilities in the probabilistic graphical model which syntheti cally alter the conditional probability tables, and joint probabilities, (2) in a high dimensional multivariate dataset, under-sampling eliminates most of the records (\~80%), and (3) over-sampling adds repeated samples from minor classes, which could cause the model to overfit. Thus, in this study, we used a cross-entropy loss function to address the imbalanced data issue.

## 3.2.3. Cross-entropy loss

Cross- entropy loss is a well-known method to formularize loss in neural network studies [39], it is used to adjust model-weights during model training. The aim is to minimize the loss, i.e., the smaller the loss the better the model. A perfect model has a cross-entropy loss of zero (0). The multi-class cross-entropy loss of the $\mathrm { i } ^ { \mathrm { t h } }$ row can be defined as:

$$
L _ {C E} (i) = - t _ {i} \log (p _ {i})
$$

Where $t _ { i }$ is the corresponding one-hot element vector that shows the truth label, and $p _ { i }$ is the predicted probability of each given class. The objective is to make the model output as close as possible to the desired output (truth values). During model training, the model weights are iteratively adjusted accordingly with the aim of minimizing the Cross-Entropy loss. The process of adjusting the weights is what defines model training and as the model keeps training and the loss is getting minimized, we say that the model is learning. Some recent studies in object detection proposes adaptations of cross-entropy loss function to resolve class imbalance [28] problem, including balanced cross-entropy [19], focal loss [20], effective number of samples [4], and the real world- weight cross-entropy [13].

Mutual Information and Uncertainty Concepts. In traditional statistical analysis, we would likely examine correlation and covariance between the variables to establish their relative importance, especially regarding the target variable, “Injury Severity.” In this study, we present a different approach, which is based on information theory. Instead of computing the correlation coefficient, we consider how the uncertainty of the states of a to-be-predicted variable is affected by observing a predictor variable. Beyond our common-sense understanding of uncer tainty, there is a more formal quantification of uncertainty in informa tion theory, and that is entropy. More specifically, we use entropy to quantify the uncertainty manifested in the probability distribution of a variable or of a set of variables. In the context of our study, the uncer tainty relates to the predicted injury severity.

It is fair to say that we would need detailed information about an accident to make a reasonable prediction. However, in the absence of any specific information, would we be entirely uncertain about its value? Probably not. Even if we did not know details about an accident, we would have some contextual knowledge, i.e., that the vehicle involved in the accident is a large truck, rather than a passenger car. That knowledge significantly reduces the range of possible values. Based on the probability distribution, we can compute the entropy. The defi nition of entropy for a discrete distribution is:

$$
H (B) = \sum_ {b \in B} P (b) \log_ {2} P (b)
$$

The information gain or entropy reduction from learning about “BodyType” of this vehicle is obvious. Observing a different accident with a more common vehicle type, e.g., passenger car, would presum ably provide less information and, thus, have less predictive value for that accident. However, we wish to know how much information we would gain on average considering all values of “BodyType” along with their probabilities—by generally observing it as a predictive variable for “InjurySeverity.” Knowing this “average information gain” would reflect the predictive importance of observing the variable “BodyType.” To compute this, we need two quantities. First, the marginal entropy of the target variable H(InjurySeverity) and second, the conditional entropy of the target variable given the predictive variable:

$$
\mathrm{H} (\text { InjurySeverity } \mid \text { BodyType })
$$

$$
= \sum_ {i} P (\text { InjurySeverity }) H (\text { InjurySeverity } _ {i} | \text { BodyType } _ {i})
$$

The difference between the marginal entropy of the target variable and the conditional entropy of the target given the predictive variable is formally known as Mutual Information, denoted by I. In our example, the Mutual Information I between “InjurySeverity” and “BodyType” is the marginal entropy of “InjurySeverity” minus the conditional entropy of “InjurySeverity” given “BodyType”:

I(InjurySeverity, BodyType) = H(InjurySeverity) − H(InjurySeverity | BodyType)

More generally, the Mutual Information I between variables A and B is defined by:

$$
\mathrm{I} (\mathrm{A}, B) = \mathrm{H} (A) - \mathrm{H} (\mathrm{A} \mid \mathrm{B})
$$

which is equivalent to:

$$
\mathrm{I} (\mathrm{A}, B) = \sum_ {a \in A} P (a) \sum_ {b \in B} P (b | a) l o g _ {2} \frac {P (b | a)}{P (b)} \cdot \Bigg)
$$

This allows us to compute the Mutual Information between a target variable and any possible predictors. As a result, we can find out which predictor provides the maximum information gain and, thus, has the most considerable predictive importance—also probabilistic de pendencies between “independent” variables.

![](/api/attachments/ZGCHGNW8/fulltext/images/b3cd403d4fc507d76f3dac6eb96957a51dd30a9588d0116a1445177595c9dbd8.jpg)  
Fig. 4. An illustration of simple DAG.

## 3.3. Bayesian network probabilistic inference model

Probabilistic models derived from DAG (Directed Acyclic Graphs) have come along way, starting from Sewall Wright’s work in the early 20th Century. Its variations have been used in a lot of fields. Artificial intelligence and cognitive science are referred to as BNs and as directed graphical models in statistics. The initiation of BNs towards the end of the 1970s was driven by the need to demonstrate a top-down and bottom-up combination for reasoning [27]. BNs later replaced the ad hoc rule-based systems and became the number one option for inde terminate inferences in expert systems and artificial intelligence [3,23]. Essentially, the BN model is a DAG whereby the nodes match up with the specific variables (e.g., the driver’s age, whether the occupants use any type of restrain, a feature of the vehicle). Arcs are used to denote the conditional dependency among variables [27]. The arc directions describe parent-child relations. BN can be illustrated as linking A to B, A is the parental node of $\mathbf { B } ,$ and B is the child node.

Assuming there are no other variables, in Fig. 4, you can see a simple DAG that represents the relationship between b1: age of the occupants, b2: seating position, and b3: restraint type. We can define structures in this relationship: (1) Common effect as age and seating position cause restraint type, (2) common cause as age causes seating position and restraint type, and (3) indirect effect as age causes seating position and restraint type.

Probability distributions can be marginal or conditional. For parentless nodes, it is marginal and conditional for those with parents. Whereas, in conditional, the dependencies will be measured using conditional probability tables (CPT) for every node that has its parent in that graph. After specification, the BN efficiently portrays the JPD (joint probability distribution) and can, therefore, be used to figure out the posterior probabilities of any subgroup of variables. BN chain rule is often used to represent complicated probability distributions [15]:

$$
P \left(b _ {1}, \dots , b _ {n}\right) = \prod_ {i = 1} ^ {n} P \left(b _ {i} \mid A _ {b _ {i}}\right),
$$

where each b represents a variable, and $A _ { b i }$ is the parents of that vari able. For example, in the graph in Fig. 4, P(b3 |b2,b1) is the probability of restraint type given the values of age and seating position.

Finding BN exact inference is NP-hard and explained by Pearl [26], why it is necessary to use approximate inference, by forbidding re lations, and using previous dissemination over limitations of the network, or fixing the structural portions [26]. There are two methods of learning BN structure; the first uses score-based algorithms, which are founded on a system that measures the candidate networks' quality with the experimented data. The other one uses constraint-based algorithms, which are used based on the probabilistic semantic of BNs. It is unde batable that BNs are more helpful since it’s easy to translate previous information in a network structure, by forbidding relations, and using previous dissemination over limitations of the network, or fixing the structural portions.

![](/api/attachments/ZGCHGNW8/fulltext/images/31a449c9fe2ab5160c8ffb7d4a681d872994b5a0a6419cb153df565481dd5b81.jpg)  
Fig. 5. Tree augmented naïve Bayes network structure.

The process starts with the Naïve Bayes, which offers inferences to all analyzed variables in the intended focus. The Naïve Bayes classifier adheres to the Bayes principle, which limits the network with a strong assumption of all variables are independent except the target variable. Tree Augmented Naïve Bayes (TAN) method, which is an advancement of the naïve Bayes classifiers, offers a tree-like model, approximates the interactions between different predictor variables [9]. TAN performs better than naïve Bayes and maintains simplicity in the computation, which requires no search. It uses a parentless class variable; however, for each attribute, the conditional probability is calculated for the class variable and another attribute (see Fig. 5). The TAN method is the best compared to Markov Blanket (MB) and Naïve Bayes, which are also constraint-based structural learning algorithms [16]. In Fig. 5, TAN structure exemplified as C is the class variable (that has no parents $( A _ { C }$ $= \emptyset ) )$ , each predictor b has the C as a parent, along with at most one other attribute such as $b _ { 1 }$ as a parent for $b _ { 2 } .$

In our case, we have applied the BN’s TAN model because of its exceptional performance regarding the others. Our aim was to deter mine conditional dependencies due to its enhanced performance, unlike alternatives. A proper depiction of the parents for a variable b can be shown as:

$$
A _ {b _ {i}} = \left\{C, b _ {\delta (i)} \right\}
$$

where the tree is a function over $\delta ( i ) > 0 ,$ , is the set of parents for each $b _ { i } ,$ and C is the class variable that has no parents, namely $A _ { C } = \varnothing$

The Tree Bayesian concept by Chow and Liu’s (1968), is applied in constructing TAN structure as follows:

• Calculate mutual information for each (i, j) pairs as:

$$
\boldsymbol {I} _ {P} \left(\boldsymbol {b} _ {i}: \boldsymbol {b} _ {j} | \boldsymbol {C}\right) = \sum_ {\boldsymbol {b} _ {i}, \boldsymbol {b} _ {j, C}} \boldsymbol {P} \left(\boldsymbol {b} _ {i}, \boldsymbol {b} _ {j}, C\right) \log \frac {\boldsymbol {P} \left(\boldsymbol {b} _ {i} , \boldsymbol {b} _ {j} | \boldsymbol {C}\right)}{\boldsymbol {P} \left(\boldsymbol {b} _ {i} | \boldsymbol {C}\right) \boldsymbol {P} \left(\boldsymbol {b} _ {j} | \boldsymbol {C}\right)}, i \neq j\tag{8}
$$

• Construct a directionless graph and use the mutual information function to note the weight of an edge connecting b to b .

• Create a maximum-weighted spanning tree.

• Convert the directionless graph to a directed one by choosing a root variable and setting the direction of all edges to be away from it.

• Add a C labeled vertex and an arc right from C to each $b _ { i \cdot }$

After tree construction, the conditional probability of the features i conditioned to its parent. Then the calculation of the class label takes place prior to being kept. Also, the conditioned root variable’s proba bility is figured out and kept. Afterward, the posterior probability for every class label, $\mathrm { ~ P ~ } ( \mathrm { C } \mid \mathbf { B } 1 , . . . , \mathbf { B } \mathbf { n } )$ , is premeditated as a creation of the conditional probability of the root variable and the conditional proba bility of every attribute. The class label that has the highest future probability value will be allocated to the test sample. The conceptual proof and formulation can be found at [9].

## 3.4. Inference simulator

How can we infer knowledge from data using BN representation? A BN can serve as an inference engine and thus simulate a domain comprehensively. Through simulation, we can obtain all associations that exist in our domain, and, most importantly, we can accurately reason about a problem domain despite many unknowns and perform Omni-directional inference. Extracting inference by means of simulation within a BN is not a small calculation. Though, algorithms have been established that can accomplish the required tasks in the background, which are all executed suitably in the inference simulator.

![](/api/attachments/ZGCHGNW8/fulltext/images/25e356760fc8583639e212b6c0a243b8b6c6a07fefe975a61edf79d8890ae063.jpg)  
Fig. 6. The WebSimulator interface.

Table 1 Summary of clusters.

<table><tr><td>System-level Clusters</td><td>Number of Factors</td><td>Color Code</td><td>Factor Name</td></tr><tr><td>Human</td><td>12</td><td></td><td>Factor_2</td></tr><tr><td>Vehicle</td><td>12</td><td></td><td>Factor_4</td></tr><tr><td>Crash</td><td>13</td><td></td><td>Factor_0</td></tr><tr><td>Environment</td><td>11</td><td></td><td>Factor_1</td></tr><tr><td>Road</td><td>13</td><td></td><td>Factor_3</td></tr><tr><td>TOTAL</td><td>61</td><td></td><td></td></tr></table>

We use the WebSimulator as a platform to broadcast interactive models via the web, which means that any BN model built can be shared publicly with a broader audience. Once a model is published via the WebSimulator, end users can try out scenarios and examine the under lying dynamics of the model (Fig. 6). WebSimulator has turned out to be an instructional instrument that can efficiently recover and transfer the information inside the BN through visualization, simulation, and anal ysis, hence becoming a link between human and artificial intelligence.

## 3.5. Introduction of system-level taxonomy

There are few cross-sectional conceptual frameworks in vehicle safety, and these studies mainly focus on modeling driver behavior [8,33]. Research in conceptualizing the vehicle accident is essential and yet rare. This study does not present a theoretical framework but instead introduces a systems-level taxonomy, a step towards understanding the mechanism of injury severity. The presented system-level taxonomy helps classify accident data into hazard sources, identifying high-level causal factors. The system-level taxonomy includes five different con structs: (1) The technical features of the motor vehicle (vehicle), (2) the condition of the road at the time of the accident (road), (3) the envi ronmental condition or time-related factors (environment), (4) the crash-related situation features (crash), and (5) demographic or behavioral characteristics of the occupants (human). Table 1 summa rizes system-level clusters and details regarding the graphical results. System-level findings are presented in the results section.

## 3.6. Evaluation metrics and validation framework

Literature includes several metrics regarding the “true performance” of multiclass response variable models [36] and “true understanding” of complex relations [11,17]. Present a comprehensive picture of the per formance, and understand the complex structure of the problem (a) values for evaluating the overall performance (AUC, precision, and reliability) and (b) values for representing interrelations, conditional dependencies are presented (mutual information and entropy).

In order to differentiate between training and testing data sets, in recent years, the usual methodology for assessing the prediction accu racy of classification-type data mining models has been to split the data into two mutually exclusive subsets, usually called training and testing sets. An improved version of the single split methodology where the data is split into many (i.e., k number of) subsets is called k-fold cross validation. In k-fold cross-validation, the preprocessed, analytics ready data is randomly split into k number of mutually exclusive, near equal size, data sets. In order to maintain the proportional representation of the class distribution on all subsets, a stratification method, where the strata is the target variable. is used. Once the folds are identified. the classification method is trained on all-but-one folds, and then tested on the remaining fold. This training and testing process is repeated for k number of times, each time a different sunset (i.e., fold) is used as the test data, and the remainder of the data samples are used as the training data set. That is, in this cross-validation methodology, the training and testing process is repeated k number of times, each time the data samples of one of the folds being used as the test data. At the end of this iterative process, the overall performance (i.e., the prediction power) of the classifier is calculated using a simple aggregation and averaging of the k individual test sample performances.

Table 2  
Ten-fold cross-validation classification performance measures for all models.

<table><tr><td rowspan="2"></td><td colspan="2">Multiclass- No vs. Minor vs. Severe</td><td colspan="2">Binary- Minor vs. Severe</td></tr><tr><td>No Balancing</td><td>Cross-Entropy Data Balancing</td><td>No Balancing</td><td>Cross-Entropy Data Balancing</td></tr><tr><td>Mean ROC</td><td>73.33%</td><td>67.96%</td><td>78.91%</td><td>79.25%</td></tr><tr><td>Overall Precision</td><td>73.61%</td><td>65.44%</td><td>87.18%</td><td>80.83%</td></tr><tr><td>Overall Reliability</td><td>70.78%</td><td>70.21%</td><td>92.03%</td><td>92.48%</td></tr><tr><td>Severe Class Precision</td><td>29.92%</td><td>56.58%</td><td>53.73%</td><td>68.61%</td></tr></table>

## 4. Results, sensitivity and what-if analysis

BN can reliably carry out inference with multiple pieces of uncertain and even conflicting evidence. The inherent ability of BN to facilitate computations under uncertainty makes them highly suitable for a wide range of real-world applications. In this study, our goal is to create an explanatory model rather than a predictive one. We will note the pre dictive performance but focus on data interpretation using a multiclass probabilistic Bayesian inference model. Starting with data issues, we assumed the data is MAR and implemented BN’s stochastic conditional missing data procedure. Also, we considered imbalanced data issues and investigated the cross-entropy loss function method to balance the dataset. Table 2 lists the cross-validated overall results when crossentropy loss function has been implemented to address the imbal anced data issue. We also included binary model results to compare the values with multiclass and benchmark results that exist in the literature. The predictive performance of the multiclass classification results, as they relate to the overall “True Performance” metric, the imbalanced datasets produced better than the balanced ones. In imbalanced datasets, overall accuracy often is a misleading indicator or prediction power. The prediction accuracy of the minority class usually suffers in such cases. Therefore, the precision for the “severe” class (which is the minority class and the one we are primarily focused on) came out significantly better with the balanced datasets.

![](/api/attachments/ZGCHGNW8/fulltext/images/177235077d9c6ebde20d51fc6b8ddf6b6c9a0169689ea49bf9a2b100a15152fb.jpg)  
Fig. 7. Bayesian Network for prediction of injury severity (arc values indicate mutual information; node size represents entropy).

This study finds that the overall performance metrics have not improved significantly with the application of ordinary cross-entropy data balancing method, as it is compared to the performance obtained from the imbalanced dataset. In this study, a 10-fold stratified cross validation methodology was employed; that is, we developed ten probabilistic inference models, each time using a different tenth of the complete dataset as the test set. We had to pick one of the ten folds to build the exemplary model and the corresponding graphical network for practical reasons. Because of its close performance to the aggregated results built on all ten folds, we chose fold number five as the repre sentative model. As discussed earlier in the methods section, this study takes an alternative approach regarding uncertainty. We use entropy and mutual information to quantify the uncertainty manifested in the probability distribution and determine which predictor provides the highest predictive importance of a set of variables. In the context of our study, the uncertainty relates to the predicted injury severity. The probabilistic graphical network is shown in Fig. 7, where the values on arcs indicate mutual information between variables and node size rep resents the entropy values (explanation of entropy and mutual infor mation can be found in section 3).

In addition to generating human-readable and interpretable structures, we want to illustrate how we can immediately use the machine-learned BN model as an “inference engine” for automated inference and prediction. To comprehend the interdependencies, we illustrate a toy example with omnidirectional inference and operate numerous experimental queries on different compartments of the model. Fig. 8 exemplifies how much information we gain by observing “Body Type” along with their probabilities, as mentioned in an earlier example. Observing the variable “BodyType” – large trucks vs. passenger cars- the probability of severe injury in large trucks are lower than passenger cars. Omnidirectional inference update can be seen when adding one more observed variable to the calculation, in our example “Travel Speed.” Having a piece of evidence/belief, such as setting TRAV\_SP > 90, has caused several apprises to remaining predictors\` distributions. Similar to having multiple dependent variables. Indeed, all the probabilities in other variables all over the network were revised, but we only see the modifications of distributions of nodes that are available in the example.

Given that our probabilistic inference model can serve as a highdimensional representation of a real-world domain, web simulator al lows us to interactively—even playfully— engage with this domain to learn about it. You can find the publicly accessible web simulator here: https://simulator.bavesialab.com/#!simulator/240342181145.

Even though this study is not aiming to create a conceptual frame work, it creates a systems-level taxonomy, which will help researchers towards understanding the mechanism of injury severity. Five high-level constructs were created, and their individual contributors are listed in Table 3.

![](/api/attachments/ZGCHGNW8/fulltext/images/2e964465677644dab2c81dec3a620b7eff09b01804c7487d41e75065241d5cd3.jpg)  
Fig. 8. Omnidirectional inference update example (observed body type and travel speed).

The most critical manifest variables are “First Harmful Event” for the crash, “Weather Condition Group” for the environment, “Age of the Occupant” for the human, “Traffic Control Device Functioning” for the road, and “Age of the Vehicle” for the vehicle construct. Fig. 9 illustrates the mutual information between constructs themselves, and constructtarget (injury severity) pairs. Crash construct provides more informa tion gain than others. The least essential construct is displayed as the vehicle.

## 5. Summary and conclusion

Our study explains and expands the current analytics literature in terms of analytical methods, and interfaces between data and nontech nical decision-makers. Therefore, this research may be incorporated into an effective decision-support system to improve understanding of the “causal” anatomy of given risk factors. Our analysis shows that the Bayesian inference simulator provides understandable, interpretable, and actionable results without compromising on the accuracy of the prediction task.

Future research can benefit the presented domain knowledge and proposed methodology to explore different risk problems. Results show that the probabilistic inference model is capable of not only explaining the “causal” relations but also predicting injury severity in motor vehicle accidents with satisfying performance. Implementing various data pre processing techniques, including stochastic conditional imputation procedure in this body of research, also investigates different ap proaches in the literature regarding the impact and contribution of data balancing and creating high-level constructs to the resultant prediction models. Adaptations of different cross-entropy loss functions will be explored and comparatively investigated in a future study. The capa bility for omnidirectional inferences, combined with a rigorous proba bilistic foundation, our probabilistic inference model provides decisionmakers to the easily interpretable data science tool

The inherent ability of BNs to explicitly model uncertainty makes them suitable for a broad range of real-world applications. In our probabilistic inference framework, diagnosis, prediction, and simulation

Individual contributors to the high-level constructs. Table 3

<table><tr><td>Crash Components</td><td>Contribution (%)</td><td>Environment Components</td><td>Contribution (%)</td><td>Human Components</td><td>Contribution (%)</td><td>Road Components</td><td>Contribution (%)</td><td>Vehicle Components</td><td>Contribution (%)</td></tr><tr><td>ACC_CONF</td><td>19.9</td><td>DAYNIGHT</td><td>4.6</td><td>AGE_IM</td><td>39.3</td><td>INT_HWY</td><td>17.3</td><td>AIR_BAG_DEPL</td><td>0.1</td></tr><tr><td>ACC_TYPE_CAT</td><td>10.8</td><td>HOUR_DAYTIME</td><td>0.8</td><td>ALCHL_IM</td><td>0.1</td><td>REL_ROAD</td><td>1.6</td><td>BDYTYP_IM_UPD</td><td>3.3</td></tr><tr><td>EVENT1_IM_MANCOL</td><td>51.6</td><td>LGTCON_IM</td><td>1.7</td><td>DISTRACTED</td><td>6.4</td><td>REJCT1_IM</td><td>1.9</td><td>BUS_USE</td><td>2.5</td></tr><tr><td>HITRUN_IM</td><td>0.3</td><td>MONTH</td><td>0.2</td><td>DISTRACTED_DRIVING</td><td>28.9</td><td>TYP_INT</td><td>2.6</td><td>CARGO_BT_UPD</td><td>0.9</td></tr><tr><td>IMPACT1_IM</td><td>1.4</td><td>REGION</td><td>0.1</td><td>DRUGS</td><td>0.2</td><td>VALIGN</td><td>0.1</td><td>GVWR</td><td>6.6</td></tr><tr><td>J_KNIFE</td><td>0.1</td><td>URBANICITY</td><td>0</td><td>SPEEDREL_UPD</td><td>0.6</td><td>VNUM_LAN</td><td>0.4</td><td>MODELYEAR</td><td>12.2</td></tr><tr><td>PERMVIT</td><td>0.4</td><td>WEATHER_IM</td><td>37.2</td><td>REST_MIS</td><td>1.2</td><td>VPROFILE</td><td>0.3</td><td>NUMOCCS</td><td>0.2</td></tr><tr><td>PERNOTMVIT</td><td>8.4</td><td>WEATHER_G</td><td>38.4</td><td>REST_USED</td><td>0.1</td><td>VSPD_LIM</td><td>6.7</td><td>PCRASH1_IM</td><td>0.2</td></tr><tr><td>PVH_INVL</td><td>0.5</td><td>WEEKDAY_UPD</td><td>2.1</td><td>REST_TYP</td><td>1.1</td><td>VSURCOND</td><td>0.1</td><td>SCH_BUS</td><td>0.9</td></tr><tr><td>ROLINLOC</td><td>0.1</td><td>WEEKEND</td><td>14.8</td><td>SEAT_IM</td><td>21.5</td><td>VTCONT_F</td><td>38.1</td><td>TOW_VEH</td><td>3.9</td></tr><tr><td>ROLLOVER</td><td>0.1</td><td>YEAR</td><td>0.1</td><td>SEX_IM</td><td>0.1</td><td>VTRAFCON</td><td>21.5</td><td>V_CONFIG</td><td>5.6</td></tr><tr><td>VE_TOTAL</td><td>5.7</td><td></td><td></td><td>TRAV_SP</td><td>0.5</td><td>VTRAFWAY</td><td>8.4</td><td>VEH_AGE</td><td>63.6</td></tr><tr><td>VEH_NO</td><td>0.7</td><td></td><td></td><td></td><td></td><td>WRK_ZONE</td><td>1</td><td></td><td></td></tr><tr><td>TOTAL</td><td>100</td><td>TOTAL</td><td>100</td><td>TOTAL</td><td>100</td><td>TOTAL</td><td>100</td><td>TOTAL</td><td>100</td></tr></table>

![](/api/attachments/ZGCHGNW8/fulltext/images/7a08203935ff4689695494fcdaa5492f38dd90c5412a5513250bbe92684d2f72.jpg)  
Fig. 9. System-level taxonomy and high-level constructs of injury severity.

are identical computations.[42–59]

## References

[1] K.A. Abay, R. Paleti, C.R. Bhat, The joint analysis of injury severity of drivers in two-vehicle crashes accommodating seat belt use endogeneity, Transp. Res. B Methodol. 50 (2013) 74–89, https://doi.org/10.1016/j.trb.2013.01.007.

[2] L.J. Blincoe, T.R. Miller, E. Zaloshnja, B.A. Lawrence, The economic and societal impact of motor vehicle crashes (DOT HS 812 013), National Highway Traffic Safety Administration, 2015.

[3] K. Coussement, M. Phan, A. De Caigny, D.F. Benoit, A. Raes, Predicting student dropout in subscription-based online learning environments: The beneficial impact of the logit leaf model, Decis. Support. Syst. 135 (2020), 113325.

[4] Y. Cui, M. Jia, T.-Y. Lin, Y. Song, S. Belongie, Class-balanced loss based on effective number of samples, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2019. pp. 9268–9277

[5] A. Dag, K. Topuz, A. Oztekin, S. Bulur, F.M. Megahed, A probabilistic data-driven framework for scoring the preoperative recipient-donor heart transplant survival, Decis. Support. Syst. 86 (2016) 1–12, https://doi.org/10.1016/j.dss.2016.02.007.

[6] D. Delen, K. Topuz, E. Eryarsoy, Development of a Bayesian belief network-based DSS for predicting and understanding freshmen student attrition, Eur. J. Oper. Res. 281 (3) (2020) 575–587, https://doi.org/10.1016/j.ejor.2019.03.037.

[7] D. Dimitriou, T. Poufinas, Quantitative financial analysis for the estimation of road accident costs, Intern. J. Decision Supp. Syst. 2 (4) (2017) 260–277.

[8] Z. Elamrani Abou Elassad, H. Mousannif, H. Al Moatassime, A. Karkouch, The application of machine learning techniques for driving behavior analysis: A conceptual framework and a systematic literature review, Eng. Appl. Artif. Intell. 87 (2020) 103312. https://doi.org/10.1016/i.engappai,2019.103312

[9] N. Friedman. D. Geiger. M. Goldszmidt. Bavesian network classifiers. Mach. Learn

[10] S. García-Herrero, J.M. Guti´errez, S. Herrera, A. Azimian, M.A. Mariscal, Sensitivity analysis of driver’s behavior and psychophysical conditions, Saf. Sci 125 (2020) 104586, https://doi.org/10.1016/j.ssci.2019.104586.

[11] J. González-López, S. Ventura, A. Cano, Distributed Selection of Continuous Features in Multilabel Classification Using Mutual Information. JEEE Transactions on Neural Networks and Learning Systems. 2019.

[12] S. Guha, S. Kumar, Emergence of big data research in operations management, information systems, and healthcare: past contributions and future roadmap. Prod Oper, Manag, 27 (9) (2018) 1724–1735, https://doi.org/10.1111/poms.12833.

[13] Y. Ho, S. Wookey, The real-world-weight cross-entropy loss function: modeling the costs of mislabeling, IEEE Access 8 (2020) 4806–4813, https://doi.org/10.1109 ACCESS,2019.2962617

[14] Y. Huang, S. Meng, Automobile insurance classification ratemaking based on telematics driving data, Decis. Support. Syst. 127 (2019) 113156.

[15] D. Koller, N. Friedman, Probabilistic Graphical Models: Principles and Techniques, MIT press, 2009.

[16] K.B. Korb, A.E. Nicholson, Bayesian Artificial Intelligence, CRC press, 2010.

[17] S. Kumar, A. Sharma, T. Tsunoda, An improved discriminative filter bank selection approach for motor imagery EEG signal classification using mutual information, BMC Bioinform. 18 (16) (2017) 545.

[18] P.C. Lane, D. Clarke, P. Hender, On developing robust models for favourability analysis: model choice, feature sets and imbalanced data, Decis. Support. Syst. 53 (4) (2012) 712–718.

[19] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Doll´ar, C.

[20] T.-Y. Lin, P. Goyal, R. Girshick, K. He, P. Dollar, ´ Focal loss for dense object detection, in: Proceedings of the IEEE International Conference on Computer Vision, 2017, pp. 2980–2988

[21] S. Mokhtarimousavi, J.C. Anderson, A. Azizinamini, M. Hadi, Factors affecting injury severity in vehicle-pedestrian crashes: A day-of-week analysis using random parameter ordered response models and artificial neural networks, Intern. J. Trans. Sci. Technol. 9 (2) (2020) 100–115, https://doi.org/10.1016/j.ijtst.2020.01.001.

[22] R.O. Mujalli, J. de Ona, ˜ A method for simplifying the analysis of traffic accidents injury severity on two-lane highways using Bayesian networks, J. Saf. Res. 42 (5) (2011) 317–326, https://doi.org/10.1016/j.jsr.2011.06.010

[23] S. Nadkarni, P.P. Shenoy, A causal mapping approach to constructing Bayesian networks, Decis, Support, Syst, 38 (2) (2004) 259–281.

[24] National Center for Statistics and Analysis, Early estimate of motor vehicle traffic fatalities for the first quarter of 2020 (Crash•Stats Brief Statistical Summary. Repor DOT HS 812 966). National Highway Traffic Safety Administration. 2020.

[25] J. Pahukula, S. Hernandez, A. Unnikrishnan, A time of day analysis of crashes involving large trucks in urban areas, Accid. Anal. Prev. 75 (2015) 155–163, https://doi.org/10.1016/j.aap.2014.11.021.

[26] J. Pearl, Causal inference in statistics: an overview, Statis. Surv. 3 (2009) 96–146.

[27] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference, Elsevier, 2014.

[28] T.H. Phan, K. Yamamoto, Resolving Class Imbalance in Object Detection with Weighted Cross Entropy Losses, 2020, p. 13.

[29] S. Piri, Missing care: A framework to address the issue of frequent missing values; the case of a clinical decision support system for Parkinson’s disease, Decis. Support. Syst. 113339 (2020), https://doi.org/10.1016/j.dss.2020.113339.

[30] E. Rahimi, A. Shamshiripour, A. Samimi, A. Mohammadian, Investigating the injury severity of single-vehicle truck crashes in a developing country, Accid. Anal. Prev. 137 (2020) 105444, https://doi.org/10.1016/j.aap.2020.105444.

[31] M.S. Rahman, M. Abdel-Aty, S. Hasan, Q. Cai, Applying machine learning approaches to analyze the vulnerable road-users’ crashes at statewide traffic analysis zones, J. Saf. Res. 70 (2019) 275–288, https://doi.org/10.1016/j. jsr.2019.04.008.

[32] B. Ryder, B. Gahr, P. Egolf, A. Dahlinger, F. Wortmann, Preventing traffic accidents with in-vehicle decision support systems-the impact of accident hotspot warnings on driver behaviour, Decis. Support. Syst. 99 (2017) 64–74.

[33] F. Sagberg, Selpi, G.F.B. Piccinini, J. Engstrom, ¨ A review of research on driving styles and road safety, Hum. Factors (2015), https://doi.org/10.1177/ 0018720815591313

[34] S. Sarkar, A. Pramanik, J. Maiti, G. Reniers, Predicting and analyzing injury severity: a machine learning-based approach using class-imbalanced proactive and reactive data, Saf. Sci. 125 (2020), https://doi.org/10.1016/j.ssci.2020.104616. Scopus.

[35] G. Shankaranarayanan, Y. Cai, Supporting data quality management in decision-

[36] M. Sokolova, G. Lapalme. A systematic analysis of performance measures for classification tasks, Inf. Process. Manag. 45 (4) (2009) 427–437, https://doi.org/ 10.1016/i ipm 2009.03.002

[37] K. Topuz, F.D. Zengul, A. Dag, A. Almehmi, M.B. Yildirim, Predicting graft survival among kidney transplant recipients: A Bayesian decision support model, Decis Support. Syst. 106 (2018) 97–109, https://doi.org/10.1016/j.dss.2017.12.004.

[38] M. Uddin, N. Huynh, Injury severity analysis of truck-involved crashes under different weather conditions, Accid. Anal. Prey, 141 (2020) 105529, https://doi. org/10.1016/j.aap.2020.105529.

[39] X. Wu, D. Sahoo, S.C.H. Hoi, Recent advances in deep learning for object detection, Neurocomputing 396 (2020) 39–64, https://doi.org/10.1016/j. neucom.2020.01.085

[40] X. Zhang, S. Mahadevan, Bayesian neural networks for flight trajectory prediction and safety assessment, Decis. Support. Syst. 131 (2020) 113246.

[41] W. Zou, X. Wang, D. Zhang, Truck crash severity in New York city: an investigation of the spatial and the time of day effects, Accid Anal Prey 99 (2017) 249–261 https://doi.org/10.1016/j.aap.2016.11.024.

[42], E.K. Adanu, R. Smith. L. Powell, S. Jones, Multilevel analysis of the role of humar factors in regional disparities in crash outcomes, Accident Analysis & Prevention 109 (2017) 10–17, https://doi.org/10.1016/j.aap.2017.09.022.

[43] A.P. Afghari, M.M. Haque, S. Washington, Applying a joint model of crash count and crash severity to identify road segments with high risk of fatal and serious injury crashes, Accident Analysis & Prevention 144 (2020) 105615, https://doi. org/10.1016/j.aap.2020.105615.

[44] N.S.S. Al-Bdairi, S. Hernandez, Comparison of contributing factors for injury severity of large truck drivers in run-off-road crashes on rural and urban roadways: Accounting for unobserved heterogeneity. International Journal of Transportation Science and Technology 9 (2) (2020) 116–127, https://doi.org/10.1016/j. jitst.2020.01.004.

[45] S. Bahrololoom, W. Young, D. Logan, Modelling injury severity of bicyclists in bicycle-car crashes at intersections, Accident Analysis & Prevention 144 (2020) 105597, https://doi.org/10.1016/j.aap.2020.105597.

[46] E. Basso, LJ. Basso, R. Pezoa, The importance of flow composition in real-time crash prediction, Accident Analysis & Prevention 137 (2020) 105436, https://doi. org/10.1016/j.aap.2020.105436.

[47] K. Bhaskaran, L. Smeeth, What is the difference between missing completely at random and missing at random? International Journal of Epidemiology 43 (4) (2014) 1336–1339. https://doi.org/10.1093/jie/dyu080.

[48] C. Chow, C. Liu, Approximating discrete probability distributions with dependence trees, IEEE Transactions on Information Theory 14 (3) (1968) 462–467, https:// dei 0rg/10.1109/TIT 1968.1054142

[49] D. Delen, A comparative analysis of machine learning techniques for student retention management, Decision Support Systems 49 (4) (2010) 498–506.

[50] D. Delen, L. Tomak, K. Topuz, E. Eryarsoy, Investigating injury severity risk factors in automobile crashes with predictive analytics and sensitivity analysis methods, Journal of Transport & Health 4 (2017) 118–131, https://doi.org/10.1016/j. jth.2017.01.009.

[52] G. Fountas, A. Fonzone, N. Gharavi, T. Rye, The joint effect of weather and lighting conditions on iniury severities of single-vehicle accidents. Analvtic Methods ir Accident Research 27 (2020) 100124, https://doi.org/10.1016/j. amar.2020.100124.

[53] S. García-Herrero, J.M. Guti´errez, S. Herrera, A. Azimian, M.A. Mariscal, Sensitivity analysis of driver’s behavior and psychophysical conditions, Safety Science 125 (2020) 104586, https://doi.org/10.1016/j.ssci.2019.104586.

[54] D. Heckerman, A Tutorial on Learning with Bayesian Networks, in: D.E. Holmes, L. C. Jain (Eds.), Innovations in Bayesian Networks: Theory and Applications (pp. 33–82), Springer, 2008, https://doi.org/10.1007/978-3-540-85066-3\_3.

[55] Z. Li, C. Chen, Y. Ci, G. Zhang, O. Wu, C. Liu, Z. (Sean) Oian, Examining driver injury severity in intersection-related crashes using cluster analysis and hierarchical Bayesian models, Accident Analysis & Prevention 120 (2018) 139–151, https://doi.org/10.1016/j.aap.2018.08.009.

[56] K.-J. Lui, D. McGee, P. Rhodes, D. Pollock, An application of a conditional logistic regression to study the effects of safety belts, principal impact points, and car weights on drivers’ fatalities, Journal of Safety Research 19 (4) (1988) 197–203, https://doi.org/10.1016/0022-4375(88)90024-2

[57] M.G. Mohamed, N. Saunier, L.F. Miranda-Moreno, S.V. Ukkusuri, A clustering regression approach: A comprehensive injury severity analysis of pedestrian–vehicle crashes in New York, US and Montreal, Canada, Safety Science 54 (2013) 27–37, https://doi.org/10.1016/j.ssci.2012.11.001.

[58] D.B. Rubin, Inference and missing data, Biometrika 63 (3) (1976) 581–592 https://doi.org/10.1093/biomet/63.3.581.

[59] K. Topuz, H. Uner, A. Oztekin, M.B. Yildirim, Predicting pediatric clinic no-shows: A decision analytic framework using elastic net and Bayesian belief network, Annals of Operations Research 263 (1–2) (2018) 479–499

[60] H. Zhou, C. Yuan, N. Dong, S.C. Wong, P. Xu, Severity of passenger injuries on public buses: A comparative analysis of collision injuries and non-collision injuries, Journal of Safety Research (2020), https://doi.org/10.1016/j.jsr.2020.04.003.

![](/api/attachments/ZGCHGNW8/fulltext/images/f1d6ad4256531e36d92098f9bd5510c23ec4598425267a5c8751ae62f29003a1.jpg)

Dr. Kazim Topuz is the Chapman Assistant Professor of Op erations Management & Business Analytics in the Collins College of Business at the Tulsa University (TU). Before joining TU, he taught at the Price College of Business at the University of Oklahoma (OuD) as a lecturer, and he worked for the Center for Health Systems Innovation at Oklahoma State University (OSU) as a Research Fellow. In addition to his doctorate in philosophy (Ph.D.) from the Wichita State University (WSU), Dr. Topuz holds masters\` degrees in Information Systems Engineering from Lehigh University and Industrial and Systems Engineering from Rutgers University. He is a member of the Industrial En gineering Honor Society, Alpha Phi Mu, INFORMS, Decision Sciences Institute (DSI), and American Medical Informatics

Association (AMIA). He has served as a session chair and organized workshops at national conferences.

![](/api/attachments/ZGCHGNW8/fulltext/images/53870cf663664c3ebbe1b1fb86c468e490b2893cbdddceb4741293df13eb23df.jpg)

Dr. Dursun Delen is the holder of William S. Spears and Neal Patterson Endowed Chairs in Business Analytics. Director of Research for the Center for Health Systems Innovation, and Regents Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engi neering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, h worked for a privately-owned research and consultancy com pany, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for five vears, during which he led a number of decision support, information systems and advanced analytics related research proiects funded by federal agencies

including DoD. NASA. NIST and DOE. His has published more than 120 journal papers and eleven books/textbooks in the broad are of business analytics and data science. Dr. Delen is often invited to government agencies and companies for consultancy engagements and national and international conferences for keynote addresses on topics related to Business Analytics, Data/Text Mining, Business Intelligence. Decision Support Systems. Healthcare Analytics and Knowledge Management. He regularly serves and chairs tracks and mini tracks at various information systems and analytics conferences, and serves on several academic journals as editor-in-chief, senior editor, associate editor and editorial board member. His research and teaching interests are in data science, business analytics, data and text mining, decision support systems, knowledge management, business intelligence and enterprise modeling.
