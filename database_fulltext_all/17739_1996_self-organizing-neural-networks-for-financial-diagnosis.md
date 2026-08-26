---
otero_id: 17739
otero_key: "QWT4WXCY"
title: "Self organizing neural networks for financial diagnosis"
authors: "Carlos Serrano-Cinca"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00033-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Self organizing neural networks for financial diagnosis

Carlos Serrano-Cinca \*

Departamento de Contabilidad y Finanzas, Facultad de Ciencias Económicas y Empresariales, Universidad de Zaragoza, Zaragoza, Spain

## Abstract

A complete Decision Support System (DSS) for financial diagnosis based on Self Organizing Feature Maps (SOFM) is described. This is a neural network model which, on the basis of the information contained in a multidimensional space — in the case exposed, financial ratios — generates a space of lesser dimensions. In this way, similar input patterns — in the case exposed, companies — are represented close to one another on a map. The neural network has been complemented and compared with multivariate statistical models such as Linear Discriminant Analysis (LDA), as well as with neural models such as the Multilayer Perceptron (MLP). As the principal advantage, this DSS provides a complete analysis which goes beyond that of the traditional models based on the construction of a solvency indicator also known as Z score, without renouncing simplicity for the final decision maker.

Keywords: Self organizing feature maps; Neural networks; Kohonen maps; Financial diagnosis; Bankruptcy prediction

## 1. Introduction

Financial analysis has developed a large number of techniques aimed at helping decision makers such as potential investors and financial analysts. The multivariate statistical models represent a great advance when compared to those which study each variable separately. However, traditional statistical models, despite their undoubted usefulness, are not free of problems which make their application difficult in the firm. Amongst these problems we find the difficulty of working with complex statistical models, the restrictive hypotheses that need to be satisfied and the difficulty of drawing conclusions by non-specialists in the matter.

To overcome these problems, the tools provided by Artificial Intelligence have shown themselves to be most appropriate for business management, given that the philosophy from which they spring is different, namely to help in the taking of decisions by simplifying the task of the final user, in such a way that comprehensive technological knowledge is not required from the decision maker. Expert Systems, the most well known branch of Artificial Intelligence, has emerged with this same aim in mind. Having said that, after thirty years of study, these systems are not bearing the fruit expected of them in areas such as the evaluation of the solvency of an entity. Their high cost, the difficulty in obtaining the knowledge of a specialist, as well as in managing incomplete or incorrect information, and their limited flexibility in the face of change, are given as the causes of their limited application. Artificial Neural Networks, a newer paradigm for Artificial Intelligence, are multivariate mathematical models that can be easily integrated in a DSS, and could offer very interesting advantages for immediate application in the financial diagnosis of the firms.

The Multilayer Perceptron (MLP) with Back Propagation training is the most popular neural model and has already been used in a variety of disciplines, including Accounting, Finance and Banking $[2,14–18]$ . The Multilayer Perceptron belongs to the supervised neural networks, that is to say, it is necessary to provide the model with some input variables and the desired output. Thus it is comparable to Linear Discriminant Analysis (LDA) or Logit Analysis. These models, neural or statistical, provide a solvency indicator, also known as Z score, which can be used to infer the probability of bankruptcy of a firm. However, this indicator is not always sufficient in the decision making process. Recently, Mar-Molinero and Ezzamel $[12]$ and Mar-Molinero and Serrano-Cinca $[13]$ have proposed the use of another multivariate statistical technique, namely Multidimensional Scaling (MDS) as a complement to the traditional statistical models based on Z analysis. MDS visually classifies bankrupt and solvent firms, so that the decision making process is enriched and more intuitive.

In this paper we take as starting point the work of Serrano-Cinca and Martín-del-Brío [10,11,16] who propose Self Organizing Feature Maps (SOFM) as a tool for financial analysis. An SOFM is an unsupervised neural model; it is only necessary to provide it with input data and it then makes a grouping of the same. It is related, therefore, to statistical models such as Principal Component Analysis (PCA), Multidimensional Scaling (MDS) or Hierarchical Cluster Analysis (HCA). The paper is organised in the following way. Section 2 is devoted to a description of SOFM. In Section 3 we describe the use of SOFM in this context, applying it to a study of bankruptcy. In Section 4 we integrate SOFM into a DSS designed to help in the taking of decisions with LDA and MLP. The conclusions are set out in Section 5.

