---
otero_id: 12756
otero_key: "M374HDHF"
title: "A hybrid model by clustering and evolving fuzzy rules for sales decision supports in printed circuit board industry"
authors: "Pei-Chann Chang; Chen-Hao Liu; Yen-Wen Wang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.10.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid model by clustering and evolving fuzzy rules for sales decision supports in printed circuit board industry

Pei-Chann Chang <sup>\*</sup>, Chen-Hao Liu, Yen-Wen Wang

Department of Industrial Engineering and Management, Yuan Ze University, Taoyuan 32026, Taiwan, R.O.C.

Received 14 January 2005; received in revised form 11 October 2005; accepted 24 October 2005 Available online 13 December 2005

## Abstract

This research develops a hybrid model by integrating Self Organization Map (SOM) neural network, Genetic Algorithms (GA) and Fuzzy Rule Base (FRB) to forecast the future sales of a printed circuit board factory. This hybrid model encompasses two novel concepts: (1) clustering an FRB into different clusters, thus the interaction between fuzzy rules is reduced and a more accurate prediction model can be established, and (2) evolving an FRB by optimizing the number of fuzzy terms of the input and output variables, thus the prediction accuracy of the FRB is further improved. Numerical data of various affecting factors and actual demand of the past 5 years of the printed circuit board (PCB) factory are collected and inputted into the hybrid model for future monthly sales forecasting. Experimental results show the effectiveness of the hybrid model when comparing it with other approaches. However, the theoretical development of the validity of clustering an FRB into sub clusters remains to be proven. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Sales forecasting; Printed circuit board; Genetic algorithm; Fuzzy rule base; SOM neural network

## 1. Introduction

Printed Circuit Board (PCB) industry is a very important business in Taiwan, because of its high value of output. While local production suffered from the global recession and unfavorable environment, the growth of overseas production continued, especially in China. Today, Taiwan has established one of the best PCB production supply chain and infrastructures in the world with advanced technical capabilities and an extended customer base. The emergence of China however highlights some of Taiwan’s intrinsic difficulties, such as the lack of local market and rising labor and land costs, which make the future growth more challenging.

Under the situation of the short life span and high circulating rate of related electronic products of PCB, general production models cannot fulfill customers’ demands effectively. Thus, how to predict customer’s demand and prepare material flows in advance to reduce the cycle time has become a pressing issue to be dealt with. Furthermore, an efficient sales forecasting tool can be the key to strengthen the company’s survival ability in the competitive environment. Therefore, it becomes indispensable to build a forecasting model to predict the monthly sales in PCB industry through an efficient and effective forecasting model.

The prediction of monthly sales in PCB industry can be considered as a modeling problem, which is to establish mapping between input(s) and output(s). Usually, the mapping is hard to define and it is nonlinear and chaotic. After such a mapping is set up, the model can be applied to predict future sales based on past and current observations.

## 2. Approaches in sales forecasting

Traditionally, the most commonly used forecasting techniques are statistical methods, such as Multiple Regression model in [27,28,31] and time series models such as moving average, exponential smoothing and the Box-Jenkins autoregressive integrates moving average (ARIMA) methods in [1,6,8,15,28]. These models have been proven to be very effective for data with simple trend and seasonality tendency. However, in the real world the relationship between the factors or the past time series data (independent variables) and the sales (dependent variable) are always nonlinear and quite chaotic. Another alternative approach is an <sup>b</sup>Econometric Model<sup>Q</sup> which is to investigate the relationship between the external economic variables and the final sales. Srinivasan [39] proposes a forecasting model based on Econometric Model integrated with Neural Network and proved that it could have better performance measure when compared to traditional approaches.

Recently, with the development of the Artificial Intelligence techniques, several methods are found to have better performance than traditional models when applied to forecasting problems and Artificial Neural Networks (ANNs) are the most commonly used tools. After being trained by historical data, ANNs can be used to predict the sales in the future. Many researchers have successfully applied ANNs to solve forecasting related problems as in [4,7,18,20–24,26,40,41].

Ever since Zadeh [51] introduces the concept of fuzzy logic, fuzzy-set theory has been widely applied in the industrial system controls that are very complex, uncertain and cannot be modeled precisely. The fuzzy controllers with many fuzzy control rules will capture the reasoning process of human operators. Especially, fuzzy rules based controller have been the most popular and easiest way to capture and represent fuzzy, vague, imprecise and uncertain domain knowledge. Traditionally, these FRBs are provided and extracted from domain experts. It is very difficult and time-consuming to obtain accurate and reasonable FRBs. In recent years, much research has been proposed to generate and produce FRBs from a set of sample data. An automated fuzzy knowledge base generation and tuning method is presented in [2]. Hong and Chen [12] provide a method to construct membership functions for FRBs generation, while in [13] a way to process individual fuzzy attributes for fuzzy rule induction is given. A GA method to select fuzzy if-then rules for classification problems could be found in [16]. Kao and Chen [17] propose a method to generate FRBs from training data with noise for classification problems. Ravi et al. [38] present a method for the generation of fuzzy rule base and its optimization by using modified threshold accepting. Wang and Hong [46] present a method to optimize and simplify fuzzy rules. A fuzzy decision tree induction technique is proposed to generate fuzzy rules [50].

According to the literature survey above, there are many methods that allow us to generate a set of FRB; however, these extracted rules are found to be far from optimal and sometimes redundant. Therefore, this paper focuses on the performance improvement of FRB by integrating Self-Organizing Map (SOM) neural network, Genetic Algorithms (GA) and Fuzzy Rule Base (FRB) to forecast the future sales of a printed circuit board factory. This hybrid model encompasses two new concepts: (1) clustering an FRB into different sub-clusters, thus the interactions between fuzzy rules can be reduced and a more accurate prediction model can be established, and (2) evolving an FRB by optimizing the number of fuzzy terms of the input and output variables, thus the prediction accuracy of the FRB is further improved.

## 3. Features of the prediction model

A key to success for manufacturing companies in the worldwide competition is to build a reliable and accurate forecasting model that can predict in time suitable items at sufficient quantity and to adapt to an uncertain environment. Therefore, forecasting plays an important role in today’s business planning. The fundamental basis of the master production schedule is generated according to the orders received and the sales forecasted from the sales department to explore the future production quantity of the next 3–5 months for production planning department to follow. However, traditional forecasting methods suffer from several deficiencies and limitations, which make them severely inadequate for strategic business planning in today’s business environment. First, a mathematical model is really hard to be defined and the relationship between the forecasted output and the decision factors is nonlinear or chaotic; especially when there are lots of factors to be considered. This limits the usefulness of the conventional forecasting methods like econometric or time series forecasting. Second, today’s business environment is constantly changing as the customers and competitors are also changing, thus causing the decision boundaries to shift. Conventional forecasting methods are not flexible and cannot adapt to the dynamic environment in time. Third, conventional forecasting methods rely heavily on large amount of historical data, which are often unavailable in the real world. It is therefore desirable to develop a new sale forecasting model that can handle vague, imprecise, and uncertain situations and is more similar to the reasoning process of human being.

An accurate and reliable sales forecasting system as described in [42] must satisfy the following criteria:

1. To quickly react to the significant variation of trend and seasonality in the market;

2. To identify and smooth purely random noises;

3. To consider the influences of endogenous variables related to the PCB product itself;

4. To take into account the influences of exogenous variables (demographic variables, macroeconomic indicators, competitors, etc.).

To enable the generation of explicit knowledge, this research presents a novel approach by combining SOM and fuzzy rule base for sales forecasting. An earlier research in [5] was carried out by applying Winter’ Exponential Smoothing to take care of the trend, seasonality, and noise situation and adopting Grey Relation Analysis to screen endogenous and exogenous variables from PCB industry and outside environment. In this paper, an extension of our previous work is proposed and a fuzzy rule base clustered by an SOM and evolved by a GA to predict the monthly sales of a PCB factory is developed. First, independent variables related to sales variation are collected and fed into the SOM for classification. Then, the corresponding fuzzy rule base with less interaction and more accuracy is selected and applied for sales forecasting. Genetic process is further applied to fine-tune the composition of the rule base. Finally, the generated hybrid model is applied as a tool for sales prediction in printed circuit board industry.

