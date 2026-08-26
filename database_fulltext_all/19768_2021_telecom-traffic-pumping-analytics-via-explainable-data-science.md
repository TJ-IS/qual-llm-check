---
otero_id: 19768
otero_key: "5CXBABZG"
title: "Telecom traffic pumping analytics via explainable data science"
authors: "María Elisa Irarrázaval; Sebastián Maldonado; Juan Pérez; Carla Vairetti"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113559"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Telecom traffic pumping analytics via explainable data science

María Elisa Irarrazaval´ <sup>a</sup>, Sebastian ´ Maldonado <sup>b,c</sup>, Juan P´erez <sup>a,\*</sup>, Carla Vairetti <sup>a,c</sup>

<sup>a</sup> Universidad de los Andes, Facultad de Ingeniería y Ciencias Aplicadas, Chile

<sup>b</sup> Department of Management Control and Information Systems, School of Economics and Business, University of Chile, Santiago, Chile

<sup>c</sup> Instituto Sistemas Complejos de Ingenier a (ISCI), Chile

## A R T I C L E I N F O

Keywords: Fraud prediction Unsupervised learning Interpretable machine learning EXplainable AI (XAI) Telecommunications

## A B S T R A C T

Traffic pumping is a type of fraud committed in several countries, in which small telephone operators inflate the number of incoming calls to their networks, profiting from a higher access charge in relation to the network operator associated with the origin of the call. The identification of traffic pumping is complex due to the lack of labels for performing supervised learning, and the scarce literature on the topic. We propose a decision support system for fraud detection via clustering and decision trees. After data collection and feature engineering, we group the potential fraud cases into various clusters via an unsupervised learning approach. Then, we con structed a decision tree by using the cluster memberships as labels, evolving into the rules of a given variable and a certain label required for filing lawsuits against the suspicious cases. Telecommunication experts validate these rules to seek a legal resource against alleged perpetrators. We present the results of a case study from a Chilean telecommunication provider. All the lawsuits taken by the legal department were granted, confirming our success in dramatically reducing current and future fraud losses for the company

## 1. Introduction

During the last decades, fraud strategies have been in constant evolution in the telecommunication industry, ranging from simple ap proaches to make free calls in the early days to complex schemes based on multiple stakeholders, networks, and technologies [1]. In this sense, several studies have been devoted in analyzing, classifying, and pro posing recommendations in relation to the different types of frauds; see e.g. [1–4].

The timely identification of fraudulent behaviors is extremely important in this industry. According to the 2015 Global Fraud Loss Survey made to service providers in telecommunications, the monetary loss that fraud caused that year was estimated to 38.1 billion US dollars, representing 1.69% of the global revenue [1]. The monetary loss, however, is not the only problem caused by successful fraud attempts. Fraudulent cases may severely damage the reputation of a company, especially if they cause service disruption. Furthermore, it negatively affects customer satisfaction. For example, in 2016, the US Federal Trade Commission (FTC) reported 400,000 complaints per month on average [1]. Due to these reasons, major service providers mobilize considerable resources in technologies for preventing fraud. In this sense, machine learning and Big Data systems play a crucial role for data processing, online monitoring, and decision support [4].

Among the different types of telephony fraud, traffic pumping is considered of utmost importance since it has generated important losses to large network operators in different countries. This fraud involves small network operators artificially boosting their incoming calls in order to charge a fraudulent access fee to the telephone operator from which the calls originated $[ 1 , 3 ]$

Traffic pumping is perpetrated in countries with large access charges, i.e., the interconnection service tariffs paid by all mobile network pro viders each time they end a call to another company’s network. Access charges are defined by regulatory agencies based on the size, demand, and technology of the network operators [5]. Although the purpose of access charges is to avoid monopolistic competition, it creates perverse incentives for a small operator to generate artificial calls to its network from a large competitor [5].

The recent literature in machine learning has provided new strate gies for making machine learning models explainable. This popular and recent trend is known as interpretable machine learning or eXplainable Artificial Intelligence (XAI) [6,7]. This is a key feature in our proposal because our aim is to initiate a legal process against the fraudulent op erators that commit traffic pumping. For this purpose, suspicious cases must be properly justified to sustain a claim to be filed.

In this paper, we propose a five-step decision support system (DSS) for explainable fraud detection via unsupervised learning and decision trees. After data collection using call detail records (CDRs, step 1), the second step involves the creation of network variables that allow the correct identification of traffic pumping.

The third step consists in applying several unsupervised learning methods in order to find the most suitable one for fraud detection. Notice that labels (known fraudulent/non-fraudulent cases) are not available in fraud detection systems implemented for the first time, and therefore, standard classifiers cannot be used.

Unsupervised learning methods do not usually provide ways to interpret the outcome of the model, and are considered as ‘black-box approaches. This is an important limitation in business analytics since the insights gained into the application may be narrow [7]. Inspired by the XAI studies by Verbeke et al. [8] and Martens et al. [9] for churn prediction and credit scoring, respectively, the fourth step consists in the construction of a decision tree based on the labels generated by clus tering approach, in order to generate a set of rules for decision-making. Notice that the Verbeke et al. [8] and Martens et al. [9] approaches were designed in the context of supervised learning, using artificial neural networks.

The final step consists in the validation of the interpretable rules by a team of experts. We applied the framework to a traffic pumping study developed for a major Chilean telephone operator to provide rules that justify claims held against the suspicious fraudsters. The main contri butions achieved in this study are the following ones:

• There is an important gap in the fraud detection literature since this is the first study that proposes a machine learning approach for dealing with traffic pumping exclusively, to the best of our knowl edge. There are a few benchmark studies that mention this issue; see e.g. [1,3,5], including also general-purpose fraud detection mecha nisms that indicate traffic pumping as a potential application [10].

• Despite the fact that there are some methodologies that derive rules from machine learning methods; see e.g. [8], this is the first one tailored for fraud prediction in telecommunications.

• This is one of the first studies in fraud prediction in the context of XAI or interpretable machine learning, and the first in the telecommu nications domain with unsupervised learning, to the best of our knowledge. There are some successful studies in other domains and/ or based on supervised learning, such as the fuzzy rule-based detection system proposed in financial statement fraud detection [11].

• Most fraud detection papers are not able to report a successful business case, making a retrospective statistical analysis of the per formance achieved by their proposal. In this case, we discuss the success of both the proposed method after its implementation and the results of the legal process against the fraudulent cases. All of the lawsuits filed by the legal team were confirmed to be fraudulent.

This paper is structured as follows: Section 2 provides a review of relevant approaches for fraud analytics, also discussing traffic pumping fraud. The proposed two-step framework for interpretable fraud pre diction is presented in Section 3, along with the machine learning methods implemented in the case study. Experimental results using a traffic pumping fraud dataset from an important Chilean company are provided in Section 4. Finally, a summary of this study is given in Sec tion 5, which includes the main conclusions, managerial insights into the application, and future developments.

## 2. Prior work on fraud detection and interpretable machine learning

There are several types of fraud in telecommunications. According to Becker et al. [3], the following examples of telephony fraud are frequently committed:

• Subscription fraud: A customer subscribes to a service without any intention to pay for it.

• Masquerading and identity theft: For example a fraudster makes calls using a stolen credit card number.

• Fraud based on technological loopholes: Vulnerabilities of the sys tems, such as weak passwords, are exploited by fraudsters in order to enter in the systems.

• Intrusion fraud: A legitimate account becomes compromised by an intruder.

• Fraud based on new technology: For example, the rise of the Voice over Internet Protocol (VoIP) technology allowed cheap interna tional calls. Fraudsters used this technology to resell technology services illegally at a higher price.

• Fraud based on new regulations: In order to promote fairness, reg ulators design regulatory schemes that can be exploited for fraud. This is precisely the cause that drives traffic pumping fraud, dis cussed in the next section.

This section is structured as follows. Section 2.1 explains traffic pumping fraud; an important type of it that has not previously been reported in the machine learning literature. Next, Section 2.2 motivates the importance of fraud analytics in telecommunications, discussing the main strategies for dealing with this task. Finally, studies in explainable artificial intelligence are presented in Section 2.3, indicating their relevance to fraud detection and our proposal.

## 2.1. Traffic pumping fraud

A few years ago, voice communication was the most important ser vice provided by telecommunications network operators, because most of the profit came from this business line. Nowadays, the most relevant service for consumers and firms is the internet, both mobile and fixed. Despite this, in many countries, telephony is relevant and is part of the bundles offered by telecommunications firms. Operators still offer mo bile voice services for individuals and fixed telephone lines for com panies. NRAs (National Regulatory Agencies) are still concerned about regulatory issues related to the voice service, such as the definition of access charges, also known as termination rates [5].

When a consumer makes a call in the network of an operator A (OA), and the receiver is in the network of an operator B (OB), the termination of the call requires and uses the OB’s network. The access charge or termination rate (TR) is the cost associated with this part (termination) of the call. See Laffont and Tirole [5] for a broader analysis and defi nition of issues related to TR.

The only way for OA to reach consumers of OB is using OB’s network. Therefore, OB has a monopoly over its consumers when receiving calls from other operators. This monopolistic situation is known as the mo nopoly of the terminal network [5], in this context, NRAs are required to define the termination rates, in specialized and often arduous regulatory processes.

The NRA calculates the TR based on the operator’s size, technology and demand forecasts. The technology deployed by network operators differs from operator to operator: while some of them use mobile, others are keen on fixed technology. For each of these technologies, there are also differences in demand levels and coverage. This leads to different cost functions, economies of scale, scope, and density for operators. Some NRAs recognize these differences, which implies that the TR dif fers among operators.

