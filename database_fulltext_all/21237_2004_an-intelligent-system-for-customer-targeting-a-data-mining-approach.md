---
otero_id: 21237
otero_key: "HCZ2W8VM"
title: "An intelligent system for customer targeting: a data mining approach"
authors: "YongSeog Kim; W.Nick Street"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00008-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 37 (2004) 215 – 228

www.elsevier.com/locate/dsw

# An intelligent system for customer targeting: a data mining approach

YongSeog Kim<sup>a,</sup>\*, W. Nick Street<sup>b</sup>

<sup>a</sup> Business Information Systems, Utah State University, Logan, UT 84322, USA <sup>b</sup> Management Sciences, University of Iowa, Iowa City, IA 52242, USA

Received 1 August 2002; accepted 1 December 2002

Available online 15 February 2003

## Abstract

We propose a data mining approach for market managers that uses artificial neural networks (ANNs) guided by genetic algorithms (GAs). Our predictive model allows the selection of an optimal target point where expected profit from direct mailing is maximized. Our approach also produces models that are easier to interpret by using a smaller number of predictive features. Through sensitivity analysis, we also show that our chosen model significantly outperforms the baseline algorithms in terms of hit rate and expected net profit on key target points. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Customer targeting; Data mining; Feature selection; Genetic algorithms; Neural networks; Ensemble

## 1. Introduction

The ultimate goal of decision support systems is to provide managers with information that is useful for understanding various managerial aspects of a problem and to choose a best solution among many alternatives. In this paper, we focus on a very specific decision support system on behalf of market managers who want to develop and implement efficient marketing programs by fully utilizing a customer database. This is important because, due to the growing interest in micro-marketing, many firms devote considerable resources to identifying households that may be open to targeted marketing messages. This becomes more critical through the easy availability of data warehouses combining demographic, psychographic and behavioral information.

Both the marketing [8,19,33] and data-mining communities [4,32,27,13] have presented various database-based approaches for direct marketing. A good review of how data mining can be integrated into a knowledge-based marketing can be found in [41]. Traditionally, the optimal selection of mailing targets has been considered one of the most important factors for direct marketing to be successful. Thus, many models aim to identify as many customers as possible who will respond to a specific solicitation campaign letter, based on the customer’s estimated probability of responding to marketing program.

This problem becomes more complicated when the interpretability of the model is important. For example, in database marketing applications, it is critical for managers to understand the key drivers of consumer response. A predictive model that is essentially a ‘‘black box’’ is not useful for developing comprehensive marketing strategies. At the same time, a rulebased system that consists of too many if-then statements can make it difficult for users to identify the key drivers. Note that two principal goals, model interpretability and predictive accuracy, can be in conflict.

Another important but often neglected aspect of models is the decision support function that helps market managers make strategic marketing plans. For example, market managers want to know how many customers should be targeted to maximize the expected net profit or increase market share while at least recovering the operational costs of a specific campaign. In order to attain this goal, market managers need a sensitivity analysis that shows how the value of the objective function (e.g., the expected net profit from the campaign) changes as campaign parameters vary (e.g., the campaign scope measured by the number of customers targeted).

In this paper, we propose a data-mining approach to building predictive models that satisfies these requirements efficiently and effectively. First, we show how to build predictive models that combine artificial neural networks (ANNs) [37] with genetic algorithms (GAs) [18] to help market managers identify prospective households. ANNs have been used in other marketing applications such as customer clustering [1,16] and market segmentation [2,21]. We use ANNs to identify optimal campaign targets based on each individual’s likelihood of responding to campaign message positively. This can be done by learning linear or possibly nonlinear relationships between given input variables and the response indicator. We go one step further from this traditional approach. Because we are also interested in isolating key determinants of customer response, we select different subsets of variables using GAs and use only those selected variables to train different ANNs.

GAs have become a very powerful tool in finance, economics, accounting, operations research, and other fields as an alternative to hill-climbing search algorithms. This is mainly because those heuristic algorithms might lead to a local optimum, while GAs are more likely to avoid local optima by evaluating multiple solutions simultaneously and adjusting their search bias toward more promising areas. Further, GAs have been known to have superior performance to other search algorithms for data sets with high dimensionality [28].

Second, we demonstrate through a sensitivity analysis that our approach can be used to determine the scope of marketing campaign given marginal revenue per customer and marginal cost per campaign mail. This can be a very useful tool for market managers who want to assess the impacts of various factors such as mailing cost and limited campaign budget on the outcomes of marketing campaign.

Finally, we enhance the interpretability of our model by reducing the dimensionality of data sets. Traditionally, feature extraction algorithms including principal component analysis (PCA) have been often used for this purpose. However, PCA is not appropriate when the ultimate goal is not only to reduce the dimensionality, but also to obtain highly accurate predictive models. This is because PCA does not take into account the relationship between dependant and other input variables in the process of data reduction. Further, the resulting principal components from PCA can be difficult to interpret when the space of input variables is huge.

Data reduction is performed via feature selection in our approach. Feature selection is defined as the process of choosing a subset of the original predictive variables by eliminating features that are either redundant or possess little predictive information. If we extract as much information as possible from a given data set while using the smallest number of features, we cannot only save a great amount of computing time and cost, but also build a model that generalizes better to households not in the test mailing. Feature selection can also significantly improve the comprehensibility of the resulting classifier models. Even a complicated model—such as a neural network—can be more easily understood if constructed from only a few variables.

Our methodology exploits the desirable characteristics of GAs and ANNs to achieve two principal goals of household targeting at a specific target point: model interpretability and predictive accuracy. A standard GA is used to search through the possible combinations of features. The input features selected by GA are used to train ANNs. The trained ANN is tested on an evaluation set, and a proposed model is evaluated in terms of two quality measurements— cumulative hit rate (which is maximized) and complexity (which is minimized). We define the cumulative hit rate as the ratio of the number of actual customers identified out of the total number of actual customers in a data set. This process is repeated many times as the algorithm searches for a desirable balance between predictive accuracy and model complexity. The result is a highly accurate predictive model that uses only a subset of the original features, thus simplifying the model and reducing the risk of overfitting. It also provides useful information on reducing future data collection costs.

