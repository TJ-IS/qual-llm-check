---
otero_id: 21445
otero_key: "GWJJ6H65"
title: "Decision support for real-time telemarketing operations through Bayesian network learning"
authors: "Jae-Hyeon Ahn; Kazuo J. Ezawa"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00009-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for real-time telemarketing operations through Bayesian network learning $^{1}$

Jae-Hyeon Ahn $^{a,*}$ , Kazuo J. Ezawa $^{b}$

$^{a}$ AT & T Laboratories, Room 7E-530, 600 Mountain Avenue, Murray Hill, NJ 07974, USA $^{b}$ AT & T Laboratories, Room 7E-523, 600 Mountain Avenue, Murray Hill, NJ 07974, USA

## Abstract

Many knowledge discovery systems have been developed in diverse areas, but few systems address the use of knowledge in decision problems explicitly. This paper presents a decision support system for real-time telemarketing operations using the information extracted from the Bayesian network learning model. A prototype decision support system was developed for AT&T customer-contact employees to provide a recommendation regarding the promotion of a telephone discount plan. The system integrated a Bayesian network learning model (knowledge discovery process) and decision-making technique (influence diagram) to provide real-time decision support. A Bayesian network learning model was used to predict a probability of the customer's response from the previous promotion/response history. The influence diagram framework was used to integrate the predicted probability with the cost and benefit related to the possible actions. It was demonstrated that decision support by the Bayesian network learning model itself can be misleading. However, by linking the Bayesian network learning model with rigorous decision-making techniques such as influence diagrams, the decision support system developed in this paper was shown to provide an intelligent decision advice. © 1997 Elsevier Science B.V.

Keywords: Service operations management; Decision support system; Bayesian network learning; Influence diagrams; Telecommunication applications

## 1. Introduction

Modern corporate transactions are increasingly made electronically using information technologies. For example, many operational and financial transactions are made through computer networks. Interactive customer purchases and information gatherings are made through the Internet. Telecommunications service operations are provided through sophisticated computer control. These ubiquitous electronic transactions, especially aided by information technologies, make it increasingly easy to collect and store large volume of customers- and transactions-related data. As corporations amass huge amounts of data from their daily operations, utilization of the collected data becomes an important corporate activity. To provide the most needed services and products to the customers and win the business in the ever-changing market place, it is necessary to understand the data and extract valuable information from them. The extracted information could be used in all stages of corporate activities; from idea generation, product planning and design, to targeted marketing and advertisement.

However, it is a very difficult task to extract information from data as the number of variables and volume of the data become large and interactions among the variables become complex. For example, there are more than 90 million AT&T customers, and for each customer, there are many disjointed customer records in hundreds of databases AT&T currently manages. On top of that, new information is generated every second as streams of electronic information are pumped into the AT&T network by the users. It means that over 200 million new data points are generated every day in the AT&T operations. With this extraordinarily huge amount of data and their complex interrelationships, it is a challenge to understand customers at the proper market segment level, not to mention at the individual customer level. To understand and improve this challenging process, a field known as Knowledge Discovery in Databases (KDD) attracted considerable attention from many diverse fields such as statistics, information technology, machine learning, knowledge-based systems, database management, etc.

KDD is a process of discovering previously unknown patterns in large databases. Also known as data mining in statistics, KDD is a highly interactive and iterative process which includes 1) selection, cleaning, transformation, and projection of data, 2) mining the data to extract patterns, 3) evaluating the patterns to decide what constitutes ‘knowledge,’ 4) consolidating the knowledge, 5) resolving conflicts with previously extracted knowledge, and 6) making the knowledge available for use on the KDD system [7].

Even though many KDD systems were developed for applications in the areas of finance, insurance, marketing, medicine, geology, astronomy, etc. [8], few systems [2,17] address the use of knowledge in the decision-making processes explicitly. Once the knowledge becomes available from the KDD system, patterns or knowledge identified from the KDD process can be used in decision-making processes. Most of the KDD systems developed so far, however, focused on how to discover knowledge but not on how to use it. Therefore, the link between the knowledge discovery process and applications of the discovered knowledge has been either not emphasized or ignored as a different subject. Knowledge is valuable when it is applied appropriately in decision-making processes. In this paper, an attempt was made to link the knowledge discovery process (Bayesian network learning model) and decision-making process. Based on the information extracted from the Bayesian network learning model, a prototype decision support system was developed for real-time telemarketing operations in the telecommunications industry. An influence diagram framework was used as a decision engine or problem processing system in the term used by Bonczek et al. [1] to recommend the best action to take.

