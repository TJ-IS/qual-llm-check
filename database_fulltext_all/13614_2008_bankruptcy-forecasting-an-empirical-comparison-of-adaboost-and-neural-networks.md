---
otero_id: 13614
otero_key: "8GMJXHXE"
title: "Bankruptcy forecasting: An empirical comparison of AdaBoost and neural networks"
authors: "Esteban Alfaro; Noelia García; Matías Gámez; David Elizondo"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bankruptcy forecasting: An empirical comparison of AdaBoost and neural networks ☆

Esteban Alfaro <sup>a,⁎</sup>, Noelia García <sup>a</sup>, Matías Gámez <sup>a</sup>, David Elizondo <sup>b</sup>

<sup>a</sup> Economic and Business Sciences Faculty of Albacete, Castilla-La Mancha University, Plaza de la Universidad, 1. 02071 Albacete, Spain <sup>b</sup> School of Computing, De Montfort University, The Gateway, Leicester LE1 9BH, U.K.

Received 21 February 2007; received in revised form 22 November 2007; accepted 3 December 2007 Available online 8 December 2007

## Abstract

The goal of this study is to show an alternative method to corporate failure prediction. In the last decades Artificial Neural Networks have been widely used for this task. These models have the advantage of being able to detect non-linear relationships and show a good performance in presence of noisy information, as it usually happens, in corporate failure prediction problems. AdaBoost is a novel ensemble learning algorithm that constructs its base classifiers in sequence using different versions of the training data set. In this paper, we compare the prediction accuracy of both techniques on a set of European firms, considering the usual predicting variables such as financial ratios, as well as qualitative variables, such as firm size, activity and legal structure. We show that our approach decreases the generalization error by about thirty percent with respect to the error produced with a neural network.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Corporate Failure Prediction; Neural Network; AdaBoost

## 1. Introduction

Predicting corporate failure is a hot topic in management science due to its importance for making correct business decisions. The accuracy of the forecasting model is clearly of crucial importance in failure prediction because many economic agents not only enterprises but financial institutions, auditors, consultants, policy makers or clients are affected by the bankrupt of a firm. In classification terms, the type I error is especially important, i.e. when a firm which will fail in the future is classified as healthy. Owing to this fact many researchers have focused their effort on finding the most efficient classifier. In the last decades artificial neural networks have received special attention and several studies have dealt with failure forecasting using this technique. Here we present some of them only as examples. Wilson and Sharda [55] used a sample of 129 firms, 65 of which went bankrupt between 1975 and 1982 and 64 non bankrupt firms matched on industry and year. They applied resampling techniques to generate the training and test data sets and reached very satisfactory results with only five accounting ratios.

Serrano–Cinca [48] provided a data set made up of 66 Spanish banks, 29 of them in bankruptcy and the rest solvent. He used nine ratios chosen from amongst those most commonly employed in accounting empirical research. The author proved the superiority of the neural network model against linear discriminant analysis using the leaving one out estimation of the error. Charalambous et al [16] applied several neural networks methods to a dataset of 139 matched-pairs of bankrupt and non-bankrupt U.S. firms for the period 1983–1994. The authors compared the predictive performance of five methods, namely Learning Vector Quantization, Radial Basis Function, Feedforward networks that use the conjugate gradient optimization algorithm, the backpropagation algorithm and the logistic regression.

In this research, the neural network approach is compared to AdaBoosted [19] classification trees for predicting corporate failure. As far as we are aware, this is the first study to compare AdaBoost and Neural Networks capabilities for corporate failure prediction. To illustrate its usefulness, we will apply AdaBoost on a selection of Spanish companies, and in order to ensure that these results are general and can be projected to other European countries and to the United States, we will use financial ratios that have proved significant for predicting business failure in previous studies (e.g. Frydman [23]).

The lack of a unified theory on corporate failure has meant that most studies dealing with distress prediction have focused on increasing the accuracy of the model and have not always paid enough attention to the model interpretation. This is clearly important in failure prediction as the firm must make appropriate decisions. Ensemble methods like AdaBoost do not improve model interpretation by themselves. Even more, they break the model interpretation conveyed by a decision tree. But, on the other hand, attribute importance methods can be devised to provide useful information for problem understanding. We will also calculate a novel measure for the importance of variables to facilitate model interpretation. This measure takes into account how often variables are actually used in the individual trees and, on the basis of this measure, the variables can be ranked in terms of importance.

The following factors should be taken into account within the empirical application. We use the legal definition of corporate failure which only includes bankrupt and temporary receivership firms. This is the most common definition in corporate failure prediction literature. One numerical (the firm size) and two categorical variables (activity sector and legal structure) are included as descriptors in addition to the usual financial ratios. The AdaBoost method is applied to the failure prediction, analyzing the extent to which this methodology is suitable for the subject.

In Section 2 of this paper, we present the AdaBoost method included in the study with a discussion of how it works in practice and we describe the algorithm used. The following sections introduce the failure prediction problem and the data used in the analysis. The classification results are then presented and the wellknown neural network model is compared with the novel AdaBoost classifier. Finally, following on from the empirical analysis, we present our conclusions.

## 2. AdaBoost

A classifier system builds a model which is able to predict the class of a new observation given a data set. The accuracy of the classifier will depend on the quality of the method used and the difficulty of the specific application [24]. If the obtained classifier achieves a better accuracy than the default rule, then the classification method has found some structure in the data enabling it to do so. AdaBoost [19] is a method that makes maximum use of a classifier by improving its accuracy. The classifier method is therefore used as a subroutine to build an extremely accurate classifier based on the training set.

AdaBoost applies the classification system repeatedly to the training data, but at each application, the learning attention is focused on different examples of this set using adaptive weights $( \omega _ { b } ( i ) )$ , in contrast to other ensembles as Bagging [12] which do not update the weights. Once the training process has finished, the single classifiers obtained are combined into a final, highly accurate classifier based on the training set. The final classifier therefore usually achieves a high degree of accuracy in the test set as various authors have shown both theoretically and empirically [5,8,13,17,22].

Even though there are several versions of the AdaBoost algorithm [22], the most widely used is the one by Freund and Schapire [19] which is known as AdaBoost. For simplification purposes, it can be assumed, without loss of generality, that there are only two classes. A training set is given by $T _ { n } { = } \{ ( X _ { 1 } , Y _ { 1 } ) , ( X _ { 2 } , Y _ { 2 } ) , { \ldots } , ( X _ { n } , Y _ { n } ) \}$ where Y takes values of $\{ - 1 , \ 1 \}$ . The weight $\omega _ { b } ( i )$ is assigned to each observation $X _ { i }$ and is initially set to 1/n. This value will be updated after each step. A basic classifier denoted $C _ { b } ( X _ { i } )$ is built on this new training set,

$T ^ { b }$ , and is applied to each training sample. The error of this classifier is represented by $\varepsilon _ { b }$ and is calculated as