In order to help market managers determine the campaign scope, we run the GA/ANN model repeatedly over different target points to obtain local solutions. A local solution is a predictive feature subset with the highest fitness value at a specific target point. At a target point i where $0 \leq i \leq 1 0 0$ , our GA/ANN model searches for a model that is optimal when the best i% of customers in a new data set is targeted based on the estimated probability of responding to the marketing campaign. Once we obtain local solutions, we combine them into an Ensemble, a global solution that is used to choose the best target point. Note that our Ensemble model is different from popular ensemble algorithms such as Bagging [7] and Boosting [15] that combine the predictions of multiple models by voting. Each local solution in our Ensemble model scores and selects prospects at a specific target point independently of other local solutions. Finally, in order to present the performance of local solutions and an Ensemble, we use a lift curve that shows the relationship between target points and corresponding cumulative hit rate.

This paper is organized as follows. In Section 2, we explain GAs for feature selection in detail, and motivate the use of a GA to search for the global optimum. In Section 3, we describe the structure of the GA/ ANN model, and review the feature subset selection procedure. In Section 4, we present experimental results of both the GA/ANN model and a single ANN with the complete set of features. In particular, a global solution is constructed by incorporating the local solutions obtained over various target points. We show that such a model can be used to help market managers determine the best target point where the expected profit is maximized. In Section 5, we review related work for direct marketing from both the marketing and data mining communities. Section 6 concludes the paper and provides suggestions for future research directions.

## 2. Genetic algorithms for feature selection

A genetic algorithm (GA) is a parallel search procedure that simulates the evolutionary process by applying genetic operators. We provide a simple introduction to a standard GA in this section. More extensive discussions on GAs can be found in [18].

Since [18], various types of GAs have been used for many different applications. However, many variants still share common characteristics. Typically, a GA starts with and maintains a population of chromosomes that correspond to solutions to the problem. A chromosome can be represented by a number of different schema including but not limited to strings of bits or vectors of real numbers with fixed or variable length. A chromosome is typically represented by a fixed-size string and consists of a number of genes called alleles. In our approach for feature selection, the representation of an agent consists of D bits, where D is the number of input features, with each of the bits indicating whether the corresponding feature is selected or not (1 if a feature is selected, 0 otherwise).

Since a GA cannot typically search the whole space of chromosomes, it gradually limits its focus to more highly fit regions of the search space. One or more fitness values must be assigned to each string in order to guide a GA toward more promising regions. By default, standard GAs are designed for maximization problems with only one objective. Each fitness value can be determined by a fitness function that we want to optimize. In our work, the fitness value for a string is determined by a neural network. Using information from households with an observed response, the ANN is able to learn the typical buying patterns of customers in the dataset. The trained ANN is tested on an evaluation set, and the proposed model is evaluated both on the hit rate (which is maximized) and the complexity (number of features, which is minimized) of the solution. Finally, these two quality measurements are combined into one and used to evaluate the quality of each string.

Note that combining multiple objectives into one is not recommended in general. However, the main goal of this paper is to propose an intelligent system for customer targeting that can support strategic marketing plans. In order to show the feasibility of such a model, we keep our model as simple as possible by using a standard GA that can consider only one objective. Further, combining multiple objectives is one of the most common practices [42] and our framework can be easily modified to consider multiple objectives separately. For readers who are interested in a customer targeting problem using GAs that consider multiple objectives, we refer to previous work [5,27].

Once fitness values are assigned to each chromosome in the current population, the GA proceeds to the next generation through three genetic operators: reproduction, crossover, and mutation. We describe three generic operators as follows:

Reproduction: This operator determines which strings in the current population survive into the next generation. A fundamental rule is that a string with a higher fitness value has higher chance of surviving into the next generation. Roulette wheel selection is one frequently used method, in which each string survives in proportion to the ratio of its fitness to the overall population fitness. In our work, we use another well-known method, ranking-based reproduction. In this scheme, the strings are sorted by their fitness value, and a fixed number of the best elements from the current population are copied into the next generation.

Crossover: The crossover (or recombination) operator combines a part of one string with a part of another string and is controlled by a crossover probability Pr(crossover). Typically, it takes two strings called the parents as inputs, and returns one or two new ones, the offspring. In this way, we hope to combine the good parts of one string with the good parts of another string, yielding an even better string after the operation. Many different kinds of crossover operators have been proposed including single-point, two-point, and uniform crossover [30]. Our crossover operator follows the commonality-based crossover framework assuming that commonly selected features in the parents are more likely to lead to the offspring with improved performance [10]. In our implementation, it takes two agents, a parent a and a random mate, and scans through every bit of the two agents. If it locates a different bit, it flips a coin to determine the offspring’s bit.

Mutation: This operator assigns a new value to a randomly chosen gene and is controlled by a mutation probability Pr(mutation). By introducing new genetic characteristics into the pool of chromosomes, it prevents the gene depletion that might lead a GA to converge to a local optimum. The mutation operator in this paper always randomly selects one bit of each string and flips it.

## 3. GA/ANN model for customer targeting

Our predictive model of household buying behavior is a hybrid of the GA and ANN procedures. In our approach, the GA identifies relevant consumer descriptors that are used by the ANN to forecast consumer choice given a specific target point. Our final solution, Ensemble, consists of multiple local solutions each of which is an optimized solution at a specific target point. In this section, we present the structure of our GA/ANN model and the evaluation criteria used to select an appropriate predictive model.

## 3.1. Evaluation metrics

We define two heuristic evaluation metrics, F<sub>complexity</sub> and F<sub>accuracy</sub>, to evaluate selected feature subsets. These objectives are combined with equal weight to return one fitness value for candidate solutions.

$F _ { \mathrm { c o m p l e x i t y } } \mathrm { . }$ This objective is aimed at finding parsimonious solutions by minimizing the number of selected features as follows:

$$
F _ {\text { complexity }} = 1 - \frac {d - 1}{D - 1}\tag{1}
$$

where d and D represent the dimensionality of the selected feature set and of the full feature set, respectively. Note that at least one feature must be used.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
for each target point i where  $i = 10, 20, \cdots, 90$ 
run GA/ANN, optimizing top  $i\%$  of training set
select best $_{i}$  based on the fitness value
Ensemble(i) = best $_{i}$ 
endfor
</div>

## Fig. 1. Pseudo code for Ensemble construction.

Other things being equal, we expect that lower complexity will lead to easier interpretability of solutions as well as better generalization.

$F _ { \mathrm { a c c u r a c y } } .$ : The purpose of this objective is to favor feature sets with higher discriminative power to discriminate buyers from non-buyers. In our application, $F _ { \mathrm { a c c u r a c y } }$ is same as cumulative hit rate, the ratio of the number of actual customers identified, AC, out of the total actual customers, TAC. Note that AC is dependent on how many customers are targeted. Cumulative hit rate can be represented in a mathematical form as follows:

$$
F _ {\text { accuracy }} = \frac {\mathrm{AC}}{\mathrm{TAC}}.\tag{2}
$$

Often hit rate, the ratio of the number of actual customers identified out of the number of customers targeted has been used as an alternative measurement. However, we also note that it is important to have the values of two evaluation metrics in the same range between 0 and 1. Since we can always attain this requirement by using cumulative hit rate by targeting the smallest proportion of actual buyers (in the data used in this paper, about 6% of customers are actual buyers), we prefer cumulative hit rate to hit rate.

## 3.2. Algorithm outline

We show an abstract view of our algorithm in Fig. 1. As a first step, our model searches for a set of local solutions optimized at a specific target point. A local solution best is an optimal solution when the firm targets the best $i \%$ customers based on their estimated probability of responding to a solicitation letter. In this paper, we consider nine target points (10%, 20%, . . ., 90%) but more refined target points can be analyzed without the need to modify the structure of our algorithm. The GA/ANN component in our algorithm is used for finding local solutions and discussed in detail in Section 3.3. Once all the local solutions are found, we combine them into the final model, Ensemble. Each local solution is a neural network model built using the feature subset specific to a target point, and our Ensemble is a collection of such models.

However, in order to estimate the performance of Ensemble on the evaluation data, we cannot simply combine the best estimates of local solutions over different target points. Rather, the estimate of Ensemble at target point i (i.e., when we target the best $i \%$ of customers) is the estimated performance of local solution best<sub>i</sub> optimized at target point i. Ideally, the performance of Ensemble should return the highest hit rate over all the target points compared to all the local solutions.

## 3.3. Structure of GA/ANN model

The structure of GA/ANN model for finding local solutions is shown in Fig. 2. First, the GA searches the exponential space of feature subsets and passes one subset of features to an ANN. The ANN extracts predictive information from each subset and learns the patterns. Once an ANN learns the data patterns, the trained ANN is evaluated on a data set not used for training, and returns two evaluation metrics, $F _ { \mathrm { a c c u r a c y } }$ and $F _ { \mathrm { c o m p l e x i t y } } ,$ to the GA. The two evaluation metrics are then combined with equal weight into one fitness value. It is important to note that in both the learning and evaluation procedures, the ANN uses only the selected features.

![](/api/attachments/HCZ2W8VM/fulltext/images/5bda81b57e0e15dae0ebaa2d58e9aeef143a63bf60b0ada741902a678557423c.jpg)  
Fig. 2. The structure of GA/ANN model. GA searches for a good subset of features and passes them to an ANN. The ANN calculates the ‘‘goodness’’ of each subset and returns two evaluation metrics to GA.

Based on the fitness value, the GA biases its search direction to maximize the combined objective. This routine continues for a fixed number of generations. Among all the evolved models over the generations, we select the best model in terms of the fitness value. Once we choose the best model, we train the ANN using all the training points with the selected features only. The trained model is then used to rank the potential customers (the records in the evaluation set) in descending order by the probability of buying RV insurance (see Section 4), as predicted by the ANN. We finally select the top i% of the prospects in the evaluation set and evaluate the model’s accuracy.

In order to provide a reliable estimate for all the candidates, we estimate their fitness with a rigorous estimation procedure, k-fold cross validation. In this procedure, the training data is divided into k nonoverlapping groups. We train an ANN using the first k - 1 groups of training data and test the trained ANN on the kth group. We repeat this procedure until each of the groups is used as a test set once. We then take the average of the performance measurements over the k folds. In our experiment, we set k = 2. This is a reasonable compromise considering the computational complexity of systems like ours. Further, an estimate from twofold cross validation is likely to be more reliable than an estimate from a common practice using a single holdout set.

## 4. Application

The new GA/ANN methodology is applied to the prediction of households interested in purchasing an insurance policy for recreational vehicles. To benchmark the new procedure, we contrast the predictive performance of Ensemble to a single ANN with the complete set of features. We do not compare our approach to a standard logit regression model because a logit regression model is a special case of single ANN with one hidden node.

## 4.1. Data description

The data are taken from a solicitation of 9822 European households to buy insurance for a recreational vehicle. These data, taken from the CoIL 2000 forecasting competition [26], provide an opportunity to assess the properties of the GA/ ANN procedure in a customer prospecting application.<sup>1</sup> In our analysis, we use two separate datasets: a training set with 5822 households and an evaluation set with 4000 households. The training data is used to calibrate the model and to estimate the hit rate expected in the evaluation set. Of the 5822 prospects in the training dataset, 348 purchased RV insurance, resulting in a hit rate of 348/5822 = 5.97%. From the manager’s perspective, this is the hit rate that would be obtained if solicitations were sent out randomly to consumers in the firm’s database.