## 1.1. Decision support system for telemarketing

AT&T customer-contact employees (CCEs) make several million customer contacts each day. Whenever they make contact with customers relating to billing questions, inquiries, subscription of new services, complaints, etc., they can promote special long-distance telephone services which customers don't have but may like. A telephone discount plan or TDP is one of them. Additionally, in the near future, services such as local services, wireless services, entertainment services, Internet services can be promoted.

A TDP is a plan where telecommunication charges are discounted over the regular rates depending on the customer's calling pattern and usage level. At this time, it is not required for the CCE to offer it to new customers or existing customers who don't have it. However, it is believed that by offering the service they can increase customer satisfaction with the telecommunications provider and improve customer retention. Unfortunately, it is costly to promote it because the CCE has to spend time explaining the characteristics of the plan, how it works, how much money customers can save, etc., sometimes at the expense of other customers waiting on the line to be served. Because there are trade-offs between offering TDP and serving next customers, it is not obvious for the CCE to decide to promote it on a real-time basis at the time of customer contact.

An intelligent decision support system recommending the best action will be useful in this problem, and it will increase the productivity of the CCEs and the profitability of our business. In this analysis, a prototype decision support system for a specific TDP promotion decision was developed. The goal was to maximize the effectiveness of the telemarketing activities by minimizing the time spent on unsuccessful promotion. Theoretically, it can be done by predicting and promoting the TDP only to the people who would subscribe to it. The major problem was the uncertainty related to the customer's response regarding the promotion of the TDP. To predict the probability of rejecting the TDP promotion, a Bayesian network learning model was developed from a preclassified training data set. The training data set had the customers' responses for previous random promotions of the TDP. Then, a decision support system described in this paper provided the best recommendation for the CCE depending on the predicted probability from the Bayesian network model and other factors related to the promotion.

## 2. Bayesian network learning model for probability prediction

To provide intelligent decision support regarding the TDP promotion, it is necessary to predict the customer's response for the TDP offering. An approach would be to predict the customer's response based on the knowledge from previous customer contact results in the databases. To extract good predictors of customer responses, we used a machine learning system called APRI (Advanced Pattern Recognition and Identification) developed at AT&T Bell Laboratories [5]. It extracts knowledge from databases and represents it in the Bayesian network framework. In the following, we provide a brief explanation of the Bayesian network and the APRI system.

## 2.1. Bayesian network

A Bayesian network is a directed acyclic graph where each node represents a random variable and arrows signify the existence of direct causal influences from variables represented by parent nodes [11]. A typical Bayesian network used in our analysis is shown in Fig. 1. In the network, we use a special structure for the purpose of classification and later make a recommendation based on the belief which are updated by the new observations. We denote a node that we are interested in predicting as $\pi$ or by a prime node. Other variables in the model are variables explaining customer profile, which is denoted as $X = (X_{1}, X_{2}, \ldots, X_{n})$ or field nodes. Field nodes are connected depending on the probabilistic relationships between them. Probabilistic information is stored in the form of marginal distribution on the prime node and conditional distributions on the field nodes. Assessing $p(\pi|X)$ directly is often infeasible due to data and storage limitations. However, the conditional probability $p(X|\pi)$ and the marginal probability $p(\pi)$ are easier to assess by analyzing a preclassified training data set. Then, the conditional probability $p(\pi|X)$ can be calculated by applying Bayes' rule.

![](/api/attachments/GWJJ6H65/fulltext/images/d651190c77d89f787efae2c15eb53e19339060515739093f4e35fddfb5c9b941.jpg)  
Fig. 1. A Bayesian network.

Once we develop a Bayesian network, we predict the customer's response for the TDP offering based on the available customer-specific information. Historically, the actual implementation of the Bayesian classifier was infeasible because of the size of the data set. However, recent advances in evidence propagation algorithms [10,13,14,16] and computer hardware allow us to approximate the ideal Bayesian classifier by using Bayesian network models [3,12,18]. For purposes of using APRI for the classification and comparison with other methods, see Ezawa and Schuermann [6].

## 2.2. APRI system