$$
\varepsilon_ {b} = \sum_ {i = 1} ^ {n} \omega_ {b} (i) \zeta_ {b} (i) \quad \text { where } \quad \zeta_ {b} (i) = \left\{ \begin{array}{l l} 0 & C _ {b} (x _ {i}) = y _ {i} \\ 1 & C _ {b} (x _ {i}) \neq y _ {i} \end{array} \right..\tag{1}
$$

The new weight for the (b + 1)-th iteration will be

$$
\omega_ {b + 1} (i) = \omega_ {b} (i) \cdot \exp (\alpha_ {b} \xi_ {b} (i)).\tag{2}
$$

where $\boldsymbol { \mathcal { a } _ { b } }$ is a constant calculated from the error of the classifier in the b-th iteration. More specifically, according to the authors mentioned above $\alpha _ { b } { = } \ln ( ( 1 - \varepsilon _ { b } ) / \varepsilon _ { b } )$

The calculated weights are then normalized so that they add up to one. Accordingly, $\varepsilon _ { b } { = } 0 . 5 - \gamma _ { b } ,$ where $\gamma _ { b }$ shows the advantage of the basic classifier of the b-th step over the default rule in the worst case, where both classes have the same a priori probability (0.5). Therefore, the weights of the wrongly classified observations are increased and the weights of the correctly classified ones are decreased, forcing the single classifier built in the following iteration to focus on the hardest examples. Furthermore, the differences when the weights are updated are greater when the error of the single classifier is small since more importance is given to the few mistakes mentioned when the classifier achieves a high level of accuracy. The alpha constant can therefore be interpreted as a learning rate which is calculated as a function of the error made on each epoch. This constant is also used in the final decision rule giving more importance to the individual classifiers that made a smaller error.

This process is repeated in every step for b = 1, 2, 3, …, B. Finally, the ensemble classifier is built as a linear combination of the single classifiers weighted by the corresponding constant $\alpha _ { b }$

$$
C (x) = \operatorname{sign} \left(\sum_ {b = 1} ^ {B} \alpha_ {b} C _ {b} (x)\right).\tag{3}
$$

The AdaBoost algorithm is shown below:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
AdaBoost algorithm (Freund and Schapire [19])
1. Start with  $\omega_{b}(i)=1/n, i=1,2,\ldots,n.$ 
2. Repeat for  $b=1,2,\ldots,B$ 
a) Fit the classifier  $C_{b}(x)\in\{-1,1\}$  using weights  $\omega_{b}(i)$  on  $T^{b}$ .
b) Compute:  $\varepsilon_{b}=\sum_{i=1}^{n}\omega_{b}(i)\xi_{b}(i)$  and  $\alpha_{b}=ln((1-\varepsilon_{b})/\varepsilon_{b})$ 
c) Update the weights  $\omega_{b+1}(i)=\omega_{b}(i)\cdot\exp(\alpha_{b}\xi_{b}(i))$  and normalize them.
3. Output the final classifier  $C(x)=\text{sign}\left(\sum_{b=1}^{B}\alpha_{b}C_{b}(x)\right)$
</div>

Freund and Schapire [20] showed that when the number B of iterations is increased, the training error level of the AdaBoost classifier exponentially tends to zero. They also demonstrated that the generalization or true error $\left( \varepsilon _ { R } \right)$ of the final classifier $C _ { F } ( \boldsymbol { x } )$ has an upper limit which depends on the training or apparent error $( \varepsilon _ { A } )$ , the size of the training set (n), the Vapnik-Chervonenkis's dimensionality coefficient of the parametric space of basic classifiers (d) and the number of iterations B in AdaBoost (number of combined single classifiers)

$$
\hat {\varepsilon} _ {R} = \hat {\varepsilon} _ {A} + O \left(\sqrt {\frac {B d}{n}}\right).\tag{4}
$$

The generalization error of the final classifier may be reduced by increasing the size of the training data set. This error will increase when the number of single classifiers included increases. This is a sign of the classifier overfitting (a classifier is said to be overfitted when it is too closely adjusted to the training set, thereby losing its generalization capacity on the total population, and being therefore inaccurate when classifying previously unseen samples).

## 3. Problem description

Predicting corporate failure is an important management science problem and its main goal is to differentiate those firms with a high probability of distress in the future from healthy firms. In other words, a model is built to forecast the moment of distress so that the firm's economic agents may make suitable decisions. In order to be able to predict failure, it is essential to have access to information about the company's situation. This information is basically given by financial ratios but additional information (e.g. activity, company size, age, etc.) should also be taken into account.

Prediction of corporate failure is not new and many studies have dealt with this problem since 1966. It is therefore interesting to study the state of the art of corporate failure prediction. There is no doubt that the pioneering failure prediction studies were provided by Beaver [9] at a univariate level and Altman [2] with the application of multivariate analysis. Subsequently, and basically to overcome the restrictive statistical requirements of normality for the explanatory variables and equality for the variance-covariance group matrices, logit and probit models were also applied (Ohlson [36] and Zmijewski [58]). Classification trees or recursive partitioning proved useful in studies by Frydman et al.

[23]. More recently, artificial neural networks have been introduced as a powerful approach to this task (Odom and Sharda, [35]). For a more detailed study of neural network applications in bankruptcy forecasting see Chang Lee et al. [15], Laitinen and Kankaanpaa [30], Perez [38] or the most recent work provided by Ravi Kumar and Ravi [44]. These papers present an interesting collection of the main failure prediction studies which are grouped according to the classification method used for prediction. Some of these results are shown in Table 1. Relating to the comparison of results, it should be noted that although classification accuracies of these studies are shown in Laitinen's work, care should be taken when comparing the prediction ability of alternative techniques in accounting because of the different starting conditions in alternative studies.

Although there is a general consensus on the importance of failure prediction, there is not the same degree of agreement on the definition of corporate failure (i.e. when a company is considered to have failed). From a global perspective, a firm will have failed if it does not achieve its goals, especially those relating to profitability, solvency, and survival. However and in order to facilitate comparisons with previous studies, we have used the most common corporate failure definition which uses a legal perspective and only includes bankruptcy and firms in temporary receivership as failed firms.

## 4. Data description

The companies used in this study were selected from the SABI database of Bureau Van Dijk (BVD), one of Europe's leading publishers of electronic business information databases and provider of the Wharton Research Data Services. SABI covers all the companies whose accounts are placed on the Spanish Mercantile Registry.

Results of previous experiences on bankruptcy forecasting [44]

<table><tr><td>Study</td><td>Sample size</td><td>Neural models(1)</td><td>Other methods</td><td>Best results with ...</td></tr><tr><td>Tam [51]</td><td>188</td><td>BP</td><td>LDA, F-L, K-NN, ID3</td><td>BP</td></tr><tr><td>Tam and Kiang [52]</td><td>202</td><td>FF, BP</td><td>LDA, LOGIT, K-NN, ID3</td><td>NN</td></tr><tr><td>Salchenberger [46]</td><td>862</td><td>BP</td><td>LOGIT</td><td>BP</td></tr><tr><td>Sharda and Wilson [49]</td><td>129</td><td>BP</td><td>LDA, LOGIT</td><td>BP</td></tr><tr><td>Fletcher and Goss [18]</td><td>36</td><td>BP</td><td>LOGIT</td><td>BP</td></tr><tr><td>Altman et al. [3]</td><td>3465</td><td>BP</td><td>LDA</td><td>LDA</td></tr><tr><td>Wilson and Sharda [55]</td><td>129</td><td>BP</td><td>LDA</td><td>BP</td></tr><tr><td>Tsukuda and Baba [53]</td><td>114</td><td>BP</td><td>LDA</td><td>BP</td></tr><tr><td>Lacher et al. [29]</td><td>282</td><td>CASCOR</td><td>LDA</td><td>CASCOR</td></tr><tr><td>Leshno and Spector [34]</td><td>88</td><td>P</td><td>LDA</td><td>P</td></tr><tr><td>Rahimian et al. [43]</td><td></td><td>BP, AT, P</td><td>LDA</td><td>BP</td></tr><tr><td>Serrano-Cinca [47]</td><td>129</td><td>SOFM with LDA, BP, P, AT</td><td></td><td>BP, P, AT</td></tr><tr><td>Serrano-Cinca [48]</td><td>66</td><td>FF</td><td>LDA</td><td>FF</td></tr><tr><td>Barniv et al [7]</td><td>237</td><td>BP</td><td>NPDA, LOGIT</td><td>BP</td></tr><tr><td>Bell [10]</td><td>2067</td><td>BP</td><td>LOGIT</td><td>BP</td></tr><tr><td>Piramuthu et al. [39]</td><td>182 202 48</td><td>BP, BPFC</td><td></td><td>BPFC</td></tr><tr><td>Kiviluoto [27]</td><td>1137</td><td>LVQ, SOFM, RBF-SOFM</td><td>K-NN</td><td>RBF-SOFM</td></tr><tr><td>Zhang et al. [57]</td><td>220</td><td>GRG2NN</td><td>LOGIT</td><td>GRG2NN</td></tr><tr><td>Yang et al. [56]</td><td>122</td><td>PNN-PN PNN, BP</td><td>FDA, LDA</td><td>PNN and BP with non-deflated data and FDA with deflated data</td></tr><tr><td>Charalambous [16]</td><td>278</td><td>SOFM, RBF, BP, LVQ FF (LSEF+CG)</td><td>LOGIT</td><td>FF (LSEF+CG)</td></tr><tr><td>Atiya [4]</td><td>1160</td><td>BP</td><td></td><td>BP with novel indicators</td></tr><tr><td>Kaski et al. [26]</td><td>1500</td><td>SOFM-E, SOFM-F</td><td></td><td>SOFM-F</td></tr><tr><td>Swicegood and Clark [50]</td><td>1741</td><td>BP</td><td>LDA, REG</td><td>BP</td></tr><tr><td>Baek and Cho [6]</td><td>662</td><td>AANN, BP</td><td></td><td>AANN</td></tr><tr><td>Lam [31]</td><td>364</td><td>BP</td><td></td><td>BP integrating fundamental and technical analysis</td></tr><tr><td>Lee et al. [32]</td><td>166</td><td>LDA-ASBP ID3-ASBP SOFM-ASBP</td><td>LDA, ID3</td><td>Hybrid BP models</td></tr><tr><td>Lee et al. [33]</td><td>168</td><td>BP, SOFM</td><td>LDA</td><td>BP</td></tr></table>