Operators with less market share and coverage (usually fixed net works) have higher TR than those with higher coverage and market share (usually mobile service providers). This creates perverse in centives for an operator with a high TR to generate calls to its network artificially, originating them from the competitors’ network. This leads to fraudulent incomes because of the difference between the ones due to access charges, and the cost of generating those calls. This is known as traffic pumping [1,3], and it is only possible because nowadays most telephony subscriptions include unlimited call minutes.

Formally, let TR be the TR of operator B in dollars per minute. If OB pumps P minutes in a month, then OA will have to pay $T R _ { B } P \ U S \mathrm { D } . \mathrm { I f } S _ { A }$ is the monthly subscription price to have unlimited minutes in OA, then it will be convenient for OB to perform traffic pumping if OB pumps $\begin{array} { r } { P > \frac { S _ { A } } { T R _ { B } } . } \end{array}$

Fig. 1 illustrates the concept of traffic pumping. This figure shows four main agents: The Mobile Network Operator (MNO), the Fixed Network Operator (FNO), a third-party company, and the fraudsters. On the one hand, the MNO started offering plans (bundles) with unlimited voice minutes. On the other, the FNO has a high access charge due to its coverage and technology, and, assisted by a third-party company, they contracted several plans (sim cards) with unlimited voice minutes per month.

The sim cards, managed by automated systems, originated several calls to numbers from the FNO. Hence, this high voice traffic from the MNO to the FNO generates elevated total payments for access charges from the MNO to the FNO. The numbers within the FNO were allegedly providing call center or miscellaneous services (horoscope, history telling, specialized chats, among many others). Nevertheless, in prac tice, the services did not exist and were only ‘empty’ communications or calls without any voice transmissions.

The final stage of the traffic pumping fraud occurs when the total traffic pumped from the MNO to the FNO is more than the total pay ment, due to the plans contracted to the MNO. In this case, the FNO profits from an activity not allowed by the local legislation.

Let us consider the following question: can this abnormal behavior be modeled by the MNO, identifying fraudulent calls? The answer is yes, and it can be done automatically via machine learning. We propose a general methodology for interpretable clustering based on CDR data, which can be useful for knowledge discovery in telecommunications. We applied this methodology to a traffic pumping case faced by a Chilean mobile operator that asked us for help. The model and the results of thi case study are reported in the following sections.

## 2.2. Fraud analytics in telecommunications

In the Big Data era, identifying fraudulent activities in telecommu nications has become a sort of finding a needle in a haystack. This task usually involves analyzing a large amount of data in the form of CDRs, which is an intractable task for humans and even for traditional statis tical techniques [2]. The recent advances in machine learning and Big Data, however, have revolutionized the fraud analytics community, providing efficient solutions for dealing with one of the most complex problems faced by artificial intelligence practitioners [2,4].

Fraud analytics have been widely used in telecommunications [2,4].

These techniques can be classified into supervised or unsupervised learning depending whether the labels that identify fraud cases are available or not [12]. Regarding supervised methods, some studies are devoted to casting the problem into a binary classification task. For example, a comparative study of various classification methods was presented in [13], in which convolutional neural networks (CNNs) outperformed traditional machine learning techniques such as support vector machine, random forest, or gradient boosting.

Fraud detection in telecommunication appears as a complex chal lenge because it implies dealing with Big Data. On the one hand, fraud detection is a class-imbalance problem, given that only a small fraction of the calls are fraudulent in relation to the total call traffic [14]. On the other, it is an exceedingly dynamic issue since fraudsters adapt their strategies once others’ fraudulent behavior is detected [12].

Another important issue in fraud analytics is the lack of labels to guide the learning process [2]. Labels are often unavailable or are inaccurate because of the difficulty of validating suspicious cases. When this situation occurs, unsupervised learning is a suitable strategy fo fraud detection. This approach is aimed at grouping the observations in homogeneous clusters, having also the potential of identifying outliers $[ 2 , 1 2 ]$

Since labels are seldom available for fraud analytics in telecommu nications, a plethora of different unsupervised approaches have been discussed in the literature. An important topic is graph-based anomaly detection. A thorough revision of the existing techniques is presented in [4]. In telecommunications, the CDR data provides a suitable source of information for constructing voice call graphs, allowing the develop ment of fraud detection algorithms. Another approach is constructing consumer profiles based on their activities, and clustering them using unsupervised methods. Some techniques used for this task are selforganizing maps (SOMs) [15] or Latent Dirichlet Allocation (LDA) $[ 1 4 , 1 6 ]$

Text analytics have also been useful in fraud detection. For example, a mobile VoIP application is developed in [17], which aims at under standing the content of a call via natural language processing (NLP) in a supervised manner. Text analytics for fraud detection have also been considered in other domains, such as automobile insurance fraud [18]. In this study, LDA is used to extract textual features from the de scriptions of the accidents provided in the claims, while artificial neural networks (ANNs) are then used for fraud classification.

## 2.3. Explainable artificial intelligence for business analytic

Interpretable machine learning is a hot topic for researchers and practitioners given the need for transparency and trust in AI [19]. Despite the revolutionary character of the current AI systems, their lack of explainability hinders their usage because of the impossibility to verify the decisions made by these so-called ‘black box’ models [19–21]. This is particularly true in business analytics applications, in which interpretability is often a constraint due to regulatory issues [8,9].

![](/api/attachments/5CXBABZG/fulltext/images/e81f094fd9d506df0aab486ead187f73f2933eddaa21739918f7adf4d598350f.jpg)  
Fig. 1. Illustrative example of traffic pumping: Fraudsters generate traffic from large MNOs to small FNOs

Interpretable methods can be categorized based on different criteria [7]. Explainability can be achieved by limiting the complexity of the model. For example, a decision tree can be pruned to reduce the number of rules that lead to the outcomes, or complex models such as ANNs can be approximated by interpretable methods as for example decision trees [8,9]. These approaches are known as intrinsic interpretable methods [7]. Alternatively, explainability can be conferred by using a post-hoc method after training a black-box model [7].

One example of a post-hoc method is the SHAP (SHapley Additive exPlanations) approach and its variants, such as TreeSHAP [22] or KernelSHAP [6]. The reasoning behind this approach is to explain the model performance as a series of ‘payouts’, in which each attribute value is a player in a game that contributes to the prediction. This technique computes the Shapley values, a widely used measure from coalitional game theory, to distribute the payouts among the attributes [6]. Although the computation of all Shapley values coalitions can be computationally rather expensive [7], TreeSHAP provides a particularly efficient algorithm for an approximate solution [22]. The outputs of this type of models are usually graphs that illustrate the individual feature importance and the feature dependencies [7].

A second classification for interpretable machine learning corre sponds to the model’s capacity to interpret it entirely at once (global model interpretability), or rather explain individual predictions, which can be aggregated or grouped in order to derive patterns for particular segments (local model interpretability) [7].

Intrinsic interpretable methods designed for global model inter pretability have been used in business analytics tasks. Verbeke et al. [8], for example, proposed a two-step strategy for churn prediction. An ANN classifier is first trained and then decision trees are used to derive rules using the output of the ANN model as labels. A similar approach was proposed by Martens et al. [9] for credit scoring, deriving rules from a support vector machine classifier. In fraud analytics, the only existing rule-based decision support system was proposed in [11] for financial statement fraud prediction, to the best of our knowledge.

There are several explainable approaches used in business analytics that go beyond rule-based strategies and feature selection. For example, Martens and Provost [23] developed an instance-level explanation framework for text analytics, in which a minimal set of terms or concepts is identified for characterizing a document. Another approach is the use of process mining in combination with language models and NLP to provide interpretable prediction for business processes [24].

The vast majority of the interpretable machine learning methods reported in the literature are devoted to supervised learning [7], in contrast to our proposal. There are a few unsupervised XAI techniques, including InfoSSM, an extension of the Gaussian process state-space model (GPSSM) that uses mutual information to learn interpretable dynamics patterns from time series data [25]. No XAI approach has been considered in unsupervised tasks for business analytics, to the best of our knowledge.

## 3. Proposed approach for traffic pumping fraud analytics

In this section, we propose a five-step DSS for traffic pumping fraud prediction. The proposal is tailored to our case study for a major Chilean telecommunication company in the next section.

The goal of our proposal is to derive a set of rules from graph-based features, allowing network operators to file legal procedures against fraudsters. The ability of proving fraudulent behavior is decisive for the success of the claim in this particular task.

Our study is inspired in the XAI approaches by Verbeke et al. [8] and by Martens et al. [9] for churn prediction and credit scoring, respec tively. However, our proposal is different since the labels are not available. For this reason, we create them using clustering algorithms. Our proposal contributes to the state of the art of XAI by presenting a rule-based strategy for unsupervised black-box modeling, being also the first machine learning model tailored for traffic pumping prediction.

The decision tree is key for casting the output of the clustering model into a set of interpretable rules. Interpretability in this case is not only relevant in a managerial context, but it is a legal constraint since the goal is to bring fraudsters to justice. In traffic pumping, it is a legal require ment to be able to clearly explain the reasons for suspicion in order to file lawsuits against the perpetrators.

The proposed DSS is summarized in Fig. 2. This DSS is formalized following the guidelines of different DSS proposed in business analytics; see e.g. [18,26–28]. The first two steps, data preparation and feature engineering, are discussed in Section 3.1. Next, clustering methods are used to identify homogeneous segments of users that follow different patterns, such as regular customers, companies, call centers, and fraudulent behaviors. We propose using a variety of partitioning and density-based methods for clustering, selecting the one with the best performance. The unsupervised learning methods and the performance metrics are discussed in Section 3.2.

