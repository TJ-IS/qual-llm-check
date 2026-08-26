---
otero_id: 27625
otero_key: "V6CQTZQD"
title: "Latent Similarity-Enhanced Credit Risk Prediction"
authors: "Hongzhe Zhang; Wei Qian; Xiao Fang"
year: "2026"
journal: "MIS Quarterly"
doi: "10.25300/misq/2025/18080"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# LATENT SIMILARITY-ENHANCED CREDIT RISK PREDICTION<sup>1</sup>

Hongzhe Zhang 1C

Shenzhen Finance Institute, School of Management and Economics, The Chinese University of Hong Kong, Shenzhen, CHINA {zhanghongzhe@cuhk.edu.cn}

Wei Qian Department of Applied Economics and Statistics, University of Delaware, Newark, DE, U.S.A. {weiqian@udel.edu}

Xiao Fang Lerner College of Business and Economics, University of Delaware, Newark, DE, U.S.A. {xfang@udel.edu}

Given the sheer size of the consumer credit market and the huge number of consumer credit users, credit risk prediction, or predicting the probability of consumer credit delinquency (or default), has become a critical problem in the consumer credit industry. Effective credit risk prediction aids financial institutions in granting and managing extensions of credit and can help secure the availability of credit for worthy applicants. While it is desirable to employ both users’ intrinsic characteristics and similarities among them for effective credit risk prediction, existing studies rely solely on similarities derived from their observed characteristics and fail to account for unobserved similarities among them. To address this challenge, we propose a latent similarityenhanced credit risk prediction model, which operationalizes the similarity between a pair of users as a combination of the observed and latent similarities between them. We then present a new design for a new method that estimates the model parameters, learns latent similarities among users, and integrates both observed and latent similarities among users with their intrinsic characteristics for credit risk prediction. We further extend our method to the multiclass and numerical credit risk prediction problems. Extensive empirical evaluations with real-world data demonstrate the superior predictive power of our method over benchmark methods for a broad spectrum of credit risk prediction problems. We also show substantial economic value generated from the superiority of our method through a case study.

Keywords: Credit risk prediction, latent similarity, machine learning, information systems: enabling technologies

## Introduction

Consumer credit refers to an amount of money loaned to a consumer by a financial institution (Hand & Henley, 1997). Over the years, the number of consumer credit users and the size of the consumer credit market have grown tremendously. Taking the U.S. as an example, as of late 2020 (Cox, 2021), its consumer credit market, including credit cards, auto and student loans, and mortgages, had reached \$14.6 trillion, or 69.5% of the GDP, with more than 90% of U.S. adults holding at least one credit card (Horymski, 2025). Given the huge number of consumer credit users and the sheer size of the consumer credit market, credit risk prediction, or predicting the probabilities of consumer credit delinquency (or default), has become a critical problem in the consumer credit industry (Altman et al., 2005; Chatterjee et al., 2007; De Almeida Filho et al., 2010). Credit risk prediction impacts consumers, financial institutions, and even national and international economies. Effective credit risk prediction benefits consumers by helping to facilitate access to credit for worthy applicants, and benefits financial institutions by helping them understand credit risk levels, thereby assisting them in granting and managing extensions of credit and allowing them to reduce default losses. Consequently, while effective credit risk prediction has a positive impact on national and international economies, ineffective credit risk prediction can harm both consumers and financial institutions, in turn damaging economies. For example, the global financial crisis of 2007- 2008 was partially caused by ineffective credit risk management (Thomas et al., 2017), and the estimated cost of the crisis was estimated at between \$6 trillion and \$14 trillion in the U.S. alone (Atkinson et al., 2013).

There are two types of credit risk prediction: application scoring and behavioral scoring. Application scoring targets credit applicants and seeks to predict their individual probability of defaulting on a potential loan (e.g., estimates the likelihood of a loan applicant failing to repay the loan as scheduled). Behavioral scoring, on the other hand, focuses on existing borrowers and attempts to predict and monitor their individual probability of delinquency (e.g., estimates the likelihood of an existing borrower failing to keep up with minimum payments). Both application scoring and behavioral scoring are important to financial institutions. The former assists financial institutions in identifying and filtering out risky credit applicants, whereas the latter helps them mitigate risks associated with existing loans. Moreover, the banking regulations established by the Basel II Accord in 2004 require financial institutions to estimate the risks for all of their existing loan portfolios and set aside regulatory capital accordingly (Thomas et al., 2017). As a result, behavioral scoring has become an essential tool for financial institutions and is the focus of this study.

Both application scoring and behavioral scoring can be formulated as classification problems and solved using classification methods, although training data for behavioral scoring can be made richer with the inclusion of additional information such as borrowers’ repayment and billing data (Thomas, 2000). Logistic regression remains the most commonly used classification method for credit risk prediction (Thomas et al., 2017). Ensemble methods, which combine multiple classifiers through bagging or boosting (Breiman, 1996; Freund & Schapire, 1997), have also been employed for credit risk prediction (West et al., 2005; Paleologo et al., 2010). Among the ensemble methods, XGBoost (or extreme gradient boosting) has gained popularity due to its excellent predictive performance (Chen & Guestrin, 2016). In addition, recent studies have proposed deep learning-based methods, such as recurrent neural network, for credit risk prediction (Babaev et al., 2019).

The methods discussed above employ borrowers’ intrinsic characteristics for credit risk prediction. Prior studies have proposed credit risk prediction methods that utilize similarities among borrowers, in addition to their intrinsic characteristics. For example, Henley and Hand (1996) and Kennedy et al. (2013) identified a borrower’s nearest neighbors based on their similarities with other borrowers, applying the k-nearest neighbor (KNN) classifier to predict their credit risk. Lee et al. (2021) computed similarities among borrowers to construct a borrower network and then employed a graph convolutional network approach (Kipf & Welling, 2017) to extract network features for credit risk prediction. While it is beneficial to consider both similarities among borrowers and their intrinsic characteristics for credit risk prediction, existing studies have relied solely on similarities computed from observed characteristics. For example, Lee et al. (2021) calculated similarities among borrowers based on their observed characteristics, such as credit history and demographic information.

Similarities among borrowers manifest in various aspects beyond those derived from observed characteristics. Therefore, we operationalized the similarity between a pair of borrowers as a combination of two components: observed similarity, computed from their observed intrinsic characteristics, and latent similarity (unobserved similarity), derived from unobserved intrinsic characteristics. Building on this, we proposed a credit risk prediction model that integrates both observed and latent similarities among borrowers, as well as their intrinsic characteristics. We then designed a method to estimate the model parameters, learn latent similarities, and combine observed and latent similarities among borrowers with their intrinsic characteristics for credit risk prediction. Therefore, our method differs from prior credit risk prediction methods focusing solely on observed similarities among borrowers. Moreover, unlike traditional credit risk prediction methods that rely exclusively on borrowers’ intrinsic characteristics, our method leverages the predictive power of a borrower’s similar peers’ credit risks to enhance the prediction of the borrower’s credit risk.

## Related Work

## Fintech and Industry Assignment

In general, credit risk prediction, including application scoring and behavioral scoring, can be modeled as a classification problem, which is then solved using a classification method (Thomas, 2000). Training data for application scoring typically contain loan applicants demographic data (e.g., age), financial data (e.g., income), and credit history data (e.g., credit score). In addition, training data for behavioral scoring also consist of existing borrowers’ repayment and spending data (Thomas, 2000). Once the training data are constructed, common classification methods can be applied to the data for application scoring or behavioral scoring.

The most widely used classification method for credit risk prediction is logistic regression (Thomas et al., 2017), which models a binary dependent variable (e.g., delinquency or not) using a linear combination of independent variables transformed through a sigmoid function. Aside from logistic regression, other classification methods, such as discriminant analysis, naive Bayes, and nearest neighbor, have also been applied to credit risk prediction (Hand, 2001). Fostered by the advancement of artificial intelligence in recent years, credit risk prediction methods have also been developed based on machine learning algorithms, including multilayer perceptron (Malhotra & Malhotra, 2003; Sinha & May, 2004), decision tree (Lessmann et al., 2015), and support vector machine (Yao et al., 2015). Meanwhile, it is well known that combining multiple classifiers through bagging or boosting can outperform a single classifier in predictive performance (Freund & Schapire, 1997; Breiman, 1996). Accordingly, West et al. (2005) investigated different ensemble strategies for the neural network model and found that the generalization ability of the ensembled model is superior to that of the single-best model in credit risk prediction. Paleologo et al. (2010) adopted an ensemble technique, namely sub-bagging, to improve the performance of base classifiers for credit risk prediction. Because of its excellent performance, XGBoost is one of the most commonly used ensemble methods for credit risk prediction (Chen & Guestrin, 2016); the method keeps the scheme of gradient boosting machine (Friedman, 2001) but introduces a more advanced regularization mechanism to avoid model overfitting. In addition, recent studies have employed deep learning methods, such as recurrent neural network and graph convolutional network, for credit risk prediction (Babaev et al., 2019; Lee et al., 2021). Homophily theory suggests that individuals with similar characteristics tend to exhibit similar behaviors (McPherson et al., 2001). Therefore, another way to improve the performance of credit risk prediction is leveraging similarities among users, which we review next.

## Similarity-Based Credit Risk Prediction

An early study employing similarities among borrowers for credit risk prediction is Henley and Hand’s (1996) study, which applied the KNN classifier to predict borrowers’ credit risks. Specifically, a borrower’s nearest neighbors are identified based on similarities among borrowers, which are calculated using their characteristics provided in their loan application forms. Due to its good performance and interpretability, the KNNbased method has been widely adopted in credit risk prediction (Hand & Vinciotti, 2003; Twala, 2010; Kennedy et al., 2013). Another prevalent approach predicts a borrower’s credit risk using the weighted average of other borrowers’ credit risks, where weights are determined based on similarities among borrowers. For instance, Guo et al. (2016) proposed a method that employs kernel weights to predict a loan’s return rate by calculating a weighted average of the return rates of similar loans. Other methods construct a network of borrowers based on similarities among them and then utilize network features for credit risk prediction. For example, Giudici et al. (2019) built a network by treating each borrower as a node and assigning the weight of an edge between two borrowers based on the similarity between them. Here, the similarity is calculated as the reciprocal of the Euclidean distance between the borrowers’ characteristics. Centrality measures are then derived from the network for credit risk prediction. Lee et al. (2021) also constructed a network of borrowers based on similarities among them but employed a graph convolutional network approach (Kipf & Welling, 2017; Xu et al., 2025) to extract network features for credit risk prediction. Additional data have been explored to measure similarities among borrowers. For example, Fernandes and Artes (2016) and Medina-Olivares et al. (2022) computed spatial similarities among borrowers using their geographical data and demonstrated that incorporating these similarities can significantly improve the performance of credit risk prediction.

Our literature review suggests the following research gaps. First, traditional credit risk prediction methods ignore the predictive power of similar borrowers’ repayment behaviors in predicting a borrower’s credit risk. Second, while recent studies highlight the benefits of considering similarities among borrowers for more effective credit risk prediction, they focus only on similarities derived from borrowers’ observed characteristics, failing to account for unobserved similarities among them. To address these gaps, we proposed a latent similarity-enhanced credit risk prediction model, which operationalizes the similarity between a pair of borrowers as a combination of observed and latent similarities between them. The former is measured based on the borrowers’ observed intrinsic characteristics, and the latter is gauged from their unobserved intrinsic characteristics. We then developed a novel method to estimate the model parameters and predict borrowers’ probabilities of delinquency. Therefore, the novelty of our study lies in its novel credit risk prediction model and a new method, which estimates the model parameters and incorporates both observed and latent similarities to predict borrowers’ credit risks.

## Problem Formulation and Model

Let $V = \{ v _ { 1 } , v _ { 2 } , \cdots , v _ { n } \}$ denote a set of ?? users of a credit product (e.g., credit card). They are granted credit by a financial institution and need to periodically pay statement balances or installments. For user $v _ { i } ,$ let $\mathbf { x } _ { i , t } \in \mathbb { R } ^ { p }$ represent ?? observed intrinsic characteristics of the user in billing cycle $t , i = 1 , 2 , \ldots , n .$ A billing cycle is typically a month. Further, we denote the credit delinquency outcome for user $v _ { 1 }$ in billing cycle ?? as a binary variable $y _ { i , t } ,$ where $y _ { i , t } =$ 1 represents delinquency and $y _ { i , t } = 0$ means no delinquency. More specifically, in the credit card example, $\mathbf { x } _ { i , t }$ describes $v _ { i } { ' } s$ information available at the end of billing cycle ?? such as income level, education level, statement balance at the end of the billing cycle, and number of transactions in the billing cycle, whereas the outcome variable $y _ { i , t }$ represents whether the user pays at least the minimum payment due within 21 days after the closing date of the billing cycle, i.e., $y _ { i , t } = 0$ if the user pays the minimum payment due or more and $y _ { i , t } = 1$ otherwise. Now we can formally define the credit risk prediction problem studied in this paper.

Credit risk prediction problem: Let Ψ denote the current billing cycle. Given a set of ?? credit product users $V =$ $\{ v _ { 1 } , v _ { 2 } , \cdots , v _ { n } \}$ , their observed intrinsic characteristics $\mathbf { x } _ { i , t }$ and delinquency outcomes $y _ { i , t }$ in each of the previous ?? billing cycles ?? for $t = \Psi - L , \cdots , \Psi - 1$ , as well as their characteristics $\mathbf { x } _ { i , \Psi }$ in the current billing cycle Ψ, $i =$ $1 , 2 , \ldots , n ,$ we aimed to predict these users’ delinquency outcomes $y _ { i , \Psi }$ in the current billing cycle.

We next describe our model for credit risk prediction. As a distinguishing feature, we take advantage of similarities among users for credit risk prediction beyond the sole use of their observed intrinsic characteristics. For the sake of simplicity, we dropped the time subscript ?? from $\mathbf { x } _ { i , t }$ and $y _ { i , t } ,$ since our model is applicable to each billing cycle. Given any user pair $\{ v _ { i } , v _ { j } \}$ from ?? with $i \neq j ,$ , we denote the similarity between them as $s _ { i j }$ , which is modeled as follows:

$$
s _ {i j} = \alpha_ {i} + \alpha_ {j} + \widetilde {\pmb {x}} _ {i} ^ {T} \widetilde {\pmb {x}} _ {j} + \pmb {z} _ {i} ^ {T} \pmb {z} _ {j}\tag{1}
$$

Here, $\widetilde { \mathbf { x } } _ { i } = \mathbf { x } _ { i } / \| \mathbf { x } _ { i } \| _ { 2 }$ is the normalization of $\mathbf { x } _ { i } ,$ where $\mathbf { x } _ { i }$ represents the vector of observed intrinsic characteristics of user $v _ { i } .$ . Thus, the term $\tilde { \mathbf { x } } _ { i } ^ { T } \tilde { \mathbf { x } } _ { j }$ corresponds to the observed similarity between $v _ { i }$ and $v _ { j }$ , which is measured based on their observed intrinsic characteristics (e.g., those recorded in the data). The term $\boldsymbol { \alpha } _ { i } + \boldsymbol { \alpha } _ { j } + \mathbf { z } _ { i } ^ { T } \mathbf { z } _ { j }$ models the unobserved (latent) similarity between $v _ { i }$ and $v _ { j } .$ , where $\alpha _ { i }$ and $\mathbf { z } _ { i }$ represent unobserved intrinsic characteristics of $v _ { i }$ . Using both the additive term $( \alpha _ { i } + \alpha _ { j } )$ and the product term $( \mathbf { z } _ { i } ^ { T } \mathbf { z } _ { j } )$ to model the unobserved similarity enriches the flexibility of our model, which is in line with the literature (Miller et al., 2009; Menon & Elkan, 2011). According to Equation (1), the similarity between a pair of users consists of both the observed and unobserved similarities between them.

As similar users are likely to exhibit similar repayment behaviors, it follows that for a user $v _ { i } \in V .$ , the user’s delinquent probability $p _ { i }$ is implied by the user’s observed intrinsic characteristics $\mathbf { x } _ { i } ,$ as well as the delinquent probabilities of other users who are similar to the user. Therefore, we model $p _ { i }$ as the probability of delinquency, conditioning on $\vec { v _ { i } } \mathbf { \bar { s } }$ intrinsic characteristics $\mathbf { x } _ { i } ,$ , similarity information $S _ { i } = \{ s _ { i j } { : } v _ { j } \in V , v _ { j } \neq v _ { i } \}$ , and delinquent probabilities of other users $\mathcal { P } _ { j | j \neq i } = \{ p _ { j } : v _ { j } \in V , v _ { j } \neq v _ { i } \} \mathrm { : }$

$$
p _ {i} = P r \big (y _ {i} = 1 \big | \pmb {x} _ {i}, S _ {i}, \mathcal {P} _ {j | j \neq i} \big).\tag{2}
$$

Let $\theta _ { i }$ denote $\vec { v _ { i } } \mathbf { \bar { s } }$ log-odds of delinquency and $\theta _ { i } =$ log $\frac { p _ { i } } { 1 - p _ { i } }$ Following the same idea of modeling $p _ { i }$ , we model $\theta _ { i }$ as:

$$
\theta_ {i} = \boldsymbol {x} _ {i} ^ {T} \boldsymbol {\beta} + c _ {i} \sum_ {v _ {j} \in V: j \neq i} s _ {i j} \theta_ {j},\tag{3}
$$

where $\pmb { \beta } \in \mathbb { R } ^ { p }$ is the coefficient vector and $\theta _ { j }$ denotes $v _ { j } { ' } \mathbf { s }$ log-odds of delinquency, $j \neq i$ . Here $\theta _ { i }$ is expressed as the addition of two components: the first component $\mathbf { x } _ { i } ^ { T } \pmb { \beta }$ is a linear combination of ??<sub>??</sub>’s observed intrinsic characteristics; the second component $\textstyle \sum _ { v _ { j } \in V : j \neq i } s _ { i j } \theta _ { j }$ is related to similarity information and is the sum of other users’ log-odds of delinquency weighted by the similarity between each of them and $v _ { i } .$ . User-specific parameter $c _ { i }$ regulates the relative importance between the user’s intrinsic component (first component) and similarity component (second component) in predicting $\theta _ { i } .$ . In sum, Equations (1) and (3) constitute our credit risk prediction model, the parameters of which are $\pmb { \beta } , c _ { i } , \alpha _ { i } .$ and $\mathbf { z } _ { i } , i = 1 , 2 , \ldots , n$ . Our model is distinguished from existing models for credit risk prediction in its operationalization of similarity, i.e., the model of $s _ { i j }$ in Equation (1) and the similarity component in Equation (3).

## Solution Method

In this section, we propose the estimation of our model parameters and the prediction of users’ delinquent probabilities based on the estimated parameters.

## Objective Function

We define vectors $\pmb { \theta } = ( \theta _ { 1 } , \theta _ { 2 } , \cdot \cdot \cdot , \theta _ { n } ) ^ { T } , \pmb { c } = ( c _ { 1 } , c _ { 2 } , \cdot \cdot \cdot$ $, c _ { n } ) ^ { T } , \pmb { \alpha } = ( \alpha _ { 1 } , \alpha _ { 2 } , \cdot \cdot \cdot , \alpha _ { n } ) ^ { T }$ , and matrices $\begin{array} { r } { X = ( { \bf x } _ { 1 } , { \bf x } _ { 2 } , \cdot \cdot } \end{array}$ $\bar { { \bf \Phi } } , { \bf x } _ { n } ) ^ { T } , \tilde { X } = ( \tilde { \bf x } _ { 1 } , \tilde { \bf x } _ { 2 } , \cdot \cdot \cdot , \tilde { \bf x } _ { n } ) ^ { T } , Z = ( { \bf z } _ { 1 } , { \bf z } _ { 2 } , \cdot \cdot \cdot , { \bf z } _ { n } ) ^ { T } , C =$ diag ${ \bf \tau } ( c ) , G = [ s _ { i j } ] _ { n \times n } .$ , where ?? is a ?? × ?? diagonal matrix with $c _ { 1 } , c _ { 2 } , \cdots , c _ { n }$ as its diagonal elements and diagonal elements in $G$ are defined to be 0. With these definitions, by the model of $\dot { \theta } _ { i }$ in Equation (3), it can be seen that

$$
\boldsymbol {\theta} = X \boldsymbol {\beta} + C G \boldsymbol {\theta}.\tag{4}
$$

Moreover, by the model of $s _ { i j }$ in Equation (1), we have

$$
G = \mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} - 2 d i a g (\pmb {\alpha}) + \tilde {X} \tilde {X} ^ {T} + Z Z ^ {T} - \sum_ {i = 1} ^ {n} (\widetilde {\pmb {x}} _ {i} ^ {T} \widetilde {\pmb {x}} _ {i} + \pmb {z} _ {i} ^ {T} \pmb {z} _ {i}) \pmb {e} _ {i} \pmb {e} _ {i} ^ {T},\tag{5}
$$

where $\mathbf { 1 } _ { n } \in \mathbb { R } ^ { n }$ is an all-ones vector, diag(??) is a $n \times n$ diagonal matrix with $\alpha _ { 1 } , \alpha _ { 2 } , \cdots , \alpha _ { n }$ as its diagonal elements, and $\mathbf { e } _ { i } \in \mathbb { R } ^ { n }$ is a standard unit vector with its $i ^ { \stackrel { \smile } { t h } }$ element being 1 and other elements being 0. The derivations of Equations (4) and (5) are given in Appendices A1 and A2, respectively.

According to Equation (4), we have

$$
\pmb {\theta} = (E _ {n} - C G) ^ {- 1} X \pmb {\beta} =: M ^ {- 1} X \pmb {\beta},\tag{6}
$$

where $M = E _ { n } - C G$ and $E _ { n }$ is an identity matrix of size ??. Interestingly, Equation (6) reveals an explicit form for each user’s log-odds of delinquency, which depends on the user’s intrinsic characteristics in $X ,$ coefficient vector $\beta ,$ and similarities among users captured in M (that involves $Z , \alpha ,$ and ??).

To estimate parameters $\mathbf { \delta } _ { \mathbf { \beta } _ { \mathbf { \varepsilon } } } \mathbf { { \vec { \beta } } _ { \mathbf { \varepsilon } } } _ { \mathbf { \beta } _ { \mathbf { \varepsilon } } } \mathbf { { \vec { \beta } } _ { \mathbf { \varepsilon } } } _ { \mathbf { \beta } _ { \mathbf { \varepsilon } } }$ ?? and ??, we obtained the negative log-likelihood $h ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } )$ from a training data set of users’ observed intrinsic characteristics and their delinquency outcomes $\{ \mathbf { x } _ { i } , y _ { i } \} _ { i = 1 } ^ { n }$

$$
h (\pmb {\beta}, Z, \pmb {\alpha}, \pmb {c}) = \frac {1}{n} \sum_ {i = 1} ^ {n} - y _ {i} \theta_ {i} + l o g \big (1 + e ^ {\theta_ {i}} \big).\tag{7}
$$

The derivation of $h ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } )$ is given in Appendix A3. To avoid overfitting, we imposed ridge-type regularization (Hastie et al., 2009, p. 61) on the parameters and used a penalized objective function $q ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } )$ for parameter estimation,

$$
q (\boldsymbol {\beta}, Z, \boldsymbol {\alpha}, \boldsymbol {c}) = h (\boldsymbol {\beta}, Z, \boldsymbol {\alpha}, \boldsymbol {c}) + \frac {\lambda_ {z}}{2} \| Z \| _ {F} ^ {2} + \frac {\lambda_ {\alpha}}{2} \| \boldsymbol {\alpha} \| _ {2} ^ {2} + \frac {\lambda_ {c}}{2} \| \boldsymbol {c} \| _ {2} ^ {2} + \frac {\lambda_ {\beta}}{2} \| \boldsymbol {\beta} \| _ {2} ^ {2} (8)
$$

where ∥·∥<sub>??</sub> is the Frobenius norm, $\lVert \cdot \rVert _ { 2 }$ is the $l _ { 2 } { \mathrm { - n o r m } }$ , and $\lambda _ { Z } , \lambda _ { \alpha } , \lambda _ { c } ,$ and $\lambda _ { \beta }$ are positive hyperparameters.

