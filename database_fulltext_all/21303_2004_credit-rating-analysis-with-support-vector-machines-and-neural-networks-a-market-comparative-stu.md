---
otero_id: 21303
otero_key: "FFD5P5PS"
title: "Credit rating analysis with support vector machines and neural networks: a market comparative study"
authors: "Zan Huang; Hsinchun Chen; Chia-Jung Hsu; Wun-Hwa Chen; Soushan Wu"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00086-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Credit rating analysis with support vector machines and neural networks: a market comparative study

Zan Huang<sup>a,</sup>\*, Hsinchun Chen<sup>a</sup>, Chia-Jung Hsu<sup>a</sup>, Wun-Hwa Chen<sup>b</sup>, Soushan Wu<sup>c</sup>

<sup>a</sup> Department of Management Information Systems, Eller College of Business and Public Administration, The University of Arizona,

Rm. 430, McClelland Hall, 1130 E. Helen Street, Tucson, AZ 85721, USA

<sup>b</sup> Department of Business Administration, National Taiwan University, Taiwan

<sup>c</sup> College of Management, Chang-Gung University, Taiwan

Available online 4 July 2003

## Abstract

Corporate credit rating analysis has attracted lots of research interests in the literature. Recent studies have shown that Artificial Intelligence (AI) methods achieved better performance than traditional statistical methods. This article introduces a relatively new machine learning technique, support vector machines (SVM), to the problem in attempt to provide a model with better explanatory power. We used backpropagation neural network (BNN) as a benchmark and obtained prediction accuracy around 80% for both BNN and SVM methods for the United States and Taiwan markets. However, only slight improvement of SVM was observed. Another direction of the research is to improve the interpretability of the AI-based models. We applied recent research results in neural network model interpretation and obtained relative importance of the input financial variables from the neural network models. Based on these results, we conducted a market comparative analysis on the differences of determining factors in the United States and Taiwan markets. .2003 F1 PV.A11

Keywords: Data mining; Credit rating analysis; Bond rating prediction; Backpropagation neural networks; Support vector machines; Input variable contribution analysis; Cross-market analysis

## 1. Introduction

Credit ratings have been extensively used by bond investors, debt issuers, and governmental officials as a surrogate measure of riskiness of the companies and bonds. They are important determinants of risk premiums and even the marketability of bonds.

Company credit ratings are typically very costly to obtain, since they require agencies such as Standard and Poor’s and Moody’s to invest large amount of time and human resources to perform deep analysis of the company’s risk status based on various aspects ranging from strategic competitiveness to operational level details. As a result, not all companies can afford yearly updated credit ratings from these agencies, which makes credit rating prediction quite valuable to the investment community.

Although rating agencies and many institutional writers emphasize the importance of analysts’ subjective judgment in determining credit ratings, many researchers have obtained promising results on credit rating prediction applying different statistical and Artificial Intelligence (AI) methods. The grand assumption is that financial variables extracted from public financial statements, such as financial ratios, contain a large amount of information about a company’s credit risk. These financial variables, combined with historical ratings given by the rating agencies, have embedded in them valuable expertise of the agencies in evaluating companies’ credit risk levels. The overall objective of credit rating prediction is to build models that can extract knowledge of credit risk evaluation from past observations and to apply it to evaluate credit risk of companies with much broader scope. Besides the prediction, the modeling of the bond-rating process also provides valuable information to users. By determining what information was actually used by expert financial analysts, these studies can also help users capture fundamental characteristics of different financial markets.

In this study, we experimented with using a relatively new learning method for the field of credit rating prediction, support vector machines, together with a frequently used high-performance method, backpropagation neural networks, to predict credit ratings. We were also interested in interpreting the models and helping users to better understand bond raters’ behavior in the bond-rating process. We conducted input financial variable contribution analysis in an attempt to interpret neural network models and used the interpretation results to compare the characteristics of bond-rating processes in the United States and Taiwan markets. The remainder of the paper is structured as follows. A background section about credit rating follows the introduction. Then, a literature review about credit rating prediction is provided, followed by descriptions of the analytical methods. We also include descriptions of the data sets, the experiment results and analysis followed by the discussion and future directions.

## 2. Credit risk analysis

There are two basic types of credit ratings, one is for specific debt issues or other financial obligations and the other is for debt issuers. The former is the one most frequently studied and can be referred to as a ‘‘bond rating’’ or ‘‘issue credit rating.’’ It is essentially an attempt to inform the public of the likelihood of an investor receiving the promised principal and interest payments associated with a bond issue. The latter is a current opinion of an issuer’s overall capacity to pay its financial obligations, which conveys the issuer’s fundamental creditworthiness. It focuses on the issuer’s ability and willingness to meet its financial commitments on a timely basis. This rating can be referred to as ‘‘counterparty credit rating,’’ ‘‘default rating’’ or ‘‘issuer credit rating.’’ Both types of ratings are very important to the investment community. A lower rating usually indicates higher risk, which causes an immediate effect on the subsequent interest yield of the debt issue. Besides this, many regulatory requirements for investment or financial decision in different countries are specified based on such credit ratings. Many agencies allow investment only in companies having the top four rating categories (‘‘investment’’ level ratings). There is also substantial empirical evidence in the finance and accounting literature that have established the importance of information content contained in credit ratings. ‘‘These studies showed that both the stock and bond markets react in a manner that indicated credit ratings convey important information regarding the value of the firm and its prospects of being able to repay its debt obligations as scheduled’’ [28].

A company obtains a credit rating by contacting a rating agency requesting that an issuer rating be assigned to the company or that an issue rating be assigned to a new debt issue. Typically, the company requesting a credit rating submits a package containing the following documentation: annual reports for past years, latest quarterly reports, income statement and balance sheet, most recent prospectus for debt issues and other specialized information and statistical reports. The rating agency then assigns a team of financial analysts to conduct basic research on the characteristics of the company and the individual issue. After meeting with the issuer, the designated analyst prepares a rating report and presents it to the rating committee, together with his or her rating recommendations. A committee reviews the documentation presented and discuss with the analysts involved. They make the final decision on the credit rating and take responsibility for the rating results.

It is generally believed that the credit rating process involves highly subjective assessment of both quanti tative and qualitative factors of a particular company as well as pertinent industry-level or market-level variables. Rating agencies and some researchers have emphasized the importance of subjective judgment in the bond-rating process and criticized the use of simple statistical models and other models derived from AI techniques to predict credit ratings, although they agree that such analysis provide a basic ground from judgment in general. However, as we will show in the next section, the literature of credit rating prediction has demonstrated that statistical models and AI models (mainly neural networks) achieved remarkably good prediction performance and largely captured the characteristics of the bondrating process.

## 3. Literature review

Substantial literature can be found in bond-rating prediction history. We categorized the methods extensively used in prior research into statistical methods and machine learning methods.

## 3.1. Statistical methods

The use of statistical methods for bond-rating prediction can be traced back to 1959, when Fisher utilized ordinary least squares (OLS) in an attempt to explain the variance of a bond’s risk premium [13]. Many subsequent studies used OLS to predict bond ratings [19,36,47]. Pinches and Mingo [33,34] utilized multiple discriminant analysis (MDA) to yield a linear discriminant function relating a set of independent variables to a dependent variable to better suit the ordinal nature of bond-rating data and increase classification accuracy. Other researchers also utilized logistic regression analysis [10] and probit analysis [17,22]. These studies used different data sets and the prediction results were typically between 50% and 70%. Different financial variables have been used in different studies. The financial variables typically selected included measures of size, financial leverage, long-term capital intensiveness, return on investment, short-term capital intensiveness, earnings stability and debt coverage stability [34].

The general conclusion from these efforts in bondrating prediction using statistical methods was that a simple model with a small list of financial variables could classify about two-thirds of a holdout sample of bonds. These statistical models were succinct and were easy to explain. However, the problem with applying these methods to the bond-rating prediction problem is that the multivariate normality assumptions for independent variables are frequently violated in financial data sets [8], which makes these methods theoretically invalid for finite samples.

## 3.2. Artificial intelligence methods

