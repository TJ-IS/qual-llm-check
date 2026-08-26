---
otero_id: 11846
otero_key: "QTDE6XX2"
title: "Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model"
authors: "Shuai Ding; Yeqing Li; Desheng Wu; Youtao Zhang; Shanlin Yang"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.12.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Time-aware cloud service recommendation using similarityenhanced collaborative filtering and ARIMA model

![](/api/attachments/QTDE6XX2/fulltext/images/50ab967a43d4af836a5456b0b9caaf9f473977494c366a733215678331e1b5ce.jpg)

Shuai Ding, Yeqing Li, Desheng Wu, Youtao Zhang, Shanlin Yang

<table><tr><td>PII:</td><td>S0167-9236(17)30241-5</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2017.12.012</td></tr><tr><td>Reference:</td><td>DECSUP 12913</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>18 March 2017</td></tr><tr><td>Revised date:</td><td>8 December 2017</td></tr><tr><td>Accepted date:</td><td>25 December 2017</td></tr></table>

Please cite this article as: Shuai Ding, Yeqing Li, Desheng Wu, Youtao Zhang, Shanlin Yang , Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), https://doi.org 10.1016/j.dss.2017.12.012

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Time-aware Cloud Service Recommendation Using Similarity-enhanced Collaborative

Filtering and ARIMA Model

Shuai Ding<sup>a,b</sup>, Yeqing Li<sup>a,b</sup>, Desehng Wu <sup>c,</sup>,Youtao Zhang<sup>d</sup>, Shanlin Yang<sup>a,b</sup>

<sup>a</sup> School of Management, Hefei University of Technology, Anhui, Hefei 23009, China

<sup>b</sup> Key Laboratory of Process Optimization and Intelligent Decision-Making (Ministry of

Education), Hefei University of Technology, Anhui, Hefei 23009, China

<sup>c</sup> Economics and Management School, University of Chinese Academy of Sciences, Beijing,

100190, China and Stockholm University

<sup>d</sup> Department of Computer Science, University of Pittsburgh, Pittsburgh 15213, PA, USA

Corresponding author:

Both Desheng Wu and Shanlin Yang are Corresponding authors.

Desheng Wu, Email: dash@risklab.ca, dash.wu@gmail.com

Time-aware Cloud Service Recommendation Using Similarity-enhanced Collaborative Filtering and ARIMA Model

## Abstract

The quality of service (QoS) of cloud services change frequently over time. Existing service recommendation approaches either ignore this property or address it inadequately, leading to ineffective service recommendation. In this paper, we propose a time-aware service recommendation (taSR) approach to address this issue. We first develop a novel similarityenhanced collaborative filtering (CF) approach to capture the time feature of user similarity and address the data sparsity in the existing PITs (point in time). We then apply model (ARIMA) to predict the QoS values in the future PIT under QoS instantaneity. We evaluate the proposed approach and compare it to the state-of-the-art. Our experimental results show that taSR achieves significant performance improvements over existing approaches.

Keywords: cloud service, time-aware recommendation, QoS, similarity-enhanced CF, ARIMA

## 1. Introduction

With the rapid development of cloud computing technology in the past decade, cloud services have prevailed in various application domains. While there are a large number of cloud services in commercial service markets, e.g., Apple APP store and Tencent application treasure, many of these services share similar or even overlapped functionalities. Recent studies have shown that, for either individual users or small and medium enterprise (SME) users, adopting appropriate cloud services can significantly reduce IT cost and increase operation efficiency, which has made cloud service recommendation and selection one of the most important tasks in cloud computing.

Given the difficulty in choosing appropriate services from a large set of services candidates that share same or similar functionalities, cloud users depend increasingly on recommendations from the cloud service vendors. In addition to the functionality information of cloud services, the cloud service vendors may collect non-functional information, such as response time, throughput, cost [1], referred to as QoS (quality of service) indicators, to better characterize the services. QoS-based service recommendation systems, e.g., kernel-based quantile estimator [2], clustering algorithm [3], and deviation-based neighborhood model [4], achieved better recommendation over the baseline that recommends services only using the functionality information.

However, recent studies revealed that QoS indicators exhibit strong instantaneity in the cloud computing environment [18], e.g., the response time of a service depends on the real significantly from those in other recommendation systems, e.g., E-commence recommendation focuses on user-generated comments, blogs and discussion posts that remain stable for hours or even weeks. Recent advances in cloud service recommendation started to adopt time-aware approaches to address QoS instantaneity. Such as [18], which applies linear combination to fit the influence of time in QoS prediction. In a word, the CF-model based approaches [5] utilize attenuation function to solve the dynamic of user similarity caused by QoS changes, and the ARIMA-based approaches [17] captured the instantaneity in timeaware long-term QoS prediction. However, CF-based models are not effective in predicting the real world.

In this paper, we propose a novel time-aware cloud service recommendation approach (taSR) for cloud service vendors. By better exploration of QoS instantaneity, the service vendors can recommend services that match users’ demands better, which effectively addresses the limitations in existing methods. The followings summarize our contributions.

(1) TaSR, by combining CF model and ARIMA model, exploits the advantages of both models. TaSR adopts a CF method to replenish the missing QoS values such that the data series are ready for constructing effective ARIMA model. It then exploits ARIMA model to precisely capture the dynamics of QoS values and predict QoS values at future PITs (point in time). TaSR formulates the service recommendation as multi-criterion decision-making (MCDM) problem, which normalizes and weights in multiple QoS indicators, for better service recommendation.

(2) TaSR, by integrating user global similarity and user invocation similarity, improves the CF method for time-aware user similarity estimation. The proposed similarity-enhanced CF approach can comprehensively capture the dynamics of user similarity and accurately predict the missing QoS values at either a past PIT and the current PIT.

(3) We evaluate the proposed taSR approach and compare it to the state-of-the-art. The experimental results show that taSR achieves significant improvements over CF-based approaches and ARIMA-based approaches in various settings.

For the rest of the paper, Section 2 reviews the related background. Section 3 presents an overview of the proposed taSR approach. We elaborate the time-aware similarity estimation and the prediction model in Section 4 and Section 5, respectively. Section 6 discusses the experiments and analyzes the results. We summarize the paper in Section 7.

## 2. Literature review

In the last decade, QoS analysis based approaches have demonstrated their effectiveness in cloud service recommendation. Most cloud service recommendation systems adopt CF (collaborative filtering) based approaches, which can be divided into neighbor-based and model-based approaches [7]. The neighbor-based approaches may be further categorized into three kinds based on the type of neighbors: user-similarity based [8][9], item-similarity based [10][11], and hybrid-similarity based [12][13]. The first two predict the QoS values according to the values of their similar users and services, respectively, for improved prediction accuracy, and the last one integrates user similarity and service similarity in estimation. Meanwhile, model-based approaches have been used in QoS prediction. For examples, Silic et al. [14] presented CLUS to divide users/services into different groups based on the k-means algorithm. Yu et al. [15] applied trace norm regularized matrix factorization to predict the reliability of web services.

These traditional schemes adopt static prediction model and thus show good performance only for a specified PIT (point in time). Since the QoS values of cloud services change with different network connection and workload in different invocation time, it is necessary to take time into consideration in the estimation of user/service similarity. For example, two services that show high similarity one month ago may not be treated to be similar as the cloud hardware may have been updated over the time. Some CF-based approaches have proposed time-aware user similarity estimation to capture QoS instantaneity Qi et al. [16] weighted the similarity according to the time span between the invocation time with an exponential decay function. Hu et al. [5] designed an exponential decay function to weight the similarity but according to the time span between invocation time to current.

However, very few CF-based approaches have the capacity to precisely characterize the temporal dynamics of QoS [17]. Currently, there are models proposed to find the correlation between different invocations. Wang et al. [18] predicted the current QoS by the linear combination of similar sequences and estimated the linear combination coefficients by Lasso. Ye et al. [6] proposed to integrate ARIMA model and Holt-Winters model for better longterm QoS performance. Chu et al. [19] proposed a time-aware Bayesian network to discover the time dependent quality of service relationships structure. Geebelen et al. [5] used kernelbased quantile estimator, a powerful non-linear black-box regressor, with online adaptation of the constant offset to predict future QoS values. Hu et al. [17] took the latest observation as a feedback to revise forecasts to future QoS values for each individual service with Kalman filtering.

