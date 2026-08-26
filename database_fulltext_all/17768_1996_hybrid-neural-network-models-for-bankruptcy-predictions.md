---
otero_id: 17768
otero_key: "C2BCS7H3"
title: "Hybrid neural network models for bankruptcy predictions"
authors: "Kun Chang Lee; Ingoo Han; Youngsig Kwon"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00018-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hybrid neural network models for bankruptcy predictions

Kun Chang Lee $^{a}$ , Ingoo Han $^{b,*}$ , Youngsig Kwon $^{c}$

$^{a}$ Department of Management Information Systems, Center for Artificial Intelligence Research (CAIR), Kyonggi University, Suwon 791-940, South Korea

$^{b}$ Department of Management Information Systems, Korea Advanced Institute of Science and Technology, Seoul 130-650, South Korea $^{c}$ Department of Industrial Engineering, Dong-Kuk University, Seoul 100-715, South Korea

## Abstract

The objective of this paper is to develop the hybrid neural network models for bankruptcy prediction. The proposed hybrid neural network models are (1) a MDA-assisted neural network, (2) an ID3-assisted neural network, and (3) a SOFM(self organizing feature map)-assisted neural network. Both the MDA-assisted neural network and the ID3-assisted neural network are the neural network models operating with the input variables selected by the MDA method and ID3 respectively. The SOFM-assisted neural network combines a backpropagation model (supervised learning) with a SOFM model (unsupervised learning). The performance of the hybrid neural network model is evaluated using MDA and ID3 as a benchmark. Empirical results using Korean bankruptcy data show that hybrid neural network models are very promising neural network models for bankruptcy prediction in terms of predictive accuracy and adaptability.

Keywords: Bankruptcy prediction; Neural network; Hybrid neural network; Unsupervised learning

## 1. Introduction

