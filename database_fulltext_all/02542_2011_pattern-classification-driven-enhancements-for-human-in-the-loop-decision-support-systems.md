---
otero_id: 2542
otero_key: "5CV8SZHR"
title: "Pattern classification driven enhancements for human-in-the-loop decision support systems"
authors: "Halasya Siva Subramania; Vineet R. Khare"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Pattern classi<sup>fi</sup>cation driven enhancements for human-in-the-loop decision support systems

Halasya Siva Subramania ⁎<sup>,1</sup>, Vineet R. Khare

Diagnosis & Prognosis Group, India Science Lab, General Motors Global Research and Development, GM Technical Centre India Pvt Ltd, Creator Building, International Tech Park Ltd., Whitefield Road, Bangalore, 560 066, India

## a r t i c l e i n f o

Article history: Received 4 November 2009 Received in revised form 13 October 2010 Accepted 1 November 2010 Available online 5 November 2010

Keywords: Decision support systems Human expert Pattern classi<sup>fi</sup>cation Decision trees Support vector machines Confusion matrix

## a b s t r a c t

Data mining has been a key technology in the warranty sector for mass manufacturers to understand and improve product quality, reliability and durability. Cost savings is an important aspect of business which calls for processes that are error proof. Pattern classi<sup>fi</sup>cation methods applied to the diagnostic data could help build error proof processes by improving the diagnostic technology. In this paper we present a case study from the automotive warranty and service domain involving a human-in-the-loop decision support system (HIL-DSS). The automotive manufacturers offer warranties on products, made of parts from different suppliers, and rely on a dealer network to assess warranty claims. The dealers use diagnostic equipment manufactured by third parties and also draw on their own expertise. In addition, a subject matter expert (SME) assesses these collective decisions to distinguish between inaccurate diagnoses by the dealers or an inadequate decision algorithm in the diagnostic equipment. Altogether this makes a comprehensive HIL-DSS. The proposed methodology continuously learns from collective decision making systems, enhances the diagnostic equipment, adds to the knowledge of dealers and minimizes the SME involvement in the review process of the overall system. Improving the diagnostic equipment helps in better warranty servicing, whereas improvements in the human expert knowledge help prevent <sup>fi</sup>eld error and avoid customer dissatisfaction due to improper fault diagnosis

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

There are different kinds of decision support systems (DSS) — model driven, communication driven, data driven, document driven and knowledge driven [23]. Knowledge is gathered over time. It plays a crucial role in the decision making process. There are many ways of designing the DSS, namely — to incorporate all the possible factors under consideration which in real life can make the system very complicated. Realistically, only quanti<sup>fi</sup>able factors can be easily incorporated into the DSS and there is less possibility for the DSS to learn new information and update automatically. This suggests the DSS' limitations and incompleteness. Human experts on the other hand, can learn and use the knowledge gained to make decisions even based on factors that cannot be easily incorporated algorithmically. For instance, let us consider a scenario where human experts use limited/incomplete DSS to make actionable decisions but not blindly follow them, i.e. the humans use their expertise on top of the DSS to make the <sup>fi</sup>nal decision. This limited/incomplete DSS plus the human expertise (which can be a representation of a knowledge driven DSS)

forms a comprehensive system that we call a human-in-the-loop decision support system (HIL-DSS). Decisions made this way are quite common in real life setup, e.g. warranty and service domain and air traf<sup>fi</sup>c management [28].

In this paper, we will demonstrate the enhancements to the HIL-DSS using the warranty and service domain as an example. The warranty space is a complex and sensitive structure in the view of the manufacturer because it needs special handling to take into account the customer priority <sup>fi</sup>rst and still maintain pro<sup>fi</sup>tability. In such a case, there are several factors that need to be considered while designing the DSS. As an illustration, if we consider the automotive warranty domain, manufacturers de<sup>fi</sup>ne service procedures, provide diagnostic testing tools and train the dealers to provide service support to the customers. In modern vehicles, many diagnostic sensors are also inbuilt in the car to comply with government regulations [2]. These regulations are focused towards customer safety and environmental concerns. For parts like battery, air conditioning system and others, manufacturers depend either on built-in sensors [32] or on commercial testing equipment. For the latter, manufacturers choose testers [8,19] that satisfy their criteria and provide requirements to the tester-OEM (original equipment manufacturer) to adapt them to suit their needs. These testers are then deployed in the <sup>fi</sup>eld and dealer technicians are instructed to take appropriate action as per the tester outcomes. In the process, diagnostic data measured by the testers pertaining to repairs performed by the dealer technicians are mandatorily collected as part of the warranty claims. With high warranty costs, the manufacturers are apprehensive about many of the claims but they are restrained towards actions. The reason is two-fold — 1) the nature and large volume of claims that they cannot verify; and 2) the lack of adequate proof to back their apprehension. The incorrect/incomplete data provided by the dealers towards the claims usually adds to the confusion. More importantly, the manufacturer too may not know about all the factors that need to be collected in order to assess the correctness of the diagnosis and take subsequent action on every claim. Needless to say, understanding the completeness of the data collection is a continuous learning process.

Fig. 1, shows the current HIL-DSS used in the automotive warranty space. The various components involved in the HIL-DSS are described as follows:

• Scenario: The vehicle encounters a problem that requires it to be brought to the dealer for repair. A “scenario” is a representation of the failure.

• DSS: The diagnostic tester is the DSS used by the dealer for the assessment of the failed component in a given scenario.

• Human expert: The dealer technician, or the human expert, takes the liberty to take appropriate action based on his/her experience and does not rely entirely on the tester outcome. Although, the decisions through the human expertise and knowledge are expected to enhance the DSS, it also leaves an opportunity for <sup>fi</sup>eld errors to prevail.

• Subject matter expert: Humans with in-depth knowledge of the domain. These subject matter experts (SMEs) are capable of reviewing decisions made by the DSS or the human expert and recommend enhancements/improvements in the two (human knowledge or diagnostic tester algorithm).

Here it is important to stress the difference between the human experts and the subject matter experts. Human experts are part of the dealer network and make decisions on every scenario, while subject matter experts are part of the manufacturers who review those decisions made by the DSS and the human experts on a conditional basis.

In the current setup, both the DSS and the human expert can bene<sup>fi</sup>t from the decisions made by the SME. However, the large volume of claims prohibits a comprehensive SME review. In this paper, we present a novel approach based on pattern-classi<sup>fi</sup>cation to — 1) continuously learn from collective decision making systems; 2) enhance the limited/incomplete DSS; 3) add to the knowledge of human expertise; and 4) minimize the SME involvement in the review process of the overall system. A detailed description of various steps involved in our methodology is presented in Sections 4 and 6.

