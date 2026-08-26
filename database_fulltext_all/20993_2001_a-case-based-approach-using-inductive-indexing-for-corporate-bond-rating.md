---
otero_id: 20993
otero_key: "5ZWE7ZSR"
title: "A case-based approach using inductive indexing for corporate bond rating"
authors: "Kyung-shik Shin; Ingoo Han"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00099-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A case-based approach using inductive indexing for corporate bond rating

Kyung-shik Shin <sup>a,)</sup>, Ingoo Han <sup>b</sup>

<sup>a</sup> College of Business Administration, Ewha Woman’s UniÕersity, 11-1 Daehyun-dong, Seodaemun-gu, Seoul 120-750, South Korea b Graduate School of Management, Korea AdÕanced Institute of Science and Technology, Seoul, South Korea

## Abstract

Case-based reasoning CBR is a problem solving technique by re-using past cases and experiences to find a solution to Ž . problems. The central tasks involved in CBR methods are to identify the current problem situation, find a past case similar to the new one, use that case to suggest a solution to the current problem, evaluate the proposed solution, and update the system by learning from this experience. In doing tasks, one of the critical issues in building a useful CBR system lies in the application of general domain knowledge to the indexing of cases, which may support the retrieval of relevant cases to the problem.

This paper investigates the effectiveness of inductive learning approach to case indexing process for business classification tasks. We suggest this approach as a unifying framework to combine general domain knowledge and case-specific knowledge. Our particular interest involves optimal or near optimal decision trees that represent an optimal combination level between the two knowledge types. The proposed approach is demonstrated by applications to corporate bond rating. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Corporate bond rating; Case-based reasoning; Inductive learning

## 1. Introduction

Case-based reasoning CBR is a problem solvingŽ . technique that is fundamentally different from other major artificial intelligence AI approaches. Instead Ž . of relying on making associations along generalized relationships between problem descriptors and conclusions, CBR benefits from utilizing case-specific knowledge of previously experienced problem situations. A new problem is solved by finding a similar past case and reusing it in the new problem situation. A wide range of applications of CBR has been reported 1,4,7,14,16,17,19,20,23 , including busi-<sup>w</sup> <sup>x</sup> ness classification for decision making such as bond rating 3,26,27 and bankruptcy prediction 2 . <sup>w</sup> <sup>x</sup> <sup>w x</sup>

The central tasks that CBR methods have to deal with are to identify the current problem situation, find a past case similar to the new one, use that case to suggest a solution to the current problem, evaluate the proposed solution and update the system by learning from this experience 12,23,30 . <sup>w</sup> <sup>x</sup>

In doing these major tasks, one of the major issues lies in the retrieval of appropriate cases 8 .<sup>w</sup> <sup>x</sup> An index used to retrieve cases from memory may fail even if there is a relevant case in memory 11 .<sup>w</sup> <sup>x</sup> This happens when the index does not correspond to the one used to index the case. For this reason, the integration of general domain knowledge into case indexing and retrieving processes is highly recommended in building a successful CBR system. The indexing problem 11 refers to the task of storing <sup>w</sup> <sup>x</sup> cases for an effective and efficient retrieval.

In this paper, we discuss the implementation of effective indexing methods to build a case-based system. Our particular interest involves a case indexing approach using induction technique to retrieve more relevant cases. This approach is aimed at unifying case-specific and general domain knowledge within the system. The proposed approach is demonstrated by applications to corporate bond rating.

This paper is organized as follows. The following section provides a brief description of bond rating applications, including a review of prior research relevant to this issue. Section 3 describes the characteristics of CBR methods, including case indexing and retrieving issues. Section 4 explains the integrated approach for an effective CBR system. Sections 5 and 6 report the experiments and empirical results of corporate bond rating applications. The final section discusses the conclusions and future research issues.

## 2. Bond rating applications

## 2.1. A description of corporate bond rating

Corporate bond rating informs the public of the likelihood of an investor receiving the promised principal and interest payments associated with bond issues. Bond ratings by independent rating agencies characterize the risk of the investments and affect the cost of borrowing for the issuer. Agencies such as Moody’s, Standard and Poor, and Fitch earn fees for evaluating the credit status of the firms that issue new bonds. Since market yields correspond to bond ratings, which indicates an association between rating and risk, the study of the rating process is of interest not only to bond issuers but also to investors.

Generally, the rating process includes a review of the package submitted by the issuer containing the following documentation: annual reports for past years, latest quarterly reports, income statement and balance sheet, most recent prospectus for debt issues, and other specialized information and statistical reports. After a review of the package by analysts and a meeting with the issuer, the responsible analyst prepares a rating report and presents it to the rating committee, together with his or her recommendations for a rating. Generally, the decision-making body ultimately responsible for all ratings is the rating’s committee. The committee members review the documentation presented and discuss issues with the analysts involved, who must be able to support and clarify all issues and points raised. A decision made after the review and discussion by the committee is taken as the final rating.

The methods and input variables used for rating are not publicly disclosed. It is generally believed that ratings are to a certain extent judged on the basis of qualitative factors that are not easily quantifiable and on variables not directly related to a particular firm, such as economic conditions. Due to these ambiguities, the ratings cannot be independently reproduced with 100% accuracy. Nevertheless, for financial institutions, it is helpful to be able to evaluate the creditworthiness of a firm independently by estimating the ratings based on a model, since rating agencies do not provide credit ratings for all firms.

## 2.2. PreÕious research

