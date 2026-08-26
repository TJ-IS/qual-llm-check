---
otero_id: 19740
otero_key: "VETJ5U8B"
title: "Modeling relationships between retail prices and consumer reviews: A machine discovery approach and comprehensive evaluations"
authors: "Xian Yang; Guangfei Yang; Jiangning Wu; Yanzhong Dang; Weiguo Fan"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113536"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling relationships between retail prices and consumer reviews: A machine discovery approach and comprehensive evaluations

![](/api/attachments/VETJ5U8B/fulltext/images/1c6a405eb3d651511763b8e7f314cfbdc877d3c7c2a1f7196908a47552cb09b6.jpg)

Xian Yang <sup>a</sup>, Guangfei Yang <sup>b,\*</sup>, Jiangning Wu <sup>b</sup>, Yanzhong Dang <sup>b</sup>, Weiguo Fan <sup>c</sup>

<sup>a</sup> School of Management Science and Engineering, Dongbei University of Finance and Economics, Dalian, Liaoning, China

<sup>b</sup> School of Management Science and Engineering, Dalian University of Technology, Dalian, Liaoning, China

<sup>c</sup> Department of Management Sciences, Tippie College of Business, University of Iowa, Iowa City, IA, United States

## A R T I C L E I N F O

Keywords: Consumer reviews Retail price Data-driven Machine learning Genetic programming Product involvement

## A B S T R A C T

Setting the retail price as a part of marketing would affect customers' cognition regarding products and affect their post-purchase behavior of review writing. To deeply understand the relationships between retail prices and reviews, this paper designs an intelligent data-driven Generate/Test Cycle using a machine learning technique to automatically discover the relationship model from a huge amount of data without a prior hypothesis. From a unique dataset, various free-form relationship models with their own structures and parameters have been discovered. By the comprehensive evaluations of candidate models, a guided map was offered to understand the relationship between dynamic retail prices and the volume/valence of reviews for different types of products. Experimental results show that 37.69% of products in our sample exhibit the following trend: When the price is increased to a certain level, the volume of reviews shifts from a decreasing trend to an increasing trend. Results also demonstrate that a linearly increasing relationship model between prices and the valence of reviews is more suitable for the low-involvement products than for the high-involvement products. In addition to the new findings, this research provides a powerful tool to assist domain experts in building relationship models for decision making in a highly efficient manner.

## 1. Introduction

Word-of-mouth (WOM) plays a significant role in influencing con sumers’ attitudes and purchase decisions [1,2]. The popularity of online retailer websites enables consumers to post reviews on products and services, which act as a good proxy for electronic WOM with a high degree of credibility [3]. A survey conducted by Dimensional showed that an overwhelming 90% of respondents, who recall reading online reviews, claim that positive online reviews influence their buying de cisions [4]. A report from Harvard Business Review found that a one-star increase in Yelp rating led to a 5%–9% increase in revenue [5]. These data suggest that consumer reviews have a significant impact on others purchase decisions and retail companies’ revenues.

Marketing tools price is an important decision variable in marketing for a product and can affect customers’ cognition, feelings [6], purchase decisions, and post-purchase satisfaction [7]. Previous research also found that the price could affect the consumer reviews [8,9]. The online retailers are able to adjust their prices more frequently and easily compared to physical retail stores. A survey estimated that Amazon changes retail prices more than 2.5 million times daily for its millions of products.<sup>1</sup>

In this vein, a fundamentally important question to ask is as follows: What effects can be observed regarding volume and valence of consumer reviews after increasing or decreasing the retail price for a specific product? In this study, volume measures the total amount of reviews posted on a product and is an important cue for product popularity [10]. Valence (i. e., star rating) captures the positive or negative nature of reviews, which contains evaluation information on product quality. To answer this question, computable models for describing relationships between pri ces and volume/valence of reviews should be built.

Previous researcher have found that the price has a direct or indirect effect on consumer reviews because of intermediate factors, such as sales, satisfaction [11], loyalty [12,13], and biased acquisition [14]. However, these intermediate factors exist concurrently, making them difficult to disentangle. An open problem remains: Relationships be tween retail prices and consumer reviews are unclear. A handful of studies have attempted to understand the relationship between market price and consumer reviews. Chen et al. (2011) [8] found a U-shaped relationship between market price and volume of reviews and no sig nificant relationship between market price and valence of reviews at mature stages of Internet use based on the automobile-model data, and Li and Hitt (2010) [9] found that market average price has a significant negative effect on the valence of reviews based on the digital camera data.

These studies have been performed at the macro (market) level by employing market price,<sup>2</sup> in other words, a constant average of market prices for all products at an aggregate level. Moreover, in that research, consumer reviews and prices were collected from different websites, and the price was not the real transactional price. As a result, their findings might not help understand the nuances of relationships between product prices and consumer reviews. A variety of information sources are very coarse in revealing the relationships between prices and reviews because each review has not been associated with the price at which the con sumer bought the product. Because the transaction price corresponding to a review is difficult to obtain, relationship searching is difficult.

Fortunately, we obtained a unique data set from an online retailer that comprised 321 types of products with retail prices and corre sponding reviews. According to statistics, prices changed 5431 times during the period of data collection, and 1,738,114 pieces of reviews were crawled in the same period. For model building, the traditional paradigm often depends on a Generate/Test Cycle [15,16]. Such cycles begin with observations of the data, and then hypotheses are generated and tested against the data. Eventually, promising models are produced. This paper designs a new data-driven Generate/Test Cycle to automat ically discover relationship models by using machine learning tech niques. Unlike the traditional paradigm by domain experts to generate alternatives and test them against constraints, the proposed approach develops a mechanism to automatically learn the structures and pa rameters of models from data, without prior hypothetical forms pro vided by domain experts. The key is an intelligent model discovery method based on genetic programming (GP) [17], which has demon strated its capability successfully in various fields to discover functions, for example, relationship functions [18,19] and ranking functions [20,21].

Thus, in this paper, the GP method as an intelligent tool is introduced to exploit functional relationships between retail prices and consumer reviews from a large and unique data set. Experimental results show that for the relationships between retail prices and volume of reviews, three types of models demonstrate the best performance: the linearly decreasing, asymmetric U-shaped, and asymmetric inverted U-shaped model. For the relationships between retail prices and valence of re views, the promising models are the linearly decreasing, asymmetric inverted U-shaped, and linearly increasing model.

Nevertheless, none of the models dominate all the others on the basis of three evaluation metrics: fitness, complexity, and coverage. For example, for the relationships between retail prices and volume of re views, the linearly decreasing models feature high coverage, low complexity, and low fitness, whereas the asymmetric U-shaped model features low coverage, high complexity, and high fitness. Instead of simply suggesting on model, comprehensive evaluations have been conducted to examine the performance of each candidate model in various categories of products to show its comparative advantages and disadvantages. The experimental results provide detailed references for the application of relationship models, such as which model is more suitable for a product or how to choose another model to complement this model when it does not model the relationship under a certain metric.

The research in this paper makes the following contributions.

• A novel data-driven Generate/Test Cycle using a machine learning technique, namely, GP, was designed to automatically discover feasible models to express the relationships between prices and re views. This type of research demonstrates an alternative modeling method in information systems research that could greatly improve modeling efficiency.

• Research on the impact of vendor marketing strategies on usergenerated content (UGC) was extended. More specifically, based on the unique datasets, our research is the first to model the relation ships between retail prices and consumer reviews for one product at the individual level. It could be more useful for marketers to perform marketing activities precisely and cost-effectively regarding the product.

• Empirical findings and a guided map were offered to understand the relationship between dynamic retail prices and the volume/valence of consumer reviews by using the comprehensive evaluations of the candidate models. This method advances empirical research in in formation system field.

The remainder of the paper is organized as follows. In Section 2, we provide related research. In Section 3, we first introduce the framework and then illustrate the method. Furthermore, we use a Monte Carlo simulation to validate the proposed method. In Section 4 and 5, we describe the data and elaborate on the results. Finally, we discuss the findings in Section 6 and conclude our paper in Section 7.

## 2. Related research

## 2.1. Relationship between price and consumer reviews

Previous research has found that price affects volume and valence of consumer reviews through various mediating factors, such as sales, satisfaction [11], loyalty [12,13], and biased acquisition [14]. First, consumer reviews can be posted on an e-commerce website only after purchase. More sales could possibly lead to more reviews and vice versa. Price affects sales and is ultimately reflected in volume of consumer reviews. In addition, when facing quality uncertainty, consumers are likely to use price as a signal of expected quality [22], whereas dis confirmation of an expectation of perceived quality influences consumer satisfaction [11]. Researchers have found that satisfaction is the main driver of posting reviews, and consumers who experience extreme satisfaction or dissatisfaction exhibit a higher propensity to engage in writing reviews [23]. Therefore, the price may affect the perceived quality of products, which accordingly influences reviews in terms of their volume and valence. Price changes could also segment loyal and non-loyal consumers [12]. Loyal consumers have a greater propensity to generate consumer reviews [13]. Furthermore, price generally increases acquisition bias and inflates observed mean ratings [14]. However, these intermediate factors exist concurrently; it is rather difficult to confirm the relative importance of the factors, and the interaction of various factors is also intricate. Thus, the relationships between the prices and volume/valence of reviews will have multiple possible consequences

The research on the relationships between prices and of reviews has yielded inconsistent results. Chen et al. (2011) [8] found a U-shaped relationship between market price and volume of reviews and no sig nificant relationship between market price and valence of reviews at mature stages of Internet use based on automobile model data, and Li and Hitt (2010) [9] found that market price has a significant negative effect on the valence of reviews based on digital camera data. Re searchers have found that consumers prefer to engage more, such as by writing reviews, in high-involvement products to relieve tension [24].

These conflicting results imply that the relationship between mar keting price and volume/valence of reviews is complex and will be different for product categories. The aforementioned researchers have studied the relationships between market prices and reviews for all products at an aggregate level. According to our review of the literature, the relationship between dynamic retail prices and reviews for one product at an individual level remains unclear. Additionally, although the discovered relationships, such as the U-shaped model, have proven useful, they remain unverified in other product categories, and other more suitable models are unavailable. Thus, this paper focuses on research on the relationship between product retail price and volume/ valence of reviews for one product. Furthermore, we explore the various relationship models for different product categories.

## 2.2. Traditional model-driven model building

In traditional model-driven research, a relationship model usually refers to generalizations on the effects of marketing effort variables (e.g., price and advertising) on sales, market share, or brand [25]. Various relationship functions of sales and marketing effort variables have been observed, for example, the linear model, semi-logarithmic model, quadratic model, and exponential model.

Almost all these models have been designed by following a procedure that could be abstracted as the Generate/Test Cycle [15,16]: observe the data, assume the structure of the model, learn the parameters, and test the parameters against the constraints. To investigate the relationships between product prices and consumer reviews, a safe strategy is to follow the sophisticated cycle again.

However, model building is usually a time-consuming task, espe cially when managing the various data which comes with high velocity. The difficulty caused by the enormous data space and huge solution space in the modern ages, from the efficiency perspective, calls for a more efficient method, such as a computer-aided approach, to help domain experts search the data space and solution space intelligently.

## 2.3. Intelligent data-driven model building

The automation of science has been recently discussed to challenge the hypothetic-deductive method for scientific research and allow ma chines to contribute scientific knowledge [26]. Additionally, the ex plosion of digital data calls for the translation of data into improved decision-making [27].

There are two main means to apply intelligent data-driven model building. The first means is build black-box models to handle complex data and to improve the prediction or classification accuracy, by using support vector machines (SVM) [28] and neural network (NN) [29,30]. The second means is to build white-box models. Many achievements have demonstrated that the intelligent data-driven approach builds scientific function models with a performance comparable to that of domain experts.

