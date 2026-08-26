---
otero_id: 4728
otero_key: "EY398EEJ"
title: "From predictive to prescriptive analytics: A data-driven multi-item newsvendor model"
authors: "Sushil Punia; Surya Prakash Singh; Jitendra K. Madaan"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113340"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

From predictive to prescriptive analytics: A data-driven multiitem newsvendor model

ELSEVIER Decision Support Systems

Sushil Punia, Surya Prakash Singh, Jitendra K. Madaan

![](/api/attachments/EY398EEJ/fulltext/images/0addbdbebf606c3f099e34ac26b5aa8c0044b35ce7f0d685ecde0c106ad0ead7.jpg)

PII: S0167-9236(20)30095-6

DOI: https://doi.org/10.1016/j.dss.2020.113340

Reference: DECSUP 113340

To appear in: Decision Support Systems

Received date: 3 March 2020

Revised date: 22 May 2020

Accepted date: 6 June 2020

Please cite this article as: S. Punia, S.P. Singh and J.K. Madaan, From predictive to prescriptive analytics: A data-driven multi-item newsvendor model, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113340

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

From Predictive to Prescriptive Analytics: A Data-Driven Multi-Item Newsvendor Model

Sushil Punia<sup>\*</sup>, Surya Prakash Singh, Jitendra K. Madaan

Department of Management Studies, Indian Institute of Technology Delhi, Hauz Khas, New Delhi 110016, India. sushil.punia@dms.iitd.ac.in

surya.singh@gmail.com

jmadaan@dms.iitd.ac.in

Corresponding author. sushil.punia@dms.iitd.ac.in; s.punia.official@gmail.co m. +91-9643264474.

## Abstract

This paper considers a multi-item newsvendor problem with a capacity constraint (Z). The problem has already been addressed in the literature using the classical newsvendor problem. However, provided solutions made assumptions for demand distributions, which are often incorrect and led to errors in the inventory optimization. This research proposes a distributionfree and completely data-driven solution approach to Z. The proposed approach uses sample demand data as input, and machine (and deep) learning methods with empirical risk minimization principle to find order qu antities. A heuristic is developed using hierarchies of the retail products to perform multi-ite entory optimizat when a capacity constraint is active. The proposed approach is tested on a real-world dataset of retail products. The results from the proposed method are compared with data-driven max-min and empirical inventory optimization methods, and it outperformed all of them. The machine (and deep) learning-based demand forecasting methods (part of the proposed approach) providing better results than neural networks, multiple regression, arima, arimax, etc. Finally, a comparison of total inventory cost from the proposed, max-min, and empirical inventory optimization methods are carried out, and it is observed that the proposed data-driven approach leads to a significant reduction in inventory cost.

Keywords: multi-item newsvendor model; machine learning; quantile regression; resource allocation; hierarchical forecast.

## 1. Introduction

Many firms, including manufacturers, distributors, and retailers, commonly face two critical problems. The first problem is to decide the production or order quantity for products with short life-cycle before selling season. The second problem for firms is to do the allocation of a limited resource. Under the first problem, if the order quantity for a product is higher than its demand, then the retailer will incur obsolescence cost; and if the order quantity for a product is lower than the demand, then the retailer will have opportunity and goodwill loss. Thus, a tradeoff between ordering too much or too little is a crucial decision to make for a retailer. A newsvendor model, and its variations very well represent this inventory management problem. This type of problem is relevant to many industries, such as fast-food, fashion clothing, groceries, bakeries, sports goods, and perishable products industry.

In a classic newsvendor problem, a retailer minimizes the expected total cost of ordering items from an upstream supply chain partner. To find out the order quantities for products, retailer assumes a specific distribution of the stochastic demand, and that leads to errors in order quantities, and consequently increase Although a large number of retailers use these theoretical newsvendor models, the assumption of a specific statistical distribution for demand does not hold well in reality. Moreover, the pattern of demand changes with the business environment, thus changes the distribution of demand over time, too (Levi, Perakis, & Uichanco, 2015). Such an approach that is free from the assumption of demand distribution shall be useful for inventory management in practice.

Under the second problem, firms have to do allocations of a limited resource (e.g., budget, shelf-space, or time, etc.) among multiple products/items. This problem is known as a resource allocation problem. For example, a retailer has to allocate limited shelf-space to different variants of a particular food item, or similarly, a fashion store has limited space for different colors and sizes of the same garment.

The paper address these two problems by formulating a multi-item inventory optimization problem with a capacity constraint and providing a data-driven solution to it. Recently, some efforts were made to develop data-driven solutions for the newsvendor problem (Huber, Müller, Fleischmann, & Stuckenschmidt, 2019). However, literature is somewhat fragmented, and multiitem case with a capacity constraint is not addressed. Therefore, this paper address this gap through a data-based solution. A large real-world dataset consisting of demand and business environment data is used as input, and advanced machine (deep) learning algorithms are used to contributions and insights are elaborated herewith.

## 1.1 Contributions and Insights

## 1.1.1 A Machine (deep) learning-based demand estimation method

As a part of the newsvendor model, it is needed to estimate the products' demand for future periods. So, first, we tried to find out an accurate demand estimation method that can be used in the proposed data-driven inventory optimization model. The advanced machine learning deep neural network) are used to estimate the demand for future periods. The predictions from these methods are compared with widely used time-series and regression methods to investigate the performance of the proposed method.

## 1.1.2 A data-driven Inventory optimization method

To overcome the limitations of a classical newsvendor inventory model, we proposed a novel quantile-regression and machine learning-based approach to find the optimal order quantities for products. The proposed optimization approach integrates the demand estimation and inventory optimization steps eliminating redundant efforts to perform two separate steps. The maximal approximation (Gallego & Moon, 1993; Scarf, 1958), and normal distribution based empirical methods are used to adjudge the performance of the proposed method. In data-driven models, Gallego and Moon (1993) provided a method to solve a multi-item inventory optimization under a budget constraint. Because it is a simple yet effective data-driven model, it is used as a benchmark to test our solution.

## 1.1.3 A heuristic for multi-item inventory optimization with a limited capacity

A heuristic is proposed to determine the optimal order quantities for multiple products under a capacity constraint. In this novel heuristic, top-down hierarchies of the products are used along with demand data to provide the complete data-driven solution to the multi-item inventory optimization with a limited capacity problem. Different possible cases of the problem are discussed, and solutions are provided for the same.

The goal of inventory management is to decide order quantities to procure products from an upstream supply chain member at minimum cost. So, we calculated the total inventory cost for techniques are analyzed on the total inventory cost.

## 1.2 Organization of the paper

The remainder of this paper is organized as follows. In Section 2, an overview of related literature is discussed, and research $\mathrm { { \bf g } } { \cdot } \mathrm { { \bf \Pi } } _ { \mathrm { { \bf f } } } { \cdot } { \bf \{ \Pi \} }$ are identified. The problem description and proposed data-driven models tory esented in Section 3. Section 4 contain detailed empirical analysis, ussions. Finally, Section 5 contains the conclusion and directions for future or

## 2. Related Literature

The newsvendor models (hereafter, NVM) in operations management is a widely discussed inventory management problem. To tackle the stochastic nature of demand in NVM, several approaches have been suggested to model the demand uncertainty. The most common approach, in research and practice both, is to assume a specific distribution for demand and calculate its parameters; and, afterward, use the parameters to solve the NVM to find optimal order quantities. The approach is available in several textbooks (Silver, Pyke, & Thomas, 2016)

and review papers (Qin, Wang, Vakharia, Chen, & Seref, 2011). This approach is included in our analysis to benchmark the results of the proposed model (Huber et al., 2019).

Another class of methods is data-driven models. The first approach under data-driven models is robust optimization, i.e., the optimization of NVM is performed using partially available demand information (Chen, Sim, & Sun, 2007). Scarf (1958) presented the NVM in which only the mean and variance of the demand data is known. Using a mathematical proof, he provided an ordering rule to find the order quantity with the worst and best possible distributions Moon (1993) extended this idea in several directions underlining its practical value under the conservative approach of using only mean and variance. It is extended to different cases, where second buying opportunity is available, where fixed ordering cost is involved, to random yield, and a multi-item under a capacity constraint. Random yield is a case where yield from production is assumed to be a random variable.

Bertsimas and Thiele (2006) extended the research on robust optimization by proposing a heterogenous demand distributions overtime on echelons. The authors claimed that under robust optimization (knowing mean and variance of demand only), their approach outperforms the models assuming some specific distribution of the demand variable. Another approach under data-driven models is sample average approximation, where a sample of the demand data is used to solve the NVM (Levi, Roundy, & Shmoys, 2007). Levi et al. (2015) provided the distributionspecific tighter bounds version of Levi et al. (2007) for single period featureless NVM and showed that sample average approximation could perform at par with the empirical model. Huber et al. (2019) applied the sample average approximation to NVM with multi-feature data and found it is performing better than empirical methods in some of the cases.

In data-driven methods, a more recent approach to use demand data for solving NVM advocates integrating the demand estimation and optimization steps into a single step. Ban and

Rudin (2018) proposed a big data newsvendor problem in which the authors used the machine learning algorithms along with empirical risk minimization and kernel weights optimization to solve a multi-feature NVM. The authors showed that the empirical risk minimization approach is equivalent to a high-dimensional quantile regression and can be solved by convex optimization methods. Oroojlooy, Snyder, and Takáč (2019) used the deep neural networks to solve the NVM using an integrated method to solve NVM and extended the approach for (??, ??) policy. However, they have not used quantile regression for the same. A similar approach is proposed by Huber et

## 2.1 Time-series, Machine and Deep learning methods for demand forecasting

