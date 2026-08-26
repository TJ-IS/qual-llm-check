---
otero_id: 19974
otero_key: "5UX37JAM"
title: "Towards risk-aware artificial intelligence and machine learning systems: An overview"
authors: "Xiaoge Zhang; Felix T.S. Chan; Chao Yan; Indranil Bose"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113800"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards risk-aware artificial intelligence and machine learning systems: An overview

![](/api/attachments/5UX37JAM/fulltext/images/4ead76ef5cf7d51050f48d2acc3a59f30f0e35be638fea089411fd9377ee23ee.jpg)

Xiaoge Zhang <sup>a,\*</sup>, Felix T.S. Chan <sup>b</sup>, Chao Yan <sup>c</sup>, Indranil Bose <sup>d</sup>

<sup>a</sup> Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Kowloon, Hong Kong

<sup>b</sup> Department of Decision Sciences, Macau University of Science and Technology, Avenida Wai Long, Taipa, Macao

<sup>c</sup> Department of Biomedical Informatics, Vanderbilt University Medical Center, Nashville, TN 37235, USA

<sup>d</sup> Department of Information Systems, Supply Chain Management & Decision Support, NEOMA Business School, 59 rue Pierre Taittinger, Reims 51100, France

## A R T I C L E I N F O

Keywords: Risk analysis Artificial intelligence and machine learning Risk management Safety assurance Uncertainty

## A B S T R A C T

The adoption of artificial intelligence (AI) and machine learning (ML) in risk-sensitive environments is still in it infancy because it lacks a systematic framework for reasoning about risk, uncertainty, and their potentially catastrophic consequences. In high-impact applications, inference on risk and uncertainty will become decisive in the adoption of AI/ML systems. To this end, there is a pressing need for a consolidated understanding on the varied risks arising from AI/ML systems, and how these risks and their side effects emerge and unfold in practice In this paper, we provide a systematic and comprehensive overview of a broad array of inherent risks that can arise in AI/ML systems. These risks are grouped into two categories: data-level risk (e.g., data bias, dataset shift. out-of-domain data, and adversarial attacks) and model-level risk (e.g., model bias, misspecification, and un certainty). In addition, we highlight the research needs for developing a holistic framework for risk management dedicated to AI/ML systems to hedge the corresponding risks. Furthermore, we outline several research related challenges and opportunities along with the development of risk-aware AI/ML systems. Our research has the potential to significantly increase the credibility of deploying AI/ML models in high-stakes decision settings for facilitating safety assurance, and preventing systems from unintended consequences

## 1. Introduction

The past decade has witnessed the fast-paced development of arti ficial intelligence (AI) and machine learning (ML) in solving longstanding problems, and AI/ML has played an indispensable role in profoundly transforming business, transportation, finance, and health care, to name but a few. Nowadays, AI/ML is pervasively used in a broad array of applications across a variety of areas to benefit the whole of society, such as recommendation systems [1–3], fraud detection [4,5], autonomous driving [6,7], social media analysis [8–10], and business analytics [11–13]. One of the digital tools that most people heavily rely on nowadays is the AI/ML-powered personalized recommendation, which involves services covering almost every aspect of our life. These services range from route planning (i.e., Google Maps, Waze) [14] and customized content [15] to individualized product recommendation [16] and precise treatment [17]. With the increasing maturity of these applications, our life (e.g., commuting, entertainment, e-commerce, disease diagnosis) has been drastically improved.

However, the widespread deployment of AI/ML in high-impact ap plications, such as healthcare, manufacturing, and aerospace industries, is still in its infancy. Due to the lack of accurate and timely forecasting and analysis ability in high-impact areas, domain practitioners seek to leverage AI/ML techniques to achieve reliable and sustainable operations of the relevant systems. Detection of cancer is one of those critical tasks that was largely underdeveloped and has improved significantly with the help of AI/ML engines. The advancement of AI/ML has shown superiority over physicians in the early detection of fatal cancers (i.e., colorectal cancer), thus enabling timely interventions and the improvement in the survival rate of patients [18]. From the perspective of practical usage, however, though a large number of published studies repeatedly demonstrate the success of AI/ML tools to improve the per formance of the original systems in risk-sensitive areas, very few have been translated into practice from experimental studies [19].

One of the major roadblocks is that the current usage of AI/ML fundamentally lacks a rigorous and systematic framework for assess ment of risk and uncertainty. In the critical applications, a tiny failure could lead to disastrous outcomes and might put human lives in danger. For example, in a recent road test conducted in Maricopa County, Ari zona, U.S.A., the automated system in an Uber self-driving car failed to identify a pedestrian crossing mid-block and thus led to a fatality [20]. According to the investigation report by the National Transportation Safety Board, Uber’s “inadequate safety risk assessment procedures” and “ineffective oversight of vehicle operators” were the primary contrib uting factors to the accident [21]. From the perspective of model robustness, it has been widely realized that deep neural networks, one of the major components of AI/ML, are susceptible to adversarial pertur bations [22]. A small perturbation to an input image that is impercep tible to the human eye can make a well-trained neural network yield a drastically different classification with high confidence. Notably, Eykholt et al. [23] demonstrated that, by adding a small amount of spray paint or stickers on a stop sign, a highly accurate deep neural networkbased classifier can be easily fooled such that it incorrectly identifies the stop sign as a speed limit sign, leading to an auto-driving car failing to stop. In fact, organizations, such as governments and manufacturing companies, not only care about achieving their goals in an efficient manner, but also have concerns on transparency, accountability, fair ness, interpretability, traceability, and quality that must be factored into the overall risk management strategies. As such, notwithstanding the revolutionary impact of AI/ML systems, the lack of a rigorous frame work for risk analysis and assessment renders a low translation of AI/ML systems into practical solutions for risk-sensitive applications [24].

A common system assessment paradigm that has been practiced is to rely on aggregated prediction accuracy metrics to evaluate the quality of an AI/ML system [25,26], such as the mean squared error (MSE) and mean absolute error (MAE) for regression problems, and the area under the receiver operating characteristic curve (AUROC), precision, recall, and accuracy for classification problems. Though such metrics are suf ficient for many low-risk applications, it is dangerous to solely count on them in highly risk-sensitive applications, such as medical diagnosis and manufacturing industries, where safety and quality are the top priority. As shown by Nushi et al. [27], a model with a small MSE can still make large pointwise errors on individual inferences. In the medical domain, an aggregated accuracy metric can not provide the necessary informa tion that is essential for personalized medicine. This is because the reliability of model prediction can differ significantly between in dividuals. For example, in estimating the severity for two individual patients using the Parkinson’s Disease Rating Scale (PDRS) [28], it is likely that the PDRS score for one person is 123 ± 50 (low certainty) and 123 ± 8 (high certainty) for the other. In this case, an overall MSE will not provide such element-wise information that is essential for indi vidualized treatment. Thus, a general performance metric with respect to the whole dataset is inadequate in providing the desired safety and quality assurance in these applications.

Since the consequence of AI/ML system failures in safety and security-critical applications can be catastrophic in terms of economic loss and human fatalities or injuries, it is abundantly clear that reasoning about risk and uncertainty will become a cornerstone in translating AI/ ML models into high-stakes decision settings at scale. However, there is a lack of systematic studies to identify, define, examine, characterize, model, and quantify risks arising from heterogeneous sources in AI/ML systems. In the short term, the careful examination of risks in AI/ML systems is an important step for the subsequent risk characterization, quantification, assessment, and mitigation. In the long term, the effort dedicated to examining risks in AI/ML systems will lay a firm foundation for the development of risk management models to support risk-aware AI/ML systems. The risk management framework, built upon rigorous risk examination, will then help prevent unintended or harmful behav iors that might emerge from AI/ML systems, increase the credibility of adopting AI/ML systems in critical applications, and eventually facili tate the realization of safety assurance in AI/ML systems.

To fill this research gap, in this paper, we are motivated to provide a consistent, rigorous, and consolidated overview on a broad set of risks associated with the adoption of general AI/ML systems. In terms of scope, we focus on the types of risks that closely impact on the perfor mance of systems that are built with supervised AI/ML models and al gorithms. Consequently, risks pertaining to data privacy and ethical issues are not within the scope of this paper. The systematic overview in this paper offers a concrete and consolidated understanding on signifi cant issues characterizing the concerns of stakeholders when adopting AI/ML systems in critical applications from the risk analysis perspective. This overview also highlights the research efforts that are needed before fully embracing AI/ML systems in risk-sensitive scenarios. We also discuss the potential solutions and research directions that will inspire the development of comprehensive risk management strategies to guide future implementation decisions. We believe this overview can spark a lot of interests in the development of quantitative approaches, strate gies, and control checkpoints to safeguard the use of AI/ML models in risk-sensitive applications. The main contributions of this paper are summarized as follows:

1. To the best of our knowledge, we are the first to conduct a comprehensive examination of risks for AI/ML systems, where we identify risks that are inherent in AI/ML systems arising from different sources. Each type of risk is clearly defined, described, explained, and categorized. The clarification on each type of risk will facilitate the design of reliable, dependable, safe, and trustworthy AI/ML systems.

2. We outline the specific research needs for a systematic risk analysis and management framework associated with the characteristics of distinct AI/ML systems in high-stakes decision-making environments.

3. We outline several critical research challenges and opportunities that researchers may encounter in the development of risk analysis and a risk management framework dedicated to AI/ML systems.