The APRI system was developed primarily for learning Bayesian network models with very large data sets of the telecommunications industry. It is a supervised machine learning system. It uses a heuristic approximation to the full Bayesian classifier in the Bayesian network paradigm using entropy measure (mutual information) to perform variable and dependency selections (See Appendix A for more information). In order to obtain a useful approximation of the full conditional probability structure, the APRI system uses mutual information both for variable selection and dependency selection between each pair of the selected variables. This approach was chosen to reduce training time with special emphasis on limiting repeated reading of the training data, which can be a critical factor for generating large data sets. To select variables and dependencies, it uses two parameters $T_{\pi x}$ and $T_{xx}$ both ranging from 0 to 1. $T_{\pi x}$ is a parameter for the selection of variables (field nodes) and $T_{xx}$ is a parameter for the selection of dependencies between field nodes in the Bayesian network. The two parameters $T_{\pi x}$ and $T_{xx}$ will be iteratively selected by the user to achieve the maximum discrimination power. APRI constructs a graphical Bayesian network model in four steps.

Step 1: APRI parses the input database and characterizes its variables. If the prime node is continuous, APRI first defines the class outcomes either by discretization or kernel density estimation. APRI then scans the database to identify the outcome sets for each variable. For continuous variables, it either estimates the kernel density or information-based discretization.

Step 2: APRI chooses variables to be in the Bayesian network model. The choice is based on the mutual information calculation. If the mutual information between the prime node and any other node or $I(\pi; X_i)$ is zero, then it implies that the variable $X_i$ doesn't help to classify the prime node. On the other hand, $I(\pi; X_i)$ will take higher value if $\pi$ and $X_i$ have a higher functional relationship. From this reasoning, we select variables in the order of the highest mutual information until the sum of the mutual information of the selected variables doesn't exceed $T_{\pi x}$ times the total mutual information.

Step 3: APRI selects the dependencies among the variables selected in step 2. In particular, it computes the conditional mutual information $I(X_i; X_j | \pi)$ between pairs of the previously selected variables. These candidate links are rank ordered and the highest ranked links are selected until the cumulative value doesn't exceed $T_{xx}$ times the total conditional mutual information. Directionality of these links is based on the mutual information variable ranking determined in step 2, with higher ranked variables pointing toward the lower ranked ones.

Step 4: APRI estimated $p(\pi)$ and $p(X_i | C(X_i))$ using frequency counts, where $C(X_i)$ represents the parents of the node $X_i$ .

APRI reads the database from secondary storage which is quite different from other analyses which assumes that data is stored in fast random-access memory $[3]$ . With the big size of data, typically gigabyte-sized, the assumption is not applicable to our problem. APRI is very efficient in this regard, reading the data set no more than 5 times. Also, APRI performs better than other competing methods for problems with asymmetric populations and containing both continuous and categorical data. To see the comparison of APRI with conventional statistical classification tools and machine learning algorithms, see Refs. $[5,6]$ .

## 3. Bayesian network learning model

To develop a Bayesian network learning model predicting customer's response to the TDP promotion, we followed three stages. First, we prepared a data set to train a Bayesian network model from an existing database (data processing stage). Second, we trained a Bayesian network learning model using APRI (model training stage). Finally, we measured the discriminating power of the Bayesian network learning model (performance evaluation stage).

## 3.1. Bayesian network learning model development

In this analysis, an AT&T marketing database was used to develop a data set because it contains prior history of customer responses for the TDP promotions as well as customer profiles. From the marketing database, 37,124 TDP promotion records were collected during the first half of 1995 in a specific region. It was expected that the data set would contain 'good' predictors which can effectively discriminate takers and nontakers for the TDP promotions. Additional records could have been collected, but the current sample was considered sufficient for the development of a prototype model.

We called those customers who took the offer, takers, and those who declined it, nontakers. Out of a total 37,124 customers in the data set, 26,172 customers took the offer and 10,952 customers didn't take the offer yielding a $29.5\%$ unconditional probability of being a nontaker. In this paper, we estimated the probability of being a nontaker because they are the customers we want to avoid promoting.

## 3.2. Data processing stage

The marketing database used in this analysis contained almost 300 variables for each customer. Some variables were considered to be relevant to the TDP promotion, but most of them were considered irrelevant. After consulting subject matter experts, 30 variables were preselected out of about 300 variables as the most relevant variables (field nodes) to extract the pattern regarding TDP subscriptions. The preselected 30 variables were candidate variables for the development of the Bayesian network learning model in the next model training stage. For those 30 variables, there were continuous variables (e.g., monthly telephone usage in dollars) and categorical variables (e.g., geographical location, date information). The information on whether a specific customer is a taker or nontaker (prime node) was also included in the data set as a binary variable.

## 3.3. Model training stage