The evaluation data is used to validate the predictive models. Our Ensemble predictive model is designed to return the top i% of customers in the evaluation dataset judged to be most likely to buy RV insurance. The model’s predictive accuracy is examined by computing the observed hit rate among the selected households. It is important to understand that only information in the training dataset is used in developing the model. Data in the evaluation dataset is used exclusively for forecasting.

In addition to the observed RV insurance policy choices, each household’s record also contains 93 additional variables, containing information on both socio-demographic characteristics (variables 1 – 51) and ownership of various types of insurance policies (variables 52– 93). Originally, each data set had 85 attributes. We omitted the first feature (customer subtype) mainly because it would expand search space dramatically with little information gain if we represented it a 41-bit variable. Further, we can still exploit the information of customer type by recording the fifth feature (customer main type) as a 10-bit variable, which is coded into 10 binary variables (variables 4– 13). Details are provided in Table 1.

The socio-demographic data are based upon postal code information. That is, all customers living in areas with the same postal code have the same sociodemographic attributes. The insurance firm in this study scales most socio-demographic variables on a 10-point ordinal scale (indicating the relative likelihood that the socio-demographic trait is found in a particular postal code area). This 10-point ordinal scaling includes variables denoted as ‘‘proportions’’ in Table 1. For the purposes of this study, all these variables were regarded as continuous. The psychographic segment assignments (variables 4– 13), however, are household-specific and are binary variables.

In our subsequent discussion, the word feature refers to 1 of the 93 variables listed in Table 1. For example, the binary variable that determines whether or not a household falls into the ‘‘successful hedonist’’ segment is a single feature. Accordingly, in the feature selection step of the GA/ANN model, the algorithm can choose to use any possible subset of the 93 variables in developing the predictive model.

## 4.2. Experimental results

In our experiment, we first select local solutions over different target points and construct lift curves for each of them. A lift curve shows the percentage of all buyers identified in the group selected for a direct mail solicitation at the given target point out of all buyers in the database. We also construct the lift curve of Ensemble and compare it to those of the local models. Finally, we show how our Ensemble solution can be used to select the best target point where the expected profit is maximized under two different campaign scenarios.

We set the values for GA parameters as follows: Pr (mutation) = 1.0, Pr(crossover) = 0.8, Population =100, and Iteration = 200. We use a three-layer ANN and train it with the standard backpropagation algorithm.

Household background characteristics

<table><tr><td>Feature ID</td><td>Feature description</td></tr><tr><td>1</td><td>Number of houses owned by residents</td></tr><tr><td>2</td><td>Average size of households</td></tr><tr><td>3</td><td>Average age of residents</td></tr><tr><td>4–13</td><td>Psychographic segment: successful hedonists, driven growers, average family, career loners, living well, cruising seniors, retired and religious, family with grown ups, conservative families, or farmers</td></tr><tr><td>14–17</td><td>Proportion of residents with Catholic, Protestant, others and no religion</td></tr><tr><td>18–21</td><td>Proportion of residents of married, living together, other relation, and singles</td></tr><tr><td>22–23</td><td>Proportion of households without children and with children</td></tr><tr><td>24–26</td><td>Proportion of residents with high, medium, and lower education level</td></tr><tr><td>27</td><td>Proportion of residents in high status</td></tr><tr><td>28–32</td><td>Proportion of residents who are entrepreneur, farmer, middle management, skilled laborers, and unskilled laborers</td></tr><tr><td>33–37</td><td>Proportion of residents in social class A, B1, B2, C, and D</td></tr><tr><td>38–39</td><td>Proportion of residents who rented home and owned home</td></tr><tr><td>40–42</td><td>Proportion of residents who have 1, 2, and no car</td></tr><tr><td>43–44</td><td>Proportion of residents with national and private health service</td></tr><tr><td>45–50</td><td>Proportion of residents whose income level is &lt;US$30,000, US$30,000–45,000, US$45,000–75,000, US$75,000–123,000, &gt;US$123,000, and average</td></tr><tr><td>51</td><td>Proportion of residents in purchasing power class</td></tr><tr><td>52–72</td><td>Scaled contribution to various types of insurance policies such as private third party, third party firms, third party agriculture, car, van, motorcycle/scooter, truck, trailer, tractor, agricultural M/C, moped, life, private accident, family accidents, disability, fire, surfboard, boat, bicycle, property, social security</td></tr><tr><td>73–93</td><td>Scaled number of households holding insurance policies for the same categories as in scaled contribution attributes</td></tr></table>