The rest of the paper is structured as follows. Section 2 defines risk in the context of AI/ML systems, and describes a variety of risks per taining to input data and models in AI/ML systems. Section 3 discusses existing issues in the state-of-the-art literature, and outlines the research needs for a systematic risk analysis and management framework. Sec tion 4 summarizes the research challenges and opportunities in devel oping risk-aware AI/ML systems. Section 6 provides concluding remarks.

## 2. Risks in AI/ML systems

AI/ML systems continue to play an integral role in the recent AI/ML revolution. In brief, AI/ML systems usually employ a particular set of algorithms to automate the learning of patterns and relationships from data without being explicitly programmed. While AI/ML systems demonstrate powerful learning ability, the potential risks posed by these systems are expected to increase substantially. The failure of AI/ML systems could lead to unintended, or in some cases, serious conse quences in risk-sensitive applications. Thus, it is of paramount impor tance to approach the risk management challenge systematically. In this section, we review the principal risks arising in an AI/ML system. In general, risks in a generic AI/ML system can be grouped into two broad categories: data-level risk, and model-level risk. Fig. 1 illustrates the hierarchical structure of the risk categorization in AI/ML systems, where we identify a wide array of sources that primarily contribute to the data level and model-level risks from different perspectives.

## 2.1. Data-level risk

## 2.1.1. Data bias

Data bias is an important issue that many researchers and practi tioners can encounter in developing and evaluating AI/ML models [29]. Specifically, data bias refers to certain groups or certain types of elements that are over-weighted or over-represented than others in AI/ ML models, or variables that are crucial to characterize a phenomenon of interest, but are not properly captured by the learned models. Since AI/ML models typically learn to make decisions based on historical data, they often perpetuate existing biases present in the historical data. If a specific class or group is under-represented in the data, the trained AI/ ML model might have poor performance on this group in spite of the overall high model accuracy [30].

![](/api/attachments/5UX37JAM/fulltext/images/99ecd6681677c91ab2f2e2822ef73801907eaceb0d1197e7a897ec8e1f76fec6.jpg)  
Fig. 1. Risk categorization in AI/ML systems.

Data bias is an underlying issue in reality, but is often overlooked by many developers and researchers. In many situations, it is even assumed that the collected data is complete and representative; although most of the time this is not the case. In particular, data bias is even more evident in the context of recommendation and personalization systems [31]. For example, Piramuthu et al. [32] reported that data bias in user-generated reviews exist in many different shapes and forms, such as user person ality (e.g., impulsive, calm), context (e.g., user comments vary depending on the specific purpose of purchasing the product), and temporal (e.g., user comments may change over time).

The quality of an AI/ML model is largely determined by the quality of the data that is used to build the model. Bias in data often results in biased models, and it can eventually lead to discriminatory, inequitable, and harmful decisions affecting humans. For example, the e-commerce giant, Amazon, recently shut down an internal project that used AI/ML to speed up vetting job applications for employment because the established system consistently assigned lower scores to female candi dates due to the biased data rooting from the male-dominated working environment in the technology industry [33]. Another example of data bias is the predictive policing systems that are built on the crime data produced over the flawed and racially-biased document period [34]. The bias rooted in the data is propagated through the model training process, and eventually leads to an inaccurate and systematically biased AI/ML model. Last but not least. as most data on the Web used for building recommendation systems is generated by people in the context of their own biases, such as background, culture, education, economical development, location, it is easy to understand the bias that pervasively exists in the Web data. Thus, it is essential to examine bias in the collected data, develop quantitative metrics to identify data bias, and use measures to prevent AI/ML models from producing biased outcomes that might impact on our daily lives.

## 2.1.2. Dataset shift

The term dataset shift” was first used by Quinonero-Candela ˜ et al.

[35] to characterize the situation where the training data and the testing data (or data in runtime) of an AI/ML model demonstrate different distributions [36]. The current state-of-the-art literature has used many variants of the term dataset shift, such as concept shift (drift), distri butional shift, changing environments etc., but they all refer to the same phenomenon. In practice, the performance of an AI/ML system degrades significantly due to the mismatch between the dataset with which it was developed and the dataset on which it is deployed [37–39]. In general, dataset shift can be roughly categorized into the following classes:

1. Covariate shift: when training AI/ML models, people typically assume that the training data and the testing data follow the same probability distribution [40,41]. However, this common assumption is usually violated in many real-world applications [42], especially in dynamic environments. Covariate shift is developed to model the situation in which the functional relationship between X and Y remains unchanged while X follows two different probability dis tributions in the training data and testing data. Mathematically, we have $p ^ { \mathrm { t r a i n } } ( { \mathcal { X } } ) \neq p ^ { \mathrm { t e s t } } ( { \mathcal { X } } )$ . As shown in Fig. 2, the training data and testing data follows two different probability distributions while the underlving relationship between X and ¿ (see target function in Fig. 2) remains the same. As can be observed in Fig. 2, due to data biases, the AI/ML model does not learn the underlying function be tween X and Y correctly, which leads to inaccurate predictions for testing samples. Covariate shift occurs in a broad variety of realworld applications. For example, if a medical condition prediction model is trained predominantly on elderly people, covariate shift will occur if this model is used for prediction of medical conditions in a test dataset that has large proportion of younger people.

2. Prior probability shift: while covariate shift focuses on the variance of the probability distribution corresponding to X , prior probability shift centers on the change associated with the probability distribu tion of Y [43,44]. Mathematically, prior probability shift can be characterized as $p ^ { \mathrm { t r a i n } } ( \mathcal { Y } ) \neq p ^ { \mathrm { t e s t } } ( \mathcal { Y } )$ . Basically, prior probability shift refers to the situation where the training data and testing data differ in the distribution of Y . Consider the classification problem shown in Fig. 3. In the training data, class A is the majority class, while the situation is reversed in the testing data where class B is the dominating class. The significant change in the proportion of class distribution has a non-negligible effect on the performance of the AI

![](/api/attachments/5UX37JAM/fulltext/images/a8c34c87aa3a4df7de873d646f1ae8d7677a94368c6cb5872b631abefe34493a.jpg)

![](/api/attachments/5UX37JAM/fulltext/images/78a1fc4ba055ff55f3c0277c89bc44aa096adcbed90fba7e378946d364633faf.jpg)  
Fig. 2. Illustration of covariate shift.

![](/api/attachments/5UX37JAM/fulltext/images/91f882f0fa199b107c416ca06c8945fb90637bb8637d44f3641647fca377672d.jpg)

![](/api/attachments/5UX37JAM/fulltext/images/0be1fae1cc9fcbfb04099811422ea0d4e4511ae71d661b9a351b02c7945d2dd1.jpg)  
Fig. 3. Illustration of prior probability shift. Different shapes represent different classes.

ML algorithm, which might result in biased decisions towards certain subgroups. This bias can be seen in the use of the COMPAS dataset. COMPAS keeps track of the demographic and criminal history of defendants as well as their recommitted crime history within a certain period of time [45]. In 2013, Caucasians and African-Americans constituted 32.7% and 48.6% of re-offenders (re-of fenders refer to defendants that recommit a crime within a certain period of time), respectively. However, these fractions varied significantly in 2014. Specifically, the percentage of Caucasian and African-American re-offenders became 63.6% and 70.6%, respec tively [46]. If such prior probability shift is not accommodated properly, an AI/ML model might end up with biased and unfair de cisions towards individuals belonging to the population subgroups exhibiting prior probability shifts.

3. Concept shift: Differing from covariate shift and prior probability shift, concept shift, which is often referred to as concept drift”, characterizes the situation in which the underlying relationship be tween $\mathcal { X }$ and $\mathcal { Y }$ changes in non-stationary environments [47,48]. Mathematically, concept shift is represented as $p ^ { \mathrm { t r a i n } } ( \mathcal { Y } | \mathcal { X } ) \neq p ^ { \mathrm { t e s t } } ( \mathcal { Y } | \mathcal { X } )$ ). Basically, the conditional distributions of the target variable Y given the input variable X are different in the training data and testing data while the distribution of the input variable $\mathcal { X }$ remains the same. Fig. 4 illustrates an instance of concept shift. As can be observed, the relationship between $\mathcal { X }$ and $\mathcal { Y }$ has significantly changed in the training data and testing data. As reflected by the decision boundary of this classification problem, the functional relationship in the training data is no longer applicable to the testing data because of concept shift. In non-stationary envi ronments, due to the rapid change in operational environments, the patterns inferred from the past data might lead to poor decisions and prediction outcomes. Concept shift has been recognized as one of the major factors that leads to performance degradation in many AI/ML algorithms [49]. If concept shift is not captured appropriately, many early warning systems will lose their effectiveness.

![](/api/attachments/5UX37JAM/fulltext/images/46074cc5a9db92a7aebfe84e25f72a1e42221a27d7a40788fdd1c8d90bd512ea.jpg)

![](/api/attachments/5UX37JAM/fulltext/images/6f94ada54258bcb797c41f96f26e1794308a1777af06e8d3128473424cd7e9dd.jpg)  
Fig, 4. Illustration of concept shift. The red dashed line indicates the decision boundary, and dots in the same color belong to the same class. (For interpre tation of the references to color in this figure legend, the reader is referred to the web version of this article.)

## 2.1.3. Out-of-domain data