Step 4 is devoted to making the model interpretable by fitting a decision tree to the output of the chosen clustering model. By carrying this out, the clusters can be explained as a series of rules, which is a requirement for an eventual legal process against the suspicious fraud ulent cases. Finally, the last step consists in labeling each resulting cluster as either fraudulent or non-fraudulent, based on the rules generated by the trees. For this step, a team of experts needs to be conformed in order to translate their business knowledge into actionable clustering. These two steps are discussed in Section 3.3.

## 3.1. Steps 1 and 2: data preparation and feature engineering

The first step consists in data collection and preparation. We propose considering CDR data with the specifics of the call (starting time/date, duration, and addresses). Additionally, the International Mobile Equipment Identity (IMEI) data provides valuable information for dis tinguishing calls made from different numbers, but using the same phone. Other important sources of information that can help to detect traffic pumping are the International Mobile Subscriber Identity -IMSI-, and the specifics of the cell site related to both OA and OB.

We suggest constructing a dataset in which each row represents the link between two phone numbers from different operators OA (ANUM) and OB (BNUM). In order to reduce complexities of problems, we sug gest filtering out those consumers that did not carry out at least one long call in a given month. These users exhibit an evident non-fraudulent behavior, and their removal alleviates the issue of dealing with Big Data.

The second step corresponds to the creation of variables that can be useful for detecting traffic pumping. Three set of variables are able to be designed based on the literature of traffic pumping [29,30]: (1) inde gree/outdegree variables that can distinguish regular users from com panies, call centers, and fraudulent behaviors, (2) variables that reflect different monthly patterns in terms of the total minutes called, and (3) variables that may indicate a systematic behavior during the day.

The first set of variables corresponds to centrality features from graph theory. We expect to distinguish between non-fraudulent patterns such as contact centers or regular consumers, carried out by the indegree and/or outdegree of the vertex. Centrality variables have been used successfully in several fraud prediction studies [4]. In the same direc tion, the IMEI information allows the design of additional centrality features that can reflect fraudulent behavior.

The second set of variables aims at identifying ‘heavy users’ in terms of the amount of time spoken in a given month. Also interesting are the standard deviation (sd) of different indicators that may reflect system atic monthly patterns. For example, a small sd for the duration of the calls may be a sign of an automated call system for traffic pumping.

The final set of variables aims at discriminating among daily patterns. The literature suggests that non-fraudulent behavior has recognizable peak hours, such as lunchtime and after-office hours (see e. g. [29,30]). Fig. 3 illustrates a standard calling behavior suggested in these studies for the case of the regular users (blue series), call centers (red series), and fraudsters (green series). People and call centers follow an expected hourly traffic pattern based on the literature, although regular users make significantly less calls. In contrast, fraud cases follow a systematic pattern in which they start calling at 7:00 a.m. until 8:00 p. m. This new set of variables may be useful for distinguishing this behavior.

![](/api/attachments/5CXBABZG/fulltext/images/63ed267b57f6cd3a7960de4df37c7fb152b15f42ed90f7b39625a1b4cb416af4.jpg)  
Fig. 2. The proposed DSS for interpretable traffic pumping detection. It consists of five steps: data preparation, feature engineering, unsupervised learning, mode interpretability via decision trees, and labeling.

## 3.2. Step 3: unsupervised learning

After the data selection and feature engineering steps, step 3 consists in applying a clustering model for grouping the phone numbers in accordance with their call patterns. Our assumption is that the feature engineering process would allow these methods to distinguish fraudu lent from non-fraudulent behavior without the use of labels.

Given that evident non-fraudulent users that do not make at least one long call on a given month are filtered out, our hypothesis is that traffic pumping fraud prediction is not the traditional outlier prediction problem in which fraudsters can be seen as outliers. We expect to discover groups of fraudulent behaviors that follow systematic call patterns for traffic pumping.

![](/api/attachments/5CXBABZG/fulltext/images/e6b011beccd9e4a5fcf342721dd618e7368dc7dd25c2fb3903ff4267f1dbb03a.jpg)  
Fig. 3. Hourly total traffic profiles, in minutes, for call centers, fraudsters, and regular users.

We first suggest the use of the well-known k-means clustering, which is the industry-standard for customer profiling and provides quite good results when clusters that are relatively homogeneous in size are desir able, in contrast to density-based methods [31]. k-means has also been used in fraud detection. For example, Vaishali [32] successfully used this strategy for credit card fraud prediction. However, it is not a common approach in telephony fraud analytics due to the imbalanced nature of the problem, which is not the case in this particular study of traffic pumping fraud.

We also suggest different density-based clustering strategies as al ternatives for k-means. Some of them that have proven positive results are DBSCAN [33], HDBSCAN [34], and OPTICS [35]. The various methods mentioned in this section are formalized in the appendix pro vided as supplementary material. In accordance with the well-known ‘no free lunch’ theorem [36], we suggest exploring different clustering techniques and select the best one in terms of model fit.

The choice of the number of clusters K and the parameters associated to the density based methods, as well as the final choice of the unsu pervised method, can be done using the following cluster quality measures:

• Silhouette: This measure computes the similarity between an object and its own cluster (cohesion) in relation to other clusters (separa tion) using the Euclidean distance. Formally, Silhouette estimates the average distance of an object i to all the objects in the belonging cluster as a(i), and the average distance to the elements of other clusters as b(i). The a(i) indicates how well this data point is assigned to its cluster. The silhouette value for object i is computed as the ratio between b(i) − a(i) and max{a(i),b(i)}. This measure ranges between − 1 and 1 [37]. If most data points have a high silhouette value, then the clustering model is adequate. In contrast, the configuration is suboptimal if several objects have low values. Based on this, we implement the average silhouette for all data points as a quality measure for a certain clustering outcome.

• Davies-Bouldin: This index computes the average similarity $R _ { i j }$ between two clusters i and j as the sum of the within-cluster dispersion of both of them (the average distance between each point to its corresponding cluster center) divided by the separation between clusters i and j. Then, the maximum $R _ { i j }$ for all j with $j \neq i$ quantifies how similar cluster i is in relation to its most similar one. Finally, the Davies-Bouldin Index (DBI) is obtained by averaging all the $R _ { i } = $ max ${ \mathrm { \Sigma } } _ { j } R _ { i j }$ values. Therefore, one is able to conclude that the smaller the DBI, the better the clustering configuration [38].

• Calinsky-Harabasz: This measure, also known as variance ratio cri terion, is a quality measure that relates the within-cluster variance $S S _ { B }$ and between-cluster variance $S S _ { W }$ in a similar fashion as the ANOVA test. For a given cluster, the following ratio is computed: [39]:

$$
C H = \frac {S S _ {B}}{S S _ {W}} \times \frac {N - k}{k - 1},
$$

where N is the number of data points and k the number of them. A large value of this index implies a better cluster partitioning.

## 3.3. Steps 4 and 5: model interpretability and labeling

In order to make our output interpretable, step 4 consists in casting the output into a series of rules via Classification And Regression Trees (CART) [40]. CART trees are a general version of the C4.5 algorithm, in which either entropy or the Gini index can be considered [40]. The XAI approaches by Verbeke et al. [8] and by Martens et al. [9] used C4.5 for rule induction via decision trees in business analytics.

To guarantee the precise definition of fraudulent cases, we suggest imposing two conditions for labeling an example as fraud: (1) it must belong to a cluster with suspicious fraudulent cases, and (2) it must be correctly classified by the CART model in this cluster. The latter con dition is important since the CART model may misclassify some of the objects. Geometrically speaking, our procedure is analogous to create inscribed squares within the clusters defined by the previous step.

Step 5 consists in labeling the clusters as fraudulent or nonfraudulent based on the resulting set of rules that lead to the respec tive cluster. For this step, the input of the experts is crucial.

We suggest building a team of seasoned professionals with experi ence in both regulatory processes and mathematical modeling. At least three experts should be considered to manage the modeling and labeling processes, and, in case they are external consultants, they should hold frequent meetings with experts of the MNO, who can provide important insights for the labeling process.

Regarding inter-rater reliability, the labeling can be an informal process in which the labels assigned to each cluster are able to be discussed among the experts until a consensus is reached. The final model is then discussed with the experts of the MNO before starting the legal process.

In case the group of experts is excessively large to reach a consensus in an informal manner, the Delphi method is suggested. This is an iter ative process in which the experts answer questionnaires in each round, and an anonymized summary is provided afterward with the reasons that justify the answers. Next, the members of the panel have the op portunity to adjust their responses based on the arguments of the other experts [41].

In case the labeling process is inconclusive for a given cluster, a second CART model can be trained to further split the cluster, or it can be labeled as non-fraudulent to make the safest decision. Alternatively, step 4 can be performed again with a different clustering configuration.

## 4. Experimental results

The proposed framework for interpretable traffic pumping fraud analytics is applied to data from a major Chilean network operator. This section is organized as follows: Section 4.1 provides the experimental setup and the description of the dataset. Subsequently, the main results are discussed in Section 4.2. Finally, the model implementation and subsequent legal process against the fraudsters is reported in Section 4.3.

## 4.1. Description of the case study and experimental setting

In 2015, the three largest mobile network operators (MNO) in Chile started offering bundles with unlimited voice minutes included. This crucial aspect enabled other small, fixed line operators to pump traffic from those to their networks.

We collaborated with two of the three affected MNO for a 2.5-year period between 2016 and 2018. The third affected operator benefited from the process indirectly as it was part of the same legal process.