We set the number of epochs = 10 and heuristically determine the number of hidden nodes using the formula min(3, $\sqrt { \mathrm { n o d e _ { \mathrm { i n } } } }$ where $\mathrm { n o d e _ { \mathrm { i n } } }$ represents the number of input nodes.

Lift curve of GA/ANN mode

![](/api/attachments/HCZ2W8VM/fulltext/images/db2b9425980841968133bd8134a30bf8f1ada41051898513b8d6ea58ec6a7bd1.jpg)  
Fig. 3. Lift curves of local and Ensemble solution. The lift curve of each local solution is represented as a thin dotted line. The lift curve of Ensemble is constructed by combining the lift curves of local solutions at various target points and shown as a thick solid line.

## 4.2.1. Analysis of lift curves

We first show the lift curves of local solutions (shown as dotted lines) and Ensemble (shown as the thick solid line) in Fig. 3. The lift curve of a local solution best is constructed as follows: We estimate the probability of buying new insurance for each prospect in the evaluation data with trained ANNs using the subset of features chosen by best<sub>i</sub>. After sorting prospects in descending order of the estimated probability, we compute the values of F<sub>accuracy</sub> over various target points j where $j = 1 0 \% , 2 0 \%$ 90%. We define the cumulative hit rate of a model as the value of $F _ { \mathrm { a c c u r a c y } }$ at a given market point. Recall that best<sub>i</sub> is an optimal solution at target point i. The lift curve shows the relationship between a set of market points and their corresponding cumulative hit rates.

The lift curve of Ensemble is constructed by combining a set of cumulative hit rates of best at target point i where $i = 1 0 , 2 0 , . . . , 9 0 . ^ { 2 }$ Under random sampling, the lift curve is a $4 5 ^ { \circ }$ line starting at the origin of the graph. In an ideal case, the lift curve of Ensemble should be a convex hull of lift curves of local solutions because it is a combination of local optimal solutions. However, it is possible for GA to be stuck to local optimum, or for the chose solution to generalize poorly. Among nine target points considered in our model, Ensemble shows the best performance at five target points $( i = 1 0 , 2 0 , 3 0 , 5 0 , 8 0 )$ and second best at one target point (i = 70). Compared to random sampling, our Ensemble returns 3.1 (2.5) times higher cumulative hit rate when we target the best 10% (20%) of customers. For comparison purposes, we implemented an ANN with the complete set of input variables.

We show the hit rates of Ensemble and the single ANN model on the evaluation data in Fig. 4. Our Ensemble shows much better performance at target points i = 10, 20 but loses its advantages over middle target points $i = 3 0 , . . . , 6 0$ . However, our model regains its superior performance at higher target points $i = 7 0 , . . . , 9 0$ . We partially attribute to oversearching [31,35] the lower performance of our model over the middle target points. A model like ours can find fluke rules that fit the training data well but have low predictive accuracy on new data by overusing the estimate of model accuracy. A recent discussion on oversearching caused by multiple comparison procedures can be found in [22].

Though it is worthwhile to determine why the performance of Ensemble changes over different target points, we will leave this issue to future research in order to be consistent with the main purpose of this paper: proposing an intelligent recommendation system for customer targeting. Further, the single ANN requires all the input variables and provides more of a black box solution that market managers cannot utilize for making strategic marketing plans.

We also show the index of chosen features by local solutions in Table 2. Each local solution clearly highlights different predictive features at the given target point. We partially attribute this finding to the strong correlation among insurance-related features. However, note that one feature (55, scaled contribution to car policy) is chosen by all local solutions. This makes considerable sense, given the fact that the firm is soliciting households to buy insurance for recreational vehicles.

Other insurance-related features (scaled contribution to and ownership of boat (69, 90) and fire policy (67, 88)) are also chosen by multiple solutions. Demographic variables such as income levels (45, 50), home ownership (39), and jobs (farmer, 29) are also selected by few solutions. In general, the results are in line with marketing science work on customer segmentation, which shows that information about current purchase behavior is most predictive of future choices [39]. We refer to our previous work [26] for readers who are interested in building a potentially valuable profile of likely customers.

![](/api/attachments/HCZ2W8VM/fulltext/images/a7a7164c0a24cb4ec9c635a1d815cd94733181a13a8d3cab36f172c9a9410fea.jpg)  
Fig. 4. Hit rates of GA/ANN and single ANN model on the evaluation data. The differences are statistically significant (a =0.05) at six target points (i = 10, 20, 40, 50, 60, 80).

Table 2  
Chosen features by local solutions

<table><tr><td>Local solution</td><td>Feature index</td><td>Local solution</td><td>Feature index</td></tr><tr><td> $best_{10}$ </td><td>26, 39, 52, 55, 67, 90</td><td> $best_{50}$ </td><td>29, 39, 55, 80, 90, others</td></tr><tr><td> $best_{20}$ </td><td>54, 55, 67, 69, 90</td><td> $best_{60}$ </td><td>8, 30, 55</td></tr><tr><td> $best_{30}$ </td><td>40, 50, 55, 69, 88</td><td> $best_{70}$ </td><td>29, 45, 55</td></tr><tr><td> $best_{40}, best_{90}$ </td><td>55, 88</td><td> $best_{80}$ </td><td>8, 45, 55</td></tr></table>

In terms of data reduction, all local solutions choose at most six features except one that chooses 26 features at target point i = 50. On average, local solutions choose six features, which reduces the data dimensionality by $( 9 3 – 6 ) / 9 3 \approx 9 3 . 5 \%$ . This implies that the firm could reduce data collection and storage costs considerably. This is possible through reduced storage requirements, and the reduced labor and data transmission costs.

## 4.2.2. Sensitivity analysis

In this section, we focus on the decision support functionality of the Ensemble solution. In particular, we want to show how our Ensemble solution can be used to select the best target point where the expected profit is maximized. We consider two different marketing strategies: one case targeting customers with a nice-looking brochure of higher cost per mailing (US\$7) and the other case using a plain letter of lower cost per mailing (US\$0.71).<sup>3</sup> However, we make two common assumptions for both cases that the marginal revenue per buyer is US\$70 and the firm has a list of 1 million prospects to target. We show our experimental results in Fig. 5.

In order to choose the best target point, we compute the expected profits over different target points using the estimated hit rates of Ensemble on the training data. When the cost per mailing is not expensive (US\$0.71), our Ensemble returns the maximized expected profit when the best 80% of customers in the evaluation set are targeted. This makes sense because it is wise to target as many customers as possible up to a certain point. Once we determine the target point i, we can compute the expected profits of three different models when we target the top i% of 1 million prospects. Though all models return positive profits, the Ensemble solution returns the maximum profit.

![](/api/attachments/HCZ2W8VM/fulltext/images/5ead378b2ee7b4f5de301f1e48e2e12a7d440a3f7878700a1aa784ce8ac9b8ee.jpg)

![](/api/attachments/HCZ2W8VM/fulltext/images/757ef5cd2ac60b4cb7a5d1fe28c938f9b06dfb4a2834cc28a84b058ccc965641.jpg)

Model selection based on the expected net profit(\$)  
![](/api/attachments/HCZ2W8VM/fulltext/images/4a079e144efb320afdf709e89eac80432690a12ac776f3e0726b80f98d8f68b7.jpg)

![](/api/attachments/HCZ2W8VM/fulltext/images/7078dc7014eb931149fdcadf07095214f714c0666afeeb3d4abd81a2b2c2896c.jpg)  
Fig. 5. The selection of the best target point and the estimation of expected profit of market campaign using Ensemble on the evaluation data. The two figures at the top panel show results when the cost per mailing is US\$0.71. The other two figures at the bottom are results when the cost per mailing is US\$7.

When the cost per mailing is expensive (US\$7), the best target point is i = 10 in terms of maximized profit. This time, random targeting returns a negative profit as we target the best 10% of customers because of the increased mailing cost. The Ensemble solution returns the highest expected profit followed by the single ANN solution. Note that a market manager can select the best target point at i = 40 when her main interest is not in maximizing the expected profit but in increasing the market share while recovering at least the campaign costs. This is particularly useful when marginal revenue per customer and/or mailing cost information is not known as in our case.

## 5. Related work

Various multivariate statistical and analytical techniques in marketing community have been applied to the database marketing problem. Routine mailings to existing customers are typically based upon the RFM (recency, frequency, monetary) approach that targets households using knowledge of the customer’s purchase history [40]. However, the RFM model has major disadvantages including its limited applicability to current customers only and redundancy because of inter-dependency among RFM variables. Mailings to households with no prior relationship with the firm are based upon the analysis of the relationship between demographics and the response to a test mailing of a representative household sample. A brief summary of other traditional models such as Chi-square Automatic Interaction Detection (CH-AID), multiple regression methods, discriminant analysis, and gains chart analysis can be found in [8,20].

A more elaborate model for identifying optimal targets was presented by Bult and Wansbeek [8]. Their profit maximization (PM) approach is mainly based on the gains chart model [3] in a single period campaign. In their model, only those prospects whose expected return is higher than the marginal cost of the mailing are selected for direct mailing. From a comparative experiment on a real data set, they reported improved performance compared to CH-AID and the gains chart model. Bitran and Mondschein [6] presented a stochastic model to determine the optimal mailing frequency and assumed that multiple mailings would result in only one response.

Go¨nu¨l and Shi [19] presents a Markov decision model for the optimal mailing policy over an infinite period. In their model, two different objectives from both customers (maximizing utility) and direct mailers (maximizing profit) are optimized simultaneously. Their model utilized the estimated impact of recency and frequency on the customer’s response probability, and showed significantly improved performance over a single-period model. However, their recency- and frequency-based model cannot be applied to a certain types of commodities (e.g. seasonal goods). Further, their model can be computationally expensive once monetary value is added in the state definition.

Piersma and Jonker [33] studied a problem for optimizing the frequency for the direct mailing over a long-term but finite campaign horizon. Their model is simpler than [19] because of finite campaign horizon considered, but more general than [6] in the sense that they allow multiple responses to multiple mailings. Through comparative experiments on a data set from Dutch charitable organization, they showed that their model significantly increased the customer profitability and reduced wasteful mailings. Other models for direct marketing include a split-hazard model for estimating a physician’s propensity of using new drug in [24] and a latent trait and a latent class model for cross-selling of financial services in [23,25].

Researchers from the machine learning and datamining community have developed models without making prior assumptions about data distribution. Problems for effectively profiling users have been studied in [9,14,36]. Fawcett and Provost [14] presented a model for detecting fraudulent usage of cellular calls. Chan and Stolfo [9] presented a costsensitive model for detecting fraudulent usage of credit cards. Noting that the original distribution can be different from the desired distribution for optimal training, they divided a given data set into subsets with the appropriate class distribution through preliminary experiments. They obtained their final model by combining multiple classifiers trained on different subsets and reported some success. In [36], a predictive profiling model was presented for profiling customers of an Internet service provider who are most likely to stop using internet service. In [29], difficulties encountered in the process of applying data mining techniques to direct marketing were discussed.

A more relevant response model for direct mail campaigns can be found in [4]. In [4], Bhattacharyya proposed a GA-based approach for developing optimal models at different target points. In his framework, each candidate solution was expressed as a linear combination of the input variables and was evaluated in terms of two evaluation criteria— response rate and robustness. He further analyzed tradeoffs of multiple objectives by varying weights assigned to multiple criteria at different target points. He reported significantly improved performance over the traditional logit regression model at the first few target points. Recent works [5,27] studied the same problem in a Pareto optimization framework, where multiple criteria are not combined but considered independently in order to avoid a subjective weighting scheme.

In [32], the profitability condition of a campaign was explicitly formulated as a function of the lift of the model, uniform campaign cost per mailing, and marginal revenue per identified positive record. A brief review of evaluation metrics for marketing campaigns can be found in [38]. They also provided heuristics to estimate the expected profit from targeting a subset of records without going through a lengthy data mining process. Chou et al. [11] devised an effective model for identifying prospective insurance buyers when buyer versus non-buyer information is not available. Gersten et al. [17] presented a model to select prospects in the automotive industry where the buying decision takes a long time.

Domingos and Richardson [13] view a market as a social network where each customer has a different network value, influence on other customers’ probability of buying a product. The network value of a customer in their model is computed as the expected profit from additional sales to customers whom she recursively influences to buy. Considering network effects can change optimal marketing strategy dramatically. For example, it is worth marketing to one whose intrinsic value is lower than the cost of marketing when her influence on others’ purchasing decision is strong. From several experiments on a publicly available data (www.research.compaq.com/src/eachmovie/), they not only reported superior performance to traditional direct marketing strategy but also profiled good customers to target.

## 6. Conclusion

In this paper, we presented a novel approach for customer targeting in database marketing. We used a genetic algorithm to search for possible combinations of features and an artificial neural network to score customers. One of the clear strengths of the GA/ANN approach is its ability to construct predictive models that reflect the direct marketer’s decision process. In particular, with information of campaign costs and profit per additional actual customer, we show that our system not only maximizes the hit rate at fixed target point but also selects a ‘‘best’’ target point where expected profit from direct mailing is maximized. Further, our models are made easier to interpret by using smaller number of features.

In future work, we will look into a customer targeting model that assumes the heterogeneous structure of marginal revenue per each prospect. The data set we analyzed in this paper does not include critical information such as monetary values that each customer spent to purchase a caravan insurance policy. It is also reasonable to assume that there is relatively small difference in terms of monetary values in insurance options available to customers. However, assume the case that a non-profit organization sends solicitation letters to possible donors for charity. For this organization, maximizing the total amount of donated money is more important than identifying as many donors as possible. This is because, in an extreme case, single donor can donate more money than all the other donors. In this case, value-based customer targeting becomes critical. By considering raised monetary value by targeted customers as one objective, our GA/ANN model will be able to find an optimal solution with maximized monetary value.

Related to this direction of research, it is interesting to see if a bi-level model that has two separate procedures, one for estimating donation probability and the other for estimating donation amounts, can do better. It was claimed that any single classifier model that learns two parameters is likely to make more errors in learning decision rules than a bi-level model [43].

Another research direction is to investigate whether or not the chosen feature subsets are related with target points. Our experimental results in Section 4.2.1 show that different feature subsets are chosen at different target points except for a few common features. We expected a good predictive subset of features to appear in most of the local solutions. We suspect that a certain subset of features can discriminate well buyers from non-buyers at a target point, but not as well as other features at different points. It could also happen because of strong correlation among insurance-related features. However, it warrants further investigation to support our speculation.

## Acknowledgements

The authors wish to thank Peter van der Putten and Maarten van Someren for making the CoIL data available for this paper. This work is partially supported by NSF grant IIS-99-96044.

## References

[1] S.C. Ahalt, A.K. Krishnamurthy, P. Chen, D.E. Melton, Competitive learning algorithms for vector quantization, Neural Networks 3 (1990) 277–290.

[2] P.V.S. Balakrishnan, M.C. Cooper, V.S. Jacob, P.A. Lewis, Comparative performance of the FSCL neural net and K-means

algorithm for market segmentation, European Journal of Operation Research 93 (10) (1996) 346– 357.

[3] J. Banslaben, Predictive modeling, in: E.L. Nash (Ed.), The Direct Marketing Handbook, McGraw-Hill, New York, NY, 1992, pp. 626– 636.

[4] S. Bhattacharyya, Direct marketing response models using genetic algorithms, Proc. of 4th Int’l Conf. on Knowledge Discovery and Data Mining (KDD-98), ACM, New York, NY, 1998, pp. 144 – 148.

[5] S. Bhattacharyya, Evolutionary algorithms in data mining: multi-objective performance modeling for direct marketing, Proc. of 6th ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-00), ACM, New York, NY, 2000, pp. 465 – 473.