Once a data set was prepared, the data set was separated into two different data sets: training data set and test data set. The training data set was used to develop a Bayesian network learning model using APRI. The test data set was used to check the performance of the developed Bayesian network learning model. In our analysis, we randomly selected 90% of the data set for training and 10% for testing. So, the training data set contained 33,411 records and the test data set contained 3713 records with nontaker's probability being equal to 29.5% for both data sets. After performing 10 fold cross-validations, the most promising result (the most discriminating power which is discussed in the performance evaluation stage) was obtained by constructing a Bayesian network with 12 variables and parameters $T_{\pi x}=0.95$ , $T_{xx}=0.25$ . Fig. 2 shows a Bayesian network learning model developed with 12 variables.

## 3.4. Performance evaluation stage

Based on the Bayesian network learning model developed above, the probability of being a nontaker was predicted using the test data set. That is, the customer-specific information from the test data set was used to propagate the information through the Bayesian network, and the probability of being a nontaker was predicted.

![](/api/attachments/GWJJ6H65/fulltext/images/812f8e5e90b2ff2bb81232148d4d30f79717be8ecd8a0c9d6974a92e3056dd3f.jpg)  
Fig. 2. A Bayesian network learning model with 12 variables.

In many practical problems, a perfect prediction is not possible. To evaluate the usefulness of the prediction, it is necessary to measure its discriminating power. To evaluate the performance of the prediction based on the Bayesian network model, the test data set was ordered in descending order depending on the estimated probability of being a nontaker. The second and third columns in Table 1 showed the maximum and minimum probabilities for each decile. The average predicted probability was calculated for each decile (fifth column in Table 1). Then, the number of nontakers (sixth column in Table 1) was counted and the fraction of nontakers (seventh column in Table 1) was calculated for each decile of ordered data set. The eighth column in Table 1 was calculated by dividing the seventh column by 29.5% to show the degree of discrimination in each decile. The cumulative index showing the percentage of captured nontakers was also calculated (ninth column in Table 1).

If we can make a perfectly discriminating prediction, all the nontakers would belong to the upper part of the ordered data set. Table 1 shows that, for the first decile in the ordered data set, the percentage of nontakers was 60.1% (the percentage of nontakers in the training data set was 29.5% yielding a lift of 203.8%) which was considered impressive. Also, it showed that we can capture almost 71% of the nontakers up to the fifth decile of the ordered data set.

## 3.5. Misclassification probability and misclassification cost

The Bayesian network learning model can be used for classification based on the probability prediction. If the classifications are perfect, then it is easy to recommend the optimal decision based on them. That is, if a customer is classified as a taker, then offer the TDP. If a customer is classified as a nontaker, then do not offer it. We can save costs from unsuccessful promotion. Therefore, with perfect classification capability, the Bayesian network model can be used as a decision support system directly. In reality, perfect classification procedures are hardly obtainable.

One way of evaluating the performance of any classification procedure is to calculate the misclassification probability. Suppose that we classify a customer as taker or nontaker based on the predicted probability. That is, if the predicted probability (of being a nontaker) is greater than the 'threshold probability', then we classify the customer as a nontaker. If the predicted probability is less than the 'threshold probability', then we classify it as a taker. We will label the nontaker's population as $\pi_1$ and the taker's population as $\pi_2$ . Let's denote prior probability of population $i$ as $p(\pi_i)$ , and the probability of classifying population $i$ given that it is actually from the population $j$ as $p(i|j)$ , $i, j = 1, 2$ . Note that $p(i|j)$ is different depending on different 'threshold proba bilities'. Then, the misclassification probability is calculated as the weighted sum of the false negative rate and the false positive rate weighted by their prior probabilities, or $p(2|1) \cdot p(\pi_{1}) + p(1|2) \cdot p(\pi_{2})$ . The misclassification probability was calculated to be minimum at the threshold level 0.5. Therefore it would be good to use threshold level 0.5 for classification if we want to minimize the misclassification probability. It means that a little bit over 10% of customers will be classified as nontaker (See minimum probability in Table 1).

Table 1
Gains table