The commonly used methods for demand forecasting are time-series methods such as exponential smoothing method (Hyndman et al. 2002; Gardner Jr. 2006), Auto-Regressive Integrated Moving Average (ARIMA) Zhang, 2003; Makridakis & Hibon, 1997), Kalman filters (Choi et al., 2011; Xie, Song, Sirbu, & Wang, 1997) and so forth that mainly try to model the trend and cyclicity in a series. The use of some multivariate time-series methods such as ARIMAX is methods are preferred for handling covariates forecasting problems where data on external business variables are present (Punia, Nikolopoulos, Singh, Madaan, & Litsiou, 2020). The covariates methods establish relationships among demand and independent variables. Machine learning (ML) methods gained popularity in recent years for demand forecasting. The ML methods model patterns in the demand based on correlations with independent variables. In ML methods, artificial neural networks (ANN) are widely used for demand prediction and reported improvements in the accuracy of forecasts in various cases (Alon, Qi, & Sadowski, 2001; Au, Choi, & Yu, 2008).

Random forest (RF) is based on regression trees and bagging algorithms. The advantages of RF over NNs are in terms of interpretability and accuracy on non-time-series data (Ferreira,

Lee, & Simchi-Levi, 2016). The latest addition to a set of machine learning methods is deep learning (Punia, Singh, & Madaan, 2019). The deep neural network, recurrent neural networks, etc. were used for forecasting in several domains. As reported by Loureiro, Miguéis, and da Silva (2018), results were encouraging to explore further the use of deep learning for sales forecasting.

## 2.2 Research Gaps and Main Contribution

Within the line of research for multi-feature data-driven NVM optimization, some research gaps exist that we identified and aim to bridge through our work. The first research gap is that random forest, a widely used machine learning algorithm for demand forecasting in retail (Ferreira et al., 2016), and similarly, deep neural networks are not used to model a priori nonlinear multi-feature relationships between order quantities and demand data and their impact on inventory performance. The second research gap is that multi-item inventory optimization under the capacity constraint case is not discussed in data-driven decision models for multi-feature NVM. The paper aim to bridge these gaps in the literature by investigating how does a retailer shall use sales data to optimize its inventories under limited resources? To address the research under a capacity constraint. The primary contribution to research in comparison with data-driven approaches is summarized in Table 1.

-- Insert Table 1 --

## 3. Methodology

In this section, we present the problem description and proposed methodology for determining the optimal order quantities for products in multi-item inventory management. This section consists of three parts: 1) demand estimation techniques, 2) inventory optimization techniques, and 3) multi-item inventory optimization under capacity constraint. Following are the main list of notations used in the paper to explain the proposed methodology:

$d _ { i }$ = random variable for the demand for an item ??

$c _ { i } =$ purchasing cost for each unit of item ??

 ?? = selling price for each unit of item ??

$h ^ { i }$ = overage/holding cost per each unit of item ??

$b ^ { i }$ = underage/backordering cost for each unit of item ??

 ?? = total no. of items/products

$G _ { n } = \mathrm { t o t a l }$ no. of items in a product group

 ?? = total resource capacity for all products of a product group

$Q _ { i } o r \ : Q ^ { i }$ = order quantity for item ??

$\pi _ { i } ( Q _ { i } )$ = total cost of inventory for item ??

$Q _ { i } ^ { u }$ = unconstrained order quantity for item ??

$\alpha ^ { i } = b ^ { i } / ( b ^ { i } + h ^ { i } )$ , the critical fractile (optimal service level) for unconstrained newsvendor item ??

$\beta ^ { i } = v ^ { i } / ( b ^ { i } + h ^ { i } )$ , is the ratio of the capacity requirement to the marginal revenue for item ?? The other notations will be defined as and when required.

## 3.1 Problem Description

A multi-item newsvendor problem with unknown demand distributions is considered. The inventory system has a single linear constraint, which represents a limited capacity or a limited budget available with a retailer to spend on the items. The retailer has to decide the optimal quantities required to be ordered before the selling season. As this is variant of newsvendor problem (hereafter, NVP), so as in a classical NVP, overage/holding cost of ℎ, and underage/backordering cost of ?? for each unit is considered. In a (single item) newsvendor model, the objective function is to minimize the total expected cost, which is given by: min<sub>????</sub> $\operatorname { E } [ b ^ { i } ( d ^ { i } - Q ^ { i } ) ^ { + } + h ^ { i } ( Q ^ { i } - d ^ { i } ) ^ { + } ] ,$ (1)

where $Q _ { i }$ is the order quantity, and $d _ { i }$ is the random demand for an item ??. If $F ^ { i } ( . )$ is the cumulative density function of the demand distribution of item ?? and $F ^ { i ^ { - 1 } } ( . )$ is its inverse. The optimal solution to this (unconstrained) problem is given by:

$$
Q ^ {i *} = F ^ {i - 1} \left(\frac {b ^ {i}}{b ^ {i} + h ^ {i}}\right) = F ^ {i - 1} (\alpha^ {i}),\tag{2}
$$

In a case of multiple items with no capacity constraint, the optimal order quantity for each item can be found out by using Eq. (2) for each item. Moreover, the obtained order quantities will also be optimal when the available capacity is greater than or equal to the sum of ordered quantities.

The actual demand distributions for items, $F ^ { i } \forall i = 1 , 2 , \ldots , m$ , are unknown. Only the historical demand data, ${ \cal { S } } = \left\{ \left( d _ { j } ^ { 1 } , X _ { j } ^ { 1 } \right) , \ldots , \left( d _ { j } ^ { i } , X _ { j } ^ { i } \right) , \ldots , \left( d _ { j } ^ { m } , X _ { j } ^ { m } \right) \right\} _ { j = 1 } ^ { ? }$ , where $d _ { j }$ is the demand and $X _ { j }$ is a vector of its covariates with independent features $( \mathrm { { e } \ { \mathrm { ~ g } } . , \mathrm { { r } . i c e } }$ , no. of clicks, promotion, etc.) for each item (??) are known. In this case, either we have to assume the distribution for the inventory optimization. Both methods have their limitations, which are already discussed and well documented in the literature also, e.g assumption-based (empirical) and data-based methods for inventory optimization.

Overall, the following sections present the proposed solution methodology consisting of demand estimation, multi-item inventory optimization steps to develop a complete datadriven model to find the to the above-described problem. In addition, appropriate inventory optimization methods are also discussed to make the discussions complete.

## 3.2 Demand Estimation through Machine/Deep Learning

As the distributions of the actual demand for the products are not known, so general forecasting methods are used for demand estimation. As explained in Section 2, ML methods such as random forest (RF) and deep neural network (DNNs) are used to estimate the demand.

Random Forest (RF) algorithm uses the principle of bagging to reach the final demand prediction. Initially, a q number of bootstrap samples of size, $S _ { \mathrm { n } }$ are randomly selected from the demand data with equal probability and replacement. Say, $\Phi _ { \mathrm { q } }$ is an i.i.d. random variable. The classification and regression trees (CART) algorithm is applied to each sample $( S _ { n } ^ { \phi l } , \ldots , S _ { n } ^ { \phi q } )$ to develop q predicting trees $( \hat { h } ( X , \ S _ { n } ^ { \ \phi l } ) , \ . \ . \ . , \ \hat { h } ( X , \ S _ { n } ^ { \ \phi q } ) )$ (Breiman, 2001). Then demand predictions from the trees are aggregated using Eq. (3) to get the final demand prediction.

$$
Y ^ {\prime} = \frac {1}{q} \sum_ {l = 1} ^ {q} \hat {h} (X, S _ {n} ^ {\varPhi_ {l}})\tag{3}
$$