## 4. Hybrid model for sales decision support in PCB industry

There are several sources of variation affecting the sales prediction in PCB industries other than trend, seasonality and random noise. However, these affecting factors are very difficult to identify. Even if these factors are known, there is no exact governing function describing the relationship between these factors and the total sales. The mathematical function, $F ( x _ { 1 } , x _ { 2 } , \ldots ,$ $x _ { \mathrm { n } } ) _ { \mathrm { \ell } }$ , is unknown. Therefore, there is a need to develop a model free approach—a Fuzzy Rule Base, to deal with this nonlinear, imprecise, uncertain, ambiguous and dynamic data set. The architecture of the proposed hybrid model for sales decision supports is depicted in Fig. 1.

![](/api/attachments/M374HDHF/fulltext/images/c5ead1ea87d6293a070616389383c18b12a4ecab164ee0ef7784f221a58538cf.jpg)  
Fig. 1. An architecture of the hybrid model for sales decision supports.

The system is designed in a PC based environment; the user from either sales department or production planning and control can retrieve related input data from the web. These data will be inputted to the hybrid model to generate new forecasted sales for decision support. Also, statistical software can be further applied to analyze these forecasted outputs. The whole system is very user friendly and easy to use when implemented in the factory and it does provide a wealth of information for production planning, material flow and inventory control.

The detailed hybrid model as shown in Fig. 2 includes four main stages: (1) data collecting stage, (2) data classifying stage, (3) evolving fuzzy rule stage and (4) output forecasting stage. The hybrid model combining various soft computing approaches and has the capability of discovering the correlations between the input and output data that transcend the human intuition power. In addition, a SOM is adopted to reduce the interactions of FRB and genetic process is applied to further evolve FRB. The details of each stage are described in the following sections. In addition, the shaded part of Fig. 2 is illustrated in detail in Fig. 5.

![](/api/attachments/M374HDHF/fulltext/images/30f46cb31055789b72ebae5d21da5ea55df249ed2cbf79765b61807c40ac051d.jpg)  
Fig. 2. The framework of the hybrid model by clustering and evolving fuzzy rules.

![](/api/attachments/M374HDHF/fulltext/images/a64112c573e9350e5eb9a5279a82146d53697e7084537ca9539a4cc9e2b91629.jpg)  
Fig. 3. Variations of the historical monthly sales in Taiwan PCB company.

## 4.1. Data collecting stage

Monthly sales data from a real-world PCB Company in Taiwan from 1999/1 to 2003/12 have been collected for model training and testing. This paper follows an earlier research conducted by [5] applying Winter’s Exponential Smoothing to pre-process all the historical data. These preprocessed historical data address the effects of trend, seasonality and random noise and they are entered into the hybrid model as the input variable $X _ { 1 }$ . As for other endogenous and exogenous variables that will influence the sales demand of PCB, they are identified from the following three domains: macroeconomic data, downstream production data and industrial production data. Representative indexes screened by Grey Relation Analysis in [5] are selected from these three domains and they are consumer price index, $X _ { 2 }$ liquid crystal element demand $X _ { 3 } ,$ and PCB total production value $X _ { 4 } .$ These three representative indexes are also input into the hybrid model for monthly sales prediction.

Furthermore, the actual historical sales are assumed to be the output data y. All these data including input and output variables are shown in Appendix A. The variations of the historical monthly sales data from the subject PCB Company are shown in Fig. 3 and they are highly dynamic and nonlinear. Since fuzzy logic systems and neural networks are universal function approximators as described in [3,14,47], the adaptive control schemes of nonlinear systems that incorporate the fuzzy logic theory have grown rapidly as in [10,11,33–37,43,45]. Therefore, the fuzzy method is applied in this research to resolve this nonlinear sales forecasting problem. To forecast the next monthly sales, SOM is applied for data/rules clustering and a new test data will be clustered into one of these clusters. Then, the subset of fuzzy rules will be applied to forecast the sales of the test data. For a data point, these four input variables will be transformed into memberships of fuzzy sets by fuzzifying functions and for each term of an input variable, a membership value $\mu _ { \mathrm { T e r m } } ( X )$ is given to the scalar X. The fuzzifying process of these input and output variables and their corresponding figures are shown in Appendix B. Later on, a GA is applied for globally searching for the near-optimal number of fuzzy terms for each input variable.

![](/api/attachments/M374HDHF/fulltext/images/5107b01f266c103d4fe538f8475c84dc34f4f6b103ce32383394272bffd32490.jpg)

![](/api/attachments/M374HDHF/fulltext/images/cfcbb5915b429e147b3be20ad46ea7552ea70f47ac11785d855c8eeeebfab755.jpg)  
Fig. 4. Historical monthly sales clustered by SOM into two and three clusters.

![](/api/attachments/M374HDHF/fulltext/images/142d92cb8721b9b6d42cd15db6f518c7efaeebeed2260f672435ecaa3fb9da35.jpg)  
Fig. 5. The structure of Evolving Fuzzy Rule.

## 4.2. Data classification stage

For sales forecasting in printed circuit board industry, the first step is to classify the available data into different clusters, so that the data can be split into more homogeneous sub-populations. During the process of a FRB, each historical data represents an independent rule and it is also a final result from the output of these affecting variables, i.e., $X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 }$ . To forecast the next monthly sales from an original historical data set may not be as good as that of a small-sample data which can be more representative and similar to the current understudied environment. Therefore, this research tries to use fewer and more relative/representative data/rules to forecast the next monthly sales. Based on this viewpoint, the study applies SOM to classify the data/rules into different clusters first, then, according to the current input situation, the monthly sales of next time period can be generated only by applying a subset (cluster) of the fuzzy rules. As a result, the accuracy of the hybrid model can be further improved.

Self-organizing maps were introduced in [19], which represented the most popular artificial neural network methodology based on the unsupervised learning paradigm. The neurons of this neural network were arranged in a two-dimensional grid and there was a competition among those neurons to display the input patterns. An SOM placed similar patterns to contiguous locations in output space and provided projection and visualization options for high dimensional data. The main focus of the SOM was to summarize information while preserving topological relationships. The range of applications included: Pattern Recognition and Signal Processing, Optimization, Monitoring and Data Mining, Financial Analysis, Temporal Sequence Processing, Image Analysis and Vision as surveyed in [32]. During the training process, the neurons tended to represent statistical properties of the input data, maximally preserving the topology of the input space.

![](/api/attachments/M374HDHF/fulltext/images/10499fad946578fcdc2e9dc474d9001404ac278b82b1dfbf0bc85c9fb30673eb.jpg)  
Fig. 6. Chromosome encoding.

![](/api/attachments/M374HDHF/fulltext/images/61d23c82f0c2c7928892b0b413438e3265568a254b3055d0c74d1e36c75739f1.jpg)  
Fig. 7. The convergence of different population size and generation number.

SOM is applied in this research to divide the data into sub-populations and reduce the complexity of the whole data space to something more homogeneous. Detailed procedures of the SOM model are described in Appendix C.

Fig. 4 shows two different clustered diagrams: one in two clusters and the other in three clusters.

## 4.3. Fuzzy rules generation and evolution stage

The fuzzy modeling method proposed in [48] is applied for fuzzy rule generation. However, it has two major weaknesses: uniform partition of the domain space and arbitrary selection of the number of partitions. To rectify the second weakness, the Wang and Mendel (WM) method is evolved with genetic algorithms (GAs) and the idea is similar to evolving neural network presented in [29,49]. Essentially, a simple GA is used to determine the near-optimal number of fuzzy terms for each variable. The framework of Evolving Fuzzy Rule is shown in Fig. 5 and the detailed procedure of evolving FRB is described as follows:

## Step 1. Encoding:

Each sub-gene represents the number of fuzzy terms in different input and output variables $( X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 }$ and y). A chromosome is constructed from a series of sub-genes as shown in Fig. 6. For example, the first sub-gene in the chromosome represents the number of the fuzzy terms of $X _ { 1 } ,$ , the second is for $X _ { 2 } ,$ the third is for $X _ { 3 } ,$ , and the fourth is for $X _ { 4 }$ . Finally, the last subgene is the number of the fuzzy terms of $y .$ The binary code is used for each gene. Each variable is coded with three binary digits, which means that the range of the fuzzy terms in each variable is from 1 to 8.

## Step 2. Generate the initial population:

Initial chromosomes are randomly generated, and each of them is coded in binary; these initial solutions form the first population. GA operator will evaluate these chromosomes later.

## Step 3. Compute the objective value by WM method:

The WM method consists of five steps and the detailed procedures are described in Appendix D.

Table 1  
Signal levels and codes of factors

<table><tr><td>Factor</td><td>Crossover/(A)</td><td>Mutation/(B)</td><td>Replacement/(C)</td><td>Crossover rate/(D)</td><td>Mutation rate/(E)</td></tr><tr><td>Level 1</td><td>One point crossover</td><td>One point mutation</td><td>Totally replacement</td><td>0.2</td><td>0.1</td></tr><tr><td>Level 2</td><td>One point crossover</td><td>One point mutation</td><td>Totally replacement</td><td>0.4</td><td>0.3</td></tr><tr><td>Level 3</td><td>Two points crossover</td><td>Two point mutation</td><td>Elitist strategy</td><td>0.6</td><td>0.5</td></tr><tr><td>Level 4</td><td>Two points crossover</td><td>Two point mutation</td><td>Elitist strategy</td><td>0.8</td><td>0.7</td></tr></table>

S/N ratio of each factor  
Table 2

<table><tr><td>Factors</td><td>(A)</td><td>(B)</td><td>(C)</td><td>(D)</td><td>(E)</td></tr><tr><td>Level 1</td><td>30.75</td><td>33.29</td><td>27.82</td><td>23.18</td><td>33.74</td></tr><tr><td>Level 2</td><td>-</td><td>-</td><td>-</td><td>24.66</td><td>32.56</td></tr><tr><td>Level 3</td><td>32.25</td><td>28.47</td><td>32.45</td><td>27.34</td><td>31.48</td></tr><tr><td>Level 4</td><td>-</td><td>-</td><td>-</td><td>32.17</td><td>30.27</td></tr></table>

## Step 4. Compute the fitness function:

The original concept of fitness is <sup>b</sup>the larger the better<sup>Q</sup>, because solutions with larger fitness tend to propagate to the next generation. This paper considers the minimization of objectives; hence it contradicts the original idea of fitness. A transformation should be made to reverse the minimization to maximization. For a solution x, its fitness equals to the max value minus itself. The formula is given as:

$$
f i t (s) = \max - g (s)\tag{1}
$$

## Step 5. Reproduction/selection:

After the parameter design (please find details in Section 5), the roulette wheel selection described in Goldberg [9] is applied in this research. The probability p(s) of each chromosome s will be chosen to re-produce as defined below:

$$
p (s) = \frac {f i t (s)}{\sum f i t (s)}.\tag{2}
$$

## Step 6. Crossover:

After the parameter design, two-point crossover method is applied in the research.

## Step 7. Mutation:

After the parameter design, one-point mutation method is applied in the research.

## Step 8. Elite strategy:

The elite strategy retains the top 10% solutions in order to keep the quality solutions of each generation. Step 9. Replacement:

The new population generated by the previous steps updates the old population.

## Step 10. Stopping criteria:

If the number of generations equals to the maximum generation number, then stop; otherwise go to step 3.

Table 3  
RMSE of monthly sales prediction by WM and GA+WM models

<table><tr><td>Models</td><td>WM</td><td>GA+WM</td></tr><tr><td>RMSE</td><td>72221.42</td><td>32832.42</td></tr><tr><td>MAPE</td><td>0.089</td><td>0.038</td></tr><tr><td>Time (s)</td><td>0.0124</td><td>5.531</td></tr><tr><td>No. of rules</td><td>17</td><td>35</td></tr></table>

Table 4  
RMSE and MAPE of monthly sales prediction using SOM+GA+WM (two-cluster) model

<table><tr><td rowspan="2"></td><td colspan="3">SOM (2)+GA+WM</td></tr><tr><td>Cluster1</td><td>Cluster2</td><td>Total</td></tr><tr><td>RMSE</td><td>33,624.2</td><td>14,682.4</td><td>27,738.0</td></tr><tr><td>MAPE</td><td>0.034</td><td>0.019</td><td>0.025</td></tr><tr><td>Time (s)</td><td>1.015</td><td>2.375</td><td>3.390</td></tr><tr><td>No. of rules</td><td>13</td><td>26</td><td>39</td></tr></table>

## 4.4. Forecast stage

In this stage, two error measurements, i.e., RMSE (Root of Mean Square Error) and MAPE (Mean Absolute Percentage Error), are used to evaluate the accuracy of each forecast model.

## 5. Evolution of fuzzy rules

The performance of an FRB depends not only on the input variable selections but also on the generation of fuzzy rules. GA is applied to further improve the performance of the FRB generated. To properly setup the parameters in GA, Taguchi experiment design is applied in fine-tuning the parameters such as the number of populations, crossover rate, and mutation rate. Higher Signal-to-Noise (S/N) ratio presents the better parameter combination, which is defined as,

$$
S / N = - 1 0 \times \log \left(\frac {1}{n} \times \sum_ {i = 1} ^ {n} y _ {i} ^ {2}\right)\tag{3}
$$

where, n is the total number of experiment, $y _ { i }$ is the result of the ith test, $y _ { i } \in ( 0 , 1 ) , \forall i = 1 , 2 , . . . , n$ . Table 1 illustrates the signal levels and codes of each factor.

According to the convergence curve illustrated in Fig. 7, the model can converge after 20 generations even for small population size, 10. However, for a quick and smooth convergence according to the figure below, population 50 will be selected since the model can converge into a good steady state after 10 generations.

Table 5  
RMSEs and MAPEs of monthly sales prediction using GA+WM+ SOM (three-cluster) model

<table><tr><td rowspan="2"></td><td colspan="4">SOM (3)+GA+WM</td></tr><tr><td>Cluster1</td><td>Cluster2</td><td>Cluster3</td><td>Total</td></tr><tr><td>RMSE</td><td>12106.1</td><td>1076.0</td><td>32339.3</td><td>21346.0</td></tr><tr><td>MAPE</td><td>0.014</td><td>0.002</td><td>0.036</td><td>0.022</td></tr><tr><td>Time (s)</td><td>1.453</td><td>0.765</td><td>1.797</td><td>4.015</td></tr><tr><td>No. of rules</td><td>16</td><td>16</td><td>9</td><td>41</td></tr></table>

Table 7  
Table 6  
RMSE comparisons of various sales prediction models

<table><tr><td>Models</td><td>WM</td><td>GA+WM</td><td>SOM(2)+ GA+WM</td><td>SOM(3)+ GA+WM</td></tr><tr><td>RMSE</td><td>72221.42</td><td>32832.42</td><td>27738.0</td><td>21346.0</td></tr><tr><td>MAPE</td><td>0.089</td><td>0.038</td><td>0.025</td><td>0.022</td></tr><tr><td>Time (s)</td><td>0.012</td><td>5.531</td><td>3.390</td><td>4.015</td></tr><tr><td>No. of rules</td><td>17</td><td>35</td><td>39</td><td>41</td></tr></table>