<table><tr><td rowspan="2">Decile %</td><td rowspan="2">Maximum probability</td><td rowspan="2">Minimum probability</td><td rowspan="2">Observation per group</td><td rowspan="2">Average predicted probability</td><td rowspan="2">Number of nontakers</td><td colspan="2">Nontaker</td><td rowspan="2">Cumulative index %</td></tr><tr><td>Rate %</td><td>Index %</td></tr><tr><td>0–10</td><td>1.0</td><td>0.553</td><td>371</td><td>0.681</td><td>223</td><td>60.1</td><td>203.8</td><td>20.4</td></tr><tr><td>10–20</td><td>0.553</td><td>0.429</td><td>371</td><td>0.486</td><td>189</td><td>50.9</td><td>172.7</td><td>37.6</td></tr><tr><td>20–30</td><td>0.429</td><td>0.349</td><td>371</td><td>0.387</td><td>144</td><td>38.8</td><td>131.6</td><td>50.8</td></tr><tr><td>30–40</td><td>0.349</td><td>0.293</td><td>371</td><td>0.320</td><td>115</td><td>31.0</td><td>105.1</td><td>61.3</td></tr><tr><td>40–50</td><td>0.293</td><td>0.245</td><td>371</td><td>0.268</td><td>105</td><td>28.3</td><td>96.0</td><td>70.9</td></tr><tr><td>50–60</td><td>0.245</td><td>0.203</td><td>371</td><td>0.223</td><td>89</td><td>24.0</td><td>81.3</td><td>80.0</td></tr><tr><td>60–70</td><td>0.203</td><td>0.166</td><td>371</td><td>0.183</td><td>75</td><td>20.2</td><td>68.5</td><td>85.8</td></tr><tr><td>70–80</td><td>0.166</td><td>0.123</td><td>371</td><td>0.144</td><td>69</td><td>18.6</td><td>63.1</td><td>92.1</td></tr><tr><td>80–90</td><td>0.123</td><td>0.086</td><td>371</td><td>0.102</td><td>55</td><td>14.8</td><td>50.3</td><td>97.2</td></tr><tr><td>90–100</td><td>0.086</td><td>0.035</td><td>374</td><td>0.056</td><td>31</td><td>8.3</td><td>28.1</td><td>100.0</td></tr><tr><td>Total</td><td></td><td></td><td>3713</td><td>0.295</td><td>1095</td><td>29.5</td><td></td><td></td></tr></table>

Note: (Column 8) = (Column 7)/29.5%.

On the other hand, suppose that we were interested in minimizing the expected misclassification cost (EMC) of the classification procedure. Let's denote the cost of classifying nontaker (population 1) into taker (population 2) as $C(2|1)$ and cost of classifying taker into nontaker as $C(1|2)$ . Then the EMC is expressed as

$$
\begin{array}{r l} \mathrm{EMC} & = C (2 | 1) p (2 | 1) p (\pi_ {1}) \\ & + C (1 | 2) p (1 | 2) p (\pi_ {2}). \end{array}
$$

Suppose that $C(2|1)$ is two times larger than $C(1|2)$ , then the ‘threshold probability’ minimizing EMC is calculated as 0.4. This is because the cost of misclassifying nontakers as takers is high (for example, the time spent for customer contact), therefore it is better to classify customers aggressively as nontakers. On the other hand, if $C(1|2)$ is two times larger than $C(2|1)$ , then the ‘threshold probability’ minimizing EMC is calculated as 0.8. This is because the cost of misclassifying takers as nontakers is high (for example, poor customer satisfaction and possible change of companies), therefore it is better to classify customers conservatively as nontakers. If $C(1|2)$ is the same as $C(2|1)$ , then the EMC criterion gives the same ‘threshold probability’ as the minimizing misclassification probability.

As was shown above, if there exists an asymmetric misclassification cost structure, a classification procedure depending only on the misclassification probability criterion may provide misleading input for the decision-making process. It doesn't consider the cost related to the classification. If the misclassification cost is different for each customer and uncertainty is attached to the misclassification cost structure, even the EMC criterion does not provide sensible input on the individual customer level. Therefore, it is better to use the predicted probability directly as an input in the decision-making process rather than the classification result. That is, regardless of the objective in the decision problem (whether it is minimizing misclassification probability or misclassification cost), the predicted probability should be used directly in the decision-making process. Because the Bayesian network learning model is based on probability theory, the predicted probability from the model can be perfectly linked with the influence diagram framework which is also based on probabilistic decision theory.

## 4. A prototype decision support system development