## 2. Self organizing feature maps

In this Section we describe the SOFM. This neural system was developed in its present form by Kohonen [7,8] and thus they are also known as

Kohonen Maps. It has demonstrated its efficiency in real domains, including clustering, the recognition of patterns, the reduction of dimensions and the extraction of features. Any personal computer with a link to Internet can access the server cochlea.hut.fi (130.233.168.48) which is resident in Finland. This file contains software and over one thousand bibliographical references on published papers on the subject of SOFM.

The SOFM model is made up of two neural layers. The input layer has as many neurons as it has variables, and its function is merely to capture the information. Let m be the number of neurons in the input layer; and let $n_{x} * n_{y}$ the number of neurons in the output layer which are arranged in a rectangular pattern with x rows and y columns, which is called “the map”. Each neuron in the input layer is connected to each neuron in the output layer. Thus, each neuron in the output layer has m connections to the input layer. Each one of these connections has a synaptic weight associated with it. Let $w_{ij}$ the weight associated with the connection between input neuron i and output neuron j. Fig. 1 gives a visual representation of this neural arrangement.

SOFM tries to project the multidimensional input space, which in our case could be financial information, into the output space in such a way that the input patterns whose variables present similar values appear close to one another on the map which is created. Each neuron learns to recognise a specific type of input pattern. Neurons which are close on the map will recognise similar input patterns whose images therefore, will appear close to one another on the created map. In this way, the essential topology of the input space is preserved in the output space. In order to achieve this, SOFM uses a competitive algorithm known as “winner takes all”.

Initially, the $w_{ij}$ 's are given random values. These values will be corrected as the algorithm progresses (training). Training proceeds by presenting the input layer with financial ratios, one firm at a time. Let $r_{ik}$ be the value of ratio i for firm k. This ratio will be read by neuron i. The algorithm takes each neuron in the output layer at a time and computes the Euclidean distance as a similarity measure,

$$
d (j, k) = \sqrt {\sum_ {i} \left(r _ {i k} - w _ {i j k}\right) ^ {2}}.
$$

![](/api/attachments/QWT4WXCY/fulltext/images/54a0228a57f7358864331cdc55ee4a73ce9c05c12e90993977ef7c6a57e2ed37.jpg)  
Fig. 1. Self organizing neural network with m neurons in the input layer and $n_{x} * n_{y}$ neurons in the output layer. Each neuron in the output layer has m connexics $w_{ij}$ (synaptic weights) to the input layer.

The output neuron for which $d(j, k)$ is smallest is the “winner neuron”. Let such neuron be $k^{*}$ . The algorithm now proceeds to change the synaptic weights $w_{ij}$ in such a way that the distance $d(j, k^{*})$ is reduced. A correction takes place, which depends on the number of iterations already performed and on the absolute value of the difference between $r_{ik}$ and $w_{ijk}$ . But other synaptic weights are also adjusted in function to how near they are to the winning neuron $k^{*}$ and the number of iterations that have already taken place.

The procedure is repeated until complete training stops. Once the training is completed, the weights are fixed and the network is ready to be used. From now on, when a new pattern is presented, each neuron computes in parallel the distance between the input vector and the weight vector that it stores, and a competition starts that is won by the neuron whose weights are more similar to the input vector. Alternatively, we can consider the activity of the neurons on the map (inverse to the distance) as the output. The region where the maximum activity takes place indicates the class that the present input vector belongs to. If a new pattern is presented to the input layer and no neuron is stimulated by its presence the activity will be minimal, and this means that the pattern is not recognized. In this case, the possibility of re-training a map with new data without requiring starting from scratch has to be contemplated. This is a procedure suggested by Kohonen [7] and adapted by Martín-del-Brío and Serrano-Cinca [10] who give full details.

## 3. Proposed method of work with SOFM for the analysis of company failure

Fig. 2 describes the habitual working procedure followed with the Self Organizing Feature Maps neural model. The type of task which we can carry out is varied: bond rating, credit scoring, failure prediction, etc. On this occasion our aim is to develop a model to detect corporate failure. The data base used in our paper is found in the work of Rahimian et al. [15]. This practical case has been chosen because there are a number of previous empirical studies with which to compare our results, namely Odom and Sharda [14], and Wilson and Sharda [18] using LDA and another neural model,