<sup>(1)</sup>AANN=Auto associative neural networks, AT=Athena, BP=Backpropagation, CASCOR=Cascade correlation neural network, CG=Conjugate Gradient, FF=Feedforward, F-L=Factor-logistic, GRG2NN=Generalized reducing gradient, ID3-ASBP=ID3 assisted Backpropagation, K-NN=K-nearest neighbour, LDA=Linear Discriminant Analysis, LDA-ASBP=LDA assisted Backpropagation, LVQ=Learning Vector Quantization, MLP=Multilayer Perceptron, P=Single layer Perceptron, RBF=Radial Basis Functions, REG=Regulators, SOFM=Self Organizing Feature Maps, SOFM-ASBP=SOFM assisted Backpropagation, SOFM-E=Euclidean Self Organizing Maps, SOFM-F=Fisher metric Self Organizing Maps

In the case of failed firms, firms which had failed (bankruptcy and temporary receivership) during the period 2000–2003 were selected, but with the additional requirement that full information be provided about all the variables at the moment of failure and from the previous year. It is usual in failure prediction studies to select failed firms from various years in order to collect a higher sample size. There were therefore firms that had failed in the years 2000, 2001, 2002 and 2003 so the information on variables should be understood in relative terms with respect to the moment of failure (t) with the previous year being t − 1.

Healthy firms, on the other hand, were selected from active companies at the end of 2003 with full data for 2003 and 2002. In this case, a second requirement was added: any firm with constantly negative profits during the last three years would be rejected, the reason being that even though they were still active in December 2003, they would soon enter a state of failure if they kept making a loss.

Within these requirements, 590 firms were randomly selected for each group (failed/healthy), obtaining 1180 observations for the total data set. Instead of pairing the failed/healthy firms by sector or size as several failure studies have done, these variables were used as predictors in the selection process: the sector as a qualitative variable with ten categories using the National Classification of Economic Activities (NACE-93 digit-1 level), and the size using the natural logarithm of Total Assets as a proxy variable. The legal structure was also used as a categorical explanatory variable with three options: public corporations, limited corporations, and other corporations.

In addition, thirteen accounting-based ratios were included in the initial data set. In failure prediction studies, financial ratios are usually selected on the basis of three criteria: they should be commonly used in failure prediction literature, the information needed to calculate these ratios should be available, and finally, the researchers' own decisions based on their experience in previous studies or on the basis of the preliminary trials. The same criteria were followed in this study. Sixteen predictor variables were therefore used for each company with information from the year prior to the moment of failure and these variables are listed in Table 2.

Once the explanatory variables were selected, we carried out an exploratory analysis of the quantitative data. Tables 3 and 4 show some statistics, normality tests for each variable and the correlation matrix. From these results it is worth to point out that none of the variables follows a normal distribution and that there is a high degree of correlation among the variables.

Table 2  
Description of variables

<table><tr><td>Variable</td><td>Description</td><td>Variable</td><td>Description</td></tr><tr><td>CA.TA</td><td>Current Assets/Total Assets</td><td>L.TD</td><td>Liabilities/Total Debt</td></tr><tr><td>CA.CL</td><td>Current Assets/Current Liabilities</td><td>C.TA</td><td>Cash/Total Assets</td></tr><tr><td>EBIT.TA</td><td>Earnings before interest and taxes/Total Assets</td><td>C.CL</td><td>Cash/Current liabilities</td></tr><tr><td>CF.TD</td><td>Cash Flow/Total Debt</td><td>S.CAP</td><td>Sales/Capital</td></tr><tr><td>NACE1</td><td>NACE code at one digit</td><td>EBIT.CAP</td><td>Earnings before taxes/Capital</td></tr><tr><td>WC.TA</td><td>Working Capital/Total Assets</td><td>lnTA</td><td>Logarithm of Total Assets</td></tr><tr><td>WC.S</td><td>Working Capital/Sales</td><td>S.CA</td><td>Sales /Current Assets</td></tr><tr><td>LE</td><td>Legal structure</td><td>S.TA</td><td>Sales /Total Assets</td></tr></table>

Some of the following ratios are explained in White [54] and also in the web http://faculty.philau.edu/lermackh/.

Furthermore, Table 5 shows the discriminant capacity of each variable and the misclassification percentage of the univariate approach (LDA). Although some variables present acceptable discriminant power, we decided not to apply linear techniques based on the Fisher approach (linear discriminant or logistic regression) because the conditions to be optimal could not be satisfied (normality and unitary covariance matrix). As an alternative to overcome this problem, we could use natural logarithm transformations to approximate a normal distribution even though the transformed variables may be very difficult to interpret in this area. However, as it will be shown in Section 5, we applied the LDA in order to have a basic reference to be able to compare the results provided by the Adaboost and Artificial Neural Network model.

## 5. Experimental results

In this paper, the same failure prediction problem is solved using two different classification methods in order to compare their classification accuracies in this task. To estimate the real accuracy, the total initial sample of 1180 Spanish companies was divided into two sets: eighty percent were used as a training set to build the classifier, and the rest were hidden from the classification method and were presented as new data to check the prediction accuracy. The training set therefore comprised 472 healthy firms and a further 472 failed firms (944 firms represent 80% of the total set). The test set consisted of 236 firms, with an equal number of healthy and failed firms (20% of the total). As mentioned before, 16 diagnostic variables were used for each company with information for the year prior to the moment of failure.

C<sub>orre</sub>l<sub>a</sub>ti<sub>on ma</sub>t<sub>r</sub>i<sub>x</sub>  
T<sub>a</sub>bl<sub>e</sub> 3  
R<sub>esu</sub>lt<sub>s</sub> <sub>o</sub>bt<sub>a</sub>i<sub>ne</sub>d f<sub>rom</sub> <sub>exp</sub>l<sub>ora</sub>t<sub>ory</sub> d<sub>a</sub>t<sub>a</sub> <sub>ana</sub>l<sub>ys</sub>i<sub>s</sub>

