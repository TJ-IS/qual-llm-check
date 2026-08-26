---
otero_id: 1854
otero_key: "3G5WVD7V"
title: "Agent-mediated architecture for reputation-based electronic tourism systems: A neural network approach"
authors: "Qing Cao; Marc J. Schniederjans"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2006.03.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/im

# Agent-mediated architecture for reputation-based electronic tourism systems: A neural network approach

Qing Cao <sup>a</sup>, Marc J. Schniederjans <sup>b,\*</sup>

<sup>a</sup> University of Missouri-Kansas City, Henry W. Bloch School of Business and Public Administration, 5100 Rockhill Road, Kansas City, MO 64110-2499, United States

<sup>b</sup> University of Nebraska-Lincoln, College of Business Administration, Lincoln, NE 68588-0491, United States Received in revised form 17 August 2005; accepted 11 March 2006 Available online 3 May 2006

## Abstract

Agent technology can be used in searching and selecting a good e-tourism system. However, most such systems focus mainly on price and avoid important purchasing decision-making factors such as quality and reputation. Here we define a reputation-based architecture for an e-tourism system that we have called ‘reputation-based electronic tourism’ (RET). An artificial neural network model was created for a reputation agent to evaluate capabilities for selecting products and services in an e-tourism setting. The classification performance of the model was compared to another method. The results indicated that RET could outperform and be more accurate in classifying perspective products and services for consumers. <sup>#</sup> 2006 Elsevier B.V. All rights reserved.

Keywords: E-commerce; Multiple agent system; Neural networks; Management information systems; Tourism

## 1. Introduction

Since the first tourism website was launched, etourism has been one of the fastest growing segments of electronic commerce. In 2005, online tourism transactions jumped to \$32.4 billion from only \$8.6 billion in 1999, leading all other categories in electronic transactions [18]. To support this dramatic increase in business, e-tourism utilizes advanced technologies. One of the most promising technologies for development of electronic commerce is agent technology. it has been used in e-tourism and other e-commerce where a personalized, continuously running, autonomous behavior is desirable [11,29]. Agents can be defined as active objects with special properties tailored to open environments. In computer science, an intelligent agent (IA) refers to a software component that exhibits some form of AI. While the working of software agents used for operator assistance or data mining (Bots) are often based on fixed pre-programmed rules, the term here implies the ability to adapt and learn. The key aspects of agents are their autonomy and abilities to reason and act in their environment, as well as to interact and communicate with other agents to solve complex problems [15]. Autonomy means that the agent can act without the direct intervention of humans or other agents and that it has control over its own actions and internal state. The agent must communicate with the user or other agents to receive instructions and provide results. An essential quality of an agent is the amount of learned behavior and possible reasoning capacity that it has.

At the basic level, the agent may follow a set of rules predefined by the user. The agent then applies them.

The intelligent agent will learn and be able to adapt to the environment in terms of user requests consistent with the available resources [24]. Agent technology is playing an increasingly important role in the development of e-tourism, transforming systems from online brochures to advanced systems with innovative services. Software agents are catalysts for commerce on the Web, with the ultimate goal of agents to accelerate the evolution of the Web from a passive, static medium to a highly interactive environment.

Multiple agent systemb (MAS) may be formed by agents interacting with one another. This is the emerging subfield of distributed AI that tries to provide complex systems of multiple agents and mechanisms for coordinating their behavior [4,30]. In a MAS, a multitude of asynchronous and loosely coupled agents together solve problems, that are beyond the capacity of a single agent.

Currently agent-based e-tourism systems have employed software agents in some stages of consumer buying behavior, such as searching for information, communicating with vendors, and, in cases like Expedia [9] and Priceline [26], making purchase decisions for consumers.

However, the application of agent technology has limitations. Although tourism services produce more revenue than any other product, only about 5% of customers browsing the largest online tourism service sites actually purchase tickets online and use the service [28]. Another shortcoming is that most systems focus only on price and leave out important purchasing decision-making factors, such as the service and product quality and company reputation. Empirical studies have indicated that such factors determine many Internet purchasing decisions. To improve consumer etourism purchases, agent-mediated e-tourism systems should therefore be able to provide capabilities for consumers to evaluate and choose vendors based on multiple criteria.

