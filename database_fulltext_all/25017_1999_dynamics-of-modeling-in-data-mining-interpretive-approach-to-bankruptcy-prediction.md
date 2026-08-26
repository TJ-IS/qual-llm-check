---
otero_id: 25017
otero_key: "9VQSWTF3"
title: "Dynamics of Modeling in Data Mining: Interpretive Approach to Bankruptcy Prediction"
authors: "Tae Kyung Sung; Namsik Chang; Gunhee Lee"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518234"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamics of Modeling in Data Mining: Interpretive Approach to Bankruptcy Prediction

Tae Kyung Sung, Namsik Chang & Gunhee Lee

To cite this article: Tae Kyung Sung, Namsik Chang & Gunhee Lee (1999) Dynamics of Modeling in Data Mining: Interpretive Approach to Bankruptcy Prediction, Journal of Management Information Systems, 16:1, 63-85, DOI: 10.1080/07421222.1999.11518234

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518234

![](/api/attachments/9VQSWTF3/fulltext/images/801d32468b7f3207ce1637450345bdccf9ed1ba925c534f8a4e0aef1468c376b.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/9VQSWTF3/fulltext/images/67242c0ce0a6b4ee38d4b1a081b6d84243de7e2126b39ae8d165eaaa038a89af.jpg)

Submit your article to this journal ↗

![](/api/attachments/9VQSWTF3/fulltext/images/332a5866c2775ab19bd2c641f60d13d9da4de992aaf16581c5cea7a932bfe4d4.jpg)

Article views: 3

![](/api/attachments/9VQSWTF3/fulltext/images/0faf2a1de277f6f50362002033f9521360a224ff59efbab9e382d266641f6e77.jpg)

View related articles ↗

![](/api/attachments/9VQSWTF3/fulltext/images/2aed50f038812eebe930a7917cceccec87f51a1ea53f64713f8a2b6d1e781e6b.jpg)

Citing articles: 4 View citing articles ↗

# Dynamics of Modeling in Data Mining: Interpretive Approach to Bankruptcy Prediction

TAE KYUNG SUNG, NAMSIK CHANG, AND GUNHEE LEE

TAE KYUNG SUNG is an Associate Professor of MIS at Kyonggi University, Korea. He received his Ph.D. in MIS from the University of Texas at Austin and a B.B.A. from Sungkyunkwan University. Dr. Sung's papers have been published in Technological Forecasting and Social Changes, Journal of MIS Research, Journal of Industrial Studies, Journal of Management Education and Research, Korean Management Science Review, Korean Management Review, Journal of Information Processing, International Business Review, and other journals. His research interests include information systems strategy, planning, and management, data mining and applications, business innovation, and knowledge/technology/information sharing and transfer.

NAMSIK CHANG is an Assistant Professor at the College of Economics and Business Administration at the University of Seoul. He received his Ph.D. in MIS from the University of Arizona, an M.B.A. from the University of Missouri, St. Louis, and a B.S. from Korea University, Seoul. Dr. Chang has published in Decision Support Systems, International Journal of Information and Management Sciences, and Business Information Review, among other journals. He is currently conducting research in data-mining techniques and their applications to real-world domains, and database and data warehouse modeling.

GUNHEE LEE is an Assistant Professor at the College of Business at Sogang University, Korea. He has a Ph.D. and an M.A. in statistics from the University of Missouri, Columbia, and a B.S. from Seoul National University. His publications have appeared in Environmental Toxicology and Chemistry and Journal of Korean Statistical Society. Dr. Lee's primary interests include data mining, reliability, statistical computing and modeling, Bayesian theory, and asymptotic theory.

ABSTRACT: This paper uses a data-mining approach to develop bankruptcy prediction models suitable for normal and crisis economic conditions. It observes the dynamics of model change from normal to crisis conditions and provides interpretation of bankruptcy classifications. The bankruptcy prediction model revealed that the major variables in predicting bankruptcy were “cash flow to total assets” and “productivity of capital” under normal conditions and “cash flow to liabilities,” “productivity of capital,” and “fixed assets to stockholders equity and long-term liabilities” under crisis conditions. The accuracy rates of final prediction models in normal conditions and in crisis conditions were found to be 83.3 percent and 81.0 percent, respectively. When the normal model was applied in crisis situations, prediction accuracy dropped significantly in the case of bankruptcy classification (from 66.7 percent to 36.7 percent) to the level of a blind guess (35.71 percent). Therefore, the need for a different model in crisis economic conditions is justified.

KEY WORDS AND PHRASES: bankruptcy prediction, crisis management, data mining, dynamics of modeling.

AS WE NEAR THE TWENTY-FIRST CENTURY, CORPORATE BANKRUPTCY in the world, especially in East Asia, has reached an unprecedented level. Corporate bankruptcy brings with it economic losses to management, stockholders, employees, customers, and others, together with great social and economical cost to the nation. Thus, accurate prediction of bankruptcy has become an important issue in finance. Since the seminal study of Altman [3] on bankruptcy prediction, numerous followup studies have tried to further develop appropriate models, by applying data-mining techniques including multivariate discriminant analysis, logistical regression analysis, probit analysis, genetic algorithms, neural networks, decision trees, and other statistical and computational methods. It is worth noting, however, that all of these bankruptcy models assume “normal” economic conditions.

The present economic crisis in East Asia thus raises an important issue: Can we profitably apply bankruptcy prediction models that assume “normal” economic conditions to “crisis” conditions? It may be that these painstakingly built bankruptcy prediction models become almost useless under crisis situations. In Korea, for example, a large number of corporations rated “very sound” or “healthy” by traditional corporate bankruptcy models nonetheless went spectacularly bankrupt during the International Monetary Fund (IMF) relief period. Therefore, both academicians and practitioners have begun to suspect the validity of accepted bankruptcy prediction models built under “normal” conditions and are seeking more appropriate models. The primary purpose of this paper, thus, is to develop bankruptcy varied prediction models suitable for normal and crisis economic conditions, noting the dynamics of model changes from normal to crisis conditions.

If the accuracy of a classification or prediction were all that mattered, then the predictive efficiency (and not the interpretation of results) would be the major concern. But there are certain situations where the ability to explain a prediction as well as the face validity of the model is crucial $[13]$ . In Korea, the fate of a number of firms of either “existence” or “exit” depends on the bankruptcy prediction made by financial institutions. There has been heated controversy over the validity of bankruptcy prediction, and firms are strongly demanding explanations of the logic of prediction. Firms find it more acceptable to hear, for instance, that the prediction was based on computer-generated rules (such as cash flow ratio is less than 2.64 and productivity of capital is less than 20.61) than to hear only that the decision has been made by an advanced technique that offers no explanation for its action.

Thus, the secondary purpose of this paper is to develop bankruptcy models that provide as much interpretation of causes as possible without losing noticeable predictive accuracy. To pursue this end, the decision tree technique was used to provide interpretation of both the model itself and bankruptcy prediction decisions as well as to evaluate the predictive accuracy of the models. Discriminant analysis was applied to benchmark the performance of the prediction models built by the decision tree technique, since discriminant analysis has been proved to be the most widely accepted and successful method in bankruptcy prediction literature $[3, 4, 6, 11, 67]$ . Neural networks were excluded from this study on the grounds that they cannot explain their results despite a superb performance.

## Literature Review

## Bankruptcy Prediction

THE DETECTION OF CORPORATE FAILURES IS A SUBJECT that has been particularly amenable to financial ratio analysis. According to Altman [4], the first study was done in 1935 by Smith and Winakor during the Great Depression era; then, in 1942, Merwin showed that failing firms exhibit significantly different ratios than do successful firms. Beaver [11] then applied univariate analysis of financial ratios to predict corporate bankruptcy, while others strongly recommended multivariate analysis [3, 4, 5].