In brief, though the manufacturers provide requirements to the tester-OEM and the tester is modi<sup>fi</sup>ed to suit them, in the real world, the algorithm of the tester is not shared because of intellectual property issues. The absence of the tester algorithm adds to the dif<sup>fi</sup>culty of the subject matter experts in assessing the correctness of the claim outcomes. To overcome this, we fuse the tester outcomes with the human decisions and assume high con<sup>fi</sup>dence on the decisions being correct when they match. Pattern classi<sup>fi</sup>cation techniques [6,25] can be used to learn the underlying model from this agreement data. Outcomes from the learnt model on the disagreement data enables the manufacturers to (through a process of SME review):

![](/api/attachments/5CV8SZHR/fulltext/images/dd26722ba78b0069c03be7961a0331bac71c47b124d02ff1b344e8d62e959bae.jpg)  
Fig. 1. The current human-in-the-loop DSS used in automotive warranty space.

1. Request modi<sup>fi</sup>cation of current DSS algorithm or inclusion of new features to enhance the limited/incomplete DSS.

2. Train the human experts using the knowledge gained from this learning for better <sup>fi</sup>eld decision making.

To emphasize, the SME involvement in the overall process is reduced signi<sup>fi</sup>cantly as s/he is required to assess only the disagreement scenarios. The rest of the paper will focus on elaborating the methodology and present results based on a case study from the automotive domain. It is organized as follows. The following section discusses the motivation for this work, followed by a discussion on the related literature in Section 3 that the work builds on. Section 4 describes the proposed methodology for pattern classi<sup>fi</sup>cation driven enhancements for HIL-DSS. Section 5 describes an automotive warranty space case study in detail. Following this, the results are discussed in Section 6 and conclusions are drawn.

## 2. Motivation

Warranty is an integral part of any product these days. For “specialty products” which undergo a lot of scrutiny by the customers before the purchase [1], warranty assumes even greater importance. Better warranty signals better product quality and provides assurance to the customers. This drives manufacturers to follow the mantra of quality, reliability and durability. In spite of extensive testing, failures do happen (in accordance to the product reliability) and warranty provides coverage against these failures for a speci<sup>fi</sup>ed amount of time/usage.

Product reliability is in<sup>fl</sup>uenced by decisions made during the design and manufacturing phase of the product life-cycle [20,21]. In a domain such as automotive, the product reliability is dependent on various parts obtained from different suppliers, and warranty coverage is based on individual reliability information for the supplied parts. When a vehicle comes for a repair, the importance of proper diagnosis of the part failure cannot be over-emphasized. It is crucial for the following reasons:

1. It enables better warranty servicing, thereby results in customer satisfaction. It further enhances the brand image of the product.

2. It keeps the warranty cost low by avoiding repetitive failures.

3. It provides the manufacturer the crucial failure data to learn and adapt its warranty strategy.

While diagnosing a part failure there can potentially be two kinds of errors:

False negatives — Failure to diagnose faulty part. Diagnosing faults ef<sup>fi</sup>ciently by keeping false negatives minimal is a crucial part of service performance. These have a negative in<sup>fl</sup>uence on the brand image which impacts sales and revenue due to customer dissatisfaction.

False positives — Erroneous classi<sup>fi</sup>cation of a good part as faulty. False positives add to the warranty cost and product wastage results in environmental damage.

The limitations in the diagnostic procedure result in false negatives. False positives, however, may have other reasons – <sup>fi</sup>rstly, to keep the service performance high in the eyes of the customer, the diagnostic thresholds that qualify a part as faulty are set relatively wide, meaning – a few good parts are also diagnosed faulty and thrown out. Secondly, part replacement might be more lucrative and pro<sup>fi</sup>table from the dealer's viewpoint.

The issue of misdiagnosis, leading to high warranty claims and customer dissatisfaction, motivated the presented work. However, the proposed methodology is generic which not only allows learning from the <sup>fi</sup>eld data to improve the current DSS (and hence the diagnostic tool, in the aim of reducing false positives) but also aims at <sup>fi</sup>eld error prevention. In the process, customer perspective is still given the highest consideration.

## 3. Related literature review

The relevant literature speci<sup>fi</sup>c to the work presented, comes from a variety of <sup>fi</sup>elds — decision support systems, anomaly detection and pattern classi<sup>fi</sup>cation (confusion matrix, boosting, and multiple classi<sup>fi</sup>er systems).

Several decision support systems exist in various <sup>fi</sup>elds including automotive fault diagnosis and management, medical diagnosis, security, business management and air traf<sup>fi</sup>c control. In the design of a DSS, knowledge plays an important role. Hence, in real world systems, the design process has to be temporally adaptive irrespective of the availability of prior knowledge. The role of humans for decision making in addition to the DSS has been addressed in other research areas, such as air traf<sup>fi</sup>c management [28] and Internet security [9]. In [9], the need for a human-in-the-loop system to perform security critical functions is emphasized.

As mentioned in Section 1, we look into the human-in-the-loop decision support system (HIL-DSS) in the context of the warranty and service domain. In the current system (Fig. 1), the underlying algorithm of the DSS is not shared [8,19] in detail with manufacturers which makes the DSS, a black box DSS. Pattern classi<sup>fi</sup>cation methods of data mining come very handy in such a scenario where the underlying algorithm of a black box DSS can be learnt using the data collected from the DSS. This is true mainly for decision support systems that are designed to measure diagnostic factors upon which the decisions are based. Classi<sup>fi</sup>cation learning is sometimes called supervised learning because the method operates under supervision by being provided with the actual outcome for each case, i.e. the diagnostic factors represent the input features and the decisions are the outcomes which represent the target classes of the supervised learning techniques. There are many classi<sup>fi</sup>cation methods available with a wide variety of applications. The choice of the methods depends on the nature of the data because each method has its advantages and disadvantages in handling different aspects of the data. In this paper, the classi<sup>fi</sup>cation learning methods are not our focus but those chosen for our case study have been justi<sup>fi</sup>ed in Section 5.4.

Anomaly detection techniques can help in identi<sup>fi</sup>cation and prevention of misdiagnosis (<sup>fi</sup>eld errors), which is one of the goals of this work. In some previous works [5,18], generally two step strategies are followed for anomaly detection. First, anomalous data is separated from the good data and second, classi<sup>fi</sup>cation learning is applied to learn the “normal” model. This means, while testing the anomalous data using the normal model, the data that does not <sup>fi</sup>t the normal model are tagged as anomalies. In another work [11], a normal model is learnt using some assumptions while the test data does not necessarily contain only anomaly data but includes the learned classes as well. Authors in [11] propose anomaly detection support vector machines (ADSVM) which uni<sup>fi</sup>es the classi<sup>fi</sup>cation and anomaly detection, and provides a multiclass extension. The methodology that we propose, uses the two step strategy of learning a normal model and then testing, but it also uni<sup>fi</sup>es classi<sup>fi</sup>cation and anomaly detection.