## Parameter Estimation

Given the objective function (Equation 8), we propose an alternating minimization approach formally presented in Algorithm 1, which learns parameters ??, ??, ?? and ?? of the credit risk prediction problem via block-wise minimization iteratively until convergence. Owing to its computational efficiency and excellent performance, alternating minimization has been widely adopted to solve nonconvex problems (Goodfellow et al., 2016). As shown, the algorithm takes a training data set of users’ observed intrinsic characteristics and their delinquency outcomes $\{ \mathbf { x } _ { i } , y _ { i } \} _ { i = 1 } ^ { n }$ as inputs and produces an estimation for the parameters. It first randomly initializes these parameters. In our implementation, we initialized each element in $\hat { Z } ^ { ( 0 ) }$ and ${ \widehat { \pmb { \beta } } } ^ { ( 0 ) }$ by randomly sampling from a standard normal distribution and set each element in $\widehat { \pmb { \alpha } } ^ { ( 0 ) }$ and $\hat { \pmb { c } } ^ { ( 0 ) }$ to $0 \mathrm { a n d } { \frac { 1 } { n } }$ respectively, where $\hat { Z } ^ { ( 0 ) } , \mathcal { \widehat { \pmb { \beta } } } ^ { ( 0 ) } , \mathcal { \widehat { \pmb { \alpha } } } ^ { ( 0 ) }$ and $\hat { \pmb { c } } ^ { ( 0 ) }$ denote the initializations of the parameters. The algorithm then iteratively updated one set of parameters while fixing the others until convergence (Lines 4-11 of the algorithm). For example, in Line 5, it minimized the objective function with respect to the parameters in ?? while fixing the rest of the parameters as constants.

Although Algorithm 1 is built upon the general framework of alternating minimization, there are problem-specific obstacles that need to be conquered. In particular, we need to find an efficient way to solve the optimization problems in Lines 5-8 of the algorithm with stable numerical performance. In response, we analyze the properties of our problem in Propositions 1-3, propose an efficient algorithm to solve these optimization problems, and show the convergence of Algorithm 1 in Theorem 1. Specifically, we solve the optimization problems with gradient descent and derive the gradients in Proposition 1.

Proposition 1: The gradients of the objective $q ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } )$ w.r.t. $Z , \alpha , c ,$ and ?? are

$$
\begin{array}{r l} & {\frac {\partial q}{\partial Z} = (M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C Z\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}\right) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z)} \\ & {\qquad - 2 Z \odot \left((M ^ {- 1} X \pmb {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}\right) \mathbf {1} _ {d} ^ {T}\right) + \lambda_ {Z} Z,} \\ & {\frac {\partial q}{\partial \pmb {\alpha}} = (M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}\right) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n})} \\ & {\qquad - 2 (M ^ {- 1} X \pmb {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}\right) + \lambda_ {\pmb {\alpha}} \pmb {\alpha},} \\ & {\frac {\partial q}{\partial \pmb {c}} = \left((M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}\right) \odot (G M ^ {- 1} X \pmb {\beta}) + \lambda_ {c} \pmb {c},} \\ & {\frac {\partial q}{\partial \pmb {\beta}} = X ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}} + \lambda_ {\pmb {\beta}} \pmb {\beta},} \end{array}
$$

$$
\begin{array}{r l} & {\text {where} \quad \frac {\partial h}{\partial \pmb {\theta}} = \frac {1}{n} (- \pmb {y} + \pmb {\pi} _ {\pmb {\theta}}), \pmb {y} = (y _ {1}, \dots , y _ {n}) ^ {T}, \pmb {\pi} _ {\theta} =} \\ & {(\pi (\theta_ {1}), \dots , \pi (\theta_ {n})) ^ {T}, \pi (\theta_ {i}) = \frac {1}{1 + e ^ {- \theta_ {i}}}, \frac {\partial h}{\partial \pmb {\theta} ^ {T}} = (\frac {\partial h}{\partial \pmb {\theta}}) ^ {T}, \odot} \end{array}
$$

denotes the element-wise product, and $\mathbf { 1 } _ { n } \in \mathbb { R } ^ { n }$ is an all-ones vector. (Proof: See Appendix B1)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:  $\varepsilon &gt; 0$ : convergence threshold
 $\{x_{i}, y_{i}\}_{i=1}^{n}$ : training data

Output:  $\hat{\beta}, \hat{Z}, \hat{\alpha}, \hat{c}$ : parameter estimations

1: Set iteration count r = 0.

2: Initialize  $\hat{Z}^{(r)}, \hat{\alpha}^{(r)}, \hat{c}^{(r)}, \hat{\beta}^{(r)}$ .

3: Compute  $q^{(r)} = q(\hat{\beta}^{(r)}, \hat{Z}^{(r)}, \hat{\alpha}^{(r)}, \hat{c}^{(r)})$  according to Equation (8).

4: repeat

5:  $\hat{Z}^{(r+1)} = \arg\min_{Z} q(\hat{\beta}^{(r)}, Z, \hat{\alpha}^{(r)}, \hat{c}^{(r)})$ .

6:  $\hat{\alpha}^{(r+1)} = \arg\min_{\alpha} q(\hat{\beta}^{(r)}, \hat{Z}^{(r+1)}, \alpha, \hat{c}^{(r)})$ .

7:  $\hat{c}^{(r+1)} = \arg\min_{c} q(\hat{\beta}^{(r)}, \hat{Z}^{(r+1)}, \hat{\alpha}^{(r+1)}, c)$ .

8:  $\hat{\beta}^{(r+1)} = \arg\min_{\beta} q(\beta, \hat{Z}^{(r+1)}, \hat{\alpha}^{(r+1)}, \hat{c}^{(r+1)})$ .

9: Compute  $q^{(r+1)} = q(\hat{\beta}^{(r+1)}, \hat{Z}^{(r+1)}, \hat{\alpha}^{(r+1)}, \hat{c}^{(r+1)})$  according to Equation (8).

10:  $r = r + 1$ .

11: until  $|q^{(r)} - q^{(r-1)}| &lt; \varepsilon$ .

12: return  $(\hat{\beta}, \hat{Z}, \hat{\alpha}, \hat{c}) = (\hat{\beta}^{(r)}, \hat{Z}^{(r)}, \hat{\alpha}^{(r)}, \hat{c}^{(r)})$ .

Algorithm 1. An Alternating Minimization Algorithm for Parameter Estimation.
</div>

With these explicit forms of gradients, it seems straightforward to solve these optimization problems with gradient descent. Nevertheless, the credit risk prediction problem typically involves a large number of users, and it is computationally prohibitive to calculate the inverse of the ?? × ?? matrix ?? in the gradients, where ?? is the number of users. Computing the inverse of an $n \times n$ matrix can have a large time complexity of $O ( n ^ { 3 } )$ , except for some special matrices (e.g., diagonal matrix).<sup>2</sup> To overcome this technical difficulty, we analyze the special structure of matrix ?? in Proposition 2 and propose an efficient way to compute its inverse in Proposition 3 by leveraging its special structure. We note that existing alternating minimization algorithms, such as the ALS algorithm (Hastie et al., 2015), are designed to overcome the computational challenge of conducting the singular value decomposition operation on a large and sparse matrix. Thus, they are not applicable to the specific technical difficulty encountered in our problem.

Proposition 2: Define $D _ { n } = E _ { n } + C ( 2 d i a g ( { \pmb { \alpha } } ) + \sum _ { i = 1 } ^ { n } ( \widetilde { x } _ { i } ^ { T } \widetilde { x } _ { i } +$ $\pmb { z } _ { i } ^ { T } \pmb { z } _ { i } \big ) \pmb { e } _ { i } \pmb { e } _ { i } ^ { T } ) , Q _ { 1 } = \left( \pmb { 1 } _ { n } , \pmb { \alpha } , \tilde { X } , Z \right)$ and $Q _ { 2 } = ( \pmb { \alpha } , \mathbf { 1 } _ { n } , \tilde { X } , Z )$ , where $Q _ { 1 }$ is the column-wise concatenation of ${ \bf 1 } _ { n } , { \pmb { \alpha } } , \tilde { X } , Z$ and $Q _ { 2 }$ is the column-wise concatenation of ??, $\mathbf { 1 } _ { n } , { \tilde { X } } , Z .$ By the definition of ?? in Equation $( 6 ) ,$ , we have $M = D _ { n } - C Q _ { 1 } Q _ { 2 } ^ { T } .$ (Proof: See Appendix B2)

It is noted that $D _ { n }$ is a diagonal matrix of size ?? and both $Q _ { 1 }$ and $Q _ { 2 } \mathrm { a r e } n \times ( p + d + 2 )$ matrices, where ?? and $d ,$ respectively, denote the number of observed and unobserved characteristics of a user. In our intended applications, we have $p + d + 2 \ll n .$ , as the combined number of observed and unobserved characteristics of a user is much less than the number of users. Moreover, the rank of $C Q _ { 1 } Q _ { 2 } ^ { T }$ is, at most, $p + d + 2 $ , since ?? is a diagonal matrix of size ?? and the rank of both $Q _ { 1 }$ and $Q _ { 2 }$ cannot exceed $p + d + 2 .$ According to Proposition $^ { 2 , }$ ?? can be expressed as a low-rank correction $( \mathrm { i . e . , } C Q _ { 1 } Q _ { 2 } ^ { T } )$ to a diagonal matrix of size ?? $( \mathrm { i } . { \mathrm { e } } . , D _ { n } )$ . Employing the special structure of ?? discovered in Proposition 3, we can efficiently compute $M ^ { - 1 }$ by Proposition 3.

Proposition 3: Based on Proposition 2, we have

$$
M ^ {- 1} = D _ {n} ^ {- 1} + D _ {n} ^ {- 1} C Q _ {1} (E _ {p + d + 2} - Q _ {2} ^ {T} D _ {n} ^ {- 1} C Q _ {1}) ^ {- 1} Q _ {2} ^ {T} D _ {n} ^ {- 1},
$$

where $E _ { p + d + 2 }$ is an identity matrix of size $p + d + 2 .$ . (Proof: Given the special structure of ?? in Proposition 2, Proposition 3 follows from a direct application of the Sherman-Morrison-Woodbury formula—Press et al., 2007, p. 80).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: $\varepsilon^{Z}$: convergence threshold for updating $Z$, $\varepsilon^{Z} &gt; 0$ $\gamma$, $\zeta$: Armijo parameters, $0 &lt; \gamma \leq 1/2$, $0 &lt; \zeta &lt; 1$
Output: $\hat{Z}^{(r+1)}$
1: Set iteration count $\rho = 0$.
2: Initialize $\check{Z}^{(\rho)} = \hat{Z}^{(r)}$, $\check{q}^{(\rho)} = q(\hat{\boldsymbol{\beta}}^{(r)}, \check{Z}^{(\rho)}, \hat{\boldsymbol{\alpha}}^{(r)}, \hat{\boldsymbol{c}}^{(r)})$.
3: Define $q(Z) = q(\hat{\boldsymbol{\beta}}^{(r)}, Z, \hat{\boldsymbol{\alpha}}^{(r)}, \hat{\boldsymbol{c}}^{(r)})$.
4: repeat
5: Compute the gradient of $q(Z)$ at $Z = \check{Z}^{(\rho)}$, denoted by $\frac{\partial q}{\partial Z} (\check{Z}^{(\rho)})$, with the formulas given in Propositions 1 and 3.
6: Set stepsize $u = 1$.
7: while $q(\check{Z}^{(\rho)} - u \frac{\partial q}{\partial Z} (\check{Z}^{(\rho)})) &gt; q(\check{Z}^{(\rho)}) - \gamma u \| \frac{\partial q}{\partial Z} (\check{Z}^{(\rho)}) \|_{F}^{2}$ do
8: $u = \zeta u$. (choose step size $u$ via a backtracking line search)
9: end while
10: $\check{Z}^{(\rho+1)} = \check{Z}^{(\rho)} - u \frac{\partial q}{\partial Z} (\check{Z}^{(\rho)})$.
11: Compute $\check{q}^{(\rho+1)} = q(\hat{\boldsymbol{\beta}}^{(r)}, \check{Z}^{(\rho+1)}, \hat{\boldsymbol{\alpha}}^{(r)}, \hat{\boldsymbol{c}}^{(r)})$ according to Equation (8).
12: $\rho = \rho + 1$.
13: until $|\check{q}^{(\rho)} - \check{q}^{(\rho-1)}| &lt; \varepsilon^{Z}$.
14: return $\hat{Z}^{(r+1)} = \check{Z}^{(\rho)}$.
Algorithm 2. A Gradient Descent Algorithm for Updating Z in Line 5 of Algorithm 1.
</div>

By Proposition 3, computing the inverse of the large-sized matrix ?? can be equivalently converted to an expression that involves inverting matrices $D _ { n }$ and $E _ { p + d + 2 } - Q _ { 2 } ^ { T } D _ { n } ^ { - 1 } C Q _ { 1 } ,$ both of which can be efficiently inverted. Matrix $D _ { n }$ is a diagonal matrix, whose inverse can be directly and efficiently obtained by replacing each diagonal element with its reciprocal. Matrix $E _ { p + d + 2 } - Q _ { 2 } ^ { T } D _ { n } ^ { - 1 } C Q _ { 1 }$ is a square matrix of size $p \ + \ d \ + \ 2$ (typically much smaller than ??); thus it is more time-efficient to invert $E _ { p + d + 2 } - Q _ { 2 } ^ { T } D _ { n } ^ { - 1 } C Q _ { 1 }$ than it is to invert ??. Equipped with Proposition 3, our proposed Algorithm 1 is particularly suitable for real-world credit risk prediction problems involving a large number of users.

Based on Propositions 1-3, we propose a solution to the optimization problems in Lines 5-8 of Algorithm 1. In particular, Algorithm 2 solves the optimization problem in Line 5 of Algorithm 1 and updates parameter estimations ??<sup>̂</sup>. Algorithms for solving the other optimization problems are similar to Algorithm 2 and thus omitted for reasons of space. As shown, Algorithm 2 updates ??<sup>̂</sup> via gradient descent, where the gradient can be computed using the formulas given in Propositions 1 and 3. It employs the backtracking line search with the Armijo rule (Nocedal & Wright, 2006, p. 33) to choose step size (Lines 6-9 in Algorithm 2), which ensures that the objective function keeps going downhill and converges (Bertsekas, 1999). Next, we show the convergence of Algorithm 1.

Theorem 1: The proposed Algorithm 1 for parameter estimation converges. (Proof: See Appendix B3)

Taken together, Algorithm 1 iteratively updates estimations for parameters ??, ??, ?? and ?? via blockwise minimization. Each optimization step of the algorithm is solved using Algorithm 2 or a similar procedure developed based on Propositions 1-3. Theorem 1 guarantees the convergence of Algorithm 1.

## Credit Risk Prediction

We used training data from the previous billing cycles to estimate the parameters. Specifically, we employed the training data of users’ observed intrinsic characteristics $\mathbf { x } _ { i , t }$ and delinquency outcomes $y _ { i , t }$ in each of the previous ?? billing cycles ??, where $t = \Psi - L , \cdot \cdot \cdot , \Psi - 1 , i = 1 , 2 , \cdot \cdot \cdot , n _ { \mathrm { { \ L } } }$ and Ψ denotes the current billing cycle. We then constructed the negative log-likelihood $h _ { t } ( \beta , Z , \alpha , c )$ for each of the previous billing cycles in the same way as that of Equation (7), and formed the composite negative log-likelihood objective function $\begin{array} { r l } {  { \sum _ { t = \Psi - L } ^ { \Psi - 1 } h _ { t } ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } ) } } \end{array}$ (Varin et al., 2011). Next, we substituted $h ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } )$ in Equation (8) with the composite negative log-likelihood objective function and the proposed Algorithm 1 remains applicable for parameter estimation. Our model can thereby effectively learn parameters $\mathbf { z } _ { i }$ and $\alpha _ { i }$ based on users’ diverse historical repayment behaviors and timevariant intrinsic characteristics With the estimated parameters $( \widehat { \pmb { \beta } } , \widehat { Z } , \widehat { \pmb { \alpha } } , \widehat { \pmb { c } } )$ and users’ observed intrinsic characteristics $\mathbf { x } _ { i , \Psi }$ in the current billing cycle Ψ, $i = 1 , 2 , $ $\cdot , n ,$ , we can compute their log-odds of delinquency ${ \pmb \theta } _ { \Psi } \ =$ $( \theta _ { 1 , \Psi } , \theta _ { 2 , \Psi } , \cdot \cdot \cdot , \bar { \theta _ { n , \Psi } } ) ^ { T }$ using Equation (6). The predicted individual delinquent probabilities are then given by $p _ { i , \Psi } =$ $\begin{array} { r } { \pi \big ( \theta _ { i , \Psi } \big ) = \frac { 1 } { 1 + e ^ { - \theta _ { i , \Psi } } } , i = 1 , 2 , \cdots , n . } \end{array}$

In sum, our proposed credit risk prediction method is distinct from existing methods in its operationalization of similarity. Specifically, our method models similarity in Equation (1) and incorporates it into credit risk prediction in Equation (3). It then estimates the model parameters using Algorithms 1 and 2, based on the findings in Propositions 1-3 and Theorem 1. These algorithms, propositions, and theorem constitute the methodological novelty of our study.

## Extensions

We next extend our model to solve the multiclass credit risk prediction problem in the following subsection and the numerical credit risk prediction problem in the subsequent subsection.

## Multiclass Credit Risk Prediction Problem

For the multiclass credit risk prediction problem, credit risk outcome ?? takes one of the more than two categories, i.e., $y _ { i } \in$ $\{ 0 , 1 , \cdots , K \}$ with $K \ge 2$ . For example, credit card companies make a significant portion of their revenues from interest charged on cards with partially paid statement balances (Stolba, 2019). Therefore, it is reasonable to further categorize nondelinquent users into two subgroups: those who pay off their statement balances (i.e., no interest charged) and those who make partial payments (i.e., interest charged). In this example, $y _ { i }$ can be one of the three outcomes defined below:

$$
y _ {i} = \left\{ \begin{array}{l l} 2 & \text {   if   user   } v _ {i} \text {   is   deliquent   (failing   to   pay   the   minimum   due)   }, \\ 1 & \text {   if   user   } v _ {i} \text {   is   non - deliquent   but   only   makes   partial   payment, } \\ 0 & \text {   if   user   } v _ {i} \text {   is   non - deliquent   and   pays   off   the   statement   balance. } \end{array} \right.
$$

Let $p _ { k , i }$ be the probability that the credit risk outcome of user $v _ { i }$ is ??. To define the log-odds of being a credit risk outcome, we set credit risk outcome 0 as the reference. Accordingly, for user $v _ { i } ,$ we define the user’s log-odds $\theta _ { k , i }$ of being credit risk outcome ?? as $\begin{array} { r } { \theta _ { k , i } = \log \frac { p _ { k , i } } { p _ { 0 , i } } ~ \mathrm { ( i . e . } } \end{array}$ , the logarithm of the probability of being credit risk outcome ?? to that of being outcome 0), for $k = 1 , 2 , \cdot \cdot \cdot , K .$ Following the same reasoning of modeling log-odds for the binary credit risk prediction problem, we model $\theta _ { k , i }$ as

$$
\theta_ {k, i} = \pmb {x} _ {i} ^ {T} \pmb {\beta} _ {k} + c _ {i} \sum_ {v _ {i} \in V: j \neq i} s _ {i j} \theta_ {k, j} \quad \mathrm{for} k = 1, 2 \ldots , K,\tag{9}
$$

where $\pmb { \beta } _ { k } \in \mathbb { R } ^ { p }$ is the coefficient vector associated with credit risk outcome ?? and $s _ { i j }$ is the similarity between $v _ { i }$ and $v _ { j } ,$ which is modeled by Equation (1). According to Equation (9), $\theta _ { k , i }$ depends on user $\vec { v _ { i } } \mathbf { \bar { s } }$ observed intrinsic characteristics $\mathbf { x } _ { i , \astrosun }$ as well as the log-odds of other users who are similar to the user. Parameter ?? denotes the relative importance between the component of the user’s intrinsic characteristics and the similarity component in determining $\theta _ { k , i }$

Denoting $\pmb { \theta } _ { k } = ( \theta _ { k , 1 } , \theta _ { k , 2 } , \cdot \cdot \cdot , \theta _ { k , n } ) ^ { T }$ and using notations $X , ~ C , ~ G ,$ , and $E _ { n }$ defined in the Objective Function subsection, we can derive the following equation from Equation (9).

$$
\pmb {\theta} _ {k} = X \pmb {\beta} _ {k} + C G \pmb {\theta} _ {k},\tag{10}
$$

where ?? is given in Equation (5). The derivation of Equation (10) is similar to that of Equation (4) shown in Appendix A1 and is thus omitted. Via Equation (10), we can obtain the explicit form for the log-odds ${ \pmb \theta } _ { k } \mathrm { : }$

$$
\pmb {\theta} _ {k} = (E _ {n} - C G) ^ {- 1} X \pmb {\beta} _ {k} =: M ^ {- 1} X \pmb {\beta} _ {k},\tag{11}
$$

where $M = E _ { n } - C G$ . For the simplicity of notation, we denote the coefficients set $( \pmb { \beta } _ { 1 } , \pmb { \beta } _ { 2 } , \cdots , \pmb { \beta } _ { K } )$ as $\pmb { \beta } _ { \{ 1 : K \} }$ . To estimate parameters $\beta _ { \{ 1 : K \} } , Z _ { \{ 1 : K \} }$ , ??, and ?? for the multiclass credit risk prediction problem, we derived the negative loglikelihood $h ^ { m } ( \pmb { \beta } _ { \{ 1 : K \} } , Z , \pmb { \alpha } , \pmb { c } )$ from a training data set of users’ observed intrinsic characteristics and their multiclass credit risk outcomes $\{ \mathbf { x } _ { i } , y _ { i } \} _ { i = 1 } ^ { n } \colon$

$$
h ^ {m} \left(\boldsymbol {\beta} _ {\{1: K \}}, Z, \boldsymbol {\alpha}, \boldsymbol {c}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\left(\sum_ {k = 1} ^ {K} - \delta_ {k, i} \theta_ {k, i}\right) + \log \left(1 + \sum_ {k = 1} ^ {K} e ^ {\theta_ {k, i}}\right)\right),\tag{12}
$$

where $\delta _ { k , i } = 1$ if $y _ { i } = k$ and $\delta _ { k , i } = 0$ otherwise. The derivation of the equation is given in Appendix C1. Consequently, the regularized objective function is given by

$$
\begin{array}{l} q ^ {m} \left(\boldsymbol {\beta} _ {\{1: K \}}, Z, \boldsymbol {\alpha}, \boldsymbol {c}\right) = h ^ {m} \left(\boldsymbol {\beta} _ {\{1: K \}}, Z, \boldsymbol {\alpha}, \boldsymbol {c}\right) + \frac {\lambda_ {Z}}{2} \| Z \| _ {F} ^ {2} + \frac {\lambda_ {\boldsymbol {\alpha}}}{2} \| \boldsymbol {\alpha} \| _ {2} ^ {2} \\ \quad + \frac {\lambda_ {c}}{2} \| \boldsymbol {c} \| _ {2} ^ {2} + \sum_ {k = 1} ^ {K} \frac {\lambda_ {\boldsymbol {\beta}}}{2} \| \boldsymbol {\beta} _ {k} \| _ {2} ^ {2}, \end{array} \tag {13}\tag{13}
$$

where $\lambda _ { Z } , \lambda _ { { \pmb { \alpha } } } , \lambda _ { c }$ and $\lambda _ { \beta }$ are positive hyper-parameters.

We estimated the parameters by optimizing the objective function (Equation 13) with an alternating minimization algorithm. The algorithm is similar to Algorithm 1, except that it uses the gradients given in Proposition 4 and updates $\pmb { \beta } _ { \{ 1 : K \} }$ instead of $\pmb { \beta }$ in each iteration. We present the algorithm in Appendix C2 to save space here.

Proposition 4: The gradients of the objective $\boldsymbol { q } ^ { m } ( \pmb { \beta } _ { \{ 1 : K \} } , Z , \pmb { \alpha } , \pmb { c } )$ w.r.t. ??,??, ??, and $\pmb { \beta } _ { \{ 1 : K \} }$ are

$$
\begin{array}{l} \frac {\partial q ^ {m}}{\partial Z} = \sum_ {k = 1} ^ {K} [ (M ^ {- 1} X \pmb {\beta} _ {k}) \left(\frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} M ^ {- 1} C Z\right) + \Big (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} \Big) (\pmb {\beta} _ {k} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z) \\ \qquad - 2 Z \odot \Big ((M ^ {- 1} X \pmb {\beta} _ {k}) \odot \Big (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} \Big) \mathbf {1} _ {d} ^ {T} \Big) ] + \lambda_ {Z} Z, \\ \frac {\partial q ^ {m}}{\partial \pmb {\alpha}} = \sum_ {k = 1} ^ {K} [ (M ^ {- 1} X \pmb {\beta} _ {k}) \left(\frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + \Big (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} \Big) (\pmb {\beta} _ {k} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ \qquad - 2 (M ^ {- 1} X \pmb {\beta} _ {k}) \odot \Big (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} \Big) ] + \lambda_ {\alpha} \pmb {\alpha}, \\ \frac {\partial q ^ {m}}{\partial \pmb {c}} = \sum_ {k = 1} ^ {K} [ \Big ((M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} \Big) \odot (G M ^ {- 1} X \pmb {\beta} _ {k}) ] + \lambda_ {\pmb {c}} \pmb {c}, \\ \frac {\partial q ^ {m}}{\partial \pmb {\beta} _ {k}} = X ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} + \lambda_ {\pmb {\beta}} \pmb {\beta} _ {k} \quad f o r \quad k = 1, 2, \dots , K, \end{array}
$$