[6] G.R. Bitran, S.V. Mondschein, Mailing decisions in the catalog sales industry, Management Science 42 (1996) 1364– 1381.

[7] L. Breiman, Bagging predictors, Machine Learning 24 (2), Kluwer, Dordrecht, The Netherlands (1996) 123 – 140.

[8] J.R. Bult, T. Wansbeek, Optimal selection for direct mail, Marketing Science 14 (4) (1995) 378 – 394.

[9] P.K. Chan, S.J. Stolfo, Toward scalable learning with nonuniform class and cost distributions: a case study in credit card fraud detection, Proc. of 4th ACM SIGKDD Int’l. Conf. on Knowledge Discovery and Data Mining (KDD-98), ACM, New York, NY, 1998, pp. 164–168.

[10] S. Chen, C. Guerra-Salcedo, S. Smith, Non-standard crossover for a standard representation—commonality-based feature subset selection, GECCO-99: Proc. of the Genetic and Evolutionary Computation Conference, Morgan Kaufmann, 1999, pp. 129 – 134.

[11] P.B. Chou, E. Grossman, D. Gunopulos, P. Kamesam, Identifying prospective customers, Proc. of 6th Int’l Conf. on Knowledge Discovery and Data Mining, ACM, New York, NY, 2000, pp. 447– 456.