For example, Fan et al. (2006, 2009) [20,21] discovered the ranking functions for information retrieval. Schmidt and Lipson (2009) [18] searched motion-tracking data from various physical systems to discover the laws of geometric and momentum conservation. Yoshihara et al. (2013) [31] determined a formula to predict tumour purity based on the ESTIMATE score. Chattopadhyay et al. (2013) [19] rediscovered the reactions underlving Gillespie's stochastic simulation de novo from observational data. Li et al. (2019) [32] analyzed the cluster relationship between carbon dioxide emissions and economic growth. These ap proaches have all been driven by data in an autonomous manner and share the same core methodology, that is, GP [17]. The intelligent datadriven approach could integrate the advantages of explicit models by incorporating closed-forms solutions and the advantage of implicit models by benefiting from computational power [18,19]. The structure and parameters of the model can be learned together simultaneously by machines.

However, in information system research, given the complexity and idiosyncrasy of human experience, vitalist metaphysics implies that no universal laws of causation are in the social world waiting to be discovered and harnessed through the scientific method [33]. That is, the relationship is not universal for all products at all times, and it will have various possibilities in different scenarios. For example, the re lationships between prices and consumer reviews could be described by multiple potentially applicable candidate models, and only a few uni versal models are applicable to all products. For different product cat egories, feasible relationship models could also differ. Thus, how to use the approach to discover feasible models for different product types is also a challenge.

## 3. Methodology

In this section, we present the methodology. We first describe the framework and then introduce the model searching and model selection. To validate the proposed method, a Monte Carlo simulation is performed to examine whether it could accurately discover the models

## 3.1. Framework

Good models are hard to find [34]. To find a good model, a classic method is to perform the Generate/Test Cycle by designing alternatives and testing them against constraints (Fig. 1). The traditional Generate/ Test Cycle explicitly determines the models by human researchers on the basis of their hypothetical solution space, which becomes an obstacle when discovering the model from the solution space with sheer size. For example, in the relationship between price and reviews in our research, there are many potentially applicable candidate models. The models should be tested with many products associated with frequent price changes and a huge amount of reviews on the selected retail website. Thus, generating and testing many candidate models by human re searchers would be time-consuming.

To overcome this obstacle, we propose a new approach to the Generate/Test Cycle by incorporating an artificial intelligent (AI) researcher (Fig. 2). Human experts do not have to perform the cycle to determine the proper models, and the AI researcher automatically sug gests alternatives to describe the relationships hidden in data. The new approach has two processing stages: model searching and model selec tion. In the model searching stage, it generates and tests the model by using GP for each subset of data corresponding to one product. In the model selection stage, it first selects the Pareto optimal models for the given products at the individual level, namely, local pruning. Next, it discovers the models with high coverage for all types of products at the group level, namely, global pruning.

The intelligent data-driven generating/testing approach can search for promising models from an extremely large solution space by means of its two-phase operations. The core of the approach is evolutionary algorithms GP with easy transferability, which identifies meaningful analytical links and distills free-form models from data [18].

## 3.2. Meta-model definition

To reveal the relationships between price changes and the volume/ valence of reviews, GP is adopted to automatically discover the math ematical model. The functional form expresses the nature of the relation, and the substantive meaning could be concretely made by some linear or nonlinear mathematical models. Following Bass’s recommendation of simplicity to describe a pattern [35], the fundamental relationship in terms of reviews and price is defined as follows:

$$
\text { REVIEWS } = f (\text { PRICE })\tag{1}
$$

By fundamental, we mean a pattern that repeats itself in multiple circumstances and can be described simply by mathematical functions. Identifying fundamental relationships is a critical pursuit of research [11,35]. Such a model is more likely to be generalizable and provides a starting point for further replication and extension of research.

![](/api/attachments/VETJ5U8B/fulltext/images/367f80827eec318f7209df124eb760be47a4f8001ba9fe11663660f23d54627c.jpg)  
Fig. 1. Traditional Generate/Test Cycle [revised from (Simon 1996 [15], Hevner et al. 2004 [16])]

![](/api/attachments/VETJ5U8B/fulltext/images/62868784613df107d5389e66c828448d49e7231038fd1d6dc26f1093d3d9575b.jpg)  
Fig. 2. New generate/test cycle.

Based on the basic model (1), the volume and valence of reviews have been seriously considered in this study, and their functional re lationships with prices are represented by the following formulas (2) and (3):

$$
R _ {i t} ^ {v o} = f _ {i t} ^ {v o} \left(P _ {i t}\right)\tag{2}
$$

$$
R _ {i t} ^ {v a} = f _ {i t} ^ {v a} \left(P _ {i t}\right)\tag{3}
$$

where $P _ { i t }$ denotes the price for a product i for t period; $R _ { i t } ^ { \nu o }$ and $R _ { i t } ^ { \nu a }$ respectively, denote the volume and the valence of reviews regarding the $P _ { i t } .$ Formulas (2) and (3) can be the meta-models for GP by which more relationship models with regard to the given data can be explored.

## 3.3. Model searching by Using GP

GP is the variant of the genetic algorithm with tree structure encoding and could be applied as a function discovery approach to analyze a multivariate dataset [17]. GP explores the solution space by combining building blocks from a set of mathematical operators and operands (e.g., variables and constants) and searching the space of the mathematical expressions to find the model that best fits a given dataset.

GP inherits the evolutionary features of genetic algorithm and, in theory, can manage global optimization with a high probability.

In GP, a candidate solution is encoded as a tree structure. The flowchart of GP is shown in Fig. 3. There are several procedure. First, initialize the population. We select a set of primitive functional opera tors and variables to integrate into the mathematical models to express the intrinsic relationship. The functional operators commonly used in relationship models include addition (+), subtraction (− ), multiplica tion (×), exponential (exp), natural logarithm (ln), variable and con stant. Second, calculate the fitness of the model until the terminal condition is satisfied. The fitting accuracy of the corresponding model is measured by the R-squared value. Last, the structures and parameters of models are evolved by genetic operators, such as reproduction, cross over and mutation (Fig 4) Reproduction is used to select better in: dividuals into the next generation directly. Crossover is used to exchange parts of two individuals and generate two new individuals. Mutation is used to alter a small portion of one individual randomly. Genetic operators generate new individuals. The configuration of the GP used for function discovery is in Table 1. The computational time in our research is 1000 s, at this point the results have converged.

By using GP, it returns many candidate models. To evaluate each model, two measures are defined in this paper: fitness and complexity. The fitness of model i is measured by the R-squared value:

![](/api/attachments/VETJ5U8B/fulltext/images/9491c6c18b8879d84b5cba72b447446325f07864e762947ee12ac99a6d9f864f.jpg)  
Fig. 3. Flowchart of GP.

$$
R _ {i} ^ {2} = 1 - \frac {\sum \left(Y _ {i} - \widehat {Y} _ {i}\right) ^ {2}}{\sum \left(Y _ {i} - \overline {{Y}} _ {i}\right) ^ {2}}\tag{4}
$$

where $Y _ { i }$ is the observed value, $\widehat { Y } _ { i }$ is the predicted value from the model, and $\overline { { Y } } _ { i }$ is the average observed value. The complexity of model i is signified by Comp :

$$
\operatorname{Comp} _ {i} = \sum_ {j = 0} ^ {n} \operatorname{compOfOpr} _ {i j}\tag{5}
$$

where n is the number of all functional operators in model i, and com $p O f O p r _ { i j }$ is the complexity of the jth functional operator in model i. The complexities for the functional operators: $+ , - , \times ,$ , exp, ln, variable, and constant are 1, 1, 1, 4, 4, 1, and 1, respectively.

## 3.4. Model selection

Because GP returns a huge number of candidates, model selection plays a key role in pruning the less-promising candidates. Two steps for pruning are designed: local pruning and global pruning. The main principle of local pruning is to select the Pareto optimal models by considering their complexity and fitness based on Occam’s razor [38], and the global pruning considers the coverage of the selected models.

After pruning, the models with low complexity, high fitness and coverage remain for further analysis.

The local pruning is performed by that for a specific complexity level, and only the model with maximal fitness is selected:

$$
\min (e r r o, C) = \min \bigl (\bigl (1 - R ^ {2} \bigr), C \bigr)\tag{6}
$$

Such a selection leads to a limited number of models for the tradeoff between error and complexity on a Pareto front.

Global pruning is performed to eliminate the less frequently appearing model when considering the whole data sets, and each data set corresponds to one product in our research. After local pruning, all the Pareto optimal models can be collected, and the coverage value of each model structure can be counted. By ranking all the models by coverage, the top k models are selected for further analysis. The coverage of model i, denoted by Cove , indicates the proportion of the products that the corresponding model fits and is measured by

$$
Cove_{i} = \frac{n_{i}}{m}\times 100\%\tag{7}
$$

where m is the number of products, and $n _ { i }$ is the number of products that model i is selected for.

## 3.5. Method validation by Monte Carlo simulation

## 3.5.1. Model discovered by GP

The research question of this paper is about discovering the rela tionship between retail prices and reviews, which is an unsupervised learning approach without a labelled training set. Thus, to validate whether GP with model selection method can discover the underlying model in data accurately, Monte Carlo simulation is conducted. The data are seeded from models with predefined structures and parameters and mixed with various levels of noise. GP with model selection method is applied to discover models from the data, and its performance is then measured by whether the correct structures and parameters are found.

There are two types of model seeds: one model is linear (e.g., Eq. 8), and the other model is quadratic (e.g., Eq. 9).

$$
y = a - b x,\tag{8}
$$

Table 1  
Components of function discovery using GP.

<table><tr><td>Components</td><td>Values</td></tr><tr><td>Terminals</td><td> $P_{it}$ .</td></tr><tr><td>Functional operators</td><td>+, -, ×, exp, ln.</td></tr><tr><td>Fitness function</td><td>R-squared</td></tr><tr><td>Genetic operators</td><td>Reproduction, Crossover, Mutation.</td></tr></table>

![](/api/attachments/VETJ5U8B/fulltext/images/3bc2c5b4de3613fbb189774033492c650a86fd7dab62d38fa1611c7730c7b715.jpg)  
Fig. 4. Genetic operations in symbolic regression.

$$
y = a + b x ^ {2} - c x\tag{9}
$$

The sample size of each data set is randomly chosen, and the range is 10 to 50. For each sample, the variables x and y are generated as follows:

$$
x _ {i} \leftarrow r a n d (x _ {\min}, x _ {\max})\tag{10}
$$

$$
y (x _ {i}) \leftarrow y (x _ {i}) ^ {*} (1 + \theta^ {*} r a n d (- 1, 1))\tag{11}
$$

x is generated from a uniform distribution within the range of (x , $x _ { \mathrm { m a x } } ) . y$ is disturbed by a random noise factor $( 1 + \theta ^ { * } r a n d ( - 1 , 1 ) )$ , where parameter θ controls the noise level. The parameter θ is defined over four levels: 5%, 10%, 30%, and 50%. With higher noisy level, the generated data will be deviated more randomly, which makes it more difficult to discover the true underlying model. There are 24 sets of data generated from six model seeds (Table 2), and 2400 datasets are generated in total for all θ.

We first determine whether the true structure of the models could be discovered by applying the methods. In Fig. 5, the best structures are listed after pruning. The best model structure discovered by our approach is exactly the true structure for the given seed, which shows overwhelming coverage value. Detailed information on the best and the second-best structures are compared in Table 3. For all simulations, the true structures emerged from candidates with a dominant performance. In other words, the true structures of models could be discovered accurately by using our approach.

The estimation of a parameter is also evaluated by calculating the mean absolute percentage error (MAPE):

$$
\mathrm{MAPE} = \frac {\left| E s i m a t e d V a l u e - T r u e V a l u e \right|}{T r u e V a l u e} \times 100 \%\tag{12}
$$