A deep neural network (hereafter, DNN) takes the demand data and independent variables in the input layer, and then process data using linear and non-linear functions to obtain the output values. The schematic of a fundamental building block of DNN is shown in Figure 1 (a). It (b). The data is processed layer by layer in a way that output from $\sim _ { x }$ layer is fed to a node of the next layer using a sum of weighted input data $( \sum w _ { i } x _ { i } )$ and a non-linear activation function $f .$ . For activation functions are linear $\left( f ( x ) = x \right)$ , sigmoid $\textstyle \left( f ( x ) = { \frac { 1 } { 1 + e ^ { - x } } } \right)$ , rectified linear unit (ReLU) $( f ( x ) = { \{ \begin{array} { l l } { 0 f o r x \leq 0 , } \\ { x f o r x \geq 0 , } \end{array}  }$ , and tanh $\begin{array} { r } { \left( f \left( x \right) = \frac { e ^ { x } - e ^ { - x } } { e ^ { x } + e ^ { - x } } \right) } \end{array}$ . The fully connected network shown in Figure 1 (b) is called a feedforward multilayer neural network, in $\therefore \sin \angle$ weights, biases, and activations functions are used to convert the inputs to the outputs. The DNNs can approximate any continuous function (Glorot & Bengio, 2010), making these suitable to use for demand forecasting when enough historical data is available. Recently DNNs are found to be useful for time-series forecasting problems (Fischer $\&$ Krauss, 2018; Loureiro, Miguéis, & da Silva, 2018). Following this line of research, we develop ML/DL based demand estimation models to leverage the vast amount of data generated by a large number of products in a retail environment to generate accurate demand estimates.

-- Insert Figure 1 --

## 3.3 Inventory Optimization

The maximal approximation, empirical, and proposed data-driven optimization models are presented. The demand estimates from the previous section were used as the inputs and the optimal order quantity $( q _ { i } )$ is the expected outcome from these inventory optimization models.

## 3.3.1 The maximal approximation model

Scarf (1958) provided the min-max model for inventory optimization when demand distributions are unknown, and only mean, and standard deviation of the demand is known to the user. Scarf's ordering rule provides the order quantity, assuming the worst and best possible cases of demand distribution with mean, ??, and standard deviation, ??. The detailed mathematical proof was provided (readers are suggested to refer to Scarf (1958) for the details), which was later extended by the other authors (Gallego & Moon, 1993). The paper use this approximation model and the proposed model.

## 3.3.2 Empirical Demand Distribution Model

Based on the historical demand data, $\boldsymbol { S ^ { i } } = \left\{ \left( \boldsymbol { u } _ { \boldsymbol { J } } ^ { i } \boldsymbol { X } , \right) \right\} _ { \boldsymbol { j } = 1 } ^ { n }$ , the mean demand forecasts are calculated. The forecast errors obtained from demand data and mean forecasts are obtained. The errors are assumed to follow a specific distribution, assumed normal distribution here. The parameters of the normal distribution – mean $( \mu _ { i } )$ and standard deviation $( \sigma _ { i } )$ , and thus, cumulative distribution function, $F ^ { i } ( . ) , \mathsf { a r t }$ calculated using forecast errors. The optimal solution to the inventory optimization pro $Q _ { i }$

$$
Q _ {i} ^ {*} (X _ {j}) = a _ {i} (X _ {j}) + \inf \left\{y: F ^ {i} (p, \mu_ {i}, \sigma_ {i}) \geq \left(\frac {b ^ {i}}{b ^ {i} + h ^ {i}}\right) \right\}\tag{4}
$$

Where $\widehat { d } _ { \iota }$ is the mean demand forecast, $X _ { j }$ are the independent features, and $\frac { b ^ { i } } { b ^ { i } + h ^ { i } }$ is the optimal service level, which represents the probability of satisfying demand in a period, ??.

## 3.3.3 Proposed inventory optimization model: QR-ML

The proposed approach uses the quantile regression - machine learning (QR-ML) methods and helps to reduce the burden of the calculating mean forecast, forecast errors, and assuming a specific distribution of the forecast errors. In this approach, the optimal order quantities are directly calculated using historical demand and independent features data for an item ??, i.e. $\left\{ d _ { j } ^ { i } , X _ { j } ^ { i } \right\} _ { j = 1 } ^ { n }$ . The proposed approach is based on the machine learning principle of empirical risk minimization (ERM) (Vapnik, 1998). The ERM approach assumes that optimal order quantity is a linear function of the features and, thus, can be formulated as a linear program (Ban & Rudin, 2018). This ERM approach is extended to non-linear relationships by incorporating the ML methods, in the following way:

$$
\begin{array}{r l} \min _ {Q ^ {i} (\varphi^ {i}, X)} \hat {R} (Q ^ {i} (\varphi^ {i}, X); S ^ {i}) & = \min _ {q ^ {i}} \frac {1}{n} \sum_ {j = 1} ^ {n} \bigg [ b ^ {i} \left(d _ {j} ^ {i} - Q _ {j} ^ {i} (\varphi^ {i}, X _ {j})\right) ^ {+} \\ & \quad + h _ {j} ^ {i} \big (Q _ {j} ^ {i} (\varphi^ {i}, X _ {j}) - d _ {j} ^ {i} \big) ^ {+} \bigg ], \end{array} \tag {5}\tag{5}
$$

where, $Q _ { j } ^ { i } \big ( \varphi ^ { i } , X _ { j } \big )$ is the output in the period $j \sin ^ { \cdot + h } X _ { j }$ as the input and $\varphi ^ { i }$ are the parameters of the ML-based demand estimation method. The following problem can be reformulated using the dummy variables $u _ { j } ^ { i }$ and $o _ { j } ^ { i } { \hat { \quad } } { \mathrm { ~ r ~ } }$ the underage and overage in period $j .$ . The

$$
\begin{array}{r l} & {\min \hat {R} (Q ^ {i} (\varphi^ {i}, X); S ^ {i})} \\ & {\qquad Q ^ {i} (\varphi^ {i}, X)} \end{array} = \min _ {q ^ {i}} \frac {1}{n} \sum_ {j = 1} ^ {n} \left[ b ^ {i} \big (a _ {j} ^ {i} - Q _ {j} ^ {i} (\varphi^ {i}, X _ {j}) \big) ^ {+} + h _ {j} ^ {i} \big (Q _ {j} ^ {i} (\varphi^ {i}, X _ {j}) - d _ {j} ^ {i} \big) ^ {+} \right] \equiv \min \frac {1}{n} \sum_ {j = 1} ^ {n} \left(b ^ {i} u _ {j} ^ {i} + a _ {j} ^ {i} o _ {j} ^ {i}\right)
$$

subject to $\forall \ : \mathrm { j } = \ : \mathbf { 1 } , \ : ? , \ : \dots , \ : \mathrm { r }$ 1

$$
u _ {j} ^ {i} \geq d _ {j} ^ {i} - Q _ {j} ^ {i} (\varphi^ {i}, X _ {j})
$$

$$
o _ {j} ^ {i} \geq Q _ {j} ^ {i} (\varphi^ {i}, X _ {j}) - d _ {j} ^ {i},
$$

$$
u _ {j} ^ {i}, o _ {j} ^ {i} \geq 0
$$

The NV-ERM is an NLP of ?? + 2?? dimensional decision vector and 4?? constraints. The objective of the NLP is to minimize the overall empirical risk $\left( { \hat { R } } \right)$ of backordering and holding, i.e., the deviation of demand estimates from actual demand is correctly assigned to underage and overage. The objective function, $\hat { R }$ is a function of $Q ^ { i } ( \varphi ^ { i } , X )$ with respect to the data, $S ^ { i }$ . Using data, $S ^ { i }$ , the parameters of the ML method $( \varphi ^ { i ^ { * } } )$ are obtained for the minimization of empirical risk, ??̂ in NV-ERM. The corresponding order quantity for item ?? in period ?? is the quantile forecast of $Q _ { j } ^ { i } \big ( \varphi ^ { i ^ { * } } , X _ { j } \big )$ ).

Ban and Rudin (2018) and Huber et al. (2019) showed that the objective function of the NV-ERM has the same form as that of loss function of high-dimensional quantile regression (QR) and thus, it can be solved using QR and the demand data. The loss function of QR is given by:

$$
\mathcal {L} \big (\xi_ {j} | \alpha \big) = \left\{ \begin{array}{c c} \alpha \xi_ {j} & i f \xi_ {j} \geq 0 \\ (1 - \alpha) \xi_ {j} & i f \xi_ {j} <   0 \end{array} \right.\tag{6}
$$

where $\xi _ { j }$ is the error and $0 < \alpha < 1$ . By using quantiles of underages $( \alpha \in ( 0 , 1 ) )$ and overages (1 − ??), an estimate for the quantile in inventory optimization can be obtained by using the following loss function, $\begin{array} { r } { \sum _ { j = 1 } ^ { n } \left( \alpha { \left( d _ { i } - \widehat { d } _ { \iota } \right) } ^ { + } + ( 1 - \operatorname { \gamma } ) { \left( \widehat { \lambda } _ { \iota } - d _ { i } \right) } ^ { + } \right) } \end{array}$ (Koenker, 2005). In this loss function, $\begin{array} { r } { \alpha ^ { i } = \frac { b ^ { i } } { b ^ { i } + h ^ { i } } } \end{array}$ of demand distribution $\begin{array} { r } { \mathrm { ~ \mathfrak ~ { ~ n ~ } ~ } \cdot 1 ^ { - } \alpha ^ { i } ) = \frac { h ^ { i } } { b ^ { i } + h ^ { i } } } \end{array}$ and using these values of $\alpha ^ { i }$ and $( 1 - \alpha ^ { i } )$ quantile regression with the direct input of demand data and independent variables.

3.4 The multi-item inventory optimization with a capacity constraint

As mentioned in the literature, in retail stores, products are arranged into hierarchies where one product group breaks down into several of its variants (Figure 2). This hierarchies are utilized to improve accuracy and efficiency of the demand estimation algorithm in the literature (Dangerfield & Morris, 1992; Gross & Sohl, 1990; Villegas & Pedregal, 2018) and in this study, it is used in solving the capacity constraint problem in multi-item inventory management in situations where a retailer has limited capacity (shelves) at the product group level, e.g., packaged foods of different flavors, etc.

-- Insert Figure 2 --

In a product group (PG), as shown in Figure 2, the products are of similar characteristics so that these can be assumed of a similar cost structure. By similar cost structure, it is meant that 1) underage cost of products is decided by a constant markup from the unit price, i.e. $b ^ { i } = m * c _ { i }$ and 2) overage cost of products is a constant proportion of the unit cost, i.e. $h ^ { i } = c _ { i } * d$ . As mentioned in the literature, these two conditions are generally valid for products in a retail store (Ding, Dong, & Pan, 2016; Villegas & Pedregal, 2018). So, the inventory optimization algorithm (QR-ML) is applied at product groups levels, and unconstrained optimal quantities are found out.

To derive the optimal order quantities $( Q _ { i } ^ { * } )$ at product level from unconstrained optimal quantities $( Q _ { P G i } ^ { * } )$ at the product groups, three possible cases can arise when a capacity constraint is active. Say, available capacity for each group is $C _ { P G i }$ . Then three possible cases are 1) $Q _ { P G i } ^ { * } <$ $C _ { P G i }$ , 2) $Q _ { P G i } ^ { * } = C _ { P G i }$ , and 3) $Q _ { P G i } ^ { * } > C _ { P G i }$ . For the first two cases, as the capacity constraint is already satisfied, and, it is proposed to use historical $\mathrm { { d e } } ^ { \lnot \cdot \ l _ { 2 , \ldots } }$ proportions as in top-down hierarchies to find the optimal quantities for products. The top-down is an efficient way of obtaining accurate forecasts (Gross & Sohl, 1990) . The historical demand proportions are calculated from the available historical demand data (Sbrana & Silvestrini, 2013).