An increment in the total voice traffic from big MNO to small, fixed line operators (mobile to fixed traffic or MF) was the first sign of an anomaly. In Chile and the world, there was a descending trend in MF traffic. However, a few months after the launch of the bundles with unlimited voice traffic, this behavior appeared. This phenomenon was expected at first, but the fact that it only affected some small operators raised suspicion. The three affected MNOs also own fixed networks (FNOs), and they did not observe an increase in traffic within their networks.

The dataset studied in this project consists of CDR data from one month (March 2016), and one of the MNOs. As data preparation (step 1), we selected only those phone numbers that made at least one call of more than 45 min long that month.

After data collection and preparation, our dataset encompasses 469,440 CDR examples, leading to 107,290 OA-OB pairs. The following 41 numeric variables were obtained after performing the feature engineering process proposed in Section 3.1 (step 2):

• Set 1: centrality features

– ANUMS-PER-BNUM: Number of unique ANUMs that call the same BNUM.

– BNUMS-PER-ANUM: Number of unique BNUMS that are called by that ANUM.

– NRotations: Absolute value of the subtraction between ANUMS-PER-BNUM and BNUMS-PER-ANUM.

– Sharing-Address: Number of unique ANUMs that call from that same address.

– Sharing-IMEI: Number of unique ANUMs that call from the same phone, identified by its IMEI.

• Set 2: Monthly patterns

– Charged-total: Total number of seconds called by an ANUM in a given month.

– AVG-charged: Average duration of calls in minutes.

– Sd-charged: Standard deviation of the call duration in minutes.

– Number-calls: Total number of calls made in a given month.

– Days-spoken: Number of days in which at least one call was made in a given month.

– AVG-CACC: Average charge made to the telecommunication company.

– Sd-CACC: Standard deviation of the charge made to the telecom munication company.

• Set 3: Daily patterns

– AVG-calls-per-day: Average number of calls made in one day (the ratio of Number-calls to Days-spoken).

– AVG-occupation-rate-period: Fraction of time in which the OA-OB pair were speaking in a given period of the day. The average for all the days in a given month.

– Sd-occupation-rate-period: Fraction of time in which the OA-OB pair were speaking in a given period of the day. The standard deviation for all the days in a given month.

– VG-Calls-per-hour-period: Average of calls per hour in a given period of the day.

– Sd-Calls-per-hour-period: Standard deviation of calls per hour in a given period of the day.

– AVG-start-hour: Average starting time of the calls in a day (in mi nutes, starting from the 0:00 based on a 24-h clock).

– Sd-start-hour: Standard deviation of the starting time of the calls in a day (in minutes, starting from the 0:00 based on a 24-h clock).

## Table 1

Descriptive information for all variables, including the minimum, the first quartile, the mean, the standard deviation, the coefficient of variation, the third quartile, and the maximum.

<table><tr><td>Variable</td><td>Min</td><td>Q1</td><td>Mean</td><td>Sd</td><td>Coefvar</td><td>Q3</td><td>Max</td></tr><tr><td colspan="8">Set 1: Centrality features</td></tr><tr><td>ANUMS-per-BNUM</td><td>1.00</td><td>530.00</td><td>11,783</td><td>8769</td><td>1.34</td><td>15,341</td><td>23,574</td></tr><tr><td>BNUMS-per-ANUM</td><td>1.00</td><td>1.00</td><td>6.02</td><td>18.80</td><td>0.32</td><td>1.00</td><td>83.0</td></tr><tr><td>Nrotations</td><td>0.00</td><td>529.00</td><td>11,777</td><td>8775</td><td>1.34</td><td>15,340</td><td>23,573</td></tr><tr><td>Sharing-Address</td><td>0.00</td><td>16.00</td><td>49.25</td><td>49.74</td><td>0.99</td><td>62.00</td><td>339.0</td></tr><tr><td>Sharing-Imei</td><td>0.00</td><td>1.00</td><td>1.76</td><td>4.65</td><td>0.38</td><td>1.00</td><td>38.0</td></tr><tr><td>Charged-Total</td><td>1.00</td><td>7.00</td><td>10,775</td><td>60,621</td><td>0.18</td><td>185</td><td>505,704</td></tr><tr><td colspan="8">Set 2: Monthly patterns</td></tr><tr><td>AVG-charged</td><td>0.02</td><td>0.10</td><td>1.07</td><td>4.12</td><td>0.26</td><td>0.90</td><td>120.1</td></tr><tr><td>Sd-charged</td><td>0.00</td><td>0.00</td><td>0.19</td><td>1.44</td><td>0.13</td><td>0.00</td><td>84.8</td></tr><tr><td>number-calls</td><td>1.00</td><td>1.00</td><td>4.38</td><td>26.25</td><td>0.17</td><td>1.00</td><td>2092.0</td></tr><tr><td>Days-spoken</td><td>1.00</td><td>1.00</td><td>1.37</td><td>1.87</td><td>0.73</td><td>1.00</td><td>18.0</td></tr><tr><td>AVG-CACC</td><td>0.19</td><td>2.23</td><td>22.46</td><td>86.62</td><td>0.26</td><td>18.96</td><td>2678.2</td></tr><tr><td>Sd-CACC</td><td>0.00</td><td>0.00</td><td>3.99</td><td>29.80</td><td>0.13</td><td>0.00</td><td>1890.6</td></tr><tr><td colspan="8">Set 3: Daily patterns</td></tr><tr><td>AVG-calls-per-day</td><td>1.00</td><td>1.00</td><td>1.54</td><td>3.25</td><td>0.47</td><td>1.00</td><td>348.7</td></tr><tr><td>AVG-start-hour</td><td>0.00</td><td>692.0</td><td>861.5</td><td>224.1</td><td>3.84</td><td>1030.0</td><td>1439.0</td></tr><tr><td>Sd-start-hour</td><td>0.00</td><td>0.00</td><td>18.34</td><td>64.47</td><td>0.28</td><td>0.00</td><td>1014.0</td></tr><tr><td>AVG-finish-hour</td><td>0.03</td><td>693.4</td><td>862.6</td><td>224.1</td><td>3.85</td><td>1031.2</td><td>1447.1</td></tr><tr><td>Sd-finish-hour</td><td>0.00</td><td>0.00</td><td>18.40</td><td>64.47</td><td>0.29</td><td>0.00</td><td>1014.0</td></tr><tr><td>Calls-per-hour-AVG-1-7</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.06</td><td>0.00</td><td>10.00</td></tr><tr><td>Sd-calls-hour-1-7</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>1.01</td></tr><tr><td>Occupation-rate-AVG-1-7</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.46</td><td>0.03</td><td>0.00</td><td>57.13</td></tr><tr><td>Sd-Occupation-rate-1-7</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.09</td></tr><tr><td>Calls-per-hour-AVG-8-9</td><td>0.00</td><td>0.00</td><td>0.14</td><td>0.45</td><td>0.31</td><td>0.00</td><td>28.17</td></tr><tr><td>Sd-calls-hour-8-9</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.16</td><td>0.13</td><td>0.00</td><td>10.11</td></tr><tr><td>Occupation-rate-AVG-8-9</td><td>0.00</td><td>0.00</td><td>0.22</td><td>1.75</td><td>0.12</td><td>0.00</td><td>200.1</td></tr><tr><td>Sd-Occupation-rate-8-9</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.10</td><td>0.00</td><td>0.37</td></tr><tr><td>Calls-per-hour-AVG-10-13</td><td>0.00</td><td>0.00</td><td>0.16</td><td>0.40</td><td>0.41</td><td>0.25</td><td>31.29</td></tr><tr><td>Sd-calls-hour-10-13</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.15</td><td>0.14</td><td>0.00</td><td>6.54</td></tr><tr><td>Occupation-rate-AVG-10-13</td><td>0.00</td><td>0.00</td><td>0.27</td><td>1.44</td><td>0.19</td><td>0.08</td><td>100.0</td></tr><tr><td>Sd-Occupation-rate-10-13</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.11</td><td>0.00</td><td>0.25</td></tr><tr><td>Calls-per-hour-AVG-14-19</td><td>0.00</td><td>0.00</td><td>0.15</td><td>0.37</td><td>0.41</td><td>0.17</td><td>29.14</td></tr><tr><td>Sd-calls-hour-14-19</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.15</td><td>0.14</td><td>0.00</td><td>4.73</td></tr><tr><td>Occupation-rate-AVG-14-19</td><td>0.00</td><td>0.00</td><td>0.23</td><td>1.20</td><td>0.19</td><td>0.08</td><td>100.0</td></tr><tr><td>Sd-Occupation-rate-14-19</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.12</td><td>0.00</td><td>0.20</td></tr><tr><td>Calls-per-hour-AVG-20-21</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.17</td><td>0.18</td><td>0.00</td><td>7.50</td></tr><tr><td>Sd-calls-hour-20-21</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.02</td><td>0.00</td><td>3.80</td></tr><tr><td>Occupation-rate-AVG-20-21</td><td>0.00</td><td>0.00</td><td>0.08</td><td>1.13</td><td>0.07</td><td>0.00</td><td>100.0</td></tr><tr><td>Sd-Occupation-rate-20-21</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.00</td><td>0.39</td></tr><tr><td>Calls-per-hour-AVG-22-0</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.11</td><td>0.12</td><td>0.00</td><td>6.33</td></tr><tr><td>Sd-calls-hour-22-0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.02</td><td>0.00</td><td>3.30</td></tr><tr><td>Occupation-rate-AVG-22-0</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.87</td><td>0.06</td><td>0.00</td><td>66.65</td></tr><tr><td>Sd-Occupation-rate-22-0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.00</td><td>0.27</td></tr></table>