The MAPE for parameters a, b, and c are 1.68%, 2.25%, and 2.28%, respectively, and the overall MAPE is 1.87% (Table 4). The errors of estimation are all very small, which indicates that the parameters of models could be learned accurately. In summary, the Monte Carlo simulations prove that our approach can discover the structures and parameters for models precisely.

## 3.5.2. Comparison with neural network

We used the neural network (NN) as a baseline for comparison with genetic programming (GP). The greatest difference between GP and NN is model interpretability. A NN often requires many weights, especially for nonlinear models. Based on the perceptron with a nonlinear acti vation function, although the NN can approximate a mathematical function, it is rather complicated and difficult to explain the relationship between variables. To compare the results of the two methods, we use the model $y = 2 1 , 2 0 0 \ + \ 0 . 0 5 \ \times \ ^ { 2 } { \cdot } 6 5 \times$ and randomly generate 10 datasets from the model, with a 10% level of noise mixed. Both an NN and GP are applied to discover models from the data. The experimental results of the NN and GP are shown in Table 5 and Table $^ { 6 , }$ respectively.

The structure of the NN model, including the number of hidden layers, the number of hidden units, and the activation function (sigmoid, ReLU, or tanh), should all be predefined. It is difficult to find an un derstandable model, even though the learned model can reach a high goodness of fit. We used the structure model with the common nonlinear activation sigmoid function to test the datasets and found that the standard variance of all parameters is large (Table 5). In other words, the parameters of the 10 NN models are different, which shows the risk of overfitting for the noise data.

For the same datasets, we used GP and the model selection method discussed in our paper. Our method could discover the model structure explicitly with an average $R ^ { 2 }$ of 0.992 (Table 6). The MAPEs for pa rameters a, b, and c are 2.17%, 2.4%, and 2.14%, respectively, and the overall MAPE is 2.24%. The errors of estimation are all very small, which indicates that the parameters of the models could also be correctly learned by our approach. Therefore, our approach could discover the model with the correct structure and parameters. It is more suitable to discover the model that describes the relationship between retail prices and reviews in this paper.

## 4. Data

The dataset is from Jingdong (JD.com), one of the largest B2C online retailers in China. JD.com has 236.5 million active customer accounts and US\$26.7 billion GMV for the first quarter of 2017.<sup>3</sup> Similar to Amazon.com, JD.com provides a platform where consumers can write post-purchase reviews. If a review is approved as valid by JD.com ac cording to its criteria described on the website, the user can obtain 10 points. The points can be used as cash when buying other products. 100 points equal 1 yuan (CNY) in cash, and point payment cannot exceed 50% of the total price of an order.

To find the patterns of users who wrote reviews, we developed a survey to measure the rate of reviews on JD.com. The result shows that for 67.9% of the respondents, the rate of review that is a ratio of the number of reviews to the number of purchases writing, is higher than 40%. Notably, each review is labelled by the date of purchase on JD.com (Fig. 6). For each product, based on the dates, we associated the pur chase with the retail prices of that day so that we could identify the retail price corresponding to the review for the purchased product. In our study, the retail prices and reviews had been crawled every day for 6 months from the beginning of October 2016 to the end of March 2017.

The JD.com systematically provides detailed product categorization. We collected the data based on the product categorization provided by the website. A total of 360 products are collected, including electronics and food & drinks. The product is removed if its price changed less than three times.<sup>4</sup> After processing, 321 products remained with 1,738,040 reviews. The prices for those products changed 5431 times in total and the price for each product changed 16.9 times on average. Table 7 provides a detailed description of the dataset: the price, volume of re view, and valence of reviews (average rating) for all products. In the table, price is the real retail price,<sup>5</sup> and reviews are also collected under this price.<sup>6</sup> Fig. 7 presents how price, volume of reviews, and valence of reviews change over time for a given laptop.

The collected dataset is unique because both retail prices and reviews are acquired from the same retailer website. Moreover, we observe the price for each transaction and associate each review with its actual transaction price. The exact retail price, rather than the market average price, increase the convenience of studying of the direct impact of price on consumer reviews. Studies have investigated the relationship be tween market price and reviews for all products at an aggregate level [8,9], whereas we investigate the relationship for one product at an individual level based on a unique dataset.

## 5. Results and findings

In this section, we describe the found models and analyze the re lationships between the prices and volume/valence of reviews described

Table 2 Design of simulations.

<table><tr><td>ID</td><td>Structure</td><td>Model</td><td> $(x_{\min}, x_{\max})$ </td><td>θ</td><td>ID</td><td>Structure</td><td>Model</td><td> $(x_{\min}, x_{\max})$ </td><td>θ</td></tr><tr><td>1</td><td>y = a - bx</td><td>y = 100 - 2×</td><td>(10,30)</td><td>5%</td><td>13</td><td>y = a - bx + cx2</td><td>y = 450 + x2 - 40×</td><td>(10, 30)</td><td>5%</td></tr><tr><td>2</td><td></td><td></td><td></td><td>10%</td><td>14</td><td></td><td></td><td></td><td>10%</td></tr><tr><td>3</td><td></td><td></td><td></td><td>30%</td><td>15</td><td></td><td></td><td></td><td>30%</td></tr><tr><td>4</td><td></td><td></td><td></td><td>50%</td><td>16</td><td></td><td></td><td></td><td>50%</td></tr><tr><td>5</td><td></td><td>y = 500-0.5×</td><td>(500, 800)</td><td>5%</td><td>17</td><td></td><td>y = 21,200 - 65× + 0.05 ×2</td><td>(500, 800)</td><td>5%</td></tr><tr><td>6</td><td></td><td></td><td></td><td>10%</td><td>18</td><td></td><td></td><td></td><td>10%</td></tr><tr><td>7</td><td></td><td></td><td></td><td>30%</td><td>19</td><td></td><td></td><td></td><td>30%</td></tr><tr><td>8</td><td></td><td></td><td></td><td>50%</td><td>20</td><td></td><td></td><td></td><td>50%</td></tr><tr><td>9</td><td></td><td>y = 900-0.2×</td><td>(3000, 4000)</td><td>5%</td><td>21</td><td></td><td>y = 25,000 -14× + 0.002 ×2</td><td>(3000, 4000)</td><td>5%</td></tr><tr><td>10</td><td></td><td></td><td></td><td>10%</td><td>22</td><td></td><td></td><td></td><td>10%</td></tr><tr><td>11</td><td></td><td></td><td></td><td>30%</td><td>23</td><td></td><td></td><td></td><td>30%</td></tr><tr><td>12</td><td></td><td></td><td></td><td>50%</td><td>24</td><td></td><td></td><td></td><td>50%</td></tr></table>

![](/api/attachments/VETJ5U8B/fulltext/images/63a8dd053883919f80419fbdf98482d02c7fa8760b17c09ae9c8300ad8584830.jpg)  
Fig. 5. Top ten model structures.

by the models.

## 5.1. Top models with high fitness

By using local pruning, a set of Pareto front models will come toward a certain product. For the given dataset, 321 sets of Pareto front models were generated for 321 products. Taking the “mouse” as an example, nine models of a Pareto front are explored by GP in Fig. 8, which have different fitness and complexity.

In general, the model with higher fitness $( R ^ { 2 } )$ has more complexity (Comp). In Fig. 8, the first model is the optimal model with the highest fitness $( R ^ { 2 } = 0 . 8 7 )$ , and its complexity (Comp = 45) is higher than the others. This finding suggests that this model fits the given data well but has the overfitting problem. Therefore, we must find the universal model that explains the general relationship between price and consumer re views for all products.

## 5.2. Top models with high coverage

Coverage is another measure to consider. The models with high coverage are much more universal; thus, they fit most of the products well. After global pruning, for the given dataset, the top ten models sorted by the coverage are presented in Table 8 and used to describe the relationships between prices and volume of reviews. Various forms of models are involved, including the linear model $( \mathrm { i . e . , ~ } \ \mathrm { M } ^ { \mathrm { v o } } { } _ { 1 } )$ , the quadratic models $\mathrm { ( i . e . , ~ M ^ { v o } } _ { 2 } , ~ M ^ { v o } { } _ { 3 } ,$ and $M ^ { \mathrm { v o } } { } _ { 6 } ) ,$ the semi-logarithmic model $( \mathrm { i . e . , ~ M ^ { v o } } _ { 4 }$ and $\mathbb { M } ^ { \mathrm { v o } } { } _ { 5 } ) ,$ , and the cubic models $( \mathrm { i . e . , ~ M ^ { v o } } _ { 7 } , ~ \mathrm { M ^ { v o } } _ { 8 } ,$ $\mathbf { M } ^ { \mathbf { v 0 } } \mathbf { 9 } ,$ and $\mathbf { M } ^ { \mathbf { v o } } \mathbf { \Phi } _ { 1 0 } )$

The models have different advantages and disadvantages. For example, the linear model is more universal. When we have few ideas regarding domain knowledge, the linear model is a good choice. Addi tionally, the quadratic models are worthy of consideration because their fitness is usually much higher than the linear models.

For the relationships between prices and valence of reviews, the top ten models are listed in Table 9. Among them, the top three with the highest coverage (above 10%) are linear $( \mathbf { M } ^ { \mathbf { v a } } )$ and $\mathbf { M } ^ { \mathbf { v a } } \mathbf { _ { 3 } } )$ or quadratic $( \mathbf { M } ^ { \mathbf { v a } } 2 ) .$ . Semi-logarithmic $( \mathbf { M } ^ { \mathbf { v a } } \mathbf { 8 } )$ and cubic models $\boldsymbol { ( \mathrm { M } ^ { \mathrm { v a } } 7 }$ and $\mathbf { M } ^ { \mathbf { v a } } \mathbf { _ { 9 } } )$ are also observed.

Complex models are usually more goodness of fit (Tables 8 and 9). When comparing Tables 8 and 9, one major difference is that the fitness and coverage in Table 9 compared with Table 8 are lower. The differ ence suggests that a precise description of the relationship between price and valence of reviews compared with the relationship between price and volume of reviews is more difficult.

Table 3  
Detailed information on the top two model structures.