Recently, Artificial Intelligence (AI) techniques, particularly rule-based expert systems, case-based reasoning systems and machine learning techniques such as neural networks have been used to support such analysis. The machine learning techniques automatically extract knowledge from a data set and construct different model representations to explain the data set. The major difference between traditional statistical methods and machine learning methods is that statistical methods usually need the researchers to impose structures to different models, such as the linearity in the multiple regression analysis, and to construct the model by estimating parameters to fit the data or observation, while machine learning techniques also allow learning the particular structure of the model from the data. As a result, the humanimposed structures of the models used in statistical methods are relatively simple and easy to interpret, while models obtained in machine learning methods are usually very complicated and hard to explain. Galindo and Tamayo [14] used model size to differentiate statistical methods from machine learning methods. For a given training sample size, there is an optimal model size. The models used in statistical methods are usually too simple and tend to under-fit the data while machine learning methods generate complex models and tend to over-fit the data. This is in fact the trade-off between the explanatory power and parsimony of a model, where explanatory power leads to high prediction accuracy and parsimony usually assures generalizability and interpretability of the model.

The most frequently used AI method was backpropagation neural networks. Many previous studies compared the performance of neural networks with statistical methods and other machine learning techniques. Dutta and Shekhar [9] started to investigate the applicability of neural networks to bond rating in 1988. They got a prediction accuracy of 83.3% classifying ‘‘AA’’ and ‘‘non-AA’’ rated bonds.

Singleton and Surkan [38] used a backpropagation neural network to classify bonds of the 18 Bell Telephone companies divested by AT and T in 1982. The task was to classify a bond as being rated either ‘‘Aaa’’ or one of ‘‘A1’’, ‘‘A2’’ and ‘‘A3’’ by Moody’s. They experimented with backpropagation neural networks with one or two hidden layers and the best network obtained 88% testing accuracy. They also compared a neural network model with multiple discriminant analysis (MDA) and demonstrated that neural networks achieved better performance in predicting direction of a bond rating than discriminant analysis could [39].

Kim [25] compared the neural network approach with linear regression, discriminant analysis, logistic analysis, and a rule-based system for bond rating. They found that neural networks achieved better performance than other methods in terms of classification accuracy. The data set used in this study was prepared from Standard and Poor’s Compustat financial data, and the prediction task was on six rating categories.

Moody and Utans [30] used neural networks to predict 16 categories of S and P rating ranging from ‘‘B-’’ and below (3) to ‘‘AAA’’ (18). Their model predicted the ratings of 36.2% of the firms correctly. They also tested the system with 5-class prediction and 3-class prediction and obtained prediction accuracies of 63.8% and 85.2%, respectively.

Maher and Sen [28] compared the performance of neural networks on bond-rating prediction with that of logistic regression. They used data from Moody’s Annual Bond Record and Standard and Poor’s Compustat financial data. The best performance they obtained was 70%.

Kwon et al. [27] applied ordinal pairwise partitioning (OPP) approaches to backpropagation neural networks. They used Korean bond-rating data and demonstrated that neural networks with OPP had the highest level of accuracy (71–73%), followed by conventional neural networks (66 –67%) and multiple discriminant analysis (58 – 61%).

Chaveesuk et al. [3] also compared backpropagation neural network with radial basis function, learning vector quantization and logistic regression. Their study revealed that neural networks and logistic regression model obtained the best performances. However, the two methods only achieved accuracy of 51.9% and 53.3%, respectively.

Other researchers explored building case-based reasoning systems to predict bond ratings and at the same time provide better user interpretability. The basic principle of case-based reasoning is to match a new problem with the closest previous cases and try to learn from experiences to solve the problem. Shin and Han [37] proposed a case-based reasoning approach to predict bond rating of firms. They used inductive learning for case indexing, and used nearest-neighbor matching algorithms to retrieve similar past cases. They demonstrated that their system had higher prediction accuracy (75.5%) than the MDA (60%) and ID3 (59%) methods. They used Korean bond-rating data and the prediction was for five categories.

Some other researchers have studied the problems of default prediction and bankruptcy prediction [26,41,49], which are closely related to the bondrating prediction problem. Similar financial variables and methods were used in such studies and the prediction performance was typically higher because of the binary output categories.

We summarized important prior studies that applied AI techniques to the bond-rating prediction problem in Table 1. In summary, previous literature has consisted of extensive efforts to apply neural networks to the bond-rating prediction problem and comparisons with other statistical methods and machine learning methods have been conducted by many researchers. The general conclusion has been that neural networks outperformed conventional statistical methods and inductive learning methods in most prior studies. The assessment of the prediction accuracy obtained by individual studies should be adjusted by the number of prediction classes used. For studies that classified into more than five classes, the typical accuracy level was between 55% and 75%. The financial variables and sample sizes used by different studies both covered very wide ranges. The number of financial variables used ranged from 7 to 87 and the sample size ranged from 47 to 3886. Past academic research in

T<sub>a</sub>bl<sub>e</sub> 1  
P<sub>r</sub>i<sub>or</sub> b<sub>on</sub>d <sub>ra</sub>ti<sub>ng pre</sub>di<sub>c</sub>ti<sub>on s</sub>t<sub>u</sub>di<sub>es us</sub>i<sub>ng</sub> A<sub>r</sub>tifi<sub>c</sub>i<sub>a</sub>l I<sub>n</sub>t<sub>e</sub>lli<sub>gence</sub> t<sub>ec</sub>h<sub>n</sub>i<sub>ques</sub>

<table><tr><td>Study</td><td>Bond rating categories</td><td>AI methods</td><td>Accuracy</td><td>Data</td><td>Variables</td><td>Sample size</td><td>Benchmark statistical methods</td></tr><tr><td>[9]</td><td>2 (AA vs. non-AA)</td><td>BP</td><td>83.30%</td><td>US</td><td>Liability/cash asset, debt ratio, sales/net worth, profit/sales, financial strength, earning/fixed costs, past 5 year revenue growth rate, projected next 5 year revenue growth rate, working capital/sales, subjective prospect of company.</td><td>30/17</td><td>LinR (64.7%)</td></tr><tr><td>[38]</td><td>2 (Aaa vs. A1, A2 or A3)</td><td>BP</td><td>88%</td><td>US(Bell companies)</td><td>Debt/total capital, pre-tax interest expense/income, return on investment (or equity), 5-year ROE variation, log(total assets), construction cost/total cash flow, toll revenue ratio.</td><td>126</td><td>MDA (39%)</td></tr><tr><td>[15]</td><td>3</td><td>BP</td><td>84.90%</td><td>US S&amp;P</td><td>87 financial variables</td><td>797</td><td>N/A</td></tr><tr><td>[25]</td><td>6</td><td>BP, RBS</td><td>55.17% (BP), 31.03% (RBS)</td><td>US S and P</td><td>Total assets, total debt, long term debt or total invested capital, current asset or liability, (net income + interest)/interest, preferred dividend, stock price or common equity per share, subordination.</td><td>110/58/60</td><td>LinR (36.21%), MDA (36.20%), LogR (43.10%)</td></tr><tr><td>[30]</td><td>16</td><td>BP</td><td>36.2%, 63.8% (5 classes), 85.2% (3 classes)</td><td>US S&amp;P</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>[28]</td><td>6</td><td>BP</td><td>70% (7), 66.67% (5)</td><td>US Moody&#x27;s</td><td>Total assets, long-term debt/total assets, Net income from operations/total asset, subordination status, common stock market beta value.</td><td>299</td><td>LogR (61.66%), MDA (58–61%)</td></tr><tr><td>[27]</td><td>5</td><td>BP(with OPP)</td><td>71–73%(with OPP), 66–67%(without OPP)</td><td>Korean</td><td>24 financial variables</td><td>126</td><td>MDA (58–62%)</td></tr><tr><td>[27]</td><td>5</td><td>ACLS, BP</td><td>59.9% (ACLS), 72.5% (BP)</td><td>Korean</td><td>24 financial variables</td><td>126</td><td>MDA (61.6%)</td></tr><tr><td>[3]</td><td>6</td><td>BP, RBF, LVQ</td><td>56.7% (BP), 38.3% (RBF), 36.7% (LVQ)</td><td>US S&amp;P</td><td>Total assets, total debt, long-term debt/total capital, short-term debt/total capital, current asset/current liability, (net income + interest expense)/interest expense, total debt/total asset, profit/sales.</td><td>60/60(10 for each category)</td><td>LogR (53.3%)</td></tr><tr><td>[37]</td><td>5</td><td>CBR, GA</td><td>75.5% (CBR, GA combined) 62.0% (CBR) 53–54% (ID3)</td><td>Korean</td><td>Firm classification, firm type, total assets, stockholders&#x27; equity, sales, years after founded, gross profit/sales, net cash flow/total asset, financial expense/sales, total liabilities/total assets, depreciation/total expense, working capital turnover</td><td>3886</td><td>MDA (58.4–61.6%)</td></tr></table>