![](/api/attachments/QWT4WXCY/fulltext/images/bc6fef4bfd77c407d5ffec481083f25ca00c85ce529dd19c11d72f83f45a438d.jpg)  
Fig. 2. Proposed method of work with self organizing maps.

Table 1  
Financial ratios employed, Wilks' lambda and univariate $F$ -ratio with 1 and 72 degrees of freedom. Ratio number 5 has low capacity to discriminate between solvent and bankrupt firms

<table><tr><td>Financial ratio</td><td>Wilks&#x27; lambda</td><td>F-ratio</td><td>Significance</td></tr><tr><td> $R_1$  working capital/total assets</td><td>0.82</td><td>15.57</td><td>0.0002</td></tr><tr><td> $R_2$  retained earnings/total assets</td><td>0.59</td><td>50.09</td><td>0.0000</td></tr><tr><td> $R_3$  earnings before interest and tax/total assets</td><td>0.57</td><td>54.44</td><td>0.0000</td></tr><tr><td> $R_4$  market value of equity/total debt</td><td>0.92</td><td>6.16</td><td>0.0154</td></tr><tr><td> $R_5$  sales/total assets</td><td>0.98</td><td>1.46</td><td>0.2314</td></tr></table>

![](/api/attachments/QWT4WXCY/fulltext/images/7c59f0a6b230b08f4b842ace33aa0c16d017df8005a48d506232e10efc9b3f2c.jpg)  
○ Bankrupt Companies
□ Solvent Companies

![](/api/attachments/QWT4WXCY/fulltext/images/dd66a0b44c1ef3d6b82d55ea151d8cc2b3694345ead42e3fa9278d8d0b1c5863.jpg)

![](/api/attachments/QWT4WXCY/fulltext/images/41e7830c2570186f6aae9c8e8a7cda6ad31e95764ff4d013c81d3fc432a0fe5b.jpg)  
Fig. 3. (a) MAP I. Location of firms on the solvency map, made up of $12 \times 12$ training neurons. 1 to 36 are solvent firms; 37 to 74 (round neurons) contain information for one year prior to the incidence of bankruptcy. (b) MAP II. Showing, for each neuron, which firm gives the strongest response. We can see two main areas, one consisting of neurons that have tuned to the bankrupt companies, and the other of neurons that have tuned to the solvent ones.

MLP, and Rahimian et al. [15] who propose a series of improvements to the MLP and also analyse another neural model, the Athena.

The data base contains five financial ratios taken from Moody's Industrial Manual from 1975 through to 1985 for a total of 129 firms, of which 65 are bankrupt and the rest are solvent. In the work carried out in Refs. [14,15,18] the sample was randomly divided into two groups, the first made up of 74 firms, used for training and the second of 55, used for testing the models. We have proceeded in the same way in this study. Table 1 contains the ratios employed, which coincide with those selected by

Altman [1]. It is necessary to carry out, a priori, a statistical analysis of the variables, discarding those that do not possess discriminatory power. For this purpose we have used a discriminant analysis, discarding non-significant variables by means of a univariate F-ratio analysis, which is summarised in Table 1. The discriminatory power of each one of the ratios can be clearly seen. Thus, ratio number 5 has low capacity to discriminate between solvent and bankrupt firms, and so it was decided not to include it in the model. Ratios 2 and 3 present the greater discriminatory power.

The next stage was to develop a neural architecture in accordance with those ratios. The number of neurons and the chosen similarity measure depend on how the information is presented. A neural network with 4 neurons in the input layer was chosen, that is to say, the same number as the number of ratios we have available to us, and 144 neurons in the output layer arranged in a 12\*12 square grid in order to adequately accommodate the 74 patterns in our data base. Given the non-supervised character of the algorithm employed, it is not necessary to indicate whether the firm is solvent or not. The input variables have been standardized to mean zero and variance 1. If there is little to choose between two particular firms on the basis of their financial structure, any measure of similarity that may be calculated will take a small value, and if two firms have diverse financial structures, any measure of similarity will take a large value. Although it is possible to think of many ways of comparing individual firms, the easiest way to do it is to calculate the Euclidean distance between firms using standardised ratios as variables. The advantage of proceeding in this way is that the parallelism with Principal Component Analysis (PCA) and Multidimensional Scaling (MDS) is maintained [3].