For the third case, we used the $\boldsymbol { r } _ { \mathrm { \perp } } \mathrm { e a } \mathrm { \perp }$ and variance of items to find the optimal order quantities individually for all items. The works of Nahmias and Schmidt (1984), Gallego and followed to develop a data-driven heuristic solution. In general, multi-item NVP can be written as Z:

$$
\begin{array}{l} \min \pi = \sum_ {k = 1} ^ {G _ {n}} \pi_ {k} (Q _ {k G}) \\ \text {subject to} \\ \quad \sum_ {k = 1} ^ {n} v _ {k} (Q _ {k}) \leq C, \text {and} Q _ {k} \geq 0 \forall k = 1, 2, \dots , G _ {n} \end{array}\tag{Z}
$$

With the assumption of the similar cost structure for the items under a PG, optimal service levels, $\begin{array} { r } { \alpha _ { k } \left( = \frac { b ^ { k } } { b ^ { k } + h ^ { k } } \forall k = 1 , 2 , \dots , G _ { n } \right) } \end{array}$ are identical, and ratios of revenue per unit due to selling versus salvaging, $\begin{array} { r } { \beta _ { k } \left( = \frac { v ^ { k } } { b ^ { k } + h ^ { k } } \forall k = 1 , 2 , \dots , G _ { n } \right) } \end{array}$ , for all items will also be identical. $S 0 ,$ we can write the following property regarding optimal order quantities of these ?? items.

???????????????? 1. If $\alpha _ { k } = \alpha .$ , and $\beta _ { k } = \beta ,$ , for $k = 1 , 2 , \dots , G _ { n }$ , then $F _ { 1 } ( Q _ { 1 } ^ { * } ) = \dots = F _ { k } ( Q _ { k } ^ { * } ) = \dots =$ $F _ { G _ { n } } ( Q _ { G _ { n } } ^ { * } )$

This property holds even when a capacity constraint is present and for any set of demand distributions of items. Based on Property 1, we can get optimal order quantities for all items from the following theorem.

??ℎ?????????? 1. Suppose $l _ { 1 } , l _ { 2 } , \ldots , l _ { m }$ are the common shape parameters of the $G _ { n }$ demand distributions and transformation T is defined as $\begin{array} { r } { T ( d _ { i } , \mu _ { i } , \sigma _ { i } , l _ { 1 } , l _ { 2 } , \dots , l _ { m } , f , g ) = \frac { d _ { i } - [ \mu _ { i } - \sigma _ { i } f ( l _ { 1 } , l _ { 2 } , \dots , l _ { m } ) ] } { \sigma _ { i } g ( l _ { 1 } , l _ { 2 } , \dots , l _ { m } ) } , } \end{array}$ where $f , g$ are the functions of the shape parameters. Under the capacity constraint and condition that $T ( d _ { i } , \mu _ { i } , \sigma _ { i } , l _ { 1 } , l _ { 2 } , \ldots , l _ { m } , f , g ) \sim$ $T \bigl ( d _ { j } , \mu _ { j } , \sigma _ { j } , l _ { 1 } , l _ { 2 } , \ldots , l _ { m } , f , g \bigr ) \forall ( i , j ) \in \{ 1 , 2 , \ldots , G _ { n } \}$ , the optimal quantity is given by

$$
Q _ {k} ^ {*} = \mu_ {k} + \sigma_ {k} \frac {C - \sum_ {k = 1} ^ {G _ {n}} v _ {j} \mu_ {j}}{\sum_ {k = 1} ^ {G _ {n}} v _ {j} \sigma_ {j}}\tag{7}
$$

## ??????????: Appendix I.

Theorem 1, under the assumption of products $i , j$ have identical distribution (denoted by \~ in Theorem 1), provides the conditions to get the optimal order quantities for the products of a PG. Note that the expression for optimal quantities is free from any specific distribution assumption; hence, we accomplish our goal of providing a data-driven solution to the multi-item inventory optimization.

Overall, a data-driven solution to multi-item inventory optimization is provided using the proposed QR-ML approach and a heuristic. In the proposed framework, the computation efforts will get reduced by a factor of $N / M$ in an ideal case when all forecasts of PGs are less than capacity, where N is the number of products, M is the number of product groups. This novel approach is used to solve a multi-item NVM using top-down hierarchies; thus, we may call it a top-down NVM (TD-NVM). The performance of the proposed approach is investigated in detailed empirical analysis in the next section.

## 4. Empirical Evaluation

In this section, first, the data used for empirical analysis are described in detail. After that, the basic details and parameter setup for time-series methods, i.e., seasonal naïve, ETS, ARIMA, and ARIMA with external regressors; and machine learning methods, i.e., multiple regression, neural networks, and random forest are discussed. The different forecasting methods are evaluated on multiple performance criteria to judge the best demand forecasting method. The impact of these methods on inventory cost is analyzed. After that, inventory optimization techniques - maximal approximation, the empirical optimization (normal distribution), and the proposed method – quantile regression - machine learning (QR-ML) method, as explained in Section 3.3, are applied. The results from these inventory optimizations are analyzed to select the best model based on minimum inventory cost.

## 4.1 Data and Descriptive Statistics

The real-world data is collected from a retailer who sells perishable food items. The dataset consists of point-of-sales data for such items and is available for 156 weeks. The retailer has to decide the order quantities for each item per week, and in this way, the business requires at least 16 inventory decision makings every week. The time-series data consist of multiple independent variables related to point-of-sales, promotions, store, calendar, holidays, weather, etc. The summary statistics of the variables from the dataset are provided in Table 2.

-- Insert Table 2 --

Here economic activity index (Econ\_Index) measures the average economic growth in a metropolitan area (Arias, Gascon, & Rapach, 2016) and found to be a good indicator of sales in the literature (Badorf & Hoberg, 2020). The data for weather and economic indicators is collected through the website of the National Oceanic and Atmospheric Administration (NOAA), USA. Four weeks of data were used as the test dataset, and the rest of the data is used as the training dataset.

4.2 Forecasting methods, Parameter Setup, and Performance Metrics

The widely used time-series methods for sales forecasting like seasonal naïve, ETS, and ARIMA (Auto-Regressive Integrated Moving Average); and machine learning methods like multiple regression, artificial neural network, and random forest, are used as the benchmarking forecasting methods. Also, we provide the details and parameter selection of these methods for our forecasting purposes.

## 4.2.1 Time-series methods

In the seasonal naïve method, actual demand from some last period is used as the forecast demand is strongly dependent on some previous period's demand. The forecast for the next period is equal to actual values from the kth period of the past season, i.e. $\hat { y } _ { t + 1 } = y _ { t + 1 - k }$ . In our case, we used the frequency of k=4. The number was selected based on the acf plots of the residuals from the naïve forecasts as k = 4 resulted in non-significant autocorrelation in the acf plots of residuals.

ETS is a class of exponential smoothing methods that are used to model the error, trend, demand based on a weighted sum of previous observations. The advanced versions, double and triple exponential smoothing, use the trend and seasonality also to produce more accurate forecasting results. The forecast package (Hyndman & Khandakar, 2008) is used to estimate the parameters of the models for demand forecasting in our case.

