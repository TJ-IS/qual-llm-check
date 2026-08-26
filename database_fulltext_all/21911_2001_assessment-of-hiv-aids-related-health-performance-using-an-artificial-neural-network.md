---
otero_id: 21911
otero_key: "BJGR3JNJ"
title: "Assessment of HIV/AIDS-related health performance using an artificial neural network"
authors: "Chang W. Lee; Jung-A Park"
year: "2001"
journal: "Information & Management"
doi: "10.1016/s0378-7206(00)00068-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessment of HIV/AIDS-related health performance using an artificial neural network

Chang W. Lee $^{a,*}$ , Jung-A Park $^{b}$

$^{a}$ Department of Business Administration, Chinju National University, Chinju 660-758, South Korea $^{b}$ Institute of Food and Nutrition Science, Keimyung University, Taegu 704-200, South Korea

Received 30 October 1999; received in revised form 11 April 2000; accepted 7 August 2000

## Abstract

This paper presents an application of neural networks to classify and predict the symptomatic status of HIV/AIDS patients. The purpose of this study is to apply an artificial neural network (ANN) to provide correct classification of AIDS versus HIV status patients. An ANN model is developed using publicly available HIV/AIDS data in the AIDS Cost and Services Utilization Survey (ACSUS) datasets as input and output variables. The proposed model:

1. demonstrates which factors will affect classification of AIDS and HIV status;

2. reinforces HIV/AIDS patient prevention and care planning and strategies to meet more appropriately health-care policy and regulations;

3. provides decision-makers and policy-makers with more accurate information to allow them to implement better health-care systems.

Several different neural network topologies are applied to the datasets. A neural network model was developed to classify both the HIV and AIDS status of patients and analyzed in terms of validity and reliability of the test in order to demonstrate the model capability. The ANN model can facilitate planning, decision-making, and managerial control by providing hospital administration information. © 2001 Elsevier Science B.V. All rights reserved.

Keywords: Computer utilization; Data management; Decision-making performance; Predictive model; Task uncertainty

## 1. Introduction

In the early 1970s, the idea of a neural network was viewed as a theoretical foundation for building machine learning systems. It was proven to have many limitations. Recent neural network research has overcome some early limitations. One of the advanced features is the development of a back propagation algorithm (BPA) in a learning mechanism to train multi-layer networks. The BPA using the hidden layer allows the data to be classified.

Appropriate use of an artificial neural network (ANN) model to implement a large-scale health services research dataset is most difficult. Moreover, if attributes of the factors are ill defined and/or ill-structured, finding a solution will be very difficult and complicated. Many studies have applied an ANN model to classify and to predict desired solutions or to improve methodological aspects. In spite of the successful application in such models, scant attention has been made to the HIV/AIDS prevention and care planning area. Recently, a study of an ANN application to the classification of the functional health status of AIDS/HIV patients was explored. However, the utilization of ANN models in classification issues of business, health services research, and others have been generally limited to the adoption of factors with continuous or ratio variables, rather than the categorized values found in socioeconomic or demographic variables $[8,9,13,24,28]$ .

The purpose of this study is to apply an ANN to produce a good discriminator between HIV and AIDS status. An ANN model is developed based on the publicly available HIV/AIDS data of AIDS Cost and Services Utilization Survey (ACSUS) data as input and output variables.

## 2. The artificial neural network and its literature

## 2.1. Artificial neural network

An ANN is a mechanism that imitates human intelligence for the purpose of deriving certain performance characteristics. The ANN is normally developed as a generalization of a nonparametric methodology. The ANN model assumes that

1. neurons (i.e. nodes) have their own values for data processing;

2. values are passed through neurons over connection links;

3. each link has a weight, which multiplies the values transmitted in a neural network; and

4. each neuron applies an activation function to its input to determine its output value $[4,18,25,29]$ .