![](/api/attachments/QWT4WXCY/fulltext/images/06bbf7903f8767b0b68f5cbce7c767f4892d149b80a588f607f676d58b6806d3.jpg)  
Fig. 4. (a) Weight maps III $_{1,2,3,4}$ . Every weight map is dedicated to one input variable; the weights that connect every input variable (R $_{1}$ to R $_{4}$ ) with all the neurons of the square output layer (12 × 12 neurons) are represented on every map, their magnitude being coded in grey levels. (b) Map IV. Showing, for each neuron, which financial ratio provokes the greatest response, in absolute values. Map V. Regions obtained on the Solvency Map. From the study of the synaptic weights maps of the 4 ratios (Maps III and IV) we can determine which variable dominate over one or other zone of the map.

Once the variables and the input patterns have been selected, we are in a position to start training. After a time, which will depend upon the specific computer system used, we obtain the first results. Fig. 3a shows where each pattern is situated on Map I at the end of the training phase. This map serves to obtain a first approximation of the different regions which appear. Two large zones can be noted, one corresponding to the solvent firms (1 to 36) and the other made up of the bankrupt firms (37 to 74). These neurons have been rounded to delimitate the bankrupt zone. Empty spaces appear on this first map because there are more neurons than patterns, so that the regions cannot be traced with complete precision. In response to this we have obtained Map II (Fig. 3b) which shows the patterns which most activate or stimulate each neuron. Here it is possible to delimitate with greater clarity those regions which have appeared on the map, because all the neurons are stimulated in the presence of the ratios of one or other firm. These maps are called Self-Organizing Solvency Maps, and were discussed earlier in Refs. [10,16].

The vision provided by these maps is not sufficient, in that we do not know how the grouping has been carried out, which variables have been the most relevant in the decision taking process, etc. It is often the case that neural models are accused of acting like a black-box, in the sense that it is difficult to know how the results have been obtained. A study of the synaptic weights will help us to determine which variables dominate over one or other zone of the map. The synaptic weights maps indicate, for each ratio, the weights which connect the neuron of the input layer associated to it with all the neurons of the map. Fig. 4a shows the synaptic weights. We have codified their magnitude in different shades of grey. In this way it is easy to observe the relationships which exist between the input variables, thus allowing us to distinguish regions on the map.

If we compare the maps of Fig. 4 with Fig. 3, that is to say, with the map which delimitates the bankrupt and solvent firms, we can see how the zone on the upper left hand side groups those firms with high $R_{1}$ , $R_{2}$ and $R_{3}$ . The upper right hand zone of the map corresponds to high earnings ratios ( $R_{2}$ and $R_{3}$ ). The lower right hand zone of the map are firms with high $R_{4}$ , whilst the lower left hand zone corresponds to low values of the 4 ratios. Ratios 2 and 3 contribute with greatest clarity to the delimitation of the bankrupt region. As was expected, almost all the firms that are found in the bankrupt zone show patterns that are characterised by low earnings, whilst these are high for solvent ones. From the study of the synaptic weights we can surmise a series of regions on the maps: high earnings, low liquidity, etc.

We can delimit the regions with greater clarity by studying the absolute value of the synaptic weights of each neuron, obtaining information on the variables which dominate in each region of the map. Map IV, represented in Fig. 4b, indicates with respect to each neuron, which variable has become specialised in recognition, that is to say, which positive or negative feature has impressed it most. From a study of the Maps III and IV we can finally determine the regions which make up Map V, represented in Fig. 4c. Two large zones have been determined, one made up of neurons which synthesize when faced with high values of the ratios, and the other made up of neurons which specialise in recognising firms with deficient ratios. In both zones, which generally coincide with the zones of solvency and bankruptcy, subzones of high and low earnings, liquidity, etc., can be identified.

We know that, in the neural network, firms which are close to one another are firms which present similar patterns and that, by way of a study of the synaptic weights, we can obtain regions on the map. However, this might not be sufficient to clearly determine the frontiers between the firms. We can follow the method proposed by Martín-del-Brío and Medrano [9] for automatic extraction of clusters by means of SOFM. Imagine, for example, that we are interested in obtaining three clusters. Then, we treat the synaptics weights of the 144 neurons as patterns of another neural network with only three neurons on the output layer. In this way we force the selforganization of patterns into three groups. We can superimpose the results onto Map II (Solvency Map) or onto Map V (Regions), thus obtaining Map VI of Fig. 5, on which firms with similar financial characteristics appear in the same group. In this map we can see that the Group 1 corresponds to bankrupt companies and that solvent companies belong to Group 3. Group 2 is made up of bankrupt and solvent companies: this is a zone of indefinition with respect to which it would not be prudent to make judgements on the firms which are grouped therein.