BP : Backpropagation Neural Networks<sub>,</sub> RB S : Rule-based System<sub>,</sub> ACLS : Analog Concept Learning System<sub>,</sub> RBF : Radial Basis Function<sub>,</sub> LVQ : Learning Vector Quantization<sub>,</sub> CBR: C<sub>ase</sub>-b<sub>ase</sub>d R<sub>eason</sub>i<sub>ng,</sub> GA<sub>:</sub> G<sub>ene</sub>ti<sub>c</sub> Al<sub>gor</sub>ith<sub>m,</sub> MDA<sub>:</sub> M<sub>u</sub>lti<sub>p</sub>l<sub>e</sub> Di<sub>scr</sub>i<sub>m</sub>i<sub>nan</sub>t A<sub>na</sub>l<sub>ys</sub>i<sub>s,</sub> Li<sub>n</sub>R<sub>:</sub> Li<sub>near</sub> R<sub>egress</sub>i<sub>on,</sub> L<sub>og</sub>R<sub>:</sub> L<sub>og</sub>i<sub>s</sub>ti<sub>c</sub> R<sub>egress</sub>i<sub>on,</sub> OPP <sub>:</sub> O<sub>r</sub>di<sub>nary</sub> P<sub>a</sub>i<sub>rw</sub>i<sub>se</sub> P<sub>ar</sub>titi<sub>on</sub>i<sub>ng</sub>. S<sub>amp</sub>l<sub>e s</sub>i<sub>ze :</sub> T<sub>ra</sub>i<sub>n</sub>i<sub>ng</sub>/t<sub>un</sub>i<sub>ng</sub>/t<sub>es</sub>ti<sub>ng</sub>.

bond-rating prediction has mainly been conducted in the United States and Korean markets.

## 4. Research questions

The literature of bond-rating prediction can be viewed as researchers’ efforts to model bond raters’ rating behavior by using publicly available financial information. There were two themes in these studies, prediction accuracy and explanatory power of the models. By exploring the statistical methods for addressing the bond-rating prediction problem, researchers have shown that ‘‘relatively simple functions on historical and publicly available data can be used as an excellent first approximation for the ‘highly complex’ and ‘subjective’ bond-rating process’’ [24]. These statistical methods have provided relatively higher prediction accuracy than expectation and simple interpretations of the bond-rating process. Many studies have reported lists of important variables for bond-rating prediction models.

The recent application of different Artificial Intelligence (AI) techniques to the bond-rating prediction problem achieved higher prediction accuracy with typically more sophisticated models in which stronger learning capabilities were embedded. One of the most successful AI techniques was the neural network, which generally achieved the best results in the reported studies. However, due to the difficulty of interpreting the neural network models, most studies that applied neural networks focused on prediction accuracy. Few efforts to use neural network models to provide better understanding of the bond-rating process have been reported in the literature.

This research attempts to extend previous research in two directions. Firstly, we are interested in applying a relatively new learning algorithm, support vector machines (SVM), to the bond-rating prediction problem. SVM is a novel learning machine based on statistical learning theory, which has yielded excellent generalization performance on a wide range of problems. We expect to improve prediction accuracy by adopting this new algorithm. Secondly, we want to apply the results from previous research on neural network model interpretation to the bond-rating problem, and to try to provide some insights about the bond-rating process through neural network models.

Thirdly, although there are different markets, such as the United States market and Korean market, few efforts have been made to provide cross-market analysis. Based on interpretation of neural network models, we aim to explore the differences between bondrating processes in different markets.

## 5. Analytical methods

The literature of bond-rating prediction has shown that backpropagation neural networks have achieved better accuracy level than other statistical methods (multiple linear regression, multiple discriminant analysis, logistic regression, etc.) and other machine learning algorithms (inductive learning methods such as decision trees). In this study, we chose backpropagation neural networks and a newly introduced learning method, support vector machines, to analyze bond ratings. We provide some brief descriptions of the two methods in this section. Since neural network is a widely adopted method, we will focus more on the relatively new method, support vector machines.

## 5.1. Backpropagation neural network

Backpropagation neural networks have been extremely popular for their unique learning capability [48] and have been shown to perform well in different applications in our previous research such as medical application [43] and game playing [4]. A typical backpropagation neural network consists of a threelayer structure: input-layer nodes, output-layer nodes and hidden-layer nodes. In our study, we used financial variables as the input nodes and rating outcome as the output layer nodes.

Backpropagation networks are fully connected, layered, feed-forward models. Activations flow from the input layer through the hidden layer, then to the output layer. A backpropagation network typically starts out with a random set of weights. The network adjusts its weights each time it sees an input –output pair. Each pair is processed at two stages, a forward pass and a backward pass. The forward pass involves presenting a sample input to the network and letting activations flow until they reach the output layer. During the backward pass, the network’s actual output is compared with the target output and error estimates are computed for the output units. The weights connected to the output units are adjusted to reduce the errors (a gradient descent method). The error estimates of the output units are then used to derive error estimates for the units in the hidden layer. Finally, errors are propagated back to the connections stemming from the input units. The backpropagation network updates its weights incrementally until the network stabilizes. For algorithm details, readers are referred to Refs. [1,48].

Although researchers have tried different neural network architecture selection methods to build the optimal neural network model for better prediction performance [30], in this study, we used a standard three-layer fully connected backpropagation neural network, in which the input layer nodes are financial variables, output nodes are bond-rating classes, and the number of hidden layer nodes is (number of input nodes + number of output nodes)/2. We followed this standard neural network architecture because it provides comparable results to the optimal architecture and works well as a benchmark for comparison.

## 5.2. Support vector machines

Recent advances in statistics, generalization theory, computational learning theory, machine learning and complexity have provided new guidelines and deep insights into the general characteristics and nature of the model building/learning/fitting process [14]. Some researchers have pointed out that statistical and machine learning models are not all that different conceptually [29,46]. Many of the new computational and machine learning methods generalize the idea of parameter estimation in statistics. Among these new methods, Support Vector Machines have attracted most interest in the last few years.

Support vector machine (SVM) is a novel learning machine introduced first by Vapnik [45]. It is based on the Structural Risk Minimization principle from computational learning theory. Hearst et al. [18] positioned the SVM algorithm at the intersection of learning theory and practice: ‘‘it contains a large class of neural nets, radial basis function (RBF) nets, and polynomial classifiers as special cases. Yet it is simple enough to be analyzed mathematically, because it can be shown to correspond to a linear method in a highdimensional feature space nonlinearly related to input space.’’ In this sense, support vector machines can be a good candidate for combining the strengths of more theory-driven and easy to be analyzed conventional statistical methods and more data-driven, distributionfree and robust machine learning methods.

In the last few years, there have been substantial developments in different aspects of support vector machine. These aspects include theoretical understanding, algorithmic strategies for implementation and reallife applications. SVM has yielded excellent generalization performance on a wide range of problems including bioinformatics [2,21,52], text categorization [23], image detection [32], etc. These application domains typically have involved high-dimensional input space, and the good performance is also related to the fact that SVM’s learning ability can be independent of the dimensionality of the feature space.

