---
otero_id: 494
otero_key: "JY9SJKDV"
title: "Loyal to your city? A data mining analysis of a public service loyalty program"
authors: "Sofie De Cnudde; David Martens"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Loyal to your city? A data mining analysis of a public service loyalty program

Sofie De Cnudde ⁎, David Martens

Department of Engineering Management, Prinsstraat 13, B-2000 Antwerp, Belgium

a r t i c l e i n f o

Article history: Received 5 November 2014 Received in revised form 11 March 2015 Accepted 12 March 2015 Available online 25 March 2015

Keywords: Knowledge discovery Data mining CRM Behavioral data Loyalty card

## a b s t r a c t

Customer loyalty programs are largely present in the private sector and have been elaborately studied. Applications from the private sector have found resonance in a public setting, however, simply extrapolating research results is not acceptable, as their rationale inherently differs. This study focuses on data from a loyalty program issued by the city of Antwerp (Belgium). The aim of the loyalty card entails large citizen participation, however, an active user base of only 20 % is reached. Predictive techniques are emploved to increase this number. Using spatial behavioral user information, a Naive Bayes classi<sup>fi</sup>er and a Support Vector Machine are used which result in models capable of predicting whether a user will actively use its card, whether a user will defect in the near future and which locations a user will visit. Also, a projection of spatial behavioral data onto even more <sup>fi</sup>negrained spatio-temporal data is performed. The results are promising: the best model achieves an AUC value of 92.5 %, 85.5 % and 88.12 % (averaged over <sup>fi</sup>ve locations) for the predictions, respectively. Moreover, as behavior is modeled in more detail, better predictions are made. Two main contributions are made in this study. First, as a theoretical contribution, <sup>fi</sup>ne-grained behavioral data contributes to a more sound decision-making process. Second, as a practical contribution, the city of Antwerp can now make tailored strategic decisions to increase its active user base.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Since the evolution from a product-centric to a customer-centric approach, managing customer relationships has become a necessity for organizations [1]. Customers need to be understood on a percustomer basis in terms of their needs, preferences and potential [2,3]. Maintaining close ties to customers may lead to a competitive advantage and to customer loyalty [4]. In order for organizations to initiate and maintain connections to their customers, Customer Relationship Management (CRM) systems are used. Data mining forms an integral part of these systems and provides insight into raw customer data [5]. Consequently, organizations can closely monitor their customers and anticipate accordingly through proactive marketing such as offering personalized incentives [5]. An important source for CRM data constitutes the output of loyalty programs and more speci<sup>fi</sup>cally from loyalty cards [6]. Loyalty card data is typically characterized by a large sample of transactional data connected to the customers, for which also sociodemographic data is available [7].

The analysis of loyalty programs has been largely researched in literature related to the pro<sup>fi</sup>t sector, especially in retail [8]. In contrast, the behavior of customers in a non-traditional customer–supplier relationship such as the relationship between a customer and the government has not received that kind of attention [2]. The results from analyses performed in the pro<sup>fi</sup>t sector cannot simply be extended to the non-pro<sup>fi</sup>t sector due to their differing rationale. To our knowledge, the analysis of loyalty card data in the context of a public institution has not yet been researched. This study performs an analysis of such data and thereby is a <sup>fi</sup>rst attempt to contribute to this gap. We state the contributions as follows: (1) gaining insight into the behavior of users of a government loyalty card and (2) attempting to learn non-trivial user information from this behavior with the help of data mining techniques. Both should contribute to the design of a decision support system able to lead to highquality information for decision makers.

Concretely, in this design science paper [9], we analyze the behavior of users of the A-Card, a loyalty card issued by the city of Antwerp (Belgium) that can be used in public institutions and partnering institutions such as libraries and musea. The purpose of the card consists of promoting participation in cultural services offered by the city. The data consists of 4 million transactions concerning approximately 177,000 persons visiting one of 102 locations. Currently, there is no widespread use of the bene<sup>fi</sup>ts that come along with the loyalty card. Moreover, users visit a relatively unilateral set of locations. This research presents an analysis of this government data that should empower the city to take appropriate strategic decisions.

The rest of this paper is organized as follows. Section 2 discusses relevant background and previous related work. Section 3 gives a detailed description of the data, the used data mining techniques and the evaluation criteria. Next, in Section 4, the experimental set-up of the research is presented. The results of the analysis are presented and discussed in Section 5. Lastly, Section 6 concludes our work and presents avenues for further research.

## 2. Background and related work

## 2.1. CRM

In the 1990s, organizations' customer focus shifted from a transactional view to a relational view [10]. CRM has since become a pivotal part of organizations. An understanding of customers' preferences may lead to the possibility of tailoring products and services to their wishes, which leads to higher customer satisfaction. This subsequently results in behavioral customer loyalty [11] and ultimately in pro<sup>fi</sup>t. In order for these CRM systems to be of any value for the organization, data has to be collected and techniques have to be available to analyze this data [12]. Loyalty programs are one way of tying customers to an organization through incentives [4]. They are also a source for capturing behavioral patterns of the users which results in a large amount of transactional data.

## 2.2. High-dimensional, behavioral data

Since data collection and storage have become cheap, data is being gathered in vast amounts [13,14]. This data often consists of <sup>fi</sup>negrained behavioral data, such as click behavior of website visitors, payment transactions of a client of a bank or locations visited by a mobile phone user. These <sup>fi</sup>ne-grained features are testimonies of an individual's behavior. Using this data, predictions can be made concerning individual users as to whether they would be interested in a certain news article [15], a certain banking product [16] or a mobile ad [17]. An application in the public sector entails fraud detection in companies using their payment data [18,19]. These big highdimensional feature sets lead to more complexity in the analysis [20], for which traditional dimensionality reduction techniques are not relevant given the low redundancy of the features. Traditional summarizing features such as socio-demographic variables contain more information on a per feature basis in comparison to behavioral features. The latter, however, each gradually add more information which leads to a more informative whole [21].

## 2.3. Analysis techniques in CRM

Once the data is collected, techniques have to be identi<sup>fi</sup>ed to extract information and knowledge. Data mining techniques are techniques that are able to extract patterns from the data which can subsequently lead to vital knowledge for the organization [22]. Ngai, Xiu and Chau performed a comprehensive literature review of data mining studies in the CRM <sup>fi</sup>eld [8]. Here, the CRM <sup>fi</sup>eld is subdivided into four stages: identi<sup>fi</sup>cation, attraction, retention and development of customers. The bulk of the research is positioned in the customer retention phase, and more speci<sup>fi</sup>cally in personalizing marketing campaigns dependent on user's behavior (one-to-one marketing) and with the goal of tying customers to the organization (loyalty programs). The techniques mostly used in these studies consist of neural networks, decision trees and association rule techniques. Applications of data mining techniques in the context of CRM can be found in different sectors such as retail, the banking sector and telco companies [22]. In retailing, a typical application is market basket analysis in order to determine which products are frequently bought together. The banking sector is mainly interested in segmenting its customers in order to focus their marketing efforts towards the right customers. Another important application is fraud detection where suspicious transactions are identi<sup>fi</sup>ed. In the telecommunications sector, churn prediction is of vital importance due to the highly competitive environment.

## 2.4. CRM in a public setting

The public sector deals with distinct challenges with respect to its private counterpart, among others providing basic services to its citizens. Lately, their modernization process has resulted in them adopting a more privatized character [23] along with private-like principles such as a focus on ef<sup>fi</sup>ciency, competitiveness and pro<sup>fi</sup>tability [24]. As time evolves, this transformation will result in applications originating from the private sector, migrating towards the public sector [25]. CRM applications in the public <sup>fi</sup>eld, referred to as e-government, have until now mostly focused on providing equally accessible, transparent and omnipresent public services [26], on citizen engagement [27] and on policing [28]. To this end, diverse data can be used such as citizen feedback and complaints, social media data [29] and government data from legacy systems. The data traditionally used in big data government applications, however, is mostly textual [30]. Introducing behavioral data of some sort could open a new avenue of research and lead to surprising results, as it did in advertising research.