## 4. Integration of SOFM with other models

The Neural System which we have described is, in itself, of great usefulness in the analysis of financial information produced by companies. The financial situation of a particular firm will determine its location on the map, but it must be taken into account that a firm can excite more than one neuron and can do so with different levels of intensity. Furthermore, this model allows us: to study the evolution in time of a firm by introducing information from various accounting periods; to situate the firm in relation to its competitors; to develop sectoral maps; to introduce additional ratios or items such as sales or assets figures, etc.

The Neural System can be integrated in a broader decision making context, using different tools provided by Artificial Intelligence and Statistics. We can combine SOFM with other mathematical models applied to the prediction of corporate failure. From amongst all these, without doubt the most popular is Linear Discriminant Analysis (LDA). The objective of LDA is to obtain a Z indicator which discriminates between two or more groups,

$$
Z = \sum \left(A _ {i} * X _ {i}\right),
$$

![](/api/attachments/QWT4WXCY/fulltext/images/ea484c5216a9af5c063e57290b716362f4cc29d0927475284107a90097f9d11f.jpg)

![](/api/attachments/QWT4WXCY/fulltext/images/d56366a25d4e7add5367bc2e34b334d261cd66ceeab5f28ac8fca0f3d3e236e6.jpg)  
Fig. 5. MAP VI. Superimposition of the three clusters onto Map III. The trace of the strongest line divides the plane into solvent and bankrupt firms.

where $X_{i}$ are the variables, in our case financial ratios and $A_{i}$ are the parameters which it obtains.

LDA makes extensive demands on the structure of the data. It starts from the premise that two different populations coexist in the data set, one of failed and one of continuing firms. Both populations are described by multivariate normal distributions with the same variance-covariance matrices, although their means are presumed to be different. This assumption is not totally necessary, it is only required for computational convenience since it results on linear classification rules that are easy to apply in practice. The assumption of common covariance structures can be relaxed, but there is a severe price to pay: models become much more difficult to estimate and implement. For a discussion of the issues involved see Ref. [4].

An LDA has been carried out on the data used in this work. Thereafter we have obtained, for each firm, the Z score and we have then superimposed this indicator onto the selforganizing map. This has allowed us to obtain some regions made up by firms whose solvency is similar according to the said multivariate analysis. These regions have been given the name isosolvency regions; they are four in number and can be seen in Fig. 6a. Note that the two isosolvency regions higher than 7 belong to the solvency zone and, similarly, how the isosolvency

![](/api/attachments/QWT4WXCY/fulltext/images/cf35b7f4def7814448e4c13004374c65d6b041db091595624f2e8b7e38eeb996.jpg)  
Fig. 6. Isosolvent regions. (a) Superimposition of the results of Linear Discriminant Analysis (LDA) on Map III. (b) Superimposition of the results of Multilayer Perceptron (MLP) on Map III.

Table 2

region lower than 2 is included in the bankruptcy zone. Finally, the central zone groups firms with Z score between 2 and 5.

Another neural model, the Multilayer Perceptron (MLP), can also be used to obtain the isosolvent regions. This model has the common objective with LDA of obtaining a Z indicator which can be used as a measure of the solvency of the companies and is also capable of separating non-linear patterns. Gallinari et al. [5] demonstrate how in reality LDA is a particular case of the single layer perceptron. What is more, MLP is a universal approximator of functions, as is demonstrated in Ref. [6]. In fact, an MLP with one hidden layer is essentially the same as the projection pursuit regression. We used an MLP to complete the information on the isosolvency regions. An MLP was trained with a hidden layer with 3 neurons and a sigmoid transfer function, providing an output between 0 and 1, which is interpreted as a measure of solvency. By virtue of its greater discriminatory power and the use of a sigmoid function in the last neuron, MLP obtains results which are in general close to 0 or 1. It only hesitates in the case of firms 11, 14, 20, 24, 30, 35, 42, 49, 55, 64, 66, 68, 71, 72 and 73 and these, which according to MLP do not clearly belong to one group or another, are marked in Fig. 6b. This allows us to obtain another zone of indefinition in the map.