An ANN consists of a number of data processing layers interconnected in a network. Each layer is a computational mechanism with mathematical functions. A layer receives input values from one layer and aggregates input values based on an input function. Then, the layer generates output values based on an output function. The output values are then routed to other layers, as designed by the architecture of the network.

An ANN is characterized by the pattern of connections between the nodes (called its architecture), the method of determining the weights on the connections (called its training or learning), and the activation function. Each node is connected to other nodes by means of direct communication links, each with an associated weight. This weight represents information being used by the net to solve a problem. Each node has an activation or activity level, which is a function of the inputs. Because a node sends its activation as a value to several other nodes, it is able to send one value at a time, while the value is sent to several other nodes.

Early studies recognized that combining many simple nodes (or neurons) into neural network systems was the source of increased computational power. The weights on the neural network are set so that the node performs a particular logic function, along with different nodes performing different functions. The nodes can be arranged into a net to produce any output that can be represented as a combination of logic functions. A learning law has been designed for ANN: if two nodes are active simultaneously, then the strength of the connection between them should be increased. The idea is closely related to a correlation matrix learning mechanism.

The flow of information through the network assumes a unit time step for data to travel from one node to the next. This lead-time allows the network to model some perceptual processes. The most typical “perceptron (or single layer networks)” consisted of an input layer connected by paths with fixed weights to associated nodes. The weights on the connection paths are adjustable. The perceptron learning rule uses an iterative weight adjustment. Perceptron learning can converge to the correct weights if the weights allow the network to reproduce correctly all of the training input and target output pairs. However, the mathematical proof of the convergence of iterative learning under suitable assumptions demonstrates the limitations on what perceptron networks can learn.

A least-mean-squares rule, an alternative-learning rule, adjusts the connection weights to a unit whenever the response of the unit is incorrect. The response indicates a classification of the input pattern. The least-mean-squares rule (or delta rule) adjusts the weights to reduce the difference between the input and the target output. This leads to the smallest mean-squared error (MSE). The learning rule for a single-layer and multi-layers networks is interpreted as an adaptive linear system. The difference in learning rule results in greater ability of the network to generalize.

More advanced studies deal with associative memory neural networks, along with the development of self-organizing feature maps that use a topological structure for the cluster units. This feature truncates the linear output to prevent the output from becoming too large to reach a stable solution (or an optimal solution) as the network iterates.

A back propagation method has been developed to overcome the failure of single-layer networks. It can solve complex problems, lacking a general method of training a multilayer network. This model is derived from a number of neural networks, based on fixed weights and adaptive activation. These networks can serve as associative memory nets and can be used to solve constraint satisfaction problems. The development of stochastic neural networks, in which weights or activations are changed on the basis of a probability density function, incorporates such ideas as simulated annealing and Bayesian decision theory.

## 2.2. Related literature

Since the development of the ANN, it has received considerable attention and has been applied to a variety of problems in classification and prediction. Neural networks (NN) have been applied successfully for development of nonparametric statistical models. More reliable outcome research has been explored in the area of pattern classification and pattern prediction. An ANN model is able to recognize and to predict an existing pattern of data in different categories, assisting decision-makers $[2,22,27]$ .

Neural networks in health-care applications have been used for clinical diagnosis $[3,7]$ , HIV-structure analysis $[1]$ , HIV/AIDS functional health status $[16]$ , image analysis $[6]$ , prediction of cancer $[10,23]$ , prediction of length of stay $[5,19,26]$ , sequence analysis $[11]$ , and speech recognition $[15]$ . Business applications of neural networks are also found in areas such as audit decision $[12,17]$ , initial public offerings $[14]$ , and multi-criteria decision making $[20]$ .

## 3. Model development

## 3.1. Data collection

ANN modeling of HIV/AIDS classification involves the interaction of many diverse variables. Its relationships are often ill defined and/or ill structured so that the classification of outcomes is very difficult and complicated. This study utilizes the ACSUS dataset, which is the outcome of a longitudinal study of persons with HIV/AIDS-related diseases from 10 US cities. Information was gathered on 1949 HIV/AIDS-infected persons in a series of interviews over a total of six time-periods with quarterly follow-up surveys from 1 March 1991 to 31 August 1992. After collecting information on demographic and functional health status, interviewers contacted clinical and other medical service providers, identified by the study subject, twice during the six time periods to collect relevant information.