In Section 3, it was shown that decision support based only on the Bayesian network model can be misleading depending on the objective of the decision problem. So, it is linked with a rigorous decision-making tool to provide an intelligent decision support. In this section, the Bayesian network learning model and the influence diagram framework were integrated to develop a prototype decision support system. The Bayesian network learning model developed by the APRI system was used to predict the probability. And, the influence diagram framework [15] was used as a decision engine for the CCE to make recommendations based on the probability prediction and other related factors to the TDP promotion decision. Fig. 3 shows a prototype decision support system based on the influence diagram framework recommending whether the CCE should promote the TDP or not.

To represent the problem in an influence diagram framework, four types of nodes and two types of arrows are used to represent variables and the relationships among them. The rectangle symbolizes a decision node which represents a decision variable for the decision maker and contains decision alternatives (promote or do not promote). The oval symbolizes a chance node which represents uncertain events and contains a random variable for the event. The double circle symbolizes a deterministic node which represents functional or logical relationships among variables. The round rectangle symbolizes a value node which represents an objective to maximize or minimize. An arrow into a chance node implies the probabilistic dependency between the nodes. An arrow into a decision node implies that when we make a decision, we have information on the value of the predecessor.

![](/api/attachments/GWJJ6H65/fulltext/images/6610f20e85750c5d38d6a07fe4f696bde206808ba909334820006ce1e9c4a98f.jpg)  
Fig. 3. Prototype decision support system for the TDP promotion.

Once a Bayesian network model predicts the probability of being a nontaker, the information is represented as the node ‘predicted probability’ in Fig. 3. The Bayesian network learning model predicts the probability in a continuous scale and later it is discretized to be used in making a recommendation. The node ‘predicted probability’ in Fig. 3 is dynamically linked to the Bayesian network learning model described in Section 3. The event of being an actual taker or nontaker is represented as the node ‘taker or nontaker’ given the node ‘predicted probability.’ The probability of being a nontaker (‘predicted probability’ node) is calibrated using the actual nontaker’s ratio in each decile (seventh column in Table 1). An arrow from the node ‘predicted probability’ to a decision node ‘promote or not’ implies that the predicted probability is available at the time of the decision. A node ‘customer status’ represents the uncertainty that the customer may leave AT&T depending on whether a TDP is offered or not, and the customer is actually a taker or a nontaker. The actual cost of CCE’s time is represented as ‘CCE’s cost’ determined jointly by whether the TDP is offered or not and the CCE's cost per contact. The node ‘monthly usage level (US\$)’ is used to represent the revenue impact related to the decision. The value function we want to maximize is dependent on the cost of offer and the expected revenue from a customer.

Based on the relationships among the variables shown in Fig. 3, a decision support system was implemented on a Sun SPARC Station 10. The interface is designed so that the AT&T CCE can use the system without ever knowing either Bayesian network or influence diagrams. When a customer contact is made, the customer's profile is retrieved from the relevant databases. The Bayesian network learning model, if necessary, predicts the probability of being a nontaker based on the information from the customer profile. Then, the best recommendation regarding the TDP promotion is derived using the influence-diagrams solution algorithm [15]. Based on the recommendation, the decision support system recommends to the CCE whether to promote the plan or not to the current customer. If there is missing information on the customer profile, then the CCE may ask customer questions to better predict the probability. The missing data are shown in the order of importance (based on the mutual information calculation), and as far as it is possible, it is recommended to ask questions in that order because more uncertainty can be resolved in that order. The system then makes a new recommendation based on the new customer information.

As is shown in Fig. 3, there are three arrows into a decision node which imply that the three values are known when optimal decision is derived. Therefore, the optimal recommendation is based on the three values: monthly usage level, CCE's cost/contact and predicted probability. Table 2 summarizes the possible recommendations regarding the TDP promotion. It shows the following. If the average monthly bill size (international charge) is large (more than US $X_2$ /month), then offer the TDP regardless of predicted probability and the cost of offering because the potential benefit of keeping this customer outweighs the cost of offering. The cost of offering would be dependent not only on the expected CCE's time to promote, but on how many customers are waiting in queue to be served. If the monthly bill size is moderate (from US $X_1$ to US $X_2$ /month), then 1) offer it when the cost of offering is small (US $Y_1$ ), 2) offer it only when the cost of offering is moderate (US $Y_2$ ) and the predicted probability (of being a nontaker) is less than $Z_2$ , and 3) do not offer it if the cost of offering is high (US $Y_3$ ). If monthly bill size is small (less than US $X_1$ /month), then offer it only when the cost of offering is small (US $Y_1$ ) and the predicted probability is less than $Z_1$ . Note that the actual numbers are not shown here for proprietary reasons.

Table 2  
Optimal recommendations