The breakthrough bankruptcy prediction model, the Z-score model developed by Altman [3], came in the late 1960s. The five-variable Z-score model using multiple discriminant analysis showed very strong predictice power (above 90 percent). After Altman, a number of studies corroborated this result, and multiple discriminant analysis thereby became the dominant approach. Since most of the studies, including that of Altman [3], used relatively small firms in their samples, generalization of research results was hard to accept. Altman, Haldeman, and Narayanan [5] therefore developed the ZETA model to be applied to larger firms, not limited to specific industries. But controversial aspects of discriminant analysis with respect to failure prediction were raised by Platt [53, 54], Weiss [70], and Zavgren et al. [77], among others.

Unlike authors of other discriminant studies, Blum [15, 16] postulated a general framework for variable selection based on the concept of a business firm as a reservoir of financial resources with the probability of failure expressed in terms of expected cash flow. Deakin [24] tried to capture the best of both Beaver's [11] and Altman's [3] models by employing the fourteen ratios used by Beaver to search for the linear combination of these ratios with the greatest predictive accuracy. Using a subset of Deakin's [24] fourteen-variable set, Libby [43] designed his study to determine whether accounting ratios provided useful information to loan officers trying to predict business failures. Libby identified five independent sources of variation within the fourteen-variable set using principal component analysis. Building on Libby's [43] factor analysis contribution, Deakin [25] extended his 1972 study in order to provide an indication of the frequency and nature of misclassification of nonfailing companies and to compare auditors' opinions with the model's predictability. Edminister [28] reported that the predictive power of ratio analysis depended on both the choice of analytical method and the selection of ratios. Applying the gambler's ruin model, Wilcox [73] tried to develop a theoretical model to better explain Beaver's [11] results and to generate hypotheses leading to potentially better predictors of failure. He argued that most bankruptcy studies lacked a conceptual framework. But, ironically, the gambler's ruin model is no longer in existence [4]. Scott [62] compared several of the leading empirical models, in terms of both their observed accuracy and their theoretical coherence, according to Scott's own conceptual framework. He concluded that the ZETA model is perhaps the most convincing multidimensional model since it has high discriminating power, is reasonably parsimonious, and includes accounting and stock market data as well as earnings and debt variables.

Similar methodologies have attempted to improve upon the robust but restrictive discriminant structure. Based on the regression analysis, Ohlson's [49] logit regression framework, and Zmijewski's [78] probit analysis model attempted to quantify the likelihood of bankruptcy and to assess more directly the impact of specific variables on the distress probabilities. Other statistical methodologies in the literature include logit analysis [44], the arctangent regression approach [40], and factor-logistic analysis [71].

Most of the works described so far have used a classic classification methodology—discriminant analysis—to model corporate bankruptcy predictions $[63]$ . While discriminant analysis enables an explicit linkage between the explanatory variables and the groupings, a host of statistical problems has been cited as rendering the results somewhat problematic $[4]$ . A technique that may eliminate many of the above problems is the decision tree or recursive partitioning analysis $[55, 56, 57]$ . Decision tree analysis sets out to maximize the entropy of the split subsets, while recursive partitioning is designed to minimize the expected cost of misclassification. Frydman, Altman, and Kao $[29]$ applied recursive partitioning analysis to generate a discriminant tree to classify bankruptcy. Following this study, Messier and Hansen $[45]$ developed the decision tree model to predict corporate failures.

Beginning in the mid-1980s, neural networks became the dominant research methodology in artificial intelligence; researchers actively applied neural networks to classification problems including bankruptcy prediction. Most neural network studies in bankruptcy prediction centered on the comparison of performance (prediction accuracy) of neural networks and other methodologies such as discriminant analysis, logit analysis, genetic algorithms, decision tree, and others $[6, 26, 27, 38, 48, 61, 68, 69, 74]$ . A number of studies report that the performance of neural networks is slightly better than that of other techniques, but generally the results are contradictory or inconclusive.

Another stream of research applies genetic algorithms to the problem $[46]$ . Genetic algorithms are stochastic techniques that can search large and complicated spaces $[33]$ . Based on genetic and evolutionary principles, genetic algorithms work by repeatedly modifying a population of artificial structures through the application of initialization, selection, crossover, and mutation operators. Back, Laitinen and Sere $[9]$ applied genetic algorithms to predict bankruptcy and compared the findings with those of neural networks. The results were promising. Hybrid studies combining neural networks and genetic algorithms are beginning to emerge [33].

Kim, Chung, and Paradice [37] added a new dimension to expert decision making by introducing the interaction between task domain and models. They extended previous research by analyzing individual experts' decision strategies in loan evaluation, comparing the performance of four popular inductive modeling methods, and matching their performance against decision strategy type. This study strongly suggests that, if more reliable decision models or expert systems are to be built, it will be necessary to obtain a more complete understanding of how well a certain strategy is modeled by a certain algorithm. Chung and Silver [21] and Chung and Tam [22] performed comparative analyses on learning algorithms.

## Data-Mining Techniques

An explicit comparison of data-mining techniques is not possible since each application has different goals and circumstances that require different data-mining techniques. Also, each data-mining technique has its inherent limitations as well as assumptions that limit its application to specific actual cases. According to Berry and Linoff [13], data-mining techniques are senselessly applied in many cases without prior consultation. Thus, it is worth reviewing the assumptions and advantages as well as limitations of data-mining techniques. This review of data-mining techniques is rather generalized and may not cover all contingencies.

The most widely and popularly used data-mining technique in bankruptcy prediction literature is discriminant analysis. In addition to its popularity in numerous studies, the strengths of discriminant analysis include: (1) the ability to incorporate multiple financial ratios simultaneously; (2) the provision of appropriate coefficients for combining the independent variables; and (3) ease of application once the initial model has been developed $[35, 67]$ . But the potential problems of discriminant analysis are categorized as: (1) violations of the underlying normality and independence assumptions of the classical linear regression or discriminant approaches that may negate analysis results, (2) reduction of dimensionality issues, (3) varied interpretation of the relative importance of individual variables, (4) difficulty of specifying the appropriate classification algorithm, and (5) properly interpreting time-series prediction tests $[5, 67]$ . In all its guises, discriminant analysis assumes the following: (1) variables describing the members of the group observations are multivariate normally distributed within each group; (2) group covariances are equal across all groups; and (3) groups are discrete, nonoverlapping, and identifiable. It is not easy to fulfill all three conditions in real situations and this is why discriminant analysis is vulnerable to methodological controversies $[4]$ .

In contrast, decision tree analysis requires only the last assumption. The other strengths of decision tree methods are:

1. Ability to generate understandable rules;

2. Performing classification without requiring much computation;

3. Ease of calculation at classification time;

4. Ability to handle both continuous and categorical variables;

5. Provision of a clear indication of which fields are the most important for prediction and classification [13].

There are, nevertheless, a number of weaknesses inherent in this approach as well. Some decision tree algorithms, for example, can only deal with binary-valued target classes and are thereby vulnerable to error in the case of many classes. Most decision tree algorithms only examine a single field at a time and lead to rectangular classification boxes that may not correspond well with the actual distribution of records in the decision space. Also, the process of growing a decision tree is computationally expensive to educate. Thus, decision tree methods are a good choice when the data-mining task is a classification of records or a prediction of outcomes. It is a natural choice when the goal is to generate rules that can be easily understood, explained, and translated into SQL or a natural language $[1]$ .

The most dominant data-mining technique at present, neural networks, has both advantages and disadvantages. Neural networks (1) can handle a wide range of problems, (2) produce good results even in complicated domains, (3) can handle both categorical and continuous variables, and (4) are available in many off-the-shelf packages. Even so, there are several problems with neural networks: (1) they require inputs in the range from 0 to 1; (2) they cannot explain the results; and (3) they may converge prematurely to an inferior solution.

Nevertheless, neural networks are a good choice for most classification and prediction tasks when the model's results are more important than understanding how the model itself works (because neural networks are opaque “black boxes,” it is difficult to extract rules from them). The only time neural networks do not work well is when there are many input features. A large number of features makes it more difficult for the network to find patterns, resulting in a long training phase that never converges to a good solution [1, 4, 13].