We have therefore proposed a reputation-based electronic tourism (RET) approach that assesses and selects vendors on the behavior of consumers based on multiple criteria. It uses an artificial intelligence-based model (see Appendix A).

## 2. Related work

## 2.1. E-tourism

E-tourism involves the buying and selling of tourism products and services via electronic channels, such as the Internet, cable TV, etc. Most tourism products (e.g., hotel rooms or flight tickets) are time-constrained and non-stockable. As such, it is necessary for tourism vendors to distribute their products and services in a wide-reaching market where the customers have easy access. As a consumer-centric industry where information plays an important role, e-tourism fits well with the Internet. E-tourism falls into the category of E-retailing which is a special type of e-commerce business model [14]. By the end of year 2005, more than 700 online tourism websites were in operation. According to a recent report by Smith Travel Research (2005), etourism represented 25.4% of the total lodging industry revenues (\$113.7 billion) in the US alone. More recently however [13] claimed that the true size of the e-tourism market was substantially larger, since current e-tourism research focuses only on the marketing of tourism and hospitality operations online.

## 2.2. Intelligent agents and multiple agent systems

Intelligent agents are software agents or entities. They have four well accepted properties that distinguish them from other traditional approaches [16]: characteristics-autonomy (they operate without direct intervention), social ability (they, interact with other agents or humans), reactivity (they respond to the environment in a timely fashion), and pro-activeness (they exhibit goal-directed behavior). These allow agent-based systems to act semi-autonomously, giving agents an important role in the information-rich environment of e-commerce. As argued in [3] there is a strong affinity between the Web and the capability of agents to act through software.

Agent technology has received a great deal of attention over the last decade. Some of the more recent frameworks include JADE [1], ZEUS [23], and JACK [12]. Standards for agent communication have been proposed, the knowledge query and manipulation language [10].

More recently, MAS have gained popularity in IA research [4]. They may have several characteristics: each agent has as a limited viewpoint, there is no global system control, data is decentralized, and computation is asynchronous. These provide the benefits of robustness and efficiency, allowing inter-operation of existing legacy systems and solving problems in which data, expertise, or control is distributed.

## 2.3. Agent applications in electronic commerce

The ‘‘consumer buying behavior’’ (CBB) model presented in [21] had six stages of consumer buying behavior in electronic commerce: need identification (conceptualize a need), product brokering (determine what to buy), merchant brokering (determine who to buy from), negotiation (determine the transaction terms), purchase and delivery (specify how to pay for and receive the goods), and service and evaluation (post-purchase service and buying evaluation). This model captured the roles of agents as mediators in electronic commerce, helping to explain the roles that agents could play in electronic commerce.

Early e-tourism systems in the late 1990s did little more than map traditional offline service to the Web. During the same period most e-tourism websites just provided online brochures. When agent technology was used in e-tourism in the late 1990s, several new business models appeared. For example, using a ‘‘name your own price’’ service, Priceline.com asks customers to provide their desired price for airline tickets or hotel rooms, and the software agents do the work of searching for suitable services, negotiating with vendors, and purchasing the products or services.

Agent technology is often used for product or merchant brokering, and negotiation of the CBB model. Table 1 shows a list of agent applications in e-tourism. It is interesting to note that there is currently no e-tourism system dealing with the ‘‘need identification’’ and ‘‘evaluation’’ stages of the CBB model, although both are important in this informationintensive industry.

In product brokering stage, agents function as assistants helping consumers decide what products to buy, based on their needs and criteria. For example, the ‘vocation expert tool’ of Travelocity.com can narrow down suitable tourism services for consumers according to their personalities, accommodation styles, and other preferences [5]. Similarly, TravelPlan [32] can recommend the most suitable solution or narrow down the possible solutions for consumers based on their preferences and tourism needs.

Agents in the merchant brokering stage query the vendors for information of pricing and service quality, sort and compare such information, and finally make purchase decisions for consumers.

The business transactions are determined in the negotiation stage. However, in current e-tourism systems, agents negotiate only based on price, rather than multiple criteria. According to [6,22], this has limited the usefulness of e-commerce systems.

## 3. RET: an e-tourism system