<table><tr><td></td><td>EBIT.TA</td><td>EBIT.CAP</td><td>CA.TA</td><td>C.TA</td><td>S.CAP</td><td>CA.CL</td><td>C.CL</td><td>WC.S</td><td>L.TD</td><td>CF.TD</td><td>WC.TA</td><td>S.TA</td><td>S.CA</td><td>lnTA</td></tr><tr><td>Mean</td><td>1.5514</td><td>0.5328</td><td>0.5197</td><td>0.1474</td><td>8.1580</td><td>2.7673</td><td>0.7119</td><td>2.0219</td><td>-0.3856</td><td>0.8728</td><td>0.0187</td><td>1.0233</td><td>1.0065</td><td>7.5469</td></tr><tr><td>Median</td><td>0.0784</td><td>0.3855</td><td>0.5984</td><td>0.0404</td><td>0.7804</td><td>1.1235</td><td>0.1025</td><td>0.0670</td><td>0.6832</td><td>0.0624</td><td>0.0620</td><td>0.8442</td><td>1.4837</td><td>7.4184</td></tr><tr><td>Std. Dev.</td><td>54.8164</td><td>4.3662</td><td>5.7313</td><td>1.8576</td><td>63.1374</td><td>17.1474</td><td>18.0535</td><td>17.2610</td><td>10.0915</td><td>10.1956</td><td>4.9913</td><td>1.3517</td><td>44.4035</td><td>1.5616</td></tr><tr><td>Asymmetry</td><td>31.6723</td><td>14.3114</td><td>-24.9542</td><td>20.3904</td><td>2.8566</td><td>-2.4655</td><td>-20.7833</td><td>0.6569</td><td>24.3215</td><td>-27.2205</td><td>-24.2789</td><td>-1.5633</td><td>-33.6943</td><td>0.5617</td></tr><tr><td>Skewness</td><td>1072.4834</td><td>305.8308</td><td>846.8311</td><td>733.5410</td><td>216.9099</td><td>182.5282</td><td>604.3463</td><td>95.7141</td><td>757.4138</td><td>872.4553</td><td>782.4589</td><td>36.3493</td><td>1147.4768</td><td>1.9395</td></tr><tr><td>Minimum</td><td>-394.3403</td><td>-25.1707</td><td>-179.9724</td><td>-27.4740</td><td>-1106.5820</td><td>-294.5847</td><td>-521.8325</td><td>-240.3293</td><td>-46.8859</td><td>-324.0337</td><td>-154.2119</td><td>-16.2484</td><td>-1514.6670</td><td>1.4081</td></tr><tr><td>Maximum</td><td>1840.4110</td><td>102.4375</td><td>66.5612</td><td>56.0455</td><td>1225.0620</td><td>283.4821</td><td>121.3837</td><td>239.3921</td><td>310.0544</td><td>60.1981</td><td>49.0374</td><td>10.4067</td><td>66.2963</td><td>15.0009</td></tr><tr><td>1st Quartil</td><td>0.0194</td><td>0.1390</td><td>0.1790</td><td>0.0117</td><td>0.0468</td><td>0.8083</td><td>0.0200</td><td>-0.0786</td><td>-1.1317</td><td>0.0114</td><td>-0.0474</td><td>0.0577</td><td>0.4463</td><td>6.5744</td></tr><tr><td>3rd Quartil</td><td>0.2778</td><td>0.6984</td><td>0.8683</td><td>0.1022</td><td>8.1562</td><td>2.0993</td><td>0.5633</td><td>0.7276</td><td>0.9118</td><td>1.5821</td><td>0.2064</td><td>1.6190</td><td>2.5122</td><td>8.4297</td></tr><tr><td>SW Test</td><td>0.0180</td><td>0.1812</td><td>0.0493</td><td>0.0563</td><td>0.2205</td><td>0.2405</td><td>0.1053</td><td>0.2706</td><td>0.1711</td><td>0.1228</td><td>0.0599</td><td>0.7327</td><td>0.0275</td><td>0.9745</td></tr><tr><td>SWp-value</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>KS test</td><td>0.3743</td><td>0.3558</td><td>0.4992</td><td>0.4992</td><td>0.4418</td><td>0.5559</td><td>0.4559</td><td>0.2465</td><td>0.2792</td><td>0.3651</td><td>0.3122</td><td>0.4738</td><td>0.4858</td><td>0.9970</td></tr><tr><td>KS p-value</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000.</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 4

<table><tr><td></td><td>EBIT.TA</td><td>EBIT.CAP</td><td>CA.TA</td><td>C.TA</td><td>S.CAP</td><td>CA.CL</td><td>C.CL</td><td>WC.S</td><td>L.TD</td><td>CF.TD</td><td>WC.TA</td><td>S.TA</td><td>S.CA</td><td>lnTA</td></tr><tr><td>EBIT.TA</td><td>1.0000</td><td>0.0356</td><td>0.5241</td><td>0.9500</td><td>-0.0035</td><td>0.0019</td><td>0.0031</td><td>-0.0092</td><td>-0.0121</td><td>0.1012</td><td>0.4728</td><td>-0.2322</td><td>-0.0009</td><td>-0.0972</td></tr><tr><td>EBIT.CAP</td><td>0.0356</td><td>1.0000</td><td>0.0122</td><td>0.0309</td><td>0.2833</td><td>0.0011</td><td>0.0019</td><td>0.0115</td><td>0.0007</td><td>0.0105</td><td>0.0119</td><td>0.0064</td><td>-0.0025</td><td>-0.0019</td></tr><tr><td>CA.TA</td><td>0.5241</td><td>0.0122</td><td>1.0000</td><td>0.6997</td><td>0.0067</td><td>0.0084</td><td>-0.0007</td><td>0.0124</td><td>0.0015</td><td>0.0290</td><td>0.9603</td><td>0.2638</td><td>0.0020</td><td>0.0107</td></tr><tr><td>C.TA</td><td>0.9500</td><td>0.0309</td><td>0.6997</td><td>1.0000</td><td>-0.0061</td><td>-0.0035</td><td>-0.0368</td><td>-0.0290</td><td>-0.0252</td><td>0.0950</td><td>0.6282</td><td>-0.1172</td><td>0.0015</td><td>-0.0936</td></tr><tr><td>S.CAP</td><td>-0.0035</td><td>0.2833</td><td>0.0067</td><td>-0.0061</td><td>1.0000</td><td>-0.0119</td><td>-0.0044</td><td>-0.0152</td><td>0.0160</td><td>-0.0106</td><td>-0.0008</td><td>0.1428</td><td>0.0056</td><td>0.0366</td></tr><tr><td>CA.CL</td><td>0.0019</td><td>0.0011</td><td>0.0084</td><td>-0.0035</td><td>-0.0119</td><td>1.0000</td><td>0.2627</td><td>0.1035</td><td>-0.0589</td><td>0.0357</td><td>0.0197</td><td>-0.0684</td><td>-0.0010</td><td>-0.0223</td></tr><tr><td>C.CL</td><td>0.0031</td><td>0.0019</td><td>-0.0007</td><td>-0.0368</td><td>-0.0044</td><td>0.2627</td><td>1.0000</td><td>0.0222</td><td>0.0936</td><td>-0.0442</td><td>0.0015</td><td>-0.0229</td><td>0.0019</td><td>0.0131</td></tr><tr><td>WC.S</td><td>-0.0092</td><td>0.0115</td><td>0.0124</td><td>-0.0290</td><td>-0.0152</td><td>0.1035</td><td>0.0222</td><td>1.0000</td><td>-0.0669</td><td>0.0612</td><td>0.0339</td><td>-0.0879</td><td>0.0062</td><td>-0.0104</td></tr><tr><td>L.TD</td><td>-0.0121</td><td>0.0007</td><td>0.0015</td><td>-0.0252</td><td>0.0160</td><td>-0.0589</td><td>0.0936</td><td>-0.0669</td><td>1.0000</td><td>-0.9526</td><td>0.0025</td><td>0.0993</td><td>0.0625</td><td>-0.0505</td></tr><tr><td>CF.TD</td><td>0.1012</td><td>0.0105</td><td>0.0290</td><td>0.0950</td><td>-0.0106</td><td>0.0357</td><td>-0.0442</td><td>0.0612</td><td>-0.9526</td><td>1.0000</td><td>0.0322</td><td>-0.1002</td><td>-0.0552</td><td>0.0183</td></tr><tr><td>WC.TA</td><td>0.4728</td><td>0.0119</td><td>0.9603</td><td>0.6282</td><td>-0.0008</td><td>0.0197</td><td>0.0015</td><td>0.0339</td><td>0.0025</td><td>0.0322</td><td>1.0000</td><td>0.2098</td><td>-0.0019</td><td>0.0369</td></tr><tr><td>S.TA</td><td>-0.2322</td><td>0.0064</td><td>0.2638</td><td>-0.1172</td><td>0.1428</td><td>-0.0684</td><td>-0.0229</td><td>-0.0879</td><td>0.0993</td><td>-0.1002</td><td>0.2098</td><td>1.0000</td><td>0.0435</td><td>-0.1790</td></tr><tr><td>S.CA</td><td>-0.0009</td><td>-0.0025</td><td>0.0020</td><td>0.0015</td><td>0.0056</td><td>-0.0010</td><td>0.0019</td><td>0.0062</td><td>0.0625</td><td>-0.0552</td><td>-0.0019</td><td>0.0435</td><td>1.0000</td><td>-0.0401</td></tr><tr><td>lnTA</td><td>-0.0972</td><td>-0.0019</td><td>0.0107</td><td>-0.0936</td><td>0.0366</td><td>-0.0223</td><td>0.0131</td><td>-0.0104</td><td>-0.0505</td><td>0.0183</td><td>0.0369</td><td>-0.1790</td><td>-0.0401</td><td>1.0000</td></tr></table>

Table 5  
ANOVA and discriminatory capacity for each variable

