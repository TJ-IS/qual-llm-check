---
otero_id: 21653
otero_key: "6WFG3XWX"
title: "A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights"
authors: "R.J. Kuo; K.C. Xue"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00067-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights

R.J. Kuo <sup>a,)</sup>, K.C. Xue <sup>b</sup>

<sup>a</sup> Department of Industrial Engineering, National Taipei UniÕersity of Technology, Taipei, 10643, Taiwan 1 Graduate School of Management Science, I-Shou UniÕersity, Kaohsiung County, 840, Taiwan

Accepted 19 October 1998

## Abstract

Sales forecasting plays a very prominent role in business strategy. Numerous investigations addressing this problem have generally employed statistical methods, such as regression or autoregressive and moving average ARMA . However, salesŽ . forecasting is very complicated owing to influence by internal and external environments. Recently, artificial neural networks ANNs have also been applied in sales forecasting since their promising performances in the areas of control andŽ . pattern recognition. However, further improvement is still necessary since unique circumstances, e.g., promotion, cause a sudden change in the sales pattern. Thus, this study utilizes fuzzy logic a proposed fuzzy neural network FNN for the sakeŽ . of learning fuzzy IF–THEN rules obtained from the marketing experts with respect to promotion. The result from FNN is further integrated with the forecast from ANN using the time series data and the promotion length through the other ANN. Model evaluation results indicate that the proposed system can more accurately perform than the conventional statistical method and single ANN. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Sales forecasting; Artificial neural networks; Fuzzy neural networks

## 1. Introduction

To enhance the commercial competitive advantage in a constantly fluctuating environment, an organization’s management must make the right decision in time depending on the information at hand. However, the decision lead time ranges from several years to several hours based on the types of business. Thus, making an accurate decision in time plays a prominent role.

Intuitively, historical data can provide a feasible estimate through the forecasting models. Therefore, if the marketing department can estimate the sales quantity for the next period, the materials department can then effectively control the inventory to achieve just-in-time JIT . In addition, the production department can make Ž . the scheduling and arrange the facility utilization. Such an action may cause the production cost to decrease. Therefore, obtaining an accurate forecast most likely appears to be critical. Statistical methods, such as regression model and ARMA, have been the candidates for decision makers. However, these methods are only efficient for data which are seasonal or cyclical. If the data are influenced by the special case, like promotion, they are not feasible. Even artificial neural networks ANNs are better than the conventional statistical methodsŽ . <sup>w</sup> <sup>x</sup> 1,5,13,16 have been recently employed, the problem still arises. These research do put the promotion into consideration. Nonetheless, it is treated as an easy way, like one input of the ANN. Thus, this study first attempts to propose a fuzzy neural network FNN which is able to learn the IF–THEN rules obtained from theŽ . marketing experts with respect to the promotion. Though FNN concept and learning algorithm have first been presented by Lin and Lee 19 , yet it is only for the real inputs and real outputs. The FNN proposed in this study is not only able to learn the ‘fuzzy’ IF–THEN rules or fuzzy inputs and outputs , but also posses the fuzzyŽ . weights. The main reason to propose such FNN is that the promotion effect on sales is always very vague, or fuzzy.

However, having the promotion effect on sales is not enough. It is also necessary to provide the forecast of the sales. Therefore, this paper also aims to develop an intelligent sales forecasting. The sales forecasting system consists of four parts: 1 data collection, 2 general pattern model ANN , 3 special pattern model FNN ,Ž . Ž . Ž . Ž . Ž . and 4 decision integration ANN . To evaluate the proposed system, the actual data provided by the well Ž . Ž . known convenience store CVS company in Taiwan are used, while the promotion effect is obtained byŽ . surveying the experts in the retailing. According to these results, the proposed system performs more accurately than the conventional statistical method and single ANN, particularly when the promotion is conducted.

The rest of this paper is organized as follows. Section 2 provides some necessary background information while the proposed system is discussed in Section 3. Section 4 presents the simulation results of FNN, while the evaluation results are summarized in Section 5. Discussion and concluding remarks are finally made in Sections 6 and 7, respectively.

## 2. Background

In this section, sales forecasting systems and applications of artificial neural networks in sales forecasting are briefly reviewed. In addition, fuzzy neural networks are also discussed in the following.

## 2.1. Artificial neural networks in sales forecasting

Sales forecasting always plays a prominent role in a decision support system. Obtaining effective sales forecasting in advance can help the decision maker calculate production and materials costs, even determine the sale price 18 . This will result in a lower inventory level and achieve the objective of just-in-time. Regarding<sup>w</sup> <sup>x</sup> conventional sales forecasting methods 6,8,23 , most of them used either factors or time series data to <sup>w</sup> <sup>x</sup> determine the forecast. However, the relationship between the factors or the past time series data independent Ž variables and the sales dependent variable is always quite complicated. Obtaining results through the above . Ž . mentioned approaches is quite difficult. Therefore, various decision makers prefer using their own intuition, instead of model-based approaches i.e., time series or regression models . However, a model-free approach,Ž . ANN, is applied in the area of forecasting recently owing to its adequate performance in control and pattern recognition.

Artificial neural network ANN is a system derived through models of neurophysiology. In general, itŽ . consists of a collection of simple nonlinear computing elements whose inputs and outputs are tied together to form a network. Many studies have attempted to apply ANN to time-series forecasting. However, their conclusions are often contradictory. Some studies concluded that ANNs are better than conventional methods <sup>w x</sup> <sup>w x</sup> <sup>w x</sup> 26 , while others reached an opposite conclusion 25 . Weigen et al. 26 introduced the ‘eight-elimination’ backpropagation learning procedure to effectively deal with the overfitting problem, and applied it to sunspots and an exchange rate time series. Tang et al. 25 compared the ANN and Box–Jenkins models, using<sup>w</sup> <sup>x</sup> international airline passenger traffic, domestic car sales and foreign car sales in the USA. They concluded that the Box–Jenkins models outperformed the ANN models in short-term forecasting. On the other hand, the ANN models outperformed the Box–Jenkins in long term forecasting.

Chakraborty et al. 5 presented an ANN approach to multivariate time-series analysis. They accurately<sup>w</sup> <sup>x</sup> predicted the flour prices in three cities in the USA. According to their results, the ANN approach is a leading contender among statistical modeling approaches.

Lachtermacher and Fuller 16 developed a calibrated ANN model. The model used Box–Jenkins methods to<sup>w</sup> <sup>x</sup> identify the ‘lag components’ of the data, that should be used as input variables. Also, it employed a heuristics to suggest the number of hidden units needed in structuring the model. In examining the stationary series, they observed the calibrated ANN models have only a slightly better overall performance than the conventional time-series methods used in the benchmark. In the case of a non-stationary series, the calibrated ANN models outperformed the ARMA model for three of the four series, and almost as well as the ARMA in the fourth series. The above survey indicates that ANN is more appropriate for the time series data. Ansuj et al. 2 compared the time series model with interventions and ANN model in analyzing the behavior of sales in a medium size enterprise. The results showed that ANN model is more accurate. Kumar et al. 13 found that<sup>w</sup> <sup>x</sup> ANN does quite well compared to logistic regression in predicting a dichotomous choice in the presence of several independent variables. However, only considering some series data may result in a worse forecast. Including both the time series data and factors in the forecasting model seems to be preferable.

Recently, Bigus 3 used promotion, time of year, end of month flag, and weekly sales as inputs for the ANN <sup>w</sup> <sup>x</sup> in order to forecast the weekly demand. The results seem very promising. Agrawal and Schorling 1 also have <sup>w</sup> <sup>x</sup> shown that ANN is able to predict brand shares quite well even when price promotions, feature, and display are present in the data set.

## 2.2. Fuzzy neural networks

An ANN, which is employed for recognition purposes, generally lacks the ability to be developed for a given task within a reasonable time. On the other hand, fuzzy modeling 17,27 , which is applied to fuse the decisions from the different variables, requires an approach to learn from experience i.e., data collected in advance .Ž . ANNs, fuzzy logic, and genetic systems constitute the three independent research fields regarding sixth generation systems SGS . ANNs and the fuzzy model have been used in many application areas 17,22 , eachŽ . <sup>w</sup> <sup>x</sup> pairing its own advantages and disadvantages. Therefore, how to combine these two approaches successfully, ANNs and fuzzy modeling, has become a relevant concern of further studies.

Two major parts have recently received much interest: 1 Fuse ANN and fuzzy logic, and 2 Integrate ANNŽ . Ž . and fuzzy logic. In the first one, the traditional fuzzy system mentioned above is based on experts’ knowledge. However, it is not very objective. Besides, acquiring robust knowledge and finding available human experts are extremely difficult. Now, ANN’s learning algorithm has been applied to enhance the performance of a fuzzy system and demonstrated to be an innovative approach. Also, fuzzy if–then rules were generated and adjusted by learning methods using numerical data. Lin and Lee 19 and Lin and Lu 20 proposed the so-called Neural-Network-Based Fuzzy Logic Control System NN-FLCS . They introduced the low-level learning powerŽ . of neural networks in the fuzzy logic system and provided high-level human-understandable meaning to the normal connectionist architecture. Also, Kuo and Cohen 14,15 introduced a feedforward ANN into fuzzy<sup>w</sup> <sup>x</sup> inference represented by the Takagi–Sugeno model.