Due to the fact that bond rating provides a suitable test case for the simulation of expert judgments as well as the practical needs of independent evaluations as described in the section above, studies examining bond rating model development have a long history. Bond rating studies have traditionally used statistical techniques such as ordinal least squares Ž . OLS 9 , multiple discriminant analysis MDA <sup>w</sup> <sup>x</sup> Ž . <sup>w</sup> <sup>x</sup> <sup>w x</sup> 21 , and logit 7 models. Among the statistical techniques, the most common means for classifying bonds into their rating categories is MDA, which yields a liner discriminant function relating a set of independent variables to a dependent variable. In using statistical technique, however, the violation of multivariate normality assumptions for independent variables frequently occurs with financial data 5 .<sup>w</sup> <sup>x</sup>

Recently, however, a number of studies have demonstrated that AI approaches such as inductive learning and artificial neural networks can be used as alternative methodologies for bond rating applications. While traditional statistical methods assume certain data distributions and focus on optimizing the likelihood of correct classification 15 , inductive <sup>w</sup> <sup>x</sup> learning is a technology that automatically extracts knowledge from training samples, in which induction algorithms such as ID3 22 and CART Classifica-<sup>w</sup> <sup>x</sup> Ž tion and Regression Trees generate a tree-type struc- . ture to organize cases in memory. Thus, the difference between a statistical approach and an inductive learning approach is that different assumptions and algorithms are used to generate knowledge structures. For example, Shaw and Gentry 25 applied<sup>w</sup> <sup>x</sup> inductive learning methods to risk classification applications and found that inductive learning’s classification performance was better than probit or logit analysis. They have concluded that this result can be attributed to the fact that inductive learning is free from parametric and structural assumptions that underlie statistical methods.

Artificial neural networks are computing devices that have been used for modeling a wide variety of classification, clustering and pattern-recognition problems 13,18,24 . While basically an information processing technology, neural networks fundamentally differ from parametric statistical models. Parametric statistical models require the developer to specify the nature of the functional relationship such as linear or logistic between the dependent and independent variables. Once an assumption is made about the functional form, optimization techniques are used to determine a set of parameters that minimizes the measure of error. In contrast, neural networks with at least one hidden layer use data to develop an internal representation of the relationship between variables so that a priori assumptions about underlying parameter distributions are not required. As a consequence, better results might be expected with neural networks when the relationship between the variables does not fit the assumed model 24 . Dutta and<sup>w</sup> <sup>x</sup> Shekhar 6 were the first to investigate the ability of<sup>w</sup> <sup>x</sup> neural networks to bond rating. They obtained a very high accuracy of 83.3% in discerning AA from non-AA rated bonds. However, only one category of bonds was distinguished, and the study was not clearly comparable with earlier research which had predicted a wide range of rating categories. They used both 6 and 10 financial variables that are used in prior bond rating studies. Since only 30 patterns are used for training neural networks, it is hard to conclude based on their study that the developed models can be generalized.

Singleton and Surkan 28 also investigated the<sup>w</sup> <sup>x</sup> bond rating abilities of neural networks and linear models. They used multiple discriminant analysis, and found that neural networks outperformed the linear model for bond rating application. Another study by Singleton and Surkan 29 demonstrated <sup>w</sup> <sup>x</sup> that neural networks could predict better the direction of a bond rating than could discriminant analysis.

Kim et al. 10 compared neural networks model<sup>w</sup> <sup>x</sup> with regression, ID3, discriminant analysis and logistic analysis for bond rating with six categories of ratings. The results showed that the neural network model was the best among the above techniques in terms of classification accuracy.

Another study in bond rating prediction using neural networks was conducted by Moody and Utans <sup>w</sup> <sup>x</sup> 18 . They obtained 63.8% and 85.2% rates of accuracy when five and three classes were considered, respectively.

The recent study of bond rating done by Maher and Sen 16 compared the performance of neural <sup>w</sup> <sup>x</sup> networks with that of logistic regression. The results indicate that neural networks model performed better than a traditional logistic regression model. The best performance of the model was 70% 42 out of 60Ž samples ..

Kwon et al. 13 developed a corporate bond <sup>w</sup> <sup>x</sup> rating model using Korean bond rating data. They used ordinal pair-wise partitioning OPP approachesŽ . to back-propagation neural networks training for corporate bond rating prediction. The main idea of the OPP approach is to partition the data set in an ordinal and pair-wise manner into the output classes. Experimental results show that the OPP approach has the highest level of accuracy 71–73% , fol-Ž . lowed by conventional neural networks 66–67%Ž . and multiple discriminant analysis 58–61% . Ž .

Although numerous experimental studies reported the usefulness of neural networks in classification studies, there is a major drawback in building and using a model in which the user cannot readily comprehend the final rules that neural network models acquire. CBR, in contrast, utilizes the most natural form of knowledge; a memory of stored cases recording specific prior episode. The basic principle underlying CBR is that human experts use analogical reasoning to solve complex problems and to learn from problem-solving experiences. Shin and Han <sup>w</sup> <sup>x</sup> 26 proposed a case-based approach to predict bond rating of firms. They used nearest-neighbor matching algorithms to retrieve similar past cases. To find an optimal or near optimal importance weight vector for the attributes of cases in case retrieving, they utilized a machine learning approach, genetic algorithms. Experimental results show that the model has a higher prediction accuracy rate 75.5% than theŽ . individual methods of MDA, ID3, and CBR models with equal importance weights.

