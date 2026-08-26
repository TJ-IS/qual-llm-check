---
otero_id: 17576
otero_key: "G6AMQUFR"
title: "A two-stage neural network approach for ARMA model identification with ESACF"
authors: "Jae Kyu Lee; Won Chul Jhee"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90019-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A two-stage neural network approach for ARMA model identification with ESACF

Jae Kyu Lee

Korea Advanced Institute of Science and Technology, Seoul, Korea

Won Chul Jhee

Hong Ik University, Seoul, Korea

We attempt to design artificial neural networks that can help in the automatic identification of the Autoregressive Moving Average (ARMA) model. For this purpose, we adopt the Extended Sample Autocorrelation Function (ESACF) as a feature extractor, and the Multi-Layered Perceptron as a Pattern Classification Network. Since the performance test from the network is sensitive to the noise in input ESACF patterns, we suggest a preprocessing Noise Filtering Network. It turns out that the Noise Filtering Network significantly improves the performance. To reduce the computational burden of training the full Pattern Classification Network, we suggest a Reduced Network that can still perform as good as the full network. The two-stage filtering and classifying networks performed very well (90% of accuracy) not only with the artificially generated data sets but also with the real world time series. We have also reconfirmed that the performance of ESACF is superior to that of ACF and PACF.

Keywords: Artificial Neural Network (ANN); Time series modeling; ARMA model identification; Extended sample autocorrelation function (ESACF); Pattern classification; Noise filtering; Backpropagation algorithm.

## 1. Introduction

Among various time series analysis techniques, ARMA modeling is one of the most widely used methods for managerial forecasting. A typical ARMA model building procedure consists of three steps: identification, parameter estimation, and diagnostic checking as depicted in Figure 1(a) [2]. Among these three steps, the identification step, which determines the order p of the AR process and the order q of the MA process to construct a model ARMA( $p$ , q), is very important in building a good model. However, this step requires expert judgment in interpreting statistical information such as the Autocorrelation Function (ACF) and the Partial Autocorrelation Function (PACF) [2], the ESACF [24], and so forth [1,7,12,22,29]. This is why the ARMA modeling procedure cannot be automated fully, and thus cannot be used widely in practical situations despite its theoretical comprehensiveness [17,27].

![](/api/attachments/G6AMQUFR/fulltext/images/1cdb1c72e884422a9c2b8ff3a8bde269d586b793ffeba09238c2059d2224a100.jpg)

Jae Kyu Lee is an associate professor in the Department of Management Information Systems in Korea Advanced Institute of Science and Technology at Seoul. He has received Ph.D. from the Wharton School, University of Pennsylvania. He has written several books on expert systems and numerous papers in Expert Systems with Applications: An International Journal, Expert Systems, Decision Support Systems, Decision Sciences, Fuzzy Sets and Systems, Interna tional Journal of Man-Machine Studies, etc. Currently, he serves as a member of editors for Expert Systems with Applications: An International Journal and International Journal of Intelligent Systems in Accounting, Finance and Management.

![](/api/attachments/G6AMQUFR/fulltext/images/e281cd8a592f97b274a9622982104edfb99e78c43d4da129673279220c7981d5.jpg)

Won Chul Jhee is an assistant professor in the department of Industrial Engineering at the Hong Ik University. He received B.B.A from Seoul National University, M.S. in I.E., Ph.D. in management information system from Korean Advanced Institute of Science and Technology. His research interests are business applications of neural networks, intelligent decision support systems, applied AI and knowledge-based simulation.

The purpose of our research is to automate the human judgment step of ARMA model identification by adopting the Artificial Neural Networks (ANN) approach based on selected statistical features as depicted in Figure 1(b) [3,14,15]. Thus, the key research issues are:

(1) Which statistical feature is most effective?

(2) How should the ANN be designed?

(3) How does the ANN approach perform?

(4) Can the ANN replace not only the identification step, but also the parameter estimation step?

To proceed with the research, we have decomposed the research into three projects.

(1) When we use ACF and PACF as statistical features, how does the ANN approach for ARMA model identification perform? [9].

(2) When we use ESACF as a statistical feature, how does the ANN approach perform in identification? What is the performance of this approach in comparison with that of the first approach?

(3) When a set of time series data is fed directly into the ANN as depicted in Figure 1(c), what is the forecasting performance in comparison with the two approaches above? [10].

We have dedicated one paper to each project, and this paper is the result of the second project. The remainder of this paper is organized as follows. In section 2, the ESACF approach to ARMA model identification is briefly reviewed. In section 3, an ANN - specifically a Multi-Layered Perceptron with two hidden layers (MLP2H) - is designed for ESACF pattern classification; data sets for experiments are generated; the network is trained by backpropagation algorithm; and the performance is evaluated. In section 4, we introduce a preprocessing ANN to reduce the noises in the original ESACF patterns, and briefly discuss the effect of features by comparing the performance of ESACF with that of ACF and PACF. In section 5, we suggest a Reduced Pattern Classification Network (Reduced PCN) with simpler architecture than MLP2H, in an attempt to enhance computational efficiency. The performance of the Reduced PCN is tested using noise-filtered ESACF patterns as inputs. In section 6, we show the usefulness of the two-stage neural network approach by testing on three real world economic time series data.

a) Traditional ARMA Model Building Procedure  
![](/api/attachments/G6AMQUFR/fulltext/images/48e97a7dada35b5a894f1de108a4007303bb0d30807b3ac8d424d20de0e8b5ab.jpg)

b) Automate the Identification Step by Adopting the ANN  
![](/api/attachments/G6AMQUFR/fulltext/images/98299d3cd33db190bee580621127c7cc668855386423a3d2b5f5b13fb7af11c9.jpg)

c) Modeling the Whole Procedure by an ANN

![](/api/attachments/G6AMQUFR/fulltext/images/3a6aae613b3d6996e22b0a16ddbc8055dc2871801d912db1da34ab9230dc821a.jpg)  
Fig. 1. ARMA model building procedure and suggested approaches.

## 2. Extended Sample Autocorrelation Function

Since we use ESACF as a statistical feature in this project, let us review the definition and properties of ESACF. The ESACF table looks like the example given in Figure 2(a). Since the Figure 2(a) is not easy to read, we convert the table into a format resembling that of Figure 2(b), which shows the theoretical prototype pattern of ARMA(1, 1) without any noise. With this figure, all a human expert has to do is to find the vertex of the triangle of 1's. However, this task may not be straightforward if noises exist as in Figure 2(c), which is converted from Figure 2(a). Furthermore, a time series with some seasonality can often yield multiple overlapping triangular patterns which make it difficult for the human analyzer to select the right vertex. Thus, it is essential to automate the judgment process. Therefore, our objective is to build an ANN which receives the converted ESACF pattern as input and classifies it into the ARMA(p, q) model as depicted in Figure 3. Before moving to the issue of the ANN design, we briefly summarize the ESACF approach to explain how to get such a pattern from a set of time series data. Readers may skip the remainder of this section if they are not particularly interested in statistics.

An ARMA $(p, q)$ model for a time series $\{z_t, t = 0, \pm 1, \pm 2, \ldots\}$ is expressed as:

$$
\begin{array}{r l} z _ {t} & = \phi_ {1} z _ {t - 1} + \dots + \phi_ {p} z _ {t - p} + a _ {t} - \theta_ {1} a _ {t - 1} - \dots \\ & - \theta_ {q} a _ {t - q}, \end{array} \tag {1}\tag{1}
$$

where $\{a_{t}\}$ consists of normally distributed independent random variables from $\mathbb{N}(0,\sigma^{2})$ , and $\phi$ 's and $\theta$ 's are autoregressive (AR) and moving average (MA) parameters to be estimated, respectively.

For the selection of appropriate orders $(p, q)$ , Tsay and Tiao [24] extend the Box-Jenkins method using the property that the Sample Autocorrelation Function (SACF) of pure MA(q) model abruptly drops to zeros after lag q, which is called “cut-off behavior” [2]. Since the moving average portion in (1) is the residuals from the autoregression of order p, i.e. AR(p) regression, they first developed the iterated regressions to obtain consistent estimates of the AR parameters. Since the estimates from the j-th iterated AR(k) regression can be recursively computed using the ordinary least square estimates of AR(k), AR(k+1), $\cdots$ , AR(k+j) fittings, the ESACF approach can be computationally efficient. Furthermore, there is no need to worry about the order of differencing which is indispensable for Box-Jenkins method, because the j-th iterated regression procedure yields consistent estimates of true AR parameters even for the nonstationary ARMA(k,q) model if j>q. Therefore, for each assumed value k for p, the k-th ESACF is defined as follows:

Definition The value of the k-th ESACF at lag j is defined as the sample autocorrelation of an estimate of the moving average portion, which is the residuals of the j-th iterated AR(k) regression.

The k-th ESACF for the ARMA $(p, q)$ model has the following properties:

(1) If $k = 0$ , ESACF is just the ordinary ACF in the Box-Jenkins method.

a) An Illustrative ESACF Table

<table><tr><td> $_{AR}^{\backslash MA}$ </td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0.57</td><td>0.50</td><td>0.40</td><td>0.36</td><td>0.33</td><td>0.35</td><td>0.39</td><td>0.32</td><td>0.30</td><td>0.25</td></tr><tr><td>1</td><td>-0.39</td><td>0.01</td><td>-0.06</td><td>-0.01</td><td>-0.06</td><td>-0.01</td><td>0.15</td><td>-0.07</td><td>0.01</td><td>0.04</td></tr><tr><td>2</td><td>-0.29</td><td>-0.27</td><td>-0.04</td><td>0.01</td><td>-0.05</td><td>-0.01</td><td>0.16</td><td>0.03</td><td>0.04</td><td>0.07</td></tr><tr><td>3</td><td>-0.50</td><td>-0.01</td><td>0.10</td><td>-0.01</td><td>-0.01</td><td>-0.03</td><td>0.16</td><td>-0.03</td><td>0.11</td><td>-0.02</td></tr><tr><td>4</td><td>-0.48</td><td>-0.02</td><td>0.08</td><td>-0.02</td><td>-0.01</td><td>-0.04</td><td>0.14</td><td>0.03</td><td>0.09</td><td>-0.03</td></tr><tr><td>5</td><td>-0.39</td><td>-0.41</td><td>-0.17</td><td>0.01</td><td>-0.17</td><td>-0.02</td><td>0.10</td><td>-0.01</td><td>0.06</td><td>0.07</td></tr><tr><td>6</td><td>-0.49</td><td>0.15</td><td>-0.18</td><td>0.00</td><td>-0.26</td><td>-0.06</td><td>0.09</td><td>-0.10</td><td>0.05</td><td>0.02</td></tr><tr><td>7</td><td>0.18</td><td>-0.02</td><td>0.04</td><td>0.33</td><td>0.26</td><td>-0.09</td><td>-0.23</td><td>0.03</td><td>0.01</td><td>0.03</td></tr><tr><td>8</td><td>0.31</td><td>0.07</td><td>0.00</td><td>0.25</td><td>0.30</td><td>-0.11</td><td>-0.15</td><td>0.13</td><td>-0.03</td><td>0.01</td></tr><tr><td>9</td><td>0.50</td><td>-0.02</td><td>0.01</td><td>0.17</td><td>-0.03</td><td>0.15</td><td>-0.08</td><td>0.13</td><td>0.01</td><td>0.01</td></tr></table>

b) The Prototype Pattern of the Converted ESACF Table for ARMA(1,1)