<table><tr><td></td><td>EBIT. TA</td><td>EBIT. CAP</td><td>CA. TA</td><td>C.TA</td><td>S.CAP</td><td>CA.CL</td><td>C.CL</td><td>WC.S</td><td>L.TD</td><td>CF.TD</td><td>WC. TA</td><td>S.TA</td><td>S.CA</td><td>lnTA</td></tr><tr><td colspan="15">ANOVA for each variable</td></tr><tr><td>F value</td><td>0.9811</td><td>0.0486</td><td>1.7694</td><td>2.7768</td><td>12.4850</td><td>10.3950</td><td>1.3542</td><td>19.339</td><td>20.226</td><td>9.4274</td><td>0.1121</td><td>294.38</td><td>1.0849</td><td>0.0675</td></tr><tr><td>Prob (&gt;F)</td><td>0.3221</td><td>0.8256</td><td>0.1837</td><td>0.0959</td><td>0.0004</td><td>0.0013</td><td>0.2448</td><td>0.0000</td><td>0.0000</td><td>0.0022</td><td>0.7378</td><td>0.0000</td><td>0.2978</td><td>0.7951</td></tr><tr><td colspan="15">LDA using each variable as explanatory (50 experiments: 5×10 folders cross validation)</td></tr><tr><td>Mean error rate</td><td>0.4961</td><td>0.5097</td><td>0.4331</td><td>0.4654</td><td>0.3383</td><td>0.3595</td><td>0.4537</td><td>0.3304</td><td>0.2138</td><td>0.2705</td><td>0.4878</td><td>0.2214</td><td>0.4996</td><td>0.4966</td></tr></table>

In order to apply the AdaBoost algorithm, we have used the adabag library [1] for the R statistical program. This program consists of a series of packages for data manipulation, calculus, and graphics [42]. Among other characteristics, it has a well developed and effective programming language (R language). The R program has much in common with the well-known S-Plus program, but with the difference that the R program is a freely available software program which can be downloaded from http://cran.r-project.org/. The R program has a base environment, with a few statistical, mathematical, and graphical utilities. More sophisticated techniques can be added using packages which are available on the CRAN website mentioned above. On the other hand, the neural networks models have been implemented using the TRAJAN software (http://www. trajan-software.demon.co.uk/).

## 5.1. Corporate failure prediction using neural networks

An artificial neural network is an information processing device inspired on biological nervous systems. Generally these models consist of a set of computational units, also called neurons, organized in layers. Each neuron is connected to other neurons through synaptic junctions called synapses. The learning process is shown through changes in strength connections. There are several models of artificial neural networks. The most common architecture is the Multilayer Perceptron [11,25], a feedforward network that consists of an input layer, an output layer and a number of hidden layers. This kind of nets is fundamentally characterized by the fact that information signal is propagated from the input nodes until it has reached an output node without cycles of links. The goal is to find suitable values for the synaptic weights so that minimize the deviation between the output given by the net and the desired output. This process is known as supervised learning and the most known mechanism for weight adaptation is the backpropagation algorithm [45]. The B-P method uses gradient descent to change the weights proportional to the derivative of the error function with respect to each weight. The procedure is repeated for all patterns in the training set. The patterns are continuously presented and weights are adjusted until the error is sufficiently low.

The neural network model selected in this work is the well-known Multilayer Perceptron with one hidden layer. The number of nodes in the input and the output layers has been set by the structure of our analysis, i. e. the number of explanatory and output variables, respectively. On the other hand, several experiments were conducted to find the number of hidden elements which gave the greatest accuracy in predicting the test data set. Table 6 shows the results (minimum, maximum and mean percentage of correctly classified cases) obtained from twenty different topologies,

## Table 6

Impact of the number of hidden nodes in the percentage of correctly classified cases (10 experiments for each topology)

<table><tr><td rowspan="2">#hidden layers</td><td colspan="3">% of correctly classified cases</td></tr><tr><td>Min</td><td>Max</td><td>Mean</td></tr><tr><td>1</td><td>57.63</td><td>58.47</td><td>58.39</td></tr><tr><td>2</td><td>53.39</td><td>80.51</td><td>61.86</td></tr><tr><td>3</td><td>57.63</td><td>71.19</td><td>60.68</td></tr><tr><td>4</td><td>55.08</td><td>70.34</td><td>59.49</td></tr><tr><td>5</td><td>55.93</td><td>66.95</td><td>59.32</td></tr><tr><td>6</td><td>56.78</td><td>63.56</td><td>59.24</td></tr><tr><td>7</td><td>56.78</td><td>61.86</td><td>58.64</td></tr><tr><td>8</td><td>57.63</td><td>76.27</td><td>61.78</td></tr><tr><td>9</td><td>57.63</td><td>66.95</td><td>60.00</td></tr><tr><td>10</td><td>56.78</td><td>60.17</td><td>58.47</td></tr><tr><td>11</td><td>56.78</td><td>64.41</td><td>59.32</td></tr><tr><td>12</td><td>55.93</td><td>84.75</td><td>64.49</td></tr><tr><td>13</td><td>55.93</td><td>77.97</td><td>60.51</td></tr><tr><td>14</td><td>57.63</td><td>77.12</td><td>62.88</td></tr><tr><td>15</td><td>57.63</td><td>75.42</td><td>60.51</td></tr><tr><td>16</td><td>56.78</td><td>72.03</td><td>60.42</td></tr><tr><td>17</td><td>56.78</td><td>77.12</td><td>63.31</td></tr><tr><td>18</td><td>56.78</td><td>67.80</td><td>59.92</td></tr><tr><td>19</td><td>57.63</td><td>82.20</td><td>63.05</td></tr><tr><td>20</td><td>56.78</td><td>69.49</td><td>61.19</td></tr></table>

varying the number of hidden elements from 1 to 20 and training ten times each topology. This procedure resulted in the selection of a 16:27-12-1:1 network, i.e. an input layer with sixteen nodes, pre-processed into twenty-seven nodes (The qualitative variables LE and NACE1 have been encoded using the one-of-N method. This technique uses a set of dichotomous variables, one for each possible nominal value. Three nodes have been necessary for LE and ten for NACE1. So, the total number of input variables changed from 16 to 27), a hidden layer with twelve elements, and finally an output layer with one. This architecture is shown in Fig. 1.

In order to train the network, the following decisions were set. Firstly, the above mentioned division of the sample cases into two subsets: training and test. The activation functions were selected to be linear in the input layer and sigmoid in the hidden and output layers. The error function selected was the sum of squared errors and the learning algorithm to minimize it was Back Propagation with adaptive learning starting at 0.3 and finishing at 0.01 and momentum term set at the value 0.3. After 1868 epochs the network was trained and the following results were yielded. The main result from the confusion matrix in Table 7 is the error percentage, measured as the percentage of wrongly classified cases. The error is closed to 11% for the training set and it is a little higher for the test set (12.712%). It is worth stressing that if we consider the most important error as the classification of a failed firm as a healthy one (Type I error), the behaviour of the network is very satisfactory since it is about 4.025% in the training set (7.627% in the test set).

![](/api/attachments/8GMJXHXE/fulltext/images/bafb7a6a3661a75ceb65e7d41d2e9d15cd9edef6bbdbcb0b9ff3e91455d1ac23.jpg)  
Fig. 1. MLP 16:27-12-1:1 architecture.

Table 7  
Confusion matrices and errors of the Neural Network classifier

<table><tr><td rowspan="2">Predicted class</td><td colspan="5">Observed class</td></tr><tr><td>N. Network (MLP)</td><td>Training Failed</td><td>10.805% Healthy</td><td>Test Failed</td><td>12.712% Healthy</td></tr><tr><td></td><td>Failed</td><td>453</td><td>83</td><td>109</td><td>21</td></tr><tr><td></td><td>Healthy</td><td>19</td><td>389</td><td>9</td><td>97</td></tr></table>

The relative contribution of each input variable to the global performance can be assessed by means of a sensitivity analysis, which entails testing the performance of the network as if the input variables were unavailable. This ratio measures the relation of the error if the correspondent input variable is unavailable with the error if all the variables are available. A ratio of one or lower therefore means that pruning this input variable has no effect on the performance of the network. Table 8 shows the ranking of the input variables with a ratio above 1.05, which means that these variables can be considered as the most important ones in terms of their discriminatory power. According to the sensitive analysis results, the most important ratios are the efficiency, the sector the proxy variable for the firm size, the legal structure and the level of indebtedness. The first ratio refers to as the rate of sales over the total assets and shows, in a figurative sense, how many times the asset has been sold and, therefore, its number of turnovers, i.e. how many times it has been sold and replaced. This ratio can also be interpreted as the amount of sales in euros by each euro invested in assets, reflecting the capacity of assets to generate sales and the firm relative efficiency on managing them. The higher this ratio, for the same commercial margin, the higher the profit for a lower invest and, therefore, the higher the profitability.