– AVG-finish-hour: Average finish time of the calls in a day (in mi nutes, starting from the 0:00 based on a 24-h clock).

– Sd-finish-hour: Standard deviation of the finish time of the calls in a day (in minutes, starting from the 0:00 based on a 24-h clock).

The descriptive information for this dataset is summarized in Table 1. The following descriptive statistics were computed for each variable: the minimum (min), the first quartile (Q1), the mean, the standard deviation (Sd), the coefficient of variation (Coefvar), the third quartile (Q3), and the maximum (max).

In Table 1, we observe interesting patterns that are useful for dis tinguishing fraudulent behavior. For example, the maximum number of seconds talked by an OA-OB pair in a given month is 505,704 (5.85 days), which is a clear sign of traffic pumping. Also interesting are the out- and indegree patterns. On the one hand, a large BNUMS-per-ANUM means that a single phone is calling up to 83 unique numbers from a single network provider, which is unrealistic and a case of potential fraud. On the other, a large ANUMS-per-BNUM implies that up to a number receives calls from up to 23,574 unique phones, indicating a probable case of a regular contact center.

Next, a typical fraud configuration is presented in Fig. 4. We use a graph representation to illustrate one fraudulent behavior identified with our approach, in which each node represents a phone number, while the size of the nodes and edges indicate the number of incoming calls for a given number and the calls made by an OA-OB pair, respec tively. Fig. 4 distinguishes two important fraudulent patterns: a single ANUM calling multiple BNUMs (Fig. 4i) repeatedly without receiving calls, and multiple ANUMs calling a single BNUM (Figure 4ii). In both cases, the BNUMs do not perform calls. Note that the two figures correspond to a single fraudulent configuration, in which we emphasize only some of the nodes to ease the visualization of the relevant patterns.

## 4.2. Results summary

The results obtained for the various clustering models described in Section 3.2 are reported in Table 2. Based on the metrics used for assessing cluster quality, we first observe that the k-means method has a better performance in comparison to the remaining algorithms that perform outlier detection, confirming that traffic pumping fraud has a different nature when compared to traditional fraud prediction. This is an important conclusion of this study. Additionally, these metrics sug gest that using K = 3 leads to the best clustering configuration. Regarding the OPTICS method, it was not possible to find a combination of parameters ε and minPoints that provides a solution with three clusters after a broad grid search procedure.

![](/api/attachments/5CXBABZG/fulltext/images/e640e2eb01e8295fd45363b0accf0d1c73e3bc0afe42a0a921b95f987054c11e.jpg)

## Table 2

Summary for the various clustering methods and cluster quality measures. The best performance (largest Silhouette and Calinsky - Harabasz values, smallest Davies - Bouldin value) is emphasized in bold type.  
i Single ANUM calling multiple BNUMs

<table><tr><td>Quality measure</td><td colspan="4">Number of cluster K</td></tr><tr><td>k-means</td><td>K = 3</td><td>K = 5</td><td>K = 7</td><td>K = 9</td></tr><tr><td>Davies - Bouldin</td><td>0.920</td><td>0.985</td><td>1.272</td><td>1.232</td></tr><tr><td>Silhouette</td><td>0.456</td><td>0.376</td><td>0.337</td><td>0.300</td></tr><tr><td>Calinsky - Harabasz</td><td>65,170</td><td>55,427</td><td>45,284</td><td>40,927</td></tr><tr><td>DBSCAN</td><td>K = 3</td><td>K = 5</td><td>K = 7</td><td>K = 9</td></tr><tr><td>Davies - Bouldin</td><td>1.740</td><td>1.901</td><td>1.447</td><td>1.300</td></tr><tr><td>Silhouette</td><td>0.3051</td><td>0.4353</td><td>0.167</td><td>0.263</td></tr><tr><td>Calinsky - Harabasz</td><td>8500</td><td>35,041</td><td>15,460</td><td>23,561</td></tr><tr><td>Param. ε/minPoints</td><td>0.6 / 250</td><td>0.51 / 250</td><td>0.18 / 500</td><td>0.24 / 500</td></tr><tr><td>OPTICS</td><td>K = 3</td><td>K = 5</td><td>K = 7</td><td>K = 9</td></tr><tr><td>Davies - Bouldin</td><td>-</td><td>0.882</td><td>0.930</td><td>0.926</td></tr><tr><td>Silhouette</td><td>-</td><td>0.1216</td><td>0.212</td><td>0.242</td></tr><tr><td>Calinsky - Harabasz</td><td>-</td><td>5798</td><td>24,754</td><td>25,959</td></tr><tr><td>Param. ε/minPoints</td><td>-</td><td>0.6 / 250</td><td>0.32 / 750</td><td>0.3 / 500</td></tr><tr><td>HDBSCAN</td><td>K = 3</td><td>K = 5</td><td>K = 7</td><td>K = 9</td></tr><tr><td>Davies - Bouldin</td><td>1.712</td><td>1.816</td><td>1.453</td><td>1.485</td></tr><tr><td>Silhouette</td><td>0.3066</td><td>0.4380</td><td>0.418</td><td>0.35011</td></tr><tr><td>Calinsky - Harabasz</td><td>8627</td><td>35,078</td><td>59,164</td><td>26,311</td></tr><tr><td>Param. ε/minPoints</td><td>0.6 / 250</td><td>0.51 / 250</td><td>0.18 / 750</td><td>0.26 / 250</td></tr></table>

As discussed above, it is expected that better partitioning of clusters have higher Silhouette and Calinsky - Harabasz scores, alternatively Davies & Bouldin shows a better performance while the magnitude is closer to 0. Bearing that in mind, as shown in Table 2, the lower the K in k-means, the better the index. This is transversal in all three indexes and both in Silhouette and in Calinsky- Harabasz. We find the best perfor mance of all clustering algorithms in k-means with K = 3. On the other hand, DBSCAN and its hierarchical version HDBSCAN algorithms show lower performance in all three scores than other methods. OPTICS outperforms k-means and other methods in Davies & Bouldin index when parameters eps and minSamples (counterpart to minPoints) are set as 0.28 and 250, respectively. In the scenario described above, k-means with K = 3 is selected among the other methods as the best clustering partition.

Regarding model stability, we acknowledge that a drawback of the Kmeans algorithm is that different initial conditions may lead to different solutions. We have addressed this issue by running the K-means algo rithm 10 times using different randomly generated centroids. The result of this experiment was that all 10 runs of the algorithm converged to the same clustering solution. We can conclude that the final model with three clusters is stable and robust to different random seeds.

Next, the decision tree that results from using k-means with k = 3 (X0, X1, and X2) is presented in Fig. 5. This simple tree can be easily interpreted: OA-OB pairs with a considerably large indegree (more than 9270 unique numbers, variable ANUMS-PER-BNUM) fall in cluster X1, which represents 65% of the cases. This is an expected behavior between a contact center (BNUM) and users (ANUM) that perform one or more long calls to it. We label this cluster as non-fraudulent. In contrast, cluster X2 has a smaller indegree but an extremely large outdegree (more than 62 unique numbers, variable BNUMS-PER-ANUM). We label this behavior as fraudulent based on the experts’ input. This cluster represents 5% of the cases. Note that the second row of data in each node represents the percentage of objects in each cluster that follow that path. According to this, the classification performance of the CART tree is perfect or almost perfect.

![](/api/attachments/5CXBABZG/fulltext/images/4ce27cf22ef8c7fe694dae2135e559ecf03cde5a607803de235265973fc231c8.jpg)  
ii Multiple ANUMs calling a single BNUMs  
Fig. 4. Graph representation of a typical fraudulent behavior. Each node represents a phone number, while the size of the nodes and edges indicate the number of incoming calls for a given number and the calls made by an OA-OB pair, respectively.

Cluster X0 is harder to evaluate because it includes the 30% of the OA-OB pairs that do not follow these extreme behaviors. Based on the experts’ input, we decided to perform a second clustering model split ting cluster X0 into new ones, allowing the identification of additional fraudulent behaviors. Following the same methodology applied for the previous clustering model, we analyze the performance of the k-means algorithm for the various K values in Table 3. Based on this table, we decided to use $K = 6 ,$ , dividing cluster X0 into six new ones resulting in a total of eight.

The resulting decision tree for dividing cluster X0 is presented in Fig. 6. We adjusted the notation and referred to these six new clusters as X3 to X8, considering X1 and X2 from Fig. 5 as final clusters. The following rules can be derived from this tree, which allow us to identify new fraudulent behaviors.

• The first rule indicates that the OA-OB pairs that have calls with an average duration (AVG-charged) below 49 s belong to either cluster X3 or X6. This is considered as a non-fraudulent behavior. The number of unique phones calling from that same address (Sharing Address) is used to distinguish cluster X3 (regular users) from X6 (companies with four or more lines).

• The second rule is based on the standard deviation of the charge made to the telecommunication company (Sd-CACC). This variable was created in order to distinguish ‘heavy users’(see first rule) that have a rather erratic behavior in contrast to systematic call patterns that may be a sign of fraud. Consumers with a large variance end up in clusters X3 or X7, using Sharing-Address to distinguish between them. Both clusters are then considered as a non-fraudulent behavior.

• The third rule is the average starting hour of the calls (AVG-starthour), equal or longer than 840 min, which coincides with 2 pm. In

## Table 3