There are several factors that evaluate a classi<sup>fi</sup>er — speed, robustness, scalability and interpretability [13]. Confusion matrix [16] is a visualization tool used in pattern classi<sup>fi</sup>cation (typically supervised learning) to assess the performance of a classi<sup>fi</sup>er. It contains information about the actual and predicted classi<sup>fi</sup>cations done by a classi<sup>fi</sup>er. It is particularly useful when the dataset is imbalanced (a lot of instances from one class and only a few from the other). In our context, however, we use confusion matrix to determine instances which can help make improvements in the diagnostic tester and also discover potential <sup>fi</sup>eld errors (Section 5.3.1). Subject matter expertise is required to interpret misclassi<sup>fi</sup>ed cases accounted in the confusion matrix and also to validate the learnt algorithm.

As mentioned earlier, the choice of classi<sup>fi</sup>ers depends on the dataset. In pattern classi<sup>fi</sup>cation literature, multiple classi<sup>fi</sup>er systems are used to improve classi<sup>fi</sup>cation performance. It is well known fact that, classi<sup>fi</sup>er combinations outperform single classi<sup>fi</sup>ers either because they have statistical advantages or because they perform problem decomposition [14]. Examples of combinations are — averaging and voting. In simple averaging [22] and simple voting [3] all member networks are trained, independently, on complete datasets but have different initial conditions, hence they converge to local minima of the error function used for training. These methods have been shown [4,17] to perform no worse than the average performance of all classi<sup>fi</sup>ers. In [15] authors propose a method for the prediction of the e-Commerce customer's purchase behavior by combining multiple classi<sup>fi</sup>ers based on genetic algorithm [12]. In the present work, we also combine the outcomes of two classi<sup>fi</sup>ers which is described as part of the case study.

In case of noisy data, boosting methods are useful to pull important information out of the data which can get buried in the noise under regular classi<sup>fi</sup>cation techniques. In boosting [10], member classi<sup>fi</sup>ers are trained on data sets with entirely different distributions and results of multiple classi<sup>fi</sup>ers or “weak” classi<sup>fi</sup>ers are combined into a “strong” classi<sup>fi</sup>er. In boosting-by-<sup>fi</sup>ltering [26] a strong learning model is built around a weak one by modifying the distribution of examples. For instance, three experts are arbitrarily labeled “<sup>fi</sup>rst”, “second” and “third”. The second expert is forced to learn a distribution entirely different from that learned by the <sup>fi</sup>rst and the third expert is forced to learn the parts of the distribution that are “hard-to-learn” by the <sup>fi</sup>rst and second experts. A boosting algorithm for a probabilistic decision support system is presented in [30,31], where the DSS proposed obtains rules from different sources (experts and databases). The <sup>fi</sup>nal decision is made based on different classi<sup>fi</sup>ers through voting. The organization of the voting system is based on the qualities of information sources. In this work, we use boosting to obtain more con<sup>fi</sup>dence on the results achieved. To be more speci<sup>fi</sup>c, we use two classi<sup>fi</sup>ers and compare the outputs. Agreement of the outputs from the two classi<sup>fi</sup>ers provides us with more con<sup>fi</sup>dence on the output being correct, especially in the absence of the ground truth.

## 4. Pattern classi<sup>fi</sup>cation approach to DSS enhancements

The fundamental components of our approach as shown in Fig. 2 are — the scenarios, the decision support system (DSS), human expert, the classi<sup>fi</sup>er model and the subject matter expert (SME). Following steps describe the proposed methodology for pattern classi<sup>fi</sup>cation approach to HIL-DSS enhancements:

Step 1 — Each scenario in the database is presented to the DSS, the DSS processes the scenario and suggests a decision.

Step 2 — The human expert then makes the decision by taking into account several other factors and the DSS decision.

Step 3 — The decisions by the DSS and the human expert are now combined. S/he might disagree with the DSS decision. The reason why the human expert chooses to differ from the DSS can be two-fold — 1) S/he is trying to incorporate some of the additional factors which are not quanti<sup>fi</sup>able and, thus, are not implemented in the DSS; or 2) S/he (un)intentionally made the incorrect decision. Let us call the subset of all the scenarios where there is disagreement, the disagreement data.

![](/api/attachments/5CV8SZHR/fulltext/images/0042be0300b7e8a4755900514fd2ba27722360dce5afa2727ad497f716bfa286.jpg)  
Fig. 2. Proposed methodology used for enhancing human-in-the-loop decision support systems

When the DSS decision and the human expert's decision are in agreement, we obtain the agreement data. For this data we have more con<sup>fi</sup>dence to make an assumption that the decision is correct.

Step 4 — Now we choose a pattern classi<sup>fi</sup>er and train it on the agreement data. The scenarios within this set provides us with the instances where we are con<sup>fi</sup>dent about the decision made being correct and should help us learn the underlying distribution behind the required decision making process.

Step 5 — The model learnt on the agreement data is now tested on the disagreement data.

Step 6 — Out of all the scenarios in the disagreement data, to determine whether the DSS or the human expert decision is incorrect, we compare the learnt model (which is assumed to have captured the characteristics of the underlying distribution) with the two decisions, respectively. Suggestions on enhancing the DSS are obtained from all the scenarios where the learnt model decision disagrees with the DSS decision. Similarly, the suggestions for improved decision making by the human experts are obtained from all the scenarios where the learnt model decision disagrees with the human expert decisions. For binary decisions, the decisions made by the DSS and the human experts are complementary on the disagreement data. In such a scenario, both the suggestions for improved decision making by the human experts and suggestions on enhancing the DSS can be obtained only by comparing the learnt model output with the human expert decisions (Fig. 2).

Step 7 — For the DSS improvement, the SME will use the learnt model to understand the rules (only applicable with C4.5) and assess them based on physics knowledge to suggest enhancements to the tester algorithm. The SME could also determine new factors that are in<sup>fl</sup>uencing the human expert decisions and capture them as part of the DSS. For the human expert knowledge improvement, the subject matter expert (SME) will separate the <sup>fi</sup>eld error scenarios from the rest and directives/training will be issued to the concerned human experts (technician/dealer).

The proposed method is to be used intermittently. It needs a critical mass of scenarios (warranty claims) to train the classi<sup>fi</sup>er model. Once the SME recommendations (for improvements in the diagnostic equipment and improvements in decision making by human experts) are implemented, the method is run again after t time interval for the continued improvements in the HIL-DSS method. Assuming this implementation takes t months, the method should be run every t + Δt months.

