---
otero_id: 13364
otero_key: "Z6SKPFG2"
title: "Fast fashion sales forecasting with limited data and time"
authors: "Tsan-Ming Choi; Chi-Leung Hui; Na Liu; Sau-Fun Ng; Yong Yu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Tsan-Ming Choi ⁎, Chi-Leung Hui, Na Liu, Sau-Fun Ng, Yong Yu

Business Division, Institute of Textiles and Clothing, Faculty of Applied Science and Textiles, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

a r t i c l e i n f o

Article history: Received 16 May 2012 Received in revised form 10 October 2013 Accepted 26 October 2013 Available online 2 November 2013

Keywords: Fashion forecasting Fast fashion Quick forecasting Time series Intelligent forecasting

## a b s t r a c t

Fast fashion is a commonly adopted strategy in fashion retailing. Under fast fashion, operational decisions have to be made with a tight schedule and the corresponding forecasting method has to be completed with very limited data within a limited time duration. Motivated by fast fashion business practices, in this paper, an intelligent forecasting algorithm, which combines tools such as the extreme learning machine and the grey model, is developed Our real data analysis demonstrates that this newly derived algorithm can generate reasonably good forecasting under the given time and data constraints. Further analysis with an arti<sup>fi</sup>cial dataset shows that the proposed algorithm performs especially well when either (i) the demand trend slope is large, or (ii) the seasonal cycle's variance is large. These two features <sup>fi</sup>t the fast fashion demand pattern very well because the trend factor is signi<sup>fi</sup>cant and the seasonal cycle is usually highly variable in fast fashion. The results from this paper lay the foundation which can help to achieve real time sales forecasting for fast fashion operations in the future. Some managerial implications are also discussed.

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

Fast fashion is an industrial practice widely applied in fashion retailing. Its central idea is to offer a continuous stream of new merchandise to the market which re<sup>fl</sup>ects the latest fashion trend, and helps capture the hottest design that the market most prefers. For example, famous international fashion retail brands such as H&M, Top Shop, and Zara all are implementing fast fashion and Zara can even achieve the “two weeks magic” in which the whole product cycle from having the preliminary conceptual design to the <sup>fi</sup>nal product in the sales <sup>fl</sup>oor in just about two weeks [20]. In the literature, fast fashion has been a popular research topic over the past few years. For instance, Caro and Gallien [6] investigated, using an optimization approach, the fashion retailing assortment planning problem for fast fashion products. They derived a novel dynamic programming based inventory policy which could yield the optimal fast fashion product assortment. Later, Cachon and Swinney [5] and Caro and Gallien [7] considered fast fashion systems which had various different features. To be speci<sup>fi</sup>c, Caro and Gallien [7] explored the situation inspired by Zara's case and they took the assortment plan as an input and aimed at <sup>fi</sup>nding the optimal inventory allocation within the fast fashion supply chain network. Cachon and Swinney [5] conducted an analytical study with a focus on optimizing the fast fashion production systems with forward-looking strategic consumers. They proposed that the fast fashion system could offer a shortened lead time as well as an improved design to attract customers. Under their model, they developed important insights on how fast fashion systems could best operate. Notice that the above reviewed studies had indicated several bene<sup>fi</sup>ts and operational challenges associated with fast fashion. In particular, we can see that demand uncertainty is very high for fast fashion products (as it relates highly to the ever changing fashion trend and consumer preference) and the fast fashion companies have to make their inventory decisions based on forecasts with a very short lead time and hence a very tight schedule. As a result, fast fashion companies have to conduct sales forecasting for their products in a near real time basis (a very short lead time) and also with a very limited amount of data (because of the short selling season of the related demand data for forecasting).

Motivated by the above industrial practice in fast fashion, this paper explores the sales forecasting system for fast fashion by developing a novel algorithm, called the Fast Fashion Forecasting (3F) algorithm which can conduct forecasting with limited data within limited time. This hybrid algorithm combines two well-established arti<sup>fi</sup>cial intelligence (AI) methods, namely the extreme learning machine (ELM) and the grey model (GM). By using real data from the industry, we examine the performance of the proposed algorithm and <sup>fi</sup>nd that it can yield reasonable forecasting accuracy under the given very tight time schedule. We then conduct further analysis by employing some arti<sup>fi</sup>cial time series datasets and show that the proposed algorithm performs especially well when either (i) the trend slope is large, or (ii) the seasonal cycle's variance is large. We argue that these two features <sup>fi</sup>t the industrial observation on fast fashion sales very well because the trend factor is signi<sup>fi</sup>cant and the seasonal cycle is known to be highly variable. To the best of our knowledge, this paper is the <sup>fi</sup>rst to explore the problem of sales forecasting with limited data and limited time. This problem is signi<sup>fi</sup>cant because it is very practical and it captures the essential elements of the timely industrial topic of fast fashion business operations.

The rest of this paper is organized as follows. Section 2 presents a more detailed literature review and demonstrates clearly the literature positioning of this paper. Section 3 shows the proposed model and the algorithm. Section 4 reports the computational results of the proposed algorithm based on real data. Section 5 shows the results and <sup>fi</sup>ndings derived from further analysis with the arti<sup>fi</sup>cial datasets. Section 6 concludes the paper and discusses the managerial implications and future research directions.

## 2. Literature review

Sales forecasting is a very important task. It is especially important in the fast fashion industry<sup>1</sup> because of ever-changing fashion trends and super highly volatile demand pattern. In fast fashion, it is well-known that fashionable products generally have very short life-cycles (e.g., two weeks in Zara), and therefore for every product line or stock keeping unit (SKU), there are usually very few historical data points available for the company to conduct forecasting. Even worse, in order to have useful forecasting results with the use of most timely information, a fast fashion company must conduct forecasting within a very short time limit. As a consequence, forecasting fashion sales for the scenario with the above two features is a practical but very challenging issue. As reported in the literature, there are many analytical models which can be employed to complete the forecasting task. Some commonly adopted methods include statistical models [1,4] such as Auto Regression Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) [14], arti<sup>fi</sup>cial intelligence (AI) models such as Arti<sup>fi</sup>cial Neural Networks (ANN) [9,10,22,33,41], and some other scienti<sup>fi</sup>c methods such as wavelet analysis [44]. Different models have (i) different basic requirements on the amount of historical data to be used and (ii) different basic modeling assumptions. For instance, the ARIMA model assumes that there is a linearity relationship in the data while the ANN assumes non-linearity. These relationships are highly related to the property of the data. It hence poses a big challenge to the fast fashion company to select the right forecasting model if the given data is insuf<sup>fi</sup>cient.