It is worth to stress that the following variables in the ranking are not the usual financial ratios but the additional firm information proposed as potentially useful in this research.

The fifth ratio is L.TD (Liabilities/Total Debt). This ratio considers the weight of indebtedness in the financial structure, showing that firms with lower levels of indebtedness are more able to apply for new external financing sources and therefore, have greater possibilities of survival.

Table 8  
Sensitive analysis

<table><tr><td>Ranking</td><td>Variable</td><td>Ratio</td></tr><tr><td>1</td><td>S.TA</td><td>1.3091</td></tr><tr><td>2</td><td>NACE1</td><td>1.2109</td></tr><tr><td>3</td><td>LnTA</td><td>1.1585</td></tr><tr><td>4</td><td>LE</td><td>1.1311</td></tr><tr><td>5</td><td>L.TD</td><td>1.0964</td></tr></table>

## 5.2. Corporate failure prediction using AdaBoost

The adabag package has three functions dealing with AdaBoost developed in R language: the first trains the AdaBoost classifier and assigns a class to the examples of the training set, the second uses a previously trained AdaBoost classifier to predict the classes of the cases in the new data set, and the third enables cross validation to be applied in order to estimate the error of an AdaBoost classifier. As in any R function, there are a few initial arguments to be set such as the name of the data frame where the data is stored or the name of the variable that contains the observation class and the explanatory variables, the number of individual trees to be used, and the size of these trees.

AdaBoost can use any sort of classification system as the individual classifier, but we have used decision trees [14] in this application basically for the following three reasons: decision trees are used in most AdaBoost applications, they achieve good results and classification trees easily handle qualitative variables. Very briefly, we can see a classification tree like a method to express knowledge and aid decision making. This technique provides a way to encapsulate and structure the knowledge of experts to be used by less-experienced user. The construction of classification trees aims to find a decision tree that is as small as possible and fits the data. This way it is assumed that it is more likely to find a good generalization of the training data. A tree is first built as a given set of pre-classified training examples partitioned recursively according to a chosen attribute at each node. The tree-building process is further divided into three steps: attributes evaluation, splitting point selection and training data partition. Then a bottom-up tree pruning process follows to remove branches with lower predictive power, once the whole decision tree has been built. Pruning techniques, such as those used in the most known algorithms ID3 [40], CART [14] and C4.5 [41] have proved to be really useful in order to avoid overfitting.

Table 9  
Confusion matrices and errors of the AdaBoost classifier

<table><tr><td rowspan="3">Predicted class</td><td colspan="5">Observed class</td></tr><tr><td>AdaBoost</td><td>Training</td><td>7.627%</td><td>Test</td><td>8.898%</td></tr><tr><td></td><td>Failed</td><td>Healthy</td><td>Failed</td><td>Healthy</td></tr><tr><td></td><td>Failed</td><td>460</td><td>60</td><td>114</td><td>17</td></tr><tr><td></td><td>Healthy</td><td>12</td><td>412</td><td>4</td><td>101</td></tr></table>

Table 10  
Comparison of results with other methods

<table><tr><td rowspan="3">Models</td><td colspan="6">Error rates</td></tr><tr><td colspan="3">Training</td><td colspan="3">Testing</td></tr><tr><td>Overall</td><td>Type I</td><td>Type II</td><td>Overall</td><td>Type I</td><td>Type II</td></tr><tr><td>LDA</td><td>20.763%</td><td>24.364%</td><td>17.161%</td><td>20.339%</td><td>28.814%</td><td>11.864%</td></tr><tr><td>C.Trees</td><td>10.452%</td><td>0.753%</td><td>20.155%</td><td>12.714%</td><td>3.390%</td><td>22.034%</td></tr><tr><td>ANN</td><td>10.805%</td><td>4.025%</td><td>17.585%</td><td>12.712%</td><td>7.627%</td><td>17.797%</td></tr><tr><td>AdaBoost</td><td>7.627%</td><td>2.523%</td><td>12.712%</td><td>8.898%</td><td>3.390%</td><td>14.407%</td></tr></table>

Using the functions described above an AdaBoost classifier is built with 100 trees that have been pruned using a maximum depth of 2 to limit the size of the individual tree in each AdaBoost epoch. The depth of the tree is the distance between a leaf node and the root node. Since the test error is of 8.898%, there is a reduction of 30% compared with the neural network test error, which is of 12.712%. In addition, if the confusion matrix is analyzed, it can be seen that most of these errors are made because a healthy firm is classified as failed while the Type I error is 3.39% in the test set. Table 9 shows the errors of the AdaBoost classifier in the training and test sets and their confusion matrices.

As we mentioned in the previous section a LDA was carried out only with the purpose of having a reference point. As it can be seen in Table 10, the results from the linear model are much less satisfactory with a percentage of misclassification over 20% in both (training and test) data sets. Table 10 also shows the results provided by a single tree pruned by the rule “minimum error in crossvalidation plus one standard deviation”. These results are very similar to the neural network ones.

In order to ensure that the comparison between the neural network model and the AdaBoost ensemble does not happen by chance, we used five repetitions of 10- fold cross-validation (Opitz and Maclin [37]). The entire set (1180 firms) is used for each of the 10-fold crossvalidation experiment. This way we obtained the error rates for the AdaBoost and the Neural Networks on each one of the 50 experiments. Once we checked the normality of the error distributions of both classification methods using the tests shown in Table 11, we can apply the test for comparing the means of two normal distributions. To achieve a higher degree of certainty we used the one tail test, establishing the null hypothesis that the average error of the AdaBoost classifier is equal or higher than the neural network average error against the alternative hypothesis that it is lower than the neural network one. This way, if we reject the null hypothesis, we will be almost sure that the alternative one is true. The result obtained is enlightening because the t statistic is −8.0884 and its corresponding p-value is 8.821• $1 0 ^ { - 1 3 }$ . So we can reject the null hypothesis and state that the differences are statistically significant with Ada-Boost ahead. In fact, AdaBoost reduces the average error in the cross-validation analysis by 28.04% compared with the neural network.

Table 11  
Normality tests, average and standard deviation error

<table><tr><td>Test</td><td>N.Network</td><td>AdaBoost</td></tr><tr><td>Kolmogorov–Smirnov</td><td>0.1454</td><td>0.1103</td></tr><tr><td>KS. p value</td><td>0.2408</td><td>0.5768</td></tr><tr><td>Shapiro</td><td>0.9559</td><td>0.9766</td></tr><tr><td>Shapiro p value</td><td>0.0602</td><td>0.4196</td></tr><tr><td>Average error</td><td>0.1359</td><td>0.0978</td></tr><tr><td>Standard deviation</td><td>0.0249</td><td>0.0222</td></tr></table>

The AdaBoost function of the adabag package allows us to quantify the relative importance of the predictor variables. This is a really important advantage because it is difficult to interpret the hundreds or thousands of trees used in the AdaBoost ensemble. This measure takes into account how often each variable is selected to realize a split. It is logical to consider that the more important variables will be used in a greater number of splits than the less important ones. Table 12 shows all variables arranged from the greatest to least relative importance. In this case, the most important ratios are EBIT.TA, L.TD, S.TA and lnTA with values at this measure of 17.33, 13.72, 10.47 and 9.02%, respectively. Those variables which are different from financial ratios (NACE1, lnTA and LE) have an interesting contribution of 20.2% in total.

Table 12  
Relative importance of variables

<table><tr><td>Variable</td><td>Relative importance</td><td>Variable</td><td>Relative importance</td></tr><tr><td>EBIT.TA</td><td>17.33</td><td>CA.TA</td><td>5.05</td></tr><tr><td>L.TD</td><td>13.72</td><td>EBIT.CAP</td><td>3.61</td></tr><tr><td>S.TA</td><td>10.47</td><td>LE</td><td>2.88</td></tr><tr><td>LnTA</td><td>9.02</td><td>S.CAP</td><td>2.17</td></tr><tr><td>C.CL</td><td>8.66</td><td>WC.TA</td><td>2.17</td></tr><tr><td>NACE1</td><td>8.30</td><td>CA.CL</td><td>1.80</td></tr><tr><td>CF.TD</td><td>6.50</td><td>S.CA</td><td>1.80</td></tr><tr><td>C.TA</td><td>5.05</td><td>WC.S</td><td>1.44</td></tr></table>