The SVM approach has been applied in several financial applications recently, mainly in the area of time series prediction and classification [42,44]. A recent study closely related to our work investigated the use of the SVM approach to select bankruptcy predictors. They reported that SVM was competitive and outperformed other classifiers (including neural networks and linear discriminant classifier) in terms of generalization performance [12]. In this study, we are interested in evaluating the performance of the SVM approach in the domain of credit rating prediction in comparison with that of backpropagation neural networks. A simple description of the SVM algorithm is provided here, for more details please refer to Refs. [7,31].

The underlying theme of the class of supervised learning methods is to learn from observations. There is an input space, denoted by $X , X \subseteq R ^ { n }$ , an output space, denoted by Y, and a training set, denoted by S, $S { = } ( ( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } ) , . . . , ( x _ { l } , y _ { l } ) ) { \subseteq } ( X \times Y ) ^ { l }$ , l is the size of the training set. The overall assumption for learning is the existence of a hidden function $Y { = } f ( X )$ , and the task of classification is to construct a heuristic function h(X), such that $h  f$ on the prediction of Y. The nature of the output space Y decides the learning type. $Y = \{ 1 , - 1 \}$ leads to a binary classification problem, $Y = \{ 1 , 2 , 3 , . . . . m \}$ leads to a multiple class classification problem, and $Y \subseteq R ^ { n }$ leads to a regression problem.

SVM belongs to the type of maximal margin classifier, in which the classification problem can be represented as an optimization problem, as shown in Eq. (1).

$$
\begin{array}{l} \min _ {w, b} <   w, w > \\ s. t. y _ {i} (<   w, \phi (x _ {i}) > + b) \geq 1, \\ i = 1, \ldots , l \end{array}\tag{1}
$$

Vapnik [45] showed how training a support vector machine for pattern recognition leads to a quadratic optimization problem with bound constraints and one linear equality constraint (Eq. (2)). The quadratic optimization problem belongs to a type of problem that we understand very well, and because the number of training examples determines the size of the problem, using standard quadratic problem solvers will easily make the computation impossible for large size training sets. Different solutions have been proposed on solving the quadratic programming problem in SVM by utilizing its special properties. These strategies include gradient ascent methods, chunking and decomposition and Platt’s Sequential Minimal Optimization (SMO) algorithm (which extended the chunking approach to the extreme by updating two parameters at a time) [35].

$$
\begin{array}{l} \max W (\alpha) = \sum_ {i = 1} ^ {l} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {l} y _ {i} y _ {j} \alpha_ {i} \alpha_ {j} <   \phi (x _ {i}), \phi (x _ {j}) > \\ = \sum_ {i = 1} ^ {l} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {l} y _ {i} y _ {j} \alpha_ {i} \alpha_ {j} K (x _ {i}, x _ {j}) s. t. \sum_ {i = 1} ^ {l} y _ {i} \alpha_ {i} \\ = 0, \alpha_ {i} > 0, i = 1, \dots l \end{array} \tag {2}
$$

where a kernel function, $K ( x _ { i } , x _ { j } )$ , is applied to allow all necessary computations to be performed directly in the input space (a kernel function $K ( x _ { i } , x _ { j } )$ is a function of the inner product between $x _ { i }$ and $x _ { j } ,$ thus it transforms the computation of inner product $< \phi ( x _ { i } ) , \phi ( x _ { j } ) >$ to that of $< x _ { i } , x _ { j } > )$ . Conceptually, the kernel functions map the original data into a higher-dimension space and make the input data set linearly separable in the transformed space. The choice of kernel functions is highly application-dependent and it is the most important factor in support vector machine applications.

The formulation in Eq. (2) only considers the separable case, which corresponds to an empirical error of zero. For noisy data, slack variables are introduced to relax the hard-margin constraints to allow for some classification errors [5], as shown in Eq. (3). In this new formulation, noise level C>0 determines the tradeoff between the empirical error and the complexity term.

$$
\begin{array}{l} \min _ {w, b, \xi} <   w, w > + C \sum_ {i = 1} ^ {n} \xi_ {i} \\ y _ {i} (<   w, \phi (x _ {i}) > + b) \geq 1 - \xi_ {i}, \xi_ {i} \geq 0, i = 1, \dots , l \end{array}\tag{3}
$$

This extended formulation leads to the dual problem described in Eq. (4).

$$
\begin{array}{l} \max W (\alpha) = \sum_ {i = 1} ^ {l} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {l} y _ {i} y _ {j} \alpha_ {i} \alpha_ {j} <   \phi (x _ {i}), \\ \phi (x _ {j}) > = \sum_ {i = 1} ^ {l} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {l} y _ {i} y _ {j} \alpha_ {i} \alpha_ {j} K (x _ {i}, x _ {j}) s. t. \sum_ {i = 1} ^ {l} y _ {i} \alpha_ {i} \\ = 0, 0 \leq \alpha_ {i} C, i = 1, \dots l \end{array}\tag{4}
$$

The standard SVM formulation solves only the binary classification problem, so we need to use several binary classifiers to construct a multi-class classifier or make fundamental changes to the original formulation to consider all classes at the same time. Hsu and Lin’s recent paper [20] compared several methods for multi-class support vector machines and concluded that the ‘‘one-against-one’’ and DAG methods are more suitable for practical uses. We used the software package Hsu and Lin provided, BSVM, for our study. We experimented with different SVM parameter settings on the credit rating data, including the noise level C and different kernel functions (including the linear, polynomial, radial basis and sigmoid function). We also experimented with different approaches for multi-class classification using SVM [20]. The final SVM setting used Crammer and Singer’s formulation [6] for multi-class SVM classification, a radial basis kernel function $( K ( x _ { i } ,$ $x _ { j } ) = e ^ { - \gamma | x _ { i } - x _ { j } | ^ { 2 } } , \gamma = 0 . 1 ) ^ { 1 }$ , and C with a value of 1000. This setting achieved a relatively better performance on the credit rating data set.

## 6. Data sets

For the purpose of this study, we prepared two bond-rating data sets from the United States and Taiwan markets.

## 6.1. Taiwan data set

Corporate credit rating has a relatively short history in Taiwan. Taiwan Ratings Corporation (TRC) is the first credit rating service organization in Taiwan and is currently partnering with Standard and Poor’s. Established in 1997, the TRC started rating companies in February 1998. It has a couple of hundred rating results so far, over half of which are credit ratings of financial institutes. We obtained the rating information from TRC and limited our target to financial organizations because of the data availability.

Companies requesting for credit ratings are required to provide their last five annual reports and financial statements of the last three quarter at the beginning of the rating process. Usually, it takes 3 to 6 months for the rating process, depending on the scheduling of required conferences with the high-level management.

We obtained fundamental financial variables from Securities and Futures Institute (SFI). Publicly traded companies report their quarterly financial statements and financial ratios to the SFI quarterly. Although the SFI has 36 financial ratios in its database, not every company reported all 36 financial ratios, and some ratios are not used by most industries. We needed to match the financial data from SFI with the rating information from TRC. To keep more data points, we decided to use financial variables two quarters before the rating release date as the basis for rating prediction. It is reasonable to assume that the most recent financial information contributes most to the bondrating results. We obtained the releasing date of the ratings and the company’s fiscal year information, and used the financial variables two quarters prior to the rating release to form a case in our data set. After matching and filtering data with missing values, we obtained a data set of 74 cases with bank credit rating and 21 financial variables, which covered 25 financial institutes from 1998 to 2002. Five rating categories appeared in our data set, including twAAA, twAA, twA, twBBB and twBB.

## 6.2. United States data set

We prepared a comparable US corporate rating data set to the Taiwan data set from Standard and Poor’s Compustat data set. We obtained comparable financial variables with those in the Taiwan data set, and the S and P senior debt rating for all the commercial banks (DNUM 6021). The data set covered financial variables and ratings from 1991 to 2000. Since the rating release date was not available, financial variables of the first quarter were used to match with the rating results. After filtering data with missing values, we obtained 265 cases of 10-year data for 36 commercial banks. Five rating categories appeared in our data set, including AA, A, BBB, BB and B. The distributions of the credit rating categories of the two data sets are presented in Table 2.

## 6.3. Variable selection

The financial variables we obtained in the Taiwan data set are listed in Table 3. These variables include the financial ratios that were available in the SFI database and two balance measures frequently used in bond-rating prediction literature, total assets and total liabilities. The first seven variables are frequently used financial variables in prior bond-rating prediction studies. Some other financial ratios are not commonly used in US; therefore, short descriptions are provided.