Then repeat the experiment five times, and compute the S/N ratio of each factor in each level. The results are shown in Table 2.

From the table above, the best parameter combination is found as (A) 3–(B) 1–(C) 3–(D) 4–(E) 1. These codes represent two point crossover, one point mutation, and elitist strategy replacement with crossover rate = 0.8 and mutation rate = 0.1.

According to the setup described above, fuzzy rules are generated by applying WM model and GA to the set of data. The RMSE and MAPE of the WM and GA+WM models are shown in Table 3.

Originally, all variables including input and output are set up with three fuzzy terms and during the evolution process the number of terms will be changed, for example, form (3,3,3,3,3) to (3,2,4,3,4). Next, WM is applied again to generate a new FRB according to this new set of fuzzy terms. New forecasted sales for testing data are generated by applying this new FRB, and a new fitness value is calculated. Then a new evolution cycle starts again. Finally, after the evolution process, the near-optimal term set for the final output is 2, 3, 3, 2, and 6, which indicates: the first variable has two terms; the second variable has three terms, and the last variable has six terms.

Computational complexity of the hybrid model is an important research issue for algorithm development. The computational complexity of GA is O(MN<sup>2</sup>) where M is the number of individuals and N is the number of generations. The computational complexity of fuzzy rule generation is O(K) and K is the number of data. In our case, K will be 48 for training data. After combing these two methods together, the computational complexity of the hybrid model will be O(KMN<sup>2</sup>)which is bearable for experimental tests, since most soft computing methods are Meta heuristics and their computational times are tractable. The computational times of each model applied in the experiments are listed in the tables.

## 6. Experimental results and analysis

Commercial NN and language software, such as Neural Work Professional II Plus by Neural Ware and Borland C++ Builder 6.0 by Borland, are applied in the experiments with an Intel Pentium 2.4 G Hertz computer. Sixty historical monthly sales data are divided into two parts: the first 48 monthly sales are for training data and the last 12 monthly sales are for testing data. To test the performance of the hybrid model, the experiments are set up as described in the following sections.

## 6.1. Comparisons of WM, GA+WM and SOM+ GA+WM Models

To test the effectiveness of the SOM in clustering the FRBs, these 60 records of data are inputted into the SOM model and two different groups are generated: one is in two clusters and the other is in three clusters. Furthermore, the prediction accuracy before and after clustering is compared to demonstrate the performance improved by clustering rules.

## 6.1.1. SOM+GA+WM Model (two-cluster)

The fuzzy rule base clustered by the SOM into two clusters is applied to the testing data. The RMSE and MAPE of the test result are shown in Table 4.

## 6.1.2. WM and SOM method (three-cluster)

The fuzzy rule base clustered by the SOM into three clusters is applied to the testing data. The RMSE and MAPE of the test result are shown in Table 5.

Through the clustering of the FRB, the interaction between fuzzy rules can be reduced and the forecasted sales can be more accurately represented. From the experimental results shown in Tables 5 and 6, the comparison of GA+WM with and without the SOM clustering, the accuracy performance is improved in RMSE from 32832 down to 27738 (two clusters) and 21346 (three clusters) and in MAPE from 3.8% down to 2.5% (two clusters) and 2.2% (three clusters). The rule clustering does reduce the interaction between rules and each forecasted output is better represented by the sub-rulecluster. Therefore, the forecasted sales can have a better accuracy.

## 6.1.3. Comparisons of WM, GA+WM, and SOM + GA+ WM models

To test the performance among all these models, i.e., WM, GA+WM, and SOM+GA+WM, the data are in-

Comparison of hybrid model and multiple regression

<table><tr><td></td><td>Hybrid model</td><td>Multiple regression</td></tr><tr><td>MAPE</td><td>2.16%</td><td>9.10%</td></tr><tr><td>RMSE</td><td>21346.0</td><td>115334.40</td></tr><tr><td>Time (s)</td><td>4.015</td><td>&lt;1.0</td></tr></table>

Experimental design about BPN  
![](/api/attachments/M374HDHF/fulltext/images/dd6088b57a04c0453a5520612b14e48f6fa03b985f88c3a909d3dcdd93c16b00.jpg)  
Num. of neurons in the 1st and the 2nd hidden layer.

Fig. 8. Different structure designs of a BPN.

putted to these models and RMSEs and MAPEs are recorded for comparisons. The final result is shown in Table 6.

As shown in Table 8, the results of our comparative studies show that the hybrid model has the lowest RSME and MAPE values. In conclusion, the hybrid model generates not only human-understandable rules, but also more accurate predictions. The detailed forecasted results of each model are shown in Appendix E.

## 6.2. Comparison of hybrid model with multiple regression analysis

Those Input variables of the multiple regression model are the forecasted sales from Winter’s exponential smoothing $( X _ { 1 } ) _ { : }$ , Consumer Price Index $( X _ { 2 } )$ , liquid crystal element demand $( X _ { 3 } )$ and PCB Production Value $( X _ { 4 } )$ . The multiple regression formula is $Y { = } a _ { 1 } X _ { 1 } { + }$ $a _ { 2 } X _ { 2 } + a _ { 3 } X _ { 3 } + a _ { 4 } X _ { 4 } + b$ . Table 7 shows the errors, estimated by two different measures, MAPE and RMSE, from the hybrid model and multiple regression (95% confidence level).

As shown in the table above, the errors produced by using hybrid model are lower, which means that hybrid model is superior to multiple regression.

## 6.3. Comparison of hybrid model with BPN

The following setups are applied to fine tune the structure of the BPN: number of hidden layer: 1–2; number of neurons: 1–5.

The MAPE of each BPN structure is shown in Fig. 8, and the one with four neurons in the 1st hidden-layer and one neuron in the 2nd hidden-layer has the minimum MAPE performance.

The sigmoid function is used as the activation function between the input layer and the hidden layer. The Delta-Rule is used as the learning rule, where the learning ratio is 0.4, momentum is 0.5 and epoch size is 100,000. The structure design of the BPN has 4 input variables and one output and two hidden layers with 4 neurons in the first layer and one neuron in the second layer. The results are shown in Table 8 and the performance of the hybrid model is still better than BPN, however the computational time of the hybrid model is a little longer.

## 7. Conclusion

In this paper, a novel hybrid model is presented to help PCB companies in monthly sales forecasting. PCB companies can follow this sales forecasting model to make plans and to coordinate related production activities such as material management and production scheduling. There are several sources of variation affecting the sales prediction in PCB industries other than trend, seasonality and random noise; and these affecting factors are very difficult to identify.

A hybrid-modeling framework combining various soft computing approaches is proposed in this research to deal with the variations of the PCB monthly sales. An SOM neural network has been provided to cluster the fuzzy rules into sub-clusters. Through experiment, the interactions between rules can be reduced and the accuracy of the FRB can be further controlled by this rule clustering. Furthermore, genetic process is applied to evolve an FRB, thus a hybrid model with better performance is established.

Comparison of hybrid model and BPN

<table><tr><td></td><td>Hybrid Model</td><td>BPN</td></tr><tr><td>MAPE</td><td>2.16%</td><td>8.3846%</td></tr><tr><td>RMSE</td><td>21346.0</td><td>109467.08</td></tr><tr><td>Time (s)</td><td>4.015</td><td>0.510</td></tr></table>

The experimental results show that the performance of the hybrid model is superior to traditional statistical models, i.e., Multiple Regression and BPN. Thus, the effectiveness of the hybrid model is provided by the experimental results. However, the theoretical development of the validity of clustering FRB into sub clusters remains to be proven and that could be a future research topic. In practice, the successful application of this hybrid model provides a promising solution to the forecasting problems for relevant industries.

## Acknowledgments

The authors would like to thank three anonymous referees for their constructive comments. This research work was supported by the National Science of Council in Taiwan with the Contract No. NSC92-2213-E-155- 053. We also like to thank the Golden Circuit Company, Taiwan, for generously providing the past 5 years of historical sales data.