With this DSS, and despite the complexity resulting from the combination of different tools, it is very easy for a final user to evaluate the solvency of an entity by introducing no more than the values of its ratios. The model shows us, first, whether the firm is in the solvency or bankruptcy zone and, by studying the map of the regions, which financial features stand out. Furthermore, it shows us to which cluster the firm belongs and which firms present similar ratios. Finally, it shows whether the firm belongs to one or other of the isosolvency regions, according to LDA, and if it is a zone of indefinition, according to MLP.

A test was carried out with the financial ratios of the 55 firms of the test data set. Table 2 shows the results obtained with the test by way of LDA, the single layer perceptron, the MLP used by [14] and the MLP and the Athena neural model used by [15], as well as the score obtained by our own MLP. The LDA obtained 41 out of 55 correct classifications, whilst the other models obtained 45 out of 55, an accuracy of 81.8%.

The table shows the score obtained by the multilayer perceptron (MLP) and the results obtained with the test by way of six different models

<table><tr><td>No.</td><td>MLP</td><td>Other studies</td><td>No</td><td>MLP</td><td>Other studies</td></tr><tr><td>1</td><td>0.99</td><td></td><td>29</td><td>0.03</td><td></td></tr><tr><td>2</td><td>0.96</td><td></td><td>30</td><td>0.03</td><td></td></tr><tr><td>3</td><td>0.99</td><td></td><td>31</td><td>0.12</td><td></td></tr><tr><td>4</td><td>0.99</td><td></td><td>32</td><td>0.06</td><td></td></tr><tr><td>5</td><td>1.00</td><td></td><td>33</td><td>0.00</td><td></td></tr><tr><td>6</td><td>1.00</td><td></td><td>34</td><td>0.05</td><td></td></tr><tr><td>7</td><td>0.99</td><td></td><td>35</td><td>0.33</td><td>* %</td></tr><tr><td>8</td><td>0.87</td><td></td><td>36</td><td>0.36</td><td>* %</td></tr><tr><td>9</td><td>1.00</td><td></td><td>37</td><td>0.00</td><td></td></tr><tr><td>10</td><td>1.00</td><td></td><td>38</td><td>0.16</td><td></td></tr><tr><td>11</td><td>0.98</td><td></td><td>39</td><td>0.71</td><td>* #%&amp;@$</td></tr><tr><td>12</td><td>1.00</td><td>#@</td><td>40</td><td>0.20</td><td>* #%&amp;@</td></tr><tr><td>13</td><td>0.59</td><td></td><td>41</td><td>0.00</td><td></td></tr><tr><td>14</td><td>0.97</td><td></td><td>42</td><td>0.00</td><td></td></tr><tr><td>15</td><td>0.96</td><td></td><td>43</td><td>0.09</td><td></td></tr><tr><td>16</td><td>0.90</td><td></td><td>44</td><td>0.00</td><td></td></tr><tr><td>17</td><td>0.02</td><td>* #%&amp;@$</td><td>45</td><td>0.00</td><td></td></tr><tr><td>18</td><td>0.02</td><td>* #%&amp;@$</td><td>46</td><td>0.58</td><td>* #%&amp;@$</td></tr><tr><td>19</td><td>0.99</td><td></td><td>47</td><td>0.49</td><td>*</td></tr><tr><td>20</td><td>0.72</td><td></td><td>48</td><td>0.00</td><td></td></tr><tr><td>21</td><td>0.42</td><td>#%&amp;$</td><td>49</td><td>0.79</td><td>* #%&amp;@$</td></tr><tr><td>22</td><td>1.00</td><td></td><td>50</td><td>0.78</td><td>* # &amp;@$</td></tr><tr><td>23</td><td>0.96</td><td></td><td>51</td><td>0.48</td><td>*</td></tr><tr><td>24</td><td>0.87</td><td></td><td>52</td><td>0.01</td><td></td></tr><tr><td>25</td><td>0.03</td><td>* #%&amp;@$</td><td>53</td><td>0.08</td><td></td></tr><tr><td>26</td><td>1.00</td><td></td><td>54</td><td>0.92</td><td>* #%&amp;@$</td></tr><tr><td>27</td><td>0.98</td><td></td><td>55</td><td>0.40</td><td>*</td></tr><tr><td>28</td><td>0.58</td><td></td><td></td><td></td><td></td></tr></table>