Recently, the genetic algorithm has emerged as another data-mining techniques $[33, 46]$ . The strengths of genetic algorithms are (1) that they produce explainable results as the genes contained in the genome; (2) it is easy to apply the results since they take the form of parameters in the fitness function; (3) they are able to handle a wide range of data types; (4) they allow application of optimization; and (5) they can be integrated with neural networks.

The weaknesses of genetic algorithms include (1) that they involve difficulty in encoding many problems because of fixed-length genomes; (2) they offer no guarantee of optimality, thus leading to a near-optium solution, not the best solution; (3) they are computationally expensive when the fitness function comprises multiple functions evaluated over a training set; and (4) their availability in commercial packages is limited.

Genetic algorithms are often incorporated into other packages. In particular, neural network packages are increasingly using the power of genetic algorithms to improve the performance of neural networks $[1, 13]$ . As described above, each data-mining technique has its own merits and disadvantages as well as suitable applications (Table 1). Therefore, a researcher's choice of data-mining technique should be determined by the specific objectives and concrete situations of the particular application, rather than just by its performance advantage.

Table 1 Advantages and Disadvantages of Data Mining Techniques

<table><tr><td>Techniques</td><td>Advantages</td><td>Disadvantages</td></tr><tr><td>Discriminant analysis</td><td>·Able to incorporate multiple financial ratios simultaneously·Able to combine independent variables·Easy to apply once the model has been developed</td><td>·Violations of normality and independence·Reduction of dimensionality·Difficulty interpreting relative importance·Difficulty specifying classification algorithm·Difficulty interpreting time-series prediction test</td></tr><tr><td>Decision tree</td><td>·Able to generate understandable rules·Able to perform in rule-oriented domains·Ease of calculation at classification time·Able to handle continuous and categorical variables·Able to indicate best fields clearly</td><td>·Error-prone with too many classes·Computationally expensive to train·Trouble with nonrectangular regions</td></tr><tr><td>Neural networks</td><td>·Versatile—able to handle a wide range of problems·Produce good results in complicated domains·Able to handle categorical and continuous variables·Available in many off-the-shelf packages</td><td>·Require inputs in the range of [0,1]·Cannot explain the results·May converge on an inferior solution</td></tr><tr><td>Genetic algorithms</td><td>·Produce explainable results·Results are easy to apply·Able to handle a wide range of data types·Applicable for optimization·Integrate well with neural networks</td><td>·Difficulty encoding·No guarantee of optimality·Computationally expensive·Available in few commercial packages</td></tr></table>

Recent data-mining studies add several new perspectives. Askira-Gelman [7] recognized the comprehensibility of the results as an important condition for the use of data-mining methods while Galal, Cook, and Holder [30] outlined a general approach for scaling data-mining systems using parallel and distributed resources. The case-specific approach using temporal data mining was examined by Spenceley and Warren [66] and interface with text data mining for web search design was described by Kawano and Hasegawa [36]. Piramuthu [51, 52] stressed the importance of preprocessing input data and suggested Hausdor-distance measure for feature selection in learning applications. Also, the introduction of a partially automated method for generating intentional answers at multiple abstraction levels for a query using data-mining approaches and development of consensus models for knowledge have been attempted [50, 76]. Collier et al. [23] developed a framework for evaluating data-mining tools and demonstrated the method's effectiveness.

## Dynamics of Modeling in Normal Versus Crisis Situations

A comprehensive review of the bankruptcy prediction literature found no study that attempted to develop a bankruptcy prediction model under crisis situations. This omission may be partly explained by the essentially stable economic situation in the world economy in the 1960s when bankruptcy prediction studies began. There was no need to build models for crisis conditions when none existed. A more plausible explanation for the oversight would be that most researchers believed it was not possible to build any usable prediction model for use in crisis situations, in which every variable is seen as uncertain. Nevertheless, there is a rich body of literature concerning crisis situations in other academic fields at hand, including organization theory and decision making.

Smart and Vertinsky [64, 65] undertook empirical studies that examined the relationship between the types of external environment in which a firm operates and the repertoire of strategic responses firms develop to cope with crises. This study indicated that economic crisis may affect how financial institutions operate, which in turn affects how they evaluate the credit status of corporations so as to minimize any loss from uncollectable or undercollectable loans due to bankruptcy. Bryson [17] argued that such crises open up five different kinds of “opportunity space” for decision makers. Expanded opportunity spaces involve, in effect, a relaxation of the “normal” constraints around decision making in organizations. In other words, different sets of constraints or rules should be applied to normal and crisis situations, which leads to the conclusion that a separate bankruptcy prediction model must be developed for each situation.

From a decision-making perspective, Billings, Milburin, and Schaalman $[14]$ reported that decision makers in crises show totally different behaviors and apply different decision-making models compared with normal situations due to increased uncertainties, the short reaction time, a hostile atmosphere, the high costs involved, mental pressure to make right decisions, the consequences of wrong decisions, and other such factors. Similar research results were also observed by Belardo et al. $[12]$ , who thus strongly recommended that decision-making models in crises should be radically different from those in normal situations and that new models ought to be designed to minimize the mental disturbance for decision makers as they adjust to new situations.

Currently, East Asia is suffering economic downturns, and an unprecedented number of corporations are filing for bankruptcy. To make matters worse, many financial institutions are being led astray by inaccurate bankruptcy prediction models designed under (and for) normal conditions $[10, 39]$ . Therefore, both the theoretical paucity of literature on crises and practical economic requirements call for the rapid development of suitable “crisis-based” bankruptcy prediction models.

Research Methodology

Data Collection

THE GOAL OF THIS STUDY IS TO DEVELOP TWO BANKRUPTCY PREDICTION models, one for use under normal economic conditions and another for use under crisis economic conditions. Korea was selected as the sample frame since it provided a natural setting for both conditions. While stable throughout most of the 1990s, economic crisis in Korea officially appeared in the fourth quarter of 1997 (even though there had been early warning signs since the second quarter). Because of the crisis, an International Monetary Funds (IMF) bailout package of standby credit was delivered in mid-December, albeit under harsh mandatory IMF restructuring agreements. Since then, an unprecedented number of corporations have gone bankrupt, because banks were reluctant to loan money causing firms to suffer from high interest rates, loans from abroad were similarly blocked, and strong labor unions hindered necessary layoffs.

For the sample in economic crisis, all bankrupt corporations from the second quarter of 1997 to the first quarter of 1998 from the Korea Stock Exchange (KSE) list were investigated. Bankrupt firms were referred to as an act of filing a petition for bankruptcy reported by the KSE. Under such a definition, seventy-five listed firms went bankrupt. For the purposes of this study, however, both “chaebol” companies and small firms were excluded from the sample, because chaebol companies showed totally obscure financial structures (due to mutual loan guarantees and manipulated financial statements) [76], and it was almost impossible to collect financial statements for small firms. Surprisingly, most of the bankrupt corporations were in manufacturing industries, with only two firms in service, one in financing, and two in construction. This uneven bankruptcy distribution across industries prohibited a cross-sectional study. Thus, only thirty manufacturing firms were included in this study. According to the same analytical profile, a total of fifty-six listed firms went bankrupt under “normal” economic conditions (considered from the second quarter of 1991 to the first quarter of 1995, when the Korean economy showed stable growth). After the application of the same screening procedure, twenty-nine bankrupt firms remained in the study.

As the control sample, each selected bankrupt firm was matched with one or two nonbankrupt firms by carefully comparing the year of the reported data, size of assets, and number of employees. The selected nonbankrupt corporations were within $\pm20$ percent of the selection criteria. Forty-nine and fifty-four nonbankrupt firms were selected for normal and crisis economic conditions, respectively. Table 2 presents the demographic profile of the sample. All financial data collected in this study were gathered directly from the KSE, the authoritative institution. The data were then double-checked with financial reports from the Bank of Korea and Korea Industrial Bank.

Table 2 Demographic Profile of Sample Corporations