where $\begin{array} { r } { \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } } = \frac { 1 } { n } ( - \pmb { \delta } _ { k } + \pmb { \pi } _ { k } ^ { m } ) , \pmb { \delta } _ { k } = ( \pmb { \delta } _ { k , 1 } , \cdots , \pmb { \delta } _ { k , n } ) ^ { T } , \pmb { \pi } _ { k } ^ { m } = } \end{array}$ $\begin{array} { r } { ( \pi _ { k , 1 } ^ { m } , \cdots , \pi _ { k , n } ^ { m } ) ^ { T } , \pi _ { k , i } ^ { m } = \frac { e ^ { \theta _ { k , i } } } { 1 + \sum _ { \widetilde { k } = 1 } ^ { K } e ^ { \theta _ { \widetilde { k } , i } } } } \end{array}$ , and $\frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } = ( \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } } ) ^ { T }$ . (Proof: See Appendix C3)

We note that Propositions 2 and 3 remain applicable to efficiently compute the inverse of the large-sized matrix ?? in the gradients given in Proposition 4. As a result, Algorithm 2 is still applicable to the multiclass credit risk prediction problem, with the simple modification of using the gradients in Proposition 4 for the multiclass case. Therefore, this subsection generalizes the credit risk prediction problem defined in the Problem Formulation and Model section to the multiclass scenario and maintains the convenient computational scale-up.

By applying the algorithm developed in this subsection to the training data of users’ observed intrinsic characteristics and credit risk outcomes in the previous ?? billing cycles, we obtained parameter estimates $( \widehat { \pmb { \beta } } _ { \{ 1 : k \} } , \widehat { Z } , \widehat { \pmb { \alpha } } , \widehat { \pmb { c } } )$ . With these parameter estimates and users’ observed intrinsic characteristics $\mathbf { x } _ { i , \Psi }$ in the current billing cycle Ψ, $i \ =$ $1 , 2 , \ldots , n ,$ we employed Equation (11) to compute the log-odds $\pmb { \theta } _ { k , \Psi } = ( \theta _ { k , 1 , \Psi } , \theta _ { k , 2 , \Psi } , \cdot \cdot \cdot , \theta _ { k , n , \Psi } ) ^ { T }$ for each credit risk outcome $k , \mathrm { ~  ~ { ~ \boldsymbol ~ { ~ k ~ } ~ } ~ } = 1 , 2 , \ldots , K .$ Recall that $\begin{array} { r } { \theta _ { k , i , \Psi } = \log \frac { p _ { k , i , \Psi } } { p _ { 0 , i , \Psi } } } \end{array}$ and $\begin{array} { r } { \sum _ { k = 0 } ^ { K } p _ { k , i , \Psi } = 1 } \end{array}$ . We can thus calculate the predicted probability of each credit risk outcome for user $v _ { i }$ in the current billing cycle Ψ as

$$
p _ {0, i, \Psi} = \frac {1}{1 + \sum_ {\underline {{k}} = 1} ^ {K} e ^ {\theta_ {\overline {{k}} , i , \Psi}}}, p _ {k, i, \Psi} = \frac {e ^ {\theta_ {k , i , \Psi}}}{1 + \sum_ {\underline {{k}} = 1} ^ {K} e ^ {\theta_ {\overline {{k}} , i , \Psi}}} \quad \text {for} k = 1, 2 \dots , K.
$$

## Numerical Credit Risk Prediction Problem

Numerical credit risk indicators, such as the repayment rate $( \mathrm { i . e . } ,$ the proportion of statement balance repaid), reveal more granular information about users’ credit risks than categorical credit risk outcomes. For example, non-delinquent users who pay the minimum payment due can be further differentiated according to their repayment rates. We thus extend our model to predict numerical credit risk indicators. Let $\mu _ { i }$ denote the estimation of user $v _ { i } { } ^ { \ } \mathbf { s }$ numerical credit risk indicator $y _ { i }$ Similar to the binary credit risk prediction problem, we model $\mu _ { i }$ as the addition of two components: One component is defined on $v _ { i } { } ^ { \ } \mathbf { s }$ observed intrinsic characteristics $\mathbf { x } _ { i }$ and the other is based on similarity information. Accordingly, we have

$$
\mu_ {i} = \pmb {x} _ {i} ^ {T} \pmb {\beta} + c _ {i} \sum_ {v _ {j} \in V: j \neq i} s _ {i j} \mu_ {j},\tag{14}
$$

where $\pmb { \beta } \in \mathbb { R } ^ { p }$ denotes the coefficient vector, $c _ { i }$ represents the relative importance between the two components, and $s _ { i j }$ is defined in Equation (1). We denote $\pmb { \mu } = ( \mu _ { 1 } , \mu _ { 2 } , \cdot \cdot \cdot , \mu _ { n } ) ^ { T }$ and use notations $X , C , G$ and $E _ { n } ,$ defined in the Objective Function subsection. Similar to the derivation of Equation (4) in Appendix A1, we can obtain the following equations from Equation (14):

$$
\pmb {\mu} = X \pmb {\beta} + C G \pmb {\mu},\tag{15}
$$

which implies that

$$
\pmb {\mu} = (E _ {n} - C G) ^ {- 1} X \pmb {\beta} =: M ^ {- 1} X \pmb {\beta},\tag{16}
$$

where $M = E _ { n } - C G .$

To estimate parameters ??, ??, ?? and ??, we employed a penalized ordinary least squares (OLS) approach and obtained the OLS loss function $h ^ { \bar { n } }$ from a training data set of users’ observed intrinsic characteristics and their numerical credit risk indicators $\{ \mathbf { x } _ { i } , y _ { i } \} _ { i = 1 } ^ { n } \mathrm { : }$

$$
h ^ {n} (\pmb {\beta}, Z, \pmb {\alpha}, \pmb {c}) = \frac {1}{2 n} (Y - \pmb {\mu}) ^ {T} (Y - \pmb {\mu}),\tag{17}
$$

where $Y = ( y _ { 1 } , y _ { 2 } , \cdot \cdot \cdot , y _ { n } ) ^ { T }$ . The penalized objective $q ^ { n } ( \beta , Z , \alpha , c )$ is then given by

$$
\begin{array}{l} q ^ {n} (\boldsymbol {\beta}, Z, \boldsymbol {\alpha}, \boldsymbol {c}) = h ^ {n} (\boldsymbol {\beta}, Z, \boldsymbol {\alpha}, \boldsymbol {c}) + \frac {\lambda_ {z}}{2} \| Z \| _ {F} ^ {2} + \frac {\lambda_ {\alpha}}{2} \| \boldsymbol {\alpha} \| _ {2} ^ {2} + \frac {\lambda_ {c}}{2} \| \boldsymbol {c} \| _ {2} ^ {2} + \\ \frac {\lambda_ {\beta}}{2} \| \boldsymbol {\beta} \| _ {2} ^ {2}, \end{array} \tag {18}
$$

where $\lambda _ { Z } , \lambda _ { { \pmb { \alpha } } } , \lambda _ { c }$ and $\lambda _ { \beta }$ are positive hyper-parameters.

An alternating minimization algorithm is proposed to estimate the parameters by optimizing the objective function (Equation 18). Note that given $\hat { Z } , \widehat { \pmb { \alpha } }$ and ??̂, estimating parameters $\pmb { \beta }$ reduces to the parameter estimation for a ridge linear regression problem and has a closed-form solution (e.g., Hastie et al., 2009, p.64):

$$
\widehat {\pmb {\beta}} = \left(X _ {\widehat {M}} ^ {T} X _ {\widehat {M}} + \lambda_ {\pmb {\beta}} E _ {p}\right) ^ {- 1} X _ {\widehat {M}} ^ {T} Y,\tag{19}
$$

where $X _ { \widehat { M } } = \widehat { M } ^ { - 1 } X , \widehat { M } = E _ { n } - \widehat { C } \widehat { G }$ according to Equation $( 1 6 ) , \hat { C } = \mathrm { d i a g } ( \hat { \pmb { c } } )$ , ??<sup>̂</sup> is computed by plugging ??<sup>̂</sup> and ??̂ into Equation (5), and $E _ { p }$ is an identity matrix of size ??. The parameter estimation algorithm described in Appendix D1 is similar to Algorithm 1, except that it updates $\pmb { \beta }$ according to Equation (19) and other parameters with the gradients given in Proposition 5. The algorithm enjoys the same advantages as demonstrated from Propositions 2 and 3 for the efficient computation of $M ^ { - 1 }$ in the gradients given in Proposition 5. We can obtain parameter estimates $( \widehat { \pmb { \beta } } , \widehat { Z } , \widehat { \pmb { \alpha } } , \widehat { \pmb { c } } )$ by applying the algorithm to the training data of users’ observed intrinsic characteristics and credit risk indicators in the previous ?? billing cycles. With the estimated parameters and users observed intrinsic characteristics $\mathbf { x } _ { i , \Psi }$ in the current billing cycle $\Psi , i = 1 , 2 , \dots , n ,$ their predicted credit risk indicators, $\mu _ { \Psi } ,$ , can be computed through Equation (16).

Proposition 5: The gradients of the objective $q ^ { n } ( \pmb { \beta } , Z , \pmb { \alpha } , \pmb { c } )$ with respect to $Z , \pmb { \alpha } ,$ and ?? are

$$
\begin{array}{r l} & {\frac {\partial q ^ {n}}{\partial Z} = (M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} M ^ {- 1} C Z\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}}\right) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z)} \\ & {\qquad - 2 Z \odot \left((M ^ {- 1} X \pmb {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}}\right) \mathbf {1} _ {d} ^ {T}\right) + \lambda_ {Z} Z,} \\ & {\frac {\partial q ^ {n}}{\partial \pmb {\alpha}} = (M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}}\right) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n})} \\ & {\qquad - 2 (M ^ {- 1} X \pmb {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}}\right) + \lambda_ {\alpha} \pmb {\alpha},} \\ & {\frac {\partial q ^ {n}}{\partial \pmb {c}} = \left((M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}}\right) \odot (G M ^ {- 1} X \pmb {\beta}) + \lambda_ {c} \pmb {c},} \end{array}
$$

where $\begin{array} { r } { \frac { \partial h ^ { n } } { \partial \pmb { \mu } } = \pmb { \mu } - Y \mathrm { a n d } \frac { \partial h ^ { n } } { \partial \pmb { \mu } ^ { T } } = \left( \frac { \partial h ^ { n } } { \partial \pmb { \mu } } \right) ^ { T } } \end{array}$ . (Proof: See Appendix D2)

## Empirical Evaluation

## Data and Evaluation Procedure

We obtained data from a non-U.S. commercial bank’s provincial branch. One data set contained 11,761 credit card users’ repayment information over 22 billing cycles/months. For every user in each billing cycle, the data set showed the user’s minimum payment due and the repayment amount within 21 days after the closing date of the billing cycle. A user $v _ { i }$ would be delinquent for billing cycle ?? if the user’s repayment amount was less than the minimum payment due; we set $y _ { i , t } = 1 ;$ otherwise, the user would be considered non-delinquent, and $y _ { i , t } = 0$ . On average, there were 3,932 delinquent users (or 33.43% of the credit card users in our data set) per billing cycle.<sup>3</sup> The delinquency rate ranged from 28.89% to 35.07% across 22 billing cycles, with a median of 33.81%.

Another data set depicted the billing information of these users over the same time period. Specifically, it included the spending amount and the number of transactions by a user in a billing cycle as well as the user’s statement balance, accumulated interest owed by the end of the billing cycle, and the number of historical delinquencies. The third data set contained users’ demographic information, including home type (e.g., rent or own), income level, account holding branch, and education level.<sup>4</sup> User $\vec { v _ { i } } \mathbf { \bar { s } }$ billing and demographic information in billing cycle ?? was used to construct the user’s observed intrinsic characteristics $\mathbf { x } _ { i , t }$

We next detail the evaluation procedure. Let Ψ be the current billing cycle. We constructed training data using users intrinsic characteristics $\mathbf { x } _ { i , t }$ and delinquency outcomes $y _ { i , t }$ in each of the previous 12 billing cycles ??, $t = \Psi - 1 2 , ~ \cdot \cdot \cdot , \Psi -$ 1. Using the training data, we then trained our method and each benchmark method to predict delinquent probability $p _ { i , \Psi }$ for every user in the current billing cycle based on $\mathbf { x } _ { i , \Psi } . ^ { 5 }$ The performance of a method was evaluated using common metrics for credit risk prediction that include precision, recall, F1 score, and AUC (Khandani et al., 2010; Lu et al., 2023; Xu et al., 2023). Specifically, for a method, top-?? users refer to the group of ?? users with the highest delinquent probabilities predicted by this method and deemed as delinquent by the method. Let $T P _ { \Psi }$ denote the number of true delinquent users among the top-?? users and $n _ { \Psi } ^ { d }$ be the number of true delinquent users in billing cycle Ψ. Precision is the fraction of predicted delinquent users who are actually delinquent:

$$
p r e c i s i o n = \frac {T P _ {\psi}}{Q}.
$$

Recall is the fraction of true delinquent users who are correctly predicted as delinquent:

$$
r e c a l l = \frac {T P _ {\psi}}{n _ {\psi} ^ {d}}.
$$

F1 score is the harmonic mean of precision and recall:

$$
F 1 = \frac {2 \times p r e c i s i o n \times r e c a l l}{p r e c i s i o n + r e c a l l}.
$$

In our evaluation, AUC reveals the probability that a randomly chosen delinquent user will be predicted to have a higher delinquent probability than a randomly chosen nondelinquent user (Fang et al., 2013). The value of AUC is in the range of [0,1] and a higher AUC indicates better performance of credit risk prediction.

We carefully chose representative existing methods for credit risk prediction as benchmarks. Logistic regression is the most widely used method and industry standard for credit risk prediction (Thomas et al., 2017). Moreover, the key methodological difference between our latent similarityenhanced method (LSE) and ridge logistic regression (RLR) (Cessie & Houwelingen, 1992) is the consideration of similarity by LSE, where the similarity between a pair of users consists of both the observed and latent similarities between them. Therefore, RLR was chosen as a useful benchmark. The performance difference between our method and RLR not only reveals the practical value of our method but also demonstrates the performance contribution from its methodological novelty. Further, we benchmarked against two representative methods for credit risk prediction: multilayer perceptron (MLP) and support vector machine (SVM). Both methods have shown excellent performance for credit risk prediction (Baesens et al., 2003). We also compared our method with a popular ensemble method for credit risk prediction—extreme gradient boosting (XGBoost) (Chen & Guestrin, 2016). Recent studies have proposed deep learning-based methods for credit risk prediction. A representative method in this category was developed by Babaev et al. (2019), who proposed a recurrent neural network (RNN) model based on gated recurrent unit (GRU) for credit risk prediction. We adapted this method for our data set and named it RNN-GRU. In addition, Wang et al. (2021) proposed a temporal-aware graph neural network (TemGNN) method for credit risk prediction over dynamic graphs. To apply this method, we first utilized users observed intrinsic characteristics to construct a similarity network among them for each billing cycle and then adapted TemGNN to these constructed dynamic similarity networks for credit risk prediction. We designate this benchmark method as SIM-TemGNN. Table 1 summarizes the methods compared in our evaluation.<sup>6</sup>

To tune hyperparameters for each compared method, we trained the method with users’ observed intrinsic characteristics and delinquency outcomes in billing cycles 1 to 12 to predict each user’s delinquent probability in billing cycle 13 (Ψ = 13). Hyperparameter values enabling the method to achieve its best performance (measured with the metrics elaborated above) were then chosen. For our method, we set its hyperparameters as $\lambda _ { Z } = 0 . 0 1 , \lambda _ { c } = 0 . 5 , \lambda _ { \alpha } =$ $1 , \lambda _ { \beta } = 0 . 0 0 1 , \mathrm { a n d } d = 2 .$ and set convergence thresholds in Algorithms 1 and 2 to 0.001. Each user has a connection score $\alpha _ { i }$ that needs to be learned, whereas regression coefficients $\pmb { \beta }$ are shared by all users. Therefore, a large $\lambda _ { \alpha }$ was chosen to reduce the model complexity while a small $\lambda _ { \beta }$ was selected to help learn the relation between users’ observed intrinsic characteristics and delinquency outcomes. The Armijo parameters ?? and $\zeta$ in Algorithm 2 were set to 0.1 and 0.5, respectively. For RLR, its ridge parameter was set to 10<sup>−4</sup>. MLP had 3 hidden layers of sizes 128, 64, and 32, respectively. SVM employed the RBF kernel (Burges, 1998) with its regularization parameter being set to 10. XGBoost used tree boosters with a maximum depth of 7, and the number of boosting rounds was set to 400. RNN-GRU was trained using the Adam optimizer with a learning rate of 0.001 and a batch size of 256, and the size of its hidden states was set to 128. For SIM-TemGNN, to construct a similarity network for each billing cycle, we calculated the Euclidean distance between each pair of users based on their observed intrinsic characteristics $\mathbf { x } _ { i , t }$ in each billing cycle. For each user, the top 10 closest users (with the smallest distances) were selected as adjacent nodes in the similarity network for that billing cycle. The MLP component of SIM-TemGNN had 3 hidden layers with sizes of 128, 64, and 32, respectively; its GNN component consisted of 2 layers, each with an embedding size of $3 2 ,$ and the size of each hidden state of its LSTM component was set to 64.

<table><tr><td colspan="2">Table 1. Summary of Methods Compared in the Evaluation</td></tr><tr><td>Method</td><td>Notes</td></tr><tr><td>LSE</td><td>Latent similarity-enhanced method, our method</td></tr><tr><td>RLR</td><td>Ridge logistic regression, benchmark</td></tr><tr><td>MLP</td><td>Multilayer perceptron, benchmark</td></tr><tr><td>SVM</td><td>Support vector machine, benchmark</td></tr><tr><td>XGBoost</td><td>eXtreme gradient boosting, benchmark</td></tr><tr><td>RNN-GRU</td><td>Recurrent neural network based on gated recurrent unit, benchmark</td></tr><tr><td>SIM-TemGNN</td><td>Temporal-aware GNN applied to dynamic similarity networks, benchmark</td></tr></table>

Table 2. Performance Comparison for Credit Risk Prediction Problem

<table><tr><td>Metric</td><td>Method</td><td> $\Psi=14$ </td><td> $\Psi=15$ </td><td> $\Psi=16$ </td><td> $\Psi=17$ </td><td> $\Psi=18$ </td><td> $\Psi=19$ </td><td> $\Psi=20$ </td><td> $\Psi=21$ </td><td> $\Psi=22$ </td><td>Mean</td><td>Std.</td></tr><tr><td rowspan="7">Precision (Q=3,900)</td><td>LSE (our method)</td><td>0.829</td><td>0.837</td><td>0.843</td><td>0.848</td><td>0.851</td><td>0.843</td><td>0.839</td><td>0.841</td><td>0.836</td><td>0.841</td><td>0.006</td></tr><tr><td>RLR</td><td>0.579</td><td>0.573</td><td>0.569</td><td>0.556</td><td>0.581</td><td>0.563</td><td>0.563</td><td>0.566</td><td>0.568</td><td>0.569</td><td>0.008</td></tr><tr><td>MLP</td><td>0.660</td><td>0.677</td><td>0.634</td><td>0.674</td><td>0.693</td><td>0.700</td><td>0.643</td><td>0.664</td><td>0.695</td><td>0.671</td><td>0.023</td></tr><tr><td>SVM</td><td>0.613</td><td>0.624</td><td>0.631</td><td>0.618</td><td>0.627</td><td>0.628</td><td>0.614</td><td>0.612</td><td>0.613</td><td>0.620</td><td>0.008</td></tr><tr><td>XGBoost</td><td>0.770</td><td>0.775</td><td>0.778</td><td>0.775</td><td>0.792</td><td>0.785</td><td>0.771</td><td>0.775</td><td>0.774</td><td>0.777</td><td>0.007</td></tr><tr><td>RNN-GRU</td><td>0.747</td><td>0.752</td><td>0.751</td><td>0.754</td><td>0.757</td><td>0.751</td><td>0.753</td><td>0.747</td><td>0.749</td><td>0.751</td><td>0.003</td></tr><tr><td>SIM-TemGNN</td><td>0.711</td><td>0.734</td><td>0.721</td><td>0.715</td><td>0.724</td><td>0.739</td><td>0.728</td><td>0.717</td><td>0.728</td><td>0.724</td><td>0.009</td></tr><tr><td rowspan="7">Recall (Q=3,900)</td><td>LSE (our method)</td><td>0.810</td><td>0.809</td><td>0.823</td><td>0.852</td><td>0.819</td><td>0.832</td><td>0.842</td><td>0.858</td><td>0.832</td><td>0.831</td><td>0.017</td></tr><tr><td>RLR</td><td>0.566</td><td>0.553</td><td>0.556</td><td>0.559</td><td>0.559</td><td>0.555</td><td>0.565</td><td>0.578</td><td>0.564</td><td>0.562</td><td>0.008</td></tr><tr><td>MLP</td><td>0.644</td><td>0.654</td><td>0.619</td><td>0.678</td><td>0.667</td><td>0.690</td><td>0.645</td><td>0.678</td><td>0.691</td><td>0.663</td><td>0.024</td></tr><tr><td>SVM</td><td>0.598</td><td>0.603</td><td>0.616</td><td>0.622</td><td>0.604</td><td>0.620</td><td>0.616</td><td>0.625</td><td>0.609</td><td>0.612</td><td>0.009</td></tr><tr><td>XGBoost</td><td>0.752</td><td>0.749</td><td>0.760</td><td>0.780</td><td>0.762</td><td>0.775</td><td>0.773</td><td>0.790</td><td>0.770</td><td>0.768</td><td>0.013</td></tr><tr><td>RNN-GRU</td><td>0.729</td><td>0.726</td><td>0.733</td><td>0.758</td><td>0.729</td><td>0.741</td><td>0.755</td><td>0.762</td><td>0.744</td><td>0.742</td><td>0.014</td></tr><tr><td>SIM-TemGNN</td><td>0.694</td><td>0.710</td><td>0.704</td><td>0.719</td><td>0.697</td><td>0.729</td><td>0.730</td><td>0.731</td><td>0.724</td><td>0.715</td><td>0.015</td></tr><tr><td rowspan="7">F1 score (Q=3,900)</td><td>LSE (our method)</td><td>0.819</td><td>0.823</td><td>0.833</td><td>0.850</td><td>0.834</td><td>0.837</td><td>0.841</td><td>0.849</td><td>0.834</td><td>0.840</td><td>0.007</td></tr><tr><td>RLR</td><td>0.572</td><td>0.563</td><td>0.562</td><td>0.558</td><td>0.570</td><td>0.559</td><td>0.564</td><td>0.572</td><td>0.566</td><td>0.564</td><td>0.005</td></tr><tr><td>MLP</td><td>0.652</td><td>0.666</td><td>0.627</td><td>0.676</td><td>0.680</td><td>0.695</td><td>0.644</td><td>0.671</td><td>0.693</td><td>0.669</td><td>0.025</td></tr><tr><td>SVM</td><td>0.605</td><td>0.613</td><td>0.623</td><td>0.620</td><td>0.615</td><td>0.624</td><td>0.615</td><td>0.618</td><td>0.611</td><td>0.618</td><td>0.005</td></tr><tr><td>XGBoost</td><td>0.761</td><td>0.762</td><td>0.769</td><td>0.777</td><td>0.777</td><td>0.780</td><td>0.772</td><td>0.782</td><td>0.772</td><td>0.776</td><td>0.005</td></tr><tr><td>RNN-GRU</td><td>0.738</td><td>0.739</td><td>0.742</td><td>0.756</td><td>0.743</td><td>0.746</td><td>0.754</td><td>0.755</td><td>0.747</td><td>0.749</td><td>0.006</td></tr><tr><td>SIM-TemGNN</td><td>0.703</td><td>0.722</td><td>0.713</td><td>0.717</td><td>0.710</td><td>0.734</td><td>0.729</td><td>0.724</td><td>0.726</td><td>0.722</td><td>0.009</td></tr><tr><td rowspan="7">AUC</td><td>LSE (our method)</td><td>0.931</td><td>0.934</td><td>0.938</td><td>0.944</td><td>0.937</td><td>0.941</td><td>0.943</td><td>0.942</td><td>0.937</td><td>0.939</td><td>0.004</td></tr><tr><td>RLR</td><td>0.752</td><td>0.746</td><td>0.744</td><td>0.747</td><td>0.756</td><td>0.742</td><td>0.752</td><td>0.761</td><td>0.754</td><td>0.750</td><td>0.006</td></tr><tr><td>MLP</td><td>0.806</td><td>0.817</td><td>0.787</td><td>0.829</td><td>0.822</td><td>0.840</td><td>0.804</td><td>0.826</td><td>0.838</td><td>0.819</td><td>0.017</td></tr><tr><td>SVM</td><td>0.770</td><td>0.781</td><td>0.786</td><td>0.790</td><td>0.782</td><td>0.789</td><td>0.787</td><td>0.793</td><td>0.784</td><td>0.785</td><td>0.007</td></tr><tr><td>XGBoost</td><td>0.894</td><td>0.891</td><td>0.896</td><td>0.906</td><td>0.902</td><td>0.909</td><td>0.901</td><td>0.908</td><td>0.899</td><td>0.901</td><td>0.006</td></tr><tr><td>RNN-GRU</td><td>0.880</td><td>0.878</td><td>0.883</td><td>0.893</td><td>0.881</td><td>0.888</td><td>0.890</td><td>0.892</td><td>0.887</td><td>0.886</td><td>0.005</td></tr><tr><td>SIM-TemGNN</td><td>0.855</td><td>0.865</td><td>0.844</td><td>0.852</td><td>0.859</td><td>0.863</td><td>0.849</td><td>0.856</td><td>0.863</td><td>0.856</td><td>0.007</td></tr></table>