\* Misclassified by Linear Discriminant Analysis (LDA)  
# Misclassified by Odom and Sharda Multilayer Perceptron (MLP)  
% Misclassified by Rahimian et al. MLP  
& Misclassified by Perceptron Model  
@ Misclassified by Athena Model  
\$ Misclassified by our MLP

The Self Organizing Neural Network approach is demonstrated by analysing the first firm in the test data set. The ratios for this firm had not been used to train the network, thus no neuron in the output layer is expected to exactly represent it. However, those output neurons associated with firms that are very similar to the test firm, will be strongly stimulated, and those that are associated with dissimilar firms will have low stimulation. We introduced the ratios

![](/api/attachments/QWT4WXCY/fulltext/images/6adccf685bc02831b2c209b989a41d4c5396409fa59e4d1f52a479b8e6f54bf1.jpg)  
Fig. 7. Test firm number 1. The intensity with which the neurons are stimulated is indicated in different shades of grey. The figure shows a typical screen of the computer software developed.

for this firm onto the SOFM and we obtained the map which appears as Fig. 7. The information which the DSS supplies is quite full and the neurons which are stimulated by its presence are various. The intensity with which they are stimulated is indicated in different shades of grey. Note that nearly all of them are neurons that are specialized in recognising solvent firms. To be exact, the winner neuron is in the solvency zone which, from a study of the synaptic weights, is the zone with a very high ratio number 2 and quite high ratios 1 and 3. With respect to the cluster analysis, the winner neuron is found in the group III which includes the solvent firms. Furthermore, the three or four neurons which are in greatest syntony with pattern number 1 are in the zone of isosolvency close to 10. On the basis of all this, we can conclude that it is a solvent firm.

It is difficult to speak of Type I and Type II errors given that, in order to consider a firm as potentially solvent or bankrupt, we must take various criteria into account, namely the zone of the map, isosolvency regions, the cluster to which it belongs, etc.

![](/api/attachments/QWT4WXCY/fulltext/images/4797bcdbd45cc5d819319d6639a6f8fd4a7e4ecbe6e5444de3a7a6435bcd06d4.jpg)  
Fig. 8. Winner neuron of all of the firms which make up the test.

and, for reasons of space, the maps provided by the 55 firms have not been reproduced; what is shown, in Fig. 8, is the winner neuron for each one of them. The majority of the firms are correctly classified in a percentage similar to that obtained by earlier quoted works. In general, those firms which are badly classified by discriminant analysis and supervised neural models appear in the indefinition zone of the map. Thus, firms 17, 35, 36, 39, 47, 51 and 55 are found in the doubtful isosolvency region. The analyst may have the last word in. for example, the granting of loans to these firms. The true mistakes are firms 18, 25 and 54. The error should not be imputed to the model, but rather to the information supplied; there are firms with similar ratios but that have had a very different fate, in that some went bankrupt but others did not. On the map, the firms with similar ratios are neighbours, but one of them can lie out of its correct zone. Therefore, the emphasis should be placed on the selection of the variables, which do not necessarily have to take the form of accounting information.

## 5. Conclusions

This paper has discussed the application of a neural model, namely the Self Organizing Feature Maps, to the analysis of financial information. This model makes a projection of a multidimensional input space over a plane, preserving its topological characteristics, in such a way that points which are close to one another on the plane correspond to similar input patterns. The use of neural models must be complemented with a statistical study of the available information. On this basis, we have developed a complete DSS for the analysis of accounting statements, which includes Linear Discriminant Analysis (LDA) and Multilayer Perceptron (MLP) to delimit the isosolvency regions. The model allows for the cross sectional analysis of ratios or other financial variables, as well as time series analysis.

The proposed DSS goes beyond traditional Z analysis and provides a graphic intuitive vision which supplies information on the risk of bankruptcy, the financial characteristics of the firm and the type of firm it resembles. The flexibility of the neural model to combine with and to adapt to other structures, whether neural or otherwise, augurs a bright future for this type of model. Its combination with other neural tools, Expert Systems or statistics, leads us to believe that in the near future it can play an important role in the decision making process.

## Acknowledgements

The helpful comments received from Cecilio Mar-Molinero, of the University of Southampton, are gratefully acknowledged.

## References

[1] E.I. Altman, Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy, Journal of Finance, September (1968) 589–609.