In this study, we separate out-of-domain data as an individual type of data-level risk. AI/ML algorithms, in particular deep learning models, show remarkable performance in tackling problems where it is prohib itively challenging to formalize the problem domain (or frame) analyt ically, such as image classification, object recognition, machine translation, etc. For example, there is no way to define the digital shape of a number with mathematical formulations and representations in image classification problems. On the other hand, the AI/ML community tends to move towards the end-to-end approach for knowledge repre sentation and learning [50,51]. Towards this goal, deep learning methods have replaced traditional AI/ML approaches that manually handcraft and engineer features from raw data with a holistic end-to-end approach in a high-dimensional space through multiple layers of neuron and activation functions [52,53]. The end-to-end learning capability has allowed deep learning models to take over the role of data preprocessing that used to be fulfilled by pre-processing pipelines.

Most AI/ML models are trained with a closed-world assumption, and the training data and testing data is assumed to be drawn from the same distribution [54,55]. However, once an AI/ML model is deployed, it processes inputs from a dynamic and open-world environment. How ever, the lack of a clear definition of the problem domain might pose a serious risk when deploying AI/ML algorithms in practice as we lack an effective approach to filter out data that fall outside of the domain of the training manifold. Without proper validation and management on the input data, it is highly probable that the trained AI/ML model will make erroneous predictions with high confidence for many instances of model inputs. The unconstrained inputs together with the lack of definition of the problem domain might cause unintended outcomes and conse quences, especially in risk-sensitive contexts. For example, with respect to the example shown in Fig. 5, if an image with the English letter $\mathsf { A } ^ { \prime \prime }$ is fed to an AI/ML model that is trained to classify digits $( \boldsymbol { \mathrm { e . g . } } , 0 , 1 , . . . , 9 )$ no matter how accurate the AI/ML model is, it will fail as the input data is bevond the domain that the AI/ML model is trained with. Unfortu. nately, once the $\mathbf { A I / M I }$ model is deployed, we have no control over what input is fed into the model. On the other hand, it is impossible to enumerate all out-of-domain cases and include them in the training data. As a result, blindly accepting model predictions on inputs without further examination might lead to catastrophic failures, especially in high-stakes decision-making applications where safety and quality are the top priority.

## 2.1.4. Adversarial attack

In recent years, adversarial attack has emerged as a new type of threat to the safety of AI/ML models [22,56]. Recent advances have shown that a deep learning model with high predictive accuracy frequently misbehaves on adversarial examples [57,58]. In particular, a small perturbation to an input image, which is imperceptible to humans, could fool a well-trained deep learning model into making completely different predictions [23]. Fig. 6 shows a well-known example of adversarial attack. Originally, the classifier has 57.7% of confidence in labeling the input image as a panda. After adding a negligible degree of perturbation, humans can still recognize the image as a panda without any problem. However, the same classifier fails to classify the modified image correctly and labels it as a gibbon with a much higher confidence of 99.3%. The unstable behavior of deep learning models has received increasing attention and raised serious concerns regarding safety, reli ability and stability of deep learning models [59]. In general, adversarial attacks can be grouped into two classes:

1. Targeted adversarial attack: The goal of targeted adversarial attack is to make an AI/ML model classify an adversarial image with a true label of $\mathcal { K }$ as a target class $\mathcal { T } \left( \mathcal { T } \neq \mathcal { K } \right)$ through intentional design $( \mathrm { i . e . } _ { \cdot }$ , data manipulation).

2. Untargeted adversarial attack: The objective of untargeted adversarial attack is to make an AI/ML model generate a prediction that is different from the true label without intended target.

In adversarial attack, adversarial inputs are generated by solving an optimization problem. Consider a classifier $f : \mathcal { X } \to \mathcal { Y } ,$ , a data point $x \in \mathcal { X }$ , and its class label $y \in \mathcal { Y } ,$ , where $f ( x ) = y .$ . The goal of adversarial attack is to produce an adversarial input x<sup>′</sup> $\in \mathcal { X }$ such that $f ( x ^ { \prime } ) \neq y ,$ while the distance between x and x<sup>′</sup> is less than ε. Intuitively, the goal of the optimization problem is to maximize the probability of tricking the classifier f into making a wrong prediction on the data point x<sup>′</sup> while x<sup>′</sup> is ε distant away from x. A complete list of AI/ML system failures caused by adversarial attack is given in Ref. [60].

## 2.2. Model-level risk

In this section, we review different types of risks pertaining to AI/ML models that include model bias, model misspecification, and model uncertainty.

## 2.2.1. Model bias

![](/api/attachments/5UX37JAM/fulltext/images/10d65caffa2d00953ad0838d7aa1129d72a489ba984ab2d2b9ad9f5b6e48ce13.jpg)

As most AI/ML algorithms are data-driven, data represents a core component that is tightly coupled with the functionality of the AI/ML models and it affects the performance of AI/ML systems substantially. If the training data has a bias towards certain population groups, then such a bias in training data is propagated to the AI/ML model. As a conse quence, the trained AI/ML model becomes biased, and the model pro duces biased outcomes. In brief, model bias (or algorithmic bias) refers to the bias that is purely incurred by the model during model develop ment [61]. While data bias is a major contributor of model bias, model bias actually manifests itself in different forms and shapes, such as presentation bias, model evaluation bias, and popularity bias. In addi tion, model bias arises from various sources [62], such as AI/ML model selection (e.g., support vector machine, decision trees), regularization methods, algorithm configurations, and optimization techniques. For example, it has been found that the random forest tends to favor fields with a large number of categorical values, which increases the risk of poor decision prediction [63,64].

![](/api/attachments/5UX37JAM/fulltext/images/cf39ec5db95e42f34df72be6f03661305ae32781c35b72bf4f4c3b1e8edd1df5.jpg)  
Fig. 5. Demonstration of out-of-domain data.

![](/api/attachments/5UX37JAM/fulltext/images/a7a2b234a3d6a25ddd3aa0f795d2aba31f180ecfa9f6fd2e34b14326934b45c6.jpg)  
Fig. 6. An example of adversarial attack.

Recently, Mehrabi et al. [65] conducted a comprehensive review to systematically examine biases arising from data and algorithms. As highlighted by Mehrabi et al. [65], model bias and data bias are inter connected, and the algorithmic design choices could lead to different types of bias that will eventually manifest in the data. Take the data on the Web as an example. Users typically click top-ranked results more frequently than others on the same web pages, making these results receive more clicks than others. The biases in the collected Web data are then looped back to guide the improvement of the ranking algorithm. Clearly, data bias and algorithmic bias influence each other, and the interrelation might lead to an amplified bias in both the data and the model. With the deeply propagated biases, users may only be able to view biased information online that has already been pre-screened [66].

If model bias is not addressed in a sound manner, it can lead to discriminatory behavior towards certain groups or populations in re ality. Osoba and Welser IV [67] have summarized a broad range of scenarios where AI/ML systems with model bias can affect our daily life, such as flight booking systems, hospital and residents matching pro grams, traffic routing algorithms, search and advertisement algorithms, etc. In particular, AI/ML systems are increasingly used for many sensi tive applications, and if model bias is not accounted for, the distorted decisions from AI/ML systems can have a life-changing impact as the legal rights of affected people may be undermined due to the biased result produced by the AI/ML model.

## 2.2.2. Model misspecification

As mentioned earlier, an important assumption in AI/ML systems is that training data and testing data are drawn from the same distribution. However, in practice, we rarely know the actual underlying distribution for testing data beforehand, let alone verify whether the testing data and training data are from the same distribution or not. Model mis specification occurs when model assumptions (e.g., model forms) are inappropriate for the data used for training. Model misspecification can be caused by three factors:

1. Model form error: when all explanatory variables are readily avail able, but the model still fails to characterize the relationship between the explanatory variables $\mathcal { X }$ and the quantity of interest $\mathcal { Y } ,$ then the model has functional form misspecification. In other words, the specified functional form is inadequate to characterize the true relationship. The outcome of the model form error is that the spec ified AI/ML model underfits the training data. For example, it is improper to use a linear regression model to fit data that has complex nonlinear interactions between the variables. Fig. 7(a) illustrates an example of model form error. While there is a nonlinear relationship between $\mathcal { X }$ and $\mathcal { Y } : \boldsymbol { y } = \boldsymbol { x } ^ { 1 . 5 }$ , but a linear regression model is used to fit the data. Even though the trend of the data within [2,10] is well captured, the fitted linear regression model $( y = 3 . 3 x - 3 . 6 1 )$ does not characterize the actual underlying function correctly. Hence, the use of a linear function is insufficient to fit the training samples.

2. Model overfitting: In contrast to model form error, if we fit a very complex model, even though the model shows excellent performance in fitting the training data, its performance beyond the training data may be very poor. For example, Fig. 7(b) demonstrates the concept of model overfitting. Our target function is $y = \cos \left( 1 . 5 ^ { * } \pi ^ { * } x \right)$ . If we replace this simple function with a polynomial function with a high degree of freedom, it is observed that the polynomial function fits the training data well, but model predictions on testing samples have a very high variance. The consequence of model overfitting is obvious: the performance of the model is unstable when making predictions, and the trained model might not generalize well on the testing data. As a result, model overfitting carries a serious risk in AI/ML systems.