## 5. Automotive domain warranty space — a case study

Warranty assumes signi<sup>fi</sup>cance in more than one ways in the automotive domain. From the manufacturer's point of view, a good assessment of failures is quite crucial. This not only helps the manufacturer to remedy the problem and save on the high warranty costs, but also helps in building the brand image for the product. The pattern classi<sup>fi</sup>cation approach for DSS enhancements (Section 4) helps the manufacturer in both of these aspects. It aids the diagnostic process, thereby helping in improved customer satisfaction and reduced warranty costs. It also helps in detecting <sup>fi</sup>eld errors in the warranty management system which results in further savings. Various components of the methodology presented in Section 3 speci<sup>fi</sup>c to the case study are described in detail later.

## 5.1. Diagnostic tester (DSS) and field (human expert) decisions

As described in Section 1, commercially available diagnostic testers are used to test speci<sup>fi</sup>c components in a vehicle when it comes for repair. Manufacturers instruct dealers to use speci<sup>fi</sup>c testers and take action accordingly. The diagnostic information measured by the testers is mandated by the manufacturer to the dealer to provide as part of the warranty claims. The action taken by the dealers represents <sup>fi</sup>eld decisions (F). The action recommended by the tester represents tester decisions (T). The technician at the dealers sometimes takes action based on his/her experience than relying completely on the tester. Based on only the claim information, it is very dif<sup>fi</sup>cult for the manufacturer to infer which action is correct, either the one taken in the <sup>fi</sup>eld (F) or the one recommended by the tester (T). However, when they agree we have more con<sup>fi</sup>dence on the decision because both the technician's experience and the tester agree on the decision.

## 5.2. Data

The data selected for this study is a set of claims data, observed between September 2007 and May 2009, of the battery component which is tested using a diagnostic tester. The diagnostic information in the form of parameter values related to the component, provided with the claims consist of four parameters out of which two of them A, B are categorical and two of them C, D are continuous. The outcome of the tester is also available with each of the claims which are marked as tester decisions. The tester decisions are mainly based on the nature of the failure. At a high-level, the failure modes can be classi<sup>fi</sup>ed as repairable and irreparable or as “Good” and “Bad”, respectively. Table 1 illustrates the dataset showing typical values of the parameters and the outcomes.

Data in the aforementioned format is derived for two car brands — let us call them brand $B _ { 1 }$ and $B _ { 2 } .$ . The class distribution for the data corresponding to the two brands is shown in Fig. 3.

• For brand B there are in total 5417 scenarios. Out of which, for 5181 scenarios there is an agreement between the <sup>fi</sup>eld and the diagnostic tester decisions and in 236 scenarios they disagree. Out of the 5181 agreement scenarios, 5041 are classi<sup>fi</sup>ed as “Bad” and the rest are “Good”. And out of the 236 disagreement scenarios, 229 are classi<sup>fi</sup>ed as “Good” by the diagnostic tester and 7 are classi<sup>fi</sup>ed as “Good” in the <sup>fi</sup>eld.

• For brand $B _ { 2 }$ there are in total 24,312 scenarios. Out of which, for 23,442 scenarios there is an agreement between the <sup>fi</sup>eld and the diagnostic tester decisions and in 870 scenarios they disagree. Out of the 23,442 agreement scenarios, 22,998 are classi<sup>fi</sup>ed as “Bad” and the rest are “Good”. And out of the 870 disagreement scenarios, 833 are classi<sup>fi</sup>ed as “Good” by the diagnostic tester and 37 are classi<sup>fi</sup>ed as “Good” in the <sup>fi</sup>eld.

Three observations can be made from the two sets of data:

1. There is agreement between the <sup>fi</sup>eld results and the diagnostic tester for majority of scenarios (95.6% agreement in brand $B _ { 1 }$ data and 96.4% agreement in brand $B _ { 2 }$ data).

2. When in agreement, majority of scenarios are classi<sup>fi</sup>ed as “Bad” (97.3% and 98.1% in brands $B _ { 1 }$ and $B _ { 2 } ,$ respectively).

3. When in disagreement, majority of scenarios are classi<sup>fi</sup>ed as “Good” by the diagnostic tester (97.0% and 95.8% in brands $B _ { 1 }$ and $B _ { 2 } ,$ respectively).

## 5.3. Approach

In this work anomalous data is one where the <sup>fi</sup>eld and the tester decisions do not agree. In such cases either one of the two are wrong. As discussed earlier, in the absence of any ground truth about the decisions, it is dif<sup>fi</sup>cult to say whether the <sup>fi</sup>eld decision (F) or the diagnostic tester decision (T) is correct. However, when they agree we have more con<sup>fi</sup>dence on the decision because both the technician's experience and the tester agree on the decisions. Hence, we try to learn the characteristics about the underlying distribution using the agreement scenarios. Later, out of all the disagreement scenarios, to <sup>fi</sup>gure out whether the tester or the <sup>fi</sup>eld decision is incorrect we compare the learnt model (which is assumed to have captured the characteristics of the underlying distribution) with the <sup>fi</sup>eld and the tester decisions (Section 5.3.1). Finally, we also assess the accuracy of the learnt models (C4.5 decision tree and SVM; choice of classi<sup>fi</sup>er is discussed in Section 5.4) in Section 5.3.2.

Illustration of the data used in this study.

<table><tr><td rowspan="2">Surface charge detected (A)</td><td rowspan="2">Temp. above freezing (B)</td><td rowspan="2">Current (C)</td><td rowspan="2">Voltage (D)</td><td colspan="2">Decision</td></tr><tr><td>Tester (T)</td><td>Field (F)</td></tr><tr><td>No</td><td>Yes</td><td>140</td><td>12.9</td><td>Bad</td><td>Good</td></tr><tr><td>Yes</td><td>Yes</td><td>15</td><td>11.8</td><td>Good</td><td>Bad</td></tr><tr><td>No</td><td>No</td><td>0</td><td>11.9</td><td>Bad</td><td>Bad</td></tr><tr><td>Yes</td><td>No</td><td>250</td><td>8.7</td><td>Good</td><td>Bad</td></tr></table>

## 5.3.1. Field error detection and diagnostic tester tuning

Testing the <sup>fi</sup>eld decisions on the disagreement scenarios is equivalent to testing the diagnostic tester decisions because for each disagreement scenario the decision of one is complementary to the other. For each disagreement scenario, the learnt model will agree with either the <sup>fi</sup>eld decision or the diagnostic tester decision. Consider the following four scenarios (Fig. 4):