Buta 3 also developed a CBR model that pre-<sup>w</sup> <sup>x</sup> dicts corporate bond rating using financial data and ratings information of 1000 companies from 1991 to 1992 in the S&P’s Compustat database. Although performance of the system varied considerably based on the specific rating class of the company, the system matched the S&P recommended ratings for unseen cases 100 cases 90.4% of the time.Ž .

Shin et al. 27 developed a corporate bond rating<sup>w</sup> <sup>x</sup> model using Korean bond rating data. They applied case-based reasoning using an inductive indexing method without controlling the depth of the trees. The total sample used was 2651 companies whose commercial papers had been rated in 1991, 1992, 1993, 1994, and 1995, respectively. Despite the optimistic hope that inductive indexing methods could improve the effectiveness of case reasoning compared to the pure nearest-neighbor method resulting in higher classification accuracy, the experimental results were rather disappointing. Although the proposed model failed in respect to classification accuracy, the exercise has provided some valuable insights. Specifically, the success of the case-based reasoning system using an inductive indexing approach largely depends on the appropriateness of induction trees, underlining the necessity of optimizing trees.

## 3. Case-based reasoning approach

Case-based reasoning is a problem solving technique in which past cases and experiences are re-used to find a solution to particular problems. The central tasks involved in CBR methods are to identify the current problem situation, find a past case similar to the new one, use that case to suggest a solution to the current problem, evaluate the proposed solution and update the system by learning from this experience 12,23,30 . Fig. 1 illustrates the processes in-<sup>w</sup> <sup>x</sup> volved in CBR represented by a schematic cycle.

## 3.1. Case representation

A case is a contextualized piece of knowledge representing an experience. It contains a past lesson that is the content of the case and a context in which the lesson can be used. Typically a case comprises of: 1 the problem that describes the state of theŽ . world when the case occurred, 2 the solution whichŽ . states the derived solution to that problem and 3Ž . the outcome which describes the state of the world after the case occurred 11 .<sup>w</sup> <sup>x</sup>

Cases can be represented in a variety of forms using the full range of AI representational formalisms, including frames, objects, predicates, semantic nets and rules 12,23 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/5ZWE7ZSR/fulltext/images/eab73bc65b81180a670a58bd969f304cdd9a2afc6bc544b40b2bf4dda1b11754.jpg)  
Fig. 1. Overview of the case-based reasoning process 23 . <sup>w</sup> <sup>x</sup>

## 3.2. Case indexing and retrieÕing

Case indexing involves assigning indexes to cases to facilitate their retrieval. The Indexes organize and label cases so that appropriate cases can be found when needed. In building case-based reasoning systems, the CBR community proposes several guidelines for choosing indexes for particular cases: 1Ž . indexes should be predictive, 2 indexes should beŽ . abstract enough to make a case useful in a variety of future situations, 3 indexes should be concreteŽ . enough to be recognizable in future cases, and 4Ž . prediction should be useful 11,12 . Both manual and<sup>w</sup> <sup>x</sup> automated methods have been used to select indexes. Choosing indexes manually involves deciding the purpose of the case with respect to the aims of the reasoner and deciding under what circumstances the case may be useful.

The second issue of indexing cases is how to structure the indexes so that the search through case library can be done efficiently and accurately. Given a description of a problem, a retrieval algorithm which uses the indexes in a case-memory should retrieve the most similar cases to the current problem or situation. The retrieval algorithm relies on the organization of the memory to direct the search to potentially useful cases.

The indexes can either index case features independently for strictly associative retrieval or arrange cases from the most general to the most specific for hierarchical retrieval. There are three approaches to case indexing: nearest-neighbor, inductive, and knowledge-guided 1,2,26 . The nearest-neighbor ap- <sup>w</sup> <sup>x</sup> proach lets the user retrieve cases based on a weighted sum of features in the input cases that match the cases in memory. Every feature in the input cases is matched to its corresponding feature in the stored or old cases and the degree of match of each pair is computed. One of the most obvious measures of similarity between two cases is the distance. A matching function of the nearest-neighbor method is as follows:

$$
\mathrm{DIS} _ {\mathrm{ab}} = \sqrt {\sum_ {i = 1} ^ {n} w _ {i} \times \left(f _ {\mathrm{a} i} - f _ {\mathrm{b} i}\right) ^ {2}}
$$

where DIS is the matching function using Euclidean distance between cases, n is the number of features, and $w _ { i }$ is the importance weighting of a feature i. Basic steps of nearest-neighbor retrieval algorithms are quite simple and straightforward. Every feature in the input case is matched to its corresponding feature in the stored case, and the degree of match of each pair is computed using the matching function. Based on the importance assigned to each dimension, an aggregate match score is then computed. Ranking procedures order cases according to their scores where higher scoring cases are used before lower scoring ones.

Inductive indexing methods generally look for similarities over a series of instances and then form categories based on those similarities. Induction algorithms, such as ID3 and CART, determine which features best discriminate cases, and generate a treetype structure to organize the cases in memory. An induction tree is then built upon a database of training cases. This approach is useful when a single case feature is required as a solution and where that case feature is dependent upon others.

Knowledge-guided indexing applies existing domain and experimental knowledge to locate relevant cases. Although this method is conceptually superior to the other two, knowledge-guided indexing is difficult to carry out since such knowledge often cannot be successfully and exhaustively captured and represented. Therefore, many systems use knowledgeguided indexing in conjunction with other indexing techniques 1 .<sup>w</sup> <sup>x</sup>

## 3.3. Adaptation