3. Variable inclusion error: variable inclusion error is the third type of model misspecification. In general, there are two kinds of variable inclusion error. In the first kind of error, significant variables that should be included in the model are omitted from the model for a variety of reasons (e.g., by mistake, on purpose). As a result of the omitted significant variable. the model is unable to characterize the underlying data-generation process, and eventually has omittedvariable bias. The second type of variable inclusion error is that irrelevant variables are included in the model. The inclusion of the irrelevant variable may lead to model overfitting.

Models that are misspecified are known to give rise to inaccurate parameter estimations, inconsistent error terms, and erroneous pre dictions. All these factors put together will lead to poor prediction performance on unseen data and biased consequences when making decisions [68]. It is of paramount importance to carefully examine the functional form and variables that are included in the AI/ML model to avoid omitted-variable bias or model overfitting.

## 2.2.3. Model prediction uncertainty

Last but not least, uncertainty in model parameters and the model structure is another type of risk inherent in AI/ML models. A variety of methods have been developed to quantify, propagate, and represent the uncertainty associated with the model parameter and model structure in model predictions using many types of measures [69–71], such as pre diction interval, predictive distribution, etc. Among them, the Bayesian method is a popular way to quantify the uncertainty in the model structure and the model parameters [72]. In the context of Bayesian inference, instead of having deterministic values for model parameters, a prior distribution is placed for each model parameter, and is then combined with the training data to infer the posterior distribution for every model parameter. With the derived posterior distributions, it al lows the use of predictive distributions to represent the uncertainty in the model parameters and model structure.

![](/api/attachments/5UX37JAM/fulltext/images/38e9994258e013906b5dfae1498c19aed2ad72415dee82ea8fbf99fb928d116f.jpg)  
(a)

![](/api/attachments/5UX37JAM/fulltext/images/896e9c16d31963bec79580415e9ea01654ddfd0eec86eb28b5488e68a3fa7f07.jpg)  
(b)  
Fig. 7. Illustration of misspecified models.

Fig. 8 illustrates the uncertainty in model prediction due to mea surement noise associated with the quantity of interest y. The observed data is represented by black solid dots; and they have different degrees of measurement noise. The length of the error bar indicates the level of inherent noise in the corresponding observation. The underlying func tion (target function) that we aim to infer is denoted by the green solid line. By leveraging probabilistic AI/ML models (e.g., Bayesian neural network, Gaussian process), the variability in the measurement noise is characterized and propagated to the model prediction level. As a consequence, we not only have a mean point estimate as represented by the purple solid line, but also an uncertainty bound denoted by the pink area to reflect the uncertainty in the model prediction. Clearly, the variability associated with the measurement noise poses a severe risk when leveraging AI/ML systems in risk-sensitive applications.

Uncertainty in model prediction plays an important role in affecting decision-making activities, and the quantified uncertainty is closely associated with risk assessment. In particular, uncertainty in model prediction underpins many crucial decisions related to life or safetycritical applications [73]. Predictions without measured uncertainty are neither predictions nor actionable in high-stakes environments. Typically, low variance (or spread of distribution) indicates low risk, and vice versa. Thus, it is essential to account for the uncertainty in model prediction when evaluating the risk in an AI/ML system.

Table 1 summarizes the types of risk existing in AI/ML systems described earlier. We report the key findings encompassing the root cause and potential outcomes that might result from each specific risk. Obviously, these heterogeneous sources of risks have adverse impact on the performance of the AI/ML model. In particular, in the case of adversarial attack and out-of-domain data, the AI/ML model could make a completely wrong judgement. In the last column of Table 1, we also report the occurrence frequency of these varied risks. The severity of these risks, their occurrence frequency as well as their potential adverse consequences are important considerations when adopting AI/ML-based solutions.

![](/api/attachments/5UX37JAM/fulltext/images/983b1616bed9c95fe90daa3b8f1d5935672d0d1461e2dd8265a30134e76bf5db.jpg)  
Fig. 8. Demonstration of model prediction uncertainty.

Table 1  
Summary of a broad range of risks in AI/ML systems.

<table><tr><td>Risk type</td><td>Root cause</td><td>Potential outcomes</td><td>Frequency</td></tr><tr><td>Data bias</td><td>Class not represented equally</td><td>Biased modelsBiased inference results</td><td>High</td></tr><tr><td>Dataset shift</td><td>Mismatch between training data and testing data</td><td>Erroneous inferences</td><td>High</td></tr><tr><td>Out-of-domain data</td><td>Unable to control model inputs</td><td>Wrong inferences</td><td>Low</td></tr><tr><td>Adversarial attack</td><td>Lack of model robustness</td><td>Misclassification</td><td>Low</td></tr><tr><td>Model bias</td><td>Data biasImproper model training</td><td>Biased modelsBiased inference results</td><td>High</td></tr><tr><td>Model mis-specification</td><td>Inappropriate model assumptions</td><td>Underfitting or overfittingPoor model inference performance</td><td>Medium</td></tr><tr><td>Model uncertainty</td><td>Noise in input dataUncertainty in model parameters</td><td>Uncertainty in model inferencesUncertainty in decision making</td><td>High</td></tr></table>

## 3. Systematic risk analysis and risk management needs

In Section 2, we describe several types of primary risks associated with data and models in a general AI/ML system. In this section, we discuss existing issues in the state-of-the-art studies, and highlight the urgent need for a systematic risk analysis and management framework to facilitate the realization of risk-aware AI/ML systems.

As mentioned earlier, although AI/ML has advanced rapidly, due to the lack of a systematic risk analysis and a reliability engineering framework, such systems have not witnessed an effective adoption in life and safety-critical applications in terms of breadth and depth. In recent vears, researchers have devoted attention to conducting risk analytics and reliability analysis of AI/ML systems from multiple facets. Extant studies in this domain can be roughly categorized into two principal classes: data quality monitoring and model reliability analysis. Fo example, Bosni´c and Kononenko [83] have provided an overview of the recent advances in the development of methodologies to estimate the model reliability of individual predictions in AI/ML systems. Rabanser et al. [84] developed an approach for detecting and characterizing dataset shift in multiple contexts with the hope of clearing the dataset shift roadblock obstructing the deployment of AI/ML models in critical applications. As shown in Table 2, we summarize the major findings in the relevant literature with an emphasis on developing risk analysis and risk management methods for AI/ML systems from the perspective of input data quality control and model reliability analysis.

Regardless of the tremendous progress as seen in the literature so far, several crucial issues remain to be addressed along the direction of risk analysis and risk management of AI/ML systems. To ensure that AI/ML systems operate safely in high-stakes environments, the following issues need to be addressed in a rigorous fashion:

(i) A systematic framework for risk modeling: Risk modeling is very useful, especially in risk-sensitive applications, such as selfdriving, medical diagnosis, aerospace etc. As introduced in Sec tion 2, AI/ML systems face a wide set of risks ranging from dataset shift to model bias. These risks arise from a wide range of sources and are quite diverse in terms of sources, characteristics and root causes. Most of the state-of-the-art studies focus on a single type of risk, such as dataset shift [82], adversarial attack [80], etc. These risks are often studied relatively independently of each other, and so there is a lack of a systematic framework to integrate them. To date, no study has attempted to develop an approach to connect these single dots together to form an end-toend pipeline consisting of a series of safety control checkpoints for handling the varied risks in a systematic fashion. Due to the inherent unpredictability and volatility of real-world settings, it is necessary to make AI/ML systems robust to a variety of unfore seen events that may arise from each type of risk. If any type of risk is not measured and managed properly, it can lead to cata strophic consequences in high-stakes decision settings. Hence, it is vitally important to safeguard the usage of AI/ML systems and adopt effective measures to reduce risks inherent in data and AI/ ML models to a minimum level following a systems engineeringbased approach.

(ii) Establishing a test bed for risk analysis: The extant literature lacks a unified benchmark problem to demonstrate the variety of risks described earlier. As indicated in the third column of Table 2, the application area and dataset used for model perfor mance validation varies from paper to paper. There is an urgent need to establish a test bed for transparent verification, valida tion, and assessment of the effectiveness and performance of different models and algorithms in safeguarding AI/ML systems against varied risks across the wide range of scenarios described earlier. The test bed will act as a public platform for fair and rigorous testing of new theories and methodologies, reduce the time to test new concepts, and facilitate the identification of shortcomings and advantages of each approach. The test bed will also increase our current understanding on the underlying mechanisms of each approach in protecting the corresponding AI/ML system from every specific type of risk. Another benefit is that the test bed will make it easy to compare the performances of different models side by side, thus directing future research in improving model performance and accelerating the development of advanced methodologies for risk analysis and management.

Table 2  
A summary of recent progress on methods that are developed for risk and reliability analysis of AI/ML systems.\*