[12] F. Coetzee, E. Glover, S. Lawrence, C.L. Giles, Feature selection in web applications using ROC inflections, Symposium on Applications and the Internet, SAINT, San Diego, CA, 2001, pp. 5 –14.

[13] P. Domingos, M. Richardson, Mining the network value of customers, Proc. of 7th ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-01), ACM, New York, NY, 2001, pp. 57 – 66.

[14] T. Fawcett, F. Provost, Combining data mining and machine learning for effective user profiling, Proc. of 2nd ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-96), ACM, New York, NY, 1996, pp. 8 – 13.

[15] Y. Freund, R. Schapire, Experiments with a new boosting algorithm, Proc. of 13th Int’l Conf. on Machine Learning, Bari, Italy, IEEE, Los Alamitos, CA, 1996, pp. 148 – 156.

[16] I. Gath, A.B. Geva, Unsupervised optimal fuzzy clustering, IEEE Transactions on Pattern Analysis and Machine Intelligence 11 (7) (1988) 773 – 781.

[17] W. Gersten, R. Wirth, D. Arndt, Predictive modeling in automotive direct marketing: tools, experiences and open issues, Proc. of 6th Int’l Conf. on Knowledge Discovery and Data Mining, ACM, New York, NY, 2000, pp. 398–406.

[18] D.E. Goldberg, Genetic Algorithms in Search, Optimization

and Machine Learning, Addison-Wesley, New York, MA, 1989.

[19] F. Go¨nu¨l, M.Z. Shi, Optimal mailing of catalogs: a new methodology using estimable structural dynamic programming models, Management Science 44 (9), INFORMS, Linthicum, MD (1998) 1249– 1262.

[20] P.E. Green, D.S. Green, Research for Marketing Decisions, 5th ed., Prentice-Hall, Englewood Cliffs, NJ, 1988.

[21] H. Hruschka, M. Natter, Comparing performance of feedforward neural nets and K-means for market segmentation, European Journal of Operational Research 114, Berlin, Heidelberg (1999) 346–353.

[22] D.D. Jensen, P.R. Cohen, Multiple comparisons in induction algorithms, Machine Learning 38 (3) (2000) 309 – 338.