We ran ANOVA on the Taiwan data set to test whether the differences between different rating classes were significant in each financial variable. If the difference was not significant (high p-value), the financial variable was considered not informative with regard to the bond-rating decision. Table 3 shows pvalues of each variable, which provides information about whether or not the difference is significant. We eliminated five ratios in our data set that had relatively high p-values (X5, X9, X17, X19 and X20). Thus, we kept 14 ratios and two balance measures in our final Taiwan data set. For better comparison of the two markets, we tried to use similar variables in the US market. Two ratios were not available in US data set (X6 and X21). Therefore, the US data set contained 12 available ratios and two balance measures<sup>2</sup>.

Ratings in the two data sets

<table><tr><td>TW data</td><td></td><td>US data</td><td></td></tr><tr><td>twAAA</td><td>8</td><td>AA</td><td>20</td></tr><tr><td>twAA</td><td>11</td><td>A</td><td>181</td></tr><tr><td>twA</td><td>31</td><td>BBB</td><td>56</td></tr><tr><td>twBBB</td><td>23</td><td>BB</td><td>7</td></tr><tr><td>twBB</td><td>1</td><td>B</td><td>1</td></tr><tr><td>Total</td><td>74</td><td>Total</td><td>265</td></tr></table>

Table 3  
Financial ratios used in the data set

<table><tr><td></td><td>Financial ratio name/description</td><td>ANOVA between-group p-value</td></tr><tr><td>X1</td><td>Total assets</td><td>0.00</td></tr><tr><td>X2</td><td>Total liabilities</td><td>0.00</td></tr><tr><td>X3</td><td>Long-term debts/total invested capital</td><td>0.12</td></tr><tr><td>X4</td><td>Debt ratio</td><td>0.00</td></tr><tr><td>X5</td><td>Current ratio</td><td>0.36</td></tr><tr><td>X6</td><td>Times interest earned (EBIT/interest)</td><td>0.00</td></tr><tr><td>X7</td><td>Operating profit margin</td><td>0.00</td></tr><tr><td>X8</td><td>(Shareholders’ equity + long-term debt)/fixed assets</td><td>0.00</td></tr><tr><td>X9</td><td>Quick ratio</td><td>0.37</td></tr><tr><td>X10</td><td>Return on total assets</td><td>0.01</td></tr><tr><td>X11</td><td>Return on equity</td><td>0.04</td></tr><tr><td>X12</td><td>Operating income/received capitals</td><td>0.00</td></tr><tr><td>X13</td><td>Net income before tax/received capitals</td><td>0.00</td></tr><tr><td>X14</td><td>Net profit margin</td><td>0.00</td></tr><tr><td>X15</td><td>Earnings per share</td><td>0.00</td></tr><tr><td>X16</td><td>Gross profit margin</td><td>0.02</td></tr><tr><td>X17</td><td>Non-operating income/sales</td><td>0.81</td></tr><tr><td>X18</td><td>Net income before tax/sales</td><td>0.00</td></tr><tr><td>X19</td><td>Cash flow from operating activities/current liabilities</td><td>0.84</td></tr><tr><td>X20</td><td>(Cash flow from operating activities/(capital expenditures + increased in inventory + cash dividends)) in last 5 years</td><td>0.64</td></tr><tr><td>X21</td><td>(Cash flow from operating activities-cash dividends)/(fixed assets + other assets + working capitals)</td><td>0.08</td></tr></table>

## 7. Experiment results and analysis

Based on the two data sets, we prepared for the two markets, we constructed four models for an initial experiment. For each market, we constructed a simple model with commonly used financial variables and a complex model with all available financial variables. The models we constructed are the following. TW I: Rating = f(X1, X2, X3, X4, X6, X7), TW II: Rating = f(X1, X2, X3, X4, X6, X7, X8, X10, X11, X12, X13, X14, X15, X16, X18, X21), US I: Rating = f(X1, X2, X3, X4, X7), and US II: Rating = f(X1, X2, X3, X4, X7, X8, X10, X11, X12, X13, X14, X15, X16, X17).

## 7.1. Prediction accuracy analysis

For each of the four models, we used backpropagation neural network and support vector machines to predict the bond ratings. To evaluate the prediction performance, we followed the 10-fold cross-validation procedure, which has shown good performance in model selection [46]. Because some credit rating classes had a very small number of data points for both the US and Taiwan datasets, we also conducted the leaveone-out cross-validation procedure to access the prediction performances. When performing the crossvalidation procedures for the neural networks, 10% of the data was used as a validation set. Table 4 summarizes the prediction accuracies of the four models using both cross-validation procedures. For comparison purposes, the prediction accuracies of a regression model that achieved relatively good performance in the literature, the logistic regression model, are also reported in Table 4. The following observations are summarized: support vector machines achieved the best performance in three of the four models that we tested; support vector machines and neural networks model outperformed the logistic regression model consistently; the 10-fold and leave-one-out cross-validation procedures obtained comparable prediction accuracies.

Prediction accuracies (LogR: logistic regression model, SVM: support vector machines, NN: neural networks)

<table><tr><td rowspan="2"></td><td colspan="3">10-fold Cross-validation</td><td colspan="3">Leave-one-out Cross-validation</td></tr><tr><td>LogR (%)</td><td>SVM (%)</td><td>NN (%)</td><td>LogR (%)</td><td>SVM (%)</td><td>NN (%)</td></tr><tr><td>TW I</td><td>72.97</td><td>79.73</td><td>75.68</td><td>75.68</td><td>79.73</td><td>74.32</td></tr><tr><td>TW II</td><td>70.27</td><td>77.03</td><td>75.68</td><td>70.27</td><td>75.68</td><td>74.32</td></tr><tr><td>US I</td><td>76.98</td><td>78.87</td><td>80.00</td><td>75.09</td><td>80.38</td><td>80.75</td></tr><tr><td>US II</td><td>75.47</td><td>80.00</td><td>79.25</td><td>75.47</td><td>80.00</td><td>75.68</td></tr></table>

Many previous studies using backpropagation neural networks have provided analysis of prediction errors in the number of rating categories. We also prepared Table 5 to show the ability of the backpropagation neural network to get predictions within one class away from actual rating. We can conclude that the probabilities for the predictions to be within one class away from the actual rating were over 90% for all four models.

We can draw several conclusions from the experiment results obtained. First, our results conform to prior research results indicating that analytical models based on publicly available financial information built by machine learning algorithms could provide accurate predictions. Although the rating agencies and many institutional writers emphasize the importance of subjective judgment of the analyst in determining the ratings, it appeared that a relatively small list of financial variables largely determined the rating results. This phenomenon appears consistently in different financial markets. In our study, we obtained the highest prediction accuracies of 79.73% for Taiwan data set and 80.75% for the United States data set. Second, support vector machines slightly improved the credit rating prediction accuracies. Third, the results also showed that models using the small set of financial variables that have been frequently used in the literature achieved comparable and in some cases, even better results than models using a larger set of financial variables. This validated that the set of financial variables identified in previous studies captured the most relevant information for the credit rating decision.

## 7.2. Variable contribution analysis

Another focus of this study was on the interpretability of machine learning based models. By examining the input variables and accuracies of the models, we could provide useful information about the bond-rating process. For example, in our study, we could conclude that bond raters largely rely on a small list of financial variables to make rating decisions. However, it is generally difficult to interpret the relative importance of the variables in the models for either support vector machines or neural networks. In fact, this limitation has been a frequent complaint about neural networks in the literature [41,50]. In the case of bond-rating prediction, neural networks have been shown in many studies to have excellent accuracy performance, but little effort has been made in prior studies to try to explain the results. In this study, we tried to extend previous research by applying results from recent research in neural network model interpretation, and to try to find out the relative importance of selected financial variables to the bond-rating problem.

Within-1-class accuracy results