<table><tr><td>The solution (study)</td><td>Type</td><td>Application area</td><td>Key findings</td></tr><tr><td>Schulam Saria [74]</td><td>M</td><td>Healthcare, energy, real estate, etc.</td><td>Develop a Resampling Uncertainty Estimation (RUE) algorithm to compute an uncertainty score for each individual model predictionRUE exploits the gradient and Hessian of the model&#x27;s loss functionAudit pointwise reliability of model predictions using the uncertainty of model prediction</td></tr><tr><td>Adomavicius and Wang [75]</td><td>M</td><td>Energy consumption, stock market forecast, Parkinson&#x27;s disease severity, etc.</td><td>Employ the estimated absolute prediction error as the indicator of individual prediction reliabilityDevelop a ML-based framework to estimate individual prediction reliability</td></tr><tr><td>Kukar and Kononenko [76], Saunders et al. [77]</td><td>M</td><td>Breast cancer, nuclear power plant, diabetes, primary tumor, voting, Iris classification</td><td>Quantify the differences in classifier&#x27;s probability between inductive and transductive steps for reliability assessment of single pointEstablish a transductive framework to generate the reliability estimate for each single example</td></tr><tr><td>Virani et al. [78]</td><td>M</td><td>Power grid, power demand classification, traffic sign recognition, Iris classification</td><td>Extend the Justified True Belief (JTB) theory for ML models to infer reliability of individual predictionsRegions in input space are divided as region of extrapolation (i.e., I don&#x27;t know), region of confusion (i.e., I may know), and region of trust (i.e., I know)Perform justification-oriented class assignment and leverage the abstaining mechanism to avoid making a class assignment if concrete evidence is missing</td></tr><tr><td>Fang et al. [39]</td><td>D</td><td>Multi-domain text sentiment classification</td><td>Cross-domain text sentiment classification when in-domain data is unavailableCombine sentiment information from other domains with a hand-picked opinion-ated word listConstruct latent space representation to fulfill the cross-domain sentiment classification</td></tr><tr><td>Mårtensson et al. [79]</td><td>D</td><td>Medical image analysis</td><td>Systematically investigate a CNN model performance in out-of-distribution (OOD) magnetic resonance imaging (MRI) dataCNN model performance drops significantly when applied to external clinical data</td></tr><tr><td>Anindya and Kantarcioglu [80]</td><td>D</td><td>Network traffic</td><td>Assess the impact of adversarial attacks on anomaly detection modelsDevelop a robust centroid-based clustering method to detect mimicry attacks</td></tr><tr><td>Lwowski Rios [81]</td><td>D</td><td>Social media</td><td>Explore the impact of biases of different ML models on detecting influenza-related contentThe resulting ML models for influenza-related tasks using social media data are biased</td></tr><tr><td>Subbaswamy et al. [82]</td><td>D</td><td>Sepsis diagnosis</td><td>Evaluate the stability and robustness of ML models to distributional shiftFormally define distributional shifts and establish a sampling-based approach to estimate model performance under distributional shifts</td></tr></table>

Last but not least, the meticulously fine-tuned and representative tests in the test bed can assist government agencies (e.g., food and drug administration, aviation agency) for certifying AI/ML sys tems before they go to the market by identifying flaws, loopholes, and deficiencies in the design of AI/ML systems in advance.

(iii) Systematic representation of failure modes in AI/ML sys tems: Facing a broad array of risks that are heterogeneous in nature, it is an essential task to leverage the expertise in risk and reliability engineering to ensure that the AI/ML systems perform as intended and do not lead to errors. A prerequisite along this front is to adopt the common practices in the risk and reliability engineering discipline to identify the failure modes, root causes, occurrence probability, as well as the consequences associated with each failure mode in AI/ML systems. Such information can be collected, analyzed, and represented using the event tree or Bayesian network approaches that are commonly used in the field of risk and reliability engineering. The conjunction of risk and reliability engineering and AI/ML systems will significantly enhance our ability to diagnose the root cause of abnormal events when AI/ML systems malfunction.

The benefits of developing a diagram to systematically represent system failure modes are multi-fold. First of all, the diagram on system failure modes will greatly facilitate the systematic reasoning about risk, uncertainty, and their catastrophic outcomes in AI/ML systems. Sec ondly, the identification of system failure modes will build a strong foundation for the development of safety control checkpoints to prevent AI/ML systems from unintended outcomes. The developed safety control checkpoints can also be integrated into the existing software develop ment and security practices to constrain the use of AI/ML systems within a safe zone. More importantly, the information associated with system failure modes can be appropriately accommodated in the objective function of AI/ML models so as to formulate a risk-driven objective function when developing AI/ML models. The inclusion of system fail ure modes in the objective function will direct the optimization algo rithm to develop prudential and cautious behavior when handling cases that come with severe consequences.

(iv) Need for a risk management framework that is dedicated to AI/ML systems: Rather than relying on a traditional risk man agement framework, a dedicated risk management framework for AI/ML systems needs to be developed as AI/ML systems pose unfamiliar risks and create new challenges that are quite different in characteristics from the risks we have observed and dealt with before. As our reliance on AI/ML systems continues to grow, so does the risk. AI/ML systems have created a new broad range of risk types, such as compliance [79], algorithmic defects & risks [81], environmental changes, legal, and regulatory risks [82]. A large proportion of these risks exhibit characteristics that are quite different from the risks in financial systems that we have encountered before. Up to now, there are no well-established risk management models and frameworks with a long history of widespread adoption that can manage the risks in AI/ML systems. Traditional risk modeling methods that are widely used in the financial industries (e.g., market risk, value at risk–VaR, credit risk etc.) may not be applicable for characterizing the varied and diverse risks arising from the widespread use of AI/ML systems, such as legal risk, compliance risk, and model defects risk, etc. In addition, traditional model risk management (MRM) typically takes 6 to 12 weeks of review time, and it is difficult to adopt it to the fast-pace and agile iterations during the development of AI/ ML models [63]. As a result, there is a pressing need for a risk management framework that can accommodate the features specific to the risks in AI/ML systems.

(v) Mapping uncertainty to risk: Although there is a wide range of methods to quantify the uncertainty in model prediction [74,76,77], an important component that is missing is how to verify and objectively validate the uncertainty arising from different models under various assumptions. In other words, how to verify that the derived uncertainty characterizes the reality, given that there are so many different ways to quantify uncer tainty. The lack of rigorous approaches for verification and vali dation of uncertainty poses a severe risk when adopting methods to measure uncertainty in in AI/ML systems. Besides, another critical component is missing for bridging uncertainty and risk. As a matter of fact, risk and uncertainty are quite different in nature. Uncertainty is concerned with the variability of an event outcome we are not sure abolut due to a lack of knowledge or imperfect information, whereas risk refers to the occurrence probability of hazardous (or bad) outcomes in an event. The risks that uncertainty imposes on system safety and key functionality need to be appropriately modeled and assessed.

It is essential to transform the quantitative uncertainty measures into risk metrics so that it can be directly used for decision making. In gen eral, three key elements are considered when characterizing a risk measure: the failure scenario (i.e., AI/ML model fails to make the right prediction), the probability of failure, and the economic and societal losses caused by the AI/ML system failure. However, state-of-the-art uncertainty quantification methods lack a sound approach for con necting the uncertainty measures with the likelihood of the actual value falling within the uncertainty measure (e.g., prediction interval, pre dictive distribution), although such information is essential for con verting uncertainty measures to risk metrics. By the mapping of uncertainty to risk, the situational awareness of decision makers will be improved substantially. When risk is above a certain threshold, an early warning can be sent to alert stakeholders so that they can adopt cautious measures.

## 4. Research challenges and opportunities

As described in Section 2, AI/ML systems face a broad range of risks arising from different sources, and they are quite different from each other in terms of their characteristics. There is an increasing demand for embedding risk analysis and risk management in the development pipeline of AI/ML systems. In this section, we highlight several research challenges that may be faced along the development of risk-aware AI/ ML systems, as discussed below.

1. Black-box nature of certain AI/ML models. Among AI/ML sys tems, deep learning models, as an important branch, have developed rapidly in recent years. However, the large number of model pa rameters and the complex model structure makes it extremely diffi cult to interpret predictions made by the model. Although there has been tremendous progress in the development of interpretable deep learning models [85,86], most of the existing studies focus on using sensitivity analysis to show the relevance or correlation (e.g., salience map) between model inputs and model predictions. There is no universally accepted definition on interpretability, and a quanti tative end-to-end interpretable framework with the ability for inference (e.g., forward propagation, backward inference) that works like a Bayesian network is still lacking. The black-box nature of deep learning models increases the difficulty of deriving failure mechanisms as well as the probability of each failure mode for a given AI/ML system.

2. High computational burden. As there is no analytical solution to extract failure mechanisms in AI/ML systems, it is computationally expensive to estimate the occurrence probability of each failure mode through exhaustive enumeration of all combinations of model inputs via sampling-based methods, such as Monte Carlo sampling. This means that an enormous amount of data needs to be generated to derive an accurate failure probability associated with each failure mode. Some failure modes may have an extremely low occurrence probability, which is also referred to as a rare event. In addition, in deep learning models, as the sensitivity of model parameters to the perturbation of model inputs is highly complex (see the adversarial example shown in Fig. 6), it is challenging to simplify the data sampling process to reduce the computational effort. All the factors combined together significantly increase the computational burden for building a diagram to represent failure modes in AI/ML systems.

3. Domain-specific risk conceptualization. The nature and extent of risk varies from one field to another. To effectively embed risk management in AI/ML systems, it is important to work closely with domain experts to develop appropriate risk conceptualization for the understanding, assessment, and management of risk. Along this front, the treatment of varied uncertainties need to be connected with the basic theories, principles, and methodologies for risk quantification, assessment and management in a reasonable manner. Domain-specific risk conceptualization is an important step before embedding risk management in AI/ML systems. However, the risk conceptualization process involves a great deal of human in teractions and subjective human judgements, which may slow down the progress of risk conceptualization. It is worth investigating how to achieve objective risk conceptualization through data exchange and integration by fusing the data from different sources.