<table><tr><td rowspan="2">ID</td><td rowspan="2">True structure</td><td colspan="3">Best model structure</td><td colspan="3">Second-best model structure</td></tr><tr><td>Structure</td><td>Cove</td><td> $R^2$ </td><td>Structure</td><td>Cove</td><td> $R^2$ </td></tr><tr><td>1</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.98(0.01)</td><td>y=a-bx-cx2</td><td>33%</td><td>0.98(0.01)</td></tr><tr><td>2</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.91(0.03)</td><td>y=a-bx+cx2</td><td>29%</td><td>0.91(0.03)</td></tr><tr><td>3</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.54(0.11)</td><td>y=a-bln(x)</td><td>33%</td><td>0.54(0.10)</td></tr><tr><td>4</td><td>y=a-bx</td><td>y=a-bx</td><td>90%</td><td>0.46(0.30)</td><td>y=a-bx+cx2</td><td>30%</td><td>0.54(0.30)</td></tr><tr><td>5</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.99(0.01)</td><td>y=a-bx-cx2</td><td>35%</td><td>0.99(0.004)</td></tr><tr><td>6</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.94(0.02)</td><td>y=a-bx2</td><td>32%</td><td>0.94(0.023)</td></tr><tr><td>7</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.63(0.11)</td><td>y=a-bx2</td><td>38%</td><td>0.62(0.11)</td></tr><tr><td>8</td><td>y=a-bx</td><td>y=a-bx</td><td>95%</td><td>0.75(0.37)</td><td>y=a-bx2</td><td>24%</td><td>0.56(0.32)</td></tr><tr><td>9</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.99(0.003)</td><td>y=a-bx2</td><td>30%</td><td>0.99(0.004)</td></tr><tr><td>10</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.93(0.10)</td><td>y=a-bx2</td><td>39%</td><td>0.92(0.12)</td></tr><tr><td>11</td><td>y=a-bx</td><td>y=a-bx</td><td>100%</td><td>0.70(0.10)</td><td>y=a-bln(x)</td><td>37%</td><td>0.74(0.07)</td></tr><tr><td>12</td><td>y=a-bx</td><td>y=a-bx</td><td>99%</td><td>0.49(0.21)</td><td>y=a-bx2</td><td>50%</td><td>0.49(0.21)</td></tr><tr><td>13</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.99(0.003)</td><td>y=a-bx+cx2-dx3</td><td>24%</td><td>0.99(0.002)</td></tr><tr><td>14</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.97(0.01)</td><td>y=a-bx+cx3</td><td>21%</td><td>0.97(0.01)</td></tr><tr><td>15</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>99%</td><td>0.79(0.07)</td><td>y=a-bx+cx3</td><td>27%</td><td>0.82(0.07)</td></tr><tr><td>16</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>95%</td><td>0.59(0.13)</td><td>y=a+bx-cln(x)</td><td>30%</td><td>0.64 (0.11)</td></tr><tr><td>17</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.99(0.02)</td><td>y=a-bx+cx3-dx5</td><td>25%</td><td>0.99(0.01)</td></tr><tr><td>18</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.99(0.004)</td><td>y=a-bx+cx3</td><td>29%</td><td>0.99(0.003)</td></tr><tr><td>19</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.93(0.03)</td><td>y=a-bx+cx3</td><td>33%</td><td>0.94(0.03)</td></tr><tr><td>20</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.83(0.07)</td><td>y=a-bx+cx3</td><td>35%</td><td>0.83 (0.06)</td></tr><tr><td>21</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.98(0.01)</td><td>y=a-bx+cx3</td><td>38%</td><td>0.98 (0.01)</td></tr><tr><td>22</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>100%</td><td>0.94(0.03)</td><td>y=a-bx+cx3</td><td>45%</td><td>0.94(0.02)</td></tr><tr><td>23</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>98%</td><td>0.62(0.12)</td><td>y=a-bx+cx3</td><td>34%</td><td>0.66(0.08)</td></tr><tr><td>24</td><td>y=a-bx+cx2</td><td>y=a-bx+cx2</td><td>88%</td><td>0.41(0.15)</td><td>y=a-bx+cx3</td><td>24%</td><td>0.39(0.13)</td></tr></table>

Table 4  
MAPE of parameter estimation.

<table><tr><td rowspan="2">ID</td><td colspan="4">MAPE</td><td rowspan="2">ID</td><td colspan="4">MAPE</td><td rowspan="2">ID</td><td colspan="4">MAPE</td></tr><tr><td>a</td><td>b</td><td>c</td><td>Avg.</td><td>a</td><td>b</td><td>c</td><td>Avg.</td><td>a</td><td>b</td><td>c</td><td>Avg.</td></tr><tr><td>1</td><td>0.11%</td><td>0.15%</td><td>N/A</td><td>0.13%</td><td>9</td><td>0.46%</td><td>0.50%</td><td>N/A</td><td>0.48%</td><td>17</td><td>0.17%</td><td>0.15%</td><td>0.13%</td><td>0.15%</td></tr><tr><td>2</td><td>1.04%</td><td>2.10%</td><td>N/A</td><td>1.57%</td><td>10</td><td>0.18%</td><td>0.50%</td><td>N/A</td><td>0.34%</td><td>18</td><td>0.07%</td><td>0.11%</td><td>0.15%</td><td>0.11%</td></tr><tr><td>3</td><td>1.87%</td><td>3.90%</td><td>N/A</td><td>2.89%</td><td>11</td><td>1.05%</td><td>1.00%</td><td>N/A</td><td>1.02%</td><td>19</td><td>0.15%</td><td>0.10%</td><td>0.07%</td><td>0.11%</td></tr><tr><td>4</td><td>4.77%</td><td>11.45%</td><td>N/A</td><td>8.11%</td><td>12</td><td>2.37%</td><td>3.00%</td><td>N/A</td><td>2.68%</td><td>20</td><td>2.95%</td><td>2.91%</td><td>2.85%</td><td>2.90%</td></tr><tr><td>5</td><td>0.27%</td><td>0.40%</td><td>N/A</td><td>0.34%</td><td>13</td><td>0.02%</td><td>0.11%</td><td>0.86%</td><td>0.33%</td><td>21</td><td>1.22%</td><td>1.23%</td><td>1.21%</td><td>1.22%</td></tr><tr><td>6</td><td>0.74%</td><td>1.20%</td><td>N/A</td><td>0.97%</td><td>14</td><td>1.25%</td><td>1.32%</td><td>1.25%</td><td>1.28%</td><td>22</td><td>0.94%</td><td>0.96%</td><td>0.94%</td><td>0.95%</td></tr><tr><td>7</td><td>1.09%</td><td>1.40%</td><td>N/A</td><td>1.25%</td><td>15</td><td>0.75%</td><td>1.27%</td><td>1.49%</td><td>1.17%</td><td>23</td><td>2.11%</td><td>2.20%</td><td>2.25%</td><td>2.19%</td></tr><tr><td>8</td><td>0.97%</td><td>2.20%</td><td>N/A</td><td>1.58%</td><td>16</td><td>1.76%</td><td>2.19%</td><td>1.11%</td><td>1.68%</td><td>24</td><td>13.9%</td><td>14.4%</td><td>14.5%</td><td>14.3%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Avg.</td><td>1.68%</td><td>2.25%</td><td>2.28%</td><td>1.87%</td></tr></table>

Table 5  
The results by NN.

<table><tr><td>Dataset</td><td> $R^2$ </td><td> $w_{11}$ </td><td> $w_{12}$ </td><td> $w_{21}$ </td><td> $w_{22}$ </td><td> $α_1$ </td><td> $α_2$ </td><td>β</td></tr><tr><td>1</td><td>0.998</td><td>4.16</td><td>2.42</td><td>6.09</td><td>-15.75</td><td>-3.21</td><td>2.8</td><td>12.69</td></tr><tr><td>2</td><td>0.997</td><td>3.18</td><td>4.77</td><td>-13.27</td><td>6.38</td><td>3.77</td><td>-2.71</td><td>10.58</td></tr><tr><td>3</td><td>0.998</td><td>-3.03</td><td>-3.08</td><td>10.23</td><td>-13.22</td><td>-2.68</td><td>3.27</td><td>10.1</td></tr><tr><td>4</td><td>0.997</td><td>3.2</td><td>-3.77</td><td>9.64</td><td>8.36</td><td>-2.34</td><td>-3.04</td><td>-3.19</td></tr><tr><td>5</td><td>0.991</td><td>-3.66</td><td>-2.43</td><td>-8.17</td><td>36.2</td><td>3.09</td><td>-3.94</td><td>5.11</td></tr><tr><td>6</td><td>0.995</td><td>-2.24</td><td>3.46</td><td>30.8</td><td>9.5</td><td>-3.54</td><td>-2.62</td><td>-3.51</td></tr><tr><td>7</td><td>0.994</td><td>5.4</td><td>-4.95</td><td>5.55</td><td>6.12</td><td>-3.16</td><td>-3.66</td><td>-2.32</td></tr><tr><td>8</td><td>0.982</td><td>5.11</td><td>11.42</td><td>-3.47</td><td>-0.41</td><td>3.35</td><td>1.71</td><td>2.15</td></tr><tr><td>9</td><td>0.993</td><td>3.41</td><td>2.35</td><td>-12.32</td><td>41.16</td><td>3.38</td><td>-3.88</td><td>9.15</td></tr><tr><td>10</td><td>0.967</td><td>5.52</td><td>-19.86</td><td>6.16</td><td>3.36</td><td>-4.06</td><td>-12.6</td><td>-1.85</td></tr><tr><td>Avg.(Stdev)</td><td>0.991(0.01)</td><td>2.11(3.62)</td><td>-0.97(8.27)</td><td>3.12(13.17)</td><td>8.17(18.29)</td><td>-0.54(3.42)</td><td>-2.47(4.56)</td><td>3.89(6.41)</td></tr></table>

## 5.2.1. Linear models

The linear models for both volume and valence of reviews have the highest coverage; thus, such models can be applied to most of the products.

(1) Linear models for the relationships between prices and the volume of reviews $( \mathbf { M } ^ { \mathbf { v o } } \mathbf { 1 } )$

$$
\mathbf {M} _ {1} ^ {\mathrm{vo}}: R ^ {\mathrm{vo}} = \beta_ {1 0} - \beta_ {1 1} P
$$

The linear model with a decreasing trend covers 65.11% of all products:

(13)

where the constant $\beta _ { 1 0 }$ embodies the fixed effects of all factors other than the price [25], and the constant $\beta _ { 1 1 }$ is the slope of the line. The coefficients of the model are positive, and the model suggests that the volume of reviews always decreases by a constant amount to a constant increase in price.

The model could be explained by the law of demand. Consumers are less likely to buy a product at a high price; thus, consumers would have fewer channels to post reviews [39]. In other words, consumers respond to the higher price by buying fewer products and writing fewer reviews, and vice versa.

Table 6  
The results by GP.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2"> $R^2$ </td><td rowspan="2">Model: y = a + bx2- cx</td><td colspan="3">MAPE</td><td rowspan="2">Avg.</td></tr><tr><td>a</td><td>b</td><td>c</td></tr><tr><td>1</td><td>0.998</td><td>y = 20,218.54 + 0.048 × 2-62.25×</td><td>4.63%</td><td>4%</td><td>4.24%</td><td>4.29%</td></tr><tr><td>2</td><td>0.989</td><td>y = 21,424.1 + 0.05 × 2-65.43×</td><td>1.06%</td><td>0%</td><td>0.67%</td><td>0.58%</td></tr><tr><td>3</td><td>0.996</td><td>y = 22,028.19+ 0.052 × 2-67.72×</td><td>3.91%</td><td>4%</td><td>4.18%</td><td>4.03%</td></tr><tr><td>4</td><td>0.996</td><td>y = 20,321.65 + 0.047 × 2-62.02×</td><td>4.14%</td><td>6%</td><td>4.59%</td><td>4.91%</td></tr><tr><td>5</td><td>0.989</td><td>y = 21,455.24 + 0.051 × 2-65.87×</td><td>1.20%</td><td>2%</td><td>1.33%</td><td>1.51%</td></tr><tr><td>6</td><td>0.993</td><td>y = 21,460.4 + 0.051 × 2-65.74×</td><td>1.23%</td><td>2%</td><td>1.13%</td><td>1.45%</td></tr><tr><td>7</td><td>0.992</td><td>y = 21,234.3 + 0.05 × 2-65.08×</td><td>0.16%</td><td>0%</td><td>0.12%</td><td>0.09%</td></tr><tr><td>8</td><td>0.992</td><td>y = 20,855.05 + 0.049 × 2-64.12×</td><td>1.63%</td><td>2%</td><td>1.35%</td><td>1.66%</td></tr><tr><td>9</td><td>0.991</td><td>y = 20,790.32 + 0.049 × 2-63.79×</td><td>1.93%</td><td>2%</td><td>1.86%</td><td>1.93%</td></tr><tr><td>10</td><td>0.99</td><td>y = 20,808.79+ 0.049 × 2-63.74×</td><td>1.85%</td><td>2%</td><td>1.94%</td><td>1.93%</td></tr><tr><td>Avg.(Stdev)</td><td>0.992(0.003)</td><td></td><td>2.17%</td><td>2.40%</td><td>2.14%</td><td>2.24%</td></tr></table>

![](/api/attachments/VETJ5U8B/fulltext/images/03ba1110159633798a460f5e9430a391fa52a4db5ca4ede12775756f15c29105.jpg)  
Fig. 6. A snapshot of reviews crawled on JD.com.

Table 7  
Descriptive statistics.