Despite some resemblances between the public and the private sector, two major differences have to be kept in mind. First, the ‘customer’ base of public services is diverse and dynamic [31,32]. Namely, the ‘customer’ base encompasses all citizens that belong to the governing institution. The customer base in the private sector only is a portion of this citizen base. Thus, the data collection opportunities are intrinsically larger and more diverse [33]. Secondly, the ‘customers’ cannot be valued based on pro<sup>fi</sup>tability. In case of CRM in a government setting, customers must not only be served on an individual basis, an extra equality constraint is introduced [2]. Although the principles of CRM can be applied across sectors and industries [34,35], care must thus be taken as to whether results from research in a private setting can be applied to its public counterpart [35]. A government-issued loyalty card cannot be evaluated solely on its <sup>fi</sup>nancial bene<sup>fi</sup>ts for the institution. The element of so-called public value has to be taken into account [36].

## 2.5. Relevance

Underpinning the relevance of our study are the following arguments. First, the public sector is an omnipresent institution in everyday life and offers its services to all aspects of society with a diverse set of stakeholders with whom unique relationships are held, i.e. no pro<sup>fi</sup>tability element is involved [24]. This distinct character results in interesting research opportunities. In the past, research concerning strategy [31], management practices [37], information technology [38] and information systems [39] has been conducted in the public sector and has been compared with practices in the private sector. Extending this research effort to loyalty programs may result in interesting discoveries. Secondly, the use of CRM in the public sector is quite unilateral at present. Using <sup>fi</sup>ne-grained behavioral data has proven to lead to good predictive results [21] and has been employed in advertising research [17,15,16,40]. Hence, investigating whether and to what extent these results are feasible with behavioral data originating from the public sector may give rise to interesting research conclusions. Finally, concerning the overall relevance of this work with respect to the government's cultural responsibility, cultural participation can help connect individuals and lead to civic engagement and social cohesion [41]. One of the goals of the A-Card is to encourage people to take part in the cultural life of the city of Antwerp and to this end analyze the behavior of users visiting public institutions in order to tailor the cultural offer. Getting insight into this behavior may thus lead to bene<sup>fi</sup>ts for the city as a whole.

## 3. Research methodology

## 3.1. The city of Antwerp loyalty card: A-card

The A-Card was introduced on 18 December 2010 by the city of Antwerp (Belgium). Antwerp is the most populated city in Belgium with approximately 510,610 inhabitants [42]. With the A-Card, the city wishes to inform its citizens about its cultural offers, simplify access to cultural venues and convince people to visit cultural venues they have not yet visited. Overall, the goal is to promote participation of inhabitants and visitors in cultural activities organized by the city of Antwerp and for the city to brand itself as attractive for people who live in, work in or visit Antwerp [43].

Inhabitants and visitors of Antwerp can register for an A-Card and use it when visiting certain public venues or venues from partnering institutions. The card can be used in 102 different places located over the city, that are grouped in 9 categories i.e. libraries, swimming pools, musea, cultural centra, the city shop, events, meeting centra, youth centra and digital registration events. The loyalty card costs three euros and is currently only required when lending items in a library. At registration time, users provide some mandatory socio-demographic background and contact information, i.e. name, address, date of birth, gender, nationality, e-mail address. Optionally, they may also provide some extra information regarding their personal interests or the number of members in their family. At registration time, each user immediately receives <sup>fi</sup>ve starter advantages that can be used in each of the following locations: library, swimming pool, museum, cultural center and the city shop. Each subsequent visit yields a point, given that the card is scanned at a so-called A-Card-pillar. These pillars are located in the entrance hallway of the venues and visitors scan their card upon entrance. After collecting 10 points, users can cash these out in return for an advantage such as a discount on an entrance ticket. Points collected from 1 January to 31 August expire on the <sup>fi</sup>rst of January the next year. Points collected from September to December remain active during the next year and expire along with points collected from January to August of that next year. During the last week of October and the <sup>fi</sup>rst week of November, subscribers are reminded of this imminent expiration through two action weeks. The goal is to encourage users to cash out their collected points by offering them extra advantages during these weeks such as discounted or free entrance tickets.

## 3.2. Data characteristics

The data originating from the A-card consists of the visiting behavior of 177,761 users, which in total amount to 4,015,091 transactions that took place between 18 December 2010 and 5 February 2014. In 2011, the standard library card was replaced with the A-Card, which resulted in a high number of registrations that year, i.e. 50.20 % of all users registered then. Table 1 shows these and some other general statistics regarding the loyalty card data. Most transactions take place on Wednesday, while Sunday and Monday are less busy. This can be explained by the fact that school ends at noon on Wednesdays and that most public institutions are closed or only open for half a day on Sunday and Monday. October, November, December and January are busy months. This can be explained by the action weeks that take place during October and November and potentially also the renewal of library subscriptions during January. During holiday periods, such as April, July and August, the transactions experience a low.

## 3.3. Problem introduction

The city of Antwerp would like its A-Card users to actively use their card and cash out the offered bene<sup>fi</sup>ts on a regular basis. However, 56.55 % of all users have never taken advantage of those loyalty bene<sup>fi</sup>ts. Moreover, the active user base, i.e. users collecting and cashing out points on a regular basis, only consists of 18.62 % of the total user population. Fig. 1 shows the users that have enough points to cash out, the so-called potentials, and the users that actually cash out every month. The graph shows the number of potentials rising during 2011 and 2012 and, then, in January 2013 experiencing a signi<sup>fi</sup>cant drop. This drop is attributed to the expiration of points collected from the start until August 2012 (the city of Antwerp decided not to let points expire in January 2012 due to it being the <sup>fi</sup>rst year). After the expiration of points, the potentials group starts rising again until a new imminent expiration. More importantly, Fig. 1 makes clear that a minority of users having collected enough points cash out these points. Possible explanations for this might be that users are not informed about the cashing-out process, that they do not know what bene<sup>fi</sup>ts the city offers them or that these bene<sup>fi</sup>ts do not appeal to them. With respect to loyalty programs in the private sector, Vittal et al. [44] report an average of 35 % of program users who make use of their rewards. We have not found a benchmark in literature which states that a ratio of 20 % active users equals too low a program participation. Moreover, the loyalty card has only been in place for three years. However, we believe it is safe to state that this percentage, along with the <sup>fi</sup>ndings in Fig. 1, is not highly satisfying, considering the context of this particular citizen loyalty program.

Table 1  
General characteristics of the loyalty card data.

<table><tr><td>Total number of users</td><td></td><td>177,761</td></tr><tr><td>Total number of transactions</td><td></td><td>4,015,091</td></tr><tr><td rowspan="4">Number of users registered</td><td>in 2010</td><td>1.75 %</td></tr><tr><td>in 2011</td><td>59.25 %</td></tr><tr><td>in 2012</td><td>32.19 %</td></tr><tr><td>in 2013</td><td>20.22 %</td></tr><tr><td rowspan="3">Usage by</td><td>inhabitants of Antwerp</td><td>85.43 %</td></tr><tr><td>visitors from outside Antwerp</td><td>14.40 %</td></tr><tr><td>foreign tourists</td><td>0.14 %</td></tr><tr><td>Gender (female)</td><td></td><td>54.63 %</td></tr><tr><td rowspan="9">Users with age between</td><td>1-10</td><td>1.05 %</td></tr><tr><td>11-20</td><td>21.71 %</td></tr><tr><td>21-30</td><td>14.88 %</td></tr><tr><td>31-40</td><td>13.57 %</td></tr><tr><td>41-50</td><td>11.31 %</td></tr><tr><td>51-60</td><td>10.08 %</td></tr><tr><td>61-70</td><td>8.94 %</td></tr><tr><td>71-80</td><td>5.57 %</td></tr><tr><td>81-90</td><td>2.22 %</td></tr><tr><td rowspan="7">Transactions per weekday</td><td>Monday</td><td>8.97 %</td></tr><tr><td>Tuesday</td><td>19.12 %</td></tr><tr><td>Wednesday</td><td>21.04 %</td></tr><tr><td>Thursday</td><td>15.08 %</td></tr><tr><td>Friday</td><td>13.05 %</td></tr><tr><td>Saturday</td><td>14.39 %</td></tr><tr><td>Sunday</td><td>8.35 %</td></tr><tr><td rowspan="12">Transactions per month</td><td>January</td><td>6.92 %</td></tr><tr><td>February</td><td>7.72 %</td></tr><tr><td>March</td><td>8.66 %</td></tr><tr><td>April</td><td>7.85 %</td></tr><tr><td>May</td><td>8.61 %</td></tr><tr><td>June</td><td>8.09 %</td></tr><tr><td>July</td><td>7.49 %</td></tr><tr><td>August</td><td>8.22 %</td></tr><tr><td>September</td><td>9.39 %</td></tr><tr><td>October</td><td>12.18 %</td></tr><tr><td>November</td><td>8.54 %</td></tr><tr><td>December</td><td>6.33 %</td></tr></table>