Adaptation is the process of adjusting the retrieved cases to fit the current case. Once a matching case is retrieved, a CBR system should adapt the solution stored in the retrieved case to the needs of the current case. Adaptation looks for prominent differences between the retrieved case and the current case and then applies formulae or rules that take those differences into account when suggesting a solution.

In general, there are two kinds of adaptation in CBR: 1 substitution method and 2 transformationŽ . Ž . methods. The substitution method substitutes values appropriate for the new situation for values in the old solution. The transformation methods are used to transform an old solution into one that will work in a new situation 12 .<sup>w</sup> <sup>x</sup>

## 4. Inductive learning technique for case indexing

The quality of knowledge-based system involves how well relevant parts of the application domain are captured by the knowledge base. To be able to meet the requirements of the knowledge-based system with respect to robust competence, particularly in open and weak theory domains such as the corporate bond rating, a stronger emphasis should be placed on the combined utilization of general domain knowledge and case-specific knowledge. The inductive learning methods provide a general knowledge for the application domain, relying on making associations along a generalized relationship between problem descriptors and conclusions. In contrast, CBR, more specifically, nearest-neighbor retrieving method, utilizes different types of knowledge by capturing concrete and specific knowledge related to problem solving experience.

The reason why we use an inductive technique for case indexing is to build a knowledge-based system that can combine these two types of knowledge. The underlying rationale is this: if you can cluster cases that are similar to one another and figure out which cluster best matches the new situation according to a general domain knowledge, then only cases in that cluster need be considered in finding a best matching case. Several inductive learning methods can be used to extract general domain knowledge. Induction algorithms such as ID3 and CART determine which features do the best job in discriminating cases and generate a tree-type structure to organize the cases.

The combination itself, however, is not enough to ensure robustness of the systems. Another point we should consider is an optimal combination level between the two knowledge types. How much should be generalized and how much specific knowledge should be utilized are important issues that need to be considered for competent knowledge-based systems.

The inductive indexing method that this study applies is as follows. As a first step, we build a decision tree for case indexing. As we mentioned in the above section, the success of inductive indexing approach depends largely on the appropriateness of decision trees for case retrieval 12,27 . To find an<sup>w</sup> <sup>x</sup> optimal or near optimal decision tree, we apply four different stopping conditions for the tree. The stopping criterion denotes the maximal depth of the tree, defining the maximal number of levels an induction tree can have. Fig. 2 illustrates the levels of depth of the decision tree.

This decision tree is built using induction techniques on a database of previous cases. When the new case arrives, our method works as follows: First, we apply the decision tree to some depth to retrieveŽ . a class of cases that are similar to the new one. On this subset of cases, we perform nearest neighbor retrieval to find the single best match.

The first model applies an induction tree having three levels of depth and case-based reasoning by applying the nearest-neighbor algorithm at the end of the decision tree. This allows the examiner to determine the most similar cases to the current situation, and to choose the most probable value in this subset of cases. The second, third and fourth models follow the same procedure except that the decision trees have five, seven and nine levels of depth, respectively. In building decision trees, we use the software package KATE. It consists of KATE-Induction and KATE-CBR modules, providing the capabilities of generating decision trees using inductive learning algorithms and nearest-neighbor retrieving algorithm, respectively. Fig. 3 illustrates the hybrid structure of IND Induction NN Nearest-neighbor models.Ž . Ž . <sub>–</sub>

![](/api/attachments/5ZWE7ZSR/fulltext/images/2ed3a1403e7debf5567d83d3a6c5df86c7f8ea99160f55ee2de927bda8c36353.jpg)  
Fig. 2. Depths of the decision tree.

![](/api/attachments/5ZWE7ZSR/fulltext/images/cd096ea63d3d28e81b02ab270d098a642896f8a19b508a3d565cca804231ee33.jpg)  
Fig. 3. The structure of IND-NN models.

## 5. Experimental designs and data

The sample data consists of financial ratios derived from a financial statement and the correspond ing bond ratings of Korean companies. The ratings have been performed by the National Information and Credit Evaluation, one of the most prominent bond rating agencies in Korea. The total sample available includes 3886 companies whose commercial papers have been rated from 1991 to 1995. Credit grades are defined as outputs and classified as five grade groups A1, A2, A3, B, C according toŽ . credit levels. Table 1 shows the organization of the data set.

We apply two stages of the input variable selection process. At the first stage, we select 27 variables Ž . 23 quantitative<sup>r</sup>4 qualitative using factor analysis, one-way ANOVA between input variable and credit Ž grade as output variable and Kruskal–Wallis test.

Table 1  
Number of companies in each rating

<table><tr><td>Ratings</td><td>Number of cases</td><td>%</td></tr><tr><td>A1</td><td>260</td><td>6.7</td></tr><tr><td>A2</td><td>833</td><td>21.4</td></tr><tr><td>A3</td><td>1314</td><td>33.8</td></tr><tr><td>B</td><td>1406</td><td>36.2</td></tr><tr><td>C</td><td>73</td><td>1.9</td></tr><tr><td>Sum</td><td>3886</td><td>100.0</td></tr></table>

Ž . for qualitative variables . In the second stage, we select 12 financial variables 10 quantitativeŽ <sup>r</sup>2 qualitative using stepwise method of MDA to reduce the. dimensionality. We select input variables satisfying the univariate test first, and then select significant variables by stepwise method for refinement. In choosing qualitative variables, four variables are initially selected. However, audit opinion and audit firm are excluded by the expert’s opinion. Two of the four qualitative variables selected are firm classification by group conglomerate types and firmŽ . types. We classify conglomerates into five categories, namely, top-10 conglomerates, top-20 conglomerates, top-30 conglomerates, top-40 conglomerates and non-conglomerates. The four types of firms are: listed, registered, externally audited and others. Table 2 illustrates the selected variables for this study.