The above mentioned FNNs are only appropriate for numerical data. However, the experts’ knowledge is always fuzzy type. Thus, some researchers have attempted to address this problem. Ishibuchi et al. 9,10<sup>w</sup> <sup>x</sup> proposed learning methods of neural networks to utilize not only numerical data but also expert knowledge represented by fuzzy if–then rules. Lin 21 also presented a FNN, capable of handling both the fuzzy inputs and<sup>w</sup> <sup>x</sup> outputs. Meanwhile, Buckley and Hayashi 4 surveyed recent results on learning algorithms and applications<sup>w</sup> <sup>x</sup> for FNNs. Furthermore, Buckley introduced several methods in the EBP learning algorithms.

## 3. Methodology

The above section has emphasized the relevance of sales forecasting as well as some necessary background information. Though the research, like Refs. 1,3 , have put the promotion effect on the sales into consideration,<sup>w</sup> <sup>x</sup> yet it is still straightforward instead of sophisticated. It is necessary to develop a more robust approach to handle the promotion effect on the sales and then input it to the ANN. The proposed system is discussed in more detail in the following.

The proposed intelligent forecasting system consists of 1 data collection, 2 general pattern model ANN ,Ž . Ž . Ž . Ž . Ž . Ž . Ž . 3 special pattern model FNN , and 4 decision integration ANN . Fig. 1 shows the proposed system architecture. Basically, the system determines the forecasted product and the factors affecting the sales first. Thereafter, the general pattern of the sales is forecasted by an ANN while FNN considers the effect on the sales if the promotion is conducted. Finally, the decisions from these two networks and time effect are integrated through the other ANN. Each part is thoroughly discussed in the following subsections.

## 3.1. ANN architecture

In the first part, i.e., ANN , the feedforward ANN with error backpropagation EBP learning algorithm isŽ . Ž . employed. Since one-hidden-layer ANN has been applied in many domains, this research only consider a one-hidden-layer network instead of a two-hidden-layer network. ANN’s input layer with some neurons represents the previous sales data, say period t<sup>y</sup>p to period t<sup>y</sup>1. The hidden layer with some neurons is connected with the output layer with one single neuron which represents the sales for period t. The input neurons use $y = f ( x ) = x$ Ž . no change in input and all the other neurons generally have the sigmoidal function $y = f ( x ) = ( 1 + \exp ( - x ) ) ^ { - 1 }$ . The objective is to minimize cost function defined as

![](/api/attachments/6WFG3XWX/fulltext/images/5665eb2b28722858f68bb627a9f998533b7db885db154d37f4de6c63d41c43d4.jpg)  
Fig. 1. The architecture of the proposed forecasting system.

$$
E = \frac {1}{2} \sum_ {p} \left(T _ {p} - O _ {p}\right) ^ {2}.\tag{1}
$$

Therefore, from the above setup and required data, the ANN can learn the relationship between the sales at period t and previous sales from periods t <sup>y</sup> 1 to $t - p$

## 3.2. FNN architecture

In the first part, ANN can provide us sales without promotion effects. However, if the promotion is running, then ANN’s forecast will be inaccurate. Thus, this section discusses how to use FNN to effectively handle the circumstance of promotion by means of FNN. Since the FNN architecture is based on the fuzzy logic which possesses both the precondition and consequence, the precondition variables represent the effective factors while the sales represents the consequence variable. First, the data and if–then rules are obtained through the fuzzy Delphi method. After this procedure, the collected data can be applied to train the proposed FNN. The structure of FNN presented in this study is similar to 9 . The main difference is that the network employs the asymmetric <sup>w</sup> <sup>x</sup> bell shape instead of triangular fuzzy weights. In the following, the two components, fuzzy Delphi and FNN, are discussed in more detail.

## 3.2.1. Fuzzy Delphi

The Delphi method was first developed by Dalkey 28 in RAND. This approach has been widely applied in<sup>w</sup> <sup>x</sup> many management areas, e.g., forecasting, public policy analysis, or project planning 7,11 . However, the<sup>w</sup> <sup>x</sup> conventional Delphi method cannot converge very well. Besides, high survey frequencies always result in high costs. Thus, Ishikawa 29 utilized fuzzy sets theory in the Delphi method to resolve the above shortcomings. <sup>w</sup> <sup>x</sup> However, the method proposed by Ishikawa is inappropriate for this research. Therefore, the procedures of the modified fuzzy Delphi method for this research are as follows.

Ž .a Collect all the possible factors which may affect the sales and make the sorting, grouping in order to formulate the first questionnaire. In this questionnaire, all the factors are ‘separate’ and survey results are the FNN inputs.

Ž . Ž . b Select one event from each group or dimension to formulate an if–then rule in order to form the second questionnaire which is a set of if–then rules.

Ž .c Fuzzify the returned second questionnaires from the senior managers and determine the pessimistic index, optimistic index and average index. The formulations are as follows:

Ž . Ž . 1 Pessimistic Minimum index

$$
l = \frac {l _ {1} + l _ {2} + \dots + l _ {n}}{n}\tag{2}
$$

where $l _ { i }$ is the pessimistic index of the ith expert and n is the number of the experts.

Ž . Ž . 2 Optimistic Maximum index

$$
u = \frac {u _ {1} + u _ {2} + \ldots + u _ {n}}{n}\tag{3}
$$

where $u _ { i }$ is the optimistic index of the ith expert.

Ž . Ž . 3 Average most appropriate index

$$
m = \left(m _ {1} \times m _ {2} \times \dots \times m _ {n}\right) ^ {1 / n}
$$

For each interval $( l _ { i } , \ u _ { i } ) _ { \cdot }$ , calculate the mid point, $m _ { i } = ( l _ { i } + u _ { i } ) / 2$ and then find

Ž . 4

Thereafter, the fuzzy number $A = \left( \mu , \ \sigma ^ { \mathrm { R } } , \ \sigma ^ { \mathrm { L } } \right)$ , which represents the mean, right width, and left width, respectively, for an asymmetric bell shaped function, can be determined through the above indices:

$$
\sigma^ {\mathrm{R}} = \frac {l - \mu}{3}\tag{5}
$$

$$
\sigma^ {\mathrm{L}} = \frac {u - \mu}{3}\tag{6}
$$

Ž . d Formulate the third questionnaire with the above indices and make the survey.

Ž .e Repeat the procedure c.

Ž .f Employ dissemblance index rule 12 to examine the second and third questionnaire fuzzy numbers. <sup>w</sup> <sup>x</sup> Restated, the dissemblance index rule determines whether the membership functions have converged or not. If not, continue the next questionnaire until converging. Otherwise, results of the third questionnaire are the FNN output. The distance between two fuzzy numbers Ž A and $\overline { { B } } )$ is

$$
\begin{array}{l} \delta (\overline {{A}}, \overline {{B}}) = \int_ {\alpha = 0} \delta (\overline {{A}} [ \alpha ], \overline {{B}} [ \alpha ]) \mathrm{d} \alpha = \frac {1}{2} (\beta_ {2} - \beta_ {1}) \int_ {\alpha = 0} \left[ \left(| \overline {{A}} [ \alpha ] ^ {\mathrm{L}} - \overline {{B}} [ \alpha ] ^ {\mathrm{L}} |\right) + \left(| \overline {{A}} [ \alpha ] ^ {\mathrm{U}} - \overline {{B}} [ \alpha ] ^ {\mathrm{U}} |\right) \right] \mathrm{d} \alpha \end{array}\tag{7}
$$

where $\beta _ { 1 }$ and $\underline { { \beta } } _ { 2 }$ are given any convenient values in order to surround both $A [ \alpha ] = 0$ and $B [ \alpha ] = 0 ( \mathrm { F i g } . 2 )$ Basically, $\delta ( \overline { { A } } , \overline { { B } } )$ is in the interval 0,1 .<sup>w</sup> <sup>x</sup>

## 3.2.2. FNN with asymmetric bell shaped fuzzy weights

The above subsection has determined the shape for each membership function. However, most FNNs can only handle the actual real input and output except Refs. 9,21 . Thus, this component intends to modify<sup>w</sup> <sup>x</sup> Ishibuchi’s work 9 . In Ishibuchi’s work, the input, weight, and output fuzzy numbers are symmetric triangular. <sup>w</sup> <sup>x</sup> However, this assumption is not similar to a human being’s way of thinking. Thus, this paper replaces the triangular fuzzy numbers with asymmetric Gaussian functions since it can speed up the convergence. The input–output relation of the proposed FNN is discussed next, however, the operations of fuzzy numbers are presented first.

3.2.2.1. Operations of fuzzy numbers. Before describing the FNN architecture, fuzzy numbers and fuzzy number operations are defined by the extension principle. In the proposed algorithm, real numbers and fuzzy numbers are denoted by the lowercase letters $( \boldsymbol { \mathrm { e . g . } } , \boldsymbol { a } , \boldsymbol { b } , \dots )$ and a bar placed over uppercase letters $( \mathrm { e . g . , ~ } \bar { A } , \overline { { B } } , \dots ) .$ respectively.