In summary, the traditional CF approaches failed to precisely characterize the temporal dynamics of QoS, even though the construction of time-aware models need high quality QoS data. The existing time-aware QoS-based recommendation schemes cannot fully address the instantaneity of QoS values. In this article, we first propose novel similarity-enhanced CF approach to capture the time feature of similarity estimation and replenish the missing QoS value for further prediction. The ARIMA model is then applied to predict the QoS values in the near future for better accuracy. Finally, as a MCDM problem, the different indicators are combined to recommend cloud services.

## 3. taSR: Time-aware Cloud Service Recommendation

Clearly, it is crucial to address the instantaneity of QoS values for better service recommendation. In this paper, we propose a time-aware service recommendation approach that integrates the time-aware similarity-enhanced CF and the ARIMA model. The similarityenhanced CF improves the calculation of user similarity for better QoS data filling, and the ARIMA model predicts the QoS values at a future PIT more accurately with high quality data. The procedure consists of three steps, as shown in Fig. 1.

![](/api/attachments/QTDE6XX2/fulltext/images/ec2d28d5cd1e4ec984e6bef28280d7c11a0ca345b6a828e4749eb6040c9342d7.jpg)  
Fig. 1. The taSR time-aware cloud service recommendation.

In the first step, taSR adopts a novel similarity metric to reconcile dynamic user similarity based on instantaneous QoS values. We use PCC (Pearson correlation coefficient) to calculate the global similarity based on QoS values，and adopt a custom attenuation function to adjust QoS prediction based on the user’s risk preference. We then evaluate the user invocation similarity based on the adoption of edit distance. We integrate the two similarity values in one metric using their geometric mean.

In the second step, taSR employs the similarity estimated in the first step and selects the users that are most similar to the target user to fill missing QoS values in the past and current PITs. Moreover, we adopt the ARIMA model to extend the QoS prediction to include not only the past and current PITs but also a future PIT with faithful description of QoS instantaneity.

The cloud service section is a multi-criterion decision-making (MCDM) problem when adopting different indicators to evaluate QoS performance. In the last step, with the filled user-service matrices, considering the inconsistency of different QoS indicators, we normalize the $\boldsymbol { \mathrm { Q o S } }$ values and weight the indicators to integrate the comprehensive QoS values. We then rank the QoS values and recommend the top-k candidate services.

## 4. Time-aware user similarity estimation

In this section, we elaborate the similarity estimation details in taSR. We discuss the model used in similarity estimation, present our similarity metric, and integrate the similarity estimation with edit distance.

The user-service matrix is a model for modeling the relationship between users and services, which is widely adopted in current cloud service recommendation studies. To model QoS instantaneity, the 2D matrix can be extended with time direction, resulting in time series user-service matrices, as shown in Fig. 2. In the figure, u<sub>i</sub> $( i \in [ 1 , I ] )$ and $s _ { j } ( j \in [ 1 , J ] )$ ) denote different users, and cloud services, respectively. An entry in the matrix $Q _ { i j } ^ { h }$ denotes the observed/predicted QoS value to be used in similarity estimation (e.g., response-time, throughput). $t _ { h } ( \mathrm { h } { = } 1 \dots H , H { + } I )$ denotes different PITs (points in time). t denotes the system start PIT while t<sub>H</sub> and $t _ { H + }$ <sub>1</sub> denote the current PIT, and the next PIT in the future, respectively.

![](/api/attachments/QTDE6XX2/fulltext/images/17046444f08964ace1775081ac6ccd0a80fce7345d5b6ca211967a05f16d96ec.jpg)

![](/api/attachments/QTDE6XX2/fulltext/images/a91a35f975fd9956ffec3dd870a52d1f1f7444288c81b77b6f66bc29c3e9d901.jpg)

(a) The collected raw matrices

(b) The predicted matrix for the future

PIT

Fig. 2. Modeling the user, service, and PIT relationship.

## 4.1. User Global Similarity Estimation

Since user similarity analysis plays the key role in cloud service recommendation, we focus on better user similarity analysis approaches in this section. In particular, we adopt a novel similarity metric to address the dynamic nature of user similarity. Recent studies have revealed that, of all user similarity results at different PITS, those from recent PITs tend to have a larger impact [5].

The basic inter-user similarity is modeled by PCC (Pearson correlation coefficient) using Eq. (1). In the equation, the service set includes all the services with the similar function that the users used before. $Q _ { p j } ^ { h }$ and $Q _ { q j } ^ { h }$ denote the QoS values of service s<sub>j</sub> invoked by users $u _ { p }$ and $u _ { q } ,$ respectively, at PIT t<sub>h</sub>. $\bar { Q } _ { p } ^ { h }$ and $\bar { Q } _ { q } ^ { h }$ denote the average QoS values of all service candidates invoked by u<sub>p</sub> and $u _ { q } .$

$$
\operatorname{Sim} _ {p q} ^ {h} = \frac {\sum_ {j = 1} ^ {J} \left(Q _ {p j} ^ {h} - \overline {{{Q}}} _ {p} ^ {h}\right) \left(Q _ {q j} ^ {h} - \overline {{{Q}}} _ {q} ^ {h}\right)}{\sqrt {\sum_ {j = 1} ^ {J} \left(Q _ {p j} ^ {h} - \overline {{{Q}}} _ {p} ^ {h}\right) ^ {2}} \sqrt {\sum_ {j = 1} ^ {J} \left(Q _ {q j} ^ {h} - \overline {{{Q}}} _ {q} ^ {h}\right) ^ {2}}}\tag{1}
$$

We then model the attenuation of similarity correlation over time. Studies have shown that the risk preference of cloud users greatly affects their behaviors [20]. There are three types of users: risk-averse, risk-neutral and risk-taking users. While risk-averse users pay more attention to the performance of recently invoked services, risk-taking users have less interest in recent PITs. A risk neutral user is often calm to the change of QoS values. Traditional methods, like questionnaire [21], expected-utility mode [22], have been applied to collect the risk preference information. In this paper, we assume cloud service vendors gain users’ risk preference using history invocation information as a feedback.

There exist two main types of attenuation functions, i.e., logistic function and exponential function [23]. A logistic function is an S-curve function while an exponential function is a concave one. To precisely capture the risk preference and the evolution trend of user similarity, we propose a custom attenuation function as shown in Eq. (2).

$$
f (h) = \frac {2}{1 + (h / H) ^ {- \alpha}}\tag{2}
$$

where H denotes the total number of PITs. In this way, we make h/H vary from 0 to 1, and α is a tunable parameter adjusted to indicate the risk preference of service similarity. Fig. 3 plots the function with different α values. From the figure, the correlation of inter-user similarity changes significantly when α falls below and exceeds 1.

![](/api/attachments/QTDE6XX2/fulltext/images/7a3550c934795c81314c172a30dfbcc98cb56b9c92bc26467e091fa0d07a9934.jpg)  
Fig. 3. The similarity attenuation function.

We then estimate the user global similarity at consecutive PITs t<sub>1</sub> .. t<sub>H</sub> using Eq. (3).

$$
\operatorname{Sim} _ {p q} ^ {\text { Global }} = \frac {\sum_ {h = 1} ^ {H} (f (h) * \operatorname{Sim} _ {p q} ^ {h})}{\sum_ {h = 1} ^ {H} f (h)}\tag{3}
$$

The user global similarity proposed in this article is a dynamic metric that is closely coupled with the attenuation function f (h). α is the coefficient of users’ risk preference. A risk-averse user may choose α being smaller than 1, which has slow attenuation rate and reflects the large impact of recent PITs; a risk-taking user may choose α being bigger than 1, which has fast attenuation rate such that the recommendation of cloud services depends less on recent PITs. Meanwhile, a risk neutral user chooses α being 1. We initialize α to 1.0 indicating every user is neutral at the beginning. In addition to recommending top N services under the current α, the vendor may supply additional m services using a smaller α and m services using a large α. m is much smaller than N. We update α dynamically according to the user’s choice. Once a user selects the cloud service recommended by a larger α, we adjust the initial α to a larger one for the next time. Empathy, we adjust α to fit the users’ risk preference.

## 4.2. User Invocation Similarity Estimation Adopting Edit Distance

To improve the accuracy of user similarity estimation, we next exploit users’ service invocation history to enable additional similarity analysis among different users, similar as those in recent studies [12][24][25]. Two users are regarded as similar if they either invoke or do not invoke a service at a given time. In this paper, we convert the service invocation record of each user-service pair to a binary string with the values in the string sorted by their invocation times. Therefore, we quantify the similarity using edit distance (ED), a method

that has been widely adopted to evaluate the similarity of different strings [26][27][28]. Adopting edit distance helps to capture not only the same invocation but also the same uninvocation, i.e., a service is not invocated by either user. The latter is often ignored in existing methods that estimate user invocation similarity [29].