Table 2  
Definition of variables

<table><tr><td>Variables</td><td>Definitions</td></tr><tr><td>X1</td><td>Firm classification by conglomerate types</td></tr><tr><td>X2</td><td>Firm types</td></tr><tr><td>X3</td><td>Total assets</td></tr><tr><td>X4</td><td>Stockholders&#x27; equity</td></tr><tr><td>X5</td><td>Sales</td></tr><tr><td>X6</td><td>Year after founded</td></tr><tr><td>X7</td><td>Gross profit to sales</td></tr><tr><td>X8</td><td>Net cash flow to total assets</td></tr><tr><td>X9</td><td>Financial expenses to sales</td></tr><tr><td>X10</td><td>Total liability to total asset</td></tr><tr><td>X11</td><td>Depreciation to total expenses</td></tr><tr><td>X12</td><td>Working capital turnover</td></tr></table>

Table 3  
Importance weights assigned by experts

<table><tr><td>Variables</td><td>Average assigned value</td></tr><tr><td>X1</td><td>0.72</td></tr><tr><td>X2</td><td>0.40</td></tr><tr><td>X3</td><td>0.80</td></tr><tr><td>X4</td><td>0.88</td></tr><tr><td>X5</td><td>0.80</td></tr><tr><td>X6</td><td>0.72</td></tr><tr><td>X7</td><td>0.68</td></tr><tr><td>X8</td><td>0.72</td></tr><tr><td>X9</td><td>0.76</td></tr><tr><td>X10</td><td>0.80</td></tr><tr><td>X11</td><td>0.48</td></tr><tr><td>X12</td><td>0.68</td></tr></table>

Each data set is split into two subsets, a reference set and a validation holdout set. The reference dataŽ . are used to form a decision tree to index cases and also as a case base for retrieval. The validation data are used to test the model’s results with the data which have not been used to develop the system. The number of the reference cases and the validation cases are 3486 and 400, respectively.

## 6. Results and analysis

To study the effectiveness of the integrated approach for case indexing in the context of the corporate bond rating problem, the results obtained are compared with those of other indexing techniques such as Nearest-neighbor model and Nearest-neighbor Expert model. The Nearest-neighbor model uses<sub>–</sub> a nearest-neighbor matching algorithm that has equal weights among attributes. The Nearest-neighbor Ex-<sub>–</sub> pert model applies importance weights assigned by experts.

For this experiment, we had five experts designate the importance of an attribute by assigning the five qualitative values through interviewing. We selected three experts from the bond rating department of a credit rating agency and two from the credit analysis department of a commercial bank. The selected experts’ work experience related to credit analysis ranged from 2 to 8.5 years while the average of experience is 4 years and 2 months. The five qualitative values are: Amost important,B Avery important,B Aimportant,B Aless important,B and AignoredB which are associated with the numbers 1.0, 0.8, 0.6, 0.4, and 0.2, respectively, for computation. Table 3 shows the assigned importance to each attribute via expert opinion. Importance values range from 0.4 to 0.88.

As mentioned above, we apply four predetermined stopping conditions. IND NN model 1 ap-Ž . <sub>–</sub> plies the decision tree which has three levels of depth. IND NN model 2 , 3 and 4 follow theŽ . Ž . Ž . <sub>–</sub> same procedure except the decision trees have five, seven and nine levels of depth, respectively. Table 5 represents different stopping conditions and the corresponding figures of the decision tree.

As shown in Table 4, the important figures of the decision tree are dramatically affected by different stopping conditions. For example, the number of leaves increases from 8 to 746 depending on the depth of the tree. Since the number of leaves corresponds to the number of inductive clusters for case organization, 8 and 746 leaves denote 8 and 746 clusters for cases, respectively. Since the main role of induction in this context is to extract general domain knowledge from the database, we can easily expect that a higher number of clusters does not ensure an effective case-based model.

Table 4  
Figures depend on different stopping conditions

<table><tr><td>Model</td><td>Stopping condition (depth)</td><td>Number of nodes</td><td>Number of leaves</td><td>Number of cases per leaf</td><td>Average number of questions</td><td>Average depth</td></tr><tr><td>IND-NN (1)</td><td>3</td><td>15</td><td>8</td><td>435.8</td><td>2</td><td>3</td></tr><tr><td>IND-NN (2)</td><td>5</td><td>63</td><td>32</td><td>108.9</td><td>3.4</td><td>5</td></tr><tr><td>IND-NN (3)</td><td>7</td><td>229</td><td>115</td><td>30.3</td><td>4.7</td><td>6.9</td></tr><tr><td>IND-NN (4)</td><td>9</td><td>511</td><td>256</td><td>13.6</td><td>5.5</td><td>8.4</td></tr><tr><td>Full (no condition)</td><td></td><td>1491</td><td>746</td><td>4.7</td><td>6.9</td><td>11.8</td></tr></table>

Table 5  
Classification accuracies %Ž .