Summary for the various K values and cluster quality measures. k-means clus tering on cluster X0. The best performance (largest Silhouette and Calinsky - Harabasz values, smallest Davies - Bouldin value) is emphasized in bold type.

<table><tr><td>k-means</td><td>K = 3</td><td>K = 4</td><td>K = 5</td><td>K = 6</td><td>K = 7</td></tr><tr><td>Davies - Bouldin</td><td>1.771</td><td>1.526</td><td>1.386</td><td>1.301</td><td>1.336</td></tr><tr><td>Silhouette</td><td>0.178</td><td>0.202</td><td>0.196</td><td>0.215</td><td>0.205</td></tr><tr><td>Calinsky - Harabasz</td><td>6070</td><td>6230</td><td>6069</td><td>5731</td><td>5438</td></tr></table>

this case, we distinguish between consumers that usually made calls in the afternoon or night, from the ones that made calls during the morning. Given the experts’ input, we conclude that scammers tend to make calls in the morning, and therefore we label consumers that belong to either cluster X3 or X4 as non-fraudulent. AS was the case in the previous rules, cluster X3 involves only a few phone numbers calling from the same address, supporting our previous conclusion (neither fraudulent behaviors, nor call centers).

• The fourth and final rule is the use of the outdegree variable BNUMS-PER-ANUM, implemented to identify fraudulent cluster X2. In this case, cluster X8 shows an abnormally large outdegree (19 or more unique phone numbers). Since the previous rules suggest a suspicious behavior, we label this cluster as fraudulent. It is important to notice that this cluster’s classification is perfect or almost perfect (see sec ond row of the X8 node), which means that the decision tree is certain of this pattern. Similar to the cases of possible non-fraudulent behavior, cluster X3 is distinguished from another one (X5 in this case) using the Sharing-Address variable, which supports our reasoning.

Regarding model implementation, we considered the Recursive PARTitioning (RPART) approach implemented in the ‘rpart’ R package. This method considers the generalized Gini index as an impurity func tion to minimize in the splitting step, and includes a pruning parameter CP used to limit the growth of the tree and therefore reduce the risk of overfitting. Despite the fact that the goal of the tree is to describe the clusters and does not have a predictive purpose, we propose to use a simple holdout procedure for tuning parameter CP. This procedure is adequate for constructing interpretable trees that are not too deep, and also to assess its ability to generalize the patterns on an unseen dataset.

![](/api/attachments/5CXBABZG/fulltext/images/344dff78c4f2135b43538a5f3e5cfb2926300c8f615d604714aadeef1905f927.jpg)  
Fig. 5. CART tree for the best K-means clustering model. The leaf nodes represent the outcome of the model.

Table 4  
![](/api/attachments/5CXBABZG/fulltext/images/408e578b8705333575b1f74edbacfcb8fd8fbeaaecc3d3bf4ac0c1039c1b6551.jpg)  
Fig. 6. CART tree for cluster X0 of the K-means model. The leaf nodes represent the outcome of the model.

## 4.3. Implementation and legal process

In summary, we identified two different clusters of fraudulent behavior: X2, with 5% of the OA-OB pairs, and X8, with 2% of the OA-OB pairs (5% of the examples in X0). The two decision trees constructed in the previous section were able to effectively cast the output of the clustering models into a set of rules, especially regarding the two clusters of fraudulent cases. This is demonstrated in Table 4, which illustrates the confusion matrix created as a result of combining the two decision trees using the full dataset. The overall accuracy of the model is 97.1%, and it is particularly positive for the fraudulent clusters.

Table 5 illustrates the results obtained from the test set using holdout validation: 70% of the samples were applied for training and the remaining percentage was used for testing. The overall accuracy of the procedure is 97.0%, confirming the ability of the decision trees to identify the clusters correctly on an out-of-sample setting. This allows us to discard any sign of overfitting.

This study’s approach is the average daily patterns we observed in each cluster, which follow the expected behaviors of regular users, call centers, and fraudulent cases. For example, Fig. 3 contained in Section 3.1 was constructed by using the data from cluster X1 (call centers), X2 (fraudsters), and X5 (regular users). This figure allowed us to confirm the labels we assumed for each cluster based on the rules extracted from the decision trees, and also to better understand the fraudulent patterns.

We advised the network company to start legal actions against the users that were associated with the clusters that were classified as fraudsters by the decision trees. As can be seen in Tables 4, 5773 and 1664 samples were classified as clusters X2 and X8, respectively.

## Table 5

Confusion matrix for the test dataset of the holdout procedure. The numbers in the diagonal represents the users correctly identified in their corresponding clusters.

<table><tr><td>Pred./Real</td><td>X1</td><td>X2</td><td>X3</td><td>X4</td><td>X5</td><td>X6</td><td>X7</td><td>X8</td></tr><tr><td>X1</td><td>13,775</td><td>0</td><td>1</td><td>4</td><td>7</td><td>0</td><td>5</td><td>0</td></tr><tr><td>X2</td><td>0</td><td>1164</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>X3</td><td>0</td><td>0</td><td>599</td><td>5</td><td>6</td><td>2</td><td>1</td><td>0</td></tr><tr><td>X4</td><td>0</td><td>0</td><td>10</td><td>1317</td><td>5</td><td>149</td><td>11</td><td>0</td></tr><tr><td>X5</td><td>0</td><td>0</td><td>11</td><td>0</td><td>1378</td><td>65</td><td>19</td><td>1</td></tr><tr><td>X6</td><td>0</td><td>0</td><td>12</td><td>33</td><td>93</td><td>1296</td><td>16</td><td>22</td></tr><tr><td>X7</td><td>0</td><td>1</td><td>91</td><td>30</td><td>25</td><td>4</td><td>948</td><td>8</td></tr><tr><td>X8</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>339</td></tr></table>

Furthermore, cases from X2 are predicted as cluster X8 on 26 occasions. According to the experts, these cases can be considered with certain degree of conviction as fraudulent; therefore, a total of 7463 cases were acknowledged as such.

We started a legal process against all these suspicious behaviors, leading to confirmation and fines by the Chilean legal system. The legal team analyzed the OA-OB pairs proposed as fraudulent, and decided to pursue legal actions against 7462 of them, which ended with a positive outcome for the plaintiff and the model; all of the cases taken to Court received a favorable award, with fraud being declared in each verdict.

Similar to other fraud detection tasks, it is not possible to confirm whether we have false negatives or not, since no actions were taken against the cases labeled as non-fraudulent. Since true labels are not available, the proportion of fraudulent cases within the clusters labeled as non-fraudulent is also unknown. For these reasons, it is close to impossible to assess the real performance of fraud prediction. Never theless, we strongly believe that the proposal is considerably effective at detecting traffic pumping accurately. Fraudsters require to spend several hours per day on the phones in order to profit from this type of felony. This significantly reduces the risk of undetected fraudulent behavior.

Confusion matrix for the full dataset. The numbers in the diagonal represents the users correctly identified in their corresponding clusters.

<table><tr><td>Pred./Real</td><td>X1</td><td>X2</td><td>X3</td><td>X4</td><td>X5</td><td>X6</td><td>X7</td><td>X8</td></tr><tr><td>X1</td><td>69,376</td><td>0</td><td>3</td><td>25</td><td>37</td><td>0</td><td>29</td><td>0</td></tr><tr><td>X2</td><td>0</td><td>5773</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>X3</td><td>0</td><td>0</td><td>2894</td><td>23</td><td>29</td><td>12</td><td>1</td><td>0</td></tr><tr><td>X4</td><td>0</td><td>0</td><td>50</td><td>6550</td><td>22</td><td>737</td><td>116</td><td>0</td></tr><tr><td>X5</td><td>0</td><td>0</td><td>38</td><td>0</td><td>6819</td><td>274</td><td>119</td><td>4</td></tr><tr><td>X6</td><td>0</td><td>0</td><td>49</td><td>197</td><td>532</td><td>6403</td><td>76</td><td>84</td></tr><tr><td>X7</td><td>0</td><td>4</td><td>415</td><td>110</td><td>90</td><td>16</td><td>4647</td><td>45</td></tr><tr><td>X8</td><td>0</td><td>26</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1664</td></tr></table>

Notice that the results presented in this section correspond to one month of data for one of the two advised MNOs. The following process was applied thirty times at the end of 30 consecutive months (2.5 years):

1. The two advised MNOs provided the CDRs of the outgoing traffic from the MNOs to the FNOs allegedly to be fraudulent.

2. The team of experts provided a recommendation based on the rules derived from the CDR data to the two advised MNOs.

3. Once the rules are validated, a presentation was made to the National Regulatory Agency (NRA, called SUBTEL in Chile) team in charge of the technical trial, in which they were the judges. Representatives of the accused FNOs were also there to defend their positions.

All the people that participated in the entire process were seasoned professionals. The team of experts that developed the mathematical model consisted of three engineers with a master’s degree (two of them also with a Ph.D.) with more than 20 years of experience. They have participated, either individually or as a team, in several (more than 60) regulatory processes, pricing projects, tariff estimations, economic dis putes, due diligence processes, arbitrages, and studies in network eco nomics, mainly the telecommunications industry and energy. This team was advised by the two MNO groups, which included one electrical engineer and one senior regulatory manager each.

## 5. Conclusions

This paper presents a data-driven approach for addressing traffic pumping via unsupervised learning techniques and XAI. Although several studies acknowledge the importance of this type of fraud [1,3], our proposal is the first machine learning approach tailored for traffic pumping, to the best of our knowledge.