R<sup>GG</sup>, $R _ { F } ^ { B B } -$ Learnt model agrees with the <sup>fi</sup>eld decision. This implies that for all these scenarios the diagnostic tester decision is incorrect and there is a requirement to change/update the diagnostic algorithm of the tester.

$R _ { F } ^ { G B } -$ Learnt model classi<sup>fi</sup>es these scenarios as “Bad” whereas the <sup>fi</sup>eld decision is “Good.” This implies that for all these scenarios the tester decision is correct whereas the <sup>fi</sup>eld decision is incorrect which will eventually make the customer come back again causing customer dissatisfaction. This scenario is crucial and effort must be made to avoid it completely.

$R _ { F } ^ { B G }$ — Learnt model classi<sup>fi</sup>es these scenarios as “Good” whereas the <sup>fi</sup>eld decision is “Bad.” For all such scenarios the diagnostic tester decisions agree with the learnt model. But this decision was ignored in the <sup>fi</sup>eld. These are the scenarios which provide information on the wrong action decisions by the technicians.

## 5.3.2. Assessing the proposed methodology

In the absence of the ground truth for the decision outcomes, the proposed method can be assessed in the following two ways — 1) How well the classi<sup>fi</sup>er is able to learn the agreement data; and 2) Since the proposed method is used for continuous improvement, the proportion of disagreement scenarios that are sent to the SME for the review, must reduce over time.

The assessment of the learning on the agreement data is observed using the classi<sup>fi</sup>cation accuracy and the stability of the learnt rules. The classi<sup>fi</sup>cation accuracy of the learnt model is presented using a (66:34) data split and 10-fold cross validation on the agreement data. The rules learnt are proprietary and will not be discussed in the paper. However, the reduction in the number of scenarios to be reviewed, by the SME, during subsequent iterations also indicates the stability of the rules. This reduction is discussed in Section 6.4.

## 5.4. Choice of algorithm

For the given problem (Section 5.1) and the nature of the data (Section 5.2), decision trees are an obvious choice for variety of reasons: nominal data, interpretability and rapid classi<sup>fi</sup>cation [25]. Hence we choose C4.5 [24] classi<sup>fi</sup>er as our <sup>fi</sup>rst choice. In addition, we also use SVMs [7,27] for their popularity and immense success in various classi<sup>fi</sup>cation tasks and anomaly detection. The implementations of both of these algorithms in WEKA [29], a data mining software, are used in this work. The following parameter values are used for the two algorithms:

![](/api/attachments/5CV8SZHR/fulltext/images/1c4a0b004d23c47a4983167acddb7b846602dbe153885e21aa771b8a92f0bd94.jpg)

![](/api/attachments/5CV8SZHR/fulltext/images/f7cc34da9c938681f63a2653ca1dd23e5b8f4b85efb20c8cab1f8246771b856b.jpg)

![](/api/attachments/5CV8SZHR/fulltext/images/214110503071fbb85e42630d80d78b57c9c7f47ed348e105d9f329c5d2b61eb5.jpg)  
Fig. 3. Class distribution for the battery claims derived from brands B and $B _ { 2 } .$

• For C4.5, multi-way splits are used for nominal data. Pruning is performed, including the sub-tree raising option, with a con<sup>fi</sup>dence factor of 0.25.

• For SVM, the cost parameter (c) is 1.0, the tolerance of the termination criteria (ε) is 0.001 and radial basis kernel functions (with the Gaussian kernel radius γ=0.2) are used.

Decision trees trained using a greedy algorithm are known to be unstable with respect to the changes in training data — small changes in training data lead to signi<sup>fi</sup>cantly different classi<sup>fi</sup>ers and large changes in accuracy [25]. To overcome this problem we use a boosting approach where the <sup>fi</sup>nal interpretations are made using the combined outputs of C4.5 and SVM classi<sup>fi</sup>ers (Section 6).

## 6. Results and discussion

Let us <sup>fi</sup>rst examine brand $B _ { 1 }$ and the two classi<sup>fi</sup>ers. The confusion matrices (which contains information about the actual and predicted classi<sup>fi</sup>cations done by the classi<sup>fi</sup>er) for C4.5 and SVM are given in Table 2. For both of these, the test set is obtained from the <sup>fi</sup>eld decisions. From Table 2, we note that out of 236 disagreement scenarios, the learnt model agrees with the <sup>fi</sup>eld decision 115 times and with the tester decision 121 times. Let us discuss all the non-zero entries in the confusion matrix separately:

1. 115 scenarios where the learnt model agrees with the <sup>fi</sup>eld decision (“Bad”) and disagrees with the tester decision. All these scenarios need to be analyzed for required changes/updates the diagnostic algorithm of the tester.

2. 114 scenarios (false positives) where the learnt model disagrees with the <sup>fi</sup>eld decision (“Bad”) and agrees with the tester decision. All these could potentially be misdiagnosed scenarios and need further investigation.

3. 7 scenarios (false negatives) where the learnt model disagrees with the <sup>fi</sup>eld decision (“Good”) and agrees with the tester decision. All these scenarios must be dealt with the dealer to avoid repeat visits and customer dissatisfaction.

<table><tr><td colspan="2">Learnt Model Decision</td><td rowspan="2" colspan="2"></td></tr><tr><td>Good</td><td>Bad</td></tr><tr><td> $R_{F}^{GG}$ </td><td> $R_{F}^{GB}$ </td><td>Good</td><td rowspan="2">Field Decision</td></tr><tr><td> $R_{F}^{BG}$ </td><td> $R_{F}^{BB}$ </td><td>Bad</td></tr></table>

Fig. 4. Interpretation of the learnt model and the <sup>fi</sup>eld decision outcomes based on the confusion matrix.

When we look at SVM as the classi<sup>fi</sup>er (Table 2), we discover that there are 78 scenarios where the learnt model disagrees with the <sup>fi</sup>eld decision (“Bad”) and agrees with the tester decision. 73 out of these 78 scenarios are classi<sup>fi</sup>ed as “Good” by the C4.5 algorithm also. For these 73 scenarios (false positives) we have a consensus from the two classi<sup>fi</sup>ers that the <sup>fi</sup>eld decisions are incorrect. This gives us more con<sup>fi</sup>dence about these being misdiagnosed scenarios.

Similarly, 110 out of the 115 scenarios classi<sup>fi</sup>ed as correct <sup>fi</sup>eld decisions by C4.5 are again classi<sup>fi</sup>ed as correct by the SVM (these are included in the 151 scenarios presented in the confusion matrix in Table 2). Hence, for these 110 scenarios we have strengthened con<sup>fi</sup>dence about the incorrect tester decision. These scenarios should be used to investigate changes/updates required in the diagnostic algorithm of the tester.