<table><tr><td colspan="2">Methods</td><td> $A1^a$ </td><td>A2</td><td>A3</td><td>B</td><td>C</td><td> $Avg.^b$ </td></tr><tr><td>MDA</td><td></td><td>57.7</td><td>69.8</td><td>58.3</td><td>55.0</td><td>77.8</td><td>60.0</td></tr><tr><td> $Inductive\ learning^c$ </td><td></td><td>65.4</td><td>55.8</td><td>47.5</td><td>72.9</td><td>33.3</td><td>59.0</td></tr><tr><td rowspan="6">CBR</td><td> $NN^d$ </td><td>65.4</td><td>66.3</td><td>58.3</td><td>66.4</td><td>0.0</td><td>62.0</td></tr><tr><td> $NN\_Expert^e$ </td><td>69.2</td><td>65.1</td><td>58.3</td><td>63.6</td><td>0.0</td><td>61.0</td></tr><tr><td> $IND-NN (1)^f$ </td><td>84.6</td><td>74.4</td><td>64.7</td><td>70.7</td><td>22.2</td><td>69.3</td></tr><tr><td>IND-NN (2)</td><td>80.8</td><td>72.1</td><td>66.9</td><td>72.9</td><td>22.2</td><td>70.0</td></tr><tr><td>IND-NN (3)</td><td>76.9</td><td>62.8</td><td>63.3</td><td>73.6</td><td>11.1</td><td>66.5</td></tr><tr><td>IND-NN (4)</td><td>61.5</td><td>61.6</td><td>58.3</td><td>71.4</td><td>11.1</td><td>62.8</td></tr></table>

<sup>a</sup> Bond ratings.  
<sup>b</sup>The weighted average value considering the number of cases in each rating.  
<sup>c</sup> Derived by packaged software KATE-Induction.  
<sup>d</sup> Nearest-neighbor matching algorithm that has equal weights among attributes.  
<sup>e</sup>Nearest-neighbor matching algorithm that applied weights assigned by experts.  
<sup>f</sup> IND-NN 1 applies the decision tree which has three levels of depth. IND-NN 2 , 3 and 4 follow the same procedure except the Ž . Ž . Ž . Ž . decision trees have five, seven and nine levels of depth, respectively

Table 5 represents a comparison of the results of the classification techniques applied for this study. Each cell contains the accuracy of the various classification techniques by classes. The results of MDA and the inductive learning model using KATE-Induction are also presented as benchmarks to verify the applicability of the proposed model to the domain. MDA is a representative of statistical classification methods, and the linear discriminant function is as follows;

$$
Z = W _ {1} X _ {1} + W _ {2} X _ {2} + \ldots + W _ {n} X _ {n}
$$

where Z is a discriminant score, $W _ { i }$ is a discriminant weight for variable $i , \ X _ { i }$ is an independent variable i. The interpretation of MDA involves examining the discriminant functions to determine the relative importance of each independent variable in discriminating between the groups.

![](/api/attachments/5ZWE7ZSR/fulltext/images/73d252f159c5aa58d0b191578bef2ff4708dfa958952f263055750f282183f6c.jpg)  
Fig. 4. Classification accuracies by integrated models % . Ž .

Table 6  
A 2-by-2 contingency table

<table><tr><td>Benchmark model</td><td>Proposed model</td><td>Count</td></tr><tr><td># of correct classification</td><td># of correct classification</td><td>corresponding frequency</td></tr><tr><td># of correct classification</td><td># of incorrect classification</td><td>corresponding frequency</td></tr><tr><td># of incorrect classification</td><td># of correct classification</td><td>corresponding frequency</td></tr><tr><td># of incorrect classification</td><td># of incorrect classification</td><td>corresponding frequency</td></tr></table>

Among the techniques, the IND NN models have<sub>–</sub> the highest level of accuracies IND NN 2 : 70.0%,Ž Ž . <sub>–</sub> IND NN 1 : 69.3%, IND NN 3 : 66.5% in theŽ . Ž . . <sub>– –</sub> given data sets, followed by Nearest-neighbor model Ž . 62.0% . MDA and induction have similar levels of classification accuracy. As we expected, the classification accuracies are affected by the depth of the decision tree. Fig. 4 shows that corresponding accu racies depend on the depth of the trees.

A comparison of IND NN models indicates that<sub>–</sub> higher levels of depth in induction does not necessarily guarantee higher performance for integration. The accuracies of IND NN model 3 and 4 decreaseŽ . Ž . <sub>–</sub> as the depth of the decision tree increases. This result underlines the necessity of optimizing decision trees applied in a case-based retrieval and not simply leaving it to the induction technique itself.

We use the McNemar tests to examine whether the predictive performance of inductive indexing approach is significantly higher than that of other techniques. The McNemar test is a nonparametric test of the hypothesis that two related dichotomous variables have the same means, i.e. used to test the null hypothesis that the population median of the paired differences is 0 with counted data arranged in a AcontingencyB table format. Since we are interested in defining the fact that the proposed approach outperforms the existing one, we can make a 2-by-2 contingency table as shown in Table 6.

Table 7 shows the results of McNemar tests to compare the classification ability between benchmark models and an IND NN model 2 using a Ž . <sub>–</sub> decision tree which has five levels of depth for holdout samples.

The result shows the IND NN model 2 per-Ž . forms significantly better than every benchmark model proposed for this study at 1% significance level. Based on the results, we conclude that the inductive indexing approach employing an optimal level of general domain knowledge is effective, enhancing the overall classification accuracy of the case-based system for the application domain.

Table 7  
McNemar values for the pairwise comparison of performance between models