<table><tr><td rowspan="2">Acutal rating</td><td colspan="5">Predicted rating</td><td rowspan="2">Acutal rating</td><td colspan="5">Predicted rating</td></tr><tr><td>twAAA</td><td>twAA</td><td>twA</td><td>twBBB</td><td>twBB</td><td>twAAA</td><td>twAA</td><td>twA</td><td>twBBB</td><td>twBB</td></tr><tr><td>twAAA</td><td>7</td><td>0</td><td>1</td><td>0</td><td>0</td><td>twAAA</td><td>5</td><td>0</td><td>2</td><td>1</td><td>0</td></tr><tr><td>twAA</td><td>0</td><td>10</td><td>1</td><td>0</td><td>0</td><td>twAA</td><td>0</td><td>9</td><td>2</td><td>0</td><td>0</td></tr><tr><td>twA</td><td>4</td><td>1</td><td>23</td><td>3</td><td>0</td><td>twA</td><td>2</td><td>4</td><td>22</td><td>2</td><td>0</td></tr><tr><td>twBBB</td><td>1</td><td>0</td><td>6</td><td>16</td><td>0</td><td>twBBB</td><td>0</td><td>0</td><td>5</td><td>17</td><td>1</td></tr><tr><td>twBB</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>twBB</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td colspan="6">TW I: within-1-class accuracy: 91.89%</td><td colspan="6">TW II: within-1-class accuracy: 93.24%</td></tr><tr><td rowspan="2">Acutal rating</td><td colspan="5">Predicted rating</td><td rowspan="2">Acutal rating</td><td colspan="5">Predicted rating</td></tr><tr><td>AA</td><td>A</td><td>BBB</td><td>BB</td><td>B</td><td>AA</td><td>A</td><td>BBB</td><td>BB</td><td>B</td></tr><tr><td>AA</td><td>0</td><td>20</td><td>0</td><td>0</td><td>0</td><td>AA</td><td>6</td><td>13</td><td>1</td><td>0</td><td>0</td></tr><tr><td>A</td><td>0</td><td>178</td><td>3</td><td>0</td><td>0</td><td>A</td><td>2</td><td>165</td><td>12</td><td>2</td><td>0</td></tr><tr><td>BBB</td><td>0</td><td>23</td><td>33</td><td>0</td><td>0</td><td>BBB</td><td>0</td><td>16</td><td>37</td><td>2</td><td>1</td></tr><tr><td>BB</td><td>0</td><td>2</td><td>5</td><td>0</td><td>0</td><td>BB</td><td>0</td><td>0</td><td>0</td><td>2</td><td>3</td></tr><tr><td>B</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>B</td><td>0</td><td>0</td><td>0</td><td>4</td><td>1</td></tr><tr><td colspan="6">US I: within-1-class accuracy: 97.74%</td><td colspan="6">US II: within-1-class accuracy: 98.44%</td></tr></table>

Before further analysis on the neural network model, we optimized the backpropagation models for both Taiwan and United States markets by selecting optimal sets of input financial variables following a procedure similar to that of step-wise regression. We started from the simple model, we constructed (US I and TW I), and then tried to remove each financial variable in the model and to add each remaining financial variable one at a time. During this process, we modified the model if any prediction accuracy improvement was observed. We iterated the process with the modified model until no improvement was observed. The optimal neural network models we obtained for the two markets were TW III: Rating = f(X1, X2, X3, X4, X6, X7, X8) and US III: Rating = f(X1, X2, X3, X4, X7, X11). We obtained the highest 10-fold cross-validation prediction accuracy from these two models, 77.52% and 81.32%, respectively. The following model interpretation analysis will be based on these two fine-tuned models.

Many researchers have attempted to identify the contribution of the input variables in neural network models. This information can be used to construct the optimal neural network model or to provide better understanding of the models [11]. These methods mainly extract information from the connection strengths (inter-layer weights) of the neural network model to interpret the model. Several studies have tried to analyze the first order derivatives of the neural network with respect to the network parameters (including input units, hidden units and weights). For example, Garson [16] developed measures of relative importance or relative strength [51] of inputs to the network. Other researchers used the connection strengths to extract symbolic rules [40] in order to provide interpretation capability similar to that of decision tree algorithms.

In this study, we were interested in using Garson’s contribution measures to evaluate the relative importance of the input variables in the bond-rating neural network models. Both of these two measures are based on a typical three-layer backpropagation neural network. We use the following notations to describe the two measures. Consider a neural network with I input units, J hidden units, and K output units. The connection strengths between input, hidden and output layers are denoted as $w _ { j i }$ and $\nu _ { j k } ,$ where $i = 1 , . . . I , j = 1 , . . . , J$ and $k { = } 1 , \ \ldots { } K .$ Garson’s measure of relative contribution of input i on output k is defined as $\operatorname { E q . } \left( 5 \right)$ and Yoon et al.’s measure is defined as Eq. (6).

$$
\operatorname{Con} _ {i k} = \frac {\sum_ {j = 1} ^ {J} \frac {\left| w _ {j i} \right\rVert v _ {j k} |}{\sum_ {i = 1} ^ {I} \left| w _ {j i} \right|}}{\sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {J} \frac {\left| w _ {j i} \right\rVert v _ {j k} |}{\sum_ {i = 1} ^ {I} \left| w _ {j i} \right|}}\tag{5}
$$

$$
\operatorname{Con} _ {i k} = \frac {\sum_ {j = 1} ^ {J} w _ {j i} v _ {j k}}{\sum_ {i = 1} ^ {I} \left| \sum_ {j = 1} ^ {J} w _ {j i} v _ {j k} \right|}\tag{6}
$$

Garson’s method places more emphasis on the connection strengths from the hidden layer to the output layer, but it does not measure the direction of the influence. The two methods both measure the relative contribution of each input variable to each of the output units. The number of output nodes in our neural network architecture was the number of bondrating classes. Thus, the contribution measures described above will evaluate the contribution of each input variables to each of the bond-rating classes. This brought some problems to interpret Yoon’s contribution measures. The direction of the influence of an input financial variable may be different across bondrating classes. With relatively large number of bondrating classes, the results we obtained were too complicated to permit interpreting the contribution measures and did not improve understanding of the bond-rating process. On the other hand, the contribution analysis results from Garson’s method showed that input variables made similar contributions to different bond-rating classes, which allowed us to understand the relative importance of different input financial variables in our neural network models. We summarize the results we obtained using Garson’s method in Fig. 1.

![](/api/attachments/FFD5P5PS/fulltext/images/6740c760733502fe12341ac235c555bf7a6c955ec588b61938b1795094b02630.jpg)

![](/api/attachments/FFD5P5PS/fulltext/images/e7b186a49f476f6b1dac81386434cdaaede126e36e0d5e4652506a5246d7e5fa.jpg)  
Fig. 1. Financial variable contribution based on Garson’s measure.

## 7.3. Cross-market analysis

Using Garson’s contribution measure, we can assess the relative importance of each input financial variable to the bond-rating process in different markets. Since the neural network models we constructed for the Taiwan and the United States markets both achieved prediction accuracy close to 80%, we believe that information about variable importance extracted from the models also to a large extent captures the bond raters’ behavior.

As showed in Fig. 1, although the optimal neural network models for Taiwan and US data sets used a similar list of input financial variables (five financial variables including X1, X2, X3, X4 and X7 were selected by both models), the relative importance of different financial variables was quite different in the two models. For the US model, X1, X2, X3, and X7 were more important, while X4 and X11 were relatively less important. For the Taiwan market, X4, X7, X8 were more important while X1, X2, X3 and X6 were relatively less important.

The important financial variables in the US model were total assets, total liabilities, long-term debts/total invested capital and operating profit margin, while debt ratio, operating profit margin, and (shareholders’ equity + long-term debt)/fixed assets were more important in the Taiwan model. The total assets (X1) and total liabilities (X2) were the most important variables in the US data set, which indicated that US bond raters rely more on the size of the target company in giving ratings. The most important variable for the Taiwan data set was the operating profit margin (X7), which indicated that Taiwan raters focus more on the companies’ profitability when making rating decisions.