Our proposal extends the existing literature on interpretable ma chine learning by deriving rules from a clustering algorithm, and casting the model into a set of rules that can be used to justify a legal procedure against fraudsters (scammers). In particular, the proposed DSS is an extension of the XAI studies by Verbeke et al. [8] and Martens et al. [9] for churn prediction and credit scoring, respectively. In contrast to these studies, our methodology derives rules from unsupervised learning techniques, contributing to the state of the art on XAI strategies for business analytics, and to the praxis of fraud prediction in telecommunications.

From the experiments conducted in this paper, we concluded that k means achieved best performance in relation to alternative clustering algorithms that perform outlier detection using three different metrics (Davies - Bouldin, Silhouette, and Calinsky - Harabasz). This result confirms our hypothesis that traffic pumping fraud has a different nature when compared to traditional fraud prediction, once evident nonfraudulent cases are filtered out. In this case, regular mobile users that did not perform a single long call within the period of study were filtered out in order to ease the learning process, resulting in a problem with clearly defined clusters rather than an outlier detection task. This is an important conclusion of this study, since density-based clustering tech niques for outlier detection have become the ‘de facto’ strategy for un supervised fraud detection (see e.g. [4,12]).

A second important conclusion that can be drawn from our results is the success of the CART trees in making the clusters interpretable, adjusting their shape. The out-of-sample accuracy for this step was 97.0%, which is extremely positive for a multi-class problem with eight different labels. We proposed a robust labeling scheme in which two conditions must be fulfilled by the suspicious cases: it should belong to a cluster labeled as fraudulent, and it must be classified correctly by the decision tree.

This work goes beyond most machine learning and business analytics papers that compare several methods considering, mainly, performance, which leads to favoring a particular method above others. This work is a case study in which the success of the method lies in the legal procedures carried out against the fraudsters. For the data sample studied in this paper (one month for one MNO), the legal team of the company that requested the proposed model used it to file claims against 7462 sus picious OA-OB pairs unveiled by our strategy. These claims were ratified as fraud in court, and the fraudsters were fined. With these measures, the company was able to reduce their losses and discourage this behavior in future references.

In order to provide a rough estimate of the benefits of the DSS, we observed a total increment in MF traffic between 2015 and 2016 of more than 70% by the suspicious FNOs. It is relevant to point out that the total MF traffic is less than 20% of the total outgoing one from MNOs, and the traffic to the suspicious operators was less than 40% of the total MF. We have no evidence to confirm that all the incremented traffic was fraudulent, but we believe it is useful for making the estimation.

There is a direct relation between the MF traffic and the money paid in access charges by the MNOs to the FNOs, since the latter are computed as the access charge tariff (in Chilean pesos per minute) times the MF traffic (in minutes). Considering only the two MNOs we advised, we estimate they roughly saved 5 million USD (2.5 million each) during the 2.5 years of study. This represents approximately a 40% reduction in the total access charges the MNOs would have to pay. We know this computation does not account for the 70% increment in MF traffic, but we had no proof to confirm it was due to fraudulent behavior.

The proposed procedure confirms that the advantages of interpret able machine learning in business analytics go beyond gaining mana gerial insights into the application. Interpretability may be a constraint imposed by regulators in order to pursue a given action, such as a legal process against suspicious fraudulent cases. In this sense, there is a parallel between this study and credit scoring. For this task, credit grantors are required to be able to explain the reasons why applicants are accepted or rejected. Therefore, only interpretable classifiers are allowed by the international agreements, being the Basel III Accord the current legal scheme in several countries [42].

One limitation of this study is that it provides a static view of a dy namic, adversarial problem such as fraud prediction. For this reason, we limited our study to the first month in which the legal actions were taken against the fraudsters. There are, however, several dynamic clustering techniques that may be useful for modeling the fraudulent behavior for the different periods (see e.g. [43]). We believe this is an interesting avenue for future research, since we have access to the CDR data for the months following the lawsuits. According to the company, the fraudsters adjusted their behavior in order to pass undetected. We can use this information to develop novel dynamic models that are able to capture this adversarial behavior, gaining relevant insights into the application.

There are interesting opportunities for future research. For example, supervised learning can be used to model the dynamics of the task using the labels generated in this study. Recent developments such as the generalized random forest [44], or casual forest can be useful at boosting performance while model causal relations in the data.

## Acknowledgements

The authors gratefully acknowledge financial support from CON ICYT PIA-BASAL AFB180003 and FONDECYT-Chile, grants 1200221 and 11200007. The authors are grateful to the anonymous referees for their careful reading and helpful suggestions that improved the paper greatly.

<table><tr><td colspan="2">Algorithm 1 K-means algorithm</td></tr><tr><td colspan="2">Random initialization of the centroids {m1,...,mK}.</td></tr><tr><td colspan="2">repeat</td></tr><tr><td colspan="2">1. Partitioning step: assign each sample i to the closest cluster centroid:</td></tr><tr><td colspan="2">C(i) = argmin1≤k≤K ||xi - mk||2 (A.1)</td></tr><tr><td colspan="2">2. Centroid update step: compute the new centroid k as the mean of all samples that belong to cluster k, based on the encoder C.</td></tr><tr><td colspan="2">until Convergence is reached (assignments do not change)</td></tr></table>

## Appendix A. The clustering approaches

## k-means clustering

The k-means clustering algorithm assigns each training sample $i \in \{ 1 , . . . , m \}$ to a given cluster $k \in \left\{ 1 , . . . , K \right\}$ , with K defined a priori. An encoder C can be used, where the assignment of sample i to cluster k is represented by $C ( i ) = k [ 3 6 ]$ . This process is done via a two-step heuristic in order to minimize the total within-cluster variance, having the cluster centroids $\{ m _ { 1 } , . . . , m _ { K } \}$ as decision variables. The K-means algorithm follows:

We also explore the following clustering approaches: The Density Based Spatial Clustering of Applications with Noise (DBSCAN) method, Ordering Points to Identify the Clustering Structure (OPTICS), and Hierarchical DBSCAN (HDBSCAN). These methods are described below.

## DBSCAN

DBSCAN classifies the examples in either a dense region where clusters belong, or a sparse zone in which the outliers will be found [33]. This method considers $\varepsilon ,$ the maximal distance for two points to be taken as neighbors, and minPoints, the minimal number of points in a neighborhood in order to be considered as dense, as input parameters. DBSCAN then labels each example either as core, border, or noise point based on the following rules:

• Core point: a point which in its ε-neighborhood contains at least minPoints number of points.

• Border point: refers to the frontier of a dense region. This point is part of a cluster but not dense in itself, in the sense that the size of its own ε–neighborhood is not large enough to be considered as a core point.

• Noise: every point that is neither a core or border point.

After labeling each point, the method defines the set of points that conform each cluster by considering three different criteria:

• Directly density-reachable: a point q is directly density-reachable from point p if p is a core point and distance(p, q) is less or equal to ε.

• Density-reachable: a point q is density-reachable from point p, if q is directly density reachable from a point p, which is also directly density reachable from point p, i.e. there is a set of core points leading from p to q.

• Density connected: two points p and q are density connected if there is a point o that serves as a bridge between them. In this case, points q and p are density reachable from point o.

Finally, a cluster is a subset with at least one core point having all its density-reachable, and density-connected points associated to it. OPTICS

One of the disadvantages of the DBSCAN algorithm is that it assumes that all clusters have the same density [35]. OPTICS improves this aspect by identifying clusters with different densities. To do so, the dataset is sorted in such a way that closest examples become neighbors after the ordering process, simplifying the generation of clusters. In relation to DBSCAN, the OPTICS algorithm introduces the following two new distances:

• Core-distance: given an ε–neighborhood from core point p, the core-distance is that between the core point p and the minPoints neighbor. In case p is not a core point, core-distance will be undefined.

• Reachability distance: the reachability distance of point q with respect to core point p in an ε – neighborhood of p corresponds to the maximal one between distance(p, q) and core distance of point p. In case the cardinality of the ε-neighborhood from point p is inferior to minPoints, this distance will be set as undefined

The OPTICS algorithm first stores the core and reachability-distance for every point in the dataset with respect to any ε<sup>′</sup> smaller than the generating distance ε. Then, the data points are ordered with respect to ε and minPoints, assigning a cluster to each point. If p and q are nearest neighbors, for example, they will belong to the same cluster if $\varepsilon ^ { \prime } < \varepsilon \ [ 3 5 ]$

## HDBSCAN

The HDBSCAN algorithm is a DBSCAN variant in which border points are labeled as noise, while the membership of a cluster is defined by the distance between points ordered as a hierarchical tree [34].

An important concept in HDBSCAN is the mutual-reachability distance, which corresponds to the maximum one between the core–distance of p, the core–distance of q, and distance(p, q). Under this distance, objects in dense zones (i.e. with low core distance) remain at the same one from each other, while outliers are pushed away

Representing the dataset as a weighted graph with edges between vertices (the objects), being represented by the mutual-reachability distances, we can generate a process for dropping edges and generating connected groups of examples. The use of varying thresholds to disconnect the graph leads t a hierarchical structure (from fully connected to fully disconnected).

HDBSCAN works as follows: it computes a single linkage hierarchy tree using the mutual-reachability distance measure, pruning noisy data points/ outliers from the tree and generating clusters as the threshold decreases. Then, the algorithm selects the best clustering combination by maximizing each cluster stability [34].

## Appendix B. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.dss.2021.113559.

## References

[1] M. Sahin, A. Francillon, P. Gupta, M. Ahamad, Sok: Fraud in telephony networks, in: 2017 IEEE European Symposium on Security and Privacy (EuroS&P), IEEE, 2017, pp. 235–250.