In our proposed RET system, intelligent agents work together to choose e-tourism vendors for their customers based on multiple criteria. RET is a distributed MAS in which different agents performing four different tasks:

 Record and analyze customer profile.

 Search for and communicate with vendors for products and services.

 Calculate the vendor reputation, based on postconsumption rating by customers, and the preference of the potential customer.

 Evaluate and select vendor based on multiple criteria.

All agents cooperate under in evaluating and selecting the vendor based on the behavioral choices.

## 3.1. Architecture of the RET

In the RET System, software agents would play important roles in the CBB stages of merchant brokering, negotiation, and evaluation. RET would analyze customer needs, search for suitable services, negotiate with vendors, decide the most suitable services based on customer preferences, and purchase the service on behalf of the customer. RET would therefore improve current e-tourism systems by providing two new features:

Table 1  
Roles and examples of agent systems as mediators in e-tourism

<table><tr><td>Stages of consumer buying behavior</td><td>Epedia.com</td><td>Priceline.com</td><td>Travelocity.com</td><td>ATA Airlines</td><td>TravelPlan</td><td>Proposed RET</td></tr><tr><td>1. Need identification</td><td colspan="6">No agent-mediated system has been reported at present</td></tr><tr><td>2. Product brokering</td><td></td><td></td><td>×</td><td></td><td>×</td><td></td></tr><tr><td>3. Merchant brokering</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>4. Negotiation</td><td></td><td>×</td><td></td><td></td><td></td><td>×</td></tr><tr><td>5. Purchase and delivery</td><td colspan="6">The character of consuming products at the point of production lends tourism the advantage of avoiding delivering of any physical products</td></tr><tr><td>6. Product service &amp; evaluation</td><td></td><td></td><td></td><td></td><td></td><td>×</td></tr></table>

 A reputation mechanism with which it can determine the service reputation, based on customer feedback of the post-consumption rating.

 Evaluating and choosing services and products on multiple criteria: preferences of the consumer, such as price and reputation of the vendor, which may be weighted differently in the purchase decision-making according to the buying strategy of the consumer.

Fig. 1 shows the RET infrastructure: agents with different functions and tasks cooperate. The system has four different agent types, as shown.

\- Personal agents communicate with an e-tourism customer who can link up with a personal agent by signing on to RET. When a personal agent has been initiated, it will stay with the customer, knowing his or her preferences. The personal agent also answers the queries and functions as the bridge between the customer and RET.

\- Expert agents, such as hotel expert agent, airline expert agent, etc. analyze the problems and query product agents, shopbots, personal agents, and other expert agents. The expert agents determines the available choices and selects merchants.

\- Shopbot agents interact with other network services as though they were a person. They are any type of autonomous software that operates as an agent for a user or program or simulates human activity. They communicate with third party systems through the Internet. They search and retrieve information queried by the expert agent, negotiate with third party agents, and purchase the services and products on behalf of customers based on the expert agent decisions.

 Reputation Agents store the ad hoc profile and reputation information of the vendor. Moreover, they are responsible for calculating the reputation from the viewpoint of the customer and selecting the vendor for the customer.

Many of the individual components have been discussed in prior literature. Here, only one element (the reputation agent) is discussed.

## 4. Reputation agent

Reputation is the opinion or view of a person about an entity. It is thus very close to the concept of a collaborative filtering system, which recommends systems based on a database of user ratings (as opposed to content-based recommender systems that use the characteristics of the objects). The clients must therefore give information about themselves by rating some of the products or features they know, so that they can receive accurate recommendations [19]. We define the reputation of a tourism vendor as the customer’s belief in the quality of its service and product; i.e., customer preferences and information provided by prior customers. Such opinions influence the buying behavior of the customer of a potential vendor; they are considered an important element in choosing a service [7].

According to [27], reputation is multi-dimensional. For example, a hotel’s reputation can be viewed as the combination of objective reputation criteria (location, facilities, star ranking), and subjective criteria (staff attitude and cleanliness) [8].

## 5. Our study

## 5.1. Survey method