A closer study of the characteristics of the data set provided a partial explanation of some of the contributions of the variables in different models. From our experimental data set, the operating profit margin for each rating group in the US data set, except for the B rating group, averaged between 30% and 35%, but the average operating profit margin ranged from 3.6% in BBB group to 40% in AAA group in the Taiwan data set. Thus, operating profit margin in the Taiwan data set provided more information to the credit ratings model than it did to the US model. A similar phenomenon was observed for debt ratio (X4). Debt ratio measures how a company is leveraging its debt against the capital committed by its owners. Based on contemporary financial theory, companies are encouraged to operate at leverage in order to grow rapidly. Most US companies do operate at high leverage. However, similar to most Asian countries, most of Taiwan’s companies are more conservative and choose not to operate at very high leverage. While comparing the two data sets, we found that every rating group in the US data set had average debt ratio over 90%; no rating group in the Taiwan data set had average debt ratio higher than 90%. For example, the AAA group in Taiwan data set had average debt ratio of 37%, which was much lower than the debt ratios of most US companies. This information confirmed our variable contribution analysis, where the debt ratio was assigned as having the least contribution in the US model while it was one of the more important variables in the Taiwan data set.

In summary, we extended prior research by adopting relative importance measures of to interpret relative importance of input variables in bond-rating neural network models. The results we obtained showed quite different characteristics of bond-rating processes in Taiwan and the United States. We tried to provide some explanations of the contribution analysis results by examining the data distribution characteristics in different data sets. However, expert judgment and field study are needed to further rationalize and evaluate the relative importance information extracted from the neural network models.

## 8. Discussion and future directions

In this study, we applied a newly introduced learning method based on statistical learning theory, support vector machines, together with a frequently used highperformance method, backpropagation neural networks, to the problem of credit rating prediction. We used two data sets for Taiwan financial institutes and United States commercial banks as our experiment testbed. The results showed that support vector machines achieved accuracy comparable to that of backpropagation neural networks. Applying the results from research in neural network model interpretation, we conducted input financial variable contribution analysis and determined the relative importance of the input variables. We believe this information can help users understand the bond-rating process better. We also used the contribution analysis results to compare the characteristics of bond-rating processes in the United States and Taiwan markets. We found that the optimal models we built for the two markets used similar lists of financial variables as inputs but found the relative importance of the variables was quite different across the two markets.

One future direction of the research would be to conduct a field study or a survey study to compare the interpretation of the bond-rating process we have obtained from our models with bond-rating experts’ knowledge. Deeper market structure analysis is also needed to fully explain the differences we found in our models.

## Acknowledgements

This research is partly supported by NSF Digital Library Initiative-2, ‘‘High-performance Digital Library Systems: From Information Retrieval to Knowledge Management’’, IIS-9817473, April 1999 –March 2002.

We would like to thank Securities and Futures Institute for providing the dataset and assistance from Ann Hsu during the project. We would also like to thank Dr. Jerome Yen for the valuable comments during the initial stage of this research.

## References

[1] C.M. Bishop, Neural Networks for Pattern Recognition, Oxford Univ. Press, New York, 1995.

[2] M.P. Brown, W.N. Grudy, D. Lin, N. Cristianini, C.W. Sugnet, T.S. Furey, M. Ares, D. Haussler, Knowledge-based analysis of microarray gene expression data by using support vector machines. Proceedings of National Academy of Sciences 97 (1) (2000) 262 – 267.

[3] R. Chaveesuk, C. Srivaree-Ratana, A.E. Smith, Alternative neural network approaches to corporate bond rating, Journal of Engineering Valuation and Cost Analysis 2 (2) (1999) 117– 131.

[4] H. Chen, P. Buntin, L. She, S. Sutjahjo, C. Sommer, D. Neely, Expert prediction, symbolic learning, and neural networks: an experiment on greyhound racing, IEEE Expert 9 (6) (1994) 21–27.

[5] C. Cortes, V.N. Vapnik, Support vector networks, Machine Learning 20 (1995) 273– 297.

[6] K. Crammer, Y. Singer, On the learnability and design of output codes for multiclass problems, Proceedings of the Thirteenth Annual Conference on Computational Learning Theory, Morgan Kaufmann, San Francisco, 2000, pp. 35– 46.

[7] N. Cristianini, J. Shawe-Taylor, An Introduction to Support Vector Machines, Cambridge Univ. Press, Cambridge, New York, 2000.

[8] E.B. Deakin, Discriminant analysis of predictors of business failure, Journal of Accounting Research (1976) 167 – 179.

[9] S. Dutta, S. Shekhar, Bond rating: a non-conservative application of neural networks, Proceedings of IEEE International Conference on Neural Networks, 1988, pp. II443 – II450.

[10] H.L. Ederington, Classification models and bond ratings, Financial Review 20 (4) (1985) 237 – 262.

[11] A. Engelbrecht, I. Cloete, Feature extraction from feedforward neural networks using sensitivity analysis, Proceedings of the International Conference on Systems, Signals, Control, Computers, 1998, pp. 221 – 225.

[12] A. Fan, M. Palaniswami, Selecting bankruptcy predictors using a support vector machine approach, Proceedings of the International Joint Conference on Neural Networks, 2000.

[13] L. Fisher, Determinants of risk premiums on corporate bonds, Journal of Political Economy (1959) 217 – 237.

[14] J. Galindo, P. Tamayo, Credit risk assessment using statistical and machine learning: basic methodology and risk modeling applications, Computational Economics 15 (1 – 2) (2000) 107–143.

[15] S. Garavaglia, An application of a Counter-Propagation Neural Networks: Simulating the Standard & Poor’s Corporate

Bond Rating System, Proceedings of the First International Conference on Artificial Intelligence on Wall Street, 1991, pp. 278 – 287.

[16] D. Garson, Interpreting neural-network connection strengths, AI Expert (1991) 47– 51.

[17] J.A. Gentry, D.T. Whitford, P. Newbold, Predicting industrial bond ratings with a probit model and funds flow components, Financial Review 23 (3) (1988) 269–286.

[18] M.A. Hearst, S.T. Dumais, E. Osman, J. Platt, B. Scho¨ lkopf, Support vector machines, IEEE Intelligent Systems 13 (4) (1998) 18– 28.

[19] J.O. Horrigan, The determination of long term credit standing with financial ratios, Journal of Accounting Research, Supplement (1966) 44– 62.

[20] C.W. Hsu, C.J. Lin, A comparison of methods for multi-class support vector machines, Technical report, National Taiwan University, Taiwan, 2001.

[21] T.S. Jaakkola, D. Haussler, Exploiting generative models in discriminative classifiers, in: M.S. Kearns, S.A. Solla, D.A. Cohn (Eds.), Advances in Neural Information Processing Systems, MIT Press, Cambridge, 1998.

[22] J.D. Jackson, J.W. Boyd, A statistical approach to modeling the behavior of bond raters, The Journal of Behavioral Economics 17 (3) (1988) 173 – 193.

[23] T. Joachims, Text categorization with support vector machines, Proceedings of the European Conference on Machine Learning (ECML), 1998.

[24] R.S. Kaplan, G. Urwitz, Statistical models of bond ratings: a methodological inquiry, The Journal of Business 52 (2) (1979) 231– 261.

[25] J.W. Kim, Expert systems for bond rating: a comparative analysis of statistical, rule-based and neural network systems, Expert Systems 10 (1993) 167 – 171.

[26] C.L. Kun, H. Ingoo, K. Youngsig, Hybrid neural network models for bankruptcy predictions, Decision Support Systems 18 (1) (1996) 63 – 72.

[27] Y.S. Kwon, I.G. Han, K.C. Lee, Ordinal Pairwise Partitioning (OPP) approach to neural networks training in bond rating, Intelligent Systems in Accounting, Finance and Management 6 (1997) 23– 40.

[28] J.J. Maher, T.K. Sen, Predicting bond ratings using neural networks: a comparison with logistic regression, Intelligent Systems in Accounting, Finance and Management 6 (1997) 59 – 72.

[29] D. Michie, D.J. Spiegelhalter, C.C. Taylor, Machine Learning, Neural and Statistical Classification, Elis Horwood, London, 1994.