The most important ratios in the analysis are the economic profitability, level of indebtedness, efficiency, and the proxy variable for the firm size. The first of these ratios shows the corporation's success in the application of assets, measuring them by means of the weight of generated earnings before interest and taxes on this accounting magnitude. The most efficient firms in this aspect will undoubtedly have a greater likelihood of being classified as healthy. The variables in the positions from second to fourth in this ranking appeared also in the sensitive analysis of the neural network, although they are placed in different order.

In the AdaBoost literature, the concept of margin [21] is important. The margin for an object is intuitively related to the certainty of its classification and is calculated as the difference between the support of the correct class and the maximum support of an incorrect class. For q classes, the margin of an example x is calculated using the degree of support of the different classes $\mu _ { j }$ $( x ) , j { = } 1 , 2 { , } { \ldots } q$ as

$$
m (x) = \mu_ {k} (x) - \max _ {j \neq k} \mu_ {j} (x).\tag{5}
$$

where k is the correct class of x and $\textstyle \sum _ { j = 1 } ^ { q } \mu _ { j } ( x ) = 1$

All the wrongly classified examples will therefore have negative margins and those correctly classified will have positive margins. Correctly classified observations with a high degree of confidence will have margins which are close to one whereas examples with an uncertain classification will have small margins and margins close to zero. Since a small margin is an instability symptom in the assigned class, the same example could be assigned to different classes by similar classifiers. For visualization purposes, Kuncheva [28] uses margin distribution graphs showing the cumulative distribution of the margins for a given data set. The x-axis is the margin (m) and the y-axis is the number of points where the margin is less than or equal to m. If all the training points have been correctly classified, there will only be positive margins. Ideally, all points should be classified correctly so that all the margins are positive. If all the points have been correctly classified and with the maximum possible certainty, the cumulative graph will be a single vertical line at $m = 1$ . Fig. 2 shows the margin cumulative distribution for the AdaBoost classifier developed in this application. In this case, 7.63% of the negative margins match the training error. It should also be pointed out that about 25% of the observations have margins which are close to the unit (which shows those firms that have been classified with a probability equal to one).

![](/api/attachments/8GMJXHXE/fulltext/images/c3c390a9e6d6c7f608f17fbca09bcd6e457dbb0776a545fbdeea382e91ba1e52.jpg)  
Fig. 2. Margin cumulative distribution graph.

## 6. Conclusions

In this study, two classification methods have been compared, showing the improvement in accuracy that AdaBoost achieves against the Neural Network. As has been seen, AdaBoost is based on building consecutive classifiers on modified versions of the training set which are generated according to the error rate of the previous classifier, while focusing on the hardest examples of the training set. In the practical application, the legal concept of corporate failure have been used which includes bankruptcy and temporary receivership firms. The application has worked as usual with two classes, where healthy companies have been distinguished from failed ones, with the AdaBoost method achieving a test error of 8.898%. Failed firms are therefore properly differentiated from healthy companies. This result means that the AdaBoost strategy for combining single trees achieves a reduction of 30% in the test error compared with the individual neural network.

Moreover, it has been confirmed that the AdaBoost ensemble of trees outperforms Neural Networks both in the cross-validation and test set estimation of the classification error, with the empirical comparison therefore, demonstrating the superiority of simple trees ensembles over individual neural networks.

Since the pioneering works of Beaver [9] and Altman [2], many studies have been developed to predict corporate failure using accounting-based variables, and it does seem that there might be other quantitative and qualitative variables that can help prediction. In this research, the size of the firm, the activity sector and the legal structure have proved useful and the joint relative importance of these is 20.2%.

The most outstanding ratios for AdaBoost are the economic profitability, level of indebtedness, efficiency, and the proxy variable for the firm size, and these results are in line with previous studies of corporate failure.

This research has not addressed many important tasks such as the effect of the interdependence of combined classifiers on joint accuracy or the behaviour of combination methods in the presence of noisy data. Our immediate task is the use of neural networks as basic classifiers for AdaBoost. Consequently, these offer future lines of research.

## References

[1] E. Alfaro, M. Gámez, N. García, Adabag: implements AdaBoost. M1 and bagging. R package version 1.0, http://www.R-project. org 2006.

[2] E.I. Altman, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, Journal of Finance 23 (4) (1968) 589–609.

[3] E.I. Altman, G. Marco, F. Varetto, Corporate distress diagnosis: comparison using linear discriminant analysis and neural networks (the Italian experience), Journal of Banking and Finance 18 (1994) 505–529.

[4] A.F. Atiya, Bankruptcy prediction for credit risk using neural networks: a survey and new results, IEEE Transaction on Neural Networks 12 (4) (2001) 929–935.

[5] R.E. Banfield, L.O. Hall, K.W. Bowyer, D. Bhadoria, W.P. Kegelmeyer, S. Eschrich, A comparison of ensemble creation techniques, in: F. Roli, J. Kittler, T. Windeatt (Eds.), Multiple Classifier Systems, Vol. 3077 of Lecture Notes in Computer Science, Springer, Cagliari, 2004, pp. 223–232.

[6] J. Baek, S. Cho, Bankruptcy prediction for credit risk using an auto associative neural network in Korean firms, Proceeding of the International Conference on Computational Intelligence for Financial Engineering, IEEE Press, Hong Kong, 2003, pp. 25–29.

[7] R. Barniv, A. Anuragh, R. Leach, Predicting the out come following bankruptcy filing: a three state classification using NN, International Journal of Intelligence Systems in Accounting, Finance and Management 6 (1997) 177–194.

[8] E. Bauer, R. Kohavi, An empirical comparison of voting classification algorithm: bagging, boosting and variants, Machine Learning 36 (1999) 105–142.

[9] W.H. Beaver, Financial ratios as predictors of failure, Empirical Research in Accounting. Selected Studies. Supplement to Vol. 4 of Journal of Accounting Research, Blackwell Publishing, 1966, pp. 71–111.

[10] T.B. Bell, Neural nets or the logit model? A comparison of each model's ability to predict commercial bank failures, In International Journal of Intelligence Systems in Accounting, Finance and Management 6 (1997) 249–264.

[11] C.M. Bishop, Neural networks for pattern recognition, Clarendon Press, Oxford, 1995.

[12] L. Breiman, Bagging predictors, Machine Learning 24 (2) (1996) 123–140.

[13] L. Breiman, Arcing classifiers, The Annals of Statistics 26 (3) (1998) 801–849.

[14] L. Breiman, J.H. Friedman, R. Olshen, C.J. Stone, Classification and regression trees, Wadsworth International Group, Belmont, 1984.

[15] K. Chang Lee, I. Han, Y. Kwon, Hybrid neural network models for bankruptcy predictions, Decision Support Systems 18 (1) (1996) 63–72.

[16] C. Charalambous, A. Charitou, F. Kaorou, Comparative analysis of artificial neural network models: application in bankruptcy prediction, Annals of Operation Research 99 (4) (2000) 403–425.

[17] T.G. Dietterich, Ensemble methods in machine learning, in: J. Kittler, F. Roli (Eds.), Multiple Classifier Systems, Vol. 1857 of Lecture Notes in Computer Science, Springer, Cagliari, 2000, pp. 1–15.

[18] D. Fletcher, E. Goss, Application forecasting with neural networks. An application using bankruptcy data, Information and Management 24 (1993) 159–167.

[19] Y. Freund, R.E. Schapire, Experiments with a new boosting algorithm, Proc. 13th International Conference on Machine Learning, Morgan Kaufmann, San Francisco, 1996, pp. 148–156.

[20] Y. Freund, R.E. Schapire, A decision-theoretic generalization of on-line learning and an application to boosting, Journal of Computer and System Sciences 55 (1) (1997) 119–139.

[21] Y. Freund, R.E. Schapire, P. Bartlett, W.S. Lee, Boosting the margin: a new explanation for the effectiveness of voting methods, The Annals of Statistics 26 (5) (1998) 1651–1686.

[22] J. Friedman, T. Hastie, R. Tibshirani, Additive logistic regression: a statistical view of boosting, The Annals of Statistics 38 (2) (2000) 391–393.

[23] H. Frydman, E. Altman, D. Kao, Introducing recursive partitioning for financial classification: the case of financial distress, Journal of Finance (1985) 269–291.