We used a survey questionnaire for data collection, beginning by reviewing the literature for applicable questions. This was followed by conducting interviews with tourists to screen questions for the study. Based on these efforts, a preliminary series of questions were developed to address the key variables of the study. A pilot study was then conducted by distributing the questionnaire to a focus group of 35 part-time MBA students who had used e-tourism systems. The subjects were asked to examine the degree of ease or difficulty in filling out and understanding the questionnaire. Interviews were then conducted to confirm the relationship between the basic constructs and the questions. In addition, construct validity tests where conducted. The unidimensionality test provides evidence of a single latent construct. EFA is a commonly used method to assess unidimensionality in operations management research. A rule of thumb for EFA that indicates unidimensionality is that all or most of the items should have sizable loadings on the first factor with a factor value greater than 0.3. In this research scales items loaded strongly (>0.5) on their intended factors (see Table 2), and all of the criteria of this unidimensionality test were met.

![](/api/attachments/3G5WVD7V/fulltext/images/e320e5b0ee72bd3485ef3f16dde7aff6a1bc547b8f5abd613389b38c8d9808fd.jpg)  
Fig. 1. Architecture of the RET system.

## 5.2. Data collection

Once the questionnaire was finalized it was used to collect the responses from tourists who confirmed they were familiar with and used e-tourism systems. An email survey was used to collect data from a random sample of 800 alumni of a university in the Midwestern region of the USA [2,17].

From the e-mailing, 348 responses were received, constituting a 43.6% response rate. Of the 338 responses, 268 were usable, resulting in a useful response of 33.5%, which was judged sufficient for our study. The 80 unusable responses did not contain sufficient data for further analysis. Table 3 shows the demographic profile of the respondents.

## 5.3. Variable selection

Input variable selection is important in the design of neural networks. Based on previous hotel management and information systems literature, ten input variables (neurons) are used in modeling the reputation agent (hotels): location, price, brand name, physical property, guestroom design, price, functional service, interpersonal service, marketing, food and beverage services, and quality standards. The output variables were 12 hotels with various star ratings (4 with ‘‘5 Star’’, 4 with ‘‘4 Star’’, and 4 with ‘‘3 Star’’) in a major city in the Midwest. Respondents were given detailed information on these twelve hotels. Table 4 provides a summary of the input variables for each hotel and the corresponding measurement instrument.

Table 2  
Construct factor loadings

<table><tr><td>Constructs</td><td>Loading</td></tr><tr><td>Location</td><td>0.81</td></tr><tr><td>Price</td><td>0.72</td></tr><tr><td>Brand name</td><td>0.62</td></tr><tr><td>Physical property</td><td>0.59</td></tr><tr><td>Guestroom design and amenities</td><td>0.82</td></tr><tr><td>Service (functional)</td><td>0.74</td></tr><tr><td>Service (interpersonal)</td><td>0.55</td></tr><tr><td>F&amp;B service</td><td>0.77</td></tr><tr><td>Marketing</td><td>0.54</td></tr></table>

Table 3  
Demographics of respondents

<table><tr><td>Demographics</td><td>Respondents n = 268</td></tr><tr><td>Gender</td><td></td></tr><tr><td>Male</td><td>153</td></tr><tr><td>Female</td><td>115</td></tr><tr><td>Age</td><td></td></tr><tr><td>20–30</td><td>66</td></tr><tr><td>31–40</td><td>94</td></tr><tr><td>41–50</td><td>85</td></tr><tr><td>Over 50</td><td>23</td></tr><tr><td>Education Level</td><td></td></tr><tr><td>Bachelors degree</td><td>72</td></tr><tr><td>Masters degree</td><td>182</td></tr><tr><td>Doctorate degree</td><td>14</td></tr><tr><td>Annual family income</td><td></td></tr><tr><td>Below $29,999</td><td>17</td></tr><tr><td>$30,000–$59,999</td><td>118</td></tr><tr><td>$60,000–$99,999</td><td>94</td></tr><tr><td>Above $100,000</td><td>39</td></tr></table>

## 5.4. Developing the ANN classifier models