<table><tr><td>AR\MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td> $\frac{1}{2}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td><td> $\frac{1}{1}$ </td></tr><tr><td>2</td><td>0</td><td>0</td><td> $\frac{1}{1}$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\frac{1}{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\frac{1}{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\frac{1}{0}$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\frac{1}{0}$ </td><td>1</td><td>1</td></tr><tr><td>8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

c) The Converted ESACF Table from (a)

<table><tr><td>AR\MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>7</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>9</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

Fig. 2. Example of ESACF pattern for ARMA(1, 1) model This example is extracted from the Series A in Box & Jenkins (1976).

(2) If 0 < k < p, ESACF cannot display cut-off behavior because the estimated residuals still have some information about the AR process.

(3) If $k = p$ , ESACF shows the cut-off behavior after lag q because the estimated residuals from the j-th iterated AR(k) regressions follow an pure MA(q) process when j > q.

(4) If k > p, ESACF can display cut-off behavior when $0 \leq k - p < j - q$ , because the effect of overfitting the AR order leads to an increase in the MA order of the estimated residuals.

![](/api/attachments/G6AMQUFR/fulltext/images/bedd4e108cbace3f158e7b259d666be874dfd7bf3230cbc37289a51edbd2ad58.jpg)  
Fig. 3. ESACF pattern classification with Multi-Layered Perceptron of two hidden layers.

Therefore, if we arrange the ESACF values in a two-way table, the model can be identified by finding the vertex of a triangle of asymptotic zero values. To facilitate this task, we can transform each element of ESACF table into binary value using the rule: If the ESACF value lies between its two standard deviations, $^{1}$ then convert it 1; otherwise convert it 0. Using this supplementary procedure, we can theoretically obtain the triangular pattern of 1's which has its boundary lines at k = p and j - k = q - p in the case of ARMA(p, q) model. As shown in Figure 2(b), the row and column coordinates of the vertex correspond precisely to the AR and MA order, respectively. However, Figure 2(b) merely represents an ideal prototype pattern. In practical situations, the noisy ESACF patterns as in Figure 2(c) are usually obtained from the time series. Therefore, our problem is to classify the noisy ESACF patterns into the ARMA model by determining the degree of matching between noisy ESACF patterns with the prototype patterns using the ANN approach.

## 3. The Multi-Layered Perceptron approach for ARMA model identification

For the identification of ARMA models with ESACF patterns, we adopted the Multi-Layered Perceptron (MLP) which is one of the most widely used ANN models as pattern classification networks (PCN) [15,20]. MLP is a feedforward network in which a Processing Element (PE) in one layer is fully connected with all PE's in the adjacent layer. For the training of MLP, we used a backpropagation algorithm [21,26], which consists of three steps: forward pass, backward pass, and weight update as depicted in Figure 3. Since each connection between PE's has a corresponding weight, learning in the backpropagation algorithm is achieved by adjusting the weights based on the given training data set of input/output pairs.

## 3.1. Design of the network

To configure the structure of MLP, we need to describe the number of hidden layers, the number of PE's in each layer, and the types of activation functions for PE's. These issues are handled in the following way:

(1) We adopt two hidden layers in order to exploit the full classification power of MLP [15].

(2) Since we use $10 \times 10$ ESACF table, we arrange 100 corresponding input PE's. By the same token, since we consider the maximum orders of $p = 5$ and $q = 5$ , we arrange 35 output PE's which correspond to $(p + 1)(q + 1) - 1$ PE's.

(3) The number of hidden PE's affects the convergence rate in learning and the performance of MLP. In general, the increased number of hidden PE's will improve the recognition performance. However, excessive use may cause the MLP to try to learn from unnecessary noise in training patterns which may deteriorate the generalization power. On the other hand, too small a number of hidden PB's may lead to slow convergence and bad performance. Therefore, many researchers have tried to find an appropriate size by simulating a various number of hidden PB's [4,13]. In the MLP2H, we adopt 70 and 50 PB's in the first and second hidden layer respectively as a starting point.

(4) The sigmoid function is adopted as an activation function for all PE's in hidden and output layers.

## 3.2. Data sets for experiments

To make the MLP2H robust to the input noises, we added noises to our training data sets, and generated four groups each of which included ESACF patterns with different noise levels: 0%, 10%, 20%, and 30%. By using these four data groups, we can observe the impact of noises in the training data set. The training data sets are prepared as follows:

(1) To add noises into a pure ESACF prototype pattern, we randomly inverted 10, 20 and 30 binary values respectively. Prototypes were considered to have 0% noise level.

(2) Since the noises in the triangle easily break the original shape of the ESACF pattern, we restricted the number of noises in the triangle to less than 12 - p - q.

(a) Classification Performance of MLP2H for Each Noise Level in the Test Sets  
![](/api/attachments/G6AMQUFR/fulltext/images/2b0f144e8dc559def0bf0285df3d12ef3153333aa999e75652f21580dbfc55ee.jpg)

(b) Effects of Training Sets on the Classification Performance of MLP2H  
![](/api/attachments/G6AMQUFR/fulltext/images/995505179f70a1d3818802fde4b754e71d504947b8ee526e1317665f4fdd8c06.jpg)  
Fig. 4. Test results from MLP with two hidden layers.

(3) In the target output vector, the ARMA $(p,q)$ model had “1” in the $(6p+q)$ -th element while having zeros in the remainders.

(4) After generating five noisy patterns for each noise level of each ARMA $(p, q)$ model with their corresponding target output vectors, we organized these input/output pairs into the following four training data sets:

1. the first set had 35 prototype patterns;

2. the second set had 210 patterns (the first set plus 175 patterns of 10% noises, i.e., 5 noisy patterns for each of 35 ARMA models);

3. the third set had 385 patterns (the second set plus 175 patterns of 20% noises); and

4. the fourth set had 560 patterns (the third set plus 175 patterns of 30% noises).

To test the performance of the learned ANN's, we generated the test patterns with different noise levels in the same way we prepared the training data sets. We prepared 15 test sets, each of which consisted of 210 test patterns: 2 noisy ESACF patterns for each ARMA model for each of three noise levels (10%, 20%, 30%). Therefore, each test set can be divided into 3 subsets of different noise levels, each of which has 70 patterns.

## 3.3. Training

Before we start the training, the binary values of 0 or 1 in training sets are transformed into 0.1 and 0.9 respectively to facilitate the learning. Since convergence behavior in backpropagation algorithm can be regulated by the learning rate $\eta$ , which can be globally or locally fixed [8], and the constant $\alpha$ for the momentum term [21], we adopted $\eta = 0.1$ and $\alpha = 0.9$ . We stop the training when the average squared error becomes less than the predetermined error bound of 0.005.

We have applied a step-by-step training method to the four training sets. First, the training starts with the first training set. Once the MLP2H has reached the predetermined error bound, the learned MLP2H is trained again with the second training set. This iterative procedure continues with the third and fourth training sets. By adopting this approach, we can compare the performances of MLP2H's which have learned from the training sets of different noise levels. In addition, we have confirmed that the incremental increase of the noise level during the learning phase reduced the training time and led to stable learning over the noisy training sets. Similar experimental results were reported by Waibel et al. [25].

![](/api/attachments/G6AMQUFR/fulltext/images/4351f1603472f460a1d78b07cfac901473faeed90558ccec3bf2584ff06b2af6.jpg)  
Fig. 5. The structure of Noise Filtering Network.

Table 1  
Average classification accuracy of MLP2H for each test subset as a function of training sets

<table><tr><td rowspan="2">Noise Level in test subset</td><td colspan="4">Noise level in training sets</td><td rowspan="2">One-way ANOVA test: F(3, 56)</td></tr><tr><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td></tr><tr><td>10%</td><td>94.95 (2.80) *</td><td>96.86 (2.40)</td><td>95.81 (2.24)</td><td>96.10 (2.11)</td><td>1.50 p = 0.224 **</td></tr><tr><td>20%</td><td>75.05 (3.25)</td><td>78.86 (4.43)</td><td>84.10 (2.75)</td><td>83.04 (2.90)</td><td>20.85 p &lt; 0.001</td></tr><tr><td>30%</td><td>55.33 (4.15)</td><td>58.29 (5.88)</td><td>65.05 (4.72)</td><td>65.72 (5.11)</td><td>15.01 p &lt; 0.001</td></tr><tr><td>Average over all subsets</td><td>75.11 (2.01)</td><td>78.00 (3.06)</td><td>81.65 (2.10)</td><td>81.71 (2.52)</td><td>23.50 p &lt; 0.001</td></tr></table>

Legend:  
\* standard deviation.  
\*\* F probability.

Under the training setting, the MLP2H for each training set required 791, 882, 917 and 969 epochs respectively to converge into the predetermined error bound. The trained MLP2H correctly recognized all the patterns in the training sets.

## 3.4. Test and discussions

For each of three noise levels in test sets, the classification accuracy of the MLP2H is tested. The results are displayed in Figure 4(a). To know the effect of noises in training sets, the averaged performance of the MLP2H learned from each training set is also tested. The results are summarized in Figure 4(b) and Table 1.

From the above test results, we can first observe that the designed MLP2H suffers in classifying the test patterns with the higher noise level, although the MLP2H can learn from noisy training patterns. As shown in Figure 5 and the fifth column in Table 1, the averaged classification accuracy drops from 96.1% to 83.0% and 65.7% as the noise level in the test patterns increases from 10% to 20% and 30% respectively. The result of one-way analysis of variance, F(2, 42) =

244.93 p < 0.001, supports this hypothesis. The observation implies that the higher the noise level of the test pattern, the higher the risk of wrong classification. This general principle is a fact of life which we cannot overcome, even though we may be able to ameliorate the issue to some extent.

Our second observation is that the performance of the MLP2H trained by the fourth training set had not improved at all in comparison with the results by the third training set. For instance, the performance of the 20% noisy test patterns had even fallen slightly. The F-values in Table 1 tell us the effect of noise levels in training sets. When the test subset has a 10% noise level, we cannot accept the significant effect of training sets because $F(3, 56) = 1.50 \quad p = 0.224$ . However, test subsets with 20% and 30% noise levels were significantly affected by the noise levels of training sets for $F(3, 56) = 20.85 \quad p < 0.001$ and $F(3, 56) = 15.01 \quad p < 0.001$ respectively. In spite of these effects of the training set, Scheffe's procedure in one-way ANOVA analysis [18] indicated that there is no difference between the results from third and fourth training sets. Therefore, we confirm that training sets with too high a noise level do not contribute to improvements in the performance of the MLP2H.

From these observations, we conclude that it is necessary to devise a step that can reduce noises in the original ESACF patterns. This requires us to introduce a preprocessing Noise Filtering Network (NFN) before the ESACF Pattern Classification Network (PCN). The following section deals with NFN.

## 4. Noise filtering network

## 4.1. Design of the network

As we have observed in the previous section, if the noises in ESACF patterns can be eliminated or reduced below a 10% noise level, the PCN's performance can be about 95%. To implement this idea, we suggest a two-stage neural network approach by adopting a Noise Filtering Network as a predecessor to PCN. The role of NFN is to filter noises in the ESACF patterns to recover patterns as close as the triangular prototype patterns seen in Figure 2(b). By the nature of noise filtering, NFN should be able to respond to highly noisy ESACF patterns.

As a candidate model of NFN, we can consider the content addressable memories or associative memories which are useful when only a cue for an input pattern is available and the recall of the complete pattern of the class exemplar or prototype is necessary $[15,20]$ . Since theoretical prototypes of ESACF patterns exist, it seems that associative memories can be easily applied to our problem and can give us the benefit of greatly reduced training efforts because the associative memories require only class exemplars for training. However, associative memories such as the Hopfield Network $[6]$ may not be appropriate for identifying ARMA models with ESACF for the following two reasons:

(1) The number of classes in associative memories should be kept well below 15% of the input PE number, the so-called limitation of memory capacity [16]. Therefore, 35 ARMA model classes are excessively large.

(2) Since similar ESACF prototypes have much in common with each other, the recall of the exemplar pattern may be very unstable [15].

Thus, we use a multi-layered perceptron as the ANN model for NFN, but make the MLP behave like associative memories by making the input and output layers of NFN have the same number of PB's as depicted in Figure 5.

In the NFN, we used only one hidden layer whose number of PB's is smaller than those in input/output layers. The reduction in the hidden PE number will clear out the noises by abstracting the essential information about the triangular region in the input pattern and by restoring it in the output layer. This process will recover the ESACF pattern as close as its prototype. To trace the effect of the number of the hidden PE's, we examine 4 cases: 55, 60, 65 and 70 hidden PE's.

## 4.2. Training

For the training of NFN, we prepared four training sets of different noise levels by mapping the noisy ESACF patterns with the theoretical ESACF prototypes. We adopted the backpropagation algorithm and the step-by-step training method as we did for the MLP2H. However, we used 0.01 as a predetermined error bound, and to prevent oscillations of error, the learning rate $\eta$ was lowered from 0.1 to 0.05 when the NFN learns from the fourth training set. Table 2 shows, for each training set, the number of cumulative epochs for each hidden PE number for each training set. The learned NFN correctly recognized all training patterns.

![](/api/attachments/G6AMQUFR/fulltext/images/3e5b87f3fb1349add508f1b61d00384ee074a2b80c858854597658741dfc65ba.jpg)  
Fig. 6. Average noise level after filtering by the Noise Filtering Network.

Table 2  
Cumulative epochs for the convergence of noise filtering network as a function of hidden PE numbers

<table><tr><td rowspan="2">Number of hidden PE&#x27;s in NFN</td><td colspan="4">Noise level in training sets</td></tr><tr><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td></tr><tr><td>55 PE&#x27;s</td><td>214</td><td>317</td><td>493</td><td>1104</td></tr><tr><td>60 PE&#x27;s</td><td>186</td><td>301</td><td>475</td><td>718</td></tr><tr><td>65 PE&#x27;s</td><td>159</td><td>253</td><td>456</td><td>676</td></tr><tr><td>70 PE&#x27;s</td><td>137</td><td>216</td><td>434</td><td>648</td></tr></table>

## 4.3. Tests and discussions

We use the 15 test sets used in section 3, each of which consisted of 210 patterns that can be further divided into 3 subsets of 10, 20 and 30% noise levels. Before we discuss the effect of a hidden PE number, let us analyze the performance of the NFN with 65 hidden PE's. The results are graphically shown in Figures 6 and 7. The input noises 10%, 20%, and 30% are significantly reduced to 0.67%, 2.11%, and 5.62%, respectively. Owing to the noise reduction, we anticipate that the PCN can classify the ESACF patterns better than the performance of the test set with 10% noise in Table 1.

To validate the idea, we have tested the performance of PCN with the filtered patterns by NFN. Figure 7 shows the average performance of the MLP2H for the total test patterns (solid lines) and the 30% noise level test patterns (dotted lines) for each test set. We can observe that the performance of the MLP2H with a noise filtering stage is superior to that of the MLP2H without noise filtering for all test patterns. This performance gap becomes even larger for the 30% noise level. The t-test supports the significant difference between them by the value of t = 6.98 p < 0.001 in Table 3. For total test patterns, average classification accuracy of the MLP2H with NFN is increased to 89.05% from 81.71% by the MLP2H without noise filtering. However, the MLP2H with NFN failed to perform to our expectation. This is caused by wrong filtering in NFN.

The analysis of noise-filtered patterns revealed that two types of noises are left:

(1) The noise filtered pattern still has some spurious values. The shaded areas in Figure 8(a) represent the noises which NFN does not eliminate. This type of noise occurs when the input pattern has overlapping triangles.

![](/api/attachments/G6AMQUFR/fulltext/images/a9bcc5a30466f19d5996e5d5937a86f1456ff5e7d415e1c16bc1e9f91e80a275.jpg)  
Fig. 7. Average classification accuracy of MLP2H with Noise Filtering Network of 65 Hidden PE's.

Table 3  
Average classification accuracy of PCN's with NFN of 65 hidden PE's

<table><tr><td rowspan="2">Noise level in test subsets</td><td colspan="3">MLP&#x27;s used in experiments</td></tr><tr><td>MLP2H w/o NFN</td><td>MLP2H with NFN</td><td>R. PCN† with NFN</td></tr><tr><td>10%</td><td>96.10(2.11) *</td><td>96.67(2.74)</td><td>97.05(2.78)</td></tr><tr><td>20%</td><td>83.04(2.90)</td><td>89.71(3.50)</td><td>89.62(3.10)</td></tr><tr><td>30%</td><td>65.72(5.11)</td><td>80.76(5.30)</td><td>79.43(4.36)</td></tr><tr><td>Average over test subsets</td><td>81.71(2.52)</td><td>89.05(2.97)</td><td>88.70(2.69)</td></tr><tr><td>t-values</td><td colspan="3"> $6.98 \ p < 0.001$  **  $-1.54 \ p = 0.129$ </td></tr></table>

Legend:  
\* standard deviations,

Table 4  
Average classification accuracy of NFN on total test sets as a function of hidden PE numbers

<table><tr><td rowspan="2">Number of hidden PE&#x27;s in NFN</td><td colspan="4">Noise level in training sets</td><td rowspan="2">t-values</td></tr><tr><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td></tr><tr><td>55 PE&#x27;s</td><td>74.16(3.17) *</td><td>78.89(2.68)</td><td>82.35(2.36)</td><td>84.22(2.88)</td><td>-</td></tr><tr><td>60 PE&#x27;s</td><td>76.16(2.17)</td><td>80.98(2.32)</td><td>85.30(1.96)</td><td>88.03(2.61)</td><td>3.62 $p = 0.001^{**}$ </td></tr><tr><td>65 PE&#x27;s</td><td>75.49(3.79)</td><td>83.08(2.92)</td><td>86.67(2.27)</td><td>90.32(2.55)</td><td>2.17 $p = 0.034$ </td></tr><tr><td>70 PE&#x27;s</td><td>74.32(3.23)</td><td>79.14(3.34)</td><td>83.97(3.06)</td><td>88.89(3.08)</td><td>-1.36 $p = 0.193$ </td></tr></table>

Legend:  
\* standard deviations  
\*\* $t$ probability,  
† The Reduced PCN model is discussed in section 5.  
\*\* $t$ probability.

(2) The noise filtered pattern is a clean triangular pattern, but it does not match with its corresponding prototype. That means the pattern is wrongly recovered. In Figure 8(b), the solid-line triangle is a desired prototype while the dotted-line triangle is one that is wrongly recovered one by NFN.

We found that as the noise level in ESACF patterns goes up, the probability of triangles overlapping goes up. This is why the performance by the 30% noise level is inferior to the one by total patterns in Figure 7.

To determine the structure of NFN, we compare the performance of NFN with different numbers of hidden PB's: 55, 60, 65, and 70. The values in noise-filtered patterns are changed into binary values using the threshold of 0.7. For each hidden PE number, the changes in the performance of NFN are shown in Table 4.

According to the three-way ANOVA test, the number of hidden PE's significantly affected the performance of NFN. F-values of three main effects (the noise level in the training set, the noise level in the test set, and the hidden PB number) were $F(3, 852) = 426.71 \quad p < 0.001$ , $F(2, 852) = 4747.44 \quad p < 0.001$ , and $F(3, 852) = 37.21 \quad p < 0.001$ , respectively. Our second observation with respect to hidden PE numbers is that performance improves as the number of hidden PE's increases to 65. However, increasing the hidden PE number to 70 did not bring further improvement, although it required less training epochs as shown in Table 2. This observation was supported by the one-way ANOVA test on the performance results obtained from NFN. That is,

![](/api/attachments/G6AMQUFR/fulltext/images/be67c757e56386aa5c20d89912284413f54c32c250cbb1c052a54d65ab747e29.jpg)  
(a) Recovered Pattern with Some Spurious Values

![](/api/attachments/G6AMQUFR/fulltext/images/59703ccc45338581f6024106d6d3333cbeaa864f3d5b76db07bcb64dcc42c73e.jpg)  
(b) Wrongly Recovered Pattern  
Fig. 8. Two types of noise distributions in the noise-filtered test patterns.

Table 5  
![](/api/attachments/G6AMQUFR/fulltext/images/0c39974357467395be16d1b937666f7a9a26320c340fac989323cb08facfe7cf.jpg)  
Fig. 9. Architecture of Reduced Pattern Classification Network.

$F(3, 56) = 12.24 \quad p < 0.001$ . Although Scheffe's procedure did not indicate differences among the performances of 60, 65 and 70 hidden PB's, the pairwise $t$ -tests support that the difference between 60 and 65 hidden PB's is $t = 2.17 \quad p = 0.034$ , although the difference between 65 and 70 hidden PE's cannot be strongly supported because $t = -1.36 \quad p = 0.180$ .

We have also confirmed that the performance of NFN with 65 hidden PE's on test subsets of a 30% noise level significantly increases as the noise level in training sets increases. The ANOVA test confirms that $F(3, 56) = 70.15 \quad p < 0.001$ . Specifically, performance is improved by 17% when we compared the result (82.76%) from NFN with that without noise filtering stage (65.72% in Table 1).

The average number of wrongly recovered noise-filtered patterns that indicated incorrect ARMA models

<table><tr><td rowspan="2">Noise Level in test subsets</td><td colspan="4">Deviations in AR of MA Order</td><td rowspan="2">Total</td></tr><tr><td>AR1</td><td>MA1</td><td>AR1/MA1</td><td>Others</td></tr><tr><td>10%</td><td>0.00(0.00) *</td><td>1.43(2.04)</td><td>0.29(0.41)</td><td>0.29(0.41)</td><td>2.01(2.87)</td></tr><tr><td>20%</td><td>0.29(0.41)</td><td>3.86(5.51)</td><td>1.26(1.80)</td><td>0.86(1.23)</td><td>6.27(8.96)</td></tr><tr><td>30%</td><td>0.71(1.01)</td><td>5.86(8.37)</td><td>2.57(3.67)</td><td>2.92(4.17)</td><td>12.06(17.22)</td></tr><tr><td>Total</td><td>1.00(0.47)</td><td>11.15(5.31)</td><td>4.12(1.96)</td><td>4.07(1.94)</td><td>20.34(9.69)</td></tr></table>

Legend:

In short, our NFN correctly recovered 90.32% of 210 test patterns on the average. In other words, about 20 patterns in each test set were wrongly recovered. However, as shown in Table 5, even in the case of wrongly recovered patterns, most of them were only near-misses. AR1 and MA1 in Table 5 indicate that the identified $\hat{p}$ and $\hat{q}$ deviate from the original p and q by 1. Although NFN has performed relatively poorly in identifying MA orders, the performance of NFN is in general quite acceptable.

To experiment with the effect of the feature extractors, we apply the MLP2H with NFN to the data set used in our first project which adopted ACF and PACF as feature extractors [9]. According to our experiment, it is confirmed that ESACF performs much better than ACF and PACF. $^{2}$

## 5. Reduced Pattern Classification Network

## 5.1. Design of the network

Since the effort of training the MLP2H is a great burden, we attempt to design a reduced network which can perform as well as the MLP2H while reducing the training effort significantly. To implement the idea of a reduced network (let's call it Reduced PCN), we consider only one hidden layer with fewer input and output PE's. Figure 9 shows the structure of the Reduced PCN, including the number of PE's in each layer. The sigmoid activation function is also used in all hidden and output PE's.

## 5.1.1. Preprocessing the noise-filtered ESACF pattern

We reduce the number of input PE's by utilizing the boundary information of the triangular region. For this purpose, we process $m \times n$ noise-filtered ESACF patterns to prepare the input vectors for Reduced PCN in the following way: (see Figure 10)

(1) ESACF values are averaged row-wise and column-wise respectively.

(2) ESACF values in two adjacent left-to-right diagonal lines are divided by 2m.

The above preprocessing method reduces the input PE number from mn to $2(m+n)-1$ . Therefore, the number of input PE's for Reduced PCN is reduced from 100 to 39.

## 5.1.2. Partition of the Pattern Classification Network

We also reduce the output PE number by dividing the PCN into two sub-networks: one for the AR process and one for the MA process. Owing to the partitioning, we can reduce $(p +$

![](/api/attachments/G6AMQUFR/fulltext/images/ccea2bfbbb18ef918b9ca1adb800baddff88281e6accb0ba2a811d317ab5ebed.jpg)  
Fig. 10. Preprocessing method for the input of Reduced PCN.

1) $(q+1)-1$ output PB's in the MLP2H to $(p+1)$ output PE's for the AR network and $(q+1)$ output PB's for the MA network. When p=q=5, the output PE's fall from 35 to 6 in each sub-network.

## 5.2. Training

To eliminate the effect of wrong-filtered patterns as in Figure 9(b), we collected 126 patterns excluding such wrong-filtered patterns. The input vectors are prepared as described in section 5.1.1. Then two reduced networks (AR and MA) are trained by the backpropagation algorithm. For both networks, we used $\eta = 0.1$ , $\alpha = 0.9$ and the predetermined error bound was 0.001.

The learned AR and MA networks correctly recognized all their training patterns as shown in Table 6. The Reduced PCN required 63% of the training time required for the MLP2H.

## 5.3. Test and discussions

We tested the performance of AR and MA networks using the noise filtered test patterns from NFN with 65 hidden PB's. To eliminate the bias that might be caused by wrongly recovered

Training and test results of PCN's on correctly noise-filtered patterns

<table><tr><td>Models of PCN</td><td></td><td>Epochs</td><td>Training Time</td><td>Recognition of Training Set</td><td colspan="2">Classification Accuracy of Test Set</td></tr><tr><td>MLP2H</td><td></td><td>467</td><td>100%</td><td>100%</td><td colspan="2">97.33% (1.39) *</td></tr><tr><td>Reduced</td><td>AR</td><td>889</td><td>12%</td><td>100%</td><td>96.60%</td><td>99.79 (1.39) *</td></tr><tr><td>PCN</td><td>MA</td><td>2122</td><td>51%</td><td>100%</td><td>(2.03)</td><td>97.05 (1.94)</td></tr></table>

Legend:  
\* standard deviation.

patterns, we first remove the wrongly recovered test patterns from NFN. The average number of patterns with this qualification in 15 test sets is 189.66. As shown in Table 6, the percentage of correct classifications by the MLP2H is 97.33%, while the performances by the AR and MA networks are 99.79 and 97.05% respectively. The percentage that correctly classified the orders of both AR and MA models is 96.6%. According to the F-test, the performances of the MLP2H and

![](/api/attachments/G6AMQUFR/fulltext/images/d297374ac185d950d213259b74025eac12ad49ae384e23137a5aecf74a4efc18.jpg)  
Fig. 11. Flow diagram of experiment with the two-staged neural network approach.

Reduced PCN do not reveal any significant differences because $F(1, 28) = 1.33 \ p = 0.259$ . One thing of note is that, as is the case with NFN, the MA network did not perform as well as the AR network. Even when we include the wrongly recovered patterns from NFN, the performance of Reduced PCN is as good as that of MLP2H as shown in Table 3, although the performance of both networks fell to 89.05% and 88.70%.

Therefore, we use the Reduced PCN in place of the MLP2H without damaging to classification performance, and reduce the training efforts for PCN. The two-stage neural network approach consists of three MLP's – namely, NFN, AR and

(a)

<table><tr><td>AR\MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>5</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>6</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>7</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>9</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

(b)

<table><tr><td>AR\MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0.100</td><td>0.107</td><td>0.099</td><td>0.105</td><td>0.096</td><td>0.096</td><td>0.096</td><td>0.096</td><td>0.096</td><td>0.096</td></tr><tr><td>1</td><td>0.099</td><td>0.116</td><td>0.111</td><td>0.118</td><td>0.100</td><td>0.093</td><td>0.092</td><td>0.092</td><td>0.093</td><td>0.093</td></tr><tr><td>2</td><td>0.873</td><td>0.907</td><td>0.907</td><td>0.900</td><td>0.914</td><td>0.907</td><td>0.901</td><td>0.901</td><td>0.901</td><td>0.901</td></tr><tr><td>3</td><td>0.113</td><td>0.899</td><td>0.984</td><td>0.905</td><td>0.900</td><td>0.915</td><td>0.909</td><td>0.900</td><td>0.900</td><td>0.900</td></tr><tr><td>4</td><td>0.115</td><td>0.112</td><td>0.895</td><td>0.903</td><td>0.906</td><td>0.900</td><td>0.914</td><td>0.909</td><td>0.900</td><td>0.900</td></tr><tr><td>5</td><td>0.100</td><td>0.115</td><td>0.112</td><td>0.895</td><td>0.903</td><td>0.906</td><td>0.900</td><td>0.914</td><td>0.914</td><td>0.900</td></tr><tr><td>6</td><td>0.100</td><td>0.100</td><td>0.115</td><td>0.112</td><td>0.895</td><td>0.903</td><td>0.907</td><td>0.900</td><td>0.914</td><td>0.910</td></tr><tr><td>7</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.115</td><td>0.112</td><td>0.895</td><td>0.903</td><td>0.907</td><td>0.900</td><td>0.914</td></tr><tr><td>8</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.115</td><td>0.112</td><td>0.895</td><td>0.903</td><td>0.907</td><td>0.900</td></tr><tr><td>9</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.115</td><td>0.112</td><td>0.895</td><td>0.903</td><td>0.907</td></tr></table>

(c)  
![](/api/attachments/G6AMQUFR/fulltext/images/4af441de927cb7bc2197226e61f72b220cb1630fe8fb1636b4310a6bbdc9caac.jpg)  
(d) AR Network : 0.1063 0.2140 0.8036 0.0952 0.0943 0.1023
MA Network : 0.9433 0.1583 0.0937 0.1127 0.1532 0.0831  
Fig. 12. Test result of the U.S. GNP Data: ARMA(2, 0) ((a) ESACF pattern (b) Noise Filtered Pattern (c) Preprocessed Values (d) Outputs of Reduced PCN).

MA Networks. Figure 11 summarizes the training and classification procedures in our two-stage approach.

## 6. Tests with real world data

In order to test the applicability of the two-stage approach in practical situations, we used three data sets of economic time series found in the real world.

CASE I: Quarterly Gross National Product of the U.S.

Figure 12 shows the test result obtained from U.S. quarterly GNP data between 1946 and 1970. The $10 \times 10$ converted ESACF pattern in Figure 12(a) has 24 different values from the prototype

(a)

$$
\begin{array}{c c c c c c c c c c c} \text {AR} ^ {\mathrm{MA}} & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\ \hline 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 0 \\ 2 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 1 \\ 3 & 1 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 1 & 1 \\ 4 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 1 & 1 \\ 5 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 \\ 6 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\ 7 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 1 \\ 8 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\ 9 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 1 \end{array}
$$

(b)

<table><tr><td>AR\MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0.100</td><td>0.094</td><td>0.095</td><td>0.103</td><td>0.091</td><td>0.091</td><td>0.091</td><td>0.091</td><td>0.091</td><td>0.091</td></tr><tr><td>1</td><td>0.062</td><td>0.044</td><td>0.093</td><td>0.107</td><td>0.087</td><td>0.077</td><td>0.074</td><td>0.074</td><td>0.074</td><td>0.075</td></tr><tr><td>2</td><td>0.165</td><td>0.890</td><td>0.770</td><td>0.891</td><td>0.913</td><td>0.914</td><td>0.891</td><td>0.890</td><td>0.891</td><td>0.891</td></tr><tr><td>3</td><td>0.004</td><td>0.005</td><td>0.222</td><td>0.103</td><td>0.223</td><td>0.264</td><td>0.256</td><td>0.225</td><td>0.225</td><td>0.225</td></tr><tr><td>4</td><td>0.109</td><td>0.100</td><td>0.139</td><td>0.900</td><td>0.799</td><td>0.899</td><td>0.920</td><td>0.920</td><td>0.900</td><td>0.900</td></tr><tr><td>5</td><td>0.100</td><td>0.110</td><td>0.100</td><td>0.140</td><td>0.901</td><td>0.799</td><td>0.899</td><td>0.920</td><td>0.920</td><td>0.900</td></tr><tr><td>6</td><td>0.100</td><td>0.100</td><td>0.110</td><td>0.100</td><td>0.139</td><td>0.901</td><td>0.800</td><td>0.899</td><td>0.920</td><td>0.920</td></tr><tr><td>7</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.109</td><td>0.100</td><td>0.139</td><td>0.900</td><td>0.799</td><td>0.899</td><td>0.920</td></tr><tr><td>8</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.109</td><td>0.100</td><td>0.139</td><td>0.900</td><td>0.799</td><td>0.899</td></tr><tr><td>9</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.109</td><td>0.139</td><td>0.900</td><td>0.799</td></tr></table>

(c)  
![](/api/attachments/G6AMQUFR/fulltext/images/bc38e9ce12720b93356729106a8ec6ae5fa8a2e9ef467e40fb861a859a041256.jpg)  
(d) AR Network : 0.1117 0.1034 0.4943 0.1014 0.9589 0.1069
MA Network : 0.1196 0.2586 0.1218 0.7230 0.1432 0.1068

Fig. 13. Test result of Consumer Price Index Data: ARMA(4, 3) ((a) ESACF pattern (b) Noise Filtered Pattern (c) Preprocessed Values (d) Outputs of Reduced PCN).

pattern of ARMA(2, 0). Although the pattern has 24% noise level, NFN completely removes noise. The underlined numbers in Figure 12(b) clearly represent a triangle whose vertex is found on the third row and the first column. Figure 12(c) shows the input to Reduced PCN which consists of 39 values obtained by preprocessing the noise-filtered pattern in Figure 12(b). Figure 12(d) shows the outputs of the AR and MA Networks.

The output vector of the AR Network has the largest value in the third element which means an AR order of 2. The output vector of the MA Network indicates an MA order of 0. Thus, the two-stage approach correctly classifies U.S. GNP data as AR(2, 0) without any difficulty.

Nelson [17] analyzed this data as AR(1) after applying the first order of integration filter, that is, differencing the data once. However, note that

(a)

$$
\begin{array}{c c c c c c c c c c c} \text {AR} ^ {\text {MA}} & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\ \hline 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & 1 & 1 & 1 & 0 & 1 & 0 & 0 & 1 & 1 \\ 2 & 1 & 1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 1 \\ 3 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 \\ 4 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\ 5 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 1 \\ 6 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 1 \\ 7 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 0 \\ 8 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\ 9 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 0 \end{array}
$$

(b)

<table><tr><td>AR\MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0.100</td><td>0.166</td><td>0.008</td><td>0.091</td><td>0.081</td><td>0.081</td><td>0.081</td><td>0.081</td><td>0.081</td><td>0.081</td></tr><tr><td>1</td><td>0.370</td><td>0.173</td><td>0.251</td><td>0.038</td><td>0.211</td><td>0.186</td><td>0.184</td><td>0.188</td><td>0.189</td><td>0.189</td></tr><tr><td>2</td><td>0.098</td><td>0.856</td><td>0.743</td><td>0.837</td><td>0.548</td><td>0.900</td><td>0.899</td><td>0.899</td><td>0.899</td><td>0.899</td></tr><tr><td>3</td><td>0.099</td><td>0.212</td><td>0.857</td><td>0.758</td><td>0.835</td><td>0.524</td><td>0.895</td><td>0.899</td><td>0.899</td><td>0.899</td></tr><tr><td>4</td><td>0.080</td><td>0.101</td><td>0.216</td><td>0.861</td><td>0.756</td><td>0.835</td><td>0.520</td><td>0.901</td><td>0.900</td><td>0.900</td></tr><tr><td>5</td><td>0.100</td><td>0.081</td><td>0.101</td><td>0.216</td><td>0.861</td><td>0.755</td><td>0.835</td><td>0.521</td><td>0.901</td><td>0.900</td></tr><tr><td>6</td><td>0.100</td><td>0.100</td><td>0.081</td><td>0.101</td><td>0.217</td><td>0.861</td><td>0.756</td><td>0.835</td><td>0.521</td><td>0.901</td></tr><tr><td>7</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.080</td><td>0.101</td><td>0.217</td><td>0.861</td><td>0.756</td><td>0.835</td><td>0.521</td></tr><tr><td>8</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.080</td><td>0.101</td><td>0.217</td><td>0.861</td><td>0.755</td><td>0.835</td></tr><tr><td>9</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.080</td><td>0.101</td><td>0.217</td><td>0.861</td><td>0.755</td></tr></table>

(c)  
![](/api/attachments/G6AMQUFR/fulltext/images/e25a0f97b2e97394cbbd36a9ab086f3cf58665bfce8132d6abdfa55a866e8df9.jpg)  
(d) AR Network : 0.0956 0.2824 0.5405 0.1114 0.0954 0.1016
MA Network : 0.0318 0.3816 0.0000 0.0286 0.1053 0.6980  
Fig. 14. Test result of the Caffeine Data: ARMA(2, 5) ((a) ESACF pattern (b) Noise Filtered Pattern (c) Preprocessed Values (d) Outputs of Reduced PCN).

the AR(1) process with a differencing is equivalent to the ARMA(2, 0) process, and the adoption of ESACF does not require any differencing before the specification of the ARMA(2, 0) model.

CASE II: Monthly Consumer Price Index of the U.S.

It is known that the monthly U.S. CPI data between 1953 and 1970 has a strong exponential trend, and ARMA(4, 3) is an appropriate model for this time series [19]. If we use the Box-Jenkins method, we must determine the order of differencing to eliminate the trend in the time series. However, we can obtain the ESACF pattern in Figure 13(a) from the raw time series without differencing. The ESACF pattern has a $27\%$ noise level and indicates two possible models: ARMA(2, 1) or ARMA(4, 3). The noise-filtered pattern has some spurious values like Figure 9(a) - i.e., the underlined numbers in the third row of Figure 13(b). The output vectors of the AR and MA network have the largest values in the fifth and fourth elements, respectively, and have the second largest value in the third and second elements, respectively. Therefore, the appropriate model for CPI data is ARMA(4, 3). However, ARMA(2, 1) can be considered as an alternative model to ARMA(4, 3) as discussed in [19].

## CASE III: Caffeine Data

Figure 14 shows the case in which seasonality is involved in the time series. The data consists of 178 observations of caffeine levels in instant coffee taken every weekday, which is known to follow the ARMA(2, 5) model [5,24]. The ESACF pattern has a $41\%$ noise level and does not show any obvious triangular shape. However, NFN reduces the noise, although it leaves the other type of spurious values as depicted in Figure 14(b) - namely, the underlined numbers in diagonal lines. According to the output vectors, the noise-filtered pattern indicates that the orders of AR and MA are 2 and 5, respectively. Thus, the two-stage approach correctly classifies caffeine data into ARMA(2, 5).

## 7. Concluding remarks

We have shown that the neural networks can identify ARMA model with about 90% of accuracy using ESACF inputs. To accommodate the noisy environment, Noise Filtering Network is adopted which improved the performance significantly. To reduce the training effort without losing the performance, we have also devised a Reduced Model for Pattern Classification Network.

Follow-on question is the comparative performance of neural network for forecasting itself as mentioned in the introduction. For this issue, readers may refer to [10].

## Acknowledgement

We would like to thank Kar Yan Tam, two anonymous reviewers, and Peter Silhan for their helpful comments on this paper and suggestions for our ongoing researches.

## References

[1] H. Akaike, A New Look at the Statistical Model Identification, IEEE Transactions on Automatic Control AC-19, (1974) 716–723.

[2] G.E.P. Box and G.M. Jenkins, Time Series Analysis - Forecasting and Control (Holden-Day Inc., San Francisco, 1976).

[3] R.P. Gorman and T.J. Sejnowski, Analysis of Hidden Units in a Layered Network Trained to Classify Sonar Targets, Neural Networks 1, Nr. 1 (1988) 75–89.

[4] M. Gutierrez, J. Wang and R. Grondin, Estimating Hidden Unit Number for Two-layer Perceptron, Proceedings of IEEE 3rd International Conference on Neural Networks, (1989) I677–I681.

[5] D.C. Hamilton and D.G. Watts, Interpreting Partial Autocorrelation Functions of Seasonal Time Series Models, Biometrika, 65, (1978) 135–140.

[6] J.J. Hopfield, Neural Network and Physical Systems with Emergent Collective Computational Abilities, Proceedings of National Academy Science, USA, 79, (1982) 2554–2558.

[7] G.W. Hill and D. Woodworth, Automatic Box-Jenkins Forecasting, Journal of Operational Research Society, 31, (1980) 413–422.

[8] R.A. Jacobs, Increased Rates of Convergence through Learning Rate Adaptation, Neural Networks, 1, (1988) 285–307.

[9] W.C. Jhee, J.K. Lee and K.C. Lee, A Neural Network Approach for the Identification of Box-Jenkins Model, Forthcoming in Network: Computation in Neural Systems (1992).

[10] W.C. Jhee and J.K. Lee, Performance of Neural Networks in Managerial Forecasting, International Journal of Intelligent Systems in Accounting, Finance and Management, 2.1, (1992) 55–72.

[11] D.C. Montgomery and L.A. Johnson, Forecasting and Time Series Analysis (McGraw-Hill, New York, 1976).

[12] C.A. Kang, D. Bedworth and D. Rollier, Automatic Identification of ARIMA Time Series, IIE Transactions, 14, (1982) 156–166.

[13] S.Y. Kung and J.N. Hwang, An Algebraic Projection Analysis for Optimal Hidden Units Size and Learning Rates in Back-Propagation Learning, IEEE 2nd International Conference on Neural Networks, (1988) I363–I370.

[14] A. Lapedes and R. Farber, Nonlinear Signal Processing Using Neural Networks: Prediction and System Modeling, Los Almos National Laboratory Report LA-UR-87-2662 (1987).

[15] R.P. Lippmann, An Introduction to Computing with Neural Nets, IEEE ASSP Magazine, 4, (1987) 4–22.

[16] R.J. McEliece, E.C. Posner, E.R. Rodemich and S.S. Venkatesh, The Capacity of the Hopfield Associative Memory, IEEE Transactions of Information Theory 33, Nr. 4 (1987) 461–482.

[17] C.R. Nelson, Applied Time Series Analysis for Managerial Forecasting (Holden-Day Inc., San Francisco, 1973).

[18] M.J. Norusis, SPSS/PC+ for the IBM PC/XT/AT (SPSS Inc., 1986).

[19] S.M. Pandit and S.M. Wu, Time Series and System Analysis with Applications (John Wiley and Sons, New York, 1983).

[20] Y.H. Pao, Adaptive Pattern Recognition and Neural Networks (Addison-Wesley, MA., 1988).

[21] D.E. Rumelhart, G.E. Hinton and R.J. Williams, Learning Internal Representations by Error Propagation, in: D.E. Rumelhart and J.L. McClelland, Eds., Parallel Dis

tributed Processing: Explorations in the Microstructure of Cognition. Vol. I: Foundations (MIT Press, 1986).

[22] G. Schwarz, Estimating the Dimension of a Model, The Annals of Statistics 6, Nr. 2 (1978) 461–464.

[23] T.J. Sejnowski and P.K. Kienker, Learning Symmetry Groups with Hidden Units: Beyond the Perceptron, Physica, 22D, (1986) 260–275.

[24] R.S. Tsay and G.C. Tiao, Consistent Estimates of Autoregressive Parameters and Extended Sample Autocorrelation Function for Stationary and Nonstationary ARMA Models, Journal of American Statistical Association, 79, (1984) 84–96.

[25] A. Waibel, T. Hanazawa, G. Hinton, K. Shikano and K. Lang, Phoneme Recognition Using Time-Delay Neural Networks, IEEE Transactions on ASSP 37, Nr. 3 (1989) 328–339.

[26] PJ. Werbos, Generalization of Backpropagation with Application to a Recurrent Gas Market Model. Neural Networks 1, Nr. 4, (1988) 339–356.

[27] S.C. Wheelwright and S. Makridakis, Forecasting Methods for Management, (John Wiley & Sons, New York, 1985).

[28] H. White, Economic Prediction Using Neural Networks: The Case of IBM Daily Stock Returns, IEEE 2nd International Joint Conference on Neural Networks, (1988) II451–II458.

[29] W.A. Woodward and H.L. Gray, On the Relationship between S-Array and the Box-Jenkins Method of ARMA Model Identification, Journal of American Statistical Association 76, (1981) 579–587.