## Evaluation Results and Analysis

Following the evaluation procedure, we conducted experiments to evaluate the performance of each method in Table 1 by varying the current billing cycle from Ψ = 14 to Ψ = 22. Given the average number of delinquent users in a billing cycle being 3,932, we set ?? = 3,900 in all experiments. Taking the experiment with Ψ = 14 as an example, in this experiment, each method was trained with users’ observed intrinsic characteristics and delinquency outcomes in billing cycles 2 to 13 to predict each user’s delinquent probability in billing cycle 14; this method predicted that the top 3,900 users with the highest delinquent probabilities would be delinquent.

Table 2 summarizes the performance of the investigated methods and shows that LSE outperforms each benchmark across different evaluation billing cycles in all four performance metrics. Averaged across Ψ, the average precision of LSE is 0.841; that is, on average, 84.1% of the users predicted to be delinquent by our method were truly delinquent. In comparison, the average precision of XGBoost (the best performing benchmark) is 0.777, which is 8.18% lower than that of our method. In addition, LSE surpassed XGBoost by 8.19% in average recall, 8.28% in average F1 score, and 4.20% in average AUC. By applying the paired t-test to the experimental results in Table 2, the performance improvement by LSE over each benchmark in every evaluation metric was shown to be statistically significant (?? < 0.001). The observed performance advantage of our method over the benchmarks can be attributed to its methodological novelty, i.e., our new model of user similarity for credit risk prediction. This is particularly evidenced by the performance improvements of our method over RLR (i.e., 47.87% in average precision, 47.89% in average recall, 48.79% in average F1 score, and 25.06% in average AUC), as our method is largely reduced to RLR if we drop the methodological novelty from it. Therefore, these performance improvements reveal the performance contributions through the methodological novelty of our method. Further, the outperformance of LSE over SIM-TemGNN (i.e., 16.10% in average precision, 16.11% in average recall, 16.32% in average F1 score, and 9.62% in average AUC) also sheds light on the value of latent similarity for credit risk prediction, even when temporal information is explicitly taken into account. Unlike SIM-TemGNN, which relies on observed similarities among users for credit risk prediction, our method is built on both observed and unobserved similarities among users.

Moreover, we conducted an ablation study to empirically investigate the contribution of factors ?? and ?? to the performance of our method. In the ablation study, we dropped only the term involving factor ?? from Equation (1) but kept Equation (3) intact. We called this simplified method without factor ?? LSE-Z. The performance difference between our method LSE and LSE-Z reveals the contribution of factor ?? to the predictive accuracy of our method. Similarly, we dropped only the term involving factor ?? from Equation (1) and referred to the resulting method without factor ?? as LSE-??. We also removed both the term involving factor ?? and the term involving factor ?? from Equation (1) and referred to the resulted method without both factors as LSE-Z-??. We compared the AUC of the four methods for billing cycle Ψ = 14. As reported in Table 3, LSE outperformed LSE-Z by 3.79% due to the consideration of factor ??, surpassed LSE-?? by 2.87% due to the inclusion of factor ??, and exceeded LSE-Z-?? by 10.05% due to the incorporation of both factors.

In addition, we conducted an evaluation by reducing the number of training billing cycles. This allowed us to investigate how the performance benefits of the proposed method would be affected if a bank sought to predict users’ credit risks at an earlier stage and had limited observations of users’ historical behaviors. Averaged across test billing cycles Ψ = 14, 15, . . . , 22, Table 4 presents the average AUC for LSE (our method) and XGBoost (the best-performing benchmark), respectively, with the number of training billing cycles reduced from 12 to 6. As expected, while our method continued to outperform the best-performing benchmark, its performance improvement declined as the number of training billing cycles was reduced. The main advantage of our method lies in leveraging unobserved similarities among users to enhance credit risk prediction. When fewer training billing cycles are employed, less historical data are available for learning unobserved similarities among users. Consequently, it becomes more challenging for our method to effectively learn these unobserved similarities, thereby diminishing the performance advantage of our method. Further analyses in Appendix E showcase the performance of our method across different subgroups of users, illustrate its robustness by varying the values of ??, and demonstrate its effectiveness in reconstructing latent similarities among users. In particular, the subgroup analyses in Appendix E1 indicate that our method is particularly effective in classifying users for whom the similarity component plays a more significant predictive role, as well as those who exhibit strong similarities with a larger number of individuals. These observations align with the rationale of our method. That is, if a user shows strong similarities with a greater number of individuals, our method can harness additional predictive power from the behaviors of these similar counterparts, leading to improved predictive performance.

<table><tr><td colspan="3">Table 3. Ablation Study (Ψ = 14)</td></tr><tr><td>Method</td><td>AUC</td><td>AUC improvement by LSE</td></tr><tr><td>LSE (our method)</td><td>0.931</td><td>-</td></tr><tr><td>LSE-Z</td><td>0.897</td><td>3.79%</td></tr><tr><td>LSE-α</td><td>0.905</td><td>2.87%</td></tr><tr><td>LSE-Z-α</td><td>0.846</td><td>10.05%</td></tr></table>

Table 4. Performance Comparison on Average AUC: Reducing Number of Training Billing Cycles

<table><tr><td># of training billing cycles</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td></tr><tr><td>LSE (our method)</td><td>0.939</td><td>0.938</td><td>0.935</td><td>0.931</td><td>0.928</td><td>0.922</td><td>0.913</td></tr><tr><td>XGBoost</td><td>0.901</td><td>0.902</td><td>0.899</td><td>0.896</td><td>0.897</td><td>0.894</td><td>0.893</td></tr><tr><td>Improvement by LSE</td><td>4.20%</td><td>3.99%</td><td>4.00%</td><td>3.90%</td><td>3.45%</td><td>3.13%</td><td>2.24%</td></tr></table>

![](/api/attachments/V6CQTZQD/fulltext/images/5bbf6942d023a261933b74e19b69966766fcd25ea9bddf11ee03b5351a8a7732.jpg)  
Figure 1. Timeline of Predicted and True Delinquency Outcomes

## Case Study

Having demonstrated the superiority of our method in predicting delinquency outcomes, we now show the economic value generated from its superior predictive power using a case study. Consider the following profit matrix for user $v _ { i } ,$ given the predicted and actual outcomes for the current billing cycle Ψ. Each entry of the matrix $P _ { i , \Psi } ( a , b )$ denotes the profit resulting from predicting the user as outcome $^ { a , }$ while the true outcome is $b$ for billing cycle $\Psi ,$ where $a , b \in \{ 0 , 1 \} ,$ with 0 being “no delinquency” and 1 being “delinquency.” A negative value of $P _ { i , \Psi } ( a , b )$ means cost. Given a method’s prediction and the true outcome for user $v _ { i } ,$ we can derive the profit by the method for $v _ { i }$ from the profit matrix. The overall profit generated from the method is the sum of the individual profits across all users. Next, we define each entry of the profit matrix:

<table><tr><td colspan="3">Profit matrix for user  $v_i$  given prediction for billing cycle  $\Psi$ </td></tr><tr><td></td><td>Actual“no delinquency”</td><td>Actual“delinquency”</td></tr><tr><td>Predict as “no delinquency”</td><td> $P_{i,\Psi}(0,0)$ </td><td> $P_{i,\Psi}(0,1)$ </td></tr><tr><td>Predict as “delinquency”</td><td> $P_{i,\Psi}(1,0)$ </td><td> $P_{i,\Psi}(1,1)$ </td></tr></table>

As shown in Figure 1, a user’s delinquency outcome is predicted at the closing date of the billing cycle, and the true outcome is observed on the payment due date, 21 days after the closing date. Therefore, to specify each entry in the profit matrix, we need to determine the impact of the delinquency outcome prediction over the 21-day period between the billing cycle’s closing date and payment due date. The bank from which we collected data has two primary sources of profit from its credit card business: interchange fees and interest. The former refers to the fee charged by the bank to merchants who process credit card transactions, and the latter is the interest charged by the bank to users who do not pay their bills in full. Following the literature (Elkan, 2001), we measured each entry in the profit matrix against the same baseline, which is the state of the bank before it makes a decision regarding a user. Specifically, if a user is predicted as “delinquency,” the bank will suspend the user’s credit card immediately. As a result, the bank will make no profit but will also suffer no loss from the user compared to the baseline. Thus, we have

$$
P _ {i, \psi} (1, 0) = P _ {i, \psi} (1, 1) = 0.\tag{20}
$$

If a user is predicted as “no delinquency,” the user will be able to use the credit card as usual. Let $A m t _ { i , \Psi }$ denote user $ { \boldsymbol { v } } _ { i } ^ { \prime }$ s credit card spending amount during the 21-day period immediately following the closing date of billing cycle Ψ. Importantly, even if a user is currently non-delinquent, the bank may still incur a loss if the user later becomes a charge-off and permanently fails to repay $A m t _ { i , \Psi } .$ Le $p ^ { L }$ denote the probability that a currently non-delinquent user will eventually become a charge-off. Then, we have

$$
P _ {i, \Psi} (0, 0) = A m t _ {i, \Psi} \times r ^ {f} + A m t _ {i, \Psi} \times r ^ {n} \times (1 - p ^ {L}) - A m t _ {i, \Psi} \times p ^ {L}. (2 1)
$$

Here, $A m t _ { i , \Psi } \times r ^ { f }$ is the interchange fee collected from the merchant, where ${ \mathrm { r } } ^ { \mathrm { f } }$ is the rate of interchange fee. The term $A m t _ { i , \Psi } \times r ^ { n } \times ( 1 - p ^ { L } )$ represents the expected interest income, conditional on the currently non-delinquent user not charging off and eventually repaying $A m t _ { i , \Psi }$ (with probability $1 - p ^ { L } ) . r ^ { n }$ denotes the expected amount of interest earned per dollar of credit card spending. The term $A m t _ { i , \Psi } \times p ^ { L }$ reflects the expected loss due to the future charge-off risk.

Similarly, for users who are currently delinquent, not all will ultimately charge off; some may still repay their overdue amounts in future billing cycles. Accordingly, we define $p ^ { L D }$ as the probability that a currently delinquent user will become a charge-off. As a result, for users predicted to be non-delinquent who become delinquent, we have

$$
P _ {i, \Psi} (0, 1) = A m t _ {i, \Psi} \times r ^ {f} + A m t _ {i, \Psi} \times r ^ {n} \times (1 - p ^ {L D}) - A m t _ {i, \Psi} \times p ^ {L D},\tag{22}
$$

where $A m t _ { i , \Psi } \times r ^ { n } \times ( 1 - p ^ { L D } )$ represents the expected interest income if the delinquent user eventually repays, and $A m t _ { i , \Psi } \times p ^ { L D }$ reflects the expected loss from the potential charge-off. According to the bank, the rate of interchange fee $r ^ { f }$ is 0.45% and the expected amount of interest generated from one dollar of credit card spending $r ^ { n }$ is $\$ 0.0112.$ The probabilities of charge-off for non-delinquent and delinquent users are 0.0046 and 0.0641, respectively; that is, $p ^ { L } = \bar { 0 . 0 0 4 6 }$ and $p ^ { L D } = \ 0 . 0 6 4 1$

Next, we determine the prediction decision based on the expected profit from classifying the user as “no delinquency.” Specifically, because the realized profits $P _ { i , \Psi } ( 0 , 0 )$ and $P _ { i , \Psi } ( 0 , 1 )$ depend on the actual spending $A m t _ { i , \Psi }$ , which has not yet been observed at the moment of decision-making, we instead estimate these profits as follows

$$
\overline {{P}} _ {i} (0, 0) := \overline {{A m t}} _ {i} \times r ^ {f} + \overline {{A m t}} _ {i} \times r ^ {n} \times (1 - p ^ {L}) - \overline {{A m t}} _ {i} \times p ^ {L},
$$

and

$$
\overline {{P}} _ {i} (0, 1) := \overline {{A m t}} _ {i} \times r ^ {f} + \overline {{A m t}} _ {i} \times r ^ {n} \times (1 - p ^ {L D}) - \overline {{A m t}} _ {i} \times p ^ {L D},
$$

where $\overline { { A m t } } _ { i }$ is the average spending of user $v _ { i }$ across several historical 21-day grace periods. Given the predicted delinquency probability $p _ { i , \Psi } ,$ , the expected profit of classifying the user as non-delinquent is computed as

$$
\left(1 - p _ {i, \Psi}\right) \times \overline {{P}} _ {i} (0, 0) + p _ {i, \Psi} \times \overline {{P}} _ {i} (0, 1).
$$

If this expected profit is positive, the user is classified as $\ " \mathrm { \sim } \mathrm { n o }$ delinquency” and allowed to continue using the card; otherwise, the user is classified as “delinquency” and their card is suspended.

Once decisions have been made for all users, the total realized profit is computed as the sum of $\cdot _ { P _ { i , \Psi } ( a , b ) }$ over all users $v _ { i } .$ . Table 5 reports the profit generated by each method for billing cycle $\Psi =$ 14. As reported, the profit of LSE is \$70,581, which surpasses that of XGBoost (the best performing benchmark) by 19.95% and that of RLR (the worst performing benchmark) by 120.33%. The results for other billing cycles are qualitatively similar.

## Evaluation Results for Multiclass and Numerical Credit Risk Prediction Problems

For the multiclass credit risk prediction problem, we considered a case of three credit risk outcomes: user v<sub>i</sub> being delinquent in billing cycle ?? (failing to pay the minimum payment due), user $v _ { i }$ being non-delinquent in billing cycle ?? but only making a partial payment, or user $v _ { i }$ being non-delinquent in billing cycle ?? and paying off their statement balance. Accordingly, we set $y _ { i , t } = 2 ,$

1, and 0 for these three outcomes, respectively. Averaged across 22 billing cycles in our data, 33.43% of the users (or 3,932 users) were delinquent, 11.17% of the users (or 1,314 users) were nondelinquent with partial payment, and 55.39% of the users (or 6,515 users) were non-delinquent with full payment. We still used user $\vec { v _ { i } \textrm { s } }$ billing and demographic information in billing cycle ?? to construct $\mathbf { x } _ { i , t } ,$ , as described in the Data and Evaluation Procedure subection.

The evaluation procedure for multiclass credit risk prediction is similar to that for binary credit risk prediction described in the Data and Evaluation Procedure subection. Let $\Psi$ be current billing cycle. We constructed the training data using users’ observed intrinsic characteristics $\mathbf { x } _ { i , t }$ and multiclass credit risk outcomes $y _ { i , t }$ in each of the previous 12 billing cycles ??, $t \ =$ $\Psi - 1 2 , \cdot \cdot \cdot , \Psi - 1$ . Using the training data, we trained our method and each benchmark method to predict probability $p _ { i , k , \Psi }$ for every user in billing cycle Ψ based on the user’s observed intrinsic characteristics $\mathbf { x } _ { i , \Psi } .$ , where $p _ { i , k , \Psi }$ denotes the probability that the credit risk outcome of user $v _ { i }$ in billing cycle Ψ is ?? $( k =$ 0,1,2). User $v _ { i }$ was then predicted to be the credit risk outcome associated with the highest predicted probability. The performance of a method was evaluated by comparing its predicted credit risk outcome against the true credit risk outcome for each user in billing cycle Ψ with commonly used multiclass classification metrics: accuracy, macro precision, macro recall and macro F1 score (Stab & Gurevych, 2014; Narasimhan et al., 2016). Here, accuracy is the percentage of correctly classified users. To compute the other metrics, we first calculated the binary precision, recall, and F1 score for each credit risk outcome by treating the outcome as positive and the rest of the outcomes as negative. Macro precision, recall, and F1 score are the average of binary precisions, binary recalls, and binary F1 scores across all the credit risk outcomes, respectively.

For the multiclass credit risk prediction case, we tuned hyperparameters for each method with $\Psi = 1 3 ;$ we report their performance from Ψ = 14 to Ψ = 22 in Table $6 . ^ { 8 }$ As shown in the table, our method significantly outperformed each benchmark method across billing cycles in each evaluation metric $( p <$ 0.001). For example, averaged across Ψ, the mean accuracy of LSE was 0.805. That is, on average, 80.5% of credit risk outcomes predicted by our method turned out to be true, outperforming RLR and XGBoost by 18.16% and 4.67%, respectively. The superiority of our method reported in Table 6 further confirms the value of our methodological novelty.

<table><tr><td colspan="3">Table 5. Profit Generated by Each Method (Ψ = 14)</td></tr><tr><td>Method</td><td>Profit</td><td>Improvement by LSE</td></tr><tr><td>LSE (our method)</td><td>$70,581</td><td>-</td></tr><tr><td>RLR</td><td>$32,034</td><td>120.33%</td></tr><tr><td>MLP</td><td>$37,311</td><td>89.17%</td></tr><tr><td>SVM</td><td>$35,919</td><td>96.50%</td></tr><tr><td>XGBoost</td><td>$58,844</td><td>19.95%</td></tr><tr><td>RNN-GRU</td><td>$49,407</td><td>42.86%</td></tr><tr><td>SIM-TemGNN</td><td>$40,158</td><td>75.76%</td></tr></table>

Table 6. Evaluation Results for Multiclass Credit Risk Prediction