<table><tr><td rowspan="2"></td><td colspan="3">Normal</td><td colspan="3">Crisis</td></tr><tr><td>Bankrupt</td><td>Nonbankrup t</td><td>Total</td><td>Bankrupt</td><td>Nonbankrup t</td><td>Total</td></tr><tr><td>N</td><td>29</td><td>49</td><td>78</td><td>30</td><td>54</td><td>84</td></tr><tr><td>Average assets* (std. dev.)</td><td>47.1(39.8)</td><td>44.8(29.1)</td><td>45.7(33.2)</td><td>112.8(61.3)</td><td>105.1(85.5)</td><td>107.8(74.4)</td></tr><tr><td>Average number of employees (std. dev.)</td><td>388(198)</td><td>442(231)</td><td>422(220)</td><td>379(238)</td><td>443(253)</td><td>420(248)</td></tr></table>

\* Units in billion Korean won

## Variable Selection and Data Validation

Through extensive literature review on bankruptcy prediction, fifty-six financial ratios were identified. After careful analysis of characteristics of each financial ratio, sixteen ratios were eliminated due to duplication. The final input variables were forty financial ratios categorized as growth, profitability, safety/leverage, activity/efficiency, and productivity. The appendix contains a detailed description of the variables. Again, financial ratios were collected from the KSE database and verified by actual calculations based on financial statements and other documents.

## Bankruptcy Prediction Model

As described above, the decision tree techniques were applied to build the models as well as to provide interpretation of bankruptcy prediction decisions for both normal and crisis situations. Multivariate discriminant analysis was used as the performance benchmark. Despite their excellent performance, neural networks were excluded because they are not able to explain the results.

## Multivariate Discriminant Analysis

From a total forty financial ratios (variables), a large number were found to be significant indicators of bankruptcy prediction. The stepwise procedure with the 10 percent significance level as entry and the 30 percent significance level as removal criteria was applied to select critical variables. In normal conditions, three variables were selected as the result of the stepwise procedure. The final discriminant function is as follows: $^{1}$

$$
Z = 0. 0 5 8 D 9 + 0. 0 6 2 F 6 - 0. 0 0 6 E 4 ^ {2}
$$

$$
(0. 8 1 2) ^ {3} \quad (0. 5 5 6) \quad (- 0. 3 8 1)
$$

where D9 = cash flow to total assets; F6 = productivity of capital; E4 = average turnover period for inventories; and Z = discriminant score.

On the comparison of means for three variables, it was observed that bankrupt firms showed lower cash flow to total assets, lower productivity of capital, and longer turnover period for inventories, while nonbankrupt corporations showed otherwise. This result matched the general belief of financial experts $[67, 72, 76]$ , which, in turn, showed the face validity of the prediction model. The means of discriminant scores for bankrupt and nonbankrupt groups were -1.21 and 0.71, respectively.

Under a crisis condition, three variables were also selected as the result of the same stepwise procedure. The final discriminant function is as follows:

$$
Z = 0. 0 5 3 D 8 + 0. 0 5 6 F 6 + 0. 0 1 4 D 3
$$

$$
(0. 8 2 9) \quad (0. 5 5 5) \quad (0. 4 1 6)
$$

where $D8 =$ cash flow to liabilities; $F6 =$ productivity of capital; and $D3 =$ fixed assets to stockholders' equity and long-term liabilities.

From comparing the means for the three variables, it was observed that bankrupt firms showed lower cash flow to liabilities, lower productivity of capital, and lower fixed assets to stockholders' equity and long-term liabilities, while nonbankrupt corporations showed otherwise. Again, the result showed face validity $[67, 72, 76]$ . The means of discriminant scores for bankrupt and nonbankrupt firms were -0.82 and 0.45, respectively.

## Validation

To validate the prediction accuracy, the original sample should be divided into two subsamples: training and test. The first is for training the model itself; the second is for cross-validation of the model. However, because of the small sample size in this study, difficulties arose from choosing the size of the test sample and checking the consistency of the prediction accuracy for different settings of two subsamples. To overcome these difficulties, a special technique called the jackknife method (sometimes referred to as Lachenbruch's holdout procedure) was applied to split the sample [42]. In the jackknife method, one case is excluded from the original sample and the model is trained based on the remaining sample. Then, the trained model predicts the excluded case. This procedure is repeated for each case. Each case's accuracy is summed over the entire sample. It is shown that the jackknife method provides nearly unbiased estimators of prediction accuracy [2]. The jackknife method was therefore applied to both the multivariate discriminant analysis and the decision tree technique to validate the study models' prediction accuracy.

## Decision Tree with Boosting

Decision tree induction approaches construct a decision tree using a training data set, where the tree is a simple recursive structure for representing a decision procedure in which a new case is assigned to one of the predefined classes. A nonterminal (interior) node in the tree represents a decision attribute value test, and a terminal (leaf) node denotes a decision class.

Hunt, Marin, and Stone $[34]$ introduced this concept, and Quinlan $[57]$ later modified it and developed the ID3 algorithm. C4.5 is a descendant of the ID3 and extended the original ID3 algorithm by accounting for unknown values, continuous attribute value range, tree pruning, and rule deviation $[41, 58, 59]$ . Because of its particular efficiency, simplicity, and popularity, C4.5 has formed the central component in several commercial packages and has been applied in various business domains such as high-performance funds classification $[47]$ , stock portfolio construction $[68]$ , and bank failure prediction $[69]$ .

In this study, C4.5 combined with the “confidence level” (CL) and “minimum number of cases” (MC) criteria were used as tree pruners to reduce the effects of noisy data. That is, the high value of these parameters usually restricts the tests that can be used near the leaves of the tree and usually produces a simpler decision tree, and hence leads to a smaller rule set. Figure 1 depicts the prediction accuracy with various levels of the CL (i.e., 0, 10, 20, and 30) and the MC (i.e., 1 through 7) in normal and crisis economic conditions. It was evident that the pruning significantly increased the overall prediction accuracy in economic crises, especially by increasing the MC. This result implied that the data collected in a crisis were more influenced by noise than data collected under normal conditions. It was also found that the prediction accuracy was maximized when the MC was set at 6 for normal and 7 for crisis conditions.

Table 3 shows the rules derived from these pruned trees, the reliability of the rules, and attributes forming the rules. Only the attribute “productivity of capital” played a key role in classifying cases regardless of economic conditions. “Cash flow to total assets” was a classifier in normal conditions but was replaced by “cash flow to liabilities” in crises, as was the case in multivariate discriminant analysis.

To improve prediction accuracy, the boosting technique was adopted $[59, 60]$ . The main idea of this technique is to construct several classifiers rather than just one. For example, the first classifier is constructed by the cases in the training data set, and then the second classifier is generated by paying more attention to those misclassified cases of the training set in the first classifier in an attempt to classify them correctly. This iterative process continues for a prespecified number of times. When a new case from a test data set is classified, each classifier votes for its prediction and the final class is determined by counting the votes $[20]$ . An additional six (“growth rate of property, plant, and equipment,” “gross profit to net sales,” “cash flow per share,” “stockholders’ equity to total assets,” “fixed assets to stockholders’ equity and long-term liabilities,” and “inventories turnover ratio”) and three (“operating income to net sales,” “ordinary income to stockholders’ equity,” and “fixed ratio”) attributes were found to improve the prediction accuracy in the process of the boosting. These additional attributes were not overlapped between the two models even though the same data-mining technique was applied.

(a) Normal Condition  
![](/api/attachments/9VQSWTF3/fulltext/images/ff2200f01768b3629eea2fcd291a888c70fa676a204f2c7ddf863fd162232094.jpg)

(b) Crisis  
![](/api/attachments/9VQSWTF3/fulltext/images/514ddd6b76273c88349726e7183fd946b8aaef52d69ddaa81fd66807775b3819.jpg)  
Figure 1. Prediction Accuracy at Various Levels of Pruning Parameters

## Analysis of Model Performance

Three statistical measures were applied to examine the predictive validity: percentage accuracy, chi-square, and sensitivity. Percentage accuracy shows the capability of each model in classifying cases correctly, chi-square measures the existence of structural dependency between the models, while sensitivity investigates the models' robustness. Table 4 presents the classification accuracy rates of the discriminant models. The models showed strong prediction power for nonbankrupt firms under both normal and crisis conditions (89.5 percent and 85.2 percent, respectively), but the accuracy rates for bankrupt corporations were low, especially in crisis conditions (69.0 percent for normal and 53.3 percent for crisis).

D3 = fixed assets to stockholders' equity and long-term liabilities; D8 = cash flow to liabilities; D9 = cash flow to total assets; F6 = productivity of capital.

Table 3 Rules Derived from Decision Trees

<table><tr><td rowspan="2">Economic conditions</td><td colspan="4">Rules</td></tr><tr><td>No.</td><td>Conditions</td><td>Predictions</td><td>Reliability*</td></tr><tr><td rowspan="3">Normal</td><td>1</td><td> $F6 > 19.65$ </td><td>Nonbankrupt</td><td>0.86</td></tr><tr><td>2</td><td> $D9 > -5.64$ </td><td>Nonbankrupt</td><td>0.95</td></tr><tr><td>3</td><td> $D9 \leq -5.64$  and  $F6 \leq 19.65$ </td><td>Bankrupt</td><td>0.84</td></tr><tr><td rowspan="4">Crisis</td><td>1</td><td> $F6 > 20.61$ </td><td>Nonbankrupt</td><td>0.91</td></tr><tr><td>2</td><td> $D8 > 2.64$ </td><td>Nonbankrupt</td><td>0.85</td></tr><tr><td>3</td><td> $D3 > 87.23$ </td><td>Nonbankrupt</td><td>0.86</td></tr><tr><td>4</td><td> $D8 \leq 2.64, F6 \leq D \ 20.61, \ and \ D3 \leq 87.23$ </td><td>Bankrupt</td><td>0.82</td></tr></table>

\* Confidence level of prediction for the rule.

Table 4 Prediction Accuracy of Discriminant Analysis

<table><tr><td rowspan="2">Economic conditions</td><td colspan="2">Prediction accuracy*</td><td rowspan="2">Overall accuracy</td><td rowspan="2">Key attributes</td></tr><tr><td>Bankrupt</td><td>Nonbankrupt</td></tr><tr><td>Normal</td><td>69.0%</td><td>89.8%</td><td>82.1%</td><td>D9, F6, E4</td></tr><tr><td>Crisis</td><td>53.3%</td><td>85.2%</td><td>73.8%</td><td>D8, F6, D3</td></tr></table>

\* Number of correctly predicted (bankrupt, nonbankrupt) cases / actual number of cases (bankrupt, nonbankrupt)] × 100.  
E4 = average turnover period for inventories; D3 = fixed assets to stockholders' equity and long-term liabilities; D8 = cash flow to liabilities; D9 = cash flow to total assets; F6 = productivity of capital.