<table><tr><td></td><td>MDA</td><td>Inductive learning</td><td> $NN^a$ </td><td> $NN\_Expert^b$ </td><td>IND-NN (2)</td></tr><tr><td>MDA</td><td>-</td><td> $0.0500^c$ </td><td>0.2988</td><td>0.0529</td><td>9.7500***</td></tr><tr><td>Inductive learning</td><td>-</td><td>-</td><td>0.7857</td><td>0.3182</td><td>12.6644***</td></tr><tr><td>NN</td><td>-</td><td>-</td><td>-</td><td>0.1000</td><td>8.3904***</td></tr><tr><td>NN_Expert</td><td>-</td><td>-</td><td>-</td><td>-</td><td>8.1441***</td></tr></table>

<sup>a</sup> Nearest-neighbor matching algorithm that has equal weights among attributes.  
<sup>b</sup>Nearest-neighbor matching algorithm that applied weights assigned by experts.  
<sup>c</sup>Chi-square values.  
<sup>) ) )</sup> significant at 1%.

## 7. Concluding remarks

This paper examined the effectiveness of inductive learning approach to case indexing process for business classification tasks. In this approach, the induction technique is used to extract general domain knowledge for efficient and effective retrieval. Our experimental results have shown that this approach support an effective retrieval of cases and increases overall classification accuracy significantly.

Findings of this study are twofold. First, in building a knowledge-based system, the combination of two types of knowledge, the general domain knowledge and case-specific knowledge, is very important to ensure robust competence. While the inductive learning methods provide a general knowledge for the application domain, relying on making associations along a generalized relationship between problem descriptors and conclusions, CBR more specifi- Ž cally nearest neighbor utilizes different types of. knowledge by capturing concrete and specific knowledge related to problem solving experience. Second, there should be an optimal combination level between the two knowledge types. The combination itself is not enough. Rather, issues involving how much should be generalized and how much specific knowledge should be utilized are more important for competent knowledge-based systems, especially in weak theory and complex domains such as bond rating.

This study has several limitations that require further attention. First, the determination of decision trees using different stopping conditions has a critical impact on the performance of the system. However, we have not suggested theoretically sound procedures to determine the optimal stopping conditions, including the depth and the criterion itself. We intend to find a general method to determine the stopping conditions in future research. This issue has more to do with the appropriate stopping criteria that represent the level of generalization than it does the depth of trees.

The second issue for future research involves the use of more accountable target variables. The target variables used for the study are ratings by credit analysts of bond rating agency. This means that if those historical ratings that human raters evaluated do not correspond to the correct credit level of the company, the system also cannot provide correct credit information to the users. To overcome this limitation, the use of more accountable target variables that accurately represent the credit level of the company should be considered in future research.

The final issue for future work concerns the extensive use of knowledge-guided indexing. Although we used inductive learning method to extract general domain knowledge in retrieving cases for this study, we are able to utilize different knowledge types such as deductive rules which directly codify domain heuristics and knowledge. We believe that integrating the rules with case-based mechanisms in a hybrid fashion may lead to achieve more accurate and powerful case indexing and retrieval.

The aim of integrating different techniques is to make more powerful and efficient systems by taking advantage of the strength of each technique. Therefore, developing more effective methods using synergistic integration is a continuing research issue to be addressed in future research.

## Acknowledgements

We thank the editor and the anonymous reviewers for their useful comments and suggestions. This research was supported by the Brain Korea 21 Grant.

## References

<sup>w</sup> <sup>x</sup> 1 C.E. Brown, U.G. Gupta, Applying case-based reasoning to the accounting domain. Intelligent Systems in Accounting, Finance and Management 3 1994 205–221.Ž .

<sup>w</sup> <sup>x</sup> 2 S.M. Bryant, A case-based reasoning approach to bankruptcy prediction modeling. Intelligent Systems in Accounting, Finance and Management 6 1997 195–214.Ž .

<sup>w</sup> <sup>x</sup> 3 P. Buta, Mining for financial knowledge with CBR. AI Expert 9 2 1994 34–41.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 R.T. Chi, M. Chen, M.Y. Kiang, Generalized case-based reasoning system for portfolio management. Expert Systems with Applications 6 1 1993 67–76.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 E.B. Deakin, Discriminant analysis of predictors of business failure. Journal of Accounting Research 1976 167–179Ž . Ž . Spring .

<sup>w</sup> <sup>x</sup> 6 S. Dutta, S. Shekhar, Bond rating: a non-conservative application of neural networks. Proceedings of IEEE International Conference on Neural Networks 2, San Diego, CA, 1988, pp. 443–450.

<sup>w</sup> <sup>x</sup> 7 H.L. Ederington, Classification models and bond ratings. Financial Review 20 4 1985 237–262.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 J. Hansen, R.D. Meservy, L.E. Wood, Case-based reasoning:

application techniques for decision support. Intelligent Systems in Accounting, Finance and Management 4 1995 Ž . 137–146.

<sup>w</sup> <sup>x</sup> 9 J.O. Horrigan, The determination of long term credit standing with financial ratios. Journal of Accounting Research 1966Ž . 44–62, supplement.

10 J. Kim, H.R. Weistroffer, R.T. Redmond, Expert systems for bond rating: a comparative analysis of statistical, rule-based and neural network systems. Expert Systems 10 3 1993Ž . Ž . 167–172.

<sup>w</sup> <sup>x</sup> 11 J. Kolodner, Improving human decision making through case-based decision aiding. AI Magazine 12 2 1991 52–Ž . Ž . 68.