ARIMA (Auto-Regressive Integrated Moving Average) method is widely applied for demand forecasting in the supply chain (Gaur, Giloni, & Seshadri, 2005). ARIMA model combines the autoregressive (AR) and moving average (MA) model of time series forecasting. AR(p) model uses past observations to predict future values. The AR model is defined as: $y _ { t } = c + \Phi _ { 1 } \mathrm { y } _ { { \mathrm { t } } - 1 } + \Phi _ { 2 } \mathrm { y } _ { { \mathrm { t } } - 2 } + \cdots + \Phi _ { \mathrm { p } } \mathrm { y } _ { { \mathrm { t } } - \mathrm { p } } + \mathrm { e } _ { \mathrm { t } } . ~ y _ { t }$ is regressed over $p$ time-lagged value of $y _ { t }$ , and $\mathrm { e } _ { \mathrm { t } } .$ , which is the white noise in the time series. $\Phi _ { 1 }$ and ?? are the model parameters. Similarly, in MA(q) model is defined as: $y _ { t } = c + \mathsf { \boldsymbol { \theta } } _ { 1 } \mathsf { e } _ { { \mathsf { t } } - 1 } + \mathsf { \boldsymbol { \theta } } _ { 2 } \mathsf { e } _ { { \mathsf { t } } - 2 } + \cdots + \mathsf { \boldsymbol { \theta } } _ { \mathsf { q } } \mathsf { e } _ { { \mathsf { t } } - \mathsf { q } } + \mathsf { \boldsymbol { e } } _ { \mathsf { t } }$ . In MA(q) model, past forecast error values are used rather than forecast variable values. $y _ { t }$ is regressed over q time-lagged errors and, $\theta _ { 1 }$ and c are model parameters. Overall, ARIMA (p, d, q) is defined as: $y _ { \phantom { ' } t } ^ { \phantom { ' } } = c + \Phi _ { 1 } ^ { \phantom { ' } } \mathrm { y } _ { \phantom { ' } t - 1 } ^ { \prime } + \cdots + \Phi _ { \mathrm { p } } \mathrm { y } _ { \phantom { ' } t - \mathrm { p } } ^ { \prime } + \Theta _ { 1 } \mathrm { e } _ { \mathrm { t } - 1 } + \cdots + \Theta _ { q } \mathrm { e } _ { \mathrm { t } - \mathrm { q } } + \mathrm { e } _ { \mathrm { t } } .$ The $\boldsymbol { y } _ { \ t } ^ { \prime }$ represents the differenced value of the dependent variable. p, q, and d are the parameters of the ARIMA model. d is the degree of differencing. ARIMA model is fitted, and optimal parameters of the ARIMA model are estimated such that errors are minimized. The Box-Jenkins method with Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) as error minimization criteria were used to find the values of parameters ??, ??, ?????? ??.

## 4.2.2 Machine learning methods

Feedforward Neural Networks (FNNs). Single-layer feed-forward neural networks are The FNN has three types of layers, namely, an input layer, an output layer, and hidden layers. The number of hidden layers was restricted (equal to 1) as with more than one hidden layer configurations are covered by DNN. The inputs $( X _ { 1 } , X _ { 2 } , \ldots , X _ { p } )$ and $\left( \boldsymbol { y } _ { t } \right)$ are related through the equation: $y _ { t } = \alpha _ { o } + \sum _ { j = 1 } ^ { q } \alpha _ { j } g \big ( \beta _ { o j } + \sum _ { i = 1 } ^ { p } \beta _ { i j } \boldsymbol { X } _ { \iota - i } \big ) \textsf { r } \varepsilon _ { t }$ , where ??s and $\beta \mathrm { s }$ are connection weights, p is the number of input nodes and q is the number of hidden nodes. The final output of the network is $y _ { t } = f \bigl ( X _ { 1 } , X _ { 2 } , \ldots , X _ { p } , w \bigr ) + \mathfrak { c } _ { v }$ , where ?? is a vector of all parameters, and f is a non-linear function that maps the $\mathrm { i n _ { \mathrm { l } } \cdot \mathrm { \Psi } ^ { \mathrm { t r } } }$ to outputs with the help of w and connection weights. Thus, the neural network is equivalent to a nonlinear model. In our model, while architecting the neural network, time-series data was de-trended and deseasonalized through differencing, and then we used the single-layer feed-forward neural network.

Random Forest (RF). The details of the RF algorithm are already explained in Section 3.2, so only important parameters of RF are discussed here. There are two main characteristics of the RF, namely, the generalization error and the measure of variable importance (MOVI). The former is also known as out-of-bag-error (OOBE) and is the estimation of the generalization ability of the model. It is the mean prediction error of the out of sample or first-seen observations and serves the purpose of internal cross-validation. The OOBE is given by ???????? = $\textstyle { \frac { 1 } { n } } \sum _ { i = n } ^ { n } ( Y _ { i } - { \widehat { Y } } _ { \imath } ) ^ { 2 }$ . On the other hand, the MOVI is obtained by permuting a feature and averaging the difference in OOBE before and after permuting over all trees, ???????? $\begin{array} { r } { ( X ^ { j } ) = \frac { 1 } { q } \sum _ { l = 1 } ^ { q } ( O \widetilde { O B E } _ { l } - } \end{array}$ $O B B E _ { l } )$ . The higher the value of MOVI(X <sup>j</sup>), the more critical is feature $X ^ { j } .$ Through OOBE and MOVI, the RF provides the best fit among independent variables and targets. The parameters are explained in Section 4.3.

## 4.2.3 Performance Metrics

The performance of the forecasting methods is compared using three essential characteristics. These are:

 Bias – to check the forecasting method for its tendency of over-forecasting or underforecasting of actual values.

 Accuracy – to check how closely forecasted values conforms to the actual values.

 Uncertainty – to check the average deviation of the forecast from the mean forecast.

The performance metrics used to measure the characteristics mentioned above are as follows: mean error (ME), mean absolute error (MAE) and root mean squared error (RMSE) for bias, accuracy, and variance (Hyndman & Koehler, 2006). The practice-oriented accuracy metric, mean absolute percen tage error (MAPE), is also included in the analysis. The multiple performance metrics are used because each of these metrics has some strengths and weaknesses. For example, MAE and RMSE are scale-dependent. MAPE is bounded on a lower limit and unbounded on the upper limit.

As the errors are calculated for multiple demand series, these errors are aggregated to get a single metric to compare the forecasts known as average error. Because the performance of different forecasting methods is compared, therefore, the relative measures are also included. The relative metrics are easy to interpret, scale, and allows to summarize the results from different series concisely and coherently (Davydenko & Fildes, 2013; Shankar, Ilavarasan, Punia, & Singh,

2019). The relative mean error, relative mean absolute error, and relative mean squared errors are used to compare the performance of these methods. These relative errors are calculated by dividing the sum or mean of errors from the evaluated method by that of a benchmark method. The seasonal naïve method is used as a benchmark method.

Also, a practice-oriented approach, FVA (forecast value-added) analysis is performed to compare the forecasting methods based on MAPE (Gilliland & Sglavo, 2010). FVA helps to identify percentage improvement by a method over other methods and benchmark methods. FVA consists of following three steps approach:

1) Calculate forecasting accuracy using MAPE, i.e. (100 – MAPE),

2) Estimation of FVA points to know the performance of the proposed model over the benchmarking model using the following equation:

?????? =

(???????????????? ???????????????? ???? ???????????????? ??????ℎ????) −

(???????????????? ???????????????? ???? ????????ℎ???????? ??????ℎ????)

3) Estimation of marginal improvements in forecasting accuracy by a different method.

In this way, the following metrics are used for the analysis: mean error, mean absolute error, root mean squared error, mean absolute percentage error, the relative average mean error, the relative average mean absolute error, relative average root mean squared error and FVA analysis. 4.3 Demand Estimation: Results and Discussions

To implement the forecasting models, parameter tuning was performed. The k= 4 for the naïve method is selected based on acf plots of the residuals. The auto.arima and ets functions were used for auto-selection of the parameters, and the seasadj function is used for the deseasonalized series for FNN from the forecast package in R language (Hyndman & Khandakar, 2008). For the optimization of the number of nodes, the grid search algorithm is used in FNN. For RF, repeated cross-validation with a random search grid is used to find the best set of parameters (Fischer & Krauss, 2018). The maximum depth = 20, and the number of trees were allowed to be 500, and the number of variables randomly sampled as candidates at each split (mtry) was left default as ${ \sqrt { p } } ,$ where p is the number of variables (Breiman, 2001). For DNNs, we used the network with three hidden layers with a different set of nodes varying from 12 to 36 (and input layer of 12 and output layer of 1 node) were used and optimal configuration was selected by hyperparameter optimization performed by designing a grid search within Keras (Bergstra & Bengio, 2012). Besides, dropout of {01-0.5} and L1 regularization was used to avoid overfitting.

The results from the demand estimations are presented in Table 3. Three months of data is used as test data for the calculation of out-of-sample-errors. $\smash {  { \mathbf { T } } ^ { 1 } \ b { \mathbf { \Phi } } } _ { \perp = 1 } ^ { \cdot 1 } \ b { \mathbf { \Phi } } _ { \perp , 3 }$ (ME), accuracy (MAE) and variance (RMSE), and other measures of accuracy of the forecasts are presented. It is observed that mean errors (bias) for the methods (except RF and ARIMAx) are negative, which means that these methods are underestimating the demand. RF has the smallest mean error, i.e. on average, predictions from RF are neither underestimated nor overestimated, and thus, it can be said that RF has a minimum bias in prediction. MAEs suggests that the accuracy of machine learning methods RF and DNN are significantly more accurate than other methods. A similar trend is variance, too, among all method

During analysis, it was observed that forecasting of sales pattern of a few products is dependent on the time-based components and as well as on independent variables. The hybrid methods are suitable for this type of pattern prediction. Thus, for the proof of the concept, a stateof-the-art hybrid method, ARIMAx, is included in the analysis. ARIMAx is an extended version of the ARIMA which considers the independent variables too. ARIMAx is a hybrid of ARIMA and multiple linear regression, and its advantage is that it uses the autocorrelation present in the residuals, and regression between demand and independent variables to improve the forecasting accuracy of the model. As evident from Table 3, ARIMAx is performing better than the timeseries method due to the added prediction power of regression. Punia et al. (2020) can be referred for a detailed study on hybrid machine/deep learning methods.

Overall, RF and DNN are better than other methods on all three characteristics viz. bias, accuracy, and variance. MAPE results also established that RF is best among all methods. For a concise and scale-independent comparison of the error metrics, the relative errors viz. Rel-ME, Rel-MAE, and Rel-RMSE are also presented in Table 3.

-- Insert Table 3 --

The value-added analysis for forecasts in Table 4 suggests that except ETS, all other methods have better forecast accuracy than the s-naïve, the benchmark method. The comparative improvements in FVA analysis show a significant jump in forecast accuracy from ARIMA (a time-series method) to ARIMAx, which highlights the significance of using external business information in the data-driven prediction models. DNN and RF are the best and have small but significant incremental improvements in the forecast accuracy over ARIMAx.

\- Insert Table 4 --

## 4.4 Inventory Analysis

For inventory analysis, we are using data for four product groups consisting of a total of 16 products. As explained in Section 3.4, these products can be mapped to the structure of a products' hierarchy. The products in each group exhibit very similar characteristics. The inventory analysis is initiated with each group, which later taken to the product level with the help of top-down product hierarchies and proposed heuristic.

## 4.4.1 Effects of demand estimation on inventory costs

The demand estimates for the next period in the newsvendor model for each product group (PG) are used in the NVM to calculate the inventory costs. The inventory costs are calculated at the optimal service level $\left( \frac { b ^ { i } } { b ^ { i } + h ^ { i } } \right)$ . The average relative inventory costs for different product groups are presented in Table 5.

-- Insert Table 5 --

The machine learning methods (RF and DNN) have better performance than time-series methods in all cases except PG2, where ARIMAx is best. The better performance of ML methods can be attributed to the large data used by these methods to produce more robust and accurate forecasts. These robust forecasts lead to better inventory costs. The results from the PG2 are showing an aberration, which further supports our proposition in Section 4.4 that some demand patterns of some products can be better modeled through a hybrid method. As here, ARIMAx has a lower cost than time-series and ML methods. Overall, from Table 5, it can be concluded that demand estimation significantly impacts inventory costs.

## 4.4.2 Effects of inventory optimization techniques on inventory cost