[23] W.A. Kamakura, S.N. Ramaswami, R.K. Srivastava, Applying latent trait analysis in the evaluation of prospects for crossselling of financial services, International Journal of Research in Marketing 8, Elsevier, Amsterdam, The Netherlands (1991) 329– 349.

[24] W.A. Kamakura, B.S. Kossar, A factor analytic split-hazard model for database marketing, Tech. Rep. 98-12-009, Department of Marketing, University of Iowa, Iowa, IA, 1998.

[25] W.A. Kamakura, F. de Rosa, M. Wedel, J.A. Mazzon, Crossselling financial services with database marketing, unpublished working paper, University of Iowa, Iowa, IA (2000).

[26] Y. Kim, W.N. Street, CoIL challenge 2000: Choosing and explaining likely caravan insurance customers, Tech. Rep. 2000 – 09, Sentient Machine Research and Leiden Institute of Advanced Computer Science, Leiden University, The Netherlands, http://www.wi.leidenuniv.nl/putten/library/cc2000/ (2000 June).

[27] Y. Kim, W.N. Street, G.J. Russell, F. Menczer, Customer targeting: a neural network approach guided by genetic algorithms, Management Science, under revision.

[28] M. Kudo, J. Sklansky, Comparison of algorithms that select features for pattern classifiers, Pattern Recognition 33 (2000) 25– 41.

[29] C.X. Ling, C. Li, Data mining for direct marketing: problems and solutions, Proc. of 4th ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-98), ACM, New York, NY, 1998, pp. 73 – 79.

[30] S.M. Mahfoud, Niching methods for genetic algorithms, PhD thesis, Department of General Engineering, University of Illinois at Urbana-Champaign, Champaign, IL, 1995.

[31] S. Murthy, S. Salzberg, Lookahead and pathology in decision tree induction, in: C.S. Mellish (Ed.), Proc. of 14th Int’l Joint Conf. on Artificial Intelligence, Morgan Kaufmann, San Francisco, CA, 1995, pp. 1025 – 1031.

[32] G. Piatetsky-Shapiro, B. Masand, Estimating campaign benefits and modeling lift, Proc. of 5th ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-99), ACM, New York, NY, 1999, pp. 185 – 193.

[33] N. Piersma, J. Jonker, Determining the direct mailing frequency with dynamic stochastic programming, Tech. Rep. EI2000-34A, Econometric Institute, Erasmus University, Rotterdam, Netherlands, 2000.

[34] F. Provost, T. Fawcett, Robust classification systems for

imprecise environments, Proc. of 15th National Conf. on Artificial Intelligence (AAAI-98), IEEE, Piscataway, NJ, 1998, pp. 706 – 713.

[35] J.R. Quinlan, R.M. Cameron-Jones, Oversearching and lay ered search in empirical learning, Proc. of 14th Int’l Joint Conf. on Artificial Intelligence, Morgan Kaufmann, San Francisco, CA, 1995, pp. 1019– 1024.

[36] N. Raghavan, R.M. Bell, M. Schonlau, Defection detection, Proc. of 6th Int’l Conf. on Knowledge Discovery and Data Mining, ACM, New York, NY, 2000, pp. 447 – 456.

[37] M. Riedmiller, Advanced supervised learning in multi-layer perceptrons—from backpropagation to adaptive learning algorithms, International Journal of Computer Standards and Interfaces 16 (5), Elsevier, Amsterdam, The Netherlands (1994) 265– 278.

[38] S. Rosset, E. Neumann, U. Eick, N. Vatnik, I. Idan, Evaluation of prediction models for marketing campaigns, Proc. of 7th ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-01), ACM, New York, NY, 2001, pp. 456–461.

[39] P.E. Rossi, R. McCulloch, G. Allenby, The value of household information in target marketing, Marketing Science 15 (3) INFORMS, Linthicum, MD (1996) 321 – 340.

[40] J. Schmid, A. Weber, Desktop Database Marketing, NTC Business Books, NTC Businness Books, Lincolnwood, IL, 1998.

[41] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowl edge management and data mining for marketing, Decision Support Systems 31 (1) Elsevier, Amsterdam, The Netherlands (2001) 127– 137.

[42] J. Yang, V. Honavar, Feature subset selection using a genetic algorithm, IEEE Intelligent Systems & their Applications 13 (2) Elsevier, Amsterdam, The Netherlands (1998) 44 – 49.

[43] B. Zadrozny, C. Elkan, Learning and making decisions when costs and probabilities are both unknown, Proc. of 7th ACM SIGKDD Int’l Conf. on Knowledge Discovery and Data Mining (KDD-01), ACM, New York, NY, 2001, pp. 204 – 213.

![](/api/attachments/HCZ2W8VM/fulltext/images/b185e9643aa42998b73403a1177b52e3b4d1abfc6f771cb0a739db3c52d08cf7.jpg)

Dr. YongSeog Kim is an Assistant Professor in Business Information Systems department at the Utah State University. He received his MS degree in Computer Science and PhD in Business Administration from the University of Iowa. Dr. Kim’s primary research area is data mining including feature selection, clustering, ensemble methods, streaming data analysis, and spatial and temporal data analysis. Recently, he becomes interested in applying data mining

algorithms to solve some business problems in customer targeting, e-commerce, and computational finance and economics. His other research interests include digital government, electronic books, and computer – human interface.

![](/api/attachments/HCZ2W8VM/fulltext/images/6b0663d401e3ee8b14c9fd62704da59e86fd1bdcb5f72a671b3569fdf4dad33f.jpg)

Dr. Nick Street is an Associate Professor in the Management Sciences Department at the University of Iowa. He received a PhD in 1994 in Computer Sciences from the University of Wisconsin. His research interests are in machine learning and data mining, particularly the use of mathematical optimization in inductive learning techniques. His recent work has focused on dimensionality reduction (feature selection) in high-dimensional data for both classifi-

cation and clustering, ensemble prediction methods for massive and streaming data sets, and learning shapes for image segmentation, classification, and retrieval. He has received an NSF CAREER award and an NIH INRSA postdoctoral fellowship.