Patterns of use of health services and changes in these factors over the course of the disease can be analyzed for HIV/AIDS-infected persons receiving care. Initially, 20 variables were selected for this study from the original dataset. After filtering them, one dependent variable (output variable) and nine independent variables (input variables) were selected after controlling them by the variance inflation factor (VIF) method for detecting multicollinearity between input variables. Out of 1949 cases, 1171 subjects were selected as valid cases, implying a person had either on HIV status or on AIDS status.

These selected cases provided valid information based on the responses of specific patients (i.e. cases were excluded if their responses were Don't Know, Refused, or any other inappropriate ones). Thus, 1171 cases have complete information on each patient, based on the selected input and output variables. The descriptive statistics for input and output variables are presented in Table 1.

## 3.2. Neural network modeling

The model developed to classify a current symptomatic status of HIV/AIDS-related patients involves the three-layer back-propagation algorithm. An input layer is used to represent a set of input variables. An output layer is used to represent the output variable. The hidden layer has an arbitrary number of hidden nodes. Thus, the number of hidden nodes is chosen arbitrarily and they derive different possible results.

<table><tr><td>Variablea</td><td>Mean</td><td>M.S.E.</td><td>S.D.</td><td>Min</td><td>Max</td><td>N</td></tr><tr><td>CSS</td><td>0.43</td><td>0.02</td><td>0.50</td><td>0</td><td>1</td><td>1171</td></tr><tr><td>Sex</td><td>0.84</td><td>0.01</td><td>0.37</td><td>0</td><td>1</td><td>1171</td></tr><tr><td>Race</td><td>1.78</td><td>0.02</td><td>0.81</td><td>1</td><td>3</td><td>1171</td></tr><tr><td>EXPRO</td><td>1.87</td><td>0.02</td><td>0.64</td><td>1</td><td>4</td><td>1171</td></tr><tr><td>ADMT</td><td>1.61</td><td>0.09</td><td>2.94</td><td>0</td><td>78</td><td>1171</td></tr><tr><td>IPNGTT</td><td>17.8</td><td>0.91</td><td>31.1</td><td>0</td><td>235</td><td>1171</td></tr><tr><td>AMVST</td><td>25.5</td><td>0.66</td><td>22.7</td><td>0</td><td>218</td><td>1171</td></tr><tr><td>ERVST</td><td>2.02</td><td>0.08</td><td>2.83</td><td>0</td><td>37</td><td>1171</td></tr><tr><td>HCVST</td><td>15.6</td><td>0.54</td><td>18.3</td><td>0</td><td>218</td><td>1171</td></tr><tr><td>MDVST</td><td>6.75</td><td>0.34</td><td>11.7</td><td>0</td><td>78</td><td>1171</td></tr><tr><td colspan="7">aVIF values &lt; 1.700 for multicollinearity diagnosis; CSS: current symptomatic status; EXPRO: exposure route; ADMT: total number of patient admission; IPNGTT: total number of inpatient nights; AMVST: total number of ambulatory visits; ERVST: total number of emergency room visits; HCVST: total number of hospital clinic visits; MDVST: total number of private physician visit.</td></tr></table>

Table 1  
Descriptive statistics of input and output variables

For the purpose of this study, categories in output variables have been recoded as follows.

\- For the first node in the output layer, the output is zero if the current symptomatic status is HIV, and 1 if the current symptomatic status is AIDS; and

\- For the second node in the output layer, the code is assigned in the reverse way.

Table 2 presents descriptions of the input and output variables in the model.

Since no prior information is available on how the layers should be connected in the three-layer network, all nodes in the two adjacent layers are fully connected to each other. Fig. 1 shows the neural network topology.

The input pattern has 15 nodes. Each of these variables is entered into the corresponding input layer of the network. They are then multiplied by computer-generated random numbers, resulting in the input values of the hidden layer. Each value is placed in a logistic function that computes the net activation of the hidden layer, becoming input values of the output layer. This value is entered into the same logistic function that computes the activation of the output layer, resulting in the output values: HIV status or AIDS status. Thus, in practice, the output values could be considered as representing the likelihood of HIV status or AIDS status in the current symptomatic status of each HIV/AIDS patient.

<table><tr><td>Table 2Summary of input and output variables</td></tr><tr><td>Input variablesSexS-male (1 if male, or 0 otherwise)S-female (1 if female, or 0 otherwise)RaceR-white (1 if white, or 0 otherwise)R-black (1 if black, or 0 otherwise)R-Hispanic (1 if Hispanic, or 0 otherwise)Exposure routeE-homo (1 if exposure route is homosexual/bisexual, or 0 otherwise)E-IDU (1 if exposure route is IV drug user, or 0 otherwise)E-IV (1 if exposure route is IV, or 0 otherwise)E-hetero (1 if exposure route is heterosexual, or 0 otherwise)Medical recordsADMT: total number of patient admissionIPNGTT: total number of inpatient nightsAMVST: total number of ambulatory visitsERVST: total number of emergency room visitsHCVST: total number of hospital clinic visitsMDVST: total number of private physician visit</td></tr><tr><td>Output variableCSS: current symptomatic status (CSS is either HIV status or AIDS status)</td></tr></table>

The network architecture is designed to be a three-layer BPA network. The BPA has a linear approximation function for the input layer and a logistic function for the output layer. After configuring the network, a learning rate, initial weight, and momentum-learning epoch are assigned to the model to initiate the training. Since assigning a learning rate, momentum, and number of epoch is arbitrary, a certain value is assigned as a default for each in the model. Once the model is designed, a certain percent of the total is extracted for the training set and the rest become the test set. An epoch is considered completed after the network examines all the input and output patterns for all the training sets. Epochs for training set are repeated 200 times as a learning rate. In order to avoid the overfitting the network, the learning process was stopped when the total number of epoch repeats reached 20,000. A software system, NeuroShell $^{®}$ 2, was utilized to conduct this study [21]. Table 3 gives a summary of the BPA network modeling.

![](/api/attachments/BJGR3JNJ/fulltext/images/e74b11c305cc79058f25f492a44e9c8feaca7eeafe7c405c1129e17f11a49b18.jpg)  
Fig. 1. Neural network topology.

Table 3  
Summary for the BPA neural network system

<table><tr><td>NN modeling</td><td>Parameters</td></tr><tr><td>Total pattern</td><td>1171</td></tr><tr><td>Training set</td><td>1026</td></tr><tr><td>Test seta</td><td>145 with 20,000 events</td></tr><tr><td>Pattern selection</td><td>Random</td></tr><tr><td>Weight updates</td><td>Momentum with 0.1</td></tr><tr><td>Learning epoch</td><td>200 with learning rate 0.1</td></tr><tr><td>Initial weight</td><td>0.3</td></tr><tr><td>Hidden nodes</td><td>3, 5, 7, 10</td></tr></table>

$^{a}$ Approximation of 10% random extraction from the total pattern.

## 4. Model analysis and discussion

In order to analyze the model result, a network topology must be selected. Since there is no formal way to select it, some trial experiments were performed to show different possible outcomes under different topologies. A test set of 145 patients was used to examine the performance of the neural network model. A variety of tests were then performed to analyze the model. The training ended when the number of events of the minimum test set error exceeded 20,000, as specified in the mode design. Table 4 presents a summary of model statistics with respect to different numbers of hidden nodes (i.e. H=3, H=5, H=7, and H=10) in hidden layer.

In the case where the hidden layer has five nodes $(H_{5})$ , the L.A.E. and M.A.E. have the lowest values of 0.277 and 0.268, respectively. All model with different hidden nodes show the different best test set event, $(H_{3}=60,200, H_{5}=79,600, H_{7}=53,200,$ and $H_{10}=43,400)$ and the epochs are also different with a minimum average error $(H_{3}=17, H_{5}=7, H_{7}=10, H_{10}=1)$ .

Table 5 illustrates the relative contribution between input and output variables. In this table, the BPA network model with different hidden nodes presents similar results. The model shows variables with the relative contributions. Among these high contribution variables, IPNGTT (total number of inpatient night) is the most significant factor in classifying HIV versus AIDS status. Different hidden nodes resulted in different relative contributions among input variables.

Two aspects of the objective tests are important in this study: validity and reliability. Two indices are utilized to evaluate the validity — sensitivity and specificity. These indices are usually determined by administrating the test to one group that has the HIV symptomatic status and to another group that has the AIDS-infected group and then comparing the results.

Thus, sensitivity is defined as the percent of those who have an HIV status and are so predicted by the network test. Specificity is defined as the percent of those who have an AIDS status and are so predicted by the network model.

Table 4  
Summary of model statistics with different hidden nodes

<table><tr><td></td><td> $H_3$ </td><td> $H_5$ </td><td> $H_7$ </td><td> $H_{10}$ </td></tr><tr><td colspan="5">Training set (1026 training patterns)</td></tr><tr><td>Best test set learning event</td><td>60200</td><td>79600</td><td>53200</td><td>43400</td></tr><tr><td>Learning epoch</td><td>58</td><td>77</td><td>51</td><td>42</td></tr><tr><td>L.A.E. (last average error)</td><td>0.296</td><td>0.277</td><td>0.285</td><td>0.290</td></tr><tr><td>M.A.E. (minimum average error)</td><td>0.269</td><td>0.268</td><td>0.271</td><td>0.273</td></tr><tr><td>Epochs since M.A.E.</td><td>17</td><td>7</td><td>10</td><td>1</td></tr><tr><td colspan="5">Test set (145 training patterns)</td></tr><tr><td>Test interval (event)</td><td>200</td><td>200</td><td>200</td><td>200</td></tr><tr><td>L.A.E. (last average error)</td><td>0.279</td><td>0.299</td><td>0.322</td><td>0.289</td></tr><tr><td>M.A.E. (minimum average error)</td><td>0.275</td><td>0.275</td><td>0.275</td><td>0.275</td></tr><tr><td>Event since M.A.E.</td><td>20000</td><td>20000</td><td>20000</td><td>20000</td></tr><tr><td> $R^2$ </td><td>0.108</td><td>0.119</td><td>0.106</td><td>0.101</td></tr><tr><td>M.S.E. (mean squared error)</td><td>0.219</td><td>0.216</td><td>0.219</td><td>0.220</td></tr><tr><td>M.A.E. (mean absolute error)</td><td>0.437</td><td>0.437</td><td>0.435</td><td>0.444</td></tr></table>

Another two indices are used to evaluate the reliability of a test: positive predictive value (PPV) and negative predictive value (NPV). These provide information about the meaning of a positive or a negative test result. A positive predictive value is the probability of the HIV status being actually present, given that a symptomatic status of HIV is predicted as HIV. A negative predictive value is the probability of the

Table 5  
Relative strengths between input and output variables

<table><tr><td>BPA network</td><td> $H_3$ </td><td> $H_5$ </td><td> $H_7$ </td><td> $H_{10}$ </td></tr><tr><td>RW</td><td>0.56</td><td>1.48</td><td>2.03</td><td>1.57</td></tr><tr><td>RB</td><td>1.02</td><td>2.51</td><td>1.24</td><td>1.60</td></tr><tr><td>RH</td><td>1.07</td><td>2.14</td><td>0.73</td><td>2.04</td></tr><tr><td>SexM</td><td>1.07</td><td>2.26</td><td>2.62</td><td>3.66</td></tr><tr><td>SexF</td><td>0.93</td><td>1.27</td><td>1.77</td><td>2.81</td></tr><tr><td>Expr-homo</td><td>0.86</td><td>2.80</td><td>2.00</td><td>1.70</td></tr><tr><td>Expr-IDU</td><td>0.56</td><td>2.01</td><td>2.94</td><td>3.32</td></tr><tr><td>Expr-IV</td><td>0.40</td><td>1.39</td><td>0.92</td><td>1.11</td></tr><tr><td>Expr-hetero</td><td>0.48</td><td>0.91</td><td>1.44</td><td>1.58</td></tr><tr><td>ADMT</td><td>2.55</td><td>4.06</td><td>3.15</td><td>3.73</td></tr><tr><td>IPNGTT</td><td>8.46</td><td>14.0</td><td>9.88</td><td>10.9</td></tr><tr><td>AMSVT</td><td>2.90</td><td>3.86</td><td>3.04</td><td>3.68</td></tr><tr><td>ERVST</td><td>3.66</td><td>6.33</td><td>4.66</td><td>4.48</td></tr><tr><td>MDVST</td><td>0.89</td><td>1.33</td><td>1.08</td><td>1.99</td></tr><tr><td>HCVST</td><td>2.76</td><td>3.88</td><td>3.01</td><td>2.74</td></tr></table>

AIDS status being actually present if a symptomatic status of AIDS is predicted as AIDS.

There are four groups for these tests:

1. those who were predicted as HIV status and actually have HIV status: called true positives;

2. those who were predicted as HIV status but actually have AIDS status: called false positives;

3. those who were predicted as AIDS status and actually have AIDS status: called false negatives; and

4. those who were predicted as AIDS status but actually have HIV status: called true negatives.

Table 6 presents a summary of results of correct classification with respect to each network and the relevant analysis. As it indicates, sensitivity for actual HIV status over ANN classification is somewhat high, but specificity is rather low. This means that the HIV status can be identified easier than AIDS status. Since the AIDS status is very time-dependent, it is very difficult to identify AIDS status through socioeconomic variables and/or simple clinical records.

The optimal number of hidden nodes in hidden layer is one of the conflicting methodological questions for generalization of ANN. Table 7 exhibits the paired T-test for difference between actual symptomatic status and ANN classification along with different hidden nodes. Based on the research design used in this study, the best hidden node for the hidden layer is three. T-test statistics in the table indicate that

Table 6  
Summary of results analysis about correct classification

<table><tr><td>Neural network topology (BPANN)</td><td>HIV–HIV (n = 667)</td><td>AIDS–AIDS (n = 504)</td><td>Sensitivity</td><td>Specificity</td><td>Positive predictive value</td><td>Negative predictive value</td></tr><tr><td> $H_3$ </td><td>587</td><td>169</td><td>88</td><td>34</td><td>64</td><td>68</td></tr><tr><td> $H_5$ </td><td>561</td><td>210</td><td>84</td><td>41</td><td>66</td><td>66</td></tr><tr><td> $H_7$ </td><td>556</td><td>199</td><td>83</td><td>39</td><td>65</td><td>64</td></tr><tr><td> $H_{10}$ </td><td>564</td><td>194</td><td>85</td><td>38</td><td>65</td><td>65</td></tr></table>

Table 7
Paired T-test

<table><tr><td></td><td> $D_{H_3}$ </td><td> $D_{H_5}$ </td><td> $D_{H_7}$ </td><td> $D_{H_{10}}$ </td></tr><tr><td> $D_{H_3}$ </td><td>-</td><td>-8.30*</td><td>-6.43*</td><td>-5.50*</td></tr><tr><td> $D_{H_5}$ </td><td>8.30*</td><td>-</td><td>6.00a</td><td>1.89**</td></tr><tr><td> $D_{H_7}$ </td><td>6.43*</td><td>-6.00a</td><td>-</td><td>1.54a</td></tr><tr><td> $D_{H_{10}}$ </td><td>5.50*</td><td>-1.89**</td><td>-1.54a</td><td>-</td></tr></table>

\* Significant at p-value < 0.00.  
\*\* Significant at p-value < 0.06.  
$^{a}$ No significance.

$D_{H_{3}}$ has statistically significant difference over all other hidden nodes ( $D_{H_{5}}, D_{H_{7}}, D_{H_{10}}$ ) (p-value < 0.000) and $D_{H_{5}}$ has statistically significant difference over $D_{H_{5}}$ (p-value < 0.06).

## 5. Conclusion

This study presents an application of neural networks to classify and predict the symptomatic status of HIV/AIDS patients. A neural network model was developed and analyzed. The diagnostic accuracy of the ANN was evaluated. Several different neural network topologies were applied to ACSUS datasets in order to demonstrate the neural network's capability.

Neural networks are known to be able to identify relationships even when some of the input data are very complex, ill defined, and ill structured. One of the advantages of an ANN is that it can discriminate linearly inseparable data. Even though ANN techniques have been applied to a variety of areas in business, public sector, and health services research, this study makes a substantial contribution to the HIV/AIDS care and prevention planning area. If the appropriate methodologies in various ANN design models were different, it would be interesting to see what impact this would have on the classification of HIV/AIDS-related persons.

## Acknowledgements

The authors wish to acknowledge the financial support of the Korea Research Foundation made in the program year of 1998.

## References

[1] H. Andreassen, H. Bohr, J. Bohr, S. Brunak, T. Bugge, R.M. Cotterill, C. Jacobsen, P. Kusk, B. Lautrup, S.B. Petersen, Analysis of the secondary structure of the human immunodeficiency virus (HIV) proteins p17, gp120, and gp41 by computer modeling based on neural network methods, Journal of Acquired Immune Deficiency Syndromes 3 (6), 1990, pp. 615–622.

[2] N.P. Archer, S. Wang, Application of the back propagation neural network algorithm with monotonicity constraints for two-group classification problems, Decision Sciences 24 (1), 1993, pp. 60–75.

[3] W.G. Baxt, Use of an artificial neural network for the diagnosis of myocardial infarction, Annals of Internal Medicine 115, 1991, pp. 843–848.

[4] J. Bode, Decision support with neural networks in the management of research and development: concepts and application to cost estimation, Information & Management 34(1), 1998, pp. 33–40.

[5] G.E. Davis, W.E. Lowell, G.L. Davis, A neural network that predicts psychiatric length of stay, MD Computing 10 (2), 1993, pp. 87–92.

[6] A.E. Dawson, R.E. Austin Jr., D.S. Weinberg, Nuclear grading of breast carcinoma by image analysis: classification by multivariate and neural network analysis, American Journal of Clinical Pathology 95 (4), 1991, pp. S29–37.

[7] G. Dorffner, G. Porenta, On using feedforward neural networks for clinical diagnostic tasks, Artificial Intelligence in Medicine 6 (5), 1994, pp. 417–435.

[8] M.H. Ebell, Artificial neural network for predicting failure to survive following in-hospital cardiopulmonary resuscitation, Journal of Family Practice 36 (3), 1993, pp. 297–303.

[9] D. Faraggi, R. Simon, A neural network model for survival data, Statistics in Medicine 14, 1995, pp. 73–82.

[10] C.E. Floyd Jr., J.Y. Lo, A.J. Yun, D.C. Sullivan, P.J. Kornguth, Prediction of breast cancer malignancy using an artificial neural network, Cancer 74 (10), 1994, pp. 2944–2948.

[11] L. Fu, Polygenic trait analysis by neural network learning, Artificial Intelligence in Medicine 6 (1), 1994, pp. 51–65.

[12] J.V. Hansen, J.B. McDonald, J.D. Stice, Artificial intelligence and generalized qualitative-response models: an empirical test on two audit decision-making domains, Decision Sciences 23(3), 1992, pp. 708–723.

[13] A. Hart, Using neural networks for classification tasks—some experiments on datasets and practical advice, Journal of the Operational Research Society 44, 1992, pp. 1129–1145.

[14] B.A. Jain, B.N. Nag, Artificial neural network models for pricing initial public offerings, Decision Sciences 26 (3), 1995, pp. 283–302.

[15] S. Kurogi, Speech recognition by an artificial neural network using findings on the afferent auditory system, Biological Cybernetics 64 (3), 1991, pp. 243–249.

[16] N.K. Kwak, C.W. Lee, A neural network application to classification of health status of HIV/AIDS patients, Journal of Medical Systems 21 (2), 1997, pp. 87–97.

[17] M.J. Lenard, P. Alam, G.R. Madey, The application of neural networks and a qualitative response model to the auditor's going concern uncertainty decision, Decision Sciences 26 (2), 1995, pp. 209–227.

[18] E.Y. Li, Artificial neural networks and their business applications, Information & Management 27 (5), 1994, pp. 303–313.

[19] W.E. Lowell, G.E. Davis, Predicting length of stay for psychiatric diagnosis-related groups using neural networks, Journal of the American Medical Informatics Association 1(6), 1994, pp. 459–466.

[20] B. Malakooti, Y.Q. Zhou, Feedforward artificial neural networks for solving discrete multiple criteria decision making problems, Management Science 40 (11), 1994, pp. 1542–1561.

[21] NeuroShell $^{®}$ 2, Frederick, MD: Ward Systems Groups, Inc., 1993.

[22] E. Patuwo, M.H. Hu, M.S. Hung, Two-group classification using neural networks, Decision Sciences 24 (4), 1993, pp. 825–845.

[23] P.M. Ravdin, G.M. Clark, A practical application of neural network analysis for predicting outcome of individual breast cancer patients, Breast Cancer Research 22 (3), 1992, pp. 285–293.

[24] R. Sharda, Neural networks for the MS/OR analyst: an application bibliography, Interfaces 24 (2), 1994, pp. 116–130.

[25] J. Sohl, A.R. Venkatachalam, A neural network approach to forecasting model selection, Information & Management 29(6), 1995, pp. 297–303.

[26] J.V. Tu, A comparison of neural network and logistic regression models for predicting length of stay in the intensive care unit following cardiac surgery, Unpublished Masters Thesis, University of Toronto, Canada, 1993.

[27] S. Wang, The unpredictability of standard back propagation neural networks in classification applications, Management Science 41 (3), 1995, pp. 555–559.

[28] R.L. Wilson, Ranking college football teams: a neural network approach, Interfaces 25 (4), 1995, pp. 44–59.

[29] B.K. Wong, Y. Selvi, Neural network applications in finance: a review and analysis of literature (1990–1996), Information & Management 34 (3), 1998, pp. 129–139.

![](/api/attachments/BJGR3JNJ/fulltext/images/ec74d2a5a031cea28cf7ca430d87d7c4ffa1f35bb71960ab81d945b0f68b4528.jpg)

Chang W. Lee is a faculty member at department of business administration of Chinju National University. He received his MS and PhD from Saint Louis University, USA. His publications have appeared in European Journal of Operational Research, Journal of the Operational Research Society, Journal of Medical Systems, Application of Management Science, Korean Journal of Business, Journal of Information Sys-

tems, Review of Business and Economics, and others. He served as referees of Health Care Management Science and International Journal of Operations and Quantitative Methods.

![](/api/attachments/BJGR3JNJ/fulltext/images/02a6e519cd4d0aa8fd3c574f3e008928bf73e7122c37c8ef5786c72215c2168d.jpg)

Jung-A Park is a fellow of Institute of Food and Nutrition Science at Keimyung University. She received her MS from Eastern Michigan University, USA and PhD from Keimyung University. Her publications have appeared in Korean Journal of Nutrition, Journal of Community Nutrition, and others.