<table><tr><td>Metric</td><td>Method</td><td> $\Psi=14$ </td><td> $\Psi=15$ </td><td> $\Psi=16$ </td><td> $\Psi=17$ </td><td> $\Psi=18$ </td><td> $\Psi=19$ </td><td> $\Psi=20$ </td><td> $\Psi=21$ </td><td> $\Psi=22$ </td><td>Mean</td><td>Std.</td></tr><tr><td rowspan="7">Accuracy</td><td>LSE (our method)</td><td>0.800</td><td>0.804</td><td>0.799</td><td>0.805</td><td>0.809</td><td>0.812</td><td>0.810</td><td>0.808</td><td>0.801</td><td>0.805</td><td>0.005</td></tr><tr><td>RLR</td><td>0.671</td><td>0.682</td><td>0.675</td><td>0.680</td><td>0.692</td><td>0.688</td><td>0.687</td><td>0.682</td><td>0.677</td><td>0.682</td><td>0.007</td></tr><tr><td>MLP</td><td>0.713</td><td>0.726</td><td>0.709</td><td>0.724</td><td>0.728</td><td>0.734</td><td>0.741</td><td>0.733</td><td>0.721</td><td>0.725</td><td>0.010</td></tr><tr><td>SVM</td><td>0.664</td><td>0.683</td><td>0.666</td><td>0.672</td><td>0.678</td><td>0.674</td><td>0.682</td><td>0.688</td><td>0.670</td><td>0.675</td><td>0.008</td></tr><tr><td>XGBoost</td><td>0.757</td><td>0.763</td><td>0.767</td><td>0.770</td><td>0.775</td><td>0.780</td><td>0.782</td><td>0.765</td><td>0.766</td><td>0.769</td><td>0.008</td></tr><tr><td>RNN-GRU</td><td>0.747</td><td>0.754</td><td>0.750</td><td>0.758</td><td>0.757</td><td>0.760</td><td>0.756</td><td>0.752</td><td>0.753</td><td>0.754</td><td>0.004</td></tr><tr><td>SIM-TemGNN</td><td>0.723</td><td>0.737</td><td>0.741</td><td>0.731</td><td>0.719</td><td>0.738</td><td>0.732</td><td>0.736</td><td>0.732</td><td>0.732</td><td>0.007</td></tr><tr><td rowspan="7">Macro Precision</td><td>LSE (our method)</td><td>0.742</td><td>0.749</td><td>0.745</td><td>0.754</td><td>0.763</td><td>0.764</td><td>0.770</td><td>0.766</td><td>0.759</td><td>0.757</td><td>0.010</td></tr><tr><td>RLR</td><td>0.577</td><td>0.600</td><td>0.601</td><td>0.590</td><td>0.609</td><td>0.603</td><td>0.595</td><td>0.609</td><td>0.602</td><td>0.598</td><td>0.010</td></tr><tr><td>MLP</td><td>0.464</td><td>0.481</td><td>0.465</td><td>0.474</td><td>0.490</td><td>0.488</td><td>0.489</td><td>0.479</td><td>0.476</td><td>0.478</td><td>0.010</td></tr><tr><td>SVM</td><td>0.571</td><td>0.580</td><td>0.579</td><td>0.564</td><td>0.595</td><td>0.571</td><td>0.596</td><td>0.601</td><td>0.572</td><td>0.581</td><td>0.013</td></tr><tr><td>XGBoost</td><td>0.703</td><td>0.687</td><td>0.692</td><td>0.688</td><td>0.697</td><td>0.673</td><td>0.707</td><td>0.675</td><td>0.688</td><td>0.690</td><td>0.011</td></tr><tr><td>RNN-GRU</td><td>0.502</td><td>0.497</td><td>0.497</td><td>0.495</td><td>0.500</td><td>0.498</td><td>0.497</td><td>0.498</td><td>0.490</td><td>0.497</td><td>0.003</td></tr><tr><td>SIM-TemGNN</td><td>0.475</td><td>0.487</td><td>0.486</td><td>0.480</td><td>0.472</td><td>0.485</td><td>0.476</td><td>0.480</td><td>0.481</td><td>0.480</td><td>0.005</td></tr><tr><td rowspan="7">Macro Recall</td><td>LSE (our method)</td><td>0.682</td><td>0.709</td><td>0.703</td><td>0.715</td><td>0.708</td><td>0.702</td><td>0.705</td><td>0.715</td><td>0.705</td><td>0.705</td><td>0.010</td></tr><tr><td>RLR</td><td>0.486</td><td>0.504</td><td>0.499</td><td>0.496</td><td>0.510</td><td>0.506</td><td>0.519</td><td>0.522</td><td>0.501</td><td>0.505</td><td>0.011</td></tr><tr><td>MLP</td><td>0.518</td><td>0.523</td><td>0.519</td><td>0.521</td><td>0.528</td><td>0.530</td><td>0.534</td><td>0.538</td><td>0.523</td><td>0.526</td><td>0.007</td></tr><tr><td>SVM</td><td>0.476</td><td>0.491</td><td>0.470</td><td>0.473</td><td>0.493</td><td>0.483</td><td>0.494</td><td>0.514</td><td>0.482</td><td>0.487</td><td>0.013</td></tr><tr><td>XGBoost</td><td>0.624</td><td>0.631</td><td>0.632</td><td>0.645</td><td>0.640</td><td>0.651</td><td>0.653</td><td>0.631</td><td>0.624</td><td>0.637</td><td>0.011</td></tr><tr><td>RNN-GRU</td><td>0.546</td><td>0.549</td><td>0.551</td><td>0.554</td><td>0.558</td><td>0.555</td><td>0.549</td><td>0.556</td><td>0.551</td><td>0.552</td><td>0.004</td></tr><tr><td>SIM-TemGNN</td><td>0.527</td><td>0.536</td><td>0.545</td><td>0.533</td><td>0.526</td><td>0.536</td><td>0.529</td><td>0.541</td><td>0.534</td><td>0.534</td><td>0.006</td></tr><tr><td rowspan="7">Macro F1 Score</td><td>LSE (our method)</td><td>0.693</td><td>0.721</td><td>0.717</td><td>0.729</td><td>0.725</td><td>0.718</td><td>0.721</td><td>0.725</td><td>0.721</td><td>0.693</td><td>0.010</td></tr><tr><td>RLR</td><td>0.485</td><td>0.511</td><td>0.503</td><td>0.499</td><td>0.507</td><td>0.507</td><td>0.517</td><td>0.512</td><td>0.503</td><td>0.505</td><td>0.009</td></tr><tr><td>MLP</td><td>0.489</td><td>0.498</td><td>0.490</td><td>0.495</td><td>0.503</td><td>0.506</td><td>0.509</td><td>0.506</td><td>0.497</td><td>0.499</td><td>0.007</td></tr><tr><td>SVM</td><td>0.470</td><td>0.488</td><td>0.453</td><td>0.465</td><td>0.488</td><td>0.479</td><td>0.495</td><td>0.516</td><td>0.481</td><td>0.482</td><td>0.018</td></tr><tr><td>XGBoost</td><td>0.643</td><td>0.648</td><td>0.649</td><td>0.659</td><td>0.657</td><td>0.659</td><td>0.670</td><td>0.643</td><td>0.639</td><td>0.652</td><td>0.010</td></tr><tr><td>RNN-GRU</td><td>0.521</td><td>0.521</td><td>0.521</td><td>0.523</td><td>0.527</td><td>0.525</td><td>0.522</td><td>0.523</td><td>0.519</td><td>0.522</td><td>0.002</td></tr><tr><td>SIM-TemGNN</td><td>0.499</td><td>0.509</td><td>0.513</td><td>0.505</td><td>0.497</td><td>0.509</td><td>0.501</td><td>0.509</td><td>0.506</td><td>0.505</td><td>0.005</td></tr></table>

Table 7. Evaluation Results for Numerical Credit Risk Prediction

<table><tr><td>Metric</td><td>Method</td><td> $\Psi=14$ </td><td> $\Psi=15$ </td><td> $\Psi=16$ </td><td> $\Psi=17$ </td><td> $\Psi=18$ </td><td> $\Psi=19$ </td><td> $\Psi=20$ </td><td> $\Psi=21$ </td><td> $\Psi=22$ </td><td>Mean</td><td>Std.</td></tr><tr><td rowspan="7">MAE</td><td>LSE (our method)</td><td>0.187</td><td>0.179</td><td>0.182</td><td>0.177</td><td>0.183</td><td>0.180</td><td>0.176</td><td>0.183</td><td>0.185</td><td>0.181</td><td>0.004</td></tr><tr><td>RLR</td><td>0.358</td><td>0.360</td><td>0.359</td><td>0.359</td><td>0.357</td><td>0.359</td><td>0.359</td><td>0.361</td><td>0.367</td><td>0.360</td><td>0.003</td></tr><tr><td>MLP</td><td>0.329</td><td>0.335</td><td>0.318</td><td>0.320</td><td>0.331</td><td>0.327</td><td>0.321</td><td>0.343</td><td>0.334</td><td>0.329</td><td>0.008</td></tr><tr><td>SVM</td><td>0.305</td><td>0.298</td><td>0.291</td><td>0.293</td><td>0.290</td><td>0.294</td><td>0.307</td><td>0.309</td><td>0.302</td><td>0.299</td><td>0.007</td></tr><tr><td>XGBoost</td><td>0.230</td><td>0.221</td><td>0.232</td><td>0.230</td><td>0.226</td><td>0.221</td><td>0.219</td><td>0.224</td><td>0.229</td><td>0.226</td><td>0.005</td></tr><tr><td>RNN-GRU</td><td>0.403</td><td>0.396</td><td>0.414</td><td>0.403</td><td>0.408</td><td>0.398</td><td>0.417</td><td>0.403</td><td>0.407</td><td>0.405</td><td>0.007</td></tr><tr><td>SIM-TemGNN</td><td>0.403</td><td>0.441</td><td>0.436</td><td>0.428</td><td>0.435</td><td>0.444</td><td>0.438</td><td>0.427</td><td>0.439</td><td>0.435</td><td>0.006</td></tr></table>

For the numerical credit risk prediction problem, we considered a case of predicting the repayment rate (or the proportion of repaid statement balance). In this case, we still used each user’s billing and demographic information in every billing cycle to construct $\mathbf { x } _ { i , t }$ but set $y _ { i , t }$ as the user’s repayment rate in the billing cycle. The average repayment rate in our data set was 0.617. Like before, we used training data in the previous 12 billing cycles to train each method to predict repayment rate $\mu _ { i , \Psi }$ for every user in current billing cycle Ψ. The performance of a method is measured using the mean absolute error (MAE), a widely adopted metric for numerical predictions (e.g., Yang et al., 2019):

$$
\mathrm{MAE} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left| \mu_ {i, \Psi} - y _ {i, \Psi} \right|,
$$

where $\mu _ { i , \Psi }$ and $y _ { i , \Psi }$ denote user $\vec { v _ { i } } \mathbf { \bar { s } }$ predicted and actual repayment rate in billing cycle Ψ, respectively, and ?? is the number of users. Since RLR and SVM are designed for classification, we employed their respective regression version: ridge regression (RR) (Hastie et al., 2009, p. 61) and support vector regression (SVR) (Smola & Schölkopf, 2004), to predict the numerical repayment rate. The other benchmark methods are also applicable to regression problems. We tuned hyperparameters for each method with $\Psi = 1 3$ and conducted experiments to compare their performance from Ψ = 14 to $\Psi = 2 2 . ^ { 9 }$ As shown in Table 7 above, LSE significantly outperformed each benchmark method in terms of MAE $( p < 0 . 0 0 1 )$ . The average MAE of LSE was 0.181, which is lower than that of the benchmark methods by a range between 19.66% and 58.25%.

## Conclusion

Our study belongs to the computational genre of design science research, which is concerned with developing computational methods to solve business and societal problems and seeks to make methodological contributions (Rai, 2017; Padmanabhan et al., 2022). In particular, our study solves the problem of credit risk prediction and adds the following methodological contributions to the extant literature. First, we proposed a novel latent similarityenhanced credit risk prediction model, which operationalizes the similarity between a pair of users as a combination of the observed and latent similarities between them. In contrast, prior research on similarity-based credit risk prediction has solely employed observed similarity. Second, we developed a new method that estimates the model parameters, learns latent similarities among users, and predicts users’ probabilities of delinquency. Premised in our derived propositions and theorem, the method is computationally efficient and guaranteed to converge. Thus, it is particularly suitable for solving real-world credit risk prediction problems with a large number of users. In addition, we extended our model and method to the multiclass and numerical credit risk prediction problems. Consequently, our developed methods can solve a broad spectrum of credit risk prediction problems.

Our study offers several implications for business. First, our proposed method allows financial institutions to conduct credit risk prediction beyond the use of users’ intrinsic data. This is realized through the similarity component of our method. As a result, the predictive power of our method substantially outperforms that of credit risk prediction methods widely used in the industry, such as RLR, as demonstrated in our empirical evaluation. The improved predictive power offered by our method can enable financial institutions to more accurately pinpoint risky users and prevent losses while better serving creditworthy users and increasing profits. As we show in a case study (see Case Study subsection), our method produced 120.33% more profit than RLR, the industry standard for credit risk prediction (Thomas et al., 2017), and 19.95% more profit than XGBoost, a popular credit risk prediction method used by financial institutions. Considering the enormous size of the consumer credit market, the effective use of our method could potentially generate considerably higher profits for financial institutions, compared to standard methods currently used in the industry. In addition, our method also benefits creditworthy users. By differentiating risky users from creditworthy users more accurately, our method reduces the chance of creditworthy users being misclassified as risky users, thereby providing creditworthy users with broader access to consumer credit. It is worth noting that the performance advantage of our method over the benchmarks stems from our novel model of user similarity for credit risk prediction. This underscores the predictive power of similar users’ repayment behaviors in evaluating a focal user’s credit risk. In other words, the repayment behaviors of users who have a high degree of similarity with a focal user could function as predictors for the focal user’s credit risk. Thus, credit risk analysts could assess a user’s credit status by analyzing the credit status of the user’s similar peers, in addition to examining the user’s own behavioral repayment data. In addition, our study equips financial institutions with tools that can predict credit risks at a more refined level. The multiclass credit risk prediction method allows practitioners to further divide non-delinquent users into more business-relevant subgroups.

This could be useful, as the repayment behaviors of nondelinquent users are not homogeneous. For example, some users pay the full statement balance and incur no interest charges, while others merely pay the minimum due and accrue interest. The numerical credit risk prediction method can enable practitioners to predict individualized credit risk indicators such as repayment rate and future spending amount. Armed with these useful indicators, financial institutions could design personalized services for their users, such as deciding whether to increase the credit limit for a user and, if so, how much to increase it. Moreover, the proposed method could be applied to other business domains. For example, it could be extended to support personalized marketing. The objective of this task is to predict customers’ future spending behaviors (e.g., spending amount) and design individualized marketing strategies (e.g., incentives) for each customer based on the predictions. Understandably, the spending behaviors of a customer’s similar peers could function as predictors for the customer’s spending behavior. Therefore, our method could improve the effectiveness of the prediction by considering not only a customer’s past spending behaviors but also the spending behaviors of the customer’s similar peers.

Our study could be extended in several directions. First, we developed a linear credit risk prediction model that considers similarities among users. It would be interesting to investigate how to incorporate the similarity component into a nonlinear model for credit risk prediction, such as a neural network model. Second, future work could extend our method to the application scoring problem, where no historical data are available to learn latent similarities. One viable approach to addressing this challenge would be transfer learning, which would learn a latent similarity model using users’ historical data collected from other domains (e.g., spending data on e-commerce platforms) and adapt the model to the domain of credit risk prediction. Third, our method considers the number of historical delinquencies but overlooks the sequential information of historical delinquencies. Future work could integrate this information into our method to further improve its performance.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the three anonymous reviewers for their valuable guidance and constructive feedback, which have greatly improved the paper. W. Qian and X. Fang are the corresponding authors of this paper. W. Qian acknowledges partial support from NSF DMS-2413833 and DE-INBRE/NIH P20GM103446.

## References

Altman, E. I., Resti, A. C., & Sironi, A. (2005). Recovery risk: The next challenge in credit risk management. Risk Books.

Atkinson, T., Luttrell, D., & Rosenblum, H. (2013). How bad was it? The costs and consequences of the 2007-09 financial crisis (Staff Papers, No. 20, July 2013). Federal Reserve Bank of Dallas.

Babaev, D., Savchenko, M., Tuzhilin, A., & Umerenkov, D. (2019). E.T.-RNN: Applying deep learning to credit loan applications. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 2183-2190). https://doi.org/10.1145/3292500.3330693

Baesens, B., Van Gestel, T., Viaene, S., Stepanova, M., Suykens, J., & Vanthienen, J. (2003). Benchmarking state-of-the-art classification algorithms for credit scoring. Journal of the Operational Research Society, 54(6), 627-635. https://doi.org/10.1057/palgrave.jors. 2601545

Bertsekas, D. P. (1999). Nonlinear programming (2nd ed.). Athena Scientific.

Breiman, L. (1996). Bagging predictors. Machine Learning, 24(2), 123-140. https://doi.org/10.1007/BF00058655

Burges, C. J. (1998). A tutorial on support vector machines for pattern recognition. Data Mining and Knowledge Discovery, 2(2), 121- 167. https://doi.org/10.1023/A:1009715923555

Cessie, S. L., & Houwelingen, J. V. (1992). Ridge estimators in logistic regression. Journal of the Royal Statistical Society Series C: Applied Statistics, 41(1), 191-201. https://doi.org/10.2307/2347628

Chatterjee, S., Corbae, D., Nakajima, M., & Ríos‐Rull, J. V. (2007). A quantitative theory of unsecured consumer credit with risk of default. Econometrica, 75(6), 1525-1589. https://doi.org/10.1111 j.1468-0262.2007.00806.x

Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785- 794). https://doi.org/10.1145/2939672.2939785

Chen, Y. (2023). Machine learning and optimization with latent variables [Unpublished doctoral dissertation]. Princeton University.

Cox, J. (2021). Household debt rises to \$14.6 trillion due to recordbreaking rise in mortgage loans. CNBC. https://www.cnbc.com/ 2021/02/17/household-debt-rises-to-14point6-trillion-due-torecord-breaking-rise-in-mortgage-loans

De Almeida Filho, A. T., Mues, C., & Thomas, L. C. (2010). Optimizing the collections process in consumer credit. Production and Operations Management, 19(6), 698-708. https://doi.org/ 10.1111/j.1937-5956.2010.01152.x

Elkan, C. (2001). The foundations of cost-sensitive learning. In Proceedings of 17th International Joint Conference on Artificial Intelligence (pp. 973-978).

Fang, X., Hu, P. J. H., Li, Z., & Tsai, W. (2013). Predicting adoption probabilities in social networks. Information Systems Research, 24(1), 128-145. https://doi.org/10.1287/isre.1120.0461

Fernandes, G. B., & Artes, R. (2016). Spatial dependence in credit risk and its improvement in credit scoring. European Journal of Operational Research, 249(2), 517-524. https://doi.org/10.1016 j.ejor.2015.07.013

Freund, Y., & Schapire, R. E. (1997). A decision-theoretic generalization of on-line learning and an application to boosting. Journal of Computer and System Sciences, 55(1), 119-139. https://doi.org/10.1006/jcss.1997.1504

Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. The Annals of Statistics, 29(5), 1189-1232. https://doi.org/10.1214/aos/1013203451

Giudici, P., Hadji-Misheva, B., & Spelta, A. (2019). Network based credit risk models. Quality Engineering, 32(2), 199-211. https://doi.org/10.1080/08982112.2019.1655159

Goodfellow, I., Bengio, Y., Courville, A., & Bengio, Y. (2016). Deep learning. MIT Press.

Guo, Y., Zhou, W., Luo, C., Liu, C., & Xiong, H. (2016). Instancebased credit risk assessment for investment decisions in P2P lending. European Journal of Operational Research, 249(2), 417- 426. https://doi.org/10.1016/j.ejor.2015.05.050

Hand, D. J. (2001). Modelling consumer credit risk. IMA Journal of Management Mathematics, 12(2), 139-155. https://doi.org 10.1093/imaman/12.2.139

Hand, D. J., & Henley, W. E. (1997). Statistical classification methods in consumer credit scoring: a review. Journal of the Royal Statistical Society: Series A (Statistics in Society), 160(3), 523-541. https://doi.org/10.1111/j.1467-985X.1997.00078.x

Hand, D. J., & Vinciotti, V. (2003). Choosing k for two-class nearest neighbour classifiers with unbalanced classes. Pattern Recognition Letters, 24(9-10), 1555-1562. https://doi.org/10.1016/S0167- 8655(02)00394-X

Hastie, T., Mazumder, R., Lee, J. D., & Zadeh, R. (2015). Matrix completion and low-rank SVD via fast alternating least squares. The Journal of Machine Learning Research, 16(1), 3367-3402.

Hastie, T., Tibshirani, R., Friedman, J., & Franklin, J. (2009). The elements of statistical learning: data mining, inference and prediction (2nd ed.). Springer. https://doi.org/10.1007/978-0-387- 84858-7

Henley, W., & Hand, D. J. (1996). A k-nearest-neighbour classifier for assessing consumer credit risk. Journal of the Royal Statistical Society: Series D (The Statistician), 45(1), 77-95. https://doi.org/ 10.2307/2348414

Horymski, C. (2025). What is the average number of credit cards? Experian. https://www.experian.com/blogs/ask-experian/averagenumber-of-credit-cards-a-person-has

Kennedy, K., Namee, B. M., & Delany, S. J. (2013). Using semisupervised classifiers for credit scoring. Journal of the Operational Research Society, 64(4), 513-529. https://doi.org/10.1057/ jors.2011.30

Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via machine-learning algorithms. Journal of Banking & Finance, 34(11), 2767-2787. https://doi.org/10.1016/j.jbankfin. 2010.06.001

Kipf, T. N., & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. In Proceedings of the 5th International Conference on Learning.

Lee, J. W., Lee, W. K., & Sohn, S. Y. (2021). Graph convolutional network-based credit default prediction utilizing three types of virtual distances among borrowers. Expert Systems with Applications, 168, Article 114411. https://doi.org/10.1016/j.eswa. 2020.114411

Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015). Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research. European Journal of Operational Research, 247(1), 124-136. https://doi.org/10.1016/j.ejor.2015. 05.030

Lu, T., Zhang, Y., & Li, B. (2023). Profit vs. equality? The case of financial risk assessment and a new perspective on alternative data. MIS Quarterly, 47(4), 1517-1556. https://doi.org/10.25300 MISQ/2023/17330

Malhotra, R., & Malhotra, D. K. (2003). Evaluating consumer loans using neural networks. Omega, 31(2), 83-96. https://doi.org/ 10.1016/S0305-0483(03)00016-1

McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather: Homophily in social networks. Annual Review of Sociology, 27(1), 415-444. https://doi.org/10.1146/annurev. soc.27.1.415

Medina-Olivares, V., Calabrese, R., Dong, Y., & Shi, B. (2022). Spatial dependence in microfinance credit default. International Journal of Forecasting, 38(3), 1071-1085. https://doi.org/10.1016/ j.ijforecast.2021.05.009

Menon, A. K., & Elkan, C. (2011). Link prediction via matrix factorization. In Proceedings of the European Conference on Machine Learning and Knowledge Discovery in Databases (pp. 437-452). https://doi.org/10.1007/978-3-642-23783-6\_28

Miller, K., Jordan, M., & Griffiths, T. (2009). Nonparametric latent feature models for link prediction. In Proceedings of the 23rd International Conference on Neural Information Processing Systems (pp. 1276-1284).

Narasimhan, H., Pan, W., Kar, P., Protopapas, P., & Ramaswamy, H. G. (2016). Optimizing the multiclass F-measure via biconcave programming. In Proceedings of the 16th International Conference on Data Mining (pp. 1101-1106). https://doi.org 10.1109/ICDM.2016.0143

Nocedal, J., & Wright, S. J. (2006). Numerical optimization (2nd ed.). Springer.

Padmanabhan, B., Fang, X., Sahoo, N., & Burton-Jones, A. (2022). Editor’s comments: Machine learning in information systems research. MIS Quarterly, 46(1), iii-xix. https://doi.org/10.25300/ MISQ/2022/461E1

Paleologo, G., Elisseeff, A., & Antonini, G. (2010). Subagging for credit scoring models. European Journal of Operational Research, 201(2), 490-499. https://doi.org/10.1016/j.ejor.2009.03.008

Press, W., Teukolsky, S., Vetterling, W., & Flannery, B. (2007). Numerical recipes: The art of scientific computing (3rd ed.). Cambridge University Press.

Rai, A. (2017). Editor’s comments: Diversity of design science research. MIS Quarterly, 41(1), iii-xviii.

Sinha, A. P., & May, J. H. (2004). Evaluating and tuning predictive data mining models using receiver operating characteristic curves. Journal of Management Information Systems, 21(3), 249-280. https://doi.org/10.1080/07421222.2004.11045815

Smola, A. J., & Schölkopf, B. (2004). A tutorial on support vector regression. Statistics and Computing, 14(3), 199-222. https://doi.org/10.1023/b:stco.0000035301.49549.88

Stab, C., & Gurevych, I. (2014). Identifying argumentative discourse structures in persuasive essays. In Proceedings of the Conference on Empirical Methods in Natural Language Processing (pp. 46- 56). https://doi.org/10.3115/v1/D14-1006

Stolba, S. L. (2019). How do credit card companies make money? Experian. https://www.experian.com/blogs/ask-experian/how-docredit-card-companies-make-money/

Thomas, L., Crook, J., & Edelman, D. (2017). Credit scoring and its applications (2nd ed.). Society for Industrial and Applied Mathematics.

Thomas, L. C. (2000). A survey of credit and behavioural scoring: forecasting financial risk of lending to consumers. International Journal of Forecasting, 16(2), 149-172. https://doi.org/10.1016/ S0169-2070(00)00034-0

Twala, B. (2010). Multiple classifier application to credit risk assessment. Expert Systems with Applications, 37(4), 3326-3336. https://doi.org/10.1016/j.eswa.2009.10.018

Varin, C., Reid, N., & Firth, D. (2011). An overview of composite likelihood methods. Statistica Sinica, 21(1), 5-42.

Wang, D., Zhang, Z., Zhou, J., Cui, P., Fang, J., Jia, Q., Fang, Y., & Qi, Y. (2021). Temporal-aware graph neural network for credit risk prediction. In Proceedings of the SIAM International Conference on Data Mining (pp. 702-710). https://doi.org/10.1137/ 1.9781611976700.79

West, D., Dellana, S., & Qian, J. (2005). Neural network ensemble strategies for financial decision applications. Computers & Operations Research, 32(10), 2543-2559. https://doi.org/10.1016/ j.cor.2004.03.017

Xu, J., Wang, J., Zhou, Z., & Lu, T. (2025). Toward graph data collaboration in a data-sharing-free manner: A novel privacypreserving graph pretraining model. INFORMS Journal on Computing, 38(2), 676-691. https://doi.org/10.1287/ijoc.2023.0115