## Appendix A. Data of historical monthly sales and related variables

Historical monthly sales data and related input variables of Taiwan PCB company

<table><tr><td>Date</td><td> $X_{1}$ </td><td> $X_{2}$ </td><td> $X_{3}$ </td><td> $X_{4}$ </td><td>y</td></tr><tr><td>Oct-86</td><td>543,675</td><td>11,420,838</td><td>45,501</td><td>9252.8</td><td>553,678</td></tr><tr><td>Nov-86</td><td>491,465</td><td>10,503,706</td><td>36,465</td><td>8954.5</td><td>515,985</td></tr><tr><td>Dec-86</td><td>714,565</td><td>761,6493</td><td>40,177</td><td>10,253.2</td><td>748,610</td></tr><tr><td>Jan-87</td><td>642,222</td><td>8,674,804</td><td>23,527</td><td>7609.4</td><td>678,307</td></tr><tr><td>Feb-87</td><td>638,685</td><td>10,580,745</td><td>29,208</td><td>8155.5</td><td>678,763</td></tr><tr><td>Mar-87</td><td>741,159</td><td>9,102,389</td><td>36,497</td><td>8589</td><td>793,636</td></tr><tr><td>Apr-87</td><td>779,432</td><td>9,357,663</td><td>30,013</td><td>8189.7</td><td>834,252</td></tr><tr><td>May-87</td><td>738,308</td><td>9,111,833</td><td>26,029</td><td>8302</td><td>793,293</td></tr><tr><td>Jun-87</td><td>549,289</td><td>8,935,974</td><td>30,963</td><td>8555.8</td><td>613,227</td></tr><tr><td>Jul-87</td><td>723,844</td><td>9,632,109</td><td>31,186</td><td>9606.6</td><td>797,339</td></tr><tr><td>Aug-87</td><td>1,059,280</td><td>9,476,439</td><td>27,014</td><td>10,072.6</td><td>1,134,829</td></tr><tr><td>Sep-87</td><td>1,010,351</td><td>8,660,979</td><td>26,876</td><td>10,938.1</td><td>1,061,306</td></tr><tr><td>Oct-87</td><td>859,530</td><td>10,443,753</td><td>25,853</td><td>10,130.5</td><td>937,904</td></tr><tr><td>Nov-87</td><td>405,435</td><td>9,041,456</td><td>29,444</td><td>11,845.8</td><td>437,582</td></tr><tr><td>Dec-87</td><td>589,368</td><td>9,799,850</td><td>34,352</td><td>11,585.7</td><td>620,259</td></tr><tr><td>Jan-88</td><td>665,465</td><td>7,572,281</td><td>29,350</td><td>11,172.7</td><td>709,506</td></tr><tr><td>Feb-88</td><td>795,875</td><td>10,394,228</td><td>23,309</td><td>8973.1</td><td>842,393</td></tr><tr><td>Mar-88</td><td>891,553</td><td>9,149,164</td><td>39,387</td><td>12,231.9</td><td>926,282</td></tr></table>

Table 9 (continued)

<table><tr><td>Date</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td>y</td></tr><tr><td>Apr-88</td><td>1,003,783</td><td>10,327,938</td><td>37,966</td><td>11,153.6</td><td>1,029,183</td></tr><tr><td>May-88</td><td>996,677</td><td>9,846,491</td><td>39,251</td><td>10,716.6</td><td>1,005,137</td></tr><tr><td>Jun-88</td><td>884,111</td><td>9,957,870</td><td>42,141</td><td>11,474.2</td><td>874,773</td></tr><tr><td>Jul-88</td><td>1,089,077</td><td>10,705,240</td><td>43,888</td><td>12,208.2</td><td>1,057,271</td></tr><tr><td>Aug-88</td><td>1,194,111</td><td>9,846,958</td><td>42,368</td><td>12,984</td><td>1,144,526</td></tr><tr><td>Sep-88</td><td>939,783</td><td>11,464,267</td><td>36,933</td><td>13,049.6</td><td>899,864</td></tr><tr><td>Oct-88</td><td>590,234</td><td>11,553,682</td><td>38,323</td><td>14,010.4</td><td>420,119</td></tr><tr><td>Nov-88</td><td>549,685</td><td>11,025,265</td><td>37,857</td><td>14,652.6</td><td>558,776</td></tr><tr><td>Dec-88</td><td>688,075</td><td>11,865,047</td><td>38,336</td><td>14,753.7</td><td>687,149</td></tr><tr><td>Jan-89</td><td>444,248</td><td>9,045,674</td><td>36,115</td><td>14,043.9</td><td>422,863</td></tr><tr><td>Feb-89</td><td>498,017</td><td>11,949,390</td><td>29,902</td><td>10,564.8</td><td>492,605</td></tr><tr><td>Mar-89</td><td>594,095</td><td>12,255,430</td><td>41,972</td><td>13,957.1</td><td>613,800</td></tr><tr><td>Apr-89</td><td>480,354</td><td>13,137,517</td><td>38,432</td><td>14,185.1</td><td>519,449</td></tr><tr><td>May-89</td><td>697,069</td><td>12,391,860</td><td>43,372</td><td>15,332</td><td>779,520</td></tr><tr><td>Jun-89</td><td>500,890</td><td>13,573,099</td><td>43,294</td><td>15,679.2</td><td>595,869</td></tr><tr><td>Jul-89</td><td>601,759</td><td>12,746,544</td><td>45,183</td><td>17,849.1</td><td>711,963</td></tr><tr><td>Aug-89</td><td>613,572</td><td>12,933,210</td><td>41,329</td><td>17,856.2</td><td>744,712</td></tr><tr><td>Sep-89</td><td>441,666</td><td>13,657,784</td><td>36,453</td><td>17,969.7</td><td>598,816</td></tr><tr><td>Oct-89</td><td>626,008</td><td>12,723,275</td><td>36,087</td><td>18,737.8</td><td>601,675</td></tr><tr><td>Nov-89</td><td>516,689</td><td>12,091,034</td><td>33,912</td><td>19,681.4</td><td>494,645</td></tr><tr><td>Dec-89</td><td>682,209</td><td>9,827,088</td><td>29,759</td><td>17,971</td><td>666,988</td></tr><tr><td>Jan-90</td><td>723,786</td><td>10,126,016</td><td>26,388</td><td>13,957.3</td><td>720,610</td></tr><tr><td>Feb-90</td><td>798,539</td><td>11,718,515</td><td>31,541</td><td>14,032</td><td>772,659</td></tr><tr><td>Mar-90</td><td>711,118</td><td>10,841,181</td><td>37,485</td><td>14,848.4</td><td>654,890</td></tr><tr><td>Apr-90</td><td>799,637</td><td>101,49,935</td><td>31,449</td><td>13,752.3</td><td>740,697</td></tr><tr><td>May-90</td><td>837,546</td><td>10,327,190</td><td>30,017</td><td>13,170.5</td><td>759,466</td></tr><tr><td>Jun-90</td><td>372,758</td><td>9,704,380</td><td>25,954</td><td>12,590.8</td><td>298,746</td></tr><tr><td>Jul-90</td><td>651,528</td><td>9,445,136</td><td>25,495</td><td>13,668.8</td><td>612,528</td></tr><tr><td>Aug-90</td><td>529,568</td><td>8,854,962</td><td>28,534</td><td>14,979.2</td><td>512,144</td></tr><tr><td>Sep-90</td><td>725,386</td><td>11,435,107</td><td>32,410</td><td>13,972</td><td>736,557</td></tr><tr><td>Oct-90</td><td>649,700</td><td>10,172,510</td><td>33,092</td><td>16,063.5</td><td>649,066</td></tr><tr><td>Nov-90</td><td>465,219</td><td>10,268,871</td><td>34,143</td><td>15,201.7</td><td>466,750</td></tr><tr><td>Dec-90</td><td>623,542</td><td>9,682,218</td><td>33,504</td><td>12,620.4</td><td>633,615</td></tr><tr><td>Jan-91</td><td>681,530</td><td>8,042,396</td><td>31,840</td><td>14,072.8</td><td>693,946</td></tr><tr><td>Feb-91</td><td>783,733</td><td>11,446,863</td><td>25,360</td><td>11,702.7</td><td>785,838</td></tr><tr><td>Mar-91</td><td>693,935</td><td>10,858,289</td><td>39,323</td><td>15,491.4</td><td>679,312</td></tr><tr><td>Apr-91</td><td>753,675</td><td>11,039,892</td><td>34,471</td><td>15,182.1</td><td>723,914</td></tr><tr><td>May-91</td><td>800,210</td><td>11,225,384</td><td>36,726</td><td>15,722.5</td><td>757,490</td></tr><tr><td>Jun-91</td><td>949,143</td><td>11,141,761</td><td>31,605</td><td>14,084.9</td><td>836,846</td></tr><tr><td>Jul-91</td><td>1,019,900</td><td>10,887,644</td><td>35,040</td><td>14,763.8</td><td>833,012</td></tr><tr><td>Aug-91</td><td>1,100,546</td><td>11,251,648</td><td>33,425</td><td>14,413.6</td><td>860,892</td></tr><tr><td>Sep-91</td><td>1,189,945</td><td>11,483,422</td><td>34,849</td><td>14,905.8</td><td>912,182</td></tr></table>