[2] T.B. Bell, G.S. Ribar and J.R. Verchio, Neural Nets versus Logistic Regression: A comparison of Each Model's Ability to Predict Commercial Bank Failures, Proceedings of the 1990 Deloitte and Touche/University of Kansas Symposium on Auditing Problems (1990) 29–53.

[3] C. Chatfield and A.J. Collins, Introduction to Multivariate Analysis (Chapman and Hall, London, 1980).

[4] R.A. Eisenbeis, Pitfalls in the Application of Discriminant Analysis in Business, Finance, and Economics, The Journal of Finance 32 (1977) 875–900.

[5] P. Gallinari, S. Thiria, F. Badran and F. Fogelman-Soulie, On the Relations Between Discriminant Analysis and Multilayer Perceptrons, Neural Networks 4 (1991) 349–360.

[6] K. Hornik; M. Stinchcombe and H. White, Multilayer Feedforward Networks are Universal Aproximators, Neural Networks 2 (1989) 359–366.

[7] T. Kohonen, Self Organization and Associative Memory. 3rd ed. (Springer-Verlag, Berlin, 1989).

[8] T. Kohonen, The Self Organizing Map, Proceedings of the IEEE 78, No. 9 (1990) 1464–1480.

[9] B. Martín-del-Brío and N. Medrano, Feature Map Architectures for Pattern Recognition: Techniques for Automatic Region Selection, in: D. W. Pearson, N.C. Steele and R.F. Albrecht, Eds., Artificial Neural Nets and Genetic Algorithms (Springer-Verlag, Berlin, 1995) 124–127.

[10] B. Martín-del-Brío and C. Serrano-Cinca, Self-Organizing Neural Networks for the Analysis and Representación of Data: Some Financial Cases, Neural Computing and Applications 1 (Springer-Verlag, Berlin, 1993) 193–206.

[11] B. Martín-del-Brio and C. Serrano-Cinca, Self-Organizing Neural Networks: The Financial State of Spanish Companies, in: N.A.D. Refenes, Eds., Neural Networks in the Capital Markets (Wiley, London, 1995) Ch. XXIII.

[12] C. Mar-Molinero and M. Ezzamel, Multidimensional Scaling Applied to Corporate Failure, OMEGA, International Journal of Management Science 19, No. 4 (1990) 259–274.

[13] C. Mar-Molinero and C. Serrano-Cinca, Bank Failure: A Multidimensional Scaling Approach, 17th Congress of European Accounting Association, Venezia, Italy (1994).

[14] M. Odom and R. Sharda, A Neural Network Model for Bankruptcy Prediction, in: R.R. Trippi and E. Turban, Eds., Neural Networks in Finance and Investing (Probus Publishing Company, Chicago, 1993).

[15] E. Rahimian, S. Singh, T. Thammachacote and R. Virmani, Bankruptcy Prediction by Neural Networks, in: R.R. Trippi and E. Turban, Eds., Neural Networks in Finance and Investing (Probus Publishing Company, Chicago, 1993).

[16] C. Serrano-Cinca and B. Martín-del-Brío, Predicción de la Crisis Bancaria Mediante el Empleo de Redes Neuronales Artificiales, Revista Española de Financiación y Contabilidad XXII, No. 74 (1993) 153–176.

[17] K.Y. Tam and M.L. Kiang, Managerial Applications of Neural Networks: The Case of Bank Failure Predictions, in: R.R. Trippi and E. Turban, Eds., Neural Networks in Finance and Investing (Probus Publishing Company, Chicago, 1993).

[18] R.L. Wilson and R. Sharda, Bankruptcy Prediction using Neural Networks, Decision Support Systems 11, No. 5 (1994).

![](/api/attachments/QWT4WXCY/fulltext/images/693d8ae20f51391897e0ccd8bff909bbe4c25168e529146ba1c65f53f3a1e6e0.jpg)

Carlos Serrano-Cinca received his Ph.D. in Economics and Business Administration from the University of Zaragoza (Spain) in 1994. He is Lecturer in Accounting and Finance in this University and he is currently Visiting Lecturer at the Department of Accounting and Management Science of the University of Southampton (UK). His research interests include neural networks and other multivariate mathematical models, Decision Support Systems,

and Information Technologies in Accounting and Finance. Dr Serrano-Cinca has published articles in journals and written chapters in books on Neural Networks such as Neural Computing & Applications and Neural Networks in the Capital Markets. He also publishes and serves as an ad hoc reviewer for academic journals in the field of Accounting and Finance.