In order to ensure the reliable operations of high-stakes AI/ML sys tems, there is great potential to combine AI/ML systems with practices that are commonly used in other disciplines (e.g., reliability engineer ing, quality engineering, safety engineering, risk engineering, drug development regulation, etc) to ensure product and system quality and reliability. There are many opportunities to exploit the expertise and knowledge accumulated in these fields and incorporate them in AI/ML systems so as to ensure that AI/ML systems perform as intended. The opportunities along the development of risk-aware AI/ML systems can be grouped into the following categories:

1. Defining the safety margin for AI/ML systems: The ultimate goal of defining and quantifying risks present in the input data and model prediction is to make the AI/ML system aware of its limitations in the complex decision environment, such that it can identify strange” inputs or off-nominal situations, take appropriately preventive measures, and inform end users in a timely manner when the overall risk is above a threshold and the system is no longer able to make reliable predictions or decisions. Along this front, we can leverage the safety margin concept that is widely used in aviation engineering to ensure flight safety [87]. In the context of aviation engineering, the safety margin is defined as the distance” that the present flight is away from the accident boundary. Likewise, we can adopt a similar approach in AI/ML systems, and a safety margin varying with the specific risk level can be defined to reflect the distance of the investigated case away from the accident boundary. In addition, safety zones with different levels of reliability (e.g., high, medium, low) can be identified for a given AI/ML system. A safety margin can be used in conjunction with the safety zone to ensure the safe operation of AI/ML systems.

2. Reliability-based design of AI/ML systems. Reliability engineer ing is the discipline that bridges safety and AI/ML systems, and it seeks to ensure that a system performs as intended. Hence, it is useful to investigate popular concepts in the field of reliability engineering and incorporate them in AI/ML systems, such as the reliability test, fault tolerance, condition-based maintenance, reliability-based design, etc. For example, a reliability test can be performed in AI/ ML systems with respect to model inputs, subject to a predefined degree of variance. In addition, element-wise model prediction reliability $p ( | y - { \widehat { y } } | \leq \varepsilon | \mathbf { x } )$ can be formulated to indicate the proba bility of the actual value falling within a given range so as to provide more informative insights on point-wise model reliability. Model reliability can also be modeled as a constraint in the objective function of the AI/ML model so as to develop AI/ML systems subject to the requirement of a minimum model reliability.

3. Verification and validation of risk analysis and risk manage ment approaches. Prior to the deployment of risk analysis and management methodologies in real-world settings, an important step is to verify and validate the correctness of the computational results of the developed approach in a variety of scenarios to make sure that it meets the design specifications and requirements. In addition, the decision making procedures in risk analysis and risk management methods need to be transparent so that reasoning and justification can be provided with respect to the risk associated with each case on an objective manner. The explicit risk analysis procedures facilitate the diagnosis of the developed approach if it malfunctions in some scenarios, thus guiding the future directions for improving the pro posed method for risk analysis.

## 5. Theoretical and practical implications

In this paper, we provide a comprehensive review on prevailing risks in AI/ML systems and highlight the key research needs to facilitate the realization of risk-aware AI/ML systems. The nuanced understanding of AI/ML systems through a risk analysis lens has essential significance for theoretical developments and practical implementation.

The thorough comprehension of the characteristics of different sources of risks and the adverse outcomes they might lead to serves as a starting point in the subsequent development of an integrative approach for a holistic risk assessment and management in AI/ML systems. Examining how these different types of risks and their effects emerge and unfold individually and collectively will inspire the leveraging of well-established theories and practices in other domains (i.e., reliability engineering, aviation safety engineering, system engineering, software engineering). In the long run, this will spark the development of appropriate policies, novel approaches, effective safeguards, and con crete actions to improve the situation awareness in risk management during the lifespan of AI/ML systems.

On the other hand, this paper also has significant practical implica tions. The heterogeneous sources of risks pose a serious challenge when organizations adopt AI/ML solutions in practice. Hence, companies need to consider the benefits and potential adverse outcomes as well as the legal issues arising from adopting AI/ML solutions. Towards this end, AI/ML solutions need to be scrutinized with caution and rigor especially in high-stakes decision environments. Dedicated managerial capacity and resources need to be allocated to adapt the existing risk assessment and management practices in place to suit the unique needs for AI/ML development. Proper workflow and procedures need to be established to actively monitor the risk of adopting AI/ML in dynamic environments. Cases where AI/ML solutions are not in line with the regulatory re quirements need to be pre-emptively identified to reduce the liability of the company.

## 6. Conclusions

In this paper, we comprehensively review the primary sources of risks inherent in AI/ML systems that are closely related to model pre diction performance from two perspectives: data-related risk (e.g., data bias, dataset shift, adversarial attack, and out-of-domain data) and model-related risk (e.g., model bias, model misspecification, and model prediction uncertainty). Careful and rigorous examination of varied risks in AI/ML systems is an important step before fully exploring the applications of AI/ML systems in high-stakes decision-making environ ments. As AI/ML systems introduce a broad set of risks with unique characteristics that cannot be identified and managed with the tradi tional risk management framework, there is a pressing need for devel oping a risk analysis and management framework that is tailored to AI/ ML systems. Towards this end, we highlight several pressing issues that need to be addressed rigorously, but have not been investigated. Our hope is that this work will motivate researchers to develop innovative means to systematically identify, assess, and manage risks inherent in AI/ML systems for the sake of increasing the credibility in adopting and safeguarding their usage in risk-sensitive environments.

## CRediT authorship contribution statement

Xiaoge Zhang: Conceptualization, Methodology, Funding acquisi tion, Writing – original draft. Felix T.S. Chan: Writing – review & editing. Chao Yan: Methodology. Indranil Bose: Methodology, Writing – review & editing.

## Acknowledgements

The work described in this paper was supported by the Innovation and Technology Commission of The Hong Kong SAR Government, and the Research Committee of The Hong Kong Polytechnic University under project code 1-BE6V.

## References

[1] J. Guo, W. Zhang, W. Fan, W. Li, Combining geographical and social influences with deep learning for personalized point-of-interest recommendation, J. Manag. Inf. Svst. 35 (4) (2018) 1121–1153.

[2] S. Ding, Y. Li, D. Wu, Y. Zhang, S. Yang, Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model, Decis. Support. Syst. 107 (2018) 103–115.

[3] Y. Guan, O. Wei, G. Chen, Deep learning based personalized recommendation with multi-view information integration, Decis. Support. Syst. 118 (2019) 58–69.

[4] W. Zhou, G. Kapoor, Detecting evolutionary financial statement fraud, Decis Support. Syst. 50 (3) (2011) 570–575.

[5] E. Kim, J. Lee, H. Shin, H. Yang, S. Cho, S.-K. Nam, Y. Song, J.-A. Yoon, J.-I. Kim, Champion-challenger analysis for credit card fraud detection: hybrid ensemble and deep learning, Expert Syst. Appl. 128 (2019) 214–224.

[6] M. Al-Qizwini, I. Barjasteh, H. Al-Qassab, H. Radha, Deep learning algorithm for autonomous driving using GoogLeNet, in: 2017 IEEE Intelligent Vehicles Symposium (IV), IEEE, 2017, pp. 89–96.

[7] Y. Tian, K. Pei, S. Jana, B. Ray, Deeptest: Automated testing of deep-neural network-driven autonomous cars, in: Proceedings of the 40th International Conference on Software Engineering, 2018, pp. 303–314.

[8] D. Shin, S. He, G.M. Lee, A.B. Whinston, S. Cetintas, K.-C. Lee, Enhancing social media analysis with visual data analytics: a deep learning approach, MIS Q. 44 (4) (2020) 1459–1492.

[9] P. Adamopoulos, A. Ghose, V. Todri, The impact of user personality traits on word of mouth: text-mining social media platforms. Inf, Syst. Res. 29 (3) (2018)

[10] J. Qiu, C. Liu, Y. Li, Z. Lin, Leveraging sentiment analysis at the aspects level to predict ratings of reviews. Inf, Sci, 451 (2018) 295–309.

[11] G. Park, M. Song, Predicting performances in business processes using deep neural

[12] N. Chaudhuri, G. Gupta, V. Vamsi, I. Bose, On the platform but will they buy? Predicting customers’ purchase behavior using deep learning, in: Decision Support Systems, 2021, p. 113622.

[13] X. Zheng, S. Zhu, Z. Lin, Capturing the essence of word-of-mouth for social supervised approach, Decis, Support, Syst, 56 (2013) 211–222.

[14] M. Gebresselassie. T.W. Sanchez, “Smart" tools for socially sustainable transport: a review of mobility apps, Urban Sci. 2 (2) (2018) 45

[15] L. Backstrom, Serving a billion personalized news feeds, in: Proceedings of the Ninth ACM International Conference on Web Search and Data Mining, 2016, p. 469.

[16] B. Xiao, I. Benbasat, An empirical examination of the influence of biased personalized product recommendations on consumers’ decision making outcomes. Decis. Support, Syst. 110 (2018) 46–57.

[17] N.S. Madhukar, P.K. Khade, L. Huang, K. Gayvert, G. Galletti, M. Stogniew, J. E. Allen, P. Giannakakou, O. Elemento, A Bayesian machine learning approach for drug target identification using diverse data types, Nat. Commun. 10 (1) (2019)