Both SVM and C4.5 identify the same 7 scenarios (false negatives) where the learnt model disagrees with the <sup>fi</sup>eld decision (“Good”). Again for these scenarios we have more con<sup>fi</sup>dence that these misdiagnoses by the dealer/technician must be avoided in the future to prevent repeat visits and customer dissatisfaction.

For Brand $B _ { 2 }$ and the two classi<sup>fi</sup>ers, the confusion matrices for C4.5 and SVM are given in Table 3. Again, using the same rationale discussed previously we discover the following three types of scenarios:

• 192 scenarios (false positives) where both the classi<sup>fi</sup>ers say that the instance is “Good” against the decision taken in the <sup>fi</sup>eld. All these could potentially be misdiagnosed scenarios and need further investigation.

• 527 scenarios where both the classi<sup>fi</sup>ers agree with the <sup>fi</sup>eld decision being “Bad.” These scenarios should be used to investigate changes/updates required in the diagnostic algorithm of the tester.

• 37 scenarios (false negatives) where both the classi<sup>fi</sup>ers disagree with the <sup>fi</sup>eld decision being “Good.” These misdiagnoses by the dealer/technician must be avoided in the future to prevent repeat visits and customer dissatisfaction.

Confusion matrices from the disagreement data using learnt model (J48/C4.5 and SVM) from the agreement data for brand B .

<table><tr><td>Good</td><td>Bad</td><td></td><td></td></tr><tr><td colspan="4">Learnt model decision (C4.5)</td></tr><tr><td>0</td><td>7</td><td>Good</td><td>Field decision</td></tr><tr><td>144</td><td>115</td><td>Bad</td><td></td></tr><tr><td colspan="4">Learnt model decision (SVM)</td></tr><tr><td>0</td><td>7</td><td>Good</td><td>Field decision</td></tr><tr><td>78</td><td>151</td><td>Bad</td><td></td></tr></table>

Table 3  
Confusion matrices from the disagreement data using learnt model (J48/C4.5 and SVM) from the agreement data for brand $B _ { 2 } .$

<table><tr><td>Good</td><td>Bad</td><td></td><td></td></tr><tr><td colspan="4">Learnt model decision (C4.5)</td></tr><tr><td>0</td><td>37</td><td>Good</td><td>Field decision</td></tr><tr><td>299</td><td>534</td><td>Bad</td><td></td></tr><tr><td colspan="4">Learnt model decision (SVM)</td></tr><tr><td>0</td><td>37</td><td>Good</td><td>Field decision</td></tr><tr><td>199</td><td>634</td><td>Bad</td><td></td></tr></table>

From the two brands' data we have identi<sup>fi</sup>ed the scenarios for <sup>fi</sup>eld errors and diagnostic tester tuning opportunities. These are presented in Table 4.

## 6.1. Learnt classifier assessment

In order to assess the learnt classi<sup>fi</sup>er, the classi<sup>fi</sup>cation accuracy of the learnt model is measured using a (66:34) data split and 10-fold cross validation. The classi<sup>fi</sup>cation accuracy refers to how many scenarios of the testing data are mis-classi<sup>fi</sup>ed based on the model learnt from the training data. In this case, both the training and the testing data are made of the agreement dataset (i.e. agreement between the diagnostic tester and the human expert) which we assume to be of high quality with very low noise. The accuracy numbers, as given in (Table 5), show that both the classi<sup>fi</sup>ers can learn the agreement data very well.

## 6.2. Field error identification from the results

For the recommendations regarding potential <sup>fi</sup>eld errors, all the scenarios for both the models are veri<sup>fi</sup>ed against the <sup>fi</sup>eld decisions. The scenarios where the learnt model decision is “Good” against the <sup>fi</sup>eld decision (73 scenarios for $B _ { 1 }$ and 192 scenarios for $B _ { 2 } )$ are identi<sup>fi</sup>ed as potentially misdiagnosed scenarios. However, these may also include scenarios where the human expert's decision was based on non-quanti<sup>fi</sup>able factors, such as, physical damage, corrosion and other quanti<sup>fi</sup>able factors the testers' algorithm cannot judge. The subject matter expert (SME) will decide how to handle such scenarios. After an SME review of such scenarios (Section 6.4), either the dealer training needs or additional features, like charging time, for the tester algorithm can be identi<sup>fi</sup>ed.

In addition to the <sup>fi</sup>eld error scenarios, there are other scenarios where the tester and the classi<sup>fi</sup>ers <sup>fi</sup>nd the component to be “Bad” but the dealer has passed them off as “Good” (false-negatives). The results show that there are very few such scenarios (7 scenarios for $B _ { 1 }$ and 37 scenarios for $B _ { 2 } )$ . These false-negatives, as observed, resulted in repeat visits causing customer dissatisfaction. Considering the customer perspective these need to be dealt with strictly through proper training and must be avoided in the future.

Number of scenarios identi<sup>fi</sup>ed which can be focused upon for <sup>fi</sup>eld error prevention and diagnostic tester tuning.

<table><tr><td>Scenario</td><td>Brand  $B_1$ </td><td>Brand  $B_2$ </td></tr><tr><td>Field errors (both classifiers? decision is “Good” against the field decision)</td><td>73</td><td>192</td></tr><tr><td>Field errors (both classifiers? decision is “Bad” against the field decision)</td><td>7</td><td>37</td></tr><tr><td>Diagnostic tester tuning opportunities (both classifiers? agree with the field decision being “Bad”)</td><td>110</td><td>527</td></tr></table>

Table 5  
Percentage accuracy of the two classi<sup>fi</sup>ers on the two datasets based on data split

<table><tr><td rowspan="2">Brand</td><td colspan="2">Classifier C4.5</td><td colspan="2">Classifier SVM</td></tr><tr><td>Data split</td><td>10-fold</td><td>Data split</td><td>10-fold</td></tr><tr><td> $B_1$ </td><td>99.1%</td><td>99.0%</td><td>98.6%</td><td>98.6%</td></tr><tr><td> $B_2$ </td><td>98.7%</td><td>98.8%</td><td>98.4%</td><td>98.5%</td></tr></table>

## 6.3. Identification of tester improvement areas

For the identi<sup>fi</sup>cation of diagnostic tester tuning opportunities, 110 scenarios in brand $B _ { 1 }$ and 527 scenarios in brand $B _ { 2 }$ are chosen i.e. both the learnt classi<sup>fi</sup>ers match with the <sup>fi</sup>eld decision in classifying the component as “Bad” though the tester decision classi<sup>fi</sup>ed the component as “Good”. These scenarios require immediate action to tune the tester in order to reduce the false negatives.