<table><tr><td rowspan="2">Product name</td><td rowspan="2">Products quantity</td><td colspan="4">Volume of reviews</td><td colspan="3">Valence of reviews</td><td colspan="4">Times of price changes</td><td colspan="3">Prices (CNY)</td></tr><tr><td>Count</td><td>Min</td><td>Max</td><td>Mean</td><td>Min</td><td>Max</td><td>Mean</td><td>Count</td><td>Min</td><td>Max</td><td>Mean</td><td>Min</td><td>Max</td><td>Mean</td></tr><tr><td>Beer</td><td>40</td><td>211,685</td><td>1504</td><td>25,034</td><td>5292</td><td>4.82</td><td>4.97</td><td>4.91</td><td>684</td><td>7</td><td>34</td><td>17</td><td>39</td><td>453.6</td><td>140.47</td></tr><tr><td>Chocolate</td><td>37</td><td>224,221</td><td>628</td><td>20,429</td><td>6060</td><td>4.68</td><td>4.97</td><td>4.91</td><td>506</td><td>4</td><td>44</td><td>14</td><td>9.9</td><td>258</td><td>62.65</td></tr><tr><td>Coffee</td><td>57</td><td>311,856</td><td>699</td><td>31,392</td><td>5471</td><td>4.70</td><td>4.98</td><td>4.93</td><td>1019</td><td>4</td><td>48</td><td>18</td><td>6.6</td><td>158</td><td>63.19</td></tr><tr><td>Cookie</td><td>34</td><td>211,745</td><td>825</td><td>19,926</td><td>6227</td><td>2.94</td><td>4.96</td><td>4.86</td><td>618</td><td>5</td><td>45</td><td>18</td><td>9.9</td><td>216</td><td>60.90</td></tr><tr><td>Laptop</td><td>29</td><td>85,743</td><td>357</td><td>17,068</td><td>2957</td><td>4.18</td><td>4.85</td><td>4.71</td><td>938</td><td>5</td><td>69</td><td>32</td><td>1849</td><td>9288</td><td>5689.87</td></tr><tr><td>Mobile phone</td><td>56</td><td>441,343</td><td>437</td><td>46,956</td><td>7881</td><td>4.59</td><td>4.94</td><td>4.83</td><td>767</td><td>3</td><td>54</td><td>14</td><td>799</td><td>7199</td><td>3618.94</td></tr><tr><td>Mouse</td><td>38</td><td>204,992</td><td>278</td><td>33,870</td><td>5395</td><td>4.70</td><td>4.92</td><td>4.82</td><td>358</td><td>5</td><td>18</td><td>9</td><td>19.89</td><td>1049</td><td>229.82</td></tr><tr><td>Printer</td><td>30</td><td>46,637</td><td>105</td><td>10,971</td><td>1.555</td><td>4.65</td><td>5.00</td><td>4.89</td><td>541</td><td>3</td><td>38</td><td>18</td><td>179</td><td>1899</td><td>857.03</td></tr><tr><td>Sum</td><td>321</td><td>1,738,222</td><td></td><td></td><td>5415</td><td></td><td></td><td>4.86</td><td>5431</td><td></td><td></td><td>17</td><td></td><td></td><td>1340.36</td></tr></table>

![](/api/attachments/VETJ5U8B/fulltext/images/15cffd0abf39aaefc57bd1bee85f9f7d1ecfa02aff9163c4453eb8cedc3db59c.jpg)  
(a) Changes in prices and volume of reviews

![](/api/attachments/VETJ5U8B/fulltext/images/fbea1e4217bb6bf6a76f32d4e2580a6be3636407bbec7c657bf02778bcd22344.jpg)  
(b) Changes in prices and valence of reviews  
Fig. 7. Curves of price-change history and volume/valence of reviews for a given laptop.

(2) Linear models for the relationships between prices and the valence of reviews $( \mathbf { M } ^ { \mathbf { v a } } )$ and $\mathbf { M } ^ { \mathbf { v a } } \mathbf { _ { 3 } } )$

Together, the linear models $\mathbf { M } ^ { \mathbf { v a } } )$ and $\mathbf { M } ^ { \mathbf { v a } } { } _ { 3 }$ cover nearly 38% of the products:

$$
\mathbf {M} _ {1} ^ {\mathrm{va}}: R ^ {\nu a} = \gamma_ {1 0} - \gamma_ {1 1} P\tag{14}
$$

$$
\mathrm{M} _ {3} ^ {\mathrm{va}}: R ^ {\mathrm{va}} = \gamma_ {3 0} + \gamma_ {3 1} P\tag{15}
$$

Although the average $\mathrm { R } ^ { 2 }$ of the two models are similar, $\mathbf { M } ^ { \mathbf { v a } } { } _ { 1 }$ can cover two times more products than $\mathbf { M } ^ { \mathbf { v a } } { } _ { 3 } .$ . These two models describe a completely opposite relationships between the prices and valence of reviews. $\mathbf { M } ^ { \mathbf { v a } }$ describes a negative relationship, whereas $\mathbf { M } ^ { \mathbf { v a } } { } _ { 3 }$ describes a positive relationship.

They seem to be contradictive; however, both are explainable. For $\mathbf { M } ^ { \mathbf { v a } } { } _ { 1 } ,$ it suggests that with the increasing price, consumers’ satisfaction

![](/api/attachments/VETJ5U8B/fulltext/images/2ded871e9413a33f42d0534aef4be71c921352c94f2bc9630c4e8a45b1ccb65a.jpg)  
Fig. 8. A set of Pareto front models for a “mouse” product data.

Table 8  
Models for the relationships between prices and volume of reviews.

<table><tr><td>ID</td><td>Model</td><td> $R^2(Stdev)$ </td><td>Comp</td><td>Cove</td></tr><tr><td> $M^{vo}_{1}$ </td><td> $R^{vo} = \beta_{10} - \beta_{11}P$ </td><td>0.27(0.22)</td><td>5</td><td>65.11%</td></tr><tr><td> $M^{vo}_{2}$ </td><td> $R^{vo} = \beta_{20} - \beta_{21}P + \beta_{22}P^2$ </td><td>0.46(0.26)</td><td>11</td><td>37.69%</td></tr><tr><td> $M^{vo}_{3}$ </td><td> $R^{vo} = -\beta_{30} + \beta_{31}P - \beta_{32}P^2$ </td><td>0.44(0.29)</td><td>11</td><td>11.84%</td></tr><tr><td> $M^{vo}_{4}$ </td><td> $R^{vo} = \beta_{40} - \beta_{41}lnP$ </td><td>0.37(0.19)</td><td>9</td><td>11.84%</td></tr><tr><td> $M^{vo}_{5}$ </td><td> $R^{vo} = \beta_{50} + \beta_{51}P - \beta_{52}lnP$ </td><td>0.49(0.28)</td><td>13</td><td>8.72%</td></tr><tr><td> $M^{vo}_{6}$ </td><td> $R^{vo} = \beta_{60} - \beta_{61}P^2$ </td><td>0.30(0.25)</td><td>7</td><td>8.72%</td></tr><tr><td> $M^{vo}_{7}$ </td><td> $R^{vo} = \beta_{70} - \beta_{71}P + \beta_{72}P^2 - \beta_{73}P^3$ </td><td>0.48 (0.29)</td><td>19</td><td>5.61%</td></tr><tr><td> $M^{vo}_{8}$ </td><td> $R^{vo} = -\beta_{80} + \beta_{81}P - \beta_{82}P^3$ </td><td>0.49(0.32)</td><td>13</td><td>4.36%</td></tr><tr><td> $M^{vo}_{9}$ </td><td> $R^{vo} = \beta_{90} - \beta_{91}P^3$ </td><td>0.35(0.28)</td><td>9</td><td>4.36%</td></tr><tr><td> $M^{vo}_{10}$ </td><td> $R^{vo} = \beta_{100} - \beta_{101}P + \beta_{102}P^3$ </td><td>0.58(0.31)</td><td>13</td><td>4.05%</td></tr></table>

Notes: All coefficients (β) are positive values.

Table 9  
Models for the relationships between prices and valence of reviews.

<table><tr><td>ID</td><td>Model</td><td> $R^2$ (Stdev)</td><td>Comp</td><td>Cove</td></tr><tr><td> $M^{va}_{1}$ </td><td> $R^{va} = \gamma_{10} - \gamma_{11}P$ </td><td>0.17(0.18)</td><td>5</td><td>27.41%</td></tr><tr><td> $M^{va}_{2}$ </td><td> $R^{va} = \gamma_{20} - \gamma_{21}P + \gamma_{22}P^2$ </td><td>0.31(0.27)</td><td>11</td><td>22.43%</td></tr><tr><td> $M^{va}_{3}$ </td><td> $R^{va} = \gamma_{30} + \gamma_{31}P$ </td><td>0.17(0.18)</td><td>5</td><td>10.90%</td></tr><tr><td> $M^{va}_{4}$ </td><td> $R^{va} = \gamma_{40} + \gamma_{41}P - \gamma_{42}P^2$ </td><td>0.34(0.30)</td><td>11</td><td>9.35%</td></tr><tr><td> $M^{va}_{5}$ </td><td> $R^{va} = \gamma_{50} - \gamma_{51}P^2$ </td><td>0.21(0.19)</td><td>7</td><td>9.35%</td></tr><tr><td> $M^{va}_{6}$ </td><td> $R^{va} = -\gamma_{60} + \gamma_{61}P - \gamma_{62}P^2$ </td><td>0.43(0.29)</td><td>11</td><td>8.10%</td></tr><tr><td> $M^{va}_{7}$ </td><td> $R^{va} = \gamma_{70} - \gamma_{71}P + \gamma_{72}P^2$ </td><td>0.41(0.34)</td><td>13</td><td>6.23%</td></tr><tr><td> $M^{va}_{8}$ </td><td> $R^{va} = \gamma_{80} + \gamma_{81}P - \gamma_{82}lnP$ </td><td>0.27(0.29)</td><td>13</td><td>4.67%</td></tr><tr><td> $M^{va}_{9}$ </td><td> $R^{va} = \gamma_{90} - \gamma_{91}P^3$ </td><td>0.26(0.21)</td><td>9</td><td>4.36%</td></tr><tr><td> $M^{va}_{10}$ </td><td> $R^{va} = \gamma_{100} + \gamma_{101}P^2$ </td><td>0.14(0.10)</td><td>7</td><td>3.43%</td></tr></table>

Note: Coefficients (γ) are positive.

decreases $[ 1 1 , 1 2 ] .$ . These consumers are more likely to post a negative review. As for $\mathbf { M } ^ { \mathbf { v a } } { } _ { 3 } ,$ we are surprised that consumers prefer to post positive reviews at an increased price. This result can be explained by the theory of loyalty and acquisition bias. Price changes the result in loyal and non-loyal consumer segments [12]. Customers loyalty to a brand product are less sensitive to a relatively high price, whereas nonloyal customers may often switch their alternatives. Thus, when the price is high, only the loyal customers are retained, who are easier to be satisfied with the product and more likely to post favorable reviews [39]. Additionally, the price can enhance acquisition bias and boost the observed mean ratings [14]. The fitting performance of the linear models is relatively low. To find models with higher fitness, the other forms of models such as nonlinear models should be further investigated.

## 5.2.2. Quadratic models

(1) Quadratic models for the relationships between prices and the volume of reviews $\mathbf { { ( M ^ { v 0 } 2 } }$ and $\mathbf { M } ^ { \mathbf { v o } } \mathbf { _ { 3 } } )$

The second and third models with the highest coverage are quadratic models presented in Table 6:

$$
\mathrm{M} _ {2} ^ {\mathrm{vo}}: R ^ {\mathrm{vo}} = \beta_ {2 0} - \beta_ {2 1} P + \beta_ {2 2} P ^ {2}\tag{16}
$$

$$
\mathrm{M} _ {3} ^ {\mathrm{vo}}: R ^ {\mathrm{vo}} = - \beta_ {3 0} + \beta_ {3 1} P - \beta_ {3 2} P ^ {2}\tag{17}
$$