An ANN refers to a real, highly complex plexus that is an interconnected group of artificial neurons using a mathematical or computational model for information processing based on a connectionist approach to computation. The ANN classifier models were developed using NeuroShell<sup>1</sup> 2, a Microsoft<sup>1</sup> Windows based application software. The predictive accuracy of ANN models was assessed by using a cross-validation method, K-fold cross validation. In this, the original sample is partitioned into K subsamples. Of these, a single subsample is retained as testing data, while the remaining K  1 subsamples are used as training data. The cross-validation process is repeated K times (the folds), with each of the K subsamples used exactly once as the validation data. The K results from the folds can then be averaged (or otherwise combined) to produce a single estimation. This reduces the variance of the resulting estimate as k is increased. A value of 10 for k is popular and was adopted by us.

Table 4 Summary of input variables

<table><tr><td>Input variables</td><td>Definition</td><td>Scale</td></tr><tr><td>Location</td><td>The convenience of location</td><td rowspan="9">The rating of input variables was based on a scale of 1–5, 5 being best and 1 worst</td></tr><tr><td>Price</td><td>The nightly price/rate</td></tr><tr><td>Brand name</td><td>The hotel brand image and reputation</td></tr><tr><td>Physical property</td><td>Exterior and public space; property cleanliness, property aesthetics, location landscaping, property size, property architecture and property public space</td></tr><tr><td>Guestroom design and amenities</td><td>Room size, room cleanliness, room aesthetics, room work equipment, room entertainment, and other guestroom related features</td></tr><tr><td>Service (functional)</td><td>Service overall, service speed, service efficiency, check-in and check-out efficiency</td></tr><tr><td>Service (interpersonal)</td><td>Service friendliness, service attentiveness, and service professionalism, service customization and personal recognition</td></tr><tr><td>F&amp;B service</td><td>Food and beverage related service</td></tr><tr><td>Marketing</td><td>Room availability, Frequent-guest program, discounts, and marketing</td></tr></table>

## 5.5. Results

In order to assess the effectiveness of the ANN based classifiers for the reputation agent of RET, a comparative analysis of the ‘‘classifying accuracy’’ of neural network models with the forecast accuracy of the traditional MDA technique was presented (for details of MDA, see Appendix B). Correct classifications are defined as the total number of examples in the training data that the network categorizes accurately. The higher the percentage of correct classifications by either model, the more accurate it is. The network generates these percentages by comparing its classification with the category specified for each example in the training data and then summarizes the results for the entire training set. Table 5 shows the predictive accuracy of 10 runs using both ANN and MDA methods. Pair wise ttest was used to examine the significance of the differences of the models. In cases where there was a significant difference, the model with the highest percentage was accepted as being the better hotel classifier.

Table 5  
Comparative analysis of the predictive accuracy of ANN vs. MDA

<table><tr><td>Run</td><td>ANN (%)</td><td>MDA (%)</td><td>Ho: μANN-μMDA (t-value)</td></tr><tr><td>1</td><td>90.8</td><td>72.3</td><td>11.0a</td></tr><tr><td>2</td><td>89.8</td><td>64.5</td><td></td></tr><tr><td>3</td><td>92.1</td><td>67.8</td><td></td></tr><tr><td>4</td><td>85.6</td><td>72.3</td><td></td></tr><tr><td>5</td><td>81.7</td><td>59.4</td><td></td></tr><tr><td>6</td><td>91.8</td><td>71.1</td><td></td></tr><tr><td>7</td><td>87.6</td><td>60.3</td><td></td></tr><tr><td>8</td><td>79.3</td><td>58.4</td><td></td></tr><tr><td>9</td><td>86.4</td><td>47.3</td><td></td></tr><tr><td>10</td><td>76.7</td><td>53.5</td><td></td></tr><tr><td>Average</td><td>86.2</td><td>62.7</td><td></td></tr></table>

<sup>a</sup> Significant at 0.01.

The results indicated that ANN classification outperformed the MDA in all runs. It should be noted that the stringent linearity assumptions of MDAs may cause the inferior classification performance of the MDA. It requires that the data set that distinguishes outputs be linearly separable. However, the overall accuracy of the MDA classifier is only 62.7%. This may suggest that nonlinear effects are present and that, linear models, cannot be adequate in classifying the hotels. Clearly, the ANN method is a good choice for the RET systems.

## 6. Summary