We next elaborate the similarity estimation using invocation experiences of the set of services that the users used before with similar function. When a user u<sub>p</sub> invokes service s<sub>j</sub> at consecutive PITs $t _ { 1 } \dots t _ { H } , \{ Q _ { p j } ^ { h } , h { = } 1 . . H \}$ denotes their raw QoS values. taSR first maps the QoS values into a binary string $B _ { p j } = \{ b _ { p j } ^ { h } , h { = } 1 . . H \}$ , where $b _ { p j } ^ { h } = 1$ if $Q _ { p j } ^ { h } \neq n u l l$ and $b _ { p j } ^ { h } = 0$ otherwise. Then we conduct the $B _ { p j } \lvert + 1$ row and $B _ { q i } \rvert + 1$ column distance matrix $D [ | B _ { p j } | + 1 , |$ $B _ { q j } \left| + 1 \right] = D [ m , n ]$ , where D[m,n] is the $e d i t _ { p q } ^ { j } ( m , n )$ computed by:

$$
\left\{ \begin{array}{l l} e d i t _ {p q} ^ {j} (0, 0) = 0, & m = n = 0 \\ e d i t _ {p q} ^ {j} (m, 0) = m, & m > 0 \text {   and   } n = 0 \\ e d i t _ {p q} ^ {j} (0, n) = n, & m = 0 \text {   and   } n > 0 \\ e d i t _ {p q} ^ {j} (m, n) = \min \left\{ \begin{array}{l l} e d i t _ {p q} ^ {j} (m, n - 1) + 1 \\ e d i t _ {p q} ^ {j} (m - 1, n) + 1 \\ e d i t _ {p q} ^ {j} (m - 1, n - 1) + f _ {p q} ^ {j} (m, n) \end{array} , m > 0 \text {   and   } n > 0 \right. \end{array} \right.\tag{4}
$$

where $f _ { p q } ^ { j } ( m , n ) = 1$ if the (m-1)th value in $B _ { p j }$ is equal to the (n-1)th value in $B _ { q j }$ , and $f _ { p q } ^ { j } ( m , n ) = 0$ otherwise.

Once m=n=H+1, we get the final edit distance between $B _ { p j }$ and $B _ { q j } \mathrm { ~ -- ~ } \ e d \dot { u } t _ { p q } ^ { j } ( H { + } 1 , H { + } 1 )$ Then taSR calculates the invocation similarity between $u _ { p }$ and $u _ { q }$ for service s as follows.

$$
\operatorname{Sim} _ {p q} ^ {j} = 1 - \frac {\operatorname{edit} _ {p q} ^ {j} (H + 1 , H + 1)}{H}\tag{5}
$$

At last, taSR estimates the user invocation similarity by calculating the average similarity for cloud services invocated by user $u _ { p }$ or $u _ { q } ,$ that is, $S i m _ { p q } ^ { E v } = \sum _ { j = 1 } ^ { J } S i m _ { p q } ^ { j } / N _ { p q }$ ,where $N _ { p q }$ is the number of cloud services invocated by user $u _ { p }$ or $u _ { q }$ . Note that if two users have the same

invocation experiences for all candidates, we have $\mathrm { ~ \it S i m } _ { p q } ^ { E x p } = 1$ . For instance, assume two users $u _ { p }$ and $u _ { q }$ invoke service s<sub>j</sub> at four consecutive PITs t<sub>1</sub> <sub>..</sub> t<sub>4</sub>, the collected response-time values (i.e., the QoS values) are {1.57, 2.31, null, null} and {0.98, null, 1.86, null} for two users, respectively. taSR shall transform them to the binary strings as $B _ { p j } = \{ 1 , 1 , 0 , 0 \}$ and $B _ { q j } = \{ 1 , 0 , 1 , 0 \}$

## Table 1

## Table 2

The constructed computation matrix  
The edit distance between $u _ { p }$ and $u _ { q }$

<table><tr><td></td><td> $b_{pj}$ </td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $b_{qj}$ </td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>1</td><td>1</td><td>/</td><td>/</td><td>/</td><td>/</td></tr><tr><td>0</td><td>2</td><td>/</td><td>/</td><td>/</td><td>/</td></tr><tr><td>1</td><td>3</td><td>/</td><td>/</td><td>/</td><td>/</td></tr><tr><td>0</td><td>4</td><td>/</td><td>/</td><td>/</td><td>/</td></tr></table>

<table><tr><td></td><td> $b_{pj}$ </td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $b_{qj}$ </td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>0</td><td>2</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td>1</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td></tr><tr><td>0</td><td>4</td><td>3</td><td>2</td><td>1</td><td>2</td></tr></table>

Table 1 and Table 2 show how to fill in the distance matrix D[5,5]. The values in the first row and the first column are calculated by $e d i t _ { p q } ^ { j } ( m , 0 ) = m$ and $e d i t _ { p q } ^ { j } ( 0 , n ) = n$ respectively, as shown in Table 1. We then fill in other edit distance values in the distance matrix, as shown in Table 2. For example, D[2,2] is estimated as min $\{ 1 + 1 , 1 + 1 , 0 + 0 \} = 0$ where $f _ { p q } ^ { j } ( 2 , 2 ) = 0$ . Finally, the edit distance between $B _ { p j }$ and $B _ { q j }$ is $e d i t _ { p q } ^ { j } ( 5 , 5 ) = 2$

## 4.3. Integrated similarity estimation

From the above discussion, the user global similarity extracts traditional user-service relationship and adopts attenuation function to emphasize the dynamic nature of user similarity; the user invocation similarity extracts the hidden information from invocation history from all PITs. To achieve better similarity estimation, taSR integrates the two similarity values in one time-aware similarity metric using geometric mean.

$$
\operatorname{Sim} _ {p q} = \sqrt {\operatorname{Sim} _ {p q} ^ {\text {Global}} \times \operatorname{Sim} _ {p q} ^ {\text {Exp}}}\tag{6}
$$

Here, $S i m _ { p q }$ is within [0, 1] and a larger value stands for better user similarity.

## 5. Time-aware cloud service recommendation

## 5.1. QoS prediction for a past or the current PIT

Given the time series user-service matrices, we predict their missing QoS values at either a past or the current PIT using our similarity-enhanced CF. To prevent distraction from users with low similarity, we rank the users based on the measure of the similarity to the target user, i.e., using Eq. (6), and pick up the top k users. The missing QoS value $\hat { Q } _ { p j } ^ { h }$ of $\mathrm { s j }$ for $u _ { p }$ at PIT $t _ { h }$ is calculated as follows.

$$
\hat {Q} _ {p j} ^ {h} = \bar {Q} _ {p} ^ {h} + \frac {\sum_ {q = 1} ^ {k} \operatorname{Sim} _ {p q} \times \left(Q _ {q j} ^ {h} - \bar {Q} _ {q} ^ {h}\right)}{\sum_ {q = 1} ^ {k} \operatorname{Sim} _ {p q}}\tag{7}
$$

where $\{ Q _ { q j } ^ { h } , q = 1 . . k \}$ denotes the available QoS values of $u _ { q }$ in service $s _ { j }$ in PIT $t _ { h } . S i m _ { p q }$ denotes the similarity between $u _ { p }$ and $u _ { q , }$ <sub>,</sub> which is computed from Eq. (6); $\bar { Q } _ { p } ^ { h }$ denotes the average QoS value of $u _ { p }$ at PIT $t _ { h } .$ We adopt CF for QoS prediction at either a past or the current PIT because it shows high efficiency and stable performance in information filtering.

## 5.2. QoS Prediction for the future PIT

We next elaborate QoS value prediction for a future PIT. Given all QoS values are missing at a future PIT, we adopt the ARIMA model [30], a model that has been widely applied for time series based future value prediction. Comparing to existing ARIMA-based recommendation approaches [31][32], our proposed taSR approach improves service recommendation through better similarity analysis.

ARIMA model uses Box-Jenkins approach to predict future values, including model identification, parameter estimation, model checking. There are three equations in ARIMA model constructed as Eq.(8). The AR(ε) equation captures QoS value instantaneity, i.e., the QoS values at PIT $t _ { H + 1 }$ are affected by the QoS values at PITs $t _ { H - \varepsilon + 1 }$ .. t<sub>H</sub> and the autoregressive coefficient $\varphi _ { \varepsilon }$ . The MA(ξ) equation means $Q _ { p j } ^ { H + 1 }$ depends on the random errors $r _ { p j } ^ { h } ( h = H \mathbf { \cdot }$ ξ+1 .. H) and the moving average coefficients coefficient $\theta _ { \xi }$ . The ARMA(ε, ξ) equation indicates that $Q _ { p j } ^ { H + 1 }$ is both affected by the QoS values and random errors.

$$
Q _ {p j} ^ {H + 1} = \left\{ \begin{array}{l l} \sum_ {h = H - \varepsilon + 1} ^ {H} \varphi_ {\varepsilon} Q _ {p j} ^ {h} + r _ {p j} ^ {H}, & A R (\varepsilon), \text {ACF decays and PACF cuts off} \\ \sum_ {h = H - \xi + 1} ^ {H} \theta_ {\xi} r _ {p j} ^ {h} + r _ {p j} ^ {H}, & M A (\xi), \text {ACF cuts off and PACF decays} \\ \sum_ {h = H - \varepsilon + 1} ^ {H} \varphi_ {h} Q _ {p j} ^ {h} + \sum_ {h = H - \xi + 1} ^ {H} \theta_ {\xi} r _ {p j} ^ {h} + r _ {p j} ^ {H}, & A R M A (\varepsilon , \xi), \text {ACF and PACF decays} \end{array} \right.\tag{8}
$$

where $Q _ { p j } ^ { H + 1 }$ denotes the predicted QoS value for user $u _ { p }$ on service $s _ { j }$ at the future PIT $t _ { H + 1 }$

To determine the equation to use, we firstly preprocess the QoS values to obtain the stationary data by difference equation; we then adopt Auto-Correlation Function (ACF) and Partial Auto-Correlation Function (PACF) [30] to identify the model according to the to estimate the model coefficient $\varphi _ { \varepsilon }$ and $\theta _ { \xi }$ . Moreover, the Bayesian Information Criterion is utilized to check the model (the parameters ε and ξ). It is an iterative process to find the best model for QoS prediction.

Table 3 ACF and PACF of three models

<table><tr><td></td><td>AR(ε)</td><td>MA(ξ)</td><td>ARMA(ε,ξ)</td></tr><tr><td>ACF</td><td>decay</td><td>cut off in ξ steps</td><td>decay</td></tr><tr><td>PACF</td><td>cut off in ε steps</td><td>decay</td><td>decay</td></tr></table>

Based on Table 3, we use the AR(ε) equation when the PACF curve cuts off in ɛ steps and the ACF curve decays. If the ACF curve cuts off in $\xi$ steps and the PACF curve decays, we adopt the MA(ξ) to predict the QoS values. Once both of the ACF and PACF decay, we utilize the ARMA(ε, ξ) equation in prediction.

## 5.3 Cloud service selection

We recommend cloud services based on the predicted QoS values of the future PIT. Different QoS values may not always be consistent. For example, while we prefer lower response-time values and larger throughput values, one cloud service may have low responsetime but also low throughput values. To achieve effective service recommendation, we next formulate the problem as an MCDM (multi-criteria decision making) [33]. At a given PIT, suppose $Q _ { j } ^ { l } ( l \epsilon [ 1 , L ] , j \epsilon [ 1 , J ] )$ is the QoS value of indicator l of cloud service s<sub>j</sub>. We first use the widely adopted extremum method to normalize QoS values.

$$
\hat {Q} _ {j} ^ {l} = \left\{ \begin{array}{l} \frac {Q _ {j} ^ {l} - \min Q _ {j} ^ {l}}{\max Q _ {j} ^ {l} - \min Q _ {j} ^ {l}}, \text {benefit indicator} \\ \frac {\max Q _ {j} ^ {l} - Q _ {j} ^ {l}}{\max Q _ {j} ^ {l} - \min Q _ {j} ^ {l}}, \text {cost indicator} \end{array} \right.\tag{15}
$$

$Q _ { j } ^ { l }$ $\hat { Q } _ { j } ^ { l }$ is the normalized QoS value of indicator l of s in the future given PIT.

$w _ { l } = S _ { l } / \sum _ { l = 1 } ^ { L } S _ { l } \left[ 3 4 \right]$ , where S<sub>l</sub> is the variance of normalized QoS values $\hat { Q } _ { j } ^ { l }$ of all cloud services in a given PIT. Since users tend to pay more attention to QoS indicators that have large difference [34], this method assigns larger weights to indicators with larger variances. In our future work, we plan to enhance the weight assignment by taking the different preferences from the individual users.

We finally integrate the QoS values of different indicators of cloud service s<sub>j</sub> as $Q _ { j } = \sum _ { l = 1 } ^ { L } w _ { l } Q _ { j } ^ { l }$ , where $Q _ { j }$ is the aggregated QoS value of $s _ { j }$ for the future PIT. We rank the cloud service according to the aggregated QoS value and recommend the top cloud services.

## 6. Experiments

## 6.1. Data description

To study the effectiveness of our proposed taSR approach, we conducted experiments to compare its performance with the state-of-the-art time-aware service recommendation approaches. We adopted the open QoS dataset from WS-DREAM [12], which is the most representative dataset and has been widely adopted in QoS studies [35][36][37][38][39]. The dataset consists of 4532 distributed services collected from 142 distributed computers (i.e., users) located in 57 countries. Each computer invokes services (e.g., apps in Tencent Cloud platform) randomly with a time interval of 15 minutes such that one sequence contains at most 64 PITs, lasting for 16 hours. Two different QoS indicators, i.e., response-time (rt) and throughput (tp), are used to represent the user-side personalized QoS. In particular, the QoS values in this dataset exhibit instantaneity, as shown in [38][39], which makes the dataset an appropriate one in our experiment. We randomly extracted two $1 2 0 ^ { * } 5 0 0 ^ { * }$ 64 time-aware service-user matrices (response-time, throughput) from the original dataset for the experiments. Fig. 4 shows the distribution of response-time and throughput of QoS values in the dataset. In the experiments, t<sub>64</sub> is treated as the future PIT so that all of its QoS values are to be predicted.

![](/api/attachments/QTDE6XX2/fulltext/images/42fde8fad4275f81c74089afd2b7c77002e39f6cb2b5986a21dc8a27b820b135.jpg)

![](/api/attachments/QTDE6XX2/fulltext/images/3f2f8ae3be820b4918225ef21ba40a934a79fcf503c1ff5aa45cc7fedd5bb22b.jpg)  
Fig.4. QoS value distributions.

## 6.2. Evaluation metrics

Matrix density. Given a test dataset, we randomly remove a subset of data values to simulate data sparsity, i.e., some QoS values are missing in the real world. The matrix density is defined as the percentage of available QoS values in the time-aware user-service matrix. As an example, suppose there are 10 users and 5 cloud services in 8 PITs. After removing 241 QoS values, we have the matrix density being 1-241/(10\*5\*8)=0.3975. For the dataset used in the experiments, we have the matrix density being $D { = } 1 { - } N / ( 1 2 0 ^ { * } 5 0 0 ^ { * } 6 3 )$ , where N denotes the total number of missing QoS values. We vary the matrix density D from 0.05 to 0.5 with the step being 0.05.

MAE and RMSE. Given that taSR adopts rating-oriented CF, we used Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess the prediction accuracy and to compare different approaches [40]. MAE and RMSE are defined as:

$$
M A E = \frac {\sum_ {p , j , h} \left| Q _ {p j} ^ {h} - Q _ {p j} ^ {h} \right|}{N}\tag{9}
$$

$$
R M S E = \sqrt {\frac {\sum_ {p , j , h} (Q _ {p j} ^ {h} - Q _ {p j} ^ {h}) ^ {2}}{N}}\tag{10}
$$

where $Q _ { p j } ^ { h }$ and ${ Q } _ { p j } ^ { h }$ denote the observed and the predicted QoS values, respectively, for service $s _ { j }$ invoked by user $u _ { p }$ at PIT $t _ { h } .$ N is the total number of addition operations of the numerator, which equals to the total number of missing QoS values that we predicted. Note, MAE and RMSE decrease with increasing accuracy of QoS prediction.

$\mathbf { N D C G } .$ To evaluate the service recommendation, we adopted Normalized Discounted Cumulative Gain (NDCG) to assess the ranking accuracy of the k recommended services, i.e., the top-k candidates. NDCG is a gain-based evaluation metric focusing on the ranking prediction performance [41]. It calculates the performance according to the order of corresponding QoS values but not the values themselves. While throughput is a benefit-based QoS indicator, response-time is a cost-based QoS indicator. Therefore, we first normalized them to benefit indicators to obtain the rank of each QoS value. $\mathrm { N D C G }$ is defined as follows.

$$
N D C G _ {k} = \frac {D C G _ {k}}{I D C G _ {k}},\tag{11}
$$

where $\mathrm { D C G } _ { k }$ and IDCG<sub>k</sub> denote the discounted cumulative gain on top-k ranked services according to the generated recommendation list and the ideal ranking, respectively. $\mathrm { D C G } _ { k }$ is computed as follows.

$$
D C G _ {k} = r e l _ {1} + \sum_ {k} \frac {r e l _ {k}}{\log_ {2} k},\tag{12}
$$

where $r e l _ { k }$ denotes the real QoS values on service $s _ { k }$ at position k in the predicted ranking. If the generated recommendation is close to the ideal QoS ranking, DCG<sub>k</sub> approximates $\mathrm { I D C G } _ { k }$ such that $\mathrm { N D C G }$ is close to 1. That is, the closer the value is to 1, the better performance the service recommendation approach has.

## 6.3. Results

In this section, we compared our proposed taSR approach with traditional rating-oriented CF-based approaches and a state-of-the-art time-ware ARIMA-based Kalman approach [17]. In these experiments, we set the parameter α to 1 for constructing the similarity attenuation function in Eq. (2); we select the top-10 similar neighbors for predicting missing QoS values.

## 6.3.1. Comparison with the rating-oriented approaches

We first compared taSR with three conventional rating-oriented CF-based approaches that are widely applied in recommendation --- user-based CF using PCC (UPCC) [42], item-based CF using PCC (IPCC) [43] and WSRec [12]. UPCC is a method that adopts user-based PCC adopts item-based PCC. WSRec integrates UPCC and IPCC to predict the missing values. WSRec is often used as a baseline for performance comparison [17][18]. AVG is an approach that fills the user-service matrix with the average of the observed QoS values in the last 3 PITs [18]. In the experiments, we first filled in the 63 PITs with four approaches and our similarity-enhanced CF approach, and then predicted the future QoS values in PIT t<sub>64</sub> with the ARIMA model.

![](/api/attachments/QTDE6XX2/fulltext/images/fe81c67fd846634cdd4af395430d9ccf3d794dc5b09d04db3bdc839ca0f075aa.jpg)  
(a)

![](/api/attachments/QTDE6XX2/fulltext/images/e341f0ef08d89df006c4970e2722d1e553809d6d265e8baa12ceb8768cc07b6e.jpg)  
(b)

![](/api/attachments/QTDE6XX2/fulltext/images/829918dc110fc8335767c16c958446dd9dd0e0701d408de62fe9e9e52888d872.jpg)  
(c)

![](/api/attachments/QTDE6XX2/fulltext/images/dd36743eba254dc5b8936b56c86f3fd4eb00ca6e97993df311455d21992ddc36.jpg)  
(d)  
Fig. 5. Comparing MAE and RMSE from different approaches.

Fig. 5 summarizes the experimental results from different approaches under different matrix density settings. Figs. 5(a) and 5(b) present the comparison on response-time matrices while Figs. 5(c) and 5(d) present the comparison on throughput matrices. As shown in the figure, MAE and RMSE results decrease when the matrix density varies from 0.05 to 0.5. This is because dense matrices contain more useful information than sparse matrices. From the figure, we found that taSR outperforms all four other approaches on both response-time and throughput results, which demonstrates that, by better capturing the dynamic user similarity, we fill in the missing QoS values of the first 63 PITs more accurately. This leads to the better performance when adopting the ARIMA model in recommendation. Except for the value of RMSE in response-time, AVG and taSR generate better prediction than UPCC, IPCC approaches, indicating that time-aware approaches achieve better accuracy. Moreover, taSR outperforms AVG for the comprehensive consideration of the instantaneity.

To assess the accuracy of the service recommendation, we compared different recommendation approaches using the metrics $\mathrm { N D C G } _ { 1 0 } ,$ NDCG<sub>30</sub> and NDCG<sub>50</sub>. Fig.6 summarizes the ranking results based response-time and throughput, respectively. In general, the results from taSR are closer to 1.0 than those from other approaches. For response-time, the NDCG values increase when the density increases from 0.05 to 0.5, i.e., when there are more data. The NDCG values of response-time improve with the increasing numbers of the ranked cloud services, which indicates the robustness and stability of our approach. For throughput, taSR is clearly superior to other approaches when the density varies from 0.05 to 0.2 while the raw NDCG values remain stable with further increase of density. Both AVG and taSR generate better prediction than UPCC, IPCC and WSRec, indicating that time-aware approaches achieve better accuracy. Moreover, taSR outperforms AVG for the comprehensive consideration of the instantaneity except for $\mathrm { N D C G } _ { 5 0 }$ with 0.45 and 0.5 density points. From the results, we concluded that taSR is effective for both similarity analysis and for the final service recommendation.

![](/api/attachments/QTDE6XX2/fulltext/images/a7622b6cab715284e877986e2ec1d0a12e7e22225fb7c558b7f40a3b6c3192d4.jpg)  
(a)

![](/api/attachments/QTDE6XX2/fulltext/images/2925492eb6ae3a066e5f7d2c85b3cd886344e59390ccef9fc062dac22dbc2dab.jpg)  
(b)

![](/api/attachments/QTDE6XX2/fulltext/images/08654565d0c6c5277c714485866933650a10dc81c0227d3c403edff191760959.jpg)  
(c)

![](/api/attachments/QTDE6XX2/fulltext/images/8da0ef426cf48e69c5661e36b3d3e27addedb2d3f930ed79a803bd067c846e27.jpg)  
(d)

![](/api/attachments/QTDE6XX2/fulltext/images/8fd63677fa645f01916653e8a7ad9013698b694ee17b276b5c576ada361b864e.jpg)  
(e)

![](/api/attachments/QTDE6XX2/fulltext/images/63a2c103932beda79e7acae59c593d0495b1332ca7fe292a4cfffd885be8690a.jpg)  
(f)  
Fig. 6. Comparing $\mathrm { N D C G } _ { 1 0 } ,$ NDCG<sub>30</sub> and $\mathrm { N D C G } _ { 5 0 }$ from different approaches.

## 6.3.2. Comparison with the state-of-the-art time-aware approach

Next, we studied the prediction of QoS values at PIT $t _ { 6 4 } .$ , i.e., for a future PIT, after adopting the ARIMA model. We compared taSR with the Kalman approach [17]. Hu et al. adopted Kalman to predict the QoS value for each of nine real-world web services with the full time-aware QoS sequences [17]. As a recursive approach, Kalman defines a state vector and a process noise vector according to the ARIMA model, and takes the new observation as a feedback. In this paper, we focused on the personalized QoS prediction, and compared the performance for taSR and Kalman. For the data preprocessing, we randomly removed a subset of data in the first 63 PITs to simulate the data sparsity in the real world, and filled in the missing data with traditional UPCC method for Kalman and with our similarity-enhanced CF method for taSR.

![](/api/attachments/QTDE6XX2/fulltext/images/3f533cf15c54982cb7b0eec56c33bcd3a1451f687aa312d89550ffc9d57d55e4.jpg)  
(a)

![](/api/attachments/QTDE6XX2/fulltext/images/c86529c58e7886203540c40d66ace36639e0c659366c408b637395d6c40d9e43.jpg)  
(b)

![](/api/attachments/QTDE6XX2/fulltext/images/4daa842b212d0791b9d8565efb74c9cef6a9b93020c57a766ec4e3ea16476548.jpg)  
(c)

![](/api/attachments/QTDE6XX2/fulltext/images/d87301bdb99edf8205c037fd12ae1d12d5035e2d2099ff4e26b02380b25a5395.jpg)  
(d)  
Fig. 7. Comparing MAE and RMSE from taSR and the Kalman approach.  
Fig. 7 summarizes the MAE and RMSE results from taSR and the Kalman approaches. We used the the same dataset and matrix density. taSR and Kalman both predict the future QoS values in the future $\mathrm { P I T } ( t _ { 6 4 } )$ . From the figure, taSR approach outperforms Kalman approach on both response-time and throughput. This is because the similarity estimation in the Kalman approach only used the QoS values of neighbor users at a specified PIT, even

We then compared the performance of taSR and the Kalman approach in making the optimal service recommendation. Fig. 8 summarizes the $\mathrm { N D C G } _ { 1 0 } ,$ $\mathrm { N D C G } _ { 3 0 }$ and $\mathrm { N D C G } _ { 5 0 }$ results from both approaches. From the figure, taSR is better than Kalman for all matrix densities and different QoS indicators. For response-time, taSR achieves better ranking with more data. For throughput, taSR generates good results, i.e., around 0.9, for $\mathrm { N D C G } _ { 1 0 } .$ $\mathrm { N D C G } _ { 3 0 }$ and $\mathrm { N D C G } _ { 5 0 }$ . tsSR achieves not only better stability but also better accuracy in throughput than those in response-time for the matrix density range that we evaluated.

Also from the figure, the Kalman approach is less sensitive to the matrix density as it uses the state transition matrix to predict the missing QoS value for the future. In the Kalman approach, the state transition matrix is predetermined so that it keeps unchanged across multiple iterations during prediction.

![](/api/attachments/QTDE6XX2/fulltext/images/ea58dd29b605eaea19ebd7ac504a077dce559be703eeb69203b06489da6d0fd8.jpg)  
(a)

![](/api/attachments/QTDE6XX2/fulltext/images/af0cb50b1a2acb68635249c89378afdf4dcbb513566375d54ba709f79b1a88dc.jpg)  
(b)

![](/api/attachments/QTDE6XX2/fulltext/images/b0d21b5712029f7fe09e7f1d4b435315f38c6fc07f9f3a9efa51e426a8d7d784.jpg)  
(c)

![](/api/attachments/QTDE6XX2/fulltext/images/2a38057a03847974aff48723841385b44bce343ff02da3013fd9dad16fdb467f.jpg)  
(d)

![](/api/attachments/QTDE6XX2/fulltext/images/73401a63269883f135b7283aa3170701c71343db6315511c3a730f9c87715688.jpg)

![](/api/attachments/QTDE6XX2/fulltext/images/958179918e925d75a4841dfc402001b081a6c6b5cade9b81ba084062bdc2133b.jpg)

(e)

(f)

Fig. 8. Comparing $\mathrm { N D C G } _ { 1 0 } ,$ $\mathrm { N D C G } _ { 3 0 }$ and $\mathrm { N D C G } _ { 5 0 }$ from taSR and the Kalman approach.

## 6.3.3 Comparison on cloud service selection

When adopting different indicators of QoS to evaluate the performance of cloud service, we formulate the selection as an MCDM problem and compute the aggregated QoS value as elaborated in Section 5.3.3.

Fig.9 compares the accuracy of cloud service selection based on the aggregated QoS values. We found that our approach ranks the cloud service more accurately for all NDCGs. The performance of taSR improves gradually when the density varies from 0.05 to 0.5, i.e., with more data information. When D=0.35, taSR produces the best ranking with the $\mathrm { N D C G } _ { 1 0 } { = } 0 . 8 9 9$ $\mathrm { N D C G } _ { 3 0 } { = } 0 . 9 1 9$ $\mathrm { N D C G } _ { 5 0 } { = } 0 . 9 2 8$ . Based on the same dataset, filling the missing QoS values with separate UPCC in 63 PITs, Kalman is superior to UPCC, because Kalman improves the performance of ARIMA by correcting the prediction with new observation data. Furthermore, AVG produces a prediction rank better than UPCC, IPCC, WSRec and Kalman, as for the time-aware populating of data. Also from the figure, the accuracy of taSR increases with the increase of ranked services, demonstrating the stability and robustness of the proposed approach.

![](/api/attachments/QTDE6XX2/fulltext/images/395118548f32b2470d870fed1f46c4f45b9f6b66411911f82513cd379d094b8a.jpg)  
(a)

![](/api/attachments/QTDE6XX2/fulltext/images/312ca8fe2bf911eab6ee85be00790d0a414d6ebb6d2c566fb45dd32565144717.jpg)

(b)  
![](/api/attachments/QTDE6XX2/fulltext/images/fd080bf76f04213c274253d678b882bb4e1e7e396cf54781a9d0693412dfd36e.jpg)  
(c)  
Fig.9. Comparing $\mathrm { N D C G } _ { 1 0 } ,$ $\mathrm { N D C G } _ { 3 0 }$ and $\mathrm { N D C G } _ { 5 0 }$ on cloud service selection.

## 6.3.4 Impact of k in recommendation

In our taSR approach, we choose top k similar users to the target user to filling the missing values in QoS matrices, which will influence the accuracy of prediction significantly. We tested k=2, 5, 10 and 30 to find the most appreciate k with the best performance. Tables 4, 5 and 6 show the performance of our approach with different k values. In general, our proposed approach achieves better performance with the k=5, except the NDCGs in throughput. TaSR has worse performance when k=2 or k=30. This is because it lacks

sufficient information when k=2; and, when k=30, the aggregate effect of many less-similar users may distract the prediction of the choice of the target user. Therefore, we chose k=5 in the experiments to optimize the performance.

Table 4 summarizes the impact of k in response-time. In all density values, k=5 is clearly superior to others. In general, MAE and RMSE produce better prediction with smaller errors when k=5; $\mathrm { N D C G } _ { 1 0 } ,$ $\mathrm { N D C G } _ { 3 0 }$ and $\mathrm { N D C G } _ { 5 0 }$ perform better with the value closer to 1 when k=5. From the table, the best NDCGs for density $\mathrm { D } { = } 0 . 0 5$ appear when k=10 -- this is because, when density is very low, having more similar users helps to provide more information to improve prediction.

Table 5 summarizes the impact of k of throughput. The prediction of QoS values becomes more accurate when k=5 --- we observe smaller error of MAE and RMSE, except the RMSE in D=0.05. When $k { = } 1 0 ,$ the predicted rank of cloud services matches the real rank better than other k values for all density values we evaluated. Table 6 summarizes the impact of k in MCDM recommendation. We found that, for $\mathrm { N D C G } _ { 1 0 } .$ $\mathrm { N D C G } _ { 3 0 }$ and $\mathrm { N D C G } _ { 5 0 }$ , taSR achieves more precise recommendation when k=5 and the matrix density varies from 0.15 to 0.45. When D=0.05, taSR prefers to choose k=10 to recommend top 10 or 30 cloud services.

Table 4 impact of k in response-time

<table><tr><td rowspan="2">response-time</td><td rowspan="2">k</td><td colspan="5">Matrix Density</td></tr><tr><td>0.05</td><td>0.15</td><td>0.25</td><td>0.35</td><td>0.45</td></tr><tr><td rowspan="4">MAE</td><td>2</td><td>2.673</td><td>2.312</td><td>1.823</td><td>1.680</td><td>1.465</td></tr><tr><td>5</td><td>2.668</td><td>1.858</td><td>1.635</td><td>1.522</td><td>1.448</td></tr><tr><td>10</td><td>2.694</td><td>2.130</td><td>1.787</td><td>1.593</td><td>1.480</td></tr><tr><td>30</td><td>2.693</td><td>2.307</td><td>2.196</td><td>2.030</td><td>1.772</td></tr><tr><td rowspan="4">RMSE</td><td>2</td><td>4.461</td><td>3.953</td><td>3.815</td><td>3.820</td><td>3.788</td></tr><tr><td>5</td><td>4.386</td><td>3.798</td><td>3.728</td><td>3.723</td><td>3.712</td></tr><tr><td>10</td><td>4.407</td><td>3.973</td><td>3.787</td><td>3.703</td><td>3.688</td></tr><tr><td>30</td><td>4.406</td><td>4.097</td><td>4.039</td><td>3.969</td><td>3.849</td></tr><tr><td rowspan="4"> $NDCG_{10}$ </td><td>2</td><td>0.215</td><td>0.375</td><td>0.348</td><td>0.439</td><td>0.465</td></tr><tr><td>5</td><td>0.355</td><td>0.418</td><td>0.438</td><td>0.503</td><td>0.508</td></tr><tr><td>10</td><td>0.373</td><td>0.381</td><td>0.418</td><td>0.447</td><td>0.503</td></tr><tr><td>30</td><td>0.368</td><td>0.417</td><td>0.418</td><td>0.429</td><td>0.469</td></tr><tr><td rowspan="4"> $NDCG_{30}$ </td><td>2</td><td>0.397</td><td>0.423</td><td>0.462</td><td>0.498</td><td>0.524</td></tr><tr><td>5</td><td>0.425</td><td>0.491</td><td>0.519</td><td>0.597</td><td>0.616</td></tr><tr><td>10</td><td>0.440</td><td>0.454</td><td>0.499</td><td>0.537</td><td>0.611</td></tr><tr><td>30</td><td>0.435</td><td>0.487</td><td>0.483</td><td>0.514</td><td>0.542</td></tr><tr><td rowspan="4"> $NDCG_{50}$ </td><td>2</td><td>0.457</td><td>0.483</td><td>0.527</td><td>0.539</td><td>0.586</td></tr><tr><td>5</td><td>0.469</td><td>0.530</td><td>0.565</td><td>0.646</td><td>0.660</td></tr><tr><td>10</td><td>0.482</td><td>0.498</td><td>0.540</td><td>0.584</td><td>0.655</td></tr><tr><td>30</td><td>0.477</td><td>0.490</td><td>0.524</td><td>0.554</td><td>0.604</td></tr></table>

Table 5 impact of k in throughput

<table><tr><td rowspan="2">through -put</td><td rowspan="2">k</td><td colspan="5">Matrix Density</td></tr><tr><td>0.05</td><td>0.15</td><td>0.25</td><td>0.35</td><td>0.45</td></tr><tr><td rowspan="4">MAE</td><td>2</td><td>2.268</td><td>1.867</td><td>1.743</td><td>1.672</td><td>1.406</td></tr><tr><td>5</td><td>2.257</td><td>1.843</td><td>1.589</td><td>1.426</td><td>1.287</td></tr><tr><td>10</td><td>2.264</td><td>1.989</td><td>1.722</td><td>1.544</td><td>1.385</td></tr><tr><td>30</td><td>2.264</td><td>2.056</td><td>1.945</td><td>1.820</td><td>1.632</td></tr><tr><td rowspan="4">RMSE</td><td>2</td><td>4.543</td><td>4.269</td><td>3.819</td><td>3.604</td><td>3.407</td></tr><tr><td>5</td><td>4.510</td><td>3.931</td><td>3.698</td><td>3.452</td><td>3.323</td></tr><tr><td>10</td><td>4.468</td><td>4.214</td><td>3.822</td><td>3.578</td><td>3.433</td></tr><tr><td>30</td><td>4.476</td><td>4.295</td><td>4.117</td><td>4.002</td><td>3.759</td></tr><tr><td rowspan="4"> $NDCG_{10}$ </td><td>2</td><td>0.897</td><td>0.921</td><td>0.901</td><td>0.873</td><td>0.869</td></tr><tr><td>5</td><td>0.918</td><td>0.927</td><td>0.871</td><td>0.882</td><td>0.876</td></tr><tr><td>10</td><td>0.924</td><td>0.944</td><td>0.897</td><td>0.903</td><td>0.916</td></tr><tr><td>30</td><td>0.921</td><td>0.930</td><td>0.890</td><td>0.881</td><td>0.888</td></tr><tr><td rowspan="4"> $NDCG_{30}$ </td><td>2</td><td>0.889</td><td>0.894</td><td>0.843</td><td>0.867</td><td>0.856</td></tr><tr><td>5</td><td>0.910</td><td>0.908</td><td>0.857</td><td>0.870</td><td>0.861</td></tr><tr><td>10</td><td>0.917</td><td>0.927</td><td>0.893</td><td>0.903</td><td>0.909</td></tr><tr><td>30</td><td>0.914</td><td>0.927</td><td>0.884</td><td>0.869</td><td>0.870</td></tr><tr><td rowspan="4"> $NDCG_{50}$ </td><td>2</td><td>0.873</td><td>0.857</td><td>0.845</td><td>0.832</td><td>0.841</td></tr><tr><td>5</td><td>0.889</td><td>0.888</td><td>0.843</td><td>0.856</td><td>0.849</td></tr><tr><td>10</td><td>0.896</td><td>0.906</td><td>0.876</td><td>0.886</td><td>0.863</td></tr><tr><td>30</td><td>0.893</td><td>0.906</td><td>0.870</td><td>0.854</td><td>0.852</td></tr></table>

Table 6 impact of k in cloud service selection

<table><tr><td rowspan="2">selection</td><td rowspan="2">k</td><td colspan="5">Matrix Density</td></tr><tr><td>0.05</td><td>0.15</td><td>0.25</td><td>0.35</td><td>0.45</td></tr><tr><td rowspan="4"> $NDCG_{10}$ </td><td>2</td><td>0.863</td><td>0.873</td><td>0.876</td><td>0.883</td><td>0.890</td></tr><tr><td>5</td><td>0.867</td><td>0.880</td><td>0.889</td><td>0.899</td><td>0.895</td></tr><tr><td>10</td><td>0.868</td><td>0.871</td><td>0.873</td><td>0.887</td><td>0.894</td></tr><tr><td>30</td><td>0.867</td><td>0.871</td><td>0.882</td><td>0.875</td><td>0.889</td></tr><tr><td rowspan="4"> $NDCG_{30}$ </td><td>2</td><td>0.883</td><td>0.892</td><td>0.901</td><td>0.908</td><td>0.910</td></tr><tr><td>5</td><td>0.899</td><td>0.908</td><td>0.914</td><td>0.919</td><td>0.916</td></tr><tr><td>10</td><td>0.900</td><td>0.903</td><td>0.902</td><td>0.913</td><td>0.916</td></tr><tr><td>30</td><td>0.900</td><td>0.902</td><td>0.909</td><td>0.903</td><td>0.906</td></tr><tr><td rowspan="4"> $NDCG_{50}$ </td><td>2</td><td>0.912</td><td>0.916</td><td>0.920</td><td>0.918</td><td>0.921</td></tr><tr><td>5</td><td>0.914</td><td>0.921</td><td>0.925</td><td>0.928</td><td>0.927</td></tr><tr><td>10</td><td>0.914</td><td>0.918</td><td>0.921</td><td>0.924</td><td>0.927</td></tr><tr><td>30</td><td>0.914</td><td>0.917</td><td>0.923</td><td>0.917</td><td>0.924</td></tr></table>

## 8. Conclusion

While service recommendation and selection has become one of the most important tasks in cloud computing, it remains a major challenge to recommend the services that are most appropriate to match users’ computing and service demands. In this paper, we propose taSR, a time-aware service recommendation approach that integrates similarity-enhanced CF based QoS prediction and time series analysis. taSR first enhanced similarity analysis by integrating user global similarity and invocation similarity. In particular, taSR adopts a time aware user similarity to describe the dynamic nature of user similarity. taSR then fills missing QoS values in the past PITs and the current PIT and adopts the ARIMA model to produce better recommendation for the future PIT.

With the fast advances of cloud computing paradigm, there exist a large amount of usergenerated data in the cloud. It has become a major challenge for the research community to effectively exploit such data to improve service recommendation. In this paper, we made the effort to exploit the structured QoS data. In our future work, we will take advantage of unstructured data such as user comments, blogs, and discussion posts and adopt text-mining techniques [44] to further improve service recommendation and selection process.

## Acknowledgements

The work is partially supported by the Ministry of Science and Technology of China under grant 2016YFC0503606, and fully supported by the National Natural Science Foundation of China (Nos. 71571058, 71131002, 71471055, 71501058, and 91546102), and a project funded by the China Postdoctoral Science Foundation grant no. 2015M570535.

## References

[1] ZB Zheng, YL Zhang, MR Lyu, Distributed QoS Evaluation for Real-World Web Services, IEEE International Conference on Web Services. IEEE Computer Society, (2010) 83-90.

[2] D. Geebelen, K, Geebelen, E. Truyen, et al, QoS prediction for web service compositions Information Sciences 268 (1) (2014) 397-424.

[3] K. Su, B. Xiao, B. Liu, et al, TAP: A personalized trust-aware QoS prediction approach for web service recommendation, Knowledge-Based Systems 115 (2017) 55-65.

[4] H. Wu, K. Yue, C.H. Hsu, et al, Deviation-based neighborhood model for context-aware QoS prediction of cloud and IoT services, Future Generation Computer Systems (2016), http://dx.doi.org/10.1016/j.future.2016.10.015.

[5] Y. Hu, Q. Peng, X. Hu, A time-aware and data sparsity tolerant approach for web service recommendation, IEEE International Conference on Web Services 2014, pp. 33-40.

[6] Z Ye, S.K Mistry, A Bouguettaya, et al, Long-term QoS-aware Cloud Service Composition using Multivariate Time Series Analysis, IEEE Transactions on Services Computing 9(3) (2016) 382-393.

[7] C.F. Tsai, C. Hung, Cluster ensembles in collaborative filtering recommendation, Applied Soft Computing 12 (4) (2012) 1417-1425.

[8] Y M Afify, I F Moawad, N L Badr, et al, Enhanced similarity measure for personalized cloud services recommendation, Concurrency & Computation Practice & Experience 29 (2017).

[9] C Yin, J Wang, J H Park, An Improved Recommendation Algorithm for Big Data Cloud Service based on the Trust in Sociology, Neurocomputing (2017).

[10] S Roy, R Bose, D Sarddar, A novel replica placement strategy using binary item-to-item collaborative filtering for efficient voronoi-based cloud-oriented content delivery network, Computer Engineering and Applications. IEEE, (2015) 603-608.

[11] M. Deshpande, G. Karypis, Item-based top-n recommendation algorithms, ACM

[12] Z.B. Zheng, H. Ma, M.R. Lyu, et al, QoS-aware web service recommendation by collaborative filtering, IEEE Transactions on Services Computing 4 (2) (2011) 140–152

[13] Y. Hu, Q. Peng, X. Hu, et al, Time aware and data sparsity tolerant web service recommendation based on improved collaborative filtering, IEEE Transactions on Services Computing 8 (5) (2015) 782-794.

[14] M. Silic, G. Delac, S. Srbljic, Prediction of atomic web services reliability for qos-aware recommendation, IEEE Transactions on Services Computing 8 (3) (2015) 425-438.

[15] Q Yu, Z Zheng, H Wang, Trace Norm Regularized Matrix Factorization for Service Recommendation, IEEE International Conference on Web Services (2013) 34-41.

[16] L Qi, X Xu, W Dou, et al, Time-Aware IoE Service Recommendation on Sparse Data, Mobile Information Systems (2016).

[17] Y. Hu, Q. Peng, X. Hu, et al, Web service recommendation based on time series forecasting and collaborative filtering, IEEE International Conference on Web Services 2015, pp. 233-240.

[18] X. Wang, J. Zhu, Z. Zheng, et al, A spatial-temporal QoS prediction approach for timeaware web service recommendation, ACM Transactions on the Web 10 (1) (2016)

[19] V W Chu, R K Wong, F Chen, et al, Web Service Recommendations Based on Time Aware Bayesian Networks, IEEE International Congress on Big Data (2015) 359-366.

[20] E Borgonovo, V Cappelli, F Maccheroni, et al, Risk Analysis and Decision Theory: A Bridge, European Journal of Operational Research, 2017.

[21] D Ergu, G Kou, Questionnaire design improvement and missing item scores estimation for rapid and efficient decision making, Annals of Operations Research, 197(1) (2012) 5- 23.

[22] J W Payne, J R Bettman, E J Johnson, Behavioral Decision Research: A Constructive Processing Perspective, Annual Review of Psychology, 43(1) (1992) 87-131.

[23] L Li, L Zheng, F Yang, et al, Modeling and broadening temporal user interest in personalized news recommendation, Expert Systems with Applications, 41(7) (2014) 3168-3177.

[24] Y Pan, D Wu, D L Olson. Online to offline (O2O) service recommendation method based on multi-dimensional similarity measurement, Decision Support Systems, 2017.

[25] S. Jimenez, F.A. Gonzalez, A. Gelbukh, Mathematical properties of Soft Cardinality: Enhancing Jaccard, Dice and cosine similarity measures with element-wise distance, Information Sciences 367 (2016) 373-389.

[26] S. Yabushita, A comparative analysis of the Tanimoto index and graph edit distance for measuring the topological similarity of trees, Applied Mathematics & Computation 259

(C) (2015) 242-250.

[27] J. Abreu, J.R. Rico-Juan, Characterization of contour regularities based on the Levenshtein edit distance, Pattern Recognition Letters 32 (10) (2011) 1421-1427.

[28] S.H. Ryu, B. Benatallah, Experts community memory for entity similarity functions recommendation, Information Sciences 379 (2017) 338-355.

[29] S Ding, C Y Xia, K L Zhou, et al. Decision support for personalized cloud service selection through multi-attribute trustworthiness evaluation, Plos One, 9(6) (2014).

[30] J C Chambers, S K Mullick, D D Smith, How to choose the right forecasting technique, Harvard Business Review, 49(4) (1971) 45-74.

[31] M Godse, U Bellur, R Sonar, Automating QoS Based Service Selection, IEEE International Conference on Web Services. IEEE, (2010) 534-541.

[32] A Amin, A Colman, L Grunske, An Approach to Forecasting QoS Attributes of Web Services Based on ARIMA and GARCH Models, International Conference on Web Services. IEEE, (2012) 74-81.

[33] H Ma, Z Hu, K Li, et al, Toward trustworthy cloud service selection: A time-aware approach using interval neutrosophic set, Journal of Parallel & Distributed Computing, 96 (2016) 75-94.

[34] O Kempthorne, The correlation between relatives on the supposition of mendelian inheritance,. American Journal of Human Genetics, 20(4) (1968) 402.

[35] C Wu, W Qiu, X Wang, et al, Time-Aware and Sparsity-Tolerant QoS Prediction Based on Collaborative Filtering, IEEE International Conference on Web Services. IEEE, (2016)

637-640.

[36] S Chen, Y Fan, W Tan, et al, Time-Aware Collaborative Poisson Factorization for Service Recommendation, IEEE International Conference on Web Services (2016) 196-203

[37] X Wang, J Zhu, Z Zheng, et al, A Spatial-Temporal QoS Prediction Approach for Time aware Web Service Recommendation, Acm Transactions on the Web 10(1) (2016) 7.

[38] Y Zhang, Z Zheng, M R Lyu. Real-Time Performance Prediction for Cloud Components, IEEE International Symposium on Object/component/service-Oriented Real-Time Distributed Computing Workshops, IEEE, (2012) 106-111.

[39] C Yu, L Huang. Time-Aware Collaborative Filtering for QoS-Based Service Recommendation, IEEE International Conference on Web Services. IEEE Computer Society (2014) 265-272.

[40] J. Abreu, J.R. Rico-Juan, Characterization of contour regularities based on the Levenshtein edit distance, Pattern Recognition Letters 32 (10) (2011) 1421-1427.

[41] K Rvelin, Kek, J Inen, Cumulated gain-based evaluation of IR techniques, Acm Transactions on Information Systems 20(4) (2002) 422-446.

[42] J S Breese, D Heckerman, C Kadie. Empirical analysis of predictive algorithms for collaborative filtering, Fourteenth Conference on Uncertainty in Artificial Intelligence, Morgan Kaufmann Publishers Inc (1998) 43-52.

[43] B Sarwar, G Karypis, J Konstan, et al. Item-based collaborative filtering recommendation algorithms, International Conference on World Wide Web. ACM, (2001) 285-295.

[44] L. Flory, K.M. Bryson, M. Thomas, A new web personalization decision-support artifact

for utility-sensitive customer review analysis, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.11.003.

Shuai Ding is an associate professor at School of Management, Hefei University of Technology, China. He got his PhD from Hefei University of Technology. Yeqing Li is a PhD candidate at School of Management, Hefei University of Technology, China.

Desheng Dash Wu is the Distinguished professor at University of Chinese Academy of Sciences, Professor of Stockholm University. His research interests focus on enterprise risk management in operations, performance evaluation in financial industry, and decision sciences. He has published more than 100 papers in refereed journals such as Production and Operations Management, Decision Support Systems, Decision Sciences, Risk Analysis, IEEE Transactions on Systems Man and Cybernetics etc. He is the editor of Springer book series titled “Computational Risk Management”. He has served as associate editors/guest editors in such journals as IEEE Transactions on Systems Man and Cybernetics, Annals of Operations Research, Computers and Operations Research, International Journal of Production Economics, Omega etc. He is a Senor Editor at Decision Support Systems.

Youtao Zhang is an associate professor of Computer Science at the University of Pittsburgh. He received the Ph.D. degree in computer science from the University of Arizona, Tucson, AZ, USA, in 2002, and the B.S. and M.E. degrees from Nanjing University, Nanjing, China, in 1993 and 1996, respectively. Dr. Zhang has authored over 30 journal articles and more than 70 conference presentations in cloud computing, software engineering, memory systems and data intensive computing. Dr. Zhang was the recipient of the U.S. National Science Foundation Career Award in 2005, the Distinguished Paper Award of International Conference on Software Engineering 2003, and the Best Paper Award of International Symposium on Low Power Electronics and Design 2013. He is a member of ACM and IEEE.

## Highlights

We propose to integrate user global similarity and service invocation similarity in a novel time-aware similarity metric to address the instantaneity of QoS values.

We propose to replenish missing QoS values for the past and current PITs through collaborative filtering (CF) and the predict QoS values in the future PIT with ARIMA model.

Our experimental results showed that taSR achieves significantly improvements over existing approaches in various settings.