<table><tr><td rowspan="2">Monthly usage level ($)</td><td colspan="3">CCE&#x27;s cost</td></tr><tr><td>US$Y1</td><td>US$Y2</td><td>US$Y3</td></tr><tr><td>0-US$X1</td><td>Offer only if predicted probability &lt; Z1</td><td>Do not offer</td><td>Do not offer</td></tr><tr><td>US$X1-US$X2</td><td>Offer</td><td>Offer only if predicted probability &lt; Z2</td><td>Do not offer</td></tr><tr><td>&gt; US$X2</td><td>Offer</td><td>Offer</td><td>Offer</td></tr></table>

Note: $X_{1} < X_{2}, Y_{1} < Y_{2} < Y_{3}$ , and $Z_{1} < Z_{2}$ .

Those recommendations have some implications on how to implement this decision support system. For example, if a specific customer's bill size is large, then don't bother to predict probability from the Bayesian network learning model, but promote it all the time. If a specific customer's bill size is small, then run the Bayesian network model to predict probability only when the cost of offering is small.

For the purpose of analysis in this paper, we have chosen a simplified version to demonstrate how the prototype decision support system really works. In the real implementation, more factors should be considered such as 1) the effect of stimulated usage because of the TDP subscription, 2) reduced revenue because of discount due to TDP subscription, 3) a more sophisticated assessment of the customer's life with or without the TDP.

## 5. Conclusion

We developed a prototype decision support system based on the Bayesian network learning model and influence diagram framework. The system was specially developed to make recommendations for a TDP promotion. In Section 3, it was shown that decision support based only on the Bayesian network learning model can be misleading if there are different objectives in the decision problem. So, it was linked with a rigorous decision-making tool to provide an intelligent decision support.

To do that, a Bayesian network learning model was used to predict the response probability for the promotion, and the influence diagram framework was used to integrate the predicted probability with the cost and benefit related to the possible actions. In this paper, it was demonstrated how the knowledge (predicted probability) was extracted using a Bayesian network learning model and linked to the decision support system. The Bayesian-network-based knowledge discovery process was useful in finding patterns out of the customer's response, and it was fed as an important input to the decision support system. Because the Bayesian network learning model was based on probability theory, the predicted probability from the model was perfectly linked with the influence diagram framework which was also based on probabilistic decision theory. Following this approach, the decision support system provided a better recommendation considering various cost factors related to the TDP promotion decision.

There are two areas which deserve to have more attention. First, in this paper, a real-time decision support system using a Bayesian network learning model was presented for a special TDP promotion decision. However, this approach can be equally useful to target customers in providing services such as wireless service, Internet service, entertainment service, banking service, local service, as well as our traditional long-distance service. Second, the data set can be enriched by adding more new information like demographic data from other databases. Those would certainly improve the predicting power of the Bayesian network learning model. But accessing multiple databases at the same time for real-time processing may cause some delay in access time, and it poses a problem to be addressed.

## Acknowledgements

We want to thank Jay Ohm, Yung-Seop Lee, Ann Skudlark, and two anonymous referees for their helpful comments on this paper.

## Appendix A. Entropy and mutual information

As a measure of uncertainty of a random variable, entropy measure has been widely used [4]. The entropy $H(X)$ of a discrete random variable X is defined by $H(X) = -\sum_{x \in X} p(x) \log p(x)$ . It is a measure of information on the average to describe the random variable. From the definition of mutual information, relative entropy can be defined.

Definition: Relative entropy $D(p||q)$ between two probability mass function $p(x)$ and $q(x)$ is defined as

$$
D (p \| q) = \sum_ {x \in X} p (x) \log \frac {p (x)}{q (x)}.
$$

One can show that relative entropy is always nonnegative and is zero if and only if they are mutually independent [9]. In that sense, it is a measure of inefficiency of assuming $q(x)$ when $p(x)$ is the real distribution. From this definition, we can represent mutual information in terms of relative entropy. Let $p(x, y)$ and $p(x)$ and $p(y)$ be joint and marginal probability mass functions of two random variables X and Y.

Definition: Mutual information $I(X;Y)$ of random variables X and Y is defined as the relative entropy between $p(x, y)$ and $p(x)$ $p(y)$ . That is

$$
\begin{array}{r l} I (X; Y) & = D (p (x, y) \| p (x) p (y)) \\ & = \sum_ {x \in X} \sum_ {y \in Y} p (x, y) \log \frac {p (x , y)}{p (x) p (y)}, \\ & \text { or } H (X) - H (X _ {-} Y) \end{array}
$$