The contribution of this paper is two-fold. First, a reputation based ‘‘multiple agent systems’’ (MAS) for e-tourism (called RET) has been proposed to automate the procedures of product brokering, negotiation, and vendor evaluation. Second, an artificial neural network model was created for the reputation agent (one of the components of RET) to evaluate and select products/ services based on a multiple criteria decision-making concept in an e-tourism setting.

We have discussed the importance of incorporating behavior factors in e-tourism systems and proposed a reputation based multiple agent e-tourism system architecture for product brokering, negotiation, and vendor evaluation. The core component of the architecture is the reputation agent, which can store an ad hoc profile and reputation information to help in selection of the vendor based on reputation. To illustrate this, the reputation agent was modeled using an artificial neural network. A comparative analysis of the approach verses a statistical method was conducted to show that ANN was superior in performance. The module is easy to use and does not require significant ANN expertise.

One limitation of this study was the small number of output variables, namely, the number of the hotels from which to choose.

## Appendix A. Modeling reputation agent

We applied a behavior-based AI approach to model the reputation agent. This approach uses observed behavior: it interprets common behavior through the construction of artificial systems. Researchers have designed systems using artificial neural networks (ANN) in order to stay close to plausible biological structures [20,33,31,34].

An ANN is a parallel distribution processor made up of processing units, which can store experiential knowledge and make it available for use. Its major benefits include nonlinearity and adaptivity. They are capable of detecting and extracting nonlinear relationships and interactions among predictor variables and their inferred patterns and associated estimates of precision do not depend on any assumptions about the distribution of the variables.

A neuron is an information-processing unit. As shown in Fig. 2, it consists of five elementart types: input signals $( x _ { 1 } , ~ x _ { 2 } , ~ . ~ . ~ . , ~ x _ { m } )$ , synaptic weights $( w _ { k _ { 1 } } , w _ { k _ { 2 } } , \ldots , w _ { k _ { m } } ) .$ , a summing junction $( u _ { k } )$ , activation function (w), and output $( y _ { k } )$

![](/api/attachments/3G5WVD7V/fulltext/images/d07ae2f6583b880b48cf0a4153ff24b135dc916f8e05ce259e8b8bc355f9e66c.jpg)  
Fig. 2. Nonlinear model of a neuron.

A signal $x _ { j }$ at the input of synapse j connected to neuron k is multiplied by the synaptic weight $w _ { k j } .$ . The Summing junction aggregates the inputs by applying the synaptic weights to them. An activation function is then applied to the aggregated value to produce an output for a single neuron k. The selection of the activation function depends on the nature of the input data and objective of the ANN. In our study, we created classification ANNs using a ‘softmax function, according to [25]. The following equations depicts a neuron k:

$$
u _ {k} = \sum_ {j = 1} ^ {m} w _ {k j} x _ {j}\tag{1}
$$

and

$$
y _ {k} = \frac {\exp \left(\sum_ {j} w _ {k j} z _ {j}\right)}{\sum_ {k} \exp \left(\sum_ {j} w _ {k j} z _ {j}\right)}\tag{2}
$$

Such multilayer perceptrons have an identify transfer function in the output unit and logistic functions in the middle-layer units that can approximate any continuous functions given enough middle-layer units. The generic three-layer network model can be expressed as:

$$
Y _ {t} = f [ X, \alpha , \beta ] = \sum_ {j = 1} ^ {n} \alpha_ {j} \operatorname{logsig} \left(\sum_ {i = 1} ^ {k} \beta_ {i j} x _ {i} + \beta_ {0 j}\right)\tag{3}
$$

where $Y _ { t }$ is the network’s output, X the input vector, n the number of units in the middle layer, k the number of inputs, a represents a vector of the coefficients (weights) from the middle to output layer units, $\beta$ indicates a matrix of the coefficients from the input to middle-layer units, $\alpha _ { j }$ the weight of the output layer that connects the jth hidden layer unit to the output, $\beta _ { j } = \{ \beta _ { i j } , i = 1 , 2 , . . . , k \}$ the weight vector of the jth unit of the middle layer, $\beta _ { 0 j }$ the bias weight of the jth unit of middle layer unit, and logsig is the logistic transfer function:

$$
\operatorname{logsig} (a) = \frac {1}{1 + \exp (- a)}\tag{4}
$$