These two quadratic models fit the data with higher fitness compared with the linear models. They cover nearly 50% of the products.

In Figs. 9 (a) and (b), $\mathbf { M } ^ { \mathbf { v o } } 2$ is U-shaped, and $\mathbf { M } ^ { \mathbf { v o } } { } _ { 3 }$ is inverted Ushaped. To measure the asymmetry, a new parameter, namely, increasing-decreasing-measure (IDM), is defined as follows:

$$
\mathrm{IDM} = \frac {P _ {\text { max }} - P _ {\text { ver }}}{P _ {\text { ver }} - P _ {\text { min }}}\tag{18}
$$

where $P _ { m a x }$ is the maximum price within the feasible range, $P _ { m i n }$ is the minimum price, and $P _ { \nu e r }$ is the price at the vertex of the curve [i.e., the bottom point in Fig. 9(a), or the top point in Fig. 9(b)]. Based on the coefficients of the model, we calculated the IDM, and there are six types of shapes to be formed:

Type-1: U-shaped curve for $0 < \mathrm { I D M } < 1 ;$ Type-2: U-shaped curve for $\mathrm { I D M } = 0 ;$ Type-3: U-shaped curve for $\mathrm { I D M } > 1 ;$ Type-4: inverted Ushaped curve for IDM > 1; Type-5: inverted U-shaped curve for 0 < IDM < 1; Type-6: inverted U-shaped curve for $\mathrm { I D M } = 0$

Table 10 shows the types of quadratic models for price and volume of reviews. Among the six types, Type-1 and Type-4 are dominant, espe cially Type-1. The Type-1 model suggests that the volume of reviews first decreases along with the increasing price, and when the price rea ches a certain level, the volume of reviews increases. By contrast, the Type-4 model shows that when the price increases. the volume of reviews first increases and then decreases.

![](/api/attachments/VETJ5U8B/fulltext/images/4d21e5245ef73c43aebab5c65070ad128727f70b22a917be409ed7f9e986b336.jpg)  
(a) Model ${ { \bf { M } } ^ { \mathrm { { v } } 0 } } _ { 2 }$

![](/api/attachments/VETJ5U8B/fulltext/images/4682a0194f612c6aa7b8cd734f10aa4ff159492d3892b48692b48042d7601f8c.jpg)  
(b) Model ${ { \bf { M } } ^ { \mathrm { { v o } } } } _ { 3 }$  
Fig. 9. Quadratic models.

Table 10  
Six types of quadratic models for the relationships between prices and volume of reviews.

<table><tr><td colspan="4"> $M^{vo}_{2}$ </td><td colspan="3"> $M^{vo}_{3}$ </td></tr><tr><td>Type</td><td>Type-1</td><td>Type-2</td><td>Type-3</td><td>Type-4</td><td>Type-2</td><td>Type-3</td></tr><tr><td>Shape</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cove</td><td>32.09%</td><td>4.05%</td><td>1.55%</td><td>9.03%</td><td>1.87%</td><td>0.93%</td></tr><tr><td>IDM</td><td>(0.01, 0.95), 0.46</td><td>(0,0), 0</td><td>(1.07,2.85), 1.81</td><td>(1.02, 4.39), 1.55</td><td>(0.49, 0.99), 0.75</td><td>(0, 0), 0</td></tr><tr><td> $R^{2}$ (Stdev)</td><td>0.48 (0.26)</td><td>0.45 (0.27)</td><td>0.15 (0.09)</td><td>0.43 (0.26)</td><td>0.31 (0.34)</td><td>0.82 (0.13)</td></tr></table>

Notes: The minimum, maximum, and average value of IDM are calculated.

The decreasing periods, such as the left side of Type-1 model and the right side of Type-4 model, could be explained by the reduction in purchases, which leads to a decrease in the volume of reviews. The increasing periods, such as the right side of Type-1 model and the left side of Type-4 model, may be caused by factors such as satisfaction, which affect the propensity of posting reviews for consumers.

The literature has suggested a U-shaped relationship between satis faction and WOM volume [11,23]. This finding can be explained: A lower price for a given product implies a purchase decision that is easier make and, usually, a more easily satisfied customer. A higher price causes consumers to expect a high-quality product. Once the distortion appears post-purchase, customers may be very sad, which evokes more individuals to comment on the price. As a result, more reviews could be generated from a higher price.

(2) Quadratic models for the relationships between prices and the valence of reviews $( \mathbf { M } ^ { \mathbf { v a } } \mathbf { _ { 2 } } )$ ).

Among all five quadratic models in Table $^ { 9 , }$ model $\mathbf { M } ^ { \mathbf { v a } } 2$ has the highest coverage value (22.43%), which is a U-shaped curve:

$$
\mathrm{M} _ {2} ^ {\mathrm{va}}: R ^ {\nu a} = \gamma_ {2 0} - \gamma_ {2 1} P + \gamma_ {2 2} P ^ {2}\tag{19}
$$

By calculating IDM, three types of $\mathbf { M } ^ { \mathbf { v a } } 2$ are formed (Table 11).

The decreasing periods, such as the left sides of Type-1 and Type-2 models, and the whole Type-3 model, could be explained by the dete riorated satisfaction caused by the increase in price. Most of the con sumers are more or less sensitive to price, and it is reasonable for them to express negative sentiments prompted by the high prices.

However, when the price increases to a certain level, we are sur prised that the valence of reviews increases along with the price increase (the right sides of the Type-1 and Type-2 models). The explanation for the increasing trends could be that the reviews are written by loyal or price-insensitive customers, who are the only customers who have been retained and are also more likely to share positive reviews.

Table 11  
Three types of quadratic models for the relationships between the prices and valence of review.

<table><tr><td colspan="4"> $M^{va}_{2}$ </td></tr><tr><td>Type</td><td>Type-1</td><td>Type-2</td><td>Type-3</td></tr><tr><td>Shape</td><td></td><td></td><td></td></tr><tr><td>Cove</td><td>13.08%</td><td>0.62%</td><td>8.72%</td></tr><tr><td>IDM</td><td>(0.24, 0.94), 0.68</td><td>(0,0), 0</td><td>(1.01,3.06), 1.50</td></tr><tr><td> $R^{2}$ (Stdev)</td><td>0.34(0.29)</td><td>0.18 (0.07)</td><td>0.29 (0.25)</td></tr></table>

Notes: The minimum, maximum, and average value of IDM are calculated.

## 6. Discussions

## 6.1. Product category

The aforementioned experiments were conducted on the whole dataset for all the products. Different products play a different role in consumers’ purchase decisions. The literature has divided products into two categories: high-involvement products and low-involvement prod ucts. Product involvement-levels refer to a consumer’s perceived importance or interest in a product [36]. High-involvement products mean products that are more important and interesting to consumer. Typical examples of high-involvement products are durable product such as electronics with complex functionality and long life [42], and typical examples of low-involvement products are consumable products such as food [40].

Table 12  
Main measures of models for relationships between the prices and reviews in product categories.

<table><tr><td></td><td></td><td colspan="3">Price &amp;Volume</td><td colspan="3">Price &amp;Valence</td></tr><tr><td>Product category</td><td></td><td> $M^{vo}_{1}$ </td><td> $M^{vo}_{2}$ </td><td> $M^{vo}_{3}$ </td><td> $M^{va}_{1}$ </td><td> $M^{va}_{2}$ </td><td> $M^{va}_{3}$ </td></tr><tr><td colspan="8">Low-involvement product</td></tr><tr><td rowspan="2">Beer</td><td>Cove</td><td>62.50%</td><td>40.00%</td><td>7.50%</td><td>7.50%</td><td>15%</td><td>22.50%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.18(0.13)</td><td>0.35(0.20)</td><td>0.12(0.06)</td><td>0.27(0.04)</td><td>0.16(0.06)</td><td>0.08 (0.08)</td></tr><tr><td rowspan="2">Chocolate</td><td>Cove</td><td>56.76%</td><td>37.84%</td><td>8.11%</td><td>29.73%</td><td>18.92%</td><td>10.81%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.26(0.21)</td><td>0.39(0.26)</td><td>0.67(0.29)</td><td>0.19(0.10)</td><td>0.30(0.31)</td><td>0.30(0.17)</td></tr><tr><td rowspan="2">Coffee</td><td>Cove</td><td>68.42%</td><td>33.33%</td><td>8.77%</td><td>24.56%</td><td>24.56%</td><td>12.28%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.27(0.21)</td><td>0.46(0.24)</td><td>0.59(0.19)</td><td>0.18(0.21)</td><td>0.38(0.33)</td><td>0.33(0.23)</td></tr><tr><td rowspan="2">Cookie</td><td>Cove</td><td>67.65%</td><td>44.12%</td><td>8.82%</td><td>17.65%</td><td>20.59%</td><td>14.71%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.24(0.15)</td><td>0.41(0.21)</td><td>0.29(0.22)</td><td>0.20(0.20)</td><td>0.23(0.22)</td><td>0.13(0.06)</td></tr><tr><td rowspan="2">Average</td><td>Cove</td><td>63.83%</td><td>38.82%</td><td>8.30%</td><td>19.86%</td><td>19.77%</td><td>15.08%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.24(0.18)</td><td>0.40(0.23)</td><td>0.42(0.19)</td><td>0.21(0.14)</td><td>0.27(0.23)</td><td>0.21(0.14)</td></tr><tr><td colspan="8">High-involvement product</td></tr><tr><td rowspan="2">Laptop</td><td>Cove</td><td>75.86%</td><td>44.83%</td><td>17.24%</td><td>51.72%</td><td>27.59%</td><td>6.90%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.22(0.19)</td><td>0.34(0.25)</td><td>0.37(0.09)</td><td>0.18(0.16)</td><td>0.30(0.28)</td><td>0.16(0.05)</td></tr><tr><td rowspan="2">Mobile phone</td><td>Cove</td><td>44.64%</td><td>30.36%</td><td>14.29%</td><td>35.71%</td><td>30.36%</td><td>5.36%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.25(0.26)</td><td>0.54(0.26)</td><td>0.54(0.32)</td><td>0.12(0.16)</td><td>0.42(0.28)</td><td>0.23(0.25)</td></tr><tr><td rowspan="2">Mouse</td><td>Cove</td><td>76.32%</td><td>31.58%</td><td>18.42%</td><td>34.21%</td><td>18.42%</td><td>7.89%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.36(0.24)</td><td>0.63(0.23)</td><td>0.32(0.19)</td><td>0.23(0.21)</td><td>0.32(0.11)</td><td>0.10(0.08)</td></tr><tr><td rowspan="2">Printer</td><td>Cove</td><td>83.33%</td><td>50.00%</td><td>13.33%</td><td>23.33%</td><td>23.33%</td><td>6.67%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.37(0.24)</td><td>0.60(0.26)</td><td>0.41(0.31)</td><td>0.19(0.20)</td><td>0.19(0.20)</td><td>0.14(0.04)</td></tr><tr><td rowspan="2">Average</td><td>Cove</td><td>70.04%</td><td>39.19%</td><td>15.82%</td><td>36.24%</td><td>24.93%</td><td>6.71%</td></tr><tr><td> $R^2(Stdev)$ </td><td>0.30(0.23)</td><td>0.52(0.25)</td><td>0.41(0.23)</td><td>0.18(0.18)</td><td>0.31(0.22)</td><td>0.16(0.10)</td></tr></table>

Notes: Coverage and R-squared of the top three dominant models. Coverage is calculated by dividing the total number of products in each category, not in all categories.

In our study, the collected data set covers both the high-involvement products and the low-involvement products, which are then subdivided into eight categories: laptop, mobile phone, mouse, printer, beer, chocolate, coffee, and cookies. The first four categories highinvolvement products, and the last four categories are lowinvolvement products. After the model search and selection by using the proposed approach, relationship models in different product cate gories have been built, and their three main measures are listed in Table 12.