[18] H. Luo, Q. Zhao, W. Wei, L. Zheng, S. Yi, G. Li, W. Wang, H. Sheng, H. Pu, H. Mo, et al., Circulating tumor DNA methylation profiles enable early diagnosis, prognosis

prediction, and screening for colorectal cancer, Sci. Transl. Med. 12 (524) (2020) eaax7533.

[19] J. Wiens, S. Saria, M. Sendak, M. Ghassemi, V.X. Liu, F. Doshi-Velez, K. Jung, K. Heller, D. Kale, M. Saeed, et al., Do no harm: a roadmap for responsible machin learning for health care, Nat. Med. 25 (9) (2019) 1337–1340.

[20] Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian. https://www.bbc. com/news/technology-54175359. Accessed: 2020-08-28.

[21] Uber’’s self-driving operator charged over fatal crash. https://www.ntsb. gov/news/events/Documents/2019-HWY18MH010-BMG-abstract.pdf. Accessed: 2020-08-28.

[22] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, Y. Bengio, Generative adversarial nets, Advances in Neural Information Processing Systems 27.

[23] K. Eykholt, I. Evtimov, E. Fernandes, B. Li, A. Rahmati, C. Xiao, A. Prakash, T. Kohno, D. Song, Robust physical-world attacks on deep learning visual classification, in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018, pp. 1625–1634.

[24] A. Meyer, D. Zverinski, B. Pfahringer, J. Kempfert, T. Kuehne, S.H. Sündermann, C. Stamm, T. Hofmann, V. Falk, C. Eickhoff, Machine learning for real-time prediction of complications in critical care: a retrospective study, Lancet Respir. Med. 6 (12) (2018) 905–914.

[25] H.A. Dolatsara, Y.-J. Chen, C. Evans, A. Gupta, F.M. Megahed, A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint, Decis. Support. Syst. 137 (2020), 113363.

[26] J.-S. Chou, T.-K. Nguyen, Forward forecast of stock price using sliding-window metaheuristic-optimized machine-learning regression, IEEE Trans. Indust. Inform. 14 (7) (2018) 3132–3142.

[27] B. Nushi, E. Kamar, E. Horvitz, Towards accountable ai: Hybrid human-machine analyses for characterizing system failure, in: Proceedings of the AAAI Conference on Human Computation and Crowdsourcing vol. 6, 2018.

[28] A. Tsanas, M.A. Little, P.E. McSharry, L.O. Ramig, Accurate telemonitoring of Parkinson’s disease progression by noninvasive speech tests, IEEE Trans. Biomed. Eng. 57 (4) (2009) 884–893.

[29] B. Gao, N. Hu, I. Bose, Follow the herd or be myself? An analysis of consistency in behavior of reviewers and helpfulness of their reviews, Decis. Support. Syst. 95 (2017) 1–11.

[30] J. Buolamwini, T. Gebru, Gender shades: Intersectional accuracy disparities in commercial gender classification, in: Conference on Fairness, Accountability and Transparency, PMLR, 2018, pp. 77–91.

[31] R. Baeza-Yates. Data and algorithmic bias in the web. in: Proceedings of the 8th

[32] S. Piramuthu, G. Kapoor, W. Zhou, S. Mauw, Input online review data and related bias in recommender systems. Decis. Support. Syst. 53 (3) (2012) 418–424

[33] Amazon reportedly scraps internal AI recruiting tool that was biased against women. https://www.theverge.com/2018/10/10/17958784/airecruiting-tool-bias-amazon-report 2021.

[34] R. Richardson, J.M. Schultz, K. Crawford, Dirty data, bad predictions: how civil rights violations impact police data, predictive policing systems, and justice, NYUL Rev, Online 94 (2019) 15

[35] J. Quinonero-Candela, ˜ M. Sugiyama, N.D. Lawrence, A. Schwaighofer, Dataset Shift in Machine Learning, MIT Press. 2009.

[36] A. Storkey, When training and test sets are different: characterizing learning transfer, Dataset Shift Machine Learn. 30 (2009) 3–28.

[37] A. Subbaswamy, S. Saria, From development to deployment: dataset shift, causality, and shift-stable models in health AI, Biostatistics 21 (2) (2020) 345–352.

[38] J.G. Moreno-Torres, T. Raeder, R. Alaiz-Rodrguez, N.V. Chawla, F. Herrera. A unifying view on dataset shift in classification, Pattern Recogn. 45 (1) (2012) 521–530.

[39] F. Fang, K. Dutta, A. Datta, Domain adaptation for sentiment classification in light of multiple sources, INFORMS J. Comput. 26 (3) (2014) 586–598.

[40] A.J. Smola, B. Scholkopf, ¨ Learning with Kernels vol. 4, 1998. Citeseer.

[41] M. Sugiyama, M. Krauledat, K.-R. Müller, Covariate shift adaptation by importanc weighted cross validation., J. Mach. Learn. Res. 8 (5).

[42] M. Sugiyama, T. Suzuki, S. Nakajima, H. Kashima, P. von Bünau, M. Kawanabe, Direct importance estimation for covariate shift adaptation. Ann. Inst. Stat. Math 60 (4) (2008) 699–746

[43] G.I. Webb, K.M. Ting, On the application of ROC analysis to predict classification performance under varying class distributions, Mach. Learn. 58 (1) (2005) 25–32.

[44] X. Zhang, S. Mahadevan. Ensemble machine learning models for aviation incident risk prediction, Decis. Support. Syst. 116 (2019) 48–63.

[45] J. Dressel, H. Farid, The accuracy, fairness, and limits of predicting recidivism, Sci. Ady, 4 (1) (2018), eaao5580

[46] A. Biswas, S. Mukherjee, Ensuring fairness under prior probability shifts, in: Proceedings of the 2021 AAAI/ACM Conference on AI. Ethics, and Society, 2021 pp. 414–424.

[47] J. Gama, I. Zliobaite, <sup>ˇ</sup> A. Bifet, M. Pechenizkiy, A. Bouchachia, A survey on concept drift adaptation, ACM Comput. Surv. 46 (4) (2014) 1–37.

[48] L.L. Minku, X. Yao, DDD: a new ensemble approach for dealing with concept drift, IEEE Trans. Knowl. Data Eng. 24 (4) (2011) 619–633.

[49] J. Lu, A. Liu, F. Dong, F. Gu, J. Gama, G. Zhang, Learning under concept drift: a review, IEEE Trans. Knowl. Data Eng. 31 (12) (2018) 2346–2363.

[50] J. Du, J. Rong, H. Wang, Y. Zhang, Neighbor-aware review helpfulness prediction, Decis, Support, Syst, 113581 (2021).

[51] M. Zhang, Z. Cui, M. Neumann, Y. Chen, An end-to-end deep learning architecture for graph classification. in: Thirty-Second AAAI Conference on Artificia Intelligence, 2018.

[52] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (7553) (2015) 436–444.

[53] X. Zhang, S. Mahadevan, Bayesian neural networks for flight trajectory prediction and safety assessment, Decis. Support. Syst. 131 (2020), 113246.

[54] W.J. Scheirer, A. de Rezende Rocha, A. Sapkota, T.E. Boult, Toward open set recognition, IEEE Trans. Pattern Anal. Mach. Intell. 35 (7) (2012) 1757–1772.

[55] Y. Zheng, G. Chen, M. Huang, Out-of-domain detection for natural language understanding in dialog systems, IEEE/ACM Trans. Audio, Speech. Language Proc. 28 (2020) 1198–1209.

[56] H. Yuan, J. Zheng, Q. Ye, Y. Qian, Y. Zhang, Improving fake news detection with domain-adversarial and graph-attention neural network, Decis. Support. Syst. 113633 (2021).

[57] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, R. Fergus, Intriguing properties of neural networks, in: 2nd International Conference on Learning Representations 2014, ICLR, 2014.

[58] D.J. Miller, Z. Xiang, G. Kesidis, Adversarial learning targeting deep neural network classification: a comprehensive review of defenses against attacks, Proc IEEE 108 (3) (2020) 402–433.

[59] X. Huang, D. Kroening, W. Ruan, J. Sharp, Y. Sun, E. Thamo, M. Wu, X. Yi, A survey of safety and trustworthiness of deep neural networks: verification, testing, adversarial attack and defence, and interpretability, Comp. Sci. Rev. 37 (2020), 100270.

[60] Failure Modes in Machine Learning. https://docs.microsoft.com/en-us/security/e ngineering/failure-modes-in-machine-learning. Accessed: 2020-08-28.

[61] R. Baeza-Yates, Bias on the web, Commun. ACM 61 (6) (2018) 54–61.

[62] D. Danks, A.J. London, Algorithmic bias in autonomous systems, in: Proceedings of the 26th International Joint Conference on Artificial Intelligence, 2017, pp. 4691–4697.

[63] B. Babel, K. Buehler, A. Pivonka, B. Richardson, D. Waldron, Derisking machine learning and artificial intelligence, McKinsey Quarterly. Business Technology Office.

[64] G. Zhang, Y. Lu, Bias-corrected random forests in regression, J. Appl. Stat. 39 (1)

[65] N. Mehrabi. F. Morstatter. N. Saxena. K. Lerman. A. Galstvan. A survey on bias and

[66] N. Kordzadeh, Investigating bias in the online physician reviews published on healthcare organizations' websites. Decis. Support. Syst. 118 (2019) 70–82