<sup>w</sup> <sup>x</sup> 12 J. Kolodner, Case-Based Reasoning. Morgan Kaufmann, San Mateo, CA, 1993.

<sup>w</sup> <sup>x</sup> 13 Y.S. Kwon, I.G. Han, K.C. Lee, Ordinal pairwise partitioning OPP approach to neural networks training in bond Ž . rating. Intelligent Systems in Accounting, Finance and Management 6 1997 23–40.Ž .

<sup>w</sup> <sup>x</sup> 14 Y.F.D Law, S.B. Foong, S.E.J. Kwan, An integrated casebased reasoning approach for intelligent help desk fault management. Expert Systems with Applications 13 4 1997Ž . Ž . 265–274.

<sup>w</sup> <sup>x</sup> 15 T.P. Liang, J.S. Chandler, I. Han, Integrating statistical and inductive learning methods for knowledge acquisition. Expert Systems with Applications 1 1990 391–401.Ž .

<sup>w</sup> <sup>x</sup> 16 J.J. Maher, T.K. Sen, Predicting bond ratings using neural networks: a comparison with logistic regression. Intelligent Systems in Accounting, Finance and Management 6 1997Ž . 59–72.

<sup>w</sup> <sup>x</sup> 17 A.I. Mechitov, H.M. Moshkovich, D.L. Olson, B. Killingsworth, Knowledge acquisition tool for case-based reasoning system. Expert Systems with Applications 9 2Ž . Ž . 1995 201–212.

<sup>w</sup> <sup>x</sup> 18 J. Moody, J. Utans, Architecture selection strategies for neural networks application to corporate bond rating. in: A. Refenes Ed. , Neural Networks in the Capital Markets.Ž . Wiley, Chichester, 1995, pp. 277–300.

<sup>w</sup> <sup>x</sup> 19 B.W. Morris, SCAN: a case-based reasoning model for generating information system control recommendations. Intelligent Systems in Accounting, Finance and Management 3 Ž . 1994 47–63.

<sup>w</sup> <sup>x</sup> 20 B. O’Roarty, D. Patterson, S. McGreal, A. Adair, A casebased reasoning approach to the selection of comparable evidence of retail rent determination. Expert Systems with Applications 12 4 1997 417–428.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 G.E. Pinches, K.A. Mingo, A multivariate analysis of industrial bond ratings. Journal of Finance 28 1 1973 1–18.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 J.R. Quinlan, Induction of decision trees. Machine Learning 1 1986 81–106.Ž .

<sup>w</sup> <sup>x</sup> 23 C.K. Riesbeck, R.C. Schank, Inside Case-Based Reasoning. Lawrence Erlbaum Associates, Hillsdale, NJ, 1989.

<sup>w</sup> <sup>x</sup> 24 L.M. Salchenberger, E.M. Cinar, N.A. Lash, Neural networks: a new tool for predicting thrift failures. in: R. Trippi, E. Turban Eds. , Neural Networks in Finance and Investing. Ž . Probus Publishing, 1992.

<sup>w</sup> <sup>x</sup> 25 M. Shaw, J. Gentry, Inductive learning for risk classification. IEEE Expert 1990 47–53, February. Ž .

<sup>w</sup> <sup>x</sup> 26 K.S. Shin, I. Han, Case-based reasoning supported by genetic algorithms for corporate bond rating. Expert Systems with Applications 16 2 1999 85–95.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 K.S. Shin, T.S. Shin, I. Han, Using induction technique to support case-based reasoning: a case of corporate bond rating. Proceedings of MS<sup>r</sup>OR Society Conference, Seoul, Korea. 1997, pp. 199–202.

<sup>w</sup> <sup>x</sup> 28 J.C. Singleton, A.J. Surkan, Neural networks for bond rating improved by multiple hidden layers. Proceedings of the IEEE International Conference on Neural Networks 2, 1990, pp. 163–168.

<sup>w</sup> <sup>x</sup> 29 J.C. Singleton, A.J. Surkan, Bond rating with neural networks. in: A. Refenes Ed. , Neural Networks in the CapitalŽ . Markets. London Business School, England, 1995.

<sup>w</sup> <sup>x</sup> 30 S. Slade, Case-based reasoning: a research paradigm. AI Magazine 12 1 1991 42–55.Ž . Ž .

![](/api/attachments/5ZWE7ZSR/fulltext/images/464da189afe73f1d9c97e9f6555dfa8a3d51ee7d75155cd4d8e913057a5e3b72.jpg)

Kyung-shik Shin is an Assistant Professor of Management Information Systems, College of Business Administration, at the Ewha Womans University in Korea. He received his MBA from the George Washington University and Ph.D. from the Korea Advanced Institute of Science and Technology in 1998. His research interests include decision support systems, intelligent systems, data mining, artificial intelligence applications for business and electronic commerce.

![](/api/attachments/5ZWE7ZSR/fulltext/images/461b4a504981eea8af339a565e4a20cb1b3d81ede0659fc492596a16f551e8d3.jpg)

Ingoo Han is an Associate Professor at the KAIST Graduate School of Management. He received the PhD from University of Illinois at Urbana-Champaign. His research interests are information audit<sup>r</sup>security and artificial intelligence applications in accounting and finance. He published in the Decision Support Systems, Information & Management, Expert Systems with Applications, International Journal of Intelligent Systems in Accounting Finance & Management,

International Journal of EC, Telecommunication Systems, Engineering Economy, Contemporary Accounting Research, etc.