Neural networks have performed well in business classifications including bankruptcy prediction. A neural network model has a good ability in modeling and forecasting. The success of the neural network model is attributable to its generalization capability to predict the output for new data after the neural network was trained. Bankruptcy prediction has been a major research issue in accounting and finance for the last thirty years. There exist extensive studies in this area using statistical approaches $[1,2,4,10,$ [11,16,20] and AI (artificial intelligence) approaches [3,8,9,21,24,28]. MDA has been used the most frequently among the statistical approaches in bankruptcy prediction. Previous empirical results show that neural network models provide higher predictive accuracies than statistical methods and other AI methods such as inductive learning and genetic algorithm. However, it has not been resolved yet how to design a neural network model suitable for a specific problem. It has been proposed that the hybrid model combining two or more models has a potential to achieve a high predictive performance [19]. We propose three kinds of hybrid neural network models: (1) MDA-assisted neural network, (2) ID3-assisted neural network, and (3) SOFM (self organizing feature map)-assisted neural network models. The purpose of this study is then to explore the possibility of the proposed hybrid neural network models in bankruptcy prediction.

A MDA-assisted neural network is a neural network model operating with input variables selected by MDA method. Similarly, an ID3-assisted neural network indicates a neural network model operating with input variables selected by the ID3 method. A SOFM-assisted neural network is a neural network model combining a supervised neural network model with an unsupervised neural network model. In this study, we use a popular backpropagated neural network model as supervised model and a SOFM neural network model $[17]$ as unsupervised model. We use a SOFM model as preprocessing mechanism. Then, the backpropagated neural network model performs a classification task based on the information given by the SOFM model. We use MDA and ID3 methods as benchmarking tools.

The testbed used in this study consists of bankruptcy cases reported in Korea from 1979 through 1992. We collected a sample of 83 bankrupt firms. The 57 financial variables were used as input variables. To simulate a predictive mode, we divided the bankruptcy data into the training data over one period and the hold-out data over the next period. In addition, we organized the sample by the three groups to investigate the adaptability of classification models to the changes in the training data.

The rest of the paper is organized as follows. The classification models used in this study are discussed in the next section. Research data and modeling is presented in Section 3. Empirical results are provided in Section 4. Concluding remarks are presented in Section 5.

## 2. Classification models for bankruptcy prediction

In this section, we briefly discuss the characteristics of classification models used in our empirical tests: MDA, ID3, MDA-assisted neural network, an ID3-assisted neural network, and a SOFM-assisted neural network.

## 2.1. Multivariate discriminant analysis

The MDA method is based on the Fisher procedure [12] which constructs a discriminant function by maximizing the ratio of between-groups and within-groups variances. Linear classifiers derived from the Fisher procedure are known to be optimal in minimizing the expected cost of misclassifications, provided the following conditions are satisfied:

1. each group follows a multivariate normal distribution,

2. the covariance matrices of each group are identical,

3. mean vectors, covariance matrices, and prior probabilities of misclassification are known.

MDA yields a linear discriminant function or hyperplane relating a set of independent variables to a dependent variable. In bankruptcy prediction, financial ratios are used as independent variables while the state of bankruptcy or non-bankruptcy is used as dependent variable. The violation of multivariate normality assumptions for independent variables frequently occurs in the financial data [11]. As an alternative to overcome this problem, natural logarithm transformations are used to approximate normal distribution although the transformed variables may be difficult to interpret.

## 2.2. ID3

Instead of generating a decision rule in the form of a discriminant function, the ID3 method yields a decision tree that classifies the training sample by using the entropy measure $[22,23]$ . This inductive learning method has been applied to various business classification problems including credit scoring $[7]$ , corporate failures prediction $[20]$ , stock portfolio construction $[28]$ , stock market behavior prediction $[5]$ , and bankruptcy risk prediction $[18]$ . The ID3 method intends to minimize the entropy by splitting subsets.

## 2.3. MDA-assisted neural network

In general, the neural network model does not impose any kind of assumptions on input variables while most statistical methods such as MDA impose strict statistical assumptions on the input variables. The intention underlying the MDA-assisted neural network model is that MDA method is used as preprocessing mechanism for selecting important input variables which will be used in the neural network model.

## 2.4. ID3-assisted neural network

The ID3-assisted neural network intends to incorporate ID3 in the form of preprocessing mechanism. ID3 selects input variables which are to be used later in the neural network model. The experiment using ID3 as preprocessor is to test how well ID3 performs in selecting input variables based on the entropy values.

## 2.5. SOFM-assisted neural network

Neural network-based learning is the process by which a neural network model adjusts their connection weights when presented with external input. There are two types of neural network-based learning: supervised and unsupervised. In supervised learning, the actual output of a neural network is compared to the desired output. Then, the connection weights are adjusted to minimize the error between the actual and desired output. In unsupervised learning, only the input is given without any information on what the desired output should be, and then the neural network is self-organized by its weights according to the learning rules such as Kohonen's, Hebbian, and Grossberg's rule.

The unsupervised learning has not been applied for business classification research though it seems to have a good potential for improving the predictive performance. In this paper, we propose the SOFM-assisted neural network model which integrates unsupervised and supervised learning in a sequential manner. The problem solving logic underlying this hybrid neural network model is that the uncertainty and/or fuzziness residing in the data may be reduced as the unsupervised neural network learning model is first applied to the input data and generates a certain number of clusters.

Next, the supervised neural network learning model is applied to the clusters. The SOFM-assisted neural network basically combines the SOFM model with a LVQ (Linear Vector Quantization) model in a sequential manner so that more refined clusters can be extracted from the given input data, where a cluster represents a regularity or a rule describing the data as a whole.

The SOFM model proposed by Kohonen [17] is one of the unsupervised neural network models. Its essential constituents are as follows:

1. An array of neurons receiving coherent inputs and computing a simple output function,

2. A mechanism for comparing the neuronal outputs to select the neuron producing maximum output,

3. A local interaction between the selected neuron and its neighbors,

4. An adaptive mechanism that updates the interconnection weights.

The SOFM model is a two-layered neural network such as an input layer and a competitive layer. All the neurons in the input layer are fully interconnected to those in the competitive layer. The main recipe of SOFM learning is that an input pattern is presented sequentially to the input layer, and then the best matching neurons are found in the competitive layer through learning. Afterward, the best matching neurons activate their neighbors to classify the same input patterns. In contrast to the random mapping in competitive learning, the SOFM model transforms the input data into a topology-preserving map constituted by the competitive neurons. As a result, the similarities among the patterns are mapped into the closeness relationships on the competitive layer.

Each neuron in the competitive layer is called quantization neuron which computes how close its quantization vector is to the input vector. Suppose that x is the M-dimensional input vector incident to the neuron along the connection weight vector (or called quantization vector) $m_{i}$ . If the best match between vectors $m_{i}$ and x occurs at neuron c, then we have

$$
\| \boldsymbol {x} - \boldsymbol {m} _ {c} \| = \min \| \boldsymbol {x} - \boldsymbol {m} _ {i} \|, \quad i = 0, 1, \dots , N ^ {2}
$$

where $\|\cdot\|$ indicates the Euclidean norm. The weight updating rule is given as

$$
\begin{array}{l} m _ {i} (t + 1) \\ = \left\{ \begin{array}{l l} m _ {i} (t) + \alpha (t) (x (t) - m _ {i} (t)) & \text { for } i \in N _ {c} \\ m _ {i} (t) & \text { otherwise }, \end{array} \right. \end{array}
$$

where $\alpha(t)$ is a positive constant that decays with time and $N_{c}$ defines a topological neighborhood around the maximally responding neuron c, such that it also decreases with time. Different parts of the neural network become selectively sensitized to different inputs in an ordered fashion so as to form a continuous map of the signal space. After a number of sweeps through the training data, with weight updating at each iteration obeying the weight updating rule above, the asymptotic values of $m_{i}$ cause the output space to attain proper topological ordering. This is basically a variation of unsupervised learning.

Meanwhile, the structure of learning with the LVQ model [17] is basically the same as SOFM-based learning. However, the LVQ model is based on supervised learning by assigning quantization vectors $m_{i}$ to each class. Each class is labeled with the corresponding class symbols, and then the class borders are determined by the nearest-neighbor method that computes the smallest distance between the input vector x with the quantization vector $m_{i}$ in terms of Euclidean distance. As a result, the label of the closest weight vector $m_{c}$ defines the classification of input vector x.

Based on the arguments about SOFM and LVQ models, the SOFM-assisted neural network is composed of two stages: (1) the clustering neural network (CNN) stage and (2) the output neural network (ONN) stage.

## Stage 1: CNN stage

Input data samples are clustered to detect the regularities hidden in them. The clusters may be expressed as rules $[27]$ . For the purpose of clustering, we used two neural network models SOFM and LVQ proposed by Kohonen $[17]$ in a hybrid manner. Based on these two neural network models, the CNN stage is composed of the following three steps:

Step 1: Apply SOFM model.

The SOFM neural model, one of the unsupervised neural network models proposed by Kohonen [17], is applied to the input data samples. Then we can obtain a certain number of clusters by separating the given input data set. Such clusters represent a set of meaningful rules encompassing the input data. Since those rules help to find the regularity among the related output classes more clearly, the neural network model can have a better ability of generalization for the unknown data.

Step 2: Refine with LVQ model.

The LVQ model, which is also proposed by Kohonen [17], is used to refine the boundaries between clusters formed by SOFM. In this way, the vague cases which SOFM cannot correctly classify into an appropriate cluster are assigned to proper clusters. As mentioned previously, the LVQ model is a supervised neural network model different from the SOFM model. Hung [15] shows the effectiveness of combining SOFM and LVQ models in building a neuro-fuzzy learning control system.

Step 3: Train the clusters with backpropagated neural network.

After the appropriate clusters hidden in the input data samples are detected by the SOFM model and refined by the LVQ model in a sequential manner, backpropagation learning $[25]$ is applied to the input data samples with cluster outputs given by SOFM and LVQ models. Therefore, CNN is a backpropagated neural network model which is trained to find an appropriate cluster for each given sample.

## Stage 2: ONN stage

ONN is built by applying the backpropagation neural network model to each cluster. ONN is a mapping function between the input sample and corresponding desired output (i.e., “bankrupt” or “non-bankrupt”). Once ONN is built, then the sample can be classified into one of the “bankrupt” or “non-bankrupt” states.

## 3. Research data and modeling

## 3.1. Research data

The data sample consists of Korean firms that failed in the period 1979–1992. They were selected from the bankrupt companies listed in the Korea Stock Exchange. We define the state of bankruptcy as follows:

1. The firms which applied for, have started, or are under the process of corporate clearance.

Table 1  
The size of sample and the year by group

<table><tr><td>Group</td><td>Training data</td><td>Testing data</td></tr><tr><td>Group I</td><td>66 (1979–1984)</td><td>100 (1985–1992)</td></tr><tr><td>Group II</td><td>96 (1979–1990)</td><td>70 (1991–1992)</td></tr><tr><td>Group III</td><td>126 (1979–1991)</td><td>40 (1992)</td></tr></table>

Table 2  
A list of 57 financial variables

<table><tr><td>Section</td><td>No.</td><td>Financial ratio</td></tr><tr><td rowspan="11">Growth</td><td>1</td><td>Growth rate of total assets</td></tr><tr><td>2</td><td>Growth rate of sales</td></tr><tr><td>3</td><td>Growth rate of ordinary incomes</td></tr><tr><td>4</td><td>Growth rate of net incomes</td></tr><tr><td>5</td><td>Growth rate of fixed asset 1</td></tr><tr><td>6</td><td>Growth rate of fixed asset 2</td></tr><tr><td>7</td><td>Growth rate of fixed asset 3</td></tr><tr><td>8</td><td>Growth rate of total liabilities 1</td></tr><tr><td>9</td><td>Growth rate of total liabilities 2</td></tr><tr><td>10</td><td>Growth rate of total liabilities 3</td></tr><tr><td>11</td><td>Growth rate of total liabilities 4</td></tr><tr><td rowspan="12">Profitability</td><td>12</td><td>Ordinary income to total assets</td></tr><tr><td>13</td><td>Net income to total assets</td></tr><tr><td>14</td><td>Ordinary income to business capital</td></tr><tr><td>15</td><td>Ordinary income to stock holders&#x27; equity</td></tr><tr><td>16</td><td>Net income to stock holders&#x27; equity</td></tr><tr><td>17</td><td>Net income to capital stock</td></tr><tr><td>18</td><td>Ordinary income to sales</td></tr><tr><td>19</td><td>Net income to sales</td></tr><tr><td>20</td><td>Gross profit to sales</td></tr><tr><td>21</td><td>Operating income to sales</td></tr><tr><td>22</td><td>Financial expenses to sales</td></tr><tr><td>23</td><td>Dividends to capital stock</td></tr><tr><td rowspan="18">Stability</td><td>24</td><td>Stock holders&#x27; equity to total assets</td></tr><tr><td>25</td><td>Current ratio</td></tr><tr><td>26</td><td>Quick ratio</td></tr><tr><td>27</td><td>Fixed ratio</td></tr><tr><td>28</td><td>Fixed assets to stockholders&#x27; equity and long-term liabilities</td></tr><tr><td>29</td><td>Debt ratio</td></tr><tr><td>30</td><td>Current liabilities ratio</td></tr><tr><td>31</td><td>Fixed liabilities ratio</td></tr><tr><td>32</td><td>Total borrowings and bonds to total assets 1</td></tr><tr><td>33</td><td>Total borrowings and bonds to total assets 2</td></tr><tr><td>34</td><td>Total borrowings and bonds to total assets 3</td></tr><tr><td>35</td><td>Total liability composition</td></tr><tr><td>36</td><td>Fixed asset composition</td></tr><tr><td>37</td><td>Inventory to current assets</td></tr><tr><td>38</td><td>Change in inventory to current assets</td></tr><tr><td>39</td><td>Net working capital to total assets</td></tr><tr><td>40</td><td>Interest coverage ratio</td></tr><tr><td>41</td><td>Interest ratio</td></tr><tr><td rowspan="4">Cash flow</td><td>42</td><td>Cash Flow to stockholders&#x27; equity</td></tr><tr><td>43</td><td>Cash flow to total borrowings and bond</td></tr><tr><td>44</td><td>Cash flow to total assets</td></tr><tr><td>45</td><td>Cash flow to sales</td></tr><tr><td rowspan="4">Activity</td><td>46</td><td>Total assets turnover</td></tr><tr><td>47</td><td>Stockholders&#x27; equity turnover</td></tr><tr><td>48</td><td>Net working capital turnover</td></tr><tr><td>49</td><td>Fixed assets turnover</td></tr></table>

Table 2 (continued)

<table><tr><td>Section</td><td>No.</td><td>Financial ratio</td></tr><tr><td rowspan="2">Activity</td><td>50</td><td>Inventories turnover</td></tr><tr><td>51</td><td>Change in Inventories turnover</td></tr><tr><td rowspan="6">Credibility</td><td>52</td><td>Change in payables to receivables</td></tr><tr><td>53</td><td>Payables to current liabilities</td></tr><tr><td>54</td><td>Change in payables to current liabilities</td></tr><tr><td>55</td><td>Change in receivables to current assets</td></tr><tr><td>56</td><td>Payables to receivables</td></tr><tr><td>57</td><td>Payables to inventories</td></tr></table>

2. The firms which quit or closed business.

3. The firms which have had losses for the consecutive three years and are currently under legal control.

4. The firms which reported the withdrawal of listing or terminated to be listed by the Korea Stock Exchange.

Using the above definition of bankruptcy, 83 bankrupt firms were selected. A failed firm was matched with a nonfailed firm in terms of (1) asset size, (2) capital size, (3) number of employees, and (4) age. Therefore, 166 firms in total were selected as sample. We grouped the training sample into the three subsamples by the time period: (1) Group I (1979–1984), (2) Group II (1979–1990), and (3) Group III (1979–1991). The motivation of this grouping is to see the impact of training sample size on the performance of classification models. Group I, II, and III contains 66, 96, and 126 training firms and 100, 70, and 40 hold-out firms respectively, as shown in Table 1. This grouping will help to find how the neural network models can perform as the new training data are added.

Initially 57 financial variables are selected for the prediction model. The list of financial ratios is shown in Table 2.

The 57 financial variables are those which were found significant in predicting bankruptcy by previous studies or have been used in practice to predict bankruptcy. The 57 ratios can be grouped into six categories such as growth, profitability, stability, cash flow, activity, and credibility.

One of major assumptions of MDA is that independent variables are normally distributed. Financial ratios are usually skewed to the positive side [14]. Buijink and Kegers [6] found that the skewness of financial ratios holds for the long term period as well as for the short term period. The ways to approximate normal distribution are trimming, truncation, and log-transformation. Trimming and truncation are used to eliminate or adjust outliers. Inappropriate trimming or truncation may lead to serious errors. In this sense, Berry and Tregueiros [3] advocate the use of log-transformation. In this study, the log-transformation is used to approximate the normal distribution of financial variables. To verify the normal approximation of the log-transformed financial ratios, a statistical analysis was performed. The results show that the log-transformed ratios are normally distributed at the significance level of 5%. The t-test was performed for each of the 57 financial variables in the data sample to test the discriminative power of input variables.

## 3.2. MDA

To determine a linear function of input variables for the MDA, there are two methods; a direct method and a stepwise method. In this research, we used the stepwise method using Wilk's Lambda to sequentially select important variables from 57 variables. Table 3, Table 4, and Table 5 show the MDA results for each group. For Group I, 10 financial variables were selected as important input variables for predicting bankruptcy. Similarly, 18 and 17 financial variables were chosen for Group II and III, respectively.

Table 3  
Financial ratios selected by MDA in Group I

<table><tr><td colspan="2">Selected financial ratios</td><td>Wilk&#x27;s  $\lambda$ </td></tr><tr><td>x4:</td><td>Growth rate of net income</td><td>0.45958</td></tr><tr><td>x12:</td><td>Ordinary income to total assets</td><td>0.29407</td></tr><tr><td>x18:</td><td>Ordinary income to sales</td><td>0.34206</td></tr><tr><td>x23:</td><td>Dividends to capital stock</td><td>0.48159</td></tr><tr><td>x24:</td><td>Stock holders&#x27; equity to total assets</td><td>0.36554</td></tr><tr><td>x26:</td><td>Quick ratio</td><td>0.43109</td></tr><tr><td>x31:</td><td>Fixed liabilities ratio</td><td>0.30236</td></tr><tr><td>x46:</td><td>Total assets turnover</td><td>0.31162</td></tr><tr><td>x47:</td><td>Stock holders&#x27; equity turnover</td><td>0.35251</td></tr><tr><td>x49:</td><td>Fixed assets turnover</td><td>0.32575</td></tr></table>

Table 4  
Financial ratios selected by MDA in Group II

<table><tr><td colspan="2">Independent variable</td><td>Wilks&#x27;s  $\lambda$ </td></tr><tr><td>x4:</td><td>Growth rate of net incomes</td><td>0.40187</td></tr><tr><td>x5:</td><td>Growth rate of fixed assets 1</td><td>0.32671</td></tr><tr><td>x9:</td><td>Growth rate of total liabilities 2</td><td>0.34777</td></tr><tr><td>x12:</td><td>Ordinary income to total assets</td><td>0.35616</td></tr><tr><td>x13:</td><td>Net income to total assets</td><td>0.47133</td></tr><tr><td>x16:</td><td>Net income to stock holders&#x27; equity</td><td>0.38720</td></tr><tr><td>x18:</td><td>Ordinary income to sales</td><td>0.29298</td></tr><tr><td>x23:</td><td>Dividends to capital stock</td><td>0.50334</td></tr><tr><td>x24:</td><td>Stock holders&#x27; equity to total assets</td><td>0.36999</td></tr><tr><td>x26:</td><td>Quick ratio</td><td>0.42133</td></tr><tr><td>x28:</td><td>Fixed assets to stock holders&#x27; equity and long-term liabilities</td><td>0.28450</td></tr><tr><td>x30:</td><td>Current liabilities ratio</td><td>0.37989</td></tr><tr><td>x35:</td><td>Total liability composition</td><td>0.29298</td></tr><tr><td>x41:</td><td>Fixed asset composition</td><td>0.28839</td></tr><tr><td>x42:</td><td>Cash flow to stock holders&#x27; equity ratio</td><td>0.3197</td></tr><tr><td>x44:</td><td>Cash flow to total assets</td><td>0.33337</td></tr><tr><td>x47:</td><td>Stock holders&#x27; equity turnover</td><td>0.27996</td></tr><tr><td>x48:</td><td>Net working capital turnover</td><td>0.45011</td></tr></table>

Table 5  
Financial ratios selected by MDA in Group III

<table><tr><td colspan="2">Independent variable</td><td>Wilk&#x27;s  $\lambda$ </td></tr><tr><td>x3:</td><td>Growth rate of ordinary incomes</td><td>0.38273</td></tr><tr><td>x5:</td><td>Growth rate of fixed assets 1</td><td>0.46688</td></tr><tr><td>x9:</td><td>Growth rate of total liabilities 2</td><td>0.39475</td></tr><tr><td>x12:</td><td>Ordinary income to capital stock</td><td>0.29407</td></tr><tr><td>x13:</td><td>Net income to total assets</td><td>0.41362</td></tr><tr><td>x14:</td><td>Financial expenses and ordinary income to total assets</td><td>0.41915</td></tr><tr><td>x19:</td><td>Net income to sales</td><td>0.40761</td></tr><tr><td>x23:</td><td>Dividends to capital stock</td><td>0.58411</td></tr><tr><td>x24:</td><td>Stock holders&#x27; equity to total assets</td><td>0.44148</td></tr><tr><td>x26:</td><td>Quick ratio</td><td>0.47886</td></tr><tr><td>x28:</td><td>Fixed assets to stock holders&#x27; equity and long-term liabilities</td><td>0.49619</td></tr><tr><td>x30:</td><td>Current liabilities ratio</td><td>0.40202</td></tr><tr><td>x33:</td><td>Total borrowings and bonds to total assets 2</td><td>0.51856</td></tr><tr><td>x40:</td><td>Interest coverage ratio</td><td>0.39475</td></tr><tr><td>x45:</td><td>Cash flow to sales</td><td>0.38942</td></tr><tr><td>x47:</td><td>Stock holders&#x27; equity turnover</td><td>0.43100</td></tr><tr><td>x54:</td><td>Change in payables to current liabilities</td><td>0.45836</td></tr></table>

< Figure 1 > Decision Tree for Group 1  
![](/api/attachments/C2BCS7H3/fulltext/images/1f5d11d0561e742b810020881e3f237669140498d931f5b18d4515c7f7e2391a.jpg)  
Fig. 1. Decision tree for group 1. Legend: B: Bankruptcy, NB: Non-bankruptcy.

## 3.3. ID3

ID3 forms a decision tree that correctly classifies all the input data on the basis of the entropy measure of attribute. The ID3 algorithm was coded in Pascal. The classification tree generated by ID3 for Group I is illustrated in Fig. 1. The number of financial variables chosen by ID3 is 7 for Group I in the process of building a decision tree. Similarly, 7 and 9 financial variables were selected by using ID3 for Group II and III, respectively.

## 3.4. Neural network model

We have constructed 3-layer networks. The number of hidden units are set to be the same as the number of input units for the neural networks for Group I, II, and III. The backpropagation learning algorithm has been frequently used in business classification studies while SOFM and LVQ have been hardly used in this area. We used NeuralWorks Professional V5.0 (Neural Ware Inc., 1994) to implement the neural network models.

## 4. Empirical results

The prediction accuracies by MDA are 68%, 68.57%, and 70% for Group I, II, and III respectively. The prediction results by ID3 are 74%,

72.86%, and 77.50% for Group I, II, and III respectively. MDA-assisted neural network uses the financial variables, selected by the stepwise method of MDA, as input variables. Therefore, the input variables are the same as those of MDA. There has yet been a formal method to design or configure a neural network appropriate for a certain classification task (for example, the number of neurons and hidden layers, selection of learning algorithms, and learning parameters, etc). Exploratory experiments were performed to find an appropriate architecture.

In the experiment for MDA-assisted neural network, 10 input neurons are placed in the input layer for Group I, 18 input neurons for Group II, and 17 input neurons for Group III. We used one hidden layer containing the same number of hidden neurons as the input units. Finally, two output neurons are placed in the output layer.

Therefore, experiments with the MDA-assisted neural network were performed with three kinds of neural network architectures: (1) neural network with 10 input neurons, 10 hidden neurons, and 2 output neurons (Group I), (2) neural network with 18 input neurons, 18 hidden neurons, and 2 output neurons (Group II), and (3) neural network with 17 input neurons, 17 hidden neurons, and 2 output neurons (Group III). The prediction accuracies by the MDA-assisted neural network are 70%, 80%, and 80% for Group I, II, and III.

The ID3-assisted neural network indicates a neural network model operating with the input variables included in the decision tree by ID3. The architecture of the ID3-assisted neural network is similar to that of MDA-assisted neural network except for the number of input neurons. The stepwise method of MDA selects input variables in terms of geometric distance measure while ID3 selects input variables in terms of entropy measure. For the experiments of ID3-assisted neural network, the input variables are obtained by ID3. Neural network models for both Group I and II have 7 input neurons, 7 hidden neurons, and 2 output neurons. The neural network for Group III has 9 input neurons, 9 hidden neurons, and 2 output neurons. The prediction accuracies by the ID3-assisted neural network are 73%, 81.43%, and 82.5% for Group I, II, and III respectively.

The SOFM-assisted neural network is a sequential integration of SOFM and supervised network. The selection of input variables are performed by MDA and ID3 as before. The SOFM-assisted neural network model using input variables selected by the stepwise method of MDA is denoted by SOFM(MDA)-assisted neural network. Similarly, the SOFM(ID3)-assisted neural network uses input variables included in the decision tree of ID3. The prediction accuracies of the SOFM(MDA)-assisted neural network are 84%, 74.3%, and 82.5%. Those of the SOFM(ID3)-assisted neural network are 74%, 80%, and 77.5% respectively. The results are summarized in Table 6.

Table 6  
Prediction accuracies of classification models

<table><tr><td>Group</td><td>MDA</td><td>ID3</td><td>MDA-assisted NN</td><td>ID3-assisted NN</td><td>SOFM(MDA)-assisted NN</td><td>SOFM(ID3)-assisted NN</td><td>Total</td></tr><tr><td>Group I</td><td>68.00%</td><td>74.00%</td><td>70.00%</td><td>73.00%</td><td>84.00%</td><td>74.00%</td><td>73.83%</td></tr><tr><td>Group II</td><td>68.57%</td><td>72.86%</td><td>80.00%</td><td>81.43%</td><td>74.30%</td><td>80.00%</td><td>76.19%</td></tr><tr><td>Group III</td><td>70.00%</td><td>77.50%</td><td>80.00%</td><td>82.50%</td><td>82.50%</td><td>77.50%</td><td>78.33%</td></tr><tr><td>Total</td><td>68.57%</td><td>74.29%</td><td>75.24%</td><td>77.62%</td><td>80.48%</td><td>76.67%</td><td>75.00%</td></tr></table>

Legend: NN = Neural Network.

On the average, the SOFM(MDA)-assisted neural network model performs the best. This model shows an outstanding prediction accuracy (84%) for Group I. The addition of more training data does not improve the predictive performance of the SOFM(MDA)-assisted neural network. The next one is the ID3-assisted neural network. Although performing poorly for Group I, it provides a strong performance for Group II and III. The third one is the SOFM(ID3)-assisted neural network. The MDA-assisted neural network is the fourth. ID3 is placed in the fifth place. The MDA performs the worst. Therefore, our proposed hybrid neural network models outperform the MDA and ID3 models. It is noteworthy that the performances of the hybrid neural network models generally improve as the training data increase in number. This can be found by comparing the performance of each group in Table 6. However, this trend is weak for MDA and ID3. The MDA-assisted neural network and the ID3-assisted neural network show a big increase in the prediction performance between Group I and Group II. The trend is not clear for the SOFM(MDA)-assisted neural network and the SOFM(ID3)-assisted neural network.

In summary, hybrid neural network models perform better than MDA and ID3. The SOFM-assisted neural network turns out to have a great potential in bankruptcy prediction. This is attributable to the fact that it categorizes the input data samples into appropriate numbers of clusters and extracts regularities from each cluster. Therefore, the SOFM-assisted neural network can cope with the noise or irregularities more efficiently than the other models.

Table 7  
Z values for the pairwise comparison of performance between classification models

<table><tr><td></td><td>ID3-assisted NN</td><td>SOFM(ID3)-assisted NN</td><td>MDA-assisted NN</td><td>ID3</td><td>MDA</td></tr><tr><td>SOFM(MDA)-assisted NN</td><td>0.7201</td><td>0.9515</td><td> $1.2932^a$ </td><td> $1.5162^a$ </td><td> $2.8009^c$ </td></tr><tr><td>ID3-assisted NN</td><td>-</td><td>0.2318</td><td>0.5746</td><td>0.7985</td><td> $2.0911^b$ </td></tr><tr><td>SOFM(ID3)-assisted NN</td><td>-</td><td>-</td><td>0.3429</td><td>0.5669</td><td> $1.8613^b$ </td></tr><tr><td>MDA-assisted NN</td><td>-</td><td>-</td><td>-</td><td>0.2241</td><td> $1.5206^a$ </td></tr><tr><td>ID3</td><td>-</td><td>-</td><td>-</td><td>-</td><td> $1.2974^a$ </td></tr></table>

$^{a}$ Significant at 10%.  
$^{b}$ Significant at 5%.  
$^{c}$ Significant at 1%.

We use the Z-tests to examine whether the prediction accuracies of hybrid models are higher than those of MDA or ID3. Table 7 shows the standardized normalized test statistic, Z values when the prediction accuracies of the left-vertical methods are compared with those of the right-horizontal methods.

The SOFM(MDA)-assisted neural network performs significantly better than MDA at a 1% level and marginally better than the MDA-assisted neural network or ID3 at a 10% level. The ID3-assisted neural network performs significantly better than MDA at a 5% level. The SOFM(ID3)-assisted neural network performs significantly better than MDA at a 5% level. The MDA-assisted neural network performs marginally better than MDA at a 10% level. In general, the predictive performance is improved by using the hybrid approach.

## 5. Concluding remarks

This paper has suggested the hybrid neural network models which perform very well in the bankruptcy prediction tasks. Our proposed hybrid neural network models either integrate different kinds of neural network models (like SOFM-assisted neural network) or combine neural network model with other statistical or AI models (like MDA-assisted or ID3-assisted neural network models). The SOFM-assisted neural network model integrates unsupervised learning model (SOFM) and supervised learning (LVQ) to find more refined regularity hidden in the input data. Meanwhile, a MDA-assisted or an ID3-assisted neural network model uses MDA or ID3 models as a preprocessor for selecting the appropriate input variables which are to be used by the supervised neural network model.

This study experimented MDA, ID3, and hybrid neural network models using Korean bankruptcy data. Experimental results showed that the SOFM(MDA)-assisted neural network model performs the best, which implies the high potential of integrating unsupervised learning with supervised learning. This is an exploratory study to propose and test hybrid neural network models. Future studies are expected to present improved hybrid neural network models with superior performances.

## References

[1] E.I. Altman, Financial Ratios, Discriminant Analysis and Prediction of Corporate Bankruptcy, The Journal of Finance 23 (September 1968) 589–609.

[2] E.I. Altman, R.G. Haldeman and P. Narayanan, Zeta Analysis, Journal of Banking and Finance (June 1977) 29–51.

[3] R. Berry and D. Treigueiros, The Application of Neural Network Based Methods to the Extraction of Knowledge from Accounting Reports, IEEE International Joint Conference on Neural Networks (1991) 136–146.

[4] M. Blum, Failing Company Discriminant Analysis, Journal of Accounting Research (Spring 1974) 1–25.

[5] H. Braun and J.S. Chandler, Predicting Stock Market Behavior through Rule Induction: An Application of the Learning-From-Example Approach, Decision Science 18 (1987) 415–429.

[6] Buijink, W. and M. Jegers, Cross-Sectional Distributional Properties of Financial Ratios of Belgian Manufacturing Industries: Some Empirical Evidence, Technical Report, University of Antwerp, Belgium (1984).

[7] C. Carter and J. Catlett, Assessing Credit Card Applications Using Machine Learning, IEEE Expert (Fall 1987) 71–79.

[8] H. Chung and K. Tam, A Comparative Analysis of Inductive-Learning Algorithm, Intelligent Systems in Accounting, Finance and Management 2 (1992) 3–18.

[9] J.R. Coakley and C.E. Brown, Neural Networks Applied to Ratio Analysis in the Analytical Review Process, The 4th International Symposium on Expert Systems in Accounting, Finance and Management (1991) 1–35.

[10] R.A. Collins and R.D. Green, Statistical Methods for Bankruptcy Forecasting, Journal of Economics and Business 32 (1972) 349–354.

[11] E.B. Deakin, A Discriminant Analysis of Predictors of Business Failure, Journal of Accounting Research (Spring 1976) 167–179.

[12] R.A. Fisher, The Use of Multiple Measurements in Taxonomic Problems, Ann. Eugenics 7 (1936) 179–188.

[13] C.H. Harris and P.A. Frishkoff, An Expert Decision Support System for Auditor Going concern Evaluation, Working Paper, The University of Texas at Arlington (1989).

[14] J. Horrigan, The Determination of Long Term Credit Standing with Financial Ratios, Journal of Accounting Research (1965) 44–68.

[15] C. Hung, Building a Neuro-Fuzzy Learning Control System, AI EXPERT (Nov 1993) 40–49.

[16] G.V. Karels and A. Prakash, Multivariate Normality and Forecasting of Business Bankruptcy, Journal of Business Finance and Accounting (Winter 1987) 573–93.

[17] T. Kohonen, Self-Organizing Map, Proceedings of the IEEE 78, No. 9 (September 1990).

[18] S.B. Lee and S.H. Oh, A Comparative Study of Recursive Partitioning Algorithm and Analog Concept Learning System, Expert Systems with Applications 1 (1990) 403–416.

[19] T. Liang, J. Chandler, and I. Han, Integrating Statistical and Inductive Learning Methods for Knowledge Acquisition, Expert Systems with Applications 1 (1990) 391–401.

[20] W.F. Messier and J.V. Hansen, Inducing Rules for Expert System Development: An Example Using Default and Bankruptcy data, Management Science 34, No. 12 (Dec 1988) 1403–1415.

[21] M. Odom and R. Sharda, A Neural Network Model for Bankruptcy Prediction, Proceedings of the IEEE International Conference on Neural Network 2 (1990) 163–168

[22] J.R. Quinlan, Discovering Rules by Induction from Large Collection of Examples, in: D. Michie, Ed., Expert Systems in the Micro Electronic Age (Edinburg University Press, 1979).

[23] J.R. Quinlan, Induction of Decision Trees, Machine Learning 1 (1986) 81–106.

[24] W. Raghupathi, L. Schkade and B.S. Raju, A Neural Network Application for Bankruptcy Prediction, IEEE International Joint Conference on Neural Networks (1991) 147–155.

[25] D.E. Rumelhart, G.E. Hinton, and R.J. Williams, Learning Internal Representations by Error Propagation, in: D.E. Rumelhart and J.L. McClelland, Eds., Parallel Distributed Processing: Exploration in the Microstructure of Cognition (MIT Press, Cambridge, MA, 1986).

[26] J.G. Siegel, Warning Signs of Impending Business Failure and Means to Counteract such Prospective Failure, The National Public Accountant (April 1981) 9–13.

[27] H. Takagi and I. Hayashi, NN-Driven Fuzzy Reasoning, International Journal of Approximate Reasoning 5 (1991) 191–212.

[28] K.Y. Tam and R. Chi, Inducing Stock Screening Rules for Portfolio Construction, Journal of Operations Research Society (1991, to appear).