[24] D.J. Hand, Discrimination and classification, John Wiley, New Jersey, 1981.

[25] S. Haykin, Neural networks. A comprehensive foundation, Prentice Hall, New York, 1994

[26] S. Kaski, J. Sinkkonen, J. Peltonen, Bankruptcy analysis with self-organizing maps in learning metrics, IEEE Transaction on Neural Networks 12 (4) (2001).

[27] K. Kiviluoto, Predicting bankruptcies with self organizing maps, Neurocomputing 21 (1998) 191–201.

[28] L.I. Kuncheva, Combining pattern classifiers. Methods and algorithms, Wiley, New Jersey, 2004.

[29] R.C. Lacher, P.K. Coats, S.C. Sharma, L.F. Fantc, A neural network for classifying the financial health of a firm, European Journal of Operational Research 85 (1995) 53–65.

[30] T. Laitinen, M. Kankaanpaa, Comparative analysis of failure prediction methods: the Finish case, European Accounting Review 8 (1) (1999) 67–92.

[31] M. Lam, Neural network techniques for financial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (2004) 567–581.

[32] K.C. Lee, I. Han, Y. Kwon, Hybrid neural network models for bankruptcy predictions, Decision Support Systems 18 (1996) 63–72.

[33] K. Lee, D. Booth, P. Alam, A comparison of supervised and unsupervised neural networks in predicting bankruptcy of Korean firms, Expert Systems with Applications 29 (2005) 1–16.

[34] M. Leshno, Y. Spector, Neural network prediction analysis: the bankruptcy case, Neurocomputing 10 (1996) 125–147.

[35] M. Odom, R. Sharda, A neural network for bankruptcy prediction, Proceedings of the International Joint Conference on Neural Networks, IEEE Press, San Diego, CA, 1990.

[36] J.A. Olshon, Financial ratios and the probabilistic prediction of bankruptcy, Journal of Accounting Research 18 (1) (1980) 5–12.

[37] D. Opitz, R. Maclin, Popular ensemble methods: an empirical study, Journal of Artificial Intelligence Research 11 (1999) 169–198.

[38] M. Pérez, Artificial neural networks and bankruptcy forecasting: a state of the art, Neural Computing & Applications 15 (2) (2006) 154–163.

[39] S. Piramuthu, H. Ragavan, M.J. Shaw, Using feature construction to improve the performance of the neural networks, Management Sciences 44 (3) (1998)

[40] J.R. Quinlan, Induction on decision trees, Mach. Learn. 1 (1986) 81–106.

[41] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Francisco, 1993.

[42] R Development Core Team, R: a language and environment for statistical computing. R Foundation for Statistical Computing. Viena, http://www.R-project.org 2004.

[43] E. Rahimian, S. Singh, T. Thammachote, R. Virmani, Bankruptcy prediction by neural networks, in: R.R. Trippi, E. Turban (Eds.), Neural Networks in Finance and Investing, Irwin Professional Pub., Burr Ridge, 1996.

[44] P. Ravi Kumar, V. Ravi, Bankruptcy prediction in banks and firms via statistical and intelligent techniques — a review, European Journal of Operational Research 180 (2007) 1–28.

[45] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representation by error propagation, in: D.E. Rumelhart, J.L. McClelland (Eds.), Parallel Distributed Processing: Explorations in the Microstructure of Cognition, vol. 1, The MIT Press, Cambridge, 1986, pp. 318–362.

[46] L. Salchenberger, C. Mine, N. Lash, Neural networks: a tool for predicting thrift failures, Decision Sciences 23 (1992) 899–916.

[47] C. Serrano-Cinca, Self organizing neural networks for financial diagnosis, Decision Support Systems 17 (3) (1996) 227–238.

[48] C. Serrano-Cinca, Feedforward neural networks in the classification of financial information, European Journal of Finance 3 (3) (1997) 183–202.

[49] R. Sharda, R.L. Wilson, Performance comparison issues in neural network experiments for classification problems, Proceedings of the 26th Hawaii International Conference on Systems Sciences, IEEE Press, Hawaii, 1993.

[50] P. Swicegood, J.A. Clark, Off-site monitoring for predicting bank under performance: a comparison of neural networks, discriminant analysis and professional human judgement, International Journal in Accounting, Finance and Management 10 (2001) 169–186.

[51] K.Y. Tam, Neural networks models and the prediction of bank bankruptcy, Omega 19 (5) (1991) 429–445.

[52] K.Y. Tam, M. Kiang, Predicting bank failures: a neural network approach, Decision Sciences 23 (1992) 926–947.

[53] J. Tsukuda, S.I. Baba, Predicting Japanese corporate bankruptcy in terms of finance data using neural network, Computers and Industrial Engineering 27 (1-4) (1994) 445–448.

[54] G.I. White, A.C. Sondhi, D. Fried, The analysis and use of financial statements, John Wiley & Sons, Inc., 2003.

[55] R.L. Wilson, R. Sharda, Bankruptcy prediction using neural network, Decision Support Systems 11 (1994) 545–557.

[56] Z.R. Yang, M.B. Platt, H.D. Platt, Probability neural networks in bankruptcy prediction, Journal of Business Research 44 (1999) 67–74.

[57] G. Zhang, M.Y. Hu, B.E. Patuwo, D.C. Indro, Artificial neural networks and bankruptcy prediction general framework and cross-validated analysis, European Journal of Operational Research 116 (1999) 16–32.

[58] M. Zmijewski, Methodological issues related to the estimation of financial distress prediction models, Journal of Accounting Research 22 (1984) 59–86.

![](/api/attachments/8GMJXHXE/fulltext/images/62e07eca8fa12f792aa8bbb2630fb3ea6fa3554afd879c2e3ee71b19d6cfeb65.jpg)

<sup>Esteban Alfaro Cortés</sup> teaches Statistics at the Faculty of Economic and Business Sciences in the University of Castilla-La Mancha. He completed his degree in Business in 1999 and got his Ph. D. in Economics in 2005, both in the University of Castilla-La Mancha. His thesis dealt with the application of ensemble classifiers to corporate failure prediction. Current research deals with spatial statistics and the combination of classifiers (decision trees and neural nets) for solving heated topics in the Economics.

![](/api/attachments/8GMJXHXE/fulltext/images/863d0770d4affc186077113782b594a749345afb98d673e13e2d75e5af2d2c8b.jpg)

<sup>Noelia García Rubio</sup> teaches Statistics at the Faculty of Economic and Business Sciences in the University of Castilla-La Mancha. She got her degree in Economics at the University of Madrid (UAM) in 1996 and completed her Ph. D. in Economics in 2004 on the construction of an intelligent and automated system for property valuation through the combination of neural nets and a geographic information system (GIS). Current research deals with

spatial statistics and the combination of classifiers (decision trees and neural nets) for solving heated topics in the Economics.

![](/api/attachments/8GMJXHXE/fulltext/images/1d2feb901a98d13a25ff4dd9e929a24914680e37b0fb7ef68895ff6bd004970c.jpg)

Matías Gámez Martínez <sub>teaches Statistics</sub> at the Faculty of Economic and Business Sciences in the University of Castilla-La Mancha. He got his degree in Mathematics at the University of Granada in 1991 and finished a Master in Applied Statistics a year after. He completed his Ph. D. in Economics at the University of Castilla-La Mancha in 1998 on the application of geo-statistical techniques to the estimation of housing prices.

Current research deals with spatial statistics and the combination of classifiers (decision trees and neural nets) for solving heated topics in the Economics.

![](/api/attachments/8GMJXHXE/fulltext/images/f2266b6358384f7c2cada125e29b038b2df0a5aa37bc3b4aeb05a0f6ca49abe5.jpg)

<sup>D. Elizondo</sup> received the B.Sc. degree in computer science from Knox College, Galesbourg, IL, in 1986, the M.Sc. degree in artificial intelligence from the University of Georgia, Athens, in 1992, and the Ph.D. degree in computer science from the Universite Louis Pasteur, Strasbourg, France, and the Institut Dalle Molle d'Intelligence Artificielle Perceptive (IDIAP), Martigny, Switzerland, in 1996. He is currently a Senior Lecturer at the Centre for

Computational Intelligence of the School of Computing at De Montfort University, Leicester, U.K. His research interests include applied neural network research, computational geometry approaches towards neural networks, and knowledge extraction from neural networks.