The models and their corresponding performance of decision trees are presented in Table 5, which shows that the prediction accuracy rates were improved by boosting (i.e., 78.2 percent to 83.3 percent for normal and 79.5 percent to 81.0 percent for crisis conditions). These prediction accuracy rates were slightly higher than the discriminant model under normal conditions and quite better under crisis conditions. This level of performance was considered satisfactory compared with previous studies [6, 9, 26, 27, 33, 47, 49, 61, 69, 74]. Thus, decision tree models were employed in the following discussion as the final models.

Table 6 shows the performance comparison of both normal and crisis models applied to crisis conditions. When the normal model was applied in crisis situations, a nonbankruptcy case shows a slight decrease in prediction accuracy compared with the crisis prediction model's performance (from 88.9 percent to 81.5 percent). But, in the case of bankruptcy prediction, the accuracy of the normal model dropped significantly under crisis conditions (from 66.7 percent to 36.7 percent). Also, considering that the sample consisted of thirty bankrupt and fifty-four nonbankrupt firms (which means the blind guess is about 35.71 percent), the normal bankruptcy prediction model was almost useless as a predictor of bankruptcy under crisis conditions. Another performance measure, the chi-square statistic, was applied to investigate the goodness of fit test for homogeneity between crisis and normal model. The two models were significantly different, since the chi-square statistic of 46.07 exceeded the critical value at the 0.05 significant level (3.84). Therefore, the dynamic modeling in “normal” and “crisis” economic conditions is justified.

Table 5 Bankruptcy Models and Performance by Decision Trees

<table><tr><td rowspan="2">Economic conditions</td><td rowspan="2">MC</td><td rowspan="2">CL</td><td rowspan="2">No. of boosting</td><td colspan="2">Prediction accuracy*</td><td rowspan="2">Overall ac- curacy</td><td colspan="2">Attributes</td></tr><tr><td>Bankrupt</td><td>Non- bankrupt</td><td>Major</td><td>Additional</td></tr><tr><td>Normal</td><td>1</td><td>0</td><td>3</td><td>72.4%</td><td>90.0%</td><td>83.3%</td><td>D9, F6</td><td>B2, C1, C13, D1, D3, E3</td></tr><tr><td>Crisis</td><td>8</td><td>20</td><td>2</td><td>66.7%</td><td>88.9%</td><td>81.0%</td><td>D8, F6, D3</td><td>C2, C8, D2</td></tr></table>

\* [Number of correctly predicted (bankrupt, nonbankrupt) cases / actual number of cases (bankrupt, nonbankrupt)] × 100.  
B2 = growth rate of property, plant, and equipment; C1 = gross profit to net sales; C2 = operating income to net sales; C8 = ordinary income to stockholder's equity; C13 = cash flow per share; D1 = stockholder's equity to total assets; D2 = fixed ratio; D3 = fixed assets to stockholders' equity and long-term liabilities; E3 = inventories turnover ratio.

Table 6 Performance Comparison of Models Applied to Crisis Conditions

<table><tr><td rowspan="2">Applied models</td><td colspan="2">Prediction accuracy*</td><td rowspan="2">Overall accuracy</td></tr><tr><td>Bankrupt</td><td>Nonbankrupt</td></tr><tr><td>Normal</td><td>36.7%</td><td>81.5%</td><td>65.5%</td></tr><tr><td>Crisis</td><td>66.7%</td><td>88.9%</td><td>81.0%</td></tr><tr><td colspan="4">Chi-square statistic = 46.07, p &lt; 0.0001.</td></tr></table>

To evaluate the performance of models further, sensitivity analysis was performed. Sensitivity is defined as a proportion of correctly predicted cases among the actual bankruptcy cases. This performance measure is important since misclassification of bankrupt corporations as nonbankrupt is a more serious mistake than the opposite. Low sensitivity means more “death” penalties to “innocent” firms. The sensitivity with a different setting of cutoff value (sometimes referred to as threshold value) is shown in figure 2. With low cutoff value, the predictive accuracy rate for bankruptcy becomes high, while the predictive accuracy rate for nonbankruptcy becomes low. Hence, there is a tradeoff between two accuracy rates. The cutoff value used for the final model was the one that maximized the overall accuracy. With the range of cutoff value from 0.1 and 0.7, which was the range of interest in our study, the crisis model was significantly superior to the normal model. Also, the sensitivity of the normal model was close to the blind guess line (35.7 percent) when the cutoff value is between 0.1 and 0.6. Thus, the need for different models in normal and crisis economic conditions was once again clearly demonstrated.

![](/api/attachments/9VQSWTF3/fulltext/images/f83d29ddbfcd7a8631c40b8f5a62734fcbc950bf64bc11e00c12f9ae94ff1e2b.jpg)  
Figure 2. Sensitivity Analysis of Models

## Discussion and Implications

THE BANKRUPTCY PREDICTION MODELS DERIVED FROM THE DECISION TREE technique had the most interpretive power $[1, 13]$ . The prediction model for normal economic conditions showed “cash flow to total assets” and “productivity of capital” to be the most important variables, while “cash flow to liabilities,” “productivity of capital,” and “fixed assets to stockholders equity and long-term liabilities” were the vital variables for crisis conditions (Table 4). “Cash flow” and “productivity of capital” were found to be the common critical variables in both models. “Cash flow” has been the most cited key variable in the bankruptcy prediction literature including Beaver $[11]$ , Blum $[15, 16]$ , Deakin $[24, 25]$ , and Edminister $[28]$ . Furthermore, Casey and Bartczak $[18, 19]$ reported that “cash flow” together with other financial ratios provided better prediction accuracy and subsequent studies reinforced this finding $[8, 31, 32, 72]$ . Thus, the prediction models developed in this study verified this universal importance of “cash flow” in predicting bankruptcy.