Fig. 2 shows the visiting behavior of subscribers of the A-Card in terms of the number of locations and the number of types of locations that one visits. Nearly 45 % of all users only visit one location, while almost 50 % also only visits one type of location. The visiting behavior of most users is thus quite unilateral. This <sup>fi</sup>nding is not satisfactory, as the city of Antwerp wishes to get people to visit a diverse set of cultural venues. Fig. 3 also con<sup>fi</sup>rms this <sup>fi</sup>nding via the degree distribution for the users and the locations. The degree distribution for the users is clearly skewed. Most users only visit few locations. Its counterpart degree distribution for the locations shows that the same holds, but since only 102 locations are used, the distribution does not demonstrate the same skewness with respect to that of the users.

![](/api/attachments/JY9SJKDV/fulltext/images/60da5d820c65bb474e7805eff314e37c8d77916016d74608e1735b2bef1c0e9f.jpg)  
Fig. 1. Number of users who have collected enough points to cash out (potentials) and number of users who actually cash out their loyalty points.

In conclusion, the city of Antwerp presently has a loyalty card that does not quite reach the objectives as stated in the mission statement. Fig. 4 schematically demonstrates where strategic decisions should be made related to the two above-mentioned problems. In order to achieve active use of the bene<sup>fi</sup>ts of the loyalty card, in the <sup>fi</sup>rst place, users must be encouraged to become active users (cash out their collected points). Secondly, users should be identi<sup>fi</sup>ed in time as likely to become inactive and consequently must be re-engaged (defect). At last, when a user has reached the active status, he should be retained by visiting (diverse) locations (visit locations, diverse locations). This decision-making process can be facilitated by a decision support system. The goal of this sytem is to provide insight into unstructured problems, represented by raw data [45]. These insights should then lead the way to high-quality decisions. In this work, we build a predictive and a descriptive model that will serve as the decision support system. Concretely, the objectives of this study are stated as follows: (1) build a predictive model able to predict which users make use of the bene<sup>fi</sup>ts and which users do not (cash out behavior), (2) build a predictive model able to predict future visiting behavior (visit locations), (3) build a descriptive model able to identify locations frequently visited together (visit diverse locations), (4) build a predictive model able to predict which users are likely to become inactive (defect behavior).

## 3.4. Data mining techniques

Of the top ten algorithms in data mining [46], the relevant ones in this case are C 4.5, Support Vector Machines, AdaBoost, k-nearest neighbor classi<sup>fi</sup>cation, Naive Bayes classi<sup>fi</sup>cation and CART. Regarding the fact that our problem deals with high-dimensional data, tree classi<sup>fi</sup>ers are not very suitable [47]. AdaBoost might over<sup>fi</sup>t the training data in the presence of noise. In the light of big data in both dimensions, knearest neighbor classi<sup>fi</sup>cation does not scale with respect to execution time. Support Vector Machines (SVM) and Naive Bayes classi<sup>fi</sup>ers (NB) are two appropriate choices able to deal with the big dimensions of the data. We wish to state that we do not claim to have used the two best performing classi<sup>fi</sup>cation techniques. We believe, however, that we have selected two appropriate techniques taking into account the speci<sup>fi</sup>cs of this study.

Both models take as input a data set of the following form: $\left( \mathbf { x } _ { i } , y _ { i } \right)$ with $( i = 1 , . . . , n ) , \mathbf { x _ { i } } \in \mathbb { R } ^ { m } , y _ { i } \in \{ - 1 , + 1 \}$ , n the number of data points and m the number of features of each data point. This data set is called the training set. The classi<sup>fi</sup>er builds a predictive model, which is then used to predict y-values of data points in a test set.

![](/api/attachments/JY9SJKDV/fulltext/images/0542e82023377f858392f8d35f16ff95359e5addcee073dd137c2f39769792fe.jpg)

![](/api/attachments/JY9SJKDV/fulltext/images/07fd07f091e0a2beb59434166fa177c66a3c40fa83af79b2db9179e69410b0b0.jpg)  
Fig. 2. Number of locations (left) and number of types of locations (right) visited by users

![](/api/attachments/JY9SJKDV/fulltext/images/6622d10ae1e2aa2c8422cae9a67acf65497fdeb75b20eb7aa0297b3f9f516a7e.jpg)

![](/api/attachments/JY9SJKDV/fulltext/images/d2209e607b247e94d523b340900fcdb2fd9ac8cd6f51df50ec82d5e1615a4f40.jpg)  
Fig. 3. Degree distribution for users (left) and locations (right).

The Naive Bayes (NB) classi<sup>fi</sup>er [48] uses Bayes' rule with naive assumptions to build a predictive model. Bayes' theorem is de<sup>fi</sup>ned as follows:

$$
p (y _ {i} | x _ {i}) = \frac {p (y _ {i}) p (x _ {i} | y _ {i})}{p (x _ {i})}.\tag{1}
$$

Since the denominator is not dependent on the class variable y , it is not taken into account. Then, making use of the naive assumption that the features are mutually conditionally independent, the above equation can be rewritten as follows:

$$
p (y _ {i} | x _ {i}) \propto p (y _ {i}) \prod_ {j = 1} ^ {m} p \left(x _ {i, j} | y _ {i}\right).\tag{2}
$$

Data points from the test set are classi<sup>fi</sup>ed by selecting the class with the highest probability as de<sup>fi</sup>ned in Eq. (2). Despite the naive assumption, the NB classi<sup>fi</sup>er is able to build predictive models in a timeef<sup>fi</sup>cient manner providing competitive results with respect to more advanced classi<sup>fi</sup>ers.

The more complex SVM [49] project data points into a highdimensional feature space with the help of a kernel function. In that space, the SVM looks for a maximal margin hyperplane that optimally separates the data points. This hyperplane takes the following form:

$$
H = \mathbf {w} ^ {T} \mathbf {x} + b = 0,\tag{3}
$$

with w a weight vector for the features of the data points and b a bias. Concretely, the goal for the hyperplane is to maximally separate the data instances of the two distinct classes that are nearest to the hyperplane. These data points are called support vectors. Maximizing this distance leads to higher generalizability and to lower variance. The SVM <sup>fi</sup>nds the hyperplane by solving the following optimization problem:

$$
\min _ {w} \frac {1}{2} \mathbf {w} ^ {T} \mathbf {w} + C \sum_ {i = 1} ^ {n} \xi_ {i},\tag{4}
$$

$$
\text { s.t. } y _ {i} \left(\mathbf {w} ^ {T} \mathbf {x} _ {i} + b\right) \geq 1 - \xi_ {i},\tag{5}
$$

$$
\xi_ {i} \geq 0,\tag{6}
$$

with C a penalty parameter that represents a trade-off between complexity and error rate and $\xi _ { i } ( i = 1 , . . . , n )$ slack variables that allow misclassi<sup>fi</sup>cations. The Linear SVM (L-SVM) uses a linear kernel function to transform the data points, which results in a lower execution time compared to a non-linear-kernel SVM. The L-SVM is also considered more appropriate for large dimensional datasets [50]. We use L2-regularization and thus the loss function is de<sup>fi</sup>ned as follows:

$$
L (\boldsymbol {\xi} _ {i}) = \max \left(0, 1 - y _ {i} \mathbf {w} ^ {T} \mathbf {x} _ {i}\right) ^ {2}.\tag{7}
$$