A commonly used learning method in ANNs is ‘‘back propagation.’’ It has two phases: the forward phase where activations are propagated from the input to the output layer and the backward phase where the error between the observed actual and the requested nominal value in the output layer are propagated backwards to modify the weights and bias values.

## Appendix B. Discriminant analysis

Discriminant analysis classifies objects into one of two or more groups based on a set of features that describe them. In general, we assign an object to one of a number of predetermined groups based on observations made on the object. The LDA procedure constructs a linear discriminant function by maximizing the ratio of between- to within-groups variances. If X is the vector of scores or predictor attributes, then for a binary classification problem the discriminant function can be written as follows:

$$
D (X) = X \sum^ {- 1} (\mu_ {1} - \mu_ {2}) - \frac {1}{2} (\mu_ {1} - \mu_ {2}) ^ {T} \sum^ {- 1} (\mu_ {1} + \mu_ {2}),\tag{5}
$$

where $( \mu _ { 1 } - \mu _ { 1 } )$ , and $\sum _ { \alpha ^ { \mathbf { f } } } ^ { - 1 }$ are mean vectors for group 1, group 2 and inverse of common covariance matrix, respectively. The term D(X) is a constant number for a given vector X.

## References

[1] F. Bellifernine, A. Poggi, G. Rimassa, Developing multi-agent systems with JADE, 7th International Workshop Proceedings, 2000, pp. 89–103.

[2] K.K. Boyer, J.R. Olson, R.J. Calantone, J. Roger, E. Jackson, Print versus electronic surveys: a comparison of data collection methodologies, Journal of Operations Management 20(4), 2002, pp. 357–373.

[3] E. Brynjolfsson, M.D. Smith, Frictionless commerce? A comparison of internet and conventional retailers Management Science 46(4), 2000, pp. 563–585.

[4] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25(3), 1999, pp. 225–237.

[5] D. Camacho, D. Borrajo, M.J. Molina, Intelligent travel planning: a multiagent planning system to solve web problems in the e-tourism domain, Autonomous Agents & Multi-Agent Systems 4(5), 2001, pp. 387–401.

[6] K. Chen, B. Church, Multi-item classification and generic inventory stock control policies, Production and Inventory Management Journal 11(2), 1992, pp. 30–49.

[7] G.C. Dellaert, Tourists’ valuation of other tourists’ contribution to travel web sites, Proceedings Information and Communication Technologies in Tourism 2000, pp. 293–302.

[8] L. Dube, L.M. Renaghan, How hotel attributes deliver the promised benefits, Cornell Hotel and Restaurant Administration Quarterly 40(5), 1999, pp. 89–95.

[9] Expedia, www.expedia.com.

[10] T. Finin, R. Fritzson, D. McKay, R. McEntire, KQML as an agent communication language, Proceedings of the Third International Conference on Information and Knowledge Management, New York, NY, 1994.

[11] R.H. Guttman, A.G. Moukas, P. Maes, Agent-mediated electronic commerce: a survey, The Knowledge Engineering Review 13, 1998, pp. 147–156.

[12] N. Howden, R. Ro¨nnquist, A. Hodgson, A. Lucas, JACK intelligent agents: summary of an agent infrastructure, Paper presented at the 5th International Conference on Autonomous Agents, 2001, Montreal, Canada.

[13] S. Hudson, N. Lang, A destination case study of marketing tourism online: Banff, Canada, Journal of Vacation Marketing 8(2), 2002, pp. 155–165.

[14] J. Jaehun, A business model and its development strategies for electronic tourism markets, Information Systems Management 19(5), 2002, pp. 58–69.

[15] A.K. Jain, M. Aparico, M.P. Singh, Agents for process coherence in virtual enterprises, Communications of the ACM 42(3), 1999, pp. 62–69.

[16] N.R. Jennings, K. Sycara, M. Wooldridge, A roadmap of agent research and development, International Journal of Autonomous Agents and Multi-Agent Systems 1(1), 1998, pp. 7–38.

[17] R.D. Klassen, J. Jacobs, Experimental comparison of web, electronic and mail survey technologies in operations management, Journal of Operations Management 19(6), 2001, pp. 713– 728.