[30] J. Moody, J. Utans, Architecture selection strategies for neural networks application to corporate bond rating, in: A. Refenes (Ed.), Neural Networks in the Capital Markets, Wiley, Chichester, 1995, pp. 277 – 300.

[31] K.-R. Mu¨ller, S. Mika, G. Ratsch, K. Tsuda, B. Scho¨ lkopf, An introduction to kernel-based learning algorithms, IEEE Transactions on Neural Networks 12 (2) (2001) 181– 201.

[32] E. Osuna, R. Freund, F. Girosi, Training support vector machines: an application to face detection, Proceedings of Computer Vision and Pattern Recognition, 1997, pp. 130 – 136.

[33] G.E. Pinches, K.A. Mingo, A multivariate analysis of industrial bond ratings, Journal of Finance 28 (1) (1973) 1 – 18.

[34] G.E. Pinches, K.A. Mingo, The role of subordination and industrial bond ratings, Journal of Finance 30 (1) (1975) 201– 206.

[35] J.C. Platt, Fast training of support vector machines using sequential minimum optimization, in: B. Scho¨lkopf, C. Burges, A. Smola (Eds.), Advances in Kernel Methods-Support Vector Learning, MIT Press, Cambridge, 1998, pp. 185 – 208.

[36] T.F. Pogue, R.M. Soldofsky, What’s in a bond rating? Journal of Financial and Quantitative Analysis 4 (2) (1969) 201– 228.

[37] K.S. Shin, I. Han, A case-based approach using inductive indexing for corporate bond rating, Decision Support Systems 32 (2001) 41 – 52.

[38] J.C. Singleton, A.J. Surkan, Neural networks for bond rating improved by multiple hidden layers, Proceedings of the IEEE International Conference on Neural Networks, 1990, pp. 163 – 168.

[39] J.C. Singleton, A.J. Surkan, Bond rating with neural networks, in: A. Refenes (Ed.), Neural Networks in the Capital Markets, Wiley, Chichester, 1995, pp. 301 – 307.

[40] I.A. Taha, J. Ghosh, Symbolic interpretation of artificial neural networks, IEEE Transactions on Knowledge and Data Engineering 11 (3) (1999) 448–463.

[41] K. Tam, M. Kiang, Managerial application of neural networks: the case of bank failure predictions, Management Science 38 (7) (1992) 926– 947.

[42] F.E.H. Tay, L.J. Cao, Modified support vector machines in financial time series forecasting, Neurocomputing 48 (2002) 847– 861.

[43] K.M. Tolle, H. Chen, H. Chow, Estimating drug/plasma concentration levels by applying neural networks to pharmacokinetic data sets, Decision Support Systems, Special Issue on Decision Support for Health Care in a New Information Age 30 (2) (2000) 139– 152.

[44] T. Van Gestel, J.A.K. Suykens, D.-E. Baestaens, A. Lambrechts, G. Lanckriet, B. Vandaele, B. De Moor, J. Vandewalle, Financial time series prediction using least squares support vector machines within the evidence framework, IEEE Transactions on Neural Networks 12 (4) (2001) 809– 821.

[45] V. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag, New York, 1995.

[46] S.M. Weiss, C.A. Kulikowski, Computer Systems That Learn: Classification and Prediction Methods from Statistics, Neural Networks, Machine Learning and Expert Systems, Morgan Kaufmann, San Mateo, 1991.

[47] R.R. West, An alternative approach to predicting corporate bond ratings, Journal of Accounting Research 8 (1) (1970) 118– 125.

[48] B. Widrow, D.E. Rumelhart, M.A. Lehr, Neural networks: applications in industry, business, and science, Communications of the ACM 37 (1994) 93– 105.

[49] R.L. Wilson, S.R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11 (5) (1994) 545– 557.

[50] I.H. Witten, E. Frank, J. Gray, Data Mining: Practical Machine

Learning Tools and Techniques with Java Implementations, Morgan Kaufmann, San Francisco, 1999.

[51] Y. Yoon, T. Guimaraes, G. Swales, Integrating artificial neural networks with rule-based expert systems, Decision Support Systems 11 (1994) 497– 507.

[52] A. Zien, G. Ra¨tsch, S. Mika, B. Scho¨lkopf, T. Lengauer, K.-R. Mu¨ller, Engineering support vector machine kernels that recognize translation initiation sites, Bioinformatics 16 (9) (2000) 799– 807.

![](/api/attachments/FFD5P5PS/fulltext/images/1d4e268964d0e03aa730d47f9d5b7149b2e055bec7df50d79d69af2bc05b015e.jpg)

Zan Huang is a doctoral student in the Department of Management Information Systems at the University of Arizona, and a research associate in the Artificial Intelligence Lab. His current research interests include recommender systems, data mining and text mining for financial applications, intelligent agents and experimental economics-related research for electronic markets. He received a BS in Management Information Systems from Tsinghua Uni-

versity, Beijing, China.  
![](/api/attachments/FFD5P5PS/fulltext/images/51ad58809975bff48bb45be214fef10cc25a8b4d808958af6b23e1f0621d1cb0.jpg)

Hsinchun Chen is McClelland Professor of MIS and Andersen Professor of MIS at the University of Arizona, where he is the director of the Artificial Intelligence Lab and the director of the Hoffman E-Commerce Lab. His articles have appeared in Communications of the ACM, IEEE Computer, Journal of the American Society for Information Science and Technology, IEEE Expert, and many other publications. Professor Chen has received grant awards from

the NSF, DARPA, NASA, NIH, NIJ, NLM, NCSA, HP, SAP, 3COM, and AT and T. He serves on the editorial board of Decision Support Systems and the Journal of the American Society for Information Science and Technology, and has served as the conference general chair of the International Conferences on Asian Digital Library in the past 4 years.

![](/api/attachments/FFD5P5PS/fulltext/images/5b96d8306b79f769f8e6013e3f6aa5f1aa1a096f4b8f2b62cd65c0834bfc1e7c.jpg)  
pleted CFA level I in 2001.

Chia-Jung Hsu received his BS in Economics from National Taiwan University in 1997, and an MBA in International Management from Thunderbird, the American Graduate School of International Management, in 2000. Currently, he is working towards a Master of Science in Management Information Systems at the University of Arizona. He has experience in the field of security analysis and is a certified security and futures broker (Taiwan). He com-

![](/api/attachments/FFD5P5PS/fulltext/images/0d10b256e257576b9994612c84b35b6d7d67c8fc6b4ae7894c1db5c78a222fd2.jpg)

Wun-Hwa Chen received his PhD in Management Science from the State University of New York at Buffalo in 1989. He is currently a Professor of Operations Management in the Department of Business Administration at National Taiwan University. Prior to his current affiliation, he was an Assistant Professor in the Department of Management and Systems at Washington State University. His research and teaching interests lie in production planning and

scheduling, AI/OR algorithmic design, data mining models for customer relationship management, and mathematical financial modeling. He has published articles in several journals including Annals of Operational Research, IEEE Transactions on Robotics and Automation, European Journal of Operational Research, and Computers and Operations Research. In addition, Dr. Chen has held the Chairmanship in Information Technology Advisory Committees of several government agencies in Taiwan and has extensive consulting experiences with many major corporations in Taiwan. He was also a visiting scholar at the University of New South Wales, Sydney, Australia, in 1995 and the University of Arizona in 2001.

![](/api/attachments/FFD5P5PS/fulltext/images/1364bb2b96022983bbfb0193ffc4f6843ec256d1f848cc69fea8667c10c8e89e.jpg)

Soushan Wu received his PhD in Finance from the University of Florida in 1984. He is a Chair Professor and Dean of the College of Management, Chang-Gung University, Taiwan. He is also a visiting scholar at Clemson University, Hong Kong Polytechnic University. His research interests cover Management Science, Investment Science, Capital Markets, and Information Systems. He has published more than 70 articles in Research in Finance, Financial Manage-

ment, Asia-Pacific Journal of Finance, International Journal of Accounting and Information Systems, etc. He has also served as an ad hoc reviewer for academic journals in the fields of Accounting, Finance, and Information Management. Dr. Soushan Wu serves as a chief editor of the Review of Securities and Futures Markets and Asia-Pacific Journal of Management and Technology.