QR-ML method are compared with the cost from the maximal approximation approach. The average inventory costs for each product group are calculated and plotted in Figure 3.

-- Insert Figure 3 –

The plots in Figure 3 are analyzed in two different dimensions. First, along with demand impact from inventory optimization techniques. Second, it can be observed, among inventory optimization models, that normal distribution based NVM has a lower cost than MA in all of the cases, and proposed QR-ML based inventory optimization has a lower cost than normal distribution based empirical model except in a few cases where the difference is relatively small and non-significant. Therefore, the proposed approach of quantile regression-based machine learning inventory optimization is performing better than other combinations. It is because of the prediction power of the ML method and efficient use of data for optimization in-place of assuming erroneous demand distributions for inventory optimization.

## 4.4.3 The multi-item capacity allocation

After finding the minimum cost unconstrained quantities for PGs, the product level optimal quantities are derived in this section. The available capacity for each product group is 200 units in the store. The optimal order quantity for each of the products is estimated through QR-RF based inventory optimization technique. The order quantities found out to be 192, 199, 213, and 184 units for PG1, PG2, PG3, and PG4, respectively. Overall, the total quantity is 788, which is under the total available capacity of 800 units. However, at the PG level, only three

-- Insert Figure 4 --

To apply top-down allocation of capacity to products, the historical proportion is calculated for all product hierarchies. The hierarchies and historical demand proportion are shown in Figure 4. Except for PG3, direct order quantities can be found out by direct allocation, i.e. $Q ^ { i * } = p * Q _ { G } ^ { \phantom { * } } { } ^ { * }$ , where p is the proportions $\operatorname { a n c } Q ^ { i * }$ is the optimal order quantities for a product of a product group G, and ${ Q _ { G } } ^ { * }$ is the optimal aggregate quantity for a product group G. The order quantities for products of PG1 , PG2, and PG4 are presented in Table 6 (rounded off to higher numbers). For PG3, using the standard deviation of the items in Eq. (7), the optimal quantities are found out and are als presented in Table 6.

$$
- - \text { Insert   Table } 6 - -
$$

Finally, the total cost is calculated for all products and plotted for three inventory optimization techniques within the multi-item case. As shown in Figure 5, the total cost for the proposed approach QR-RF is found to be lower than the multi-item approach of Gallego and Moon (1993). Also, the effect of accurate demand estimations is clearly dominating the effect of inventory optimization techniques.

-- Insert Figure 5 –

Overall, through the above analyses, it can be said that: 1) the proposed machine learning methods are significantly better than other benchmarking methods for demand estimation, and 2) the performance of proposed QR-ML inventory optimization techniques found to be better than other inventory optimization techniques approaches. Also, the proposed heuristic provided the optimal order quantities for the products within capacity constraint from already minimum cost order quantities of their respective product groups.

## 5. Conclusion

In this paper, we proposed a data-driven solution to a multi-item newsvendor model with a capacity constraint. The proposed model uses the machine learning-based quantile regression to obtain the order quantities for the newsvendor model in a single step. Thus, it eliminates the need for separate demand estimation and inventory optimization processes. Besides, it includes a heuristic to provide the order quantities under competitive resource requirements among multiple products. Through the proposed method, $\smash { \mathrm { W } _ { \mathrm { ~ \breve { ~ } \sim ~ } } \mathrm { \ell _ { 1 } ^ { \cdot } l _ { 2 } } } , \ell _ { 1 } ^ { \cdot }$ two crucial research gaps in the literature on data-driven multi-item inventory optimization. The first gap was to use advanced non-linear second gap was to extend the data-driven model to solve the multi-item newsvendor problems with a capacity constraint. Filling these gaps will help in solving the demand forecasting and inventory management problems, which are relevant to many industries, such as fast-food, fashion clothing, groceries, bakeries, sports goods, and perishable products industry.

The performance of the proposed method is investigated through several analyses, and the following important observations are worth mentioning here. These are: 1) the external variables play a significant part in enhancing the accuracy of the demand estimation method, 2) the machine and deep learning methods outperformed the time-series methods for demand estimation with large datasets, 3) the accurate demand estimations have significant impact on total cost of the inventory management, and 4) the proposed data-driven QR-ML approach is better than the empirical solution.

The data-driven models incorporating machine learning methods for the newsvendor model are an active field of research; thus, the research can be extended in several directions. As come up during analyses, the use of hybrid demand estimation methods and their incorporation in quantile regression's loss function will be a good opportunity to explore. Especially, it includes designing more advanced deep learning-based method to develop the data-driven model for newsvendor problem. Finally, solving multi-period newsvendor models using data-driven methods will be an exciting area for future research.

## Appendix I

Since $T ( d _ { i } , \mu _ { i } , \sigma _ { i } , l _ { 1 } , l _ { 2 } , \ldots , l _ { m } , f , g ) \sim T \big ( d _ { j } , \mu _ { j } , \sigma _ { j } , l _ { 1 } , l _ { 2 } , \ldots , l _ { n } , f , \iota \big ) \ \forall \ ( i , j ) \ \in \{ 1 , 2 , \ldots , G _ { n } \}$ , and

$$
F _ {i} (Q _ {i} ^ {*}) = F _ {i} \left(Q _ {j} ^ {*}\right) \forall (i, j) \in \{1, 2, \dots , G _ {n} \}
$$

therefore ,

$$
\frac {Q _ {i} ^ {*} - [ \mu_ {i} - \sigma_ {i} f (l _ {1} , l _ {2} , \ldots , l _ {m}) ]}{\sigma_ {i} g (l _ {1} , l _ {2} , \ldots , l _ {m})} = \frac {Q _ {j} ^ {*} - [ \mu_ {j} - \sigma_ {j} f (l _ {1} , l _ {2} , \ldots , l _ {m}) ]}{\sigma_ {j} g (l _ {1} , l _ {2} , \ldots , l _ {m})}, o r
$$

$$
Q _ {j} ^ {*} = \mu_ {j} - \sigma_ {j} f (l _ {1}, l _ {2}, \dots , l _ {m}) + \frac {\sigma_ {j}}{\sigma_ {i}} * (\mathcal {C} _ {i} ^ {*} - [ r _ {i} - \sigma_ {i} f (l _ {1}, l _ {2}, \dots , l _ {m}) ])
$$

Multiply both sides by $v _ { j }$ and aggregate over $j ,$ ,

$$
\sum_ {j = 1} ^ {G _ {n}} v _ {j} Q _ {j} ^ {*} = \sum_ {j = 1} ^ {G _ {n}} v _ {j} [ \mu_ {j} - c _ {j} t (l _ {1}, l _ {2}, \dots , l _ {m}) + \frac {\sigma_ {j}}{\sigma_ {i}} * (Q _ {i} ^ {*} - [ \mu_ {i} - \sigma_ {i} f (l _ {1}, l _ {2}, \dots , l _ {m}) ]) ]
$$

Given, $\textstyle \sum _ { j = 1 } ^ { G _ { n } } v _ { j } Q _ { j } ^ { * } = C$ , where $C$ is the capacity for items under a PG, hence,

$$
Q _ {i} ^ {*} = \mu_ {i} + \frac {\sigma_ {i}}{\sum_ {j = 1} ^ {G _ {n}} v _ {j} \sigma_ {j}} \Bigg (C - \sum_ {j = 1} ^ {G _ {n}} v _ {j} \mu_ {j} \Bigg).
$$

$_ { \mathrm { 0 r } } ,$ for a $K ^ { t h }$ product of a PG,

$$
Q _ {k} ^ {*} = \mu_ {k} + \sigma_ {k} \frac {C - \sum_ {k = 1} ^ {G _ {n}} v _ {j} \mu_ {j}}{\sum_ {k = 1} ^ {G _ {n}} v _ {j} \sigma_ {j}}\tag{QED.}
$$

## References

Alon, I., Qi, M., & Sadowski, R. J. (2001). Forecasting aggregate retail sales: A comparison of artificial neural networks and traditional methods. Journal of Retailing and Consumer Services, 8(3), 147–156.

Arias, M. A., Gascon, C. S., & Rapach, D. E. (2016). Metro business cycles. Journal of Urban Economics, 94, 90–108. doi: 10.1016/j.jue.2016.05.005

Au, K.-F., Choi, T.-M., & Yu, Y. (2008). Fashion retail forecasting by evolutionary neural networks. International Journal of Production Economics, 114(2), 615–630. doi: 10.1016/j.ijpe.2007.06.013

Badorf, F., & Hoberg, K. (2020). The impact of daily weather on retail sales: An empirical study in brick-and-mortar stores. Journal of Retailing and Consumer Services, 52, 101921.

Ban, G.-Y., & Rudin, C. (2018). The Big Data Newsvendor: Practical Insights from Machine Learning. Operations Research, 67(1), 90–108. doi: 10.1287/opre.2018.1757

Bergstra, J., & Bengio, Y. (2012). Random search for hyper-parameter optimization. Journal of

Bertsimas, D., & Thiele, A. (2006). A robust optimization approach to inventory theory. Operations Research, 54(1), 150–168.

Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32.

Chen, X., Sim, M., & Sun, P. (2007). A robust optimization perspective on stochastic programming. Operations Research, 55(6), 1058–1071. doi: 10.1287/opre.1070.0441

Dangerfield, B. J., & Morris, J. S. (1992). Top-down or bottom-up: Aggregate versus disaggregate extrapolations. International Journal of Forecasting, 8(2), 233–241. doi:

Davydenko, A., & Fildes, R. (2013). Measuring forecasting accuracy: The case of judgmental adjustments to SKU-level demand forecasts. International Journal of Forecasting, 29(3), 510–522.