## Appendix B. Membership functions of input and output variables

Assume the fuzzy term of each variable is three, and there are three different membership functions for each variable. Those fuzzy terms of each variable are defined as Low (L), Medium (M) and High (H), and their membership functions are shown as follows:

$$
\mu_ {\tilde {L}} (x _ {i}) = \left\{ \begin{array}{c c} 1 & , \quad x _ {i} \leq \min \\ \frac {\text { average } - x _ {i}}{\text { average } - \min} & , \quad \min \leq x _ {i} \leq \text { average } \\ 0 & , \quad x _ {i} \geq \text { average } \end{array} \right.\tag{4}
$$

![](/api/attachments/M374HDHF/fulltext/images/4a836bb90bf65d125eace2f15132787775a0e80f091d675865f5e3e81ac4fc9f.jpg)  
Fig. 9. The membership function of input variable $X _ { 1 }$

$$
\mu_ {\widetilde {M}} (x _ {i}) = \left\{ \begin{array}{c c c} 0 & , & x _ {i} \leq \min \\ \frac {\text { average } - x _ {i}}{\text { average } - \min} & , & \min \leq x _ {i} \leq \text { average } \\ 1 & , & x _ {i} = \text { average } \\ \frac {x _ {i} - \text { average }}{\max - \text { average }} & , & \text { average } \leq x _ {i} \leq \max \\ 0 & , & x _ {i} \geq \max \end{array} \right.\tag{5}
$$

$$
\mu_ {\widetilde {H}} (x _ {i}) = \left\{ \begin{array}{c c} 0 & , \quad x _ {i} \leq \text { average } \\ \frac {\max - x _ {i}}{\max - \text { average }} & , \quad \text { average } \leq x _ {i} \leq \max \\ 1 & , \quad x _ {i} \geq \max \end{array} \right.\tag{6}
$$

To calculate the membership value of each sample datum, the term with highest membership value is the representative one. It is shown as the following equation.

$$
\mu_ {\tilde {A}} (x _ {i}) = \text { maximize } \big (\mu_ {\tilde {L}} (x _ {i}), \mu_ {\widetilde {M}} (x _ {i}), \mu_ {\widetilde {H}} (x _ {i}) \big)\tag{7}
$$

The membership functions of each variable with three fuzzy terms are shown in Figs. 9–13.

## Appendix C. Detailed procedures of SOM model

The detailed procedures of SOM model are described as follows:

Step 1: Initialize each neuron weight $w =$ $\left[ w _ { 1 } , w _ { 2 } , \ldots , w _ { i j } \right] ^ { T } { \in } \mathfrak { R } ^ { j }$ . In this research, neuron weights are initialized by drawing random samples from input dataset.

![](/api/attachments/M374HDHF/fulltext/images/c608f5e4c8bf302628eb5f2a1504eedc682a32981e13186106bf534eb5d9058a.jpg)  
Fig. 10. The membership function of input variable $X _ { 2 } .$

![](/api/attachments/M374HDHF/fulltext/images/13f156b981b20b1556afe0e58d43fd2a4288bf33967ce9ffdff3772b215af55b.jpg)  
Fig. 11. The membership function of input variable $X _ { 3 } .$

Step 2: Present an input pattern $\begin{array} { r } { \boldsymbol { x } = [ x _ { 1 } , x _ { 2 } , } \end{array}$ $\dots , x _ { j } ] ^ { T } { \in } \Re ^ { j }$ . In this case, input pattern is a series of variables representing current shop floor status. Calculate the distance between pattern x, and each neuron weight $w _ { i }$ and therefore, identify the winning neuron or best matching unit c such as

$$
\left| \left| x - w _ {c} \right| \right| = \min _ {i} \left\{\left| \left| x - w _ {i} \right| \right| \right\}\tag{8}
$$

SOMToolbox employs Euclidian distance as the distance metric.

Step 3: Adjust the weights of winning neuron c and all neighbor units

$$
w _ {i} (t + 1) = w _ {i} (t) + h _ {c i} (t) [ x (t) - w _ {i} (t) ]\tag{9}
$$

where i is the index of the neighbor neuron and t is an integer, the discrete time coordinate. The neighborhood kernel $h _ { c i } ( t )$ is a function of time and the distance between neighbor neuron i and winning neuron $c h _ { c i } ( t )$ defines the region of influence that the input pattern has on the SOM and consists of two parts: the neighborhood function $h ( \parallel \cdot \parallel , \ t )$ and the learning rate function a(t), in Eq. (3).

$$
h _ {c i} (t) = h \left(\left| \left| r _ {c} - r _ {i} \right| \right|, t\right) \alpha (t)\tag{10}
$$

where r is the location of the neuron on two-dimensional map grids. In this work we used Gaussian Neighborhood Function. The learning rate function ${ \boldsymbol { \alpha } } ( t )$ is a decreasing function of time. The final form of the neighborhood kernel with Gaussian function is

![](/api/attachments/M374HDHF/fulltext/images/327efe8928d2663985e6fff401bc97b81cb12f64cde3e55ab23383368089465e.jpg)  
Fig. 12. The membership function of input variable $X _ { 4 } .$

![](/api/attachments/M374HDHF/fulltext/images/630c1ba7bd373414b196cda3a9b88277f4236b702116fe3b921a0926dd378b93.jpg)  
Fig. 13. The membership function of output variable y.

$$
h _ {c i} (t) = \exp \left(\frac {| | r _ {c} - r _ {i} | |}{2 \sigma^ {2} (t)}\right) \alpha (t)\tag{11}
$$

where $\alpha ( t )$ defines the width of the kernel.

Step4: Repeat steps 2 and 3 until the convergence criterion is satisfied.

## Appendix D. Detailed procedures of WM model

The detailed procedures of WM model are described in as follows:

Step 1: Divide the Input and Output Spaces into Fuzzy Regions.

Given a set of examples with multiple inputs (m) and single output, denoted as $( x _ { \mathrm { j } } ^ { k } ; y ^ { k } )$ where $j = 1 , . . . , m$ and $k ^ { = 1 , \dotsc , n }$ . Define the universe of discourse of each input variable as $[ x _ { j } ^ { - } ; x _ { j } ^ { + } ]$ and the output variable as $[ y ^ { - } ;$ $y ^ { + } ]$ and then divide each universe of discourse into N regions.

The minimal and maximal values of each variable are often used to define its universe of discourse. That is, $[ x _ { j } ^ { - } ; x _ { j } ^ { + } ] { = } [ \operatorname* { m i n } ( x _ { j } )$ , max(x )]. They are also considered to be the center of the left end term and the right end term, respectively. That is, $c _ { 1 j } = \operatorname* { m i n } ( x _ { j } )$ and $c _ { N j } { = } \operatorname* { m a x } ( x _ { j } )$ . Accordingly, the other term center, $c _ { i j } ,$ can be computed as follows:

![](/api/attachments/M374HDHF/fulltext/images/8956a098f154d783af486e179b8d9621f5734ceb15bc9004ec0a651bc35846bd.jpg)  
Fig. 14. Forecasted sales from multiple regressions.

![](/api/attachments/M374HDHF/fulltext/images/4657d86dc032491daddaaacf2141a1e74682dd277c45d0f06a94ec1bdd100907.jpg)  
Fig. 15. Forecasted sales from Winter’s exponential smoothing.

$$
\begin{array}{l} c _ {i j} = \min (x _ {j}) + i (\max (x _ {j})) \\ \quad - \min (x _ {j})) / (N - 1), \text { where } i = 2, \dots , N - 1 \end{array}\tag{12}
$$

Step 2: Generate fuzzy rules from given examples.

Firstly, determine the membership degrees of each example belonging to each fuzzy term defined for each region, variable by variable (including the output variable). Secondly, associate each example with the term having the highest membership degree variableby-variable, denoted as $m d _ { j } .$ . Finally, obtain one rule for each example using the term selected in the previous step. The rules generated are <sup>b</sup>and<sup>Q</sup> rules and the antecedents of the IF part of each rule must be met simultaneously in order for the consequent of the rule to occur. Letting $T x _ { j }$ be a term selected for variable $x _ { j }$ of an example, a rule could look like:

![](/api/attachments/M374HDHF/fulltext/images/d1f58df017a722f9fa0c5d50cf55b6110235c5fbb494d4d66c94e19fc2906256.jpg)  
Fig. 16. Forecasted sales from BPN.

![](/api/attachments/M374HDHF/fulltext/images/0e9bfc6f5f2af9fbda05526928130a164653ad50e5bdddf167a50219af69d7d4.jpg)  
Fig. 17. Forecasted sales from GA+W&M.

$$
\begin{array}{l} \text {   If   } x _ {1} \text {   is   } T x _ {1} (\text {   with   } m d _ {1}) \text {   and   } x _ {2} \text {   is   } T x _ {2} (\text {   with   } m d _ {2}) \text {   and   } \dots \\ \text {   and   } x _ {m} \text {   is   } T x _ {m} (\text {   with   } m d _ {m}) \\ \text {   THEN   } y \text {   is   } T y (\text {   with   } m d _ {y}). \end{array} \tag {13}
$$

Step 3: Assign a degree to each rule.

The rule degree is computed as the product of the membership degree of all variables. Let $D ^ { \hat { k } }$ be the degree of the rule generated by example k. Mathematically,

$$
D ^ {k} = \prod_ {j = 1, \dots , m \text { and } y} m d _ {j} ^ {k}.\tag{14}
$$

The degree of a rule generated by an example indicates our belief of its usefulness.

Step 4: Create a combined fuzzy rule base.

When the number of examples is high, it is quite possible that the same rule could be generated for more than one example. These rules are redundant rules. In addition, rules with the same if part but a different then part could also be generated. These rules are conflicting rules. The redundant and conflicting rules must be removed to maintain the integrity of the rule base. This is achieved by keeping only the rule with the highest degree for each fuzzy region: this rule is deemed most useful.

![](/api/attachments/M374HDHF/fulltext/images/2afbb90fbd268f634bbafedaf3e1ee705e9a430d751a875c9d9522a34be3bca6.jpg)  
Fig. 18. Forecasted sales from hybrid model (2 clusters).

![](/api/attachments/M374HDHF/fulltext/images/517991f55fde00670f3564e33622c7324a3705363eda1723e1c22c1789460191.jpg)  
Fig. 19. Forecasted sales from hybrid model (3 clusters).

Up to this step, the fuzzy rule base is complete; however, the usefulness of the rule base must be shown using some fuzzy inference method, as introduced in the next step.

Step 5. Determine a mapping based on the combined fuzzy rule base.

To predict the output of an unseen example denoted as $x _ { \mathrm { j } } ,$ the centroid defuzzification formula is used. Accordingly, the predicted output, y, is computed as

$$
\hat {y} = \sum_ {r = 1} ^ {R} a m d ^ {r} c ^ {r} / \sum_ {r = 1} ^ {R} a m d ^ {r}\tag{15}
$$

where $\begin{array} { r } { a m d ^ { r } = \prod _ { j = 1 , m } m d _ { j } ^ { r } ; c ^ { r } } \end{array}$ is the center value of the consequent term of rule $r ;$ and R denotes the total number of combined rules.

Step 6. Calculate the RMSE.

In this research, RMSE is set as the objective function to evaluate the deviation of the training data, which is computed as the objective $g ( s ) { \mathrm { o f } }$ each chromosome s.

$$
\begin{array}{l} g (s) = \text { RMSE } = \sqrt {\frac {1}{n} \sum_ {t = 1} ^ {n} (F _ {t} - A _ {t}) ^ {2}}, s \\ = 1, 2, \ldots , N _ {\text { pop }} \end{array}\tag{16}
$$

## Appendix E. Forecasted results of each model

Detailed forecasted results of each model are depicted and shown in Figs. 14–19.

## References

[1] R.E. Abdel-Aal, A.Z. Al-Garni, Forecasting monthly electric energy consumption in eastern Saudi Arabia using univariate time series analysis, Energy 22 (1997) 1059– 1069.

[2] D.G. Burkhardt, P.P. Bonissone, Automated fuzzy knowledge base generation and tuning, Proc. 1992 IEEE Int. Conf. Fuzzy Systems, San Diego, CA, 1992, pp. 179– 188.

[3] J.L. Castro, Fuzzy logic controllers are universal approximators, IEEE Transactions on Systems, Man, and Cybernetics 25 (4) (1995) 629–635.

[4] P.C. Chang, J.C. Hsieh, A Neural network approach for due-date assignment in a wafer fabrication factory, International Journal of Industrial Engineering 10 (2003) 55–61.

[5] P.C. Chang, Y.W. Wang, C.Y. Tsai, Evolving neural network for printed circuit board sales forecasting, Expert Systems with Applications 29 (1) (2005) 83–92.

[6] C.W. Chase, Ways to improve sales forecasts, Journal of Business Forecasting 12 (3) (1993) 15– 17.

[7] T.W.S. Chow and C.T. Leung, Nonlinear autoregressive integrated neural network model for short-term load forecasting, IEE Proceeding Online no. 19960600, 500–506, 1996.

[8] M.M. Florance, M.S. Sawicz, Positioning sales forecasting for better results, Journal of Business Forecasting 12 (4) (1993) 27–28.

[9] D.A. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison-Wesley, Reading, MA, 1989.

[10] N. Golea, A. Golea, K. Benmahammed, Stable indirect fuzzy adaptive control, Fuzzy Sets and Systems 137 (2003) 353– 366.

[11] E.T. Hancock, F. Fallside, Stable control of nonlinear systems using neural networks, Robust Nonlinear Control 2 (1992) 63– 68.

[12] T.P. Hong, J.B. Chen, Finding relevant attributes and membership functions, Fuzzy Sets and Systems 103 (3) (1999) 289– 404.

[13] T.P. Hong, J.B. Chen, Processing individual fuzzy attributes for fuzzy rule induction, Fuzzy Sets and Systems 112 (1) (2000) 127–140.

[14] K. Hornik, Multilayer feedforward networks are universal approximators, Neural Networks 2 (1989) 359–366.

[15] P.H. Hsu, C.H. Wang, Joseph Z. Shyu, H.C. Yu, A Litterman BVAR approach for production forecasting of technology indus tries, Technological Forecasting & Social Change 70 (2002) 67–82.

[16] H. Ishibuchi, K. Nozaki, N. Yamaoto, H. Tanaka, Selecting fuzzy if-then rules for classification problems using genetic algorithms, IEEE Transactions on Fuzzy Systems 3 (3) (1995) 260–270.

[17] C.H. Kao, S.M. Chen, A new method to generate fuzzy rules from training data containing noise for handling classification problems, Proc. 5th Conf. Artificial Intelligence and Applications, Taipei, Taiwan, R.O.C., 2000, pp. 323–331.

[18] T. Kimoto, K. Asakawa, Stock market prediction system with modular neural network, IEEE International Joint Conference on Neural Network, 1990, pp. 1 –6.

[19] T. Kohonen, Self-organized formation of topologically correct feature maps, Biological Cybernetics 43 (1982) 59 – 69.

[20] H.M. Krolzig, J. Toro, Multiperiod forecasting in stock markets: a paradox solved, Decision Support Systems 37 (2004) 531– 542.

[21] R.J. Kuo, A sales forecasting system based on fuzzy neural network with initial weights generated by Genetic Algorithm, European Journal of Operational Research 129 (2001) 496– 517.

[22] R.J. Kuo, J.A. Chen, A decision support system for order selection in electronic commerce based on fuzzy neural network supported by real-coded genetic algorithm, Expert Systems with Application 26 (2004) 141– 154.

[23] R.J. Kuo, K.C. Xue, A Decision Support System for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 (1998) 105– 126.

[24] R. Law, N. Au, A neural network model to forecast Japanese demand for travel to Hong Kong, Tourism Management 20 (1999) 89– 97.

[26] J.T. Luxh, Jens O. Riis, Brian Stensballe, A hybrid econometricneural network modeling approach for sales forecasting, International Journal of Production Economics 43 (1996) 175– 192.

[27] S. Menard, Applied Logistic Regression Analysis Series: Quantitative Applications in the Social Sciences, Sage, Thousand Oaks, CA, 1993.

[28] G.G. Meyer, Marketing research and sales forecasting at Schlegel Corporation, Journal of Business Forecasting 12 (2) (1993) 22–23.

[29] D. Montana, L. Davis, Training feed forward neural networks using genetic algorithms, Proceedings of 11th International Joint Conference on Artificial Intelligence, Morgan Kaufmanns, San Mateo, CA, 1989, pp. 762–767.

[31] J. Neter, W. Wasserman, M.H. Kutner, Applied Linear Statistical Models, 2nd ed., Richard D. Irwin Inc., Homewood, IL, 1985.

[32] M. Oja, S. Kaski, T. Kohonen, Bibliography of self-organizing map (SOM) papers: 1998–2001 addendum, Neural Computing Surveys 3 (2003) 1– 156.

[33] J.-H. Park, S.-H. Kim, Direct adaptive output-feedback fuzzy controller for nonaffine nonlinear system, IEE Proceedings.— Control Theory Application 151 (1) (2004) 65–72.

[34] J.-H. Park, G.-T. Park, Robust adaptive fuzzy controller for nonaffine nonlinear systems with dynamic rule activation, International Journal of Robust and Nonlinear Control 13 (2) (2003) 117– 139.

[35] J.-H. Park, G.-T. Park, Adaptive fuzzy observer with minimal dynamic order for uncertain nonlinear systems, IEE Proceedings.—Control Theory Application 150 (2) (2003) 189– 197.

[36] J.-H. Park, S.-J. Seo, G.-T. Park, Robust adaptive fuzzy controller for nonlinear system using estimation of bounds for approximation errors, Fuzzy Sets and Systems 133 (1) (2003) 19– 36.

[37] M.U. Polycarpou, M.J. Mears, Stable adaptive tracking of uncertain systems using nonlinearly parameterized on-line approximators, International Journal of Control 70 (3) (1998) 363–384.

[38] V. Ravi, P.J. Reddy, H.-J. Zimmermann, Fuzzy rule base generation for classification and its minimization via modified threshold accepting, Fuzzy Sets and System 120 (2) (2001) 271–279.

[39] Dipti Srinivasan, Evolving artificial neural networks for short term load forecasting, Neural Computing 23 (1998) 265– 276.

[40] M. Tawfik, Sales forecasting practices of egyptian public enterprises: survey evidence, International Journal of Forecasting 16 (2000) 359– 368.

[41] A.S. Tawfiq, E.A. Ibrahim, Artificial neural networks as applied to long-term demand forecasting, Artificial Intelligence in Engineering 13 (1999) 189– 197.

[42] S. Thomassey, M. Happiette, J.M. Castelain, A global forecasting support system adapted to textile distribution, International Journal of Production Economics 96 (2005) 81– 95.

[43] S. Tong, H.-H. Li, Observer-based robust fuzzy control of nonlinear systems with parametric uncertainties, Fuzzy Sets and Systems 131 (2002) 165–184.

[45] L.X. Wang, Stable adaptive fuzzy controllers with application to inverted tracking, IEEE Transactions on Fuzzy Systems 26 (5) (1996) 677–691.

[46] L.X. Wang, J. Hong, Learning optimization in simplifying fuzzy rules, Fuzzy Sets and Systems 106 (3) (1999) 349–356.

[47] L.-X. Wang, J.M. Mendel, Fuzzy basis functions universal approximation, and orthogonal least square learning, IEEE Transactions on Neural Network 3 (5) (1992) 807– 814.

[48] L.X. Wang, J.M. Mendel, Generating fuzzy rules by learning from examples, IEEE Transactions On Systems, Man, and Cybernetics 22 (6) (1992) 1414– 1427.

[49] X. Yao, Evolving artificial neural networks, Proceedings of the IEEE 87 (9) (1999) 1423– 1447.

[50] Y. Yuan, M.J. Shaw, Induction of fuzzy decision trees, Fuzzy Sets and Systems 69 (1995) 125– 139.

[51] L.A. Zadeh, Fuzzy sets, Information Control 8 (1965) 338 – 353.

![](/api/attachments/M374HDHF/fulltext/images/495770fbdbe7e9d309f16fcaca00adaffbcbd7ef06ca3b7d88bfd7c14ae87950.jpg)

Dr. P. C. Chang received his M.S. and Ph.D. from the department of Industrial Engineering at Lehigh University in 1985 and 1989. He is a professor in the department of Industrial Engineering and Management of Yuan-Ze University in Taiwan. His research fields covers Production Scheduling, Forecasting, Case Based Reasoning, ERP, and Applications of Soft Computing. He published in several SCI Journals, such as, Expert Systems with Applications, European Journal of

Operational Research, Applied Soft Computing, Journal of Intelligent Manufacturing, Computers and Industrial Engineering, International Journal of Production Economics, Computers and Mathematics with Applications, Computers and Operations Research, etc.

![](/api/attachments/M374HDHF/fulltext/images/6144f84c05e02dfd9767a54ebc0078022942fd894264bc2ea4b1db4fa2191735.jpg)  
Mr. C. H. Liu is a PhD student from the department of Industrial Engineering at Yuan Ze University in Taiwan. He is interested in Production Scheduling, Applications of Soft Computing, Multi-Objective Optimization Problems and Multi-Criteria Decision Making.

![](/api/attachments/M374HDHF/fulltext/images/4e385cb9cf43eeea1d6763e6a67c0ce4544635095113a10cd5cc5890b2de05f7.jpg)  
Mr. Y. W. Wang is a PhD student from the department of Industrial Engineering at Yuan Ze University in Taiwan. He is interested in Production Scheduling, Applications of Artificial Intelligence, Forecasting and Global Logistics.