Surprisingly, two other key variables employed in this study, “productivity of capital” and “fixed assets to stockholders’ equity and long-term liabilities,” rarely appeared in the literature. To investigate this result, an expert panel was formed consisting of three financial specialists who have at least fifteen years experience (such panel studies are considered to be quite powerful for interpreting similar research results [18, 19, 43]). The expert panel unanimously picked “productivity of capital” as the most critical variable to differentiate troubled firms from the rest. “Productivity of capital” measures “gross valued added” per capital. Thus, it indicates how much capital is being contributed to the firm and is the key variable checking viability of the firm. In other words, if this ratio is low, it is safe to infer that the firm is losing its competitiveness.

"Fixed assets to stockholders' equity and long-term liabilities" emerged as the key variable in crisis conditions. This ratio refers to how reliable or safe the firm is in funding fixed assets. If this ratio is too high, the firm is suffering from a scarcity of current assets and will not be able to pay back short-term loans. But if this ratio is too low, the firm is not efficiently utilizing the capital since there are excessive current assets. The threshold of 100 percent is applicable in general [76]. This ratio is critical for financial institutions to decide whether firms are able to pay back the loans, especially in situations of economic downturn.

“Cash flow to total assets” in normal conditions was replaced by “cash flow to liabilities” in crisis conditions. This change reflects the fact that the more sensitive ratio is more applicable to crisis situations since “cash flow to liabilities” is more volatile than “cash flow to total assets.” Thus, it is safe to infer that sensitivity, viability, and efficiency are the most important factors to predict bankruptcy in crisis conditions.

The need for developing different bankruptcy prediction models suitable for normal and crisis economic conditions were justified by this study. This, together with the sensitivity issue of performance, leads to the following suggestions on data-mining modeling: First, data mining is very much data-oriented without a strong theoretical background $[13]$ . So data-mining models tend to be very sensitive to changes of data or situations. Thus, it is evident that this nonrobustness of data-mining modeling requires continuous remodeling as data or situation changes. Second, performance of data-mining models/algorithms varies across different task domains. This interaction between task domain and model/algorithm is clearly demonstrated by Kim, Chung, and Paradice $[37]$ . Therefore, researchers should take relationships among task domain, performance, and modeling algorithm more seriously into account. Third, there should be more valid and reliable performance measures. Percentage accuracy has been the most dominant performance measure but does not show how close the classification is. Borderline classification is where the decision maker should pay much more attention, since there is a great risk of misclassification, which can lead to disastrous results. Fourth, data-mining techniques have inherent advantages and disadvantages as well as assumptions that may limit applications of certain techniques to certain cases. Therefore, the choice of data-mining models/algorithms should be determined by the specific objectives and concrete situations of particular applications, rather than just by performance advantage.

## Summary and Conclusions

THE PRIMARY PURPOSE OF THIS PAPER WAS TO DEVELOP bankruptcy prediction models suitable for normal and crisis economic conditions and to observe the dynamics of model change from normal to crisis conditions. Its secondary purpose was to provide as much interpretation as possible concerning bankruptcy classifications. Thirty bankrupt firms from the second quarter of 1997 to the first quarter of 1998 were selected as crisis samples, and twenty-nine bankrupt firms from the second quarter of 1991 to the first quarter of 1995 were chosen as normal samples. As control samples, forty-nine and fifty-four nonbankrupt firms were selected for normal and crisis economic conditions by matching the year of the reported data, assets size, and the number of employees of respective bankrupt firms within ±20 percent of the selection criteria.

Under normal conditions, the bankruptcy prediction model using the decision tree model with boosting technique revealed that the major variables in predicting the bankruptcy of the sample firms were “cash flow to total assets” and “productivity of capital.” If the “cash flow to total assets” ratio was greater than -5.64 percent or “productivity of capital” was greater than 19.65 percent, then the firm was not expected to go bankrupt; otherwise it was predicted that it would go bankrupt. Under crisis conditions, “cash flow to liabilities,” “productivity of capital,” and “fixed assets to stockholders’ equity and long-term liabilities” became the three major variables in bankruptcy prediction modeling. The usual interpretation was that if the “cash flow to liabilities” ratio was greater than 2.64 percent, or “productivity of capital” was greater than 20.61 percent, or “fixed assets to stockholders’ equity and long-term liabilities” was greater than 87.23 percent, then the firm was not expected to go bankrupt; otherwise, it was predicted to go bankrupt. The accuracy of the final prediction model in normal conditions was 72.4 percent for bankruptcy and 90.0 percent for nonbankruptcy, while it was 66.7 percent and 88.9 percent, respectively, under crisis conditions. The level of accuracy obtained was comparable to other research [6, 9, 26, 27, 33, 47, 49, 61, 69, 74], and interpretation of the model itself and rules for classification were provided at the same time. When the normal model was applied in crisis situations, prediction accuracy dropped significantly in the case of bankruptcy classification (from 66.7 percent to 36.7 percent) to the level of a blind guess (35.71 percent). Therefore, the need for a different model in crisis economic conditions is justified.

A number of limitations in this study must be noted, however. First, the sample size was relatively small and not cross-sectional in nature, since the sample was restricted to manufacturing industries. Thus, the generalizability of the research results is somewhat limited. The second limitation is that only financial ratio variables were included. There may be other important key quantitative variables (e.g., stock data, market value, age, and size) as well as qualitative variables (leadership, reputation, type of ownership, etc.), and there is a rich literature in organization theory reporting the importance of these variables. Finally, cost analysis was not applied. It is important to measure actual monetary implications of misclassification rather than just accuracy. If the cost of misclassification is five times greater, then the prediction model should be readjusted to reflect such a weight.

These limitations open up a wide opportunity for future research. The bankruptcy prediction models developed in this study can be revalidated with a large number of samples and in different industries for both normal and crisis economic conditions. Prediction models applied across different nations could be developed and compared. More quantitative and qualitative variables could also be included to the model for better prediction and/or less misclassification based on the cost factor. In any case, an important foundation has been provided by the study for improved bankruptcy prediction under crisis conditions.

## NOTES

1. Coefficients of the discriminant function were estimated using the SAS DISCRIM procedure.

2. This function is based on the entire original sample.

3. Numbers in parentheses represent the standardized coefficient of the discriminant coefficient.

## REFERENCES

1. Adriaans, P., and Zantinge, D. Data Mining. Harlow, UK: Addison-Wesley, 1996.

2. Afifi, A., and Clark, V. Computer-Aided Multivariate Analysis. New York: Van Nostrand Reinhold, 1990.

3. Altman, E. Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. Journal of Finance, 23, 3 (September 1968), 589–609.

4. Altman, E. Corporate Financial Distress and Bankruptcy. New York: John Wiley and Sons, 1993.

5. Altman, E.; Haldeman, R.; and Narayanan, P. ZETA analysis: a new model to identify bankruptcy risk of corporations. Journal of Banking and Finance, 1, 1 (January 1977), 29–54.

6. Altman, E.; Macro, G.; and Varetto, R. Corporate distress diagnosis comparisons using linear discriminant analysis and neural networks. Journal of Banking and Finance, 18, 3 (1994), 505–529.

7. Askira-Gelman, I. Knowledge discovery: comprehensibility of the results. The Thirty-First Hawaii International Conference on Systems Science, vol. 5. IEEE Computer Society (1998), pp. 247–255.

8. Aziz, A., and Lawson, G. Cash flow reporting and financial distress modeling: testing of hypothesis. Financial Management, 1, 2 (1989), 55–63.

9. Back, B.; Laitinen, P.; and Sere, K. Neural network and genetic algorithms for bankruptcy predictions. Proceedings of the Third World Congress on Expert Systems. Korea Expert Systems Association (1996), pp. 123–130.

10. Bank of Korea. Financial Statement Analysis. Seoul: Bank of Korea Press, 1997.