[67] O.A. Osoba, W. Welser IV, An Intelligence in our Image: The Risks of bias and Errors in Artificial Intelligence, Rand Corporation, 2017.

[68] K. Kuang, R. Xiong, P. Cui, S. Athey, B. Li, Stable prediction with model misspecification and agnostic distribution shift, in: Proceedings of the AAAI Conference on Artificial Intelligence 34, 2020, pp. 4485–4492.

[69] A. Khosravi, S. Nahavandi, D. Creighton, A.F. Atiya, Comprehensive review of neural network-based prediction intervals and new advances, JEEE Trans. Neural Netw, 22 (9) (2011) 1341–1356

[70] M. Abdar, F. Pourpanah, S. Hussain, D. Rezazadegan, L. Liu, M. Ghavamzadeh, P. Fieguth, X. Cao, A. Khosravi, U. R. Acharya, et al., A review of uncertainty quantification in deep learning: techniques, applications and challenges, Information Fusion.

[71] X. Zhang, F.T. Chan, S. Mahadevan, Explainable machine learning in image classification models: an uncertainty quantification perspective, Knowl.-Based Syst. 108418 (2022).

[72] R.M. Neal, Bayesian Learning for Neural Networks vol. 118, Springer Science &

[73] E. Begoli, T. Bhattacharya, D. Kusnezov, The need for uncertainty quantification in machine-assisted medical decision making, Nat. Mach. Intel. 1 (1) (2019) 20–23.

[74] P. Schulam, S. Saria, Can you trust this prediction? Auditing pointwise reliability after learning, in: The 22nd International Conference on Artificial Intelligence and Statistics 1022–1031, PMLR. 2019.

[75] G. Adomavicius, Y. Wang, Improving reliability estimation for individual numeric predictions: a machine learning approach, INFORMS J. Comput., doi: https://doi. org/10.1287/jioc.2020.1019. Published Online.

[76] M. Kukar, I. Kononenko, Reliable classifications with machine learning, in: European Conference on Machine Learning 219–231, Springer, 2002.

[77] C. Saunders, A. Gammerman, V. Vovk, Transduction with confidence and Intelligence. 1999, pp. 722–726

[78] N. Virani, N. Iyer, Z. Yang, Justification-based reliability in machine learning, in: pp. 6078–6085.

[79] G. Mårtensson, D. Ferreira, T. Granberg, L. Cavallin, K. Oppedal, A. Padovani.

deep learning model in clinical out-of-distribution MRI data: a multicohort study, Med. Image Anal. 66 (2020), 101714.

[80] I.C. Anindya, M. Kantarcioglu, Adversarial anomaly detection using centroid-based clustering, in: 2018 IEEE International Conference on Information Reuse and Integration (IRD).1-8. JEEE. 2018

[81] B. Lwowski, A. Rios, The risk of racial bias while tracking influenza-related content on social media using machine learning, J. Am. Med. Inform. Assoc. 28 (4) (2021) 839–849.

[82] A. Subbaswamy, R. Adams, S. Saria, Evaluating model robustness and stability to dataset shift. in: International Conference on Artificial Intelligence and Statistics 2611-2619, PMLR, 2021.

[83] Z. Bosni´c, I. Kononenko, An overview of advances in reliability estimation of individual predictions in machine learning, Intell. Data Anal. 13 (2) (2009) 385–401.

[84] S. Rabanser, S. Günnemann, Z. Lipton, Failing loudly: an empirical study of methods for detecting dataset shift, Adv. Neural Inf. Proces. Syst. 32 (2019) 1396-1408.

[85] L.M. Zintgraf, T.S. Cohen, T. Adel, M. Welling, Visualizing deep neural network decisions: Prediction difference analysis, in: The Fifth International Conference on Learning Representations (ICLR 2017), 2017.

[86] F. Hohman, H. Park, C. Robinson, D.H.P. Chau, S ummit: scaling deep learning interpretability by visualizing activation and attribution summarizations, IEEE Trans. Vis. Comput. Graph. 26 (1) (2019) 1096–1106.

[87] H.-S. Jing, C.-S. Sheng, Y.-F. Lin, Flight safety margin theory-a theory for the engineering analysis of flight safety, in: International Conference on Engineering Psychology and Cognitive Ergonomics 377–387, Springer, 2015.

![](/api/attachments/5UX37JAM/fulltext/images/2add52efb376d12e3eca7556bb09e545da0b024e04eb23515d1271dc2989f43b.jpg)

Xiaoge Zhang received his Ph.D. from Vanderbilt University in May 2019. Nashville. TN. From August to December in 2016. he interned at the National Aeronautics and Space Administration (NASA) Ames Research Center (ARC), Moffett Field, CA, working at the Prognostics Center of Excellence (PCoE) led by Dr. Kai Goebel. From August 2019 to February 2020, he worked as a Postdoctoral Research Scholar with Vanderbilt University. From March 2020 to August 2021, he worked as a Senior Op erations Research Analyst in the Operations Research & Spatia Analytics (ORSA) group FedEx Express, Memphis. TN. USA Since August 2021. he has joined the Department of Industrial and System Engineering at the Hong Kong Polytechnic University as an Assistant Professor. He was a recipient of the

Chinese Government Award for Outstanding Self-financed Students Abroad in 2017. He has published more than 40 research papers in leading academic journals, such as Risk Analysis, Decision Support Systems, International Journal of Production Research, IEEE Transactions on Cybernetics, IEEE Transactions on Reliability, IEEE Transactions on Intelligent Transportation Systems, Reliability Engineering and System Safety, and Annals of Operations Research, among others. His current research interests include risk analysis, reliability assessment, machine learning, and data science. He is a member of IEEE, IN FORMS, and SIAM

![](/api/attachments/5UX37JAM/fulltext/images/e7d4328c46e5b5cf2d42493f8821c1d3925d1b466330cce123b3d6fe22bd361b.jpg)

Felix T.S. Chan Prof. Felix Chan received his BSc Degree in Mechanical Engineering from Brighton University, UK, and obtained his MSc and PhD in Manufacturing Engineering from the Imperial College of Science and Technology, University of London, UK. Prior joining Macau University of Science and Technology, Prof. Chan has many years of working experience in other universities including The Hong Kong Polytechnic; University of Hong Kong; University of South Australia; Uni versity of Strathclyde. His current research interests are Logis tics and Supply Chain Management, Decision Making, AI Optimisation, Operations Research, Production and Operations Management. Distribution Coordination. To date. Prof, Chan has published over 16 book chapters, over 390 SCI refereed international journal papers and 320 peer reviewed international conference papers. His total number of citations >11,000, h Index = 54.

Chan is a chartered member of the Chartered Institute of Logistics and Transport in Hong Kong. Based on the recent compilations (2020) and (2021) from a research group of Stanford about the impact of scientists (top 2% listed). The work is published in the following website: https://journals.plos.org/plosbiology/article?id=10.1371/journal. pbio,3000918: Prof, Felix Chan is categorized in the field of Operations Research ranked 10 out of over 23.450 scientists worldwide. i.e.. Top 0.04% worldwide. for TwO consecutive vears (2020 and 2021)

![](/api/attachments/5UX37JAM/fulltext/images/91ff173fed143073a6328b87a0aa6b93f15230d3e883c878cb1c81f5fbc3e278.jpg)

Chao Yan is a post-doctoral fellow of the Department of Biomedical Informatics, Vanderbilt University Medical Center, Nashville, TN. USA. He is a member of Health Information Privacy Laboratory, which is a part of the Vanderbilt Health Data Science Center. He received his B.S. degree in network engineering from Southwest University in 2012, the M.S. de gree in computer science from the University of Chinese Academy of Sciences in 2015 (both in China), and the Ph.D. degree in computer science from Vanderbilt University, Nash ville, TN, USA. His research focuses on 1) representation learning and predictive modeling in the healthcare domain, 2) health data simulation via generative models, and 3) the mechanisms of anomaly detection/auditing for privacy pro

tection in healthcare organizations. He has published more than 30 peer-reviewed journa and conference papers, such as IEEE ICDE, IEEE CIC, IEEE ICHI, AAAI, American Medica Informatics Association Annual Symposium, ACM Transactions on Privacy and Security, Journal of the American Medical Informatics Association. Journal of Medical Internet Research, etc. He is a student editorial board member of Journal of the American Medica Informatics Association.

![](/api/attachments/5UX37JAM/fulltext/images/fc65040b9627a498873ad5390bcfd337c946eed6e8b7fa512d7278b16f5abb76.jpg)

Indranil Bose is Distinguished Professor of Management In formation Systems at the NEOMA Business School. He acts as Head of the Area of Excellence in Artificial Intelligence, Data Science, and Business. He holds a BTech from the Indian Institute of Technology, MS from the University of Iowa, and MS and PhD from Purdue University. His research interests are in business analytics, digital transformation, information se curity, and management of emerging technologies. His publi cations have appeared in MIS Quarterly, Journal of the MIS, Communications of the ACM, Communications of the AIS, Computers and Operations Research, Decision Support Sys tems, Electronic Markets, European Journal of Operational Research, Information & Management, International Journal of

Production Economics, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information Science and Technology, Operations Research Letters, Technological Forecasting and Social Change, etc. He serves as Senior Editor of Decision Support Systems and Pacific Asia Journal of the AIS, and as Associate Editor of Communications of the AIS, Information & Management, and Journal of the AIS.