## 6.4. HIL-DSS enhancement methodology

Isolation of the scenarios in Sections 6.2 and 6.3 only identi<sup>fi</sup>es potential areas of improvement. As illustrated in Fig. 2 of Section 4, a subject matter expert needs to look at these few isolated scenarios and decide (step 7 in the proposed methodology) what action is required for either the DSS or the human expert knowledge improvement.

When the scenarios were presented to the SME, based on only the available parameters, approximately 51% of the presented scenarios were identi<sup>fi</sup>ed as inappropriate tester decisions and another 32% of the scenarios were identi<sup>fi</sup>ed as inappropriate <sup>fi</sup>eld decisions. The rest 17% of the scenarios needed a deeper root-cause study by the SME and discussions with <sup>fi</sup>eld technicians to understand the reason for disagreement (for example qualitative factors).

• In terms of the tester improvements, the decision support algorithm in the tester had problems causing inappropriate decisions. It also had scenarios where the threshold ranges were found to be wider than the normal level for the failure decisions (Section 2) and required tightening. In addition, the root cause investigation done by the SME resulted in the recommendation for the inclusion of a “estimated charging time” parameter in the tester to enhance the decision support system. The charging time was found to be the most frequent cause for the <sup>fi</sup>eld decision taken against the tester among these 17% scenarios.

• In terms of the <sup>fi</sup>eld improvements, a training session was arranged to avoid such wrong decisions in the future because, based on the available factors, the batteries were perfectly healthy and either needed no replacement or needed replacement instead of recharging.

At the time of writing this paper, the implementation of the SME recommendations is still under way. Once these improvements are incorporated in the DSS and the human expert knowledge, we expect in the new set of data from battery warranty the number of disagreement scenarios to be lower. We also expect that the new set of data will have disagreement scenarios primarily due to qualitative factors other than the available tester parameters. For the continuous improvement opportunity, if the tester provides the capability of integrating SME based conditions with the tester algorithm, one can use the methodology after collecting a critical mass of data points every few months and keep upgrading or updating the learnt model.

## 7. Conclusions and future work

Decision support systems with human-in-the-loop (HIL-DSS) are quite common. There are two essential components of such systems — the algorithmic component and the human expert. The algorithmic component is usually well-de<sup>fi</sup>ned and well-designed based on the requirements of the DSS. The human involvement enables the decisions to be based on experience and also factors which are non-quanti<sup>fi</sup>able that cannot be easily implemented algorithmically. The algorithmic component is limited/incomplete in the absence of these human-based factors. Human involvement however, also brings in fuzziness into the system due to (un)intentional errors from humans. The HIL-DSS that we consider in this work is complex on both the fronts — the algorithm behind the algorithmic component is not known (proprietary reasons) and the human expert also introduces uncertainty into the system. The absence of the DSS algorithm makes the understanding of the DSS outcomes dif<sup>fi</sup>cult.

We present a novel approach based on pattern-classi<sup>fi</sup>cation to — 1) continuously learn from collective decision making systems; 2) enhance the limited/incomplete DSS; 3) add to the knowledge of human expertise; and 4) minimize the human involvement in the review process of the overall system. This necessitates a completely data-driven bottom-up approach for this purpose. Based on data availability, data mining techniques can be used to learn the DSS algorithm at a high level which also has the features of the human decisions inculcated in the learning. Following are the salient features of the proposed methodology:

Agreement/disagreement data — With the availability of data on both the DSS decisions and the human decisions a simple Set-Intersection based on the decisions can divide the data into agreement and disagreement data.

Classifier selection — We learn the comprehensive model using two different pattern classi<sup>fi</sup>cation techniques namely, Decision trees and Support Vector Machines. These were chosen based on the nature of our data we used for our analysis. We assess the learnt model by studying its classi<sup>fi</sup>cation accuracy both by data-splitting of the agreement data and also using cross-validation.

Testing the learnt model — The model learnt using the agreement data and is applied to the disagreement data to determine those scenarios that either agree with the human decisions or the DSS decisions. They are complementary because you test on one of the either two decisions.

Identification of field errors and DSS improvement areas — The disagreement between the learnt model and the <sup>fi</sup>eld decisions indicates potentially misdiagnosed scenarios which need further investigation. The disagreement between the learnt model and the tester decisions <sup>fl</sup>ags scenarios that need to be analyzed for required changes/updates to the diagnostic algorithm of the tester. Boosted classifier outputs — The disagreement between the learnt model and the human/DSS decisions that have been isolated using the confusion matrices for each of the classi<sup>fi</sup>ers are fused using Set-Intersection to obtain boosted classi<sup>fi</sup>er outputs with higher con<sup>fi</sup>dence.

Subject matter expert review and feedback — These boosted classi<sup>fi</sup>er outputs are further reviewed by the subject matter experts and recommendations are made on the enhancements. These enhancements, in the context of the case study presented, can be addition of new features to the diagnostic tester (for example charging/repair time which in<sup>fl</sup>uences customer satisfaction) or revision of the service procedure to be followed by the technician. Feedback from the subject matter expert is expected to continuously reduce the number of disagreement scenarios and hence will make the system robust.

Incorporation of non-quantifiable factors — Some of the nonquanti<sup>fi</sup>able factors can be quanti<sup>fi</sup>ed by adding features to the diagnostic tester. For example, inclusion of charging time estimate helps explain the decisions made in the <sup>fi</sup>eld, based on customer satisfaction.

To summarize, by using the past data and the pattern classi<sup>fi</sup>cation approach we have identi<sup>fi</sup>ed potential areas of improvement in the

DSS and the human expert knowledge. In addition, we have also signi<sup>fi</sup>cantly reduced the number of scenarios to be reviewed by the subject matter expert, thereby making the HIL-DSS more ef<sup>fi</sup>cient. For the case study presented, we have managed to limit the number of scenarios to be reviewed by the subject matter expert from 5417 to $1 9 0 \ : ( = 7 3 + 1 1 0 + 7 ;$ 96.49%reduction) in brand $B _ { 1 }$ dataset and from 24,312 to 756 $( = 1 9 2 + 5 2 7 + 3 7$ ; 96.89% reduction) in brand $B _ { 2 }$ dataset (Table 4).

However, there are certain limitations in our approach — 1) There is an inherent assumption that the data is of good quality and has not been manipulated or skewed. It needs to be validated in the presence of noise; 2) The approach does not work for data with missing values. These scenarios are simply ignored; 3) There is some subjectivity involved due to the SME. This cannot be removed; and 4) The approach only handles binary decisions (as against nominal decisions). We plan to address these limitations in future.

## Acknowledgments