11. Beaver, W. Financial ratios as predictors of failures. Empirical Research in Accounting, selected studies supplement to the Journal of Accounting Research, 4, 1 (1966), 71–127.

12. Belardo, S.; Pazer, H.; Wallace, W.; and Danko, W. Simulation of a crisis management information network: a serendipitous evaluation. Decision Sciences, 14, 4 (Fall 1983), 588–606.

13. Berry, M., and Linoff, G. Data Mining Techniques: For Marketing, Sales, and Customer Support. New York: John Wiley and Sons, 1997.

14. Billings, R.; Milburin, T.; and Schaalman, M. A model of crisis perception: a theoretical and empirical analysis. Administrative Science Quarterly, 25, 2 (June 1980), 300–316.

15. Blum, M.P. Failing company discriminant analysis. Journal of Accounting Research, 12, 1 (1974), 1–25.

16. Blum, M.P. The failing company doctrine. Boston College Industrial and Commercial Review, 16 (1974), 13–31.

17. Bryson, J. A perspective on planning and crises in the public sector. Strategic Management Journal, 1, 2 (April–June 1981), 181–196.

18. Casey, C., and Bartczak, N. Cash flow, it's not the bottom line. Harvard Business Review, 69, 4 (July–August 1984), 60–66.

19. Casey, C., and Bartczak, N. Using operating cash flow data to predict financial distress: some extensions. Journal of Accounting Research, 23, 1 (Spring 1985), 384–401.

20. Chang, N., and Sheng, O.L. Automated decision rule discovery from domains with joint decision outcomes: a decision tree induction approach. Proceedings of the Third International Conference of the ISDSS, vol. 2. Phoenix, AZ: Elsevier, 1995, pp. 259–267.

21. Chung, H.M., and Silver, M.S. Rule-based expert systems and linear models: an empirical comparison of learning-by-examples methods. Decision Sciences, 23, 3 (1992), 687–707.

22. Chung, H.M., and Tam, K.Y. A comparative analysis of inductive learning algorithms. International Journal of Intelligent Systems in Accounting, Finance and Management, 2, 1 (1994), 3–18.

23. Collier, K.; Carey, B.; Sautter, D.; and Marjaniemi, A. A methodology for evaluating and selecting data mining software. Thirty-Second Hawaii International Conference on Systems Science. Honolulu: IEEE Computer Society, 1999.

24. Deakin, E.B. A discriminant analysis of predictors of business failure. Journal of Accounting Research, 10, 1 (Spring 1972), 167–179.

25. Deakin, E.B. Business failure prediction: an empirical analysis. In E. Altman and A Sametz (eds.), Financial Crises: Institutions and Markets in a Fragile Environment. New York: John Wiley, 1977, pp. 117–138.

26. Dutta, S., and Shekhar, S. Bond rating: a non-conservative application of neural networks. IEEE Proceedings of the International Conference on Neural Networks, 11 (1988), 567–576.

27. Dutta, S.; Shekhar, S.; and Wong, W.Y. Decision support in non-conservative domains: generalization with neural networks. Decision Support Systems, 11, 5 (1994), 527–544.

28. Edminster, R.O. An empirical test of financial ratio analysis for small business failure prediction. Journal of Financial and Quantitative Analysis, 7, 1 (March 1972), 1477–1493.

29. Frydman, H.; Altman, E.; and Kao, D. Introducing recursive partitioning for financial classification: the case of financial distress. Journal of Finance, 40, 1 (1985), 269–291.

30. Galal, G.; Cook, D.J.; and Holder, L.B. Exploiting parallelism in knowledge discovery systems to improve scalability. Thirty-First Hawaii International Conference on Systems Science, 5 (1998), 256–265.

31. Gentry, J.; Newbold, P.; and Whitford, D. Classifying bankruptcy firms with funds flow components. Journal of Accounting Research (Spring 1985), 146–160.

32. Gentry, J.; Newbold, P.; and Whitford, D. Bankruptcy, working capital, and funds flow. Managerial Finance, 10, 3–4 (1985), 177–194.

33. Goldberg, D.E. Genetic Algorithms in Search, Optimization and Machine Learning. Reading, MA: Addison-Wesley, 1989.

34. Hunt, E.; Martin, J.; and Stone, P. Experiments in Induction. New York: Academic Press, 1966.

35. Johnson, R., and Wichern, D. Applied Multivariate Statistical Analysis. Englewood Cliffs, NJ: Prentice-Hall, 1992.

36. Kawano, H., and Hasegawa, T. Mondou: interface with text data mining for web search engine. Thirty-First Hawaii International Conference on Systems Science, 5 (1998), 275–283.

37. Kim, C.N.; Chung, H.M.; and Paradice, D.B. Inductive modeling of expert decision making in loan evaluation: a decision strategy perspective. Decision Support Systems, 21, 2 (1997), 83–98.

38. Klimasauskas, C. Applying neural networks. In R.R. Trippi and E. Turban (eds.), Neural Networks In Finance and Investing. New York: PROBUS, 1993, pp. 47–72.

39. Korea Industrial Bank. Financial Management. Seoul: Korean Industrial Bank Press, 1997.

40. Korobow, L., and Stuhr, D. Performance measurement of early warning models. Journal of Banking and Finance, 9, 2 (1985), 267–273.

41. Kufrin, R. Generating C4.5 production rules in parallel. Proceedings of the Fourteenth National Conference on Artificial Intelligence (AAAI–97), American Association for Artificial Intelligence, July 1997, pp. 565–570.

42. Lachenbruch, P., and Mickey, M. Estimation of error rates in discriminant analysis. Technometrics, 10, 1 (1968), 1–11.

43. Libby, R. Accounting ratios and the prediction of failure: some behavioral evidence. Journal of Accounting Research, 13, 1 (Spring 1975), 150–161.

44. Martin, D. Early warning of bank failure, a logit regression approach. Journal of Banking and Finance, 1, 3 (1977), 249–276.

45. Messier, W.F., and Hansen, J. Inducing rules for expert system development: an example using default and bankruptcy data. Management Science, 34, 12 (1988), 1403–1415.

46. Michalewicz, Z. Genetic Algorithms + Data Structures = Evolution Programs. New York: Springer-Verlag, 1984.

47. Norris, R.C. Classifying high performance mutual funds: a comparison of C4.5, LDA & logit. Proceedings of the International Conference on INFORMS, May 1996, pp. 152–159.

48. Odom, M.D., and Sharda, R. A neural network model for bankruptcy prediction. Proceedings of IEEE International Conference on Neural Networks, 1990, pp. 151–173.

49. Ohlson, J. Financial ratios and the probabilistic prediction of bankruptcy. Journal of Accounting Research, 18, 1 (1980), 109–131.

50. O'Leary, D.E. Models of consensus for knowledge acquisition. Thirty-Second Hawaii International Conference on Systems Science, 1999.

51. Piramuthu, S. Evaluating feature selection methods for learning in data mining applications. Thirty-First Hawaii International Conference on Systems Science, vol. 5, 1998, pp. 294–301.

52. Piramuthu, S. The Hausdor\_Distance measure for feature selection in learning applications. Thirty-Second Hawaii International Conference on Systems Science, 1999.

53. Platt, H.D., and Platt, M.B. Development of stable predictive variables: the case of bankruptcy prediction. Journal of Business Finance and Accounting, 17, 1 (1990), 31–44.

54. Platt, H.D., and Platt, M.B. A note on the use of industry-relative ratios in bankruptcy prediction. Journal of Business Finance, 1, 5–6 (December 1991), 1183–1194.

55. Quilnan, J. Discovering rules by induction from large collection of examples. In D. Michie (ed.), Expert Systems in the Micro Electronic Age. Edinburgh: Edinburgh University Press, 1979, pp. 168–201.

56. Quilnan, J. Learning efficient classification procedures and their applications to chess end games. In R.S. Cichalski, J. Carbonell, and T. Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach. Palo Alto: CA: Tioga, 1983, pp. 463–482.

57. Quinlan, J.R. Induction of decision trees. Machine Learning, 1 (1986), 81–106.