At the same time, the speed of forecasting is also critical to real fast fashion operations. In the following, we review several existing methods for accomplishing quick time series forecasting. First, quick time series forecasting can be accomplished by classical statistical models. Since the forecasting models and algorithms are all given in closed-form, the corresponding forecasting scheme can be performed very quickly, only a few seconds. However, these statistical methods all require relatively restrictive conditions on the high degree of <sup>fi</sup>tness to the model assumptions for them to perform well. As a result, user knowledge will be needed in order to properly select and employ these statistical methods for forecasting fashion sales time series. However, this level of knowledge cannot be assumed for ordinary business managers in the fashion industry. Moreover, for the fast fashion retailers, the amount of SKUs can be huge. For example, the number of SKUs in a single shop could easily reach 10,000. If the fashion retailer would like to adopt the market-driven quick response [48] practice (such as the fast fashion inventory management concept in retailers of Zara and H&M), it has to conduct sales forecasting for every SKU in a very timely manner (e.g., all 10,000 units' forecasting has to be completed within an hour). This imposes a tremendous burden on both the computing system and the staff members, as well as requiring a very careful planning of the forecasting algorithm. In addition, since fashion sales time series usually exhibit a high degree of randomness, it is commonly argued that the pure statistical methods are insuf<sup>fi</sup>cient to yield good forecasting results. In light of the shortcomings of the pure statistical methods, recent literature proposed various AI methods.<sup>2</sup> However, compared to statistical methods, AI methods are much slower. For example, computational results showed that a simple ANN would take several minutes and ENN would take hours [2,27,40] to complete a simple fashion sales time series forecasting task. Recently, there were many new proposals of fast AI computation methods which included the development of the extreme learning machine (ELM) [27,39]. In fact, ELM is nothing more than a single-hidden layer feed-forward neural network. However, with its special features, ELM can learn faster than the conventional gradient-based learning methods. In addition to the popular ELM and its extensions (such as the Extended ELM denoted by EELM [39]), which is a method of running ELM repeatedly for many times, El-Bakry and Mastorakis [18] proposed a new model called HSNN which could yield fast forecasting by speeding up the prediction stage of the forecasting task. They applied a cross correlation method between the whole input data and the weights of neural networks in order to speed up the process. Although ELM and HSNN are all faster than the conventional ANN and ENN, a substantial amount of time is still needed in order for them to complete the forecasting task. In addition, they all require a certain amount of data in order to yield a reasonably good forecasting result.

In terms of forecasting with insuf<sup>fi</sup>cient historical data, the grey method (GM) has been known as a good candidate. For example, Hsu and Chen [23] employed the GM based algorithm to conduct forecasting on power demand with very few historical data, and they reported some promising results from their GM based algorithm. Hsu and Chen [23] applied the GM based model to establish a forecasting scheme for the integrated circuit industry and obtain encouraging prediction results. Yao et al. [45] proposed an improved GM based method and applied it for electricity demand forecasting. They found that under some important conditions that applied well to the electricity industry, their proposed new GM method performed very satisfactorily with a relatively limited amount of historical data. Other recent GM model related forecasting research includes [25,26,30,31]. Despite being known as a good tool for conducting forecasting with relatively few historical data, it was found that the GM based models were also relatively unreliable (compared to other methods). In particular, if the underlying data pattern is highly volatile and without obvious trend, the GM based methods were known to perform poorly [15,23].

Based on the above reviewed literature and discussions, on one hand, we know that in order to support fast fashion operations, there is a genuine need to develop a forecasting method which can achieve a reasonable level of accuracy within a very short time and under the constraint that only very few historical data points are available. On the other hand, the existing methods in the literature all have insuf<sup>fi</sup>- ciency in achieving this forecasting task because the reported methods are either fast but require enough data, or are capable of conducting forecasting with very few data but are known to be unreliable or not fast enough. This calls for new research ideas, e.g., based on hybrid methods which combine multiple methods together and try to employ the best quality of each one of them in accomplishing the forecasting task (see [38] for many recent developments in this domain on forecasting seasonal time series with computational intelligence). As a consequence, we develop in this paper the 3F algorithm and examine its performance by various analyses. To better illustrate the literature positioning of this paper, a detailed comparison between the 3F algorithm and the closely related literature is shown in Table 2.1.

Table 2.1  
Comparisons between the Fast Fashion Forecasting (3F) algorithm and other recently developed forecasting models

<table><tr><td>Papers</td><td>Data requirements</td><td>Forecasting speed</td><td>Stability</td><td>Application domain</td><td>Methods</td></tr><tr><td>[42]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Control loading problems</td><td>Fourier transform model</td></tr><tr><td>[2]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Fashion sales time series problems</td><td>ANN</td></tr><tr><td>[3]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Generic</td><td>Fuzzy model</td></tr><tr><td>[8]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Control loading problems</td><td>Hierarchical neural model</td></tr><tr><td>[29]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Advertisement</td><td>Hierarchical Bayes model</td></tr><tr><td>[32]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Finance</td><td>Wilcoxon ANN and Wilcoxon functional link ANN</td></tr><tr><td>[35]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Finance</td><td>Differential EMD</td></tr><tr><td>[37]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Network intrusion</td><td>Markov chain</td></tr><tr><td>[43]</td><td>Sufficiency is assumed</td><td>Slow</td><td>High</td><td>Finance</td><td>Genetic algorithm</td></tr><tr><td>[17]</td><td>Sufficiency is assumed</td><td>Moderate</td><td>High</td><td>Generic</td><td>Fuzzy c-means and neural networks</td></tr><tr><td>[34]</td><td>Sufficiency is assumed</td><td>Moderate</td><td>High</td><td>Finance</td><td>Bayesian kernel method</td></tr><tr><td>[19]</td><td>Sufficiency is assumed</td><td>Fast</td><td>Moderate</td><td>Control loading problems</td><td>Ensemble ANN</td></tr><tr><td>[16]</td><td>Sufficiency is assumed</td><td>Fast</td><td>High</td><td>Technology assessment problems</td><td>Fuzzy inference system</td></tr><tr><td>[28]</td><td>Sufficiency is assumed</td><td>Fast</td><td>High</td><td>Technology trend</td><td>Decision tree</td></tr><tr><td>[46]</td><td>Sufficiency is assumed</td><td>Fast</td><td>High</td><td>Fashion sales time series problems</td><td>Extreme learning machine</td></tr><tr><td>[25]</td><td>Sufficiency is NOT assumed</td><td>Moderate</td><td>Low</td><td>Integrated circuit output</td><td>Genetic algorithm based multivariable grey optimization model</td></tr><tr><td>[26]</td><td>Sufficiency is NOT assumed</td><td>Moderate</td><td>Low</td><td>Integrated circuit output</td><td>Grey model</td></tr><tr><td>[30]</td><td>Sufficiency is NOT assumed</td><td>Moderate</td><td>Low</td><td>Electricity</td><td>Grey model</td></tr><tr><td>This paper</td><td>Sufficiency is NOT assumed</td><td>Fast</td><td>Moderate</td><td>Fashion sales time series problems</td><td>Extended extreme learning machine, grey model</td></tr></table>

## 3. Methodology

In this section, we present the details of the data and review the related methods to be employed in developing the 3F algorithm.

## 3.1. The fast fashion sales data

The sales dataset from a knitwear fashion company adopting a fast fashion concept [13] is employed in this research. To be speci<sup>fi</sup>c, fourperiod real sales datasets<sup>3</sup> from the company were collected and used in the analysis. The products of this company are categorized into various types and there are several styles and colors for each product type. A part of the sales dataset is shown in Table 3.1 for different color codes.

## 3.2. Extended extreme learning machine

To develop the 3F algorithm, we consider the versatile and robust AI method known as extreme learning machine (ELM). Let us review its technical details as follows. First, ELM [27] refers to a machine learning mechanism for the single hidden layer feedforward neural network (SLFN). It is depicted in Fig. 3.1. It analytically determines the output weight matrix $\beta$ of the SLFN by randomly assigning the input weight matrix W.

If a SLFN with m hidden layer neurons can approximate n distinct samples (x ,a ) with a zero error, we will have:

$$
H \beta = A,\tag{1}
$$

where $\mathrm { H } = \{ h _ { i j } \} , i = 1 , 2 , . . . , n \mathrm { a n d } j = 1 , 2 , . . . , m ,$ is the hidden-layer output matrix, $h _ { i j }$ is the matrix of output weights which denotes the output of the jth hidden neuron with respect to $\mathbf { x } _ { i } , \beta = ( \beta _ { 1 } \beta _ { 2 } . . . . , \beta _ { M } )$ , and $A = ( a _ { 1 } , a _ { 2 } , . . . , a _ { \mathrm { N } } ) ^ { T }$ is the matrix of targets. Observe that one key feature of ELM is that the input weights and hidden biases are randomly generated instead of being tuned. As a result, the determination of the output weights is relatively simple and similar to <sup>fi</sup>nding the minimum norm least-square solution, denoted by $\beta ^ { * } ,$ , to any given linear system as shown in Eq. (2) below:

$$
\beta^ {*} = H ^ {- 1} A,\tag{2}
$$

where $H ^ { - 1 }$ is the generalized inverse of the matrix H. Notice that $\beta ^ { * }$ uniquely exists (see [39]).

While ELM has the well-known advantages of being able to avoid many notorious dif<sup>fi</sup>culties encountered by gradient-based learning algorithms [2,11,21] such as stopping criteria, learning rate, local minima, and the over-tuning challenge, it is very fast (see [36] for more discussions). ELM's solution is not <sup>fi</sup>xed, and will vary from time to time because the input weights and hidden biases are by default randomly chosen. As a result, this becomes an issue which affects the performance of ELM. Recently, Sun et al. [39] proposed an extended ELM method (EELM) which produces forecasting by an integration of ELMs. In their proposed EELM, the average series of multiple (K) ELMs' outputs was used as the <sup>fi</sup>nal predicted result. The EELM was proven to be much more stable than the ELM. However, the EELM method requires multiple runs of the ELM as well as taking the average, which all implies a relatively longer required computational time for completing the forecasting task than the original ELM method. For our proposed 3F algorithm, it is thus critically important to <sup>fi</sup>nd an optimal number of repeating runs in the EELM with a balance of time and stability of forecasting results.

## 3.3. The grey method

The grey method (GM) originated from systems theory with uncertainty. See [31] for a recent update of the related literature. It relates to the fundamental concept of having “grey” as a color between “black” and “white” because it is sometimes impossible to classify some systems with uncertainty as purely “black” or “white” (we hence call it “grey”). In a seminal work, Deng [15] de<sup>fi</sup>ned such an uncertain system which exhibited the features of having both known and unknown information as a grey system. After its invention, GM has been widely employed in a variety of applications because of its versatile nature. In fact, GM can be used to model problems with multiple variables and an arbitrary order of differential equations. It is hence usually represented as GM (C,D), where C is the order of differential equations employed in the method and D is the number of variables. The most frequently used GM model for time series analysis is ${ \cal G } \mathrm { M } ( 1 , 1 )$ , because it is relatively neat and has the lowest computational burden.

Table 3.1  
The real sales data (a partial list).

<table><tr><td>Period</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Color code</td><td></td><td></td><td></td><td></td></tr><tr><td>A</td><td>694</td><td>2438</td><td>4495</td><td>4977</td></tr><tr><td>B</td><td>537</td><td>5535</td><td>6763</td><td>4693</td></tr><tr><td>C</td><td>2697</td><td>3486</td><td>1313</td><td>2296</td></tr><tr><td>D</td><td>3314</td><td>13049</td><td>13792</td><td>12674</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

![](/api/attachments/Z6SKPFG2/fulltext/images/f6c54c4fec9b8c1c2bd614228ade6ec5bd84b3d8a8b791bf1feeb2d00c05654b.jpg)  
Fig. 3.1. A single hidden layer feedforward neural network [49].

In the GM(1,1), we de<sup>fi</sup>ne the time series by: $X ^ { P } = [ x ^ { ( P ) } ( 1 )$ $x ^ { ( P ) } ( 2 ) , . . . , x ^ { ( P ) } \dot { ( n ) } ]$ , where $x ^ { ( P ) } ( l )$ is the data point of time series $" P "$ at time l, where $l = { 1 , 2 , . . . , n }$ . When $P = 0 ,$ , we have the original time series. A new series X<sup>−1</sup> will be generated by the Accumulated Generating Operation (see [12,15,31]) by using $X ^ { 0 } ,$ , where

$$
X ^ {1} = \left[ x ^ {(1)} (1), x ^ {(1)} (2), \dots , x ^ {(1)} (n) \right],
$$

$$
\text { and } x ^ {(1)} (l) = \sum_ {i = 1} ^ {l} x ^ {(0)} (i), \text { where } l = 1, 2,..., n.
$$

The forecasting of $X ^ { 1 }$ at time $l ,$ represented by $\hat { x } ^ { ( 1 ) } ( l ) ,$ can be derived, and the prediction of future value o $\bar { \cdot } \chi ^ { 0 }$ at time $l + 1$ can be obtained by forecasting the future value of $X ^ { 1 }$ at time $l + 1$ and l (see [15] for the analytical details):

$$
\hat {x} ^ {(0)} (l + 1) = \hat {x} ^ {(1)} (l + 1) - \hat {x} ^ {(1)} (l).\tag{3}
$$

As we reviewed in Section 2, GM was used in forecasting with very few historical data in various applications (e.g., for power demand forecasting in [23,30], and output forecasting in integrated circuits in [24,26]). However, it was also reported that GM based methods were rather unreliable when employed to conduct forecasting with very few data. It thus requires very careful consideration before using it as the sole method in conducting forecasting. Alternatively, it is probably better to use it as a component of a hybrid method as proposed in the 3F algorithm below.

## 3.4. The 3F algorithm

Many time series analysis tools, such as ANN, can be used in combination with GM to improve their performance. In this paper, to develop the 3F algorithm, we do not employ ANN owing to its over-long computational time. As such, a time constrained EELM model will be used in our algorithm to improve the forecasting accuracy of GM. The rationale behind this is: Since GM is not ideal at modeling unexpected and nonlinear events, we try to supplement it by using EELM. Such a combined model can yield an algorithm which keeps the merits of both. As illustrated in Fig. 3.2, the new time series generated by the GM forecasting model is denoted as $x _ { G M } ( l )$ , and the residual series (Rse) of the forecasting can be obtained by $\varepsilon ( l ) = x ( l ) - x _ { G M } ( l )$ where $x ( l )$ is the original time series [i.e., the original time series is split into two time series (known as the GM modeled series and Rse, respectively) and forecasting can be conducted in the two time series].

![](/api/attachments/Z6SKPFG2/fulltext/images/9413f040c2333efcc0be5727ed9304b1a97d7d3d48363765147ca61f9c37f236.jpg)  
Fig. 3.2. The model combining GM and EELM

In the proposed 3F algorithm, the forecasting for the main time series is conducted by the GM (1,1) model (to yield $x _ { G M } ( l ) )$ , and an EELM model is used for the forecasting of the residual based on the residual series $\varepsilon ( l ) .$ An EELM with two hidden neurons is adopted in this algorithm because the EELM with one hidden neuron has been found to be insuf<sup>fi</sup>cient to learn the data pattern and a two-hidden-neuron

![](/api/attachments/Z6SKPFG2/fulltext/images/30613ac3d31a00f571ef71ebb31ef5aa6f1902d475714ef5bc8dbf2191bcea82.jpg)  
Fig. 3.3. The proposed 3F algorithm.

Table 4.1  
Forecasting errors in MAPE: a comparison.

<table><tr><td></td><td>Time limit (second)</td><td>Forecasting error (MAPE)</td></tr><tr><td rowspan="4">The 3F algorithm</td><td>10</td><td>43.5%</td></tr><tr><td>1</td><td>45.1%</td></tr><tr><td>0.5</td><td>44.6%</td></tr><tr><td>0.36</td><td>50.7%</td></tr><tr><td>GM(1,1)</td><td></td><td>50.7%</td></tr><tr><td>GM(1,1)-EELM</td><td></td><td>42.2%</td></tr></table>

EELM has a suf<sup>fi</sup>cient learning capability for such a very short time series forecasting task. A one percent training goal of the mean of the original time series is imposed to (i) ensure that the network will not be overtrained, and (ii) maintain the capability of generalization or forecasting. The <sup>fi</sup>nal forecasting comes from the combination of the GM forecasting of the main series and the EELM forecasting of the residual series, which is given by $\hat { x } ^ { ' } ( l ) = x _ { G M } ( l ) + \varepsilon _ { E E L M } ( l )$ . The forecasting accuracy of GM is hereby improved by the EELM, while we can enjoy the versatility of the GM method as reported in the literature.

## 3.5. The 3F algorithm with GM and GM-EELM models

Similar to the literature employing the GM based methods, in getting the 3F algorithm, we employ GM-EELM for the sake of better accuracy. In our study, the time used by the GM model is found to be linearly related to the number of data points in the training sample (S), so it can be proven that the total time cost by the whole algorithm (TC) is given in the following quadratic format:

$$
T C = P t _ {1} N S ^ {2} + P t _ {2} N ^ {2} S + P t _ {3} + n,\tag{4}
$$

where N is the number of neurons in the ELM, P is the number of times of repeating the ELM to form EELM, S is the number of data points in the training sample, n is the program startup time, and $t _ { 1 } , t _ { 2 }$ and $t _ { 3 }$ are coef-<sup>fi</sup>cient constants which will be found by the proposed algorithm. The 3F algorithm will fall back to the GM model if the time limit to run the full version cannot be met. The whole 3F algorithm is constructed as in Fig. 3.3.

Table 5.1  
Four arti<sup>fi</sup>cial time series datasets.

<table><tr><td>Time series datasets</td><td>Trend slope</td><td>Season variance</td><td>Noise variance</td></tr><tr><td>1</td><td>0.2</td><td>20</td><td>10</td></tr><tr><td>2</td><td>0.2</td><td>20</td><td>1</td></tr><tr><td>3</td><td>0.2</td><td>2</td><td>1</td></tr><tr><td>4</td><td>0.4</td><td>20</td><td>1</td></tr></table>

As a remark, the 3F algorithm can perform forecasting to support fast fashion operations under the tight time constraint in conducting forecasting as well as neutralizing the data suf<sup>fi</sup>ciency problem.

## 4. Testing results with real data analysis

The 3F algorithm is tested with the data in Table 3.1 and the results are listed in Table 4.1. Forecasting for Period 4 based on the 3 periods of historical data is conducted. The time limits in seconds of 10, 1, 0.5, and 0.36 are employed respectively in the test. The reason for using 0.36 s as the time limit is that when we want 10,000 instances of such forecasting to be <sup>fi</sup>nished within 1 hour, the time limit for 1 item's forecasting is given by 0.36 s. The 3F algorithm can automatically and intelligently select the appropriate model between GM(1,1) and GM(1,1)-EELM, and the results for GM(1,1) and GM(1,1)-ANN from [14] are cited for reference.

In Table 4.1, we can observe that for the time limits 10 s, 1 s, and 0.5 s, the forecasting errors range from 43.5% to 45.1%. In these cases, the time limit is enough for the 3F algorithm to use the GM(1,1)-EELM to perform the forecasting task with a limited repetition. Notice that the errors are slightly higher than GM(1,1)-ANN because we are using the GM(1,1)-EELM to compromise accuracy for speed. The worst case occurs at a time constraint of 0.36 $s ,$ where the MAPE is 50.7%. We can tell that, in this case, although the time is not enough for the GM(1,1)-EELM and GM(1,1) models to be used, the same forecasting error as using GM(1,1) is obtained.

![](/api/attachments/Z6SKPFG2/fulltext/images/88df2330544cb51c42f5f4ee189b88cae44e81e43481a931ebe455f9a4c1d7b4.jpg)

![](/api/attachments/Z6SKPFG2/fulltext/images/9e877e8ebdbb5aa4fa5936058b80d35872a7f3e485d21613d5fbd94621dc5da5.jpg)

![](/api/attachments/Z6SKPFG2/fulltext/images/fe56d95efb654c4f818da3f149e63dc26bfa2a2b65dc568d949beaa375e3b30b.jpg)  
Fig. 5.1. An illustration of time series 1.

![](/api/attachments/Z6SKPFG2/fulltext/images/7c89a1469074492196834b1293e5a26fd9c705330efbe4b634355da967c138a5.jpg)  
Fig. 5.2. The MAPE of 10 consecutive forecasting results of different methods on the arti<sup>fi</sup>cial dataset 1.

Observing from the results, we <sup>fi</sup>nd that the 3F algorithm with GM(1,1) and GM(1,1)-EELM can produce a reasonable forecasting accuracy under the constraints on time and data suf<sup>fi</sup>ciency. As expected, with a given longer time limit, a better accuracy can be achieved; whereas with a tight time limit, the algorithm can still offer a reasonably good result. Observe that despite having a relatively large forecasting error, we have to understand the dif<sup>fi</sup>culty behind this problem. Owing to the computational time restrictions as well as the lack of enough data, fast fashion forecasting is an extremely dif<sup>fi</sup>cult problem. Unfortunately, this forecasting task is still essential for the real world operations for fast fashion companies. As a result, we believe that the proposed 3F algorithm can provide a scienti<sup>fi</sup>cally sound and practical method to accomplish this goal.

## 5. Further analysis on arti<sup>fi</sup>cial datasets

In this section, we conduct some more tests on the 3F algorithm based on some arti<sup>fi</sup>cial datasets. By employing this kind of arti<sup>fi</sup>cial data, we can reveal additional insights regarding the performance of the 3F algorithm with respect to different features of the given datasets. To be speci<sup>fi</sup>c, an arti<sup>fi</sup>cial dataset is constructed from the summation of three components of the time series: The trend series, the seasonal cycle series, and the noise series. The features of the components are given by their variances or the slopes of the trend. A typical time series with 100 time units of data points is constructed by trend slope = 0.2, seasonal variance = 20, and noise variance = 10, which is depicted in Fig. 5.1.

Three other time series with different features of the three components are given in Table 5.1. Tests on these four time series can reveal the impacts brought by a change of these three components.

Notice that in our proposed 3F algorithm, the GM-EELM model is actually more-preferred for the sake of better forecasting accuracy. However, under the given time limit constraint to support fast fashion, we often have to conduct forecasting under the 3F algorithm by employing the GM model (under the 3F algorithm, this change is automatic). By the tests on these four time series in Table 5.1, we explore the performance of the 3F algorithm with different amounts of historical data points as well as different time limits to study the validity of the model selection scheme in the 3F algorithm. Fig. 5.2 through Fig. 5.5 plot the results from the tests. As we can see from the experimental results, the GM-EELM with 2 neurons and 2 inputs is found to meet the time limit of 0.5 s, and the GM-EELM with 2 neurons and 7 inputs is found to meet the time limit of 20 s (but NOT 0.5 s). In order to illustrate how the speci<sup>fi</sup>c features of the data time series affect the performance of the 3F algorithm with respect to its selection of the right model during the forecasting process, we compare it with three other algorithms:

Algorithm 1 The Static GM algorithm, which is the same as the general GM(1,1);

Algorithm 2 The Static GM-EELM algorithm (with a 0.5 second time limit, neuron number = 2 and input number = 2);

Algorithm 3 The Static GM\_EELM algorithm (with a 20 seconds time limit, neuron number = 2 and input number = 7).

![](/api/attachments/Z6SKPFG2/fulltext/images/d70d69e3e63c32b11d8220783ab6da5672de1b4bd6e96473c831034e1af419eb.jpg)  
Fig. 5.3. The MAPE of 10 consecutive forecasting results of different methods on the arti<sup>fi</sup>cial dataset 2.

![](/api/attachments/Z6SKPFG2/fulltext/images/65d3bd551ce5d4a9844f511f266c8570a06dd5083345049b613f7461d606b1bb.jpg)  
Fig. 5.4. The MAPE of 10 consecutive forecasting results of different methods on the arti<sup>fi</sup>cial dataset 3.

Observe that the performance of the 3F algorithm will be exactly the same as the performance of one of the three algorithms (Algorithms 1 to 3) if that algorithm is chosen in the 3F algorithm as the appropriate method to perform the actual forecasting. With the input and training requirements, the forecasting of the Static GM-EELM algorithm can only start from 6, and 10 historical data points (the minimum numbers of data points). In order for the Static GM algorithm to work, at least 3 data points are required. The actual forecasting results are obtained from the 3F algorithm with the appropriate choice between the Static GM and the Static GM-EELM algorithms; such an appropriate choice is depicted by the thick grey dotted lines in Fig. 5.2 through 5.5.

In general, we can see that the Static GM-EELM algorithm is more accurate for the case when the number of historical data points ranges from 6 to around 10. With the speci<sup>fi</sup>c data constraint of having only 20 or fewer than 20 data points, the 3F algorithm makes an appropriate selection to choose the Static GM-EELM algorithm as the forecasting model. As for the forecasting with a data limit of over 20 points, the results would highly depend on the feature of the dataset. As shown in Fig. 5.2, with a high variance of white noise, all three models perform poorly and there is no clear advantage of any single method over the other two. The appropriate choice of the Static GM algorithm or others under the 3F algorithm does not make a major difference in such a situation. While as shown in Fig. 5.2, the Static GM-EELM algorithm with a sophisticated structure dominates the others whenever it is applicable for the modeling, and the appropriate choice that the 3F algorithm made, which favors the Static GM-EELM algorithm, is often the appropriate one because it can yield better forecasting results. As we stated earlier, the 3F algorithm is designed for forecasting fast fashion which is characterized by having a tight time limit and insuf<sup>fi</sup>cient historical data. These features match perfectly the condition where the number of data points is fewer than 20. Comparing Figs. 5.2 and 5.3 which are derived from the results on time series 1 and 2, we <sup>fi</sup>nd that dampening the white noise variance improves the accuracies of all the algorithms, while the Static GM-EELM algorithm with a loose time constraint obviously performs the best. This directly implies that the corresponding 3F algorithm which relies on it will also achieve better results as shown in Fig. 5.3.

If we further reduce the seasonal cycle variance to 2, which is 10 times lower than that in Fig. 5.3, we produce Fig. 5.4 which reveals that the forecasting errors may become lower due to the signi<sup>fi</sup>cantly lowered total variance of the whole time series. However, it turns out that all the algorithms under testing cannot differentiate the seasonal cycle from the noise, which leads to an inferior performance. Hence, rather than reducing the variance of noise, a reduction of the seasonal cycle's variance actually reduces the performance of all algorithms and decreases the advantages of our 3F algorithm. When the slope of the trend is considered, as in time series 4, with the slope being doubled from 0.2 to 0.4, the results as shown in Fig. 5.5 are similar to Fig 5.3, where the overall errors may become lower due to the smaller total variance; the differences between the algorithms are similar because the 3F algorithm, which utilizes the Static GM-EELM algorithm mostly in this case, still dominates the others in terms of accuracy. This reveals that trend is a useful feature that needs to be captured by the forecasting algorithms. However, noise, unlike the pattern, is an obstacle to all forecasting algorithms; an increase of noise variance, or a decrease of pattern variance (or similarly, slope of the trend) will undermine the forecasting accuracy of the algorithm. We notice that if these two are of a similar level, Algorithms 1 to 3 under testing will all perform poorly; in such a case, our proposed 3F algorithm also produces bad results. Removing this special case, our 3F algorithm produces better results than Algorithms 1 to 3. A summary of the core insights from the numerical analysis with arti<sup>fi</sup>cial datasets is shown in Table 5.2.

![](/api/attachments/Z6SKPFG2/fulltext/images/0c1f6337a7bec4b74c4ea2803841001c3e6417900ade384bf34b48c7d8197dd4.jpg)  
Fig. 5.5. The MAPE of 10 consecutive forecasting results of different methods on the arti<sup>fi</sup>cial dataset 4.

Insights from the further data analysis (↑ = increases).

<table><tr><td></td><td>Trend slope ↑ (when noise is insignificant)</td><td>Seasonal cycle&#x27;s variance ↑ (when noise is insignificant)</td><td>White noise variance ↑ (when noise is significant)</td></tr><tr><td>Data Points ≤20 (data insufficiency)</td><td>The 3F algorithm performs best.</td><td>The 3F algorithm performs best.</td><td>All models perform worse.</td></tr><tr><td>Data Points &gt;20 (having sufficient data)</td><td>The Static GM-EELM-20s algorithm performs the best.</td><td>The Static GM-EELM-20s algorithm performs the best.</td><td>All models perform worse.</td></tr><tr><td>Time Limit (20 s, loose constraint)</td><td>The 3F algorithm performs best.</td><td>The 3F algorithm performs best.</td><td>All models perform worse.</td></tr><tr><td>Time Limit (0.5 s, tight constraint)</td><td>The 3F algorithm performs best.</td><td>The 3F algorithm performs best.</td><td>All models perform worse.</td></tr></table>

## 6. Conclusion and managerial implications

Fast fashion is a commonly adopted and timely strategy in fashion retailing. Under fast fashion, many operational decisions in the supply chain must be made with a tight schedule and the product life cycle is very short. As a result, the corresponding fashion demand forecasting function has to be completed within a very short time with very few historical data being available. Motivated by an aim to improve fast fashion business practices, we have integrated the GM and the EELM models to form the 3F algorithm. The newly proposed 3F algorithm has been tested with both real fashion company's sales datasets as well as arti<sup>fi</sup>cial datasets. We have found that we can obtain acceptable forecasting accuracy with the 3F algorithm. In fact, the 3F algorithm employs the “best-effort strategy in conducting forecasting”. With a relatively loose time limit, the 3F algorithm provides a better forecasting accuracy than GM(1,1). With a tight time limit, the 3F algorithm converts to GM(1,1) to provide a rapid forecasting result, but still yields an acceptable accuracy. In addition, we have the following managerial implications:

(i) Since our analysis reveals that the 3F algorithm performs forecasting especially well when (a) the data pattern exhibits a large trend slope, and (b) the seasonal cycle's variance is large for the case when data is insuf<sup>fi</sup>cient with a tight time limit. These two features help characterize the situations under which the management of the fast fashion company should very seriously consider employing the 3F algorithm because its performance will be especially promising. In other words, managers of fast fashion companies could check the trend slope and seasonal cycle's variance of their own sales datasets and see if they are large or not. If they are large, the 3F algorithm will help improve the company's forecasting performance a lot.

(ii) With the 3F algorithm, the fast fashion company can achieve the goal of conducting sales forecasting in a very timely manner. This helps the company to achieve quick response inventory management practice because the inventory <sup>fl</sup>ow is driven by the fast forecasting result. In the supply chain system, both the manufacturing and the retailing operations can hence be highly market-driven and “pulled” by the timely forecasting result.

(iii) With the reasonably good forecasting result achieved by the 3F algorithm, the inventory performance of the fast fashion company will improve because the company will be able to better match its own demand and supply. This directly leads to a reduction of the amount of required markdown and also improves inventory service level. This aspect is very important to the fast fashion companies because inventory cost is very signi<sup>fi</sup>cant and even the famous fast fashion company Zara is considering to conduct markdown and discount outlet sales nowadays.<sup>4</sup>

Notice that even though the 3F algorithm is speci<sup>fi</sup>cally designed for fast fashion sales forecasting, we believe that it can be applied to other domains. For example, it can be used for predicting the prices of some recently listed stocks in the <sup>fi</sup>nancial market, and forecasting the demands of some short-life highly seasonal products (e.g., some seasonal toys and consumer electronics products). Observe that for the above mentioned domains, decision makers commonly wish to have a quick forecasting result in order to support their decision making (P.S.: In <sup>fi</sup>nance, investment decisions must be made promptly with respect to the latest information available; for the highly seasonal products, their lives are short and forecasting must be done as soon as possible). At the same time, since these stocks are young and the seasonal products have short lives, only a very limited amount of data is available for making the prediction. Our proposed 3F algorithm, which has the capability of conducting forecasting in the presence of limited data and limited time, can hence help.

Further research can be conducted on examining how the 3F algorithm performs in connection with other supply chain operations in fast fashion such as inventory planning by simulation studies. In terms of real world applications, it will also be important to study in the future how the 3F algorithm can be developed into a forecasting decision support system for fast fashion operations.

## References

[1] B. Abraham, J. Ledolter, Statistical methods for forecasting, Probability and Mathematical Statistics. Wiley Series. 1983.

[2] K.F. Au, T.M. Choi, Y. Yu, Fashion retail forecasting by evolutionary neural networks, International Journal of Production Economics 114 (2) (2008) 615–630.

[3] J.L. Aznarte, J. Alcalá-Fdez, A. Arauzo-Azofra, J.M. Benítez, Financial time series forecasting with a bio-inspired fuzzy model, Expert Systems with Applications 39 (16) (2012)12302-12309

[4] G.E.P. Box, G.M. Jenkins, G.C. Reinsel, Time Series Analysis: Forecasting and Control, 4th edition John Wiley, 2008

[5] G. Cachon, R. Swinney, The value of fast fashion: quick response, enhanced design, and strategic consumer behavior, Management Science 57 (4) (2011) 778–795.

[6] F. Caro, J. Gallien, Dynamic assortment with demand learning for seasonal consumer goods, Management Science 53 (2) (2007) 276–292.

[7] F. Caro, J. Gallien, Inventory management of a fast-fashion retail network, Operations Research 58 (2) (2010) 257–273.

[8] O.A.S. Carpinteiroa, R.C. Leme, A.C.Z. de Souza, C.A.M. Pinheiro, E.M. Moreira, Long-term load forecasting via a hierarchical neural model with time integrators, Electric Power Systems Research 77 (3–4) (2007) 371–378.

[9] H. Chaoui, P. Sicard, W. Gueaieb, ANN-based adaptive control of robotic manipulators with friction and joint elasticity, IEEE Transactions on Industrial Electronics 56 (8) (2009) 3174–3187.

[10] P.C. Chang, Y.W. Wang, C.H. Liu, The development of a weighted evolving fuzzy neural network for PCB sales forecasting, Expert Systems with Applications 32 (1) (2007) 86–96.

[11] P.C. Chang, Y.W. Wang, C.Y. Tsai, Evolving neural network for printed circuit board sales forecasting, Expert Systems with Applications 29 (1) (2005) 83–92

[12] F.L. Chen, T.Y. Ou, Gray relation analysis and multilayer functional link network sales forecasting model for perishable food in convenience store, Expert Systems with Applications 36 (3) (2009) 7054–7063.

[13] T.M. Choi, C.L. Hui, S.F. Ng, Y. Yu, Color trend forecasting of fashionable products with very few historical data JEEE Transactions on Systems Man and Cybernetics Part C: Applications and Reviews 42 (6) (2012) 1003–1010

[14] T.M. Choi, Y. Yu, K.F. Au, A hybrid SARIMA wavelet transform method for sales forecasting, Decision Support Systems 51 (1) (2011) 130–140.

[15] J.L. Deng, Introduction to grey system theory, The Journal of Grey System 1 (1) (1989) 1–24.

[45] A.W.L. Yao, S.C. Chi, J.H. Chen, An improved grey-based approach for electricity demand forecasting, Electric Power Systems Research 67 (3) (2003) 217–224

[16] T. Dereli, K. Altun, A novel approach for assessment of candidate technologies with respect to their innovation potentials: quick innovation intelligence process, Expert Systems with Applications 40 (3) (2013) 881–891.

[17] E. Egrioglu, C.H. Aladag, U. Yolcu, Fuzzy time series forecasting with a novel hybrid approach combining fuzzy c-means and neural networks, Expert Systems with Applications 40 (3) (2013) 854–857.

[18] H.M. El-Bakry, N. Mastorakis, A New Fast Forecasting Technique Using High Speed Neural Networks, Proceedings of the 8th WSEAS International Conference on Signal, Speech and Image Processing (SSIP '08), Spain (2008), 2008, pp. 116–138.

[19] S. Fan, L.N. Chen, W.J. Lee, Short-term load forecasting using comprehensive combination based on multimeteorological information, IEEE Transactions on Industry Applications 45 (4) (2009) 1460–1466.

[20] P. Ghemawat, J.L. Nueno, ZARA: Fast Fashion, Harvard Business School Case (9-703-497), 2003. 1–35.

[21] C. Hamzaçebia, D. Akay, F. Kutay, Comparison of direct and iterative arti<sup>fi</sup>cial neural network forecast approaches in multi-periodic time series forecasting, Expert Systems with Applications 36 (2) (2009) 3839–3844.

[22] J.V. Hansen, R.D. Nelson, Neural networks and traditional time series methods: a synergistic combination in state economic forecasts, IEEE Transactions on Neural Networks 8 (4) (1997) 863–873.

[23] C.C. Hsu, C.Y. Chen, Applications of improved grey prediction model for power demand forecasting, Energy Conversion and Management 44 (14) (2003) 2241–2249.

[24] L.C. Hsu, Applying the grey prediction model to the global integrated circuit industry, Technological Forecasting and Social Change 70 (6) (2003) 563–574.

[25] L.C. Hsu, Forecasting the output of integrated circuit industry using genetic algorithm based multivariable grey optimization models, Expert Systems with Applications 36 (4) (2009) 7898–7903.

[26] L.C. Hsu, C.H. Wang, Forecasting the output of integrated circuit industry using a grey model improved by the Bayesian analysis, Technological Forecasting and Social Change 74 (6) (2007) 843–853.

[27] G.B. Huang, Q.Y. Zhu, C.K. Siew, Extreme learning machine: theory and applications, Neurocomputing 70 (1–3) (2006) 489–501.

[28] J. Kim, M. Hwang, D.H. Jeong, H. Jung, Technology trends analysis and forecasting application based on decision tree and statistical feature analysis, Expert Systems with Applications 39 (16) (2012) 12618–12625.

[29] C. Kim, S. Park, K. Kwon, W. Chang, An empirical test to forecast the sales rank of a keyword advertisement using a hierarchical Bayes model, Expert Systems with Applications 39 (17) (2012) 12727–12742.

[30] M. Lei, Z. Feng, A proposed grey model for short-term electricity price forecasting in competitive power markets, International Journal of Electrical Power & Energy Systems 43 (1) (2012) 531–538.

[31] Y.H. Lin, P.C. Lee, Novel high-precision grey forecasting model, Automation in Construction 16 (6) (2007) 771–777.

[32] B. Majhi, M. Rout, R. Majhi, G. Panda, P.J. Fleming, New robust forecasting models for exchange rates prediction, Expert Systems with Applications 39 (16) (2012) 12658–12670.

[33] T. Orlowska-Kowalska, K. Szabat, Neural-network application for mechanical variables estimation of a two-mass drive system, IEEE Transactions on Industrial Electronics 54 (3) (2007) 1352–1364.

[34] H. Park, J. Lee, Forecasting nonnegative option price distributions using Bayesian kernel methods, Expert Systems with Applications 39 (18) (2012) 13243–13252.

[35] B. Premanode, C. Toumazou, Improving prediction of exchange rates using Differential EMD. Expert Systems with Applications 40 (1) (2013) 377–384.

[36] H.J. Rong, Y.S. Ong, A.H. Tan, Z. Zhu, A fast pruned-extreme learning machine for classi<sup>fi</sup>cation problem, Neurocomputing 72 (1–3) (2008) 359–366.

[37] S. Shin, S. Lee, H. Kim, S. Kim, Advanced probabilistic approach for network intrusion forecasting and detection, Expert Systems with Applications 40 (1) (2013) 315–322.

[38] M. Štěpnička, P. Cortez, J.P. Donate, L. Štěpničková, Forecasting seasonal time series with computational intelligence: on recent methods and the potential of their combinations, Expert Systems with Applications 40 (6) (2013) 1981–1992.

[39] Z.L. Sun, K.F. Au, T.M. Choi, A neuro-fuzzy inference system through integration of fuzzy logic and extreme learning machines, IEEE Transactions on Systems, Man, and Cybernetics — Part B: Cybernetics 37 (5) (2007) 1321–1331.

[40] Z.L. Sun, T.M. Choi, K.F. Au, Y. Yu, Sales forecasting using extreme learning machine with applications in fashion retailing, Decision Support Systems 46 (1) (2008) 411–419.

[41] H. Takahashi, D. Ukishima, K. Kawamoto, K. Hirota, A study on predicting hazard factors for safe driving, IEEE Transactions on Industrial Electronics 54 (2) (2007) 781–789.

[42] H.L. Willis, T.W. Parks, Fast algorithms for small area electric load forecasting, IEEE Transactions on Power Apparatus and Systems PAS-102 (10) (1983) 3425–3432.

[43] C. Won, J. Kim, J.K. Bae, Using genetic algorithm based knowledge re<sup>fi</sup>nement model for dividend policy forecasting, Expert Systems with Applications 39 (18) (2012) 13472-13479

[44] Q. Wu, The forecasting model based on wavelet ν-support vector machine, Expert Systems with Applications 36 (4) (2009) 7604–7610.

[46] Y. Yu, T.M. Choi, C.L. Hui, An intelligent fast sales forecasting model for fashion products Expert Systems with Applications 38 (6) (2011) 7373–7379.

[47] N. Liu, S. Ren, T.M. Choi, C.L. Hui, S.F. Ng, Sales forecasting for fashion retailing service industry: a review, Mathematical Problems in Engineering (2013), http://dx.doi.org/10.1155/2013/738675(in press).

[48] T.M. Choi, S. Sethi, Innovative quick response programmes: a review, International Journal of Production Economics 127 (1) (2010) 1–12.

[49] Y. Yu, T.M. Choi, C.L. Hui, An intelligent quick prediction algorithm for industrial control and loading problems, IEEE Transactions on Automation Science and Engineering 9 (2) (2012) 276–287.

![](/api/attachments/Z6SKPFG2/fulltext/images/0751e7c7277f3e5fc4d50abe88863dbe0d775fe1f5e8f540635be6963ffc2d28.jpg)

Tsan-Ming Choi is currently an associate professor at The Hong Kong Polytechnic University. His research interests mainly focus on information systems and supply chain operations. He has published extensively in leading academic journals such as Annals of Operations Research Automatica Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Automatic Control, Production and Operations Management, Service Sciences (INFORMS Journal), and <sup>fi</sup>ve other leading IEEE Transactions. He authored/edited ten research handbooks and guest edited over twelve special issues in academic journals. He is currently an area editor/associate editor/guest editor of Annals of Operations Research, Decision Sciences, Decision Support Systems, European Management Journal, IEEE Transactions on Systems,

Man, and Cybernetics — Systems, Information Sciences, Journal of the Operational Research Society, Production and Operations Management, and various information systems and operations management journals. He received The Hong Kong Polytechnic University's President Award for Excellent Performance/Achievement in 2011, and the Best Associate Editor Award of the IEEE Systems, Man, and Cybernetics Society's Publications in 2013

![](/api/attachments/Z6SKPFG2/fulltext/images/f6398a5a8fd11371435e7e812dbb8c52037d60b2786142312e77172f920f4ae4.jpg)

Chi-Leung Hui gained an MSc in Technological Economics from the University of Stirling, UK in 1988, an MSc in Information Systems from the Hong Kong Polytechnic in 1992, an MSc(Eng.) in Computers in Manufacturing from the University of Hong Kong in 1995, a PhD from The Hong Kong Polytechnic University in 1999, a LLB (Hons) from the University of Wolverhampton, UK in 2004, a LLM degree in information technology and intellectual property law from the University of Hong Kong in 2008, and Diploma in Marketing from the Chartered Institute of Marketing, UK, in 1988 and the Certi<sup>fi</sup>ed Diploma in Finance and Accounting from The Chartered Association of Certi<sup>fi</sup>ed Accountants, UK, in 1991. He is a Chartered Engineer and is a chartered member of both the British Computer Society and the Chartered Institute of Marketing. He has published over 50 refereed papers in journals such as Computers in Industry, IEEE Transactions on Engineering Management and IEEE Transactions on Systems, Man and Cybernetics — Parts A & C, and international conferences. Dr Hui is an associate professor at The Hong Kong Polytechnic University.

![](/api/attachments/Z6SKPFG2/fulltext/images/96a4d89a293794f19c1382a9f979691c144369db64906971ac23d4c2e79f5544.jpg)

Na Liu obtained her Ph.D from The Hong Kong Polytechnic University and she is now a postdoctoral research associate. She was the chairlady of IEEE Systems, Man, and Cybernetics Society Hong Kong Chapter (IEEE-SMC-HK)'s student branch at The Hong Kong Polytechnic University from 2009–2012. Her research interests focus on mass customization in fashion supply chains and forecasting. She has published papers in academic journals such as Decision Support Systems, IEEE Transactions on Systems, Man, and Cybernetics — Part A, Mathematical Problems in Engineering, and Journal of Brand Management. She also received the outstanding paper award (2nd prize) in the IEEE-SMC-HK PhD Student Paper Contest in 2010.

![](/api/attachments/Z6SKPFG2/fulltext/images/7b94de1d4cdfc4ac8acf392a6d8597b49ee062a7caa4ec13590d37e9d220d55e.jpg)

Sau-Fun Ng is currently an Associate Professor at The Hong Kong Polytechnic University. Dr Ng graduated with a Higher Diploma in Fashion & Clothing Technology from the Hong Kong Polytechnic in 1978. She gained her MPhil from Leicester Polytechnic UK in 1990 and was awarded a PhD from De Montfort University, UK, on the basis of research in the area of pressure garments in 1996. Dr Ng has published extensively on topics of relevance to medical clothing and pressure garments for the scienti<sup>fi</sup>c treatment hypertrophic scars.

![](/api/attachments/Z6SKPFG2/fulltext/images/e7667b8b2ee92141df818c8cb91f100c0d58b6332a691e21a3b669e56cb42c94.jpg)

Yong Yu is a postdoctoral research associate at the Hong Kong Polytechnic University. He received his PhD from the Hong Kong Polytechnic University and he extensively published in journals such as Decision Support Systems, Expert Systems with Applications, IEEE Transactions on Automation Science and Engineering IEEE Transactions on Systems Man and Cybernetics — Parts A and C, and International Journal of Production Economics.