L2 regularization is chosen here due to the nature of the features i.e. <sup>fi</sup>ne-grained and low redundant. Predictions are now made by the L-SVM by determining the side of the hyperplane the test points are. Although faster than the non-linear variant, the L-SVM runs slower than the Naive Bayes classi<sup>fi</sup>er.

![](/api/attachments/JY9SJKDV/fulltext/images/3d93cf8d38983a19ea7dd6d416b56140b9a888d929d0bdc844bab8949e0106f6.jpg)  
Fig. 4. Schematic overview of where predictive models can help to get people in, retain them in and prevent them from leaving the active set of users.

In trying to identify locations frequently visited together, the wellknown and widely used Apriori algorithm is used [51]. The algorithm looks for frequent item sets in a transactional database, where a transaction equals a collection of items such as items bought together or applied to our case, locations visited together. Then, the algorithm <sup>fi</sup>nds rules of the form $X  Y ,$ with X and Y item sets. Two constraints are used while looking for these item sets and rules. The <sup>fi</sup>rst is the support of an item set, support(X), and is de<sup>fi</sup>ned as the ratio of transactions containing the items in X. The con<sup>fi</sup>dence of a rule, confidence(X → Y), is de<sup>fi</sup>ned as support(X ∪ Y)/support(X) and represents the strength with which one can state that if X is present also Y is present in a transaction.

## 3.5. Evaluation criteria

Accuracy is a fairly intuitive measure of performance: it expresses the percentage of correctly predicted instances, i.e. the ratio of true positives and true negatives. However, this measure is known to be in<sup>fl</sup>uenced by class imbalance [52]. If 1 positive case occurs in a set of 100 instances, a model predicting all instances as negative has an accuracy of 99 %, despite the fact that the model does not make use of any information in the data. Accuracy can thus not be used as conclusive evidence regarding the model's performance. Therefore, the AUC measure is used to determine the predictive performance of the models: the Area Under Receiving Operator Curve [53]. This measure is insensitive to class imbalance. The AUC expresses the ability of the model to rank the instances in a descending fashion in terms of their prediction score and thus represents the probability of a classi<sup>fi</sup>er to rank a randomly chosen positive instance higher than a randomly chosen negative instance. An AUC of 50 % corresponds to a model performing no better than random.

The problem environment, being the public management area, implies that not only predictive power is important, an insight into the predictions made by the model also is relevant. Therefore, confusion matrices for the test sets are derived. A confusion matrix is a $1 2 \times 2 \cdot$ matrix of which Table 2 shows the form. The confusion matrix shows the possible classi<sup>fi</sup>cations of instances in a test set. A positive instance is preferably classi<sup>fi</sup>ed as positive (TP), otherwise it is referred to as a false negative (FN). Analogous for the negative test instances, when correctly classi<sup>fi</sup>ed, the instance is referred to as a true negative (TN), otherwise it is called a false positive (FP). A good model preferably has a large amount of true positives and true negatives, but a trade-off is inherently present.

When comparing the AUC results achieved for each technique and for all datasets, a statistical signi<sup>fi</sup>cance test has to be used to ascertain whether the difference in performance results is signi<sup>fi</sup>cant. We employ tenfold cross-validation, thus the AUCs are stabilized over different runs of the algorithms. The Wilcoxon signed rank test [54] is then used to compare the performance of two classi<sup>fi</sup>ers. As we project spatial behavior onto spatio-temporal behavior, more detailed analyses are needed for which the Friedman test is used followed by the Nemenyi post-hoc test [54]. For further detail regarding these statistical signi<sup>fi</sup>cance tests, we refer to Demšar's work [54].

## 4. Experimental set-up

## 4.1. Data set

Two choices are made when transforming the transactional dataset into a behavioral dataset. Modeling users' visiting behavior can be done using the frequency of the visits or a weighted frequency measure. However, the choice was made to build binary matrices, omitting any frequency information. If this would not lead to good predictions, subsequently frequency information can be included. A second choice concerns the decision related to the time period along which user

$$
\begin{array}{c c c c} \text {Table 2} & & \\ \text {Confusion matrix.} & & \\ & & \text {True class} \\ & & + & - \\ \text {Predicted class} & + & \text {True Positive} & \text {False Positive} \\ & - & \text {False Negative} & \text {True Negative} \end{array}
$$

behavior is observed. It is assumed that the longer one goes back in time, the more irrelevant that action becomes in the present. Imagine a location visited as a child and how irrelevant it would be to use it to predict the next location visited by the same person as an adult. Concretely, we <sup>fi</sup>rst transform the transactional data set into a sparse behavioral binary input matrix. The matrix is sparse due to the limited behavioral capital [21]. This denotes the fact that there are only so much actions a person can take from the entire set of possible actions. This matrix X is a n × m-matrix with n the number of users (177,761) and m the number of features, here locations (102). Each element $x _ { i , j }$ is de<sup>fi</sup>ned as follows:

