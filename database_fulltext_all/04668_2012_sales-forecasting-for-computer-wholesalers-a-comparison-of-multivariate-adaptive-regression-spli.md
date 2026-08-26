---
otero_id: 4668
otero_key: "D88GM5V7"
title: "Sales forecasting for computer wholesalers: A comparison of multivariate adaptive regression splines and artificial neural networks"
authors: "Chi-Jie Lu; Tian-Shyug Lee; Chia-Mei Lian"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sales forecasting for computer wholesalers: A comparison of multivariate adaptive regression splines and arti<sup>fi</sup>cial neural networks

Chi-Jie Lu <sup>a</sup>, Tian-Shyug Lee <sup>b,</sup>⁎, Chia-Mei Lian <sup>c</sup>

<sup>a</sup> Department of Industrial Management, Chien Hsin University of Science and Technology, Taiwan

<sup>b</sup> Department of Business and Administration, Fu Jen Catholic University, Taiwan

<sup>c</sup> Graduate School of Business Administration, Fu Jen Catholic University, Taiwan

## a r t i c l e i n f o

Article history: Received 27 October 2010 Received in revised form 27 May 2012 Accepted 11 August 2012 Available online 21 August 2012

Keywords: Sales forecasting Computer wholesaler Multivariate adaptive regression splines Arti<sup>fi</sup>cial neural networks IT industry

## a b s t r a c t

Arti<sup>fi</sup>cial neural networks (ANNs) have been found to be useful for sales/demand forecasting. However, one of the main shortcomings of ANNs is their inability to identify important forecasting variables. This study uses multivariate adaptive regression splines (MARS), a nonlinear and non-parametric regression methodology, to construct sales forecasting models for computer wholesalers. Through the outstanding variable screening ability of MARS, important sales forecasting variables for computer wholesalers can be obtained to enable them to make better sales management decisions Two sets of real sales data collected from Taiwanese com: puter wholesalers are used to evaluate the performance of MARS. The experimental results show that the MARS model outperforms backpropagation neural networks, a support vector machine, a cerebellar model articulation controller neural network, an extreme learning machine, an ARIMA model, a multivariate linear regression model, and four two-stage forecasting schemes across various performance criteria. Moreover, the MARS forecasting results provide useful information about the relationships between the forecasting variables selected and sales amounts through the basis functions, important predictor variables, and the MARS prediction function obtained, and hence they have important implications for the implementation of appropriate sales decisions or strategies.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the consumer-centric environment of today's business world, enterprises seeking good sales performance often need to maintain a balance between meeting customer demand and controlling inventory costs. Carrying a larger inventory allows customer demand to be satis<sup>fi</sup>ed at all times, but can result in over-stocking, leading to problems such as tied up capital, inventory writedowns, and reduced profit margins. Lower inventory levels, in contrast, may reduce inventory costs, but can result in opportunity costs arising from missed sale op portunities, reduced customer satisfaction, and other problems. Sales forecasting can be used to determine the required inventory level and avoid the problem of under/over-stocking. In addition, sales forecasting can have implications for corporate <sup>fi</sup>nancial planning, marketing, client management, and other areas of business. Improving the accuracy of sales forecasts has therefore become an important aspect of operating a business.

There is an extensive body of literature on sales forecasting in such industries as textiles and clothing [52–54], fashion [41,47,58], books [7,10,48], and electronics [9,11–13]. However, very few studies center on sales forecasting in the information technology (IT) industry, especially for computer wholesalers. Lu and Wang [34] employed a combination of independent component analysis, growing hierarchical self-organizing maps, and support vector regression analysis to develop a hybrid sales forecasting model for a computer dealer. In the wake of technological advances and rapid changes in consumer demand, IT products have come to be characterized by their variety, constant changes in speci<sup>fi</sup>cations, and rapid price declines. These factors have made sales forecasting in the IT industry an important but dif<sup>fi</sup>- cult task. This paper focuses on sales forecasting for computer wholesalers in light of the important role they play in the IT industry by distributing IT products to retailers and customers.

Arti<sup>fi</sup>cial neural network (ANN) algorithms such as backpropagation neural networks (BPN) and support vector regression (SVR) have been found to be useful techniques for sales/demand forecasting due to their ability to capture subtle functional relationships among empirical data, even where the underlying relationships are unknown or hard to describe [9,22,34,63]. Unlike traditional time series forecasting models such as the Box–Jenkins ARIMA model and multivariate regression analysis, ANNs are data-driven and non-parametric. They require no strong model assumptions, and can map any nonlinear function without a priori assumptions about the properties of the data [24,56,65]. Coupled with their superior performance in constructing non-linear models,

ANNs have been successfully applied in sales/demand forecasting [9,22,53].

Kuo and Xue [28] used ANNs to forecast sales for a beverage company. Their results showed that the forecasting ability of ANNs is indeed better than that of ARIMA speci<sup>fi</sup>cations. Chang and Wang [9] applied a fuzzy BPN to forecast sales for the Taiwanese printed circuit board industry. Hyunchul et al. [27] <sup>fi</sup>rst used independent component analysis to screen variables before employing an ANN algorithm to predict sales for a Korean shopping mall. They also showed that the proposed forecasting scheme is superior to a forecasting method in which principal component analysis is <sup>fi</sup>rst used to screen variables before an ANN algorithm is applied. Yang et al. [63] reported that SVR is a promising method for predicting Chinese tobacco sales. Luis and Richard [37] combined ARIMA and ANN models to forecast sales for a Chilean supermarket. Their results showed that this combined forecasting technique can help <sup>fi</sup>rms make correct decisions. Sun et al. [47] successfully used an extreme learning machine (ELM) to forecast sales for a fashion retailer. Wu [61] utilized the combination of a wavelet support vector machine and particle swarm optimization to develop a hybrid model for auto sales forecasting. The results indicated that the forecasting ability of the hybrid model is indeed better than that of ARIMA models. Wong and Guo [58] integrated an extreme learning machine with a harmony search algorithm to develop a hybrid sales forecasting model for fashion retail supply chains.

Despite the existence of a signi<sup>fi</sup>cant body of literature on sales forecasting using ANNs, the dif<sup>fi</sup>culty of identifying important forecasting variables makes ANNs less attractive for sales predictions, as the selection of important forecasting variables is crucial to the construction of sales forecasting models, given that the variables selected will usually affect the accuracy of the model. Having too many forecasting variables will add complexity to the forecasting model, while having too few may result in an ineffective model. Important forecasting variables that have an impact on sales forecasting results are often the key focus areas or indicators requiring managerial attention. Discussing and understanding these important forecasting variables will lead to improved management and sales ef<sup>fi</sup>ciency. This study therefore utilizes a methodology that enables both faster processing and the selection of variables – multivariate adaptive regression splines (MARS) – to construct sales forecasting models for computer wholesalers. Through the outstanding variable screening ability of MARS, variables important to sales forecasting for these wholesalers can be obtained to make better sales management decisions.

MARS is a nonlinear and non-parametric regression methodology [23]. It is a <sup>fl</sup>exible procedure that requires no advance speci<sup>fi</sup>cation of a functional form. Rather, it attempts to adapt to the unknown functional form using a series of piecewise regression splines. This makes it very suitable for modeling complex non-linear relationships among variables. Moreover, unlike ANNs, MARS can identify ‘important’ independent (forecasting) variables and investigate the relationship between the selected independent and dependent (target) variables through the built basis functions when many potential forecasting variables are considered. Finally, MARS does not require a long training process and hence can save lots of time in the model building process. The power of MARS in building prediction models has been demonstrated in many applications such as network intrusion detection [40], electricity price forecasting [2], cancer diagnosis [18,33], software engineering [5,45,66], and credit scoring [16,31]. However, to the best of the authors' knowledge, in no reported study has MARS been used to forecast sales.

This study applies <sup>fi</sup>ve different methodologies – MARS, BPN, SVR, ELM, and a cerebellar model articulation controller neural network (CMACNN), the latter being an effective neural network model [59] – in sales forecasting for computer wholesalers, and compares the merits of MARS against those of the three other ANN algorithms. To achieve this objective, forecasting models are developed using backpropagation neural networks, a support vector machine, an extreme learning machine, a CMACNN, and four two-stage forecasting schemes. First, MARS, BPN,

SVR, and CMACNN are applied to construct sales forecasting models using all forecasting variables. In the case of the two-stage forecasting schemes, MARS is <sup>fi</sup>rst used as a screening tool for the forecasting variables, after which the important forecasting variables obtained are used as input variables for forecasting models developed using BPN, SVR, ELM, and CMACNN. This results in four two-stage forecasting models respectively called the MARS–BPN, MARS–SVR, MARS–ELM, and MARS– CMACNN models. Finally, to compare the results of the sales forecasting models proposed in this study, experiments are carried out using monthly sales data from two Taiwanese computer wholesalers.

The rest of this paper is organized as follows. Section 2 gives a brief introduction to the MARS, SVR, BPN, and CMACNN methodologies. The experimental results and related discussions are presented in Section 3. Section 4 concludes the paper.

## 2. Methodology

## 2.1. Multivariate adaptive regression splines

MARS is a nonlinear and non-parametric regression methodology <sup>fi</sup>rst proposed by Friedman [23] as a <sup>fl</sup>exible procedure in which model relationships are nearly additive or involve interactions with fewer variables. The MARS modeling procedure is based on a divideand-conquer strategy in which training data sets are partitioned into separate regions, each of which is assigned its own regression equation. MARS excels at <sup>fi</sup>nding not only optimal variable transformations and interactions, but also in identifying the complex data structures often concealed in high-dimensional data. This makes MARS particularly suitable for problems with high input dimensions.

MARS essentially builds <sup>fl</sup>exible models by <sup>fi</sup>tting piecewise linear regressions; that is, the non-linearity of a model is approximated through the use of separate linear regression slopes in distinct intervals of the independent variable space. Therefore, the slope of the regression line is allowed to change from one interval to the other as the two ‘knot’ points are crossed. The variables to be used and the end points of the intervals for each variable are found through a fast but intensive search procedure. In addition to searching for variables one by one, MARS also searches for interactions between variables, allowing any degree of interaction to be considered as long as the built model provides a better <sup>fi</sup>t with the data.

Fig. 1 depicts a simple example of how MARS would attempt to <sup>fi</sup>t data in a two-dimensional space with piecewise linear regression. Note that y and x in Fig. 1 are the dependent and independent variables, respectively. It can be observed that $\mathbf { k } _ { 1 }$ and k in Fig. 1 are two knot points delimiting three intervals where different linear relationships are identi<sup>fi</sup>ed.

![](/api/attachments/D88GM5V7/fulltext/images/cca4d88fba8de138535990eaefde6dd76016657172b40bd619cd0871704f327b.jpg)  
Fig. 1. A simple example of MARS.

The general MARS function can be represented using the following equation [23].