In Table 12, two models, the linearly decreasing model $( \mathbf { M } ^ { \mathbf { v o } } \mathbf { \Phi } _ { 1 } )$ and the U-shaped model $( \mathbf { M } ^ { \mathbf { v o } } _ { 2 } ) ;$ are superior to the others in terms of their coverage in each category. The inverted U-shaped model $( \mathbf { M } ^ { \mathbf { v o } } { } _ { 3 } )$ is better than the other models in high-involvement products. Some plausible reasons for this result are as follows. Because the high-involvement products are usually more expensive, to avoid financial risk, con sumers are more sensitive to price changes [36]. If the price increases further, individuals would again raise their expectation of perceived quality, but sometimes they are likely to be dissatisfied.

Compared with the other models, the linearly decreasing model $( \mathbf { M } ^ { \mathbf { v a } } )$ performs best for the high-involvement products. This model suggests that price plays an important role in influencing the valence of reviews. Unlike the price of the low-involvement product, which usually changes little, the price of the high-involvement products such as a laptop may fluctuate hundreds or even thousands of CNY. Thus, due to the perception of the high financial risk of the high-involvement prod ucts, consumers are prone to negatively rate the overpriced products once they are aware of the mismatch between the price and the quality of products.

The linearly increasing model $( \mathbf { M } ^ { \mathbf { v o } } { } _ { 3 } )$ is most suitable for lowinvolvement products, especially for beer. This model suggests that loyalty often occurs for low-involvement products. For example, con sumers who are fond of a certain beer will not skimp on a positive rating for the selected product, even if its price slightly increases.

![](/api/attachments/VETJ5U8B/fulltext/images/647b0353de5244598993f167f707d37c0bf8b89c149e6767e8926e0693944711.jpg)  
(a) Low-involvement product

![](/api/attachments/VETJ5U8B/fulltext/images/58e37c8323bbe3c6c1005f4a9ce82c1365a8917fb27b2d98e5c1662cea3b0edc.jpg)  
(b) High-involvement product  
Fig. 10. Guide map of the dominant relationships between the prices and volume of reviews Notes: To highlight the dominant models, we set a threshold of 15% for coverage and a threshold of 0.15 for $\mathrm { { R } } ^ { 2 } .$

![](/api/attachments/VETJ5U8B/fulltext/images/6349e976a12065480671f0c8ef4ffa871b72657853c12c820d41d65ff6a90054.jpg)  
(a) Low-involvement product

![](/api/attachments/VETJ5U8B/fulltext/images/ac60720353ee21164e0eeb81258edf1af1a06ed2ad09233d56ca5e65e06ede50.jpg)  
(b) High-involvement product  
Fig. 11. Guide map of the dominant relationships between prices and the valence of reviews.

## 6.2. Post hoc analysis

Previous research has found that price affects reviews through various mediating factors [11–14]. It is rather difficult to confirm the relative importance of the factors, and the interaction of various factors is also intricate. The relationships between the retail prices and volume/ valence of reviews may be nonlinear. In addition, due to the complexity and idiosyncrasy of human experience, the effect of each factor may exhibit dynamic patterns and evolve over time, which makes a universal relationship outcome difficult. Thus, the relationships between the retail prices and of reviews will have multiple possible consequences. For example, Chen et al. (2011) [8] found that the relationship between the market price and the valence of reviews is not significant for the product “automobiles.” Li and Hitt (2010) [9] found the relationship between the market price and valence of reviews is significant linearly and decreasing for the product “digital cameras.” Although the findings are inconsistent, all are possible. The problem is that their research provided a limited understanding of the relationships between marketing price and valence of reviews, not the whole picture for more products.

To draw a bigger picture, we employ a data-driven method to automatically discover the hidden relationships from data. Instead of providing a specific type of relationship, we comprehensively found the multiple possible types across many products. Our results provide more detailed references and improve understanding.

## 6.3. A guide map

To describe the dominant relationship models, the guide map is built to provide concise information for references (Figs. 10 and 11). From the guide map we can find:

At first, none of the relationship models is absolutely superior to all the others for all the products. Similar to the proverb Blind Man and An Elephant, each relationship model can only be reasonable in some as pects, but cannot cover everything. This study attempts to provide more possible models to reference the advantages and disadvantages of the most competitive alternatives in the guide map by conducting compre hensive evaluations.

Second, both similarities and differences are observed between models for both volume and valence of reviews. The similarities include the linearly decreasing, asymmetric U-shaped, asymmetric inverted Ushaped, and the differences are that the linear decreasing relationship is only suitable for the price and the volume of reviews, whereas the lin early increasing relationship is for the valence of reviews. In addition, the relationships between prices and the volume of reviews are more significant than those of valence.

Third, the feasible relationships for both high and low-involvement products are also distinct. For example, a linearly increasing relationship between the price and the valence of reviews can display better performance in the low-involvement products. Additionally, the other relationships for the high-involvement products are more signifi cant than those for the low-involvement products.

Fourth, symmetric U-shaped relationship always shows both high fitness and high coverage, relative to all other alternatives. If referring to two tables by analyzing IDM (Tables 10 and 11), the asymmetric Ushaped relationship comprises a longer linearly decreasing shape at the beginning and then a shorter linearly increasing shape. It could be the most suitable choice to complement the linearly decreasing relationship.

## 6.4. Scalability study

In addition to the single platform $( \mathrm { i . e . , }$ , JD.com) studied in the above section, two other platforms are now analyzed: Taobao.com and Pind uoduo.com. Taobao.com is a C2C online retail website under the Ali: baba Group in China. Alibaba, JD, and Pinduoduo were the top 3 largest e-commerce companies in China in $2 0 2 0 . ^ { 8 }$ Table 13 shows the descrip tive statistics for the three different platforms. We selected data for mobile phones, tea & nuts, and fruit from June to September 2020. which included reviews and transaction prices for each product from the five sellers. The experimental results of the products from the two platforms are listed in Table 14.

The following could be observed from the results:

(1) The major findings observed from datasets for JD.com are reproduced in Table 14 using datasets for the other platforms. For example, for the relationship between price and volume of the reviews, the linearly decreasing model $( \mathbf { M } ^ { \mathbf { v o } } \mathbf { 1 } )$ and the U-shaped model $( \mathbf { M } ^ { \mathbf { v o } } 2 )$ are superior to the others in terms of coverage in each category. In addition, the inverted U-shaped model $( \mathbf { M } ^ { \mathbf { v o } } \mathbf { _ { 3 } } )$ is better than the other models for high-involvement products. For the relationship between price and valence of reviews, the line arly decreasing model $( \mathbf { M } ^ { \mathbf { v a } } )$ performs best for the highinvolvement products. The linearly increasing model $( \mathbf { M } ^ { \mathbf { v o } } { } _ { 3 } )$ is most suitable for the low-involvement products.

(2) By analyzing the coefficient of the model, we found that the asymmetric U-shaped and asymmetric inverted U-shaped struc tures were more dominant. In particular. for the newly analvzed data, the linearly increasing relationship is more dominant than in the valence of reviews for low-involvement products (tea & nuts and fruits). The finding is especially useful for fruit products, which suggests that consumers who are fond of a certain fruit will not skimp on a positive rating for the product, even if its price slightly increases. This finding also agrees with the results that found using JD.com data.

Table 13  
Descriptive statistics for datasets collected from different platforms.

<table><tr><td>Platform</td><td>Product</td><td>No. of products</td><td>No. of reviews</td><td>Variables</td><td>Min</td><td>Max</td><td>Mean</td></tr><tr><td rowspan="3">Taobao</td><td rowspan="3">Mobile phones</td><td rowspan="3">10</td><td rowspan="3">1118</td><td>Volume of reviews</td><td>1</td><td>87</td><td>9.32</td></tr><tr><td>Valence of reviews</td><td>3</td><td>5</td><td>4.54</td></tr><tr><td>Prices</td><td>890</td><td>4840</td><td>2140.37</td></tr><tr><td rowspan="3">Taobao</td><td rowspan="3">Fruit</td><td rowspan="3">10</td><td rowspan="3">1841</td><td>Volume of reviews</td><td>1</td><td>383</td><td>16.89</td></tr><tr><td>Valence of reviews</td><td>1.67</td><td>5</td><td>4.7</td></tr><tr><td>Prices</td><td>4.98</td><td>238</td><td>60.94</td></tr><tr><td rowspan="3">Pinduoduo</td><td rowspan="3">Tea&amp; Nut</td><td rowspan="3">10</td><td rowspan="3">2823</td><td>Volume of reviews</td><td>1</td><td>979</td><td>44.81</td></tr><tr><td>Valence of reviews</td><td>4.64</td><td>5</td><td>4.94</td></tr><tr><td>Prices</td><td>13.77</td><td>113.8</td><td>46.1</td></tr></table>

Table 14  
Models for relationships between prices and reviews for new products.

<table><tr><td></td><td></td><td colspan="3">Price &amp;Volume</td><td colspan="3">Price &amp;Valence</td></tr><tr><td>Product category</td><td></td><td> $M^{vo}_{1}$ </td><td> $M^{vo}_{2}$ </td><td> $M^{vo}_{3}$ </td><td> $M^{va}_{1}$ </td><td> $M^{va}_{2}$ </td><td> $M^{va}_{3}$ </td></tr><tr><td colspan="8">High-involvement</td></tr><tr><td rowspan="2">Mobile phones</td><td>Cove</td><td>80%</td><td>50%</td><td>20%</td><td>50%</td><td>40%</td><td>/</td></tr><tr><td> $R^{2}(Stdev)$ </td><td>0.30(0.18)</td><td>0.49(0.22)</td><td>0.31(0.01)</td><td>0.26(0.1)</td><td>0.46(0.08)</td><td>/</td></tr><tr><td colspan="8">Low-involvement</td></tr><tr><td rowspan="2">Tea&amp; Nuts</td><td>Cove</td><td>70%</td><td>20%</td><td>/</td><td>10%</td><td>20%</td><td>50%</td></tr><tr><td> $R^{2}(Stdev)$ </td><td>0.32(0.23)</td><td>0.63(0.26)</td><td>/</td><td>0.16(0)</td><td>0.3(0.05)</td><td>0.29(0.07)</td></tr><tr><td rowspan="2">Fruit</td><td>Cove</td><td>70%</td><td>50%</td><td>10%</td><td>/</td><td>40%</td><td>60%</td></tr><tr><td> $R^{2}(Stdev)$ </td><td>0.32(0.12)</td><td>0.39(0.16)</td><td>0.49(0)</td><td>/</td><td>0.43(0.17)</td><td>0.28(0.09)</td></tr><tr><td rowspan="2">Average</td><td>Cove</td><td>70%</td><td>35%</td><td>5%</td><td>5%</td><td>30%</td><td>55%</td></tr><tr><td> $R^{2}(Stdev)$ </td><td>0.32(0.18)</td><td>0.41(0.2)</td><td>0.49(0)</td><td>0.16(0)</td><td>0.39(0.2)</td><td>0.29(0.08)</td></tr></table>

## 7. Conclusions and implications

Much recent research has indicated that consumer reviews are crit ical to product management and how product managers engage in proactive marketing efforts, such as modifying the retail price, to affect the online review behavior of consumers after shopping. Thus, the model is necessary and helpful for depicting the relationships between reviews and prices. Considering this information, we designed an intelligent data-driven Generate/Test Cycle by introducing a machine learning approach without a hypothesis to automatically discover the functional relationship models between the retail prices and of reviews. Specifically, various relationship models have been found by using GP based on the real data, we validated the method by conducting a Monte Carlo simulation. Accordingly, we conducted a considerable number of experiments on different types of products. Based on the comprehensive evaluations, the dominant relationship models for different product categories were observed and a guide map was drawn to compare the advantages and disadvantages of various relationship models.

## 7.1. Theoretical implications