Xu, J., Yang, Y., Pu, S., Fu, Y., Feng, J., Jiang, W., Lu, J., & Wang, C. (2023). Netrl: Task-aware network denoising via deep reinforcement learning. IEEE Transactions on Knowledge and Data Engineering, 35(1), 810-823. https://doi.org/10.1109/ tkde.2021.3091022

Yang, M., Zheng, Z., & Mookerjee, V. (2019). Prescribing response strategies to manage customer opinions: A stochastic differential equation approach. Information Systems Research, 30(2), 351-374. https://doi.org/10.1287/isre.2018.0805

Yao, X., Crook, J., & Andreeva, G. (2015). Support vector regression for loss given default modelling. European Journal of Operational Research, 240(2), 528-538. https://doi.org/10.1016/j.ejor.2014. 06.043

## About the Authors

Hongzhe Zhang is an assistant professor in information systems at the Chinese University of Hong Kong, Shenzhen. He received his Ph.D. in financial services analytics from the Alfred Lerner College of Business & Economics, University of Delaware. Prior to that, he earned his B.Sc. in mathematics from Xiamen University and his M.Sc. in statistics from Rutgers University. His research focuses on addressing important problems in financial technology, privacypreserving AI, and recommender systems by designing novel machine learning algorithms and methods. ORCiD: 0000-0002- 0541-1285

Wei Qian received his Ph.D. degree in statistics from the University of Minnesota in 2014. He joined the School of Mathematics and Statistics at Rochester Institute of Technology as an assistant professor in the same year and then moved to the Department of Applied Economics and Statistics at the University of Delaware in 2017, where he has been an associate professor since 2021. His research interests include high-dimensional statistics, model selection, dimension reduction, statistical computing, deep learning, reinforcement learning, and data science applications. He also serves as a JPMC Fellow and affiliated member of the Institute of Financial Services Analytics at the University of Delaware. ORCiD: 0000-0003-1022-1141

Xiao Fang is a professor of MIS and JPMorgan Chase Senior Fellow at the Lerner College of Business & Economics and the Institute for Financial Services Analytics, University of Delaware. His current research focuses on GenAI, financial technology, and healthcare analytics, with methods and tools drawn from reference disciplines including management science (e.g., optimization) and computer science (e.g., machine learning). He has published in Information Systems journals, including MIS Quarterly, Information Systems Research, Management Science, and Operations Research, as well as computer science outlets such as ACM Transactions on Information Systems and IEEE Transactions on Knowledge and Data Engineering. ORCiD: 0000-0002-9429-5748

## Appendix A

## Derivations of Equations (4), (5), and (7)

## A1. Derivation of Equation (4)

For the convenience of reading, we repeat notations defined in the Objective Function subsection: $\pmb { \theta } = ( \theta _ { 1 } , \cdot \cdot \cdot , \theta _ { n } ) ^ { T } , X = ( \mathbf { x } _ { 1 } , \cdot \cdot \cdot , \mathbf { x } _ { n } ) ^ { T } , \pmb { c } =$ $( c _ { 1 } , \cdot \cdot \cdot , c _ { n } ) ^ { T } , C = \operatorname { d i a g } ( c )$ , and $G = [ s _ { i j } ] _ { n \times n } .$ , where diagonal elements in ?? are defined to be 0. By the model of $\dot { \theta } _ { i }$ in Equation (3), we have

$$
\theta_ {i} = \pmb {x} _ {i} ^ {T} \pmb {\beta} + c _ {i} \sum_ {v _ {j} \in V: j \neq i} s _ {i j} \theta_ {j}.
$$

Let $\mathbf { e } _ { i }$ denote a standard unit vector with its $i ^ { t h }$ element being 1 and other elements being 0. It is easy to see that $\mathbf { \boldsymbol { \theta } } _ { i } = \mathbf { e } _ { i } ^ { T } \mathbf { \boldsymbol { \theta } }$ . Therefore, we have

$$
\begin{array}{r l} & {\theta_ {i} = \pmb {e} _ {i} ^ {T} \pmb {\theta} = \pmb {x} _ {i} ^ {T} \pmb {\beta} + c _ {i} \sum_ {v _ {j} \in V: j \neq i} s _ {i j} \theta_ {j}} \\ & {\quad = \pmb {x} _ {i} ^ {T} \pmb {\beta} + c _ {i} (s _ {i 1}, \dots , s _ {i (i - 1)}, 0, s _ {i (i + 1)}, \dots , s _ {i n}) \pmb {\theta}} \\ & {\quad = \pmb {x} _ {i} ^ {T} \pmb {\beta} + c _ {i} \pmb {e} _ {i} ^ {T} G \pmb {\theta}} \\ & {\quad = \pmb {e} _ {i} ^ {T} X \pmb {\beta} + \pmb {e} _ {i} ^ {T} C G \pmb {\theta}} \\ & {\quad = \pmb {e} _ {i} ^ {T} (X \pmb {\beta} + C G \pmb {\theta}).} \end{array}
$$

Equation (4) follows immediately. ∎

## A2. Derivation of Equation (5)

We use the notation in Appendix A.1 as well as $Z = ( \mathbf { z } _ { 1 } , \cdot \cdot \cdot , \mathbf { z } _ { n } ) ^ { T } , \pmb { \alpha } = ( \alpha _ { 1 } , \cdot \cdot \cdot , \alpha _ { n } ) ^ { T }$ . With the definition of $G = [ s _ { i j } ] _ { n \times n } ,$ it can be seen that $s _ { i j } = \mathbf { e } _ { i } ^ { T } G \mathbf { e } _ { j }$ . By Equation (1), we have

$$
\begin{array}{r l} & {s _ {i j} = \pmb {e} _ {i} ^ {T} G \pmb {e} _ {j} = \alpha_ {i} + \alpha_ {j} + \widetilde {\pmb {x}} _ {i} ^ {T} \widetilde {\pmb {x}} _ {j} + \pmb {z} _ {i} ^ {T} \pmb {z} _ {j}} \\ & {\qquad = \pmb {e} _ {i} ^ {T} \pmb {\alpha} + \pmb {\alpha} ^ {T} \pmb {e} _ {j} + \pmb {e} _ {i} ^ {T} \tilde {X} \tilde {X} ^ {T} \pmb {e} _ {j} + \pmb {e} _ {i} ^ {T} Z Z ^ {T} \pmb {e} _ {j}} \\ & {\qquad = \pmb {e} _ {i} ^ {T} \pmb {1} _ {n} \pmb {\alpha} ^ {T} \pmb {e} _ {j} + \pmb {e} _ {i} ^ {T} \pmb {\alpha} \pmb {1} _ {n} ^ {T} \pmb {e} _ {j} + \pmb {e} _ {i} ^ {T} \tilde {X} \tilde {X} ^ {T} \pmb {e} _ {j} + \pmb {e} _ {i} ^ {T} Z Z ^ {T} \pmb {e} _ {j}} \\ & {\qquad = \pmb {e} ^ {T} \big (\pmb {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \pmb {1} _ {n} ^ {T} + \bar {X} \bar {\tilde {X}} ^ {T} + Z Z ^ {T} \big) \pmb {e} _ {j},} \end{array}
$$

where $\mathbf { 1 } _ { n } \in \mathbb { R } ^ { n }$ is an all-ones vector.

Recall that the diagonal elements of ?? are defined to be 0. Specifically, the $i ^ { t h }$ diagonal element of ?? is given by

$$
\begin{array}{r l r} & & {\mathbf {e} _ {i} ^ {T} \big (\mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} + \tilde {X} \tilde {X} ^ {T} + Z Z ^ {T} \big) \mathbf {e} _ {i}} \\ & & {= \pmb {\alpha} ^ {T} \mathbf {e} _ {i} + \mathbf {e} _ {i} ^ {T} \pmb {\alpha} + \mathbf {e} _ {i} ^ {T} \tilde {X} \tilde {X} ^ {T} \mathbf {e} _ {i} + \mathbf {e} _ {i} ^ {T} Z Z ^ {T} \mathbf {e} _ {i}} \\ & & {= 2 \alpha_ {i} + \tilde {\mathbf {x}} _ {i} ^ {T} \tilde {\mathbf {x}} _ {i} + \mathbf {z} _ {i} ^ {T} \mathbf {z} _ {i}.} \end{array}
$$

To make the diagonal elements of ?? being 0, we have

$$
G = \mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} + \tilde {X} \tilde {X} ^ {T} + Z Z ^ {T} - 2 d i a g (\pmb {\alpha}) - \sum_ {i = 1} ^ {n} (\widetilde {\pmb {x}} _ {i} ^ {T} \widetilde {\pmb {x}} _ {i} + \pmb {z} _ {i} ^ {T} \pmb {z} _ {i}) \pmb {e} _ {i} \pmb {e} _ {i} ^ {T}.
$$

This completes the derivation of Equation (5). ∎

## A3. Derivation of the Negative Log-likelihood Function (7)

Given a training data set of users’ observed characteristics and their delinquency outcomes $\{ \mathbf { x } _ { i } , y _ { i } \} _ { i = 1 } ^ { n } ,$ , we have

$$
\begin{array}{r l} & h (\pmb {\beta}, Z, \pmb {\alpha}, \pmb {c}) = - \frac {1}{n} \log \left(\prod_ {i = 1} ^ {n} p _ {i} ^ {y _ {i}} (1 - p _ {i}) ^ {(1 - y _ {i})}\right) \\ & \qquad = - \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} \log (p _ {i}) + (1 - y _ {i}) \log (1 - p _ {i}) \\ & \qquad = - \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} \log \frac {p _ {i}}{1 - p _ {i}} + \log (1 - p _ {i}). \end{array}
$$

Recall that $\begin{array} { r } { \theta _ { i } = \log \frac { p _ { i } } { 1 - p _ { i } } } \end{array}$ and we have

$$
\begin{array}{r} h (\pmb {\beta}, Z, \pmb {\alpha}, \pmb {c}) = \frac {1}{n} \sum_ {i = 1} ^ {n} - y _ {i} \theta_ {i} - l o g (1 - \frac {e ^ {\theta_ {i}}}{1 + e ^ {\theta_ {i}}}) \\ = \frac {1}{n} \sum_ {i = 1} ^ {n} - y _ {i} \theta_ {i} + l o g (1 + e ^ {\theta_ {i}}). \end{array}
$$

This completes the derivation of the negative log-likelihood function (7). ∎

## Appendix B

## Proof of Propositions 1, 2 and Theorem 1

## B1. Proof of Proposition 1

We first derive the derivatives of matrix $M ^ { - 1 }$ with respect to parameters $z _ { i j } , \alpha _ { i } ,$ and $c _ { i } ,$ , where ?? is defined in Equation (6). These derivatives will then be used in the derivation of the gradients in Proposition 1.

$$
\begin{array}{r l} & {\frac {\partial M ^ {- 1}}{\partial z _ {i j}} = - M ^ {- 1} \frac {\partial M}{\partial z _ {i j}} M ^ {- 1} = - M ^ {- 1} \frac {\partial (E _ {n} - C G)}{\partial z _ {i j}} M ^ {- 1} = - M ^ {- 1} \left[ - C \frac {\partial G}{\partial z _ {i j}} \right] M ^ {- 1}} \\ & {\quad = M ^ {- 1} C \frac {\partial (\mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} - 2 d i a g (\pmb {\alpha}) + \bar {X} \bar {X} ^ {T} + Z Z ^ {T} - \sum_ {l = 1} ^ {n} (\widetilde {\pmb {x}} _ {l} ^ {T} \widetilde {\pmb {x}} _ {l} + \pmb {z} _ {l} ^ {T} \pmb {z} _ {l}) \pmb {e} _ {i} \pmb {e} _ {l} ^ {T})}{\partial z _ {i j}} M ^ {- 1}} \\ & {\quad = M ^ {- 1} C \frac {\partial (Z Z ^ {T} - \sum_ {\bar {l} = 1} ^ {n} (\pmb {z} _ {\bar {l}} ^ {T} \pmb {z} _ {\bar {l}}) \pmb {e} _ {\bar {i}} \pmb {e} _ {\bar {l}} ^ {T})}{\partial z _ {i j}} M ^ {- 1}} \\ & {\quad = M ^ {- 1} C (Z \frac {\partial Z ^ {T}}{\partial z _ {i j}} + \frac {\partial Z}{\partial z _ {i j}} Z ^ {T} - \frac {\partial \pmb {z} _ {i} ^ {T} \pmb {z} _ {i}}{\partial z _ {i j}} \pmb {e} _ {i} \pmb {e} _ {i} ^ {T}) M ^ {- 1}} \\ & {\quad = M ^ {- 1} C (Z (\pmb {e} _ {i} \pmb {e} _ {j} ^ {T}) ^ {T} + (\pmb {e} _ {i} \pmb {e} _ {j} ^ {T}) Z ^ {T} - \frac {\partial (\sum_ {j = 1} ^ {d} z _ {i j} ^ {2})}{\partial z _ {i j}} \pmb {e} _ {i} \pmb {e} _ {i} ^ {T}) M ^ {- 1}} \\ & {\quad = M ^ {- 1} C (Z \pmb {e} _ {j} \pmb {e} _ {i} ^ {T} + \pmb {e} _ {i} (Z \pmb {e} _ {j}) ^ {T} - 2 z _ {i j} \pmb {e} _ {i} \pmb {e} _ {i} ^ {T}) M ^ {- 1}.} \end{array}\tag{A1}
$$

$$
\begin{array}{r l} & {\frac {\partial M ^ {- 1}}{\partial \alpha_ {i}} = - M ^ {- 1} \frac {\partial M}{\partial \alpha_ {i}} M ^ {- 1} = - M ^ {- 1} \frac {\partial (E _ {n} - C G)}{\partial \alpha_ {i}} M ^ {- 1} = - M ^ {- 1} \left(- C \frac {\partial G}{\partial \alpha_ {i}}\right) M ^ {- 1}} \\ & {\quad = M ^ {- 1} C \frac {\partial (\mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {a} \mathbf {1} _ {n} ^ {T} - 2 d i a g (\pmb {\alpha}) + \tilde {X} \tilde {X} ^ {T} + Z Z ^ {T} - \sum_ {i = 1} ^ {n} (\widetilde {x} _ {i} ^ {T} \widetilde {x} _ {i} + z _ {i} ^ {T} z _ {i}) \pmb {e} _ {i} \pmb {e} _ {i} ^ {T})}{\partial \alpha_ {i}} M ^ {- 1}} \\ & {\quad = M ^ {- 1} C \frac {\partial (\mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} - 2 d i a g (\pmb {\alpha}))}{\partial \alpha_ {i}} M ^ {- 1}} \\ & {\quad = M ^ {- 1} C (\mathbf {1} _ {n} \pmb {e} _ {i} ^ {T} + \pmb {e} _ {i} \mathbf {1} _ {n} ^ {T} - 2 \pmb {e} _ {i} \pmb {e} _ {i} ^ {T}) M ^ {- 1}.} \end{array}\tag{A2}
$$

$$
\begin{array}{r l} & {\frac {\partial M ^ {- 1}}{\partial c _ {i}} = - M ^ {- 1} \frac {\partial M}{\partial c _ {i}} M ^ {- 1} = - M ^ {- 1} \frac {\partial (E _ {n} - C G)}{\partial c _ {i}} M ^ {- 1} = - M ^ {- 1} \left(- \frac {\partial C}{\partial c _ {i}} G\right) M ^ {- 1}} \\ & {\qquad = M ^ {- 1} \frac {\partial d i a g (\pmb {c})}{\partial c _ {i}} G M ^ {- 1}} \\ & {\qquad = M ^ {- 1} (\pmb {e} _ {i} \pmb {e} _ {i} ^ {T} G) M ^ {- 1}.} \end{array}\tag{A3}
$$

We also derive the partial derivative of the negative log-likelihood h defined in Equation (7) with respect to $\theta _ { i }$ as follows:

$$
\begin{array}{c} \frac {\partial h}{\partial \theta_ {i}} = \frac {\partial \left(\frac {1}{n} \sum_ {i = 1} ^ {n} - y _ {i} \theta_ {i} + \log \left(1 + e ^ {\theta_ {i}}\right)\right)}{\partial \theta_ {i}} \\ = \frac {1}{n} \left(- y _ {i} + \frac {1}{1 + e ^ {- \theta_ {i}}}\right). \end{array}
$$

Denoting $\begin{array} { r } { \pi ( \theta _ { i } ) = \frac { 1 } { 1 + e ^ { - \theta _ { i } } } , } \end{array}$ we obtain

$$
\frac {\partial h}{\partial \pmb {\theta}} = \frac {1}{n} (- \pmb {y} + \pmb {\pi} _ {\theta}),\tag{A4}
$$

where $\pmb { y } = ( y _ { 1 } , \dots , y _ { n } ) ^ { T }$ and $\pmb { \pi } _ { \pmb { \theta } } = ( \pi ( \theta _ { 1 } ) , \dots , \pi ( \theta _ { n } ) ) ^ { T }$

Given Equations (A1), (A4), (6) and (8), we have

$$
\begin{array}{l} \frac {\partial q}{\partial z _ {i j}} = \frac {\partial h}{\partial z _ {i j}} + \lambda_ {Z} z _ {i j} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial \pmb {\theta}}{\partial z _ {i j}} + \lambda_ {Z} z _ {i j} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial (M ^ {- 1} X \pmb {\beta})}{\partial z _ {i j}} + \lambda_ {Z} z _ {i j} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial M ^ {- 1}}{\partial z _ {i j}} X \pmb {\beta} + \lambda_ {Z} z _ {i j} \\ = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C \big (Z \mathbf {e} _ {j} \mathbf {e} _ {i} ^ {T} + \mathbf {e} _ {i} (Z \mathbf {e} _ {j}) ^ {T} - 2 z _ {i j} \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T} \big) M ^ {- 1} X \pmb {\beta} + \lambda_ {Z} z _ {i j} \\ = \Big (\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C Z \mathbf {e} _ {j} \Big) (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) + (\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C \mathbf {e} _ {i}) ((Z \mathbf {e} _ {j}) ^ {T} M ^ {- 1} X \pmb {\beta}) \\ - 2 z _ {i j} \left(\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C \mathbf {e} _ {i}\right) (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) + \lambda_ {Z} z _ {i j} \\ = (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C Z \mathbf {e} _ {j}\right) + (\mathbf {e} _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z \mathbf {e} _ {j}) \\ - 2 z _ {i j} (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) (\mathbf {e} _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}) + \lambda_ {Z} z _ {i j} \\ = \mathbf {e} _ {i} ^ {T} (M ^ {- 1} X \pmb {\beta} \frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C Z) \mathbf {e} _ {j} + \mathbf {e} _ {i} ^ {T} (C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}} \pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z) \mathbf {e} _ {j} \\ - 2 (\mathbf {e} _ {i} ^ {T} Z \mathbf {e} _ {j}) (\mathbf {e} _ {i} ^ {T} ((M ^ {- 1} X \pmb {\beta}) \odot ((C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}})) \mathbf {1} _ d d e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f e f f, \\ = (\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}\partial p m a x y i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o v i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o w i n s t r a c l o u n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i n d i u n d i n d i n d i u n d i n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i u n d i v e r b e r g. \\ = (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial \pmb {\theta}} M ^ {- 1}) (X, Y) + (\frac {\partial h}{\partial p m a x y i n s t r a c l O W}) (X, Y) + (\frac {\partial h}{\partial p m a x y i n s t r a c l O W}) (X, Y) + (\frac {\partial h}{\partial p m a x y i n s t r a c l O W}) (X, Y) + (\frac {\partial h}{\partial p m a x y i n s t r a c l O W}) (X, Y) + (\frac {}{)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, Y)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, Z)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, X)} {(X, I)}{(x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , x , } \\ = (- 2 (\texttt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J | J |J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|J|
$$

which immediately implies that

$$
\begin{array}{c} \frac {\partial q}{\partial Z} = (M ^ {- 1} X \boldsymbol {\beta}) \left(\frac {\partial h}{\partial \boldsymbol {\theta} ^ {T}} M ^ {- 1} C Z\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}\right) (\boldsymbol {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z) \\ - 2 Z \odot \left((M ^ {- 1} X \boldsymbol {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}\right) \mathbf {1} _ {d} ^ {T}\right) + \lambda_ {Z} Z. \end{array}
$$

Employing Equations (A2), (A4), (6) and (8), we have

$$
\begin{array}{r l} & {\frac {\partial q}{\partial \alpha_ {i}} = \frac {\partial h}{\partial \alpha_ {i}} + \lambda_ {\alpha} \alpha_ {i} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial \pmb {\theta}}{\partial \alpha_ {i}} + \lambda_ {\alpha} \alpha_ {i} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial (M ^ {- 1} X \pmb {\beta})}{\partial \alpha_ {i}} + \lambda_ {\alpha} \alpha_ {i} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial M ^ {- 1}}{\partial \alpha_ {i}} X \pmb {\beta} + \lambda_ {\alpha} \alpha_ {i}} \\ & {\quad = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C (\mathbf {1} _ {n} e _ {i} ^ {T} + e _ {i} \mathbf {1} _ {n} ^ {T} - 2 e _ {i} e _ {i} ^ {T}) M ^ {- 1} X \pmb {\beta} + \lambda_ {\alpha} \alpha_ {i}} \\ & {\quad = (e _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + (e _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n})} \\ & {\quad - 2 (e _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) \left(e _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}\right) + \lambda_ {\alpha} \alpha_ {i}} \\ & {\quad = e _ {i} ^ {T} (M ^ {- 1} X \pmb {\beta}) \left(\frac {\partial h}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + e _ {i} ^ {T} (C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}) (\pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n})} \\ & {\quad - 2 e _ {i} ^ {T} (M ^ {- 1} X \pmb {\beta} \odot C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \pmb {\theta}}) + \lambda_ {\alpha} e _ {i} ^ {T} \pmb {\alpha},} \end{array}
$$

which immediately implies that

$$
\begin{array}{c} \frac {\partial q}{\partial \boldsymbol {\alpha}} = (M ^ {- 1} X \boldsymbol {\beta}) \left(\frac {\partial h}{\partial \boldsymbol {\theta} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}\right) (\boldsymbol {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ - 2 (M ^ {- 1} X \boldsymbol {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}\right) + \lambda_ {\boldsymbol {\alpha}} \boldsymbol {\alpha}. \end{array}
$$

Armed with Equations (A3), (A4), (6) and (8), we have

$$
\begin{array}{l} \frac {\partial q}{\partial c _ {i}} = \frac {\partial h}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \frac {\partial h}{\partial \boldsymbol {\theta} ^ {T}} \frac {\partial \boldsymbol {\theta}}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \frac {\partial h}{\partial \boldsymbol {\theta} ^ {T}} \frac {\partial (M ^ {- 1} X \boldsymbol {\beta})}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \frac {\partial h}{\partial \boldsymbol {\theta} ^ {T}} \frac {\partial M ^ {- 1}}{\partial c _ {i}} X \boldsymbol {\beta} + \lambda_ {c} c _ {i} \\ = \frac {\partial h}{\partial \boldsymbol {\theta} ^ {T}} (M ^ {- 1} \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T} G M ^ {- 1}) X \boldsymbol {\beta} + \lambda_ {c} c _ {i} \\ = (\mathbf {e} _ {i} ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}) (\mathbf {e} _ {i} ^ {T} G M ^ {- 1} X \boldsymbol {\beta}) + \lambda_ {c} c _ {i} \\ = \mathbf {e} _ {i} ^ {T} \left(\left((M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}\right) \odot (G M ^ {- 1} X \boldsymbol {\beta})\right) + \lambda_ {c} \mathbf {e} _ {i} ^ {T} \mathbf {c}, \end{array}
$$

which immediately implies that

$$
\frac {\partial q}{\partial \boldsymbol {c}} = \left((M ^ {- 1}) ^ {T} \frac {\partial h}{\partial \boldsymbol {\theta}}\right) \odot (G M ^ {- 1} X \beta) + \lambda_ {c} \boldsymbol {c}.
$$

Given Equations (A4), (6) and (8), we have