[2] B. Baesens, V. Van Vlasselaer, W. Verbeke, Fraud Analytics Using Descriptive, Predictive, and Social Network Techniques: A Guide to Data Science for Fraud Detection, John Wiley & Sons, 2015.

[3] R.A. Becker, C. Volinsky, A.R. Wilks, Fraud detection in telecommunications: history and lessons learned, Technometrics 52 (1) (2010) 20–33.

[4] T. Pourhabibi, K.-L. Ong, B.H. Kam, Y.L. Boo, Fraud detection: a systematic literature review of graph-based anomaly detection approaches, Decis. Support. Syst. 113303 (2020).

[5] J.-J. Laffont, J. Tirole, Competition in Telecommunications, MIT press, 2001.

[6] S.M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, in: Advances in Neural Information Processing Systems, 2017, pp. 4765–4774.

[7] C. Molnar, Interpretable machine learning: a guide for making black box models explainable, URL https://christophm.github. io/interpretable-ml-book (2020).

[8] W. Verbeke, D. Martens, C. Mues, B. Baesens, Building comprehensible customer churn prediction models with advanced rule induction techniques, Expert Syst. Appl. 38 (2011) 2354–2364.

[9] D. Martens, B. Baesens, T. Van Gestel, J. Vanthienen, Comprehensible credit scoring models using rule extraction from support vector machines, Eur. J. Oper. Res, 183 (3) (2007) 1466–1476.

[10] R.F.L. Costa, Next Generation Machine Learning based Real Time Fraud Detection, Ph.D. thesis. Universidade do Porto. 2020.

[11] P. Hajek, Interpretable fuzzy rule-based systems for detecting financial statement fraud, in: IFIP International Conference on Artificial Intelligence Applications and Innovations, Springer, 2019, pp. 425–436

[12] R.J. Bolton, D.J. Hand, et al.. Ünsupervised profiling methods for fraud detection in: Credit Scoring and Credit Control VII, 2001, pp. 235–255.

[13] A. Chouiekh, E.H.I.E. Haj, Convnets for fraud detection analysis, Procedia Comp. Sci. 127 (2018) 133–138.

[14] D. Olszewski, A probabilistic approach to fraud detection in telecommunications, Knowl.-Based Syst. 26 (2012) 246–258.

[15] D. Olszewski, Fraud detection using self-organizing map visualizing the user profiles, Knowl.-Based Syst. 70 (2014) 324–334.

[16] D. Xing, M. Girolami, Employing latent dirichlet allocation for fraud detection in telecommunications, Pattern Recogn. Lett. 28 (13) (2007) 1727–1734.

[17] Q. Zhao, K. Chen, T. Li, Y. Yang, X. Wang, Detecting telecommunication fraud by understanding the contents of a call, Cybersecurity 1 (1) (2018) 8.

[18] Y. Wang, W. Xu, Leveraging deep learning with lda-based text analytics to detect automobile insurance fraud, Decis. Support. Syst. 105 (2018) 87–95.

[19] W. Samek, G. Montavon, A. Vedaldi, L.K. Hansen, K.-R. Müller, Explainable AI: Interpreting, Explaining and Visualizing Deep Learning Vol. 11700, Springer Nature, 2019.

[20] Scott M. Lundberg, Gabriel G. Erion, Su-In Lee, Consistent individualized feature attribution for tree ensembles, 2019 arXiv:1802.03888.

[21] S. Han, J. Pool, J. Tran, W. Dally, Learning both weights and connections for efficient neural network, in: Advances in Neural Information Processing Systems, 2015, pp. 1135–1143.

[22] Finale Doshi-Velez, Been Kim. Towards a rigorous science of interpretable machine learning, 2017 arXiv:1702.08608

[23] D. Martens, F. Provost, Explaining data-driven document classifications, MIS Q. 38

[24]. D. Breuker, M. Matzner. P. Delfmann. J. Becker, Comprehensible predictive models for business processes, MIS Q. 40 (2016) 2016, https://doi.org/10.25300/MISQ/ 2016/40.4.10.

[25] Y.-J. Park, H.-L. Choi, Infossm: Interpretable unsupervised learning of nonparametric state-space model for multi-modal dynamics. arXiv:1809.07109, 2018.

[26] F. Villarroel-Ordenes, B. Theodoulidis, J. Burton, T. Gruber, M. Zaki, Analyzing customer experience feedback using text mining: a linguistics-based approach,

[27] K. Coussement, D. Van den Poel, Improving customer complaint management b automatic email classification using linguistic style features as predictors, Decis. Support. Syst, 44 (4) (2008) 870–882.

[28] S. Maldonado, R.G. Gonz´alez-Ramírez, F. Quijada, A. Ramírez-Nafarrate, Analytics meets port logistics: a decision support system for container stacking operations, Decis. Support. Syst. 121 (2019) 84–93.

[29] P.E. Heegaard, Evolution of traffic patterns in telecommunication systems, in: 2007 Second International Conference on Communications and Networking in China, IEEE, 2007, pp. 28–32.

[30] O. Jarv, R. Ahas, E. Saluveer, B. Derudder, F. Witlox, Mobile phones in a traffic flow: A geographical perspective to evening rush hour traffic analysis using cal detail records, PLoS One 7 (11) (2012) 1–12, https://doi.org/10.1371/journal. pone.0049171. URL

[31] R.C. Blattberg, B.-D. Kim, S.A. Neslin, Database Marketing: Analyzing and Managing Customers, Springer, 2008.

[32] V. Vaishali, Fraud detection in credit card by clustering approach, Int. J. Comput. Appl. 98 (3) (2014) 29–32.

[33] M. Ester, H.-P. Kriegel, J. Sander, X. Xu, et al., A density-based algorithm for discovering clusters in large spatial databases with noise, in: KDD-96 Proceedings, 1996, pp. 226–231.

[34] R.J. Campello, D. Moulavi, J. Sander, Density-based clustering based on hierarchical density estimates, in: Pacific-Asia Conference on Knowledge Discovery and Data Mining, Springer. 2013, pp. 160–172.

[35] M. Ankerst, M.M. Breunig, H.-P. Kriegel, J. Sander, Optics: ordering points to identify the clustering structure. ACM SIGMOD Rec. 28 (2) (1999) 49–60.

[36] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer Science & Business Media, 2009.

[37] P.J. Rousseeuw, Silhouettes: a graphical aid to the interpretation and validation of cluster analysis, J. Comput. Appl, Math. 20 (1987) 53–65

[38] D.L. Davies, D.W. Bouldin. A cluster separation measure. JEEE Trans. Pattern Anal Mach. Intell, PAMI-1 (2) (1979) 224–227.

[39] T. Calinski, ´ J. Harabasz, A dendrite method for cluster analysis, Communicat. Stat.

[40] L. Breiman, J. Friedman, C.J. Stone, R.A. Olshen, Classification and Regression Trees, CRC press, 1984.

[41] G. Rowe, G. Wright, The Delphi technique as a forecasting tool: issues and analysis Int. J. Forecast. 15 (4) (1999) 353–375.

[42] B. Baesens, D. Roesch, Scheule, Credit Risk Analytics: Measurement Techniques, Applications, and Examples in SAS, John Wiley & Sons, 2016

[43] R. Saltos, R. Weber, S. Maldonado, Dynamic rough-fuzzy support vector clustering, JEEE Trans. Fuzzy Syst, 25 (6) (2017) 1508–1521

[44] S. Athey. J. Tibshirani, S. Wager, Generalized random forests. Ann, Stat. 47 (2 (2019) 1148–1178.

![](/api/attachments/5CXBABZG/fulltext/images/cacea4d84c87358e3d5000f11ab210766aa773eadd508ab90a9038703489a8bc.jpg)  
María Elisa Irarrazaval ´ is MSc and Industrial Engineer. This manuscript is a result of her thesis work. which was supervised by Carla Vairetti

![](/api/attachments/5CXBABZG/fulltext/images/008290d436147bcd055b1281417259ef6d5b141bea9610a7e02d6357c0c2011e.jpg)

![](/api/attachments/5CXBABZG/fulltext/images/1bcaa2e62bdbd62f3a4766970141a968d0a979871fb4e0537432c055e99221e9.jpg)

Sebastián Maldonado received his B.S. and M.S. degrees from the University of Chile, in 2007, and his Ph.D. degree from the University of Chile, in 2011. He is currently Full Professor at the Department of Management Control and Information Systems, School of Economics and Business, University of Chile. Hi research interests include statistical learning, data mining and business analytics. Sebasti´an Maldonado has published mor than 70 scientific contributions in the last ten years.

Juan Perez ´ is an Associate Professor at Universidad de Lo Andes (Chile). He received his bachelor’s degree in Electrical Engineering, MSc in Operations Research, and a Ph.D. in En gineering Systems from the University of Chile. His research interest: operations research. mathematical modeling. and pricing analytics

![](/api/attachments/5CXBABZG/fulltext/images/3c90b4878e19aea105593c93c99e8130e8061bf42a809fe51dd905d7f7f25439.jpg)

Carla Vairetti received her B.S. degree in Computer Science in 2000 from the University Nacional de La Plata, Argentina. She also received an M.S. degree in Sciences in 2013 from the Pontificia Universidad Catolica, ´ Chile, and the Ph.D. degree in Engineering Sciences in 2016 from the University of Trento, Italy. Currently, she is Assistant Professor of Universidad de Los Andes. Her research interests include classification in imbal anced domains, multiclassification problems with ensembles and decomposition techniques, data science in big data appli cations, computational Intelligence (including machine and deep learning) and data science.