Our research extends the literature on the relationship between marketing variables and online review-posting behavior. Many re searchers have emphasized that behavioral or psychological drivers of consumers can affect the motivations of a consumer who will post online reviews after shopping [13,43]. Additionally, a few researchers have revealed the effect of retailers’ marketing efforts such as advertising [37], monetary rewards [44], and market price [8,9] affect UGC. This paper quantitatively studied the relationships between consumers reviewing behaviors and marketing efforts.

More specifically, we contribute to the research on modeling the relationships between the retail prices and reviews for the given product at an individual level. The research studied the relationship between market average price and reviews for all products at an aggregate level [8,9]. By contrast, we explored the relationships between retail prices and reviews for each product by using a unique dataset. The results provide more detailed information that is especially useful when per forming marketing activities.

This paper also extends the research paradigm for building the relationship model in a more efficient manner. The relationship models in the literature have usually been designed by domain experts who used a Generate/Test Cycle [15,16]. To find relationship models, the tradi tional paradigm would assume the relationship between variables, design the promising structure of a model, and learn the parameters of the model from the history data [25]. This paper proposes an intelligent data-driven Generate/Test Cycle using GP to learn about the relation ship model from data in an automatic manner without a prior hypoth esis, including its structure and parameters. When managing big data, our new approach could be more helpful and will relieve the heavy burden of researchers to discover hidden knowledge from the data.

Moreover, this paper offers empirical findings and a guide map that improve the understanding of the relationship between retail prices and the volume/valence of reviews. The comprehensive evaluations of each candidate model in various categories of products precisely describe its comparative advantages and disadvantages. This will advance empirical research in the information systems field.

## 7.2. Practical implications

The reviews are very important for retailers to help increase sales. Product managers could benefit from a proactive strategy [41], rather than reacting passively to WOM generated in the past.

For commercial practitioners, price is an effective marketing tool to stimulate consumer reviews. Through the experiments, we discovered multiple quantitative relationship models that could be applied to stimulate reviews by adjusting the price in a more cost-effective manner. Practitioners could refer to the guide map and choose a proper response model for specific products according to the models provided by our research. If the practitioner wants to acquire more consumer reviews, it should be effective for most products by lowering the price. Our results also show that a higher price does not always lead to a decreased number of reviews, and we also describe which type of products belong to such cases. If a commercial practitioner wants to boost the average rating, it can adjust the price according to our suggestions in this paper. For example, for high-involvement products, it is more effective to lower the price.

For academic practitioners, it is attractive to generate candidate relationship models for theoretical studies by distilling knowledge from data efficiently. People often spend much time preprocessing and analyzing data to determine what types of relationship are worthy of further investigation. Our research provides a new tool for generating promising models and testing them against a large dataset, which can reduce the burden of data analysis for a human researcher.

## 7.3. Limitation and future work

In addition to price, various factors affect consumer reviews, such as advertising, competitors, and monetary rewards. In this paper, only the price is considered, which accordingly reduces the fitting accuracy observed by $\mathrm { { R } } ^ { 2 } .$ If more data is integrated, the $\mathrm { R } ^ { 2 }$ would be expected to improve a lot, and the model will become more complex due to the interactive effect of multiple factors. Modeling the interactive relation ship of multiple variables using the GP is an important research topic in the future. Besides, our research shows that most reviews are posted within one month, which suggests that the impact of time bias may be limited. How posting time could introduce bias or even distortion to the quality of online reviews remains an open question. Additionally, a limited number of interpretations are provided for models discovered in this paper, most of which are cited from the literature or based on intuition. Further empirical analysis is necessary to provide additional evidence to reveal the influence mechanism of price on consumer reviews.

## Acknowledgement

This work was supported by the National Natural Science Foundation of China (42071273, 71671024, 71871041, 71421001), Research Funds of Education Department of Liaoning Province (LN2020Q30), Research Funds of Dongbei University of Finance and Economics (DUFE2020Q08), Fundamental Research Funds for the Central Univer sities (DUT20JC38), Liaoning Revitalization Talents Program (XLYC1807143), and Social Planning Foundation of Liaoning (L17AGL012).

## References

[1] M. Olmedilla, M. Martínez-Torres, S. Toralc, The superhit effect and long tai phenomenon in the context of electronic word of mouth, Decis. Support. Syst. 125 (2019) 1–10.

[2] X. Yang, G. Yang, J. Wu, Integrating rich and heterogeneous information to design

[3] X. Lu, S. Ba, L. Huang, Y. Feng, Promotional marketing or word-of-mouth? Evidence from online restaurant reviews, Inf. Syst. Res. 24 (3) (2013) 596–612.

[4] A. Gesenhues, Survey: 90% of Customers Say Buving Decisions Are Influenced by Online Reviews, 2013

[5] M. Luca, Reviews, reputation, and revenue: The case of Yelp.com, Harvard Business Review. 2011.

[6] V.R. Rao, Pricing research in marketing: the state of the art, J. Bus. 57 (1) (1984) 39–71.

[7] M. Puccinelli, C. Goodstein, D. Grewal, Customer experience management in retailing: understanding the buying process, J. Retail. 85 (1) (2009) 15–30.

[8] Y. Chen, S. Fay, Q. Wang, The role of marketing in social media: how online

[9] X. Li, L. Hitt, Price effects in online product reviews: an analytical model and empirical analysis, MIS Q. 34 (4) (2010) 809–831.

[10] N. Archak, A. Ghose, G. Ipeirotis, Deriving the pricing power of product features by

[111 E. Anderson, Customer satisfaction and word of mouth, J. Sery. Res. 1 (1) (1998

[12] L. Krishnamurthi, S. Raj, An empirical analysis of the relationship between loyalty and consumer price elasticity. Mark, Sci. 10 (2) (1991) 172–183.

[13] D. Bowman, D. Narayandas, Managing customer-initiated contacts with manufactures: the impact on share of category requirements and word-of-mouth behavior, J. Mark, Res, 38 (3) (2001) 281–297.

[14] N. Hu, P. Pavlou, J. Zhang, On self-selection biases in online product reviews, MIS Q. 41 (2) (2017) 449–471.

[15] H. Simon, The sciences of the artificial (3rd ed.), MIT Press Cambridge MA (1996).

[16] A. Hevner, S. March, J. Park, S. Ram, Design science in information systems research, MIS O. 28 (1) (2004) 75–105.

[17] J. Koza, Genetic programming: on the programming of computers by means o natural selection, MIT Press (1992).

[18] M. Schmidt, H. Lipson, Distilling free-form natural laws from experimental data, Science 324 (5923) (2009) 81–85.

[19] I. Chattopadhyay, A. Kuchina, G. Süel, Inverse Gillespie for inferring stochastic reaction mechanisms from intermittent samples. Proc. Natl. Acad. Sci. 110 (32) (2013)12990–12995

[20] W. Fan, P. Pathak, L. Wallace, Nonlinear ranking function representations in genetic programming-based ranking discovery for personalized search, Decis. Support. Syst. 42 (3) (2006) 1338–1349.

[21] W. Fan, P. Pathak, M. Zhou, Genetic-based approaches in ranking function discovery and optimization in information retrieval - a framework, Decis. Support Syst, 47 (4) (2009) 398–407.

[22] E. Maslowska, E.C. Malthouse, V. Viswanathan, Do customer reviews drive purchase decisions? The moderating roles of review exposure and price, Decis. Support. Syst. 98 (2017) 1–9.

[23] C. Dellarocas, R. Narayan, A statistical measure of a population’s propensity to engage in postpurchase online word-of-mouth, Stat. Sci. 21 (2) (2006) 277–285.

[24] D. Sundaram, K. Mitra, C. Webster, Word-of-mouth communications: a motivational analysis, Ady, Consum, Res. 25 (1998) 527–531.

[25] D. Hanssens, L. Parsons, R. Schultz, Market response models: econometric and time series analysis second edition, Kluwer Academic Publishers (2003)

[26] R. King, J. Rowland, S. Oliver, et al., The automation of science, Science 324 (5923) (2009) 85–89.

[27] A. McAfee, E. Brynjolfsson, Big data: the management revolution, Harv. Bus. Rev. 90 (10) (2012) 1–15.

[28] X. Zhang, S. Mahadevan, Ensemble machine learning models for aviation incident risk prediction, Decis, Support, Syst, 116 (2019) 48–63

[29] X. Zhang, S. Mahadevan, Bayesian neural networks for flight trajectory prediction and safety assessment, Decis. Support. Syst. 131 (2020) 1–17.

[30] U. Yolcu, E. Egrioglu, C. Aladag, A new linear & nonlinear artificial neural network model for time series forecasting, Decis. Support. Syst. 54 (3) (2013) 1340–1347.

[31] K. Yoshihara, M. Shahmoradgoli, E. Martínez, et al., Inferring tumor purity and stromal and immune cell admixture from expression data. Nat. Commun. 4 (2612 (2013) 1–11.

[32] W. Li, G. Yang, X. Li, et al., Cluster analysis of the relationship between carbon dioxide emissions and economic growth, J. Clean, Prod. 225 (2019) 459–471.

[33] G. Dhillon, J. Ward. Chaos theory as a framework for studving information

[34] J. Little. Models and managers: the concept of a decision calculus. Manag. Sci. 50 (12) (2004) 1841–1853.

[35] F. Bass. The future of research in marketing: marketing science., J. Mark. Res. 30

[36] B. Gu, J. Park. P. Konana. The impact of external word-of-mouth sources on retailet sales for high involvement products. Inf, Syst. Res, 1 (23) (2012) 182–196.

[37] E. Keller, B. Fay, Word-of-mouth advocacy: a new key to advertising effectiveness, J. Advert. Res. 52 (4) (2012) 459–464

[38] Y. Jin, B. Sendhoff, Pareto-based multi-objective machine learning: an overview 397-415.

[39] D. Godes, D. Mayzlin, Using online conversations to study word-of-mouth communication, Mark. Sci. 23 (4) (2004) 545–560

[40] W.D. Hover, D.H. Macinnis, Consumer Behavior, 5th ed., South-Western, Mason OH. 2008.

[41] M. Yang, Z. Zheng, V. Mookerjee, Prescribing response strategies to manage customer opinions: a stochastic differential equation approach, Inf. Syst. Res. 30 (2) (2019) 351–374.

[42] C. Jiang, R. Duan, H.K. Jain, S. Liu, K. Liang, Hybrid collaborative filtering fo high-involvement products: a solution to opinion sparsity and dynamics, Decis Support. Syst. 79 (2015) 195–208.

[43] C. Cheung, M. Lee, What drives consumers to spread electronic word of mouth in online consumer-opinion platforms, Decis. Support. Syst. 53 (1) (2012) 218–225.

[44] Y. Sun, X. Dong, S. McIntyre, Motivation of user-generated content: social connectedness moderates the effects of monetary rewards, Mark. Sci. 36 (3) (2017)

Xian Yang is an assistant professor at School of Management Science and Engineering in Dongbei University of Finance and Economics. Her research focuses on online reviews, computational intelligence and business data analysis.

Guangfei Yang is a professor at Institute of Systems Engineering in Dalian University of Technology. He received his doctoral degree in engineering at Waseda University in 2009 His research is about data mining and computational intelligence.

Jiangning Wu is a professor at Institute of Systems Engineering in Dalian University of Technology. She received her PhD at The University of Hong Kong. Her research is about data mining and business intelligence.

Yanzhong Dang is a professor at Institute of Systems Engineering in Dalian University of Technology. His research is about data mining, knowledge management and business intelligence.

Weiguo Fan is Henry B. Tippie Chair Professor in Business Analytics at the University of Iowa. He received his PhD in Business Administration from the Ross School of Business,

University of Michigan, Ann Arbor, in 2002. His research interests focus on the design and development of novel information technologies — information retrieval, data mining, text analytics, social media analytics, business intelligence techniques — to support bette business information management and decision making.