![](/api/attachments/6WFG3XWX/fulltext/images/0212fc312d1d30da28ba756ac886bb5d818e204dc3de9dd9c1ff8ae02e86eb17.jpg)  
Fig. 2. The concept of dissemblance index of two fuzzy numbers.

![](/api/attachments/6WFG3XWX/fulltext/images/682a954332566e939a8a00c811027e60098a88f7139f9ff74ef0408dc141d317.jpg)  
Fig. 3. The FNN architecture.

Since input vectors, connection weights and output vectors of multi-layer feedforward neural networks are fuzzified in the proposed FNN, the addition, multiplication and nonlinear mapping of fuzzy numbers are necessary for defining the proposed FNN. Thus, they are defined as follows:

$$
\bar {Z} (z) = \bar {X} (x) + \bar {Y} (y) = \max \left\{\bar {X} (x) \wedge \bar {Y} (y) | z = x + y \right\};\tag{8}
$$

$$
\bar {Z} (z) = \bar {X} (x) \bar {Y} (y) = \max \left\{\bar {X} (x) \wedge \bar {Y} (y) | z = x y \right\};\tag{9}
$$

$$
\bar {Z} (z) = \max \left\{\overline {{\operatorname{Net}}} (x) | z = f (x) \right\},\tag{10}
$$

where $\overline { { { X } } } , \overline { { { Y } } } , \overline { { { Z } } }$ are fuzzy numbers, $\overline { { * } } ( . )$ denotes the membership function of each fuzzy number, <sup>n</sup> is the minimum operator, and $f ( x ) = ( 1 + \exp ( - x ) ) ^ { - }$ <sup>1</sup> is the activation function of hidden units and output units of the proposed FNN. The -cut of fuzzy number $\overbar { X }$ is defined as

$$
\bar {X} [ \alpha ] = \left\{x | \bar {X} (x) \geq \alpha , x \in R \right\} \text {   for   } 0 <   \alpha \leq 1,
$$

where X <sup>w</sup> <sup>x</sup> represents $\bar { X } [ \alpha ] = [ \bar { X } [ \alpha ] ^ { \mathrm { L } } , \bar { X } [ \alpha ] ^ { \mathrm { U } } ]$ and $\overline { { X } } [ \alpha ] ^ { \mathrm { L } }$ and $\overline { { X } } [ \alpha ] ^ { \mathrm { U } }$ are the lower boundary and the upper boundary of the -cut set ${ \overline { { X } } } [ \alpha ] .$ , respectively.

3.2.2.2. FNN learning algorithm. The proposed FNN learning algorithm is similar to EBP-type learning algorithm 24 . Before discussing the algorithm, some assumptions should be clarified as follows:<sup>w</sup> <sup>x</sup>

1. Fuzzify a three layer feedforward neural network with $n _ { \mathrm { I } }$ input units, $n _ { \mathrm { H } }$ hidden units, and $n _ { \mathrm { O } }$ output units Ži.e., input vectors, target vectors connection weights and thresholds are fuzzified ;.

2. The input vectors are non-negative fuzzy numbers;

3. These fuzzy numbers are asymmetric Gaussian shaped fuzzy numbers.

The input–output relation of the proposed FNN Fig. 3 is defined by the extension principle 9 and can beŽ . <sup>w</sup> <sup>x</sup> written as follows: Input layer:

$$
\overline {{O}} _ {p i} [ \alpha ] = \overline {{X}} _ {p i} [ \alpha ] i = 1, 2, \dots , n _ {\mathrm{I}},\tag{11}
$$

Hidden layer:

$$
\overline {{O}} _ {p h} [ \alpha ] = f \big (\overline {{\mathrm{Net}}} _ {p h} [ \alpha ] \big), h = 1, 2, \dots , n _ {\mathrm{H}},\tag{12}
$$

$$
\overline {{\operatorname{Net}}} _ {p h} [ \alpha ] = \sum_ {i = 1} ^ {n _ {\mathrm{I}}} \overline {{W}} _ {h i} [ \alpha ] \overline {{O}} _ {p i} [ \alpha ] + \overline {{\Theta}} _ {h} [ \alpha ],\tag{13}
$$

Output layer:

$$
\overline {{O}} _ {p k} [ \alpha ] = f \big (\overline {{\mathrm{Net}}} _ {p k} [ \alpha ] \big), k = 1, 2, \dots , n _ {\mathrm{O}},\tag{14}
$$

$$
\overline {{\mathrm{Net}}} _ {p k} [ \alpha ] = \sum_ {k = 1} ^ {n _ {\mathrm{O}}} \overline {{W}} _ {k h} [ \alpha ] \overline {{O}} _ {p h} [ \alpha ] + \overline {{\Theta}} _ {k} [ \alpha ].\tag{15}
$$

From Eqs. 11 – 15 , the Ž . Ž . -cut sets of the fuzzy output $\overline { { O } } _ { p k }$ are calculated from the fuzzy inputs, fuzzy weights, and fuzzy biases. If the -cut set of the fuzzy outputs $O _ { p k }$ is required, then the above relation can be rewritten as follows: Input layer:

$$
\overline {{O}} _ {p i} [ \alpha ] = \left[ \overline {{O}} _ {p i} [ \alpha ] ^ {\mathrm{L}}, \overline {{O}} _ {p i} [ \alpha ] ^ {\mathrm{U}} \right] = \left[ \overline {{X}} _ {p i} [ \alpha ] ^ {\mathrm{L}}, \overline {{X}} _ {p i} [ \alpha ] ^ {\mathrm{U}} \right], i = 1, 2, \ldots , n _ {\mathrm{I}},\tag{16}
$$

Hidden layer:

$$
\begin{array}{r l} \overline {{O}} _ {p h} [ \alpha ] & = \left[ \overline {{O}} _ {p h} [ \alpha ] ^ {\mathrm{L}}, \overline {{O}} _ {p h} [ \alpha ] ^ {\mathrm{U}} \right] \\ & = \left[ f \big (\overline {{\mathrm{Net}}} _ {p h} [ \alpha ] ^ {\mathrm{L}} \big), f \big (\overline {{\mathrm{Net}}} _ {p h} [ \alpha ] ^ {\mathrm{U}} \big) \right], h = 1, 2, \ldots , n _ {\mathrm{H}}, \end{array}\tag{17}
$$

For both the lower and upper fuzzy