$$
x _ {i, j} = \left\{ \begin{array}{l l} 0: & \text {user i has not visited location j in a certain time period t}, \\ 1: & \text {user i has visited location j in a certain time period t}. \end{array} \right.\tag{8}
$$

Since a student will probably visit locations during off-school hours while an unemployed user may visit venues during work hours, it is apparent that the time of day when people visit locations can be informative when trying to make predictions. Since more behavioral features lead to better predictive results [21], breaking down mere spatial behavioral information into spatio-temporal behavioral information might result in more sound predictions. Hence, in a second set of <sup>fi</sup>ner grained behavioral data matrices, different time dimensions are taken into account. With increasing granularity, these are:

• Whether the location was visited during work hours (from 08.00 to 17.00 on Monday until Friday),

• Whether the location was visited during school hours (from 08.30 to 16.00 on Monday, Tuesday, Thursday and Friday and from 08.30 to 12.00 on Wednesday),

• Whether the location was visited in the week or the weekend,

• What day of the week the location was visited,

• During which hour of the day the location was visited.

Table 3 shows an example of a binary behavioral input matrix and its projection in terms of the week granularity level. One binary behavioral feature is projected onto seven-day variables.

## 4.2. Predicting target variables

Regarding the second choice to be made with respect to transforming the transactional dataset into a behavioral one, we state that the underlying premise of this study encompasses the fact that past behavior is predictive for future behavior [55,56]. However, since a person changes over time, the further one goes back in time, the less relevant this behavior is for the person he is now. Hence, we include the visiting behavior of users only from the past year. More concretely, we use the visiting behavior of users from January to September and make predictions regarding their cash out, visit and defect behavior for the period of October to December. Concretely, a user is labeled as cashing out points or visiting a location, if he cashes out points or visits that location in the period from October to December (Fig. 5).

Table 3  
Example of a binary behavioral input matrix and its projection onto the temporal behavioral variant using the week granularity level. One binary behavioral feature is projected onto seven day variables. Ann's visit to the Permeke library in the binary variant is projected onto more detail in the week variant, i.e. Ann visited the library on both Monday and Tuesday.

<table><tr><td></td><td>Permeke library</td><td>MAS museum</td><td>...</td></tr><tr><td>Ann</td><td>1</td><td>0</td><td>...</td></tr><tr><td>Bill</td><td>0</td><td>1</td><td>...</td></tr></table>

<table><tr><td></td><td>Permeke (Monday)</td><td>Permeke (Tuesday)</td><td>...</td><td>Permeke (Sunday)</td><td>MAS (Monday)</td><td>...</td></tr><tr><td>Ann</td><td>1</td><td>1</td><td>...</td><td>0</td><td>0</td><td>...</td></tr><tr><td>Bill</td><td>0</td><td>0</td><td>...</td><td>0</td><td>1</td><td>...</td></tr></table>

Regarding location prediction, <sup>fi</sup>ve locations are selected for which to predict whether a user will frequent it i.e. the Permeke library, the Wezenberg swimming pool, the museum MAS, the Roma cultural center and the Zoo of Antwerp. In this way, we believe we have a diverse set of types of locations that are also visited on different scales by different sets of users. The Permeke library and the Wezenberg swimming pool are the most visited locations: i.e. 13.97 % and 7.35 % respectively of all transactions involve these venues. The Permeke library and the MAS museum are the top two locations when it comes to the number of unique visitors, i.e. 32.70 % and 19.14 %. In order to check the predictive value for locations not that frequently visited, also the Zoo and the Roma cultural center are included.

For the case of predicting whether a person will become inactive, a user is labeled as such in an adaptive fashion. This seems an intuitive approach considering that some people might visit the library every week and others might lend books only once every three months. While one month might be too long a period to wait for the <sup>fi</sup>rst user, sending re-activation e-mails after one month of inactivity might be perceived annoying by the second user. Fig. 6 shows the number of users that, after a certain period of inactivity (shown along the x-axis), become active again. As can be seen, there are users becoming active again after a period of 125 days (approximately three months) of being inactive. Therefore, for each user, his/her average period of inactivity is used to determine whether he/she is likely to become inactive. The prediction is thus tailored to each individual user and his visiting behavior. Considering Fig. 6, a period of three months for determining whether a user is going to churn is too short. Therefore, the target variable must be determined over a longer period. We opt for a period of six months. A second factor to deal with consists of the action weeks. Considering that users are then persuaded to use their card more frequently, the prediction might be biased. Thus we choose the six months preceding these two weeks: from May until October 2013. The prediction is then based on the visiting behavior in the year preceding this period: from April 2012 to April 2013.

## 4.3. Set-up of the data mining techniques

We use tenfold cross-validation when evaluating the predictive techniques. The data set is randomly divided in 90 % training set to build the predictive model, which is subsequently tested on the remaining 10 % of the data set. This procedure is then performed ten times in order to obtain rigor in our evaluation and to not over<sup>fi</sup>t the model to a particular training set [57]. We report the average performance results of these runs. From the training set, a 10 % validation set is derived to tune the C parameter of the Linear SVM, based on the best AUC value.

The majority of the data sets demonstrate class imbalance as can be seen in Table 4. Some of these high class imbalances lead to poor classi-<sup>fi</sup>cation performance when using the L-SVM. In that case, the decision boundary is biased towards the minority class, which results in a high number of false negatives and a lower classi<sup>fi</sup>er performance. Solutions to this problem include undersampling and oversampling [58]. When randomly undersampling the majority class of the data set, information loss might occur. Here, we randomly oversample the minority class. The multivariate Naive Bayes implementation tailored to big data is used [21]. For the L-SVM, the LIBLINEAR-library is used [50].

## 5. Experimental results

The results obtained by the predictive models are presented in Table 5. In short, future visiting behavior, the visiting behavior of users that cash out collected points, and the visiting behavior of users that will defect, can be modeled in an accurate manner and hence these target variables are quite predictable. An evaluation of statistical significance of the results along three dimensions is now performed i.e. between the techniques, between the time granularity levels of the behavioral data and the nature of the prediction (whether future visiting behavior versus loyalty and defect behavior is predicted). We perform the Wilcoxon test when comparing the Naive Bayes classi<sup>fi</sup>er and the L-SVM over all datasets and over the two types of predictions. The Friedman test is used when de<sup>fi</sup>ning whether a signi<sup>fi</sup>cant difference exists over the six time dimensions. We present the following statistically signi<sup>fi</sup>cant results:

• When comparing the performance results over all datasets and over all time granularities. the Naive Baves classifier performs best with a z-value of − 3.59 at the α = 0.05 signi<sup>fi</sup>cance level (Wilcoxon). As the datasets have diverse time level characteristics and distinct predictive purposes (location vs. loyalty and defection), this result is investigated in more detail.

• When comparing the results for the non-temporal datasets, the Naive Bayes classi<sup>fi</sup>er performs better due to a T-value of 0 that is smaller than the critical Wilcoxon value at the α = 0.05 con<sup>fi</sup>dence level.

• When using the Linear SVM technique, the use of hourly data performs better than the use of non-temporal data and better than the time levels of work, school and weekend with a critical difference value of 2.85 from the Nemenyi post-hoc test. There is no signi<sup>fi</sup>cant difference between the non-temporal variant on the one hand and the work, school and weekend variants on the other when employing the L-SVM technique. Also, no signi<sup>fi</sup>cant difference was found between the hour level and the weekday level.

![](/api/attachments/JY9SJKDV/fulltext/images/652bfaf4e78fe21be7ffaaeab2962fffd99f5b7c61e951bf43905d97c595f8df.jpg)  
Fig. 5. Visualization of the predictive modeling procedure.

![](/api/attachments/JY9SJKDV/fulltext/images/5dc81dd26db0c1e376b4941b0eaf3f1300d4ac63bb3ec5cf325e04f320e59802.jpg)  
Fig. 6. Number of active users after inactive period.

• When performing loyalty or defect prediction, the use of the Naive Bayes classi<sup>fi</sup>er performs better than the use of the L-SVM with a zvalue of − 2.90 at the α = 0.05 con<sup>fi</sup>dence level (Wilcoxon).

• When performing location prediction, the NB classi<sup>fi</sup>er performs best with non-temporal data, while the L-SVM performs better with behavioral data on an hourly level, both at the α = 0.05 con<sup>fi</sup>dence level with a zero T-value.

Overall, the NB classi<sup>fi</sup>er performs best except for location prediction on an hourly time level. Independent of the type of prediction, i.e. whether it concerns location prediction or loyalty or defect prediction, it is apparent that adding <sup>fi</sup>ner-grained behavioral data in terms of hourly behavior contributes to a higher performance when employing the L-SVM. When performing loyalty or defect prediction, the behavior of the users is best modeled by the NB classi<sup>fi</sup>er for all time levels. This might originate from the fact that no dependence is relevant between the features when modeling behavior of users cashing out or defecting. For location prediction, the NB classi<sup>fi</sup>er performs better when using non-temporal data and the L-SVM performs better in case hourly data is used. The hourly level seems to add the most useful information with respect to the other time granularities.

It may seem obvious that high AUC values are obtained in the case of location prediction: predicting whether a user will visit a location X in the future is probably largely based on whether or not the user visited that location in the past. However, when looking at the top ten weights of the features determined by the L-SVM (Table 6) for the Permeke library and the MAS museum, it is apparent that the information not only comes from visiting the location under consideration.

Table 4  
Imbalance of the datasets for the considered target variables.

<table><tr><td>Data set</td><td>% of positive cases</td></tr><tr><td>Museum MAS</td><td>1.82 %</td></tr><tr><td>Roma cultural center</td><td>0.96 %</td></tr><tr><td>Permeke library</td><td>7.29 %</td></tr><tr><td>Zoo</td><td>0.85 %</td></tr><tr><td>Wezenberg swimming pool</td><td>2.18 %</td></tr><tr><td>Cash out</td><td>6.71 %</td></tr><tr><td>Defect</td><td>13.20 %</td></tr></table>

In order to get a more intuitive insight into the quality of the predictions made by the models, confusion matrices are shown in Table 7. These result from predictions made by the best performing model on the highest behavioral granularity level (L-SVM for location prediction, NB for loyalty and defect prediction). Regarding location prediction, wrongly labeling a user as likely to visit a certain venue, might be disturbing for users if future communication is based on this fact. The same holds for persons that are labeled as likely to defect, while they are not planning on becoming inactive. Targeting these users with reactivation e-mails might be perceived annoying and in the extreme case might result in judicial actions. It is apparent that the number of false positives must be reduced in these cases. The false positives ratio in Table 7 for the location prediction models is located in a small interval around 11 %. For the defect target variable this ratio amounts to 15.49 %. The ratio of false negatives is ‘lost’ customers that are not targeted. This trade-off seems fair since a low ratio of false positives is considered a priority in this public management setting. Regarding cash out prediction, the false negative ratio is of importance, since these are the users that are wrongly labeled as not cashing out. Communicating with these users in function of convincing them to cash out might result in annoyance and potentially in lost active users. As can be seen in Table 7, this ratio only amounts to 8.29 %. The false positive ratio here is relatively higher i.e. almost 20 % of non-active users might be lost since no targeting campaign includes them in persuading them to become active. At <sup>fi</sup>rst sight, this does not comply with our previously stated goal of attempting to increase the active user base. However, a tradeoff has to be made between the public character of the decision support process on the one hand (a government spamming its citizens is not desirable) and the increase of the active user base on the other. We believe this trade-off has been taken into account in the presented results.

Table 8 shows the results from applying the Apriori algorithm with a support of 0.02 and a con<sup>fi</sup>dence value of 0.6. This means that the item sets present in the rules only occur in 2 % of the transactions and that for these transactions the rule holds in 60 % of the cases. The reason for the low support originates from the majority of users only visiting one location, as is seen in Fig. 2. This leads to a smaller pool of possible frequent item sets and thus to a lower support. The highest con<sup>fi</sup>dence that is gained for association rules in this dataset is 0.7. Taking into account the fact that close to 50 % of all transactions consist of one item, the achieved con<sup>fi</sup>dence for these rules seems acceptable. As the active user base increases along with the number of venues that support the A-Card, and subsequently the number of users frequenting two or more locations increases, the association rules can become stronger and more diverse.

Table 5  
Predictive performance of the models in terms of AUC (highest achieved performance in boldface).

<table><tr><td rowspan="2">Target variables</td><td colspan="6">Naive Bayes</td><td colspan="6">Linear SVM</td></tr><tr><td>Non-temporal</td><td>Hour</td><td>Weekday</td><td>Weekend</td><td>Work</td><td>School</td><td>Non-temporal</td><td>Hour</td><td>Weekday</td><td>Weekend</td><td>Work</td><td>School</td></tr><tr><td>Permeke library</td><td>85.60</td><td>83.85</td><td>83.85</td><td>83.17</td><td>83.40</td><td>83.47</td><td>83.42</td><td>85.51</td><td>84.77</td><td>83.64</td><td>83.52</td><td>83.83</td></tr><tr><td>Wezenberg swimming pool</td><td>88.52</td><td>88.10</td><td>88.30</td><td>88.21</td><td>88.43</td><td>88.43</td><td>86.75</td><td>90.69</td><td>88.51</td><td>86.89</td><td>86.17</td><td>86.70</td></tr><tr><td>Museum MAS</td><td>78.97</td><td>78.50</td><td>78.75</td><td>79.10</td><td>78.97</td><td>79.02</td><td>75.05</td><td>81.56</td><td>78.58</td><td>73.91</td><td>73.76</td><td>74.23</td></tr><tr><td>Cultural center Roma</td><td>89.19</td><td>88.87</td><td>88.98</td><td>89.19</td><td>89.20</td><td>89.18</td><td>83.61</td><td>91.33</td><td>88.51</td><td>81.77</td><td>81.70</td><td>81.83</td></tr><tr><td>Zoo</td><td>88.57</td><td>88.52</td><td>88.77</td><td>89.05</td><td>88.87</td><td>88.94</td><td>83.26</td><td>91.97</td><td>90.04</td><td>81.72</td><td>81.27</td><td>81.51</td></tr><tr><td>Cash out</td><td>89.08</td><td>92.50</td><td>91.9</td><td>90.28</td><td>90.50</td><td>90.68</td><td>87.58</td><td>92.36</td><td>91.55</td><td>87.91</td><td>89.11</td><td>89.26</td></tr><tr><td>Defect</td><td>82.66</td><td>85.50</td><td>85.14</td><td>81.35</td><td>81.60</td><td>81.53</td><td>82.82</td><td>83.73</td><td>83.71</td><td>79.53</td><td>79.67</td><td>79.51</td></tr></table>

## 6. Conclusion and future work

## 6.1. Conclusion

CRM applications in the public area mostly consist of simplifying citizen access to government's services. In the past, the public sector has shown a habit of adopting business-like practices. Notwithstanding obvious resemblances between both sectors, their rationale clearly is different. Private companies operate from a pro<sup>fi</sup>t point of view, while governments need to take into account all citizens. We believe the research conducted in this study contributes to the gap existing in CRM-applications in the public sector.

This design science research paper presented a data mining analysis of spatio-temporal behavioral data of users of a government loyalty card of the city of Antwerp (Belgium). The mission of the A-Card mainly consists of promoting participation in cultural activities offered by the city. While analyzing the data, it was found that the bulk of the card users did not actively use their card and that the set of locations visited was not very diverse.

The result of the study is a decision support system in the form of a predictive model which is capable of distinguishing between different visiting behaviors of the loyalty card users. Concretely, we are now able to predict whether a user will make use of his received rewards, whether a user will visit a certain location, and whether a user is likely to become inactive in some time in the near future. The data consists of a transformation of transactional data into <sup>fi</sup>ne-grained spatio-temporal behavioral data. For location prediction ends, the best predictive model is the L-SVM. For cash out and defect prediction, the Naive Bayes classi<sup>fi</sup>er performs best. These results are achieved in case the behavioral data is projected onto <sup>fi</sup>ner-grained hourly visiting behavior, which is the highest granular behavioral level.

## 6.2. Contributions

The novelty of this research does not lie in one particular element such as the data or the used method. The innovation comes from a diverse interplay of different elements. First of all, the data is found in an atypical context: loyalty card data mostly originates from the private sector. More importantly, this transactional data has been transformed to <sup>fi</sup>ne-grained behavioral data in the form of spatiotemporal behavioral data. The results gained from this projection hint that the larger the number of features available to model a person's behavior, the better the predictions that can be made. It is highly probable that if the set of cultural venues is extended or the time granularity increased or extra behavioral information added, that even better predictions can be made. Also, as the user base grows, more data instances could also improve the predictive performance of the models. These <sup>fi</sup>ndings correspond to the results described in [21].

Table 6  
Top ten feature-weights for two location prediction variables.

<table><tr><td>Permeke library</td><td>Museum MAS</td></tr><tr><td>Cultural Center Ekeren</td><td>Youth - Teenage offer</td></tr><tr><td>Museum Middelheim</td><td>Museum Mayer van den Bergh</td></tr><tr><td>Antwerp Sport Event</td><td>CC Luchtbal theatre</td></tr><tr><td>Cultural Center De Schelde</td><td>Digipoint</td></tr><tr><td>Meeting Center Merksemdok</td><td>Museum Rubens</td></tr><tr><td>Library Luchtbal</td><td>Topvolley</td></tr><tr><td>Museum Vleeshuis</td><td>Ecohouse</td></tr><tr><td>Swimming pool De Molen</td><td>Swimming pool IJspiste</td></tr><tr><td>Permeke library</td><td>Museum Plantin-Moretus</td></tr><tr><td>Swimming pool De Schinde</td><td>Library Elsschot</td></tr></table>

Concretely, as a theoretical contribution, we state that an increase in levels when modeling a person's behavior, in this case temporal levels, results in better predictions. As a second theoretical contribution, we have demonstrated the need for more diverse CRM-related data research in a government context. Further privatization of public institutions, along with the presence of a vast amount of data available to these institutions, will lead to a growing need for research of private-like decision-support systems in a public setting.

We state our second contribution as a practical one. The city of Antwerp, along with other organizations disposing of this kind of data, is now able to predict loyalty behavior, defect behavior and future visiting behavior based solely on past visiting behavior of their users. This should capacitate them to proactively change the behavior of their citizens. The interventions can be made at four points with the goal of increasing the active user base (visualized in Fig. 4). First, since users can now be identi<sup>fi</sup>ed as active or not, the non-active users can be targeted using their preferences or using information regarding their visiting behavior. Personalizing communication and offers might convince these users to actively use their card. Second, when users have joined the active customer base, the city wants them to stay there. This can be done by tailoring communications and/or bene<sup>fi</sup>ts to locations that users will visit in the future, but also by surprising them with relevant suggestions regarding other venues. Getting users to visit other locations then works self-reinforcing as more users visit more different places and more relevant suggestions can be made. Third, the city wishes to minimize the <sup>fl</sup>ow of users leaving the active user base. The designed decision support system is capable of identifying likely future defectors, and thus the city can intervene in time. This can be done by offering tailored bene<sup>fi</sup>ts based on preferences or previous visiting behavior. Since the problem of the low active user base might be rooted elsewhere. first a general survey might be conducted with the goal of <sup>fi</sup>nding out if and to what extent users are fully aware of the bene<sup>fi</sup>ts offered by the loyalty card. Moreover, the nature of the loyalty bene<sup>fi</sup>ts might be investigated. It was mentioned by the city of Antwerp that these bene<sup>fi</sup>ts might not be convincing enough for some users. For users frequently going to the swimming pool, the collected points can be used as free entrance ticket, whereas the bene<sup>fi</sup>ts for people wanting to cash out their points in a library or a cultural center are not that straightforward.

Table 8  
Table 7  
Confusion matrices for the target variables as resulting from their best predictive model.

<table><tr><td colspan="3">Permeke library</td><td colspan="3">Wezenberg swimming pool</td><td colspan="3">Museum MAS</td><td colspan="3">Cultural center Roma</td></tr><tr><td></td><td>+</td><td>-</td><td></td><td>+</td><td>-</td><td></td><td>+</td><td>-</td><td></td><td>+</td><td>-</td></tr><tr><td>+</td><td>74.5</td><td>11.85</td><td>+</td><td>75.6</td><td>11.12</td><td>+</td><td>70.2</td><td>11.09</td><td>+</td><td>71.3</td><td>11.25</td></tr><tr><td>-</td><td>25.5</td><td>88.15</td><td>-</td><td>24.4</td><td>88.88</td><td>-</td><td>29.8</td><td>88.91</td><td>-</td><td>28.7</td><td>88.75</td></tr><tr><td rowspan="4" colspan="3"></td><td colspan="3">Zoo</td><td colspan="3">Cashout</td><td colspan="3">Defect</td></tr><tr><td>+</td><td>-</td><td>+</td><td>-</td><td>+</td><td>-</td><td>+</td><td>-</td><td>-</td></tr><tr><td>+</td><td>72.1</td><td>10.59</td><td>+</td><td>91.7</td><td>19.55</td><td>+</td><td>72.9</td><td>15.49</td></tr><tr><td>-</td><td>27.9</td><td>89.41</td><td>-</td><td>8.29</td><td>80.45</td><td>-</td><td>27.1</td><td>84.51</td></tr></table>

## 6.3. Limitations of our study

One of the main limitations of our study consists of the fact that we only perform this analysis in one city. We cannot claim that the results are generalizable to cultural loyalty programs of other cities. Further data collection in this context is necessary. Subsequently, this data must be thoroughly analyzed and only then can conclusions be made as to whether these results hold in general. Second, the locations that are recognized by the A-Card are limited to cultural venues. Whether the conclusions will hold for cards supporting other types of locations such as docking stations for bike rental or other non-cultural public areas, can only be ascertained if more data is available and subsequently analyzed. Obviously, since bigger is better, having more data instances and more dimensions to our disposal, would also greatly bene<sup>fi</sup>t the study. A third limitation of our study is related to location prediction. We have evaluated the predictive performance of our models on <sup>fi</sup>ve locations out of the total of 102 locations. As doing the analysis for all locations would be more valid when formulating conclusions, it would also be too elaborate to discuss in a research paper and moreover, in the event that more features are added, not feasible. We have therefore selected <sup>fi</sup>ve locations which demonstrate distinct characteristics such that their results can be extrapolated to the remaining locations.

## 6.4. Avenues for further research

The opportunities for further research at the government-CRM intersection are vast. With respect to the A-Card or other cultural loyalty cards, we believe that in time, the vast behavioral data can be used to customize to a large extent the city's cultural offer to its citizens' preferences. In particular in this research, we have focused on loyalty cards in the context of cultural venues. More generally, there can be a diverse array of other behavioral CRM data in the public sector. Illustrations of these entail city cards for tourists, bike rental cards or public transportation cards. In time, these different research avenues with respect to user-de<sup>fi</sup>ning behavioral data could lead to the consolidation of all this data, which could in turn lead to more sound and more diverse predictions. Furthermore, projecting this vast and diverse amount of information onto an even more <sup>fi</sup>ne-grained temporal level, might lead to stunning results. Investigating whether dimensions other than temporal levels lead to equally good or better results, might also lead to interesting conclusions. Making strong predictions about users and reacting in an adequate fashion may lead to higher citizen satisfaction, which in turn may bene<sup>fi</sup>t the community as a whole. More broadly, these results may lead to the introduction of CRM in other public institutions and to subsequent government-tailored analyses of these data.

Association rules resulting from the Apriori algorithm.

<table><tr><td>X →</td><td>Y</td><td>Confidence</td></tr><tr><td>Swimming pool Sportoase</td><td>Permeke library</td><td>0.6</td></tr><tr><td>Cultural center Roma</td><td>Museum MAS</td><td>0.6</td></tr><tr><td>Museum Middelheim</td><td>Museum MAS</td><td>0.6</td></tr><tr><td>Permeke library and City shop</td><td>Museum MAS</td><td>0.6</td></tr><tr><td>Museum Plantin-Moretus</td><td>Museum MAS</td><td>0.6</td></tr><tr><td>Kaeck library</td><td>Bist library</td><td>0.6</td></tr><tr><td>Ecohouse</td><td>Permeke library</td><td>0.6</td></tr><tr><td>Meeting center Atlas</td><td>Permeke library</td><td>0.7</td></tr><tr><td>Museum MAS and Swimming pool Sportoase</td><td>Permeke library</td><td>0.7</td></tr></table>

## Acknowledgments

We would like to thank the city of Antwerp for letting us use the data set of the A-card and for their valuable input.

## References

[1] W. Reinartz, M. Krafft, W.D. Hoyer, The customer relationship management process: its measurement and impact on performance, Journal of Marketing Research 41 (3) (2004) 293–305.

[2] S.-L. Pan, C.-W. Tan, E.T. Lim, Customer relationship management (CRM) in egovernment: a relational perspective, Decision Support Systems 42 (1) (2006) 237–250.

[3] D.L. Goodhue, B.H. Wixom, H.J. Watson, Realizing business bene<sup>fi</sup>ts through CRM: hitting the right target in the right way, MIS Quarterly Executive 1 (2) (2002) 79–94.

[4] G. R. Dowling, M. Uncles, Do customer loyalty programs really work?, Research Brief 1.

[5] S. Lessmann, S. Voß, A reference model for customer-centric data mining with support vector machines, European Journal of Operational Research 199 (2) (2009) 520–530.

[6] C. Mauri, Card loyalty. A new emerging issue in grocery retailing, Journal of Retailing and Consumer Services 10 (1) (2003) 13–25.

[7] B. Berman, Developing an effective customer loyalty program, California Management Review 49 (1) (2006) 123.

[8] E.W. Ngai, L. Xiu, D.C. Chau, Application of data mining techniques in customer relationship management: a literature review and classi<sup>fi</sup>cation, Expert Systems with Applications 36 (2) (2009) 2592–2602.

[9] R.H. von Alan, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[10] E. Garbarino, M.S. Johnson, The different roles of satisfaction, trust, and commitment in customer relationships, The Journal of Marketing (1999) 70–87.

[11] A.S. Dick K. Basu, Customer lovalty: toward an integrated conceptual framework Journal of the Academy of Marketing Science 22 (2) (1994) 99–113.

[12] S. Lessmann, S. Voß, A reference model for customer-centric data mining with support vector machines, European Journal of Operational Research 199 (2) (2009) 520–530.

[13] A. Jacobs, The pathologies of big data, Communications of the ACM 52 (8) (2009) 36–44.

[14] D. Boyd, K. Crawford, Critical questions for big data: provocations for a cultural, technological, and scholarly phenomenon, Information, Communication and Society 15 (5) (2012) 662–679.

[15] J. Liu, P. Dolan, E.R. Pedersen, Personalized news recommendation based on click behavior, Proceedings of the 15th International Conference on Intelligent User Interfaces, ACM 2010, pp. 31–40

[16] D. Martens, F. Provost, Pseudo-social network targeting from consumer transaction data.

[17] K. Li, T.C. Du, Building a targeted mobile advertising system for location-based services, Decision Support Systems 54 (1) (2012) 1–8.

[18] T. Fawcett, F. Provost, Adaptive fraud detection, Data Mining and Knowledge Discovery 1 (3) (1997) 291–316.

[19] E. Junqué de Fortuny, M. Stankova, J. Moeyersoms, B. Minnaert, F. Provost, D. Martens, Corporate residence fraud detection, Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM 2014, pp. 1650–1659.

[20] L. Yu, H. Liu, Feature Selection for High-dimensional Data: A Fast Correlation-based Filter Solution, ICML, vol. 3 2003, pp. 856–863.

[21] E. Junqué de Fortuny, D. Martens, F. Provost, Predictive modeling with big data: is bigger really better? Big Data 1. (4) (2013) 215–226

[22] C. Rygielski, J.-C. Wang, D.C. Yen, Data mining techniques for customer relationship management, Technology in Society 24 (4) (2002) 483–502.

[23] P.R. Devadoss, S.L. Pan, J.C. Huang, Structurational analysis of e-government initiatives: a case study of SCO, Decision Support Systems 34 (3) (2003) 253–269.

[24] M.S. Haque, The diminishing publicness of public service under the current mode of governance, Public Administration Review 61 (1) (2001) 65–82.

[25] D. Dufner, L.M. Holley, B. Reed, Can private sector strategic information systems planning techniques work for the public sector? Communications of the Association for Information Systems 8 (1) (2002) 28.

[26] C.G. Reddick, The adoption of centralized customer service systems: a survey of local governments Government Information Ouarterly 26 (1) (2009) 219–226

[27] R.P. Lourenço, J.P. Costa, Incorporating citizens' views in local policy decision making processes Decision Support Systems 43 (4) (2007) 1499–1511

[28] H. Chen, J. Schroeder, R.V. Hauck, L. Ridgeway, H. Atabakhsh, H. Gupta, C. Boarman, K. Rasmussen, A.W. Clements, COPLINK connect: information and knowledge management for law enforcement, Decision Support Systems 34 (3) (2003) 271–285.

[29] J.C. Bertot, P.T. Jaeger, J.M. Grimes, Using ICTs to create a culture of transparency: Egovernment and social media as openness and anti-corruption tools for societies, Government Information Quarterly 27 (3) (2010) 264–271.

[30] H. Chen, R.H. Chiang, V.C. Storey, Business intelligence and analytics: from big data to big impact, MIS Quarterly 36 (4) (2012) 1165–1188

[31] G.A. Boyne, Public and private management: what's the difference? Journal of Management Studies 39 (1) (2002) 97–122.

[32] J. Rowley, E-government stakeholders — who are they and what do they want? International Journal of Information Management 31 (1) (2011) 53–62.

[33] F. H. Cate, Government data mining: The need for a legal framework, Harvard Civil Rights-Civil Liberties Law Review (CR-CL) 43 (2).

[34] S.F. King, Citizens as customers: exploring the future of CRM in UK local government, Government Information Quarterly 24 (1) (2007) 47–63.

[35] A. Schellong, in: Peter Lang (Ed.)Citizen Relationship Management: A Study of CRM in Government, vol. 560, 2008.

[36] M. Raus, J. Liu, A. Kipp, Evaluating IT innovations in a business-to-government context: a framework and its applications, Government Information Quarterly 27 (2) (2010) 122–133.

[37] S. Bretschneider, Management information systems in public and private organizations: an empirical test, Public Administration Review (1990) 536–545.

[38] W. Cats-Baril, R. Thompson, Managing information technology projects in the public sector, Public Administration Review (1995) 559–566.

[39] P.S. Ring, J.L. Perry, Strategic management in public and private organizations: implications of distinctive contexts and constraints, Academy of Management Review 10 (2) (1985) 276–286.

[40] F. Provost, Geo-social targeting for privacy-friendly mobile advertising: Position paper.

[41] M.S. Jeannotte, Singing alone? The contribution of cultural capital to social cohesion and sustainable communities, The International Journal of Cultural Policy 9 (1) (2003) 35–49.

[42] Federal Public Service (FOD) Economics Belgium, The Belgian Provinces 2001, Statistics Belgium2014

[43] City of Antwerp, Minutes of ‘College van Burgemeester en Schepen’, http:// notulus.antwerpen.be/rs-bin/RightSite.exe/getcontent/C2010-00722 7.pdf? DMW OBIECTID=090f45ab80540dbb DMW FORMAT=pdf fext=.pdf (2011)

[44] S. Vittal, E. Murphy, Benchmarking Customer Loyalty Program Efforts, Forrester, 2012.

[45] R.H. Sprague Jr., A framework for the development of decision support systems, MIS Ouarterly (1980).1-26

[46] X. Wu, V. Kumar, J.R. Quinlan, J. Ghosh, Q. Yang, H. Motoda, G.J. McLachlan, A. Ng, B. Liu, S.Y. Philip, et al., Top 10 algorithms in data mining, Knowledge and Information Systems 14 (1) (2008) 1–37.

[47] T.-N. Do, P. Lenca, S. Lallich, N.-K. Pham, Classifying very-high-dimensional data with random forests of oblique decision trees, Advances in Knowledge Discovery and Management, Springer 2010, pp. 39–55.

[48] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques Morgan Kaufmann, 2005.

[49] C. Cortes, V. Vapnik, Support-vector networks, Machine Learning 20 (3) (1995) 273–297.

[50] R.-E. Fan, K.-W. Chang, C.-J. Hsieh, X.-R. Wang, C.-J. Lin, Liblinear: a library for large linear classi<sup>fi</sup>cation, Journal of Machine Learning Research 9 (2008) 1871–1874.

[51] R. Agrawal, T. Imieliński, A. Swami, Mining association rules between sets of items in large databases, ACM SIGMOD Record, 22, ACM 1993, pp. 207–216.

[52] F.J. Provost, T. Fawcett, R. Kohavi, The case against accuracy estimation for comparing induction algorithms, ICML, vol. 98 1998, pp. 445–453.

[53] T. Fawcett, An introduction to ROC analysis, Pattern Recognition Letters 27 (8) (2006).861-874

[54] J. Demšar, Statistical comparisons of classi<sup>fi</sup>ers over multiple data sets, Journal of Machine Learning Research 7 (2006) 1–30.

[55] K. Coussement, D.V. d. Poel, Improving customer attrition prediction by integrating emotions from client/company interaction emails and evaluating multiple classi-<sup>fi</sup>ers, Expert Systems with Applications 36 (3) (2009) 6127–6134.

[56] S.-Y. Hung, D.C. Yen, H.-Y. Wang, Applying data mining to telecom churn management, Expert Systems with Applications 31 (3) (2006) 515–524.

[57] P. Domingos, A few useful things to know about machine learning, Communications of the ACM 55 (10) (2012) 78–87.

[58] M. Farquad, I. Bose, Preprocessing unbalanced data using support vector machine, Decision Support Systems 53 (1) (2012) 226–233.

So<sup>fi</sup>e De Cnudde is a Ph.D. candidate in the Department of Engineering Management at the Applied Data Mining research group of the University of Antwerp, Belgium. She received a M.S. degree in Computer Science in 2011 and a M.S. degree in Business Economics in 2014 at Ghent University. Her doctoral research is focused on big data analysis for customer analytics. Previous research in the <sup>fi</sup>eld of process mining has appeared in Expert Systems with Applications.

David Martens is an assistant professor at the University of Antwerp, where he heads the Applied Data Mining research group. His research focuses on the development and application of data mining techniques that lead to improved understanding of human behavior, and the use thereof in marketing and finance, His work has been published in high impact journals, such as MIS Quarterly, Machine Learning, Journal of Machine Learning Research, IEEE Transactions on Neural Networks, IEEE Transactions on Knowledge and Data Engineering and IEEE Transactions on Evolutionary Computation. In 2014, David won the Best EJOR Application Award (European Journal of Operational Research) for his work on churn prediction. In 2008 David was a <sup>fi</sup>nalist of the prestigious international KDD doctora dissertation award. Together with prof. Foster Provost, he is an inventor of four pending patent applications on data mining methods