[18] K. Lau, K. Lee, P. Lam, Y. Ho, Web-site marketing for the travel and tourism industry, Cornell Hotel and Restaurant Administration Quarterly 42(6), 2001, pp. 55–62.

[19] D. Lemire, Scale and translation invariant collaborative filtering systems, Information Retrieval 8(1), 2005, pp. 129–150.

[20] E.Y. Li, Artificial neural networks and their business applications, Information & Management 27(3), 1994, pp. 303– 313.

[21] P. Maes, R.H. Guttman, A.G. Moukas, Agents that buy and sell, Communications of the ACM 42(3), 1999, pp. 81–87.

[22] J. Morris, P. Ree, P. Maes, Sardine: dynamic seller strategies in an auction marketplace, Proceedings of the 2nd ACM Conference on Electronic Commerce, 2000, New York, NY.

[23] H.S. Nwana, D.T. Ndumu, L.C. Lee, J.C. Collis, ZEUS: a toolkit for building distributed multiagent systems, Applied Artificial Intelligence 13(1–2), 1999, pp. 129–185.

[24] M.P. Papazoglou, Agent-oriented technology in support of ebusiness, Communications of the ACM 44(4), 2001, pp. 71– 77.

[25] F.Y. Partovi, M. Anandarajan, Classifying inventory using an artificial neural network approach, Computers & Industrial Engineering 41(4), 2002, pp. 389–404.

[26] Princeline.com http://www.priceline.com.

[27] J. Sabater, C. Sierra, Regret: a reputation model for gregarious societies, In report of Artificial Intelligence Research Institute CSIC - Spanish Scientific Research Council, 2000, Bellaterra, Catalonia, Spain.

[28] B.L.D. Santosa, K. Peffersb, Competitor and vendor influence on the adoption of innovative applications in electronic commerce, Information & Management 34(3), 1998, pp. 175–184.

[29] M.J. Schniederjans, Q. Cao, E-Commerce Operations Management, World Scientific, Singapore, 2002.

[30] R. Sikora, M.J. Shaw, A multi-agent framework for the coordination and integration of information systems, Management Science 44(11), 1998, pp. S65–S79.

[31] K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Management Science 38(7), 1992, pp. 926–947.

[32] Travelplan.com http://www.travelplan.com.

[33] B.K. Wonga, J.A. Monacob, Expert system applications in business: a review and analysis of the literature (1977–1993), Information & Management 29(3), 1995, pp. 141–152.

[34] B.K. Wonga, S. Selvib, Neural network applications in finance: a review and analysis of literature (1990–1996), Information & Management 34(3), 1998, pp. 129–139.

![](/api/attachments/3G5WVD7V/fulltext/images/368dbbf2df90bce863ee5c86522b3f1bf67c3c7693177f9da29861153b87f7af.jpg)

Qing Cao is an Assistant Professor of Management Information Systems at H.W. Bloch School of Business at the University of Missouri, Kansas City. He received a PhD in management information systems/operations management from University of Nebraska – Lincoln. His research interests include artificial intelligence, electronic commerce, systems analysis and design, and information systems strategy.

He has published 16 research articles in journals such as Communications of ACM, Decision Sciences, IEEE Transactions on Systems, Man, and Cybernetics, Information and Management, Journal of Operations Management, International Journal of Production Research, European Journal of Operational Research, Computers and Operations Research, Journal of Database Management, International Journal of Production Economics, among others. He is the recipient of the 2005 UMKC Trustees’ Faculty Fellowship Award for his accomplishments in research.

![](/api/attachments/3G5WVD7V/fulltext/images/90b3c5c3eb53c8eae0e8b14f012a2e2f3a1dc04f3987ce2185acaad291f21bfd.jpg)

Marc J. Schniederjans is the C. Wheaton Battey Distinguished Professor of Business in the College of Business Administration at the University of Nebraska-Lincoln. He holds a PhD and MBA from Saint Louis University. He has authored numerous books and published more than 90 journal articles, appearing in such journals as Operations Research, Decision Sciences, Production and Operations Management

Journal, European Journal of Operational Research, Communications of the ACM, Information & Management, Decision Support Systems, Interfaces, IEEE Transactions on Engineering Management, and Computers and Operations Research.