58. Quinlan, J.R. C4.5: programs for machine learning. San Mateo, CA: Morgan Kaufmann, 1993.

59. Quinlan, J.R. Improved use of continuous attributes in C4.5. Journal of Artificial Intelligence Research, 4 (1996), 77–90.

60. Quinlan, J.R. Bagging, boosting, and C4.5. Proceedings of the Thirteenth National Conference on Artificial Intelligence (AAAI–96), American Association for Artificial Intelligence, August 1996, pp. 725–730.

61. Rahimain, E.; Sing, S.; Thammachote, T.; and Virmani, R. Bankruptcy prediction by neural network. In R.R. Trippi and E. Turban (eds.), Neural Networks in Finance and Investing. New York: PROBUS, 1993, pp. 159–176.

62. Scott, J. The probability of bankruptcy: a comparison of empirical predictions and theoretical models. Journal of Banking and Finance, 5, 3 (September 1981), 317–344.

63. Sinkey, J. A multivariate statistical analysis of the characteristics of problem banks. Journal of Finance, 47, 1 (March 1975), 21–36.

64. Smart, C., and Vertinsky, I. Designs for crisis decision units. Administrative Science Quarterly, 22, 4 (December 1977), 640–677.

65. Smart, C., and Vertinsky, I. Strategy and environment: a study of corporate responses to crisis. Strategic Management Journal, 5, 3 (July–September 1984), 199–214.

66. Spenceley, S.E., and Warren, J.R. The intelligent interface for on-line electronic medical records using temporal data mining. Thirty-First Hawaii International Conference on Systems Science, vol. 5, 1998, pp. 266–274.

67. Stickney, C. Financial reporting and statement analysis: a strategy perspective. New York: Dryden Press, 1996.

68. Tam, K., and Chi, R. Inducing stock screening rules for portfolio construction. Journal of Operations Research Society, 8, 2 (1991), 168–182.

69. Tam, K., and Kiang, M. Managerial applications of neural networks: the case of bankruptcy Predictions. Management Science, 38, 7 (July 1992), 926–947.

70. Weiss, L. Bankruptcy prediction: a methodological and empirical update. Working paper, Tulane, OK, Freeman School of Business, 1981.

71. West, R.G. A factor-analytic approach to bank condition. Journal of Banking and Finance, 9, 2 (1985), 253–266.

72. White, G.; Sondhi, A.; and Fried, D. The Analysis and Use of Financial Statements. New York: John Wiley and Sons, 1994.

73. Wilcox, J. A simple theory of financial ratios as predictors of failures. Journal of Accounting Research, 9, 3 (Autumn 1971), 389–395.

74. Wilson, R.L., and Sharda, R. Bankruptcy prediction using neural networks. Decision Support Systems, 11, 5 (1994), 545–557.

75. Yoon, S., and Park, E.K. An approach to intentional query answering at multiple abstraction levels using data mining approaches. The Thirty-Second Hawaii International Conference on Systems Science, 1999.

76. Yoon, J.S.; Yoon, J.O.; Chung, B.S.; and Park, S.M. Financial Accounting. Seoul: Hakmoonsa, 1997.

77. Zavgren, C.V.; Dugan, M.T.; and Reeve, J.M. The association between probabilities of bankruptcy and market responses: a test of market anticipation. Journal of Business Finance and Accounting, 15, 1 (Spring 1988), 19–45.

78. Zmijewski, M.E. Methodological issues related to the estimation of financial distress prediction models. Journal of Accounting Research, 22, 1 (1984), 59–82.

APPENDIX: Description of Research Variables

<table><tr><td>Category</td><td>Denotation</td><td>Description</td></tr><tr><td rowspan="5">Growth</td><td>B1</td><td>Growth rate of total assets</td></tr><tr><td>B2</td><td>Growth rate of property, plant, and equipment</td></tr><tr><td>B3</td><td>Growth rate of current assets</td></tr><tr><td>B4</td><td>Growth rate of sales</td></tr><tr><td>B5</td><td>Growth rate of net income</td></tr><tr><td rowspan="13">Profitability</td><td>C1</td><td>Gross profit to net sales</td></tr><tr><td>C2</td><td>Operating income to net sales</td></tr><tr><td>C3</td><td>Ordinary income to net sales</td></tr><tr><td>C4</td><td>Net income to net sales</td></tr><tr><td>C5</td><td>Operating income to total assets</td></tr><tr><td>C6</td><td>Ordinary income to total assets</td></tr><tr><td>C7</td><td>Net income to total assets</td></tr><tr><td>C8</td><td>Ordinary income to stockholders' equity</td></tr><tr><td>C9</td><td>Net income to stockholders' equity</td></tr><tr><td>C10</td><td>Dividend ratio</td></tr><tr><td>C11</td><td>Dividends to net income</td></tr><tr><td>C12</td><td>Earnings per share</td></tr><tr><td>C13</td><td>Cash flow per share</td></tr><tr><td rowspan="9">Safety/leverage</td><td>D1</td><td>Stockholders' equity to total assets</td></tr><tr><td>D2</td><td>Fixed ratio</td></tr><tr><td>D3</td><td>Fixed assets to stockholders' equity and long-term liabilities</td></tr><tr><td>D4</td><td>Current ratio</td></tr><tr><td>D5</td><td>Quick ratio</td></tr><tr><td>D6</td><td>Debt ratio</td></tr><tr><td>D7</td><td>Interest coverage ratio</td></tr><tr><td>D8</td><td>Cash flow to liabilities</td></tr><tr><td>D9</td><td>Cash flow to total assets</td></tr><tr><td rowspan="6">Activity/efficiency</td><td>E1</td><td>Total assets turnover ratio</td></tr><tr><td>E2</td><td>Stockholders' equity turnover ratio</td></tr><tr><td>E3</td><td>Inventories turnover ratio</td></tr><tr><td>E4</td><td>Average turnover period for inventories</td></tr><tr><td>E5</td><td>Receivables turnover ratio</td></tr><tr><td>E6</td><td>Average collection period for receivables</td></tr><tr><td rowspan="8">Productivity</td><td>F1</td><td>Gross value added</td></tr><tr><td>F2</td><td>Productivity of labor</td></tr><tr><td>F3</td><td>Ordinary income per employee</td></tr><tr><td>F4</td><td>Net income per employee</td></tr><tr><td>F5</td><td>Total assets per capital</td></tr><tr><td>F6</td><td>Productivity of capital</td></tr><tr><td>F7</td><td>Gross value added to net sales</td></tr><tr><td>Class</td><td>{Bankrupt, nonbankrupt}</td></tr></table>

![](/api/attachments/9VQSWTF3/fulltext/images/85ecb8ca7ffb687228d181aaa6590aff9cc7d37407f6881a2baa728264a1203c.jpg)

# Foundations of Information Systems

Vladimir Zwass, Fairleigh Dickinson University
ISBN: 0697133125

Instructor's Supplements: Instructor's Manual, Test Bank, Computerized Test Bank, PowerPoint® Classroom Presentation Software, available on Instructor CD ROM.

Comprehensive, interesting, authoritative, and highlighting the vital aspects of today's business and technological environments, Vladimir Zwass' Foundations of Information Systems will help you take your students into the 21st century.

The text is built around six principal themes: transformation of business processes with information systems, strategic use of information systems, organizational knowledge management, Internet-based electronic commerce, information systems in business globalization, and quality management. The most recent organizational experience and literature are invoked to cover these themes in depth within a strong overall IS framework.

Zwass introduces students to the fundamental concepts of information systems by showing their varied applications in business life. Emphasis is placed on business processes that can be redesigned using the capabilities of IS to reach new heights of performance and achieve a superior long-term competitive position. Each chapter begins with a real-world minicase and ends with an extensive real-world case. “Spotlight” boxes throughout reveal exactly how an actual entrepreneur, company leader, or knowledge worker used IT/IS to achieve business results. Alive with carefully selected examples of success and failure, the text is both exciting and instructive.

To order your complimentary copy, simply call 1-800-338-3987.