in entropy terms.

It is a measure of inefficiency of representing $p(x, y)$ as $p(x)$ $p(y)$ . In other words, it is a measure of inefficiency of assuming independence between two random variables X and Y. Also, we can regard mutual information $I(X;Y)$ as the potential uncertainty reduction of random variable X due to knowledge about the random variable Y. Mutual information is one of the most commonly used criterion for ranking information sources [14].

## References

[1] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Future directions for developing decision support systems, Decision Sciences 11 (1980) 616–631.

[2] A.R. Chaturvedi, Supporting complex real-time decision making through machine learning, Decision Support System 10 (1993) 213–233.

[3] G.F. Cooper, E. Herskovits, A Bayesian method for the induction of probabilistic networks from data, Machine Learning 9 (1992) 309–347.

[4] T.M. Cover, J.A. Thomas, Elements of Information Theory, Wiley, New York, 1991.

[5] K.J. Ezawa, S. Norton, Constructing Bayesian networks to predict uncollectible telecommunications accounts, IEEE Expert 11 (1996) 45–51.

[6] K.J. Ezawa, T. Schuermann, A Bayesian network based learning system: Architecture and performance comparison with other methods, in: C. Froideveaux, J. Kohlas (Eds.), Symbolic and Quantitative Approaches to Reasoning and Uncertainty: Lecture Notes in Artificial Intelligence 946, Springer, Berlin, 1995.

[7] U.M. Fayyad, R. Uthurusamy, Proceedings of the First International Conference on Knowledge Discovery and Data Mining, AAAI Press, Menlo Park, 1995.

[8] U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, Menlo Park, 1995.

[9] R.G. Gallager, Information Theory and Reliable Communication, Simon and Schuster, New York, 1968.

[10] F.V. Jensen, K.G. Olesen, S.K. Anderson, An algebra of Bayesian universes for knowledge-based systems, Networks 20 (1990) 637–659.

[11] F.V. Jensen, Introduction to Bayesian Networks, Springer, Berlin, 1996.

[12] P. Langley, S. Sage, Induction of selective Bayesian classifiers, Uncertainty in Artificial Intelligence 10 (1994) 399-406.

[13] S.L. Lauritzen and, D.J. Spiegelhalter, Local computations with probabilities on graphical structures and their application to expert systems, J. R. Statistics Society B50 (1988) 157–224.

[14] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufmann, 1988.

[15] R.D. Shachter, Evaluating influence diagrams, Operations Research 34 (1986) 871–882.

[16] R.D. Shachter, Evidence absorption and propagation through evidence reversals, Uncertainty in Artificial Intelligence 5, North-Holland (1990) pp. 173–190.

[17] M.J. Shaw, Applying inductive learning to enhance knowledge-based expert systems, Decision Support Systems 4 (1987) 319–332.

[18] M. Singh, M. Valtorta, Construction of Bayesian Network Structures from Data: a Brief Survey and an Efficient Algorithm, Int. J. of Approximate Reasoning 12 (1995) 111–121.

![](/api/attachments/GWJJ6H65/fulltext/images/ff9e76ac4c49b924f29e2d7c9704922508d023a2c67f2b767132e22bd13082c0.jpg)

Jae-Hyeon Ahn is a senior technical staff member at AT&T Laboratories, NJ, USA. He received his B.S. and M.S. degrees in Industrial Engineering from Seoul National University, South Korea. He received his Ph.D. degree in Engineering-Economic Systems from Stanford University, CA, in 1993. He has research and consulting experiences in telecommunications, energy, and health industries. His current research interests include decision analysis, strategy anal-

ysis in the telecommunications industry, service operations management and Bayesian network modeling. His papers appear in Management Science, European Journal of Operational Research, and Journal of Information Technology.

![](/api/attachments/GWJJ6H65/fulltext/images/6dfe5b3248d4932f74827a57b09501d9d32992ded247f17b5f11da9db906cbfe.jpg)

Kazuo J. Ezawa is a technology consultant at AT&T Laboratories, NJ, USA. His expertise includes decision analysis, influence diagrams, Bayesian network learning and normative expert/decision support systems. He received his M.S. in Operations Research from the University of Michigan, Ann Arbor and his Ph.D. degree in Engineering-Economic Systems from Stanford University, CA, in 1986. His papers appear in IEEE Expert, Operations Research, and Un

certainty in Artificial Intelligence proceedings.