$$
f (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \prod_ {k = 1} ^ {K} \left[ s _ {k, m} \Bigl (x (k, m) - t _ {k, m} \Bigr) \right],\tag{1}
$$

where $a _ { 0 }$ is a constant; $a _ { m }$ are the coef<sup>fi</sup>cients of the model, which are estimated to yield the best <sup>fi</sup>t to the data; M is the number of basis functions; K is the number of “splits” that generate the m-th basis function; $s _ { k , m }$ takes values of either 1 or -1 and indicates the (right/ left) sense of the associated step function; The x(k,m) is the label of the independent variable; and $t _ { k , m }$ indicates the knot locations.

The optimal MARS model is selected in a two-stage process. First, MARS initially constructs a very large number of basis functions to over<sup>fi</sup>t the data, where variables are allowed to enter as continuous, categorical, or ordinal (the formal mechanism by which variable intervals are de<sup>fi</sup>ned) and they can interact with one another or be restricted to entry as additive components only. In this stage, MARS <sup>fi</sup>nds the pair of basis functions that gives the maximum reduction in sum-of-squares residual error. The two basis functions in the pair are the same except that a different side of a mirrored hinge function is used for each function. A hinge function is de<sup>fi</sup>ned by a variable and a knot, i.e. max(0, x — const) or max(0, const — x) where const is the knot. MARS uses a greedy algorithm to consider whether to add a basis function to the MARS model by searching all combinations of all values of all variables. The basis functions are selected initially based on the mean of the values of the independent variables. This process of adding basis functions continues until the change in residual error is too small to continue or until the maximum number of basis function is reached [23].

In the second stage, basis functions are deleted in the order of least contributions using the generalized cross-validation (GCV) criterion. A measure of variable importance can then be assessed by observing the decrease in the calculated GCV when a variable is removed from the model. This process continues until the remaining basis functions all satisfy the pre-determined requirements. The GCV can be expressed as follows [23].

$$
\operatorname{GCV} (M) = \frac {1}{N} \sum_ {i = 1} ^ {N} \frac {\left[ y _ {i} - f _ {M} \left(x _ {i}\right) \right] ^ {2}}{\left[ 1 - \frac {C (M)}{N} \right] ^ {2}},\tag{2}
$$

where there are N observations and C(M) is the cost-penalty measures of a model containing M basis functions (therefore, the numerator measures the lack of <sup>fi</sup>t on the M basis function model $f _ { M } ( x _ { i } )$ and the denominator denotes the penalty for model complexity C(M)). In other words, the purpose of C(M) is to penalize model complexity, to avoid over<sup>fi</sup>tting, and to promote model parsimony. To do so, C(M) introduces a cost incurred per basis function to the model that is similar to the adjusted $\mathsf { R } ^ { 2 }$ in least-squares regression. It is usually de<sup>fi</sup>ned as C(M)=M in linear least-squares regression; this formulation is also used in this paper.

After creating a MARS model, one can estimate the relative importance of a variable based on its contribution to the <sup>fi</sup>t of the model on a scale of 0 to 100. To do this, MARS deletes all terms containing the selected variable, re<sup>fi</sup>ts the model and then calculates the <sup>fi</sup>t's reduction. The highest scoring and most important variable is the one that most reduces the <sup>fi</sup>t of the model after being deleted. Less important variables receive lower scores, which correspond to the ratio of the reduction in <sup>fi</sup>t produced by these variables to that of the most important variable.

MARS is capable of tracking very complex data structures often concealed in high-dimensional data. Please refer to Friedman [23] for more details regarding the model building process.

## 2.2. Support vector regression

SVR is a novel neural network algorithm technique based on statistical learning theory that has received increasing attention as a method for solving nonlinear regression estimation problems. SVR is derived from the structural risk minimization principle to estimate a function by minimizing an upper bound of the generalization error [55]. It has been successfully applied in different time series prediction problems such as production value forecasting, traf<sup>fi</sup>c <sup>fl</sup>ow prediction, and <sup>fi</sup>nancial time series forecasting [6,36,42,50,51].

The SVR model can be expressed as the following equation [55].

$$
f (x) = (\mathbf {z} \cdot \phi (x)) + b,\tag{3}
$$

where z is a weight vector, b is bias, and $\phi ( x )$ is a kernel function in which a non-linear function is used to transform the non-linear input into a linear mode in a high-dimension feature space.

Under traditional regression analysis, coef<sup>fi</sup>cients are found by minimizing the square error, which can be considered empirical risk based on a loss function. Vapnik [55] introduced the so-called ε-insensitivity loss function to SVR. It can be expressed as

$$
L _ {\varepsilon} (f (x) - y) = \left\{ \begin{array}{c c} | f (x) - y | - \varepsilon & i f | f (x) - y | \geq \varepsilon \\ 0 & \text { otherwise } \end{array} \right.,\tag{4}
$$

where ε is de<sup>fi</sup>ned as the region of ε-insensitivity; when the predicted value falls into the band area, the loss is zero. In contrast, if the predicted value falls outside the band area, then the loss is equal to the difference between the predicted value and the margin.

When empirical risk and structure risk are considered together, the SVR model can be constructed to minimize the following quadratic programming problem.

$$
\begin{array}{c} \text {Min}: \frac {1}{2} \mathbf {z} ^ {T} \mathbf {z} + C \sum_ {i} \left(\xi_ {i} + \xi_ {i} ^ {*}\right) \\ \text {Subject to} \left\{ \begin{array}{c} y _ {i} - \mathbf {z} ^ {T} x _ {i} - b \leq \varepsilon + \xi_ {i} \\ \mathbf {z} ^ {T} x _ {i} + b - y _ {i} \leq \varepsilon + \xi_ {i} ^ {*}, \\ \xi_ {i}, \xi_ {i} ^ {*} \geq 0 \end{array} \right. \end{array}\tag{5}
$$

where $i { = } 1 , { \ldots } , \Pi$ is the number of training data; $( \xi _ { i } + \xi _ { i } ^ { * } )$ is the empirical risk; $\scriptstyle { \frac { 1 } { 2 } } \mathbf { z } ^ { T } \mathbf { z }$ z is the structure risk preventing over-learning and lack of applied universality; and C is a modifying coef<sup>fi</sup>cient representing the trade-off between empirical risk and structure risk.

Eq. (5) is a standard quadratic programming problem. After selecting an appropriate modifying coef<sup>fi</sup>cient (C), band area width (ε), and kernel function (φ), the optimum value of each parameter can be resolved though Lagrange functions. The general form of the SVR-based regression function can be written as [55]

$$
f (x, \mathbf {z}) = f (x, \alpha , \alpha^ {*}) = \sum_ {i = 1} ^ {n} (\alpha_ {i} - \alpha_ {i} ^ {*}) \varphi (x _ {i}, x _ {j}) + b,\tag{6}
$$

where $\alpha _ { i }$ and $\alpha _ { i } ^ { * }$ are Lagrangian multipliers and satisfy the equality $\alpha _ { i } { \alpha _ { i } } ^ { * } { = } 0 ; \varphi ( x _ { i } , x _ { j } )$ is the kernel function. Any function that meets Mercer's condition can be used as the kernel function.

Following Cherkassky and Ma's [17] proposal that a radial basis function (RBF) is suitable for solving most forecasting problems, this paper uses an RBF with parameter $\sigma { = } 0 . 2$ as the kernel function in the SVR modeling process. SVR performance is mainly affected by the setting of parameters C and ε [17]. There are no general rules governing the choice of C and ε. Lu et al. [36] proposed an analytic parameter selection method for SVR modeling that is based on sketching the structure of training data and using a trial-and-error approach to determine the best parameter values. This study employs this analytic method to determine the best set of C and ε parameter values.

## 2.3. Backpropagation neural network

The most popular neural network training algorithm is the BPN, which has a simple architecture but powerful problem-solving ability [3,65]. The network architecture is organized into nodes and the types of connections permitted. Fig. 2 displays a simple BPN topology that consists of a number of nodes (neurons) connected by links and comprises three (or more) layers: the input layer, the hidden layer(s), and the output layer. The nodes in the input layer receive input signals from an external source, while the nodes in the output layer provide the target output signals. Any layers between the input and output layers are called hidden layers. Because a one hidden layer network is suf<sup>fi</sup>cient to model any complex system with the desired degree of accuracy [14], the BPN model designed in this study will have only one hidden layer (as seen in Fig. 2).

From Fig. 2, it can be seen that each layer comprises several neurons interconnected by sets of weights. The neurons obtain inputs from initial inputs or interconnections and generate outputs using a nonlinear transfer function. A BPN uses a gradient descent training algorithm to minimize error (the difference between the desired output and the network output) and adjusts interconnection weights during the training process. For the gradient descent algorithm, the step size (otherwise known as the learning rate) must be speci<sup>fi</sup>ed <sup>fi</sup>rst. The learning rate is a crucial aspect of a BPN model because lower learning rates tend to slow down the learning process before convergence, while higher learning rates may cause network oscillation and an inability to converge.

BPN performance is mainly affected by the setting of the network topology, i.e., the number of nodes in each layer and the learning rates. There are no general rules governing the choice of network topology. Its selection is usually based on the trial-and-error (or cross-validation) method. In this study, the optimal network topology of the BPN model is determined using the trial-and-error method. See Chauvin and Rumelhart [14] and Haykin [24] for more details on how to determine the appropriate network topology (the number of layers, the number of nodes in each layer, and the appropriate learning rates).

## 2.4. Cerebellar model articulation controller neural network

A CMACNN is a supervised neural network based on the functions of the human cerebellum, which is responsible for muscle control and motor coordination [1,59]. A cerebellum works as follows. An input signal to the cerebellum activates many mossy <sup>fi</sup>bers, each of which touches a granule cell. The output of the cerebellum is the sum of the activated granule cells. A CMACNN performs cerebellum functions through a series of mappings and acts as a clever look-up table. Its advantages include very fast learning, reasonable generalization ability, and robust noise resistance [59]. Furthermore, Miller et al. [39] found that a CMACNN had a higher convergence speed than a standard BPN. CMACNNs have been successfully used for many purposes such as control, diagnosis, classi<sup>fi</sup>cation, and prediction [32,35,44,46,57,62,67].

![](/api/attachments/D88GM5V7/fulltext/images/980bbbd3b0acdfccb83aa2b77ec561c237fad62b355910c588517aff072e4954.jpg)  
Fig. 2. A three-layer BPN topology.

A CMACNN comprises <sup>fi</sup>ve cells – an input space (X), a sensory cell (S), an association cell (A), a physical memory cell (P), and an output cell (Y) – and transforms input values into output values using a series of mappings [59]. First, the data in the input space (X) are transformed into a sensory cell (S). A quantization operator is used to transform components of input vectors into discrete quantization indices. A sensory cell comprises random tables [59]. The size of each random table is calculated by

$$
R _ {i} = E _ {i} + g - 1, i = 1, 2,.., N,\tag{7}
$$

where $R _ { i }$ is the size of the random table of input vector x ; E is the quantization resolution of input vector x ; and g is generalization size. Second, the data in the sensory cell (S) are mapped to random table i, the association cell (A). The segment mappings are created based on parameter g. The quantization and segment mappings generate natural interpolation and give the CMACNN the ability to generalize [59]. A large g value enhances the ability to generalize, but reduces approximation accuracy. Finally, vector a in the association cell corresponds to table w in the physical memory cell (P). Table w stores many weights. An actual output value in output cell (Y) can be computed by the following matrix operation.

$$
\mathbf {y} = \mathbf {a} ^ {T} \mathbf {w},\tag{8}
$$

where $\mathbf { a } = ( a _ { 1 } , a _ { 2 } , . . . , a _ { h } ) ^ { T } ; \mathbf { w } = ( w _ { 1 } , w _ { 2 } , . . . , w _ { h } ) ^ { T } ;$ h is the size of vectors a and w; and y is the actual output. The CMACNN uses the least mean squares (LMS) rule to adjust the weights. Only activated weights need to be modi<sup>fi</sup>ed in the CMACNN algorithm.

## 3. Experimental results

## 3.1. Dataset and forecasting variables

This study used monthly sales datasets from a computer wholesaler in Taiwan (called Company A) to evaluate the performance of the MARS, SVR, BPN, and CMACNN forecasting models. The Company A is one of the top three IT product wholesalers in Taiwan, representing over 270 global leading IT brands (such as Intel, Microsoft and HP) and selling up to 6000 products. The company's main suppliers are large-scale and well-known manufacturers of computer gadgets and components, such as Intel, HP, Microsoft, ASUS and ACER. Its target customers include government agencies, large and medium-sized enterprises and small wholesalers.

The data collection period for sales amounts is from January 1996 to February 2009, giving a total of 158 monthly sales amounts. The sales trend is shown in Fig. 3. As shown in Fig. 3, the following are the major events during that period. These events had signi<sup>fi</sup>cant impacts on the sales of Company A.

➣ 1997: When the Internet and e-commerce business boomed, sales increased drastically.

➣ 2000: Y2K concerns prompted many government agencies and large enterprises to replace their computers.

➣ 2002: The stock market plummeted due to political factors and the poor economic situation, which reduced the willingness of enterprises to purchase new equipment.

➣ 2003: The economy was hit hard by the SARS outbreak and corporations were less willing to spend.

➣ 2006: Equipment purchased in 2000 had become obsolete and needed to be replaced by new models.

Table 1  
![](/api/attachments/D88GM5V7/fulltext/images/c4a9c0eb70c687f0618baa5f12ca347c37f44377c60dcc93bfb210e839e322d1.jpg)  
Fig. 3. The monthly sales amount of a Taiwan computer wholesaler.

➣ 2008: The subprime mortgage crisis led to signi<sup>fi</sup>cant layoffs. The unemployment rate rose and business computer sales were adversely affected.

The <sup>fi</sup>rst 126 data points (about 80% of the total number of sample points) are used as the training sample, while the remaining 32 data points (about 20% of the total number of sample points) are employed as the holdout and used as the testing sample for measuring out-ofsample forecasting ability.

To build the forecasting models, the 11 indicators depicted in Table 1, which were chosen on the basis of subjective judgment, expert opinion, and by reference to the more commonly used <sup>fi</sup>nancial market variables, are employed as forecasting variables. Note that relative strength (RSI) and BIAS indicators are also adopted in this study due to their status as the most widely used measures in stock price prediction [60]. Please refer to Wood [60] for details concerning technical indicators.

This study utilizes four commonly used performance criteria to evaluate the accuracy of the four forecasting models: root mean squared error (RMSE), mean absolute percentage error (MAPE), mean absolute deviation (MAD), and root mean squared percentage error (RMSPE). The de<sup>fi</sup>nitions of these criteria can be found in Table 2. RMSE, MAD, RMSPE, and MAPE measure the deviation of the forecast value from the actual value. Hence, the smaller the indicator value, the greater the accuracy.

Because the input variable data employed in this study include a variety of measurements re<sup>fl</sup>ecting a range of units, the magnitude of the absolute value can vary signi<sup>fi</sup>cantly for different variables. If the original values of input variables are applied directly in modeling neural network models, including BPN, SVR, and CAMCNN speci<sup>fi</sup>cations, the large value input variables may overwhelm smaller value inputs in the neural network learning process, leading to the neural network learning saturation problem. Saturation means that continued learning does not lead to improved network performance, and is often indicative of over<sup>fi</sup>tting and detrimental to generalization [4,30]. Moreover, many studies have reported that linear scaling can improve the performance of neural networks [19,20,49,65]. Therefore, to avoid the saturation problem and produce accurate forecasts, the raw input variable data employed in this study are linear-scaled into the range of [−1.0, 1.0] before the neural network models are constructed.

List of forecasting variables in building forecasting models.

<table><tr><td>Variables</td><td>Description</td></tr><tr><td>X1</td><td>3-month moving average (MA3)</td></tr><tr><td>X2</td><td>6-month moving average(MA6)</td></tr><tr><td>X3</td><td>Previous month&#x27;s sales amount (T-1)</td></tr><tr><td>X4</td><td>Previous two months&#x27; sales amount (T-2)</td></tr><tr><td>X5</td><td>Previous three months&#x27; sales amount (T-3)</td></tr><tr><td>X6</td><td>3-month relative strength indicator (RSI3)</td></tr><tr><td>X7</td><td>6-month relative strength indicator (RSI6)</td></tr><tr><td>X8</td><td>12-month relative strength indicator (RSI12)</td></tr><tr><td>X9</td><td>3-month BIAS (BIAS3)</td></tr><tr><td>X10</td><td>6-month BIAS (BIAS6)</td></tr><tr><td>X11</td><td>12-month BIAS (BIAS12)</td></tr></table>

To build the SVR, CMACNN, BPN, and MARS forecasting models, this study adopts the LIBSVM package proposed by Chang and Lin [8], a self-developed code using MATLAB, the neural network toolbox of MATLAB, and MARS 2.0 [38] generated by Salford Systems, respectively. Note that the default settings of LIBSVM package, neural network toolbox and MARS 2.0 software are used.

## 3.2. Forecasting results

To compare the results derived from a total of seven forecasting models under the two frameworks, this section <sup>fi</sup>rst discusses the forecasting models constructed using the MARS, BPN, SVR, and CMACNN methodologies to predict total sales amounts.

To develop the MARS forecasting model, the forecasting variables and basis functions should <sup>fi</sup>rst be selected. The variable selection results and the basis functions obtained are summarized in Table 3. It can be observed that three variables – X1 (MA3), X4 (T-2: sales amount in the T-2 period), and X3 (T-1: previous month's sales amount) – are identi<sup>fi</sup>ed from the initial 11 variables and play crucial roles in building the MARS sales forecasting model. Table 3 also shows that the basis functions, the important predictor variables, and the MARS prediction function obtained provide important implications for sales management and will help managers make or adopt appropriate sales decisions or strategies. The detailed discussion is presented in Section 3.4.

Performance measures and their de<sup>fi</sup>nitions.

<table><tr><td>Metrics</td><td> $Calculation^a$ </td></tr><tr><td>RMSE</td><td> $RMSE = \sqrt{\frac{\sum_{i=1}^{N} (f_i - y_i)^2}{N}}$ </td></tr><tr><td>MAD</td><td> $MAD = \frac{\sum_{i=1}^{N} |f_i - y_i|}{N}$ </td></tr><tr><td>MAPE</td><td> $MAPE = \frac{\sum_{i=1}^{N} \left| \frac{f_i - y_i}{y_i} \right|}{N} \times 100\%$ </td></tr><tr><td>RMSPE</td><td> $RMSPE = \sqrt{\frac{\sum_{i=1}^{N} \left( \frac{f_i - y_i}{y_i} \right)^2}{N}} \times 100\%$ </td></tr></table>

<sup>a</sup> Note that y and f represent the actual and predicted value, respectively; N is total number of data points.

Table 3  
Basis functions and important forecasting variables using MARS.

<table><tr><td colspan="2">Variable selection results</td><td>Basis function</td></tr><tr><td>Variable name</td><td>Relative importance (%)</td><td>Equation name</td></tr><tr><td>X1(MA3)</td><td>100.00</td><td>BF2 = max(0, X1(MA3) - 381);</td></tr><tr><td>X4(T-2)</td><td>78.94</td><td>BF4 = max(0, X4(T-2) - 1226);</td></tr><tr><td>X3(T-1)</td><td>46.69</td><td>BF5 = max(0, 1226 - X4(T-2));</td></tr><tr><td></td><td></td><td>BF6 = max(0, X3(T-1) - 282);</td></tr><tr><td colspan="3">MARS prediction function: f(x) = -365.25 + 3.00*BF2 - 1.00*BF4 + 1.00*BF5 - 1.00*BF6;</td></tr></table>

In constructing the SVR model, all 11 predictor variables are used as the input variables. In selecting parameters for the SVR model, $\varepsilon =$ 0.0103 and C=1.3 can be obtained by adopting the analytic approach described in Section 2.3. Because $\varepsilon { = } 0 . 0 1 0 3$ is close to $\varepsilon { = } \bar { 2 } ^ { \stackrel { - } { - } 3 }$ and C=1.3 is near C=2<sup>1</sup>, the parameter set $( \varepsilon = 2 ^ { - 3 } , \mathsf C = 2 ^ { 1 } )$ is used as the starting point of the grid search to <sup>fi</sup>nd the best parameters. Table 4 summarizes the results of testing the SVR model with different combinations of parameter sets. It can be seen that the parameter set $( \varepsilon = 2 ^ { - 3 } , \mathsf C = 2 ^ { \bar { 1 } } )$ gives the best test result (minimum testing MSE) and is the best parameter set for the SVR sales forecasting model.

In the BPN model, the input layer has 11 nodes as the 11 forecasting variables are all adopted. As there are no general rules for determining the appropriate number of nodes in the hidden layer, the number of hidden nodes to be tested is set at 22, 23, 24, 25, and 26. The network has only one output node: the forecast sales amount. As lower learning rates tend to give the best network results [14], learning rates of 0.001, 0.01, 0.03, 0.05, and 0.1 are tested during the training process. The network topology with the minimum testing MSE is considered the optimal network. Table 5 reports the results of testing the BPN model with different combinations of hidden nodes and learning rates. From Table 5, it can be observed that the {11-24-1} topology ({11-24-1} indicates there are 11 nodes in the input layer, 24 nodes in the hidden layer, and one node in the output layer) with a learning rate of 0.05 gives the minimum testing MSE and hence is the best topology setup for the BPN sales forecasting model.

Table 4  
The model selection results of the SVR model

<table><tr><td> $\varepsilon$ </td><td>C</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5"> $2^{-7}$ </td><td> $2^{-3}$ </td><td>0.0123</td><td>0.2549</td></tr><tr><td> $2^{-1}$ </td><td>0.0126</td><td>0.3072</td></tr><tr><td> $2^{1}$ </td><td>0.0139</td><td>0.5048</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td rowspan="5"> $2^{-5}$ </td><td> $2^{-3}$ </td><td>0.0116</td><td>0.2177</td></tr><tr><td> $2^{-1}$ </td><td>0.0119</td><td>0.2409</td></tr><tr><td> $2^{1}$ </td><td>0.0108</td><td>0.4253</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td rowspan="5"> $2^{-3}$ </td><td> $2^{-3}$ </td><td>0.0118</td><td>0.2480</td></tr><tr><td> $2^{-1}$ </td><td>0.0112</td><td>0.3000</td></tr><tr><td> $2^{1}$ </td><td>0.0092</td><td>0.1777</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td rowspan="5"> $2^{-1}$ </td><td> $2^{-3}$ </td><td>0.0118</td><td>0.2287</td></tr><tr><td> $2^{-1}$ </td><td>0.0113</td><td>0.2956</td></tr><tr><td> $2^{1}$ </td><td>0.0094</td><td>0.1975</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td rowspan="5"> $2^{1}$ </td><td> $2^{-3}$ </td><td>0.0117</td><td>0.2277</td></tr><tr><td> $2^{-1}$ </td><td>0.0113</td><td>0.2956</td></tr><tr><td> $2^{1}$ </td><td>0.0095</td><td>0.1977</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1323</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1323</td></tr></table>

Table 5  
The model selection results of the single BPN model.

<table><tr><td>Number of nodes in the hidden layer</td><td>Learning rate</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5">22</td><td>0.001</td><td>0.0309</td><td>1.1231</td></tr><tr><td>0.010</td><td>0.0315</td><td>1.1006</td></tr><tr><td>0.030</td><td>0.0304</td><td>2.1932</td></tr><tr><td>0.050</td><td>0.0330</td><td>1.0548</td></tr><tr><td>0.100</td><td>0.0516</td><td>1.7929</td></tr><tr><td rowspan="5">23</td><td>0.001</td><td>0.0642</td><td>1.0329</td></tr><tr><td>0.010</td><td>0.0275</td><td>1.3008</td></tr><tr><td>0.030</td><td>0.0533</td><td>1.9315</td></tr><tr><td>0.050</td><td>0.0228</td><td>1.0866</td></tr><tr><td>0.100</td><td>0.0582</td><td>2.2638</td></tr><tr><td rowspan="5">24</td><td>0.001</td><td>0.0202</td><td>1.1652</td></tr><tr><td>0.010</td><td>0.0307</td><td>1.2753</td></tr><tr><td>0.030</td><td>0.0284</td><td>1.1012</td></tr><tr><td>0.050</td><td>0.0276</td><td>1.0006</td></tr><tr><td>0.100</td><td>0.0425</td><td>1.5303</td></tr><tr><td rowspan="5">25</td><td>0.001</td><td>0.0168</td><td>1.0459</td></tr><tr><td>0.010</td><td>0.0186</td><td>1.8150</td></tr><tr><td>0.030</td><td>0.0264</td><td>1.5934</td></tr><tr><td>0.050</td><td>0.0335</td><td>1.8796</td></tr><tr><td>0.100</td><td>0.0404</td><td>1.8129</td></tr><tr><td rowspan="5">26</td><td>0.001</td><td>0.0327</td><td>1.1931</td></tr><tr><td>0.010</td><td>0.0205</td><td>1.8069</td></tr><tr><td>0.030</td><td>0.0521</td><td>1.6475</td></tr><tr><td>0.050</td><td>0.0187</td><td>2.0333</td></tr><tr><td>0.100</td><td>0.0402</td><td>2.4788</td></tr></table>

In constructing the CMACNN model, there are again no general rules governing the choice of important CMACNN algorithm parameters: parameters E and g. It is on this basis that the trial-and-error method is adopted to determine the best parameter set for building the CMACNN sales forecasting model. The optimal settings of parameters (E, g) for the CMACNN model are evaluated by using $E = \{ 1 0 , 2 0 ,$ 30, 40, 50} and g={10, 20, 30, 40, 50}. Table 6, which lists the CMACNN model selection results, shows that the parameter set (E, g) =(40, 30) is the best model set due to having the best training and testing MSE.

In building the three two-stage forecasting schemes – the MARS– SVR, MARS–BPN, and MARS–CMACNN models – the important predictor variables obtained from the MARS forecasting model discussed earlier in this section are used as the SVR, BPN, and CMACNN input nodes. According to the MARS model described above, three signi<sup>fi</sup>- cant predictor variables are used as inputs for the three two-stage forecasting models. Using the same modeling process summarized earlier, the analytic parameter selection method is used to select the best parameter set for the MARS–SVR model. The best parameter sets for building the MARS–BPN and MARS–CMACNN sales forecasting models are determined using the trial-and-error method. Tables 7 to 9 summarize the results of testing the MARS–SVR, MARS–BPN, and MARS–CMACNN models, respectively, with different combinations of parameter sets. It can be observed from Table 7 that the parameter set $( \varepsilon = 2 ^ { - 5 } , \mathsf C = 2 ^ { - 1 } )$ is the best setup for constructing the MARS–SVR sales forecasting model. As shown in Table 8, the {4-7-1} topology with a learning rate of 0.01 is the best topology setup for the MARS–

Table 6  
The model selection results of the single CMACNN model.

<table><tr><td>E</td><td>g</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5">10</td><td>10</td><td>0.0689</td><td>0.0549</td></tr><tr><td>20</td><td>0.0371</td><td>0.8768</td></tr><tr><td>30</td><td>0.0271</td><td>0.8286</td></tr><tr><td>40</td><td>0.0219</td><td>0.7912</td></tr><tr><td>50</td><td>0.0181</td><td>0.6854</td></tr><tr><td rowspan="5">20</td><td>10</td><td>0.0219</td><td>0.7912</td></tr><tr><td>20</td><td>0.0181</td><td>0.6854</td></tr><tr><td>30</td><td>0.0156</td><td>0.6644</td></tr><tr><td>40</td><td>0.0130</td><td>0.6614</td></tr><tr><td>50</td><td>0.0500</td><td>0.5100</td></tr><tr><td rowspan="5">30</td><td>10</td><td>0.0318</td><td>0.4776</td></tr><tr><td>20</td><td>0.0167</td><td>0.5228</td></tr><tr><td>30</td><td>0.0129</td><td>0.5046</td></tr><tr><td>40</td><td>0.0108</td><td>0.4788</td></tr><tr><td>50</td><td>0.0318</td><td>0.4776</td></tr><tr><td rowspan="5">40</td><td>10</td><td>0.0108</td><td>0.4788</td></tr><tr><td>20</td><td>0.0089</td><td>0.4715</td></tr><tr><td>30</td><td>0.0054</td><td>0.4476</td></tr><tr><td>40</td><td>0.0064</td><td>0.4550</td></tr><tr><td>50</td><td>0.0378</td><td>0.4578</td></tr><tr><td rowspan="5">50</td><td>10</td><td>0.0240</td><td>0.5248</td></tr><tr><td>20</td><td>0.0194</td><td>0.5024</td></tr><tr><td>30</td><td>0.0164</td><td>0.4784</td></tr><tr><td>40</td><td>0.0139</td><td>0.4709</td></tr><tr><td>50</td><td>0.0126</td><td>0.4625</td></tr></table>

Table 7  
The model selection results of the MARS–SVR model.

<table><tr><td>ε</td><td>C</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5"> $2^{-7}$ </td><td> $2^{-3}$ </td><td>0.0107</td><td>0.6649</td></tr><tr><td> $2^{-1}$ </td><td>0.0075</td><td>0.6511</td></tr><tr><td> $2^{1}$ </td><td>0.0194</td><td>0.8567</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td rowspan="5"> $2^{-5}$ </td><td> $2^{-3}$ </td><td>0.0058</td><td>0.1608</td></tr><tr><td> $2^{-1}$ </td><td>0.0046</td><td>0.0492</td></tr><tr><td> $2^{1}$ </td><td>0.0142</td><td>0.6621</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td rowspan="5"> $2^{-3}$ </td><td> $2^{-3}$ </td><td>0.0058</td><td>0.1997</td></tr><tr><td> $2^{-1}$ </td><td>0.0046</td><td>0.0674</td></tr><tr><td> $2^{1}$ </td><td>0.0142</td><td>0.6597</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td rowspan="5"> $2^{-1}$ </td><td> $2^{-3}$ </td><td>0.0058</td><td>0.1611</td></tr><tr><td> $2^{-1}$ </td><td>0.0049</td><td>0.0582</td></tr><tr><td> $2^{1}$ </td><td>0.0162</td><td>0.6491</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td rowspan="5"> $2^{1}$ </td><td> $2^{-3}$ </td><td>0.0077</td><td>0.3869</td></tr><tr><td> $2^{-1}$ </td><td>0.0057</td><td>0.2645</td></tr><tr><td> $2^{1}$ </td><td>0.0145</td><td>0.7422</td></tr><tr><td> $2^{3}$ </td><td>0.0279</td><td>1.1517</td></tr><tr><td> $2^{5}$ </td><td>0.0279</td><td>1.1517</td></tr></table>

Table 8 The model selection results of the MARS-BPN model

<table><tr><td>Number of nodes in the hidden layer</td><td>Learning rate</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5">6</td><td>0.001</td><td>0.2297</td><td>1.2715</td></tr><tr><td>0.010</td><td>0.0091</td><td>0.8752</td></tr><tr><td>0.030</td><td>0.1352</td><td>2.0834</td></tr><tr><td>0.050</td><td>0.1699</td><td>1.4753</td></tr><tr><td>0.100</td><td>0.0249</td><td>0.8337</td></tr><tr><td rowspan="5">7</td><td>0.001</td><td>0.0184</td><td>0.8134</td></tr><tr><td>0.010</td><td>0.0348</td><td>0.7490</td></tr><tr><td>0.030</td><td>0.0202</td><td>1.2310</td></tr><tr><td>0.050</td><td>0.1110</td><td>0.8457</td></tr><tr><td>0.100</td><td>0.0583</td><td>1.4910</td></tr><tr><td rowspan="5">8</td><td>0.001</td><td>0.0948</td><td>1.2653</td></tr><tr><td>0.010</td><td>0.1431</td><td>0.7942</td></tr><tr><td>0.030</td><td>0.1126</td><td>1.8683</td></tr><tr><td>0.050</td><td>0.0963</td><td>1.7817</td></tr><tr><td>0.100</td><td>0.0142</td><td>1.5384</td></tr><tr><td rowspan="5">9</td><td>0.001</td><td>0.0500</td><td>1.6429</td></tr><tr><td>0.010</td><td>0.0590</td><td>1.0170</td></tr><tr><td>0.030</td><td>0.0257</td><td>1.3576</td></tr><tr><td>0.050</td><td>0.0053</td><td>1.2115</td></tr><tr><td>0.100</td><td>0.0138</td><td>0.9076</td></tr><tr><td rowspan="5">10</td><td>0.001</td><td>0.0663</td><td>1.1034</td></tr><tr><td>0.010</td><td>0.3057</td><td>1.3072</td></tr><tr><td>0.030</td><td>0.2787</td><td>1.0740</td></tr><tr><td>0.050</td><td>0.0053</td><td>1.0039</td></tr><tr><td>0.100</td><td>0.0081</td><td>1.0917</td></tr></table>

Table 9  
The model selection results of the MARS–CMACNN model

<table><tr><td>E</td><td>g</td><td>Training MSE</td><td>Testing MSE</td></tr><tr><td rowspan="5">10</td><td>10</td><td>0.2877</td><td>0.3596</td></tr><tr><td>20</td><td>0.2196</td><td>0.3682</td></tr><tr><td>30</td><td>0.1768</td><td>0.3512</td></tr><tr><td>40</td><td>0.1497</td><td>0.3380</td></tr><tr><td>50</td><td>0.1251</td><td>0.3307</td></tr><tr><td rowspan="5">20</td><td>10</td><td>0.2790</td><td>0.3658</td></tr><tr><td>20</td><td>0.1674</td><td>0.3471</td></tr><tr><td>30</td><td>0.1169</td><td>0.2927</td></tr><tr><td>40</td><td>0.0899</td><td>0.2298</td></tr><tr><td>50</td><td>0.0723</td><td>0.2193</td></tr><tr><td rowspan="5">30</td><td>10</td><td>0.0568</td><td>0.2057</td></tr><tr><td>20</td><td>0.0362</td><td>0.1994</td></tr><tr><td>30</td><td>0.0770</td><td>0.2163</td></tr><tr><td>40</td><td>0.0984</td><td>0.3265</td></tr><tr><td>50</td><td>0.0399</td><td>0.3029</td></tr><tr><td rowspan="5">40</td><td>10</td><td>0.1995</td><td>0.2195</td></tr><tr><td>20</td><td>0.1107</td><td>0.3181</td></tr><tr><td>30</td><td>0.0785</td><td>0.2989</td></tr><tr><td>40</td><td>0.0617</td><td>0.2763</td></tr><tr><td>50</td><td>0.0524</td><td>0.2758</td></tr><tr><td rowspan="5">50</td><td>10</td><td>0.0441</td><td>0.2542</td></tr><tr><td>20</td><td>0.0380</td><td>0.2572</td></tr><tr><td>30</td><td>0.0433</td><td>0.2363</td></tr><tr><td>40</td><td>0.1610</td><td>0.3189</td></tr><tr><td>50</td><td>0.1373</td><td>0.2982</td></tr></table>

BPN sales forecasting model. Table 9 indicates that the best parameter set for building the MARS–CMACNN sales forecasting model is (E=30, $\mathbf { g } = 2 0 )$

Table 10 compares the forecasting results derived from the seven sales forecasting models. The table shows that the MAD, RMSE, MAPE and RMSPE values for the MARS model are signi<sup>fi</sup>cantly better than those of the other six models, and hence produce the best forecasting results. Fig. 4 reports the actual sales amounts calculated using test data and the sales values predicted by the MARS model and the six comparison models. The <sup>fi</sup>gures demonstrate that the MARS model provides the best forecasting results: the values predicted by the MARS model are closer to the actual values than are those produced by the six comparison models. In addition, the table and <sup>fi</sup>gure show that the forecasting results of the two-stage models are better than those produced by the SVR, BPN, and CMACNN models. For example, the forecasting error of the MARS–SVR model is smaller than that of the SVR model. This shows that using forecasting variables that have <sup>fi</sup>rst been screened by MARS can indeed enhance model forecasting performance.

To further evaluate the forecasting performance of the MARS model, this study also employs a novel neural network algorithm called the ELM. The design of the ELM proposed by Huang et al. [25,26] is based on a single-hidden layer feedforward neural network (SLFNN) with a wide variety of hidden nodes, which randomly generates hidden parameters before analytically determining the output weights [29,58]. Prior investigations have reported that the ELM tends to provide better generalization performance and a much faster learning speed than BPN and SVR models [25,26]. As many studies have demonstrated that the ELM can be successfully used for sales forecasting [15,47,58,64], the

Table 10  
The comparison of the forecast results from the seven types of sales forecasting model.

<table><tr><td>Methods</td><td>MAD</td><td>RMSE</td><td>MAPE</td><td>RMSPE</td></tr><tr><td>MARS</td><td>52.49</td><td>134.06</td><td>0.11</td><td>0.21</td></tr><tr><td>SVR</td><td>147.56</td><td>202.01</td><td>0.32</td><td>0.36</td></tr><tr><td>BPN</td><td>260.72</td><td>357.83</td><td>0.41</td><td>0.74</td></tr><tr><td>CMACNN</td><td>189.75</td><td>264.06</td><td>0.36</td><td>0.44</td></tr><tr><td>MARS-SVR</td><td>117.51</td><td>140.72</td><td>0.25</td><td>0.34</td></tr><tr><td>MARS-BPN</td><td>256.49</td><td>353.73</td><td>0.38</td><td>0.48</td></tr><tr><td>MARS-CMACNN</td><td>155.83</td><td>218.00</td><td>0.36</td><td>0.43</td></tr></table>

(a) comparison of MARS, SVR and MARS-SVR  
![](/api/attachments/D88GM5V7/fulltext/images/097b74abbd4fd96df886852d7042b3ec743dfec93119b3d8768d9d834168e1d4.jpg)

(b) comparison of MARS, BPN and MARS-BPN  
![](/api/attachments/D88GM5V7/fulltext/images/547c3696dd8f02593b66d9d23d49e52e1626b02bcf9f1cdf7c5d677f8ecaabed.jpg)

(c) comparison of MARS, CMACNN and MARS-CMACNN  
![](/api/attachments/D88GM5V7/fulltext/images/96569d017d6a65ff55d9a5d715d380fa464b80623b405eb70a4d29d260f2bf0b.jpg)  
Fig. 4. The actual sales amounts of testing data and their predicted values from the MARS and the six comparison models.

![](/api/attachments/D88GM5V7/fulltext/images/96a6812da0e1c87b3404454636888480e369b7002923504991d0565e4234ae84.jpg)  
Fig. 5. The RMSE values of the ELM and MARS–ELM models with different numbers of hidden nodes.

Table 11  
The comparison of the forecast results from the ELM, MARS–ELM, ARIMA, MLR and the MARS models.

<table><tr><td>Methods</td><td>MAD</td><td>RMSE</td><td>MAPE</td><td>RMSPE</td></tr><tr><td>MARS</td><td>52.49</td><td>134.06</td><td>0.11</td><td>0.21</td></tr><tr><td>ELM</td><td>186.33</td><td>233.71</td><td>0.35</td><td>0.42</td></tr><tr><td>MARS-ELM</td><td>146.25</td><td>210.06</td><td>0.33</td><td>0.40</td></tr><tr><td>ARIMA</td><td>666.06</td><td>845.52</td><td>0.56</td><td>0.66</td></tr><tr><td>MLR</td><td>629.91</td><td>944.65</td><td>0.64</td><td>1.01</td></tr></table>

ELM model using the original input variables as direct inputs and the two-stage MARS–ELM model utilizing the same procedure as the two-stage forecasting models described earlier are used as comparison models in this study. Moreover, to fully assess the performance of the MARS model, its forecasting performance is compared with that of the traditional ARIMA and multivariate linear regression (MLR) speci<sup>fi</sup>cations.

It is known that the most important and critical ELM parameter is the number of hidden nodes and that ELM tends to be unstable in single run forecasting [25,26,47]. Therefore, ELM and MARS–ELM models with different numbers of hidden nodes varying from 1 to 15 are constructed. For each number of nodes, the ELM and MARS–ELM models are repeated 30 times and the number of hidden nodes that gives the smallest testing RMSE value is selected. Fig. 5 shows the RMSE values of the ELM and MARS–ELM models with different numbers of hidden nodes. From the <sup>fi</sup>gure, it can be seen that the ELM model with four hidden nodes and the MARS–ELM model with three hidden nodes have the smallest RMSE values and are therefore the best ELM and MARS–ELM models considered in this study.

Table 11 summarizes the sales forecasting results of the ELM, MARS–ELM, ARIMA, and MLR models. Note that the ARIMA and MLR models are estimated using SAS software. Table 11 also compares the MARS model with these four comparison models and shows that the MARS model has the smallest MAD, RMSE, MAPE and RMSPE values. Fig. 6 shows the actual sales amounts based on test data and the forecasting results generated by the MARS, ELM, MARS–ELM, ARIMA and MLR models. showing that the forecasting results of the MARS model are superior to those of the four comparison models. It can therefore be concluded that the MARS model outperforms the ELM, MARS–ELM, ARIMA and MLR models in forecasting computer wholesaler sales. Table 11 and Fig. 6 also show that using the MARS model to select important forecasting variables can improve forecasting results, as the forecasting performance of the MARS–ELM model is better than that of the ELM model.

Based on the <sup>fi</sup>ndings discussed above, it can be inferred that the MARS methodology is suitable for constructing forecasting models for computer wholesalers due to its excellent variable screening and model interpretation credentials.

## 3.3. Robustness evaluation and significance test

The performance of the 11 forecasting models compared in this study is tested using different ratios of training and testing sample sizes (the relative ratio) to evaluate the robustness of the proposed MARS method. The testing plan is based on the relative ratio calculated as the size of the training dataset to the size of the complete dataset. Three relative ratios are considered: 70, 80, and 90%. The sales data prediction results for the 11 methods examined herein are summarized in Table 12 in terms of the MAPE metric. From Table 12, it can be seen that the MARS model has the lowest MAPE for all the testing ratios. Its forecasting results are also far better than those produced using the other methods, indicating that the MARS methodology indeed provides better forecasting accuracy than the other ten approaches and is suitable for computer wholesaler sales forecasting.

The Wilcoxon signed-rank test is also used to test whether the MARS model developed in this study is superior to the other ten sales forecasting models. The test is a distribution-free, non-parametric technique that does not require any underlying distribution in the data and deals with the signs and ranks of the values rather than with their magnitude (and thus is not in<sup>fl</sup>uenced by outlier data points). It is one of the most commonly adopted tests for evaluating the predictive capabilities of two different models [21,43].

We employ the test to evaluate the predictive performance of the 11 built models under different training dataset size to complete dataset size ratios. Table 13 compares the Z statistic values calculated under the two-tailed Wilcoxon signed-rank test for RMSE values for the built MARS model and the other ten models, where the numbers in parentheses are the corresponding p-values. Table 13 shows that the MARS model gives better forecasting results than all the other models (with pb0.01). We therefore conclude that the MARS speci<sup>fi</sup>cation is signi<sup>fi</sup>- cantly better than the other 10 models in forecasting sales for computer wholesalers.

3.4. Discussion on the selection of MARS variables and the basis function results

Table 14 brings together MARS variable screening results under different training to testing sample size ratios to facilitate discussion of the selection results. From Table 14, it can be observed that variables X1(MA3), X3(T-1), and X4(T-2) are picked up by MARS screening, signifying the importance of these three variables to sales forecasting for computer wholesalers and con<sup>fi</sup>rming the consistent variable screening ability of MARS.

The Table 14 results also provide us with an opportunity to discuss the sales management implications of MARS basic functions. Under the relative ratio of 70%, among the BF1 selected by MARS, when the three-month moving average (X1) is higher than 1318, the sales amount for the following month will be higher. Conversely, when the quarterly moving average is lower than 1318, it gives no information about the sales amount for the following month.

![](/api/attachments/D88GM5V7/fulltext/images/27aa614647c2a8e958a43fc47a62c85147b1abbe953ae8d44afe11c3f0c9951c.jpg)  
Fig. 6. The actual sales amounts of testing data and their predicted values from the MARS, ELM, MARS–ELM, ARIMA and MLR models

Table 12  
Robustness evaluation of the eleven forecasting models under different relative ratios.

<table><tr><td>Relative ratio (%)</td><td>Models</td><td>Testing MAPE (%)</td></tr><tr><td rowspan="11">90</td><td>MARS</td><td>0.07</td></tr><tr><td>SVR</td><td>0.18</td></tr><tr><td>BPN</td><td>0.44</td></tr><tr><td>CMACNN</td><td>0.24</td></tr><tr><td>ELM</td><td>0.25</td></tr><tr><td>ARIMA</td><td>0.53</td></tr><tr><td>MLR</td><td>0.48</td></tr><tr><td>MARS-SVR</td><td>0.14</td></tr><tr><td>MARS-BPN</td><td>0.30</td></tr><tr><td>MARS-CMACNN</td><td>0.17</td></tr><tr><td>MARS-ELM</td><td>0.21</td></tr><tr><td rowspan="11">80</td><td>MARS</td><td>0.11</td></tr><tr><td>SVR</td><td>0.32</td></tr><tr><td>BPN</td><td>0.41</td></tr><tr><td>CMACNN</td><td>0.36</td></tr><tr><td>ELM</td><td>0.35</td></tr><tr><td>ARIMA</td><td>0.56</td></tr><tr><td>MLR</td><td>0.64</td></tr><tr><td>MARS-SVR</td><td>0.25</td></tr><tr><td>MARS-BPN</td><td>0.38</td></tr><tr><td>MARS-CMACNN</td><td>0.36</td></tr><tr><td>MARS-ELM</td><td>0.33</td></tr><tr><td rowspan="11">70</td><td>MARS</td><td>0.19</td></tr><tr><td>SVR</td><td>0.37</td></tr><tr><td>BPN</td><td>0.45</td></tr><tr><td>CMACNN</td><td>0.40</td></tr><tr><td>ELM</td><td>0.38</td></tr><tr><td>ARIMA</td><td>0.54</td></tr><tr><td>MLR</td><td>0.68</td></tr><tr><td>MARS-SVR</td><td>0.30</td></tr><tr><td>MARS-BPN</td><td>0.42</td></tr><tr><td>MARS-CMACNN</td><td>0.33</td></tr><tr><td>MARS-ELM</td><td>0.35</td></tr></table>

Second, in BF3, when the sales amount in the (t-1) period rises above 2895, the sales amount will be lower, but there will be no impact if it goes below 2895 (thousand dollars). In BF4, sales are not affected when the sales amount in the (t-1) period rises above 2895, but they will grow if it falls below 2895. Based on the BF3 and BF4 results, it can be determined that when the sales amount in the (t-1) period is above 2895, sales will fall. Conversely, when the sales amount in the (t-1) period is below 2895, sales will increase. Finally, for BF5, when the sales amount in the (t-2) period is above 857, sales will decline from the next month onwards.

From the detailed discussion of BFs, it can be found that MARS can show the major turning points and changes with its prediction model. The knot value of the predictor variable X1 is 1318, which is the sales turning point because we can see from Fig. 3 that there was no lower level of sales for most of the period. Therefore, if the three-month moving average is less than 1300, then the sales <sup>fi</sup>gure should increase in the following month. The knot value of the predictor variable X3 (t-1 period), i.e. 2895, can be used to describe the turning point of the highest sales <sup>fi</sup>gure. In Fig. 3, the highest point of the vast majority of the sales data is around 3000. Finally, the knot value of the predictor variable X4 (t-2 period), i.e. 857, can be used to indicate the variation in the lower sales <sup>fi</sup>gures, especially those that are particularly low (due to certain major events). An example can be found in Fig. 3, in which the lowest sales <sup>fi</sup>gure, 857, was observed in 2002. As MARS can show the major turning points and changes with its prediction model, it can offer better prediction performance than the comparison methods.

Table 14  
Basis functions and selected important forecasting variables with different ratios of training and testing sample sizes using MARS.

<table><tr><td>Relative ratio (%)</td><td>Selected variables</td><td>Relative importance</td><td>Basis functions</td></tr><tr><td rowspan="7">90</td><td>X1(MA3)</td><td>100.00%</td><td>BF1 = max(0, X1 - 1086);</td></tr><tr><td>X4(T-2)</td><td>62.04%</td><td>BF5 = max(0, X3 - 3387);</td></tr><tr><td>X3(T-1)</td><td>61.85%</td><td>BF6 = max(0, 3387 - X3);</td></tr><tr><td></td><td></td><td>BF7 = max(0, X4 - 2004);</td></tr><tr><td></td><td></td><td>BF8 = max(0, 2004 - X4);</td></tr><tr><td colspan="3">MARS prediction function:</td></tr><tr><td colspan="3">f(x) = -2131.54 + 3.00*BF1 - 1.00*BF5 + 1.00*BF6 - 1.00*BF7 + 1.00*BF8;</td></tr><tr><td rowspan="6">80</td><td>X1(MA3)</td><td>100.00%</td><td>BF2 = max(0, X1 - 381);</td></tr><tr><td>X4(T-2)</td><td>78.93%</td><td>BF4 = max(0,X4 - 1226);</td></tr><tr><td>X3(T-1)</td><td>46.69%</td><td>BF5 = max(0,1226 - X4);</td></tr><tr><td></td><td></td><td>BF6 = max(0, X3 - 282);</td></tr><tr><td colspan="3">MARS prediction function:</td></tr><tr><td colspan="3">f(x) = -365.25 + 3.00*BF2 - 1.00*BF4 + 1.00*BF5 - 1.00*BF6;</td></tr><tr><td rowspan="6">70</td><td>X1(MA3)</td><td>100.00%</td><td>BF1 = max(0, X1 - 1318);</td></tr><tr><td>X3(T-1)</td><td>62.82%</td><td>BF3 = max(0, X3 - 2895);</td></tr><tr><td>X4(T-2)</td><td>62.22%</td><td>BF4 = max(0, 2895 - X3);</td></tr><tr><td></td><td></td><td>BF5 = max(0, X4 - 857);</td></tr><tr><td colspan="3">MARS prediction function:</td></tr><tr><td colspan="3">f(x) = 203.35 + 3.00*BF1 - 1.00*BF3 + 1.00*BF4 - 1.00*BF5;</td></tr></table>

The foregoing discussion also draws attention to the implication of these numerical turning points: when sales go above/below a certain value, the company may need to adjust its operating strategy. For example, when the following month's sales are forecast to be higher, the company will need to employ only <sup>fi</sup>xed time interval advertising to maintain consumer awareness; if lower sales are forecast for the coming period, however, then the company may have to engage in additional promotional activities or increase the frequency of its advertising to attract consumers.

## 3.5. Evaluating the effectiveness of the MARS model using additional sales data

In this section, additional monthly sales amounts provided by another computer wholesaler in Taiwan (called Company B) are used to evaluate the effectiveness of the MARS model in more depth. The Company B data used in this study were collected between January 1997 and February 2010, as shown in Fig. 7. Company B is a small computer wholesaler and its main target customers are retail stores in business districts, end users with higher purchasing power and small-sized enterprises. It mainly sells the products of large computer brands such as HP, ASUS and ACER. The following are the major events during that period which signi<sup>fi</sup>cantly affected Company B's sales.

Table 13  
Wilcoxon signed-rank test between the MARS model and the ten comparison models by different relative ratios (%).

<table><tr><td rowspan="2">Model</td><td rowspan="2">%</td><td colspan="10">Comparison models</td></tr><tr><td>SVR</td><td>BPN</td><td>CMACNN</td><td>MARS-SVR</td><td>MARS-BPN</td><td>MARS-CMACNN</td><td>ELM</td><td>ARIMA</td><td>MLR</td><td>MARS-ELM</td></tr><tr><td rowspan="3">MARS</td><td>90</td><td>-3.672(0.000)</td><td>-5.031(0.000)</td><td>-4.180(0.000)</td><td>-3.287(0.000)</td><td>-4.903(0.000)</td><td>-3.585(0.000)</td><td>-4.261(0.000)</td><td>-5.475(0.000)</td><td>-5.291(0.000)</td><td>-3.787(0.000)</td></tr><tr><td>80</td><td>-2.580(0.010)</td><td>-3.983(0.000)</td><td>-3.166(0.001)</td><td>-2.076(0.038)</td><td>-3.571(0.000)</td><td>-3.011(0.000)</td><td>-3.095(0.001)</td><td>-4.691(0.000)</td><td>-4.814(0.000)</td><td>-2.673(0.009)</td></tr><tr><td>70</td><td>-2.992(0.003)</td><td>-4.151(0.000)</td><td>-3.366(0.000)</td><td>-2.889(0.003)</td><td>-3.777(0.000)</td><td>-3.310(0.001)</td><td>-3.012(0.002)</td><td>-4.581(0.000)</td><td>-4.932(0.000)</td><td>-3.512(0.000)</td></tr></table>

Note: The numbers in parentheses are the corresponding p-values.

![](/api/attachments/D88GM5V7/fulltext/images/2fb6c413ad5ecfc2d07279c2388ed5f6395a9c08930330b6c36697396cef5cd1.jpg)  
Fig. 7. An additional monthly sales amount from January 1997 to February 2010

➣ 1999–2000: Computer sales increased as there were more low-cost computers on the market and the Internet had become more popular.

➣ 2004: Intel released a CPU with new architecture that promoted the growth in demand for personal computers.

➣ 2006: Microsoft launched a new operating system and more customers became keen on purchasing new computers.

➣ 2008: Sales in the personal computer market were seriously affected by the global <sup>fi</sup>nancial crisis and poor economic conditions.

➣ 2009: Low-cost netbook PCs came onto the market, and with subsidies from the Taiwanese government their sales increased.

As Fig. 7 shows, the dataset includes a total of 158 monthly sales amounts. Using the same modeling process as that described in

Comparison of forecasting results of the MARS and the ten comparison models under different relative ratios by using the additional sales data.

<table><tr><td>Relative ratio (%)</td><td>Models</td><td>Testing MAPE (%)</td></tr><tr><td rowspan="11">90</td><td>MARS</td><td>0.02</td></tr><tr><td>SVR</td><td>0.14</td></tr><tr><td>BPN</td><td>1.42</td></tr><tr><td>CMACNN</td><td>0.45</td></tr><tr><td>ELM</td><td>0.25</td></tr><tr><td>ARIMA</td><td>0.46</td></tr><tr><td>MLR</td><td>0.94</td></tr><tr><td>MARS-SVR</td><td>0.03</td></tr><tr><td>MARS-BPN</td><td>0.63</td></tr><tr><td>MARS-CMACNN</td><td>0.31</td></tr><tr><td>MARS-ELM</td><td>0.22</td></tr><tr><td rowspan="11">80</td><td>MARS</td><td>0.02</td></tr><tr><td>SVR</td><td>0.28</td></tr><tr><td>BPN</td><td>0.58</td></tr><tr><td>CMACNN</td><td>0.57</td></tr><tr><td>ELM</td><td>0.34</td></tr><tr><td>ARIMA</td><td>0.72</td></tr><tr><td>MLR</td><td>0.61</td></tr><tr><td>MARS-SVR</td><td>0.06</td></tr><tr><td>MARS-BPN</td><td>0.40</td></tr><tr><td>MARS-CMACNN</td><td>0.56</td></tr><tr><td>MARS-ELM</td><td>0.31</td></tr><tr><td rowspan="11">70</td><td>MARS</td><td>0.04</td></tr><tr><td>SVR</td><td>0.29</td></tr><tr><td>BPN</td><td>0.93</td></tr><tr><td>CMACNN</td><td>1.11</td></tr><tr><td>ELM</td><td>0.37</td></tr><tr><td>ARIMA</td><td>0.81</td></tr><tr><td>MLR</td><td>0.68</td></tr><tr><td>MARS-SVR</td><td>0.08</td></tr><tr><td>MARS-BPN</td><td>0.56</td></tr><tr><td>MARS-CMACNN</td><td>0.67</td></tr><tr><td>MARS-ELM</td><td>0.35</td></tr></table>

Sections 3.1 to 3.4, Table 15 compares the forecasting results of the MARS model with those of the other ten comparison models under different relative ratios. From Table 15, it can be seen that the MARS model also outperforms the ten comparison models in the additional testing dataset. These supplementary results therefore provide further evidence that the MARS model delivers better forecasting accuracy than the other ten approaches in the computer wholesaler sales context. Moreover, it also can be observed from Table 15 that the MARS model is an effective variable screening tool because the forecasting performance of two-stage models is better than those of forecasting models with all independent variables as inputs.

Table 16 shows the basis functions obtained and the important forecasting variables selected under different relative ratios when the additional sales data are entered into the MARS model. The table demonstrates that for all the relative ratios tested, the signi<sup>fi</sup>cant predictor variables selected are X1(MA3), X3(T-1), and X4(T-2), identical to those selected using the <sup>fi</sup>rst dataset in the MARS model. The numerical turning points in the basis functions also provide valuable insights into how to make better sales/inventory management decisions.

The <sup>fi</sup>ndings reported in this section therefore show that the threemonth moving average (MA3), previous two months' sales volume (T-2), and previous month's sales volume (T-1) variables can provide computer wholesalers with valuable information for sales and

## Table 16

Basis functions and selected important forecasting variables with different ratios of training and testing sample sizes using MARS for the additional sales data.

<table><tr><td>Relative ratio (%)</td><td>Selected variables</td><td>Relative importance</td><td>Basis functions</td></tr><tr><td rowspan="8">90</td><td>X1(MA3)</td><td>100.00%</td><td>BF7 = max(0, X1 - 602);</td></tr><tr><td>X4(T-2)</td><td>64.19%</td><td>BF8 = max(0, 602 - X1(3));</td></tr><tr><td>X3(T-1)</td><td>58.23%</td><td>BF9 = max(0, X4 - 1078);</td></tr><tr><td></td><td></td><td>BF10 = max(0, 1078 - X4);</td></tr><tr><td></td><td></td><td>BF11 = max(0, X3 - 1520);</td></tr><tr><td></td><td></td><td>BF12 = max(0, 1520 - X3);</td></tr><tr><td colspan="3">MARS prediction function:</td></tr><tr><td colspan="3">f(x) = -791.42 + 3.00*BF7 - 3.00*BF8 - 1.00*BF9 + 1.00*BF10 - 1.00*BF11 + 1.00*BF12;</td></tr><tr><td rowspan="7">80</td><td>X1(MA3)</td><td>100.00%</td><td>BF1 = max(0, X1 - 375);</td></tr><tr><td>X4(T-2)</td><td>62.29%</td><td>BF4 = max(0,X4 - 1061);</td></tr><tr><td>X3(T-1)</td><td>58.51%</td><td>BF5 = max(0,1061 - X4);</td></tr><tr><td></td><td></td><td>BF6 = max(0,X3 - 1513);</td></tr><tr><td></td><td></td><td>BF7 = max(0,1513 - X3);</td></tr><tr><td colspan="3">MARS prediction function:</td></tr><tr><td colspan="3">f(x) = -1449.53 + 3.00*BF1 - 1.00*BF4 + 1.00*BF5 - 1.00*BF6 + 1.00*BF7;</td></tr><tr><td rowspan="8">70</td><td>X1(MA3)</td><td>100.00%</td><td>BF6 = max(0, X1 - 736);</td></tr><tr><td>X4(T-2)</td><td>64.01%</td><td>BF7 = max(0, 736 - X1);</td></tr><tr><td>X3(T-1)</td><td>61.00%</td><td>BF8 = max(0, X4 - 1096);</td></tr><tr><td></td><td></td><td>BF9 = max(0, 1096 - X4);</td></tr><tr><td></td><td></td><td>BF10 = max(0, X3 - 1457);</td></tr><tr><td></td><td></td><td>BF11 = max(0, 1457 - X3);</td></tr><tr><td colspan="3">MARS prediction function:</td></tr><tr><td colspan="3">f(x) = -342.95 + 3.00*BF6 - 3.00*BF7 - 1.00*BF8 + 1.00*BF9 - 1.00*BF10 + 1.00*BF11;</td></tr></table>

inventory decisions. The sales turning points indicated by the MARS basis functions can help companies adapt their operating strategies to secure better performance in the future.

## 4. Conclusion

Sales forecasting is a crucial aspect of business <sup>fi</sup>nancial planning, inventory management, and customer service among computer wholesalers due to the demand uncertainty they face and the short lifespan and quick obsolescence of IT products. This study uses MARS, a nonlinear and non-parametric regression methodology, to construct a sales forecasting model for a computer wholesaler and investigate the relationship between important forecasting variables and sales amounts through the basis functions and forecasting function constructed. The experiments evaluate two sets of real sales data collected from two Taiwanese computer wholesalers. The forecasting results obtained using the MARS model are compared with those of the SVR, BPN, ELM, CMACNN, ARIMA, and MLR models, along with those of four two-stage forecasting models: the MARS–SVR, MARS–BPN, MARS–ELM, and MARS–CMACNN models. The experimental results show that the MARS methodology produces results with a lower degree of prediction error and outperforms the ten comparison methods. The results also demonstrate that MARS represents a good alternative sales forecasting method for computer wholesalers, as it delivers good forecasting performance and is capable of identifying signi<sup>fi</sup>cant forecasting variables – in this case, three-month moving average (MA3), previous two months' sales volume (T-2), and previous month's sales volume (T-1) – which may provide valuable information for further sales and inventory decisions/ strategies. Moreover, the sales turning points identi<sup>fi</sup>ed by MARS basis functions can help companies adjust their operating strategy to support better performance in the future.

## Acknowledgment

This work is partially supported by the National Science Council of the Republic of China, Grant nos. NSC 98-2622-E-231-005-CC3 and NSC 99-2622-E-231-003-CC3. The authors also gratefully acknowledge the helpful comments and suggestions of the reviewers, which have improved the presentation.

## References

[1] J.S. Albus, A new approach to manipulator control: the cerebellar model articulation controller (CMAC), ASME Journal of Dynamic Systems Measurement and Control 97 (1975) 220–227.

[2] A. Andalib, F. Atry, Multi-step ahead forecasts for electricity prices using NARX: a new approach, a critical analysis of one-step ahead forecasts, Energy Conversion and Management 50 (3) (2009) 739–747.

[3] G.S. Atsalakis, K.P. Valavanis, Surveying stock market forecasting techniques — part II: soft computing methods, Expert Systems with Applications 36 (3) (2009) 5932–5941.

[4] P. Bartlett, The sample complexity of pattern classi<sup>fi</sup>cation with neural networks: the size of the weights is more important than the size of the network, IEEE Transactions on Information Theory 44 (2) (1998) 525–536.

[5] L.C. Briand, B. Freimut, F. Vollei, Using multiple adaptive regression splines to support decision making in code inspections, Journal of Systems and Software 73 (2) (2004) 205–217.

[6] M. Castro-Neto, Y.S. Jeong, M.K. Jeong, L.D. Han, Online-SVR for short-term traf<sup>fi</sup>c <sup>fl</sup>ow prediction under typical and atypical traf<sup>fi</sup>c conditions, Expert Systems with Applications 36 (3) (2009) 6164–6173.

[7] P.C. Chang, C.Y. Lai, A hybrid system combining self-organizing maps with case-based reasoning in wholesaler's new-release book forecasting, Expert Systems with Applications 29 (1) (2005) 183–192

[8] C.C. Chang, C.J. Lin, LIBSVM: a library for support vector machines. available online at: http://www.csie.ntuedu.tw/\~cilin/libsym/index.html2010.

[9] P.C. Chang, Y.W. Wang, Fuzzy Delphi and back-propagation model for sales forecasting in PCB industry, Expert Systems with Applications 30 (4) (2006) 715–726.

[10] P.C. Chang, C.Y. Lai, K.R. Lai, A hybrid system by evolving case-based reasoning with genetic algorithm in wholesaler's returning book forecasting, Decision Support Systems 42 (3) (2006) 1715–1729.

[11] P.C. Chang, C.H. Liu, Y.W. Wang, A hybrid model by clustering and evolving fuzzy rules for sales decision supports in printed circuit board industry, Decision Support Systems 42 (3) (2006) 1254–1269.

[12] P.C. Chang, Y.W. Wang, C.H. Liu, The development of a weighted evolving fuzzy neural network for PCB sales forecasting, Expert Systems with Applications 32 (1) (2007) 86–96.

[13] P.C. Chang, C.H. Liu, C.Y. Fan, Data clustering and fuzzy neural network for sales forecasting: a case study in printed circuit board industry, Knowledge-Based Systems 22 (5) (2009) 344–355.

[14] Y. Chauvin, D.E. Rumelhart, Backpropagation: Theory Architectures and Applications, Lawrence Erlbaum Associates, New Jersey, 1995.

[15] F.L. Chen, T.Y. Ou, Sales forecasting system based on gray extreme learning machine with Taguchi method in retail industry, Expert Systems with Applications 38 (3) (2011) 1336–1345.

[16] W. Chen, C. Ma, L. Ma, Mining the customer credit using hybrid support vector machine technique, Expert Systems with Applications 36 (4) (2009) 7611–7616.

[17] V. Cherkassky, Y. Ma, Practical selection of SVM parameters and noise estimation for SVM regression, Neural Networks 17 (2004) 113–126.

[18] N.R. Cook, R.Y.L. Zee, P.M. Ridker, Tree and spline based association analysis of gene–gene interaction models for ischemic stroke, Statistics in Medicine 23 (9) (2004) 1439–1453.

[19] S.F. Crone, J. Guajardo, R. Weber, The impact of preprocessing on support vector regression and neural networks in time series prediction, in: Proceedings of the International Conference on Data Mining, Las Vegas, USA, 2006, pp. 37–44.

[20] S.F. Crone, S. Lessmann, R. Stahlbock, The impact of preprocessing on data mining: an evaluation of classi<sup>fi</sup>er sensitivity in direct marketing, European Journal of Operational Research 173 (3) (2006) 781–800.

[21] F.X. Diebold, R.S. Mariano, Comparing predictive accuracy, Journal of Business and Economic Statistics 13 (1995) 253–263.

[22] R. Fildes, K. Nikolopoulos, S.F. Crone, A.A. Syntetos, Forecasting and operational research: a review, Journal of the Operational Research Society 59 (9) (2008) 1150–1172.

[23] J.H. Friedman, Multivariate adaptive regression splines, The Annals of Statistics 19 (1) (1991) 1–141.

[24] S. Haykin, Neural Network: A Comprehensive Foundation, Prentice Hall, New Jersey, 1999.

[25] G.B. Huang, Q.Y. Zhu, C.K. Siew, Extreme learning machine: a new learning scheme of feedforward neural networks, in: Proceedings of 2004 International Joint Conference on Neural Networks, Budapest, Hungary, 2004, pp. 985–990.

[26] G.B. Huang, Q.Y. Zhu, C.K. Siew, Extreme learning machine: theory and applications, Neurocomputing 70 (2006) 489–501.

[27] A. Hyunchul, C. Eunsup, H. Ingoo, Extracting underlying meaningful features and canceling noise using independent component analysis for direct marketing, Expert Systems with Applications 33 (1) (2007) 181–191.

[28] R.J. Kuo, K.C. Xue, A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 (2) (1998) 105–126.

[29] Y. Lan, Y.C. Soh, G.B. Huang, Constructive hidden nodes selection of extreme learning machine for regression, Neurocomputing 73 (2010) 3191–3199.

[30] Y. Lee, S. Oh, M.W. Kim, An analysis of premature saturation in back propagation learning, Neural Networks 6 (5) (1993) 719–728.

[31] T.S. Lee, C.C. Chiu, Y.C. Chou, C.J. Lu, Mining the customer credit using classi<sup>fi</sup>cation and regression tree and multivariate adaptive regression splines, Computa tional Statistics and Data Analysis 50 (4) (2006) 1113–1130.

[32] C.M. Lin, L.Y. Chen, C.H. Chen, RCMAC hybrid control for MIMO uncertain nonlinear systems using sliding-mode technology, IEEE Transactions on Neural Networks 18 (2007) 708–720

[33] H.Y. Lin, W. Wang, Y.H. Liu, S.J. Soong, T.P. York, L. Myers, J.J. Hu, Comparison of multivariate adaptive regression splines and logistic regression in detecting SNP–SNP interactions and their application in prostate cancer, Journal of Human Genetics 53 (9) (2008) 802–811.

[34] C.J. Lu, Y.W. Wang, Combining independent component analysis and growing hierarchical self-organizing maps with support vector regression in product demand forecasting, International Journal of Production Economics 128 (2) (2010) 603–613.

[35] C.J. Lu, J.Y. Wu, Forecasting <sup>fi</sup>nancial time series via an ef<sup>fi</sup>cient CMAC neural network, Lecture Notes in Electrical Engineering 67 (2010) 73–82.

[36] C.J. Lu, T.S. Lee, C.C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2) (2009) 115–125.

[37] A. Luis, W. Richard, Improved supply chain management based on hybrid demand forecasts, Applied Soft Computing 7 (1) (2007) 136–144.

[38] MARS 2.0—for Windows 95/98/NT, Salford Systems, San Diego, CA, 2001.

[39] W.T. Miller, F.H. Glanz, L.G. Kraft, CMAC: an associative neural network alternative to backpropagation, Proceedings of the IEEE 78 (1990) 1561–1567.

[40] S. Mukkamala, A.H. Sung, A. Abraham, Intrusion detection using an ensemble of intelligent paradigms, Journal of Network and Computer Applications 28 (2) (2005) 167–182.

[41] Y. Ni, F. Fan, A two-stage dynamic sales forecasting model for the fashion retail, Expert Systems with Applications 38 (3) (2011) 1529–1536.

[42] P.F. Pai, S.L. Yang, P.T. Chang, Forecasting output of integrated circuit industry by support vector regression models with marriage honey-bees optimization algorithms Expert Systems with Applications 36 (7) (2009) 10746–10751.

[43] A.C. Pollock, A. Macaulay, M.E. Thomson, D. Onkal, Performance evaluation of judgemental directional exchange rate predictions, International Journal of Forecasting 21 (2005) 473–489.

[44] D. Qiaolin, T. Jing, L. Jianxin, Application of new FCMAC neural network in power system marginal price forecasting, in: Proceedings of the 7th International Power Engineering Conference, Singapore, 2005, pp. 1–57.

[45] N. Raj Kiran, V. Ravi, Software reliability prediction by soft computing techniques, Journal of Systems and Software 81 (4) (2008) 576–583.

[46] D.M. Shi, J.B. Gao, R. Tilani, Univariate time series forecasting with fuzzy CMAC, in: Proceedings of the 2004 International Conference on Machine Learning and Cy bernetics, Singapore, 2004, pp. 4166–4170.

[47] Z.L. Sun, T.M. Choi, K.F. Au, Y. Yu, Sales forecasting using extreme learning machine with applications in fashion retailing, Decision Support Systems 46 (1) (2008) 411–419.

[48] K. Tanaka, A sales forecasting model for new-released and nonlinear sales trend products, Expert Systems with Applications 37 (11) (2010) 7387–7393.

[49] Z. Tang, P.A. Fishwick, Feed-forward neural nets as models for time series forecasting, ORSA Journal on Computing 4 (5) (1993) 374–386.

[50] F.E.H. Tay, L.J. Cao, Application of support vector machines in <sup>fi</sup>nancial time series forecasting, Omega 29 (2001) 309–317.

[51] F.E.H. Tay, L.J. Cao, Support vector machine with adaptive parameters in <sup>fi</sup>nancial time series forecasting, IEEE Transactions on Neural Networks 14 (2003) 1506–1518.

[52] S. Thomassey, Sales forecasts in clothing industry: the key success factor of the supply chain management, International Journal of Production Economics 128 (2) (2010) 470–483.

[53] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (1) (2006) 408–421.

[54] S. Thomassey, M. Happiette, A neural clustering and classi<sup>fi</sup>cation system for sales forecasting of new apparel items, Applied Soft Computing 7 (4) (2007) 1177–1187.

[55] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 2000.

[56] A. Vellido, P.J.G. Lisboa, J. Vaughan, Neural networks in business: a survey of applications (1992–1998), Expert Systems with Applications 17 (1999) 51–70.

[57] S. Wang, Z. Jiang, Valve fault detection and diagnosis based on CMAC neural networks, Energy and Buildings 36 (2004) 599–610.

[58] W.K. Wong, Z.X. Guo, A hybrid intelligent model for medium-term sales forecasting in fashion retail supply chains using extreme learning machine and harmony search algorithm, International Journal of Production Economics 128 (2) (2010) 614–624.

[59] Y.F. Wong, A. Sideris, Learning convergence in the cerebellar model articulation controller, IEEE Transactions on Neural Networks 3 (1992) 115–121.

[60] S. Wood, Float Analysis: Powerful Technical Indicators using Price and Volume, John Wiley & Sons, New York, 2002.

[61] Q. Wu, The forecasting model based on wavelet ν-support vector machine, Expert Systems with Applications 36 (4) (2009) 7604–7610.

[62] J.Y. Wu, C.J. Lu, Applying classi<sup>fi</sup>cation problems via a data mining approach based on a cerebellar model articulation controller, in: Proceedings of the 1st Asian Conference on Intelligent Information and Database Systems, Dong Hoi City, Vietnam, 2009, pp. 61–66.

[63] Y. Yang, R. Fuli, C. Huiyou, X. Zhijiao, SVR mathematical model and methods for sale prediction, Journal of Systems Engineering and Electronics 18 (4) (2007) 769–773.

[64] Y. Yu, T.M. Choi, C.L. Hui, An intelligent fast sales forecasting model for fashion products, Expert Systems with Applications 38 (6) (2011) 7373–7379.

[65] G. Zhang, B.E. Patuwo, M.Y. Hu, Forecasting with arti<sup>fi</sup>cial neural networks: the state of the art, International Journal of Forecasting 14 (1998) 35–62.

[66] Y. Zhou, H. Leung, Predicting object-oriented software maintainability using multivariate adaptive regression splines, Journal of Systems and Software 80 (8) (2007)1349-1361

[67] H. Zhou, J. Chen, H. Wu, S.L. Ho, CMAC-based short-term electricity price forecasting, in: Proceedings of the 6th International Conference on Advances in Power System Control, Operation and Management, Hong Kong, 2003, pp. 348–353.

![](/api/attachments/D88GM5V7/fulltext/images/78ff26f0070e5f56debbe1c00bbfe733a98ca279a421fce151ba61007fff6a34.jpg)

Chi-Jie Lu is an associate professor in the Department of Industrial Management at Chien Hsin University of Science and Technology (formerly Ching Yun University), Taiwan.. He got his Ph.D. in Industrial Engineering and Management from Yuan-Ze University. Taiwan, in 2005. His research and teaching interests are in the area of data pattern recognition, time series forecasting, statistical process control, and machine vision and inspection. He has published articles in various journals, including Pattern Recognition, Decision Support Systems, Image and Vision Computing, International Journal of Production Economics, International Journal of Production Research and Computational Statistics and Data Analysis

![](/api/attachments/D88GM5V7/fulltext/images/959f253504a2c25f9b2cc4999e57ca81c8b1f5b42f4b2136f367be7c8cf996d5.jpg)

Tian-Shyug Lee is a professor and Dean of College Management at Fu-Jen Catholic University. He is also currently the President of the International Association of Jesuit Business Schools (IAJBS). He got his Ph.D. in Operations Research and Industrial Engineering from the University of Texas at Austin. His research and teaching interests are in the area of applied statistics and probability, application of arti<sup>fi</sup>cial intelligence and data mining. He has published articles in various journals, including Computational Statistics and Data Analysis, Decision Support Systems, Digestive and Liver Disease, Expert Systems with Applications, International Journal of Systems Science International Journal of Fuzzy Systems, Journal of Human Resource and Adult Learning, Journal of Intelligent Manufacturing, Probability in the Engineering and Informational Sciences, and Obesity Surgery.

![](/api/attachments/D88GM5V7/fulltext/images/2d21ebe969842736c5d3e35ea1c679d20e17bc22886264960a859b49d73ffef5.jpg)

Chia-Mei Lian is the Vice President at Hon Yu Technology Corporation in Taiwan. She has over 17 years experience in IT Chain Store Planning and Management. She is also currently working towards the Ph.D. degree in Business Administration at Fu-Jen University, Taipei, Taiwan. Her research interests include Data Mining, Retailing Management Mastering Strategy and Supply Chain Management