Ding, Q., Dong, C., & Pan, Z. (2016). A hierarchical pricing decision process on a dual-channel problem with one manufacturer and one retailer. International Journal of Production Economics, 175, 197–212. doi: 10.1016/j.ijpe.2016.02.014

Erlebacher, S. J. (2000). Optimal and heuristic solutions for the multi-item newsvendor problem with a single capacity constraint. Production and Operations Management, 9(3), 303– 318.

Ferreira, K. J., Lee, B. H. A., & Simchi-Levi, D. (2016). Analytics for an Online Retailer: Demand Forecasting and Price Optimization. Manufacturing & Service Operations Management, 18(1), 69–88. doi: 10.1287/msom.2015.0561

Fischer, T., & Krauss, C. (2018). Deep learning with long short-term memory networks for financial market predictions. European Journa Operational Research, 270(2), 654– 669. doi: 10.1016/j.ejor.2017.11.054

Gallego, G., & Moon, I. (1993). The distribution free newsboy problem: Review and extensions. Journal of the Operational Research Society, 44(8), 825–834. doi: 10.1057/jors.1993.141

Gaur, V., Giloni, A., & Seshadri, S. (2005). Information sharing in a supply chain under ARMA demand. Management Science, 51(6), 961–969.

Gilliland, M., & Sglavo, U. (2010). Worst practices in business forecasting. Analytics, 12–17.

Glorot, X., & Bengio, Y. (2010). Understanding the difficulty of training deep feedforward neural networks. Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics, 249–256.

Godfrey, G. A., & Powell, W. B. (2001). An adaptive, distribution-free algorithm for the newsvendor problem with censored demands, with applications to inventory and distribution. Management Science, 47(8), 1101–1112. doi: 10.1287/mnsc.47.8.1101.10231

Gross, C. W., & Sohl, J. E. (1990). Disaggregation methods to expedite product line forecasting. Journal of Forecasting, 9(3), 233–254. doi: 10.1002/for.3980090304

Huber, J., Müller, S., Fleischmann, M., & Stuckenschmidt, H. (2019). A data-driven newsvendor problem: From data to decision. European Journal of Operational Research, 278(3), 904–915. doi: 10.1016/j.ejor.2019.04.043

Hyndman, R. J., & Khandakar, Y. (2008). Automatic time series forecasting: The forecast package for R. Journal of Statistical Software, 27(3), 1–22. doi: 10.18637/jss.v027.i03

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. International Journal of Forecasting, 22(4), 679–688.

Koenker, R. (2005). Quantile regression. doi: 10.1017/CBO9780511754098

Levi, R., Perakis, G., & Uichanco, J. (2015). The data-driven newsvendor problem: New bounds and insights. Operations Research, 63(6), 1294–1306. doi: 10.1287/opre.2015.1422

Levi, R., Roundy, R. O., & Shmoys, D. B. (2007). Provably near-optimal sampling-based policies for stochastic inventory control models. Mathematics of Operations Research, 32(4), 821–839. doi: 10.1287/moor.1070.02 72

Loureiro, A. L. D., Miguéis, V. L., & da Silva, L. F. M. (2018). Exploring the use of deep neural networks for sales forecasting retail. Decision Support Systems, 114, 81–93. doi: 10.1016/j.dss.2018.08.010

Nahmias, S., & Schmidt, C. P. (1984). Efficient heuristic for the multi-item newsboy problem with a single constraint. Naval Research Logistics Quarterly, 31(3), 463–474. doi: 10.1002/nav.3800310311

Oroojlooy, A., Snyder, L., & Takáč, M. (2019). Applying Deep Learning to the Newsvendor Problem. IISE Transactions, (just-accepted), 1–39.

Punia, S., Nikolopoulos, K., Singh, S., Madaan, J., & Litsiou, K. (2020). Deep learning with long short-term memory networks and random forests for demand forecasting in multi-channel retail. International Journal of Production Research.

Punia, S., Singh, S., & Madaan, J. (2019). Deep Learning and Cross-Temporal Hierarchies Based Framework for Demand Forecasting. Proceedings of XXIII Annual International Conference of the SOM 2019, Kanpur, India, 62.

Qin, Y., Wang, R., Vakharia, A. J., Chen, Y., & Seref, M. M. (2011). The newsvendor problem: Review and directions for future research. European Journal of Operational Research, 213(2), 361–374.

Sbrana, G., & Silvestrini, A. (2013). Forecasting aggregate demand: Analytical comparison of top-down and bottom-up approaches in a multivariate exponential smoothing framework. International Journal of Production Economics, 146(1) , 185 198.

Scarf, H. (1958). A min-max solution of an inventory problem. Studies in the Mathematical Theory of Inventory and Production, 201–209.

Shankar, S., Ilavarasan, P. V., Punia, S., & Singh, S. P. (2019). Forecasting container throughput with long-short-term-memory networ 10.1108/IMDS-07-2019-0370

supply chains. CRC Press.

Vapnik, V. N. (1998). Statistical Learning Theory.

Villegas, M. A., & Pedregal, D. J. (2018). Supply chain decision support systems based on a novel hierarchical forecasting approach. Decision Support Systems, 114, 29–36. doi: 10.1016/j.dss.2018.08.003

Zhang, G. P. (2001). An investigation of neural networks for linear time-series forecasting. Computers & Operations Research, 28(12), 1183–1202.

## List of Tables

Table 1: Comparison of data-driven inventory optimization approaches

<table><tr><td>Paper</td><td>Data Used</td><td>Demand Forecasting Technique</td><td>Inventory Optimization</td><td>Additional Remarks</td></tr></table>

<table><tr><td></td><td></td><td>TS</td><td>ML</td><td>DL</td><td>Multi-item*</td><td>Constraints</td><td></td></tr><tr><td>1) Scarf (1958)</td><td>Mean and variance</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Proposed Min-max approach</td></tr><tr><td>2) Gallego &amp; Moon (1993)</td><td>Mean and variance</td><td>-</td><td>-</td><td>-</td><td>√</td><td>Capacity</td><td>Extended version of (1)</td></tr><tr><td>3) Bertsimas &amp; Thiele (2006)</td><td>Mean and variance</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Used heterogenous demand distributions over the time on echelons</td></tr><tr><td>4) Levi et al., (2007), (2015)</td><td>Demand data</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Used weighted mean spread and featureless data</td></tr><tr><td>5) Ban &amp; Rudin (2018)</td><td>Demand data</td><td>-</td><td>√</td><td>-</td><td>-</td><td>-</td><td>Used multi-feature data and quantile regression (linear) for optimization</td></tr><tr><td>6) Oroojlooy et al. (2019)</td><td>Demand data</td><td>-</td><td>-</td><td>√</td><td>-</td><td>-</td><td>Used revised loss function for optimization</td></tr><tr><td>7) Huber et al. (2019)</td><td>Demand data</td><td>√</td><td>√</td><td>-</td><td>-</td><td>-</td><td>Used multi-feature data and quantile regression (non-linear) for optimization</td></tr><tr><td>Proposed</td><td>Demand data</td><td>√</td><td>√</td><td>√</td><td>√</td><td>Capacity</td><td>Using multi-feature data, quantile regression(non-linear) optimization, deep learning, cross-sectional hierarchies, multi-product, capacity constraint, and a heuristic.</td></tr></table>

- TS – time-series; ML – Machine Learning; DL- Deep Learning, and \* - multi-item solutions shall valid only when some constraint is active on them.

Table 2: Summary statistics of variables

<table><tr><td colspan="4">Descriptive Statistics</td></tr><tr><td>Variable Name</td><td>Median</td><td>Mean (SD)</td><td>Remark</td></tr><tr><td>Sales</td><td>40</td><td>42.89 (14.61)</td><td>Product Sales</td></tr><tr><td>Price</td><td>2.89</td><td>3.20 (1.50)</td><td>Selling Price</td></tr><tr><td>% Discount</td><td>0.00</td><td>0.22 (0.416)</td><td>Promotional Discount</td></tr><tr><td>Visits</td><td>17</td><td>20.09 (12.64)</td><td>No. of customer visits</td></tr><tr><td>HHS</td><td>17</td><td>19.72 (12.33)</td><td>No. of households</td></tr><tr><td>TAVG</td><td>497</td><td>490.8 (89.39)</td><td>Average temperature</td></tr><tr><td>TMIN</td><td>429.5</td><td>424.9 (93.73)</td><td>Minimum temperature</td></tr><tr><td>TMAX</td><td>563</td><td>556.7 (87.30)</td><td>Maximum temperature</td></tr><tr><td>PRCP</td><td>0.1850</td><td>0.756 (1.33)</td><td>Precipitation</td></tr><tr><td>Eco_Index</td><td>3.41</td><td>1.183 (5.40)</td><td>Economic Index</td></tr><tr><td>Oil_Price</td><td>2.754</td><td>2.896 (0.53)</td><td>Oil Price</td></tr><tr><td colspan="3">% of cases</td><td>Remark</td></tr><tr><td>Feature</td><td colspan="2">95.35</td><td>In in-store circular</td></tr><tr><td>Display</td><td colspan="2">7.57</td><td>In-store Display</td></tr><tr><td>TPR</td><td colspan="2">9.81</td><td>Temporary Price Reduction</td></tr></table>

Table 3: Error metrics for demand estimation