$$
\begin{array}{r l} & {\frac {\partial q}{\partial \beta_ {p}} = \frac {\partial h}{\partial \beta_ {p}} + \lambda_ {\beta} \beta_ {p}} \\ & {\quad = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial \pmb {\theta}}{\partial \beta_ {p}} + \lambda_ {\beta} \beta_ {p} = \frac {\partial h}{\partial \pmb {\theta} ^ {T}} \frac {\partial (M ^ {- 1} X \pmb {\beta})}{\partial \beta_ {p}} + \lambda_ {\beta} \beta_ {p} = \frac {\partial l}{\partial \pmb {\theta} ^ {T}} M ^ {- 1} X \mathbf {e} _ {p} + \lambda_ {\beta} \pmb {\beta} ^ {T} \mathbf {e} _ {p}} \\ & {\quad = \mathbf {e} _ {p} ^ {T} \Big (X ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial l}{\partial \pmb {\theta}} + \lambda_ {\beta} \pmb {\beta} \Big),} \end{array}
$$

which immediately implies that

$$
\frac {\partial q}{\partial \pmb {\beta}} = X ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial l}{\partial \pmb {\theta}} + \lambda_ {\pmb {\beta}} \pmb {\beta}.
$$

This completes the proof. ∎

## B2. Proof of Proposition 2

Define $\begin{array} { r } { D _ { n } = E _ { n } + C ( 2 \mathrm { d i a g } ( \boldsymbol { \alpha } ) + \sum _ { i = 1 } ^ { n } \left( \tilde { \mathbf { x } } _ { i } ^ { T } \tilde { \mathbf { x } } _ { i } + \mathbf { z } _ { i } ^ { T } \mathbf { z } _ { i } \right) \mathbf { e } _ { i } \mathbf { e } _ { i } ^ { T } ) , Q _ { 1 } = \left( \mathbf { 1 } _ { n } , \boldsymbol { \alpha } , \tilde { X } , Z \right) } \end{array}$ , and $Q _ { 2 } = ( \pmb { \alpha } , \mathbf { 1 } _ { n } , \tilde { X } , Z )$ . By the definition of ?? in Equation (6) and the expression of ?? in Equation (5), we have

$$
\begin{array}{l} M = E _ {n} - C G \\ \qquad = E _ {n} - C (\mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} - 2 \mathrm{diag} (\pmb {\alpha}) + \tilde {X} \tilde {X} ^ {T} + Z Z ^ {T} - \sum_ {i = 1} ^ {n} (\tilde {\mathbf {x}} _ {i} ^ {T} \tilde {\mathbf {x}} _ {i} + \mathbf {z} _ {i} ^ {T} \mathbf {z} _ {i}) \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T}) \\ \qquad = E _ {n} + C \left(2 \mathrm{diag} (\pmb {\alpha}) + \sum_ {i = 1} ^ {n} (\tilde {\mathbf {x}} _ {i} ^ {T} \tilde {\mathbf {x}} _ {i} + \mathbf {z} _ {i} ^ {T} \mathbf {z} _ {i}) \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T}\right) - C (\mathbf {1} _ {n} \pmb {\alpha} ^ {T} + \pmb {\alpha} \mathbf {1} _ {n} ^ {T} + \tilde {X} \tilde {X} ^ {T} + Z Z ^ {T}) \\ \qquad = E _ {n} + C \left(2 \mathrm{diag} (\pmb {\alpha}) + \sum_ {i = 1} ^ {n} (\tilde {\mathbf {x}} _ {i} ^ {T} \tilde {\mathbf {x}} _ {i} + \mathbf {z} _ {i} ^ {T} \mathbf {z} _ {i)} \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T}\right) - C (\mathbf {1} _ {n}, \pmb {\alpha}, \tilde {X}, Z) (\pmb {\alpha}, \mathbf {1} _ {n}, \tilde {X}, Z) ^ {T} \\ \qquad = D _ {n} - C Q _ {1} Q _ {2} ^ {T}. \end{array}
$$

This completes the proof of Proposition 2. ∎

## B3. Proof of Theorem 1

To prove the convergence of Algorithm 1, we first show that each iteration of the algorithm does not increase the objective (Equation 8); that is

$$
q \big (\widehat {\pmb {\beta}} ^ {(r)}, \widehat {Z} ^ {(r)}, \widehat {\pmb {\alpha}} ^ {(r)}, \widehat {\pmb {c}} ^ {(r)} \big) \geq q \big (\widehat {\pmb {\beta}} ^ {(r + 1)}, \widehat {Z} ^ {(r + 1)}, \widehat {\pmb {\alpha}} ^ {(r + 1)}, \widehat {\pmb {c}} ^ {(r + 1)} \big).\tag{A5}
$$

Recall that each iteration of the algorithm consists of four minimization steps, each of which updates estimations for one subset of parameters while fixing the others. These minimization steps are implemented using gradient descent with the Armijo rule, which ensures that the objective (Equation 8) keeps going downhill after each minimization step. Therefore, we have

$$
\begin{array}{r l} & q \big (\widehat {\pmb {\beta}} ^ {(r)}, \hat {Z} ^ {(r)}, \widehat {\pmb {\alpha}} ^ {(r)}, \widehat {\pmb {c}} ^ {(r)} \big) \geq q \big (\widehat {\pmb {\beta}} ^ {(r)}, \hat {Z} ^ {(r + 1)}, \widehat {\pmb {\alpha}} ^ {(r)}, \widehat {\pmb {c}} ^ {(r)} \big) \\ & \qquad \geq q (\widehat {\pmb {\beta}} ^ {(r)}, \hat {Z} ^ {(r + 1)}, \widehat {\pmb {\alpha}} ^ {(r + 1)}, \widehat {\pmb {c}} ^ {(r)}) \\ & \qquad \geq q (\widehat {\pmb {\beta}} ^ {(r)}, \hat {Z} ^ {(r + 1)}, \widehat {\pmb {\alpha}} ^ {(r + 1)}, \widehat {\pmb {c}} ^ {(r + 1)}) \\ & \qquad \geq q \big (\widehat {\pmb {\beta}} ^ {(r + 1)}, \hat {Z} ^ {(r + 1)}, \widehat {\pmb {\alpha}} ^ {(r + 1)}, \widehat {\pmb {c}} ^ {(r + 1)} \big). \end{array}
$$

Furthermore, the objective (Equation 8) is defined as

$$
q (\boldsymbol {\beta}, Z, \boldsymbol {\alpha}, \boldsymbol {c}) = h (\boldsymbol {\beta}, Z, \boldsymbol {\alpha}, \boldsymbol {c}) + \frac {\lambda_ {z}}{2} \| Z \| _ {F} ^ {2} + \frac {\lambda_ {\alpha}}{2} \| \boldsymbol {\alpha} \| _ {2} ^ {2} + \frac {\lambda_ {c}}{2} \| \boldsymbol {c} \| _ {2} ^ {2} + \frac {\lambda_ {\beta}}{2} \| \boldsymbol {\beta} \| _ {2} ^ {2},
$$

where the negative log-likelihood function $h ( \beta , Z , \alpha , c ) \ge 0$ and and $\lambda _ { z } , \lambda _ { \alpha } , \lambda _ { c } ,$ , and $\lambda _ { \beta }$ are positive hyper-parameters. It immediately implies $q ( \beta , Z , \alpha , c ) \geq 0$ . Since Algorithm 1 monotonically decreases the lower-bounded objective (Equation 8), it is guaranteed to converge. ∎

## Appendix C

## Multiclass Credit Risk Prediction Problem

## C1. Derivation of Equation (12)

Given a training data set of users’ observed characteristics and their multiclass credit risk outcomes $\{ \mathbf { x } _ { i } , y _ { i } \} , y _ { i } \in \{ 0 , 1 , \dotsc , K \} , i \ =$ $1 , 2 , \ldots , n ,$ , we have

$$
\begin{array}{r} h ^ {m} \big (\pmb {\beta} _ {\{1: K \}}, Z, \pmb {\alpha}, \pmb {c} \big) = - \frac {1}{n} \log \left(\prod_ {i = 1} ^ {n} p _ {k, i} ^ {\delta_ {k, i}}\right) \\ = - \frac {1}{n} \sum_ {i = 1} ^ {n} \sum_ {k = 0} ^ {K} \delta_ {k, i} \log p _ {k, i}, \end{array}\tag{A6}
$$

where $p _ { k , i }$ is the probability that user $v _ { i }$ belongs to credit risk outcome ?? and $\delta _ { k , i } = 1$ if $y _ { i } = k$ and $\delta _ { k , i } = ~ 0$ otherwise.

Recall that $\theta _ { k , i } = \log \frac { p _ { k , i } } { p _ { 0 , i } }$ and $\begin{array} { r } { \sum _ { k = 0 } ^ { K } p _ { k , i } = 1 } \end{array}$ . Therefore, we have

$$
p _ {0, i} = \frac {1}{1 + \sum_ {\widetilde {k} = 1} ^ {K} e ^ {\theta_ {\widetilde {k} , i}}}, \qquad p _ {k, i} = \frac {e ^ {\theta_ {k , i}}}{1 + \sum_ {\widetilde {k} = 1} ^ {K} e ^ {\theta_ {\widetilde {k} , i}}}, \qquad k = 1, \ldots , K.\tag{A7}
$$

Substitute the expressions of the probabilities in Equation (A7) into Equation (A6), we have

$$
\begin{array}{c} h ^ {m} \big (\boldsymbol {\beta} _ {\{1: K \}}, Z, \boldsymbol {\alpha}, \boldsymbol {c} \big) = - \frac {1}{n} \sum_ {i = 1} ^ {n} \left(- \delta_ {0, i} \log \left(1 + \sum_ {k = 1} ^ {K} e ^ {\theta_ {\widetilde {k}, i}}\right) + \sum_ {k = 1} ^ {K} \left(\delta_ {k, i} \theta_ {k, i} - \delta_ {k, i} \log \left(1 + \sum_ {k = 1} ^ {K} e ^ {\theta_ {\widetilde {k}, i}}\right)\right)\right) \\ = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\left(\sum_ {k = 1} ^ {K} - \delta_ {k, i} \theta_ {k, i}\right) + \left(\sum_ {k = 0} ^ {K} \delta_ {k, i}\right) \log (1 + \sum_ {k = 1} ^ {K} e ^ {\theta_ {\widetilde {k}, i}})\right). \end{array}
$$

Noting that $\begin{array} { r } { \sum _ { k = 0 } ^ { K } \delta _ { k , i } = 1 } \end{array}$ and replacing $\tilde { k }$ with ??, we immediately have

$$
h ^ {m} \left(\boldsymbol {\beta} _ {\{1: K \}}, Z, \boldsymbol {\alpha}, \boldsymbol {c}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\left(\sum_ {k = 1} ^ {K} - \delta_ {k, i} \theta_ {k, i}\right) + \log \left(1 + \sum_ {k = 1} ^ {K} e ^ {\theta_ {k, i}}\right)\right).
$$

## C2. Parameter Estimation for the Multiclass Credit Risk Prediction Problem

```txt
Input: ε: convergence threshold, ε > 0
{xi, yi}ni=1: training data
Output: β{1:K}, Z, α, c: parameter estimations
1: r = 0. // r: iteration count
2: Initialize Z(r), α(r), c(r), β(r){1:K}.
3: Compute qm,(r) = qm(β(r){1:K}, Z(r), α(r), c(r)) according to Equation (13).
4: repeat
5:    Z(r+1) = arg minZ qm(β(r){1:K}, Z, α(r), c(r)).
6:    α(r+1) = arg minα qm(β(r){1:K}, Z(r+1), α, c(r)).
7:    c(r+1) = arg minc qm(β(r){1:K}, Z(r+1), α(r+1), c).
8:    β(r+1){1:K} = arg minβ{1:K} qm(β{1:K}, Z(r+1), α(r+1), c(r+1)).
9:    Compute qm,(r+1) = qm(β(r+1){1:K}, Z(r+1), α(r+1), c(r+1)) according to Equation (13).
10:    r = r + 1.
11: until |qm,(r) - qm,(r-1)| < ε.
12: return (β{1:K}, Z, α, c) = (β(r){1:K}, Z(r), α(r), c(r)).
```

Algorithm C1. An Alternating Minimization Algorithm for Parameter Estimation (Multiclass Case)

## C3. Proof of Proposition 4

We first derive the partial derivative of $h ^ { m }$ (defined in Equation 12) with respect to $\theta _ { k , i } \colon$

$$
\begin{array}{c} \frac {\partial h ^ {m}}{\partial \theta_ {k , i}} = \frac {\partial \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \left(\left(\sum_ {\bar {k} = 1} ^ {K} - \delta_ {\bar {k} , i} \theta_ {\bar {k} , i}\right) + \log \left(1 + \sum_ {\bar {k} = 1} ^ {K} e ^ {\theta_ {\bar {k} , i}}\right)\right)\right)}{\partial \theta_ {k , i}} \\ = \frac {1}{n} \left(- \delta_ {k, i} + \frac {e ^ {\theta_ {k , i}}}{1 + \sum_ {\bar {k} = 1} ^ {K} e ^ {\theta_ {\bar {k} , i}}}\right). \end{array}
$$

Define $\pmb { \delta } _ { k } = ( \delta _ { k , 1 } , \ldots , \delta _ { k , n } ) ^ { T } , \pmb { \pi } _ { k } ^ { m } = ( \pi _ { k , 1 } ^ { m } , \ldots , \pi _ { k , n } ^ { m } ) ^ { T }$ , and $\begin{array} { r } { \pi _ { k , i } ^ { m } = \frac { e ^ { \theta _ { k , i } } } { 1 + \sum _ { \tilde { k } = 1 } ^ { K } e ^ { \theta _ { \widetilde { k } , i } } } . } \end{array}$ We have

$$
\frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} = \frac {1}{n} (- \pmb {\delta} _ {k} + \pmb {\pi} _ {k} ^ {m}).\tag{A8}
$$

Given Equations (A1), (A8), (11) and (13), we have

$$
\begin{array} { r l } &  \frac { \partial q ^ { m } } { \partial z _ { i j } } = \frac { \partial h ^ { m } } { \partial z _ { i j } } + \lambda _ { Z } z _ { i j } = \sum _ { k = 1 } ^ { K } \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } \frac { \partial \pmb { \theta } _ { k } } { \partial z _ { i j } } + \lambda _ { Z } z _ { i j } = \sum _ { k = 1 } ^ { K } \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } \frac { \partial ( M ^ { - 1 } X \pmb { \beta } _ { k } ) } { \partial z _ { i j } } + \lambda _ { Z } z _ { i j } = \sum _ { k = 1 } ^ { K } \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } \frac { \partial M ^ { - 1 } } { \partial z _ { i j } } X \pmb { \beta } _ { k } + \lambda _ { Z } z _ { i j } \\ &  = \sum _ { k = 1 } ^ { K } \left[ \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } M ^ { - 1 } C ( Z _ { j } \pmb { e } _ { i } ^ { T } + \pmb { e } _ { i } Z _ { j } ^ { T } - 2 z _ { i j } \pmb { e } _ { i } \pmb { e } _ { i } ^ { T } ) M ^ { - 1 } X \pmb { \beta } _ { k } \right] + \lambda _ { Z } z _ { i j } \\ &  = \sum _ { k = 1 } ^ { K } [ ( \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } M ^ { - 1 } C Z _ { j } ) ( \pmb { e } _ { i } ^ { T } M ^ { - 1 } X \pmb { \beta } _ { k } ) + ( \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } M ^ { - 1 } C \pmb { e } _ { i } ) ( Z _ { j } ^ { T } M ^ { - 1 } X \pmb { \beta } _ { k } ) \\ &  - 2 z _ { i j } ( \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } M ^ { - 1 } C \pmb { e } _ { i } ) ( \pmb { e } _ { i } ^ { T } M ^ { - 1 } X \pmb { \beta } _ { k} ) ] + \lambda _ { Z } z _ { i j } \\ &  = \sum _ { k = 1 } ^ { K } [ ( \pmb { e } _ { i } ^ { T } M ^ { - 1 } X \pmb { \beta } _ { k } ) ( \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T } } M ^ { - 1 } C Z \pmb { e } _ { j } ) + ( \pmb { e } _ { i } ^ { T } C ( M ^ { - 1 } ) ^ { T } \frac { \partial h ^ { m } }  \partial \pmb { \theta } _ { k } ) ( \pmb { \beta } _ { k } ^ { T } X ^ { T } ( M ^ { - 1 } ) ^ { T } Z \pmb { e } _ { j} ) \\ &  - 2 z _ { i j } ( \pmb { e } _ { i } ^ { T} M ^ { - 1 } X \pmb { \beta } _ { k } ) ( \pmb { e } _ { i } ^ { T} C ( M ^ { - 1 } ) ^ { T } \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k} ) ] + \lambda _ { Z } z _ { i j }} \\ &  = \sum _ { k = 1 } ^ { K } [ \pmb { e } _ { i } ^ { T } ( M ^ { - 1 } X \pmb { \beta } _ { k }   \frac { \partial h ^ { m } } { \partial \pmb { \theta } _ { k } ^ { T} } M ^ { - 1 } C Z )   \pmb { e} _ { j } +   [   [ C ( M ^ { - 1 } ) ^ T   ]   [   [ D ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ].    [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ].    [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ] +   [   [ Z ( M ^ {- 1} ) ^ T   ]   ].    [   [ Z ( M ^ {- 1} ) ^ T   ]   ]   ]. \\ & {- 2 ( \pmb {\mathbf e} _ { i } ^ { T} Z \pmb {\mathbf e} _ { j} ) ( \pmb {\mathbf e} _ {\mathrm{i}} ^ { T} ( ( M ^ {- 1} X \pmb {\mathbf e} _ {\mathrm{k} )}) ⊙ ( C ( M ^ {- 1} ) ^ T   ]   [   [ D (\ p u a d) ] p u a d) ] + . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ,}. \\ & {- 2 ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ] + Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmb {\mathbf f} ) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d) ) ( Z (\pmp u a d)) ,.    [ P u a d) ] P u a d)} \\ & {- 2 ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\qquad S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R s ,).    [ P u a d) ] P u a d)} \\ & {- 2 ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\qquad S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R S U R s ,).    [ P u a d) ] P u a d)} \\ & {- 2 ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\qquad S U R S U R S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad S U R s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) ( Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad s ,)) (Z (\qquad t ,))    [ P u a d) ] P u a d)} \\ & {- 2 ( Z (\pmb {\mathbf e} _ {\mathrm{i}} ^ {\mathrm{T}} Z (\pmb {\mathbf e} _ {\mathrm{j} )}) ( P u a d) ] P u a d)} \\ & - 2 ( P u a d) | P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d |
| & - 2 ( P u a d) | P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 1, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    |
| & {- 2 ( P u a d) | P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d | > 0, P u a d |> 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N.    [ P u a d) | P u a d | > 0, N..    [ P u a d) | P u a d | > 0, N.    [ P u a d) |P u a d | > 0, N.    [ Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q: Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q : Q       /         /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /          /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /           /            ;        I = I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I* I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I * I* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II*II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* II* III.     [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = q.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]    [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = q.u.a.]     [P = p.u.a.]     [P = q.u.a.]     [P = p.u.a.]     [P = q.u.a.]     [P = p.u.a.]     [P = q.u.a.]     [P = p.u.a.]     [P = q.u.a.]     [P = p.u.a.]     [P = q.u.a.]     [P = p.u.a.]     [P = q.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]      [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = p.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [P = n.u.a.]     [Q: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K: K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:K:k:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I,I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:I:II:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I}:I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I):I:A(I)< ecel>< nl>
$$

which implies that

$$
\begin{array}{l} \frac {\partial q ^ {m}}{\partial Z} = \sum_ {k = 1} ^ {K} [ (M ^ {- 1} X \boldsymbol {\beta} _ {k}) \left(\frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} M ^ {- 1} C Z\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}}\right) (\boldsymbol {\beta} _ {k} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z) \\ - 2 Z \odot \left((M ^ {- 1} X \boldsymbol {\beta} _ {k}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}}\right) \mathbf {1} _ {d} ^ {T}\right) ] + \lambda_ {Z} Z. \end{array}
$$

With Equations (A2), (A8), (11) and (13), we have

$$
\begin{array}{l} \frac {\partial q ^ {m}}{\partial \alpha_ {i}} = \frac {\partial h ^ {m}}{\partial \alpha_ {i}} + \lambda_ {\alpha} \alpha_ {i} = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} \frac {\partial \boldsymbol {\theta} _ {k}}{\partial \alpha_ {i}} + \lambda_ {\alpha} \alpha_ {i} = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} \frac {\partial (M ^ {- 1} X \boldsymbol {\beta} _ {k})}{\partial \alpha_ {i}} + \lambda_ {\alpha} \alpha_ {i} = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} \frac {\partial M ^ {- 1}}{\partial \alpha_ {i}} X \boldsymbol {\beta} _ {k} + \lambda_ {\alpha} \alpha_ {i} \\ = \sum_ {k = 1} ^ {K} \left[ \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} M ^ {- 1} C (\mathbf {1} _ {n} \mathbf {e} _ {i} ^ {T} + \mathbf {e} _ {i} \mathbf {1} _ {n} ^ {T} - 2 \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T}) M ^ {- 1} X \boldsymbol {\beta} _ {k} \right] + \lambda_ {\alpha} \alpha_ {i} \\ = \sum_ {k = 1} ^ {K} [ (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \boldsymbol {\beta} _ {k}) (\frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}) + (\mathbf {e} _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}}) (\boldsymbol {\beta} _ {k} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ - 2 (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \boldsymbol {\beta} _ {k}) (\mathbf {e} _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}}) ] + \lambda_ {\alpha} \alpha_ {i} \\ = \sum_ {k = 1} ^ {K} [ \mathbf {e} _ {i} ^ {T} (M ^ {- 1} X \boldsymbol {\beta} _ {k}) (\frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}) + \mathbf {e} _ {i} ^ {T} (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}}) (\boldsymbol {\beta} _ {k} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ - 2 \mathbf {e} _ {i} ^ {T} (M ^ {- 1} X \boldsymbol {\beta} _ {k} \odot C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}}) ] + \lambda_ {\alpha} \mathbf {e} _ {i} ^ {T} \boldsymbol {\alpha}, \end{array}
$$

which implies that

$$
\begin{array}{r l} & {\frac {\partial q ^ {m}}{\partial \pmb {\alpha}} = \sum_ {k = 1} ^ {K} [ (M ^ {- 1} X \pmb {\beta} _ {k}) (\frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} M ^ {- 1} C 1 _ {n}) + (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}}) (\pmb {\beta} _ {k} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} 1 _ {n})} \\ & {\qquad - 2 (M ^ {- 1} X \pmb {\beta} _ {k}) \odot (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}}) ] + \lambda_ {\pmb {\alpha}} \pmb {\alpha}.} \end{array}
$$

Employing Equations (A3), (A4), (6) and (8), we have

$$
\begin{array}{r l} & {\frac {\partial q ^ {m}}{\partial c _ {i}} = \frac {\partial h ^ {m}}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} \frac {\partial \pmb {\theta} _ {k}}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} \frac {\partial (M ^ {- 1} X \pmb {\beta} _ {k})}{\partial c _ {i}} + \lambda_ {c} c _ {i}} \\ & {\qquad = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} \frac {\partial M ^ {- 1}}{\partial c _ {i}} X \pmb {\beta} _ {k} + \lambda_ {c} c _ {i} = \sum_ {k = 1} ^ {K} [ \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} (M ^ {- 1} \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T} G M ^ {- 1}) X \pmb {\beta} _ {k} ] + \lambda_ {c} c _ {i}} \\ & {\qquad = \sum_ {k = 1} ^ {K} [ (\mathbf {e} _ {i} ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}}) (\mathbf {e} _ {i} ^ {T} G M ^ {- 1} X \pmb {\beta} _ {k}) ] + \lambda_ {c} c _ {i}} \\ & {\qquad = \sum_ {k = 1} ^ {K} [ \mathbf {e} _ {i} ^ {T} ((M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}}) \odot (G M ^ {- 1} X \pmb {\beta} _ {k})) ] + \lambda_ {c} \mathbf {e} _ {i} ^ {T} \mathbf {c},} \end{array}
$$