The authors would like to thank Dr. Pulak Bandyopadhyay, Dr. Ravikumar Karumanchi (General Motors R&D, India) and the journal reviewers for their important contributions to improve the prior drafts of the paper.

## References

[1] G.J. Avlonitis, P. Papastathopoulou, Product and Services Management, Sage Publications. 2006

[2] P. Baltusis, On Board Vehicle Diagnostics, 20048 SAE 2004-21-0009

[3] R. Battiti, A.M. Colla, Democracy in neural nets: voting schemes for classi<sup>fi</sup>cation, Neural Networks 7 (1994) 691–707.

[4] E. Bauer, R. Kohavi, An empirical comparison of voting classi<sup>fi</sup>cation algorithms: bagging, boosting, and variants, Machine Learning 36 (1999) 105–139.

[5] C.M. Bishop, Novelty detection and neural network validation, Vision, Image and Signal Processing, IEEE Proceedings 141 (1994) 217–222

[6] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006.

[7] B.E. Boser, I.M. Guyon, V.N. Vapnik, A training algorithm for optimal margin classi<sup>fi</sup>ers, Proceedings of the 5th Annual ACM Workshop on Computational Learning Theory, ACM Press, 1992, pp. 144–152.

[8] Cadex Electronics Inc., Battery Charger and Battery Analyzer Experts, 20098 http:// www.cadex.com.

[9] L.F. Cranor, A framework for reasoning about the human in the loop, UPSEC'08: Proceedings of the 1st Conference on Usability, Psychology, and Security, USENIX Association, Berkeley, CA, USA, 2008, pp. 1–15.

[10] H. Drucker, C. Cortes, L.D. Jackel, Y. LeCun, V. Vapnik, Boosting and other ensemble methods, Neural Computation 6 (1994) 1289–1301.

[11] R. Fujimaki, Anomaly detection support vector machine and its application to fault diagnosis, ICDM '08: Proceedings of the 2008 Eighth IEEE International Conference on Data Mining, IEEE Computer Society, Washington, DC, USA, 2008, pp. 797–802.

[12] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison-Wesley Professional, 1989.

[13] J. Han, M. Kamber, Data Mining: Concepts and Techniques, 2 editionMorgan Kaufmann Publishers Inc., San Francisco, CA, USA, 2006.

[14] V.R. Khare, Automatic Problem Decomposition using Co-evolution and Modular Neural Networks, Ph.D. thesis, The University of Birmingham, Birmingham, UK, 2007.

[15] E. Kim, W. Kim, Y. Lee, Combination of multiple classi<sup>fi</sup>ers for the customer's purchase behavior prediction, Decision Support Systems 34 (2003) 167–175.

[16] R. Kohavi, F. Provost, Glossary of terms, Machine Learning 30 (1998) 271–274.

[17] A. Krogh, J. Vedelsby, Neural network ensembles, cross validation, and active learning, Advances in Neural Information Processing Systems, MIT Press, 1995, pp. 231–238.

[18] Y. Li, M.J. Pont, N.B. Jones, Improving the performance of radial basis function classi<sup>fi</sup>ers in condition monitoring and fault diagnosis applications where 'unknown' faults may occur, Pattern Recognition Letters 23 (2002) 569–577

[19] Midtronics Inc., Midtronics Battery Testers/Analyzers, 20098 http://www.midtronics com

[20] D.N.P. Murthy, I. Djamaludin, New product warranty: a literature review, International Journal of Production Economics 79 (2002) 231–260

[21] D.N.P. Murthy, O. Solem, T. Roren, Product warranty logistics: issues and challenges European Journal of Operational Research 156 (2004) 110–126

[22] M.P. Perrone, Improving regression estimation: averaging methods for variance reduction with extensions to general convex measure optimization. Ph.D. thesis Brown University Providence RI USA 1993

[23] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Quorum Books, Westport, CN, 2002

[24] R.J. Quinlan, C4.5: Programs for Machine Learning (Morgan Kaufmann Series in Machine Learning), Morgan Kaufmann, 1993.

[25] D.G.S. Richard, O. Duda, Peter E. Hart, Pattern Classi<sup>fi</sup>cation, 2 editionJohn Wiley & Sons, 2001.

[26] R.E. Schapire, The strength of weak learnability, Machine Learning 5 (1990) 197–227.

[27] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag New York Inc., New York, NY, USA, 1995.

[28] C.R. Wanke, N.J. Taber, S.L. Miller, C.G. Ball, L. Fellman, Human-in-the-loop evaluation of a multi-strategy traf<sup>fi</sup>c management decision support capability, in: Proceedings of the 5th Eurocontrol/FAA ATM R&D Seminar, pp. 1–11.

[29] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2 editionMorgan Kaufmann, 2005.

[30] M. Wozniak, Concept of the knowledge quality management for rule-based decision system, Intelligent Information Systems, Advances in Soft Computing, Springer, 2003, pp. 575–579.

[31] M. Wozniak, Proposition of boosting algorithm for probabilistic decision support system, International Conference on Computational Science, Lecture Notes in Computer Science, 3036, Springer, 2004, pp. 675–678.

[32] Y. Zhang, G. Gantt, M. Rychlinski, R. Edwards, J. Correia, C. Wolf, Vehicle design validation via remote vehicle diagnosis: a feasibility study on battery management system, in: PHM 2008: International Conference on Prognostics and Health Management, pp. 1–6.

![](/api/attachments/5CV8SZHR/fulltext/images/de32c86fe566df84555c4f3560e57f259d30e838520d0476442026982690d01a.jpg)  
Halasya Siva Subramania is a senior researcher in the Diagnosis and Prognosis Group at General Motor's India Science Laboratory. He received Bachelor of Science (B.Sc) in Physics degree from University of Madras in 1998 and Masters of Science (M.Sc) in Physics from Indian Institute of Technology, Madras in 2000. He received Ph.D in Physics from University of Houston, Houston, TX in 2005 and specialized in Experimental High Energy Physics. His current research interests include data analysis and visualization, experimenting accelerated aging techniques to develop prognostic models for critical components in the car, data-driven fault modeling in the automotive domain, and knowledge management.

![](/api/attachments/5CV8SZHR/fulltext/images/e17b5b22b21bf7ea453f12a0c9a40767841460608cdaa0a859a64e38c90f47d1.jpg)

Vineet R. Khare is a senior researcher in the Diagnosis and Prognosis Group at the General Motor's India Science Laboratory. He received his Bachelor's degree in Mechanical Engineering from the IIT Kanpur, India in 2001 and Master's and Ph.D degrees in Computer Science from the University of Birmingham, UK in 2002 and 2006, respectively. His research interests include statistical machine learning, text mining, soft computing and multi-objective evolutionary algorithms.