<table><tr><td></td><td>ME</td><td>MAE</td><td>RMSE</td><td>MAPE</td><td>Rel-ME</td><td>Rel-MAE</td><td>Rel-RMSE</td></tr><tr><td>s-naive</td><td>-1.8854</td><td>7.4271</td><td>8.9059</td><td>50.5903</td><td>1.0000</td><td>1.0000</td><td>1.0000</td></tr><tr><td>ARIMA</td><td>-1.5737</td><td>5.5223</td><td>6.7977</td><td>42.6875</td><td>0.8347</td><td>0.7435</td><td>0.7633</td></tr><tr><td>ETS</td><td>-3.0334</td><td>6.6520</td><td>7.9669</td><td>51.3972</td><td>1.6089</td><td>0.8956</td><td>0.8946</td></tr><tr><td>FNN</td><td>-0.4626</td><td>5.4530</td><td>7.1420</td><td>44.1978</td><td>0.2454</td><td>0.7342</td><td>0.8019</td></tr><tr><td>RF</td><td>0.0281</td><td>1.4695</td><td>1.9264</td><td>8.7740</td><td>-0.0149</td><td>0.1979</td><td>0.2163</td></tr><tr><td>DNN</td><td>-0.0356</td><td>1.7121</td><td>2.2545</td><td>12.1680</td><td>0.0189</td><td>0.2305</td><td>0.2531</td></tr><tr><td>ARIMAx</td><td>0.3245</td><td>2.5112</td><td>3.3312</td><td>17.3360</td><td>-0.1721</td><td>0.3381</td><td>0.3740</td></tr></table>

Table 4: FVA Analysis

<table><tr><td></td><td>Forecast Accuracy (%)</td><td>Comparative Improvements in forecast accuracy (%)</td><td>Cumulative FVA over benchmark, s-naïve (%)</td></tr><tr><td>s-naive</td><td>49.40</td><td>-</td><td>-</td></tr><tr><td>FNN</td><td>55.80</td><td>6.40</td><td>6.40</td></tr><tr><td>ARIMA</td><td>57.31</td><td>1.51</td><td>7.91</td></tr><tr><td>ARIMAx</td><td>82.66</td><td>25.35</td><td>33.26</td></tr><tr><td>DNN</td><td>87.83</td><td>5.17</td><td>38.43</td></tr><tr><td>RF</td><td>91.22</td><td>3.52</td><td>41.82</td></tr></table>

Table 5: Average inventory costs relative to the best approach for each product groups

<table><tr><td rowspan="2">Demand Forecast Method</td><td></td><td>PG1</td><td>PG2</td><td>PG3</td><td>PG4</td></tr><tr><td></td><td>Cost</td><td>Cost</td><td>Cost</td><td>Cost</td></tr><tr><td rowspan="2">s-naive</td><td>MA</td><td>2.78</td><td>1.89</td><td>4.28</td><td>9.24</td></tr><tr><td>Norm</td><td>2.22</td><td>1.51</td><td>3.42</td><td>7.37</td></tr><tr><td rowspan="2">ARIMA</td><td>MA</td><td>3.45</td><td>1.44</td><td>5.68</td><td>2.07</td></tr><tr><td>Norm</td><td>2.75</td><td>1.34</td><td>4.53</td><td>2.01</td></tr><tr><td rowspan="2">ARIMAx</td><td>MA</td><td>1.63</td><td>1.25</td><td>5.84</td><td>2.58</td></tr><tr><td>Norm</td><td>1.30</td><td>1.00</td><td>4.66</td><td>2.06</td></tr><tr><td rowspan="2">ETS</td><td>MA</td><td>2.69</td><td>1.78</td><td>9.96</td><td>4.12</td></tr><tr><td>Norm</td><td>2.14</td><td>1.42</td><td>7.93</td><td>3.29</td></tr><tr><td rowspan="3">FNN</td><td>MA</td><td>2.78</td><td>1.89</td><td>6.46</td><td>6.74</td></tr><tr><td>Norm</td><td>2.22</td><td>1.51</td><td>4.28</td><td>5.38</td></tr><tr><td>QR</td><td>1.81</td><td>1.74</td><td>4.16</td><td>2.54</td></tr><tr><td rowspan="3">RF</td><td>MA</td><td>1.30</td><td>2.50</td><td>2.02</td><td>1.28</td></tr><tr><td>Norm</td><td>1.11</td><td>2.33</td><td>1.74</td><td>1.03</td></tr><tr><td>QR</td><td>1.00</td><td>2.32</td><td>1.00</td><td>1.00</td></tr><tr><td rowspan="3">DNN</td><td>MA</td><td>1.59</td><td>4.38</td><td>3.42</td><td>1.69</td></tr><tr><td>Norm</td><td>1.27</td><td>3.19</td><td>1.75</td><td>1.65</td></tr><tr><td>QR</td><td>1.46</td><td>3.77</td><td>1.39</td><td>1.54</td></tr></table>

Table 6: Optimal Order quantities

<table><tr><td>Product Group</td><td colspan="4">PG1</td><td colspan="4">PG2</td><td colspan="4">PG3</td><td colspan="4">PG4</td></tr><tr><td>Products</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Order Quantities</td><td>75</td><td>15</td><td>54</td><td>50</td><td>46</td><td>38</td><td>90</td><td>26</td><td>60</td><td>64</td><td>41</td><td>35</td><td>45</td><td>42</td><td>67</td><td>32</td></tr></table>

## List of Figures

(a)  
![](/api/attachments/EY398EEJ/fulltext/images/39f5ea656e0462812a6171e0f4e2bacf85451d436454f73132de9ce350867ea5.jpg)

![](/api/attachments/EY398EEJ/fulltext/images/cc66e70f6bbe5b43538af63b6c7b94f1dd04097ee6e7c560100f868d988f5a58.jpg)  
Figure 1: Schematic diagram for ${ \mathrm { \ s \ d e } } _ { \mathsf { c } _ { \mathsf { \tau } } } )$ neural network – (a) the mathematical functions, and (b) A deep neural network architecture

![](/api/attachments/EY398EEJ/fulltext/images/79a1d83c32dc7f3250de0f37708d932df4fec9f1a40d498291546348e5df8e6c.jpg)  
Figure 2: A Products' Hierarchy in retail store

![](/api/attachments/EY398EEJ/fulltext/images/f2f302ff29b597787378c05e53278d5f6df96f07b295f5b6f58590279976dfe9.jpg)

![](/api/attachments/EY398EEJ/fulltext/images/f8bd0fe6d729fe8a51d7694c2c6ec4fdcf22385fd7c18fe419c1cf73612a1b41.jpg)

![](/api/attachments/EY398EEJ/fulltext/images/661735b650b3af7ccc68aa5a4cf95778b5440bc777f03fcc4fe4021572eda98b.jpg)

![](/api/attachments/EY398EEJ/fulltext/images/4009fac56bc1c9a3ac239fcd4f5d33cd0f9d274ffbf26dadbce6b0a1e70f7493.jpg)

![](/api/attachments/EY398EEJ/fulltext/images/56634adfaaadd00e1c1acaf3195b2a36d317cf30933902ddaa6da36188aac943.jpg)  
Figure 3: Comparison of inventory cost from the inventory optimization techniques using different demand estimation techniques

![](/api/attachments/EY398EEJ/fulltext/images/1e829a0bfabb8d979a7ba0192756f75d3cfaea56a9335f779f57c708d8ee99f8.jpg)  
Figure 4: Products hierarchies and their historical demand proportions

![](/api/attachments/EY398EEJ/fulltext/images/fce14a347cdcce9d187ae139c8d7aa5e67bc2b8cdfbb44a16188a7b9f1aba20f.jpg)  
Figure 5: Comparison of total inventory cost from the inventory optimization techniques and demand estimation techniques

## Sushil Punia

Sushil Punia (M.Tech (IIT Kanpur), B.Tech (NIT KKR)) is a Ph.D. candidate at the Indian Institute of Technology Delhi, India. His area of research in Ph.D. is the operations and supply chain management and he is working on machine learning and deep learning-based data-driven decision models for supply chains. His research has appeared in International Journal of Production Research (IJPR), Industrial Management and Data Systems (IMDS), etc. and presented at international conferences like INFORMS 2017, and SOM 2019. He has been awarded one of the Springer Nature’s Best Paper Award at SOM 2019. He also awarded Emerald Outstanding Reviewer Award 2018. His research interests are application of AI in Healthcare, and Industry 4.0.

## Surya Prakash Singh

Surya Prakash Singh is Professor in the Department of Management Studies, IIT Delhi, India. He holds a PhD Degree from IIT Kanpur. He is also Post-Doctoral Fellow from NUS Singapore-MIT USA Alliance. His research interest lies in facility layout problems, heuristics and meta-heuristics. His work has been published in leading international journals such as IJPR, LNCS, IJAMT, EJM, RBR, IJRTE and APMR. He regularly reviews articles for many leading journals. His biography appeared in Marquis, USA Who’s Who in Science and Engineering, December 2007, and Who’s Who in the World, November 2010. Recently, he has been awarded Young Outstanding Faculty Fellowship from IIT Delhi.

## Jitendra K. Madaan

Dr. Jitendra Madaan received his B.Tech Degree in Production and Industrial Engineering from M.B.M Govt. Engg College, Jodhpur (JNV University), India, and obtained his M. Tech in Manufacturing System Engg. from Department of Mechanical Engg. MREC (Now MNIT), Jaipur and PhD in Mechanical Engineering from the Indian Institute of Technology (IIT) Delhi, India. His current research interests are Reverse Logistics and Supply Chain Management, Sustainable Operations Management, Production Management, information and governance effectiveness, Systems Modelling and Simulation, etc. To date, Dr. Madaan has published over 4 book chapters, over 25 refereed international journal papers and 48 peer reviewed international conference papers. He is a reviewer of several international journal of repute.

Sushil Punia: Conceptualization, Methodology, Data curation, Analysis, Writing- Original draft preparation, Writing- Reviewing and Editing, Surya Singh: Supervision, and Review. Jitendra Madaan: Supervision.

## Highlights

 Address multi-item inventory optimization problem with a capacity constraint

 Developed data-driven (distribution free) solution for the newsvendor problem

 Used deep learning, random forest and time-series methods for demand estimation

 Used hierarchical information to design a heuristic for inventory optimization