$$
\left\{ \begin{array}{l}\overline{\mathrm{Net}}_{ph}[\alpha ]^{\mathrm{L}} = \sum_{\substack{i = 1\\ \overline{W}_{hi}[\alpha ]^{L}\geq 0}}^{n_{\mathrm{I}}} \overline{W}_{hi}[\alpha ]^{\mathrm{L}}\overline{O}_{pi}[\alpha ]^{\mathrm{L}} + \sum_{\substack{i = 1\\ \overline{W}_{hi}[\alpha ]^{\mathrm{L}} <   0}}^{n_{\mathrm{I}}} \overline{W}_{hi}[\alpha ]^{\mathrm{L}}\overline{O}_{pi}[\alpha ]^{\mathrm{U}} + \overline{\Theta}_{h}[\alpha ]^{\mathrm{L}},\\ \overline{\mathrm{Net}}_{ph}[\alpha ]^{\mathrm{U}} = \sum_{\substack{i = 1\\ \overline{W}_{hi}[\alpha ]^{\mathrm{U}}\geq 0}}^{n_{\mathrm{I}}} \overline{W}_{hi}[\alpha ]^{\mathrm{U}}\overline{O}_{pi}[\alpha ]^{\mathrm{U}} + \sum_{\substack{i = 1\\ \overline{W}_{hi}[\alpha ]^{\mathrm{U}} <   0}}^{n_{\mathrm{I}}} \overline{W}_{hi}[\alpha ]^{\mathrm{U}}\overline{O}_{pi}[\alpha ]^{\mathrm{L}} + \overline{\Theta}_{h}[\alpha ]^{\mathrm{U}}, \end{array} \right.\tag{18}
$$

Output layer:

$$
\begin{array}{r l} \overline {{O}} _ {p k} [ \alpha ] & = [ \overline {{O}} _ {p k} [ \alpha ] ^ {\mathrm{L}}, \overline {{O}} _ {p k} [ \alpha ] ^ {\mathrm{U}} ] \\ & = [ f (\overline {{\mathrm{Net}}} _ {p k} [ \alpha ] ^ {\mathrm{L}}), f (\overline {{\mathrm{Net}}} _ {p k} [ \alpha ] ^ {\mathrm{U}}) ], k = 1, 2 \dots , n _ {\mathrm{O}}, \end{array}\tag{19}
$$

$$
\left\{ \begin{array}{l}\overline{\mathrm{Net}}_{pk}[\alpha ]^{\mathrm{L}} = \sum_{\substack{k = 1\\ \overline{W}_{kh}[\alpha ]^{\mathrm{L}}\geq 0}}^{n_{\mathrm{O}}} \overline{W}_{kh}[\alpha ]^{\mathrm{L}}\overline{O}_{ph}[\alpha ]^{\mathrm{L}} + \sum_{\substack{k = 1\\ \overline{W}_{kh}[\alpha ]^{\mathrm{L}} <   0}}^{n_{\mathrm{O}}} \overline{W}_{kh}[\alpha ]^{\mathrm{L}}\overline{O}_{ph}[\alpha ]^{\mathrm{U}} + \overline{\Theta}_{k}[\alpha ]^{\mathrm{L}}\\ \\ \overline{\mathrm{Net}}_{pk}[\alpha ]^{\mathrm{U}} = \sum_{\substack{k = 1\\ \overline{W}_{kh}[\alpha ]^{\mathrm{U}}\geq 0}}^{n_{\mathrm{O}}} \overline{W}_{kh}[\alpha ]^{\mathrm{U}}\overline{O}_{ph}[\alpha ]^{\mathrm{U}} + \sum_{\substack{k = 1\\ \overline{W}_{kh}[\alpha ]^{\mathrm{U}} <   0}}^{n_{\mathrm{O}}} \overline{W}_{kh}[\alpha ]^{\mathrm{U}}\overline{O}_{ph}[\alpha ]^{\mathrm{L}} + \overline{\Theta}_{k}[\alpha ]^{\mathrm{U}}, \end{array} \right.\tag{20}
$$

The objective is to minimize the cost function defined as:

$$
E _ {p} = \sum_ {\alpha} \sum_ {k = 1} ^ {n _ {\mathrm{O}}} \alpha \Big (E _ {k (\alpha)} ^ {\mathrm{L}} + E _ {k (\alpha)} ^ {\mathrm{U}} \Big) = \sum_ {\alpha} E _ {p (\alpha)},\tag{21}
$$

where

$$
\begin{array}{l} E _ {p (\alpha)} = \sum_ {k = 1} ^ {n _ {\mathrm{O}}} \alpha \left(E _ {k (\alpha)} ^ {\mathrm{L}} + E _ {k (\alpha)} ^ {\mathrm{U}}\right), \\ \left\{ \begin{array}{l} E _ {k (\alpha)} ^ {\mathrm{L}} = \frac {1}{2} \left(\bar {T} _ {p k} [ \alpha ] ^ {\mathrm{L}} - \bar {O} _ {p k} [ \alpha ] ^ {\mathrm{L}}\right) ^ {2} \\ E _ {k (\alpha)} ^ {\mathrm{U}} = \frac {1}{2} \left(\bar {T} _ {p k} [ \alpha ] ^ {\mathrm{U}} - \bar {O} _ {p k} [ \alpha ] ^ {\mathrm{U}}\right) ^ {2}, \end{array} \right. \end{array}\tag{22}
$$

Ž . 23

Where $E _ { k ( \alpha ) } ^ { \mathrm { L } }$ and $E _ { k ( \alpha ) } ^ { \mathrm { U } }$ can be viewed as the squared errors for the lower boundaries and the upper boundaries of the -cut sets of a fuzzy weight. Other -cut sets of a fuzzy weight are independently modified to reduce $E _ { p ( \alpha ) } .$ Otherwise, the fuzzy numbers after modifications are distorted. Therefore, each fuzzy weight is updated in a similar but still different way from the approach of Ishibuchi 9 . That is, in the proposed FNN, the membership functions are asymmetric Gaussian functions i.e., a general shape which is represented as:Ž .

$$
\bar {A} (x) = \left\{ \begin{array}{l l} \exp \left(- \frac {1}{2} \left(\frac {x - \mu}{\sigma^ {\mathrm{L}}}\right) ^ {2}\right), & x <   \mu \\ 1, & x = \mu \\ \exp \left(- \frac {1}{2} \left(\frac {x - \mu}{\sigma^ {\mathrm{R}}}\right) ^ {2}\right), & \text { otherwise } \end{array} \right.\tag{24}
$$

Thus, the asymmetric Gaussian fuzzy weights are specified by their three parameters i.e., center right width andŽ left width . The gradient search method is derived for each parameter. It is the amount of adjustment for each. parameter using the cost function $E _ { p ( \alpha ) }$ as follows:

$$
\begin{array}{l} \Delta \mu_ {k h} (t) = - \eta \frac {\partial E _ {p (\alpha)}}{\partial \mu_ {k h}} + \beta \Delta \mu_ {k h} (t - 1) \\ \left\{ \begin{array}{l} \Delta \sigma_ {k h} ^ {\mathrm{L}} (t) = - \eta \frac {\partial E _ {p (\alpha)}}{\partial \sigma_ {k h} ^ {\mathrm{L}}} + \beta \Delta \sigma_ {k h} ^ {\mathrm{L}} (t - 1) \\ \Delta \sigma_ {k h} ^ {\mathrm{R}} (t) = - \eta \frac {\partial E _ {p (\alpha)}}{\partial \sigma_ {k h} ^ {\mathrm{R}}} + \beta \Delta \sigma_ {k h} ^ {\mathrm{R}} (t - 1) \end{array} \right. \end{array}\tag{25}
$$

Ž . 26

Lastly, assume that m patterns $( { \mathrm { i . e . , ~ } } \bar { X } _ { p i } , \bar { T } _ { p i } ) , I = 1 , 2 , \ldots m )$ , of fuzzy input vectors are given as training data, and also assume that S values of -cut are used for the learning of the proposed FNN. In the case, the learning algorithm of the proposed FNN can be written as follows:

## Learning algorithm

Step 1: Initialize the fuzzy weights and the fuzzy biases.

Step 2: Repeat step 3 for $s = 1 , 2 , \ldots , S .$

Step 3: Repeat the following procedures for $p = 1 , 2 , \ldots , m .$

Ž . 1 Forward calculation: Calculate the -cut set of the fuzzy output vector $O _ { p i }$ corresponding to the fuzzy input vector $X _ { p i }$

Ž . 2 Back-propagation: Adjust the fuzzy weights and the fuzzy biases using the cost function $E _ { p s }$

Step 4: If a performed stopping condition is not satisfied, go to step 2.

## 3.3. Decision integration

From the above two parts, ANN provides the sales without any special promotion while the promotion effect is forecasted by the FNN. To yield the final result, for the sales which consider both the general pattern and the promotional effect, only integrating the results from the ANN and FNN is inadequate in that the promotional effect during the promotion interval may differ. Thus, this part will employ the other ANN to combine the ANN result, the FNN result, and the time effect. Since the result from FNN is a fuzzy number, the -cut, <sup>s</sup>0.6, 0.8 and 1, is applied in order to get the real numbers from the FNN. Thus, there are five input nodes which represent the promotion effect.

![](/api/attachments/6WFG3XWX/fulltext/images/4b75364bfcad95d4dc5809b1ce143db6ca42d87347e055f0ff40b9188c56afe9.jpg)  
Fig. 4. The fuzzy input and output data of example one for training.

## 4. Simulation

Section 3 has shown the proposed fuzzy neural network with asymmetric fuzzy inputs, weights, and outputs theoretically. In order to verify its feasibility, this section employs four examples to simulate the FNN. Examples one to three are all one-input–one-output problems, while example four is a two-input–one-output problem. The simulation results can be referenced for the real life problem which will be presented in the next section.

The FNN model is written in C language being implemented in an IBM compatible PC. All the required parameters are set up in the following:

1. The number of hidden nodes: Examples 1–3:3; Example 4:3–6.

2. -cut levels: <sup>s</sup> 0.1, 0.3, 0.5, 0.7, and 0.9.

![](/api/attachments/6WFG3XWX/fulltext/images/2883832575110550b2f65f9e47e132f5560f878e5469dd1094d2f4ad5b43e5ac.jpg)  
Fig. 5. The testing results of training samples for example one.

![](/api/attachments/6WFG3XWX/fulltext/images/9ecaf9855a8a7ff39bb4c97ac249d8b3a29841b8e9f93b0757ae36e258f90219.jpg)  
Fig. 6. The testing results of two testing samples.

3. The number of training epochs: depending on the training condition.

4. Training rate: $\eta = 0 . 3 .$

5. Momentum: $\beta = 0 . 6 .$

## 4.1. Example 1

The first example is a linear mapping. Three training samples, $( \overline { { X } } _ { p } , \overline { { T } } _ { p } )$ where ${ \overline { { X } } } _ { p }$ is the fuzzy input, $\overline { { T } } _ { p }$ is the fuzzy desired output and training sample number $p = 1 , 2 , 3$ , are developed in the two-dimensional space. The relationship of fuzzy inputs and fuzzy outputs are shown in Fig. 4 as $\alpha = 0 . 1 , 0 . 3 , 0 . 5 , 0 . 7 .$ , and 0.9.

The FNN has one input node which is connected to three hidden nodes which are further connected to one output node. The training will halt if the training epochs reach 20,000. Fig. 5 illustrates the training samples results after training, while the computational results of two testing samples are presented in Fig. 6. It is obvious that the proposed FNN can learn the fuzzy relation between fuzzy inputs and fuzzy outputs accurately. The network takes 3000 training epochs to converge.

## 4.2. Example 2

Example two simulates the non-linear relation of sine function. Six training pairs, $( \overline { { X } } _ { p } , \ \overline { { T } } _ { p } )$ where $p = 1$ $2 , \ldots , 6 ,$ in two-dimensional space are used. The graphical relation of fuzzy inputs and outputs as is equal to 0.1, 0.3, 0.5, 0.7 and 0.9 is shown in Fig. 7. The network structure is also 1–3–1. The stop criteria is as training epochs reach 90,000. But the network can converge very well after 5000 training epochs. Fig. 8 illustrates the testing results for training pairs. The computational results show that the FNN can learn the nonlinear relationship compared with Fig. 7. The MSE values curve during training is shown in Fig. 9.

![](/api/attachments/6WFG3XWX/fulltext/images/54188319dc354bf996ed2bbeb2c311474be20233d8ece5c570b1f691e414ac5b.jpg)  
Fig. 7. The fuzzy input and output data of example two for training.

![](/api/attachments/6WFG3XWX/fulltext/images/7ba4918bebb3c221dcee61cb963a992e0ef9b378368329f013e4d297d5ae539b.jpg)  
Fig. 8. The results of testing pairs for example two.

## 4.3. Example 3

This example will show the competency of FNN to learn the fuzzy IF–THEN rules. Meanwhile, the trained FNN can infer the new rules which are not covered in the trained fuzzy IF–THEN rule-base. First, assume that there are three known fuzzy IF–THEN rules used to control the engine speed with respect to different degrees of temperature. They are as follows:

Rule 1: IF temperature Ž . Ž . Ž . Ž . X is very low VL , THEN the engine speed Y is stop SS .

Rule 2: IF temperature Ž . Ž . Ž . Ž . X is medium M , THEN the engine speed Y is medium M .

Rule 3: IF temperature Ž . Ž . Ž . Ž . X is very high VH , THEN the engine speed Y is very quick VQ .

The corresponding membership functions of every linguistic term, such as very low, medium, and very high, are illustrated in Figs. 10 and 11. The network structure is also 1–3–1. If new linguistic terms, like low and hot, are inputted to the FNN, the network can infer the new fuzzy outputs automatically. These two inference rules are:

IF temperature Ž . Ž . Ž . Ž . X is low L , THEN the engine speed Y is slow S .

IF temperature Ž . Ž . Ž . Ž . X is high H , THEN the engine speed Y is quick Q .

Figs. 12 and 13 show the membership function for the input and output linguistic terms after inference.

![](/api/attachments/6WFG3XWX/fulltext/images/28020610ad87cf4d9059269d81ee453a94b7e93fcd11dadbaef2fd7a8282a0af.jpg)  
Fig. 9. The mean square error values during training.

![](/api/attachments/6WFG3XWX/fulltext/images/88093ce59c5e298789df595b44dcddd7d64357aa4a2141f035490b8529d2f360.jpg)  
Fig. 10. Membership functions for three linguistic terms very high, medium and very low of temperature.Ž .

![](/api/attachments/6WFG3XWX/fulltext/images/30910c5bedbf46b29837a7222b80426627f67755e534b064dba245b976b275d1.jpg)  
Fig. 11. Membership functions of three linguistic terms stop, medium and very quick of engine speed. Ž .

![](/api/attachments/6WFG3XWX/fulltext/images/ebc24956393e57815686bc5728668fe4219008de1baf12d5002ac729c0fb7581.jpg)  
Fig. 12. Membership functions of five linguistic terms very high, high, medium, low and very low of temperature. Ž .

![](/api/attachments/6WFG3XWX/fulltext/images/6fc7027a1d5532e192db31e98dacb4b9549a36e722f58d6ae09a0cf306722f69.jpg)  
Fig. 13. Membership functions of five linguistic terms stop, slow, medium, quick, and very quick of engine speed. Ž .

Table 1  
Example four’s fuzzy IF–THEN rules table

<table><tr><td rowspan="2"></td><td>L</td><td>M</td><td></td><td>S</td><td></td><td>S</td></tr><tr><td>ML</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5"> $X_1$ </td><td>M</td><td>ML</td><td></td><td>S</td><td></td><td>S</td></tr><tr><td>MS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>S</td><td>L</td><td></td><td>ML</td><td></td><td>M</td></tr><tr><td></td><td>S</td><td>MS</td><td>M</td><td>ML</td><td>L</td></tr><tr><td></td><td></td><td></td><td> $X_2$ </td><td></td><td></td></tr></table>

## 4.4. Example 4

The above examples have successfully applied the FNN for inferring the new fuzzy IF–THEN rules. Thus, this example will try to learn fuzzy IF–THEN rules with two precondition variables temperature and humidityŽ . and one consequence variable engine speed through FNN. These rules are:Ž .

Rule 1. IF $X _ { 1 }$ is small and $X _ { 2 }$ is small THEN Y is large.

Rule 2. IF $X _ { 1 }$ is small and $X _ { 2 }$ is medium THEN Y is large.

Rule 3. IF $X _ { 1 }$ is small and $X _ { 2 }$ is large THEN Y is large.

Rule 4. IF $X _ { 1 }$ is medium and $X _ { 2 }$ is small THEN Y is small.

Rule 5. IF $X _ { 1 }$ is medium and $X _ { 2 }$ is medium THEN Y is large.

Rule 6. IF $X _ { 1 }$ is medium and $X _ { 2 }$ is small THEN Y is small.

Rule 7. IF $X _ { 1 }$ is large and $X _ { 2 }$ is small THEN Y is medium.

Rule 8. IF $X _ { 1 }$ is large and $X _ { 2 }$ is medium THEN Y is small.

Rule 9. IF $X _ { 1 }$ is large and $X _ { 2 }$ is large THEN Y is small.

$X _ { 1 }$ and $X _ { 2 }$ are temperature and humidity, respectively, and Y is the engine speed. The definition of linguistic terms, small, medium, and large are similar to that used in the example 3. The fuzzy rules table for these 9 fuzzy IF–THEN rules are shown in Table 1. Totally, there are nine training pairs for FNN. In order to determine the best network topology, different hidden node numbers ranging from 3 to 6 are implemented. Similarly, different training rates, 0.2, 0.5, and 0.8, and different momentum terms, 0.2, 0.5, and 0.8, are also tested. The simulation results as the number of hidden nodes is equal to 4 are shown in Table 2. The main goal of trained FNN is to infer two more linguistic terms for each precondition variable with respect to the existing three linguistic terms.

Table 2  
The computational results of different combinations of training rate and momentum when the number of hidden nodes is 4

<table><tr><td colspan="2">The number of hidden nodes: 4</td><td> $\beta = 0.2$ </td><td> $\beta = 0.5$ </td><td> $\beta = 0.8$ </td></tr><tr><td rowspan="3"> $\eta = 0.2$ </td><td>Training MSE</td><td>0.085048</td><td>0.01746</td><td>*0.011703</td></tr><tr><td>Training Epochs</td><td>120,000</td><td>84,000</td><td>106,000</td></tr><tr><td>Testing MSE</td><td>#0.078179</td><td>0.023068</td><td>0.017301</td></tr><tr><td rowspan="3"> $\eta = 0.5$ </td><td>Training MSE</td><td>0.102442</td><td>*0.011935</td><td>0.024824</td></tr><tr><td>Training Epochs</td><td>60,000</td><td>110,000</td><td>50,000</td></tr><tr><td>Testing MSE</td><td>#0.085513</td><td>**0.017294</td><td>0.023551</td></tr><tr><td rowspan="3"> $\eta = 0.8$ </td><td>Training MSE</td><td>0.145062</td><td>*0.012960</td><td>0.205448</td></tr><tr><td>Training Epochs</td><td>50,000</td><td>40,000</td><td>40,000</td></tr><tr><td>Testing MSE</td><td>#0.132292</td><td>0.018019</td><td>#0.178341</td></tr></table>

Table 3  
Example four’s complete fuzzy IF–THEN rules table after training

<table><tr><td rowspan="2"></td><td>L</td><td>M</td><td>MS</td><td>S</td><td>S</td><td>S</td></tr><tr><td>ML</td><td>ML</td><td>MS</td><td>S</td><td>S</td><td>S</td></tr><tr><td rowspan="5"> $X_1$ </td><td>M</td><td>ML</td><td>MS</td><td>S</td><td>S</td><td>S</td></tr><tr><td>MS</td><td>L</td><td>ML</td><td>MS</td><td>MS</td><td>MS</td></tr><tr><td>S</td><td>L</td><td>L</td><td>ML</td><td>ML</td><td>M</td></tr><tr><td></td><td>S</td><td>MS</td><td>M</td><td>ML</td><td>L</td></tr><tr><td></td><td></td><td></td><td> $X_2$ </td><td></td><td></td></tr></table>

Thus, totally there are twenty-five fuzzy IF–THEN rules after inference. The new added fuzzy rules are presented in Table 3.

## 5. Model evaluation results

The above sections have presented the proposed forecasting system and FNN’s feasibility numerically. Further, a real life problem is used to verify the proposed system’s practicality. In addition, the proposed system is also compared with the other method, single ANN and ARMA. Both the procedures and results are sequentially shown in the following subsections.

## 5.1. Data collection

The data are provided by a locally well-known CVS company. Since the forecasting pattern is divided into two categories, general pattern and special pattern, the data collection is also comprised of two parts.

## 5.1.1. Time series data

The company provides the daily sales of 500 c.c. papaya milk. The total number of the data points is 379 as shown in Fig. 14. The sudden increase of sales indicates that the promotion is being conducted. Totally there are five times of promotion. The time period lasts from $1 / 1 / 1 9 9 5$ to $1 / 1 4 / 1 9 9 6$ . For the purpose of testing, these 376 data points are further divided into training samples and testing samples. The front one has 334 data points while the latter one has 45 data points.

## 5.1.2. Expert questionnaire

To survey all the possible factors of promotion and their effects on the sales, this paper employs fuzzy Delphi method. The questionnaire’s setup is based on the company’s practical requirements. Thus, some factors are included. The procedures based on the modified fuzzy Delphi method presented in the above section are as follows.

![](/api/attachments/6WFG3XWX/fulltext/images/707e07846d6ef22888cdfb9f64f4907beb9f5873b91f69f4c68cfca7296b5e3d.jpg)  
Fig. 14. The time series data.

Table 4  
The fuzzy number of each event for the third questionnaire

<table><tr><td>Factors</td><td>Events</td><td>Average (μ)</td><td> $\sigma^R = (l - \mu)/(3)$ </td><td> $\sigma^L = (u - \mu)/(3)$ </td></tr><tr><td rowspan="4">Promotion methods</td><td>10 dollars discount</td><td>0.85</td><td>0.0310</td><td>0.0338</td></tr><tr><td>5 dollars discount</td><td>0.48</td><td>0.0257</td><td>0.0378</td></tr><tr><td>3 dollars discount</td><td>0.21</td><td>0.0206</td><td>0.0454</td></tr><tr><td>Buy two get one free</td><td>0.70</td><td>0.0266</td><td>0.0369</td></tr><tr><td rowspan="7">Advertising media</td><td>At night on TV</td><td>0.77</td><td>0.0345</td><td>0.0387</td></tr><tr><td>At noon on TV</td><td>0.32</td><td>0.0159</td><td>0.0523</td></tr><tr><td>In the evening on TV</td><td>0.36</td><td>0.0223</td><td>0.0524</td></tr><tr><td>Radio</td><td>0.44</td><td>0.0126</td><td>0.0534</td></tr><tr><td>Newspaper</td><td>0.43</td><td>0.0213</td><td>0.0492</td></tr><tr><td>POP notice</td><td>0.69</td><td>0.0255</td><td>0.0325</td></tr><tr><td>Poster</td><td>0.65</td><td>0.0290</td><td>0.0365</td></tr><tr><td rowspan="4">Promotion length</td><td>15 days</td><td>0.54</td><td>0.0221</td><td>0.0432</td></tr><tr><td>20 days</td><td>0.58</td><td>0.0343</td><td>0.0477</td></tr><tr><td>30 days</td><td>0.68</td><td>0.0227</td><td>0.0413</td></tr><tr><td>45 days</td><td>0.62</td><td>0.0245</td><td>0.0442</td></tr><tr><td rowspan="2">Others</td><td>Related products without promotion</td><td>0.73</td><td>0.0259</td><td>0.0348</td></tr><tr><td>Related products with promotion</td><td>0.48</td><td>0.0177</td><td>0.0343</td></tr></table>

5.1.2.1. Factors determination. A large number of factors can generally affect the sales. However, a different product has different characteristics. After discussing with the company’s senior managers, all the factors are divided into three dimensions. The first dimension represents the methods of promotion, while the types of advertising media are presented in the second dimension. The third dimension represents the competitors’ actions. Though some factors are not included in the questionnaire, yet it is for the company’s practical requirements.

5.1.2.2. First questionnaire formulation. After the events have been determined in the above procedure, these events can be used to formulate the first questionnaire. Provide the questionnaires to the senior managers for survey. Calculate the membership function for each event. Results obtained from the first questionnaire can provide the degree of importance for each event and are the FNN inputs.

![](/api/attachments/6WFG3XWX/fulltext/images/d679ec63f1e851cc655b160fedee6650404ad3a1ce063ca28f1480f91cc4ea05.jpg)  
Fig. 15. Four fuzzy numbers.

Table 5  
Dissemblance index rule testing results for separate events

<table><tr><td>Factors</td><td>Events</td><td> $\delta (\overline{A},\overline{B})$ </td><td> $\delta = 0.06$ </td><td> $\delta = 0.08$ </td></tr><tr><td rowspan="4">Promotion methods</td><td>10 dollars discount</td><td>0.010842</td><td>Accept</td><td>Accept</td></tr><tr><td>5 dollars discount</td><td>0.012683</td><td>Accept</td><td>Accept</td></tr><tr><td>3 dollars discount</td><td>0.055033</td><td>Accept</td><td>Accept</td></tr><tr><td>Buy two get one free</td><td>0.021496</td><td>Accept</td><td>Accept</td></tr><tr><td rowspan="7">Advertising media</td><td>at night on TV</td><td>0.008304</td><td>Accept</td><td>Accept</td></tr><tr><td>at noon on TV</td><td>0.072394</td><td>Reject</td><td>Accept</td></tr><tr><td>In the evening on TV</td><td>0.036122</td><td>Accept</td><td>Accept</td></tr><tr><td>Radio</td><td>0.020922</td><td>Accept</td><td>Accept</td></tr><tr><td>Newspaper</td><td>0.039173</td><td>Accept</td><td>Accept</td></tr><tr><td>POP notice</td><td>0.017868</td><td>Accept</td><td>Accept</td></tr><tr><td>Poster</td><td>0.011316</td><td>Accept</td><td>Accept</td></tr><tr><td rowspan="4">Promotion length</td><td>15 days</td><td>0.032976</td><td>Accept</td><td>Accept</td></tr><tr><td>20 days</td><td>0.015148</td><td>Accept</td><td>Accept</td></tr><tr><td>30 days</td><td>0.006339</td><td>Accept</td><td>Accept</td></tr><tr><td>45 days</td><td>0.013148</td><td>Accept</td><td>Accept</td></tr><tr><td rowspan="2">Others</td><td>Related products without promotion</td><td>0.031801</td><td>Accept</td><td>Accept</td></tr><tr><td>Related products with promotion</td><td>0.02144</td><td>Accept</td><td>Accept</td></tr></table>

5.1.2.3. Second questionnaire formulation. Since the questionnaire attempts to provide training data for FNN, the events of all three dimensions can be used to formulate the second questionnaire which is a set of IF–THEN rules. Totally, there are 56 4Ž .<sup>=</sup>7<sup>=</sup>2 if–then rules. For example, the first rule of the questionnaire is

IF discount is 10 dollars and

advertising time is from 8 pm to 9 pm on TV and

no related product is under promotion

THEN the effect on sales ranges from \_\_ to \_\_.

After the survey of this questionnaire, all the required information, i.e., pessimistic, optimistic, and average indexes, is calculated on the basis of Section 3, methodology.

5.1.2.4. Third questionnaire surÕey. Formulate the third questionnaire which includes the pessimistic, optimistic and average indexes. Continue the next third survey and calculate all the information again. Table 4 presents Ž . the fuzzy number of each event. However, directly using these fuzzy numbers is time-consuming and complicated. Therefore, all the similar events should be combined together. Finally, only four linguistic terms are used: bad, medium, good and very good. Fig. 15 presents the fuzzy numbers of these four linguistic terms.

5.1.2.5. Similarity testing. To determine the necessity of the next survey, the dissemblance index rule should be utilized. The single event results and combinational events results are summarized in Tables 5 and 6, respectively. This finding suggests that the membership function of each linguistic term has converged. The next survey does not need to be performed. Therefore, this knowledge base will be applied to train the FNN and represents the FNN outputs.

Table 6  
The dissemblance index rule test results for combinational events

<table><tr><td>Sales linguistic terms</td><td> $\delta (\overline{A},\overline{B})$ </td><td> $\delta = 0.06$ </td><td> $\delta = 0.08$ </td></tr><tr><td>Poor</td><td>0.018939</td><td>Accept</td><td>Accept</td></tr><tr><td>Medium</td><td>0.004207</td><td>Accept</td><td>Accept</td></tr><tr><td>Good</td><td>0.013379</td><td>Accept</td><td>Accept</td></tr><tr><td>Very good</td><td>0.005568</td><td>Accept</td><td>Accept</td></tr></table>

Table 7  
The testing alternatives for general pattern model

<table><tr><td>Pattern number</td><td>Network structure (I×H×O)</td><td>MSE( $10^{-3}$ )</td><td>Percentage increase (%)</td></tr><tr><td>0</td><td>AR(3)</td><td>2.21</td><td>**</td></tr><tr><td>1</td><td> $2 \times 2 \times 1$ </td><td>2.36</td><td>6.79</td></tr><tr><td>2</td><td> $2 \times 2 \times 2 \times 1$ </td><td>2.36</td><td>6.78</td></tr><tr><td>3</td><td> $5 \times 5 \times 1$ </td><td>2.22</td><td>0.45</td></tr><tr><td>4</td><td> $5 \times 5 \times 5 \times 1$ </td><td>2.23</td><td>0.76</td></tr><tr><td>5</td><td> $7 \times 7 \times 1$ </td><td>2.20</td><td>-0.45</td></tr><tr><td>6</td><td> $7 \times 7 \times 7 \times 1$ </td><td>2.20</td><td>-0.52</td></tr></table>

## 5.2. General pattern model ANN( )

Only 379 data points are used for training. However, in general pattern model ANN , the data points underŽ . promotion are not included in the training samples. Thus, after subtracting the number of promotion data points from 379, the number of training samples is 288. This study will test different alternatives, say network topology. Basically, both one and two hidden layers are tested. In addition, different combinations of training rate and momentum terms are also verified. The network will halt if the training epochs reach 50,000. All of these data points are normalized in 0,1 . The computational results indicate that the network structure<sup>w</sup> <sup>x</sup> $7 \times 7 \times 1$ has the best performance as the training rate and momentum are equal to 0.3 and 0.8, respectively. In addition, statistical method, ARMA, is also used to model the above time series data. AR 3 has the MSE valueŽ . $2 . 2 1 \times 1 0 ^ { - 3 }$ . This indicates that the time series model, ARMA, and ANN have the similar results as the time series data has no special promotion. The summarized results are shown in Table 7.

## 5.3. Special pattern model FNN( )

Data collection demonstrated that the questionnaire should have 56 IF–THEN rules. After using unsimilarity index rule to test the similarity, the result indicates that both the event ‘newspaper’ A and event ‘radio’ B areŽ . Ž . quite similar in that $\delta ( \overline { { A } } , \overline { { B } } )$ is equal to 0.017966, i.e., being smaller than , 0.08. Thus, combining the two events results in the total number of rules is 48 $( 4 \times 6 \times 2 )$ .

The setup of proposed FNN with asymmetric bell shaped fuzzy weights is similar to the general ANN. The network structure consists of three input nodes, i.e., dimensions, which are connected to six hidden nodes, i.e., numbers which are connected to one output node. The network will not stop learning until 30,000 epochs. The -level sets are 0.2, 0.4, 0.6, 0.8, and 1.0. Different training rates and momentum terms may yield different results. Testing results as shown in Table 8 indicate that the lowest MSE value is $8 . 1 5 \times 1 0 ^ { - 3 }$ as training rate and momentum are 0.1 and 0.5, respectively. Finally, this network becomes integrated with general pattern model, ANN, in the next part, decision integration.

Table 8  
MSEs $( \times 1 0 ^ { - 3 } )$ for different FNN setup

<table><tr><td rowspan="2">Momentum</td><td colspan="3">Training rate</td></tr><tr><td>0.1</td><td>0.3</td><td>0.5</td></tr><tr><td>0.1</td><td>8.31</td><td>9.10</td><td>8.46</td></tr><tr><td>0.5</td><td>8.15</td><td>8.52</td><td>8.63</td></tr><tr><td>0.8</td><td>13.85</td><td>8.96</td><td>11.30</td></tr></table>

Table 9  
MSEs for different models

<table><tr><td>Forecasting model</td><td>MSE( $\times 10^{-3}$ )</td><td>Percentage increase of MSE</td></tr><tr><td>Integration ANN</td><td>3.37</td><td>**</td></tr><tr><td>ARMA(2,5)</td><td>4.88</td><td>46.13</td></tr><tr><td>ANN1( $5 \times 5 \times 1$ )</td><td>4.95</td><td>48.35</td></tr><tr><td>ANN2( $5 \times 5 \times 5 \times 1$ )</td><td>5.50</td><td>49.80</td></tr><tr><td>ANN3( $10 \times 10 \times 1$ )</td><td>4.76</td><td>44.77</td></tr><tr><td>ANN4( $10 \times 10 \times 10 \times 1$ )</td><td>4.77</td><td>43.10</td></tr></table>

Table 10  
The forecasting results

<table><tr><td>Forecasting model</td><td>MSE( $\times 10^{-3}$ )</td><td>Percentage increase of MSE</td></tr><tr><td>Integration ANN</td><td>3.10</td><td>**</td></tr><tr><td>Short term memory ANN</td><td>6.61</td><td>113.63</td></tr><tr><td>Long term memory ANN</td><td>6.78</td><td>118.99</td></tr></table>

## 5.4. Decision integration model ANN ( )

The above two parts can provide results obtained from the general pattern and special pattern promotionŽ . models. This part attempts to integrate the above two models. Basically, the inputs originate from the following three sources:

a. General pattern model provides one input node which is the general pattern trend;

b. A special pattern model provides five input nodes which are from FNN as  is equal to 0.6, 0.8 and 1.0, respectively; and

c. The promotion length implies one input node.

Therefore, the total number of integration ANN input nodes is seven. Similarly, different network structures and different combinations of the training rate and momentum are tested. The training limit is 50,000 epochs. The computational results show that the network structure $7 \times 7 \times 1$ has the lowest MSE value $3 . 3 7 \times 1 0 ^ { - 3 }$ as shown in Table 9. In order to make the comparison, the 379 training samples with promotion data points are applied to train the single ANN and determine the ARMA model. Table 9 shows that ARMA 2, 5 provide MSEŽ . value $4 . 8 8 \times 1 0 ^ { - 3 }$ . Different network structures are also tested. Table 9 presents the best result for each structure with respect to different combinations of training rate and momentum.

So far, the paper has presented the ‘training’ results. In the following, three models, i.e., integration ANN, short term memory ANN1, and long term memory ANN3, are used to forecast the 45 data points with one time of promotion. The related results are listed in Table 10 and Fig. 16.

![](/api/attachments/6WFG3XWX/fulltext/images/a1145a85df9afef27489ee7e6bbe7e3355ed9e35fc9d4f1e66ae084e453e081a.jpg)  
Fig. 16. The integration ANN forecasting result.

## 6. Discussion

The above section has presented evaluation results based on data accumulated from a CVS company. The factor effects on the sales seem to be subjective since the data are provided by either the senior managers or experts. However, the number of experts is twenty, implying that the subjective factors can be eliminated to a minimum. In particular the fuzzy Delphi method is employed; the above consideration can also be reduced. Among all types of promotion methods, the event ‘10 dollars discount’ is the most effective event while the worst event is ‘3 dollars discount.’ Regarding the types of the advertising media, the event ‘advising time from 8 to 9 pm on TV’ affects sales the most. Undoubtedly, since 8 to 9 pm is the so-called ‘golden interval,’ the promotion of the related product yields a negative effect.

Notably, the pessimistic, optimistic, and average indexes are put in the third questionnaire. The reason is that providing the others experts’ opinions may accelerate the converge of the fuzzy numbers. In the third questionnaire, thirteen fuzzy numbers are combined into four fuzzy numbers. The main reason is to reduce the computational complexity. The forecast’s precision may not differ significantly. Moreover, the third questionnaire also used the unsimilarity index rule to determine the necessity for the next survey. Table 5 indicates that all the pairing fuzzy numbers are similar as is equal to 0.06 or 0.08. Even by viewing the separate events result, only the event ‘advertising at noon on TV’ is not similar as is 0.06. Therefore, using these data orŽ fuzzy numbers to train the FNN is obviously objective. Basically, this is a pilot study to indicate the sources of. the fuzzy inputs and fuzzy outputs. Both Ishibuchi et al. 9 and Lin 21 , i.e., two representative papers <sup>w x</sup> <sup>w</sup> <sup>x</sup> considering the fuzzy inputs and outputs, did not provide a means to find the fuzzy inputs and outputs for training.

In the second part of the proposed system, six alternatives, from short-term to long term memories, are tested. The MSE values indicate that the network with long-term memory seven outperforms the network withŽ . short-term memory two or five . However, continuously increasing the length of memory does not yield aŽ . better result. The reason is that the unnecessary information may mislead the network’s memory. Regarding the number of hidden layers, the results indicate either one or two hidden layers can provide a similar forecast. Owing to computational considerations, one hidden layer is more feasible. Moreover, it is the reason to select $7 \times 7 \times 1$ network instead of $7 \times 7 \times 7 \times 1$ network to integrate with FNN.

Table 9 indicates that Integration ANN outperforms all other forecasting methods, e.g., ARMA 2, 5 andŽ . single ANN. The reason is that the integration ANN prioritizes the promotion effect on the sales pattern. Even with the forecasting result, the integration ANN is also second to none. Interestingly, the short and long term ANNs always have one day delay. It is because this kind of ANN only depends on the previous data. However, the integration ANN poses the promotion effect in the network.

Regarding the ARMA model and ANN model, the results are dependent. Basically, if the ANN can be well set up, it can provide the better result.

Meanwhile, the main objective of this study is to propose a new approach for the sales forecasting, especially the FNN to learn the fuzzy IF–THEN rules. Therefore, the other kinds of statistical modes are not implemented. The proposed system seems very complicated, yet if the system can be computerized, it is very suitable for the practical applications.

## 7. Conclusions

This study has developed a forecasting system based on FNN to solve the sales forecasting problem under promotion. Though directly using a single ANN to model the sales pattern has been shown to be better than the conventional statistical methods, it still need further improvement. Integrating the ANN and the FNN can provide more reliable forecast. In addition, the fuzzy Delphi method was applied to collect the fuzzy inputs and outputs for the FNN. To our knowledge, this is the first paper to consider this existing but unresolved problem. In the future, the authors would like to further improve the FNN, like the pruning of the fuzzy weights and training speed of the network. From a marketing perspective, more factors, which may yield a more precise result, can be included, though the CVS company does not use them regularly.

## 8. Nomenclature

$p$ the sample number $X _ { p }$ the input vector of sample $p$ $\dot { T _ { p } }$ the target vector of sample $p$ $O _ { p k }$ the output of kth output node $O _ { p h }$ the output of hth hidden node $\bar { W } _ { i h }$ the connection weight from ith input node to hth hidden node $W _ { h k }$ the connection weight from hth hidden node to kth output node $\mathrm { N e t } _ { p k }$ the net internal activity level of kth output node $\mathrm { N e t } _ { p h }$ the net internal activity level of hth hidden node $\Theta _ { j }$ the bias of jth output node $E _ { p }$ the cost function for sample $p$ $E _ { p s }$ the cost function of s-level’s -cut set for sample p $E _ { p k s } ^ { \mathrm { L } }$ the cost function of the lower boundary for s-level’s -cut set of sample p $E _ { p k s } ^ { \mathrm { L } }$ the cost function of the upper boundary for s-level’s -cut set of sample $p$ ${ \underline { { \overline { { X } } } } _ { p } }$ the fuzzy input for sample $p$ $O _ { p }$ the fuzzy output for sample $p$ $\underline { { \overline { { W } } } } _ { i h } , \underline { { \overline { { W } } } } _ { h k }$ the fuzzy weights $\Theta _ { h } , \Theta _ { k }$ the fuzzy biases $\eta$ the learning rate $\alpha$ the momentum term $\overline { { * } } [ \alpha ] ^ { \mathrm { L } } , \overline { { * } } [ \alpha ] ^ { \mathrm { U } }$ the lower limit and the upper limit of the -cut of fuzzy number

## Acknowledgements

The authors would like to thank the National Science Council, Republic of China for partially supporting this manuscript under Contract No. NSC 87-2416-H-327-003-E10. Mr. L.C. Shie, who is the manager of the company providing the data, is also appreciated for providing the daily sales data and his valuable discussion regarding chain store promotion. The authors also thank the anonymous reviewers for their helpful comments.

## References

<sup>w</sup> <sup>x</sup>1 D. Agrawal, C. Schorling, Market share forecasting: an empirical comparison of artificial neural networks and multinomial logit model, Journal of Retailing 72 4 1997 383–408.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 A.P. Ansuj, M.E. Camargo, R. Radharamanan, D.G. Petry, Sales forecasting using time series and neural networks, Computers and Industrial Engineering 31 1Ž . Ž . <sup>r</sup>2 1996 421–424.

<sup>w</sup> <sup>x</sup> 3 J.P. Bigus, Data mining with neural networks: solving business problems-from application development to decision support, McGraw-Hill International Edition, 1996.

<sup>w</sup> <sup>x</sup> 4 J.J. Buckley, Y. Hayashi, Fuzzy neural networks: a survey, Fuzzy Sets and Systems 66 1994 1–13.Ž .

<sup>w</sup> <sup>x</sup> 5 K. Chakraborty, K. Mehrotra, C.K. Mohan, Forecasting the behavior of multivariate time series using neural networks, Neural Networks 5 6 1992 961–970.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 C.W. Chase, Ways to improve sales forecasts, Journal of Business Forecasting 12 3 1993 15–17.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 N.C. Kalkey, O. Helmer, An experimental application of the Delphi method to the use of experts, Management Science 9 1963 Ž . 458–467.

<sup>w</sup> <sup>x</sup> 8 M.M. Florance, M.S. Sawicz, Positioning sales forecasting for better results, Journal of Business Forecasting 12 4 1993 27–28.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 H. Ishibuchi, K. Kwon, H. Tanaka, A learning algorithm of fuzzy neural networks with triangular fuzzy weights, Fuzzy Sets and Systems 71 1995 277–293. Ž .

<sup>w</sup> <sup>x</sup> 10 H. Ishibuchi, H. Okada, R. Fujioka, H. Tanaka, Neural networks that learn from fuzzy if–then rules, IEEE Transactions on Fuzzy System 1 2 1993 85–97.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 J. Jarrett, Business Forecasting Metheds, Basil Blackwell, 1991.

12 A. Kaufmann, M.M. Gupta, Introduction to Fuzzy Arithmetic, North-Holland, Amsterdam, 1985.

<sup>w</sup> <sup>x</sup> 13 A. Kumar, V.R. Rao, H. Soni, An empirical comparison of neural network and logistic regression models, Marketing Letters 6 4Ž . Ž . 1995 251–263.

14 R.J. Kuo, Multi-sensor integration for intelligent control of machining through artificial neural networks and fuzzy modeling, Ph.D. Thesis, Department of Industrial Engineering, Pennsylvania State University, 1994.

<sup>w</sup> <sup>x</sup> 15 R.J. Kuo, P.H. Cohen, Manufacturing process control through integration of neural networks and fuzzy model, Fuzzy Sets and Systems Ž . Ž . 1998 to appear .

<sup>w</sup> <sup>x</sup> 16 G. Lachtermacher, J.D. Fuller, Backpropagation in time-series forecasting, Journal of Forecasting 14 1995 381–393.Ž .

<sup>w</sup> <sup>x</sup> 17 C.C. Lee, Fuzzy logic in control systems: fuzzy logic controller-parts I and II, IEEE Transactions on Systems, Man, and Cybernetics 20 Ž . Ž .2 1990 404–435.

<sup>w</sup> <sup>x</sup> 18 G.S. LeVee, The key to understanding the forecasting process, Journal of Business Forecasting, Vol. 11, Issue 4, Winter 1992–1993Ž . 12–16.

<sup>w</sup> <sup>x</sup> 19 C.T. Lin, C.S.G. Lee, Neural-network-based fuzzy logic control and decision system, IEEE Transactions Computer C 40 12 1991 Ž . Ž . 1320–1336.

<sup>w</sup> <sup>x</sup> 20 C.T. Lin, Y.C. Lu, A neural fuzzy system with linguistic teaching signals, IEEE Transactions on Fuzzy Systems 3 2 1995 169–189. Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 C.T. Lin, A neural fuzzy control system with structure and parameter learning, Fuzzy Sets and Systems 70 1995 183–212.Ž .

<sup>w</sup> <sup>x</sup> 22 R.P. Lippmann, An introduction to computing with neural nets, IEEE ASSP Magazine, April 1987 4–22. Ž .

<sup>w</sup> <sup>x</sup> 23 G.G. Meyer, Marketing research and sales forecasting at Schlegel corporation, Journal of Business Forecasting 12 2 1993 22–23. Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 D.E. Rumelhart, J.L. McClelland, The PDP Research Group, Parallel Distributed Processing, Vol. 1, MIT Press, Cambridge, MA, 1986.

<sup>w</sup> <sup>x</sup> 25 Z. Tang, C. Almeida, P.A. Fishwick, Times series forecasting using neural networks vs. Box–Jenkins methodology, Simulations, Simulations Councils, Nov. 1991 303–310.Ž .

<sup>w</sup> <sup>x</sup> 26 A.S. Weigen, D.E. Rumelhart, B.A. Huberman, Generalization by weight-elimination with application to forecasting, Advances in Neural Information Processing Systems 3 1991 875–882.Ž .

27 L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision processes, IEEE Transactions on Systems, Man, and Cybernetics 3 1 1973 28–44.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 N.C. Dalkey, O. Helmer, An experimental application of the Delphi method to the use of experts, Management Science, Vol. 9, April Ž . 1963 458–467.

<sup>w</sup> <sup>x</sup> 29 A. Ishikawa, M. Amagasa, G. Tomiqawa, R. Tatsuta, H. Mieno, The mix-min Delphi method and fuzzy Delphi method via fuzzy integration, Fuzzy Sets and Systems 55 1993 241–253.Ž .

![](/api/attachments/6WFG3XWX/fulltext/images/8ccb06bd7272c72565fb7d72e47d5704ae9cafc6c2ad47fedc2429732cc3b408.jpg)  
R.J. Kuo received the MS degree in Industrial and Manufacturing Systems Engineering from Iowa State University, Ames, IA, in 1990 and the Ph.D. degree in Industrial and Management Systems Engineering from the Pennsylvania State University, University Park, PA, in 1994. Currently, he is an Associate Professor in the Department of Industrial Engineering, National Taipei University of Technology, Taiwan, ROC. His research interests include architecture issues of neural networks, fuzzy logic, and genetic algorithms, and their applications in process control and forecasting.

![](/api/attachments/6WFG3XWX/fulltext/images/5d6cef53f453c816fdc3f8ed5f5cb8f6411be00b1bb6d48dabdddb34ee98d2c5.jpg)  
K.C. Xue received the MS degree in management science from the I-Shou University, Taiwan, in 1996. Currently, he is the production control engineer of T.Y.C. Brother Industrial, Taiwan, ROC. His research interests include neural networks, fuzzy logic, and their applications in marketing and forecasting.