which implies that

$$
\frac {\partial q ^ {m}}{\partial \boldsymbol {c}} = \sum_ {k = 1} ^ {K} [ \Big ((M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \boldsymbol {\theta} _ {k}} \Big) \odot (G M ^ {- 1} X \boldsymbol {\beta} _ {k}) ] + \lambda_ {c} \boldsymbol {c}.
$$

Given Equations (A8), (11) and (13), we have

$$
\begin{array}{r l} & {\frac {\partial q ^ {m}}{\partial \beta_ {k , p}} = \frac {\partial h ^ {m}}{\partial \beta_ {k , p}} + \lambda_ {\beta} \beta_ {k, p} = \sum_ {k = 1} ^ {K} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {\bar {k}} ^ {T}} \frac {\partial \pmb {\theta} _ {\bar {k}}}{\partial \beta_ {k , p}} + \lambda_ {\beta} \beta_ {k, p} = \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} \frac {\partial (M ^ {- 1} X \pmb {\beta} _ {k})}{\partial \beta_ {k , p}} + \lambda_ {\beta} \beta_ {k, p}} \\ & {\qquad = \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k} ^ {T}} M ^ {- 1} X \mathbf {e} _ {p} + \lambda_ {\beta} \pmb {\beta} _ {k} ^ {T} \mathbf {e} _ {p} = \pmb {e} _ {p} ^ {T} \Big (X ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} + \lambda_ {\beta} \pmb {\beta} _ {k} \Big),} \end{array}
$$

which implies that

$$
\frac {\partial q ^ {m}}{\partial \pmb {\beta} _ {k}} = X ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h ^ {m}}{\partial \pmb {\theta} _ {k}} + \lambda_ {\pmb {\beta}} \pmb {\beta} _ {k}.
$$

This completes the proof of Proposition 4. ∎

## Appendix D

## Numerical Credit Risk Prediction Problem

## D1. Parameter Estimation for the Numerical Credit Risk Prediction Problem

```txt
Input: ε: convergence threshold, ε > 0; {xi, yi}n i=1: training data
Output: β, Z, α, c: parameter estimations
1: r = 0. // r: iteration count
2: Initialize β(r), α(r), c(r).
3: Compute β(r) according to Equation (19).
4: Compute q^{n,(r)} = q^n(β(r), Z(r), α(r), c(r)) according to Equation (18).
5: repeat
6:    β(r+1) = arg min_Z q^n(β(r), Z, α(r), c(r)).
7:    α(r+1) = arg min_α q^n(β(r), Z(r+1), α, c(r)).
8:    c(r+1) = arg min_c q^n(β(r), Z(r+1), α(r+1), c).
9:    Compute β(r+1) according to Equation (19).
10:    Compute q^{n,(r+1)} = q^n(β(r+1), Z(r+1), α(r+1), c(r+1)) according to Equation (18).
11:    r = r + 1.
12: until |q^{n,(r)} - q^{n,(r-1)}| < ε.
13: return (β, Z, α, c) = (β(r), Z(r), α(r), c(r)).
```

Algorithm D1. An Alternating Minimization Algorithm for Parameter Estimation (Numerical Case)

## D2. Proof of Proposition 5

The partial derivative of loss function $h ^ { n }$ (defined in Equation 17) with respect to $\pmb { \mu }$ is

$$
\frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}} = \frac {\partial \left(\frac {1}{2} (Y - \boldsymbol {\mu}) ^ {T} (Y - \boldsymbol {\mu})\right)}{\partial \boldsymbol {\mu}} = \frac {1}{2} \frac {\partial (Y ^ {T} Y - 2 \boldsymbol {\mu} ^ {T} Y + \boldsymbol {\mu} ^ {T} \boldsymbol {\mu})}{\partial \boldsymbol {\mu}} = \boldsymbol {\mu} - Y.\tag{A9}
$$

Given Equations (A1), (A9), (16) and (18), we have

$$
\begin{array}{l} \frac {\partial q ^ {n}}{\partial z _ {i j}} = \frac {\partial h ^ {n}}{\partial z _ {i j}} + \lambda_ {z} z _ {i j} = \frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} \frac {\partial \pmb {\mu}}{\partial z _ {i j}} + \lambda_ {z} z _ {i j} = \frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} \frac {\partial (M ^ {- 1} X \pmb {\beta})}{\partial z _ {i j}} + \lambda_ {z} z _ {i j} = \frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} \frac {\partial M ^ {- 1}}{\partial z _ {i j}} X \pmb {\beta} + \lambda_ {z} z _ {i j} \\ = \frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} M ^ {- 1} C \big (Z _ {j} \mathbf {e} _ {i} ^ {T} + \mathbf {e} _ {i} Z _ {j} ^ {T} - 2 z _ {i j} \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T} \big) M ^ {- 1} X \pmb {\beta} + \lambda_ {z} z _ {i j} \\ - 2 z _ {i j} \left(\frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} M ^ {- 1} C \mathbf {e} _ {i}\right) (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \pmb {\beta}) + \lambda_ {z} z _ {i j} \\ = \mathbf {e} _ {i} ^ {T} \Big (M ^ {- 1} X \pmb {\beta} \frac {\partial h ^ {n}}{\partial \pmb {\mu} ^ {T}} M ^ {- 1} C Z \Big) \mathbf {e} _ {j} + \mathbf {e} _ {i} ^ {T} \Big (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}} \pmb {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z \Big) \mathbf {e} _ {j} \\ - 2 (\mathbf {e} _ {i} ^ {T} Z \mathbf {e} _ {j}) \Big (\mathbf {e} _ {i} ^ {T} \Big ((M ^ {- 1} X \pmb {\beta}) \odot (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \pmb {\mu}}) \Big) \mathbf {1} _ {d} ^ {T} \mathbf {e} _ {j} \Big) + \lambda_ {z} \mathbf {e} _ {i} ^ {T} Z \mathbf {e} _ {j}, \end{array}
$$

which implies that

$$
\begin{array}{l} \frac {\partial q ^ {n}}{\partial Z} = (M ^ {- 1} X \boldsymbol {\beta}) \left(\frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} M ^ {- 1} C Z\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}\right) (\boldsymbol {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} Z) \\ - 2 Z \odot \left((M ^ {- 1} X \boldsymbol {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}\right) \mathbf {1} _ {d} ^ {T}\right) + \lambda_ {Z} Z. \end{array}
$$

With Equations (A2), (A9), (16) and (18) we have

$$
\begin{array}{l} \frac {\partial q ^ {n}}{\partial \alpha_ {i}} = \frac {\partial h ^ {n}}{\partial \alpha_ {i}} + \lambda_ {\boldsymbol {\alpha}} \alpha_ {i} = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} \frac {\partial \boldsymbol {\mu}}{\partial \alpha_ {i}} + \lambda_ {\boldsymbol {\alpha}} \alpha_ {i} = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} \frac {\partial (M ^ {- 1} X \boldsymbol {\beta})}{\partial \alpha_ {i}} + \lambda_ {\boldsymbol {\alpha}} \alpha_ {i} = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} \frac {\partial M ^ {- 1}}{\partial \alpha_ {i}} X \boldsymbol {\beta} + \lambda_ {\boldsymbol {\alpha}} \alpha_ {i} \\ = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} M ^ {- 1} C (\mathbf {1} _ {n} \mathbf {e} _ {i} ^ {T} + \mathbf {e} _ {i} \mathbf {1} _ {n} ^ {T} - 2 \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T}) M ^ {- 1} X \boldsymbol {\beta} + \lambda_ {\boldsymbol {\alpha}} \alpha_ {i} \\ = (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \boldsymbol {\beta}) \left(\frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + (\mathbf {e} _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}) (\boldsymbol {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ - 2 (\mathbf {e} _ {i} ^ {T} M ^ {- 1} X \boldsymbol {\beta}) (\mathbf {e} _ {i} ^ {T} C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}) + \lambda_ {\boldsymbol {\alpha}} \alpha_ {i} \\ = \mathbf {e} _ {i} ^ {T} (M ^ {- 1} X \boldsymbol {\beta}) (\frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}) + \mathbf {e} _ {i} ^ {T} (C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}) (\boldsymbol {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ - 2 \mathbf {e} _ {i} ^ {T} (M ^ {- 1} X \boldsymbol {\beta} \odot C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}) + \lambda_ {\boldsymbol {\alpha}} \mathbf {e} _ {i} ^ {T} \boldsymbol {\alpha}, \end{array}
$$

which implies that

$$
\begin{array}{c} \frac {\partial q ^ {n}}{\partial \boldsymbol {\alpha}} = (M ^ {- 1} X \boldsymbol {\beta}) \left(\frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} M ^ {- 1} C \mathbf {1} _ {n}\right) + \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}\right) (\boldsymbol {\beta} ^ {T} X ^ {T} (M ^ {- 1}) ^ {T} \mathbf {1} _ {n}) \\ - 2 (M ^ {- 1} X \boldsymbol {\beta}) \odot \left(C (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}\right) + \lambda_ {\boldsymbol {\alpha}} \boldsymbol {\alpha}. \end{array}
$$

Employing Equations (A3), (A9), (16) and (18), we have

$$
\begin{array}{l} \frac {\partial q ^ {n}}{\partial c _ {i}} = \frac {\partial h ^ {n}}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} \frac {\partial \boldsymbol {\mu}}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} \frac {\partial (M ^ {- 1} X \boldsymbol {\beta})}{\partial c _ {i}} + \lambda_ {c} c _ {i} = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} \frac {\partial M ^ {- 1}}{\partial c _ {i}} X \boldsymbol {\beta} + \lambda_ {c} c _ {i} \\ = \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu} ^ {T}} (M ^ {- 1} \mathbf {e} _ {i} \mathbf {e} _ {i} ^ {T} G M ^ {- 1}) X \boldsymbol {\beta} + \lambda_ {c} c _ {i} \\ = (\mathbf {e} _ {i} ^ {T} (M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}) (\mathbf {e} _ {i} ^ {T} G M ^ {- 1} X \boldsymbol {\beta}) + \lambda_ {c} c _ {i} \\ = \mathbf {e} _ {i} ^ {T} \left(\left((M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}\right) \odot (G M ^ {- 1} X \boldsymbol {\beta})\right) + \lambda_ {c} \mathbf {e} _ {i} ^ {T} \boldsymbol {c}, \end{array}
$$

which implies that

$$
\frac {\partial q ^ {n}}{\partial \boldsymbol {c}} = \left((M ^ {- 1}) ^ {T} \frac {\partial h ^ {n}}{\partial \boldsymbol {\mu}}\right) \odot (G M ^ {- 1} X \boldsymbol {\beta}) + \lambda_ {c} \boldsymbol {c}
$$

This completes the proof of Proposition 5. ∎

## Appendix E

## Additional Analyses on Method Performance

## E1. Subgroup Analyses

We conducted subgroup analyses to further demonstrate the advantages of our proposed method. According to Equation (3), our proposed latent similarity-enhanced credit risk prediction model is given by:

$$
\theta_ {i} = \mathbf {x} _ {i} ^ {T} \pmb {\beta} + c _ {i} \sum_ {v _ {j} \in V: j \neq i} s _ {i j} \theta_ {j}.
$$

Here $\theta _ { i }$ denotes user $\vec { v _ { i } } \cdot \boldsymbol { \mathbf { s } }$ log-odds of delinquency. It is the addition of two components: the intrinsic

component, represented by $\mathbf { x } _ { i } ^ { T } \pmb { \beta } ,$ and the similarity component $\begin{array} { r } { \sum _ { v _ { j } \in V : j \neq i } s _ { i j } \theta _ { j } } \end{array}$ , which is the summation of other users’ log-odds of delinquency weighted by the similarity between each of them and $v _ { i } ( \mathrm { i } . \mathrm { e } . , s _ { i j } )$ . User-specific parameter $c _ { i }$ regulates the relative importance between the intrinsic component and the similarity component in predicting $\theta _ { i }$

First, we conducted a subgroup analysis with respect to $c _ { i } .$ . We divided users into two equally sized subgroups based on their respective value of $\mathrm { i } c _ { i } . \mathrm { A }$ user with a higher value of $\dot { \boldsymbol { c } } _ { i }$ indicates that the similarity component plays a more substantial role in predicting the user’s delinquency. Averaged across all billing cycles, the AUC for the subgroup having smaller values of $c _ { i }$ stands at 0.905, while the AUC for the subgroup with greater values of $c _ { i }$ is 0.956. The result suggests that our method is more likely to correctly classify users, for whom the similarity component has a greater predictive role. Figure E1(a) reports F1 scores for each subgroup across different values of ??. Similarly, F1 scores of the subgroup with higher values of $c _ { i }$ consistently surpass those of the subgroup with lower values of $c _ { i } .$ These observations are in alignment with our expectation that if the individual behaves more independently, the benefit of considering the similarity component would be decreased, which in turn leads to the reduced advantage of the proposed method.

Next, we performed another subgroup analysis with respect to $s _ { i j }$ . For each user, we counted its number of user-pairs with strong similarities, where a strong similarity is defined to be above the median of all pair-wise similarities among users. We then constructed two equally sized subgroups of users based on their respective number of user-pairs with strong similarities. A user having a greater number of user-pairs with strong similarities indicates that the user has more strong similarity peers. The average AUC for the subgroup of users with more strong similarity peers is 0.954; while for the subgroup of users with fewer such peers, it stands at 0.912. Figure E1b plots the F1 score for each subgroup against the value of $Q .$ As shown, F1 scores of the subgroup with more strong similarity peers consistently outperforms those of the subgroup with fewer such peers Again, these performance differences between the two subgroups are in alignment with the rationale of our method. When a user has strong similarities with more individuals, our method can potentially exploit more predictive power from these similar individuals’ behaviors, resulting in improved predictive performance.

![](/api/attachments/V6CQTZQD/fulltext/images/bbc2852694e0a2d7a71a7cef7c86a709fd0ac7ec46729f7f88a6f6e27f991a77.jpg)  
Figure E1. Subgroup Analysis: F1 Score

## E2. Robustness Check

For a robustness check, we further varied the number of predicted delinquent users from ?? = 3, 000 (∼ 25% of all users) to ?? = 4, 800 (∼ 40% of all users), with an increment of 300. Table E1 reports the evaluation results for billing cycle Ψ = 14 in terms of precision, recall, and F1 score. Averaged across ??, the average precision of LSE is 0.824, outperforming that of benchmark methods by a range between 7.14% and 42.38%. Moreover, the average recall of LSE surpasses that of benchmark methods by a range between 7.32% and 42.53%, and the average F1 score improves by a range between 7.23% and 42.46%. The performance improvement by our method over each benchmark in every evaluation metric, as reported in Table E1, is also statistically significant (?? < 0.001). Similarly, we obtained significant improvements by LSE over benchmarks for other billing cycles and omitted these evaluation results here for space consideration.

Table E1. Performance Comparison for Credit Risk Prediction Problem: Varying ?? (?? = ????)

<table><tr><td>Metric</td><td>Method</td><td>Q=3000</td><td>Q=3300</td><td>Q=3600</td><td>Q=3900</td><td>Q=4200</td><td>Q=4500</td><td>Q=4800</td><td>Mean</td><td>Std.</td></tr><tr><td rowspan="7">Precision</td><td>LSE (our method)</td><td>0.888</td><td>0.871</td><td>0.853</td><td>0.829</td><td>0.805</td><td>0.777</td><td>0.748</td><td>0.824</td><td>0.051</td></tr><tr><td>RLR</td><td>0.634</td><td>0.617</td><td>0.598</td><td>0.579</td><td>0.560</td><td>0.541</td><td>0.524</td><td>0.579</td><td>0.040</td></tr><tr><td>MLP</td><td>0.722</td><td>0.702</td><td>0.681</td><td>0.660</td><td>0.633</td><td>0.605</td><td>0.581</td><td>0.655</td><td>0.051</td></tr><tr><td>SVM</td><td>0.669</td><td>0.648</td><td>0.630</td><td>0.613</td><td>0.595</td><td>0.576</td><td>0.553</td><td>0.612</td><td>0.041</td></tr><tr><td>XGBoost</td><td>0.847</td><td>0.821</td><td>0.796</td><td>0.770</td><td>0.743</td><td>0.717</td><td>0.692</td><td>0.770</td><td>0.066</td></tr><tr><td>RNN-GRU</td><td>0.836</td><td>0.806</td><td>0.775</td><td>0.747</td><td>0.720</td><td>0.695</td><td>0.670</td><td>0.750</td><td>0.050</td></tr><tr><td>SIM-TemGNN</td><td>0.811</td><td>0.782</td><td>0.751</td><td>0.711</td><td>0.674</td><td>0.653</td><td>0.621</td><td>0.715</td><td>0.070</td></tr><tr><td rowspan="7">Recall</td><td>LSE (our method)</td><td>0.667</td><td>0.720</td><td>0.769</td><td>0.810</td><td>0.847</td><td>0.876</td><td>0.899</td><td>0.798</td><td>0.084</td></tr><tr><td>RLR</td><td>0.476</td><td>0.510</td><td>0.539</td><td>0.566</td><td>0.589</td><td>0.610</td><td>0.630</td><td>0.560</td><td>0.055</td></tr><tr><td>MLP</td><td>0.542</td><td>0.580</td><td>0.614</td><td>0.644</td><td>0.665</td><td>0.682</td><td>0.698</td><td>0.632</td><td>0.057</td></tr><tr><td>SVM</td><td>0.503</td><td>0.536</td><td>0.568</td><td>0.598</td><td>0.626</td><td>0.649</td><td>0.664</td><td>0.592</td><td>0.060</td></tr><tr><td>XGBoost</td><td>0.636</td><td>0.678</td><td>0.718</td><td>0.752</td><td>0.782</td><td>0.808</td><td>0.832</td><td>0.744</td><td>0.071</td></tr><tr><td>RNN-GRU</td><td>0.628</td><td>0.666</td><td>0.698</td><td>0.729</td><td>0.757</td><td>0.783</td><td>0.806</td><td>0.724</td><td>0.064</td></tr><tr><td>SIM-TemGNN</td><td>0.610</td><td>0.646</td><td>0.677</td><td>0.694</td><td>0.709</td><td>0.736</td><td>0.746</td><td>0.688</td><td>0.049</td></tr><tr><td rowspan="7">F1 Score</td><td>LSE (our method)</td><td>0.762</td><td>0.788</td><td>0.809</td><td>0.819</td><td>0.826</td><td>0.824</td><td>0.816</td><td>0.806</td><td>0.023</td></tr><tr><td>RLR</td><td>0.544</td><td>0.558</td><td>0.567</td><td>0.572</td><td>0.574</td><td>0.573</td><td>0.572</td><td>0.566</td><td>0.011</td></tr><tr><td>MLP</td><td>0.619</td><td>0.635</td><td>0.646</td><td>0.652</td><td>0.649</td><td>0.641</td><td>0.634</td><td>0.640</td><td>0.011</td></tr><tr><td>SVM</td><td>0.574</td><td>0.587</td><td>0.597</td><td>0.605</td><td>0.610</td><td>0.610</td><td>0.603</td><td>0.598</td><td>0.013</td></tr><tr><td>XGBoost</td><td>0.727</td><td>0.743</td><td>0.755</td><td>0.761</td><td>0.762</td><td>0.759</td><td>0.756</td><td>0.752</td><td>0.013</td></tr><tr><td>RNN-GRU</td><td>0.717</td><td>0.729</td><td>0.735</td><td>0.738</td><td>0.738</td><td>0.737</td><td>0.732</td><td>0.732</td><td>0.007</td></tr><tr><td>SIM-TemGNN</td><td>0.696</td><td>0.708</td><td>0.712</td><td>0.703</td><td>0.691</td><td>0.692</td><td>0.678</td><td>0.697</td><td>0.012</td></tr></table>

## E3. Latent Similarity Reconstruction

We conducted a simulation study to validate the meaningfulness of the unobserved (latent) similarity learned by our method. In the simulation study, we generated synthetic data to validate whether our method can effectively reconstruct unobserved similarities among users. Recal that the similarity $s _ { i j }$ between users $v _ { i }$ and $v _ { j }$ is defined as

$$
s _ {i j} = \alpha_ {i} + \alpha_ {j} + \tilde {\mathbf {x}} _ {i} ^ {T} \tilde {\mathbf {x}} _ {j} + \mathbf {z} _ {i} ^ {T} \mathbf {z} _ {j},\tag{A10}
$$

where $\tilde { \mathbf { x } } _ { i }$ is the normalization of observed intrinsic characteristics of user $v _ { i } , \mathbf { z } _ { i }$ and $\alpha _ { i }$ represent unobserved intrinsic characteristics of this user. Correspondingly, the unobserved similarity within $\boldsymbol { s } _ { i j } ^ { \circ }$ is expressed as

$$
\mathbf {\boldsymbol {s}} _ {i j} ^ {\circ} := \alpha_ {i} + \alpha_ {j} + \mathbf {z} _ {i} ^ {T} \mathbf {z} _ {j}.\tag{A11}
$$

In the simulation study, we aimed to reconstruct the unobserved similarity $\boldsymbol { s } _ { i j } ^ { \circ }$ using our method.

To generate synthetic data, we first simulated each user with eight observed intrinsic characteristics and three unobserved intrinsi characteristics (two ??’s and one ??). The value of each observed or unobserved intrinsic characteristic was generated from the standard normal distribution ??(0, 1). Next, we need to generate the label (0 or 1) for each user, where 0 represents no delinquency and 1 denotes delinquency. For this purpose, with the generated observed and unobserved intrinsic characteristics of each user, we calculated the user’s log-odds of delinquency $\theta _ { i }$ using Equations (1) and (3). In this calculation, the regression coefficients $\pmb { \beta }$ were simulated from a uniform distribution ??[5, 20], and the parameter $c _ { i }$ was set to 1/50. With a user’s $\theta _ { i }$ calculated, we computed the user’s probability of delinquency $p _ { i } \operatorname { a s } { \frac { e ^ { \theta _ { i } } } { 1 + e ^ { \theta _ { i } } } }$ and sampled the user’s delinquency label $y _ { i }$ according to $p _ { i }$ . In our simulation study, we generated synthetic data for 50 users over 12 billing cycles.

Before executing our method, we removed the unobserved intrinsic characteristics from the generated synthetic data. Subsequently, we employed our method on the modified synthetic data to estimate these unobserved intrinsic characteristics. The estimated unobserved similarity $\boldsymbol { s } _ { i j } ^ { \circ }$ between a pair of users was then calculated with their estimated unobserved intrinsic characteristics using Equation (A11). It is common to validate the meaningfulness of a latent variable employed by a machine learning algorithm by showing how effective the variable can be reconstructed by the algorithm (Chen, 2023). Accordingly, to validate the meaningfulness of the unobserved similarity in our study, we evaluated the effective- ness of reconstructing this latent variable by our method using the relative error (RE) measure defined below:

$$
\mathrm{RE} = \frac {\sum_ {i \neq j} \left(s _ {i j} ^ {\circ} - \hat {s} _ {i j} ^ {\circ}\right) ^ {2}}{\sum_ {i \neq j} \left(s _ {i j} ^ {\circ}\right) ^ {2}}.\tag{A12}
$$

The value of RE is in the range of [0, +∞], and a smaller relative error indicates a more effective reconstruction.

We conducted the simulation study for 100 times. The averaged relative error attained by our method across 100 simulation runs is 0.447. It is noted that our method achieves this reconstruction error without the knowledge of the distribution of unobserved intrinsic characteristics. In comparison, let us consider a benchmark that has the knowledge of the distribution of unobserved intrinsic characteristics. Specifically, the benchmark sampled unobserved intrinsic characteristics from the standard normal distribution and then calculated the estimated unobserved similarity $\boldsymbol { s } _ { i j } ^ { \circ }$ using Equation (A11). The benchmark achieved an averaged relative error of 1.99 across 100 simulation runs. The significant outperformance of our method, operated without the distribution knowledge, over the benchmark equipped with the distribution knowledge demonstrates the effectiveness of our method in reconstructing the unobserved similarity.
